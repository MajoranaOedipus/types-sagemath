import _cython_3_2_1
from sage.categories.category import ZZ_sage as ZZ_sage
from sage.libs.ntl.ntl_ZZ_pEContext import ntl_ZZ_pEContext as ntl_ZZ_pEContext
from sage.rings.integer_ring import IntegerRing as IntegerRing
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

make_ZZ_pE: _cython_3_2_1.cython_function_or_method

class ntl_ZZ_pE:
    """ntl_ZZ_pE(v=None, modulus=None)

    File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pE.pyx (starting at line 51)

    The \\class{ZZ_pE} class is used to model `\\Z / p\\Z [x] / (f(x))`.
    The modulus `p` may be any positive integer, not necessarily prime,
    and the modulus f is not required to be irreducible.

    Objects of the class \\class{ZZ_pE} are represented as a \\code{ZZ_pX} of
    degree less than the degree of `f`.

    Each \\class{ZZ_pE} contains a pointer of a \\class{ZZ_pEContext} which
    contains pre-computed data for NTL.  These can be explicitly constructed
    and passed to the constructor of a \\class{ZZ_pE} or the \\class{ZZ_pEContext}
    method \\code{ZZ_pE} can be used to construct a \\class{ZZ_pE} element.

    This class takes care of making sure that the C++ library NTL global
    variable is set correctly before performing any arithmetic."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, v=..., modulus=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pE.pyx (starting at line 69)

                Initialize an ntl ZZ_pE.

                EXAMPLES::

                    sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1],11))
                    sage: c.ZZ_pE([13,4,1])
                    [1 3]
                    sage: c.ZZ_pE(Integer(95413094))
                    [7]
                    sage: c.ZZ_pE('[1]')
                    [1]

                AUTHOR: David Roe (2007-9-25)
        """
    @overload
    def get_as_ZZ_pX_doctest(self) -> Any:
        """ntl_ZZ_pE.get_as_ZZ_pX_doctest(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pE.pyx (starting at line 282)

        This method exists solely for automated testing of get_as_ZZ_pX().

        sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1],11))
        sage: x = ntl.ZZ_pE([42,1],modulus=c)
        sage: i = x.get_as_ZZ_pX_doctest()
        sage: i
        [9 1]
        sage: type(i)
        <class 'sage.libs.ntl.ntl_ZZ_pX.ntl_ZZ_pX'>"""
    @overload
    def get_as_ZZ_pX_doctest(self) -> Any:
        """ntl_ZZ_pE.get_as_ZZ_pX_doctest(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pE.pyx (starting at line 282)

        This method exists solely for automated testing of get_as_ZZ_pX().

        sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1],11))
        sage: x = ntl.ZZ_pE([42,1],modulus=c)
        sage: i = x.get_as_ZZ_pX_doctest()
        sage: i
        [9 1]
        sage: type(i)
        <class 'sage.libs.ntl.ntl_ZZ_pX.ntl_ZZ_pX'>"""
    def get_modulus_context(self) -> Any:
        """ntl_ZZ_pE.get_modulus_context(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pE.pyx (starting at line 169)"""
    @overload
    def modulus(self) -> Any:
        """ntl_ZZ_pE.modulus(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pE.pyx (starting at line 321)

        Return the modulus as an NTL ZZ_pX.

        sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1],11))
        sage: n=ntl.ZZ_pE([2983,233],c)
        sage: n.modulus()
        [1 1 1]"""
    @overload
    def modulus(self) -> Any:
        """ntl_ZZ_pE.modulus(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pE.pyx (starting at line 321)

        Return the modulus as an NTL ZZ_pX.

        sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1],11))
        sage: n=ntl.ZZ_pE([2983,233],c)
        sage: n.modulus()
        [1 1 1]"""
    def set_from_ZZ_pX_doctest(self, value) -> Any:
        """ntl_ZZ_pE.set_from_ZZ_pX_doctest(self, value)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pE.pyx (starting at line 303)

        This method exists solely for automated testing of set_from_ZZ_pX().

        sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1],11))
        sage: x = ntl.ZZ_pE(modulus=c)
        sage: x.set_from_ZZ_pX_doctest(ntl.ZZ_pX([5,2,1],11))
        sage: x
        [4 1]"""
    def __add__(self, ntl_ZZ_pEself, other) -> Any:
        """ntl_ZZ_pE.__add__(ntl_ZZ_pE self, other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pE.pyx (starting at line 240)"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __invert__(self) -> Any:
        """ntl_ZZ_pE.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pE.pyx (starting at line 203)

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([2,7,1],11))
            sage: ~ntl.ZZ_pE([1,1],modulus=c)
            [7 3]"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __mul__(self, ntl_ZZ_pEself, other) -> Any:
        """ntl_ZZ_pE.__mul__(ntl_ZZ_pE self, other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pE.pyx (starting at line 218)"""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __neg__(self) -> Any:
        """ntl_ZZ_pE.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pE.pyx (starting at line 254)"""
    def __pow__(self, ntl_ZZ_pEself, longe, ignored) -> Any:
        """ntl_ZZ_pE.__pow__(ntl_ZZ_pE self, long e, ignored)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pE.pyx (starting at line 262)"""
    def __radd__(self, other):
        """Return value+self."""
    def __reduce__(self) -> Any:
        """ntl_ZZ_pE.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pE.pyx (starting at line 159)

        EXAMPLES::

            sage: a = ntl.ZZ_pE([4],ntl.ZZ_pX([1,1,1],ntl.ZZ(7)))
            sage: loads(dumps(a)) == a
            True"""
    def __rmul__(self, other):
        """Return value*self."""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
    def __rsub__(self, other):
        """Return value-self."""
    def __sub__(self, ntl_ZZ_pEself, other) -> Any:
        """ntl_ZZ_pE.__sub__(ntl_ZZ_pE self, other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pE.pyx (starting at line 230)"""
