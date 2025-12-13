from sage.categories.cw_complexes import CWComplexes as CWComplexes
from sage.sets.family import Family as Family
from sage.structure.element import Element as Element
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class Surface(UniqueRepresentation, Parent):
    """
    An example of a CW complex: a (2-dimensional) surface.

    This class illustrates a minimal implementation of a CW complex.

    EXAMPLES::

        sage: from sage.categories.cw_complexes import CWComplexes
        sage: X = CWComplexes().example(); X
        An example of a CW complex: the surface given by the boundary map (1, 2, 1, 2)

        sage: X.category()
        Category of finite finite dimensional CW complexes

    We conclude by running systematic tests on this manifold::

        sage: TestSuite(X).run()
    """
    def __init__(self, bdy=(1, 2, 1, 2)) -> None:
        """
        EXAMPLES::

            sage: from sage.categories.cw_complexes import CWComplexes
            sage: X = CWComplexes().example((1, 2)); X
            An example of a CW complex: the surface given by the boundary map (1, 2)

        TESTS::

            sage: TestSuite(X).run()
        """
    def cells(self):
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
    def an_element(self):
        """
        Return an element of the CW complex, as per
        :meth:`Sets.ParentMethods.an_element`.

        EXAMPLES::

            sage: from sage.categories.cw_complexes import CWComplexes
            sage: X = CWComplexes().example()
            sage: X.an_element()
            2-cell f
        """
    class Element(Element):
        """
        A cell in a CW complex.
        """
        def __init__(self, parent, dim, name) -> None:
            """
            Initialize ``self``.

            EXAMPLES::

                sage: from sage.categories.cw_complexes import CWComplexes
                sage: X = CWComplexes().example()
                sage: f = X.an_element()
                sage: TestSuite(f).run()
            """
        def __eq__(self, other):
            """
            Check equality.

            EXAMPLES::

                sage: from sage.categories.cw_complexes import CWComplexes
                sage: X = CWComplexes().example()
                sage: f = X.an_element()
                sage: f == X(2, 'f')
                True
                sage: e1 = X(1, 'e1')
                sage: e1 == f
                False
            """
        def dimension(self):
            """
            Return the dimension of ``self``.

            EXAMPLES::

                sage: from sage.categories.cw_complexes import CWComplexes
                sage: X = CWComplexes().example()
                sage: f = X.an_element()
                sage: f.dimension()
                2
            """
Example = Surface
