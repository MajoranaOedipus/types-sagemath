r"""
Interface to GAP

Sage provides an interface to the GAP system. This system provides
extensive group theory, combinatorics, etc.

The GAP interface will only work if GAP is installed on your
computer; this should be the case, since GAP is included with Sage.
The interface offers three pieces of functionality:


#. ``gap_console()`` -- a function that dumps you into
   an interactive command-line GAP session.

#. ``gap(expr)`` -- evaluation of arbitrary GAP
   expressions, with the result returned as a string.

#. ``gap.new(expr)`` -- creation of a Sage object that
   wraps a GAP object. This provides a Pythonic interface to GAP. For
   example, if ``f=gap.new(10)``, then
   ``f.Factors()`` returns the prime factorization of
   `10` computed using GAP.


First Examples
--------------

We factor an integer using GAP::

    sage: n = gap(20062006); n
    20062006
    sage: n.parent()
    Gap
    sage: fac = n.Factors(); fac
    [ 2, 17, 59, 73, 137 ]
    sage: fac.parent()
    Gap
    sage: fac[1]
    2

GAP and Singular
----------------

This example illustrates conversion between Singular and GAP via
Sage as an intermediate step. First we create and factor a Singular
polynomial.

::

    sage: singular(389)
    389
    sage: R1 = singular.ring(0, '(x,y)', 'dp')
    sage: f = singular('9*x^16-18*x^13*y^2-9*x^12*y^3+9*x^10*y^4-18*x^11*y^2+36*x^8*y^4+18*x^7*y^5-18*x^5*y^6+9*x^6*y^4-18*x^3*y^6-9*x^2*y^7+9*y^8')
    sage: F = f.factorize()
    sage: print(F)
    [1]:
       _[1]=9
       _[2]=x^6-2*x^3*y^2-x^2*y^3+y^4
       _[3]=-x^5+y^2
    [2]:
       1,1,2

Next we convert the factor `-x^5+y^2` to a Sage
multivariate polynomial. Note that it is important to let
`x` and `y` be the generators of a polynomial ring,
so the eval command works.

::

    sage: R.<x,y> = PolynomialRing(QQ,2)
    sage: s = F[1][3].sage_polystring(); s
    '-x**5+y**2'
    sage: g = eval(s); g
    -x^5 + y^2

Next we create a polynomial ring in GAP and obtain its
indeterminates::

    sage: R = gap.PolynomialRing('Rationals', 2); R
    PolynomialRing( Rationals, ["x_1", "x_2"] )
    sage: I = R.IndeterminatesOfPolynomialRing(); I
    [ x_1, x_2 ]

In order to eval `g` in GAP, we need to tell GAP to view
the variables ``x0`` and ``x1`` as the two
generators of `R`. This is the one tricky part. In the GAP
interpreter the object ``I`` has its own name (which
isn't ``I``). We can access its name using
``I.name()``.

::

    sage: _ = gap.eval("x := %s[1];; y := %s[2];;"%(I.name(), I.name()))

Now `x_0` and `x_1` are defined, so we can
construct the GAP polynomial `f` corresponding to
`g`::

    sage: R.<x,y> = PolynomialRing(QQ,2)
    sage: f = gap(str(g)); f
    -x_1^5+x_2^2

We can call GAP functions on `f`. For example, we evaluate
the GAP ``Value`` function, which evaluates `f`
at the point `(1,2)`.

::

    sage: f.Value(I, [1,2])
    3
    sage: g(1,2)        # agrees
    3

Saving and loading objects
--------------------------

Saving and loading GAP objects (using the dumps method, etc.) is
*not* supported, since the output string representation of Gap
objects is sometimes not valid input to GAP. Creating classes that
wrap GAP objects *is* supported, via simply defining the a
_gap_init_ member function that returns a string that when
evaluated in GAP constructs the object. See
``groups/perm_gps/permgroup.py`` for a nontrivial
example of this.

Long Input
----------

The GAP interface reads in even very long input (using files) in a
robust manner, as long as you are creating a new object.

.. NOTE::

   Using ``gap.eval`` for long input is much less robust, and is not
   recommended.

::

    sage: t = '"%s"'%10^10000   # ten thousand character string.
    sage: a = gap(t)

Changing which GAP is used, and how
-----------------------------------

Set the environment variable :envvar:`SAGE_GAP_COMMAND` to specify
how GAP executable is called. E.g.  ::

  $ SAGE_GAP_COMMAND = "/usr/local/bin/gap -s 4G" ./sage

will use GAP installed in `/usr/local/bin`, with 4Gb RAM.


Set the environment variable :envvar:`SAGE_GAP_MEMORY` to specify the amount
of RAM allocated to :mod:`~sage.libs.gap.libgap` and to the GAP executable.
If :envvar:`SAGE_GAP_COMMAND` is set, as well, then
:envvar:`SAGE_GAP_MEMORY` is only used for `libgap`. ::

    sage: gap.eval('GAPInfo.CommandLineOptions.s') # not tested
    '"42m"'

After the GAP interface initialisation, setting :envvar:`SAGE_GAP_MEMORY`
has no effect::

    sage: os.environ['SAGE_GAP_MEMORY'] = '24M'
    sage: gap.eval('GAPInfo.CommandLineOptions.s') # not tested
    '"4g"'


AUTHORS:

- David Joyner and William Stein: initial version(s)

- William Stein (2006-02-01): modified gap_console command so it uses
  exactly the same startup command as Gap.__init__.

- William Stein (2006-03-02): added tab completions: gap.[tab], x =
  gap(...), x.[tab], and docs, e.g., gap.function? and x.function?
"""
import sage.interfaces.abc
from sage.cpython.string import bytes_to_str as bytes_to_str
from sage.env import GAP_ROOT_PATHS as GAP_ROOT_PATHS, SAGE_EXTCODE as SAGE_EXTCODE, SAGE_GAP_COMMAND as SAGE_GAP_COMMAND, SAGE_GAP_MEMORY as SAGE_GAP_MEMORY
from sage.interfaces.expect import Expect as Expect, ExpectElement as ExpectElement, ExpectFunction as ExpectFunction, FunctionElement as FunctionElement
from sage.interfaces.gap_workspace import gap_workspace_file as gap_workspace_file, prepare_workspace_dir as prepare_workspace_dir
from sage.interfaces.tab_completion import ExtraTabCompletion as ExtraTabCompletion
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.instancedoc import instancedoc as instancedoc
from sage.misc.misc import is_in_string as is_in_string
from sage.structure.element import ModuleElement as ModuleElement

WORKSPACE: str
first_try: bool
gap_cmd: str

def gap_command(use_workspace_cache: bool = True, local: bool = True): ...

class Gap_generic(ExtraTabCompletion, Expect):
    """
    Generic interface to the GAP3/GAP4 interpreters.

    AUTHORS:

    - William Stein and David Joyner (interface for GAP4)

    - Franco Saliola (Feb 2010): refactored to separate out the generic
      code
    """
    def interrupt(self, tries=None, timeout: int = 1, quit_on_fail: bool = True):
        '''
        Interrupt the GAP process.

        Gap installs a SIGINT handler, we call it directly instead of
        trying to sent Ctrl-C. Unlike
        :meth:`~sage.interfaces.expect.Expect.interrupt`, we only try
        once since we are knowing what we are doing.

        Sometimes GAP dies while interrupting.

        EXAMPLES::

            sage: gap._eval_line(\'while(1=1) do i:=1;; od;\', wait_for_prompt=False)
            \'\'
            sage: rc = gap.interrupt(timeout=1)
            sage: [ gap(i) for i in range(10) ]   # check that it is still working
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        TESTS::

            sage: gap(\'"finished computation"\'); gap.interrupt(); gap(\'"ok"\')
            finished computation
            True
            ok
        '''
    def load_package(self, pkg, verbose: bool = False) -> None:
        '''
        Load the Gap package with the given name.

        If loading fails, raise a :exc:`RuntimeError` exception.

        TESTS::

            sage: gap.load_package("chevie")
            Traceback (most recent call last):
            ...
            RuntimeError: Error loading Gap package chevie. You may want to install gap_packages SPKG.
        '''
    def eval(self, x, newlines: bool = False, strip: bool = True, split_lines: bool = True, **kwds):
        '''
        Send the code in the string s to the GAP interpreter and return the
        output as a string.

        INPUT:

        - ``s`` -- string containing GAP code

        - ``newlines`` -- boolean (default: ``True``); if ``False``,
          remove all backslash-newlines inserted by the GAP output formatter

        - ``strip`` -- ignored

        - ``split_lines`` -- boolean (default: ``True``); if ``True`` then each
          line is evaluated separately.  If ``False``, then the whole
          block of code is evaluated all at once.

        EXAMPLES::

            sage: gap.eval(\'2+2\')
            \'4\'
            sage: gap.eval(\'Print(4); #test\\n Print(6);\')
            \'46\'
            sage: gap.eval(\'Print("#"); Print(6);\')
            \'#6\'
            sage: gap.eval(\'4; \\n 6;\')
            \'4\\n6\'
            sage: gap.eval(\'if 3>2 then\\nPrint("hi");\\nfi;\')
            \'hi\'
            sage: gap.eval(\'## this is a test\\nPrint("OK")\')
            \'OK\'
            sage: gap.eval(\'Print("This is a test. Oh no, a #");# but this is a comment\\nPrint("OK")\')
            \'This is a test. Oh no, a #OK\'
            sage: gap.eval(\'if 4>3 then\')
            \'\'
            sage: gap.eval(\'Print("Hi how are you?")\')
            \'Hi how are you?\'
            sage: gap.eval(\'fi\')
            \'\'

        TESTS:

        Whitespace is not stripped from the front of the result
        (:issue:`28439`)::

            sage: gap.eval(r\'Print("  -\\n\\\\\\\\-  ")\')
            \'  -\\n\\\\\\\\-\'
        '''
    def unbind(self, var) -> None:
        """
        Clear the variable named var.

        EXAMPLES::

            sage: gap.set('x', '2')
            sage: gap.get('x')
            '2'
            sage: gap.unbind('x')
            sage: gap.get('x')
            Traceback (most recent call last):
            ...
            RuntimeError: Gap produced error output
            Error, Variable: 'x' must have a value
            ...
        """
    def version(self):
        """
        Return the version of GAP being used.

        EXAMPLES::

            sage: print(gap.version())
            4...
        """
    def function_call(self, function, args=None, kwds=None):
        '''
        Call the GAP function with ``args`` and ``kwds``.

        EXAMPLES::

            sage: gap.function_call(\'SymmetricGroup\', [5])
            SymmetricGroup( [ 1 .. 5 ] )

        If the GAP function does not return a value, but prints something
        to the screen, then a string of the printed output is returned.

        ::

            sage: s = gap.function_call(\'Display\', [gap.SymmetricGroup(5).CharacterTable()])
            sage: type(s)
            <class \'sage.interfaces.interface.AsciiArtString\'>
            sage: s.startswith(\'CT\')
            True

        TESTS:

        If the function call is too long, two ``gap.eval`` calls are made
        since returned values from commands in a file cannot be handled
        properly::

            sage: g = Gap()
            sage: g.function_call("ConjugacyClassesSubgroups", sage.interfaces.gap.GapElement(g, \'SymmetricGroup(2)\', name = \'a_variable_with_a_very_very_very_long_name\')) # random
            [ ConjugacyClassSubgroups(SymmetricGroup( [ 1 .. 2 ] ),Group( () )),
              ConjugacyClassSubgroups(SymmetricGroup( [ 1 .. 2 ] ),Group( [ (1,2) ] )) ]

        When the command itself is so long that it warrants use of a temporary
        file to be communicated to GAP, this does not cause problems since
        the file will contain a single command::

            sage: g.function_call("ConjugacyClassesSubgroups", sage.interfaces.gap.GapElement(g, \'SymmetricGroup(2)\', name = \'a_variable_with_a_name_so_very_very_very_long_that_even_by_itself_will_make_expect_use_a_file\')) # random
            [ ConjugacyClassSubgroups(SymmetricGroup( [ 1 .. 2 ] ),Group( () )),
              ConjugacyClassSubgroups(SymmetricGroup( [ 1 .. 2 ] ),Group( [ (1,2) ] )) ]
        '''
    def get_record_element(self, record, name):
        '''
        Return the element of a GAP record identified by ``name``.

        INPUT:

        - ``record`` -- a GAP record
        - ``name`` -- string

        OUTPUT: :class:`GapElement`

        EXAMPLES::

            sage: rec = gap(\'rec( a := 1, b := "2" )\')
            sage: gap.get_record_element(rec, \'a\')
            1
            sage: gap.get_record_element(rec, \'b\')
            2

        TESTS::

            sage: rec = gap(\'rec( a := 1, b := "2" )\')
            sage: type(gap.get_record_element(rec, \'a\'))
            <class \'sage.interfaces.gap.GapElement\'>
        '''

class GapElement_generic(ModuleElement, ExtraTabCompletion, ExpectElement):
    """
    Generic interface to the GAP3/GAP4 interpreters.

    AUTHORS:

    - William Stein and David Joyner (interface for GAP4)

    - Franco Saliola (Feb 2010): refactored to separate out the generic
      code
    """
    def __bool__(self) -> bool:
        """
        EXAMPLES::

            sage: bool(gap(2))
            True
            sage: gap(0).bool()
            False
            sage: gap('false').bool()
            False
        """
    def __len__(self) -> int:
        '''
        EXAMPLES::

            sage: v = gap(\'[1,2,3]\'); v
            [ 1, 2, 3 ]
            sage: len(v)
            3

        len is also called implicitly by if::

            sage: if gap(\'1+1 = 2\'):
            ....:     print("1 plus 1 does equal 2")
            1 plus 1 does equal 2

        ::

            sage: if gap(\'1+1 = 3\'):
            ....:     print("it is true")
            ....: else:
            ....:     print("it is false")
            it is false
        '''
    def is_string(self):
        '''
        Tell whether this element is a string.

        EXAMPLES::

            sage: gap(\'"abc"\').is_string()
            True
            sage: gap(\'[1,2,3]\').is_string()
            False
        '''

class Gap(Gap_generic):
    """
    Interface to the GAP interpreter.

    AUTHORS:

    - William Stein and David Joyner
    """
    def __init__(self, max_workspace_size=None, maxread=None, script_subdirectory=None, use_workspace_cache: bool = True, server=None, server_tmpdir=None, logfile=None, seed=None, env={}) -> None:
        """
        EXAMPLES::

            sage: from sage.interfaces.gap import gap
            sage: gap == loads(dumps(gap))
            True
        """
    def set_seed(self, seed=None):
        """
        Set the seed for gap interpreter.

        The seed should be an integer.

        EXAMPLES::

            sage: g = Gap()
            sage: g.set_seed(0)
            0
            sage: [g.Random(1,10) for i in range(5)]
            [2, 3, 3, 4, 2]
        """
    def __reduce__(self):
        """
        EXAMPLES::

            sage: from sage.interfaces.gap import gap
            sage: gap.__reduce__()
            (<function reduce_load_GAP at 0x...>, ())
            sage: f, args = _
            sage: f(*args)
            Gap
        """
    def cputime(self, t=None):
        """
        Return the amount of CPU time that the GAP session has used. If
        ``t`` is not None, then it returns the difference
        between the current CPU time and ``t``.

        EXAMPLES::

            sage: t = gap.cputime()
            sage: t  #random
            0.13600000000000001
            sage: gap.Order(gap.SymmetricGroup(5))
            120
            sage: gap.cputime(t)  #random
            0.059999999999999998
        """
    def save_workspace(self) -> None:
        '''
        Save the GAP workspace.

        TESTS:

        We make sure that :issue:`9938` (GAP does not start if the path
        to the GAP workspace file contains more than 82 characters) is
        fixed::

            sage: ORIGINAL_WORKSPACE = sage.interfaces.gap.WORKSPACE
            sage: import tempfile
            sage: with tempfile.NamedTemporaryFile(prefix="0"*80) as f:    # long time (4s on sage.math, 2013)
            ....:     sage.interfaces.gap.WORKSPACE = f.name
            ....:     gap = Gap()
            ....:     gap(\'3+2\')
            5
            sage: sage.interfaces.gap.WORKSPACE = ORIGINAL_WORKSPACE
        '''
    def help(self, s, pager: bool = True):
        """
        Print help on a given topic.

        EXAMPLES:

        Note: In order to ensure consistent unicode handling from GAP we
        start a GAP instance with a forced UTF-8 locale::

            sage: gap = Gap(env={'LC_CTYPE': 'en_US.UTF-8'})
            sage: print(gap.help('SymmetricGroup', pager=False))
            <BLANKLINE>
              50.1-... SymmetricGroup
            <BLANKLINE>
              ‣ SymmetricGroup( [filt, ]deg ) ─────────────────────────────────── function
            ...
            <BLANKLINE>
        """
    def set(self, var, value) -> None:
        """
        Set the variable var to the given value.

        EXAMPLES::

            sage: gap.set('x', '2')
            sage: gap.get('x')
            '2'
        """
    def get(self, var, use_file: bool = False):
        """
        Get the string representation of the variable var.

        EXAMPLES::

            sage: gap.set('x', '2')
            sage: gap.get('x')
            '2'
        """
    def console(self) -> None:
        """
        Spawn a new GAP command-line session.

        EXAMPLES::

            sage: gap.console()  # not tested
            *********   GAP, Version 4.5.7 of 14-Dec-2012 (free software, GPL)
            *  GAP  *   https://www.gap-system.org
            *********   Architecture: x86_64-unknown-linux-gnu-gcc-default64
            Libs used:  gmp, readline
            Loading the library and packages ...
            Packages:   GAPDoc 1.5.1
            Try '?help' for help. See also  '?copyright' and  '?authors'
            gap>
        """

def gap_reset_workspace(max_workspace_size=None, verbose: bool = False) -> None:
    '''
    Call this to completely reset the GAP workspace, which is used by
    default when Sage first starts GAP.

    The first time you start GAP from Sage, it saves the startup state
    of GAP in a file ``$HOME/.sage/gap/workspace-gap-HASH``, where
    ``HASH`` is a hash of the directory where Sage is installed. This
    is useful because the subsequent startup of GAP is at least ten
    times as fast. But if you update GAP or any of its packages, those
    changes won\'t take effect until the workspace is reset.

    TESTS:

    Check that the race condition from :issue:`14242` has been fixed.
    We temporarily need to change the worksheet filename, and to set
    ``first_try=True`` to ensure that the new workspace is created::

        sage: # long time
        sage: ORIGINAL_WORKSPACE = sage.interfaces.gap.WORKSPACE
        sage: saved_first_try = sage.interfaces.gap.first_try
        sage: sage.interfaces.gap.first_try = True
        sage: sage.interfaces.gap.WORKSPACE = tmp_filename()
        sage: from multiprocessing import Process
        sage: import time
        sage: gap = Gap()  # reset GAP session
        sage: P = [Process(target=gap, args=("14242",)) for i in range(4)]
        sage: for p in P:  # indirect doctest
        ....:     p.start()
        ....:     time.sleep(float(0.2))
        sage: for p in P:
        ....:     p.join()
        sage: os.unlink(sage.interfaces.gap.WORKSPACE)
        sage: sage.interfaces.gap.WORKSPACE = ORIGINAL_WORKSPACE
        sage: sage.interfaces.gap.first_try = saved_first_try
    '''

class GapElement(GapElement_generic, sage.interfaces.abc.GapElement):
    def __getitem__(self, n):
        """
        EXAMPLES::

            sage: a = gap([1,2,3])
            sage: a[1]
            1
        """
    def str(self, use_file: bool = False):
        """
        EXAMPLES::

            sage: print(gap(2))
            2
        """

class GapFunctionElement(FunctionElement): ...
class GapFunction(ExpectFunction): ...

def is_GapElement(x):
    """
    Return ``True`` if ``x`` is a :class:`GapElement`.

    This function is deprecated; use :func:`isinstance`
    (of :class:`sage.interfaces.abc.GapElement`) instead.

    EXAMPLES::

        sage: from sage.interfaces.gap import is_GapElement
        sage: is_GapElement(gap(2))
        doctest:...: DeprecationWarning: the function is_GapElement is deprecated; use isinstance(x, sage.interfaces.abc.GapElement) instead
        See https://github.com/sagemath/sage/issues/34823 for details.
        True
        sage: is_GapElement(2)
        False
    """
def gfq_gap_to_sage(x, F):
    """
    INPUT:

    - ``x`` -- GAP finite field element

    - ``F`` -- Sage finite field

    OUTPUT: element of ``F``

    EXAMPLES::

        sage: x = gap('Z(13)')
        sage: F = GF(13, 'a')
        sage: F(x)
        2
        sage: F(gap('0*Z(13)'))
        0
        sage: F = GF(13^2, 'a')
        sage: x = gap('Z(13)')
        sage: F(x)
        2
        sage: x = gap('Z(13^2)^3')
        sage: F(x)
        12*a + 11
        sage: F.multiplicative_generator()^3
        12*a + 11

    TESTS:

    Check that :issue:`18048` is fixed::

        sage: K.<a> = GF(16)
        sage: b = a^2 + a
        sage: K(b._gap_())
        a^2 + a

    AUTHOR:

    - David Joyner and William Stein
    """
def intmod_gap_to_sage(x):
    """
    INPUT:

    - ``x`` -- Gap integer mod ring element

    EXAMPLES::

        sage: a = gap(Mod(3, 18)); a
        ZmodnZObj( 3, 18 )
        sage: b = sage.interfaces.gap.intmod_gap_to_sage(a); b
        3
        sage: b.parent()
        Ring of integers modulo 18

        sage: a = gap(Mod(3, 17)); a
        Z(17)
        sage: b = sage.interfaces.gap.intmod_gap_to_sage(a); b
        3
        sage: b.parent()
        Finite Field of size 17

        sage: a = gap(Mod(0, 17)); a
        0*Z(17)
        sage: b = sage.interfaces.gap.intmod_gap_to_sage(a); b
        0
        sage: b.parent()
        Finite Field of size 17

        sage: a = gap(Mod(3, 65537)); a
        ZmodpZObj( 3, 65537 )
        sage: b = sage.interfaces.gap.intmod_gap_to_sage(a); b
        3
        sage: b.parent()
        Ring of integers modulo 65537
    """

gap: Gap

def reduce_load_GAP():
    """
    Return the GAP interface object defined in ``sage.interfaces.gap``.

    EXAMPLES::

        sage: from sage.interfaces.gap import reduce_load_GAP
        sage: reduce_load_GAP()
        Gap
    """
def gap_console() -> None:
    '''
    Spawn a new GAP command-line session.

    Note that in gap-4.5.7 you cannot use a workspace cache that had
    no commandline to restore a gap session with commandline.

    EXAMPLES::

        sage: gap_console()  # not tested
        *********   GAP, Version 4.5.7 of 14-Dec-2012 (free software, GPL)
        *  GAP  *   https://www.gap-system.org
        *********   Architecture: x86_64-unknown-linux-gnu-gcc-default64
        Libs used:  gmp, readline
        Loading the library and packages ...
        Packages:   GAPDoc 1.5.1
        Try \'?help\' for help. See also  \'?copyright\' and  \'?authors\'
        gap>

    TESTS::

        sage: import subprocess as sp
        sage: from sage.interfaces.gap import gap_command
        sage: cmd = \'echo "quit;" | \' + gap_command(use_workspace_cache=False)[0]
        sage: gap_startup = sp.check_output(cmd, shell=True,
        ....:                               stderr=sp.STDOUT,
        ....:                               encoding=\'latin1\')
        sage: \'www.gap-system.org\' in gap_startup
        True
        sage: \'Error\' not in gap_startup
        True
        sage: \'sorry\' not in gap_startup
        True
    '''
