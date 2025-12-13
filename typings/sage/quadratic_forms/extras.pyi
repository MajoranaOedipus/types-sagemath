from sage.arith.misc import legendre_symbol as legendre_symbol
from sage.matrix.constructor import matrix as matrix
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.element import Matrix as Matrix

def is_triangular_number(n, return_value: bool = False) -> bool | tuple:
    """
    Return whether ``n`` is a triangular number.

    A *triangular number* is a number of the form `k(k+1)/2` for some
    nonnegative integer `n`. See :wikipedia:`Triangular_number`. The sequence
    of triangular number is references as A000217 in the Online encyclopedia of
    integer sequences (OEIS).

    If you want to get the value of `k` for which `n=k(k+1)/2` set the
    argument ``return_value`` to ``True`` (see the examples below).

    INPUT:

    - ``n`` -- integer

    - ``return_value`` -- boolean (default: ``False``); if set to
      ``True`` the function returns a pair made of a boolean and the value `v`
      such that `v(v+1)/2 = n`

    EXAMPLES::

        sage: is_triangular_number(3)
        True
        sage: is_triangular_number(3, return_value=True)
        (True, 2)

        sage: is_triangular_number(2)
        False
        sage: is_triangular_number(2, return_value=True)
        (False, None)

        sage: is_triangular_number(25*(25+1)/2)
        True

        sage: is_triangular_number(10^6 * (10^6 +1)/2, return_value=True)
        (True, 1000000)

    TESTS::

        sage: F1 = [n for n in range(1,100*(100+1)/2)
        ....:       if is_triangular_number(n)]
        sage: F2 = [n*(n+1)/2 for n in range(1,100)]
        sage: F1 == F2
        True

        sage: for n in range(1000):
        ....:     res,v = is_triangular_number(n,return_value=True)
        ....:     assert res == is_triangular_number(n)
        ....:     if res: assert v*(v+1)/2 == n
    """
def extend_to_primitive(A_input):
    '''
    Given a matrix (resp. list of vectors), extend it to a square
    matrix (resp. list of vectors), such that its determinant is the
    gcd of its minors (i.e. extend the basis of a lattice to a
    "maximal" one in `\\ZZ^n`).

    Author(s): Gonzalo Tornaria and Jonathan Hanke.

    INPUT:

    - ``A_input`` -- a matrix or a list of length n vectors (in the same space)

    OUTPUT: a square matrix or a list of n vectors (resp.)

    EXAMPLES::

        sage: A = Matrix(ZZ, 3, 2, range(6))
        sage: extend_to_primitive(A)
        [ 0  1 -1]
        [ 2  3  0]
        [ 4  5  0]

        sage: extend_to_primitive([vector([1,2,3])])
        [(1, 2, 3), (0, 1, 1), (-1, 0, 0)]
    '''
def least_quadratic_nonresidue(p):
    """
    Return the smallest positive integer quadratic non-residue in `\\ZZ/p\\ZZ` for primes `p>2`.

    EXAMPLES::

        sage: least_quadratic_nonresidue(5)
        2
        sage: [least_quadratic_nonresidue(p) for p in prime_range(3, 100)]              # needs sage.libs.pari
        [2, 2, 3, 2, 2, 3, 2, 5, 2, 3, 2, 3, 2, 5, 2, 2, 2, 2, 7, 5, 3, 2, 3, 5]

    TESTS:

    This raises an error if input is a positive composite integer. ::

        sage: least_quadratic_nonresidue(20)
        Traceback (most recent call last):
        ...
        ValueError: p must be a prime number > 2

    This raises an error if input is 2. This is because every integer is a
    quadratic residue modulo 2. ::

        sage: least_quadratic_nonresidue(2)
        Traceback (most recent call last):
        ...
        ValueError: there are no quadratic non-residues in Z/2Z
    """
