from sage.categories.category_singleton import Category_singleton as Category_singleton
from sage.categories.category_with_axiom import CategoryWithAxiom as CategoryWithAxiom
from sage.categories.sets_cat import Sets as Sets
from sage.categories.simplicial_complexes import SimplicialComplexes as SimplicialComplexes
from sage.misc.abstract_method import abstract_method as abstract_method
from sage.misc.cachefunc import cached_method as cached_method

class Graphs(Category_singleton):
    """
    The category of graphs.

    EXAMPLES::

        sage: from sage.categories.graphs import Graphs
        sage: C = Graphs(); C
        Category of graphs

    TESTS::

        sage: TestSuite(C).run()
    """
    @cached_method
    def super_categories(self):
        """
        EXAMPLES::

            sage: from sage.categories.graphs import Graphs
            sage: Graphs().super_categories()
            [Category of simplicial complexes]
        """
    class ParentMethods:
        @abstract_method
        def vertices(self) -> None:
            """
            Return the vertices of ``self``.

            EXAMPLES::

                sage: from sage.categories.graphs import Graphs
                sage: C = Graphs().example()
                sage: C.vertices()
                [0, 1, 2, 3, 4]
            """
        @abstract_method
        def edges(self) -> None:
            """
            Return the edges of ``self``.

            EXAMPLES::

                sage: from sage.categories.graphs import Graphs
                sage: C = Graphs().example()
                sage: C.edges()
                [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]
            """
        def dimension(self):
            """
            Return the dimension of ``self`` as a CW complex.

            EXAMPLES::

                sage: from sage.categories.graphs import Graphs
                sage: C = Graphs().example()
                sage: C.dimension()
                1
            """
        def facets(self):
            """
            Return the facets of ``self``.

            EXAMPLES::

                sage: from sage.categories.graphs import Graphs
                sage: C = Graphs().example()
                sage: C.facets()
                [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]
            """
        def faces(self):
            """
            Return the faces of ``self``.

            EXAMPLES::

                sage: from sage.categories.graphs import Graphs
                sage: C = Graphs().example()
                sage: sorted(C.faces(), key=lambda x: (x.dimension(), x.value))
                [0, 1, 2, 3, 4, (0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]
            """
    class Connected(CategoryWithAxiom):
        """
        The category of connected graphs.

        EXAMPLES::

            sage: from sage.categories.graphs import Graphs
            sage: C = Graphs().Connected()
            sage: TestSuite(C).run()
        """
        def extra_super_categories(self):
            """
            Return the extra super categories of ``self``.

            A connected graph is also a metric space.

            EXAMPLES::

                sage: from sage.categories.graphs import Graphs
                sage: Graphs().Connected().super_categories() # indirect doctest
                [Category of connected topological spaces,
                 Category of connected simplicial complexes,
                 Category of graphs,
                 Category of metric spaces]
            """
