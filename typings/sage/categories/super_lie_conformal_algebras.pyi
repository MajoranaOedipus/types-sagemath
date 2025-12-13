from sage.categories.graded_modules import GradedModulesCategory as GradedModulesCategory
from sage.categories.lambda_bracket_algebras import LambdaBracketAlgebras as LambdaBracketAlgebras
from sage.categories.super_modules import SuperModulesCategory as SuperModulesCategory
from sage.misc.abstract_method import abstract_method as abstract_method

class SuperLieConformalAlgebras(SuperModulesCategory):
    """
    The category of super Lie conformal algebras.

    EXAMPLES::

        sage: LieConformalAlgebras(AA).Super()                                          # needs sage.rings.number_field
        Category of super Lie conformal algebras over Algebraic Real Field

    Notice that we can force to have a *purely even* super Lie
    conformal algebra::

        sage: bosondict = {('a','a'): {1:{('K',0):1}}}
        sage: R = LieConformalAlgebra(QQ, bosondict, names=('a',),                      # needs sage.combinat sage.modules
        ....:                         central_elements=('K',), super=True)
        sage: [g.is_even_odd() for g in R.gens()]                                       # needs sage.combinat sage.modules
        [0, 0]
    """
    def extra_super_categories(self):
        """
        The extra super categories of ``self``.

        EXAMPLES::

            sage: LieConformalAlgebras(QQ).Super().super_categories()
            [Category of super modules over Rational Field,
             Category of Lambda bracket algebras over Rational Field]
        """
    def example(self):
        """
        An example parent in this category.

        EXAMPLES::

            sage: LieConformalAlgebras(QQ).Super().example()                            # needs sage.combinat sage.modules
            The Neveu-Schwarz super Lie conformal algebra over Rational Field
        """
    class ParentMethods: ...
    class ElementMethods:
        @abstract_method
        def is_even_odd(self) -> None:
            """
            Return ``0`` if this element is *even* and ``1`` if it is
            *odd*.

            EXAMPLES::

                sage: R = lie_conformal_algebras.NeveuSchwarz(QQ)                       # needs sage.combinat sage.modules
                sage: R.inject_variables()                                              # needs sage.combinat sage.modules
                Defining L, G, C
                sage: G.is_even_odd()                                                   # needs sage.combinat sage.modules
                1
            """
    class Graded(GradedModulesCategory):
        """
        The category of H-graded super Lie conformal algebras.

        EXAMPLES::

            sage: LieConformalAlgebras(AA).Super().Graded()                             # needs sage.rings.number_field
            Category of H-graded super Lie conformal algebras over Algebraic Real Field
        """
