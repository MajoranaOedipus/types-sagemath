from sage.categories.graded_modules import GradedModulesCategory as GradedModulesCategory
from sage.categories.signed_tensor import SignedTensorProductsCategory as SignedTensorProductsCategory
from sage.misc.cachefunc import cached_method as cached_method

class GradedCoalgebras(GradedModulesCategory):
    """
    The category of graded coalgebras.

    EXAMPLES::

        sage: C = GradedCoalgebras(QQ); C
        Category of graded coalgebras over Rational Field
        sage: C is Coalgebras(QQ).Graded()
        True

    TESTS::

        sage: TestSuite(C).run()
    """
    class SubcategoryMethods:
        def SignedTensorProducts(self):
            """
            Return the full subcategory of objects of ``self`` constructed
            as signed tensor products.

            .. SEEALSO::

                - :class:`~sage.categories.signed_tensor.SignedTensorProductsCategory`
                - :class:`~.covariant_functorial_construction.CovariantFunctorialConstruction`

            EXAMPLES::

                sage: CoalgebrasWithBasis(QQ).Graded().SignedTensorProducts()
                Category of signed tensor products of graded coalgebras with basis
                 over Rational Field
            """
    class SignedTensorProducts(SignedTensorProductsCategory):
        @cached_method
        def extra_super_categories(self):
            """
            EXAMPLES::

                sage: Coalgebras(QQ).Graded().SignedTensorProducts().extra_super_categories()
                [Category of graded coalgebras over Rational Field]
                sage: Coalgebras(QQ).Graded().SignedTensorProducts().super_categories()
                [Category of graded coalgebras over Rational Field]

            Meaning: a signed tensor product of coalgebras is a coalgebra
            """
