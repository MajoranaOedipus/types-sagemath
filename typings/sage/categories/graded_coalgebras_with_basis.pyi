from sage.categories.graded_modules import GradedModulesCategory as GradedModulesCategory
from sage.categories.signed_tensor import SignedTensorProductsCategory as SignedTensorProductsCategory
from sage.misc.cachefunc import cached_method as cached_method

class GradedCoalgebrasWithBasis(GradedModulesCategory):
    """
    The category of graded coalgebras with a distinguished basis.

    EXAMPLES::

        sage: C = GradedCoalgebrasWithBasis(QQ); C
        Category of graded coalgebras with basis over Rational Field
        sage: C is Coalgebras(QQ).WithBasis().Graded()
        True

    TESTS::

        sage: TestSuite(C).run()
    """
    class SignedTensorProducts(SignedTensorProductsCategory):
        """
        The category of coalgebras with basis constructed by signed tensor
        product of coalgebras with basis.
        """
        @cached_method
        def extra_super_categories(self):
            """
            EXAMPLES::

                sage: Cat = CoalgebrasWithBasis(QQ).Graded()
                sage: Cat.SignedTensorProducts().extra_super_categories()
                [Category of graded coalgebras with basis over Rational Field]
                sage: Cat.SignedTensorProducts().super_categories()
                [Category of graded coalgebras with basis over Rational Field,
                 Category of signed tensor products of graded coalgebras over Rational Field]
            """
