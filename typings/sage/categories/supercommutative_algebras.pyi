from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring as CategoryWithAxiom_over_base_ring
from sage.categories.signed_tensor import SignedTensorProductsCategory as SignedTensorProductsCategory
from sage.categories.super_algebras import SuperAlgebras as SuperAlgebras
from sage.misc.cachefunc import cached_method as cached_method

class SupercommutativeAlgebras(CategoryWithAxiom_over_base_ring):
    """
    The category of supercommutative algebras.

    An `R`-*supercommutative algebra* is an `R`-super algebra
    `A = A_0 \\oplus A_1` endowed with an `R`-super algebra structure
    satisfying:

    .. MATH::

        x_0 x'_0 = x'_0 x_0, \\qquad
        x_1 x'_1 = -x'_1 x_1, \\qquad
        x_0 x_1 = x_1 x_0,

    for all `x_0, x'_0 \\in A_0` and `x_1, x'_1 \\in A_1`.

    EXAMPLES::

        sage: Algebras(ZZ).Supercommutative()
        Category of supercommutative algebras over Integer Ring

    TESTS::

        sage: TestSuite(Algebras(ZZ).Supercommutative()).run()
    """
    class SignedTensorProducts(SignedTensorProductsCategory):
        @cached_method
        def extra_super_categories(self):
            """
            Return the extra super categories of ``self``.

            A signed tensor product of supercommutative algebras is a
            supercommutative algebra.

            EXAMPLES::

                sage: C = Algebras(ZZ).Supercommutative().SignedTensorProducts()
                sage: C.extra_super_categories()
                [Category of supercommutative algebras over Integer Ring]
            """
    class WithBasis(CategoryWithAxiom_over_base_ring):
        class ParentMethods: ...
