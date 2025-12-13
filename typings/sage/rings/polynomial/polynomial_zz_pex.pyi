import _cython_3_2_1
import sage.rings.polynomial.polynomial_element
from sage.rings.fraction_field_element import FractionFieldElement as FractionFieldElement
from sage.structure.element import canonical_coercion as canonical_coercion, coerce_binop as coerce_binop, have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

make_element: _cython_3_2_1.cython_function_or_method

class Polynomial_ZZ_pEX(Polynomial_template):
    """Polynomial_ZZ_pEX(parent, x=None, check=True, is_gen=False, construct=False)

    File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zz_pex.pyx (starting at line 68)

    Univariate Polynomials over `\\GF{p^n}` via NTL's ``ZZ_pEX``.

    EXAMPLES::

        sage: K.<a> = GF(next_prime(2**60)**3)
        sage: R.<x> = PolynomialRing(K, implementation='NTL')
        sage: (x^3 + a*x^2 + 1) * (x + a)
        x^4 + 2*a*x^3 + a^2*x^2 + x + a"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, x=..., check=..., is_gen=..., construct=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zz_pex.pyx (starting at line 79)

                Create a new univariate polynomials over `\\GF{p^n}`.

                EXAMPLES::

                    sage: K.<a> = GF(next_prime(2**60)**3)
                    sage: R.<x> = PolynomialRing(K, implementation='NTL')
                    sage: x^2+a
                    x^2 + a

                TESTS:

                The following tests against a bug that was fixed in :issue:`9944`.
                With the ring definition above, we now have::

                    sage: R([3,'1234'])
                    1234*x + 3
                    sage: R([3,'12e34'])
                    Traceback (most recent call last):
                    ...
                    TypeError: unable to convert '12e34' to an integer
                    sage: R([3,x])
                    Traceback (most recent call last):
                    ...
                    TypeError: x is not a constant polynomial

                Check that NTL contexts are correctly restored and that
                :issue:`9524` has been fixed::

                    sage: x = polygen(GF(9, 'a'))
                    sage: x = polygen(GF(49, 'a'))
                    sage: -x
                    6*x
                    sage: 5*x
                    5*x

                Check that :issue:`11239` is fixed::

                    sage: Fq.<a> = GF(2^4); Fqq.<b> = GF(3^7)
                    sage: PFq.<x> = Fq[]; PFqq.<y> = Fqq[]
                    sage: f = x^3 + (a^3 + 1)*x
                    sage: sage.rings.polynomial.polynomial_zz_pex.Polynomial_ZZ_pEX(PFqq, f)
                    Traceback (most recent call last):
                    ...
                    TypeError: unable to coerce from a finite field other than the prime subfield
        """
    def compose_mod(self, other, modulus) -> Any:
        """Polynomial_ZZ_pEX.compose_mod(self, other, modulus)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zz_pex.pyx (starting at line 715)

        Compute `f(g) \\bmod h`.

        To be precise about the order fo compostion, given ``self``, ``other``
        and ``modulus`` as `f(x)`, `g(x)` and `h(x)` compute `f(g(x)) \\bmod h(x)`.

        INPUT:

        - ``other`` -- a polynomial `g(x)`
        - ``modulus`` -- a polynomial `h(x)`

        EXAMPLES::

            sage: R.<x> = GF(3**6)[]
            sage: f = R.random_element()
            sage: g = R.random_element()
            sage: g.compose_mod(g, f) == g(g) % f
            True

            sage: F.<z3> = GF(3**6)
            sage: R.<x> = F[]
            sage: f = 2*z3^2*x^2 + (z3 + 1)*x + z3^2 + 2
            sage: g = (z3^2 + 2*z3)*x^2 + (2*z3 + 2)*x + 2*z3^2 + z3 + 2
            sage: h = (2*z3 + 2)*x^2 + (2*z3^2 + 1)*x + 2*z3^2 + z3 + 2
            sage: f.compose_mod(g, h)
            (z3^5 + z3^4 + z3^3 + z3^2 + z3)*x + z3^5 + z3^3 + 2*z3 + 2
            sage: f.compose_mod(g, h) == f(g) % h
            True

        AUTHORS:

        - Giacomo Pope (2024-08) initial implementation"""
    def inverse_series_trunc(self, prec) -> Any:
        """Polynomial_ZZ_pEX.inverse_series_trunc(self, prec)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zz_pex.pyx (starting at line 552)

        Compute and return the inverse of ``self`` modulo `x^{prec}`.

        The constant term of ``self`` must be invertible.

        EXAMPLES::

            sage: R.<x> = GF(101^2)[]
            sage: z2 =  R.base_ring().gen()
            sage: f = (3*z2 + 57)*x^3 + (13*z2 + 94)*x^2 + (7*z2 + 2)*x + 66*z2 + 15
            sage: f.inverse_series_trunc(1)
            51*z2 + 92
            sage: f.inverse_series_trunc(2)
            (30*z2 + 30)*x + 51*z2 + 92
            sage: f.inverse_series_trunc(3)
            (42*z2 + 94)*x^2 + (30*z2 + 30)*x + 51*z2 + 92
            sage: f.inverse_series_trunc(4)
            (99*z2 + 96)*x^3 + (42*z2 + 94)*x^2 + (30*z2 + 30)*x + 51*z2 + 92

        TESTS::

            sage: R.<x> = GF(163^2)[]
            sage: f = R([p for p in primes(20)])
            sage: f.inverse_series_trunc(1)
            82
            sage: f.inverse_series_trunc(2)
            40*x + 82
            sage: f.inverse_series_trunc(3)
            61*x^2 + 40*x + 82
            sage: f.inverse_series_trunc(0)
            Traceback (most recent call last):
            ...
            ValueError: the precision must be positive, got 0
            sage: f.inverse_series_trunc(-1)
            Traceback (most recent call last):
            ...
            ValueError: the precision must be positive, got -1
            sage: f = x + x^2 + x^3
            sage: f.inverse_series_trunc(5)
            Traceback (most recent call last):
            ...
            ValueError: constant term 0 is not a unit"""
    def is_irreducible(self, algorithm=..., iter=...) -> Any:
        """Polynomial_ZZ_pEX.is_irreducible(self, algorithm='fast_when_false', iter=1)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zz_pex.pyx (starting at line 320)

        Return ``True`` precisely when ``self`` is irreducible over its base ring.

        INPUT:

        - ``algorithm`` -- string (default: ``'fast_when_false'``);
          there are 3 available algorithms:
          ``'fast_when_true'``, ``'fast_when_false'``, and ``'probabilistic'``

        - ``iter`` -- (default: 1) if the algorithm is ``'probabilistic'``,
          defines the number of iterations. The error probability is bounded
          by `q^{\\text{-iter}}` for polynomials in `\\GF{q}[x]`.

        EXAMPLES::

            sage: K.<a> = GF(next_prime(2**60)**3)
            sage: R.<x> = PolynomialRing(K, implementation='NTL')
            sage: P = x^3 + (2-a)*x + 1
            sage: P.is_irreducible(algorithm='fast_when_false')
            True
            sage: P.is_irreducible(algorithm='fast_when_true')
            True
            sage: P.is_irreducible(algorithm='probabilistic')
            True
            sage: Q = (x^2+a)*(x+a^3)
            sage: Q.is_irreducible(algorithm='fast_when_false')
            False
            sage: Q.is_irreducible(algorithm='fast_when_true')
            False
            sage: Q.is_irreducible(algorithm='probabilistic')
            False"""
    @overload
    def list(self, boolcopy=...) -> list:
        """Polynomial_ZZ_pEX.list(self, bool copy=True) -> list

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zz_pex.pyx (starting at line 181)

        Return the list of coefficients.

        EXAMPLES::

            sage: K.<a> = GF(5^3)
            sage: P = PolynomialRing(K, 'x')
            sage: f = P.random_element(100)
            sage: f.list() == [f[i] for i in range(f.degree()+1)]
            True
            sage: P.0.list()
            [0, 1]"""
    @overload
    def list(self) -> Any:
        """Polynomial_ZZ_pEX.list(self, bool copy=True) -> list

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zz_pex.pyx (starting at line 181)

        Return the list of coefficients.

        EXAMPLES::

            sage: K.<a> = GF(5^3)
            sage: P = PolynomialRing(K, 'x')
            sage: f = P.random_element(100)
            sage: f.list() == [f[i] for i in range(f.degree()+1)]
            True
            sage: P.0.list()
            [0, 1]"""
    @overload
    def list(self) -> Any:
        """Polynomial_ZZ_pEX.list(self, bool copy=True) -> list

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zz_pex.pyx (starting at line 181)

        Return the list of coefficients.

        EXAMPLES::

            sage: K.<a> = GF(5^3)
            sage: P = PolynomialRing(K, 'x')
            sage: f = P.random_element(100)
            sage: f.list() == [f[i] for i in range(f.degree()+1)]
            True
            sage: P.0.list()
            [0, 1]"""
    @overload
    def minpoly_mod(self, other) -> Any:
        """Polynomial_ZZ_pEX.minpoly_mod(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zz_pex.pyx (starting at line 370)

        Compute the minimal polynomial of this polynomial modulo another
        polynomial in the same ring.

        ALGORITHM:

        NTL's ``MinPolyMod()``, which uses Shoup's algorithm [Sho1999]_.

        EXAMPLES::

            sage: R.<x> = GF(101^2)[]
            sage: f = x^17 + x^2 - 1
            sage: (x^2).minpoly_mod(f)
            x^17 + 100*x^2 + 2*x + 100

        TESTS:

        Random testing::

            sage: p = random_prime(50)
            sage: e = randrange(2,10)
            sage: R.<x> = GF((p,e),'a')[]
            sage: d = randrange(1,50)
            sage: f = R.random_element(d)
            sage: g = R.random_element((-1,5*d))
            sage: poly = g.minpoly_mod(f)
            sage: poly(R.quotient(f)(g))
            0"""
    @overload
    def minpoly_mod(self, f) -> Any:
        """Polynomial_ZZ_pEX.minpoly_mod(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zz_pex.pyx (starting at line 370)

        Compute the minimal polynomial of this polynomial modulo another
        polynomial in the same ring.

        ALGORITHM:

        NTL's ``MinPolyMod()``, which uses Shoup's algorithm [Sho1999]_.

        EXAMPLES::

            sage: R.<x> = GF(101^2)[]
            sage: f = x^17 + x^2 - 1
            sage: (x^2).minpoly_mod(f)
            x^17 + 100*x^2 + 2*x + 100

        TESTS:

        Random testing::

            sage: p = random_prime(50)
            sage: e = randrange(2,10)
            sage: R.<x> = GF((p,e),'a')[]
            sage: d = randrange(1,50)
            sage: f = R.random_element(d)
            sage: g = R.random_element((-1,5*d))
            sage: poly = g.minpoly_mod(f)
            sage: poly(R.quotient(f)(g))
            0"""
    @overload
    def minpoly_mod(self, f) -> Any:
        """Polynomial_ZZ_pEX.minpoly_mod(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zz_pex.pyx (starting at line 370)

        Compute the minimal polynomial of this polynomial modulo another
        polynomial in the same ring.

        ALGORITHM:

        NTL's ``MinPolyMod()``, which uses Shoup's algorithm [Sho1999]_.

        EXAMPLES::

            sage: R.<x> = GF(101^2)[]
            sage: f = x^17 + x^2 - 1
            sage: (x^2).minpoly_mod(f)
            x^17 + 100*x^2 + 2*x + 100

        TESTS:

        Random testing::

            sage: p = random_prime(50)
            sage: e = randrange(2,10)
            sage: R.<x> = GF((p,e),'a')[]
            sage: d = randrange(1,50)
            sage: f = R.random_element(d)
            sage: g = R.random_element((-1,5*d))
            sage: poly = g.minpoly_mod(f)
            sage: poly(R.quotient(f)(g))
            0"""
    def modular_composition(self, *args, **kwargs):
        """Polynomial_ZZ_pEX.compose_mod(self, other, modulus)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zz_pex.pyx (starting at line 715)

        Compute `f(g) \\bmod h`.

        To be precise about the order fo compostion, given ``self``, ``other``
        and ``modulus`` as `f(x)`, `g(x)` and `h(x)` compute `f(g(x)) \\bmod h(x)`.

        INPUT:

        - ``other`` -- a polynomial `g(x)`
        - ``modulus`` -- a polynomial `h(x)`

        EXAMPLES::

            sage: R.<x> = GF(3**6)[]
            sage: f = R.random_element()
            sage: g = R.random_element()
            sage: g.compose_mod(g, f) == g(g) % f
            True

            sage: F.<z3> = GF(3**6)
            sage: R.<x> = F[]
            sage: f = 2*z3^2*x^2 + (z3 + 1)*x + z3^2 + 2
            sage: g = (z3^2 + 2*z3)*x^2 + (2*z3 + 2)*x + 2*z3^2 + z3 + 2
            sage: h = (2*z3 + 2)*x^2 + (2*z3^2 + 1)*x + 2*z3^2 + z3 + 2
            sage: f.compose_mod(g, h)
            (z3^5 + z3^4 + z3^3 + z3^2 + z3)*x + z3^5 + z3^3 + 2*z3 + 2
            sage: f.compose_mod(g, h) == f(g) % h
            True

        AUTHORS:

        - Giacomo Pope (2024-08) initial implementation"""
    @overload
    def resultant(self, other) -> Any:
        """Polynomial_ZZ_pEX.resultant(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zz_pex.pyx (starting at line 288)

        Return the resultant of ``self`` and ``other``, which must lie in the same
        polynomial ring.

        INPUT:

        - ``other`` -- a polynomial

        OUTPUT: an element of the base ring of the polynomial ring

        EXAMPLES::

            sage: K.<a> = GF(next_prime(2**60)**3)
            sage: R.<x> = PolynomialRing(K, implementation='NTL')
            sage: f = (x-a)*(x-a**2)*(x+1)
            sage: g = (x-a**3)*(x-a**4)*(x+a)
            sage: r = f.resultant(g)
            sage: r == prod(u - v for (u,eu) in f.roots() for (v,ev) in g.roots())
            True"""
    @overload
    def resultant(self, g) -> Any:
        """Polynomial_ZZ_pEX.resultant(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zz_pex.pyx (starting at line 288)

        Return the resultant of ``self`` and ``other``, which must lie in the same
        polynomial ring.

        INPUT:

        - ``other`` -- a polynomial

        OUTPUT: an element of the base ring of the polynomial ring

        EXAMPLES::

            sage: K.<a> = GF(next_prime(2**60)**3)
            sage: R.<x> = PolynomialRing(K, implementation='NTL')
            sage: f = (x-a)*(x-a**2)*(x+1)
            sage: g = (x-a**3)*(x-a**4)*(x+a)
            sage: r = f.resultant(g)
            sage: r == prod(u - v for (u,eu) in f.roots() for (v,ev) in g.roots())
            True"""
    @overload
    def reverse(self, degree=...) -> Any:
        """Polynomial_ZZ_pEX.reverse(self, degree=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zz_pex.pyx (starting at line 491)

        Return the polynomial obtained by reversing the coefficients
        of this polynomial.  If degree is set then this function behaves
        as if this polynomial has degree ``degree``.

        EXAMPLES::

            sage: R.<x> = GF(101^2)[]
            sage: f = x^13 + 11*x^10 + 32*x^6 + 4
            sage: f.reverse()
            4*x^13 + 32*x^7 + 11*x^3 + 1
            sage: f.reverse(degree=15)
            4*x^15 + 32*x^9 + 11*x^5 + x^2
            sage: f.reverse(degree=2)
            4*x^2

        TESTS::

            sage: R.<x> = GF(163^2)[]
            sage: f = R([p for p in primes(20)])
            sage: f.reverse()
            2*x^7 + 3*x^6 + 5*x^5 + 7*x^4 + 11*x^3 + 13*x^2 + 17*x + 19
            sage: f.reverse(degree=200)
            2*x^200 + 3*x^199 + 5*x^198 + 7*x^197 + 11*x^196 + 13*x^195 + 17*x^194 + 19*x^193
            sage: f.reverse(degree=0)
            2
            sage: f.reverse(degree=-5)
            Traceback (most recent call last):
            ...
            ValueError: degree argument must be a nonnegative integer, got -5

        Check that this implementation is compatible with the generic one::

            sage: p = R([0,1,0,2])
            sage: all(p.reverse(d) == Polynomial.reverse(p, d)
            ....:     for d in [None, 0, 1, 2, 3, 4])
            True"""
    @overload
    def reverse(self) -> Any:
        """Polynomial_ZZ_pEX.reverse(self, degree=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zz_pex.pyx (starting at line 491)

        Return the polynomial obtained by reversing the coefficients
        of this polynomial.  If degree is set then this function behaves
        as if this polynomial has degree ``degree``.

        EXAMPLES::

            sage: R.<x> = GF(101^2)[]
            sage: f = x^13 + 11*x^10 + 32*x^6 + 4
            sage: f.reverse()
            4*x^13 + 32*x^7 + 11*x^3 + 1
            sage: f.reverse(degree=15)
            4*x^15 + 32*x^9 + 11*x^5 + x^2
            sage: f.reverse(degree=2)
            4*x^2

        TESTS::

            sage: R.<x> = GF(163^2)[]
            sage: f = R([p for p in primes(20)])
            sage: f.reverse()
            2*x^7 + 3*x^6 + 5*x^5 + 7*x^4 + 11*x^3 + 13*x^2 + 17*x + 19
            sage: f.reverse(degree=200)
            2*x^200 + 3*x^199 + 5*x^198 + 7*x^197 + 11*x^196 + 13*x^195 + 17*x^194 + 19*x^193
            sage: f.reverse(degree=0)
            2
            sage: f.reverse(degree=-5)
            Traceback (most recent call last):
            ...
            ValueError: degree argument must be a nonnegative integer, got -5

        Check that this implementation is compatible with the generic one::

            sage: p = R([0,1,0,2])
            sage: all(p.reverse(d) == Polynomial.reverse(p, d)
            ....:     for d in [None, 0, 1, 2, 3, 4])
            True"""
    @overload
    def reverse(self, degree=...) -> Any:
        """Polynomial_ZZ_pEX.reverse(self, degree=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zz_pex.pyx (starting at line 491)

        Return the polynomial obtained by reversing the coefficients
        of this polynomial.  If degree is set then this function behaves
        as if this polynomial has degree ``degree``.

        EXAMPLES::

            sage: R.<x> = GF(101^2)[]
            sage: f = x^13 + 11*x^10 + 32*x^6 + 4
            sage: f.reverse()
            4*x^13 + 32*x^7 + 11*x^3 + 1
            sage: f.reverse(degree=15)
            4*x^15 + 32*x^9 + 11*x^5 + x^2
            sage: f.reverse(degree=2)
            4*x^2

        TESTS::

            sage: R.<x> = GF(163^2)[]
            sage: f = R([p for p in primes(20)])
            sage: f.reverse()
            2*x^7 + 3*x^6 + 5*x^5 + 7*x^4 + 11*x^3 + 13*x^2 + 17*x + 19
            sage: f.reverse(degree=200)
            2*x^200 + 3*x^199 + 5*x^198 + 7*x^197 + 11*x^196 + 13*x^195 + 17*x^194 + 19*x^193
            sage: f.reverse(degree=0)
            2
            sage: f.reverse(degree=-5)
            Traceback (most recent call last):
            ...
            ValueError: degree argument must be a nonnegative integer, got -5

        Check that this implementation is compatible with the generic one::

            sage: p = R([0,1,0,2])
            sage: all(p.reverse(d) == Polynomial.reverse(p, d)
            ....:     for d in [None, 0, 1, 2, 3, 4])
            True"""
    @overload
    def reverse(self, degree=...) -> Any:
        """Polynomial_ZZ_pEX.reverse(self, degree=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zz_pex.pyx (starting at line 491)

        Return the polynomial obtained by reversing the coefficients
        of this polynomial.  If degree is set then this function behaves
        as if this polynomial has degree ``degree``.

        EXAMPLES::

            sage: R.<x> = GF(101^2)[]
            sage: f = x^13 + 11*x^10 + 32*x^6 + 4
            sage: f.reverse()
            4*x^13 + 32*x^7 + 11*x^3 + 1
            sage: f.reverse(degree=15)
            4*x^15 + 32*x^9 + 11*x^5 + x^2
            sage: f.reverse(degree=2)
            4*x^2

        TESTS::

            sage: R.<x> = GF(163^2)[]
            sage: f = R([p for p in primes(20)])
            sage: f.reverse()
            2*x^7 + 3*x^6 + 5*x^5 + 7*x^4 + 11*x^3 + 13*x^2 + 17*x + 19
            sage: f.reverse(degree=200)
            2*x^200 + 3*x^199 + 5*x^198 + 7*x^197 + 11*x^196 + 13*x^195 + 17*x^194 + 19*x^193
            sage: f.reverse(degree=0)
            2
            sage: f.reverse(degree=-5)
            Traceback (most recent call last):
            ...
            ValueError: degree argument must be a nonnegative integer, got -5

        Check that this implementation is compatible with the generic one::

            sage: p = R([0,1,0,2])
            sage: all(p.reverse(d) == Polynomial.reverse(p, d)
            ....:     for d in [None, 0, 1, 2, 3, 4])
            True"""
    @overload
    def reverse(self) -> Any:
        """Polynomial_ZZ_pEX.reverse(self, degree=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zz_pex.pyx (starting at line 491)

        Return the polynomial obtained by reversing the coefficients
        of this polynomial.  If degree is set then this function behaves
        as if this polynomial has degree ``degree``.

        EXAMPLES::

            sage: R.<x> = GF(101^2)[]
            sage: f = x^13 + 11*x^10 + 32*x^6 + 4
            sage: f.reverse()
            4*x^13 + 32*x^7 + 11*x^3 + 1
            sage: f.reverse(degree=15)
            4*x^15 + 32*x^9 + 11*x^5 + x^2
            sage: f.reverse(degree=2)
            4*x^2

        TESTS::

            sage: R.<x> = GF(163^2)[]
            sage: f = R([p for p in primes(20)])
            sage: f.reverse()
            2*x^7 + 3*x^6 + 5*x^5 + 7*x^4 + 11*x^3 + 13*x^2 + 17*x + 19
            sage: f.reverse(degree=200)
            2*x^200 + 3*x^199 + 5*x^198 + 7*x^197 + 11*x^196 + 13*x^195 + 17*x^194 + 19*x^193
            sage: f.reverse(degree=0)
            2
            sage: f.reverse(degree=-5)
            Traceback (most recent call last):
            ...
            ValueError: degree argument must be a nonnegative integer, got -5

        Check that this implementation is compatible with the generic one::

            sage: p = R([0,1,0,2])
            sage: all(p.reverse(d) == Polynomial.reverse(p, d)
            ....:     for d in [None, 0, 1, 2, 3, 4])
            True"""
    @overload
    def reverse(self, degree=...) -> Any:
        """Polynomial_ZZ_pEX.reverse(self, degree=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zz_pex.pyx (starting at line 491)

        Return the polynomial obtained by reversing the coefficients
        of this polynomial.  If degree is set then this function behaves
        as if this polynomial has degree ``degree``.

        EXAMPLES::

            sage: R.<x> = GF(101^2)[]
            sage: f = x^13 + 11*x^10 + 32*x^6 + 4
            sage: f.reverse()
            4*x^13 + 32*x^7 + 11*x^3 + 1
            sage: f.reverse(degree=15)
            4*x^15 + 32*x^9 + 11*x^5 + x^2
            sage: f.reverse(degree=2)
            4*x^2

        TESTS::

            sage: R.<x> = GF(163^2)[]
            sage: f = R([p for p in primes(20)])
            sage: f.reverse()
            2*x^7 + 3*x^6 + 5*x^5 + 7*x^4 + 11*x^3 + 13*x^2 + 17*x + 19
            sage: f.reverse(degree=200)
            2*x^200 + 3*x^199 + 5*x^198 + 7*x^197 + 11*x^196 + 13*x^195 + 17*x^194 + 19*x^193
            sage: f.reverse(degree=0)
            2
            sage: f.reverse(degree=-5)
            Traceback (most recent call last):
            ...
            ValueError: degree argument must be a nonnegative integer, got -5

        Check that this implementation is compatible with the generic one::

            sage: p = R([0,1,0,2])
            sage: all(p.reverse(d) == Polynomial.reverse(p, d)
            ....:     for d in [None, 0, 1, 2, 3, 4])
            True"""
    @overload
    def reverse(self, degree=...) -> Any:
        """Polynomial_ZZ_pEX.reverse(self, degree=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zz_pex.pyx (starting at line 491)

        Return the polynomial obtained by reversing the coefficients
        of this polynomial.  If degree is set then this function behaves
        as if this polynomial has degree ``degree``.

        EXAMPLES::

            sage: R.<x> = GF(101^2)[]
            sage: f = x^13 + 11*x^10 + 32*x^6 + 4
            sage: f.reverse()
            4*x^13 + 32*x^7 + 11*x^3 + 1
            sage: f.reverse(degree=15)
            4*x^15 + 32*x^9 + 11*x^5 + x^2
            sage: f.reverse(degree=2)
            4*x^2

        TESTS::

            sage: R.<x> = GF(163^2)[]
            sage: f = R([p for p in primes(20)])
            sage: f.reverse()
            2*x^7 + 3*x^6 + 5*x^5 + 7*x^4 + 11*x^3 + 13*x^2 + 17*x + 19
            sage: f.reverse(degree=200)
            2*x^200 + 3*x^199 + 5*x^198 + 7*x^197 + 11*x^196 + 13*x^195 + 17*x^194 + 19*x^193
            sage: f.reverse(degree=0)
            2
            sage: f.reverse(degree=-5)
            Traceback (most recent call last):
            ...
            ValueError: degree argument must be a nonnegative integer, got -5

        Check that this implementation is compatible with the generic one::

            sage: p = R([0,1,0,2])
            sage: all(p.reverse(d) == Polynomial.reverse(p, d)
            ....:     for d in [None, 0, 1, 2, 3, 4])
            True"""
    @overload
    def reverse(self, degree=...) -> Any:
        """Polynomial_ZZ_pEX.reverse(self, degree=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zz_pex.pyx (starting at line 491)

        Return the polynomial obtained by reversing the coefficients
        of this polynomial.  If degree is set then this function behaves
        as if this polynomial has degree ``degree``.

        EXAMPLES::

            sage: R.<x> = GF(101^2)[]
            sage: f = x^13 + 11*x^10 + 32*x^6 + 4
            sage: f.reverse()
            4*x^13 + 32*x^7 + 11*x^3 + 1
            sage: f.reverse(degree=15)
            4*x^15 + 32*x^9 + 11*x^5 + x^2
            sage: f.reverse(degree=2)
            4*x^2

        TESTS::

            sage: R.<x> = GF(163^2)[]
            sage: f = R([p for p in primes(20)])
            sage: f.reverse()
            2*x^7 + 3*x^6 + 5*x^5 + 7*x^4 + 11*x^3 + 13*x^2 + 17*x + 19
            sage: f.reverse(degree=200)
            2*x^200 + 3*x^199 + 5*x^198 + 7*x^197 + 11*x^196 + 13*x^195 + 17*x^194 + 19*x^193
            sage: f.reverse(degree=0)
            2
            sage: f.reverse(degree=-5)
            Traceback (most recent call last):
            ...
            ValueError: degree argument must be a nonnegative integer, got -5

        Check that this implementation is compatible with the generic one::

            sage: p = R([0,1,0,2])
            sage: all(p.reverse(d) == Polynomial.reverse(p, d)
            ....:     for d in [None, 0, 1, 2, 3, 4])
            True"""
    def shift(self, intn) -> Any:
        """Polynomial_ZZ_pEX.shift(self, int n)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zz_pex.pyx (starting at line 442)

        EXAMPLES::

            sage: K.<a> = GF(next_prime(2**60)**3)
            sage: R.<x> = PolynomialRing(K, implementation='NTL')
            sage: f = x^3 + x^2 + 1
            sage: f.shift(1)
            x^4 + x^3 + x
            sage: f.shift(-1)
            x^2 + x"""
    def __call__(self, *x, **kwds) -> Any:
        """Polynomial_ZZ_pEX.__call__(self, *x, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zz_pex.pyx (starting at line 224)

        Evaluate polynomial at `a`.

        EXAMPLES::

            sage: K.<u> = GF(next_prime(2**60)**3)
            sage: R.<x> = PolynomialRing(K, implementation='NTL')
            sage: P = (x-u)*(x+u+1)
            sage: P(u)
            0
            sage: P(u+1)
            2*u + 2

        TESTS:

        The work around provided in :issue:`10475` is superseded by :issue:`24072`::

            sage: F.<x> = GF(4)
            sage: P.<y> = F[]
            sage: p = y^4 + x*y^3 + y^2 + (x + 1)*y + x + 1
            sage: SR(p)                                                                 # needs sage.symbolic
            Traceback (most recent call last):
            ...
            TypeError: positive characteristic not allowed in symbolic computations

        Check that polynomial evaluation works when using logarithmic
        representation of finite field elements (:issue:`16383`)::

            sage: for i in range(10):
            ....:     F = FiniteField(random_prime(15) ** ZZ.random_element(2, 5), 'a', repr='log')
            ....:     b = F.random_element()
            ....:     P = PolynomialRing(F, 'x')
            ....:     f = P.random_element(8)
            ....:     assert f(b) == sum(c * b^i for i, c in enumerate(f))"""
    def __lshift__(self, intn) -> Any:
        """Polynomial_ZZ_pEX.__lshift__(self, int n)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zz_pex.pyx (starting at line 463)

        EXAMPLES::

            sage: K.<a> = GF(next_prime(2**60)**3)
            sage: R.<x> = PolynomialRing(K, implementation='NTL')
            sage: f = x^3 + x^2 + 1
            sage: f << 1
            x^4 + x^3 + x
            sage: f << -1
            x^2 + x"""
    def __pow__(self, exp, modulus) -> Any:
        '''Polynomial_ZZ_pEX.__pow__(self, exp, modulus)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zz_pex.pyx (starting at line 621)

        Exponentiation of ``self``.

        If ``modulus`` is not ``None``, the exponentiation is performed
        modulo the polynomial ``modulus``.

        EXAMPLES::

            sage: K.<a> = GF(101^2, \'a\', modulus=[1,1,1])
            sage: R.<x> = PolynomialRing(K, implementation="NTL")
            sage: pow(x, 100)
            x^100
            sage: pow(x + 3, 5)
            x^5 + 15*x^4 + 90*x^3 + 68*x^2 + x + 41

        If modulus is not ``None``, performs modular exponentiation::

            sage: K.<a> = GF(101^2, \'a\', modulus=[1,1,1])
            sage: R.<x> = PolynomialRing(K, implementation="NTL")
            sage: pow(x, 100, x^2 + x + a)
            (19*a + 64)*x + 30*a + 2
            sage: pow(x, 100 * 101**200, x^2 + x + a)
            (19*a + 64)*x + 30*a + 2

        The modulus can have smaller degree than ``self``::

            sage: K.<a> = GF(101^2, \'a\', modulus=[1,1,1])
            sage: R.<x> = PolynomialRing(K, implementation="NTL")
            sage: pow(x^4, 25, x^2 + x + a)
            (19*a + 64)*x + 30*a + 2

        TESTS:

        Canonical coercion should apply::

            sage: xx = GF(101)["x"].gen()
            sage: pow(x+1, 25, 2)
            0
            sage: pow(x + a, 101**2, xx^3 + xx + 1)
            4*x^2 + 44*x + a + 70
            sage: pow(x + a, int(101**2), xx^3 + xx + 1)
            4*x^2 + 44*x + a + 70
            sage: xx = polygen(GF(97))
            sage: _ = pow(x + a, 101**2, xx^3 + xx + 1)
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents: ...
 '''
    def __rlshift__(self, other):
        """Return value<<self."""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
    def __rrshift__(self, other):
        """Return value>>self."""
    def __rshift__(self, intn) -> Any:
        """Polynomial_ZZ_pEX.__rshift__(self, int n)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zz_pex.pyx (starting at line 477)

        EXAMPLES::

            sage: K.<a> = GF(next_prime(2**60)**3)
            sage: R.<x> = PolynomialRing(K, implementation='NTL')
            sage: f = x^3 + x^2 + 1
            sage: f >> 1
            x^2 + x
            sage: f >> -1
            x^4 + x^3 + x"""

class Polynomial_template(sage.rings.polynomial.polynomial_element.Polynomial):
    """Polynomial_template(parent, x=None, check=True, is_gen=False, construct=False)

    File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 60)

    Template for interfacing to external C / C++ libraries for implementations of polynomials.

    AUTHORS:

    - Robert Bradshaw (2008-10): original idea for templating
    - Martin Albrecht (2008-10): initial implementation

    This file implements a simple templating engine for linking univariate
    polynomials to their C/C++ library implementations. It requires a
    'linkage' file which implements the ``celement_`` functions (see
    :mod:`sage.libs.ntl.ntl_GF2X_linkage` for an example). Both parts are
    then plugged together by inclusion of the linkage file when inheriting from
    this class. See :mod:`sage.rings.polynomial.polynomial_gf2x` for an
    example.

    We illustrate the generic glueing using univariate polynomials over
    `\\mathop{\\mathrm{GF}}(2)`.

    .. NOTE::

        Implementations using this template MUST implement coercion from base
        ring elements and :meth:`get_unsafe`. See
        :class:`~sage.rings.polynomial.polynomial_gf2x.Polynomial_GF2X` for an
        example."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, x=..., check=..., is_gen=..., construct=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 87)

                EXAMPLES::

                    sage: P.<x> = GF(2)[]
                    sage: P(0)
                    0
                    sage: P(GF(2)(1))
                    1
                    sage: P(3)
                    1
                    sage: P([1,0,1])
                    x^2 + 1
                    sage: P(list(map(GF(2),[1,0,1])))
                    x^2 + 1
        """
    @overload
    def degree(self) -> Any:
        """Polynomial_template.degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 768)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: x.degree()
            1
            sage: P(1).degree()
            0
            sage: P(0).degree()
            -1"""
    @overload
    def degree(self) -> Any:
        """Polynomial_template.degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 768)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: x.degree()
            1
            sage: P(1).degree()
            0
            sage: P(0).degree()
            -1"""
    @overload
    def degree(self) -> Any:
        """Polynomial_template.degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 768)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: x.degree()
            1
            sage: P(1).degree()
            0
            sage: P(0).degree()
            -1"""
    @overload
    def degree(self) -> Any:
        """Polynomial_template.degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 768)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: x.degree()
            1
            sage: P(1).degree()
            0
            sage: P(0).degree()
            -1"""
    @overload
    def gcd(self, Polynomial_templateother) -> Any:
        """Polynomial_template.gcd(self, Polynomial_template other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 342)

        Return the greatest common divisor of ``self`` and ``other``.

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: f = x*(x+1)
            sage: f.gcd(x+1)
            x + 1
            sage: f.gcd(x^2)
            x

        TESTS:

        Ensure non-invertible elements does not crash Sage (:issue:`37317`)::

            sage: R.<x> = Zmod(4)[]
            sage: f = R(2 * x)
            sage: f.gcd(f)
            Traceback (most recent call last):
            ...
            ValueError: leading coefficient must be invertible

        ::

            sage: f = x^2 + 3 * x + 1
            sage: g = x^2 + x + 1
            sage: f.gcd(g)
            Traceback (most recent call last):
            ...
            RuntimeError: FLINT gcd calculation failed"""
    @overload
    def gcd(self, f) -> Any:
        """Polynomial_template.gcd(self, Polynomial_template other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 342)

        Return the greatest common divisor of ``self`` and ``other``.

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: f = x*(x+1)
            sage: f.gcd(x+1)
            x + 1
            sage: f.gcd(x^2)
            x

        TESTS:

        Ensure non-invertible elements does not crash Sage (:issue:`37317`)::

            sage: R.<x> = Zmod(4)[]
            sage: f = R(2 * x)
            sage: f.gcd(f)
            Traceback (most recent call last):
            ...
            ValueError: leading coefficient must be invertible

        ::

            sage: f = x^2 + 3 * x + 1
            sage: g = x^2 + x + 1
            sage: f.gcd(g)
            Traceback (most recent call last):
            ...
            RuntimeError: FLINT gcd calculation failed"""
    @overload
    def gcd(self, g) -> Any:
        """Polynomial_template.gcd(self, Polynomial_template other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 342)

        Return the greatest common divisor of ``self`` and ``other``.

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: f = x*(x+1)
            sage: f.gcd(x+1)
            x + 1
            sage: f.gcd(x^2)
            x

        TESTS:

        Ensure non-invertible elements does not crash Sage (:issue:`37317`)::

            sage: R.<x> = Zmod(4)[]
            sage: f = R(2 * x)
            sage: f.gcd(f)
            Traceback (most recent call last):
            ...
            ValueError: leading coefficient must be invertible

        ::

            sage: f = x^2 + 3 * x + 1
            sage: g = x^2 + x + 1
            sage: f.gcd(g)
            Traceback (most recent call last):
            ...
            RuntimeError: FLINT gcd calculation failed"""
    def get_cparent(self) -> Any:
        """Polynomial_template.get_cparent(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 179)"""
    @overload
    def is_gen(self) -> Any:
        """Polynomial_template.is_gen(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 692)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: x.is_gen()
            True
            sage: (x+1).is_gen()
            False"""
    @overload
    def is_gen(self) -> Any:
        """Polynomial_template.is_gen(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 692)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: x.is_gen()
            True
            sage: (x+1).is_gen()
            False"""
    @overload
    def is_gen(self) -> Any:
        """Polynomial_template.is_gen(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 692)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: x.is_gen()
            True
            sage: (x+1).is_gen()
            False"""
    @overload
    def is_one(self) -> bool:
        """Polynomial_template.is_one(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 758)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: P(1).is_one()
            True"""
    @overload
    def is_one(self) -> Any:
        """Polynomial_template.is_one(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 758)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: P(1).is_one()
            True"""
    @overload
    def is_zero(self) -> bool:
        """Polynomial_template.is_zero(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 748)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: x.is_zero()
            False"""
    @overload
    def is_zero(self) -> Any:
        """Polynomial_template.is_zero(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 748)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: x.is_zero()
            False"""
    @overload
    def list(self, boolcopy=...) -> list:
        """Polynomial_template.list(self, bool copy=True) -> list

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 192)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: x.list()
            [0, 1]
            sage: list(x)
            [0, 1]"""
    @overload
    def list(self) -> Any:
        """Polynomial_template.list(self, bool copy=True) -> list

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 192)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: x.list()
            [0, 1]
            sage: list(x)
            [0, 1]"""
    @overload
    def list(self, x) -> Any:
        """Polynomial_template.list(self, bool copy=True) -> list

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 192)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: x.list()
            [0, 1]
            sage: list(x)
            [0, 1]"""
    def quo_rem(self, Polynomial_templateright) -> Any:
        """Polynomial_template.quo_rem(self, Polynomial_template right)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 501)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: f = x^2 + x + 1
            sage: f.quo_rem(x + 1)
            (x, 1)"""
    def shift(self, intn) -> Any:
        """Polynomial_template.shift(self, int n)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 708)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: f = x^3 + x^2 + 1
            sage: f.shift(1)
            x^4 + x^3 + x
            sage: f.shift(-1)
            x^2 + x"""
    def truncate(self, longn) -> Polynomial:
        """Polynomial_template.truncate(self, long n) -> Polynomial

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 782)

        Return this polynomial mod `x^n`.

        EXAMPLES::

            sage: R.<x> =GF(2)[]
            sage: f = sum(x^n for n in range(10)); f
            x^9 + x^8 + x^7 + x^6 + x^5 + x^4 + x^3 + x^2 + x + 1
            sage: f.truncate(6)
            x^5 + x^4 + x^3 + x^2 + x + 1

        If the precision is higher than the degree of the polynomial then
        the polynomial itself is returned::

            sage: f.truncate(10) is f
            True

        If the precision is negative, the zero polynomial is returned::

            sage: f.truncate(-1)
            0"""
    def xgcd(self, Polynomial_templateother) -> Any:
        """Polynomial_template.xgcd(self, Polynomial_template other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 394)

        Compute extended gcd of ``self`` and ``other``.

        EXAMPLES::

            sage: P.<x> = GF(7)[]
            sage: f = x*(x+1)
            sage: f.xgcd(x+1)
            (x + 1, 0, 1)
            sage: f.xgcd(x^2)
            (x, 1, 6)"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __copy__(self) -> Any:
        """Polynomial_template.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 674)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: copy(x) is x
            False
            sage: copy(x) == x
            True"""
    def __hash__(self) -> Any:
        """Polynomial_template.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 556)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: {x:1}
            {x: 1}"""
    def __lshift__(self, intn) -> Any:
        """Polynomial_template.__lshift__(self, int n)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 721)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: f = x^3 + x^2 + 1
            sage: f << 1
            x^4 + x^3 + x
            sage: f << -1
            x^2 + x"""
    def __neg__(self) -> Any:
        """Polynomial_template.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 262)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: -x
            x"""
    def __pow__(self, ee, modulus) -> Any:
        """Polynomial_template.__pow__(self, ee, modulus)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 591)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: x^1000
            x^1000
            sage: (x+1)^2
            x^2 + 1
            sage: (x+1)^(-2)
            1/(x^2 + 1)
            sage: f = x^9 + x^7 + x^6 + x^5 + x^4 + x^2 + x
            sage: h = x^10 + x^7 + x^6 + x^5 + x^4 + x^3 + x^2 + 1
            sage: (f^2) % h
            x^9 + x^8 + x^7 + x^5 + x^3
            sage: pow(f, 2, h)
            x^9 + x^8 + x^7 + x^5 + x^3

        TESTS:

        Ensure modulo `0` and modulo `1` does not crash (:issue:`37169`)::

            sage: R.<x> = GF(2)[]
            sage: pow(x + 1, 2, R.zero())
            Traceback (most recent call last):
            ...
            ZeroDivisionError: modulus must be nonzero
            sage: pow(x + 1, 2, R.one())
            0

        ::

            sage: R.<x> = GF(2^8)[]
            sage: pow(x + 1, 2, R.zero())
            Traceback (most recent call last):
            ...
            ZeroDivisionError: modulus must be nonzero
            sage: pow(x + 1, 2, R.one())
            0"""
    def __reduce__(self) -> Any:
        """Polynomial_template.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 182)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: loads(dumps(x)) == x
            True"""
    def __rlshift__(self, other):
        """Return value<<self."""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
    def __rrshift__(self, other):
        """Return value>>self."""
    def __rshift__(self, intn) -> Any:
        """Polynomial_template.__rshift__(self, int n)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 734)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: x>>1
            1
            sage: (x^2 + x)>>1
            x + 1
            sage: (x^2 + x) >> -1
            x^3 + x^2"""
