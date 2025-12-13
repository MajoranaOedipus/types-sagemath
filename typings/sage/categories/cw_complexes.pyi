from sage.categories.category_singleton import Category_singleton as Category_singleton
from sage.categories.category_with_axiom import CategoryWithAxiom as CategoryWithAxiom
from sage.categories.sets_cat import Sets as Sets
from sage.misc.abstract_method import abstract_method as abstract_method
from sage.misc.cachefunc import cached_method as cached_method

class CWComplexes(Category_singleton):
    '''
    The category of CW complexes.

    A CW complex is a Closure-finite cell complex in the Weak topology.

    REFERENCES:

    - :wikipedia:`CW_complex`

    .. NOTE::

        The notion of "finite" is that the number of cells is finite.

    EXAMPLES::

        sage: from sage.categories.cw_complexes import CWComplexes
        sage: C = CWComplexes(); C
        Category of CW complexes

    TESTS::

        sage: TestSuite(C).run()
    '''
    @cached_method
    def super_categories(self):
        """
        EXAMPLES::

            sage: from sage.categories.cw_complexes import CWComplexes
            sage: CWComplexes().super_categories()
            [Category of topological spaces]
        """
    class SubcategoryMethods:
        @cached_method
        def Connected(self):
            """
            Return the full subcategory of the connected objects of ``self``.

            EXAMPLES::

                sage: from sage.categories.cw_complexes import CWComplexes
                sage: CWComplexes().Connected()
                Category of connected CW complexes

            TESTS::

                sage: TestSuite(CWComplexes().Connected()).run()
                sage: CWComplexes().Connected.__module__
                'sage.categories.cw_complexes'
            """
        @cached_method
        def FiniteDimensional(self):
            """
            Return the full subcategory of the finite dimensional
            objects of ``self``.

            EXAMPLES::

                sage: from sage.categories.cw_complexes import CWComplexes
                sage: C = CWComplexes().FiniteDimensional(); C
                Category of finite dimensional CW complexes

            TESTS::

                sage: from sage.categories.cw_complexes import CWComplexes
                sage: C = CWComplexes().FiniteDimensional()
                sage: TestSuite(C).run()
                sage: CWComplexes().Connected().FiniteDimensional.__module__
                'sage.categories.cw_complexes'
            """
    class Connected(CategoryWithAxiom):
        """
        The category of connected CW complexes.
        """
    class FiniteDimensional(CategoryWithAxiom):
        """
        Category of finite dimensional CW complexes.
        """
    class Finite(CategoryWithAxiom):
        """
        Category of finite CW complexes.

        A finite CW complex is a CW complex with a finite number of cells.
        """
        def extra_super_categories(self):
            """
            Return the extra super categories of ``self``.

            A finite CW complex is a compact finite-dimensional CW complex.

            EXAMPLES::

                sage: from sage.categories.cw_complexes import CWComplexes
                sage: C = CWComplexes().Finite()
                sage: C.extra_super_categories()
                [Category of finite dimensional CW complexes,
                 Category of compact topological spaces]
            """
        class ParentMethods:
            @cached_method
            def dimension(self):
                """
                Return the dimension of ``self``.

                EXAMPLES::

                    sage: from sage.categories.cw_complexes import CWComplexes
                    sage: X = CWComplexes().example()
                    sage: X.dimension()
                    2
                """
    def Compact_extra_super_categories(self):
        """
        Return extraneous super categories for ``CWComplexes().Compact()``.

        A compact CW complex is finite, see Proposition A.1 in [Hat2002]_.

        .. TODO::

            Fix the name of finite CW complexes.

        EXAMPLES::

            sage: from sage.categories.cw_complexes import CWComplexes
            sage: CWComplexes().Compact() # indirect doctest
            Category of finite finite dimensional CW complexes
            sage: CWComplexes().Compact() is CWComplexes().Finite()
            True
        """
    class ElementMethods:
        @abstract_method
        def dimension(self) -> None:
            """
            Return the dimension of ``self``.

            EXAMPLES::

                sage: from sage.categories.cw_complexes import CWComplexes
                sage: X = CWComplexes().example()
                sage: X.an_element().dimension()
                2
            """
    class ParentMethods:
        @abstract_method
        def dimension(self) -> None:
            """
            Return the dimension of ``self``.

            EXAMPLES::

                sage: from sage.categories.cw_complexes import CWComplexes
                sage: X = CWComplexes().example()
                sage: X.dimension()
                2
            """
        def cells(self) -> None:
            """
            Return the cells of ``self``.

            EXAMPLES::

                sage: from sage.categories.cw_complexes import CWComplexes
                sage: X = CWComplexes().example()
                sage: C = X.cells()
                sage: sorted((d, C[d]) for d in C.keys())
                [(0, (0-cell v,)),
                 (1, (0-cell e1, 0-cell e2)),
                 (2, (2-cell f,))]
            """
