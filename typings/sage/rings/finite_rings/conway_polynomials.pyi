from _typeshed import Incomplete
from sage.misc.fast_methods import WithEqualityById as WithEqualityById
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.finite_rings.finite_field_constructor import FiniteField as FiniteField
from sage.rings.integer import Integer as Integer
from sage.structure.sage_object import SageObject as SageObject

def conway_polynomial(p, n):
    """
    Return the Conway polynomial of degree `n` over ``GF(p)``.

    If the requested polynomial is not known, this function raises a
    :exc:`RuntimeError` exception.

    INPUT:

    - ``p`` -- prime number

    - ``n`` -- positive integer

    OUTPUT:

    - the Conway polynomial of degree `n` over the finite field
      ``GF(p)``, loaded from a table.

    .. NOTE::

       The first time this function is called a table is read from
       disk, which takes a fraction of a second. Subsequent calls do
       not require reloading the table.

    See also the ``ConwayPolynomials()`` object, which is the table of
    Conway polynomials used by this function.

    EXAMPLES::

        sage: conway_polynomial(2,5)                                                    # needs conway_polynomials
        x^5 + x^2 + 1
        sage: conway_polynomial(101,5)                                                  # needs conway_polynomials
        x^5 + 2*x + 99
        sage: conway_polynomial(97,101)                                                 # needs conway_polynomials
        Traceback (most recent call last):
        ...
        RuntimeError: requested Conway polynomial not in database.
    """
def exists_conway_polynomial(p, n):
    """
    Check whether the Conway polynomial of degree `n` over ``GF(p)``
    is known.

    INPUT:

    - ``p`` -- prime number

    - ``n`` -- positive integer

    OUTPUT:

    - boolean: ``True`` if the Conway polynomial of degree `n` over
      ``GF(p)`` is in the database, ``False`` otherwise.

    If the Conway polynomial is in the database, it can be obtained
    using the command ``conway_polynomial(p,n)``.

    EXAMPLES::

        sage: exists_conway_polynomial(2,3)                                             # needs conway_polynomials
        True
        sage: exists_conway_polynomial(2,-1)
        False
        sage: exists_conway_polynomial(97,200)
        False
        sage: exists_conway_polynomial(6,6)
        False
    """

class PseudoConwayLattice(WithEqualityById, SageObject):
    """
    A pseudo-Conway lattice over a given finite prime field.

    The Conway polynomial `f_n` of degree `n` over `\\Bold{F}_p` is
    defined by the following four conditions:

    - `f_n` is irreducible.

    - In the quotient field `\\Bold{F}_p[x]/(f_n)`, the element
      `x\\bmod f_n` generates the multiplicative group.

    - The minimal polynomial of `(x\\bmod f_n)^{\\frac{p^n-1}{p^m-1}}`
      equals the Conway polynomial `f_m`, for every divisor `m` of
      `n`.

    - `f_n` is lexicographically least among all such polynomials,
      under a certain ordering.

    The final condition is needed only in order to make the Conway
    polynomial unique.  We define a pseudo-Conway lattice to be any
    family of polynomials, indexed by the positive integers,
    satisfying the first three conditions.

    INPUT:

    - ``p`` -- prime number

    - ``use_database`` -- boolean.  If ``True``, use actual Conway
      polynomials whenever they are available in the database.  If
      ``False``, always compute pseudo-Conway polynomials.

    EXAMPLES::

        sage: # needs sage.rings.finite_rings
        sage: from sage.rings.finite_rings.conway_polynomials import PseudoConwayLattice
        sage: PCL = PseudoConwayLattice(2, use_database=False)
        sage: PCL.polynomial(3)   # random
        x^3 + x + 1

    TESTS::

        sage: from sage.rings.finite_rings.conway_polynomials import PseudoConwayLattice
        sage: PCL = PseudoConwayLattice(3)
        sage: hash(PCL)  # random
        8738829832350

        sage: from sage.rings.finite_rings.conway_polynomials import PseudoConwayLattice
        sage: PseudoConwayLattice(3) == PseudoConwayLattice(3)
        False
        sage: PseudoConwayLattice(3) != PseudoConwayLattice(3)
        True
        sage: P = PseudoConwayLattice(5)
        sage: P == P
        True
        sage: P != P
        False
    """
    p: Incomplete
    ring: Incomplete
    nodes: Incomplete
    def __init__(self, p, use_database: bool = True) -> None:
        """
        TESTS::

            sage: # needs sage.rings.finite_rings
            sage: from sage.rings.finite_rings.conway_polynomials import PseudoConwayLattice
            sage: PCL = PseudoConwayLattice(3)
            sage: PCL.polynomial(3)  # random
            x^3 + 2*x + 1

            sage: # needs sage.rings.finite_rings
            sage: PCL = PseudoConwayLattice(5, use_database=False)
            sage: PCL.polynomial(12)  # random
            x^12 + 4*x^11 + 2*x^10 + 4*x^9 + 2*x^8 + 2*x^7 + 4*x^6 + x^5 + 2*x^4 + 2*x^2 + x + 2
            sage: PCL.polynomial(6)   # random
            x^6 + x^5 + 4*x^4 + 3*x^3 + 3*x^2 + 2*x + 2
            sage: PCL.polynomial(11)  # random
            x^11 + x^6 + 3*x^3 + 4*x + 3
        """
    def polynomial(self, n):
        """
        Return the pseudo-Conway polynomial of degree `n` in this
        lattice.

        INPUT:

        - ``n`` -- positive integer

        OUTPUT: a pseudo-Conway polynomial of degree `n` for the prime `p`

        ALGORITHM:

        Uses an algorithm described in [HL1999]_, modified to find
        pseudo-Conway polynomials rather than Conway polynomials.  The
        major difference is that we stop as soon as we find a
        primitive polynomial.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: from sage.rings.finite_rings.conway_polynomials import PseudoConwayLattice
            sage: PCL = PseudoConwayLattice(2, use_database=False)
            sage: PCL.polynomial(3)   # random
            x^3 + x + 1
            sage: PCL.polynomial(4)   # random
            x^4 + x^3 + 1
            sage: PCL.polynomial(60)  # random
            x^60 + x^59 + x^58 + x^55 + x^54 + x^53 + x^52 + x^51 + x^48 + x^46 + x^45 + x^42 + x^41 + x^39 + x^38 + x^37 + x^35 + x^32 + x^31 + x^30 + x^28 + x^24 + x^22 + x^21 + x^18 + x^17 + x^16 + x^15 + x^14 + x^10 + x^8 + x^7 + x^5 + x^3 + x^2 + x + 1
        """
    def check_consistency(self, n) -> None:
        """
        Check that the pseudo-Conway polynomials of degree dividing
        `n` in this lattice satisfy the required compatibility
        conditions.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: from sage.rings.finite_rings.conway_polynomials import PseudoConwayLattice
            sage: PCL = PseudoConwayLattice(2, use_database=False)
            sage: PCL.check_consistency(6)
            sage: PCL.check_consistency(60)  # long time
        """
