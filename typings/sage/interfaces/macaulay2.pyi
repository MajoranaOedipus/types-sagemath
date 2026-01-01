r"""
Interface to Macaulay2

.. NOTE::

    You must have ``Macaulay2`` installed on your computer
    for this interface to work. Macaulay2 is not included with Sage,
    but you can obtain it from https://macaulay2.com/.
    No additional optional Sage packages are required.

Sage provides an interface to the Macaulay2 computational algebra
system. This system provides extensive functionality for commutative
algebra. You do not have to install any optional packages.

The Macaulay2 interface offers three pieces of functionality:

- ``macaulay2_console()`` -- a function that dumps you
  into an interactive command-line Macaulay2 session

- ``macaulay2.eval(expr)`` -- evaluation of arbitrary Macaulay2
  expressions, with the result returned as a string

- ``macaulay2(expr)`` -- creation of a Sage object that wraps a
  Macaulay2 object.  This provides a Pythonic interface to Macaulay2.  For
  example, if ``f = macaulay2(10)``, then ``f.gcd(25)`` returns the
  GCD of `10` and `25` computed using Macaulay2.

EXAMPLES::

    sage: macaulay2('3/5 + 7/11')
    68
    --
    55
    sage: f = macaulay2('f = i -> i^3')
    sage: f
    f
    sage: f(5)
    125

    sage: R = macaulay2('ZZ/5[x,y,z]')
    sage: R
    ZZ
    --[x...z]
     5
    sage: x = macaulay2('x')
    sage: y = macaulay2('y')
    sage: (x+y)^5
     5    5
    x  + y
    sage: parent((x+y)^5)
    Macaulay2

The name of the variable to which a Macaulay2 element is assigned internally
can be passed as an argument. This is useful for types like polynomial rings
which acquire that name in Macaulay2::

    sage: R = macaulay2('QQ[x,y,z,w]', 'R')
    sage: R
    R

    sage: f = macaulay2('x^4 + 2*x*y^3 + x*y^2*w + x*y*z*w + x*y*w^2'
    ....:               '+ 2*x*z*w^2 + y^4 + y^3*w + 2*y^2*z*w + z^4 + w^4')
    sage: f
     4       3    4    4      2     3                2           2         2    4
    x  + 2x*y  + y  + z  + x*y w + y w + x*y*z*w + 2y z*w + x*y*w  + 2x*z*w  + w
    sage: g = f * macaulay2('x+y^5')
    sage: print(g.factor())
      4       3    4    4      2     3                2           2         2    4   5
    (x  + 2x*y  + y  + z  + x*y w + y w + x*y*z*w + 2y z*w + x*y*w  + 2x*z*w  + w )(y  + x)

Use :meth:`eval` for explicit control over what is sent to the interpreter.
The argument is evaluated in Macaulay2 as is::

    sage: macaulay2.eval('compactMatrixForm')
    true
    sage: macaulay2.eval('compactMatrixForm = false;')
    sage: macaulay2.eval('matrix {{1, x^2+y}}')
    |      2      |
    |  1  x  + y  |
    <BLANKLINE>
            1      2
    Matrix R  <-- R
    sage: macaulay2.eval('compactMatrixForm = true;')


AUTHORS:

- Kiran Kedlaya and David Roe (2006-02-05, during Sage coding sprint)
- William Stein (2006-02-09): inclusion in Sage; prompt uses regexp,
  calling of Macaulay2 functions via __call__.
- William Stein (2006-02-09): fixed bug in reading from file and
  improved output cleaning.
- Kiran Kedlaya (2006-02-12): added ring and ideal constructors,
  list delimiters, is_Macaulay2Element, sage_polystring,
  __floordiv__, __mod__, __iter__, __len__; stripped extra
  leading space and trailing newline from output.

.. TODO::

    Get rid of all numbers in output, e.g., in ideal function below.
"""
import sage.interfaces.abc
from _typeshed import Incomplete
from sage.interfaces.expect import Expect as Expect, ExpectElement as ExpectElement, ExpectFunction as ExpectFunction, FunctionElement as FunctionElement
from sage.interfaces.interface import AsciiArtString as AsciiArtString
from sage.interfaces.tab_completion import ExtraTabCompletion as ExtraTabCompletion
from sage.misc.instancedoc import instancedoc as instancedoc
from sage.misc.multireplace import multiple_replace as multiple_replace
from sage.misc.superseded import deprecated_function_alias as deprecated_function_alias
from sage.structure.global_options import GlobalOptions as GlobalOptions

def remove_output_labels(s) -> str:
    """
    Remove output labels of Macaulay2 from a string.

    - s: output of Macaulay2

    - s: string

    Returns: the input string with `n` symbols removed from the beginning of
    each line, where `n` is the minimal number of spaces or symbols of
    Macaulay2 output labels (looking like 'o39 = ') present on every non-empty
    line.

    Return type: string

    .. NOTE::

        If ``s`` consists of several outputs and their labels have
        different width, it is possible that some strings will have leading
        spaces (or maybe even pieces of output labels). However, this
        function will try not cut any messages.

    EXAMPLES::

        sage: from sage.interfaces.macaulay2 import remove_output_labels
        sage: output = 'o1 = QQ [x, y]\\n\\no1 : PolynomialRing\\n'
        sage: remove_output_labels(output)
        'QQ [x, y]\\n\\nPolynomialRing\\n'
    """

PROMPT: str
PROMPT_LOAD: str

class Macaulay2(ExtraTabCompletion, Expect):
    """
    Interface to the Macaulay2 interpreter.
    """
    def __init__(self, maxread=None, script_subdirectory=None, logfile=None, server=None, server_tmpdir=None, command=None) -> None:
        """
        Initialize a Macaulay2 interface instance.

        We replace the standard input prompt with a strange one, so that
        we do not catch input prompts inside the documentation.

        We replace the standard input continuation prompt, which is
        just a bunch of spaces and cannot be automatically detected in a
        reliable way. This is necessary for allowing commands that occupy
        several strings.

        We also change the starting line number to make all the output
        labels to be of the same length. This allows correct stripping of
        the output of several commands.

        TESTS::

            sage: from sage.interfaces.macaulay2 import macaulay2
            sage: macaulay2 == loads(dumps(macaulay2))
            True
        """
    def __reduce__(self):
        """
        Used in serializing a Macaulay2 interface.

        EXAMPLES::

            sage: rlm2, t = Macaulay2().__reduce__()
            sage: rlm2(*t)
            Macaulay2
        """
    def eval(self, code, strip: bool = True, **kwds):
        '''
        Send the code x to the Macaulay2 interpreter and return the output
        as a string suitable for input back into Macaulay2, if possible.

        INPUT:

        - ``code`` -- string
        - ``strip`` -- ignored

        EXAMPLES::

            sage: macaulay2.eval("2+2") # optional - macaulay2
            4
        '''
    def restart(self) -> None:
        """
        Restart Macaulay2 interpreter.

        TESTS::

            sage: macaulay2.restart()  # optional - macaulay2
        """
    def set_seed(self, seed=None):
        """
        Set the seed for Macaulay2 interpreter.

        INPUT:

        - ``seed`` -- number (default: ``None``); if ``None``, it
          is set to a random number

        OUTPUT: the new seed

        EXAMPLES::

            sage: m = Macaulay2()                     # optional - macaulay2
            sage: m.set_seed(123456)                  # optional - macaulay2
            123456
            sage: [m.random(100) for _ in range(11)]  # optional - macaulay2
            [8, 29, 5, 22, 4, 32, 35, 57, 3, 95, 36]
        """
    class options(GlobalOptions):
        """
        Global options for Macaulay2 elements.

        @OPTIONS@

        EXAMPLES::

            sage: # optional - macaulay2
            sage: macaulay2.options.after_print = True
            sage: A = macaulay2(matrix([[1, 2], [3, 6]])); A
            | 1 2 |
            | 3 6 |
            <BLANKLINE>
                     2        2
            Matrix ZZ  <--- ZZ
            sage: A.kernel()
            image | 2  |
                  | -1 |
            <BLANKLINE>
                                      2
            ZZ-module, submodule of ZZ
            sage: macaulay2.options.after_print = False
        """
        NAME: str
        module: str
        after_print: Incomplete
    def get(self, var):
        '''
        Get the value of the variable ``var``.

        INPUT:

        - ``var`` -- string; the name of the variable in Macaulay2

        OUTPUT: string of the textual representation of the variable in
        Macaulay2

        EXAMPLES::

            sage: macaulay2.set("a", "2") # optional - macaulay2
            sage: macaulay2.get("a")      # optional - macaulay2
            2

        Note that the following syntax is used to obtain a
        ``Macaulay2Element`` instead::

            sage: a = macaulay2(\'2\'); a   # optional - macaulay2
            2
            sage: type(a)                 # optional - macaulay2
            <class \'sage.interfaces.macaulay2.Macaulay2Element\'>
        '''
    def set(self, var, value) -> None:
        '''
        Set the variable ``var`` to the given value.

        INPUT:

        - ``var`` -- string; the name of the variable in Macaulay2
        - ``value`` -- string to evaluate

        EXAMPLES::

            sage: macaulay2.set("a", "1+1")  # optional - macaulay2
            sage: macaulay2.get("a")         # optional - macaulay2
            2

        TESTS:

        Check that internal expect variables do not acquire their global
        variable name and that ``use`` is invoked (:issue:`28303`)::

            sage: # optional - macaulay2
            sage: R = macaulay2(\'QQ[x, y]\')  # indirect doctest
            sage: R.net()
            QQ[x...y]
            sage: S = R / macaulay2(\'ideal {x^2 - y}\')
            sage: macaulay2.eval(\'class x === %s\' % S.name())
            true
        '''
    def clear(self, var) -> None:
        """
        Clear the variable named ``var``.

        The interface automatically clears Macaulay2 elements when they fall
        out of use, so calling this method is usually not necessary.

        EXAMPLES::

            sage: # optional - macaulay2
            sage: macaulay2.eval('R = QQ[x,y];')
            sage: macaulay2.eval('net class R')
            PolynomialRing
            sage: macaulay2.clear('R')
            sage: macaulay2.eval('net class R')
            Symbol

        TESTS:

        Check that only internal variables get reused by the interface::

            sage: all(s.startswith('sage') for s in macaulay2._available_vars)  # optional - macaulay2
            True
        """
    def console(self) -> None:
        """
        Spawn a new M2 command-line session.

        EXAMPLES::

            sage: macaulay2.console()                    # not tested
            Macaulay 2, version 1.1
            with packages: Classic, Core, Elimination, IntegralClosure, LLLBases, Parsing, PrimaryDecomposition, SchurRings, TangentCone
            ...
        """
    def cputime(self, t=None):
        '''
        EXAMPLES::

            sage: # optional - macaulay2
            sage: R = macaulay2("QQ[x,y]")
            sage: x,y = R.gens()
            sage: a = (x+y+1)^20
            sage: macaulay2.cputime()       # random
            0.48393700000000001
        '''
    def version(self):
        """
        Return the version of Macaulay2 as a tuple.

        EXAMPLES::

            sage: macaulay2.version() # optional - macaulay2
            (1, ...)
        """
    def ideal(self, *gens):
        """
        Return the ideal generated by gens.

        INPUT:

        - ``gens`` -- list or tuple of Macaulay2 objects (or objects that can be
          made into Macaulay2 objects via evaluation)

        OUTPUT: the Macaulay2 ideal generated by the given list of gens

        EXAMPLES::

            sage: R2 = macaulay2.ring('QQ', '[x, y]'); R2            # optional - macaulay2
            QQ[x...y]
            sage: I = macaulay2.ideal( ('y^2 - x^3', 'x - y') ); I   # optional - macaulay2
                      3    2
            ideal (- x  + y , x - y)
            sage: J = I^3; J.gb().gens().transpose()                 # optional - macaulay2
            {-9} | y9-3y8+3y7-y6             |
            {-7} | xy6-2xy5+xy4-y7+2y6-y5    |
            {-5} | x2y3-x2y2-2xy4+2xy3+y5-y4 |
            {-3} | x3-3x2y+3xy2-y3           |
        """
    def ring(self, base_ring: str = 'ZZ', vars: str = '[x]', order: str = 'Lex'):
        """
        Create a Macaulay2 polynomial ring.

        INPUT:

        - ``base_ring`` -- base ring (see examples below)
        - ``vars`` -- tuple or string that defines the variable names
        - ``order`` -- string (default: ``'Lex'``); the monomial order

        OUTPUT: a Macaulay2 ring

        EXAMPLES:

        This is a ring in variables named ``a`` through ``d`` over the finite
        field of order 7, with graded reverse lex ordering::

            sage: R1 = macaulay2.ring('ZZ/7', '[a..d]', 'GRevLex')  # optional - macaulay2
            sage: R1.describe()  # optional - macaulay2
            ZZ
            --[a..d, Degrees => {4:1}, Heft => {1}, MonomialOrder => {MonomialSize => 16},
             7                                                       {GRevLex => {4:1}  }
                                                                     {Position => Up    }
            --------------------------------------------------------------------------------
            DegreeRank => 1]
            sage: R1.char()  # optional - macaulay2
            7

        This is a polynomial ring over the rational numbers::

            sage: R2 = macaulay2.ring('QQ', '[x, y]')  # optional - macaulay2
            sage: R2.describe()  # optional - macaulay2
            QQ[x..y, Degrees => {2:1}, Heft => {1}, MonomialOrder => {MonomialSize => 16},
                                                                     {Lex => 2          }
                                                                     {Position => Up    }
            --------------------------------------------------------------------------------
            DegreeRank => 1]

        TESTS::

            sage: macaulay2.ring('QQ', '[a_0..a_2,b..<d,f]').vars()     # optional - macaulay2
            | a_0 a_1 a_2 b c f |
        """
    def help(self, s):
        '''
        EXAMPLES::

            sage: macaulay2.help("load")  # optional - macaulay2 - 1st call might be chatty...
            ...
            sage: macaulay2.help("load")  # optional - macaulay2
            load...
            ****...
            ...
              * "input" -- read Macaulay2 commands and echo
              * "notify" -- whether to notify the user when a file is loaded...

        TESTS:

        Check that help also works for Macaulay2 keywords and variables
        (:issue:`28565`)::

            sage: from sage.repl.interpreter import get_test_shell
            sage: shell = get_test_shell()
            sage: shell.run_cell(\'macaulay2.help("try")\')  # optional - macaulay2
            try -- catch an error
            ****...
            The object "try" is a...

            sage: from sage.repl.interpreter import get_test_shell
            sage: shell = get_test_shell()
            sage: shell.run_cell(\'macaulay2.help("errorDepth")\')  # optional - macaulay2
            errorDepth...
            The object "errorDepth" is a...
        '''
    def use(self, R) -> None:
        '''
        Use the Macaulay2 ring R.

        EXAMPLES::

            sage: # optional - macaulay2
            sage: R = macaulay2("QQ[x,y]")
            sage: P = macaulay2("ZZ/7[symbol x, symbol y]")
            sage: macaulay2("x").cls()._operator(\'===\', P)
            true
            sage: macaulay2.use(R)
            sage: macaulay2("x").cls()._operator(\'===\', R)
            true
        '''
    def new_from(self, type, value):
        '''
        Return a new ``Macaulay2Element`` of type ``type`` constructed from
        ``value``.

        EXAMPLES::

            sage: l = macaulay2.new_from("MutableList", [1,2,3]) # optional - macaulay2
            sage: l                                              # optional - macaulay2
            MutableList{...3...}
            sage: list(l)                                        # optional - macaulay2
            [1, 2, 3]
        '''

class Macaulay2Element(ExtraTabCompletion, ExpectElement, sage.interfaces.abc.Macaulay2Element):
    """
    Instances of this class represent objects in Macaulay2.

    Using the method :meth:`sage` we can translate some of them to
    SageMath objects:

    .. automethod:: _sage_
    """
    def __iter__(self):
        """
        EXAMPLES::

            sage: l = macaulay2([1,2,3]) # optional - macaulay2
            sage: list(iter(l))          # optional - macaulay2
            [1, 2, 3]
        """
    def external_string(self):
        '''
        EXAMPLES::

           sage: R = macaulay2("QQ[symbol x, symbol y]")  # optional - macaulay2
           sage: R.external_string()                      # optional - macaulay2
           \'QQ(monoid[x..y, Degrees => {2:1}, Heft => {1}, MonomialOrder => VerticalList{MonomialSize => 32, GRevLex => {2:1}, Position => Up}, DegreeRank => 1])\'
        '''
    def name(self, new_name=None):
        '''
        Get or change the name of this Macaulay2 element.

        INPUT:

        - ``new_name`` -- string (default: ``None``); if ``None``, return the
          name of this element. Else return a new object identical to ``self``
          whose name is ``new_name``.

        Note that this can overwrite existing variables in the system.

        EXAMPLES::

            sage: # optional - macaulay2
            sage: S = macaulay2(QQ[\'x,y\'])
            sage: S.name()
            \'sage...\'
            sage: R = S.name("R")
            sage: R.name()
            \'R\'
            sage: R.vars().cokernel().resolution()
             1      2      1
            R  <-- R  <-- R  <-- 0
            <BLANKLINE>
            0      1      2      3

        The name can also be given at definition::

            sage: A = macaulay2(ZZ[\'x,y,z\'], name=\'A\')  # optional - macaulay2
            sage: A.name()                              # optional - macaulay2
            \'A\'
            sage: A^1                                   # optional - macaulay2
             1
            A
        '''
    def __len__(self) -> int:
        """
        EXAMPLES::

            sage: l = macaulay2([1,2,3])  # optional - macaulay2
            sage: len(l)                  # optional - macaulay2
            3
            sage: type(_)                 # optional - macaulay2
            <... 'int'>
        """
    def __getitem__(self, n):
        """
        EXAMPLES::

            sage: l = macaulay2([1,2,3])  # optional - macaulay2
            sage: l[0]                    # optional - macaulay2
            1
        """
    def __setitem__(self, index, value) -> None:
        '''
        EXAMPLES::

            sage: l = macaulay2.new_from("MutableList", [1,2,3]) # optional - macaulay2
            sage: l[0] = 4               # optional - macaulay2
            sage: list(l)                # optional - macaulay2
            [4, 2, 3]
        '''
    def __call__(self, x):
        '''
        EXAMPLES::

            sage: # optional - macaulay2
            sage: R = macaulay2("QQ[x, y]")
            sage: x,y = R.gens()
            sage: I = macaulay2.ideal(x*y, x+y)
            sage: gb = macaulay2.gb
            sage: gb(I)
            GroebnerBasis[status: done; S-pairs encountered up to degree 1]
        '''
    def __floordiv__(self, x):
        """
        Quotient of division of ``self`` by ``other``.  This is denoted ``//``.

        EXAMPLES::

            sage: R.<x,y> = GF(7)[]

        Now make the M2 version of R, so we can coerce elements of R to M2::

            sage: # optional - macaulay2
            sage: _ = macaulay2(R)
            sage: h = macaulay2((x^3 + 2*y^2*x)^7); h
             21     7 14
            x   + 2x y
            sage: h1 = macaulay2(x^2 + 2*y*x)
            sage: h2 = macaulay2(x^3 + 2*y*x)
            sage: u = h // [h1,h2]
            sage: h == u[0]*h1 + u[1]*h2 + (h % [h1,h2])
            True
        """
    def __mod__(self, x):
        """
        Remainder of division of ``self`` by ``other``.  This is denoted ``%``.

        EXAMPLES::

            sage: R.<x,y> = GF(7)[]

        Now make the M2 version of R, so we can coerce elements of R to M2::

            sage: # optional - macaulay2
            sage: _ = macaulay2(R)
            sage: h = macaulay2((x^3 + 2*y^2*x)^7); h
             21     7 14
            x   + 2x y
            sage: h1 = macaulay2(x^2 + 2*y*x)
            sage: h2 = macaulay2(x^3 + 2*y*x)
            sage: h % [h1,h2]
            -3x*y
            sage: u = h // [h1,h2]
            sage: h == u[0]*h1 + u[1]*h2 + (h % [h1,h2])
            True
        """
    def __bool__(self) -> bool:
        '''
        Return whether this Macaulay2 element is not ``False`` or not ``0``.

        EXAMPLES::

            sage: # optional - macaulay2
            sage: a = macaulay2(0)
            sage: a == 0
            True
            sage: bool(a)
            False

        TESTS:

        Check that :issue:`28705` is fixed::

            sage: # optional - macaulay2
            sage: t = macaulay2(True); t
            true
            sage: bool(t)
            True
            sage: bool(macaulay2(\'false\'))
            False
            sage: bool(macaulay2(\'"a"\'))
            True
        '''
    def sage_polystring(self):
        """
        If this Macaulay2 element is a polynomial, return a string
        representation of this polynomial that is suitable for
        evaluation in Python.  Thus ``*`` is used for multiplication
        and ``**`` for exponentiation.   This function is primarily
        used internally.

        EXAMPLES::

            sage: # optional - macaulay2
            sage: R = macaulay2.ring('QQ','(x,y)')
            sage: f = macaulay2('x^3 + 3*y^11 + 5')
            sage: print(f)
             3     11
            x  + 3y   + 5
            sage: f.sage_polystring()
            'x**3+3*y**11+5'
        """
    def structure_sheaf(self):
        """
        EXAMPLES::

            sage: # optional - macaulay2
            sage: S = macaulay2('QQ[a..d]')
            sage: R = S / macaulay2('a^3 + b^3 + c^3 + d^3')
            sage: X = R.Proj().name('X')
            sage: X.structure_sheaf()
            doctest:...: DeprecationWarning: The function `structure_sheaf` is deprecated. Use `self.sheaf()` instead.
            See https://github.com/sagemath/sage/issues/27848 for details.
            OO
              X
            sage: X.sheaf()
            OO
              X
        """
    def subs(self, *args, **kwds):
        '''
        Note that we have to override the substitute method so that we get
        the default one from Macaulay2 instead of the one provided by Element.

        EXAMPLES::

            sage: # optional - macaulay2
            sage: R = macaulay2("QQ[x]")
            sage: P = macaulay2("ZZ/7[symbol x]")
            sage: x, = R.gens()
            sage: a = x^2 + 1
            sage: a = a.substitute(P)
            sage: a.sage().parent()
            Univariate Polynomial Ring in x over Finite Field of size 7
        '''
    def cls(self):
        """
        Since class is a keyword in Python, we have to use cls to call
        Macaulay2's class.  In Macaulay2, class corresponds to Sage's
        notion of parent.

        EXAMPLES::

            sage: macaulay2(ZZ).cls()  # optional - macaulay2
            Ring
        """
    def after_print_text(self):
        """
        Obtain type information for this Macaulay2 element.

        This is the text that is displayed using ``AfterPrint`` in a Macaulay2
        interpreter.

        Macaulay2 by default includes this information in the output.
        In Sage, this behavior can optionally be enabled by setting the option
        ``after_print`` in :class:`Macaulay2.options`.

        EXAMPLES::

            sage: B = macaulay2(matrix([[1, 2], [3, 6]])).kernel(); B  # optional - macaulay2
            image | 2  |
                  | -1 |
            sage: B.after_print_text()  # optional - macaulay2
                                      2
            ZZ-module, submodule of ZZ
        """
    def dot(self, x):
        '''
        EXAMPLES::

            sage: # optional - macaulay2
            sage: d = macaulay2.new("MutableHashTable")
            sage: d["k"] = 4
            sage: d.dot("k")
            4
        '''
    def sharp(self, x):
        """
        EXAMPLES::

            sage: a = macaulay2([1,2,3]) # optional - macaulay2
            sage: a.sharp(0)             # optional - macaulay2
            1
        """
    def starstar(self, x):
        """
        The binary operator ``**`` in Macaulay2 is usually used for tensor
        or Cartesian power.

        EXAMPLES::

            sage: a = macaulay2([1,2]).set()  # optional - macaulay2
            sage: a.starstar(a)               # optional - macaulay2
            set {(1, 1), (1, 2), (2, 1), (2, 2)}
        """
    def underscore(self, x):
        """
        EXAMPLES::

            sage: a = macaulay2([1,2,3])  # optional - macaulay2
            sage: a.underscore(0)         # optional - macaulay2
            1
        """
    to_sage: Incomplete

class Macaulay2Function(ExpectFunction):
    """
    TESTS::

        sage: gb = macaulay2.gb  # optional - macaulay2
        sage: type(gb)           # optional - macaulay2
        <class 'sage.interfaces.macaulay2.Macaulay2Function'>
        sage: gb._name           # optional - macaulay2
        'gb'
    """
class Macaulay2FunctionElement(FunctionElement): ...

def is_Macaulay2Element(x):
    """
    Return ``True`` if ``x`` is a :class:`Macaulay2Element`.

    This function is deprecated; use :func:`isinstance`
    (of :class:`sage.interfaces.abc.Macaulay2Element`) instead.

    EXAMPLES::

        sage: from sage.interfaces.macaulay2 import is_Macaulay2Element
        sage: is_Macaulay2Element(2)              # optional - macaulay2
        doctest:...: DeprecationWarning: the function is_Macaulay2Element is deprecated; use isinstance(x, sage.interfaces.abc.Macaulay2Element) instead
        See https://github.com/sagemath/sage/issues/34804 for details.
        False
        sage: is_Macaulay2Element(macaulay2(2))   # optional - macaulay2
        True
    """

macaulay2: Macaulay2

def macaulay2_console() -> None:
    """
    Spawn a new M2 command-line session.

    EXAMPLES::

        sage: macaulay2_console()                    # not tested
        Macaulay 2, version 1.1
        with packages: Classic, Core, Elimination, IntegralClosure, LLLBases, Parsing, PrimaryDecomposition, SchurRings, TangentCone
        ...
    """
def reduce_load_macaulay2():
    """
    Used for reconstructing a copy of the Macaulay2 interpreter from a pickle.

    EXAMPLES::

        sage: from sage.interfaces.macaulay2 import reduce_load_macaulay2
        sage: reduce_load_macaulay2()
        Macaulay2
    """
