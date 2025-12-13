import sage.matroids.matroid
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.matroids.utilities import newlabel as newlabel, sanitize_contractions_deletions as sanitize_contractions_deletions, split_vertex as split_vertex
from typing import Any, ClassVar, overload

class GraphicMatroid(sage.matroids.matroid.Matroid):
    """GraphicMatroid(G, groundset=None)

    File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 95)

    The graphic matroid class.

    INPUT:

    - ``G`` -- :class:`Graph`
    - ``groundset`` -- list (optional); in 1-1 correspondence with ``G.edge_iterator()``

    OUTPUT: :class:`GraphicMatroid` where the groundset elements are the edges of `G`

    .. NOTE::

        If a disconnected graph is given as input, the instance of :class:`GraphicMatroid`
        will connect the graph components and store this as its graph.

    EXAMPLES::

        sage: from sage.matroids.advanced import *
        sage: M = GraphicMatroid(graphs.BullGraph()); M
        Graphic matroid of rank 4 on 5 elements
        sage: N = GraphicMatroid(graphs.CompleteBipartiteGraph(3,3)); N
        Graphic matroid of rank 5 on 9 elements

    A disconnected input will get converted to a connected graph internally::

        sage: G1 = graphs.CycleGraph(3); G2 = graphs.DiamondGraph()
        sage: G = G1.disjoint_union(G2)
        sage: len(G)
        7
        sage: G.is_connected()
        False
        sage: M = GraphicMatroid(G)
        sage: M
        Graphic matroid of rank 5 on 8 elements
        sage: H = M.graph()
        sage: H
        Looped multi-graph on 6 vertices
        sage: H.is_connected()
        True
        sage: M.is_connected()
        False

    You can still locate an edge using the vertices of the input graph::

        sage: G1 = graphs.CycleGraph(3); G2 = graphs.DiamondGraph()
        sage: G = G1.disjoint_union(G2)
        sage: M = Matroid(G)
        sage: H = M.graph()
        sage: vm = M.vertex_map()
        sage: (u, v, l) = G.random_edge()
        sage: H.has_edge(vm[u], vm[v])
        True"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @overload
    def __init__(self, G, groundset=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 152)

                See the class definition for full documentation.

                EXAMPLES::

                    sage: from sage.matroids.advanced import *
                    sage: G1 = graphs.CycleGraph(3); G2 = graphs.DiamondGraph()
                    sage: G = G1.disjoint_union(G2)
                    sage: M = GraphicMatroid(G); M
                    Graphic matroid of rank 5 on 8 elements
                    sage: M.graph()
                    Looped multi-graph on 6 vertices
                    sage: M.graph().is_connected()
                    True
                    sage: M.is_connected()
                    False

                TESTS::

                    sage: TestSuite(M).run(verbose=True)
                    running ._test_category() . . . pass
                    running ._test_new() . . . pass
                    running ._test_not_implemented_methods() . . . pass
                    running ._test_pickling() . . . pass
        """
    @overload
    def __init__(self, G) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 152)

                See the class definition for full documentation.

                EXAMPLES::

                    sage: from sage.matroids.advanced import *
                    sage: G1 = graphs.CycleGraph(3); G2 = graphs.DiamondGraph()
                    sage: G = G1.disjoint_union(G2)
                    sage: M = GraphicMatroid(G); M
                    Graphic matroid of rank 5 on 8 elements
                    sage: M.graph()
                    Looped multi-graph on 6 vertices
                    sage: M.graph().is_connected()
                    True
                    sage: M.is_connected()
                    False

                TESTS::

                    sage: TestSuite(M).run(verbose=True)
                    running ._test_category() . . . pass
                    running ._test_new() . . . pass
                    running ._test_not_implemented_methods() . . . pass
                    running ._test_pickling() . . . pass
        """
    @overload
    def graph(self) -> Any:
        """GraphicMatroid.graph(self)

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 1145)

        Return the graph that represents the matroid.

        The graph will always have loops and multiedges enabled.

        OUTPUT: graph

        EXAMPLES::

            sage: M = Matroid(Graph([(0, 1, 'a'), (0, 2, 'b'), (0, 3, 'c')]))
            sage: M.graph().edges(sort=True)
            [(0, 1, 'a'), (0, 2, 'b'), (0, 3, 'c')]
            sage: M = Matroid(graphs.CompleteGraph(5))
            sage: M.graph()
            Looped multi-graph on 5 vertices"""
    @overload
    def graph(self) -> Any:
        """GraphicMatroid.graph(self)

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 1145)

        Return the graph that represents the matroid.

        The graph will always have loops and multiedges enabled.

        OUTPUT: graph

        EXAMPLES::

            sage: M = Matroid(Graph([(0, 1, 'a'), (0, 2, 'b'), (0, 3, 'c')]))
            sage: M.graph().edges(sort=True)
            [(0, 1, 'a'), (0, 2, 'b'), (0, 3, 'c')]
            sage: M = Matroid(graphs.CompleteGraph(5))
            sage: M.graph()
            Looped multi-graph on 5 vertices"""
    @overload
    def graph(self) -> Any:
        """GraphicMatroid.graph(self)

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 1145)

        Return the graph that represents the matroid.

        The graph will always have loops and multiedges enabled.

        OUTPUT: graph

        EXAMPLES::

            sage: M = Matroid(Graph([(0, 1, 'a'), (0, 2, 'b'), (0, 3, 'c')]))
            sage: M.graph().edges(sort=True)
            [(0, 1, 'a'), (0, 2, 'b'), (0, 3, 'c')]
            sage: M = Matroid(graphs.CompleteGraph(5))
            sage: M.graph()
            Looped multi-graph on 5 vertices"""
    @overload
    def graphic_coextension(self, u, v=..., X=..., element=...) -> Any:
        """GraphicMatroid.graphic_coextension(self, u, v=None, X=None, element=None)

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 1430)

        Return a matroid coextended by a new element.

        A coextension in a graphic matroid is the opposite of contracting an
        edge; that is, a vertex is split, and a new edge is added between the
        resulting vertices. This method will create a new vertex `v` adjacent
        to `u`, and move the edges indicated by `X` from `u` to `v`.

        INPUT:

        - ``u`` -- the vertex to be split
        - ``v`` -- (optional) the name of the new vertex after splitting
        - ``X`` -- (optional) a list of the matroid elements corresponding to
          edges incident to ``u`` that move to the new vertex after splitting
        - ``element`` -- (optional) the name of the newly added element

        OUTPUT:

        An instance of :class:`GraphicMatroid` coextended by the new element.
        If ``X`` is not specified, the new element will be a coloop.

        .. NOTE::

            A loop on ``u`` will stay a loop unless it is in ``X``.

        EXAMPLES::

            sage: G = Graph([(0, 1, 0), (0, 2, 1), (0, 3, 2), (0, 4, 3),
            ....:            (1, 2, 4), (1, 4, 5), (2, 3, 6), (3, 4, 7)])
            sage: M = Matroid(G)
            sage: M1 = M.graphic_coextension(0, X=[1,2], element='a')
            sage: M1.graph().edges(sort=True)
            [(0, 1, 0),
             (0, 4, 3),
             (0, 5, 'a'),
             (1, 2, 4),
             (1, 4, 5),
             (2, 3, 6),
             (2, 5, 1),
             (3, 4, 7),
             (3, 5, 2)]

        TESTS::

            sage: M = Matroid(range(3), graphs.CycleGraph(3))
            sage: M = M.graphic_extension(0, element='a')
            sage: M.graph().edges(sort=True)
            [(0, 0, 'a'), (0, 1, 0), (0, 2, 1), (1, 2, 2)]
            sage: M1 = M.graphic_coextension(0, X=[1], element='b')
            sage: M1.graph().edges(sort=True)
            [(0, 0, 'a'), (0, 1, 0), (0, 3, 'b'), (1, 2, 2), (2, 3, 1)]
            sage: M2 = M.graphic_coextension(0, X=[1, 'a'], element='b')
            sage: M2.graph().edges(sort=True)
            [(0, 1, 0), (0, 3, 'a'), (0, 3, 'b'), (1, 2, 2), (2, 3, 1)]

        ::

            sage: M = Matroid(graphs.CycleGraph(3))
            sage: M = M.graphic_coextension(u=2, element='a')
            sage: M.graph()
            Looped multi-graph on 4 vertices
            sage: M.graph().loops()
            []
            sage: M = M.graphic_coextension(u=2, element='a')
            Traceback (most recent call last):
            ...
            ValueError: cannot extend by element already in groundset
            sage: M = M.graphic_coextension(u=4)
            Traceback (most recent call last):
            ...
            ValueError: u must be an existing vertex

        TESTS::

            sage: M = Matroid(graphs.EmptyGraph())
            sage: M.graphic_coextension(u=0)
            Graphic matroid of rank 1 on 1 elements

            sage: M = Matroid(graphs.DiamondGraph())
            sage: N = M.graphic_coextension(0,'q')
            sage: list(N.graph().vertex_iterator())
            ['q', 0, 1, 2, 3]

        ::

            sage: M = Matroid(range(5), graphs.DiamondGraph())
            sage: N = M.graphic_coextension(u=3, v=5, element='a')
            sage: N.graph().edges(sort=True)
            [(0, 1, 0), (0, 2, 1), (1, 2, 2), (1, 3, 3), (2, 3, 4), (3, 5, 'a')]
            sage: N = M.graphic_coextension(u=3, element='a')
            sage: N.graph().edges(sort=True)
            [(0, 1, 0), (0, 2, 1), (1, 2, 2), (1, 3, 3), (2, 3, 4), (3, 4, 'a')]
            sage: N = M.graphic_coextension(u=3, v=3, element='a')
            Traceback (most recent call last):
            ...
            ValueError: u and v must be distinct"""
    @overload
    def graphic_coextension(self, u=..., element=...) -> Any:
        """GraphicMatroid.graphic_coextension(self, u, v=None, X=None, element=None)

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 1430)

        Return a matroid coextended by a new element.

        A coextension in a graphic matroid is the opposite of contracting an
        edge; that is, a vertex is split, and a new edge is added between the
        resulting vertices. This method will create a new vertex `v` adjacent
        to `u`, and move the edges indicated by `X` from `u` to `v`.

        INPUT:

        - ``u`` -- the vertex to be split
        - ``v`` -- (optional) the name of the new vertex after splitting
        - ``X`` -- (optional) a list of the matroid elements corresponding to
          edges incident to ``u`` that move to the new vertex after splitting
        - ``element`` -- (optional) the name of the newly added element

        OUTPUT:

        An instance of :class:`GraphicMatroid` coextended by the new element.
        If ``X`` is not specified, the new element will be a coloop.

        .. NOTE::

            A loop on ``u`` will stay a loop unless it is in ``X``.

        EXAMPLES::

            sage: G = Graph([(0, 1, 0), (0, 2, 1), (0, 3, 2), (0, 4, 3),
            ....:            (1, 2, 4), (1, 4, 5), (2, 3, 6), (3, 4, 7)])
            sage: M = Matroid(G)
            sage: M1 = M.graphic_coextension(0, X=[1,2], element='a')
            sage: M1.graph().edges(sort=True)
            [(0, 1, 0),
             (0, 4, 3),
             (0, 5, 'a'),
             (1, 2, 4),
             (1, 4, 5),
             (2, 3, 6),
             (2, 5, 1),
             (3, 4, 7),
             (3, 5, 2)]

        TESTS::

            sage: M = Matroid(range(3), graphs.CycleGraph(3))
            sage: M = M.graphic_extension(0, element='a')
            sage: M.graph().edges(sort=True)
            [(0, 0, 'a'), (0, 1, 0), (0, 2, 1), (1, 2, 2)]
            sage: M1 = M.graphic_coextension(0, X=[1], element='b')
            sage: M1.graph().edges(sort=True)
            [(0, 0, 'a'), (0, 1, 0), (0, 3, 'b'), (1, 2, 2), (2, 3, 1)]
            sage: M2 = M.graphic_coextension(0, X=[1, 'a'], element='b')
            sage: M2.graph().edges(sort=True)
            [(0, 1, 0), (0, 3, 'a'), (0, 3, 'b'), (1, 2, 2), (2, 3, 1)]

        ::

            sage: M = Matroid(graphs.CycleGraph(3))
            sage: M = M.graphic_coextension(u=2, element='a')
            sage: M.graph()
            Looped multi-graph on 4 vertices
            sage: M.graph().loops()
            []
            sage: M = M.graphic_coextension(u=2, element='a')
            Traceback (most recent call last):
            ...
            ValueError: cannot extend by element already in groundset
            sage: M = M.graphic_coextension(u=4)
            Traceback (most recent call last):
            ...
            ValueError: u must be an existing vertex

        TESTS::

            sage: M = Matroid(graphs.EmptyGraph())
            sage: M.graphic_coextension(u=0)
            Graphic matroid of rank 1 on 1 elements

            sage: M = Matroid(graphs.DiamondGraph())
            sage: N = M.graphic_coextension(0,'q')
            sage: list(N.graph().vertex_iterator())
            ['q', 0, 1, 2, 3]

        ::

            sage: M = Matroid(range(5), graphs.DiamondGraph())
            sage: N = M.graphic_coextension(u=3, v=5, element='a')
            sage: N.graph().edges(sort=True)
            [(0, 1, 0), (0, 2, 1), (1, 2, 2), (1, 3, 3), (2, 3, 4), (3, 5, 'a')]
            sage: N = M.graphic_coextension(u=3, element='a')
            sage: N.graph().edges(sort=True)
            [(0, 1, 0), (0, 2, 1), (1, 2, 2), (1, 3, 3), (2, 3, 4), (3, 4, 'a')]
            sage: N = M.graphic_coextension(u=3, v=3, element='a')
            Traceback (most recent call last):
            ...
            ValueError: u and v must be distinct"""
    @overload
    def graphic_coextension(self, u=..., element=...) -> Any:
        """GraphicMatroid.graphic_coextension(self, u, v=None, X=None, element=None)

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 1430)

        Return a matroid coextended by a new element.

        A coextension in a graphic matroid is the opposite of contracting an
        edge; that is, a vertex is split, and a new edge is added between the
        resulting vertices. This method will create a new vertex `v` adjacent
        to `u`, and move the edges indicated by `X` from `u` to `v`.

        INPUT:

        - ``u`` -- the vertex to be split
        - ``v`` -- (optional) the name of the new vertex after splitting
        - ``X`` -- (optional) a list of the matroid elements corresponding to
          edges incident to ``u`` that move to the new vertex after splitting
        - ``element`` -- (optional) the name of the newly added element

        OUTPUT:

        An instance of :class:`GraphicMatroid` coextended by the new element.
        If ``X`` is not specified, the new element will be a coloop.

        .. NOTE::

            A loop on ``u`` will stay a loop unless it is in ``X``.

        EXAMPLES::

            sage: G = Graph([(0, 1, 0), (0, 2, 1), (0, 3, 2), (0, 4, 3),
            ....:            (1, 2, 4), (1, 4, 5), (2, 3, 6), (3, 4, 7)])
            sage: M = Matroid(G)
            sage: M1 = M.graphic_coextension(0, X=[1,2], element='a')
            sage: M1.graph().edges(sort=True)
            [(0, 1, 0),
             (0, 4, 3),
             (0, 5, 'a'),
             (1, 2, 4),
             (1, 4, 5),
             (2, 3, 6),
             (2, 5, 1),
             (3, 4, 7),
             (3, 5, 2)]

        TESTS::

            sage: M = Matroid(range(3), graphs.CycleGraph(3))
            sage: M = M.graphic_extension(0, element='a')
            sage: M.graph().edges(sort=True)
            [(0, 0, 'a'), (0, 1, 0), (0, 2, 1), (1, 2, 2)]
            sage: M1 = M.graphic_coextension(0, X=[1], element='b')
            sage: M1.graph().edges(sort=True)
            [(0, 0, 'a'), (0, 1, 0), (0, 3, 'b'), (1, 2, 2), (2, 3, 1)]
            sage: M2 = M.graphic_coextension(0, X=[1, 'a'], element='b')
            sage: M2.graph().edges(sort=True)
            [(0, 1, 0), (0, 3, 'a'), (0, 3, 'b'), (1, 2, 2), (2, 3, 1)]

        ::

            sage: M = Matroid(graphs.CycleGraph(3))
            sage: M = M.graphic_coextension(u=2, element='a')
            sage: M.graph()
            Looped multi-graph on 4 vertices
            sage: M.graph().loops()
            []
            sage: M = M.graphic_coextension(u=2, element='a')
            Traceback (most recent call last):
            ...
            ValueError: cannot extend by element already in groundset
            sage: M = M.graphic_coextension(u=4)
            Traceback (most recent call last):
            ...
            ValueError: u must be an existing vertex

        TESTS::

            sage: M = Matroid(graphs.EmptyGraph())
            sage: M.graphic_coextension(u=0)
            Graphic matroid of rank 1 on 1 elements

            sage: M = Matroid(graphs.DiamondGraph())
            sage: N = M.graphic_coextension(0,'q')
            sage: list(N.graph().vertex_iterator())
            ['q', 0, 1, 2, 3]

        ::

            sage: M = Matroid(range(5), graphs.DiamondGraph())
            sage: N = M.graphic_coextension(u=3, v=5, element='a')
            sage: N.graph().edges(sort=True)
            [(0, 1, 0), (0, 2, 1), (1, 2, 2), (1, 3, 3), (2, 3, 4), (3, 5, 'a')]
            sage: N = M.graphic_coextension(u=3, element='a')
            sage: N.graph().edges(sort=True)
            [(0, 1, 0), (0, 2, 1), (1, 2, 2), (1, 3, 3), (2, 3, 4), (3, 4, 'a')]
            sage: N = M.graphic_coextension(u=3, v=3, element='a')
            Traceback (most recent call last):
            ...
            ValueError: u and v must be distinct"""
    @overload
    def graphic_coextension(self, u=...) -> Any:
        """GraphicMatroid.graphic_coextension(self, u, v=None, X=None, element=None)

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 1430)

        Return a matroid coextended by a new element.

        A coextension in a graphic matroid is the opposite of contracting an
        edge; that is, a vertex is split, and a new edge is added between the
        resulting vertices. This method will create a new vertex `v` adjacent
        to `u`, and move the edges indicated by `X` from `u` to `v`.

        INPUT:

        - ``u`` -- the vertex to be split
        - ``v`` -- (optional) the name of the new vertex after splitting
        - ``X`` -- (optional) a list of the matroid elements corresponding to
          edges incident to ``u`` that move to the new vertex after splitting
        - ``element`` -- (optional) the name of the newly added element

        OUTPUT:

        An instance of :class:`GraphicMatroid` coextended by the new element.
        If ``X`` is not specified, the new element will be a coloop.

        .. NOTE::

            A loop on ``u`` will stay a loop unless it is in ``X``.

        EXAMPLES::

            sage: G = Graph([(0, 1, 0), (0, 2, 1), (0, 3, 2), (0, 4, 3),
            ....:            (1, 2, 4), (1, 4, 5), (2, 3, 6), (3, 4, 7)])
            sage: M = Matroid(G)
            sage: M1 = M.graphic_coextension(0, X=[1,2], element='a')
            sage: M1.graph().edges(sort=True)
            [(0, 1, 0),
             (0, 4, 3),
             (0, 5, 'a'),
             (1, 2, 4),
             (1, 4, 5),
             (2, 3, 6),
             (2, 5, 1),
             (3, 4, 7),
             (3, 5, 2)]

        TESTS::

            sage: M = Matroid(range(3), graphs.CycleGraph(3))
            sage: M = M.graphic_extension(0, element='a')
            sage: M.graph().edges(sort=True)
            [(0, 0, 'a'), (0, 1, 0), (0, 2, 1), (1, 2, 2)]
            sage: M1 = M.graphic_coextension(0, X=[1], element='b')
            sage: M1.graph().edges(sort=True)
            [(0, 0, 'a'), (0, 1, 0), (0, 3, 'b'), (1, 2, 2), (2, 3, 1)]
            sage: M2 = M.graphic_coextension(0, X=[1, 'a'], element='b')
            sage: M2.graph().edges(sort=True)
            [(0, 1, 0), (0, 3, 'a'), (0, 3, 'b'), (1, 2, 2), (2, 3, 1)]

        ::

            sage: M = Matroid(graphs.CycleGraph(3))
            sage: M = M.graphic_coextension(u=2, element='a')
            sage: M.graph()
            Looped multi-graph on 4 vertices
            sage: M.graph().loops()
            []
            sage: M = M.graphic_coextension(u=2, element='a')
            Traceback (most recent call last):
            ...
            ValueError: cannot extend by element already in groundset
            sage: M = M.graphic_coextension(u=4)
            Traceback (most recent call last):
            ...
            ValueError: u must be an existing vertex

        TESTS::

            sage: M = Matroid(graphs.EmptyGraph())
            sage: M.graphic_coextension(u=0)
            Graphic matroid of rank 1 on 1 elements

            sage: M = Matroid(graphs.DiamondGraph())
            sage: N = M.graphic_coextension(0,'q')
            sage: list(N.graph().vertex_iterator())
            ['q', 0, 1, 2, 3]

        ::

            sage: M = Matroid(range(5), graphs.DiamondGraph())
            sage: N = M.graphic_coextension(u=3, v=5, element='a')
            sage: N.graph().edges(sort=True)
            [(0, 1, 0), (0, 2, 1), (1, 2, 2), (1, 3, 3), (2, 3, 4), (3, 5, 'a')]
            sage: N = M.graphic_coextension(u=3, element='a')
            sage: N.graph().edges(sort=True)
            [(0, 1, 0), (0, 2, 1), (1, 2, 2), (1, 3, 3), (2, 3, 4), (3, 4, 'a')]
            sage: N = M.graphic_coextension(u=3, v=3, element='a')
            Traceback (most recent call last):
            ...
            ValueError: u and v must be distinct"""
    @overload
    def graphic_coextension(self, u=...) -> Any:
        """GraphicMatroid.graphic_coextension(self, u, v=None, X=None, element=None)

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 1430)

        Return a matroid coextended by a new element.

        A coextension in a graphic matroid is the opposite of contracting an
        edge; that is, a vertex is split, and a new edge is added between the
        resulting vertices. This method will create a new vertex `v` adjacent
        to `u`, and move the edges indicated by `X` from `u` to `v`.

        INPUT:

        - ``u`` -- the vertex to be split
        - ``v`` -- (optional) the name of the new vertex after splitting
        - ``X`` -- (optional) a list of the matroid elements corresponding to
          edges incident to ``u`` that move to the new vertex after splitting
        - ``element`` -- (optional) the name of the newly added element

        OUTPUT:

        An instance of :class:`GraphicMatroid` coextended by the new element.
        If ``X`` is not specified, the new element will be a coloop.

        .. NOTE::

            A loop on ``u`` will stay a loop unless it is in ``X``.

        EXAMPLES::

            sage: G = Graph([(0, 1, 0), (0, 2, 1), (0, 3, 2), (0, 4, 3),
            ....:            (1, 2, 4), (1, 4, 5), (2, 3, 6), (3, 4, 7)])
            sage: M = Matroid(G)
            sage: M1 = M.graphic_coextension(0, X=[1,2], element='a')
            sage: M1.graph().edges(sort=True)
            [(0, 1, 0),
             (0, 4, 3),
             (0, 5, 'a'),
             (1, 2, 4),
             (1, 4, 5),
             (2, 3, 6),
             (2, 5, 1),
             (3, 4, 7),
             (3, 5, 2)]

        TESTS::

            sage: M = Matroid(range(3), graphs.CycleGraph(3))
            sage: M = M.graphic_extension(0, element='a')
            sage: M.graph().edges(sort=True)
            [(0, 0, 'a'), (0, 1, 0), (0, 2, 1), (1, 2, 2)]
            sage: M1 = M.graphic_coextension(0, X=[1], element='b')
            sage: M1.graph().edges(sort=True)
            [(0, 0, 'a'), (0, 1, 0), (0, 3, 'b'), (1, 2, 2), (2, 3, 1)]
            sage: M2 = M.graphic_coextension(0, X=[1, 'a'], element='b')
            sage: M2.graph().edges(sort=True)
            [(0, 1, 0), (0, 3, 'a'), (0, 3, 'b'), (1, 2, 2), (2, 3, 1)]

        ::

            sage: M = Matroid(graphs.CycleGraph(3))
            sage: M = M.graphic_coextension(u=2, element='a')
            sage: M.graph()
            Looped multi-graph on 4 vertices
            sage: M.graph().loops()
            []
            sage: M = M.graphic_coextension(u=2, element='a')
            Traceback (most recent call last):
            ...
            ValueError: cannot extend by element already in groundset
            sage: M = M.graphic_coextension(u=4)
            Traceback (most recent call last):
            ...
            ValueError: u must be an existing vertex

        TESTS::

            sage: M = Matroid(graphs.EmptyGraph())
            sage: M.graphic_coextension(u=0)
            Graphic matroid of rank 1 on 1 elements

            sage: M = Matroid(graphs.DiamondGraph())
            sage: N = M.graphic_coextension(0,'q')
            sage: list(N.graph().vertex_iterator())
            ['q', 0, 1, 2, 3]

        ::

            sage: M = Matroid(range(5), graphs.DiamondGraph())
            sage: N = M.graphic_coextension(u=3, v=5, element='a')
            sage: N.graph().edges(sort=True)
            [(0, 1, 0), (0, 2, 1), (1, 2, 2), (1, 3, 3), (2, 3, 4), (3, 5, 'a')]
            sage: N = M.graphic_coextension(u=3, element='a')
            sage: N.graph().edges(sort=True)
            [(0, 1, 0), (0, 2, 1), (1, 2, 2), (1, 3, 3), (2, 3, 4), (3, 4, 'a')]
            sage: N = M.graphic_coextension(u=3, v=3, element='a')
            Traceback (most recent call last):
            ...
            ValueError: u and v must be distinct"""
    @overload
    def graphic_coextension(self, u=..., v=..., element=...) -> Any:
        """GraphicMatroid.graphic_coextension(self, u, v=None, X=None, element=None)

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 1430)

        Return a matroid coextended by a new element.

        A coextension in a graphic matroid is the opposite of contracting an
        edge; that is, a vertex is split, and a new edge is added between the
        resulting vertices. This method will create a new vertex `v` adjacent
        to `u`, and move the edges indicated by `X` from `u` to `v`.

        INPUT:

        - ``u`` -- the vertex to be split
        - ``v`` -- (optional) the name of the new vertex after splitting
        - ``X`` -- (optional) a list of the matroid elements corresponding to
          edges incident to ``u`` that move to the new vertex after splitting
        - ``element`` -- (optional) the name of the newly added element

        OUTPUT:

        An instance of :class:`GraphicMatroid` coextended by the new element.
        If ``X`` is not specified, the new element will be a coloop.

        .. NOTE::

            A loop on ``u`` will stay a loop unless it is in ``X``.

        EXAMPLES::

            sage: G = Graph([(0, 1, 0), (0, 2, 1), (0, 3, 2), (0, 4, 3),
            ....:            (1, 2, 4), (1, 4, 5), (2, 3, 6), (3, 4, 7)])
            sage: M = Matroid(G)
            sage: M1 = M.graphic_coextension(0, X=[1,2], element='a')
            sage: M1.graph().edges(sort=True)
            [(0, 1, 0),
             (0, 4, 3),
             (0, 5, 'a'),
             (1, 2, 4),
             (1, 4, 5),
             (2, 3, 6),
             (2, 5, 1),
             (3, 4, 7),
             (3, 5, 2)]

        TESTS::

            sage: M = Matroid(range(3), graphs.CycleGraph(3))
            sage: M = M.graphic_extension(0, element='a')
            sage: M.graph().edges(sort=True)
            [(0, 0, 'a'), (0, 1, 0), (0, 2, 1), (1, 2, 2)]
            sage: M1 = M.graphic_coextension(0, X=[1], element='b')
            sage: M1.graph().edges(sort=True)
            [(0, 0, 'a'), (0, 1, 0), (0, 3, 'b'), (1, 2, 2), (2, 3, 1)]
            sage: M2 = M.graphic_coextension(0, X=[1, 'a'], element='b')
            sage: M2.graph().edges(sort=True)
            [(0, 1, 0), (0, 3, 'a'), (0, 3, 'b'), (1, 2, 2), (2, 3, 1)]

        ::

            sage: M = Matroid(graphs.CycleGraph(3))
            sage: M = M.graphic_coextension(u=2, element='a')
            sage: M.graph()
            Looped multi-graph on 4 vertices
            sage: M.graph().loops()
            []
            sage: M = M.graphic_coextension(u=2, element='a')
            Traceback (most recent call last):
            ...
            ValueError: cannot extend by element already in groundset
            sage: M = M.graphic_coextension(u=4)
            Traceback (most recent call last):
            ...
            ValueError: u must be an existing vertex

        TESTS::

            sage: M = Matroid(graphs.EmptyGraph())
            sage: M.graphic_coextension(u=0)
            Graphic matroid of rank 1 on 1 elements

            sage: M = Matroid(graphs.DiamondGraph())
            sage: N = M.graphic_coextension(0,'q')
            sage: list(N.graph().vertex_iterator())
            ['q', 0, 1, 2, 3]

        ::

            sage: M = Matroid(range(5), graphs.DiamondGraph())
            sage: N = M.graphic_coextension(u=3, v=5, element='a')
            sage: N.graph().edges(sort=True)
            [(0, 1, 0), (0, 2, 1), (1, 2, 2), (1, 3, 3), (2, 3, 4), (3, 5, 'a')]
            sage: N = M.graphic_coextension(u=3, element='a')
            sage: N.graph().edges(sort=True)
            [(0, 1, 0), (0, 2, 1), (1, 2, 2), (1, 3, 3), (2, 3, 4), (3, 4, 'a')]
            sage: N = M.graphic_coextension(u=3, v=3, element='a')
            Traceback (most recent call last):
            ...
            ValueError: u and v must be distinct"""
    @overload
    def graphic_coextension(self, u=..., element=...) -> Any:
        """GraphicMatroid.graphic_coextension(self, u, v=None, X=None, element=None)

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 1430)

        Return a matroid coextended by a new element.

        A coextension in a graphic matroid is the opposite of contracting an
        edge; that is, a vertex is split, and a new edge is added between the
        resulting vertices. This method will create a new vertex `v` adjacent
        to `u`, and move the edges indicated by `X` from `u` to `v`.

        INPUT:

        - ``u`` -- the vertex to be split
        - ``v`` -- (optional) the name of the new vertex after splitting
        - ``X`` -- (optional) a list of the matroid elements corresponding to
          edges incident to ``u`` that move to the new vertex after splitting
        - ``element`` -- (optional) the name of the newly added element

        OUTPUT:

        An instance of :class:`GraphicMatroid` coextended by the new element.
        If ``X`` is not specified, the new element will be a coloop.

        .. NOTE::

            A loop on ``u`` will stay a loop unless it is in ``X``.

        EXAMPLES::

            sage: G = Graph([(0, 1, 0), (0, 2, 1), (0, 3, 2), (0, 4, 3),
            ....:            (1, 2, 4), (1, 4, 5), (2, 3, 6), (3, 4, 7)])
            sage: M = Matroid(G)
            sage: M1 = M.graphic_coextension(0, X=[1,2], element='a')
            sage: M1.graph().edges(sort=True)
            [(0, 1, 0),
             (0, 4, 3),
             (0, 5, 'a'),
             (1, 2, 4),
             (1, 4, 5),
             (2, 3, 6),
             (2, 5, 1),
             (3, 4, 7),
             (3, 5, 2)]

        TESTS::

            sage: M = Matroid(range(3), graphs.CycleGraph(3))
            sage: M = M.graphic_extension(0, element='a')
            sage: M.graph().edges(sort=True)
            [(0, 0, 'a'), (0, 1, 0), (0, 2, 1), (1, 2, 2)]
            sage: M1 = M.graphic_coextension(0, X=[1], element='b')
            sage: M1.graph().edges(sort=True)
            [(0, 0, 'a'), (0, 1, 0), (0, 3, 'b'), (1, 2, 2), (2, 3, 1)]
            sage: M2 = M.graphic_coextension(0, X=[1, 'a'], element='b')
            sage: M2.graph().edges(sort=True)
            [(0, 1, 0), (0, 3, 'a'), (0, 3, 'b'), (1, 2, 2), (2, 3, 1)]

        ::

            sage: M = Matroid(graphs.CycleGraph(3))
            sage: M = M.graphic_coextension(u=2, element='a')
            sage: M.graph()
            Looped multi-graph on 4 vertices
            sage: M.graph().loops()
            []
            sage: M = M.graphic_coextension(u=2, element='a')
            Traceback (most recent call last):
            ...
            ValueError: cannot extend by element already in groundset
            sage: M = M.graphic_coextension(u=4)
            Traceback (most recent call last):
            ...
            ValueError: u must be an existing vertex

        TESTS::

            sage: M = Matroid(graphs.EmptyGraph())
            sage: M.graphic_coextension(u=0)
            Graphic matroid of rank 1 on 1 elements

            sage: M = Matroid(graphs.DiamondGraph())
            sage: N = M.graphic_coextension(0,'q')
            sage: list(N.graph().vertex_iterator())
            ['q', 0, 1, 2, 3]

        ::

            sage: M = Matroid(range(5), graphs.DiamondGraph())
            sage: N = M.graphic_coextension(u=3, v=5, element='a')
            sage: N.graph().edges(sort=True)
            [(0, 1, 0), (0, 2, 1), (1, 2, 2), (1, 3, 3), (2, 3, 4), (3, 5, 'a')]
            sage: N = M.graphic_coextension(u=3, element='a')
            sage: N.graph().edges(sort=True)
            [(0, 1, 0), (0, 2, 1), (1, 2, 2), (1, 3, 3), (2, 3, 4), (3, 4, 'a')]
            sage: N = M.graphic_coextension(u=3, v=3, element='a')
            Traceback (most recent call last):
            ...
            ValueError: u and v must be distinct"""
    @overload
    def graphic_coextension(self, u=..., v=..., element=...) -> Any:
        """GraphicMatroid.graphic_coextension(self, u, v=None, X=None, element=None)

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 1430)

        Return a matroid coextended by a new element.

        A coextension in a graphic matroid is the opposite of contracting an
        edge; that is, a vertex is split, and a new edge is added between the
        resulting vertices. This method will create a new vertex `v` adjacent
        to `u`, and move the edges indicated by `X` from `u` to `v`.

        INPUT:

        - ``u`` -- the vertex to be split
        - ``v`` -- (optional) the name of the new vertex after splitting
        - ``X`` -- (optional) a list of the matroid elements corresponding to
          edges incident to ``u`` that move to the new vertex after splitting
        - ``element`` -- (optional) the name of the newly added element

        OUTPUT:

        An instance of :class:`GraphicMatroid` coextended by the new element.
        If ``X`` is not specified, the new element will be a coloop.

        .. NOTE::

            A loop on ``u`` will stay a loop unless it is in ``X``.

        EXAMPLES::

            sage: G = Graph([(0, 1, 0), (0, 2, 1), (0, 3, 2), (0, 4, 3),
            ....:            (1, 2, 4), (1, 4, 5), (2, 3, 6), (3, 4, 7)])
            sage: M = Matroid(G)
            sage: M1 = M.graphic_coextension(0, X=[1,2], element='a')
            sage: M1.graph().edges(sort=True)
            [(0, 1, 0),
             (0, 4, 3),
             (0, 5, 'a'),
             (1, 2, 4),
             (1, 4, 5),
             (2, 3, 6),
             (2, 5, 1),
             (3, 4, 7),
             (3, 5, 2)]

        TESTS::

            sage: M = Matroid(range(3), graphs.CycleGraph(3))
            sage: M = M.graphic_extension(0, element='a')
            sage: M.graph().edges(sort=True)
            [(0, 0, 'a'), (0, 1, 0), (0, 2, 1), (1, 2, 2)]
            sage: M1 = M.graphic_coextension(0, X=[1], element='b')
            sage: M1.graph().edges(sort=True)
            [(0, 0, 'a'), (0, 1, 0), (0, 3, 'b'), (1, 2, 2), (2, 3, 1)]
            sage: M2 = M.graphic_coextension(0, X=[1, 'a'], element='b')
            sage: M2.graph().edges(sort=True)
            [(0, 1, 0), (0, 3, 'a'), (0, 3, 'b'), (1, 2, 2), (2, 3, 1)]

        ::

            sage: M = Matroid(graphs.CycleGraph(3))
            sage: M = M.graphic_coextension(u=2, element='a')
            sage: M.graph()
            Looped multi-graph on 4 vertices
            sage: M.graph().loops()
            []
            sage: M = M.graphic_coextension(u=2, element='a')
            Traceback (most recent call last):
            ...
            ValueError: cannot extend by element already in groundset
            sage: M = M.graphic_coextension(u=4)
            Traceback (most recent call last):
            ...
            ValueError: u must be an existing vertex

        TESTS::

            sage: M = Matroid(graphs.EmptyGraph())
            sage: M.graphic_coextension(u=0)
            Graphic matroid of rank 1 on 1 elements

            sage: M = Matroid(graphs.DiamondGraph())
            sage: N = M.graphic_coextension(0,'q')
            sage: list(N.graph().vertex_iterator())
            ['q', 0, 1, 2, 3]

        ::

            sage: M = Matroid(range(5), graphs.DiamondGraph())
            sage: N = M.graphic_coextension(u=3, v=5, element='a')
            sage: N.graph().edges(sort=True)
            [(0, 1, 0), (0, 2, 1), (1, 2, 2), (1, 3, 3), (2, 3, 4), (3, 5, 'a')]
            sage: N = M.graphic_coextension(u=3, element='a')
            sage: N.graph().edges(sort=True)
            [(0, 1, 0), (0, 2, 1), (1, 2, 2), (1, 3, 3), (2, 3, 4), (3, 4, 'a')]
            sage: N = M.graphic_coextension(u=3, v=3, element='a')
            Traceback (most recent call last):
            ...
            ValueError: u and v must be distinct"""
    @overload
    def graphic_coextensions(self, vertices=..., v=..., element=..., cosimple=...) -> Any:
        """GraphicMatroid.graphic_coextensions(self, vertices=None, v=None, element=None, cosimple=False)

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 1560)

        Return an iterator of graphic coextensions.

        This method iterates over the vertices in the input. If
        ``cosimple == False``, it first coextends by a coloop and series edge
        for every edge incident with the vertices. For vertices of degree four
        or higher, it will consider the ways to partition the vertex into two
        sets of cardinality at least two, and these will be the edges incident
        with the vertices after splitting.

        At most one series coextension will be taken for each series class.

        INPUT:

        - ``vertices`` -- (optional) the vertices to be split
        - ``v`` -- (optional) the name of the new vertex
        - ``element`` -- (optional) the name of the new element
        - ``cosimple`` -- boolean (default: ``False``); if ``True``, coextensions
          by a coloop or series elements will not be taken

        OUTPUT:

        An iterable containing instances of :class:`GraphicMatroid`. If
        ``vertices`` is not specified, the method iterates over all vertices.

        EXAMPLES::

            sage: G = Graph([(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 4), (2, 3), (3, 4)])
            sage: M = Matroid(range(8), G)
            sage: I = M.graphic_coextensions(vertices=[0], element='a')
            sage: sorted([N.graph().edges_incident(0, sort=True) for N in I], key=str)
            [[(0, 1, 0), (0, 2, 1), (0, 3, 2), (0, 4, 3), (0, 5, 'a')],
             [(0, 1, 0), (0, 2, 1), (0, 3, 2), (0, 5, 'a')],
             [(0, 1, 0), (0, 2, 1), (0, 4, 3), (0, 5, 'a')],
             [(0, 1, 0), (0, 2, 1), (0, 5, 'a')],
             [(0, 1, 0), (0, 3, 2), (0, 4, 3), (0, 5, 'a')],
             [(0, 1, 0), (0, 3, 2), (0, 5, 'a')],
             [(0, 2, 1), (0, 3, 2), (0, 4, 3), (0, 5, 'a')],
             [(0, 2, 1), (0, 3, 2), (0, 5, 'a')]]

        ::

            sage: N = Matroid(range(4), graphs.CycleGraph(4))
            sage: I = N.graphic_coextensions(element='a')
            sage: for N1 in I:  # random
            ....:     N1.graph().edges(sort=True)
            [(0, 1, 0), (0, 3, 1), (0, 4, 'a'), (1, 2, 2), (2, 3, 3)]
            [(0, 1, 0), (0, 3, 1), (1, 4, 2), (2, 3, 3), (2, 4, 'a')]
            sage: sum(1 for n in N.graphic_coextensions(cosimple=True))
            0

        TESTS::

            sage: M = Matroid(graphs.EmptyGraph())
            sage: M.graphic_coextension(0)
            Graphic matroid of rank 1 on 1 elements
            sage: I = M.graphic_coextensions(element='a')
            sage: for m in I:
            ....:     m.graph().edges(sort=True)
            [(0, 1, 'a')]
            sage: N = Matroid(graphs.CycleGraph(4))
            sage: I = N.graphic_coextensions(vertices=[3, 4], element='a')
            sage: next(I)
            Traceback (most recent call last):
            ...
            ValueError: vertices are not all in the graph

        We expect 136 graphic coextensions of an 8-spoked wheel: 128 extensions
        from the center vertex because there are (256/2) ways to put the 8
        center edges into 2 sets, and then 8 more for series extensions of the
        rims::

            sage: M = Matroid(graphs.WheelGraph(9))
            sage: I = M.graphic_coextensions()
            sage: sum(1 for N in I)
            136
            sage: I = M.graphic_coextensions(cosimple=True)
            sage: sum(1 for N in I)
            119
            sage: sum(1 for N in Matroid(graphs.WheelGraph(8)).graphic_coextensions())
            71

        This graph has max degree 3, so the only series extensions should be
        non-cosimple, ie. a coloop and one for every coseries class.
        12 total::

            sage: edgedict = {0: [1, 2, 3], 1: [2, 4], 2: [3], 3: [6],
            ....:             4: [5, 7], 5: [6, 7], 6: [7]}
            sage: M = Matroid(range(12), Graph(edgedict))
            sage: sorted(M.coclosure([4]))
            [4, 6]
            sage: sum(1 for N in M.graphic_coextensions())
            12
            sage: sum(1 for N in M.graphic_coextensions(cosimple=True))
            0"""
    @overload
    def graphic_coextensions(self, vertices=..., element=...) -> Any:
        """GraphicMatroid.graphic_coextensions(self, vertices=None, v=None, element=None, cosimple=False)

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 1560)

        Return an iterator of graphic coextensions.

        This method iterates over the vertices in the input. If
        ``cosimple == False``, it first coextends by a coloop and series edge
        for every edge incident with the vertices. For vertices of degree four
        or higher, it will consider the ways to partition the vertex into two
        sets of cardinality at least two, and these will be the edges incident
        with the vertices after splitting.

        At most one series coextension will be taken for each series class.

        INPUT:

        - ``vertices`` -- (optional) the vertices to be split
        - ``v`` -- (optional) the name of the new vertex
        - ``element`` -- (optional) the name of the new element
        - ``cosimple`` -- boolean (default: ``False``); if ``True``, coextensions
          by a coloop or series elements will not be taken

        OUTPUT:

        An iterable containing instances of :class:`GraphicMatroid`. If
        ``vertices`` is not specified, the method iterates over all vertices.

        EXAMPLES::

            sage: G = Graph([(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 4), (2, 3), (3, 4)])
            sage: M = Matroid(range(8), G)
            sage: I = M.graphic_coextensions(vertices=[0], element='a')
            sage: sorted([N.graph().edges_incident(0, sort=True) for N in I], key=str)
            [[(0, 1, 0), (0, 2, 1), (0, 3, 2), (0, 4, 3), (0, 5, 'a')],
             [(0, 1, 0), (0, 2, 1), (0, 3, 2), (0, 5, 'a')],
             [(0, 1, 0), (0, 2, 1), (0, 4, 3), (0, 5, 'a')],
             [(0, 1, 0), (0, 2, 1), (0, 5, 'a')],
             [(0, 1, 0), (0, 3, 2), (0, 4, 3), (0, 5, 'a')],
             [(0, 1, 0), (0, 3, 2), (0, 5, 'a')],
             [(0, 2, 1), (0, 3, 2), (0, 4, 3), (0, 5, 'a')],
             [(0, 2, 1), (0, 3, 2), (0, 5, 'a')]]

        ::

            sage: N = Matroid(range(4), graphs.CycleGraph(4))
            sage: I = N.graphic_coextensions(element='a')
            sage: for N1 in I:  # random
            ....:     N1.graph().edges(sort=True)
            [(0, 1, 0), (0, 3, 1), (0, 4, 'a'), (1, 2, 2), (2, 3, 3)]
            [(0, 1, 0), (0, 3, 1), (1, 4, 2), (2, 3, 3), (2, 4, 'a')]
            sage: sum(1 for n in N.graphic_coextensions(cosimple=True))
            0

        TESTS::

            sage: M = Matroid(graphs.EmptyGraph())
            sage: M.graphic_coextension(0)
            Graphic matroid of rank 1 on 1 elements
            sage: I = M.graphic_coextensions(element='a')
            sage: for m in I:
            ....:     m.graph().edges(sort=True)
            [(0, 1, 'a')]
            sage: N = Matroid(graphs.CycleGraph(4))
            sage: I = N.graphic_coextensions(vertices=[3, 4], element='a')
            sage: next(I)
            Traceback (most recent call last):
            ...
            ValueError: vertices are not all in the graph

        We expect 136 graphic coextensions of an 8-spoked wheel: 128 extensions
        from the center vertex because there are (256/2) ways to put the 8
        center edges into 2 sets, and then 8 more for series extensions of the
        rims::

            sage: M = Matroid(graphs.WheelGraph(9))
            sage: I = M.graphic_coextensions()
            sage: sum(1 for N in I)
            136
            sage: I = M.graphic_coextensions(cosimple=True)
            sage: sum(1 for N in I)
            119
            sage: sum(1 for N in Matroid(graphs.WheelGraph(8)).graphic_coextensions())
            71

        This graph has max degree 3, so the only series extensions should be
        non-cosimple, ie. a coloop and one for every coseries class.
        12 total::

            sage: edgedict = {0: [1, 2, 3], 1: [2, 4], 2: [3], 3: [6],
            ....:             4: [5, 7], 5: [6, 7], 6: [7]}
            sage: M = Matroid(range(12), Graph(edgedict))
            sage: sorted(M.coclosure([4]))
            [4, 6]
            sage: sum(1 for N in M.graphic_coextensions())
            12
            sage: sum(1 for N in M.graphic_coextensions(cosimple=True))
            0"""
    @overload
    def graphic_coextensions(self, element=...) -> Any:
        """GraphicMatroid.graphic_coextensions(self, vertices=None, v=None, element=None, cosimple=False)

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 1560)

        Return an iterator of graphic coextensions.

        This method iterates over the vertices in the input. If
        ``cosimple == False``, it first coextends by a coloop and series edge
        for every edge incident with the vertices. For vertices of degree four
        or higher, it will consider the ways to partition the vertex into two
        sets of cardinality at least two, and these will be the edges incident
        with the vertices after splitting.

        At most one series coextension will be taken for each series class.

        INPUT:

        - ``vertices`` -- (optional) the vertices to be split
        - ``v`` -- (optional) the name of the new vertex
        - ``element`` -- (optional) the name of the new element
        - ``cosimple`` -- boolean (default: ``False``); if ``True``, coextensions
          by a coloop or series elements will not be taken

        OUTPUT:

        An iterable containing instances of :class:`GraphicMatroid`. If
        ``vertices`` is not specified, the method iterates over all vertices.

        EXAMPLES::

            sage: G = Graph([(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 4), (2, 3), (3, 4)])
            sage: M = Matroid(range(8), G)
            sage: I = M.graphic_coextensions(vertices=[0], element='a')
            sage: sorted([N.graph().edges_incident(0, sort=True) for N in I], key=str)
            [[(0, 1, 0), (0, 2, 1), (0, 3, 2), (0, 4, 3), (0, 5, 'a')],
             [(0, 1, 0), (0, 2, 1), (0, 3, 2), (0, 5, 'a')],
             [(0, 1, 0), (0, 2, 1), (0, 4, 3), (0, 5, 'a')],
             [(0, 1, 0), (0, 2, 1), (0, 5, 'a')],
             [(0, 1, 0), (0, 3, 2), (0, 4, 3), (0, 5, 'a')],
             [(0, 1, 0), (0, 3, 2), (0, 5, 'a')],
             [(0, 2, 1), (0, 3, 2), (0, 4, 3), (0, 5, 'a')],
             [(0, 2, 1), (0, 3, 2), (0, 5, 'a')]]

        ::

            sage: N = Matroid(range(4), graphs.CycleGraph(4))
            sage: I = N.graphic_coextensions(element='a')
            sage: for N1 in I:  # random
            ....:     N1.graph().edges(sort=True)
            [(0, 1, 0), (0, 3, 1), (0, 4, 'a'), (1, 2, 2), (2, 3, 3)]
            [(0, 1, 0), (0, 3, 1), (1, 4, 2), (2, 3, 3), (2, 4, 'a')]
            sage: sum(1 for n in N.graphic_coextensions(cosimple=True))
            0

        TESTS::

            sage: M = Matroid(graphs.EmptyGraph())
            sage: M.graphic_coextension(0)
            Graphic matroid of rank 1 on 1 elements
            sage: I = M.graphic_coextensions(element='a')
            sage: for m in I:
            ....:     m.graph().edges(sort=True)
            [(0, 1, 'a')]
            sage: N = Matroid(graphs.CycleGraph(4))
            sage: I = N.graphic_coextensions(vertices=[3, 4], element='a')
            sage: next(I)
            Traceback (most recent call last):
            ...
            ValueError: vertices are not all in the graph

        We expect 136 graphic coextensions of an 8-spoked wheel: 128 extensions
        from the center vertex because there are (256/2) ways to put the 8
        center edges into 2 sets, and then 8 more for series extensions of the
        rims::

            sage: M = Matroid(graphs.WheelGraph(9))
            sage: I = M.graphic_coextensions()
            sage: sum(1 for N in I)
            136
            sage: I = M.graphic_coextensions(cosimple=True)
            sage: sum(1 for N in I)
            119
            sage: sum(1 for N in Matroid(graphs.WheelGraph(8)).graphic_coextensions())
            71

        This graph has max degree 3, so the only series extensions should be
        non-cosimple, ie. a coloop and one for every coseries class.
        12 total::

            sage: edgedict = {0: [1, 2, 3], 1: [2, 4], 2: [3], 3: [6],
            ....:             4: [5, 7], 5: [6, 7], 6: [7]}
            sage: M = Matroid(range(12), Graph(edgedict))
            sage: sorted(M.coclosure([4]))
            [4, 6]
            sage: sum(1 for N in M.graphic_coextensions())
            12
            sage: sum(1 for N in M.graphic_coextensions(cosimple=True))
            0"""
    @overload
    def graphic_coextensions(self, cosimple=...) -> Any:
        """GraphicMatroid.graphic_coextensions(self, vertices=None, v=None, element=None, cosimple=False)

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 1560)

        Return an iterator of graphic coextensions.

        This method iterates over the vertices in the input. If
        ``cosimple == False``, it first coextends by a coloop and series edge
        for every edge incident with the vertices. For vertices of degree four
        or higher, it will consider the ways to partition the vertex into two
        sets of cardinality at least two, and these will be the edges incident
        with the vertices after splitting.

        At most one series coextension will be taken for each series class.

        INPUT:

        - ``vertices`` -- (optional) the vertices to be split
        - ``v`` -- (optional) the name of the new vertex
        - ``element`` -- (optional) the name of the new element
        - ``cosimple`` -- boolean (default: ``False``); if ``True``, coextensions
          by a coloop or series elements will not be taken

        OUTPUT:

        An iterable containing instances of :class:`GraphicMatroid`. If
        ``vertices`` is not specified, the method iterates over all vertices.

        EXAMPLES::

            sage: G = Graph([(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 4), (2, 3), (3, 4)])
            sage: M = Matroid(range(8), G)
            sage: I = M.graphic_coextensions(vertices=[0], element='a')
            sage: sorted([N.graph().edges_incident(0, sort=True) for N in I], key=str)
            [[(0, 1, 0), (0, 2, 1), (0, 3, 2), (0, 4, 3), (0, 5, 'a')],
             [(0, 1, 0), (0, 2, 1), (0, 3, 2), (0, 5, 'a')],
             [(0, 1, 0), (0, 2, 1), (0, 4, 3), (0, 5, 'a')],
             [(0, 1, 0), (0, 2, 1), (0, 5, 'a')],
             [(0, 1, 0), (0, 3, 2), (0, 4, 3), (0, 5, 'a')],
             [(0, 1, 0), (0, 3, 2), (0, 5, 'a')],
             [(0, 2, 1), (0, 3, 2), (0, 4, 3), (0, 5, 'a')],
             [(0, 2, 1), (0, 3, 2), (0, 5, 'a')]]

        ::

            sage: N = Matroid(range(4), graphs.CycleGraph(4))
            sage: I = N.graphic_coextensions(element='a')
            sage: for N1 in I:  # random
            ....:     N1.graph().edges(sort=True)
            [(0, 1, 0), (0, 3, 1), (0, 4, 'a'), (1, 2, 2), (2, 3, 3)]
            [(0, 1, 0), (0, 3, 1), (1, 4, 2), (2, 3, 3), (2, 4, 'a')]
            sage: sum(1 for n in N.graphic_coextensions(cosimple=True))
            0

        TESTS::

            sage: M = Matroid(graphs.EmptyGraph())
            sage: M.graphic_coextension(0)
            Graphic matroid of rank 1 on 1 elements
            sage: I = M.graphic_coextensions(element='a')
            sage: for m in I:
            ....:     m.graph().edges(sort=True)
            [(0, 1, 'a')]
            sage: N = Matroid(graphs.CycleGraph(4))
            sage: I = N.graphic_coextensions(vertices=[3, 4], element='a')
            sage: next(I)
            Traceback (most recent call last):
            ...
            ValueError: vertices are not all in the graph

        We expect 136 graphic coextensions of an 8-spoked wheel: 128 extensions
        from the center vertex because there are (256/2) ways to put the 8
        center edges into 2 sets, and then 8 more for series extensions of the
        rims::

            sage: M = Matroid(graphs.WheelGraph(9))
            sage: I = M.graphic_coextensions()
            sage: sum(1 for N in I)
            136
            sage: I = M.graphic_coextensions(cosimple=True)
            sage: sum(1 for N in I)
            119
            sage: sum(1 for N in Matroid(graphs.WheelGraph(8)).graphic_coextensions())
            71

        This graph has max degree 3, so the only series extensions should be
        non-cosimple, ie. a coloop and one for every coseries class.
        12 total::

            sage: edgedict = {0: [1, 2, 3], 1: [2, 4], 2: [3], 3: [6],
            ....:             4: [5, 7], 5: [6, 7], 6: [7]}
            sage: M = Matroid(range(12), Graph(edgedict))
            sage: sorted(M.coclosure([4]))
            [4, 6]
            sage: sum(1 for N in M.graphic_coextensions())
            12
            sage: sum(1 for N in M.graphic_coextensions(cosimple=True))
            0"""
    @overload
    def graphic_coextensions(self, element=...) -> Any:
        """GraphicMatroid.graphic_coextensions(self, vertices=None, v=None, element=None, cosimple=False)

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 1560)

        Return an iterator of graphic coextensions.

        This method iterates over the vertices in the input. If
        ``cosimple == False``, it first coextends by a coloop and series edge
        for every edge incident with the vertices. For vertices of degree four
        or higher, it will consider the ways to partition the vertex into two
        sets of cardinality at least two, and these will be the edges incident
        with the vertices after splitting.

        At most one series coextension will be taken for each series class.

        INPUT:

        - ``vertices`` -- (optional) the vertices to be split
        - ``v`` -- (optional) the name of the new vertex
        - ``element`` -- (optional) the name of the new element
        - ``cosimple`` -- boolean (default: ``False``); if ``True``, coextensions
          by a coloop or series elements will not be taken

        OUTPUT:

        An iterable containing instances of :class:`GraphicMatroid`. If
        ``vertices`` is not specified, the method iterates over all vertices.

        EXAMPLES::

            sage: G = Graph([(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 4), (2, 3), (3, 4)])
            sage: M = Matroid(range(8), G)
            sage: I = M.graphic_coextensions(vertices=[0], element='a')
            sage: sorted([N.graph().edges_incident(0, sort=True) for N in I], key=str)
            [[(0, 1, 0), (0, 2, 1), (0, 3, 2), (0, 4, 3), (0, 5, 'a')],
             [(0, 1, 0), (0, 2, 1), (0, 3, 2), (0, 5, 'a')],
             [(0, 1, 0), (0, 2, 1), (0, 4, 3), (0, 5, 'a')],
             [(0, 1, 0), (0, 2, 1), (0, 5, 'a')],
             [(0, 1, 0), (0, 3, 2), (0, 4, 3), (0, 5, 'a')],
             [(0, 1, 0), (0, 3, 2), (0, 5, 'a')],
             [(0, 2, 1), (0, 3, 2), (0, 4, 3), (0, 5, 'a')],
             [(0, 2, 1), (0, 3, 2), (0, 5, 'a')]]

        ::

            sage: N = Matroid(range(4), graphs.CycleGraph(4))
            sage: I = N.graphic_coextensions(element='a')
            sage: for N1 in I:  # random
            ....:     N1.graph().edges(sort=True)
            [(0, 1, 0), (0, 3, 1), (0, 4, 'a'), (1, 2, 2), (2, 3, 3)]
            [(0, 1, 0), (0, 3, 1), (1, 4, 2), (2, 3, 3), (2, 4, 'a')]
            sage: sum(1 for n in N.graphic_coextensions(cosimple=True))
            0

        TESTS::

            sage: M = Matroid(graphs.EmptyGraph())
            sage: M.graphic_coextension(0)
            Graphic matroid of rank 1 on 1 elements
            sage: I = M.graphic_coextensions(element='a')
            sage: for m in I:
            ....:     m.graph().edges(sort=True)
            [(0, 1, 'a')]
            sage: N = Matroid(graphs.CycleGraph(4))
            sage: I = N.graphic_coextensions(vertices=[3, 4], element='a')
            sage: next(I)
            Traceback (most recent call last):
            ...
            ValueError: vertices are not all in the graph

        We expect 136 graphic coextensions of an 8-spoked wheel: 128 extensions
        from the center vertex because there are (256/2) ways to put the 8
        center edges into 2 sets, and then 8 more for series extensions of the
        rims::

            sage: M = Matroid(graphs.WheelGraph(9))
            sage: I = M.graphic_coextensions()
            sage: sum(1 for N in I)
            136
            sage: I = M.graphic_coextensions(cosimple=True)
            sage: sum(1 for N in I)
            119
            sage: sum(1 for N in Matroid(graphs.WheelGraph(8)).graphic_coextensions())
            71

        This graph has max degree 3, so the only series extensions should be
        non-cosimple, ie. a coloop and one for every coseries class.
        12 total::

            sage: edgedict = {0: [1, 2, 3], 1: [2, 4], 2: [3], 3: [6],
            ....:             4: [5, 7], 5: [6, 7], 6: [7]}
            sage: M = Matroid(range(12), Graph(edgedict))
            sage: sorted(M.coclosure([4]))
            [4, 6]
            sage: sum(1 for N in M.graphic_coextensions())
            12
            sage: sum(1 for N in M.graphic_coextensions(cosimple=True))
            0"""
    @overload
    def graphic_coextensions(self, vertices=..., element=...) -> Any:
        """GraphicMatroid.graphic_coextensions(self, vertices=None, v=None, element=None, cosimple=False)

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 1560)

        Return an iterator of graphic coextensions.

        This method iterates over the vertices in the input. If
        ``cosimple == False``, it first coextends by a coloop and series edge
        for every edge incident with the vertices. For vertices of degree four
        or higher, it will consider the ways to partition the vertex into two
        sets of cardinality at least two, and these will be the edges incident
        with the vertices after splitting.

        At most one series coextension will be taken for each series class.

        INPUT:

        - ``vertices`` -- (optional) the vertices to be split
        - ``v`` -- (optional) the name of the new vertex
        - ``element`` -- (optional) the name of the new element
        - ``cosimple`` -- boolean (default: ``False``); if ``True``, coextensions
          by a coloop or series elements will not be taken

        OUTPUT:

        An iterable containing instances of :class:`GraphicMatroid`. If
        ``vertices`` is not specified, the method iterates over all vertices.

        EXAMPLES::

            sage: G = Graph([(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 4), (2, 3), (3, 4)])
            sage: M = Matroid(range(8), G)
            sage: I = M.graphic_coextensions(vertices=[0], element='a')
            sage: sorted([N.graph().edges_incident(0, sort=True) for N in I], key=str)
            [[(0, 1, 0), (0, 2, 1), (0, 3, 2), (0, 4, 3), (0, 5, 'a')],
             [(0, 1, 0), (0, 2, 1), (0, 3, 2), (0, 5, 'a')],
             [(0, 1, 0), (0, 2, 1), (0, 4, 3), (0, 5, 'a')],
             [(0, 1, 0), (0, 2, 1), (0, 5, 'a')],
             [(0, 1, 0), (0, 3, 2), (0, 4, 3), (0, 5, 'a')],
             [(0, 1, 0), (0, 3, 2), (0, 5, 'a')],
             [(0, 2, 1), (0, 3, 2), (0, 4, 3), (0, 5, 'a')],
             [(0, 2, 1), (0, 3, 2), (0, 5, 'a')]]

        ::

            sage: N = Matroid(range(4), graphs.CycleGraph(4))
            sage: I = N.graphic_coextensions(element='a')
            sage: for N1 in I:  # random
            ....:     N1.graph().edges(sort=True)
            [(0, 1, 0), (0, 3, 1), (0, 4, 'a'), (1, 2, 2), (2, 3, 3)]
            [(0, 1, 0), (0, 3, 1), (1, 4, 2), (2, 3, 3), (2, 4, 'a')]
            sage: sum(1 for n in N.graphic_coextensions(cosimple=True))
            0

        TESTS::

            sage: M = Matroid(graphs.EmptyGraph())
            sage: M.graphic_coextension(0)
            Graphic matroid of rank 1 on 1 elements
            sage: I = M.graphic_coextensions(element='a')
            sage: for m in I:
            ....:     m.graph().edges(sort=True)
            [(0, 1, 'a')]
            sage: N = Matroid(graphs.CycleGraph(4))
            sage: I = N.graphic_coextensions(vertices=[3, 4], element='a')
            sage: next(I)
            Traceback (most recent call last):
            ...
            ValueError: vertices are not all in the graph

        We expect 136 graphic coextensions of an 8-spoked wheel: 128 extensions
        from the center vertex because there are (256/2) ways to put the 8
        center edges into 2 sets, and then 8 more for series extensions of the
        rims::

            sage: M = Matroid(graphs.WheelGraph(9))
            sage: I = M.graphic_coextensions()
            sage: sum(1 for N in I)
            136
            sage: I = M.graphic_coextensions(cosimple=True)
            sage: sum(1 for N in I)
            119
            sage: sum(1 for N in Matroid(graphs.WheelGraph(8)).graphic_coextensions())
            71

        This graph has max degree 3, so the only series extensions should be
        non-cosimple, ie. a coloop and one for every coseries class.
        12 total::

            sage: edgedict = {0: [1, 2, 3], 1: [2, 4], 2: [3], 3: [6],
            ....:             4: [5, 7], 5: [6, 7], 6: [7]}
            sage: M = Matroid(range(12), Graph(edgedict))
            sage: sorted(M.coclosure([4]))
            [4, 6]
            sage: sum(1 for N in M.graphic_coextensions())
            12
            sage: sum(1 for N in M.graphic_coextensions(cosimple=True))
            0"""
    @overload
    def graphic_coextensions(self) -> Any:
        """GraphicMatroid.graphic_coextensions(self, vertices=None, v=None, element=None, cosimple=False)

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 1560)

        Return an iterator of graphic coextensions.

        This method iterates over the vertices in the input. If
        ``cosimple == False``, it first coextends by a coloop and series edge
        for every edge incident with the vertices. For vertices of degree four
        or higher, it will consider the ways to partition the vertex into two
        sets of cardinality at least two, and these will be the edges incident
        with the vertices after splitting.

        At most one series coextension will be taken for each series class.

        INPUT:

        - ``vertices`` -- (optional) the vertices to be split
        - ``v`` -- (optional) the name of the new vertex
        - ``element`` -- (optional) the name of the new element
        - ``cosimple`` -- boolean (default: ``False``); if ``True``, coextensions
          by a coloop or series elements will not be taken

        OUTPUT:

        An iterable containing instances of :class:`GraphicMatroid`. If
        ``vertices`` is not specified, the method iterates over all vertices.

        EXAMPLES::

            sage: G = Graph([(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 4), (2, 3), (3, 4)])
            sage: M = Matroid(range(8), G)
            sage: I = M.graphic_coextensions(vertices=[0], element='a')
            sage: sorted([N.graph().edges_incident(0, sort=True) for N in I], key=str)
            [[(0, 1, 0), (0, 2, 1), (0, 3, 2), (0, 4, 3), (0, 5, 'a')],
             [(0, 1, 0), (0, 2, 1), (0, 3, 2), (0, 5, 'a')],
             [(0, 1, 0), (0, 2, 1), (0, 4, 3), (0, 5, 'a')],
             [(0, 1, 0), (0, 2, 1), (0, 5, 'a')],
             [(0, 1, 0), (0, 3, 2), (0, 4, 3), (0, 5, 'a')],
             [(0, 1, 0), (0, 3, 2), (0, 5, 'a')],
             [(0, 2, 1), (0, 3, 2), (0, 4, 3), (0, 5, 'a')],
             [(0, 2, 1), (0, 3, 2), (0, 5, 'a')]]

        ::

            sage: N = Matroid(range(4), graphs.CycleGraph(4))
            sage: I = N.graphic_coextensions(element='a')
            sage: for N1 in I:  # random
            ....:     N1.graph().edges(sort=True)
            [(0, 1, 0), (0, 3, 1), (0, 4, 'a'), (1, 2, 2), (2, 3, 3)]
            [(0, 1, 0), (0, 3, 1), (1, 4, 2), (2, 3, 3), (2, 4, 'a')]
            sage: sum(1 for n in N.graphic_coextensions(cosimple=True))
            0

        TESTS::

            sage: M = Matroid(graphs.EmptyGraph())
            sage: M.graphic_coextension(0)
            Graphic matroid of rank 1 on 1 elements
            sage: I = M.graphic_coextensions(element='a')
            sage: for m in I:
            ....:     m.graph().edges(sort=True)
            [(0, 1, 'a')]
            sage: N = Matroid(graphs.CycleGraph(4))
            sage: I = N.graphic_coextensions(vertices=[3, 4], element='a')
            sage: next(I)
            Traceback (most recent call last):
            ...
            ValueError: vertices are not all in the graph

        We expect 136 graphic coextensions of an 8-spoked wheel: 128 extensions
        from the center vertex because there are (256/2) ways to put the 8
        center edges into 2 sets, and then 8 more for series extensions of the
        rims::

            sage: M = Matroid(graphs.WheelGraph(9))
            sage: I = M.graphic_coextensions()
            sage: sum(1 for N in I)
            136
            sage: I = M.graphic_coextensions(cosimple=True)
            sage: sum(1 for N in I)
            119
            sage: sum(1 for N in Matroid(graphs.WheelGraph(8)).graphic_coextensions())
            71

        This graph has max degree 3, so the only series extensions should be
        non-cosimple, ie. a coloop and one for every coseries class.
        12 total::

            sage: edgedict = {0: [1, 2, 3], 1: [2, 4], 2: [3], 3: [6],
            ....:             4: [5, 7], 5: [6, 7], 6: [7]}
            sage: M = Matroid(range(12), Graph(edgedict))
            sage: sorted(M.coclosure([4]))
            [4, 6]
            sage: sum(1 for N in M.graphic_coextensions())
            12
            sage: sum(1 for N in M.graphic_coextensions(cosimple=True))
            0"""
    @overload
    def graphic_coextensions(self, cosimple=...) -> Any:
        """GraphicMatroid.graphic_coextensions(self, vertices=None, v=None, element=None, cosimple=False)

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 1560)

        Return an iterator of graphic coextensions.

        This method iterates over the vertices in the input. If
        ``cosimple == False``, it first coextends by a coloop and series edge
        for every edge incident with the vertices. For vertices of degree four
        or higher, it will consider the ways to partition the vertex into two
        sets of cardinality at least two, and these will be the edges incident
        with the vertices after splitting.

        At most one series coextension will be taken for each series class.

        INPUT:

        - ``vertices`` -- (optional) the vertices to be split
        - ``v`` -- (optional) the name of the new vertex
        - ``element`` -- (optional) the name of the new element
        - ``cosimple`` -- boolean (default: ``False``); if ``True``, coextensions
          by a coloop or series elements will not be taken

        OUTPUT:

        An iterable containing instances of :class:`GraphicMatroid`. If
        ``vertices`` is not specified, the method iterates over all vertices.

        EXAMPLES::

            sage: G = Graph([(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 4), (2, 3), (3, 4)])
            sage: M = Matroid(range(8), G)
            sage: I = M.graphic_coextensions(vertices=[0], element='a')
            sage: sorted([N.graph().edges_incident(0, sort=True) for N in I], key=str)
            [[(0, 1, 0), (0, 2, 1), (0, 3, 2), (0, 4, 3), (0, 5, 'a')],
             [(0, 1, 0), (0, 2, 1), (0, 3, 2), (0, 5, 'a')],
             [(0, 1, 0), (0, 2, 1), (0, 4, 3), (0, 5, 'a')],
             [(0, 1, 0), (0, 2, 1), (0, 5, 'a')],
             [(0, 1, 0), (0, 3, 2), (0, 4, 3), (0, 5, 'a')],
             [(0, 1, 0), (0, 3, 2), (0, 5, 'a')],
             [(0, 2, 1), (0, 3, 2), (0, 4, 3), (0, 5, 'a')],
             [(0, 2, 1), (0, 3, 2), (0, 5, 'a')]]

        ::

            sage: N = Matroid(range(4), graphs.CycleGraph(4))
            sage: I = N.graphic_coextensions(element='a')
            sage: for N1 in I:  # random
            ....:     N1.graph().edges(sort=True)
            [(0, 1, 0), (0, 3, 1), (0, 4, 'a'), (1, 2, 2), (2, 3, 3)]
            [(0, 1, 0), (0, 3, 1), (1, 4, 2), (2, 3, 3), (2, 4, 'a')]
            sage: sum(1 for n in N.graphic_coextensions(cosimple=True))
            0

        TESTS::

            sage: M = Matroid(graphs.EmptyGraph())
            sage: M.graphic_coextension(0)
            Graphic matroid of rank 1 on 1 elements
            sage: I = M.graphic_coextensions(element='a')
            sage: for m in I:
            ....:     m.graph().edges(sort=True)
            [(0, 1, 'a')]
            sage: N = Matroid(graphs.CycleGraph(4))
            sage: I = N.graphic_coextensions(vertices=[3, 4], element='a')
            sage: next(I)
            Traceback (most recent call last):
            ...
            ValueError: vertices are not all in the graph

        We expect 136 graphic coextensions of an 8-spoked wheel: 128 extensions
        from the center vertex because there are (256/2) ways to put the 8
        center edges into 2 sets, and then 8 more for series extensions of the
        rims::

            sage: M = Matroid(graphs.WheelGraph(9))
            sage: I = M.graphic_coextensions()
            sage: sum(1 for N in I)
            136
            sage: I = M.graphic_coextensions(cosimple=True)
            sage: sum(1 for N in I)
            119
            sage: sum(1 for N in Matroid(graphs.WheelGraph(8)).graphic_coextensions())
            71

        This graph has max degree 3, so the only series extensions should be
        non-cosimple, ie. a coloop and one for every coseries class.
        12 total::

            sage: edgedict = {0: [1, 2, 3], 1: [2, 4], 2: [3], 3: [6],
            ....:             4: [5, 7], 5: [6, 7], 6: [7]}
            sage: M = Matroid(range(12), Graph(edgedict))
            sage: sorted(M.coclosure([4]))
            [4, 6]
            sage: sum(1 for N in M.graphic_coextensions())
            12
            sage: sum(1 for N in M.graphic_coextensions(cosimple=True))
            0"""
    @overload
    def graphic_coextensions(self) -> Any:
        """GraphicMatroid.graphic_coextensions(self, vertices=None, v=None, element=None, cosimple=False)

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 1560)

        Return an iterator of graphic coextensions.

        This method iterates over the vertices in the input. If
        ``cosimple == False``, it first coextends by a coloop and series edge
        for every edge incident with the vertices. For vertices of degree four
        or higher, it will consider the ways to partition the vertex into two
        sets of cardinality at least two, and these will be the edges incident
        with the vertices after splitting.

        At most one series coextension will be taken for each series class.

        INPUT:

        - ``vertices`` -- (optional) the vertices to be split
        - ``v`` -- (optional) the name of the new vertex
        - ``element`` -- (optional) the name of the new element
        - ``cosimple`` -- boolean (default: ``False``); if ``True``, coextensions
          by a coloop or series elements will not be taken

        OUTPUT:

        An iterable containing instances of :class:`GraphicMatroid`. If
        ``vertices`` is not specified, the method iterates over all vertices.

        EXAMPLES::

            sage: G = Graph([(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 4), (2, 3), (3, 4)])
            sage: M = Matroid(range(8), G)
            sage: I = M.graphic_coextensions(vertices=[0], element='a')
            sage: sorted([N.graph().edges_incident(0, sort=True) for N in I], key=str)
            [[(0, 1, 0), (0, 2, 1), (0, 3, 2), (0, 4, 3), (0, 5, 'a')],
             [(0, 1, 0), (0, 2, 1), (0, 3, 2), (0, 5, 'a')],
             [(0, 1, 0), (0, 2, 1), (0, 4, 3), (0, 5, 'a')],
             [(0, 1, 0), (0, 2, 1), (0, 5, 'a')],
             [(0, 1, 0), (0, 3, 2), (0, 4, 3), (0, 5, 'a')],
             [(0, 1, 0), (0, 3, 2), (0, 5, 'a')],
             [(0, 2, 1), (0, 3, 2), (0, 4, 3), (0, 5, 'a')],
             [(0, 2, 1), (0, 3, 2), (0, 5, 'a')]]

        ::

            sage: N = Matroid(range(4), graphs.CycleGraph(4))
            sage: I = N.graphic_coextensions(element='a')
            sage: for N1 in I:  # random
            ....:     N1.graph().edges(sort=True)
            [(0, 1, 0), (0, 3, 1), (0, 4, 'a'), (1, 2, 2), (2, 3, 3)]
            [(0, 1, 0), (0, 3, 1), (1, 4, 2), (2, 3, 3), (2, 4, 'a')]
            sage: sum(1 for n in N.graphic_coextensions(cosimple=True))
            0

        TESTS::

            sage: M = Matroid(graphs.EmptyGraph())
            sage: M.graphic_coextension(0)
            Graphic matroid of rank 1 on 1 elements
            sage: I = M.graphic_coextensions(element='a')
            sage: for m in I:
            ....:     m.graph().edges(sort=True)
            [(0, 1, 'a')]
            sage: N = Matroid(graphs.CycleGraph(4))
            sage: I = N.graphic_coextensions(vertices=[3, 4], element='a')
            sage: next(I)
            Traceback (most recent call last):
            ...
            ValueError: vertices are not all in the graph

        We expect 136 graphic coextensions of an 8-spoked wheel: 128 extensions
        from the center vertex because there are (256/2) ways to put the 8
        center edges into 2 sets, and then 8 more for series extensions of the
        rims::

            sage: M = Matroid(graphs.WheelGraph(9))
            sage: I = M.graphic_coextensions()
            sage: sum(1 for N in I)
            136
            sage: I = M.graphic_coextensions(cosimple=True)
            sage: sum(1 for N in I)
            119
            sage: sum(1 for N in Matroid(graphs.WheelGraph(8)).graphic_coextensions())
            71

        This graph has max degree 3, so the only series extensions should be
        non-cosimple, ie. a coloop and one for every coseries class.
        12 total::

            sage: edgedict = {0: [1, 2, 3], 1: [2, 4], 2: [3], 3: [6],
            ....:             4: [5, 7], 5: [6, 7], 6: [7]}
            sage: M = Matroid(range(12), Graph(edgedict))
            sage: sorted(M.coclosure([4]))
            [4, 6]
            sage: sum(1 for N in M.graphic_coextensions())
            12
            sage: sum(1 for N in M.graphic_coextensions(cosimple=True))
            0"""
    @overload
    def graphic_coextensions(self) -> Any:
        """GraphicMatroid.graphic_coextensions(self, vertices=None, v=None, element=None, cosimple=False)

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 1560)

        Return an iterator of graphic coextensions.

        This method iterates over the vertices in the input. If
        ``cosimple == False``, it first coextends by a coloop and series edge
        for every edge incident with the vertices. For vertices of degree four
        or higher, it will consider the ways to partition the vertex into two
        sets of cardinality at least two, and these will be the edges incident
        with the vertices after splitting.

        At most one series coextension will be taken for each series class.

        INPUT:

        - ``vertices`` -- (optional) the vertices to be split
        - ``v`` -- (optional) the name of the new vertex
        - ``element`` -- (optional) the name of the new element
        - ``cosimple`` -- boolean (default: ``False``); if ``True``, coextensions
          by a coloop or series elements will not be taken

        OUTPUT:

        An iterable containing instances of :class:`GraphicMatroid`. If
        ``vertices`` is not specified, the method iterates over all vertices.

        EXAMPLES::

            sage: G = Graph([(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 4), (2, 3), (3, 4)])
            sage: M = Matroid(range(8), G)
            sage: I = M.graphic_coextensions(vertices=[0], element='a')
            sage: sorted([N.graph().edges_incident(0, sort=True) for N in I], key=str)
            [[(0, 1, 0), (0, 2, 1), (0, 3, 2), (0, 4, 3), (0, 5, 'a')],
             [(0, 1, 0), (0, 2, 1), (0, 3, 2), (0, 5, 'a')],
             [(0, 1, 0), (0, 2, 1), (0, 4, 3), (0, 5, 'a')],
             [(0, 1, 0), (0, 2, 1), (0, 5, 'a')],
             [(0, 1, 0), (0, 3, 2), (0, 4, 3), (0, 5, 'a')],
             [(0, 1, 0), (0, 3, 2), (0, 5, 'a')],
             [(0, 2, 1), (0, 3, 2), (0, 4, 3), (0, 5, 'a')],
             [(0, 2, 1), (0, 3, 2), (0, 5, 'a')]]

        ::

            sage: N = Matroid(range(4), graphs.CycleGraph(4))
            sage: I = N.graphic_coextensions(element='a')
            sage: for N1 in I:  # random
            ....:     N1.graph().edges(sort=True)
            [(0, 1, 0), (0, 3, 1), (0, 4, 'a'), (1, 2, 2), (2, 3, 3)]
            [(0, 1, 0), (0, 3, 1), (1, 4, 2), (2, 3, 3), (2, 4, 'a')]
            sage: sum(1 for n in N.graphic_coextensions(cosimple=True))
            0

        TESTS::

            sage: M = Matroid(graphs.EmptyGraph())
            sage: M.graphic_coextension(0)
            Graphic matroid of rank 1 on 1 elements
            sage: I = M.graphic_coextensions(element='a')
            sage: for m in I:
            ....:     m.graph().edges(sort=True)
            [(0, 1, 'a')]
            sage: N = Matroid(graphs.CycleGraph(4))
            sage: I = N.graphic_coextensions(vertices=[3, 4], element='a')
            sage: next(I)
            Traceback (most recent call last):
            ...
            ValueError: vertices are not all in the graph

        We expect 136 graphic coextensions of an 8-spoked wheel: 128 extensions
        from the center vertex because there are (256/2) ways to put the 8
        center edges into 2 sets, and then 8 more for series extensions of the
        rims::

            sage: M = Matroid(graphs.WheelGraph(9))
            sage: I = M.graphic_coextensions()
            sage: sum(1 for N in I)
            136
            sage: I = M.graphic_coextensions(cosimple=True)
            sage: sum(1 for N in I)
            119
            sage: sum(1 for N in Matroid(graphs.WheelGraph(8)).graphic_coextensions())
            71

        This graph has max degree 3, so the only series extensions should be
        non-cosimple, ie. a coloop and one for every coseries class.
        12 total::

            sage: edgedict = {0: [1, 2, 3], 1: [2, 4], 2: [3], 3: [6],
            ....:             4: [5, 7], 5: [6, 7], 6: [7]}
            sage: M = Matroid(range(12), Graph(edgedict))
            sage: sorted(M.coclosure([4]))
            [4, 6]
            sage: sum(1 for N in M.graphic_coextensions())
            12
            sage: sum(1 for N in M.graphic_coextensions(cosimple=True))
            0"""
    @overload
    def graphic_coextensions(self, cosimple=...) -> Any:
        """GraphicMatroid.graphic_coextensions(self, vertices=None, v=None, element=None, cosimple=False)

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 1560)

        Return an iterator of graphic coextensions.

        This method iterates over the vertices in the input. If
        ``cosimple == False``, it first coextends by a coloop and series edge
        for every edge incident with the vertices. For vertices of degree four
        or higher, it will consider the ways to partition the vertex into two
        sets of cardinality at least two, and these will be the edges incident
        with the vertices after splitting.

        At most one series coextension will be taken for each series class.

        INPUT:

        - ``vertices`` -- (optional) the vertices to be split
        - ``v`` -- (optional) the name of the new vertex
        - ``element`` -- (optional) the name of the new element
        - ``cosimple`` -- boolean (default: ``False``); if ``True``, coextensions
          by a coloop or series elements will not be taken

        OUTPUT:

        An iterable containing instances of :class:`GraphicMatroid`. If
        ``vertices`` is not specified, the method iterates over all vertices.

        EXAMPLES::

            sage: G = Graph([(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 4), (2, 3), (3, 4)])
            sage: M = Matroid(range(8), G)
            sage: I = M.graphic_coextensions(vertices=[0], element='a')
            sage: sorted([N.graph().edges_incident(0, sort=True) for N in I], key=str)
            [[(0, 1, 0), (0, 2, 1), (0, 3, 2), (0, 4, 3), (0, 5, 'a')],
             [(0, 1, 0), (0, 2, 1), (0, 3, 2), (0, 5, 'a')],
             [(0, 1, 0), (0, 2, 1), (0, 4, 3), (0, 5, 'a')],
             [(0, 1, 0), (0, 2, 1), (0, 5, 'a')],
             [(0, 1, 0), (0, 3, 2), (0, 4, 3), (0, 5, 'a')],
             [(0, 1, 0), (0, 3, 2), (0, 5, 'a')],
             [(0, 2, 1), (0, 3, 2), (0, 4, 3), (0, 5, 'a')],
             [(0, 2, 1), (0, 3, 2), (0, 5, 'a')]]

        ::

            sage: N = Matroid(range(4), graphs.CycleGraph(4))
            sage: I = N.graphic_coextensions(element='a')
            sage: for N1 in I:  # random
            ....:     N1.graph().edges(sort=True)
            [(0, 1, 0), (0, 3, 1), (0, 4, 'a'), (1, 2, 2), (2, 3, 3)]
            [(0, 1, 0), (0, 3, 1), (1, 4, 2), (2, 3, 3), (2, 4, 'a')]
            sage: sum(1 for n in N.graphic_coextensions(cosimple=True))
            0

        TESTS::

            sage: M = Matroid(graphs.EmptyGraph())
            sage: M.graphic_coextension(0)
            Graphic matroid of rank 1 on 1 elements
            sage: I = M.graphic_coextensions(element='a')
            sage: for m in I:
            ....:     m.graph().edges(sort=True)
            [(0, 1, 'a')]
            sage: N = Matroid(graphs.CycleGraph(4))
            sage: I = N.graphic_coextensions(vertices=[3, 4], element='a')
            sage: next(I)
            Traceback (most recent call last):
            ...
            ValueError: vertices are not all in the graph

        We expect 136 graphic coextensions of an 8-spoked wheel: 128 extensions
        from the center vertex because there are (256/2) ways to put the 8
        center edges into 2 sets, and then 8 more for series extensions of the
        rims::

            sage: M = Matroid(graphs.WheelGraph(9))
            sage: I = M.graphic_coextensions()
            sage: sum(1 for N in I)
            136
            sage: I = M.graphic_coextensions(cosimple=True)
            sage: sum(1 for N in I)
            119
            sage: sum(1 for N in Matroid(graphs.WheelGraph(8)).graphic_coextensions())
            71

        This graph has max degree 3, so the only series extensions should be
        non-cosimple, ie. a coloop and one for every coseries class.
        12 total::

            sage: edgedict = {0: [1, 2, 3], 1: [2, 4], 2: [3], 3: [6],
            ....:             4: [5, 7], 5: [6, 7], 6: [7]}
            sage: M = Matroid(range(12), Graph(edgedict))
            sage: sorted(M.coclosure([4]))
            [4, 6]
            sage: sum(1 for N in M.graphic_coextensions())
            12
            sage: sum(1 for N in M.graphic_coextensions(cosimple=True))
            0"""
    def graphic_extension(self, u, v=..., element=...) -> Any:
        """GraphicMatroid.graphic_extension(self, u, v=None, element=None)

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 1287)

        Return a graphic matroid extended by a new element.

        A new edge will be added between ``u`` and ``v``. If ``v`` is not
        specified, then a loop is added on ``u``.

        INPUT:

        - ``u`` -- vertex in the matroid's graph
        - ``v`` -- (optional) another vertex
        - ``element`` -- (optional) the label of the new element

        OUTPUT:

        A :class:`GraphicMatroid` with the specified element added. Note that if
        ``v`` is not specified or if ``v`` is ``u``, then the new element will
        be a loop. If the new element's label is not specified, it will be
        generated automatically.

        EXAMPLES::

            sage: M = matroids.CompleteGraphic(4)
            sage: M1 = M.graphic_extension(0,1,'a'); M1
            Graphic matroid of rank 3 on 7 elements
            sage: list(M1.graph().edge_iterator())
            [(0, 1, 'a'), (0, 1, 0), (0, 2, 1), (0, 3, 2), (1, 2, 3), (1, 3, 4), (2, 3, 5)]
            sage: M2 = M1.graphic_extension(3); M2
            Graphic matroid of rank 3 on 8 elements

        ::

            sage: M = Matroid(range(10), graphs.PetersenGraph())
            sage: sorted(M.graphic_extension(0, 'b', 'c').graph().vertex_iterator(), key=str)
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'b']
            sage: M.graphic_extension('a', 'b', 'c').graph().vertices(sort=False)
            Traceback (most recent call last):
            ...
            ValueError: u must be an existing vertex

        TESTS::

            sage: M = Matroid(graphs.EmptyGraph())
            sage: M.graphic_extension(0)
            Graphic matroid of rank 0 on 1 elements
            sage: M.graphic_extension(0, 1, 'a')
            Graphic matroid of rank 1 on 1 elements"""
    @overload
    def graphic_extensions(self, element=..., vertices=..., simple=...) -> Any:
        """GraphicMatroid.graphic_extensions(self, element=None, vertices=None, simple=False)

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 1348)

        Return an iterable containing the graphic extensions.

        This method iterates over the vertices in the input. If
        ``simple == False``, it first extends by a loop. It will then add an
        edge between every pair of vertices in the input, skipping pairs of
        vertices with an edge already between them if ``simple == True``.

        This method only considers the current graph presentation, and
        does not take 2-isomorphism into account. Use
        :meth:`twist <sage.matroids.graphic_matroid.GraphicMatroid.twist>` or
        :meth:`one_sum <sage.matroids.graphic_matroid.GraphicMatroid.one_sum>`
        if you wish to change the graph presentation.

        INPUT:

        - ``element`` -- (optional) the name of the newly added element in
          each extension
        - ``vertices`` -- (optional) a set of vertices over which the extension
          may be taken
        - ``simple`` -- boolean (default: ``False``); if ``True``, extensions
          by loops and parallel elements are not taken

        OUTPUT:

        An iterable containing instances of :class:`GraphicMatroid`. If
        ``vertices`` is not specified, every vertex is used.

        .. NOTE::

            The extension by a loop will always occur unless
            ``simple == True``. The extension by a coloop will never occur.

        EXAMPLES::

            sage: M = Matroid(range(5), graphs.DiamondGraph())
            sage: I = M.graphic_extensions('a')
            sage: for N in I:
            ....:     list(N.graph().edge_iterator())
            [(0, 0, 'a'), (0, 1, 0), (0, 2, 1), (1, 2, 2), (1, 3, 3), (2, 3, 4)]
            [(0, 1, 'a'), (0, 1, 0), (0, 2, 1), (1, 2, 2), (1, 3, 3), (2, 3, 4)]
            [(0, 1, 0), (0, 2, 'a'), (0, 2, 1), (1, 2, 2), (1, 3, 3), (2, 3, 4)]
            [(0, 1, 0), (0, 2, 1), (0, 3, 'a'), (1, 2, 2), (1, 3, 3), (2, 3, 4)]
            [(0, 1, 0), (0, 2, 1), (1, 2, 'a'), (1, 2, 2), (1, 3, 3), (2, 3, 4)]
            [(0, 1, 0), (0, 2, 1), (1, 2, 2), (1, 3, 'a'), (1, 3, 3), (2, 3, 4)]
            [(0, 1, 0), (0, 2, 1), (1, 2, 2), (1, 3, 3), (2, 3, 'a'), (2, 3, 4)]

        ::

            sage: M = Matroid(graphs.CompleteBipartiteGraph(3,3))
            sage: I = M.graphic_extensions(simple=True)
            sage: sum (1 for i in I)
            6
            sage: I = M.graphic_extensions(vertices=[0,1,2])
            sage: sum (1 for i in I)
            4"""
    @overload
    def graphic_extensions(self, simple=...) -> Any:
        """GraphicMatroid.graphic_extensions(self, element=None, vertices=None, simple=False)

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 1348)

        Return an iterable containing the graphic extensions.

        This method iterates over the vertices in the input. If
        ``simple == False``, it first extends by a loop. It will then add an
        edge between every pair of vertices in the input, skipping pairs of
        vertices with an edge already between them if ``simple == True``.

        This method only considers the current graph presentation, and
        does not take 2-isomorphism into account. Use
        :meth:`twist <sage.matroids.graphic_matroid.GraphicMatroid.twist>` or
        :meth:`one_sum <sage.matroids.graphic_matroid.GraphicMatroid.one_sum>`
        if you wish to change the graph presentation.

        INPUT:

        - ``element`` -- (optional) the name of the newly added element in
          each extension
        - ``vertices`` -- (optional) a set of vertices over which the extension
          may be taken
        - ``simple`` -- boolean (default: ``False``); if ``True``, extensions
          by loops and parallel elements are not taken

        OUTPUT:

        An iterable containing instances of :class:`GraphicMatroid`. If
        ``vertices`` is not specified, every vertex is used.

        .. NOTE::

            The extension by a loop will always occur unless
            ``simple == True``. The extension by a coloop will never occur.

        EXAMPLES::

            sage: M = Matroid(range(5), graphs.DiamondGraph())
            sage: I = M.graphic_extensions('a')
            sage: for N in I:
            ....:     list(N.graph().edge_iterator())
            [(0, 0, 'a'), (0, 1, 0), (0, 2, 1), (1, 2, 2), (1, 3, 3), (2, 3, 4)]
            [(0, 1, 'a'), (0, 1, 0), (0, 2, 1), (1, 2, 2), (1, 3, 3), (2, 3, 4)]
            [(0, 1, 0), (0, 2, 'a'), (0, 2, 1), (1, 2, 2), (1, 3, 3), (2, 3, 4)]
            [(0, 1, 0), (0, 2, 1), (0, 3, 'a'), (1, 2, 2), (1, 3, 3), (2, 3, 4)]
            [(0, 1, 0), (0, 2, 1), (1, 2, 'a'), (1, 2, 2), (1, 3, 3), (2, 3, 4)]
            [(0, 1, 0), (0, 2, 1), (1, 2, 2), (1, 3, 'a'), (1, 3, 3), (2, 3, 4)]
            [(0, 1, 0), (0, 2, 1), (1, 2, 2), (1, 3, 3), (2, 3, 'a'), (2, 3, 4)]

        ::

            sage: M = Matroid(graphs.CompleteBipartiteGraph(3,3))
            sage: I = M.graphic_extensions(simple=True)
            sage: sum (1 for i in I)
            6
            sage: I = M.graphic_extensions(vertices=[0,1,2])
            sage: sum (1 for i in I)
            4"""
    @overload
    def graphic_extensions(self, vertices=...) -> Any:
        """GraphicMatroid.graphic_extensions(self, element=None, vertices=None, simple=False)

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 1348)

        Return an iterable containing the graphic extensions.

        This method iterates over the vertices in the input. If
        ``simple == False``, it first extends by a loop. It will then add an
        edge between every pair of vertices in the input, skipping pairs of
        vertices with an edge already between them if ``simple == True``.

        This method only considers the current graph presentation, and
        does not take 2-isomorphism into account. Use
        :meth:`twist <sage.matroids.graphic_matroid.GraphicMatroid.twist>` or
        :meth:`one_sum <sage.matroids.graphic_matroid.GraphicMatroid.one_sum>`
        if you wish to change the graph presentation.

        INPUT:

        - ``element`` -- (optional) the name of the newly added element in
          each extension
        - ``vertices`` -- (optional) a set of vertices over which the extension
          may be taken
        - ``simple`` -- boolean (default: ``False``); if ``True``, extensions
          by loops and parallel elements are not taken

        OUTPUT:

        An iterable containing instances of :class:`GraphicMatroid`. If
        ``vertices`` is not specified, every vertex is used.

        .. NOTE::

            The extension by a loop will always occur unless
            ``simple == True``. The extension by a coloop will never occur.

        EXAMPLES::

            sage: M = Matroid(range(5), graphs.DiamondGraph())
            sage: I = M.graphic_extensions('a')
            sage: for N in I:
            ....:     list(N.graph().edge_iterator())
            [(0, 0, 'a'), (0, 1, 0), (0, 2, 1), (1, 2, 2), (1, 3, 3), (2, 3, 4)]
            [(0, 1, 'a'), (0, 1, 0), (0, 2, 1), (1, 2, 2), (1, 3, 3), (2, 3, 4)]
            [(0, 1, 0), (0, 2, 'a'), (0, 2, 1), (1, 2, 2), (1, 3, 3), (2, 3, 4)]
            [(0, 1, 0), (0, 2, 1), (0, 3, 'a'), (1, 2, 2), (1, 3, 3), (2, 3, 4)]
            [(0, 1, 0), (0, 2, 1), (1, 2, 'a'), (1, 2, 2), (1, 3, 3), (2, 3, 4)]
            [(0, 1, 0), (0, 2, 1), (1, 2, 2), (1, 3, 'a'), (1, 3, 3), (2, 3, 4)]
            [(0, 1, 0), (0, 2, 1), (1, 2, 2), (1, 3, 3), (2, 3, 'a'), (2, 3, 4)]

        ::

            sage: M = Matroid(graphs.CompleteBipartiteGraph(3,3))
            sage: I = M.graphic_extensions(simple=True)
            sage: sum (1 for i in I)
            6
            sage: I = M.graphic_extensions(vertices=[0,1,2])
            sage: sum (1 for i in I)
            4"""
    @overload
    def groundset(self) -> frozenset:
        """GraphicMatroid.groundset(self) -> frozenset

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 222)

        Return the groundset of the matroid as a frozenset.

        EXAMPLES::

            sage: M = Matroid(graphs.DiamondGraph())
            sage: sorted(M.groundset())
            [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3)]
            sage: G = graphs.CompleteGraph(3).disjoint_union(graphs.CompleteGraph(4))
            sage: M = Matroid(range(G.num_edges()), G); sorted(M.groundset())
            [0, 1, 2, 3, 4, 5, 6, 7, 8]
            sage: M = Matroid(Graph([(0, 1, 'a'), (0, 2, 'b'), (0, 3, 'c')]))
            sage: sorted(M.groundset())
            ['a', 'b', 'c']"""
    @overload
    def groundset(self) -> Any:
        """GraphicMatroid.groundset(self) -> frozenset

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 222)

        Return the groundset of the matroid as a frozenset.

        EXAMPLES::

            sage: M = Matroid(graphs.DiamondGraph())
            sage: sorted(M.groundset())
            [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3)]
            sage: G = graphs.CompleteGraph(3).disjoint_union(graphs.CompleteGraph(4))
            sage: M = Matroid(range(G.num_edges()), G); sorted(M.groundset())
            [0, 1, 2, 3, 4, 5, 6, 7, 8]
            sage: M = Matroid(Graph([(0, 1, 'a'), (0, 2, 'b'), (0, 3, 'c')]))
            sage: sorted(M.groundset())
            ['a', 'b', 'c']"""
    @overload
    def groundset(self) -> Any:
        """GraphicMatroid.groundset(self) -> frozenset

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 222)

        Return the groundset of the matroid as a frozenset.

        EXAMPLES::

            sage: M = Matroid(graphs.DiamondGraph())
            sage: sorted(M.groundset())
            [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3)]
            sage: G = graphs.CompleteGraph(3).disjoint_union(graphs.CompleteGraph(4))
            sage: M = Matroid(range(G.num_edges()), G); sorted(M.groundset())
            [0, 1, 2, 3, 4, 5, 6, 7, 8]
            sage: M = Matroid(Graph([(0, 1, 'a'), (0, 2, 'b'), (0, 3, 'c')]))
            sage: sorted(M.groundset())
            ['a', 'b', 'c']"""
    @overload
    def groundset(self) -> Any:
        """GraphicMatroid.groundset(self) -> frozenset

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 222)

        Return the groundset of the matroid as a frozenset.

        EXAMPLES::

            sage: M = Matroid(graphs.DiamondGraph())
            sage: sorted(M.groundset())
            [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3)]
            sage: G = graphs.CompleteGraph(3).disjoint_union(graphs.CompleteGraph(4))
            sage: M = Matroid(range(G.num_edges()), G); sorted(M.groundset())
            [0, 1, 2, 3, 4, 5, 6, 7, 8]
            sage: M = Matroid(Graph([(0, 1, 'a'), (0, 2, 'b'), (0, 3, 'c')]))
            sage: sorted(M.groundset())
            ['a', 'b', 'c']"""
    def groundset_to_edges(self, X) -> list:
        """GraphicMatroid.groundset_to_edges(self, X) -> list

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 1199)

        Return a list of edges corresponding to a set of groundset elements.

        INPUT:

        - ``X`` -- subset of the groundset

        OUTPUT: list of graph edges

        EXAMPLES::

            sage: M = Matroid(range(5), graphs.DiamondGraph())
            sage: M.groundset_to_edges([2, 3, 4])
            [(1, 2, 2), (1, 3, 3), (2, 3, 4)]
            sage: M.groundset_to_edges([2, 3, 4, 5])
            Traceback (most recent call last):
            ...
            ValueError: input must be a subset of the groundset"""
    @overload
    def is_graphic(self) -> bool:
        """GraphicMatroid.is_graphic(self) -> bool

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 1115)

        Return if ``self`` is graphic.

        This is trivially ``True`` for a :class:`GraphicMatroid`.

        EXAMPLES::

            sage: M = Matroid(graphs.PetersenGraph())
            sage: M.is_graphic()
            True"""
    @overload
    def is_graphic(self) -> Any:
        """GraphicMatroid.is_graphic(self) -> bool

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 1115)

        Return if ``self`` is graphic.

        This is trivially ``True`` for a :class:`GraphicMatroid`.

        EXAMPLES::

            sage: M = Matroid(graphs.PetersenGraph())
            sage: M.is_graphic()
            True"""
    @overload
    def is_regular(self) -> bool:
        """GraphicMatroid.is_regular(self) -> bool

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 1129)

        Return if ``self`` is regular.

        This is always ``True`` for a :class:`GraphicMatroid`.

        EXAMPLES::

            sage: M = Matroid(graphs.DesarguesGraph())
            sage: M.is_regular()
            True"""
    @overload
    def is_regular(self) -> Any:
        """GraphicMatroid.is_regular(self) -> bool

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 1129)

        Return if ``self`` is regular.

        This is always ``True`` for a :class:`GraphicMatroid`.

        EXAMPLES::

            sage: M = Matroid(graphs.DesarguesGraph())
            sage: M.is_regular()
            True"""
    @overload
    def is_valid(self, certificate=...) -> Any:
        """GraphicMatroid.is_valid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 1094)

        Test if the data obey the matroid axioms.

        Since a graph is used for the data, this is always the case.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``)

        OUTPUT: ``True``, or ``(True, {})``

        EXAMPLES::

            sage: M = matroids.CompleteGraphic(4); M
            M(K4): Graphic matroid of rank 3 on 6 elements
            sage: M.is_valid()
            True"""
    @overload
    def is_valid(self) -> Any:
        """GraphicMatroid.is_valid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 1094)

        Test if the data obey the matroid axioms.

        Since a graph is used for the data, this is always the case.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``)

        OUTPUT: ``True``, or ``(True, {})``

        EXAMPLES::

            sage: M = matroids.CompleteGraphic(4); M
            M(K4): Graphic matroid of rank 3 on 6 elements
            sage: M.is_valid()
            True"""
    def one_sum(self, X, u, v) -> Any:
        """GraphicMatroid.one_sum(self, X, u, v)

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 1819)

        Arrange matroid components in the graph.

        The matroid's graph must be connected even if the matroid is not
        connected, but if there are multiple matroid components, the user may
        choose how they are arranged in the graph. This method will take the
        block of the graph that represents `X` and attach it by vertex `u` to
        another vertex `v` in the graph.

        INPUT:

        - ``X`` -- subset of the groundset
        - ``u`` -- vertex spanned by the edges of the elements in ``X``
        - ``v`` -- vertex spanned by the edges of the elements not in ``X``

        OUTPUT: :class:`GraphicMatroid` isomorphic to this matroid but
        with a graph that is not necessarily isomorphic

        EXAMPLES::

            sage: edgedict = {0:[1, 2], 1:[2, 3], 2:[3], 3:[4, 5], 6:[4, 5]}
            sage: M = Matroid(range(9), Graph(edgedict))
            sage: M.graph().edges(sort=True)
            [(0, 1, 0),
             (0, 2, 1),
             (1, 2, 2),
             (1, 3, 3),
             (2, 3, 4),
             (3, 4, 5),
             (3, 5, 6),
             (4, 6, 7),
             (5, 6, 8)]
            sage: M1 = M.one_sum(u=3, v=1, X=[5, 6, 7, 8])
            sage: M1.graph().edges(sort=True)
            [(0, 1, 0),
             (0, 2, 1),
             (1, 2, 2),
             (1, 3, 3),
             (1, 4, 5),
             (1, 5, 6),
             (2, 3, 4),
             (4, 6, 7),
             (5, 6, 8)]
            sage: M2 = M.one_sum(u=4, v=3, X=[5, 6, 7, 8])
            sage: M2.graph().edges(sort=True)
            [(0, 1, 0),
             (0, 2, 1),
             (1, 2, 2),
             (1, 3, 3),
             (2, 3, 4),
             (3, 6, 7),
             (3, 7, 5),
             (5, 6, 8),
             (5, 7, 6)]

        TESTS::

            sage: M = matroids.CompleteGraphic(4)
            sage: M.one_sum(u=1, v=2, X=[0,1])
            Traceback (most recent call last):
            ...
            ValueError: the input must display a 1-separation

        ::

            sage: M = Matroid(range(5), graphs.BullGraph())
            sage: M.graph().edges(sort=True)
            [(0, 1, 0), (0, 2, 1), (1, 2, 2), (1, 3, 3), (2, 4, 4)]
            sage: M1 = M.one_sum(u=3, v=0, X=[3,4])
            Traceback (most recent call last):
            ...
            ValueError: too many vertices in the intersection

            sage: M1 = M.one_sum(u=3, v=2, X=[3])
            sage: M1.graph().edges(sort=True)
            [(0, 1, 0), (0, 2, 1), (1, 2, 2), (2, 4, 4), (2, 5, 3)]

            sage: M2 = M1.one_sum(u=5, v=0, X=[3,4])
            sage: M2.graph().edges(sort=True)
            [(0, 1, 0), (0, 2, 1), (0, 3, 3), (1, 2, 2), (3, 4, 4)]

            sage: M = Matroid(range(5), graphs.BullGraph())
            sage: M.one_sum(u=0, v=1, X=[3])
            Traceback (most recent call last):
            ...
            ValueError: first vertex must be spanned by the input

            sage: M.one_sum(u=1, v=3, X=[3])
            Traceback (most recent call last):
            ...
            ValueError: second vertex must be spanned by the rest of the graph"""
    @overload
    def regular_matroid(self) -> Any:
        """GraphicMatroid.regular_matroid(self)

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 1952)

        Return an instance of :class:`RegularMatroid` isomorphic to this
        :class:`GraphicMatroid`.

        EXAMPLES::

            sage: M = matroids.CompleteGraphic(5); M
            M(K5): Graphic matroid of rank 4 on 10 elements
            sage: N = M.regular_matroid(); N
            Regular matroid of rank 4 on 10 elements with 125 bases
            sage: M.equals(N)
            True
            sage: M == N
            False

        TESTS:

        Check that :issue:`28482` is fixed::

            sage: G = Graph([[3, 4], [4, 1], [1, 2], [2, 3], [3, 5], [5, 6], [6, 3]])
            sage: M = Matroid(G)
            sage: R = M.regular_matroid()
            sage: set(M.circuits()) == set(R.circuits())
            True"""
    @overload
    def regular_matroid(self) -> Any:
        """GraphicMatroid.regular_matroid(self)

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 1952)

        Return an instance of :class:`RegularMatroid` isomorphic to this
        :class:`GraphicMatroid`.

        EXAMPLES::

            sage: M = matroids.CompleteGraphic(5); M
            M(K5): Graphic matroid of rank 4 on 10 elements
            sage: N = M.regular_matroid(); N
            Regular matroid of rank 4 on 10 elements with 125 bases
            sage: M.equals(N)
            True
            sage: M == N
            False

        TESTS:

        Check that :issue:`28482` is fixed::

            sage: G = Graph([[3, 4], [4, 1], [1, 2], [2, 3], [3, 5], [5, 6], [6, 3]])
            sage: M = Matroid(G)
            sage: R = M.regular_matroid()
            sage: set(M.circuits()) == set(R.circuits())
            True"""
    @overload
    def regular_matroid(self) -> Any:
        """GraphicMatroid.regular_matroid(self)

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 1952)

        Return an instance of :class:`RegularMatroid` isomorphic to this
        :class:`GraphicMatroid`.

        EXAMPLES::

            sage: M = matroids.CompleteGraphic(5); M
            M(K5): Graphic matroid of rank 4 on 10 elements
            sage: N = M.regular_matroid(); N
            Regular matroid of rank 4 on 10 elements with 125 bases
            sage: M.equals(N)
            True
            sage: M == N
            False

        TESTS:

        Check that :issue:`28482` is fixed::

            sage: G = Graph([[3, 4], [4, 1], [1, 2], [2, 3], [3, 5], [5, 6], [6, 3]])
            sage: M = Matroid(G)
            sage: R = M.regular_matroid()
            sage: set(M.circuits()) == set(R.circuits())
            True"""
    @overload
    def relabel(self, mapping) -> Any:
        """GraphicMatroid.relabel(self, mapping)

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 1982)

        Return an isomorphic matroid with relabeled groundset.

        The output is obtained by relabeling each element `e` by
        ``mapping[e]``, where ``mapping`` is a given injective map. If
        ``mapping[e]`` is not defined, then the identity map is assumed.

        INPUT:

        - ``mapping`` -- a Python object such that ``mapping[e]`` is the new
          label of `e`

        OUTPUT: matroid

        EXAMPLES::

            sage: M = matroids.CompleteGraphic(4)
            sage: sorted(M.groundset())
            [0, 1, 2, 3, 4, 5]
            sage: N = M.relabel({0: 6, 5: 'e'})
            sage: sorted(N.groundset(), key=str)
            [1, 2, 3, 4, 6, 'e']
            sage: N.is_isomorphic(M)
            True

        TESTS::

            sage: M = matroids.CompleteGraphic(4)
            sage: f = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g'}
            sage: N = M.relabel(f)
            sage: for S in powerset(M.groundset()):
            ....:     assert M.rank(S) == N.rank([f[x] for x in S])"""
    @overload
    def relabel(self, f) -> Any:
        """GraphicMatroid.relabel(self, mapping)

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 1982)

        Return an isomorphic matroid with relabeled groundset.

        The output is obtained by relabeling each element `e` by
        ``mapping[e]``, where ``mapping`` is a given injective map. If
        ``mapping[e]`` is not defined, then the identity map is assumed.

        INPUT:

        - ``mapping`` -- a Python object such that ``mapping[e]`` is the new
          label of `e`

        OUTPUT: matroid

        EXAMPLES::

            sage: M = matroids.CompleteGraphic(4)
            sage: sorted(M.groundset())
            [0, 1, 2, 3, 4, 5]
            sage: N = M.relabel({0: 6, 5: 'e'})
            sage: sorted(N.groundset(), key=str)
            [1, 2, 3, 4, 6, 'e']
            sage: N.is_isomorphic(M)
            True

        TESTS::

            sage: M = matroids.CompleteGraphic(4)
            sage: f = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g'}
            sage: N = M.relabel(f)
            sage: for S in powerset(M.groundset()):
            ....:     assert M.rank(S) == N.rank([f[x] for x in S])"""
    def subgraph_from_set(self, X) -> Any:
        """GraphicMatroid.subgraph_from_set(self, X)

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 1242)

        Return the subgraph corresponding to the matroid restricted to `X`.

        INPUT:

        - ``X`` -- subset of the groundset

        OUTPUT: graph

        EXAMPLES::

            sage: M = Matroid(range(5), graphs.DiamondGraph())
            sage: M.subgraph_from_set([0,1,2])
            Looped multi-graph on 3 vertices
            sage: M.subgraph_from_set([3,4,5])
            Traceback (most recent call last):
            ...
            ValueError: input must be a subset of the groundset"""
    def twist(self, X) -> Any:
        """GraphicMatroid.twist(self, X)

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 1711)

        Perform a Whitney twist on the graph.

        `X` must be part of a 2-separation.
        The connectivity of `X` must be 1, and the subgraph induced by `X` must
        intersect the subgraph induced by the rest of the elements on exactly
        two vertices.

        INPUT:

        - ``X`` -- the set of elements to be twisted with respect
          to the rest of the matroid

        OUTPUT: :class:`GraphicMatroid` isomorphic to this matroid but
        with a graph that is not necessarily isomorphic

        EXAMPLES::

            sage: edgelist = [(0, 1, 0), (1, 2, 1), (1, 2, 2), (2, 3, 3),
            ....:             (2, 3, 4), (2, 3, 5), (3, 0, 6)]
            sage: M = Matroid(Graph(edgelist, multiedges=True))
            sage: M1 = M.twist([0, 1, 2]); M1.graph().edges(sort=True)
            [(0, 1, 1), (0, 1, 2), (0, 3, 6), (1, 2, 0), (2, 3, 3), (2, 3, 4), (2, 3, 5)]
            sage: M2 = M.twist([0, 1, 3])
            Traceback (most recent call last):
            ...
            ValueError: the input must display a 2-separation that is not a 1-separation

        TESTS::

            sage: edgedict = {0: [1, 2], 1: [2, 3], 2: [3], 3: [4, 5], 4: [5]}
            sage: M = Matroid(range(8), Graph(edgedict))
            sage: M.graph().edges(sort=True)
            [(0, 1, 0),
             (0, 2, 1),
             (1, 2, 2),
             (1, 3, 3),
             (2, 3, 4),
             (3, 4, 5),
             (3, 5, 6),
             (4, 5, 7)]
            sage: M1 = M.twist([0, 1]); M1.graph().edges(sort=True)
            [(0, 1, 1),
             (0, 2, 0),
             (1, 2, 2),
             (1, 3, 3),
             (2, 3, 4),
             (3, 4, 5),
             (3, 5, 6),
             (4, 5, 7)]
            sage: M2 = M1.twist([0, 1, 2]); M2.graph().edges(sort=True)
            [(0, 1, 0),
             (0, 2, 1),
             (1, 2, 2),
             (1, 3, 3),
             (2, 3, 4),
             (3, 4, 5),
             (3, 5, 6),
             (4, 5, 7)]
            sage: M1 == M
            False
            sage: M2 == M
            True
            sage: M2.twist([3, 4])
            Traceback (most recent call last):
            ...
            ValueError: too many vertices in the intersection"""
    @overload
    def vertex_map(self) -> Any:
        """GraphicMatroid.vertex_map(self)

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 1165)

        Return a dictionary mapping the input vertices to the current vertices.

        The graph for the matroid is always connected. If the constructor is
        given a graph with multiple components, it will connect them. The
        Python dictionary given by this method has the vertices from the
        input graph as keys, and the corresponding vertex label after any
        merging as values.

        OUTPUT: dictionary

        EXAMPLES::

            sage: G = Graph([(0, 1), (0, 2), (1, 2), (3, 4), (3, 5), (4, 5),
            ....: (6, 7), (6, 8), (7, 8), (8, 8), (7, 8)], multiedges=True, loops=True)
            sage: M = Matroid(range(G.num_edges()), G)
            sage: M.graph().edges(sort=True)
            [(0, 1, 0),
             (0, 2, 1),
             (1, 2, 2),
             (1, 4, 3),
             (1, 5, 4),
             (4, 5, 5),
             (4, 7, 6),
             (4, 8, 7),
             (7, 8, 8),
             (7, 8, 9),
             (8, 8, 10)]
            sage: M.vertex_map()
            {0: 0, 1: 1, 2: 2, 3: 1, 4: 4, 5: 5, 6: 4, 7: 7, 8: 8}"""
    @overload
    def vertex_map(self) -> Any:
        """GraphicMatroid.vertex_map(self)

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 1165)

        Return a dictionary mapping the input vertices to the current vertices.

        The graph for the matroid is always connected. If the constructor is
        given a graph with multiple components, it will connect them. The
        Python dictionary given by this method has the vertices from the
        input graph as keys, and the corresponding vertex label after any
        merging as values.

        OUTPUT: dictionary

        EXAMPLES::

            sage: G = Graph([(0, 1), (0, 2), (1, 2), (3, 4), (3, 5), (4, 5),
            ....: (6, 7), (6, 8), (7, 8), (8, 8), (7, 8)], multiedges=True, loops=True)
            sage: M = Matroid(range(G.num_edges()), G)
            sage: M.graph().edges(sort=True)
            [(0, 1, 0),
             (0, 2, 1),
             (1, 2, 2),
             (1, 4, 3),
             (1, 5, 4),
             (4, 5, 5),
             (4, 7, 6),
             (4, 8, 7),
             (7, 8, 8),
             (7, 8, 9),
             (8, 8, 10)]
            sage: M.vertex_map()
            {0: 0, 1: 1, 2: 2, 3: 1, 4: 4, 5: 5, 6: 4, 7: 7, 8: 8}"""
    def __eq__(self, other) -> Any:
        """GraphicMatroid.__eq__(self, other)

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 363)

        Compare two matroids.

        For two graphic matroids to be equal, all attributes of the underlying
        graphs must be equal.

        INPUT:

        - ``other`` -- matroid

        OUTPUT: ``True`` if ``self`` and ``other`` have the same graph;
        ``False`` otherwise

        EXAMPLES::

            sage: M = Matroid(graphs.CompleteGraph(3))
            sage: N = Matroid(graphs.CycleGraph(3))
            sage: O = Matroid(graphs.ButterflyGraph())
            sage: P = Matroid(Graph([(0, 1, 'a'), (0, 2, 'b'), (1, 2, 'c')]))
            sage: M == N
            True
            sage: M == O
            False
            sage: M == P
            False

        A more subtle example where the vertex labels differ::

            sage: G1 = Graph([(0,1,0),(0,2,1),(1,2,2)])
            sage: G2 = Graph([(3,4,3),(3,5,4),(4,5,5),(4,6,6),(5,6,7)])
            sage: G = G1.disjoint_union(G2)
            sage: H = G2.disjoint_union(G1)
            sage: Matroid(G) == Matroid(H)
            False
            sage: Matroid(G).equals(Matroid(H))
            True

        Same except for vertex labels::

            sage: G1 = Graph([(0,1,0),(1,2,1),(2,0,2)])
            sage: G2 = Graph([(3,4,0),(4,5,1),(5,3,2)])
            sage: Matroid(G1) == Matroid(G2)
            False"""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __hash__(self) -> Any:
        """GraphicMatroid.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 334)

        Return an invariant of the matroid.

        This function is called when matroids are added to a set. It is very
        desirable to override it so it can distinguish matroids on the same
        groundset, which is a very typical use case!

        .. WARNING::

            This method is linked to ``__richcmp__`` (in Cython) and ``__cmp__``
            or ``__eq__``/``__ne__`` (in Python). If you override one, you
            should (and, in Cython, \\emph{must}) override the other!

        EXAMPLES::

            sage: M = Matroid(graphs.CompleteGraph(3))
            sage: N = Matroid(graphs.CycleGraph(3))
            sage: O = Matroid(graphs.ButterflyGraph())
            sage: hash(M) == hash(N)
            True
            sage: hash(O) == hash(N)
            False
            sage: P = Matroid(Graph([(0, 1, 'a'), (0, 2, 'b'), (1, 2, 'c')]))
            sage: hash(P) == hash(M)
            False"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other) -> Any:
        """GraphicMatroid.__ne__(self, other)

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 414)

        Compare two matroids.

        INPUT:

        - ``other`` -- matroid

        OUTPUT: ``False`` if ``self`` and ``other`` have the same graph;
        ``True`` otherwise

        EXAMPLES::

            sage: M = Matroid(range(4), graphs.CycleGraph(4))
            sage: N = Matroid(range(4), graphs.CompleteBipartiteGraph(2,2))
            sage: O = Matroid(graphs.PetersenGraph())
            sage: M != N
            True
            sage: M.equals(N)
            True
            sage: M != O
            True"""
    def __reduce__(self) -> Any:
        """GraphicMatroid.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/matroids/graphic_matroid.pyx (starting at line 441)

        Save the matroid for later reloading.

        EXAMPLES::

            sage: M = Matroid(graphs.PetersenGraph())
            sage: M == loads(dumps(M))
            True
            sage: loads(dumps(M))
            Graphic matroid of rank 9 on 15 elements"""
