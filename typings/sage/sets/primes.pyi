from .set import Set_generic as Set_generic
from sage.arith.misc import nth_prime as nth_prime
from sage.categories.infinite_enumerated_sets import InfiniteEnumeratedSets as InfiniteEnumeratedSets
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class Primes(Set_generic, UniqueRepresentation):
    """
    The set of prime numbers.

    EXAMPLES::

        sage: P = Primes(); P
        Set of all prime numbers: 2, 3, 5, 7, ...

    We show various operations on the set of prime numbers::

        sage: P.cardinality()
        +Infinity
        sage: R = Primes()
        sage: P == R
        True
        sage: 5 in P
        True
        sage: 100 in P
        False

        sage: len(P)
        Traceback (most recent call last):
        ...
        NotImplementedError: infinite set
    """
    @staticmethod
    def __classcall__(cls, proof: bool = True):
        """
        TESTS::

            sage: Primes(proof=True) is Primes()
            True
            sage: Primes(proof=False) is Primes()
            False
        """
    def __init__(self, proof) -> None:
        """
        EXAMPLES::

            sage: P = Primes(); P
            Set of all prime numbers: 2, 3, 5, 7, ...

            sage: Q = Primes(proof=False); Q
            Set of all prime numbers: 2, 3, 5, 7, ...

        TESTS::

            sage: P.category()
            Category of facade infinite enumerated sets
            sage: TestSuite(P).run()                                                    # needs sage.libs.pari

            sage: Q.category()
            Category of facade infinite enumerated sets
            sage: TestSuite(Q).run()                                                    # needs sage.libs.pari

        The set of primes can be compared to various things,
        but is only equal to itself::

            sage: P = Primes()
            sage: R = Primes()
            sage: P == R
            True
            sage: P != R
            False
            sage: Q = [1,2,3]
            sage: Q != P        # indirect doctest
            True
            sage: R.<x> = ZZ[]
            sage: P != x^2+x
            True
        """
    def __contains__(self, x) -> bool:
        """
        Check whether an object is a prime number.

        EXAMPLES::

            sage: P = Primes()
            sage: 5 in P
            True
            sage: 100 in P
            False
            sage: 1.5 in P
            False
            sage: e in P                                                                # needs sage.symbolic
            False
        """
    def first(self):
        """
        Return the first prime number.

        EXAMPLES::

            sage: P = Primes()
            sage: P.first()
            2
        """
    def next(self, pr):
        """
        Return the next prime number.

        EXAMPLES::

            sage: P = Primes()
            sage: P.next(5)                                                             # needs sage.libs.pari
            7
        """
    def unrank(self, n):
        """
        Return the n-th prime number.

        EXAMPLES::

            sage: P = Primes()
            sage: P.unrank(0)                                                           # needs sage.libs.pari
            2
            sage: P.unrank(5)                                                           # needs sage.libs.pari
            13
            sage: P.unrank(42)                                                          # needs sage.libs.pari
            191
        """
