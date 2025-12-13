from sage.categories.category_singleton import Category_singleton as Category_singleton
from sage.categories.category_with_axiom import CategoryWithAxiom as CategoryWithAxiom
from sage.categories.sets_cat import Sets as Sets
from sage.misc.abstract_method import abstract_method as abstract_method
from sage.misc.cachefunc import cached_method as cached_method

class SimplicialComplexes(Category_singleton):
    """
    The category of abstract simplicial complexes.

    An abstract simplicial complex `A` is a collection of sets `X`
    such that:

    - `\\emptyset \\in A`,
    - if `X \\subset Y \\in A`, then `X \\in A`.

    .. TODO::

        Implement the category of simplicial complexes considered
        as :class:`CW complexes <sage.categories.cw_complexes.CWComplexes>`
        and rename this to the category of ``AbstractSimplicialComplexes``
        with appropriate functors.

    EXAMPLES::

        sage: from sage.categories.simplicial_complexes import SimplicialComplexes
        sage: C = SimplicialComplexes(); C
        Category of simplicial complexes

    TESTS::

        sage: TestSuite(C).run()
    """
    @cached_method
    def super_categories(self):
        """
        Return the super categories of ``self``.

        EXAMPLES::

            sage: from sage.categories.simplicial_complexes import SimplicialComplexes
            sage: SimplicialComplexes().super_categories()
            [Category of sets]
        """
    class Finite(CategoryWithAxiom):
        """
        Category of finite simplicial complexes.
        """
        class ParentMethods:
            @cached_method
            def dimension(self):
                """
                Return the dimension of ``self``.

                EXAMPLES::

                    sage: S = SimplicialComplex([[1,3,4], [1,2],[2,5],[4,5]])           # needs sage.graphs
                    sage: S.dimension()                                                 # needs sage.graphs
                    2
                """
    class ParentMethods:
        @abstract_method
        def facets(self) -> None:
            """
            Return the facets of ``self``.

            EXAMPLES::

                sage: S = SimplicialComplex([[1,3,4], [1,2],[2,5],[4,5]])               # needs sage.graphs
                sage: sorted(S.facets())                                                # needs sage.graphs
                [(1, 2), (1, 3, 4), (2, 5), (4, 5)]
            """
        @abstract_method
        def faces(self) -> None:
            """
            Return the faces of ``self``.

            EXAMPLES::

                sage: S = SimplicialComplex([[1,3,4], [1,2],[2,5],[4,5]])               # needs sage.graphs
                sage: S.faces()                                                         # needs sage.graphs
                {-1: {()},
                 0: {(1,), (2,), (3,), (4,), (5,)},
                 1: {(1, 2), (1, 3), (1, 4), (2, 5), (3, 4), (4, 5)},
                 2: {(1, 3, 4)}}
            """
    class SubcategoryMethods:
        @cached_method
        def Connected(self):
            """
            Return the full subcategory of the connected objects of ``self``.

            EXAMPLES::

                sage: from sage.categories.simplicial_complexes import SimplicialComplexes
                sage: SimplicialComplexes().Connected()
                Category of connected simplicial complexes

            TESTS::

                sage: SimplicialComplexes().Connected.__module__
                'sage.categories.simplicial_complexes'
            """
    class Connected(CategoryWithAxiom):
        """
        The category of connected simplicial complexes.

        EXAMPLES::

            sage: from sage.categories.simplicial_complexes import SimplicialComplexes
            sage: C = SimplicialComplexes().Connected()
            sage: TestSuite(C).run()
        """
