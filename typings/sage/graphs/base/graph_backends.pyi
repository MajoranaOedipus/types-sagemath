import _cython_3_2_1
import sage.structure.sage_object
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from typing import Any, ClassVar, overload

unpickle_graph_backend: _cython_3_2_1.cython_function_or_method

class GenericGraphBackend(sage.structure.sage_object.SageObject):
    """File: /build/sagemath/src/sage/src/sage/graphs/base/graph_backends.pyx (starting at line 62)

        A generic wrapper for the backend of a graph.

        Various graph classes use extensions of this class.  Note, this graph has a
        number of placeholder functions, so the doctests are rather silly.

        TESTS::

            sage: import sage.graphs.base.graph_backends
    """
    _loops: ClassVar[bool] = ...
    _multiple_edges: ClassVar[bool] = ...
    _name: ClassVar[str] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def add_edge(self, u, v, l, directed) -> Any:
        """GenericGraphBackend.add_edge(self, u, v, l, directed)

        File: /build/sagemath/src/sage/src/sage/graphs/base/graph_backends.pyx (starting at line 77)

        Add an edge `(u,v)` to ``self``, with label `l`.

        If ``directed`` is ``True``, this is interpreted as an arc from `u` to
        `v`.

        INPUT:

        - ``u``, ``v`` -- vertices
        - ``l`` -- edge label
        - ``directed`` -- boolean

        TESTS::

            sage: G = sage.graphs.base.graph_backends.GenericGraphBackend()
            sage: G.add_edge(1,2,'a',True)
            Traceback (most recent call last):
            ...
            NotImplementedError
 """
    def add_edges(self, edges, directed) -> Any:
        """GenericGraphBackend.add_edges(self, edges, directed)

        File: /build/sagemath/src/sage/src/sage/graphs/base/graph_backends.pyx (starting at line 100)

        Add a sequence of edges to ``self``.

        If ``directed`` is ``True``, these are interpreted as arcs.

        INPUT:

        - ``edges`` -- list/iterator of edges to be added

        - ``directed`` -- boolean

        TESTS::

            sage: G = sage.graphs.base.graph_backends.GenericGraphBackend()
            sage: G.add_edges([],True)
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    def add_vertex(self, name) -> Any:
        """GenericGraphBackend.add_vertex(self, name)

        File: /build/sagemath/src/sage/src/sage/graphs/base/graph_backends.pyx (starting at line 122)

        Add a labelled vertex to ``self``.

        INPUT:

        - ``name`` -- vertex label

        OUTPUT: if ``name=None``, the new vertex name is returned, ``None`` otherwise

        TESTS::

            sage: G = sage.graphs.base.graph_backends.GenericGraphBackend()
            sage: G.add_vertex(0)
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    def add_vertices(self, vertices) -> Any:
        """GenericGraphBackend.add_vertices(self, vertices)

        File: /build/sagemath/src/sage/src/sage/graphs/base/graph_backends.pyx (starting at line 142)

        Add labelled vertices to ``self``.

        INPUT:

        - ``vertices`` -- iterator of vertex labels; a new label is created,
          used and returned in the output list for all ``None`` values in
          ``vertices``

        OUTPUT:

        Generated names of new vertices if there is at least one ``None`` value
        present in ``vertices``. ``None`` otherwise.

        EXAMPLES::

            sage: G = sage.graphs.base.graph_backends.GenericGraphBackend()
            sage: G.add_vertices([1,2,3])
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    def degree(self, v, directed) -> Any:
        """GenericGraphBackend.degree(self, v, directed)

        File: /build/sagemath/src/sage/src/sage/graphs/base/graph_backends.pyx (starting at line 167)

        Return the total number of vertices incident to `v`.

        INPUT:

        - ``v`` -- a vertex label
        - ``directed`` -- boolean

        OUTPUT: degree of `v`

        TESTS::

            sage: G = sage.graphs.base.graph_backends.GenericGraphBackend()
            sage: G.degree(1, False)
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    def del_edge(self, u, v, l, directed) -> Any:
        """GenericGraphBackend.del_edge(self, u, v, l, directed)

        File: /build/sagemath/src/sage/src/sage/graphs/base/graph_backends.pyx (starting at line 224)

        Delete the edge `(u,v)` with label `l`.

        INPUT:

        - ``u``, ``v`` -- vertices
        - ``l`` -- edge label
        - ``directed`` -- boolean

        TESTS::

            sage: G = sage.graphs.base.graph_backends.GenericGraphBackend()
            sage: G.del_edge(1,2,'a',True)
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    def del_vertex(self, v) -> Any:
        """GenericGraphBackend.del_vertex(self, v)

        File: /build/sagemath/src/sage/src/sage/graphs/base/graph_backends.pyx (starting at line 244)

        Delete a labelled vertex in ``self``.

        INPUT:

        - ``v`` -- vertex label

        TESTS::

            sage: G = sage.graphs.base.graph_backends.GenericGraphBackend()
            sage: G.del_vertex(0)
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    def del_vertices(self, vertices) -> Any:
        """GenericGraphBackend.del_vertices(self, vertices)

        File: /build/sagemath/src/sage/src/sage/graphs/base/graph_backends.pyx (starting at line 262)

        Delete labelled vertices in ``self``.

        INPUT:

        - ``vertices`` -- iterator of vertex labels

        TESTS::

            sage: G = sage.graphs.base.graph_backends.GenericGraphBackend()
            sage: G.del_vertices([1,2,3])
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    def get_edge_label(self, u, v) -> Any:
        """GenericGraphBackend.get_edge_label(self, u, v)

        File: /build/sagemath/src/sage/src/sage/graphs/base/graph_backends.pyx (starting at line 280)

        Return the edge label of `(u, v)`.

        INPUT:

        - ``u``, ``v`` -- vertex labels

        OUTPUT:

            label of `(u,v)`

        TESTS::

            sage: G = sage.graphs.base.graph_backends.GenericGraphBackend()
            sage: G.get_edge_label(1,2)
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    def has_edge(self, u, v, l) -> Any:
        """GenericGraphBackend.has_edge(self, u, v, l)

        File: /build/sagemath/src/sage/src/sage/graphs/base/graph_backends.pyx (starting at line 302)

        Check whether ``self`` has an edge `(u,v)` with label `l`.

        INPUT:

        - ``u``, ``v`` -- vertex labels
        - ``l`` -- label

        OUTPUT: boolean

        TESTS::

            sage: G = sage.graphs.base.graph_backends.GenericGraphBackend()
            sage: G.has_edge(1,2,'a')
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    def has_vertex(self, v) -> Any:
        """GenericGraphBackend.has_vertex(self, v)

        File: /build/sagemath/src/sage/src/sage/graphs/base/graph_backends.pyx (starting at line 323)

        Check whether ``self`` has a vertex with label `v`.

        INPUT:

        - ``v`` -- vertex label

        OUTPUT: boolean

        TESTS::

            sage: G = sage.graphs.base.graph_backends.GenericGraphBackend()
            sage: G.has_vertex(0)
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    def in_degree(self, v) -> Any:
        """GenericGraphBackend.in_degree(self, v)

        File: /build/sagemath/src/sage/src/sage/graphs/base/graph_backends.pyx (starting at line 188)

        Return the in-degree of `v`.

        INPUT:

        - ``v`` -- a vertex label

        TESTS::

            sage: G = sage.graphs.base.graph_backends.GenericGraphBackend()
            sage: G.in_degree(1)
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    def iterator_edges(self, vertices, labels) -> Any:
        """GenericGraphBackend.iterator_edges(self, vertices, labels)

        File: /build/sagemath/src/sage/src/sage/graphs/base/graph_backends.pyx (starting at line 343)

        Iterate over the edges incident to a sequence of vertices.

        Edges are assumed to be undirected.

        This method returns an iterator over the edges `(u, v)` such that either
        `u` or `v` is in ``vertices`` and the edge `(u, v)` is in ``self``.

        INPUT:

        - ``vertices`` -- list of vertex labels
        - ``labels`` -- boolean

        OUTPUT:

            a generator which yields edges, with or without labels
            depending on the labels parameter.

        TESTS::

            sage: G = sage.graphs.base.graph_backends.GenericGraphBackend()
            sage: G.iterator_edges([],True)
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    def iterator_in_edges(self, vertices, labels) -> Any:
        """GenericGraphBackend.iterator_in_edges(self, vertices, labels)

        File: /build/sagemath/src/sage/src/sage/graphs/base/graph_backends.pyx (starting at line 372)

        Iterate over the incoming edges incident to a sequence of vertices.

        This method returns an iterator over the edges `(u, v)` such that `v` is
        in ``vertices`` and the edge `(u, v)` is in ``self``.

        INPUT:

        - ``vertices`` -- list of vertex labels
        - ``labels`` -- boolean

        OUTPUT: a generator which yields edges, with or without labels
        depending on the labels parameter

        TESTS::

            sage: G = sage.graphs.base.graph_backends.GenericGraphBackend()
            sage: G.iterator_in_edges([],True)
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    def iterator_in_nbrs(self, v) -> Any:
        """GenericGraphBackend.iterator_in_nbrs(self, v)

        File: /build/sagemath/src/sage/src/sage/graphs/base/graph_backends.pyx (starting at line 448)

        Iterate over the in-neighbors of vertex `v`.

        This method returns an iterator over the vertices `u` such that the edge
        `(u, v)` is in ``self`` (that is, predecessors of `v`).

        INPUT:

        - ``v`` -- vertex label

        OUTPUT: a generator which yields vertex labels

        TESTS::

            sage: G = sage.graphs.base.graph_backends.GenericGraphBackend()
            sage: G.iterator_in_nbrs(0)
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    def iterator_nbrs(self, v) -> Any:
        """GenericGraphBackend.iterator_nbrs(self, v)

        File: /build/sagemath/src/sage/src/sage/graphs/base/graph_backends.pyx (starting at line 424)

        Iterate over the vertices adjacent to `v`.

        This method returns an iterator over the vertices `u` such that either
        the edge `(u, v)` or the edge `(v, u)` is in ``self`` (that is,
        neighbors of `v`).

        INPUT:

        - ``v`` -- vertex label

        OUTPUT: a generator which yields vertex labels

        TESTS::

            sage: G = sage.graphs.base.graph_backends.GenericGraphBackend()
            sage: G.iterator_nbrs(0)
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    def iterator_out_edges(self, vertices, labels) -> Any:
        """GenericGraphBackend.iterator_out_edges(self, vertices, labels)

        File: /build/sagemath/src/sage/src/sage/graphs/base/graph_backends.pyx (starting at line 397)

        Iterate over the outbound edges incident to a sequence of vertices.

        This method returns an iterator over the edges `(v, u)` such that `v` is
        in ``vertices`` and the edge `(v, u)` is in ``self``.

        INPUT:

        - ``vertices`` -- list of vertex labels
        - ``labels`` -- boolean

        OUTPUT:

            a generator which yields edges, with or without labels depending on
            the labels parameter.

        TESTS::

            sage: G = sage.graphs.base.graph_backends.GenericGraphBackend()
            sage: G.iterator_out_edges([],True)
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    def iterator_out_nbrs(self, v) -> Any:
        """GenericGraphBackend.iterator_out_nbrs(self, v)

        File: /build/sagemath/src/sage/src/sage/graphs/base/graph_backends.pyx (starting at line 471)

        Iterate over the out-neighbors of `v`.

        This method returns an iterator over the vertices `u` such that the edge
        `(v, u)` is in ``self`` (that is, successors of `v`).

        INPUT:

        - ``v`` -- vertex label

        OUTPUT: a generator which yields vertex labels

        TESTS::

            sage: G = sage.graphs.base.graph_backends.GenericGraphBackend()
            sage: G.iterator_out_nbrs(0)
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    def iterator_verts(self, verts) -> Any:
        """GenericGraphBackend.iterator_verts(self, verts)

        File: /build/sagemath/src/sage/src/sage/graphs/base/graph_backends.pyx (starting at line 494)

        Iterate over the vertices `v` with labels in ``verts``.

        INPUT:

        - ``verts`` -- vertex labels

        OUTPUT: a generator which yields vertices

        TESTS::

            sage: G = sage.graphs.base.graph_backends.GenericGraphBackend()
            sage: G.iterator_verts(0)
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def loops(self, new=...) -> Any:
        """GenericGraphBackend.loops(self, new=None)

        File: /build/sagemath/src/sage/src/sage/graphs/base/graph_backends.pyx (starting at line 514)

        Get/set whether or not ``self`` allows loops.

        INPUT:

        - ``new`` -- can be a boolean (in which case it sets the value) or
          ``None``, in which case the current value is returned. It is set to
          ``None`` by default.

        TESTS::

            sage: G = sage.graphs.base.graph_backends.GenericGraphBackend()
            sage: G.loops(True)
            Traceback (most recent call last):
            ...
            NotImplementedError
            sage: G.loops(None)
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def loops(self, _True) -> Any:
        """GenericGraphBackend.loops(self, new=None)

        File: /build/sagemath/src/sage/src/sage/graphs/base/graph_backends.pyx (starting at line 514)

        Get/set whether or not ``self`` allows loops.

        INPUT:

        - ``new`` -- can be a boolean (in which case it sets the value) or
          ``None``, in which case the current value is returned. It is set to
          ``None`` by default.

        TESTS::

            sage: G = sage.graphs.base.graph_backends.GenericGraphBackend()
            sage: G.loops(True)
            Traceback (most recent call last):
            ...
            NotImplementedError
            sage: G.loops(None)
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def loops(self, _None) -> Any:
        """GenericGraphBackend.loops(self, new=None)

        File: /build/sagemath/src/sage/src/sage/graphs/base/graph_backends.pyx (starting at line 514)

        Get/set whether or not ``self`` allows loops.

        INPUT:

        - ``new`` -- can be a boolean (in which case it sets the value) or
          ``None``, in which case the current value is returned. It is set to
          ``None`` by default.

        TESTS::

            sage: G = sage.graphs.base.graph_backends.GenericGraphBackend()
            sage: G.loops(True)
            Traceback (most recent call last):
            ...
            NotImplementedError
            sage: G.loops(None)
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def multiple_edges(self, new=...) -> Any:
        """GenericGraphBackend.multiple_edges(self, new=None)

        File: /build/sagemath/src/sage/src/sage/graphs/base/graph_backends.pyx (starting at line 538)

        Get/set whether or not ``self`` allows multiple edges.

        INPUT:

        - ``new`` -- can be a boolean (in which case it sets the value) or
          ``None``, in which case the current value is returned. It is set to
          ``None`` by default.

        TESTS::

            sage: G = sage.graphs.base.graph_backends.GenericGraphBackend()
            sage: G.multiple_edges(True)
            Traceback (most recent call last):
            ...
            NotImplementedError
            sage: G.multiple_edges(None)
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def multiple_edges(self, _True) -> Any:
        """GenericGraphBackend.multiple_edges(self, new=None)

        File: /build/sagemath/src/sage/src/sage/graphs/base/graph_backends.pyx (starting at line 538)

        Get/set whether or not ``self`` allows multiple edges.

        INPUT:

        - ``new`` -- can be a boolean (in which case it sets the value) or
          ``None``, in which case the current value is returned. It is set to
          ``None`` by default.

        TESTS::

            sage: G = sage.graphs.base.graph_backends.GenericGraphBackend()
            sage: G.multiple_edges(True)
            Traceback (most recent call last):
            ...
            NotImplementedError
            sage: G.multiple_edges(None)
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def multiple_edges(self, _None) -> Any:
        """GenericGraphBackend.multiple_edges(self, new=None)

        File: /build/sagemath/src/sage/src/sage/graphs/base/graph_backends.pyx (starting at line 538)

        Get/set whether or not ``self`` allows multiple edges.

        INPUT:

        - ``new`` -- can be a boolean (in which case it sets the value) or
          ``None``, in which case the current value is returned. It is set to
          ``None`` by default.

        TESTS::

            sage: G = sage.graphs.base.graph_backends.GenericGraphBackend()
            sage: G.multiple_edges(True)
            Traceback (most recent call last):
            ...
            NotImplementedError
            sage: G.multiple_edges(None)
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def name(self, new=...) -> Any:
        '''GenericGraphBackend.name(self, new=None)

        File: /build/sagemath/src/sage/src/sage/graphs/base/graph_backends.pyx (starting at line 562)

        Get/set name of ``self``.

        INPUT:

        - ``new`` -- can be a string (in which case it sets the value) or
          ``None``, in which case the current value is returned. It is set to
          ``None`` by default.

        TESTS::

            sage: G = sage.graphs.base.graph_backends.GenericGraphBackend()
            sage: G.name("A Generic Graph")
            Traceback (most recent call last):
            ...
            NotImplementedError
            sage: G.name(None)
            Traceback (most recent call last):
            ...
            NotImplementedError'''
    @overload
    def name(self, _None) -> Any:
        '''GenericGraphBackend.name(self, new=None)

        File: /build/sagemath/src/sage/src/sage/graphs/base/graph_backends.pyx (starting at line 562)

        Get/set name of ``self``.

        INPUT:

        - ``new`` -- can be a string (in which case it sets the value) or
          ``None``, in which case the current value is returned. It is set to
          ``None`` by default.

        TESTS::

            sage: G = sage.graphs.base.graph_backends.GenericGraphBackend()
            sage: G.name("A Generic Graph")
            Traceback (most recent call last):
            ...
            NotImplementedError
            sage: G.name(None)
            Traceback (most recent call last):
            ...
            NotImplementedError'''
    @overload
    def num_edges(self, directed) -> Any:
        """GenericGraphBackend.num_edges(self, directed)

        File: /build/sagemath/src/sage/src/sage/graphs/base/graph_backends.pyx (starting at line 586)

        Return the number of edges in ``self``.

        INPUT:

        - ``directed`` -- boolean

        TESTS::

            sage: G = sage.graphs.base.graph_backends.GenericGraphBackend()
            sage: G.num_edges(True)
            Traceback (most recent call last):
            ...
            NotImplementedError
            sage: G.num_edges(False)
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def num_edges(self, _True) -> Any:
        """GenericGraphBackend.num_edges(self, directed)

        File: /build/sagemath/src/sage/src/sage/graphs/base/graph_backends.pyx (starting at line 586)

        Return the number of edges in ``self``.

        INPUT:

        - ``directed`` -- boolean

        TESTS::

            sage: G = sage.graphs.base.graph_backends.GenericGraphBackend()
            sage: G.num_edges(True)
            Traceback (most recent call last):
            ...
            NotImplementedError
            sage: G.num_edges(False)
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def num_edges(self, _False) -> Any:
        """GenericGraphBackend.num_edges(self, directed)

        File: /build/sagemath/src/sage/src/sage/graphs/base/graph_backends.pyx (starting at line 586)

        Return the number of edges in ``self``.

        INPUT:

        - ``directed`` -- boolean

        TESTS::

            sage: G = sage.graphs.base.graph_backends.GenericGraphBackend()
            sage: G.num_edges(True)
            Traceback (most recent call last):
            ...
            NotImplementedError
            sage: G.num_edges(False)
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def num_verts(self) -> Any:
        """GenericGraphBackend.num_verts(self)

        File: /build/sagemath/src/sage/src/sage/graphs/base/graph_backends.pyx (starting at line 608)

        Return the number of vertices in ``self``.

        TESTS::

            sage: G = sage.graphs.base.graph_backends.GenericGraphBackend()
            sage: G.num_verts()
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def num_verts(self) -> Any:
        """GenericGraphBackend.num_verts(self)

        File: /build/sagemath/src/sage/src/sage/graphs/base/graph_backends.pyx (starting at line 608)

        Return the number of vertices in ``self``.

        TESTS::

            sage: G = sage.graphs.base.graph_backends.GenericGraphBackend()
            sage: G.num_verts()
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    def out_degree(self, v) -> Any:
        """GenericGraphBackend.out_degree(self, v)

        File: /build/sagemath/src/sage/src/sage/graphs/base/graph_backends.pyx (starting at line 206)

        Return the out-degree of `v`.

        INPUT:

        - ``v`` -- a vertex label

        TESTS::

            sage: G = sage.graphs.base.graph_backends.GenericGraphBackend()
            sage: G.out_degree(1)
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    def relabel(self, perm, directed) -> Any:
        """GenericGraphBackend.relabel(self, perm, directed)

        File: /build/sagemath/src/sage/src/sage/graphs/base/graph_backends.pyx (starting at line 622)

        Relabel the vertices of ``self`` by a permutation.

        INPUT:

        - ``perm`` -- permutation
        - ``directed`` -- boolean

        TESTS::

            sage: G = sage.graphs.base.graph_backends.GenericGraphBackend()
            sage: G.relabel([],False)
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    def set_edge_label(self, u, v, l, directed) -> Any:
        """GenericGraphBackend.set_edge_label(self, u, v, l, directed)

        File: /build/sagemath/src/sage/src/sage/graphs/base/graph_backends.pyx (starting at line 641)

        Label the edge `(u,v)` by `l`.

        INPUT:

        - ``u``, ``v`` -- vertices
        - ``l`` -- edge label
        - ``directed`` -- boolean

        TESTS::

            sage: G = sage.graphs.base.graph_backends.GenericGraphBackend()
            sage: G.set_edge_label(1,2,'a',True)
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    def __reduce__(self) -> Any:
        '''GenericGraphBackend.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/graphs/base/graph_backends.pyx (starting at line 661)

        Return a tuple used for pickling this graph.

        OUTPUT:

        This function returns a pair ``(f, args)`` such that ``f(*args)``
        produces a copy of ``self``. The function returned is always
        :func:`unpickle_graph_backend`.

        EXAMPLES:

        Pickling of the static graph backend makes pickling of immutable
        graphs and digraphs work::

            sage: G = Graph(graphs.PetersenGraph(), immutable=True)
            sage: G == loads(dumps(G))
            True
            sage: uc = [[2, 3], [], [1], [1], [1], [3, 4]]
            sage: D = DiGraph({i: uc[i] for i in range(len(uc))}, immutable=True)
            sage: loads(dumps(D)) == D
            True

        No problems with loops and multiple edges, with Labels::

            sage: g = Graph(multiedges=True, loops=True)
            sage: g.add_edges(2 * graphs.PetersenGraph().edges(sort=False))
            sage: g.add_edge(0, 0)
            sage: g.add_edge(1, 1, "a label")
            sage: g.add_edges([(0, 1, "labellll"), (0, 1, "labellll"), (0, 1, "LABELLLL")])
            sage: g.add_vertex("isolated vertex")
            sage: gi = g.copy(immutable=True)
            sage: loads(dumps(gi)) == gi
            True

        Similar, with a directed graph::

            sage: g = DiGraph(multiedges=True, loops=True)
            sage: H = 2 * (digraphs.Circuit(15) + DiGraph(graphs.PetersenGraph()))
            sage: g.add_edges(H.edge_iterator())
            sage: g.add_edge(0, 0)
            sage: g.add_edge(1, 1, "a label")
            sage: g.add_edges([(0, 1, "labellll"), (0, 1, "labellll"), (0, 1, "LABELLLL")])
            sage: g.add_vertex("isolated vertex")
            sage: gi = g.copy(immutable=True)
            sage: loads(dumps(gi)) == gi
            True

        TESTS:

        Check that :issue:`38900` is fixed::

            sage: from itertools import product
            sage: for sparse, immutable in product([True, False], [True, False]):
            ....:     G = Graph([[0, 1, 2], [(0, 1)]], sparse=sparse, immutable=immutable)
            ....:     H = loads(dumps(G))
            ....:     if type(G._backend) != type(H._backend):
            ....:         print(sparse, immutable, type(G._backend), type(H._backend))'''
