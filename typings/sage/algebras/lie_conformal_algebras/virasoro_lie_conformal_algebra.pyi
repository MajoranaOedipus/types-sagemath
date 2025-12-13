from .graded_lie_conformal_algebra import GradedLieConformalAlgebra as GradedLieConformalAlgebra

class VirasoroLieConformalAlgebra(GradedLieConformalAlgebra):
    """
    The Virasoro Lie Conformal algebra over `R`.

    INPUT:

    - ``R`` -- a commutative ring; behaviour is undefined if `R` is
      not a Field of characteristic zero

    EXAMPLES::

        sage: Vir = lie_conformal_algebras.Virasoro(QQ)
        sage: Vir.category()
        Category of H-graded finitely generated Lie conformal algebras with basis over Rational Field
        sage: Vir.inject_variables()
        Defining L, C
        sage: L.bracket(L)
        {0: TL, 1: 2*L, 3: 1/2*C}

    TESTS::

        sage: Vir.gens()
        (L, C)
    """
    def __init__(self, R) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: V = lie_conformal_algebras.Virasoro(QQ)
            sage: TestSuite(V).run()
        """
