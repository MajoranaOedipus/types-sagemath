from _typeshed import Incomplete
from sage.env import DOT_SAGE as DOT_SAGE, LIE_INFO_DIR as LIE_INFO_DIR
from sage.interfaces.expect import Expect as Expect, ExpectElement as ExpectElement, ExpectFunction as ExpectFunction, FunctionElement as FunctionElement
from sage.interfaces.interface import AsciiArtString as AsciiArtString
from sage.interfaces.tab_completion import ExtraTabCompletion as ExtraTabCompletion
from sage.misc.instancedoc import instancedoc as instancedoc
from sage.misc.misc_c import prod as prod
from sage.misc.sage_eval import sage_eval as sage_eval

COMMANDS_CACHE: Incomplete
HELP_CACHE: Incomplete

class LiE(ExtraTabCompletion, Expect):
    """
    Interface to the LiE interpreter.

    Type ``lie.[tab]`` for a list of all the functions available
    from your LiE install.  Type ``lie.[tab]?`` for LiE's
    help about a given function.  Type ``lie(...)`` to create
    a new LiE object, and ``lie.eval(...)`` to run a string
    using LiE (and get the result back as a string).
    """
    def __init__(self, maxread=None, script_subdirectory=None, logfile=None, server=None) -> None:
        """
        EXAMPLES::

            sage: from sage.interfaces.lie import lie
            sage: lie == loads(dumps(lie))
            True
        """
    def __reduce__(self):
        """
        EXAMPLES::

            sage: LiE().__reduce__()
            (<function reduce_load_lie at 0x...>, ())
        """
    def read(self, filename) -> None:
        """
        EXAMPLES::

            sage: filename = tmp_filename()
            sage: with open(filename, 'w') as f:
            ....:     _ = f.write('x = 2\\n')
            sage: lie.read(filename)  # optional - lie
            sage: lie.get('x')        # optional - lie
            '2'
            sage: import os
            sage: os.unlink(filename)
        """
    def console(self) -> None:
        """
        Spawn a new LiE command-line session.

        EXAMPLES::

            sage: lie.console()                    # not tested
            LiE version 2.2.2 created on Sep 26 2007 at 18:13:19
            Authors: Arjeh M. Cohen, Marc van Leeuwen, Bert Lisser.
            Free source code distribution
            ...
        """
    def version(self) -> str:
        """
        EXAMPLES::

            sage: lie.version() # optional - lie
            '2...'
        """
    def help(self, command):
        """
        Return a string of the LiE help for command.

        EXAMPLES::

            sage: lie.help('diagram') # optional - lie
            'diagram(g)...'
        """
    def eval(self, code, strip: bool = True, **kwds):
        """
        EXAMPLES::

            sage: lie.eval('2+2')  # optional - lie
            '4'
        """
    def set(self, var, value) -> None:
        """
        Set the variable var to the given value.

        EXAMPLES::

            sage: lie.set('x', '2')  # optional - lie
            sage: lie.get('x')       # optional - lie
            '2'
        """
    def get(self, var):
        """
        Get the value of the variable var.

        EXAMPLES::

            sage: lie.set('x', '2')  # optional - lie
            sage: lie.get('x')       # optional - lie
            '2'
        """
    def get_using_file(self, var) -> None:
        """
        EXAMPLES::

            sage: lie.get_using_file('x')
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    def function_call(self, function, args=None, kwds=None):
        '''
        EXAMPLES::

            sage: lie.function_call("diagram", args=[\'A4\']) # optional - lie
            O---O---O---O
            1   2   3   4
            A4
        '''

class LiEElement(ExtraTabCompletion, ExpectElement):
    def type(self):
        """
        EXAMPLES::

            sage: m = lie('[[1,0,3,3],[12,4,-4,7],[-1,9,8,0],[3,-5,-2,9]]') # optional - lie
            sage: m.type() # optional - lie
            'mat'
        """

class LiEFunctionElement(FunctionElement): ...
class LiEFunction(ExpectFunction): ...

def is_LiEElement(x) -> bool:
    """
    EXAMPLES::

        sage: from sage.interfaces.lie import is_LiEElement
        sage: is_LiEElement(2)
        doctest:...: DeprecationWarning: the function is_LiEElement is deprecated; use isinstance(x, sage.interfaces.abc.LiEElement) instead
        See https://github.com/sagemath/sage/issues/34804 for details.
        False
        sage: l = lie(2) # optional - lie
        sage: is_LiEElement(l) # optional - lie
        True
    """

lie: Incomplete

def reduce_load_lie():
    """
    EXAMPLES::

        sage: from sage.interfaces.lie import reduce_load_lie
        sage: reduce_load_lie()
        LiE Interpreter
    """
def lie_console() -> None:
    """
    Spawn a new LiE command-line session.

    EXAMPLES::

        sage: from sage.interfaces.lie import lie_console
        sage: lie_console()                    # not tested
        LiE version 2.2.2 created on Sep 26 2007 at 18:13:19
        Authors: Arjeh M. Cohen, Marc van Leeuwen, Bert Lisser.
        Free source code distribution
        ...
    """
def lie_version():
    """
    EXAMPLES::

        sage: from sage.interfaces.lie import lie_version
        sage: lie_version() # optional - lie
        '2...'
    """
