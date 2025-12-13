from .generic_graph import GenericGraph as GenericGraph
from .graph import Graph as Graph
from _typeshed import Incomplete
from collections.abc import Generator
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.integer import Integer as Integer

class BipartiteGraph(Graph):
    '''
    Bipartite graph.

    INPUT:

    - ``data`` -- can be any of the following:

      #. Empty or ``None`` (creates an empty graph).

      #. An arbitrary graph.

      #. A reduced adjacency matrix.

         A reduced adjacency matrix contains only the non-redundant
         portion of the full adjacency matrix for the bipartite graph.
         Specifically, for zero matrices of the appropriate size, for
         the reduced adjacency matrix ``H``, the full adjacency matrix
         is ``[[0, H\'], [H, 0]]``. The columns correspond to vertices
         on the left, and the rows correspond to vertices on the
         right.

      #. A file in alist format.

         The alist file format is described at
         http://www.inference.phy.cam.ac.uk/mackay/codes/alist.html

      #. A ``graph6`` string (see documentation of :meth:`~graph6_string`).

      #. From a NetworkX bipartite graph.

    - ``partition`` -- (default: ``None``) a tuple defining vertices of the left
      and right partition of the graph. Partitions will be determined
      automatically if ``partition`` is ``None``.

    - ``check`` -- boolean (default: ``True``); if ``True``, an invalid input
      partition raises an exception. In the other case offending edges simply
      won\'t be included.

    - ``loops`` -- ignored; bipartite graphs cannot have loops

    - ``multiedges`` -- boolean (default: ``None``); whether to allow multiple
      edges

    - ``weighted`` -- boolean (default: ``None``); whether graph thinks of
      itself as weighted or not. See ``self.weighted()``

    - ``hash_labels`` -- boolean (default: ``None``); whether to include edge
      labels during hashing. This parameter defaults to ``True`` if the graph is
      weighted. This parameter is ignored if the graph is mutable.
      Beware that trying to hash unhashable labels will raise an error.

    .. NOTE::

        All remaining arguments are passed to the ``Graph`` constructor

    EXAMPLES:

    #. No inputs or ``None`` for the input creates an empty graph::

        sage: B = BipartiteGraph()
        sage: type(B)
        <class \'sage.graphs.bipartite_graph.BipartiteGraph\'>
        sage: B.order()
        0
        sage: B == BipartiteGraph(None)
        True

    #. From a graph: without any more information, finds a bipartition::

        sage: B = BipartiteGraph(graphs.CycleGraph(4))
        sage: B = BipartiteGraph(graphs.CycleGraph(5))
        Traceback (most recent call last):
        ...
        ValueError: input graph is not bipartite
        sage: G = Graph({0: [5, 6], 1: [4, 5], 2: [4, 6], 3: [4, 5, 6]})
        sage: B = BipartiteGraph(G)
        sage: B == G
        True
        sage: B.left
        {0, 1, 2, 3}
        sage: B.right
        {4, 5, 6}
        sage: B = BipartiteGraph({0: [5, 6], 1: [4, 5], 2: [4, 6], 3: [4, 5, 6]})
        sage: B == G
        True
        sage: B.left
        {0, 1, 2, 3}
        sage: B.right
        {4, 5, 6}

    #. If a ``Graph`` or ``DiGraph`` is used as data, you can specify
       a partition using ``partition`` argument. Note that if such
       graph is not bipartite, then Sage will raise an error. However,
       if one specifies ``check=False``, the offending edges are
       simply deleted (along with those vertices not appearing in
       either list).  We also lump creating one bipartite graph from
       another into this category::

        sage: P = graphs.PetersenGraph()
        sage: partition = [list(range(5)), list(range(5, 10))]
        sage: B = BipartiteGraph(P, partition)
        Traceback (most recent call last):
        ...
        TypeError: input graph is not bipartite with respect to the given partition

        sage: B = BipartiteGraph(P, partition, check=False)
        sage: B.left
        {0, 1, 2, 3, 4}
        sage: B.show()                                                                  # needs sage.plot

       ::

        sage: G = Graph({0: [5, 6], 1: [4, 5], 2: [4, 6], 3: [4, 5, 6]})
        sage: B = BipartiteGraph(G)
        sage: B2 = BipartiteGraph(B)
        sage: B == B2
        True
        sage: B3 = BipartiteGraph(G, [list(range(4)), list(range(4, 7))])
        sage: B3
        Bipartite graph on 7 vertices
        sage: B3 == B2
        True

       ::

        sage: G = Graph({0: [], 1: [], 2: []})
        sage: part = (list(range(2)), [2])
        sage: B = BipartiteGraph(G, part)
        sage: B2 = BipartiteGraph(B)
        sage: B == B2
        True

       ::

        sage: d = DiGraph(6)
        sage: d.add_edge(0, 1)
        sage: part=[[1, 2, 3], [0, 4, 5]]
        sage: b = BipartiteGraph(d, part)
        sage: b.left
        {1, 2, 3}
        sage: b.right
        {0, 4, 5}

    #. From a reduced adjacency matrix::

        sage: # needs sage.modules
        sage: M = Matrix([(1,1,1,0,0,0,0), (1,0,0,1,1,0,0),
        ....:             (0,1,0,1,0,1,0), (1,1,0,1,0,0,1)])
        sage: M
        [1 1 1 0 0 0 0]
        [1 0 0 1 1 0 0]
        [0 1 0 1 0 1 0]
        [1 1 0 1 0 0 1]
        sage: H = BipartiteGraph(M); H
        Bipartite graph on 11 vertices
        sage: H.edges(sort=True)
        [(0, 7, None),
         (0, 8, None),
         (0, 10, None),
         (1, 7, None),
         (1, 9, None),
         (1, 10, None),
         (2, 7, None),
         (3, 8, None),
         (3, 9, None),
         (3, 10, None),
         (4, 8, None),
         (5, 9, None),
         (6, 10, None)]

       ::

        sage: M = Matrix([(1, 1, 2, 0, 0), (0, 2, 1, 1, 1), (0, 1, 2, 1, 1)])           # needs sage.modules
        sage: B = BipartiteGraph(M, multiedges=True, sparse=True)                       # needs sage.modules
        sage: B.edges(sort=True)                                                        # needs sage.modules
        [(0, 5, None),
         (1, 5, None),
         (1, 6, None),
         (1, 6, None),
         (1, 7, None),
         (2, 5, None),
         (2, 5, None),
         (2, 6, None),
         (2, 7, None),
         (2, 7, None),
         (3, 6, None),
         (3, 7, None),
         (4, 6, None),
         (4, 7, None)]

       ::

         sage: # needs sage.modules sage.rings.finite_rings
         sage: F.<a> = GF(4)
         sage: MS = MatrixSpace(F, 2, 3)
         sage: M = MS.matrix([[0, 1, a + 1], [a, 1, 1]])
         sage: B = BipartiteGraph(M, weighted=True, sparse=True)
         sage: B.edges(sort=True)
         [(0, 4, a), (1, 3, 1), (1, 4, 1), (2, 3, a + 1), (2, 4, 1)]
         sage: B.weighted()
         True

    #. From an alist file::

         sage: import tempfile
         sage: with tempfile.NamedTemporaryFile(mode=\'w+t\') as f:
         ....:     _ = f.write("7 4 \\n 3 4 \\n 3 3 1 3 1 1 1 \\n\\\n         ....:                  3 3 3 4 \\n 1 2 4 \\n 1 3 4 \\n 1 0 0 \\n\\\n         ....:                  2 3 4 \\n 2 0 0 \\n 3 0 0 \\n 4 0 0 \\n\\\n         ....:                  1 2 3 0 \\n 1 4 5 0 \\n 2 4 6 0 \\n\\\n         ....:                  1 2 4 7 \\n")
         ....:     f.flush()
         ....:     B = BipartiteGraph(f.name)
         sage: B.is_isomorphic(H)                                                       # needs sage.modules
         True

    #. From a ``graph6`` string::

         sage: B = BipartiteGraph(\'Bo\')
         sage: B
         Bipartite graph on 3 vertices
         sage: B.left
         {0}
         sage: B.right
         {1, 2}

       ::

         sage: B = BipartiteGraph(\'F?^T_\\n\', format=\'graph6\')
         sage: B.vertices(sort=True)
         [0, 1, 2, 3, 4, 5, 6]
         sage: B.edges(sort=True)
         [(0, 5, None), (0, 6, None), (1, 4, None), (1, 5, None), (2, 4, None),
          (2, 6, None), (3, 4, None), (3, 5, None), (3, 6, None)]
         sage: B.left
         {0, 1, 2, 3}
         sage: B.right
         {4, 5, 6}

       ::
         sage: B = BipartiteGraph(\'Bo\', partition=[[0], [1, 2]])
         sage: B.left
         {0}
         sage: B.right
         {1, 2}

       ::

         sage: B = BipartiteGraph(\'F?^T_\\n\', partition=[[0, 1, 2], [3, 4, 5, 6]])
         Traceback (most recent call last):
         ...
         TypeError: input graph is not bipartite with respect to the given partition

         sage: B = BipartiteGraph(\'F?^T_\\n\', partition=[[0, 1, 2], [3, 4, 5, 6]], check=False)
         sage: B.left
         {0, 1, 2}
         sage: B.show()                                                                 # needs sage.plot

    #. From a NetworkX bipartite graph::

        sage: # needs networkx
        sage: import networkx
        sage: G = graphs.OctahedralGraph()
        sage: N = networkx.make_clique_bipartite(G.networkx_graph())
        sage: B = BipartiteGraph(N)

    TESTS:

    Make sure we can create a ``BipartiteGraph`` with keywords but no positional
    arguments (:issue:`10958`)::

        sage: B = BipartiteGraph(multiedges=True)
        sage: B.allows_multiple_edges()
        True

    Ensure that we can construct a ``BipartiteGraph`` with isolated vertices via
    the reduced adjacency matrix (:issue:`10356`)::

        sage: # needs sage.modules
        sage: a = BipartiteGraph(matrix(2, 2, [1, 0, 1, 0]))
        sage: a
        Bipartite graph on 4 vertices
        sage: a.vertices(sort=True)
        [0, 1, 2, 3]
        sage: g = BipartiteGraph(matrix(4, 4, [1] * 4 + [0] * 12))
        sage: g.vertices(sort=True)
        [0, 1, 2, 3, 4, 5, 6, 7]
        sage: sorted(g.left.union(g.right))
        [0, 1, 2, 3, 4, 5, 6, 7]

    Make sure that loops are not allowed (:issue:`23275`)::

        sage: B = BipartiteGraph(loops=True)
        Traceback (most recent call last):
        ...
        ValueError: loops are not allowed in bipartite graphs
        sage: B = BipartiteGraph(loops=None)
        sage: B.allows_loops()
        False
        sage: B.add_edge(0, 0)
        Traceback (most recent call last):
        ...
        ValueError: cannot add edge from 0 to 0 in graph without loops
    '''
    left: Incomplete
    right: Incomplete
    def __init__(self, data=None, partition=None, check: bool = True, hash_labels=None, *args, **kwds) -> None:
        """
        Create a bipartite graph.

        See documentation ``BipartiteGraph?`` for detailed information.

        EXAMPLES::

            sage: P = graphs.PetersenGraph()
            sage: partition = [list(range(5)), list(range(5, 10))]
            sage: B = BipartiteGraph(P, partition, check=False)

        TESTS:

        Check that :issue:`33249` is fixed::

            sage: G = BipartiteGraph({2:[1], 3:[1], 4:[5]}, partition=([2,3,4],[1,5]))
            sage: print(G.left, G.right)
            {2, 3, 4} {1, 5}
            sage: G = BipartiteGraph({2:[1], 3:[1]}, partition=([1,2],[3]), check=True)
            Traceback (most recent call last):
            ...
            TypeError: input graph is not bipartite with respect to the given partition
            sage: G = BipartiteGraph({2:[1], 3:[1], 4:[5]}, partition=([2,3,4],[1]))
            Traceback (most recent call last):
            ...
            ValueError: not all vertices appear in partition
            sage: G = BipartiteGraph({2:[1], 3:[1], 4:[5]}, partition=([2,3,4],[1, 2]))
            Traceback (most recent call last):
            ...
            ValueError: the parts are not disjoint
            sage: G = BipartiteGraph({2:[1], 3:[1], 4:[5]}, partition=([2, 3, 4], [1, 7]))
            Traceback (most recent call last):
            ...
            LookupError: vertex (7) is not a vertex of the graph

        Check that :issue:`39295` is fixed::

            sage: B = BipartiteGraph(matrix([[1, 1], [1, 1]]), immutable=True)
            sage: print(B.vertices(), B.edges())
            [0, 1, 2, 3] [(0, 2, None), (0, 3, None), (1, 2, None), (1, 3, None)]
            sage: B.add_vertices([4], left=True)
            Traceback (most recent call last):
            ...
            TypeError: this graph is immutable and so cannot be changed
        """
    @cached_method
    def __hash__(self):
        """
        Compute a hash for ``self``, if ``self`` is immutable.

        EXAMPLES::

            sage: A = BipartiteGraph([(1, 2, 1)], immutable=True)
            sage: B = BipartiteGraph([(1, 2, 33)], immutable=True)
            sage: A.__hash__() == B.__hash__()
            True
            sage: A = BipartiteGraph([(1, 2, 1)], immutable=True, hash_labels=True)
            sage: B = BipartiteGraph([(1, 2, 33)], immutable=True, hash_labels=True)
            sage: A.__hash__() == B.__hash__()
            False
            sage: A = BipartiteGraph([(1, 2, 1)], immutable=True, weighted=True)
            sage: B = BipartiteGraph([(1, 2, 33)], immutable=True, weighted=True)
            sage: A.__hash__() == B.__hash__()
            False

        TESTS::

            sage: A = BipartiteGraph([(1, 2, 1)], immutable=False)
            sage: A.__hash__()
            Traceback (most recent call last):
            ...
            TypeError: This graph is mutable, and thus not hashable. Create an immutable copy by `g.copy(immutable=True)`
            sage: B = BipartiteGraph([(1, 2, {'length': 3})], immutable=True, hash_labels=True)
            sage: B.__hash__()
            Traceback (most recent call last):
            ...
            TypeError: unhashable type: 'dict'
        """
    def add_vertex(self, name=None, left: bool = False, right: bool = False):
        """
        Create an isolated vertex. If the vertex already exists, then
        nothing is done.

        INPUT:

        - ``name`` -- (default: ``None``) name of the new vertex. If no name is
          specified, then the vertex will be represented by the least
          nonnegative integer not already representing a vertex. Name must be
          an immutable object and cannot be ``None``.

        - ``left`` -- boolean (default: ``False``); if ``True``, puts the new
          vertex in the left partition

        - ``right`` -- boolean (default: ``False``); if ``True``, puts the new
          vertex in the right partition

        Obviously, ``left`` and ``right`` are mutually exclusive.

        As it is implemented now, if a graph `G` has a large number of vertices
        with numeric labels, then ``G.add_vertex()`` could potentially be slow,
        if name is ``None``.

        OUTPUT:

        - If ``name`` is ``None``, the new vertex name is returned. ``None``
          otherwise.

        EXAMPLES::

            sage: G = BipartiteGraph()
            sage: G.add_vertex(left=True)
            0
            sage: G.add_vertex(right=True)
            1
            sage: G.vertices(sort=True)
            [0, 1]
            sage: G.left
            {0}
            sage: G.right
            {1}

        TESTS:

        Exactly one of ``left`` and ``right`` must be true::

            sage: G = BipartiteGraph()
            sage: G.add_vertex()
            Traceback (most recent call last):
            ...
            RuntimeError: partition must be specified (e.g. left=True)
            sage: G.add_vertex(left=True, right=True)
            Traceback (most recent call last):
            ...
            RuntimeError: only one partition may be specified

        Adding the same vertex must specify the same partition::

            sage: bg = BipartiteGraph()
            sage: bg.add_vertex(0, right=True)
            sage: bg.add_vertex(0, right=True)
            sage: bg.vertices(sort=False)
            [0]
            sage: bg.add_vertex(0, left=True)
            Traceback (most recent call last):
            ...
            RuntimeError: cannot add duplicate vertex to other partition
        """
    def add_vertices(self, vertices, left: bool = False, right: bool = False) -> None:
        """
        Add vertices to the bipartite graph from an iterable container of
        vertices.

        Vertices that already exist in the graph will not be added again.

        INPUT:

        - ``vertices`` -- sequence of vertices to add

        - ``left`` -- (default: ``False``) either ``True`` or sequence of same
          length as ``vertices`` with boolean elements

        - ``right`` -- (default: ``False``) either ``True`` or sequence of the
          same length as ``vertices`` with boolean elements

        Only one of ``left`` and ``right`` keywords should be provided.  See
        the examples below.

        EXAMPLES::

            sage: bg = BipartiteGraph()
            sage: bg.add_vertices([0, 1, 2], left=True)
            sage: bg.add_vertices([3, 4, 5], left=[True, False, True])
            sage: bg.add_vertices([6, 7, 8], right=[True, False, True])
            sage: bg.add_vertices([9, 10, 11], right=True)
            sage: bg.left
            {0, 1, 2, 3, 5, 7}
            sage: bg.right
            {4, 6, 8, 9, 10, 11}

        TESTS::

            sage: bg = BipartiteGraph()
            sage: bg.add_vertices([0, 1, 2], left=True)
            sage: bg.add_vertices([0, 1, 2], left=[True, True, True])
            sage: bg.add_vertices([0, 1, 2], right=[False, False, False])
            sage: bg.add_vertices([0, 1, 2], right=[False, False, False])
            sage: bg.add_vertices([0, 1, 2])
            Traceback (most recent call last):
            ...
            RuntimeError: partition must be specified (e.g. left=True)
            sage: bg.add_vertices([0,1,2], left=True, right=True)
            Traceback (most recent call last):
            ...
            RuntimeError: only one partition may be specified
            sage: bg.add_vertices([0,1,2], right=True)
            Traceback (most recent call last):
            ...
            RuntimeError: cannot add duplicate vertex to other partition
            sage: (bg.left, bg.right)
            ({0, 1, 2}, set())
        """
    def delete_vertex(self, vertex, in_order: bool = False) -> None:
        """
        Delete vertex, removing all incident edges.

        Deleting a non-existent vertex will raise an exception.

        INPUT:

        - ``vertex`` -- a vertex to delete

        - ``in_order`` -- boolean (default: ``False``); if ``True``, deletes the
          `i`-th vertex in the sorted list of vertices,
          i.e. ``G.vertices(sort=True)[i]``

        EXAMPLES::

            sage: B = BipartiteGraph(graphs.CycleGraph(4))
            sage: B
            Bipartite cycle graph: graph on 4 vertices
            sage: B.delete_vertex(0)
            sage: B
            Bipartite cycle graph: graph on 3 vertices
            sage: B.left
            {2}
            sage: B.edges(sort=True)
            [(1, 2, None), (2, 3, None)]
            sage: B.delete_vertex(3)
            sage: B.right
            {1}
            sage: B.edges(sort=True)
            [(1, 2, None)]
            sage: B.delete_vertex(0)
            Traceback (most recent call last):
            ...
            ValueError: vertex (0) not in the graph

        ::

            sage: g = Graph({'a': ['b'], 'c': ['b']})
            sage: bg = BipartiteGraph(g)  # finds bipartition
            sage: bg.vertices(sort=True)
            ['a', 'b', 'c']
            sage: bg.delete_vertex('a')
            sage: bg.edges(sort=True)
            [('b', 'c', None)]
            sage: bg.vertices(sort=True)
            ['b', 'c']
            sage: bg2 = BipartiteGraph(g)
            sage: bg2.delete_vertex(0, in_order=True)
            sage: bg2 == bg
            True
        """
    def delete_vertices(self, vertices) -> None:
        """
        Remove vertices from the bipartite graph taken from an iterable
        sequence of vertices.

        Deleting a non-existent vertex will raise an exception.

        INPUT:

        - ``vertices`` -- a sequence of vertices to remove

        EXAMPLES::

            sage: B = BipartiteGraph(graphs.CycleGraph(4))
            sage: B
            Bipartite cycle graph: graph on 4 vertices
            sage: B.delete_vertices([0, 3])
            sage: B
            Bipartite cycle graph: graph on 2 vertices
            sage: B.left
            {2}
            sage: B.right
            {1}
            sage: B.edges(sort=True)
            [(1, 2, None)]
            sage: B.delete_vertices([0])
            Traceback (most recent call last):
            ...
            ValueError: vertex (0) not in the graph
        """
    def add_edge(self, u, v=None, label=None) -> None:
        '''
        Add an edge from `u` to `v`.

        INPUT:

        - ``u`` -- the tail of an edge

        - ``v`` -- (default: ``None``) the head of an edge. If ``v=None``, then
          attempt to understand ``u`` as a edge tuple

        - ``label`` -- (default: ``None``) the label of the edge ``(u, v)``

        The following forms are all accepted:

        - ``G.add_edge(1, 2)``
        - ``G.add_edge((1, 2))``
        - ``G.add_edges([(1, 2)])``
        - ``G.add_edge(1, 2, \'label\')``
        - ``G.add_edge((1, 2, \'label\'))``
        - ``G.add_edges([(1, 2, \'label\')])``

        See :meth:`~sage.graphs.graph.Graph.add_edge` for more detail.

        This method simply checks that the edge endpoints are in different
        partitions. If a new vertex is to be created, it will be added to the
        proper partition. If both vertices are created, the first one will be
        added to the left partition, the second to the right partition. If
        both vertices are in the same partition but different connected
        components, one of the components will be "flipped", i.e. each vertex
        will be put into whichever partition it\'s not currently in. This will
        allow for the graph to remain bipartite, without changing the edges or
        vertices.

        TESTS::

            sage: bg = BipartiteGraph()
            sage: bg.add_vertices([0, 1, 2], left=[True, False, True])
            sage: bg.add_edges([(0, 1), (2, 1)])
            sage: bg.add_edge(0, 2)
            Traceback (most recent call last):
            ...
            RuntimeError: edge vertices must lie in different partitions
            sage: bg.add_edge(0, 3); list(bg.right)
            [1, 3]
            sage: bg.add_edge(5, 6); 5 in bg.left; 6 in bg.right
            True
            True
            sage: G = BipartiteGraph()
            sage: G.add_edges([(0, 1), (3, 2)])
            sage: G.bipartition()
            ({0, 3}, {1, 2})
            sage: G.add_edge(1,2)
            sage: G.bipartition()
            ({0, 2}, {1, 3})
        '''
    def add_edges(self, edges, loops: bool = True) -> None:
        '''
        Add edges from an iterable container.

        INPUT:

        - ``edges`` -- an iterable of edges, given either as ``(u, v)``
          or ``(u, v, label)``

        - ``loops`` -- ignored

        See :meth:`~sage.graphs.graph.Graph.add_edges` for more detail.

        This method simply checks that the edge endpoints are in different
        partitions. If a new vertex is to be created, it will be added to the
        proper partition. If both vertices are created, the first one will be
        added to the left partition, the second to the right partition. If
        both vertices are in the same partition but different connected
        components, one of the components will be "flipped", i.e. each vertex
        will be put into whichever partition it\'s not currently in. This will
        allow for the graph to remain bipartite, without changing the edges or
        vertices.

        EXAMPLES::

            sage: bg = BipartiteGraph()
            sage: bg.add_vertices([0, 1, 2], left=[True, False, True])
            sage: bg.add_edges([(0, 1), (2, 1)])
            sage: bg.add_edges([[0, 2]])
            Traceback (most recent call last):
            ...
            ValueError: the specified set of edges cannot be added
            while still preserving the bipartition property
            sage: G = BipartiteGraph()
            sage: G.add_edges([(0, 1), (3, 2), (1, 2)])
            sage: G.bipartition()
            ({0, 2}, {1, 3})


        Loops will raise an error::

            sage: bg.add_edges([[0, 3], [3, 3]])
            Traceback (most recent call last):
            ...
            ValueError: the specified set of edges cannot be added
            while still preserving the bipartition property

        Adding edges is fine as long as there exists a valid bipartition.
        Otherwise an error is raised without modifyiong the graph::

            sage: G = BipartiteGraph()
            sage: G.add_edges([(0, 1), (2, 3)])
            sage: G.bipartition()
            ({0, 2}, {1, 3})
            sage: G.add_edges([(0,2), (0,3)])
            Traceback (most recent call last):
            ...
            ValueError: the specified set of edges cannot be added
            while still preserving the bipartition property
            sage: G.bipartition()
            ({0, 2}, {1, 3})
            sage: G.edges(labels=False, sort=True)
            [(0, 1), (2, 3)]
        '''
    def allow_loops(self, new, check: bool = True) -> None:
        """
        Change whether loops are permitted in the (di)graph.

        .. NOTE::

            This method overwrite the
            :meth:`~sage.graphs.generic_graph.GenericGraph.allow_loops` method
            to ensure that loops are forbidden in :class:`~BipartiteGraph`.

        INPUT:

        - ``new`` -- boolean

        EXAMPLES::

            sage: B = BipartiteGraph()
            sage: B.allow_loops(True)
            Traceback (most recent call last):
            ...
            ValueError: loops are not allowed in bipartite graphs
        """
    def is_bipartite(self, certificate: bool = False):
        """
        Check whether the graph is bipartite.

        This method always returns ``True`` as first value, plus a certificate
        when ``certificate == True``.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); whether to return a
          certificate. If set to ``True``, the certificate returned is a proper
          2-coloring of the vertices.

        .. SEEALSO:: :meth:`~GenericGraph.is_bipartite`

        EXAMPLES::

            sage: g = BipartiteGraph(graphs.RandomBipartite(3, 3, .5))                  # needs numpy
            sage: g.is_bipartite()                                                      # needs numpy
            True
            sage: g.is_bipartite(certificate=True)  # random                            # needs numpy
            (True, {(0, 0): 0, (0, 1): 0, (0, 2): 0, (1, 0): 1, (1, 1): 1, (1, 2): 1})

        TESTS::

            sage: BipartiteGraph().is_bipartite()
            True
            sage: BipartiteGraph().is_bipartite(certificate=True)
            (True, {})
        """
    def complement(self):
        """
        Return a complement of this graph.

        Given a simple :class:`~sage.graphs.bipartite_graph.BipartiteGraph`
        `G = (L, R, E)` with vertex set `L\\cup R` and edge set `E`, this method
        returns a :class:`~sage.graphs.graph.Graph` `H = (V, F)`, where
        `V = L\\cup R` and `F` is the set of edges of a complete graph of order
        `|V|` minus the edges in `E`.

        .. WARNING::

            This method returns the complement of a bipartite graph
            `G = (V = L \\cup R, E)` with respect the complete graph of order
            `|V|`. If looking for the complement with respect the complete
            bipartite graph `K = (L, R, L\\times R)`, use method
            :meth:`~sage.graphs.bipartite_graph.BipartiteGraph.complement_bipartite`.

        .. SEEALSO::

            :meth:`~sage.graphs.bipartite_graph.BipartiteGraph.complement_bipartite`

        EXAMPLES::

            sage: B = BipartiteGraph({1: [2, 4], 3: [4, 5]})
            sage: G = B.complement(); G
            Graph on 5 vertices
            sage: G.edges(sort=True, labels=False)
            [(1, 3), (1, 5), (2, 3), (2, 4), (2, 5), (4, 5)]
            sage: B.size() + G.size() == graphs.CompleteGraph(B.order()).size()
            True
        """
    def complement_bipartite(self):
        """
        Return the bipartite complement of this bipartite graph.

        Given a simple :class:`~sage.graphs.bipartite_graph.BipartiteGraph`
        `G = (L, R, E)` with vertex set `L\\cup R` and edge set `E`, this
        method returns a :class:`~sage.graphs.bipartite_graph.BipartiteGraph`
        `H = (L\\cup R, F)`, where `F` is the set of edges of a complete
        bipartite graph between vertex sets `L` and `R` minus the edges in `E`.

        .. SEEALSO::

            :meth:`~sage.graphs.bipartite_graph.BipartiteGraph.complement`

        EXAMPLES:

            sage: B = BipartiteGraph({0: [1, 2, 3]})
            sage: C = B.complement_bipartite()
            sage: C
            Bipartite graph on 4 vertices
            sage: C.is_bipartite()
            True
            sage: B.left == C.left and B.right == C.right
            True
            sage: C.size() == len(B.left)*len(B.right) - B.size()
            True
            sage: G = B.complement()
            sage: G.is_bipartite()
            False
        """
    def to_undirected(self):
        """
        Return an undirected Graph (without bipartite constraint) of the given
        object.

        EXAMPLES::

            sage: BipartiteGraph(graphs.CycleGraph(6)).to_undirected()
            Cycle graph: Graph on 6 vertices
        """
    def bipartition(self):
        """
        Return the underlying bipartition of the bipartite graph.

        EXAMPLES::

            sage: B = BipartiteGraph(graphs.CycleGraph(4))
            sage: B.bipartition()
            ({0, 2}, {1, 3})
        """
    def project_left(self):
        """
        Project ``self`` onto left vertices. Edges are 2-paths in the original.

        EXAMPLES::

            sage: B = BipartiteGraph(graphs.CycleGraph(20))
            sage: G = B.project_left()
            sage: G.order(), G.size()
            (10, 10)
        """
    def project_right(self):
        """
        Project ``self`` onto right vertices. Edges are 2-paths in the original.

        EXAMPLES::

            sage: B = BipartiteGraph(graphs.CycleGraph(20))
            sage: G = B.project_right()
            sage: G.order(), G.size()
            (10, 10)

        TESTS:

        Issue :issue:`25985` is fixed::

            sage: B = BipartiteGraph(graphs.CycleGraph(6))
            sage: B.project_left().vertices(sort=True)
            [0, 2, 4]
            sage: B.project_right().vertices(sort=True)
            [1, 3, 5]
        """
    def plot(self, *args, **kwds):
        """
        Override Graph's plot function, to illustrate the bipartite nature.

        EXAMPLES::

            sage: B = BipartiteGraph(graphs.CycleGraph(20))
            sage: B.plot()                                                              # needs sage.plot
            Graphics object consisting of 41 graphics primitives
        """
    def matching_polynomial(self, algorithm: str = 'Godsil', name=None):
        '''
        Compute the matching polynomial.

        The *matching polynomial* is defined as in [God1993]_, where `p(G, k)`
        denotes the number of `k`-matchings (matchings with `k` edges) in `G` :

        .. MATH::

            \\mu(x)=\\sum_{k \\geq 0} (-1)^k p(G,k) x^{n-2k}

        INPUT:

        - ``algorithm`` -- string (default: ``\'Godsil\'``); either "Godsil" or
          "rook"; "rook" is usually faster for larger graphs

        - ``name`` -- string (default: ``None``); name of the variable in the
          polynomial, set to `x` when ``name`` is ``None``

        EXAMPLES::

            sage: BipartiteGraph(graphs.CubeGraph(3)).matching_polynomial()             # needs sage.libs.flint
            x^8 - 12*x^6 + 42*x^4 - 44*x^2 + 9

        ::

            sage: x = polygen(QQ)
            sage: g = BipartiteGraph(graphs.CompleteBipartiteGraph(16, 16))
            sage: bool(factorial(16) * laguerre(16, x^2)                                # needs sage.symbolic
            ....:       == g.matching_polynomial(algorithm=\'rook\'))
            True

        Compute the matching polynomial of a line with `60` vertices::

            sage: from sage.functions.orthogonal_polys import chebyshev_U               # needs sage.symbolic
            sage: g = next(graphs.trees(60))
            sage: (chebyshev_U(60, x/2)                                                 # needs sage.symbolic
            ....:   == BipartiteGraph(g).matching_polynomial(algorithm=\'rook\'))
            True

        The matching polynomial of a tree is equal to its characteristic
        polynomial::

            sage: g = graphs.RandomTree(20)
            sage: p = g.characteristic_polynomial()                                     # needs sage.modules
            sage: p == BipartiteGraph(g).matching_polynomial(algorithm=\'rook\')          # needs sage.modules
            True

        TESTS::

            sage: # needs sage.modules
            sage: g = BipartiteGraph(matrix.ones(4, 3))
            sage: g.matching_polynomial()                                               # needs sage.libs.flint
            x^7 - 12*x^5 + 36*x^3 - 24*x
            sage: g.matching_polynomial(algorithm=\'rook\')
            x^7 - 12*x^5 + 36*x^3 - 24*x
        '''
    def perfect_matchings(self, labels: bool = False) -> Generator[Incomplete, Incomplete]:
        """
        Return an iterator over all perfect matchings of the bipartite graph.

        ALGORITHM:

        Choose a vertex `v` in the right set of vertices, then recurse through
        all edges incident to `v`, removing one edge at a time whenever an edge
        is added to a matching.

        INPUT:

        - ``labels`` -- boolean (default: ``False``); when ``True``, the edges
          in each perfect matching are triples (containing the label as the
          third element), otherwise the edges are pairs.

        .. SEEALSO::

            :meth:`~sage.graphs.graph.Graph.perfect_matchings`
            :meth:`matching`

        EXAMPLES::

            sage: B = BipartiteGraph({0: [5, 7], 1: [4, 6, 7], 2: [4, 5, 8],
            ....:                     3: [4, 5, 6], 6: [9], 8: [9]})
            sage: len(list(B.perfect_matchings()))
            6
            sage: G = Graph(B.edges(sort=False))
            sage: len(list(G.perfect_matchings()))
            6

        The algorithm ensures that for any edge of a perfect matching, the first
        vertex is on the left set of vertices and the second vertex in the right
        set::

            sage: B = BipartiteGraph({0: [5, 7], 1: [4, 6, 7], 2: [4, 5, 8],
            ....:                     3: [4, 5, 6], 6: [9], 8: [9]})
            sage: m = next(B.perfect_matchings(labels=False))
            sage: B.left
            {0, 1, 2, 3, 9}
            sage: B.right
            {4, 5, 6, 7, 8}
            sage: sorted(m)
            [(0, 7), (1, 4), (2, 5), (3, 6), (9, 8)]
            sage: all((u in B.left and v in B.right) for u, v in m)
            True

        Multiple edges are taken into account::

            sage: B = BipartiteGraph({0: [5, 7], 1: [4, 6, 7], 2: [4, 5, 8],
            ....:                     3: [4, 5, 6], 6: [9], 8: [9]})
            sage: B.allow_multiple_edges(True)
            sage: B.add_edge(0, 7)
            sage: len(list(B.perfect_matchings()))
            10


        Empty graph::

            sage: list(BipartiteGraph().perfect_matchings())
            [[]]

        Bipartite graph without perfect matching::

            sage: B = BipartiteGraph(graphs.CompleteBipartiteGraph(3, 4))
            sage: list(B.perfect_matchings())
            []

        Check that the number of perfect matchings of a complete bipartite graph
        is consistent with the matching polynomial::

            sage: B = BipartiteGraph(graphs.CompleteBipartiteGraph(4, 4))
            sage: len(list(B.perfect_matchings()))
            24
            sage: B.matching_polynomial(algorithm='rook')(0)                            # needs sage.modules
            24

        TESTS::

            sage: B = BipartiteGraph(graphs.CompleteBipartiteGraph(3, 4))
            sage: B.left, B.right
            ({0, 1, 2}, {3, 4, 5, 6})
            sage: B.add_vertex(left=True)
            7
            sage: B.left, B.right
            ({0, 1, 2, 7}, {3, 4, 5, 6})
            sage: list(B.perfect_matchings())
            []
            sage: B = BipartiteGraph(graphs.CompleteBipartiteGraph(3, 3))
            sage: B.add_vertex(left=True)
            6
            sage: B.add_vertex(right=True)
            7
            sage: list(B.perfect_matchings())
            []
            sage: G = Graph(B)
            sage: list(G.perfect_matchings())
            []
        """
    def load_afile(self, fname):
        '''
        Load into the current object the bipartite graph specified in the given
        file name.

        This file should follow David MacKay\'s alist format, see
        http://www.inference.phy.cam.ac.uk/mackay/codes/data.html for examples
        and definition of the format.

        EXAMPLES::

            sage: import tempfile
            sage: with tempfile.NamedTemporaryFile(mode=\'w+t\') as f:
            ....:     _ = f.write("7 4 \\n 3 4 \\n 3 3 1 3 1 1 1 \\n\\\n            ....:                 3 3 3 4 \\n 1 2 4 \\n 1 3 4 \\n\\\n            ....:                 1 0 0 \\n 2 3 4 \\n 2 0 0 \\n 3 0 0 \\n\\\n            ....:                 4 0 0 \\n 1 2 3 0 \\n 1 4 5 0 \\n\\\n            ....:                 2 4 6 0 \\n 1 2 4 7 \\n")
            ....:     f.flush()
            ....:     B = BipartiteGraph()
            ....:     B2 = BipartiteGraph(f.name)
            ....:     B.load_afile(f.name)
            Bipartite graph on 11 vertices
            sage: B.edges(sort=True)
            [(0, 7, None),
             (0, 8, None),
             (0, 10, None),
             (1, 7, None),
             (1, 9, None),
             (1, 10, None),
             (2, 7, None),
             (3, 8, None),
             (3, 9, None),
             (3, 10, None),
             (4, 8, None),
             (5, 9, None),
             (6, 10, None)]
             sage: B2 == B
             True
        '''
    def save_afile(self, fname):
        '''
        Save the graph to file in alist format.

        Saves this graph to file in David MacKay\'s alist format, see
        http://www.inference.phy.cam.ac.uk/mackay/codes/data.html
        for examples and definition of the format.

        EXAMPLES::

            sage: # needs sage.modules
            sage: M = Matrix([(1,1,1,0,0,0,0), (1,0,0,1,1,0,0),
            ....:             (0,1,0,1,0,1,0), (1,1,0,1,0,0,1)])
            sage: M
            [1 1 1 0 0 0 0]
            [1 0 0 1 1 0 0]
            [0 1 0 1 0 1 0]
            [1 1 0 1 0 0 1]
            sage: b = BipartiteGraph(M)
            sage: import tempfile
            sage: with tempfile.NamedTemporaryFile() as f:
            ....:     b.save_afile(f.name)
            ....:     b2 = BipartiteGraph(f.name)
            sage: b.is_isomorphic(b2)
            True

        TESTS::

            sage: import tempfile
            sage: f = tempfile.NamedTemporaryFile()
            sage: for order in range(3, 13, 3):                                         # needs sage.combinat
            ....:     num_chks = int(order / 3)
            ....:     num_vars = order - num_chks
            ....:     partition = (list(range(num_vars)), list(range(num_vars, num_vars+num_chks)))
            ....:     for idx in range(100):
            ....:         g = graphs.RandomGNP(order, 0.5)
            ....:         try:
            ....:             b = BipartiteGraph(g, partition, check=False)
            ....:             b.save_afile(f.name)
            ....:             b2 = BipartiteGraph(f.name)
            ....:             if not b.is_isomorphic(b2):
            ....:                 print("Load/save failed for code with edges:")
            ....:                 print(b.edges(sort=True))
            ....:                 break
            ....:         except Exception:
            ....:             print("Exception encountered for graph of order "+ str(order))
            ....:             print("with edges: ")
            ....:             g.edges(sort=True)
            ....:             raise
            sage: f.close()  # this removes the file
        '''
    def reduced_adjacency_matrix(self, sparse: bool = True, *, base_ring=None, **kwds):
        """
        Return the reduced adjacency matrix for the given graph.

        A reduced adjacency matrix contains only the non-redundant portion of
        the full adjacency matrix for the bipartite graph.  Specifically, for
        zero matrices of the appropriate size, for the reduced adjacency
        matrix ``H``, the full adjacency matrix is ``[[0, H'], [H, 0]]``.

        By default, the matrix returned is over the integers.

        INPUT:

        - ``sparse`` -- boolean (default: ``True``); whether to return a sparse
          matrix

        - ``base_ring`` -- a ring (default: ``None``); the base ring of the
          matrix space to use. By default, the base ring is ``ZZ`` if the graph
          is not weighted and otherwise the same ring as the (first) weights.

        - ``**kwds`` -- other keywords to pass to
          :func:`~sage.matrix.constructor.matrix`

        EXAMPLES:

        Bipartite graphs that are not weighted will return a matrix over ZZ,
        unless a base ring is specified::

            sage: # needs sage.modules
            sage: M = Matrix([(1,1,1,0,0,0,0), (1,0,0,1,1,0,0),
            ....:             (0,1,0,1,0,1,0), (1,1,0,1,0,0,1)])
            sage: B = BipartiteGraph(M)
            sage: N = B.reduced_adjacency_matrix(); N
            [1 1 1 0 0 0 0]
            [1 0 0 1 1 0 0]
            [0 1 0 1 0 1 0]
            [1 1 0 1 0 0 1]
            sage: N == M
            True
            sage: N[0,0].parent()
            Integer Ring
            sage: N2 = B.reduced_adjacency_matrix(base_ring=RDF); N2
            [1.0 1.0 1.0 0.0 0.0 0.0 0.0]
            [1.0 0.0 0.0 1.0 1.0 0.0 0.0]
            [0.0 1.0 0.0 1.0 0.0 1.0 0.0]
            [1.0 1.0 0.0 1.0 0.0 0.0 1.0]
            sage: N2[0, 0].parent()
            Real Double Field

        Multi-edge graphs also return a matrix over ZZ,
        unless a base ring is specified::

            sage: # needs sage.modules
            sage: M = Matrix([(1,1,2,0,0), (0,2,1,1,1), (0,1,2,1,1)])
            sage: B = BipartiteGraph(M, multiedges=True, sparse=True)
            sage: N = B.reduced_adjacency_matrix()
            sage: N == M
            True
            sage: N[0,0].parent()
            Integer Ring
            sage: N2 = B.reduced_adjacency_matrix(base_ring=RDF)
            sage: N2[0, 0].parent()
            Real Double Field

        Weighted graphs will return a matrix over the ring given by their
        (first) weights, unless a base ring is specified::

            sage: # needs sage.modules sage.rings.finite_rings
            sage: F.<a> = GF(4)
            sage: MS = MatrixSpace(F, 2, 3)
            sage: M = MS.matrix([[0, 1, a+1], [a, 1, 1]])
            sage: B = BipartiteGraph(M, weighted=True, sparse=True)
            sage: N = B.reduced_adjacency_matrix(sparse=False)
            sage: N == M
            True
            sage: N[0,0].parent()
            Finite Field in a of size 2^2
            sage: N2 = B.reduced_adjacency_matrix(base_ring=F)
            sage: N2[0, 0].parent()
            Finite Field in a of size 2^2

        TESTS::

            sage: B = BipartiteGraph()
            sage: B.reduced_adjacency_matrix()                                          # needs sage.modules
            []
            sage: M = Matrix([[0,0], [0,0]])                                            # needs sage.modules
            sage: BipartiteGraph(M).reduced_adjacency_matrix() == M                     # needs sage.modules
            True
            sage: M = Matrix([[10,2/3], [0,0]])                                         # needs sage.modules
            sage: B = BipartiteGraph(M, weighted=True, sparse=True)                     # needs sage.modules
            sage: M == B.reduced_adjacency_matrix()                                     # needs sage.modules
            True

        An error is raised if the specified base ring is not compatible with the
        type of the weights of the bipartite graph::

            sage: # needs sage.modules sage.rings.finite_rings
            sage: F.<a> = GF(4)
            sage: MS = MatrixSpace(F, 2, 3)
            sage: M = MS.matrix([[0, 1, a+1], [a, 1, 1]])
            sage: B = BipartiteGraph(M, weighted=True, sparse=True)
            sage: B.reduced_adjacency_matrix(base_ring=RDF)
            Traceback (most recent call last):
            ...
            TypeError: float() argument must be a string or a ...number, not 'sage.rings.finite_rings.element_givaro.FiniteField_givaroElement'
        """
    def matching(self, value_only: bool = False, algorithm=None, use_edge_labels: bool = False, solver=None, verbose: int = 0, *, integrality_tolerance: float = 0.001):
        '''
        Return a maximum matching of the graph represented by the list of its
        edges.

        Given a graph `G` such that each edge `e` has a weight `w_e`, a maximum
        matching is a subset `S` of the edges of `G` of maximum weight such that
        no two edges of `S` are incident with each other.

        INPUT:

        - ``value_only`` -- boolean (default: ``False``); when set to ``True``,
          only the cardinal (or the weight) of the matching is returned

        - ``algorithm`` -- string (default: ``\'Hopcroft-Karp\'`` if
          ``use_edge_labels==False``, otherwise ``\'Edmonds\'``); algorithm to use
          among:

          - ``\'Hopcroft-Karp\'`` selects the default bipartite graph algorithm as
            implemented in NetworkX

          - ``\'Eppstein\'`` selects Eppstein\'s algorithm as implemented in
            NetworkX

          - ``\'Edmonds\'`` selects Edmonds\' algorithm as implemented in NetworkX

          - ``\'LP\'`` uses a Linear Program formulation of the matching problem

        - ``use_edge_labels`` -- boolean (default: ``False``)

          - when set to ``True``, computes a weighted matching where each edge
            is weighted by its label (if an edge has no label, `1` is assumed);
            only if ``algorithm`` is ``\'Edmonds\'``, ``\'LP\'``

          - when set to ``False``, each edge has weight `1`

        - ``solver`` -- string (default: ``None``); specifies a Mixed
          Integer Linear Programming (MILP) solver to be used. If set
          to ``None``, the default one is used. For more information
          on MILP solvers and which default solver is used, see the
          method :meth:`solve
          <sage.numerical.mip.MixedIntegerLinearProgram.solve>` of the
          class :class:`MixedIntegerLinearProgram
          <sage.numerical.mip.MixedIntegerLinearProgram>`.

        - ``verbose`` -- integer (default: 0); sets the level of
          verbosity. Set to 0 by default, which means quiet.

        - ``integrality_tolerance`` -- float; parameter for use with
          MILP solvers over an inexact base ring; see
          :meth:`MixedIntegerLinearProgram.get_values`.

        .. SEEALSO::

            - :wikipedia:`Matching_(graph_theory)`
            - :meth:`~Graph.matching`

        EXAMPLES:

        Maximum matching in a cycle graph::

            sage: G = BipartiteGraph(graphs.CycleGraph(10))
            sage: G.matching()                                                          # needs networkx
            [(0, 1, None), (2, 3, None), (4, 5, None), (6, 7, None), (8, 9, None)]

        The size of a maximum matching in a complete bipartite graph using
        Eppstein::

            sage: G = BipartiteGraph(graphs.CompleteBipartiteGraph(4,5))
            sage: G.matching(algorithm=\'Eppstein\', value_only=True)                     # needs networkx
            4

        TESTS:

        If ``algorithm`` is not set to one of the supported algorithms, an
        exception is raised::

            sage: G = BipartiteGraph(graphs.CompleteBipartiteGraph(4,5))
            sage: G.matching(algorithm=\'somethingdifferent\')
            Traceback (most recent call last):
            ...
            ValueError: algorithm must be "Hopcroft-Karp", "Eppstein", "Edmonds" or "LP"

        Maximum matching in a weighted bipartite graph::

            sage: G = graphs.CycleGraph(4)
            sage: B = BipartiteGraph([(u,v,2) for u,v in G.edges(sort=True, labels=0)])
            sage: sorted(B.matching(use_edge_labels=True))                              # needs networkx
            [(0, 3, 2), (1, 2, 2)]
            sage: B.matching(use_edge_labels=True, value_only=True)                     # needs networkx
            4
            sage: B.matching(use_edge_labels=True, value_only=True, algorithm=\'Edmonds\')            # needs networkx
            4
            sage: B.matching(use_edge_labels=True, value_only=True, algorithm=\'LP\')     # needs sage.numerical.mip
            4
            sage: B.matching(use_edge_labels=True, value_only=True, algorithm=\'Eppstein\')
            Traceback (most recent call last):
            ...
            ValueError: use_edge_labels cannot be used with "Hopcroft-Karp" or "Eppstein"
            sage: B.matching(use_edge_labels=True, value_only=True, algorithm=\'Hopcroft-Karp\')
            Traceback (most recent call last):
            ...
            ValueError: use_edge_labels cannot be used with "Hopcroft-Karp" or "Eppstein"
            sage: B.matching(use_edge_labels=False, value_only=True,                    # needs networkx
            ....:            algorithm=\'Hopcroft-Karp\')
            2
            sage: B.matching(use_edge_labels=False, value_only=True,                    # needs networkx
            ....:            algorithm=\'Eppstein\')
            2
            sage: B.matching(use_edge_labels=False, value_only=True, algorithm=\'Edmonds\')           # needs networkx
            2
            sage: B.matching(use_edge_labels=False, value_only=True, algorithm=\'LP\')    # needs sage.numerical.mip
            2

        With multiedges enabled::

            sage: G = BipartiteGraph(graphs.CubeGraph(3))
            sage: for e in G.edges(sort=True):
            ....:     G.set_edge_label(e[0], e[1], int(e[0]) + int(e[1]))
            sage: G.allow_multiple_edges(True)
            sage: G.matching(use_edge_labels=True, value_only=True)                     # needs networkx
            444

        Empty bipartite graph and bipartite graphs without edges::

            sage: B = BipartiteGraph()
            sage: algorithms = ["Hopcroft-Karp", "Eppstein", "Edmonds", "LP"]
            sage: not any(B.matching(algorithm=algo) for algo in algorithms)            # needs networkx
            True
            sage: all(B.matching(algorithm=algo, value_only=True) == 0 for algo in algorithms)      # needs networkx
            True
            sage: B.add_vertex(1, left=True)
            sage: B.add_vertex(2, left=True)
            sage: B.add_vertex(3, right=True)
            sage: not any(B.matching(algorithm=algo) for algo in algorithms)            # needs networkx
            True
            sage: all(B.matching(algorithm=algo, value_only=True) == 0 for algo in algorithms)      # needs networkx
            True
        '''
    def vertex_cover(self, algorithm: str = 'Konig', value_only: bool = False, reduction_rules: bool = True, solver=None, verbose: int = 0, *, integrality_tolerance: float = 0.001):
        '''
        Return a minimum vertex cover of ``self`` represented by a set of vertices.

        A minimum vertex cover of a graph is a set `S` of vertices such that
        each edge is incident to at least one element of `S`, and such that `S`
        is of minimum cardinality. For more information, see
        :wikipedia:`Vertex_cover`.

        Equivalently, a vertex cover is defined as the complement of an
        independent set.

        As an optimization problem, it can be expressed as follows:

        .. MATH::

            \\mbox{Minimize : }&\\sum_{v\\in G} b_v\\\\\n            \\mbox{Such that : }&\\forall (u,v) \\in G.edges(sort=True), b_u+b_v\\geq 1\\\\\n            &\\forall x\\in G, b_x\\mbox{ is a binary variable}

        INPUT:

        - ``algorithm`` -- string (default: ``\'Konig\'``); algorithm to use
          among:

          - ``\'Konig\'`` will compute a minimum vertex cover using Konig\'s
            algorithm (:wikipedia:`Kőnig%27s_theorem_(graph_theory)`)

          - ``\'Cliquer\'`` will compute a minimum vertex cover
            using the Cliquer package

          - ``\'MILP\'`` will compute a minimum vertex cover through a mixed
            integer linear program

          - ``\'mcqd\'`` will use the MCQD solver
            (`<http://www.sicmm.org/~konc/maxclique/>`_), and the MCQD
            package must be installed

        - ``value_only`` -- boolean (default: ``False``); if set to ``True``,
          only the size of a minimum vertex cover is returned. Otherwise,
          a minimum vertex cover is returned as a list of vertices.

        - ``reduction_rules`` -- (default: ``True``) specify if the reductions
          rules from kernelization must be applied as pre-processing or not.
          See [ACFLSS04]_ for more details. Note that depending on the instance,
          it might be faster to disable reduction rules.  This parameter is
          currently ignored when ``algorithm == "Konig"``.

        - ``solver`` -- string (default: ``None``); specifies a Mixed Integer
          Linear Programming (MILP) solver to be used. If set to ``None``, the
          default one is used. For more information on MILP solvers and which
          default solver is used, see the method :meth:`solve
          <sage.numerical.mip.MixedIntegerLinearProgram.solve>` of the class
          :class:`MixedIntegerLinearProgram
          <sage.numerical.mip.MixedIntegerLinearProgram>`.

        - ``verbose`` -- integer (default: 0); sets the level of
          verbosity. Set to 0 by default, which means quiet.

        - ``integrality_tolerance`` -- float; parameter for use with MILP
          solvers over an inexact base ring; see
          :meth:`MixedIntegerLinearProgram.get_values`.

        EXAMPLES:

        On the Cycle Graph::

            sage: B = BipartiteGraph(graphs.CycleGraph(6))
            sage: len(B.vertex_cover())                                                 # needs networkx
            3
            sage: B.vertex_cover(value_only=True)                                       # needs networkx
            3

        The two algorithms should return the same result::

           sage: # needs networkx numpy
           sage: g = BipartiteGraph(graphs.RandomBipartite(10, 10, .5))
           sage: vc1 = g.vertex_cover(algorithm=\'Konig\')
           sage: vc2 = g.vertex_cover(algorithm=\'Cliquer\')
           sage: len(vc1) == len(vc2)
           True

        TESTS:

        Giving a non connected bipartite graph::

            sage: B = BipartiteGraph(graphs.CycleGraph(4) * 2)
            sage: len(B.vertex_cover())                                                 # needs networkx
            4

        Empty bipartite graph and bipartite graphs without edges::

            sage: B = BipartiteGraph()
            sage: algorithms = ["Konig", "Cliquer", "MILP"]
            sage: all(B.vertex_cover(algorithm=algo) == [] for algo in algorithms)
            True
            sage: all(B.vertex_cover(algorithm=algo, value_only=True) == 0 for algo in algorithms)
            True
            sage: B.add_vertex(1, left=True)
            sage: B.add_vertex(2, left=True)
            sage: B.add_vertex(3, right=True)
            sage: all(B.vertex_cover(algorithm=algo) == [] for algo in algorithms)
            True
            sage: all(B.vertex_cover(algorithm=algo, value_only=True) == 0 for algo in algorithms)
            True
        '''
    def canonical_label(self, partition=None, certificate: bool = False, edge_labels: bool = False, algorithm=None, return_graph: bool = True, immutable=None):
        """
        Return the canonical graph.

        A canonical graph is the representative graph of an isomorphism
        class by some canonization function `c`. If `G` and `H` are graphs,
        then `G \\cong c(G)`, and `c(G) == c(H)` if and only if `G \\cong H`.

        See the :wikipedia:`Graph_canonization` for more information.

        INPUT:

        - ``partition`` -- if given, the canonical label with respect
          to this set partition will be computed. The default is the unit
          set partition.

        - ``certificate`` -- boolean (default: ``False``); when set to
          ``True``, a dictionary mapping from the vertices of the (di)graph
          to its canonical label will also be returned

        - ``edge_labels`` -- boolean (default: ``False``); when set to
          ``True``, allows only permutations respecting edge labels

        - ``algorithm`` -- string (default: ``None``); the algorithm to use.
          Currently available:

          * ``'bliss'``: use the optional package bliss
            (http://www.tcs.tkk.fi/Software/bliss/index.html);
          * ``'sage'``: always use Sage's implementation.
          * ``None`` (default): use bliss when available and possible

            .. NOTE::

                Make sure you always compare canonical forms obtained by the
                same algorithm.

        - ``return_graph`` -- boolean (default: ``True``); when set to
          ``False``, returns the list of edges of the canonical graph
          instead of the canonical graph. Only available when ``'bliss'``
          is explicitly set as algorithm.

        - ``immutable`` -- boolean (default: ``None``); whether to create a
          mutable/immutable (di)graph. ``immutable=None`` (default) means that
          the (di)graph and its canonical (di)graph will behave the same way.

        EXAMPLES::

            sage: B = BipartiteGraph( [(0, 4), (0, 5), (0, 6), (0, 8), (1, 5),
            ....:                      (1, 7), (1, 8), (2, 6), (2, 7), (2, 8),
            ....:                      (3, 4), (3, 7), (3, 8), (4, 9), (5, 9),
            ....:                      (6, 9), (7, 9)] )
            sage: C = B.canonical_label(partition=(B.left,B.right), algorithm='sage')
            sage: C
            Bipartite graph on 10 vertices
            sage: C.left
            {0, 1, 2, 3, 4}
            sage: C.right
            {5, 6, 7, 8, 9}

        ::

            sage: B = BipartiteGraph( [(0, 4), (0, 5), (0, 6), (0, 8), (1, 5),
            ....:                      (1, 7), (1, 8), (2, 6), (2, 7), (2, 8),
            ....:                      (3, 4), (3, 7), (3, 8), (4, 9), (5, 9),
            ....:                      (6, 9), (7, 9)] )
            sage: C, cert = B.canonical_label(partition=(B.left, B.right),
            ....:                             certificate=True, algorithm='sage')
            sage: C
            Bipartite graph on 10 vertices
            sage: C.left
            {0, 1, 2, 3, 4}
            sage: C.right
            {5, 6, 7, 8, 9}
            sage: cert == {0: 3, 1: 0, 2: 1, 3: 2, 4: 5, 5: 7, 6: 6, 7: 8, 8: 9, 9: 4}
            True

        ::

            sage: G = Graph({0: [5, 6], 1: [4, 5], 2: [4, 6], 3: [4, 5, 6]})
            sage: B = BipartiteGraph(G)
            sage: C = B.canonical_label(partition=(B.left, B.right),
            ....:                       edge_labels=True, algorithm='sage')
            sage: C.left
            {0, 1, 2, 3}
            sage: C.right
            {4, 5, 6}

        TESTS:

        Check that :issue:`38832` is fixed::

            sage: B = BipartiteGraph(matrix([[1, 1], [1, 1]]))
            sage: B.canonical_label()
            Bipartite graph on 4 vertices
            sage: B.canonical_label(certificate=True)[0]
            Bipartite graph on 4 vertices
            sage: B.canonical_label(edge_labels=True)
            Bipartite graph on 4 vertices
            sage: B.allow_multiple_edges(True)
            sage: B.add_edges(B.edges())
            sage: B.canonical_label()
            Bipartite multi-graph on 4 vertices

        Check the behavior for immutable graphs::

            sage: G = BipartiteGraph(graphs.CycleGraph(4))
            sage: G.canonical_label().is_immutable()
            False
            sage: G.canonical_label(immutable=True).is_immutable()
            True
            sage: G = BipartiteGraph(graphs.CycleGraph(4), immutable=True)
            sage: G.canonical_label().is_immutable()
            True
            sage: G.canonical_label(immutable=False).is_immutable()
            False

        .. SEEALSO::

            :meth:`~sage.graphs.generic_graph.GenericGraph.canonical_label()`
        """
