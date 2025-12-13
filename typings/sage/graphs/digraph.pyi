from _typeshed import Incomplete
from collections.abc import Generator
from sage.graphs.comparability import is_transitive as is_transitive
from sage.graphs.connectivity import is_strongly_connected as is_strongly_connected, strong_articulation_points as strong_articulation_points, strongly_connected_component_containing_vertex as strongly_connected_component_containing_vertex, strongly_connected_components_digraph as strongly_connected_components_digraph, strongly_connected_components_subgraphs as strongly_connected_components_subgraphs
from sage.graphs.cycle_enumeration import all_cycles_iterator as all_cycles_iterator, all_simple_cycles as all_simple_cycles
from sage.graphs.dot2tex_utils import have_dot2tex as have_dot2tex
from sage.graphs.generic_graph import GenericGraph as GenericGraph
from sage.graphs.views import EdgesView as EdgesView
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ

class DiGraph(GenericGraph):
    '''
    Directed graph.

    A digraph or directed graph is a set of vertices connected by oriented
    edges. See also the :wikipedia:`Directed_graph`. For a collection of
    pre-defined digraphs, see the :mod:`~sage.graphs.digraph_generators` module.

    A :class:`DiGraph` object has many methods whose list can be obtained by
    typing ``g.<tab>`` (i.e. hit the :kbd:`Tab` key) or by reading the documentation
    of :mod:`~sage.graphs.digraph`, :mod:`~sage.graphs.generic_graph`, and
    :mod:`~sage.graphs.graph`.

    INPUT:

    By default, a :class:`DiGraph` object is simple (i.e. no *loops* nor
    *multiple edges*) and unweighted. This can be easily tuned with the
    appropriate flags (see below).

    - ``data`` -- can be any of the following (see the ``format`` argument):

      #. ``DiGraph()`` -- build a digraph on 0 vertices

      #. ``DiGraph(5)`` -- return an edgeless digraph on the 5 vertices 0,...,4

      #. ``DiGraph([list_of_vertices, list_of_edges])`` -- return a digraph with
         given vertices/edges

         To bypass auto-detection, prefer the more explicit
         ``DiGraph([V, E], format=\'vertices_and_edges\')``.

      #. ``DiGraph(list_of_edges)`` -- return a digraph with a given list of
         edges (see documentation of
         :meth:`~sage.graphs.generic_graph.GenericGraph.add_edges`).

         To bypass auto-detection, prefer the more explicit
         ``DiGraph(L, format=\'list_of_edges\')``.

      #. ``DiGraph({1: [2,3,4], 3: [4]})`` -- return a digraph by associating to
         each vertex the list of its out-neighbors.

         To bypass auto-detection, prefer the more explicit
         ``DiGraph(D, format=\'dict_of_lists\')``.

      #. ``DiGraph({1: {2: \'a\', 3: \'b\'}, 3: {2: \'c\'}})`` -- return a digraph by
         associating a list of out-neighbors to each vertex and providing its
         edge label.

         To bypass auto-detection, prefer the more explicit
         ``DiGraph(D, format=\'dict_of_dicts\')``.

         For digraphs with multiple edges, you can provide a list of labels
         instead, e.g.: ``DiGraph({1: {2: [\'a1\', \'a2\'], 3:[\'b\']},
         3:{2:[\'c\']}})``.

      #. ``DiGraph(a_matrix)`` -- return a digraph with given (weighted)
         adjacency matrix (see documentation of
         :meth:`~sage.graphs.generic_graph.GenericGraph.adjacency_matrix`).

         To bypass auto-detection, prefer the more explicit ``DiGraph(M,
         format=\'adjacency_matrix\')``. To take weights into account, use
         ``format=\'weighted_adjacency_matrix\'`` instead.

      #. ``DiGraph(a_nonsquare_matrix)`` -- return a digraph with given
         incidence matrix (see documentation of
         :meth:`~sage.graphs.generic_graph.GenericGraph.incidence_matrix`).

         To bypass auto-detection, prefer the more explicit ``DiGraph(M,
         format=\'incidence_matrix\')``.

      #. ``DiGraph([V, f])`` -- return a digraph with a vertex set ``V`` and an
         edge `u,v` whenever `f(u, v)` is ``True``. Example: ``DiGraph([
         [1..10], lambda x,y: abs(x - y).is_square()])``

      #. ``DiGraph(\'FOC@?OC@_?\')`` -- return a digraph from a ``dig6`` string
         (see documentation of :meth:`~dig6_string`).

      #. ``DiGraph(another_digraph)`` -- return a digraph from a Sage (di)graph,
         `pygraphviz <https://pygraphviz.github.io/>`__ digraph, `NetworkX
         <https://networkx.github.io/>`__ digraph, or `igraph
         <http://igraph.org/python/>`__ digraph.

    - ``pos`` -- dictionary (default: ``None``); a positioning dictionary. For
      example, the spring layout from NetworkX for the 5-cycle is::

         {0: [-0.91679746, 0.88169588],
          1: [ 0.47294849, 1.125     ],
          2: [ 1.125     ,-0.12867615],
          3: [ 0.12743933,-1.125     ],
          4: [-1.125     ,-0.50118505]}

    - ``name`` -- string (default: ``None``); gives the graph a name (e.g.,
      name=\'complete\')

    - ``loops`` -- boolean (default: ``None``); whether to allow loops (ignored
      if data is an instance of the DiGraph class)

    - ``multiedges`` -- boolean (default: ``None``); whether to allow multiple
      edges (ignored if data is an instance of the DiGraph class)

    - ``weighted`` -- boolean (default: ``None``); whether digraph thinks of
      itself as weighted or not. See ``self.weighted()``

    - ``format`` -- string (default: ``None``); if set to ``None``,
      :class:`DiGraph` tries to guess input\'s format. To avoid this possibly
      time-consuming step, one of the following values can be specified (see
      description above): ``\'int\'``, ``\'dig6\'``, ``\'rule\'``,
      ``\'list_of_edges\'``, ``\'dict_of_lists\'``, ``\'dict_of_dicts\'``,
      ``\'adjacency_matrix\'``, ``\'weighted_adjacency_matrix\'``,
      ``\'incidence_matrix\'``, ``"NX"``, ``\'igraph\'``.

    - ``sparse`` -- boolean (default: ``True``); ``sparse=True`` is an alias for
      ``data_structure="sparse"``, and ``sparse=False`` is an alias for
      ``data_structure="dense"``

    - ``data_structure`` -- string (default: ``\'sparse\'``); one of the following
      (for more information, see :mod:`~sage.graphs.base.overview`):

      * ``\'dense\'`` -- selects the :mod:`~sage.graphs.base.dense_graph` backend

      * ``\'sparse\'`` -- selects the :mod:`~sage.graphs.base.sparse_graph`
        backend

      * ``\'static_sparse\'`` -- selects the
        :mod:`~sage.graphs.base.static_sparse_backend` (this backend is faster
        than the sparse backend and smaller in memory, and it is immutable, so
        that the resulting graphs can be used as dictionary keys).

    - ``immutable`` -- boolean (default: ``False``); whether to create a
      immutable digraph. Note that ``immutable=True`` is actually a shortcut for
      ``data_structure=\'static_sparse\'``.

    - ``hash_labels`` -- boolean (default: ``None``); whether to include edge
      labels during hashing. This parameter defaults to ``True`` if the digraph
      is weighted. This parameter is ignored if the digraph is mutable.
      Beware that trying to hash unhashable labels will raise an error.

    - ``vertex_labels`` -- boolean (default: ``True``); whether to allow any
      object as a vertex (slower), or only the integers `0,...,n-1`, where `n`
      is the number of vertices.

    - ``convert_empty_dict_labels_to_None`` -- boolean (default: ``None``); this
      arguments sets the default edge labels used by NetworkX (empty
      dictionaries) to be replaced by ``None``, the default Sage edge label. It
      is set to ``True`` iff a NetworkX graph is on the input.

    EXAMPLES:

    #. A dictionary of dictionaries::

            sage: g = DiGraph({0: {1: \'x\', 2: \'z\', 3: \'a\'}, 2: {5: \'out\'}}); g
            Digraph on 5 vertices

       The labels (\'x\', \'z\', \'a\', \'out\') are labels for edges. For example,
       \'out\' is the label for the edge from 2 to 5. Labels can be used as
       weights, if all the labels share some common parent.

    #. A dictionary of lists (or iterables)::

            sage: g = DiGraph({0: [1, 2, 3], 2: [4]}); g
            Digraph on 5 vertices
            sage: g = DiGraph({0: (1, 2, 3), 2: (4,)}); g
            Digraph on 5 vertices

    #. A list of vertices and a function describing adjacencies. Note that the
       list of vertices and the function must be enclosed in a list (i.e.,
       ``[list of vertices, function]``).

       We construct a graph on the integers 1 through 12 such that there is a
       directed edge from `i` to `j` if and only if `i` divides `j`::

            sage: g = DiGraph([[1..12], lambda i,j: i != j and i.divides(j)])
            sage: g.vertices(sort=True)
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
            sage: g.adjacency_matrix()                                                  # needs sage.modules
            [0 1 1 1 1 1 1 1 1 1 1 1]
            [0 0 0 1 0 1 0 1 0 1 0 1]
            [0 0 0 0 0 1 0 0 1 0 0 1]
            [0 0 0 0 0 0 0 1 0 0 0 1]
            [0 0 0 0 0 0 0 0 0 1 0 0]
            [0 0 0 0 0 0 0 0 0 0 0 1]
            [0 0 0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0 0 0]

    #. A Sage matrix: Note: If format is not specified, then Sage assumes a
       square matrix is an adjacency matrix, and a nonsquare matrix is an
       incidence matrix.

       - an adjacency matrix::

            sage: M = Matrix([[0, 1, 1, 1, 0], [0, 0, 0, 0, 0],                         # needs sage.modules
            ....:             [0, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]); M
            [0 1 1 1 0]
            [0 0 0 0 0]
            [0 0 0 0 1]
            [0 0 0 0 0]
            [0 0 0 0 0]
            sage: DiGraph(M)                                                            # needs sage.modules
            Digraph on 5 vertices

            sage: M = Matrix([[0,1,-1], [-1,0,-1/2], [1,1/2,0]]); M                     # needs sage.modules
            [   0    1   -1]
            [  -1    0 -1/2]
            [   1  1/2    0]
            sage: G = DiGraph(M, sparse=True, weighted=True); G                         # needs sage.modules
            Digraph on 3 vertices
            sage: G.weighted()                                                          # needs sage.modules
            True

       - an incidence matrix::

            sage: M = Matrix(6, [-1,0,0,0,1, 1,-1,0,0,0, 0,1,-1,0,0,                    # needs sage.modules
            ....:                0,0,1,-1,0, 0,0,0,1,-1, 0,0,0,0,0]); M
            [-1  0  0  0  1]
            [ 1 -1  0  0  0]
            [ 0  1 -1  0  0]
            [ 0  0  1 -1  0]
            [ 0  0  0  1 -1]
            [ 0  0  0  0  0]
            sage: DiGraph(M)                                                            # needs sage.modules
            Digraph on 6 vertices

    #. A ``dig6`` string: Sage automatically recognizes whether a string is in
       ``dig6`` format, which is a directed version of ``graph6``::

            sage: D = DiGraph(\'IRAaDCIIOWEOKcPWAo\')
            sage: D
            Digraph on 10 vertices

            sage: D = DiGraph(\'IRAaDCIIOEOKcPWAo\')
            Traceback (most recent call last):
            ...
            RuntimeError: the string (IRAaDCIIOEOKcPWAo) seems corrupt: for n = 10, the string is too short

            sage: D = DiGraph("IRAaDCI\'OWEOKcPWAo")
            Traceback (most recent call last):
            ...
            RuntimeError: the string seems corrupt: valid characters are
            ?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~

    #. A NetworkX MultiDiGraph::

            sage: import networkx                                                       # needs networkx
            sage: g = networkx.MultiDiGraph({0: [1, 2, 3], 2: [4]})                     # needs networkx
            sage: DiGraph(g)                                                            # needs networkx
            Multi-digraph on 5 vertices


    #. A NetworkX digraph::

            sage: import networkx                                                       # needs networkx
            sage: g = networkx.DiGraph({0: [1, 2, 3], 2: [4]})                          # needs networkx
            sage: DiGraph(g)                                                            # needs networkx
            Digraph on 5 vertices

    #. An igraph directed Graph (see also
       :meth:`~sage.graphs.generic_graph.GenericGraph.igraph_graph`)::

           sage: import igraph                                   # optional - python_igraph
           sage: g = igraph.Graph([(0,1),(0,2)], directed=True)  # optional - python_igraph
           sage: DiGraph(g)                                      # optional - python_igraph
           Digraph on 3 vertices

       If ``vertex_labels`` is ``True``, the names of the vertices are given by
       the vertex attribute ``\'name\'``, if available::

           sage: # optional - python_igraph
           sage: g = igraph.Graph([(0,1),(0,2)], directed=True, vertex_attrs={\'name\':[\'a\',\'b\',\'c\']})
           sage: DiGraph(g).vertices(sort=True)
           [\'a\', \'b\', \'c\']
           sage: g = igraph.Graph([(0,1),(0,2)], directed=True, vertex_attrs={\'label\':[\'a\',\'b\',\'c\']})
           sage: DiGraph(g).vertices(sort=True)
           [0, 1, 2]

       If the igraph Graph has edge attributes, they are used as edge labels::

           sage: g = igraph.Graph([(0, 1), (0, 2)], directed=True,                  # optional - python_igraph
           ....:                  edge_attrs={\'name\':[\'a\', \'b\'], \'weight\':[1, 3]})
           sage: DiGraph(g).edges(sort=True)                                        # optional - python_igraph
           [(0, 1, {\'name\': \'a\', \'weight\': 1}), (0, 2, {\'name\': \'b\', \'weight\': 3})]


    TESTS::

        sage: DiGraph({0:[1,2,3], 2:[4]}).edges(sort=True)
        [(0, 1, None), (0, 2, None), (0, 3, None), (2, 4, None)]
        sage: DiGraph({0:(1,2,3), 2:(4,)}).edges(sort=True)
        [(0, 1, None), (0, 2, None), (0, 3, None), (2, 4, None)]
        sage: DiGraph({0:Set([1,2,3]), 2:Set([4])}).edges(sort=True)
        [(0, 1, None), (0, 2, None), (0, 3, None), (2, 4, None)]

    Demonstrate that digraphs using the static backend are equal to mutable
    graphs but can be used as dictionary keys::

        sage: # needs networkx
        sage: import networkx
        sage: g = networkx.DiGraph({0:[1,2,3], 2:[4]})
        sage: G = DiGraph(g)
        sage: G_imm = DiGraph(G, data_structure=\'static_sparse\')
        sage: H_imm = DiGraph(G, data_structure=\'static_sparse\')
        sage: H_imm is G_imm
        False
        sage: H_imm == G_imm == G
        True
        sage: {G_imm:1}[H_imm]
        1
        sage: {G_imm:1}[G]
        Traceback (most recent call last):
        ...
        TypeError: This graph is mutable, and thus not hashable. Create an
        immutable copy by `g.copy(immutable=True)`

    The error message states that one can also create immutable graphs by
    specifying the ``immutable`` optional argument (not only by
    ``data_structure=\'static_sparse\'`` as above)::

        sage: J_imm = DiGraph(G, immutable=True)                                        # needs networkx
        sage: J_imm == G_imm                                                            # needs networkx
        True
        sage: type(J_imm._backend) == type(G_imm._backend)                              # needs networkx
        True

    From a list of vertices and a list of edges::

        sage: G = DiGraph([[1,2,3],[(1,2)]]); G
        Digraph on 3 vertices
        sage: G.edges(sort=True)
        [(1, 2, None)]

    Check that :issue:`27505` is fixed::

        sage: DiGraph(DiGraph().networkx_graph(), weighted=None, format=\'NX\')           # needs networkx
        Digraph on 0 vertices
    '''
    def __init__(self, data=None, pos=None, loops=None, format=None, weighted=None, data_structure: str = 'sparse', vertex_labels: bool = True, name=None, multiedges=None, convert_empty_dict_labels_to_None=None, sparse: bool = True, immutable: bool = False, hash_labels=None) -> None:
        '''
        TESTS::

            sage: D = DiGraph()
            sage: loads(dumps(D)) == D
            True

            sage: a = matrix(2,2,[1,2,0,1])                                             # needs sage.modules
            sage: DiGraph(a, sparse=True).adjacency_matrix() == a                       # needs sage.modules
            True

            sage: a = matrix(2,2,[3,2,0,1])                                             # needs sage.modules
            sage: DiGraph(a, sparse=True).adjacency_matrix() == a                       # needs sage.modules
            True

        The positions are copied when the DiGraph is built from another DiGraph
        or from a Graph ::

            sage: g = DiGraph(graphs.PetersenGraph())
            sage: h = DiGraph(g)
            sage: g.get_pos() == h.get_pos()
            True
            sage: g.get_pos() == graphs.PetersenGraph().get_pos()
            True

        The position dictionary is not the input one (:issue:`22424`)::

            sage: my_pos = {0:(0,0), 1:(1,1)}
            sage: D = DiGraph([[0,1], [(0,1)]], pos=my_pos)
            sage: my_pos == D._pos
            True
            sage: my_pos is D._pos
            False

        Detection of multiple edges::

            sage: DiGraph({1:{2:[0,1]}})
            Multi-digraph on 2 vertices
            sage: DiGraph({1:{2:0}})
            Digraph on 2 vertices

        An empty list or dictionary defines a simple graph (:issue:`10441` and
        :issue:`12910`)::

            sage: DiGraph([])
            Digraph on 0 vertices
            sage: DiGraph({})
            Digraph on 0 vertices
            sage: # not "Multi-digraph on 0 vertices"

        Problem with weighted adjacency matrix (:issue:`13919`)::

            sage: B = {0:{1:2,2:5,3:4},1:{2:2,4:7},2:{3:1,4:4,5:3},
            ....:      3:{5:4},4:{5:1,6:5},5:{4:1,6:7,5:1}}
            sage: grafo3 = DiGraph(B, weighted=True)
            sage: matad = grafo3.weighted_adjacency_matrix()                            # needs sage.modules
            sage: grafo4 = DiGraph(matad, format=\'adjacency_matrix\', weighted=True)     # needs sage.modules
            sage: grafo4.shortest_path(0, 6, by_weight=True)                            # needs sage.modules
            [0, 1, 2, 5, 4, 6]

        Building a DiGraph with ``immutable=False`` returns a mutable graph::

            sage: g = graphs.PetersenGraph()
            sage: g = DiGraph(g.edges(sort=True), immutable=False)
            sage: g.add_edge("Hey", "Heyyyyyyy")
            sage: {g:1}[g]
            Traceback (most recent call last):
            ...
            TypeError: This graph is mutable, and thus not hashable. Create an immutable copy by `g.copy(immutable=True)`
            sage: copy(g) is g
            False
            sage: {g.copy(immutable=True):1}[g.copy(immutable=True)]
            1

        But building it with ``immutable=True`` returns an immutable graph::

            sage: g = DiGraph(graphs.PetersenGraph(), immutable=True)
            sage: g.add_edge("Hey", "Heyyyyyyy")
            Traceback (most recent call last):
            ...
            TypeError: this graph is immutable and so cannot be changed
            sage: {g:1}[g]
            1
            sage: copy(g) is g    # copy is mutable again
            False

        Unknown input format::

            sage: DiGraph(4, format=\'HeyHeyHey\')
            Traceback (most recent call last):
            ...
            ValueError: unknown input format \'HeyHeyHey\'

        Sage DiGraph from igraph undirected graph::

            sage: import igraph            # optional - python_igraph
            sage: DiGraph(igraph.Graph())  # optional - python_igraph
            Traceback (most recent call last):
            ...
            ValueError: a *directed* igraph graph was expected. To build an undirected graph, call the Graph constructor

        Vertex labels are retained in the graph (:issue:`14708`)::

            sage: g = DiGraph()
            sage: g.add_vertex(0)
            sage: g.set_vertex(0, \'foo\')
            sage: g.get_vertices()
            {0: \'foo\'}
            sage: DiGraph(g).get_vertices()
            {0: \'foo\'}
        '''
    def dig6_string(self):
        """
        Return the ``dig6`` representation of the digraph as an ASCII string.

        This is only valid for simple (no multiple edges) digraphs on at most
        `2^{18} - 1 = 262143` vertices.

        .. NOTE::

            As the ``dig6`` format only handles graphs with vertex set `\\{0,
            \\ldots, n-1\\}`, a :meth:`relabelled copy
            <sage.graphs.generic_graph.GenericGraph.relabel>` will be encoded,
            if necessary.

        .. SEEALSO::

            * :meth:`~sage.graphs.graph.Graph.graph6_string` -- a similar string
              format for undirected graphs

        EXAMPLES::

            sage: D = DiGraph({0: [1, 2], 1: [2], 2: [3], 3: [0]})
            sage: D.dig6_string()
            'CW`_'
            sage: L = DiGraph({0: [1, 2], 1: [2], 2: [3], 3: [3]})
            sage: L.dig6_string()
            'CW`C'

        TESTS::

            sage: DiGraph().dig6_string()
            '?'
        """
    def is_directed(self):
        """
        Since digraph is directed, return ``True``.

        EXAMPLES::

            sage: DiGraph().is_directed()
            True
        """
    def is_directed_acyclic(self, certificate: bool = False):
        """
        Check whether the digraph is acyclic or not.

        A directed graph is acyclic if for any vertex `v`, there is no directed
        path that starts and ends at `v`. Every directed acyclic graph (DAG)
        corresponds to a partial ordering of its vertices, however multiple dags
        may lead to the same partial ordering.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); whether to return a
          certificate

        OUTPUT:

        * When ``certificate=False``, returns a boolean value

        * When ``certificate=True``:

          * If the graph is acyclic, returns a pair ``(True, ordering)`` where
            ``ordering`` is a list of the vertices such that `u` appears
            before `v` in ``ordering`` if `uv` is an edge.

          * Else, returns a pair ``(False, cycle)`` where ``cycle`` is a list of
            vertices representing a circuit in the graph.

        EXAMPLES:

        At first, the following graph is acyclic::

            sage: D = DiGraph({0:[1, 2, 3], 4:[2, 5], 1:[8], 2:[7], 3:[7], 5:[6,7], 7:[8], 6:[9], 8:[10], 9:[10]})
            sage: D.plot(layout='circular').show()                                      # needs sage.plot
            sage: D.is_directed_acyclic()
            True

        Adding an edge from `9` to `7` does not change it::

            sage: D.add_edge(9, 7)
            sage: D.is_directed_acyclic()
            True

        We can obtain as a proof an ordering of the vertices such that `u`
        appears before `v` if `uv` is an edge of the graph::

            sage: D.is_directed_acyclic(certificate=True)
            (True, [4, 5, 6, 9, 0, 1, 2, 3, 7, 8, 10])

        Adding an edge from 7 to 4, though, makes a difference::

            sage: D.add_edge(7, 4)
            sage: D.is_directed_acyclic()
            False

        Indeed, it creates a circuit `7, 4, 5`::

            sage: D.is_directed_acyclic(certificate=True)
            (False, [7, 4, 5])

        Checking acyclic graphs are indeed acyclic ::

            sage: def random_acyclic(n, p):
            ....:  g = graphs.RandomGNP(n, p)
            ....:  h = DiGraph()
            ....:  h.add_edges(((u, v) if u < v else (v, u)) for u, v in g.edge_iterator(labels=False))
            ....:  return h
            ...
            sage: all(random_acyclic(100, .2).is_directed_acyclic()    # long time
            ....:      for i in range(50))
            True

        TESTS:

        What about loops? ::

            sage: g = digraphs.ButterflyGraph(3)
            sage: g.allow_loops(True)
            sage: g.is_directed_acyclic()
            True
            sage: g.add_edge(0, 0)
            sage: g.is_directed_acyclic()
            False
        """
    def to_directed(self):
        """
        Since the graph is already directed, simply returns a copy of itself.

        EXAMPLES::

            sage: DiGraph({0: [1, 2, 3], 4: [5, 1]}).to_directed()
            Digraph on 6 vertices
        """
    def to_undirected(self, data_structure=None, sparse=None):
        '''
        Return an undirected version of the graph.

        Every directed edge becomes an edge.

        INPUT:

        - ``data_structure`` -- string (default: ``None``); one of
          ``\'sparse\'``, ``\'static_sparse\'``, or ``\'dense\'``. See the
          documentation of :class:`Graph` or :class:`DiGraph`.

        - ``sparse`` -- boolean (default: ``None``); ``sparse=True`` is an
          alias for ``data_structure="sparse"``, and ``sparse=False`` is an
          alias for ``data_structure="dense"``.

        EXAMPLES::

            sage: D = DiGraph({0: [1, 2], 1: [0]})
            sage: G = D.to_undirected()
            sage: D.edges(sort=True, labels=False)
            [(0, 1), (0, 2), (1, 0)]
            sage: G.edges(sort=True, labels=False)
            [(0, 1), (0, 2)]

        TESTS:

        Immutable graphs yield immutable graphs (:issue:`17005`)::

            sage: DiGraph([[1, 2]], immutable=True).to_undirected()._backend
            <sage.graphs.base.static_sparse_backend.StaticSparseBackend object at ...>

        Vertex labels will be retained (:issue:`14708`)::

            sage: D.set_vertex(0, \'foo\')
            sage: G = D.to_undirected()
            sage: D.get_vertices()
            {0: \'foo\', 1: None, 2: None}
            sage: G.get_vertices()
            {0: \'foo\', 1: None, 2: None}
        '''
    def incoming_edge_iterator(self, vertices, labels: bool = True):
        """
        Return an iterator over all arriving edges from vertices.

        INPUT:

        - ``vertices`` -- a vertex or a list of vertices

        - ``labels`` -- boolean (default: ``True``); whether to return edges as
          pairs of vertices, or as triples containing the labels

        EXAMPLES::

            sage: D = DiGraph({0: [1,2,3], 1: [0,2], 2: [3], 3: [4], 4: [0,5], 5: [1]})
            sage: for a in D.incoming_edge_iterator([0]):
            ....:     print(a)
            (1, 0, None)
            (4, 0, None)
        """
    def incoming_edges(self, vertices, labels: bool = True):
        """
        Return a list of edges arriving at vertices.

        INPUT:

        - ``vertices`` -- a vertex or a list of vertices

        - ``labels`` -- boolean (default: ``True``); whether to return edges as
          pairs of vertices, or as triples containing the labels

        EXAMPLES::

            sage: D = DiGraph({0: [1,2,3], 1: [0,2], 2: [3], 3: [4], 4: [0,5], 5: [1]})
            sage: D.incoming_edges([0])
            [(1, 0, None), (4, 0, None)]
        """
    def outgoing_edge_iterator(self, vertices, labels: bool = True):
        """
        Return an iterator over all departing edges from vertices.

        INPUT:

        - ``vertices`` -- a vertex or a list of vertices

        - ``labels`` -- boolean (default: ``True``); whether to return edges as
          pairs of vertices, or as triples containing the labels

        EXAMPLES::

            sage: D = DiGraph({0: [1,2,3], 1: [0,2], 2: [3], 3: [4], 4: [0,5], 5: [1]})
            sage: for a in D.outgoing_edge_iterator([0]):
            ....:     print(a)
            (0, 1, None)
            (0, 2, None)
            (0, 3, None)
        """
    def outgoing_edges(self, vertices, labels: bool = True):
        """
        Return a list of edges departing from vertices.

        INPUT:

        - ``vertices`` -- a vertex or a list of vertices

        - ``labels`` -- boolean (default: ``True``); whether to return edges as
          pairs of vertices, or as triples containing the labels

        EXAMPLES::

            sage: D = DiGraph({0: [1,2,3], 1: [0,2], 2: [3], 3: [4], 4: [0,5], 5: [1]})
            sage: D.outgoing_edges([0])
            [(0, 1, None), (0, 2, None), (0, 3, None)]
        """
    def neighbor_in_iterator(self, vertex) -> Generator[Incomplete, Incomplete]:
        """
        Return an iterator over the in-neighbors of ``vertex``.

        A vertex `u` is an in-neighbor of a vertex `v` if `uv` in an edge.

        EXAMPLES::

            sage: D = DiGraph({0: [1,2,3], 1: [0,2], 2: [3], 3: [4], 4: [0,5], 5: [1]})
            sage: for a in D.neighbor_in_iterator(0):
            ....:     print(a)
            1
            4

        TESTS:

        With multiple edges, check that the neighbors are listed only once::

            sage: D = DiGraph([[0, 1, 2], [(0, 1), (0, 1), (1, 2) ]],multiedges=True)
            sage: list(D.neighbor_in_iterator(0))
            []
            sage: list(D.neighbor_in_iterator(1))
            [0]
            sage: list(D.neighbor_in_iterator(2))
            [1]

        Check that the iterator lists ``vertex`` in the presence of loop(s):

            sage: D = DiGraph([[0, 1, 2], [(0, 0), (0, 0), (1, 1)]],multiedges=True, loops=True)
            sage: list(D.neighbor_in_iterator(0))
            [0]
            sage: list(D.neighbor_in_iterator(1))
            [1]
            sage: list(D.neighbor_in_iterator(2))
            []

        """
    def neighbors_in(self, vertex):
        """
        Return the list of the in-neighbors of a given vertex.

        A vertex `u` is an in-neighbor of a vertex `v` if `uv` in an edge.

        EXAMPLES::

            sage: D = DiGraph({0: [1,2,3], 1: [0,2], 2: [3], 3: [4], 4: [0,5], 5: [1]})
            sage: D.neighbors_in(0)
            [1, 4]
        """
    def neighbor_out_iterator(self, vertex) -> Generator[Incomplete, Incomplete]:
        """
        Return an iterator over the out-neighbors of a given vertex.

        A vertex `u` is an out-neighbor of a vertex `v` if `vu` in an edge.

        EXAMPLES::

            sage: D = DiGraph({0: [1,2,3], 1: [0,2], 2: [3], 3: [4], 4: [0,5], 5: [1]})
            sage: for a in D.neighbor_out_iterator(0):
            ....:     print(a)
            1
            2
            3

        TESTS:

        With multiple edges, check that the neighbors are listed only once::

            sage: D = DiGraph([[0, 1, 2], [(0, 1), (0, 1), (1, 2) ]],multiedges=True)
            sage: list(D.neighbor_out_iterator(0))
            [1]
            sage: list(D.neighbor_out_iterator(1))
            [2]
            sage: list(D.neighbor_out_iterator(2))
            []

        Check that the iterator lists ``vertex`` in the presence of loop(s):

            sage: D = DiGraph([[0, 1, 2], [(0, 0), (0, 0), (1, 1)]],multiedges=True, loops=True)
            sage: list(D.neighbor_out_iterator(0))
            [0]
            sage: list(D.neighbor_out_iterator(1))
            [1]
            sage: list(D.neighbor_out_iterator(2))
            []

        """
    def neighbors_out(self, vertex):
        """
        Return the list of the out-neighbors of a given vertex.

        A vertex `u` is an out-neighbor of a vertex `v` if `vu` in an edge.

        EXAMPLES::

            sage: D = DiGraph({0: [1,2,3], 1: [0,2], 2: [3], 3: [4], 4: [0,5], 5: [1]})
            sage: D.neighbors_out(0)
            [1, 2, 3]
        """
    def in_degree(self, vertices=None, labels: bool = False):
        """
        Same as degree, but for in degree.

        EXAMPLES::

            sage: D = DiGraph({0: [1,2,3], 1: [0,2], 2: [3], 3: [4], 4: [0,5], 5: [1]})
            sage: D.in_degree(vertices=[0, 1, 2], labels=True)
            {0: 2, 1: 2, 2: 2}
            sage: D.in_degree()
            [2, 2, 2, 2, 1, 1]
            sage: G = graphs.PetersenGraph().to_directed()
            sage: G.in_degree(0)
            3
        """
    def in_degree_iterator(self, vertices=None, labels: bool = False) -> Generator[Incomplete]:
        """
        Same as degree_iterator, but for in degree.

        EXAMPLES::

            sage: D = graphs.Grid2dGraph(2,4).to_directed()
            sage: sorted(D.in_degree_iterator())
            [2, 2, 2, 2, 3, 3, 3, 3]
            sage: sorted(D.in_degree_iterator(labels=True))
            [((0, 0), 2),
             ((0, 1), 3),
             ((0, 2), 3),
             ((0, 3), 2),
             ((1, 0), 2),
             ((1, 1), 3),
             ((1, 2), 3),
             ((1, 3), 2)]
        """
    def in_degree_sequence(self):
        """
        Return the in-degree sequence.

        EXAMPLES:

        The in-degree sequences of two digraphs::

            sage: g = DiGraph({1: [2, 5, 6], 2: [3, 6], 3: [4, 6], 4: [6], 5: [4, 6]})
            sage: g.in_degree_sequence()
            [5, 2, 1, 1, 1, 0]

        ::

            sage: V = [2, 3, 5, 7, 8, 9, 10, 11]
            sage: E = [[], [8, 10], [11], [8, 11], [9], [], [], [2, 9, 10]]
            sage: g = DiGraph(dict(zip(V, E)))
            sage: g.in_degree_sequence()
            [2, 2, 2, 2, 1, 0, 0, 0]
        """
    def out_degree(self, vertices=None, labels: bool = False):
        """
        Same as degree, but for out degree.

        EXAMPLES::

            sage: D = DiGraph({0: [1,2,3], 1: [0,2], 2: [3], 3: [4], 4: [0,5], 5: [1]})
            sage: D.out_degree(vertices=[0, 1 ,2], labels=True)
            {0: 3, 1: 2, 2: 1}
            sage: D.out_degree()
            [3, 2, 1, 1, 2, 1]
            sage: D.out_degree(2)
            1
        """
    def out_degree_iterator(self, vertices=None, labels: bool = False) -> Generator[Incomplete]:
        """
        Same as degree_iterator, but for out degree.

        EXAMPLES::

            sage: D = graphs.Grid2dGraph(2,4).to_directed()
            sage: sorted(D.out_degree_iterator())
            [2, 2, 2, 2, 3, 3, 3, 3]
            sage: sorted(D.out_degree_iterator(labels=True))
            [((0, 0), 2),
             ((0, 1), 3),
             ((0, 2), 3),
             ((0, 3), 2),
             ((1, 0), 2),
             ((1, 1), 3),
             ((1, 2), 3),
             ((1, 3), 2)]
        """
    def out_degree_sequence(self):
        """
        Return the outdegree sequence of this digraph.

        EXAMPLES:

        The outdegree sequences of two digraphs::

            sage: g = DiGraph({1: [2, 5, 6], 2: [3, 6], 3: [4, 6], 4: [6], 5: [4, 6]})
            sage: g.out_degree_sequence()
            [3, 2, 2, 2, 1, 0]

        ::

            sage: V = [2, 3, 5, 7, 8, 9, 10, 11]
            sage: E = [[], [8, 10], [11], [8, 11], [9], [], [], [2, 9, 10]]
            sage: g = DiGraph(dict(zip(V, E)))
            sage: g.out_degree_sequence()
            [3, 2, 2, 1, 1, 0, 0, 0]
        """
    def sources(self) -> list:
        """
        Return a list of sources of the digraph.

        OUTPUT: list of the vertices of the digraph that have no edges going into them

        EXAMPLES::

            sage: G = DiGraph({1: {3: ['a']}, 2: {3: ['b']}})
            sage: G.sources()
            [1, 2]
            sage: T = DiGraph({1: {}})
            sage: T.sources()
            [1]
        """
    def sinks(self) -> list:
        """
        Return a list of sinks of the digraph.

        OUTPUT: list of the vertices of the digraph that have no edges beginning at them

        EXAMPLES::

            sage: G = DiGraph({1: {3: ['a']}, 2: {3: ['b']}})
            sage: G.sinks()
            [3]
            sage: T = DiGraph({1: {}})
            sage: T.sinks()
            [1]
        """
    def degree_polynomial(self):
        """
        Return the generating polynomial of degrees of vertices in ``self``.

        This is the sum

        .. MATH::

            \\sum_{v \\in G} x^{\\operatorname{in}(v)} y^{\\operatorname{out}(v)},

        where ``in(v)`` and ``out(v)`` are the number of incoming and outgoing
        edges at vertex `v` in the digraph `G`.

        Because this polynomial is multiplicative for Cartesian product of
        digraphs, it is useful to help see if the digraph can be isomorphic to a
        Cartesian product.

        .. SEEALSO::

            :meth:`num_verts` for the value at `(x, y) = (1, 1)`

        EXAMPLES::

            sage: G = posets.PentagonPoset().hasse_diagram()                            # needs sage.modules
            sage: G.degree_polynomial()                                                 # needs sage.modules
            x^2 + 3*x*y + y^2

            sage: G = posets.BooleanLattice(4).hasse_diagram()
            sage: G.degree_polynomial().factor()                                        # needs sage.libs.pari
            (x + y)^4
        """
    def feedback_edge_set(self, constraint_generation: bool = True, value_only: bool = False, solver=None, verbose: int = 0, *, integrality_tolerance: float = 0.001):
        '''
        Compute the minimum feedback edge set of a digraph (also called
        feedback arc set).

        The minimum feedback edge set of a digraph is a set of edges that
        intersect all the circuits of the digraph.  Equivalently, a minimum
        feedback arc set of a DiGraph is a set `S` of arcs such that the digraph
        `G - S` is acyclic. For more information, see the
        :wikipedia:`Feedback_arc_set`.

        INPUT:

        - ``value_only`` -- boolean (default: ``False``)

          - When set to ``True``, only the minimum cardinal of a minimum edge
            set is returned.

          - When set to ``False``, the ``Set`` of edges of a minimal edge set is
            returned.

        - ``constraint_generation`` -- boolean (default: ``True``); whether to
          use constraint generation when solving the Mixed Integer Linear
          Program.

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

        ALGORITHM:

        This problem is solved using Linear Programming, in two different
        ways. The first one is to solve the following formulation:

        .. MATH::

            \\mbox{Minimize : }&\\sum_{(u,v)\\in G} b_{(u,v)}\\\\\n            \\mbox{Such that : }&\\\\\n            &\\forall (u,v)\\in G, d_u-d_v+ n \\cdot b_{(u,v)}\\geq 0\\\\\n            &\\forall u\\in G, 0\\leq d_u\\leq |G|\\\\\n
        An explanation:

        An acyclic digraph can be seen as a poset, and every poset has a linear
        extension. This means that in any acyclic digraph the vertices can be
        ordered with a total order `<` in such a way that if `(u,v) \\in G`, then
        `u < v`.

        Thus, this linear program is built in order to assign to each vertex `v`
        a number `d_v \\in [0,\\dots,n-1]` such that if there exists an edge
        `(u, v) \\in G` such that `d_v < d_u`, then the edge `(u,v)` is removed.

        The number of edges removed is then minimized, which is the objective.

        (Constraint Generation)

        If the parameter ``constraint_generation`` is enabled, a more efficient
        formulation is used :

        .. MATH::

            \\mbox{Minimize : }&\\sum_{(u,v)\\in G} b_{(u,v)}\\\\\n            \\mbox{Such that : }&\\\\\n            &\\forall C\\text{ circuits }\\subseteq G, \\sum_{uv\\in C}b_{(u,v)}\\geq 1\\\\\n
        As the number of circuits contained in a graph is exponential, this LP
        is solved through constraint generation. This means that the solver is
        sequentially asked to solved the problem, knowing only a portion of the
        circuits contained in `G`, each time adding to the list of its
        constraints the circuit which its last answer had left intact.

        EXAMPLES:

        If the digraph is created from a graph, and hence is symmetric (if `uv`
        is an edge, then `vu` is an edge too), then obviously the cardinality of
        its feedback arc set is the number of edges in the first graph::

            sage: cycle = graphs.CycleGraph(5)
            sage: dcycle = DiGraph(cycle)
            sage: cycle.size()
            5
            sage: dcycle.feedback_edge_set(value_only=True)                             # needs sage.numerical.mip
            5

        And in this situation, for any edge `uv` of the first graph, `uv` of
        `vu` is in the returned feedback arc set::

           sage: g = graphs.RandomGNP(5,.3)
           sage: while not g.num_edges():
           ....:     g = graphs.RandomGNP(5,.3)
           sage: dg = DiGraph(g)
           sage: feedback = dg.feedback_edge_set()                                      # needs sage.numerical.mip
           sage: u,v,l = next(g.edge_iterator())
           sage: (u,v) in feedback or (v,u) in feedback                                 # needs sage.numerical.mip
           True

        TESTS:

        Comparing with/without constraint generation. Also double-checks issue
        :issue:`12833`::

            sage: for i in range(20):                                                   # needs sage.numerical.mip
            ....:     g = digraphs.RandomDirectedGNP(10, .3)
            ....:     x = g.feedback_edge_set(value_only=True)
            ....:     y = g.feedback_edge_set(value_only=True,
            ....:            constraint_generation=False)
            ....:     if x != y:
            ....:         print("Oh my, oh my !")
            ....:         break

        Loops are part of the feedback edge set (:issue:`23989`)::

            sage: # needs sage.combinat
            sage: D = digraphs.DeBruijn(2, 2)
            sage: sorted(D.loops(labels=None))
            [(\'00\', \'00\'), (\'11\', \'11\')]
            sage: FAS = D.feedback_edge_set(value_only=False)                           # needs sage.numerical.mip
            sage: all(l in FAS for l in D.loops(labels=None))                           # needs sage.numerical.mip
            True
            sage: FAS2 = D.feedback_edge_set(value_only=False,                          # needs sage.numerical.mip
            ....:                            constraint_generation=False)
            sage: len(FAS) == len(FAS2)                                                 # needs sage.numerical.mip
            True

        Check that multi-edges are properly taken into account::

            sage: cycle = graphs.CycleGraph(5)
            sage: dcycle = DiGraph(cycle)
            sage: dcycle.feedback_edge_set(value_only=True)                             # needs sage.numerical.mip
            5
            sage: dcycle.allow_multiple_edges(True)
            sage: dcycle.add_edges(dcycle.edges(sort=True))
            sage: dcycle.feedback_edge_set(value_only=True)                             # needs sage.numerical.mip
            10
            sage: dcycle.feedback_edge_set(value_only=True,                             # needs sage.numerical.mip
            ....:                          constraint_generation=False)
            10

        Strongly connected components are well handled (:issue:`23989`)::

            sage: g = digraphs.Circuit(3) * 2
            sage: g.add_edge(0, 3)
            sage: g.feedback_edge_set(value_only=True)                                  # needs sage.numerical.mip
            2
        '''
    def reverse(self, immutable=None):
        """
        Return a copy of digraph with edges reversed in direction.

        INPUT:

        - ``immutable`` -- boolean (default: ``None``); whether to return an
          immutable digraph or not. By default (``None``), the returned digraph
          has the same setting than ``self``. That is, if ``self`` is immutable,
          the returned digraph also is.

        EXAMPLES::

            sage: adj = {0: [1,2,3], 1: [0,2], 2: [3], 3: [4], 4: [0,5], 5: [1]}
            sage: D = DiGraph(adj)
            sage: R = D.reverse(); R
            Reverse of (): Digraph on 6 vertices
            sage: H = R.reverse()
            sage: adj == H.to_dictionary()
            True

        TESTS::

            sage: adj = {0: [1, 1], 1: [1]}
            sage: D = DiGraph(adj, immutable=True, multiedges=True, loops=True)
            sage: R = D.reverse()
            sage: R.is_immutable() and R.allows_loops() and R.allows_multiple_edges()
            True
            sage: adj == R.reverse().to_dictionary(multiple_edges=True)
            True

        Check the behavior of parameter ``immutable``::

            sage: D = DiGraph([(0, 1)], immutable=False)
            sage: R = D.reverse()
            sage: R.is_immutable()
            False
            sage: R = D.reverse(immutable=True)
            sage: R.is_immutable()
            True
            sage: H = R.reverse()
            sage: H.is_immutable()
            True
            sage: H = R.reverse(immutable=False)
            sage: H.is_immutable()
            False
        """
    def reverse_edge(self, u, v=None, label=None, inplace: bool = True, multiedges=None):
        """
        Reverse the edge from `u` to `v`.

        INPUT:

        - ``inplace`` -- boolean (default: ``True``); if ``False``, a new
          digraph is created and returned as output, otherwise ``self`` is
          modified.

        - ``multiedges`` -- boolean (default: ``None``); how to decide what
          should be done in case of doubt (for instance when edge `(1,2)` is to
          be reversed in a graph while `(2,1)` already exists):

          - If set to ``True``, input graph will be forced to allow parallel
            edges if necessary and edge `(1,2)` will appear twice in the graph.

          - If set to ``False``, only one edge `(1,2)` will remain in the graph
            after `(2,1)` is reversed. Besides, the label of edge `(1,2)` will
            be overwritten with the label of edge `(2,1)`.

          The default behaviour (``multiedges = None``) will raise an exception
          each time a subjective decision (setting ``multiedges`` to ``True`` or
          ``False``) is necessary to perform the operation.

        The following forms are all accepted:

        - D.reverse_edge( 1, 2 )
        - D.reverse_edge( (1, 2) )
        - D.reverse_edge( [1, 2] )
        - D.reverse_edge( 1, 2, 'label' )
        - D.reverse_edge( ( 1, 2, 'label') )
        - D.reverse_edge( [1, 2, 'label'] )
        - D.reverse_edge( ( 1, 2), label='label' )

        EXAMPLES:

        If ``inplace`` is ``True`` (default), ``self`` is modified::

            sage: D = DiGraph([(0, 1 ,2)])
            sage: D.reverse_edge(0, 1)
            sage: D.edges(sort=True)
            [(1, 0, 2)]

        If ``inplace`` is ``False``, ``self`` is not modified and a new digraph
        is returned::

            sage: D = DiGraph([(0, 1, 2)])
            sage: re = D.reverse_edge(0, 1, inplace=False)
            sage: re.edges(sort=True)
            [(1, 0, 2)]
            sage: D.edges(sort=True)
            [(0, 1, 2)]

        If ``multiedges`` is ``True``, ``self`` will be forced to allow parallel
        edges when and only when it is necessary::

            sage: D = DiGraph([(1, 2, 'A'), (2, 1, 'A'), (2, 3, None)])
            sage: D.reverse_edge(1, 2, multiedges=True)
            sage: D.edges(sort=True)
            [(2, 1, 'A'), (2, 1, 'A'), (2, 3, None)]
            sage: D.allows_multiple_edges()
            True

        Even if ``multiedges`` is ``True``, ``self`` will not be forced to allow
        parallel edges when it is not necessary::

            sage: D = DiGraph( [(1, 2, 'A'), (2, 1, 'A'), (2, 3, None)] )
            sage: D.reverse_edge(2, 3, multiedges=True)
            sage: D.edges(sort=True)
            [(1, 2, 'A'), (2, 1, 'A'), (3, 2, None)]
            sage: D.allows_multiple_edges()
            False

        If user specifies ``multiedges = False``, ``self`` will not be forced to
        allow parallel edges and a parallel edge will get deleted::

            sage: D = DiGraph( [(1, 2, 'A'), (2, 1, 'A'), (2, 3, None)] )
            sage: D.edges(sort=True)
            [(1, 2, 'A'), (2, 1, 'A'), (2, 3, None)]
            sage: D.reverse_edge(1, 2, multiedges=False)
            sage: D.edges(sort=True)
            [(2, 1, 'A'), (2, 3, None)]

        Note that in the following graph, specifying ``multiedges = False`` will
        result in overwriting the label of `(1, 2)` with the label of `(2, 1)`::

            sage: D = DiGraph( [(1, 2, 'B'), (2, 1, 'A'), (2, 3, None)] )
            sage: D.edges(sort=True)
            [(1, 2, 'B'), (2, 1, 'A'), (2, 3, None)]
            sage: D.reverse_edge(2, 1, multiedges=False)
            sage: D.edges(sort=True)
            [(1, 2, 'A'), (2, 3, None)]

        If input edge in digraph has weight/label, then the weight/label should
        be preserved in the output digraph.  User does not need to specify the
        weight/label when calling function::

            sage: D = DiGraph([[0, 1, 2], [1, 2, 1]], weighted=True)
            sage: D.reverse_edge(0, 1)
            sage: D.edges(sort=True)
            [(1, 0, 2), (1, 2, 1)]
            sage: re = D.reverse_edge([1, 2], inplace=False)
            sage: re.edges(sort=True)
            [(1, 0, 2), (2, 1, 1)]

        If ``self`` has multiple copies (parallel edges) of the input edge, only
        1 of the parallel edges is reversed::

            sage: D = DiGraph([(0, 1, '01'), (0, 1, '01'), (0, 1, 'cat'), (1, 2, '12')], weighted=True, multiedges=True)
            sage: re = D.reverse_edge([0, 1, '01'], inplace=False)
            sage: re.edges(sort=True)
            [(0, 1, '01'), (0, 1, 'cat'), (1, 0, '01'), (1, 2, '12')]

        If ``self`` has multiple copies (parallel edges) of the input edge but
        with distinct labels and no input label is specified, only 1 of the
        parallel edges is reversed (the edge that is labeled by the first label
        on the list returned by :meth:`.edge_label`)::

            sage: D = DiGraph([(0, 1, 'A'), (0, 1, 'B'), (0, 1, 'mouse'), (0, 1, 'cat')], multiedges=true)
            sage: D.edge_label(0, 1)
            ['cat', 'mouse', 'B', 'A']
            sage: D.reverse_edge(0, 1)
            sage: D.edges(sort=True)
            [(0, 1, 'A'), (0, 1, 'B'), (0, 1, 'mouse'), (1, 0, 'cat')]

        Finally, an exception is raised when Sage does not know how to choose
        between allowing multiple edges and losing some data::

            sage: D = DiGraph([(0, 1, 'A'), (1, 0, 'B')])
            sage: D.reverse_edge(0, 1)
            Traceback (most recent call last):
            ...
            ValueError: reversing the given edge is about to create two parallel
            edges but input digraph doesn't allow them - User needs to specify
            multiedges is True or False.

        The following syntax is supported, but note that you must use the
        ``label`` keyword::

            sage: D = DiGraph()
            sage: D.add_edge((1, 2), label='label')
            sage: D.edges(sort=True)
            [(1, 2, 'label')]
            sage: D.reverse_edge((1, 2), label='label')
            sage: D.edges(sort=True)
            [(2, 1, 'label')]
            sage: D.add_edge((1, 2), 'label')
            sage: D.edges(sort=False)
            [((1, 2), 'label', None), (2, 1, 'label')]
            sage: D.reverse_edge((1, 2), 'label')
            sage: D.edges(sort=False)
            [('label', (1, 2), None), (2, 1, 'label')]

        TESTS::

            sage: D = DiGraph([(0, 1, None)])
            sage: D.reverse_edge(0, 1, 'mylabel')
            Traceback (most recent call last):
            ...
            ValueError: input edge must exist in the digraph
        """
    def reverse_edges(self, edges, inplace: bool = True, multiedges=None):
        """
        Reverse a list of edges.

        INPUT:

        - ``edges`` -- list of edges in the DiGraph

        - ``inplace`` -- boolean (default: ``True``); if ``False``, a new
          digraph is created and returned as output, otherwise ``self`` is
          modified

        - ``multiedges`` -- boolean (default: ``None``); if ``True``, input
          graph will be forced to allow parallel edges when necessary (for more
          information see the documentation of :meth:`~DiGraph.reverse_edge`)

        .. SEEALSO::

            :meth:`~DiGraph.reverse_edge` -- reverses a single edge

        EXAMPLES:

        If ``inplace`` is ``True`` (default), ``self`` is modified::

            sage: D = DiGraph({ 0: [1, 1, 3], 2: [3, 3], 4: [1, 5]}, multiedges=true)
            sage: D.reverse_edges([[0, 1], [0, 3]])
            sage: D.reverse_edges([(2, 3), (4, 5)])
            sage: D.edges(sort=True)
            [(0, 1, None), (1, 0, None), (2, 3, None), (3, 0, None),
             (3, 2, None), (4, 1, None), (5, 4, None)]

        If ``inplace`` is ``False``, ``self`` is not modified and a new digraph
        is returned::

            sage: D = DiGraph([(0, 1, 'A'), (1, 0, 'B'), (1, 2, 'C')])
            sage: re = D.reverse_edges([(0, 1), (1, 2)],
            ....:                       inplace=False,
            ....:                       multiedges=True)
            sage: re.edges(sort=True)
            [(1, 0, 'A'), (1, 0, 'B'), (2, 1, 'C')]
            sage: D.edges(sort=True)
            [(0, 1, 'A'), (1, 0, 'B'), (1, 2, 'C')]
            sage: D.allows_multiple_edges()
            False
            sage: re.allows_multiple_edges()
            True

        If ``multiedges`` is ``True``, ``self`` will be forced to allow parallel
        edges when and only when it is necessary::

            sage: D = DiGraph([(1, 2, 'A'), (2, 1, 'A'), (2, 3, None)])
            sage: D.reverse_edges([(1, 2), (2, 3)], multiedges=True)
            sage: D.edges(sort=True)
            [(2, 1, 'A'), (2, 1, 'A'), (3, 2, None)]
            sage: D.allows_multiple_edges()
            True

        Even if ``multiedges`` is ``True``, ``self`` will not be forced to allow
        parallel edges when it is not necessary::

            sage: D = DiGraph([(1, 2, 'A'), (2, 1, 'A'), (2, 3, None)])
            sage: D.reverse_edges([(2, 3)], multiedges=True)
            sage: D.edges(sort=True)
            [(1, 2, 'A'), (2, 1, 'A'), (3, 2, None)]
            sage: D.allows_multiple_edges()
            False

        If ``multiedges`` is ``False``, ``self`` will not be forced to allow
        parallel edges and an edge will get deleted::

            sage: D = DiGraph([(1, 2), (2, 1)])
            sage: D.edges(sort=True)
            [(1, 2, None), (2, 1, None)]
            sage: D.reverse_edges([(1, 2)], multiedges=False)
            sage: D.edges(sort=True)
            [(2, 1, None)]

        If input edge in digraph has weight/label, then the weight/label should
        be preserved in the output digraph.  User does not need to specify the
        weight/label when calling function::

            sage: D = DiGraph([(0, 1, '01'), (1, 2, 1), (2, 3, '23')], weighted=True)
            sage: D.reverse_edges([(0, 1, '01'), (1, 2), (2, 3)])
            sage: D.edges(sort=True)
            [(1, 0, '01'), (2, 1, 1), (3, 2, '23')]

        TESTS::

            sage: D = digraphs.Circuit(6)
            sage: D.reverse_edges(D.edges(sort=True), inplace=False).edges(sort=True)
            [(0, 5, None), (1, 0, None), (2, 1, None),
             (3, 2, None), (4, 3, None), (5, 4, None)]

            sage: D = digraphs.Kautz(2, 3)                                              # needs sage.combinat
            sage: Dr = D.reverse_edges(D.edges(sort=True), inplace=False,               # needs sage.combinat
            ....:                      multiedges=True)
            sage: Dr.edges(sort=True) == D.reverse().edges(sort=True)                   # needs sage.combinat
            True
        """
    def eccentricity(self, v=None, by_weight: bool = False, algorithm=None, weight_function=None, check_weight: bool = True, dist_dict=None, with_labels: bool = False):
        '''
        Return the eccentricity of vertex (or vertices) ``v``.

        The eccentricity of a vertex is the maximum distance to any other
        vertex.

        For more information and examples on how to use input variables, see
        :meth:`~GenericGraph.shortest_path_all_pairs`,
        :meth:`~GenericGraph.shortest_path_lengths` and
        :meth:`~GenericGraph.shortest_paths`

        INPUT:

        - ``v`` -- either a single vertex or a list of vertices. If it is not
          specified, then it is taken to be all vertices

        - ``by_weight`` -- boolean (default: ``False``); if ``True``, edge
          weights are taken into account; if ``False``, all edges have weight 1

        - ``algorithm`` -- string (default: ``None``); one of the following
          algorithms:

          - ``\'BFS\'`` -- the computation is done through a BFS centered on each
            vertex successively. Works only if ``by_weight==False``

          - ``\'Floyd-Warshall-Cython\'`` -- a Cython implementation of the
            Floyd-Warshall algorithm. Works only if ``by_weight==False`` and
            ``v is None`` or ``v`` should contain all vertices of ``self``.

          - ``\'Floyd-Warshall-Python\'`` -- a Python implementation of the
            Floyd-Warshall algorithm. Works also with weighted graphs, even with
            negative weights (but no negative cycle is allowed). However, ``v``
            must be ``None`` or ``v`` should contain all vertices of ``self``.

          - ``\'Dijkstra_NetworkX\'`` -- the Dijkstra algorithm, implemented in
            NetworkX. It works with weighted graphs, but no negative weight is
            allowed.

          - ``\'Dijkstra_Boost\'`` -- the Dijkstra algorithm, implemented in Boost
            (works only with positive weights)

          - ``\'Johnson_Boost\'`` -- the Johnson algorithm, implemented in
            Boost (works also with negative weights, if there is no negative
            cycle). Works only if ``v is None`` or ``v`` should contain all
            vertices of ``self``.

          - ``\'From_Dictionary\'`` -- uses the (already computed) distances, that
            are provided by input variable ``dist_dict``

          - ``None`` (default): Sage chooses the best algorithm:
            ``\'From_Dictionary\'`` if ``dist_dict`` is not None, ``\'BFS\'`` for
            unweighted graphs, ``\'Dijkstra_Boost\'`` if all weights are
            positive, ``\'Johnson_Boost\'`` otherwise.

        - ``weight_function`` -- function (default: ``None``); a function that
          takes as input an edge ``(u, v, l)`` and outputs its weight. If not
          ``None``, ``by_weight`` is automatically set to ``True``. If ``None``
          and ``by_weight`` is ``True``, we use the edge label ``l``, if ``l``
          is not ``None``, else ``1`` as a weight.

        - ``check_weight`` -- boolean (default: ``True``); if ``True``, we check
          that the ``weight_function`` outputs a number for each edge

        - ``dist_dict`` -- dictionary (default: ``None``); a dict of dicts of
          distances (used only if ``algorithm==\'From_Dictionary\'``)

        - ``with_labels`` -- boolean (default: ``False``); whether to return a
          list or a dictionary keyed by vertices

        EXAMPLES::

            sage: G = graphs.KrackhardtKiteGraph().to_directed()
            sage: G.eccentricity()
            [4, 4, 4, 4, 4, 3, 3, 2, 3, 4]
            sage: G.vertices(sort=True)
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            sage: G.eccentricity(7)
            2
            sage: G.eccentricity([7,8,9])
            [2, 3, 4]
            sage: G.eccentricity([7,8,9], with_labels=True) == {8: 3, 9: 4, 7: 2}
            True
            sage: G = DiGraph(3)
            sage: G.eccentricity(with_labels=True)
            {0: +Infinity, 1: +Infinity, 2: +Infinity}
            sage: G = DiGraph({0:[]})
            sage: G.eccentricity(with_labels=True)
            {0: 0}
            sage: G = DiGraph([(0,1,2), (1,2,3), (2,0,2)])
            sage: G.eccentricity(algorithm=\'BFS\')
            [2, 2, 2]
            sage: G.eccentricity(algorithm=\'Floyd-Warshall-Cython\')
            [2, 2, 2]
            sage: G.eccentricity(by_weight=True, algorithm=\'Dijkstra_NetworkX\')         # needs networkx
            [5, 5, 4]
            sage: G.eccentricity(by_weight=True, algorithm=\'Dijkstra_Boost\')
            [5, 5, 4]
            sage: G.eccentricity(by_weight=True, algorithm=\'Johnson_Boost\')
            [5, 5, 4]
            sage: G.eccentricity(by_weight=True, algorithm=\'Floyd-Warshall-Python\')
            [5, 5, 4]
            sage: G.eccentricity(dist_dict=G.shortest_path_all_pairs(by_weight=True)[0])
            [5, 5, 4]

        TESTS:

        A non-implemented algorithm::

            sage: G.eccentricity(algorithm=\'boh\')
            Traceback (most recent call last):
            ...
            ValueError: unknown algorithm "boh"

        An algorithm that does not work with edge weights::

            sage: G.eccentricity(by_weight=True, algorithm=\'BFS\')
            Traceback (most recent call last):
            ...
            ValueError: algorithm \'BFS\' does not work with weights
            sage: G.eccentricity(by_weight=True, algorithm=\'Floyd-Warshall-Cython\')
            Traceback (most recent call last):
            ...
            ValueError: algorithm \'Floyd-Warshall-Cython\' does not work with weights

        An algorithm that computes the all-pair-shortest-paths when not all
        vertices are needed::

            sage: G.eccentricity(0, algorithm=\'Floyd-Warshall-Cython\')
            Traceback (most recent call last):
            ...
            ValueError: algorithm \'Floyd-Warshall-Cython\' works only if all eccentricities are needed
            sage: G.eccentricity(0, algorithm=\'Floyd-Warshall-Python\')
            Traceback (most recent call last):
            ...
            ValueError: algorithm \'Floyd-Warshall-Python\' works only if all eccentricities are needed
            sage: G.eccentricity(0, algorithm=\'Johnson_Boost\')
            Traceback (most recent call last):
            ...
            ValueError: algorithm \'Johnson_Boost\' works only if all eccentricities are needed
        '''
    def radius(self, by_weight: bool = False, algorithm=None, weight_function=None, check_weight: bool = True):
        """
        Return the radius of the DiGraph.

        The radius is defined to be the minimum eccentricity of any vertex,
        where the eccentricity is the maximum distance to any other
        vertex. For more information and examples on how to use input variables,
        see :meth:`~GenericGraph.shortest_paths` and
        :meth:`~DiGraph.eccentricity`

        INPUT:

        - ``by_weight`` -- boolean (default: ``False``); if ``True``, edge
          weights are taken into account; if ``False``, all edges have weight 1

        - ``algorithm`` -- string (default: ``None``); see method
          :meth:`eccentricity` for the list of available algorithms

        - ``weight_function`` -- function (default: ``None``); a function that
          takes as input an edge ``(u, v, l)`` and outputs its weight. If not
          ``None``, ``by_weight`` is automatically set to ``True``. If ``None``
          and ``by_weight`` is ``True``, we use the edge label ``l``, if ``l``
          is not ``None``, else ``1`` as a weight.

        - ``check_weight`` -- boolean (default: ``True``); if ``True``, we check
          that the ``weight_function`` outputs a number for each edge

        EXAMPLES:

        The more symmetric a DiGraph is, the smaller (diameter - radius) is::

            sage: G = graphs.BarbellGraph(9, 3).to_directed()
            sage: G.radius()
            3
            sage: G.diameter()
            6

        ::

            sage: G = digraphs.Circuit(9)
            sage: G.radius()
            8
            sage: G.diameter()
            8

        TESTS::

            sage: G = DiGraph()
            sage: G.radius()
            Traceback (most recent call last):
            ...
            ValueError: radius is not defined for the empty DiGraph

        Check that :issue:`35300` is fixed::

            sage: H = DiGraph([[42, 'John'], [(42, 'John')]])
            sage: H.radius()
            1
        """
    def diameter(self, by_weight: bool = False, algorithm=None, weight_function=None, check_weight: bool = True):
        """
        Return the diameter of the DiGraph.

        The diameter is defined to be the maximum distance between two vertices.
        It is infinite if the DiGraph is not strongly connected.

        For more information and examples on how to use input variables, see
        :meth:`~GenericGraph.shortest_paths` and
        :meth:`~DiGraph.eccentricity`

        INPUT:

        - ``by_weight`` -- boolean (default: ``False``); if ``True``, edge
          weights are taken into account; if ``False``, all edges have weight 1

        - ``algorithm`` -- string (default: ``None``); one of the following
          algorithms:

          - ``'BFS'``: the computation is done through a BFS centered on each
            vertex successively. Works only if ``by_weight==False``. It computes
            all the eccentricities and return the maximum value.

          - ``'Floyd-Warshall-Cython'``: a Cython implementation of the
            Floyd-Warshall algorithm. Works only if ``by_weight==False``. It
            computes all the eccentricities and return the maximum value.

          - ``'Floyd-Warshall-Python'``: a Python implementation of the
            Floyd-Warshall algorithm. Works also with weighted graphs, even with
            negative weights (but no negative cycle is allowed). It computes all
            the eccentricities and return the maximum value.

          - ``'Dijkstra_NetworkX'``: the Dijkstra algorithm, implemented in
            NetworkX. It works with weighted graphs, but no negative weight is
            allowed. It computes all the eccentricities and return the maximum
            value.

          - ``'DiFUB'``, ``'2Dsweep'``: these algorithms are
            implemented in :func:`sage.graphs.distances_all_pairs.diameter` and
            :func:`sage.graphs.base.boost_graph.diameter`. ``'2Dsweep'`` returns
            lower bound on the diameter, while ``'DiFUB'`` returns the exact
            computed diameter. They also work with negative weight, if there is
            no negative cycle. See the functions documentation for more
            information.

          - ``'standard'`` : the standard algorithm is implemented in
            :func:`sage.graphs.distances_all_pairs.diameter`. It works only
            if ``by_weight==False``. See the function documentation for more
            information. It computes all the eccentricities and return the
            maximum value.

          - ``'Dijkstra_Boost'``: the Dijkstra algorithm, implemented in Boost
            (works only with positive weights). It computes all the
            eccentricities and return the maximum value.

          - ``'Johnson_Boost'``: the Johnson algorithm, implemented in
            Boost (works also with negative weights, if there is no negative
            cycle). It computes all the eccentricities and return the maximum
            value.

          - ``None`` (default): Sage chooses the best algorithm: ``'DiFUB'``.

        - ``weight_function`` -- function (default: ``None``); a function that
          takes as input an edge ``(u, v, l)`` and outputs its weight. If not
          ``None``, ``by_weight`` is automatically set to ``True``. If ``None``
          and ``by_weight`` is ``True``, we use the edge label ``l``, if ``l``
          is not ``None``, else ``1`` as weight.

        - ``check_weight`` -- boolean (default: ``True``); if ``True``, we check
          that the ``weight_function`` outputs a number for each edge

        EXAMPLES::

            sage: # needs sage.combinat
            sage: G = digraphs.DeBruijn(5,4)
            sage: G.diameter()
            4
            sage: G = digraphs.GeneralizedDeBruijn(9, 3)
            sage: G.diameter()
            2

        TESTS::

            sage: G = graphs.RandomGNP(40, 0.4).to_directed()
            sage: d1 = G.diameter(algorithm='DiFUB', by_weight=True)
            sage: d2 = max(G.eccentricity(algorithm='Dijkstra_Boost', by_weight=True))
            sage: d1 == d2
            True
            sage: G.diameter(algorithm='BFS', by_weight=True)
            Traceback (most recent call last):
            ...
            ValueError: algorithm 'BFS' does not work with weights
            sage: G.diameter(algorithm='Floyd-Warshall-Cython', by_weight=True)
            Traceback (most recent call last):
            ...
            ValueError: algorithm 'Floyd-Warshall-Cython' does not work with weights
            sage: G = digraphs.Path(5)
            sage: G.diameter(algorithm = 'DiFUB')
            +Infinity
            sage: G = DiGraph([(1,2,4), (2,1,7)])
            sage: G.diameter(algorithm='2Dsweep', by_weight=True)
            7.0
            sage: G.delete_edge(2,1,7)
            sage: G.add_edge(2,1,-5)
            sage: G.diameter(algorithm='2Dsweep', by_weight=True)
            Traceback (most recent call last):
            ...
            ValueError: the graph contains a negative cycle
            sage: G = DiGraph()
            sage: G.diameter()
            Traceback (most recent call last):
            ...
            ValueError: diameter is not defined for the empty DiGraph

        :issue:`32095` is fixed::

            sage: g6 = 'guQOUOQCW[IaDBCVP_IE\\\\RfxV@WMSaeHgheEIA@tfOJkB~@EpGLCrs'
            sage: g6 += 'aPIpwgQI_`Abs_x?VWxNJAo@w\\\\hffCDAW]bYGMIZGC_PYOrIw[Gp['
            sage: g6 += '@FTgc_O}E?fXAnGCB{gSaUcD'
            sage: G = Graph(g6).to_directed()
            sage: G.diameter(algorithm='DiFUB', by_weight=False)
            3
            sage: G.diameter(algorithm='DiFUB', by_weight=True)
            3.0

        Check that :issue:`35300` is fixed::

            sage: H = DiGraph([[42, 'John'], [(42, 'John')]])
            sage: H.diameter()
            +Infinity
            sage: H.add_edge('John', 42)
            sage: H.diameter()
            1
        """
    def center(self, by_weight: bool = False, algorithm=None, weight_function=None, check_weight: bool = True):
        """
        Return the set of vertices in the center of the DiGraph.

        The center is the set of vertices whose eccentricity is equal to the
        radius of the DiGraph, i.e., achieving the minimum eccentricity.

        For more information and examples on how to use input variables,
        see :meth:`~GenericGraph.shortest_paths` and
        :meth:`~DiGraph.eccentricity`

        INPUT:

        - ``by_weight`` -- boolean (default: ``False``); if ``True``, edge
          weights are taken into account; if ``False``, all edges have weight 1

        - ``algorithm`` -- string (default: ``None``); see method
          :meth:`eccentricity` for the list of available algorithms

        - ``weight_function`` -- function (default: ``None``); a function that
          takes as input an edge ``(u, v, l)`` and outputs its weight. If not
          ``None``, ``by_weight`` is automatically set to ``True``. If ``None``
          and ``by_weight`` is ``True``, we use the edge label ``l`` as a
          weight, if ``l`` is not ``None``, else ``1`` as a weight.

        - ``check_weight`` -- boolean (default: ``True``); if ``True``, we check
          that the ``weight_function`` outputs a number for each edge

        EXAMPLES:

        Every vertex is a center in a Circuit-DiGraph::

            sage: G = digraphs.Circuit(9)
            sage: G.center()
            [0, 1, 2, 3, 4, 5, 6, 7, 8]

        Center can be the whole graph::

            sage: G.subgraph(G.center()) == G
            True

        Some other graphs::

            sage: G = digraphs.Path(5)
            sage: G.center()
            [0]
            sage: G = DiGraph([(0,1,2), (1,2,3), (2,0,2)])
            sage: G.center(by_weight=True)
            [2]

        TESTS::

            sage: G = DiGraph()
            sage: G.center()
            []
            sage: G = DiGraph(3)
            sage: G.center()
            [0, 1, 2]
        """
    def periphery(self, by_weight: bool = False, algorithm=None, weight_function=None, check_weight: bool = True):
        """
        Return the set of vertices in the periphery of the DiGraph.

        The periphery is the set of vertices whose eccentricity is equal to the
        diameter of the DiGraph, i.e., achieving the maximum eccentricity.

        For more information and examples on how to use input variables,
        see :meth:`~GenericGraph.shortest_paths` and
        :meth:`~DiGraph.eccentricity`

        INPUT:

        - ``by_weight`` -- boolean (default: ``False``); if ``True``, edge
          weights are taken into account; if ``False``, all edges have weight 1

        - ``algorithm`` -- string (default: ``None``); see method
          :meth:`eccentricity` for the list of available algorithms

        - ``weight_function`` -- function (default: ``None``); a function that
          takes as input an edge ``(u, v, l)`` and outputs its weight. If not
          ``None``, ``by_weight`` is automatically set to ``True``. If ``None``
          and ``by_weight`` is ``True``, we use the edge label ``l`` as a
          weight, if ``l`` is not ``None``, else ``1`` as a weight.

        - ``check_weight`` -- boolean (default: ``True``); if ``True``, we check
          that the ``weight_function`` outputs a number for each edge

        EXAMPLES::

            sage: G = graphs.DiamondGraph().to_directed()
            sage: G.periphery()
            [0, 3]
            sage: P = digraphs.Path(5)
            sage: P.periphery()
            [1, 2, 3, 4]
            sage: G = digraphs.Complete(5)
            sage: G.subgraph(G.periphery()) == G
            True

        TESTS::

            sage: G = DiGraph()
            sage: G.periphery()
            []
            sage: G.add_vertex()
            0
            sage: G.periphery()
            [0]
        """
    def path_semigroup(self):
        """
        The partial semigroup formed by the paths of this quiver.

        EXAMPLES::

            sage: Q = DiGraph({1: {2: ['a', 'c']}, 2: {3: ['b']}})
            sage: F = Q.path_semigroup(); F                                             # needs sage.libs.flint
            Partial semigroup formed by the directed paths of Multi-digraph on 3 vertices
            sage: list(F)                                                               # needs sage.libs.flint
            [e_1, e_2, e_3, a, c, b, a*b, c*b]
        """
    def auslander_reiten_quiver(self):
        """
        Return the Auslander-Reiten quiver of ``self``.

        .. SEEALSO::

            :class:`~sage.quivers.ar_quiver.AuslanderReitenQuiver`

        EXAMPLES::

            sage: D = DiGraph([[1,2,'a'], [1,2,'b']], multiedges=True)
            sage: D.auslander_reiten_quiver()
            Auslander-Reiten quiver of Multi-digraph on 2 vertices
        """
    def topological_sort(self, implementation: str = 'default'):
        '''
        Return a topological sort of the digraph if it is acyclic.

        If the digraph contains a directed cycle, a :exc:`TypeError`
        is raised. As topological sorts are not necessarily unique,
        different implementations may yield different results.

        A topological sort is an ordering of the vertices of the digraph such
        that each vertex comes before all of its successors. That is, if `u`
        comes before `v` in the sort, then there may be a directed path from `u`
        to `v`, but there will be no directed path from `v` to `u`.

        INPUT:

        - ``implementation`` -- string (default: ``\'default\'``); either use the
          default Cython implementation, or the default NetworkX library
          (``implementation = "NetworkX"``)

        .. SEEALSO::

            - :meth:`is_directed_acyclic` -- tests whether a directed graph is
              acyclic (can also join a certificate; a topological sort or a
              circuit in the graph)

        EXAMPLES::

            sage: D = DiGraph({0: [1, 2, 3], 4: [2, 5], 1: [8], 2: [7], 3: [7],
            ....:   5: [6, 7], 7: [8], 6: [9], 8: [10], 9: [10]})
            sage: D.plot(layout=\'circular\').show()                                      # needs sage.plot
            sage: D.topological_sort()
            [4, 5, 6, 9, 0, 1, 2, 3, 7, 8, 10]

        ::

            sage: D.add_edge(9, 7)
            sage: D.topological_sort()
            [4, 5, 6, 9, 0, 1, 2, 3, 7, 8, 10]

        Using the NetworkX implementation ::

            sage: s = list(D.topological_sort(implementation="NetworkX")); s  # random  # needs networkx
            [0, 4, 1, 3, 2, 5, 6, 9, 7, 8, 10]
            sage: all(s.index(u) < s.index(v)                                           # needs networkx
            ....:     for u, v in D.edges(sort=False, labels=False))
            True

        ::

            sage: D.add_edge(7, 4)
            sage: D.topological_sort()
            Traceback (most recent call last):
            ...
            TypeError: digraph is not acyclic; there is no topological sort

        TESTS:

        A wrong value for the ``implementation`` keyword::

            sage: D.topological_sort(implementation = "cloud-reading")
            Traceback (most recent call last):
            ...
            ValueError: implementation must be set to one of "default" or "NetworkX"
        '''
    def topological_sort_generator(self):
        '''
        Return an iterator over all topological sorts of the digraph if
        it is acyclic.

        If the digraph contains a directed cycle, a :exc:`TypeError`
        is raised.

        A topological sort is an ordering of the vertices of the digraph such
        that each vertex comes before all of its successors. That is, if u comes
        before v in the sort, then there may be a directed path from u to v, but
        there will be no directed path from v to u. See also
        :meth:`topological_sort`.

        AUTHORS:

        - Mike Hansen - original implementation

        - Robert L. Miller: wrapping, documentation

        REFERENCE:

        - [1] Pruesse, Gara and Ruskey, Frank. Generating Linear
          Extensions Fast. SIAM J. Comput., Vol. 23 (1994), no. 2, pp.
          373-386.

        EXAMPLES::

            sage: D = DiGraph({0: [1, 2], 1: [3], 2: [3, 4]})
            sage: D.plot(layout=\'circular\').show()                                      # needs sage.plot
            sage: list(D.topological_sort_generator())                                  # needs sage.modules sage.rings.finite_rings
            [[0, 1, 2, 3, 4], [0, 2, 1, 3, 4], [0, 2, 1, 4, 3],
             [0, 2, 4, 1, 3], [0, 1, 2, 4, 3]]

        ::

            sage: for sort in D.topological_sort_generator():                           # needs sage.modules sage.rings.finite_rings
            ....:     for u, v in D.edge_iterator(labels=False):
            ....:         if sort.index(u) > sort.index(v):
            ....:             print("this should never happen")
        '''
    def layout_acyclic(self, rankdir: str = 'up', **options):
        """
        Return a ranked layout so that all edges point upward.

        To this end, the heights of the vertices are set according to the level
        set decomposition of the graph (see :meth:`.level_sets`).

        This is achieved by calling ``graphviz`` and ``dot2tex`` if available
        (see :meth:`.layout_graphviz`), and using a spring layout with fixed
        vertical placement of the vertices otherwise (see
        :meth:`.layout_acyclic_dummy` and
        :meth:`~sage.graphs.generic_graph.GenericGraph.layout_ranked`).

        Non acyclic graphs are partially supported by ``graphviz``, which then
        chooses some edges to point down.

        INPUT:

        - ``rankdir`` -- string (default: ``'up'``); indicates which direction
          the edges should point toward among ``'up'``, ``'down'``, ``'left'``,
          or ``'right'``

        - ``**options`` -- passed down to
          :meth:`~sage.graphs.generic_graph.GenericGraph.layout_ranked` or
          :meth:`~sage.graphs.generic_graph.GenericGraph.layout_graphviz`

        EXAMPLES::

            sage: H = DiGraph({0: [1, 2], 1: [3], 2: [3], 3: [], 5: [1, 6], 6: [2, 3]})

        The actual layout computed depends on whether dot2tex and graphviz are
        installed, so we don't test its relative values::

            sage: H.layout_acyclic()
            {0: [..., ...], 1: [..., ...], 2: [..., ...], 3: [..., ...], 5: [..., ...], 6: [..., ...]}

            sage: H = DiGraph({0: [1]})
            sage: pos = H.layout_acyclic(rankdir='up')
            sage: pos[1][1] > pos[0][1] + .5
            True
            sage: pos = H.layout_acyclic(rankdir='down')
            sage: pos[1][1] < pos[0][1] - .5
            True
            sage: pos = H.layout_acyclic(rankdir='right')
            sage: pos[1][0] > pos[0][0] + .5
            True
            sage: pos = H.layout_acyclic(rankdir='left')
            sage: pos[1][0] < pos[0][0] - .5
            True
        """
    def layout_acyclic_dummy(self, heights=None, rankdir: str = 'up', **options):
        """
        Return a ranked layout so that all edges point upward.

        To this end, the heights of the vertices are set according to the level
        set decomposition of the graph (see :meth:`level_sets`). This is
        achieved by a spring layout with fixed vertical placement of the
        vertices otherwise (see :meth:`layout_acyclic_dummy` and
        :meth:`~sage.graphs.generic_graph.GenericGraph.layout_ranked`).

        INPUT:

        - ``rankdir`` -- string (default: ``'up'``); indicates which direction
          the edges should point toward among ``'up'``, ``'down'``, ``'left'``,
          or ``'right'``

        - ``**options`` -- passed down to
          :meth:`~sage.graphs.generic_graph.GenericGraph.layout_ranked`

        EXAMPLES::

            sage: H = DiGraph({0: [1, 2], 1: [3], 2: [3], 3: [], 5: [1, 6], 6: [2, 3]})
            sage: H.layout_acyclic_dummy()
            {0: [1.0..., 0], 1: [1.0..., 1], 2: [1.5..., 2], 3: [1.5..., 3], 5: [2.0..., 0], 6: [2.0..., 1]}

            sage: H = DiGraph({0: [1]})
            sage: H.layout_acyclic_dummy(rankdir='up')
            {0: [0.5..., 0], 1: [0.5..., 1]}
            sage: H.layout_acyclic_dummy(rankdir='down')
            {0: [0.5..., 1], 1: [0.5..., 0]}
            sage: H.layout_acyclic_dummy(rankdir='left')
            {0: [1, 0.5...], 1: [0, 0.5...]}
            sage: H.layout_acyclic_dummy(rankdir='right')
            {0: [0, 0.5...], 1: [1, 0.5...]}
            sage: H = DiGraph({0: [1, 2], 1: [3], 2: [3], 3: [1], 5: [1, 6], 6: [2, 3]})
            sage: H.layout_acyclic_dummy()
            Traceback (most recent call last):
            ...
            ValueError: `self` should be an acyclic graph

        TESTS:

        :issue:`31681` is fixed::

            sage: H = DiGraph({0: [1], 'X': [1]}, format='dict_of_lists')
            sage: pos = H.layout_acyclic_dummy(rankdir='up')
            sage: pos['X'][1] == 0 and pos[0][1] == 0
            True
            sage: pos[1][1] == 1
            True
        """
    def level_sets(self):
        """
        Return the level set decomposition of the digraph.

        OUTPUT: list of non empty lists of vertices of this graph

        The level set decomposition of the digraph is a list `l` such that the
        level `l[i]` contains all the vertices having all their predecessors in
        the levels `l[j]` for `j < i`, and at least one in level `l[i-1]`
        (unless `i = 0`).

        The level decomposition contains exactly the vertices not occurring in
        any cycle of the graph. In particular, the graph is acyclic if and only
        if the decomposition forms a set partition of its vertices, and we
        recover the usual level set decomposition of the corresponding poset.

        EXAMPLES::

            sage: H = DiGraph({0: [1, 2], 1: [3], 2: [3], 3: [], 5: [1, 6], 6: [2, 3]})
            sage: H.level_sets()
            [[0, 5], [1, 6], [2], [3]]

            sage: H = DiGraph({0: [1, 2], 1: [3], 2: [3], 3: [1], 5: [1, 6], 6: [2, 3]})
            sage: H.level_sets()
            [[0, 5], [6], [2]]

        This routine is mostly used for Hasse diagrams of posets::

            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: H = HasseDiagram({0: [1, 2], 1: [3], 2: [3], 3: []})
            sage: [len(x) for x in H.level_sets()]
            [1, 2, 1]

        ::

            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: H = HasseDiagram({0: [1, 2], 1: [3], 2: [4], 3: [4]})
            sage: [len(x) for x in H.level_sets()]
            [1, 2, 1, 1]

        Complexity: `O(n+m)` in time and `O(n)` in memory (besides the storage
        of the graph itself), where `n` and `m` are respectively the number of
        vertices and edges (assuming that appending to a list is constant time,
        which it is not quite).
        """
    def is_aperiodic(self):
        """
        Return whether the current ``DiGraph`` is aperiodic.

        A directed graph is aperiodic if there is no integer `k > 1` that
        divides the length of every cycle in the graph. See the
        :wikipedia:`Aperiodic_graph` for more information.

        EXAMPLES:

        The following graph has period ``2``, so it is not aperiodic::

            sage: g = DiGraph({0: [1], 1: [0]})
            sage: g.is_aperiodic()
            False

        The following graph has a cycle of length 2 and a cycle of length 3,
        so it is aperiodic::

            sage: g = DiGraph({0: [1, 4], 1: [2], 2: [0], 4: [0]})
            sage: g.is_aperiodic()
            True

        .. SEEALSO::

            :meth:`period`
        """
    def period(self):
        """
        Return the period of the current ``DiGraph``.

        The period of a directed graph is the largest integer that divides the
        length of every cycle in the graph. See the :wikipedia:`Aperiodic_graph`
        for more information.

        EXAMPLES:

        The following graph has period ``2``::

            sage: g = DiGraph({0: [1], 1: [0]})
            sage: g.period()
            2

        The following graph has a cycle of length 2 and a cycle of length 3,
        so it has period ``1``::

            sage: g = DiGraph({0: [1, 4], 1: [2], 2: [0], 4: [0]})
            sage: g.period()
            1

        Here is an example of computing the period of a digraph which is not
        strongly connected. By definition, it is the :func:`gcd` of the periods
        of its strongly connected components::

            sage: g = DiGraph({-1: [-2], -2: [-3], -3: [-1],
            ....:     1: [2], 2: [1]})
            sage: g.period()
            1
            sage: sorted([s.period() for s
            ....:         in g.strongly_connected_components_subgraphs()])
            [2, 3]

        ALGORITHM:

        See the networkX implementation of ``is_aperiodic``, that is based on
        breadth first search.

        .. SEEALSO::

            :meth:`is_aperiodic`
        """
    def flow_polytope(self, edges=None, ends=None, backend=None):
        """
        Return the flow polytope of a digraph.

        The flow polytope of a directed graph is the polytope consisting of all
        nonnegative flows on the graph with a given set `S` of sources and a
        given set `T` of sinks.

        A *flow* on a directed graph `G` with a given set `S` of sources and a
        given set `T` of sinks means an assignment of a nonnegative real to each
        edge of `G` such that the flow is conserved in each vertex outside of
        `S` and `T`, and there is a unit of flow entering each vertex in `S` and
        a unit of flow leaving each vertex in `T`. These flows clearly form a
        polytope in the space of all assignments of reals to the edges of `G`.

        The polytope is empty unless the sets `S` and `T` are equinumerous.

        By default, `S` is taken to be the set of all sources (i.e., vertices of
        indegree `0`) of `G`, and `T` is taken to be the set of all sinks (i.e.,
        vertices of outdegree `0`) of `G`. If a different choice of `S` and `T`
        is desired, it can be specified using the optional ``ends`` parameter.

        The polytope is returned as a polytope in `\\RR^m`, where `m` is the
        number of edges of the digraph ``self``. The `k`-th coordinate of a
        point in the polytope is the real assigned to the `k`-th edge of
        ``self``. The order of the edges is the one returned by
        ``self.edges(sort=True)``. If a different order is desired, it can be specified
        using the optional ``edges`` parameter.

        The faces and volume of these polytopes are of interest. Examples of
        these polytopes are the Chan-Robbins-Yuen polytope and the
        Pitman-Stanley polytope [PS2002]_.

        INPUT:

        - ``edges`` -- list (default: ``None``); a list of edges of ``self``. If
          not specified, the list of all edges of ``self`` is used with the
          default ordering of ``self.edges(sort=True)``. This determines which coordinate
          of a point in the polytope will correspond to which edge of
          ``self``. It is also possible to specify a list which contains not all
          edges of ``self``; this results in a polytope corresponding to the
          flows which are `0` on all remaining edges. Notice that the edges
          entered here must be in the precisely same format as outputted by
          ``self.edges()``; so, if ``self.edges()`` outputs an edge in the form
          ``(1, 3, None)``, then ``(1, 3)`` will not do!

        - ``ends`` -- (default: ``(self.sources(), self.sinks())``) a
          pair `(S, T)` of an iterable `S` and an iterable `T`

        - ``backend`` -- string or ``None`` (default); the backend to use;
          see :meth:`sage.geometry.polyhedron.constructor.Polyhedron`

        .. NOTE::

            Flow polytopes can also be built through the ``polytopes.<tab>``
            object::

                sage: polytopes.flow_polytope(digraphs.Path(5))                         # needs sage.geometry.polyhedron
                A 0-dimensional polyhedron in QQ^4 defined as the convex hull of 1 vertex

        EXAMPLES:

        A commutative square::

            sage: G = DiGraph({1: [2, 3], 2: [4], 3: [4]})
            sage: fl = G.flow_polytope(); fl                                            # needs sage.geometry.polyhedron
            A 1-dimensional polyhedron in QQ^4 defined as the convex hull
            of 2 vertices
            sage: fl.vertices()                                                         # needs sage.geometry.polyhedron
            (A vertex at (0, 1, 0, 1), A vertex at (1, 0, 1, 0))

        Using a different order for the edges of the graph::

            sage: ordered_edges = G.edges(sort=True, key=lambda x: x[0] - x[1])
            sage: fl = G.flow_polytope(edges=ordered_edges); fl                         # needs sage.geometry.polyhedron
            A 1-dimensional polyhedron in QQ^4 defined as the convex hull of 2 vertices
            sage: fl.vertices()                                                         # needs sage.geometry.polyhedron
            (A vertex at (0, 1, 1, 0), A vertex at (1, 0, 0, 1))

        A tournament on 4 vertices::

            sage: H = digraphs.TransitiveTournament(4)
            sage: fl = H.flow_polytope(); fl                                            # needs sage.geometry.polyhedron
            A 3-dimensional polyhedron in QQ^6 defined as the convex hull
            of 4 vertices
            sage: fl.vertices()                                                         # needs sage.geometry.polyhedron
            (A vertex at (0, 0, 1, 0, 0, 0),
             A vertex at (0, 1, 0, 0, 0, 1),
             A vertex at (1, 0, 0, 0, 1, 0),
             A vertex at (1, 0, 0, 1, 0, 1))

        Restricting to a subset of the edges::

            sage: fl = H.flow_polytope(edges=[(0, 1, None), (1, 2, None),               # needs sage.geometry.polyhedron
            ....:                             (2, 3, None), (0, 3, None)]); fl
            A 1-dimensional polyhedron in QQ^4 defined as the convex hull
            of 2 vertices
            sage: fl.vertices()                                                         # needs sage.geometry.polyhedron
            (A vertex at (0, 0, 0, 1), A vertex at (1, 1, 1, 0))

        Using a different choice of sources and sinks::

            sage: # needs sage.geometry.polyhedron
            sage: fl = H.flow_polytope(ends=([1], [3])); fl
            A 1-dimensional polyhedron in QQ^6 defined as the convex hull
            of 2 vertices
            sage: fl.vertices()
            (A vertex at (0, 0, 0, 1, 0, 1), A vertex at (0, 0, 0, 0, 1, 0))
            sage: fl = H.flow_polytope(ends=([0, 1], [3])); fl
            The empty polyhedron in QQ^6
            sage: fl = H.flow_polytope(ends=([3], [0])); fl
            The empty polyhedron in QQ^6
            sage: fl = H.flow_polytope(ends=([0, 1], [2, 3])); fl
            A 3-dimensional polyhedron in QQ^6 defined as the convex hull
            of 5 vertices
            sage: fl.vertices()
            (A vertex at (0, 0, 1, 1, 0, 0),
             A vertex at (0, 1, 0, 0, 1, 0),
             A vertex at (1, 0, 0, 2, 0, 1),
             A vertex at (1, 0, 0, 1, 1, 0),
             A vertex at (0, 1, 0, 1, 0, 1))
            sage: fl = H.flow_polytope(edges=[(0, 1, None), (1, 2, None),
            ....:                             (2, 3, None), (0, 2, None),
            ....:                             (1, 3, None)],
            ....:                      ends=([0, 1], [2, 3])); fl
            A 2-dimensional polyhedron in QQ^5 defined as the convex hull
            of 4 vertices
            sage: fl.vertices()
            (A vertex at (0, 0, 0, 1, 1),
             A vertex at (1, 2, 1, 0, 0),
             A vertex at (1, 1, 0, 0, 1),
             A vertex at (0, 1, 1, 1, 0))

        A digraph with one source and two sinks::

            sage: Y = DiGraph({1: [2], 2: [3, 4]})
            sage: Y.flow_polytope()                                                     # needs sage.geometry.polyhedron
            The empty polyhedron in QQ^3

        A digraph with one vertex and no edge::

            sage: Z = DiGraph({1: []})
            sage: Z.flow_polytope()                                                     # needs sage.geometry.polyhedron
            A 0-dimensional polyhedron in QQ^0 defined as the convex hull
            of 1 vertex

        A digraph with multiple edges (:issue:`28837`)::

            sage: G = DiGraph([(0, 1), (0,1)], multiedges=True); G
            Multi-digraph on 2 vertices
            sage: P = G.flow_polytope(); P                                              # needs sage.geometry.polyhedron
            A 1-dimensional polyhedron in QQ^2 defined as the convex hull of 2 vertices
            sage: P.vertices()                                                          # needs sage.geometry.polyhedron
            (A vertex at (1, 0), A vertex at (0, 1))
            sage: P.lines()                                                             # needs sage.geometry.polyhedron
            ()
        """
    def is_tournament(self):
        """
        Check whether the digraph is a tournament.

        A tournament is a digraph in which each pair of distinct vertices is
        connected by a single arc.

        EXAMPLES::

            sage: g = digraphs.RandomTournament(6)
            sage: g.is_tournament()
            True
            sage: u,v = next(g.edge_iterator(labels=False))
            sage: g.add_edge(v, u)
            sage: g.is_tournament()
            False
            sage: g.add_edges([(u, v), (v, u)])
            sage: g.is_tournament()
            False

        .. SEEALSO::

            - :wikipedia:`Tournament_(graph_theory)`
            - :meth:`~sage.graphs.digraph_generators.DiGraphGenerators.RandomTournament`
            - :meth:`~sage.graphs.digraph_generators.DiGraphGenerators.TransitiveTournament`
        """
    def out_branchings(self, source, spanning: bool = True):
        """
        Return an iterator over the out branchings rooted at given vertex in
        ``self``.

        An out-branching is a directed tree rooted at ``source`` whose arcs are
        directed from source to leaves. An out-branching is spanning if it
        contains all vertices of the digraph.

        If no spanning out branching rooted at ``source`` exist, raises
        :exc:`ValueError` or return non spanning out branching rooted at
        ``source``, depending on the value of ``spanning``.

        INPUT:

        - ``source`` -- vertex used as the source for all out branchings

        - ``spanning`` -- boolean (default: ``True``); if ``False`` return
          maximum out branching from ``source``. Otherwise, return spanning out
          branching if exists.

        OUTPUT: an iterator over the out branchings rooted in the given source

        .. SEEALSO::

            - :meth:`~sage.graphs.digraph.DiGraph.in_branchings`
              -- iterator over in-branchings rooted at given vertex.
            - :meth:`~sage.graphs.graph.Graph.spanning_trees`
              -- returns all spanning trees.
            - :meth:`~sage.graphs.generic_graph.GenericGraph.spanning_trees_count`
              -- counts the number of spanning trees.

        ALGORITHM:

        Recursively computes all out branchings.

        At each step:

            0. clean the graph (see below)
            1. pick an edge e out of source
            2. find all out branchings that do not contain e by first
               removing it
            3. find all out branchings that do contain e by first
               merging the end vertices of e

        Cleaning the graph implies to remove loops and replace multiedges by a
        single one with an appropriate label since these lead to similar steps
        of computation.

        EXAMPLES:

        A bidirectional 4-cycle::

            sage: G = DiGraph({1:[2,3], 2:[1,4], 3:[1,4], 4:[2,3]}, format='dict_of_lists')
            sage: list(G.out_branchings(1))
            [Digraph on 4 vertices,
             Digraph on 4 vertices,
             Digraph on 4 vertices,
             Digraph on 4 vertices]

        With the Petersen graph turned into a symmetric directed graph::

            sage: G = graphs.PetersenGraph().to_directed()
            sage: len(list(G.out_branchings(0)))
            2000

        With a non connected ``DiGraph`` and ``spanning = True``::

            sage: G = graphs.PetersenGraph().to_directed() + graphs.PetersenGraph().to_directed()
            sage: G.out_branchings(0, spanning=True)
            Traceback (most recent call last):
            ...
            ValueError: no spanning out branching from vertex (0) exist

        With a non connected ``DiGraph`` and ``spanning = False``::

            sage: g=DiGraph([(0,1), (0,1), (1,2), (3,4)],multiedges=True)
            sage: list(g.out_branchings(0, spanning=False))
            [Digraph on 3 vertices, Digraph on 3 vertices]

        With multiedges::

            sage: G = DiGraph({0:[1,1,1], 1:[2,2]}, format='dict_of_lists', multiedges=True)
            sage: len(list(G.out_branchings(0)))
            6

        With a DiGraph already being a spanning out branching::

            sage: G = DiGraph({0:[1,2], 1:[3,4], 2:[5], 3:[], 4:[], 5:[]}, format='dict_of_lists')
            sage: next(G.out_branchings(0)) == G
            True

        TESTS:

        The empty ``DiGraph``::

            sage: G = DiGraph()
            sage: G.out_branchings(0)
            Traceback (most recent call last):
            ...
            ValueError: vertex (0) is not a vertex of the digraph

            sage: edges = [(0,0,'x'), (0,0,'y')]
            sage: G = DiGraph(edges, multiedges=True, loops=True, weighted=True)
            sage: list(G.out_branchings(0))
            [Digraph on 1 vertex]

            sage: edges = [(0,1,'x'), (0,1,'y'), (1,2,'z'), (2,0,'w')]
            sage: G = DiGraph(edges, multiedges=True, loops=True, weighted=True)
            sage: len(list(G.out_branchings(0)))
            2
        """
    def in_branchings(self, source, spanning: bool = True):
        """
        Return an iterator over the in branchings rooted at given vertex in
        ``self``.

        An in-branching is a directed tree rooted at ``source`` whose arcs are
        directed to source from leaves. An in-branching is spanning if it
        contains all vertices of the digraph.

        If no spanning in branching rooted at ``source`` exist, raises
        :exc:`ValueError` or return non spanning in branching rooted at
        ``source``, depending on the value of ``spanning``.

        INPUT:

        - ``source`` -- vertex used as the source for all in branchings

        - ``spanning`` -- boolean (default: ``True``); if ``False`` return
          maximum in branching to ``source``. Otherwise, return spanning in
          branching if exists.

        OUTPUT: an iterator over the in branchings rooted in the given source

        .. SEEALSO::

            - :meth:`~sage.graphs.digraph.DiGraph.out_branchings`
              -- iterator over out-branchings rooted at given vertex.
            - :meth:`~sage.graphs.graph.Graph.spanning_trees`
              -- returns all spanning trees.
            - :meth:`~sage.graphs.generic_graph.GenericGraph.spanning_trees_count`
              -- counts the number of spanning trees.

        ALGORITHM:

        Recursively computes all in branchings.

        At each step:

            0. clean the graph (see below)
            1. pick an edge e incoming to source
            2. find all in branchings that do not contain e by first
               removing it
            3. find all in branchings that do contain e by first
               merging the end vertices of e

        Cleaning the graph implies to remove loops and replace multiedges by a
        single one with an appropriate label since these lead to similar steps
        of computation.

        EXAMPLES:

        A bidirectional 4-cycle::

            sage: G = DiGraph({1:[2,3], 2:[1,4], 3:[1,4], 4:[2,3]}, format='dict_of_lists')
            sage: list(G.in_branchings(1))
            [Digraph on 4 vertices,
             Digraph on 4 vertices,
             Digraph on 4 vertices,
             Digraph on 4 vertices]

        With the Petersen graph turned into a symmetric directed graph::

            sage: G = graphs.PetersenGraph().to_directed()
            sage: len(list(G.in_branchings(0)))
            2000

        With a non connected ``DiGraph`` and ``spanning = True``::

            sage: G = graphs.PetersenGraph().to_directed() + graphs.PetersenGraph().to_directed()
            sage: G.in_branchings(0)
            Traceback (most recent call last):
            ...
            ValueError: no spanning in branching to vertex (0) exist

        With a non connected ``DiGraph`` and ``spanning = False``::

            sage: g=DiGraph([(1,0), (1,0), (2,1), (3,4)],multiedges=True)
            sage: list(g.in_branchings(0,spanning=False))
            [Digraph on 3 vertices, Digraph on 3 vertices]

        With multiedges::

            sage: G = DiGraph({0:[1,1,1], 1:[2,2]}, format='dict_of_lists', multiedges=True)
            sage: len(list(G.in_branchings(2)))
            6

        With a DiGraph already being a spanning in branching::

            sage: G = DiGraph({0:[], 1:[0], 2:[0], 3:[1], 4:[1], 5:[2]}, format='dict_of_lists')
            sage: next(G.in_branchings(0)) == G
            True

        TESTS:

        The empty ``DiGraph``::

            sage: G = DiGraph()
            sage: G.in_branchings(0)
            Traceback (most recent call last):
            ...
            ValueError: vertex (0) is not a vertex of the digraph

            sage: edges = [(0,0,'x'), (0,0,'y')]
            sage: G = DiGraph(edges, multiedges=True, loops=True, weighted=True)
            sage: list(G.in_branchings(0))
            [Digraph on 1 vertex]

            sage: edges = [(0,1,'x'), (0,1,'y'), (1,2,'z'), (2,0,'w')]
            sage: G = DiGraph(edges, multiedges=True, loops=True, weighted=True)
            sage: len(list(G.in_branchings(0)))
            1
        """
