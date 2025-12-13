from sage.libs.ntl.ntl_GF2EContext import ntl_GF2EContext as ntl_GF2EContext
from sage.libs.ntl.ntl_ZZ import unpickle_class_args as unpickle_class_args
from typing import Any, ClassVar

class ntl_GF2EX:
    """ntl_GF2EX(modulus=None, x=[])

    File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2EX.pyx (starting at line 44)

    Minimal wrapper of NTL's GF2EX class."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, modulus=..., x=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2EX.pyx (starting at line 48)

                Minimal wrapper of NTL's GF2EX class.

                EXAMPLES::

                    sage: ctx = ntl.GF2EContext(ntl.GF2X([1,1,0,1,1,0,1]))
                    sage: ntl.GF2EX(ctx, '[[1 0] [2 1]]')
                    [[1] [0 1]]
        """
    def modulus_context(self) -> Any:
        """ntl_GF2EX.modulus_context(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2EX.pyx (starting at line 102)"""
    def __add__(self, ntl_GF2EXself, other) -> Any:
        """ntl_GF2EX.__add__(ntl_GF2EX self, other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2EX.pyx (starting at line 201)

        EXAMPLES::

            sage: ctx = ntl.GF2EContext(ntl.GF2X([1,1,0,1,1,0,1]))
            sage: f = ntl.GF2EX(ctx, '[[1 0] [2 1]]')
            sage: g = ntl.GF2EX(ctx, '[[1 0 1 1] [0 1 1 0 1] [1 0 1]]')
            sage: f+g ## indirect doctest
            [[0 0 1 1] [0 0 1 0 1] [1 0 1]]"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __mul__(self, ntl_GF2EXself, other) -> Any:
        """ntl_GF2EX.__mul__(ntl_GF2EX self, other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2EX.pyx (starting at line 161)

        EXAMPLES::

            sage: ctx = ntl.GF2EContext(ntl.GF2X([1,1,0,1,1,0,1]))
            sage: f = ntl.GF2EX(ctx, '[[1 0] [2 1]]')
            sage: g = ntl.GF2EX(ctx, '[[1 0 1 1] [0 1 1 0 1] [1 0 1]]')
            sage: f*g ## indirect doctest
            [[1 0 1 1] [0 0 1 1] [1 0 0 1 0 1] [0 1 0 1]]"""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __neg__(self) -> Any:
        """ntl_GF2EX.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2EX.pyx (starting at line 221)

        EXAMPLES::

            sage: ctx = ntl.GF2EContext(ntl.GF2X([1,1,0,1,1,0,1]))
            sage: f = ntl.GF2EX(ctx, '[[1 0] [2 1]]')
            sage: -f ## indirect doctest
            [[1] [0 1]]"""
    def __pow__(self, ntl_GF2EXself, longe, ignored) -> Any:
        """ntl_GF2EX.__pow__(ntl_GF2EX self, long e, ignored)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2EX.pyx (starting at line 236)

        EXAMPLES::

            sage: ctx = ntl.GF2EContext(ntl.GF2X([1,1,0,1,1,0,1]))
            sage: f = ntl.GF2EX(ctx, '[[1 0] [2 1]]')
            sage: f**2 ## indirect doctest
            [[1] [] [0 0 1]]"""
    def __radd__(self, other):
        """Return value+self."""
    def __reduce__(self) -> Any:
        """ntl_GF2EX.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2EX.pyx (starting at line 109)

        EXAMPLES::

            sage: ctx = ntl.GF2EContext(ntl.GF2X([1,1,0,1,1,0,1]))
            sage: f = ntl.GF2EX(ctx, '[[1 0 1] [1 0 0 1] [1]]')
            sage: f == loads(dumps(f))
            True"""
    def __rmul__(self, other):
        """Return value*self."""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
    def __rsub__(self, other):
        """Return value-self."""
    def __sub__(self, ntl_GF2EXself, other) -> Any:
        """ntl_GF2EX.__sub__(ntl_GF2EX self, other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2EX.pyx (starting at line 181)

        EXAMPLES::

            sage: ctx = ntl.GF2EContext(ntl.GF2X([1,1,0,1,1,0,1]))
            sage: f = ntl.GF2EX(ctx, '[[1 0] [2 1]]')
            sage: g = ntl.GF2EX(ctx, '[[1 0 1 1] [0 1 1 0 1] [1 0 1]]')
            sage: f-g ## indirect doctest
            [[0 0 1 1] [0 0 1 0 1] [1 0 1]]"""
