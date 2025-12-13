from .sage0 import Sage as Sage, SageElement as SageElement

number: int

class PSage(Sage):
    def __init__(self, **kwds) -> None: ...
    def is_locked(self) -> bool: ...
    def __del__(self) -> None:
        """
        TESTS:

        Check that :issue:`29989` is fixed::

            sage: PSage().__del__()
        """
    def eval(self, x, strip: bool = True, **kwds):
        """
        INPUT:

        - ``x`` -- code
        - ``strip`` --ignored
        """
    def get(self, var):
        """
        Get the value of the variable var.
        """
    def set(self, var, value) -> None:
        """
        Set the variable var to the given value.
        """

class PSageElement(SageElement):
    def is_locked(self): ...
