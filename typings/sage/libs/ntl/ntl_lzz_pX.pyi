import _cython_3_2_1
from sage.categories.category import ZZ_sage as ZZ_sage
from sage.libs.ntl.ntl_lzz_pContext import ntl_zz_pContext as ntl_zz_pContext
from sage.rings.integer_ring import IntegerRing as IntegerRing
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

make_zz_pX: _cython_3_2_1.cython_function_or_method

class ntl_zz_pX:
    """ntl_zz_pX(ls=[], modulus=None)

    File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 53)

    The class \\class{zz_pX} implements polynomial arithmetic modulo `p`,
    for p smaller than a machine word.

    Polynomial arithmetic is implemented using the FFT, combined with
    the Chinese Remainder Theorem.  A more detailed description of the
    techniques used here can be found in [Shoup, J. Symbolic
    Comp. 20:363-397, 1995].

    Small degree polynomials are multiplied either with classical
    or Karatsuba algorithms."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, ls=..., modulus=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 67)

                EXAMPLES::

                    sage: f = ntl.zz_pX([1,2,5,-9],20)
                    sage: f
                    [1, 2, 5, 11]
                    sage: g = ntl.zz_pX([0,0,0],20); g
                    []
                    sage: g[10]=5
                    sage: g
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5]
                    sage: g[10]
                    5
                    sage: f = ntl.zz_pX([10^30+1, 10^50+1], 100); f
                    [1, 1]
        """
    @overload
    def clear(self) -> Any:
        """ntl_zz_pX.clear(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 850)

        Reset this polynomial to 0.  Changes this polynomial in place.

        EXAMPLES::

            sage: f = ntl.zz_pX([1,2,3],17)
            sage: f
            [1, 2, 3]
            sage: f.clear()
            sage: f
            []"""
    @overload
    def clear(self) -> Any:
        """ntl_zz_pX.clear(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 850)

        Reset this polynomial to 0.  Changes this polynomial in place.

        EXAMPLES::

            sage: f = ntl.zz_pX([1,2,3],17)
            sage: f
            [1, 2, 3]
            sage: f.clear()
            sage: f
            []"""
    @overload
    def constant_term(self) -> Any:
        """ntl_zz_pX.constant_term(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 612)

        Return the constant coefficient of this polynomial.

        EXAMPLES::

            sage: f = ntl.zz_pX([3,6,9],127)
            sage: f.constant_term()
            3
            sage: f = ntl.zz_pX([], 12223)
            sage: f.constant_term()
            0"""
    @overload
    def constant_term(self) -> Any:
        """ntl_zz_pX.constant_term(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 612)

        Return the constant coefficient of this polynomial.

        EXAMPLES::

            sage: f = ntl.zz_pX([3,6,9],127)
            sage: f.constant_term()
            3
            sage: f = ntl.zz_pX([], 12223)
            sage: f.constant_term()
            0"""
    @overload
    def constant_term(self) -> Any:
        """ntl_zz_pX.constant_term(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 612)

        Return the constant coefficient of this polynomial.

        EXAMPLES::

            sage: f = ntl.zz_pX([3,6,9],127)
            sage: f.constant_term()
            3
            sage: f = ntl.zz_pX([], 12223)
            sage: f.constant_term()
            0"""
    @overload
    def degree(self) -> Any:
        """ntl_zz_pX.degree(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 573)

        Return the degree of this polynomial.  The degree of the 0
        polynomial is -1.

        EXAMPLES::

            sage: f = ntl.zz_pX([5,0,1],50)
            sage: f.degree()
            2
            sage: f = ntl.zz_pX(range(100),50)
            sage: f.degree()
            99
            sage: f = ntl.zz_pX([],10)
            sage: f.degree()
            -1
            sage: f = ntl.zz_pX([1],77)
            sage: f.degree()
            0"""
    @overload
    def degree(self) -> Any:
        """ntl_zz_pX.degree(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 573)

        Return the degree of this polynomial.  The degree of the 0
        polynomial is -1.

        EXAMPLES::

            sage: f = ntl.zz_pX([5,0,1],50)
            sage: f.degree()
            2
            sage: f = ntl.zz_pX(range(100),50)
            sage: f.degree()
            99
            sage: f = ntl.zz_pX([],10)
            sage: f.degree()
            -1
            sage: f = ntl.zz_pX([1],77)
            sage: f.degree()
            0"""
    @overload
    def degree(self) -> Any:
        """ntl_zz_pX.degree(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 573)

        Return the degree of this polynomial.  The degree of the 0
        polynomial is -1.

        EXAMPLES::

            sage: f = ntl.zz_pX([5,0,1],50)
            sage: f.degree()
            2
            sage: f = ntl.zz_pX(range(100),50)
            sage: f.degree()
            99
            sage: f = ntl.zz_pX([],10)
            sage: f.degree()
            -1
            sage: f = ntl.zz_pX([1],77)
            sage: f.degree()
            0"""
    @overload
    def degree(self) -> Any:
        """ntl_zz_pX.degree(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 573)

        Return the degree of this polynomial.  The degree of the 0
        polynomial is -1.

        EXAMPLES::

            sage: f = ntl.zz_pX([5,0,1],50)
            sage: f.degree()
            2
            sage: f = ntl.zz_pX(range(100),50)
            sage: f.degree()
            99
            sage: f = ntl.zz_pX([],10)
            sage: f.degree()
            -1
            sage: f = ntl.zz_pX([1],77)
            sage: f.degree()
            0"""
    @overload
    def degree(self) -> Any:
        """ntl_zz_pX.degree(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 573)

        Return the degree of this polynomial.  The degree of the 0
        polynomial is -1.

        EXAMPLES::

            sage: f = ntl.zz_pX([5,0,1],50)
            sage: f.degree()
            2
            sage: f = ntl.zz_pX(range(100),50)
            sage: f.degree()
            99
            sage: f = ntl.zz_pX([],10)
            sage: f.degree()
            -1
            sage: f = ntl.zz_pX([1],77)
            sage: f.degree()
            0"""
    @overload
    def diff(self) -> Any:
        """ntl_zz_pX.diff(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 480)

        The formal derivative of ``self``.

        EXAMPLES::

            sage: f = ntl.zz_pX(range(10), 17)
            sage: f.diff()
            [1, 4, 9, 16, 8, 2, 15, 13, 13]"""
    @overload
    def diff(self) -> Any:
        """ntl_zz_pX.diff(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 480)

        The formal derivative of ``self``.

        EXAMPLES::

            sage: f = ntl.zz_pX(range(10), 17)
            sage: f.diff()
            [1, 4, 9, 16, 8, 2, 15, 13, 13]"""
    def invert_and_truncate(self, longm) -> Any:
        """ntl_zz_pX.invert_and_truncate(self, long m)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 721)

        Compute and return the inverse of ``self`` modulo `x^m`.
        The constant term of ``self`` must be 1 or -1.

        EXAMPLES::

            sage: f = ntl.zz_pX([1,2,3,4,5,6,7],20)
            sage: f.invert_and_truncate(20)
            [1, 18, 1, 0, 0, 0, 0, 8, 17, 2, 13, 0, 0, 0, 4, 0, 17, 10, 9]
            sage: g = f.invert_and_truncate(20)
            sage: g * f
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 4, 4, 3]"""
    @overload
    def is_monic(self) -> Any:
        """ntl_zz_pX.is_monic(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 786)

        Return ``True`` exactly if this polynomial is monic.

        EXAMPLES::

            sage: f = ntl.zz_pX([2,0,0,1],17)
            sage: f.is_monic()
            True
            sage: g = f.reverse()
            sage: g.is_monic()
            False
            sage: g
            [1, 0, 0, 2]
            sage: f = ntl.zz_pX([1,2,0,3,0,2],717)
            sage: f.is_monic()
            False"""
    @overload
    def is_monic(self) -> Any:
        """ntl_zz_pX.is_monic(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 786)

        Return ``True`` exactly if this polynomial is monic.

        EXAMPLES::

            sage: f = ntl.zz_pX([2,0,0,1],17)
            sage: f.is_monic()
            True
            sage: g = f.reverse()
            sage: g.is_monic()
            False
            sage: g
            [1, 0, 0, 2]
            sage: f = ntl.zz_pX([1,2,0,3,0,2],717)
            sage: f.is_monic()
            False"""
    @overload
    def is_monic(self) -> Any:
        """ntl_zz_pX.is_monic(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 786)

        Return ``True`` exactly if this polynomial is monic.

        EXAMPLES::

            sage: f = ntl.zz_pX([2,0,0,1],17)
            sage: f.is_monic()
            True
            sage: g = f.reverse()
            sage: g.is_monic()
            False
            sage: g
            [1, 0, 0, 2]
            sage: f = ntl.zz_pX([1,2,0,3,0,2],717)
            sage: f.is_monic()
            False"""
    @overload
    def is_monic(self) -> Any:
        """ntl_zz_pX.is_monic(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 786)

        Return ``True`` exactly if this polynomial is monic.

        EXAMPLES::

            sage: f = ntl.zz_pX([2,0,0,1],17)
            sage: f.is_monic()
            True
            sage: g = f.reverse()
            sage: g.is_monic()
            False
            sage: g
            [1, 0, 0, 2]
            sage: f = ntl.zz_pX([1,2,0,3,0,2],717)
            sage: f.is_monic()
            False"""
    @overload
    def is_one(self) -> Any:
        """ntl_zz_pX.is_one(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 770)

        Return ``True`` exactly if this polynomial is 1.

        EXAMPLES::

            sage: f = ntl.zz_pX([1,1],101)
            sage: f.is_one()
            False
            sage: f = ntl.zz_pX([1],2)
            sage: f.is_one()
            True"""
    @overload
    def is_one(self) -> Any:
        """ntl_zz_pX.is_one(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 770)

        Return ``True`` exactly if this polynomial is 1.

        EXAMPLES::

            sage: f = ntl.zz_pX([1,1],101)
            sage: f.is_one()
            False
            sage: f = ntl.zz_pX([1],2)
            sage: f.is_one()
            True"""
    @overload
    def is_one(self) -> Any:
        """ntl_zz_pX.is_one(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 770)

        Return ``True`` exactly if this polynomial is 1.

        EXAMPLES::

            sage: f = ntl.zz_pX([1,1],101)
            sage: f.is_one()
            False
            sage: f = ntl.zz_pX([1],2)
            sage: f.is_one()
            True"""
    @overload
    def is_x(self) -> Any:
        '''ntl_zz_pX.is_x(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 830)

        ``True`` if this is the polynomial "x".

        EXAMPLES::

            sage: f = ntl.zz_pX([],100)
            sage: f.set_x()
            sage: f.is_x()
            True
            sage: f = ntl.zz_pX([0,1],383)
            sage: f.is_x()
            True
            sage: f = ntl.zz_pX([1],38)
            sage: f.is_x()
            False'''
    @overload
    def is_x(self) -> Any:
        '''ntl_zz_pX.is_x(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 830)

        ``True`` if this is the polynomial "x".

        EXAMPLES::

            sage: f = ntl.zz_pX([],100)
            sage: f.set_x()
            sage: f.is_x()
            True
            sage: f = ntl.zz_pX([0,1],383)
            sage: f.is_x()
            True
            sage: f = ntl.zz_pX([1],38)
            sage: f.is_x()
            False'''
    @overload
    def is_x(self) -> Any:
        '''ntl_zz_pX.is_x(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 830)

        ``True`` if this is the polynomial "x".

        EXAMPLES::

            sage: f = ntl.zz_pX([],100)
            sage: f.set_x()
            sage: f.is_x()
            True
            sage: f = ntl.zz_pX([0,1],383)
            sage: f.is_x()
            True
            sage: f = ntl.zz_pX([1],38)
            sage: f.is_x()
            False'''
    @overload
    def is_x(self) -> Any:
        '''ntl_zz_pX.is_x(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 830)

        ``True`` if this is the polynomial "x".

        EXAMPLES::

            sage: f = ntl.zz_pX([],100)
            sage: f.set_x()
            sage: f.is_x()
            True
            sage: f = ntl.zz_pX([0,1],383)
            sage: f.is_x()
            True
            sage: f = ntl.zz_pX([1],38)
            sage: f.is_x()
            False'''
    @overload
    def is_zero(self) -> Any:
        """ntl_zz_pX.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 752)

        Return ``True`` exactly if this polynomial is 0.

        EXAMPLES::

            sage: f = ntl.zz_pX([0,0,0,20],5)
            sage: f.is_zero()
            True
            sage: f = ntl.zz_pX([0,0,1],30)
            sage: f
            [0, 0, 1]
            sage: f.is_zero()
            False"""
    @overload
    def is_zero(self) -> Any:
        """ntl_zz_pX.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 752)

        Return ``True`` exactly if this polynomial is 0.

        EXAMPLES::

            sage: f = ntl.zz_pX([0,0,0,20],5)
            sage: f.is_zero()
            True
            sage: f = ntl.zz_pX([0,0,1],30)
            sage: f
            [0, 0, 1]
            sage: f.is_zero()
            False"""
    @overload
    def is_zero(self) -> Any:
        """ntl_zz_pX.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 752)

        Return ``True`` exactly if this polynomial is 0.

        EXAMPLES::

            sage: f = ntl.zz_pX([0,0,0,20],5)
            sage: f.is_zero()
            True
            sage: f = ntl.zz_pX([0,0,1],30)
            sage: f
            [0, 0, 1]
            sage: f.is_zero()
            False"""
    @overload
    def leading_coefficient(self) -> Any:
        """ntl_zz_pX.leading_coefficient(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 596)

        Return the leading coefficient of this polynomial.

        EXAMPLES::

            sage: f = ntl.zz_pX([3,6,9],19)
            sage: f.leading_coefficient()
            9
            sage: f = ntl.zz_pX([],21)
            sage: f.leading_coefficient()
            0"""
    @overload
    def leading_coefficient(self) -> Any:
        """ntl_zz_pX.leading_coefficient(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 596)

        Return the leading coefficient of this polynomial.

        EXAMPLES::

            sage: f = ntl.zz_pX([3,6,9],19)
            sage: f.leading_coefficient()
            9
            sage: f = ntl.zz_pX([],21)
            sage: f.leading_coefficient()
            0"""
    @overload
    def leading_coefficient(self) -> Any:
        """ntl_zz_pX.leading_coefficient(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 596)

        Return the leading coefficient of this polynomial.

        EXAMPLES::

            sage: f = ntl.zz_pX([3,6,9],19)
            sage: f.leading_coefficient()
            9
            sage: f = ntl.zz_pX([],21)
            sage: f.leading_coefficient()
            0"""
    @overload
    def list(self) -> Any:
        """ntl_zz_pX.list(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 557)

        Return list of entries as a list of python ints.

        EXAMPLES::

            sage: f = ntl.zz_pX([23, 5,0,1], 10)
            sage: f.list()
            [3, 5, 0, 1]
            sage: type(f.list()[0])
            <... 'int'>"""
    @overload
    def list(self) -> Any:
        """ntl_zz_pX.list(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 557)

        Return list of entries as a list of python ints.

        EXAMPLES::

            sage: f = ntl.zz_pX([23, 5,0,1], 10)
            sage: f.list()
            [3, 5, 0, 1]
            sage: type(f.list()[0])
            <... 'int'>"""
    @overload
    def list(self) -> Any:
        """ntl_zz_pX.list(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 557)

        Return list of entries as a list of python ints.

        EXAMPLES::

            sage: f = ntl.zz_pX([23, 5,0,1], 10)
            sage: f.list()
            [3, 5, 0, 1]
            sage: type(f.list()[0])
            <... 'int'>"""
    def multiply_and_truncate(self, ntl_zz_pXother, longm) -> Any:
        """ntl_zz_pX.multiply_and_truncate(self, ntl_zz_pX other, long m)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 676)

        Return self*other but with terms of degree >= m removed.

        EXAMPLES::

            sage: f = ntl.zz_pX([1,2,3,4,5],20)
            sage: g = ntl.zz_pX([10],20)
            sage: f.multiply_and_truncate(g, 2)
            [10]
            sage: g.multiply_and_truncate(f, 2)
            [10]"""
    def preallocate_space(self, longn) -> Any:
        """ntl_zz_pX.preallocate_space(self, long n)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 866)

        Pre-allocate spaces for n coefficients.  The polynomial that f
        represents is unchanged.  This is useful if you know you'll be
        setting coefficients up to n, so memory isn't re-allocated as
        the polynomial grows.  (You might save a millisecond with this
        function.)

        EXAMPLES::

            sage: f = ntl.zz_pX([1,2,3],17)
            sage: f.preallocate_space(20)
            sage: f
            [1, 2, 3]
            sage: f[10]=5  # no new memory is allocated
            sage: f
            [1, 2, 3, 0, 0, 0, 0, 0, 0, 0, 5]"""
    @overload
    def quo_rem(self, ntl_zz_pXright) -> Any:
        """ntl_zz_pX.quo_rem(self, ntl_zz_pX right)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 406)

        Return the quotient and remainder when ``self`` is divided by ``right``.

        Specifically, this returns `r`, `q` such that ``self = q * right + r``.

        EXAMPLES::

            sage: f = ntl.zz_pX(range(7), 19)
            sage: g = ntl.zz_pX([2,4,6], 19)
            sage: f // g
            [1, 1, 15, 16, 1]
            sage: f % g
            [17, 14]
            sage: f.quo_rem(g)
            ([1, 1, 15, 16, 1], [17, 14])
            sage: (f // g) * g + f % g
            [0, 1, 2, 3, 4, 5, 6]"""
    @overload
    def quo_rem(self, g) -> Any:
        """ntl_zz_pX.quo_rem(self, ntl_zz_pX right)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 406)

        Return the quotient and remainder when ``self`` is divided by ``right``.

        Specifically, this returns `r`, `q` such that ``self = q * right + r``.

        EXAMPLES::

            sage: f = ntl.zz_pX(range(7), 19)
            sage: g = ntl.zz_pX([2,4,6], 19)
            sage: f // g
            [1, 1, 15, 16, 1]
            sage: f % g
            [17, 14]
            sage: f.quo_rem(g)
            ([1, 1, 15, 16, 1], [17, 14])
            sage: (f // g) * g + f % g
            [0, 1, 2, 3, 4, 5, 6]"""
    @overload
    def reverse(self) -> Any:
        """ntl_zz_pX.reverse(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 495)

        Return ``self`` with coefficients reversed, i.e. ``x^n self(x^{-n})``.

        EXAMPLES::

            sage: f = ntl.zz_pX([2,4,6], 17)
            sage: f.reverse()
            [6, 4, 2]"""
    @overload
    def reverse(self) -> Any:
        """ntl_zz_pX.reverse(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 495)

        Return ``self`` with coefficients reversed, i.e. ``x^n self(x^{-n})``.

        EXAMPLES::

            sage: f = ntl.zz_pX([2,4,6], 17)
            sage: f.reverse()
            [6, 4, 2]"""
    @overload
    def set_x(self) -> Any:
        '''ntl_zz_pX.set_x(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 809)

        Set this polynomial to the monomial "x".

        EXAMPLES::

            sage: f = ntl.zz_pX([],177)
            sage: f.set_x()
            sage: f
            [0, 1]
            sage: g = ntl.zz_pX([0,1],177)
            sage: f == g
            True

        Though f and g are equal, they are not the same objects in memory:
            sage: f is g
            False'''
    @overload
    def set_x(self) -> Any:
        '''ntl_zz_pX.set_x(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 809)

        Set this polynomial to the monomial "x".

        EXAMPLES::

            sage: f = ntl.zz_pX([],177)
            sage: f.set_x()
            sage: f
            [0, 1]
            sage: g = ntl.zz_pX([0,1],177)
            sage: f == g
            True

        Though f and g are equal, they are not the same objects in memory:
            sage: f is g
            False'''
    def square(self) -> Any:
        """ntl_zz_pX.square(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 628)

        Return f*f.

        EXAMPLES::

            sage: f = ntl.zz_pX([-1,0,1],17)
            sage: f*f
            [1, 0, 15, 0, 1]"""
    def square_and_truncate(self, longm) -> Any:
        """ntl_zz_pX.square_and_truncate(self, long m)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 699)

        Return self*self but with terms of degree >= m removed.

        EXAMPLES::

            sage: f = ntl.zz_pX([1,2,3,4,5],20)
            sage: f.square_and_truncate(4)
            [1, 4, 10]
            sage: (f*f).truncate(4)
            [1, 4, 10]"""
    def truncate(self, longm) -> Any:
        """ntl_zz_pX.truncate(self, long m)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 645)

        Return the truncation of this polynomial obtained by
        removing all terms of degree >= m.

        EXAMPLES::

            sage: f = ntl.zz_pX([1,2,3,4,5],70)
            sage: f.truncate(3)
            [1, 2, 3]
            sage: f.truncate(8)
            [1, 2, 3, 4, 5]
            sage: f.truncate(1)
            [1]
            sage: f.truncate(0)
            []
            sage: f.truncate(-1)
            []
            sage: f.truncate(-5)
            []"""
    def __add__(self, ntl_zz_pXself, other) -> Any:
        """ntl_zz_pX.__add__(ntl_zz_pX self, other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 250)

        Return ``self + other``.

        EXAMPLES::

            sage: ntl.zz_pX(range(5),20) + ntl.zz_pX(range(6),20) ## indirect doctest
            [0, 2, 4, 6, 8, 5]
            sage: ntl.zz_pX(range(5),20) + ntl.zz_pX(range(6),50)
            Traceback (most recent call last):
            ...
            ValueError: arithmetic operands must have the same modulus."""
    def __delitem__(self, other) -> None:
        """Delete self[key]."""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __floordiv__(self, ntl_zz_pXself, ntl_zz_pXright) -> Any:
        """ntl_zz_pX.__floordiv__(ntl_zz_pX self, ntl_zz_pX right)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 433)

        Return the whole part of ``self / right``.

        EXAMPLES::

            sage: f = ntl.zz_pX(range(10), 19); g = ntl.zz_pX([1]*5, 19)
            sage: f // g ## indirect doctest
            [8, 18, 18, 18, 18, 9]"""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __getitem__(self, longi) -> Any:
        """ntl_zz_pX.__getitem__(self, long i)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 190)

        Return the i-th coefficient of f.

        EXAMPLES::

            sage: f = ntl.zz_pX(range(7), 71)
            sage: f[3] ## indirect doctest
            3

            sage: f[-5]
            0

            sage: f[27]
            0"""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lshift__(self, ntl_zz_pXself, longn) -> Any:
        """ntl_zz_pX.__lshift__(ntl_zz_pX self, long n)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 450)

        Shift this polynomial to the left, which is multiplication by `x^n`.

        EXAMPLES::

            sage: f = ntl.zz_pX([2,4,6], 17)
            sage: f << 2 ## indirect doctest
            [0, 0, 2, 4, 6]"""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __mod__(self, ntl_zz_pXself, other) -> Any:
        """ntl_zz_pX.__mod__(ntl_zz_pX self, other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 358)

        Given polynomials a, b in ZZ[X], there exist polynomials q, r
        in QQ[X] such that a = b*q + r, deg(r) < deg(b).  This
        function returns q if q lies in ZZ[X], and otherwise raises an
        Exception.

        EXAMPLES::

            sage: f = ntl.zz_pX([2,4,6],17); g = ntl.zz_pX([2],17)
            sage: f % g   ## indirect doctest
            []

            sage: f = ntl.zz_pX(range(10),17); g = ntl.zz_pX([-1,0,1],17)
            sage: f % g
            [3, 8]"""
    def __mul__(self, ntl_zz_pXself, other) -> Any:
        """ntl_zz_pX.__mul__(ntl_zz_pX self, other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 296)

        EXAMPLES::

            sage: ntl.zz_pX(range(5),20) * ntl.zz_pX(range(6),20) ## indirect doctest
            [0, 0, 1, 4, 10, 0, 10, 14, 11]
            sage: ntl.zz_pX(range(5),20) * ntl.zz_pX(range(6),50)
            Traceback (most recent call last):
            ...
            ValueError: arithmetic operands must have the same modulus."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __neg__(self) -> Any:
        """ntl_zz_pX.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 510)

        Return the negative of ``self``.

        EXAMPLES::

            sage: f = ntl.zz_pX([2,0,0,1],20)
            sage: -f
            [18, 0, 0, 19]"""
    def __pow__(self, ntl_zz_pXself, longn, ignored) -> Any:
        """ntl_zz_pX.__pow__(ntl_zz_pX self, long n, ignored)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 387)

        Return the `n`-th nonnegative power of ``self``.

        EXAMPLES::

            sage: g = ntl.zz_pX([-1,0,1],20)
            sage: g**10 ## indirect doctest
            [1, 0, 10, 0, 5, 0, 0, 0, 10, 0, 8, 0, 10, 0, 0, 0, 5, 0, 10, 0, 1]"""
    def __radd__(self, other):
        """Return value+self."""
    def __reduce__(self) -> Any:
        """ntl_zz_pX.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 168)

        TESTS::

            sage: f = ntl.zz_pX([10,10^30+1], 20)
            sage: f == loads(dumps(f))
            True"""
    def __rfloordiv__(self, other):
        """Return value//self."""
    def __rlshift__(self, other):
        """Return value<<self."""
    def __rmod__(self, other):
        """Return value%self."""
    def __rmul__(self, other):
        """Return value*self."""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
    def __rrshift__(self, other):
        """Return value>>self."""
    def __rshift__(self, ntl_zz_pXself, longn) -> Any:
        """ntl_zz_pX.__rshift__(ntl_zz_pX self, long n)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 465)

        Shift this polynomial to the right, which is division by `x^n` (and truncation).

        EXAMPLES::

            sage: f = ntl.zz_pX([1,2,3], 17)
            sage: f >> 2 ## indirect doctest
            [3]"""
    def __rsub__(self, other):
        """Return value-self."""
    def __rtruediv__(self, other):
        """Return value/self."""
    def __setitem__(self, longi, val) -> Any:
        """ntl_zz_pX.__setitem__(self, long i, val)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 213)

        Set the i-th coefficient of ``self`` to val. If
        i is out of range, raise an exception.

        EXAMPLES::

            sage: f = ntl.zz_pX([], 7)
            sage: f[3] = 2 ; f
            [0, 0, 0, 2]
            sage: f[-1] = 5
            Traceback (most recent call last):
            ...
            ValueError: index (=-1) is out of range"""
    def __sub__(self, ntl_zz_pXself, other) -> Any:
        """ntl_zz_pX.__sub__(ntl_zz_pX self, other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 273)

        Return ``self - other``.

        EXAMPLES::

            sage: ntl.zz_pX(range(5),32) - ntl.zz_pX(range(6),32)
            [0, 0, 0, 0, 0, 27]
            sage: ntl.zz_pX(range(5),20) - ntl.zz_pX(range(6),50) ## indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: arithmetic operands must have the same modulus."""
    def __truediv__(self, ntl_zz_pXself, other) -> Any:
        """ntl_zz_pX.__truediv__(ntl_zz_pX self, other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pX.pyx (starting at line 319)

        Compute quotient ``self / other``, if the quotient is a polynomial.
        Otherwise an Exception is raised.

        EXAMPLES::

            sage: f = ntl.zz_pX([1,2,3],17) * ntl.zz_pX([4,5],17)**2
            sage: g = ntl.zz_pX([4,5],17)
            sage: f/g ## indirect doctest
            [4, 13, 5, 15]
            sage: ntl.zz_pX([1,2,3],17) * ntl.zz_pX([4,5],17)
            [4, 13, 5, 15]

            sage: f = ntl.zz_pX(range(10),17); g = ntl.zz_pX([-1,0,1],17)
            sage: f/g
            Traceback (most recent call last):
            ...
            ArithmeticError: self (=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) is not divisible by other (=[16, 0, 1])
            sage: ntl.zz_pX(range(5),20) / ntl.zz_pX(range(6),50)
            Traceback (most recent call last):
            ...
            ValueError: arithmetic operands must have the same modulus."""
