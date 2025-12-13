from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring as CategoryWithAxiom_over_base_ring
from sage.categories.graded_modules import GradedModulesCategory as GradedModulesCategory
from sage.categories.lambda_bracket_algebras import LambdaBracketAlgebras as LambdaBracketAlgebras

class FinitelyGeneratedLambdaBracketAlgebras(CategoryWithAxiom_over_base_ring):
    """
    The category of finitely generated lambda bracket algebras.

    EXAMPLES::

        sage: from sage.categories.lambda_bracket_algebras import LambdaBracketAlgebras
        sage: LambdaBracketAlgebras(QQbar).FinitelyGenerated()                          # needs sage.rings.number_field
        Category of finitely generated lambda bracket algebras over Algebraic Field
    """
    class ParentMethods:
        def ngens(self):
            """
            The number of generators of this Lie conformal algebra.

            EXAMPLES::

                sage: Vir = lie_conformal_algebras.Virasoro(QQ)                         # needs sage.combinat sage.modules
                sage: Vir.ngens()                                                       # needs sage.combinat sage.modules
                2

                sage: V = lie_conformal_algebras.Affine(QQ, 'A2')                       # needs sage.combinat sage.modules
                sage: V.ngens()                                                         # needs sage.combinat sage.modules
                9
            """
        def gen(self, i):
            """
            The ``i``-th generator of this Lie conformal algebra.

            EXAMPLES::

                sage: # needs sage.combinat sage.modules
                sage: V = lie_conformal_algebras.Affine(QQ, 'A1')
                sage: V.gens()
                (B[alpha[1]], B[alphacheck[1]], B[-alpha[1]], B['K'])
                sage: V.gen(0)
                B[alpha[1]]
                sage: V.1
                B[alphacheck[1]]
            """
        def some_elements(self):
            """
            Some elements of this Lie conformal algebra.

            This method returns a list with elements containing at
            least the generators.

            EXAMPLES::

                sage: V = lie_conformal_algebras.Affine(QQ, 'A1',                       # needs sage.combinat sage.modules
                ....:                                   names=('e', 'h', 'f'))
                sage: V.some_elements()                                                 # needs sage.combinat sage.modules
                [e, h, f, K, ...]
                sage: all(v.parent() is V for v in V.some_elements())                   # needs sage.combinat sage.modules
                True
            """
    class Graded(GradedModulesCategory):
        """
        The category of H-graded finitely generated Lie conformal algebras.

        EXAMPLES::

            sage: LieConformalAlgebras(QQbar).FinitelyGenerated().Graded()              # needs sage.rings.number_field
            Category of H-graded finitely generated Lie conformal algebras
             over Algebraic Field
        """
