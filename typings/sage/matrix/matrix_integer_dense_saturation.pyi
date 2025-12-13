from sage.arith.misc import binomial as binomial
from sage.matrix import matrix_integer_dense_hnf as matrix_integer_dense_hnf
from sage.matrix.constructor import identity_matrix as identity_matrix, random_matrix as random_matrix
from sage.misc.randstate import current_randstate as current_randstate
from sage.misc.verbose import verbose as verbose
from sage.rings.integer_ring import ZZ as ZZ

def p_saturation(A, p, proof: bool = True):
    """
    INPUT:

    - ``A`` -- a matrix over ZZ
    - ``p`` -- a prime
    - ``proof`` -- boolean (default: ``True``)

    OUTPUT:

    The p-saturation of the matrix A, i.e., a new matrix in Hermite form
    whose row span a ZZ-module that is p-saturated.

    EXAMPLES::

        sage: from sage.matrix.matrix_integer_dense_saturation import p_saturation
        sage: A = matrix(ZZ, 2, 2, [3,2,3,4]); B = matrix(ZZ, 2,3,[1,2,3,4,5,6])
        sage: A.det()
        6
        sage: C = A*B; C
        [11 16 21]
        [19 26 33]
        sage: C2 = p_saturation(C, 2); C2
        [ 1  8 15]
        [ 0  9 18]
        sage: C2.index_in_saturation()
        9
        sage: C3 = p_saturation(C, 3); C3
        [ 1  0 -1]
        [ 0  2  4]
        sage: C3.index_in_saturation()
        2
    """
def random_sublist_of_size(k, n):
    """
    INPUT:

    - ``k`` -- integer
    - ``n`` -- integer

    OUTPUT: a randomly chosen sublist of ``range(k)`` of size `n`

    EXAMPLES::

        sage: import sage.matrix.matrix_integer_dense_saturation as s
        sage: l = s.random_sublist_of_size(10, 3)
        sage: len(l)
        3
        sage: l_check = [-1] + l + [10]
        sage: all(l_check[i] < l_check[i+1] for i in range(4))
        True
        sage: l = s.random_sublist_of_size(10, 7)
        sage: len(l)
        7
        sage: l_check = [-1] + l + [10]
        sage: all(l_check[i] < l_check[i+1] for i in range(8))
        True
    """
def solve_system_with_difficult_last_row(B, A):
    """
    Solve the matrix equation ``B*Z = A`` when the last row of `B`
    contains huge entries.

    INPUT:

    - ``B`` -- a square n x n nonsingular matrix with painful big bottom row
    - ``A`` -- an n x k matrix

    OUTPUT: the unique solution to ``B*Z = As``

    EXAMPLES::

        sage: from sage.matrix.matrix_integer_dense_saturation import solve_system_with_difficult_last_row
        sage: B = matrix(ZZ, 3, [1,2,3, 3,-1,2,939239082,39202803080,2939028038402834]); A = matrix(ZZ,3,2,[1,2,4,3,-1,0])
        sage: X = solve_system_with_difficult_last_row(B, A); X
        [  290668794698843/226075992027744         468068726971/409557956572]
        [-226078357385539/1582531944194208       1228691305937/2866905696004]
        [      2365357795/1582531944194208           -17436221/2866905696004]
        sage: B*X == A
        True
    """
def saturation(A, proof: bool = True, p: int = 0, max_dets: int = 5):
    """
    Compute a saturation matrix of `A`.

    INPUT:

    - ``A`` -- a matrix over `\\ZZ`
    - ``proof`` -- boolean (default: ``True``)
    - ``p`` -- integer (default: 0); if not 0 only guarantees that output is
      `p`-saturated
    - ``max_dets`` -- integer (default: 4); max number of dets of submatrices to
      compute

    OUTPUT: matrix; saturation of the matrix `A`

    EXAMPLES::

        sage: from sage.matrix.matrix_integer_dense_saturation import saturation
        sage: A = matrix(ZZ, 2, 2, [3,2,3,4]); B = matrix(ZZ, 2,3,[1,2,3,4,5,6]); C = A*B
        sage: C
        [11 16 21]
        [19 26 33]
        sage: C.index_in_saturation()
        18
        sage: S = saturation(C); S
        [11 16 21]
        [-2 -3 -4]
        sage: S.index_in_saturation()
        1
        sage: saturation(C, proof=False)
        [11 16 21]
        [-2 -3 -4]
        sage: saturation(C, p=2)
        [11 16 21]
        [-2 -3 -4]
        sage: saturation(C, p=2, max_dets=1)
        [11 16 21]
        [-2 -3 -4]
    """
def index_in_saturation(A, proof: bool = True):
    """
    The index of A in its saturation.

    INPUT:

    - ``A`` -- matrix over `\\ZZ`

    - ``proof`` -- boolean (``True`` or ``False``)

    OUTPUT: integer

    EXAMPLES::

        sage: from sage.matrix.matrix_integer_dense_saturation import index_in_saturation
        sage: A = matrix(ZZ, 2, 2, [3,2,3,4]); B = matrix(ZZ, 2,3,[1,2,3,4,5,6]); C = A*B; C
        [11 16 21]
        [19 26 33]
        sage: index_in_saturation(C)
        18
        sage: W = C.row_space()
        sage: S = W.saturation()
        sage: W.index_in(S)
        18

    For any zero matrix the index in its saturation is 1 (see :issue:`13034`)::

        sage: m = matrix(ZZ, 3)
        sage: m
        [0 0 0]
        [0 0 0]
        [0 0 0]
        sage: m.index_in_saturation()
        1
        sage: m = matrix(ZZ, 2, 3)
        sage: m
        [0 0 0]
        [0 0 0]
        sage: m.index_in_saturation()
        1

    TESTS::

        sage: zero = matrix(ZZ, [[]])
        sage: zero.index_in_saturation()
        1
    """
