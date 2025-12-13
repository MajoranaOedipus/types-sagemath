from _typeshed import Incomplete
from sage.functions.log import exp as exp
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.functional import sqrt as sqrt
from sage.misc.prandom import normalvariate as normalvariate
from sage.misc.verbose import verbose as verbose
from sage.modules.free_module import FreeModule as FreeModule
from sage.modules.free_module_element import vector as vector
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.rings.real_mpfr import RealField as RealField
from sage.stats.distributions.discrete_gaussian_integer import DiscreteGaussianDistributionIntegerSampler as DiscreteGaussianDistributionIntegerSampler
from sage.structure.sage_object import SageObject as SageObject
from sage.symbolic.constants import pi as pi

class DiscreteGaussianDistributionLatticeSampler(SageObject):
    """
    GPV sampler for Discrete Gaussians over Lattices.

    EXAMPLES::

        sage: D = distributions.DiscreteGaussianDistributionLatticeSampler(ZZ^10, 3.0); D
        Discrete Gaussian sampler with Gaussian parameter σ = 3.00000000000000, c=(0, 0, 0, 0, 0, 0, 0, 0, 0, 0) over lattice with basis
        <BLANKLINE>
        [1 0 0 0 0 0 0 0 0 0]
        [0 1 0 0 0 0 0 0 0 0]
        [0 0 1 0 0 0 0 0 0 0]
        [0 0 0 1 0 0 0 0 0 0]
        [0 0 0 0 1 0 0 0 0 0]
        [0 0 0 0 0 1 0 0 0 0]
        [0 0 0 0 0 0 1 0 0 0]
        [0 0 0 0 0 0 0 1 0 0]
        [0 0 0 0 0 0 0 0 1 0]
        [0 0 0 0 0 0 0 0 0 1]


    We plot a histogram::

        sage: import warnings
        sage: warnings.simplefilter('ignore', UserWarning)
        sage: D = distributions.DiscreteGaussianDistributionLatticeSampler(identity_matrix(2), 3.0)
        sage: S = [D() for _ in range(2^12)]
        sage: l = [vector(v.list() + [S.count(v)]) for v in set(S)]
        sage: list_plot3d(l, point_list=True, interpolation='nn')                       # needs sage.plot
        Graphics3d Object

    REFERENCES:

    - [GPV2008]_

    .. automethod:: __init__
    .. automethod:: __call__
    """
    @staticmethod
    def compute_precision(precision, sigma):
        """
        Compute precision to use.

        INPUT:

        - ``precision`` -- integer `>= 53` nor ``None``
        - ``sigma`` -- if ``precision`` is ``None`` then the precision of
          ``sigma`` is used

        EXAMPLES::

            sage: DGL = distributions.DiscreteGaussianDistributionLatticeSampler
            sage: DGL.compute_precision(100, RR(3))
            100
            sage: DGL.compute_precision(100, RealField(200)(3))
            100
            sage: DGL.compute_precision(100, 3)
            100
            sage: DGL.compute_precision(None, RR(3))
            53
            sage: DGL.compute_precision(None, RealField(200)(3))
            200
            sage: DGL.compute_precision(None, 3)
            53
        """
    is_spherical: bool
    n: Incomplete
    B: Incomplete
    Q: Incomplete
    D: Incomplete
    VS: Incomplete
    r: Incomplete
    def __init__(self, B, sigma: int = 1, c: int = 0, r=None, precision=None, sigma_basis: bool = False) -> None:
        """
        Construct a discrete Gaussian sampler over the lattice `\\Lambda(B)`
        with parameter ``sigma`` and center `c`.

        INPUT:

        - ``B`` -- a (row) basis for the lattice, one of the following:

          - an integer matrix,
          - an object with a ``.matrix()`` method, e.g. ``ZZ^n``, or
          - an object where ``matrix(B)`` succeeds, e.g. a list of vectors

        - ``sigma`` -- Gaussian parameter, one of the following:

          - a real number `\\sigma > 0` (spherical),
          - a positive definite matrix `\\Sigma` (non-spherical), or
          - any matrix-like ``S``, equivalent to `\\Sigma = SS^T`, when
            ``sigma_basis`` is set

        - ``c`` -- (default: 0) center `c`, any vector in `\\ZZ^n` is
          supported, but `c \\in \\Lambda(B)` is faster

        - ``r`` -- (default: ``None``) rounding parameter `r` as defined in
          [Pei2010]_; ignored for spherical Gaussian parameter; if not provided,
          set to be the maximal possible such that `\\Sigma - rBB^T` is positive
          definite
        - ``precision`` -- bit precision `\\geq 53`
        - ``sigma_basis`` -- boolean (default: ``False``); when set, ``sigma`` is treated as
            a (row) basis, i.e. the covariance matrix is computed by `\\Sigma = SS^T`

        .. TODO::

            Rename class methods like ``.f`` and hide most of them
            (at least behind something like ``.data``).

        EXAMPLES::

            sage: n = 2; sigma = 3.0
            sage: D = distributions.DiscreteGaussianDistributionLatticeSampler(ZZ^n, sigma)
            sage: f = D.f
            sage: nf = D._normalisation_factor_zz(); nf                                 # needs sage.symbolic
            56.5486677646...

            sage: from collections import defaultdict
            sage: counter = defaultdict(Integer); m = 0
            sage: def add_samples(i):
            ....:     global counter, m
            ....:     for _ in range(i):
            ....:         counter[D()] += 1
            ....:         m += 1

            sage: v = vector(ZZ, n, (-3, -3))
            sage: v.set_immutable()
            sage: while v not in counter: add_samples(1000)
            sage: while abs(m*f(v)*1.0/nf/counter[v] - 1.0) >= 0.1:                     # needs sage.symbolic
            ....:     add_samples(1000)

            sage: counter = defaultdict(Integer); m = 0
            sage: v = vector(ZZ, n, (0, 0))
            sage: v.set_immutable()
            sage: while v not in counter:
            ....:     add_samples(1000)
            sage: while abs(m*f(v)*1.0/nf/counter[v] - 1.0) >= 0.1:                     # needs sage.symbolic
            ....:     add_samples(1000)

        Spherical covariance are automatically handled::

            sage: distributions.DiscreteGaussianDistributionLatticeSampler(ZZ^3, sigma=Matrix(3, 3, 2))
            Discrete Gaussian sampler with Gaussian parameter σ = 2.00000000000000, c=(0, 0, 0) over lattice with basis
            <BLANKLINE>
            [1 0 0]
            [0 1 0]
            [0 0 1]

        The sampler supports non-spherical covariance in the form of a Gram
        matrix::

            sage: n = 3
            sage: Sigma = Matrix(ZZ, [[5, -2, 4], [-2, 10, -5], [4, -5, 5]])
            sage: c = vector(ZZ, [7, 2, 5])
            sage: D = distributions.DiscreteGaussianDistributionLatticeSampler(ZZ^n, Sigma, c)
            sage: f = D.f
            sage: nf = D._normalisation_factor_zz(); nf # This has not been properly implemented
            78.6804...

        We can compute the expected number of samples before sampling a vector::

            sage: v = vector(ZZ, n, (11, 4, 8))
            sage: v.set_immutable()
            sage: 1 / (f(v) / nf)
            2553.9461...

            sage: counter = defaultdict(Integer); m = 0
            sage: while v not in counter:
            ....:     add_samples(1000)
            sage: sum(counter.values())  # random
            3000
            sage: while abs(m*f(v)*1.0/nf/counter[v] - 1.0) >= 0.1:                     # needs sage.symbolic
            ....:     add_samples(1000)

        If the covariance provided is not positive definite, an error is thrown::

            sage: Sigma = Matrix(ZZ, [[0, 1], [1, 0]])
            sage: distributions.DiscreteGaussianDistributionLatticeSampler(ZZ^2, Sigma)
            Traceback (most recent call last):
            ...
            RuntimeError: Sigma(=[0.000000000000000  1.00000000000000]
            [ 1.00000000000000 0.000000000000000]) is not positive definite

        The sampler supports passing a basis for the covariance::

            sage: n = 3
            sage: S = Matrix(ZZ, [[2, 0, 0], [-1, 3, 0], [2, -1, 1]])
            sage: D = distributions.DiscreteGaussianDistributionLatticeSampler(ZZ^n, S, sigma_basis=True)
            sage: D.sigma()
            [ 4.00000000000000 -2.00000000000000  4.00000000000000]
            [-2.00000000000000  10.0000000000000 -5.00000000000000]
            [ 4.00000000000000 -5.00000000000000  6.00000000000000]

        The non-spherical sampler supports offline computation to speed up
        sampling. This will be useful when changing the center `c` is supported.
        The difference is more significant for larger matrices. For 128x128 we
        observe a 4x speedup (86s -> 20s)::

            sage: D.offline_samples = []
            sage: T = 2**12
            sage: L = [D() for _ in range(T)] # 560ms
            sage: D.add_offline_samples(T)    # 150ms
            sage: L = [D() for _ in range(T)] # 370ms

        We can also initialise with matrix-like objects::

            sage: qf = matrix(3, [2, 1, 1,  1, 2, 1,  1, 1, 2])
            sage: D = distributions.DiscreteGaussianDistributionLatticeSampler(qf, 3.0); D
            Discrete Gaussian sampler with Gaussian parameter σ = 3.00000000000000, c=(0, 0, 0) over lattice with basis
            <BLANKLINE>
            [2 1 1]
            [1 2 1]
            [1 1 2]
            sage: D().parent() is D.c().parent()
            True
        """
    def __call__(self):
        """
        Return a new sample.

        EXAMPLES::

            sage: D = distributions.DiscreteGaussianDistributionLatticeSampler(ZZ^3, 3.0, c=(1,0,0))
            sage: L = [D() for _ in range(2^12)]
            sage: mean_L = sum(L) / len(L)
            sage: norm(mean_L.n() - D.c()) < 0.25
            True

            sage: D = distributions.DiscreteGaussianDistributionLatticeSampler(ZZ^3, 3.0, c=(1/2,0,0))
            sage: L = [D() for _ in range(2^12)]    # long time
            sage: mean_L = sum(L) / len(L)          # long time
            sage: norm(mean_L.n() - D.c()) < 0.25   # long time
            True

            sage: import numpy
            sage: M = matrix(ZZ, [[1,2],[0,1]])
            sage: D = distributions.DiscreteGaussianDistributionLatticeSampler(M, 20.0)
            sage: L = [D() for _ in range(2^12)]                                               # long time
            sage: div = numpy.mean([abs(x) for x,y in L]) / numpy.mean([abs(y) for x,y, in L]) # long time
            sage: 0.9 < div < 1.1                                                              # long time
            True

        """
    def f(self, x):
        """
        Compute the Gaussian `\\rho_{\\Lambda, c, \\Sigma}`.

        EXAMPLES::

            sage: Sigma = Matrix(ZZ, [[5, -2, 4], [-2, 10, -5], [4, -5, 5]])
            sage: D = distributions.DiscreteGaussianDistributionLatticeSampler(ZZ^3, Sigma)
            sage: D.f([1, 0, 1])
            0.802518797962478
            sage: D.f([1, 0, 3])
            0.00562800641440405
        """
    def sigma(self):
        """
        Gaussian parameter `\\sigma`.

        If `\\sigma` is a real number, samples from this sampler will have expected norm
        `\\sqrt{n}\\sigma` where `n` is the dimension of the lattice.

        EXAMPLES::

            sage: D = distributions.DiscreteGaussianDistributionLatticeSampler(ZZ^3, 3.0, c=(1,0,0))
            sage: D.sigma()
            3.00000000000000
        """
    def c(self):
        """
        Center `c`.

        Samples from this sampler will be centered at `c`.

        EXAMPLES::

            sage: D = distributions.DiscreteGaussianDistributionLatticeSampler(ZZ^3, 3.0, c=(1,0,0)); D
            Discrete Gaussian sampler with Gaussian parameter σ = 3.00000000000000, c=(1, 0, 0) over lattice with basis
            <BLANKLINE>
            [1 0 0]
            [0 1 0]
            [0 0 1]

            sage: D.c()
            (1, 0, 0)
        """
    def set_c(self, c) -> None:
        """
        Modifies center `c`.

        EXAMPLES::

            sage: D = distributions.DiscreteGaussianDistributionLatticeSampler(ZZ^3, 3.0, c=(1,0,0))
            sage: D.set_c((2, 0, 0))
            sage: D
            Discrete Gaussian sampler with Gaussian parameter σ = 3.00000000000000, c=(2, 0, 0) over lattice with basis
            <BLANKLINE>
            [1 0 0]
            [0 1 0]
            [0 0 1]
        """
    def add_offline_samples(self, cnt: int = 1) -> None:
        """
        Precompute samples from `B^{-1}D_1` to be used in :meth:`_call_non_spherical`.

        EXAMPLES::

            sage: Sigma = Matrix([[5, -2, 4], [-2, 10, -5], [4, -5, 5]])
            sage: D = distributions.DiscreteGaussianDistributionLatticeSampler(ZZ^3, Sigma)
            sage: assert not D.is_spherical
            sage: D.add_offline_samples(2^12)
            sage: L = [D() for _ in range(2^12)] # Takes less time
        """
