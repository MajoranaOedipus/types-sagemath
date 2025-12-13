from sage.categories.category_types import Category_over_base_ring as Category_over_base_ring
from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring as CategoryWithAxiom_over_base_ring
from sage.categories.fields import Fields as Fields
from sage.categories.sets_cat import Sets as Sets
from sage.misc.cachefunc import cached_method as cached_method

class VectorBundles(Category_over_base_ring):
    """
    The category of vector bundles over any base space and base field.

    .. SEEALSO:: :class:`~sage.manifolds.vector_bundle.TopologicalVectorBundle`

    EXAMPLES::

        sage: M = Manifold(2, 'M', structure='top')
        sage: from sage.categories.vector_bundles import VectorBundles
        sage: C = VectorBundles(M, RR); C
        Category of vector bundles over Real Field with 53 bits of precision
         with base space 2-dimensional topological manifold M
        sage: C.super_categories()
        [Category of topological spaces]

    TESTS::

        sage: TestSuite(C).run(skip='_test_category_over_bases')
    """
    def __init__(self, base_space, base_field, name=None) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: M = Manifold(2, 'M')
            sage: from sage.categories.vector_bundles import VectorBundles
            sage: C = VectorBundles(M, RR)
            sage: TestSuite(C).run(skip='_test_category_over_bases')
        """
    @cached_method
    def super_categories(self):
        """
        EXAMPLES::

            sage: M = Manifold(2, 'M')
            sage: from sage.categories.vector_bundles import VectorBundles
            sage: VectorBundles(M, RR).super_categories()
            [Category of topological spaces]
        """
    def base_space(self):
        """
        Return the base space of this category.

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='top')
            sage: from sage.categories.vector_bundles import VectorBundles
            sage: VectorBundles(M, RR).base_space()
            2-dimensional topological manifold M
        """
    class SubcategoryMethods:
        @cached_method
        def Differentiable(self):
            """
            Return the subcategory of the differentiable objects
            of ``self``.

            EXAMPLES::

                sage: M = Manifold(2, 'M')
                sage: from sage.categories.vector_bundles import VectorBundles
                sage: VectorBundles(M, RR).Differentiable()
                Category of differentiable vector bundles over Real Field with
                 53 bits of precision with base space 2-dimensional
                 differentiable manifold M

            TESTS::

                sage: TestSuite(VectorBundles(M, RR).Differentiable()).run()
                sage: VectorBundles(M, RR).Differentiable.__module__
                'sage.categories.vector_bundles'
            """
        @cached_method
        def Smooth(self):
            """
            Return the subcategory of the smooth objects of ``self``.

            EXAMPLES::

                sage: M = Manifold(2, 'M')
                sage: from sage.categories.vector_bundles import VectorBundles
                sage: VectorBundles(M, RR).Smooth()
                Category of smooth vector bundles over Real Field with 53 bits
                 of precision with base space 2-dimensional differentiable
                 manifold M

            TESTS::

                sage: TestSuite(VectorBundles(M, RR).Smooth()).run()
                sage: VectorBundles(M, RR).Smooth.__module__
                'sage.categories.vector_bundles'
            """
    class Differentiable(CategoryWithAxiom_over_base_ring):
        """
        The category of differentiable vector bundles.

        A differentiable vector bundle is a differentiable manifold with
        differentiable surjective projection on a differentiable base space.
        """
    class Smooth(CategoryWithAxiom_over_base_ring):
        """
        The category of smooth vector bundles.

        A smooth vector bundle is a smooth manifold with
        smooth surjective projection on a smooth base space.
        """
