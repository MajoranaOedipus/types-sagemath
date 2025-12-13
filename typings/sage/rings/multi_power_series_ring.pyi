from sage.categories.commutative_rings import CommutativeRings as CommutativeRings
from sage.categories.integral_domains import IntegralDomains as IntegralDomains
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.infinity import infinity as infinity
from sage.rings.laurent_series_ring import LaurentSeriesRing as LaurentSeriesRing
from sage.rings.multi_power_series_ring_element import MPowerSeries as MPowerSeries
from sage.rings.polynomial.multi_polynomial_ring import MPolynomialRing_base as MPolynomialRing_base
from sage.rings.polynomial.polynomial_ring import PolynomialRing_generic as PolynomialRing_generic
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.polynomial.term_order import TermOrder as TermOrder
from sage.rings.power_series_ring import PowerSeriesRing as PowerSeriesRing, PowerSeriesRing_generic as PowerSeriesRing_generic
from sage.structure.nonexact import Nonexact as Nonexact
from sage.structure.parent import Parent as Parent

def is_MPowerSeriesRing(x):
    """
    Return ``True`` if input is a multivariate power series ring.

    TESTS::

        sage: from sage.rings.power_series_ring import is_PowerSeriesRing
        sage: from sage.rings.multi_power_series_ring import is_MPowerSeriesRing
        sage: M = PowerSeriesRing(ZZ, 4, 'v')
        sage: is_PowerSeriesRing(M)
        doctest:warning...
        DeprecationWarning: The function is_PowerSeriesRing is deprecated;
        use 'isinstance(..., (PowerSeriesRing_generic, LazyPowerSeriesRing) and ....ngens() == 1)' instead.
        See https://github.com/sagemath/sage/issues/38290 for details.
        False
        sage: is_MPowerSeriesRing(M)
        doctest:warning...
        DeprecationWarning: The function is_MPowerSeriesRing is deprecated;
        use 'isinstance(..., (MPowerSeriesRing_generic, LazyPowerSeriesRing))' instead.
        See https://github.com/sagemath/sage/issues/38290 for details.
        True
        sage: T = PowerSeriesRing(RR, 'v')
        sage: is_PowerSeriesRing(T)
        True
        sage: is_MPowerSeriesRing(T)
        False
        sage: L = LazyPowerSeriesRing(QQ, 'x')
        sage: is_MPowerSeriesRing(L)
        True
        sage: L = LazyPowerSeriesRing(QQ, 'x, y')
        sage: is_MPowerSeriesRing(L)
        True
    """

class MPowerSeriesRing_generic(PowerSeriesRing_generic, Nonexact):
    '''
    A multivariate power series ring.  This class is implemented as a
    single variable power series ring in the variable ``T`` over a
    multivariable polynomial ring in the specified generators.  Each
    generator ``g`` of the multivariable polynomial ring (called the
    "foreground ring") is mapped to ``g*T`` in the single variable power series
    ring (called the "background ring").  The background power series ring
    is used to do arithmetic and track total-degree precision.  The
    foreground polynomial ring is used to display elements.

    For usage and examples, see above, and :meth:`PowerSeriesRing`.
    '''
    Element = MPowerSeries
    @staticmethod
    def __classcall__(cls, base_ring, num_gens, name_list, order: str = 'negdeglex', default_prec: int = 10, sparse: bool = False):
        """
        Preprocessing of arguments: The term order can be given as string
        or as a :class:`~sage.rings.polynomial.term_order.TermOrder` instance.

        TESTS::

            sage: P1 = PowerSeriesRing(QQ, ['f0','f1','f2','f3'], order=TermOrder('degrevlex'))
            sage: P2 = PowerSeriesRing(QQ,4,'f', order='degrevlex')
            sage: P1 is P2   # indirect doctest
            True
        """
    def __init__(self, base_ring, num_gens, name_list, order: str = 'negdeglex', default_prec: int = 10, sparse: bool = False) -> None:
        """
        Initialize a multivariate power series ring.  See PowerSeriesRing
        for complete documentation.

        INPUT:

        - ``base_ring`` -- a commutative ring

        - ``num_gens`` -- number of generators

        - ``name_list`` -- list of indeterminate names or a single name
            If a single name is given, indeterminates will be this name
            followed by a number from 0 to num_gens - 1.  If a list is
            given, these will be the indeterminate names and the length
            of the list must be equal to num_gens.

        - ``order`` -- ordering of variables; default is
          negative degree lexicographic

        - ``default_prec`` -- (default: 10) the default total-degree precision
          for elements

        - ``sparse`` -- whether or not the power series are sparse; the
          underlying polynomial ring is always sparse

        EXAMPLES::

            sage: R.<t,u,v> = PowerSeriesRing(QQ)
            sage: g = 1 + v + 3*u*t^2 - 2*v^2*t^2
            sage: g = g.add_bigoh(5); g
            1 + v + 3*t^2*u - 2*t^2*v^2 + O(t, u, v)^5
            sage: g in R
            True

        TESTS:

        By :issue:`14084`, the multi-variate power series ring belongs to the
        category of integral domains, if the base ring does::

            sage: P = ZZ[['x','y']]
            sage: P.category()
            Category of integral domains
            sage: TestSuite(P).run()

        Otherwise, it belongs to the category of commutative rings::

            sage: P = Integers(15)[['x','y']]
            sage: P.category()
            Category of commutative rings
            sage: TestSuite(P).run()
        """
    def is_integral_domain(self, proof: bool = False):
        """
        Return ``True`` if the base ring is an integral domain; otherwise
        return False.

        EXAMPLES::

            sage: M = PowerSeriesRing(QQ,4,'v'); M
            Multivariate Power Series Ring in v0, v1, v2, v3 over Rational Field
            sage: M.is_integral_domain()
            True
        """
    def is_noetherian(self, proof: bool = False):
        """
        Power series over a Noetherian ring are Noetherian.

        EXAMPLES::

            sage: M = PowerSeriesRing(QQ,4,'v'); M
            Multivariate Power Series Ring in v0, v1, v2, v3 over Rational Field
            sage: M.is_noetherian()
            True

            sage: W = PowerSeriesRing(InfinitePolynomialRing(ZZ,'a'),2,'x,y')
            sage: W.is_noetherian()
            False
        """
    def term_order(self):
        """
        Print term ordering of ``self``.  Term orderings are implemented by the
        TermOrder class.

        EXAMPLES::

            sage: M.<x,y,z> = PowerSeriesRing(ZZ,3)
            sage: M.term_order()
            Negative degree lexicographic term order
            sage: m = y*z^12 - y^6*z^8 - x^7*y^5*z^2 + x*y^2*z + M.O(15); m
            x*y^2*z + y*z^12 - x^7*y^5*z^2 - y^6*z^8 + O(x, y, z)^15

            sage: N = PowerSeriesRing(ZZ,3,'x,y,z', order='deglex')
            sage: N.term_order()
            Degree lexicographic term order
            sage: N(m)
            -x^7*y^5*z^2 - y^6*z^8 + y*z^12 + x*y^2*z + O(x, y, z)^15
        """
    def characteristic(self):
        """
        Return characteristic of base ring, which is characteristic of ``self``.

        EXAMPLES::

            sage: H = PowerSeriesRing(GF(65537),4,'f'); H                               # needs sage.rings.finite_rings
            Multivariate Power Series Ring in f0, f1, f2, f3 over
            Finite Field of size 65537
            sage: H.characteristic()                                                    # needs sage.rings.finite_rings
            65537
        """
    def construction(self):
        """
        Return a functor `F` and base ring `R` such that ``F(R) == self``.

        EXAMPLES::

            sage: M = PowerSeriesRing(QQ, 4, 'f'); M
            Multivariate Power Series Ring in f0, f1, f2, f3 over Rational Field

            sage: (c,R) = M.construction(); (c,R)
            (Completion[('f0', 'f1', 'f2', 'f3'), prec=12],
             Multivariate Polynomial Ring in f0, f1, f2, f3 over Rational Field)
            sage: c
            Completion[('f0', 'f1', 'f2', 'f3'), prec=12]
            sage: c(R)
            Multivariate Power Series Ring in f0, f1, f2, f3 over Rational Field
            sage: c(R) == M
            True

        TESTS::

            sage: M2 = PowerSeriesRing(QQ,4,'f', sparse=True)
            sage: M == M2
            False
            sage: c,R = M2.construction()
            sage: c(R)==M2
            True
            sage: M3 = PowerSeriesRing(QQ,4,'f', order='degrevlex')
            sage: M3 == M
            False
            sage: M3 == M2
            False
            sage: c,R = M3.construction()
            sage: c(R)==M3
            True
        """
    def change_ring(self, R):
        """
        Return the power series ring over `R` in the same variable as ``self``.
        This function ignores the question of whether the base ring of self
        is or can extend to the base ring of `R`; for the latter, use
        ``base_extend``.

        EXAMPLES::

            sage: R.<t,u,v> = PowerSeriesRing(QQ); R
            Multivariate Power Series Ring in t, u, v over Rational Field
            sage: R.base_extend(RR)                                                     # needs sage.rings.real_mpfr
            Multivariate Power Series Ring in t, u, v over Real Field with
            53 bits of precision
            sage: R.change_ring(IntegerModRing(10))
            Multivariate Power Series Ring in t, u, v over Ring of integers
            modulo 10
            sage: R.base_extend(IntegerModRing(10))
            Traceback (most recent call last):
            ...
            TypeError: no base extension defined


            sage: S = PowerSeriesRing(GF(65537),2,'x,y'); S                             # needs sage.rings.finite_rings
            Multivariate Power Series Ring in x, y over Finite Field of size
            65537
            sage: S.change_ring(GF(5))                                                  # needs sage.rings.finite_rings
            Multivariate Power Series Ring in x, y over Finite Field of size 5
        """
    def remove_var(self, *var):
        """
        Remove given variable or sequence of variables from ``self``.

        EXAMPLES::

            sage: A.<s,t,u> = PowerSeriesRing(ZZ)
            sage: A.remove_var(t)
            Multivariate Power Series Ring in s, u over Integer Ring
            sage: A.remove_var(s,t)
            Power Series Ring in u over Integer Ring


            sage: M = PowerSeriesRing(GF(5),5,'t'); M
            Multivariate Power Series Ring in t0, t1, t2, t3, t4
             over Finite Field of size 5
            sage: M.remove_var(M.gens()[3])
            Multivariate Power Series Ring in t0, t1, t2, t4
             over Finite Field of size 5

        Removing all variables results in the base ring::

            sage: M.remove_var(*M.gens())
            Finite Field of size 5
        """
    def laurent_series_ring(self) -> None:
        """
        Laurent series not yet implemented for multivariate power series rings.

        TESTS::

            sage: M = PowerSeriesRing(ZZ,3,'x,y,z')
            sage: M.laurent_series_ring()
            Traceback (most recent call last):
            ...
            NotImplementedError: Laurent series not implemented for
            multivariate power series.
        """
    def is_sparse(self):
        """
        Check whether ``self`` is sparse.

        EXAMPLES::

            sage: M = PowerSeriesRing(ZZ, 3, 's,t,u'); M
            Multivariate Power Series Ring in s, t, u over Integer Ring
            sage: M.is_sparse()
            False
            sage: N = PowerSeriesRing(ZZ, 3, 's,t,u', sparse=True); N
            Sparse Multivariate Power Series Ring in s, t, u over Integer Ring
            sage: N.is_sparse()
            True
        """
    def is_dense(self):
        """
        Is ``self`` dense? (opposite of sparse)

        EXAMPLES::

            sage: M = PowerSeriesRing(ZZ, 3, 's,t,u'); M
            Multivariate Power Series Ring in s, t, u over Integer Ring
            sage: M.is_dense()
            True
            sage: N = PowerSeriesRing(ZZ, 3, 's,t,u', sparse=True); N
            Sparse Multivariate Power Series Ring in s, t, u over Integer Ring
            sage: N.is_dense()
            False
        """
    def gen(self, n: int = 0):
        """
        Return the `n`-th generator of ``self``.

        EXAMPLES::

            sage: M = PowerSeriesRing(ZZ, 10, 'v')
            sage: M.gen(6)
            v6
        """
    def ngens(self):
        """
        Return number of generators of ``self``.

        EXAMPLES::

            sage: M = PowerSeriesRing(ZZ, 10, 'v')
            sage: M.ngens()
            10
        """
    def gens(self) -> tuple:
        """
        Return the generators of this ring.

        EXAMPLES::

            sage: M = PowerSeriesRing(ZZ, 3, 'v')
            sage: M.gens()
            (v0, v1, v2)
        """
    def prec_ideal(self):
        """
        Return the ideal which determines precision; this is the ideal
        generated by all of the generators of our background polynomial
        ring.

        EXAMPLES::

            sage: A.<s,t,u> = PowerSeriesRing(ZZ)
            sage: A.prec_ideal()
            Ideal (s, t, u) of
             Multivariate Polynomial Ring in s, t, u over Integer Ring
        """
    def bigoh(self, prec):
        """
        Return big oh with precision ``prec``.  The function ``O`` does the same thing.

        EXAMPLES::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2); T
            Multivariate Power Series Ring in a, b over Integer Ring
            sage: T.bigoh(10)
            0 + O(a, b)^10
            sage: T.O(10)
            0 + O(a, b)^10
        """
    def O(self, prec):
        """
        Return big oh with precision ``prec``.  This function is an alias for ``bigoh``.

        EXAMPLES::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2); T
            Multivariate Power Series Ring in a, b over Integer Ring
            sage: T.O(10)
            0 + O(a, b)^10
            sage: T.bigoh(10)
            0 + O(a, b)^10
        """

def unpickle_multi_power_series_ring_v0(base_ring, num_gens, names, order, default_prec, sparse):
    """
    Unpickle (deserialize) a multivariate power series ring according
    to the given inputs.

    EXAMPLES::

        sage: P.<x,y> = PowerSeriesRing(QQ)
        sage: loads(dumps(P)) == P # indirect doctest
        True
    """
