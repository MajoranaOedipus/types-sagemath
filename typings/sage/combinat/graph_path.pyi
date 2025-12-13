from _typeshed import Incomplete
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.structure.parent import Parent as Parent

def GraphPaths(g, source=None, target=None):
    """
    Return the combinatorial class of paths in the directed acyclic graph g.

    EXAMPLES::

        sage: G = DiGraph({1:[2,2,3], 2:[3,4], 3:[4], 4:[5,5]}, multiedges=True)

    If source and target are not given, then the returned class
    contains all paths (including trivial paths containing only one
    vertex).

    ::

        sage: p = GraphPaths(G); p
        Paths in Multi-digraph on 5 vertices
        sage: p.cardinality()
        37
        sage: path = p.random_element()
        sage: all(G.has_edge(*path[i:i+2]) for i in range(len(path) -1))
        True

    If the source is specified, then the returned class contains all of
    the paths starting at the vertex source (including the trivial
    path).

    ::

        sage: p = GraphPaths(G, source=3); p
        Paths in Multi-digraph on 5 vertices starting at 3
        sage: p.list()
        [[3], [3, 4], [3, 4, 5], [3, 4, 5]]

    If the target is specified, then the returned class contains all of
    the paths ending at the vertex target (including the trivial
    path).

    ::

        sage: p = GraphPaths(G, target=3); p
        Paths in Multi-digraph on 5 vertices ending at 3
        sage: p.cardinality()
        5
        sage: p.list()
        [[3], [1, 3], [2, 3], [1, 2, 3], [1, 2, 3]]

    If both the target and source are specified, then the returned
    class contains all of the paths from source to target.

    ::

        sage: p = GraphPaths(G, source=1, target=3); p
        Paths in Multi-digraph on 5 vertices starting at 1 and ending at 3
        sage: p.cardinality()
        3
        sage: p.list()
        [[1, 2, 3], [1, 2, 3], [1, 3]]

    Note that G must be a directed acyclic graph.

    ::

        sage: G = DiGraph({1:[2,2,3,5], 2:[3,4], 3:[4], 4:[2,5,7], 5:[6]}, multiedges=True)
        sage: GraphPaths(G)
        Traceback (most recent call last):
        ...
        TypeError: g must be a directed acyclic graph
    """

class GraphPaths_common:
    def __eq__(self, other):
        """
        Test for equality.

        EXAMPLES::

            sage: G1 = DiGraph({1:[2,3], 2:[3]})
            sage: p1 = GraphPaths(G1)
            sage: G2 = DiGraph({2:[3], 3:[4]})
            sage: p2 = GraphPaths(G2)
            sage: p1 == p1
            True
            sage: p1 == p2
            False
        """
    def __ne__(self, other):
        """
        Test for unequality.

        EXAMPLES::

            sage: G1 = DiGraph({1:[2,3], 2:[3]})
            sage: p1 = GraphPaths(G1)
            sage: G2 = DiGraph({2:[3], 3:[4]})
            sage: p2 = GraphPaths(G2)
            sage: p1 != p2
            True
            sage: p1 != p1
            False
        """
    def outgoing_edges(self, v):
        """
        Return a list of v's outgoing edges.

        EXAMPLES::

            sage: G = DiGraph({1:[2,2,3], 2:[3,4], 3:[4], 4:[5,5]}, multiedges=True)
            sage: p = GraphPaths(G)
            sage: p.outgoing_edges(2)
            [(2, 3, None), (2, 4, None)]
        """
    def incoming_edges(self, v):
        """
        Return a list of v's incoming edges.

        EXAMPLES::

            sage: G = DiGraph({1:[2,2,3], 2:[3,4], 3:[4], 4:[5,5]}, multiedges=True)
            sage: p = GraphPaths(G)
            sage: p.incoming_edges(2)
            [(1, 2, None), (1, 2, None)]
        """
    def outgoing_paths(self, v):
        """
        Return a list of the paths that start at v.

        EXAMPLES::

            sage: G = DiGraph({1:[2,2,3], 2:[3,4], 3:[4], 4:[5,5]}, multiedges=True)
            sage: gp = GraphPaths(G)
            sage: gp.outgoing_paths(3)
            [[3], [3, 4], [3, 4, 5], [3, 4, 5]]
            sage: gp.outgoing_paths(2)
            [[2],
             [2, 3],
             [2, 3, 4],
             [2, 3, 4, 5],
             [2, 3, 4, 5],
             [2, 4],
             [2, 4, 5],
             [2, 4, 5]]
        """
    def incoming_paths(self, v):
        """
        Return a list of paths that end at v.

        EXAMPLES::

            sage: G = DiGraph({1:[2,2,3], 2:[3,4], 3:[4], 4:[5,5]}, multiedges=True)
            sage: gp = GraphPaths(G)
            sage: gp.incoming_paths(2)
            [[2], [1, 2], [1, 2]]
        """
    def paths_from_source_to_target(self, source, target):
        """
        Return a list of paths from source to target.

        EXAMPLES::

            sage: G = DiGraph({1:[2,2,3], 2:[3,4], 3:[4], 4:[5,5]}, multiedges=True)
            sage: gp = GraphPaths(G)
            sage: gp.paths_from_source_to_target(2,4)
            [[2, 3, 4], [2, 4]]
        """
    def paths(self):
        """
        Return a list of all the paths of ``self``.

        EXAMPLES::

            sage: G = DiGraph({1:[2,2,3], 2:[3,4], 3:[4], 4:[5,5]}, multiedges=True)
            sage: gp = GraphPaths(G)
            sage: len(gp.paths())
            37
        """

class GraphPaths_all(Parent, GraphPaths_common):
    """
    EXAMPLES::

        sage: G = DiGraph({1:[2,2,3], 2:[3,4], 3:[4], 4:[5,5]}, multiedges=True)
        sage: p = GraphPaths(G)
        sage: p.cardinality()
        37
    """
    graph: Incomplete
    def __init__(self, g) -> None:
        """
        TESTS::

            sage: G = DiGraph({1:[2,2,3], 2:[3,4], 3:[4], 4:[5,5]}, multiedges=True)
            sage: p = GraphPaths(G)
            sage: p == loads(dumps(p))
            True
        """
    def list(self):
        """
        Return a list of the paths of ``self``.

        EXAMPLES::

            sage: G = DiGraph({1:[2,2,3], 2:[3,4], 3:[4], 4:[5,5]}, multiedges=True)
            sage: len(GraphPaths(G).list())
            37
        """

class GraphPaths_t(Parent, GraphPaths_common):
    graph: Incomplete
    target: Incomplete
    def __init__(self, g, target) -> None:
        """
        TESTS::

            sage: G = DiGraph({1:[2,2,3], 2:[3,4], 3:[4], 4:[5,5]}, multiedges=True)
            sage: p = GraphPaths(G, target=4)
            sage: p == loads(dumps(p))
            True
        """
    def list(self):
        """
        EXAMPLES::

            sage: G = DiGraph({1:[2,2,3], 2:[3,4], 3:[4], 4:[5,5]}, multiedges=True)
            sage: p = GraphPaths(G, target=4)
            sage: p.list()
            [[4],
             [2, 4],
             [1, 2, 4],
             [1, 2, 4],
             [3, 4],
             [1, 3, 4],
             [2, 3, 4],
             [1, 2, 3, 4],
             [1, 2, 3, 4]]
        """

class GraphPaths_s(Parent, GraphPaths_common):
    graph: Incomplete
    source: Incomplete
    def __init__(self, g, source) -> None:
        """
        TESTS::

            sage: G = DiGraph({1:[2,2,3], 2:[3,4], 3:[4], 4:[5,5]}, multiedges=True)
            sage: p = GraphPaths(G, 4)
            sage: p == loads(dumps(p))
            True
        """
    def list(self):
        """
        EXAMPLES::

            sage: G = DiGraph({1:[2,2,3], 2:[3,4], 3:[4], 4:[5,5]}, multiedges=True)
            sage: p = GraphPaths(G, 4)
            sage: p.list()
            [[4], [4, 5], [4, 5]]
        """

class GraphPaths_st(Parent, GraphPaths_common):
    """
    EXAMPLES::

        sage: G = DiGraph({1:[2,2,3], 2:[3,4], 3:[4], 4:[5,5]}, multiedges=True)
        sage: GraphPaths(G,1,2).cardinality()
        2
        sage: GraphPaths(G,1,3).cardinality()
        3
        sage: GraphPaths(G,1,4).cardinality()
        5
        sage: GraphPaths(G,1,5).cardinality()
        10
        sage: GraphPaths(G,2,3).cardinality()
        1
        sage: GraphPaths(G,2,4).cardinality()
        2
        sage: GraphPaths(G,2,5).cardinality()
        4
        sage: GraphPaths(G,3,4).cardinality()
        1
        sage: GraphPaths(G,3,5).cardinality()
        2
        sage: GraphPaths(G,4,5).cardinality()
        2
    """
    graph: Incomplete
    source: Incomplete
    target: Incomplete
    def __init__(self, g, source, target) -> None:
        """
        TESTS::

            sage: G = DiGraph({1:[2,2,3], 2:[3,4], 3:[4], 4:[5,5]}, multiedges=True)
            sage: p = GraphPaths(G,1,2)
            sage: p == loads(dumps(p))
            True
        """
    def list(self):
        """
        EXAMPLES::

            sage: G = DiGraph({1:[2,2,3], 2:[3,4], 3:[4], 4:[5,5]}, multiedges=True)
            sage: p = GraphPaths(G,1,2)
            sage: p.list()
            [[1, 2], [1, 2]]
        """
