import _cython_3_2_1
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from typing import Any, ClassVar, overload

biconnected_components_subgraphs: _cython_3_2_1.cython_function_or_method
blocks_and_cut_vertices: _cython_3_2_1.cython_function_or_method
blocks_and_cuts_tree: _cython_3_2_1.cython_function_or_method
bridges: _cython_3_2_1.cython_function_or_method
cleave: _cython_3_2_1.cython_function_or_method
connected_component_containing_vertex: _cython_3_2_1.cython_function_or_method
connected_components: _cython_3_2_1.cython_function_or_method
connected_components_number: _cython_3_2_1.cython_function_or_method
connected_components_sizes: _cython_3_2_1.cython_function_or_method
connected_components_subgraphs: _cython_3_2_1.cython_function_or_method
edge_connectivity: _cython_3_2_1.cython_function_or_method
is_connected: _cython_3_2_1.cython_function_or_method
is_cut_edge: _cython_3_2_1.cython_function_or_method
is_cut_vertex: _cython_3_2_1.cython_function_or_method
is_edge_cut: _cython_3_2_1.cython_function_or_method
is_strongly_connected: _cython_3_2_1.cython_function_or_method
is_triconnected: _cython_3_2_1.cython_function_or_method
is_vertex_cut: _cython_3_2_1.cython_function_or_method
minimal_separators: _cython_3_2_1.cython_function_or_method
spqr_tree: _cython_3_2_1.cython_function_or_method
spqr_tree_to_graph: _cython_3_2_1.cython_function_or_method
strong_articulation_points: _cython_3_2_1.cython_function_or_method
strongly_connected_component_containing_vertex: _cython_3_2_1.cython_function_or_method
strongly_connected_components_digraph: _cython_3_2_1.cython_function_or_method
strongly_connected_components_subgraphs: _cython_3_2_1.cython_function_or_method
vertex_connectivity: _cython_3_2_1.cython_function_or_method

class TriconnectivitySPQR:
    """TriconnectivitySPQR(G, check=True)

    File: /build/sagemath/src/sage/src/sage/graphs/connectivity.pyx (starting at line 3325)

    Decompose a graph into triconnected components and build SPQR-tree.

    This class implements the algorithm proposed by Hopcroft and Tarjan in
    [Hopcroft1973]_, and later corrected by Gutwenger and Mutzel in [Gut2001]_,
    for finding the triconnected components of a biconnected graph. It then
    organizes these components into a SPQR-tree. See the:wikipedia:`SPQR_tree`.

    A SPQR-tree is a tree data structure used to represent the triconnected
    components of a biconnected (multi)graph and the 2-vertex cuts separating
    them. A node of a SPQR-tree, and the graph associated with it, can be one of
    the following four types:

    - ``'S'`` -- the associated graph is a cycle with at least three vertices
      ``'S'`` stands for ``series`` and is also called a ``polygon``

    - ``'P'`` -- the associated graph is a dipole graph, a multigraph with two
      vertices and three or more edges. ``'P'`` stands for ``parallel`` and the
      node is called a ``bond``.

    - ``'Q'`` -- the associated graph has a single real edge. This trivial case
      is necessary to handle the graph that has only one edge.

    - ``'R'`` -- the associated graph is a 3-vertex-connected graph that is not
      a cycle or dipole. ``'R'`` stands for ``rigid``.

    The edges of the tree indicate the 2-vertex cuts of the graph.

    INPUT:

    - ``G`` -- graph; if ``G`` is a :class:`DiGraph`, the computation is done on
      the underlying :class:`Graph` (i.e., ignoring edge orientation)

    - ``check`` -- boolean (default: ``True``); indicates whether ``G`` needs to
      be tested for biconnectivity

    .. SEEALSO::

        - :meth:`sage.graphs.connectivity.spqr_tree`
        - :meth:`~Graph.is_biconnected`
        - :wikipedia:`SPQR_tree`

    EXAMPLES:

    Example from the :wikipedia:`SPQR_tree`::

        sage: from sage.graphs.connectivity import TriconnectivitySPQR
        sage: from sage.graphs.connectivity import spqr_tree_to_graph
        sage: G = Graph([(1, 2), (1, 4), (1, 8), (1, 12), (3, 4), (2, 3),
        ....: (2, 13), (3, 13), (4, 5), (4, 7), (5, 6), (5, 8), (5, 7), (6, 7),
        ....: (8, 11), (8, 9), (8, 12), (9, 10), (9, 11), (9, 12), (10, 12)])
        sage: tric = TriconnectivitySPQR(G)
        sage: T = tric.get_spqr_tree()
        sage: G.is_isomorphic(spqr_tree_to_graph(T))
        True

    An example from [Hopcroft1973]_::

        sage: G = Graph([(1, 2), (1, 4), (1, 8), (1, 12), (1, 13), (2, 3),
        ....: (2, 13), (3, 4), (3, 13), (4, 5), (4, 7), (5, 6), (5, 7), (5, 8),
        ....: (6, 7), (8, 9), (8, 11), (8, 12), (9, 10), (9, 11), (9, 12),
        ....: (10, 11), (10, 12)])
        sage: tric = TriconnectivitySPQR(G)
        sage: T = tric.get_spqr_tree()
        sage: G.is_isomorphic(spqr_tree_to_graph(T))
        True
        sage: tric.print_triconnected_components()
        Triconnected: [(8, 9, None), (9, 12, None), (9, 11, None), (8, 11, None), (10, 11, None), (9, 10, None), (10, 12, None), (8, 12, 'newVEdge0')]
        Bond: [(8, 12, None), (8, 12, 'newVEdge0'), (8, 12, 'newVEdge1')]
        Polygon: [(6, 7, None), (5, 6, None), (7, 5, 'newVEdge2')]
        Bond: [(7, 5, 'newVEdge2'), (5, 7, 'newVEdge3'), (5, 7, None)]
        Polygon: [(5, 7, 'newVEdge3'), (4, 7, None), (5, 4, 'newVEdge4')]
        Bond: [(5, 4, 'newVEdge4'), (4, 5, 'newVEdge5'), (4, 5, None)]
        Polygon: [(4, 5, 'newVEdge5'), (5, 8, None), (1, 4, 'newVEdge9'), (1, 8, 'newVEdge10')]
        Triconnected: [(1, 2, None), (2, 13, None), (1, 13, None), (3, 13, None), (2, 3, None), (1, 3, 'newVEdge7')]
        Polygon: [(1, 3, 'newVEdge7'), (3, 4, None), (1, 4, 'newVEdge8')]
        Bond: [(1, 4, None), (1, 4, 'newVEdge8'), (1, 4, 'newVEdge9')]
        Bond: [(1, 8, None), (1, 8, 'newVEdge10'), (1, 8, 'newVEdge11')]
        Polygon: [(8, 12, 'newVEdge1'), (1, 8, 'newVEdge11'), (1, 12, None)]

    An example from [Gut2001]_::

        sage: G = Graph([(1, 2), (1, 4), (2, 3), (2, 5), (3, 4), (3, 5), (4, 5),
        ....: (4, 6), (5, 7), (5, 8), (5, 14), (6, 8), (7, 14), (8, 9), (8, 10),
        ....: (8, 11), (8, 12), (9, 10), (10, 13), (10, 14), (10, 15), (10, 16),
        ....: (11, 12), (11, 13), (12, 13), (14, 15), (14, 16), (15, 16)])
        sage: T = TriconnectivitySPQR(G).get_spqr_tree()
        sage: G.is_isomorphic(spqr_tree_to_graph(T))
        True

    An example with multi-edges and accessing the triconnected components::

        sage: G = Graph([(1, 2), (1, 5), (1, 5), (2, 3), (2, 3), (3, 4), (4, 5)], multiedges=True)
        sage: tric = TriconnectivitySPQR(G)
        sage: T = tric.get_spqr_tree()
        sage: G.is_isomorphic(spqr_tree_to_graph(T))
        True
        sage: tric.print_triconnected_components()
        Bond:  [(1, 5, None), (1, 5, None), (1, 5, 'newVEdge0')]
        Bond:  [(2, 3, None), (2, 3, None), (2, 3, 'newVEdge1')]
        Polygon:  [(4, 5, None), (1, 5, 'newVEdge0'), (3, 4, None), (2, 3, 'newVEdge1'), (1, 2, None)]

    An example of a triconnected graph::

        sage: G = Graph([('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd'), ('c', 'd')])
        sage: T = TriconnectivitySPQR(G).get_spqr_tree()
        sage: print(T.vertices(sort=True))
        [('R', Multi-graph on 4 vertices)]
        sage: G.is_isomorphic(spqr_tree_to_graph(T))
        True

    An example of a directed graph with multi-edges::

        sage: G = DiGraph([(1, 2), (2, 3), (3, 4), (4, 5), (1, 5), (5, 1)])
        sage: tric = TriconnectivitySPQR(G)
        sage: tric.print_triconnected_components()
        Bond:  [(1, 5, None), (5, 1, None), (1, 5, 'newVEdge0')]
        Polygon:  [(4, 5, None), (1, 5, 'newVEdge0'), (3, 4, None), (2, 3, None), (1, 2, None)]

    Edge labels are preserved by the construction::

        sage: G = Graph([(0, 1, '01'), (0, 4, '04'), (1, 2, '12'), (1, 5, '15'),
        ....: (2, 3, '23'), (2, 6, '26'), (3, 7, '37'), (4, 5, '45'),
        ....: (5, 6, '56'), (6, 7, 67)])
        sage: T = TriconnectivitySPQR(G).get_spqr_tree()
        sage: H = spqr_tree_to_graph(T)
        sage: all(G.has_edge(e) for e in H.edge_iterator())
        True
        sage: all(H.has_edge(e) for e in G.edge_iterator())
        True

    TESTS:

    A disconnected graph::

        sage: from sage.graphs.connectivity import TriconnectivitySPQR
        sage: G = Graph([(1,2),(3,5)])
        sage: tric = TriconnectivitySPQR(G)
        Traceback (most recent call last):
        ...
        ValueError: graph is not connected

    A graph with a cut vertex::

        sage: from sage.graphs.connectivity import TriconnectivitySPQR
        sage: G = Graph([(1,2),(1,3),(2,3),(3,4),(3,5),(4,5)])
        sage: tric = TriconnectivitySPQR(G)
        Traceback (most recent call last):
        ...
        ValueError: graph has a cut vertex"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @overload
    def __init__(self, G, check=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/graphs/connectivity.pyx (starting at line 3477)

                Initialize this object, decompose the graph and build SPQR-tree.

                INPUT:

                - ``G`` -- graph; if ``G`` is a :class:`DiGraph`, the computation is
                  done on the underlying :class:`Graph` (i.e., ignoring edge
                  orientation)

                - ``check`` -- boolean (default: ``True``); indicates whether ``G``
                  needs to be tested for biconnectivity

                EXAMPLES:

                Example from the :wikipedia:`SPQR_tree`::

                    sage: from sage.graphs.connectivity import TriconnectivitySPQR
                    sage: from sage.graphs.connectivity import spqr_tree_to_graph
                    sage: G = Graph([(1, 2), (1, 4), (1, 8), (1, 12), (3, 4), (2, 3),
                    ....: (2, 13), (3, 13), (4, 5), (4, 7), (5, 6), (5, 8), (5, 7), (6, 7),
                    ....: (8, 11), (8, 9), (8, 12), (9, 10), (9, 11), (9, 12), (10, 12)])
                    sage: tric = TriconnectivitySPQR(G)
                    sage: T = tric.get_spqr_tree()
                    sage: G.is_isomorphic(spqr_tree_to_graph(T))
                    True
        """
    @overload
    def __init__(self, G) -> Any:
        """File: /build/sagemath/src/sage/src/sage/graphs/connectivity.pyx (starting at line 3477)

                Initialize this object, decompose the graph and build SPQR-tree.

                INPUT:

                - ``G`` -- graph; if ``G`` is a :class:`DiGraph`, the computation is
                  done on the underlying :class:`Graph` (i.e., ignoring edge
                  orientation)

                - ``check`` -- boolean (default: ``True``); indicates whether ``G``
                  needs to be tested for biconnectivity

                EXAMPLES:

                Example from the :wikipedia:`SPQR_tree`::

                    sage: from sage.graphs.connectivity import TriconnectivitySPQR
                    sage: from sage.graphs.connectivity import spqr_tree_to_graph
                    sage: G = Graph([(1, 2), (1, 4), (1, 8), (1, 12), (3, 4), (2, 3),
                    ....: (2, 13), (3, 13), (4, 5), (4, 7), (5, 6), (5, 8), (5, 7), (6, 7),
                    ....: (8, 11), (8, 9), (8, 12), (9, 10), (9, 11), (9, 12), (10, 12)])
                    sage: tric = TriconnectivitySPQR(G)
                    sage: T = tric.get_spqr_tree()
                    sage: G.is_isomorphic(spqr_tree_to_graph(T))
                    True
        """
    @overload
    def __init__(self, G) -> Any:
        """File: /build/sagemath/src/sage/src/sage/graphs/connectivity.pyx (starting at line 3477)

                Initialize this object, decompose the graph and build SPQR-tree.

                INPUT:

                - ``G`` -- graph; if ``G`` is a :class:`DiGraph`, the computation is
                  done on the underlying :class:`Graph` (i.e., ignoring edge
                  orientation)

                - ``check`` -- boolean (default: ``True``); indicates whether ``G``
                  needs to be tested for biconnectivity

                EXAMPLES:

                Example from the :wikipedia:`SPQR_tree`::

                    sage: from sage.graphs.connectivity import TriconnectivitySPQR
                    sage: from sage.graphs.connectivity import spqr_tree_to_graph
                    sage: G = Graph([(1, 2), (1, 4), (1, 8), (1, 12), (3, 4), (2, 3),
                    ....: (2, 13), (3, 13), (4, 5), (4, 7), (5, 6), (5, 8), (5, 7), (6, 7),
                    ....: (8, 11), (8, 9), (8, 12), (9, 10), (9, 11), (9, 12), (10, 12)])
                    sage: tric = TriconnectivitySPQR(G)
                    sage: T = tric.get_spqr_tree()
                    sage: G.is_isomorphic(spqr_tree_to_graph(T))
                    True
        """
    @overload
    def __init__(self, G) -> Any:
        """File: /build/sagemath/src/sage/src/sage/graphs/connectivity.pyx (starting at line 3477)

                Initialize this object, decompose the graph and build SPQR-tree.

                INPUT:

                - ``G`` -- graph; if ``G`` is a :class:`DiGraph`, the computation is
                  done on the underlying :class:`Graph` (i.e., ignoring edge
                  orientation)

                - ``check`` -- boolean (default: ``True``); indicates whether ``G``
                  needs to be tested for biconnectivity

                EXAMPLES:

                Example from the :wikipedia:`SPQR_tree`::

                    sage: from sage.graphs.connectivity import TriconnectivitySPQR
                    sage: from sage.graphs.connectivity import spqr_tree_to_graph
                    sage: G = Graph([(1, 2), (1, 4), (1, 8), (1, 12), (3, 4), (2, 3),
                    ....: (2, 13), (3, 13), (4, 5), (4, 7), (5, 6), (5, 8), (5, 7), (6, 7),
                    ....: (8, 11), (8, 9), (8, 12), (9, 10), (9, 11), (9, 12), (10, 12)])
                    sage: tric = TriconnectivitySPQR(G)
                    sage: T = tric.get_spqr_tree()
                    sage: G.is_isomorphic(spqr_tree_to_graph(T))
                    True
        """
    @overload
    def __init__(self, G) -> Any:
        """File: /build/sagemath/src/sage/src/sage/graphs/connectivity.pyx (starting at line 3477)

                Initialize this object, decompose the graph and build SPQR-tree.

                INPUT:

                - ``G`` -- graph; if ``G`` is a :class:`DiGraph`, the computation is
                  done on the underlying :class:`Graph` (i.e., ignoring edge
                  orientation)

                - ``check`` -- boolean (default: ``True``); indicates whether ``G``
                  needs to be tested for biconnectivity

                EXAMPLES:

                Example from the :wikipedia:`SPQR_tree`::

                    sage: from sage.graphs.connectivity import TriconnectivitySPQR
                    sage: from sage.graphs.connectivity import spqr_tree_to_graph
                    sage: G = Graph([(1, 2), (1, 4), (1, 8), (1, 12), (3, 4), (2, 3),
                    ....: (2, 13), (3, 13), (4, 5), (4, 7), (5, 6), (5, 8), (5, 7), (6, 7),
                    ....: (8, 11), (8, 9), (8, 12), (9, 10), (9, 11), (9, 12), (10, 12)])
                    sage: tric = TriconnectivitySPQR(G)
                    sage: T = tric.get_spqr_tree()
                    sage: G.is_isomorphic(spqr_tree_to_graph(T))
                    True
        """
    @overload
    def __init__(self, G) -> Any:
        """File: /build/sagemath/src/sage/src/sage/graphs/connectivity.pyx (starting at line 3477)

                Initialize this object, decompose the graph and build SPQR-tree.

                INPUT:

                - ``G`` -- graph; if ``G`` is a :class:`DiGraph`, the computation is
                  done on the underlying :class:`Graph` (i.e., ignoring edge
                  orientation)

                - ``check`` -- boolean (default: ``True``); indicates whether ``G``
                  needs to be tested for biconnectivity

                EXAMPLES:

                Example from the :wikipedia:`SPQR_tree`::

                    sage: from sage.graphs.connectivity import TriconnectivitySPQR
                    sage: from sage.graphs.connectivity import spqr_tree_to_graph
                    sage: G = Graph([(1, 2), (1, 4), (1, 8), (1, 12), (3, 4), (2, 3),
                    ....: (2, 13), (3, 13), (4, 5), (4, 7), (5, 6), (5, 8), (5, 7), (6, 7),
                    ....: (8, 11), (8, 9), (8, 12), (9, 10), (9, 11), (9, 12), (10, 12)])
                    sage: tric = TriconnectivitySPQR(G)
                    sage: T = tric.get_spqr_tree()
                    sage: G.is_isomorphic(spqr_tree_to_graph(T))
                    True
        """
    @overload
    def __init__(self, G) -> Any:
        """File: /build/sagemath/src/sage/src/sage/graphs/connectivity.pyx (starting at line 3477)

                Initialize this object, decompose the graph and build SPQR-tree.

                INPUT:

                - ``G`` -- graph; if ``G`` is a :class:`DiGraph`, the computation is
                  done on the underlying :class:`Graph` (i.e., ignoring edge
                  orientation)

                - ``check`` -- boolean (default: ``True``); indicates whether ``G``
                  needs to be tested for biconnectivity

                EXAMPLES:

                Example from the :wikipedia:`SPQR_tree`::

                    sage: from sage.graphs.connectivity import TriconnectivitySPQR
                    sage: from sage.graphs.connectivity import spqr_tree_to_graph
                    sage: G = Graph([(1, 2), (1, 4), (1, 8), (1, 12), (3, 4), (2, 3),
                    ....: (2, 13), (3, 13), (4, 5), (4, 7), (5, 6), (5, 8), (5, 7), (6, 7),
                    ....: (8, 11), (8, 9), (8, 12), (9, 10), (9, 11), (9, 12), (10, 12)])
                    sage: tric = TriconnectivitySPQR(G)
                    sage: T = tric.get_spqr_tree()
                    sage: G.is_isomorphic(spqr_tree_to_graph(T))
                    True
        """
    @overload
    def __init__(self, G) -> Any:
        """File: /build/sagemath/src/sage/src/sage/graphs/connectivity.pyx (starting at line 3477)

                Initialize this object, decompose the graph and build SPQR-tree.

                INPUT:

                - ``G`` -- graph; if ``G`` is a :class:`DiGraph`, the computation is
                  done on the underlying :class:`Graph` (i.e., ignoring edge
                  orientation)

                - ``check`` -- boolean (default: ``True``); indicates whether ``G``
                  needs to be tested for biconnectivity

                EXAMPLES:

                Example from the :wikipedia:`SPQR_tree`::

                    sage: from sage.graphs.connectivity import TriconnectivitySPQR
                    sage: from sage.graphs.connectivity import spqr_tree_to_graph
                    sage: G = Graph([(1, 2), (1, 4), (1, 8), (1, 12), (3, 4), (2, 3),
                    ....: (2, 13), (3, 13), (4, 5), (4, 7), (5, 6), (5, 8), (5, 7), (6, 7),
                    ....: (8, 11), (8, 9), (8, 12), (9, 10), (9, 11), (9, 12), (10, 12)])
                    sage: tric = TriconnectivitySPQR(G)
                    sage: T = tric.get_spqr_tree()
                    sage: G.is_isomorphic(spqr_tree_to_graph(T))
                    True
        """
    @overload
    def __init__(self, G) -> Any:
        """File: /build/sagemath/src/sage/src/sage/graphs/connectivity.pyx (starting at line 3477)

                Initialize this object, decompose the graph and build SPQR-tree.

                INPUT:

                - ``G`` -- graph; if ``G`` is a :class:`DiGraph`, the computation is
                  done on the underlying :class:`Graph` (i.e., ignoring edge
                  orientation)

                - ``check`` -- boolean (default: ``True``); indicates whether ``G``
                  needs to be tested for biconnectivity

                EXAMPLES:

                Example from the :wikipedia:`SPQR_tree`::

                    sage: from sage.graphs.connectivity import TriconnectivitySPQR
                    sage: from sage.graphs.connectivity import spqr_tree_to_graph
                    sage: G = Graph([(1, 2), (1, 4), (1, 8), (1, 12), (3, 4), (2, 3),
                    ....: (2, 13), (3, 13), (4, 5), (4, 7), (5, 6), (5, 8), (5, 7), (6, 7),
                    ....: (8, 11), (8, 9), (8, 12), (9, 10), (9, 11), (9, 12), (10, 12)])
                    sage: tric = TriconnectivitySPQR(G)
                    sage: T = tric.get_spqr_tree()
                    sage: G.is_isomorphic(spqr_tree_to_graph(T))
                    True
        """
    @overload
    def __init__(self, G) -> Any:
        """File: /build/sagemath/src/sage/src/sage/graphs/connectivity.pyx (starting at line 3477)

                Initialize this object, decompose the graph and build SPQR-tree.

                INPUT:

                - ``G`` -- graph; if ``G`` is a :class:`DiGraph`, the computation is
                  done on the underlying :class:`Graph` (i.e., ignoring edge
                  orientation)

                - ``check`` -- boolean (default: ``True``); indicates whether ``G``
                  needs to be tested for biconnectivity

                EXAMPLES:

                Example from the :wikipedia:`SPQR_tree`::

                    sage: from sage.graphs.connectivity import TriconnectivitySPQR
                    sage: from sage.graphs.connectivity import spqr_tree_to_graph
                    sage: G = Graph([(1, 2), (1, 4), (1, 8), (1, 12), (3, 4), (2, 3),
                    ....: (2, 13), (3, 13), (4, 5), (4, 7), (5, 6), (5, 8), (5, 7), (6, 7),
                    ....: (8, 11), (8, 9), (8, 12), (9, 10), (9, 11), (9, 12), (10, 12)])
                    sage: tric = TriconnectivitySPQR(G)
                    sage: T = tric.get_spqr_tree()
                    sage: G.is_isomorphic(spqr_tree_to_graph(T))
                    True
        """
    def get_spqr_tree(self) -> Any:
        """TriconnectivitySPQR.get_spqr_tree(self)

        File: /build/sagemath/src/sage/src/sage/graphs/connectivity.pyx (starting at line 4657)

        Return an SPQR-tree representing the triconnected components of the
        graph.

        An SPQR-tree is a tree data structure used to represent the triconnected
        components of a biconnected (multi)graph and the 2-vertex cuts
        separating them. A node of a SPQR-tree, and the graph associated with
        it, can be one of the following four types:

        - ``'S'`` -- the associated graph is a cycle with at least three vertices.
          ``'S'`` stands for ``series``.

        - ``'P'`` -- the associated graph is a dipole graph, a multigraph with
          two vertices and three or more edges. ``'P'`` stands for ``parallel``.

        - ``'Q'`` -- the associated graph has a single real edge. This trivial
          case is necessary to handle the graph that has only one edge.

        - ``'R'`` -- the associated graph is a 3-connected graph that is not a
          cycle or dipole. ``'R'`` stands for ``rigid``.

        The edges of the tree indicate the 2-vertex cuts of the graph.

        OUTPUT:

        ``SPQR-tree`` a tree whose vertices are labeled with the block's
        type and the subgraph of three-blocks in the decomposition.

        EXAMPLES::

            sage: from sage.graphs.connectivity import TriconnectivitySPQR
            sage: G = Graph(2)
            sage: for i in range(3):
            ....:     G.add_clique([0, 1, G.add_vertex(), G.add_vertex()])
            sage: tric = TriconnectivitySPQR(G)
            sage: Tree = tric.get_spqr_tree()
            sage: K4 = graphs.CompleteGraph(4)
            sage: all(u[1].is_isomorphic(K4) for u in Tree if u[0] == 'R')
            True
            sage: from sage.graphs.connectivity import spqr_tree_to_graph
            sage: G.is_isomorphic(spqr_tree_to_graph(Tree))
            True

            sage: G = Graph(2)
            sage: for i in range(3):
            ....:     G.add_path([0, G.add_vertex(), G.add_vertex(), 1])
            sage: tric = TriconnectivitySPQR(G)
            sage: Tree = tric.get_spqr_tree()
            sage: C4 = graphs.CycleGraph(4)
            sage: all(u[1].is_isomorphic(C4) for u in Tree if u[0] == 'S')
            True
            sage: G.is_isomorphic(spqr_tree_to_graph(Tree))
            True

            sage: G.allow_multiple_edges(True)
            sage: G.add_edges(G.edge_iterator())
            sage: tric = TriconnectivitySPQR(G)
            sage: Tree = tric.get_spqr_tree()
            sage: all(u[1].is_isomorphic(C4) for u in Tree if u[0] == 'S')
            True
            sage: G.is_isomorphic(spqr_tree_to_graph(Tree))
            True

            sage: G = graphs.CycleGraph(6)
            sage: tric = TriconnectivitySPQR(G)
            sage: Tree = tric.get_spqr_tree()
            sage: Tree.order()
            1
            sage: G.is_isomorphic(spqr_tree_to_graph(Tree))
            True
            sage: G.add_edge(0, 3)
            sage: tric = TriconnectivitySPQR(G)
            sage: Tree = tric.get_spqr_tree()
            sage: Tree.order()
            3
            sage: G.is_isomorphic(spqr_tree_to_graph(Tree))
            True

            sage: G = Graph([(0, 1)], multiedges=True)
            sage: tric = TriconnectivitySPQR(G)
            sage: Tree = tric.get_spqr_tree()
            sage: Tree.vertices(sort=True)
            [('Q', Multi-graph on 2 vertices)]
            sage: G.add_edge(0, 1)
            sage: Tree = TriconnectivitySPQR(G).get_spqr_tree()
            sage: Tree.vertices(sort=True)
            [('P', Multi-graph on 2 vertices)]"""
    @overload
    def get_triconnected_components(self) -> Any:
        """TriconnectivitySPQR.get_triconnected_components(self)

        File: /build/sagemath/src/sage/src/sage/graphs/connectivity.pyx (starting at line 4629)

        Return the triconnected components as a list of tuples.

        Each component is represented as a tuple of the type of the component
        and the list of edges of the component.

        EXAMPLES::

            sage: from sage.graphs.connectivity import TriconnectivitySPQR
            sage: G = Graph(2)
            sage: for i in range(3):
            ....:     G.add_path([0, G.add_vertex(), G.add_vertex(), 1])
            sage: tric = TriconnectivitySPQR(G)
            sage: tric.get_triconnected_components()
            [('Polygon', [(4, 5, None), (0, 4, None), (1, 5, None), (1, 0, 'newVEdge1')]),
            ('Polygon', [(6, 7, None), (0, 6, None), (1, 7, None), (1, 0, 'newVEdge3')]),
            ('Bond', [(1, 0, 'newVEdge1'), (1, 0, 'newVEdge3'), (1, 0, 'newVEdge4')]),
            ('Polygon', [(1, 3, None), (1, 0, 'newVEdge4'), (2, 3, None), (0, 2, None)])]"""
    @overload
    def get_triconnected_components(self) -> Any:
        """TriconnectivitySPQR.get_triconnected_components(self)

        File: /build/sagemath/src/sage/src/sage/graphs/connectivity.pyx (starting at line 4629)

        Return the triconnected components as a list of tuples.

        Each component is represented as a tuple of the type of the component
        and the list of edges of the component.

        EXAMPLES::

            sage: from sage.graphs.connectivity import TriconnectivitySPQR
            sage: G = Graph(2)
            sage: for i in range(3):
            ....:     G.add_path([0, G.add_vertex(), G.add_vertex(), 1])
            sage: tric = TriconnectivitySPQR(G)
            sage: tric.get_triconnected_components()
            [('Polygon', [(4, 5, None), (0, 4, None), (1, 5, None), (1, 0, 'newVEdge1')]),
            ('Polygon', [(6, 7, None), (0, 6, None), (1, 7, None), (1, 0, 'newVEdge3')]),
            ('Bond', [(1, 0, 'newVEdge1'), (1, 0, 'newVEdge3'), (1, 0, 'newVEdge4')]),
            ('Polygon', [(1, 3, None), (1, 0, 'newVEdge4'), (2, 3, None), (0, 2, None)])]"""
    @overload
    def print_triconnected_components(self) -> Any:
        """TriconnectivitySPQR.print_triconnected_components(self)

        File: /build/sagemath/src/sage/src/sage/graphs/connectivity.pyx (starting at line 4591)

        Print the type and list of edges of each component.

        EXAMPLES:

        An example from [Hopcroft1973]_::

            sage: from sage.graphs.connectivity import TriconnectivitySPQR
            sage: from sage.graphs.connectivity import spqr_tree_to_graph
            sage: G = Graph([(1, 2), (1, 4), (1, 8), (1, 12), (1, 13), (2, 3),
            ....: (2, 13), (3, 4), (3, 13), (4, 5), (4, 7), (5, 6), (5, 7), (5, 8),
            ....: (6, 7), (8, 9), (8, 11), (8, 12), (9, 10), (9, 11), (9, 12),
            ....: (10, 11), (10, 12)])
            sage: tric = TriconnectivitySPQR(G)
            sage: T = tric.get_spqr_tree()
            sage: G.is_isomorphic(spqr_tree_to_graph(T))
            True
            sage: tric.print_triconnected_components()
            Triconnected: [(8, 9, None), (9, 12, None), (9, 11, None), (8, 11, None), (10, 11, None), (9, 10, None), (10, 12, None), (8, 12, 'newVEdge0')]
            Bond: [(8, 12, None), (8, 12, 'newVEdge0'), (8, 12, 'newVEdge1')]
            Polygon: [(6, 7, None), (5, 6, None), (7, 5, 'newVEdge2')]
            Bond: [(7, 5, 'newVEdge2'), (5, 7, 'newVEdge3'), (5, 7, None)]
            Polygon: [(5, 7, 'newVEdge3'), (4, 7, None), (5, 4, 'newVEdge4')]
            Bond: [(5, 4, 'newVEdge4'), (4, 5, 'newVEdge5'), (4, 5, None)]
            Polygon: [(4, 5, 'newVEdge5'), (5, 8, None), (1, 4, 'newVEdge9'), (1, 8, 'newVEdge10')]
            Triconnected: [(1, 2, None), (2, 13, None), (1, 13, None), (3, 13, None), (2, 3, None), (1, 3, 'newVEdge7')]
            Polygon: [(1, 3, 'newVEdge7'), (3, 4, None), (1, 4, 'newVEdge8')]
            Bond: [(1, 4, None), (1, 4, 'newVEdge8'), (1, 4, 'newVEdge9')]
            Bond: [(1, 8, None), (1, 8, 'newVEdge10'), (1, 8, 'newVEdge11')]
            Polygon: [(8, 12, 'newVEdge1'), (1, 8, 'newVEdge11'), (1, 12, None)]"""
    @overload
    def print_triconnected_components(self) -> Any:
        """TriconnectivitySPQR.print_triconnected_components(self)

        File: /build/sagemath/src/sage/src/sage/graphs/connectivity.pyx (starting at line 4591)

        Print the type and list of edges of each component.

        EXAMPLES:

        An example from [Hopcroft1973]_::

            sage: from sage.graphs.connectivity import TriconnectivitySPQR
            sage: from sage.graphs.connectivity import spqr_tree_to_graph
            sage: G = Graph([(1, 2), (1, 4), (1, 8), (1, 12), (1, 13), (2, 3),
            ....: (2, 13), (3, 4), (3, 13), (4, 5), (4, 7), (5, 6), (5, 7), (5, 8),
            ....: (6, 7), (8, 9), (8, 11), (8, 12), (9, 10), (9, 11), (9, 12),
            ....: (10, 11), (10, 12)])
            sage: tric = TriconnectivitySPQR(G)
            sage: T = tric.get_spqr_tree()
            sage: G.is_isomorphic(spqr_tree_to_graph(T))
            True
            sage: tric.print_triconnected_components()
            Triconnected: [(8, 9, None), (9, 12, None), (9, 11, None), (8, 11, None), (10, 11, None), (9, 10, None), (10, 12, None), (8, 12, 'newVEdge0')]
            Bond: [(8, 12, None), (8, 12, 'newVEdge0'), (8, 12, 'newVEdge1')]
            Polygon: [(6, 7, None), (5, 6, None), (7, 5, 'newVEdge2')]
            Bond: [(7, 5, 'newVEdge2'), (5, 7, 'newVEdge3'), (5, 7, None)]
            Polygon: [(5, 7, 'newVEdge3'), (4, 7, None), (5, 4, 'newVEdge4')]
            Bond: [(5, 4, 'newVEdge4'), (4, 5, 'newVEdge5'), (4, 5, None)]
            Polygon: [(4, 5, 'newVEdge5'), (5, 8, None), (1, 4, 'newVEdge9'), (1, 8, 'newVEdge10')]
            Triconnected: [(1, 2, None), (2, 13, None), (1, 13, None), (3, 13, None), (2, 3, None), (1, 3, 'newVEdge7')]
            Polygon: [(1, 3, 'newVEdge7'), (3, 4, None), (1, 4, 'newVEdge8')]
            Bond: [(1, 4, None), (1, 4, 'newVEdge8'), (1, 4, 'newVEdge9')]
            Bond: [(1, 8, None), (1, 8, 'newVEdge10'), (1, 8, 'newVEdge11')]
            Polygon: [(8, 12, 'newVEdge1'), (1, 8, 'newVEdge11'), (1, 12, None)]"""

class _Component:
    """_Component(list edge_list, int type_c)

    File: /build/sagemath/src/sage/src/sage/graphs/connectivity.pyx (starting at line 3219)

    Connected component class.

    This is a helper class for ``TriconnectivitySPQR``.

    This class is used to store a connected component. It contains:

    - ``edge_list`` -- list of edges belonging to the component,
      stored as a :class:`_LinkedList`

    - ``component_type`` -- the type of the component

      - 0 if bond.
      - 1 if polygon.
      - 2 is triconnected component."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, listedge_list, inttype_c) -> Any:
        """File: /build/sagemath/src/sage/src/sage/graphs/connectivity.pyx (starting at line 3236)

                Initialize this component.

                INPUT:

                - ``edge_list`` -- list of edges to be added to the component

                - ``type_c`` -- type of the component (0, 1, or 2)

                TESTS::

                    sage: cython_code = [
                    ....: 'from sage.graphs.connectivity cimport _Component',
                    ....: 'cdef _Component comp = _Component([], 0)',
                    ....: 'comp.add_edge(2)',
                    ....: 'comp.add_edge(3)',
                    ....: 'comp.finish_tric_or_poly(4)',
                    ....: 'print(comp)']
                    sage: cython(os.linesep.join(cython_code))                                  # needs sage.misc.cython
                    Polygon: 2 3 4
        """
