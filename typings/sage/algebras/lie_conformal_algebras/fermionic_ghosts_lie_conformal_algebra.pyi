from .graded_lie_conformal_algebra import GradedLieConformalAlgebra as GradedLieConformalAlgebra

class FermionicGhostsLieConformalAlgebra(GradedLieConformalAlgebra):
    """
    The Fermionic ghosts or `bc`-system super Lie conformal algebra.

    INPUT:

    - ``R`` -- a commutative ring; the base ring of this Lie
      conformal algebra
    - ``ngens`` -- an even positive Integer (default: ``2``); the
      number of non-central generators of this Lie conformal
      algebra
    - ``names`` -- tuple of strings; alternative names for the
      generators
    - ``index_set`` -- an enumerated set; alternative indexing
      set for the generators

    OUTPUT:

    The Fermionic Ghosts super Lie conformal algebra with generators
    `b_i,c_i, i=1,\\ldots,n` and `K` where `2n` is ``ngens``.

    EXAMPLES::

        sage: R = lie_conformal_algebras.FermionicGhosts(QQ); R
        The Fermionic ghosts Lie conformal algebra with generators (b, c, K) over Rational Field
        sage: R.inject_variables()
        Defining b, c, K
        sage: b.bracket(c) == c.bracket(b)
        True
        sage: b.degree()
        1
        sage: c.degree()
        0
        sage: R.category()
        Category of H-graded super finitely generated Lie conformal algebras with basis over Rational Field

        sage: R = lie_conformal_algebras.FermionicGhosts(QQbar, ngens=4, names = 'abcd');R
        The Fermionic ghosts Lie conformal algebra with generators (a, b, c, d, K) over Algebraic Field
        sage: R.structure_coefficients()
        Finite family {('a', 'c'): ((0, K),),  ('b', 'd'): ((0, K),),  ('c', 'a'): ((0, K),),  ('d', 'b'): ((0, K),)}
    """
    def __init__(self, R, ngens: int = 2, names=None, index_set=None) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: V = lie_conformal_algebras.BosonicGhosts(QQ)
            sage: TestSuite(V).run()
        """
