import _cython_3_2_1
from sage.categories.category import ZZ_sage as ZZ_sage
from sage.libs.ntl.ntl_ZZ import unpickle_class_args as unpickle_class_args
from sage.libs.ntl.ntl_ZZ_pContext import ntl_ZZ_pContext as ntl_ZZ_pContext
from sage.rings.integer_ring import IntegerRing as IntegerRing
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

ntl_ZZ_p_random_element: _cython_3_2_1.cython_function_or_method

class ntl_ZZ_p:
    """ntl_ZZ_p(v=None, modulus=None)

    File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_p.pyx (starting at line 76)

    The \\class{ZZ_p} class is used to represent integers modulo `p`.
    The modulus `p` may be any positive integer, not necessarily prime.

    Objects of the class \\class{ZZ_p} are represented as a \\code{ZZ} in the
    range `0, \\ldots, p-1`.

    Each \\class{ZZ_p} contains a pointer of a \\class{ZZ_pContext} which
    contains pre-computed data for NTL.  These can be explicitly constructed
    and passed to the constructor of a \\class{ZZ_p} or the \\class{ZZ_pContext}
    method \\code{ZZ_p} can be used to construct a \\class{ZZ_p} element.

    This class takes care of making sure that the C++ library NTL global
    variable is set correctly before performing any arithmetic."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, v=..., modulus=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_p.pyx (starting at line 93)

                Initialize an NTL integer mod p.

                EXAMPLES::

                    sage: c = ntl.ZZ_pContext(11)
                    sage: ntl.ZZ_p(12r, c)
                    1
                    sage: ntl.ZZ_p(Integer(95413094), c)
                    7
                    sage: ntl.ZZ_p('-1', c)
                    10

                AUTHOR: Joel B. Mohler (2007-06-14)
        """
    @overload
    def lift(self) -> Any:
        """ntl_ZZ_p.lift(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_p.pyx (starting at line 405)

        Return a lift of ``self`` as an ntl.ZZ object.

        EXAMPLES::

            sage: x = ntl.ZZ_p(8,18)
            sage: x.lift()
            8
            sage: type(x.lift())
            <class 'sage.libs.ntl.ntl_ZZ.ntl_ZZ'>"""
    @overload
    def lift(self) -> Any:
        """ntl_ZZ_p.lift(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_p.pyx (starting at line 405)

        Return a lift of ``self`` as an ntl.ZZ object.

        EXAMPLES::

            sage: x = ntl.ZZ_p(8,18)
            sage: x.lift()
            8
            sage: type(x.lift())
            <class 'sage.libs.ntl.ntl_ZZ.ntl_ZZ'>"""
    @overload
    def lift(self) -> Any:
        """ntl_ZZ_p.lift(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_p.pyx (starting at line 405)

        Return a lift of ``self`` as an ntl.ZZ object.

        EXAMPLES::

            sage: x = ntl.ZZ_p(8,18)
            sage: x.lift()
            8
            sage: type(x.lift())
            <class 'sage.libs.ntl.ntl_ZZ.ntl_ZZ'>"""
    def lift_centered(self) -> Any:
        """ntl_ZZ_p.lift_centered(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_p.pyx (starting at line 438)

        Compute a representative of ``self`` in `(-n/2 , n/2]` as an
        ``ntl.ZZ`` object.

        OUTPUT:

        - A ``ntl.ZZ`` object `r` such that  `-n/2 < r \\leq n/2` and `Mod(r, n) == self`.

        EXAMPLES::

            sage: x = ntl.ZZ_p(8, 18)
            sage: x.lift_centered()
            8
            sage: type(x.lift_centered())
            <class 'sage.libs.ntl.ntl_ZZ.ntl_ZZ'>
            sage: x = ntl.ZZ_p(12, 18)
            sage: x.lift_centered()
            -6
            sage: type(x.lift_centered())
            <class 'sage.libs.ntl.ntl_ZZ.ntl_ZZ'>"""
    @overload
    def modulus(self) -> Any:
        """ntl_ZZ_p.modulus(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_p.pyx (starting at line 422)

        Return the modulus as an NTL ZZ.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(ntl.ZZ(20))
            sage: n = ntl.ZZ_p(2983,c)
            sage: n.modulus()
            20"""
    @overload
    def modulus(self) -> Any:
        """ntl_ZZ_p.modulus(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_p.pyx (starting at line 422)

        Return the modulus as an NTL ZZ.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(ntl.ZZ(20))
            sage: n = ntl.ZZ_p(2983,c)
            sage: n.modulus()
            20"""
    @overload
    def modulus_context(self) -> Any:
        """ntl_ZZ_p.modulus_context(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_p.pyx (starting at line 173)

        Return the modulus for ``self``.

        EXAMPLES::

            sage: x = ntl.ZZ_p(5,17)
            sage: c = x.modulus_context()
            sage: y = ntl.ZZ_p(3,c)
            sage: x+y
            8
            sage: c == y.modulus_context()
            True
            sage: c == ntl.ZZ_p(7,17).modulus_context()
            True"""
    @overload
    def modulus_context(self) -> Any:
        """ntl_ZZ_p.modulus_context(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_p.pyx (starting at line 173)

        Return the modulus for ``self``.

        EXAMPLES::

            sage: x = ntl.ZZ_p(5,17)
            sage: c = x.modulus_context()
            sage: y = ntl.ZZ_p(3,c)
            sage: x+y
            8
            sage: c == y.modulus_context()
            True
            sage: c == ntl.ZZ_p(7,17).modulus_context()
            True"""
    @overload
    def modulus_context(self) -> Any:
        """ntl_ZZ_p.modulus_context(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_p.pyx (starting at line 173)

        Return the modulus for ``self``.

        EXAMPLES::

            sage: x = ntl.ZZ_p(5,17)
            sage: c = x.modulus_context()
            sage: y = ntl.ZZ_p(3,c)
            sage: x+y
            8
            sage: c == y.modulus_context()
            True
            sage: c == ntl.ZZ_p(7,17).modulus_context()
            True"""
    @overload
    def modulus_context(self) -> Any:
        """ntl_ZZ_p.modulus_context(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_p.pyx (starting at line 173)

        Return the modulus for ``self``.

        EXAMPLES::

            sage: x = ntl.ZZ_p(5,17)
            sage: c = x.modulus_context()
            sage: y = ntl.ZZ_p(3,c)
            sage: x+y
            8
            sage: c == y.modulus_context()
            True
            sage: c == ntl.ZZ_p(7,17).modulus_context()
            True"""
    def __add__(self, ntl_ZZ_pself, other) -> Any:
        """ntl_ZZ_p.__add__(ntl_ZZ_p self, other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_p.pyx (starting at line 285)

        EXAMPLES::

            sage: x = ntl.ZZ_p(5,31) ; y = ntl.ZZ_p(8,31)
            sage: x+y ## indirect doctest
            13"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    @overload
    def __int__(self) -> Any:
        """ntl_ZZ_p.__int__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_p.pyx (starting at line 336)

        Return ``self`` as an int.

        EXAMPLES::

            sage: x = ntl.ZZ_p(3,8)
            sage: x.__int__()
            3
            sage: type(x.__int__())
            <... 'int'>"""
    @overload
    def __int__(self) -> Any:
        """ntl_ZZ_p.__int__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_p.pyx (starting at line 336)

        Return ``self`` as an int.

        EXAMPLES::

            sage: x = ntl.ZZ_p(3,8)
            sage: x.__int__()
            3
            sage: type(x.__int__())
            <... 'int'>"""
    @overload
    def __int__(self) -> Any:
        """ntl_ZZ_p.__int__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_p.pyx (starting at line 336)

        Return ``self`` as an int.

        EXAMPLES::

            sage: x = ntl.ZZ_p(3,8)
            sage: x.__int__()
            3
            sage: type(x.__int__())
            <... 'int'>"""
    def __invert__(self) -> Any:
        """ntl_ZZ_p.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_p.pyx (starting at line 232)

        EXAMPLES::

            sage: c=ntl.ZZ_pContext(11)
            sage: ~ntl.ZZ_p(2r,modulus=c)
            6"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __mul__(self, ntl_ZZ_pself, other) -> Any:
        """ntl_ZZ_p.__mul__(ntl_ZZ_p self, other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_p.pyx (starting at line 247)

        EXAMPLES::

            sage: x = ntl.ZZ_p(5,31) ; y = ntl.ZZ_p(8,31)
            sage: x*y ## indirect doctest
            9"""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __neg__(self) -> Any:
        """ntl_ZZ_p.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_p.pyx (starting at line 306)

        EXAMPLES::

            sage: x = ntl.ZZ_p(5,31)
            sage: -x ## indirect doctest
            26"""
    def __pow__(self, ntl_ZZ_pself, longe, ignored) -> Any:
        """ntl_ZZ_p.__pow__(ntl_ZZ_p self, long e, ignored)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_p.pyx (starting at line 321)

        EXAMPLES::

            sage: x = ntl.ZZ_p(5,31)
            sage: x**3 ## indirect doctest
            1"""
    def __radd__(self, other):
        """Return value+self."""
    def __reduce__(self) -> Any:
        """ntl_ZZ_p.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_p.pyx (starting at line 163)

        EXAMPLES::

            sage: a = ntl.ZZ_p(4,7)
            sage: loads(dumps(a)) == a
            True"""
    def __rmul__(self, other):
        """Return value*self."""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
    def __rsub__(self, other):
        """Return value-self."""
    def __sub__(self, ntl_ZZ_pself, other) -> Any:
        """ntl_ZZ_p.__sub__(ntl_ZZ_p self, other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_p.pyx (starting at line 266)

        EXAMPLES::

            sage: x = ntl.ZZ_p(5,31) ; y = ntl.ZZ_p(8,31)
            sage: x-y ## indirect doctest
            28
            sage: y-x
            3"""
