from sage.categories.graphs import Graphs as Graphs
from sage.structure.element_wrapper import ElementWrapper as ElementWrapper
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class Cycle(UniqueRepresentation, Parent):
    """
    An example of a graph: the cycle of length `n`.

    This class illustrates a minimal implementation of a graph.

    EXAMPLES::

        sage: from sage.categories.graphs import Graphs
        sage: C = Graphs().example(); C
        An example of a graph: the 5-cycle

        sage: C.category()
        Category of graphs

    We conclude by running systematic tests on this graph::

        sage: TestSuite(C).run()
    """
    def __init__(self, n: int = 5) -> None:
        """
        EXAMPLES::

            sage: from sage.categories.graphs import Graphs
            sage: C = Graphs().example(6); C
            An example of a graph: the 6-cycle

        TESTS::

            sage: TestSuite(C).run()
        """
    def an_element(self):
        """
        Return an element of the graph, as per
        :meth:`Sets.ParentMethods.an_element`.

        EXAMPLES::

            sage: from sage.categories.graphs import Graphs
            sage: C = Graphs().example()
            sage: C.an_element()
            0
        """
    def vertices(self):
        """
        Return the vertices of ``self``.

        EXAMPLES::

            sage: from sage.categories.graphs import Graphs
            sage: C = Graphs().example()
            sage: C.vertices()
            [0, 1, 2, 3, 4]
        """
    def edges(self):
        """
        Return the edges of ``self``.

        EXAMPLES::

            sage: from sage.categories.graphs import Graphs
            sage: C = Graphs().example()
            sage: C.edges()
            [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]
        """
    class Element(ElementWrapper):
        def dimension(self):
            """
            Return the dimension of ``self``.

            EXAMPLES::

                sage: from sage.categories.graphs import Graphs
                sage: C = Graphs().example()
                sage: e = C.edges()[0]
                sage: e.dimension()
                2
                sage: v = C.vertices()[0]
                sage: v.dimension()
                1
            """
Example = Cycle
