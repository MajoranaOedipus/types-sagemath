from sage.matrix.constructor import matrix as matrix
from sage.rings.integer_ring import ZZ as ZZ

def gram_schmidt(B):
    """
    Return the Gram-Schmidt orthogonalization of the entries in the list
    B of vectors, along with the matrix mu of Gram-Schmidt coefficients.

    Note that the output vectors need not have unit length. We do this
    to avoid having to extract square roots.

    .. NOTE::

        Use of this function is discouraged.  It fails on linearly
        dependent input and its output format is not as natural as it
        could be.  Instead, see :meth:`sage.matrix.matrix2.Matrix2.gram_schmidt`
        which is safer and more general-purpose.

    EXAMPLES::

        sage: B = [vector([1,2,1/5]), vector([1,2,3]), vector([-1,0,0])]
        sage: from sage.modules.misc import gram_schmidt
        sage: G, mu = gram_schmidt(B)
        sage: G
        [(1, 2, 1/5), (-1/9, -2/9, 25/9), (-4/5, 2/5, 0)]
        sage: G[0] * G[1]
        0
        sage: G[0] * G[2]
        0
        sage: G[1] * G[2]
        0
        sage: mu
        [      0       0       0]
        [   10/9       0       0]
        [-25/126    1/70       0]
        sage: a = matrix([])
        sage: a.gram_schmidt()
        ([], [])
        sage: a = matrix([[],[],[],[]])
        sage: a.gram_schmidt()
         ([], [])

    Linearly dependent input leads to a zero dot product in a denominator.
    This shows that :issue:`10791` is fixed. ::

        sage: from sage.modules.misc import gram_schmidt
        sage: V = [vector(ZZ,[1,1]), vector(ZZ,[2,2]), vector(ZZ,[1,2])]
        sage: gram_schmidt(V)
        Traceback (most recent call last):
        ...
        ValueError: linearly dependent input for module version of Gram-Schmidt

    TESTS::

        sage: from sage.modules.misc import gram_schmidt
        sage: V = []
        sage: gram_schmidt(V)
        ([], [])
        sage: V = [vector(ZZ,[0])]
        sage: gram_schmidt(V)
        Traceback (most recent call last):
        ...
        ValueError: linearly dependent input for module version of Gram-Schmidt
    """
