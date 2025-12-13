import sage.graphs.base.c_graph
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from typing import Any, ClassVar, overload

class SparseGraph(sage.graphs.base.c_graph.CGraph):
    """File: /build/sagemath/src/sage/src/sage/graphs/base/sparse_graph.pyx (starting at line 224)

        Compiled sparse graphs.

        ::

            sage: from sage.graphs.base.sparse_graph import SparseGraph

        Sparse graphs are initialized as follows::

            sage: S = SparseGraph(nverts = 10, expected_degree = 3, extra_vertices = 10)

        INPUT:

        - ``nverts`` -- nonnegative integer, the number of vertices

        - ``expected_degree`` -- nonnegative integer (default: 16); expected upper
          bound on degree of vertices

        - ``extra_vertices`` -- nonnegative integer (default: 0); how many extra
          vertices to allocate

        - ``verts`` -- (optional) list of vertices to add

        - ``arcs`` -- (optional) list of arcs to add

        The first ``nverts`` are created as vertices of the graph, and the next
        ``extra_vertices`` can be freely added without reallocation. See top level
        documentation for more details. The input ``verts`` and ``arcs`` are mainly
        for use in pickling.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, nverts=..., expected_degree=..., extra_vertices=...) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
    def add_arc_label(self, intu, intv, intl=...) -> Any:
        """SparseGraph.add_arc_label(self, int u, int v, int l=0)

        File: /build/sagemath/src/sage/src/sage/graphs/base/sparse_graph.pyx (starting at line 885)

        Add arc ``(u, v)`` to the graph with label ``l``.

        INPUT:

        - ``u``, ``v`` -- nonnegative integers, must be in ``self``

        - ``l`` -- positive integer label, or zero for no label

        EXAMPLES::

            sage: from sage.graphs.base.sparse_graph import SparseGraph
            sage: G = SparseGraph(5)
            sage: G.add_arc_label(0,1)
            sage: G.add_arc_label(4,7)
            Traceback (most recent call last):
            ...
            LookupError: vertex (7) is not a vertex of the graph
            sage: G.has_arc(1,0)
            False
            sage: G.has_arc(0,1)
            True
            sage: G.add_arc_label(1,2,2)
            sage: G.arc_label(1,2)
            2"""
    def in_degree(self, intv) -> int:
        """SparseGraph.in_degree(self, int v) -> int

        File: /build/sagemath/src/sage/src/sage/graphs/base/sparse_graph.pyx (starting at line 791)

        Return the in-degree of ``v``

        INPUT:

        - ``v`` -- integer

        EXAMPLES::

            sage: from sage.graphs.base.sparse_graph import SparseGraph
            sage: G = SparseGraph(5)
            sage: G.add_arc(0,1)
            sage: G.add_arc(1,2)
            sage: G.add_arc(1,3)
            sage: G.in_degree(0)
            0
            sage: G.in_degree(1)
            1"""
    @overload
    def is_directed(self) -> bool:
        """SparseGraph.is_directed(self) -> bool

        File: /build/sagemath/src/sage/src/sage/graphs/base/sparse_graph.pyx (starting at line 463)

        Return whether the graph is directed.

        EXAMPLES::

            sage: from sage.graphs.base.sparse_graph import SparseGraph
            sage: G = SparseGraph(5)
            sage: G.is_directed()
            True
            sage: G = SparseGraph(5, directed=False)
            sage: G.is_directed()
            False"""
    @overload
    def is_directed(self) -> Any:
        """SparseGraph.is_directed(self) -> bool

        File: /build/sagemath/src/sage/src/sage/graphs/base/sparse_graph.pyx (starting at line 463)

        Return whether the graph is directed.

        EXAMPLES::

            sage: from sage.graphs.base.sparse_graph import SparseGraph
            sage: G = SparseGraph(5)
            sage: G.is_directed()
            True
            sage: G = SparseGraph(5, directed=False)
            sage: G.is_directed()
            False"""
    @overload
    def is_directed(self) -> Any:
        """SparseGraph.is_directed(self) -> bool

        File: /build/sagemath/src/sage/src/sage/graphs/base/sparse_graph.pyx (starting at line 463)

        Return whether the graph is directed.

        EXAMPLES::

            sage: from sage.graphs.base.sparse_graph import SparseGraph
            sage: G = SparseGraph(5)
            sage: G.is_directed()
            True
            sage: G = SparseGraph(5, directed=False)
            sage: G.is_directed()
            False"""
    def out_degree(self, intu) -> int:
        """SparseGraph.out_degree(self, int u) -> int

        File: /build/sagemath/src/sage/src/sage/graphs/base/sparse_graph.pyx (starting at line 721)

        Return the out-degree of ``v``

        INPUT:

        - ``u`` -- integer

        EXAMPLES::

            sage: from sage.graphs.base.sparse_graph import SparseGraph
            sage: G = SparseGraph(5)
            sage: G.add_arc(0,1)
            sage: G.add_arc(1,2)
            sage: G.add_arc(1,3)
            sage: G.out_degree(0)
            1
            sage: G.out_degree(1)
            2"""
    def realloc(self, inttotal) -> Any:
        """SparseGraph.realloc(self, int total)

        File: /build/sagemath/src/sage/src/sage/graphs/base/sparse_graph.pyx (starting at line 375)

        Reallocate the number of vertices to use, without actually adding any.

        INPUT:

        - ``total`` -- integer; the total size to make the array

        Returns -1 and fails if reallocation would destroy any active vertices.

        EXAMPLES::

            sage: from sage.graphs.base.sparse_graph import SparseGraph
            sage: S = SparseGraph(nverts=4, extra_vertices=4)
            sage: S.current_allocation()
            8
            sage: S.add_vertex(6)
            6
            sage: S.current_allocation()
            8
            sage: S.add_vertex(10)
            10
            sage: S.current_allocation()
            16
            sage: S.add_vertex(40)
            Traceback (most recent call last):
            ...
            RuntimeError: requested vertex is past twice the allocated range: use realloc
            sage: S.realloc(50)
            sage: S.add_vertex(40)
            40
            sage: S.current_allocation()
            50
            sage: S.realloc(30)
            -1
            sage: S.current_allocation()
            50
            sage: S.del_vertex(40)
            sage: S.realloc(30)
            sage: S.current_allocation()
            30"""

class SparseGraphBackend(sage.graphs.base.c_graph.CGraphBackend):
    """SparseGraphBackend(int n, directed=True)

    File: /build/sagemath/src/sage/src/sage/graphs/base/sparse_graph.pyx (starting at line 1211)

    Backend for Sage graphs using SparseGraphs.

    ::

        sage: from sage.graphs.base.sparse_graph import SparseGraphBackend

    This class is only intended for use by the Sage Graph and DiGraph class.
    If you are interested in using a SparseGraph, you probably want to do
    something like the following example, which creates a Sage Graph instance
    which wraps a SparseGraph object::

        sage: G = Graph(30, sparse=True)
        sage: G.add_edges([(0,1), (0,3), (4,5), (9, 23)])
        sage: G.edges(sort=True, labels=False)
        [(0, 1), (0, 3), (4, 5), (9, 23)]

    Note that Sage graphs using the backend are more flexible than SparseGraphs
    themselves. This is because SparseGraphs (by design) do not deal with Python
    objects::

        sage: G.add_vertex((0,1,2))
        sage: sorted(list(G),
        ....:        key=lambda x: (isinstance(x, tuple), x))
        [0,
        ...
         29,
         (0, 1, 2)]
        sage: from sage.graphs.base.sparse_graph import SparseGraph
        sage: SG = SparseGraph(30)
        sage: SG.add_vertex((0,1,2))
        Traceback (most recent call last):
        ...
        TypeError: an integer is required"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, intn, directed=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/graphs/base/sparse_graph.pyx (starting at line 1248)

                Initialize a sparse graph with n vertices.

                EXAMPLES::

                    sage: D = sage.graphs.base.sparse_graph.SparseGraphBackend(9)
                    sage: D.add_edge(0,1,None,False)
                    sage: list(D.iterator_edges(range(9), True))
                    [(0, 1, None)]
        """
    def get_edge_label(self, u, v) -> Any:
        """SparseGraphBackend.get_edge_label(self, u, v)

        File: /build/sagemath/src/sage/src/sage/graphs/base/sparse_graph.pyx (starting at line 1294)

        Return the edge label for ``(u, v)``.

        INPUT:

        - ``u``, ``v`` -- the vertices of the edge

        EXAMPLES::

            sage: D = sage.graphs.base.sparse_graph.SparseGraphBackend(9)
            sage: D.add_edges([(0,1,1), (2,3,2), (4,5,3), (5,6,2)], False)
            sage: list(D.iterator_edges(range(9), True))
            [(0, 1, 1), (2, 3, 2), (4, 5, 3), (5, 6, 2)]
            sage: D.get_edge_label(3,2)
            2"""
    def has_edge(self, u, v, l) -> Any:
        """SparseGraphBackend.has_edge(self, u, v, l)

        File: /build/sagemath/src/sage/src/sage/graphs/base/sparse_graph.pyx (starting at line 1326)

        Return whether this graph has edge ``(u,v)`` with label ``l``. If ``l``
        is ``None``, return whether this graph has an edge ``(u,v)`` with any
        label.

        INPUT:

        - ``u``, ``v`` -- the vertices of the edge

        - ``l`` -- the edge label, or ``None``

        EXAMPLES::

            sage: D = sage.graphs.base.sparse_graph.SparseGraphBackend(9)
            sage: D.add_edges([(0,1), (2,3), (4,5), (5,6)], False)
            sage: D.has_edge(0,1,None)
            True"""
    @overload
    def multiple_edges(self, new) -> Any:
        """SparseGraphBackend.multiple_edges(self, new)

        File: /build/sagemath/src/sage/src/sage/graphs/base/sparse_graph.pyx (starting at line 1366)

        Get/set whether or not ``self`` allows multiple edges.

        INPUT:

        - ``new`` -- boolean (to set) or ``None`` (to get)

        EXAMPLES::

            sage: G = sage.graphs.base.sparse_graph.SparseGraphBackend(9)
            sage: G.multiple_edges(True)
            sage: G.multiple_edges(None)
            True
            sage: G.multiple_edges(False)
            sage: G.multiple_edges(None)
            False
            sage: G.add_edge(0,1,0,True)
            sage: G.add_edge(0,1,0,True)
            sage: list(G.iterator_out_edges(range(9), True))
            [(0, 1, 0)]"""
    @overload
    def multiple_edges(self, _True) -> Any:
        """SparseGraphBackend.multiple_edges(self, new)

        File: /build/sagemath/src/sage/src/sage/graphs/base/sparse_graph.pyx (starting at line 1366)

        Get/set whether or not ``self`` allows multiple edges.

        INPUT:

        - ``new`` -- boolean (to set) or ``None`` (to get)

        EXAMPLES::

            sage: G = sage.graphs.base.sparse_graph.SparseGraphBackend(9)
            sage: G.multiple_edges(True)
            sage: G.multiple_edges(None)
            True
            sage: G.multiple_edges(False)
            sage: G.multiple_edges(None)
            False
            sage: G.add_edge(0,1,0,True)
            sage: G.add_edge(0,1,0,True)
            sage: list(G.iterator_out_edges(range(9), True))
            [(0, 1, 0)]"""
    @overload
    def multiple_edges(self, _None) -> Any:
        """SparseGraphBackend.multiple_edges(self, new)

        File: /build/sagemath/src/sage/src/sage/graphs/base/sparse_graph.pyx (starting at line 1366)

        Get/set whether or not ``self`` allows multiple edges.

        INPUT:

        - ``new`` -- boolean (to set) or ``None`` (to get)

        EXAMPLES::

            sage: G = sage.graphs.base.sparse_graph.SparseGraphBackend(9)
            sage: G.multiple_edges(True)
            sage: G.multiple_edges(None)
            True
            sage: G.multiple_edges(False)
            sage: G.multiple_edges(None)
            False
            sage: G.add_edge(0,1,0,True)
            sage: G.add_edge(0,1,0,True)
            sage: list(G.iterator_out_edges(range(9), True))
            [(0, 1, 0)]"""
    @overload
    def multiple_edges(self, _False) -> Any:
        """SparseGraphBackend.multiple_edges(self, new)

        File: /build/sagemath/src/sage/src/sage/graphs/base/sparse_graph.pyx (starting at line 1366)

        Get/set whether or not ``self`` allows multiple edges.

        INPUT:

        - ``new`` -- boolean (to set) or ``None`` (to get)

        EXAMPLES::

            sage: G = sage.graphs.base.sparse_graph.SparseGraphBackend(9)
            sage: G.multiple_edges(True)
            sage: G.multiple_edges(None)
            True
            sage: G.multiple_edges(False)
            sage: G.multiple_edges(None)
            False
            sage: G.add_edge(0,1,0,True)
            sage: G.add_edge(0,1,0,True)
            sage: list(G.iterator_out_edges(range(9), True))
            [(0, 1, 0)]"""
    @overload
    def multiple_edges(self, _None) -> Any:
        """SparseGraphBackend.multiple_edges(self, new)

        File: /build/sagemath/src/sage/src/sage/graphs/base/sparse_graph.pyx (starting at line 1366)

        Get/set whether or not ``self`` allows multiple edges.

        INPUT:

        - ``new`` -- boolean (to set) or ``None`` (to get)

        EXAMPLES::

            sage: G = sage.graphs.base.sparse_graph.SparseGraphBackend(9)
            sage: G.multiple_edges(True)
            sage: G.multiple_edges(None)
            True
            sage: G.multiple_edges(False)
            sage: G.multiple_edges(None)
            False
            sage: G.add_edge(0,1,0,True)
            sage: G.add_edge(0,1,0,True)
            sage: list(G.iterator_out_edges(range(9), True))
            [(0, 1, 0)]"""
    def set_edge_label(self, u, v, l, booldirected) -> Any:
        """SparseGraphBackend.set_edge_label(self, u, v, l, bool directed)

        File: /build/sagemath/src/sage/src/sage/graphs/base/sparse_graph.pyx (starting at line 1392)

        Label the edge ``(u,v)`` by ``l``.

        INPUT:

        - ``u``, ``v`` -- the vertices of the edge

        - ``l`` -- the edge label

        - ``directed`` -- if ``False``, also set ``(v,u)`` with label ``l``

        EXAMPLES::

            sage: G = sage.graphs.base.sparse_graph.SparseGraphBackend(9)
            sage: G.add_edge(1,2,None,True)
            sage: G.set_edge_label(1,2,'a',True)
            sage: list(G.iterator_out_edges(range(9), True))
            [(1, 2, 'a')]

        Note that it fails silently if there is no edge there::

            sage: G.set_edge_label(2,1,'b',True)
            sage: list(G.iterator_out_edges(range(9), True))
            [(1, 2, 'a')]"""
