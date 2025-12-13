import _cython_3_2_1
from sage.libs.ntl.ntl_ZZ_pEContext import ntl_ZZ_pEContext as ntl_ZZ_pEContext
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

make_ZZ_pEX: _cython_3_2_1.cython_function_or_method

class ntl_ZZ_pEX:
    """ntl_ZZ_pEX(v=None, modulus=None)

    File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 51)

    The class \\class{ZZ_pEX} implements polynomials over finite ring extensions of `\\Z / p\\Z`.

    It can be used, for example, for arithmetic in `GF(p^n)[X]`.
    However, except where mathematically necessary (e.g., GCD computations),
    ZZ_pE need not be a field."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, v=..., modulus=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 60)

                EXAMPLES::

                    sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 7))
                    sage: a = ntl.ZZ_pE([3,2], c)
                    sage: b = ntl.ZZ_pE([1,2], c)
                    sage: f = ntl.ZZ_pEX([a, b, b])
                    sage: f
                    [[3 2] [1 2] [1 2]]
                    sage: g = ntl.ZZ_pEX([0,0,0], c); g
                    []
                    sage: g[10]=5
                    sage: g
                    [[] [] [] [] [] [] [] [] [] [] [5]]
                    sage: g[10]
                    [5]
        """
    @overload
    def clear(self) -> Any:
        """ntl_ZZ_pEX.clear(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 1196)

        Reset this polynomial to 0.  Changes this polynomial in place.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 11))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: f
            [[3 2] [1 2] [1 2]]
            sage: f.clear(); f
            []"""
    @overload
    def clear(self) -> Any:
        """ntl_ZZ_pEX.clear(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 1196)

        Reset this polynomial to 0.  Changes this polynomial in place.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 11))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: f
            [[3 2] [1 2] [1 2]]
            sage: f.clear(); f
            []"""
    @overload
    def constant_term(self) -> Any:
        """ntl_ZZ_pEX.constant_term(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 800)

        Return the constant coefficient of this polynomial.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 11))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: f.constant_term()
            [3 2]"""
    @overload
    def constant_term(self) -> Any:
        """ntl_ZZ_pEX.constant_term(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 800)

        Return the constant coefficient of this polynomial.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 11))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: f.constant_term()
            [3 2]"""
    def convert_to_modulus(self, ntl_ZZ_pContext_classc) -> Any:
        """ntl_ZZ_pEX.convert_to_modulus(self, ntl_ZZ_pContext_class c)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 611)

        Return a new ntl_ZZ_pX which is the same as self, but considered modulo a different p (but the SAME polynomial).

        In order for this to make mathematical sense, c.p should divide self.c.p
        (in which case ``self`` is reduced modulo c.p) or self.c.p should divide c.p
        (in which case ``self`` is lifted to something modulo c.p congruent to ``self`` modulo self.c.p)

        EXAMPLES::

            sage: c = ntl.ZZ_pEContext(ntl.ZZ_pX([-5, 0, 1], 5^20))
            sage: a = ntl.ZZ_pE([192870, 1928189], c)
            sage: b = ntl.ZZ_pE([18275,293872987], c)
            sage: f = ntl.ZZ_pEX([a, b])
            sage: g = f.convert_to_modulus(ntl.ZZ_pContext(ntl.ZZ(5^5)))
            sage: g
            [[2245 64] [2650 1112]]
            sage: g.get_modulus_context()
            NTL modulus [3120 0 1] (mod 3125)
            sage: g^2
            [[1130 2985] [805 830] [2095 2975]]
            sage: (f^2).convert_to_modulus(ntl.ZZ_pContext(ntl.ZZ(5^5)))
            [[1130 2985] [805 830] [2095 2975]]"""
    @overload
    def degree(self) -> Any:
        """ntl_ZZ_pEX.degree(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 763)

        Return the degree of this polynomial.  The degree of the 0
        polynomial is -1.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 11))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: f.degree()
            2
            sage: ntl.ZZ_pEX([], c).degree()
            -1"""
    @overload
    def degree(self) -> Any:
        """ntl_ZZ_pEX.degree(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 763)

        Return the degree of this polynomial.  The degree of the 0
        polynomial is -1.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 11))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: f.degree()
            2
            sage: ntl.ZZ_pEX([], c).degree()
            -1"""
    @overload
    def degree(self) -> Any:
        """ntl_ZZ_pEX.degree(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 763)

        Return the degree of this polynomial.  The degree of the 0
        polynomial is -1.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 11))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: f.degree()
            2
            sage: ntl.ZZ_pEX([], c).degree()
            -1"""
    @overload
    def derivative(self) -> Any:
        """ntl_ZZ_pEX.derivative(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 851)

        Return the derivative of this polynomial.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 11))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: f.derivative()
            [[1 2] [2 4]]"""
    @overload
    def derivative(self) -> Any:
        """ntl_ZZ_pEX.derivative(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 851)

        Return the derivative of this polynomial.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 11))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: f.derivative()
            [[1 2] [2 4]]"""
    def discriminant(self) -> Any:
        """ntl_ZZ_pEX.discriminant(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 1147)

        Return the discriminant of a=self, which is by definition
        $$
                (-1)^{m(m-1)/2} {\\mbox{\\tt resultant}}(a, a')/lc(a),
        $$
        where m = deg(a), and lc(a) is the leading coefficient of a.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 11))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: f.discriminant()
            [1 6]"""
    @overload
    def gcd(self, ntl_ZZ_pEXother, check=...) -> Any:
        """ntl_ZZ_pEX.gcd(self, ntl_ZZ_pEX other, check=True)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 702)

        Return ``gcd(self, other)`` if we are working over a field.

        NOTE: Does not work if p is not prime or if the modulus is not irreducible.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 11))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: g = f^2
            sage: h = f^3
            sage: g.gcd(h)
            [[2 1] [8 1] [9 1] [2] [1]]
            sage: f^2
            [[5 8] [9 8] [6 8] [5] [8]]
            sage: eight = ntl.ZZ_pEX([[8]], c)
            sage: f^2 / eight
            [[2 1] [8 1] [9 1] [2] [1]]"""
    @overload
    def gcd(self, other) -> Any:
        """ntl_ZZ_pEX.gcd(self, ntl_ZZ_pEX other, check=True)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 702)

        Return ``gcd(self, other)`` if we are working over a field.

        NOTE: Does not work if p is not prime or if the modulus is not irreducible.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 11))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: g = f^2
            sage: h = f^3
            sage: g.gcd(h)
            [[2 1] [8 1] [9 1] [2] [1]]
            sage: f^2
            [[5 8] [9 8] [6 8] [5] [8]]
            sage: eight = ntl.ZZ_pEX([[8]], c)
            sage: f^2 / eight
            [[2 1] [8 1] [9 1] [2] [1]]"""
    @overload
    def gcd(self, h) -> Any:
        """ntl_ZZ_pEX.gcd(self, ntl_ZZ_pEX other, check=True)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 702)

        Return ``gcd(self, other)`` if we are working over a field.

        NOTE: Does not work if p is not prime or if the modulus is not irreducible.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 11))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: g = f^2
            sage: h = f^3
            sage: g.gcd(h)
            [[2 1] [8 1] [9 1] [2] [1]]
            sage: f^2
            [[5 8] [9 8] [6 8] [5] [8]]
            sage: eight = ntl.ZZ_pEX([[8]], c)
            sage: f^2 / eight
            [[2 1] [8 1] [9 1] [2] [1]]"""
    @overload
    def get_modulus_context(self) -> Any:
        """ntl_ZZ_pEX.get_modulus_context(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 197)

        Return the structure that holds the underlying NTL modulus.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 7))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: f.get_modulus_context()
            NTL modulus [1 1 1] (mod 7)"""
    @overload
    def get_modulus_context(self) -> Any:
        """ntl_ZZ_pEX.get_modulus_context(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 197)

        Return the structure that holds the underlying NTL modulus.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 7))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: f.get_modulus_context()
            NTL modulus [1 1 1] (mod 7)"""
    def invert_and_truncate(self, longm) -> Any:
        """ntl_ZZ_pEX.invert_and_truncate(self, long m)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 996)

        Compute and return the inverse of ``self`` modulo `x^m`.
        The constant term of ``self`` must be invertible.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 11))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: g = f.invert_and_truncate(5)
            sage: g
            [[8 6] [4 4] [5 9] [1 4] [0 1]]
            sage: f * g
            [[1] [] [] [] [] [2 8] [9 10]]"""
    @overload
    def is_monic(self) -> Any:
        """ntl_ZZ_pEX.is_monic(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 566)

        Return ``True`` exactly if this polynomial is monic.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 7))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: f.is_monic()
            False
            sage: f = ntl.ZZ_pEX([a, b, 1], c)
            sage: f.is_monic()
            True"""
    @overload
    def is_monic(self) -> Any:
        """ntl_ZZ_pEX.is_monic(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 566)

        Return ``True`` exactly if this polynomial is monic.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 7))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: f.is_monic()
            False
            sage: f = ntl.ZZ_pEX([a, b, 1], c)
            sage: f.is_monic()
            True"""
    @overload
    def is_monic(self) -> Any:
        """ntl_ZZ_pEX.is_monic(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 566)

        Return ``True`` exactly if this polynomial is monic.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 7))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: f.is_monic()
            False
            sage: f = ntl.ZZ_pEX([a, b, 1], c)
            sage: f.is_monic()
            True"""
    @overload
    def is_one(self) -> Any:
        """ntl_ZZ_pEX.is_one(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 547)

        Return ``True`` exactly if this polynomial is 1.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 7))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: f.is_one()
            False
            sage: f = ntl.ZZ_pEX([1, 0, 0], c)
            sage: f.is_one()
            True"""
    @overload
    def is_one(self) -> Any:
        """ntl_ZZ_pEX.is_one(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 547)

        Return ``True`` exactly if this polynomial is 1.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 7))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: f.is_one()
            False
            sage: f = ntl.ZZ_pEX([1, 0, 0], c)
            sage: f.is_one()
            True"""
    @overload
    def is_one(self) -> Any:
        """ntl_ZZ_pEX.is_one(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 547)

        Return ``True`` exactly if this polynomial is 1.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 7))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: f.is_one()
            False
            sage: f = ntl.ZZ_pEX([1, 0, 0], c)
            sage: f.is_one()
            True"""
    @overload
    def is_x(self) -> Any:
        '''ntl_ZZ_pEX.is_x(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 834)

        ``True`` if this is the polynomial "x".

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 11))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: f.is_x()
            False
            sage: f.set_x(); f.is_x()
            True'''
    @overload
    def is_x(self) -> Any:
        '''ntl_ZZ_pEX.is_x(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 834)

        ``True`` if this is the polynomial "x".

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 11))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: f.is_x()
            False
            sage: f.set_x(); f.is_x()
            True'''
    @overload
    def is_x(self) -> Any:
        '''ntl_ZZ_pEX.is_x(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 834)

        ``True`` if this is the polynomial "x".

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 11))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: f.is_x()
            False
            sage: f.set_x(); f.is_x()
            True'''
    @overload
    def is_zero(self) -> Any:
        """ntl_ZZ_pEX.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 528)

        Return ``True`` exactly if this polynomial is 0.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 7))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: f.is_zero()
            False
            sage: f = ntl.ZZ_pEX([0,0,7], c)
            sage: f.is_zero()
            True"""
    @overload
    def is_zero(self) -> Any:
        """ntl_ZZ_pEX.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 528)

        Return ``True`` exactly if this polynomial is 0.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 7))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: f.is_zero()
            False
            sage: f = ntl.ZZ_pEX([0,0,7], c)
            sage: f.is_zero()
            True"""
    @overload
    def is_zero(self) -> Any:
        """ntl_ZZ_pEX.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 528)

        Return ``True`` exactly if this polynomial is 0.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 7))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: f.is_zero()
            False
            sage: f = ntl.ZZ_pEX([0,0,7], c)
            sage: f.is_zero()
            True"""
    @overload
    def leading_coefficient(self) -> Any:
        """ntl_ZZ_pEX.leading_coefficient(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 782)

        Return the leading coefficient of this polynomial.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 11))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: f.leading_coefficient()
            [1 2]"""
    @overload
    def leading_coefficient(self) -> Any:
        """ntl_ZZ_pEX.leading_coefficient(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 782)

        Return the leading coefficient of this polynomial.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 11))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: f.leading_coefficient()
            [1 2]"""
    def left_shift(self, longn) -> Any:
        """ntl_ZZ_pEX.left_shift(self, long n)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 644)

        Return the polynomial obtained by shifting all coefficients of
        this polynomial to the left n positions.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 7))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b]); f
            [[3 2] [1 2] [1 2]]
            sage: f.left_shift(2)
            [[] [] [3 2] [1 2] [1 2]]
            sage: f.left_shift(5)
            [[] [] [] [] [] [3 2] [1 2] [1 2]]

        A negative left shift is a right shift::

            sage: f.left_shift(-2)
            [[1 2]]"""
    @overload
    def list(self) -> Any:
        """ntl_ZZ_pEX.list(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 261)

        Return list of entries as a list of ntl_ZZ_pEs.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 7))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: f.list()
            [[3 2], [1 2], [1 2]]"""
    @overload
    def list(self) -> Any:
        """ntl_ZZ_pEX.list(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 261)

        Return list of entries as a list of ntl_ZZ_pEs.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 7))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: f.list()
            [[3 2], [1 2], [1 2]]"""
    @overload
    def minpoly_mod(self, ntl_ZZ_pEXmodulus) -> Any:
        """ntl_ZZ_pEX.minpoly_mod(self, ntl_ZZ_pEX modulus)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 1173)

        Return the minimal polynomial of this polynomial modulo the
        modulus.  The modulus must be monic of degree bigger than
        ``self``.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 11))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: m = ntl.ZZ_pEX([a - b, b^2, a, a*b])
            sage: f.minpoly_mod(m)
            [[2 9] [8 2] [3 10] [1]]"""
    @overload
    def minpoly_mod(self, m) -> Any:
        """ntl_ZZ_pEX.minpoly_mod(self, ntl_ZZ_pEX modulus)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 1173)

        Return the minimal polynomial of this polynomial modulo the
        modulus.  The modulus must be monic of degree bigger than
        ``self``.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 11))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: m = ntl.ZZ_pEX([a - b, b^2, a, a*b])
            sage: f.minpoly_mod(m)
            [[2 9] [8 2] [3 10] [1]]"""
    def multiply_and_truncate(self, ntl_ZZ_pEXother, longm) -> Any:
        """ntl_ZZ_pEX.multiply_and_truncate(self, ntl_ZZ_pEX other, long m)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 951)

        Return self*other but with terms of degree >= m removed.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 11))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: g = ntl.ZZ_pEX([a - b, b^2, a, a*b])
            sage: f*g
            [[6 4] [4 9] [4 6] [7] [1 9] [2 5]]
            sage: f.multiply_and_truncate(g, 3)
            [[6 4] [4 9] [4 6]]"""
    @overload
    def multiply_mod(self, ntl_ZZ_pEXother, ntl_ZZ_pEXmodulus) -> Any:
        """ntl_ZZ_pEX.multiply_mod(self, ntl_ZZ_pEX other, ntl_ZZ_pEX modulus)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 1023)

        Return ``self*other % modulus``.  The modulus must be monic with
        ``deg(modulus) > 0``, and ``self`` and ``other`` must have smaller degree.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 11))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: g = ntl.ZZ_pEX([b^4, a*b^2, a - b])
            sage: m = ntl.ZZ_pEX([a - b, b^2, a, a*b])
            sage: f.multiply_mod(g, m)
            [[10 10] [4 4] [10 3]]"""
    @overload
    def multiply_mod(self, g, m) -> Any:
        """ntl_ZZ_pEX.multiply_mod(self, ntl_ZZ_pEX other, ntl_ZZ_pEX modulus)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 1023)

        Return ``self*other % modulus``.  The modulus must be monic with
        ``deg(modulus) > 0``, and ``self`` and ``other`` must have smaller degree.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 11))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: g = ntl.ZZ_pEX([b^4, a*b^2, a - b])
            sage: m = ntl.ZZ_pEX([a - b, b^2, a, a*b])
            sage: f.multiply_mod(g, m)
            [[10 10] [4 4] [10 3]]"""
    @overload
    def norm_mod(self, ntl_ZZ_pEXmodulus) -> Any:
        """ntl_ZZ_pEX.norm_mod(self, ntl_ZZ_pEX modulus)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 1124)

        Return the norm of this polynomial modulo the modulus.  The
        modulus must be monic, and of positive degree strictly greater
        than the degree of ``self``.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 11))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: m = ntl.ZZ_pEX([a - b, b^2, a, a*b])
            sage: f.norm_mod(m)
            [9 2]"""
    @overload
    def norm_mod(self, m) -> Any:
        """ntl_ZZ_pEX.norm_mod(self, ntl_ZZ_pEX modulus)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 1124)

        Return the norm of this polynomial modulo the modulus.  The
        modulus must be monic, and of positive degree strictly greater
        than the degree of ``self``.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 11))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: m = ntl.ZZ_pEX([a - b, b^2, a, a*b])
            sage: f.norm_mod(m)
            [9 2]"""
    def preallocate_space(self, longn) -> Any:
        """ntl_ZZ_pEX.preallocate_space(self, long n)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 1216)

        Pre-allocate spaces for n coefficients.  The polynomial that f
        represents is unchanged.  This is useful if you know you'll be
        setting coefficients up to n, so memory isn't re-allocated as
        the polynomial grows.  (You might save a millisecond with this
        function.)

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 11))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: f[10]=ntl.ZZ_pE([1,8],c)  # no new memory is allocated
            sage: f
            [[3 2] [1 2] [1 2] [] [] [] [] [] [] [] [1 8]]"""
    @overload
    def quo_rem(self, ntl_ZZ_pEXother) -> Any:
        """ntl_ZZ_pEX.quo_rem(self, ntl_ZZ_pEX other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 417)

        Given polynomials a, b in ZZ_pE[X], if p is prime and the defining modulus irreducible,
        there exist polynomials q, r in ZZ_pE[X] such that a = b*q + r, deg(r) < deg(b).  This
        function returns (q, r).

        If p is not prime or the modulus is not irreducible, this function may raise a
        :exc:`RuntimeError` due to division by a noninvertible element of ZZ_p.

        EXAMPLES::

            sage: c = ntl.ZZ_pEContext(ntl.ZZ_pX([-5, 0, 1], 5^10))
            sage: a = c.ZZ_pE([5, 1])
            sage: b = c.ZZ_pE([4, 99])
            sage: f = c.ZZ_pEX([a, b])
            sage: g = c.ZZ_pEX([a^2, -b, a + b])
            sage: g.quo_rem(f)
            ([[4947544 2492106] [4469276 6572944]], [[1864280 2123186]])
            sage: f.quo_rem(g)
            ([], [[5 1] [4 99]])"""
    @overload
    def quo_rem(self, f) -> Any:
        """ntl_ZZ_pEX.quo_rem(self, ntl_ZZ_pEX other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 417)

        Given polynomials a, b in ZZ_pE[X], if p is prime and the defining modulus irreducible,
        there exist polynomials q, r in ZZ_pE[X] such that a = b*q + r, deg(r) < deg(b).  This
        function returns (q, r).

        If p is not prime or the modulus is not irreducible, this function may raise a
        :exc:`RuntimeError` due to division by a noninvertible element of ZZ_p.

        EXAMPLES::

            sage: c = ntl.ZZ_pEContext(ntl.ZZ_pX([-5, 0, 1], 5^10))
            sage: a = c.ZZ_pE([5, 1])
            sage: b = c.ZZ_pE([4, 99])
            sage: f = c.ZZ_pEX([a, b])
            sage: g = c.ZZ_pEX([a^2, -b, a + b])
            sage: g.quo_rem(f)
            ([[4947544 2492106] [4469276 6572944]], [[1864280 2123186]])
            sage: f.quo_rem(g)
            ([], [[5 1] [4 99]])"""
    @overload
    def quo_rem(self, g) -> Any:
        """ntl_ZZ_pEX.quo_rem(self, ntl_ZZ_pEX other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 417)

        Given polynomials a, b in ZZ_pE[X], if p is prime and the defining modulus irreducible,
        there exist polynomials q, r in ZZ_pE[X] such that a = b*q + r, deg(r) < deg(b).  This
        function returns (q, r).

        If p is not prime or the modulus is not irreducible, this function may raise a
        :exc:`RuntimeError` due to division by a noninvertible element of ZZ_p.

        EXAMPLES::

            sage: c = ntl.ZZ_pEContext(ntl.ZZ_pX([-5, 0, 1], 5^10))
            sage: a = c.ZZ_pE([5, 1])
            sage: b = c.ZZ_pE([4, 99])
            sage: f = c.ZZ_pEX([a, b])
            sage: g = c.ZZ_pEX([a^2, -b, a + b])
            sage: g.quo_rem(f)
            ([[4947544 2492106] [4469276 6572944]], [[1864280 2123186]])
            sage: f.quo_rem(g)
            ([], [[5 1] [4 99]])"""
    @overload
    def resultant(self, ntl_ZZ_pEXother) -> Any:
        """ntl_ZZ_pEX.resultant(self, ntl_ZZ_pEX other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 1101)

        Return the resultant of ``self`` and ``other``.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 11))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: g = ntl.ZZ_pEX([a - b, b^2, a, a*b])
            sage: f.resultant(g)
            [1]
            sage: (f*g).resultant(f^2)
            []"""
    @overload
    def resultant(self, g) -> Any:
        """ntl_ZZ_pEX.resultant(self, ntl_ZZ_pEX other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 1101)

        Return the resultant of ``self`` and ``other``.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 11))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: g = ntl.ZZ_pEX([a - b, b^2, a, a*b])
            sage: f.resultant(g)
            [1]
            sage: (f*g).resultant(f^2)
            []"""
    @overload
    def reverse(self, hi=...) -> Any:
        """ntl_ZZ_pEX.reverse(self, hi=None)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 900)

        Return the polynomial obtained by reversing the coefficients
        of this polynomial.  If hi is set then this function behaves
        as if this polynomial has degree hi.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 11))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: f.reverse()
            [[1 2] [1 2] [3 2]]
            sage: f.reverse(hi=5)
            [[] [] [] [1 2] [1 2] [3 2]]
            sage: f.reverse(hi=1)
            [[1 2] [3 2]]
            sage: f.reverse(hi=-2)
            []"""
    @overload
    def reverse(self) -> Any:
        """ntl_ZZ_pEX.reverse(self, hi=None)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 900)

        Return the polynomial obtained by reversing the coefficients
        of this polynomial.  If hi is set then this function behaves
        as if this polynomial has degree hi.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 11))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: f.reverse()
            [[1 2] [1 2] [3 2]]
            sage: f.reverse(hi=5)
            [[] [] [] [1 2] [1 2] [3 2]]
            sage: f.reverse(hi=1)
            [[1 2] [3 2]]
            sage: f.reverse(hi=-2)
            []"""
    @overload
    def reverse(self, hi=...) -> Any:
        """ntl_ZZ_pEX.reverse(self, hi=None)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 900)

        Return the polynomial obtained by reversing the coefficients
        of this polynomial.  If hi is set then this function behaves
        as if this polynomial has degree hi.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 11))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: f.reverse()
            [[1 2] [1 2] [3 2]]
            sage: f.reverse(hi=5)
            [[] [] [] [1 2] [1 2] [3 2]]
            sage: f.reverse(hi=1)
            [[1 2] [3 2]]
            sage: f.reverse(hi=-2)
            []"""
    @overload
    def reverse(self, hi=...) -> Any:
        """ntl_ZZ_pEX.reverse(self, hi=None)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 900)

        Return the polynomial obtained by reversing the coefficients
        of this polynomial.  If hi is set then this function behaves
        as if this polynomial has degree hi.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 11))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: f.reverse()
            [[1 2] [1 2] [3 2]]
            sage: f.reverse(hi=5)
            [[] [] [] [1 2] [1 2] [3 2]]
            sage: f.reverse(hi=1)
            [[1 2] [3 2]]
            sage: f.reverse(hi=-2)
            []"""
    @overload
    def reverse(self, hi=...) -> Any:
        """ntl_ZZ_pEX.reverse(self, hi=None)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 900)

        Return the polynomial obtained by reversing the coefficients
        of this polynomial.  If hi is set then this function behaves
        as if this polynomial has degree hi.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 11))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: f.reverse()
            [[1 2] [1 2] [3 2]]
            sage: f.reverse(hi=5)
            [[] [] [] [1 2] [1 2] [3 2]]
            sage: f.reverse(hi=1)
            [[1 2] [3 2]]
            sage: f.reverse(hi=-2)
            []"""
    def right_shift(self, longn) -> Any:
        """ntl_ZZ_pEX.right_shift(self, long n)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 673)

        Return the polynomial obtained by shifting all coefficients of
        this polynomial to the right n positions.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 7))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b]); f
            [[3 2] [1 2] [1 2]]
            sage: f.right_shift(2)
            [[1 2]]
            sage: f.right_shift(5)
            []

        A negative right shift is a left shift::

            sage: f.right_shift(-5)
            [[] [] [] [] [] [3 2] [1 2] [1 2]]"""
    @overload
    def set_x(self) -> Any:
        '''ntl_ZZ_pEX.set_x(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 816)

        Set this polynomial to the monomial "x".

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 11))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: f
            [[3 2] [1 2] [1 2]]
            sage: f.set_x(); f
            [[] [1]]'''
    @overload
    def set_x(self) -> Any:
        '''ntl_ZZ_pEX.set_x(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 816)

        Set this polynomial to the monomial "x".

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 11))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: f
            [[3 2] [1 2] [1 2]]
            sage: f.set_x(); f
            [[] [1]]'''
    @overload
    def square(self) -> Any:
        """ntl_ZZ_pEX.square(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 448)

        Return `f^2`.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 7))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: f.square()
            [[5 1] [5 1] [2 1] [1] [4]]"""
    @overload
    def square(self) -> Any:
        """ntl_ZZ_pEX.square(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 448)

        Return `f^2`.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 7))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: f.square()
            [[5 1] [5 1] [2 1] [1] [4]]"""
    def square_and_truncate(self, longm) -> Any:
        """ntl_ZZ_pEX.square_and_truncate(self, long m)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 974)

        Return self*self but with terms of degree >= m removed.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 11))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: f^2
            [[5 8] [9 8] [6 8] [5] [8]]
            sage: f.square_and_truncate(3)
            [[5 8] [9 8] [6 8]]"""
    @overload
    def trace_mod(self, ntl_ZZ_pEXmodulus) -> Any:
        """ntl_ZZ_pEX.trace_mod(self, ntl_ZZ_pEX modulus)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 1046)

        Return the trace of this polynomial modulo the modulus.
        The modulus must be monic, and of positive degree bigger
        than the degree of ``self``.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 11))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: m = ntl.ZZ_pEX([a - b, b^2, a, a*b])
            sage: f.trace_mod(m)
            [8 1]"""
    @overload
    def trace_mod(self, m) -> Any:
        """ntl_ZZ_pEX.trace_mod(self, ntl_ZZ_pEX modulus)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 1046)

        Return the trace of this polynomial modulo the modulus.
        The modulus must be monic, and of positive degree bigger
        than the degree of ``self``.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 11))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: m = ntl.ZZ_pEX([a - b, b^2, a, a*b])
            sage: f.trace_mod(m)
            [8 1]"""
    def truncate(self, longm) -> Any:
        """ntl_ZZ_pEX.truncate(self, long m)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 928)

        Return the truncation of this polynomial obtained by
        removing all terms of degree >= m.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 11))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: f.truncate(3)
            [[3 2] [1 2] [1 2]]
            sage: f.truncate(1)
            [[3 2]]"""
    def xgcd(self, ntl_ZZ_pEXother) -> Any:
        """ntl_ZZ_pEX.xgcd(self, ntl_ZZ_pEX other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 732)

        Return `r`, `s`, `t` such that ``r = s*self + t*other``.

        Here `r` is the gcd of ``self`` and ``other``.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 11))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: g = ntl.ZZ_pEX([a-b, b^2, a])
            sage: h = ntl.ZZ_pEX([a^2-b, b^4, b,a])
            sage: r,s,t = (g*f).xgcd(h*f)
            sage: r
            [[4 6] [1] [1]]
            sage: f / ntl.ZZ_pEX([b])
            [[4 6] [1] [1]]
            sage: s*f*g+t*f*h
            [[4 6] [1] [1]]"""
    def __add__(self, ntl_ZZ_pEXself, ntl_ZZ_pEXother) -> Any:
        """ntl_ZZ_pEX.__add__(ntl_ZZ_pEX self, ntl_ZZ_pEX other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 280)

        Add ``self`` and ``other``.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 7))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: g = ntl.ZZ_pEX([-b, a])
            sage: f + g
            [[2] [4 4] [1 2]]"""
    def __copy__(self) -> Any:
        """ntl_ZZ_pEX.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 172)

        Return a copy of ``self``.

        TESTS::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 7))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: f
            [[3 2] [1 2] [1 2]]
            sage: y = copy(f)
            sage: y == f
            True
            sage: y is f
            False
            sage: f[0] = 0; y
            [[3 2] [1 2] [1 2]]"""
    def __delitem__(self, other) -> None:
        """Delete self[key]."""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __getitem__(self, longi) -> Any:
        """ntl_ZZ_pEX.__getitem__(self, long i)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 235)

        Return the i-th coefficient of ``self``.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 7))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: f[0]
            [3 2]
            sage: f[5]
            []"""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __mod__(self, ntl_ZZ_pEXself, ntl_ZZ_pEXother) -> Any:
        """ntl_ZZ_pEX.__mod__(ntl_ZZ_pEX self, ntl_ZZ_pEX other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 386)

        Given polynomials a, b in ZZ_pE[X], if p is prime and the defining modulus irreducible,
        there exist polynomials q, r in ZZ_pE[X] such that a = b*q + r, deg(r) < deg(b).  This
        function returns r.

        If p is not prime or the modulus is not irreducible, this
        function may raise a :exc:`RuntimeError` due to division by
        a noninvertible element of ZZ_p.

        EXAMPLES::

            sage: c = ntl.ZZ_pEContext(ntl.ZZ_pX([-5, 0, 1], 5^10))
            sage: a = c.ZZ_pE([5, 1])
            sage: b = c.ZZ_pE([4, 99])
            sage: f = c.ZZ_pEX([a, b])
            sage: g = c.ZZ_pEX([a^2, -b, a + b])
            sage: g % f
            [[1864280 2123186]]
            sage: f % g
            [[5 1] [4 99]]"""
    def __mul__(self, ntl_ZZ_pEXself, ntl_ZZ_pEXother) -> Any:
        """ntl_ZZ_pEX.__mul__(ntl_ZZ_pEX self, ntl_ZZ_pEX other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 326)

        Return the product ``self * other``.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 7))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: g = ntl.ZZ_pEX([-b, a])
            sage: f * g
            [[1 3] [1 1] [2 4] [6 4]]
            sage: c2 = ntl.ZZ_pEContext(ntl.ZZ_pX([4,1,1], 5)) # we can mix up the moduli
            sage: x = c2.ZZ_pEX([2,4])
            sage: x^2
            [[4] [1] [1]]
            sage: f * g # back to the first one and the ntl modulus gets reset correctly
            [[1 3] [1 1] [2 4] [6 4]]"""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __neg__(self) -> Any:
        """ntl_ZZ_pEX.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 593)

        Return the negative of ``self``.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 7))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: -f
            [[4 5] [6 5] [6 5]]"""
    def __pow__(self, ntl_ZZ_pEXself, longn, ignored) -> Any:
        """ntl_ZZ_pEX.__pow__(ntl_ZZ_pEX self, long n, ignored)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 468)

        Return the `n`-th nonnegative power of ``self``.

        EXAMPLES::

            sage: c = ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 7))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: f ^ 5
            [[5 1] [2 6] [4 5] [5 1] [] [6 2] [2 3] [0 1] [1 4] [3 6] [2 4]]
            sage: f ^ 0
            [[1]]
            sage: f ^ 1
            [[3 2] [1 2] [1 2]]
            sage: f ^ (-1)
            Traceback (most recent call last):
            ...
            ArithmeticError"""
    def __radd__(self, other):
        """Return value+self."""
    def __reduce__(self) -> Any:
        """ntl_ZZ_pEX.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 143)

        TESTS::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 7))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: loads(dumps(f)) == f
            True"""
    def __rmod__(self, other):
        """Return value%self."""
    def __rmul__(self, other):
        """Return value*self."""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
    def __rsub__(self, other):
        """Return value-self."""
    def __rtruediv__(self, other):
        """Return value/self."""
    def __setitem__(self, longi, a) -> Any:
        """ntl_ZZ_pEX.__setitem__(self, long i, a)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 212)

        Set the i-th coefficient of ``self`` to be a.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 7))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: f[1] = 4; f
            [[3 2] [4] [1 2]]"""
    def __sub__(self, ntl_ZZ_pEXself, ntl_ZZ_pEXother) -> Any:
        """ntl_ZZ_pEX.__sub__(ntl_ZZ_pEX self, ntl_ZZ_pEX other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 303)

        Subtracts ``other`` from ``self``.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 7))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a, b, b])
            sage: g = ntl.ZZ_pEX([-b, a])
            sage: f - g
            [[4 4] [5] [1 2]]"""
    def __truediv__(self, ntl_ZZ_pEXself, ntl_ZZ_pEXother) -> Any:
        """ntl_ZZ_pEX.__truediv__(ntl_ZZ_pEX self, ntl_ZZ_pEX other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEX.pyx (starting at line 355)

        Compute quotient ``self / other``, if the quotient is a polynomial.
        Otherwise an Exception is raised.

        EXAMPLES::

            sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 7))
            sage: a = ntl.ZZ_pE([3,2], c)
            sage: b = ntl.ZZ_pE([1,2], c)
            sage: f = ntl.ZZ_pEX([a^2, -a*b-a*b, b^2])
            sage: g = ntl.ZZ_pEX([-a, b])
            sage: f / g
            [[4 5] [1 2]]
            sage: g / f
            Traceback (most recent call last):
            ...
            ArithmeticError: self (=[[4 5] [1 2]]) is not divisible by other (=[[5 1] [2 6] [4]])"""
