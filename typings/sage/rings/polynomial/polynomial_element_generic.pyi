from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.rings.infinity import Infinity as Infinity, infinity as infinity
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.padics.precision_error import PrecisionError as PrecisionError
from sage.rings.polynomial.polynomial_element import Polynomial as Polynomial, Polynomial_generic_dense as Polynomial_generic_dense, Polynomial_generic_dense_inexact as Polynomial_generic_dense_inexact
from sage.rings.polynomial.polynomial_rational_flint import Polynomial_rational_flint as Polynomial_rational_flint
from sage.rings.polynomial.polynomial_singular_interface import Polynomial_singular_repr as Polynomial_singular_repr
from sage.structure.element import EuclideanDomainElement as EuclideanDomainElement, IntegralDomainElement as IntegralDomainElement, coerce_binop as coerce_binop, parent as parent
from sage.structure.factorization import Factorization as Factorization
from sage.structure.richcmp import rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_item as richcmp_item

class Polynomial_generic_sparse(Polynomial):
    """
    A generic sparse polynomial.

    The ``Polynomial_generic_sparse`` class defines functionality for sparse
    polynomials over any base ring. A sparse polynomial is represented using a
    dictionary which maps each exponent to the corresponding coefficient. The
    coefficients must never be zero.

    EXAMPLES::

        sage: R.<x> = PolynomialRing(PolynomialRing(QQ, 'y'), sparse=True)
        sage: f = x^3 - x + 17
        sage: type(f)
        <class 'sage.rings.polynomial.polynomial_ring.PolynomialRing_integral_domain_with_category.element_class'>
        sage: loads(f.dumps()) == f
        True

    A more extensive example::

        sage: # needs sage.libs.pari
        sage: A.<T> = PolynomialRing(Integers(5), sparse=True)
        sage: f = T^2 + 1; B = A.quo(f)
        sage: C.<s> = PolynomialRing(B)
        sage: C
        Univariate Polynomial Ring in s over Univariate Quotient Polynomial Ring in Tbar
         over Ring of integers modulo 5 with modulus T^2 + 1
        sage: s + T
        s + Tbar
        sage: (s + T)**2
        s^2 + 2*Tbar*s + 4
    """
    def __init__(self, parent, x=None, check: bool = True, is_gen: bool = False, construct: bool = False) -> None:
        """
        TESTS::

            sage: PolynomialRing(RIF, 'z', sparse=True)([RIF(-1, 1), RIF(-1,1)])                    # needs sage.rings.real_interval_field
            0.?*z + 0.?
            sage: PolynomialRing(RIF, 'z', sparse=True)((RIF(-1, 1), RIF(-1,1)))                    # needs sage.rings.real_interval_field
            0.?*z + 0.?
            sage: PolynomialRing(CIF, 'z', sparse=True)([CIF(RIF(-1,1), RIF(-1,1)), RIF(-1,1)])     # needs sage.rings.complex_interval_field
            0.?*z + 0.? + 0.?*I
        """
    def monomial_coefficients(self, copy=None):
        """
        Return a new copy of the dict of the underlying
        elements of ``self``.

        EXAMPLES::

            sage: R.<w> = PolynomialRing(Integers(8), sparse=True)
            sage: f = 5 + w^1997 - w^10000; f
            7*w^10000 + w^1997 + 5
            sage: d = f.monomial_coefficients(); d
            {0: 5, 1997: 1, 10000: 7}
            sage: d[0] = 10
            sage: f.monomial_coefficients()
            {0: 5, 1997: 1, 10000: 7}

        ``dict`` is an alias::

            sage: f.dict()
            {0: 5, 1997: 1, 10000: 7}
        """
    dict = monomial_coefficients
    def coefficients(self, sparse: bool = True):
        """
        Return the coefficients of the monomials appearing in ``self``.

        EXAMPLES::

            sage: R.<w> = PolynomialRing(Integers(8), sparse=True)
            sage: f = 5 + w^1997 - w^10000; f
            7*w^10000 + w^1997 + 5
            sage: f.coefficients()
            [5, 1, 7]

        TESTS:

        Check that all coefficients are in the base ring::

            sage: S.<x> = PolynomialRing(QQ, sparse=True)
            sage: f = x^4
            sage: all(c.parent() is QQ for c in f.coefficients(False))
            True
        """
    def exponents(self):
        """
        Return the exponents of the monomials appearing in ``self``.

        EXAMPLES::

            sage: R.<w> = PolynomialRing(Integers(8), sparse=True)
            sage: f = 5 + w^1997 - w^10000; f
            7*w^10000 + w^1997 + 5
            sage: f.exponents()
            [0, 1997, 10000]
        """
    def valuation(self, p=None):
        """
        Return the valuation of ``self``.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: R.<w> = PolynomialRing(GF(9, 'a'), sparse=True)
            sage: f = w^1997 - w^10000
            sage: f.valuation()
            1997
            sage: R(19).valuation()
            0
            sage: R(0).valuation()
            +Infinity
        """
    def integral(self, var=None):
        """
        Return the integral of this polynomial.

        By default, the integration variable is the variable of the
        polynomial.

        Otherwise, the integration variable is the optional parameter ``var``

        .. NOTE::

            The integral is always chosen so that the constant term is 0.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ, sparse=True)
            sage: (1 + 3*x^10 - 2*x^100).integral()
            -2/101*x^101 + 3/11*x^11 + x

        TESTS:

        Check that :issue:`18600` is fixed::

            sage: R.<x> = PolynomialRing(ZZ, sparse=True)
            sage: (x^2^100).integral()
            1/1267650600228229401496703205377*x^1267650600228229401496703205377

        Check the correctness when the base ring is a polynomial ring::

            sage: R.<x> = PolynomialRing(ZZ, sparse=True)
            sage: S.<t> = PolynomialRing(R, sparse=True)
            sage: (x*t+1).integral()
            1/2*x*t^2 + t
            sage: (x*t+1).integral(x)
            1/2*x^2*t + x

        Check the correctness when the base ring is not an integral domain::

            sage: R.<x> = PolynomialRing(Zmod(4), sparse=True)
            sage: (x^4 + 2*x^2  + 3).integral()
            x^5 + 2*x^3 + 3*x
            sage: x.integral()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: inverse of Mod(2, 4) does not exist
        """
    def __getitem__(self, n):
        '''
        Return the `n`-th coefficient of this polynomial.

        Negative indexes are allowed and always return 0 (so you can
        view the polynomial as embedding Laurent series).

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: R.<w> = PolynomialRing(RDF, sparse=True)
            sage: e = RDF(e)
            sage: f = sum(e^n*w^n for n in range(4)); f   # abs tol 1.1e-14
            20.085536923187664*w^3 + 7.3890560989306495*w^2 + 2.718281828459045*w + 1.0
            sage: f[1]  # abs tol 5e-16
            2.718281828459045
            sage: f[5]
            0.0
            sage: f[-1]
            0.0

            sage: R.<x> = PolynomialRing(RealField(19), sparse=True)                    # needs sage.rings.real_mpfr
            sage: f = (2-3.5*x)^3; f                                                    # needs sage.rings.real_mpfr
            -42.875*x^3 + 73.500*x^2 - 42.000*x + 8.0000

        Using slices, we can truncate polynomials::

            sage: f[:2]                                                                 # needs sage.rings.real_mpfr
            -42.000*x + 8.0000

        Any other kind of slicing is an error, see :issue:`18940`::

            sage: f[1:3]                                                                # needs sage.rings.real_mpfr
            Traceback (most recent call last):
            ...
            IndexError: polynomial slicing with a start is not defined

            sage: f[1:3:2]                                                              # needs sage.rings.real_mpfr
            Traceback (most recent call last):
            ...
            IndexError: polynomial slicing with a step is not defined

        TESTS::

            sage: f["hello"]                                                            # needs sage.rings.real_mpfr
            Traceback (most recent call last):
            ...
            TypeError: list indices must be integers, not str
        '''
    def list(self, copy: bool = True):
        """
        Return a new copy of the list of the underlying
        elements of ``self``.

        EXAMPLES::

            sage: R.<z> = PolynomialRing(Integers(100), sparse=True)
            sage: f = 13*z^5 + 15*z^2 + 17*z
            sage: f.list()
            [0, 17, 15, 0, 0, 13]
        """
    def degree(self, gen=None):
        """
        Return the degree of this sparse polynomial.

        EXAMPLES::

            sage: R.<z> = PolynomialRing(ZZ, sparse=True)
            sage: f = 13*z^50000 + 15*z^2 + 17*z
            sage: f.degree()
            50000
        """
    def __floordiv__(self, right):
        """
        Return the quotient upon division (no remainder).

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<x> = PolynomialRing(QQbar, sparse=True)
            sage: f = (1+2*x)^3 + 3*x; f
            8*x^3 + 12*x^2 + 9*x + 1
            sage: g = f // (1+2*x); g
            4*x^2 + 4*x + 5/2
            sage: f - g * (1+2*x)
            -3/2
            sage: f.quo_rem(1+2*x)
            (4*x^2 + 4*x + 5/2, -3/2)
        """
    def shift(self, n):
        """
        Return this polynomial multiplied by the power `x^n`.

        If `n` is negative, terms below `x^n` will be discarded. Does
        not change this polynomial.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ, sparse=True)
            sage: p = x^100000 + 2*x + 4
            sage: type(p)
            <class 'sage.rings.polynomial.polynomial_ring.PolynomialRing_integral_domain_with_category.element_class'>
            sage: p.shift(0)
             x^100000 + 2*x + 4
            sage: p.shift(-1)
             x^99999 + 2
            sage: p.shift(-100002)
             0
            sage: p.shift(2)
             x^100002 + 2*x^3 + 4*x^2

        TESTS:

        Check that :issue:`18600` is fixed::

            sage: R.<x> = PolynomialRing(ZZ, sparse=True)
            sage: p = x^2^100 - 5
            sage: p.shift(10)
            x^1267650600228229401496703205386 - 5*x^10
            sage: p.shift(-10)
            x^1267650600228229401496703205366
            sage: p.shift(1.5)                                                          # needs sage.rings.real_mpfr
            Traceback (most recent call last):
            ...
            TypeError: Attempt to coerce non-integral RealNumber to Integer

        AUTHOR:
        - David Harvey (2006-08-06)
        """
    @coerce_binop
    def quo_rem(self, other):
        """
        Return the quotient and remainder of the Euclidean division of
        ``self`` and ``other``.

        Raises :exc:`ZeroDivisionError` if ``other`` is zero.

        Raises :exc:`ArithmeticError` if ``other`` has a nonunit leading
        coefficient and this causes the Euclidean division to fail.

        EXAMPLES::

            sage: P.<x> = PolynomialRing(ZZ, sparse=True)
            sage: R.<y> = PolynomialRing(P, sparse=True)
            sage: f = R.random_element(10)
            sage: while x.divides(f.leading_coefficient()):
            ....:     f = R.random_element(10)
            sage: g = y^5 + R.random_element(4)
            sage: q, r = f.quo_rem(g)
            sage: f == q*g + r and r.degree() < g.degree()
            True
            sage: g = x*y^5
            sage: f.quo_rem(g)
            Traceback (most recent call last):
            ...
            ArithmeticError: Division non exact
            (consider coercing to polynomials over the fraction field)
            sage: g = 0
            sage: f.quo_rem(g)
            Traceback (most recent call last):
            ...
            ZeroDivisionError: Division by zero polynomial

        If the leading coefficient of ``other`` is not a unit, Euclidean division may still work::

            sage: f = -x*y^10 + 2*x*y^7 + y^3 - 2*x^2*y^2 - y
            sage: g = x*y^5
            sage: f.quo_rem(g)
            (-y^5 + 2*y^2, y^3 - 2*x^2*y^2 - y)

        Polynomials over noncommutative rings are also allowed::

            sage: # needs sage.combinat sage.modules
            sage: HH = QuaternionAlgebra(QQ, -1, -1)
            sage: P.<x> = PolynomialRing(HH, sparse=True)
            sage: f = P.random_element(5)
            sage: g = P.random_element((0, 5))
            sage: q, r = f.quo_rem(g)
            sage: f == q*g + r
            True

        TESTS::

            sage: P.<x> = PolynomialRing(ZZ, sparse=True)
            sage: f = x^10 - 4*x^6 - 5
            sage: g = 17*x^22 + x^15 - 3*x^5 + 1
            sage: q, r = g.quo_rem(f)
            sage: g == f*q + r and r.degree() < f.degree()
            True
            sage: zero = P(0)
            sage: zero.quo_rem(f)
            (0, 0)
            sage: Q.<y> = IntegerModRing(14)[]
            sage: f = y^10 - 4*y^6 - 5
            sage: g = 17*y^22 + y^15 - 3*y^5 + 1
            sage: q, r = g.quo_rem(f)
            sage: g == f*q + r and r.degree() < f.degree()
            True
            sage: f += 2*y^10  # 3 is invertible mod 14
            sage: q, r = g.quo_rem(f)
            sage: g == f*q + r and r.degree() < f.degree()
            True

        The following shows that :issue:`16649` is indeed fixed. ::

            sage: P.<x> = PolynomialRing(ZZ, sparse=True)
            sage: (4*x).quo_rem(2*x)
            (2, 0)

        AUTHORS:

        - Bruno Grenet (2014-07-09)
        """
    @coerce_binop
    def gcd(self, other, algorithm=None):
        '''
        Return the gcd of this polynomial and ``other``.

        INPUT:

        - ``other`` -- a polynomial defined over the same ring as this
          polynomial

        ALGORITHM:

        Two algorithms are provided:

        - ``\'generic\'`` -- uses the generic implementation, which depends on the
          base ring being a UFD or a field
        - ``\'dense\'`` -- the polynomials are converted to the dense
          representation, their gcd is computed and is converted back to the
          sparse representation

        Default is ``\'dense\'`` for polynomials over `\\ZZ` and ``\'generic\'`` in the
        other cases.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ, sparse=True)
            sage: p = x^6 + 7*x^5 + 8*x^4 + 6*x^3 + 2*x^2 + x + 2
            sage: q = 2*x^4 - x^3 - 2*x^2 - 4*x - 1
            sage: gcd(p, q)
            x^2 + x + 1
            sage: gcd(p, q, algorithm=\'dense\')
            x^2 + x + 1
            sage: gcd(p, q, algorithm=\'generic\')
            x^2 + x + 1
            sage: gcd(p, q, algorithm=\'foobar\')
            Traceback (most recent call last):
            ...
            ValueError: Unknown algorithm \'foobar\'

        TESTS:

        Check that :issue:`19676` is fixed::

            sage: S.<y> = R[]
            sage: x.gcd(y)
            1
            sage: (6*x).gcd(9)
            3

        Check that :issue:`36427` is fixed::

            sage: P = PolynomialRing(ZZ, "q", sparse=True)
            sage: q = P.gen()
            sage: 2*q^-100
            2/q^100
            sage: gcd(1, q^100)
            1
            sage: gcd(q^0, q^100)
            1
        '''
    def reverse(self, degree=None):
        """
        Return this polynomial but with the coefficients reversed.

        If an optional degree argument is given, the coefficient list will be
        truncated or zero padded as necessary and the reverse polynomial will
        have the specified degree.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ, sparse=True)
            sage: p = x^4 + 2*x^2^100
            sage: p.reverse()
            x^1267650600228229401496703205372 + 2
            sage: p.reverse(10)
            x^6
        """
    def truncate(self, n):
        """
        Return the polynomial of degree `< n` equal to ``self`` modulo `x^n`.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ, sparse=True)
            sage: (x^11 + x^10 + 1).truncate(11)
            x^10 + 1
            sage: (x^2^500 + x^2^100 + 1).truncate(2^101)
            x^1267650600228229401496703205376 + 1
        """
    def number_of_terms(self):
        """
        Return the number of nonzero terms.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ, sparse=True)
            sage: p = x^100 - 3*x^10 + 12
            sage: p.number_of_terms()
            3
        """

class Polynomial_generic_domain(Polynomial, IntegralDomainElement):
    def __init__(self, parent, is_gen: bool = False, construct: bool = False) -> None: ...
    def is_unit(self):
        """
        Return ``True`` if this polynomial is a unit.

        *EXERCISE* (Atiyah-McDonald, Ch 1): Let `A[x]` be a polynomial
        ring in one variable.  Then `f=\\sum a_i x^i \\in A[x]` is a
        unit if and only if `a_0` is a unit and `a_1,\\ldots, a_n` are
        nilpotent.

        EXAMPLES::

            sage: R.<z> = PolynomialRing(ZZ, sparse=True)
            sage: (2 + z^3).is_unit()
            False
            sage: f = -1 + 3*z^3; f
            3*z^3 - 1
            sage: f.is_unit()
            False
            sage: R(-3).is_unit()
            False
            sage: R(-1).is_unit()
            True
            sage: R(0).is_unit()
            False
        """

class Polynomial_generic_field(Polynomial_singular_repr, Polynomial_generic_domain, EuclideanDomainElement):
    @coerce_binop
    def quo_rem(self, other):
        """
        Return a tuple ``(quotient, remainder)`` where
        ``self = quotient * other + remainder``.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<y> = PolynomialRing(QQ)
            sage: K.<t> = NumberField(y^2 - 2)
            sage: P.<x> = PolynomialRing(K)
            sage: x.quo_rem(K(1))
            (x, 0)
            sage: x.xgcd(K(1))
            (1, 0, 1)
        """

class Polynomial_generic_sparse_field(Polynomial_generic_sparse, Polynomial_generic_field):
    """
    EXAMPLES::

        sage: R.<x> = PolynomialRing(Frac(RR['t']), sparse=True)
        sage: f = x^3 - x + 17
        sage: type(f)
        <class 'sage.rings.polynomial.polynomial_ring.PolynomialRing_field_with_category.element_class'>
        sage: loads(f.dumps()) == f
        True
    """
    def __init__(self, parent, x=None, check: bool = True, is_gen: bool = False, construct: bool = False) -> None: ...

class Polynomial_generic_dense_field(Polynomial_generic_dense, Polynomial_generic_field):
    def __init__(self, parent, x=None, check: bool = True, is_gen: bool = False, construct: bool = False) -> None: ...

class Polynomial_generic_cdv(Polynomial_generic_domain):
    """
    A generic class for polynomials over complete discrete
    valuation domains and fields.

    AUTHOR:

    - Xavier Caruso (2013-03)
    """
    def newton_slopes(self, repetition: bool = True):
        """
        Return a list of the Newton slopes of this polynomial.

        These are the valuations of the roots of this polynomial.

        If ``repetition`` is ``True``, each slope is repeated a number of
        times equal to its multiplicity. Otherwise it appears only
        one time.

        EXAMPLES::

            sage: # needs sage.geometry.polyhedron sage.rings.padics
            sage: K = Qp(5)
            sage: R.<t> = K[]
            sage: f = 5 + 3*t + t^4 + 25*t^10
            sage: f.newton_polygon()
            Finite Newton polygon with 4 vertices: (0, 1), (1, 0), (4, 0), (10, 2)
            sage: f.newton_slopes()
            [1, 0, 0, 0, -1/3, -1/3, -1/3, -1/3, -1/3, -1/3]
            sage: f.newton_slopes(repetition=False)
            [1, 0, -1/3]

        AUTHOR:

        - Xavier Caruso (2013-03-20)
        """
    def newton_polygon(self):
        """
        Return a list of vertices of the Newton polygon of this polynomial.

        .. NOTE::

            If some coefficients have not enough precision an error is raised.

        EXAMPLES::

            sage: # needs sage.geometry.polyhedron sage.rings.padics
            sage: K = Qp(5)
            sage: R.<t> = K[]
            sage: f = 5 + 3*t + t^4 + 25*t^10
            sage: f.newton_polygon()
            Finite Newton polygon with 4 vertices: (0, 1), (1, 0), (4, 0), (10, 2)
            sage: g = f + K(0,0)*t^4; g
            (5^2 + O(5^22))*t^10 + O(5^0)*t^4 + (3 + O(5^20))*t + 5 + O(5^21)
            sage: g.newton_polygon()
            Traceback (most recent call last):
            ...
            PrecisionError: The coefficient of t^4 has not enough precision

        TESTS:

        Check that :issue:`22936` is fixed::

            sage: S.<x> = PowerSeriesRing(GF(5))
            sage: R.<y> = S[]
            sage: p = x^2 + y + x*y^2
            sage: p.newton_polygon()                                                    # needs sage.geometry.polyhedron
            Finite Newton polygon with 3 vertices: (0, 2), (1, 0), (2, 1)

        AUTHOR:

        - Xavier Caruso (2013-03-20)
        """
    def hensel_lift(self, a):
        """
        Lift `a` to a root of this polynomial (using
        Newton iteration).

        If `a` is not close enough to a root (so that
        Newton iteration does not converge), an error
        is raised.

        EXAMPLES::

            sage: # needs sage.rings.padics
            sage: K = Qp(5, 10)
            sage: P.<x> = PolynomialRing(K)
            sage: f = x^2 + 1
            sage: root = f.hensel_lift(2); root
            2 + 5 + 2*5^2 + 5^3 + 3*5^4 + 4*5^5 + 2*5^6 + 3*5^7 + 3*5^9 + O(5^10)
            sage: f(root)
            O(5^10)

            sage: g = (x^2 + 1) * (x - 7)                                               # needs sage.rings.padics
            sage: g.hensel_lift(2)  # here, 2 is a multiple root modulo p               # needs sage.rings.padics
            Traceback (most recent call last):
            ...
            ValueError: a is not close enough to a root of this polynomial

        AUTHOR:

        - Xavier Caruso (2013-03-23)
        """
    def factor_of_slope(self, slope=None):
        """
        INPUT:

        - ``slope`` -- a rational number (default: the first slope
          in the Newton polygon of ``self``)

        OUTPUT:

        The factor of ``self`` corresponding to the slope ``slope`` (i.e.
        the unique monic divisor of ``self`` whose slope is ``slope`` and
        degree is the length of ``slope`` in the Newton polygon).

        EXAMPLES::

            sage: # needs sage.geometry.polyhedron sage.rings.padics
            sage: K = Qp(5)
            sage: R.<x> = K[]
            sage: K = Qp(5)
            sage: R.<t> = K[]
            sage: f = 5 + 3*t + t^4 + 25*t^10
            sage: f.newton_slopes()
            [1, 0, 0, 0, -1/3, -1/3, -1/3, -1/3, -1/3, -1/3]
            sage: g = f.factor_of_slope(0)
            sage: g.newton_slopes()
            [0, 0, 0]
            sage: (f % g).is_zero()
            True
            sage: h = f.factor_of_slope()
            sage: h.newton_slopes()
            [1]
            sage: (f % h).is_zero()
            True

        If ``slope`` is not a slope of ``self``, the corresponding factor
        is `1`::

            sage: f.factor_of_slope(-1)                                                 # needs sage.geometry.polyhedron sage.rings.padics
            1 + O(5^20)

        AUTHOR:

        - Xavier Caruso (2013-03-20)
        """
    def slope_factorization(self):
        """
        Return a factorization of ``self`` into a product of factors
        corresponding to each slope in the Newton polygon.

        EXAMPLES::

            sage: # needs sage.geometry.polyhedron sage.rings.padics
            sage: K = Qp(5)
            sage: R.<x> = K[]
            sage: K = Qp(5)
            sage: R.<t> = K[]
            sage: f = 5 + 3*t + t^4 + 25*t^10
            sage: f.newton_slopes()
            [1, 0, 0, 0, -1/3, -1/3, -1/3, -1/3, -1/3, -1/3]
            sage: F = f.slope_factorization()
            sage: F.prod() == f
            True
            sage: for (f,_) in F:
            ....:     print(f.newton_slopes())
            [-1/3, -1/3, -1/3, -1/3, -1/3, -1/3]
            [0, 0, 0]
            [1]

        TESTS::

            sage: S.<x> = PowerSeriesRing(GF(5))
            sage: R.<y> = S[]
            sage: p = x^2 + y + x*y^2
            sage: p.slope_factorization()                                               # needs sage.geometry.polyhedron
            (x)
            * ((x + O(x^22))*y + 1 + 4*x^3 + 4*x^6 + 3*x^9 + x^15 + 3*x^18 + O(x^21))
            * ((x^-1 + O(x^20))*y + x + x^4 + 2*x^7 + 4*x^13 + 2*x^16 + 2*x^19 + O(x^22))

        AUTHOR:

        - Xavier Caruso (2013-03-20)
        """

class Polynomial_generic_dense_cdv(Polynomial_generic_dense_inexact, Polynomial_generic_cdv): ...
class Polynomial_generic_sparse_cdv(Polynomial_generic_sparse, Polynomial_generic_cdv): ...
class Polynomial_generic_cdvr(Polynomial_generic_cdv): ...
class Polynomial_generic_dense_cdvr(Polynomial_generic_dense_cdv, Polynomial_generic_cdvr): ...
class Polynomial_generic_sparse_cdvr(Polynomial_generic_sparse_cdv, Polynomial_generic_cdvr): ...
class Polynomial_generic_cdvf(Polynomial_generic_cdv, Polynomial_generic_field): ...
class Polynomial_generic_dense_cdvf(Polynomial_generic_dense_cdv, Polynomial_generic_cdvf): ...
class Polynomial_generic_sparse_cdvf(Polynomial_generic_sparse_cdv, Polynomial_generic_cdvf): ...
