from sage.categories.cartesian_product import CartesianProductsCategory as CartesianProductsCategory
from sage.categories.category_with_axiom import CategoryWithAxiom as CategoryWithAxiom
from sage.categories.covariant_functorial_construction import RegressiveCovariantConstructionCategory as RegressiveCovariantConstructionCategory
from sage.categories.sets_cat import Sets as Sets
from sage.misc.cachefunc import cached_method as cached_method

class TopologicalSpacesCategory(RegressiveCovariantConstructionCategory): ...

class TopologicalSpaces(TopologicalSpacesCategory):
    """
    The category of topological spaces.

    EXAMPLES::

        sage: Sets().Topological()
        Category of topological spaces
        sage: Sets().Topological().super_categories()
        [Category of sets]

    The category of topological spaces defines the topological structure,
    which shall be preserved by morphisms::

        sage: Sets().Topological().additional_structure()
        Category of topological spaces

    TESTS::

        sage: TestSuite(Sets().Topological()).run()
    """
    class CartesianProducts(CartesianProductsCategory):
        def extra_super_categories(self):
            """
            Implement the fact that a (finite) Cartesian product of topological spaces is
            a topological space.

            EXAMPLES::

                sage: from sage.categories.topological_spaces import TopologicalSpaces
                sage: C = TopologicalSpaces().CartesianProducts()
                sage: C.extra_super_categories()
                [Category of topological spaces]
                sage: C.super_categories()
                [Category of Cartesian products of sets, Category of topological spaces]
                sage: C.axioms()
                frozenset()
            """
    class SubcategoryMethods:
        @cached_method
        def Connected(self):
            """
            Return the full subcategory of the connected objects of ``self``.

            EXAMPLES::

                sage: Sets().Topological().Connected()
                Category of connected topological spaces

            TESTS::

                sage: TestSuite(Sets().Topological().Connected()).run()
                sage: Sets().Topological().Connected.__module__
                'sage.categories.topological_spaces'
            """
        @cached_method
        def Compact(self):
            """
            Return the subcategory of the compact objects of ``self``.

            EXAMPLES::

                sage: Sets().Topological().Compact()
                Category of compact topological spaces

            TESTS::

                sage: TestSuite(Sets().Topological().Compact()).run()
                sage: Sets().Topological().Compact.__module__
                'sage.categories.topological_spaces'
            """
    class Connected(CategoryWithAxiom):
        """
        The category of connected topological spaces.
        """
        class CartesianProducts(CartesianProductsCategory):
            def extra_super_categories(self):
                """
                Implement the fact that a (finite) Cartesian product of connected
                topological spaces is connected.

                EXAMPLES::

                    sage: from sage.categories.topological_spaces import TopologicalSpaces
                    sage: C = TopologicalSpaces().Connected().CartesianProducts()
                    sage: C.extra_super_categories()
                    [Category of connected topological spaces]
                    sage: C.super_categories()
                    [Category of Cartesian products of topological spaces,
                     Category of connected topological spaces]
                    sage: C.axioms()
                    frozenset({'Connected'})
                """
    class Compact(CategoryWithAxiom):
        """
        The category of compact topological spaces.
        """
        class CartesianProducts(CartesianProductsCategory):
            def extra_super_categories(self):
                """
                Implement the fact that a (finite) Cartesian product of compact
                topological spaces is compact.

                EXAMPLES::

                    sage: from sage.categories.topological_spaces import TopologicalSpaces
                    sage: C = TopologicalSpaces().Compact().CartesianProducts()
                    sage: C.extra_super_categories()
                    [Category of compact topological spaces]
                    sage: C.super_categories()
                    [Category of Cartesian products of topological spaces,
                     Category of compact topological spaces]
                    sage: C.axioms()
                    frozenset({'Compact'})
                """
