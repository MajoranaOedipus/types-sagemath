from .graded_lie_conformal_algebra import GradedLieConformalAlgebra as GradedLieConformalAlgebra
from sage.matrix.special import identity_matrix as identity_matrix
from sage.structure.indexed_generators import standardize_names_index_set as standardize_names_index_set

class BosonicGhostsLieConformalAlgebra(GradedLieConformalAlgebra):
    """
    The Bosonic ghosts or `\\beta-\\gamma`-system Lie conformal
    algebra.

    INPUT:

    - ``R`` -- a commutative ring
    - ``ngens`` -- an even positive Integer (default: ``2``); the
      number of non-central generators of this Lie conformal
      algebra.
    - ``names`` -- list of ``str``; alternative names for the
      generators
    - ``index_set`` -- an enumerated set; an indexing set for the
      generators

    OUTPUT:

    The Bosonic Ghosts Lie conformal algebra with generators
    `\\beta_i,\\gamma_i, i=1,\\ldots,n` and `K`, where `2n` is
    ``ngens``.

    EXAMPLES::

        sage: R = lie_conformal_algebras.BosonicGhosts(QQ); R
        The Bosonic ghosts Lie conformal algebra with generators (beta, gamma, K) over Rational Field
        sage: R.inject_variables(); beta.bracket(gamma)
        Defining beta, gamma, K
        {0: K}
        sage: beta.degree()
        1
        sage: gamma.degree()
        0

        sage: R = lie_conformal_algebras.BosonicGhosts(QQbar, ngens = 4, names = 'abcd'); R
        The Bosonic ghosts Lie conformal algebra with generators (a, b, c, d, K) over Algebraic Field
        sage: R.structure_coefficients()
        Finite family {('a', 'c'): ((0, K),),  ('b', 'd'): ((0, K),),  ('c', 'a'): ((0, -K),),  ('d', 'b'): ((0, -K),)}

    TESTS::

        sage: lie_conformal_algebras.BosonicGhosts(AA).category()
        Category of H-graded finitely generated Lie conformal algebras with basis over Algebraic Real Field
    """
    def __init__(self, R, ngens: int = 2, names=None, index_set=None) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: V = lie_conformal_algebras.BosonicGhosts(QQ)
            sage: TestSuite(V).run()
        """
