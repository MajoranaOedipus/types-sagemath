from .laurent_series_ring import LaurentSeriesRing as LaurentSeriesRing
from .laurent_series_ring_element import LaurentSeries as LaurentSeries
from _typeshed import Incomplete
from sage.categories.complete_discrete_valuation import CompleteDiscreteValuationRings as CompleteDiscreteValuationRings
from sage.interfaces.abc import MagmaElement as MagmaElement
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings import integer as integer, power_series_mpoly as power_series_mpoly, power_series_poly as power_series_poly, power_series_ring_element as power_series_ring_element
from sage.rings.fraction_field_element import FractionFieldElement as FractionFieldElement
from sage.rings.infinity import infinity as infinity
from sage.rings.polynomial.multi_polynomial_ring_base import MPolynomialRing_base as MPolynomialRing_base
from sage.rings.polynomial.polynomial_ring import PolynomialRing_generic as PolynomialRing_generic
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.structure.category_object import normalize_names as normalize_names
from sage.structure.element import Expression as Expression, parent as parent
from sage.structure.nonexact import Nonexact as Nonexact
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

def PowerSeriesRing(base_ring, name=None, arg2=None, names=None, sparse: bool = False, default_prec=None, order: str = 'negdeglex', num_gens=None, implementation=None):
    """
    Create a univariate or multivariate power series ring over a given
    (commutative) base ring.

    INPUT:

    - ``base_ring`` -- a commutative ring

    - ``name``, ``names`` -- name(s) of the indeterminate

    - ``default_prec`` -- the default precision used if an exact object must
      be changed to an approximate object in order to do an arithmetic
      operation.  If left as ``None``, it will be set to the global
      default (20) in the univariate case, and 12 in the multivariate case.

    - ``sparse`` -- boolean (default: ``False``); whether power series
      are represented as sparse objects

    - ``order`` -- (default: ``negdeglex``) term ordering, for multivariate case

    - ``num_gens`` -- number of generators, for multivariate case

    There is a unique power series ring over each base ring with given
    variable name. Two power series over the same base ring with
    different variable names are not equal or isomorphic.

    EXAMPLES (Univariate)::

        sage: R = PowerSeriesRing(QQ, 'x'); R
        Power Series Ring in x over Rational Field

    ::

        sage: S = PowerSeriesRing(QQ, 'y'); S
        Power Series Ring in y over Rational Field

    ::

        sage: R = PowerSeriesRing(QQ, 10)
        Traceback (most recent call last):
        ...
        ValueError: variable name '10' does not start with a letter

    ::

        sage: S = PowerSeriesRing(QQ, 'x', default_prec=15); S
        Power Series Ring in x over Rational Field
        sage: S.default_prec()
        15

    EXAMPLES (Multivariate) See also :doc:`multi_power_series_ring`::

        sage: R = PowerSeriesRing(QQ, 't,u,v'); R
        Multivariate Power Series Ring in t, u, v over Rational Field

    ::

        sage: N = PowerSeriesRing(QQ,'w',num_gens=5); N
        Multivariate Power Series Ring in w0, w1, w2, w3, w4 over Rational Field

    Number of generators can be specified before variable name without using keyword::

        sage: M = PowerSeriesRing(QQ,4,'k'); M
        Multivariate Power Series Ring in k0, k1, k2, k3 over Rational Field

    Multivariate power series can be constructed using angle bracket or double square bracket notation::

        sage: R.<t,u,v> = PowerSeriesRing(QQ, 't,u,v'); R
        Multivariate Power Series Ring in t, u, v over Rational Field

        sage: ZZ[['s,t,u']]
        Multivariate Power Series Ring in s, t, u over Integer Ring

    Sparse multivariate power series ring::

        sage: M = PowerSeriesRing(QQ,4,'k',sparse=True); M
        Sparse Multivariate Power Series Ring in k0, k1, k2, k3 over
        Rational Field

    Power series ring over polynomial ring::

        sage: H = PowerSeriesRing(PolynomialRing(ZZ,3,'z'), 4, 'f'); H
        Multivariate Power Series Ring in f0, f1, f2, f3 over Multivariate
        Polynomial Ring in z0, z1, z2 over Integer Ring

    Power series ring over finite field::

        sage: S = PowerSeriesRing(GF(65537),'x,y'); S                                   # needs sage.rings.finite_rings
        Multivariate Power Series Ring in x, y over Finite Field of size
        65537

    Power series ring with many variables::

        sage: R = PowerSeriesRing(ZZ, ['x%s'%p for p in primes(100)]); R                # needs sage.libs.pari
        Multivariate Power Series Ring in x2, x3, x5, x7, x11, x13, x17, x19,
        x23, x29, x31, x37, x41, x43, x47, x53, x59, x61, x67, x71, x73, x79,
        x83, x89, x97 over Integer Ring

    - Use :meth:`inject_variables` to make the variables available for
      interactive use.

      ::

        sage: R.inject_variables()                                                      # needs sage.libs.pari
        Defining x2, x3, x5, x7, x11, x13, x17, x19, x23, x29, x31, x37,
        x41, x43, x47, x53, x59, x61, x67, x71, x73, x79, x83, x89, x97

        sage: f = x47 + 3*x11*x29 - x19 + R.O(3)                                        # needs sage.libs.pari
        sage: f in R                                                                    # needs sage.libs.pari
        True


    Variable ordering determines how series are displayed::

        sage: T.<a,b> = PowerSeriesRing(ZZ,order='deglex'); T
        Multivariate Power Series Ring in a, b over Integer Ring
        sage: T.term_order()
        Degree lexicographic term order
        sage: p = - 2*b^6 + a^5*b^2 + a^7 - b^2 - a*b^3 + T.O(9); p
        a^7 + a^5*b^2 - 2*b^6 - a*b^3 - b^2 + O(a, b)^9

        sage: U = PowerSeriesRing(ZZ,'a,b',order='negdeglex'); U
        Multivariate Power Series Ring in a, b over Integer Ring
        sage: U.term_order()
        Negative degree lexicographic term order
        sage: U(p)
        -b^2 - a*b^3 - 2*b^6 + a^7 + a^5*b^2 + O(a, b)^9


    TESTS::

        sage: N = PowerSeriesRing(QQ,'k',num_gens=5); N
        Multivariate Power Series Ring in k0, k1, k2, k3, k4 over Rational Field

    The following behavior of univariate power series ring will eventually
    be deprecated and then changed to return a multivariate power series
    ring::

        sage: N = PowerSeriesRing(QQ,'k',5); N
        Power Series Ring in k over Rational Field
        sage: N.default_prec()
        5
        sage: L.<m> = PowerSeriesRing(QQ,5); L
        Power Series Ring in m over Rational Field
        sage: L.default_prec()
        5

    By :issue:`14084`, a power series ring belongs to the category of integral
    domains, if the base ring does::

        sage: P = ZZ[['x']]
        sage: P.category()
        Category of integral domains
        sage: TestSuite(P).run()
        sage: M = ZZ[['x','y']]
        sage: M.category()
        Category of integral domains
        sage: TestSuite(M).run()

    Otherwise, it belongs to the category of commutative rings::

        sage: P = Integers(15)[['x']]
        sage: P.category()
        Category of commutative rings
        sage: TestSuite(P).run()
        sage: M = Integers(15)[['x','y']]
        sage: M.category()
        Category of commutative rings
        sage: TestSuite(M).run()

    .. SEEALSO::

        * :func:`sage.misc.defaults.set_series_precision`
    """
def is_PowerSeriesRing(R):
    """
    Return ``True`` if this is a *univariate* power series ring.  This is in
    keeping with the behavior of ``is_PolynomialRing``
    versus ``is_MPolynomialRing``.

    EXAMPLES::

        sage: from sage.rings.power_series_ring import is_PowerSeriesRing
        sage: is_PowerSeriesRing(10)
        doctest:warning...
        DeprecationWarning: The function is_PowerSeriesRing is deprecated;
        use 'isinstance(..., (PowerSeriesRing_generic, LazyPowerSeriesRing) and ....ngens() == 1)' instead.
        See https://github.com/sagemath/sage/issues/38290 for details.
        False
        sage: is_PowerSeriesRing(QQ[['x']])
        True
        sage: is_PowerSeriesRing(LazyPowerSeriesRing(QQ, 'x'))
        True
        sage: is_PowerSeriesRing(LazyPowerSeriesRing(QQ, 'x, y'))
        False
    """

class PowerSeriesRing_generic(UniqueRepresentation, Parent, Nonexact):
    """
    A power series ring.
    """
    Element: Incomplete
    def __init__(self, base_ring, name=None, default_prec=None, sparse: bool = False, implementation=None, category=None) -> None:
        """
        Initialize a power series ring.

        INPUT:

        - ``base_ring`` -- a commutative ring

        - ``name`` -- name of the indeterminate

        - ``default_prec`` -- the default precision

        - ``sparse`` -- whether or not power series are sparse

        - ``implementation`` -- either ``'poly'``, ``'mpoly'``, or
          ``'pari'``. Other values (for example ``'NTL'``) are passed to
          the attached polynomial ring.  The default is ``'pari'`` if
          the base field is a PARI finite field, and ``'poly'`` otherwise.

        If the base ring is a polynomial ring, then the option
        ``implementation='mpoly'`` causes computations to be done with
        multivariate polynomials instead of a univariate polynomial
        ring over the base ring. Only use this for dense power series
        where you will not do too much arithmetic, but the arithmetic you
        do must be fast.  You must explicitly call
        ``f.do_truncation()`` on an element for it to truncate away
        higher order terms (this is called automatically before
        printing).

        EXAMPLES:

        Since :issue:`11900`, it is in the category of commutative rings,
        and since :issue:`14084` it is actually an integral domain::

            sage: R.<x> = ZZ[[]]
            sage: R.category()
            Category of integral domains
            sage: TestSuite(R).run()

        When the base ring `k` is a field, the ring `k[[x]]` is not only a
        commutative ring, but also a complete discrete valuation ring (CDVR).
        The appropriate (sub)category is automatically set in this case::

            sage: k = GF(11)
            sage: R.<x> = k[[]]
            sage: R.category()
            Category of complete discrete valuation rings
            sage: TestSuite(R).run()

        It is checked that the default precision is nonnegative
        (see :issue:`19409`)::

            sage: PowerSeriesRing(ZZ, 'x', default_prec=-5)
            Traceback (most recent call last):
            ...
            ValueError: default_prec (= -5) must be nonnegative
        """
    def variable_names_recursive(self, depth=None):
        """
        Return the list of variable names of this and its base rings.

        EXAMPLES::

            sage: R = QQ[['x']][['y']][['z']]
            sage: R.variable_names_recursive()
            ('x', 'y', 'z')
            sage: R.variable_names_recursive(2)
            ('y', 'z')
        """
    def is_sparse(self):
        """
        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(ZZ)
            sage: t.is_sparse()
            False
            sage: R.<t> = PowerSeriesRing(ZZ, sparse=True)
            sage: t.is_sparse()
            True
        """
    def is_dense(self):
        """
        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(ZZ)
            sage: t.is_dense()
            True
            sage: R.<t> = PowerSeriesRing(ZZ, sparse=True)
            sage: t.is_dense()
            False
        """
    def construction(self):
        """
        Return the functorial construction of ``self``, namely, completion of
        the univariate polynomial ring with respect to the indeterminate
        (to a given precision).

        EXAMPLES::

            sage: R = PowerSeriesRing(ZZ, 'x')
            sage: c, S = R.construction(); S
            Univariate Polynomial Ring in x over Integer Ring
            sage: R == c(S)
            True
            sage: R = PowerSeriesRing(ZZ, 'x', sparse=True)
            sage: c, S = R.construction()
            sage: R == c(S)
            True
        """
    def base_extend(self, R):
        """
        Return the power series ring over `R` in the same variable as ``self``,
        assuming there is a canonical coerce map from the base ring of ``self``
        to `R`.

        EXAMPLES::

            sage: R.<T> = GF(7)[[]]; R
            Power Series Ring in T over Finite Field of size 7
            sage: R.change_ring(ZZ)
            Power Series Ring in T over Integer Ring
            sage: R.base_extend(ZZ)
            Traceback (most recent call last):
            ...
            TypeError: no base extension defined
        """
    def change_ring(self, R):
        """
        Return the power series ring over `R` in the same variable as ``self``.

        EXAMPLES::

            sage: R.<T> = QQ[[]]; R
            Power Series Ring in T over Rational Field
            sage: R.change_ring(GF(7))
            Power Series Ring in T over Finite Field of size 7
            sage: R.base_extend(GF(7))
            Traceback (most recent call last):
            ...
            TypeError: no base extension defined
            sage: R.base_extend(QuadraticField(3,'a'))                                  # needs sage.rings.number_field
            Power Series Ring in T over Number Field in a
             with defining polynomial x^2 - 3 with a = 1.732050807568878?
        """
    def change_var(self, var):
        """
        Return the power series ring in variable ``var`` over the same base ring.

        EXAMPLES::

            sage: R.<T> = QQ[[]]; R
            Power Series Ring in T over Rational Field
            sage: R.change_var('D')
            Power Series Ring in D over Rational Field
        """
    def is_exact(self):
        """
        Return ``False`` since the ring of power series over any ring is not
        exact.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(ZZ)
            sage: R.is_exact()
            False
        """
    def gen(self, n: int = 0):
        """
        Return the generator of this power series ring.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(ZZ)
            sage: R.gen()
            t
            sage: R.gen(3)
            Traceback (most recent call last):
            ...
            IndexError: generator n>0 not defined
        """
    def gens(self) -> tuple:
        """
        Return the generators of this ring.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(ZZ)
            sage: R.gens()
            (t,)
        """
    def uniformizer(self):
        """
        Return a uniformizer of this power series ring if it is
        a discrete valuation ring (i.e., if the base ring is actually
        a field). Otherwise, an error is raised.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(QQ)
            sage: R.uniformizer()
            t

            sage: R.<t> = PowerSeriesRing(ZZ)
            sage: R.uniformizer()
            Traceback (most recent call last):
            ...
            TypeError: The base ring is not a field
        """
    def ngens(self):
        """
        Return the number of generators of this power series ring.

        This is always 1.

        EXAMPLES::

            sage: R.<t> = ZZ[[]]
            sage: R.ngens()
            1
        """
    def random_element(self, prec=None, *args, **kwds):
        """
        Return a random power series.

        INPUT:

        - ``prec`` -- integer specifying precision of output (default:
          default precision of ``self``)

        - ``*args``, ``**kwds`` -- passed on to the ``random_element`` method for
          the base ring

        OUTPUT:

        Power series with precision ``prec`` whose coefficients are
        random elements from the base ring, randomized subject to the
        arguments ``*args`` and ``**kwds``.

        ALGORITHM:

        Call the ``random_element`` method on the underlying polynomial
        ring.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(QQ)
            sage: R.random_element(5)  # random
            -4 - 1/2*t^2 - 1/95*t^3 + 1/2*t^4 + O(t^5)
            sage: R.random_element(10)  # random
            -1/2 + 2*t - 2/7*t^2 - 25*t^3 - t^4 + 2*t^5 - 4*t^7 - 1/3*t^8 - t^9 + O(t^10)

        If given no argument, ``random_element`` uses default precision of self::

            sage: T = PowerSeriesRing(ZZ,'t')
            sage: T.default_prec()
            20
            sage: T.random_element()  # random
            4 + 2*t - t^2 - t^3 + 2*t^4 + t^5 + t^6 - 2*t^7 - t^8 - t^9 + t^11
             - 6*t^12 + 2*t^14 + 2*t^16 - t^17 - 3*t^18 + O(t^20)
            sage: S = PowerSeriesRing(ZZ,'t', default_prec=4)
            sage: S.random_element()  # random
            2 - t - 5*t^2 + t^3 + O(t^4)


        Further arguments are passed to the underlying base ring (:issue:`9481`)::

            sage: SZ = PowerSeriesRing(ZZ,'v')
            sage: SQ = PowerSeriesRing(QQ,'v')
            sage: SR = PowerSeriesRing(RR,'v')

            sage: SZ.random_element(x=4, y=6)  # random
            4 + 5*v + 5*v^2 + 5*v^3 + 4*v^4 + 5*v^5 + 5*v^6 + 5*v^7 + 4*v^8
             + 5*v^9 + 4*v^10 + 4*v^11 + 5*v^12 + 5*v^13 + 5*v^14 + 5*v^15
             + 5*v^16 + 5*v^17 + 4*v^18 + 5*v^19 + O(v^20)
            sage: SZ.random_element(3, x=4, y=6)  # random
            5 + 4*v + 5*v^2 + O(v^3)
            sage: SQ.random_element(3, num_bound=3, den_bound=100)  # random
            1/87 - 3/70*v - 3/44*v^2 + O(v^3)
            sage: SR.random_element(3, max=10, min=-10)  # random
            2.85948321262904 - 9.73071330911226*v - 6.60414378519265*v^2 + O(v^3)
        """
    def __contains__(self, x) -> bool:
        """
        Return ``True`` if x is an element of this power series ring or
        canonically coerces to this ring.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(ZZ)
            sage: t + t^2 in R
            True
            sage: 1/t in R
            False
            sage: 5 in R
            True
            sage: 1/3 in R
            False
            sage: S.<s> = PowerSeriesRing(ZZ)
            sage: s in R
            False
        """
    def is_field(self, proof: bool = True):
        """
        Return ``False`` since the ring of power series over any ring is never
        a field.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(ZZ)
            sage: R.is_field()
            False
        """
    def is_finite(self):
        """
        Return ``False`` since the ring of power series over any ring is never
        finite.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(ZZ)
            sage: R.is_finite()
            False
        """
    def characteristic(self):
        """
        Return the characteristic of this power series ring, which is the
        same as the characteristic of the base ring of the power series
        ring.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(ZZ)
            sage: R.characteristic()
            0
            sage: R.<w> = Integers(2^50)[[]]; R
            Power Series Ring in w over Ring of integers modulo 1125899906842624
            sage: R.characteristic()
            1125899906842624
        """
    def residue_field(self):
        """
        Return the residue field of this power series ring.

        EXAMPLES::

            sage: R.<x> = PowerSeriesRing(GF(17))
            sage: R.residue_field()
            Finite Field of size 17
            sage: R.<x> = PowerSeriesRing(Zp(5))                                        # needs sage.rings.padics
            sage: R.residue_field()                                                     # needs sage.rings.padics
            Finite Field of size 5
        """
    def laurent_series_ring(self):
        """
        If this is the power series ring `R[[t]]`, return the
        Laurent series ring `R((t))`.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(ZZ, default_prec=5)
            sage: S = R.laurent_series_ring(); S
            Laurent Series Ring in t over Integer Ring
            sage: S.default_prec()
            5
            sage: f = 1 + t; g = 1/f; g
            1 - t + t^2 - t^3 + t^4 + O(t^5)
        """

class PowerSeriesRing_domain(PowerSeriesRing_generic):
    def fraction_field(self):
        """
        Return the Laurent series ring over the fraction field of the base
        ring.

        This is actually *not* the fraction field of this ring, but its
        completion with respect to the topology defined by the valuation.
        When we are working at finite precision, these two fields are
        indistinguishable; that is the reason why we allow ourselves to
        make this confusion here.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(ZZ)
            sage: R.fraction_field()
            Laurent Series Ring in t over Rational Field
            sage: Frac(R)
            Laurent Series Ring in t over Rational Field
        """

class PowerSeriesRing_over_field(PowerSeriesRing_domain):
    def fraction_field(self):
        """
        Return the fraction field of this power series ring, which is
        defined since this is over a field.

        This fraction field is just the Laurent series ring over the base
        field.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(GF(7))
            sage: R.fraction_field()
            Laurent Series Ring in t over Finite Field of size 7
            sage: Frac(R)
            Laurent Series Ring in t over Finite Field of size 7
        """

def unpickle_power_series_ring_v0(base_ring, name, default_prec, sparse):
    """
    Unpickle (deserialize) a univariate power series ring according to
    the given inputs.

    EXAMPLES::

        sage: P.<x> = PowerSeriesRing(QQ)
        sage: loads(dumps(P)) == P  # indirect doctest
        True
    """
