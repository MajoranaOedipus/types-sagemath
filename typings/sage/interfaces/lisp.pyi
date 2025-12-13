from _typeshed import Incomplete
from sage.interfaces.expect import Expect as Expect, ExpectElement as ExpectElement, ExpectFunction as ExpectFunction, FunctionElement as FunctionElement, gc_disabled as gc_disabled
from sage.misc.instancedoc import instancedoc as instancedoc
from sage.structure.element import RingElement as RingElement, parent as parent
from sage.structure.richcmp import rich_to_bool as rich_to_bool

class Lisp(Expect):
    def __init__(self, maxread=None, script_subdirectory=None, logfile=None, server=None, server_tmpdir=None) -> None:
        """
        EXAMPLES::

            sage: from sage.interfaces.lisp import lisp
            sage: lisp == loads(dumps(lisp))
            True
        """
    def eval(self, code, strip: bool = True, **kwds):
        """
        EXAMPLES::

            sage: lisp.eval('(+ 2 2)')
            '4'

        TESTS:

        Verify that it works when input == output::

            sage: lisp.eval('2')
            '2'
        """
    def set(self, var, value) -> None:
        """
        Set the variable var to the given value.

        EXAMPLES::

            sage: lisp.set('x', '2')
            sage: lisp.get('x')
            '2'

        TESTS:

        It must also be possible to eval the variable by name::

            sage: lisp.eval('x')
            '2'
        """
    def get(self, var):
        """
        EXAMPLES::

            sage: lisp.set('x', '2')
            sage: lisp.get('x')
            '2'
        """
    def __reduce__(self):
        """
        EXAMPLES::

            sage: Lisp().__reduce__()
            (<function reduce_load_Lisp at 0x...>, ())
        """
    def kill(self, var) -> None:
        """
        EXAMPLES::

            sage: lisp.kill('x')
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    def console(self) -> None:
        """
        Spawn a new Lisp command-line session.

        EXAMPLES::

            sage: lisp.console() #not tested
            ECL (Embeddable Common-Lisp) ...
            Copyright (C) 1984 Taiichi Yuasa and Masami Hagiya
            Copyright (C) 1993 Giuseppe Attardi
            Copyright (C) 2000 Juan J. Garcia-Ripoll
            ECL is free software, and you are welcome to redistribute it
            under certain conditions; see file 'Copyright' for details.
            Type :h for Help.  Top level.
            ...
        """
    def version(self):
        """
        Return the version of Lisp being used.

        EXAMPLES::

            sage: lisp.version()
            'Version information is given by lisp.console().'
        """
    def help(self, command) -> None:
        """
        EXAMPLES::

            sage: lisp.help('setq')
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    def function_call(self, function, args=None, kwds=None):
        """
        Call the Lisp function with given ``args`` and ``kwds``.
        For Lisp functions, the ``kwds`` are ignored.

        EXAMPLES::

            sage: lisp.function_call('sin', ['2'])
            0.9092974
            sage: lisp.sin(2)
            0.9092974
        """

class LispElement(RingElement, ExpectElement):
    def __bool__(self) -> bool:
        """
        EXAMPLES::

            sage: lisp(2).bool()
            True
            sage: lisp(0).bool()
            False
            sage: bool(lisp(2))
            True
            sage: bool(lisp('T'))
            True
            sage: bool(lisp('NIL'))
            False
        """
    def __pow__(self, n):
        """
        EXAMPLES::

            sage: a = lisp(3)
            sage: a^3
            27
        """

class LispFunctionElement(FunctionElement): ...
class LispFunction(ExpectFunction): ...

def is_LispElement(x):
    """
    EXAMPLES::

        sage: from sage.interfaces.lisp import is_LispElement
        sage: is_LispElement(2)
        doctest:...: DeprecationWarning: the function is_LispElement is deprecated; use isinstance(x, sage.interfaces.abc.LispElement) instead
        See https://github.com/sagemath/sage/issues/34804 for details.
        False
        sage: is_LispElement(lisp(2))
        True
    """

lisp: Incomplete

def reduce_load_Lisp():
    """
    EXAMPLES::

        sage: from sage.interfaces.lisp import reduce_load_Lisp
        sage: reduce_load_Lisp()
        Lisp Interpreter
    """
def lisp_console() -> None:
    """
    Spawn a new Lisp command-line session.

    EXAMPLES::

        sage: lisp.console() #not tested
        ECL (Embeddable Common-Lisp) ...
        Copyright (C) 1984 Taiichi Yuasa and Masami Hagiya
        Copyright (C) 1993 Giuseppe Attardi
        Copyright (C) 2000 Juan J. Garcia-Ripoll
        ECL is free software, and you are welcome to redistribute it
        under certain conditions; see file 'Copyright' for details.
        Type :h for Help.  Top level.
        ...
    """
