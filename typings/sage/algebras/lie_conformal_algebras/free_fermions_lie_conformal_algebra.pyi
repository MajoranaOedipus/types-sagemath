from .graded_lie_conformal_algebra import GradedLieConformalAlgebra as GradedLieConformalAlgebra

class FreeFermionsLieConformalAlgebra(GradedLieConformalAlgebra):
    """
    The Free Fermions Super Lie conformal algebra.

    INPUT:

    - ``R`` -- a commutative ring
    - ``ngens`` -- a positive Integer (default: ``1``); the number of
      non-central generators of this Lie conformal algebra
    - ``gram_matrix`` -- a symmetric square matrix with coefficients
      in ``R`` (default: ``identity_matrix(ngens)``); the Gram
      matrix of the inner product

    OUTPUT:

    The Free Fermions Lie conformal algebra with generators
     `\\psi_i`, `i=1,...,n` and `\\lambda`-brackets

     .. MATH::

        [{\\psi_i}_{\\lambda} \\psi_j] = M_{ij} K,

    where `n` is the number of generators ``ngens`` and `M` is the
    ``gram_matrix``. This super Lie conformal
    algebra is `H`-graded where every generator has degree `1/2`.

    EXAMPLES::

        sage: R = lie_conformal_algebras.FreeFermions(QQbar); R
        The free Fermions super Lie conformal algebra with generators (psi, K) over Algebraic Field
        sage: R.inject_variables()
        Defining psi, K
        sage: psi.bracket(psi)
        {0: K}

        sage: R = lie_conformal_algebras.FreeFermions(QQbar,gram_matrix=Matrix([[0,1],[1,0]])); R
        The free Fermions super Lie conformal algebra with generators (psi_0, psi_1, K) over Algebraic Field
        sage: R.inject_variables()
        Defining psi_0, psi_1, K
        sage: psi_0.bracket(psi_1)
        {0: K}
        sage: psi_0.degree()
        1/2
        sage: R.category()
        Category of H-graded super finitely generated Lie conformal algebras with basis over Algebraic Field
    """
    def __init__(self, R, ngens=None, gram_matrix=None, names=None, index_set=None) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: V = lie_conformal_algebras.FreeFermions(QQ)
            sage: TestSuite(V).run()
        """
    def gram_matrix(self):
        """
        The Gram matrix that specifies the `\\lambda`-brackets of the
        generators.

        EXAMPLES::

            sage: R = lie_conformal_algebras.FreeFermions(QQ,ngens=2);
            sage: R.gram_matrix()
            [1 0]
            [0 1]
        """
