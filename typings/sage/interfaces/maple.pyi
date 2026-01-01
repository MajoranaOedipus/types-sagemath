r"""
Interface to Maple

AUTHORS:

- William Stein (2005): maple interface

- Gregg Musiker (2006-02-02): tutorial

- William Stein (2006-03-05): added tab completion, e.g., maple.[tab],
  and help, e.g, maple.sin?.

You must have the optional commercial Maple interpreter installed
and available as the command ``maple`` in your PATH in
order to use this interface. You do not have to install any
optional Sage packages.

Type ``maple.[tab]`` for a list of all the functions
available from your Maple install. Type
``maple.[tab]?`` for Maple's help about a given
function. Type ``maple(...)`` to create a new Maple
object, and ``maple.eval(...)`` to run a string using
Maple (and get the result back as a string).

EXAMPLES::

    sage: # optional - maple
    sage: maple('3 * 5')
    15
    sage: maple.eval('ifactor(2005)')
    '``(5)*``(401)'
    sage: maple.ifactor(2005)
    ``(5)*``(401)
    sage: maple.fsolve('x^2=cos(x)+4', 'x=0..5')
    1.914020619
    sage: maple.factor('x^5 - y^5')
    (x-y)*(x^4+x^3*y+x^2*y^2+x*y^3+y^4)

If the string "error" (case insensitive) occurs in the output of
anything from Maple, a :exc:`RuntimeError` exception is raised.

Tutorial
--------

AUTHORS:

- Gregg Musiker (2006-02-02): initial version.

This tutorial is based on the Maple Tutorial for number theory from
http://www.math.mun.ca/~drideout/m3370/numtheory.html.

There are several ways to use the Maple Interface in Sage. We will
discuss two of those ways in this tutorial.


#. If you have a maple expression such as

   ::

       factor( (x^5-1));

   We can write that in sage as

   ::

       sage: maple('factor(x^5-1)')                 # optional - maple
       (x-1)*(x^4+x^3+x^2+x+1)

   Notice, there is no need to use a semicolon.

#. Since Sage is written in Python, we can also import maple
   commands and write our scripts in a Pythonic way. For example,
   ``factor()`` is a maple command, so we can also factor
   in Sage using

   ::

       sage: maple('(x^5-1)').factor()              # optional - maple
       (x-1)*(x^4+x^3+x^2+x+1)

   where ``expression.command()`` means the same thing as
   ``command(expression)`` in Maple. We will use this
   second type of syntax whenever possible, resorting to the first
   when needed.

   ::

       sage: maple('(x^12-1)/(x-1)').simplify()     # optional - maple
       (x+1)*(x^2+1)*(x^2+x+1)*(x^2-x+1)*(x^4-x^2+1)


The normal command will always reduce a rational function to the
lowest terms. The factor command will factor a polynomial with
rational coefficients into irreducible factors over the ring of
integers. So for example,

::

    sage: maple('(x^12-1)').factor( )           # optional - maple
    (x-1)*(x+1)*(x^2+x+1)*(x^2-x+1)*(x^2+1)*(x^4-x^2+1)

::

    sage: maple('(x^28-1)').factor( )           # optional - maple
    (x-1)*(x^6+x^5+x^4+x^3+x^2+x+1)*(x+1)*(x^6-x^5+x^4-x^3+x^2-x+1)*(x^2+1)*(x^12-x^10+x^8-x^6+x^4-x^2+1)

Another important feature of maple is its online help. We can
access this through sage as well. After reading the description of
the command, you can press :kbd:`q` to immediately get back to your
original prompt.

Incidentally you can always get into a maple console by the
command ::

    sage: maple.console()          # not tested
    sage: !maple                   # not tested

Note that the above two commands are slightly different, and the
first is preferred.

For example, for help on the maple command fibonacci, we type

::

    sage: maple.help('fibonacci')  # not tested, since it uses a pager

We see there are two choices. Type

::

    sage: maple.help('combinat, fibonacci')   # not tested, since it uses a pager

We now see how the Maple command fibonacci works under the
combinatorics package. Try typing in

::

    sage: maple.fibonacci(10)                # optional - maple
    fibonacci(10)

You will get fibonacci(10) as output since Maple has not loaded the
combinatorics package yet. To rectify this type

::

    sage: maple('combinat[fibonacci]')(10)     # optional - maple
    55

instead.

If you want to load the combinatorics package for future
calculations, in Sage this can be done as

::

    sage: maple.with_package('combinat')       # optional - maple

or

::

    sage: maple.load('combinat')               # optional - maple

Now if we type ``maple.fibonacci(10)``, we get the
correct output::

    sage: maple.fibonacci(10)                  # optional - maple
    55

Some common maple packages include ``combinat``,
``linalg``, and ``numtheory``. To produce
the first 19 Fibonacci numbers, use the sequence command.

::

    sage: maple('seq(fibonacci(i),i=1..19)')     # optional - maple
    1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584,
    4181

Two other useful Maple commands are ifactor and isprime. For
example

::

    sage: maple.isprime(maple.fibonacci(27))     # optional - maple
    false
    sage: maple.ifactor(maple.fibonacci(27))     # optional - maple
    ``(2)*``(17)*``(53)*``(109)

Note that the isprime function that is included with Sage (which
uses PARI) is better than the Maple one (it is faster and gives a
provably correct answer, whereas Maple is sometimes wrong).

::

    sage: # optional - maple
    sage: alpha = maple('(1+sqrt(5))/2')
    sage: beta = maple('(1-sqrt(5))/2')
    sage: f19  = alpha^19 - beta^19/maple('sqrt(5)')
    sage: f19
    (1/2+1/2*5^(1/2))^19-1/5*(1/2-1/2*5^(1/2))^19*5^(1/2)
    sage: f19.simplify()          # somewhat randomly ordered output
    6765+5778/5*5^(1/2)

Let's say we want to write a maple program now that squares a
number if it is positive and cubes it if it is negative. In maple,
that would look like

::

    mysqcu := proc(x)
    if x > 0 then x^2;
    else x^3; fi;
    end;

In Sage, we write

::

    sage: mysqcu = maple('proc(x) if x > 0 then x^2 else x^3 fi end')    # optional - maple
    sage: mysqcu(5)                                                      # optional - maple
    25
    sage: mysqcu(-5)                                                     # optional - maple
    -125

More complicated programs should be put in a separate file and
loaded.
"""
from sage.cpython.string import bytes_to_str as bytes_to_str
from sage.env import DOT_SAGE as DOT_SAGE
from sage.interfaces.expect import Expect as Expect, ExpectElement as ExpectElement, ExpectFunction as ExpectFunction, FunctionElement as FunctionElement, gc_disabled as gc_disabled
from sage.interfaces.tab_completion import ExtraTabCompletion as ExtraTabCompletion
from sage.misc.instancedoc import instancedoc as instancedoc
from sage.misc.pager import pager as pager
from sage.structure.richcmp import rich_to_bool as rich_to_bool

COMMANDS_CACHE: str

class Maple(ExtraTabCompletion, Expect):
    """
    Interface to the Maple interpreter.

    Type ``maple.[tab]`` for a list of all the functions
    available from your Maple install. Type
    ``maple.[tab]?`` for Maple's help about a given
    function. Type ``maple(...)`` to create a new Maple
    object, and ``maple.eval(...)`` to run a string using
    Maple (and get the result back as a string).
    """
    def __init__(self, maxread=None, script_subdirectory=None, server=None, server_tmpdir=None, logfile=None, ulimit=None) -> None:
        """
        Create an instance of the Maple interpreter.

        EXAMPLES::

            sage: from sage.interfaces.maple import maple
            sage: maple == loads(dumps(maple))
            True
        """
    def __reduce__(self):
        """
        EXAMPLES::

            sage: Maple().__reduce__()
            (<function reduce_load_Maple at 0x...>, ())
            sage: f, args = _
            sage: f(*args)
            Maple
        """
    def expect(self):
        """
        Return the pexpect object for this Maple session.

        EXAMPLES::

            sage: # optional - maple
            sage: m = Maple()
            sage: m.expect() is None
            True
            sage: m._start()
            sage: m.expect()
            Maple with PID ...
            sage: m.quit()
        """
    def console(self) -> None:
        """
        Spawn a new Maple command-line session.

        EXAMPLES::

            sage: maple.console()  # not tested
                |\\^/|     Maple 2019 (X86 64 LINUX)
            ._|\\|   |/|_. Copyright (c) Maplesoft, a division of Waterloo Maple Inc. 2019
             \\  MAPLE  /  All rights reserved. Maple is a trademark of
             <____ ____>  Waterloo Maple Inc.
                  |       Type ? for help.
        """
    def completions(self, s):
        """
        Return all commands that complete the command starting with the
        string ``s``.

        This is like typing ``s`` + :kbd:`Ctrl` + :kbd:`T`
        in the Maple interpreter.

        EXAMPLES::

            sage: c = maple.completions('di')  # optional - maple
            sage: 'divide' in c                # optional - maple
            True
        """
    def cputime(self, t=None):
        """
        Return the amount of CPU time that the Maple session has used.

        If ``t`` is not None, then it returns the difference
        between the current CPU time and ``t``.

        EXAMPLES::

            sage: # optional - maple
            sage: t = maple.cputime()
            sage: t                   # random
            0.02
            sage: x = maple('x')
            sage: maple.diff(x^2, x)
            2*x
            sage: maple.cputime(t)    # random
            0.0
        """
    def set(self, var, value) -> None:
        """
        Set the variable ``var`` to the given ``value``.

        EXAMPLES::

            sage: maple.set('xx', '2') # optional - maple
            sage: maple.get('xx')      # optional - maple
            '2'
        """
    def get(self, var):
        """
        Get the value of the variable ``var``.

        EXAMPLES::

            sage: maple.set('xx', '2') # optional - maple
            sage: maple.get('xx')      # optional - maple
            '2'
        """
    def source(self, s) -> None:
        """
        Display the Maple source (if possible) about ``s``.

        This is the same as
        returning the output produced by the following Maple commands:

        interface(verboseproc=2): print(s)

        INPUT:

        - ``s`` -- string representing the function whose
          source code you want

        EXAMPLES::

            sage: maple.source('curry')  # not tested
            ... -> subs('_X' = _passed[2 .. _npassed],() -> ...(_X, _passed))
        """
    def help(self, string) -> None:
        '''
        Display Maple help about ``string``.

        This is the same as typing "?string" in the Maple console.

        INPUT:

        - ``string`` -- string to search for in the maple help
          system

        EXAMPLES::

            sage: maple.help(\'Psi\')  # not tested
            Psi - the Digamma and Polygamma functions
            ...
        '''
    def with_package(self, package) -> None:
        """
        Make a package of Maple procedures available in the interpreter.

        INPUT:

        - ``package`` -- string

        EXAMPLES: Some functions are unknown to Maple until you use with to
        include the appropriate package.

        ::

            sage: # optional - maple
            sage: maple.quit()   # reset maple
            sage: maple('partition(10)')
            partition(10)
            sage: maple('bell(10)')
            bell(10)
            sage: maple.with_package('combinat')
            sage: maple('partition(10)')
            [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 2], [1, 1, 1, 1, 1, 1, 2, 2], [1, 1, 1, 1, 2, 2, 2], [1, 1, 2, 2, 2, 2], [2, 2, 2, 2, 2], [1, 1, 1, 1, 1, 1, 1, 3], [1, 1, 1, 1, 1, 2, 3], [1, 1, 1, 2, 2, 3], [1, 2, 2, 2, 3], [1, 1, 1, 1, 3, 3], [1, 1, 2, 3, 3], [2, 2, 3, 3], [1, 3, 3, 3], [1, 1, 1, 1, 1, 1, 4], [1, 1, 1, 1, 2, 4], [1, 1, 2, 2, 4], [2, 2, 2, 4], [1, 1, 1, 3, 4], [1, 2, 3, 4], [3, 3, 4], [1, 1, 4, 4], [2, 4, 4], [1, 1, 1, 1, 1, 5], [1, 1, 1, 2, 5], [1, 2, 2, 5], [1, 1, 3, 5], [2, 3, 5], [1, 4, 5], [5, 5], [1, 1, 1, 1, 6], [1, 1, 2, 6], [2, 2, 6], [1, 3, 6], [4, 6], [1, 1, 1, 7], [1, 2, 7], [3, 7], [1, 1, 8], [2, 8], [1, 9], [10]]
            sage: maple('bell(10)')
            115975
            sage: maple('fibonacci(10)')
            55
        """
    load = with_package
    def clear(self, var) -> None:
        """
        Clear the variable named ``var``.

        To clear a Maple variable, you must assign 'itself' to itself.
        In Maple 'expr' prevents expr to be evaluated.

        EXAMPLES::

            sage: # optional - maple
            sage: maple.set('xx', '2')
            sage: maple.get('xx')
            '2'
            sage: maple.clear('xx')
            sage: maple.get('xx')
            'xx'
        """

class MapleFunction(ExpectFunction): ...
class MapleFunctionElement(FunctionElement): ...

class MapleElement(ExtraTabCompletion, ExpectElement):
    def __float__(self) -> float:
        """
        Return a floating point version of ``self``.

        EXAMPLES::

            sage: float(maple(1/2))  # optional - maple
            0.5
            sage: type(_)            # optional - maple
            <... 'float'>
        """
    def __hash__(self):
        """
        Return a 64-bit integer representing the hash of ``self``. Since
        Python uses 32-bit hashes, it will automatically convert the result
        of this to a 32-bit hash.

        These examples are optional, and require Maple to be installed. You
        don't need to install any Sage packages for this.

        EXAMPLES::

            sage: # optional - maple
            sage: m = maple('x^2+y^2')
            sage: m.__hash__()          # random
            188724254834261060184983038723355865733
            sage: hash(m)               # random
            5035731711831192733
            sage: m = maple('x^2+y^3')
            sage: m.__hash__()          # random
            264835029579301191531663246434344770556
            sage: hash(m)               # random
            -2187277978252104690
        """
    def op(self, i=None):
        """
        Return the `i`-th operand of this expression.

        INPUT:

        - ``i`` -- integer or ``None``

        EXAMPLES::

            sage: V = maple(vector(QQ,[4,5,6]))      # optional - maple
            sage: V.op(1)                            # optional - maple
            3
            sage: V.op(2)                            # optional - maple
            {1 = 4, 2 = 5, 3 = 6}
        """

maple: Maple

def reduce_load_Maple():
    """
    Return the maple object created in sage.interfaces.maple.

    EXAMPLES::

        sage: from sage.interfaces.maple import reduce_load_Maple
        sage: reduce_load_Maple()
        Maple
    """
def maple_console() -> None:
    """
    Spawn a new Maple command-line session.

    EXAMPLES::

        sage: maple_console() #not tested
            |^/|     Maple 11 (IBM INTEL LINUX)
        ._|\\|   |/|_. Copyright (c) Maplesoft, a division of Waterloo Maple Inc. 2007
         \\  MAPLE  /  All rights reserved. Maple is a trademark of
         <____ ____>  Waterloo Maple Inc.
              |       Type ? for help.
        >
    """
