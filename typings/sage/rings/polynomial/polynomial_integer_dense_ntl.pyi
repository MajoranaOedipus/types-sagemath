import cypari2.pari_instance
import sage.rings.polynomial.polynomial_element
from sage.arith.functions import lcm as lcm
from sage.categories.category import ZZ as ZZ, ZZ_sage as ZZ_sage
from sage.rings.fraction_field_element import FractionFieldElement as FractionFieldElement
from sage.rings.integer_ring import IntegerRing as IntegerRing
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import coerce_binop as coerce_binop, have_same_parent as have_same_parent, parent as parent
from sage.structure.factorization import Factorization as Factorization
from typing import Any, ClassVar, overload

pari: cypari2.pari_instance.Pari

class Polynomial_integer_dense_ntl(sage.rings.polynomial.polynomial_element.Polynomial):
    """Polynomial_integer_dense_ntl(parent, x=None, check=True, is_gen=False, construct=False)

    File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_ntl.pyx (starting at line 74)

    A dense polynomial over the integers, implemented via NTL."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, x=..., check=..., is_gen=..., construct=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_ntl.pyx (starting at line 88)

                EXAMPLES::

                    sage: R.<x> = PolynomialRing(ZZ, implementation='NTL')
                    sage: x
                    x

                Construct from list and tuple::

                    sage: R([])
                    0
                    sage: R([1, -2, 3])
                    3*x^2 - 2*x + 1
                    sage: R(())
                    0
                    sage: R((1, -2, 3))
                    3*x^2 - 2*x + 1

                Coercions from other rings are attempted automatically::

                    sage: R([1, -6/3, 3])
                    3*x^2 - 2*x + 1
                    sage: R([1, 5/2, 2])
                    Traceback (most recent call last):
                    ...
                    TypeError: no conversion of this rational to integer

                Construct from constant::

                    sage: R(3)
                    3

                Coercion from PARI polynomial::

                    sage: f = R([-1, 2, 5]); f
                    5*x^2 + 2*x - 1
                    sage: type(f)
                    <class 'sage.rings.polynomial.polynomial_integer_dense_ntl.Polynomial_integer_dense_ntl'>
                    sage: type(pari(f))
                    <class 'cypari2.gen.Gen'>
                    sage: type(R(pari(f)))
                    <class 'sage.rings.polynomial.polynomial_integer_dense_ntl.Polynomial_integer_dense_ntl'>
                    sage: R(pari(f))
                    5*x^2 + 2*x - 1

                Coercion from NTL polynomial::

                    sage: f = ntl.ZZX([1, 2, 3])
                    sage: print(R(f))
                    3*x^2 + 2*x + 1

                Coercion from dictionary::

                    sage: f = R({2: -4, 3: 47}); f
                    47*x^3 - 4*x^2

                Coercion from fraction field element with trivial denominator::

                    sage: f = (x^3 - 1) / (x - 1)
                    sage: type(f)
                    <class 'sage.rings.fraction_field_element.FractionFieldElement'>
                    sage: g = R(f); g
                    x^2 + x + 1

                NTL polynomials are limited in size to slightly under the word length::

                    sage: PolynomialRing(ZZ, 'x', implementation='NTL')({2^3: 1})
                    x^8
                    sage: import sys
                    sage: PolynomialRing(ZZ, 'x', implementation='NTL')({sys.maxsize>>1: 1})
                    Traceback (most recent call last):
                    ...
                    OverflowError: Dense NTL integer polynomials have a maximum degree of 268435455    # 32-bit
                    OverflowError: Dense NTL integer polynomials have a maximum degree of 1152921504606846975    # 64-bit
        """
    @overload
    def content(self) -> Any:
        """Polynomial_integer_dense_ntl.content(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_ntl.pyx (starting at line 240)

        Return the greatest common divisor of the coefficients of this
        polynomial. The sign is the sign of the leading coefficient.
        The content of the zero polynomial is zero.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ, implementation='NTL')
            sage: (2*x^2 - 4*x^4 + 14*x^7).content()
            2
            sage: (2*x^2 - 4*x^4 - 14*x^7).content()
            -2
            sage: x.content()
            1
            sage: R(1).content()
            1
            sage: R(0).content()
            0"""
    @overload
    def content(self) -> Any:
        """Polynomial_integer_dense_ntl.content(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_ntl.pyx (starting at line 240)

        Return the greatest common divisor of the coefficients of this
        polynomial. The sign is the sign of the leading coefficient.
        The content of the zero polynomial is zero.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ, implementation='NTL')
            sage: (2*x^2 - 4*x^4 + 14*x^7).content()
            2
            sage: (2*x^2 - 4*x^4 - 14*x^7).content()
            -2
            sage: x.content()
            1
            sage: R(1).content()
            1
            sage: R(0).content()
            0"""
    @overload
    def content(self) -> Any:
        """Polynomial_integer_dense_ntl.content(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_ntl.pyx (starting at line 240)

        Return the greatest common divisor of the coefficients of this
        polynomial. The sign is the sign of the leading coefficient.
        The content of the zero polynomial is zero.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ, implementation='NTL')
            sage: (2*x^2 - 4*x^4 + 14*x^7).content()
            2
            sage: (2*x^2 - 4*x^4 - 14*x^7).content()
            -2
            sage: x.content()
            1
            sage: R(1).content()
            1
            sage: R(0).content()
            0"""
    @overload
    def content(self) -> Any:
        """Polynomial_integer_dense_ntl.content(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_ntl.pyx (starting at line 240)

        Return the greatest common divisor of the coefficients of this
        polynomial. The sign is the sign of the leading coefficient.
        The content of the zero polynomial is zero.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ, implementation='NTL')
            sage: (2*x^2 - 4*x^4 + 14*x^7).content()
            2
            sage: (2*x^2 - 4*x^4 - 14*x^7).content()
            -2
            sage: x.content()
            1
            sage: R(1).content()
            1
            sage: R(0).content()
            0"""
    @overload
    def content(self) -> Any:
        """Polynomial_integer_dense_ntl.content(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_ntl.pyx (starting at line 240)

        Return the greatest common divisor of the coefficients of this
        polynomial. The sign is the sign of the leading coefficient.
        The content of the zero polynomial is zero.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ, implementation='NTL')
            sage: (2*x^2 - 4*x^4 + 14*x^7).content()
            2
            sage: (2*x^2 - 4*x^4 - 14*x^7).content()
            -2
            sage: x.content()
            1
            sage: R(1).content()
            1
            sage: R(0).content()
            0"""
    @overload
    def content(self) -> Any:
        """Polynomial_integer_dense_ntl.content(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_ntl.pyx (starting at line 240)

        Return the greatest common divisor of the coefficients of this
        polynomial. The sign is the sign of the leading coefficient.
        The content of the zero polynomial is zero.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ, implementation='NTL')
            sage: (2*x^2 - 4*x^4 + 14*x^7).content()
            2
            sage: (2*x^2 - 4*x^4 - 14*x^7).content()
            -2
            sage: x.content()
            1
            sage: R(1).content()
            1
            sage: R(0).content()
            0"""
    @overload
    def degree(self, gen=...) -> Any:
        """Polynomial_integer_dense_ntl.degree(self, gen=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_ntl.pyx (starting at line 803)

        Return the degree of this polynomial. The zero polynomial has
        degree `-1`.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ, implementation='NTL')
            sage: x.degree()
            1
            sage: (x^2).degree()
            2
            sage: R(1).degree()
            0
            sage: R(0).degree()
            -1"""
    @overload
    def degree(self) -> Any:
        """Polynomial_integer_dense_ntl.degree(self, gen=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_ntl.pyx (starting at line 803)

        Return the degree of this polynomial. The zero polynomial has
        degree `-1`.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ, implementation='NTL')
            sage: x.degree()
            1
            sage: (x^2).degree()
            2
            sage: R(1).degree()
            0
            sage: R(0).degree()
            -1"""
    @overload
    def degree(self) -> Any:
        """Polynomial_integer_dense_ntl.degree(self, gen=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_ntl.pyx (starting at line 803)

        Return the degree of this polynomial. The zero polynomial has
        degree `-1`.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ, implementation='NTL')
            sage: x.degree()
            1
            sage: (x^2).degree()
            2
            sage: R(1).degree()
            0
            sage: R(0).degree()
            -1"""
    @overload
    def degree(self) -> Any:
        """Polynomial_integer_dense_ntl.degree(self, gen=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_ntl.pyx (starting at line 803)

        Return the degree of this polynomial. The zero polynomial has
        degree `-1`.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ, implementation='NTL')
            sage: x.degree()
            1
            sage: (x^2).degree()
            2
            sage: R(1).degree()
            0
            sage: R(0).degree()
            -1"""
    @overload
    def degree(self) -> Any:
        """Polynomial_integer_dense_ntl.degree(self, gen=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_ntl.pyx (starting at line 803)

        Return the degree of this polynomial. The zero polynomial has
        degree `-1`.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ, implementation='NTL')
            sage: x.degree()
            1
            sage: (x^2).degree()
            2
            sage: R(1).degree()
            0
            sage: R(0).degree()
            -1"""
    def discriminant(self, proof=...) -> Any:
        """Polynomial_integer_dense_ntl.discriminant(self, proof=True)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_ntl.pyx (starting at line 822)

        Return the discriminant of ``self``, which is by definition

        .. MATH::

            (-1)^{m(m-1)/2} \\text{resultant}(a, a')/lc(a),

        where `m = deg(a)`, and `lc(a)` is the leading coefficient of a.
        If ``proof`` is False (the default is True), then this function
        may use a randomized strategy that errors with probability no
        more than `2^{-80}`.

        EXAMPLES::

            sage: f = ntl.ZZX([1,2,0,3])
            sage: f.discriminant()
            -339
            sage: f.discriminant(proof=False)
            -339"""
    def factor(self) -> Any:
        """Polynomial_integer_dense_ntl.factor(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_ntl.pyx (starting at line 962)

        This function overrides the generic polynomial factorization to
        make a somewhat intelligent decision to use PARI or NTL based on
        some benchmarking.

        Note: This function factors the content of the polynomial,
        which can take very long if it's a really big integer.  If you
        do not need the content factored, divide it out of your
        polynomial before calling this function.

        EXAMPLES::

            sage: R.<x> = ZZ[]
            sage: f = x^4 - 1
            sage: f.factor()
            (x - 1) * (x + 1) * (x^2 + 1)
            sage: f = 1 - x
            sage: f.factor()
            (-1) * (x - 1)
            sage: f.factor().unit()
            -1
            sage: f = -30*x; f.factor()
            (-1) * 2 * 3 * 5 * x"""
    def factor_mod(self, p) -> Any:
        """Polynomial_integer_dense_ntl.factor_mod(self, p)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_ntl.pyx (starting at line 996)

        Return the factorization of ``self`` modulo the prime `p`.

        INPUT:

        - ``p`` -- prime

        OUTPUT: factorization of ``self`` reduced modulo `p`

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ, 'x', implementation='NTL')
            sage: f = -3*x*(x-2)*(x-9) + x
            sage: f.factor_mod(3)
            x
            sage: f = -3*x*(x-2)*(x-9)
            sage: f.factor_mod(3)
            Traceback (most recent call last):
            ...
            ArithmeticError: factorization of 0 is not defined

            sage: f = 2*x*(x-2)*(x-9)
            sage: f.factor_mod(7)
            (2) * x * (x + 5)^2"""
    def factor_padic(self, p, prec=...) -> Any:
        """Polynomial_integer_dense_ntl.factor_padic(self, p, prec=10)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_ntl.pyx (starting at line 1034)

        Return `p`-adic factorization of ``self`` to given precision.

        INPUT:

        - ``p`` -- prime

        - ``prec`` -- integer; the precision

        OUTPUT: factorization of ``self`` over the completion at `p`

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ, implementation='NTL')
            sage: f = x^2 + 1
            sage: f.factor_padic(5, 4)
            ((1 + O(5^4))*x + 2 + 5 + 2*5^2 + 5^3 + O(5^4))
            * ((1 + O(5^4))*x + 3 + 3*5 + 2*5^2 + 3*5^3 + O(5^4))

        A more difficult example::

            sage: f = 100 * (5*x + 1)^2 * (x + 5)^2
            sage: f.factor_padic(5, 10)
            (4 + O(5^10)) * (5 + O(5^11))^2 * ((1 + O(5^10))*x + 5 + O(5^10))^2
            * ((5 + O(5^10))*x + 1 + O(5^10))^2"""
    @overload
    def gcd(self, right) -> Any:
        """Polynomial_integer_dense_ntl.gcd(self, right)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_ntl.pyx (starting at line 565)

        Return the GCD of ``self`` and ``right``.  The leading
        coefficient need not be 1.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ, implementation='NTL')
            sage: f = (6*x + 47) * (7*x^2 - 2*x + 38)
            sage: g = (6*x + 47) * (3*x^3 + 2*x + 1)
            sage: f.gcd(g)
            6*x + 47"""
    @overload
    def gcd(self, g) -> Any:
        """Polynomial_integer_dense_ntl.gcd(self, right)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_ntl.pyx (starting at line 565)

        Return the GCD of ``self`` and ``right``.  The leading
        coefficient need not be 1.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ, implementation='NTL')
            sage: f = (6*x + 47) * (7*x^2 - 2*x + 38)
            sage: g = (6*x + 47) * (3*x^3 + 2*x + 1)
            sage: f.gcd(g)
            6*x + 47"""
    @overload
    def lcm(self, right) -> Any:
        """Polynomial_integer_dense_ntl.lcm(self, right)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_ntl.pyx (starting at line 586)

        Return the LCM of ``self`` and ``right``.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ, implementation='NTL')
            sage: f = (6*x + 47) * (7*x^2 - 2*x + 38)
            sage: g = (6*x + 47) * (3*x^3 + 2*x + 1)
            sage: h = f.lcm(g); h
            126*x^6 + 951*x^5 + 486*x^4 + 6034*x^3 + 585*x^2 + 3706*x + 1786
            sage: h == (6*x + 47) * (7*x^2 - 2*x + 38) * (3*x^3 + 2*x + 1)
            True

        TESTS:

        Check that :issue:`32033` has been fixed::

            sage: R.<x> = PolynomialRing(ZZ, implementation='NTL')
            sage: R(0).lcm(R(0))
            0"""
    @overload
    def lcm(self, g) -> Any:
        """Polynomial_integer_dense_ntl.lcm(self, right)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_ntl.pyx (starting at line 586)

        Return the LCM of ``self`` and ``right``.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ, implementation='NTL')
            sage: f = (6*x + 47) * (7*x^2 - 2*x + 38)
            sage: g = (6*x + 47) * (3*x^3 + 2*x + 1)
            sage: h = f.lcm(g); h
            126*x^6 + 951*x^5 + 486*x^4 + 6034*x^3 + 585*x^2 + 3706*x + 1786
            sage: h == (6*x + 47) * (7*x^2 - 2*x + 38) * (3*x^3 + 2*x + 1)
            True

        TESTS:

        Check that :issue:`32033` has been fixed::

            sage: R.<x> = PolynomialRing(ZZ, implementation='NTL')
            sage: R(0).lcm(R(0))
            0"""
    @overload
    def list(self, boolcopy=...) -> list:
        """Polynomial_integer_dense_ntl.list(self, bool copy=True) -> list

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_ntl.pyx (starting at line 1076)

        Return a new copy of the list of the underlying
        elements of ``self``.

        EXAMPLES::

            sage: x = PolynomialRing(ZZ, 'x', implementation='NTL').0
            sage: f = x^3 + 3*x - 17
            sage: f.list()
            [-17, 3, 0, 1]
            sage: f = PolynomialRing(ZZ, 'x', implementation='NTL')(0)
            sage: f.list()
            []"""
    @overload
    def list(self) -> Any:
        """Polynomial_integer_dense_ntl.list(self, bool copy=True) -> list

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_ntl.pyx (starting at line 1076)

        Return a new copy of the list of the underlying
        elements of ``self``.

        EXAMPLES::

            sage: x = PolynomialRing(ZZ, 'x', implementation='NTL').0
            sage: f = x^3 + 3*x - 17
            sage: f.list()
            [-17, 3, 0, 1]
            sage: f = PolynomialRing(ZZ, 'x', implementation='NTL')(0)
            sage: f.list()
            []"""
    @overload
    def list(self) -> Any:
        """Polynomial_integer_dense_ntl.list(self, bool copy=True) -> list

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_ntl.pyx (starting at line 1076)

        Return a new copy of the list of the underlying
        elements of ``self``.

        EXAMPLES::

            sage: x = PolynomialRing(ZZ, 'x', implementation='NTL').0
            sage: f = x^3 + 3*x - 17
            sage: f.list()
            [-17, 3, 0, 1]
            sage: f = PolynomialRing(ZZ, 'x', implementation='NTL')(0)
            sage: f.list()
            []"""
    @overload
    def quo_rem(self, right) -> Any:
        """Polynomial_integer_dense_ntl.quo_rem(self, right)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_ntl.pyx (starting at line 480)

        Attempt to divide ``self`` by ``right``, and return a quotient and remainder.

        If right is monic, then it returns ``(q, r)`` where ``self = q * right + r``
        and ``deg(r) < deg(right)``.

        If right is not monic, then it returns `(q, 0)` where ``q = self/right`` if
        ``right`` exactly divides ``self``, otherwise it raises an exception.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ, implementation='NTL')
            sage: f = R(range(10)); g = R([-1, 0, 1])
            sage: q, r = f.quo_rem(g)
            sage: q, r
            (9*x^7 + 8*x^6 + 16*x^5 + 14*x^4 + 21*x^3 + 18*x^2 + 24*x + 20, 25*x + 20)
            sage: q*g + r == f
            True

            sage: 0//(2*x)
            0

            sage: f = x^2
            sage: f.quo_rem(0)
            Traceback (most recent call last):
            ...
            ArithmeticError: division by zero polynomial

            sage: f = (x^2 + 3) * (2*x - 1)
            sage: f.quo_rem(2*x - 1)
            (x^2 + 3, 0)

            sage: f = x^2
            sage: f.quo_rem(2*x - 1)
            Traceback (most recent call last):
            ...
            ArithmeticError: division not exact in Z[x] (consider coercing to Q[x] first)

        TESTS::

            sage: z = R(0)
            sage: z.quo_rem(1)
            (0, 0)
            sage: z.quo_rem(x)
            (0, 0)
            sage: z.quo_rem(2*x)
            (0, 0)"""
    @overload
    def quo_rem(self, g) -> Any:
        """Polynomial_integer_dense_ntl.quo_rem(self, right)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_ntl.pyx (starting at line 480)

        Attempt to divide ``self`` by ``right``, and return a quotient and remainder.

        If right is monic, then it returns ``(q, r)`` where ``self = q * right + r``
        and ``deg(r) < deg(right)``.

        If right is not monic, then it returns `(q, 0)` where ``q = self/right`` if
        ``right`` exactly divides ``self``, otherwise it raises an exception.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ, implementation='NTL')
            sage: f = R(range(10)); g = R([-1, 0, 1])
            sage: q, r = f.quo_rem(g)
            sage: q, r
            (9*x^7 + 8*x^6 + 16*x^5 + 14*x^4 + 21*x^3 + 18*x^2 + 24*x + 20, 25*x + 20)
            sage: q*g + r == f
            True

            sage: 0//(2*x)
            0

            sage: f = x^2
            sage: f.quo_rem(0)
            Traceback (most recent call last):
            ...
            ArithmeticError: division by zero polynomial

            sage: f = (x^2 + 3) * (2*x - 1)
            sage: f.quo_rem(2*x - 1)
            (x^2 + 3, 0)

            sage: f = x^2
            sage: f.quo_rem(2*x - 1)
            Traceback (most recent call last):
            ...
            ArithmeticError: division not exact in Z[x] (consider coercing to Q[x] first)

        TESTS::

            sage: z = R(0)
            sage: z.quo_rem(1)
            (0, 0)
            sage: z.quo_rem(x)
            (0, 0)
            sage: z.quo_rem(2*x)
            (0, 0)"""
    @overload
    def quo_rem(self, x) -> Any:
        """Polynomial_integer_dense_ntl.quo_rem(self, right)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_ntl.pyx (starting at line 480)

        Attempt to divide ``self`` by ``right``, and return a quotient and remainder.

        If right is monic, then it returns ``(q, r)`` where ``self = q * right + r``
        and ``deg(r) < deg(right)``.

        If right is not monic, then it returns `(q, 0)` where ``q = self/right`` if
        ``right`` exactly divides ``self``, otherwise it raises an exception.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ, implementation='NTL')
            sage: f = R(range(10)); g = R([-1, 0, 1])
            sage: q, r = f.quo_rem(g)
            sage: q, r
            (9*x^7 + 8*x^6 + 16*x^5 + 14*x^4 + 21*x^3 + 18*x^2 + 24*x + 20, 25*x + 20)
            sage: q*g + r == f
            True

            sage: 0//(2*x)
            0

            sage: f = x^2
            sage: f.quo_rem(0)
            Traceback (most recent call last):
            ...
            ArithmeticError: division by zero polynomial

            sage: f = (x^2 + 3) * (2*x - 1)
            sage: f.quo_rem(2*x - 1)
            (x^2 + 3, 0)

            sage: f = x^2
            sage: f.quo_rem(2*x - 1)
            Traceback (most recent call last):
            ...
            ArithmeticError: division not exact in Z[x] (consider coercing to Q[x] first)

        TESTS::

            sage: z = R(0)
            sage: z.quo_rem(1)
            (0, 0)
            sage: z.quo_rem(x)
            (0, 0)
            sage: z.quo_rem(2*x)
            (0, 0)"""
    @overload
    def real_root_intervals(self) -> Any:
        """Polynomial_integer_dense_ntl.real_root_intervals(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_ntl.pyx (starting at line 781)

        Return isolating intervals for the real roots of this polynomial.

        EXAMPLES:
        We compute the roots of the characteristic polynomial of some Salem numbers::

            sage: R.<x> = PolynomialRing(ZZ, implementation='NTL')
            sage: f = 1 - x^2 - x^3 - x^4 + x^6
            sage: f.real_root_intervals()                                               # needs sage.libs.linbox
            [((1/2, 3/4), 1), ((1, 3/2), 1)]"""
    @overload
    def real_root_intervals(self) -> Any:
        """Polynomial_integer_dense_ntl.real_root_intervals(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_ntl.pyx (starting at line 781)

        Return isolating intervals for the real roots of this polynomial.

        EXAMPLES:
        We compute the roots of the characteristic polynomial of some Salem numbers::

            sage: R.<x> = PolynomialRing(ZZ, implementation='NTL')
            sage: f = 1 - x^2 - x^3 - x^4 + x^6
            sage: f.real_root_intervals()                                               # needs sage.libs.linbox
            [((1/2, 3/4), 1), ((1, 3/2), 1)]"""
    @overload
    def resultant(self, other, proof=...) -> Any:
        """Polynomial_integer_dense_ntl.resultant(self, other, proof=True)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_ntl.pyx (starting at line 1093)

        Return the resultant of ``self`` and ``other``, which must lie in the same
        polynomial ring.

        If ``proof=False`` (the default is ``proof=True``), then this function may use a
        randomized strategy that errors with probability no more than `2^{-80}`.

        INPUT:

        - ``other`` -- a polynomial

        OUTPUT: an element of the base ring of the polynomial ring

        EXAMPLES::

            sage: x = PolynomialRing(ZZ, 'x', implementation='NTL').0
            sage: f = x^3 + x + 1;  g = x^3 - x - 1
            sage: r = f.resultant(g); r
            -8
            sage: r.parent() is ZZ
            True"""
    @overload
    def resultant(self, g) -> Any:
        """Polynomial_integer_dense_ntl.resultant(self, other, proof=True)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_ntl.pyx (starting at line 1093)

        Return the resultant of ``self`` and ``other``, which must lie in the same
        polynomial ring.

        If ``proof=False`` (the default is ``proof=True``), then this function may use a
        randomized strategy that errors with probability no more than `2^{-80}`.

        INPUT:

        - ``other`` -- a polynomial

        OUTPUT: an element of the base ring of the polynomial ring

        EXAMPLES::

            sage: x = PolynomialRing(ZZ, 'x', implementation='NTL').0
            sage: f = x^3 + x + 1;  g = x^3 - x - 1
            sage: r = f.resultant(g); r
            -8
            sage: r.parent() is ZZ
            True"""
    @overload
    def squarefree_decomposition(self) -> Any:
        """Polynomial_integer_dense_ntl.squarefree_decomposition(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_ntl.pyx (starting at line 862)

        Return the square-free decomposition of ``self``.  This is
        a partial factorization of ``self`` into square-free, relatively
        prime polynomials.

        This is a wrapper for the NTL function ``SquareFreeDecomp``.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ, implementation='NTL')
            sage: p = 37 * (x-1)^2 * (x-2)^2 * (x-3)^3 * (x-4)
            sage: p.squarefree_decomposition()
            (37) * (x - 4) * (x^2 - 3*x + 2)^2 * (x - 3)^3

        TESTS:

        Verify that :issue:`13053` has been resolved::

            sage: R.<x> = PolynomialRing(ZZ, implementation='NTL')
            sage: f = -x^2
            sage: f.squarefree_decomposition()
            (-1) * x^2"""
    @overload
    def squarefree_decomposition(self) -> Any:
        """Polynomial_integer_dense_ntl.squarefree_decomposition(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_ntl.pyx (starting at line 862)

        Return the square-free decomposition of ``self``.  This is
        a partial factorization of ``self`` into square-free, relatively
        prime polynomials.

        This is a wrapper for the NTL function ``SquareFreeDecomp``.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ, implementation='NTL')
            sage: p = 37 * (x-1)^2 * (x-2)^2 * (x-3)^3 * (x-4)
            sage: p.squarefree_decomposition()
            (37) * (x - 4) * (x^2 - 3*x + 2)^2 * (x - 3)^3

        TESTS:

        Verify that :issue:`13053` has been resolved::

            sage: R.<x> = PolynomialRing(ZZ, implementation='NTL')
            sage: f = -x^2
            sage: f.squarefree_decomposition()
            (-1) * x^2"""
    @overload
    def squarefree_decomposition(self) -> Any:
        """Polynomial_integer_dense_ntl.squarefree_decomposition(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_ntl.pyx (starting at line 862)

        Return the square-free decomposition of ``self``.  This is
        a partial factorization of ``self`` into square-free, relatively
        prime polynomials.

        This is a wrapper for the NTL function ``SquareFreeDecomp``.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ, implementation='NTL')
            sage: p = 37 * (x-1)^2 * (x-2)^2 * (x-3)^3 * (x-4)
            sage: p.squarefree_decomposition()
            (37) * (x - 4) * (x^2 - 3*x + 2)^2 * (x - 3)^3

        TESTS:

        Verify that :issue:`13053` has been resolved::

            sage: R.<x> = PolynomialRing(ZZ, implementation='NTL')
            sage: f = -x^2
            sage: f.squarefree_decomposition()
            (-1) * x^2"""
    def xgcd(self, right) -> Any:
        """Polynomial_integer_dense_ntl.xgcd(self, right)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_ntl.pyx (starting at line 615)

        This function can't in general return `(g,s,t)` as above,
        since they need not exist.  Instead, over the integers, we
        first multiply `g` by a divisor of the resultant of `a/g` and
        `b/g`, up to sign, and return ``g, u, v`` such that
        ``g = u*self + v*right``.  But note that this `g` may be a
        multiple of the gcd.

        If ``self`` and ``right`` are coprime as polynomials over the
        rationals, then ``g`` is guaranteed to be the resultant of
        ``self`` and ``right``, as a constant polynomial.

        EXAMPLES::

            sage: P.<x> = PolynomialRing(ZZ, implementation='NTL')
            sage: F = (x^2 + 2)*x^3; G = (x^2+2)*(x-3)
            sage: g, u, v = F.xgcd(G)
            sage: g, u, v
            (27*x^2 + 54, 1, -x^2 - 3*x - 9)
            sage: u*F + v*G
            27*x^2 + 54
            sage: x.xgcd(P(0))
            (x, 1, 0)
            sage: f = P(0)
            sage: f.xgcd(x)
            (x, 0, 1)
            sage: F = (x-3)^3; G = (x-15)^2
            sage: g, u, v = F.xgcd(G)
            sage: g, u, v
            (2985984, -432*x + 8208, 432*x^2 + 864*x + 14256)
            sage: u*F + v*G
            2985984"""
    def __floordiv__(self, right) -> Any:
        """Polynomial_integer_dense_ntl.__floordiv__(self, right)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_ntl.pyx (starting at line 730)

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ, implementation='NTL')
            sage: f = R([9,6,1]) ; f
            x^2 + 6*x + 9
            sage: f // x
            x + 6
            sage: f // 3
            2*x + 3
            sage: g = x^3 ; g
            x^3
            sage: f // g
            0
            sage: g // f
            x - 6"""
    def __pari__(self, variable=...) -> Any:
        '''Polynomial_integer_dense_ntl.__pari__(self, variable=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_ntl.pyx (starting at line 849)

        EXAMPLES::

            sage: t = PolynomialRing(ZZ, "t", implementation=\'NTL\').gen()
            sage: f = t^3 + 3*t - 17
            sage: pari(f)
            t^3 + 3*t - 17'''
    def __reduce__(self) -> Any:
        """Polynomial_integer_dense_ntl.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_ntl.pyx (starting at line 325)

        Used for pickling.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ, implementation='NTL')
            sage: loads(dumps(x)) == x
            True
            sage: f = 2*x + 3
            sage: loads(dumps(f)) == f
            True"""
    def __rfloordiv__(self, other):
        """Return value//self."""
