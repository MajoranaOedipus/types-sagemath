from _typeshed import Incomplete
from collections.abc import Generator
from sage.arith.misc import divisors as divisors, euler_phi as euler_phi, gauss_sum as gauss_sum, gcd as gcd, is_prime as is_prime, kronecker_symbol as kronecker_symbol, moebius as moebius
from sage.combinat.integer_vector_weighted import WeightedIntegerVectors as WeightedIntegerVectors
from sage.functions.generalized import sgn as sgn
from sage.functions.log import log as log
from sage.functions.other import ceil as ceil, floor as floor, frac as frac
from sage.geometry.lattice_polytope import LatticePolytope as LatticePolytope
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.functional import cyclotomic_polynomial as cyclotomic_polynomial
from sage.misc.misc_c import prod as prod
from sage.modular.hypergeometric_misc import hgm_coeffs as hgm_coeffs
from sage.modules.free_module_element import vector as vector
from sage.rings.finite_rings.finite_field_constructor import GF as GF
from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as IntegerModRing
from sage.rings.fraction_field import FractionField as FractionField
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.padics.factory import Zp as Zp
from sage.rings.padics.padic_generic_element import gauss_table as gauss_table
from sage.rings.polynomial.polynomial_ring import polygen as polygen, polygens as polygens
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.power_series_ring import PowerSeriesRing as PowerSeriesRing
from sage.rings.rational_field import QQ as QQ
from sage.rings.universal_cyclotomic_field import UniversalCyclotomicField as UniversalCyclotomicField
from sage.schemes.generic.spec import Spec as Spec

def characteristic_polynomial_from_traces(traces, d, q, i, sign, deg=None, use_fe: bool = True):
    """
    Given a sequence of traces `t_1, \\dots, t_k`, return the
    corresponding characteristic polynomial with Weil numbers as roots.

    The characteristic polynomial is defined by the generating series

    .. MATH::

        P(T) = \\exp\\left(- \\sum_{k\\geq 1} t_k \\frac{T^k}{k}\\right)

    and should have the property that reciprocals of all roots have
    absolute value `q^{i/2}`.

    INPUT:

    - ``traces`` -- list of integers `t_1, \\dots, t_k`

    - ``d`` -- the degree of the characteristic polynomial

    - ``q`` -- power of a prime number

    - ``i`` -- integer; the weight in the motivic sense

    - ``sign`` -- integer; the sign

    - ``deg`` -- integer or ``None``

    - ``use_fe`` -- boolean (default: ``True``)

    OUTPUT: a polynomial

    If ``deg`` is specified, only the coefficients up to this degree (inclusive) are computed.

    If ``use_fe`` is ``False``, we ignore the local functional equation.

    EXAMPLES::

        sage: from sage.modular.hypergeometric_motive import characteristic_polynomial_from_traces
        sage: characteristic_polynomial_from_traces([1, 1], 1, 3, 0, -1)
        -T + 1
        sage: characteristic_polynomial_from_traces([25], 1, 5, 4, -1)
        -25*T + 1

        sage: characteristic_polynomial_from_traces([3], 2, 5, 1, 1)
        5*T^2 - 3*T + 1
        sage: characteristic_polynomial_from_traces([1], 2, 7, 1, 1)
        7*T^2 - T + 1

        sage: characteristic_polynomial_from_traces([20], 3, 29, 2, 1)
        24389*T^3 - 580*T^2 - 20*T + 1
        sage: characteristic_polynomial_from_traces([12], 3, 13, 2, -1)
        -2197*T^3 + 156*T^2 - 12*T + 1

        sage: characteristic_polynomial_from_traces([36, 7620], 4, 17, 3, 1)
        24137569*T^4 - 176868*T^3 - 3162*T^2 - 36*T + 1
        sage: characteristic_polynomial_from_traces([-4, 276], 4, 5, 3, 1)
        15625*T^4 + 500*T^3 - 130*T^2 + 4*T + 1
        sage: characteristic_polynomial_from_traces([4, -276], 4, 5, 3, 1)
        15625*T^4 - 500*T^3 + 146*T^2 - 4*T + 1
        sage: characteristic_polynomial_from_traces([22, 484], 4, 31, 2, -1)
        -923521*T^4 + 21142*T^3 - 22*T + 1

        sage: characteristic_polynomial_from_traces([22], 4, 31, 2, -1, deg=1)
        -22*T + 1
        sage: characteristic_polynomial_from_traces([22, 484], 4, 31, 2, -1, deg=4)
        -923521*T^4 + 21142*T^3 - 22*T + 1

    TESTS::

        sage: characteristic_polynomial_from_traces([-36], 4, 17, 3, 1)
        Traceback (most recent call last):
        ...
        ValueError: not enough traces were given
    """
def enumerate_hypergeometric_data(d, weight=None) -> Generator[Incomplete, None, Incomplete]:
    """
    Return an iterator over parameters of hypergeometric motives (up to swapping).

    INPUT:

    - ``d`` -- the degree

    - ``weight`` -- (optional) integer; specifies the motivic weight

    EXAMPLES::

        sage: from sage.modular.hypergeometric_motive import enumerate_hypergeometric_data as enum
        sage: l = [H for H in enum(6, weight=2) if H.hodge_numbers()[0] == 1]
        sage: len(l)
        112
    """
def possible_hypergeometric_data(d, weight=None) -> list:
    """
    Return the list of possible parameters of hypergeometric motives (up to swapping).

    INPUT:

    - ``d`` -- the degree

    - ``weight`` -- (optional) integer; specifies the motivic weight

    EXAMPLES::

        sage: from sage.modular.hypergeometric_motive import possible_hypergeometric_data as P
        sage: [len(P(i,weight=2)) for i in range(1, 7)]
        [0, 0, 10, 30, 93, 234]
    """
def cyclotomic_to_alpha(cyclo) -> list:
    """
    Convert a list of indices of cyclotomic polynomials
    to a list of rational numbers.

    The input represents a product of cyclotomic polynomials.

    The output is the list of arguments of the roots of the
    given product of cyclotomic polynomials.

    This is the inverse of :func:`alpha_to_cyclotomic`.

    EXAMPLES::

        sage: from sage.modular.hypergeometric_motive import cyclotomic_to_alpha
        sage: cyclotomic_to_alpha([1])
        [0]
        sage: cyclotomic_to_alpha([2])
        [1/2]
        sage: cyclotomic_to_alpha([5])
        [1/5, 2/5, 3/5, 4/5]
        sage: cyclotomic_to_alpha([1, 2, 3, 6])
        [0, 1/6, 1/3, 1/2, 2/3, 5/6]
        sage: cyclotomic_to_alpha([2, 3])
        [1/3, 1/2, 2/3]
    """
def alpha_to_cyclotomic(alpha) -> list:
    """
    Convert from a list of rationals arguments to a list of integers.

    The input represents arguments of some roots of unity.

    The output represent a product of cyclotomic polynomials with exactly
    the given roots. Note that the multiplicity of `r/s` in the list
    must be independent of `r`; otherwise, a :exc:`ValueError` will be raised.

    This is the inverse of :func:`cyclotomic_to_alpha`.

    EXAMPLES::

        sage: from sage.modular.hypergeometric_motive import alpha_to_cyclotomic
        sage: alpha_to_cyclotomic([0])
        [1]
        sage: alpha_to_cyclotomic([1/2])
        [2]
        sage: alpha_to_cyclotomic([1/5, 2/5, 3/5, 4/5])
        [5]
        sage: alpha_to_cyclotomic([0, 1/6, 1/3, 1/2, 2/3, 5/6])
        [1, 2, 3, 6]
        sage: alpha_to_cyclotomic([1/3, 2/3, 1/2])
        [2, 3]
    """
def capital_M(n):
    """
    Auxiliary function, used to describe the canonical scheme.

    INPUT:

    - ``n`` -- integer

    OUTPUT: a rational

    EXAMPLES::

        sage: from sage.modular.hypergeometric_motive import capital_M
        sage: [capital_M(i) for i in range(1, 8)]
        [1, 4, 27, 64, 3125, 432, 823543]
    """
def cyclotomic_to_gamma(cyclo_up, cyclo_down) -> dict:
    """
    Convert a quotient of products of cyclotomic polynomials
    to a quotient of products of polynomials `x^n - 1`.

    INPUT:

    - ``cyclo_up`` -- list of indices of cyclotomic polynomials in the numerator
    - ``cyclo_down`` -- list of indices of cyclotomic polynomials in the denominator

    OUTPUT:

    a dictionary mapping an integer `n` to the power of `x^n - 1` that
    appears in the given product

    EXAMPLES::

        sage: from sage.modular.hypergeometric_motive import cyclotomic_to_gamma
        sage: cyclotomic_to_gamma([6], [1])
        {2: -1, 3: -1, 6: 1}
    """
def gamma_list_to_cyclotomic(galist):
    """
    Convert a quotient of products of polynomials `x^n - 1`
    to a quotient of products of cyclotomic polynomials.

    INPUT:

    - ``galist`` -- list of integers, where an integer `n` represents
      the power `(x^{|n|} - 1)^{\\operatorname{sgn}(n)}`

    OUTPUT:

    a pair of list of integers, where `k` represents the cyclotomic
    polynomial `\\Phi_k`

    EXAMPLES::

        sage: from sage.modular.hypergeometric_motive import gamma_list_to_cyclotomic
        sage: gamma_list_to_cyclotomic([-1, -1, 2])
        ([2], [1])

        sage: gamma_list_to_cyclotomic([-1, -1, -1, -3, 6])
        ([2, 6], [1, 1, 1])

        sage: gamma_list_to_cyclotomic([-1, 2, 3, -4])
        ([3], [4])

        sage: gamma_list_to_cyclotomic([8, 2, 2, 2, -6, -4, -3, -1])
        ([2, 2, 8], [3, 3, 6])
    """

class HypergeometricData:
    def __init__(self, cyclotomic=None, alpha_beta=None, gamma_list=None) -> None:
        """
        Creation of hypergeometric motives.

        INPUT:

        Three possibilities are offered, each describing a quotient
        of products of cyclotomic polynomials.

        - ``cyclotomic`` -- a pair of lists of nonnegative integers,
          each integer `k` represents a cyclotomic polynomial `\\Phi_k`

        - ``alpha_beta`` -- a pair of lists of rationals,
          each rational represents a root of unity

        - ``gamma_list`` -- a pair of lists of nonnegative integers,
          each integer `n` represents a polynomial `x^n - 1`

        In the last case, it is also allowed to send just one list of signed
        integers where signs indicate to which part the integer belongs to.

        EXAMPLES::

            sage: from sage.modular.hypergeometric_motive import HypergeometricData as Hyp
            sage: Hyp(cyclotomic=([2], [1]))
            Hypergeometric data for [1/2] and [0]

            sage: Hyp(alpha_beta=([1/2], [0]))
            Hypergeometric data for [1/2] and [0]
            sage: Hyp(alpha_beta=([1/5,2/5,3/5,4/5], [0,0,0,0]))
            Hypergeometric data for [1/5, 2/5, 3/5, 4/5] and [0, 0, 0, 0]

            sage: Hyp(gamma_list=([5], [1,1,1,1,1]))
            Hypergeometric data for [1/5, 2/5, 3/5, 4/5] and [0, 0, 0, 0]
            sage: Hyp(gamma_list=([5,-1,-1,-1,-1,-1]))
            Hypergeometric data for [1/5, 2/5, 3/5, 4/5] and [0, 0, 0, 0]
        """
    def __eq__(self, other) -> bool:
        """
        Return whether two data are equal.

        EXAMPLES::

            sage: from sage.modular.hypergeometric_motive import HypergeometricData as Hyp
            sage: H1 = Hyp(alpha_beta=([1/2], [0]))
            sage: H2 = Hyp(cyclotomic=([6,2], [1,1,1]))
            sage: H1 == H1
            True
            sage: H1 == H2
            False
        """
    def __ne__(self, other) -> bool:
        """
        Return whether two data are unequal.

        EXAMPLES::

            sage: from sage.modular.hypergeometric_motive import HypergeometricData as Hyp
            sage: H1 = Hyp(alpha_beta=([1/2], [0]))
            sage: H2 = Hyp(cyclotomic=([6,2], [1,1,1]))
            sage: H1 != H1
            False
            sage: H1 != H2
            True
        """
    def __hash__(self):
        """
        Return a hash for ``self``.

        EXAMPLES::

            sage: from sage.modular.hypergeometric_motive import HypergeometricData as Hyp
            sage: H1 = Hyp(alpha_beta=([1/2], [0]))
            sage: h = hash(H1)
        """
    def cyclotomic_data(self) -> tuple:
        """
        Return the pair of tuples of indices of cyclotomic polynomials.

        EXAMPLES::

            sage: from sage.modular.hypergeometric_motive import HypergeometricData as Hyp
            sage: Hyp(alpha_beta=([1/2], [0])).cyclotomic_data()
            ([2], [1])
        """
    def alpha_beta(self) -> tuple:
        """
        Return the pair of lists of rational arguments.

        EXAMPLES::

            sage: from sage.modular.hypergeometric_motive import HypergeometricData as Hyp
            sage: Hyp(alpha_beta=([1/2], [0])).alpha_beta()
            ([1/2], [0])
        """
    def alpha(self) -> list:
        """
        Return the first tuple of rational arguments.

        EXAMPLES::

            sage: from sage.modular.hypergeometric_motive import HypergeometricData as Hyp
            sage: Hyp(alpha_beta=([1/2], [0])).alpha()
            [1/2]
        """
    def beta(self) -> list:
        """
        Return the second tuple of rational arguments.

        EXAMPLES::

            sage: from sage.modular.hypergeometric_motive import HypergeometricData as Hyp
            sage: Hyp(alpha_beta=([1/2], [0])).beta()
            [0]
        """
    def defining_polynomials(self) -> tuple:
        """
        Return the pair of products of cyclotomic polynomials.

        EXAMPLES::

            sage: from sage.modular.hypergeometric_motive import HypergeometricData as Hyp
            sage: Hyp(alpha_beta=([1/4,3/4], [0,0])).defining_polynomials()
            (x^2 + 1, x^2 - 2*x + 1)
        """
    def gamma_array(self) -> dict:
        """
        Return the dictionary `\\{v: \\gamma_v\\}` for the expression

        .. MATH::

            \\prod_v (T^v - 1)^{\\gamma_v}

        EXAMPLES::

            sage: from sage.modular.hypergeometric_motive import HypergeometricData as Hyp
            sage: Hyp(alpha_beta=([1/2], [0])).gamma_array()
            {1: -2, 2: 1}
            sage: Hyp(cyclotomic=([6,2], [1,1,1])).gamma_array()
            {1: -3, 3: -1, 6: 1}
        """
    def gamma_list(self) -> list:
        """
        Return a list of integers describing the `x^n - 1` factors.

        Each integer `n` stands for `(x^{|n|} - 1)^{\\operatorname{sgn}(n)}`.

        EXAMPLES::

            sage: from sage.modular.hypergeometric_motive import HypergeometricData as Hyp
            sage: Hyp(alpha_beta=([1/2], [0])).gamma_list()
            [-1, -1, 2]

            sage: Hyp(cyclotomic=([6,2], [1,1,1])).gamma_list()
            [-1, -1, -1, -3, 6]

            sage: Hyp(cyclotomic=([3], [4])).gamma_list()
            [-1, 2, 3, -4]
        """
    def wild_primes(self) -> list:
        """
        Return the wild primes.

        EXAMPLES::

            sage: from sage.modular.hypergeometric_motive import HypergeometricData as Hyp
            sage: Hyp(cyclotomic=([3], [4])).wild_primes()
            [2, 3]
            sage: Hyp(cyclotomic=([2,2,2,2,3,3,3,6,6], [1,1,4,5,9])).wild_primes()
            [2, 3, 5]
        """
    def zigzag(self, x, flip_beta: bool = False):
        """
        Count ``alpha``'s at most ``x`` minus ``beta``'s at most ``x``.

        This function is used to compute the weight and the Hodge numbers.
        With ``flip_beta`` set to ``True``, replace each `b` in `\\beta`
        with `1-b`.

        .. SEEALSO::

            :meth:`weight`, :meth:`hodge_numbers`

        EXAMPLES::

            sage: from sage.modular.hypergeometric_motive import HypergeometricData as Hyp
            sage: H = Hyp(alpha_beta=([1/6,1/3,2/3,5/6], [1/8,3/8,5/8,7/8]))
            sage: [H.zigzag(x) for x in [0, 1/3, 1/2]]
            [0, 1, 0]
            sage: H = Hyp(cyclotomic=([5], [1,1,1,1]))
            sage: [H.zigzag(x) for x in [0,1/6,1/4,1/2,3/4,5/6]]
            [-4, -4, -3, -2, -1, 0]
        """
    def weight(self):
        """
        Return the motivic weight of this motivic data.

        EXAMPLES:

        With rational inputs::

            sage: from sage.modular.hypergeometric_motive import HypergeometricData as Hyp
            sage: Hyp(alpha_beta=([1/2], [0])).weight()
            0
            sage: Hyp(alpha_beta=([1/4,3/4], [0,0])).weight()
            1
            sage: Hyp(alpha_beta=([1/6,1/3,2/3,5/6], [0,0,1/4,3/4])).weight()
            1
            sage: H = Hyp(alpha_beta=([1/6,1/3,2/3,5/6], [1/8,3/8,5/8,7/8]))
            sage: H.weight()
            1

        With cyclotomic inputs::

            sage: Hyp(cyclotomic=([6,2], [1,1,1])).weight()
            2
            sage: Hyp(cyclotomic=([6], [1,2])).weight()
            0
            sage: Hyp(cyclotomic=([8], [1,2,3])).weight()
            0
            sage: Hyp(cyclotomic=([5], [1,1,1,1])).weight()
            3
            sage: Hyp(cyclotomic=([5,6], [1,1,2,2,3])).weight()
            1
            sage: Hyp(cyclotomic=([3,8], [1,1,1,2,6])).weight()
            2
            sage: Hyp(cyclotomic=([3,3], [2,2,4])).weight()
            1

        With gamma list input::

            sage: Hyp(gamma_list=([8,2,2,2], [6,4,3,1])).weight()
            3
        """
    def degree(self):
        """
        Return the degree.

        This is the sum of the Hodge numbers.

        .. SEEALSO::

            :meth:`hodge_numbers`

        EXAMPLES::

            sage: from sage.modular.hypergeometric_motive import HypergeometricData as Hyp
            sage: Hyp(alpha_beta=([1/2], [0])).degree()
            1
            sage: Hyp(gamma_list=([2,2,4], [8])).degree()
            4
            sage: Hyp(cyclotomic=([5,6], [1,1,2,2,3])).degree()
            6
            sage: Hyp(cyclotomic=([3,8], [1,1,1,2,6])).degree()
            6
            sage: Hyp(cyclotomic=([3,3], [2,2,4])).degree()
            4
        """
    def hodge_numbers(self) -> list:
        """
        Return the Hodge numbers.

        .. SEEALSO::

            :meth:`degree`, :meth:`hodge_polynomial`, :meth:`hodge_polygon`

        EXAMPLES::

            sage: from sage.modular.hypergeometric_motive import HypergeometricData as Hyp
            sage: H = Hyp(cyclotomic=([3], [6]))
            sage: H.hodge_numbers()
            [1, 1]

            sage: H = Hyp(cyclotomic=([4], [1,2]))
            sage: H.hodge_numbers()
            [2]

            sage: H = Hyp(gamma_list=([8,2,2,2], [6,4,3,1]))
            sage: H.hodge_numbers()
            [1, 2, 2, 1]

            sage: H = Hyp(gamma_list=([5], [1,1,1,1,1]))
            sage: H.hodge_numbers()
            [1, 1, 1, 1]

            sage: H = Hyp(gamma_list=[6,1,-4,-3])
            sage: H.hodge_numbers()
            [1, 1]

            sage: H = Hyp(gamma_list=[-3]*4 + [1]*12)
            sage: H.hodge_numbers()
            [1, 1, 1, 1, 1, 1, 1, 1]

        REFERENCES:

        - [Fedorov2015]_
        """
    def hodge_polynomial(self):
        """
        Return the Hodge polynomial.

        .. SEEALSO::

            :meth:`hodge_numbers`, :meth:`hodge_polygon_vertices`, :meth:`hodge_function`

        EXAMPLES::

            sage: from sage.modular.hypergeometric_motive import HypergeometricData as Hyp
            sage: H = Hyp(cyclotomic=([6,10], [3,12]))
            sage: H.hodge_polynomial()
            (T^3 + 2*T^2 + 2*T + 1)/T^2
            sage: H = Hyp(cyclotomic=([2,2,2,2,3,3,3,6,6], [1,1,4,5,9]))
            sage: H.hodge_polynomial()
            (T^5 + 3*T^4 + 3*T^3 + 3*T^2 + 3*T + 1)/T^2
        """
    def hodge_function(self, x):
        """
        Evaluate the Hodge polygon as a function.

        .. SEEALSO::

            :meth:`hodge_numbers`, :meth:`hodge_polynomial`, :meth:`hodge_polygon_vertices`

        EXAMPLES::

            sage: from sage.modular.hypergeometric_motive import HypergeometricData as Hyp
            sage: H = Hyp(cyclotomic=([6,10], [3,12]))
            sage: H.hodge_function(3)
            2
            sage: H.hodge_function(4)
            4
        """
    def hodge_polygon_vertices(self) -> list:
        """
        Return the vertices of the Hodge polygon.

        .. SEEALSO::

            :meth:`hodge_numbers`, :meth:`hodge_polynomial`, :meth:`hodge_function`

        EXAMPLES::

            sage: from sage.modular.hypergeometric_motive import HypergeometricData as Hyp
            sage: H = Hyp(cyclotomic=([6,10], [3,12]))
            sage: H.hodge_polygon_vertices()
            [(0, 0), (1, 0), (3, 2), (5, 6), (6, 9)]
            sage: H = Hyp(cyclotomic=([2,2,2,2,3,3,3,6,6], [1,1,4,5,9]))
            sage: H.hodge_polygon_vertices()
            [(0, 0), (1, 0), (4, 3), (7, 9), (10, 18), (13, 30), (14, 35)]
        """
    def E_polynomial(self, vars=None):
        """
        Return the E-polynomial of ``self``.

        This is a bivariate polynomial.

        The algorithm is taken from [FRV2019]_.

        INPUT:

        - ``vars`` -- (optional) pair of variables (default: `u,v`)

        REFERENCES:

        .. [FRV2019] Fernando Rodriguez Villegas, *Mixed Hodge numbers
           and factorial ratios*, :arxiv:`1907.02722`

        EXAMPLES::

            sage: from sage.modular.hypergeometric_motive import HypergeometricData
            sage: H = HypergeometricData(gamma_list=[-30, -1, 6, 10, 15])
            sage: H.E_polynomial()
            8*u*v + 7*u + 7*v + 8

            sage: p, q = polygens(QQ,'p,q')
            sage: H.E_polynomial((p, q))
            8*p*q + 7*p + 7*q + 8

            sage: H = HypergeometricData(gamma_list=(-11, -2, 1, 3, 4, 5))
            sage: H.E_polynomial()
            5*u^2*v + 5*u*v^2 + u*v + 1

            sage: H = HypergeometricData(gamma_list=(-63, -8, -2, 1, 4, 16, 21, 31))
            sage: H.E_polynomial()
            21*u^3*v^2 + 21*u^2*v^3 + u^3*v + 23*u^2*v^2 + u*v^3 + u^2*v + u*v^2 + 2*u*v + 1
        """
    def M_value(self):
        """
        Return the `M` coefficient that appears in the trace formula.

        OUTPUT: a rational

        .. SEEALSO:: :meth:`canonical_scheme`

        EXAMPLES::

            sage: from sage.modular.hypergeometric_motive import HypergeometricData as Hyp
            sage: H = Hyp(alpha_beta=([1/6,1/3,2/3,5/6], [1/8,3/8,5/8,7/8]))
            sage: H.M_value()
            729/4096
            sage: Hyp(alpha_beta=(([1/2,1/2,1/2,1/2], [0,0,0,0]))).M_value()
            256
            sage: Hyp(cyclotomic=([5], [1,1,1,1])).M_value()
            3125
        """
    def is_primitive(self) -> bool:
        """
        Return whether this data is primitive.

        .. SEEALSO::

            :meth:`primitive_index`, :meth:`primitive_data`

        EXAMPLES::

            sage: from sage.modular.hypergeometric_motive import HypergeometricData as Hyp
            sage: Hyp(cyclotomic=([3], [4])).is_primitive()
            True
            sage: Hyp(gamma_list=[-2, 4, 6, -8]).is_primitive()
            False
            sage: Hyp(gamma_list=[-3, 6, 9, -12]).is_primitive()
            False
        """
    def primitive_index(self):
        """
        Return the primitive index.

        .. SEEALSO::

            :meth:`is_primitive`, :meth:`primitive_data`

        EXAMPLES::

            sage: from sage.modular.hypergeometric_motive import HypergeometricData as Hyp
            sage: Hyp(cyclotomic=([3], [4])).primitive_index()
            1
            sage: Hyp(gamma_list=[-2, 4, 6, -8]).primitive_index()
            2
            sage: Hyp(gamma_list=[-3, 6, 9, -12]).primitive_index()
            3
        """
    def has_symmetry_at_one(self) -> bool:
        """
        If ``True``, the motive H(t=1) is a direct sum of two motives.

        Note that simultaneous exchange of (t,1/t) and (alpha,beta)
        always gives the same motive.

        EXAMPLES::

            sage: from sage.modular.hypergeometric_motive import HypergeometricData as Hyp
            sage: Hyp(alpha_beta=[[1/2]*16, [0]*16]).has_symmetry_at_one()
            True

        REFERENCES:

        - [Roberts2017]_
        """
    def lfunction(self, t, prec: int = 53):
        """
        Return the `L`-function of ``self``.

        The result is a wrapper around a PARI `L`-function.

        INPUT:

        - ``prec`` -- precision (default: 53)

        EXAMPLES::

            sage: from sage.modular.hypergeometric_motive import HypergeometricData as Hyp
            sage: H = Hyp(cyclotomic=([3], [4]))
            sage: L = H.lfunction(1/64); L
            PARI L-function associated to Hypergeometric data for [1/3, 2/3] and [1/4, 3/4]
            sage: L(4)
            0.997734256321692
        """
    def canonical_scheme(self, t=None):
        """
        Return the canonical scheme.

        This is a scheme that contains this hypergeometric motive in its cohomology.

        EXAMPLES::

            sage: from sage.modular.hypergeometric_motive import HypergeometricData as Hyp
            sage: H = Hyp(cyclotomic=([3], [4]))
            sage: H.gamma_list()
            [-1, 2, 3, -4]
            sage: H.canonical_scheme()
            Spectrum of Quotient of Multivariate Polynomial Ring
            in X0, X1, Y0, Y1 over Fraction Field of Univariate Polynomial Ring
            in t over Rational Field by the ideal
            (X0 + X1 - 1, Y0 + Y1 - 1, (-t)*X0^2*X1^3 + 27/64*Y0*Y1^4)

            sage: H = Hyp(gamma_list=[-2, 3, 4, -5])
            sage: H.canonical_scheme()
            Spectrum of Quotient of Multivariate Polynomial Ring
            in X0, X1, Y0, Y1 over Fraction Field of Univariate Polynomial Ring
            in t over Rational Field by the ideal
            (X0 + X1 - 1, Y0 + Y1 - 1, (-t)*X0^3*X1^4 + 1728/3125*Y0^2*Y1^5)

        REFERENCES:

        [Kat1991]_, section 5.4
        """
    def lattice_polytope(self):
        """
        Return the associated lattice polytope.

        This uses the matrix defined in section 3 of [RRV2022]_ and
        section 3 of [RV2019]_.

        EXAMPLES::

            sage: from sage.modular.hypergeometric_motive import HypergeometricData as Hyp
            sage: H = Hyp(gamma_list=[-5, -2, 3, 4])
            sage: P = H.lattice_polytope(); P
            2-d lattice polytope in 2-d lattice M
            sage: P.polyhedron().f_vector()
            (1, 4, 4, 1)
            sage: len(P.points())
            7

        The Chebyshev example from [RV2019]_::

            sage: H = Hyp(gamma_list=[-30, -1, 6, 10, 15])
            sage: P = H.lattice_polytope(); P
            3-d lattice polytope in 3-d lattice M
            sage: len(P.points())
            19
            sage: P.polyhedron().f_vector()
            (1, 5, 9, 6, 1)
        """
    def twist(self):
        """
        Return the twist of this data.

        This is defined by adding `1/2` to each rational in `\\alpha`
        and `\\beta`.

        This is an involution.

        EXAMPLES::

            sage: from sage.modular.hypergeometric_motive import HypergeometricData as Hyp
            sage: H = Hyp(alpha_beta=([1/2], [0]))
            sage: H.twist()
            Hypergeometric data for [0] and [1/2]
            sage: H.twist().twist() == H
            True

            sage: Hyp(cyclotomic=([6], [1,2])).twist().cyclotomic_data()
            ([3], [1, 2])
        """
    def swap_alpha_beta(self):
        """
        Return the hypergeometric data with ``alpha`` and ``beta`` exchanged.

        EXAMPLES::

            sage: from sage.modular.hypergeometric_motive import HypergeometricData as Hyp
            sage: H = Hyp(alpha_beta=([1/2], [0]))
            sage: H.swap_alpha_beta()
            Hypergeometric data for [0] and [1/2]
        """
    def primitive_data(self):
        """
        Return a primitive version.

        .. SEEALSO::

            :meth:`is_primitive`, :meth:`primitive_index`

        EXAMPLES::

            sage: from sage.modular.hypergeometric_motive import HypergeometricData as Hyp
            sage: H = Hyp(cyclotomic=([3], [4]))
            sage: H2 = Hyp(gamma_list=[-2, 4, 6, -8])
            sage: H2.primitive_data() == H
            True
        """
    def gauss_table(self, p, f, prec):
        """
        Return (and cache) a table of Gauss sums used in the trace formula.

        .. SEEALSO::

            :meth:`gauss_table_full`

        EXAMPLES::

            sage: from sage.modular.hypergeometric_motive import HypergeometricData as Hyp
            sage: H = Hyp(cyclotomic=([3], [4]))
            sage: H.gauss_table(2, 2, 4)
            (4, [1 + 2 + 2^2 + 2^3, 1 + 2 + 2^2 + 2^3, 1 + 2 + 2^2 + 2^3])
        """
    def gauss_table_full(self):
        """
        Return a dict of all stored tables of Gauss sums.

        The result is passed by reference, and is an attribute of the class;
        consequently, modifying the result has global side effects. Use with
        caution.

        .. SEEALSO::

            :meth:`gauss_table`

        EXAMPLES::

            sage: from sage.modular.hypergeometric_motive import HypergeometricData as Hyp
            sage: H = Hyp(cyclotomic=([3], [4]))
            sage: H.euler_factor(2, 7, cache_p=True)
            7*T^2 - 3*T + 1
            sage: H.gauss_table_full()[(7, 1)]
            (2, array('l', [-1, -29, -25, -48, -47, -22]))

        Clearing cached values::

            sage: H = Hyp(cyclotomic=([3], [4]))
            sage: H.euler_factor(2, 7, cache_p=True)
            7*T^2 - 3*T + 1
            sage: d = H.gauss_table_full()
            sage: d.clear() # Delete all entries of this dict
            sage: H1 = Hyp(cyclotomic=([5], [12]))
            sage: d1 = H1.gauss_table_full()
            sage: len(d1.keys()) # No cached values
            0
        """
    @cached_method
    def padic_H_value(self, p, f, t, prec=None, cache_p: bool = False):
        """
        Return the `p`-adic trace of Frobenius, computed using the
        Gross-Koblitz formula.

        If left unspecified, `prec` is set to the minimum `p`-adic precision
        needed to recover the Euler factor.

        If ``cache_p`` is ``True``, then the function caches an intermediate
        result which depends only on `p` and `f`. This leads to a significant
        speedup when iterating over `t`.

        INPUT:

        - ``p`` -- a prime number

        - ``f`` -- integer such that `q = p^f`

        - ``t`` -- a rational parameter

        - ``prec`` -- precision (optional)

        - ``cache_p`` -- boolean

        OUTPUT: integer

        EXAMPLES:

        From Benasque report [Benasque2009]_, page 8::

            sage: from sage.modular.hypergeometric_motive import HypergeometricData as Hyp
            sage: H = Hyp(alpha_beta=([1/2]*4, [0]*4))
            sage: [H.padic_H_value(3,i,-1) for i in range(1,3)]
            [0, -12]
            sage: [H.padic_H_value(5,i,-1) for i in range(1,3)]
            [-4, 276]
            sage: [H.padic_H_value(7,i,-1) for i in range(1,3)]
            [0, -476]
            sage: [H.padic_H_value(11,i,-1) for i in range(1,3)]
            [0, -4972]

        From [Roberts2015]_ (but note conventions regarding `t`)::

            sage: H = Hyp(gamma_list=[-6,-1,4,3])
            sage: t = 189/125
            sage: H.padic_H_value(13,1,1/t)
            0

        TESTS:

        Check issue from :issue:`28404`::

            sage: H1 = Hyp(cyclotomic=([1,1,1], [6,2]))
            sage: H2 = Hyp(cyclotomic=([6,2], [1,1,1]))
            sage: [H1.padic_H_value(5,1,i) for i in range(2,5)]
            [1, -4, -4]
            sage: [H2.padic_H_value(5,1,i) for i in range(2,5)]
            [-4, 1, -4]

        Check for potential overflow::

            sage: H = Hyp(cyclotomic=[[10,6], [5,4]])
            sage: H.padic_H_value(101, 2, 2)
            -1560629

        Check issue from :issue:`29778`::

            sage: H = Hyp(alpha_beta=([1/5,2/5,3/5,4/5,1/5,2/5,3/5,4/5],  [1/4,3/4,1/7,2/7,3/7,4/7,5/7,6/7]))
            sage: try:
            ....:     print(H.padic_H_value(373, 4, 2))
            ....: except ValueError as s:
            ....:     print(s)
            p^f cannot exceed 2^31

        Check error handling for wild and tame primes::

            sage: H = Hyp(alpha_beta=([1/5,2/5,3/5,4/5,1/5,2/5,3/5,4/5],  [1/4,3/4,1/7,2/7,3/7,4/7,5/7,6/7]))
            sage: try:
            ....:     print(H.padic_H_value(5, 1, 2))
            ....: except NotImplementedError as s:
            ....:     print(s)
            p is wild
            sage: try:
            ....:     print(H.padic_H_value(3, 1, 3))
            ....: except NotImplementedError as s:
            ....:     print(s)
            p is tame

        Check that :issue:`37910` is resolved::

            sage: H = Hyp(alpha_beta=[[1/2,1/2,1/2,1/2,1/2,1/3,2/3,1/6,5/6],  [0,0,0,0,0,0,0,0,0]])
            sage: H.padic_H_value(151, 2, -512000)
            50178940126155881

        REFERENCES:

        - [MagmaHGM]_
        """
    trace = padic_H_value
    @cached_method
    def H_value(self, p, f, t, ring=None):
        """
        Return the trace of the Frobenius, computed in terms of Gauss sums
        using the hypergeometric trace formula.

        INPUT:

        - ``p`` -- a prime number

        - ``f`` -- integer such that `q = p^f`

        - ``t`` -- a rational parameter

        - ``ring`` -- (default: :class:`UniversalCyclotomicfield`)

        The ring could be also ``ComplexField(n)`` or ``QQbar``.

        OUTPUT: integer

        .. WARNING::

            This is apparently working correctly as can be tested
            using ``ComplexField(70)`` as the value ring.

            Using instead :class:`UniversalCyclotomicfield`, this is much
            slower than the `p`-adic version :meth:`padic_H_value`.

            Unlike in :meth:`padic_H_value`, tame and wild primes are not supported.

        EXAMPLES:

        With values in the :class:`UniversalCyclotomicField` (slow)::

            sage: from sage.modular.hypergeometric_motive import HypergeometricData as Hyp
            sage: H = Hyp(alpha_beta=([1/2]*4, [0]*4))
            sage: [H.H_value(3,i,-1) for i in range(1,3)]
            [0, -12]
            sage: [H.H_value(5,i,-1) for i in range(1,3)]
            [-4, 276]
            sage: [H.H_value(7,i,-1) for i in range(1,3)]  # not tested
            [0, -476]
            sage: [H.H_value(11,i,-1) for i in range(1,3)]  # not tested
            [0, -4972]
            sage: [H.H_value(13,i,-1) for i in range(1,3)]  # not tested
            [-84, -1420]

        With values in :class:`ComplexField`::

            sage: [H.H_value(5,i,-1, ComplexField(60)) for i in range(1,3)]
            [-4, 276]

        Check issue from :issue:`28404`::

            sage: H1 = Hyp(cyclotomic=([1,1,1], [6,2]))
            sage: H2 = Hyp(cyclotomic=([6,2], [1,1,1]))
            sage: [H1.H_value(5,1,i) for i in range(2,5)]
            [1, -4, -4]
            sage: [H2.H_value(5,1,QQ(i)) for i in range(2,5)]
            [-4, 1, -4]

        TESTS:

        Check issue from :issue:`29778`::

            sage: H = Hyp(cyclotomic=[[5,5], [4,7]])
            sage: try:
            ....:     print(H.padic_H_value(373, 4, 2))
            ....: except ValueError as s:
            ....:     print(s)
            p^f cannot exceed 2^31

        Check error handling for wild and tame primes::

            sage: H = Hyp(cyclotomic=[[5,5], [4,7]])
            sage: try:
            ....:     print(H.padic_H_value(5, 1, 2))
            ....: except NotImplementedError as s:
            ....:     print(s)
            p is wild
            sage: try:
            ....:     print(H.padic_H_value(3, 1, 3))
            ....: except NotImplementedError as s:
            ....:     print(s)
            p is tame

        REFERENCES:

        - [BeCoMe]_ (Theorem 1.3)
        - [Benasque2009]_
        """
    def sign(self, t, p):
        """
        Return the sign of the functional equation for the Euler factor of the motive `H_t` at the prime `p`.

        For odd weight, the sign of the functional equation is +1. For even
        weight, the sign is computed by a recipe found in Section 11.1 of [Watkins]_
        (when 0 is not in alpha).

        EXAMPLES::

            sage: from sage.modular.hypergeometric_motive import HypergeometricData as Hyp
            sage: H = Hyp(cyclotomic=([6,2], [1,1,1]))
            sage: H.weight(), H.degree()
            (2, 3)
            sage: [H.sign(1/4,p) for p in [5,7,11,13,17,19]]
            [1, 1, -1, -1, 1, 1]

            sage: H = Hyp(alpha_beta=([1/12,5/12,7/12,11/12], [0,1/2,1/2,1/2]))
            sage: H.weight(), H.degree()
            (2, 4)
            sage: t = -5
            sage: [H.sign(1/t,p) for p in [11,13,17,19,23,29]]
            [-1, -1, -1, 1, 1, 1]

        We check that :issue:`28404` is fixed::

            sage: H = Hyp(cyclotomic=([1,1,1], [6,2]))
            sage: [H.sign(4,p) for p in [5,7,11,13,17,19]]
            [1, 1, -1, -1, 1, 1]
        """
    def euler_factor_tame_contribution(self, t, p, mo, deg=None):
        """
        Return a contribution to the Euler factor of the motive `H_t` at a tame prime.

        The output is only nontrivial when `t` has nonzero `p`-adic valuation.
        The algorithm is described in Section 11.4.1 of [Watkins]_.

        INPUT:

        - ``t`` -- rational number, not 0 or 1

        - ``p`` -- prime number of good reduction

        - ``mo`` -- integer

        - ``deg`` -- integer (optional)

        OUTPUT: a polynomial

        If ``deg`` is specified, the output is truncated to that degree (inclusive).

        EXAMPLES::

            sage: from sage.modular.hypergeometric_motive import HypergeometricData as Hyp
            sage: H = Hyp(cyclotomic=[[3,7], [4,5,6]])
            sage: H.euler_factor_tame_contribution(11^2, 11, 4)
            1
            sage: H.euler_factor_tame_contribution(11^20, 11, 4)
            1331*T^2 + 1
            sage: H.euler_factor_tame_contribution(11^20, 11, 4, deg=1)
            1
            sage: H.euler_factor_tame_contribution(11^20, 11, 5)
            1771561*T^4 + 161051*T^3 + 6171*T^2 + 121*T + 1
            sage: H.euler_factor_tame_contribution(11^20, 11, 5, deg=3)
            161051*T^3 + 6171*T^2 + 121*T + 1
            sage: H.euler_factor_tame_contribution(11^20, 11, 6)
            1
        """
    @cached_method
    def euler_factor(self, t, p, deg=None, cache_p: bool = False):
        """
        Return the Euler factor of the motive `H_t` at prime `p`.

        INPUT:

        - ``t`` -- rational number, not 0

        - ``p`` -- prime number of good reduction

        - ``deg`` -- integer or ``None``

        OUTPUT: a polynomial

        See [Benasque2009]_ for explicit examples of Euler factors.

        For odd weight, the sign of the functional equation is +1. For even
        weight, the sign is computed by a recipe found in Section 11.1 of [Watkins]_.

        If ``deg`` is specified, then the polynomial is only computed up to degree
        ``deg`` (inclusive).

        The prime `p` may be tame, but not wild. When `v_p(t-1)` is nonzero and even,
        the Euler factor includes a linear term described in Section 11.2 of [Watkins]_.

        EXAMPLES::

            sage: from sage.modular.hypergeometric_motive import HypergeometricData as Hyp
            sage: H = Hyp(alpha_beta=([1/2]*4, [0]*4))
            sage: H.euler_factor(-1, 5)
            15625*T^4 + 500*T^3 - 130*T^2 + 4*T + 1

            sage: H = Hyp(gamma_list=[-6,-1,4,3])
            sage: H.weight(), H.degree()
            (1, 2)
            sage: t = 189/125
            sage: [H.euler_factor(1/t,p) for p in [11,13,17,19,23,29]]
            [11*T^2 + 4*T + 1,
            13*T^2 + 1,
            17*T^2 + 1,
            19*T^2 + 1,
            23*T^2 + 8*T + 1,
            29*T^2 + 2*T + 1]

            sage: H = Hyp(cyclotomic=([6,2], [1,1,1]))
            sage: H.weight(), H.degree()
            (2, 3)
            sage: [H.euler_factor(1/4,p) for p in [5,7,11,13,17,19]]
            [125*T^3 + 20*T^2 + 4*T + 1,
             343*T^3 - 42*T^2 - 6*T + 1,
             -1331*T^3 - 22*T^2 + 2*T + 1,
             -2197*T^3 - 156*T^2 + 12*T + 1,
             4913*T^3 + 323*T^2 + 19*T + 1,
             6859*T^3 - 57*T^2 - 3*T + 1]

            sage: H = Hyp(alpha_beta=([1/12,5/12,7/12,11/12], [0,1/2,1/2,1/2]))
            sage: H.weight(), H.degree()
            (2, 4)
            sage: t = -5
            sage: [H.euler_factor(1/t,p) for p in [11,13,17,19,23,29]]
            [-14641*T^4 - 1210*T^3 + 10*T + 1,
             -28561*T^4 - 2704*T^3 + 16*T + 1,
             -83521*T^4 - 4046*T^3 + 14*T + 1,
             130321*T^4 + 14440*T^3 + 969*T^2 + 40*T + 1,
             279841*T^4 - 25392*T^3 + 1242*T^2 - 48*T + 1,
             707281*T^4 - 7569*T^3 + 696*T^2 - 9*T + 1]

        This is an example of higher degree::

            sage: H = Hyp(cyclotomic=([11], [7, 12]))
            sage: H.euler_factor(2, 13)
            371293*T^10 - 85683*T^9 + 26364*T^8 + 1352*T^7 - 65*T^6 + 394*T^5 - 5*T^4 + 8*T^3 + 12*T^2 - 3*T + 1
            sage: H.euler_factor(2, 13, deg=4)
            -5*T^4 + 8*T^3 + 12*T^2 - 3*T + 1
            sage: H.euler_factor(2, 19) # long time
            2476099*T^10 - 651605*T^9 + 233206*T^8 - 77254*T^7 + 20349*T^6 - 4611*T^5 + 1071*T^4 - 214*T^3 + 34*T^2 - 5*T + 1

        This is an example of tame primes::

            sage: H = Hyp(cyclotomic=[[4,2,2], [3,1,1]])
            sage: H.euler_factor(8, 7)
            -7*T^3 + 7*T^2 - T + 1
            sage: H.euler_factor(50, 7)
            -7*T^3 + 7*T^2 - T + 1
            sage: H.euler_factor(7, 7)
            -T + 1
            sage: H.euler_factor(1/7^2, 7)
            T + 1
            sage: H.euler_factor(1/7^4, 7)
            7*T^3 + 7*T^2 + T + 1

        This is an example with `t = 1`::

            sage: H = Hyp(cyclotomic=[[4,2], [3,1]])
            sage: H.euler_factor(1, 7)
            -T^2 + 1
            sage: H = Hyp(cyclotomic=[[5], [1,1,1,1]])
            sage: H.euler_factor(1, 7)
            343*T^2 - 6*T + 1

        TESTS::

             sage: H1 = Hyp(alpha_beta=([1,1,1], [1/2,1/2,1/2]))
             sage: H2 = H1.swap_alpha_beta()
             sage: H1.euler_factor(-1, 3)
             27*T^3 + 3*T^2 + T + 1
             sage: H2.euler_factor(-1, 3)
             27*T^3 + 3*T^2 + T + 1
             sage: H = Hyp(alpha_beta=([0,0,0,1/3,2/3], [1/2,1/5,2/5,3/5,4/5]))
             sage: H.euler_factor(5,7)
             16807*T^5 - 686*T^4 - 105*T^3 - 15*T^2 - 2*T + 1

        Check for precision downsampling::

            sage: H = Hyp(cyclotomic=[[3], [4]])
            sage: H.euler_factor(2, 11, cache_p=True)
            11*T^2 - 3*T + 1
            sage: H = Hyp(cyclotomic=[[12], [1,2,6]])
            sage: H.euler_factor(2, 11, cache_p=True)
            -T^4 + T^3 - T + 1

        Check issue from :issue:`29778`::

            sage: H = Hyp(cyclotomic=[[5,5], [4,7]])
            sage: try:
            ....:     print(H.euler_factor(2, 373))
            ....: except ValueError as s:
            ....:     print(s)
            p^f cannot exceed 2^31

        Check handling of some tame cases::

            sage: H = Hyp(cyclotomic=[[4,2,2,2], [3,1,1,1]])
            sage: H.euler_factor(8, 7)
            2401*T^4 - 392*T^3 + 46*T^2 - 8*T + 1
            sage: H.euler_factor(50, 7)
            16807*T^5 - 343*T^4 - 70*T^3 - 10*T^2 - T + 1
            sage: H = Hyp(cyclotomic=[[3,7], [4,5,6]])
            sage: H.euler_factor(11, 11)
            1
            sage: H.euler_factor(11**4, 11)
            1331*T^2 + 1
            sage: H.euler_factor(11**5, 11)
            1771561*T^4 + 161051*T^3 + 6171*T^2 + 121*T + 1
            sage: H.euler_factor(11**5, 11, deg=3)
            161051*T^3 + 6171*T^2 + 121*T + 1
            sage: H.euler_factor(11**-3, 11)
            1331*T^2 + 1
            sage: H.euler_factor(11**-7, 11)
            2357947691*T^6 - 58564*T^3 + 1
            sage: H = Hyp(cyclotomic=[[7], [5,1,1]])
            sage: H.euler_factor(2, 2)
            -T + 1
            sage: H.euler_factor(2^-7, 2)
            8*T^6 - 2*T^3 + 1
            sage: H.euler_factor(3, 2)
            4*T^5 + 4*T^4 + 2*T^3 + 2*T^2 + T + 1

        More examples of tame primes from [Watkins]_::

            sage: H = Hyp(cyclotomic=[[3,12], [6,6,1,1]])
            sage: H.euler_factor(1/8, 7).factor()
            (-1) * (7*T - 1) * (117649*T^4 + 2744*T^3 + 105*T^2 + 8*T + 1)
            sage: H.euler_factor(1/12, 11).factor()
            (11*T + 1) * (1771561*T^4 - 18634*T^3 + 22*T^2 - 14*T + 1)
            sage: H = Hyp(cyclotomic=[[4,4,4],[6,2,1,1,1]])
            sage: H.euler_factor(1/8, 7).factor()
            (49*T + 1) * (5764801*T^4 - 86436*T^3 + 2758*T^2 - 36*T + 1)
            sage: H.euler_factor(1/12, 11).factor()
            (-1) * (121*T - 1) * (214358881*T^4 - 527076*T^3 + 12694*T^2 - 36*T + 1)
            sage: H = Hyp(cyclotomic=[[10,4,2], [18,1]])
            sage: H.euler_factor(1/14, 13)
            -4826809*T^6 + 114244*T^5 + 2197*T^4 - 13*T^2 - 4*T + 1

        Check error handling for wild primes::

            sage: H = Hyp(cyclotomic=[[5,5], [4,7]])
            sage: try:
            ....:     print(H.euler_factor(2, 5))
            ....: except NotImplementedError as s:
            ....:     print(s)
            p is wild

        REFERENCES:

        - [Roberts2015]_
        - [Watkins]_
        """
