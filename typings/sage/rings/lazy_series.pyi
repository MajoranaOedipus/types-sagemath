from sage.arith.functions import lcm as lcm
from sage.arith.misc import divisors as divisors, factorial as factorial, moebius as moebius
from sage.arith.power import generic_power as generic_power
from sage.categories.integral_domains import IntegralDomains as IntegralDomains
from sage.categories.rings import Rings as Rings
from sage.categories.tensor import tensor as tensor
from sage.combinat.partition import Partition as Partition, Partitions as Partitions
from sage.data_structures.stream import Stream_add as Stream_add, Stream_cauchy_compose as Stream_cauchy_compose, Stream_cauchy_invert as Stream_cauchy_invert, Stream_cauchy_mul as Stream_cauchy_mul, Stream_cauchy_mul_commutative as Stream_cauchy_mul_commutative, Stream_derivative as Stream_derivative, Stream_dirichlet_convolve as Stream_dirichlet_convolve, Stream_dirichlet_invert as Stream_dirichlet_invert, Stream_exact as Stream_exact, Stream_function as Stream_function, Stream_integral as Stream_integral, Stream_lmul as Stream_lmul, Stream_map_coefficients as Stream_map_coefficients, Stream_neg as Stream_neg, Stream_plethysm as Stream_plethysm, Stream_rmul as Stream_rmul, Stream_shift as Stream_shift, Stream_sub as Stream_sub, Stream_truncated as Stream_truncated, Stream_uninitialized as Stream_uninitialized, Stream_zero as Stream_zero
from sage.misc.derivative import derivative_parse as derivative_parse
from sage.misc.misc_c import prod as prod
from sage.rings.infinity import infinity as infinity
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.laurent_polynomial_ring import LaurentPolynomialRing as LaurentPolynomialRing
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import Element as Element, parent as parent
from sage.structure.richcmp import op_EQ as op_EQ, op_NE as op_NE

class LazyModuleElement(Element):
    """
    A lazy sequence with a module structure given by term-wise
    addition and scalar multiplication.

    EXAMPLES::

        sage: L.<z> = LazyLaurentSeriesRing(ZZ)
        sage: M = L(lambda n: n, valuation=0)
        sage: N = L(lambda n: 1, valuation=0)
        sage: M[0:10]
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        sage: N[0:10]
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    Two sequences can be added::

        sage: O = M + N
        sage: O[0:10]
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    Two sequences can be subtracted::

        sage: P = M - N
        sage: P[0:10]
        [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8]

    A sequence can be multiplied by a scalar::

        sage: Q = 2 * M
        sage: Q[0:10]
        [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

    The negation of a sequence can also be found::

        sage: R = -M
        sage: R[0:10]
        [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
    """
    def __init__(self, parent, coeff_stream) -> None:
        """
        Initialize the series.

        TESTS::

            sage: L.<z> = LazyLaurentSeriesRing(ZZ)
            sage: TestSuite(L.an_element()).run()

            sage: L = LazyDirichletSeriesRing(QQbar, 'z')                               # needs sage.rings.number_field
            sage: g = L(constant=1)                                                     # needs sage.rings.number_field
            sage: TestSuite(g).run()                                                    # needs sage.rings.number_field
        """
    def __getitem__(self, n):
        '''
        Return the homogeneous degree ``n`` part of the series.

        INPUT:

        - ``n`` -- integer; the degree

        For a series ``f``, the slice ``f[start:stop]`` produces the following:

        - if ``start`` and ``stop`` are integers, return the list of
          terms with given degrees

        - if ``start`` is ``None``, return the list of terms
          beginning with the valuation

        - if ``stop`` is ``None``, return a
          :class:`~sage.misc.lazy_list.lazy_list_generic` instead.

        EXAMPLES::

            sage: L.<z> = LazyLaurentSeriesRing(ZZ)
            sage: f = z / (1 - 2*z^3)
            sage: [f[n] for n in range(20)]
            [0, 1, 0, 0, 2, 0, 0, 4, 0, 0, 8, 0, 0, 16, 0, 0, 32, 0, 0, 64]
            sage: f[0:20]
            [0, 1, 0, 0, 2, 0, 0, 4, 0, 0, 8, 0, 0, 16, 0, 0, 32, 0, 0, 64]
            sage: f[:20]
            [1, 0, 0, 2, 0, 0, 4, 0, 0, 8, 0, 0, 16, 0, 0, 32, 0, 0, 64]
            sage: f[::3]
            lazy list [1, 2, 4, ...]

            sage: M = L(lambda n: n, valuation=0)
            sage: [M[n] for n in range(20)]
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

            sage: L.<z> = LazyLaurentSeriesRing(ZZ, sparse=True)
            sage: M = L(lambda n: n, valuation=0)
            sage: [M[n] for n in range(20)]
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

        Similarly for multivariate series::

            sage: L.<x,y> = LazyPowerSeriesRing(QQ)
            sage: sin(x*y)[:11]
            [x*y, 0, 0, 0, -1/6*x^3*y^3, 0, 0, 0, 1/120*x^5*y^5]
            sage: sin(x*y)[2::4]
            lazy list [x*y, -1/6*x^3*y^3, 1/120*x^5*y^5, ...]

        Similarly for Dirichlet series::

            sage: L = LazyDirichletSeriesRing(ZZ, "z")
            sage: L(lambda n: n)[1:11]
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        TESTS:

        Check that no more elements than necessary are computed::

            sage: L = LazyDirichletSeriesRing(ZZ, "z")
            sage: f = L(lambda n: 0 if n < 5 else n)
            sage: f[:3]
            []
            sage: f._coeff_stream._cache
            {}
        '''
    coefficient = __getitem__
    def coefficients(self, n=None):
        """
        Return the first `n` nonzero coefficients of ``self``.

        INPUT:

        - ``n`` -- (optional) the number of nonzero coefficients to return

        If the series has fewer than `n` nonzero coefficients, only
        these are returned.

        If ``n`` is ``None``, a
        :class:`~sage.misc.lazy_list.lazy_list_generic` with all
        nonzero coefficients is returned instead.

        .. WARNING::

            If there are fewer than `n` nonzero coefficients, but
            this cannot be detected, this method will not return.

        EXAMPLES::

            sage: L.<x> = LazyPowerSeriesRing(QQ)
            sage: f = L([1,2,3])
            sage: f.coefficients(5)
            doctest:...: DeprecationWarning: the method coefficients now only returns the nonzero coefficients. Use __getitem__ instead.
            See https://github.com/sagemath/sage/issues/32367 for details.
            [1, 2, 3]

            sage: f = sin(x)
            sage: f.coefficients(5)
            [1, -1/6, 1/120, -1/5040, 1/362880]

            sage: L.<x, y> = LazyPowerSeriesRing(QQ)
            sage: f = sin(x^2+y^2)
            sage: f.coefficients(5)
            [1, 1, -1/6, -1/2, -1/2]

            sage: f.coefficients()
            lazy list [1, 1, -1/6, ...]

            sage: L.<x> = LazyPowerSeriesRing(GF(2))
            sage: f = L(lambda n: n)
            sage: f.coefficients(5)
            [1, 1, 1, 1, 1]
        """
    def map_coefficients(self, f):
        '''
        Return the series with ``f`` applied to each nonzero
        coefficient of ``self``.

        INPUT:

        - ``func`` -- function that takes in a coefficient and returns
          a new coefficient

        EXAMPLES::

            sage: L.<z> = LazyLaurentSeriesRing(ZZ)
            sage: m = L(lambda n: n, valuation=0); m
            z + 2*z^2 + 3*z^3 + 4*z^4 + 5*z^5 + 6*z^6 + O(z^7)
            sage: m.map_coefficients(lambda c: c + 1)
            2*z + 3*z^2 + 4*z^3 + 5*z^4 + 6*z^5 + 7*z^6 + 8*z^7 + O(z^8)

        Similarly for Dirichlet series::

            sage: L = LazyDirichletSeriesRing(ZZ, "z")
            sage: s = L(lambda n: n-1)
            sage: s                                                                     # needs sage.symbolic
            1/(2^z) + 2/3^z + 3/4^z + 4/5^z + 5/6^z + 6/7^z + O(1/(8^z))
            sage: ms = s.map_coefficients(lambda c: c + 1)                              # needs sage.symbolic
            sage: ms                                                                    # needs sage.symbolic
            2/2^z + 3/3^z + 4/4^z + 5/5^z + 6/6^z + 7/7^z + 8/8^z + O(1/(9^z))

        Similarly for multivariate power series::

            sage: L.<x, y> = LazyPowerSeriesRing(QQ)
            sage: f = 1/(1-(x+y)); f
            1 + (x+y) + (x^2+2*x*y+y^2) + (x^3+3*x^2*y+3*x*y^2+y^3)
             + (x^4+4*x^3*y+6*x^2*y^2+4*x*y^3+y^4)
             + (x^5+5*x^4*y+10*x^3*y^2+10*x^2*y^3+5*x*y^4+y^5)
             + (x^6+6*x^5*y+15*x^4*y^2+20*x^3*y^3+15*x^2*y^4+6*x*y^5+y^6)
             + O(x,y)^7
            sage: f.map_coefficients(lambda c: c^2)
            1 + (x+y) + (x^2+4*x*y+y^2) + (x^3+9*x^2*y+9*x*y^2+y^3)
             + (x^4+16*x^3*y+36*x^2*y^2+16*x*y^3+y^4)
             + (x^5+25*x^4*y+100*x^3*y^2+100*x^2*y^3+25*x*y^4+y^5)
             + (x^6+36*x^5*y+225*x^4*y^2+400*x^3*y^3+225*x^2*y^4+36*x*y^5+y^6)
             + O(x,y)^7

        Similarly for lazy symmetric functions::

            sage: # needs sage.combinat
            sage: p = SymmetricFunctions(QQ).p()
            sage: L = LazySymmetricFunctions(p)
            sage: f = 1/(1-2*L(p[1])); f
            p[] + 2*p[1] + (4*p[1,1]) + (8*p[1,1,1]) + (16*p[1,1,1,1])
             + (32*p[1,1,1,1,1]) + (64*p[1,1,1,1,1,1]) + O^7
            sage: f.map_coefficients(lambda c: log(c, 2))
            p[1] + (2*p[1,1]) + (3*p[1,1,1]) + (4*p[1,1,1,1])
             + (5*p[1,1,1,1,1]) + (6*p[1,1,1,1,1,1]) + O^7

        TESTS:

        Dense implementation::

            sage: L.<z> = LazyLaurentSeriesRing(ZZ, sparse=False)
            sage: s = z/(1 - 2*z^2)
            sage: t = s.map_coefficients(lambda c: c + 1)
            sage: s
            z + 2*z^3 + 4*z^5 + 8*z^7 + O(z^8)
            sage: t
            2*z + 3*z^3 + 5*z^5 + 9*z^7 + O(z^8)
            sage: m = L(lambda n: n, valuation=0); m
            z + 2*z^2 + 3*z^3 + 4*z^4 + 5*z^5 + 6*z^6 + O(z^7)
            sage: m.map_coefficients(lambda c: c + 1)
            2*z + 3*z^2 + 4*z^3 + 5*z^4 + 6*z^5 + 7*z^6 + 8*z^7 + O(z^8)

        Test the zero series::

            sage: from sage.data_structures.stream import Stream_zero
            sage: L.<z> = LazyLaurentSeriesRing(ZZ)
            sage: s = L(0).map_coefficients(lambda c: c + 1); s
            0
            sage: isinstance(s._coeff_stream, Stream_zero)
            True

        An example where the series is known to be exact::

            sage: f = z + z^2 + z^3
            sage: f.map_coefficients(lambda c: c + 1)
            2*z + 2*z^2 + 2*z^3
        '''
    def truncate(self, d):
        """
        Return the series obtained by removing all terms of degree at least
        ``d``.

        INPUT:

        - ``d`` -- integer; the degree from which the series is truncated

        EXAMPLES:

        Dense implementation::

            sage: L.<z> = LazyLaurentSeriesRing(ZZ, sparse=False)
            sage: alpha = 1/(1-z)
            sage: alpha
            1 + z + z^2 + O(z^3)
            sage: beta = alpha.truncate(5)
            sage: beta
            1 + z + z^2 + z^3 + z^4
            sage: alpha - beta
            z^5 + z^6 + z^7 + O(z^8)
            sage: M = L(lambda n: n, valuation=0); M
            z + 2*z^2 + 3*z^3 + 4*z^4 + 5*z^5 + 6*z^6 + O(z^7)
            sage: M.truncate(4)
            z + 2*z^2 + 3*z^3

        Sparse Implementation::

            sage: L.<z> = LazyLaurentSeriesRing(ZZ, sparse=True)
            sage: M = L(lambda n: n, valuation=0); M
            z + 2*z^2 + 3*z^3 + 4*z^4 + 5*z^5 + 6*z^6 + O(z^7)
            sage: M.truncate(4)
            z + 2*z^2 + 3*z^3

        Series which are known to be exact can also be truncated::

            sage: M = z + z^2 + z^3 + z^4
            sage: M.truncate(4)
            z + z^2 + z^3

        TESTS:

        Check that :issue:`36154` is fixed::

            sage: L.<z> = LazyPowerSeriesRing(QQ)
            sage: f = L([0,1,2])
            sage: f.truncate(1)
            0
        """
    def restrict(self, min_degree=None, max_degree=None):
        """
        Return the series obtained by keeping only terms of
        degree between ``min_degree`` and ``max_degree``.

        INPUT:

        - ``min_degree``, ``max_degree`` -- (optional) integers
          indicating which degrees to keep

        EXAMPLES::

            sage: L.<z> = LazyLaurentSeriesRing(ZZ)
            sage: alpha = z + 2*z^2 + 3*z^3 + z^4/(1-z)
            sage: alpha
            z + 2*z^2 + 3*z^3 + z^4 + z^5 + z^6 + O(z^7)
            sage: alpha.restrict(2)
            2*z^2 + 3*z^3 + z^4 + z^5 + z^6 + O(z^7)
            sage: alpha.restrict(3)
            3*z^3 + z^4 + z^5 + z^6 + O(z^7)
            sage: alpha.restrict(3, 6)
            3*z^3 + z^4 + z^5 + z^6
            sage: alpha.restrict(max_degree=6)
            z + 2*z^2 + 3*z^3 + z^4 + z^5 + z^6

            sage: L.<z> = LazyLaurentSeriesRing(QQ)
            sage: exp(z).restrict(3)
            1/6*z^3 + 1/24*z^4 + 1/120*z^5 + 1/720*z^6 + 1/5040*z^7 + 1/40320*z^8 + 1/362880*z^9 + O(z^10)
        """
    def shift(self, n):
        """
        Return ``self`` with the indices shifted by ``n``.

        For example, a Laurent series is multiplied by the power `z^n`,
        where `z` is the variable of ``self``. For series with a fixed
        minimal valuation (e.g., power series), this removes any terms
        that are less than the minimal valuation.

        INPUT:

        - ``n`` -- the amount to shift

        EXAMPLES::

            sage: L.<z> = LazyLaurentSeriesRing(ZZ)
            sage: f = 1 / (1 + 2*z)
            sage: f
            1 - 2*z + 4*z^2 - 8*z^3 + 16*z^4 - 32*z^5 + 64*z^6 + O(z^7)
            sage: f.shift(3)
            z^3 - 2*z^4 + 4*z^5 - 8*z^6 + 16*z^7 - 32*z^8 + 64*z^9 + O(z^10)
            sage: f << -3  # shorthand
            z^-3 - 2*z^-2 + 4*z^-1 - 8 + 16*z - 32*z^2 + 64*z^3 + O(z^4)
            sage: g = z^-3 + 3 + z^2
            sage: g.shift(5)
            z^2 + 3*z^5 + z^7
            sage: L([2,0,3], valuation=2, degree=7, constant=1) << -2
            2 + 3*z^2 + z^5 + z^6 + z^7 + O(z^8)

            sage: D = LazyDirichletSeriesRing(QQ, 't')
            sage: f = D([0,1,2])
            sage: f                                                                     # needs sage.symbolic
            1/(2^t) + 2/3^t
            sage: sf = f.shift(3)
            sage: sf                                                                    # needs sage.symbolic
            1/(5^t) + 2/6^t

        Examples with power series (where the minimal valuation is `0`)::

            sage: L.<x> = LazyPowerSeriesRing(QQ)
            sage: f = 1 / (1 - x)
            sage: f.shift(2)
            x^2 + x^3 + x^4 + O(x^5)
            sage: g = f.shift(-1); g
            1 + x + x^2 + O(x^3)
            sage: f == g
            True
            sage: g[-1]
            0
            sage: h = L(lambda n: 1)
            sage: LazyPowerSeriesRing.options.halting_precision(20)  # verify up to degree 20
            sage: f == h
            True
            sage: h == f
            True
            sage: h.shift(-1) == h
            True
            sage: LazyPowerSeriesRing.options._reset()

            sage: fp = L([3,3,3], constant=1)
            sage: fp.shift(2)
            3*x^2 + 3*x^3 + 3*x^4 + x^5 + x^6 + x^7 + O(x^8)
            sage: fp.shift(-2)
            3 + x + x^2 + x^3 + O(x^4)
            sage: fp.shift(-7)
            1 + x + x^2 + O(x^3)
            sage: fp.shift(-5) == g
            True

        We compare the shifting with converting to the fraction field
        (see also :issue:`35293`)::

            sage: M = L.fraction_field()
            sage: f = L([1,2,3,4]); f
            1 + 2*x + 3*x^2 + 4*x^3
            sage: f.shift(-3)
            4
            sage: M(f).shift(-3)
            x^-3 + 2*x^-2 + 3*x^-1 + 4

        An example with a more general function::

            sage: fun = lambda n: 1 if ZZ(n).is_power_of(2) else 0
            sage: f = L(fun); f
            x + x^2 + x^4 + O(x^7)
            sage: fs = f.shift(-4)
            sage: fs
            1 + x^4 + O(x^7)
            sage: fs.shift(4)
            x^4 + x^8 + O(x^11)
            sage: M(f).shift(-4)
            x^-3 + x^-2 + 1 + O(x^4)

        TESTS::

            sage: L.<z> = LazyLaurentSeriesRing(QQ)
            sage: zero = L.zero()
            sage: zero.shift(10) is zero
            True

            sage: f = 1 / (1 + 2*z + z^2)
            sage: f.shift(5).shift(-5) - f
            0

            sage: L.<x> = LazyPowerSeriesRing(QQ)
            sage: M = L.fraction_field()
            sage: f = x.shift(-3); f
            0
            sage: f = M(x).shift(-3); f
            x^-2
            sage: f.parent()
            Lazy Laurent Series Ring in x over Rational Field

            sage: L.<x, y> = LazyPowerSeriesRing(QQ)
            sage: f = x.shift(2)
            Traceback (most recent call last):
            ...
            ValueError: arity must be equal to 1

            sage: L.<x> = LazyPowerSeriesRing(QQ)
            sage: f = L([1,2,3,4])
            sage: f.shift(-10) == L.zero()
            True

        Check the truncation works correctly::

            sage: f = L(lambda n: 1 if ZZ(n).is_power_of(2) else 0)
            sage: f.valuation()
            1
            sage: f._coeff_stream._true_order
            True
            sage: g = f.shift(-5)
            sage: g
            x^3 + O(x^7)
            sage: g._coeff_stream._approximate_order
            3
            sage: g._coeff_stream._true_order
            True
            sage: g.valuation()
            3

            sage: f = L(lambda n: 1 if ZZ(n).is_power_of(2) else 0)
            sage: g = f.shift(-5)
            sage: g._coeff_stream._approximate_order
            0
            sage: g._coeff_stream._true_order
            False
            sage: g.valuation()
            3

            sage: f = L([1,2,3,4], constant=7)
            sage: fs = f.shift(-4)
            sage: fs = f.shift(-4); fs
            7 + 7*x + 7*x^2 + O(x^3)
            sage: fs.shift(4)
            7*x^4 + 7*x^5 + 7*x^6 + O(x^7)

            sage: f = L([1,2,3,4], constant=0)
            sage: type(f.shift(-5)._coeff_stream)
            <class 'sage.data_structures.stream.Stream_zero'>
        """
    __lshift__ = shift
    def __rshift__(self, n):
        """
        Return ``self`` with the indices shifted right by ``n``.

        For example, a Laurent series is multiplied by the power `z^-n`,
        where `z` is the variable of ``self``.

        EXAMPLES::

            sage: L.<z> = LazyLaurentSeriesRing(ZZ)
            sage: f = 1/(1 + 2*z); f
            1 - 2*z + 4*z^2 - 8*z^3 + 16*z^4 - 32*z^5 + 64*z^6 + O(z^7)
            sage: f >> 3
            z^-3 - 2*z^-2 + 4*z^-1 - 8 + 16*z - 32*z^2 + 64*z^3 + O(z^4)
            sage: f >> -3
            z^3 - 2*z^4 + 4*z^5 - 8*z^6 + 16*z^7 - 32*z^8 + 64*z^9 + O(z^10)
        """
    def prec(self):
        """
        Return the precision of the series, which is infinity.

        EXAMPLES::

            sage: L.<z> = LazyLaurentSeriesRing(ZZ)
            sage: f = 1/(1 - z)
            sage: f.prec()
            +Infinity
        """
    def lift_to_precision(self, absprec=None):
        """
        Return another element of the same parent with absolute
        precision at least ``absprec``, congruent to this element
        modulo the precision of this element.

        Since the precision of a lazy series is infinity, this method
        returns the series itself, and the argument is ignored.

        EXAMPLES::

            sage: P.<t> = PowerSeriesRing(QQ, default_prec=2)
            sage: R.<z> = LazyPowerSeriesRing(P)
            sage: f = R(lambda n: 1/(1-t)^n)
            sage: f
            1 + ((1+t+O(t^2))*z) + ((1+2*t+O(t^2))*z^2)
              + ((1+3*t+O(t^2))*z^3)
              + ((1+4*t+O(t^2))*z^4)
              + ((1+5*t+O(t^2))*z^5)
              + ((1+6*t+O(t^2))*z^6) + O(z^7)
            sage: f.lift_to_precision()
            1 + ((1+t+O(t^2))*z) + ((1+2*t+O(t^2))*z^2)
              + ((1+3*t+O(t^2))*z^3)
              + ((1+4*t+O(t^2))*z^4)
              + ((1+5*t+O(t^2))*z^5)
              + ((1+6*t+O(t^2))*z^6) + O(z^7)
        """
    def __hash__(self):
        """
        Return the hash of ``self``.

        TESTS::

            sage: L = LazyLaurentSeriesRing(ZZ, 'z')
            sage: f = L([1,2,3,4], valuation=-5)
            sage: hash(f) == hash(f)
            True
            sage: g = (1 + f)/(1 - f)^2
            sage: {g: 1}
            {z^5 - 2*z^6 + z^7 + 5*z^9 - 11*z^10 + z^11 + O(z^12): 1}
        """
    def __bool__(self) -> bool:
        """
        Test whether ``self`` is not zero.

        When the halting precision is infinite, then any series that is
        not known to be zero will be ``True``.

        TESTS::

            sage: # needs sage.rings.finite_rings
            sage: L.<z> = LazyLaurentSeriesRing(GF(2))
            sage: bool(z - z)
            False
            sage: bool(1/(1 - z))
            True
            sage: M = L(lambda n: n, valuation=0); M
            z + z^3 + z^5 + O(z^7)
            sage: M.is_zero()
            False
            sage: M = L(lambda n: 2*n if n < 10 else 1, valuation=0); M
            O(z^7)
            sage: bool(M)
            True

        With the `secure` option, we raise an error if we cannot know
        whether the series is zero or not::

            sage: # needs sage.rings.finite_rings
            sage: L.options.secure = True
            sage: bool(M)
            Traceback (most recent call last):
            ...
            ValueError: undecidable
            sage: M[15]
            1
            sage: bool(M)
            True

            sage: # needs sage.rings.finite_rings
            sage: L.<z> = LazyLaurentSeriesRing(GF(2), sparse=True)
            sage: M = L(lambda n: 2*n if n < 10 else 1, valuation=0); M
            O(z^7)
            sage: bool(M)
            Traceback (most recent call last):
            ...
            ValueError: undecidable
            sage: M[15]
            1
            sage: bool(M)
            True
            sage: L.options._reset()

        Uninitialized series::

            sage: # needs sage.rings.finite_rings
            sage: g = L.undefined(valuation=0)
            sage: bool(g)
            True
            sage: g.define(0)
            sage: bool(g)
            False

            sage: # needs sage.rings.finite_rings
            sage: g = L.undefined(valuation=0)
            sage: bool(g)
            True
            sage: g.define(1 + z)
            sage: bool(g)
            True

            sage: # needs sage.rings.finite_rings
            sage: g = L.undefined(valuation=0)
            sage: bool(g)
            True
            sage: g.define(1 + z*g)
            sage: bool(g)
            True

        Comparison with finite halting precision::

            sage: # needs sage.rings.finite_rings
            sage: M = L(lambda n: 2*n if n < 10 else 0, valuation=0)
            sage: bool(M)
            True
            sage: M.is_zero()
            False

            sage: # needs sage.rings.finite_rings
            sage: L.options.halting_precision = 20
            sage: bool(M)
            False
            sage: M.is_zero()
            True

        With finite halting precision, it can be considered to
        be indistinguishable from zero until possibly enough
        coefficients are computed::

            sage: # needs sage.rings.finite_rings
            sage: L.<z> = LazyLaurentSeriesRing(GF(2))
            sage: L.options.halting_precision = 20
            sage: f = L(lambda n: 0, valuation=0)
            sage: f.is_zero()
            True

            sage: # needs sage.rings.finite_rings
            sage: g = L(lambda n: 0 if n < 50 else 1, valuation=2)
            sage: bool(g)  # checks up to degree 22 = 2 + 20
            False
            sage: bool(g)  # checks up to degree 42 = 22 + 20
            False
            sage: bool(g)  # checks up to degree 62 = 42 + 20
            True
            sage: L.options._reset()
        """
    def is_nonzero(self, proof: bool = False):
        """
        Return ``True`` if ``self`` is *known* to be nonzero.

        INPUT:

        - ``proof`` -- boolean (default: ``False``); if ``True``, this will
          also return an index such that ``self`` has a nonzero coefficient

        .. WARNING::

            If the stream is exactly zero, this will run forever.

        EXAMPLES:

        A series that it not known to be nonzero with no halting precision::

            sage: L.<z> = LazyLaurentSeriesRing(GF(2))
            sage: f = L(lambda n: 0, valuation=0)
            sage: f.is_nonzero()
            False
            sage: bool(f)
            True
            sage: g = L(lambda n: 0 if n < 50 else 1, valuation=2)
            sage: g.is_nonzero()
            False
            sage: g[60]
            1
            sage: g.is_nonzero()
            True

        With finite halting precision, it can be considered to
        be indistinguishable from zero until possibly enough
        coefficients are computed::

            sage: L.options.halting_precision = 20
            sage: f = L(lambda n: 0, valuation=0)
            sage: f.is_zero()
            True

            sage: g = L(lambda n: 0 if n < 50 else 1, valuation=2)
            sage: g.is_nonzero()  # checks up to degree 22 = 2 + 20
            False
            sage: g.is_nonzero()  # checks up to degree 42 = 22 + 20
            False
            sage: g.is_nonzero()  # checks up to degree 62 = 42 + 20
            True
            sage: L.options._reset()

        With a proof::

            sage: L.<z> = LazyLaurentSeriesRing(GF(5))
            sage: g = L(lambda n: 5 if n < 50 else 1, valuation=2)
            sage: g.is_nonzero(proof=True)
            (True, 50)

            sage: L.zero().is_nonzero(proof=True)
            (False, None)
        """
    def is_trivial_zero(self):
        """
        Return whether ``self`` is known to be trivially zero.

        EXAMPLES::

            sage: L.<z> = LazyLaurentSeriesRing(ZZ)
            sage: f = L(lambda n: 0, valuation=2)
            sage: f.is_trivial_zero()
            False

            sage: L.zero().is_trivial_zero()
            True
        """
    def define(self, s) -> None:
        '''
        Define an equation by ``self = s``.

        INPUT:

        - ``s`` -- a lazy series

        EXAMPLES:

        We begin by constructing the Catalan numbers::

            sage: L.<z> = LazyPowerSeriesRing(ZZ)
            sage: C = L.undefined()
            sage: C.define(1 + z*C^2)
            sage: C
            1 + z + 2*z^2 + 5*z^3 + 14*z^4 + 42*z^5 + 132*z^6 + O(z^7)
            sage: binomial(2000, 1000) / C[1000]                                        # needs sage.symbolic
            1001

        The Catalan numbers but with a valuation `1`::

            sage: B = L.undefined(valuation=1)
            sage: B.define(z + B^2)
            sage: B
            z + z^2 + 2*z^3 + 5*z^4 + 14*z^5 + 42*z^6 + 132*z^7 + O(z^8)

        We can define multiple series that are linked::

            sage: s = L.undefined()
            sage: t = L.undefined()
            sage: s.define(1 + z*t^3)
            sage: t.define(1 + z*s^2)
            sage: s[0:9]
            [1, 1, 3, 9, 34, 132, 546, 2327, 10191]
            sage: t[0:9]
            [1, 1, 2, 7, 24, 95, 386, 1641, 7150]

        A bigger example::

            sage: L.<z> = LazyPowerSeriesRing(ZZ)
            sage: A = L.undefined(valuation=5)
            sage: B = L.undefined()
            sage: C = L.undefined(valuation=2)
            sage: A.define(z^5 + B^2)
            sage: B.define(z^5 + C^2)
            sage: C.define(z^2 + C^2 + A^2)
            sage: A[0:15]
            [0, 0, 0, 0, 0, 1, 0, 0, 1, 2, 5, 4, 14, 10, 48]
            sage: B[0:15]
            [0, 0, 0, 0, 1, 1, 2, 0, 5, 0, 14, 0, 44, 0, 138]
            sage: C[0:15]
            [0, 0, 1, 0, 1, 0, 2, 0, 5, 0, 15, 0, 44, 2, 142]

        Counting binary trees::

            sage: L.<z> = LazyPowerSeriesRing(QQ)
            sage: s = L.undefined(valuation=1)
            sage: s.define(z + (s^2+s(z^2))/2)
            sage: s[0:9]
            [0, 1, 1, 1, 2, 3, 6, 11, 23]

        The `q`-Catalan numbers::

            sage: R.<q> = ZZ[]
            sage: L.<z> = LazyLaurentSeriesRing(R)
            sage: s = L.undefined(valuation=0)
            sage: s.define(1+z*s*s(q*z))
            sage: s
            1 + z + (q + 1)*z^2 + (q^3 + q^2 + 2*q + 1)*z^3
             + (q^6 + q^5 + 2*q^4 + 3*q^3 + 3*q^2 + 3*q + 1)*z^4
             + (q^10 + q^9 + 2*q^8 + 3*q^7 + 5*q^6 + 5*q^5 + 7*q^4 + 7*q^3 + 6*q^2 + 4*q + 1)*z^5
             + (q^15 + q^14 + 2*q^13 + 3*q^12 + 5*q^11 + 7*q^10 + 9*q^9 + 11*q^8
                + 14*q^7 + 16*q^6 + 16*q^5 + 17*q^4 + 14*q^3 + 10*q^2 + 5*q + 1)*z^6 + O(z^7)

        We count unlabeled ordered trees by total number of nodes
        and number of internal nodes::

            sage: R.<q> = QQ[]
            sage: Q.<z> = LazyPowerSeriesRing(R)
            sage: leaf = z
            sage: internal_node = q * z
            sage: L = Q(constant=1, degree=1)
            sage: T = Q.undefined(valuation=1)
            sage: T.define(leaf + internal_node * L(T))
            sage: T[0:6]
            [0, 1, q, q^2 + q, q^3 + 3*q^2 + q, q^4 + 6*q^3 + 6*q^2 + q]

        Similarly for Dirichlet series::

            sage: L = LazyDirichletSeriesRing(ZZ, "z")
            sage: g = L(constant=1, valuation=2)
            sage: F = L.undefined()
            sage: F.define(1 + g*F)
            sage: F[:16]
            [1, 1, 1, 2, 1, 3, 1, 4, 2, 3, 1, 8, 1, 3, 3]
            sage: oeis(_)                                                       # optional - internet
            0: A002033: Number of perfect partitions of n.
            1: A074206: Kalmár\'s [Kalmar\'s] problem: number of ordered factorizations of n.
            ...

            sage: F = L.undefined()
            sage: F.define(1 + g*F*F)
            sage: F[:16]
            [1, 1, 1, 3, 1, 5, 1, 10, 3, 5, 1, 24, 1, 5, 5]

        We can compute the Frobenius character of unlabeled trees::

            sage: # needs sage.combinat
            sage: m = SymmetricFunctions(QQ).m()
            sage: s = SymmetricFunctions(QQ).s()
            sage: L = LazySymmetricFunctions(m)
            sage: E = L(lambda n: s[n], valuation=0)
            sage: X = L(s[1])
            sage: A = L.undefined()
            sage: A.define(X*E(A))
            sage: A[:6]
            [m[1],
             2*m[1, 1] + m[2],
             9*m[1, 1, 1] + 5*m[2, 1] + 2*m[3],
             64*m[1, 1, 1, 1] + 34*m[2, 1, 1] + 18*m[2, 2] + 13*m[3, 1] + 4*m[4],
             625*m[1, 1, 1, 1, 1] + 326*m[2, 1, 1, 1] + 171*m[2, 2, 1] + 119*m[3, 1, 1] + 63*m[3, 2] + 35*m[4, 1] + 9*m[5]]

        TESTS::

            sage: L.<z> = LazyLaurentSeriesRing(ZZ, sparse=True)
            sage: s = L.undefined(valuation=-1)
            sage: s.define(z^-1 + z^3*s^3)
            sage: s[-1:9]
            [1, 1, 3, 12, 55, 273, 1428, 7752, 43263, 246675]

            sage: e = L.undefined(valuation=0)
            sage: e.define(1 + z*e)
            sage: e.define(1 + z*e)
            Traceback (most recent call last):
            ...
            ValueError: series already defined
            sage: z.define(1 + z^2)
            Traceback (most recent call last):
            ...
            ValueError: series already defined

            sage: e = L.undefined(valuation=0)
            sage: e.define(1)
            sage: e
            1

            sage: e = L.undefined(valuation=0)
            sage: e.define((1 + z).polynomial())
            sage: e
            1 + z

            sage: D = LazyDirichletSeriesRing(QQ, "s")
            sage: L.<z> = LazyLaurentSeriesRing(QQ)
            sage: e = L(lambda n: 1/factorial(n), 0)
            sage: g = D.undefined(valuation=2)
            sage: o = D(constant=1, valuation=2)
            sage: g.define(o * e(g))
            sage: g                                                                     # needs sage.symbolic
            1/(2^s) + 1/(3^s) + 2/4^s + 1/(5^s) + 3/6^s + 1/(7^s) + 9/2/8^s + O(1/(9^s))

        For Laurent series there is no minimal valuation, so it has
        to be specified::

            sage: L.<z> = LazyLaurentSeriesRing(QQ)
            sage: L.undefined()
            Traceback (most recent call last):
            ...
            ValueError: the valuation must be specified for undefined series

        For power series and Dirichlet series there is a minimal
        valuation, which is why the following work::

            sage: P.<x> = LazyPowerSeriesRing(QQ)
            sage: f = P.undefined()
            sage: f.define(1 - ~f*x)
            sage: f
            1 - x - x^2 - 2*x^3 - 5*x^4 - 14*x^5 - 42*x^6 + O(x^7)

            sage: D = LazyDirichletSeriesRing(QQ, "s")
            sage: g = D([0, 1])
            sage: f = D.undefined()
            sage: f.define(1 + ~f*g)
            sage: f                                                                     # needs sage.symbolic
            1 + 1/(2^s) - 1/(4^s) + O(1/(8^s))

            sage: oeis(f[:30])                                                  # optional - internet
            0: A122698: a(1)=a(2)=1 then a(n) = Sum_{d|n, 1<d<n} a(d)*a(n/d).

        Note that we cannot use division in the examples above.
        Since we allow division by series with positive valuation,
        the valuation of `x / f` might be zero::

            sage: f = P.undefined()
            sage: f.define(1 - x / f)
            sage: f[0]
            Traceback (most recent call last):
            ...
            ValueError: inverse does not exist

        Check that reversion is lazy enough::

            sage: L.<t> = LazyPowerSeriesRing(QQ)
            sage: f = L.undefined()
            sage: f.define(1+(t*f).revert())
            sage: f
            1 + t - t^2 + 3*t^3 - 13*t^4 + 69*t^5 - 419*t^6 + O(t^7)

            sage: L.<t> = LazyLaurentSeriesRing(QQ)
            sage: f = L.undefined(valuation=0)
            sage: f.define(1+(t*f).revert())
            sage: f
            1 + t - t^2 + 3*t^3 - 13*t^4 + 69*t^5 - 419*t^6 + O(t^7)

            sage: f = L.undefined(valuation=0)
            sage: f.define(1+(t*~f).revert())
            sage: f
            1 + t + t^2 + 2*t^3 + 6*t^4 + 23*t^5 + 104*t^6 + O(t^7)
            sage: oeis(f[1:20])                                                 # optional - internet
            0: A030266: ...
            1: A110447: ...

        The following can only work for power series, where we have a
        minimal valuation of `0`::

            sage: L.<t> = LazyPowerSeriesRing(QQ)
            sage: f = L.undefined(valuation=0)
            sage: f.define(1 - t*~(-f) - (-t*f).revert())
            sage: f
            1 + 2*t + 12*t^3 + 32*t^4 + 368*t^5 + 2192*t^6 + O(t^7)

            sage: # needs sage.combinat
            sage: s = SymmetricFunctions(QQ).s()
            sage: L = LazySymmetricFunctions(s)
            sage: f = L.undefined()
            sage: f.define(1+(s[1]*f).revert())
            sage: f                                                                     # needs lrcalc_python
            s[] + s[1] + (-s[1,1]-s[2])
                + (3*s[1,1,1]+6*s[2,1]+3*s[3])
                + (-13*s[1,1,1,1]-39*s[2,1,1]-26*s[2,2]-39*s[3,1]-13*s[4])
                + (69*s[1,1,1,1,1]+276*s[2,1,1,1]+345*s[2,2,1]+414*s[3,1,1]+345*s[3,2]+276*s[4,1]+69*s[5])
                + (-419*s[1,1,1,1,1,1]-2095*s[2,1,1,1,1]-3771*s[2,2,1,1]-2095*s[2,2,2]-4190*s[3,1,1,1]-6704*s[3,2,1]-2095*s[3,3]-4190*s[4,1,1]-3771*s[4,2]-2095*s[5,1]-419*s[6])
                + O^7

            sage: (f*s[1]).revert() + 1 - f                                             # needs lrcalc_python sage.combinat
            O^7

        Undefined series inside of another series (see :issue:`35071`)::

            sage: L.<z> = LazyPowerSeriesRing(QQ)
            sage: f = z^2
            sage: b = L.undefined(valuation=1)
            sage: b.define(z*f(f(b)))
            sage: b
            O(z^8)

            sage: L.<x> = LazyPowerSeriesRing(ZZ)
            sage: f = L.undefined()
            sage: f.define(L(lambda n: 0 if not n else sigma(f[n-1]+1)))
            sage: f
            x + 3*x^2 + 7*x^3 + 15*x^4 + 31*x^5 + 63*x^6 + O(x^7)
            sage: f = L.undefined()
            sage: f.define((1/(1-L(lambda n: 0 if not n else sigma(f[n-1]+1)))))
            sage: f
            1 + 3*x + 16*x^2 + 87*x^3 + 607*x^4 + 4518*x^5 + 30549*x^6 + O(x^7)
        '''
    set = define
    def change_ring(self, ring):
        """
        Return ``self`` with coefficients converted to elements of ``ring``.

        INPUT:

        - ``ring`` -- a ring

        EXAMPLES:

        Dense Implementation::

            sage: L.<z> = LazyLaurentSeriesRing(ZZ, sparse=False)
            sage: s = 2 + z
            sage: t = s.change_ring(QQ)
            sage: t^-1
            1/2 - 1/4*z + 1/8*z^2 - 1/16*z^3 + 1/32*z^4 - 1/64*z^5 + 1/128*z^6 + O(z^7)
            sage: M = L(lambda n: n, valuation=0); M
            z + 2*z^2 + 3*z^3 + 4*z^4 + 5*z^5 + 6*z^6 + O(z^7)
            sage: N = M.change_ring(QQ)
            sage: N.parent()
            Lazy Laurent Series Ring in z over Rational Field
            sage: M.parent()
            Lazy Laurent Series Ring in z over Integer Ring

        Sparse Implementation::

            sage: L.<z> = LazyLaurentSeriesRing(ZZ, sparse=True)
            sage: M = L(lambda n: n, valuation=0); M
            z + 2*z^2 + 3*z^3 + 4*z^4 + 5*z^5 + 6*z^6 + O(z^7)
            sage: M.parent()
            Lazy Laurent Series Ring in z over Integer Ring
            sage: N = M.change_ring(QQ)
            sage: N.parent()
            Lazy Laurent Series Ring in z over Rational Field
            sage: M^-1
            z^-1 - 2 + z + O(z^6)

        A Dirichlet series example::

            sage: L = LazyDirichletSeriesRing(ZZ, 'z')
            sage: s = L(constant=2)
            sage: t = s.change_ring(QQ)
            sage: t.parent()
            Lazy Dirichlet Series Ring in z over Rational Field
            sage: it = t^-1
            sage: it                                                                    # needs sage.symbolic
            1/2 - 1/2/2^z - 1/2/3^z - 1/2/5^z + 1/2/6^z - 1/2/7^z + O(1/(8^z))

        A Taylor series example::

            sage: L.<z> = LazyPowerSeriesRing(ZZ)
            sage: s = 2 + z
            sage: t = s.change_ring(QQ)
            sage: t^-1
            1/2 - 1/4*z + 1/8*z^2 - 1/16*z^3 + 1/32*z^4 - 1/64*z^5 + 1/128*z^6 + O(z^7)
            sage: t.parent()
            Lazy Taylor Series Ring in z over Rational Field
        """
    def exp(self):
        '''
        Return the exponential series of ``self``.

        EXAMPLES::

            sage: L = LazyDirichletSeriesRing(QQ, "s")
            sage: Z = L(constant=1, valuation=2)
            sage: exp(Z)                                                                # needs sage.symbolic
            1 + 1/(2^s) + 1/(3^s) + 3/2/4^s + 1/(5^s) + 2/6^s + 1/(7^s) + O(1/(8^s))
        '''
    def log(self):
        '''
        Return the series for the natural logarithm of ``self``.

        EXAMPLES::

            sage: L = LazyDirichletSeriesRing(QQ, "s")
            sage: Z = L(constant=1)
            sage: log(Z)                                                                # needs sage.symbolic
            1/(2^s) + 1/(3^s) + 1/2/4^s + 1/(5^s) + 1/(7^s) + O(1/(8^s))
        '''
    def sin(self):
        '''
        Return the sine of ``self``.

        EXAMPLES::

            sage: L.<z> = LazyLaurentSeriesRing(QQ)
            sage: sin(z)
            z - 1/6*z^3 + 1/120*z^5 - 1/5040*z^7 + O(z^8)

            sage: sin(1 + z)
            Traceback (most recent call last):
            ...
            ValueError: can only compose with a positive valuation series

            sage: L.<x,y> = LazyPowerSeriesRing(QQ)
            sage: sin(x/(1-y)).polynomial(3)
            -1/6*x^3 + x*y^2 + x*y + x

        TESTS::

            sage: L.<z> = LazyLaurentSeriesRing(QQ); x = var("x")                       # needs sage.symbolic
            sage: sin(z)[0:6] == sin(x).series(x, 6).coefficients(sparse=False)
            True
        '''
    def cos(self):
        '''
        Return the cosine of ``self``.

        EXAMPLES::

            sage: L.<z> = LazyLaurentSeriesRing(QQ)
            sage: cos(z)
            1 - 1/2*z^2 + 1/24*z^4 - 1/720*z^6 + O(z^7)

            sage: L.<x,y> = LazyPowerSeriesRing(QQ)
            sage: cos(x/(1-y)).polynomial(4)
            1/24*x^4 - 3/2*x^2*y^2 - x^2*y - 1/2*x^2 + 1

        TESTS::

            sage: L.<z> = LazyLaurentSeriesRing(QQ); x = var("x")                       # needs sage.symbolic
            sage: cos(z)[0:6] == cos(x).series(x, 6).coefficients(sparse=False)         # needs sage.symbolic
            True
        '''
    def tan(self):
        '''
        Return the tangent of ``self``.

        EXAMPLES::

            sage: L.<z> = LazyLaurentSeriesRing(QQ)
            sage: tan(z)
            z + 1/3*z^3 + 2/15*z^5 + 17/315*z^7 + O(z^8)

            sage: L.<x,y> = LazyPowerSeriesRing(QQ)
            sage: tan(x/(1-y)).polynomial(5)
            2/15*x^5 + 2*x^3*y^2 + x*y^4 + x^3*y + x*y^3 + 1/3*x^3 + x*y^2 + x*y + x

        TESTS::

            sage: L.<z> = LazyLaurentSeriesRing(QQ); x = var("x")                       # needs sage.symbolic
            sage: tan(z)[0:6] == tan(x).series(x, 6).coefficients(sparse=False)         # needs sage.symbolic
            True
        '''
    def cot(self):
        '''
        Return the cotangent of ``self``.

        EXAMPLES::

            sage: L.<z> = LazyLaurentSeriesRing(QQ)
            sage: cot(z)
            z^-1 - 1/3*z - 1/45*z^3 - 2/945*z^5 + O(z^6)

            sage: L.<x> = LazyLaurentSeriesRing(QQ)
            sage: cot(x/(1-x)).polynomial(4)
            x^-1 - 1 - 1/3*x - 1/3*x^2 - 16/45*x^3 - 2/5*x^4

        TESTS::

            sage: L.<z> = LazyLaurentSeriesRing(QQ); x = var("x")                       # needs sage.symbolic
            sage: cot(z)[0:6] == cot(x).series(x, 6).coefficients(sparse=False)         # needs sage.symbolic
            True
        '''
    def csc(self):
        '''
        Return the cosecant of ``self``.

        EXAMPLES::

            sage: L.<z> = LazyLaurentSeriesRing(QQ)
            sage: csc(z)
            z^-1 + 1/6*z + 7/360*z^3 + 31/15120*z^5 + O(z^6)

            sage: L.<x> = LazyLaurentSeriesRing(QQ)
            sage: csc(x/(1-x)).polynomial(4)
            x^-1 - 1 + 1/6*x + 1/6*x^2 + 67/360*x^3 + 9/40*x^4

        TESTS::

            sage: L.<z> = LazyLaurentSeriesRing(QQ); x = var("x")                       # needs sage.symbolic
            sage: (z*csc(z))[0:6] == (x*csc(x)).series(x, 6).coefficients(sparse=False)             # needs sage.symbolic
            True
        '''
    def sec(self):
        '''
        Return the secant of ``self``.

        EXAMPLES::

            sage: L.<z> = LazyLaurentSeriesRing(QQ)
            sage: sec(z)
            1 + 1/2*z^2 + 5/24*z^4 + 61/720*z^6 + O(z^7)

            sage: L.<x,y> = LazyPowerSeriesRing(QQ)
            sage: sec(x/(1-y)).polynomial(4)
            5/24*x^4 + 3/2*x^2*y^2 + x^2*y + 1/2*x^2 + 1

        TESTS::

            sage: L.<z> = LazyLaurentSeriesRing(QQ); x = var("x")                       # needs sage.symbolic
            sage: sec(z)[0:6] == sec(x).series(x, 6).coefficients(sparse=False)         # needs sage.symbolic
            True
        '''
    def arcsin(self):
        '''
        Return the arcsine of ``self``.

        EXAMPLES::

            sage: L.<z> = LazyLaurentSeriesRing(QQ)
            sage: arcsin(z)
            z + 1/6*z^3 + 3/40*z^5 + 5/112*z^7 + O(z^8)

            sage: L.<x,y> = LazyPowerSeriesRing(QQ)
            sage: asin(x/(1-y))
            x + x*y + (1/6*x^3+x*y^2) + (1/2*x^3*y+x*y^3)
             + (3/40*x^5+x^3*y^2+x*y^4) + (3/8*x^5*y+5/3*x^3*y^3+x*y^5)
             + (5/112*x^7+9/8*x^5*y^2+5/2*x^3*y^4+x*y^6) + O(x,y)^8

        TESTS::

            sage: L.<z> = LazyLaurentSeriesRing(QQ); x = var("x")                       # needs sage.symbolic
            sage: asin(z)[0:6] == asin(x).series(x, 6).coefficients(sparse=False)       # needs sage.symbolic
            True
        '''
    def arccos(self):
        '''
        Return the arccosine of ``self``.

        EXAMPLES::

            sage: L.<z> = LazyLaurentSeriesRing(RR)
            sage: arccos(z)                                                             # needs sage.symbolic
            1.57079632679490 - 1.00000000000000*z + 0.000000000000000*z^2
             - 0.166666666666667*z^3 + 0.000000000000000*z^4
             - 0.0750000000000000*z^5 + O(1.00000000000000*z^7)

            sage: L.<z> = LazyLaurentSeriesRing(SR)                                     # needs sage.symbolic
            sage: arccos(z/(1-z))                                                       # needs sage.symbolic
            1/2*pi - z - z^2 - 7/6*z^3 - 3/2*z^4 - 83/40*z^5 - 73/24*z^6 + O(z^7)

            sage: L.<x,y> = LazyPowerSeriesRing(SR)                                     # needs sage.symbolic
            sage: arccos(x/(1-y))                                                       # needs sage.symbolic
            1/2*pi + (-x) + (-x*y) + ((-1/6)*x^3-x*y^2) + ((-1/2)*x^3*y-x*y^3)
             + ((-3/40)*x^5-x^3*y^2-x*y^4) + ((-3/8)*x^5*y+(-5/3)*x^3*y^3-x*y^5) + O(x,y)^7

        TESTS::

            sage: L.<z> = LazyLaurentSeriesRing(SR); x = var("x")                       # needs sage.symbolic
            sage: acos(z)[0:6] == acos(x).series(x, 6).coefficients(sparse=False)       # needs sage.symbolic
            True
        '''
    def arctan(self):
        '''
        Return the arctangent of ``self``.

        EXAMPLES::

            sage: L.<z> = LazyLaurentSeriesRing(QQ)
            sage: arctan(z)
            z - 1/3*z^3 + 1/5*z^5 - 1/7*z^7 + O(z^8)

            sage: L.<x,y> = LazyPowerSeriesRing(QQ)
            sage: atan(x/(1-y))
            x + x*y - (1/3*x^3-x*y^2) - (x^3*y-x*y^3) + (1/5*x^5-2*x^3*y^2+x*y^4)
            + (x^5*y-10/3*x^3*y^3+x*y^5) - (1/7*x^7-3*x^5*y^2+5*x^3*y^4-x*y^6) + O(x,y)^8

        TESTS::

            sage: L.<z> = LazyLaurentSeriesRing(QQ); x = var("x")                       # needs sage.symbolic
            sage: atan(z)[0:6] == atan(x).series(x, 6).coefficients(sparse=False)       # needs sage.symbolic
            True
        '''
    def arccot(self):
        '''
        Return the arctangent of ``self``.

        EXAMPLES::

            sage: L.<z> = LazyLaurentSeriesRing(RR)
            sage: arccot(z)                                                             # needs sage.symbolic
            1.57079632679490 - 1.00000000000000*z + 0.000000000000000*z^2
             + 0.333333333333333*z^3 + 0.000000000000000*z^4
             - 0.200000000000000*z^5 + O(1.00000000000000*z^7)

            sage: L.<z> = LazyLaurentSeriesRing(SR)                                     # needs sage.symbolic
            sage: arccot(z/(1-z))                                                       # needs sage.symbolic
            1/2*pi - z - z^2 - 2/3*z^3 + 4/5*z^5 + 4/3*z^6 + O(z^7)

            sage: L.<x,y> = LazyPowerSeriesRing(SR)                                     # needs sage.symbolic
            sage: acot(x/(1-y))                                                         # needs sage.symbolic
            1/2*pi + (-x) + (-x*y) + (1/3*x^3-x*y^2) + (x^3*y-x*y^3)
             + ((-1/5)*x^5+2*x^3*y^2-x*y^4) + (-x^5*y+10/3*x^3*y^3-x*y^5) + O(x,y)^7

        TESTS::

            sage: L.<z> = LazyLaurentSeriesRing(SR); x = var("x")                       # needs sage.symbolic
            sage: acot(z)[0:6] == acot(x).series(x, 6).coefficients(sparse=False)       # needs sage.symbolic
            True
        '''
    def sinh(self):
        '''
        Return the hyperbolic sine of ``self``.

        EXAMPLES::

            sage: L.<z> = LazyLaurentSeriesRing(QQ)
            sage: sinh(z)
            z + 1/6*z^3 + 1/120*z^5 + 1/5040*z^7 + O(z^8)

            sage: L.<x,y> = LazyPowerSeriesRing(QQ)
            sage: sinh(x/(1-y))
            x + x*y + (1/6*x^3+x*y^2) + (1/2*x^3*y+x*y^3)
             + (1/120*x^5+x^3*y^2+x*y^4) + (1/24*x^5*y+5/3*x^3*y^3+x*y^5)
             + (1/5040*x^7+1/8*x^5*y^2+5/2*x^3*y^4+x*y^6) + O(x,y)^8

        TESTS::

            sage: L.<z> = LazyLaurentSeriesRing(SR); x = var("x")                       # needs sage.symbolic
            sage: sinh(z)[0:6] == sinh(x).series(x, 6).coefficients(sparse=False)       # needs sage.symbolic
            True
        '''
    def cosh(self):
        '''
        Return the hyperbolic cosine of ``self``.

        EXAMPLES::

            sage: L.<z> = LazyLaurentSeriesRing(QQ)
            sage: cosh(z)
            1 + 1/2*z^2 + 1/24*z^4 + 1/720*z^6 + O(z^7)

            sage: L.<x,y> = LazyPowerSeriesRing(QQ)
            sage: cosh(x/(1-y))
            1 + 1/2*x^2 + x^2*y + (1/24*x^4+3/2*x^2*y^2) + (1/6*x^4*y+2*x^2*y^3)
             + (1/720*x^6+5/12*x^4*y^2+5/2*x^2*y^4) + O(x,y)^7

        TESTS::

            sage: L.<z> = LazyLaurentSeriesRing(SR); x = var("x")                       # needs sage.symbolic
            sage: cosh(z)[0:6] == cosh(x).series(x, 6).coefficients(sparse=False)       # needs sage.symbolic
            True
        '''
    def tanh(self):
        '''
        Return the hyperbolic tangent of ``self``.

        EXAMPLES::

            sage: L.<z> = LazyLaurentSeriesRing(QQ)
            sage: tanh(z)                                                               # needs sage.libs.flint
            z - 1/3*z^3 + 2/15*z^5 - 17/315*z^7 + O(z^8)

            sage: L.<x,y> = LazyPowerSeriesRing(QQ)
            sage: tanh(x/(1-y))                                                         # needs sage.libs.flint
            x + x*y - (1/3*x^3-x*y^2) - (x^3*y-x*y^3) + (2/15*x^5-2*x^3*y^2+x*y^4)
            + (2/3*x^5*y-10/3*x^3*y^3+x*y^5) - (17/315*x^7-2*x^5*y^2+5*x^3*y^4-x*y^6) + O(x,y)^8

        TESTS::

            sage: L.<z> = LazyLaurentSeriesRing(SR); x = var("x")                       # needs sage.symbolic
            sage: tanh(z)[0:6] == tanh(x).series(x, 6).coefficients(sparse=False)       # needs sage.symbolic
            True
        '''
    def coth(self):
        '''
        Return the hyperbolic cotangent of ``self``.

        EXAMPLES::

            sage: L.<z> = LazyLaurentSeriesRing(QQ)
            sage: coth(z)                                                               # needs sage.libs.flint
            z^-1 + 1/3*z - 1/45*z^3 + 2/945*z^5 + O(z^6)

            sage: coth(z + z^2)                                                         # needs sage.libs.flint
            z^-1 - 1 + 4/3*z - 2/3*z^2 + 44/45*z^3 - 16/15*z^4 + 884/945*z^5 + O(z^6)

        TESTS::

            sage: L.<z> = LazyLaurentSeriesRing(SR); x = var("x")                       # needs sage.symbolic
            sage: coth(z)[0:6] == coth(x).series(x, 6).coefficients(sparse=False)       # needs sage.symbolic
            True
        '''
    def sech(self):
        '''
        Return the hyperbolic secant of ``self``.

        EXAMPLES::

            sage: L.<z> = LazyLaurentSeriesRing(QQ)
            sage: sech(z)                                                               # needs sage.libs.flint
            1 - 1/2*z^2 + 5/24*z^4 - 61/720*z^6 + O(z^7)

            sage: L.<x, y> = LazyPowerSeriesRing(QQ)
            sage: sech(x/(1-y))                                                         # needs sage.libs.flint
            1 - 1/2*x^2 - x^2*y + (5/24*x^4-3/2*x^2*y^2) + (5/6*x^4*y-2*x^2*y^3)
            - (61/720*x^6-25/12*x^4*y^2+5/2*x^2*y^4) + O(x,y)^7

        TESTS::

            sage: L.<z> = LazyLaurentSeriesRing(SR); x = var("x")                       # needs sage.symbolic
            sage: sech(z)[0:6] == sech(x).series(x, 6).coefficients(sparse=False)       # needs sage.symbolic
            True
        '''
    def csch(self):
        '''
        Return the hyperbolic cosecant of ``self``.

        EXAMPLES::

            sage: L.<z> = LazyLaurentSeriesRing(QQ)
            sage: csch(z)                                                               # needs sage.libs.flint
            z^-1 - 1/6*z + 7/360*z^3 - 31/15120*z^5 + O(z^6)

            sage: L.<z> = LazyLaurentSeriesRing(QQ)
            sage: csch(z/(1-z))                                                         # needs sage.libs.flint
            z^-1 - 1 - 1/6*z - 1/6*z^2 - 53/360*z^3 - 13/120*z^4 - 787/15120*z^5 + O(z^6)

        TESTS::

            sage: L.<z> = LazyLaurentSeriesRing(SR); x = var("x")                       # needs sage.symbolic
            sage: csch(z)[0:6] == csch(x).series(x, 6).coefficients(sparse=False)       # needs sage.symbolic
            True
        '''
    def arcsinh(self):
        '''
        Return the inverse of the hyperbolic sine of ``self``.

        EXAMPLES::

            sage: L.<z> = LazyLaurentSeriesRing(QQ)
            sage: asinh(z)
            z - 1/6*z^3 + 3/40*z^5 - 5/112*z^7 + O(z^8)

        ``arcsinh`` is an alias::

            sage: arcsinh(z)
            z - 1/6*z^3 + 3/40*z^5 - 5/112*z^7 + O(z^8)

            sage: L.<x,y> = LazyPowerSeriesRing(QQ)
            sage: asinh(x/(1-y))
            x + x*y - (1/6*x^3-x*y^2) - (1/2*x^3*y-x*y^3) + (3/40*x^5-x^3*y^2+x*y^4)
            + (3/8*x^5*y-5/3*x^3*y^3+x*y^5) - (5/112*x^7-9/8*x^5*y^2+5/2*x^3*y^4-x*y^6) + O(x,y)^8

        TESTS::

            sage: L.<z> = LazyLaurentSeriesRing(SR); x = var("x")                       # needs sage.symbolic
            sage: asinh(z)[0:6] == asinh(x).series(x, 6).coefficients(sparse=False)     # needs sage.symbolic
            True
        '''
    def arctanh(self):
        '''
        Return the inverse of the hyperbolic tangent of ``self``.

        EXAMPLES::

            sage: L.<z> = LazyLaurentSeriesRing(QQ)
            sage: atanh(z)
            z + 1/3*z^3 + 1/5*z^5 + 1/7*z^7 + O(z^8)

        ``arctanh`` is an alias::

            sage: arctanh(z)
            z + 1/3*z^3 + 1/5*z^5 + 1/7*z^7 + O(z^8)

            sage: L.<x, y> = LazyPowerSeriesRing(QQ)
            sage: atanh(x/(1-y))
            x + x*y + (1/3*x^3+x*y^2) + (x^3*y+x*y^3) + (1/5*x^5+2*x^3*y^2+x*y^4)
             + (x^5*y+10/3*x^3*y^3+x*y^5) + (1/7*x^7+3*x^5*y^2+5*x^3*y^4+x*y^6) + O(x,y)^8

        TESTS::

            sage: L.<z> = LazyLaurentSeriesRing(SR); x = var("x")                       # needs sage.symbolic
            sage: atanh(z)[0:6] == atanh(x).series(x, 6).coefficients(sparse=False)     # needs sage.symbolic
            True
        '''
    def hypergeometric(self, a, b):
        '''
        Return the `{}_{p}F_{q}`-hypergeometric function
        `\\,_pF_{q}` where `(p,q)` is the parameterization of ``self``.

        INPUT:

        - ``a`` -- the first parameter of the hypergeometric function
        - ``b`` -- the second parameter of the hypergeometric function

        EXAMPLES::

            sage: L.<z> = LazyLaurentSeriesRing(QQ)
            sage: z.hypergeometric([1, 1], [1])
            1 + z + z^2 + z^3 + z^4 + z^5 + z^6 + O(z^7)
            sage: z.hypergeometric([], []) - exp(z)
            O(z^7)

            sage: L.<x,y> = LazyPowerSeriesRing(QQ)
            sage: (x+y).hypergeometric([1, 1], [1]).polynomial(4)
            x^4 + 4*x^3*y + 6*x^2*y^2 + 4*x*y^3 + y^4 + x^3 + 3*x^2*y
             + 3*x*y^2 + y^3 + x^2 + 2*x*y + y^2 + x + y + 1

        TESTS::

            sage: L.<z> = LazyLaurentSeriesRing(SR); x = var("x")                       # needs sage.symbolic
            sage: z.hypergeometric([1,1],[1])[0:6] == hypergeometric([1,1],[1], x).series(x, 6).coefficients(sparse=False)                                      # needs sage.symbolic
            True
        '''
    def q_pochhammer(self, q=None):
        """
        Return the infinite ``q``-Pochhammer symbol `(a; q)_{\\infty}`,
        where `a` is ``self``.

        This is also one version of the quantum dilogarithm or
        the `q`-Exponential function.

        .. SEEALSO::

            :meth:`sage.rings.lazy_series_ring.LazyLaurentSeriesRing.q_pochhammer`

        INPUT:

        - ``q`` -- (default: `q \\in \\QQ(q)`) the parameter `q`

        EXAMPLES::

            sage: q = ZZ['q'].fraction_field().gen()
            sage: L.<z> = LazyLaurentSeriesRing(q.parent())
            sage: qp = L.q_pochhammer(q)
            sage: (z + z^2).q_pochhammer(q) - qp(z + z^2)
            O(z^7)
        """
    def euler(self):
        """
        Return the Euler function evaluated at ``self``.

        The *Euler function* is defined as

        .. MATH::

            \\phi(z) = (z; z)_{\\infty}
            = \\sum_{n=0}^{\\infty} (-1)^n q^{(3n^2-n)/2}.

        .. SEEALSO::

            :meth:`sage.rings.lazy_series_ring.LazyLaurentSeriesRing.euler`

        EXAMPLES::

            sage: L.<q> = LazyLaurentSeriesRing(ZZ)
            sage: phi = L.euler()
            sage: (q + q^2).euler() - phi(q + q^2)
            O(q^7)
        """
    def jacobi_theta(self, w, a: int = 0, b: int = 0):
        """
        Return the Jacobi theta function `\\vartheta_{ab}(w; q)` evaluated
        with the nome `q` at ``self``.

        .. SEEALSO::

            :meth:`sage.rings.lazy_series_ring.LazyLaurentSeriesRing.jacobi_theta`

        EXAMPLES::

            sage: R.<w> = LaurentSeriesRing(QQ)
            sage: L.<q> = LazyLaurentSeriesRing(R)
            sage: theta = L.jacobi_theta(w)
            sage: (q + q^2).jacobi_theta(w) - theta(q + q^2)
            O(q^7)
        """
    def polylog(self, s):
        """
        Return the polylogarithm in ``s`` evaluated at ``self``.

        EXAMPLES::

            sage: L.<z> = LazyPowerSeriesRing(QQ)
            sage: z.polylog(-2)
            z + 4*z^2 + 9*z^3 + 16*z^4 + 25*z^5 + 36*z^6 + 49*z^7 + O(z^8)
            sage: (z + z^2).polylog(3)
            z + 9/8*z^2 + 31/108*z^3 + 145/576*z^4 + 3269/18000*z^5 + 421/2400*z^6
             + 213859/1234800*z^7 + O(z^8)
            sage: polylog(3, z)
            z + 1/8*z^2 + 1/27*z^3 + 1/64*z^4 + 1/125*z^5 + 1/216*z^6 + 1/343*z^7 + O(z^8)

        We verify an identity due to D.C. Wood (1992)::

            sage: n = 5
            sage: polylog(-n, z)
            z + 32*z^2 + 243*z^3 + 1024*z^4 + 3125*z^5 + 7776*z^6 + 16807*z^7 + O(z^8)
            sage: (-1)^(n+1) * sum(factorial(k) * stirling_number2(n+1,k+1)
            ....:                  * (-1/(1-z))^(k+1) for k in range(n+1))
            z + 32*z^2 + 243*z^3 + 1024*z^4 + 3125*z^5 + 7776*z^6 + O(z^7)

        We can pass more general values::

            sage: L.<z> = LazyPowerSeriesRing(SR)
            sage: s = SR.var('s')
            sage: z.polylog(s)
            z + 1/(2^s)*z^2 + 1/(3^s)*z^3 + 1/(4^s)*z^4 + 1/(5^s)*z^5
             + 1/(6^s)*z^6 + 1/(7^s)*z^7 + O(z^8)

        REFERENCES:

        - :wikipedia:`Polylogarithm`
        """
    def dilog(self):
        """
        Return the dilogarithm evaluated at ``self``.

        EXAMPLES::

            sage: L.<z> = LazyPowerSeriesRing(QQ)
            sage: z.dilog()
            z + 1/4*z^2 + 1/9*z^3 + 1/16*z^4 + 1/25*z^5 + 1/36*z^6 + 1/49*z^7 + O(z^8)
            sage: dilog(z)
            z + 1/4*z^2 + 1/9*z^3 + 1/16*z^4 + 1/25*z^5 + 1/36*z^6 + 1/49*z^7 + O(z^8)

        We check some dilogarithm identites::

            sage: dilog(z) + dilog(-z)
            1/2*z^2 + 1/8*z^4 + 1/18*z^6 + O(z^8)
            sage: dilog(z^2) / 2
            1/2*z^2 + 1/8*z^4 + 1/18*z^6 + 1/32*z^8 + O(z^9)

            sage: dilog(z) + dilog(z/(z-1))
            -1/2*z^2 - 1/2*z^3 - 11/24*z^4 - 5/12*z^5 - 137/360*z^6 - 7/20*z^7 + O(z^8)
            sage: -1/2 * log(1 - z)^2
            -1/2*z^2 - 1/2*z^3 - 11/24*z^4 - 5/12*z^5 - 137/360*z^6 - 7/20*z^7 - 363/1120*z^8 + O(z^9)

        REFERENCES:

        - :wikipedia:`Dilogarithm`
        """
    def __pow__(self, n):
        """
        Return the ``n``-th power of the series.

        INPUT:

        - ``n`` -- the power to which to raise the series; this may be a
          rational number, an element of the base ring, or an other series

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: D = LazyDirichletSeriesRing(QQ, 's')
            sage: Z = D(constant=1)
            sage: Z^2
            1 + 2/2^s + 2/3^s + 3/4^s + 2/5^s + 4/6^s + 2/7^s + O(1/(8^s))
            sage: f = Z^(1/3)
            sage: f
            1 + 1/3/2^s + 1/3/3^s + 2/9/4^s + 1/3/5^s + 1/9/6^s + 1/3/7^s + O(1/(8^s))
            sage: f^2
            1 + 2/3/2^s + 2/3/3^s + 5/9/4^s + 2/3/5^s + 4/9/6^s + 2/3/7^s + O(1/(8^s))
            sage: f^3 - Z
            O(1/(8^s))

            sage: L.<z> = LazyLaurentSeriesRing(QQ)
            sage: f = 1 + z
            sage: f^(1 / 2)
            1 + 1/2*z - 1/8*z^2 + 1/16*z^3 - 5/128*z^4 + 7/256*z^5 - 21/1024*z^6 + O(z^7)

            sage: f^f
            1 + z + z^2 + 1/2*z^3 + 1/3*z^4 + 1/12*z^5 + 3/40*z^6 + O(z^7)

            sage: q = ZZ['q'].fraction_field().gen()
            sage: L.<z> = LazyLaurentSeriesRing(q.parent())
            sage: f = (1 - z)^q
            sage: f
            1 - q*z + ((q^2 - q)/2)*z^2 + ((-q^3 + 3*q^2 - 2*q)/6)*z^3
             + ((q^4 - 6*q^3 + 11*q^2 - 6*q)/24)*z^4
             + ((-q^5 + 10*q^4 - 35*q^3 + 50*q^2 - 24*q)/120)*z^5
             + ((q^6 - 15*q^5 + 85*q^4 - 225*q^3 + 274*q^2 - 120*q)/720)*z^6
             + O(z^7)
        """
    def sqrt(self):
        '''
        Return ``self^(1/2)``.

        EXAMPLES::

            sage: L.<z> = LazyLaurentSeriesRing(QQ)
            sage: sqrt(1+z)
            1 + 1/2*z - 1/8*z^2 + 1/16*z^3 - 5/128*z^4 + 7/256*z^5 - 21/1024*z^6 + O(z^7)

            sage: L.<x,y> = LazyPowerSeriesRing(QQ)
            sage: sqrt(1+x/(1-y))
            1 + 1/2*x - (1/8*x^2-1/2*x*y) + (1/16*x^3-1/4*x^2*y+1/2*x*y^2)
            - (5/128*x^4-3/16*x^3*y+3/8*x^2*y^2-1/2*x*y^3)
            + (7/256*x^5-5/32*x^4*y+3/8*x^3*y^2-1/2*x^2*y^3+1/2*x*y^4)
            - (21/1024*x^6-35/256*x^5*y+25/64*x^4*y^2-5/8*x^3*y^3+5/8*x^2*y^4-1/2*x*y^5)
            + O(x,y)^7

        This also works for Dirichlet series::

            sage: # needs sage.symbolic
            sage: D = LazyDirichletSeriesRing(SR, "s")
            sage: Z = D(constant=1)
            sage: f = sqrt(Z);  f
            1 + 1/2/2^s + 1/2/3^s + 3/8/4^s + 1/2/5^s + 1/4/6^s + 1/2/7^s + O(1/(8^s))
            sage: f*f - Z
            O(1/(8^s))
        '''

class LazyCauchyProductSeries(LazyModuleElement):
    """
    A class for series where multiplication is the Cauchy product.

    EXAMPLES::

        sage: L.<z> = LazyLaurentSeriesRing(ZZ)
        sage: f = 1 / (1 - z)
        sage: f
        1 + z + z^2 + O(z^3)
        sage: f * (1 - z)
        1

        sage: L.<z> = LazyLaurentSeriesRing(ZZ, sparse=True)
        sage: f = 1 / (1 - z)
        sage: f
        1 + z + z^2 + O(z^3)
    """
    def valuation(self):
        """
        Return the valuation of ``self``.

        This method determines the valuation of the series by looking for a
        nonzero coefficient. Hence if the series happens to be zero, then it
        may run forever.

        EXAMPLES::

            sage: L.<z> = LazyLaurentSeriesRing(ZZ)
            sage: s = 1/(1 - z) - 1/(1 - 2*z)
            sage: s.valuation()
            1
            sage: t = z - z
            sage: t.valuation()
            +Infinity
            sage: M = L(lambda n: n^2, 0)
            sage: M.valuation()
            1
            sage: (M - M).valuation()
            +Infinity
        """
    def __pow__(self, n):
        """
        Return the ``n``-th power of the series.

        INPUT:

        - ``n`` -- integer; the power to which to raise the series

        EXAMPLES:

        Lazy Laurent series that have a dense implementation can be
        raised to the power ``n``::

            sage: L.<z> = LazyLaurentSeriesRing(ZZ, sparse=False)
            sage: (1 - z)^-1
            1 + z + z^2 + O(z^3)
            sage: (1 - z)^0
            1
            sage: (1 - z)^3
            1 - 3*z + 3*z^2 - z^3
            sage: (1 - z)^-3
            1 + 3*z + 6*z^2 + 10*z^3 + 15*z^4 + 21*z^5 + 28*z^6 + O(z^7)
            sage: M = L(lambda n: n, valuation=0); M
            z + 2*z^2 + 3*z^3 + 4*z^4 + 5*z^5 + 6*z^6 + O(z^7)
            sage: M^2
            z^2 + 4*z^3 + 10*z^4 + 20*z^5 + 35*z^6 + 56*z^7 + 84*z^8 + O(z^9)

        We can create a really large power of a monomial, even with
        the dense implementation::

            sage: z^1000000
            z^1000000

        Lazy Laurent series that have a sparse implementation can be
        raised to the power ``n``::

            sage: L.<z> = LazyLaurentSeriesRing(ZZ, sparse=True)
            sage: M = L(lambda n: n, valuation=0); M
            z + 2*z^2 + 3*z^3 + 4*z^4 + 5*z^5 + 6*z^6 + O(z^7)
            sage: M^2
            z^2 + 4*z^3 + 10*z^4 + 20*z^5 + 35*z^6 + 56*z^7 + 84*z^8 + O(z^9)

        Lazy Laurent series that are known to be exact can be raised
        to the power ``n``::

            sage: z^2
            z^2
            sage: (1 - z)^2
            1 - 2*z + z^2
            sage: (1 + z)^2
            1 + 2*z + z^2

        We also support the general case::

            sage: L.<z> = LazyLaurentSeriesRing(SR)                                     # needs sage.symbolic
            sage: (1 + z)^(1 + z)                                                       # needs sage.symbolic
            1 + z + z^2 + 1/2*z^3 + 1/3*z^4 + 1/12*z^5 + 3/40*z^6 + O(z^7)

        TESTS:

        Check that :issue:`36154` is fixed::

            sage: L.<z> = LazyLaurentSeriesRing(Zmod(4))
            sage: f = L([2])
            sage: f^2
            0
        """
    def __invert__(self):
        """
        Return the multiplicative inverse of the element.

        EXAMPLES:

        Lazy Laurent series that have a dense implementation can be inverted::

            sage: L.<z> = LazyLaurentSeriesRing(ZZ, sparse=False)
            sage: ~(1 - z)
            1 + z + z^2 + O(z^3)
            sage: M = L(lambda n: n, valuation=0); M
            z + 2*z^2 + 3*z^3 + 4*z^4 + 5*z^5 + 6*z^6 + O(z^7)
            sage: P = ~M; P
            z^-1 - 2 + z + O(z^6)

        Lazy Laurent series that have a sparse implementation can be inverted::

            sage: L.<z> = LazyLaurentSeriesRing(ZZ, sparse=True)
            sage: M = L(lambda n: n, valuation=0); M
            z + 2*z^2 + 3*z^3 + 4*z^4 + 5*z^5 + 6*z^6 + O(z^7)
            sage: P = ~M; P
            z^-1 - 2 + z + O(z^6)

            sage: ~(~(1 - z))
            1 - z

        Lazy Laurent series that are known to be exact can be inverted::

            sage: ~z
            z^-1

        We can also compute the multiplicative inverse of a symmetric
        function::

            sage: # needs sage.modules
            sage: h = SymmetricFunctions(QQ).h()
            sage: p = SymmetricFunctions(QQ).p()
            sage: L = LazySymmetricFunctions(p)
            sage: E = L(lambda n: h[n])
            sage: (~E)[:4]
            [p[], -p[1], 1/2*p[1, 1] - 1/2*p[2], -1/6*p[1, 1, 1] + 1/2*p[2, 1] - 1/3*p[3]]

            sage: (E * ~E)[:6]                                                          # needs sage.modules
            [p[], 0, 0, 0, 0, 0]

        TESTS::

            sage: L.<x> = LazyLaurentSeriesRing(QQ)
            sage: g = L([2], valuation=-1, constant=1); g
            2*x^-1 + 1 + x + x^2 + O(x^3)
            sage: g * g^-1
            1

            sage: L.<x> = LazyPowerSeriesRing(QQ)
            sage: ~(x + x^2)
            Traceback (most recent call last):
            ...
            ZeroDivisionError: cannot divide by a series of positive valuation

        Check that :issue:`36253` is fixed::

            sage: f = L(lambda n: n)
            sage: ~f
            Traceback (most recent call last):
            ...
            ZeroDivisionError: cannot divide by a series of positive valuation
        """
    def exp(self):
        '''
        Return the exponential series of ``self``.

        We use the identity

        .. MATH::

            \\exp(s) = 1 + \\int s\' \\exp(s).

        EXAMPLES::

            sage: L.<z> = LazyLaurentSeriesRing(QQ)
            sage: exp(z)
            1 + z + 1/2*z^2 + 1/6*z^3 + 1/24*z^4 + 1/120*z^5 + 1/720*z^6 + O(z^7)
            sage: exp(z + z^2)
            1 + z + 3/2*z^2 + 7/6*z^3 + 25/24*z^4 + 27/40*z^5 + 331/720*z^6 + O(z^7)
            sage: exp(0)                                                                # needs sage.symbolic
            1
            sage: exp(1 + z)
            Traceback (most recent call last):
            ...
            ValueError: can only compose with a positive valuation series

            sage: L.<x,y> = LazyPowerSeriesRing(QQ)
            sage: exp(x+y)[4].factor()
            (1/24) * (x + y)^4
            sage: exp(x/(1-y)).polynomial(3)
            1/6*x^3 + x^2*y + x*y^2 + 1/2*x^2 + x*y + x + 1

        TESTS::

            sage: L.<z> = LazyLaurentSeriesRing(QQ); x = var("x")                       # needs sage.symbolic
            sage: exp(z)[0:6] == exp(x).series(x, 6).coefficients(sparse=False)
            True

        Check the exponential when the base ring is a lazy ring::

            sage: L.<t> = LazyPowerSeriesRing(QQ)
            sage: M.<x> = LazyPowerSeriesRing(L)
            sage: exp(x)
            1 + x + 1/2*x^2 + 1/6*x^3 + 1/24*x^4 + 1/120*x^5 + 1/720*x^6 + O(x^7)
        '''
    def log(self):
        '''
        Return the series for the natural logarithm of ``self``.

        We use the identity

        .. MATH::

            \\log(s) = \\int s\' / s.

        EXAMPLES::

            sage: L.<z> = LazyLaurentSeriesRing(QQ)
            sage: log(1/(1-z))
            z + 1/2*z^2 + 1/3*z^3 + 1/4*z^4 + 1/5*z^5 + 1/6*z^6 + 1/7*z^7 + O(z^8)

            sage: L.<x, y> = LazyPowerSeriesRing(QQ)
            sage: log((1 + x/(1-y))).polynomial(3)
            1/3*x^3 - x^2*y + x*y^2 - 1/2*x^2 + x*y + x

        TESTS::

            sage: L.<z> = LazyLaurentSeriesRing(QQ); x = var("x")                       # needs sage.symbolic
            sage: log(1+z)[0:6] == log(1+x).series(x, 6).coefficients(sparse=False)     # needs sage.symbolic
            True

            sage: log(z)
            Traceback (most recent call last):
            ...
            ValueError: can only compose with a positive valuation series
        '''

class LazyLaurentSeries(LazyCauchyProductSeries):
    """
    A Laurent series where the coefficients are computed lazily.

    EXAMPLES::

        sage: L.<z> = LazyLaurentSeriesRing(ZZ)

    We can build a series from a function and specify if the series
    eventually takes a constant value::

        sage: f = L(lambda i: i, valuation=-3, constant=-1, degree=3)
        sage: f
        -3*z^-3 - 2*z^-2 - z^-1 + z + 2*z^2 - z^3 - z^4 - z^5 + O(z^6)
        sage: f[-2]
        -2
        sage: f[10]
        -1
        sage: f[-5]
        0

        sage: f = L(lambda i: i, valuation=-3)
        sage: f
        -3*z^-3 - 2*z^-2 - z^-1 + z + 2*z^2 + 3*z^3 + O(z^4)
        sage: f[20]
        20

    Anything that converts into a polynomial can be input, where
    we can also specify the valuation or if the series eventually
    takes a constant value::

        sage: L([-5,2,0,5])
        -5 + 2*z + 5*z^3
        sage: L([-5,2,0,5], constant=6)
        -5 + 2*z + 5*z^3 + 6*z^4 + 6*z^5 + 6*z^6 + O(z^7)
        sage: L([-5,2,0,5], degree=6, constant=6)
        -5 + 2*z + 5*z^3 + 6*z^6 + 6*z^7 + 6*z^8 + O(z^9)
        sage: L([-5,2,0,5], valuation=-2, degree=3, constant=6)
        -5*z^-2 + 2*z^-1 + 5*z + 6*z^3 + 6*z^4 + 6*z^5 + O(z^6)
        sage: L([-5,2,0,5], valuation=5)
        -5*z^5 + 2*z^6 + 5*z^8
        sage: L({-2:9, 3:4}, constant=2, degree=5)
        9*z^-2 + 4*z^3 + 2*z^5 + 2*z^6 + 2*z^7 + O(z^8)

    We can also perform arithmetic::

        sage: f = 1 / (1 - z - z^2)
        sage: f
        1 + z + 2*z^2 + 3*z^3 + 5*z^4 + 8*z^5 + 13*z^6 + O(z^7)
        sage: f.coefficient(100)
        573147844013817084101
        sage: f = (z^-2 - 1 + 2*z) / (z^-1 - z + 3*z^2)
        sage: f
        z^-1 - z^2 - z^4 + 3*z^5 + O(z^6)

    However, we may not always be able to know when a result is
    exactly a polynomial::

        sage: f * (z^-1 - z + 3*z^2)
        z^-2 - 1 + 2*z + O(z^5)

    TESTS::

        sage: L.<z> = LazyLaurentSeriesRing(ZZ, sparse=True)
        sage: f = 1 / (1 - z - z^2)
        sage: TestSuite(f).run()

        sage: L.<z> = LazyLaurentSeriesRing(ZZ, sparse=False)
        sage: f = 1 / (1 - z - z^2)
        sage: TestSuite(f).run()
    """
    def is_unit(self):
        """
        Return whether this element is a unit in the ring.

        EXAMPLES::

            sage: L.<z> = LazyLaurentSeriesRing(ZZ)
            sage: (2*z).is_unit()
            False

            sage: (1 + 2*z).is_unit()
            True

            sage: (1 + 2*z^-1).is_unit()
            False

            sage: (z^3 + 4 - z^-2).is_unit()
            True
        """
    def __call__(self, g):
        '''
        Return the composition of ``self`` with ``g``.

        Given two Laurent series `f` and `g` over the same base ring, the
        composition `(f \\circ g)(z) = f(g(z))` is defined if and only if:

        - `g = 0` and `\\mathrm{val}(f) \\geq 0`,
        - `g` is nonzero and `f` has only finitely many nonzero coefficients,
        - `g` is nonzero and `\\mathrm{val}(g) > 0`.

        INPUT:

        - ``g`` -- other series

        EXAMPLES::

            sage: L.<z> = LazyLaurentSeriesRing(QQ)
            sage: f = z^2 + 1 + z
            sage: f(0)
            1
            sage: f(L(0))
            1
            sage: f(f)
            3 + 3*z + 4*z^2 + 2*z^3 + z^4
            sage: g = z^-3/(1-2*z); g
            z^-3 + 2*z^-2 + 4*z^-1 + 8 + 16*z + 32*z^2 + 64*z^3 + O(z^4)
            sage: f(g)
            z^-6 + 4*z^-5 + 12*z^-4 + 33*z^-3 + 82*z^-2 + 196*z^-1 + 457 + O(z)
            sage: g^2 + 1 + g
            z^-6 + 4*z^-5 + 12*z^-4 + 33*z^-3 + 82*z^-2 + 196*z^-1 + 457 + O(z)
            sage: f(int(2))
            7

            sage: f = z^-2 + z + 4*z^3
            sage: f(f)
            4*z^-6 + 12*z^-3 + z^-2 + 48*z^-1 + 12 + O(z)
            sage: f^-2 + f + 4*f^3
            4*z^-6 + 12*z^-3 + z^-2 + 48*z^-1 + 12 + O(z)
            sage: f(g)
            4*z^-9 + 24*z^-8 + 96*z^-7 + 320*z^-6 + 960*z^-5 + 2688*z^-4 + 7169*z^-3 + O(z^-2)
            sage: g^-2 + g + 4*g^3
            4*z^-9 + 24*z^-8 + 96*z^-7 + 320*z^-6 + 960*z^-5 + 2688*z^-4 + 7169*z^-3 + O(z^-2)

            sage: f = z^-3 + z^-2 + 1 / (1 + z^2); f
            z^-3 + z^-2 + 1 - z^2 + O(z^4)
            sage: g = z^3 / (1 + z - z^3); g
            z^3 - z^4 + z^5 - z^7 + 2*z^8 - 2*z^9 + O(z^10)
            sage: f(g)
            z^-9 + 3*z^-8 + 3*z^-7 - z^-6 - 4*z^-5 - 2*z^-4 + z^-3 + O(z^-2)
            sage: g^-3 + g^-2 + 1 / (1 + g^2)
            z^-9 + 3*z^-8 + 3*z^-7 - z^-6 - 4*z^-5 - 2*z^-4 + z^-3 + O(z^-2)

            sage: f = z^-3
            sage: g = z^-2 + z^-1
            sage: g^(-3)
            z^6 - 3*z^7 + 6*z^8 - 10*z^9 + 15*z^10 - 21*z^11 + 28*z^12 + O(z^13)
            sage: f(g)
            z^6 - 3*z^7 + 6*z^8 - 10*z^9 + 15*z^10 - 21*z^11 + 28*z^12 + O(z^13)

            sage: f = z^2 + z^3
            sage: g = z^-3 + z^-2
            sage: f^-3 + f^-2
            z^-6 - 3*z^-5 + 7*z^-4 - 12*z^-3 + 18*z^-2 - 25*z^-1 + 33 + O(z)
            sage: g(f)
            z^-6 - 3*z^-5 + 7*z^-4 - 12*z^-3 + 18*z^-2 - 25*z^-1 + 33 + O(z)
            sage: g^2 + g^3
            z^-9 + 3*z^-8 + 3*z^-7 + 2*z^-6 + 2*z^-5 + z^-4
            sage: f(g)
            z^-9 + 3*z^-8 + 3*z^-7 + 2*z^-6 + 2*z^-5 + z^-4

            sage: f = L(lambda n: n, valuation=0); f
            z + 2*z^2 + 3*z^3 + 4*z^4 + 5*z^5 + 6*z^6 + O(z^7)
            sage: f(z^2)
            z^2 + 2*z^4 + 3*z^6 + 4*z^8 + O(z^9)

            sage: f = L(lambda n: n, valuation=-2); f
            -2*z^-2 - z^-1 + z + 2*z^2 + 3*z^3 + 4*z^4 + O(z^5)
            sage: f3 = f(z^3); f3
            -2*z^-6 - z^-3 + O(z)
            sage: [f3[i] for i in range(-6,13)]
            [-2, 0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 2, 0, 0, 3, 0, 0, 4]

        We compose a Laurent polynomial with a generic element::

            sage: R.<x> = QQ[]
            sage: f = z^2 + 1 + z^-1
            sage: g = x^2 + x + 3
            sage: f(g)
            (x^6 + 3*x^5 + 12*x^4 + 19*x^3 + 37*x^2 + 28*x + 31)/(x^2 + x + 3)
            sage: f(g) == g^2 + 1 + g^-1
            True

        We compose with another lazy Laurent series::

            sage: LS.<y> = LazyLaurentSeriesRing(QQ)
            sage: f = z^2 + 1 + z^-1
            sage: fy = f(y); fy
            y^-1 + 1 + y^2
            sage: fy.parent() is LS
            True
            sage: g = y - y
            sage: f(g)
            Traceback (most recent call last):
            ...
            ZeroDivisionError: the valuation of the series must be nonnegative

            sage: g = 1 - y
            sage: f(g)
            3 - y + 2*y^2 + y^3 + y^4 + y^5 + O(y^6)
            sage: g^2 + 1 + g^-1
            3 - y + 2*y^2 + y^3 + y^4 + y^5 + O(y^6)

            sage: f = L(lambda n: n, valuation=0); f
            z + 2*z^2 + 3*z^3 + 4*z^4 + 5*z^5 + 6*z^6 + O(z^7)
            sage: f(0)
            0
            sage: f(y)
            y + 2*y^2 + 3*y^3 + 4*y^4 + 5*y^5 + 6*y^6 + 7*y^7 + O(y^8)
            sage: fp = f(y - y)
            sage: fp == 0
            True
            sage: fp.parent() is LS
            True

            sage: f = z^2 + 3 + z
            sage: f(y - y)
            3

        With both of them sparse::

            sage: L.<z> = LazyLaurentSeriesRing(QQ, sparse=True)
            sage: LS.<y> = LazyLaurentSeriesRing(QQ, sparse=True)
            sage: f = L(lambda n: 1, valuation=0); f
            1 + z + z^2 + z^3 + z^4 + z^5 + z^6 + O(z^7)
            sage: f(y^2)
            1 + y^2 + y^4 + y^6 + O(y^7)

            sage: fp = f - 1 + z^-2; fp
            z^-2 + z + z^2 + z^3 + z^4 + O(z^5)
            sage: fpy = fp(y^2); fpy
            y^-4 + y^2 + O(y^3)
            sage: fpy.parent() is LS
            True
            sage: [fpy[i] for i in range(-4,11)]
            [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

            sage: g = LS(valuation=2, constant=1); g
            y^2 + y^3 + y^4 + O(y^5)
            sage: fg = f(g); fg
            1 + y^2 + y^3 + 2*y^4 + 3*y^5 + 5*y^6 + O(y^7)
            sage: 1 + g + g^2 + g^3 + g^4 + g^5 + g^6
            1 + y^2 + y^3 + 2*y^4 + 3*y^5 + 5*y^6 + O(y^7)

            sage: h = LS(lambda n: 1 if n % 2 else 0, valuation=2); h
            y^3 + y^5 + y^7 + O(y^9)
            sage: fgh = fg(h); fgh
            1 + y^6 + O(y^7)
            sage: [fgh[i] for i in range(0, 15)]
            [1, 0, 0, 0, 0, 0, 1, 0, 2, 1, 3, 3, 6, 6, 13]
            sage: t = 1 + h^2 + h^3 + 2*h^4 + 3*h^5 + 5*h^6
            sage: [t[i] for i in range(0, 15)]
            [1, 0, 0, 0, 0, 0, 1, 0, 2, 1, 3, 3, 6, 6, 13]

        We look at mixing the sparse and the dense::

            sage: L.<z> = LazyLaurentSeriesRing(QQ)
            sage: f = L(lambda n: 1, valuation=0); f
            1 + z + z^2 + z^3 + z^4 + z^5 + z^6 + O(z^7)
            sage: g = LS(lambda n: 1, valuation=1); g
            y + y^2 + y^3 + y^4 + y^5 + y^6 + y^7 + O(y^8)
            sage: f(g)
            1 + y + 2*y^2 + 4*y^3 + 8*y^4 + 16*y^5 + 32*y^6 + O(y^7)

            sage: f = z^-2 + 1 + z
            sage: g = 1/(y*(1-y)); g
            y^-1 + 1 + y + O(y^2)
            sage: f(g)
            y^-1 + 2 + y + 2*y^2 - y^3 + 2*y^4 + y^5 + y^6 + y^7 + O(y^8)
            sage: g^-2 + 1 + g == f(g)
            True

            sage: f = z^-3 + z^-2 + 1
            sage: g = 1/(y^2*(1-y)); g
            y^-2 + y^-1 + 1 + O(y)
            sage: f(g)
            1 + y^4 - 2*y^5 + 2*y^6 - 3*y^7 + 3*y^8 - y^9
            sage: g^-3 + g^-2 + 1 == f(g)
            True
            sage: z(y)
            y

        We look at cases where the composition does not exist.
        `g = 0` and `\\mathrm{val}(f) < 0`::

            sage: g = L(0)
            sage: f = z^-1 + z^-2
            sage: f.valuation() < 0
            True
            sage: f(g)
            Traceback (most recent call last):
            ...
            ZeroDivisionError: the valuation of the series must be nonnegative

        `g \\neq 0` and `\\mathrm{val}(g) \\leq 0` and `f` has infinitely many
        nonzero coefficients::

            sage: g = z^-1 + z^-2
            sage: g.valuation() <= 0
            True
            sage: f = L(lambda n: n, valuation=0)
            sage: f(g)
            Traceback (most recent call last):
            ...
            ValueError: can only compose with a positive valuation series

            sage: f = L(lambda n: n, valuation=1)
            sage: f(1 + z)
            Traceback (most recent call last):
            ...
            ValueError: can only compose with a positive valuation series

        We compose the exponential with a Dirichlet series::

            sage: L.<z> = LazyLaurentSeriesRing(QQ)
            sage: e = L(lambda n: 1/factorial(n), 0)
            sage: D = LazyDirichletSeriesRing(QQ, "s")
            sage: g = D(constant=1)-1
            sage: g                                                                     # needs sage.symbolic
            1/(2^s) + 1/(3^s) + 1/(4^s) + O(1/(5^s))

            sage: e(g)[0:10]
            [0, 1, 1, 1, 3/2, 1, 2, 1, 13/6, 3/2]

            sage: sum(g^k/factorial(k) for k in range(10))[0:10]
            [0, 1, 1, 1, 3/2, 1, 2, 1, 13/6, 3/2]

            sage: g = D([0,1,0,1,1,2])
            sage: g                                                                     # needs sage.symbolic
            1/(2^s) + 1/(4^s) + 1/(5^s) + 2/6^s
            sage: e(g)[0:10]
            [0, 1, 1, 0, 3/2, 1, 2, 0, 7/6, 0]
            sage: sum(g^k/factorial(k) for k in range(10))[0:10]
            [0, 1, 1, 0, 3/2, 1, 2, 0, 7/6, 0]

            sage: e(D([1,0,1]))
            Traceback (most recent call last):
            ...
            ValueError: can only compose with a positive valuation series

            sage: e5 = L(e, degree=5)
            sage: e5
            1 + z + 1/2*z^2 + 1/6*z^3 + 1/24*z^4
            sage: e5(g)                                                                 # needs sage.symbolic
            1 + 1/(2^s) + 3/2/4^s + 1/(5^s) + 2/6^s + O(1/(8^s))
            sage: sum(e5[k] * g^k for k in range(5))                                    # needs sage.symbolic
            1 + 1/(2^s) + 3/2/4^s + 1/(5^s) + 2/6^s + O(1/(8^s))

        The output parent is always the common parent between the base ring
        of `f` and the parent of `g` or extended to the corresponding
        lazy series::

            sage: L.<z> = LazyLaurentSeriesRing(QQ)
            sage: R.<x> = ZZ[]
            sage: parent(z(x))
            Univariate Polynomial Ring in x over Rational Field
            sage: parent(z(R.zero()))
            Univariate Polynomial Ring in x over Rational Field
            sage: parent(z(0))
            Rational Field
            sage: f = 1 / (1 - z)
            sage: f(x)
            1 + x + x^2 + x^3 + x^4 + x^5 + x^6 + O(x^7)
            sage: three = L(3)(x^2); three
            3
            sage: parent(three)
            Univariate Polynomial Ring in x over Rational Field

        Consistency check when `g` is an uninitialized series between a
        polynomial `f` as both a polynomial and a lazy series::

            sage: L.<z> = LazyLaurentSeriesRing(QQ)
            sage: f = 1 + z
            sage: g = L.undefined(valuation=0)
            sage: f(g) == f.polynomial()(g)
            True

        TESTS:

        Check that :issue:`36154` is fixed::

            sage: L.<z> = LazyLaurentSeriesRing(Zmod(4))
            sage: f = L([0,2])
            sage: g = L([2])
            sage: f(g)
            0
        '''
    compose = __call__
    def revert(self):
        """
        Return the compositional inverse of ``self``.

        Given a Laurent series `f`, the compositional inverse is a
        Laurent series `g` over the same base ring, such that
        `(f \\circ g)(z) = f(g(z)) = z`.

        The compositional inverse exists if and only if:

        - `\\mathrm{val}(f) = 1`, or

        - `f = a + b z` with `a, b \\neq 0`, or

        - `f = a/z` with `a \\neq 0`.

        EXAMPLES::

            sage: L.<z> = LazyLaurentSeriesRing(QQ)
            sage: (2*z).revert()
            1/2*z
            sage: (2/z).revert()
            2*z^-1
            sage: (z-z^2).revert()
            z + z^2 + 2*z^3 + 5*z^4 + 14*z^5 + 42*z^6 + 132*z^7 + O(z^8)

            sage: s = L(degree=1, constant=-1)
            sage: s.revert()
            -z - z^2 - z^3 + O(z^4)

            sage: s = L(degree=1, constant=1)
            sage: s.revert()
            z - z^2 + z^3 - z^4 + z^5 - z^6 + z^7 + O(z^8)

        .. WARNING::

            For series not known to be eventually constant (e.g., being
            defined by a function) with approximate valuation `\\leq 1`
            (but not necessarily its true valuation), this assumes
            that this is the actual valuation::

                sage: f = L(lambda n: n if n > 2 else 0, valuation=1)
                sage: f.revert()
                <repr(... failed: ValueError: inverse does not exist>

        TESTS::

            sage: L.<z> = LazyLaurentSeriesRing(QQ)
            sage: s = L(lambda n: 2 if n == 1 else 0, valuation=1); s
            2*z + O(z^8)
            sage: s.revert()
            1/2*z + O(z^8)

            sage: (2+3*z).revert()
            -2/3 + 1/3*z

            sage: s = L(lambda n: 2 if n == 0 else 3 if n == 1 else 0, valuation=0); s
            2 + 3*z + O(z^7)
            sage: f = s.revert()
            sage: f[1]
            Traceback (most recent call last):
            ...
            ValueError: inverse does not exist

            sage: s = L(lambda n: 1, valuation=-2); s
            z^-2 + z^-1 + 1 + z + z^2 + z^3 + z^4 + O(z^5)
            sage: f = s.revert()
            sage: f[1]
            Traceback (most recent call last):
            ...
            ValueError: inverse does not exist

            sage: R.<q,t> = QQ[]
            sage: L.<z> = LazyLaurentSeriesRing(R.fraction_field())
            sage: s = L([q], valuation=0, constant=t); s
            q + t*z + t*z^2 + t*z^3 + O(z^4)
            sage: s.revert()
            Traceback (most recent call last):
            ...
            ValueError: compositional inverse does not exist

        We look at some cases where the compositional inverse does not exist:

        `f = 0`::

            sage: L(0).revert()
            Traceback (most recent call last):
            ...
            ValueError: compositional inverse does not exist
            sage: (z - z).revert()
            Traceback (most recent call last):
            ...
            ValueError: compositional inverse does not exist

        `\\mathrm{val}(f) != 1` and `f(0) * f(1) = 0`::

            sage: (z^2).revert()
            Traceback (most recent call last):
            ...
            ValueError: compositional inverse does not exist

            sage: L(1).revert()
            Traceback (most recent call last):
            ...
            ValueError: compositional inverse does not exist

        Reversion of exact series::

            sage: f = L([2], valuation=-1, constant=2)
            sage: f.revert()
            Traceback (most recent call last):
            ...
            ValueError: compositional inverse does not exist

            sage: f = L([1, 2], valuation=0, constant=1)
            sage: f.revert()
            Traceback (most recent call last):
            ...
            ValueError: compositional inverse does not exist

            sage: f = L([-1, -1], valuation=1, constant=-1)
            sage: f.revert()
            -z - z^2 - z^3 + O(z^4)

            sage: f = L([-1, 0, -1], valuation=1, constant=-1)
            sage: f.revert()
            (1/(-1))*z + z^3 - z^4 - 2*z^5 + 6*z^6 + z^7 + O(z^8)

            sage: f = L([-1], valuation=1, degree=3, constant=-1)
            sage: f.revert()
            (1/(-1))*z + z^3 - z^4 - 2*z^5 + 6*z^6 + z^7 + O(z^8)
        """
    compositional_inverse = revert
    def derivative(self, *args):
        """
        Return the derivative of the Laurent series.

        Multiple variables and iteration counts may be supplied; see
        the documentation of
        :func:`sage.calculus.functional.derivative` function for
        details.

        EXAMPLES::

            sage: L.<z> = LazyLaurentSeriesRing(ZZ)
            sage: z.derivative()
            1
            sage: (1+z+z^2).derivative(3)
            0
            sage: (1/z).derivative()
            -z^-2
            sage: (1/(1-z)).derivative(z)
            1 + 2*z + 3*z^2 + 4*z^3 + 5*z^4 + 6*z^5 + 7*z^6 + O(z^7)

        TESTS:

        Check the derivative of the logarithm::

            sage: L.<z> = LazyLaurentSeriesRing(QQ)
            sage: -log(1-z).derivative()
            1 + z + z^2 + z^3 + z^4 + z^5 + z^6 + O(z^7)

        Check that differentiation of 'exact' series with nonzero
        constant works::

            sage: L.<z> = LazyLaurentSeriesRing(ZZ)
            sage: f = L([1,2], valuation=-2, constant=1)
            sage: f
            z^-2 + 2*z^-1 + 1 + z + z^2 + O(z^3)
            sage: f.derivative()
            -2*z^-3 - 2*z^-2 + 1 + 2*z + 3*z^2 + 4*z^3 + O(z^4)

        Check that differentiation with respect to a variable other
        than the series variable works::

            sage: R.<q> = QQ[]
            sage: L.<z> = LazyLaurentSeriesRing(R)
            sage: (z*q).derivative()
            q

            sage: (z*q).derivative(q)
            z

            sage: (z*q).derivative(q, z)
            1

            sage: f = 1/(1-q*z+z^2)
            sage: f
            1 + q*z + (q^2 - 1)*z^2 + (q^3 - 2*q)*z^3 + (q^4 - 3*q^2 + 1)*z^4 + (q^5 - 4*q^3 + 3*q)*z^5 + (q^6 - 5*q^4 + 6*q^2 - 1)*z^6 + O(z^7)
            sage: f.derivative(q)[3]
            3*q^2 - 2

        Check that :issue:`36154` is fixed::

            sage: L.<z> = LazyLaurentSeriesRing(Zmod(4))
            sage: f = L([0,0,2])
            sage: f.derivative()
            0
        """
    def integral(self, variable=None, *, constants=None):
        """
        Return the integral of ``self`` with respect to ``variable``.

        INPUT:

        - ``variable`` -- (optional) the variable to integrate
        - ``constants`` -- (optional; keyword-only) list of integration
          constants for the integrals of ``self`` (the last constant
          corresponds to the first integral)

        If the first argument is a list, then this method interprets it as
        integration constants. If it is a positive integer, the method
        interprets it as the number of times to integrate the function.
        If ``variable`` is not the variable of the Laurent series, then
        the coefficients are integrated with respect to ``variable``.

        If the integration constants are not specified, they are considered
        to be `0`.

        EXAMPLES::

            sage: L.<t> = LazyLaurentSeriesRing(QQ)
            sage: f = t^-3 + 2 + 3*t + t^5
            sage: f.integral()
            -1/2*t^-2 + 2*t + 3/2*t^2 + 1/6*t^6
            sage: f.integral([-2, -2])
            1/2*t^-1 - 2 - 2*t + t^2 + 1/2*t^3 + 1/42*t^7
            sage: f.integral(t)
            -1/2*t^-2 + 2*t + 3/2*t^2 + 1/6*t^6
            sage: f.integral(2)
            1/2*t^-1 + t^2 + 1/2*t^3 + 1/42*t^7
            sage: L.zero().integral()
            0
            sage: L.zero().integral([0, 1, 2, 3])
            t + t^2 + 1/2*t^3

        We solve the ODE `f' = a f` by integrating both sides and
        the recursive definition::

            sage: R.<a, C> = QQ[]
            sage: L.<x> = LazyLaurentSeriesRing(R)
            sage: f = L.undefined(0)
            sage: f.define((a*f).integral(constants=[C]))
            sage: f
            C + a*C*x + 1/2*a^2*C*x^2 + 1/6*a^3*C*x^3 + 1/24*a^4*C*x^4
             + 1/120*a^5*C*x^5 + 1/720*a^6*C*x^6 + O(x^7)
            sage: C * exp(a*x)
            C + a*C*x + 1/2*a^2*C*x^2 + 1/6*a^3*C*x^3 + 1/24*a^4*C*x^4
             + 1/120*a^5*C*x^5 + 1/720*a^6*C*x^6 + O(x^7)

        We can integrate both the series and coefficients::

            sage: R.<x,y,z> = QQ[]
            sage: L.<t> = LazyLaurentSeriesRing(R)
            sage: f = (x*t^2 + y*t^-2 + z)^2; f
            y^2*t^-4 + 2*y*z*t^-2 + (2*x*y + z^2) + 2*x*z*t^2 + x^2*t^4
            sage: f.integral(x)
            x*y^2*t^-4 + 2*x*y*z*t^-2 + (x^2*y + x*z^2) + x^2*z*t^2 + 1/3*x^3*t^4
            sage: f.integral(t)
            -1/3*y^2*t^-3 - 2*y*z*t^-1 + (2*x*y + z^2)*t + 2/3*x*z*t^3 + 1/5*x^2*t^5
            sage: f.integral(y, constants=[x*y*z])
            -1/9*y^3*t^-3 - y^2*z*t^-1 + x*y*z + (x*y^2 + y*z^2)*t + 2/3*x*y*z*t^3 + 1/5*x^2*y*t^5

        TESTS::

            sage: L.<t> = LazyLaurentSeriesRing(QQ)
            sage: f = t^-2
            sage: f.integral(t, constants=[0, 0, 0])
            Traceback (most recent call last):
            ...
            ValueError: cannot integrate 3 times the series t^-2
            sage: f = t^-5 + t^-2
            sage: f.integral(3)
            Traceback (most recent call last):
            ...
            ValueError: cannot integrate 3 times the series t^-5 + t^-2
            sage: f.integral([0, 1], constants=[0, 1])
            Traceback (most recent call last):
            ...
            ValueError: integration constants given twice
            sage: f.integral(4, constants=[0, 1])
            Traceback (most recent call last):
            ...
            ValueError: the number of integrations does not match the number of integration constants
        """
    def approximate_series(self, prec, name=None):
        """
        Return the Laurent series with absolute precision ``prec`` approximated
        from this series.

        INPUT:

        - ``prec`` -- integer
        - ``name`` -- name of the variable; if it is ``None``, the name of
          the variable of the series is used

        OUTPUT: a Laurent series with absolute precision ``prec``

        EXAMPLES::

            sage: L = LazyLaurentSeriesRing(ZZ, 'z')
            sage: z = L.gen()
            sage: f = (z - 2*z^3)^5/(1 - 2*z)
            sage: f
            z^5 + 2*z^6 - 6*z^7 - 12*z^8 + 16*z^9 + 32*z^10 - 16*z^11 + O(z^12)
            sage: g = f.approximate_series(10)
            sage: g
            z^5 + 2*z^6 - 6*z^7 - 12*z^8 + 16*z^9 + O(z^10)
            sage: g.parent()
            Power Series Ring in z over Integer Ring
            sage: h = (f^-1).approximate_series(3)
            sage: h
            z^-5 - 2*z^-4 + 10*z^-3 - 20*z^-2 + 60*z^-1 - 120 + 280*z - 560*z^2 + O(z^3)
            sage: h.parent()
            Laurent Series Ring in z over Integer Ring
        """
    add_bigoh = approximate_series
    O = approximate_series
    def polynomial(self, degree=None, name=None):
        """
        Return ``self`` as a Laurent polynomial if ``self`` is actually so.

        INPUT:

        - ``degree`` -- ``None`` or an integer
        - ``name`` -- name of the variable; if it is ``None``, the name of
          the variable of the series is used

        OUTPUT:

        A Laurent polynomial if the valuation of the series is negative or
        a polynomial otherwise.

        If ``degree`` is not ``None``, the terms of the series of
        degree greater than ``degree`` are first truncated.  If
        ``degree`` is ``None`` and the series is not a polynomial or
        a Laurent polynomial, a :exc:`ValueError` is raised.

        EXAMPLES::

            sage: L.<z> = LazyLaurentSeriesRing(ZZ)
            sage: f = L([1,0,0,2,0,0,0,3], valuation=5); f
            z^5 + 2*z^8 + 3*z^12
            sage: f.polynomial()
            3*z^12 + 2*z^8 + z^5

        TESTS::

            sage: g = L([1,0,0,2,0,0,0,3], valuation=-5); g
            z^-5 + 2*z^-2 + 3*z^2
            sage: g.polynomial()
            z^-5 + 2*z^-2 + 3*z^2
            sage: z = L.gen()
            sage: f = (1 + z)/(z^3 - z^5)
            sage: f
            z^-3 + z^-2 + z^-1 + O(1)
            sage: f.polynomial(5)
            z^-3 + z^-2 + z^-1 + 1 + z + z^2 + z^3 + z^4 + z^5
            sage: f.polynomial(0)
            z^-3 + z^-2 + z^-1 + 1
            sage: f.polynomial(-5)
            0
            sage: M = L(lambda n: n^2, valuation=0)
            sage: M.polynomial(3)
            9*z^3 + 4*z^2 + z
            sage: M = L(lambda n: n^2, valuation=0)
            sage: M.polynomial(5)
            25*z^5 + 16*z^4 + 9*z^3 + 4*z^2 + z

            sage: f = 1/(1 + z)
            sage: f.polynomial()
            Traceback (most recent call last):
            ...
            ValueError: not a polynomial

            sage: L.zero().polynomial()
            0
        """

class LazyPowerSeries(LazyCauchyProductSeries):
    """
    A Taylor series where the coefficients are computed lazily.

    EXAMPLES::

        sage: L.<x, y> = LazyPowerSeriesRing(ZZ)
        sage: f = 1 / (1 - x^2 + y^3); f
        1 + x^2 - y^3 + x^4 - 2*x^2*y^3 + (x^6+y^6) + O(x,y)^7
        sage: P.<x, y> = PowerSeriesRing(ZZ, default_prec=101)
        sage: g = 1 / (1 - x^2 + y^3); f[100] - g[100]
        0

    Lazy Taylor series is picklable::

        sage: g = loads(dumps(f))
        sage: g
        1 + x^2 - y^3 + x^4 - 2*x^2*y^3 + (x^6+y^6) + O(x,y)^7
        sage: g == f
        True
    """
    def is_unit(self):
        """
        Return whether this element is a unit in the ring.

        EXAMPLES::

            sage: L.<z> = LazyPowerSeriesRing(ZZ)
            sage: (2*z).is_unit()
            False

            sage: (1 + 2*z).is_unit()
            True

            sage: (3 + 2*z).is_unit()
            False

            sage: L.<x,y> = LazyPowerSeriesRing(ZZ)
            sage: (-1 + 2*x + 3*x*y).is_unit()
            True
        """
    def exponential(self):
        """
        Return the exponential series of ``self``.

        This method is deprecated, use :meth:`exp` instead.

        TESTS::

            sage: L.<x> = LazyPowerSeriesRing(QQ)
            sage: lazy_exp = x.exponential(); lazy_exp
            doctest:...: DeprecationWarning: the method exponential is deprecated. Use exp instead.
            See https://github.com/sagemath/sage/issues/32367 for details.
            1 + x + 1/2*x^2 + 1/6*x^3 + 1/24*x^4 + 1/120*x^5 + 1/720*x^6 + O(x^7)
        """
    def compute_coefficients(self, i) -> None:
        """
        Compute all the coefficients of ``self`` up to ``i``.

        This method is deprecated, it has no effect anymore.

        TESTS::

            sage: L.<z> = LazyPowerSeriesRing(QQ)
            sage: a = L([1,2,3], constant=3)
            sage: a.compute_coefficients(5)
            doctest:...: DeprecationWarning: the method compute_coefficients obsolete and has no effect.
            See https://github.com/sagemath/sage/issues/32367 for details.
            sage: a
            1 + 2*z + 3*z^2 + 3*z^3 + 3*z^4 + O(z^5)
        """
    def __call__(self, *g):
        '''
        Return the composition of ``self`` with ``g``.

        The arity of ``self`` must be equal to the number of
        arguments provided.

        Given a Taylor series `f` of arity `n` and a tuple of Taylor
        series `g = (g_1,\\dots, g_n)` over the same base ring, the
        composition `f \\circ g` is defined if and only if for each
        `1\\leq i\\leq n`:

        - `g_i` is zero, or
        - setting all variables except the `i`-th in `f` to zero
          yields a polynomial, or
        - `\\mathrm{val}(g_i) > 0`.

        If `f` is a univariate \'exact\' series, we can check whether
        `f` is a actually a polynomial.  However, if `f` is a
        multivariate series, we have no way to test whether setting
        all but one variable of `f` to zero yields a polynomial,
        except if `f` itself is \'exact\' and therefore a polynomial.

        INPUT:

        - ``g`` -- other series, all can be coerced into the same parent

        EXAMPLES::

            sage: L.<x, y, z> = LazyPowerSeriesRing(QQ)
            sage: M.<a, b> = LazyPowerSeriesRing(ZZ)
            sage: g1 = 1 / (1 - x)
            sage: g2 = x + y^2
            sage: p = a^2 + b + 1
            sage: p(g1, g2) - g1^2 - g2 - 1
            O(x,y,z)^7

        The number of mappings from a set with `m` elements to a set
        with `n` elements::

            sage: M.<a> = LazyPowerSeriesRing(QQ)
            sage: Ea = M(lambda n: 1/factorial(n))
            sage: Ex = L(lambda n: 1/factorial(n)*x^n)
            sage: Ea(Ex*y)[5]
            1/24*x^4*y + 2/3*x^3*y^2 + 3/4*x^2*y^3 + 1/6*x*y^4 + 1/120*y^5

        So, there are `3! 2! 2/3 = 8` mappings from a three element
        set to a two element set.

        We perform the composition with a lazy Laurent series::

            sage: N.<w> = LazyLaurentSeriesRing(QQ)
            sage: f1 = 1 / (1 - w)
            sage: f2 = cot(w / (1 - w))
            sage: p(f1, f2)
            w^-1 + 1 + 5/3*w + 8/3*w^2 + 164/45*w^3 + 23/5*w^4 + 5227/945*w^5 + O(w^6)

        We perform the composition with a lazy Dirichlet series::

            sage: # needs sage.symbolic
            sage: D = LazyDirichletSeriesRing(QQ, "s")
            sage: g = D(constant=1)-1
            sage: g
            1/(2^s) + 1/(3^s) + 1/(4^s) + O(1/(5^s))
            sage: f = 1 / (1 - x - y*z); f
            1 + x + (x^2+y*z) + (x^3+2*x*y*z) + (x^4+3*x^2*y*z+y^2*z^2)
             + (x^5+4*x^3*y*z+3*x*y^2*z^2)
             + (x^6+5*x^4*y*z+6*x^2*y^2*z^2+y^3*z^3)
             + O(x,y,z)^7
            sage: fog = f(g, g, g)
            sage: fog
            1 + 1/(2^s) + 1/(3^s) + 3/4^s + 1/(5^s) + 5/6^s + O(1/(7^s))
            sage: fg = 1 / (1 - g - g*g)
            sage: fg
            1 + 1/(2^s) + 1/(3^s) + 3/4^s + 1/(5^s) + 5/6^s + 1/(7^s) + O(1/(8^s))
            sage: fog - fg
            O(1/(8^s))

            sage: f = 1 / (1 - 2*a)
            sage: f(g)                                                                  # needs sage.symbolic
            1 + 2/2^s + 2/3^s + 6/4^s + 2/5^s + 10/6^s + 2/7^s + O(1/(8^s))
            sage: 1 / (1 - 2*g)                                                         # needs sage.symbolic
            1 + 2/2^s + 2/3^s + 6/4^s + 2/5^s + 10/6^s + 2/7^s + O(1/(8^s))

        The output parent is always the common parent between the base ring
        of `f` and the parent of `g` or extended to the corresponding
        lazy series::

            sage: T.<x,y> = LazyPowerSeriesRing(QQ)
            sage: R.<a,b,c> = ZZ[]
            sage: S.<v> = R[]
            sage: L.<z> = LaurentPolynomialRing(ZZ)
            sage: parent(x(a, b))
            Multivariate Polynomial Ring in a, b, c over Rational Field
            sage: parent(x(CC(2), a))
            Multivariate Polynomial Ring in a, b, c over Complex Field with 53 bits of precision
            sage: parent(x(0, 0))
            Rational Field
            sage: f = 1 / (1 - x - y); f
            1 + (x+y) + (x^2+2*x*y+y^2) + (x^3+3*x^2*y+3*x*y^2+y^3)
             + (x^4+4*x^3*y+6*x^2*y^2+4*x*y^3+y^4)
             + (x^5+5*x^4*y+10*x^3*y^2+10*x^2*y^3+5*x*y^4+y^5)
             + (x^6+6*x^5*y+15*x^4*y^2+20*x^3*y^3+15*x^2*y^4+6*x*y^5+y^6)
             + O(x,y)^7
            sage: f(a^2, b*c)
            1 + (a^2+b*c) + (a^4+2*a^2*b*c+b^2*c^2) + (a^6+3*a^4*b*c+3*a^2*b^2*c^2+b^3*c^3) + O(a,b,c)^7
            sage: f(v, v^2)
            1 + v + 2*v^2 + 3*v^3 + 5*v^4 + 8*v^5 + 13*v^6 + O(v^7)
            sage: f(z, z^2 + z)
            1 + 2*z + 5*z^2 + 12*z^3 + 29*z^4 + 70*z^5 + 169*z^6 + O(z^7)
            sage: three = T(3)(a^2, b); three
            3
            sage: parent(three)
            Multivariate Polynomial Ring in a, b, c over Rational Field

        TESTS::

            sage: L.<x,y> = LazyPowerSeriesRing(ZZ)
            sage: f = 1 / (1 - x - y)
            sage: f(f)
            Traceback (most recent call last):
            ...
            ValueError: arity of must be equal to the number of arguments provided

            sage: f(1, x*y)
            Traceback (most recent call last):
            ...
            ValueError: can only compose with a positive valuation series

        This test will pass once pushouts are implemented::

            sage: R.<a,b> = QQ[]
            sage: f(1/2*a, x)
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents: ...

        Consistency check when `g` is an uninitialized series between a
        polynomial `f` as both a polynomial and a lazy series::

            sage: L.<z> = LazyPowerSeriesRing(QQ)
            sage: f = 1 - z
            sage: g = L.undefined(valuation=1)
            sage: f(g) == f.polynomial()(g)
            True

            sage: g = L.undefined(valuation=1)
            sage: g.define(z / (1 - g))
            sage: g
            z + z^2 + 2*z^3 + 5*z^4 + 14*z^5 + 42*z^6 + 132*z^7 + O(z^8)
            sage: gp = L.undefined(valuation=1)
            sage: gp.define(z / f(gp))
            sage: gp
            z + z^2 + 2*z^3 + 5*z^4 + 14*z^5 + 42*z^6 + 132*z^7 + O(z^8)

        Check that composing the zero series with anything yields zero::

            sage: T.<x,y> = LazyPowerSeriesRing(QQ)
            sage: M.<a, b> = LazyPowerSeriesRing(QQ)
            sage: T(0)(1/(1-a), a+b)
            0

        Check that composing `f` with zero series yields the constant term of `f`::

            sage: T(3/(1-x-2*y))(0, 0)
            3

        Check that we can compose a polynomial with anything::

            sage: T(1-x-2*y + x*y^2)(1, 3)
            3

            sage: T(1-x-2*y + x*y^2)(1 + a, 3)
            3 + 8*a

            sage: T(1-x-2*y + x*y^2)(1/(1-a), 3)
            3 + 8*a + 8*a^2 + 8*a^3 + 8*a^4 + 8*a^5 + 8*a^6 + O(a,b)^7

        Check that issue :issue:`35261` is fixed::

            sage: L.<z> = LazyPowerSeriesRing(QQ)
            sage: fun = lambda n: 1 if ZZ(n).is_power_of(2) else 0
            sage: f = L(fun)
            sage: g = L.undefined(valuation=1)
            sage: g.define((~f.shift(-1)(g)).shift(1))
            sage: g
            z - z^2 + 2*z^3 - 6*z^4 + 20*z^5 - 70*z^6 + 256*z^7 + O(z^8)

            sage: f = L(fun)
            sage: g = L.undefined(valuation=1)
            sage: g.define((z - (f - z)(g)))
            sage: g
            z - z^2 + 2*z^3 - 6*z^4 + 20*z^5 - 70*z^6 + 256*z^7 + O(z^8)
        '''
    compose = __call__
    def revert(self):
        """
        Return the compositional inverse of ``self``.

        Given a Taylor series `f` in one variable, the compositional
        inverse is a power series `g` over the same base ring, such that
        `(f \\circ g)(z) = f(g(z)) = z`.

        The compositional inverse exists if and only if:

        - `\\mathrm{val}(f) = 1`, or

        - `f = a + b z` with `a, b \\neq 0`.

        EXAMPLES::

            sage: L.<z> = LazyPowerSeriesRing(QQ)
            sage: (2*z).revert()
            1/2*z
            sage: (z-z^2).revert()
            z + z^2 + 2*z^3 + 5*z^4 + 14*z^5 + 42*z^6 + 132*z^7 + O(z^8)

            sage: s = L(degree=1, constant=-1)
            sage: s.revert()
            -z - z^2 - z^3 + O(z^4)

            sage: s = L(degree=1, constant=1)
            sage: s.revert()
            z - z^2 + z^3 - z^4 + z^5 - z^6 + z^7 + O(z^8)

        .. WARNING::

            For series not known to be eventually constant (e.g., being
            defined by a function) with approximate valuation `\\leq 1`
            (but not necessarily its true valuation), this assumes
            that this is the actual valuation::

                sage: f = L(lambda n: n if n > 2 else 0)
                sage: f.revert()
                <repr(... failed: ValueError: generator already executing>

        TESTS::

            sage: L.<z> = LazyPowerSeriesRing(QQ)
            sage: s = L(lambda n: 2 if n == 1 else 0, valuation=1); s
            2*z + O(z^8)
            sage: s.revert()
            1/2*z + O(z^8)

            sage: (2 + 3*z).revert()
            -2/3 + 1/3*z

            sage: s = L(lambda n: 2 if n == 0 else 3 if n == 1 else 0, valuation=0); s
            2 + 3*z + O(z^7)
            sage: s.revert()
            Traceback (most recent call last):
            ...
            ValueError: cannot determine whether the compositional inverse exists

            sage: R.<q,t> = QQ[]
            sage: L.<z> = LazyPowerSeriesRing(R.fraction_field())
            sage: s = L([q], valuation=0, constant=t); s
            q + t*z + t*z^2 + t*z^3 + O(z^4)
            sage: s.revert()
            Traceback (most recent call last):
            ...
            ValueError: compositional inverse does not exist

        We look at some cases where the compositional inverse does not exist:

        `f = 0`::

            sage: L(0).revert()
            Traceback (most recent call last):
            ...
            ValueError: compositional inverse does not exist
            sage: (z - z).revert()
            Traceback (most recent call last):
            ...
            ValueError: compositional inverse does not exist

        `\\mathrm{val}(f) != 1` and `f(0) * f(1) = 0`::

            sage: (z^2).revert()
            Traceback (most recent call last):
            ...
            ValueError: compositional inverse does not exist

            sage: L(1).revert()
            Traceback (most recent call last):
            ...
            ValueError: compositional inverse does not exist

        `\\mathrm{val}(f) > 1`::

            sage: L(lambda n: n, valuation=2).revert()
            Traceback (most recent call last):
            ...
            ValueError: compositional inverse does not exist

        Reversion of exact series::

            sage: f = L([1, 2], valuation=0, constant=1)
            sage: f.revert()
            Traceback (most recent call last):
            ...
            ValueError: compositional inverse does not exist

            sage: f = L([-1, -1], valuation=1, constant=-1)
            sage: f.revert()
            (-z) + (-z^2) + (-z^3) + O(z^4)

            sage: f = L([-1, 0, -1], valuation=1, constant=-1)
            sage: f.revert()
            (-z) + z^3 + (-z^4) + (-2*z^5) + 6*z^6 + z^7 + O(z^8)

            sage: f = L([-1], valuation=1, degree=3, constant=-1)
            sage: f.revert()
            (-z) + z^3 + (-z^4) + (-2*z^5) + 6*z^6 + z^7 + O(z^8)

        Check that issue :issue:`35261` is fixed::

            sage: L.<z> = LazyPowerSeriesRing(QQ)
            sage: f = L(lambda n: 1 if ZZ(n).is_power_of(2) else 0)
            sage: f
            z + z^2 + z^4 + O(z^7)
            sage: f.revert()
            z - z^2 + 2*z^3 - 6*z^4 + 20*z^5 - 70*z^6 + 256*z^7 + O(z^8)
        """
    compositional_inverse = revert
    def derivative(self, *args):
        """
        Return the derivative of the Taylor series.

        Multiple variables and iteration counts may be supplied; see
        the documentation of
        :func:`sage.calculus.functional.derivative` function for
        details.

        EXAMPLES::

            sage: T.<z> = LazyPowerSeriesRing(ZZ)
            sage: z.derivative()
            1
            sage: (1 + z + z^2).derivative(3)
            0
            sage: (z^2 + z^4 + z^10).derivative(3)
            24*z + 720*z^7
            sage: (1 / (1-z)).derivative()
            1 + 2*z + 3*z^2 + 4*z^3 + 5*z^4 + 6*z^5 + 7*z^6 + O(z^7)
            sage: T([1, 1, 1], constant=4).derivative()
            1 + 2*z + 12*z^2 + 16*z^3 + 20*z^4 + 24*z^5 + 28*z^6 + O(z^7)

            sage: R.<q> = QQ[]
            sage: L.<x, y> = LazyPowerSeriesRing(R)
            sage: f = 1 / (1-q*x+y); f
            1 + (q*x-y) + (q^2*x^2+(-2*q)*x*y+y^2)
             + (q^3*x^3+(-3*q^2)*x^2*y+3*q*x*y^2-y^3)
             + (q^4*x^4+(-4*q^3)*x^3*y+6*q^2*x^2*y^2+(-4*q)*x*y^3+y^4)
             + (q^5*x^5+(-5*q^4)*x^4*y+10*q^3*x^3*y^2+(-10*q^2)*x^2*y^3+5*q*x*y^4-y^5)
             + (q^6*x^6+(-6*q^5)*x^5*y+15*q^4*x^4*y^2+(-20*q^3)*x^3*y^3+15*q^2*x^2*y^4+(-6*q)*x*y^5+y^6)
             + O(x,y)^7
            sage: f.derivative(q)
            x + (2*q*x^2+(-2)*x*y) + (3*q^2*x^3+(-6*q)*x^2*y+3*x*y^2)
             + (4*q^3*x^4+(-12*q^2)*x^3*y+12*q*x^2*y^2+(-4)*x*y^3)
             + (5*q^4*x^5+(-20*q^3)*x^4*y+30*q^2*x^3*y^2+(-20*q)*x^2*y^3+5*x*y^4)
             + (6*q^5*x^6+(-30*q^4)*x^5*y+60*q^3*x^4*y^2+(-60*q^2)*x^3*y^3+30*q*x^2*y^4+(-6)*x*y^5)
             + O(x,y)^7

        Multivariate::

            sage: L.<x,y,z> = LazyPowerSeriesRing(QQ)
            sage: f = (x + y^2 + z)^3; f
            (x^3+3*x^2*z+3*x*z^2+z^3) + (3*x^2*y^2+6*x*y^2*z+3*y^2*z^2) + (3*x*y^4+3*y^4*z) + y^6
            sage: f.derivative(x)
            (3*x^2+6*x*z+3*z^2) + (6*x*y^2+6*y^2*z) + 3*y^4
            sage: f.derivative(y, 5)
            720*y
            sage: f.derivative(z, 5)
            0
            sage: f.derivative(x, y, z)
            12*y

            sage: f = (1 + x + y^2 + z)^-1
            sage: f.derivative(x)
            -1 + (2*x+2*z) - (3*x^2-2*y^2+6*x*z+3*z^2) + ... + O(x,y,z)^6
            sage: f.derivative(y, 2)
            -2 + (4*x+4*z) - (6*x^2-12*y^2+12*x*z+6*z^2) + ... + O(x,y,z)^5
            sage: f.derivative(x, y)
            4*y - (12*x*y+12*y*z) + (24*x^2*y-12*y^3+48*x*y*z+24*y*z^2)
            - (40*x^3*y-48*x*y^3+120*x^2*y*z-48*y^3*z+120*x*y*z^2+40*y*z^3) + O(x,y,z)^5
            sage: f.derivative(x, y, z)
            -12*y + (48*x*y+48*y*z) - (120*x^2*y-48*y^3+240*x*y*z+120*y*z^2) + O(x,y,z)^4

            sage: R.<t> = QQ[]
            sage: L.<x,y,z> = LazyPowerSeriesRing(R)
            sage: f = ((t^2-3)*x + t*y^2 - t*z)^2
            sage: f.derivative(t,x,t,y)
            24*t*y
            sage: f.derivative(t, 2)
            ((12*t^2-12)*x^2+(-12*t)*x*z+2*z^2) + (12*t*x*y^2+(-4)*y^2*z) + 2*y^4
            sage: f.derivative(z, t)
            ((-6*t^2+6)*x+4*t*z) + ((-4*t)*y^2)
            sage: f.derivative(t, 10)
            0

            sage: f = (1 + t*(x + y + z))^-1
            sage: f.derivative(x, t, y)
            4*t + ((-18*t^2)*x+(-18*t^2)*y+(-18*t^2)*z)
             + (48*t^3*x^2+96*t^3*x*y+48*t^3*y^2+96*t^3*x*z+96*t^3*y*z+48*t^3*z^2)
             + ... + O(x,y,z)^5
            sage: f.derivative(t, 2)
            (2*x^2+4*x*y+2*y^2+4*x*z+4*y*z+2*z^2) + ... + O(x,y,z)^7
            sage: f.derivative(x, y, z, t)
            (-18*t^2) + (96*t^3*x+96*t^3*y+96*t^3*z) + ... + O(x,y,z)^4

        TESTS:

        Check that :issue:`36154` is fixed::

            sage: L.<z> = LazyPowerSeriesRing(Zmod(4))
            sage: f = L([0,0,2])
            sage: f.derivative()
            0
        """
    def adams_operator(self, p):
        """
        Return the image of ``self`` under the Adams operator of index ``p``.

        This raises all variables to the power ``p``, both the power
        series variables and the variables inside the coefficient ring.

        INPUT:

        - ``p`` -- positive integer

        EXAMPLES:

        With no variables in the base ring::

            sage: A = LazyPowerSeriesRing(QQ,'t')
            sage: f = A([1,2,3,4]); f
            1 + 2*t + 3*t^2 + 4*t^3
            sage: f.adams_operator(2)
            1 + 2*t^2 + 3*t^4 + 4*t^6

        With variables in the base ring::

            sage: q = polygen(QQ,'q')
            sage: A = LazyPowerSeriesRing(q.parent(),'t')
            sage: f = A([0,1+q,2,3+q**2]); f
            ((q+1)*t) + 2*t^2 + ((q^2+3)*t^3)
            sage: f.adams_operator(2)
            ((q^2+1)*t^2) + 2*t^4 + ((q^4+3)*t^6)

        In the multivariate case::

            sage: A = LazyPowerSeriesRing(ZZ,'t,u')
            sage: f = A({(1,2):4,(2,3):6}); f
            4*t*u^2 + 6*t^2*u^3
            sage: f.adams_operator(3)
            4*t^3*u^6 + 6*t^6*u^9

        TESTS::

            sage: A = LazyPowerSeriesRing(QQ,'t')
            sage: f = A([1,2,3,4])
            sage: f.adams_operator(1)
            1 + 2*t + 3*t^2 + 4*t^3
            sage: f.adams_operator(-1)
            Traceback (most recent call last):
            ...
            ValueError: p must be a positive integer
        """
    def integral(self, variable=None, *, constants=None):
        """
        Return the integral of ``self`` with respect to ``variable``.

        INPUT:

        - ``variable`` -- (optional) the variable to integrate
        - ``constants`` -- (optional; keyword-only) list of integration
          constants for the integrals of ``self`` (the last constant
          corresponds to the first integral)

        For multivariable series, only ``variable`` should be
        specified; the integration constant is taken to be `0`.

        Now we assume the series is univariate. If the first argument is a
        list, then this method interprets it as integration constants. If it
        is a positive integer, the method interprets it as the number of times
        to integrate the function. If ``variable`` is not the variable of
        the power series, then the coefficients are integrated with respect
        to ``variable``. If the integration constants are not specified,
        they are considered to be `0`.

        EXAMPLES::

            sage: L.<t> = LazyPowerSeriesRing(QQ)
            sage: f = 2 + 3*t + t^5
            sage: f.integral()
            2*t + 3/2*t^2 + 1/6*t^6
            sage: f.integral([-2, -2])
            -2 - 2*t + t^2 + 1/2*t^3 + 1/42*t^7
            sage: f.integral(t)
            2*t + 3/2*t^2 + 1/6*t^6
            sage: f.integral(2)
            t^2 + 1/2*t^3 + 1/42*t^7
            sage: (t^3 + t^5).integral()
            1/4*t^4 + 1/6*t^6
            sage: L.zero().integral()
            0
            sage: L.zero().integral([0, 1, 2, 3])
            t + t^2 + 1/2*t^3
            sage: L([1, 2 ,3], constant=4).integral()
            t + t^2 + t^3 + t^4 + 4/5*t^5 + 2/3*t^6 + O(t^7)

        We solve the ODE `f'' - f' - 2 f = 0` by solving for `f''`, then
        integrating and applying a recursive definition::

            sage: R.<C, D> = QQ[]
            sage: L.<x> = LazyPowerSeriesRing(R)
            sage: f = L.undefined()
            sage: f.define((f.derivative() + 2*f).integral(constants=[C, D]))
            sage: f
            C + D*x + ((C+1/2*D)*x^2) + ((1/3*C+1/2*D)*x^3)
             + ((1/4*C+5/24*D)*x^4) + ((1/12*C+11/120*D)*x^5)
             + ((11/360*C+7/240*D)*x^6) + O(x^7)
            sage: f.derivative(2) - f.derivative() - 2*f
            O(x^7)

        We compare this with the answer we get from the
        characteristic polynomial::

            sage: g = C * exp(-x) + D * exp(2*x); g
            (C+D) + ((-C+2*D)*x) + ((1/2*C+2*D)*x^2) + ((-1/6*C+4/3*D)*x^3)
             + ((1/24*C+2/3*D)*x^4) + ((-1/120*C+4/15*D)*x^5)
             + ((1/720*C+4/45*D)*x^6) + O(x^7)
            sage: g.derivative(2) - g.derivative() - 2*g
            O(x^7)

        Note that ``C`` and ``D`` are playing different roles, so we need
        to perform a substitution to the coefficients of ``f`` to recover
        the solution ``g``::

            sage: fp = f.map_coefficients(lambda c: c(C=C+D, D=2*D-C)); fp
            (C+D) + ((-C+2*D)*x) + ((1/2*C+2*D)*x^2) + ((-1/6*C+4/3*D)*x^3)
             + ((1/24*C+2/3*D)*x^4) + ((-1/120*C+4/15*D)*x^5)
             + ((1/720*C+4/45*D)*x^6) + O(x^7)
            sage: fp - g
            O(x^7)

        We can integrate both the series and coefficients::

            sage: R.<x,y,z> = QQ[]
            sage: L.<t> = LazyPowerSeriesRing(R)
            sage: f = (x*t^2 + y*t + z)^2; f
            z^2 + 2*y*z*t + ((y^2+2*x*z)*t^2) + 2*x*y*t^3 + x^2*t^4
            sage: f.integral(x)
            x*z^2 + 2*x*y*z*t + ((x*y^2+x^2*z)*t^2) + x^2*y*t^3 + 1/3*x^3*t^4
            sage: f.integral(t)
            z^2*t + y*z*t^2 + ((1/3*y^2+2/3*x*z)*t^3) + 1/2*x*y*t^4 + 1/5*x^2*t^5
            sage: f.integral(y, constants=[x*y*z])
            x*y*z + y*z^2*t + 1/2*y^2*z*t^2 + ((1/9*y^3+2/3*x*y*z)*t^3) + 1/4*x*y^2*t^4 + 1/5*x^2*y*t^5

        We can integrate multivariate power series::

            sage: R.<t> = QQ[]
            sage: L.<x,y,z> = LazyPowerSeriesRing(R)
            sage: f = ((t^2 + t) - t * y^2 + t^2 * (y + z))^2; f
            (t^4+2*t^3+t^2) + ((2*t^4+2*t^3)*y+(2*t^4+2*t^3)*z)
             + ((t^4-2*t^3-2*t^2)*y^2+2*t^4*y*z+t^4*z^2)
             + ((-2*t^3)*y^3+(-2*t^3)*y^2*z) + t^2*y^4
            sage: g = f.integral(x); g
            ((t^4+2*t^3+t^2)*x) + ((2*t^4+2*t^3)*x*y+(2*t^4+2*t^3)*x*z)
             + ((t^4-2*t^3-2*t^2)*x*y^2+2*t^4*x*y*z+t^4*x*z^2)
             + ((-2*t^3)*x*y^3+(-2*t^3)*x*y^2*z) + t^2*x*y^4
            sage: g[0]
            0
            sage: g[1]
            (t^4 + 2*t^3 + t^2)*x
            sage: g[2]
            (2*t^4 + 2*t^3)*x*y + (2*t^4 + 2*t^3)*x*z
            sage: f.integral(z)
            ((t^4+2*t^3+t^2)*z) + ((2*t^4+2*t^3)*y*z+(t^4+t^3)*z^2)
             + ((t^4-2*t^3-2*t^2)*y^2*z+t^4*y*z^2+1/3*t^4*z^3)
             + ((-2*t^3)*y^3*z+(-t^3)*y^2*z^2) + t^2*y^4*z
            sage: f.integral(t)
            (1/5*t^5+1/2*t^4+1/3*t^3) + ((2/5*t^5+1/2*t^4)*y+(2/5*t^5+1/2*t^4)*z)
             + ((1/5*t^5-1/2*t^4-2/3*t^3)*y^2+2/5*t^5*y*z+1/5*t^5*z^2)
             + ((-1/2*t^4)*y^3+(-1/2*t^4)*y^2*z) + 1/3*t^3*y^4

            sage: L.<x,y,z> = LazyPowerSeriesRing(QQ)
            sage: (x + y - z^2).integral(z)
            (x*z+y*z) - 1/3*z^3

        TESTS::

            sage: L.<t> = LazyPowerSeriesRing(QQ)
            sage: f = t^2
            sage: f.integral([0, 1], constants=[0, 1])
            Traceback (most recent call last):
            ...
            ValueError: integration constants given twice
            sage: f.integral(4, constants=[0, 1])
            Traceback (most recent call last):
            ...
            ValueError: the number of integrations does not match the number of integration constants

            sage: L.<x,y,z> = LazyPowerSeriesRing(QQ)
            sage: x.integral(y, constants=[2])
            Traceback (most recent call last):
            ...
            ValueError: integration constants must not be given for multivariate series
            sage: x.integral()
            Traceback (most recent call last):
            ...
            ValueError: the integration variable must be specified
        """
    def polynomial(self, degree=None, names=None):
        """
        Return ``self`` as a polynomial if ``self`` is actually so.

        INPUT:

        - ``degree`` -- ``None`` or an integer
        - ``names`` -- names of the variables; if it is ``None``, the name of
          the variables of the series is used

        OUTPUT:

        If ``degree`` is not ``None``, the terms of the series of
        degree greater than ``degree`` are first truncated.  If
        ``degree`` is ``None`` and the series is not a polynomial
        polynomial, a :exc:`ValueError` is raised.

        EXAMPLES::

            sage: L.<x,y> = LazyPowerSeriesRing(ZZ)
            sage: f = x^2 + y*x - x + 2; f
            2 - x + (x^2+x*y)
            sage: f.polynomial()
            x^2 + x*y - x + 2

        TESTS::

            sage: g = 1 / (1 + x + y + x*y)
            sage: g3 = g.truncate(4); g3
            1 - (x+y) + (x^2+x*y+y^2) - (x^3+x^2*y+x*y^2+y^3)
            sage: g.polynomial()
            Traceback (most recent call last):
            ...
            ValueError: not a polynomial
            sage: g3.polynomial()
            -x^3 - x^2*y - x*y^2 - y^3 + x^2 + x*y + y^2 - x - y + 1
            sage: L.zero().polynomial()
            0
            sage: g3.polynomial() == g.polynomial(3)
            True
            sage: g3.polynomial(0)
            1

            sage: L.<z> = LazyPowerSeriesRing(ZZ)
            sage: f = z-z^2
            sage: f.polynomial()
            -z^2 + z
        """
    def add_bigoh(self, prec):
        """
        Return the power series of precision at most ``prec`` obtained by
        adding `O(q^\\text{prec})` to `f`, where `q` is the (tuple of)
        variable(s).

        EXAMPLES::

            sage: L.<x,y> = LazyPowerSeriesRing(QQ)
            sage: f = 1 / (1 - x + y)
            sage: f
            1 + (x-y) + (x^2-2*x*y+y^2) + (x^3-3*x^2*y+3*x*y^2-y^3)
             + (x^4-4*x^3*y+6*x^2*y^2-4*x*y^3+y^4)
             + (x^5-5*x^4*y+10*x^3*y^2-10*x^2*y^3+5*x*y^4-y^5)
             + (x^6-6*x^5*y+15*x^4*y^2-20*x^3*y^3+15*x^2*y^4-6*x*y^5+y^6)
             + O(x,y)^7
            sage: f3 = f.add_bigoh(3); f3
            1 + x - y + x^2 - 2*x*y + y^2 + O(x, y)^3
            sage: f3.parent()
            Multivariate Power Series Ring in x, y over Rational Field

            sage: R.<t> = QQ[]
            sage: L.<x> = LazyPowerSeriesRing(R)
            sage: f = 1 / (1 - t^3*x)
            sage: f
            1 + t^3*x + t^6*x^2 + t^9*x^3 + t^12*x^4 + t^15*x^5 + t^18*x^6 + O(x^7)
            sage: f3 = f.add_bigoh(3); f3
            1 + t^3*x + t^6*x^2 + O(x^3)
            sage: f3.parent()
            Power Series Ring in x over Univariate Polynomial Ring in t
             over Rational Field
        """
    O = add_bigoh

class LazyPowerSeries_gcd_mixin:
    """
    A lazy power series that also implements the GCD algorithm.
    """
    def gcd(self, other):
        """
        Return the greatest common divisor of ``self`` and ``other``.

        EXAMPLES::

            sage: L.<x> = LazyPowerSeriesRing(QQ)
            sage: a = 16*x^5 / (1 - 5*x)
            sage: b = (22*x^2 + x^8) / (1 - 4*x^2)
            sage: a.gcd(b)
            x^2
        """
    def xgcd(self, f):
        """
        Return the extended gcd of ``self`` and ``f``.

        OUTPUT:

        A triple ``(g, s, t)`` such that ``g`` is the gcd of ``self``
        and ``f``, and ``s`` and ``t`` are cofactors satisfying the
        Bezout identity

        .. MATH::

            g = s \\cdot \\mathrm{self} + t \\cdot f.

        EXAMPLES::

            sage: L.<x> = LazyPowerSeriesRing(QQ)
            sage: a = 16*x^5 / (1 - 2*x)
            sage: b = (22*x^3 + x^8) / (1 - 3*x^2)
            sage: g, s, t = a.xgcd(b)
            sage: g
            x^3
            sage: s
            1/22 - 41/242*x^2 - 8/121*x^3 + 120/1331*x^4 + 1205/5324*x^5 + 316/14641*x^6 + O(x^7)
            sage: t
            1/22 - 41/242*x^2 - 8/121*x^3 + 120/1331*x^4 + 1205/5324*x^5 + 316/14641*x^6 + O(x^7)

            sage: LazyPowerSeriesRing.options.halting_precision(20)  # verify up to degree 20

            sage: g == s * a + t * b
            True

            sage: a = 16*x^5 / (1 - 2*x)
            sage: b = (-16*x^5 + x^8) / (1 - 3*x^2)
            sage: g, s, t = a.xgcd(b)
            sage: g
            x^5
            sage: s
            1/16 - 1/16*x - 3/16*x^2 + 1/8*x^3 - 17/256*x^4 + 9/128*x^5 + 1/128*x^6 + O(x^7)
            sage: t
            1/16*x - 1/16*x^2 - 3/16*x^3 + 1/8*x^4 - 17/256*x^5 + 9/128*x^6 + 1/128*x^7 + O(x^8)
            sage: g == s * a + t * b
            True

            sage: # needs sage.rings.finite_rings
            sage: L.<x> = LazyPowerSeriesRing(GF(2))
            sage: a = L(lambda n: n % 2, valuation=3); a
            x^3 + x^5 + x^7 + x^9 + O(x^10)
            sage: b = L(lambda n: binomial(n,2) % 2, valuation=3); b
            x^3 + x^6 + x^7 + O(x^10)
            sage: g, s, t = a.xgcd(b)
            sage: g
            x^3
            sage: s
            1 + x + x^3 + x^4 + x^5 + O(x^7)
            sage: t
            x + x^2 + x^4 + x^5 + x^6 + O(x^8)
            sage: g == s * a + t * b
            True

            sage: LazyPowerSeriesRing.options._reset()  # reset the options
        """

class LazyCompletionGradedAlgebraElement(LazyCauchyProductSeries):
    """
    An element of a completion of a graded algebra that is computed lazily.
    """

class LazySymmetricFunction(LazyCompletionGradedAlgebraElement):
    """
    A symmetric function where each degree is computed lazily.

    EXAMPLES::

        sage: s = SymmetricFunctions(ZZ).s()                                            # needs sage.modules
        sage: L = LazySymmetricFunctions(s)                                             # needs sage.modules
    """
    def is_unit(self):
        """
        Return whether this element is a unit in the ring.

        EXAMPLES::

            sage: # needs sage.modules
            sage: m = SymmetricFunctions(ZZ).m()
            sage: L = LazySymmetricFunctions(m)
            sage: L(2*m[1]).is_unit()
            False
            sage: L(-1 + 2*m[1]).is_unit()
            True
            sage: L(2 + m[1]).is_unit()
            False
            sage: m = SymmetricFunctions(QQ).m()
            sage: L = LazySymmetricFunctions(m)
            sage: L(2 + 3*m[1]).is_unit()
            True
        """
    def __call__(self, *args):
        """
        Return the composition of ``self`` with ``g``.

        The arity of ``self`` must be equal to the number of
        arguments provided.

        Given a lazy symmetric function `f` of arity `n` and a tuple
        of lazy symmetric functions `g = (g_1,\\dots, g_n)` over the
        same base ring, the composition (or plethysm) `(f \\circ g)`
        is defined if and only if for each `1\\leq i\\leq n`:

        - `g_i = 0`, or
        - setting all alphabets except the `i`-th in `f` to zero
          yields a symmetric function with only finitely many
          nonzero coefficients, or
        - `\\mathrm{val}(g) > 0`.

        If `f` is a univariate 'exact' lazy symmetric function, we
        can check whether `f` has only finitely many nonzero
        coefficients.  However, if `f` has larger arity, we have no
        way to test whether setting all but one alphabets of `f` to
        zero yields a polynomial, except if `f` itself is 'exact' and
        therefore a symmetric function with only finitely many
        nonzero coefficients.

        INPUT:

        - ``g`` -- other (lazy) symmetric functions

        .. TODO::

            Allow specification of degree one elements.

        EXAMPLES::

            sage: # needs sage.modules
            sage: P.<q> = QQ[]
            sage: s = SymmetricFunctions(P).s()
            sage: L = LazySymmetricFunctions(s)
            sage: f = s[2]
            sage: g = s[3]
            sage: L(f)(L(g)) - L(f(g))
            0
            sage: f = s[2] + s[2,1]
            sage: g = s[1] + s[2,2]
            sage: L(f)(L(g)) - L(f(g))
            0
            sage: L(f)(g) - L(f(g))
            0
            sage: f = s[2] + s[2,1]
            sage: g = s[1] + s[2,2]
            sage: L(f)(L(q*g)) - L(f(q*g))
            0

        The Frobenius character of the permutation action on set
        partitions is a plethysm::

            sage: # needs sage.modules
            sage: s = SymmetricFunctions(QQ).s()
            sage: S = LazySymmetricFunctions(s)
            sage: E1 = S(lambda n: s[n], valuation=1)
            sage: E = 1 + E1
            sage: P = E(E1)
            sage: P[:5]
            [s[], s[1], 2*s[2], s[2, 1] + 3*s[3], 2*s[2, 2] + 2*s[3, 1] + 5*s[4]]

        The plethysm with a tensor product is also implemented::

            sage: # needs sage.modules
            sage: s = SymmetricFunctions(QQ).s()
            sage: X = tensor([s[1],s[[]]])
            sage: Y = tensor([s[[]],s[1]])
            sage: S = LazySymmetricFunctions(s)
            sage: S2 = LazySymmetricFunctions(tensor([s, s]))
            sage: A = S(s[1,1,1])
            sage: B = S2(X+Y)
            sage: A(B)                                                                  # needs lrcalc_python
            (s[]#s[1,1,1]+s[1]#s[1,1]+s[1,1]#s[1]+s[1,1,1]#s[])

            sage: H = S(lambda n: s[n])                                                 # needs sage.modules
            sage: H(S2(X*Y))                                                            # needs lrcalc_python sage.modules
            (s[]#s[]) + (s[1]#s[1]) + (s[1,1]#s[1,1]+s[2]#s[2])
             + (s[1,1,1]#s[1,1,1]+s[2,1]#s[2,1]+s[3]#s[3]) + O^7
            sage: H(S2(X+Y))                                                            # needs sage.modules
            (s[]#s[]) + (s[]#s[1]+s[1]#s[]) + (s[]#s[2]+s[1]#s[1]+s[2]#s[])
             + (s[]#s[3]+s[1]#s[2]+s[2]#s[1]+s[3]#s[])
             + (s[]#s[4]+s[1]#s[3]+s[2]#s[2]+s[3]#s[1]+s[4]#s[])
             + (s[]#s[5]+s[1]#s[4]+s[2]#s[3]+s[3]#s[2]+s[4]#s[1]+s[5]#s[])
             + (s[]#s[6]+s[1]#s[5]+s[2]#s[4]+s[3]#s[3]+s[4]#s[2]+s[5]#s[1]+s[6]#s[])
             + O^7

        TESTS::

            sage: # needs sage.modules
            sage: s = SymmetricFunctions(QQ).s()
            sage: S = LazySymmetricFunctions(s)
            sage: f = 1 / (1 - S(s[2]))
            sage: g = f(s[2]); g                                                        # needs lrcalc_python
            s[] + (s[2,2]+s[4]) + O^7
            sage: S(sum(f[i](s[2]) for i in range(5))).truncate(10) == g.truncate(10)   # needs lrcalc_python
            True
            sage: f = 1 / (1 - S(s[2]))
            sage: g = S(s[1]) / (1 - S(s[1]))
            sage: f(g)                                                                  # needs lrcalc_python
            s[] + s[2] + (s[1,1,1]+2*s[2,1]+s[3])
             + (2*s[1,1,1,1]+4*s[2,1,1]+5*s[2,2]+5*s[3,1]+3*s[4])
             + (2*s[1,1,1,1,1]+10*s[2,1,1,1]+14*s[2,2,1]+18*s[3,1,1]+16*s[3,2]+14*s[4,1]+4*s[5])
             + (3*s[1,1,1,1,1,1]+22*s[2,1,1,1,1]+38*s[2,2,1,1]+28*s[2,2,2]+48*s[3,1,1,1]+82*s[3,2,1]+25*s[3,3]+51*s[4,1,1]+56*s[4,2]+31*s[5,1]+9*s[6])
             + O^7
            sage: f(0)                                                                  # needs lrcalc_python
            1
            sage: f(s(1))
            Traceback (most recent call last):
            ...
            ValueError: can only compose with a positive valuation series

        Check that composing the zero series with anything yields
        zero in the correct parent::

            sage: # needs sage.modules
            sage: e = SymmetricFunctions(QQ).e()
            sage: h = SymmetricFunctions(QQ).h()
            sage: s = SymmetricFunctions(QQ).s()
            sage: p = SymmetricFunctions(QQ).p()
            sage: L = LazySymmetricFunctions(tensor([e, h]))
            sage: r = (L(0)(s[1], p[1])); r
            0
            sage: r.parent()
            Symmetric Functions over Rational Field in the Schur basis

        Check that composing `f` with zero series yields the constant term of `f`::

            sage: f = 3*L(tensor([s[1], s[1]]))                                         # needs sage.modules
            sage: f(0, 0)                                                               # needs sage.modules
            0
            sage: (3+f)(0, 0)                                                           # needs sage.modules
            3
        """
    plethysm = __call__
    def revert(self):
        """
        Return the compositional inverse of ``self``.

        Given a symmetric function `f`, the compositional inverse is
        a symmetric function `g` over the same base ring, such that
        `f \\circ g = p_1`.  Thus, it is the inverse with respect to
        plethystic substitution.

        The compositional inverse exists if and only if:

        - `\\mathrm{val}(f) = 1`, or

        - `f = a + b p_1` with `a, b \\neq 0`.

        .. SEEALSO:: :meth:`legendre_transform`

        EXAMPLES::

            sage: # needs sage.modules
            sage: h = SymmetricFunctions(QQ).h()
            sage: L = LazySymmetricFunctions(h)
            sage: f = L(lambda n: h[n]) - 1
            sage: f(f.revert())
            h[1] + O^8

        TESTS::

            sage: f = L(lambda n: h[n]) - 1 - h[1]                                      # needs sage.modules
            sage: g = f.revert()                                                        # needs sage.modules
            sage: g[1]                                                                  # needs sage.modules
            Traceback (most recent call last):
            ...
            ValueError: compositional inverse does not exist

            sage: # needs sage.modules
            sage: R.<a,b> = QQ[]
            sage: p = SymmetricFunctions(R.fraction_field()).p()
            sage: L = LazySymmetricFunctions(p)
            sage: f = L(a + b*p[1])
            sage: f.revert()
            (-a/b*p[]) + 1/b*p[1]
            sage: f = L(2*p[1])
            sage: f.revert()
            1/2*p[1]
            sage: f = L(2*p[1] + p[1,1])
            sage: f.revert()
            1/2*p[1] + (-1/8*p[1,1]) + (1/16*p[1,1,1]) + (-5/128*p[1,1,1,1])
                     + (7/256*p[1,1,1,1,1]) + (-21/1024*p[1,1,1,1,1,1])
                     + (33/2048*p[1,1,1,1,1,1,1]) + O^8
            sage: f.revert()(f)
            p[1] + O^8

        ALGORITHM:

        Let `F` be a symmetric function with valuation `1`, i.e.,
        whose constant term vanishes and whose degree one term equals
        `b p_1`.  Then

        .. MATH::

            (F - b p_1) \\circ G = F \\circ G - b p_1 \\circ G = p_1 - b G,

        and therefore `G = (p_1 - (F - b p_1) \\circ G) / b`, which
        allows recursive computation of `G`.

        .. SEEALSO::

            The compositional inverse `\\Omega` of the symmetric
            function `h_1 + h_2 + \\dots` can be handled much more
            efficiently using specialized methods. See
            :func:`~sage.combinat.species.generating_series.LogarithmCycleIndexSeries`

        AUTHORS:

        - Andrew Gainer-Dewar
        - Martin Rubey
        """
    plethystic_inverse = revert
    compositional_inverse = revert
    def legendre_transform(self):
        """
        Return the Legendre transform of ``self``.

        Given a symmetric function `f` of valuation 2, the Legendre
        transform of `f` is the unique symmetric function `g` of
        valuation 2 over the same base ring, such that

        .. MATH::

            g \\circ \\partial_{p_1} f + f = p_1 \\partial_{p_1} f.

        This implies that the derivatives of `f` and `g` with respect to `p_1`
        are inverses of each other with respect to plethystic substitution.

        The Legendre transform is an involution.

        .. SEEALSO:: :meth:`revert`

        EXAMPLES::

            sage: p = SymmetricFunctions(QQ).p()
            sage: s = SymmetricFunctions(QQ).s()
            sage: lp = LazySymmetricFunctions(p)
            sage: A = lp(s([2]))
            sage: A.legendre_transform()
            (1/2*p[1,1]-1/2*p[2]) + O^9

            sage: def asso(n):
            ....:     return p.sum_of_terms((Partition([d] * (n // d)),
            ....:          euler_phi(d) / n) for d in divisors(n))

            sage: A = lp(asso, valuation=2)
            sage: A.legendre_transform()[:5]
            [1/2*p[1, 1] - 1/2*p[2],
            -1/3*p[1, 1, 1] - 2/3*p[3],
            1/4*p[1, 1, 1, 1] + 1/4*p[2, 2] - 1/2*p[4]]

        TESTS::

            sage: p = SymmetricFunctions(QQ).p()
            sage: lp = LazySymmetricFunctions(p)
            sage: A = lp(p([1]))
            sage: A.legendre_transform()
            Traceback (most recent call last):
            ...
            ValueError: only for series of valuation 2
        """
    def derivative_with_respect_to_p1(self, n: int = 1):
        """
        Return the symmetric function obtained by taking the
        derivative of ``self`` with respect to the power-sum
        symmetric function `p_1` when the expansion of ``self`` in
        the power-sum basis is considered as a polynomial in `p_k`'s
        (with `k \\geq 1`).

        This is the same as skewing ``self`` by the first power-sum
        symmetric function `p_1`.

        INPUT:

        - ``n`` -- (default: 1) nonnegative integer which determines
          which power of the derivative is taken

        EXAMPLES:

        The species `E` of sets satisfies the relationship `E' = E`::

            sage: # needs sage.modules
            sage: h = SymmetricFunctions(QQ).h()
            sage: T = LazySymmetricFunctions(h)
            sage: E = T(lambda n: h[n])
            sage: E - E.derivative_with_respect_to_p1()
            O^6

        The species `C` of cyclic orderings and the species `L` of linear
        orderings satisfy the relationship `C' = L`::

            sage: # needs sage.modules
            sage: p = SymmetricFunctions(QQ).p()
            sage: C = T(lambda n: (sum(euler_phi(k)*p([k])**(n//k)
            ....:                      for k in divisors(n))/n if n > 0 else 0))
            sage: L = T(lambda n: p([1]*n))
            sage: L - C.derivative_with_respect_to_p1()                                 # needs sage.libs.pari
            O^6

        TESTS::

            sage: # needs sage.modules
            sage: T = LazySymmetricFunctions(p)
            sage: a = T(p([1,1,1]))
            sage: a.derivative_with_respect_to_p1()
            (3*p[1,1]) + O^9
            sage: a.derivative_with_respect_to_p1(1)
            (3*p[1,1]) + O^9
            sage: a.derivative_with_respect_to_p1(2)
            6*p[1] + O^8
            sage: a.derivative_with_respect_to_p1(3)
            6*p[] + O^7
        """
    def suspension(self):
        """
        Return the suspension of ``self``.

        This is an involution, that maps the homogeneous component
        `f_n` of degree `n` to `(-1)^{n - 1} \\omega(f_n)`, where
        `omega` is the usual involution of symmetric functions.

        EXAMPLES::

            sage: s = SymmetricFunctions(QQ).s()
            sage: ls = LazySymmetricFunctions(s)
            sage: f = ls(lambda n: s([n]), valuation=1)
            sage: g = f.revert().suspension(); g
            s[1] + (s[1,1]) + (s[2,1]) + (s[2,1,1]+s[3,1]) + ...
            sage: g.revert().suspension()
            s[1] + s[2] + s[3] + s[4] + s[5] + ...
        """
    def functorial_composition(self, *args):
        """
        Return the functorial composition of ``self`` and ``g``.

        Let `X` be a finite set of cardinality `m`.  For a group
        action of the symmetric group `g: S_n \\to S_X` and a
        (possibly virtual) representation of the symmetric group on
        `X`, `f: S_X \\to GL(V)`, the functorial composition is the
        (virtual) representation of the symmetric group `f \\Box g:
        S_n \\to GL(V)` given by `\\sigma \\mapsto f(g(\\sigma))`.

        This is more naturally phrased in the language of
        combinatorial species.  Let `F` and `G` be species, then
        their functorial composition is the species `F \\Box G` with
        `(F \\Box G) [A] = F[ G[A] ]`.  In other words, an `(F \\Box
        G)`-structure on a set `A` of labels is an `F`-structure
        whose labels are the set of all `G`-structures on `A`.

        The Frobenius character (or cycle index series) of `F \\Box G`
        can be computed as follows, see section 2.2 of [BLL1998]_):

        .. MATH::

            \\sum_{n \\geq 0} \\frac{1}{n!} \\sum_{\\sigma \\in
            \\mathfrak{S}_{n}} \\operatorname{fix} F[ (G[\\sigma])_{1},
            (G[\\sigma])_{2}, \\ldots ] \\, p_{1}^{\\sigma_{1}}
            p_{2}^{\\sigma_{2}} \\cdots.

        .. WARNING::

            The operation `f \\Box g` only makes sense when `g`
            corresponds to a permutation representation, i.e., a
            group action.

        EXAMPLES:

        The species `G` of simple graphs can be expressed in terms of
        a functorial composition: `G = \\mathfrak{p} \\Box
        \\mathfrak{p}_{2}`, where `\\mathfrak{p}` is the
        :class:`~sage.combinat.species.subset_species.SubsetSpecies`.::

            sage: # needs sage.modules
            sage: R.<q> = QQ[]
            sage: h = SymmetricFunctions(R).h()
            sage: m = SymmetricFunctions(R).m()
            sage: L = LazySymmetricFunctions(m)
            sage: P = L(lambda n: sum(q^k*h[n-k]*h[k] for k in range(n+1)))
            sage: P2 = L(lambda n: h[2]*h[n-2], valuation=2)
            sage: P.functorial_composition(P2)[:4]                                      # needs sage.libs.pari
            [m[],
             m[1],
             (q+1)*m[1, 1] + (q+1)*m[2],
             (q^3+3*q^2+3*q+1)*m[1, 1, 1] + (q^3+2*q^2+2*q+1)*m[2, 1] + (q^3+q^2+q+1)*m[3]]

        For example, there are::

            sage: P.functorial_composition(P2)[4].coefficient([4])[3]                   # needs sage.libs.pari sage.modules
            3

        unlabelled graphs on 4 vertices and 3 edges, and::

            sage: P.functorial_composition(P2)[4].coefficient([2,2])[3]                 # needs sage.libs.pari sage.modules
            8

        labellings of their vertices with two 1s and two 2s.

        The symmetric function `h_1 \\sum_n h_n` is the neutral
        element with respect to functorial composition::

            sage: # needs sage.modules
            sage: p = SymmetricFunctions(QQ).p()
            sage: h = SymmetricFunctions(QQ).h()
            sage: e = SymmetricFunctions(QQ).e()
            sage: L = LazySymmetricFunctions(h)
            sage: H = L(lambda n: h[n])
            sage: Ep = p[1]*H.derivative_with_respect_to_p1(); Ep
            h[1] + (h[1,1]) + (h[2,1]) + (h[3,1]) + (h[4,1]) + (h[5,1]) + O^7
            sage: f = L(lambda n: h[n-n//2, n//2])
            sage: f - Ep.functorial_composition(f)                                      # needs sage.libs.pari
            O^7

        The symmetric function `\\sum_n h_n` is a left absorbing element::

            sage: # needs sage.modules
            sage: H.functorial_composition(f) - H
            O^7

        The functorial composition distributes over the sum::

            sage: # needs sage.modules
            sage: F1 = L(lambda n: h[n])
            sage: F2 = L(lambda n: e[n])
            sage: f1 = F1.functorial_composition(f)
            sage: f2 = F2.functorial_composition(f)
            sage: (F1 + F2).functorial_composition(f) - f1 - f2         # long time
            O^7

        TESTS:

        Check a corner case::

            sage: h = SymmetricFunctions(QQ).h()                                        # needs sage.modules
            sage: L = LazySymmetricFunctions(h)                                         # needs sage.modules
            sage: L(h[2,1]).functorial_composition(3*h[0])                              # needs sage.libs.pari sage.modules
            3*h[] + O^7

        Check an instance of a non-group action::

            sage: # needs sage.modules
            sage: s = SymmetricFunctions(QQ).s()
            sage: p = SymmetricFunctions(QQ).p()
            sage: L = LazySymmetricFunctions(p)
            sage: f = L(lambda n: s[n])
            sage: g = 2*s[2, 1, 1] + s[2, 2] + 3*s[4]
            sage: r = f.functorial_composition(g); r[4]                                 # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            ValueError: the argument is not the Frobenius character of a permutation representation
            sage: g = -p[1, 1, 1]
            sage: r = f.functorial_composition(g); r[3]
            Traceback (most recent call last):
            ...
            ValueError: the argument is not the Frobenius character of a permutation representation
        """
    def arithmetic_product(self, *args):
        '''
        Return the arithmetic product of ``self`` with ``g``.

        The arithmetic product is a binary operation `\\boxdot` on the
        ring of symmetric functions which is bilinear in its two
        arguments and satisfies

        .. MATH::

            p_{\\lambda} \\boxdot p_{\\mu} = \\prod\\limits_{i \\geq 1, j \\geq 1}
            p_{\\mathrm{lcm}(\\lambda_i, \\mu_j)}^{\\mathrm{gcd}(\\lambda_i, \\mu_j)}

        for any two partitions `\\lambda = (\\lambda_1, \\lambda_2, \\lambda_3,
        \\dots )` and `\\mu = (\\mu_1, \\mu_2, \\mu_3, \\dots )` (where `p_{\\nu}`
        denotes the power-sum symmetric function indexed by the partition
        `\\nu`, and `p_i` denotes the `i`-th power-sum symmetric function).
        This is enough to define the arithmetic product if the base ring
        is torsion-free as a `\\ZZ`-module; for all other cases the
        arithmetic product is uniquely determined by requiring it to be
        functorial in the base ring. See
        http://mathoverflow.net/questions/138148/ for a discussion of
        this arithmetic product.

        .. WARNING::

            The operation `f \\boxdot g` was originally defined only
            for symmetric functions `f` and `g` without constant
            term.  We extend this definition using the convention
            that the least common multiple of any integer with `0` is
            `0`.

        If `f` and `g` are two symmetric functions which are homogeneous
        of degrees `a` and `b`, respectively, then `f \\boxdot g` is
        homogeneous of degree `ab`.

        The arithmetic product is commutative and associative and has
        unity `e_1 = p_1 = h_1`.

        For species `M` and `N` such that `M[\\varnothing] =
        N[\\varnothing] = \\varnothing`, their arithmetic product is
        the species `M \\boxdot N` of "`M`-assemblies of cloned
        `N`-structures".  This operation is defined and several
        examples are given in [MM2008]_.

        INPUT:

        - ``g`` -- a cycle index series having the same parent as ``self``

        OUTPUT: the arithmetic product of ``self`` with ``g``

        .. SEEALSO::

          :meth:`sage.combinat.sf.sfa.SymmetricFunctionAlgebra_generic_Element.arithmetic_product`

        EXAMPLES:

        For `C` the species of (oriented) cycles and `L_{+}` the
        species of nonempty linear orders, `C \\boxdot L_{+}`
        corresponds to the species of "regular octopuses"; a `(C
        \\boxdot L_{+})`-structure is a cycle of some length, each of
        whose elements is an ordered list of a length which is
        consistent for all the lists in the structure. ::

            sage: R.<q> = QQ[]
            sage: p = SymmetricFunctions(R).p()                                         # needs sage.modules
            sage: m = SymmetricFunctions(R).m()                                         # needs sage.modules
            sage: L = LazySymmetricFunctions(m)                                         # needs sage.modules

            sage: # needs sage.modules
            sage: c = LazyCombinatorialSpecies(QQ, "X").Cycles().cycle_index_series()
            sage: Lplus = L(lambda n: p([1]*n), valuation=1)
            sage: r = c.arithmetic_product(Lplus); r                                    # needs sage.libs.pari
            m[1] + (3*m[1,1]+2*m[2])
             + (8*m[1,1,1]+4*m[2,1]+2*m[3])
             + (42*m[1,1,1,1]+21*m[2,1,1]+12*m[2,2]+7*m[3,1]+3*m[4])
             + (144*m[1,1,1,1,1]+72*m[2,1,1,1]+36*m[2,2,1]+24*m[3,1,1]+12*m[3,2]+6*m[4,1]+2*m[5])
             + ...
             + O^7

        In particular, the number of regular octopuses is::

            sage: [r[n].coefficient([1]*n) for n in range(8)]                           # needs sage.libs.pari sage.modules
            [0, 1, 3, 8, 42, 144, 1440, 5760]

        It is shown in [MM2008]_ that the exponential generating
        function for regular octopuses satisfies `(C \\boxdot L_{+})
        (x) = \\sum_{n \\geq 1} \\sigma (n) (n - 1)! \\frac{x^{n}}{n!}`
        (where `\\sigma (n)` is the sum of the divisors of `n`). ::

            sage: [sum(divisors(i))*factorial(i-1) for i in range(1,8)]                 # needs sage.modules
            [1, 3, 8, 42, 144, 1440, 5760]

        AUTHORS:

        - Andrew Gainer-Dewar (2013)

        REFERENCES:

        - [MM2008]_

        TESTS:

        Check that the product with zero works::

            sage: # needs sage.modules
            sage: s = SymmetricFunctions(QQ).s()
            sage: L = LazySymmetricFunctions(s)
            sage: L(0).arithmetic_product(s[2])
            0
            sage: L(s[2]).arithmetic_product(0)
            0

        Check that the arithmetic product of symmetric functions of
        finite support works::

            sage: L(s([2])).arithmetic_product(s([1,1,1]))                              # needs sage.modules
            s[2, 2, 1, 1] + s[3, 1, 1, 1] + s[3, 2, 1] + s[3, 3] + 2*s[4, 1, 1]

            sage: f = 1/(1-L(s[1]))                                                     # needs sage.modules
            sage: f.arithmetic_product(s[1]) - f                                        # needs lrcalc_python sage.modules
            O^7

        Check that the arithmetic product of symmetric functions with
        constant a term works as advertised::

            sage: p = SymmetricFunctions(QQ).p()                                        # needs sage.modules
            sage: L = LazySymmetricFunctions(p)                                         # needs sage.modules
            sage: L(5).arithmetic_product(3*p[2,1])                                     # needs sage.modules
            15*p[]

        Check the arithmetic product of symmetric functions over a
        finite field works::

            sage: s = SymmetricFunctions(FiniteField(2)).s()                            # needs sage.modules
            sage: L = LazySymmetricFunctions(s)                                         # needs sage.modules
            sage: L(s([2])).arithmetic_product(s([1,1,1]))                              # needs sage.modules
            s[2, 2, 1, 1] + s[3, 1, 1, 1] + s[3, 2, 1] + s[3, 3]
        '''
    def symmetric_function(self, degree=None):
        """
        Return ``self`` as a symmetric function if ``self`` is actually so.

        INPUT:

        - ``degree`` -- ``None`` or an integer

        OUTPUT:

        If ``degree`` is not ``None``, the terms of the series of
        degree greater than ``degree`` are first truncated.  If
        ``degree`` is ``None`` and the series is not a polynomial
        polynomial, a :exc:`ValueError` is raised.

        EXAMPLES::

            sage: # needs sage.modules
            sage: s = SymmetricFunctions(QQ).s()
            sage: S = LazySymmetricFunctions(s)
            sage: elt = S(s[2])
            sage: elt.symmetric_function()
            s[2]

        TESTS::

            sage: # needs sage.modules
            sage: s = SymmetricFunctions(QQ).s()
            sage: S = LazySymmetricFunctions(s)
            sage: elt = S(s[2])
            sage: elt.symmetric_function()
            s[2]
            sage: f = 1 / (1 - elt)
            sage: f                                                                     # needs lrcalc_python
            s[] + s[2] + (s[2,2]+s[3,1]+s[4]) + (s[2,2,2]+2*s[3,2,1]+s[3,3]+s[4,1,1]+3*s[4,2]+2*s[5,1]+s[6]) + O^7
            sage: f.symmetric_function()
            Traceback (most recent call last):
            ...
            ValueError: not a symmetric function

            sage: # needs sage.modules
            sage: f4 = f.truncate(5); f4                                                # needs lrcalc_python
            s[] + s[2] + (s[2,2]+s[3,1]+s[4])
            sage: f4.symmetric_function()                                               # needs lrcalc_python
            s[] + s[2] + s[2, 2] + s[3, 1] + s[4]
            sage: f4.symmetric_function() == f.symmetric_function(4)                    # needs lrcalc_python
            True
            sage: S.zero().symmetric_function()
            0
            sage: f4.symmetric_function(0)                                              # needs lrcalc_python
            s[]
        """

class LazyDirichletSeries(LazyModuleElement):
    '''
    A Dirichlet series where the coefficients are computed lazily.

    EXAMPLES::

        sage: L = LazyDirichletSeriesRing(ZZ, "z")
        sage: f = L(constant=1)^2
        sage: f                                                                         # needs sage.symbolic
        1 + 2/2^z + 2/3^z + 3/4^z + 2/5^z + 4/6^z + 2/7^z + O(1/(8^z))
        sage: f.coefficient(100) == number_of_divisors(100)                             # needs sage.libs.pari
        True

    Lazy Dirichlet series is picklable::

        sage: g = loads(dumps(f))
        sage: g                                                                         # needs sage.symbolic
        1 + 2/2^z + 2/3^z + 3/4^z + 2/5^z + 4/6^z + 2/7^z + O(1/(8^z))
        sage: g == f
        True
    '''
    def is_unit(self):
        '''
        Return whether this element is a unit in the ring.

        EXAMPLES::

            sage: D = LazyDirichletSeriesRing(ZZ, "s")
            sage: D([0, 2]).is_unit()
            False

            sage: D([-1, 2]).is_unit()
            True

            sage: D([3, 2]).is_unit()
            False

            sage: D = LazyDirichletSeriesRing(QQ, "s")
            sage: D([3, 2]).is_unit()
            True
        '''
    def valuation(self):
        '''
        Return the valuation of ``self``.

        This method determines the valuation of the series by looking for a
        nonzero coefficient. Hence if the series happens to be zero, then it
        may run forever.

        EXAMPLES::

            sage: L = LazyDirichletSeriesRing(ZZ, "z")
            sage: mu = L(moebius); mu.valuation()                                       # needs sage.libs.pari
            0
            sage: (mu - mu).valuation()                                                 # needs sage.libs.pari
            +Infinity
            sage: g = L(constant=1, valuation=2)
            sage: g.valuation()                                                         # needs sage.symbolic
            log(2)
            sage: (g*g).valuation()                                                     # needs sage.symbolic
            2*log(2)
        '''
    def __invert__(self):
        '''
        Return the multiplicative inverse of the element.

        TESTS::

            sage: L = LazyDirichletSeriesRing(ZZ, "z", sparse=False)
            sage: ~L(constant=1) - L(moebius)                                           # needs sage.libs.pari
            O(1/(8^z))
            sage: L = LazyDirichletSeriesRing(ZZ, "z", sparse=True)
            sage: ~L(constant=1) - L(moebius)                                           # needs sage.libs.pari
            O(1/(8^z))

        Trying to invert a non-invertible \'exact\' series raises a
        :exc:`ZeroDivisionError`::

            sage: f = ~L([0,1], constant=1)
            sage: f[1]
            Traceback (most recent call last):
            ...
            ZeroDivisionError: the Dirichlet inverse only exists if the coefficient with index 1 is nonzero

            sage: f = ~L(lambda n: n-1)
            sage: f[1]
            Traceback (most recent call last):
            ...
            ZeroDivisionError: rational division by zero
        '''
    def __call__(self, p):
        '''
        Return the composition of ``self`` with a linear polynomial ``p``.

        Return the series with the variable `s` replaced by a linear
        polynomial `a\\cdot s + b`, for positive `a`.

        When `f` is an exact Dirichlet series, we can write

        .. MATH::

            f(s) = \\sum_{n=1}^k a_n / n^s + C \\zeta(s).

        Thus we can evaluate this for `p \\in \\CC` by using the analytic
        continuation of the Riemann `\\zeta` function for `p \\in \\CC`
        with the real part of `p` at most `1`. In the case `p = 1`,
        this will return `\\infty` if `C \\neq 0`.

        EXAMPLES::

            sage: D = LazyDirichletSeriesRing(QQ, "s")
            sage: P.<s> = QQ[]
            sage: Z = D(constant=1)
            sage: from sage.arith.misc import dedekind_psi
            sage: Psi = D(dedekind_psi)
            sage: Z(s)*Z(s-1)/Z(2*s) - Psi                                              # needs sage.symbolic
            O(1/(8^s))

            sage: Z(s)*Z(s-1)/Z(2*s-2) - (1/Psi).map_coefficients(abs)                  # needs sage.symbolic
            O(1/(8^s))

            sage: # needs sage.symbolic
            sage: Z(5)
            zeta(5)
            sage: Z(1+I)
            zeta(I + 1)
            sage: Z(0)
            -1/2
            sage: Z(1)
            Infinity

            sage: f = D([1,2,-3,-4], valuation=2)
            sage: f                                                                     # needs sage.symbolic
            1/(2^s) + 2/3^s - 3/4^s - 4/5^s
            sage: f(2)
            449/3600
            sage: 1/2^2 + 2/3^2 + -3/4^2 + -4/5^2
            449/3600
            sage: f(0)
            -4
            sage: f(1)
            -23/60
            sage: f(-2)
            -126

            sage: f = D([4,2,-3,2])
            sage: f(0)
            5

            sage: f = D([1,2,-3,-4], constant=2)
            sage: bool(f(2) == -1 + -5/3^2 + -6/4^2 + 2*zeta(2))                        # needs sage.symbolic
            True
            sage: f(0)                                                                  # needs sage.symbolic
            -13
            sage: f(1)                                                                  # needs sage.symbolic
            Infinity
        '''
