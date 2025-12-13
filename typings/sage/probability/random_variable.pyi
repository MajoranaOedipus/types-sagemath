from sage.functions.log import log as log
from sage.misc.functional import sqrt as sqrt
from sage.rings.rational_field import RationalField as RationalField
from sage.sets.set import Set as Set
from sage.structure.parent import Parent as Parent

def is_ProbabilitySpace(S): ...
def is_DiscreteProbabilitySpace(S): ...
def is_RandomVariable(X): ...
def is_DiscreteRandomVariable(X): ...

class RandomVariable_generic(Parent):
    """
    A random variable.
    """
    def __init__(self, X, RR) -> None: ...
    def probability_space(self): ...
    def domain(self): ...
    def codomain(self): ...
    def field(self): ...

class DiscreteRandomVariable(RandomVariable_generic):
    """
    A random variable on a discrete probability space.
    """
    def __init__(self, X, f, codomain=None, check: bool = False) -> None:
        """
        Create free binary string monoid on `n` generators.

        INPUT:

        - ``X`` -- a probability space
        - ``f`` -- dictionary such that X[x] = value for x in X
          is the discrete function on X
        """
    def __call__(self, x):
        """
        Return the value of the random variable at x.
        """
    def function(self):
        """
        The function defining the random variable.
        """
    def expectation(self):
        """
        The expectation of the discrete random variable, namely
        `\\sum_{x \\in S} p(x) X[x]`, where `X` = ``self`` and
        `S` is the probability space of `X`.
        """
    def translation_expectation(self, map):
        """
        The expectation of the discrete random variable, namely
        `\\sum_{x \\in S} p(x) X[e(x)]`, where `X` = self,
        `S` is the probability space of `X`, and
        `e` = map.
        """
    def variance(self):
        """
        The variance of the discrete random variable.

        Let `S` be the probability space of `X` = self,
        with probability function `p`, and `E(X)` be the
        expectation of `X`. Then the variance of `X` is:

        .. MATH::

           \\mathrm{var}(X) = E((X-E(x))^2) = \\sum_{x \\in S} p(x) (X(x) - E(x))^2
        """
    def translation_variance(self, map):
        """
        The variance of the discrete random variable `X \\circ e`,
        where `X` = self, and `e` = map.

        Let `S` be the probability space of `X` = self,
        with probability function `p`, and `E(X)` be the
        expectation of `X`. Then the variance of `X` is:

        .. MATH::

           \\mathrm{var}(X) = E((X-E(x))^2) = \\sum_{x \\in S} p(x) (X(x) - E(x))^2
        """
    def covariance(self, other):
        """
        The covariance of the discrete random variable X = ``self`` with Y =
        ``other``.

        Let `S` be the probability space of `X` = self,
        with probability function `p`, and `E(X)` be the
        expectation of `X`. Then the variance of `X` is:

        .. MATH::

                     \\text{cov}(X,Y) = E((X-E(X)\\cdot (Y-E(Y)) = \\sum_{x \\in S} p(x) (X(x) - E(X))(Y(x) - E(Y))
        """
    def translation_covariance(self, other, map):
        """
        The covariance of the probability space X = ``self`` with image of Y =
        ``other`` under the given map of the probability space.

        Let `S` be the probability space of `X` = self,
        with probability function `p`, and `E(X)` be the
        expectation of `X`. Then the variance of `X` is:

        .. MATH::

                     \\text{cov}(X,Y) = E((X-E(X)\\cdot (Y-E(Y)) = \\sum_{x \\in S} p(x) (X(x) - E(X))(Y(x) - E(Y))
        """
    def standard_deviation(self):
        """
        The standard deviation of the discrete random variable.

        Let `S` be the probability space of `X` = self,
        with probability function `p`, and `E(X)` be the
        expectation of `X`. Then the standard deviation of
        `X` is defined to be

        .. MATH::

                     \\sigma(X) = \\sqrt{ \\sum_{x \\in S} p(x) (X(x) - E(x))^2}
        """
    def translation_standard_deviation(self, map):
        """
        The standard deviation of the translated discrete random variable
        `X \\circ e`, where `X` = ``self`` and `e` =
        map.

        Let `S` be the probability space of `X` = ``self``,
        with probability function `p`, and `E(X)` be the
        expectation of `X`. Then the standard deviation of
        `X` is defined to be

        .. MATH::

            \\sigma(X) = \\sqrt{ \\sum_{x \\in S} p(x) (X(x) - E(x))^2}
        """
    def correlation(self, other):
        """
        The correlation of the probability space X = ``self`` with Y = ``other``.
        """
    def translation_correlation(self, other, map):
        """
        The correlation of the probability space X = ``self`` with image of Y =
        ``other`` under map.
        """

class ProbabilitySpace_generic(RandomVariable_generic):
    """
    A probability space.
    """
    def __init__(self, domain, RR) -> None:
        """
        A generic probability space on given domain space and codomain
        ring.
        """
    def domain(self): ...

class DiscreteProbabilitySpace(ProbabilitySpace_generic, DiscreteRandomVariable):
    """
    The discrete probability space
    """
    def __init__(self, X, P, codomain=None, check: bool = False) -> None:
        """
        Create the discrete probability space with probabilities on the
        space X given by the dictionary P with values in the field
        real_field.

        EXAMPLES::

            sage: S = [ i for i in range(16) ]
            sage: P = {}
            sage: for i in range(15): P[i] = 2^(-i-1)
            sage: P[15] = 2^-15
            sage: X = DiscreteProbabilitySpace(S,P)
            sage: sum(X.function().values())
            1
            sage: X.domain()
            (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
            sage: X.set()
            {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
            sage: X.entropy().n()                                                       # needs sage.libs.pari
            1.99993896484375

        A probability space can be defined on any list of elements::

            sage: AZ = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            sage: S = [ AZ[i] for i in range(26) ]
            sage: P = { 'A':1/2, 'B':1/4, 'C':1/4 }
            sage: X = DiscreteProbabilitySpace(S,P)
            sage: X
            Discrete probability space defined by {'A': 1/2, 'B': 1/4, 'C': 1/4}
            sage: X.entropy().n()                                                       # needs sage.libs.pari
            1.50000000000000
        """
    def set(self):
        """
        The set of values of the probability space taking possibly nonzero
        probability (a subset of the domain).
        """
    def entropy(self):
        """
        The entropy of the probability space.
        """
