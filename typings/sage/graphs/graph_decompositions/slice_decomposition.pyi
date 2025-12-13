import _cython_3_2_1
import sage.structure.sage_object
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from typing import Any, overload

__pyx_capi__: dict
slice_decomposition: _cython_3_2_1.cython_function_or_method

class SliceDecomposition(sage.structure.sage_object.SageObject):
    """SliceDecomposition(G, initial_vertex=None)"""
    def __init__(self, G, initial_vertex=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/slice_decomposition.pyx (starting at line 370)

                Represents a slice decomposition of a simple directed graph.

                INPUT:

                - ``G`` -- a Sage graph.

                - ``initial_vertex`` -- (default: ``None``); the first vertex to
                  consider.

                .. SEEALSO::

                    * :meth:`~slice_decomposition` -- compute a slice decomposition of
                      the simple undirected graph
                    * Section 3.2 of [TCHP2008]_ for a formal definition.

                EXAMPLES:

                The constructor of the :class:`~SliceDecomposition` class is called by
                the :meth:`~slice_decomposition` method of undirected graphs::

                    sage: from sage.graphs.graph_decompositions.slice_decomposition import SliceDecomposition
                    sage: G = graphs.PetersenGraph()
                    sage: SliceDecomposition(G) == G.slice_decomposition()
                    True

                The vertex appearing first in the slice decomposition can be specified::

                    sage: from sage.graphs.graph_decompositions.slice_decomposition import SliceDecomposition
                    sage: SliceDecomposition(graphs.PetersenGraph(), initial_vertex=3)
                    [3[2[4[8]]] [1[7]] [0] [9] [6] [5]]

                Slice decompositions are not defined for directed graphs::

                    sage: from sage.graphs.graph_decompositions.slice_decomposition import SliceDecomposition
                    sage: SliceDecomposition(DiGraph())
                    Traceback (most recent call last):
                    ...
                    ValueError: parameter G must be an undirected graph

                .. automethod:: __getitem__
        """
    @overload
    def active_edges(self, v) -> Any:
        """SliceDecomposition.active_edges(self, v)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/slice_decomposition.pyx (starting at line 819)

        Return the active edges of the vertex `v`.

        An edge `(u, w)` is said to be active for `v` if `u` and `w` belongs
        to two differents slices of the x-slice sequence of `v`. Note that it
        defines a partition of the edges of the underlying graph.

        INPUT:

        - ``v`` -- a vertex of the graph corresponding to the slice
          decomposition.

        OUTPUT:

        A list of edges

        EXAMPLES:

        ::

            sage: G = Graph('L~mpn~Nrv{^o~_').relabel('abcdefguvwxyz',inplace=False)
            sage: SD = G.slice_decomposition(initial_vertex='x')
            sage: SD.xslice_sequence('a')
            [['a'], ['b', 'c', 'd', 'e', 'f'], ['g']]
            sage: ('c', 'g') in SD.active_edges('a')
            True
            sage: ('a', 'c') in SD.active_edges('a')
            True
            sage: ('c', 'd') in SD.active_edges('a')  # c and d in same slice
            False
            sage: ('a', 'u') in SD.active_edges('a')  # u not in x-slice of a
            False

        The set of active edges of every vertex is a partition of the edges::

            sage: from itertools import chain
            sage: E = list(chain(*(SD.active_edges(v) for v in G)))
            sage: G.size() == len(E) == len(set(E)) \\\n            ....:   and all(G.has_edge(u, w) for v in G for u, w in SD.active_edges(v))
            True

        TESTS::

            sage: SD = graphs.PetersenGraph().slice_decomposition()
            sage: SD.active_edges('Graham')
            Traceback (most recent call last):
            ...
            LookupError: vertex (Graham) does not appear in the slice decomposition"""
    @overload
    def active_edges(self, v) -> Any:
        """SliceDecomposition.active_edges(self, v)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/slice_decomposition.pyx (starting at line 819)

        Return the active edges of the vertex `v`.

        An edge `(u, w)` is said to be active for `v` if `u` and `w` belongs
        to two differents slices of the x-slice sequence of `v`. Note that it
        defines a partition of the edges of the underlying graph.

        INPUT:

        - ``v`` -- a vertex of the graph corresponding to the slice
          decomposition.

        OUTPUT:

        A list of edges

        EXAMPLES:

        ::

            sage: G = Graph('L~mpn~Nrv{^o~_').relabel('abcdefguvwxyz',inplace=False)
            sage: SD = G.slice_decomposition(initial_vertex='x')
            sage: SD.xslice_sequence('a')
            [['a'], ['b', 'c', 'd', 'e', 'f'], ['g']]
            sage: ('c', 'g') in SD.active_edges('a')
            True
            sage: ('a', 'c') in SD.active_edges('a')
            True
            sage: ('c', 'd') in SD.active_edges('a')  # c and d in same slice
            False
            sage: ('a', 'u') in SD.active_edges('a')  # u not in x-slice of a
            False

        The set of active edges of every vertex is a partition of the edges::

            sage: from itertools import chain
            sage: E = list(chain(*(SD.active_edges(v) for v in G)))
            sage: G.size() == len(E) == len(set(E)) \\\n            ....:   and all(G.has_edge(u, w) for v in G for u, w in SD.active_edges(v))
            True

        TESTS::

            sage: SD = graphs.PetersenGraph().slice_decomposition()
            sage: SD.active_edges('Graham')
            Traceback (most recent call last):
            ...
            LookupError: vertex (Graham) does not appear in the slice decomposition"""
    @overload
    def active_edges(self, v) -> Any:
        """SliceDecomposition.active_edges(self, v)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/slice_decomposition.pyx (starting at line 819)

        Return the active edges of the vertex `v`.

        An edge `(u, w)` is said to be active for `v` if `u` and `w` belongs
        to two differents slices of the x-slice sequence of `v`. Note that it
        defines a partition of the edges of the underlying graph.

        INPUT:

        - ``v`` -- a vertex of the graph corresponding to the slice
          decomposition.

        OUTPUT:

        A list of edges

        EXAMPLES:

        ::

            sage: G = Graph('L~mpn~Nrv{^o~_').relabel('abcdefguvwxyz',inplace=False)
            sage: SD = G.slice_decomposition(initial_vertex='x')
            sage: SD.xslice_sequence('a')
            [['a'], ['b', 'c', 'd', 'e', 'f'], ['g']]
            sage: ('c', 'g') in SD.active_edges('a')
            True
            sage: ('a', 'c') in SD.active_edges('a')
            True
            sage: ('c', 'd') in SD.active_edges('a')  # c and d in same slice
            False
            sage: ('a', 'u') in SD.active_edges('a')  # u not in x-slice of a
            False

        The set of active edges of every vertex is a partition of the edges::

            sage: from itertools import chain
            sage: E = list(chain(*(SD.active_edges(v) for v in G)))
            sage: G.size() == len(E) == len(set(E)) \\\n            ....:   and all(G.has_edge(u, w) for v in G for u, w in SD.active_edges(v))
            True

        TESTS::

            sage: SD = graphs.PetersenGraph().slice_decomposition()
            sage: SD.active_edges('Graham')
            Traceback (most recent call last):
            ...
            LookupError: vertex (Graham) does not appear in the slice decomposition"""
    @overload
    def lexBFS_order(self) -> Any:
        """SliceDecomposition.lexBFS_order(self)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/slice_decomposition.pyx (starting at line 603)

        Return the lexBFS order corresponding to the slice decomposition.

        EXAMPLES::

            sage: from sage.graphs.traversals import _is_valid_lex_BFS_order
            sage: G = graphs.PetersenGraph(); SD = G.slice_decomposition()
            sage: SD.lexBFS_order()
            [0, 1, 4, 5, 2, 6, 3, 9, 7, 8]
            sage: _is_valid_lex_BFS_order(G, SD.lexBFS_order())
            True

        TESTS::

            sage: from sage.graphs.traversals import _is_valid_lex_BFS_order
            sage: for _ in range(5):
            ....:   G = graphs.RandomGNP(15, 0.3)
            ....:   SD = G.slice_decomposition()
            ....:   _is_valid_lex_BFS_order(G, SD.lexBFS_order())
            True
            True
            True
            True
            True"""
    @overload
    def lexBFS_order(self) -> Any:
        """SliceDecomposition.lexBFS_order(self)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/slice_decomposition.pyx (starting at line 603)

        Return the lexBFS order corresponding to the slice decomposition.

        EXAMPLES::

            sage: from sage.graphs.traversals import _is_valid_lex_BFS_order
            sage: G = graphs.PetersenGraph(); SD = G.slice_decomposition()
            sage: SD.lexBFS_order()
            [0, 1, 4, 5, 2, 6, 3, 9, 7, 8]
            sage: _is_valid_lex_BFS_order(G, SD.lexBFS_order())
            True

        TESTS::

            sage: from sage.graphs.traversals import _is_valid_lex_BFS_order
            sage: for _ in range(5):
            ....:   G = graphs.RandomGNP(15, 0.3)
            ....:   SD = G.slice_decomposition()
            ....:   _is_valid_lex_BFS_order(G, SD.lexBFS_order())
            True
            True
            True
            True
            True"""
    @overload
    def lexBFS_order(self) -> Any:
        """SliceDecomposition.lexBFS_order(self)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/slice_decomposition.pyx (starting at line 603)

        Return the lexBFS order corresponding to the slice decomposition.

        EXAMPLES::

            sage: from sage.graphs.traversals import _is_valid_lex_BFS_order
            sage: G = graphs.PetersenGraph(); SD = G.slice_decomposition()
            sage: SD.lexBFS_order()
            [0, 1, 4, 5, 2, 6, 3, 9, 7, 8]
            sage: _is_valid_lex_BFS_order(G, SD.lexBFS_order())
            True

        TESTS::

            sage: from sage.graphs.traversals import _is_valid_lex_BFS_order
            sage: for _ in range(5):
            ....:   G = graphs.RandomGNP(15, 0.3)
            ....:   SD = G.slice_decomposition()
            ....:   _is_valid_lex_BFS_order(G, SD.lexBFS_order())
            True
            True
            True
            True
            True"""
    @overload
    def lexBFS_order(self) -> Any:
        """SliceDecomposition.lexBFS_order(self)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/slice_decomposition.pyx (starting at line 603)

        Return the lexBFS order corresponding to the slice decomposition.

        EXAMPLES::

            sage: from sage.graphs.traversals import _is_valid_lex_BFS_order
            sage: G = graphs.PetersenGraph(); SD = G.slice_decomposition()
            sage: SD.lexBFS_order()
            [0, 1, 4, 5, 2, 6, 3, 9, 7, 8]
            sage: _is_valid_lex_BFS_order(G, SD.lexBFS_order())
            True

        TESTS::

            sage: from sage.graphs.traversals import _is_valid_lex_BFS_order
            sage: for _ in range(5):
            ....:   G = graphs.RandomGNP(15, 0.3)
            ....:   SD = G.slice_decomposition()
            ....:   _is_valid_lex_BFS_order(G, SD.lexBFS_order())
            True
            True
            True
            True
            True"""
    def lexicographic_label(self, v) -> Any:
        """SliceDecomposition.lexicographic_label(self, v)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/slice_decomposition.pyx (starting at line 777)

        Return the lexicographic label of the vertex `v`.

        The lexicographic label of a vertex `v` is the list of all the
        neighbors of `v` that appear before `v` in the lexBFS ordering
        corresponding to the slice decomposition.

        INPUT:

        - ``v`` -- a vertex of the graph corresponding to the slice
          decomposition.

        OUTPUT:

        A list of vertices.

        EXAMPLES::

            sage: G = Graph('L~mpn~Nrv{^o~_').relabel('abcdefguvwxyz',inplace=False)
            sage: SD = G.slice_decomposition(initial_vertex='x')
            sage: SD.lexicographic_label('f')
            ['x', 'a', 'c', 'd']
            sage: pos = lambda v: SD.lexBFS_order().index(v)
            sage: set(SD.lexicographic_label('f')) \\\n            ....:   == {v for v in G.neighbors('f') if pos(v) < pos('f')}
            True

        TESTS::

            sage: SD = graphs.PetersenGraph().slice_decomposition()
            sage: SD.lexicographic_label('Eric')
            Traceback (most recent call last):
            ...
            LookupError: vertex (Eric) does not appear in the slice decomposition"""
    def slice(self, v) -> Any:
        '''SliceDecomposition.slice(self, v)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/slice_decomposition.pyx (starting at line 646)

        Return the slice of the vertex `v`.

        The slice of `v` is the list of vertices `u` such that the neighbors of
        `u` that are before `v` in the lexBFS order are that same that the
        neighbors of `v` that are before `v` in the lexBFS order (*i.e.*, the
        lexicographic label of `v`). It can be shown that it is a factor of the
        lexBFS order.

        INPUT:

        - ``v`` -- a vertex of the graph corresponding to the slice
          decomposition.

        OUTPUT:

        A list of vertices

        EXAMPLES:

        ::

            sage: G = Graph(\'L~mpn~Nrv{^o~_\').relabel(\'abcdefguvwxyz\',inplace=False)
            sage: SD = G.slice_decomposition(initial_vertex=\'x\')
            sage: SD.slice(\'a\')
            [\'a\', \'b\', \'c\', \'d\', \'e\', \'f\', \'g\']

        The vertices of the slice have the same neighborhood "on the left"::

            sage: pos = lambda v: SD.lexBFS_order().index(v)
            sage: lla = set(SD.lexicographic_label(\'a\'))
            sage: all(lla == {u for u in G.neighbors(v) if pos(u) < pos(\'a\')} \\\n            ....:       for v in SD.slice(\'a\'))
            True

        The slice is a factor of the lexBFS order::

            sage: \'\'.join(SD.slice(\'a\')) in \'\'.join(SD.lexBFS_order())
            True

        The slice of the initial vertex is the whole graph::

            sage: SD.slice(\'x\') == SD.lexBFS_order()
            True

        TESTS::

            sage: SD.slice(\'Michael\')
            Traceback (most recent call last):
            ...
            LookupError: vertex (Michael) does not appear in the slice decomposition'''
    @overload
    def underlying_graph(self) -> Any:
        """SliceDecomposition.underlying_graph(self)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/slice_decomposition.pyx (starting at line 955)

        Return the underlying graph corresponding to the slice decomposition.

        If `G` was the graph given as parameter to compute the slice
        decomposition, the underlying graph corresponds to ``G.to_simple()``
        where labels are ignored, *i.e.*, it is the input graph without loops,
        multiple edges and labels.

        .. NOTE::

            This method is mostly defined to test the computation of
            lexicographic labels and actives edges.

        EXAMPLES:

        ::

            sage: G = Graph('L~mpn~Nrv{^o~_').relabel('abcdefguvwxyz',inplace=False)
            sage: SD = G.slice_decomposition(initial_vertex='x')
            sage: SD.underlying_graph() == G
            True

        The graph can have loops or multiple edges but they are ignored::

            sage: G = graphs.CubeConnectedCycle(2)  # multiple edges
            sage: SD = G.slice_decomposition()
            sage: SD.underlying_graph() == G.to_simple(immutable=True)
            True

            sage: G = graphs.CubeConnectedCycle(1)  # loops
            sage: SD = G.slice_decomposition()
            sage: SD.underlying_graph() == G.to_simple(immutable=True)
            True

        TESTS::

            sage: for _ in range(5):
            ....:   G = graphs.RandomGNP(15, 0.3)
            ....:   SD = G.slice_decomposition()
            ....:   SD.underlying_graph() == G
            True
            True
            True
            True
            True"""
    @overload
    def underlying_graph(self) -> Any:
        """SliceDecomposition.underlying_graph(self)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/slice_decomposition.pyx (starting at line 955)

        Return the underlying graph corresponding to the slice decomposition.

        If `G` was the graph given as parameter to compute the slice
        decomposition, the underlying graph corresponds to ``G.to_simple()``
        where labels are ignored, *i.e.*, it is the input graph without loops,
        multiple edges and labels.

        .. NOTE::

            This method is mostly defined to test the computation of
            lexicographic labels and actives edges.

        EXAMPLES:

        ::

            sage: G = Graph('L~mpn~Nrv{^o~_').relabel('abcdefguvwxyz',inplace=False)
            sage: SD = G.slice_decomposition(initial_vertex='x')
            sage: SD.underlying_graph() == G
            True

        The graph can have loops or multiple edges but they are ignored::

            sage: G = graphs.CubeConnectedCycle(2)  # multiple edges
            sage: SD = G.slice_decomposition()
            sage: SD.underlying_graph() == G.to_simple(immutable=True)
            True

            sage: G = graphs.CubeConnectedCycle(1)  # loops
            sage: SD = G.slice_decomposition()
            sage: SD.underlying_graph() == G.to_simple(immutable=True)
            True

        TESTS::

            sage: for _ in range(5):
            ....:   G = graphs.RandomGNP(15, 0.3)
            ....:   SD = G.slice_decomposition()
            ....:   SD.underlying_graph() == G
            True
            True
            True
            True
            True"""
    @overload
    def underlying_graph(self) -> Any:
        """SliceDecomposition.underlying_graph(self)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/slice_decomposition.pyx (starting at line 955)

        Return the underlying graph corresponding to the slice decomposition.

        If `G` was the graph given as parameter to compute the slice
        decomposition, the underlying graph corresponds to ``G.to_simple()``
        where labels are ignored, *i.e.*, it is the input graph without loops,
        multiple edges and labels.

        .. NOTE::

            This method is mostly defined to test the computation of
            lexicographic labels and actives edges.

        EXAMPLES:

        ::

            sage: G = Graph('L~mpn~Nrv{^o~_').relabel('abcdefguvwxyz',inplace=False)
            sage: SD = G.slice_decomposition(initial_vertex='x')
            sage: SD.underlying_graph() == G
            True

        The graph can have loops or multiple edges but they are ignored::

            sage: G = graphs.CubeConnectedCycle(2)  # multiple edges
            sage: SD = G.slice_decomposition()
            sage: SD.underlying_graph() == G.to_simple(immutable=True)
            True

            sage: G = graphs.CubeConnectedCycle(1)  # loops
            sage: SD = G.slice_decomposition()
            sage: SD.underlying_graph() == G.to_simple(immutable=True)
            True

        TESTS::

            sage: for _ in range(5):
            ....:   G = graphs.RandomGNP(15, 0.3)
            ....:   SD = G.slice_decomposition()
            ....:   SD.underlying_graph() == G
            True
            True
            True
            True
            True"""
    @overload
    def underlying_graph(self) -> Any:
        """SliceDecomposition.underlying_graph(self)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/slice_decomposition.pyx (starting at line 955)

        Return the underlying graph corresponding to the slice decomposition.

        If `G` was the graph given as parameter to compute the slice
        decomposition, the underlying graph corresponds to ``G.to_simple()``
        where labels are ignored, *i.e.*, it is the input graph without loops,
        multiple edges and labels.

        .. NOTE::

            This method is mostly defined to test the computation of
            lexicographic labels and actives edges.

        EXAMPLES:

        ::

            sage: G = Graph('L~mpn~Nrv{^o~_').relabel('abcdefguvwxyz',inplace=False)
            sage: SD = G.slice_decomposition(initial_vertex='x')
            sage: SD.underlying_graph() == G
            True

        The graph can have loops or multiple edges but they are ignored::

            sage: G = graphs.CubeConnectedCycle(2)  # multiple edges
            sage: SD = G.slice_decomposition()
            sage: SD.underlying_graph() == G.to_simple(immutable=True)
            True

            sage: G = graphs.CubeConnectedCycle(1)  # loops
            sage: SD = G.slice_decomposition()
            sage: SD.underlying_graph() == G.to_simple(immutable=True)
            True

        TESTS::

            sage: for _ in range(5):
            ....:   G = graphs.RandomGNP(15, 0.3)
            ....:   SD = G.slice_decomposition()
            ....:   SD.underlying_graph() == G
            True
            True
            True
            True
            True"""
    @overload
    def underlying_graph(self) -> Any:
        """SliceDecomposition.underlying_graph(self)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/slice_decomposition.pyx (starting at line 955)

        Return the underlying graph corresponding to the slice decomposition.

        If `G` was the graph given as parameter to compute the slice
        decomposition, the underlying graph corresponds to ``G.to_simple()``
        where labels are ignored, *i.e.*, it is the input graph without loops,
        multiple edges and labels.

        .. NOTE::

            This method is mostly defined to test the computation of
            lexicographic labels and actives edges.

        EXAMPLES:

        ::

            sage: G = Graph('L~mpn~Nrv{^o~_').relabel('abcdefguvwxyz',inplace=False)
            sage: SD = G.slice_decomposition(initial_vertex='x')
            sage: SD.underlying_graph() == G
            True

        The graph can have loops or multiple edges but they are ignored::

            sage: G = graphs.CubeConnectedCycle(2)  # multiple edges
            sage: SD = G.slice_decomposition()
            sage: SD.underlying_graph() == G.to_simple(immutable=True)
            True

            sage: G = graphs.CubeConnectedCycle(1)  # loops
            sage: SD = G.slice_decomposition()
            sage: SD.underlying_graph() == G.to_simple(immutable=True)
            True

        TESTS::

            sage: for _ in range(5):
            ....:   G = graphs.RandomGNP(15, 0.3)
            ....:   SD = G.slice_decomposition()
            ....:   SD.underlying_graph() == G
            True
            True
            True
            True
            True"""
    @overload
    def xslice_data(self, v) -> Any:
        """SliceDecomposition.xslice_data(self, v)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/slice_decomposition.pyx (starting at line 631)

        Return the data about the x-slice of the vertex `v`.

        This method is a wrapper around :meth:`SliceDecomposition.__getitem__`

        TESTS::

            sage: G = graphs.RandomGNP(15, 0.3)
            sage: SD = G.slice_decomposition()
            sage: all(SD[v] == SD.xslice_data(v) for v in G)
            True"""
    @overload
    def xslice_data(self, v) -> Any:
        """SliceDecomposition.xslice_data(self, v)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/slice_decomposition.pyx (starting at line 631)

        Return the data about the x-slice of the vertex `v`.

        This method is a wrapper around :meth:`SliceDecomposition.__getitem__`

        TESTS::

            sage: G = graphs.RandomGNP(15, 0.3)
            sage: SD = G.slice_decomposition()
            sage: all(SD[v] == SD.xslice_data(v) for v in G)
            True"""
    @overload
    def xslice_sequence(self, v) -> Any:
        """SliceDecomposition.xslice_sequence(self, v)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/slice_decomposition.pyx (starting at line 705)

        Return the x-slice sequence of the vertex `v`.

        INPUT:

        - ``v`` -- a vertex of the graph corresponding to the slice
          decomposition.

        OUTPUT:

        A list of list corresponding to the x-slice sequence of ``v``.

        EXAMPLES:

        ::

            sage: G = Graph('L~mpn~Nrv{^o~_').relabel('abcdefguvwxyz',inplace=False)
            sage: SD = G.slice_decomposition(initial_vertex='x')
            sage: SD.xslice_sequence('x')
            [['x'], ['a', 'b', 'c', 'd', 'e', 'f', 'g'], ['u', 'y', 'z'], ['v', 'w']]
            sage: SD.xslice_sequence('a')
            [['a'], ['b', 'c', 'd', 'e', 'f'], ['g']]

        The flatten x-slice sequence of a vertex corresponds to the slice of the
        same vertex::

            sage: from itertools import chain
            sage: all(list(chain(*SD.xslice_sequence(v))) == SD.slice(v) \\\n            ....:       for v in G)
            True

        The first list of the sequence is always a singleton containing the
        input vertex::

            sage: all(SD.xslice_sequence(v)[0] == [v] for v in G)
            True

        If the length of the slice if more than 1, the second list of the
        sequence is either, all the remaining vertices of the slice of `v`, if
        `v` is isolated in the subgraph induced by the slice of `v`, or the
        neighbors of `v` in the subgraph induced by the slice of `v`::

            sage: all(SD.xslice_sequence(v)[1] == SD.slice(v)[1:] for v in G \\\n            ....:           if G.subgraph(SD.slice(v)).degree(v) == 0 \\\n            ....:               and len(SD.slice(v)) > 1)
            True
            sage: for v in G:
            ....:     if len(SD.slice(v)) > 1:
            ....:         xslice_seq = SD.xslice_sequence(v)
            ....:         S = G.subgraph(SD.slice(v))
            ....:         if S.degree(v) > 0:
            ....:             set(xslice_seq[1]) == set(S.neighbor_iterator(v))
            True
            True
            True
            True

        TESTS::

            sage: SD = graphs.PetersenGraph().slice_decomposition()
            sage: SD.xslice_sequence('Terry')
            Traceback (most recent call last):
            ...
            LookupError: vertex (Terry) does not appear in the slice decomposition"""
    @overload
    def xslice_sequence(self, v) -> Any:
        """SliceDecomposition.xslice_sequence(self, v)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/slice_decomposition.pyx (starting at line 705)

        Return the x-slice sequence of the vertex `v`.

        INPUT:

        - ``v`` -- a vertex of the graph corresponding to the slice
          decomposition.

        OUTPUT:

        A list of list corresponding to the x-slice sequence of ``v``.

        EXAMPLES:

        ::

            sage: G = Graph('L~mpn~Nrv{^o~_').relabel('abcdefguvwxyz',inplace=False)
            sage: SD = G.slice_decomposition(initial_vertex='x')
            sage: SD.xslice_sequence('x')
            [['x'], ['a', 'b', 'c', 'd', 'e', 'f', 'g'], ['u', 'y', 'z'], ['v', 'w']]
            sage: SD.xslice_sequence('a')
            [['a'], ['b', 'c', 'd', 'e', 'f'], ['g']]

        The flatten x-slice sequence of a vertex corresponds to the slice of the
        same vertex::

            sage: from itertools import chain
            sage: all(list(chain(*SD.xslice_sequence(v))) == SD.slice(v) \\\n            ....:       for v in G)
            True

        The first list of the sequence is always a singleton containing the
        input vertex::

            sage: all(SD.xslice_sequence(v)[0] == [v] for v in G)
            True

        If the length of the slice if more than 1, the second list of the
        sequence is either, all the remaining vertices of the slice of `v`, if
        `v` is isolated in the subgraph induced by the slice of `v`, or the
        neighbors of `v` in the subgraph induced by the slice of `v`::

            sage: all(SD.xslice_sequence(v)[1] == SD.slice(v)[1:] for v in G \\\n            ....:           if G.subgraph(SD.slice(v)).degree(v) == 0 \\\n            ....:               and len(SD.slice(v)) > 1)
            True
            sage: for v in G:
            ....:     if len(SD.slice(v)) > 1:
            ....:         xslice_seq = SD.xslice_sequence(v)
            ....:         S = G.subgraph(SD.slice(v))
            ....:         if S.degree(v) > 0:
            ....:             set(xslice_seq[1]) == set(S.neighbor_iterator(v))
            True
            True
            True
            True

        TESTS::

            sage: SD = graphs.PetersenGraph().slice_decomposition()
            sage: SD.xslice_sequence('Terry')
            Traceback (most recent call last):
            ...
            LookupError: vertex (Terry) does not appear in the slice decomposition"""
    @overload
    def xslice_sequence(self, v) -> Any:
        """SliceDecomposition.xslice_sequence(self, v)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/slice_decomposition.pyx (starting at line 705)

        Return the x-slice sequence of the vertex `v`.

        INPUT:

        - ``v`` -- a vertex of the graph corresponding to the slice
          decomposition.

        OUTPUT:

        A list of list corresponding to the x-slice sequence of ``v``.

        EXAMPLES:

        ::

            sage: G = Graph('L~mpn~Nrv{^o~_').relabel('abcdefguvwxyz',inplace=False)
            sage: SD = G.slice_decomposition(initial_vertex='x')
            sage: SD.xslice_sequence('x')
            [['x'], ['a', 'b', 'c', 'd', 'e', 'f', 'g'], ['u', 'y', 'z'], ['v', 'w']]
            sage: SD.xslice_sequence('a')
            [['a'], ['b', 'c', 'd', 'e', 'f'], ['g']]

        The flatten x-slice sequence of a vertex corresponds to the slice of the
        same vertex::

            sage: from itertools import chain
            sage: all(list(chain(*SD.xslice_sequence(v))) == SD.slice(v) \\\n            ....:       for v in G)
            True

        The first list of the sequence is always a singleton containing the
        input vertex::

            sage: all(SD.xslice_sequence(v)[0] == [v] for v in G)
            True

        If the length of the slice if more than 1, the second list of the
        sequence is either, all the remaining vertices of the slice of `v`, if
        `v` is isolated in the subgraph induced by the slice of `v`, or the
        neighbors of `v` in the subgraph induced by the slice of `v`::

            sage: all(SD.xslice_sequence(v)[1] == SD.slice(v)[1:] for v in G \\\n            ....:           if G.subgraph(SD.slice(v)).degree(v) == 0 \\\n            ....:               and len(SD.slice(v)) > 1)
            True
            sage: for v in G:
            ....:     if len(SD.slice(v)) > 1:
            ....:         xslice_seq = SD.xslice_sequence(v)
            ....:         S = G.subgraph(SD.slice(v))
            ....:         if S.degree(v) > 0:
            ....:             set(xslice_seq[1]) == set(S.neighbor_iterator(v))
            True
            True
            True
            True

        TESTS::

            sage: SD = graphs.PetersenGraph().slice_decomposition()
            sage: SD.xslice_sequence('Terry')
            Traceback (most recent call last):
            ...
            LookupError: vertex (Terry) does not appear in the slice decomposition"""
    @overload
    def xslice_sequence(self, v) -> Any:
        """SliceDecomposition.xslice_sequence(self, v)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/slice_decomposition.pyx (starting at line 705)

        Return the x-slice sequence of the vertex `v`.

        INPUT:

        - ``v`` -- a vertex of the graph corresponding to the slice
          decomposition.

        OUTPUT:

        A list of list corresponding to the x-slice sequence of ``v``.

        EXAMPLES:

        ::

            sage: G = Graph('L~mpn~Nrv{^o~_').relabel('abcdefguvwxyz',inplace=False)
            sage: SD = G.slice_decomposition(initial_vertex='x')
            sage: SD.xslice_sequence('x')
            [['x'], ['a', 'b', 'c', 'd', 'e', 'f', 'g'], ['u', 'y', 'z'], ['v', 'w']]
            sage: SD.xslice_sequence('a')
            [['a'], ['b', 'c', 'd', 'e', 'f'], ['g']]

        The flatten x-slice sequence of a vertex corresponds to the slice of the
        same vertex::

            sage: from itertools import chain
            sage: all(list(chain(*SD.xslice_sequence(v))) == SD.slice(v) \\\n            ....:       for v in G)
            True

        The first list of the sequence is always a singleton containing the
        input vertex::

            sage: all(SD.xslice_sequence(v)[0] == [v] for v in G)
            True

        If the length of the slice if more than 1, the second list of the
        sequence is either, all the remaining vertices of the slice of `v`, if
        `v` is isolated in the subgraph induced by the slice of `v`, or the
        neighbors of `v` in the subgraph induced by the slice of `v`::

            sage: all(SD.xslice_sequence(v)[1] == SD.slice(v)[1:] for v in G \\\n            ....:           if G.subgraph(SD.slice(v)).degree(v) == 0 \\\n            ....:               and len(SD.slice(v)) > 1)
            True
            sage: for v in G:
            ....:     if len(SD.slice(v)) > 1:
            ....:         xslice_seq = SD.xslice_sequence(v)
            ....:         S = G.subgraph(SD.slice(v))
            ....:         if S.degree(v) > 0:
            ....:             set(xslice_seq[1]) == set(S.neighbor_iterator(v))
            True
            True
            True
            True

        TESTS::

            sage: SD = graphs.PetersenGraph().slice_decomposition()
            sage: SD.xslice_sequence('Terry')
            Traceback (most recent call last):
            ...
            LookupError: vertex (Terry) does not appear in the slice decomposition"""
    @overload
    def xslice_sequence(self, v) -> Any:
        """SliceDecomposition.xslice_sequence(self, v)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/slice_decomposition.pyx (starting at line 705)

        Return the x-slice sequence of the vertex `v`.

        INPUT:

        - ``v`` -- a vertex of the graph corresponding to the slice
          decomposition.

        OUTPUT:

        A list of list corresponding to the x-slice sequence of ``v``.

        EXAMPLES:

        ::

            sage: G = Graph('L~mpn~Nrv{^o~_').relabel('abcdefguvwxyz',inplace=False)
            sage: SD = G.slice_decomposition(initial_vertex='x')
            sage: SD.xslice_sequence('x')
            [['x'], ['a', 'b', 'c', 'd', 'e', 'f', 'g'], ['u', 'y', 'z'], ['v', 'w']]
            sage: SD.xslice_sequence('a')
            [['a'], ['b', 'c', 'd', 'e', 'f'], ['g']]

        The flatten x-slice sequence of a vertex corresponds to the slice of the
        same vertex::

            sage: from itertools import chain
            sage: all(list(chain(*SD.xslice_sequence(v))) == SD.slice(v) \\\n            ....:       for v in G)
            True

        The first list of the sequence is always a singleton containing the
        input vertex::

            sage: all(SD.xslice_sequence(v)[0] == [v] for v in G)
            True

        If the length of the slice if more than 1, the second list of the
        sequence is either, all the remaining vertices of the slice of `v`, if
        `v` is isolated in the subgraph induced by the slice of `v`, or the
        neighbors of `v` in the subgraph induced by the slice of `v`::

            sage: all(SD.xslice_sequence(v)[1] == SD.slice(v)[1:] for v in G \\\n            ....:           if G.subgraph(SD.slice(v)).degree(v) == 0 \\\n            ....:               and len(SD.slice(v)) > 1)
            True
            sage: for v in G:
            ....:     if len(SD.slice(v)) > 1:
            ....:         xslice_seq = SD.xslice_sequence(v)
            ....:         S = G.subgraph(SD.slice(v))
            ....:         if S.degree(v) > 0:
            ....:             set(xslice_seq[1]) == set(S.neighbor_iterator(v))
            True
            True
            True
            True

        TESTS::

            sage: SD = graphs.PetersenGraph().slice_decomposition()
            sage: SD.xslice_sequence('Terry')
            Traceback (most recent call last):
            ...
            LookupError: vertex (Terry) does not appear in the slice decomposition"""
    def __eq__(self, other) -> Any:
        """SliceDecomposition.__eq__(self, other)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/slice_decomposition.pyx (starting at line 447)

        Return whether ``self`` and ``other`` are equal.

        TESTS::

            sage: G = graphs.PetersenGraph()
            sage: SD = G.slice_decomposition()
            sage: SD == SD
            True
            sage: SD == G.slice_decomposition()
            True

            sage: P3 = graphs.PathGraph(3)
            sage: SD1 = P3.slice_decomposition(initial_vertex=0)
            sage: SD2 = P3.slice_decomposition(initial_vertex=2)
            sage: SD1 == SD2
            False
            sage: SD3 = graphs.CompleteGraph(3).slice_decomposition()
            sage: SD1 == SD3  # same lexBFS but different slice for 1
            False
            sage: SD4 = Graph([(0,1), (0,2)]).slice_decomposition()
            sage: SD3 == SD4  # same lexBFS and slices but different active edges
            False"""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __getitem__(self, v) -> Any:
        '''SliceDecomposition.__getitem__(self, v)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/slice_decomposition.pyx (starting at line 497)

        Return the data about the x-slice of the vertex `v`.

        INPUT:

        - ``v`` -- a vertex of the graph corresponding to the slice
          decomposition.

        OUTPUT:

        A dictionary with the keys:

        * ``"pivot"`` -- the vertex `v` given as parameter

        * ``"slice"`` -- the slice of `v` (see :meth:`~slice`)

        * ``"active_edges"`` -- the actives edges of `v` (see
          :meth:`~active_edges`)

        * ``"lexicographic_label"`` -- the lexicographic label of `v` (see
          :meth:`~lexicographic_label`)

        * ``"sequence"`` -- the x-slice sequence of `v` (see
          :meth:`~xslice_sequence`)

        This method can also be called via :meth:`xslice_data`.

        EXAMPLES:

        ::

            sage: G = Graph(\'L~mpn~Nrv{^o~_\').relabel(\'abcdefguvwxyz\',inplace=False)
            sage: SD = G.slice_decomposition(initial_vertex=\'x\')
            sage: SD.xslice_data(\'a\')
            {\'active_edges\': [(\'a\', \'b\'),
              (\'a\', \'c\'),
              (\'a\', \'d\'),
              (\'a\', \'e\'),
              (\'a\', \'f\'),
              (\'c\', \'g\'),
              (\'d\', \'g\'),
              (\'f\', \'g\')],
             \'lexicographic_label\': [\'x\'],
             \'pivot\': \'a\',
             \'sequence\': [[\'a\'], [\'b\', \'c\', \'d\', \'e\', \'f\'], [\'g\']],
             \'slice\': [\'a\', \'b\', \'c\', \'d\', \'e\', \'f\', \'g\']}
            sage: SD.xslice_data(\'u\')
            {\'active_edges\': [],
             \'lexicographic_label\': [\'a\', \'b\', \'c\', \'d\', \'e\', \'f\', \'g\'],
             \'pivot\': \'u\',
             \'sequence\': [[\'u\'], [\'y\', \'z\']],
             \'slice\': [\'u\', \'y\', \'z\']}

        Some values of the returned dictionary can be obtained via other
        methods (:meth:`~slice`, :meth:`~xslice_sequence`,
        :meth:`~active_edges`, :meth:`~lexicographic_label`)::

            sage: SD.slice(\'a\')
            [\'a\', \'b\', \'c\', \'d\', \'e\', \'f\', \'g\']
            sage: SD.xslice_data(\'a\')[\'slice\']
            [\'a\', \'b\', \'c\', \'d\', \'e\', \'f\', \'g\']

            sage: SD.xslice_sequence(\'a\')
            [[\'a\'], [\'b\', \'c\', \'d\', \'e\', \'f\'], [\'g\']]
            sage: SD.xslice_data(\'a\')[\'sequence\']
            [[\'a\'], [\'b\', \'c\', \'d\', \'e\', \'f\'], [\'g\']]

            sage: SD.active_edges(\'b\') == SD.xslice_data(\'b\')[\'active_edges\']
            True

            sage: SD.lexicographic_label(\'u\')
            [\'a\', \'b\', \'c\', \'d\', \'e\', \'f\', \'g\']
            sage: SD.xslice_data(\'u\')[\'lexicographic_label\']
            [\'a\', \'b\', \'c\', \'d\', \'e\', \'f\', \'g\']

        TESTS::

            sage: G = graphs.RandomGNP(15, 0.3)
            sage: SD = G.slice_decomposition()
            sage: all(SD[v][\'slice\'] == SD.slice(v) for v in G)
            True
            sage: all(SD[v][\'sequence\'] == SD.xslice_sequence(v) for v in G)
            True
            sage: all(SD[v][\'active_edges\'] == SD.active_edges(v) for v in G)
            True
            sage: all(SD[v][\'lexicographic_label\'] == SD.lexicographic_label(v) for v in G)
            True

            sage: SD = graphs.PetersenGraph().slice_decomposition()
            sage: SD[\'John\']
            Traceback (most recent call last):
            ...
            LookupError: vertex (John) does not appear in the slice decomposition'''
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __hash__(self) -> Any:
        """SliceDecomposition.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/slice_decomposition.pyx (starting at line 481)

        Compute a hash of a ``SliceDecomposition`` object.

        TESTS::

            sage: P3 = graphs.PathGraph(3)
            sage: SD1 = P3.slice_decomposition(initial_vertex=0)
            sage: SD2 = P3.slice_decomposition(initial_vertex=2)
            sage: len({SD1: 1, SD2: 2})  # indirect doctest
            2"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
