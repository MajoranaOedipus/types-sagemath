from sage.arith.misc import is_prime as is_prime, prime_divisors as prime_divisors
from sage.quadratic_forms.genera.genus import Genus as Genus, LocalGenusSymbol as LocalGenusSymbol
from sage.rings.integer_ring import ZZ as ZZ

def global_genus_symbol(self):
    """
    Return the genus of two times a quadratic form over `\\ZZ`.

    These are defined by a collection of local genus symbols (a la
    Chapter 15 of Conway-Sloane [CS1999]_), and a signature.

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,2,3,4])
        sage: Q.global_genus_symbol()
        Genus of
        [2 0 0 0]
        [0 4 0 0]
        [0 0 6 0]
        [0 0 0 8]
        Signature:  (4, 0)
        Genus symbol at 2:    [2^-2 4^1 8^1]_6
        Genus symbol at 3:     1^3 3^-1

    ::

        sage: Q = QuadraticForm(ZZ, 4, range(10))
        sage: Q.global_genus_symbol()
        Genus of
        [ 0  1  2  3]
        [ 1  8  5  6]
        [ 2  5 14  8]
        [ 3  6  8 18]
        Signature:  (3, 1)
        Genus symbol at 2:    1^-4
        Genus symbol at 563:     1^3 563^-1
    """
def local_genus_symbol(self, p):
    """
    Return the Conway-Sloane genus symbol of 2 times a quadratic form
    defined over `\\ZZ` at a prime number `p`.

    This is defined (in the class
    :class:`~sage.quadratic_forms.genera.genus.Genus_Symbol_p_adic_ring`)
    to be a list of tuples (one for each Jordan component
    `p^m\\cdot A` at `p`, where `A` is a unimodular symmetric matrix with
    coefficients the `p`-adic integers) of the following form:

    - If `p>2`, then return triples of the form [`m`, `n`, `d`] where

      - `m` = valuation of the component

      - `n` = rank of `A`

      - `d` = det(`A`) in {1, `u`} for normalized quadratic non-residue `u`.

    - If `p=2`, then return quintuples of the form [`m`, `n`, `s`, `d`, `o`] where

      - `m` = valuation of the component

      - `n` = rank of `A`

      - `d` = det(`A`) in {1, 3, 5, 7}

      - `s` = 0 (or 1) if `A` is even (or odd)

      - `o` = oddity of `A` (= 0 if `s` = 0) in `\\ZZ/8\\ZZ` = the trace of the diagonalization of `A`

    .. NOTE::

        The Conway-Sloane convention for describing the prime `p = -1`
        is not supported here, and neither is the convention for
        including the 'prime' Infinity.  See note on p370 of Conway-Sloane
        (3rd ed) [CS1999]_ for a discussion of this convention.

    INPUT:

    - ``p`` -- a prime number > 0

    OUTPUT:

    a Conway-Sloane genus symbol at `p`, which is an
    instance of the class :class:`~sage.quadratic_forms.genera.genus.Genus_Symbol_p_adic_ring`.

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,2,3,4])
        sage: Q.local_genus_symbol(2)
        Genus symbol at 2:    [2^-2 4^1 8^1]_6
        sage: Q.local_genus_symbol(3)
        Genus symbol at 3:     1^3 3^-1
        sage: Q.local_genus_symbol(5)
        Genus symbol at 5:     1^4
    """
def CS_genus_symbol_list(self, force_recomputation: bool = False):
    """
    Return the list of Conway-Sloane genus symbols in increasing order of primes dividing 2*det.

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,2,3,4])
        sage: Q.CS_genus_symbol_list()
        [Genus symbol at 2:    [2^-2 4^1 8^1]_6, Genus symbol at 3:     1^3 3^-1]
    """
