from .linear_code import LinearCode as LinearCode
from sage.features.gap import GapPackage as GapPackage
from sage.libs.gap.libgap import libgap as libgap
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.misc.randstate import current_randstate as current_randstate

def QuasiQuadraticResidueCode(p):
    """
    A (binary) quasi-quadratic residue code (or QQR code).

    Follows the definition of Proposition 2.2 in [BM2003]_. The code has a generator
    matrix in the block form `G=(Q,N)`. Here `Q` is a `p \\times p` circulant
    matrix whose top row is `(0,x_1,...,x_{p-1})`, where `x_i=1` if and only if
    `i` is a quadratic residue mod `p`, and `N` is a `p \\times p` circulant
    matrix whose top row is `(0,y_1,...,y_{p-1})`, where `x_i+y_i=1` for all
    `i`.

    INPUT:

    - ``p`` -- a prime `>2`

    OUTPUT: a QQR code of length `2p`

    EXAMPLES::

        sage: C = codes.QuasiQuadraticResidueCode(11); C   # optional - gap_package_guava
        [22, 11] linear code over GF(2)

    These are self-orthogonal in general and self-dual when `p \\equiv 3 \\pmod 4`.

    AUTHOR: David Joyner (11-2005)
    """
def RandomLinearCodeGuava(n, k, F):
    '''
    The method used is to first construct a `k \\times n` matrix of the block
    form `(I,A)`, where `I` is a `k \\times k` identity matrix and `A` is a
    `k \\times (n-k)` matrix constructed using random elements of `F`. Then
    the columns are permuted using a randomly selected element of the symmetric
    group `S_n`.

    INPUT:

    - ``n``, ``k`` -- integers with `n>k>1`

    OUTPUT: a "random" linear code with length `n`, dimension `k` over field `F`

    EXAMPLES::

        sage: C = codes.RandomLinearCodeGuava(30,15,GF(2)); C      # optional - gap_package_guava
        [30, 15] linear code over GF(2)
        sage: C = codes.RandomLinearCodeGuava(10,5,GF(4,\'a\')); C   # optional - gap_package_guava
        [10, 5] linear code over GF(4)

    AUTHOR: David Joyner (11-2005)
    '''
