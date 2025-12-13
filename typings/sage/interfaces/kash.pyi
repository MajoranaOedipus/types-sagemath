from .expect import Expect as Expect, ExpectElement as ExpectElement
from _typeshed import Incomplete
from sage.misc.instancedoc import instancedoc as instancedoc
from sage.misc.sage_eval import sage_eval as sage_eval

class Kash(Expect):
    """
    Interface to the Kash interpreter.

    AUTHORS:

    - William Stein and David Joyner
    """
    def __init__(self, max_workspace_size=None, maxread=None, script_subdirectory=None, restart_on_ctrlc: bool = True, logfile=None, server=None, server_tmpdir=None) -> None:
        """
        INPUT:

        - ``max_workspace_size`` -- (default: ``None``)
          set maximal workspace memory usage to <mem>
          <mem> stands for byte-wise allocation
          <mem>k stands for kilobyte-wise allocation
          <mem>m stands for megabyte-wise allocation
        """
    def clear(self, var) -> None:
        """
        Clear the variable named ``var``.

        Kash variables have a record structure, so if sage1 is a
        polynomial ring, sage1.1 will be its indeterminate.  This
        prevents us from easily reusing variables, since sage1.1
        might still have references even if sage1 does not.

        For now, we don't implement variable clearing to avoid these
        problems, and instead implement this method with a noop.
        """
    def __reduce__(self): ...
    def eval(self, x, newlines: bool = False, strip: bool = True, **kwds):
        """
        Send the code in the string s to the Kash interpreter and return
        the output as a string.

        INPUT:

        - ``s`` -- string containing Kash code

        - ``newlines`` -- boolean (default: ``True``); if ``False``,
          remove all backslash-newlines inserted by the Kash output formatter

        - ``strip`` -- ignored
        """
    def help(self, name=None) -> None:
        """
        Return help on KASH commands.

        This returns help on all commands with a given name.  If name
        is ``None``, return the location of the installed Kash HTML
        documentation.

        EXAMPLES::

            sage: X = kash.help('IntegerRing')   # random; optional -- kash
            1439: IntegerRing() -> <ord^rat>
            1440: IntegerRing(<elt-ord^rat> m) -> <res^rat>
            1441: IntegerRing(<seq()> Q) -> <res^rat>
            1442: IntegerRing(<fld^rat> K) -> <ord^rat>
            1443: IntegerRing(<fld^fra> K) -> <ord^num>
            1444: IntegerRing(<rng> K) -> <rng>
            1445: IntegerRing(<fld^pad> L) -> <ord^pad>

        There is one entry in X for each item found in the documentation
        for this function: If you type ``print(X[0])`` you will
        get help on about the first one, printed nicely to the screen.

        AUTHORS:

        - Sebastion Pauli (2006-02-04): during Sage coding sprint
        """
    def help_search(self, name): ...
    def set(self, var, value) -> None:
        """
        Set the variable var to the given value.
        """
    def get(self, var):
        """
        Get the value of the variable var.
        """
    def function_call(self, function, args=None, kwds=None):
        """
        EXAMPLES::

            sage: kash.function_call('ComplexToPolar', [1+I], {'Results' : 1})   # optional -- kash
            1.41421356237309504880168872421
        """
    def console(self) -> None: ...
    def version(self): ...

class KashElement(ExpectElement):
    def __mod__(self, other): ...
    def __len__(self) -> int: ...
    def __bool__(self) -> bool:
        """
        Return ``True`` if this Kash element is not 0 or FALSE.

        EXAMPLES::

            sage: bool(kash('FALSE'))                   # optional -- kash
            False
            sage: bool(kash('TRUE'))                    # optional -- kash
            True

            sage: bool(kash(0))                         # optional -- kash
            False
            sage: bool(kash(1))                         # optional -- kash
            True
        """

class KashDocumentation(list): ...

def is_KashElement(x):
    """
    Return ``True`` if ``x`` is of type :class:`KashElement`.

    EXAMPLES::

        sage: from sage.interfaces.kash import is_KashElement
        sage: is_KashElement(2)
        doctest:...: DeprecationWarning: the function is_KashElement is deprecated; use isinstance(x, sage.interfaces.abc.KashElement) instead
        See https://github.com/sagemath/sage/issues/34804 for details.
        False
        sage: is_KashElement(kash(2))  # optional - kash
        True
    """

kash: Incomplete

def reduce_load_Kash(): ...
def kash_console() -> None: ...
def kash_version(): ...
