from _typeshed import Incomplete
from sage.categories.additive_magmas import AdditiveMagmas as AdditiveMagmas
from sage.categories.cartesian_product import CartesianProductsCategory as CartesianProductsCategory
from sage.categories.category_singleton import Category_singleton as Category_singleton
from sage.categories.magmas import Magmas as Magmas
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import LazyImport as LazyImport

class MagmasAndAdditiveMagmas(Category_singleton):
    """
    The category of sets `(S, +, *)` with an additive operation '+' and
    a multiplicative operation `*`

    EXAMPLES::

        sage: from sage.categories.magmas_and_additive_magmas import MagmasAndAdditiveMagmas
        sage: C = MagmasAndAdditiveMagmas(); C
        Category of magmas and additive magmas

    This is the base category for the categories of rings and their variants::

        sage: C.Distributive()
        Category of distributive magmas and additive magmas
        sage: C.Distributive().Associative().AdditiveAssociative().AdditiveCommutative().AdditiveUnital().AdditiveInverse()
        Category of rngs
        sage: C.Distributive().Associative().AdditiveAssociative().AdditiveCommutative().AdditiveUnital().Unital()
        Category of semirings
        sage: C.Distributive().Associative().AdditiveAssociative().AdditiveCommutative().AdditiveUnital().AdditiveInverse().Unital()
        Category of rings

    This category is really meant to represent the intersection of the
    categories of :class:`Magmas` and :class:`AdditiveMagmas`; however
    Sage's infrastructure does not allow yet to model this::

        sage: Magmas() & AdditiveMagmas()
        Join of Category of magmas and Category of additive magmas

        sage: Magmas() & AdditiveMagmas()        # todo: not implemented
        Category of magmas and additive magmas

    TESTS::

        sage: TestSuite(MagmasAndAdditiveMagmas()).run()
    """
    class SubcategoryMethods:
        @cached_method
        def Distributive(self):
            """
            Return the full subcategory of the objects of ``self``
            where `*` is distributive on `+`.

            A :class:`magma <Magmas>` and :class:`additive magma
            <AdditiveMagmas>` `M` is *distributive* if, for all
            `x,y,z \\in M`,

            .. MATH::

                x * (y+z) = x*y + x*z \\text{ and } (x+y) * z = x*z + y*z

            EXAMPLES::

                sage: from sage.categories.magmas_and_additive_magmas import MagmasAndAdditiveMagmas
                sage: C = MagmasAndAdditiveMagmas().Distributive(); C
                Category of distributive magmas and additive magmas

            .. NOTE::

                Given that Sage does not know that
                :class:`MagmasAndAdditiveMagmas` is the intersection
                of :class:`Magmas` and :class:`AdditiveMagmas`, this
                method is not available for::

                    sage: Magmas() & AdditiveMagmas()
                    Join of Category of magmas and Category of additive magmas

                Still, the natural syntax works::

                    sage: (Magmas() & AdditiveMagmas()).Distributive()
                    Category of distributive magmas and additive magmas

                thanks to a workaround implemented in
                :meth:`Magmas.SubcategoryMethods.Distributive`::

                    sage: (Magmas() & AdditiveMagmas()).Distributive.__module__
                    'sage.categories.magmas'

            TESTS::

                sage: TestSuite(C).run()
                sage: Fields().Distributive.__module__
                'sage.categories.magmas_and_additive_magmas'
            """
    def super_categories(self):
        """
        EXAMPLES::

            sage: from sage.categories.magmas_and_additive_magmas import MagmasAndAdditiveMagmas
            sage: MagmasAndAdditiveMagmas().super_categories()
            [Category of magmas, Category of additive magmas]
        """
    def additional_structure(self) -> None:
        """
        Return ``None``.

        Indeed, this category is meant to represent the join of
        :class:`AdditiveMagmas` and :class:`Magmas`. As such, it
        defines no additional structure.

        .. SEEALSO:: :meth:`Category.additional_structure`

        EXAMPLES::

            sage: from sage.categories.magmas_and_additive_magmas import MagmasAndAdditiveMagmas
            sage: MagmasAndAdditiveMagmas().additional_structure()
        """
    Distributive: Incomplete
    class CartesianProducts(CartesianProductsCategory):
        def extra_super_categories(self):
            """
            Implement the fact that this structure is stable under Cartesian
            products.

            TESTS::

                sage: from sage.categories.magmas_and_additive_magmas import MagmasAndAdditiveMagmas
                sage: MagmasAndAdditiveMagmas().CartesianProducts().extra_super_categories()
                [Category of magmas and additive magmas]
            """
