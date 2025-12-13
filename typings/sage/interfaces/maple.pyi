from _typeshed import Incomplete
from sage.cpython.string import bytes_to_str as bytes_to_str
from sage.env import DOT_SAGE as DOT_SAGE
from sage.interfaces.expect import Expect as Expect, ExpectElement as ExpectElement, ExpectFunction as ExpectFunction, FunctionElement as FunctionElement, gc_disabled as gc_disabled
from sage.interfaces.tab_completion import ExtraTabCompletion as ExtraTabCompletion
from sage.misc.instancedoc import instancedoc as instancedoc
from sage.misc.pager import pager as pager
from sage.structure.richcmp import rich_to_bool as rich_to_bool

COMMANDS_CACHE: Incomplete

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

maple: Incomplete

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
