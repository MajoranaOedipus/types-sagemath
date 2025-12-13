import sage.graphs.base.c_graph
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from typing import Any, ClassVar, overload

class StaticSparseBackend(sage.graphs.base.c_graph.CGraphBackend):
    """StaticSparseBackend(G, loops=False, multiedges=False, sort=True)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, G, loops=..., multiedges=..., sort=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/graphs/base/static_sparse_backend.pyx (starting at line 430)

                A graph :mod:`backend <sage.graphs.base.graph_backends>` for static
                sparse graphs.

                EXAMPLES::

                    sage: D = sage.graphs.base.sparse_graph.SparseGraphBackend(9)
                    sage: D.add_edge(0, 1, None, False)
                    sage: list(D.iterator_edges(range(9), True))
                    [(0, 1, None)]

                ::

                    sage: from sage.graphs.base.static_sparse_backend import StaticSparseBackend
                    sage: g = StaticSparseBackend(graphs.PetersenGraph())
                    sage: list(g.iterator_edges([0], 1))
                    [(0, 1, None), (0, 4, None), (0, 5, None)]

                ::

                    sage: # needs sage.combinat
                    sage: g = DiGraph(digraphs.DeBruijn(4, 3), data_structure='static_sparse')
                    sage: gi = DiGraph(g, data_structure='static_sparse')
                    sage: gi.edges(sort=True)[0]
                    ('000', '000', '0')
                    sage: sorted(gi.edges_incident('111'))
                    [('111', '110', '0'),
                    ('111', '111', '1'),
                    ('111', '112', '2'),
                    ('111', '113', '3')]

                    sage: set(g.edges(sort=False)) == set(gi.edges(sort=False))                 # needs sage.combinat
                    True

                ::

                    sage: g = graphs.PetersenGraph()
                    sage: gi = Graph(g, data_structure='static_sparse')
                    sage: g == gi
                    True
                    sage: set(g.edges(sort=False)) == set(gi.edges(sort=False))
                    True

                ::

                    sage: gi = Graph({ 0: {1: 1}, 1: {2: 1}, 2: {3: 1}, 3: {4: 2}, 4: {0: 2}}, data_structure='static_sparse')
                    sage: (0, 4, 2) in gi.edges(sort=False)
                    True
                    sage: gi.has_edge(0, 4)
                    True

                ::

                    sage: G = Graph({1:{2:28, 6:10}, 2:{3:16, 7:14}, 3:{4:12}, 4:{5:22, 7:18}, 5:{6:25, 7:24}})
                    sage: GI = Graph({1:{2:28, 6:10}, 2:{3:16, 7:14}, 3:{4:12}, 4:{5:22, 7:18}, 5:{6:25, 7:24}}, data_structure='static_sparse')
                    sage: G == GI
                    True

                ::

                    sage: G = graphs.OddGraph(4)
                    sage: d = G.diameter()
                    sage: H = G.distance_graph(list(range(d + 1)))
                    sage: HI = Graph(H, data_structure='static_sparse')
                    sage: HI.size() == len(HI.edges(sort=False))
                    True

                ::

                    sage: g = Graph({1: {1: [1, 2, 3]}}, data_structure='static_sparse')
                    sage: g.size()
                    3
                    sage: g.order()
                    1
                    sage: g.vertices(sort=False)
                    [1]
                    sage: g.edges(sort=True)
                    [(1, 1, 1), (1, 1, 2), (1, 1, 3)]

                :issue:`15810` is fixed::

                    sage: DiGraph({1: {2: ['a', 'b'], 3: ['c']}, 2: {3: ['d']}}, immutable=True).is_directed_acyclic()
                    True
        """
    def add_edge(self, u, v, l, booldirected) -> Any:
        """StaticSparseBackend.add_edge(self, u, v, l, bool directed)

        File: /build/sagemath/src/sage/src/sage/graphs/base/static_sparse_backend.pyx (starting at line 581)

        Add an edge to the graph. No way.

        TESTS::

            sage: from sage.graphs.base.static_sparse_backend import StaticSparseBackend
            sage: g = StaticSparseBackend(graphs.PetersenGraph())
            sage: g.add_edge(1,2,3,True)
            Traceback (most recent call last):
            ...
            ValueError: graph is immutable; please change a copy instead (use function copy())"""
    def add_edges(self, edges, directed, remove_loops=...) -> Any:
        """StaticSparseBackend.add_edges(self, edges, directed, remove_loops=False)

        File: /build/sagemath/src/sage/src/sage/graphs/base/static_sparse_backend.pyx (starting at line 596)

        Add edges to the graph. No way.

        INPUT:

        - ``edges`` -- a list of edges (or not?)

        TESTS::

            sage: from sage.graphs.base.static_sparse_backend import StaticSparseBackend
            sage: g = StaticSparseBackend(graphs.PetersenGraph())
            sage: g.add_edges([[1, 2]], True)
            Traceback (most recent call last):
            ...
            ValueError: graph is immutable; please change a copy instead (use function copy())"""
    def add_vertex(self, v) -> Any:
        """StaticSparseBackend.add_vertex(self, v)

        File: /build/sagemath/src/sage/src/sage/graphs/base/static_sparse_backend.pyx (starting at line 562)

        Add a vertex to the graph. No way

        INPUT:

        - ``v`` -- a vertex (or not?)

        TESTS::

            sage: from sage.graphs.base.static_sparse_backend import StaticSparseBackend
            sage: g = StaticSparseBackend(graphs.PetersenGraph())
            sage: g.add_vertex(123)
            Traceback (most recent call last):
            ...
            ValueError: graph is immutable; please change a copy instead (use function copy())"""
    def add_vertices(self, vertices) -> Any:
        """StaticSparseBackend.add_vertices(self, vertices)

        File: /build/sagemath/src/sage/src/sage/graphs/base/static_sparse_backend.pyx (starting at line 615)

        Add vertices to the graph. No way.

        INPUT:

        - ``vertices`` -- a list of vertices (or not?)

        TESTS::

            sage: from sage.graphs.base.static_sparse_backend import StaticSparseBackend
            sage: g = StaticSparseBackend(graphs.PetersenGraph())
            sage: g.add_vertices([1, 2])
            Traceback (most recent call last):
            ...
            ValueError: graph is immutable; please change a copy instead (use function copy())"""
    @overload
    def allows_loops(self, value=...) -> Any:
        """StaticSparseBackend.allows_loops(self, value=None)

        File: /build/sagemath/src/sage/src/sage/graphs/base/static_sparse_backend.pyx (starting at line 996)

        Return whether the graph allows loops.

        INPUT:

        - ``value`` -- only useful for compatibility with other graph backends,
          where this method can be used to define this boolean. This method
          raises an exception if ``value`` is not equal to ``None``.

        TESTS::

            sage: from sage.graphs.base.static_sparse_backend import StaticSparseBackend
            sage: g = StaticSparseBackend(graphs.PetersenGraph())
            sage: g.allows_loops()
            False
            sage: g = StaticSparseBackend(graphs.PetersenGraph(), loops=True)
            sage: g.allows_loops()
            True"""
    @overload
    def allows_loops(self) -> Any:
        """StaticSparseBackend.allows_loops(self, value=None)

        File: /build/sagemath/src/sage/src/sage/graphs/base/static_sparse_backend.pyx (starting at line 996)

        Return whether the graph allows loops.

        INPUT:

        - ``value`` -- only useful for compatibility with other graph backends,
          where this method can be used to define this boolean. This method
          raises an exception if ``value`` is not equal to ``None``.

        TESTS::

            sage: from sage.graphs.base.static_sparse_backend import StaticSparseBackend
            sage: g = StaticSparseBackend(graphs.PetersenGraph())
            sage: g.allows_loops()
            False
            sage: g = StaticSparseBackend(graphs.PetersenGraph(), loops=True)
            sage: g.allows_loops()
            True"""
    @overload
    def allows_loops(self) -> Any:
        """StaticSparseBackend.allows_loops(self, value=None)

        File: /build/sagemath/src/sage/src/sage/graphs/base/static_sparse_backend.pyx (starting at line 996)

        Return whether the graph allows loops.

        INPUT:

        - ``value`` -- only useful for compatibility with other graph backends,
          where this method can be used to define this boolean. This method
          raises an exception if ``value`` is not equal to ``None``.

        TESTS::

            sage: from sage.graphs.base.static_sparse_backend import StaticSparseBackend
            sage: g = StaticSparseBackend(graphs.PetersenGraph())
            sage: g.allows_loops()
            False
            sage: g = StaticSparseBackend(graphs.PetersenGraph(), loops=True)
            sage: g.allows_loops()
            True"""
    def degree(self, v, directed) -> Any:
        """StaticSparseBackend.degree(self, v, directed)

        File: /build/sagemath/src/sage/src/sage/graphs/base/static_sparse_backend.pyx (starting at line 1290)

        Return the degree of a vertex.

        INPUT:

        - ``v`` -- a vertex

        - ``directed`` -- boolean; whether to take into account the orientation
          of this graph in counting the degree of ``v``

        EXAMPLES::

            sage: g = Graph(graphs.PetersenGraph(), data_structure='static_sparse')
            sage: g.degree(0)
            3

        :issue:`17225` about the degree of a vertex with a loop::

            sage: Graph({0: [0]}, immutable=True).degree(0)
            2
            sage: Graph({0: [0], 1: [0, 1, 1, 1]}, immutable=True).degree(1)
            7"""
    def del_edge(self, u, v, l, booldirected) -> Any:
        """StaticSparseBackend.del_edge(self, u, v, l, bool directed)

        File: /build/sagemath/src/sage/src/sage/graphs/base/static_sparse_backend.pyx (starting at line 679)

        Delete an edge of the graph. No way.

        TESTS::

            sage: from sage.graphs.base.static_sparse_backend import StaticSparseBackend
            sage: g = StaticSparseBackend(graphs.PetersenGraph())
            sage: g.del_edge(1,2,3,True)
            Traceback (most recent call last):
            ...
            ValueError: graph is immutable; please change a copy instead (use function copy())"""
    def del_edges(self, edges, directed) -> Any:
        """StaticSparseBackend.del_edges(self, edges, directed)

        File: /build/sagemath/src/sage/src/sage/graphs/base/static_sparse_backend.pyx (starting at line 694)

        Delete edges of the graph. No way.

        TESTS::

            sage: from sage.graphs.base.static_sparse_backend import StaticSparseBackend
            sage: g = StaticSparseBackend(graphs.PetersenGraph())
            sage: g.del_edges([[1,2,3]], True)
            Traceback (most recent call last):
            ...
            ValueError: graph is immutable; please change a copy instead (use function copy())"""
    def del_vertex(self, v) -> Any:
        """StaticSparseBackend.del_vertex(self, v)

        File: /build/sagemath/src/sage/src/sage/graphs/base/static_sparse_backend.pyx (starting at line 634)

        Delete a vertex from the graph. No way

        INPUT:

        - ``v`` -- a vertex (or not?)

        TESTS::

            sage: from sage.graphs.base.static_sparse_backend import StaticSparseBackend
            sage: g = StaticSparseBackend(graphs.PetersenGraph())
            sage: g.del_vertex(123)
            Traceback (most recent call last):
            ...
            ValueError: graph is immutable; please change a copy instead (use function copy())

        Check that :issue:`39270` is fixed::

            sage: g.del_vertex('a')
            Traceback (most recent call last):
            ...
            ValueError: graph is immutable; please change a copy instead (use function copy())"""
    def del_vertices(self, vertices) -> Any:
        """StaticSparseBackend.del_vertices(self, vertices)

        File: /build/sagemath/src/sage/src/sage/graphs/base/static_sparse_backend.pyx (starting at line 660)

        Delete vertices from the graph. No way

        INPUT:

        - ``vertices`` -- a list of vertices (or not?)

        TESTS::

            sage: from sage.graphs.base.static_sparse_backend import StaticSparseBackend
            sage: g = StaticSparseBackend(graphs.PetersenGraph())
            sage: g.del_vertices([123, 234])
            Traceback (most recent call last):
            ...
            ValueError: graph is immutable; please change a copy instead (use function copy())"""
    def get_edge_label(self, u, v) -> Any:
        '''StaticSparseBackend.get_edge_label(self, u, v)

        File: /build/sagemath/src/sage/src/sage/graphs/base/static_sparse_backend.pyx (starting at line 739)

        Return the edge label for ``(u, v)``.

        INPUT:

        - ``u``, ``v`` -- two vertices

        TESTS::

            sage: from sage.graphs.base.static_sparse_backend import StaticSparseBackend
            sage: g = StaticSparseBackend(graphs.PetersenGraph())
            sage: print(g.get_edge_label(0, 1))
            None
            sage: print(g.get_edge_label(0, "Hey"))
            Traceback (most recent call last):
            ...
            LookupError: one of the two vertices does not belong to the graph
            sage: print(g.get_edge_label(0, 7))
            Traceback (most recent call last):
            ...
            LookupError: the edge does not exist

        ::

            sage: from sage.graphs.base.static_sparse_backend import StaticSparseBackend
            sage: g = StaticSparseBackend(digraphs.DeBruijn(3, 2))                      # needs sage.combinat
            sage: g.has_edge(\'00\', \'01\', \'1\')                                           # needs sage.combinat
            True
            sage: g.has_edge(\'00\', \'01\', \'0\')                                           # needs sage.combinat
            False'''
    def has_edge(self, u, v, l) -> Any:
        """StaticSparseBackend.has_edge(self, u, v, l)

        File: /build/sagemath/src/sage/src/sage/graphs/base/static_sparse_backend.pyx (starting at line 811)

        Return whether this graph has edge ``(u, v)`` with label ``l``.

        If ``l`` is ``None``, return whether this graph has an edge ``(u, v)``
        with any label.

        INPUT:

        - ``u``, ``v`` -- two vertices

        - ``l`` -- a label

        TESTS::

            sage: from sage.graphs.base.static_sparse_backend import StaticSparseBackend
            sage: g = StaticSparseBackend(graphs.PetersenGraph())
            sage: g.has_edge(0, 1, 'e')
            False
            sage: g.has_edge(0, 4, None)
            True"""
    def has_vertex(self, v) -> Any:
        '''StaticSparseBackend.has_vertex(self, v)

        File: /build/sagemath/src/sage/src/sage/graphs/base/static_sparse_backend.pyx (starting at line 543)

        Test if the vertex belongs to the graph.

        INPUT:

        - ``v`` -- a vertex (or not?)

        TESTS::

            sage: from sage.graphs.base.static_sparse_backend import StaticSparseBackend
            sage: g = StaticSparseBackend(graphs.PetersenGraph())
            sage: g.has_vertex(0)
            True
            sage: g.has_vertex("Hey")
            False'''
    def in_degree(self, v) -> Any:
        """StaticSparseBackend.in_degree(self, v)

        File: /build/sagemath/src/sage/src/sage/graphs/base/static_sparse_backend.pyx (starting at line 1335)

        Return the in-degree of a vertex.

        INPUT:

        - ``v`` -- a vertex

        EXAMPLES::

            sage: g = DiGraph(graphs.PetersenGraph(), data_structure='static_sparse')
            sage: g.in_degree(0)
            3"""
    def iterator_edges(self, vertices, boollabels) -> Any:
        """StaticSparseBackend.iterator_edges(self, vertices, bool labels)

        File: /build/sagemath/src/sage/src/sage/graphs/base/static_sparse_backend.pyx (starting at line 1098)

        Iterate over the graph's edges.

        INPUT:

        - ``vertices`` -- list; only returns the edges incident to at least one
          vertex of ``vertices``

        - ``labels`` -- boolean; whether to return edge labels too

        TESTS::

            sage: from sage.graphs.base.static_sparse_backend import StaticSparseBackend
            sage: g = StaticSparseBackend(graphs.PetersenGraph())
            sage: list(g.iterator_edges(g.iterator_verts(None), False))
            [(0, 1), (0, 4), (0, 5), (1, 2), (1, 6), (2, 3), (2, 7),
            (3, 4), (3, 8), (4, 9), (5, 7), (5, 8), (6, 8), (6, 9), (7, 9)]

        :issue:`15665`::

            sage: Graph(immutable=True).edges(sort=False)
            []"""
    def iterator_in_edges(self, vertices, boollabels) -> Any:
        """StaticSparseBackend.iterator_in_edges(self, vertices, bool labels)

        File: /build/sagemath/src/sage/src/sage/graphs/base/static_sparse_backend.pyx (starting at line 868)

        Iterate over the incoming edges incident to a sequence of vertices.

        INPUT:

        - ``vertices`` -- list of vertices

        - ``labels`` -- whether to return labels too

        TESTS::

            sage: from sage.graphs.base.static_sparse_backend import StaticSparseBackend
            sage: g = StaticSparseBackend(graphs.PetersenGraph())
            sage: list(g.iterator_in_edges([0], False))
            [(0, 1), (0, 4), (0, 5)]
            sage: list(g.iterator_in_edges([0], True))
            [(0, 1, None), (0, 4, None), (0, 5, None)]

        ::

            sage: DiGraph(digraphs.Path(5), immutable=False).incoming_edges([2])
            [(1, 2, None)]
            sage: DiGraph(digraphs.Path(5), immutable=True).incoming_edges([2])
            [(1, 2, None)]"""
    def iterator_in_nbrs(self, v) -> Any:
        """StaticSparseBackend.iterator_in_nbrs(self, v)

        File: /build/sagemath/src/sage/src/sage/graphs/base/static_sparse_backend.pyx (starting at line 1470)

        Iterate over the in-neighbors of a vertex.

        INPUT:

        - ``v`` -- a vertex

        EXAMPLES::

            sage: g = DiGraph(graphs.PetersenGraph(), data_structure='static_sparse')
            sage: g.neighbors_in(0)
            [1, 4, 5]

        TESTS::

            sage: g = DiGraph({0: [1]}, immutable=True)
            sage: print(g.neighbors_in(1))
            [0]"""
    def iterator_nbrs(self, v) -> Any:
        """StaticSparseBackend.iterator_nbrs(self, v)

        File: /build/sagemath/src/sage/src/sage/graphs/base/static_sparse_backend.pyx (starting at line 1384)

        Iterate over the neighbors of a vertex.

        INPUT:

        - ``v`` -- a vertex

        EXAMPLES::

            sage: g = Graph(graphs.PetersenGraph(), data_structure='static_sparse')
            sage: g.neighbors(0)
            [1, 4, 5]

        TESTS:

        Issue :issue:`25550` is fixed::

            sage: g = DiGraph({0: [1]}, immutable=True)
            sage: g.neighbors(1)
            [0]
            sage: g = DiGraph({0: [0, 1, 1]}, loops=True, multiedges=True, immutable=True)
            sage: g.neighbors(0)
            [0, 1]
            sage: g = DiGraph({0: [1, 1], 1:[0, 0]}, multiedges=True, immutable=True)
            sage: g.neighbors(0)
            [1]
            sage: g.neighbors(1)
            [0]"""
    def iterator_out_edges(self, vertices, boollabels) -> Any:
        """StaticSparseBackend.iterator_out_edges(self, vertices, bool labels)

        File: /build/sagemath/src/sage/src/sage/graphs/base/static_sparse_backend.pyx (starting at line 916)

        Iterate over the outbound edges incident to a sequence of vertices.

        INPUT:

        - ``vertices`` -- list of vertices

        - ``labels`` -- whether to return labels too

        TESTS::

            sage: from sage.graphs.base.static_sparse_backend import StaticSparseBackend
            sage: g = StaticSparseBackend(graphs.PetersenGraph())
            sage: list(g.iterator_out_edges([0], False))
            [(0, 1), (0, 4), (0, 5)]
            sage: list(g.iterator_out_edges([0], True))
            [(0, 1, None), (0, 4, None), (0, 5, None)]"""
    def iterator_out_nbrs(self, v) -> Any:
        """StaticSparseBackend.iterator_out_nbrs(self, v)

        File: /build/sagemath/src/sage/src/sage/graphs/base/static_sparse_backend.pyx (starting at line 1441)

        Iterate over the out-neighbors of a vertex.

        INPUT:

        - ``v`` -- a vertex

        EXAMPLES::

            sage: g = DiGraph(graphs.PetersenGraph(), data_structure='static_sparse')
            sage: g.neighbors_out(0)
            [1, 4, 5]"""
    def iterator_unsorted_edges(self, *args, **kwargs):
        """StaticSparseBackend.iterator_edges(self, vertices, bool labels)

        File: /build/sagemath/src/sage/src/sage/graphs/base/static_sparse_backend.pyx (starting at line 1098)

        Iterate over the graph's edges.

        INPUT:

        - ``vertices`` -- list; only returns the edges incident to at least one
          vertex of ``vertices``

        - ``labels`` -- boolean; whether to return edge labels too

        TESTS::

            sage: from sage.graphs.base.static_sparse_backend import StaticSparseBackend
            sage: g = StaticSparseBackend(graphs.PetersenGraph())
            sage: list(g.iterator_edges(g.iterator_verts(None), False))
            [(0, 1), (0, 4), (0, 5), (1, 2), (1, 6), (2, 3), (2, 7),
            (3, 4), (3, 8), (4, 9), (5, 7), (5, 8), (6, 8), (6, 9), (7, 9)]

        :issue:`15665`::

            sage: Graph(immutable=True).edges(sort=False)
            []"""
    def iterator_verts(self, vertices) -> Any:
        '''StaticSparseBackend.iterator_verts(self, vertices)

        File: /build/sagemath/src/sage/src/sage/graphs/base/static_sparse_backend.pyx (starting at line 952)

        Iterate over the vertices.

        INPUT:

        - ``vertices`` -- list of objects; the method will only return the
          elements of the graph which are contained in ``vertices``. It\'s not
          very efficient. If ``vertices`` is equal to ``None``, all the vertices
          are returned.

        TESTS::

            sage: from sage.graphs.base.static_sparse_backend import StaticSparseBackend
            sage: g = StaticSparseBackend(graphs.PetersenGraph())
            sage: list(g.iterator_verts(None))
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            sage: list(g.iterator_verts([1, "Hey", "I am a french fry"]))
            [1]'''
    @overload
    def multiple_edges(self, value=...) -> Any:
        """StaticSparseBackend.multiple_edges(self, value=None)

        File: /build/sagemath/src/sage/src/sage/graphs/base/static_sparse_backend.pyx (starting at line 1021)

        Return whether the graph allows multiple edges.

        INPUT:

        - ``value`` -- only useful for compatibility with other graph backends,
          where this method can be used to define this boolean. This method
          raises an exception if ``value`` is not equal to ``None``.

        TESTS::

            sage: from sage.graphs.base.static_sparse_backend import StaticSparseBackend
            sage: g = StaticSparseBackend(graphs.PetersenGraph())
            sage: g.multiple_edges()
            False
            sage: g = StaticSparseBackend(graphs.PetersenGraph(), multiedges=True)
            sage: g.multiple_edges()
            True"""
    @overload
    def multiple_edges(self) -> Any:
        """StaticSparseBackend.multiple_edges(self, value=None)

        File: /build/sagemath/src/sage/src/sage/graphs/base/static_sparse_backend.pyx (starting at line 1021)

        Return whether the graph allows multiple edges.

        INPUT:

        - ``value`` -- only useful for compatibility with other graph backends,
          where this method can be used to define this boolean. This method
          raises an exception if ``value`` is not equal to ``None``.

        TESTS::

            sage: from sage.graphs.base.static_sparse_backend import StaticSparseBackend
            sage: g = StaticSparseBackend(graphs.PetersenGraph())
            sage: g.multiple_edges()
            False
            sage: g = StaticSparseBackend(graphs.PetersenGraph(), multiedges=True)
            sage: g.multiple_edges()
            True"""
    @overload
    def multiple_edges(self) -> Any:
        """StaticSparseBackend.multiple_edges(self, value=None)

        File: /build/sagemath/src/sage/src/sage/graphs/base/static_sparse_backend.pyx (starting at line 1021)

        Return whether the graph allows multiple edges.

        INPUT:

        - ``value`` -- only useful for compatibility with other graph backends,
          where this method can be used to define this boolean. This method
          raises an exception if ``value`` is not equal to ``None``.

        TESTS::

            sage: from sage.graphs.base.static_sparse_backend import StaticSparseBackend
            sage: g = StaticSparseBackend(graphs.PetersenGraph())
            sage: g.multiple_edges()
            False
            sage: g = StaticSparseBackend(graphs.PetersenGraph(), multiedges=True)
            sage: g.multiple_edges()
            True"""
    @overload
    def num_edges(self, directed) -> Any:
        """StaticSparseBackend.num_edges(self, directed)

        File: /build/sagemath/src/sage/src/sage/graphs/base/static_sparse_backend.pyx (starting at line 1046)

        Return the number of edges.

        INPUT:

        - ``directed`` -- boolean; whether to consider the graph as directed or
          not

        TESTS::

            sage: from sage.graphs.base.static_sparse_backend import StaticSparseBackend
            sage: g = StaticSparseBackend(graphs.PetersenGraph())
            sage: g.num_edges(False)
            15

        Testing the exception::

            sage: g = StaticSparseBackend(digraphs.Circuit(4))
            sage: g.num_edges(False)
            Traceback (most recent call last):
            ...
            NotImplementedError: Sorry, I have no idea what is expected in this situation. I don't think that it is well-defined either, especially for multigraphs.

        :issue:`15491`::

            sage: g = digraphs.RandomDirectedGNP(10, .3)
            sage: gi = DiGraph(g, data_structure='static_sparse')
            sage: gi.size() == len(gi.edges(sort=False))
            True"""
    @overload
    def num_edges(self, _False) -> Any:
        """StaticSparseBackend.num_edges(self, directed)

        File: /build/sagemath/src/sage/src/sage/graphs/base/static_sparse_backend.pyx (starting at line 1046)

        Return the number of edges.

        INPUT:

        - ``directed`` -- boolean; whether to consider the graph as directed or
          not

        TESTS::

            sage: from sage.graphs.base.static_sparse_backend import StaticSparseBackend
            sage: g = StaticSparseBackend(graphs.PetersenGraph())
            sage: g.num_edges(False)
            15

        Testing the exception::

            sage: g = StaticSparseBackend(digraphs.Circuit(4))
            sage: g.num_edges(False)
            Traceback (most recent call last):
            ...
            NotImplementedError: Sorry, I have no idea what is expected in this situation. I don't think that it is well-defined either, especially for multigraphs.

        :issue:`15491`::

            sage: g = digraphs.RandomDirectedGNP(10, .3)
            sage: gi = DiGraph(g, data_structure='static_sparse')
            sage: gi.size() == len(gi.edges(sort=False))
            True"""
    @overload
    def num_edges(self, _False) -> Any:
        """StaticSparseBackend.num_edges(self, directed)

        File: /build/sagemath/src/sage/src/sage/graphs/base/static_sparse_backend.pyx (starting at line 1046)

        Return the number of edges.

        INPUT:

        - ``directed`` -- boolean; whether to consider the graph as directed or
          not

        TESTS::

            sage: from sage.graphs.base.static_sparse_backend import StaticSparseBackend
            sage: g = StaticSparseBackend(graphs.PetersenGraph())
            sage: g.num_edges(False)
            15

        Testing the exception::

            sage: g = StaticSparseBackend(digraphs.Circuit(4))
            sage: g.num_edges(False)
            Traceback (most recent call last):
            ...
            NotImplementedError: Sorry, I have no idea what is expected in this situation. I don't think that it is well-defined either, especially for multigraphs.

        :issue:`15491`::

            sage: g = digraphs.RandomDirectedGNP(10, .3)
            sage: gi = DiGraph(g, data_structure='static_sparse')
            sage: gi.size() == len(gi.edges(sort=False))
            True"""
    @overload
    def num_verts(self) -> Any:
        """StaticSparseBackend.num_verts(self)

        File: /build/sagemath/src/sage/src/sage/graphs/base/static_sparse_backend.pyx (starting at line 983)

        Return the number of vertices.

        TESTS::

            sage: from sage.graphs.base.static_sparse_backend import StaticSparseBackend
            sage: g = StaticSparseBackend(graphs.PetersenGraph())
            sage: g.num_verts()
            10"""
    @overload
    def num_verts(self) -> Any:
        """StaticSparseBackend.num_verts(self)

        File: /build/sagemath/src/sage/src/sage/graphs/base/static_sparse_backend.pyx (starting at line 983)

        Return the number of vertices.

        TESTS::

            sage: from sage.graphs.base.static_sparse_backend import StaticSparseBackend
            sage: g = StaticSparseBackend(graphs.PetersenGraph())
            sage: g.num_verts()
            10"""
    def out_degree(self, v) -> Any:
        """StaticSparseBackend.out_degree(self, v)

        File: /build/sagemath/src/sage/src/sage/graphs/base/static_sparse_backend.pyx (starting at line 1361)

        Return the out-degree of a vertex.

        INPUT:

        - ``v`` -- a vertex

        EXAMPLES::

            sage: g = DiGraph(graphs.PetersenGraph(), data_structure='static_sparse')
            sage: g.out_degree(0)
            3"""
    def relabel(self, perm, directed) -> Any:
        """StaticSparseBackend.relabel(self, perm, directed)

        File: /build/sagemath/src/sage/src/sage/graphs/base/static_sparse_backend.pyx (starting at line 724)

        Relabel the graphs' vertices. No way.

        TESTS::

            sage: from sage.graphs.base.static_sparse_backend import StaticSparseBackend
            sage: g = StaticSparseBackend(graphs.PetersenGraph())
            sage: g.relabel([],True)
            Traceback (most recent call last):
            ...
            ValueError: graph is immutable; please change a copy instead (use function copy())"""
    def set_edge_label(self, u, v, l, directed) -> Any:
        """StaticSparseBackend.set_edge_label(self, u, v, l, directed)

        File: /build/sagemath/src/sage/src/sage/graphs/base/static_sparse_backend.pyx (starting at line 709)

        Set edge label. No way.

        TESTS::

            sage: from sage.graphs.base.static_sparse_backend import StaticSparseBackend
            sage: g = StaticSparseBackend(graphs.PetersenGraph())
            sage: g.set_edge_label(1,2,3,True)
            Traceback (most recent call last):
            ...
            ValueError: graph is immutable; please change a copy instead (use function copy())"""

class StaticSparseCGraph(sage.graphs.base.c_graph.CGraph):
    """File: /build/sagemath/src/sage/src/sage/graphs/base/static_sparse_backend.pyx (starting at line 55)

        :mod:`CGraph <sage.graphs.base.c_graph>` class based on the sparse graph
        data structure :mod:`static sparse graphs
        <sage.graphs.base.static_sparse_graph>`.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def add_vertex(self, intk) -> Any:
        """StaticSparseCGraph.add_vertex(self, int k)

        File: /build/sagemath/src/sage/src/sage/graphs/base/static_sparse_backend.pyx (starting at line 187)

        Add a vertex to the graph. No way.

        TESTS::

            sage: from sage.graphs.base.static_sparse_backend import StaticSparseCGraph
            sage: g = StaticSparseCGraph(graphs.PetersenGraph())
            sage: g.add_vertex(45)
            Traceback (most recent call last):
            ...
            ValueError: graph is immutable; please change a copy instead (use function copy())"""
    def del_vertex(self, intk) -> Any:
        """StaticSparseCGraph.del_vertex(self, int k)

        File: /build/sagemath/src/sage/src/sage/graphs/base/static_sparse_backend.pyx (starting at line 202)

        Remove a vertex from the graph. No way.

        TESTS::

            sage: from sage.graphs.base.static_sparse_backend import StaticSparseCGraph
            sage: g = StaticSparseCGraph(graphs.PetersenGraph())
            sage: g.del_vertex(45)
            Traceback (most recent call last):
            ...
            ValueError: graph is immutable; please change a copy instead (use function copy())"""
    def has_arc(self, intu, intv) -> bool:
        """StaticSparseCGraph.has_arc(self, int u, int v) -> bool

        File: /build/sagemath/src/sage/src/sage/graphs/base/static_sparse_backend.pyx (starting at line 240)

        Test if `uv` is an edge of the graph

        INPUT:

        - ``u``, ``v`` -- integers

        TESTS::

            sage: from sage.graphs.base.static_sparse_backend import StaticSparseCGraph
            sage: g = StaticSparseCGraph(graphs.PetersenGraph())
            sage: g.has_arc(0, 1)
            True
            sage: g.has_arc(0, 7)
            False"""
    def has_vertex(self, intv) -> bool:
        """StaticSparseCGraph.has_vertex(self, int v) -> bool

        File: /build/sagemath/src/sage/src/sage/graphs/base/static_sparse_backend.pyx (starting at line 162)

        Test if a vertex belongs to the graph

        INPUT:

        - ``n`` -- integer

        TESTS::

            sage: from sage.graphs.base.static_sparse_backend import StaticSparseCGraph
            sage: g = StaticSparseCGraph(graphs.PetersenGraph())
            sage: g.has_vertex(1)
            True
            sage: g.has_vertex(10)
            False"""
    def in_degree(self, intu) -> int:
        """StaticSparseCGraph.in_degree(self, int u) -> int

        File: /build/sagemath/src/sage/src/sage/graphs/base/static_sparse_backend.pyx (starting at line 401)

        Return the in-degree of a vertex

        INPUT:

        - ``u`` -- a vertex

        TESTS::

            sage: from sage.graphs.base.static_sparse_backend import StaticSparseCGraph
            sage: g = StaticSparseCGraph(graphs.PetersenGraph())
            sage: g.in_degree(0)
            3
            sage: g.in_degree(10)
            Traceback (most recent call last):
            ...
            LookupError: the vertex does not belong to the graph"""
    def in_neighbors(self, intu) -> list:
        """StaticSparseCGraph.in_neighbors(self, int u) -> list

        File: /build/sagemath/src/sage/src/sage/graphs/base/static_sparse_backend.pyx (starting at line 349)

        Return the in-neighbors of a vertex.

        INPUT:

        - ``u`` -- a vertex

        TESTS::

            sage: from sage.graphs.base.static_sparse_backend import StaticSparseCGraph
            sage: g = StaticSparseCGraph(graphs.PetersenGraph())
            sage: g.in_neighbors(0)
            [1, 4, 5]
            sage: g.in_neighbors(10)
            Traceback (most recent call last):
            ...
            LookupError: the vertex does not belong to the graph"""
    def out_degree(self, intu) -> int:
        """StaticSparseCGraph.out_degree(self, int u) -> int

        File: /build/sagemath/src/sage/src/sage/graphs/base/static_sparse_backend.pyx (starting at line 377)

        Return the out-degree of a vertex

        INPUT:

        - ``u`` -- a vertex

        TESTS::

            sage: from sage.graphs.base.static_sparse_backend import StaticSparseCGraph
            sage: g = StaticSparseCGraph(graphs.PetersenGraph())
            sage: g.out_degree(0)
            3
            sage: g.out_degree(10)
            Traceback (most recent call last):
            ...
            LookupError: the vertex does not belong to the graph"""
    def out_neighbors(self, intu) -> list:
        """StaticSparseCGraph.out_neighbors(self, int u) -> list

        File: /build/sagemath/src/sage/src/sage/graphs/base/static_sparse_backend.pyx (starting at line 324)

        List the out-neighbors of a vertex.

        INPUT:

        - ``u`` -- a vertex

        TESTS::

            sage: from sage.graphs.base.static_sparse_backend import StaticSparseCGraph
            sage: g = StaticSparseCGraph(graphs.PetersenGraph())
            sage: g.out_neighbors(0)
            [1, 4, 5]
            sage: g.out_neighbors(10)
            Traceback (most recent call last):
            ...
            LookupError: the vertex does not belong to the graph"""
    @overload
    def verts(self) -> list:
        """StaticSparseCGraph.verts(self) -> list

        File: /build/sagemath/src/sage/src/sage/graphs/base/static_sparse_backend.pyx (starting at line 217)

        Return the list of vertices.

        TESTS::

            sage: from sage.graphs.base.static_sparse_backend import StaticSparseCGraph
            sage: g = StaticSparseCGraph(graphs.PetersenGraph())
            sage: g.verts()
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]"""
    @overload
    def verts(self) -> Any:
        """StaticSparseCGraph.verts(self) -> list

        File: /build/sagemath/src/sage/src/sage/graphs/base/static_sparse_backend.pyx (starting at line 217)

        Return the list of vertices.

        TESTS::

            sage: from sage.graphs.base.static_sparse_backend import StaticSparseCGraph
            sage: g = StaticSparseCGraph(graphs.PetersenGraph())
            sage: g.verts()
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]"""
