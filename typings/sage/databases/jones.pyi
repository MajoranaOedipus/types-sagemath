from _typeshed import Incomplete
from sage.combinat.subset import powerset as powerset
from sage.env import SAGE_SHARE as SAGE_SHARE
from sage.features.databases import DatabaseJones as DatabaseJones
from sage.misc.persist import load as load, save as save
from sage.rings.number_field.number_field import NumberField as NumberField
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import RationalField as RationalField

def sortkey(K):
    """
    A completely deterministic sorting key for number fields.

    EXAMPLES::

        sage: from sage.databases.jones import sortkey
        sage: sortkey(QuadraticField(-3))
        (2, 3, False, x^2 + 3)
    """

class JonesDatabase:
    root: Incomplete
    def __init__(self) -> None: ...
    def unramified_outside(self, S, d=None, var: str = 'a'):
        """
        Return all fields in the database of degree d unramified
        outside S. If d is omitted, return fields of any degree up to 6.
        The fields are ordered by degree and discriminant.

        INPUT:

        - ``S`` -- list or set of primes, or a single prime

        - ``d`` -- ``None`` (default, in which case all fields of degree <= 6 are returned)
          or a positive integer giving the degree of the number fields returned

        - ``var`` -- the name used for the generator of the number fields (default: ``'a'``)

        EXAMPLES::

            sage: J = JonesDatabase()             # optional - database_jones_numfield
            sage: J.unramified_outside([101,109]) # optional - database_jones_numfield
            [Number Field in a with defining polynomial x - 1,
             Number Field in a with defining polynomial x^2 - 101,
             Number Field in a with defining polynomial x^2 - 109,
             Number Field in a with defining polynomial x^3 - x^2 - 36*x + 4,
             Number Field in a with defining polynomial x^4 - x^3 + 13*x^2 - 19*x + 361,
             Number Field in a with defining polynomial x^4 - x^3 + 14*x^2 + 34*x + 393,
             Number Field in a with defining polynomial x^5 + x^4 - 6*x^3 - x^2 + 18*x + 4,
             Number Field in a with defining polynomial x^5 + 2*x^4 + 7*x^3 + 4*x^2 + 11*x - 6,
             Number Field in a with defining polynomial x^5 - x^4 - 40*x^3 - 93*x^2 - 21*x + 17]
        """
    def __getitem__(self, S): ...
    def get(self, S, var: str = 'a'):
        """
        Return all fields in the database ramified exactly at
        the primes in S.

        INPUT:

        - ``S`` -- list or set of primes, or a single prime

        - ``var`` -- the name used for the generator of the number fields (default: ``'a'``)

        EXAMPLES::

            sage: J = JonesDatabase()              # optional - database_jones_numfield
            sage: J.get(163, var='z')              # optional - database_jones_numfield
            [Number Field in z with defining polynomial x^2 + 163,
             Number Field in z with defining polynomial x^3 - x^2 - 54*x + 169,
             Number Field in z with defining polynomial x^4 - x^3 - 7*x^2 + 2*x + 9]
            sage: J.get([3, 4])                    # optional - database_jones_numfield
            Traceback (most recent call last):
            ...
            ValueError: S must be a list of primes
        """
    def ramified_at(self, S, d=None, var: str = 'a'):
        """
        Return all fields in the database of degree d ramified exactly at
        the primes in S.  The fields are ordered by degree and discriminant.

        INPUT:

        - ``S`` -- list or set of primes

        - ``d`` -- ``None`` (default, in which case all fields of degree <= 6 are returned)
          or a positive integer giving the degree of the number fields returned

        - ``var`` -- the name used for the generator of the number fields (default: ``'a'``)

        EXAMPLES::

            sage: # optional - database_jones_numfield
            sage: J = JonesDatabase()
            sage: J.ramified_at([101,109])
            []
            sage: J.ramified_at([109])
            [Number Field in a with defining polynomial x^2 - 109,
             Number Field in a with defining polynomial x^3 - x^2 - 36*x + 4,
             Number Field in a with defining polynomial x^4 - x^3 + 14*x^2 + 34*x + 393]
            sage: J.ramified_at(101)
            [Number Field in a with defining polynomial x^2 - 101,
             Number Field in a with defining polynomial x^4 - x^3 + 13*x^2 - 19*x + 361,
             Number Field in a with defining polynomial x^5 + x^4 - 6*x^3 - x^2 + 18*x + 4,
             Number Field in a with defining polynomial x^5 + 2*x^4 + 7*x^3 + 4*x^2 + 11*x - 6,
             Number Field in a with defining polynomial x^5 - x^4 - 40*x^3 - 93*x^2 - 21*x + 17]
            sage: J.ramified_at((2, 5, 29), 3, 'c')
            [Number Field in c with defining polynomial x^3 - x^2 - 8*x - 28,
             Number Field in c with defining polynomial x^3 - x^2 + 10*x + 102,
             Number Field in c with defining polynomial x^3 - x^2 - 48*x - 188,
             Number Field in c with defining polynomial x^3 - x^2 + 97*x - 333]
        """
