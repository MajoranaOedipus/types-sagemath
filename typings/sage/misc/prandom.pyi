from sage.misc.randstate import current_randstate as current_randstate

def getrandbits(k):
    """
    getrandbits(k) -> x.  Generates a long int with k random bits.

    EXAMPLES::

        sage: getrandbits(10) in range(2^10)
        True
        sage: getrandbits(200) in range(2^200)
        True
        sage: getrandbits(4) in range(2^4)
        True
    """
def randrange(start, stop=None, step: int = 1):
    """
    Choose a random item from range(start, stop[, step]).

    This fixes the problem with randint() which includes the
    endpoint; in Python this is usually not what you want.

    EXAMPLES::

        sage: s = randrange(0, 100, 11)
        sage: 0 <= s < 100
        True
        sage: s % 11
        0

        sage: 5000 <= randrange(5000, 5100) < 5100
        True
        sage: s = [randrange(0, 2) for i in range(15)]
        sage: all(t in [0, 1] for t in s)
        True

        sage: s = randrange(0, 1000000, 1000)
        sage: 0 <= s < 1000000
        True
        sage: s % 1000
        0
        sage: -100 <= randrange(-100, 10) < 10
        True
    """
def randint(a, b):
    """
    Return random integer in range [a, b], including both end points.

    EXAMPLES::

        sage: s = [randint(0, 2) for i in range(15)]; s  # random
        [0, 1, 0, 0, 1, 0, 2, 0, 2, 1, 2, 2, 0, 2, 2]
        sage: all(t in [0, 1, 2] for t in s)
        True
        sage: -100 <= randint(-100, 10) <= 10
        True
    """
def choice(seq):
    """
    Choose a random element from a non-empty sequence.

    EXAMPLES::

        sage: s = [choice(list(primes(10, 100))) for i in range(5)]; s  # random        # needs sage.libs.pari
        [17, 47, 11, 31, 47]
        sage: all(t in primes(10, 100) for t in s)                                      # needs sage.libs.pari
        True
    """
def shuffle(x):
    """
    x, random=random.random -> shuffle list x in place; return None.

    Optional arg random is a 0-argument function returning a random
    float in [0.0, 1.0); by default, the sage.misc.random.random.

    EXAMPLES::

        sage: shuffle([1 .. 10])
    """
def sample(population, k):
    '''
    Choose k unique random elements from a population sequence.

    Return a new list containing elements from the population while
    leaving the original population unchanged.  The resulting list is
    in selection order so that all sub-slices will also be valid random
    samples.  This allows raffle winners (the sample) to be partitioned
    into grand prize and second place winners (the subslices).

    Members of the population need not be hashable or unique.  If the
    population contains repeats, then each occurrence is a possible
    selection in the sample.

    To choose a sample in a range of integers, use xrange as an
    argument (in Python 2) or range (in Python 3).  This is especially
    fast and space efficient for sampling from a large population:
    sample(range(10000000), 60)

    EXAMPLES::

        sage: from sage.misc.misc import is_sublist
        sage: l = ["Here", "I", "come", "to", "save", "the", "day"]
        sage: s = sample(l, 3); s  # random
        [\'Here\', \'to\', \'day\']
        sage: is_sublist(sorted(s), sorted(l))
        True
        sage: len(s)
        3

        sage: s = sample(range(2^30), 7); s  # random
        [357009070, 558990255, 196187132, 752551188, 85926697, 954621491, 624802848]
        sage: len(s)
        7
        sage: all(t in range(2^30) for t in s)
        True
    '''
def random():
    """
    Get the next random number in the range [0.0, 1.0).

    EXAMPLES::

        sage: sample = [random() for i in [1 .. 4]]; sample  # random
        [0.111439293741037, 0.5143475134191677, 0.04468968524815642, 0.332490606442413]
        sage: all(0.0 <= s <= 1.0 for s in sample)
        True
    """
def uniform(a, b):
    """
    Get a random number in the range [a, b).

    Equivalent to \\code{a + (b-a) * random()}.

    EXAMPLES::

        sage: s = uniform(0, 1); s  # random
        0.111439293741037
        sage: 0.0 <= s <= 1.0
        True

        sage: s = uniform(e, pi); s  # random                                           # needs sage.symbolic
        0.5143475134191677*pi + 0.48565248658083227*e
        sage: bool(e <= s <= pi)                                                        # needs sage.symbolic
        True
    """
def betavariate(alpha, beta):
    """
    Beta distribution.

    Conditions on the parameters are alpha > 0 and beta > 0.
    Returned values range between 0 and 1.

    EXAMPLES::

        sage: s = betavariate(0.1, 0.9); s  # random
        9.75087916621299e-9
        sage: 0.0 <= s <= 1.0
        True

        sage: s = betavariate(0.9, 0.1); s  # random
        0.941890400939253
        sage: 0.0 <= s <= 1.0
        True
    """
def expovariate(lambd):
    '''
    Exponential distribution.

    lambd is 1.0 divided by the desired mean.  (The parameter would be
    called "lambda", but that is a reserved word in Python.)  Returned
    values range from 0 to positive infinity.

    EXAMPLES::

        sage: sample = [expovariate(0.001) for i in range(3)]; sample  # random
        [118.152309288166, 722.261959038118, 45.7190543690470]
        sage: all(s >= 0.0 for s in sample)
        True

        sage: sample = [expovariate(1.0) for i in range(3)]; sample  # random
        [0.404201816061304, 0.735220464997051, 0.201765578600627]
        sage: all(s >= 0.0 for s in sample)
        True

        sage: sample = [expovariate(1000) for i in range(3)]; sample  # random
        [0.0012068700332283973, 8.340929747302108e-05, 0.00219877067980605]
        sage: all(s >= 0.0 for s in sample)
        True
    '''
def gammavariate(alpha, beta):
    """
    Gamma distribution.  (Not the gamma function.)

    Conditions on the parameters are alpha > 0 and beta > 0.

    EXAMPLES::

        sage: sample = gammavariate(1.0, 3.0); sample  # random
        6.58282586130638
        sage: sample > 0
        True
        sage: sample = gammavariate(3.0, 1.0); sample  # random
        3.07801512341612
        sage: sample > 0
        True
    """
def gauss(mu, sigma):
    """
    Gaussian distribution.

    mu is the mean, and sigma is the standard deviation.  This is
    slightly faster than the normalvariate() function, but is not
    thread-safe.

    EXAMPLES::

       sage: [gauss(0, 1) for i in range(3)]  # random
       [0.9191011757657915, 0.7744526756246484, 0.8638996866800877]
       sage: [gauss(0, 100) for i in range(3)]  # random
       [24.916051749154448, -62.99272061579273, -8.1993122536718...]
       sage: [gauss(1000, 10) for i in range(3)]  # random
       [998.7590700045661, 996.1087338511692, 1010.1256817458031]
    """
def lognormvariate(mu, sigma):
    """
    Log normal distribution.

    If you take the natural logarithm of this distribution, you'll get a
    normal distribution with mean mu and standard deviation sigma.
    mu can have any value, and sigma must be greater than zero.

    EXAMPLES::

        sage: [lognormvariate(100, 10) for i in range(3)]  # random
        [2.9410355688290246e+37, 2.2257548162070125e+38, 4.142299451717446e+43]
    """
def normalvariate(mu, sigma):
    """
    Normal distribution.

    mu is the mean, and sigma is the standard deviation.

    EXAMPLES::

       sage: [normalvariate(0, 1) for i in range(3)]  # random
       [-1.372558980559407, -1.1701670364898928, 0.04324100555110143]
       sage: [normalvariate(0, 100) for i in range(3)]  # random
       [37.45695875041769, 159.6347743233298, 124.1029321124009]
       sage: [normalvariate(1000, 10) for i in range(3)]  # random
       [1008.5303090383741, 989.8624892644895, 985.7728921150242]
    """
def vonmisesvariate(mu, kappa):
    """
    Circular data distribution.

    mu is the mean angle, expressed in radians between 0 and 2*pi, and
    kappa is the concentration parameter, which must be greater than or
    equal to zero.  If kappa is equal to zero, this distribution reduces
    to a uniform random angle over the range 0 to 2*pi.

    EXAMPLES::

        sage: sample = [vonmisesvariate(1.0r, 3.0r) for i in range(1, 5)]; sample  # random
        [0.898328639355427, 0.6718030007041281, 2.0308777524813393, 1.714325253725145]
        sage: all(s >= 0.0 for s in sample)
        True
    """
def paretovariate(alpha):
    """
    Pareto distribution.  alpha is the shape parameter.

    EXAMPLES::

        sage: sample = [paretovariate(3) for i in range(1, 5)]; sample  # random
        [1.0401699394233033, 1.2722080162636495, 1.0153564009379579, 1.1442323078983077]
        sage: all(s >= 1.0 for s in sample)
        True
    """
def weibullvariate(alpha, beta):
    """
    Weibull distribution.

    alpha is the scale parameter and beta is the shape parameter.

    EXAMPLES::

        sage: sample = [weibullvariate(1, 3) for i in range(1, 5)]; sample  # random
        [0.49069775546342537, 0.8972185564611213, 0.357573846531942, 0.739377255516847]
        sage: all(s >= 0.0 for s in sample)
        True
    """
