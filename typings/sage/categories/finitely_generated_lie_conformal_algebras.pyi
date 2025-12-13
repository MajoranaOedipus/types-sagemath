from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring as CategoryWithAxiom_over_base_ring
from sage.categories.graded_modules import GradedModulesCategory as GradedModulesCategory
from sage.categories.lie_conformal_algebras import LieConformalAlgebras as LieConformalAlgebras
from sage.categories.super_modules import SuperModulesCategory as SuperModulesCategory

class FinitelyGeneratedLieConformalAlgebras(CategoryWithAxiom_over_base_ring):
    """
    The category of finitely generated Lie conformal algebras.

    EXAMPLES::

        sage: LieConformalAlgebras(QQbar).FinitelyGenerated()                           # needs sage.rings.number_field
        Category of finitely generated Lie conformal algebras over Algebraic Field
    """
    class ParentMethods:
        def some_elements(self):
            """
            Some elements of this Lie conformal algebra.

            Returns a list with elements containing at least the
            generators.

            EXAMPLES::

                sage: V = lie_conformal_algebras.Affine(QQ, 'A1',                       # needs sage.combinat sage.modules
                ....:                                   names=('e', 'h', 'f'))
                sage: V.some_elements()                                                 # needs sage.combinat sage.modules
                [e, h, f, K, ...]
                sage: all(v.parent() is V for v in V.some_elements())                   # needs sage.combinat sage.modules
                True
            """
    class Super(SuperModulesCategory):
        """
        The category of super finitely generated Lie conformal algebras.

        EXAMPLES::

            sage: LieConformalAlgebras(AA).FinitelyGenerated().Super()                  # needs sage.rings.number_field
            Category of super finitely generated Lie conformal algebras
             over Algebraic Real Field
        """
        class Graded(GradedModulesCategory):
            """
            The category of H-graded super finitely generated Lie conformal algebras.

            EXAMPLES::

                sage: LieConformalAlgebras(QQbar).FinitelyGenerated().Super().Graded()  # needs sage.rings.number_field
                Category of H-graded super finitely generated Lie conformal algebras
                 over Algebraic Field
            """
    class Graded(GradedModulesCategory):
        """
        The category of H-graded finitely generated Lie conformal algebras.

        EXAMPLES::

            sage: LieConformalAlgebras(QQbar).FinitelyGenerated().Graded()              # needs sage.rings.number_field
            Category of H-graded finitely generated Lie conformal algebras
             over Algebraic Field
        """
