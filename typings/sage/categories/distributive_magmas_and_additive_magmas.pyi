from _typeshed import Incomplete
from sage.categories.cartesian_product import CartesianProductsCategory as CartesianProductsCategory
from sage.categories.category_with_axiom import CategoryWithAxiom as CategoryWithAxiom
from sage.misc.lazy_import import LazyImport as LazyImport

class DistributiveMagmasAndAdditiveMagmas(CategoryWithAxiom):
    """
    The category of sets `(S, +, *)` with `*` distributing on `+`.

    This is similar to a ring, but `+` and `*` are only required to be
    (additive) magmas.

    EXAMPLES::

        sage: from sage.categories.distributive_magmas_and_additive_magmas import DistributiveMagmasAndAdditiveMagmas
        sage: C = DistributiveMagmasAndAdditiveMagmas(); C
        Category of distributive magmas and additive magmas
        sage: C.super_categories()
        [Category of magmas and additive magmas]

    TESTS::

        sage: from sage.categories.magmas_and_additive_magmas import MagmasAndAdditiveMagmas
        sage: C is MagmasAndAdditiveMagmas().Distributive()
        True
        sage: C is (Magmas() & AdditiveMagmas()).Distributive()
        True
        sage: TestSuite(C).run()
    """
    class AdditiveAssociative(CategoryWithAxiom):
        class AdditiveCommutative(CategoryWithAxiom):
            class AdditiveUnital(CategoryWithAxiom):
                class Associative(CategoryWithAxiom):
                    AdditiveInverse: Incomplete
                    Unital: Incomplete
    class ParentMethods: ...
    class CartesianProducts(CartesianProductsCategory):
        def extra_super_categories(self):
            """
            Implement the fact that a Cartesian product of magmas distributing
            over additive magmas is a magma distributing over an
            additive magma.

            EXAMPLES::

                sage: C = (Magmas() & AdditiveMagmas()).Distributive().CartesianProducts()
                sage: C.extra_super_categories()
                [Category of distributive magmas and additive magmas]
                sage: C.axioms()
                frozenset({'Distributive'})
            """
