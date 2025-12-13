import sage.graphs.base.c_graph
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from typing import Any, ClassVar, overload

__pyx_capi__: dict

class DenseGraph(sage.graphs.base.c_graph.CGraph):
    """File: /build/sagemath/src/sage/src/sage/graphs/base/dense_graph.pyx (starting at line 133)

        Compiled dense graphs.

        ::

            sage: from sage.graphs.base.dense_graph import DenseGraph

        Dense graphs are initialized as follows::

            sage: D = DenseGraph(nverts=10, extra_vertices=10)

        INPUT:

        - ``nverts`` -- nonnegative integer; the number of vertices
        - ``extra_vertices`` -- nonnegative integer (default: 10); how many extra
          vertices to allocate
        - ``verts`` -- list (default: ``None``); optional list of vertices to add
        - ``arcs`` -- list (default: ``None``); optional list of arcs to add
        - ``directed`` -- boolean (default: ``None``); whether the graph is directed

        The first ``nverts`` are created as vertices of the graph, and the next
        ``extra_vertices`` can be freely added without reallocation. See top level
        documentation for more details. The input ``verts`` and ``arcs`` are mainly
        for use in pickling.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, nverts=..., extra_vertices=...) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def complement(self) -> Any:
        """DenseGraph.complement(self)

        File: /build/sagemath/src/sage/src/sage/graphs/base/dense_graph.pyx (starting at line 387)

        Replace the graph with its complement.

        .. NOTE::

            Assumes that the graph has no loop.

        EXAMPLES::

            sage: from sage.graphs.base.dense_graph import DenseGraph
            sage: G = DenseGraph(5)
            sage: G.add_arc(0, 1)
            sage: G.has_arc(0, 1)
            True
            sage: G.complement()
            sage: G.has_arc(0, 1)
            False"""
    @overload
    def complement(self) -> Any:
        """DenseGraph.complement(self)

        File: /build/sagemath/src/sage/src/sage/graphs/base/dense_graph.pyx (starting at line 387)

        Replace the graph with its complement.

        .. NOTE::

            Assumes that the graph has no loop.

        EXAMPLES::

            sage: from sage.graphs.base.dense_graph import DenseGraph
            sage: G = DenseGraph(5)
            sage: G.add_arc(0, 1)
            sage: G.has_arc(0, 1)
            True
            sage: G.complement()
            sage: G.has_arc(0, 1)
            False"""
    def in_degree(self, intv) -> int:
        """DenseGraph.in_degree(self, int v) -> int

        File: /build/sagemath/src/sage/src/sage/graphs/base/dense_graph.pyx (starting at line 477)

        Return the in-degree of ``v``

        INPUT:

        - ``v`` -- integer

        EXAMPLES::

            sage: from sage.graphs.base.dense_graph import DenseGraph
            sage: G = DenseGraph(5)
            sage: G.add_arc(0,1)
            sage: G.add_arc(1,2)
            sage: G.add_arc(1,3)
            sage: G.in_degree(0)
            0
            sage: G.in_degree(1)
            1"""
    def out_degree(self, intu) -> int:
        """DenseGraph.out_degree(self, int u) -> int

        File: /build/sagemath/src/sage/src/sage/graphs/base/dense_graph.pyx (starting at line 455)

        Return the out-degree of ``v``

        INPUT:

        - ``u`` -- integer

        EXAMPLES::

            sage: from sage.graphs.base.dense_graph import DenseGraph
            sage: G = DenseGraph(5)
            sage: G.add_arc(0,1)
            sage: G.add_arc(1,2)
            sage: G.add_arc(1,3)
            sage: G.out_degree(0)
            1
            sage: G.out_degree(1)
            2"""
    def realloc(self, inttotal_verts) -> Any:
        """DenseGraph.realloc(self, int total_verts)

        File: /build/sagemath/src/sage/src/sage/graphs/base/dense_graph.pyx (starting at line 207)

        Reallocate the number of vertices to use, without actually adding any.

        INPUT:

        - ``total`` -- integer; the total size to make the array

        Returns -1 and fails if reallocation would destroy any active vertices.

        EXAMPLES::

            sage: from sage.graphs.base.dense_graph import DenseGraph
            sage: D = DenseGraph(nverts=4, extra_vertices=4)
            sage: D.current_allocation()
            8
            sage: D.add_vertex(6)
            6
            sage: D.current_allocation()
            8
            sage: D.add_vertex(10)
            10
            sage: D.current_allocation()
            16
            sage: D.add_vertex(40)
            Traceback (most recent call last):
            ...
            RuntimeError: requested vertex is past twice the allocated range: use realloc
            sage: D.realloc(50)
            sage: D.add_vertex(40)
            40
            sage: D.current_allocation()
            50
            sage: D.realloc(30)
            -1
            sage: D.current_allocation()
            50
            sage: D.del_vertex(40)
            sage: D.realloc(30)
            sage: D.current_allocation()
            30"""

class DenseGraphBackend(sage.graphs.base.c_graph.CGraphBackend):
    """DenseGraphBackend(n, directed=True)

    File: /build/sagemath/src/sage/src/sage/graphs/base/dense_graph.pyx (starting at line 577)

    Backend for Sage graphs using DenseGraphs.

    ::

        sage: from sage.graphs.base.dense_graph import DenseGraphBackend

    This class is only intended for use by the Sage Graph and DiGraph class.
    If you are interested in using a DenseGraph, you probably want to do
    something like the following example, which creates a Sage Graph instance
    which wraps a ``DenseGraph`` object::

        sage: G = Graph(30, sparse=False)
        sage: G.add_edges([(0, 1), (0, 3), (4, 5), (9, 23)])
        sage: G.edges(sort=True, labels=False)
        [(0, 1), (0, 3), (4, 5), (9, 23)]

    Note that Sage graphs using the backend are more flexible than DenseGraphs
    themselves. This is because DenseGraphs (by design) do not deal with Python
    objects::

        sage: G.add_vertex((0, 1, 2))
        sage: sorted(list(G),
        ....:        key=lambda x: (isinstance(x, tuple), x))
        [0,
        ...
         29,
         (0, 1, 2)]
        sage: from sage.graphs.base.dense_graph import DenseGraph
        sage: DG = DenseGraph(30)
        sage: DG.add_vertex((0, 1, 2))
        Traceback (most recent call last):
        ...
        TypeError: an integer is required"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, n, directed=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/graphs/base/dense_graph.pyx (starting at line 614)

                Initialize a dense graph with ``n`` vertices.

                EXAMPLES::

                    sage: D = sage.graphs.base.dense_graph.DenseGraphBackend(9)
                    sage: D.add_edge(0, 1, None, False)
                    sage: list(D.iterator_edges(range(9), True))
                    [(0, 1, None)]
        """
    def add_edges(self, edges, booldirected, boolremove_loops=...) -> Any:
        """DenseGraphBackend.add_edges(self, edges, bool directed, bool remove_loops=False)

        File: /build/sagemath/src/sage/src/sage/graphs/base/dense_graph.pyx (starting at line 654)

        Add edges from a list.

        INPUT:

        - ``edges`` -- an iterable of edges to be added; each edge can either be
          of the form ``(u, v)`` or ``(u, v, l)``

        - ``directed`` -- if ``False``, adds ``(v, u)`` as well as ``(u, v)``

        - ``remove_loops`` -- if ``True``, remove loops

        EXAMPLES::

            sage: D = sage.graphs.base.dense_graph.DenseGraphBackend(9)
            sage: D.add_edges([(0, 1), (2, 3), (4, 5), (5, 6)], False)
            sage: list(D.iterator_edges(range(9), True))
            [(0, 1, None),
             (2, 3, None),
             (4, 5, None),
             (5, 6, None)]"""
    def get_edge_label(self, u, v) -> Any:
        """DenseGraphBackend.get_edge_label(self, u, v)

        File: /build/sagemath/src/sage/src/sage/graphs/base/dense_graph.pyx (starting at line 683)

        Return the edge label for ``(u, v)``.

        Always ``None``, since dense graphs do not support edge labels.

        INPUT:

        - ``u``, ``v`` -- the vertices of the edge

        EXAMPLES::

            sage: D = sage.graphs.base.dense_graph.DenseGraphBackend(9)
            sage: D.add_edges([(0, 1), (2, 3, 7), (4, 5), (5, 6)], False)
            sage: list(D.iterator_edges(range(9), True))
            [(0, 1, None),
             (2, 3, None),
             (4, 5, None),
             (5, 6, None)]
            sage: D.del_edge(0, 1, None, True)
            sage: list(D.iterator_out_edges(range(9), True))
            [(1, 0, None),
             (2, 3, None),
             (3, 2, None),
             (4, 5, None),
             (5, 4, None),
             (5, 6, None),
             (6, 5, None)]
            sage: D.get_edge_label(2, 3)
            sage: D.get_edge_label(2, 4)
            Traceback (most recent call last):
            ...
            LookupError: (2, 4) is not an edge of the graph"""
    def has_edge(self, u, v, l) -> Any:
        """DenseGraphBackend.has_edge(self, u, v, l)

        File: /build/sagemath/src/sage/src/sage/graphs/base/dense_graph.pyx (starting at line 721)

        Check whether this graph has edge ``(u, v)``.

        .. NOTE::

            The input ``l`` is for consistency with other backends.

        INPUT:

        - ``u``, ``v`` -- the vertices of the edge

        - ``l`` -- the edge label (ignored)

        EXAMPLES::

            sage: D = sage.graphs.base.dense_graph.DenseGraphBackend(9)
            sage: D.add_edges([(0, 1), (2, 3), (4, 5), (5, 6)], False)
            sage: D.has_edge(0, 1, None)
            True"""
    @overload
    def multiple_edges(self, new) -> Any:
        """DenseGraphBackend.multiple_edges(self, new)

        File: /build/sagemath/src/sage/src/sage/graphs/base/dense_graph.pyx (starting at line 755)

        Get/set whether or not ``self`` allows multiple edges.

        INPUT:

        - ``new`` -- boolean (to set) or ``None`` (to get)

        EXAMPLES::

            sage: import sage.graphs.base.dense_graph
            sage: G = sage.graphs.base.dense_graph.DenseGraphBackend(9)
            sage: G.multiple_edges(True)
            Traceback (most recent call last):
            ...
            NotImplementedError: dense graphs do not support multiple edges
            sage: G.multiple_edges(None)
            False"""
    @overload
    def multiple_edges(self, _True) -> Any:
        """DenseGraphBackend.multiple_edges(self, new)

        File: /build/sagemath/src/sage/src/sage/graphs/base/dense_graph.pyx (starting at line 755)

        Get/set whether or not ``self`` allows multiple edges.

        INPUT:

        - ``new`` -- boolean (to set) or ``None`` (to get)

        EXAMPLES::

            sage: import sage.graphs.base.dense_graph
            sage: G = sage.graphs.base.dense_graph.DenseGraphBackend(9)
            sage: G.multiple_edges(True)
            Traceback (most recent call last):
            ...
            NotImplementedError: dense graphs do not support multiple edges
            sage: G.multiple_edges(None)
            False"""
    @overload
    def multiple_edges(self, _None) -> Any:
        """DenseGraphBackend.multiple_edges(self, new)

        File: /build/sagemath/src/sage/src/sage/graphs/base/dense_graph.pyx (starting at line 755)

        Get/set whether or not ``self`` allows multiple edges.

        INPUT:

        - ``new`` -- boolean (to set) or ``None`` (to get)

        EXAMPLES::

            sage: import sage.graphs.base.dense_graph
            sage: G = sage.graphs.base.dense_graph.DenseGraphBackend(9)
            sage: G.multiple_edges(True)
            Traceback (most recent call last):
            ...
            NotImplementedError: dense graphs do not support multiple edges
            sage: G.multiple_edges(None)
            False"""
    def set_edge_label(self, u, v, l, booldirected) -> Any:
        """DenseGraphBackend.set_edge_label(self, u, v, l, bool directed)

        File: /build/sagemath/src/sage/src/sage/graphs/base/dense_graph.pyx (starting at line 779)

        Label the edge ``(u, v)`` by ``l``.

        INPUT:

        - ``u``, ``v`` -- the vertices of the edge

        - ``l`` -- the edge label

        - ``directed`` -- if ``False``, also set ``(v, u)`` with label ``l``

        EXAMPLES::

            sage: import sage.graphs.base.dense_graph
            sage: G = sage.graphs.base.dense_graph.DenseGraphBackend(9)
            sage: G.set_edge_label(1, 2, 'a', True)
            Traceback (most recent call last):
            ...
            NotImplementedError: dense graphs do not support edge labels"""
