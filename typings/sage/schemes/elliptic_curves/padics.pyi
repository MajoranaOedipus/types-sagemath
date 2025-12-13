import math
from sage.arith.misc import valuation as valuation
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc import newton_method_sizes as newton_method_sizes
from sage.rings.big_oh import O as O
from sage.rings.integer import Integer as Integer
from sage.rings.laurent_series_ring import LaurentSeriesRing as LaurentSeriesRing
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.power_series_ring import PowerSeriesRing as PowerSeriesRing
from sage.rings.rational_field import RationalField as RationalField

sqrt = math.sqrt

def padic_lseries(self, p, normalize=None, implementation: str = 'eclib', precision=None):
    '''
    Return the `p`-adic `L`-series of ``self`` at
    `p`, which is an object whose approx method computes
    approximation to the true `p`-adic `L`-series to
    any desired precision.

    INPUT:

    - ``p`` -- prime

    - ``normalize`` -- \'L_ratio\' (default), \'period\' or \'none\';
      this is describes the way the modular symbols
      are normalized. See modular_symbol for
      more details.

    - ``implementation`` -- \'eclib\' (default), \'sage\', \'num\' or \'pollackstevens\';
      Whether to use John Cremona\'s eclib, the Sage implementation,
      numerical modular symbols
      or Pollack-Stevens\' implementation of overconvergent
      modular symbols.

    EXAMPLES::

        sage: E = EllipticCurve(\'37a\')
        sage: L = E.padic_lseries(5); L
        5-adic L-series of Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field
        sage: type(L)
        <class \'sage.schemes.elliptic_curves.padic_lseries.pAdicLseriesOrdinary\'>

    We compute the `3`-adic `L`-series of two curves of
    rank `0` and in each case verify the interpolation property
    for their leading coefficient (i.e., value at 0)::

        sage: e = EllipticCurve(\'11a\')
        sage: ms = e.modular_symbol()
        sage: [ms(1/11), ms(1/3), ms(0), ms(oo)]
        [0, -3/10, 1/5, 0]
        sage: ms(0)
        1/5
        sage: L = e.padic_lseries(3)
        sage: P = L.series(5)
        sage: P(0)
        2 + 3 + 3^2 + 2*3^3 + 2*3^5 + 3^6 + O(3^7)
        sage: alpha = L.alpha(9); alpha
        2 + 3^2 + 2*3^3 + 2*3^4 + 2*3^6 + 3^8 + O(3^9)
        sage: R.<x> = QQ[]
        sage: f = x^2 - e.ap(3)*x + 3
        sage: f(alpha)
        O(3^9)
        sage: r = e.lseries().L_ratio(); r
        1/5
        sage: (1 - alpha^(-1))^2 * r
        2 + 3 + 3^2 + 2*3^3 + 2*3^5 + 3^6 + 3^7 + O(3^9)
        sage: P(0)
        2 + 3 + 3^2 + 2*3^3 + 2*3^5 + 3^6 + O(3^7)

    Next consider the curve 37b::

        sage: e = EllipticCurve(\'37b\')
        sage: L = e.padic_lseries(3)
        sage: P = L.series(5)
        sage: alpha = L.alpha(9); alpha
        1 + 2*3 + 3^2 + 2*3^5 + 2*3^7 + 3^8 + O(3^9)
        sage: r = e.lseries().L_ratio(); r
        1/3
        sage: (1 - alpha^(-1))^2 * r
        3 + 3^2 + 2*3^4 + 2*3^5 + 2*3^6 + 3^7 + O(3^9)
        sage: P(0)
        3 + 3^2 + 2*3^4 + 2*3^5 + O(3^6)

    We can use Sage modular symbols instead to compute the `L`-series::

        sage: e = EllipticCurve(\'11a\')
        sage: L = e.padic_lseries(3, implementation = \'sage\')
        sage: L.series(5,prec=10)
        2 + 3 + 3^2 + 2*3^3 + 2*3^5 + 3^6 + O(3^7) + (1 + 3 + 2*3^2 + 3^3 + O(3^4))*T + (1 + 2*3 + O(3^4))*T^2 + (3 + 2*3^2 + O(3^3))*T^3 + (2*3 + 3^2 + O(3^3))*T^4 + (2 + 2*3 + 2*3^2 + O(3^3))*T^5 + (1 + 3^2 + O(3^3))*T^6 + (2 + 3^2 + O(3^3))*T^7 + (2 + 2*3 + 2*3^2 + O(3^3))*T^8 + (2 + O(3^2))*T^9 + O(T^10)

    Also the numerical modular symbols can be used.
    This may allow for much larger conductor in some instances::

        sage: E = EllipticCurve([101,103])
        sage: L = E.padic_lseries(5, implementation=\'num\')
        sage: L.series(2)
        O(5^4) + (3 + O(5))*T + (1 + O(5))*T^2 + (3 + O(5))*T^3 + O(5)*T^4 + O(T^5)

    Finally, we can use the overconvergent method of Pollack-Stevens.::

        sage: e = EllipticCurve(\'11a\')
        sage: L = e.padic_lseries(3, implementation = \'pollackstevens\', precision = 6)
        sage: L.series(5)
        2 + 3 + 3^2 + 2*3^3 + 2*3^5 + O(3^6) + (1 + 3 + 2*3^2 + 3^3 + O(3^4))*T + (1 + 2*3 + O(3^2))*T^2 + (3 + O(3^2))*T^3 + O(3^0)*T^4 + O(T^5)
        sage: L[3]
        3 + O(3^2)

    Another example with a semistable prime.::

        sage: E = EllipticCurve("11a1")
        sage: L = E.padic_lseries(11, implementation = \'pollackstevens\', precision=3)
        sage: L[1]
        10 + 3*11 + O(11^2)
        sage: L[3]
        O(11^0)
    '''
def padic_regulator(self, p, prec: int = 20, height=None, check_hypotheses: bool = True):
    '''
    Compute the cyclotomic `p`-adic regulator of this curve.
    The model of the curve needs to be integral and minimal at `p`.
    Moreover the reduction at `p` should not be additive.

    INPUT:

    - ``p`` -- prime >= 5

    - ``prec`` -- answer will be returned modulo `p^{\\mathrm{prec}}`

    - ``height`` -- precomputed height function; if not supplied, this function
      will call ``padic_height`` to compute it

    - ``check_hypotheses`` -- boolean; whether to check
      that this is a curve for which the `p`-adic height makes sense

    OUTPUT: the `p`-adic cyclotomic regulator of this curve, to the
    requested precision

    If the rank is 0, we output 1.

    AUTHORS:

    - Liang Xiao: original implementation at the 2006 MSRI
      graduate workshop on modular forms

    - David Harvey (2006-09-13): cleaned up and integrated into Sage,
      removed some redundant height computations

    - Chris Wuthrich (2007-05-22): added multiplicative and
      supersingular cases

    - David Harvey (2007-09-20): fixed some precision loss that was
      occurring

    EXAMPLES::

        sage: E = EllipticCurve("37a")
        sage: E.padic_regulator(5, 10)
        5 + 5^2 + 5^3 + 3*5^6 + 4*5^7 + 5^9 + O(5^10)

    An anomalous case::

        sage: E.padic_regulator(53, 10)
        26*53^-1 + 30 + 20*53 + 47*53^2 + 10*53^3 + 32*53^4 + 9*53^5 + 22*53^6 + 35*53^7 + 30*53^8 + O(53^9)

    An anomalous case where the precision drops some::

        sage: E = EllipticCurve("5077a")
        sage: E.padic_regulator(5, 10)
        5 + 5^2 + 4*5^3 + 2*5^4 + 2*5^5 + 2*5^6 + 4*5^7 + 2*5^8 + 5^9 + O(5^10)

    Check that answers agree over a range of precisions::

        sage: max_prec = 30    # make sure we get past p^2    # long time
        sage: full = E.padic_regulator(5, max_prec)           # long time
        sage: for prec in range(1, max_prec):                 # long time
        ....:     assert E.padic_regulator(5, prec) == full

    A case where the generator belongs to the formal group already
    (:issue:`3632`)::

        sage: E = EllipticCurve([37,0])
        sage: E.padic_regulator(5,10)
        2*5^2 + 2*5^3 + 5^4 + 5^5 + 4*5^6 + 3*5^8 + 4*5^9 + O(5^10)

    The result is not dependent on the model for the curve::

        sage: E = EllipticCurve([0,0,0,0,2^12*17])
        sage: Em = E.minimal_model()
        sage: E.padic_regulator(7) == Em.padic_regulator(7)
        True

    Allow a python int as input::

        sage: E = EllipticCurve(\'37a\')
        sage: E.padic_regulator(int(5))
        5 + 5^2 + 5^3 + 3*5^6 + 4*5^7 + 5^9 + 5^10 + 3*5^11 + 3*5^12 + 5^13 + 4*5^14 + 5^15 + 2*5^16 + 5^17 + 2*5^18 + 4*5^19 + O(5^20)
    '''
def padic_height_pairing_matrix(self, p, prec: int = 20, height=None, check_hypotheses: bool = True):
    '''
    Compute the cyclotomic `p`-adic height pairing matrix of
    this curve with respect to the basis ``self.gens()`` for the
    Mordell-Weil group for a given odd prime `p` of good ordinary
    reduction.
    The model needs to be integral and minimal at `p`.

    INPUT:

    - ``p`` -- prime >= 5

    - ``prec`` -- answer will be returned modulo `p^{\\mathrm{prec}}`

    - ``height`` -- precomputed height function; if not supplied, this function
      will call ``padic_height`` to compute it

    - ``check_hypotheses`` -- boolean; whether to check that this is a curve
      for which the `p`-adic height makes sense

    OUTPUT: the `p`-adic cyclotomic height pairing matrix of this curve
    to the given precision

    AUTHORS:

    - David Harvey, Liang Xiao, Robert Bradshaw, Jennifer
      Balakrishnan: original implementation at the 2006 MSRI graduate
      workshop on modular forms

    - David Harvey (2006-09-13): cleaned up and integrated into Sage,
      removed some redundant height computations

    EXAMPLES::

        sage: E = EllipticCurve("37a")
        sage: E.padic_height_pairing_matrix(5, 10)
        [5 + 5^2 + 5^3 + 3*5^6 + 4*5^7 + 5^9 + O(5^10)]

    A rank two example::

        sage: e =EllipticCurve(\'389a\')
        sage: e._set_gens([e(-1, 1), e(1,0)])  # avoid platform dependent gens
        sage: e.padic_height_pairing_matrix(5,10)
        [                      3*5 + 2*5^2 + 5^4 + 5^5 + 5^7 + 4*5^9 + O(5^10) 5 + 4*5^2 + 5^3 + 2*5^4 + 3*5^5 + 4*5^6 + 5^7 + 5^8 + 2*5^9 + O(5^10)]
        [5 + 4*5^2 + 5^3 + 2*5^4 + 3*5^5 + 4*5^6 + 5^7 + 5^8 + 2*5^9 + O(5^10)                         4*5 + 2*5^4 + 3*5^6 + 4*5^7 + 4*5^8 + O(5^10)]

    An anomalous rank 3 example::

        sage: e = EllipticCurve("5077a")
        sage: e._set_gens([e(-1,3), e(2,0), e(4,6)])
        sage: e.padic_height_pairing_matrix(5,4)
        [4 + 3*5 + 4*5^2 + 4*5^3 + O(5^4)       4 + 4*5^2 + 2*5^3 + O(5^4)       3*5 + 4*5^2 + 5^3 + O(5^4)]
        [      4 + 4*5^2 + 2*5^3 + O(5^4)   3 + 4*5 + 3*5^2 + 5^3 + O(5^4)                 2 + 4*5 + O(5^4)]
        [      3*5 + 4*5^2 + 5^3 + O(5^4)                 2 + 4*5 + O(5^4)     1 + 3*5 + 5^2 + 5^3 + O(5^4)]
    '''
def padic_height(self, p, prec: int = 20, sigma=None, check_hypotheses: bool = True):
    '''
    Compute the cyclotomic `p`-adic height.

    The equation of the curve must be integral and minimal at `p`.

    INPUT:

    - ``p`` -- prime >= 5 for which the curve has semi-stable reduction

    - ``prec`` -- integer >= 1 (default: 20); desired precision of result

    - ``sigma`` -- precomputed value of sigma; if not supplied, this function
      will call ``padic_sigma`` to compute it

    - ``check_hypotheses`` -- boolean; whether to check that this is a curve
      for which the `p`-adic height makes sense

    OUTPUT:

    A function that accepts two parameters:

    - a `\\QQ`-rational point on the curve whose height should be computed

    - optional boolean flag \'check\': if ``False``, it skips some input
      checking, and returns the `p`-adic height of that point to the
      desired precision.

    - The normalization (sign and a factor 1/2 with respect to some other
      normalizations that appear in the literature) is chosen in such a way
      as to make the `p`-adic Birch Swinnerton-Dyer conjecture hold as stated
      in [MTT1986]_.

    AUTHORS:

    - Jennifer Balakrishnan: original code developed at the 2006 MSRI
      graduate workshop on modular forms

    - David Harvey (2006-09-13): integrated into Sage, optimised to
      speed up repeated evaluations of the returned height function,
      addressed some thorny precision questions

    - David Harvey (2006-09-30): rewrote to use division polynomials
      for computing denominator of `nP`.

    - David Harvey (2007-02): cleaned up according to algorithms in
      "Efficient Computation of p-adic Heights"

    - Chris Wuthrich (2007-05): added supersingular and multiplicative heights

    EXAMPLES::

        sage: E = EllipticCurve("37a")
        sage: P = E.gens()[0]
        sage: h = E.padic_height(5, 10)
        sage: h(P)
        5 + 5^2 + 5^3 + 3*5^6 + 4*5^7 + 5^9 + O(5^10)

    An anomalous case::

        sage: h = E.padic_height(53, 10)
        sage: h(P)
        26*53^-1 + 30 + 20*53 + 47*53^2 + 10*53^3 + 32*53^4 + 9*53^5 + 22*53^6 + 35*53^7 + 30*53^8 + 17*53^9 + O(53^10)

    Boundary case::

        sage: E.padic_height(5, 3)(P)
        5 + 5^2 + O(5^3)

    A case that works the division polynomial code a little harder::

        sage: E.padic_height(5, 10)(5*P)
        5^3 + 5^4 + 5^5 + 3*5^8 + 4*5^9 + O(5^10)

    Check that answers agree over a range of precisions::

        sage: max_prec = 30    # make sure we get past p^2    # long time
        sage: full = E.padic_height(5, max_prec)(P)           # long time
        sage: for prec in range(1, max_prec):                 # long time
        ....:     assert E.padic_height(5, prec)(P) == full

    A supersingular prime for a curve::

        sage: E = EllipticCurve(\'37a\')
        sage: E.is_supersingular(3)
        True
        sage: h = E.padic_height(3, 5)
        sage: h(E.gens()[0])
        (3 + 3^3 + O(3^6), 2*3^2 + 3^3 + 3^4 + 3^5 + 2*3^6 + O(3^7))
        sage: E.padic_regulator(5)
        5 + 5^2 + 5^3 + 3*5^6 + 4*5^7 + 5^9 + 5^10 + 3*5^11 + 3*5^12 + 5^13 + 4*5^14 + 5^15 + 2*5^16 + 5^17 + 2*5^18 + 4*5^19 + O(5^20)
        sage: E.padic_regulator(3, 5)
        (3 + 2*3^2 + 3^3 + O(3^4), 3^2 + 2*3^3 + 3^4 + O(3^5))

    A torsion point in both the good and supersingular cases::

        sage: E = EllipticCurve(\'11a\')
        sage: P = E.torsion_subgroup().gen(0).element(); P
        (5 : 5 : 1)
        sage: h = E.padic_height(19, 5)
        sage: h(P)
        0
        sage: h = E.padic_height(5, 5)
        sage: h(P)
        0

    The result is not dependent on the model for the curve::

        sage: E = EllipticCurve([0,0,0,0,2^12*17])
        sage: Em = E.minimal_model()
        sage: P = E.gens()[0]
        sage: Pm = Em.gens()[0]
        sage: h = E.padic_height(7)
        sage: hm = Em.padic_height(7)
        sage: h(P) == hm(Pm)
        True

    TESTS:

    Check that issue :issue:`20798` is solved::

        sage: E = EllipticCurve("91b")
        sage: h = E.padic_height(7,10)
        sage: P = E.gen(0)
        sage: h(P)
        2*7 + 7^2 + 5*7^3 + 6*7^4 + 2*7^5 + 3*7^6 + 7^7 + 4*7^9 + 5*7^10 + O(7^11)
        sage: h(P+P)
        7 + 5*7^2 + 6*7^3 + 5*7^4 + 4*7^5 + 6*7^6 + 5*7^7 + 2*7^9 + 7^10 + O(7^11)
    '''
def padic_height_via_multiply(self, p, prec: int = 20, E2=None, check_hypotheses: bool = True):
    '''
    Compute the cyclotomic `p`-adic height.

    The equation of the curve must be minimal at `p`.

    INPUT:

    - ``p`` -- prime >= 5 for which the curve has good ordinary reduction

    - ``prec`` -- integer >= 2 (default: 20); desired precision of result

    - ``E2`` -- precomputed value of E2. If not supplied,
      this function will call padic_E2 to compute it. The value supplied
      must be correct mod `p^{prec-2}` (or slightly higher in the
      anomalous case; see the code for details).

    - ``check_hypotheses`` -- boolean; whether to check
      that this is a curve for which the `p`-adic height makes sense

    OUTPUT:

    A function that accepts two parameters:

    - a `\\QQ`-rational point on the curve whose height should be computed

    - optional boolean flag \'check\': if ``False``, it skips some input
      checking, and returns the `p`-adic height of that point to the
      desired precision.

    - The normalization (sign and a factor 1/2 with respect to some other
      normalizations that appear in the literature) is chosen in such a way
      as to make the `p`-adic Birch Swinnerton-Dyer conjecture hold as stated
      in [MTT1986]_.

    AUTHORS:

    - David Harvey (2008-01): based on the padic_height() function,
      using the algorithm of [Har2009]_.

    EXAMPLES::

        sage: E = EllipticCurve("37a")
        sage: P = E.gens()[0]
        sage: h = E.padic_height_via_multiply(5, 10)
        sage: h(P)
        5 + 5^2 + 5^3 + 3*5^6 + 4*5^7 + 5^9 + O(5^10)

    An anomalous case::

        sage: h = E.padic_height_via_multiply(53, 10)
        sage: h(P)
        26*53^-1 + 30 + 20*53 + 47*53^2 + 10*53^3 + 32*53^4 + 9*53^5 + 22*53^6 + 35*53^7 + 30*53^8 + 17*53^9 + O(53^10)

    Supply the value of E2 manually::

        sage: E2 = E.padic_E2(5, 8)
        sage: E2
        2 + 4*5 + 2*5^3 + 5^4 + 3*5^5 + 2*5^6 + O(5^8)
        sage: h = E.padic_height_via_multiply(5, 10, E2=E2)
        sage: h(P)
        5 + 5^2 + 5^3 + 3*5^6 + 4*5^7 + 5^9 + O(5^10)

    Boundary case::

        sage: E.padic_height_via_multiply(5, 3)(P)
        5 + 5^2 + O(5^3)

    Check that answers agree over a range of precisions::

        sage: max_prec = 30    # make sure we get past p^2    # long time
        sage: full = E.padic_height(5, max_prec)(P)           # long time
        sage: for prec in range(2, max_prec):                 # long time
        ....:     assert E.padic_height_via_multiply(5, prec)(P) == full
    '''
def padic_sigma(self, p, N: int = 20, E2=None, check: bool = False, check_hypotheses: bool = True):
    '''
    Compute the `p`-adic sigma function with respect to the standard
    invariant differential `dx/(2y + a_1 x + a_3)`, as
    defined by Mazur and Tate in [MT1991]_, as a power series in the usual
    uniformiser `t` at the origin.

    The equation of the curve must be minimal at `p`.

    INPUT:

    - ``p`` -- prime >= 5 for which the curve has good ordinary reduction

    - ``N`` -- integer >= 1 (default: 20); precision of result,
      see OUTPUT section for description

    - ``E2`` -- precomputed value of E2. If not supplied,
      this function will call padic_E2 to compute it. The value supplied
      must be correct mod `p^{N-2}`.

    - ``check`` -- boolean; whether to perform a
      consistency check (i.e. verify that the computed sigma satisfies
      the defining

    - ``differential equation`` -- note that this does NOT guarantee
      correctness of all the returned digits, but it comes pretty close

    - ``check_hypotheses`` -- boolean; whether to check that this is a curve
      for which the `p`-adic sigma function makes sense

    OUTPUT: a power series `t + \\cdots` with coefficients in `\\ZZ_p`

    The output series will be truncated at `O(t^{N+1})`, and
    the coefficient of `t^n` for `n \\geq 1` will be
    correct to precision `O(p^{N-n+1})`.

    In practice this means the following. If `t_0 = p^k u`,
    where `u` is a `p`-adic unit with at least
    `N` digits of precision, and `k \\geq 1`, then the
    returned series may be used to compute `\\sigma(t_0)`
    correctly modulo `p^{N+k}` (i.e. with `N` correct
    `p`-adic digits).

    ALGORITHM: Described in "Efficient Computation of p-adic Heights"
    (David Harvey) [Har2009]_ which is basically an optimised version of the
    algorithm from "p-adic Heights and Log Convergence" (Mazur, Stein,
    Tate) [MST2006]_.

    Running time is soft-`O(N^2 \\log p)`, plus whatever time is
    necessary to compute `E_2`.

    AUTHORS:

    - David Harvey (2006-09-12)

    - David Harvey (2007-02): rewrote

    EXAMPLES::

        sage: EllipticCurve([-1, 1/4]).padic_sigma(5, 10)
        O(5^11) + (1 + O(5^10))*t + O(5^9)*t^2 + (3 + 2*5^2 + 3*5^3 + 3*5^6 + 4*5^7 + O(5^8))*t^3 + O(5^7)*t^4 + (2 + 4*5^2 + 4*5^3 + 5^4 + 5^5 + O(5^6))*t^5 + O(5^5)*t^6 + (2 + 2*5 + 5^2 + 4*5^3 + O(5^4))*t^7 + O(5^3)*t^8 + (1 + 2*5 + O(5^2))*t^9 + O(5)*t^10 + O(t^11)

    Run it with a consistency check::

        sage: EllipticCurve("37a").padic_sigma(5, 10, check=True)
        O(5^11) + (1 + O(5^10))*t + O(5^9)*t^2 + (3 + 2*5^2 + 3*5^3 + 3*5^6 + 4*5^7 + O(5^8))*t^3 + (3 + 2*5 + 2*5^2 + 2*5^3 + 2*5^4 + 2*5^5 + 2*5^6 + O(5^7))*t^4 + (2 + 4*5^2 + 4*5^3 + 5^4 + 5^5 + O(5^6))*t^5 + (2 + 3*5 + 5^4 + O(5^5))*t^6 + (4 + 3*5 + 2*5^2 + O(5^4))*t^7 + (2 + 3*5 + 2*5^2 + O(5^3))*t^8 + (4*5 + O(5^2))*t^9 + (1 + O(5))*t^10 + O(t^11)

    Boundary cases::

        sage: EllipticCurve([1, 1, 1, 1, 1]).padic_sigma(5, 1)
         (1 + O(5))*t + O(t^2)
        sage: EllipticCurve([1, 1, 1, 1, 1]).padic_sigma(5, 2)
         (1 + O(5^2))*t + (3 + O(5))*t^2 + O(t^3)

    Supply your very own value of E2::

        sage: X = EllipticCurve("37a")
        sage: my_E2 = X.padic_E2(5, 8)
        sage: my_E2 = my_E2 + 5**5    # oops!!!
        sage: X.padic_sigma(5, 10, E2=my_E2)
        O(5^11) + (1 + O(5^10))*t + O(5^9)*t^2 + (3 + 2*5^2 + 3*5^3 + 4*5^5 + 2*5^6 + 3*5^7 + O(5^8))*t^3 + (3 + 2*5 + 2*5^2 + 2*5^3 + 2*5^4 + 2*5^5 + 2*5^6 + O(5^7))*t^4 + (2 + 4*5^2 + 4*5^3 + 5^4 + 3*5^5 + O(5^6))*t^5 + (2 + 3*5 + 5^4 + O(5^5))*t^6 + (4 + 3*5 + 2*5^2 + O(5^4))*t^7 + (2 + 3*5 + 2*5^2 + O(5^3))*t^8 + (4*5 + O(5^2))*t^9 + (1 + O(5))*t^10 + O(t^11)

    Check that sigma is "weight 1".

    ::

        sage: f = EllipticCurve([-1, 3]).padic_sigma(5, 10)
        sage: g = EllipticCurve([-1*(2**4), 3*(2**6)]).padic_sigma(5, 10)
        sage: t = f.parent().gen()
        sage: f(2*t)/2
        (1 + O(5^10))*t + (4 + 3*5 + 3*5^2 + 3*5^3 + 4*5^4 + 4*5^5 + 3*5^6 + 5^7 + O(5^8))*t^3 + (3 + 3*5^2 + 5^4 + 2*5^5 + O(5^6))*t^5 + (4 + 5 + 3*5^3 + O(5^4))*t^7 + (4 + 2*5 + O(5^2))*t^9 + O(5)*t^10 + O(t^11)
        sage: g
        O(5^11) + (1 + O(5^10))*t + O(5^9)*t^2 + (4 + 3*5 + 3*5^2 + 3*5^3 + 4*5^4 + 4*5^5 + 3*5^6 + 5^7 + O(5^8))*t^3 + O(5^7)*t^4 + (3 + 3*5^2 + 5^4 + 2*5^5 + O(5^6))*t^5 + O(5^5)*t^6 + (4 + 5 + 3*5^3 + O(5^4))*t^7 + O(5^3)*t^8 + (4 + 2*5 + O(5^2))*t^9 + O(5)*t^10 + O(t^11)
        sage: f(2*t)/2 -g
        O(t^11)

    Test that it returns consistent results over a range of precision::

        sage: # long time
        sage: max_N = 30   # get up to at least p^2
        sage: E = EllipticCurve([1, 1, 1, 1, 1])
        sage: p = 5
        sage: E2 = E.padic_E2(5, max_N)
        sage: max_sigma = E.padic_sigma(p, max_N, E2=E2)
        sage: for N in range(3, max_N):
        ....:    sigma = E.padic_sigma(p, N, E2=E2)
        ....:    assert sigma == max_sigma
    '''
def padic_sigma_truncated(self, p, N: int = 20, lamb: int = 0, E2=None, check_hypotheses: bool = True):
    '''
    Compute the `p`-adic sigma function with respect to the standard
    invariant differential `dx/(2y + a_1 x + a_3)`, as
    defined by Mazur and Tate in [MT1991]_, as a power series in the usual
    uniformiser `t` at the origin.

    The equation of the curve must be minimal at `p`.

    This function differs from :func:`padic_sigma` in the precision profile
    of the returned power series; see OUTPUT below.

    INPUT:

    - ``p`` -- prime >= 5 for which the curve has good ordinary reduction

    - ``N`` -- integer >= 2 (default: 20); precision of result,
      see OUTPUT section for description

    - ``lamb`` -- integer >= 0; see OUTPUT section for description

    - ``E2`` -- precomputed value of E2. If not supplied,
      this function will call padic_E2 to compute it. The value supplied
      must be correct mod `p^{N-2}`.

    - ``check_hypotheses`` -- boolean; whether to check that this is a curve
      for which the `p`-adic sigma function makes sense

    OUTPUT: a power series `t + \\cdots` with coefficients in `\\ZZ_p`

    The coefficient of `t^j` for `j \\geq 1` will be
    correct to precision `O(p^{N - 2 + (3 - j)(lamb + 1)})`.

    ALGORITHM: Described in "Efficient Computation of p-adic Heights"
    [Har2009]_, which is basically an
    optimised version of the algorithm from "p-adic Heights and Log
    Convergence" (Mazur, Stein, Tate) [MST2006]_.

    Running time is soft-`O(N^2 \\lambda^{-1} \\log p)`, plus
    whatever time is necessary to compute `E_2`.

    AUTHORS:

    - David Harvey (2008-01): wrote based on previous
      :func:`padic_sigma` function

    EXAMPLES::

        sage: E = EllipticCurve([-1, 1/4])
        sage: E.padic_sigma_truncated(5, 10)
        O(5^11) + (1 + O(5^10))*t + O(5^9)*t^2 + (3 + 2*5^2 + 3*5^3 + 3*5^6 + 4*5^7 + O(5^8))*t^3 + O(5^7)*t^4 + (2 + 4*5^2 + 4*5^3 + 5^4 + 5^5 + O(5^6))*t^5 + O(5^5)*t^6 + (2 + 2*5 + 5^2 + 4*5^3 + O(5^4))*t^7 + O(5^3)*t^8 + (1 + 2*5 + O(5^2))*t^9 + O(5)*t^10 + O(t^11)

    Note the precision of the `t^3` coefficient depends only on
    `N`, not on lamb::

        sage: E.padic_sigma_truncated(5, 10, lamb=2)
        O(5^17) + (1 + O(5^14))*t + O(5^11)*t^2 + (3 + 2*5^2 + 3*5^3 + 3*5^6 + 4*5^7 + O(5^8))*t^3 + O(5^5)*t^4 + (2 + O(5^2))*t^5 + O(t^6)

    Compare against plain padic_sigma() function over a dense range of
    N and lamb

    ::

        sage: E = EllipticCurve([1, 2, 3, 4, 7])                            # long time
        sage: E2 = E.padic_E2(5, 50)                                        # long time
        sage: for N in range(2, 10):                                        # long time
        ....:    for lamb in range(10):
        ....:       correct = E.padic_sigma(5, N + 3*lamb, E2=E2)
        ....:       compare = E.padic_sigma_truncated(5, N=N, lamb=lamb, E2=E2)
        ....:       assert compare == correct
    '''
def padic_E2(self, p, prec: int = 20, check: bool = False, check_hypotheses: bool = True, algorithm: str = 'auto'):
    '''
    Return the value of the `p`-adic modular form `E2`
    for `(E, \\omega)` where `\\omega` is the usual
    invariant differential `dx/(2y + a_1 x + a_3)`.

    INPUT:

    - ``p`` -- prime (= 5) for which `E` is good and ordinary

    - ``prec`` -- (relative) `p`-adic precision (= 1) for result

    - ``check`` -- boolean; whether to perform a consistency check. This will
      slow down the computation by a constant factor 2. (The consistency check
      is to compute the whole matrix of frobenius on Monsky-Washnitzer
      cohomology, and verify that its trace is correct to the specified
      precision. Otherwise, the trace is used to compute one column from the
      other one (possibly after a change of basis).)

    - ``check_hypotheses`` -- boolean; whether to check that this is a curve
      for which the `p`-adic sigma function makes sense

    - ``algorithm`` -- one of ``\'standard\'``, ``\'sqrtp\'``, or
      ``\'auto\'``. This selects which version of Kedlaya\'s algorithm is used.
      The ``\'standard\'`` one is the one described in Kedlaya\'s paper. The
      ``\'sqrtp\'`` one has better performance for large `p`, but only
      works when `p > 6N` (`N=` ``prec``). The ``\'auto\'`` option
      selects ``\'sqrtp\'`` whenever possible.

      Note that if the ``\'sqrtp\'`` algorithm is used, a consistency check
      will automatically be applied, regardless of the setting of the
      ``check`` flag.

    OUTPUT: `p`-adic number to precision ``prec``

    .. NOTE::

        If the discriminant of the curve has nonzero valuation at p,
        then the result will not be returned mod `p^\\text{prec}`,
        but it still *will* have ``prec`` *digits* of precision.

    .. TODO::

        Once we have a better implementation of the "standard"
        algorithm, the algorithm selection strategy for "auto" needs to be
        revisited.

    AUTHORS:

    - David Harvey (2006-09-01): partly based on code written
      by Robert Bradshaw at the MSRI 2006 modular forms workshop

    ACKNOWLEDGMENT: - discussion with Eyal Goren that led to the trace
    trick.

    EXAMPLES: Here is the example discussed in the paper "Computation
    of p-adic Heights and Log Convergence" (Mazur, Stein, Tate) [MST2006]_::

        sage: EllipticCurve([-1, 1/4]).padic_E2(5)
        2 + 4*5 + 2*5^3 + 5^4 + 3*5^5 + 2*5^6 + 5^8 + 3*5^9 + 4*5^10 + 2*5^11 + 2*5^12 + 2*5^14 + 3*5^15 + 3*5^16 + 3*5^17 + 4*5^18 + 2*5^19 + O(5^20)

    Let\'s try to higher precision (this is the same answer the MAGMA
    implementation gives)::

        sage: EllipticCurve([-1, 1/4]).padic_E2(5, 100)
        2 + 4*5 + 2*5^3 + 5^4 + 3*5^5 + 2*5^6 + 5^8 + 3*5^9 + 4*5^10 + 2*5^11 + 2*5^12 + 2*5^14 + 3*5^15 + 3*5^16 + 3*5^17 + 4*5^18 + 2*5^19 + 4*5^20 + 5^21 + 4*5^22 + 2*5^23 + 3*5^24 + 3*5^26 + 2*5^27 + 3*5^28 + 2*5^30 + 5^31 + 4*5^33 + 3*5^34 + 4*5^35 + 5^36 + 4*5^37 + 4*5^38 + 3*5^39 + 4*5^41 + 2*5^42 + 3*5^43 + 2*5^44 + 2*5^48 + 3*5^49 + 4*5^50 + 2*5^51 + 5^52 + 4*5^53 + 4*5^54 + 3*5^55 + 2*5^56 + 3*5^57 + 4*5^58 + 4*5^59 + 5^60 + 3*5^61 + 5^62 + 4*5^63 + 5^65 + 3*5^66 + 2*5^67 + 5^69 + 2*5^70 + 3*5^71 + 3*5^72 + 5^74 + 5^75 + 5^76 + 3*5^77 + 4*5^78 + 4*5^79 + 2*5^80 + 3*5^81 + 5^82 + 5^83 + 4*5^84 + 3*5^85 + 2*5^86 + 3*5^87 + 5^88 + 2*5^89 + 4*5^90 + 4*5^92 + 3*5^93 + 4*5^94 + 3*5^95 + 2*5^96 + 4*5^97 + 4*5^98 + 2*5^99 + O(5^100)

    Check it works at low precision too::

        sage: EllipticCurve([-1, 1/4]).padic_E2(5, 1)
        2 + O(5)
        sage: EllipticCurve([-1, 1/4]).padic_E2(5, 2)
        2 + 4*5 + O(5^2)
        sage: EllipticCurve([-1, 1/4]).padic_E2(5, 3)
        2 + 4*5 + O(5^3)

    TODO: With the old(-er), i.e., = sage-2.4 `p`-adics we got
    `5 + O(5^2)` as output, i.e., relative precision 1, but
    with the newer `p`-adics we get relative precision 0 and absolute
    precision 1.

    ::

        sage: EllipticCurve([1, 1, 1, 1, 1]).padic_E2(5, 1)
        O(5)

    Check it works for different models of the same curve (37a), even
    when the discriminant changes by a power of p (note that E2 depends
    on the differential too, which is why it gets scaled in some of the
    examples below)::

        sage: X1 = EllipticCurve([-1, 1/4])
        sage: X1.j_invariant(), X1.discriminant()
         (110592/37, 37)
        sage: X1.padic_E2(5, 10)
         2 + 4*5 + 2*5^3 + 5^4 + 3*5^5 + 2*5^6 + 5^8 + 3*5^9 + O(5^10)

    ::

        sage: X2 = EllipticCurve([0, 0, 1, -1, 0])
        sage: X2.j_invariant(), X2.discriminant()
         (110592/37, 37)
        sage: X2.padic_E2(5, 10)
         2 + 4*5 + 2*5^3 + 5^4 + 3*5^5 + 2*5^6 + 5^8 + 3*5^9 + O(5^10)

    ::

        sage: X3 = EllipticCurve([-1*(2**4), 1/4*(2**6)])
        sage: X3.j_invariant(), X3.discriminant() / 2**12
         (110592/37, 37)
        sage: 2**(-2) * X3.padic_E2(5, 10)
         2 + 4*5 + 2*5^3 + 5^4 + 3*5^5 + 2*5^6 + 5^8 + 3*5^9 + O(5^10)

    ::

        sage: X4 = EllipticCurve([-1*(7**4), 1/4*(7**6)])
        sage: X4.j_invariant(), X4.discriminant() / 7**12
         (110592/37, 37)
        sage: 7**(-2) * X4.padic_E2(5, 10)
         2 + 4*5 + 2*5^3 + 5^4 + 3*5^5 + 2*5^6 + 5^8 + 3*5^9 + O(5^10)

    ::

        sage: X5 = EllipticCurve([-1*(5**4), 1/4*(5**6)])
        sage: X5.j_invariant(), X5.discriminant() / 5**12
         (110592/37, 37)
        sage: 5**(-2) * X5.padic_E2(5, 10)
         2 + 4*5 + 2*5^3 + 5^4 + 3*5^5 + 2*5^6 + 5^8 + 3*5^9 + O(5^10)

    ::

        sage: X6 = EllipticCurve([-1/(5**4), 1/4/(5**6)])
        sage: X6.j_invariant(), X6.discriminant() * 5**12
         (110592/37, 37)
        sage: 5**2 * X6.padic_E2(5, 10)
         2 + 4*5 + 2*5^3 + 5^4 + 3*5^5 + 2*5^6 + 5^8 + 3*5^9 + O(5^10)

    Test check=True vs check=False::

        sage: EllipticCurve([-1, 1/4]).padic_E2(5, 1, check=False)
        2 + O(5)
        sage: EllipticCurve([-1, 1/4]).padic_E2(5, 1, check=True)
        2 + O(5)
        sage: EllipticCurve([-1, 1/4]).padic_E2(5, 30, check=False)
        2 + 4*5 + 2*5^3 + 5^4 + 3*5^5 + 2*5^6 + 5^8 + 3*5^9 + 4*5^10 + 2*5^11 + 2*5^12 + 2*5^14 + 3*5^15 + 3*5^16 + 3*5^17 + 4*5^18 + 2*5^19 + 4*5^20 + 5^21 + 4*5^22 + 2*5^23 + 3*5^24 + 3*5^26 + 2*5^27 + 3*5^28 + O(5^30)
        sage: EllipticCurve([-1, 1/4]).padic_E2(5, 30, check=True)
        2 + 4*5 + 2*5^3 + 5^4 + 3*5^5 + 2*5^6 + 5^8 + 3*5^9 + 4*5^10 + 2*5^11 + 2*5^12 + 2*5^14 + 3*5^15 + 3*5^16 + 3*5^17 + 4*5^18 + 2*5^19 + 4*5^20 + 5^21 + 4*5^22 + 2*5^23 + 3*5^24 + 3*5^26 + 2*5^27 + 3*5^28 + O(5^30)

    Here\'s one using the `p^{1/2}` algorithm::

        sage: EllipticCurve([-1, 1/4]).padic_E2(3001, 3, algorithm=\'sqrtp\')
        1907 + 2819*3001 + 1124*3001^2 + O(3001^3)
    '''
def matrix_of_frobenius(self, p, prec: int = 20, check: bool = False, check_hypotheses: bool = True, algorithm: str = 'auto'):
    """
    Return the matrix of Frobenius on the Monsky Washnitzer cohomology of
    the short Weierstrass model of the minimal model of the elliptic curve.

    INPUT:

    - ``p`` -- prime (>= 3) for which `E` is good and ordinary

    - ``prec`` -- (relative) `p`-adic precision for result (default: 20)

    - ``check`` -- boolean (default: ``False``); whether to perform a
      consistency check. This will slow down the computation by a
      constant factor 2. (The consistency check is to verify
      that its trace is correct to the specified precision. Otherwise,
      the trace is used to compute one column from the other one
      (possibly after a change of basis).)

    - ``check_hypotheses`` -- boolean; whether to check that this is a curve
      for which the `p`-adic sigma function makes sense

    - ``algorithm`` -- one of ``'standard'``, ``'sqrtp'``, or
      ``'auto'``. This selects which version of Kedlaya's algorithm is used.
      The ``'standard'`` one is the one described in Kedlaya's paper. The
      ``'sqrtp'`` one has better performance for large `p`, but only
      works when `p > 6N` (`N=` prec). The ``'auto'`` option
      selects ``'sqrtp'`` whenever possible.

      Note that if the ``'sqrtp'`` algorithm is used, a consistency check
      will automatically be applied, regardless of the setting of the
      ``check`` flag.

    OUTPUT: a matrix of `p`-adic number to precision ``prec``

    See also the documentation of padic_E2.

    EXAMPLES::

        sage: E = EllipticCurve('37a1')
        sage: E.matrix_of_frobenius(7)
        [             2*7 + 4*7^2 + 5*7^4 + 6*7^5 + 6*7^6 + 7^8 + 4*7^9 + 3*7^10 + 2*7^11 + 5*7^12 + 4*7^14 + 7^16 + 2*7^17 + 3*7^18 + 4*7^19 + 3*7^20 + O(7^21)                                   2 + 3*7 + 6*7^2 + 7^3 + 3*7^4 + 5*7^5 + 3*7^7 + 7^8 + 3*7^9 + 6*7^13 + 7^14 + 7^16 + 5*7^17 + 4*7^18 + 7^19 + O(7^20)]
        [    2*7 + 3*7^2 + 7^3 + 3*7^4 + 6*7^5 + 2*7^6 + 3*7^7 + 5*7^8 + 3*7^9 + 2*7^11 + 6*7^12 + 5*7^13 + 4*7^16 + 4*7^17 + 6*7^18 + 6*7^19 + 4*7^20 + O(7^21) 6 + 4*7 + 2*7^2 + 6*7^3 + 7^4 + 6*7^7 + 5*7^8 + 2*7^9 + 3*7^10 + 4*7^11 + 7^12 + 6*7^13 + 2*7^14 + 6*7^15 + 5*7^16 + 4*7^17 + 3*7^18 + 2*7^19 + O(7^20)]
        sage: M = E.matrix_of_frobenius(11,prec=3); M
        [   9*11 + 9*11^3 + O(11^4)          10 + 11 + O(11^3)]
        [     2*11 + 11^2 + O(11^4) 6 + 11 + 10*11^2 + O(11^3)]
        sage: M.det()
        11 + O(11^4)
        sage: M.trace()
        6 + 10*11 + 10*11^2 + O(11^3)
        sage: E.ap(11)
        -5
        sage: E = EllipticCurve('83a1')
        sage: E.matrix_of_frobenius(3,6)
        [                      2*3 + 3^5 + O(3^6)             2*3 + 2*3^2 + 2*3^3 + O(3^6)]
        [              2*3 + 3^2 + 2*3^5 + O(3^6) 2 + 2*3^2 + 2*3^3 + 2*3^4 + 3^5 + O(3^6)]
    """
