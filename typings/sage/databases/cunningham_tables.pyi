from sage.env import SAGE_SHARE as SAGE_SHARE
from sage.misc.cachefunc import cached_function as cached_function
from sage.misc.persist import load as load
from sage.rings.integer import Integer as Integer

@cached_function
def cunningham_prime_factors():
    """
    List of all the prime numbers occurring in the so called Cunningham table.

    They occur in the factorization of numbers of type `b^n+1` or `b^n-1` with `b \\in \\{2,3,5,6,7,10,11,12\\}`.

    EXAMPLES::

        sage: # optional - cunningham_tables
        sage: from sage.databases.cunningham_tables import cunningham_prime_factors
        sage: cunningham_prime_factors()
        [2,
         3,
         5,
         7,
         11,
         13,
         17,
         ...
    """
