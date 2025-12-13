from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring as CategoryWithAxiom_over_base_ring
from sage.categories.graded_modules import GradedModulesCategory as GradedModulesCategory

class LambdaBracketAlgebrasWithBasis(CategoryWithAxiom_over_base_ring):
    """
    The category of Lambda bracket algebras with basis.

    EXAMPLES::

        sage: LieConformalAlgebras(QQbar).WithBasis()                                   # needs sage.rings.number_field
        Category of Lie conformal algebras with basis over Algebraic Field
    """
    class ElementMethods:
        def index(self):
            """
            The index of this basis element.

            EXAMPLES::

                sage: # needs sage.combinat sage.modules
                sage: V = lie_conformal_algebras.NeveuSchwarz(QQ)
                sage: V.inject_variables()
                Defining L, G, C
                sage: G.T(3).index()
                ('G', 3)
                sage: v = V.an_element(); v
                L + G + C
                sage: v.index()
                Traceback (most recent call last):
                ...
                ValueError: index can only be computed for monomials, got L + G + C
            """
    class FinitelyGeneratedAsLambdaBracketAlgebra(CategoryWithAxiom_over_base_ring):
        """
        The category of finitely generated lambda bracket algebras with
        basis.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: C = LieConformalAlgebras(QQbar)
            sage: C1 = C.WithBasis().FinitelyGenerated(); C1
            Category of finitely generated Lie conformal algebras with basis
             over Algebraic Field
            sage: C2 = C.FinitelyGenerated().WithBasis(); C2
            Category of finitely generated Lie conformal algebras with basis
             over Algebraic Field
            sage: C1 is C2
            True
        """
        class Graded(GradedModulesCategory):
            """
            The category of H-graded finitely generated lambda bracket
            algebras with basis.

            EXAMPLES::

                sage: C = LieConformalAlgebras(QQbar)                                   # needs sage.rings.number_field
                sage: C.WithBasis().FinitelyGenerated().Graded()                        # needs sage.rings.number_field
                Category of H-graded finitely generated Lie conformal algebras
                 with basis over Algebraic Field
            """
            class ParentMethods:
                def degree_on_basis(self, m):
                    """
                    Return the degree of the basis element indexed by ``m``
                    in ``self``.

                    EXAMPLES::

                        sage: V = lie_conformal_algebras.Virasoro(QQ)                   # needs sage.combinat sage.modules
                        sage: V.degree_on_basis(('L', 2))                               # needs sage.combinat sage.modules
                        4
                    """
