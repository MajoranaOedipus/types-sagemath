from _typeshed import Incomplete
from sage.arith.misc import euler_phi as euler_phi, next_prime as next_prime
from sage.functions.log import log as log
from sage.functions.other import ceil as ceil, floor as floor
from sage.misc.functional import cyclotomic_polynomial as cyclotomic_polynomial, round as round, sqrt as sqrt
from sage.misc.prandom import randint as randint
from sage.misc.randstate import set_random_seed as set_random_seed
from sage.modules.free_module import FreeModule as FreeModule
from sage.modules.free_module_element import random_vector as random_vector, vector as vector
from sage.numerical.optimize import find_root as find_root
from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as IntegerModRing
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.real_mpfr import RR as RR
from sage.stats.distributions.discrete_gaussian_integer import DiscreteGaussianDistributionIntegerSampler as DiscreteGaussianDistributionIntegerSampler
from sage.stats.distributions.discrete_gaussian_polynomial import DiscreteGaussianDistributionPolynomialSampler as DiscreteGaussianDistributionPolynomialSampler
from sage.structure.element import parent as parent
from sage.structure.sage_object import SageObject as SageObject
from sage.symbolic.constants import pi as pi
from sage.symbolic.ring import SR as SR

class UniformSampler(SageObject):
    """
    Uniform sampling in a range of integers.

    EXAMPLES::

        sage: from sage.crypto.lwe import UniformSampler
        sage: sampler = UniformSampler(-2, 2); sampler
        UniformSampler(-2, 2)
        sage: sampler() in range(-2, 3)
        True

    .. automethod:: __init__
    .. automethod:: __call__
    """
    lower_bound: Incomplete
    upper_bound: Incomplete
    def __init__(self, lower_bound, upper_bound) -> None:
        """
        Construct a uniform sampler with bounds ``lower_bound`` and
        ``upper_bound`` (both endpoints inclusive).

        INPUT:

        - ``lower_bound`` -- integer
        - ``upper_bound`` -- integer

        EXAMPLES::

            sage: from sage.crypto.lwe import UniformSampler
            sage: UniformSampler(-2, 2)
            UniformSampler(-2, 2)
        """
    def __call__(self):
        """
        Return a new sample.

        EXAMPLES::

            sage: from sage.crypto.lwe import UniformSampler
            sage: sampler = UniformSampler(-12, 12)
            sage: sampler() in range(-12, 13)
            True
        """

class UniformPolynomialSampler(SageObject):
    """
    Uniform sampler for polynomials.

    EXAMPLES::

        sage: from sage.crypto.lwe import UniformPolynomialSampler
        sage: UniformPolynomialSampler(ZZ['x'], 8, -2, 2)().parent()
        Univariate Polynomial Ring in x over Integer Ring

    .. automethod:: __init__
    .. automethod:: __call__
    """
    n: Incomplete
    P: Incomplete
    lower_bound: Incomplete
    upper_bound: Incomplete
    D: Incomplete
    def __init__(self, P, n, lower_bound, upper_bound) -> None:
        """
        Construct a sampler for univariate polynomials of degree ``n-1`` where
        coefficients are drawn uniformly at random between ``lower_bound`` and
        ``upper_bound`` (both endpoints inclusive).

        INPUT:

        - ``P`` -- a univariate polynomial ring over the Integers
        - ``n`` -- number of coefficients to be sampled
        - ``lower_bound`` -- integer
        - ``upper_bound`` -- integer

        EXAMPLES::

            sage: from sage.crypto.lwe import UniformPolynomialSampler
            sage: UniformPolynomialSampler(ZZ['x'], 10, -10, 10)
            UniformPolynomialSampler(10, -10, 10)
        """
    def __call__(self):
        """
        Return a new sample.

        EXAMPLES::

            sage: from sage.crypto.lwe import UniformPolynomialSampler
            sage: sampler = UniformPolynomialSampler(ZZ['x'], 8, -12, 12)
            sage: sampler().parent()
            Univariate Polynomial Ring in x over Integer Ring
        """

class LWE(SageObject):
    """
    Learning with Errors (LWE) oracle.

    .. automethod:: __init__
    .. automethod:: __call__
    """
    n: Incomplete
    m: Incomplete
    K: Incomplete
    FM: Incomplete
    D: Incomplete
    secret_dist: Incomplete
    def __init__(self, n, q, D, secret_dist: str = 'uniform', m=None) -> None:
        """
        Construct an LWE oracle in dimension ``n`` over a ring of order
        ``q`` with noise distribution ``D``.

        INPUT:

        - ``n`` -- dimension (integer > 0)
        - ``q`` -- modulus typically > n (integer > 0)
        - ``D`` -- an error distribution such as an instance of
          :class:`DiscreteGaussianDistributionIntegerSampler` or :class:`UniformSampler`
        - ``secret_dist`` -- distribution of the secret (default: ``'uniform'``); one of

          - ``'uniform'`` -- secret follows the uniform distribution in `\\Zmod{q}`
          - ``'noise'`` -- secret follows the noise distribution
          - ``(lb, ub)`` -- the secret is chosen uniformly from ``[lb,...,ub]``
            including both endpoints

        - ``m`` -- number of allowed samples or ``None`` if no such limit exists
          (default: ``None``)

        EXAMPLES:

        First, we construct a noise distribution with standard deviation 3.0::

            sage: from sage.stats.distributions.discrete_gaussian_integer import DiscreteGaussianDistributionIntegerSampler
            sage: D = DiscreteGaussianDistributionIntegerSampler(3.0)

        Next, we construct our oracle::

            sage: from sage.crypto.lwe import LWE
            sage: lwe = LWE(n=20, q=next_prime(400), D=D); lwe
            LWE(20, 401, Discrete Gaussian sampler over the Integers with sigma = 3.000000 and c = 0.000000, 'uniform', None)

        and sample 1000 samples::

            sage: L = []
            sage: def add_samples():
            ....:     global L
            ....:     L += [lwe() for _ in range(100)]
            sage: add_samples()

        To test the oracle, we use the internal secret to evaluate the samples
        in the secret::

            sage: S = lambda : [ZZ(a.dot_product(lwe._LWE__s) - c) for (a,c) in L]

        However, while Sage represents finite field elements between 0 and q-1
        we rely on a balanced representation of those elements here. Hence, we
        fix the representation and recover the correct standard deviation of the
        noise::

            sage: from numpy import std                                                             # needs numpy
            sage: while abs(std([e if e <= 200 else e-401 for e in S()]) - 3.0) > 0.01:             # needs numpy
            ....:     L = []  # reset L to avoid quadratic behaviour
            ....:     add_samples()

        If ``m`` is not ``None`` the number of available samples is restricted::

            sage: from sage.crypto.lwe import LWE
            sage: lwe = LWE(n=20, q=next_prime(400), D=D, m=30)
            sage: _ = [lwe() for _ in range(30)]
            sage: lwe()  # 31
            Traceback (most recent call last):
            ...
            IndexError: Number of available samples exhausted.
        """
    def __call__(self):
        """
        EXAMPLES::

            sage: from sage.crypto.lwe import DiscreteGaussianDistributionIntegerSampler, LWE
            sage: LWE(10, 401, DiscreteGaussianDistributionIntegerSampler(3))()[0].parent()
            Vector space of dimension 10 over Ring of integers modulo 401
            sage: LWE(10, 401, DiscreteGaussianDistributionIntegerSampler(3))()[1].parent()
            Ring of integers modulo 401
        """

class Regev(LWE):
    """
    LWE oracle with parameters as in [Reg09]_.

    .. automethod:: __init__
    """
    def __init__(self, n, secret_dist: str = 'uniform', m=None) -> None:
        """
        Construct LWE instance parameterised by security parameter ``n`` where
        the modulus ``q`` and the ``stddev`` of the noise are chosen as in
        [Reg09]_.

        INPUT:

        - ``n`` -- security parameter (integer > 0)
        - ``secret_dist`` -- distribution of the secret. See documentation of :class:`LWE`
          for details (default='uniform')
        - ``m`` -- number of allowed samples or ``None`` if no such limit exists
          (default: ``None``)

        EXAMPLES::

            sage: from sage.crypto.lwe import Regev
            sage: Regev(n=20)
            LWE(20, 401, Discrete Gaussian sampler over the Integers with sigma = 1.915069 and c = 401.000000, 'uniform', None)
        """

class LindnerPeikert(LWE):
    """
    LWE oracle with parameters as in [LP2011]_.

    .. automethod:: __init__
    """
    def __init__(self, n, delta: float = 0.01, m=None) -> None:
        """
        Construct LWE instance parameterised by security parameter ``n`` where
        the modulus ``q`` and the ``stddev`` of the noise is chosen as in
        [LP2011]_.

        INPUT:

        - ``n`` -- security parameter (integer > 0)
        - ``delta`` -- error probability per symbol (default: 0.01)
        - ``m`` -- number of allowed samples or ``None`` in which case ``m=2*n +
          128`` as in [LP2011]_ (default: ``None``)

        EXAMPLES::

            sage: from sage.crypto.lwe import LindnerPeikert
            sage: LindnerPeikert(n=20)
            LWE(20, 2053, Discrete Gaussian sampler over the Integers with sigma = 3.600954 and c = 0.000000, 'noise', 168)
        """

class UniformNoiseLWE(LWE):
    """
    LWE oracle with uniform secret with parameters as in [CGW2013]_.

    .. automethod:: __init__
    """
    def __init__(self, n, instance: str = 'key', m=None) -> None:
        """
        Construct LWE instance parameterised by security parameter ``n`` where
        all other parameters are chosen as in [CGW2013]_.

        INPUT:

        - ``n`` -- security parameter (integer >= 89)
        - ``instance`` -- one of

          - ``'key'`` -- the LWE-instance that hides the secret key is generated
          - ``'encrypt'`` -- the LWE-instance that hides the message is generated
            (default: ``'key'``)

        - ``m`` -- number of allowed samples or ``None`` in which case ``m`` is
          chosen as in [CGW2013]_.  (default: ``None``)

        EXAMPLES::

            sage: from sage.crypto.lwe import UniformNoiseLWE
            sage: UniformNoiseLWE(89)
            LWE(89, 64311834871, UniformSampler(0, 6577), 'noise', 131)

            sage: UniformNoiseLWE(89, instance='encrypt')
            LWE(131, 64311834871, UniformSampler(0, 11109), 'noise', 181)
        """

class RingLWE(SageObject):
    """
    Ring Learning with Errors oracle.

    .. automethod:: __init__
    .. automethod:: __call__
    """
    N: Incomplete
    n: Incomplete
    m: Incomplete
    K: Incomplete
    D: Incomplete
    q: Incomplete
    poly: Incomplete
    R_q: Incomplete
    secret_dist: Incomplete
    def __init__(self, N, q, D, poly=None, secret_dist: str = 'uniform', m=None) -> None:
        """
        Construct a Ring-LWE oracle in dimension ``n=phi(N)`` over a ring of order
        ``q`` with noise distribution ``D``.

        INPUT:

        - ``N`` -- index of cyclotomic polynomial (integer > 0, must be power of 2)
        - ``q`` -- modulus typically > N (integer > 0)
        - ``D`` -- an error distribution such as an instance of
          :class:`DiscreteGaussianDistributionPolynomialSampler` or :class:`UniformSampler`
        - ``poly`` -- a polynomial of degree ``phi(N)``. If ``None`` the
          cyclotomic polynomial used (default: ``None``).
        - ``secret_dist`` -- distribution of the secret. See documentation of
          :class:`LWE` for details (default='uniform')
        - ``m`` -- number of allowed samples or ``None`` if no such limit exists
          (default: ``None``)

        EXAMPLES::

            sage: from sage.crypto.lwe import RingLWE
            sage: from sage.stats.distributions.discrete_gaussian_polynomial import DiscreteGaussianDistributionPolynomialSampler
            sage: D = DiscreteGaussianDistributionPolynomialSampler(ZZ['x'], n=euler_phi(20), sigma=3.0)                # needs sage.libs.pari
            sage: RingLWE(N=20, q=next_prime(800), D=D)                                 # needs sage.libs.pari
            RingLWE(20, 809, Discrete Gaussian sampler for polynomials of degree < 8 with σ=3.000000 in each component, x^8 - x^6 + x^4 - x^2 + 1, 'uniform', None)
        """
    def __call__(self):
        """
        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: from sage.crypto.lwe import DiscreteGaussianDistributionPolynomialSampler, RingLWE
            sage: N = 16
            sage: n = euler_phi(N)
            sage: D = DiscreteGaussianDistributionPolynomialSampler(ZZ['x'], n, 5)
            sage: ringlwe = RingLWE(N, 257, D, secret_dist='uniform')
            sage: ringlwe()[0].parent()
            Vector space of dimension 8 over Ring of integers modulo 257
            sage: ringlwe()[1].parent()
            Vector space of dimension 8 over Ring of integers modulo 257
        """

class RingLindnerPeikert(RingLWE):
    """
    Ring-LWE oracle with parameters as in [LP2011]_.

    .. automethod:: __init__
    """
    def __init__(self, N, delta: float = 0.01, m=None) -> None:
        """
        Construct a Ring-LWE oracle in dimension ``n=phi(N)`` where
        the modulus ``q`` and the ``stddev`` of the noise is chosen as in
        [LP2011]_.

        INPUT:

        - ``N`` -- index of cyclotomic polynomial (integer > 0, must be power of 2)
        - ``delta`` -- error probability per symbol (default: 0.01)
        - ``m`` -- number of allowed samples or ``None`` in which case ``3*n`` is
          used (default: ``None``)

        EXAMPLES::

            sage: from sage.crypto.lwe import RingLindnerPeikert
            sage: RingLindnerPeikert(N=16)
            RingLWE(16, 1031, Discrete Gaussian sampler for polynomials of degree < 8 with σ=2.803372 in each component, x^8 + 1, 'noise', 24)
        """

class RingLWEConverter(SageObject):
    """
    Wrapper callable to convert Ring-LWE oracles into LWE oracles by
    disregarding the additional structure.

    .. automethod:: __init__
    .. automethod:: __call__
    """
    ringlwe: Incomplete
    n: Incomplete
    def __init__(self, ringlwe) -> None:
        """
        INPUT:

        - ``ringlwe`` -- an instance of a :class:`RingLWE`

        EXAMPLES::

            sage: from sage.crypto.lwe import DiscreteGaussianDistributionPolynomialSampler, RingLWE, RingLWEConverter
            sage: D = DiscreteGaussianDistributionPolynomialSampler(ZZ['x'], euler_phi(16), 5)
            sage: lwe = RingLWEConverter(RingLWE(16, 257, D, secret_dist='uniform'))
            sage: set_random_seed(1337)
            sage: lwe()
            ((171, 197, 58, 125, 3, 216, 32, 130), ...)
        """
    def __call__(self):
        """
        EXAMPLES::

            sage: from sage.crypto.lwe import DiscreteGaussianDistributionPolynomialSampler, RingLWE, RingLWEConverter
            sage: D = DiscreteGaussianDistributionPolynomialSampler(ZZ['x'], euler_phi(16), 5)
            sage: lwe = RingLWEConverter(RingLWE(16, 257, D, secret_dist='uniform'))
            sage: set_random_seed(1337)
            sage: lwe()
            ((171, 197, 58, 125, 3, 216, 32, 130), ...)
        """

def samples(m, n, lwe, seed=None, balanced: bool = False, **kwds):
    '''
    Return ``m`` LWE samples.

    INPUT:

    - ``m`` -- the number of samples (integer > 0)
    - ``n`` -- the security parameter (integer > 0)
    - ``lwe`` -- either

      - a subclass of :class:`LWE` such as :class:`Regev` or :class:`LindnerPeikert`
      - an instance of :class:`LWE` or any subclass
      - the name of any such class (e.g., "Regev", "LindnerPeikert")

    - ``seed`` -- seed to be used for generation or ``None`` if no specific seed
      shall be set (default: ``None``)
    - ``balanced`` -- use function :func:`balance_sample` to return balanced
      representations of finite field elements (default: ``False``)
    - ``**kwds`` -- passed through to LWE constructor

    EXAMPLES::

        sage: from sage.crypto.lwe import samples, Regev
        sage: samples(2, 20, Regev, seed=1337)
        [((199, 388, 337, 53, 200, 284, 336, 215, 75, 14, 274, 234, 97, 255, 246, 153, 268, 218, 396, 351), 15),
         ((365, 227, 333, 165, 76, 328, 288, 206, 286, 42, 175, 155, 190, 275, 114, 280, 45, 218, 304, 386), 143)]

        sage: from sage.crypto.lwe import samples, Regev
        sage: samples(2, 20, Regev, balanced=True, seed=1337)
        [((199, -13, -64, 53, 200, -117, -65, -186, 75, 14, -127, -167, 97, -146, -155, 153, -133, -183, -5, -50), 15),
         ((-36, -174, -68, 165, 76, -73, -113, -195, -115, 42, 175, 155, 190, -126, 114, -121, 45, -183, -97, -15), 143)]

        sage: from sage.crypto.lwe import samples
        sage: samples(2, 20, \'LindnerPeikert\')
        [((506, 1205, 398, 0, 337, 106, 836, 75, 1242, 642, 840, 262, 1823, 1798, 1831, 1658, 1084, 915, 1994, 163), 1447),
         ((463, 250, 1226, 1906, 330, 933, 1014, 1061, 1322, 2035, 1849, 285, 1993, 1975, 864, 1341, 41, 1955, 1818, 1357), 312)]
    '''
def balance_sample(s, q=None):
    """
    Given ``(a,c) = s`` return a tuple ``(a',c')`` where ``a'`` is an integer
    vector with entries between -q//2 and q//2 and ``c`` is also within these
    bounds.

    If ``q`` is given ``(a,c) = s`` may live in the integers. If ``q`` is not
    given, then ``(a,c)`` are assumed to live in `\\Zmod{q}`.

    INPUT:

    - ``s`` -- sample of the form (a,c) where a is a vector and c is a scalar
    - ``q`` -- modulus (default: ``None``)

    EXAMPLES::

        sage: from sage.crypto.lwe import balance_sample, samples, Regev
        sage: for s in samples(10, 5, Regev):
        ....:     b = balance_sample(s)
        ....:     assert all(-29//2 <= c <= 29//2 for c in b[0])
        ....:     assert -29//2 <= b[1] <= 29//2
        ....:     assert all(s[0][j] == b[0][j] % 29 for j in range(5))
        ....:     assert s[1] == b[1] % 29


        sage: from sage.crypto.lwe import balance_sample, DiscreteGaussianDistributionPolynomialSampler, RingLWE, samples
        sage: D = DiscreteGaussianDistributionPolynomialSampler(ZZ['x'], 8, 5)
        sage: rlwe = RingLWE(20, 257, D)
        sage: for s in samples(10, 8, rlwe):
        ....:     b = balance_sample(s)
        ....:     assert all(-257//2 <= c <= 257//2 for bi in b for c in bi)
        ....:     assert all(s[i][j] == b[i][j] % 257 for i in range(2) for j in range(8))

    .. NOTE::

        This function is useful to convert between Sage's standard
        representation of elements in `\\Zmod{q}` as integers between 0 and q-1
        and the usual representation of such elements in lattice cryptography as
        integers between -q//2 and q//2.
    """
