import sage.graphs.base.graph_backends
from sage.categories.category import ZZ as ZZ
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

class CGraph:
    """File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 65)

        Compiled sparse and dense graphs.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def add_arc(self, intu, intv) -> Any:
        """CGraph.add_arc(self, int u, int v)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 724)

        Add arc ``(u, v)`` to the graph.

        INPUT:

        - ``u``, ``v`` -- nonnegative integers; must be in self

        EXAMPLES:

        On the :class:`CGraph` level, this always produces an error, as there are no vertices::

            sage: from sage.graphs.base.c_graph import CGraph
            sage: G = CGraph()
            sage: G.add_arc(0, 1)
            Traceback (most recent call last):
            ...
            LookupError: vertex (0) is not a vertex of the graph

        It works, once there are vertices and :meth:`add_arc_unsafe` is implemented::

            sage: from sage.graphs.base.dense_graph import DenseGraph
            sage: G = DenseGraph(5)
            sage: G.add_arc(0, 1)
            sage: G.add_arc(4, 7)
            Traceback (most recent call last):
            ...
            LookupError: vertex (7) is not a vertex of the graph
            sage: G.has_arc(1, 0)
            False
            sage: G.has_arc(0, 1)
            True

            sage: from sage.graphs.base.sparse_graph import SparseGraph
            sage: G = SparseGraph(5)
            sage: G.add_arc(0,1)
            sage: G.add_arc(4,7)
            Traceback (most recent call last):
            ...
            LookupError: vertex (7) is not a vertex of the graph
            sage: G.has_arc(1,0)
            False
            sage: G.has_arc(0,1)
            True"""
    def add_vertex(self, intk=...) -> Any:
        """CGraph.add_vertex(self, int k=-1)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 224)

        Add vertex ``k`` to the graph.

        INPUT:

        - ``k`` -- nonnegative integer or ``-1`` (default: ``-1``); if `k = -1`,
          a new vertex is added and the integer used is returned.  That is, for
          `k = -1`, this function will find the first available vertex that is
          not in ``self`` and add that vertex to this graph.

        OUTPUT:

        - ``-1`` -- indicates that no vertex was added because the current
          allocation is already full or the vertex is out of range

        - nonnegative integer -- this vertex is now guaranteed to be in the
          graph

        .. SEEALSO::

            - ``add_vertex_unsafe`` -- add a vertex to a graph. This method is
              potentially unsafe. You should instead use :meth:`add_vertex`

            - ``add_vertices`` -- add a bunch of vertices to a graph

        EXAMPLES:

        Adding vertices to a sparse graph::

            sage: from sage.graphs.base.sparse_graph import SparseGraph
            sage: G = SparseGraph(3, extra_vertices=3)
            sage: G.add_vertex(3)
            3
            sage: G.add_arc(2, 5)
            Traceback (most recent call last):
            ...
            LookupError: vertex (5) is not a vertex of the graph
            sage: G.add_arc(1, 3)
            sage: G.has_arc(1, 3)
            True
            sage: G.has_arc(2, 3)
            False

        Adding vertices to a dense graph::

            sage: from sage.graphs.base.dense_graph import DenseGraph
            sage: G = DenseGraph(3, extra_vertices=3)
            sage: G.add_vertex(3)
            3
            sage: G.add_arc(2,5)
            Traceback (most recent call last):
            ...
            LookupError: vertex (5) is not a vertex of the graph
            sage: G.add_arc(1, 3)
            sage: G.has_arc(1, 3)
            True
            sage: G.has_arc(2, 3)
            False

        Repeatedly adding a vertex using `k = -1` will allocate more memory
        as required::

            sage: from sage.graphs.base.sparse_graph import SparseGraph
            sage: G = SparseGraph(3, extra_vertices=0)
            sage: G.verts()
            [0, 1, 2]
            sage: for i in range(10):
            ....:     _ = G.add_vertex(-1);
            ...
            sage: G.verts()
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

        ::

            sage: from sage.graphs.base.dense_graph import DenseGraph
            sage: G = DenseGraph(3, extra_vertices=0)
            sage: G.verts()
            [0, 1, 2]
            sage: for i in range(12):
            ....:     _ = G.add_vertex(-1);
            ...
            sage: G.verts()
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

        TESTS::

            sage: from sage.graphs.base.sparse_graph import SparseGraph
            sage: G = SparseGraph(3, extra_vertices=0)
            sage: G.add_vertex(6)
            Traceback (most recent call last):
            ...
            RuntimeError: requested vertex is past twice the allocated range: use realloc

        ::

            sage: from sage.graphs.base.dense_graph import DenseGraph
            sage: G = DenseGraph(3, extra_vertices=0)
            sage: G.add_vertex(6)
            Traceback (most recent call last):
            ...
            RuntimeError: requested vertex is past twice the allocated range: use realloc"""
    def add_vertices(self, verts) -> Any:
        """CGraph.add_vertices(self, verts)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 336)

        Add vertices from the iterable ``verts``.

        INPUT:

        - ``verts`` -- an iterable of vertices; value -1 has a special meaning
          -- for each such value an unused vertex name is found, used to create
          a new vertex and returned.

        OUTPUT:

        List of generated labels if there is any -1 in ``verts``. ``None``
        otherwise.

        .. SEEALSO::

            - :meth:`add_vertex` -- add a vertex to a graph

        EXAMPLES:

        Adding vertices for sparse graphs::

            sage: from sage.graphs.base.sparse_graph import SparseGraph
            sage: S = SparseGraph(nverts=4, extra_vertices=4)
            sage: S.verts()
            [0, 1, 2, 3]
            sage: S.add_vertices([3, -1, 4, 9])
            [5]
            sage: S.verts()
            [0, 1, 2, 3, 4, 5, 9]
            sage: S.realloc(20)
            sage: S.verts()
            [0, 1, 2, 3, 4, 5, 9]

        Adding vertices for dense graphs::

            sage: from sage.graphs.base.dense_graph import DenseGraph
            sage: D = DenseGraph(nverts=4, extra_vertices=4)
            sage: D.verts()
            [0, 1, 2, 3]
            sage: D.add_vertices([3, -1, 4, 9])
            [5]
            sage: D.verts()
            [0, 1, 2, 3, 4, 5, 9]
            sage: D.realloc(20)
            sage: D.verts()
            [0, 1, 2, 3, 4, 5, 9]"""
    def all_arcs(self, intu, intv) -> list:
        """CGraph.all_arcs(self, int u, int v) -> list

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 931)

        Give the labels of all arcs ``(u, v)``. An unlabeled arc is interpreted as
        having label 0.

        EXAMPLES::

            sage: from sage.graphs.base.sparse_graph import SparseGraph
            sage: G = SparseGraph(5)
            sage: G.add_arc_label(1,2,1)
            sage: G.add_arc_label(1,2,2)
            sage: G.add_arc_label(1,2,2)
            sage: G.add_arc_label(1,2,2)
            sage: G.add_arc_label(1,2,3)
            sage: G.add_arc_label(1,2,3)
            sage: G.add_arc_label(1,2,4)
            sage: G.all_arcs(1,2)
            [4, 3, 3, 2, 2, 2, 1]"""
    def arc_label(self, intu, intv) -> int:
        """CGraph.arc_label(self, int u, int v) -> int

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 890)

        Retrieves the first label found associated with ``(u, v)``.

        INPUT:

        - ``u``, ``v`` -- nonnegative integers; must be in self

        OUTPUT: one of

        - positive integer -- indicates that there is a label on ``(u, v)``

        - ``0`` -- either the arc ``(u, v)`` is unlabeled, or there is no arc at all

        EXAMPLES::

            sage: from sage.graphs.base.sparse_graph import SparseGraph
            sage: G = SparseGraph(5)
            sage: G.add_arc_label(3,4,7)
            sage: G.arc_label(3,4)
            7

        To this function, an unlabeled arc is indistinguishable from a non-arc::

            sage: G.add_arc_label(1,0)
            sage: G.arc_label(1,0)
            0
            sage: G.arc_label(1,1)
            0

        This function only returns the *first* label it finds from ``u`` to ``v``::

            sage: G.add_arc_label(1,2,1)
            sage: G.add_arc_label(1,2,2)
            sage: G.arc_label(1,2)
            2"""
    def check_vertex(self, intn) -> Any:
        """CGraph.check_vertex(self, int n)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 131)

        Check that `n` is a vertex of ``self``.

        This method is different from :meth:`has_vertex`. The current method
        raises an error if `n` is not a vertex of this graph. On the other
        hand, :meth:`has_vertex` returns a boolean to signify whether or not
        `n` is a vertex of this graph.

        INPUT:

        - ``n`` -- nonnegative integer representing a vertex

        OUTPUT: raise an error if `n` is not a vertex of this graph

        .. SEEALSO::

            - :meth:`has_vertex`
              -- determine whether this graph has a specific vertex

        EXAMPLES::

            sage: from sage.graphs.base.sparse_graph import SparseGraph
            sage: S = SparseGraph(nverts=10, expected_degree=3, extra_vertices=10)
            sage: S.check_vertex(4)
            sage: S.check_vertex(12)
            Traceback (most recent call last):
            ...
            LookupError: vertex (12) is not a vertex of the graph
            sage: S.check_vertex(24)
            Traceback (most recent call last):
            ...
            LookupError: vertex (24) is not a vertex of the graph
            sage: S.check_vertex(-19)
            Traceback (most recent call last):
            ...
            LookupError: vertex (-19) is not a vertex of the graph

        ::

            sage: from sage.graphs.base.dense_graph import DenseGraph
            sage: D = DenseGraph(nverts=10, extra_vertices=10)
            sage: D.check_vertex(4)
            sage: D.check_vertex(12)
            Traceback (most recent call last):
            ...
            LookupError: vertex (12) is not a vertex of the graph
            sage: D.check_vertex(24)
            Traceback (most recent call last):
            ...
            LookupError: vertex (24) is not a vertex of the graph
            sage: D.check_vertex(-19)
            Traceback (most recent call last):
            ...
            LookupError: vertex (-19) is not a vertex of the graph"""
    @overload
    def current_allocation(self) -> int:
        """CGraph.current_allocation(self) -> int

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 526)

        Report the number of vertices allocated.

        OUTPUT:

        - The number of vertices allocated. This number is usually different
          from the order of a graph. We may have allocated enough memory for a
          graph to hold `n > 0` vertices, but the order (actual number of
          vertices) of the graph could be less than `n`.

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
            30

        The actual number of vertices in a graph might be less than the number
        of vertices allocated for the graph::

            sage: from sage.graphs.base.dense_graph import DenseGraph
            sage: G = DenseGraph(nverts=3, extra_vertices=2)
            sage: order = len(G.verts())
            sage: order
            3
            sage: G.current_allocation()
            5
            sage: order < G.current_allocation()
            True"""
    @overload
    def current_allocation(self) -> Any:
        """CGraph.current_allocation(self) -> int

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 526)

        Report the number of vertices allocated.

        OUTPUT:

        - The number of vertices allocated. This number is usually different
          from the order of a graph. We may have allocated enough memory for a
          graph to hold `n > 0` vertices, but the order (actual number of
          vertices) of the graph could be less than `n`.

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
            30

        The actual number of vertices in a graph might be less than the number
        of vertices allocated for the graph::

            sage: from sage.graphs.base.dense_graph import DenseGraph
            sage: G = DenseGraph(nverts=3, extra_vertices=2)
            sage: order = len(G.verts())
            sage: order
            3
            sage: G.current_allocation()
            5
            sage: order < G.current_allocation()
            True"""
    @overload
    def current_allocation(self) -> Any:
        """CGraph.current_allocation(self) -> int

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 526)

        Report the number of vertices allocated.

        OUTPUT:

        - The number of vertices allocated. This number is usually different
          from the order of a graph. We may have allocated enough memory for a
          graph to hold `n > 0` vertices, but the order (actual number of
          vertices) of the graph could be less than `n`.

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
            30

        The actual number of vertices in a graph might be less than the number
        of vertices allocated for the graph::

            sage: from sage.graphs.base.dense_graph import DenseGraph
            sage: G = DenseGraph(nverts=3, extra_vertices=2)
            sage: order = len(G.verts())
            sage: order
            3
            sage: G.current_allocation()
            5
            sage: order < G.current_allocation()
            True"""
    @overload
    def current_allocation(self) -> Any:
        """CGraph.current_allocation(self) -> int

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 526)

        Report the number of vertices allocated.

        OUTPUT:

        - The number of vertices allocated. This number is usually different
          from the order of a graph. We may have allocated enough memory for a
          graph to hold `n > 0` vertices, but the order (actual number of
          vertices) of the graph could be less than `n`.

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
            30

        The actual number of vertices in a graph might be less than the number
        of vertices allocated for the graph::

            sage: from sage.graphs.base.dense_graph import DenseGraph
            sage: G = DenseGraph(nverts=3, extra_vertices=2)
            sage: order = len(G.verts())
            sage: order
            3
            sage: G.current_allocation()
            5
            sage: order < G.current_allocation()
            True"""
    @overload
    def current_allocation(self) -> Any:
        """CGraph.current_allocation(self) -> int

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 526)

        Report the number of vertices allocated.

        OUTPUT:

        - The number of vertices allocated. This number is usually different
          from the order of a graph. We may have allocated enough memory for a
          graph to hold `n > 0` vertices, but the order (actual number of
          vertices) of the graph could be less than `n`.

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
            30

        The actual number of vertices in a graph might be less than the number
        of vertices allocated for the graph::

            sage: from sage.graphs.base.dense_graph import DenseGraph
            sage: G = DenseGraph(nverts=3, extra_vertices=2)
            sage: order = len(G.verts())
            sage: order
            3
            sage: G.current_allocation()
            5
            sage: order < G.current_allocation()
            True"""
    @overload
    def current_allocation(self) -> Any:
        """CGraph.current_allocation(self) -> int

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 526)

        Report the number of vertices allocated.

        OUTPUT:

        - The number of vertices allocated. This number is usually different
          from the order of a graph. We may have allocated enough memory for a
          graph to hold `n > 0` vertices, but the order (actual number of
          vertices) of the graph could be less than `n`.

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
            30

        The actual number of vertices in a graph might be less than the number
        of vertices allocated for the graph::

            sage: from sage.graphs.base.dense_graph import DenseGraph
            sage: G = DenseGraph(nverts=3, extra_vertices=2)
            sage: order = len(G.verts())
            sage: order
            3
            sage: G.current_allocation()
            5
            sage: order < G.current_allocation()
            True"""
    @overload
    def current_allocation(self) -> Any:
        """CGraph.current_allocation(self) -> int

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 526)

        Report the number of vertices allocated.

        OUTPUT:

        - The number of vertices allocated. This number is usually different
          from the order of a graph. We may have allocated enough memory for a
          graph to hold `n > 0` vertices, but the order (actual number of
          vertices) of the graph could be less than `n`.

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
            30

        The actual number of vertices in a graph might be less than the number
        of vertices allocated for the graph::

            sage: from sage.graphs.base.dense_graph import DenseGraph
            sage: G = DenseGraph(nverts=3, extra_vertices=2)
            sage: order = len(G.verts())
            sage: order
            3
            sage: G.current_allocation()
            5
            sage: order < G.current_allocation()
            True"""
    @overload
    def current_allocation(self) -> Any:
        """CGraph.current_allocation(self) -> int

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 526)

        Report the number of vertices allocated.

        OUTPUT:

        - The number of vertices allocated. This number is usually different
          from the order of a graph. We may have allocated enough memory for a
          graph to hold `n > 0` vertices, but the order (actual number of
          vertices) of the graph could be less than `n`.

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
            30

        The actual number of vertices in a graph might be less than the number
        of vertices allocated for the graph::

            sage: from sage.graphs.base.dense_graph import DenseGraph
            sage: G = DenseGraph(nverts=3, extra_vertices=2)
            sage: order = len(G.verts())
            sage: order
            3
            sage: G.current_allocation()
            5
            sage: order < G.current_allocation()
            True"""
    @overload
    def current_allocation(self) -> Any:
        """CGraph.current_allocation(self) -> int

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 526)

        Report the number of vertices allocated.

        OUTPUT:

        - The number of vertices allocated. This number is usually different
          from the order of a graph. We may have allocated enough memory for a
          graph to hold `n > 0` vertices, but the order (actual number of
          vertices) of the graph could be less than `n`.

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
            30

        The actual number of vertices in a graph might be less than the number
        of vertices allocated for the graph::

            sage: from sage.graphs.base.dense_graph import DenseGraph
            sage: G = DenseGraph(nverts=3, extra_vertices=2)
            sage: order = len(G.verts())
            sage: order
            3
            sage: G.current_allocation()
            5
            sage: order < G.current_allocation()
            True"""
    def del_all_arcs(self, intu, intv) -> Any:
        """CGraph.del_all_arcs(self, int u, int v)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 822)

        Delete all arcs from ``u`` to ``v``.

        INPUT:

        - ``u`` -- integer; the tail of an arc

        - ``v`` -- integer; the head of an arc

        EXAMPLES:

        On the :class:`CGraph` level, this always produces an error, as there are no vertices::

            sage: from sage.graphs.base.c_graph import CGraph
            sage: G = CGraph()
            sage: G.del_all_arcs(0,1)
            Traceback (most recent call last):
            ...
            LookupError: vertex (0) is not a vertex of the graph

        It works, once there are vertices and :meth:`del_arc_unsafe` is implemented::

            sage: from sage.graphs.base.sparse_graph import SparseGraph
            sage: G = SparseGraph(5)
            sage: G.add_arc_label(0,1,0)
            sage: G.add_arc_label(0,1,1)
            sage: G.add_arc_label(0,1,2)
            sage: G.add_arc_label(0,1,3)
            sage: G.del_all_arcs(0,1)
            sage: G.has_arc(0,1)
            False
            sage: G.arc_label(0,1)
            0
            sage: G.del_all_arcs(0,1)

            sage: from sage.graphs.base.dense_graph import DenseGraph
            sage: G = DenseGraph(5)
            sage: G.add_arc(0, 1)
            sage: G.has_arc(0, 1)
            True
            sage: G.del_all_arcs(0, 1)
            sage: G.has_arc(0, 1)
            False"""
    def del_arc_label(self, intu, intv, intl) -> Any:
        """CGraph.del_arc_label(self, int u, int v, int l)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 970)

        Delete an arc ``(u, v)`` with label ``l``.

        INPUT:

        - ``u``, ``v`` -- nonnegative integers; must be in self

        - ``l`` -- positive integer label, or zero for no label

        EXAMPLES::

            sage: from sage.graphs.base.sparse_graph import SparseGraph
            sage: G = SparseGraph(5)
            sage: G.add_arc_label(0,1,0)
            sage: G.add_arc_label(0,1,1)
            sage: G.add_arc_label(0,1,2)
            sage: G.add_arc_label(0,1,2)
            sage: G.add_arc_label(0,1,3)
            sage: G.del_arc_label(0,1,2)
            sage: G.all_arcs(0,1)
            [0, 3, 2, 1]
            sage: G.del_arc_label(0,1,0)
            sage: G.all_arcs(0,1)
            [3, 2, 1]"""
    def del_vertex(self, intv) -> Any:
        '''CGraph.del_vertex(self, int v)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 436)

        Delete the vertex `v`, along with all edges incident to it.

        If `v` is not in ``self``, fails silently.

        INPUT:

        - ``v`` -- nonnegative integer representing a vertex

        .. SEEALSO::

            - ``del_vertex_unsafe`` -- delete a vertex from a graph. This method
              is potentially unsafe. Use :meth:`del_vertex` instead

        EXAMPLES:

        Deleting vertices of sparse graphs::

            sage: from sage.graphs.base.sparse_graph import SparseGraph
            sage: G = SparseGraph(3)
            sage: G.add_arc(0, 1)
            sage: G.add_arc(0, 2)
            sage: G.add_arc(1, 2)
            sage: G.add_arc(2, 0)
            sage: G.del_vertex(2)
            sage: for i in range(2):
            ....:     for j in range(2):
            ....:         if G.has_arc(i, j):
            ....:             print("{} {}".format(i,j))
            0 1
            sage: G = SparseGraph(3)
            sage: G.add_arc(0, 1)
            sage: G.add_arc(0, 2)
            sage: G.add_arc(1, 2)
            sage: G.add_arc(2, 0)
            sage: G.del_vertex(1)
            sage: for i in range(3):
            ....:     for j in range(3):
            ....:         if G.has_arc(i, j):
            ....:             print("{} {}".format(i,j))
            0 2
            2 0

        Deleting vertices of dense graphs::

            sage: from sage.graphs.base.dense_graph import DenseGraph
            sage: G = DenseGraph(4)
            sage: G.add_arc(0, 1); G.add_arc(0, 2)
            sage: G.add_arc(3, 1); G.add_arc(3, 2)
            sage: G.add_arc(1, 2)
            sage: G.verts()
            [0, 1, 2, 3]
            sage: G.del_vertex(3); G.verts()
            [0, 1, 2]
            sage: for i in range(3):
            ....:     for j in range(3):
            ....:         if G.has_arc(i, j):
            ....:             print("{} {}".format(i,j))
            0 1
            0 2
            1 2

        If the vertex to be deleted is not in this graph, then fail silently::

            sage: from sage.graphs.base.sparse_graph import SparseGraph
            sage: G = SparseGraph(3)
            sage: G.verts()
            [0, 1, 2]
            sage: G.has_vertex(3)
            False
            sage: G.del_vertex(3)
            sage: G.verts()
            [0, 1, 2]

        ::

            sage: from sage.graphs.base.dense_graph import DenseGraph
            sage: G = DenseGraph(5)
            sage: G.verts()
            [0, 1, 2, 3, 4]
            sage: G.has_vertex(6)
            False
            sage: G.del_vertex(6)
            sage: G.verts()
            [0, 1, 2, 3, 4]'''
    def has_arc(self, intu, intv) -> bool:
        """CGraph.has_arc(self, int u, int v) -> bool

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 773)

        Check if the arc ``(u, v)`` is in this graph.

        INPUT:

        - ``u`` -- integer; the tail of an arc

        - ``v`` -- integer; the head of an arc

        OUTPUT:

        - Print a ``Not Implemented!`` message. This method is not implemented
          at the :class:`CGraph` level. A child class should provide a suitable
          implementation.

        EXAMPLES:

        On the :class:`CGraph` this always returns ``False``::

            sage: from sage.graphs.base.c_graph import CGraph
            sage: G = CGraph()
            sage: G.has_arc(0, 1)
            False

        It works once :class:`has_arc_unsafe` is implemented::

            sage: from sage.graphs.base.dense_graph import DenseGraph
            sage: G = DenseGraph(5)
            sage: G.add_arc(0, 1)
            sage: G.has_arc(1, 0)
            False
            sage: G.has_arc(0, 1)
            True

            sage: from sage.graphs.base.sparse_graph import SparseGraph
            sage: G = SparseGraph(5)
            sage: G.add_arc_label(0,1)
            sage: G.has_arc(1,0)
            False
            sage: G.has_arc(0,1)
            True"""
    def has_arc_label(self, intu, intv, intl) -> bool:
        """CGraph.has_arc_label(self, int u, int v, int l) -> bool

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 1002)

        Indicates whether there is an arc ``(u, v)`` with label ``l``.

        INPUT:

        - ``u``, ``v`` -- nonnegative integers; must be in self

        - ``l`` -- positive integer label, or zero for no label

        EXAMPLES::

            sage: from sage.graphs.base.sparse_graph import SparseGraph
            sage: G = SparseGraph(5)
            sage: G.add_arc_label(0,1,0)
            sage: G.add_arc_label(0,1,1)
            sage: G.add_arc_label(0,1,2)
            sage: G.add_arc_label(0,1,2)
            sage: G.has_arc_label(0,1,1)
            True
            sage: G.has_arc_label(0,1,2)
            True
            sage: G.has_arc_label(0,1,3)
            False"""
    def has_vertex(self, intn) -> bool:
        """CGraph.has_vertex(self, int n) -> bool

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 74)

        Determine whether the vertex `n` is in ``self``.

        This method is different from :meth:`check_vertex`. The current method
        returns a boolean to signify whether or not `n` is a vertex of this
        graph. On the other hand, :meth:`check_vertex` raises an error if
        `n` is not a vertex of this graph.

        INPUT:

        - ``n`` -- nonnegative integer representing a vertex

        OUTPUT: ``True`` if `n` is a vertex of this graph; ``False`` otherwise

        .. SEEALSO::

            - :meth:`check_vertex`
              -- raise an error if this graph does not contain a specific
              vertex.

        EXAMPLES:

        Upon initialization, a
        :class:`SparseGraph <sage.graphs.base.sparse_graph.SparseGraph>`
        or
        :class:`DenseGraph <sage.graphs.base.dense_graph.DenseGraph>`
        has the first ``nverts`` vertices::

            sage: from sage.graphs.base.sparse_graph import SparseGraph
            sage: S = SparseGraph(nverts=10, expected_degree=3, extra_vertices=10)
            sage: S.has_vertex(6)
            True
            sage: S.has_vertex(12)
            False
            sage: S.has_vertex(24)
            False
            sage: S.has_vertex(-19)
            False

        ::

            sage: from sage.graphs.base.dense_graph import DenseGraph
            sage: D = DenseGraph(nverts=10, extra_vertices=10)
            sage: D.has_vertex(6)
            True
            sage: D.has_vertex(12)
            False
            sage: D.has_vertex(24)
            False
            sage: D.has_vertex(-19)
            False"""
    def in_neighbors(self, intv) -> list:
        """CGraph.in_neighbors(self, int v) -> list

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 1249)

        Return the list of in-neighbors of the vertex ``v``.

        INPUT:

        - ``v`` -- integer representing a vertex of this graph

        OUTPUT:

        - Raise :exc:`NotImplementedError`. This method is not implemented at
          the :class:`CGraph` level. A child class should provide a suitable
          implementation.

        .. NOTE::

            Due to the implementation of SparseGraph, this method is much more
            expensive than out_neighbors_unsafe for SparseGraph's.

        EXAMPLES:

        On the :class:`CGraph` level, this always produces an error, as there are no vertices::

            sage: from sage.graphs.base.c_graph import CGraph
            sage: G = CGraph()
            sage: G.in_neighbors(0)
            Traceback (most recent call last):
            ...
            LookupError: vertex (0) is not a vertex of the graph

        It works, once there are vertices and :meth:`out_neighbors_unsafe` is implemented::

            sage: from sage.graphs.base.dense_graph import DenseGraph
            sage: G = DenseGraph(5)
            sage: G.add_arc(0, 1)
            sage: G.add_arc(3, 1)
            sage: G.add_arc(1, 3)
            sage: G.in_neighbors(1)
            [0, 3]
            sage: G.in_neighbors(3)
            [1]

            sage: from sage.graphs.base.sparse_graph import SparseGraph
            sage: G = SparseGraph(5)
            sage: G.add_arc(0,1)
            sage: G.add_arc(3,1)
            sage: G.add_arc(1,3)
            sage: G.in_neighbors(1)
            [0, 3]
            sage: G.in_neighbors(3)
            [1]"""
    def out_neighbors(self, intu) -> list:
        """CGraph.out_neighbors(self, int u) -> list

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 1195)

        Return the list of out-neighbors of the vertex ``u``.

        INPUT:

        - ``u`` -- integer representing a vertex of this graph

        EXAMPLES:

        On the :class:`CGraph` level, this always produces an error, as there are no vertices::

            sage: from sage.graphs.base.c_graph import CGraph
            sage: G = CGraph()
            sage: G.out_neighbors(0)
            Traceback (most recent call last):
            ...
            LookupError: vertex (0) is not a vertex of the graph

        It works, once there are vertices and :meth:`out_neighbors_unsafe` is implemented::

            sage: from sage.graphs.base.dense_graph import DenseGraph
            sage: G = DenseGraph(5)
            sage: G.add_arc(0, 1)
            sage: G.add_arc(1, 2)
            sage: G.add_arc(1, 3)
            sage: G.out_neighbors(0)
            [1]
            sage: G.out_neighbors(1)
            [2, 3]

            sage: from sage.graphs.base.sparse_graph import SparseGraph
            sage: G = SparseGraph(5)
            sage: G.add_arc(0,1)
            sage: G.add_arc(1,2)
            sage: G.add_arc(1,3)
            sage: G.out_neighbors(0)
            [1]
            sage: G.out_neighbors(1)
            [2, 3]"""
    def realloc(self, inttotal) -> Any:
        """CGraph.realloc(self, int total)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 613)

        Reallocate the number of vertices to use, without actually adding any.

        INPUT:

        - ``total`` -- integer; the total size to make the array of vertices

        OUTPUT:

        - Raise a :exc:`NotImplementedError`. This method is not implemented
          in this base class. A child class should provide a suitable
          implementation.

        .. SEEALSO::

            - :meth:`realloc <sage.graphs.base.sparse_graph.SparseGraph.realloc>`
              -- a ``realloc`` implementation for sparse graphs.

            - :meth:`realloc <sage.graphs.base.dense_graph.DenseGraph.realloc>`
              -- a ``realloc`` implementation for dense graphs.

        EXAMPLES:

        First, note that :meth:`realloc` is implemented for
        :class:`SparseGraph <sage.graphs.base.sparse_graph.SparseGraph>`
        and
        :class:`DenseGraph <sage.graphs.base.dense_graph.DenseGraph>`
        differently, and is not implemented at the
        :class:`CGraph` level::

            sage: from sage.graphs.base.c_graph import CGraph
            sage: G = CGraph()
            sage: G.realloc(20)
            Traceback (most recent call last):
            ...
            NotImplementedError

        The ``realloc`` implementation for sparse graphs::

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
            30

        The ``realloc`` implementation for dense graphs::

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
    @overload
    def verts(self) -> list:
        """CGraph.verts(self) -> list

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 584)

        Return a list of the vertices in ``self``.

        EXAMPLES::

            sage: from sage.graphs.base.sparse_graph import SparseGraph
            sage: S = SparseGraph(nverts=4, extra_vertices=4)
            sage: S.verts()
            [0, 1, 2, 3]
            sage: S.add_vertices([3,5,7,9])
            sage: S.verts()
            [0, 1, 2, 3, 5, 7, 9]
            sage: S.realloc(20)
            sage: S.verts()
            [0, 1, 2, 3, 5, 7, 9]

        ::

            sage: from sage.graphs.base.dense_graph import DenseGraph
            sage: G = DenseGraph(3, extra_vertices=2)
            sage: G.verts()
            [0, 1, 2]
            sage: G.del_vertex(0)
            sage: G.verts()
            [1, 2]"""
    @overload
    def verts(self) -> Any:
        """CGraph.verts(self) -> list

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 584)

        Return a list of the vertices in ``self``.

        EXAMPLES::

            sage: from sage.graphs.base.sparse_graph import SparseGraph
            sage: S = SparseGraph(nverts=4, extra_vertices=4)
            sage: S.verts()
            [0, 1, 2, 3]
            sage: S.add_vertices([3,5,7,9])
            sage: S.verts()
            [0, 1, 2, 3, 5, 7, 9]
            sage: S.realloc(20)
            sage: S.verts()
            [0, 1, 2, 3, 5, 7, 9]

        ::

            sage: from sage.graphs.base.dense_graph import DenseGraph
            sage: G = DenseGraph(3, extra_vertices=2)
            sage: G.verts()
            [0, 1, 2]
            sage: G.del_vertex(0)
            sage: G.verts()
            [1, 2]"""
    @overload
    def verts(self) -> Any:
        """CGraph.verts(self) -> list

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 584)

        Return a list of the vertices in ``self``.

        EXAMPLES::

            sage: from sage.graphs.base.sparse_graph import SparseGraph
            sage: S = SparseGraph(nverts=4, extra_vertices=4)
            sage: S.verts()
            [0, 1, 2, 3]
            sage: S.add_vertices([3,5,7,9])
            sage: S.verts()
            [0, 1, 2, 3, 5, 7, 9]
            sage: S.realloc(20)
            sage: S.verts()
            [0, 1, 2, 3, 5, 7, 9]

        ::

            sage: from sage.graphs.base.dense_graph import DenseGraph
            sage: G = DenseGraph(3, extra_vertices=2)
            sage: G.verts()
            [0, 1, 2]
            sage: G.del_vertex(0)
            sage: G.verts()
            [1, 2]"""
    @overload
    def verts(self) -> Any:
        """CGraph.verts(self) -> list

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 584)

        Return a list of the vertices in ``self``.

        EXAMPLES::

            sage: from sage.graphs.base.sparse_graph import SparseGraph
            sage: S = SparseGraph(nverts=4, extra_vertices=4)
            sage: S.verts()
            [0, 1, 2, 3]
            sage: S.add_vertices([3,5,7,9])
            sage: S.verts()
            [0, 1, 2, 3, 5, 7, 9]
            sage: S.realloc(20)
            sage: S.verts()
            [0, 1, 2, 3, 5, 7, 9]

        ::

            sage: from sage.graphs.base.dense_graph import DenseGraph
            sage: G = DenseGraph(3, extra_vertices=2)
            sage: G.verts()
            [0, 1, 2]
            sage: G.del_vertex(0)
            sage: G.verts()
            [1, 2]"""
    @overload
    def verts(self) -> Any:
        """CGraph.verts(self) -> list

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 584)

        Return a list of the vertices in ``self``.

        EXAMPLES::

            sage: from sage.graphs.base.sparse_graph import SparseGraph
            sage: S = SparseGraph(nverts=4, extra_vertices=4)
            sage: S.verts()
            [0, 1, 2, 3]
            sage: S.add_vertices([3,5,7,9])
            sage: S.verts()
            [0, 1, 2, 3, 5, 7, 9]
            sage: S.realloc(20)
            sage: S.verts()
            [0, 1, 2, 3, 5, 7, 9]

        ::

            sage: from sage.graphs.base.dense_graph import DenseGraph
            sage: G = DenseGraph(3, extra_vertices=2)
            sage: G.verts()
            [0, 1, 2]
            sage: G.del_vertex(0)
            sage: G.verts()
            [1, 2]"""
    @overload
    def verts(self) -> Any:
        """CGraph.verts(self) -> list

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 584)

        Return a list of the vertices in ``self``.

        EXAMPLES::

            sage: from sage.graphs.base.sparse_graph import SparseGraph
            sage: S = SparseGraph(nverts=4, extra_vertices=4)
            sage: S.verts()
            [0, 1, 2, 3]
            sage: S.add_vertices([3,5,7,9])
            sage: S.verts()
            [0, 1, 2, 3, 5, 7, 9]
            sage: S.realloc(20)
            sage: S.verts()
            [0, 1, 2, 3, 5, 7, 9]

        ::

            sage: from sage.graphs.base.dense_graph import DenseGraph
            sage: G = DenseGraph(3, extra_vertices=2)
            sage: G.verts()
            [0, 1, 2]
            sage: G.del_vertex(0)
            sage: G.verts()
            [1, 2]"""

class CGraphBackend(sage.graphs.base.graph_backends.GenericGraphBackend):
    """File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 1315)

        Base class for sparse and dense graph backends.

        ::

            sage: from sage.graphs.base.c_graph import CGraphBackend

        This class is extended by
        :class:`SparseGraphBackend <sage.graphs.base.sparse_graph.SparseGraphBackend>`
        and
        :class:`DenseGraphBackend <sage.graphs.base.dense_graph.DenseGraphBackend>`,
        which are fully functional backends. This class is mainly just for vertex
        functions, which are the same for both. A :class:`CGraphBackend` will not
        work on its own::

            sage: from sage.graphs.base.c_graph import CGraphBackend
            sage: CGB = CGraphBackend()
            sage: CGB.degree(0, True)
            Traceback (most recent call last):
            ...
            NotImplementedError: a derived class must return ``self._cg``

        The appropriate way to use these backends is via Sage graphs::

            sage: G = Graph(30)
            sage: G.add_edges([(0,1), (0,3), (4,5), (9, 23)])
            sage: G.edges(sort=True, labels=False)
            [(0, 1), (0, 3), (4, 5), (9, 23)]

        This class handles the labels of vertices and edges. For vertices it uses
        two dictionaries ``vertex_labels`` and ``vertex_ints``. They are just
        opposite of each other: ``vertex_ints`` makes a translation from label to
        integers (that are internally used) and ``vertex_labels`` make the
        translation from internally used integers to actual labels. This class tries
        hard to avoid translation if possible. This will work only if the graph is
        built on integers from `0` to `n-1` and the vertices are basically added in
        increasing order.

        .. SEEALSO::

            - :class:`SparseGraphBackend <sage.graphs.base.sparse_graph.SparseGraphBackend>`
              -- backend for sparse graphs.

            - :class:`DenseGraphBackend <sage.graphs.base.dense_graph.DenseGraphBackend>`
              -- backend for dense graphs.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
    def add_edge(self, u, v, l, booldirected) -> Any:
        """CGraphBackend.add_edge(self, u, v, l, bool directed)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 2334)

        Add the edge ``(u,v)`` to ``self``.

        INPUT:

        - ``u``, ``v`` -- the vertices of the edge

        - ``l`` -- the edge label

        - ``directed`` -- if ``False``, also add ``(v,u)``

        .. NOTE::

            The input ``l`` is ignored if the backend
            does not support labels.

        EXAMPLES::

            sage: D = sage.graphs.base.sparse_graph.SparseGraphBackend(9)
            sage: D.add_edge(0,1,None,False)
            sage: list(D.iterator_edges(range(9), True))
            [(0, 1, None)]

        ::

            sage: D = sage.graphs.base.dense_graph.DenseGraphBackend(9)
            sage: D.add_edge(0, 1, None, False)
            sage: list(D.iterator_edges(range(9), True))
            [(0, 1, None)]

        TESTS::

            sage: D = DiGraph(sparse=True)
            sage: D.add_edge(0,1,2)
            sage: D.add_edge(0,1,3)
            sage: D.edges(sort=True)
            [(0, 1, 3)]

        Check :issue:`22991` for sparse backend::

            sage: G = Graph(3, sparse=True)
            sage: G.add_edge(0,0)
            Traceback (most recent call last):
            ...
            ValueError: cannot add edge from 0 to 0 in graph without loops
            sage: G = Graph(3, sparse=True, loops=True)
            sage: G.add_edge(0,0); G.edges(sort=True)
            [(0, 0, None)]

        Check :issue:`22991` for dense backend::

            sage: G = Graph(3, sparse=False)
            sage: G.add_edge(0,0)
            Traceback (most recent call last):
            ...
            ValueError: cannot add edge from 0 to 0 in graph without loops
            sage: G = Graph(3, sparse=True, loops=True)
            sage: G.add_edge(0, 0); G.edges(sort=True)
            [(0, 0, None)]

        Remove edges correctly when multiedges are not allowed (:issue:`28077`)::

            sage: D = DiGraph(multiedges=False)
            sage: D.add_edge(1, 2, 'A')
            sage: D.add_edge(1, 2, 'B')
            sage: D.delete_edge(1, 2)
            sage: D.incoming_edges(2)
            []
            sage: D.shortest_path(1, 2)
            []"""
    def add_edges(self, edges, booldirected, boolremove_loops=...) -> Any:
        """CGraphBackend.add_edges(self, edges, bool directed, bool remove_loops=False)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 2300)

        Add edges from a list.

        INPUT:

        - ``edges`` -- the edges to be added; can either be of the form
          ``(u,v)`` or ``(u,v,l)``

        - ``directed`` -- if ``False``, add ``(v,u)`` as well as ``(u,v)``

        - ``remove_loops`` -- if ``True``, remove loops

        EXAMPLES::

            sage: D = sage.graphs.base.sparse_graph.SparseGraphBackend(9)
            sage: D.add_edges([(0,1), (2,3), (4,5), (5,6)], False)
            sage: list(D.iterator_edges(range(9), True))
            [(0, 1, None),
             (2, 3, None),
             (4, 5, None),
             (5, 6, None)]"""
    def add_vertex(self, name) -> Any:
        """CGraphBackend.add_vertex(self, name)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 1682)

        Add a vertex to ``self``.

        INPUT:

        - ``name`` -- the vertex to be added (must be hashable). If ``None``,
          a new name is created

        OUTPUT:

        - If ``name = None``, the new vertex name is returned. ``None``
          otherwise.

        .. SEEALSO::

            - :meth:`add_vertices` -- add a bunch of vertices of this graph

            - :meth:`has_vertex` -- returns whether or not this graph has a
              specific vertex

        EXAMPLES::

            sage: D = sage.graphs.base.dense_graph.DenseGraphBackend(9)
            sage: D.add_vertex(10)
            sage: D.add_vertex([])
            Traceback (most recent call last):
            ...
            TypeError: unhashable type: 'list'

        ::

            sage: S = sage.graphs.base.sparse_graph.SparseGraphBackend(9)
            sage: S.add_vertex(10)
            sage: S.add_vertex([])
            Traceback (most recent call last):
            ...
            TypeError: unhashable type: 'list'"""
    def add_vertices(self, vertices) -> Any:
        """CGraphBackend.add_vertices(self, vertices)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 1734)

        Add vertices to ``self``.

        INPUT:

        - ``vertices`` -- iterator of vertex labels; a new name is created, used
          and returned in the output list for all ``None`` values in
          ``vertices``

        OUTPUT:

        Generated names of new vertices if there is at least one ``None`` value
        present in ``vertices``. ``None`` otherwise.

        .. SEEALSO::

            - :meth:`add_vertex` -- add a vertex to this graph

        EXAMPLES::

            sage: D = sage.graphs.base.sparse_graph.SparseGraphBackend(1)
            sage: D.add_vertices([1, 2, 3])
            sage: D.add_vertices([None] * 4)
            [4, 5, 6, 7]

        ::

            sage: G = sage.graphs.base.sparse_graph.SparseGraphBackend(0)
            sage: G.add_vertices([0, 1])
            sage: list(G.iterator_verts(None))
            [0, 1]
            sage: list(G.iterator_edges([0, 1], True))
            []

        ::

            sage: import sage.graphs.base.dense_graph
            sage: D = sage.graphs.base.dense_graph.DenseGraphBackend(9)
            sage: D.add_vertices([10, 11, 12])"""
    def bidirectional_dijkstra(self, x, y, weight_function=..., distance_flag=...) -> Any:
        """CGraphBackend.bidirectional_dijkstra(self, x, y, weight_function=None, distance_flag=False)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 3998)

        Return the shortest path or distance from ``x`` to ``y`` using a
        bidirectional version of Dijkstra's algorithm.

        INPUT:

        - ``x`` -- the starting vertex in the shortest path from ``x`` to ``y``

        - ``y`` -- the end vertex in the shortest path from ``x`` to ``y``

        - ``weight_function`` -- function (default: ``None``); a function that
          inputs an edge ``(u, v, l)`` and outputs its weight. If ``None``, we
          use the edge label ``l`` as a weight, if ``l`` is not ``None``, else
          ``1`` as a weight.

        - ``distance_flag`` -- boolean (default: ``False``); when set to
          ``True``, the shortest path distance from ``x`` to ``y`` is returned
          instead of the path.

        OUTPUT:

        - A list of vertices in the shortest path from ``x`` to ``y`` or
          distance from ``x`` to ``y`` is returned depending upon the value of
          parameter ``distance_flag``

        EXAMPLES::

            sage: G = Graph(graphs.PetersenGraph())
            sage: for (u, v) in G.edges(sort=True, labels=None):
            ....:     G.set_edge_label(u, v, 1)
            sage: G.shortest_path(0, 1, by_weight=True)
            [0, 1]
            sage: G.shortest_path_length(0, 1, by_weight=True)
            1
            sage: G = DiGraph([(1, 2, {'weight':1}), (1, 3, {'weight':5}), (2, 3, {'weight':1})])
            sage: G.shortest_path(1, 3, weight_function=lambda e:e[2]['weight'])
            [1, 2, 3]
            sage: G.shortest_path_length(1, 3, weight_function=lambda e:e[2]['weight'])
            2

        TESTS:

        Bugfix from :issue:`7673` ::

            sage: G = Graph([(0, 1, 9), (0, 2, 8), (1, 2, 7)])
            sage: G.shortest_path_length(0, 1, by_weight=True)
            9

        Bugfix from :issue:`28221` ::

            sage: G = Graph([(0, 1, 9.2), (0, 2, 4.5), (1, 2, 4.6)])
            sage: G.shortest_path_length(0, 1, by_weight=True)
            9.1

        Bugfix from :issue:`27464` ::

            sage: G = DiGraph({0: [1, 2], 1: [4], 2: [3, 4], 4: [5], 5: [6]}, multiedges=True)
            sage: for u, v in list(G.edges(labels=None, sort=False)):
            ....:     G.set_edge_label(u, v, 1)
            sage: G.distance(0, 5, by_weight=true)
            3"""
    def bidirectional_dijkstra_special(self, x, y, weight_function=..., exclude_vertices=..., exclude_edges=..., include_vertices=..., distance_flag=..., reduced_weight=...) -> Any:
        """CGraphBackend.bidirectional_dijkstra_special(self, x, y, weight_function=None, exclude_vertices=None, exclude_edges=None, include_vertices=None, distance_flag=False, reduced_weight=None)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 3760)

        Return the shortest path or distance from ``x`` to ``y`` using a
        bidirectional version of Dijkstra's algorithm.

        This method is an extension of :meth:`bidirectional_dijkstra` method
        enabling to exclude vertices and/or edges from the search for the
        shortest path between ``x`` and ``y``.

        This method also has ``include_vertices`` option enabling to include the
        vertices which will be used to search for the shortest path between
        ``x`` and ``y``.

        INPUT:

        - ``x`` -- the starting vertex in the shortest path from ``x`` to ``y``

        - ``y`` -- the end vertex in the shortest path from ``x`` to ``y``

        - ``exclude_vertices`` -- iterable container (default: ``None``);
          iterable of vertices to exclude from the graph while calculating the
          shortest path from ``x`` to ``y``

        - ``exclude_edges`` -- iterable container (default: ``None``); iterable
          of edges to exclude from the graph while calculating the shortest path
          from ``x`` to ``y``

        - ``include_vertices`` -- iterable container (default: ``None``);
          iterable of vertices to consider in the graph while calculating the
          shortest path from ``x`` to ``y``

        - ``weight_function`` -- function (default: ``None``); a function that
          inputs an edge ``(u, v, l)`` and outputs its weight. If ``None``, we
          use the edge label ``l`` as a weight, if ``l`` is not ``None``, else
          ``1`` as a weight.

        - ``distance_flag`` -- boolean (default: ``False``); when set to
          ``True``, the shortest path distance from ``x`` to ``y`` is returned
          instead of the path.

        - ``reduced_weight`` -- dictionary (default: ``None``); a dictionary
          that takes as input an edge ``(u, v)`` and outputs its reduced weight

        OUTPUT:

        - A list of vertices in the shortest path from ``x`` to ``y`` or
          distance from ``x`` to ``y`` is returned depending upon the value of
          parameter ``distance_flag``

        EXAMPLES::

            sage: G = Graph([(1, 2, 20), (2, 3, 10), (3, 4, 30), (1, 5, 20), (5, 6, 10), (6, 4, 50), (4, 7, 5)])
            sage: G._backend.bidirectional_dijkstra_special(1, 4, weight_function=lambda e:e[2])
            [1, 2, 3, 4]
            sage: G._backend.bidirectional_dijkstra_special(1, 4, weight_function=lambda e:e[2], exclude_vertices=[2], exclude_edges=[(3, 4)])
            [1, 5, 6, 4]
            sage: G._backend.bidirectional_dijkstra_special(1, 4, weight_function=lambda e:e[2], exclude_vertices=[2, 7])
            [1, 5, 6, 4]
            sage: G._backend.bidirectional_dijkstra_special(1, 4, weight_function=lambda e:e[2],  exclude_edges=[(5, 6)])
            [1, 2, 3, 4]
            sage: G._backend.bidirectional_dijkstra_special(1, 4, weight_function=lambda e:e[2],  include_vertices=[1, 5, 6, 4])
            [1, 5, 6, 4]"""
    def breadth_first_search(self, v, reverse=..., ignore_direction=..., report_distance=..., edges=..., forbidden_vertices=...) -> Any:
        '''CGraphBackend.breadth_first_search(self, v, reverse=False, ignore_direction=False, report_distance=False, edges=False, forbidden_vertices=None)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 4413)

        Return a breadth-first search from vertex ``v``.

        INPUT:

        - ``v`` -- a vertex from which to start the breadth-first search

        - ``reverse`` -- boolean (default: ``False``); this is only relevant to
          digraphs. If this is a digraph, consider the reversed graph in which
          the out-neighbors become the in-neighbors and vice versa.

        - ``ignore_direction`` -- boolean (default: ``False``); this is only
          relevant to digraphs. If this is a digraph, ignore all orientations
          and consider the graph as undirected.

        - ``report_distance`` -- boolean (default: ``False``); if ``True``,
          reports pairs ``(vertex, distance)`` where ``distance`` is the
          distance from the ``start`` nodes. If ``False`` only the vertices are
          reported.

        - ``edges`` -- boolean (default: ``False``); whether to return the edges
          of the BFS tree in the order of visit or the vertices (default).
          Edges are directed in root to leaf orientation of the tree.

          Note that parameters ``edges`` and ``report_distance`` cannot be
          ``True`` simultaneously.

        - ``forbidden_vertices`` -- list (default: ``None``); set of vertices to
          avoid during the search. The start vertex ``v`` cannot be in this set.

        ALGORITHM:

        Below is a general template for breadth-first search.

        - **Input:** A directed or undirected graph `G = (V, E)` of order
          `n > 0`. A vertex `s` from which to start the search. The vertices
          are numbered from 1 to `n = |V|`, i.e. `V = \\{1, 2, \\dots, n\\}`.

        - **Output:** A list `D` of distances of all vertices from `s`. A
          tree `T` rooted at `s`.

        #. `Q \\leftarrow [s]`  # a queue of nodes to visit
        #. `D \\leftarrow [\\infty, \\infty, \\dots, \\infty]`  # `n` copies of `\\infty`
        #. `D[s] \\leftarrow 0`
        #. `T \\leftarrow [\\,]`
        #. while `\\text{length}(Q) > 0` do

           #. `v \\leftarrow \\text{dequeue}(Q)`
           #. for each `w \\in \\text{adj}(v)` do  # for digraphs, use out-neighbor set `\\text{oadj}(v)`

              #. if `D[w] = \\infty` then

                 #. `D[w] \\leftarrow D[v] + 1`
                 #. `\\text{enqueue}(Q, w)`
                 #. `\\text{append}(T, vw)`
        #. return `(D, T)`

        .. SEEALSO::

            - :meth:`breadth_first_search <sage.graphs.generic_graph.GenericGraph.breadth_first_search>`
              -- breadth-first search for generic graphs.

            - :meth:`depth_first_search <sage.graphs.generic_graph.GenericGraph.depth_first_search>`
              -- depth-first search for generic graphs.

            - :meth:`depth_first_search`
              -- depth-first search for fast compiled graphs.

        EXAMPLES:

        Breadth-first search of the Petersen graph starting at vertex 0::

            sage: G = Graph(graphs.PetersenGraph())
            sage: list(G.breadth_first_search(0))
            [0, 1, 4, 5, 2, 6, 3, 9, 7, 8]

        Visiting European countries using breadth-first search::

            sage: G = graphs.EuropeMap(continental=True)
            sage: list(G.breadth_first_search("Portugal"))
            [\'Portugal\', \'Spain\', ..., \'Greece\']

        Avoiding some countries:

            sage: list(G.breadth_first_search("Portugal",
            ....:                      forbidden_vertices=["Germany","Italy"]))
            [\'Portugal\', \'Spain\', ..., \'Sweden\']

        TESTS:

        The start vertex cannot be forbidden::

            sage: G = graphs.PetersenGraph()
            sage: list(G.breadth_first_search(0, forbidden_vertices=[0]))
            Traceback (most recent call last):
            ...
            ValueError: the start vertex is in the set of forbidden vertices'''
    @overload
    def c_graph(self) -> Any:
        """CGraphBackend.c_graph(self)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 1373)

        Return the ``._cg`` and ``._cg_rev`` attributes.

        .. NOTE::

            The ``._cg_rev`` attribute has been removed and hence ``None`` is returned.

        EXAMPLES::

            sage: cg,cg_rev = graphs.PetersenGraph()._backend.c_graph()
            sage: cg
            <sage.graphs.base.sparse_graph.SparseGraph object at ...>"""
    @overload
    def c_graph(self) -> Any:
        """CGraphBackend.c_graph(self)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 1373)

        Return the ``._cg`` and ``._cg_rev`` attributes.

        .. NOTE::

            The ``._cg_rev`` attribute has been removed and hence ``None`` is returned.

        EXAMPLES::

            sage: cg,cg_rev = graphs.PetersenGraph()._backend.c_graph()
            sage: cg
            <sage.graphs.base.sparse_graph.SparseGraph object at ...>"""
    @overload
    def degree(self, v, directed) -> Any:
        '''CGraphBackend.degree(self, v, directed)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 1973)

        Return the degree of the vertex ``v``.

        INPUT:

        - ``v`` -- a vertex of the graph

        - ``directed`` -- boolean; whether to take into account the
          orientation of this graph in counting the degree of ``v``

        OUTPUT: the degree of vertex ``v``

        EXAMPLES::

            sage: from sage.graphs.base.sparse_graph import SparseGraphBackend
            sage: B = SparseGraphBackend(7)
            sage: B.degree(3, False)
            0

        TESTS:

        Ensure that issue :issue:`8395` is fixed. ::

            sage: def my_add_edges(G, m, n):
            ....:     for i in range(m):
            ....:         u = randint(0, n)
            ....:         v = randint(0, n)
            ....:         G.add_edge(u, v)
            sage: G = Graph({1:[1]}); G
            Looped graph on 1 vertex
            sage: G.edges(sort=True, labels=False)
            [(1, 1)]
            sage: G.degree(); G.size()
            [2]
            1
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: G = Graph({1:[1,2], 2:[2,3]}, loops=True); G
            Looped graph on 3 vertices
            sage: my_add_edges(G, 100, 50)
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: G = Graph({1:[2,2], 2:[3]}); G
            Multi-graph on 3 vertices
            sage: G.edges(sort=True, labels=False)
            [(1, 2), (1, 2), (2, 3)]
            sage: G.degree(); G.size()
            [2, 3, 1]
            3
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: G.allow_loops(True); G
            Looped multi-graph on 3 vertices
            sage: my_add_edges(G, 100, 50)
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: D = DiGraph({1:[2], 2:[1,3]}); D
            Digraph on 3 vertices
            sage: D.edges(sort=True, labels=False)
            [(1, 2), (2, 1), (2, 3)]
            sage: D.degree(); D.size()
            [2, 3, 1]
            3
            sage: sum(D.degree()) == 2 * D.size()
            True
            sage: D.allow_loops(True); D
            Looped digraph on 3 vertices
            sage: my_add_edges(D, 100, 50)
            sage: sum(D.degree()) == 2 * D.size()
            True
            sage: D.allow_multiple_edges(True)
            sage: my_add_edges(D, 200, 50)
            sage: sum(D.degree()) == 2 * D.size()
            True
            sage: G = Graph({1:[2,2,2]})
            sage: G.allow_loops(True)
            sage: G.add_edge(1,1)
            sage: G.add_edge(1,1)
            sage: G.edges(sort=True, labels=False)
            [(1, 1), (1, 1), (1, 2), (1, 2), (1, 2)]
            sage: G.degree(1)
            7
            sage: G.allow_loops(False)
            sage: G.edges(sort=True, labels=False)
            [(1, 2), (1, 2), (1, 2)]
            sage: G.degree(1)
            3
            sage: G = Graph({1:{2:[\'a\',\'a\',\'a\']}})
            sage: G.allow_loops(True)
            sage: G.add_edge(1,1,\'b\')
            sage: G.add_edge(1,1,\'b\')
            sage: G.add_edge(1,1)
            sage: G.add_edge(1,1)
            sage: G.edges_incident()
            [(1, 1, None), (1, 1, None), (1, 1, \'b\'), (1, 1, \'b\'), (1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            11
            sage: G.allow_loops(False)
            sage: G.edges(sort=True)
            [(1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            3
            sage: G = Graph({1:{2:[\'a\',\'a\',\'a\']}})
            sage: G.allow_loops(True)
            sage: G.add_edge(1,1,\'b\')
            sage: G.add_edge(1,1,\'b\')
            sage: G.edges(sort=True)
            [(1, 1, \'b\'), (1, 1, \'b\'), (1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            7
            sage: G.allow_loops(False)
            sage: G.edges(sort=True)
            [(1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            3

        Ensure that :issue:`13664` is fixed ::

            sage: W = WeylGroup(["A",1])                                                # needs sage.combinat sage.groups
            sage: G = W.cayley_graph()                                                  # needs sage.combinat sage.groups
            sage: Graph(G).degree()                                                     # needs sage.combinat sage.groups
            [1, 1]
            sage: h = Graph()
            sage: h.add_edge(1,2,"a")
            sage: h.add_edge(1,2,"a")
            sage: h.degree()
            [1, 1]'''
    @overload
    def degree(self) -> Any:
        '''CGraphBackend.degree(self, v, directed)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 1973)

        Return the degree of the vertex ``v``.

        INPUT:

        - ``v`` -- a vertex of the graph

        - ``directed`` -- boolean; whether to take into account the
          orientation of this graph in counting the degree of ``v``

        OUTPUT: the degree of vertex ``v``

        EXAMPLES::

            sage: from sage.graphs.base.sparse_graph import SparseGraphBackend
            sage: B = SparseGraphBackend(7)
            sage: B.degree(3, False)
            0

        TESTS:

        Ensure that issue :issue:`8395` is fixed. ::

            sage: def my_add_edges(G, m, n):
            ....:     for i in range(m):
            ....:         u = randint(0, n)
            ....:         v = randint(0, n)
            ....:         G.add_edge(u, v)
            sage: G = Graph({1:[1]}); G
            Looped graph on 1 vertex
            sage: G.edges(sort=True, labels=False)
            [(1, 1)]
            sage: G.degree(); G.size()
            [2]
            1
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: G = Graph({1:[1,2], 2:[2,3]}, loops=True); G
            Looped graph on 3 vertices
            sage: my_add_edges(G, 100, 50)
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: G = Graph({1:[2,2], 2:[3]}); G
            Multi-graph on 3 vertices
            sage: G.edges(sort=True, labels=False)
            [(1, 2), (1, 2), (2, 3)]
            sage: G.degree(); G.size()
            [2, 3, 1]
            3
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: G.allow_loops(True); G
            Looped multi-graph on 3 vertices
            sage: my_add_edges(G, 100, 50)
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: D = DiGraph({1:[2], 2:[1,3]}); D
            Digraph on 3 vertices
            sage: D.edges(sort=True, labels=False)
            [(1, 2), (2, 1), (2, 3)]
            sage: D.degree(); D.size()
            [2, 3, 1]
            3
            sage: sum(D.degree()) == 2 * D.size()
            True
            sage: D.allow_loops(True); D
            Looped digraph on 3 vertices
            sage: my_add_edges(D, 100, 50)
            sage: sum(D.degree()) == 2 * D.size()
            True
            sage: D.allow_multiple_edges(True)
            sage: my_add_edges(D, 200, 50)
            sage: sum(D.degree()) == 2 * D.size()
            True
            sage: G = Graph({1:[2,2,2]})
            sage: G.allow_loops(True)
            sage: G.add_edge(1,1)
            sage: G.add_edge(1,1)
            sage: G.edges(sort=True, labels=False)
            [(1, 1), (1, 1), (1, 2), (1, 2), (1, 2)]
            sage: G.degree(1)
            7
            sage: G.allow_loops(False)
            sage: G.edges(sort=True, labels=False)
            [(1, 2), (1, 2), (1, 2)]
            sage: G.degree(1)
            3
            sage: G = Graph({1:{2:[\'a\',\'a\',\'a\']}})
            sage: G.allow_loops(True)
            sage: G.add_edge(1,1,\'b\')
            sage: G.add_edge(1,1,\'b\')
            sage: G.add_edge(1,1)
            sage: G.add_edge(1,1)
            sage: G.edges_incident()
            [(1, 1, None), (1, 1, None), (1, 1, \'b\'), (1, 1, \'b\'), (1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            11
            sage: G.allow_loops(False)
            sage: G.edges(sort=True)
            [(1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            3
            sage: G = Graph({1:{2:[\'a\',\'a\',\'a\']}})
            sage: G.allow_loops(True)
            sage: G.add_edge(1,1,\'b\')
            sage: G.add_edge(1,1,\'b\')
            sage: G.edges(sort=True)
            [(1, 1, \'b\'), (1, 1, \'b\'), (1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            7
            sage: G.allow_loops(False)
            sage: G.edges(sort=True)
            [(1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            3

        Ensure that :issue:`13664` is fixed ::

            sage: W = WeylGroup(["A",1])                                                # needs sage.combinat sage.groups
            sage: G = W.cayley_graph()                                                  # needs sage.combinat sage.groups
            sage: Graph(G).degree()                                                     # needs sage.combinat sage.groups
            [1, 1]
            sage: h = Graph()
            sage: h.add_edge(1,2,"a")
            sage: h.add_edge(1,2,"a")
            sage: h.degree()
            [1, 1]'''
    @overload
    def degree(self) -> Any:
        '''CGraphBackend.degree(self, v, directed)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 1973)

        Return the degree of the vertex ``v``.

        INPUT:

        - ``v`` -- a vertex of the graph

        - ``directed`` -- boolean; whether to take into account the
          orientation of this graph in counting the degree of ``v``

        OUTPUT: the degree of vertex ``v``

        EXAMPLES::

            sage: from sage.graphs.base.sparse_graph import SparseGraphBackend
            sage: B = SparseGraphBackend(7)
            sage: B.degree(3, False)
            0

        TESTS:

        Ensure that issue :issue:`8395` is fixed. ::

            sage: def my_add_edges(G, m, n):
            ....:     for i in range(m):
            ....:         u = randint(0, n)
            ....:         v = randint(0, n)
            ....:         G.add_edge(u, v)
            sage: G = Graph({1:[1]}); G
            Looped graph on 1 vertex
            sage: G.edges(sort=True, labels=False)
            [(1, 1)]
            sage: G.degree(); G.size()
            [2]
            1
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: G = Graph({1:[1,2], 2:[2,3]}, loops=True); G
            Looped graph on 3 vertices
            sage: my_add_edges(G, 100, 50)
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: G = Graph({1:[2,2], 2:[3]}); G
            Multi-graph on 3 vertices
            sage: G.edges(sort=True, labels=False)
            [(1, 2), (1, 2), (2, 3)]
            sage: G.degree(); G.size()
            [2, 3, 1]
            3
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: G.allow_loops(True); G
            Looped multi-graph on 3 vertices
            sage: my_add_edges(G, 100, 50)
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: D = DiGraph({1:[2], 2:[1,3]}); D
            Digraph on 3 vertices
            sage: D.edges(sort=True, labels=False)
            [(1, 2), (2, 1), (2, 3)]
            sage: D.degree(); D.size()
            [2, 3, 1]
            3
            sage: sum(D.degree()) == 2 * D.size()
            True
            sage: D.allow_loops(True); D
            Looped digraph on 3 vertices
            sage: my_add_edges(D, 100, 50)
            sage: sum(D.degree()) == 2 * D.size()
            True
            sage: D.allow_multiple_edges(True)
            sage: my_add_edges(D, 200, 50)
            sage: sum(D.degree()) == 2 * D.size()
            True
            sage: G = Graph({1:[2,2,2]})
            sage: G.allow_loops(True)
            sage: G.add_edge(1,1)
            sage: G.add_edge(1,1)
            sage: G.edges(sort=True, labels=False)
            [(1, 1), (1, 1), (1, 2), (1, 2), (1, 2)]
            sage: G.degree(1)
            7
            sage: G.allow_loops(False)
            sage: G.edges(sort=True, labels=False)
            [(1, 2), (1, 2), (1, 2)]
            sage: G.degree(1)
            3
            sage: G = Graph({1:{2:[\'a\',\'a\',\'a\']}})
            sage: G.allow_loops(True)
            sage: G.add_edge(1,1,\'b\')
            sage: G.add_edge(1,1,\'b\')
            sage: G.add_edge(1,1)
            sage: G.add_edge(1,1)
            sage: G.edges_incident()
            [(1, 1, None), (1, 1, None), (1, 1, \'b\'), (1, 1, \'b\'), (1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            11
            sage: G.allow_loops(False)
            sage: G.edges(sort=True)
            [(1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            3
            sage: G = Graph({1:{2:[\'a\',\'a\',\'a\']}})
            sage: G.allow_loops(True)
            sage: G.add_edge(1,1,\'b\')
            sage: G.add_edge(1,1,\'b\')
            sage: G.edges(sort=True)
            [(1, 1, \'b\'), (1, 1, \'b\'), (1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            7
            sage: G.allow_loops(False)
            sage: G.edges(sort=True)
            [(1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            3

        Ensure that :issue:`13664` is fixed ::

            sage: W = WeylGroup(["A",1])                                                # needs sage.combinat sage.groups
            sage: G = W.cayley_graph()                                                  # needs sage.combinat sage.groups
            sage: Graph(G).degree()                                                     # needs sage.combinat sage.groups
            [1, 1]
            sage: h = Graph()
            sage: h.add_edge(1,2,"a")
            sage: h.add_edge(1,2,"a")
            sage: h.degree()
            [1, 1]'''
    @overload
    def degree(self) -> Any:
        '''CGraphBackend.degree(self, v, directed)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 1973)

        Return the degree of the vertex ``v``.

        INPUT:

        - ``v`` -- a vertex of the graph

        - ``directed`` -- boolean; whether to take into account the
          orientation of this graph in counting the degree of ``v``

        OUTPUT: the degree of vertex ``v``

        EXAMPLES::

            sage: from sage.graphs.base.sparse_graph import SparseGraphBackend
            sage: B = SparseGraphBackend(7)
            sage: B.degree(3, False)
            0

        TESTS:

        Ensure that issue :issue:`8395` is fixed. ::

            sage: def my_add_edges(G, m, n):
            ....:     for i in range(m):
            ....:         u = randint(0, n)
            ....:         v = randint(0, n)
            ....:         G.add_edge(u, v)
            sage: G = Graph({1:[1]}); G
            Looped graph on 1 vertex
            sage: G.edges(sort=True, labels=False)
            [(1, 1)]
            sage: G.degree(); G.size()
            [2]
            1
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: G = Graph({1:[1,2], 2:[2,3]}, loops=True); G
            Looped graph on 3 vertices
            sage: my_add_edges(G, 100, 50)
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: G = Graph({1:[2,2], 2:[3]}); G
            Multi-graph on 3 vertices
            sage: G.edges(sort=True, labels=False)
            [(1, 2), (1, 2), (2, 3)]
            sage: G.degree(); G.size()
            [2, 3, 1]
            3
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: G.allow_loops(True); G
            Looped multi-graph on 3 vertices
            sage: my_add_edges(G, 100, 50)
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: D = DiGraph({1:[2], 2:[1,3]}); D
            Digraph on 3 vertices
            sage: D.edges(sort=True, labels=False)
            [(1, 2), (2, 1), (2, 3)]
            sage: D.degree(); D.size()
            [2, 3, 1]
            3
            sage: sum(D.degree()) == 2 * D.size()
            True
            sage: D.allow_loops(True); D
            Looped digraph on 3 vertices
            sage: my_add_edges(D, 100, 50)
            sage: sum(D.degree()) == 2 * D.size()
            True
            sage: D.allow_multiple_edges(True)
            sage: my_add_edges(D, 200, 50)
            sage: sum(D.degree()) == 2 * D.size()
            True
            sage: G = Graph({1:[2,2,2]})
            sage: G.allow_loops(True)
            sage: G.add_edge(1,1)
            sage: G.add_edge(1,1)
            sage: G.edges(sort=True, labels=False)
            [(1, 1), (1, 1), (1, 2), (1, 2), (1, 2)]
            sage: G.degree(1)
            7
            sage: G.allow_loops(False)
            sage: G.edges(sort=True, labels=False)
            [(1, 2), (1, 2), (1, 2)]
            sage: G.degree(1)
            3
            sage: G = Graph({1:{2:[\'a\',\'a\',\'a\']}})
            sage: G.allow_loops(True)
            sage: G.add_edge(1,1,\'b\')
            sage: G.add_edge(1,1,\'b\')
            sage: G.add_edge(1,1)
            sage: G.add_edge(1,1)
            sage: G.edges_incident()
            [(1, 1, None), (1, 1, None), (1, 1, \'b\'), (1, 1, \'b\'), (1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            11
            sage: G.allow_loops(False)
            sage: G.edges(sort=True)
            [(1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            3
            sage: G = Graph({1:{2:[\'a\',\'a\',\'a\']}})
            sage: G.allow_loops(True)
            sage: G.add_edge(1,1,\'b\')
            sage: G.add_edge(1,1,\'b\')
            sage: G.edges(sort=True)
            [(1, 1, \'b\'), (1, 1, \'b\'), (1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            7
            sage: G.allow_loops(False)
            sage: G.edges(sort=True)
            [(1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            3

        Ensure that :issue:`13664` is fixed ::

            sage: W = WeylGroup(["A",1])                                                # needs sage.combinat sage.groups
            sage: G = W.cayley_graph()                                                  # needs sage.combinat sage.groups
            sage: Graph(G).degree()                                                     # needs sage.combinat sage.groups
            [1, 1]
            sage: h = Graph()
            sage: h.add_edge(1,2,"a")
            sage: h.add_edge(1,2,"a")
            sage: h.degree()
            [1, 1]'''
    @overload
    def degree(self) -> Any:
        '''CGraphBackend.degree(self, v, directed)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 1973)

        Return the degree of the vertex ``v``.

        INPUT:

        - ``v`` -- a vertex of the graph

        - ``directed`` -- boolean; whether to take into account the
          orientation of this graph in counting the degree of ``v``

        OUTPUT: the degree of vertex ``v``

        EXAMPLES::

            sage: from sage.graphs.base.sparse_graph import SparseGraphBackend
            sage: B = SparseGraphBackend(7)
            sage: B.degree(3, False)
            0

        TESTS:

        Ensure that issue :issue:`8395` is fixed. ::

            sage: def my_add_edges(G, m, n):
            ....:     for i in range(m):
            ....:         u = randint(0, n)
            ....:         v = randint(0, n)
            ....:         G.add_edge(u, v)
            sage: G = Graph({1:[1]}); G
            Looped graph on 1 vertex
            sage: G.edges(sort=True, labels=False)
            [(1, 1)]
            sage: G.degree(); G.size()
            [2]
            1
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: G = Graph({1:[1,2], 2:[2,3]}, loops=True); G
            Looped graph on 3 vertices
            sage: my_add_edges(G, 100, 50)
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: G = Graph({1:[2,2], 2:[3]}); G
            Multi-graph on 3 vertices
            sage: G.edges(sort=True, labels=False)
            [(1, 2), (1, 2), (2, 3)]
            sage: G.degree(); G.size()
            [2, 3, 1]
            3
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: G.allow_loops(True); G
            Looped multi-graph on 3 vertices
            sage: my_add_edges(G, 100, 50)
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: D = DiGraph({1:[2], 2:[1,3]}); D
            Digraph on 3 vertices
            sage: D.edges(sort=True, labels=False)
            [(1, 2), (2, 1), (2, 3)]
            sage: D.degree(); D.size()
            [2, 3, 1]
            3
            sage: sum(D.degree()) == 2 * D.size()
            True
            sage: D.allow_loops(True); D
            Looped digraph on 3 vertices
            sage: my_add_edges(D, 100, 50)
            sage: sum(D.degree()) == 2 * D.size()
            True
            sage: D.allow_multiple_edges(True)
            sage: my_add_edges(D, 200, 50)
            sage: sum(D.degree()) == 2 * D.size()
            True
            sage: G = Graph({1:[2,2,2]})
            sage: G.allow_loops(True)
            sage: G.add_edge(1,1)
            sage: G.add_edge(1,1)
            sage: G.edges(sort=True, labels=False)
            [(1, 1), (1, 1), (1, 2), (1, 2), (1, 2)]
            sage: G.degree(1)
            7
            sage: G.allow_loops(False)
            sage: G.edges(sort=True, labels=False)
            [(1, 2), (1, 2), (1, 2)]
            sage: G.degree(1)
            3
            sage: G = Graph({1:{2:[\'a\',\'a\',\'a\']}})
            sage: G.allow_loops(True)
            sage: G.add_edge(1,1,\'b\')
            sage: G.add_edge(1,1,\'b\')
            sage: G.add_edge(1,1)
            sage: G.add_edge(1,1)
            sage: G.edges_incident()
            [(1, 1, None), (1, 1, None), (1, 1, \'b\'), (1, 1, \'b\'), (1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            11
            sage: G.allow_loops(False)
            sage: G.edges(sort=True)
            [(1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            3
            sage: G = Graph({1:{2:[\'a\',\'a\',\'a\']}})
            sage: G.allow_loops(True)
            sage: G.add_edge(1,1,\'b\')
            sage: G.add_edge(1,1,\'b\')
            sage: G.edges(sort=True)
            [(1, 1, \'b\'), (1, 1, \'b\'), (1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            7
            sage: G.allow_loops(False)
            sage: G.edges(sort=True)
            [(1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            3

        Ensure that :issue:`13664` is fixed ::

            sage: W = WeylGroup(["A",1])                                                # needs sage.combinat sage.groups
            sage: G = W.cayley_graph()                                                  # needs sage.combinat sage.groups
            sage: Graph(G).degree()                                                     # needs sage.combinat sage.groups
            [1, 1]
            sage: h = Graph()
            sage: h.add_edge(1,2,"a")
            sage: h.add_edge(1,2,"a")
            sage: h.degree()
            [1, 1]'''
    @overload
    def degree(self) -> Any:
        '''CGraphBackend.degree(self, v, directed)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 1973)

        Return the degree of the vertex ``v``.

        INPUT:

        - ``v`` -- a vertex of the graph

        - ``directed`` -- boolean; whether to take into account the
          orientation of this graph in counting the degree of ``v``

        OUTPUT: the degree of vertex ``v``

        EXAMPLES::

            sage: from sage.graphs.base.sparse_graph import SparseGraphBackend
            sage: B = SparseGraphBackend(7)
            sage: B.degree(3, False)
            0

        TESTS:

        Ensure that issue :issue:`8395` is fixed. ::

            sage: def my_add_edges(G, m, n):
            ....:     for i in range(m):
            ....:         u = randint(0, n)
            ....:         v = randint(0, n)
            ....:         G.add_edge(u, v)
            sage: G = Graph({1:[1]}); G
            Looped graph on 1 vertex
            sage: G.edges(sort=True, labels=False)
            [(1, 1)]
            sage: G.degree(); G.size()
            [2]
            1
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: G = Graph({1:[1,2], 2:[2,3]}, loops=True); G
            Looped graph on 3 vertices
            sage: my_add_edges(G, 100, 50)
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: G = Graph({1:[2,2], 2:[3]}); G
            Multi-graph on 3 vertices
            sage: G.edges(sort=True, labels=False)
            [(1, 2), (1, 2), (2, 3)]
            sage: G.degree(); G.size()
            [2, 3, 1]
            3
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: G.allow_loops(True); G
            Looped multi-graph on 3 vertices
            sage: my_add_edges(G, 100, 50)
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: D = DiGraph({1:[2], 2:[1,3]}); D
            Digraph on 3 vertices
            sage: D.edges(sort=True, labels=False)
            [(1, 2), (2, 1), (2, 3)]
            sage: D.degree(); D.size()
            [2, 3, 1]
            3
            sage: sum(D.degree()) == 2 * D.size()
            True
            sage: D.allow_loops(True); D
            Looped digraph on 3 vertices
            sage: my_add_edges(D, 100, 50)
            sage: sum(D.degree()) == 2 * D.size()
            True
            sage: D.allow_multiple_edges(True)
            sage: my_add_edges(D, 200, 50)
            sage: sum(D.degree()) == 2 * D.size()
            True
            sage: G = Graph({1:[2,2,2]})
            sage: G.allow_loops(True)
            sage: G.add_edge(1,1)
            sage: G.add_edge(1,1)
            sage: G.edges(sort=True, labels=False)
            [(1, 1), (1, 1), (1, 2), (1, 2), (1, 2)]
            sage: G.degree(1)
            7
            sage: G.allow_loops(False)
            sage: G.edges(sort=True, labels=False)
            [(1, 2), (1, 2), (1, 2)]
            sage: G.degree(1)
            3
            sage: G = Graph({1:{2:[\'a\',\'a\',\'a\']}})
            sage: G.allow_loops(True)
            sage: G.add_edge(1,1,\'b\')
            sage: G.add_edge(1,1,\'b\')
            sage: G.add_edge(1,1)
            sage: G.add_edge(1,1)
            sage: G.edges_incident()
            [(1, 1, None), (1, 1, None), (1, 1, \'b\'), (1, 1, \'b\'), (1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            11
            sage: G.allow_loops(False)
            sage: G.edges(sort=True)
            [(1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            3
            sage: G = Graph({1:{2:[\'a\',\'a\',\'a\']}})
            sage: G.allow_loops(True)
            sage: G.add_edge(1,1,\'b\')
            sage: G.add_edge(1,1,\'b\')
            sage: G.edges(sort=True)
            [(1, 1, \'b\'), (1, 1, \'b\'), (1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            7
            sage: G.allow_loops(False)
            sage: G.edges(sort=True)
            [(1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            3

        Ensure that :issue:`13664` is fixed ::

            sage: W = WeylGroup(["A",1])                                                # needs sage.combinat sage.groups
            sage: G = W.cayley_graph()                                                  # needs sage.combinat sage.groups
            sage: Graph(G).degree()                                                     # needs sage.combinat sage.groups
            [1, 1]
            sage: h = Graph()
            sage: h.add_edge(1,2,"a")
            sage: h.add_edge(1,2,"a")
            sage: h.degree()
            [1, 1]'''
    @overload
    def degree(self) -> Any:
        '''CGraphBackend.degree(self, v, directed)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 1973)

        Return the degree of the vertex ``v``.

        INPUT:

        - ``v`` -- a vertex of the graph

        - ``directed`` -- boolean; whether to take into account the
          orientation of this graph in counting the degree of ``v``

        OUTPUT: the degree of vertex ``v``

        EXAMPLES::

            sage: from sage.graphs.base.sparse_graph import SparseGraphBackend
            sage: B = SparseGraphBackend(7)
            sage: B.degree(3, False)
            0

        TESTS:

        Ensure that issue :issue:`8395` is fixed. ::

            sage: def my_add_edges(G, m, n):
            ....:     for i in range(m):
            ....:         u = randint(0, n)
            ....:         v = randint(0, n)
            ....:         G.add_edge(u, v)
            sage: G = Graph({1:[1]}); G
            Looped graph on 1 vertex
            sage: G.edges(sort=True, labels=False)
            [(1, 1)]
            sage: G.degree(); G.size()
            [2]
            1
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: G = Graph({1:[1,2], 2:[2,3]}, loops=True); G
            Looped graph on 3 vertices
            sage: my_add_edges(G, 100, 50)
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: G = Graph({1:[2,2], 2:[3]}); G
            Multi-graph on 3 vertices
            sage: G.edges(sort=True, labels=False)
            [(1, 2), (1, 2), (2, 3)]
            sage: G.degree(); G.size()
            [2, 3, 1]
            3
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: G.allow_loops(True); G
            Looped multi-graph on 3 vertices
            sage: my_add_edges(G, 100, 50)
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: D = DiGraph({1:[2], 2:[1,3]}); D
            Digraph on 3 vertices
            sage: D.edges(sort=True, labels=False)
            [(1, 2), (2, 1), (2, 3)]
            sage: D.degree(); D.size()
            [2, 3, 1]
            3
            sage: sum(D.degree()) == 2 * D.size()
            True
            sage: D.allow_loops(True); D
            Looped digraph on 3 vertices
            sage: my_add_edges(D, 100, 50)
            sage: sum(D.degree()) == 2 * D.size()
            True
            sage: D.allow_multiple_edges(True)
            sage: my_add_edges(D, 200, 50)
            sage: sum(D.degree()) == 2 * D.size()
            True
            sage: G = Graph({1:[2,2,2]})
            sage: G.allow_loops(True)
            sage: G.add_edge(1,1)
            sage: G.add_edge(1,1)
            sage: G.edges(sort=True, labels=False)
            [(1, 1), (1, 1), (1, 2), (1, 2), (1, 2)]
            sage: G.degree(1)
            7
            sage: G.allow_loops(False)
            sage: G.edges(sort=True, labels=False)
            [(1, 2), (1, 2), (1, 2)]
            sage: G.degree(1)
            3
            sage: G = Graph({1:{2:[\'a\',\'a\',\'a\']}})
            sage: G.allow_loops(True)
            sage: G.add_edge(1,1,\'b\')
            sage: G.add_edge(1,1,\'b\')
            sage: G.add_edge(1,1)
            sage: G.add_edge(1,1)
            sage: G.edges_incident()
            [(1, 1, None), (1, 1, None), (1, 1, \'b\'), (1, 1, \'b\'), (1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            11
            sage: G.allow_loops(False)
            sage: G.edges(sort=True)
            [(1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            3
            sage: G = Graph({1:{2:[\'a\',\'a\',\'a\']}})
            sage: G.allow_loops(True)
            sage: G.add_edge(1,1,\'b\')
            sage: G.add_edge(1,1,\'b\')
            sage: G.edges(sort=True)
            [(1, 1, \'b\'), (1, 1, \'b\'), (1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            7
            sage: G.allow_loops(False)
            sage: G.edges(sort=True)
            [(1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            3

        Ensure that :issue:`13664` is fixed ::

            sage: W = WeylGroup(["A",1])                                                # needs sage.combinat sage.groups
            sage: G = W.cayley_graph()                                                  # needs sage.combinat sage.groups
            sage: Graph(G).degree()                                                     # needs sage.combinat sage.groups
            [1, 1]
            sage: h = Graph()
            sage: h.add_edge(1,2,"a")
            sage: h.add_edge(1,2,"a")
            sage: h.degree()
            [1, 1]'''
    @overload
    def degree(self) -> Any:
        '''CGraphBackend.degree(self, v, directed)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 1973)

        Return the degree of the vertex ``v``.

        INPUT:

        - ``v`` -- a vertex of the graph

        - ``directed`` -- boolean; whether to take into account the
          orientation of this graph in counting the degree of ``v``

        OUTPUT: the degree of vertex ``v``

        EXAMPLES::

            sage: from sage.graphs.base.sparse_graph import SparseGraphBackend
            sage: B = SparseGraphBackend(7)
            sage: B.degree(3, False)
            0

        TESTS:

        Ensure that issue :issue:`8395` is fixed. ::

            sage: def my_add_edges(G, m, n):
            ....:     for i in range(m):
            ....:         u = randint(0, n)
            ....:         v = randint(0, n)
            ....:         G.add_edge(u, v)
            sage: G = Graph({1:[1]}); G
            Looped graph on 1 vertex
            sage: G.edges(sort=True, labels=False)
            [(1, 1)]
            sage: G.degree(); G.size()
            [2]
            1
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: G = Graph({1:[1,2], 2:[2,3]}, loops=True); G
            Looped graph on 3 vertices
            sage: my_add_edges(G, 100, 50)
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: G = Graph({1:[2,2], 2:[3]}); G
            Multi-graph on 3 vertices
            sage: G.edges(sort=True, labels=False)
            [(1, 2), (1, 2), (2, 3)]
            sage: G.degree(); G.size()
            [2, 3, 1]
            3
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: G.allow_loops(True); G
            Looped multi-graph on 3 vertices
            sage: my_add_edges(G, 100, 50)
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: D = DiGraph({1:[2], 2:[1,3]}); D
            Digraph on 3 vertices
            sage: D.edges(sort=True, labels=False)
            [(1, 2), (2, 1), (2, 3)]
            sage: D.degree(); D.size()
            [2, 3, 1]
            3
            sage: sum(D.degree()) == 2 * D.size()
            True
            sage: D.allow_loops(True); D
            Looped digraph on 3 vertices
            sage: my_add_edges(D, 100, 50)
            sage: sum(D.degree()) == 2 * D.size()
            True
            sage: D.allow_multiple_edges(True)
            sage: my_add_edges(D, 200, 50)
            sage: sum(D.degree()) == 2 * D.size()
            True
            sage: G = Graph({1:[2,2,2]})
            sage: G.allow_loops(True)
            sage: G.add_edge(1,1)
            sage: G.add_edge(1,1)
            sage: G.edges(sort=True, labels=False)
            [(1, 1), (1, 1), (1, 2), (1, 2), (1, 2)]
            sage: G.degree(1)
            7
            sage: G.allow_loops(False)
            sage: G.edges(sort=True, labels=False)
            [(1, 2), (1, 2), (1, 2)]
            sage: G.degree(1)
            3
            sage: G = Graph({1:{2:[\'a\',\'a\',\'a\']}})
            sage: G.allow_loops(True)
            sage: G.add_edge(1,1,\'b\')
            sage: G.add_edge(1,1,\'b\')
            sage: G.add_edge(1,1)
            sage: G.add_edge(1,1)
            sage: G.edges_incident()
            [(1, 1, None), (1, 1, None), (1, 1, \'b\'), (1, 1, \'b\'), (1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            11
            sage: G.allow_loops(False)
            sage: G.edges(sort=True)
            [(1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            3
            sage: G = Graph({1:{2:[\'a\',\'a\',\'a\']}})
            sage: G.allow_loops(True)
            sage: G.add_edge(1,1,\'b\')
            sage: G.add_edge(1,1,\'b\')
            sage: G.edges(sort=True)
            [(1, 1, \'b\'), (1, 1, \'b\'), (1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            7
            sage: G.allow_loops(False)
            sage: G.edges(sort=True)
            [(1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            3

        Ensure that :issue:`13664` is fixed ::

            sage: W = WeylGroup(["A",1])                                                # needs sage.combinat sage.groups
            sage: G = W.cayley_graph()                                                  # needs sage.combinat sage.groups
            sage: Graph(G).degree()                                                     # needs sage.combinat sage.groups
            [1, 1]
            sage: h = Graph()
            sage: h.add_edge(1,2,"a")
            sage: h.add_edge(1,2,"a")
            sage: h.degree()
            [1, 1]'''
    @overload
    def degree(self) -> Any:
        '''CGraphBackend.degree(self, v, directed)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 1973)

        Return the degree of the vertex ``v``.

        INPUT:

        - ``v`` -- a vertex of the graph

        - ``directed`` -- boolean; whether to take into account the
          orientation of this graph in counting the degree of ``v``

        OUTPUT: the degree of vertex ``v``

        EXAMPLES::

            sage: from sage.graphs.base.sparse_graph import SparseGraphBackend
            sage: B = SparseGraphBackend(7)
            sage: B.degree(3, False)
            0

        TESTS:

        Ensure that issue :issue:`8395` is fixed. ::

            sage: def my_add_edges(G, m, n):
            ....:     for i in range(m):
            ....:         u = randint(0, n)
            ....:         v = randint(0, n)
            ....:         G.add_edge(u, v)
            sage: G = Graph({1:[1]}); G
            Looped graph on 1 vertex
            sage: G.edges(sort=True, labels=False)
            [(1, 1)]
            sage: G.degree(); G.size()
            [2]
            1
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: G = Graph({1:[1,2], 2:[2,3]}, loops=True); G
            Looped graph on 3 vertices
            sage: my_add_edges(G, 100, 50)
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: G = Graph({1:[2,2], 2:[3]}); G
            Multi-graph on 3 vertices
            sage: G.edges(sort=True, labels=False)
            [(1, 2), (1, 2), (2, 3)]
            sage: G.degree(); G.size()
            [2, 3, 1]
            3
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: G.allow_loops(True); G
            Looped multi-graph on 3 vertices
            sage: my_add_edges(G, 100, 50)
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: D = DiGraph({1:[2], 2:[1,3]}); D
            Digraph on 3 vertices
            sage: D.edges(sort=True, labels=False)
            [(1, 2), (2, 1), (2, 3)]
            sage: D.degree(); D.size()
            [2, 3, 1]
            3
            sage: sum(D.degree()) == 2 * D.size()
            True
            sage: D.allow_loops(True); D
            Looped digraph on 3 vertices
            sage: my_add_edges(D, 100, 50)
            sage: sum(D.degree()) == 2 * D.size()
            True
            sage: D.allow_multiple_edges(True)
            sage: my_add_edges(D, 200, 50)
            sage: sum(D.degree()) == 2 * D.size()
            True
            sage: G = Graph({1:[2,2,2]})
            sage: G.allow_loops(True)
            sage: G.add_edge(1,1)
            sage: G.add_edge(1,1)
            sage: G.edges(sort=True, labels=False)
            [(1, 1), (1, 1), (1, 2), (1, 2), (1, 2)]
            sage: G.degree(1)
            7
            sage: G.allow_loops(False)
            sage: G.edges(sort=True, labels=False)
            [(1, 2), (1, 2), (1, 2)]
            sage: G.degree(1)
            3
            sage: G = Graph({1:{2:[\'a\',\'a\',\'a\']}})
            sage: G.allow_loops(True)
            sage: G.add_edge(1,1,\'b\')
            sage: G.add_edge(1,1,\'b\')
            sage: G.add_edge(1,1)
            sage: G.add_edge(1,1)
            sage: G.edges_incident()
            [(1, 1, None), (1, 1, None), (1, 1, \'b\'), (1, 1, \'b\'), (1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            11
            sage: G.allow_loops(False)
            sage: G.edges(sort=True)
            [(1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            3
            sage: G = Graph({1:{2:[\'a\',\'a\',\'a\']}})
            sage: G.allow_loops(True)
            sage: G.add_edge(1,1,\'b\')
            sage: G.add_edge(1,1,\'b\')
            sage: G.edges(sort=True)
            [(1, 1, \'b\'), (1, 1, \'b\'), (1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            7
            sage: G.allow_loops(False)
            sage: G.edges(sort=True)
            [(1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            3

        Ensure that :issue:`13664` is fixed ::

            sage: W = WeylGroup(["A",1])                                                # needs sage.combinat sage.groups
            sage: G = W.cayley_graph()                                                  # needs sage.combinat sage.groups
            sage: Graph(G).degree()                                                     # needs sage.combinat sage.groups
            [1, 1]
            sage: h = Graph()
            sage: h.add_edge(1,2,"a")
            sage: h.add_edge(1,2,"a")
            sage: h.degree()
            [1, 1]'''
    @overload
    def degree(self) -> Any:
        '''CGraphBackend.degree(self, v, directed)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 1973)

        Return the degree of the vertex ``v``.

        INPUT:

        - ``v`` -- a vertex of the graph

        - ``directed`` -- boolean; whether to take into account the
          orientation of this graph in counting the degree of ``v``

        OUTPUT: the degree of vertex ``v``

        EXAMPLES::

            sage: from sage.graphs.base.sparse_graph import SparseGraphBackend
            sage: B = SparseGraphBackend(7)
            sage: B.degree(3, False)
            0

        TESTS:

        Ensure that issue :issue:`8395` is fixed. ::

            sage: def my_add_edges(G, m, n):
            ....:     for i in range(m):
            ....:         u = randint(0, n)
            ....:         v = randint(0, n)
            ....:         G.add_edge(u, v)
            sage: G = Graph({1:[1]}); G
            Looped graph on 1 vertex
            sage: G.edges(sort=True, labels=False)
            [(1, 1)]
            sage: G.degree(); G.size()
            [2]
            1
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: G = Graph({1:[1,2], 2:[2,3]}, loops=True); G
            Looped graph on 3 vertices
            sage: my_add_edges(G, 100, 50)
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: G = Graph({1:[2,2], 2:[3]}); G
            Multi-graph on 3 vertices
            sage: G.edges(sort=True, labels=False)
            [(1, 2), (1, 2), (2, 3)]
            sage: G.degree(); G.size()
            [2, 3, 1]
            3
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: G.allow_loops(True); G
            Looped multi-graph on 3 vertices
            sage: my_add_edges(G, 100, 50)
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: D = DiGraph({1:[2], 2:[1,3]}); D
            Digraph on 3 vertices
            sage: D.edges(sort=True, labels=False)
            [(1, 2), (2, 1), (2, 3)]
            sage: D.degree(); D.size()
            [2, 3, 1]
            3
            sage: sum(D.degree()) == 2 * D.size()
            True
            sage: D.allow_loops(True); D
            Looped digraph on 3 vertices
            sage: my_add_edges(D, 100, 50)
            sage: sum(D.degree()) == 2 * D.size()
            True
            sage: D.allow_multiple_edges(True)
            sage: my_add_edges(D, 200, 50)
            sage: sum(D.degree()) == 2 * D.size()
            True
            sage: G = Graph({1:[2,2,2]})
            sage: G.allow_loops(True)
            sage: G.add_edge(1,1)
            sage: G.add_edge(1,1)
            sage: G.edges(sort=True, labels=False)
            [(1, 1), (1, 1), (1, 2), (1, 2), (1, 2)]
            sage: G.degree(1)
            7
            sage: G.allow_loops(False)
            sage: G.edges(sort=True, labels=False)
            [(1, 2), (1, 2), (1, 2)]
            sage: G.degree(1)
            3
            sage: G = Graph({1:{2:[\'a\',\'a\',\'a\']}})
            sage: G.allow_loops(True)
            sage: G.add_edge(1,1,\'b\')
            sage: G.add_edge(1,1,\'b\')
            sage: G.add_edge(1,1)
            sage: G.add_edge(1,1)
            sage: G.edges_incident()
            [(1, 1, None), (1, 1, None), (1, 1, \'b\'), (1, 1, \'b\'), (1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            11
            sage: G.allow_loops(False)
            sage: G.edges(sort=True)
            [(1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            3
            sage: G = Graph({1:{2:[\'a\',\'a\',\'a\']}})
            sage: G.allow_loops(True)
            sage: G.add_edge(1,1,\'b\')
            sage: G.add_edge(1,1,\'b\')
            sage: G.edges(sort=True)
            [(1, 1, \'b\'), (1, 1, \'b\'), (1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            7
            sage: G.allow_loops(False)
            sage: G.edges(sort=True)
            [(1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            3

        Ensure that :issue:`13664` is fixed ::

            sage: W = WeylGroup(["A",1])                                                # needs sage.combinat sage.groups
            sage: G = W.cayley_graph()                                                  # needs sage.combinat sage.groups
            sage: Graph(G).degree()                                                     # needs sage.combinat sage.groups
            [1, 1]
            sage: h = Graph()
            sage: h.add_edge(1,2,"a")
            sage: h.add_edge(1,2,"a")
            sage: h.degree()
            [1, 1]'''
    @overload
    def degree(self) -> Any:
        '''CGraphBackend.degree(self, v, directed)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 1973)

        Return the degree of the vertex ``v``.

        INPUT:

        - ``v`` -- a vertex of the graph

        - ``directed`` -- boolean; whether to take into account the
          orientation of this graph in counting the degree of ``v``

        OUTPUT: the degree of vertex ``v``

        EXAMPLES::

            sage: from sage.graphs.base.sparse_graph import SparseGraphBackend
            sage: B = SparseGraphBackend(7)
            sage: B.degree(3, False)
            0

        TESTS:

        Ensure that issue :issue:`8395` is fixed. ::

            sage: def my_add_edges(G, m, n):
            ....:     for i in range(m):
            ....:         u = randint(0, n)
            ....:         v = randint(0, n)
            ....:         G.add_edge(u, v)
            sage: G = Graph({1:[1]}); G
            Looped graph on 1 vertex
            sage: G.edges(sort=True, labels=False)
            [(1, 1)]
            sage: G.degree(); G.size()
            [2]
            1
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: G = Graph({1:[1,2], 2:[2,3]}, loops=True); G
            Looped graph on 3 vertices
            sage: my_add_edges(G, 100, 50)
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: G = Graph({1:[2,2], 2:[3]}); G
            Multi-graph on 3 vertices
            sage: G.edges(sort=True, labels=False)
            [(1, 2), (1, 2), (2, 3)]
            sage: G.degree(); G.size()
            [2, 3, 1]
            3
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: G.allow_loops(True); G
            Looped multi-graph on 3 vertices
            sage: my_add_edges(G, 100, 50)
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: D = DiGraph({1:[2], 2:[1,3]}); D
            Digraph on 3 vertices
            sage: D.edges(sort=True, labels=False)
            [(1, 2), (2, 1), (2, 3)]
            sage: D.degree(); D.size()
            [2, 3, 1]
            3
            sage: sum(D.degree()) == 2 * D.size()
            True
            sage: D.allow_loops(True); D
            Looped digraph on 3 vertices
            sage: my_add_edges(D, 100, 50)
            sage: sum(D.degree()) == 2 * D.size()
            True
            sage: D.allow_multiple_edges(True)
            sage: my_add_edges(D, 200, 50)
            sage: sum(D.degree()) == 2 * D.size()
            True
            sage: G = Graph({1:[2,2,2]})
            sage: G.allow_loops(True)
            sage: G.add_edge(1,1)
            sage: G.add_edge(1,1)
            sage: G.edges(sort=True, labels=False)
            [(1, 1), (1, 1), (1, 2), (1, 2), (1, 2)]
            sage: G.degree(1)
            7
            sage: G.allow_loops(False)
            sage: G.edges(sort=True, labels=False)
            [(1, 2), (1, 2), (1, 2)]
            sage: G.degree(1)
            3
            sage: G = Graph({1:{2:[\'a\',\'a\',\'a\']}})
            sage: G.allow_loops(True)
            sage: G.add_edge(1,1,\'b\')
            sage: G.add_edge(1,1,\'b\')
            sage: G.add_edge(1,1)
            sage: G.add_edge(1,1)
            sage: G.edges_incident()
            [(1, 1, None), (1, 1, None), (1, 1, \'b\'), (1, 1, \'b\'), (1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            11
            sage: G.allow_loops(False)
            sage: G.edges(sort=True)
            [(1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            3
            sage: G = Graph({1:{2:[\'a\',\'a\',\'a\']}})
            sage: G.allow_loops(True)
            sage: G.add_edge(1,1,\'b\')
            sage: G.add_edge(1,1,\'b\')
            sage: G.edges(sort=True)
            [(1, 1, \'b\'), (1, 1, \'b\'), (1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            7
            sage: G.allow_loops(False)
            sage: G.edges(sort=True)
            [(1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            3

        Ensure that :issue:`13664` is fixed ::

            sage: W = WeylGroup(["A",1])                                                # needs sage.combinat sage.groups
            sage: G = W.cayley_graph()                                                  # needs sage.combinat sage.groups
            sage: Graph(G).degree()                                                     # needs sage.combinat sage.groups
            [1, 1]
            sage: h = Graph()
            sage: h.add_edge(1,2,"a")
            sage: h.add_edge(1,2,"a")
            sage: h.degree()
            [1, 1]'''
    @overload
    def degree(self) -> Any:
        '''CGraphBackend.degree(self, v, directed)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 1973)

        Return the degree of the vertex ``v``.

        INPUT:

        - ``v`` -- a vertex of the graph

        - ``directed`` -- boolean; whether to take into account the
          orientation of this graph in counting the degree of ``v``

        OUTPUT: the degree of vertex ``v``

        EXAMPLES::

            sage: from sage.graphs.base.sparse_graph import SparseGraphBackend
            sage: B = SparseGraphBackend(7)
            sage: B.degree(3, False)
            0

        TESTS:

        Ensure that issue :issue:`8395` is fixed. ::

            sage: def my_add_edges(G, m, n):
            ....:     for i in range(m):
            ....:         u = randint(0, n)
            ....:         v = randint(0, n)
            ....:         G.add_edge(u, v)
            sage: G = Graph({1:[1]}); G
            Looped graph on 1 vertex
            sage: G.edges(sort=True, labels=False)
            [(1, 1)]
            sage: G.degree(); G.size()
            [2]
            1
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: G = Graph({1:[1,2], 2:[2,3]}, loops=True); G
            Looped graph on 3 vertices
            sage: my_add_edges(G, 100, 50)
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: G = Graph({1:[2,2], 2:[3]}); G
            Multi-graph on 3 vertices
            sage: G.edges(sort=True, labels=False)
            [(1, 2), (1, 2), (2, 3)]
            sage: G.degree(); G.size()
            [2, 3, 1]
            3
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: G.allow_loops(True); G
            Looped multi-graph on 3 vertices
            sage: my_add_edges(G, 100, 50)
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: D = DiGraph({1:[2], 2:[1,3]}); D
            Digraph on 3 vertices
            sage: D.edges(sort=True, labels=False)
            [(1, 2), (2, 1), (2, 3)]
            sage: D.degree(); D.size()
            [2, 3, 1]
            3
            sage: sum(D.degree()) == 2 * D.size()
            True
            sage: D.allow_loops(True); D
            Looped digraph on 3 vertices
            sage: my_add_edges(D, 100, 50)
            sage: sum(D.degree()) == 2 * D.size()
            True
            sage: D.allow_multiple_edges(True)
            sage: my_add_edges(D, 200, 50)
            sage: sum(D.degree()) == 2 * D.size()
            True
            sage: G = Graph({1:[2,2,2]})
            sage: G.allow_loops(True)
            sage: G.add_edge(1,1)
            sage: G.add_edge(1,1)
            sage: G.edges(sort=True, labels=False)
            [(1, 1), (1, 1), (1, 2), (1, 2), (1, 2)]
            sage: G.degree(1)
            7
            sage: G.allow_loops(False)
            sage: G.edges(sort=True, labels=False)
            [(1, 2), (1, 2), (1, 2)]
            sage: G.degree(1)
            3
            sage: G = Graph({1:{2:[\'a\',\'a\',\'a\']}})
            sage: G.allow_loops(True)
            sage: G.add_edge(1,1,\'b\')
            sage: G.add_edge(1,1,\'b\')
            sage: G.add_edge(1,1)
            sage: G.add_edge(1,1)
            sage: G.edges_incident()
            [(1, 1, None), (1, 1, None), (1, 1, \'b\'), (1, 1, \'b\'), (1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            11
            sage: G.allow_loops(False)
            sage: G.edges(sort=True)
            [(1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            3
            sage: G = Graph({1:{2:[\'a\',\'a\',\'a\']}})
            sage: G.allow_loops(True)
            sage: G.add_edge(1,1,\'b\')
            sage: G.add_edge(1,1,\'b\')
            sage: G.edges(sort=True)
            [(1, 1, \'b\'), (1, 1, \'b\'), (1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            7
            sage: G.allow_loops(False)
            sage: G.edges(sort=True)
            [(1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            3

        Ensure that :issue:`13664` is fixed ::

            sage: W = WeylGroup(["A",1])                                                # needs sage.combinat sage.groups
            sage: G = W.cayley_graph()                                                  # needs sage.combinat sage.groups
            sage: Graph(G).degree()                                                     # needs sage.combinat sage.groups
            [1, 1]
            sage: h = Graph()
            sage: h.add_edge(1,2,"a")
            sage: h.add_edge(1,2,"a")
            sage: h.degree()
            [1, 1]'''
    @overload
    def degree(self) -> Any:
        '''CGraphBackend.degree(self, v, directed)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 1973)

        Return the degree of the vertex ``v``.

        INPUT:

        - ``v`` -- a vertex of the graph

        - ``directed`` -- boolean; whether to take into account the
          orientation of this graph in counting the degree of ``v``

        OUTPUT: the degree of vertex ``v``

        EXAMPLES::

            sage: from sage.graphs.base.sparse_graph import SparseGraphBackend
            sage: B = SparseGraphBackend(7)
            sage: B.degree(3, False)
            0

        TESTS:

        Ensure that issue :issue:`8395` is fixed. ::

            sage: def my_add_edges(G, m, n):
            ....:     for i in range(m):
            ....:         u = randint(0, n)
            ....:         v = randint(0, n)
            ....:         G.add_edge(u, v)
            sage: G = Graph({1:[1]}); G
            Looped graph on 1 vertex
            sage: G.edges(sort=True, labels=False)
            [(1, 1)]
            sage: G.degree(); G.size()
            [2]
            1
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: G = Graph({1:[1,2], 2:[2,3]}, loops=True); G
            Looped graph on 3 vertices
            sage: my_add_edges(G, 100, 50)
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: G = Graph({1:[2,2], 2:[3]}); G
            Multi-graph on 3 vertices
            sage: G.edges(sort=True, labels=False)
            [(1, 2), (1, 2), (2, 3)]
            sage: G.degree(); G.size()
            [2, 3, 1]
            3
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: G.allow_loops(True); G
            Looped multi-graph on 3 vertices
            sage: my_add_edges(G, 100, 50)
            sage: sum(G.degree()) == 2 * G.size()
            True
            sage: D = DiGraph({1:[2], 2:[1,3]}); D
            Digraph on 3 vertices
            sage: D.edges(sort=True, labels=False)
            [(1, 2), (2, 1), (2, 3)]
            sage: D.degree(); D.size()
            [2, 3, 1]
            3
            sage: sum(D.degree()) == 2 * D.size()
            True
            sage: D.allow_loops(True); D
            Looped digraph on 3 vertices
            sage: my_add_edges(D, 100, 50)
            sage: sum(D.degree()) == 2 * D.size()
            True
            sage: D.allow_multiple_edges(True)
            sage: my_add_edges(D, 200, 50)
            sage: sum(D.degree()) == 2 * D.size()
            True
            sage: G = Graph({1:[2,2,2]})
            sage: G.allow_loops(True)
            sage: G.add_edge(1,1)
            sage: G.add_edge(1,1)
            sage: G.edges(sort=True, labels=False)
            [(1, 1), (1, 1), (1, 2), (1, 2), (1, 2)]
            sage: G.degree(1)
            7
            sage: G.allow_loops(False)
            sage: G.edges(sort=True, labels=False)
            [(1, 2), (1, 2), (1, 2)]
            sage: G.degree(1)
            3
            sage: G = Graph({1:{2:[\'a\',\'a\',\'a\']}})
            sage: G.allow_loops(True)
            sage: G.add_edge(1,1,\'b\')
            sage: G.add_edge(1,1,\'b\')
            sage: G.add_edge(1,1)
            sage: G.add_edge(1,1)
            sage: G.edges_incident()
            [(1, 1, None), (1, 1, None), (1, 1, \'b\'), (1, 1, \'b\'), (1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            11
            sage: G.allow_loops(False)
            sage: G.edges(sort=True)
            [(1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            3
            sage: G = Graph({1:{2:[\'a\',\'a\',\'a\']}})
            sage: G.allow_loops(True)
            sage: G.add_edge(1,1,\'b\')
            sage: G.add_edge(1,1,\'b\')
            sage: G.edges(sort=True)
            [(1, 1, \'b\'), (1, 1, \'b\'), (1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            7
            sage: G.allow_loops(False)
            sage: G.edges(sort=True)
            [(1, 2, \'a\'), (1, 2, \'a\'), (1, 2, \'a\')]
            sage: G.degree(1)
            3

        Ensure that :issue:`13664` is fixed ::

            sage: W = WeylGroup(["A",1])                                                # needs sage.combinat sage.groups
            sage: G = W.cayley_graph()                                                  # needs sage.combinat sage.groups
            sage: Graph(G).degree()                                                     # needs sage.combinat sage.groups
            [1, 1]
            sage: h = Graph()
            sage: h.add_edge(1,2,"a")
            sage: h.add_edge(1,2,"a")
            sage: h.degree()
            [1, 1]'''
    def del_edge(self, u, v, l, booldirected) -> Any:
        """CGraphBackend.del_edge(self, u, v, l, bool directed)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 2465)

        Delete edge ``(u, v, l)``.

        INPUT:

        - ``u``, ``v`` -- the vertices of the edge

        - ``l`` -- the edge label

        - ``directed`` -- if ``False``, also delete ``(v, u, l)``

        .. NOTE::

            The input ``l`` is ignored if the backend
            does not support labels.

        EXAMPLES::

            sage: D = sage.graphs.base.sparse_graph.SparseGraphBackend(9)
            sage: D.add_edges([(0,1), (2,3), (4,5), (5,6)], False)
            sage: list(D.iterator_edges(range(9), True))
            [(0, 1, None),
             (2, 3, None),
             (4, 5, None),
             (5, 6, None)]
            sage: D.del_edge(0,1,None,True)
            sage: list(D.iterator_out_edges(range(9), True))
            [(1, 0, None),
             (2, 3, None),
             (3, 2, None),
             (4, 5, None),
             (5, 4, None),
             (5, 6, None),
             (6, 5, None)]

        ::

            sage: D = sage.graphs.base.dense_graph.DenseGraphBackend(9)
            sage: D.add_edges([(0, 1), (2, 3), (4, 5), (5, 6)], False)
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

        TESTS::

            sage: G = Graph(sparse=True)
            sage: G.add_edge(0,1,2)
            sage: G.delete_edge(0,1)
            sage: G.edges(sort=True)
            []

            sage: G = Graph(multiedges=True, sparse=True)
            sage: G.add_edge(0,1,2)
            sage: G.add_edge(0,1,None)
            sage: G.delete_edge(0,1)
            sage: G.edges(sort=True)
            [(0, 1, 2)]

        Do we remove loops correctly? (:issue:`12135`)::

            sage: g=Graph({0:[0,0,0]}, sparse=True)
            sage: g.edges(sort=True, labels=False)
            [(0, 0), (0, 0), (0, 0)]
            sage: g.delete_edge(0,0); g.edges(sort=True, labels=False)
            [(0, 0), (0, 0)]"""
    def del_edges(self, edges, booldirected) -> Any:
        """CGraphBackend.del_edges(self, edges, bool directed)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 2437)

        Delete edges from a list.

        INPUT:

        - ``edges`` -- the edges to be added; can either be of the form
          ``(u,v)`` or ``(u,v,l)``

        - ``directed`` -- if ``False``, remove``(v,u)`` as well as ``(u,v)``

        EXAMPLES::

            sage: D = sage.graphs.base.sparse_graph.SparseGraphBackend(9)
            sage: D.add_edges([(0,1), (2,3), (4,5), (5,6)], False)
            sage: D.del_edges([(0,1), (2,3), (4,5), (5,6)], False)
            sage: list(D.iterator_edges(range(9), True))
            []"""
    def del_vertex(self, v) -> Any:
        """CGraphBackend.del_vertex(self, v)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 1789)

        Delete a vertex in ``self``, failing silently if the vertex is not
        in the graph.

        INPUT:

        - ``v`` -- vertex to be deleted

        .. SEEALSO::

            - :meth:`del_vertices` -- delete a bunch of vertices from this graph

        EXAMPLES::

            sage: D = sage.graphs.base.dense_graph.DenseGraphBackend(9)
            sage: D.del_vertex(0)
            sage: D.has_vertex(0)
            False

        ::

            sage: S = sage.graphs.base.sparse_graph.SparseGraphBackend(9)
            sage: S.del_vertex(0)
            sage: S.has_vertex(0)
            False"""
    def del_vertices(self, vertices) -> Any:
        """CGraphBackend.del_vertices(self, vertices)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 1828)

        Delete vertices from an iterable container.

        INPUT:

        - ``vertices`` -- iterator of vertex labels

        OUTPUT: same as for :meth:`del_vertex`

        .. SEEALSO::

            - :meth:`del_vertex` -- delete a vertex of this graph

        EXAMPLES::

            sage: import sage.graphs.base.dense_graph
            sage: D = sage.graphs.base.dense_graph.DenseGraphBackend(9)
            sage: D.del_vertices([7, 8])
            sage: D.has_vertex(7)
            False
            sage: D.has_vertex(6)
            True

        ::

            sage: D = sage.graphs.base.sparse_graph.SparseGraphBackend(9)
            sage: D.del_vertices([1, 2, 3])
            sage: D.has_vertex(1)
            False
            sage: D.has_vertex(0)
            True"""
    def depth_first_search(self, v, reverse=..., ignore_direction=..., forbidden_vertices=...) -> Any:
        '''CGraphBackend.depth_first_search(self, v, reverse=False, ignore_direction=False, forbidden_vertices=None)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 4310)

        Return a depth-first search from vertex ``v``.

        INPUT:

        - ``v`` -- a vertex from which to start the depth-first search

        - ``reverse`` -- boolean (default: ``False``); this is only relevant to
          digraphs. If this is a digraph, consider the reversed graph in which
          the out-neighbors become the in-neighbors and vice versa.

        - ``ignore_direction`` -- boolean (default: ``False``); this is only
          relevant to digraphs. If this is a digraph, ignore all orientations
          and consider the graph as undirected.

        - ``forbidden_vertices`` -- list (default: ``None``); set of vertices to
          avoid during the search. The start vertex ``v`` cannot be in this set.

        ALGORITHM:

        Below is a general template for depth-first search.

        - **Input:** A directed or undirected graph `G = (V, E)` of order
          `n > 0`. A vertex `s` from which to start the search. The vertices
          are numbered from 1 to `n = |V|`, i.e. `V = \\{1, 2, \\dots, n\\}`.

        - **Output:** A list `D` of distances of all vertices from `s`. A tree
          `T` rooted at `s`.

        #. `S \\leftarrow [s]`  # a stack of nodes to visit
        #. `D \\leftarrow [\\infty, \\infty, \\dots, \\infty]`  # `n` copies of `\\infty`
        #. `D[s] \\leftarrow 0`
        #. `T \\leftarrow [\\,]`
        #. while `\\text{length}(S) > 0` do

           #. `v \\leftarrow \\text{pop}(S)`
           #. for each `w \\in \\text{adj}(v)` do  # for digraphs, use out-neighbor set `\\text{oadj}(v)`

              #. if `D[w] = \\infty` then

                 #. `D[w] \\leftarrow D[v] + 1`
                 #. `\\text{push}(S, w)`
                 #. `\\text{append}(T, vw)`
        #. return `(D, T)`

        .. SEEALSO::

            - :meth:`breadth_first_search`
              -- breadth-first search for fast compiled graphs.

            - :meth:`breadth_first_search <sage.graphs.generic_graph.GenericGraph.breadth_first_search>`
              -- breadth-first search for generic graphs.

            - :meth:`depth_first_search <sage.graphs.generic_graph.GenericGraph.depth_first_search>`
              -- depth-first search for generic graphs.

        EXAMPLES:

        Traversing the Petersen graph using depth-first search::

            sage: G = graphs.PetersenGraph()
            sage: list(G.depth_first_search(0))
            [0, 5, 8, 6, 9, 7, 2, 3, 4, 1]

        Visiting German cities using depth-first search::

            sage: G = Graph({"Mannheim": ["Frankfurt","Karlsruhe"],
            ....: "Frankfurt": ["Mannheim","Wurzburg","Kassel"],
            ....: "Kassel": ["Frankfurt","Munchen"],
            ....: "Munchen": ["Kassel","Nurnberg","Augsburg"],
            ....: "Augsburg": ["Munchen","Karlsruhe"],
            ....: "Karlsruhe": ["Mannheim","Augsburg"],
            ....: "Wurzburg": ["Frankfurt","Erfurt","Nurnberg"],
            ....: "Nurnberg": ["Wurzburg","Stuttgart","Munchen"],
            ....: "Stuttgart": ["Nurnberg"], "Erfurt": ["Wurzburg"]})
            sage: list(G.depth_first_search("Stuttgart"))
            [\'Stuttgart\', \'Nurnberg\', ...]

        Avoiding some cities:

            sage: list(G.depth_first_search("Stuttgart",
            ....:                 forbidden_vertices=["Frankfurt", "Munchen"]))
            [\'Stuttgart\', \'Nurnberg\', \'Wurzburg\', \'Erfurt\']

        TESTS:

        The start vertex cannot be forbidden::

            sage: G = graphs.PetersenGraph()
            sage: list(G.depth_first_search(0, forbidden_vertices=[0, 1]))
            Traceback (most recent call last):
            ...
            ValueError: the start vertex is in the set of forbidden vertices'''
    def has_vertex(self, v) -> Any:
        """CGraphBackend.has_vertex(self, v)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 1660)

        Check whether ``v`` is a vertex of ``self``.

        INPUT:

        - ``v`` -- any object

        OUTPUT: ``True`` if ``v`` is a vertex of this graph; ``False`` otherwise

        EXAMPLES::

            sage: from sage.graphs.base.sparse_graph import SparseGraphBackend
            sage: B = SparseGraphBackend(7)
            sage: B.has_vertex(6)
            True
            sage: B.has_vertex(7)
            False"""
    def in_degree(self, v) -> Any:
        """CGraphBackend.in_degree(self, v)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 2140)

        Return the in-degree of ``v``.

        INPUT:

        - ``v`` -- a vertex of the graph

        EXAMPLES::


            sage: D = DiGraph( { 0: [1,2,3], 1: [0,2], 2: [3], 3: [4], 4: [0,5], 5: [1] } )
            sage: D.out_degree(1)
            2"""
    def is_connected(self, forbidden_vertices=...) -> Any:
        """CGraphBackend.is_connected(self, forbidden_vertices=None)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 4527)

        Check whether the graph is connected.

        INPUT:

        - ``forbidden_vertices`` -- list (default: ``None``); set of vertices to
          avoid during the search

        EXAMPLES:

        Petersen's graph is connected::

           sage: DiGraph(graphs.PetersenGraph()).is_connected()
           True

        While the disjoint union of two of them is not::

           sage: DiGraph(2*graphs.PetersenGraph()).is_connected()
           False

        A graph with non-integer vertex labels::

            sage: Graph(graphs.CubeGraph(3)).is_connected()
            True

        A graph with forbidden vertices::

            sage: G = graphs.PathGraph(5)
            sage: G._backend.is_connected()
            True
            sage: G._backend.is_connected(forbidden_vertices=[1])
            False
            sage: G._backend.is_connected(forbidden_vertices=[0, 1])
            True

        TESTS::

            sage: P = posets.PentagonPoset()                                            # needs sage.modules
            sage: H = P._hasse_diagram                                                  # needs sage.modules
            sage: H._backend.is_connected()                                             # needs sage.modules
            True"""
    @overload
    def is_directed_acyclic(self, certificate=...) -> Any:
        """CGraphBackend.is_directed_acyclic(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 4667)

        Check whether the graph is both directed and acyclic (possibly with a
        certificate)

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); whether to return a
          certificate

        OUTPUT:

        When ``certificate=False``, returns a boolean value. When
        ``certificate=True`` :

        * If the graph is acyclic, returns a pair ``(True, ordering)`` where
          ``ordering`` is a list of the vertices such that ``u`` appears before
          ``v`` in ``ordering`` if ``u, v`` is an edge.

        * Else, returns a pair ``(False, cycle)`` where ``cycle`` is a list of
          vertices representing a circuit in the graph.

        ALGORITHM:

        We pick a vertex at random, think hard and find out that if we are
        to remove the vertex from the graph we must remove all of its
        out-neighbors in the first place. So we put all of its out-neighbours in
        a stack, and repeat the same procedure with the vertex on top of the
        stack (when a vertex on top of the stack has no out-neighbors, we remove
        it immediately). Of course, for each vertex we only add its outneighbors
        to the end of the stack once : if for some reason the previous algorithm
        leads us to do it twice, it means we have found a circuit.

        We keep track of the vertices whose out-neighborhood has been added to
        the stack once with a variable named ``tried``.

        There is no reason why the graph should be empty at the end of this
        procedure, so we run it again on the remaining vertices until none are
        left or a circuit is found.

        .. NOTE::

            The graph is assumed to be directed. An exception is raised if it is
            not.

        EXAMPLES:

        At first, the following graph is acyclic::

            sage: D = DiGraph({ 0:[1,2,3], 4:[2,5], 1:[8], 2:[7], 3:[7], 5:[6,7], 7:[8], 6:[9], 8:[10], 9:[10] })
            sage: D.plot(layout='circular').show()                                      # needs sage.plot
            sage: D.is_directed_acyclic()
            True

        Adding an edge from `9` to `7` does not change it::

            sage: D.add_edge(9,7)
            sage: D.is_directed_acyclic()
            True

        We can obtain as a proof an ordering of the vertices such that `u`
        appears before `v` if `uv` is an edge of the graph::

            sage: D.is_directed_acyclic(certificate = True)
            (True, [4, 5, 6, 9, 0, 1, 2, 3, 7, 8, 10])

        Adding an edge from 7 to 4, though, makes a difference::

            sage: D.add_edge(7,4)
            sage: D.is_directed_acyclic()
            False

        Indeed, it creates a circuit `7, 4, 5`::

            sage: D.is_directed_acyclic(certificate = True)
            (False, [7, 4, 5])

        Checking acyclic graphs are indeed acyclic ::

            sage: def random_acyclic(n, p):
            ....:  g = graphs.RandomGNP(n, p)
            ....:  h = DiGraph()
            ....:  h.add_edges([ ((u,v) if u<v else (v,u)) for u,v,_ in g.edges(sort=True) ])
            ....:  return h
            ...
            sage: all( random_acyclic(100, .2).is_directed_acyclic()    # long time
            ....:      for i in range(50))
            True

        TESTS::

            sage: m = Matrix(3,[0, 1, 1, 0, 0, 0, 0, 1, 0])                             # needs sage.modules
            sage: g = DiGraph(m)                                                        # needs sage.modules
            sage: g.is_directed_acyclic(certificate=True)                               # needs sage.modules
            (True, [0, 2, 1])"""
    @overload
    def is_directed_acyclic(self) -> Any:
        """CGraphBackend.is_directed_acyclic(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 4667)

        Check whether the graph is both directed and acyclic (possibly with a
        certificate)

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); whether to return a
          certificate

        OUTPUT:

        When ``certificate=False``, returns a boolean value. When
        ``certificate=True`` :

        * If the graph is acyclic, returns a pair ``(True, ordering)`` where
          ``ordering`` is a list of the vertices such that ``u`` appears before
          ``v`` in ``ordering`` if ``u, v`` is an edge.

        * Else, returns a pair ``(False, cycle)`` where ``cycle`` is a list of
          vertices representing a circuit in the graph.

        ALGORITHM:

        We pick a vertex at random, think hard and find out that if we are
        to remove the vertex from the graph we must remove all of its
        out-neighbors in the first place. So we put all of its out-neighbours in
        a stack, and repeat the same procedure with the vertex on top of the
        stack (when a vertex on top of the stack has no out-neighbors, we remove
        it immediately). Of course, for each vertex we only add its outneighbors
        to the end of the stack once : if for some reason the previous algorithm
        leads us to do it twice, it means we have found a circuit.

        We keep track of the vertices whose out-neighborhood has been added to
        the stack once with a variable named ``tried``.

        There is no reason why the graph should be empty at the end of this
        procedure, so we run it again on the remaining vertices until none are
        left or a circuit is found.

        .. NOTE::

            The graph is assumed to be directed. An exception is raised if it is
            not.

        EXAMPLES:

        At first, the following graph is acyclic::

            sage: D = DiGraph({ 0:[1,2,3], 4:[2,5], 1:[8], 2:[7], 3:[7], 5:[6,7], 7:[8], 6:[9], 8:[10], 9:[10] })
            sage: D.plot(layout='circular').show()                                      # needs sage.plot
            sage: D.is_directed_acyclic()
            True

        Adding an edge from `9` to `7` does not change it::

            sage: D.add_edge(9,7)
            sage: D.is_directed_acyclic()
            True

        We can obtain as a proof an ordering of the vertices such that `u`
        appears before `v` if `uv` is an edge of the graph::

            sage: D.is_directed_acyclic(certificate = True)
            (True, [4, 5, 6, 9, 0, 1, 2, 3, 7, 8, 10])

        Adding an edge from 7 to 4, though, makes a difference::

            sage: D.add_edge(7,4)
            sage: D.is_directed_acyclic()
            False

        Indeed, it creates a circuit `7, 4, 5`::

            sage: D.is_directed_acyclic(certificate = True)
            (False, [7, 4, 5])

        Checking acyclic graphs are indeed acyclic ::

            sage: def random_acyclic(n, p):
            ....:  g = graphs.RandomGNP(n, p)
            ....:  h = DiGraph()
            ....:  h.add_edges([ ((u,v) if u<v else (v,u)) for u,v,_ in g.edges(sort=True) ])
            ....:  return h
            ...
            sage: all( random_acyclic(100, .2).is_directed_acyclic()    # long time
            ....:      for i in range(50))
            True

        TESTS::

            sage: m = Matrix(3,[0, 1, 1, 0, 0, 0, 0, 1, 0])                             # needs sage.modules
            sage: g = DiGraph(m)                                                        # needs sage.modules
            sage: g.is_directed_acyclic(certificate=True)                               # needs sage.modules
            (True, [0, 2, 1])"""
    @overload
    def is_directed_acyclic(self) -> Any:
        """CGraphBackend.is_directed_acyclic(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 4667)

        Check whether the graph is both directed and acyclic (possibly with a
        certificate)

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); whether to return a
          certificate

        OUTPUT:

        When ``certificate=False``, returns a boolean value. When
        ``certificate=True`` :

        * If the graph is acyclic, returns a pair ``(True, ordering)`` where
          ``ordering`` is a list of the vertices such that ``u`` appears before
          ``v`` in ``ordering`` if ``u, v`` is an edge.

        * Else, returns a pair ``(False, cycle)`` where ``cycle`` is a list of
          vertices representing a circuit in the graph.

        ALGORITHM:

        We pick a vertex at random, think hard and find out that if we are
        to remove the vertex from the graph we must remove all of its
        out-neighbors in the first place. So we put all of its out-neighbours in
        a stack, and repeat the same procedure with the vertex on top of the
        stack (when a vertex on top of the stack has no out-neighbors, we remove
        it immediately). Of course, for each vertex we only add its outneighbors
        to the end of the stack once : if for some reason the previous algorithm
        leads us to do it twice, it means we have found a circuit.

        We keep track of the vertices whose out-neighborhood has been added to
        the stack once with a variable named ``tried``.

        There is no reason why the graph should be empty at the end of this
        procedure, so we run it again on the remaining vertices until none are
        left or a circuit is found.

        .. NOTE::

            The graph is assumed to be directed. An exception is raised if it is
            not.

        EXAMPLES:

        At first, the following graph is acyclic::

            sage: D = DiGraph({ 0:[1,2,3], 4:[2,5], 1:[8], 2:[7], 3:[7], 5:[6,7], 7:[8], 6:[9], 8:[10], 9:[10] })
            sage: D.plot(layout='circular').show()                                      # needs sage.plot
            sage: D.is_directed_acyclic()
            True

        Adding an edge from `9` to `7` does not change it::

            sage: D.add_edge(9,7)
            sage: D.is_directed_acyclic()
            True

        We can obtain as a proof an ordering of the vertices such that `u`
        appears before `v` if `uv` is an edge of the graph::

            sage: D.is_directed_acyclic(certificate = True)
            (True, [4, 5, 6, 9, 0, 1, 2, 3, 7, 8, 10])

        Adding an edge from 7 to 4, though, makes a difference::

            sage: D.add_edge(7,4)
            sage: D.is_directed_acyclic()
            False

        Indeed, it creates a circuit `7, 4, 5`::

            sage: D.is_directed_acyclic(certificate = True)
            (False, [7, 4, 5])

        Checking acyclic graphs are indeed acyclic ::

            sage: def random_acyclic(n, p):
            ....:  g = graphs.RandomGNP(n, p)
            ....:  h = DiGraph()
            ....:  h.add_edges([ ((u,v) if u<v else (v,u)) for u,v,_ in g.edges(sort=True) ])
            ....:  return h
            ...
            sage: all( random_acyclic(100, .2).is_directed_acyclic()    # long time
            ....:      for i in range(50))
            True

        TESTS::

            sage: m = Matrix(3,[0, 1, 1, 0, 0, 0, 0, 1, 0])                             # needs sage.modules
            sage: g = DiGraph(m)                                                        # needs sage.modules
            sage: g.is_directed_acyclic(certificate=True)                               # needs sage.modules
            (True, [0, 2, 1])"""
    @overload
    def is_directed_acyclic(self, certificate=...) -> Any:
        """CGraphBackend.is_directed_acyclic(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 4667)

        Check whether the graph is both directed and acyclic (possibly with a
        certificate)

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); whether to return a
          certificate

        OUTPUT:

        When ``certificate=False``, returns a boolean value. When
        ``certificate=True`` :

        * If the graph is acyclic, returns a pair ``(True, ordering)`` where
          ``ordering`` is a list of the vertices such that ``u`` appears before
          ``v`` in ``ordering`` if ``u, v`` is an edge.

        * Else, returns a pair ``(False, cycle)`` where ``cycle`` is a list of
          vertices representing a circuit in the graph.

        ALGORITHM:

        We pick a vertex at random, think hard and find out that if we are
        to remove the vertex from the graph we must remove all of its
        out-neighbors in the first place. So we put all of its out-neighbours in
        a stack, and repeat the same procedure with the vertex on top of the
        stack (when a vertex on top of the stack has no out-neighbors, we remove
        it immediately). Of course, for each vertex we only add its outneighbors
        to the end of the stack once : if for some reason the previous algorithm
        leads us to do it twice, it means we have found a circuit.

        We keep track of the vertices whose out-neighborhood has been added to
        the stack once with a variable named ``tried``.

        There is no reason why the graph should be empty at the end of this
        procedure, so we run it again on the remaining vertices until none are
        left or a circuit is found.

        .. NOTE::

            The graph is assumed to be directed. An exception is raised if it is
            not.

        EXAMPLES:

        At first, the following graph is acyclic::

            sage: D = DiGraph({ 0:[1,2,3], 4:[2,5], 1:[8], 2:[7], 3:[7], 5:[6,7], 7:[8], 6:[9], 8:[10], 9:[10] })
            sage: D.plot(layout='circular').show()                                      # needs sage.plot
            sage: D.is_directed_acyclic()
            True

        Adding an edge from `9` to `7` does not change it::

            sage: D.add_edge(9,7)
            sage: D.is_directed_acyclic()
            True

        We can obtain as a proof an ordering of the vertices such that `u`
        appears before `v` if `uv` is an edge of the graph::

            sage: D.is_directed_acyclic(certificate = True)
            (True, [4, 5, 6, 9, 0, 1, 2, 3, 7, 8, 10])

        Adding an edge from 7 to 4, though, makes a difference::

            sage: D.add_edge(7,4)
            sage: D.is_directed_acyclic()
            False

        Indeed, it creates a circuit `7, 4, 5`::

            sage: D.is_directed_acyclic(certificate = True)
            (False, [7, 4, 5])

        Checking acyclic graphs are indeed acyclic ::

            sage: def random_acyclic(n, p):
            ....:  g = graphs.RandomGNP(n, p)
            ....:  h = DiGraph()
            ....:  h.add_edges([ ((u,v) if u<v else (v,u)) for u,v,_ in g.edges(sort=True) ])
            ....:  return h
            ...
            sage: all( random_acyclic(100, .2).is_directed_acyclic()    # long time
            ....:      for i in range(50))
            True

        TESTS::

            sage: m = Matrix(3,[0, 1, 1, 0, 0, 0, 0, 1, 0])                             # needs sage.modules
            sage: g = DiGraph(m)                                                        # needs sage.modules
            sage: g.is_directed_acyclic(certificate=True)                               # needs sage.modules
            (True, [0, 2, 1])"""
    @overload
    def is_directed_acyclic(self) -> Any:
        """CGraphBackend.is_directed_acyclic(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 4667)

        Check whether the graph is both directed and acyclic (possibly with a
        certificate)

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); whether to return a
          certificate

        OUTPUT:

        When ``certificate=False``, returns a boolean value. When
        ``certificate=True`` :

        * If the graph is acyclic, returns a pair ``(True, ordering)`` where
          ``ordering`` is a list of the vertices such that ``u`` appears before
          ``v`` in ``ordering`` if ``u, v`` is an edge.

        * Else, returns a pair ``(False, cycle)`` where ``cycle`` is a list of
          vertices representing a circuit in the graph.

        ALGORITHM:

        We pick a vertex at random, think hard and find out that if we are
        to remove the vertex from the graph we must remove all of its
        out-neighbors in the first place. So we put all of its out-neighbours in
        a stack, and repeat the same procedure with the vertex on top of the
        stack (when a vertex on top of the stack has no out-neighbors, we remove
        it immediately). Of course, for each vertex we only add its outneighbors
        to the end of the stack once : if for some reason the previous algorithm
        leads us to do it twice, it means we have found a circuit.

        We keep track of the vertices whose out-neighborhood has been added to
        the stack once with a variable named ``tried``.

        There is no reason why the graph should be empty at the end of this
        procedure, so we run it again on the remaining vertices until none are
        left or a circuit is found.

        .. NOTE::

            The graph is assumed to be directed. An exception is raised if it is
            not.

        EXAMPLES:

        At first, the following graph is acyclic::

            sage: D = DiGraph({ 0:[1,2,3], 4:[2,5], 1:[8], 2:[7], 3:[7], 5:[6,7], 7:[8], 6:[9], 8:[10], 9:[10] })
            sage: D.plot(layout='circular').show()                                      # needs sage.plot
            sage: D.is_directed_acyclic()
            True

        Adding an edge from `9` to `7` does not change it::

            sage: D.add_edge(9,7)
            sage: D.is_directed_acyclic()
            True

        We can obtain as a proof an ordering of the vertices such that `u`
        appears before `v` if `uv` is an edge of the graph::

            sage: D.is_directed_acyclic(certificate = True)
            (True, [4, 5, 6, 9, 0, 1, 2, 3, 7, 8, 10])

        Adding an edge from 7 to 4, though, makes a difference::

            sage: D.add_edge(7,4)
            sage: D.is_directed_acyclic()
            False

        Indeed, it creates a circuit `7, 4, 5`::

            sage: D.is_directed_acyclic(certificate = True)
            (False, [7, 4, 5])

        Checking acyclic graphs are indeed acyclic ::

            sage: def random_acyclic(n, p):
            ....:  g = graphs.RandomGNP(n, p)
            ....:  h = DiGraph()
            ....:  h.add_edges([ ((u,v) if u<v else (v,u)) for u,v,_ in g.edges(sort=True) ])
            ....:  return h
            ...
            sage: all( random_acyclic(100, .2).is_directed_acyclic()    # long time
            ....:      for i in range(50))
            True

        TESTS::

            sage: m = Matrix(3,[0, 1, 1, 0, 0, 0, 0, 1, 0])                             # needs sage.modules
            sage: g = DiGraph(m)                                                        # needs sage.modules
            sage: g.is_directed_acyclic(certificate=True)                               # needs sage.modules
            (True, [0, 2, 1])"""
    @overload
    def is_directed_acyclic(self, certificate=...) -> Any:
        """CGraphBackend.is_directed_acyclic(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 4667)

        Check whether the graph is both directed and acyclic (possibly with a
        certificate)

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); whether to return a
          certificate

        OUTPUT:

        When ``certificate=False``, returns a boolean value. When
        ``certificate=True`` :

        * If the graph is acyclic, returns a pair ``(True, ordering)`` where
          ``ordering`` is a list of the vertices such that ``u`` appears before
          ``v`` in ``ordering`` if ``u, v`` is an edge.

        * Else, returns a pair ``(False, cycle)`` where ``cycle`` is a list of
          vertices representing a circuit in the graph.

        ALGORITHM:

        We pick a vertex at random, think hard and find out that if we are
        to remove the vertex from the graph we must remove all of its
        out-neighbors in the first place. So we put all of its out-neighbours in
        a stack, and repeat the same procedure with the vertex on top of the
        stack (when a vertex on top of the stack has no out-neighbors, we remove
        it immediately). Of course, for each vertex we only add its outneighbors
        to the end of the stack once : if for some reason the previous algorithm
        leads us to do it twice, it means we have found a circuit.

        We keep track of the vertices whose out-neighborhood has been added to
        the stack once with a variable named ``tried``.

        There is no reason why the graph should be empty at the end of this
        procedure, so we run it again on the remaining vertices until none are
        left or a circuit is found.

        .. NOTE::

            The graph is assumed to be directed. An exception is raised if it is
            not.

        EXAMPLES:

        At first, the following graph is acyclic::

            sage: D = DiGraph({ 0:[1,2,3], 4:[2,5], 1:[8], 2:[7], 3:[7], 5:[6,7], 7:[8], 6:[9], 8:[10], 9:[10] })
            sage: D.plot(layout='circular').show()                                      # needs sage.plot
            sage: D.is_directed_acyclic()
            True

        Adding an edge from `9` to `7` does not change it::

            sage: D.add_edge(9,7)
            sage: D.is_directed_acyclic()
            True

        We can obtain as a proof an ordering of the vertices such that `u`
        appears before `v` if `uv` is an edge of the graph::

            sage: D.is_directed_acyclic(certificate = True)
            (True, [4, 5, 6, 9, 0, 1, 2, 3, 7, 8, 10])

        Adding an edge from 7 to 4, though, makes a difference::

            sage: D.add_edge(7,4)
            sage: D.is_directed_acyclic()
            False

        Indeed, it creates a circuit `7, 4, 5`::

            sage: D.is_directed_acyclic(certificate = True)
            (False, [7, 4, 5])

        Checking acyclic graphs are indeed acyclic ::

            sage: def random_acyclic(n, p):
            ....:  g = graphs.RandomGNP(n, p)
            ....:  h = DiGraph()
            ....:  h.add_edges([ ((u,v) if u<v else (v,u)) for u,v,_ in g.edges(sort=True) ])
            ....:  return h
            ...
            sage: all( random_acyclic(100, .2).is_directed_acyclic()    # long time
            ....:      for i in range(50))
            True

        TESTS::

            sage: m = Matrix(3,[0, 1, 1, 0, 0, 0, 0, 1, 0])                             # needs sage.modules
            sage: g = DiGraph(m)                                                        # needs sage.modules
            sage: g.is_directed_acyclic(certificate=True)                               # needs sage.modules
            (True, [0, 2, 1])"""
    @overload
    def is_directed_acyclic(self) -> Any:
        """CGraphBackend.is_directed_acyclic(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 4667)

        Check whether the graph is both directed and acyclic (possibly with a
        certificate)

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); whether to return a
          certificate

        OUTPUT:

        When ``certificate=False``, returns a boolean value. When
        ``certificate=True`` :

        * If the graph is acyclic, returns a pair ``(True, ordering)`` where
          ``ordering`` is a list of the vertices such that ``u`` appears before
          ``v`` in ``ordering`` if ``u, v`` is an edge.

        * Else, returns a pair ``(False, cycle)`` where ``cycle`` is a list of
          vertices representing a circuit in the graph.

        ALGORITHM:

        We pick a vertex at random, think hard and find out that if we are
        to remove the vertex from the graph we must remove all of its
        out-neighbors in the first place. So we put all of its out-neighbours in
        a stack, and repeat the same procedure with the vertex on top of the
        stack (when a vertex on top of the stack has no out-neighbors, we remove
        it immediately). Of course, for each vertex we only add its outneighbors
        to the end of the stack once : if for some reason the previous algorithm
        leads us to do it twice, it means we have found a circuit.

        We keep track of the vertices whose out-neighborhood has been added to
        the stack once with a variable named ``tried``.

        There is no reason why the graph should be empty at the end of this
        procedure, so we run it again on the remaining vertices until none are
        left or a circuit is found.

        .. NOTE::

            The graph is assumed to be directed. An exception is raised if it is
            not.

        EXAMPLES:

        At first, the following graph is acyclic::

            sage: D = DiGraph({ 0:[1,2,3], 4:[2,5], 1:[8], 2:[7], 3:[7], 5:[6,7], 7:[8], 6:[9], 8:[10], 9:[10] })
            sage: D.plot(layout='circular').show()                                      # needs sage.plot
            sage: D.is_directed_acyclic()
            True

        Adding an edge from `9` to `7` does not change it::

            sage: D.add_edge(9,7)
            sage: D.is_directed_acyclic()
            True

        We can obtain as a proof an ordering of the vertices such that `u`
        appears before `v` if `uv` is an edge of the graph::

            sage: D.is_directed_acyclic(certificate = True)
            (True, [4, 5, 6, 9, 0, 1, 2, 3, 7, 8, 10])

        Adding an edge from 7 to 4, though, makes a difference::

            sage: D.add_edge(7,4)
            sage: D.is_directed_acyclic()
            False

        Indeed, it creates a circuit `7, 4, 5`::

            sage: D.is_directed_acyclic(certificate = True)
            (False, [7, 4, 5])

        Checking acyclic graphs are indeed acyclic ::

            sage: def random_acyclic(n, p):
            ....:  g = graphs.RandomGNP(n, p)
            ....:  h = DiGraph()
            ....:  h.add_edges([ ((u,v) if u<v else (v,u)) for u,v,_ in g.edges(sort=True) ])
            ....:  return h
            ...
            sage: all( random_acyclic(100, .2).is_directed_acyclic()    # long time
            ....:      for i in range(50))
            True

        TESTS::

            sage: m = Matrix(3,[0, 1, 1, 0, 0, 0, 0, 1, 0])                             # needs sage.modules
            sage: g = DiGraph(m)                                                        # needs sage.modules
            sage: g.is_directed_acyclic(certificate=True)                               # needs sage.modules
            (True, [0, 2, 1])"""
    @overload
    def is_directed_acyclic(self, certificate=...) -> Any:
        """CGraphBackend.is_directed_acyclic(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 4667)

        Check whether the graph is both directed and acyclic (possibly with a
        certificate)

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); whether to return a
          certificate

        OUTPUT:

        When ``certificate=False``, returns a boolean value. When
        ``certificate=True`` :

        * If the graph is acyclic, returns a pair ``(True, ordering)`` where
          ``ordering`` is a list of the vertices such that ``u`` appears before
          ``v`` in ``ordering`` if ``u, v`` is an edge.

        * Else, returns a pair ``(False, cycle)`` where ``cycle`` is a list of
          vertices representing a circuit in the graph.

        ALGORITHM:

        We pick a vertex at random, think hard and find out that if we are
        to remove the vertex from the graph we must remove all of its
        out-neighbors in the first place. So we put all of its out-neighbours in
        a stack, and repeat the same procedure with the vertex on top of the
        stack (when a vertex on top of the stack has no out-neighbors, we remove
        it immediately). Of course, for each vertex we only add its outneighbors
        to the end of the stack once : if for some reason the previous algorithm
        leads us to do it twice, it means we have found a circuit.

        We keep track of the vertices whose out-neighborhood has been added to
        the stack once with a variable named ``tried``.

        There is no reason why the graph should be empty at the end of this
        procedure, so we run it again on the remaining vertices until none are
        left or a circuit is found.

        .. NOTE::

            The graph is assumed to be directed. An exception is raised if it is
            not.

        EXAMPLES:

        At first, the following graph is acyclic::

            sage: D = DiGraph({ 0:[1,2,3], 4:[2,5], 1:[8], 2:[7], 3:[7], 5:[6,7], 7:[8], 6:[9], 8:[10], 9:[10] })
            sage: D.plot(layout='circular').show()                                      # needs sage.plot
            sage: D.is_directed_acyclic()
            True

        Adding an edge from `9` to `7` does not change it::

            sage: D.add_edge(9,7)
            sage: D.is_directed_acyclic()
            True

        We can obtain as a proof an ordering of the vertices such that `u`
        appears before `v` if `uv` is an edge of the graph::

            sage: D.is_directed_acyclic(certificate = True)
            (True, [4, 5, 6, 9, 0, 1, 2, 3, 7, 8, 10])

        Adding an edge from 7 to 4, though, makes a difference::

            sage: D.add_edge(7,4)
            sage: D.is_directed_acyclic()
            False

        Indeed, it creates a circuit `7, 4, 5`::

            sage: D.is_directed_acyclic(certificate = True)
            (False, [7, 4, 5])

        Checking acyclic graphs are indeed acyclic ::

            sage: def random_acyclic(n, p):
            ....:  g = graphs.RandomGNP(n, p)
            ....:  h = DiGraph()
            ....:  h.add_edges([ ((u,v) if u<v else (v,u)) for u,v,_ in g.edges(sort=True) ])
            ....:  return h
            ...
            sage: all( random_acyclic(100, .2).is_directed_acyclic()    # long time
            ....:      for i in range(50))
            True

        TESTS::

            sage: m = Matrix(3,[0, 1, 1, 0, 0, 0, 0, 1, 0])                             # needs sage.modules
            sage: g = DiGraph(m)                                                        # needs sage.modules
            sage: g.is_directed_acyclic(certificate=True)                               # needs sage.modules
            (True, [0, 2, 1])"""
    @overload
    def is_strongly_connected(self) -> Any:
        """CGraphBackend.is_strongly_connected(self)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 4596)

        Check whether the graph is strongly connected.

        EXAMPLES:

        The circuit on 3 vertices is obviously strongly connected::

            sage: g = DiGraph({0: [1], 1: [2], 2: [0]})
            sage: g.is_strongly_connected()
            True

        But a transitive triangle is not::

            sage: g = DiGraph({0: [1,2], 1: [2]})
            sage: g.is_strongly_connected()
            False"""
    @overload
    def is_strongly_connected(self) -> Any:
        """CGraphBackend.is_strongly_connected(self)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 4596)

        Check whether the graph is strongly connected.

        EXAMPLES:

        The circuit on 3 vertices is obviously strongly connected::

            sage: g = DiGraph({0: [1], 1: [2], 2: [0]})
            sage: g.is_strongly_connected()
            True

        But a transitive triangle is not::

            sage: g = DiGraph({0: [1,2], 1: [2]})
            sage: g.is_strongly_connected()
            False"""
    @overload
    def is_strongly_connected(self) -> Any:
        """CGraphBackend.is_strongly_connected(self)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 4596)

        Check whether the graph is strongly connected.

        EXAMPLES:

        The circuit on 3 vertices is obviously strongly connected::

            sage: g = DiGraph({0: [1], 1: [2], 2: [0]})
            sage: g.is_strongly_connected()
            True

        But a transitive triangle is not::

            sage: g = DiGraph({0: [1,2], 1: [2]})
            sage: g.is_strongly_connected()
            False"""
    def is_subgraph(self, CGraphBackendother, vertices, boolignore_labels=...) -> Any:
        """CGraphBackend.is_subgraph(self, CGraphBackend other, vertices, bool ignore_labels=False)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 2879)

        Return whether the subgraph of ``self`` induced by ``vertices`` is a subgraph of ``other``.

        If ``vertices`` are the vertices of ``self``, return whether ``self`` is a subgraph of ``other``.

        INPUT:

            - ``other`` -- a subclass of :class:`CGraphBackend`
            - ``vertices`` -- a iterable over the vertex labels
            - ``ignore_labels`` -- boolean (default: ``False``); whether to ignore the labels

        EXAMPLES::

            sage: G = sage.graphs.base.dense_graph.DenseGraphBackend(4, directed=True)
            sage: H = sage.graphs.base.dense_graph.DenseGraphBackend(4, directed=True)
            sage: G.add_edges([[0,1],[0,2],[0,3],[1,2]], True)
            sage: H.add_edges([[0,1],[0,2],[0,3]], True)
            sage: G.is_subgraph(H, range(4))
            False
            sage: H.is_subgraph(G, range(4))
            True
            sage: G.is_subgraph(H, [0,1,3])
            True

        Ignore the labels or not::

            sage: G = sage.graphs.base.sparse_graph.SparseGraphBackend(3, directed=True)
            sage: G.multiple_edges(True)
            sage: H = sage.graphs.base.sparse_graph.SparseGraphBackend(3, directed=True)
            sage: H.multiple_edges(True)
            sage: G.add_edges([[0,1,'a'], [0,1,'b'], [0,2,'c'], [0,2,'d'], [0,2,'e']], True)
            sage: H.add_edges([[0,1,'a'], [0,1,'foo'], [0,2,'c'], [0,2,'d'], [0,2,'e'], [0,2,'e']], True)
            sage: G.is_subgraph(H, range(3))
            False
            sage: G.is_subgraph(H, range(3), ignore_labels=True)
            True

        Multiplicities of edges are considered::

            sage: G.is_subgraph(H, [0,2])
            True
            sage: H.is_subgraph(G, [0,2])
            False"""
    def iterator_edges(self, vertices, boollabels) -> Any:
        """CGraphBackend.iterator_edges(self, vertices, bool labels)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 2598)

        Iterate over the edges incident to a sequence of vertices.

        Edges are assumed to be undirected.

        .. WARNING::

            This will try to sort the two ends of every edge.

        INPUT:

        - ``vertices`` -- list of vertex labels

        - ``labels`` -- boolean, whether to return labels as well

        EXAMPLES::

            sage: G = sage.graphs.base.sparse_graph.SparseGraphBackend(9)
            sage: G.add_edge(1,2,3,False)
            sage: list(G.iterator_edges(range(9), False))
            [(1, 2)]
            sage: list(G.iterator_edges(range(9), True))
            [(1, 2, 3)]

        TESTS::

            sage: g = graphs.PetersenGraph()
            sage: g.edges_incident([0,1,2])
            [(0, 1, None),
             (0, 4, None),
             (0, 5, None),
             (1, 2, None),
             (1, 6, None),
             (2, 3, None),
             (2, 7, None)]"""
    def iterator_in_edges(self, vertices, boollabels) -> Any:
        """CGraphBackend.iterator_in_edges(self, vertices, bool labels)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 2692)

        Iterate over the incoming edges incident to a sequence of vertices.

        INPUT:

        - ``vertices`` -- list of vertex labels

        - ``labels`` -- boolean, whether to return labels as well

        EXAMPLES::

            sage: G = sage.graphs.base.sparse_graph.SparseGraphBackend(9)
            sage: G.add_edge(1,2,3,True)
            sage: list(G.iterator_in_edges([1], False))
            []
            sage: list(G.iterator_in_edges([2], False))
            [(1, 2)]
            sage: list(G.iterator_in_edges([2], True))
            [(1, 2, 3)]"""
    def iterator_in_nbrs(self, v) -> Any:
        """CGraphBackend.iterator_in_nbrs(self, v)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 2212)

        Iterate over the incoming neighbors of ``v``.

        INPUT:

        - ``v`` -- a vertex of this graph

        OUTPUT: an iterator over the in-neighbors of the vertex ``v``

        .. SEEALSO::

            - :meth:`iterator_nbrs`
              -- returns an iterator over the neighbors of a vertex

            - :meth:`iterator_out_nbrs`
              -- returns an iterator over the out-neighbors of a vertex

        EXAMPLES::

            sage: P = DiGraph(graphs.PetersenGraph().to_directed())
            sage: list(P._backend.iterator_in_nbrs(0))
            [1, 4, 5]

        TESTS::

            sage: P = DiGraph(graphs.PetersenGraph().to_directed())
            sage: list(P._backend.iterator_in_nbrs(63))
            Traceback (most recent call last):
            ...
            LookupError: vertex (63) is not a vertex of the graph"""
    def iterator_nbrs(self, v) -> Any:
        """CGraphBackend.iterator_nbrs(self, v)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 2162)

        Iterate over the neighbors of ``v``.

        INPUT:

        - ``v`` -- a vertex of this graph

        OUTPUT: an iterator over the neighbors the vertex ``v``

        .. SEEALSO::

            - :meth:`iterator_in_nbrs`
              -- returns an iterator over the in-neighbors of a vertex

            - :meth:`iterator_out_nbrs`
              -- returns an iterator over the out-neighbors of a vertex

            - :meth:`iterator_verts`
              -- returns an iterator over a given set of vertices

        EXAMPLES::

            sage: P = Graph(graphs.PetersenGraph())
            sage: list(P._backend.iterator_nbrs(0))
            [1, 4, 5]
            sage: Q = DiGraph(P)
            sage: list(Q._backend.iterator_nbrs(0))
            [1, 4, 5]"""
    def iterator_out_edges(self, vertices, boollabels) -> Any:
        """CGraphBackend.iterator_out_edges(self, vertices, bool labels)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 2669)

        Iterate over the outbound edges incident to a sequence of vertices.

        INPUT:

        - ``vertices`` -- list of vertex labels

        - ``labels`` -- boolean, whether to return labels as well

        EXAMPLES::

            sage: G = sage.graphs.base.sparse_graph.SparseGraphBackend(9)
            sage: G.add_edge(1,2,3,True)
            sage: list(G.iterator_out_edges([2], False))
            []
            sage: list(G.iterator_out_edges([1], False))
            [(1, 2)]
            sage: list(G.iterator_out_edges([1], True))
            [(1, 2, 3)]"""
    def iterator_out_nbrs(self, v) -> Any:
        """CGraphBackend.iterator_out_nbrs(self, v)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 2253)

        Iterate over the outgoing neighbors of ``v``.

        INPUT:

        - ``v`` -- a vertex of this graph

        OUTPUT: an iterator over the out-neighbors of the vertex ``v``

        .. SEEALSO::

            - :meth:`iterator_nbrs`
              -- returns an iterator over the neighbors of a vertex

            - :meth:`iterator_in_nbrs`
              -- returns an iterator over the in-neighbors of a vertex

        EXAMPLES::

            sage: P = DiGraph(graphs.PetersenGraph().to_directed())
            sage: list(P._backend.iterator_out_nbrs(0))
            [1, 4, 5]

        TESTS::

            sage: P = DiGraph(graphs.PetersenGraph().to_directed())
            sage: list(P._backend.iterator_out_nbrs(-41))
            Traceback (most recent call last):
            ...
            LookupError: vertex (-41) is not a vertex of the graph"""
    def iterator_unsorted_edges(self, vertices, boollabels) -> Any:
        """CGraphBackend.iterator_unsorted_edges(self, vertices, bool labels)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 2637)

        Iterate over the edges incident to a sequence of vertices.

        Edges are assumed to be undirected.

        This does not sort the ends of each edge.

        INPUT:

        - ``vertices`` -- list of vertex labels

        - ``labels`` -- boolean, whether to return labels as well

        EXAMPLES::

            sage: G = sage.graphs.base.sparse_graph.SparseGraphBackend(9)
            sage: G.add_edge(1,2,3,False)
            sage: list(G.iterator_unsorted_edges(range(9), False))
            [(2, 1)]
            sage: list(G.iterator_unsorted_edges(range(9), True))
            [(2, 1, 3)]

        TESTS::

            sage: G = Graph(sparse=True)
            sage: G.add_edge((1,'a'))
            sage: list(G._backend.iterator_unsorted_edges([1, 'a'],False))
            [(1, 'a')]"""
    @overload
    def iterator_verts(self, verts=...) -> Any:
        """CGraphBackend.iterator_verts(self, verts=None)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 1864)

        Iterate over the vertices of ``self`` intersected with
        ``verts``.

        INPUT:

        - ``verts`` -- an iterable container of objects (default: ``None``)

        OUTPUT:

        - If ``verts=None``, return an iterator over all vertices of this graph

        - If ``verts`` is a single vertex of the graph, treat it as the
          container ``[verts]``

        - If ``verts`` is a iterable container of vertices, find the
          intersection of ``verts`` with the vertex set of this graph and return
          an iterator over the resulting intersection

        .. SEEALSO::

            - :meth:`iterator_nbrs`
              -- returns an iterator over the neighbors of a vertex.

        EXAMPLES::

            sage: P = Graph(graphs.PetersenGraph())
            sage: list(P._backend.iterator_verts(P))
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            sage: list(P._backend.iterator_verts())
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            sage: list(P._backend.iterator_verts([1, 2, 3]))
            [1, 2, 3]
            sage: list(P._backend.iterator_verts([1, 2, 10]))
            [1, 2]"""
    @overload
    def iterator_verts(self, P) -> Any:
        """CGraphBackend.iterator_verts(self, verts=None)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 1864)

        Iterate over the vertices of ``self`` intersected with
        ``verts``.

        INPUT:

        - ``verts`` -- an iterable container of objects (default: ``None``)

        OUTPUT:

        - If ``verts=None``, return an iterator over all vertices of this graph

        - If ``verts`` is a single vertex of the graph, treat it as the
          container ``[verts]``

        - If ``verts`` is a iterable container of vertices, find the
          intersection of ``verts`` with the vertex set of this graph and return
          an iterator over the resulting intersection

        .. SEEALSO::

            - :meth:`iterator_nbrs`
              -- returns an iterator over the neighbors of a vertex.

        EXAMPLES::

            sage: P = Graph(graphs.PetersenGraph())
            sage: list(P._backend.iterator_verts(P))
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            sage: list(P._backend.iterator_verts())
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            sage: list(P._backend.iterator_verts([1, 2, 3]))
            [1, 2, 3]
            sage: list(P._backend.iterator_verts([1, 2, 10]))
            [1, 2]"""
    @overload
    def iterator_verts(self) -> Any:
        """CGraphBackend.iterator_verts(self, verts=None)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 1864)

        Iterate over the vertices of ``self`` intersected with
        ``verts``.

        INPUT:

        - ``verts`` -- an iterable container of objects (default: ``None``)

        OUTPUT:

        - If ``verts=None``, return an iterator over all vertices of this graph

        - If ``verts`` is a single vertex of the graph, treat it as the
          container ``[verts]``

        - If ``verts`` is a iterable container of vertices, find the
          intersection of ``verts`` with the vertex set of this graph and return
          an iterator over the resulting intersection

        .. SEEALSO::

            - :meth:`iterator_nbrs`
              -- returns an iterator over the neighbors of a vertex.

        EXAMPLES::

            sage: P = Graph(graphs.PetersenGraph())
            sage: list(P._backend.iterator_verts(P))
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            sage: list(P._backend.iterator_verts())
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            sage: list(P._backend.iterator_verts([1, 2, 3]))
            [1, 2, 3]
            sage: list(P._backend.iterator_verts([1, 2, 10]))
            [1, 2]"""
    @overload
    def loops(self, new=...) -> Any:
        """CGraphBackend.loops(self, new=None)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 1389)

        Check whether loops are allowed in this graph.

        INPUT:

        - ``new`` -- boolean (default: ``None``); to set or ``None`` to get

        OUTPUT:

        - If ``new=None``, return ``True`` if this graph allows self-loops or
          ``False`` if self-loops are not allowed

        - If ``new`` is a boolean, set the self-loop permission of this graph
          according to the boolean value of ``new``

        EXAMPLES::

            sage: G = Graph()
            sage: G._backend.loops()
            False
            sage: G._backend.loops(True)
            sage: G._backend.loops()
            True"""
    @overload
    def loops(self) -> Any:
        """CGraphBackend.loops(self, new=None)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 1389)

        Check whether loops are allowed in this graph.

        INPUT:

        - ``new`` -- boolean (default: ``None``); to set or ``None`` to get

        OUTPUT:

        - If ``new=None``, return ``True`` if this graph allows self-loops or
          ``False`` if self-loops are not allowed

        - If ``new`` is a boolean, set the self-loop permission of this graph
          according to the boolean value of ``new``

        EXAMPLES::

            sage: G = Graph()
            sage: G._backend.loops()
            False
            sage: G._backend.loops(True)
            sage: G._backend.loops()
            True"""
    @overload
    def loops(self, _True) -> Any:
        """CGraphBackend.loops(self, new=None)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 1389)

        Check whether loops are allowed in this graph.

        INPUT:

        - ``new`` -- boolean (default: ``None``); to set or ``None`` to get

        OUTPUT:

        - If ``new=None``, return ``True`` if this graph allows self-loops or
          ``False`` if self-loops are not allowed

        - If ``new`` is a boolean, set the self-loop permission of this graph
          according to the boolean value of ``new``

        EXAMPLES::

            sage: G = Graph()
            sage: G._backend.loops()
            False
            sage: G._backend.loops(True)
            sage: G._backend.loops()
            True"""
    @overload
    def loops(self) -> Any:
        """CGraphBackend.loops(self, new=None)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 1389)

        Check whether loops are allowed in this graph.

        INPUT:

        - ``new`` -- boolean (default: ``None``); to set or ``None`` to get

        OUTPUT:

        - If ``new=None``, return ``True`` if this graph allows self-loops or
          ``False`` if self-loops are not allowed

        - If ``new`` is a boolean, set the self-loop permission of this graph
          according to the boolean value of ``new``

        EXAMPLES::

            sage: G = Graph()
            sage: G._backend.loops()
            False
            sage: G._backend.loops(True)
            sage: G._backend.loops()
            True"""
    @overload
    def num_edges(self, directed) -> Any:
        """CGraphBackend.num_edges(self, directed)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 1421)

        Return the number of edges in ``self``.

        INPUT:

        - ``directed`` -- boolean; whether to count ``(u, v)`` and ``(v, u)`` as
          one or two edges

        OUTPUT:

        - If ``directed=True``, counts the number of directed edges in this
          graph. Otherwise, return the size of this graph.

        .. SEEALSO::

            - :meth:`num_verts`
              -- return the order of this graph.

        EXAMPLES::

            sage: G = Graph(graphs.PetersenGraph())
            sage: G._backend.num_edges(False)
            15

        TESTS:

        Ensure that :issue:`8395` is fixed. ::

            sage: G = Graph({1:[1]}); G
            Looped graph on 1 vertex
            sage: G.edges(sort=True, labels=False)
            [(1, 1)]
            sage: G.size()
            1
            sage: G = Graph({1:[2,2]}); G
            Multi-graph on 2 vertices
            sage: G.edges(sort=True, labels=False)
            [(1, 2), (1, 2)]
            sage: G.size()
            2
            sage: G = Graph({1:[1,1]}); G
            Looped multi-graph on 1 vertex
            sage: G.edges(sort=True, labels=False)
            [(1, 1), (1, 1)]
            sage: G.size()
            2
            sage: D = DiGraph({1:[1]}); D
            Looped digraph on 1 vertex
            sage: D.edges(sort=True, labels=False)
            [(1, 1)]
            sage: D.size()
            1
            sage: D = DiGraph({1:[2,2], 2:[1,1]}); D
            Multi-digraph on 2 vertices
            sage: D.edges(sort=True, labels=False)
            [(1, 2), (1, 2), (2, 1), (2, 1)]
            sage: D.size()
            4
            sage: D = DiGraph({1:[1,1]}); D
            Looped multi-digraph on 1 vertex
            sage: D.edges(sort=True, labels=False)
            [(1, 1), (1, 1)]
            sage: D.size()
            2
            sage: from sage.graphs.base.sparse_graph import SparseGraphBackend
            sage: S = SparseGraphBackend(7)
            sage: S.num_edges(False)
            0
            sage: S.loops(True)
            sage: S.add_edge(1, 1, None, directed=False)
            sage: S.num_edges(False)
            1
            sage: S.multiple_edges(True)
            sage: S.add_edge(1, 1, None, directed=False)
            sage: S.num_edges(False)
            2
            sage: from sage.graphs.base.dense_graph import DenseGraphBackend
            sage: D = DenseGraphBackend(7)
            sage: D.num_edges(False)
            0
            sage: D.loops(True)
            sage: D.add_edge(1, 1, None, directed=False)
            sage: D.num_edges(False)
            1"""
    @overload
    def num_edges(self, _False) -> Any:
        """CGraphBackend.num_edges(self, directed)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 1421)

        Return the number of edges in ``self``.

        INPUT:

        - ``directed`` -- boolean; whether to count ``(u, v)`` and ``(v, u)`` as
          one or two edges

        OUTPUT:

        - If ``directed=True``, counts the number of directed edges in this
          graph. Otherwise, return the size of this graph.

        .. SEEALSO::

            - :meth:`num_verts`
              -- return the order of this graph.

        EXAMPLES::

            sage: G = Graph(graphs.PetersenGraph())
            sage: G._backend.num_edges(False)
            15

        TESTS:

        Ensure that :issue:`8395` is fixed. ::

            sage: G = Graph({1:[1]}); G
            Looped graph on 1 vertex
            sage: G.edges(sort=True, labels=False)
            [(1, 1)]
            sage: G.size()
            1
            sage: G = Graph({1:[2,2]}); G
            Multi-graph on 2 vertices
            sage: G.edges(sort=True, labels=False)
            [(1, 2), (1, 2)]
            sage: G.size()
            2
            sage: G = Graph({1:[1,1]}); G
            Looped multi-graph on 1 vertex
            sage: G.edges(sort=True, labels=False)
            [(1, 1), (1, 1)]
            sage: G.size()
            2
            sage: D = DiGraph({1:[1]}); D
            Looped digraph on 1 vertex
            sage: D.edges(sort=True, labels=False)
            [(1, 1)]
            sage: D.size()
            1
            sage: D = DiGraph({1:[2,2], 2:[1,1]}); D
            Multi-digraph on 2 vertices
            sage: D.edges(sort=True, labels=False)
            [(1, 2), (1, 2), (2, 1), (2, 1)]
            sage: D.size()
            4
            sage: D = DiGraph({1:[1,1]}); D
            Looped multi-digraph on 1 vertex
            sage: D.edges(sort=True, labels=False)
            [(1, 1), (1, 1)]
            sage: D.size()
            2
            sage: from sage.graphs.base.sparse_graph import SparseGraphBackend
            sage: S = SparseGraphBackend(7)
            sage: S.num_edges(False)
            0
            sage: S.loops(True)
            sage: S.add_edge(1, 1, None, directed=False)
            sage: S.num_edges(False)
            1
            sage: S.multiple_edges(True)
            sage: S.add_edge(1, 1, None, directed=False)
            sage: S.num_edges(False)
            2
            sage: from sage.graphs.base.dense_graph import DenseGraphBackend
            sage: D = DenseGraphBackend(7)
            sage: D.num_edges(False)
            0
            sage: D.loops(True)
            sage: D.add_edge(1, 1, None, directed=False)
            sage: D.num_edges(False)
            1"""
    @overload
    def num_edges(self, _False) -> Any:
        """CGraphBackend.num_edges(self, directed)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 1421)

        Return the number of edges in ``self``.

        INPUT:

        - ``directed`` -- boolean; whether to count ``(u, v)`` and ``(v, u)`` as
          one or two edges

        OUTPUT:

        - If ``directed=True``, counts the number of directed edges in this
          graph. Otherwise, return the size of this graph.

        .. SEEALSO::

            - :meth:`num_verts`
              -- return the order of this graph.

        EXAMPLES::

            sage: G = Graph(graphs.PetersenGraph())
            sage: G._backend.num_edges(False)
            15

        TESTS:

        Ensure that :issue:`8395` is fixed. ::

            sage: G = Graph({1:[1]}); G
            Looped graph on 1 vertex
            sage: G.edges(sort=True, labels=False)
            [(1, 1)]
            sage: G.size()
            1
            sage: G = Graph({1:[2,2]}); G
            Multi-graph on 2 vertices
            sage: G.edges(sort=True, labels=False)
            [(1, 2), (1, 2)]
            sage: G.size()
            2
            sage: G = Graph({1:[1,1]}); G
            Looped multi-graph on 1 vertex
            sage: G.edges(sort=True, labels=False)
            [(1, 1), (1, 1)]
            sage: G.size()
            2
            sage: D = DiGraph({1:[1]}); D
            Looped digraph on 1 vertex
            sage: D.edges(sort=True, labels=False)
            [(1, 1)]
            sage: D.size()
            1
            sage: D = DiGraph({1:[2,2], 2:[1,1]}); D
            Multi-digraph on 2 vertices
            sage: D.edges(sort=True, labels=False)
            [(1, 2), (1, 2), (2, 1), (2, 1)]
            sage: D.size()
            4
            sage: D = DiGraph({1:[1,1]}); D
            Looped multi-digraph on 1 vertex
            sage: D.edges(sort=True, labels=False)
            [(1, 1), (1, 1)]
            sage: D.size()
            2
            sage: from sage.graphs.base.sparse_graph import SparseGraphBackend
            sage: S = SparseGraphBackend(7)
            sage: S.num_edges(False)
            0
            sage: S.loops(True)
            sage: S.add_edge(1, 1, None, directed=False)
            sage: S.num_edges(False)
            1
            sage: S.multiple_edges(True)
            sage: S.add_edge(1, 1, None, directed=False)
            sage: S.num_edges(False)
            2
            sage: from sage.graphs.base.dense_graph import DenseGraphBackend
            sage: D = DenseGraphBackend(7)
            sage: D.num_edges(False)
            0
            sage: D.loops(True)
            sage: D.add_edge(1, 1, None, directed=False)
            sage: D.num_edges(False)
            1"""
    @overload
    def num_edges(self, _False) -> Any:
        """CGraphBackend.num_edges(self, directed)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 1421)

        Return the number of edges in ``self``.

        INPUT:

        - ``directed`` -- boolean; whether to count ``(u, v)`` and ``(v, u)`` as
          one or two edges

        OUTPUT:

        - If ``directed=True``, counts the number of directed edges in this
          graph. Otherwise, return the size of this graph.

        .. SEEALSO::

            - :meth:`num_verts`
              -- return the order of this graph.

        EXAMPLES::

            sage: G = Graph(graphs.PetersenGraph())
            sage: G._backend.num_edges(False)
            15

        TESTS:

        Ensure that :issue:`8395` is fixed. ::

            sage: G = Graph({1:[1]}); G
            Looped graph on 1 vertex
            sage: G.edges(sort=True, labels=False)
            [(1, 1)]
            sage: G.size()
            1
            sage: G = Graph({1:[2,2]}); G
            Multi-graph on 2 vertices
            sage: G.edges(sort=True, labels=False)
            [(1, 2), (1, 2)]
            sage: G.size()
            2
            sage: G = Graph({1:[1,1]}); G
            Looped multi-graph on 1 vertex
            sage: G.edges(sort=True, labels=False)
            [(1, 1), (1, 1)]
            sage: G.size()
            2
            sage: D = DiGraph({1:[1]}); D
            Looped digraph on 1 vertex
            sage: D.edges(sort=True, labels=False)
            [(1, 1)]
            sage: D.size()
            1
            sage: D = DiGraph({1:[2,2], 2:[1,1]}); D
            Multi-digraph on 2 vertices
            sage: D.edges(sort=True, labels=False)
            [(1, 2), (1, 2), (2, 1), (2, 1)]
            sage: D.size()
            4
            sage: D = DiGraph({1:[1,1]}); D
            Looped multi-digraph on 1 vertex
            sage: D.edges(sort=True, labels=False)
            [(1, 1), (1, 1)]
            sage: D.size()
            2
            sage: from sage.graphs.base.sparse_graph import SparseGraphBackend
            sage: S = SparseGraphBackend(7)
            sage: S.num_edges(False)
            0
            sage: S.loops(True)
            sage: S.add_edge(1, 1, None, directed=False)
            sage: S.num_edges(False)
            1
            sage: S.multiple_edges(True)
            sage: S.add_edge(1, 1, None, directed=False)
            sage: S.num_edges(False)
            2
            sage: from sage.graphs.base.dense_graph import DenseGraphBackend
            sage: D = DenseGraphBackend(7)
            sage: D.num_edges(False)
            0
            sage: D.loops(True)
            sage: D.add_edge(1, 1, None, directed=False)
            sage: D.num_edges(False)
            1"""
    @overload
    def num_edges(self, _False) -> Any:
        """CGraphBackend.num_edges(self, directed)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 1421)

        Return the number of edges in ``self``.

        INPUT:

        - ``directed`` -- boolean; whether to count ``(u, v)`` and ``(v, u)`` as
          one or two edges

        OUTPUT:

        - If ``directed=True``, counts the number of directed edges in this
          graph. Otherwise, return the size of this graph.

        .. SEEALSO::

            - :meth:`num_verts`
              -- return the order of this graph.

        EXAMPLES::

            sage: G = Graph(graphs.PetersenGraph())
            sage: G._backend.num_edges(False)
            15

        TESTS:

        Ensure that :issue:`8395` is fixed. ::

            sage: G = Graph({1:[1]}); G
            Looped graph on 1 vertex
            sage: G.edges(sort=True, labels=False)
            [(1, 1)]
            sage: G.size()
            1
            sage: G = Graph({1:[2,2]}); G
            Multi-graph on 2 vertices
            sage: G.edges(sort=True, labels=False)
            [(1, 2), (1, 2)]
            sage: G.size()
            2
            sage: G = Graph({1:[1,1]}); G
            Looped multi-graph on 1 vertex
            sage: G.edges(sort=True, labels=False)
            [(1, 1), (1, 1)]
            sage: G.size()
            2
            sage: D = DiGraph({1:[1]}); D
            Looped digraph on 1 vertex
            sage: D.edges(sort=True, labels=False)
            [(1, 1)]
            sage: D.size()
            1
            sage: D = DiGraph({1:[2,2], 2:[1,1]}); D
            Multi-digraph on 2 vertices
            sage: D.edges(sort=True, labels=False)
            [(1, 2), (1, 2), (2, 1), (2, 1)]
            sage: D.size()
            4
            sage: D = DiGraph({1:[1,1]}); D
            Looped multi-digraph on 1 vertex
            sage: D.edges(sort=True, labels=False)
            [(1, 1), (1, 1)]
            sage: D.size()
            2
            sage: from sage.graphs.base.sparse_graph import SparseGraphBackend
            sage: S = SparseGraphBackend(7)
            sage: S.num_edges(False)
            0
            sage: S.loops(True)
            sage: S.add_edge(1, 1, None, directed=False)
            sage: S.num_edges(False)
            1
            sage: S.multiple_edges(True)
            sage: S.add_edge(1, 1, None, directed=False)
            sage: S.num_edges(False)
            2
            sage: from sage.graphs.base.dense_graph import DenseGraphBackend
            sage: D = DenseGraphBackend(7)
            sage: D.num_edges(False)
            0
            sage: D.loops(True)
            sage: D.add_edge(1, 1, None, directed=False)
            sage: D.num_edges(False)
            1"""
    @overload
    def num_edges(self, _False) -> Any:
        """CGraphBackend.num_edges(self, directed)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 1421)

        Return the number of edges in ``self``.

        INPUT:

        - ``directed`` -- boolean; whether to count ``(u, v)`` and ``(v, u)`` as
          one or two edges

        OUTPUT:

        - If ``directed=True``, counts the number of directed edges in this
          graph. Otherwise, return the size of this graph.

        .. SEEALSO::

            - :meth:`num_verts`
              -- return the order of this graph.

        EXAMPLES::

            sage: G = Graph(graphs.PetersenGraph())
            sage: G._backend.num_edges(False)
            15

        TESTS:

        Ensure that :issue:`8395` is fixed. ::

            sage: G = Graph({1:[1]}); G
            Looped graph on 1 vertex
            sage: G.edges(sort=True, labels=False)
            [(1, 1)]
            sage: G.size()
            1
            sage: G = Graph({1:[2,2]}); G
            Multi-graph on 2 vertices
            sage: G.edges(sort=True, labels=False)
            [(1, 2), (1, 2)]
            sage: G.size()
            2
            sage: G = Graph({1:[1,1]}); G
            Looped multi-graph on 1 vertex
            sage: G.edges(sort=True, labels=False)
            [(1, 1), (1, 1)]
            sage: G.size()
            2
            sage: D = DiGraph({1:[1]}); D
            Looped digraph on 1 vertex
            sage: D.edges(sort=True, labels=False)
            [(1, 1)]
            sage: D.size()
            1
            sage: D = DiGraph({1:[2,2], 2:[1,1]}); D
            Multi-digraph on 2 vertices
            sage: D.edges(sort=True, labels=False)
            [(1, 2), (1, 2), (2, 1), (2, 1)]
            sage: D.size()
            4
            sage: D = DiGraph({1:[1,1]}); D
            Looped multi-digraph on 1 vertex
            sage: D.edges(sort=True, labels=False)
            [(1, 1), (1, 1)]
            sage: D.size()
            2
            sage: from sage.graphs.base.sparse_graph import SparseGraphBackend
            sage: S = SparseGraphBackend(7)
            sage: S.num_edges(False)
            0
            sage: S.loops(True)
            sage: S.add_edge(1, 1, None, directed=False)
            sage: S.num_edges(False)
            1
            sage: S.multiple_edges(True)
            sage: S.add_edge(1, 1, None, directed=False)
            sage: S.num_edges(False)
            2
            sage: from sage.graphs.base.dense_graph import DenseGraphBackend
            sage: D = DenseGraphBackend(7)
            sage: D.num_edges(False)
            0
            sage: D.loops(True)
            sage: D.add_edge(1, 1, None, directed=False)
            sage: D.num_edges(False)
            1"""
    @overload
    def num_edges(self, _False) -> Any:
        """CGraphBackend.num_edges(self, directed)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 1421)

        Return the number of edges in ``self``.

        INPUT:

        - ``directed`` -- boolean; whether to count ``(u, v)`` and ``(v, u)`` as
          one or two edges

        OUTPUT:

        - If ``directed=True``, counts the number of directed edges in this
          graph. Otherwise, return the size of this graph.

        .. SEEALSO::

            - :meth:`num_verts`
              -- return the order of this graph.

        EXAMPLES::

            sage: G = Graph(graphs.PetersenGraph())
            sage: G._backend.num_edges(False)
            15

        TESTS:

        Ensure that :issue:`8395` is fixed. ::

            sage: G = Graph({1:[1]}); G
            Looped graph on 1 vertex
            sage: G.edges(sort=True, labels=False)
            [(1, 1)]
            sage: G.size()
            1
            sage: G = Graph({1:[2,2]}); G
            Multi-graph on 2 vertices
            sage: G.edges(sort=True, labels=False)
            [(1, 2), (1, 2)]
            sage: G.size()
            2
            sage: G = Graph({1:[1,1]}); G
            Looped multi-graph on 1 vertex
            sage: G.edges(sort=True, labels=False)
            [(1, 1), (1, 1)]
            sage: G.size()
            2
            sage: D = DiGraph({1:[1]}); D
            Looped digraph on 1 vertex
            sage: D.edges(sort=True, labels=False)
            [(1, 1)]
            sage: D.size()
            1
            sage: D = DiGraph({1:[2,2], 2:[1,1]}); D
            Multi-digraph on 2 vertices
            sage: D.edges(sort=True, labels=False)
            [(1, 2), (1, 2), (2, 1), (2, 1)]
            sage: D.size()
            4
            sage: D = DiGraph({1:[1,1]}); D
            Looped multi-digraph on 1 vertex
            sage: D.edges(sort=True, labels=False)
            [(1, 1), (1, 1)]
            sage: D.size()
            2
            sage: from sage.graphs.base.sparse_graph import SparseGraphBackend
            sage: S = SparseGraphBackend(7)
            sage: S.num_edges(False)
            0
            sage: S.loops(True)
            sage: S.add_edge(1, 1, None, directed=False)
            sage: S.num_edges(False)
            1
            sage: S.multiple_edges(True)
            sage: S.add_edge(1, 1, None, directed=False)
            sage: S.num_edges(False)
            2
            sage: from sage.graphs.base.dense_graph import DenseGraphBackend
            sage: D = DenseGraphBackend(7)
            sage: D.num_edges(False)
            0
            sage: D.loops(True)
            sage: D.add_edge(1, 1, None, directed=False)
            sage: D.num_edges(False)
            1"""
    @overload
    def num_verts(self) -> Any:
        """CGraphBackend.num_verts(self)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 1524)

        Return the number of vertices in ``self``.

        OUTPUT: the order of this graph

        .. SEEALSO::

            - :meth:`num_edges`
              -- return the number of (directed) edges in this graph.

        EXAMPLES::

            sage: G = Graph(graphs.PetersenGraph())
            sage: G._backend.num_verts()
            10"""
    @overload
    def num_verts(self) -> Any:
        """CGraphBackend.num_verts(self)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 1524)

        Return the number of vertices in ``self``.

        OUTPUT: the order of this graph

        .. SEEALSO::

            - :meth:`num_edges`
              -- return the number of (directed) edges in this graph.

        EXAMPLES::

            sage: G = Graph(graphs.PetersenGraph())
            sage: G._backend.num_verts()
            10"""
    def out_degree(self, v) -> Any:
        """CGraphBackend.out_degree(self, v)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 2113)

        Return the out-degree of ``v``.

        INPUT:

        - ``v`` -- a vertex of the graph

        EXAMPLES::


            sage: D = DiGraph( { 0: [1,2,3], 1: [0,2], 2: [3], 3: [4], 4: [0,5], 5: [1] } )
            sage: D.out_degree(1)
            2"""
    def relabel(self, perm, directed) -> Any:
        """CGraphBackend.relabel(self, perm, directed)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 1926)

        Relabel the graph according to ``perm``.

        INPUT:

        - ``perm`` -- anything which represents a permutation as
          ``v --> perm[v]``, for example a dict or a list

        - ``directed`` -- ignored (this is here for compatibility with other
          backends)

        EXAMPLES::

            sage: G = Graph(graphs.PetersenGraph())
            sage: G._backend.relabel(range(9,-1,-1), False)
            sage: G.edges(sort=True)
            [(0, 2, None),
             (0, 3, None),
             (0, 5, None),
             (1, 3, None),
             (1, 4, None),
             (1, 6, None),
             (2, 4, None),
             (2, 7, None),
             (3, 8, None),
             (4, 9, None),
             (5, 6, None),
             (5, 9, None),
             (6, 7, None),
             (7, 8, None),
             (8, 9, None)]"""
    def shortest_path(self, x, y, distance_flag=...) -> Any:
        """CGraphBackend.shortest_path(self, x, y, distance_flag=False)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 3492)

        Return the shortest path or distance from ``x`` to ``y``.

        INPUT:

        - ``x`` -- the starting vertex in the shortest path from ``x`` to ``y``

        - ``y`` -- the end vertex in the shortest path from ``x`` to ``y``

        - ``distance_flag`` -- boolean (default: ``False``); when set to
          ``True``, the shortest path distance from ``x`` to ``y`` is returned
          instead of the path

        OUTPUT:

        - A list of vertices in the shortest path from ``x`` to ``y`` or
          distance from ``x`` to ``y`` is returned depending upon the value of
          parameter ``distance_flag``

        EXAMPLES::

            sage: G = Graph(graphs.PetersenGraph())
            sage: G.shortest_path(0, 1)
            [0, 1]
            sage: G.shortest_path_length(0, 1)
            1"""
    def shortest_path_all_vertices(self, v, cutoff=..., distance_flag=...) -> Any:
        '''CGraphBackend.shortest_path_all_vertices(self, v, cutoff=None, distance_flag=False)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 4201)

        Return for each reachable vertex ``u`` a shortest ``v-u`` path or
        distance from ``v`` to ``u``.

        INPUT:

        - ``v`` -- a starting vertex in the shortest path

        - ``cutoff`` -- integer (default: ``None``); maximal distance of
          returned paths (longer paths will not be returned), ignored when set
          to ``None``

        - ``distance_flag`` -- boolean (default: ``False``); when set to
          ``True``, each vertex ``u`` connected to ``v`` is mapped to shortest
          path distance from ``v`` to ``u`` instead of the shortest path in the
          output dictionary.

        OUTPUT:

        - A dictionary which maps each vertex ``u`` connected to ``v`` to the
          shortest path list or distance from ``v`` to ``u`` depending upon the
          value of parameter ``distance_flag``

        .. NOTE::

            The weight of edges is not taken into account.

        ALGORITHM:

        This is just a breadth-first search.

        EXAMPLES:

        On the Petersen Graph::

            sage: g = graphs.PetersenGraph()
            sage: paths = g._backend.shortest_path_all_vertices(0)
            sage: all((not paths[v] or len(paths[v])-1 == g.distance(0,v)) for v in g)
            True
            sage: g._backend.shortest_path_all_vertices(0, distance_flag=True)
            {0: 0, 1: 1, 2: 2, 3: 2, 4: 1, 5: 1, 6: 2, 7: 2, 8: 2, 9: 2}

        On a disconnected graph::

            sage: g = 2 * graphs.RandomGNP(20, .3)
            sage: paths = g._backend.shortest_path_all_vertices(0)
            sage: all((v not in paths and g.distance(0, v) == +Infinity) or len(paths[v]) - 1 == g.distance(0, v) for v in g)
            True

        TESTS::

            sage: graphs.KrackhardtKiteGraph().eccentricity("a")
            Traceback (most recent call last):
            ...
            LookupError: vertex \'a\' is not a vertex of the graph'''
    def shortest_path_special(self, x, y, exclude_vertices=..., exclude_edges=..., distance_flag=...) -> Any:
        """CGraphBackend.shortest_path_special(self, x, y, exclude_vertices=None, exclude_edges=None, distance_flag=False)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 3298)

        Return the shortest path or distance from ``x`` to ``y``.

        This method is an extension of :meth:`shortest_path` method enabling to
        exclude vertices and/or edges from the search for the shortest path
        between ``x`` and ``y``.

        INPUT:

        - ``x`` -- the starting vertex in the shortest path from ``x`` to ``y``

        - ``y`` -- the end vertex in the shortest path from ``x`` to ``y``

        - ``exclude_vertices`` -- iterable container (default: ``None``);
          iterable of vertices to exclude from the graph while calculating the
          shortest path from ``x`` to ``y``

        - ``exclude_edges`` -- iterable container (default: ``None``); iterable
          of edges to exclude from the graph while calculating the shortest path
          from ``x`` to ``y``

        - ``distance_flag`` -- boolean (default: ``False``); when set to
          ``True``, the shortest path distance from ``x`` to ``y`` is returned
          instead of the path

        OUTPUT:

        - A list of vertices in the shortest path from ``x`` to ``y`` or
          distance from ``x`` to ``y`` is returned depending upon the value of
          parameter ``distance_flag``

        EXAMPLES::

            sage: G = Graph([(1, 2), (2, 3), (3, 4), (1, 5), (5, 6), (6, 7), (7, 4)])
            sage: G._backend.shortest_path_special(1, 4)
            [1, 2, 3, 4]
            sage: G._backend.shortest_path_special(1, 4, exclude_vertices=[5,7])
            [1, 2, 3, 4]
            sage: G._backend.shortest_path_special(1, 4, exclude_vertices=[2, 3])
            [1, 5, 6, 7, 4]
            sage: G._backend.shortest_path_special(1, 4, exclude_vertices=[2], exclude_edges=[(5, 6)])
            []
            sage: G._backend.shortest_path_special(1, 4, exclude_vertices=[2], exclude_edges=[(2, 3)])
            [1, 5, 6, 7, 4]"""
    def shortest_path_to_set(self, source, targets, by_weight=..., edge_weight=..., exclude_vertices=..., report_weight=...) -> Any:
        """CGraphBackend.shortest_path_to_set(self, source, targets, by_weight=False, edge_weight=None, exclude_vertices=None, report_weight=False)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 3632)

        Return the shortest path from ``source`` to any vertex in ``targets``.

        INPUT:

        - ``source`` -- the starting vertex.

        - ``targets`` -- iterable container; the set of end vertices.

        - ``edge_weight`` -- dictionary (default: ``None``); a dictionary
          that takes as input an edge ``(u, v)`` and outputs its weight.
          If not ``None``, ``by_weight`` is automatically set to ``True``.
          If ``None`` and ``by_weight`` is ``True``, we use the edge
          label ``l`` as a weight.

        - ``by_weight`` -- boolean (default: ``False``); if ``True``, the edges
          in the graph are weighted, otherwise all edges have weight 1.

        - ``exclude_vertices`` -- iterable container (default: ``None``);
          iterable of vertices to exclude from the graph while calculating the
          shortest path from ``source`` to any vertex in ``targets``.

        - ``report_weight`` -- boolean (default: ``False``); if ``False``, just
          a path is returned. Otherwise a tuple of path length and path is
          returned.

        OUTPUT:

        - A list of vertices in the shortest path from ``source`` to any vertex
          in ``targets`` or  a tuple of path lengh and path is returned
          depending upon the value of parameter ``report_weight``.

        EXAMPLES::

            sage: g = Graph([(1, 2, 10), (1, 3, 20), (1, 4, 30)])
            sage: g._backend.shortest_path_to_set(1, {3, 4}, by_weight=True)
            [1, 3]
            sage: g = Graph([(1, 2, 10), (2, 3, 10), (1, 4, 20), (4, 5, 20), (1, 6, 30), (6, 7, 30)])
            sage: g._backend.shortest_path_to_set(1, {5, 7}, by_weight=True, exclude_vertices=[4], report_weight=True)
            (60.0, [1, 6, 7])

        TESTS::

            sage: g = Graph([(1, 2, 10), (1, 3, 20), (1, 4, 30)])
            sage: g._backend.shortest_path_to_set(1, {3, 4}, exclude_vertices=[3], by_weight=True)
            [1, 4]
            sage: g._backend.shortest_path_to_set(1, {1, 3, 4}, by_weight=True)
            [1]

        ``source`` must not be in ``exclude_vertices``::

            sage: g._backend.shortest_path_to_set(1, {3, 4}, exclude_vertices=[1])
            Traceback (most recent call last):
            ...
            ValueError: source must not be in exclude_vertices.

        When no path exists from ``source`` to ``targets``, raise an error.

            sage: g._backend.shortest_path_to_set(1, {3, 4}, exclude_vertices=[3, 4])
            Traceback (most recent call last):
            ...
            ValueError: no path found from source to targets.

        ``exclude_vertices`` must be iterable::

            sage: g._backend.shortest_path_to_set(1, {1, 3, 4}, exclude_vertices=100)
            Traceback (most recent call last):
            ...
            TypeError: exclude_vertices (100) are not iterable."""
    @overload
    def strongly_connected_component_containing_vertex(self, v) -> Any:
        """CGraphBackend.strongly_connected_component_containing_vertex(self, v)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 4635)

        Return the strongly connected component containing the given vertex.

        INPUT:

        - ``v`` -- a vertex

        EXAMPLES:

        The digraph obtained from the ``PetersenGraph`` has an unique strongly
        connected component::

            sage: g = DiGraph(graphs.PetersenGraph())
            sage: g.strongly_connected_component_containing_vertex(0)
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        In the Butterfly DiGraph, each vertex is a strongly connected
        component::

            sage: g = digraphs.ButterflyGraph(3)
            sage: all([v] == g.strongly_connected_component_containing_vertex(v) for v in g)
            True"""
    @overload
    def strongly_connected_component_containing_vertex(self, v) -> Any:
        """CGraphBackend.strongly_connected_component_containing_vertex(self, v)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 4635)

        Return the strongly connected component containing the given vertex.

        INPUT:

        - ``v`` -- a vertex

        EXAMPLES:

        The digraph obtained from the ``PetersenGraph`` has an unique strongly
        connected component::

            sage: g = DiGraph(graphs.PetersenGraph())
            sage: g.strongly_connected_component_containing_vertex(0)
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        In the Butterfly DiGraph, each vertex is a strongly connected
        component::

            sage: g = digraphs.ButterflyGraph(3)
            sage: all([v] == g.strongly_connected_component_containing_vertex(v) for v in g)
            True"""
    def subgraph_given_vertices(self, CGraphBackendother, vertices) -> Any:
        """CGraphBackend.subgraph_given_vertices(self, CGraphBackend other, vertices)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 2929)

        Initialize ``other`` to be the subgraph of ``self`` with given vertices.

        INPUT:

        - ``other`` -- a (mutable) subclass of :class:`CGraphBackend`
        - ``vertices`` -- list of vertex labels

        .. NOTE::

            ``other`` is assumed to be the empty graph.

        EXAMPLES:

        Make a dense copy::

            sage: G = sage.graphs.base.dense_graph.DenseGraphBackend(9, directed=True)
            sage: G.loops(True)
            sage: G.add_edges([[0,1], [1,2], [2,3], [3,4], [4,5], [5,6], [7,8], [3,3]], True)
            sage: H = sage.graphs.base.dense_graph.DenseGraphBackend(0, directed=True)
            sage: H.loops(True)
            sage: G.subgraph_given_vertices(H, range(9))
            sage: list(H.iterator_out_edges(list(range(9)), False)) == list(G.iterator_out_edges(list(range(9)), False))
            True

        Make a sparse copy::

            sage: H = sage.graphs.base.sparse_graph.SparseGraphBackend(0, directed=True)
            sage: H.loops(True)
            sage: G.subgraph_given_vertices(H, range(9))
            sage: sorted(list(H.iterator_out_edges(list(range(9)), False))) == sorted(list(G.iterator_out_edges(list(range(9)), False)))
            True

        Initialize a proper subgraph::

            sage: H = sage.graphs.base.sparse_graph.SparseGraphBackend(0, directed=True)
            sage: H.loops(True)
            sage: G.subgraph_given_vertices(H, [2,3,4,5])
            sage: list(H.iterator_out_edges(list(range(9)), False))
            [(2, 3), (3, 3), (3, 4), (4, 5)]

        Loops are removed, if the other graph does not allow loops::

            sage: H = sage.graphs.base.sparse_graph.SparseGraphBackend(0, directed=True)
            sage: H.loops(False)
            sage: G.subgraph_given_vertices(H, [2,3,4,5])
            sage: list(H.iterator_out_edges(list(range(9)), False))
            [(2, 3), (3, 4), (4, 5)]

        Multiple edges and labels are copied::

            sage: G = sage.graphs.base.sparse_graph.SparseGraphBackend(4, directed=False)
            sage: G.multiple_edges(True)
            sage: G.add_edges([[0,1,'a'], [1,2,'b'], [2,3,'c'], [0,1,'d']], False)
            sage: H = sage.graphs.base.sparse_graph.SparseGraphBackend(0, directed=False)
            sage: H.multiple_edges(True)
            sage: G.subgraph_given_vertices(H, [0,1,2])
            sage: list(H.iterator_edges(list(range(4)), True))
            [(0, 1, 'a'), (0, 1, 'd'), (1, 2, 'b')]

        Multiple edges are removed, if the other graph does not allow them::

            sage: H = sage.graphs.base.sparse_graph.SparseGraphBackend(0, directed=False)
            sage: H.multiple_edges(False)
            sage: G.subgraph_given_vertices(H, [0,1,2])
            sage: list(H.iterator_edges(list(range(4)), True))
            [(0, 1, 'd'), (1, 2, 'b')]

        Labels are removed, if the other graph does not allow them::

            sage: H = sage.graphs.base.dense_graph.DenseGraphBackend(0, directed=False)
            sage: G.subgraph_given_vertices(H, [0,1,2])
            sage: list(H.iterator_edges(list(range(4)), True))
            [(0, 1, None), (1, 2, None)]

        A directed subgraph of an undirected graph is taken by initializing
        with edges in both directions::

            sage: G = sage.graphs.base.sparse_graph.SparseGraphBackend(4, directed=True)
            sage: G.loops(True)
            sage: G.multiple_edges(True)
            sage: G.add_edges([[0,1,'a'], [1,2,'b'], [2,3,'c'], [0,1,'d'], [2,2,'e']], False)
            sage: H = sage.graphs.base.sparse_graph.SparseGraphBackend(0, directed=True)
            sage: H.multiple_edges(True)
            sage: H.loops(True)
            sage: G.subgraph_given_vertices(H, [0,1,2])
            sage: list(H.iterator_out_edges(list(range(4)), True))
            [(0, 1, 'a'),
             (0, 1, 'd'),
             (1, 0, 'a'),
             (1, 0, 'd'),
             (1, 2, 'b'),
             (2, 1, 'b'),
             (2, 2, 'e')]

        An undirected subgraph of a directeed graph is not defined::

            sage: G = sage.graphs.base.sparse_graph.SparseGraphBackend(4, directed=True)
            sage: G.add_edges([[0,1,'a'], [1,2,'b'], [2,3,'c']], False)
            sage: H = sage.graphs.base.sparse_graph.SparseGraphBackend(0, directed=False)
            sage: G.subgraph_given_vertices(H, [0,1,2])
            Traceback (most recent call last):
            ...
            ValueError: cannot obtain an undirected subgraph of a directed graph

        TESTS:

        All the examples for ``self`` a static sparse graph.

        Make a dense copy::

            sage: from sage.graphs.base.static_sparse_backend import StaticSparseBackend
            sage: G = Graph(loops=True)
            sage: G.add_edges([[0,1], [1,2], [2,3], [3,4], [4,5], [5,6], [7,8], [3,3]])
            sage: G = StaticSparseBackend(G)
            sage: H = sage.graphs.base.dense_graph.DenseGraphBackend(0, directed=False)
            sage: H.loops(True)
            sage: G.subgraph_given_vertices(H, range(9))
            sage: list(H.iterator_edges(list(range(9)), False)) == list(G.iterator_edges(list(range(9)), False))
            True

        Make a sparse copy::

            sage: H = sage.graphs.base.sparse_graph.SparseGraphBackend(0, directed=False)
            sage: H.loops(True)
            sage: G.subgraph_given_vertices(H, range(9))
            sage: sorted(list(H.iterator_edges(list(range(9)), False))) == sorted(list(G.iterator_edges(list(range(9)), False)))
            True

        Initialize a proper subgraph::

            sage: H = sage.graphs.base.sparse_graph.SparseGraphBackend(0, directed=False)
            sage: H.loops(True)
            sage: G.subgraph_given_vertices(H, [2,3,4,5])
            sage: list(H.iterator_edges(list(range(9)), False))
            [(2, 3), (3, 3), (3, 4), (4, 5)]

        Loops are removed, if the other graph does not allow loops::

            sage: H = sage.graphs.base.sparse_graph.SparseGraphBackend(0, directed=False)
            sage: H.loops(False)
            sage: G.subgraph_given_vertices(H, [2,3,4,5])
            sage: list(H.iterator_edges(list(range(9)), False))
            [(2, 3), (3, 4), (4, 5)]

        Multiple edges and labels are copied::

            sage: G = Graph(multiedges=True)
            sage: G.add_edges([[0,1,'a'], [1,2,'b'], [2,3,'c'], [0,1,'d']], False)
            sage: G = StaticSparseBackend(G)
            sage: H = sage.graphs.base.sparse_graph.SparseGraphBackend(0, directed=False)
            sage: H.multiple_edges(True)
            sage: G.subgraph_given_vertices(H, [0,1,2])
            sage: list(H.iterator_edges(list(range(4)), True))
            [(0, 1, 'a'), (0, 1, 'd'), (1, 2, 'b')]

        Multiple edges are removed, if the other graph does not allow them::

            sage: H = sage.graphs.base.sparse_graph.SparseGraphBackend(0, directed=False)
            sage: H.multiple_edges(False)
            sage: G.subgraph_given_vertices(H, [0,1,2])
            sage: list(H.iterator_edges(list(range(4)), True))
            [(0, 1, 'a'), (1, 2, 'b')]

        Labels are removed, if the other graph does not allow them::

            sage: H = sage.graphs.base.dense_graph.DenseGraphBackend(0, directed=False)
            sage: G.subgraph_given_vertices(H, [0,1,2])
            sage: list(H.iterator_edges(list(range(4)), True))
            [(0, 1, None), (1, 2, None)]

        A directed subgraph of an undirected graph is taken by initializing
        with edges in both directions::

            sage: G = Graph(multiedges=True, loops=True)
            sage: G.add_edges([[0,1,'a'], [1,2,'b'], [2,3,'c'], [0,1,'d'], [2,2,'e']])
            sage: G = StaticSparseBackend(G)
            sage: H = sage.graphs.base.sparse_graph.SparseGraphBackend(0, directed=True)
            sage: H.multiple_edges(True)
            sage: H.loops(True)
            sage: G.subgraph_given_vertices(H, [0,1,2])
            sage: list(H.iterator_out_edges(list(range(4)), True))
            [(0, 1, 'a'),
             (0, 1, 'd'),
             (1, 0, 'a'),
             (1, 0, 'd'),
             (1, 2, 'b'),
             (2, 1, 'b'),
             (2, 2, 'e')]

        An undirected subgraph of a directeed graph is not defined::

            sage: G = DiGraph()
            sage: G.add_edges([[0,1,'a'], [1,2,'b'], [2,3,'c']])
            sage: G = StaticSparseBackend(G)
            sage: H = sage.graphs.base.sparse_graph.SparseGraphBackend(0, directed=False)
            sage: G.subgraph_given_vertices(H, [0,1,2])
            Traceback (most recent call last):
            ...
            ValueError: cannot obtain an undirected subgraph of a directed graph"""

class Search_iterator:
    """Search_iterator(graph, v, direction=0, reverse=False, ignore_direction=False, report_distance=False, edges=False, forbidden_vertices=None)

    File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 4865)

    An iterator for traversing a (di)graph.

    This class is commonly used to perform a depth-first or breadth-first
    search. The class does not build all at once in memory the whole list of
    visited vertices. The class maintains the following variables:

    - ``graph`` -- a graph whose vertices are to be iterated over

    - ``direction`` -- integer; this determines the position at which vertices
      to be visited are removed from the list. For breadth-first search (BFS),
      element removal follow a first-in first-out (FIFO) protocol, as signified
      by the value ``direction=0``. We use a queue to maintain the list of
      vertices to visit in this case. For depth-first search (DFS), element
      removal follow a last-in first-out (LIFO) protocol, as signified by the
      value ``direction=-1``. In this case, we use a stack to maintain the list
      of vertices to visit.

    - ``stack`` -- list of vertices to visit, used only when ``direction=-1``

    - ``queue`` -- a queue of vertices to visit, used only when ``direction=0``

    - ``seen`` -- list of vertices that are already visited

    - ``test_out`` -- boolean; whether we want to consider the out-neighbors
      of the graph to be traversed. For undirected graphs, we consider both
      the in- and out-neighbors. However, for digraphs we only traverse along
      out-neighbors.

    - ``test_in`` -- boolean; whether we want to consider the in-neighbors of
      the graph to be traversed. For undirected graphs, we consider both
      the in- and out-neighbors.

    EXAMPLES::

        sage: g = graphs.PetersenGraph()
        sage: list(g.breadth_first_search(0))
        [0, 1, 4, 5, 2, 6, 3, 9, 7, 8]"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, graph, v, direction=..., reverse=..., ignore_direction=..., report_distance=..., edges=..., forbidden_vertices=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 4921)

                Initialize an iterator for traversing a (di)graph.

                INPUT:

                - ``graph`` -- a graph to be traversed

                - ``v`` -- a vertex in ``graph`` from which to start the traversal

                - ``direction`` -- integer (default: `0`); this determines the
                  position at which vertices to be visited are removed from the
                  list. For breadth-first search (BFS), element removal follow a
                  first-in first-out (FIFO) protocol, as signified by the value
                  ``direction=0``. We use a queue to maintain the list of vertices to
                  visit in this case. For depth-first search (DFS), element removal
                  follow a last-in first-out (LIFO) protocol, as signified by the value
                  ``direction=-1``. In this case, we use a stack to maintain the list of
                  vertices to visit.

                - ``reverse`` -- boolean (default: ``False``); this is only relevant to
                  digraphs. If ``graph`` is a digraph, consider the reversed graph in
                  which the out-neighbors become the in-neighbors and vice versa.

                - ``ignore_direction`` -- boolean (default: ``False``); this is only
                  relevant to digraphs. If ``graph`` is a digraph, ignore all
                  orientations and consider the graph as undirected.

                - ``report_distance`` -- boolean (default: ``False``); if ``True``,
                  reports pairs ``(vertex, distance)`` where ``distance`` is the
                  distance from the ``start`` nodes. If ``False`` only the vertices are
                  reported.
                  Only allowed for ``direction=0``, i.e. BFS.

                - ``edges`` -- boolean (default: ``False``); whether to return the edges
                  of the BFS tree in the order of visit or the vertices (default).
                  Edges are directed in root to leaf orientation of the tree.
                  Only allowed for ``direction=0``, i.e. BFS.

                  Note that parameters ``edges`` and ``report_distance`` cannot be
                  ``True`` simultaneously.

                - ``forbidden_vertices`` -- list (default: ``None``); set of vertices to
                  avoid during the search. The start vertex ``v`` cannot be in this set.

                EXAMPLES::

                    sage: g = graphs.PetersenGraph()
                    sage: list(g.breadth_first_search(0))
                    [0, 1, 4, 5, 2, 6, 3, 9, 7, 8]
                    sage: list(g.breadth_first_search(0, forbidden_vertices=[1, 2]))
                    [0, 4, 5, 3, 9, 7, 8, 6]

                TESTS:

                A vertex which does not belong to the graph::

                    sage: list(g.breadth_first_search(-9))
                    Traceback (most recent call last):
                    ...
                    LookupError: vertex (-9) is not a vertex of the graph

                An empty graph::

                    sage: list(Graph().breadth_first_search(''))
                    Traceback (most recent call last):
                    ...
                    LookupError: vertex ('') is not a vertex of the graph

                Immutable graphs (see :issue:`16019`)::

                    sage: DiGraph([(1, 2)], immutable=True).connected_components(sort=True)
                    [[1, 2]]
        """
    def __iter__(self) -> Any:
        """Search_iterator.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 5055)

        Iterate over a traversal of a graph.

        EXAMPLES::

            sage: g = graphs.PetersenGraph()
            sage: g.breadth_first_search(0)
            <generator object ...breadth_first_search at ..."""
    def __next__(self) -> Any:
        """Search_iterator.__next__(self)

        File: /build/sagemath/src/sage/src/sage/graphs/base/c_graph.pyx (starting at line 5171)

        Return the next vertex in a breadth first search traversal of a graph.

        EXAMPLES::

            sage: g = graphs.PetersenGraph()
            sage: g.breadth_first_search(0)
            <generator object ...breadth_first_search at ...
            sage: next(g.breadth_first_search(0))
            0"""
