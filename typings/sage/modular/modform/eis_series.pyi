from sage.arith.functions import lcm as lcm
from sage.arith.misc import bernoulli as bernoulli, divisors as divisors, is_squarefree as is_squarefree
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.timing import cputime as cputime
from sage.modular.arithgroup.congroup_gammaH import GammaH_class as GammaH_class
from sage.modular.dirichlet import DirichletGroup as DirichletGroup
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.power_series_ring import PowerSeriesRing as PowerSeriesRing
from sage.rings.rational_field import QQ as QQ

def eisenstein_series_qexp(k, prec: int = 10, K=..., var: str = 'q', normalization: str = 'linear'):
    """
    Return the `q`-expansion of the normalized weight `k` Eisenstein series on
    `\\SL_2(\\ZZ)` to precision ``prec`` in the ring `K`. Three normalizations
    are available, depending on the parameter ``normalization``; the default
    normalization is the one for which the linear coefficient is 1.

    INPUT:

    - ``k`` -- an even positive integer

    - ``prec`` -- (default: 10) a nonnegative integer

    - ``K`` -- (default: `\\QQ`) a ring

    - ``var`` -- (default: ``'q'``) variable name to use for `q`-expansion

    - ``normalization`` -- (default: ``'linear'``) normalization to use. If this
      is ``'linear'``, then the series will be normalized so that the linear
      term is 1. If it is ``'constant'``, the series will be normalized to have
      constant term 1. If it is ``'integral'``, then the series will be
      normalized to have integer coefficients and no common factor, and linear
      term that is positive. Note that ``'integral'`` will work over arbitrary
      base rings, while ``'linear'`` or ``'constant'`` will fail if the
      denominator (resp. numerator) of `B_k / 2k` is invertible.

    ALGORITHM:

        We know `E_k = \\text{constant} + \\sum_n \\sigma_{k-1}(n) q^n`. So we
        compute all the `\\sigma_{k-1}(n)` simultaneously, using the fact that
        `\\sigma` is multiplicative.

    EXAMPLES::

        sage: eisenstein_series_qexp(2,5)
        -1/24 + q + 3*q^2 + 4*q^3 + 7*q^4 + O(q^5)
        sage: eisenstein_series_qexp(2,0)
        O(q^0)
        sage: eisenstein_series_qexp(2,5,GF(7))
        2 + q + 3*q^2 + 4*q^3 + O(q^5)
        sage: eisenstein_series_qexp(2,5,GF(7),var='T')
        2 + T + 3*T^2 + 4*T^3 + O(T^5)

    We illustrate the use of the ``normalization`` parameter::

        sage: eisenstein_series_qexp(12, 5, normalization='integral')
        691 + 65520*q + 134250480*q^2 + 11606736960*q^3 + 274945048560*q^4 + O(q^5)
        sage: eisenstein_series_qexp(12, 5, normalization='constant')
        1 + 65520/691*q + 134250480/691*q^2 + 11606736960/691*q^3 + 274945048560/691*q^4 + O(q^5)
        sage: eisenstein_series_qexp(12, 5, normalization='linear')
        691/65520 + q + 2049*q^2 + 177148*q^3 + 4196353*q^4 + O(q^5)
        sage: eisenstein_series_qexp(12, 50, K=GF(13), normalization='constant')
        1 + O(q^50)

    TESTS:

    Test that :issue:`5102` is fixed::

        sage: eisenstein_series_qexp(10, 30, GF(17))
        15 + q + 3*q^2 + 15*q^3 + 7*q^4 + 13*q^5 + 11*q^6 + 11*q^7 + 15*q^8 + 7*q^9 + 5*q^10 + 7*q^11 + 3*q^12 + 14*q^13 + 16*q^14 + 8*q^15 + 14*q^16 + q^17 + 4*q^18 + 3*q^19 + 6*q^20 + 12*q^21 + 4*q^22 + 12*q^23 + 4*q^24 + 4*q^25 + 8*q^26 + 14*q^27 + 9*q^28 + 6*q^29 + O(q^30)

    This shows that the bug reported at :issue:`8291` is fixed::

        sage: eisenstein_series_qexp(26, 10, GF(13))
        7 + q + 3*q^2 + 4*q^3 + 7*q^4 + 6*q^5 + 12*q^6 + 8*q^7 + 2*q^8 + O(q^10)

    We check that the function behaves properly over finite-characteristic base rings::

        sage: eisenstein_series_qexp(12, 5, K = Zmod(691), normalization='integral')
        566*q + 236*q^2 + 286*q^3 + 194*q^4 + O(q^5)
        sage: eisenstein_series_qexp(12, 5, K = Zmod(691), normalization='constant')
        Traceback (most recent call last):
        ...
        ValueError: The numerator of -B_k/(2*k) (=691) must be invertible in the ring Ring of integers modulo 691
        sage: eisenstein_series_qexp(12, 5, K = Zmod(691), normalization='linear')
        q + 667*q^2 + 252*q^3 + 601*q^4 + O(q^5)

        sage: eisenstein_series_qexp(12, 5, K = Zmod(2), normalization='integral')
        1 + O(q^5)
        sage: eisenstein_series_qexp(12, 5, K = Zmod(2), normalization='constant')
        1 + O(q^5)
        sage: eisenstein_series_qexp(12, 5, K = Zmod(2), normalization='linear')
        Traceback (most recent call last):
        ...
        ValueError: The denominator of -B_k/(2*k) (=65520) must be invertible in the ring Ring of integers modulo 2

    AUTHORS:

    - William Stein: original implementation

    - Craig Citro (2007-06-01): rewrote for massive speedup

    - Martin Raum (2009-08-02): port to cython for speedup

    - David Loeffler (2010-04-07): work around an integer overflow when `k` is large

    - David Loeffler (2012-03-15): add options for alternative normalizations
      (motivated by :issue:`12043`)
    """
def eisenstein_series_lseries(weight, prec: int = 53, max_imaginary_part: int = 0, max_asymp_coeffs: int = 40):
    """
    Return the `L`-series of the weight `2k` Eisenstein series `E_{2k}`
    on `\\SL_2(\\ZZ)`.

    This actually returns an interface to Tim Dokchitser's program
    for computing with the `L`-series of the Eisenstein series.
    See :class:`~sage.lfunctions.dokchitser.Dokchitser`.

    INPUT:

    - ``weight`` -- even integer

    - ``prec`` -- integer (bits precision)

    - ``max_imaginary_part`` -- real number

    - ``max_asymp_coeffs`` -- integer

    OUTPUT: the `L`-series of the Eisenstein series. This can be
    evaluated at argument `s`, or have
    :meth:`~sage.lfunctions.dokchitser.Dokchitser.derivative` called, etc.

    EXAMPLES:

    We compute with the `L`-series of `E_{16}` and then `E_{20}`::

        sage: L = eisenstein_series_lseries(16)
        sage: L(1)
        -0.291657724743874
        sage: L.derivative(1)
        0.0756072194360656
        sage: L = eisenstein_series_lseries(20)
        sage: L(2)
        -5.02355351645998

    Now with higher precision::

        sage: L = eisenstein_series_lseries(20, prec=200)
        sage: L(2)
        -5.0235535164599797471968418348135050804419155747868718371029
    """
def compute_eisenstein_params(character, k):
    """
    Compute and return a list of all parameters `(\\chi,\\psi,t)` that
    define the Eisenstein series with given character and weight `k`.

    Only the parity of `k` is relevant (unless k = 1, which is a slightly different case).

    If ``character`` is an integer `N`, then the parameters for
    `\\Gamma_1(N)` are computed instead.  Then the condition is that
    `\\chi(-1)*\\psi(-1) =(-1)^k`.

    If ``character`` is a list of integers, the parameters for `\\Gamma_H(N)` are
    computed, where `H` is the subgroup of `(\\ZZ/N\\ZZ)^\\times` generated by the
    integers in the given list.

    EXAMPLES::

        sage: sage.modular.modform.eis_series.compute_eisenstein_params(DirichletGroup(30)(1), 3)
        []

        sage: pars =  sage.modular.modform.eis_series.compute_eisenstein_params(DirichletGroup(30)(1), 4)
        sage: [(x[0].values_on_gens(), x[1].values_on_gens(), x[2]) for x in pars]
        [((1, 1), (1, 1), 1),
        ((1, 1), (1, 1), 2),
        ((1, 1), (1, 1), 3),
        ((1, 1), (1, 1), 5),
        ((1, 1), (1, 1), 6),
        ((1, 1), (1, 1), 10),
        ((1, 1), (1, 1), 15),
        ((1, 1), (1, 1), 30)]

        sage: pars = sage.modular.modform.eis_series.compute_eisenstein_params(15, 1)
        sage: [(x[0].values_on_gens(), x[1].values_on_gens(), x[2]) for x in pars]
        [((1, 1), (-1, 1), 1),
        ((1, 1), (-1, 1), 5),
        ((1, 1), (1, zeta4), 1),
        ((1, 1), (1, zeta4), 3),
        ((1, 1), (-1, -1), 1),
        ((1, 1), (1, -zeta4), 1),
        ((1, 1), (1, -zeta4), 3),
        ((-1, 1), (1, -1), 1)]

        sage: sage.modular.modform.eis_series.compute_eisenstein_params(DirichletGroup(15).0, 1)
        [(Dirichlet character modulo 15 of conductor 1 mapping 11 |--> 1, 7 |--> 1, Dirichlet character modulo 15 of conductor 3 mapping 11 |--> -1, 7 |--> 1, 1),
        (Dirichlet character modulo 15 of conductor 1 mapping 11 |--> 1, 7 |--> 1, Dirichlet character modulo 15 of conductor 3 mapping 11 |--> -1, 7 |--> 1, 5)]

        sage: len(sage.modular.modform.eis_series.compute_eisenstein_params(GammaH(15, [4]), 3))
        8
    """
