from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring as CategoryWithAxiom_over_base_ring
from sage.categories.graded_lie_conformal_algebras import GradedLieConformalAlgebrasCategory as GradedLieConformalAlgebrasCategory
from sage.categories.graded_modules import GradedModulesCategory as GradedModulesCategory
from sage.categories.super_modules import SuperModulesCategory as SuperModulesCategory

class LieConformalAlgebrasWithBasis(CategoryWithAxiom_over_base_ring):
    """
    The category of Lie conformal algebras with basis.

    EXAMPLES::

        sage: LieConformalAlgebras(QQbar).WithBasis()                                   # needs sage.rings.number_field
        Category of Lie conformal algebras with basis over Algebraic Field
    """
    class Super(SuperModulesCategory):
        """
        The category of super Lie conformal algebras with basis.

        EXAMPLES::

            sage: LieConformalAlgebras(AA).WithBasis().Super()                          # needs sage.rings.number_field
            Category of super Lie conformal algebras with basis
             over Algebraic Real Field
        """
        class ParentMethods: ...
        class Graded(GradedLieConformalAlgebrasCategory):
            """
            The category of H-graded super Lie conformal algebras with basis.

            EXAMPLES::

                sage: LieConformalAlgebras(QQbar).WithBasis().Super().Graded()          # needs sage.rings.number_field
                Category of H-graded super Lie conformal algebras with basis
                 over Algebraic Field
            """
    class Graded(GradedLieConformalAlgebrasCategory):
        """
        The category of H-graded Lie conformal algebras with basis.

        EXAMPLES::

            sage: LieConformalAlgebras(QQbar).WithBasis().Graded()                      # needs sage.rings.number_field
            Category of H-graded Lie conformal algebras with basis over Algebraic Field
        """
    class FinitelyGeneratedAsLambdaBracketAlgebra(CategoryWithAxiom_over_base_ring):
        """
        The category of finitely generated Lie conformal
        algebras with basis.

        EXAMPLES::

            sage: C = LieConformalAlgebras(QQbar)                                       # needs sage.rings.number_field
            sage: CWF = C.WithBasis().FinitelyGenerated(); CWF                          # needs sage.rings.number_field
            Category of finitely generated Lie conformal algebras with basis
             over Algebraic Field
            sage: CWF is C.FinitelyGenerated().WithBasis()                              # needs sage.rings.number_field
            True
        """
        class Super(SuperModulesCategory):
            """
            The category of super finitely generated Lie conformal
            algebras with basis.

            EXAMPLES::

                sage: LieConformalAlgebras(AA).WithBasis().FinitelyGenerated().Super()  # needs sage.rings.number_field
                Category of super finitely generated Lie conformal algebras with basis
                 over Algebraic Real Field
            """
            class Graded(GradedModulesCategory):
                """
                The category of H-graded super finitely generated Lie
                conformal algebras with basis.

                EXAMPLES::

                    sage: C = LieConformalAlgebras(QQbar).WithBasis().FinitelyGenerated()           # needs sage.rings.number_field
                    sage: C.Graded().Super()                                                        # needs sage.rings.number_field
                    Category of H-graded super finitely generated Lie conformal algebras
                     with basis over Algebraic Field
                    sage: C.Graded().Super() is C.Super().Graded()                                  # needs sage.rings.number_field
                    True
                """
        class Graded(GradedLieConformalAlgebrasCategory):
            """
            The category of H-graded finitely generated Lie conformal
            algebras with basis.

            EXAMPLES::

                sage: LieConformalAlgebras(QQbar).WithBasis().FinitelyGenerated().Graded()          # needs sage.rings.number_field
                Category of H-graded finitely generated Lie conformal algebras with basis
                 over Algebraic Field
            """
