from sage.matrix.constructor import Matrix as Matrix
from sage.rings.finite_rings.integer_mod import mod as mod
from sage.rings.integer_ring import ZZ as ZZ

def collect_small_blocks(G):
    """
    Return the blocks as list.

    INPUT:

    - ``G`` -- a ``block_diagonal`` matrix consisting of
      `1` by `1` and `2` by `2` blocks

    OUTPUT: list of `1` by `1` and `2` by `2` matrices; the blocks

    EXAMPLES::

        sage: from sage.quadratic_forms.genera.normal_form import collect_small_blocks
        sage: W1 = Matrix([1])
        sage: V = Matrix(ZZ, 2, [2, 1, 1, 2])
        sage: L = [W1, V, V, W1, W1, V, W1, V]
        sage: G = Matrix.block_diagonal(L)
        sage: L == collect_small_blocks(G)
        True
    """
def p_adic_normal_form(G, p, precision=None, partial: bool = False, debug: bool = False):
    """
    Return the transformation to the `p`-adic normal form of a symmetric matrix.

    Two ```p`-adic`` quadratic forms are integrally equivalent if and only if
    their Gram matrices have the same normal form.

    Let `p` be odd and `u` be the smallest non-square modulo `p`.
    The normal form is a block diagonal matrix
    with blocks `p^k G_k` such that `G_k` is either the identity matrix or
    the identity matrix with the last diagonal entry replaced by `u`.

    If `p=2` is even, define the `1` by `1` matrices::

        sage: W1 = Matrix([1]); W1
        [1]
        sage: W3 = Matrix([3]); W3
        [3]
        sage: W5 = Matrix([5]); W5
        [5]
        sage: W7 = Matrix([7]); W7
        [7]

    and the `2` by `2` matrices::

        sage: U = Matrix(2,[0,1,1,0]); U
        [0 1]
        [1 0]
        sage: V = Matrix(2,[2,1,1,2]); V
        [2 1]
        [1 2]

    For `p=2` the partial normal form is a block diagonal matrix with blocks
    `2^k G_k` such that `G_k` is a block diagonal matrix of the form
    `[U`, ... , `U`, `V`, `Wa`, `Wb]`
    where we allow `V`, `Wa`, `Wb` to be `0 \\times 0` matrices.

    Further restrictions to the full normal form apply.
    We refer to [MirMor2009]_ IV Definition 4.6. for the details.

    INPUT:

    - ``G`` -- a symmetric `n` by `n` matrix in `\\QQ`
    - ``p`` -- a prime number -- it is not checked whether it is prime
    - ``precision`` -- if not set, the minimal possible is taken
    - ``partial`` -- boolean (default: ``False``); if set, only the
      partial normal form is returned

    OUTPUT:

    - ``D`` -- the jordan matrix over `\\QQ_p`
    - ``B`` -- invertible transformation matrix over `\\ZZ_p`,
      i.e., `D = B * G * B^T`

    EXAMPLES::

        sage: from sage.quadratic_forms.genera.normal_form import p_adic_normal_form
        sage: D4 = Matrix(ZZ, 4, [2,-1,-1,-1,-1,2,0,0,-1,0,2,0,-1,0,0,2])
        sage: D4
        [ 2 -1 -1 -1]
        [-1  2  0  0]
        [-1  0  2  0]
        [-1  0  0  2]
        sage: D, B = p_adic_normal_form(D4, 2)
        sage: D
        [  2   1   0   0]
        [  1   2   0   0]
        [  0   0 2^2   2]
        [  0   0   2 2^2]
        sage: D == B * D4 * B.T
        True
        sage: A4 = Matrix(ZZ, 4, [2, -1, 0, 0, -1, 2, -1, 0, 0, -1, 2, -1, 0, 0, -1, 2])
        sage: A4
        [ 2 -1  0  0]
        [-1  2 -1  0]
        [ 0 -1  2 -1]
        [ 0  0 -1  2]
        sage: D, B = p_adic_normal_form(A4, 2)
        sage: D
        [0 1 0 0]
        [1 0 0 0]
        [0 0 2 1]
        [0 0 1 2]

    We can handle degenerate forms::

        sage: A4_extended = Matrix(ZZ, 5, [2, -1, 0, 0, -1, -1, 2, -1, 0, 0, 0, -1, 2, -1, 0, 0, 0, -1, 2, -1, -1, 0, 0, -1, 2])
        sage: D, B = p_adic_normal_form(A4_extended, 5)
        sage: D
        [1 0 0 0 0]
        [0 1 0 0 0]
        [0 0 1 0 0]
        [0 0 0 5 0]
        [0 0 0 0 0]

    and denominators::

        sage: A4dual = A4.inverse()
        sage: D, B = p_adic_normal_form(A4dual, 5)
        sage: D
        [5^-1    0    0    0]
        [   0    1    0    0]
        [   0    0    1    0]
        [   0    0    0    1]

    TESTS::

        sage: Z = Matrix(ZZ, 0, [])
        sage: p_adic_normal_form(Z, 3)
        ([], [])
        sage: Z = matrix.zero(10)
        sage: p_adic_normal_form(Z, 3)[0] == 0
        True
    """
