import sage as sage
import sage.misc.prandom as random
from sage.modules.free_module_element import vector as vector
from typing import Any, overload

class GeneralDiscreteDistribution(ProbabilityDistribution):
    """GeneralDiscreteDistribution(P, rng='default', seed=None)

    File: /build/sagemath/src/sage/src/sage/probability/probability_distribution.pyx (starting at line 1034)

    Create a discrete probability distribution.

    INPUT:

    - ``P`` -- list of probabilities; the list will automatically be
      normalised if ``sum(P)`` is not equal to 1

    - ``rng`` -- (optional) random number generator to use; may be
      one of ``'default'``, ``'luxury'``, or ``'taus'``

    - ``seed`` -- (optional) seed to use with the random number
      generator

    OUTPUT: a probability distribution where the probability of selecting
    ``x`` is ``P[x]``.

    EXAMPLES:

    Construct a ``GeneralDiscreteDistribution`` with the probability
    distribution `P` where `P(0) = 0.3`, `P(1) = 0.4`, `P(2) = 0.3`::

        sage: P = [0.3, 0.4, 0.3]
        sage: X = GeneralDiscreteDistribution(P)
        sage: X.get_random_element() in (0, 1, 2)
        True

    Checking the distribution of samples::

        sage: P = [0.3, 0.4, 0.3]
        sage: counts = [0] * len(P)
        sage: X = GeneralDiscreteDistribution(P)
        sage: nr_samples = 10000
        sage: for _ in range(nr_samples):
        ....:     counts[X.get_random_element()] += 1
        sage: [1.0*x/nr_samples for x in counts]  # abs tol 3e-2
        [0.3, 0.4, 0.3]

    The distribution probabilities will automatically be normalised::

        sage: P = [0.1, 0.3]
        sage: X = GeneralDiscreteDistribution(P, seed=0)
        sage: counts = [0, 0]
        sage: for _ in range(10000):
        ....:     counts[X.get_random_element()] += 1
        sage: float(counts[1]/counts[0])
        3.042037186742118

    TESTS:

    Make sure that repeated initializations are randomly seeded
    (:issue:`9770`)::

        sage: P = [0.001] * 1000
        sage: Xs = [GeneralDiscreteDistribution(P).get_random_element() for _ in range(1000)]
        sage: len(set(Xs)) > 2^^32
        True

    The distribution probabilities must be nonnegative::

        sage: GeneralDiscreteDistribution([0.1, -0.1])
        Traceback (most recent call last):
        ...
        ValueError: The distribution probabilities must be nonnegative"""
    @overload
    def __init__(self, P, rng=..., seed=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/probability/probability_distribution.pyx (starting at line 1105)

                Given a list of probabilities P construct an instance of a gsl
                discrete random variable generator.

                EXAMPLES::

                    sage: P = [0.3, 0.4, 0.3]
                    sage: X = GeneralDiscreteDistribution(P)
                    sage: assert X.get_random_element() in range(len(P))

                TESTS:

                Until :issue:`15089` a value of the ``seed`` keyword
                besides ``None`` was ignored. We check here that setting
                a seed is effective. ::

                    sage: P = [0.2, 0.3, 0.1, 0.4]
                    sage: T = GeneralDiscreteDistribution(P, seed=876)
                    sage: one = [T.get_random_element() for _ in range(50)]
                    sage: T = GeneralDiscreteDistribution(P, seed=876)
                    sage: two = [T.get_random_element() for _ in range(50)]
                    sage: T = GeneralDiscreteDistribution(P, seed=123)
                    sage: three = [T.get_random_element() for _ in range(50)]
                    sage: one == two
                    True
                    sage: one == three
                    False

                Testing that :issue:`24416` is fixed for when entries are larger
                than `2^{1024}`::

                    sage: from collections import Counter
                    sage: X = GeneralDiscreteDistribution([1,2,2^1024])
                    sage: Counter(X.get_random_element() for _ in range(100))
                    Counter({2: 100})
        """
    @overload
    def __init__(self, P) -> Any:
        """File: /build/sagemath/src/sage/src/sage/probability/probability_distribution.pyx (starting at line 1105)

                Given a list of probabilities P construct an instance of a gsl
                discrete random variable generator.

                EXAMPLES::

                    sage: P = [0.3, 0.4, 0.3]
                    sage: X = GeneralDiscreteDistribution(P)
                    sage: assert X.get_random_element() in range(len(P))

                TESTS:

                Until :issue:`15089` a value of the ``seed`` keyword
                besides ``None`` was ignored. We check here that setting
                a seed is effective. ::

                    sage: P = [0.2, 0.3, 0.1, 0.4]
                    sage: T = GeneralDiscreteDistribution(P, seed=876)
                    sage: one = [T.get_random_element() for _ in range(50)]
                    sage: T = GeneralDiscreteDistribution(P, seed=876)
                    sage: two = [T.get_random_element() for _ in range(50)]
                    sage: T = GeneralDiscreteDistribution(P, seed=123)
                    sage: three = [T.get_random_element() for _ in range(50)]
                    sage: one == two
                    True
                    sage: one == three
                    False

                Testing that :issue:`24416` is fixed for when entries are larger
                than `2^{1024}`::

                    sage: from collections import Counter
                    sage: X = GeneralDiscreteDistribution([1,2,2^1024])
                    sage: Counter(X.get_random_element() for _ in range(100))
                    Counter({2: 100})
        """
    @overload
    def __init__(self, P) -> Any:
        """File: /build/sagemath/src/sage/src/sage/probability/probability_distribution.pyx (starting at line 1105)

                Given a list of probabilities P construct an instance of a gsl
                discrete random variable generator.

                EXAMPLES::

                    sage: P = [0.3, 0.4, 0.3]
                    sage: X = GeneralDiscreteDistribution(P)
                    sage: assert X.get_random_element() in range(len(P))

                TESTS:

                Until :issue:`15089` a value of the ``seed`` keyword
                besides ``None`` was ignored. We check here that setting
                a seed is effective. ::

                    sage: P = [0.2, 0.3, 0.1, 0.4]
                    sage: T = GeneralDiscreteDistribution(P, seed=876)
                    sage: one = [T.get_random_element() for _ in range(50)]
                    sage: T = GeneralDiscreteDistribution(P, seed=876)
                    sage: two = [T.get_random_element() for _ in range(50)]
                    sage: T = GeneralDiscreteDistribution(P, seed=123)
                    sage: three = [T.get_random_element() for _ in range(50)]
                    sage: one == two
                    True
                    sage: one == three
                    False

                Testing that :issue:`24416` is fixed for when entries are larger
                than `2^{1024}`::

                    sage: from collections import Counter
                    sage: X = GeneralDiscreteDistribution([1,2,2^1024])
                    sage: Counter(X.get_random_element() for _ in range(100))
                    Counter({2: 100})
        """
    @overload
    def __init__(self, P, seed=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/probability/probability_distribution.pyx (starting at line 1105)

                Given a list of probabilities P construct an instance of a gsl
                discrete random variable generator.

                EXAMPLES::

                    sage: P = [0.3, 0.4, 0.3]
                    sage: X = GeneralDiscreteDistribution(P)
                    sage: assert X.get_random_element() in range(len(P))

                TESTS:

                Until :issue:`15089` a value of the ``seed`` keyword
                besides ``None`` was ignored. We check here that setting
                a seed is effective. ::

                    sage: P = [0.2, 0.3, 0.1, 0.4]
                    sage: T = GeneralDiscreteDistribution(P, seed=876)
                    sage: one = [T.get_random_element() for _ in range(50)]
                    sage: T = GeneralDiscreteDistribution(P, seed=876)
                    sage: two = [T.get_random_element() for _ in range(50)]
                    sage: T = GeneralDiscreteDistribution(P, seed=123)
                    sage: three = [T.get_random_element() for _ in range(50)]
                    sage: one == two
                    True
                    sage: one == three
                    False

                Testing that :issue:`24416` is fixed for when entries are larger
                than `2^{1024}`::

                    sage: from collections import Counter
                    sage: X = GeneralDiscreteDistribution([1,2,2^1024])
                    sage: Counter(X.get_random_element() for _ in range(100))
                    Counter({2: 100})
        """
    @overload
    def __init__(self, P) -> Any:
        """File: /build/sagemath/src/sage/src/sage/probability/probability_distribution.pyx (starting at line 1105)

                Given a list of probabilities P construct an instance of a gsl
                discrete random variable generator.

                EXAMPLES::

                    sage: P = [0.3, 0.4, 0.3]
                    sage: X = GeneralDiscreteDistribution(P)
                    sage: assert X.get_random_element() in range(len(P))

                TESTS:

                Until :issue:`15089` a value of the ``seed`` keyword
                besides ``None`` was ignored. We check here that setting
                a seed is effective. ::

                    sage: P = [0.2, 0.3, 0.1, 0.4]
                    sage: T = GeneralDiscreteDistribution(P, seed=876)
                    sage: one = [T.get_random_element() for _ in range(50)]
                    sage: T = GeneralDiscreteDistribution(P, seed=876)
                    sage: two = [T.get_random_element() for _ in range(50)]
                    sage: T = GeneralDiscreteDistribution(P, seed=123)
                    sage: three = [T.get_random_element() for _ in range(50)]
                    sage: one == two
                    True
                    sage: one == three
                    False

                Testing that :issue:`24416` is fixed for when entries are larger
                than `2^{1024}`::

                    sage: from collections import Counter
                    sage: X = GeneralDiscreteDistribution([1,2,2^1024])
                    sage: Counter(X.get_random_element() for _ in range(100))
                    Counter({2: 100})
        """
    @overload
    def get_random_element(self) -> Any:
        """GeneralDiscreteDistribution.get_random_element(self)

        File: /build/sagemath/src/sage/src/sage/probability/probability_distribution.pyx (starting at line 1209)

        Get a random sample from the probability distribution.

        EXAMPLES::

            sage: P = [0.3, 0.4, 0.3]
            sage: X = GeneralDiscreteDistribution(P)
            sage: all(X.get_random_element() in (0,1,2) for _ in range(10))
            True
            sage: isinstance(X.get_random_element(), sage.rings.integer.Integer)
            True"""
    @overload
    def get_random_element(self) -> Any:
        """GeneralDiscreteDistribution.get_random_element(self)

        File: /build/sagemath/src/sage/src/sage/probability/probability_distribution.pyx (starting at line 1209)

        Get a random sample from the probability distribution.

        EXAMPLES::

            sage: P = [0.3, 0.4, 0.3]
            sage: X = GeneralDiscreteDistribution(P)
            sage: all(X.get_random_element() in (0,1,2) for _ in range(10))
            True
            sage: isinstance(X.get_random_element(), sage.rings.integer.Integer)
            True"""
    @overload
    def get_random_element(self) -> Any:
        """GeneralDiscreteDistribution.get_random_element(self)

        File: /build/sagemath/src/sage/src/sage/probability/probability_distribution.pyx (starting at line 1209)

        Get a random sample from the probability distribution.

        EXAMPLES::

            sage: P = [0.3, 0.4, 0.3]
            sage: X = GeneralDiscreteDistribution(P)
            sage: all(X.get_random_element() in (0,1,2) for _ in range(10))
            True
            sage: isinstance(X.get_random_element(), sage.rings.integer.Integer)
            True"""
    @overload
    def reset_distribution(self) -> Any:
        """GeneralDiscreteDistribution.reset_distribution(self)

        File: /build/sagemath/src/sage/src/sage/probability/probability_distribution.pyx (starting at line 1224)

        This method resets the distribution.

        EXAMPLES::

            sage: T = GeneralDiscreteDistribution([0.1, 0.3, 0.6])
            sage: T.set_seed(0)
            sage: [T.get_random_element() for _ in range(10)]
            [2, 2, 2, 2, 2, 1, 2, 2, 1, 2]
            sage: T.reset_distribution()
            sage: [T.get_random_element() for _ in range(10)]
            [2, 2, 2, 2, 2, 1, 2, 2, 1, 2]"""
    @overload
    def reset_distribution(self) -> Any:
        """GeneralDiscreteDistribution.reset_distribution(self)

        File: /build/sagemath/src/sage/src/sage/probability/probability_distribution.pyx (starting at line 1224)

        This method resets the distribution.

        EXAMPLES::

            sage: T = GeneralDiscreteDistribution([0.1, 0.3, 0.6])
            sage: T.set_seed(0)
            sage: [T.get_random_element() for _ in range(10)]
            [2, 2, 2, 2, 2, 1, 2, 2, 1, 2]
            sage: T.reset_distribution()
            sage: [T.get_random_element() for _ in range(10)]
            [2, 2, 2, 2, 2, 1, 2, 2, 1, 2]"""
    def set_random_number_generator(self, rng=...) -> Any:
        """GeneralDiscreteDistribution.set_random_number_generator(self, rng='default')

        File: /build/sagemath/src/sage/src/sage/probability/probability_distribution.pyx (starting at line 1184)

        Set the random number generator to be used by gsl.

        EXAMPLES::

            sage: X = GeneralDiscreteDistribution([0.3, 0.4, 0.3])
            sage: X.set_random_number_generator('taus')"""
    def set_seed(self, seed) -> Any:
        """GeneralDiscreteDistribution.set_seed(self, seed)

        File: /build/sagemath/src/sage/src/sage/probability/probability_distribution.pyx (starting at line 1170)

        Set the seed to be used by the random number generator.

        EXAMPLES::

            sage: X = GeneralDiscreteDistribution([0.3, 0.4, 0.3])
            sage: X.set_seed(1)
            sage: X.get_random_element()
            1"""

class ProbabilityDistribution:
    """ProbabilityDistribution()

    File: /build/sagemath/src/sage/src/sage/probability/probability_distribution.pyx (starting at line 67)

    Concrete probability distributions should be derived from this
    abstract class."""
    def __init__(self) -> Any:
        """File: /build/sagemath/src/sage/src/sage/probability/probability_distribution.pyx (starting at line 73)

                To be implemented by a derived class::

                    sage: P = sage.probability.probability_distribution.ProbabilityDistribution()
        """
    @overload
    def generate_histogram_data(self, num_samples=..., bins=...) -> Any:
        """ProbabilityDistribution.generate_histogram_data(self, num_samples=1000, bins=50)

        File: /build/sagemath/src/sage/src/sage/probability/probability_distribution.pyx (starting at line 95)

        Compute a histogram of the probability distribution.

        INPUT:

        - ``num_samples`` -- (optional) number of times to sample from
          the probability distribution

        - ``bins`` -- (optional) number of bins to divide the samples
          into

        OUTPUT:

        - a tuple. The first element of the tuple is a list of length
          ``bins``, consisting of the normalised histogram of the random
          samples. The second list is the bins.

        EXAMPLES::

            sage: set_random_seed(0)
            sage: from sage.probability.probability_distribution import GeneralDiscreteDistribution
            sage: P = [0.3, 0.4, 0.3]
            sage: X = GeneralDiscreteDistribution(P)
            sage: h, b = X.generate_histogram_data(bins=10)                             # needs sage.plot
            sage: h  # rel tol 1e-08                                                    # needs sage.plot
            [1.6299999999999999,
             0.0,
             0.0,
             0.0,
             0.0,
             1.9049999999999985,
             0.0,
             0.0,
             0.0,
             1.4650000000000003]
            sage: b                                                                     # needs sage.plot
            [0.0,
             0.2,
             0.4,
             0.6000000000000001,
             0.8,
             1.0,
             1.2000000000000002,
             1.4000000000000001,
             1.6,
             1.8,
             2.0]"""
    @overload
    def generate_histogram_data(self, bins=...) -> Any:
        """ProbabilityDistribution.generate_histogram_data(self, num_samples=1000, bins=50)

        File: /build/sagemath/src/sage/src/sage/probability/probability_distribution.pyx (starting at line 95)

        Compute a histogram of the probability distribution.

        INPUT:

        - ``num_samples`` -- (optional) number of times to sample from
          the probability distribution

        - ``bins`` -- (optional) number of bins to divide the samples
          into

        OUTPUT:

        - a tuple. The first element of the tuple is a list of length
          ``bins``, consisting of the normalised histogram of the random
          samples. The second list is the bins.

        EXAMPLES::

            sage: set_random_seed(0)
            sage: from sage.probability.probability_distribution import GeneralDiscreteDistribution
            sage: P = [0.3, 0.4, 0.3]
            sage: X = GeneralDiscreteDistribution(P)
            sage: h, b = X.generate_histogram_data(bins=10)                             # needs sage.plot
            sage: h  # rel tol 1e-08                                                    # needs sage.plot
            [1.6299999999999999,
             0.0,
             0.0,
             0.0,
             0.0,
             1.9049999999999985,
             0.0,
             0.0,
             0.0,
             1.4650000000000003]
            sage: b                                                                     # needs sage.plot
            [0.0,
             0.2,
             0.4,
             0.6000000000000001,
             0.8,
             1.0,
             1.2000000000000002,
             1.4000000000000001,
             1.6,
             1.8,
             2.0]"""
    def generate_histogram_plot(self, name, num_samples=..., bins=...) -> Any:
        """ProbabilityDistribution.generate_histogram_plot(self, name, num_samples=1000, bins=50)

        File: /build/sagemath/src/sage/src/sage/probability/probability_distribution.pyx (starting at line 152)

        Save the histogram from :func:`generate_histogram_data() <sage.libs.gsl.ProbabilityDistribution.generate_histogram_data>`
        to a file.

        INPUT:

        - ``name`` -- file to save the histogram plot (as a PNG)

        - ``num_samples`` -- (optional) number of times to sample from
          the probability distribution

        - ``bins`` -- (optional) number of bins to divide the samples
          into

        EXAMPLES:

        This saves the histogram plot to a temporary file::

            sage: from sage.probability.probability_distribution import GeneralDiscreteDistribution
            sage: import tempfile
            sage: P = [0.3, 0.4, 0.3]
            sage: X = GeneralDiscreteDistribution(P)
            sage: with tempfile.NamedTemporaryFile() as f:                              # needs sage.plot
            ....:     X.generate_histogram_plot(f.name)"""
    @overload
    def get_random_element(self) -> Any:
        """ProbabilityDistribution.get_random_element(self)

        File: /build/sagemath/src/sage/src/sage/probability/probability_distribution.pyx (starting at line 82)

        To be implemented by a derived class::

            sage: P = sage.probability.probability_distribution.ProbabilityDistribution()
            sage: P.get_random_element()
            Traceback (most recent call last):
            ...
            NotImplementedError: implement in derived class"""
    @overload
    def get_random_element(self) -> Any:
        """ProbabilityDistribution.get_random_element(self)

        File: /build/sagemath/src/sage/src/sage/probability/probability_distribution.pyx (starting at line 82)

        To be implemented by a derived class::

            sage: P = sage.probability.probability_distribution.ProbabilityDistribution()
            sage: P.get_random_element()
            Traceback (most recent call last):
            ...
            NotImplementedError: implement in derived class"""

class RealDistribution(ProbabilityDistribution):
    """RealDistribution(type='uniform', parameters=None, rng='default', seed=None)

    File: /build/sagemath/src/sage/src/sage/probability/probability_distribution.pyx (starting at line 344)

    The :class:`RealDistribution` class provides a number of routines for sampling
    from and analyzing and visualizing probability distributions.
    For precise definitions of the distributions and their parameters
    see the gsl reference manuals chapter on random number generators
    and probability distributions.

    EXAMPLES:

    Uniform distribution on the interval ``[a, b]``::

        sage: a = 0
        sage: b = 2
        sage: T = RealDistribution('uniform', [a, b])
        sage: a <= T.get_random_element() <= b
        True
        sage: T.distribution_function(0)
        0.5
        sage: T.cum_distribution_function(1)
        0.5
        sage: T.cum_distribution_function_inv(.5)
        1.0

    The gaussian distribution takes 1 parameter ``sigma``. The standard
    gaussian distribution has ``sigma = 1``::

        sage: sigma = 1
        sage: T = RealDistribution('gaussian', sigma)
        sage: s = T.get_random_element()
        sage: s.parent()
        Real Double Field
        sage: T.distribution_function(0)
        0.3989422804014327
        sage: T.cum_distribution_function(1)
        0.8413447460685429
        sage: T.cum_distribution_function_inv(.5)
        0.0

    The rayleigh distribution has 1 parameter ``sigma``::

        sage: sigma = 3
        sage: T = RealDistribution('rayleigh', sigma)
        sage: s = T.get_random_element()
        sage: s >= 0
        True
        sage: s.parent()
        Real Double Field
        sage: T.distribution_function(0)
        0.0
        sage: T.cum_distribution_function(1)
        0.054040531093234534
        sage: T.cum_distribution_function_inv(.5)
        3.532230067546424...

    The lognormal distribution has two parameters ``sigma``
    and ``zeta``::

        sage: zeta = 0
        sage: sigma = 1
        sage: T = RealDistribution('lognormal', [zeta, sigma])
        sage: s = T.get_random_element()
        sage: s >= 0
        True
        sage: s.parent()
        Real Double Field
        sage: T.distribution_function(0)
        0.0
        sage: T.cum_distribution_function(1)
        0.5
        sage: T.cum_distribution_function_inv(.5)
        1.0

    The pareto distribution has two parameters ``a``, and ``b``::

        sage: a = 1
        sage: b = 1
        sage: T = RealDistribution('pareto', [a, b])
        sage: s = T.get_random_element()
        sage: s >= b
        True
        sage: s.parent()
        Real Double Field
        sage: T.distribution_function(0)
        0.0
        sage: T.cum_distribution_function(1)
        0.0
        sage: T.cum_distribution_function_inv(.5)
        2.0

    The t-distribution has one parameter ``nu``::

        sage: nu = 1
        sage: T = RealDistribution('t', nu)
        sage: s = T.get_random_element()
        sage: s.parent()
        Real Double Field
        sage: T.distribution_function(0)      # rel tol 1e-15
        0.3183098861837906
        sage: T.cum_distribution_function(1)  # rel tol 1e-15
        0.75
        sage: T.cum_distribution_function_inv(.5)
        0.0

    The F-distribution has two parameters ``nu1`` and ``nu2``::

        sage: nu1 = 9; nu2 = 17
        sage: F = RealDistribution('F', [nu1,nu2])
        sage: s = F.get_random_element()
        sage: s >= 0
        True
        sage: s.parent()
        Real Double Field
        sage: F.distribution_function(1)  # rel tol 1e-14
        0.6695025505192798
        sage: F.cum_distribution_function(3.68)  # rel tol 1e-14
        0.9899717772300652
        sage: F.cum_distribution_function_inv(0.99)  # rel tol 1e-14
        3.682241524045864

    The chi-squared distribution has one parameter ``nu``::

        sage: nu = 1
        sage: T = RealDistribution('chisquared', nu)
        sage: s = T.get_random_element()
        sage: s >= 0
        True
        sage: s.parent()
        Real Double Field
        sage: T.distribution_function(0)
        +infinity
        sage: T.cum_distribution_function(1)  # rel tol 1e-14
        0.6826894921370856
        sage: T.cum_distribution_function_inv(.5)  # rel tol 1e-14
        0.45493642311957305

    The exponential power distribution has two parameters ``a`` and
    ``b``::

        sage: a = 1
        sage: b = 2.5
        sage: T = RealDistribution('exppow', [a, b])
        sage: s = T.get_random_element()
        sage: s.parent()
        Real Double Field
        sage: T.distribution_function(0)  # rel tol 1e-14
        0.5635302489930136
        sage: T.cum_distribution_function(1)  # rel tol 1e-14
        0.940263052542855

    The beta distribution has two parameters ``a`` and ``b``::

        sage: a = 2
        sage: b = 2
        sage: T = RealDistribution('beta', [a, b])
        sage: s = T.get_random_element()
        sage: 0 <= s <= 1
        True
        sage: s.parent()
        Real Double Field
        sage: T.distribution_function(0)
        0.0
        sage: T.cum_distribution_function(1)
        1.0

    The exponential distribution has one parameter ``mu``::

        sage: mu = 2
        sage: T = RealDistribution('exponential', mu)
        sage: s = T.get_random_element()
        sage: 0 <= s
        True
        sage: s.parent()
        Real Double Field
        sage: T.distribution_function(0)
        0.5

    The gamma distribution has two parameters ``a`` and ``b``::

        sage: a = 2
        sage: b = 2
        sage: T = RealDistribution('gamma', [a, b])
        sage: s = T.get_random_element()
        sage: 0 <= s
        True
        sage: s.parent()
        Real Double Field
        sage: T.distribution_function(0)
        0.0

    The weibull distribution has two parameters ``a`` and ``b``::

        sage: a = 1
        sage: b = 1
        sage: T = RealDistribution('weibull', [a, b])
        sage: s = T.get_random_element()
        sage: s >= 0
        True
        sage: s.parent()
        Real Double Field
        sage: T.distribution_function(0)
        1.0
        sage: T.cum_distribution_function(1)
        0.6321205588285577
        sage: T.cum_distribution_function_inv(.5)
        0.6931471805599453

    It is possible to select which random number generator drives the
    sampling as well as the seed.  The default is the Mersenne
    twister. Also available are the RANDLXS algorithm and the
    Tausworthe generator (see the gsl reference manual for more
    details). These are all supposed to be simulation quality
    generators. For RANDLXS use ``rng='luxury'`` and for
    tausworth use ``rng='taus'``::

         sage: T = RealDistribution('gaussian', 1, rng='luxury', seed=10)

    To change the seed at a later time use ``set_seed``::

         sage: T.set_seed(100)

    TESTS:

    Make sure that repeated initializations are randomly seeded
    (:issue:`9770`)::

        sage: Xs = [RealDistribution('gaussian', 1).get_random_element() for _ in range(1000)]
        sage: len(set(Xs)) > 2^^32
        True"""
    def __init__(self, type=..., parameters=..., rng=..., seed=...) -> Any:
        '''File: /build/sagemath/src/sage/src/sage/probability/probability_distribution.pyx (starting at line 584)

                EXAMPLES::

                    sage: T = RealDistribution(\'gaussian\', 1, seed=0)
                    sage: T.get_random_element()  # rel tol 4e-16
                    0.13391860811867587

                TESTS:

                Until :issue:`15089` a value of the ``seed`` keyword
                besides ``None`` was ignored. We check here that setting
                a seed is effective. ::

                    sage: T = RealDistribution("beta",[1.6,4.3], seed=876)
                    sage: one = [T.get_random_element() for _ in range(10)]
                    sage: T = RealDistribution("beta",[1.6,4.3], seed=876)
                    sage: two = [T.get_random_element() for _ in range(10)]
                    sage: T = RealDistribution("beta",[1.6,4.3], seed=123)
                    sage: three = [T.get_random_element() for _ in range(10)]
                    sage: one == two
                    True
                    sage: one == three
                    False
        '''
    def cum_distribution_function(self, x) -> Any:
        """RealDistribution.cum_distribution_function(self, x)

        File: /build/sagemath/src/sage/src/sage/probability/probability_distribution.pyx (starting at line 938)

        Evaluate the cumulative distribution function of
        the probability distribution at ``x``.

        EXAMPLES::

            sage: T = RealDistribution('uniform', [0, 2])
            sage: T.cum_distribution_function(1)
            0.5"""
    def cum_distribution_function_inv(self, x) -> Any:
        """RealDistribution.cum_distribution_function_inv(self, x)

        File: /build/sagemath/src/sage/src/sage/probability/probability_distribution.pyx (starting at line 978)

        Evaluate the inverse of the cumulative distribution
        distribution function of the probability distribution at ``x``.

        EXAMPLES::

            sage: T = RealDistribution('uniform', [0, 2])
            sage: T.cum_distribution_function_inv(.5)
            1.0"""
    def distribution_function(self, x) -> Any:
        """RealDistribution.distribution_function(self, x)

        File: /build/sagemath/src/sage/src/sage/probability/probability_distribution.pyx (starting at line 892)

        Evaluate the distribution function of the
        probability distribution at ``x``.

        EXAMPLES::

            sage: T = RealDistribution('uniform', [0, 2])
            sage: T.distribution_function(0)
            0.5
            sage: T.distribution_function(1)
            0.5
            sage: T.distribution_function(1.5)
            0.5
            sage: T.distribution_function(2)
            0.0"""
    @overload
    def get_random_element(self) -> Any:
        """RealDistribution.get_random_element(self)

        File: /build/sagemath/src/sage/src/sage/probability/probability_distribution.pyx (starting at line 679)

        Get a random sample from the probability distribution.

        EXAMPLES::

            sage: T = RealDistribution('gaussian', 1, seed=0)
            sage: T.get_random_element()  # rel tol 4e-16
            0.13391860811867587"""
    @overload
    def get_random_element(self) -> Any:
        """RealDistribution.get_random_element(self)

        File: /build/sagemath/src/sage/src/sage/probability/probability_distribution.pyx (starting at line 679)

        Get a random sample from the probability distribution.

        EXAMPLES::

            sage: T = RealDistribution('gaussian', 1, seed=0)
            sage: T.get_random_element()  # rel tol 4e-16
            0.13391860811867587"""
    @overload
    def plot(self, *args, **kwds) -> Any:
        """RealDistribution.plot(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/probability/probability_distribution.pyx (starting at line 1019)

        Plot the distribution function for the probability
        distribution. Parameters to :func:`sage.plot.plot.plot` can be
        passed through ``*args`` and ``**kwds``.

        EXAMPLES::

            sage: T = RealDistribution('uniform', [0, 2])
            sage: P = T.plot()                                                          # needs sage.plot"""
    @overload
    def plot(self) -> Any:
        """RealDistribution.plot(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/probability/probability_distribution.pyx (starting at line 1019)

        Plot the distribution function for the probability
        distribution. Parameters to :func:`sage.plot.plot.plot` can be
        passed through ``*args`` and ``**kwds``.

        EXAMPLES::

            sage: T = RealDistribution('uniform', [0, 2])
            sage: P = T.plot()                                                          # needs sage.plot"""
    @overload
    def reset_distribution(self) -> Any:
        """RealDistribution.reset_distribution(self)

        File: /build/sagemath/src/sage/src/sage/probability/probability_distribution.pyx (starting at line 873)

        Reset the distribution.

        EXAMPLES::

            sage: T = RealDistribution('gaussian', 1, seed=10)
            sage: [T.get_random_element() for _ in range(10)]  # rel tol 4e-16
            [-0.7460999595745819, -0.004644606626413462, -0.8720538317207641, 0.6916259921666037, 2.67668674666043, 0.6325002813661014, -0.7974263521959355, -0.5284976893366636, 1.1353119849528792, 0.9912505673230749]
            sage: T.reset_distribution()
            sage: [T.get_random_element() for _ in range(10)]  # rel tol 4e-16
            [-0.7460999595745819, -0.004644606626413462, -0.8720538317207641, 0.6916259921666037, 2.67668674666043, 0.6325002813661014, -0.7974263521959355, -0.5284976893366636, 1.1353119849528792, 0.9912505673230749]"""
    @overload
    def reset_distribution(self) -> Any:
        """RealDistribution.reset_distribution(self)

        File: /build/sagemath/src/sage/src/sage/probability/probability_distribution.pyx (starting at line 873)

        Reset the distribution.

        EXAMPLES::

            sage: T = RealDistribution('gaussian', 1, seed=10)
            sage: [T.get_random_element() for _ in range(10)]  # rel tol 4e-16
            [-0.7460999595745819, -0.004644606626413462, -0.8720538317207641, 0.6916259921666037, 2.67668674666043, 0.6325002813661014, -0.7974263521959355, -0.5284976893366636, 1.1353119849528792, 0.9912505673230749]
            sage: T.reset_distribution()
            sage: [T.get_random_element() for _ in range(10)]  # rel tol 4e-16
            [-0.7460999595745819, -0.004644606626413462, -0.8720538317207641, 0.6916259921666037, 2.67668674666043, 0.6325002813661014, -0.7974263521959355, -0.5284976893366636, 1.1353119849528792, 0.9912505673230749]"""
    def set_distribution(self, name=..., parameters=...) -> Any:
        """RealDistribution.set_distribution(self, name='uniform', parameters=None)

        File: /build/sagemath/src/sage/src/sage/probability/probability_distribution.pyx (starting at line 722)

        This method can be called to change the current probability distribution.

        EXAMPLES::

            sage: T = RealDistribution('gaussian', 1)
            sage: T.set_distribution('gaussian', 1)
            sage: T.set_distribution('pareto', [0, 1])"""
    def set_random_number_generator(self, rng=...) -> Any:
        """RealDistribution.set_random_number_generator(self, rng='default')

        File: /build/sagemath/src/sage/src/sage/probability/probability_distribution.pyx (starting at line 633)

        Set the gsl random number generator to be one of ``'default'``,
        ``'luxury'``, or ``'taus'``.

        EXAMPLES::

            sage: T = SphericalDistribution()
            sage: T.set_random_number_generator('default')
            sage: T.set_seed(0)
            sage: T.get_random_element()  # rel tol 4e-16
            (0.07961564104639995, -0.05237671627581255, 0.9954486572862178)
            sage: T.set_random_number_generator('luxury')
            sage: T.set_seed(0)
            sage: T.get_random_element()  # rel tol 4e-16
            (0.07961564104639995, -0.05237671627581255, 0.9954486572862178)"""
    def set_seed(self, seed) -> Any:
        """RealDistribution.set_seed(self, seed)

        File: /build/sagemath/src/sage/src/sage/probability/probability_distribution.pyx (starting at line 620)

        Set the seed for the underlying random number generator.

        EXAMPLES::

            sage: T = RealDistribution('gaussian', 1, rng='luxury', seed=10)
            sage: T.set_seed(100)"""

class SphericalDistribution(ProbabilityDistribution):
    """SphericalDistribution(dimension=3, rng='default', seed=None)

    File: /build/sagemath/src/sage/src/sage/probability/probability_distribution.pyx (starting at line 184)

    This class is capable of producing random points uniformly distributed
    on the surface of an `(n-1)`-sphere in `n`-dimensional euclidean space. The
    dimension `n` is selected via the keyword ``dimension``. The random
    number generator which drives it can be selected using the keyword
    ``rng``. Valid choices are ``'default'`` which uses the Mersenne-Twister,
    ``'luxury'`` which uses RANDLXS, and ``'taus'`` which uses the tausworth
    generator. The default dimension is ``3``.

    EXAMPLES::

        sage: T = SphericalDistribution()
        sage: s = T.get_random_element()
        sage: s.norm()  # rel tol 1e-14
        1.0
        sage: len(s)
        3
        sage: T = SphericalDistribution(dimension=4, rng='luxury')
        sage: s = T.get_random_element()
        sage: s.norm()  # rel tol 1e-14
        1.0
        sage: len(s)
        4

    TESTS:

    Make sure that repeated initializations are randomly seeded
    (:issue:`9770`)::

        sage: Xs = [tuple(SphericalDistribution(2).get_random_element()) for _ in range(1000)]
        sage: len(set(Xs)) > 2^^32
        True"""
    @overload
    def __init__(self, dimension=..., rng=..., seed=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/probability/probability_distribution.pyx (starting at line 225)

                EXAMPLES::

                    sage: T = SphericalDistribution()
                    sage: T.get_random_element().norm()  # rel tol 1e-14
                    1.0

                TESTS:

                Until :issue:`15089` a value of the ``seed`` keyword
                besides ``None`` was ignored. We check here that setting
                a seed is effective. ::

                    sage: T = SphericalDistribution(seed=876)
                    sage: one = [T.get_random_element() for _ in range(10)]
                    sage: T = SphericalDistribution(seed=876)
                    sage: two = [T.get_random_element() for _ in range(10)]
                    sage: T = SphericalDistribution(seed=123)
                    sage: three = [T.get_random_element() for _ in range(10)]
                    sage: one == two
                    True
                    sage: one == three
                    False
        """
    @overload
    def __init__(self) -> Any:
        """File: /build/sagemath/src/sage/src/sage/probability/probability_distribution.pyx (starting at line 225)

                EXAMPLES::

                    sage: T = SphericalDistribution()
                    sage: T.get_random_element().norm()  # rel tol 1e-14
                    1.0

                TESTS:

                Until :issue:`15089` a value of the ``seed`` keyword
                besides ``None`` was ignored. We check here that setting
                a seed is effective. ::

                    sage: T = SphericalDistribution(seed=876)
                    sage: one = [T.get_random_element() for _ in range(10)]
                    sage: T = SphericalDistribution(seed=876)
                    sage: two = [T.get_random_element() for _ in range(10)]
                    sage: T = SphericalDistribution(seed=123)
                    sage: three = [T.get_random_element() for _ in range(10)]
                    sage: one == two
                    True
                    sage: one == three
                    False
        """
    @overload
    def __init__(self, dimension=..., rng=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/probability/probability_distribution.pyx (starting at line 225)

                EXAMPLES::

                    sage: T = SphericalDistribution()
                    sage: T.get_random_element().norm()  # rel tol 1e-14
                    1.0

                TESTS:

                Until :issue:`15089` a value of the ``seed`` keyword
                besides ``None`` was ignored. We check here that setting
                a seed is effective. ::

                    sage: T = SphericalDistribution(seed=876)
                    sage: one = [T.get_random_element() for _ in range(10)]
                    sage: T = SphericalDistribution(seed=876)
                    sage: two = [T.get_random_element() for _ in range(10)]
                    sage: T = SphericalDistribution(seed=123)
                    sage: three = [T.get_random_element() for _ in range(10)]
                    sage: one == two
                    True
                    sage: one == three
                    False
        """
    @overload
    def get_random_element(self) -> Any:
        """SphericalDistribution.get_random_element(self)

        File: /build/sagemath/src/sage/src/sage/probability/probability_distribution.pyx (starting at line 302)

        Get a random sample from the probability distribution.

        EXAMPLES::

            sage: T = SphericalDistribution(seed=0)
            sage: T.get_random_element()  # rel tol 4e-16
            (0.07961564104639995, -0.05237671627581255, 0.9954486572862178)"""
    @overload
    def get_random_element(self) -> Any:
        """SphericalDistribution.get_random_element(self)

        File: /build/sagemath/src/sage/src/sage/probability/probability_distribution.pyx (starting at line 302)

        Get a random sample from the probability distribution.

        EXAMPLES::

            sage: T = SphericalDistribution(seed=0)
            sage: T.get_random_element()  # rel tol 4e-16
            (0.07961564104639995, -0.05237671627581255, 0.9954486572862178)"""
    @overload
    def reset_distribution(self) -> Any:
        """SphericalDistribution.reset_distribution(self)

        File: /build/sagemath/src/sage/src/sage/probability/probability_distribution.pyx (starting at line 319)

        This method resets the distribution.

        EXAMPLES::

            sage: T = SphericalDistribution(seed=0)
            sage: [T.get_random_element() for _ in range(4)]  # rel tol 4e-16
            [(0.07961564104639995, -0.05237671627581255, 0.9954486572862178),
             (0.4123599490593727, 0.5606817859360097, -0.7180495855658982),
             (-0.9619860891623148, -0.2726473494040498, -0.015690351211529927),
             (0.5674297579435619, -0.011206783800420301, -0.8233455397322326)]
            sage: T.reset_distribution()
            sage: [T.get_random_element() for _ in range(4)]  # rel tol 4e-16
            [(0.07961564104639995, -0.05237671627581255, 0.9954486572862178),
             (0.4123599490593727, 0.5606817859360097, -0.7180495855658982),
             (-0.9619860891623148, -0.2726473494040498, -0.015690351211529927),
             (0.5674297579435619, -0.011206783800420301, -0.8233455397322326)]"""
    @overload
    def reset_distribution(self) -> Any:
        """SphericalDistribution.reset_distribution(self)

        File: /build/sagemath/src/sage/src/sage/probability/probability_distribution.pyx (starting at line 319)

        This method resets the distribution.

        EXAMPLES::

            sage: T = SphericalDistribution(seed=0)
            sage: [T.get_random_element() for _ in range(4)]  # rel tol 4e-16
            [(0.07961564104639995, -0.05237671627581255, 0.9954486572862178),
             (0.4123599490593727, 0.5606817859360097, -0.7180495855658982),
             (-0.9619860891623148, -0.2726473494040498, -0.015690351211529927),
             (0.5674297579435619, -0.011206783800420301, -0.8233455397322326)]
            sage: T.reset_distribution()
            sage: [T.get_random_element() for _ in range(4)]  # rel tol 4e-16
            [(0.07961564104639995, -0.05237671627581255, 0.9954486572862178),
             (0.4123599490593727, 0.5606817859360097, -0.7180495855658982),
             (-0.9619860891623148, -0.2726473494040498, -0.015690351211529927),
             (0.5674297579435619, -0.011206783800420301, -0.8233455397322326)]"""
    def set_random_number_generator(self, rng=...) -> Any:
        """SphericalDistribution.set_random_number_generator(self, rng='default')

        File: /build/sagemath/src/sage/src/sage/probability/probability_distribution.pyx (starting at line 271)

        Set the gsl random number generator to be one of ``default``,
        ``luxury``, or ``taus``.

        EXAMPLES::

            sage: T = SphericalDistribution()
            sage: T.set_random_number_generator('default')
            sage: T.set_seed(0)
            sage: T.get_random_element()  # rel tol 4e-16
            (0.07961564104639995, -0.05237671627581255, 0.9954486572862178)
            sage: T.set_random_number_generator('luxury')
            sage: T.set_seed(0)
            sage: T.get_random_element()  # rel tol 4e-16
            (0.07961564104639995, -0.05237671627581255, 0.9954486572862178)"""
    def set_seed(self, seed) -> Any:
        """SphericalDistribution.set_seed(self, seed)

        File: /build/sagemath/src/sage/src/sage/probability/probability_distribution.pyx (starting at line 259)

        Set the seed for the underlying random number generator.

        EXAMPLES::

            sage: T = SphericalDistribution(seed=0)
            sage: T.set_seed(100)"""
