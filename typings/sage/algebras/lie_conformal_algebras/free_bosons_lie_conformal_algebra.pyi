from .graded_lie_conformal_algebra import GradedLieConformalAlgebra as GradedLieConformalAlgebra
from sage.matrix.special import identity_matrix as identity_matrix
from sage.structure.indexed_generators import standardize_names_index_set as standardize_names_index_set

class FreeBosonsLieConformalAlgebra(GradedLieConformalAlgebra):
    """
    The Free Bosons Lie conformal algebra.

    INPUT:

    - ``R`` -- a commutative ring
    - ``ngens`` -- a positive Integer (default: `1`); the number of
      non-central generators of this Lie conformal algebra.
    - ``gram_matrix`` -- a symmetric square matrix with coefficients
      in ``R`` (default: ``identity_matrix(ngens)``); the Gram
      matrix of the inner product
    - ``names`` -- tuple of strings; alternative names for the
      generators
    - ``index_set`` -- an enumerated set; alternative indexing set
      for the generators

    OUTPUT:

    The Free Bosons Lie conformal algebra with generators
     `\\alpha_i`, `i=1,...,n` and `\\lambda`-brackets

     .. MATH::

        [{\\alpha_i}_{\\lambda} \\alpha_j] = \\lambda M_{ij} K,

    where `n` is the number of generators ``ngens`` and `M` is
    the ``gram_matrix``. This Lie conformal
    algebra is `H`-graded where every generator has conformal weight
    `1`.

    EXAMPLES::

        sage: R = lie_conformal_algebras.FreeBosons(AA); R
        The free Bosons Lie conformal algebra with generators (alpha, K) over Algebraic Real Field
        sage: R.inject_variables()
        Defining alpha, K
        sage: alpha.bracket(alpha)
        {1: K}
        sage: M = identity_matrix(QQ,2); R = lie_conformal_algebras.FreeBosons(QQ,gram_matrix=M, names='alpha,beta'); R
        The free Bosons Lie conformal algebra with generators (alpha, beta, K) over Rational Field
        sage: R.inject_variables(); alpha.bracket(beta)
        Defining alpha, beta, K
        {}
        sage: alpha.bracket(alpha)
        {1: K}
        sage: R = lie_conformal_algebras.FreeBosons(QQbar, ngens=3); R
        The free Bosons Lie conformal algebra with generators (alpha0, alpha1, alpha2, K) over Algebraic Field

    TESTS::
        sage: R = lie_conformal_algebras.FreeBosons(QQ); R.0.degree()
        1
        sage: R = lie_conformal_algebras.FreeBosons(QQbar, ngens=2, gram_matrix=identity_matrix(QQ,1,1))
        Traceback (most recent call last):
        ...
        ValueError: the gram_matrix should be a symmetric 2 x 2 matrix, got [1]
        sage: R = lie_conformal_algebras.FreeBosons(QQbar, ngens=2, gram_matrix=Matrix(QQ,[[0,1],[-1,0]]))
        Traceback (most recent call last):
        ...
        ValueError: the gram_matrix should be a symmetric 2 x 2 matrix, got [ 0  1]
        [-1  0]
    """
    def __init__(self, R, ngens=None, gram_matrix=None, names=None, index_set=None) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: V = lie_conformal_algebras.FreeBosons(QQ)
            sage: TestSuite(V).run()
        """
    def gram_matrix(self):
        """
        The Gram matrix that specifies the `\\lambda`-brackets of the
        generators.

        EXAMPLES::

            sage: R = lie_conformal_algebras.FreeBosons(QQ,ngens=2);
            sage: R.gram_matrix()
            [1 0]
            [0 1]
        """
