import cypari2.pari_instance
import sage.rings.polynomial.polynomial_element
from sage.arith.functions import lcm as lcm
from sage.categories.category import ZZ as ZZ
from sage.rings.fraction_field_element import FractionFieldElement as FractionFieldElement
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import coerce_binop as coerce_binop, have_same_parent as have_same_parent, parent as parent
from sage.structure.factorization import Factorization as Factorization
from typing import Any, ClassVar, overload

pari: cypari2.pari_instance.Pari

class Polynomial_integer_dense_flint(sage.rings.polynomial.polynomial_element.Polynomial):
    """Polynomial_integer_dense_flint(parent, x=None, check=True, is_gen=False, construct=False)

    File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 81)

    A dense polynomial over the integers, implemented via FLINT.

    TESTS::

        sage: f = ZZ['x'].random_element()
        sage: from sage.rings.polynomial.polynomial_integer_dense_flint import Polynomial_integer_dense_flint
        sage: isinstance(f, Polynomial_integer_dense_flint)
        True

    .. automethod:: _add_
    .. automethod:: _sub_
    .. automethod:: _lmul_
    .. automethod:: _rmul_
    .. automethod:: _mul_
    .. automethod:: _mul_trunc_"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, x=..., check=..., is_gen=..., construct=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 145)

                EXAMPLES::

                    sage: R.<x> = PolynomialRing(ZZ)
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
                    <class 'sage.rings.polynomial.polynomial_integer_dense_flint.Polynomial_integer_dense_flint'>
                    sage: type(pari(f))
                    <class 'cypari2.gen.Gen'>
                    sage: type(R(pari(f)))
                    <class 'sage.rings.polynomial.polynomial_integer_dense_flint.Polynomial_integer_dense_flint'>
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

                    sage: ZZ['x']({2^3: 1})
                    x^8
        """
    @overload
    def content(self) -> Integer:
        """Polynomial_integer_dense_flint.content(self) -> Integer

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 474)

        Return the greatest common divisor of the coefficients of this
        polynomial. The sign is the sign of the leading coefficient.  The
        content of the zero polynomial is zero.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ)
            sage: (2*x^2 - 4*x^4 + 14*x^7).content()
            2
            sage: x.content()
            1
            sage: R(1).content()
            1
            sage: R(0).content()
            0

        TESTS::

            sage: t = x^2+x+1
            sage: t.content()
            1
            sage: (123456789123456789123456789123456789123456789*t).content()
            123456789123456789123456789123456789123456789

        Verify that :issue:`13053` has been resolved::

            sage: R(-1).content()
            -1"""
    @overload
    def content(self) -> Any:
        """Polynomial_integer_dense_flint.content(self) -> Integer

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 474)

        Return the greatest common divisor of the coefficients of this
        polynomial. The sign is the sign of the leading coefficient.  The
        content of the zero polynomial is zero.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ)
            sage: (2*x^2 - 4*x^4 + 14*x^7).content()
            2
            sage: x.content()
            1
            sage: R(1).content()
            1
            sage: R(0).content()
            0

        TESTS::

            sage: t = x^2+x+1
            sage: t.content()
            1
            sage: (123456789123456789123456789123456789123456789*t).content()
            123456789123456789123456789123456789123456789

        Verify that :issue:`13053` has been resolved::

            sage: R(-1).content()
            -1"""
    @overload
    def content(self) -> Any:
        """Polynomial_integer_dense_flint.content(self) -> Integer

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 474)

        Return the greatest common divisor of the coefficients of this
        polynomial. The sign is the sign of the leading coefficient.  The
        content of the zero polynomial is zero.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ)
            sage: (2*x^2 - 4*x^4 + 14*x^7).content()
            2
            sage: x.content()
            1
            sage: R(1).content()
            1
            sage: R(0).content()
            0

        TESTS::

            sage: t = x^2+x+1
            sage: t.content()
            1
            sage: (123456789123456789123456789123456789123456789*t).content()
            123456789123456789123456789123456789123456789

        Verify that :issue:`13053` has been resolved::

            sage: R(-1).content()
            -1"""
    @overload
    def content(self) -> Any:
        """Polynomial_integer_dense_flint.content(self) -> Integer

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 474)

        Return the greatest common divisor of the coefficients of this
        polynomial. The sign is the sign of the leading coefficient.  The
        content of the zero polynomial is zero.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ)
            sage: (2*x^2 - 4*x^4 + 14*x^7).content()
            2
            sage: x.content()
            1
            sage: R(1).content()
            1
            sage: R(0).content()
            0

        TESTS::

            sage: t = x^2+x+1
            sage: t.content()
            1
            sage: (123456789123456789123456789123456789123456789*t).content()
            123456789123456789123456789123456789123456789

        Verify that :issue:`13053` has been resolved::

            sage: R(-1).content()
            -1"""
    @overload
    def content(self) -> Any:
        """Polynomial_integer_dense_flint.content(self) -> Integer

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 474)

        Return the greatest common divisor of the coefficients of this
        polynomial. The sign is the sign of the leading coefficient.  The
        content of the zero polynomial is zero.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ)
            sage: (2*x^2 - 4*x^4 + 14*x^7).content()
            2
            sage: x.content()
            1
            sage: R(1).content()
            1
            sage: R(0).content()
            0

        TESTS::

            sage: t = x^2+x+1
            sage: t.content()
            1
            sage: (123456789123456789123456789123456789123456789*t).content()
            123456789123456789123456789123456789123456789

        Verify that :issue:`13053` has been resolved::

            sage: R(-1).content()
            -1"""
    @overload
    def content(self) -> Any:
        """Polynomial_integer_dense_flint.content(self) -> Integer

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 474)

        Return the greatest common divisor of the coefficients of this
        polynomial. The sign is the sign of the leading coefficient.  The
        content of the zero polynomial is zero.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ)
            sage: (2*x^2 - 4*x^4 + 14*x^7).content()
            2
            sage: x.content()
            1
            sage: R(1).content()
            1
            sage: R(0).content()
            0

        TESTS::

            sage: t = x^2+x+1
            sage: t.content()
            1
            sage: (123456789123456789123456789123456789123456789*t).content()
            123456789123456789123456789123456789123456789

        Verify that :issue:`13053` has been resolved::

            sage: R(-1).content()
            -1"""
    @overload
    def content(self) -> Any:
        """Polynomial_integer_dense_flint.content(self) -> Integer

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 474)

        Return the greatest common divisor of the coefficients of this
        polynomial. The sign is the sign of the leading coefficient.  The
        content of the zero polynomial is zero.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ)
            sage: (2*x^2 - 4*x^4 + 14*x^7).content()
            2
            sage: x.content()
            1
            sage: R(1).content()
            1
            sage: R(0).content()
            0

        TESTS::

            sage: t = x^2+x+1
            sage: t.content()
            1
            sage: (123456789123456789123456789123456789123456789*t).content()
            123456789123456789123456789123456789123456789

        Verify that :issue:`13053` has been resolved::

            sage: R(-1).content()
            -1"""
    @overload
    def content(self) -> Any:
        """Polynomial_integer_dense_flint.content(self) -> Integer

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 474)

        Return the greatest common divisor of the coefficients of this
        polynomial. The sign is the sign of the leading coefficient.  The
        content of the zero polynomial is zero.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ)
            sage: (2*x^2 - 4*x^4 + 14*x^7).content()
            2
            sage: x.content()
            1
            sage: R(1).content()
            1
            sage: R(0).content()
            0

        TESTS::

            sage: t = x^2+x+1
            sage: t.content()
            1
            sage: (123456789123456789123456789123456789123456789*t).content()
            123456789123456789123456789123456789123456789

        Verify that :issue:`13053` has been resolved::

            sage: R(-1).content()
            -1"""
    @overload
    def degree(self, gen=...) -> Any:
        """Polynomial_integer_dense_flint.degree(self, gen=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 1376)

        Return the degree of this polynomial.

        The zero polynomial has degree `-1`.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ)
            sage: x.degree()
            1
            sage: (x^2).degree()
            2
            sage: R(1).degree()
            0
            sage: R(0).degree()
            -1

        TESTS::

            sage: type(x.degree())
            <class 'sage.rings.integer.Integer'>"""
    @overload
    def degree(self) -> Any:
        """Polynomial_integer_dense_flint.degree(self, gen=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 1376)

        Return the degree of this polynomial.

        The zero polynomial has degree `-1`.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ)
            sage: x.degree()
            1
            sage: (x^2).degree()
            2
            sage: R(1).degree()
            0
            sage: R(0).degree()
            -1

        TESTS::

            sage: type(x.degree())
            <class 'sage.rings.integer.Integer'>"""
    @overload
    def degree(self) -> Any:
        """Polynomial_integer_dense_flint.degree(self, gen=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 1376)

        Return the degree of this polynomial.

        The zero polynomial has degree `-1`.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ)
            sage: x.degree()
            1
            sage: (x^2).degree()
            2
            sage: R(1).degree()
            0
            sage: R(0).degree()
            -1

        TESTS::

            sage: type(x.degree())
            <class 'sage.rings.integer.Integer'>"""
    @overload
    def degree(self) -> Any:
        """Polynomial_integer_dense_flint.degree(self, gen=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 1376)

        Return the degree of this polynomial.

        The zero polynomial has degree `-1`.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ)
            sage: x.degree()
            1
            sage: (x^2).degree()
            2
            sage: R(1).degree()
            0
            sage: R(0).degree()
            -1

        TESTS::

            sage: type(x.degree())
            <class 'sage.rings.integer.Integer'>"""
    @overload
    def degree(self) -> Any:
        """Polynomial_integer_dense_flint.degree(self, gen=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 1376)

        Return the degree of this polynomial.

        The zero polynomial has degree `-1`.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ)
            sage: x.degree()
            1
            sage: (x^2).degree()
            2
            sage: R(1).degree()
            0
            sage: R(0).degree()
            -1

        TESTS::

            sage: type(x.degree())
            <class 'sage.rings.integer.Integer'>"""
    @overload
    def degree(self) -> Any:
        """Polynomial_integer_dense_flint.degree(self, gen=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 1376)

        Return the degree of this polynomial.

        The zero polynomial has degree `-1`.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ)
            sage: x.degree()
            1
            sage: (x^2).degree()
            2
            sage: R(1).degree()
            0
            sage: R(0).degree()
            -1

        TESTS::

            sage: type(x.degree())
            <class 'sage.rings.integer.Integer'>"""
    def disc(self, *args, **kwargs):
        """Polynomial_integer_dense_flint.discriminant(self, proof=True)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 1437)

        Return the discriminant of ``self``, which is by definition

        .. MATH::

            (-1)^{m(m-1)/2} \\mathop{\\mathrm{resultant}}(a, a')/\\mathop{\\mathrm{lc}}(a),

        where `m = \\mathop{\\mathrm{deg}}(a)`, and `\\mathop{\\mathrm{lc}}(a)` is
        the leading coefficient of a. If ``proof`` is False (the default is
        True), then this function may use a randomized strategy that errors
        with probability no more than `2^{-80}`.

        EXAMPLES::

            sage: R.<x> = ZZ[]
            sage: f = 3*x^3 + 2*x + 1
            sage: f.discriminant()
            -339
            sage: f.discriminant(proof=False)
            -339

        TESTS:

        Confirm that :issue:`17603` has been applied::

            sage: f.disc()
            -339"""
    def discriminant(self, proof=...) -> Any:
        """Polynomial_integer_dense_flint.discriminant(self, proof=True)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 1437)

        Return the discriminant of ``self``, which is by definition

        .. MATH::

            (-1)^{m(m-1)/2} \\mathop{\\mathrm{resultant}}(a, a')/\\mathop{\\mathrm{lc}}(a),

        where `m = \\mathop{\\mathrm{deg}}(a)`, and `\\mathop{\\mathrm{lc}}(a)` is
        the leading coefficient of a. If ``proof`` is False (the default is
        True), then this function may use a randomized strategy that errors
        with probability no more than `2^{-80}`.

        EXAMPLES::

            sage: R.<x> = ZZ[]
            sage: f = 3*x^3 + 2*x + 1
            sage: f.discriminant()
            -339
            sage: f.discriminant(proof=False)
            -339

        TESTS:

        Confirm that :issue:`17603` has been applied::

            sage: f.disc()
            -339"""
    def factor(self) -> Any:
        """Polynomial_integer_dense_flint.factor(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 1619)

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
        """Polynomial_integer_dense_flint.factor_mod(self, p)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 1654)

        Return the factorization of ``self`` modulo the prime `p`.

        INPUT:

        - ``p`` -- prime

        OUTPUT: factorization of ``self`` reduced modulo `p`

        EXAMPLES::

            sage: R.<x> = ZZ['x']
            sage: f = -3*x*(x-2)*(x-9) + x
            sage: f.factor_mod(3)
            x
            sage: f = -3 * x * (x - 2) * (x - 9)
            sage: f.factor_mod(3)
            Traceback (most recent call last):
            ...
            ArithmeticError: factorization of 0 is not defined

            sage: f = 2 * x * (x - 2) * (x - 9)
            sage: f.factor_mod(7)
            (2) * x * (x + 5)^2"""
    def factor_padic(self, p, prec=...) -> Any:
        """Polynomial_integer_dense_flint.factor_padic(self, p, prec=10)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 1692)

        Return `p`-adic factorization of ``self`` to given precision.

        INPUT:

        - ``p`` -- prime

        - ``prec`` -- integer; the precision

        OUTPUT: factorization of ``self`` over the completion at `p`

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ)
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
        """Polynomial_integer_dense_flint.gcd(self, right)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 808)

        Return the GCD of ``self`` and ``right``.  The leading
        coefficient need not be 1.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ)
            sage: f = (6*x + 47) * (7*x^2 - 2*x + 38)
            sage: g = (6*x + 47) * (3*x^3 + 2*x + 1)
            sage: f.gcd(g)
            6*x + 47"""
    @overload
    def gcd(self, g) -> Any:
        """Polynomial_integer_dense_flint.gcd(self, right)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 808)

        Return the GCD of ``self`` and ``right``.  The leading
        coefficient need not be 1.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ)
            sage: f = (6*x + 47) * (7*x^2 - 2*x + 38)
            sage: g = (6*x + 47) * (3*x^3 + 2*x + 1)
            sage: f.gcd(g)
            6*x + 47"""
    def inverse_series_trunc(self, longprec) -> Polynomial:
        """Polynomial_integer_dense_flint.inverse_series_trunc(self, long prec) -> Polynomial

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 1261)

        Return a polynomial approximation of precision ``prec`` of the inverse
        series of this polynomial.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: p = 1 + x + 2*x^2
            sage: q5 = p.inverse_series_trunc(5)
            sage: q5
            -x^4 + 3*x^3 - x^2 - x + 1
            sage: p*q5
            -2*x^6 + 5*x^5 + 1

            sage: (x-1).inverse_series_trunc(5)
            -x^4 - x^3 - x^2 - x - 1

            sage: q100 = p.inverse_series_trunc(100)
            sage: (q100 * p).truncate(100)
            1

        TESTS::

            sage: ZZ['x'].zero().inverse_series_trunc(4)
            Traceback (most recent call last):
            ...
            ValueError: constant term is zero
            sage: ZZ['x'](2).inverse_series_trunc(4)
            Traceback (most recent call last):
            ...
            ValueError: constant term 2 is not a unit
            sage: x = polygen(ZZ)
            sage: (x+1).inverse_series_trunc(0)
            Traceback (most recent call last):
            ...
            ValueError: the precision must be positive, got 0"""
    @overload
    def is_one(self) -> bool:
        """Polynomial_integer_dense_flint.is_one(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 776)

        Return ``True`` if ``self`` is equal to one.

        EXAMPLES::

            sage: R.<x> = ZZ[]
            sage: R(0).is_one()
            False
            sage: R(1).is_one()
            True
            sage: x.is_one()
            False"""
    @overload
    def is_one(self) -> Any:
        """Polynomial_integer_dense_flint.is_one(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 776)

        Return ``True`` if ``self`` is equal to one.

        EXAMPLES::

            sage: R.<x> = ZZ[]
            sage: R(0).is_one()
            False
            sage: R(1).is_one()
            True
            sage: x.is_one()
            False"""
    @overload
    def is_one(self) -> Any:
        """Polynomial_integer_dense_flint.is_one(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 776)

        Return ``True`` if ``self`` is equal to one.

        EXAMPLES::

            sage: R.<x> = ZZ[]
            sage: R(0).is_one()
            False
            sage: R(1).is_one()
            True
            sage: x.is_one()
            False"""
    @overload
    def is_one(self) -> Any:
        """Polynomial_integer_dense_flint.is_one(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 776)

        Return ``True`` if ``self`` is equal to one.

        EXAMPLES::

            sage: R.<x> = ZZ[]
            sage: R(0).is_one()
            False
            sage: R(1).is_one()
            True
            sage: x.is_one()
            False"""
    @overload
    def is_zero(self) -> bool:
        """Polynomial_integer_dense_flint.is_zero(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 760)

        Return ``True`` if ``self`` is equal to zero.

        EXAMPLES::

            sage: R.<x> = ZZ[]
            sage: R(0).is_zero()
            True
            sage: R(1).is_zero()
            False
            sage: x.is_zero()
            False"""
    @overload
    def is_zero(self) -> Any:
        """Polynomial_integer_dense_flint.is_zero(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 760)

        Return ``True`` if ``self`` is equal to zero.

        EXAMPLES::

            sage: R.<x> = ZZ[]
            sage: R(0).is_zero()
            True
            sage: R(1).is_zero()
            False
            sage: x.is_zero()
            False"""
    @overload
    def is_zero(self) -> Any:
        """Polynomial_integer_dense_flint.is_zero(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 760)

        Return ``True`` if ``self`` is equal to zero.

        EXAMPLES::

            sage: R.<x> = ZZ[]
            sage: R(0).is_zero()
            True
            sage: R(1).is_zero()
            False
            sage: x.is_zero()
            False"""
    @overload
    def is_zero(self) -> Any:
        """Polynomial_integer_dense_flint.is_zero(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 760)

        Return ``True`` if ``self`` is equal to zero.

        EXAMPLES::

            sage: R.<x> = ZZ[]
            sage: R(0).is_zero()
            True
            sage: R(1).is_zero()
            False
            sage: x.is_zero()
            False"""
    @overload
    def lcm(self, right) -> Any:
        """Polynomial_integer_dense_flint.lcm(self, right)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 834)

        Return the LCM of ``self`` and ``right``.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ)
            sage: f = (6*x + 47) * (7*x^2 - 2*x + 38)
            sage: g = (6*x + 47) * (3*x^3 + 2*x + 1)
            sage: h = f.lcm(g); h
            126*x^6 + 951*x^5 + 486*x^4 + 6034*x^3 + 585*x^2 + 3706*x + 1786
            sage: h == (6*x + 47) * (7*x^2 - 2*x + 38) * (3*x^3 + 2*x + 1)
            True

        TESTS:

        Check that :issue:`32033` has been fixed::

            sage: R.<t> = ZZ[]
            sage: lcm(R(0), R(0))
            0"""
    @overload
    def lcm(self, g) -> Any:
        """Polynomial_integer_dense_flint.lcm(self, right)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 834)

        Return the LCM of ``self`` and ``right``.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ)
            sage: f = (6*x + 47) * (7*x^2 - 2*x + 38)
            sage: g = (6*x + 47) * (3*x^3 + 2*x + 1)
            sage: h = f.lcm(g); h
            126*x^6 + 951*x^5 + 486*x^4 + 6034*x^3 + 585*x^2 + 3706*x + 1786
            sage: h == (6*x + 47) * (7*x^2 - 2*x + 38) * (3*x^3 + 2*x + 1)
            True

        TESTS:

        Check that :issue:`32033` has been fixed::

            sage: R.<t> = ZZ[]
            sage: lcm(R(0), R(0))
            0"""
    @overload
    def list(self, boolcopy=...) -> list:
        """Polynomial_integer_dense_flint.list(self, bool copy=True) -> list

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 1734)

        Return a new copy of the list of the underlying
        elements of ``self``.

        EXAMPLES::

            sage: x = PolynomialRing(ZZ,'x').0
            sage: f = x^3 + 3*x - 17
            sage: f.list()
            [-17, 3, 0, 1]
            sage: f = PolynomialRing(ZZ,'x')(0)
            sage: f.list()
            []"""
    @overload
    def list(self) -> Any:
        """Polynomial_integer_dense_flint.list(self, bool copy=True) -> list

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 1734)

        Return a new copy of the list of the underlying
        elements of ``self``.

        EXAMPLES::

            sage: x = PolynomialRing(ZZ,'x').0
            sage: f = x^3 + 3*x - 17
            sage: f.list()
            [-17, 3, 0, 1]
            sage: f = PolynomialRing(ZZ,'x')(0)
            sage: f.list()
            []"""
    @overload
    def list(self) -> Any:
        """Polynomial_integer_dense_flint.list(self, bool copy=True) -> list

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 1734)

        Return a new copy of the list of the underlying
        elements of ``self``.

        EXAMPLES::

            sage: x = PolynomialRing(ZZ,'x').0
            sage: f = x^3 + 3*x - 17
            sage: f.list()
            [-17, 3, 0, 1]
            sage: f = PolynomialRing(ZZ,'x')(0)
            sage: f.list()
            []"""
    def pseudo_divrem(self, B) -> Any:
        """Polynomial_integer_dense_flint.pseudo_divrem(self, B)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 1401)

        Write ``A = self``.  This function computes polynomials `Q` and `R`
        and an integer `d` such that

        .. MATH::

             \\mathop{\\mathrm{lead}}(B)^d A = B Q + R

        where R has degree less than that of B.

        INPUT:

        - ``B`` -- a polynomial over `\\ZZ`

        OUTPUT:

        - ``Q``, ``R`` -- polynomials
        - ``d`` -- nonnegative integer

        EXAMPLES::

            sage: R.<x> = ZZ['x']
            sage: A = R(range(10))
            sage: B = 3*R([-1, 0, 1])
            sage: Q, R, d = A.pseudo_divrem(B)
            sage: Q, R, d
            (9*x^7 + 8*x^6 + 16*x^5 + 14*x^4 + 21*x^3 + 18*x^2 + 24*x + 20, 75*x + 60, 1)
            sage: B.leading_coefficient()^d * A == B*Q + R
            True"""
    @overload
    def quo_rem(self, Polynomial_integer_dense_flintright) -> Any:
        """Polynomial_integer_dense_flint.quo_rem(self, Polynomial_integer_dense_flint right)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 690)

        Attempts to divide ``self`` by ``right``, and return a quotient and remainder.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ)
            sage: f = R(range(10)); g = R([-1, 0, 1])
            sage: q, r = f.quo_rem(g)
            sage: q, r
            (9*x^7 + 8*x^6 + 16*x^5 + 14*x^4 + 21*x^3 + 18*x^2 + 24*x + 20, 25*x + 20)
            sage: q*g + r == f
            True

            sage: f = x^2
            sage: f.quo_rem(0)
            Traceback (most recent call last):
            ...
            ZeroDivisionError: division by zero polynomial

            sage: f = (x^2 + 3) * (2*x - 1)
            sage: f.quo_rem(2*x - 1)
            (x^2 + 3, 0)

            sage: f = x^2
            sage: f.quo_rem(2*x - 1)
            (0, x^2)

        TESTS::

            sage: z = R(0)
            sage: z.quo_rem(1)
            (0, 0)
            sage: z.quo_rem(x)
            (0, 0)
            sage: z.quo_rem(2*x)
            (0, 0)

        :issue:`383`, make sure things get coerced correctly::

            sage: f = x+1; parent(f)
            Univariate Polynomial Ring in x over Integer Ring
            sage: g = x/2; parent(g)
            Univariate Polynomial Ring in x over Rational Field
            sage: f.quo_rem(g)
            (2, 1)
            sage: g.quo_rem(f)
            (1/2, -1/2)
            sage: parent(f.quo_rem(g)[0])
            Univariate Polynomial Ring in x over Rational Field
            sage: f.quo_rem(3)
            (0, x + 1)
            sage: (5*x+7).quo_rem(3)
            (x + 2, 2*x + 1)"""
    @overload
    def quo_rem(self, g) -> Any:
        """Polynomial_integer_dense_flint.quo_rem(self, Polynomial_integer_dense_flint right)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 690)

        Attempts to divide ``self`` by ``right``, and return a quotient and remainder.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ)
            sage: f = R(range(10)); g = R([-1, 0, 1])
            sage: q, r = f.quo_rem(g)
            sage: q, r
            (9*x^7 + 8*x^6 + 16*x^5 + 14*x^4 + 21*x^3 + 18*x^2 + 24*x + 20, 25*x + 20)
            sage: q*g + r == f
            True

            sage: f = x^2
            sage: f.quo_rem(0)
            Traceback (most recent call last):
            ...
            ZeroDivisionError: division by zero polynomial

            sage: f = (x^2 + 3) * (2*x - 1)
            sage: f.quo_rem(2*x - 1)
            (x^2 + 3, 0)

            sage: f = x^2
            sage: f.quo_rem(2*x - 1)
            (0, x^2)

        TESTS::

            sage: z = R(0)
            sage: z.quo_rem(1)
            (0, 0)
            sage: z.quo_rem(x)
            (0, 0)
            sage: z.quo_rem(2*x)
            (0, 0)

        :issue:`383`, make sure things get coerced correctly::

            sage: f = x+1; parent(f)
            Univariate Polynomial Ring in x over Integer Ring
            sage: g = x/2; parent(g)
            Univariate Polynomial Ring in x over Rational Field
            sage: f.quo_rem(g)
            (2, 1)
            sage: g.quo_rem(f)
            (1/2, -1/2)
            sage: parent(f.quo_rem(g)[0])
            Univariate Polynomial Ring in x over Rational Field
            sage: f.quo_rem(3)
            (0, x + 1)
            sage: (5*x+7).quo_rem(3)
            (x + 2, 2*x + 1)"""
    @overload
    def quo_rem(self, x) -> Any:
        """Polynomial_integer_dense_flint.quo_rem(self, Polynomial_integer_dense_flint right)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 690)

        Attempts to divide ``self`` by ``right``, and return a quotient and remainder.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ)
            sage: f = R(range(10)); g = R([-1, 0, 1])
            sage: q, r = f.quo_rem(g)
            sage: q, r
            (9*x^7 + 8*x^6 + 16*x^5 + 14*x^4 + 21*x^3 + 18*x^2 + 24*x + 20, 25*x + 20)
            sage: q*g + r == f
            True

            sage: f = x^2
            sage: f.quo_rem(0)
            Traceback (most recent call last):
            ...
            ZeroDivisionError: division by zero polynomial

            sage: f = (x^2 + 3) * (2*x - 1)
            sage: f.quo_rem(2*x - 1)
            (x^2 + 3, 0)

            sage: f = x^2
            sage: f.quo_rem(2*x - 1)
            (0, x^2)

        TESTS::

            sage: z = R(0)
            sage: z.quo_rem(1)
            (0, 0)
            sage: z.quo_rem(x)
            (0, 0)
            sage: z.quo_rem(2*x)
            (0, 0)

        :issue:`383`, make sure things get coerced correctly::

            sage: f = x+1; parent(f)
            Univariate Polynomial Ring in x over Integer Ring
            sage: g = x/2; parent(g)
            Univariate Polynomial Ring in x over Rational Field
            sage: f.quo_rem(g)
            (2, 1)
            sage: g.quo_rem(f)
            (1/2, -1/2)
            sage: parent(f.quo_rem(g)[0])
            Univariate Polynomial Ring in x over Rational Field
            sage: f.quo_rem(3)
            (0, x + 1)
            sage: (5*x+7).quo_rem(3)
            (x + 2, 2*x + 1)"""
    @overload
    def quo_rem(self, g) -> Any:
        """Polynomial_integer_dense_flint.quo_rem(self, Polynomial_integer_dense_flint right)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 690)

        Attempts to divide ``self`` by ``right``, and return a quotient and remainder.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ)
            sage: f = R(range(10)); g = R([-1, 0, 1])
            sage: q, r = f.quo_rem(g)
            sage: q, r
            (9*x^7 + 8*x^6 + 16*x^5 + 14*x^4 + 21*x^3 + 18*x^2 + 24*x + 20, 25*x + 20)
            sage: q*g + r == f
            True

            sage: f = x^2
            sage: f.quo_rem(0)
            Traceback (most recent call last):
            ...
            ZeroDivisionError: division by zero polynomial

            sage: f = (x^2 + 3) * (2*x - 1)
            sage: f.quo_rem(2*x - 1)
            (x^2 + 3, 0)

            sage: f = x^2
            sage: f.quo_rem(2*x - 1)
            (0, x^2)

        TESTS::

            sage: z = R(0)
            sage: z.quo_rem(1)
            (0, 0)
            sage: z.quo_rem(x)
            (0, 0)
            sage: z.quo_rem(2*x)
            (0, 0)

        :issue:`383`, make sure things get coerced correctly::

            sage: f = x+1; parent(f)
            Univariate Polynomial Ring in x over Integer Ring
            sage: g = x/2; parent(g)
            Univariate Polynomial Ring in x over Rational Field
            sage: f.quo_rem(g)
            (2, 1)
            sage: g.quo_rem(f)
            (1/2, -1/2)
            sage: parent(f.quo_rem(g)[0])
            Univariate Polynomial Ring in x over Rational Field
            sage: f.quo_rem(3)
            (0, x + 1)
            sage: (5*x+7).quo_rem(3)
            (x + 2, 2*x + 1)"""
    @overload
    def quo_rem(self, f) -> Any:
        """Polynomial_integer_dense_flint.quo_rem(self, Polynomial_integer_dense_flint right)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 690)

        Attempts to divide ``self`` by ``right``, and return a quotient and remainder.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ)
            sage: f = R(range(10)); g = R([-1, 0, 1])
            sage: q, r = f.quo_rem(g)
            sage: q, r
            (9*x^7 + 8*x^6 + 16*x^5 + 14*x^4 + 21*x^3 + 18*x^2 + 24*x + 20, 25*x + 20)
            sage: q*g + r == f
            True

            sage: f = x^2
            sage: f.quo_rem(0)
            Traceback (most recent call last):
            ...
            ZeroDivisionError: division by zero polynomial

            sage: f = (x^2 + 3) * (2*x - 1)
            sage: f.quo_rem(2*x - 1)
            (x^2 + 3, 0)

            sage: f = x^2
            sage: f.quo_rem(2*x - 1)
            (0, x^2)

        TESTS::

            sage: z = R(0)
            sage: z.quo_rem(1)
            (0, 0)
            sage: z.quo_rem(x)
            (0, 0)
            sage: z.quo_rem(2*x)
            (0, 0)

        :issue:`383`, make sure things get coerced correctly::

            sage: f = x+1; parent(f)
            Univariate Polynomial Ring in x over Integer Ring
            sage: g = x/2; parent(g)
            Univariate Polynomial Ring in x over Rational Field
            sage: f.quo_rem(g)
            (2, 1)
            sage: g.quo_rem(f)
            (1/2, -1/2)
            sage: parent(f.quo_rem(g)[0])
            Univariate Polynomial Ring in x over Rational Field
            sage: f.quo_rem(3)
            (0, x + 1)
            sage: (5*x+7).quo_rem(3)
            (x + 2, 2*x + 1)"""
    @overload
    def quo_rem(self, g) -> Any:
        """Polynomial_integer_dense_flint.quo_rem(self, Polynomial_integer_dense_flint right)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 690)

        Attempts to divide ``self`` by ``right``, and return a quotient and remainder.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ)
            sage: f = R(range(10)); g = R([-1, 0, 1])
            sage: q, r = f.quo_rem(g)
            sage: q, r
            (9*x^7 + 8*x^6 + 16*x^5 + 14*x^4 + 21*x^3 + 18*x^2 + 24*x + 20, 25*x + 20)
            sage: q*g + r == f
            True

            sage: f = x^2
            sage: f.quo_rem(0)
            Traceback (most recent call last):
            ...
            ZeroDivisionError: division by zero polynomial

            sage: f = (x^2 + 3) * (2*x - 1)
            sage: f.quo_rem(2*x - 1)
            (x^2 + 3, 0)

            sage: f = x^2
            sage: f.quo_rem(2*x - 1)
            (0, x^2)

        TESTS::

            sage: z = R(0)
            sage: z.quo_rem(1)
            (0, 0)
            sage: z.quo_rem(x)
            (0, 0)
            sage: z.quo_rem(2*x)
            (0, 0)

        :issue:`383`, make sure things get coerced correctly::

            sage: f = x+1; parent(f)
            Univariate Polynomial Ring in x over Integer Ring
            sage: g = x/2; parent(g)
            Univariate Polynomial Ring in x over Rational Field
            sage: f.quo_rem(g)
            (2, 1)
            sage: g.quo_rem(f)
            (1/2, -1/2)
            sage: parent(f.quo_rem(g)[0])
            Univariate Polynomial Ring in x over Rational Field
            sage: f.quo_rem(3)
            (0, x + 1)
            sage: (5*x+7).quo_rem(3)
            (x + 2, 2*x + 1)"""
    @overload
    def real_root_intervals(self) -> Any:
        """Polynomial_integer_dense_flint.real_root_intervals(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 1352)

        Return isolating intervals for the real roots of this
        polynomial.

        EXAMPLES:
        We compute the roots of the characteristic polynomial of some
        Salem numbers::

            sage: R.<x> = PolynomialRing(ZZ)
            sage: f = 1 - x^2 - x^3 - x^4 + x^6
            sage: f.real_root_intervals()                                               # needs sage.libs.linbox
            [((1/2, 3/4), 1), ((1, 3/2), 1)]"""
    @overload
    def real_root_intervals(self) -> Any:
        """Polynomial_integer_dense_flint.real_root_intervals(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 1352)

        Return isolating intervals for the real roots of this
        polynomial.

        EXAMPLES:
        We compute the roots of the characteristic polynomial of some
        Salem numbers::

            sage: R.<x> = PolynomialRing(ZZ)
            sage: f = 1 - x^2 - x^3 - x^4 + x^6
            sage: f.real_root_intervals()                                               # needs sage.libs.linbox
            [((1/2, 3/4), 1), ((1, 3/2), 1)]"""
    @overload
    def resultant(self, other, proof=...) -> Any:
        """Polynomial_integer_dense_flint.resultant(self, other, proof=True)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 1751)

        Return the resultant of ``self`` and ``other``, which must lie in the same
        polynomial ring.

        If ``proof=False`` (the default is ``proof=True``), then this function may
        use a randomized strategy that errors with probability no more than
        `2^{-80}`.

        INPUT:

        - ``other`` -- a polynomial

        OUTPUT: an element of the base ring of the polynomial ring

        EXAMPLES::

            sage: x = PolynomialRing(ZZ,'x').0
            sage: f = x^3 + x + 1;  g = x^3 - x - 1
            sage: r = f.resultant(g); r
            -8
            sage: r.parent() is ZZ
            True"""
    @overload
    def resultant(self, g) -> Any:
        """Polynomial_integer_dense_flint.resultant(self, other, proof=True)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 1751)

        Return the resultant of ``self`` and ``other``, which must lie in the same
        polynomial ring.

        If ``proof=False`` (the default is ``proof=True``), then this function may
        use a randomized strategy that errors with probability no more than
        `2^{-80}`.

        INPUT:

        - ``other`` -- a polynomial

        OUTPUT: an element of the base ring of the polynomial ring

        EXAMPLES::

            sage: x = PolynomialRing(ZZ,'x').0
            sage: f = x^3 + x + 1;  g = x^3 - x - 1
            sage: r = f.resultant(g); r
            -8
            sage: r.parent() is ZZ
            True"""
    @overload
    def reverse(self, degree=...) -> Any:
        """Polynomial_integer_dense_flint.reverse(self, degree=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 1793)

        Return a polynomial with the coefficients of this polynomial reversed.

        If an optional degree argument is given the coefficient list will be
        truncated or zero padded as necessary before computing the reverse.

        EXAMPLES::

            sage: R.<x> = ZZ[]
            sage: p = R([1,2,3,4]); p
            4*x^3 + 3*x^2 + 2*x + 1
            sage: p.reverse()
            x^3 + 2*x^2 + 3*x + 4
            sage: p.reverse(degree=6)
            x^6 + 2*x^5 + 3*x^4 + 4*x^3
            sage: p.reverse(degree=2)
            x^2 + 2*x + 3

        TESTS::

            sage: p.reverse(degree=1.5r)
            Traceback (most recent call last):
            ...
            ValueError: degree argument must be a nonnegative integer, got 1.5

        Check that this implementation is compatible with the generic one::

            sage: p = R([0,1,0,2])
            sage: all(p.reverse(d) == Polynomial.reverse(p, d)
            ....:     for d in [None, 0, 1, 2, 3, 4])
            True"""
    @overload
    def reverse(self) -> Any:
        """Polynomial_integer_dense_flint.reverse(self, degree=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 1793)

        Return a polynomial with the coefficients of this polynomial reversed.

        If an optional degree argument is given the coefficient list will be
        truncated or zero padded as necessary before computing the reverse.

        EXAMPLES::

            sage: R.<x> = ZZ[]
            sage: p = R([1,2,3,4]); p
            4*x^3 + 3*x^2 + 2*x + 1
            sage: p.reverse()
            x^3 + 2*x^2 + 3*x + 4
            sage: p.reverse(degree=6)
            x^6 + 2*x^5 + 3*x^4 + 4*x^3
            sage: p.reverse(degree=2)
            x^2 + 2*x + 3

        TESTS::

            sage: p.reverse(degree=1.5r)
            Traceback (most recent call last):
            ...
            ValueError: degree argument must be a nonnegative integer, got 1.5

        Check that this implementation is compatible with the generic one::

            sage: p = R([0,1,0,2])
            sage: all(p.reverse(d) == Polynomial.reverse(p, d)
            ....:     for d in [None, 0, 1, 2, 3, 4])
            True"""
    @overload
    def reverse(self, degree=...) -> Any:
        """Polynomial_integer_dense_flint.reverse(self, degree=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 1793)

        Return a polynomial with the coefficients of this polynomial reversed.

        If an optional degree argument is given the coefficient list will be
        truncated or zero padded as necessary before computing the reverse.

        EXAMPLES::

            sage: R.<x> = ZZ[]
            sage: p = R([1,2,3,4]); p
            4*x^3 + 3*x^2 + 2*x + 1
            sage: p.reverse()
            x^3 + 2*x^2 + 3*x + 4
            sage: p.reverse(degree=6)
            x^6 + 2*x^5 + 3*x^4 + 4*x^3
            sage: p.reverse(degree=2)
            x^2 + 2*x + 3

        TESTS::

            sage: p.reverse(degree=1.5r)
            Traceback (most recent call last):
            ...
            ValueError: degree argument must be a nonnegative integer, got 1.5

        Check that this implementation is compatible with the generic one::

            sage: p = R([0,1,0,2])
            sage: all(p.reverse(d) == Polynomial.reverse(p, d)
            ....:     for d in [None, 0, 1, 2, 3, 4])
            True"""
    @overload
    def reverse(self, degree=...) -> Any:
        """Polynomial_integer_dense_flint.reverse(self, degree=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 1793)

        Return a polynomial with the coefficients of this polynomial reversed.

        If an optional degree argument is given the coefficient list will be
        truncated or zero padded as necessary before computing the reverse.

        EXAMPLES::

            sage: R.<x> = ZZ[]
            sage: p = R([1,2,3,4]); p
            4*x^3 + 3*x^2 + 2*x + 1
            sage: p.reverse()
            x^3 + 2*x^2 + 3*x + 4
            sage: p.reverse(degree=6)
            x^6 + 2*x^5 + 3*x^4 + 4*x^3
            sage: p.reverse(degree=2)
            x^2 + 2*x + 3

        TESTS::

            sage: p.reverse(degree=1.5r)
            Traceback (most recent call last):
            ...
            ValueError: degree argument must be a nonnegative integer, got 1.5

        Check that this implementation is compatible with the generic one::

            sage: p = R([0,1,0,2])
            sage: all(p.reverse(d) == Polynomial.reverse(p, d)
            ....:     for d in [None, 0, 1, 2, 3, 4])
            True"""
    @overload
    def reverse(self, degree=...) -> Any:
        """Polynomial_integer_dense_flint.reverse(self, degree=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 1793)

        Return a polynomial with the coefficients of this polynomial reversed.

        If an optional degree argument is given the coefficient list will be
        truncated or zero padded as necessary before computing the reverse.

        EXAMPLES::

            sage: R.<x> = ZZ[]
            sage: p = R([1,2,3,4]); p
            4*x^3 + 3*x^2 + 2*x + 1
            sage: p.reverse()
            x^3 + 2*x^2 + 3*x + 4
            sage: p.reverse(degree=6)
            x^6 + 2*x^5 + 3*x^4 + 4*x^3
            sage: p.reverse(degree=2)
            x^2 + 2*x + 3

        TESTS::

            sage: p.reverse(degree=1.5r)
            Traceback (most recent call last):
            ...
            ValueError: degree argument must be a nonnegative integer, got 1.5

        Check that this implementation is compatible with the generic one::

            sage: p = R([0,1,0,2])
            sage: all(p.reverse(d) == Polynomial.reverse(p, d)
            ....:     for d in [None, 0, 1, 2, 3, 4])
            True"""
    def revert_series(self, n) -> Any:
        """Polynomial_integer_dense_flint.revert_series(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 1841)

        Return a polynomial `f` such that `f(` ``self`` `(x)) =` ``self`` `(f(x)) = x` (mod `x^n`).

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: f = t - t^3 + t^5
            sage: f.revert_series(6)
            2*t^5 + t^3 + t

            sage: f.revert_series(-1)
            Traceback (most recent call last):
            ...
            ValueError: argument n must be a nonnegative integer, got -1

            sage: g = - t^3 + t^5
            sage: g.revert_series(6)
            Traceback (most recent call last):
            ...
            ValueError: self must have constant coefficient 0 and a unit for coefficient t^1"""
    @overload
    def squarefree_decomposition(self) -> Any:
        """Polynomial_integer_dense_flint.squarefree_decomposition(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 1495)

        Return the square-free decomposition of ``self``.  This is
        a partial factorization of ``self`` into square-free, relatively
        prime polynomials.

        This is a wrapper for the NTL function ``SquareFreeDecomp``.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ)
            sage: p = (x-1)^2 * (x-2)^2 * (x-3)^3 * (x-4)
            sage: p.squarefree_decomposition()
            (x - 4) * (x^2 - 3*x + 2)^2 * (x - 3)^3
            sage: p = 37 * (x-1)^2 * (x-2)^2 * (x-3)^3 * (x-4)
            sage: p.squarefree_decomposition()
            (37) * (x - 4) * (x^2 - 3*x + 2)^2 * (x - 3)^3

        TESTS:

        Verify that :issue:`13053` has been resolved::

            sage: R.<x> = PolynomialRing(ZZ, implementation='FLINT')
            sage: f=-x^2
            sage: f.squarefree_decomposition()
            (-1) * x^2"""
    @overload
    def squarefree_decomposition(self) -> Any:
        """Polynomial_integer_dense_flint.squarefree_decomposition(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 1495)

        Return the square-free decomposition of ``self``.  This is
        a partial factorization of ``self`` into square-free, relatively
        prime polynomials.

        This is a wrapper for the NTL function ``SquareFreeDecomp``.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ)
            sage: p = (x-1)^2 * (x-2)^2 * (x-3)^3 * (x-4)
            sage: p.squarefree_decomposition()
            (x - 4) * (x^2 - 3*x + 2)^2 * (x - 3)^3
            sage: p = 37 * (x-1)^2 * (x-2)^2 * (x-3)^3 * (x-4)
            sage: p.squarefree_decomposition()
            (37) * (x - 4) * (x^2 - 3*x + 2)^2 * (x - 3)^3

        TESTS:

        Verify that :issue:`13053` has been resolved::

            sage: R.<x> = PolynomialRing(ZZ, implementation='FLINT')
            sage: f=-x^2
            sage: f.squarefree_decomposition()
            (-1) * x^2"""
    @overload
    def squarefree_decomposition(self) -> Any:
        """Polynomial_integer_dense_flint.squarefree_decomposition(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 1495)

        Return the square-free decomposition of ``self``.  This is
        a partial factorization of ``self`` into square-free, relatively
        prime polynomials.

        This is a wrapper for the NTL function ``SquareFreeDecomp``.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ)
            sage: p = (x-1)^2 * (x-2)^2 * (x-3)^3 * (x-4)
            sage: p.squarefree_decomposition()
            (x - 4) * (x^2 - 3*x + 2)^2 * (x - 3)^3
            sage: p = 37 * (x-1)^2 * (x-2)^2 * (x-3)^3 * (x-4)
            sage: p.squarefree_decomposition()
            (37) * (x - 4) * (x^2 - 3*x + 2)^2 * (x - 3)^3

        TESTS:

        Verify that :issue:`13053` has been resolved::

            sage: R.<x> = PolynomialRing(ZZ, implementation='FLINT')
            sage: f=-x^2
            sage: f.squarefree_decomposition()
            (-1) * x^2"""
    @overload
    def squarefree_decomposition(self) -> Any:
        """Polynomial_integer_dense_flint.squarefree_decomposition(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 1495)

        Return the square-free decomposition of ``self``.  This is
        a partial factorization of ``self`` into square-free, relatively
        prime polynomials.

        This is a wrapper for the NTL function ``SquareFreeDecomp``.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ)
            sage: p = (x-1)^2 * (x-2)^2 * (x-3)^3 * (x-4)
            sage: p.squarefree_decomposition()
            (x - 4) * (x^2 - 3*x + 2)^2 * (x - 3)^3
            sage: p = 37 * (x-1)^2 * (x-2)^2 * (x-3)^3 * (x-4)
            sage: p.squarefree_decomposition()
            (37) * (x - 4) * (x^2 - 3*x + 2)^2 * (x - 3)^3

        TESTS:

        Verify that :issue:`13053` has been resolved::

            sage: R.<x> = PolynomialRing(ZZ, implementation='FLINT')
            sage: f=-x^2
            sage: f.squarefree_decomposition()
            (-1) * x^2"""
    def xgcd(self, right) -> Any:
        """Polynomial_integer_dense_flint.xgcd(self, right)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 863)

        Return a triple `(g,s,t)` such that `g = s\\cdot{}` ``self`` + `t\\cdot{}` ``right`` and such
        that `g` is the gcd of ``self`` and ``right`` up to a divisor of the
        resultant of ``self`` and ``other``.

        As integer polynomials do not form a principal ideal domain, it is not
        always possible given `a` and `b` to find a pair `s,t` such that
        `gcd(a,b) = sa + tb`. Take `a=x+2` and `b=x+4` as an example for which the
        gcd is `1` but the best you can achieve in the Bezout identity is `2`.

        If ``self`` and ``right`` are coprime as polynomials over the
        rationals, then ``g`` is guaranteed to be the resultant of
        ``self`` and ``right``, as a constant polynomial.

        EXAMPLES::

            sage: P.<x> = PolynomialRing(ZZ)

            sage: (x + 2).xgcd(x + 4)
            (2, -1, 1)
            sage: (x + 2).resultant(x + 4)
            2
            sage: (x + 2).gcd(x + 4)
            1

            sage: F = (x^2 + 2)*x^3; G = (x^2 + 2) * (x - 3)
            sage: g, u, v = F.xgcd(G)
            sage: g, u, v
            (27*x^2 + 54, 1, -x^2 - 3*x - 9)
            sage: u*F + v*G
            27*x^2 + 54

            sage: zero = P(0)
            sage: x.xgcd(zero)
            (x, 1, 0)
            sage: zero.xgcd(x)
            (x, 0, 1)

            sage: F = (x - 3)^3; G = (x - 15)^2
            sage: g, u, v = F.xgcd(G)
            sage: g, u, v
            (2985984, -432*x + 8208, 432*x^2 + 864*x + 14256)
            sage: u*F + v*G
            2985984

        TESTS:

        Check that :issue:`17675` is fixed::

            sage: R.<x> = ZZ['x']
            sage: R(2).xgcd(R(2))
            (2, 0, 1)
            sage: R.zero().xgcd(R(2))
            (2, 0, 1)
            sage: R(2).xgcd(R.zero())
            (2, 1, 0)"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __call__(self, *x, **kwds) -> Any:
        """Polynomial_integer_dense_flint.__call__(self, *x, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 363)

        Call this polynomial with the given parameters, which can be
        interpreted as polynomial composition or evaluation by this
        method.

        If the argument is not simply an integer (``int`` or
        ``Integer``) a real number (``RealNumber``) a real interval
        (``RealIntervalFieldElement``) or a polynomial (of the same type as
        ``self``), the call is passed on to the generic implementation in the
        ``Polynomial`` class.

        EXAMPLES:

        The first example illustrates polynomial composition::

            sage: R.<t> = ZZ[]
            sage: f = t^2 - 1
            sage: g = t + 1
            sage: f(g)          # indirect doctest
            t^2 + 2*t

        Now we illustrate how a polynomial can be evaluated at an
        integer::

            sage: f(2)          # indirect doctest
            3

        TESTS:

            sage: t(-sys.maxsize-1r) == t(-sys.maxsize-1)
            True
            sage: (t^2+3)(RealBallField(100)(1/3))
            [3.1111111111111111111111111111...]
            sage: (t^2+3)(ComplexBallField(10)(i))                                      # needs sage.symbolic
            2.00"""
    def __floordiv__(self, Polynomial_integer_dense_flintself, right) -> Any:
        """Polynomial_integer_dense_flint.__floordiv__(Polynomial_integer_dense_flint self, right)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 1199)

        EXAMPLES::

            sage: R.<x> = ZZ[]
            sage: (x^2+1)//x
            x
            sage: (5*x^2+1)//(2*x)
            2*x

        Divide by a scalar.

        ::

            sage: (5*x^3 + 5*x + 10)//5
            x^3 + x + 2

        TESTS::

            sage: x//0
            Traceback (most recent call last):
            ...
            ZeroDivisionError: division by zero

            sage: (x^2 + 13*x + 169) // 13
            x + 13"""
    @overload
    def __pari__(self, variable=...) -> Any:
        '''Polynomial_integer_dense_flint.__pari__(self, variable=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 1480)

        EXAMPLES::

            sage: t = PolynomialRing(ZZ,"t").gen()
            sage: f = t^3 + 3*t - 17
            sage: pari(f)
            t^3 + 3*t - 17
            sage: f.__pari__(variable=\'y\')
            y^3 + 3*y - 17'''
    @overload
    def __pari__(self, variable=...) -> Any:
        '''Polynomial_integer_dense_flint.__pari__(self, variable=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 1480)

        EXAMPLES::

            sage: t = PolynomialRing(ZZ,"t").gen()
            sage: f = t^3 + 3*t - 17
            sage: pari(f)
            t^3 + 3*t - 17
            sage: f.__pari__(variable=\'y\')
            y^3 + 3*y - 17'''
    def __pow__(self, Polynomial_integer_dense_flintself, exp, mod) -> Any:
        """Polynomial_integer_dense_flint.__pow__(Polynomial_integer_dense_flint self, exp, mod)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 1038)

        EXAMPLES::

            sage: R.<x> = ZZ[]
            sage: r = 2*x + 2
            sage: r^0
            1
            sage: r^2
            4*x^2 + 8*x + 4
            sage: r^-2
            1/(4*x^2 + 8*x + 4)

            sage: x^(2^20)
            x^1048576

        TESTS::

            sage: z = R(0)
            sage: z^0
            1
            sage: z^1
            0
            sage: z^-1
            Traceback (most recent call last):
            ...
            ZeroDivisionError: negative exponent in power of zero

        Check that :issue:`18278` is fixed::

            sage: R.<x> = ZZ[]
            sage: x^(1/2)
            Traceback (most recent call last):
            ...
            ValueError: not a 2nd power

            sage: x^(2^100)
            Traceback (most recent call last):
            ...
            OverflowError: Sage Integer too large to convert to C long

        Test fractional powers (:issue:`20086`)::

            sage: P.<R> = ZZ[]
            sage: (R^3 + 6*R^2 + 12*R + 8)^(1/3)
            R + 2
            sage: _.parent()
            Univariate Polynomial Ring in R over Integer Ring
            sage: P(4)^(1/2)
            2
            sage: _.parent()
            Univariate Polynomial Ring in R over Integer Ring

            sage: (R^2 + 3)^(1/2)
            Traceback (most recent call last):
            ...
            ValueError: 3 is not a 2nd power

            Ring in R over Integer Ring
            sage: P(2)^P(2)
            Traceback (most recent call last):
            ...
            TypeError: no canonical coercion from Univariate Polynomial
            Ring in R over Integer Ring to Rational Field
            sage: (R + 1)^P(2)
            Traceback (most recent call last):
            ...
            TypeError: no canonical coercion from Univariate Polynomial
            Ring in R over Integer Ring to Rational Field
            sage: (R + 1)^R
            Traceback (most recent call last):
            ...
            TypeError: no canonical coercion from Univariate Polynomial
            Ring in R over Integer Ring to Rational Field
            sage: 2^R
            Traceback (most recent call last):
            ...
            TypeError: no canonical coercion from Univariate Polynomial
            Ring in R over Integer Ring to Rational Field

        Check that using third argument raises an error::

            sage: R.<x> = PolynomialRing(ZZ, implementation='FLINT')
            sage: pow(x, 2, x)
            Traceback (most recent call last):
            ...
            NotImplementedError: pow() with a modulus is not implemented for this ring"""
    def __reduce__(self) -> Any:
        """Polynomial_integer_dense_flint.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx (starting at line 520)

        Used for pickling.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ)
            sage: loads(dumps(x)) == x
            True
            sage: f = 2*x + 3
            sage: loads(dumps(f)) == f
            True"""
    def __rfloordiv__(self, other):
        """Return value//self."""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
