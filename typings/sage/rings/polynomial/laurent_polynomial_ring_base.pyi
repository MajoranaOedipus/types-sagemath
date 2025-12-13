from sage.combinat.integer_vector import IntegerVectors as IntegerVectors
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.infinity import infinity as infinity
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.structure.parent import Parent as Parent

class LaurentPolynomialRing_generic(Parent):
    """
    Laurent polynomial ring (base class).

    EXAMPLES:

    Since :issue:`11900`, it is in the category of commutative rings::

        sage: R.<x1,x2> = LaurentPolynomialRing(QQ)
        sage: R.category()
        Join of Category of unique factorization domains
            and Category of algebras with basis
                over (number fields and quotient fields and metric spaces)
            and Category of commutative algebras
                over (number fields and quotient fields and metric spaces)
            and Category of infinite sets
        sage: TestSuite(R).run()
    """
    def __init__(self, R) -> None:
        """
        EXAMPLES::

            sage: R = LaurentPolynomialRing(QQ, 2, 'x')
            sage: R == loads(dumps(R))
            True
        """
    def ngens(self):
        """
        Return the number of generators of ``self``.

        EXAMPLES::

            sage: LaurentPolynomialRing(QQ, 2, 'x').ngens()
            2
            sage: LaurentPolynomialRing(QQ, 1, 'x').ngens()
            1
        """
    @cached_method
    def gens(self) -> tuple:
        """
        Return the tuple of generators of ``self``.

        EXAMPLES::

            sage: LaurentPolynomialRing(ZZ, 2, 'x').gens()
            (x0, x1)
            sage: LaurentPolynomialRing(QQ, 1, 'x').gens()
            (x,)
        """
    def gen(self, i: int = 0):
        """
        Return the `i`-th generator of ``self``.

        If `i` is not specified, then the first generator will be returned.

        EXAMPLES::

            sage: LaurentPolynomialRing(QQ, 2, 'x').gen()
            x0
            sage: LaurentPolynomialRing(QQ, 2, 'x').gen(0)
            x0
            sage: LaurentPolynomialRing(QQ, 2, 'x').gen(1)
            x1

        TESTS::

            sage: LaurentPolynomialRing(QQ, 2, 'x').gen(3)
            Traceback (most recent call last):
            ...
            ValueError: generator not defined
        """
    def variable_names_recursive(self, depth=...) -> tuple[str]:
        """
        Return the list of variable names of this ring and its base rings,
        as if it were a single multi-variate Laurent polynomial.

        INPUT:

        - ``depth`` -- integer or :mod:`Infinity <sage.rings.infinity>`

        OUTPUT: a tuple of strings

        EXAMPLES::

            sage: T = LaurentPolynomialRing(QQ, 'x')
            sage: S = LaurentPolynomialRing(T, 'y')
            sage: R = LaurentPolynomialRing(S, 'z')
            sage: R.variable_names_recursive()
            ('x', 'y', 'z')
            sage: R.variable_names_recursive(2)
            ('y', 'z')
        """
    def is_integral_domain(self, proof: bool = True) -> bool:
        """
        Return ``True`` if ``self`` is an integral domain.

        EXAMPLES::

            sage: LaurentPolynomialRing(QQ, 2, 'x').is_integral_domain()
            True

        The following used to fail; see :issue:`7530`::

            sage: L = LaurentPolynomialRing(ZZ, 'X')
            sage: L['Y']
            Univariate Polynomial Ring in Y over
             Univariate Laurent Polynomial Ring in X over Integer Ring
        """
    def is_noetherian(self) -> bool:
        """
        Return ``True`` if ``self`` is Noetherian.

        EXAMPLES::

            sage: LaurentPolynomialRing(QQ, 2, 'x').is_noetherian()
            True
        """
    def construction(self):
        """
        Return the construction of ``self``.

        EXAMPLES::

            sage: LaurentPolynomialRing(QQ, 2, 'x,y').construction()
            (LaurentPolynomialFunctor,
             Univariate Laurent Polynomial Ring in x over Rational Field)
        """
    def completion(self, p=None, prec: int = 20, extras=None):
        """
        Return the completion of ``self``.

        Currently only implemented for the ring of formal Laurent series.
        The ``prec`` variable controls the precision used in the
        Laurent series ring. If ``prec`` is `\\infty`, then this
        returns a :class:`LazyLaurentSeriesRing`.

        EXAMPLES::

            sage: P.<x> = LaurentPolynomialRing(QQ); P
            Univariate Laurent Polynomial Ring in x over Rational Field
            sage: PP = P.completion(x); PP
            Laurent Series Ring in x over Rational Field
            sage: f = 1 - 1/x
            sage: PP(f)
            -x^-1 + 1
            sage: g = 1 / PP(f); g
            -x - x^2 - x^3 - x^4 - x^5 - x^6 - x^7 - x^8 - x^9 - x^10 - x^11
             - x^12 - x^13 - x^14 - x^15 - x^16 - x^17 - x^18 - x^19 - x^20 + O(x^21)
            sage: 1 / g
            -x^-1 + 1 + O(x^19)

            sage: # needs sage.combinat
            sage: PP = P.completion(x, prec=oo); PP
            Lazy Laurent Series Ring in x over Rational Field
            sage: g = 1 / PP(f); g
            -x - x^2 - x^3 + O(x^4)
            sage: 1 / g == f
            True

        TESTS:

        Check that the precision is taken into account (:issue:`24431`)::

            sage: L = LaurentPolynomialRing(QQ, 'x')
            sage: L.completion('x', 100).default_prec()
            100
            sage: L.completion('x', 20).default_prec()
            20
        """
    def remove_var(self, var):
        """
        EXAMPLES::

            sage: R = LaurentPolynomialRing(QQ,'x,y,z')
            sage: R.remove_var('x')
            Multivariate Laurent Polynomial Ring in y, z over Rational Field
            sage: R.remove_var('x').remove_var('y')
            Univariate Laurent Polynomial Ring in z over Rational Field
        """
    def __eq__(self, right) -> bool:
        """
        Check whether ``self`` is equal to ``right``.

        EXAMPLES::

            sage: R = LaurentPolynomialRing(QQ,'x,y,z')
            sage: P = LaurentPolynomialRing(ZZ,'x,y,z')
            sage: Q = LaurentPolynomialRing(QQ,'x,y')

            sage: R == R
            True
            sage: R == Q
            False
            sage: Q == P
            False
            sage: P == R
            False
        """
    def __ne__(self, other) -> bool:
        """
        Check whether ``self`` is not equal to ``other``.

        EXAMPLES::

            sage: R = LaurentPolynomialRing(QQ,'x,y,z')
            sage: P = LaurentPolynomialRing(ZZ,'x,y,z')
            sage: Q = LaurentPolynomialRing(QQ,'x,y')

            sage: R != R
            False
            sage: R != Q
            True
            sage: Q != P
            True
            sage: P != R
            True
        """
    def __hash__(self) -> int:
        """
        Return the hash of ``self``.

        EXAMPLES::

            sage: h1 = hash(LaurentPolynomialRing(ZZ,'x,y,z'))
            sage: h2 = hash(LaurentPolynomialRing(ZZ,'x,y,z'))
            sage: h3 = hash(LaurentPolynomialRing(QQ,'x,y,z'))
            sage: h4 = hash(LaurentPolynomialRing(ZZ,'x,y'))
            sage: h1 == h2 and h1 != h3 and h1 != h4
            True
        """
    def ideal(self, *args, **kwds):
        """
        EXAMPLES::

            sage: LaurentPolynomialRing(QQ, 2, 'x').ideal([1])
            Ideal (1) of Multivariate Laurent Polynomial Ring in x0, x1 over Rational Field

        TESTS:

        check that :issue:`26421` is fixed::

            sage: R.<t> = LaurentPolynomialRing(ZZ)
            sage: P.<x> = PolynomialRing(R)
            sage: p = x-t
            sage: p.content_ideal()    # indirect doctest
            Ideal (-t, 1) of Univariate Laurent Polynomial Ring in t over Integer Ring
        """
    def term_order(self):
        """
        Return the term order of ``self``.

        EXAMPLES::

            sage: LaurentPolynomialRing(QQ, 2, 'x').term_order()
            Degree reverse lexicographic term order
        """
    def is_finite(self) -> bool:
        """
        EXAMPLES::

            sage: LaurentPolynomialRing(QQ, 2, 'x').is_finite()
            False
        """
    def is_field(self, proof: bool = True) -> bool:
        """
        EXAMPLES::

            sage: LaurentPolynomialRing(QQ, 2, 'x').is_field()
            False
        """
    def polynomial_ring(self):
        """
        Return the polynomial ring associated with ``self``.

        EXAMPLES::

            sage: LaurentPolynomialRing(QQ, 2, 'x').polynomial_ring()
            Multivariate Polynomial Ring in x0, x1 over Rational Field
            sage: LaurentPolynomialRing(QQ, 1, 'x').polynomial_ring()
            Multivariate Polynomial Ring in x over Rational Field
        """
    def characteristic(self):
        """
        Return the characteristic of the base ring.

        EXAMPLES::

            sage: LaurentPolynomialRing(QQ, 2, 'x').characteristic()
            0
            sage: LaurentPolynomialRing(GF(3), 2, 'x').characteristic()
            3
        """
    def krull_dimension(self) -> None:
        """
        EXAMPLES::

            sage: LaurentPolynomialRing(QQ, 2, 'x').krull_dimension()
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    def random_element(self, min_valuation: int = -2, max_degree: int = 2, *args, **kwds):
        """
        Return a random polynomial with degree at most ``max_degree`` and
        lowest valuation at least ``min_valuation``.

        Uses the random sampling from the base polynomial ring then divides out
        by a monomial to ensure correct ``max_degree`` and ``min_valuation``.

        INPUT:

        - ``min_valuation`` -- integer (default: `-2`); the
          minimal allowed valuation of the polynomial

        - ``max_degree`` -- integer (default: `2`); the
          maximal allowed degree of the polynomial

        - ``*args``, ``**kwds`` -- passed to the random element generator of the
          base polynomial ring and base ring itself

        EXAMPLES::

            sage: L.<x> = LaurentPolynomialRing(QQ)
            sage: f = L.random_element()
            sage: f.degree() <= 2
            True
            sage: f.valuation() >= -2
            True
            sage: f.parent() is L
            True

        ::

            sage: L = LaurentPolynomialRing(ZZ, 2, 'x')
            sage: f = L.random_element(10, 20)
            sage: f.degree() <= 20
            True
            sage: f.valuation() >= 10
            True
            sage: f.parent() is L
            True

        ::

            sage: L = LaurentPolynomialRing(GF(13), 3, 'x')
            sage: f = L.random_element(-10, -1)
            sage: f.degree() <= -1
            True
            sage: f.valuation() >= -10
            True
            sage: f.parent() is L
            True

        ::

            sage: L.<x, y> = LaurentPolynomialRing(RR)
            sage: f = L.random_element()
            sage: f.degree() <= 2
            True
            sage: f.valuation() >= -2
            True
            sage: f.parent() is L
            True

        ::

            sage: L = LaurentPolynomialRing(QQbar, 5, 'x')
            sage: f = L.random_element(-1, 1)
            sage: f = L.random_element(-1, 1)
            sage: f.degree() <= 1
            True
            sage: f.valuation() >= -1
            True
            sage: f.parent() is L
            True

        TESTS:

        Ensure everything works for the multivariate case with only
        one generator::

            sage: L = LaurentPolynomialRing(ZZ, 1, 'x')
            sage: f = L.random_element(10, 20)
            sage: f.degree() <= 20
            True
            sage: f.valuation() >= 10
            True
            sage: f.parent() is L
            True

        Test for constructions which use multivariate polynomial rings::

            sage: rings = [RR, QQ, ZZ, GF(13), GF(7^3)]
            sage: for ring in rings:
            ....:     d = randint(1, 6)
            ....:     t = randint(5, 20)
            ....:     L = LaurentPolynomialRing(ring, d, 'x')
            ....:     for _ in range(100):
            ....:         n, m = randint(-10, 10), randint(-10, 10)
            ....:         if n > m:
            ....:             n, m = m, n
            ....:         f = L.random_element(n, m, terms=t)
            ....:         if f.is_zero(): continue # the zero polynomial is defined to have degree -1
            ....:         assert len(list(f)) <= t
            ....:         assert f.degree() <= m
            ....:         assert f.valuation() >= n

        Test for constructions which use univariate polynomial rings::

            sage: rings = [RR, QQ, ZZ, GF(13), GF(7^3)]
            sage: for ring in rings:
            ....:     L.<x> = LaurentPolynomialRing(ring)
            ....:     for _ in range(100):
            ....:         n, m = randint(-10, 10), randint(-10, 10)
            ....:         if n > m:
            ....:             n, m = m, n
            ....:         f = L.random_element(n, m)
            ....:         if f.is_zero(): continue # the zero polynomial is defined to have degree -1
            ....:         for x in L.gens():
            ....:             assert f.degree() <= m
            ....:             assert f.valuation() >= n

        The ``max_degree`` must be greater than or equal to ``min_valuation``::

            sage: L.<x> = LaurentPolynomialRing(QQ)
            sage: f = L.random_element(1, -1)
            Traceback (most recent call last):
            ...
            ValueError: `max_degree` must be greater than or equal to `min_valuation`
        """
    def is_exact(self) -> bool:
        """
        Return ``True`` if the base ring is exact.

        EXAMPLES::

            sage: LaurentPolynomialRing(QQ, 2, 'x').is_exact()
            True
            sage: LaurentPolynomialRing(RDF, 2, 'x').is_exact()
            False
        """
    def change_ring(self, base_ring=None, names=None, sparse: bool = False, order=None):
        """
        EXAMPLES::

            sage: R = LaurentPolynomialRing(QQ, 2, 'x')
            sage: R.change_ring(ZZ)
            Multivariate Laurent Polynomial Ring in x0, x1 over Integer Ring

        Check that the distinction between a univariate ring and a multivariate ring with one
        generator is preserved::

            sage: P.<x> = LaurentPolynomialRing(QQ, 1)
            sage: P
            Multivariate Laurent Polynomial Ring in x over Rational Field
            sage: K.<i> = CyclotomicField(4)                                                        # needs sage.rings.number_field
            sage: P.change_ring(K)                                                                  # needs sage.rings.number_field
            Multivariate Laurent Polynomial Ring in x over
             Cyclotomic Field of order 4 and degree 2
        """
    def fraction_field(self):
        """
        The fraction field is the same as the fraction field of the
        polynomial ring.

        EXAMPLES::

            sage: L.<x> = LaurentPolynomialRing(QQ)
            sage: L.fraction_field()
            Fraction Field of Univariate Polynomial Ring in x over Rational Field
            sage: (x^-1 + 2) / (x - 1)
            (2*x + 1)/(x^2 - x)
        """
