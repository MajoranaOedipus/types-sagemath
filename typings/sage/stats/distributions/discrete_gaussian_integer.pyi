import sage.structure.sage_object
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar

class DiscreteGaussianDistributionIntegerSampler(sage.structure.sage_object.SageObject):
    """DiscreteGaussianDistributionIntegerSampler(sigma, c=0, tau=6, algorithm=None, precision='mp')

    File: /build/sagemath/src/sage/src/sage/stats/distributions/discrete_gaussian_integer.pyx (starting at line 154)

    A Discrete Gaussian Sampler using rejection sampling.

    .. automethod:: __init__
    .. automethod:: __call__"""
    table_cutoff: ClassVar[int] = ...
    algorithm: File
    c: File
    sigma: File
    tau: File
    def __init__(self, sigma, c=..., tau=..., algorithm=..., precision=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/stats/distributions/discrete_gaussian_integer.pyx (starting at line 165)

                Construct a new sampler for a discrete Gaussian distribution.

                INPUT:

                - ``sigma`` -- samples `x` are accepted with probability proportional to
                  `\\exp(-(x-c)²/(2σ²))`

                - ``c`` -- the mean of the distribution. The value of ``c`` does not have
                  to be an integer. However, some algorithms only support integer-valued
                  ``c`` (default: ``0``)

                - ``tau`` -- samples outside the range `(⌊c⌉-⌈στ⌉,...,⌊c⌉+⌈στ⌉)` are
                  considered to have probability zero. This bound applies to algorithms which
                  sample from the uniform distribution (default: ``6``)

                - ``algorithm`` -- see list below (default: ``'uniform+table'`` for
                   `σt` bounded by ``DiscreteGaussianDistributionIntegerSampler.table_cutoff`` and
                   ``'uniform+online'`` for bigger `στ`)

                - ``precision`` -- either ``'mp'`` for multi-precision where the actual
                  precision used is taken from sigma or ``'dp'`` for double precision. In
                  the latter case results are not reproducible. (default: ``'mp'``)

                ALGORITHMS:

                - ``'uniform+table'`` -- classical rejection sampling, sampling from the
                  uniform distribution and accepted with probability proportional to
                  `\\exp(-(x-c)²/(2σ²))` where `\\exp(-(x-c)²/(2σ²))` is precomputed and
                  stored in a table. Any real-valued `c` is supported.

                - ``'uniform+logtable'`` -- samples are drawn from a uniform distribution and
                  accepted with probability proportional to `\\exp(-(x-c)²/(2σ²))` where
                  `\\exp(-(x-c)²/(2σ²))` is computed using logarithmically many calls to
                  Bernoulli distributions. See [DDLL2013]_ for details.  Only
                  integer-valued `c` are supported.

                - ``'uniform+online'`` -- samples are drawn from a uniform distribution and
                  accepted with probability proportional to `\\exp(-(x-c)²/(2σ²))` where
                  `\\exp(-(x-c)²/(2σ²))` is computed in each invocation. Typically this
                  is very slow.  See [DDLL2013]_ for details.  Any real-valued `c` is
                  accepted.

                - ``'sigma2+logtable'`` -- samples are drawn from an easily samplable
                  distribution with `σ = k·σ_2` with `σ_2 = \\sqrt{1/(2\\log 2)}` and accepted
                  with probability proportional to `\\exp(-(x-c)²/(2σ²))` where
                  `\\exp(-(x-c)²/(2σ²))` is computed using  logarithmically many calls to Bernoulli
                  distributions (but no calls to `\\exp`). See [DDLL2013]_ for details. Note that this
                  sampler adjusts `σ` to match `k·σ_2` for some integer `k`.
                  Only integer-valued `c` are supported.

                EXAMPLES::

                    sage: from sage.stats.distributions.discrete_gaussian_integer import DiscreteGaussianDistributionIntegerSampler
                    sage: DiscreteGaussianDistributionIntegerSampler(3.0, algorithm='uniform+online')
                    Discrete Gaussian sampler over the Integers with sigma = 3.000000 and c = 0.000000
                    sage: DiscreteGaussianDistributionIntegerSampler(3.0, algorithm='uniform+table')
                    Discrete Gaussian sampler over the Integers with sigma = 3.000000 and c = 0.000000
                    sage: DiscreteGaussianDistributionIntegerSampler(3.0, algorithm='uniform+logtable')
                    Discrete Gaussian sampler over the Integers with sigma = 3.000000 and c = 0.000000

                Note that ``'sigma2+logtable'`` adjusts `σ`::

                    sage: DiscreteGaussianDistributionIntegerSampler(3.0, algorithm='sigma2+logtable')
                    Discrete Gaussian sampler over the Integers with sigma = 3.397287 and c = 0.000000

                TESTS:

                We are testing invalid inputs::

                    sage: from sage.stats.distributions.discrete_gaussian_integer import DiscreteGaussianDistributionIntegerSampler
                    sage: DiscreteGaussianDistributionIntegerSampler(-3.0)
                    Traceback (most recent call last):
                    ...
                    ValueError: sigma must be > 0.0 but got -3.000000

                    sage: DiscreteGaussianDistributionIntegerSampler(3.0, tau=-1)
                    Traceback (most recent call last):
                    ...
                    ValueError: tau must be >= 1 but got -1

                    sage: DiscreteGaussianDistributionIntegerSampler(3.0, tau=2, algorithm='superfastalgorithmyouneverheardof')
                    Traceback (most recent call last):
                    ...
                    ValueError: Algorithm 'superfastalgorithmyouneverheardof' not supported by class 'DiscreteGaussianDistributionIntegerSampler'

                    sage: DiscreteGaussianDistributionIntegerSampler(3.0, c=1.5, algorithm='sigma2+logtable')
                    Traceback (most recent call last):
                    ...
                    ValueError: algorithm 'uniform+logtable' requires c%1 == 0

                We are testing correctness for multi-precision::

                    sage: def add_samples(i):
                    ....:     global mini, maxi, s, n
                    ....:     for _ in range(i):
                    ....:         x = D()
                    ....:         s += x
                    ....:         maxi = max(maxi, x)
                    ....:         mini = min(mini, x)
                    ....:         n += 1

                    sage: from sage.stats.distributions.discrete_gaussian_integer import DiscreteGaussianDistributionIntegerSampler
                    sage: D = DiscreteGaussianDistributionIntegerSampler(1.0, c=0, tau=2)
                    sage: mini = 1000; maxi = -1000; s = 0; n = 0
                    sage: add_samples(2^16)
                    sage: while mini != 0 - 2*1.0 or maxi != 0 + 2*1.0 or abs(float(s)/n) >= 0.01:
                    ....:     add_samples(2^16)

                    sage: D = DiscreteGaussianDistributionIntegerSampler(1.0, c=2.5, tau=2)
                    sage: mini = 1000; maxi = -1000; s = 0; n = 0
                    sage: add_samples(2^16)
                    sage: while mini != 2 - 2*1.0 or maxi != 2 + 2*1.0 or abs(float(s)/n - 2.45) >= 0.01:
                    ....:     add_samples(2^16)

                    sage: D = DiscreteGaussianDistributionIntegerSampler(1.0, c=2.5, tau=6)
                    sage: mini = 1000; maxi = -1000; s = 0; n = 0
                    sage: add_samples(2^18)
                    sage: while mini > 2 - 4*1.0 or maxi < 2 + 5*1.0 or abs(float(s)/n - 2.5) >= 0.01:  # long time
                    ....:     add_samples(2^18)

                We are testing correctness for double precision::

                    sage: def add_samples(i):
                    ....:     global mini, maxi, s, n
                    ....:     for _ in range(i):
                    ....:         x = D()
                    ....:         s += x
                    ....:         maxi = max(maxi, x)
                    ....:         mini = min(mini, x)
                    ....:         n += 1

                    sage: from sage.stats.distributions.discrete_gaussian_integer import DiscreteGaussianDistributionIntegerSampler
                    sage: D = DiscreteGaussianDistributionIntegerSampler(1.0, c=0, tau=2, precision='dp')
                    sage: mini = 1000; maxi = -1000; s = 0; n = 0
                    sage: add_samples(2^16)
                    sage: while mini != 0 - 2*1.0 or maxi != 0 + 2*1.0 or abs(float(s)/n) >= 0.05:
                    ....:     add_samples(2^16)

                    sage: D = DiscreteGaussianDistributionIntegerSampler(1.0, c=2.5, tau=2, precision='dp')
                    sage: mini = 1000; maxi = -1000; s = 0; n = 0
                    sage: add_samples(2^16)
                    sage: while mini != 2 - 2*1.0 or maxi != 2 + 2*1.0 or abs(float(s)/n - 2.45) >= 0.01:
                    ....:     add_samples(2^16)

                    sage: D = DiscreteGaussianDistributionIntegerSampler(1.0, c=2.5, tau=6, precision='dp')
                    sage: mini = 1000; maxi = -1000; s = 0; n = 0
                    sage: add_samples(2^16)
                    sage: while mini > -1 or maxi < 6 or abs(float(s)/n - 2.5) >= 0.1:
                    ....:     add_samples(2^16)

                We plot a histogram::

                    sage: from sage.stats.distributions.discrete_gaussian_integer import DiscreteGaussianDistributionIntegerSampler
                    sage: D = DiscreteGaussianDistributionIntegerSampler(17.0)
                    sage: S = [D() for _ in range(2^16)]
                    sage: list_plot([(v,S.count(v)) for v in set(S)])  # long time
                    Graphics object consisting of 1 graphics primitive

                These generators cache random bits for performance reasons. Hence, resetting
                the seed of the PRNG might not have the expected outcome. You can flush this cache with
                ``_flush_cache()``::

                    sage: from sage.stats.distributions.discrete_gaussian_integer import DiscreteGaussianDistributionIntegerSampler
                    sage: D = DiscreteGaussianDistributionIntegerSampler(3.0)
                    sage: sage.misc.randstate.set_random_seed(0); D()
                    3
                    sage: sage.misc.randstate.set_random_seed(0); D()
                    3
                    sage: sage.misc.randstate.set_random_seed(0); D._flush_cache(); D()
                    3

                    sage: D = DiscreteGaussianDistributionIntegerSampler(3.0)
                    sage: sage.misc.randstate.set_random_seed(0); D()
                    3
                    sage: sage.misc.randstate.set_random_seed(0); D()
                    3
                    sage: sage.misc.randstate.set_random_seed(0); D()
                    -3
        """
    def __call__(self) -> Any:
        """DiscreteGaussianDistributionIntegerSampler.__call__(self)

        File: /build/sagemath/src/sage/src/sage/stats/distributions/discrete_gaussian_integer.pyx (starting at line 454)

        Return a new sample.

        EXAMPLES::

            sage: from sage.stats.distributions.discrete_gaussian_integer import DiscreteGaussianDistributionIntegerSampler
            sage: DiscreteGaussianDistributionIntegerSampler(3.0, algorithm='uniform+online')()  # random
            -3
            sage: DiscreteGaussianDistributionIntegerSampler(3.0, algorithm='uniform+table')()  # random
            3

        TESTS::

            sage: from sage.stats.distributions.discrete_gaussian_integer import DiscreteGaussianDistributionIntegerSampler
            sage: DiscreteGaussianDistributionIntegerSampler(3.0, algorithm='uniform+logtable', precision='dp')() # random output
            13"""
