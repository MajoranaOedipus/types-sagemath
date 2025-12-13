import _random
from _typeshed import Incomplete

NV_MAGICCONST: Incomplete
TWOPI: Incomplete
LOG4: Incomplete
SG_MAGICCONST: Incomplete
BPF: int

class Random(_random.Random):
    """Random number generator base class used by bound module functions.

    Used to instantiate instances of Random to get generators that don't
    share state.  Especially useful for multi-threaded programs, creating
    a different instance of Random for each thread, and using the jumpahead()
    method to ensure that the generated sequences seen by each thread don't
    overlap.

    Class Random can also be subclassed if you want to use a different basic
    generator of your own devising: in that case, override the following
    methods: random(), seed(), getstate(), setstate() and jumpahead().
    Optionally, implement a getrandbits() method so that randrange() can cover
    arbitrarily large ranges.
    """
    VERSION: int
    gauss_next: Incomplete
    def __init__(self, x=None) -> None:
        """Initialize an instance.

        Optional argument x controls seeding, as for Random.seed().
        """
    def seed(self, a=None) -> None:
        """Initialize internal state of the random number generator.

        None or no argument seeds from current time or from an operating
        system specific randomness source if available.

        If a is not None or is an int or long, hash(a) is used instead.
        Hash values for some types are nondeterministic when the
        PYTHONHASHSEED environment variable is enabled.
        """
    def getstate(self):
        """Return internal state; can be passed to setstate() later."""
    def setstate(self, state) -> None:
        """Restore internal state from object returned by getstate()."""
    def jumpahead(self, n) -> None:
        """Change the internal state to one that is likely far away
        from the current state.  This method will not be in Py3.x,
        so it is better to simply reseed.
        """
    def __reduce__(self): ...
    def randrange(self, start, stop=None, step: int = 1, _int=..., _maxwidth=...):
        """Choose a random item from range(start, stop[, step]).

        This fixes the problem with randint() which includes the
        endpoint; in Python this is usually not what you want.
        """
    def randint(self, a, b):
        """Return random integer in range [a, b], including both end points.
        """
    def choice(self, seq):
        """Choose a random element from a non-empty sequence."""
    def shuffle(self, x, random=None) -> None:
        """x, random=random.random -> shuffle list x in place; return None.

        Optional arg random is a 0-argument function returning a random
        float in [0.0, 1.0); by default, the standard random.random.
        """
    def sample(self, population, k):
        """
        Choose k unique random elements from a population sequence.

        Return a new list containing elements from the population while
        leaving the original population unchanged.  The resulting list is
        in selection order so that all sub-slices will also be valid random
        samples.  This allows raffle winners (the sample) to be partitioned
        into grand prize and second place winners (the subslices).

        Members of the population need not be hashable or unique.  If the
        population contains repeats, then each occurrence is a possible
        selection in the sample.

        To choose a sample in a range of integers, use range as an argument.
        This is especially fast and space efficient for sampling from a
        large population:   sample(range(10000000), 60)
        """
    def uniform(self, a, b):
        """Get a random number in the range [a, b) or [a, b] depending on rounding."""
    def triangular(self, low: float = 0.0, high: float = 1.0, mode=None):
        """Triangular distribution.

        Continuous distribution bounded by given lower and upper limits,
        and having a given mode value in-between.

        http://en.wikipedia.org/wiki/Triangular_distribution
        """
    def normalvariate(self, mu, sigma):
        """Normal distribution.

        mu is the mean, and sigma is the standard deviation.
        """
    def lognormvariate(self, mu, sigma):
        """Log normal distribution.

        If you take the natural logarithm of this distribution, you'll get a
        normal distribution with mean mu and standard deviation sigma.
        mu can have any value, and sigma must be greater than zero.
        """
    def expovariate(self, lambd):
        '''Exponential distribution.

        lambd is 1.0 divided by the desired mean.  It should be
        nonzero.  (The parameter would be called "lambda", but that is
        a reserved word in Python.)  Returned values range from 0 to
        positive infinity if lambd is positive, and from negative
        infinity to 0 if lambd is negative.
        '''
    def vonmisesvariate(self, mu, kappa):
        """Circular data distribution.

        mu is the mean angle, expressed in radians between 0 and 2*pi, and
        kappa is the concentration parameter, which must be greater than or
        equal to zero.  If kappa is equal to zero, this distribution reduces
        to a uniform random angle over the range 0 to 2*pi.
        """
    def gammavariate(self, alpha, beta):
        """Gamma distribution.  Not the gamma function!

        Conditions on the parameters are alpha > 0 and beta > 0.

        The probability distribution function is::

                    x ** (alpha - 1) * math.exp(-x / beta)
          pdf(x) =  --------------------------------------
                      math.gamma(alpha) * beta ** alpha
        """
    def gauss(self, mu, sigma):
        """Gaussian distribution.

        mu is the mean, and sigma is the standard deviation.  This is
        slightly faster than the normalvariate() function.

        Not thread-safe without a lock around calls.
        """
    def betavariate(self, alpha, beta):
        """Beta distribution.

        Conditions on the parameters are alpha > 0 and beta > 0.
        Returned values range between 0 and 1.
        """
    def paretovariate(self, alpha):
        """Pareto distribution.  alpha is the shape parameter."""
    def weibullvariate(self, alpha, beta):
        """Weibull distribution.

        alpha is the scale parameter and beta is the shape parameter.
        """
