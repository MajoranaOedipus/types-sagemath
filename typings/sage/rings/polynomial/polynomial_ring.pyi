from _typeshed import Incomplete
from sage.categories.morphism import IdentityMorphism as IdentityMorphism
from sage.categories.principal_ideal_domains import PrincipalIdealDomains as PrincipalIdealDomains
from sage.categories.rings import Rings as Rings
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.misc.superseded import deprecation as deprecation
from sage.rings.finite_rings.element_base import FiniteRingElement as FiniteRingElement
from sage.rings.fraction_field_element import FractionFieldElement as FractionFieldElement
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.number_field.number_field_base import NumberField as NumberField
from sage.rings.polynomial.polynomial_ring_constructor import polynomial_default_category as polynomial_default_category
from sage.rings.polynomial.polynomial_singular_interface import PolynomialRing_singular_repr as PolynomialRing_singular_repr, can_convert_to_singular as can_convert_to_singular
from sage.rings.power_series_ring_element import PowerSeries as PowerSeries
from sage.rings.rational_field import QQ as QQ
from sage.rings.ring import CommutativeRing as CommutativeRing, Ring as Ring
from sage.structure.category_object import check_default_category as check_default_category
from sage.structure.element import Element as Element, RingElement as RingElement

def is_PolynomialRing(x):
    """
    Return ``True`` if ``x`` is a *univariate* polynomial ring (and not a
    sparse multivariate polynomial ring in one variable).

    EXAMPLES::

        sage: from sage.rings.polynomial.polynomial_ring import is_PolynomialRing
        sage: from sage.rings.polynomial.multi_polynomial_ring import is_MPolynomialRing
        sage: is_PolynomialRing(2)
        doctest:warning...
        DeprecationWarning: The function is_PolynomialRing is deprecated;
        use 'isinstance(..., PolynomialRing_generic)' instead.
        See https://github.com/sagemath/sage/issues/38266 for details.
        False

    This polynomial ring is not univariate.

    ::

        sage: is_PolynomialRing(ZZ['x,y,z'])
        False
        sage: is_MPolynomialRing(ZZ['x,y,z'])
        doctest:warning...
        DeprecationWarning: The function is_MPolynomialRing is deprecated;
        use 'isinstance(..., MPolynomialRing_base)' instead.
        See https://github.com/sagemath/sage/issues/38266 for details.
        True

    ::

        sage: is_PolynomialRing(ZZ['w'])
        True

    Univariate means not only in one variable, but is a specific data
    type. There is a multivariate (sparse) polynomial ring data type,
    which supports a single variable as a special case.

    ::

        sage: # needs sage.libs.singular
        sage: R.<w> = PolynomialRing(ZZ, implementation='singular'); R
        Multivariate Polynomial Ring in w over Integer Ring
        sage: is_PolynomialRing(R)
        False
        sage: type(R)
        <class 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular'>
    """

class PolynomialRing_generic(Ring):
    """
    Univariate polynomial ring over a ring.
    """
    Element: Incomplete
    def __init__(self, base_ring, name=None, sparse: bool = False, implementation=None, element_class=None, category=None) -> None:
        """
        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: R(-1) + R(1)
            0
            sage: (x - 2/3)*(x^2 - 8*x + 16)
            x^3 - 26/3*x^2 + 64/3*x - 32/3

            sage: category(ZZ['x'])
            Join of Category of unique factorization domains
             and Category of algebras with basis over
              (Dedekind domains and euclidean domains
               and noetherian rings and infinite enumerated sets
               and metric spaces)
             and Category of commutative algebras over
              (Dedekind domains and euclidean domains
               and noetherian rings and infinite enumerated sets
               and metric spaces)
             and Category of infinite sets

            sage: category(GF(7)['x'])
            Join of Category of euclidean domains
             and Category of algebras with basis over
              (finite enumerated fields and subquotients of monoids
               and quotients of semigroups)
            and Category of commutative algebras over
              (finite enumerated fields and subquotients of monoids
               and quotients of semigroups)
            and Category of infinite sets

        TESTS:

        Verify that :issue:`15232` has been resolved::

            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: TestSuite(R).run()

        Check that category for zero ring::

            sage: PolynomialRing(Zmod(1), 'x').category()
            Category of finite commutative rings

        Check ``is_finite`` inherited from category (:issue:`24432`)::

            sage: Zmod(1)['x'].is_finite()
            True

            sage: GF(7)['x'].is_finite()
            False

            sage: Zmod(1)['x']['y'].is_finite()
            True

            sage: GF(7)['x']['y'].is_finite()
            False
        """
    def __reduce__(self): ...
    def is_integral_domain(self, proof: bool = True):
        """
        EXAMPLES::

            sage: ZZ['x'].is_integral_domain()
            True
            sage: Integers(8)['x'].is_integral_domain()
            False
        """
    def is_unique_factorization_domain(self, proof: bool = True):
        """
        EXAMPLES::

            sage: ZZ['x'].is_unique_factorization_domain()
            True
            sage: Integers(8)['x'].is_unique_factorization_domain()
            False
        """
    def is_noetherian(self): ...
    def some_elements(self):
        """
        Return a list of polynomials.

        This is typically used for running generic tests.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: R.some_elements()
            [x, 0, 1, 1/2, x^2 + 2*x + 1, x^3, x^2 - 1, x^2 + 1, 2*x^2 + 2]
        """
    def monomials_of_degree(self, degree):
        """
        Return the list of all monomials of the given total
        degree in this univariate polynomial ring, which is simply the list with one element ``[self.gen()**degree]``.

        .. SEEALSO::

            :meth:`sage.rings.polynomial.multi_polynomial_ring_base.MPolynomialRing_base.monomials_of_degree`

        EXAMPLES::

            sage: R.<x> = ZZ[]
            sage: mons = R.monomials_of_degree(2)
            sage: mons
            [x^2]
        """
    @cached_method
    def flattening_morphism(self):
        """
        Return the flattening morphism of this polynomial ring.

        EXAMPLES::

            sage: QQ['a','b']['x'].flattening_morphism()
            Flattening morphism:
              From: Univariate Polynomial Ring in x over
                    Multivariate Polynomial Ring in a, b over Rational Field
              To:   Multivariate Polynomial Ring in a, b, x over Rational Field

            sage: QQ['x'].flattening_morphism()
            Identity endomorphism of Univariate Polynomial Ring in x over Rational Field
        """
    def construction(self):
        """
        Return the construction functor.
        """
    def completion(self, p=None, prec: int = 20, extras=None):
        """
        Return the completion of ``self`` with respect to the irreducible
        polynomial ``p``.

        Currently only implemented for ``p=self.gen()`` (the default), i.e. you
        can only complete `R[x]` with respect to `x`, the result being a ring
        of power series in `x`. The ``prec`` variable controls the precision
        used in the power series ring. If ``prec`` is `\\infty`, then this
        returns a :class:`LazyPowerSeriesRing`.

        EXAMPLES::

            sage: P.<x> = PolynomialRing(QQ)
            sage: P
            Univariate Polynomial Ring in x over Rational Field
            sage: PP = P.completion(x)
            sage: PP
            Power Series Ring in x over Rational Field
            sage: f = 1 - x
            sage: PP(f)
            1 - x
            sage: 1 / f
            -1/(x - 1)
            sage: g = 1 / PP(f); g
            1 + x + x^2 + x^3 + x^4 + x^5 + x^6 + x^7 + x^8 + x^9 + x^10 + x^11
             + x^12 + x^13 + x^14 + x^15 + x^16 + x^17 + x^18 + x^19 + O(x^20)
            sage: 1 / g
            1 - x + O(x^20)

            sage: # needs sage.combinat
            sage: PP = P.completion(x, prec=oo); PP
            Lazy Taylor Series Ring in x over Rational Field
            sage: g = 1 / PP(f); g
            1 + x + x^2 + O(x^3)
            sage: 1 / g == f
            True
        """
    def __hash__(self): ...
    def base_extend(self, R):
        """
        Return the base extension of this polynomial ring to `R`.

        EXAMPLES::

            sage: # needs sage.rings.real_mpfr
            sage: R.<x> = RR[]; R
            Univariate Polynomial Ring in x over Real Field with 53 bits of precision
            sage: R.base_extend(CC)
            Univariate Polynomial Ring in x over Complex Field with 53 bits of precision
            sage: R.base_extend(QQ)
            Traceback (most recent call last):
            ...
            TypeError: no such base extension
            sage: R.change_ring(QQ)
            Univariate Polynomial Ring in x over Rational Field
        """
    def change_ring(self, R):
        """
        Return the polynomial ring in the same variable as ``self`` over `R`.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings sage.rings.real_interval_field
            sage: R.<ZZZ> = RealIntervalField()[]; R
            Univariate Polynomial Ring in ZZZ over
             Real Interval Field with 53 bits of precision
            sage: R.change_ring(GF(19^2, 'b'))
            Univariate Polynomial Ring in ZZZ over Finite Field in b of size 19^2
        """
    def change_var(self, var):
        """
        Return the polynomial ring in variable ``var`` over the same base
        ring.

        EXAMPLES::

            sage: R.<x> = ZZ[]; R
            Univariate Polynomial Ring in x over Integer Ring
            sage: R.change_var('y')
            Univariate Polynomial Ring in y over Integer Ring
        """
    def extend_variables(self, added_names, order: str = 'degrevlex'):
        """
        Return a multivariate polynomial ring with the same base ring but
        with ``added_names`` as additional variables.

        EXAMPLES::

            sage: R.<x> = ZZ[]; R
            Univariate Polynomial Ring in x over Integer Ring
            sage: R.extend_variables('y, z')
            Multivariate Polynomial Ring in x, y, z over Integer Ring
            sage: R.extend_variables(('y', 'z'))
            Multivariate Polynomial Ring in x, y, z over Integer Ring
        """
    def variable_names_recursive(self, depth=...):
        """
        Return the list of variable names of this ring and its base rings,
        as if it were a single multi-variate polynomial.

        INPUT:

        - ``depth`` -- integer or :mod:`Infinity <sage.rings.infinity>`

        OUTPUT: a tuple of strings

        EXAMPLES::

            sage: R = QQ['x']['y']['z']
            sage: R.variable_names_recursive()
            ('x', 'y', 'z')
            sage: R.variable_names_recursive(2)
            ('y', 'z')
        """
    def characteristic(self):
        """
        Return the characteristic of this polynomial ring, which is the
        same as that of its base ring.

        EXAMPLES::

            sage: # needs sage.rings.real_interval_field
            sage: R.<ZZZ> = RealIntervalField()[]; R
            Univariate Polynomial Ring in ZZZ over Real Interval Field with 53 bits of precision
            sage: R.characteristic()
            0
            sage: S = R.change_ring(GF(19^2, 'b')); S                                   # needs sage.rings.finite_rings
            Univariate Polynomial Ring in ZZZ over Finite Field in b of size 19^2
            sage: S.characteristic()                                                    # needs sage.rings.finite_rings
            19
        """
    def cyclotomic_polynomial(self, n):
        """
        Return the `n`-th cyclotomic polynomial as a polynomial in this
        polynomial ring. For details of the implementation, see the
        documentation for
        :func:`sage.rings.polynomial.cyclotomic.cyclotomic_coeffs`.

        EXAMPLES::

            sage: R = ZZ['x']
            sage: R.cyclotomic_polynomial(8)
            x^4 + 1
            sage: R.cyclotomic_polynomial(12)
            x^4 - x^2 + 1

            sage: S = PolynomialRing(FiniteField(7), 'x')
            sage: S.cyclotomic_polynomial(12)
            x^4 + 6*x^2 + 1
            sage: S.cyclotomic_polynomial(1)
            x + 6

        TESTS:

        Make sure it agrees with other systems for the trivial case::

            sage: ZZ['x'].cyclotomic_polynomial(1)
            x - 1
            sage: gp('polcyclo(1)')                                                     # needs sage.libs.pari
            x - 1
        """
    @cached_method
    def gen(self, n: int = 0):
        """
        Return the indeterminate generator of this polynomial ring.

        EXAMPLES::

            sage: R.<abc> = Integers(8)[]; R
            Univariate Polynomial Ring in abc over Ring of integers modulo 8
            sage: t = R.gen(); t
            abc
            sage: t.is_gen()
            True

        An identical generator is always returned.

        ::

            sage: t is R.gen()
            True
        """
    def gens_dict(self) -> dict:
        """
        Return a dictionary whose entries are ``{name:variable,...}``,
        where ``name`` stands for the variable names of this
        object (as strings) and ``variable`` stands for the corresponding
        generators (as elements of this object).

        EXAMPLES::

            sage: R.<y,x,a42> = RR[]
            sage: R.gens_dict()
            {'a42': a42, 'x': x, 'y': y}
        """
    def parameter(self):
        """
        Return the generator of this polynomial ring.

        This is the same as ``self.gen()``.
        """
    @cached_method
    def is_exact(self): ...
    def is_field(self, proof: bool = True):
        """
        Return ``False``, since polynomial rings are never fields.

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: R.<z> = Integers(2)[]; R
            Univariate Polynomial Ring in z over Ring of integers modulo 2 (using GF2X)
            sage: R.is_field()
            False
        """
    def is_sparse(self):
        """
        Return ``True`` if elements of this polynomial ring have a sparse
        representation.

        EXAMPLES::

            sage: R.<z> = Integers(8)[]; R
            Univariate Polynomial Ring in z over Ring of integers modulo 8
            sage: R.is_sparse()
            False
            sage: R.<W> = PolynomialRing(QQ, sparse=True); R
            Sparse Univariate Polynomial Ring in W over Rational Field
            sage: R.is_sparse()
            True
        """
    def monomial(self, exponent):
        """
        Return the monomial with the ``exponent``.

        INPUT:

        - ``exponent`` -- nonnegative integer

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ)
            sage: R.monomial(5)
            x^5
            sage: e=(10,)
            sage: R.monomial(*e)
            x^10
            sage: m = R.monomial(100)
            sage: R.monomial(m.degree()) == m
            True
        """
    def krull_dimension(self):
        """
        Return the Krull dimension of this polynomial ring, which is one
        more than the Krull dimension of the base ring.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: R.krull_dimension()
            1

            sage: # needs sage.rings.finite_rings
            sage: R.<z> = GF(9, 'a')[]; R
            Univariate Polynomial Ring in z over Finite Field in a of size 3^2
            sage: R.krull_dimension()
            1
            sage: S.<t> = R[]
            sage: S.krull_dimension()
            2
            sage: for n in range(10):
            ....:     S = PolynomialRing(S, 'w')
            sage: S.krull_dimension()
            12
        """
    def ngens(self):
        """
        Return the number of generators of this polynomial ring, which is 1
        since it is a univariate polynomial ring.

        EXAMPLES::

            sage: R.<z> = Integers(8)[]; R
            Univariate Polynomial Ring in z over Ring of integers modulo 8
            sage: R.ngens()
            1
        """
    def random_element(self, degree=(-1, 2), monic: bool = False, *args, **kwds):
        '''
        Return a random polynomial of given degree (bounds).

        INPUT:

        - ``degree`` -- (default: ``(-1, 2)``) integer for fixing the degree or
          a tuple of minimum and maximum degrees

        - ``monic`` -- boolean (default: ``False``); indicate whether the sampled
          polynomial should be monic

        - ``*args, **kwds`` -- additional keyword parameters passed on to the
          ``random_element`` method for the base ring

        EXAMPLES::

            sage: R.<x> = ZZ[]
            sage: f = R.random_element(10, x=5, y=10)
            sage: f.degree()
            10
            sage: f.parent() is R
            True
            sage: all(a in range(5, 10) for a in f.coefficients())
            True
            sage: R.random_element(6).degree()
            6

        If a tuple of two integers is given for the ``degree`` argument, a
        polynomial is chosen among all polynomials with degree between them. If
        the base ring can be sampled uniformly, then this method also samples
        uniformly::

            sage: R.random_element(degree=(0, 4)).degree() in range(0, 5)
            True
            sage: found = [False]*5
            sage: while not all(found):
            ....:     found[R.random_element(degree=(0, 4)).degree()] = True

        Note that the zero polynomial has degree `-1`, so if you want to
        consider it set the minimum degree to `-1`::

            sage: while R.random_element(degree=(-1,2), x=-1, y=1) != R.zero():
            ....:     pass

        Monic polynomials are chosen among all monic polynomials with degree
        between the given ``degree`` argument::

            sage: all(R.random_element(degree=(-1, 1), monic=True).is_monic() for _ in range(10^3))
            True
            sage: all(R.random_element(degree=(0, 1), monic=True).is_monic() for _ in range(10^3))
            True

        TESTS::

            sage: R.random_element(degree=[5])
            Traceback (most recent call last):
            ...
            ValueError: degree argument must be an integer or a tuple of 2 integers (min_degree, max_degree)

            sage: R.random_element(degree=(5,4))
            Traceback (most recent call last):
            ...
            ValueError: minimum degree must be less or equal than maximum degree

        Check that :issue:`16682` is fixed::

            sage: R = PolynomialRing(GF(2), \'z\')
            sage: for _ in range(100):
            ....:     d = randint(-1, 20)
            ....:     P = R.random_element(degree=d)
            ....:     assert P.degree() == d

        In :issue:`37118`, ranges including integers below `-1` no longer raise
        an error::

            sage: R.random_element(degree=(-2, 3))  # random
            z^3 + z^2 + 1

        ::

            sage: 0 in [R.random_element(degree=(-1, 2), monic=True) for _ in range(500)]
            False

        Testing error handling::

            sage: R.random_element(degree=-5)
            Traceback (most recent call last):
            ...
            ValueError: degree (=-5) must be at least -1

            sage: R.random_element(degree=(-3, -2))
            Traceback (most recent call last):
            ...
            ValueError: maximum degree (=-2) must be at least -1

        Testing uniformity::

            sage: from collections import Counter
            sage: R = GF(3)["x"]
            sage: samples = [R.random_element(degree=(-1, 2)) for _ in range(27000)]    # long time
            sage: assert all(750 <= f <= 1250 for f in Counter(samples).values())       # long time

            sage: samples = [R.random_element(degree=(-1, 2), monic=True) for _ in range(13000)] # long time
            sage: assert all(750 <= f <= 1250 for f in Counter(samples).values())       # long time
        '''
    def karatsuba_threshold(self):
        """
        Return the Karatsuba threshold used for this ring by the method
        :meth:`_mul_karatsuba` to fall back to the schoolbook algorithm.

        EXAMPLES::

            sage: K = QQ['x']
            sage: K.karatsuba_threshold()
            8
            sage: K = QQ['x']['y']
            sage: K.karatsuba_threshold()
            0
        """
    def set_karatsuba_threshold(self, Karatsuba_threshold) -> None:
        """
        Changes the default threshold for this ring in the method
        :meth:`_mul_karatsuba` to fall back to the schoolbook algorithm.

        .. warning::

           This method may have a negative performance impact in polynomial
           arithmetic. So use it at your own risk.

        EXAMPLES::

            sage: K = QQ['x']
            sage: K.karatsuba_threshold()
            8
            sage: K.set_karatsuba_threshold(0)
            sage: K.karatsuba_threshold()
            0
        """
    def polynomials(self, of_degree=None, max_degree=None):
        """
        Return an iterator over the polynomials of specified degree.

        INPUT: Pass exactly one of:

        - ``max_degree`` -- an int; the iterator will generate all polynomials
          which have degree less than or equal to ``max_degree``

        - ``of_degree`` -- an int; the iterator will generate
          all polynomials which have degree ``of_degree``

        OUTPUT: an iterator

        EXAMPLES::

            sage: P = PolynomialRing(GF(3), 'y')
            sage: for p in P.polynomials(of_degree=2): print(p)
            y^2
            y^2 + 1
            y^2 + 2
            y^2 + y
            y^2 + y + 1
            y^2 + y + 2
            y^2 + 2*y
            y^2 + 2*y + 1
            y^2 + 2*y + 2
            2*y^2
            2*y^2 + 1
            2*y^2 + 2
            2*y^2 + y
            2*y^2 + y + 1
            2*y^2 + y + 2
            2*y^2 + 2*y
            2*y^2 + 2*y + 1
            2*y^2 + 2*y + 2
            sage: for p in P.polynomials(max_degree=1): print(p)
            0
            1
            2
            y
            y + 1
            y + 2
            2*y
            2*y + 1
            2*y + 2
            sage: for p in P.polynomials(max_degree=1, of_degree=3): print(p)
            Traceback (most recent call last):
            ...
            ValueError: you should pass exactly one of of_degree and max_degree

        AUTHORS:

        - Joel B. Mohler
        """
    def monics(self, of_degree=None, max_degree=None):
        """
        Return an iterator over the monic polynomials of specified degree.

        INPUT: Pass exactly one of:


        - ``max_degree`` -- an int; the iterator will generate all monic
          polynomials which have degree less than or equal to ``max_degree``

        - ``of_degree`` -- an int; the iterator will generate
          all monic polynomials which have degree ``of_degree``

        OUTPUT: an iterator

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: P = PolynomialRing(GF(4, 'a'), 'y')
            sage: for p in P.monics(of_degree=2): print(p)
            y^2
            y^2 + a
            y^2 + a + 1
            y^2 + 1
            y^2 + a*y
            y^2 + a*y + a
            y^2 + a*y + a + 1
            y^2 + a*y + 1
            y^2 + (a + 1)*y
            y^2 + (a + 1)*y + a
            y^2 + (a + 1)*y + a + 1
            y^2 + (a + 1)*y + 1
            y^2 + y
            y^2 + y + a
            y^2 + y + a + 1
            y^2 + y + 1
            sage: for p in P.monics(max_degree=1): print(p)
            1
            y
            y + a
            y + a + 1
            y + 1
            sage: for p in P.monics(max_degree=1, of_degree=3): print(p)
            Traceback (most recent call last):
            ...
            ValueError: you should pass exactly one of of_degree and max_degree

        AUTHORS:

        - Joel B. Mohler
        """
PolynomialRing_general = PolynomialRing_generic

class PolynomialRing_commutative(PolynomialRing_generic):
    """
    Univariate polynomial ring over a commutative ring.
    """
    def __init__(self, base_ring, name=None, sparse: bool = False, implementation=None, element_class=None, category=None) -> None: ...
    def quotient_by_principal_ideal(self, f, names=None, **kwds):
        """
        Return the quotient of this polynomial ring by the principal
        ideal (generated by) `f`.

        INPUT:

        - ``f`` -- either a polynomial in ``self``, or a principal
          ideal of ``self``
        - further named arguments that are passed to the quotient constructor

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: I = (x^2 - 1) * R
            sage: R.quotient_by_principal_ideal(I)                                      # needs sage.libs.pari
            Univariate Quotient Polynomial Ring in xbar
             over Rational Field with modulus x^2 - 1

        The same example, using the polynomial instead of the ideal,
        and customizing the variable name::

            sage: R.<x> = QQ[]
            sage: R.quotient_by_principal_ideal(x^2 - 1, names=('foo',))                # needs sage.libs.pari
            Univariate Quotient Polynomial Ring in foo
             over Rational Field with modulus x^2 - 1

        TESTS:

        Quotienting by the zero ideal returns ``self`` (:issue:`5978`)::

            sage: R = QQ['x']
            sage: R.quotient_by_principal_ideal(R.zero_ideal()) is R
            True
            sage: R.quotient_by_principal_ideal(0) is R
            True
        """
    def weyl_algebra(self):
        """
        Return the Weyl algebra generated from ``self``.

        EXAMPLES::

            sage: R = QQ['x']
            sage: W = R.weyl_algebra(); W                                               # needs sage.modules
            Differential Weyl algebra of polynomials in x over Rational Field
            sage: W.polynomial_ring() == R                                              # needs sage.modules
            True
        """

class PolynomialRing_integral_domain(PolynomialRing_commutative, PolynomialRing_singular_repr, CommutativeRing):
    def __init__(self, base_ring, name: str = 'x', sparse: bool = False, implementation=None, element_class=None, category=None) -> None:
        """
        TESTS::

            sage: from sage.rings.polynomial.polynomial_ring import PolynomialRing_integral_domain as PRing
            sage: R = PRing(ZZ, 'x'); R
            Univariate Polynomial Ring in x over Integer Ring
            sage: type(R.gen())                                                         # needs sage.libs.flint
            <class 'sage.rings.polynomial.polynomial_integer_dense_flint.Polynomial_integer_dense_flint'>

            sage: R = PRing(ZZ, 'x', implementation='NTL'); R                           # needs sage.libs.ntl
            Univariate Polynomial Ring in x over Integer Ring (using NTL)
            sage: type(R.gen())                                                         # needs sage.libs.ntl
            <class 'sage.rings.polynomial.polynomial_integer_dense_ntl.Polynomial_integer_dense_ntl'>
        """
    def weil_polynomials(self, d, q, sign: int = 1, lead: int = 1):
        """
        Return all integer polynomials whose complex roots all have a specified
        absolute value.

        Such polynomials `f` satisfy a functional equation

        .. MATH::

            T^d f(q/T) = s q^{d/2} f(T)

        where `d` is the degree of `f`, `s` is a sign and `q^{1/2}` is the
        absolute value of the roots of `f`.

        INPUT:

        - ``d`` -- integer; the degree of the polynomials

        - ``q`` -- integer; the square of the complex absolute value of the
          roots

        - ``sign`` -- integer (default: `1`); the sign `s` of the functional
          equation

        - ``lead`` -- integer; list of integers or list of pairs of integers
          (default: `1`), constraints on the leading few coefficients of the
          generated polynomials. If pairs `(a, b)` of integers are given, they
          are treated as a constraint of the form `\\equiv a \\pmod{b}`; the
          moduli must be in decreasing order by divisibility, and the modulus
          of the leading coefficient must be 0.

        .. SEEALSO::

            More documentation and additional options are available using the
            iterator
            :class:`sage.rings.polynomial.weil.weil_polynomials.WeilPolynomials`
            directly. In addition, polynomials have a method
            :meth:`is_weil_polynomial` to test whether or not the given
            polynomial is a Weil polynomial.

        EXAMPLES::

            sage: # needs sage.libs.flint
            sage: R.<T> = ZZ[]
            sage: L = R.weil_polynomials(4, 2)
            sage: len(L)
            35
            sage: L[9]
            T^4 + T^3 + 2*T^2 + 2*T + 4
            sage: all(p.is_weil_polynomial() for p in L)
            True

        Setting multiple leading coefficients::

            sage: R.<T> = QQ[]
            sage: l = R.weil_polynomials(4, 2, lead=((1,0), (2,4), (1,2))); l           # needs sage.libs.flint
            [T^4 + 2*T^3 + 5*T^2 + 4*T + 4,
             T^4 + 2*T^3 + 3*T^2 + 4*T + 4,
             T^4 - 2*T^3 + 5*T^2 - 4*T + 4,
             T^4 - 2*T^3 + 3*T^2 - 4*T + 4]

        We do not require Weil polynomials to be monic. This example generates Weil
        polynomials associated to K3 surfaces over `\\GF{2}` of Picard number at least 12::

            sage: R.<T> = QQ[]
            sage: l = R.weil_polynomials(10, 1, lead=2)                                 # needs sage.libs.flint
            sage: len(l)                                                                # needs sage.libs.flint
            4865
            sage: l[len(l)//2]                                                          # needs sage.libs.flint
            2*T^10 + T^8 + T^6 + T^4 + T^2 + 2

        TESTS:

        We check that products of Weil polynomials are also listed as Weil
        polynomials::

            sage: all((f * g) in R.weil_polynomials(6, q) for q in [3, 4]                                               # needs sage.libs.flint
            ....:     for f in R.weil_polynomials(2, q) for g in R.weil_polynomials(4, q))
            True

        We check that irreducible Weil polynomials of degree 6 are CM::

            sage: simples = [f for f in R.weil_polynomials(6, 3) if f.is_irreducible()]                                 # needs sage.libs.flint
            sage: len(simples)                                                                                          # needs sage.libs.flint
            348
            sage: reals = [R([f[3+i] + sum((-3)^j * (i+2*j)/(i+j) * binomial(i+j,j) * f[3+i+2*j]                        # needs sage.libs.flint
            ....:                          for j in range(1, (3+i)//2 + 1))
            ....:          for i in range(4)]) for f in simples]

        Check that every polynomial in this list has 3 real roots between `-2
        \\sqrt{3}` and `2 \\sqrt{3}`::

            sage: roots = [f.roots(RR, multiplicities=False) for f in reals]                                            # needs sage.libs.flint
            sage: all(len(L) == 3 and all(x^2 <= 12 for x in L) for L in roots)                                         # needs sage.libs.flint
            True

        Finally, check that the original polynomials are reconstructed as CM
        polynomials::

            sage: all(f == T^3*r(T + 3/T) for (f, r) in zip(simples, reals))                                            # needs sage.libs.flint
            True

        A simple check (not sufficient)::

            sage: all(f.number_of_real_roots() == 0 for f in simples)                                                   # needs sage.libs.flint
            True
        """
    def construction(self):
        """
        Return the construction functor.

        EXAMPLES::

            sage: from sage.rings.polynomial.polynomial_ring import PolynomialRing_integral_domain as PRing
            sage: R = PRing(ZZ, 'x'); R
            Univariate Polynomial Ring in x over Integer Ring
            sage: functor, arg = R.construction(); functor, arg
            (Poly[x], Integer Ring)
            sage: functor.implementation is None
            True

            sage: # needs sage.libs.ntl
            sage: R = PRing(ZZ, 'x', implementation='NTL'); R
            Univariate Polynomial Ring in x over Integer Ring (using NTL)
            sage: functor, arg = R.construction(); functor, arg
            (Poly[x], Integer Ring)
            sage: functor.implementation
            'NTL'
        """

class PolynomialRing_field(PolynomialRing_integral_domain):
    def __init__(self, base_ring, name: str = 'x', sparse: bool = False, implementation=None, element_class=None, category=None) -> None:
        """
        TESTS::

            sage: from sage.rings.polynomial.polynomial_ring import PolynomialRing_field as PRing
            sage: R = PRing(QQ, 'x'); R
            Univariate Polynomial Ring in x over Rational Field
            sage: type(R.gen())                                                         # needs sage.libs.flint
            <class 'sage.rings.polynomial.polynomial_rational_flint.Polynomial_rational_flint'>
            sage: R = PRing(QQ, 'x', sparse=True); R
            Sparse Univariate Polynomial Ring in x over Rational Field
            sage: type(R.gen())
            <class 'sage.rings.polynomial.polynomial_ring.PolynomialRing_field_with_category.element_class'>

            sage: # needs sage.rings.real_mpfr
            sage: R = PRing(CC, 'x'); R
            Univariate Polynomial Ring in x over Complex Field with 53 bits of precision
            sage: type(R.gen())
            <class 'sage.rings.polynomial.polynomial_ring.PolynomialRing_field_with_category.element_class'>

        Demonstrate that :issue:`8762` is fixed::

            sage: R.<x> = PolynomialRing(GF(next_prime(10^20)), sparse=True)            # needs sage.rings.finite_rings
            sage: x^(10^20)  # this should be fast                                      # needs sage.rings.finite_rings
            x^100000000000000000000
        """
    def divided_difference(self, points, full_table: bool = False):
        '''
        Return the Newton divided-difference coefficients of the
        Lagrange interpolation polynomial through ``points``.

        INPUT:

        - ``points`` -- list of pairs `(x_0, y_0), (x_1, y_1),
          \\dots, (x_n, y_n)` of elements of the base ring of ``self``,
          where `x_i - x_j` is invertible for `i \\neq j`.  This method
          converts the `x_i` and `y_i` into the base ring of ``self``.

        - ``full_table`` -- boolean (default: ``False``); if ``True``,
          return the full divided-difference table.  If ``False``,
          only return entries along the main diagonal; these are the
          Newton divided-difference coefficients `F_{i,i}`.

        OUTPUT:

        The Newton divided-difference coefficients of the `n`-th
        Lagrange interpolation polynomial `P_n(x)` that passes through
        the points in ``points`` (see :meth:`lagrange_polynomial`).
        These are the coefficients `F_{0,0}, F_{1,1}, \\dots, F_{n,n}`
        in the base ring of ``self`` such that

        .. MATH::

            P_n(x) = \\sum_{i=0}^n F_{i,i} \\prod_{j=0}^{i-1} (x - x_j)

        EXAMPLES:

        Only return the divided-difference coefficients `F_{i,i}`.
        This example is taken from Example 1, page 121 of [BF2005]_::

            sage: # needs sage.rings.real_mpfr
            sage: points = [(1.0, 0.7651977), (1.3, 0.6200860), (1.6, 0.4554022),
            ....:           (1.9, 0.2818186), (2.2, 0.1103623)]
            sage: R = PolynomialRing(RR, "x")
            sage: R.divided_difference(points)
            [0.765197700000000,
             -0.483705666666666,
             -0.108733888888889,
             0.0658783950617283,
             0.00182510288066044]

        Now return the full divided-difference table::

            sage: # needs sage.rings.real_mpfr
            sage: points = [(1.0, 0.7651977), (1.3, 0.6200860), (1.6, 0.4554022),
            ....:           (1.9, 0.2818186), (2.2, 0.1103623)]
            sage: R = PolynomialRing(RR, "x")
            sage: R.divided_difference(points, full_table=True)
            [[0.765197700000000],
             [0.620086000000000, -0.483705666666666],
             [0.455402200000000, -0.548946000000000, -0.108733888888889],
             [0.281818600000000, -0.578612000000000,
                                -0.0494433333333339, 0.0658783950617283],
             [0.110362300000000, -0.571520999999999, 0.0118183333333349,
                                0.0680685185185209, 0.00182510288066044]]

        The following example is taken from Example 4.12, page 225 of
        [MF1999]_::

            sage: points = [(1, -3), (2, 0), (3, 15), (4, 48), (5, 105), (6, 192)]
            sage: R = PolynomialRing(QQ, "x")
            sage: R.divided_difference(points)
            [-3, 3, 6, 1, 0, 0]
            sage: R.divided_difference(points, full_table=True)
            [[-3],
             [0, 3],
             [15, 15, 6],
             [48, 33, 9, 1],
             [105, 57, 12, 1, 0],
             [192, 87, 15, 1, 0, 0]]
        '''
    def lagrange_polynomial(self, points, algorithm: str = 'divided_difference', previous_row=None):
        """
        Return the Lagrange interpolation polynomial through the
        given points.

        INPUT:

        - ``points`` -- list of pairs `(x_0, y_0), (x_1, y_1),
          \\dots, (x_n, y_n)` of elements of the base ring of ``self``,
          where `x_i - x_j` is invertible for `i \\neq j`.  This method
          converts the `x_i` and `y_i` into the base ring of ``self``.

        - ``algorithm`` -- (default: ``'divided_difference'``) one of
          the following:

          - ``'divided_difference'``: use the method of divided
            differences.

          - ``'neville'``: adapt Neville's method as
            described on page 144 of [BF2005]_ to recursively generate
            the Lagrange interpolation polynomial.  Neville's method
            generates a table of approximating polynomials, where the
            last row of that table contains the `n`-th Lagrange
            interpolation polynomial.  The adaptation implemented by
            this method is to only generate the last row of this
            table, instead of the full table itself.  Generating the
            full table can be memory inefficient.

          - ``'pari'``: use Pari's function :pari:`polinterpolate`

        - ``previous_row`` -- (default: ``None``) this option is only
          relevant if used with ``algorithm='neville'``.  If provided,
          this should be the last row of the table resulting from a
          previous use of Neville's method.  If such a row is passed,
          then ``points`` should consist of both previous and new
          interpolating points.  Neville's method will then use that
          last row and the interpolating points to generate a new row
          containing an interpolation polynomial for the new points.

        OUTPUT:

        The Lagrange interpolation polynomial through the points
        `(x_0, y_0), (x_1, y_1), \\dots, (x_n, y_n)`.  This is the
        unique polynomial `P_n` of degree at most `n` in ``self``
        satisfying `P_n(x_i) = y_i` for `0 \\le i \\le n`.

        EXAMPLES:

        By default, we use the method of divided differences::

            sage: R = PolynomialRing(QQ, 'x')
            sage: f = R.lagrange_polynomial([(0,1), (2,2), (3,-2), (-4,9)]); f
            -23/84*x^3 - 11/84*x^2 + 13/7*x + 1
            sage: f(0)
            1
            sage: f(2)
            2
            sage: f(3)
            -2
            sage: f(-4)
            9

            sage: # needs sage.rings.finite_rings
            sage: R = PolynomialRing(GF(2**3, 'a'), 'x')
            sage: a = R.base_ring().gen()
            sage: f = R.lagrange_polynomial([(a^2+a, a), (a, 1), (a^2, a^2+a+1)]); f
            a^2*x^2 + a^2*x + a^2
            sage: f(a^2 + a)
            a
            sage: f(a)
            1
            sage: f(a^2)
            a^2 + a + 1

        Now use a memory efficient version of Neville's method::

            sage: R = PolynomialRing(QQ, 'x')
            sage: R.lagrange_polynomial([(0,1), (2,2), (3,-2), (-4,9)],
            ....:                       algorithm='neville')
            [9,
            -11/7*x + 19/7,
            -17/42*x^2 - 83/42*x + 53/7,
            -23/84*x^3 - 11/84*x^2 + 13/7*x + 1]

            sage: # needs sage.rings.finite_rings
            sage: R = PolynomialRing(GF(2**3, 'a'), 'x')
            sage: a = R.base_ring().gen()
            sage: R.lagrange_polynomial([(a^2+a, a), (a, 1), (a^2, a^2+a+1)],
            ....:                       algorithm='neville')
            [a^2 + a + 1, x + a + 1, a^2*x^2 + a^2*x + a^2]

        Repeated use of Neville's method to get better Lagrange
        interpolation polynomials::

            sage: R = PolynomialRing(QQ, 'x')
            sage: p = R.lagrange_polynomial([(0,1), (2,2)], algorithm='neville')
            sage: R.lagrange_polynomial([(0,1), (2,2), (3,-2), (-4,9)],
            ....:                       algorithm='neville', previous_row=p)[-1]
            -23/84*x^3 - 11/84*x^2 + 13/7*x + 1

            sage: # needs sage.rings.finite_rings
            sage: R = PolynomialRing(GF(2**3, 'a'), 'x')
            sage: a = R.base_ring().gen()
            sage: p = R.lagrange_polynomial([(a^2+a, a), (a, 1)], algorithm='neville')
            sage: R.lagrange_polynomial([(a^2+a, a), (a, 1), (a^2, a^2+a+1)],
            ....:                       algorithm='neville', previous_row=p)[-1]
            a^2*x^2 + a^2*x + a^2

        One can also use ``Pari``'s implementation::

            sage: R = PolynomialRing(QQ, 'x')
            sage: data = [(0,1), (2,5), (3,10)]
            sage: p = R.lagrange_polynomial(data, algorithm='pari'); p
            x^2 + 1

        TESTS:

        The value for ``algorithm`` must be either
        ``'divided_difference'`` (default), ``'neville'`` or ``'pari'``::

            sage: R = PolynomialRing(QQ, 'x')
            sage: R.lagrange_polynomial([(0,1),(2,2),(3,-2),(-4,9)], algorithm='abc')
            Traceback (most recent call last):
            ...
            ValueError: algorithm can be 'divided_difference', 'neville' or 'pari'

        Make sure that :issue:`10304` is fixed.  The return value
        should always be an element of ``self`` in the case of
        ``divided_difference``, or a list of elements of ``self`` in
        the case of ``neville``::

            sage: R = PolynomialRing(QQ, 'x')
            sage: R.lagrange_polynomial([]).parent() == R
            True
            sage: R.lagrange_polynomial([(2, 3)]).parent() == R
            True
            sage: row = R.lagrange_polynomial([], algorithm='neville')
            sage: all(poly.parent() == R for poly in row)
            True
            sage: row = R.lagrange_polynomial([(2, 3)], algorithm='neville')
            sage: all(poly.parent() == R for poly in row)
            True

        Check that base fields of positive characteristic are treated
        correctly (see :issue:`9787`)::

            sage: R.<x> = GF(101)[]
            sage: R.lagrange_polynomial([[1, 0], [2, 0]])
            0
            sage: R.lagrange_polynomial([[1, 0], [2, 0], [3, 0]])
            0
        """
    @cached_method
    def fraction_field(self):
        """
        Return the fraction field of ``self``.

        EXAMPLES::

            sage: QQbar['x'].fraction_field()
            Fraction Field of Univariate Polynomial Ring in x over Algebraic
            Field

        TESTS:

        Check that :issue:`25449` has been resolved::

            sage: # needs sage.rings.finite_rings
            sage: k = GF(25453)
            sage: F.<x> = FunctionField(k)
            sage: R.<t> = k[]
            sage: t(x)
            x

            sage: # needs sage.rings.finite_rings
            sage: k = GF(55667)
            sage: F.<x> = FunctionField(k)
            sage: R.<t> = k[]
            sage: t(x)
            x

        Fixed :issue:`37374`::

            sage: x = PolynomialRing(GF(37), ['x'], sparse=True).fraction_field().gen()
            sage: type(x.numerator())
            <class 'sage.rings.polynomial.polynomial_ring.PolynomialRing_field_with_category.element_class'>
            sage: (x^8 + 16*x^6 + 4*x^4 + x^2 + 12).numerator() - 1
            x^8 + 16*x^6 + 4*x^4 + x^2 + 11
        """

class PolynomialRing_dense_finite_field(PolynomialRing_field):
    """
    Univariate polynomial ring over a finite field.

    EXAMPLES::

        sage: R = PolynomialRing(GF(27, 'a'), 'x')                                      # needs sage.rings.finite_rings
        sage: type(R)                                                                   # needs sage.rings.finite_rings
        <class 'sage.rings.polynomial.polynomial_ring.PolynomialRing_dense_finite_field_with_category'>
    """
    def __init__(self, base_ring, name: str = 'x', element_class=None, implementation=None) -> None:
        """
        TESTS::

            sage: from sage.rings.polynomial.polynomial_ring import PolynomialRing_dense_finite_field
            sage: R = PolynomialRing_dense_finite_field(GF(5), implementation='generic')
            sage: type(R(0))
            <class 'sage.rings.polynomial.polynomial_ring.PolynomialRing_dense_finite_field_with_category.element_class'>

            sage: S = PolynomialRing_dense_finite_field(GF(25, 'a'), implementation='NTL')          # needs sage.libs.ntl sage.rings.finite_rings
            sage: type(S(0))                                                                        # needs sage.libs.ntl sage.rings.finite_rings
            <class 'sage.rings.polynomial.polynomial_zz_pex.Polynomial_ZZ_pEX'>

            sage: S = PolynomialRing_dense_finite_field(GF(64), implementation='superfast')         # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: unknown implementation 'superfast' for dense polynomial rings over Finite Field in z6 of size 2^6
        """
    def irreducible_element(self, n, algorithm=None):
        """
        Construct a monic irreducible polynomial of degree `n`.

        INPUT:

        - ``n`` -- integer; degree of the polynomial to construct

        - ``algorithm`` -- string (algorithm to use) or ``None``:

          - ``'random'`` or ``None``:
            try random polynomials until an irreducible one is found

          - ``'first_lexicographic'``: try polynomials in
            lexicographic order until an irreducible one is found

        OUTPUT: a monic irreducible polynomial of degree `n` in ``self``

        EXAMPLES::

            sage: # needs sage.modules sage.rings.finite_rings
            sage: f = GF(5^3, 'a')['x'].irreducible_element(2)
            sage: f.degree()
            2
            sage: f.is_irreducible()
            True
            sage: R = GF(19)['x']
            sage: R.irreducible_element(21, algorithm='first_lexicographic')
            x^21 + x + 5
            sage: R = GF(5**2, 'a')['x']
            sage: R.irreducible_element(17, algorithm='first_lexicographic')
            x^17 + a*x + 4*a + 3

        AUTHORS:

        - Peter Bruin (June 2013)
        - Jean-Pierre Flori (May 2014)
        """

class PolynomialRing_cdvr(PolynomialRing_integral_domain):
    """
    A class for polynomial ring over complete discrete valuation rings
    """
    def __init__(self, base_ring, name=None, sparse: bool = False, implementation=None, element_class=None, category=None) -> None:
        """
        TESTS::

            sage: from sage.rings.polynomial.polynomial_ring import PolynomialRing_cdvr

            sage: S.<x> = ZZ[]
            sage: isinstance(S, PolynomialRing_cdvr)
            False

            sage: # needs sage.rings.padics
            sage: S.<x> = Zp(5)[]
            sage: isinstance(S, PolynomialRing_cdvr)
            True
        """

class PolynomialRing_cdvf(PolynomialRing_cdvr, PolynomialRing_field):
    """
    A class for polynomial ring over complete discrete valuation fields
    """
    def __init__(self, base_ring, name=None, sparse: bool = False, implementation=None, element_class=None, category=None) -> None:
        """
        TESTS::

            sage: from sage.rings.polynomial.polynomial_ring import PolynomialRing_cdvf

            sage: S.<x> = QQ[]
            sage: isinstance(S, PolynomialRing_cdvf)
            False

            sage: S.<x> = Qp(5)[]                                                       # needs sage.rings.padics
            sage: isinstance(S, PolynomialRing_cdvf)                                    # needs sage.rings.padics
            True
        """

class PolynomialRing_dense_padic_ring_generic(PolynomialRing_cdvr):
    """
    A class for dense polynomial ring over `p`-adic rings
    """
    def __init__(self, base_ring, name=None, implementation=None, element_class=None, category=None) -> None: ...

class PolynomialRing_dense_padic_field_generic(PolynomialRing_cdvf):
    """
    A class for dense polynomial ring over `p`-adic fields
    """
    def __init__(self, base_ring, name=None, implementation=None, element_class=None, category=None) -> None: ...

class PolynomialRing_dense_padic_ring_capped_relative(PolynomialRing_dense_padic_ring_generic):
    def __init__(self, base_ring, name=None, implementation=None, element_class=None, category=None) -> None:
        """
        TESTS::

            sage: from sage.rings.polynomial.polynomial_ring import PolynomialRing_dense_padic_ring_capped_relative as PRing
            sage: R = PRing(Zp(13), name='t'); R                                                                        # needs sage.rings.padics
            Univariate Polynomial Ring in t over 13-adic Ring with capped relative precision 20
            sage: type(R.gen())                                                                                         # needs sage.rings.padics
            <class 'sage.rings.polynomial.polynomial_ring.PolynomialRing_dense_padic_ring_capped_relative_with_category.element_class'>
        """

class PolynomialRing_dense_padic_ring_capped_absolute(PolynomialRing_dense_padic_ring_generic):
    def __init__(self, base_ring, name=None, implementation=None, element_class=None, category=None) -> None:
        """
        TESTS::

            sage: from sage.rings.polynomial.polynomial_ring import PolynomialRing_dense_padic_ring_capped_absolute as PRing
            sage: R = PRing(Zp(13, type='capped-abs'), name='t'); R                                                     # needs sage.rings.padics
            Univariate Polynomial Ring in t over 13-adic Ring with capped absolute precision 20
            sage: type(R.gen())                                                                                         # needs sage.rings.padics
            <class 'sage.rings.polynomial.polynomial_ring.PolynomialRing_dense_padic_ring_capped_absolute_with_category.element_class'>
        """

class PolynomialRing_dense_padic_ring_fixed_mod(PolynomialRing_dense_padic_ring_generic):
    def __init__(self, base_ring, name=None, implementation=None, element_class=None, category=None) -> None:
        """
        TESTS::

            sage: from sage.rings.polynomial.polynomial_ring import PolynomialRing_dense_padic_ring_fixed_mod as PRing
            sage: R = PRing(Zp(13, type='fixed-mod'), name='t'); R                                                      # needs sage.rings.padics
            Univariate Polynomial Ring in t over 13-adic Ring of fixed modulus 13^20

            sage: type(R.gen())                                                                                         # needs sage.rings.padics
            <class 'sage.rings.polynomial.polynomial_ring.PolynomialRing_dense_padic_ring_fixed_mod_with_category.element_class'>
        """

class PolynomialRing_dense_padic_field_capped_relative(PolynomialRing_dense_padic_field_generic):
    def __init__(self, base_ring, name=None, implementation=None, element_class=None, category=None) -> None:
        """
        TESTS::

            sage: from sage.rings.polynomial.polynomial_ring import PolynomialRing_dense_padic_field_capped_relative as PRing
            sage: R = PRing(Qp(13), name='t'); R                                                                        # needs sage.rings.padics
            Univariate Polynomial Ring in t over 13-adic Field with capped relative precision 20
            sage: type(R.gen())                                                                                         # needs sage.rings.padics
            <class 'sage.rings.polynomial.polynomial_ring.PolynomialRing_dense_padic_field_capped_relative_with_category.element_class'>
        """

class PolynomialRing_dense_mod_n(PolynomialRing_commutative):
    def __init__(self, base_ring, name=None, element_class=None, implementation=None, category=None) -> None:
        """
        TESTS::

            sage: from sage.rings.polynomial.polynomial_ring import PolynomialRing_dense_mod_n as PRing
            sage: R = PRing(Zmod(15), 'x'); R
            Univariate Polynomial Ring in x over Ring of integers modulo 15
            sage: type(R.gen())                                                                                         # needs sage.libs.flint
            <class 'sage.rings.polynomial.polynomial_zmod_flint.Polynomial_zmod_flint'>

            sage: R = PRing(Zmod(15), 'x', implementation='NTL'); R                                                     # needs sage.libs.ntl
            Univariate Polynomial Ring in x over Ring of integers modulo 15 (using NTL)
            sage: type(R.gen())                                                                                         # needs sage.libs.ntl
            <class 'sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_modn_ntl_zz'>

            sage: R = PRing(Zmod(2**63*3), 'x', implementation='NTL'); R                                                # needs sage.libs.ntl
            Univariate Polynomial Ring in x over Ring of integers modulo 27670116110564327424 (using NTL)
            sage: type(R.gen())                                                                                         # needs sage.libs.ntl
            <class 'sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_modn_ntl_ZZ'>

            sage: R = PRing(Zmod(2**63*3), 'x', implementation='FLINT')
            Traceback (most recent call last):
            ...
            ValueError: FLINT does not support modulus 27670116110564327424

            sage: R = PRing(Zmod(2**63*3), 'x'); R                                                                      # needs sage.libs.ntl
            Univariate Polynomial Ring in x over Ring of integers modulo 27670116110564327424 (using NTL)
            sage: type(R.gen())                                                                                         # needs sage.libs.ntl
            <class 'sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_modn_ntl_ZZ'>
        """
    @cached_method
    def modulus(self):
        """
        EXAMPLES::

            sage: R.<x> = Zmod(15)[]
            sage: R.modulus()
            15
        """
    def residue_field(self, ideal, names=None):
        """
        Return the residue finite field at the given ideal.

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: R.<t> = GF(2)[]
            sage: k.<a> = R.residue_field(t^3 + t + 1); k
            Residue field in a
             of Principal ideal (t^3 + t + 1) of Univariate Polynomial Ring in t
             over Finite Field of size 2 (using GF2X)
            sage: k.list()
            [0, a, a^2, a + 1, a^2 + a, a^2 + a + 1, a^2 + 1, 1]
            sage: R.residue_field(t)
            Residue field of Principal ideal (t) of Univariate Polynomial Ring in t
             over Finite Field of size 2 (using GF2X)
            sage: P = R.irreducible_element(8) * R
            sage: P
            Principal ideal (t^8 + t^4 + t^3 + t^2 + 1) of Univariate Polynomial Ring in t
             over Finite Field of size 2 (using GF2X)
            sage: k.<a> = R.residue_field(P); k
            Residue field in a
             of Principal ideal (t^8 + t^4 + t^3 + t^2 + 1) of Univariate Polynomial Ring in t
             over Finite Field of size 2 (using GF2X)
            sage: k.cardinality()
            256

        Non-maximal ideals are not accepted::

            sage: # needs sage.libs.ntl
            sage: R.residue_field(t^2 + 1)
            Traceback (most recent call last):
            ...
            ArithmeticError: ideal is not maximal
            sage: R.residue_field(0)
            Traceback (most recent call last):
            ...
            ArithmeticError: ideal is not maximal
            sage: R.residue_field(1)
            Traceback (most recent call last):
            ...
            ArithmeticError: ideal is not maximal
        """

class PolynomialRing_dense_mod_p(PolynomialRing_dense_finite_field, PolynomialRing_dense_mod_n, PolynomialRing_singular_repr):
    def __init__(self, base_ring, name: str = 'x', implementation=None, element_class=None, category=None) -> None:
        """
        TESTS::

            sage: P = GF(2)['x']; P                                                     # needs sage.libs.ntl
            Univariate Polynomial Ring in x over Finite Field of size 2 (using GF2X)
            sage: type(P.gen())                                                         # needs sage.libs.ntl
            <class 'sage.rings.polynomial.polynomial_gf2x.Polynomial_GF2X'>

            sage: from sage.rings.polynomial.polynomial_ring import PolynomialRing_dense_mod_p
            sage: P = PolynomialRing_dense_mod_p(GF(5), 'x'); P
            Univariate Polynomial Ring in x over Finite Field of size 5
            sage: type(P.gen())                                                         # needs sage.libs.flint
            <class 'sage.rings.polynomial.polynomial_zmod_flint.Polynomial_zmod_flint'>

            sage: # needs sage.libs.ntl
            sage: P = PolynomialRing_dense_mod_p(GF(5), 'x', implementation='NTL'); P
            Univariate Polynomial Ring in x over Finite Field of size 5 (using NTL)
            sage: type(P.gen())
            <class 'sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_mod_p'>

            sage: P = PolynomialRing_dense_mod_p(GF(9223372036854775837), 'x'); P       # needs sage.libs.ntl sage.rings.finite_rings
            Univariate Polynomial Ring in x over Finite Field of size 9223372036854775837 (using NTL)
            sage: type(P.gen())                                                         # needs sage.libs.ntl sage.rings.finite_rings
            <class 'sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_mod_p'>

        This caching bug was fixed in :issue:`24264`::

            sage: # needs sage.rings.finite_rings
            sage: p = 2^64 + 13
            sage: A = GF(p^2)
            sage: B = GF(p^3)
            sage: R = A.modulus().parent()
            sage: S = B.modulus().parent()
            sage: R is S
            True
        """
    def irreducible_element(self, n, algorithm=None):
        '''
        Construct a monic irreducible polynomial of degree `n`.

        INPUT:

        - ``n`` -- integer; the degree of the polynomial to construct

        - ``algorithm`` -- string (algorithm to use) or ``None``;
          currently available options are:

          - ``\'adleman-lenstra\'``: a variant of the Adleman--Lenstra
            algorithm as implemented in PARI.

          - ``\'conway\'``: look up the Conway polynomial of degree `n`
            over the field of `p` elements in the database; raise a
            :exc:`RuntimeError` if it is not found.

          - ``\'ffprimroot\'``: use the :pari:`ffprimroot` function from
            PARI.

          - ``\'first_lexicographic\'``: return the lexicographically
            smallest irreducible polynomial of degree `n`.

          - ``\'minimal_weight\'``: return an irreducible polynomial of
            degree `n` with minimal number of non-zero coefficients.
            Only implemented for `p = 2`.

          - ``\'primitive\'``: return a polynomial `f` such that a root of
            `f` generates the multiplicative group of the finite field
            extension defined by `f`. This uses the Conway polynomial if
            possible, otherwise it uses ``\'ffprimroot\'``.

          - ``\'random\'``: try random polynomials until an irreducible
            one is found.

          If ``algorithm`` is ``None``, use `x - 1` in degree 1. In
          degree > 1, the Conway polynomial is used if it is found in
          the database.  Otherwise, the algorithm ``minimal_weight``
          is used if `p = 2`, and the algorithm ``\'adleman-lenstra\'`` if
          `p > 2`.

        OUTPUT: a monic irreducible polynomial of degree `n` in ``self``

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: GF(5)[\'x\'].irreducible_element(2)
            x^2 + 4*x + 2
            sage: GF(5)[\'x\'].irreducible_element(2, algorithm=\'adleman-lenstra\')
            x^2 + x + 1
            sage: GF(5)[\'x\'].irreducible_element(2, algorithm=\'primitive\')
            x^2 + 4*x + 2
            sage: GF(5)[\'x\'].irreducible_element(32, algorithm=\'first_lexicographic\')
            x^32 + 2
            sage: GF(5)[\'x\'].irreducible_element(32, algorithm=\'conway\')
            Traceback (most recent call last):
            ...
            RuntimeError: requested Conway polynomial not in database.
            sage: GF(5)[\'x\'].irreducible_element(32, algorithm=\'primitive\')
            x^32 + ...

        In characteristic 2::

            sage: GF(2)[\'x\'].irreducible_element(33)                                    # needs sage.rings.finite_rings
            x^33 + x^13 + x^12 + x^11 + x^10 + x^8 + x^6 + x^3 + 1
            sage: GF(2)[\'x\'].irreducible_element(33, algorithm=\'minimal_weight\')        # needs sage.rings.finite_rings
            x^33 + x^10 + 1

        In degree 1::

            sage: GF(97)[\'x\'].irreducible_element(1)                                    # needs sage.rings.finite_rings
            x + 96
            sage: GF(97)[\'x\'].irreducible_element(1, algorithm=\'conway\')                # needs sage.rings.finite_rings
            x + 92
            sage: GF(97)[\'x\'].irreducible_element(1, algorithm=\'adleman-lenstra\')       # needs sage.rings.finite_rings
            x

        AUTHORS:

        - Peter Bruin (June 2013)

        - Jeroen Demeyer (September 2014): add "ffprimroot" algorithm,
          see :issue:`8373`.
        '''
    @cached_method
    def fraction_field(self):
        """
        Return the fraction field of ``self``.

        EXAMPLES::

            sage: R.<t> = GF(5)[]
            sage: R.fraction_field()
            Fraction Field of Univariate Polynomial Ring in t
             over Finite Field of size 5
        """

def polygen(ring_or_element, name: str = 'x'):
    """
    Return a polynomial indeterminate.

    INPUT:

    - ``polygen(base_ring, name='x')``

    - ``polygen(ring_element, name='x')``

    If the first input is a ring, return a polynomial generator over
    that ring. If it is a ring element, return a polynomial generator
    over the parent of the element.

    EXAMPLES::

        sage: z = polygen(QQ, 'z')
        sage: z^3 + z +1
        z^3 + z + 1
        sage: parent(z)
        Univariate Polynomial Ring in z over Rational Field

    .. NOTE::

       If you give a list or comma-separated string to :func:`polygen`, you'll
       get a tuple of indeterminates, exactly as if you called
       :func:`polygens`.
    """
def polygens(base_ring, names: str = 'x', *args):
    """
    Return indeterminates over the given base ring with the given
    names.

    EXAMPLES::

        sage: x,y,z = polygens(QQ,'x,y,z')
        sage: (x+y+z)^2
        x^2 + 2*x*y + y^2 + 2*x*z + 2*y*z + z^2
        sage: parent(x)
        Multivariate Polynomial Ring in x, y, z over Rational Field
        sage: t = polygens(QQ, ['x','yz','abc'])
        sage: t
        (x, yz, abc)

    The number of generators can be passed as a third argument::

        sage: polygens(QQ, 'x', 4)
        (x0, x1, x2, x3)
    """
