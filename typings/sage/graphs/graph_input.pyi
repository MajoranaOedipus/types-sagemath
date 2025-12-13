from _typeshed import Incomplete
from sage.cpython.string import bytes_to_str as bytes_to_str
from sage.misc.rest_index_of_methods import gen_rest_table_index as gen_rest_table_index

def from_graph6(G, g6_string) -> None:
    """
    Fill ``G`` with the data of a graph6 string.

    INPUT:

    - ``G`` -- a graph

    - ``g6_string`` -- a graph6 string

    EXAMPLES::

        sage: from sage.graphs.graph_input import from_graph6
        sage: g = Graph()
        sage: from_graph6(g, 'IheA@GUAo')
        sage: g.is_isomorphic(graphs.PetersenGraph())
        True
    """
def from_sparse6(G, g6_string) -> None:
    """
    Fill ``G`` with the data of a sparse6 string.

    INPUT:

    - ``G`` -- a graph

    - ``g6_string`` -- a sparse6 string

    EXAMPLES::

        sage: from sage.graphs.graph_input import from_sparse6
        sage: g = Graph()
        sage: from_sparse6(g, ':I`ES@obGkqegW~')
        sage: g.is_isomorphic(graphs.PetersenGraph())
        True
    """
def from_dig6(G, dig6_string) -> None:
    """
    Fill ``G`` with the data of a dig6 string.

    INPUT:

    - ``G`` -- a graph

    - ``dig6_string`` -- a dig6 string

    EXAMPLES::

        sage: from sage.graphs.graph_input import from_dig6
        sage: g = DiGraph()
        sage: from_dig6(g, digraphs.Circuit(10).dig6_string())
        sage: g.is_isomorphic(digraphs.Circuit(10))
        True

    The string may represent a directed graph with loops::

        sage: L = DiGraph(loops=True)
        sage: from_dig6(L, 'CW`C')
        sage: L.edges(labels=False, sort=True)
        [(0, 1), (0, 2), (1, 2), (2, 3), (3, 3)]
    """
def from_seidel_adjacency_matrix(G, M) -> None:
    """
    Fill ``G`` with the data of a Seidel adjacency matrix.

    INPUT:

    - ``G`` -- a graph

    - ``M`` -- a Seidel adjacency matrix

    EXAMPLES::

        sage: from sage.graphs.graph_input import from_seidel_adjacency_matrix
        sage: g = Graph()
        sage: sam = graphs.PetersenGraph().seidel_adjacency_matrix()                    # needs sage.modules
        sage: from_seidel_adjacency_matrix(g, sam)                                      # needs sage.modules
        sage: g.is_isomorphic(graphs.PetersenGraph())                                   # needs sage.modules
        True
    """
def from_adjacency_matrix(G, M, loops: bool = False, multiedges: bool = False, weighted: bool = False) -> None:
    """
    Fill ``G`` with the data of an adjacency matrix.

    INPUT:

    - ``G`` -- a :class:`Graph` or :class:`DiGraph`

    - ``M`` -- an adjacency matrix

    - ``loops``, ``multiedges``, ``weighted`` -- booleans (default: ``False``);
      whether to consider the graph as having loops, multiple edges, or weights

    EXAMPLES::

        sage: from sage.graphs.graph_input import from_adjacency_matrix
        sage: g = Graph()
        sage: from_adjacency_matrix(g, graphs.PetersenGraph().adjacency_matrix())       # needs sage.modules
        sage: g.is_isomorphic(graphs.PetersenGraph())                                   # needs sage.modules
        True
    """
def from_incidence_matrix(G, M, loops: bool = False, multiedges: bool = False, weighted: bool = False) -> None:
    """
    Fill ``G`` with the data of an incidence matrix.

    INPUT:

    - ``G`` -- a graph

    - ``M`` -- an incidence matrix

    - ``loops``, ``multiedges``, ``weighted`` -- booleans (default: ``False``);
      whether to consider the graph as having loops, multiple edges, or weights

    EXAMPLES::

        sage: from sage.graphs.graph_input import from_incidence_matrix
        sage: g = Graph()
        sage: from_incidence_matrix(g, graphs.PetersenGraph().incidence_matrix())       # needs sage.modules
        sage: g.is_isomorphic(graphs.PetersenGraph())                                   # needs sage.modules
        True
    """
def from_oriented_incidence_matrix(G, M, loops: bool = False, multiedges: bool = False, weighted: bool = False) -> None:
    """
    Fill ``G`` with the data of an *oriented* incidence matrix.

    An oriented incidence matrix is the incidence matrix of a directed graph, in
    which each non-loop edge corresponds to a `+1` and a `-1`, indicating its
    source and destination.

    INPUT:

    - ``G`` -- a :class:`DiGraph`

    - ``M`` -- an incidence matrix

    - ``loops``, ``multiedges``, ``weighted`` -- booleans (default: ``False``);
      whether to consider the graph as having loops, multiple edges, or weights

    .. NOTE:: ``weighted`` is currently ignored.

    EXAMPLES::

        sage: from sage.graphs.graph_input import from_oriented_incidence_matrix
        sage: g = DiGraph()
        sage: im = digraphs.Circuit(10).incidence_matrix()                              # needs sage.modules
        sage: from_oriented_incidence_matrix(g, im)                                     # needs sage.modules
        sage: g.is_isomorphic(digraphs.Circuit(10))                                     # needs sage.modules
        True

    TESTS:

    Fix bug reported in :issue:`22985`::

        sage: DiGraph(matrix ([[1,0,0,1],[0,0,1,1],[0,0,1,1]]).transpose())             # needs sage.modules
        Traceback (most recent call last):
        ...
        ValueError: each column represents an edge: -1 goes to 1

    Handle incidence matrix containing a column with only zeros (:issue:`29275`)::

        sage: m = Matrix([[0,1],[0,-1],[0,0]]); m                                       # needs sage.modules
        [ 0  1]
        [ 0 -1]
        [ 0  0]
        sage: G = DiGraph(m, format='incidence_matrix')                                 # needs sage.modules
        sage: list(G.edges(sort=True, labels=False))                                    # needs sage.modules
        [(1, 0)]

    Handle incidence matrix [[1],[-1]] (:issue:`29275`)::

        sage: m = Matrix([[1],[-1]]); m                                                 # needs sage.modules
        [ 1]
        [-1]
        sage: G = DiGraph(m, format='incidence_matrix')                                 # needs sage.modules
        sage: list(G.edges(sort=True, labels=False))                                    # needs sage.modules
        [(1, 0)]
    """
def from_dict_of_dicts(G, M, loops: bool = False, multiedges: bool = False, weighted: bool = False, convert_empty_dict_labels_to_None: bool = False):
    """
    Fill ``G`` with the data of a dictionary of dictionaries.

    INPUT:

    - ``G`` -- a graph

    - ``M`` -- dictionary of dictionaries

    - ``loops``, ``multiedges``, ``weighted`` -- booleans (default: ``False``);
      whether to consider the graph as having loops, multiple edges, or weights

    - ``convert_empty_dict_labels_to_None`` -- booleans (default: ``False``);
      whether to adjust for empty dicts instead of ``None`` in NetworkX default
      edge labels

    EXAMPLES::

        sage: from sage.graphs.graph_input import from_dict_of_dicts
        sage: g = Graph()
        sage: from_dict_of_dicts(g, graphs.PetersenGraph().to_dictionary(edge_labels=True))
        sage: g.is_isomorphic(graphs.PetersenGraph())
        True

    The resulting order of vertices is unspecified but deterministic::

        sage: from sage.graphs.graph_input import from_dict_of_dicts
        sage: g = Graph()
        sage: from_dict_of_dicts(g, {i: {} for i in range(99, 90, -1)})
        sage: g.vertices(sort=False)
        [99, 98, 97, 96, 95, 94, 93, 92, 91]

    TESTS:

    :issue:`32831` is fixed::

        sage: DiGraph({0: {}, 1: {}, 2: {}, 3: {}, 4: {}})
        Digraph on 5 vertices
    """
def from_dict_of_lists(G, D, loops: bool = False, multiedges: bool = False, weighted: bool = False) -> None:
    """
    Fill ``G`` with the data of a dictionary of lists.

    INPUT:

    - ``G`` -- a :class:`Graph` or :class:`DiGraph`

    - ``D`` -- dictionary of lists

    - ``loops``, ``multiedges``, ``weighted`` -- booleans (default: ``False``);
      whether to consider the graph as having loops, multiple edges, or weights

    EXAMPLES::

        sage: from sage.graphs.graph_input import from_dict_of_lists
        sage: g = Graph()
        sage: from_dict_of_lists(g, graphs.PetersenGraph().to_dictionary())
        sage: g.is_isomorphic(graphs.PetersenGraph())
        True

    The resulting order of vertices is unspecified but deterministic::

        sage: from sage.graphs.graph_input import from_dict_of_lists
        sage: g = Graph()
        sage: from_dict_of_lists(g, {i: [] for i in range(99, 90, -1)})
        sage: g.vertices(sort=False)
        [99, 98, 97, 96, 95, 94, 93, 92, 91]
    """
def from_networkx_graph(G, gnx, weighted=None, loops=None, multiedges=None, convert_empty_dict_labels_to_None=None):
    '''
    Fill `G` with the data of a NetworkX (di)graph.

    INPUT:

    - ``G`` -- a :class:`Graph` or :class:`DiGraph`

    - ``gnx`` -- a NetworkX ``Graph``, ``MultiGraph``, ``DiGraph`` or
      ``MultiDiGraph``

    - ``weighted`` -- boolean (default: ``None``); whether graph thinks of
      itself as weighted or not. See
      :meth:`~sage.graphs.generic_graph.GenericGraph.weighted`.

    - ``loops`` -- boolean (default: ``None``); whether to allow loops

    - ``multiedges`` -- boolean (default: ``None``); whether to allow multiple
      edges

    - ``convert_empty_dict_labels_to_None`` -- boolean (default: ``None``);
      whether to replace the default edge labels used by NetworkX (empty
      dictionaries) by ``None``, the default Sage edge label. When set to
      ``False``, empty dictionaries are not converted to ``None``.

    EXAMPLES:

    Feeding a :class:`Graph` with a NetworkX ``Graph``::

        sage: # needs networkx
        sage: from sage.graphs.graph_input import from_networkx_graph
        sage: import networkx
        sage: G = Graph()
        sage: _ = gnx = networkx.Graph()
        sage: _ = gnx.add_edge(0, 1)
        sage: _ = gnx.add_edge(1, 2)
        sage: from_networkx_graph(G, gnx)
        sage: G.edges(sort=True, labels=False)
        [(0, 1), (1, 2)]

    Feeding a :class:`Graph` with a NetworkX ``MultiGraph``::

        sage: # needs networkx
        sage: G = Graph()
        sage: gnx = networkx.MultiGraph()
        sage: _ = gnx.add_edge(0, 1)
        sage: _ = gnx.add_edge(0, 1)
        sage: from_networkx_graph(G, gnx)
        sage: G.edges(sort=True, labels=False)
        [(0, 1), (0, 1)]
        sage: G = Graph()
        sage: from_networkx_graph(G, gnx, multiedges=False)
        sage: G.edges(sort=True, labels=False)
        [(0, 1)]

    When feeding a :class:`Graph` `G` with a NetworkX ``DiGraph`` `D`, `G` has
    one edge `(u, v)` whenever `D` has arc `(u, v)` or `(v, u)` or both::

        sage: # needs networkx
        sage: G = Graph()
        sage: D = networkx.DiGraph()
        sage: _ = D.add_edge(0, 1)
        sage: from_networkx_graph(G, D)
        sage: G.edges(sort=True, labels=False)
        [(0, 1)]
        sage: G = Graph()
        sage: _ = D.add_edge(1, 0)
        sage: from_networkx_graph(G, D)
        sage: G.edges(sort=True, labels=False)
        [(0, 1)]

    When feeding a :class:`Graph` `G` with a NetworkX ``MultiDiGraph`` `D`, the
    number of edges between `u` and `v` in `G` is the maximum between the number
    of arcs `(u, v)` and the number of arcs `(v, u)` in D`::

        sage: # needs networkx
        sage: G = Graph()
        sage: D = networkx.MultiDiGraph()
        sage: _ = D.add_edge(0, 1)
        sage: _ = D.add_edge(1, 0)
        sage: _ = D.add_edge(1, 0)
        sage: D.edges()
        OutMultiEdgeDataView([(0, 1), (1, 0), (1, 0)])
        sage: from_networkx_graph(G, D)
        sage: G.edges(sort=True, labels=False)
        [(0, 1), (0, 1)]

    Feeding a :class:`DiGraph` with a NetworkX ``DiGraph``::

        sage: # needs networkx
        sage: from sage.graphs.graph_input import from_networkx_graph
        sage: import networkx
        sage: G = DiGraph()
        sage: _ = gnx = networkx.DiGraph()
        sage: _ = gnx.add_edge(0, 1)
        sage: _ = gnx.add_edge(1, 2)
        sage: from_networkx_graph(G, gnx)
        sage: G.edges(sort=True, labels=False)
        [(0, 1), (1, 2)]

    Feeding a :class:`DiGraph` with a NetworkX ``MultiDiGraph``::

        sage: # needs networkx
        sage: G = DiGraph()
        sage: gnx = networkx.MultiDiGraph()
        sage: _ = gnx.add_edge(0, 1)
        sage: _ = gnx.add_edge(0, 1)
        sage: from_networkx_graph(G, gnx)
        sage: G.edges(sort=True, labels=False)
        [(0, 1), (0, 1)]
        sage: G = DiGraph()
        sage: from_networkx_graph(G, gnx, multiedges=False)
        sage: G.edges(sort=True, labels=False)
        [(0, 1)]

    When feeding a :class:`DiGraph` `G` with a NetworkX ``Graph`` `H`, `G` has
    both arcs `(u, v)` and `(v, u)` if `G` has edge `(u, v)`::

        sage: # needs networkx
        sage: G = DiGraph()
        sage: H = networkx.Graph()
        sage: _ = H.add_edge(0, 1)
        sage: from_networkx_graph(G, H)
        sage: G.edges(labels=False, sort=True)
        [(0, 1), (1, 0)]

    When feeding a :class:`DiGraph` `G` with a NetworkX ``MultiGraph`` `H`, `G`
    has `k` arcs `(u, v)` and `k` arcs `(v, u)` if `H` has `k` edges `(u, v)`,
    unless parameter ``multiedges`` is set to ``False``::

        sage: # needs networkx
        sage: G = DiGraph()
        sage: H = networkx.MultiGraph()
        sage: _ = H.add_edge(0, 1)
        sage: _ = H.add_edge(0, 1)
        sage: _ = H.add_edge(0, 1)
        sage: H.edges()
        MultiEdgeDataView([(0, 1), (0, 1), (0, 1)])
        sage: from_networkx_graph(G, H)
        sage: G.edges(labels=False, sort=True)
        [(0, 1), (0, 1), (0, 1), (1, 0), (1, 0), (1, 0)]
        sage: G = DiGraph()
        sage: from_networkx_graph(G, H, multiedges=False)
        sage: G.edges(labels=False, sort=True)
        [(0, 1), (1, 0)]

    TESTS:

    The first parameter must be a :class:`Graph` or :class:`DiGraph`::

        sage: from sage.graphs.graph_input import from_networkx_graph
        sage: from_networkx_graph("foo", "bar")
        Traceback (most recent call last):
        ...
        ValueError: the first parameter must a Sage Graph or DiGraph

    The second parameter must be a NetworkX ``Graph``, ``MultiGraph``,
      ``DiGraph`` or ``MultiDiGraph``::

        sage: from sage.graphs.graph_input import from_networkx_graph
        sage: from_networkx_graph(Graph(), "bar")                                       # needs networkx
        Traceback (most recent call last):
        ...
        ValueError: the second parameter must be a NetworkX (Multi)(Di)Graph
    '''

__doc__: Incomplete
