import types
from sage.libs.gap.libgap import libgap as libgap

class GlobalVariableContext:
    def __init__(self, variable, value) -> None:
        """
        Context manager for GAP global variables.

        It is recommended that you use the
        :meth:`sage.libs.gap.libgap.Gap.global_context` method and not
        construct objects of this class manually.

        INPUT:

        - ``variable`` -- string; the variable name

        - ``value`` -- anything that defines a GAP object

        EXAMPLES::

            sage: libgap.set_global('FooBar', 1)
            sage: with libgap.global_context('FooBar', 2):
            ....:     print(libgap.get_global('FooBar'))
            2
            sage: libgap.get_global('FooBar')
            1
        """
    def __enter__(self) -> None:
        """
        Called when entering the with-block.

        EXAMPLES::

            sage: libgap.set_global('FooBar', 1)
            sage: with libgap.global_context('FooBar', 2):
            ....:     print(libgap.get_global('FooBar'))
            2
            sage: libgap.get_global('FooBar')
            1
        """
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None):
        """
        Called when exiting the with-block.

        EXAMPLES::

            sage: libgap.set_global('FooBar', 1)
            sage: with libgap.global_context('FooBar', 2):
            ....:     print(libgap.get_global('FooBar'))
            2
            sage: libgap.get_global('FooBar')
            1
        """
