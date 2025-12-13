from _typeshed import Incomplete
from sage.graphs.graph import Graph as Graph
from sage.misc.rest_index_of_methods import doc_index as doc_index, gen_thematic_rest_table_index as gen_thematic_rest_table_index

class MatchingCoveredGraph(Graph):
    """
    Matching covered graph

    INPUT:

    - ``data`` -- can be any of the following:

      - Empty or ``None`` (throws a :exc:`ValueError` as the graph must be
        nontrival).

      - An arbitrary graph.

    - ``matching`` -- (default: ``None``); a perfect matching of the
      graph, that can be given using any valid input format of
      :class:`~sage.graphs.graph.Graph`.

      If set to ``None``, a matching is computed using the other parameters.

    - ``algorithm`` -- string (default: ``'Edmonds'``); the algorithm to be
      used to compute a maximum matching of the graph among

      - ``'Edmonds'`` selects Edmonds' algorithm as implemented in NetworkX,

      - ``'LP'`` uses a Linear Program formulation of the matching problem.

    - ``solver`` -- string (default: ``None``); specify a Mixed Integer
      Linear Programming (MILP) solver to be used. If set to ``None``, the
      default one is used. For more information on MILP solvers and which
      default solver is used, see the method :meth:`solve
      <sage.numerical.mip.MixedIntegerLinearProgram.solve>` of the class
      :class:`MixedIntegerLinearProgram
      <sage.numerical.mip.MixedIntegerLinearProgram>`.

    - ``verbose`` -- integer (default: ``0``); sets the level of verbosity:
      set to 0 by default, which means quiet (only useful when ``algorithm
      == 'LP'``).

    - ``integrality_tolerance`` -- float; parameter for use with MILP
      solvers over an inexact base ring; see
      :meth:`MixedIntegerLinearProgram.get_values`.

    OUTPUT:

    - An object of the class :class:`~MatchingCoveredGraph` if the input is
      valid and the graph is matching covered, or otherwise an error is thrown.

    .. NOTE::

        All remaining arguments are passed to the ``Graph`` constructor

    EXAMPLES:

    Generating an object of the class ``MatchingCoveredGraph`` from the
    provided instance of ``Graph`` without providing any other information::

        sage: G = MatchingCoveredGraph(graphs.PetersenGraph())
        sage: G
        Matching covered petersen graph: graph on 10 vertices
        sage: sorted(G.get_matching())
        [(0, 5, None), (1, 6, None), (2, 7, None), (3, 8, None), (4, 9, None)]

        sage: G = graphs.StaircaseGraph(4)
        sage: H = MatchingCoveredGraph(G)
        sage: H
        Matching covered staircase graph: graph on 8 vertices
        sage: H == G
        True
        sage: sorted(H.get_matching())
        [(0, 1, None), (2, 7, None), (3, 6, None), (4, 5, None)]

        sage: G = Graph({0: [1, 2, 3, 4], 1: [2, 5],
        ....:            2: [5], 3: [4, 5], 4: [5]})
        sage: H = MatchingCoveredGraph(G)
        sage: H
        Matching covered graph on 6 vertices
        sage: H == G
        True
        sage: sorted(H.get_matching())
        [(0, 4, None), (1, 2, None), (3, 5, None)]

        sage: # needs networkx
        sage: import networkx
        sage: G = Graph(networkx.complete_bipartite_graph(12, 12))
        sage: H = MatchingCoveredGraph(G)
        sage: H
        Matching covered graph on 24 vertices
        sage: H == G
        True
        sage: sorted(H.get_matching())
        [(0, 15, None), (1, 14, None), (2, 13, None), (3, 12, None),
         (4, 23, None), (5, 22, None), (6, 21, None), (7, 20, None),
         (8, 19, None), (9, 18, None), (10, 17, None), (11, 16, None)]

        sage: G = Graph('E|fG', sparse=True)
        sage: H = MatchingCoveredGraph(G)
        sage: H
        Matching covered graph on 6 vertices
        sage: H == G
        True
        sage: sorted(H.get_matching())
        [(0, 5, None), (1, 2, None), (3, 4, None)]

        sage: # needs sage.modules
        sage: M = Matrix([(0,1,0,0,1,1,0,0,0,0),
        ....:             (1,0,1,0,0,0,1,0,0,0),
        ....:             (0,1,0,1,0,0,0,1,0,0),
        ....:             (0,0,1,0,1,0,0,0,1,0),
        ....:             (1,0,0,1,0,0,0,0,0,1),
        ....:             (1,0,0,0,0,0,0,1,1,0),
        ....:             (0,1,0,0,0,0,0,0,1,1),
        ....:             (0,0,1,0,0,1,0,0,0,1),
        ....:             (0,0,0,1,0,1,1,0,0,0),
        ....:             (0,0,0,0,1,0,1,1,0,0)])
        sage: M
        [0 1 0 0 1 1 0 0 0 0]
        [1 0 1 0 0 0 1 0 0 0]
        [0 1 0 1 0 0 0 1 0 0]
        [0 0 1 0 1 0 0 0 1 0]
        [1 0 0 1 0 0 0 0 0 1]
        [1 0 0 0 0 0 0 1 1 0]
        [0 1 0 0 0 0 0 0 1 1]
        [0 0 1 0 0 1 0 0 0 1]
        [0 0 0 1 0 1 1 0 0 0]
        [0 0 0 0 1 0 1 1 0 0]
        sage: G = Graph(M)
        sage: H = MatchingCoveredGraph(G)
        sage: H == G
        True
        sage: sorted(H.get_matching())
        [(0, 5, None), (1, 6, None), (2, 7, None), (3, 8, None), (4, 9, None)]

        sage: # needs sage.modules
        sage: M = Matrix([(-1, 0, 0, 0, 1, 0, 0, 0, 0, 0,-1, 0, 0, 0, 0),
        ....:             ( 1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1, 0, 0, 0),
        ....:             ( 0, 1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1, 0, 0),
        ....:             ( 0, 0, 1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1, 0),
        ....:             ( 0, 0, 0, 1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1),
        ....:             ( 0, 0, 0, 0, 0,-1, 0, 0, 0, 1, 1, 0, 0, 0, 0),
        ....:             ( 0, 0, 0, 0, 0, 0, 0, 1,-1, 0, 0, 1, 0, 0, 0),
        ....:             ( 0, 0, 0, 0, 0, 1,-1, 0, 0, 0, 0, 0, 1, 0, 0),
        ....:             ( 0, 0, 0, 0, 0, 0, 0, 0, 1,-1, 0, 0, 0, 1, 0),
        ....:             ( 0, 0, 0, 0, 0, 0, 1,-1, 0, 0, 0, 0, 0, 0, 1)])
        sage: M
        [-1  0  0  0  1  0  0  0  0  0 -1  0  0  0  0]
        [ 1 -1  0  0  0  0  0  0  0  0  0 -1  0  0  0]
        [ 0  1 -1  0  0  0  0  0  0  0  0  0 -1  0  0]
        [ 0  0  1 -1  0  0  0  0  0  0  0  0  0 -1  0]
        [ 0  0  0  1 -1  0  0  0  0  0  0  0  0  0 -1]
        [ 0  0  0  0  0 -1  0  0  0  1  1  0  0  0  0]
        [ 0  0  0  0  0  0  0  1 -1  0  0  1  0  0  0]
        [ 0  0  0  0  0  1 -1  0  0  0  0  0  1  0  0]
        [ 0  0  0  0  0  0  0  0  1 -1  0  0  0  1  0]
        [ 0  0  0  0  0  0  1 -1  0  0  0  0  0  0  1]
        sage: G = Graph(M)
        sage: H = MatchingCoveredGraph(G)
        sage: H == G
        True
        sage: sorted(H.get_matching())
        [(0, 5, None), (1, 6, None), (2, 7, None), (3, 8, None), (4, 9, None)]

        sage: G = Graph([(0, 1), (0, 3), (0, 4), (1, 2), (1, 5), (2, 3),
        ....:            (2, 6), (3, 7), (4, 5), (4, 7), (5, 6), (6, 7)])
        sage: H = MatchingCoveredGraph(G)
        sage: H == G
        True
        sage: sorted(H.get_matching())
        [(0, 4, None), (1, 5, None), (2, 6, None), (3, 7, None)]

        sage: # optional - python_igraph
        sage: import igraph
        sage: G = Graph(igraph.Graph([(0, 1), (0, 3), (1, 2), (2, 3)]))
        sage: H = MatchingCoveredGraph(G)
        sage: H
        Matching covered graph on 4 vertices
        sage: sorted(H.get_matching())
        [(0, 3, {}), (1, 2, {})]

    One may specify a perfect matching::

        sage: P = graphs.PetersenGraph()
        sage: M = P.matching()
        sage: sorted(M)
        [(0, 5, None), (1, 6, None), (2, 7, None), (3, 8, None), (4, 9, None)]
        sage: G = MatchingCoveredGraph(P, matching=M)
        sage: G
        Matching covered petersen graph: graph on 10 vertices
        sage: P == G
        True
        sage: sorted(G.get_matching())
        [(0, 5, None), (1, 6, None), (2, 7, None), (3, 8, None), (4, 9, None)]
        sage: sorted(G.get_matching()) == sorted(M)
        True

        sage: G = graphs.TruncatedBiwheelGraph(14)
        sage: M = G.matching()
        sage: sorted(M)
        [(0, 27, None), (1, 26, None), (2, 3, None), (4, 5, None),
         (6, 7, None), (8, 9, None), (10, 11, None), (12, 13, None),
         (14, 15, None), (16, 17, None), (18, 19, None), (20, 21, None),
         (22, 23, None), (24, 25, None)]
        sage: H = MatchingCoveredGraph(G, M)
        sage: H
        Matching covered truncated biwheel graph: graph on 28 vertices
        sage: H == G
        True
        sage: sorted(H.get_matching()) == sorted(M)
        True

    One may specify some keyword arguments::

        sage: G = Graph([(0, 1, 5)], {'weighted': True})
        sage: kwds = {
        ....:   'loops': False,
        ....:   'multiedges': True,
        ....:   'pos': {0: (0, 0), 1: (1, 1)}
        ....: }
        sage: H = MatchingCoveredGraph(G, **kwds)
        sage: H
        Matching covered multi-graph on 2 vertices
        sage: H.add_edge(0, 1)
        sage: H.edges()
        [(0, 1, None), (0, 1, 5)]

    TESTS:

    An empty graph is not matching covered::

        sage: G = Graph()
        sage: H = MatchingCoveredGraph(G)
        Traceback (most recent call last):
        ...
        ValueError: the graph is trivial
        sage: G = MatchingCoveredGraph()
        Traceback (most recent call last):
        ...
        ValueError: the graph is trivial

    Providing with a graph that is not connected::

        sage: G = graphs.CycleGraph(4)
        sage: G += graphs.CycleGraph(6)
        sage: G.connected_components_number()
        2
        sage: H = MatchingCoveredGraph(G)
        Traceback (most recent call last):
        ...
        ValueError: the graph is not connected

    Make sure that self-loops are not allowed for a matching covered graph::

        sage: P = graphs.PetersenGraph()
        sage: kwds = {'loops': True}
        sage: G = MatchingCoveredGraph(P, **kwds)
        Traceback (most recent call last):
        ...
        ValueError: loops are not allowed in matching covered graphs
        sage: G = MatchingCoveredGraph(P)
        sage: G.allows_loops()
        False
        sage: G.allow_loops(True)
        Traceback (most recent call last):
        ...
        ValueError: loops are not allowed in matching covered graphs
        sage: G.add_edge(0, 0)
        Traceback (most recent call last):
        ...
        ValueError: loops are not allowed in matching covered graphs
        sage: H = MatchingCoveredGraph(P, loops=True)
        Traceback (most recent call last):
        ...
        ValueError: loops are not allowed in matching covered graphs

    Make sure that multiple edges are allowed for a matching covered graph (by
    default it is off and can be modified to be allowed)::

        sage: P = graphs.PetersenGraph()
        sage: G = MatchingCoveredGraph(P)
        sage: G
        Matching covered petersen graph: graph on 10 vertices
        sage: G.allows_multiple_edges()
        False
        sage: G.size()
        15
        sage: G.allow_multiple_edges(True)
        sage: G.allows_multiple_edges()
        True
        sage: G.add_edge(next(P.edge_iterator()))
        sage: G.size()
        16
        sage: G
        Matching covered petersen graph: multi-graph on 10 vertices
        sage: H = MatchingCoveredGraph(P, multiedges=True)
        sage: H.allows_multiple_edges()
        True
        sage: H.add_edge(next(P.edge_iterator()))
        sage: H.size()
        16
        sage: H
        Matching covered petersen graph: multi-graph on 10 vertices

    Providing with a connected nontrivial graph free of self-loops that is
    not matching covered::

        sage: G = graphs.CompleteGraph(11)
        sage: H = MatchingCoveredGraph(G)
        Traceback (most recent call last):
        ...
        ValueError: input graph is not matching covered
        sage: G = Graph({0: [1, 6, 11], 1: [2, 4], 2: [3, 5], 3: [4, 5],
        ....:            4: [5], 6: [7, 9], 7: [8, 10], 8: [9, 10], 9: [10],
        ....:            11: [12, 14], 12: [13, 15], 13: [14, 15], 14: [15]})
        sage: H = MatchingCoveredGraph(G)
        Traceback (most recent call last):
        ...
        ValueError: input graph is not matching covered

        sage: # needs networkx
        sage: import networkx
        sage: G = Graph(networkx.complete_bipartite_graph(2, 12))
        sage: H = MatchingCoveredGraph(G)
        Traceback (most recent call last):
        ...
        ValueError: input graph is not matching covered
        sage: G = Graph('F~~~w')
        sage: H = MatchingCoveredGraph(G)
        Traceback (most recent call last):
        ...
        ValueError: input graph is not matching covered

        sage: # needs sage.modules
        sage: M = Matrix([(0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0),
        ....:             (1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        ....:             (0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        ....:             (0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        ....:             (0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        ....:             (0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        ....:             (1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0),
        ....:             (0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0),
        ....:             (0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0),
        ....:             (0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0),
        ....:             (0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0),
        ....:             (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0),
        ....:             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1),
        ....:             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1),
        ....:             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1),
        ....:             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0)])
        sage: M
        [0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0]
        [1 0 1 0 1 0 0 0 0 0 0 0 0 0 0 0]
        [0 1 0 1 0 1 0 0 0 0 0 0 0 0 0 0]
        [0 0 1 0 1 1 0 0 0 0 0 0 0 0 0 0]
        [0 1 0 1 0 1 0 0 0 0 0 0 0 0 0 0]
        [0 0 1 1 1 0 0 0 0 0 0 0 0 0 0 0]
        [1 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0]
        [0 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0]
        [0 0 0 0 0 0 0 1 0 1 1 0 0 0 0 0]
        [0 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0]
        [0 0 0 0 0 0 0 1 1 1 0 0 0 0 0 0]
        [1 0 0 0 0 0 0 0 0 0 0 0 1 0 1 0]
        [0 0 0 0 0 0 0 0 0 0 0 1 0 1 0 1]
        [0 0 0 0 0 0 0 0 0 0 0 0 1 0 1 1]
        [0 0 0 0 0 0 0 0 0 0 0 1 0 1 0 1]
        [0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 0]
        sage: G = Graph(M)
        sage: H = MatchingCoveredGraph(G)
        Traceback (most recent call last):
        ...
        ValueError: input graph is not matching covered

        sage: # needs sage.modules
        sage: M = Matrix([(1, 1, 0, 0, 0, 0),
        ....:             (0, 0, 1, 1, 0, 0),
        ....:             (0, 0, 1, 0, 1, 0),
        ....:             (1, 0, 0, 0, 0, 1),
        ....:             (0, 1, 0, 1, 1, 1)])
        sage: G = Graph(M)
        sage: H = MatchingCoveredGraph(G)
        Traceback (most recent call last):
        ...
        ValueError: input graph is not matching covered
        sage: G = Graph([(11, 12), (11, 14), (0, 1), (0, 11), (0, 6), (1, 2),
        ....:            (1, 4), (2, 3), (2, 5), (3, 4), (3, 5), (4, 5),
        ....:            (6, 7), (6, 9), (7, 8), (7, 10), (8, 9), (8, 10),
        ....:            (9, 10), (12, 13), (12, 15), (13, 14), (13, 15),
        ....:            (14, 15)])
        sage: H = MatchingCoveredGraph(G)
        Traceback (most recent call last):
        ...
        ValueError: input graph is not matching covered

        sage: # optional - python_igraph
        sage: import igraph
        sage: G = Graph(igraph.Graph([(0, 1), (0, 2), (0, 3), (1, 2), (2, 3)]))
        sage: H = MatchingCoveredGraph(G)
        Traceback (most recent call last):
        ...
        ValueError: input graph is not matching covered

    Providing with a wrong matching::

        sage: P = graphs.PetersenGraph()
        sage: M = str('0')
        sage: H = MatchingCoveredGraph(P, matching=M)
        Traceback (most recent call last):
        ...
        RuntimeError: the string seems corrupt: valid characters are
        ?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~
        sage: N = str('graph')
        sage: J = MatchingCoveredGraph(P, matching=N)
        Traceback (most recent call last):
        ...
        RuntimeError: the string (graph) seems corrupt: for n = 40,
        the string is too short

        sage: G = graphs.CompleteGraph(6)
        sage: M = Graph(G.matching())
        sage: M.add_edges([(0, 1), (0, 2)])
        sage: H = MatchingCoveredGraph(G, matching=M)
        Traceback (most recent call last):
        ...
        ValueError: the input is not a matching
        sage: N = Graph(G.matching())
        sage: N.add_edge(6, 7)
        sage: H = MatchingCoveredGraph(G, matching=N)
        Traceback (most recent call last):
        ...
        ValueError: the input is not a matching of the graph
        sage: J = Graph()
        sage: J.add_edges([(0, 1), (2, 3)])
        sage: H = MatchingCoveredGraph(G, matching=J)
        Traceback (most recent call last):
        ...
        ValueError: the input is not a perfect matching of the graph

    Note that data shall be one of empty or ``None`` or an instance of
    ``Graph`` or an instance of ``MatchingCoveredGraph``. Otherwise a
    :exc:`ValueError` is returned::

        sage: D = digraphs.Complete(10)
        sage: D
        Complete digraph: Digraph on 10 vertices
        sage: G = MatchingCoveredGraph(D)
        Traceback (most recent call last):
        ...
        TypeError: input data is of unknown type
    """
    def __init__(self, data=None, matching=None, algorithm: str = 'Edmonds', solver=None, verbose: int = 0, integrality_tolerance: float = 0.001, *args, **kwds) -> None:
        """
        Create a matching covered graph, that is a connected nontrivial graph
        wherein each edge participates in some perfect matching.

        See documentation ``MatchingCoveredGraph?`` for detailed information.
        """
    def add_edge(self, u, v=None, label=None) -> None:
        """
        Add an edge from vertex ``u`` to vertex ``v``.

        .. NOTE::

            This method overwrites the
            :meth:`~sage.graphs.generic_graph.GenericGraph.add_edge` method
            to ensure that resultant graph is also matching covered.

        INPUT:

        The following forms are all accepted:

        - G.add_edge(1, 2)
        - G.add_edge((1, 2))
        - G.add_edges([(1, 2)])
        - G.add_edge(1, 2, 'label')
        - G.add_edge((1, 2, 'label'))
        - G.add_edges([(1, 2, 'label')])

        OUTPUT:

        - If an edge is provided with a valid format, but addition of the edge
          leaves the resulting graph not being matching covered, a
          :exc:`ValueError` is returned without any alteration to the existing
          matching covered graph. If the addition of the edge preserves the
          property of matching covered, then the graph is updated and nothing
          is returned.

        - If the edge is provided in an invalid format, a :exc:`ValueError`
          is returned.

        WARNING:

        The following intuitive input results in nonintuitive output,
        even though the resulting graph behind the intuition might be matching
        covered::

            sage: P = graphs.WheelGraph(6)
            sage: G = MatchingCoveredGraph(P)
            sage: G.add_edge((1, 4), 'label')
            Traceback (most recent call last):
            ...
            ValueError: the graph obtained after the addition of edge
            (((1, 4), 'label', None)) is not matching covered
            sage: G.edges(sort=False)
            [(0, 1, None), (0, 2, None), (0, 3, None), (0, 4, None),
             (0, 5, None), (1, 2, None), (1, 5, None), (2, 3, None),
             (3, 4, None), (4, 5, None)]

        The key word ``label`` must be used::

            sage: W = graphs.WheelGraph(6)
            sage: G = MatchingCoveredGraph(W)
            sage: G.add_edge((1, 4), label='label')
            sage: G.edges(sort=False)  # No alteration to the existing graph
            [(0, 1, None), (0, 2, None), (0, 3, None), (0, 4, None),
             (0, 5, None), (1, 2, None), (1, 4, 'label'), (1, 5, None),
             (2, 3, None), (3, 4, None), (4, 5, None)]

        An expression, analogous to the syntax mentioned above may be used::

            sage: S = graphs.StaircaseGraph(4)
            sage: G = MatchingCoveredGraph(S)
            sage: G.add_edge(0, 5)
            sage: G.edges(sort=False)
            [(0, 1, None), (0, 3, None), (0, 5, None), (0, 6, None),
             (1, 2, None), (1, 4, None), (2, 5, None), (2, 7, None),
             (3, 4, None), (3, 6, None), (4, 5, None), (5, 7, None),
             (6, 7, None)]
            sage: G.add_edge((2, 3))
            sage: G.edges(sort=False)
            [(0, 1, None), (0, 3, None), (0, 5, None), (0, 6, None),
             (1, 2, None), (1, 4, None), (2, 3, None), (2, 5, None),
             (2, 7, None), (3, 4, None), (3, 6, None), (4, 5, None),
             (5, 7, None), (6, 7, None)]
            sage: G.add_edges([(0, 4)])
            sage: G.edges(sort=False)
            [(0, 1, None), (0, 3, None), (0, 4, None), (0, 5, None),
             (0, 6, None), (1, 2, None), (1, 4, None), (2, 3, None),
             (2, 5, None), (2, 7, None), (3, 4, None), (3, 6, None),
             (4, 5, None), (5, 7, None), (6, 7, None)]
            sage: G.add_edge(2, 4, 'label')
            sage: G.edges(sort=False)
            [(0, 1, None), (0, 3, None), (0, 4, None), (0, 5, None),
             (0, 6, None), (1, 2, None), (1, 4, None), (2, 3, None),
             (2, 4, 'label'), (2, 5, None), (2, 7, None), (3, 4, None),
             (3, 6, None), (4, 5, None), (5, 7, None), (6, 7, None)]
            sage: G.add_edge((4, 6, 'label'))
            sage: G.edges(sort=False)
            [(0, 1, None), (0, 3, None), (0, 4, None), (0, 5, None),
             (0, 6, None), (1, 2, None), (1, 4, None), (2, 3, None),
             (2, 4, 'label'), (2, 5, None), (2, 7, None), (3, 4, None),
             (3, 6, None), (4, 5, None), (4, 6, 'label'), (5, 7, None),
             (6, 7, None)]
            sage: G.add_edges([(4, 7, 'label')])
            sage: G.edges(sort=False)
            [(0, 1, None), (0, 3, None), (0, 4, None), (0, 5, None),
             (0, 6, None), (1, 2, None), (1, 4, None), (2, 3, None),
             (2, 4, 'label'), (2, 5, None), (2, 7, None), (3, 4, None),
             (3, 6, None), (4, 5, None), (4, 6, 'label'), (4, 7, 'label'),
             (5, 7, None), (6, 7, None)]

        Note that the ``weight`` of the edge shall be input as the ``label``::

            sage: G.add_edge((1, 3), label=5)
            sage: G.edges()
            [(0, 1, None), (0, 3, None), (0, 4, None), (0, 5, None),
             (0, 6, None), (1, 2, None), (1, 3, 5), (1, 4, None),
             (2, 3, None), (2, 4, 'label'), (2, 5, None), (2, 7, None),
             (3, 4, None), (3, 6, None), (4, 5, None), (4, 6, 'label'),
             (4, 7, 'label'), (5, 7, None), (6, 7, None)]
            sage: G.add_edge((2, 4, 6), label=6)
            Traceback (most recent call last):
            ...
            ValueError: the graph obtained after the addition of edge
            (((2, 4, 6), None, 6)) is not matching covered

        Vertex name cannot be ``None``, so::

            sage: W = graphs.WheelGraph(6)
            sage: H = MatchingCoveredGraph(W)
            sage: H.add_edge(None, 1)
            Traceback (most recent call last):
            ...
            ValueError: the graph obtained after the addition of edge
            ((None, 1, None)) is not matching covered
            sage: H.edges(sort=False)  # No alteration to the existing graph
            [(0, 1, None), (0, 2, None), (0, 3, None), (0, 4, None),
             (0, 5, None), (1, 2, None), (1, 5, None), (2, 3, None),
             (3, 4, None), (4, 5, None)]
            sage: H.add_edge(None, None)
            Traceback (most recent call last):
            ...
            ValueError: the graph obtained after the addition of edge
            ((None, None, None)) is not matching covered
            sage: H.edges(sort=False)  # No alteration to the existing graph
            [(0, 1, None), (0, 2, None), (0, 3, None), (0, 4, None),
             (0, 5, None), (1, 2, None), (1, 5, None), (2, 3, None),
             (3, 4, None), (4, 5, None)]

        EXAMPLES:

        Adding an already existing edge::

            sage: P = graphs.PetersenGraph()
            sage: G = MatchingCoveredGraph(P)
            sage: G.add_edge(next(G.edge_iterator()))
            sage: P == G
            True
            sage: G.size()
            15
            sage: G.allow_multiple_edges(True)
            sage: G.add_edge(0, 1)
            sage: G.size()
            16

        Adding an edge such that the resulting graph is matching covered::

            sage: P = graphs.PetersenGraph()
            sage: G = MatchingCoveredGraph(P)
            sage: G.add_edge(1, 4)
            sage: G.edges(sort=False)
            [(0, 1, None), (0, 4, None), (0, 5, None), (1, 2, None),
             (1, 4, None), (1, 6, None), (2, 3, None), (2, 7, None),
             (3, 4, None), (3, 8, None), (4, 9, None), (5, 7, None),
             (5, 8, None), (6, 8, None), (6, 9, None), (7, 9, None)]

        Adding an edge with both the incident vertices being existent such
        that the resulting graph is not matching covered::

            sage: C = graphs.CycleGraph(4)
            sage: G = MatchingCoveredGraph(C)
            sage: G.add_edge(0, 2)
            Traceback (most recent call last):
            ...
            ValueError: the graph obtained after the addition of edge
            ((0, 2, None)) is not matching covered
            sage: G.edges(sort=False) # No alteration to the existing graph
            [(0, 1, None), (0, 3, None), (1, 2, None), (2, 3, None)]

        Adding an edge with exactly one incident vertex that is nonexistent
        throws a :exc:`ValueError` exception, as the resulting graph would
        have an odd order::

            sage: C = graphs.CycleGraph(4)
            sage: G = MatchingCoveredGraph(C)
            sage: G.add_edge(0, 4)
            Traceback (most recent call last):
            ...
            ValueError: the graph obtained after the addition of edge
            ((0, 4, None)) is not matching covered
            sage: G.edges(sort=False) # No alteration to the existing graph
            [(0, 1, None), (0, 3, None), (1, 2, None), (2, 3, None)]

        Adding an edge with both the incident vertices that is nonexistent
        throws a :exc:`ValueError` exception, as the resulting graph would
        have been disconnected::

            sage: C = graphs.CycleGraph(4)
            sage: G = MatchingCoveredGraph(C)
            sage: G.add_edge(4, 5)
            Traceback (most recent call last):
            ...
            ValueError: the graph obtained after the addition of edge
            ((4, 5, None)) is not matching covered
            sage: G.edges(sort=False) # No alteration to the existing graph
            [(0, 1, None), (0, 3, None), (1, 2, None), (2, 3, None)]

        Adding a self-loop::

            sage: H = graphs.HeawoodGraph()
            sage: G = MatchingCoveredGraph(H)
            sage: v = next(G.vertex_iterator())
            sage: G.add_edge(v, v)
            Traceback (most recent call last):
            ...
            ValueError: loops are not allowed in matching covered graphs
        """
    def add_edges(self, edges, loops: bool = False) -> None:
        """
        Add edges from an iterable container.

        .. NOTE::

            This method overwrites the
            :meth:`~sage.graphs.generic_graph.GenericGraph.add_edges` method
            to ensure that resultant graph is also matching covered.

        INPUT:

        - ``edges`` -- an iterable of edges, given either as ``(u, v)``
          or ``(u, v, 'label')``. If an edge is provided in the format
          ``(u, v)``, the label is set to ``None``.

        - ``loops`` -- boolean (default: ``False``); note that this shall
          always be set to either ``False`` or ``None`` (since matching covered
          graphs are free of loops), in which case all the loops
          ``(v, v, 'label')`` are removed from the iterator. If ``loops`` is
          set to ``True``, a :exc:`ValueError` is thrown.

        - Please note that all the loops present in the iterator are ignored,
          provided that ``loops`` is set to ``False`` or ``None``.

        OUTPUT:

        - If ``loops`` is set to ``True``, a :exc:`ValueError` is returned.

        - If ``edges`` is provided with a valid format, but addition of the
          edges leave the resulting graph not being matching covered, a
          :exc:`ValueError` is returned without any alteration to the existing
          matching covered graph. If the addition of the edges preserves the
          property of matching covered, then the graph is updated and nothing
          is returned.

        - If ``edges`` is provided in an invalid format, a :exc:`ValueError`
          is returned.

        EXAMPLES:

        Providing with an empty list of edges::

            sage: C = graphs.CycleGraph(6)
            sage: G = MatchingCoveredGraph(C)
            sage: G.add_edges([])
            sage: G == C
            True

        Adding some edges, the incident vertices of each of which are existent,
        such that the resulting graph is matching covered::

            sage: S = graphs.StaircaseGraph(4)
            sage: G = MatchingCoveredGraph(S)
            sage: F = [(0, 4), (2, 4), (4, 6), (4, 7)]
            sage: G.add_edges(F)
            sage: G.edges(sort=True, sort_vertices=True)
            [(0, 1, None), (0, 3, None), (0, 4, None), (0, 6, None),
             (1, 2, None), (1, 4, None), (2, 4, None), (2, 5, None),
             (2, 7, None), (3, 4, None), (3, 6, None), (4, 5, None),
             (4, 6, None), (4, 7, None), (5, 7, None), (6, 7, None)]

        Adding some edges, at least one of the incident vertices of some of
        which are nonexistent such that the resulting graph is matching
        covered::

            sage: C = graphs.CycleGraph(8)
            sage: G = MatchingCoveredGraph(C)
            sage: F = [(0, 9), (1, 8), (2, 9), (3, 8),
            ....:      (4, 9), (5, 8), (6, 9), (7, 8)]
            sage: G.add_edges(F)
            sage: G.edges(sort=True, sort_vertices=True)
            [(0, 1, None), (0, 7, None), (0, 9, None), (1, 2, None),
             (1, 8, None), (2, 3, None), (2, 9, None), (3, 4, None),
             (3, 8, None), (4, 5, None), (4, 9, None), (5, 6, None),
             (5, 8, None), (6, 7, None), (6, 9, None), (7, 8, None)]
            sage: G.is_isomorphic(graphs.BiwheelGraph(5))
            True

        Adding a removable double ear to a matching covered graph::

            sage: H = graphs.HexahedralGraph()
            sage: G = MatchingCoveredGraph(H)
            sage: F = {(0, 8, None), (1, 10), (4, 11, 'label'),
            ....:      (5, 9), (8, 9), (10, 11)}
            sage: G.add_edges(F)
            sage: G.edges(sort=True, sort_vertices=True)
            [(0, 1, None), (0, 3, None), (0, 4, None), (0, 8, None),
             (1, 2, None), (1, 5, None), (1, 10, None), (2, 3, None),
             (2, 6, None), (3, 7, None), (4, 5, None), (4, 7, None),
             (4, 11, 'label'), (5, 6, None), (5, 9, None), (6, 7, None),
             (8, 9, None), (10, 11, None)]

        Adding some edges, the incident vertices of each of which are existent,
        such that the resulting graph is NOT matching covered::

            sage: C = graphs.CycleGraph(6)
            sage: G = MatchingCoveredGraph(C)
            sage: F = [(0, 2), (3, 5)]
            sage: G.add_edges(F)
            Traceback (most recent call last):
            ...
            ValueError: the resulting graph after the addition ofthe edges is not matching covered

        Adding some edges, at least one of the incident vertices of some of
        which are nonexistent such that the resulting graph is NOT matching
        covered::

            sage: H = graphs.HexahedralGraph()
            sage: G = MatchingCoveredGraph(H)
            sage: F = [(3, 8), (6, 9), (8, 9)]
            sage: G.add_edges(F)
            Traceback (most recent call last):
            ...
            ValueError: the resulting graph after the addition ofthe edges is not matching covered
            sage: I = [(0, 8), (1, 9)]
            sage: G.add_edges(I)
            Traceback (most recent call last):
            ...
            ValueError: the resulting graph after the addition ofthe edges is not matching covered
            sage: J = [(u, 8) for u in range(8)]
            sage: G.add_edges(J)
            Traceback (most recent call last):
            ...
            ValueError: odd order is not allowed for matching covered graphs

        Setting the parameter ``loops`` to either ``False`` or ``None``::

            sage: W = graphs.WheelGraph(6)
            sage: G = MatchingCoveredGraph(W)
            sage: F = [(0, 0), (1, 3), (2, 4)]
            sage: G.add_edges(edges=F, loops=False)
            sage: G.edges(sort=True, sort_vertices=True)
            [(0, 1, None), (0, 2, None), (0, 3, None), (0, 4, None),
             (0, 5, None), (1, 2, None), (1, 3, None), (1, 5, None),
             (2, 3, None), (2, 4, None), (3, 4, None), (4, 5, None)]
            sage: J = [(1, 1), (3, 5)]
            sage: G.add_edges(edges=J, loops=True)
            Traceback (most recent call last):
            ...
            ValueError: loops are not allowed in matching covered graphs
            sage: G.edges(sort=True, sort_vertices=True)
            [(0, 1, None), (0, 2, None), (0, 3, None), (0, 4, None),
             (0, 5, None), (1, 2, None), (1, 3, None), (1, 5, None),
             (2, 3, None), (2, 4, None), (3, 4, None), (4, 5, None)]

        Setting the parameter ``loops`` to ``True``::

            sage: P = graphs.PetersenGraph()
            sage: G = MatchingCoveredGraph(P)
            sage: F = [(0, 0), (0, 2), (0, 3)]
            sage: G.add_edges(edges=F, loops=True)
            Traceback (most recent call last):
            ...
            ValueError: loops are not allowed in matching covered graphs

        Adding a multiple edge::

            sage: S = graphs.StaircaseGraph(4)
            sage: G = MatchingCoveredGraph(S)
            sage: G.allow_multiple_edges(True)
            sage: F = [(0, 1, 'label'), (0, 4), (1, 2)]
            sage: G.add_edges(F)
            sage: G.edges(sort=False)
            [(0, 1, None), (0, 1, 'label'), (0, 3, None), (0, 4, None),
             (0, 6, None), (1, 2, None), (1, 2, None), (1, 4, None),
             (2, 5, None), (2, 7, None), (3, 4, None), (3, 6, None),
             (4, 5, None), (5, 7, None), (6, 7, None)]
            sage: H = [(0, 1)] * 4
            sage: G.add_edges(H)
            sage: G.edge_label(0, 1)
            [None, None, None, None, None, 'label']

        TESTS:

        Providing with a non-iterable of edges::

            sage: K2 = graphs.CompleteGraph(2)
            sage: G = MatchingCoveredGraph(K2)
            sage: G.add_edges(1234)
            Traceback (most recent call last):
            ...
            ValueError: expected an iterable of edges,
            but got a non-iterable object

        Providing with an edge in ``edges`` that has 0 values to unpack::

            sage: W = graphs.WagnerGraph()
            sage: G = MatchingCoveredGraph(W)
            sage: G.add_edges([()])
            Traceback (most recent call last):
            ...
            ValueError: need more than 1 value to unpack for edge: ()

        Providing with an edge in ``edges`` that has precisely one value to unpack::

            sage: T = graphs.TruncatedBiwheelGraph(10)
            sage: G = MatchingCoveredGraph(T)
            sage: G.add_edges([(0, )])
            Traceback (most recent call last):
            ...
            ValueError: need more than 1 value to unpack for edge: (0,)

        Providing with an edge in ``edges`` that has more than 3 values to unpack::

            sage: B = graphs.BiwheelGraph(5)
            sage: G = MatchingCoveredGraph(B)
            sage: G.add_edges([(0, 1, 2, 3, 4)])
            Traceback (most recent call last):
            ...
            ValueError: too many values to unpack (expected 2) for edge: (0, 1, 2, 3, 4)

        Providing with an edge of unknown data type::

            sage: M = graphs.MurtyGraph()
            sage: G = MatchingCoveredGraph(M)
            sage: F = [None, 'edge', None]
            sage: G.add_edges(F)
            Traceback (most recent call last):
            ...
            TypeError: input edge None is of unknown type
        """
    def add_vertex(self, name=None) -> None:
        """
        Add a vertex to the (matching covered) graph.

        .. NOTE::

            This method overwrites the
            :meth:`~sage.graphs.generic_graph.GenericGraph.add_vertex` method
            to ensure that isolated vertices are forbidden in
            :class:`~MatchingCoveredGraph`.

        INPUT:

        - ``name`` -- an immutable object (default: ``None``); when no name is
          specified (default), then the new vertex will be represented by the
          least integer not already representing a vertex. ``name`` must be an
          immutable object (e.g., an integer, a tuple, etc.).

        OUTPUT:

        - If ``name`` specifies an existing vertex, then nothing is done.
          Otherwise a :exc:`ValueError` is returned with no change to the
          existing (matching covered) graph is returned since matching covered
          graphs are free of isolated vertices.

        EXAMPLES:

        Adding an existing vertex::

            sage: P = graphs.PetersenGraph()
            sage: P
            Petersen graph: Graph on 10 vertices
            sage: G = MatchingCoveredGraph(P)
            sage: G
            Matching covered petersen graph: graph on 10 vertices
            sage: u = next(G.vertex_iterator())
            sage: G.add_vertex(u)
            sage: G
            Matching covered petersen graph: graph on 10 vertices

        Adding a new/ non-existing vertex::

            sage: G.add_vertex()
            Traceback (most recent call last):
            ...
            ValueError: isolated vertices are not allowed in matching covered graphs
            sage: u = 100
            sage: G.add_vertex(u)
            Traceback (most recent call last):
            ...
            ValueError: isolated vertices are not allowed in matching covered graphs
        """
    def add_vertices(self, vertices) -> None:
        """
        Add vertices to the (matching covered) graph from an iterable container
        of vertices.

        .. NOTE::

            This method overwrites the
            :meth:`~sage.graphs.generic_graph.GenericGraph.add_vertices` method
            to ensure that isolated vertices are forbidden in
            :class:`~MatchingCoveredGraph`.

        INPUT:

        - ``vertices`` -- iterator container of vertex labels. A new label is
          created, used and returned in the output list for all ``None`` values
          in ``vertices``.

        OUTPUT:

        - If all of the vertices are existing vertices of the (matching
          covered) graph, then nothing is done; otherwise a :exc:`ValueError`
          is returned with no change to the existing (matching covered) graph
          since matching covered graphs are free of isolated vertices.

        EXAMPLES:

        Adding a list of already existing vertices::

            sage: T = graphs.TruncatedBiwheelGraph(15)
            sage: T
            Truncated biwheel graph: Graph on 30 vertices
            sage: G = MatchingCoveredGraph(T)
            sage: G
            Matching covered truncated biwheel graph: graph on 30 vertices
            sage: S = [0, 1, 2, 3]  # We choose 4 existing vertices
            sage: G.add_vertices(S)
            sage: G
            Matching covered truncated biwheel graph: graph on 30 vertices

        Adding a list of vertices in which at least one is non-existent or
        ``None`` or possibly both::

            sage: T = graphs.CompleteGraph(2)
            sage: T
            Complete graph: Graph on 2 vertices
            sage: G = MatchingCoveredGraph(T)
            sage: G
            Matching covered complete graph: graph on 2 vertices
            sage: S1 = [2, 3, 4]
            sage: G.add_vertices(S1)
            Traceback (most recent call last):
            ...
            ValueError: isolated vertices are not allowed in matching covered graphs
            sage: S2 = [None, None]
            sage: G.add_vertices(S2)
            Traceback (most recent call last):
            ...
            ValueError: isolated vertices are not allowed in matching covered graphs
            sage: S3 = [2, None, None, 5]
            sage: G.add_vertices(S3)
            Traceback (most recent call last):
            ...
            ValueError: isolated vertices are not allowed in matching covered graphs
        """
    def allow_loops(self, new, check: bool = True) -> None:
        """
        Change whether loops are allowed in (matching covered) graphs.

        .. NOTE::

            This method overwrites the
            :meth:`~sage.graphs.generic_graph.GenericGraph.allow_loops` method
            to ensure that loops are forbidden in :class:`~MatchingCoveredGraph`.

        INPUT:

        - ``new`` -- boolean

        - ``check`` -- boolean (default: ``True``); whether to remove existing
          loops from the graph when the new status is ``False``. It is an
          argument in
          :meth:`~sage.graphs.generic_graph.GenericGraph.allow_loops` method
          and is not used in this overwritten one.

        OUTPUT:

        - A :exc:`ValueError` is returned with no change to the existing
          (matching covered) graph if ``new`` is ``True`` since a matching
          covered graph, by definition, is free of self-loops. If ``new`` is
          set to ``False``, there is no output.

        EXAMPLES:

        Petersen graph is matching covered::

            sage: P = graphs.PetersenGraph()
            sage: P.is_matching_covered()
            True
            sage: G = MatchingCoveredGraph(P)
            sage: G.allow_loops(True)
            Traceback (most recent call last):
            ...
            ValueError: loops are not allowed in matching covered graphs

        .. SEEALSO::

            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.allows_loops`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.has_loops`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.loop_edges`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.loop_vertices`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.loops`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.number_of_loops`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.remove_loops`
        """
    def allows_loops(self):
        """
        Return whether loops are permitted in (matching covered) graphs.

        .. NOTE::

            This method overwrites the
            :meth:`~sage.graphs.generic_graph.GenericGraph.allows_loops` method
            to show that loops are forbidden in :class:`~MatchingCoveredGraph`.

        OUTPUT:

        - A boolean value ``False`` is returned, since matching covered graphs,
          by definition, are free of loops.

        EXAMPLES:

        Petersen graph is matching covered::

            sage: P = graphs.PetersenGraph()
            sage: P.is_matching_covered()
            True
            sage: G = MatchingCoveredGraph(P)
            sage: G.allows_loops()
            False

        .. SEEALSO::

            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.allow_loops`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.has_loops`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.loop_edges`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.loop_vertices`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.loops`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.number_of_loops`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.remove_loops`
        """
    def canonical_partition(self):
        """
        Return the canonical partition of the (matching covered) graph.

        For a matching covered graph `G`, a subset `B` of the vertex set `V` is
        a barrier if `|B| = o(G - B)`, where `|B|` denotes the cardinality of
        the set `B` and `o(G - B)` denotes the number of odd components in the
        graph `G - B`. And a barrier `B` is a maximal barrier if `C` is not a
        barrier for each `C` such that `B \\subset C \\subseteq V`.

        Note that in a matching covered graph, each vertex belongs to a unique
        maximal barrier. The maximal barriers of a matching covered graph
        partitions its vertex set and the partition of the vertex set of a
        matching covered graph into its maximal barriers is called as its
        *canonical* *partition*.

        OUTPUT:

        - A list of sets that constitute a (canonical) partition of the vertex
          set, wherein each set is a (unique) maximal barrier of the (matching
          covered) graph.

        EXAMPLES:

        Show the maximal barrier of the graph `K_4 \\odot K_{3, 3}`::

            sage: G = Graph([
            ....:    (0, 2), (0, 3), (0, 4), (1, 2),
            ....:    (1, 3), (1, 4), (2, 5), (3, 6),
            ....:    (4, 7), (5, 6), (5, 7), (6, 7)
            ....: ])
            sage: H = MatchingCoveredGraph(G)
            sage: H.canonical_partition()
            [{0}, {1}, {2, 3, 4}, {5}, {6}, {7}]

        For a bicritical graph (for instance, the Petersen graph), the
        canonical partition constitutes of only singleton sets each containing
        an individual vertex::

            sage: P = graphs.PetersenGraph()
            sage: G = MatchingCoveredGraph(P)
            sage: G.canonical_partition()
            [{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}]

        For a bipartite matching covered graph (for instance, the Hexahedral
        graph), the canonical partition consists of two sets each of which
        corresponds to the individual color class::

            sage: H = graphs.HexahedralGraph()
            sage: G = MatchingCoveredGraph(H)
            sage: G.canonical_partition()
            [{0, 2, 5, 7}, {1, 3, 4, 6}]
            sage: B = BipartiteGraph(H)
            sage: list(B.bipartition()) == G.canonical_partition()
            True

        REFERENCES:

            - [LM2024]_

        .. SEEALSO::

            - :meth:`~sage.graphs.graph.Graph.is_bicritical`
            - :meth:`~sage.graphs.graph.Graph.is_matching_covered`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.maximal_barrier`
        """
    def delete_vertex(self, vertex, in_order: bool = False) -> None:
        """
        Delete a vertex, removing all incident edges.

        .. NOTE::

            This method overwrites the
            :meth:`~sage.graphs.generic_graph.GenericGraph.delete_vertex`
            method to ensure that an odd order is forbidden in
            :class:`~MatchingCoveredGraph`.

        INPUT:

        - ``vertex`` -- a vertex that is to be deleted.

        - ``in_order`` -- boolean (default: ``False``); if ``True``, this
          deletes the `i`-th vertex in the sorted list of vertices, i.e.
          ``G.vertices(sort=True)[i]``

        OUTPUT:

        - Deleting a non-existent vertex raises a :exc:`ValueError` exception;
          also a (different) :exc:`ValueError` is returned on deleting an
          existing vertex since matching covered graphs are of even order. In
          both cases no modifications are made to the existing (matching
          covered) graph.

        EXAMPLES:

        Deleting a non-existent vertex::

            sage: W = graphs.WheelGraph(12)
            sage: G = MatchingCoveredGraph(W)
            sage: u = 100
            sage: G.delete_vertex(u)
            Traceback (most recent call last):
            ...
            ValueError: vertex (100) not in the graph
            sage: G.delete_vertex(vertex=u, in_order=True)
            Traceback (most recent call last):
            ...
            ValueError: vertex (100) not in the graph

        Deleting an existing vertex::

            sage: W = graphs.WheelGraph(12)
            sage: G = MatchingCoveredGraph(W)
            sage: u = next(G.vertex_iterator())
            sage: G.delete_vertex(u)
            Traceback (most recent call last):
            ...
            ValueError: odd order is not allowed for matching covered graphs
            sage: G.delete_vertex(vertex=u, in_order=True)
            Traceback (most recent call last):
            ...
            ValueError: odd order is not allowed for matching covered graphs
        """
    def delete_vertices(self, vertices) -> None:
        """
        Delete specified vertices form ``self``.

        This method deletes the vertices from the iterable container
        ``vertices`` from ``self`` along with incident edges. An error is
        raised if the resulting graph is not matching covered.

        .. NOTE::

            This method overwrites the
            :meth:`~sage.graphs.generic_graph.GenericGraph.delete_vertices`
            method to ensure that an odd order is forbidden in
            :class:`~MatchingCoveredGraph`.

        INPUT:

        - ``vertices`` -- a list/ set of vertices that are to be deleted.

        OUTPUT:

        - Deleting a non-existent vertex will raise a :exc:`ValueError`
          exception, in which case none of the vertices in ``vertices``
          is deleted.

        - If all of the vertices in the list/ set provided exist in the graph,
          but the resulting graph after deletion of all of those is not
          matching covered, then a :exc:`ValueError` exception is raised
          without any alterations to the existing (matching covered) graph,
          otherwise the vertices are deleted and nothing is returned.

        EXAMPLES:

        Providing with an empty list of vertices::

            sage: C = graphs.CycleGraph(6)
            sage: G = MatchingCoveredGraph(C)
            sage: G.delete_vertices([])
            sage: G == C
            True

        Removing all the existent vertices::

            sage: M = graphs.MoebiusLadderGraph(10)
            sage: G = MatchingCoveredGraph(M)
            sage: S = list(G.vertices())
            sage: G.delete_vertices(S)
            Traceback (most recent call last):
            ...
            ValueError: the resulting graph after the removal of the vertices
            is trivial, therefore is not matching covered

        Providing with a list of vertices with at least one non-existent
        vertex::

            sage: S = graphs.StaircaseGraph(4)
            sage: S
            Staircase graph: Graph on 8 vertices
            sage: G = MatchingCoveredGraph(S)
            sage: G
            Matching covered staircase graph: graph on 8 vertices
            sage: T = list(range(5, 20, 2))
            sage: G.delete_vertices(T)
            Traceback (most recent call last):
            ...
            ValueError: vertex (9) not in the graph

        Removing an odd no. of distinct vertices from
        a matching covered graph::

            sage: P = graphs.PetersenGraph()
            sage: G = MatchingCoveredGraph(P)
            sage: S = [0, 1, 2, 10, 10, 100]
            sage: G.delete_vertices(S)
            Traceback (most recent call last):
            ...
            ValueError: an odd no. of distinct vertices can not be
            removed from a matching covered graph

        Providing with a list of existent vertices whose deletion results in a
        graph which is not matching covered::

            sage: S = graphs.StaircaseGraph(4)
            sage: S
            Staircase graph: Graph on 8 vertices
            sage: G = MatchingCoveredGraph(S)
            sage: G
            Matching covered staircase graph: graph on 8 vertices
            sage: T = [1, 4]
            sage: G.delete_vertices(T)
            Traceback (most recent call last):
            ...
            ValueError: the resulting graph after the removal of
            the vertices is not matching covered

        Providing with a list of existent vertices after the deletion of which
        the resulting graph is still matching covered; note that in the
        following example, after the deletion of two vertices from a staircase
        graph, the resulting graph is NOT a staircase graph
        (see :issue:`38768`)::

            sage: S = graphs.StaircaseGraph(4)
            sage: S
            Staircase graph: Graph on 8 vertices
            sage: G = MatchingCoveredGraph(S)
            sage: G
            Matching covered staircase graph: graph on 8 vertices
            sage: T = [6, 7]
            sage: G.delete_vertices(T)
            sage: G  # Matching covered graph on 6 vertices
            Matching covered staircase graph: graph on 6 vertices
        """
    def get_matching(self):
        """
        Return an :class:`~EdgesView` of ``self._matching``.

        OUTPUT:

        - This method returns :class:`EdgesView` of the edges of a
          perfect matching of the (matching covered) graph.

        EXAMPLES:

        If one specifies a perfect matching while initializing the object, the
        value of ``self._matching`` is the same matching::

            sage: P = graphs.PetersenGraph()
            sage: M = [(0, 1), (2, 3), (4, 9), (5, 7), (6, 8)]
            sage: G = MatchingCoveredGraph(P, M)
            sage: sorted(G.get_matching())
            [(0, 1), (2, 3), (4, 9), (5, 7), (6, 8)]
            sage: M == sorted(G.get_matching())
            True

        If no matching is specified while initializing a matching
        covered graph, a perfect matching is computed
        :meth:`~sage.graphs.graph.Graph.matching` and that is captured as
        ``self._matching``::

            sage: P = graphs.PetersenGraph()
            sage: M = P.matching()
            sage: G = MatchingCoveredGraph(P)
            sage: sorted(G.get_matching())
            [(0, 5, None), (1, 6, None), (2, 7, None), (3, 8, None), (4, 9, None)]
            sage: sorted(M) == sorted(G.get_matching())
            True
        """
    def maximal_barrier(self, vertex):
        """
        Return the (unique) maximal barrier containing the vertex.

        For a matching covered graph `G`, a subset `B` of the vertex set `V` is
        a barrier if `|B| = o(G - B)`, where `|B|` denotes the cardinality of
        the set `B` and `o(G - B)` denotes the number of odd components in the
        graph `G - B`. And a barrier `B` is a maximal barrier if `C` is not a
        barrier for each `C` such that `B \\subset C \\subseteq V`.

        In a matching covered graph, each vertex belongs to a unique maximal
        barrier, which is a consequence of the following theorem.

        .. RUBRIC:: Theorem [LM2024]_:

        Let `u` and `v` be any two vertices in a matchable graph `G`. Then the
        graph `G - u - v` is matchable if and only if there is no barrier of
        `G` which contains both `u` and `v`.

        And in order to find the vertices that do not lie in the maximal
        barrier containing the provided vertex in linear time we take
        inspiration of the `M` alternating tree seach method [LR2004]_.

        INPUT:

        - ``vertex`` -- a vertex of the graph

        OUTPUT:

        - A :exc:`~ValueError` is returned if ``vertex`` is not a vertex of the
          graph, otherwise a set of vertices that constitute the (unique)
          maximal barrier containing the vertex is returned.

        EXAMPLES:

        The graph `K_4 \\odot K_{3, 3}` is matching covered. Show the set of
        vertices in the (unique) maximal barrier containing the vertex `2`::

            sage: G = Graph([
            ....:    (0, 2), (0, 3), (0, 4), (1, 2),
            ....:    (1, 3), (1, 4), (2, 5), (3, 6),
            ....:    (4, 7), (5, 6), (5, 7), (6, 7)
            ....: ])
            sage: H = MatchingCoveredGraph(G)
            sage: B = H.maximal_barrier(2)
            sage: B
            {2, 3, 4}

        Let `B` be a maximal barrier of a matching covered graph `G` (which is,
        of course, a matchable graph). The graph, `J := G - B` has no even
        component::

            sage: J = G.copy()
            sage: J.delete_vertices(B)
            sage: all(len(K)%2 != 0 for K in J.connected_components(sort=True))
            True

        Let `B` be a maximal barrier in a matching covered graph `G` and let
        `M` be a perfect matching of `G`. If `K` is an odd component of
        `J := G - B`, then `M \\cap \\partial_G(K)` has precisely one edge and if
        `v` is the end of that edge in `V(K)`, then `M \\cap E(K)` is a perfect
        matching of `K - v`::

            sage: K = J.subgraph(vertices=(J.connected_components(sort=True))[0])
            sage: # Let F := \\partial_G(K) and T := M \\cap F
            sage: F = [edge for edge in G.edge_iterator()
            ....:      if (edge[0] in K and edge[1] not in K)
            ....:      or (edge[0] not in K and edge[1] in K)
            ....: ]
            sage: M = H.get_matching()
            sage: T = [edge for edge in F if edge in M]
            sage: len(T) == 1
            True
            sage: v = T[0][0] if T[0][0] in K else T[0][1]
            sage: # Let N := M \\cap E(K) and L := K - v
            sage: N = Graph([edge for edge in K.edge_iterator() if edge in M])
            sage: L = K.copy()
            sage: L.delete_vertex(v)
            sage: # Check if N is a perfect matching of L
            sage: L.order() == 2*N.size()
            True

        Let `B` be a maximal barrier of a matching covered graph `G` (which is,
        of course, a matchable graph). The graph induced by each component of
        `G - B` is factor critical::

            sage: all((K.subgraph(vertices=connected_component)).is_factor_critical()
            ....:     for connected_component in K.connected_components(sort=True)
            ....: )
            True

        For a bicritical graph (for instance, the Petersen graph), for each
        vertex the maximal barrier is a singleton set containing only that
        vertex::

            sage: P = graphs.PetersenGraph()
            sage: G = MatchingCoveredGraph(P)
            sage: u = 0
            sage: set([u]) == G.maximal_barrier(u)
            True

        In a bipartite matching covered graph (for instance, the Hexahedral
        graph), for a vertex, the maximal barrier is the set of vertices of
        the color class that the particular vertex belongs to. In other words,
        there are precisely two maximal barriers in a bipartite matching
        covered graph, that is, the vertex sets of the individual color class::

            sage: G = graphs.HexahedralGraph()
            sage: H = MatchingCoveredGraph(G)
            sage: A, _ = H.bipartite_sets()
            sage: # needs random
            sage: import random
            sage: a = random.choice(list(A))
            sage: A == H.maximal_barrier(a)
            True

        Maximal barriers of matching covered graph constitute a partition of
        its vertex set::

            sage: S = set()
            sage: for v in H:
            ....:     B = tuple(sorted(list(H.maximal_barrier(v))))
            ....:     S.add(B)
            sage: S = list(S)
            sage: # Check that S is a partition of the vertex set of H
            sage: # Part 1: Check if S spans the vertex set of H
            sage: sorted([u for B in S for u in B]) == sorted(list(H))
            True
            sage: # Part 2: Check if each maximal barrier in S is disjoint
            sage: is_disjoint = True
            sage: for i in range(len(S)):
            ....:     for j in range(i+1, len(S)):
            ....:         c = [v for v in S[i] if v in S[j]]
            ....:         is_disjoint = (len(c) == 0)
            sage: is_disjoint
            True

        TESTS:

        Providing with a nonexistent vertex::

            sage: P = graphs.PetersenGraph()
            sage: G = MatchingCoveredGraph(P)
            sage: G.maximal_barrier('')
            Traceback (most recent call last):
            ...
            ValueError: vertex  not in the graph
            sage: G.maximal_barrier(100)
            Traceback (most recent call last):
            ...
            ValueError: vertex 100 not in the graph

        REFERENCES:

        - [LZ2004]_
        - [LM2024]_

        .. SEEALSO::

            - :meth:`~sage.graphs.graph.Graph.is_bicritical`
            - :meth:`~sage.graphs.graph.Graph.is_matching_covered`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.canonical_partition`
        """
    def has_loops(self) -> bool:
        """
        Check whether there are loops in the (matching covered) graph.

        .. NOTE::

            This method overwrites the
            :meth:`~sage.graphs.generic_graph.GenericGraph.has_loops` method in
            order to return ``False`` as matching covered graphs are always
            free of looped edges.

        OUTPUT:

        - A boolean ``False`` is returned since matching covered graphs, by
          definition, are free of self-loops.

        EXAMPLES:

        A matching covered graph, for instance the Petersen graph, is always free
        of loops::

            sage: P = graphs.PetersenGraph()
            sage: G = MatchingCoveredGraph(P)
            sage: G
            Matching covered petersen graph: graph on 10 vertices
            sage: G.has_loops()
            False
            sage: G.allows_loops()
            False
            sage: G.add_edge(0, 0)
            Traceback (most recent call last):
            ...
            ValueError: loops are not allowed in matching covered graphs

        A matching covered graph may support multiple edges, still no
        loops are allowed::

            sage: K = graphs.CompleteGraph(2)
            sage: G = MatchingCoveredGraph(K)
            sage: G.allow_multiple_edges(True)
            sage: G
            Matching covered complete graph: multi-graph on 2 vertices
            sage: G.add_edge(0, 1, 'label')
            sage: G.add_edge(0, 0)
            Traceback (most recent call last):
            ...
            ValueError: loops are not allowed in matching covered graphs
            sage: G.edges(sort=False)
            [(0, 1, None), (0, 1, 'label')]
            sage: G.allows_loops()
            False
            sage: G.has_loops()
            False
            sage: G.allow_loops(True)
            Traceback (most recent call last):
            ...
            ValueError: loops are not allowed in matching covered graphs

        .. SEEALSO::

            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.allow_loops`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.allows_loops`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.loop_edges`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.loop_vertices`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.loops`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.number_of_loops`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.remove_loops`
        """
    def has_perfect_matching(G, algorithm: str = 'Edmonds', solver=None, verbose: int = 0, *, integrality_tolerance: float = 0.001):
        '''
        Check whether the graph has a perfect matching.

        .. NOTE::

            This method overwrites the
            :meth:`~sage.graphs.graph.Graph.has_perfect_matching` method in
            order to return ``True`` (provided the input arguments are valid)
            as matching covered graphs always admit a perfect matching.

        INPUT:

        - ``algorithm`` -- string (default: ``\'Edmonds\'``)

          - ``\'Edmonds\'`` uses Edmonds\' algorithm as implemented in NetworkX to
            find a matching of maximal cardinality, then check whether this
            cardinality is half the number of vertices of the graph.

          - ``\'LP_matching\'`` uses a Linear Program to find a matching of
            maximal cardinality, then check whether this cardinality is half the
            number of vertices of the graph.

          - ``\'LP\'`` uses a Linear Program formulation of the perfect matching
            problem: put a binary variable ``b[e]`` on each edge `e`, and for
            each vertex `v`, require that the sum of the values of the edges
            incident to `v` is 1.

        - ``solver`` -- string (default: ``None``); specifies a Mixed Integer
          Linear Programming (MILP) solver to be used. If set to ``None``, the
          default one is used. For more information on MILP solvers and which
          default solver is used, see the method :meth:`solve
          <sage.numerical.mip.MixedIntegerLinearProgram.solve>` of the class
          :class:`MixedIntegerLinearProgram
          <sage.numerical.mip.MixedIntegerLinearProgram>`.

        - ``verbose`` -- integer (default: 0); sets the level of verbosity:
          set to 0 by default, which means quiet (only useful when
          ``algorithm == "LP_matching"`` or ``algorithm == "LP"``)

        - ``integrality_tolerance`` -- float; parameter for use with MILP
          solvers over an inexact base ring; see
          :meth:`MixedIntegerLinearProgram.get_values`.

        OUTPUT:

        - If the input arguments are valid, a boolean (``True``) is returned as
          a maximum matching of a matching covered graph is always a perfect
          matching, otherwise a :exc:`~ValueError` is raised.

        EXAMPLES:

        Note that regardless of the algorithm (as long as the input arguments
        are in valid format), the method always returns the boolean ``True``::

            sage: P = graphs.PetersenGraph()
            sage: P.has_perfect_matching()  # Calls Graph.has_perfect_matching()
            True
            sage: G = MatchingCoveredGraph(P)
            sage: G.has_perfect_matching()  # Calls MatchingCoveredGraph.has_perfect_matching()
            True
            sage: W = graphs.WheelGraph(6)
            sage: H = MatchingCoveredGraph(W)
            sage: H.has_perfect_matching(algorithm=\'LP_matching\')
            True

        Providing with an algorithm, that is not one of ``\'Edmonds\'``,
        ``\'LP_matching\'`` or ``\'LP\'``::

            sage: S = graphs.StaircaseGraph(4)
            sage: J = MatchingCoveredGraph(S)
            sage: J.has_perfect_matching(algorithm=\'algorithm\')
            Traceback (most recent call last):
            ...
            ValueError: algorithm must be set to \'Edmonds\',
            \'LP_matching\' or \'LP\'
        '''
    def is_biconnected(self):
        """
        Check whether the (matching covered) graph is biconnected.

        A biconnected graph is a connected graph on two or more vertices that
        is not broken into disconnected pieces by deleting any single vertex.
        By definition of matching covered graphs, it follows that a graph, that
        is matching covered, is biconnected.

        Observe that `K_2` (upto multiple edges) is biconnected. A matching
        covered graph `G`, that is not `K_2` (upto multiple edges), has at
        least four vertices and four edges. Consider any two adjacent edges
        (`e` and `f`) of `G`. Take a perfect matching `M` of `G` containing
        the edge `e` and a different perfect matching `N` of `G` containing
        the edge `f`. Observe that the symmetric difference of `M` and `N`
        has a cycle containing both of the edges `e` and `f`. Thus, each edge
        of `G` is contained in some cycle of `G`. Therefore, `G` is
        biconnected.

        .. NOTE::

            This method overwrites the
            :meth:`~sage.graphs.graph.Graph.is_biconnected` method
            in order to return ``True`` as matching covered graphs are
            biconnected.

        EXAMPLES:

        The complete graph on two vertices is the smallest biconnected graph
        that is matching covered::

            sage: K2 = graphs.CompleteGraph(2)
            sage: G = MatchingCoveredGraph(K2)
            sage: G.is_biconnected()
            True

        Petersen graph is matching covered and biconnected::

            sage: P = graphs.PetersenGraph()
            sage: G = MatchingCoveredGraph(P)
            sage: G.is_biconnected()
            True

        .. SEEALSO::

            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.is_connected`
        """
    def is_brace(self, coNP_certificate: bool = False):
        """
        Check if the (matching covered) graph is a brace.

        A matching covered graph which is free of nontrivial tight cuts is
        called a *brace* if it is bipartite. Let `G := (A \\cup B, E)` be a
        bipartite matching covered graph on six or more vertices. The
        following statements are equivalent [LM2024]_:

        1. `G` is a brace (aka free of nontrivial tight cuts).
        2. `G - a_1 - a_2 - b_1 - b_2` has a perfect matching for any two
           distinct vertices `a_1` and `a_2` in `A` and any two distinct
           vertices `b_1` and `b_2` in `B`.
        3. `G` is two extendable (any two nonadjacent distinct edges can be
           extended to some perfect matching of `G`).
        4. `|N(X)| \\geq |X| + 2`, for all `X ⊂ A` such that `0 < |X| <
           |A| - 1`, where `N(S) := \\{b \\mid (a, b) \\in E ∧ a \\in S\\}` is called
           the neighboring set of `S`.
        5. `G - a - b` is matching covered, for some perfect matching `M` of
           `G` and for each edge `ab` in `M`.

        We shall be using the 5th characterization mentioned above in order
        to determine whether the provided bipartite matching covered graph
        is a brace or not using *M*-alternating tree search [LZ2001]_.

        INPUT:

        - ``coNP_certificate`` -- boolean (default: ``False``)

        OUTPUT:

        - If the input matching covered graph is not bipartite, a
          :exc:`ValueError` is returned.

        - If the input bipartite matching covered graph is a brace, a boolean
          ``True`` is returned if ``coNP_certificate`` is set to ``False``
          otherwise a 5-tuple ``(True, None, None, None, None)`` is returned.

        - If the input bipartite matching covered graph is not a brace, a
          boolean ``False`` is returned if ``coNP_certificate`` is set to
          ``False`` otherwise a 5-tuple of

          1. a boolean ``False``,

          2. a list of edges constituting a nontrivial tight cut (which is a
             nontrivial barrier cut)

          3. a set of vertices of one of the shores of the nontrivial tight cut

          4. a string 'nontrivial tight cut'

          5. a set of vertices showing the respective barrier

          is returned.

        EXAMPLES:

        The complete graph on two vertices `K_2` is the smallest brace::

            sage: K = graphs.CompleteGraph(2)
            sage: G = MatchingCoveredGraph(K)
            sage: G.is_brace()
            True

        The cycle graph on four vertices `C_4` is a brace::

            sage: C = graphs.CycleGraph(4)
            sage: G = MatchingCoveredGraph(C)
            sage: G.is_brace()
            True

        Each graph that is isomorphic to a biwheel is a brace::

            sage: B = graphs.BiwheelGraph(15)
            sage: G = MatchingCoveredGraph(B)
            sage: G.is_brace()
            True

        A circular ladder graph of order eight or more on `2n` vertices for
        an even `n` is a brace::

            sage: n = 10
            sage: CL = graphs.CircularLadderGraph(n)
            sage: G = MatchingCoveredGraph(CL)
            sage: G.is_brace()
            True

        A moebius ladder graph of order six or more on `2n` vertices for an odd
        `n` is a brace::

            sage: n = 11
            sage: ML = graphs.MoebiusLadderGraph(n)
            sage: G = MatchingCoveredGraph(ML)
            sage: G.is_brace()
            True

        Note that the union of the above mentioned four families of braces,
        that are:

        1. the biwheel graph ``BiwheelGraph(n)``,
        2. the circular ladder graph ``CircularLadderGraph(n)`` for even ``n``,
        3. the moebius ladder graph ``MoebiusLadderGraph(n)`` for odd ``n``,

        is referred to as the *McCuaig* *family* *of* *braces.*

        The only simple brace of order six is the complete graph of the same
        order, that is `K_{3, 3}`::

            sage: L = list(graphs(6,
            ....:          lambda G: G.size() <= 15 and
            ....:                    G.is_bipartite())
            ....: )
            sage: L = list(G for G in L if G.is_connected() and
            ....:                          G.is_matching_covered()
            ....: )
            sage: M = list(MatchingCoveredGraph(G) for G in L)
            sage: B = list(G for G in M if G.is_brace())
            sage: K = graphs.CompleteBipartiteGraph(3, 3)
            sage: G = MatchingCoveredGraph(K)
            sage: next(iter(B)).is_isomorphic(G)
            True

        The nonplanar `K_{3, 3}`-free brace Heawood graph is the unique cubic
        graph of girth six with the fewest number of vertices (that is 14).
        Note that by `K_{3, 3}`-free, it shows that the Heawood graph does not
        contain a subgraph that is isomophic to a graph obtained by
        bisubdivision of `K_{3, 3}`::

            sage: K = graphs.CompleteBipartiteGraph(3, 3)
            sage: J = graphs.HeawoodGraph()
            sage: H = MatchingCoveredGraph(J)
            sage: H.is_brace() and not H.is_planar() and \\\n            ....: H.is_regular(k=3) and H.girth() == 6
            True

        Braces of order six or more are 3-connected::

            sage: H = graphs.HexahedralGraph()
            sage: G = MatchingCoveredGraph(H)
            sage: G.is_brace() and G.is_triconnected()
            True

        Braces of order four or more are 2-extendable::

            sage: H = graphs.EllinghamHorton54Graph()
            sage: G = MatchingCoveredGraph(H)
            sage: G.is_brace()
            True
            sage: e = next(G.edge_iterator(labels=False)); f = None
            sage: for f in G.edge_iterator(labels=False):
            ....:     if not (set(e) & set(f)):
            ....:          break
            sage: S = [u for x in [e, f] for u in set(x)]
            sage: J = H.copy(); J.delete_vertices(S)
            sage: M = Graph(J.matching())
            sage: M.add_edges([e, f])
            sage: if all(d == 1 for d in M.degree()) and \\\n            ....:    G.order() == M.order() and \\\n            ....:    G.order() == 2*M.size():
            ....:      print(f'graph {G} is 2-extendable')
            graph Ellingham-Horton 54-graph is 2-extendable

        Every edge in a brace of order at least six is removable::

            sage: H = graphs.CircularLadderGraph(8)
            sage: G = MatchingCoveredGraph(H)
            sage: # len(G.removble_edges()) == G.size()
            # True

        Every brace of order eight has the hexahedral graph as a spanning
        subgraph::

            sage: H = graphs.HexahedralGraph()
            sage: L = list(graphs(8,
            ....:          lambda G: G.size() <= 28 and
            ....:                    G.is_bipartite())
            ....: )
            sage: L = list(G for G in L if G.is_connected() and
            ....:                          G.is_matching_covered()
            ....: )
            sage: M = list(MatchingCoveredGraph(G) for G in L)
            sage: B = list(G for G in M if G.is_brace())
            sage: C = list(G for G in M if Graph(G).subgraph_search(H) is not None)
            sage: B == C
            True

        For every brace `G[A, B]` of order at least six, the graph
        `G - a_1 - a_2 - b_1 - b_2` has a perfect matching for any two distinct
        vertices `a_1` and `a_2` in `A` and any two distinct vertices `b_1` and
        `b_2` in `B`::

            sage: H =  graphs.CompleteBipartiteGraph(10, 10)
            sage: G = MatchingCoveredGraph(H)
            sage: G.is_brace()
            True
            sage: S = [0, 1, 10, 12]
            sage: G.delete_vertices(S)
            sage: G.has_perfect_matching()
            True

        For a brace `G[A, B]` of order six or more, `|N(X)| \\geq |X| + 2`, for
        all `X \\subset A` such that `0 < |X| <|A| - 1`, where
        `N(S) := \\{b | (a, b) \\in E \\^ a \\in S\\}` is called the neighboring set
        of `S`::

            sage: H = graphs.MoebiusLadderGraph(15)
            sage: G = MatchingCoveredGraph(H)
            sage: G.is_brace()
            True
            sage: A, _ = G.bipartite_sets()
            sage: # needs random
            sage: X = random.sample(list(A), random.randint(1, len(A) - 1))
            sage: N = {v for u in X for v in G.neighbor_iterator(u)}
            sage: len(N) >= len(X) + 2
            True

        For a brace `G` of order four or more with a perfect matching `M`, the
        graph `G - a - b` is matching covered for each edge `(a, b)` in `M`::

            sage: H = graphs.HeawoodGraph()
            sage: G = MatchingCoveredGraph(H)
            sage: G.is_brace()
            True
            sage: M = G.get_matching()
            sage: L = []
            sage: for a, b, *_ in M:
            ....:     J = G.copy(); J.delete_vertices([a, b])
            ....:     if J.is_matching_covered():
            ....:          L.append(J)
            sage: len(L) == len(M)
            True

        A cycle graph of order six or more is a bipartite matching covered
        graph, but is not a brace::

            sage: C = graphs.CycleGraph(10)
            sage: G = MatchingCoveredGraph(C)
            sage: G.is_brace()
            False

        A ladder graph of order six or more is a bipartite matching covered
        graph, that is not a brace. The tight cut decomposition of a ladder
        graph produces a list graphs the underlying graph of each of which
        is isomorphic to a 4-cycle::

            sage: L = graphs.LadderGraph(10)
            sage: G = MatchingCoveredGraph(L)
            sage: G.is_brace()
            False

        One may set the ``coNP_certificate`` to be ``True``::

            sage: H = graphs.HexahedralGraph()
            sage: G = MatchingCoveredGraph(H)
            sage: G.is_brace(coNP_certificate=True)
            (True, None, None, None, None)
            sage: C = graphs.CycleGraph(6)
            sage: D = MatchingCoveredGraph(C)
            sage: is_brace, nontrivial_tight_cut, nontrivial_odd_component, \\\n            ....: nontrivial_tight_cut_variant, cut_identifier = \\\n            ....: D.is_brace(coNP_certificate=True)
            sage: is_brace is False
            True
            sage: J = C.subgraph(vertices=nontrivial_odd_component)
            sage: J.is_isomorphic(graphs.PathGraph(3))
            True
            sage: len(nontrivial_tight_cut) == 2
            True
            sage: nontrivial_tight_cut_variant
            'nontrivial barrier cut'
            sage: # Corresponding barrier
            sage: cut_identifier == {a for u, v, *_ in nontrivial_tight_cut for a in [u, v] \\\n            ....: if a not in nontrivial_odd_component}
            True
            sage: for u, v, *_ in nontrivial_tight_cut:
            ....:     assert (u in nontrivial_odd_component and v not in nontrivial_odd_component)
            sage: L = graphs.LadderGraph(3) # A ladder graph with two constituent braces
            sage: G = MatchingCoveredGraph(L)
            sage: is_brace, nontrivial_tight_cut, nontrivial_odd_component, cut_variant, cut_identifier = \\\n            ....: G.is_brace(coNP_certificate=True)
            sage: is_brace is False
            True
            sage: G1 = L.copy()
            sage: G1.merge_vertices(list(nontrivial_odd_component))
            sage: G1.to_simple().is_isomorphic(graphs.CycleGraph(4))
            True
            sage: G2 = L.copy()
            sage: G2.merge_vertices([v for v in G if v not in nontrivial_odd_component])
            sage: G2.to_simple().is_isomorphic(graphs.CycleGraph(4))
            True
            sage: cut_variant
            'nontrivial barrier cut'
            sage: cut_identifier == {a for u, v, *_ in nontrivial_tight_cut for a in [u, v] \\\n            ....: if a not in nontrivial_odd_component}
            True
            sage: H = graphs.CompleteBipartiteGraph(3, 3)
            sage: H.delete_edge(0, 3)
            sage: G = MatchingCoveredGraph(H)
            sage: G.is_brace(coNP_certificate=True)
            (False,
             [(4, 1, None), (5, 1, None), (4, 2, None), (5, 2, None)],
             {0, 4, 5},
             'nontrivial barrier cut',
             {1, 2})

        If the input matching covered graph is nonbipartite, a
        :exc:`ValueError` is thrown::

            sage: K4 = graphs.CompleteGraph(4)
            sage: G = MatchingCoveredGraph(K4)
            sage: G.is_brace()
            Traceback (most recent call last):
            ...
            ValueError: the input graph is not bipartite
            sage: P = graphs.PetersenGraph()
            sage: H = MatchingCoveredGraph(P)
            sage: H.is_brace(coNP_certificate=True)
            Traceback (most recent call last):
            ...
            ValueError: the input graph is not bipartite

        .. SEEALSO::

            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.is_brick`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.bricks_and_braces`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.number_of_braces`
        """
    def is_brick(self, coNP_certificate: bool = False):
        """
        Check if the (matching covered) graph is a brick.

        A matching covered graph which is free of nontrivial tight cuts is
        called a *brick* if it is nonbipartite. A nonbipartite matching covered
        graph is a brick if and only if it is 3-connected and bicritical
        [LM2024]_.

        INPUT:

        - ``coNP_certificate`` -- boolean (default: ``False``)

        OUTPUT:

        - If the input matching covered graph is bipartite, a :exc:`ValueError`
          is returned.

        - If the input nonbipartite matching covered graph is a brick, a
          boolean ``True`` is returned if ``coNP_certificate`` is set to
          ``False``, otherwise a 5-tuple ``(True, None, None, None, None)`` is
          returned.

        - If the input nonbipartite matching covered graph is not a brick, a
          boolean ``False`` is returned if ``coNP_certificate`` is set to
          ``False``.

        - If ``coNP_certificate`` is set to ``True`` and the input nonbipartite
          graph is not a brick, a 5-tuple of

          1. a boolean ``False``,

          2. a list of lists of edges, each list constituting a nontrivial
             tight cut collectively representing a laminar tight cut,

          3. a list of set of vertices of one of the shores of those respective
             nontrivial tight cuts:

             #. In case of nontrivial barrier cuts, each of the shores is a
                nontrivial odd component with respect to a nontrivial barrier,
                thus the returned list forms mutually exclusive collection of
                (odd) sets.

             #. Otherwise each of the nontrivial tight cuts is a 2-separation
                cut, each of the shores form a subset sequence, with the
                `i` th shore being a proper subset of the `i + 1` th shore.

          4. a string showing whether the nontrivial tight cuts are barrier
             cuts (if the string is 'nontrivial barrier cut'), or 2-separation
             cuts (if the string is 'nontrivial 2-separation cut')

          5. a set of vertices showing the respective barrier if the
             nontrivial tight cuts are barrier cuts, or otherwise
             a set of two vertices constituting the corresponding
             two vertex cut (in this case the nontrivial tight cuts are
             2-separation cuts)

          is returned.

        EXAMPLES:

        The complete graph on four vertices `K_4` is the smallest brick::

            sage: K = graphs.CompleteGraph(4)
            sage: G = MatchingCoveredGraph(K)
            sage: G.is_brick()
            True

        The triangular circular ladder (a graph on six vertices), aka
        `\\overline{C_6}` is a brick::

            sage: C6Bar = graphs.CircularLadderGraph(3)
            sage: G = MatchingCoveredGraph(C6Bar)
            sage: G.is_brick()
            True

        Each of Petersen graph, Bicorn graph, Tricorn graph, Cubeplex graph,
        Twinplex graph, Wagner graph is a brick::

            sage: MatchingCoveredGraph(graphs.PetersenGraph()).is_brick() and \\\n            ....: MatchingCoveredGraph(graphs.StaircaseGraph(4)).is_brick() and \\\n            ....: MatchingCoveredGraph(graphs.TricornGraph()).is_brick() and \\\n            ....: MatchingCoveredGraph(graphs.CubeplexGraph()).is_brick() and \\\n            ....: MatchingCoveredGraph(graphs.TwinplexGraph()).is_brick() and \\\n            ....: MatchingCoveredGraph(graphs.WagnerGraph()).is_brick()
            True

        The Murty graph is the smallest simple brick that is not odd-intercyclic::

            sage: M = graphs.MurtyGraph()
            sage: G = MatchingCoveredGraph(M)
            sage: G.is_brick()
            True

        A circular ladder graph of order six or more on `2n` vertices for an
        odd `n` is a brick::

            sage: n = 11
            sage: CL = graphs.CircularLadderGraph(n)
            sage: G = MatchingCoveredGraph(CL)
            sage: G.is_brick()
            True

        A moebius ladder graph of order eight or more on `2n` vertices for an
        even `n` is a brick::

            sage: n = 10
            sage: ML = graphs.MoebiusLadderGraph(n)
            sage: G = MatchingCoveredGraph(ML)
            sage: G.is_brick()
            True

        A wheel graph of an even order is a brick::

            sage: W = graphs.WheelGraph(10)
            sage: G = MatchingCoveredGraph(W)
            sage: G.is_brick()
            True

        A graph that is isomorphic to a truncated biwheel graph is a brick::

            sage: TB = graphs.TruncatedBiwheelGraph(15)
            sage: G = MatchingCoveredGraph(TB)
            sage: G.is_brick()
            True

        Each of the graphs in the staircase graph family with order eight or
        more is a brick::

            sage: ST = graphs.StaircaseGraph(9)
            sage: G = MatchingCoveredGraph(ST)
            sage: G.is_brick()
            True

        Bricks are 3-connected::

            sage: P = graphs.PetersenGraph()
            sage: G = MatchingCoveredGraph(P)
            sage: G.is_brick()
            True
            sage: G.is_triconnected()
            True

        Bricks are bicritical::

            sage: P = graphs.PetersenGraph()
            sage: G = MatchingCoveredGraph(P)
            sage: G.is_brick()
            True
            sage: G.is_bicritical()
            True

        Examples of nonbipartite matching covered graphs that are not
        bricks::

            sage: H = Graph([
            ....:     (0, 3), (0, 4), (0, 7),
            ....:     (1, 3), (1, 5), (1, 7),
            ....:     (2, 3), (2, 6), (2, 7),
            ....:     (4, 5), (4, 6), (5, 6)
            ....: ])
            sage: G = MatchingCoveredGraph(H)
            sage: G.is_bipartite()
            False
            sage: G.is_bicritical()
            False
            sage: G.is_triconnected()
            True
            sage: G.is_brick()
            False
            sage: H = Graph([
            ....:     (0, 1), (0, 2), (0, 3), (0, 4), (1, 2),
            ....:     (1, 5), (2, 5), (3, 4), (3, 5), (4, 5)
            ....: ])
            sage: G = MatchingCoveredGraph(H)
            sage: G.is_bipartite()
            False
            sage: G.is_bicritical()
            True
            sage: G.is_triconnected()
            False
            sage: G.is_brick()
            False

        One may set the ``coNP_certificate`` to be ``True``::

            sage: K4 = graphs.CompleteGraph(4)
            sage: G = MatchingCoveredGraph(K4)
            sage: G.is_brick(coNP_certificate=True)
            (True, None, None, None, None)
            sage: # K(4) ⊙ K(3, 3) is nonbipartite but not a brick
            sage: H = graphs.MurtyGraph(); H.delete_edge(0, 1)
            sage: G = MatchingCoveredGraph(H)
            sage: G.is_brick(coNP_certificate=True)
            (False, [[(5, 2, None), (6, 3, None), (7, 4, None)]], [{5, 6, 7}],
             'nontrivial barrier cut', {2, 3, 4})
            sage: H = Graph([
            ....:     (0, 12), (0, 13), (0, 15), (1, 4), (1, 13), (1, 14),
            ....:     (1, 19), (2, 4), (2, 13), (2, 14), (2, 17), (3, 9),
            ....:     (3, 13), (3, 16), (3, 21), (4, 6), (4, 7), (5, 7),
            ....:     (5, 8), (5, 12), (6, 8), (6, 11), (7, 10), (8, 9),
            ....:     (9, 10), (10, 11), (11, 12), (14, 15), (14, 16), (15, 16),
            ....:     (17, 18), (17, 21), (18, 19), (18, 20), (19, 20), (20, 21)
            ....: ])
            sage: G = MatchingCoveredGraph(H)
            sage: G.is_brick(coNP_certificate=True)
            (False,
             [[(12, 0, None), (4, 1, None), (4, 2, None), (9, 3, None)],
              [(19, 1, None), (17, 2, None), (21, 3, None)],
              [(15, 0, None), (14, 1, None), (14, 2, None), (16, 3, None)]],
             [{4, 5, 6, 7, 8, 9, 10, 11, 12}, {17, 18, 19, 20, 21}, {14, 15, 16}],
             'nontrivial barrier cut', {0, 1, 2, 3})
            sage: J = Graph([
            ....:     (0, 1), (0, 2), (0, 3), (0, 4), (0, 5),
            ....:     (0, 6), (0, 7), (0, 8), (0, 9), (0, 10),
            ....:     (1, 2), (1, 11), (2, 11), (3, 4), (3, 11),
            ....:     (4, 11), (5, 6), (5, 11), (6, 11), (7, 8),
            ....:     (7, 11), (8, 11), (9, 10), (9, 11), (10, 11)
            ....: ])
            sage: G = MatchingCoveredGraph(J)
            sage: G.is_brick(coNP_certificate=True)
            (False,
             [[(0, 3, None),
               (0, 4, None),
               (0, 5, None),
               (0, 6, None),
               (0, 7, None),
               (0, 8, None),
               (0, 9, None),
               (0, 10, None),
               (1, 11, None),
               (2, 11, None)],
              [(0, 5, None),
               (0, 6, None),
               (0, 7, None),
               (0, 8, None),
               (0, 9, None),
               (0, 10, None),
               (1, 11, None),
               (2, 11, None),
               (3, 11, None),
               (4, 11, None)],
              [(0, 7, None),
               (0, 8, None),
               (0, 9, None),
               (0, 10, None),
               (1, 11, None),
               (2, 11, None),
               (3, 11, None),
               (4, 11, None),
               (5, 11, None),
               (6, 11, None)],
              [(0, 9, None),
               (0, 10, None),
               (1, 11, None),
               (2, 11, None),
               (3, 11, None),
               (4, 11, None),
               (5, 11, None),
               (6, 11, None),
               (7, 11, None),
               (8, 11, None)]],
             [{0, 1, 2},
              {0, 1, 2, 3, 4},
              {0, 1, 2, 3, 4, 5, 6},
              {0, 1, 2, 3, 4, 5, 6, 7, 8}],
             'nontrivial 2-separation cut',
             {0, 11})

        If the input matching covered graph is bipartite, a
        :exc:`ValueError` is thrown::

            sage: H = graphs.HexahedralGraph()
            sage: G = MatchingCoveredGraph(H)
            sage: G.is_brick()
            Traceback (most recent call last):
            ...
            ValueError: the input graph is bipartite
            sage: J = graphs.HeawoodGraph()
            sage: G = MatchingCoveredGraph(J)
            sage: G.is_brick(coNP_certificate=True)
            Traceback (most recent call last):
            ...
            ValueError: the input graph is bipartite

        .. SEEALSO::

            - :meth:`~sage.graphs.graph.Graph.is_bicritical`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.is_brace`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.bricks_and_braces`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.number_of_bricks`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.number_of_petersen_bricks`
        """
    def loop_edges(self, labels: bool = True):
        """
        Return a list of all loops in the (matching covered) graph.

        .. NOTE::

            This method overwrites the
            :meth:`~sage.graphs.generic_graph.GenericGraph.loop_edges` method
            in order to return an empty list as matching covered graphs are
            free of looped edges.

        INPUT:

        - ``labels`` -- boolean (default: ``True``); whether returned edges
          have labels (``(u,v,l)``) or not (``(u,v)``).

        OUTPUT:

        - A list capturing the edges that are loops in the matching covered
          graph; note that, the list is empty since matching covered graphs do
          not contain any looped edges.

        EXAMPLES:

        A matching covered graph, for instance the Heawood graph, by
        definition, is always free of loops::

            sage: H = graphs.HeawoodGraph()
            sage: G = MatchingCoveredGraph(H)
            sage: G
            Matching covered heawood graph: graph on 14 vertices
            sage: G.add_edge(0, 0)
            Traceback (most recent call last):
            ...
            ValueError: loops are not allowed in matching covered graphs
            sage: G.loops()
            []
            sage: G.loop_edges()
            []

        A matching covered graph may support multiple edges, still no
        loops are allowed::

            sage: C = graphs.CycleGraph(4)
            sage: G = MatchingCoveredGraph(C)
            sage: G.allow_multiple_edges(True)
            sage: G
            Matching covered cycle graph: multi-graph on 4 vertices
            sage: G.add_edge(0, 1, 'label')
            sage: G.add_edge(0, 0)
            Traceback (most recent call last):
            ...
            ValueError: loops are not allowed in matching covered graphs
            sage: G.edges(sort=False)
            [(0, 1, None), (0, 1, 'label'), (0, 3, None), (1, 2, None), (2, 3, None)]
            sage: G.loops()
            []
            sage: G.loop_edges()
            []

        One may set the ``label`` to either ``True`` or ``False``::

            sage: G.loop_edges(labels=False)
            []
            sage: G.loops(labels=True)
            []

        .. SEEALSO::

            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.allow_loops`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.allows_loops`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.has_loops`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.loop_vertices`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.loops`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.number_of_loops`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.remove_loops`
        """
    def loop_vertices(self):
        """
        Return a list of vertices with loops.

        .. NOTE::

            This method overwrites the
            :meth:`~sage.graphs.generic_graph.GenericGraph.loop_vertices`
            method in order to return an empty list as matching covered graphs
            are free of vertices that have looped edges.

        OUTPUT:

        - A list capturing the vertices that have loops in the matching covered
          graph; note that, the list is empty since matching covered graphs do
          not contain any looped edges.

        EXAMPLES:

        A matching covered graph, for instance the Möbius graph of order 8, by
        definition, is always free of loops::

            sage: M = graphs.MoebiusLadderGraph(4)
            sage: G = MatchingCoveredGraph(M)
            sage: G
            Matching covered moebius ladder graph: graph on 8 vertices
            sage: G.add_edge(0, 0)
            Traceback (most recent call last):
            ...
            ValueError: loops are not allowed in matching covered graphs
            sage: G.loop_vertices()
            []

        A matching covered graph may support multiple edges, still no
        loops are allowed::

            sage: S = graphs.StaircaseGraph(4)
            sage: G = MatchingCoveredGraph(S)
            sage: G.allow_multiple_edges(True)
            sage: G
            Matching covered staircase graph: multi-graph on 8 vertices
            sage: G.add_edge(0, 1, 'label')
            sage: G.add_edge(0, 0)
            Traceback (most recent call last):
            ...
            ValueError: loops are not allowed in matching covered graphs
            sage: G.edges(sort=False)
            [(0, 1, None), (0, 1, 'label'), (0, 3, None), (0, 6, None),
             (1, 2, None), (1, 4, None), (2, 5, None), (2, 7, None),
             (3, 4, None), (3, 6, None), (4, 5, None), (5, 7, None),
             (6, 7, None)]
            sage: G.loop_vertices()
            []

        .. SEEALSO::

            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.allow_loops`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.allows_loops`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.has_loops`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.loop_edges`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.loops`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.number_of_loops`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.remove_loops`
        """
    loops = loop_edges
    def number_of_loops(self):
        """
        Return the number of edges that are loops.

        .. NOTE::

            This method overwrites the
            :meth:`~sage.graphs.generic_graph.GenericGraph.number_of_loops`
            method in order to return 0 as matching covered graphs are free
            of looped edges.

        OUTPUT:

        - An integer, 0 is returned, since matching covered graphs do not
          contain zero loops.

        EXAMPLES:

        A matching covered graph, for instance the Truncated biwheel graph,
        by definition, is always free of loops::

            sage: T = graphs.TruncatedBiwheelGraph(5)
            sage: G = MatchingCoveredGraph(T)
            sage: G
            Matching covered truncated biwheel graph: graph on 10 vertices
            sage: G.add_edge(0, 0)
            Traceback (most recent call last):
            ...
            ValueError: loops are not allowed in matching covered graphs
            sage: G.loop_vertices()
            []
            sage: G.number_of_loops()
            0

        A matching covered graph may support multiple edges, still no
        loops are allowed::

            sage: B = graphs.BiwheelGraph(4)
            sage: G = MatchingCoveredGraph(B)
            sage: G.allow_multiple_edges(True)
            sage: G
            Matching covered biwheel graph: multi-graph on 8 vertices
            sage: G.add_edge(0, 1, 'label')
            sage: G.add_edge(0, 0)
            Traceback (most recent call last):
            ...
            ValueError: loops are not allowed in matching covered graphs
            sage: G.edges(sort=False)
            [(0, 1, None), (0, 1, 'label'), (0, 5, None), (0, 7, None),
             (1, 2, None), (1, 6, None), (2, 3, None), (2, 7, None),
             (3, 4, None), (3, 6, None), (4, 5, None), (4, 7, None),
             (5, 6, None)]
            sage: G.loop_vertices()
            []
            sage: G.number_of_loops()
            0

        .. SEEALSO::

            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.allow_loops`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.allows_loops`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.has_loops`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.loop_edges`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.loop_vertices`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.loops`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.remove_loops`
        """
    def remove_loops(self, vertices=None) -> None:
        """
        Remove loops on vertices in ``vertices``.

        .. NOTE::

            This method overwrites the
            :meth:`~sage.graphs.generic_graph.GenericGraph.remove_loops` method
            in order to return without any alteration as matching covered
            graphs are free of looped edges.

        INPUT:

        - ``vertices`` -- (default: ``None``) iterator container of vertex
          labels corresponding to which the looped edges are to be removed. If
          ``vertices`` is ``None``, remove all loops.

        OUTPUT:

        - Nothing is returned, as a matching covered graph is already devoid of
          any loops.

        EXAMPLES:

        A matching covered graph, for instance the Wheel graph of order six, is
        always free of loops::

            sage: W = graphs.WheelGraph(6)
            sage: G = MatchingCoveredGraph(W)
            sage: G
            Matching covered wheel graph: graph on 6 vertices
            sage: G.add_edge(0, 0)
            Traceback (most recent call last):
            ...
            ValueError: loops are not allowed in matching covered graphs
            sage: G.remove_loops()
            sage: G.edges(sort=True)
            [(0, 1, None), (0, 2, None), (0, 3, None), (0, 4, None),
             (0, 5, None), (1, 2, None), (1, 5, None), (2, 3, None),
             (3, 4, None), (4, 5, None)]

        A matching covered graph may support multiple edges, still no
        loops are allowed::

            sage: K = graphs.CompleteGraph(2)
            sage: G = MatchingCoveredGraph(K)
            sage: G.allow_multiple_edges(True)
            sage: G
            Matching covered complete graph: multi-graph on 2 vertices
            sage: G.add_edge(0, 1, 'label')
            sage: G.add_edge(0, 0)
            Traceback (most recent call last):
            ...
            ValueError: loops are not allowed in matching covered graphs
            sage: G.edges(sort=False)
            [(0, 1, None), (0, 1, 'label')]
            sage: G.remove_loops(vertices=[0, 1])
            sage: G.edges(sort=False)
            [(0, 1, None), (0, 1, 'label')]
            sage: G.remove_loops(vertices=[0..100])

        Note that the parameter ``vertices`` must be either ``None`` or an
        iterable::

            sage: G.remove_loops(vertices='')
            sage: G.edges(sort=False)
            [(0, 1, None), (0, 1, 'label')]
            sage: G.remove_loops(vertices=None)
            sage: G.edges(sort=False)
            [(0, 1, None), (0, 1, 'label')]
            sage: G.remove_loops(vertices=0)
            Traceback (most recent call last):
            ...
            TypeError: 'Integer' object is not iterable
            sage: G.remove_loops(vertices=False)
            Traceback (most recent call last):
            ...
            TypeError: 'bool' object is not iterable

        .. SEEALSO::

            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.allow_loops`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.allows_loops`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.has_loops`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.loop_edges`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.loop_vertices`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.loops`
            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.number_of_loops`
        """
    def subdivide_edge(self, *args) -> None:
        """
        Subdivide an edge `k` times.

        .. NOTE::

            This method overwrites the
            :meth:`~sage.graphs.generic_graph.GenericGraph.subdivide_edge`
            method to ensure that resultant graph is also matching covered.

        INPUT:

        The following forms are all accepted to subdivide `8` times the edge
        between vertices `1` and `2` labeled with ``'label'``.

        - ``G.subdivide_edge(1, 2, 8 )``
        - ``G.subdivide_edge((1, 2), 8 )``
        - ``G.subdivide_edge(1, 2, 'label', 8 )``
        - ``G.subdivide_edge((1, 2, 'label'), 8 )``

        .. NOTE::

            * If the given edge is labelled with `l`, all the edges created by
              the subdivision will have the same label.

            * If no label given, the label obtained from
              :meth:`~sage.graphs.generic_graph.GenericGraph.edge_label` will
              be used. If multiple such labels are present, the first one in
              the returned list will be used.

            * The number of subdivisions must be a nonnegative even integer in
              order to ensure the resultant graph is matching covered.

            * In the context of matching covered graphs, *bisubdividing* an edge
              *t* times is defined as subdividing the edge *2t* times, for some
              nonnegative integer *t*.

            * For two input arguments, the first one must be of the form
              `(u, v)` or `(u, v, label)`

        OUTPUT:

        - If an existent edge is provided with a valid format and the parameter
          ``k`` in the argument is a nonnegative even integer then the graph is
          updated and nothing is returned, otherwise a :exc:`ValueError` is
          returned if ``k`` is not a nonnegative even integer,

        - If the graph does not contain the edge provided, a :exc:`ValueError`
          is returned. Also, a :exc:`ValueError` is thrown in case the provided
          arguments are not valid.

        EXAMPLES:

        Subdividing `4` times an edge of the Petersen graph. Please note that
        the perfect matching captured at ``self.get_matching()`` also gets
        updated::

            sage: P = graphs.PetersenGraph()
            sage: G = MatchingCoveredGraph(P)
            sage: from collections import Counter
            sage: V, E = set(G.vertices()), list(G.edges(sort=True, sort_vertices=True))
            sage: M = set(G.get_matching())
            sage: G.subdivide_edge(0, 1, 4)
            sage: W, F = set(G.vertices()), list(G.edges(sort=True, sort_vertices=True))
            sage: N = set(G.get_matching())
            sage: sorted(W - V)
            [10, 11, 12, 13]
            sage: sorted(list((Counter(F) - Counter(E)).elements())), \\\n            ....: sorted(list((Counter(E) - Counter(F)).elements()))
            ([(0, 10, None), (1, 13, None), (10, 11, None), (11, 12, None),
             (12, 13, None)], [(0, 1, None)])
            sage: if (0, 1, None) in M:
            ....:     assert sorted(N - M), sorted(M - N) == \\\n            ....:         ([(0, 10, None), (1, 13, None), (11, 12, None)], [(0, 1, None)])
            ....: else:
            ....:     assert sorted(N - M), sorted(M - N) == \\\n            ....:         ([(10, 11, None), (12, 13, None)], [])

        Subdividing a multiple edge/ some multiple edges::

            sage: K = graphs.CycleGraph(4)
            sage: K.allow_multiple_edges(1)
            sage: K.add_edges([(0, 1, 2), (0, 1, 3), (0, 1, 0.5)])
            sage: K.delete_edge(0, 1, None)
            sage: G = MatchingCoveredGraph(K)
            sage: from collections import Counter
            sage: V, E = set(G.vertices()), list(G.edges(sort=True, sort_vertices=True))
            sage: G.edge_label(0, 1)
            [2, 3, 0.500000000000000]
            sage: G.subdivide_edge((0, 1), 6)  # the edge: (0, 1, 2)
            sage: G.subdivide_edge((0, 1, 3), 2)  # the edge: (0, 1, 3)
            sage: G.subdivide_edge(1, 2, None, 2)  # the edge: (1, 2, None)
            sage: W, F = set(G.vertices()), list(G.edges(sort=True, sort_vertices=True))
            sage: sorted(W - V)
            [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
            sage: sorted(list((Counter(F) - Counter(E)).elements())), \\\n            ....: sorted(list((Counter(E) - Counter(F)).elements()))
            ([(0, 4, 2), (0, 10, 3), (1, 9, 2), (1, 11, 3), (1, 12, None), (2, 13, None),
              (4, 5, 2), (5, 6, 2), (6, 7, 2), (7, 8, 2), (8, 9, 2), (10, 11, 3),
              (12, 13, None)], [(0, 1, 2), (0, 1, 3), (1, 2, None)])

        Setting ``k`` to `0` does not change the graph::

            sage: H = G.copy()
            sage: G.subdivide_edge(0, 4, 0)  # the edge: (0, 4, None)
            sage: H == G and H.edges(sort=True) == G.edges(sort=True)
            True

        If too many or too less arguments are given, an exception is raised::

            sage: G.subdivide_edge(0, 1, 'label', 4, 6)
            Traceback (most recent call last):
            ...
            ValueError: this method takes at least 2 and at most 4 arguments
            sage: G.subdivide_edge((0, 1, 'label', 4))
            Traceback (most recent call last):
            ...
            ValueError: this method takes at least 2 and at most 4 arguments

        A :exc:`ValueError` is returned for `k` being in an invalid format or
        being not an even nonnegative, or for nonexistent or invalid edges::

            sage: G.subdivide_edge(0, 4, 'label')  # No. of subdivision: 'label'
            Traceback (most recent call last):
            ...
            TypeError: '<' not supported between instances of 'str' and 'int'
            sage: G.subdivide_edge(0, 4, 3)  # No. of subdivisions: 3
            Traceback (most recent call last):
            ...
            ValueError: the number of subdivisions must be a nonnegative even integer,
            but found 3
            sage: G.subdivide_edge(0, 4, -1)  # No. of subdivisions: -1
            Traceback (most recent call last):
            ...
            ValueError: the number of subdivisions must be a nonnegative even integer,
            but found -1
            sage: G.subdivide_edge(0, 4, 0.5)  # No. of subdivisions: 0.5
            Traceback (most recent call last):
            ...
            ValueError: the number of subdivisions must be a nonnegative even integer,
            but found 0.500000000000000
            sage: G.subdivide_edge(0, 5, 4)
            Traceback (most recent call last):
            ...
            ValueError: the given edge (0, 5, None) does not exist
            sage: G.subdivide_edge((0, 5), 4)
            Traceback (most recent call last):
            ...
            ValueError: the given edge (0, 5, None) does not exist
            sage: G.subdivide_edge((0, 1, 'label', None), 4)
            Traceback (most recent call last):
            ...
            ValueError: for two input arguments, the first one must be of the form
            (u, v) or (u, v, l), but found: (0, 1, 'label', None)
            sage: G.subdivide_edge((0), 4)
            Traceback (most recent call last):
            ...
            TypeError: object of type 'sage.rings.integer.Integer' has no len()

        .. SEEALSO::

            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.subdivide_edges`
        """
    def subdivide_edges(self, edges, k) -> None:
        """
        Subdivide `k` times edges from an iterable container.

        For more information on the behaviour of this method, please refer to
        the documentation of
        :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.subdivide_edge`.

        .. NOTE::

            This method overwrites the
            :meth:`~sage.graphs.generic_graph.GenericGraph.subdivide_edges`
            method to ensure that resultant graph is also matching covered.

        INPUT:

        - ``edges`` -- an iterable of edges, each of which given either as
          ``(u, v)`` or ``(u, v, 'label')``

        - ``k`` -- a nonnegative even integer; common length of the
          subdivisions

        .. NOTE::

            * If the given edge is labelled with `l`, all the edges created by
              the subdivision will have the same label.

            * If no label given, the label obtained from
              :meth:`~sage.graphs.generic_graph.GenericGraph.edge_label` will
              be used. If multiple such labels are present, the first one in
              the returned list will be used.

            * The number of subdivisions must be a nonnegative even integer in
              order to ensure the resultant graph is matching covered.

            * In the context of matching covered graphs, *bisubdividing* an edge
              *t* times is defined as subdividing the edge *2t* times, for some
              nonnegative integer *t*.

            * Please note that if a single edge is present in the iterable, it
              is considered only one time for the subdivision operation.

        OUTPUT:

        - If existent edges are provided with a valid format and the parameter
          ``k`` in the argument is a nonnegative even integer then the graph is
          updated and nothing is returned, otherwise a :exc:`ValueError` is
          returned if ``k`` is not a nonnegative even integer,

        - If the graph does not contain at least one of the edges provided, a
          :exc:`ValueError` is returned. Also, a :exc:`ValueError` is thrown in case
          the provided arguments are not valid.

        EXAMPLES:

        Subdividing each edge of `K_4` some even number of times. Please note
        that the perfect matching captured at ``self.get_matching()`` also gets
        updated::

            sage: C = graphs.CycleGraph(4)
            sage: G = MatchingCoveredGraph(C)
            sage: from collections import Counter
            sage: V, E = set(G.vertices()), list(G.edges(sort=True, sort_vertices=True))
            sage: M = set(G.get_matching())
            sage: G.subdivide_edges(E, 2)
            sage: W, F = set(G.vertices()), list(G.edges(sort=True, sort_vertices=True))
            sage: N = set(G.get_matching())
            sage: sorted(W - V)
            [4, 5, 6, 7, 8, 9, 10, 11]
            sage: sorted(list((Counter(F) - Counter(E)).elements())), \\\n            ....: sorted(list((Counter(E) - Counter(F)).elements()))
            ([(0, 4, None), (0, 6, None), (1, 5, None), (1, 8, None),
              (2, 9, None), (2, 10, None), (3, 7, None), (3, 11, None),
              (4, 5, None), (6, 7, None), (8, 9, None), (10, 11, None)],
             [(0, 1, None), (0, 3, None), (1, 2, None), (2, 3, None)])
            sage: if (0, 1, None) in M:
            ....:     assert sorted(N - M), sorted(M - N) == \\\n            ....:         ([(0, 8, None), (1, 9, None), (2, 4, None), (3, 5, None), \\\n            ....:       (6, 7, None), (10, 11, None)], [(0, 1, None), (2, 3, None)])
            ....: else:
            ....:     assert sorted(N - M), sorted(M - N) == \\\n            ....:         ([(0, 6, None), (1, 10, None), (2, 11, None), (3, 7, None), \\\n            ....:           (4, 5, None), (8, 9, None)], [(0, 3, None), (1, 2, None)])

        If a single is present multiple times in the iterable, if that many (or
        more) edges are present in the graph, each of those edges gets subdivided::

            sage: C = graphs.CycleGraph(4)
            sage: G = MatchingCoveredGraph(C)
            sage: G.allow_multiple_edges(True)
            sage: G.add_edges([(0, 1)] * 3)
            sage: from collections import Counter
            sage: V, E = set(G.vertices()), list(G.edges(sort=True, sort_vertices=True))
            sage: M = list(G.get_matching())
            sage: G.subdivide_edges([(0, 1), (0, 1, None)], 2)
            sage: W, F = set(G.vertices()), list(G.edges(sort=True, sort_vertices=True))
            sage: N = set(G.get_matching())
            sage: sorted(W - V)
            [4, 5, 6, 7]
            sage: sorted(list((Counter(F) - Counter(E)).elements())), \\\n            ....: sorted(list((Counter(E) - Counter(F)).elements()))
            ([(0, 4, None), (0, 6, None), (1, 5, None), (1, 7, None),
              (4, 5, None), (6, 7, None)], [(0, 1, None), (0, 1, None)])
            sage: if (0, 1, None) in M:
            ....:     assert sorted(N - M), sorted(M - N) == \\\n            ....:         ([(0, 4, None), (1, 5, None)], [(0, 1, None)])
            ....:     assert sorted(N - M), sorted(M - N) == \\\n            ....:         ([(4, 5, None)], [])

        Subdividing edges with at least one of which is a multiple edge::

            sage: T = graphs.TricornGraph()
            sage: G = MatchingCoveredGraph(T)
            sage: G.allow_multiple_edges(True)
            sage: G.add_edges([
            ....:     (0, 1, 2), (0, 1, 3),
            ....:     (2, 3, 0.5), (2, 3, 4)
            ....: ])
            sage: G.delete_edge(0, 1, None)
            sage: from collections import Counter
            sage: V, E = set(G.vertices()), list(G.edges(sort=True, sort_vertices=True))
            sage: G.subdivide_edges([(0, 1), (1, 2), (2, 3)], 4)
            ....: # edges considered: (0, 1, 2), (1, 2, None), (2, 3, None)
            sage: W, F = set(G.vertices()), list(G.edges(sort=True, sort_vertices=True))
            sage: sorted(W - V)
            [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
            sage: sorted(list((Counter(F) - Counter(E)).elements())), \\\n            ....: sorted(list((Counter(E) - Counter(F)).elements()))
            ([(0, 10, 2), (1, 13, 2), (1, 14, None), (2, 17, None),
              (2, 18, None), (3, 21, None), (10, 11, 2), (11, 12, 2),
              (12, 13, 2), (14, 15, None), (15, 16, None), (16, 17, None),
              (18, 19, None), (19, 20, None), (20, 21, None)],
             [(0, 1, 2), (1, 2, None), (2, 3, None)])

        Setting ``k`` to `0` does not change the graph::

            sage: H = G.copy()
            sage: G.subdivide_edges([(0, 10), (1, 13), (2, 17)], 0)
            sage: H == G and H.edges(sort=True) == G.edges(sort=True)
            True

        Subdividing edges with at least one of which is nonexistent::

            sage: G.subdivide_edges([(4, 5), (1, 5)], 4)
            ....: # edges considered: (4, 5, None), (1, 5, None)
            Traceback (most recent call last):
            ...
            ValueError: the given edge (1, 5, None) does not exist
            sage: G.subdivide_edges([(0, 4), (0, 4, None)], 4)
            Traceback (most recent call last):
            ...
            ValueError: input contains 2 copies of the edge (0, 4, None),
            but the graph contains 1

        When ``k`` is not a nonnegative even integer::

            sage: G.subdivide_edges([(0, 1), (1, 2), (2, 3)], 3)
            Traceback (most recent call last):
            ...
            ValueError: the number of subdivisions must be a nonnegative even integer, but found 3

        Providing a noniterable object as ``edges``::

            sage: G.subdivide_edges(G.order(), 4)
            Traceback (most recent call last):
            ...
            ValueError: expected an iterable of edges, but got a non-iterable object

        Providing arguments in an invalid format::

            sage: G.subdivide_edges([(0, ), (0, 1, 'label')], 4)
            Traceback (most recent call last):
            ...
            ValueError: need more than 1 value to unpack for edge: (0,)
            sage: G.subdivide_edges([(0, 1, 2, 4), (0, 1, 'label')], 4)
            Traceback (most recent call last):
            ...
            ValueError: too many values to unpack (expected 2) for edge: (0, 1, 2, 4)
            sage: G.subdivide_edges([0, (0, 1, 'label')], 4)
            Traceback (most recent call last):
            ...
            TypeError: input edge 0 is of unknown type

        .. SEEALSO::

            - :meth:`~sage.graphs.matching_covered_graph.MatchingCoveredGraph.subdivide_edge`
        """
    def update_matching(self, matching) -> None:
        """
        Update the perfect matching captured in ``self._matching``.

        INPUT:

        - ``matching`` -- a perfect matching of the graph, that can be given
          using any valid input format of :class:`~sage.graphs.graph.Graph`.

        OUTPUT:

        - If ``matching`` is a valid perfect matching of the graph, then
          ``self._matching`` gets updated to this provided matching, or
          otherwise an exception is returned without any alterations to
          ``self._matching``.

        EXAMPLES:

        Providing with a valid perfect matching of the graph::

            sage: P = graphs.PetersenGraph()
            sage: G = MatchingCoveredGraph(P)
            sage: sorted(G.get_matching())
            [(0, 5, None), (1, 6, None), (2, 7, None), (3, 8, None), (4, 9, None)]
            sage: M = [(0, 1), (2, 3), (4, 9), (5, 7), (6, 8)]
            sage: G.update_matching(M)
            sage: sorted(G.get_matching())
            [(0, 1, None), (2, 3, None), (4, 9, None), (5, 7, None), (6, 8, None)]

        TESTS:

        Providing with a wrong matching::

            sage: P = graphs.PetersenGraph()
            sage: G = MatchingCoveredGraph(P)
            sage: sorted(G.get_matching())
            [(0, 5, None), (1, 6, None), (2, 7, None), (3, 8, None), (4, 9, None)]
            sage: S = str('0')
            sage: G.update_matching(S)
            Traceback (most recent call last):
            ...
            RuntimeError: the string seems corrupt: valid characters are
            ?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~
            sage: T = str('graph')
            sage: G.update_matching(T)
            Traceback (most recent call last):
            ...
            RuntimeError: the string (graph) seems corrupt: for n = 40,
                the string is too short
            sage: M = Graph(G.matching())
            sage: M.add_edges([(0, 1), (0, 2)])
            sage: G.update_matching(M)
            Traceback (most recent call last):
            ...
            ValueError: the input is not a matching
            sage: N = Graph(G.matching())
            sage: N.add_edge(10, 11)
            sage: G.update_matching(N)
            Traceback (most recent call last):
            ...
            ValueError: the input is not a matching of the graph
            sage: J = Graph()
            sage: J.add_edges([(0, 1), (2, 3)])
            sage: G.update_matching(J)
            Traceback (most recent call last):
            ...
            ValueError: the input is not a perfect matching of the graph
        """

__doc__: Incomplete
