from sage.arith.misc import bernoulli as bernoulli, fundamental_discriminant as fundamental_discriminant, prime_divisors as prime_divisors
from sage.misc.functional import sqrt as sqrt
from sage.misc.verbose import verbose as verbose
from sage.quadratic_forms.special_values import QuadraticBernoulliNumber as QuadraticBernoulliNumber
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ

def siegel_product(self, u):
    """
    Compute the infinite product of local densities of the quadratic
    form for the number `u`.

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1,1])
        sage: Q.theta_series(11)
        1 + 8*q + 24*q^2 + 32*q^3 + 24*q^4 + 48*q^5 + 96*q^6 + 64*q^7 + 24*q^8 + 104*q^9 + 144*q^10 + O(q^11)

        sage: Q.siegel_product(1)
        8
        sage: Q.siegel_product(2)      # This one is wrong -- expect 24, and the higher powers of 2 don't work... =(
        24
        sage: Q.siegel_product(3)
        32
        sage: Q.siegel_product(5)
        48
        sage: Q.siegel_product(6)
        96
        sage: Q.siegel_product(7)
        64
        sage: Q.siegel_product(9)
        104

        sage: Q.local_density(2,1)
        1
        sage: M = 4; len([v  for v in mrange([M,M,M,M])  if Q(v) % M == 1]) / M^3
        1
        sage: M = 16; len([v  for v in mrange([M,M,M,M])  if Q(v) % M == 1]) / M^3  # long time (2s on sage.math, 2014)
        1

        sage: Q.local_density(2,2)
        3/2
        sage: M = 4; len([v  for v in mrange([M,M,M,M])  if Q(v) % M == 2]) / M^3
        3/2
        sage: M = 16; len([v  for v in mrange([M,M,M,M])  if Q(v) % M == 2]) / M^3  # long time (2s on sage.math, 2014)
        3/2

    TESTS::

        sage: [1] + [Q.siegel_product(ZZ(a))  for a in range(1,11)] == Q.theta_series(11).list()  # long time (2s on sage.math, 2014)
        True
    """
