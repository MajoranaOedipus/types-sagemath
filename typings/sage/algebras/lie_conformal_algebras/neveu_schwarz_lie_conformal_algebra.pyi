from .graded_lie_conformal_algebra import GradedLieConformalAlgebra as GradedLieConformalAlgebra

class NeveuSchwarzLieConformalAlgebra(GradedLieConformalAlgebra):
    """
    The Neveu-Schwarz super Lie conformal algebra.

    INPUT:

    - ``R`` -- a commutative Ring; the base ring of this Lie
      conformal algebra

    EXAMPLES::

        sage: R = lie_conformal_algebras.NeveuSchwarz(AA); R
        The Neveu-Schwarz super Lie conformal algebra over Algebraic Real Field
        sage: R.structure_coefficients()
        Finite family {('G', 'G'): ((0, 2*L), (2, 2/3*C)),  ('G', 'L'): ((0, 1/2*TG), (1, 3/2*G)),  ('L', 'G'): ((0, TG), (1, 3/2*G)),  ('L', 'L'): ((0, TL), (1, 2*L), (3, 1/2*C))}
        sage: R.inject_variables()
        Defining L, G, C
        sage: G.nproduct(G,0)
        2*L
        sage: G.degree()
        3/2
    """
    def __init__(self, R) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: V = lie_conformal_algebras.NeveuSchwarz(QQ)
            sage: TestSuite(V).run()
        """
