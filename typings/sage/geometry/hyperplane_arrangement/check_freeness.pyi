from sage.matrix.constructor import matrix as matrix

def less_generators(X):
    """
    Reduce the generator matrix of the module defined by ``X``.

    This is Algorithm 6.4 in [BC2012]_ and relies on the row syzygies of
    the matrix ``X``.

    EXAMPLES::

        sage: from sage.geometry.hyperplane_arrangement.check_freeness import less_generators
        sage: R.<x,y,z> = QQ[]
        sage: m = matrix([[1, 0, 0], [0, z, -1], [0, 0, 0], [0, y, 1]])
        sage: less_generators(m)
        [ 1  0  0]
        [ 0  z -1]
        [ 0  y  1]
    """
def construct_free_chain(A):
    """
    Construct the free chain for the hyperplanes ``A``.

    ALGORITHM:

    We follow Algorithm 6.5 in [BC2012]_.

    INPUT:

    - ``A`` -- a hyperplane arrangement

    EXAMPLES::

        sage: from sage.geometry.hyperplane_arrangement.check_freeness import construct_free_chain
        sage: H.<x,y,z> = HyperplaneArrangements(QQ)
        sage: A = H(z, y+z, x+y+z)
        sage: construct_free_chain(A)
        [
        [1 0 0]  [ 1  0  0]  [    0     1     0]
        [0 1 0]  [ 0  z -1]  [y + z     0    -1]
        [0 0 z], [ 0  y  1], [    x     0     1]
        ]
    """
