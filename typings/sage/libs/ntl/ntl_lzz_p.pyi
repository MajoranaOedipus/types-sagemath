import _cython_3_2_1
from sage.categories.category import ZZ_sage as ZZ_sage
from sage.libs.ntl.ntl_lzz_pContext import ntl_zz_pContext as ntl_zz_pContext
from sage.rings.integer_ring import IntegerRing as IntegerRing
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

make_zz_p: _cython_3_2_1.cython_function_or_method

class ntl_zz_p:
    """ntl_zz_p(a=0, modulus=None)

    File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_p.pyx (starting at line 60)

    The class \\class{zz_p} implements arithmetic modulo `p`,
    for p smaller than a machine word.

    NOTE: This type is provided mostly for completeness, and
    shouldn't be used in any production code."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, a=..., modulus=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_p.pyx (starting at line 69)

                EXAMPLES::

                    sage: f = ntl.zz_p(5,7)
                    sage: f
                    5
                    sage: g = ntl.zz_p(int(-5),7)
                    sage: g
                    2
        """
    @overload
    def clear(self) -> Any:
        """ntl_zz_p.clear(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_p.pyx (starting at line 413)

        Reset this element to 0.

        EXAMPLES::

            sage: x = ntl.zz_p(5,102) ; x
            5
            sage: x.clear() ; x
            0"""
    @overload
    def clear(self) -> Any:
        """ntl_zz_p.clear(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_p.pyx (starting at line 413)

        Reset this element to 0.

        EXAMPLES::

            sage: x = ntl.zz_p(5,102) ; x
            5
            sage: x.clear() ; x
            0"""
    @overload
    def is_one(self) -> Any:
        """ntl_zz_p.is_one(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_p.pyx (starting at line 397)

        Return ``True`` exactly if this element is 1.

        EXAMPLES::

            sage: f = ntl.zz_p(1,11)
            sage: f.is_one()
            True
            sage: f = ntl.zz_p(5,11)
            sage: f.is_one()
            False"""
    @overload
    def is_one(self) -> Any:
        """ntl_zz_p.is_one(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_p.pyx (starting at line 397)

        Return ``True`` exactly if this element is 1.

        EXAMPLES::

            sage: f = ntl.zz_p(1,11)
            sage: f.is_one()
            True
            sage: f = ntl.zz_p(5,11)
            sage: f.is_one()
            False"""
    @overload
    def is_one(self) -> Any:
        """ntl_zz_p.is_one(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_p.pyx (starting at line 397)

        Return ``True`` exactly if this element is 1.

        EXAMPLES::

            sage: f = ntl.zz_p(1,11)
            sage: f.is_one()
            True
            sage: f = ntl.zz_p(5,11)
            sage: f.is_one()
            False"""
    @overload
    def is_zero(self) -> Any:
        """ntl_zz_p.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_p.pyx (starting at line 381)

        Return ``True`` exactly if this element is 0.

        EXAMPLES::

            sage: f = ntl.zz_p(0,20)
            sage: f.is_zero()
            True
            sage: f = ntl.zz_p(1,20)
            sage: f.is_zero()
            False"""
    @overload
    def is_zero(self) -> Any:
        """ntl_zz_p.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_p.pyx (starting at line 381)

        Return ``True`` exactly if this element is 0.

        EXAMPLES::

            sage: f = ntl.zz_p(0,20)
            sage: f.is_zero()
            True
            sage: f = ntl.zz_p(1,20)
            sage: f.is_zero()
            False"""
    @overload
    def is_zero(self) -> Any:
        """ntl_zz_p.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_p.pyx (starting at line 381)

        Return ``True`` exactly if this element is 0.

        EXAMPLES::

            sage: f = ntl.zz_p(0,20)
            sage: f.is_zero()
            True
            sage: f = ntl.zz_p(1,20)
            sage: f.is_zero()
            False"""
    def square(self) -> Any:
        """ntl_zz_p.square(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_p.pyx (starting at line 365)

        Return f*f.

        EXAMPLES::

            sage: f = ntl.zz_p(15,23)
            sage: f*f
            18"""
    def __add__(self, ntl_zz_pself, other) -> Any:
        """ntl_zz_p.__add__(ntl_zz_p self, other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_p.pyx (starting at line 190)

        EXAMPLES::

            sage: ntl.zz_p(5,23) + ntl.zz_p(6,23)
            11"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    @overload
    def __int__(self) -> Any:
        """ntl_zz_p.__int__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_p.pyx (starting at line 350)

        Return ``self`` as an int.

        EXAMPLES::

            sage: ntl.zz_p(3,next_prime(100)).__int__()
            3
            sage: int(ntl.zz_p(3,next_prime(100)))
            3
            sage: type(int(ntl.zz_p(3,next_prime(100))))
            <... 'int'>"""
    @overload
    def __int__(self) -> Any:
        """ntl_zz_p.__int__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_p.pyx (starting at line 350)

        Return ``self`` as an int.

        EXAMPLES::

            sage: ntl.zz_p(3,next_prime(100)).__int__()
            3
            sage: int(ntl.zz_p(3,next_prime(100)))
            3
            sage: type(int(ntl.zz_p(3,next_prime(100))))
            <... 'int'>"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __mul__(self, ntl_zz_pself, other) -> Any:
        """ntl_zz_p.__mul__(ntl_zz_p self, other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_p.pyx (starting at line 224)

        EXAMPLES::

            sage: ntl.zz_p(5,23) * ntl.zz_p(6,23)
            7"""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __neg__(self) -> Any:
        """ntl_zz_p.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_p.pyx (starting at line 303)

        Return the negative of ``self``.

        EXAMPLES::

            sage: f = ntl.zz_p(5,234)
            sage: -f ## indirect doctest
            229"""
    def __pow__(self, ntl_zz_pself, longn, ignored) -> Any:
        """ntl_zz_p.__pow__(ntl_zz_p self, long n, ignored)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_p.pyx (starting at line 260)

        Return the `n`-th nonnegative power of ``self``.

        EXAMPLES::

            sage: g = ntl.zz_p(5, 13)
            sage: g ^ 10
            12
            sage: g ^ (-1)
            8
            sage: g ^ (-5)
            8
            sage: g ^ 0
            1
            sage: z = ntl.zz_p(0, 13)
            sage: z ^ 0
            1
            sage: z ^ 1
            0
            sage: z ^ (-1)
            Traceback (most recent call last):
            ...
            ZeroDivisionError: inverse does not exist"""
    def __radd__(self, other):
        """Return value+self."""
    def __reduce__(self) -> Any:
        """ntl_zz_p.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_p.pyx (starting at line 167)

        For pickling.

        TESTS::

            sage: f = ntl.zz_p(16,244)
            sage: loads(dumps(f)) == f
            True"""
    def __rmul__(self, other):
        """Return value*self."""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
    def __rsub__(self, other):
        """Return value-self."""
    def __rtruediv__(self, other):
        """Return value/self."""
    def __sub__(self, ntl_zz_pself, other) -> Any:
        """ntl_zz_p.__sub__(ntl_zz_p self, other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_p.pyx (starting at line 207)

        EXAMPLES::

            sage: ntl.zz_p(5,23) - ntl.zz_p(6,23)
            22"""
    def __truediv__(self, ntl_zz_pself, other) -> Any:
        """ntl_zz_p.__truediv__(ntl_zz_p self, other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_p.pyx (starting at line 241)

        EXAMPLES::

            sage: ntl.zz_p(5,23) / ntl.zz_p(2,23)
            14"""
