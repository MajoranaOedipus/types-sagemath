from _typeshed import Incomplete
from sage.features.mcqd import Mcqd as Mcqd
from sage.graphs.asteroidal_triples import is_asteroidal_triple_free as is_asteroidal_triple_free
from sage.graphs.base.static_dense_graph import is_strongly_regular as is_strongly_regular
from sage.graphs.cliquer import all_cliques as all_cliques
from sage.graphs.comparability import is_comparability as is_comparability, is_permutation as is_permutation
from sage.graphs.connectivity import bridges as bridges, cleave as cleave, is_triconnected as is_triconnected, minimal_separators as minimal_separators, spqr_tree as spqr_tree
from sage.graphs.distances_all_pairs import is_distance_regular as is_distance_regular
from sage.graphs.domination import is_dominating as is_dominating, is_redundant as is_redundant, minimal_dominating_sets as minimal_dominating_sets, private_neighbors as private_neighbors
from sage.graphs.generic_graph import GenericGraph as GenericGraph
from sage.graphs.graph_coloring import fractional_chromatic_index as fractional_chromatic_index, fractional_chromatic_number as fractional_chromatic_number
from sage.graphs.graph_decompositions.bandwidth import bandwidth as bandwidth
from sage.graphs.graph_decompositions.clique_separators import atoms_and_clique_separators as atoms_and_clique_separators
from sage.graphs.graph_decompositions.cutwidth import cutwidth as cutwidth
from sage.graphs.graph_decompositions.graph_products import is_cartesian_product as is_cartesian_product
from sage.graphs.graph_decompositions.slice_decomposition import slice_decomposition as slice_decomposition
from sage.graphs.graph_decompositions.tree_decomposition import treelength as treelength, treewidth as treewidth
from sage.graphs.graph_decompositions.vertex_separation import pathwidth as pathwidth
from sage.graphs.hyperbolicity import hyperbolicity as hyperbolicity
from sage.graphs.independent_sets import IndependentSets as IndependentSets
from sage.graphs.isoperimetric_inequalities import cheeger_constant as cheeger_constant, edge_isoperimetric_number as edge_isoperimetric_number, vertex_isoperimetric_number as vertex_isoperimetric_number
from sage.graphs.line_graph import is_line_graph as is_line_graph
from sage.graphs.lovasz_theta import lovasz_theta as lovasz_theta
from sage.graphs.matching import has_perfect_matching as has_perfect_matching, is_bicritical as is_bicritical, is_factor_critical as is_factor_critical, is_matching_covered as is_matching_covered, matching as matching, perfect_matchings as perfect_matchings
from sage.graphs.orientations import acyclic_orientations as acyclic_orientations, bounded_outdegree_orientation as bounded_outdegree_orientation, eulerian_orientation as eulerian_orientation, minimum_outdegree_orientation as minimum_outdegree_orientation, orient as orient, orientations as orientations, random_orientation as random_orientation, strong_orientation as strong_orientation, strong_orientations_iterator as strong_orientations_iterator
from sage.graphs.partial_cube import is_partial_cube as is_partial_cube
from sage.graphs.spanning_tree import random_spanning_tree as random_spanning_tree, spanning_trees as spanning_trees
from sage.graphs.traversals import lex_M as lex_M, maximum_cardinality_search as maximum_cardinality_search, maximum_cardinality_search_M as maximum_cardinality_search_M
from sage.graphs.tutte_polynomial import tutte_polynomial as tutte_polynomial
from sage.graphs.views import EdgesView as EdgesView
from sage.graphs.weakly_chordal import is_long_antihole_free as is_long_antihole_free, is_long_hole_free as is_long_hole_free, is_weakly_chordal as is_weakly_chordal
from sage.misc.lazy_import import LazyImport as LazyImport, lazy_import as lazy_import
from sage.misc.rest_index_of_methods import doc_index as doc_index, gen_thematic_rest_table_index as gen_thematic_rest_table_index
from sage.parallel.decorate import parallel as parallel
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing

class Graph(GenericGraph):
    '''
    Undirected graph.

    A graph is a set of vertices connected by edges. See the
    :wikipedia:`Graph_(mathematics)` for more information. For a collection of
    pre-defined graphs, see the :mod:`~sage.graphs.graph_generators` module.

    A :class:`Graph` object has many methods whose list can be obtained by
    typing ``g.<tab>`` (i.e. hit the :kbd:`Tab` key) or by reading the documentation
    of :mod:`~sage.graphs.graph`, :mod:`~sage.graphs.generic_graph`, and
    :mod:`~sage.graphs.digraph`.

    INPUT:

    By default, a :class:`Graph` object is simple (i.e. no *loops* nor *multiple
    edges*) and unweighted. This can be easily tuned with the appropriate flags
    (see below).

    - ``data`` -- can be any of the following (see the ``format`` argument):

      #. ``Graph()`` -- build a graph on 0 vertices.

      #. ``Graph(5)`` -- return an edgeless graph on the 5 vertices 0,...,4.

      #. ``Graph([list_of_vertices, list_of_edges])`` -- returns a graph with
         given vertices/edges.

         To bypass auto-detection, prefer the more explicit
         ``Graph([V, E], format=\'vertices_and_edges\')``.

      #. ``Graph(list_of_edges)`` -- return a graph with a given list of edges
         (see documentation of
         :meth:`~sage.graphs.generic_graph.GenericGraph.add_edges`).

         To bypass auto-detection, prefer the more explicit
         ``Graph(L, format=\'list_of_edges\')``.

      #. ``Graph({1: [2, 3, 4], 3: [4]})`` -- return a graph by associating to
         each vertex the list of its neighbors.

         To bypass auto-detection, prefer the more explicit
         ``Graph(D, format=\'dict_of_lists\')``.

      #. ``Graph({1: {2: \'a\', 3:\'b\'} ,3:{2:\'c\'}})`` -- return a graph by
         associating a list of neighbors to each vertex and providing its edge
         label.

         To bypass auto-detection, prefer the more explicit
         ``Graph(D, format=\'dict_of_dicts\')``.

         For graphs with multiple edges, you can provide a list of labels
         instead, e.g.: ``Graph({1: {2: [\'a1\', \'a2\'], 3:[\'b\']} ,3:{2:[\'c\']}})``.

      #. ``Graph(a_symmetric_matrix)`` -- return a graph with given (weighted)
         adjacency matrix (see documentation of
         :meth:`~sage.graphs.generic_graph.GenericGraph.adjacency_matrix`).

         To bypass auto-detection, prefer the more explicit ``Graph(M,
         format=\'adjacency_matrix\')``. To take weights into account, use
         ``format=\'weighted_adjacency_matrix\'`` instead.

      #. ``Graph(a_nonsymmetric_matrix)`` -- return a graph with given incidence
         matrix (see documentation of
         :meth:`~sage.graphs.generic_graph.GenericGraph.incidence_matrix`).

         To bypass auto-detection, prefer the more explicit
         ``Graph(M, format=\'incidence_matrix\')``.

      #. ``Graph([V, f])`` -- return a graph from a vertex set ``V`` and a
         *symmetric* function ``f``. The graph contains an edge `u,v` whenever
         ``f(u,v)`` is ``True``.. Example: ``Graph([ [1..10], lambda x,y:
         abs(x-y).is_square()])``

      #. ``Graph(\':I`ES@obGkqegW~\')`` -- return a graph from a graph6 or sparse6
         string (see documentation of :meth:`graph6_string` or
         :meth:`sparse6_string`).

      #. ``Graph(a_seidel_matrix, format=\'seidel_adjacency_matrix\')`` -- return
         a graph with a given Seidel adjacency matrix (see documentation of
         :meth:`seidel_adjacency_matrix`).

      #. ``Graph(another_graph)`` -- return a graph from a Sage (di)graph,
         `pygraphviz <https://pygraphviz.github.io/>`__ graph, `NetworkX
         <https://networkx.github.io/>`__ graph, or `igraph
         <http://igraph.org/python/>`__ graph.

    - ``pos`` -- a positioning dictionary (cf. documentation of
      :meth:`~sage.graphs.generic_graph.GenericGraph.layout`). For example, to
      draw 4 vertices on a square::

         {0: [-1,-1],
          1: [ 1,-1],
          2: [ 1, 1],
          3: [-1, 1]}

    - ``name`` -- (must be an explicitly named parameter, i.e.,
       ``name=\'complete\')`` gives the graph a name

    - ``loops`` -- boolean (default: ``None``); whether to allow loops (ignored
      if data is an instance of the ``Graph`` class)

    - ``multiedges`` -- boolean (default: ``None``); whether to allow multiple
      edges (ignored if data is an instance of the ``Graph`` class)

    - ``weighted`` -- boolean (default: ``None``); whether graph thinks of
      itself as weighted or not. See
      :meth:`~sage.graphs.generic_graph.GenericGraph.weighted`.

    - ``format`` -- if set to ``None`` (default), :class:`Graph` tries to guess
      input\'s format. To avoid this possibly time-consuming step, one of the
      following values can be specified (see description above): ``\'int\'``,
      ``\'graph6\'``, ``\'sparse6\'``, ``\'rule\'``, ``\'list_of_edges\'``,
      ``\'dict_of_lists\'``, ``\'dict_of_dicts\'``, ``\'adjacency_matrix\'``,
      ``\'weighted_adjacency_matrix\'``, ``\'seidel_adjacency_matrix\'``,
      ``\'incidence_matrix\'``, ``"NX"``, ``\'igraph\'``.

    - ``sparse`` -- boolean (default: ``True``); ``sparse=True`` is an alias for
      ``data_structure="sparse"``, and ``sparse=False`` is an alias for
      ``data_structure="dense"``.

    - ``data_structure`` -- one of the following (for more information, see
      :mod:`~sage.graphs.base.overview`)

       * ``\'dense\'`` -- selects the :mod:`~sage.graphs.base.dense_graph`
         backend.

       * ``\'sparse\'`` -- selects the :mod:`~sage.graphs.base.sparse_graph`
         backend.

       * ``\'static_sparse\'`` -- selects the
         :mod:`~sage.graphs.base.static_sparse_backend` (this backend is faster
         than the sparse backend and smaller in memory, and it is immutable, so
         that the resulting graphs can be used as dictionary keys).

    - ``immutable`` -- boolean (default: ``False``); whether to create a
      immutable graph. Note that ``immutable=True`` is actually a shortcut for
      ``data_structure=\'static_sparse\'``. Set to ``False`` by default.

    - ``hash_labels`` -- boolean (default: ``None``); whether to include edge
      labels during hashing. This parameter defaults to ``True`` if the graph is
      weighted. This parameter is ignored if the graph is mutable.
      Beware that trying to hash unhashable labels will raise an error.

    - ``vertex_labels`` -- boolean (default: ``True``); whether to allow any
      object as a vertex (slower), or only the integers `0,...,n-1`, where `n`
      is the number of vertices.

    - ``convert_empty_dict_labels_to_None`` -- this arguments sets the default
      edge labels used by NetworkX (empty dictionaries) to be replaced by
      ``None``, the default Sage edge label. It is set to ``True`` iff a
      NetworkX graph is on the input.

    EXAMPLES:

    We illustrate the first seven input formats (the other two involve packages
    that are currently not standard in Sage):

    #. An integer giving the number of vertices::

        sage: g = Graph(5); g
        Graph on 5 vertices
        sage: g.vertices(sort=True)
        [0, 1, 2, 3, 4]
        sage: g.edges(sort=False)
        []

    #. A dictionary of dictionaries::

        sage: g = Graph({0:{1:\'x\',2:\'z\',3:\'a\'}, 2:{5:\'out\'}}); g
        Graph on 5 vertices

       The labels (\'x\', \'z\', \'a\', \'out\') are labels for edges. For example,
       \'out\' is the label for the edge on 2 and 5. Labels can be used as
       weights, if all the labels share some common parent.::

        sage: a, b, c, d, e, f = sorted(SymmetricGroup(3))                              # needs sage.groups
        sage: Graph({b: {d: \'c\', e: \'p\'}, c: {d: \'p\', e: \'c\'}})                         # needs sage.groups
        Graph on 4 vertices

    #. A dictionary of lists::

        sage: g = Graph({0:[1,2,3], 2:[4]}); g
        Graph on 5 vertices

    #. A list of vertices and a function describing adjacencies. Note that the
       list of vertices and the function must be enclosed in a list (i.e., [list
       of vertices, function]).

       Construct the Paley graph over GF(13).::

          sage: g = Graph([GF(13), lambda i,j: i!=j and (i-j).is_square()])             # needs sage.rings.finite_rings
          sage: g.vertices(sort=True)                                                   # needs sage.rings.finite_rings
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
          sage: g.adjacency_matrix()                                                    # needs sage.modules sage.rings.finite_rings
          [0 1 0 1 1 0 0 0 0 1 1 0 1]
          [1 0 1 0 1 1 0 0 0 0 1 1 0]
          [0 1 0 1 0 1 1 0 0 0 0 1 1]
          [1 0 1 0 1 0 1 1 0 0 0 0 1]
          [1 1 0 1 0 1 0 1 1 0 0 0 0]
          [0 1 1 0 1 0 1 0 1 1 0 0 0]
          [0 0 1 1 0 1 0 1 0 1 1 0 0]
          [0 0 0 1 1 0 1 0 1 0 1 1 0]
          [0 0 0 0 1 1 0 1 0 1 0 1 1]
          [1 0 0 0 0 1 1 0 1 0 1 0 1]
          [1 1 0 0 0 0 1 1 0 1 0 1 0]
          [0 1 1 0 0 0 0 1 1 0 1 0 1]
          [1 0 1 1 0 0 0 0 1 1 0 1 0]

       Construct the line graph of a complete graph.::

          sage: g = graphs.CompleteGraph(4)
          sage: line_graph = Graph([g.edges(sort=True, labels=false),
          ....:                     lambda i,j: len(set(i).intersection(set(j)))>0],
          ....:                    loops=False)
          sage: line_graph.vertices(sort=True)
          [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
          sage: line_graph.adjacency_matrix()                                           # needs sage.modules
          [0 1 1 1 1 0]
          [1 0 1 1 0 1]
          [1 1 0 0 1 1]
          [1 1 0 0 1 1]
          [1 0 1 1 0 1]
          [0 1 1 1 1 0]

    #. A graph6 or sparse6 string: Sage automatically recognizes whether a
       string is in graph6 or sparse6 format::

           sage: s = \':I`AKGsaOs`cI]Gb~\'
           sage: Graph(s, sparse=True)
           Looped multi-graph on 10 vertices

       ::

           sage: G = Graph(\'G?????\')
           sage: G = Graph("G\'?G?C")
           Traceback (most recent call last):
           ...
           RuntimeError: the string seems corrupt: valid characters are
           ?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~
           sage: G = Graph(\'G??????\')
           Traceback (most recent call last):
           ...
           RuntimeError: the string (G??????) seems corrupt: for n = 8, the string is too long

       ::

          sage: G = Graph(":I\'AKGsaOs`cI]Gb~")
          Traceback (most recent call last):
          ...
          RuntimeError: the string seems corrupt: valid characters are
          ?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~

       There are also list functions to take care of lists of graphs::

           sage: s = \':IgMoqoCUOqeb\\n:I`AKGsaOs`cI]Gb~\\n:I`EDOAEQ?PccSsge\\\\N\\n\'
           sage: graphs_list.from_sparse6(s)
           [Looped multi-graph on 10 vertices,
            Looped multi-graph on 10 vertices,
            Looped multi-graph on 10 vertices]

    #. A Sage matrix:
       Note: If format is not specified, then Sage assumes a symmetric square
       matrix is an adjacency matrix, otherwise an incidence matrix.

       - an adjacency matrix::

            sage: M = graphs.PetersenGraph().am(); M                                    # needs sage.modules
            [0 1 0 0 1 1 0 0 0 0]
            [1 0 1 0 0 0 1 0 0 0]
            [0 1 0 1 0 0 0 1 0 0]
            [0 0 1 0 1 0 0 0 1 0]
            [1 0 0 1 0 0 0 0 0 1]
            [1 0 0 0 0 0 0 1 1 0]
            [0 1 0 0 0 0 0 0 1 1]
            [0 0 1 0 0 1 0 0 0 1]
            [0 0 0 1 0 1 1 0 0 0]
            [0 0 0 0 1 0 1 1 0 0]
            sage: Graph(M)                                                              # needs sage.modules
            Graph on 10 vertices

         ::

            sage: Graph(matrix([[1,2], [2,4]]), loops=True, sparse=True)                # needs sage.modules
            Looped multi-graph on 2 vertices

            sage: M = Matrix([[0,1,-1], [1,0,-1/2], [-1,-1/2,0]]); M                    # needs sage.modules
            [   0    1   -1]
            [   1    0 -1/2]
            [  -1 -1/2    0]
            sage: G = Graph(M, sparse=True); G                                          # needs sage.modules
            Graph on 3 vertices
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
            sage: Graph(M)                                                              # needs sage.modules
            Graph on 6 vertices

            sage: Graph(Matrix([[1],[1],[1]]))                                          # needs sage.modules
            Traceback (most recent call last):
            ...
            ValueError: there must be one or two nonzero entries per column
            in an incidence matrix, got entries [1, 1, 1] in column 0
            sage: Graph(Matrix([[1],[1],[0]]))                                          # needs sage.modules
            Graph on 3 vertices

            sage: M = Matrix([[0,1,-1], [1,0,-1], [-1,-1,0]]); M                        # needs sage.modules
            [ 0  1 -1]
            [ 1  0 -1]
            [-1 -1  0]
            sage: Graph(M, sparse=True)                                                 # needs sage.modules
            Graph on 3 vertices

            sage: M = Matrix([[0,1,1], [1,0,1], [-1,-1,0]]); M                          # needs sage.modules
            [ 0  1  1]
            [ 1  0  1]
            [-1 -1  0]
            sage: Graph(M)                                                              # needs sage.modules
            Traceback (most recent call last):
            ...
            ValueError: there must be one or two nonzero entries per column
            in an incidence matrix, got entries [1, 1] in column 2

        Check that :issue:`9714` is fixed::

            sage: # needs sage.modules
            sage: MA = Matrix([[1,2,0], [0,2,0], [0,0,1]])
            sage: GA = Graph(MA, format=\'adjacency_matrix\')
            sage: MI = GA.incidence_matrix(oriented=False); MI
            [2 1 1 0 0 0]
            [0 1 1 2 2 0]
            [0 0 0 0 0 2]
            sage: Graph(MI).edges(sort=True, labels=None)
            [(0, 0), (0, 1), (0, 1), (1, 1), (1, 1), (2, 2)]

            sage: M = Matrix([[1], [-1]]); M                                            # needs sage.modules
            [ 1]
            [-1]
            sage: Graph(M).edges(sort=True)                                             # needs sage.modules
            [(0, 1, None)]

    #. A Seidel adjacency matrix::

          sage: from sage.combinat.matrices.hadamard_matrix import (                    # needs sage.combinat sage.modules
          ....:  regular_symmetric_hadamard_matrix_with_constant_diagonal as rshcd)
          sage: m = rshcd(16,1) - matrix.identity(16)                                   # needs sage.combinat sage.modules
          sage: Graph(m,                                                                # needs sage.combinat sage.modules
          ....:       format=\'seidel_adjacency_matrix\').is_strongly_regular(parameters=True)
          (16, 6, 2, 2)

    #. List of edges, or labelled edges::

          sage: g = Graph([(1, 3), (3, 8), (5, 2)]); g
          Graph on 5 vertices

          sage: g = Graph([(1, 2, "Peace"), (7, -9, "and"), (77, 2, "Love")]); g
          Graph on 5 vertices
          sage: g = Graph([(0, 2, \'0\'), (0, 2, \'1\'), (3, 3, \'2\')],
          ....:           loops=True, multiedges=True)
          sage: g.loops()
          [(3, 3, \'2\')]

    #. A NetworkX MultiGraph::

          sage: import networkx                                                         # needs networkx
          sage: g = networkx.MultiGraph({0:[1,2,3], 2:[4]})                             # needs networkx
          sage: Graph(g)                                                                # needs networkx
          Multi-graph on 5 vertices

    #. A NetworkX graph::

           sage: import networkx                                                        # needs networkx
           sage: g = networkx.Graph({0:[1,2,3], 2:[4]})                                 # needs networkx
           sage: DiGraph(g)                                                             # needs networkx
           Digraph on 5 vertices

    #. An igraph Graph (see also
       :meth:`~sage.graphs.generic_graph.GenericGraph.igraph_graph`)::

           sage: import igraph                       # optional - python_igraph
           sage: g = igraph.Graph([(0, 1), (0, 2)])  # optional - python_igraph
           sage: Graph(g)                            # optional - python_igraph
           Graph on 3 vertices

       If ``vertex_labels`` is ``True``, the names of the vertices are given by
       the vertex attribute ``\'name\'``, if available::

           sage: # optional - python_igraph
           sage: g = igraph.Graph([(0,1),(0,2)], vertex_attrs={\'name\':[\'a\',\'b\',\'c\']})
           sage: Graph(g).vertices(sort=True)
           [\'a\', \'b\', \'c\']
           sage: g = igraph.Graph([(0,1),(0,2)], vertex_attrs={\'label\':[\'a\',\'b\',\'c\']})
           sage: Graph(g).vertices(sort=True)
           [0, 1, 2]

       If the igraph Graph has edge attributes, they are used as edge labels::

           sage: g = igraph.Graph([(0, 1), (0, 2)],                             # optional - python_igraph
           ....:                  edge_attrs={\'name\': [\'a\', \'b\'], \'weight\': [1, 3]})
           sage: Graph(g).edges(sort=True)                                      # optional - python_igraph
           [(0, 1, {\'name\': \'a\', \'weight\': 1}), (0, 2, {\'name\': \'b\', \'weight\': 3})]


    When defining an undirected graph from a function ``f``, it is *very*
    important that ``f`` be symmetric. If it is not, anything can happen::

        sage: f_sym = lambda x,y: abs(x-y) == 1
        sage: f_nonsym = lambda x,y: (x-y) == 1
        sage: G_sym = Graph([[4,6,1,5,3,7,2,0], f_sym])
        sage: G_sym.is_isomorphic(graphs.PathGraph(8))
        True
        sage: G_nonsym = Graph([[4,6,1,5,3,7,2,0], f_nonsym])
        sage: G_nonsym.size()
        4
        sage: G_nonsym.is_isomorphic(G_sym)
        False

    By default, graphs are mutable and can thus not be used as a dictionary
    key::

          sage: G = graphs.PetersenGraph()
          sage: {G:1}[G]
          Traceback (most recent call last):
          ...
          TypeError: This graph is mutable, and thus not hashable.
          Create an immutable copy by `g.copy(immutable=True)`

    When providing the optional arguments ``data_structure="static_sparse"`` or
    ``immutable=True`` (both mean the same), then an immutable graph results::

          sage: G_imm = Graph(G, immutable=True)
          sage: H_imm = Graph(G, data_structure=\'static_sparse\')
          sage: G_imm == H_imm == G
          True
          sage: {G_imm:1}[H_imm]
          1

    TESTS::

        sage: Graph(4, format=\'HeyHeyHey\')
        Traceback (most recent call last):
        ...
        ValueError: Unknown input format \'HeyHeyHey\'

        sage: Graph(igraph.Graph(directed=True))  # optional - python_igraph
        Traceback (most recent call last):
        ...
        ValueError: An *undirected* igraph graph was expected.
        To build a directed graph, call the DiGraph constructor.

        sage: # needs sage.modules
        sage: m = matrix([[0, -1], [-1, 0]])
        sage: Graph(m, format=\'seidel_adjacency_matrix\')
        Graph on 2 vertices
        sage: m[0,1] = 1
        sage: Graph(m, format=\'seidel_adjacency_matrix\')
        Traceback (most recent call last):
        ...
        ValueError: the adjacency matrix of a Seidel graph must be symmetric

        sage: m[0,1] = -1; m[1,1] = 1                                                   # needs sage.modules
        sage: Graph(m, format=\'seidel_adjacency_matrix\')                                # needs sage.modules
        Traceback (most recent call last):
        ...
        ValueError: the adjacency matrix of a Seidel graph must have 0s on the main diagonal

    From a list of vertices and a list of edges::

        sage: G = Graph([[1,2,3], [(1,2)]]); G
        Graph on 3 vertices
        sage: G.edges(sort=True)
        [(1, 2, None)]

    Check that :issue:`27505` is fixed::

        sage: Graph(Graph().networkx_graph(), weighted=None, format=\'NX\')               # needs networkx
        Graph on 0 vertices
    '''
    def __init__(self, data=None, pos=None, loops=None, format=None, weighted=None, data_structure: str = 'sparse', vertex_labels: bool = True, name=None, multiedges=None, convert_empty_dict_labels_to_None=None, sparse: bool = True, immutable: bool = False, hash_labels=None) -> None:
        '''
        TESTS::

            sage: G = Graph()
            sage: loads(dumps(G)) == G
            True
            sage: a = matrix(2,2,[1,0,0,1])                                             # needs sage.modules
            sage: Graph(a).adjacency_matrix() == a                                      # needs sage.modules
            True

            sage: a = matrix(2,2,[2,0,0,1])                                             # needs sage.modules
            sage: Graph(a,sparse=True).adjacency_matrix() == a                          # needs sage.modules
            True

        The positions are copied when the graph is built from another graph ::

            sage: g = graphs.PetersenGraph()
            sage: h = Graph(g)
            sage: g.get_pos() == h.get_pos()
            True

        The position dictionary is not the input one (:issue:`22424`)::

            sage: my_pos = {0:(0,0), 1:(1,1)}
            sage: G = Graph([[0,1], [(0,1)]], pos=my_pos)
            sage: my_pos == G._pos
            True
            sage: my_pos is G._pos
            False

        Or from a DiGraph ::

            sage: d = DiGraph(g)
            sage: h = Graph(d)
            sage: g.get_pos() == h.get_pos()
            True

        Loops are not counted as multiedges (see :issue:`11693`) and edges are
        not counted twice ::

            sage: Graph({1:[1]}).num_edges()
            1
            sage: Graph({1:[2,2]}).num_edges()
            2

        An empty list or dictionary defines a simple graph
        (:issue:`10441` and :issue:`12910`)::

            sage: Graph([])
            Graph on 0 vertices
            sage: Graph({})
            Graph on 0 vertices
            sage: # not "Multi-graph on 0 vertices"

        Verify that the int format works as expected (:issue:`12557`)::

            sage: Graph(2).adjacency_matrix()                                           # needs sage.modules
            [0 0]
            [0 0]
            sage: Graph(3) == Graph(3, format=\'int\')
            True

        Problem with weighted adjacency matrix (:issue:`13919`)::

            sage: B = {0:{1:2,2:5,3:4},1:{2:2,4:7},2:{3:1,4:4,5:3},3:{5:4},4:{5:1,6:5},5:{6:7}}
            sage: grafo3 = Graph(B, weighted=True)
            sage: matad = grafo3.weighted_adjacency_matrix()                            # needs sage.modules
            sage: grafo4 = Graph(matad, format=\'adjacency_matrix\', weighted=True)       # needs sage.modules
            sage: grafo4.shortest_path(0, 6, by_weight=True)                            # needs sage.modules
            [0, 1, 2, 5, 4, 6]

        Graphs returned when setting ``immutable=False`` are mutable::

            sage: g = graphs.PetersenGraph()
            sage: g = Graph(g.edges(sort=True), immutable=False)
            sage: g.add_edge("Hey", "Heyyyyyyy")

        And their name is set::

            sage: g = graphs.PetersenGraph()
            sage: Graph(g, immutable=True)
            Petersen graph: Graph on 10 vertices

        Check error messages for graphs built from incidence matrices (see
        :issue:`18440`)::

            sage: Graph(matrix([[-1, 1, 0],[1, 0, 0]]))                                 # needs sage.modules
            Traceback (most recent call last):
            ...
            ValueError: column 1 of the (oriented) incidence matrix
            contains only one nonzero value
            sage: Graph(matrix([[1,1],[1,1],[1,0]]))                                    # needs sage.modules
            Traceback (most recent call last):
            ...
            ValueError: there must be one or two nonzero entries per column
            in an incidence matrix, got entries [1, 1, 1] in column 0
            sage: Graph(matrix([[3,1,1],[0,1,1]]))                                      # needs sage.modules
            Traceback (most recent call last):
            ...
            ValueError: each column of a non-oriented incidence matrix
            must sum to 2, but column 0 does not

        Vertex labels are retained in the graph (:issue:`14708`)::

            sage: g = Graph()
            sage: g.add_vertex(0)
            sage: g.set_vertex(0, \'foo\')
            sage: g.get_vertices()
            {0: \'foo\'}
            sage: Graph(g).get_vertices()
            {0: \'foo\'}
        '''
    def graph6_string(self):
        """
        Return the graph6 representation of the graph as an ASCII string.

        This is only valid for simple (no loops, no multiple edges) graphs
        on at most `2^{18}-1=262143` vertices.

        .. NOTE::

            As the graph6 format only handles graphs with vertex set
            `\\{0,...,n-1\\}`, a :meth:`relabelled copy
            <sage.graphs.generic_graph.GenericGraph.relabel>` will
            be encoded, if necessary.

        .. SEEALSO::

            * :meth:`~sage.graphs.digraph.DiGraph.dig6_string` --
              a similar string format for directed graphs

        EXAMPLES::

            sage: G = graphs.KrackhardtKiteGraph()
            sage: G.graph6_string()
            'IvUqwK@?G'

        TESTS::

            sage: Graph().graph6_string()
            '?'
        """
    def sparse6_string(self):
        """
        Return the sparse6 representation of the graph as an ASCII string.

        Only valid for undirected graphs on 0 to 262143 vertices, but loops
        and multiple edges are permitted.

        .. NOTE::

            As the sparse6 format only handles graphs whose vertex set is
            `\\{0,...,n-1\\}`, a :meth:`relabelled copy
            <sage.graphs.generic_graph.GenericGraph.relabel>` of your graph will
            be encoded if necessary.

        EXAMPLES::

            sage: G = graphs.BullGraph()
            sage: G.sparse6_string()
            ':Da@en'

        ::

            sage: G = Graph(loops=True, multiedges=True, data_structure='sparse')
            sage: Graph(':?', data_structure='sparse') == G
            True

        TESTS::

            sage: G = Graph()
            sage: G.sparse6_string()
            ':?'

        Check that :issue:`18445` is fixed::

            sage: Graph(graphs.KneserGraph(5,2).sparse6_string()).size()
            15

        Graphs with 1 vertex are correctly handled (:issue:`24923`)::

            sage: Graph([(0, 0)], loops=True).sparse6_string()
            ':@^'
            sage: G = Graph(_)
            sage: G.order(), G.size()
            (1, 1)
            sage: Graph([(0, 0), (0, 0)], loops=True, multiedges=True).sparse6_string()
            ':@N'
            sage: H = Graph(_)
            sage: H.order(), H.size()
            (1, 2)

        Sparse6 encoding of canonical graph is unique (:issue:`31026`)::

            sage: G = Graph([(0,1),(1,2),(2,3),(3,0),(0,2)])
            sage: H = Graph([(0,1),(1,2),(2,3),(3,0),(1,3)])
            sage: G == H
            False
            sage: G.is_isomorphic(H)
            True
            sage: G.sparse6_string() == H.sparse6_string()
            False
            sage: G_ = G.canonical_label()
            sage: H_ = H.canonical_label()
            sage: G_ == H_
            True
            sage: G_.sparse6_string() == H_.sparse6_string()
            True

        The method can handle vertices with different types (:issue:`31026`)::

            sage: G = Graph([(1, 'a')])
            sage: H = Graph(G.sparse6_string())
            sage: G.is_isomorphic(H)
            True
            sage: set(G) == set(H)
            False
        """
    def is_directed(self):
        """
        Since graph is undirected, returns False.

        EXAMPLES::

            sage: Graph().is_directed()
            False
        """
    def is_tree(self, certificate: bool = False, output: str = 'vertex'):
        """
        Test if the graph is a tree.

        The empty graph is defined to be not a tree.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); whether to return a
          certificate. The method only returns boolean answers when
          ``certificate = False`` (default). When it is set to ``True``, it
          either answers ``(True, None)`` when the graph is a tree or ``(False,
          cycle)`` when it contains a cycle. It returns ``(False, None)`` when
          the graph is empty or not connected.

        - ``output`` -- either ``'vertex'`` (default) or ``'edge'``; whether the
          certificate is given as a list of vertices (``output = 'vertex'``) or
          a list of edges (``output = 'edge'``).

        When the certificate cycle is given as a list of edges, the edges are
        given as `(v_i, v_{i+1}, l)` where `v_1, v_2, \\dots, v_n` are the
        vertices of the cycles (in their cyclic order).

        EXAMPLES::

            sage: all(T.is_tree() for T in graphs.trees(15))
            True

        With certificates::

            sage: g = graphs.RandomTree(30)
            sage: g.is_tree(certificate=True)
            (True, None)
            sage: g.add_edge(10,-1)
            sage: g.add_edge(11,-1)
            sage: isit, cycle = g.is_tree(certificate=True)
            sage: isit
            False
            sage: -1 in cycle
            True

        One can also ask for the certificate as a list of edges::

            sage: g = graphs.CycleGraph(4)
            sage: g.is_tree(certificate=True, output='edge')
            (False, [(3, 2, None), (2, 1, None), (1, 0, None), (0, 3, None)])

        This is useful for graphs with multiple edges::

            sage: G = Graph([(1, 2, 'a'), (1, 2, 'b')], multiedges=True)
            sage: G.is_tree(certificate=True)
            (False, [1, 2])
            sage: G.is_tree(certificate=True, output='edge')
            (False, [(1, 2, 'b'), (2, 1, 'a')])

        TESTS:

        :issue:`14434` is fixed::

            sage: g = Graph({0:[1,4,5],3:[4,8,9],4:[9],5:[7,8],7:[9]})
            sage: _,cycle = g.is_tree(certificate=True)
            sage: g.size()
            10
            sage: g.add_cycle(cycle)
            sage: g.size()
            10

        The empty graph::

            sage: graphs.EmptyGraph().is_tree()
            False
            sage: graphs.EmptyGraph().is_tree(certificate=True)
            (False, None)

        :issue:`22912` is fixed::

            sage: G = Graph([(0,0), (0,1)], loops=True)
            sage: G.is_tree(certificate=True)
            (False, [0])
            sage: G.is_tree(certificate=True, output='edge')
            (False, [(0, 0, None)])

        Case of edges with incomparable types (see :issue:`35903`)::

            sage: G = Graph(multiedges=True)
            sage: G.add_cycle(['A', 1, 2, 3])
            sage: G.add_cycle(['A', 1, 2, 3])
            sage: G.is_tree(certificate=True, output='vertex')
            (False, ['A', 1])
            sage: G.is_tree(certificate=True, output='edge')
            (False, [('A', 1, None), (1, 'A', None)])
        """
    def is_forest(self, certificate: bool = False, output: str = 'vertex'):
        """
        Test if the graph is a forest, i.e. a disjoint union of trees.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); whether to return a
          certificate. The method only returns boolean answers when
          ``certificate = False`` (default). When it is set to ``True``, it
          either answers ``(True, None)`` when the graph is a forest or
          ``(False, cycle)`` when it contains a cycle.

        - ``output`` -- either ``'vertex'`` (default) or ``'edge'``; whether the
          certificate is given as a list of vertices (``output = 'vertex'``) or
          a list of edges (``output = 'edge'``).

        EXAMPLES::

            sage: seven_acre_wood = sum(graphs.trees(7), Graph())
            sage: seven_acre_wood.is_forest()
            True

        With certificates::

            sage: g = graphs.RandomTree(30)
            sage: g.is_forest(certificate=True)
            (True, None)
            sage: (2*g + graphs.PetersenGraph() + g).is_forest(certificate=True)
            (False, [64, 69, 67, 65, 60])
        """
    def is_cactus(self):
        """
        Check whether the graph is cactus graph.

        A graph is called *cactus graph* if it is connected and every pair of
        simple cycles have at most one common vertex.

        There are other definitions, see the :wikipedia:`Cactus_graph`.

        EXAMPLES::

            sage: g = Graph({1: [2], 2: [3, 4], 3: [4, 5, 6, 7], 8: [3, 5], 9: [6, 7]})
            sage: g.is_cactus()
            True

            sage: c6 = graphs.CycleGraph(6)
            sage: naphthalene = c6 + c6
            sage: naphthalene.is_cactus()  # Not connected
            False
            sage: naphthalene.merge_vertices([0, 6])
            sage: naphthalene.is_cactus()
            True
            sage: naphthalene.merge_vertices([1, 7])
            sage: naphthalene.is_cactus()
            False

        TESTS::

            sage: all(graphs.PathGraph(i).is_cactus() for i in range(5))
            True

            sage: Graph('Fli@?').is_cactus()
            False

        Test a graph that is not outerplanar, see :issue:`24480`::

            sage: graphs.Balaban10Cage().is_cactus()                                    # needs networkx
            False
        """
    def is_biconnected(self):
        """
        Test if the graph is biconnected.

        A biconnected graph is a connected graph on two or more vertices that is
        not broken into disconnected pieces by deleting any single vertex.

        .. SEEALSO::

            - :meth:`~sage.graphs.generic_graph.GenericGraph.is_connected`
            - :meth:`~sage.graphs.generic_graph.GenericGraph.blocks_and_cut_vertices`
            - :meth:`~sage.graphs.generic_graph.GenericGraph.blocks_and_cuts_tree`
            - :wikipedia:`Biconnected_graph`

        EXAMPLES::

            sage: G = graphs.PetersenGraph()
            sage: G.is_biconnected()
            True
            sage: G.add_path([0,'a','b'])
            sage: G.is_biconnected()
            False
            sage: G.add_edge('b', 1)
            sage: G.is_biconnected()
            True

        TESTS::

            sage: Graph().is_biconnected()
            False
            sage: Graph(1).is_biconnected()
            False
            sage: graphs.CompleteGraph(2).is_biconnected()
            True
        """
    def is_block_graph(self):
        """
        Return whether this graph is a block graph.

        A block graph is a connected graph in which every biconnected component
        (block) is a clique.

        .. SEEALSO::

            - :wikipedia:`Block_graph` for more details on these graphs
            - :meth:`~sage.graphs.graph_generators.GraphGenerators.RandomBlockGraph`
              -- generator of random block graphs
            - :meth:`~sage.graphs.generic_graph.GenericGraph.blocks_and_cut_vertices`
            - :meth:`~sage.graphs.generic_graph.GenericGraph.blocks_and_cuts_tree`

        EXAMPLES::

            sage: G = graphs.RandomBlockGraph(6, 2, kmax=4)
            sage: G.is_block_graph()
            True
            sage: from sage.graphs.isgci import graph_classes
            sage: G in graph_classes.Block
            True
            sage: graphs.CompleteGraph(4).is_block_graph()
            True
            sage: graphs.RandomTree(6).is_block_graph()
            True
            sage: graphs.PetersenGraph().is_block_graph()
            False
            sage: Graph(4).is_block_graph()
            False
        """
    def is_cograph(self):
        """
        Check whether the graph is cograph.

        A cograph is defined recursively: the single-vertex graph is
        cograph, complement of cograph is cograph, and disjoint union
        of two cographs is cograph. There are many other
        characterizations, see the :wikipedia:`Cograph`.

        EXAMPLES::

            sage: graphs.HouseXGraph().is_cograph()
            True
            sage: graphs.HouseGraph().is_cograph()                                      # needs sage.modules
            False

        .. TODO::

            Implement faster recognition algorithm, as for instance
            the linear time recognition algorithm using LexBFS proposed
            in [Bre2008]_.

        TESTS::

            sage: [graphs.PathGraph(i).is_cograph() for i in range(6)]                  # needs sage.modules
            [True, True, True, True, False, False]
            sage: graphs.CycleGraph(5).is_cograph()  # Self-complemented                # needs sage.modules
            False
        """
    def is_apex(self):
        """
        Test if the graph is apex.

        A graph is apex if it can be made planar by the removal of a single
        vertex. The deleted vertex is called ``an apex`` of the graph, and a
        graph may have more than one apex. For instance, in the minimal
        nonplanar graphs `K_5` or `K_{3,3}`, every vertex is an apex. The apex
        graphs include graphs that are themselves planar, in which case again
        every vertex is an apex. The null graph is also counted as an apex graph
        even though it has no vertex to remove.  If the graph is not connected,
        we say that it is apex if it has at most one non planar connected
        component and that this component is apex.  See the :wikipedia:`Apex_graph`
        for more information.

        .. SEEALSO::

          - :meth:`~Graph.apex_vertices`
          - :meth:`~sage.graphs.generic_graph.GenericGraph.is_planar`

        EXAMPLES:

        `K_5` and `K_{3,3}` are apex graphs, and each of their vertices is an
        apex::

            sage: G = graphs.CompleteGraph(5)
            sage: G.is_apex()
            True
            sage: G = graphs.CompleteBipartiteGraph(3,3)
            sage: G.is_apex()
            True

        The Petersen graph is not apex::

            sage: G = graphs.PetersenGraph()
            sage: G.is_apex()
            False

        A graph is apex if all its connected components are apex, but at most
        one is not planar::

            sage: M = graphs.Grid2dGraph(3,3)
            sage: K5 = graphs.CompleteGraph(5)
            sage: (M+K5).is_apex()
            True
            sage: (M+K5+K5).is_apex()
            False

        TESTS:

        The null graph is apex::

            sage: G = Graph()
            sage: G.is_apex()
            True

        The graph might be mutable or immutable::

            sage: G = Graph(M+K5, immutable=True)
            sage: G.is_apex()
            True
        """
    def apex_vertices(self, k=None):
        """
        Return the list of apex vertices.

        A graph is apex if it can be made planar by the removal of a single
        vertex. The deleted vertex is called ``an apex`` of the graph, and a
        graph may have more than one apex. For instance, in the minimal
        nonplanar graphs `K_5` or `K_{3,3}`, every vertex is an apex. The apex
        graphs include graphs that are themselves planar, in which case again
        every vertex is an apex. The null graph is also counted as an apex graph
        even though it has no vertex to remove.  If the graph is not connected,
        we say that it is apex if it has at most one non planar connected
        component and that this component is apex.  See the
        :wikipedia:`Apex_graph` for more information.

        .. SEEALSO::

          - :meth:`~Graph.is_apex`
          - :meth:`~sage.graphs.generic_graph.GenericGraph.is_planar`

        INPUT:

        - ``k`` -- integer (default: ``None``); when set to ``None``, the method
          returns the list of all apex of the graph, possibly empty if the graph
          is not apex. When set to a positive integer, the method ends as soon
          as `k` apex vertices are found.

        OUTPUT:

        By default, the method returns the list of all apex of the graph. When
        parameter ``k`` is set to a positive integer, the returned list is
        bounded to `k` apex vertices.

        EXAMPLES:

        `K_5` and `K_{3,3}` are apex graphs, and each of their vertices is an
        apex::

            sage: G = graphs.CompleteGraph(5)
            sage: G.apex_vertices()
            [0, 1, 2, 3, 4]
            sage: G = graphs.CompleteBipartiteGraph(3,3)
            sage: G.is_apex()
            True
            sage: G.apex_vertices()
            [0, 1, 2, 3, 4, 5]
            sage: G.apex_vertices(k=3)
            [0, 1, 2]

        A `4\\\\times 4`-grid is apex and each of its vertices is an apex. When
        adding a universal vertex, the resulting graph is apex and the universal
        vertex is the unique apex vertex ::

            sage: G = graphs.Grid2dGraph(4,4)
            sage: set(G.apex_vertices()) == set(G.vertices(sort=False))
            True
            sage: G.add_edges([('universal',v) for v in G])
            sage: G.apex_vertices()
            ['universal']

        The Petersen graph is not apex::

            sage: G = graphs.PetersenGraph()
            sage: G.apex_vertices()
            []

        A graph is apex if all its connected components are apex, but at most
        one is not planar::

            sage: M = graphs.Grid2dGraph(3,3)
            sage: K5 = graphs.CompleteGraph(5)
            sage: (M+K5).apex_vertices()
            [9, 10, 11, 12, 13]
            sage: (M+K5+K5).apex_vertices()
            []

        Neighbors of an apex of degree 2 are apex::

            sage: G = graphs.Grid2dGraph(5,5)
            sage: v = (666, 666)
            sage: G.add_path([(1, 1), v, (3, 3)])
            sage: G.is_planar()
            False
            sage: G.degree(v)
            2
            sage: sorted(G.apex_vertices())
            [(1, 1), (2, 2), (3, 3), (666, 666)]


        TESTS:

        The null graph is apex although it has no apex vertex::

            sage: G = Graph()
            sage: G.apex_vertices()
            []

        Parameter ``k`` cannot be a negative integer::

            sage: G.apex_vertices(k=-1)
            Traceback (most recent call last):
            ...
            ValueError: parameter k must be a nonnegative integer

        The graph might be mutable or immutable::

            sage: G = Graph(M+K5, immutable=True)
            sage: G.apex_vertices()
            [9, 10, 11, 12, 13]
        """
    def is_overfull(self):
        '''
        Test whether the current graph is overfull.

        A graph `G` on `n` vertices and `m` edges is said to be overfull if:

        - `n` is odd

        - It satisfies `2m > (n-1)\\Delta(G)`, where `\\Delta(G)` denotes the
          maximum degree among all vertices in `G`.

        An overfull graph must have a chromatic index of `\\Delta(G)+1`.

        EXAMPLES:

        A complete graph of order `n > 1` is overfull if and only if `n` is
        odd::

            sage: graphs.CompleteGraph(6).is_overfull()
            False
            sage: graphs.CompleteGraph(7).is_overfull()
            True
            sage: graphs.CompleteGraph(1).is_overfull()
            False

        The claw graph is not overfull::

            sage: from sage.graphs.graph_coloring import edge_coloring
            sage: g = graphs.ClawGraph()
            sage: g
            Claw graph: Graph on 4 vertices
            sage: edge_coloring(g, value_only=True)                                     # needs sage.numerical_mip
            3
            sage: g.is_overfull()
            False

        The Holt graph is an example of a overfull graph::

            sage: G = graphs.HoltGraph()
            sage: G.is_overfull()
            True

        Checking that all complete graphs `K_n` for even `0 \\leq n \\leq 100`
        are not overfull::

            sage: def check_overfull_Kn_even(n):
            ....:     i = 0
            ....:     while i <= n:
            ....:         if graphs.CompleteGraph(i).is_overfull():
            ....:             print("A complete graph of even order cannot be overfull.")
            ....:             return
            ....:         i += 2
            ....:     print("Complete graphs of even order up to %s are not overfull." % n)
            ...
            sage: check_overfull_Kn_even(100)  # long time
            Complete graphs of even order up to 100 are not overfull.

        The null graph, i.e. the graph with no vertices, is not overfull::

            sage: Graph().is_overfull()
            False
            sage: graphs.CompleteGraph(0).is_overfull()
            False

        Checking that all complete graphs `K_n` for odd `1 < n \\leq 100`
        are overfull::

            sage: def check_overfull_Kn_odd(n):
            ....:     i = 3
            ....:     while i <= n:
            ....:         if not graphs.CompleteGraph(i).is_overfull():
            ....:             print("A complete graph of odd order > 1 must be overfull.")
            ....:             return
            ....:         i += 2
            ....:     print("Complete graphs of odd order > 1 up to %s are overfull." % n)
            ...
            sage: check_overfull_Kn_odd(100)  # long time
            Complete graphs of odd order > 1 up to 100 are overfull.

        The Petersen Graph, though, is not overfull while
        its chromatic index is `\\Delta+1`::

            sage: g = graphs.PetersenGraph()
            sage: g.is_overfull()
            False
            sage: from sage.graphs.graph_coloring import edge_coloring
            sage: max(g.degree()) + 1 ==  edge_coloring(g, value_only=True)             # needs sage.numerical_mip
            True
        '''
    def is_even_hole_free(self, certificate: bool = False):
        '''
        Test whether ``self`` contains an induced even hole.

        A Hole is a cycle of length at least 4 (included). It is said to be even
        (resp. odd) if its length is even (resp. odd).

        Even-hole-free graphs always contain a bisimplicial vertex, which
        ensures that their chromatic number is at most twice their clique number
        [ACHRS2008]_.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); when ``certificate =
          False``, this method only returns ``True`` or ``False``. If
          ``certificate = True``, the subgraph found is returned instead of
          ``False``.

        EXAMPLES:

        Is the Petersen Graph even-hole-free ::

            sage: g = graphs.PetersenGraph()
            sage: g.is_even_hole_free()                                                 # needs sage.modules
            False

        As any chordal graph is hole-free, interval graphs behave the same way::

            sage: g = graphs.RandomIntervalGraph(20)
            sage: g.is_even_hole_free()                                                 # needs sage.modules
            True

        It is clear, though, that a random Bipartite Graph which is not a forest
        has an even hole::

            sage: g = graphs.RandomBipartite(10, 10, .5)                                # needs numpy
            sage: g.is_even_hole_free() and not g.is_forest()                           # needs numpy sage.modules
            False

        We can check the certificate returned is indeed an even cycle::

            sage: if not g.is_forest():                                                 # needs numpy sage.modules
            ....:    cycle = g.is_even_hole_free(certificate=True)
            ....:    if cycle.order() % 2 == 1:
            ....:        print("Error !")
            ....:    if not cycle.is_isomorphic(
            ....:           graphs.CycleGraph(cycle.order())):
            ....:        print("Error !")
            ...
            sage: print("Everything is Fine !")
            Everything is Fine !

        TESTS:

        Bug reported in :issue:`9925`, and fixed by :issue:`9420`::

            sage: g = Graph(\':SiBFGaCEF_@CE`DEGH`CEFGaCDGaCDEHaDEF`CEH`ABCDEF\',
            ....:           loops=False, multiedges=False)
            sage: g.is_even_hole_free()                                                 # needs sage.modules
            False
            sage: g.is_even_hole_free(certificate=True)                                 # needs sage.modules
            Subgraph of (): Graph on 4 vertices

        Making sure there are no other counter-examples around ::

            sage: t = lambda x: (Graph(x).is_forest() or
            ....:       isinstance(Graph(x).is_even_hole_free(certificate=True), Graph))
            sage: all(t(graphs.RandomBipartite(10, 10, .5)) for i in range(100))        # needs numpy sage.modules
            True
        '''
    def is_odd_hole_free(self, certificate: bool = False):
        """
        Test whether ``self`` contains an induced odd hole.

        A Hole is a cycle of length at least 4 (included). It is said to be even
        (resp. odd) if its length is even (resp. odd).

        It is interesting to notice that while it is polynomial to check whether
        a graph has an odd hole or an odd antihole [CCLSV2005]_, it is not known
        whether testing for one of these two cases independently is polynomial
        too.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); when ``certificate =
          False``, this method only returns ``True`` or ``False``. If
          ``certificate = True``, the subgraph found is returned instead of
          ``False``.

        EXAMPLES:

        Is the Petersen Graph odd-hole-free ::

            sage: g = graphs.PetersenGraph()
            sage: g.is_odd_hole_free()                                                  # needs sage.modules
            False

        Which was to be expected, as its girth is 5 ::

            sage: g.girth()
            5

        We can check the certificate returned is indeed a 5-cycle::

            sage: cycle = g.is_odd_hole_free(certificate=True)                          # needs sage.modules
            sage: cycle.is_isomorphic(graphs.CycleGraph(5))                             # needs sage.modules
            True

        As any chordal graph is hole-free, no interval graph has an odd hole::

            sage: g = graphs.RandomIntervalGraph(20)
            sage: g.is_odd_hole_free()                                                  # needs sage.modules
            True
        """
    def is_triangle_free(self, algorithm: str = 'dense_graph', certificate: bool = False):
        '''
        Check whether ``self`` is triangle-free.

        INPUT:

        - ``algorithm`` -- (default: ``\'dense_graph\'``) specifies the algorithm
          to use among:

          - ``\'matrix\'`` -- tests if the trace of the adjacency matrix is
            positive

          - ``\'bitset\'`` -- encodes adjacencies into bitsets and uses fast
            bitset operations to test if the input graph contains a
            triangle. This method is generally faster than standard matrix
            multiplication.

          - ``\'dense_graph\'`` -- use the implementation of
            :mod:`sage.graphs.base.static_dense_graph`

        - ``certificate`` -- boolean (default: ``False``); whether to return a
          triangle if one is found. This parameter is ignored when ``algorithm``
          is ``\'matrix\'``.

        EXAMPLES:

        The Petersen Graph is triangle-free::

            sage: g = graphs.PetersenGraph()
            sage: g.is_triangle_free()
            True

        or a complete Bipartite Graph::

            sage: G = graphs.CompleteBipartiteGraph(5,6)
            sage: G.is_triangle_free(algorithm=\'matrix\')                                # needs sage.modules
            True
            sage: G.is_triangle_free(algorithm=\'bitset\')
            True
            sage: G.is_triangle_free(algorithm=\'dense_graph\')
            True

        a tripartite graph, though, contains many triangles::

            sage: G = (3 * graphs.CompleteGraph(5)).complement()
            sage: G.is_triangle_free(algorithm=\'matrix\')                                # needs sage.modules
            False
            sage: G.is_triangle_free(algorithm=\'bitset\')
            False
            sage: G.is_triangle_free(algorithm=\'dense_graph\')
            False

        Asking for a certificate::

            sage: K4 = graphs.CompleteGraph(4)
            sage: K4.is_triangle_free(algorithm=\'dense_graph\', certificate=True)
            (False, [0, 1, 2])
            sage: K4.is_triangle_free(algorithm=\'bitset\', certificate=True)
            (False, [0, 1, 2])

        TESTS:

        Comparison of algorithms::

            sage: for i in range(10):           # long time                             # needs networkx
            ....:     G = graphs.RandomBarabasiAlbert(50,2)
            ....:     bm = G.is_triangle_free(algorithm=\'matrix\')
            ....:     bb = G.is_triangle_free(algorithm=\'bitset\')
            ....:     bd = G.is_triangle_free(algorithm=\'dense_graph\')
            ....:     if bm != bb or bm != bd:
            ....:        print("That\'s not good!")

        Asking for an unknown algorithm::

            sage: g.is_triangle_free(algorithm=\'tip top\')
            Traceback (most recent call last):
            ...
            ValueError: Algorithm \'tip top\' not yet implemented. Please contribute.

        Check the empty graph::

            sage: graphs.EmptyGraph().is_triangle_free()
            True
        '''
    def is_split(self):
        '''
        Return ``True`` if the graph is a Split graph, ``False`` otherwise.

        A Graph `G` is said to be a split graph if its vertices `V(G)` can be
        partitioned into two sets `K` and `I` such that the vertices of `K`
        induce a complete graph, and those of `I` are an independent set.

        There is a simple test to check whether a graph is a split graph (see,
        for instance, the book "Graph Classes, a survey" [BLS1999]_ page
        203) :

        Given the degree sequence `d_1 \\geq ... \\geq d_n` of `G`, a graph is a
        split graph if and only if :

        .. MATH::

            \\sum_{i=1}^\\omega d_i = \\omega (\\omega - 1) + \\sum_{i=\\omega + 1}^nd_i

        where `\\omega = max \\{i:d_i\\geq i-1\\}`.

        EXAMPLES:

        Split graphs are, in particular, chordal graphs. Hence, The Petersen
        graph can not be split::

            sage: graphs.PetersenGraph().is_split()
            False

        We can easily build some "random" split graph by creating a complete
        graph, and adding vertices only connected to some random vertices of the
        clique::

            sage: g = graphs.CompleteGraph(10)
            sage: sets = Subsets(Set(range(10)))
            sage: for i in range(10, 25):
            ....:    g.add_edges([(i,k) for k in sets.random_element()])
            sage: g.is_split()
            True

        Another characterisation of split graph states that a graph is a split
        graph if and only if does not contain the 4-cycle, 5-cycle or `2K_2` as
        an induced subgraph. Hence for the above graph we have::

            sage: forbidden_subgraphs = [graphs.CycleGraph(4),
            ....:                        graphs.CycleGraph(5),
            ....:                        2 * graphs.CompleteGraph(2)]
            sage: sum(g.subgraph_search_count(H, induced=True)                          # needs sage.modules
            ....:     for H in forbidden_subgraphs)
            0
        '''
    def is_perfect(self, certificate: bool = False):
        """
        Test whether the graph is perfect.

        A graph `G` is said to be perfect if `\\chi(H)=\\omega(H)` hold for any
        induced subgraph `H\\subseteq_i G` (and so for `G` itself, too), where
        `\\chi(H)` represents the chromatic number of `H`, and `\\omega(H)` its
        clique number. The Strong Perfect Graph Theorem [CRST2006]_ gives
        another characterization of perfect graphs:

        A graph is perfect if and only if it contains no odd hole (cycle on an
        odd number `k` of vertices, `k>3`) nor any odd antihole (complement of a
        hole) as an induced subgraph.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); whether to return a
          certificate

        OUTPUT:

        When ``certificate = False``, this function returns a boolean
        value. When ``certificate = True``, it returns a subgraph of ``self``
        isomorphic to an odd hole or an odd antihole if any, and ``None``
        otherwise.

        EXAMPLES:

        A Bipartite Graph is always perfect ::

            sage: g = graphs.RandomBipartite(8,4,.5)                                    # needs numpy
            sage: g.is_perfect()                                                        # needs numpy sage.modules
            True

        So is the line graph of a bipartite graph::

            sage: g = graphs.RandomBipartite(4,3,0.7)                                   # needs numpy
            sage: g.line_graph().is_perfect()   # long time                             # needs numpy sage.modules
            True

        As well as the Cartesian product of two complete graphs::

            sage: g = graphs.CompleteGraph(3).cartesian_product(graphs.CompleteGraph(3))
            sage: g.is_perfect()                                                        # needs sage.modules
            True

        Interval Graphs, which are chordal graphs, too ::

            sage: g =  graphs.RandomIntervalGraph(7)
            sage: g.is_perfect()                                                        # needs sage.modules
            True

        The PetersenGraph, which is triangle-free and has chromatic number 3 is
        obviously not perfect::

            sage: g = graphs.PetersenGraph()
            sage: g.is_perfect()                                                        # needs sage.modules
            False

        We can obtain an induced 5-cycle as a certificate::

            sage: g.is_perfect(certificate=True)                                        # needs sage.modules
            Subgraph of (Petersen graph): Graph on 5 vertices

        TESTS:

        Check that :issue:`13546` has been fixed::

            sage: Graph(':FgGE@I@GxGs', loops=False, multiedges=False).is_perfect()     # needs sage.modules
            False
            sage: g = Graph({0: [2, 3, 4, 5],
            ....:            1: [3, 4, 5, 6],
            ....:            2: [0, 4, 5, 6],
            ....:            3: [0, 1, 5, 6],
            ....:            4: [0, 1, 2, 6],
            ....:            5: [0, 1, 2, 3],
            ....:            6: [1, 2, 3, 4]})
            sage: g.is_perfect()                                                        # needs sage.modules
            False

        TESTS::

            sage: Graph(':Ab').is_perfect()                                             # needs sage.modules
            Traceback (most recent call last):
            ...
            ValueError: This method is only defined for simple graphs, and yours is not one of them !
            sage: g = Graph()
            sage: g.allow_loops(True)
            sage: g.add_edge(0,0)
            sage: g.edges(sort=True)
            [(0, 0, None)]
            sage: g.is_perfect()                                                        # needs sage.modules
            Traceback (most recent call last):
            ...
            ValueError: This method is only defined for simple graphs, and yours is not one of them !
        """
    def is_edge_transitive(self):
        """
        Check if ``self`` is an edge transitive graph.

        A graph is edge-transitive if its automorphism group acts transitively
        on its edge set.

        Equivalently, if there exists for any pair of edges `uv,u'v'\\in E(G)` an
        automorphism `\\phi` of `G` such that `\\phi(uv)=u'v'` (note this does not
        necessarily mean that `\\phi(u)=u'` and `\\phi(v)=v'`).

        .. SEEALSO::

          - :wikipedia:`Edge-transitive_graph`
          - :meth:`~Graph.is_arc_transitive`
          - :meth:`~Graph.is_half_transitive`
          - :meth:`~Graph.is_semi_symmetric`

        EXAMPLES::

            sage: P = graphs.PetersenGraph()
            sage: P.is_edge_transitive()                                                # needs sage.libs.gap
            True
            sage: C = graphs.CubeGraph(3)
            sage: C.is_edge_transitive()                                                # needs sage.libs.gap
            True
            sage: G = graphs.GrayGraph()                                                # needs networkx
            sage: G.is_edge_transitive()                                                # needs networkx sage.libs.gap
            True
            sage: P = graphs.PathGraph(4)
            sage: P.is_edge_transitive()                                                # needs sage.libs.gap
            False
        """
    def is_arc_transitive(self):
        """
        Check if ``self`` is an arc-transitive graph.

        A graph is arc-transitive if its automorphism group acts transitively on
        its pairs of adjacent vertices.

        Equivalently, if there exists for any pair of edges `uv,u'v'\\in E(G)` an
        automorphism `\\phi_1` of `G` such that `\\phi_1(u)=u'` and
        `\\phi_1(v)=v'`, as well as another automorphism `\\phi_2` of `G` such
        that `\\phi_2(u)=v'` and `\\phi_2(v)=u'`

        .. SEEALSO::

          - :wikipedia:`arc-transitive_graph`
          - :meth:`~Graph.is_edge_transitive`
          - :meth:`~Graph.is_half_transitive`
          - :meth:`~Graph.is_semi_symmetric`

        EXAMPLES::

            sage: P = graphs.PetersenGraph()
            sage: P.is_arc_transitive()                                                 # needs sage.libs.gap
            True
            sage: G = graphs.GrayGraph()                                                # needs networkx
            sage: G.is_arc_transitive()                                                 # needs networkx sage.libs.gap
            False
        """
    def is_half_transitive(self):
        """
        Check if ``self`` is a half-transitive graph.

        A graph is half-transitive if it is both vertex and edge transitive
        but not arc-transitive.

        .. SEEALSO::

          - :wikipedia:`half-transitive_graph`
          - :meth:`~Graph.is_edge_transitive`
          - :meth:`~Graph.is_arc_transitive`
          - :meth:`~Graph.is_semi_symmetric`

        EXAMPLES:

        The Petersen Graph is not half-transitive::

            sage: P = graphs.PetersenGraph()
            sage: P.is_half_transitive()                                                # needs sage.libs.gap
            False

        The smallest half-transitive graph is the Holt Graph::

            sage: H = graphs.HoltGraph()
            sage: H.is_half_transitive()                                                # needs sage.libs.gap
            True
        """
    def is_semi_symmetric(self):
        """
        Check if ``self`` is semi-symmetric.

        A graph is semi-symmetric if it is regular, edge-transitive but not
        vertex-transitive.

        .. SEEALSO::

          - :wikipedia:`Semi-symmetric_graph`
          - :meth:`~Graph.is_edge_transitive`
          - :meth:`~Graph.is_arc_transitive`
          - :meth:`~Graph.is_half_transitive`

        EXAMPLES:

        The Petersen graph is not semi-symmetric::

            sage: P = graphs.PetersenGraph()
            sage: P.is_semi_symmetric()                                                 # needs sage.libs.gap
            False

        The Gray graph is the smallest possible cubic semi-symmetric graph::

            sage: G = graphs.GrayGraph()                                                # needs networkx
            sage: G.is_semi_symmetric()                                                 # needs networkx sage.libs.gap
            True

        Another well known semi-symmetric graph is the Ljubljana graph::

            sage: L = graphs.LjubljanaGraph()                                           # needs networkx
            sage: L.is_semi_symmetric()                                                 # needs networkx sage.libs.gap
            True
        """
    def is_path(self):
        """
        Check whether ``self`` is a path.

        A connected graph of order `n \\geq 2` is a path if it is a tree
        (see :meth:`is_tree`) with `n-2` vertices of degree 2 and two of
        degree 1. By convention, a graph of order 1 without loops is a path,
        but the empty graph is not a path.

        EXAMPLES:

            sage: G = graphs.PathGraph(5)
            sage: G.is_path()
            True
            sage: H = graphs.CycleGraph(5)
            sage: H.is_path()
            False
            sage: D = graphs.PathGraph(5).disjoint_union(graphs.CycleGraph(5))
            sage: D.is_path()
            False
            sage: E = graphs.EmptyGraph()
            sage: E.is_path()
            False
            sage: O = Graph([[1], []])
            sage: O.is_path()
            True
            sage: O.allow_loops(True)
            sage: O.add_edge(1, 1)
            sage: O.is_path()
            False
        """
    def is_chordal_bipartite(self, certificate: bool = False):
        '''
        Check whether the given graph is chordal bipartite.

        A graph `G` is chordal bipartite if it is bipartite and has no induced
        cycle of length at least 6.

        An edge `(x, y) \\in E` is bisimplical if `N(x) \\cup N(y)` induces a
        complete bipartite subgraph of `G`.

        A Perfect Edge Without Vertex Elimination Ordering of a bipartite graph
        `G = (X, Y, E)` is an ordering `e_1,...,e_m` of its edge set such that
        for all `1 \\leq i \\leq m`, `e_i` is a bisimplical edge of
        `G_i = (X, Y, E_i)` where `E_i` consists of the edges `e_i,e_{i+1}...,e_m`.

        A graph `G` is chordal bipartite if and only if it has a Perfect Edge
        Without Vertex Elimination Ordering. See Lemma 4 in [KKD1995]_.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); whether to return a
          certificate

        OUTPUT:

        When ``certificate`` is set to ``False`` (default) this method only
        returns ``True`` or ``False`` answers. When ``certificate`` is set to
        ``True``, the method either returns:

        * ``(True, pewveo)`` when the graph is chordal bipartite, where ``pewveo``
          is a Perfect Edge Without Vertex Elimination Ordering of edges.

        * ``(False, cycle)`` when the graph is not chordal bipartite, where
          ``cycle`` is an odd cycle or a chordless cycle of length at least 6.

        ALGORITHM:

        This algorithm is based on these facts. The first one is trivial.

        * A reduced adjacnecy matrix
          (:meth:`~sage.graphs.bipartite_graph.BipartiteGraph.reduced_adjacency_matrix`)
          of a bipartite graph has no cycle submatrix if and only if the graph is
          chordal bipartite, where cycle submatrix is 0-1 `n \\times n` matrix `n \\geq 3`
          with exactly two 1\'s in each row and column and no proper submatrix satsify
          this property.

        * A doubly lexical ordering
          (:meth:`~sage.matrix.matrix_mod2_dense.Matrix_mod2_dense.doubly_lexical_ordering`)
          of a 0-1 matrix is `\\Gamma`-free
          (:meth:`~sage.matrix.matrix_mod2_dense.Matrix_mod2_dense.is_Gamma_free`) if and
          only if the matrix has no cycle submatrix. See Theorem 5.4 in [Lub1987]_.

        Hence, checking a doubly lexical ordering of a reduced adjacency matrix
        of a bipartite graph is `\\Gamma`-free leads to detecting the graph
        is chordal bipartite. Also, this matrix contains a certificate. Hence,
        if `G` is chordal bipartite, we find a Perfect Edge Without Vertex
        Elimination Ordering of edges by Lemma 10 in [KKD1995]_.
        Otherwise, we can find a cycle submatrix by Theorem 5.2 in [Lub1987]_.
        The time complexity of this algorithm is `O(n^3)`.

        EXAMPLES:

        A non-bipartite graph is not chordal bipartite::

            sage: g = graphs.CycleGraph(5)
            sage: g.is_chordal_bipartite()
            False
            sage: _, cycle = g.is_chordal_bipartite(certificate=True)
            sage: len(cycle) % 2 == 1
            True

        A 6-cycle graph is not chordal bipartite::

            sage: g = graphs.CycleGraph(6)
            sage: g.is_chordal_bipartite()
            False
            sage: _, cycle = g.is_chordal_bipartite(certificate=True)
            sage: len(cycle) == 6
            True

        A `2 \\times n` grid graph is chordal bipartite::

            sage: g = graphs.Grid2dGraph(2, 6)
            sage: result, pewveo = g.is_chordal_bipartite(certificate=True)
            sage: result
            True

        Let us check the certificate given by Sage is indeed a perfect
        edge without vertex elimination ordering::

            sage: for e in pewveo:
            ....:     a = g.subgraph(vertices=g.neighbors(e[0]) + g.neighbors(e[1]))
            ....:     b = BipartiteGraph(a).complement_bipartite()
            ....:     if b.edges():
            ....:          raise ValueError("this should never happen")
            ....:     g.delete_edge(e)

        Let us check the certificate given by Sage is indeed a
        chordless cycle of length at least 6::

            sage: g = graphs.Grid2dGraph(3, 6)
            sage: result, cycle = g.is_chordal_bipartite(certificate=True)
            sage: result
            False
            sage: l = len(cycle); l >= 6
            True
            sage: for i in range(len(cycle)):
            ....:     if not g.has_edge(cycle[i], cycle[(i+1)%l]):
            ....:         raise ValueError("this should never happen")
            sage: h = g.subgraph(vertices=cycle)
            sage: h.is_cycle()
            True

        TESTS:

        The algorithm works correctly for disconnected graphs::

            sage: c4 = graphs.CycleGraph(4)
            sage: g = c4.disjoint_union(graphs.CycleGraph(6))
            sage: g.is_chordal_bipartite()
            False
            sage: _, cycle = g.is_chordal_bipartite(certificate=True)
            sage: len(cycle) == 6
            True
            sage: g = c4.disjoint_union(graphs.Grid2dGraph(2, 6))
            sage: g.is_chordal_bipartite()
            True
            sage: _, pewveo = g.is_chordal_bipartite(certificate=True)
            sage: for e in pewveo:
            ....:     a = g.subgraph(vertices=g.neighbors(e[0]) + g.neighbors(e[1]))
            ....:     b = BipartiteGraph(a).complement_bipartite()
            ....:     if b.edges():
            ....:          raise ValueError("this should never happen")
            ....:     g.delete_edge(e)
        '''
    def degree_constrained_subgraph(self, bounds, solver=None, verbose: int = 0, *, integrality_tolerance: float = 0.001):
        """
        Return a degree-constrained subgraph.

        Given a graph `G` and two functions `f, g:V(G)\\rightarrow \\mathbb Z`
        such that `f \\leq g`, a degree-constrained subgraph in `G` is
        a subgraph `G' \\subseteq G` such that for any vertex `v \\in G`,
        `f(v) \\leq d_{G'}(v) \\leq g(v)`.

        INPUT:

        - ``bounds`` -- (default: ``None``) two possibilities:

          - A dictionary whose keys are the vertices, and values a pair of
            real values ``(min,max)`` corresponding to the values
            `(f(v),g(v))`.

          - A function associating to each vertex a pair of
            real values ``(min,max)`` corresponding to the values
            `(f(v),g(v))`.

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

        OUTPUT:

        - When a solution exists, this method outputs the degree-constrained
          subgraph as a Graph object.

        - When no solution exists, returns ``False``.

        .. NOTE::

            - This algorithm computes the degree-constrained subgraph of minimum
              weight.
            - If the graph's edges are weighted, these are taken into account.
            - This problem can be solved in polynomial time.

        EXAMPLES:

        Is there a perfect matching in an even cycle? ::

            sage: g = graphs.CycleGraph(6)
            sage: bounds = lambda x: [1,1]
            sage: m = g.degree_constrained_subgraph(bounds=bounds)                      # needs sage.numerical.mip
            sage: m.size()                                                              # needs sage.numerical.mip
            3
        """
    def bipartite_color(self):
        """
        Return a dictionary with vertices as the keys and the color class
        as the values.

        Fails with an error if the graph is not bipartite.

        EXAMPLES::

            sage: graphs.CycleGraph(4).bipartite_color()
            {0: 1, 1: 0, 2: 1, 3: 0}
            sage: graphs.CycleGraph(5).bipartite_color()
            Traceback (most recent call last):
            ...
            RuntimeError: Graph is not bipartite.

        TESTS::

            sage: Graph().bipartite_color()
            {}
        """
    def bipartite_sets(self):
        """
        Return `(X,Y)` where `X` and `Y` are the nodes in each bipartite set of
        graph `G`.

        Fails with an error if graph is not bipartite.

        EXAMPLES::

            sage: graphs.CycleGraph(4).bipartite_sets()
            ({0, 2}, {1, 3})
            sage: graphs.CycleGraph(5).bipartite_sets()
            Traceback (most recent call last):
            ...
            RuntimeError: Graph is not bipartite.
        """
    def chromatic_index(self, solver=None, verbose: int = 0, *, integrality_tolerance: float = 0.001):
        """
        Return the chromatic index of the graph.

        The chromatic index is the minimal number of colors needed to properly
        color the edges of the graph.

        INPUT:

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

        This method is a frontend for method
        :meth:`sage.graphs.graph_coloring.edge_coloring` that uses a mixed
        integer-linear programming formulation to compute the chromatic index.

        .. SEEALSO::

            - :wikipedia:`Edge_coloring` for further details on edge coloring
            - :meth:`sage.graphs.graph_coloring.edge_coloring`
            - :meth:`~Graph.fractional_chromatic_index`
            - :meth:`~Graph.chromatic_number`

        EXAMPLES:

        The clique `K_n` has chromatic index `n` when `n` is odd and `n-1` when
        `n` is even::

            sage: graphs.CompleteGraph(4).chromatic_index()
            3
            sage: graphs.CompleteGraph(5).chromatic_index()
            5
            sage: graphs.CompleteGraph(6).chromatic_index()
            5

        The path `P_n` with `n \\geq 2` has chromatic index 2::

            sage: graphs.PathGraph(5).chromatic_index()                                 # needs sage.numerical.mip
            2

        The windmill graph with parameters `k,n` has chromatic index `(k-1)n`::

            sage: k,n = 3,4
            sage: G = graphs.WindmillGraph(k,n)
            sage: G.chromatic_index() == (k-1)*n                                        # needs sage.numerical.mip
            True

        TESTS:

        Graphs without vertices or edges::

            sage: Graph().chromatic_index()                                             # needs sage.numerical.mip
            0
            sage: Graph(2).chromatic_index()                                            # needs sage.numerical.mip
            0
        """
    def chromatic_number(self, algorithm: str = 'DLX', solver=None, verbose: int = 0, *, integrality_tolerance: float = 0.001):
        """
        Return the minimal number of colors needed to color the vertices of the
        graph.

        INPUT:

        - ``algorithm`` -- string (default: ``'DLX'``); one of the following
          algorithms:

          - ``'DLX'`` (default): the chromatic number is computed using the
            dancing link algorithm. It is inefficient speedwise to compute the
            chromatic number through the dancing link algorithm because this
            algorithm computes *all* the possible colorings to check that one
            exists.

          - ``'CP'``: the chromatic number is computed using the coefficients of
            the chromatic polynomial. Again, this method is inefficient in terms
            of speed and it only useful for small graphs.

          - ``'MILP'``: the chromatic number is computed using a mixed integer
            linear program. The performance of this implementation is affected
            by whether optional MILP solvers have been installed (see the
            :mod:`MILP module <sage.numerical.mip>`, or Sage's tutorial on
            Linear Programming).

          - ``'parallel'``: all the above algorithms are executed in parallel
            and the result is returned as soon as one algorithm ends. Observe
            that the speed of the above algorithms depends on the size and
            structure of the graph.

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

        .. SEEALSO::

            For more functions related to graph coloring, see the module
            :mod:`sage.graphs.graph_coloring`.

        EXAMPLES::

            sage: G = Graph({0: [1, 2, 3], 1: [2]})
            sage: G.chromatic_number(algorithm='DLX')
            3
            sage: G.chromatic_number(algorithm='MILP')
            3
            sage: G.chromatic_number(algorithm='CP')                                    # needs sage.libs.flint
            3
            sage: G.chromatic_number(algorithm='parallel')
            3

        A bipartite graph has (by definition) chromatic number 2::

            sage: graphs.RandomBipartite(50,50,0.7).chromatic_number()                  # needs numpy
            2

        A complete multipartite graph with `k` parts has chromatic number `k`::

            sage: all(graphs.CompleteMultipartiteGraph([5]*i).chromatic_number() == i
            ....:     for i in range(2, 5))
            True

        The complete graph has the largest chromatic number from all the graphs
        of order `n`. Namely its chromatic number is `n`::

            sage: all(graphs.CompleteGraph(i).chromatic_number() == i for i in range(10))
            True

        The Kneser graph with parameters `(n, 2)` for `n > 3` has chromatic
        number `n-2`::

            sage: all(graphs.KneserGraph(i,2).chromatic_number() == i-2 for i in range(4,6))
            True

        The Flower Snark graph has chromatic index 4 hence its line graph has
        chromatic number 4::

            sage: graphs.FlowerSnark().line_graph().chromatic_number()
            4

        TESTS::

            sage: G = Graph()
            sage: G.chromatic_number(algorithm='DLX')
            0
            sage: G.chromatic_number(algorithm='MILP')
            0
            sage: G.chromatic_number(algorithm='CP')                                    # needs sage.libs.flint
            0
            sage: G.chromatic_number(algorithm='parallel')
            0

            sage: G = Graph({0: [1, 2, 3], 1: [2]})
            sage: G.chromatic_number(algorithm='foo')
            Traceback (most recent call last):
            ...
            ValueError: the 'algorithm' keyword must be set to either 'DLX', 'MILP', 'CP' or 'parallel'

        Test on a random graph (:issue:`33559`, modified in :issue:`12379`)::

            sage: G = graphs.RandomGNP(15, .2)
            sage: algorithms = ['DLX', 'MILP', 'CP', 'parallel']
            sage: len(set([G.chromatic_number(algorithm=algo) for algo in algorithms])) == 1        # needs sage.libs.flint
            True
        """
    def coloring(self, algorithm: str = 'DLX', hex_colors: bool = False, solver=None, verbose: int = 0, *, integrality_tolerance: float = 0.001):
        '''
        Return the first (optimal) proper vertex-coloring found.

        INPUT:

        - ``algorithm`` -- select an algorithm from the following supported
          algorithms:

          - If ``algorithm="DLX"`` (default), the coloring is computed using the
            dancing link algorithm.

          - If ``algorithm="MILP"``, the coloring is computed using a mixed
            integer linear program. The performance of this implementation is
            affected by whether optional MILP solvers have been installed (see
            the :mod:`MILP module <sage.numerical.mip>`).

        - ``hex_colors`` -- boolean (default: ``False``); if ``True``, return a
          dictionary which can easily be used for plotting

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

        .. SEEALSO::

            For more functions related to graph coloring, see the
            module :mod:`sage.graphs.graph_coloring`.

        EXAMPLES::

            sage: G = Graph("Fooba")
            sage: P = G.coloring(algorithm=\'MILP\')
            sage: Q = G.coloring(algorithm=\'DLX\')
            sage: def are_equal_colorings(A, B):
            ....:     return Set(map(Set, A)) == Set(map(Set, B))
            sage: are_equal_colorings(P, [[1, 2, 3], [0, 5, 6], [4]])
            True
            sage: are_equal_colorings(P, Q)
            True

            sage: # needs sage.plot
            sage: G.plot(partition=P)
            Graphics object consisting of 16 graphics primitives
            sage: G.coloring(hex_colors=True, algorithm=\'MILP\')
            {\'#0000ff\': [4], \'#00ff00\': [0, 6, 5], \'#ff0000\': [2, 1, 3]}
            sage: H = G.coloring(hex_colors=True, algorithm=\'DLX\'); H
            {\'#0000ff\': [4], \'#00ff00\': [1, 2, 3], \'#ff0000\': [0, 5, 6]}
            sage: G.plot(vertex_colors=H)
            Graphics object consisting of 16 graphics primitives

        .. PLOT::

            g = Graph("Fooba")
            sphinx_plot(g.plot(partition=g.coloring()))

        TESTS::

            sage: G.coloring(algorithm=\'foo\')
            Traceback (most recent call last):
            ...
            ValueError: The \'algorithm\' keyword must be set to either \'DLX\' or \'MILP\'.
        '''
    def chromatic_symmetric_function(self, R=None):
        """
        Return the chromatic symmetric function of ``self``.

        Let `G` be a graph. The chromatic symmetric function `X_G` was described
        in [Sta1995]_, specifically Theorem 2.5 states that

        .. MATH::

            X_G = \\sum_{F \\subseteq E(G)} (-1)^{|F|} p_{\\lambda(F)},

        where `\\lambda(F)` is the partition of the sizes of the connected
        components of the subgraph induced by the edges `F` and `p_{\\mu}` is the
        powersum symmetric function.

        INPUT:

        - ``R`` -- (optional) the base ring for the symmetric functions;
          this uses `\\ZZ` by default

        ALGORITHM:

        We traverse a binary tree whose leaves correspond to subsets of
        edges, and whose internal vertices at depth `d` correspond to a
        choice of whether to include the `d`-th edge in a given subset.
        The components of the induced subgraph are incrementally
        updated using a disjoint-set forest. If the next edge would
        introduce a cycle to the subset, we prune the branch as the
        terms produced by the two subtrees cancel in this case.

        EXAMPLES::

            sage: s = SymmetricFunctions(ZZ).s()                                        # needs sage.combinat sage.modules
            sage: G = graphs.CycleGraph(5)
            sage: XG = G.chromatic_symmetric_function(); XG                             # needs sage.combinat sage.modules
            p[1, 1, 1, 1, 1] - 5*p[2, 1, 1, 1] + 5*p[2, 2, 1]
             + 5*p[3, 1, 1] - 5*p[3, 2] - 5*p[4, 1] + 4*p[5]
            sage: s(XG)                                                                 # needs sage.combinat sage.modules
            30*s[1, 1, 1, 1, 1] + 10*s[2, 1, 1, 1] + 10*s[2, 2, 1]

        Not all graphs have a positive Schur expansion::

            sage: G = graphs.ClawGraph()
            sage: XG = G.chromatic_symmetric_function(); XG                             # needs sage.combinat sage.modules
            p[1, 1, 1, 1] - 3*p[2, 1, 1] + 3*p[3, 1] - p[4]
            sage: s(XG)                                                                 # needs sage.combinat sage.modules
            8*s[1, 1, 1, 1] + 5*s[2, 1, 1] - s[2, 2] + s[3, 1]

        We show that given a triangle `\\{e_1, e_2, e_3\\}`, we have
        `X_G = X_{G - e_1} + X_{G - e_2} - X_{G - e_1 - e_2}`::

            sage: # needs sage.combinat sage.modules
            sage: G = Graph([[1,2],[1,3],[2,3]])
            sage: XG = G.chromatic_symmetric_function()
            sage: G1 = copy(G)
            sage: G1.delete_edge([1,2])
            sage: XG1 = G1.chromatic_symmetric_function()
            sage: G2 = copy(G)
            sage: G2.delete_edge([1,3])
            sage: XG2 = G2.chromatic_symmetric_function()
            sage: G3 = copy(G1)
            sage: G3.delete_edge([1,3])
            sage: XG3 = G3.chromatic_symmetric_function()
            sage: XG == XG1 + XG2 - XG3
            True

        TESTS::

            sage: Graph([]).chromatic_symmetric_function() == 1
            True

            sage: e = SymmetricFunctions(ZZ).e()
            sage: e(graphs.CompleteGraph(5).chromatic_symmetric_function())
            120*e[5]
        """
    def chromatic_quasisymmetric_function(self, t=None, R=None):
        """
        Return the chromatic quasisymmetric function of ``self``.

        Let `G` be a graph whose vertex set is totally ordered. The chromatic
        quasisymmetric function `X_G(t)` was first described in [SW2012]_. We
        use the equivalent definition given in [BC2018]_:

        .. MATH::

            X_G(t) = \\sum_{\\sigma=(\\sigma_1,\\ldots,\\sigma_n)}
            t^{\\operatorname{asc}(\\sigma)}
            M_{|\\sigma_1|,\\ldots,|\\sigma_n|},

        where we sum over all ordered set partitions of the vertex set of `G`
        such that each block `\\sigma_i` is an independent (i.e., stable) set of
        `G`, and where `\\operatorname{asc}(\\sigma)` denotes the number of edges
        `\\{u, v\\}` of `G` such that `u < v` and `v` appears in a later part of
        `\\sigma` than `u`.

        INPUT:

        - ``t`` -- (optional) the parameter `t`; uses the variable `t` in
          `\\ZZ[t]` by default

        - ``R`` -- (optional) the base ring for the quasisymmetric functions;
          uses the parent of `t` by default

        EXAMPLES::

            sage: # needs sage.combinat sage.modules
            sage: G = Graph([[1,2,3], [[1,3], [2,3]]])
            sage: G.chromatic_quasisymmetric_function()
            (2*t^2+2*t+2)*M[1, 1, 1] + M[1, 2] + t^2*M[2, 1]
            sage: G = graphs.PathGraph(4)
            sage: XG = G.chromatic_quasisymmetric_function(); XG
            (t^3+11*t^2+11*t+1)*M[1, 1, 1, 1] + (3*t^2+3*t)*M[1, 1, 2]
             + (3*t^2+3*t)*M[1, 2, 1] + (3*t^2+3*t)*M[2, 1, 1]
             + (t^2+t)*M[2, 2]
            sage: XG.to_symmetric_function()
            (t^3+11*t^2+11*t+1)*m[1, 1, 1, 1] + (3*t^2+3*t)*m[2, 1, 1]
             + (t^2+t)*m[2, 2]
            sage: G = graphs.CompleteGraph(4)
            sage: G.chromatic_quasisymmetric_function()
            (t^6+3*t^5+5*t^4+6*t^3+5*t^2+3*t+1)*M[1, 1, 1, 1]

        Not all chromatic quasisymmetric functions are symmetric::

            sage: G = Graph([[1,2], [1,5], [3,4], [3,5]])
            sage: G.chromatic_quasisymmetric_function().is_symmetric()                  # needs sage.combinat sage.modules
            False

        We check that at `t = 1`, we recover the usual chromatic symmetric
        function::

            sage: p = SymmetricFunctions(QQ).p()                                        # needs sage.combinat sage.modules
            sage: G = graphs.CycleGraph(5)
            sage: XG = G.chromatic_quasisymmetric_function(t=1); XG                     # needs sage.combinat sage.modules
            120*M[1, 1, 1, 1, 1] + 30*M[1, 1, 1, 2] + 30*M[1, 1, 2, 1]
             + 30*M[1, 2, 1, 1] + 10*M[1, 2, 2] + 30*M[2, 1, 1, 1]
             + 10*M[2, 1, 2] + 10*M[2, 2, 1]
            sage: p(XG.to_symmetric_function())                                         # needs sage.combinat sage.modules
            p[1, 1, 1, 1, 1] - 5*p[2, 1, 1, 1] + 5*p[2, 2, 1]
             + 5*p[3, 1, 1] - 5*p[3, 2] - 5*p[4, 1] + 4*p[5]

            sage: G = graphs.ClawGraph()
            sage: XG = G.chromatic_quasisymmetric_function(t=1); XG                     # needs sage.combinat sage.modules
            24*M[1, 1, 1, 1] + 6*M[1, 1, 2] + 6*M[1, 2, 1] + M[1, 3]
             + 6*M[2, 1, 1] + M[3, 1]
            sage: p(XG.to_symmetric_function())                                         # needs sage.combinat sage.modules
            p[1, 1, 1, 1] - 3*p[2, 1, 1] + 3*p[3, 1] - p[4]
        """
    def tutte_symmetric_function(self, R=None, t=None):
        """
        Return the Tutte symmetric function of ``self``.

        Let `G` be a graph. The Tutte symmetric function `XB_G` of the graph
        `G` was introduced in [Sta1998]_. We present the equivalent definition
        given in [CS2022]_.

        .. MATH::

            XB_G = \\sum_{\\pi \\vdash V} (1+t)^{e(\\pi)} \\tilde{m}_{\\lambda(\\pi)},

        where the sum ranges over all set-partitions `\\pi` of the vertex set
        `V`, `\\lambda(\\pi)` is the partition determined by the sizes of the
        blocks of `\\pi`, and `e(\\pi)` is the number of edges whose endpoints
        lie in the same block of `\\pi`. In particular, the coefficients of
        `XB_G` when expanded in terms of augmented monomial symmetric functions
        are polynomials in `t` with non-negative integer coefficients.

        For an integer partition `\\lambda = 1^{r_1}2^{r_2}\\cdots` expressed in
        the exponential notation, the augmented monomial symmetric function
        is defined as

        .. MATH::

            \\tilde{m}_{\\lambda} = \\left(\\prod_{i} r_i! \\right) m_{\\lambda}.

        INPUT:

        - ``R`` -- (default: the parent of ``t``) the base ring for the symmetric
          functions

        - ``t`` -- (default: `t` in `\\ZZ[t]`) the parameter `t`

        EXAMPLES::

            sage: p = SymmetricFunctions(ZZ).p()                                        # needs sage.combinat sage.modules
            sage: G = Graph([[1,2],[2,3],[3,4],[4,1],[1,3]])
            sage: XB_G = G.tutte_symmetric_function(); XB_G                             # needs sage.combinat sage.modules
            24*m[1, 1, 1, 1] + (10*t+12)*m[2, 1, 1] + (4*t^2+10*t+6)*m[2, 2]
             + (2*t^3+8*t^2+10*t+4)*m[3, 1]
             + (t^5+5*t^4+10*t^3+10*t^2+5*t+1)*m[4]
            sage: p(XB_G)                                                               # needs sage.combinat sage.modules
            p[1, 1, 1, 1] + 5*t*p[2, 1, 1] + 2*t^2*p[2, 2]
             + (2*t^3+8*t^2)*p[3, 1] + (t^5+5*t^4+8*t^3)*p[4]

        Graphs are allowed to have multiedges and loops::

            sage: G = Graph([[1,2],[2,3],[2,3]], multiedges = True)
            sage: XB_G = G.tutte_symmetric_function(); XB_G                             # needs sage.combinat sage.modules
            6*m[1, 1, 1] + (t^2+3*t+3)*m[2, 1] + (t^3+3*t^2+3*t+1)*m[3]

        We check that at `t = -1`, we recover the usual chromatic symmetric
        function::

            sage: G = Graph([[1,2],[1,2],[2,3],[3,4],[4,5]], multiedges=True)
            sage: XB_G = G.tutte_symmetric_function(t=-1); XB_G                         # needs sage.combinat sage.modules
            120*m[1, 1, 1, 1, 1] + 36*m[2, 1, 1, 1] + 12*m[2, 2, 1]
             + 2*m[3, 1, 1] + m[3, 2]
            sage: X_G = G.chromatic_symmetric_function(); X_G                           # needs sage.combinat sage.modules
            p[1, 1, 1, 1, 1] - 4*p[2, 1, 1, 1] + 3*p[2, 2, 1] + 3*p[3, 1, 1]
             - 2*p[3, 2] - 2*p[4, 1] + p[5]
            sage: XB_G == X_G                                                           # needs sage.combinat sage.modules
            True
        """
    def has_homomorphism_to(self, H, core: bool = False, solver=None, verbose: int = 0, *, integrality_tolerance: float = 0.001):
        '''
        Check whether there is a homomorphism between two graphs.

        A homomorphism from a graph `G` to a graph `H` is a function
        `\\phi:V(G)\\mapsto V(H)` such that for any edge `uv \\in E(G)` the pair
        `\\phi(u)\\phi(v)` is an edge of `H`.

        Saying that a graph can be `k`-colored is equivalent to saying that it
        has a homomorphism to `K_k`, the complete graph on `k` elements.

        For more information, see the :wikipedia:`Graph_homomorphism`.

        INPUT:

        - ``H`` -- the graph to which ``self`` should be sent

        - ``core`` -- boolean (default: ``False``; whether to minimize the size
          of the mapping\'s image (see note below). This is set to ``False`` by
          default.

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

        .. NOTE::

           One can compute the core of a graph (with respect to homomorphism)
           with this method ::

               sage: g = graphs.CycleGraph(10)
               sage: mapping = g.has_homomorphism_to(g, core=True)                      # needs sage.numerical.mip
               sage: print("The size of the core is {}".format(len(set(mapping.values()))))         # needs sage.numerical.mip
               The size of the core is 2

        OUTPUT:

        This method returns ``False`` when the homomorphism does not exist, and
        returns the homomorphism otherwise as a dictionary associating a vertex
        of `H` to a vertex of `G`.

        EXAMPLES:

        Is Petersen\'s graph 3-colorable::

            sage: P = graphs.PetersenGraph()
            sage: P.has_homomorphism_to(graphs.CompleteGraph(3)) is not False           # needs sage.numerical.mip
            True

        An odd cycle admits a homomorphism to a smaller odd cycle, but not to an
        even cycle::

            sage: g = graphs.CycleGraph(9)
            sage: g.has_homomorphism_to(graphs.CycleGraph(5)) is not False              # needs sage.numerical.mip
            True
            sage: g.has_homomorphism_to(graphs.CycleGraph(7)) is not False              # needs sage.numerical.mip
            True
            sage: g.has_homomorphism_to(graphs.CycleGraph(4)) is not False              # needs sage.numerical.mip
            False
        '''
    def fractional_clique_number(self, solver: str = 'PPL', verbose: int = 0, check_components: bool = True, check_bipartite: bool = True):
        """
        Return the fractional clique number of the graph.

        A fractional clique is a nonnegative weight function on the vertices of
        a graph such that the sum of the weights over any independent set is at
        most 1. The fractional clique number is the largest total weight of a
        fractional clique, which is equal to the fractional chromatic number by
        LP-duality.

        ALGORITHM:

        The fractional clique number is computed via the Linear Program for
        fractional chromatic number, see :meth:`fractional_chromatic_number
        <sage.graphs.graph_coloring.fractional_chromatic_number>`

        INPUT:

        - ``solver`` -- (default: ``'PPL'``) specify a Linear Program (LP)
          solver to be used. If set to ``None``, the default one is used. For
          more information on LP solvers and which default solver is used, see
          the method :meth:`solve
          <sage.numerical.mip.MixedIntegerLinearProgram.solve>` of the class
          :class:`MixedIntegerLinearProgram
          <sage.numerical.mip.MixedIntegerLinearProgram>`.

          .. NOTE::

              The default solver used here is ``'PPL'`` which provides exact
              results, i.e. a rational number, although this may be slower that
              using other solvers.

        - ``verbose`` -- integer (default: 0); sets the level of verbosity of
          the LP solver

        - ``check_components`` -- boolean (default: ``True``); whether the
          method is called on each biconnected component of `G`

        - ``check_bipartite`` -- boolean (default: ``True``); whether the graph
          is checked for bipartiteness. If the graph is bipartite then we can
          avoid creating and solving the LP.

        EXAMPLES:

        The fractional clique number of a `C_7` is `7/3`::

            sage: g = graphs.CycleGraph(7)
            sage: g.fractional_clique_number()                                          # needs sage.numerical.mip
            7/3
        """
    def maximum_average_degree(self, value_only: bool = True, solver=None, verbose: int = 0):
        """
        Return the Maximum Average Degree (MAD) of the current graph.

        The Maximum Average Degree (MAD) of a graph is defined as the average
        degree of its densest subgraph. More formally, ``Mad(G) =
        \\max_{H\\subseteq G} Ad(H)``, where `Ad(G)` denotes the average degree of
        `G`.

        This can be computed in polynomial time.

        INPUT:

        - ``value_only`` -- boolean (default: ``True``)

          - If ``value_only=True``, only the numerical value of the `MAD` is
            returned.

          - Else, the subgraph of `G` realizing the `MAD` is returned.

        - ``solver`` -- (default: ``None``) specify a Linear Program (LP)
          solver to be used. If set to ``None``, the default one is used. For
          more information on LP solvers and which default solver is used, see
          the method
          :meth:`solve <sage.numerical.mip.MixedIntegerLinearProgram.solve>`
          of the class
          :class:`MixedIntegerLinearProgram <sage.numerical.mip.MixedIntegerLinearProgram>`.

        - ``verbose`` -- integer (default: 0); sets the level of
          verbosity. Set to 0 by default, which means quiet.

        EXAMPLES:

        In any graph, the `Mad` is always larger than the average degree::

            sage: g = graphs.RandomGNP(20,.3)
            sage: mad_g = g.maximum_average_degree()                                    # needs sage.numerical.mip
            sage: g.average_degree() <= mad_g                                           # needs sage.numerical.mip
            True

        Unlike the average degree, the `Mad` of the disjoint union of two graphs
        is the maximum of the `Mad` of each graphs::

            sage: h = graphs.RandomGNP(20,.3)
            sage: mad_h = h.maximum_average_degree()                                    # needs sage.numerical.mip
            sage: (g+h).maximum_average_degree() == max(mad_g, mad_h)                   # needs sage.numerical.mip
            True

        The subgraph of a regular graph realizing the maximum average degree is
        always the whole graph ::

            sage: g = graphs.CompleteGraph(5)
            sage: mad_g = g.maximum_average_degree(value_only=False)                    # needs sage.numerical.mip
            sage: g.is_isomorphic(mad_g)                                                # needs sage.numerical.mip
            True

        This also works for complete bipartite graphs ::

            sage: g = graphs.CompleteBipartiteGraph(3,4)
            sage: mad_g = g.maximum_average_degree(value_only=False)                    # needs sage.numerical.mip
            sage: g.is_isomorphic(mad_g)                                                # needs sage.numerical.mip
            True

        TESTS:

        Check corner cases::

            sage: # needs sage.numerical.mip
            sage: Graph().maximum_average_degree(value_only=True)
            0
            sage: Graph().maximum_average_degree(value_only=False)
            Graph on 0 vertices
            sage: Graph(1).maximum_average_degree(value_only=True)
            0
            sage: Graph(1).maximum_average_degree(value_only=False)
            Graph on 1 vertex
            sage: Graph(2).maximum_average_degree(value_only=True)
            0
            sage: Graph(2).maximum_average_degree(value_only=False)
            Graph on 1 vertex
        """
    def independent_set_of_representatives(self, family, solver=None, verbose: int = 0, *, integrality_tolerance: float = 0.001):
        """
        Return an independent set of representatives.

        Given a graph `G` and a family `F=\\{F_i:i\\in [1,...,k]\\}` of subsets of
        ``g.vertices(sort=False)``, an Independent Set of Representatives (ISR) is an
        assignation of a vertex `v_i\\in F_i` to each set `F_i` such that `v_i !=
        v_j` if `i<j` (they are representatives) and the set `\\cup_{i}v_i` is an
        independent set in `G`.

        It generalizes, for example, graph coloring and graph list coloring.

        (See [ABZ2007]_ for more information.)

        INPUT:

        - ``family`` -- list of lists defining the family `F` (actually, a
          Family of subsets of ``G.vertices(sort=False)``)

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

        OUTPUT:

        - A list whose `i^{\\mbox{th}}` element is the representative of the
          `i^{\\mbox{th}}` element of the ``family`` list. If there is no ISR,
          ``None`` is returned.

        EXAMPLES:

        For a bipartite graph missing one edge, the solution is as expected::

           sage: g = graphs.CompleteBipartiteGraph(3,3)
           sage: g.delete_edge(1,4)
           sage: g.independent_set_of_representatives([[0,1,2],[3,4,5]])                # needs sage.numerical.mip
           [1, 4]

        The Petersen Graph is 3-colorable, which can be expressed as an
        independent set of representatives problem : take 3 disjoint copies of
        the Petersen Graph, each one representing one color. Then take as a
        partition of the set of vertices the family defined by the three copies
        of each vertex. The ISR of such a family defines a 3-coloring::

            sage: # needs sage.numerical.mip
            sage: g = 3 * graphs.PetersenGraph()
            sage: n = g.order() / 3
            sage: f = [[i, i + n, i + 2*n] for i in range(n)]
            sage: isr = g.independent_set_of_representatives(f)
            sage: c = [integer_floor(i / n) for i in isr]
            sage: color_classes = [[], [], []]
            sage: for v, i in enumerate(c):
            ....:   color_classes[i].append(v)
            sage: for classs in color_classes:
            ....:   g.subgraph(classs).size() == 0
            True
            True
            True
        """
    def minor(self, H, solver=None, verbose: int = 0, induced: bool = False, *, integrality_tolerance: float = 0.001):
        """
        Return the vertices of a minor isomorphic to `H` in the current graph.

        We say that a graph `G` has a `H`-minor (or that it has a graph
        isomorphic to `H` as a minor), if for all `h\\in H`, there exist disjoint
        sets `S_h \\subseteq V(G)` such that once the vertices of each `S_h` have
        been merged to create a new graph `G'`, this new graph contains `H` as a
        subgraph.

        When parameter ``induced`` is ``True``, this method returns an induced minor
        isomorphic to `H`, if it exists.

        We say that a graph `G` has an induced `H`-minor (or that it has a
        graph isomorphic to `H` as an induced minor), if `H` can be obtained
        from an induced subgraph of `G` by contracting edges. Otherwise, `G` is
        said to be `H`-induced minor-free.

        For more information, see the :wikipedia:`Minor_(graph_theory)`.

        INPUT:

        - ``H`` -- the minor to find for in the current graph

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

        - ``induced`` -- boolean (default: ``False``); if ``True``, returns an
          induced minor isomorphic to `H` if it exists, and raises a
          :exc:`ValueError` otherwise.

        OUTPUT:

        A dictionary associating to each vertex of `H` the set of vertices in
        the current graph representing it.

        ALGORITHM:

        Mixed Integer Linear Programming

        COMPLEXITY:

        Theoretically, when `H` is fixed, testing for the existence of a
        `H`-minor is polynomial. The known algorithms are highly exponential in
        `H`, though.

        .. NOTE::

            This function can be expected to be *very* slow, especially where
            the minor does not exist.

        EXAMPLES:

        Trying to find a minor isomorphic to `K_4` in the `4\\times 4` grid::

            sage: # needs sage.numerical.mip
            sage: g = graphs.GridGraph([4,4])
            sage: h = graphs.CompleteGraph(4)
            sage: L = g.minor(h)
            sage: gg = g.subgraph(flatten(L.values(), max_level = 1))
            sage: _ = [gg.merge_vertices(l) for l in L.values() if len(l)>1]
            sage: gg.is_isomorphic(h)
            True

        We can also try to prove this way that the Petersen graph is not planar,
        as it has a `K_5` minor::

            sage: g = graphs.PetersenGraph()
            sage: K5_minor = g.minor(graphs.CompleteGraph(5))   # long time             # needs sage.numerical.mip

        And even a `K_{3,3}` minor::

            sage: K33_minor = g.minor(graphs.CompleteBipartiteGraph(3,3))       # long time, needs sage.numerical.mip

        (It is much faster to use the linear-time test of planarity in this
        situation, though.)

        As there is no cycle in a tree, looking for a `K_3` minor is useless.
        This function will raise an exception in this case::

            sage: g = graphs.RandomGNP(20, .5)
            sage: g = g.subgraph(edges=g.min_spanning_tree())
            sage: g.is_tree()
            True
            sage: L = g.minor(graphs.CompleteGraph(3))                                  # needs sage.numerical.mip
            Traceback (most recent call last):
            ...
            ValueError: This graph has no minor isomorphic to H !

        Trying to find an induced minor isomorphic to `C_5` in a graph
        containing an induced `C_6`::

            sage: g = graphs.CycleGraph(6)
            sage: for i in range(randint(10, 30)):
            ....:     g.add_edge(randint(0, 5), g.add_vertex())
            sage: h = graphs.CycleGraph(5)
            sage: L = g.minor(h, induced=True)
            sage: gg = g.subgraph(flatten(L.values(), max_level=1))
            sage: _ = [gg.merge_vertices(l) for l in L.values() if len(l) > 1]
            sage: gg.is_isomorphic(h)
            True

        TESTS:

        A graph `g` may have a minor isomorphic to a given graph `h` but no
        induced minor isomorphic to `h`::

            sage: g = Graph([(0, 1), (0, 2), (1, 2), (2, 3), (3, 4), (3, 5), (4, 5), (6, 5)])
            sage: h = Graph([(9, 10), (9, 11), (9, 12), (9, 13)])
            sage: l = g.minor(h, induced=False)
            sage: l = g.minor(h, induced=True)
            Traceback (most recent call last):
            ...
            ValueError: This graph has no induced minor isomorphic to H !

        Checking that the returned induced minor is isomorphic to the given
        graph::

            sage: g = Graph([(0, 1), (0, 2), (1, 2), (2, 3), (3, 4), (3, 5), (4, 5), (6, 5)])
            sage: h = Graph([(7, 8), (8, 9), (9, 10), (10, 11)])
            sage: L = g.minor(h, induced=True)
            sage: gg = g.subgraph(flatten(L.values(), max_level=1))
            sage: _ = [gg.merge_vertices(l) for l in L.values() if len(l) > 1]
            sage: gg.is_isomorphic(h)
            True
        """
    def convexity_properties(self):
        """
        Return a ``ConvexityProperties`` object corresponding to ``self``.

        This object contains the methods related to convexity in graphs (convex
        hull, hull number) and caches useful information so that it becomes
        comparatively cheaper to compute the convex hull of many different sets
        of the same graph.

        .. SEEALSO::

            In order to know what can be done through this object, please refer
            to module :mod:`sage.graphs.convexity_properties`.

        .. NOTE::

            If you want to compute many convex hulls, keep this object in memory!
            When it is created, it builds a table of useful information to
            compute convex hulls. As a result ::

                sage: # needs sage.numerical.mip
                sage: g = graphs.PetersenGraph()
                sage: g.convexity_properties().hull([1, 3])
                [1, 2, 3]
                sage: g.convexity_properties().hull([3, 7])
                [2, 3, 7]

            is a terrible waste of computations, while ::

                sage: # needs sage.numerical.mip
                sage: g = graphs.PetersenGraph()
                sage: CP = g.convexity_properties()
                sage: CP.hull([1, 3])
                [1, 2, 3]
                sage: CP.hull([3, 7])
                [2, 3, 7]

            makes perfect sense.
        """
    def centrality_degree(self, v=None):
        """
        Return the degree centrality of a vertex.

        The degree centrality of a vertex `v` is its degree, divided by
        `|V(G)|-1`. For more information, see the :wikipedia:`Centrality`.

        INPUT:

        - ``v`` -- a vertex (default: ``None``); set to ``None`` (default) to
          get a dictionary associating each vertex with its centrality degree

        .. SEEALSO::

            - :meth:`~sage.graphs.generic_graph.GenericGraph.centrality_closeness`
            - :meth:`~sage.graphs.generic_graph.GenericGraph.centrality_betweenness`

        EXAMPLES::

            sage: (graphs.ChvatalGraph()).centrality_degree()
            {0: 4/11, 1: 4/11, 2: 4/11, 3: 4/11,  4: 4/11,  5: 4/11,
             6: 4/11, 7: 4/11, 8: 4/11, 9: 4/11, 10: 4/11, 11: 4/11}
            sage: D = graphs.DiamondGraph()
            sage: D.centrality_degree()
            {0: 2/3, 1: 1, 2: 1, 3: 2/3}
            sage: D.centrality_degree(v=1)
            1

        TESTS::

            sage: Graph(1).centrality_degree()
            Traceback (most recent call last):
            ...
            ValueError: the centrality degree is not defined on graphs with only one vertex
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

          - ``\'DHV\'`` -- the computation is done using the algorithm proposed in
            [Dragan2018]_. Works only if ``self`` has nonnegative edge weights
            and ``v is None`` or ``v`` should contain all vertices of ``self``.
            For more information see method
            :func:`sage.graphs.distances_all_pairs.eccentricity` and
            :func:`sage.graphs.base.boost_graph.eccentricity_DHV`.

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
          and ``by_weight`` is ``True``, we use the edge label ``l`` as a
          weight, if ``l`` is not ``None``, else ``1`` as a weight.

        - ``check_weight`` -- boolean (default: ``True``); if ``True``, we check
          that the ``weight_function`` outputs a number for each edge

        - ``dist_dict`` -- dictionary (default: ``None``); a dict of dicts of
          distances (used only if ``algorithm==\'From_Dictionary\'``)

        - ``with_labels`` -- boolean (default: ``False``); whether to return a
          list or a dictionary keyed by vertices

        EXAMPLES::

            sage: G = graphs.KrackhardtKiteGraph()
            sage: G.eccentricity()
            [4, 4, 4, 4, 4, 3, 3, 2, 3, 4]
            sage: G.vertices(sort=True)
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            sage: G.eccentricity(7)
            2
            sage: G.eccentricity([7,8,9])
            [2, 3, 4]
            sage: G.eccentricity([7, 8, 9], with_labels=True) == {8: 3, 9: 4, 7: 2}
            True
            sage: G = Graph({0: [], 1: [], 2: [1]})
            sage: G.eccentricity()
            [+Infinity, +Infinity, +Infinity]
            sage: G = Graph({0:[]})
            sage: G.eccentricity(with_labels=True)
            {0: 0}
            sage: G = Graph({0:[], 1:[]})
            sage: G.eccentricity(with_labels=True)
            {0: +Infinity, 1: +Infinity}
            sage: G = Graph([(0, 1, 1), (1, 2, 1), (0, 2, 3)])
            sage: G.eccentricity(algorithm=\'BFS\')
            [1, 1, 1]
            sage: G.eccentricity(algorithm=\'Floyd-Warshall-Cython\')
            [1, 1, 1]
            sage: G.eccentricity(by_weight=True, algorithm=\'Dijkstra_NetworkX\')         # needs networkx
            [2, 1, 2]
            sage: G.eccentricity(by_weight=True, algorithm=\'Dijkstra_Boost\')
            [2, 1, 2]
            sage: G.eccentricity(by_weight=True, algorithm=\'Johnson_Boost\')
            [2, 1, 2]
            sage: G.eccentricity(by_weight=True, algorithm=\'Floyd-Warshall-Python\')
            [2, 1, 2]
            sage: G.eccentricity(dist_dict=G.shortest_path_all_pairs(by_weight=True)[0])
            [2, 1, 2]
            sage: G.eccentricity(by_weight=False, algorithm=\'DHV\')
            [1, 1, 1]
            sage: G.eccentricity(by_weight=True, algorithm=\'DHV\')
            [2.0, 1.0, 2.0]

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
            sage: G.eccentricity(0, algorithm=\'DHV\')
            Traceback (most recent call last):
            ...
            ValueError: algorithm \'DHV\' works only if all eccentricities are needed
        '''
    def radius(self, by_weight: bool = False, algorithm: str = 'DHV', weight_function=None, check_weight: bool = True):
        """
        Return the radius of the graph.

        The radius is defined to be the minimum eccentricity of any vertex,
        where the eccentricity is the maximum distance to any other
        vertex. For more information and examples on how to use input variables,
        see :meth:`~GenericGraph.shortest_paths` and
        :meth:`~Graph.eccentricity`

        INPUT:

        - ``by_weight`` -- boolean (default: ``False``); if ``True``, edge
          weights are taken into account; if ``False``, all edges have weight 1

        - ``algorithm`` -- string (default: ``'DHV'``)

          - ``'DHV'`` -- radius computation is done using the algorithm proposed
            in [Dragan2018]_. Works for graph with nonnegative edge weights
            For more information see method
            :func:`sage.graphs.distances_all_pairs.radius_DHV` and
            :func:`sage.graphs.base.boost_graph.radius_DHV`.

          - see method :meth:`eccentricity` for the list of remaining algorithms

        - ``weight_function`` -- function (default: ``None``); a function that
          takes as input an edge ``(u, v, l)`` and outputs its weight. If not
          ``None``, ``by_weight`` is automatically set to ``True``. If ``None``
          and ``by_weight`` is ``True``, we use the edge label ``l`` as a
          weight, if ``l`` is not ``None``, else ``1`` as a weight.

        - ``check_weight`` -- boolean (default: ``True``); if ``True``, we check
          that the ``weight_function`` outputs a number for each edge

        EXAMPLES:

        The more symmetric a graph is, the smaller (diameter - radius) is::

            sage: G = graphs.BarbellGraph(9, 3)
            sage: G.radius()
            3
            sage: G.diameter()
            6

        ::

            sage: G = graphs.OctahedralGraph()
            sage: G.radius()
            2
            sage: G.diameter()
            2

        TESTS::

            sage: g = Graph()
            sage: g.radius()
            Traceback (most recent call last):
            ...
            ValueError: radius is not defined for the empty graph
        """
    def diameter(self, by_weight: bool = False, algorithm=None, weight_function=None, check_weight: bool = True):
        """
        Return the diameter of the graph.

        The diameter is defined to be the maximum distance between two vertices.
        It is infinite if the graph is not connected.

        The default algorithm is ``'iFUB'`` [CGILM2010]_ for unweighted graphs
        and ``'DHV'`` [Dragan2018]_ for weighted graphs.

        For more information and examples on how to use input variables, see
        :meth:`~GenericGraph.shortest_paths` and
        :meth:`~Graph.eccentricity`

        INPUT:

        - ``by_weight`` -- boolean (default: ``False``); if ``True``, edge
          weights are taken into account; if ``False``, all edges have weight 1

        - ``algorithm`` -- string (default: ``None``); one of the following
          algorithms:

          - ``'BFS'``: the computation is done through a BFS centered on each
            vertex successively. Works only if ``by_weight==False``.

          - ``'Floyd-Warshall-Cython'``: a Cython implementation of the
            Floyd-Warshall algorithm. Works only if ``by_weight==False`` and ``v
            is None``.

          - ``'Floyd-Warshall-Python'``: a Python implementation of the
            Floyd-Warshall algorithm. Works also with weighted graphs, even with
            negative weights (but no negative cycle is allowed). However, ``v``
            must be ``None``.

          - ``'Dijkstra_NetworkX'``: the Dijkstra algorithm, implemented in
            NetworkX. It works with weighted graphs, but no negative weight is
            allowed.

          - ``'DHV'`` -- diameter computation is done using the algorithm
            proposed in [Dragan2018]_. Works only for nonnegative edge weights
            For more information see method
            :func:`sage.graphs.distances_all_pairs.diameter_DHV` and
            :func:`sage.graphs.base.boost_graph.diameter_DHV`.

          - ``'standard'``, ``'2sweep'``, ``'multi-sweep'``, ``'iFUB'``:
            these algorithms are implemented in
            :func:`sage.graphs.distances_all_pairs.diameter`
            They work only if ``by_weight==False``. See the function
            documentation for more information.

          - ``'Dijkstra_Boost'``: the Dijkstra algorithm, implemented in Boost
            (works only with positive weights).

          - ``'Johnson_Boost'``: the Johnson algorithm, implemented in
            Boost (works also with negative weights, if there is no negative
            cycle).

          - ``None`` (default): Sage chooses the best algorithm: ``'iFUB'`` for
            unweighted graphs, ``'Dijkstra_Boost'`` if all weights are positive,
            ``'Johnson_Boost'`` otherwise.

        - ``weight_function`` -- function (default: ``None``); a function that
          takes as input an edge ``(u, v, l)`` and outputs its weight. If not
          ``None``, ``by_weight`` is automatically set to ``True``. If ``None``
          and ``by_weight`` is ``True``, we use the edge label ``l`` as a
          weight, if ``l`` is not ``None``, else ``1`` as a weight.

        - ``check_weight`` -- boolean (default: ``True``); if ``True``, we check
          that the ``weight_function`` outputs a number for each edge

        EXAMPLES:

        The more symmetric a graph is, the smaller (diameter - radius) is::

            sage: G = graphs.BarbellGraph(9, 3)
            sage: G.radius()
            3
            sage: G.diameter()
            6

        ::

            sage: G = graphs.OctahedralGraph()
            sage: G.radius()
            2
            sage: G.diameter()
            2

        TESTS::

            sage: g = Graph()
            sage: g.diameter()
            Traceback (most recent call last):
            ...
            ValueError: diameter is not defined for the empty graph
            sage: g = Graph([(1, 2, {'weight': 1})])
            sage: g.diameter(algorithm='iFUB', weight_function=lambda e: e[2]['weight'])
            Traceback (most recent call last):
            ...
            ValueError: algorithm 'iFUB' does not work on weighted graphs

        Check that :issue:`40013` is fixed::

            sage: G = graphs.PetersenGraph()
            sage: G.diameter(by_weight=True)
            2.0
        """
    def center(self, by_weight: bool = False, algorithm=None, weight_function=None, check_weight: bool = True):
        """
        Return the set of vertices in the center of the graph.

        The center is the set of vertices whose eccentricity is equal to the
        radius of the graph, i.e., achieving the minimum eccentricity.

        For more information and examples on how to use input variables,
        see :meth:`~GenericGraph.shortest_paths` and
        :meth:`~Graph.eccentricity`

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

        Is Central African Republic in the center of Africa in graph theoretic
        sense? Yes::

            sage: A = graphs.AfricaMap(continental=True)
            sage: sorted(A.center())
            ['Cameroon', 'Central Africa']

        Some other graphs. Center can be the whole graph::

            sage: G = graphs.DiamondGraph()
            sage: G.center()
            [1, 2]
            sage: P = graphs.PetersenGraph()
            sage: P.subgraph(P.center()) == P
            True
            sage: S = graphs.StarGraph(19)
            sage: S.center()
            [0]

        TESTS::

            sage: G = Graph()
            sage: G.center()
            []
            sage: G.add_vertex()
            0
            sage: G.center()
            [0]
        """
    def periphery(self, by_weight: bool = False, algorithm=None, weight_function=None, check_weight: bool = True):
        """
        Return the set of vertices in the periphery of the graph.

        The periphery is the set of vertices whose eccentricity is equal to the
        diameter of the graph, i.e., achieving the maximum eccentricity.

        For more information and examples on how to use input variables,
        see :meth:`~GenericGraph.shortest_paths` and
        :meth:`~Graph.eccentricity`

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

            sage: G = graphs.DiamondGraph()
            sage: G.periphery()
            [0, 3]
            sage: P = graphs.PetersenGraph()
            sage: P.subgraph(P.periphery()) == P
            True
            sage: S = graphs.StarGraph(19)
            sage: S.periphery()
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
            sage: G = Graph()
            sage: G.periphery()
            []
            sage: G.add_vertex()
            0
            sage: G.periphery()
            [0]
        """
    def distance_graph(self, dist):
        """
        Return the graph on the same vertex set as the original graph but
        vertices are adjacent in the returned graph if and only if they are at
        specified distances in the original graph.

        INPUT:

        - ``dist`` -- nonnegative integer or a list of nonnegative integers;
          specified distance(s) for the connecting vertices. ``Infinity`` may
          be used here to describe vertex pairs in separate components.

        OUTPUT:

        The returned value is an undirected graph.  The vertex set is identical
        to the calling graph, but edges of the returned graph join vertices
        whose distance in the calling graph are present in the input ``dist``.
        Loops will only be present if distance 0 is included. If the original
        graph has a position dictionary specifying locations of vertices for
        plotting, then this information is copied over to the distance graph.
        In some instances this layout may not be the best, and might even be
        confusing when edges run on top of each other due to symmetries chosen
        for the layout.

        EXAMPLES::

            sage: G = graphs.CompleteGraph(3)
            sage: H = G.cartesian_product(graphs.CompleteGraph(2))
            sage: K = H.distance_graph(2)
            sage: K.am()                                                                # needs sage.modules
            [0 0 0 1 0 1]
            [0 0 1 0 1 0]
            [0 1 0 0 0 1]
            [1 0 0 0 1 0]
            [0 1 0 1 0 0]
            [1 0 1 0 0 0]

        To obtain the graph where vertices are adjacent if their distance apart
        is ``d`` or less use a ``range()`` command to create the input, using
        ``d + 1`` as the input to ``range``. Notice that this will include
        distance 0 and hence place a loop at each vertex. To avoid this, use
        ``range(1, d + 1)``::

            sage: G = graphs.OddGraph(4)
            sage: d = G.diameter()
            sage: n = G.num_verts()
            sage: H = G.distance_graph(list(range(d+1)))
            sage: H.is_isomorphic(graphs.CompleteGraph(n))
            False
            sage: H = G.distance_graph(list(range(1,d+1)))
            sage: H.is_isomorphic(graphs.CompleteGraph(n))
            True

        A complete collection of distance graphs will have adjacency matrices
        that sum to the matrix of all ones::

            sage: P = graphs.PathGraph(20)
            sage: all_ones = sum([P.distance_graph(i).am() for i in range(20)])         # needs sage.modules
            sage: all_ones == matrix(ZZ, 20, 20, [1]*400)                               # needs sage.modules
            True

        Four-bit strings differing in one bit is the same as
        four-bit strings differing in three bits::

            sage: G = graphs.CubeGraph(4)
            sage: H = G.distance_graph(3)
            sage: G.is_isomorphic(H)
            True

        The graph of eight-bit strings, adjacent if different in an odd number
        of bits::

            sage: # long time, needs sage.symbolic
            sage: G = graphs.CubeGraph(8)
            sage: H = G.distance_graph([1,3,5,7])
            sage: degrees = [0]*sum([binomial(8,j) for j in [1,3,5,7]])
            sage: degrees.append(2^8)
            sage: degrees == H.degree_histogram()
            True

        An example of using ``Infinity`` as the distance in a graph that is not
        connected::

            sage: G = graphs.CompleteGraph(3)
            sage: H = G.disjoint_union(graphs.CompleteGraph(2))
            sage: L = H.distance_graph(Infinity)
            sage: L.am()                                                                # needs sage.modules
            [0 0 0 1 1]
            [0 0 0 1 1]
            [0 0 0 1 1]
            [1 1 1 0 0]
            [1 1 1 0 0]
            sage: L.is_isomorphic(graphs.CompleteBipartiteGraph(3, 2))
            True

        TESTS:

        Empty input, or unachievable distances silently yield empty graphs::

            sage: G = graphs.CompleteGraph(5)
            sage: G.distance_graph([]).num_edges()
            0
            sage: G = graphs.CompleteGraph(5)
            sage: G.distance_graph(23).num_edges()
            0

        It is an error to provide a distance that is not an integer type::

            sage: G = graphs.CompleteGraph(5)
            sage: G.distance_graph('junk')
            Traceback (most recent call last):
            ...
            TypeError: unable to convert 'junk' to an integer

        It is an error to provide a negative distance::

            sage: G = graphs.CompleteGraph(5)
            sage: G.distance_graph(-3)
            Traceback (most recent call last):
            ...
            ValueError: distance graph for a negative distance (d=-3) is not defined

        AUTHOR:

        Rob Beezer, 2009-11-25, :issue:`7533`
        """
    def to_directed(self, data_structure=None, sparse=None):
        '''
        Return a directed version of the graph.

        A single edge becomes two edges, one in each direction.

        INPUT:

        - ``data_structure`` -- one of ``\'sparse\'``, ``\'static_sparse\'``, or
          ``\'dense\'``. See the documentation of :class:`Graph` or
          :class:`DiGraph`.

        - ``sparse`` -- boolean (default: ``None``); ``sparse=True`` is an
          alias for ``data_structure="sparse"``, and ``sparse=False`` is an
          alias for ``data_structure="dense"``.

        EXAMPLES::

            sage: graphs.PetersenGraph().to_directed()
            Petersen graph: Digraph on 10 vertices

        TESTS:

        Immutable graphs yield immutable graphs::

            sage: Graph([[1, 2]], immutable=True).to_directed()._backend
            <sage.graphs.base.static_sparse_backend.StaticSparseBackend object at ...>

        :issue:`17005`::

            sage: Graph([[1,2]], immutable=True).to_directed()
            Digraph on 2 vertices

        :issue:`22424`::

            sage: G1 = graphs.RandomGNP(5,0.5)
            sage: gp1 = G1.graphplot(save_pos=True)                                     # needs sage.plot
            sage: G2 = G1.to_directed()
            sage: G2.delete_vertex(0)
            sage: G2.add_vertex(5)
            sage: gp2 = G2.graphplot()                                                  # needs sage.plot
            sage: gp1 = G1.graphplot()                                                  # needs sage.plot

        Vertex labels will be retained (:issue:`14708`)::

            sage: G = Graph({0: [1, 2], 1: [0]})
            sage: G.set_vertex(0, \'foo\')
            sage: D = G.to_directed()
            sage: G.get_vertices()
            {0: \'foo\', 1: None, 2: None}
            sage: D.get_vertices()
            {0: \'foo\', 1: None, 2: None}
        '''
    def to_undirected(self):
        """
        Since the graph is already undirected, simply returns a copy of itself.

        EXAMPLES::

            sage: graphs.PetersenGraph().to_undirected()
            Petersen graph: Graph on 10 vertices
        """
    def join(self, other, labels: str = 'pairs', immutable=None):
        '''
        Return the join of ``self`` and ``other``.

        INPUT:

        - ``labels`` -- (defaults to \'pairs\'); if set to \'pairs\', each element
          `v` in the first graph will be named `(0, v)` and each element `u` in
          ``other`` will be named `(1, u)` in the result. If set to \'integers\',
          the elements of the result will be relabeled with consecutive
          integers.

        - ``immutable`` -- boolean (default: ``None``); whether to create a
          mutable/immutable join. ``immutable=None`` (default) means that the
          graphs and their join will behave the same way.

        .. SEEALSO::

            * :meth:`~sage.graphs.generic_graph.GenericGraph.union`

            * :meth:`~sage.graphs.generic_graph.GenericGraph.disjoint_union`

        EXAMPLES::

            sage: G = graphs.CycleGraph(3)
            sage: H = Graph(2)
            sage: J = G.join(H); J
            Cycle graph join : Graph on 5 vertices
            sage: J.vertices(sort=True)
            [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1)]
            sage: J = G.join(H, labels=\'integers\'); J
            Cycle graph join : Graph on 5 vertices
            sage: J.vertices(sort=True)
            [0, 1, 2, 3, 4]
            sage: J.edges(sort=True)
            [(0, 1, None), (0, 2, None), (0, 3, None), (0, 4, None), (1, 2, None), (1, 3, None), (1, 4, None), (2, 3, None), (2, 4, None)]

        ::

            sage: G = Graph(3)
            sage: G.name("Graph on 3 vertices")
            sage: H = Graph(2)
            sage: H.name("Graph on 2 vertices")
            sage: J = G.join(H); J
            Graph on 3 vertices join Graph on 2 vertices: Graph on 5 vertices
            sage: J.vertices(sort=True)
            [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1)]
            sage: J = G.join(H, labels=\'integers\'); J
            Graph on 3 vertices join Graph on 2 vertices: Graph on 5 vertices
            sage: J.edges(sort=True)
            [(0, 3, None), (0, 4, None), (1, 3, None), (1, 4, None), (2, 3, None), (2, 4, None)]
        '''
    def seidel_adjacency_matrix(self, vertices=None, *, base_ring=None, **kwds):
        """
        Return the Seidel adjacency matrix of ``self``.

        Returns `J-I-2A`, for `A` the (ordinary) :meth:`adjacency matrix
        <sage.graphs.generic_graph.GenericGraph.adjacency_matrix>` of ``self``,
        `I` the identity matrix, and `J` the all-1 matrix.  It is closely
        related to :meth:`twograph`.

        By default, the matrix returned is over the integers.

        INPUT:

        - ``vertices`` -- list of vertices (default: ``None``); the ordering of
          the vertices defining how they should appear in the matrix. By
          default, the ordering given by
          :meth:`~sage.graphs.generic_graph.GenericGraph.vertices` is used.

        - ``base_ring`` -- a ring (default: ``None``); the base ring
          of the matrix space to use

        - ``**kwds`` -- other keywords to pass to
          :func:`~sage.matrix.constructor.matrix`

        EXAMPLES::

            sage: G = graphs.CycleGraph(5)
            sage: G = G.disjoint_union(graphs.CompleteGraph(1))
            sage: G.seidel_adjacency_matrix().minpoly()                                 # needs sage.libs.pari sage.modules
            x^2 - 5

        Selecting the base ring::

            sage: G.seidel_adjacency_matrix()[0, 0].parent()                            # needs sage.modules
            Integer Ring
            sage: G.seidel_adjacency_matrix(base_ring=RDF)[0, 0].parent()               # needs sage.modules
            Real Double Field
        """
    def seidel_switching(self, s, inplace: bool = True):
        """
        Return the Seidel switching of ``self`` w.r.t. subset of vertices ``s``.

        Returns the graph obtained by Seidel switching of ``self`` with respect
        to the subset of vertices ``s``. This is the graph given by Seidel
        adjacency matrix `DSD`, for `S` the Seidel adjacency matrix of ``self``,
        and `D` the diagonal matrix with -1s at positions corresponding to
        ``s``, and 1s elsewhere.

        INPUT:

        - ``s`` -- list of vertices of ``self``

        - ``inplace`` -- boolean (default: ``True``); whether to do the
          modification inplace, or to return a copy of the graph after
          switching

        EXAMPLES::

            sage: G = graphs.CycleGraph(5)
            sage: G = G.disjoint_union(graphs.CompleteGraph(1))
            sage: G.seidel_switching([(0,1),(1,0),(0,0)])
            sage: G.seidel_adjacency_matrix().minpoly()                                 # needs sage.libs.pari sage.modules
            x^2 - 5
            sage: G.is_connected()
            True

        TESTS::

            sage: H = G.seidel_switching([1,4,5],inplace=False)
            sage: G.seidel_switching([1,4,5])
            sage: G == H
            True
        """
    def twograph(self):
        """
        Return the two-graph of ``self``.

        Returns the :class:`two-graph <sage.combinat.designs.twographs.TwoGraph>`
        with the triples
        `T=\\{t \\in \\binom {V}{3} : \\left| \\binom {t}{2} \\cap E \\right| \\text{odd} \\}`
        where `V` and `E` are vertices and edges of ``self``, respectively.

        EXAMPLES::

            sage: p = graphs.PetersenGraph()
            sage: p.twograph()                                                          # needs sage.modules
            Incidence structure with 10 points and 60 blocks
            sage: p = graphs.chang_graphs()
            sage: T8 = graphs.CompleteGraph(8).line_graph()
            sage: C = T8.seidel_switching([(0,1,None), (2,3,None), (4,5,None), (6,7,None)],
            ....:                         inplace=False)
            sage: T8.twograph() == C.twograph()                                         # needs sage.modules
            True
            sage: T8.is_isomorphic(C)
            False

        TESTS::

            sage: from sage.combinat.designs.twographs import TwoGraph
            sage: p = graphs.PetersenGraph().twograph()                                 # needs sage.modules
            sage: TwoGraph(p, check=True)                                               # needs sage.modules
            Incidence structure with 10 points and 60 blocks

        .. SEEALSO::

            - :meth:`~sage.combinat.designs.twographs.TwoGraph.descendant` --
              computes the descendant graph of the two-graph of ``self`` at a vertex

            - :func:`~sage.combinat.designs.twographs.twograph_descendant`
              -- ditto, but much faster.
        """
    def write_to_eps(self, filename, **options) -> None:
        """
        Write a plot of the graph to ``filename`` in ``eps`` format.

        INPUT:

        - ``filename`` -- string
        - ``**options`` -- same layout options as :meth:`.layout`

        EXAMPLES::

            sage: P = graphs.PetersenGraph()
            sage: P.write_to_eps(tmp_filename(ext='.eps'))

        It is relatively simple to include this file in a LaTeX document.
        ``\\usepackage{graphics}`` must appear in the preamble, and
        ``\\includegraphics{filename}`` will include the file. To compile the
        document to ``pdf`` with ``pdflatex`` or ``xelatex`` the file needs
        first to be converted to ``pdf``, for example with ``ps2pdf filename.eps
        filename.pdf``.
        """
    def topological_minor(self, H, vertices: bool = False, paths: bool = False, solver=None, verbose: int = 0, *, integrality_tolerance: float = 0.001):
        """
        Return a topological `H`-minor from ``self`` if one exists.

        We say that a graph `G` has a topological `H`-minor (or that it has a
        graph isomorphic to `H` as a topological minor), if `G` contains a
        subdivision of a graph isomorphic to `H` (i.e.  obtained from `H`
        through arbitrary subdivision of its edges) as a subgraph.

        For more information, see the :wikipedia:`Minor_(graph_theory)`.

        INPUT:

        - ``H`` -- the topological minor to find in the current graph

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

        OUTPUT:

        The topological `H`-minor found is returned as a subgraph `M` of
        ``self``, such that the vertex `v` of `M` that represents a vertex `h\\in
        H` has ``h`` as a label (see :meth:`get_vertex
        <sage.graphs.generic_graph.GenericGraph.get_vertex>` and
        :meth:`set_vertex <sage.graphs.generic_graph.GenericGraph.set_vertex>`),
        and such that every edge of `M` has as a label the edge of `H` it
        (partially) represents.

        If no topological minor is found, this method returns ``False``.

        ALGORITHM:

        Mixed Integer Linear Programming.

        COMPLEXITY:

        Theoretically, when `H` is fixed, testing for the existence of a
        topological `H`-minor is polynomial. The known algorithms are highly
        exponential in `H`, though.

        .. NOTE::

            This function can be expected to be *very* slow, especially where
            the topological minor does not exist.

            (CPLEX seems to be *much* more efficient than GLPK on this kind of
            problem)

        EXAMPLES:

        Petersen's graph has a topological `K_4`-minor::

            sage: g = graphs.PetersenGraph()
            sage: g.topological_minor(graphs.CompleteGraph(4))                          # needs sage.numerical.mip
            Subgraph of (Petersen graph): Graph on ...

        And a topological `K_{3,3}`-minor::

            sage: g.topological_minor(graphs.CompleteBipartiteGraph(3,3))               # needs sage.numerical.mip
            Subgraph of (Petersen graph): Graph on ...

        And of course, a tree has no topological `C_3`-minor::

            sage: g = graphs.RandomGNP(15,.3)
            sage: g = g.subgraph(edges=g.min_spanning_tree())
            sage: g.topological_minor(graphs.CycleGraph(3))                             # needs sage.numerical.mip
            False
        """
    def cliques_maximal(self, algorithm: str = 'native'):
        '''
        Return the list of all maximal cliques.

        Each clique is represented by a list of vertices. A clique is an induced
        complete subgraph, and a maximal clique is one not contained in a larger
        one.

        INPUT:

        - ``algorithm`` -- can be set to ``\'native\'`` (default) to use Sage\'s
          own implementation, or to ``"NetworkX"`` to use NetworkX\'
          implementation of the Bron and Kerbosch Algorithm [BK1973]_


        .. NOTE::

            Sage\'s implementation of the enumeration of *maximal* independent
            sets is not much faster than NetworkX\' (expect a 2x speedup), which
            is surprising as it is written in Cython. This being said, the
            algorithm from NetworkX appears to be slightly different from this
            one, and that would be a good thing to explore if one wants to
            improve the implementation.

        ALGORITHM:

        This function is based on NetworkX\'s implementation of the Bron and
        Kerbosch Algorithm [BK1973]_.

        EXAMPLES::

            sage: graphs.ChvatalGraph().cliques_maximal()
            [[0, 1], [0, 4], [0, 6], [0, 9], [1, 2], [1, 5], [1, 7], [2, 3],
             [2, 6], [2, 8], [3, 4], [3, 7], [3, 9], [4, 5], [4, 8], [5, 10],
             [5, 11], [6, 10], [6, 11], [7, 8], [7, 11], [8, 10], [9, 10], [9, 11]]
            sage: G = Graph({0:[1,2,3], 1:[2], 3:[0,1]})
            sage: G.show(figsize=[2, 2])                                                # needs sage.plot
            sage: G.cliques_maximal()
            [[0, 1, 2], [0, 1, 3]]
            sage: C = graphs.PetersenGraph()
            sage: C.cliques_maximal()
            [[0, 1], [0, 4], [0, 5], [1, 2], [1, 6], [2, 3], [2, 7], [3, 4],
             [3, 8], [4, 9], [5, 7], [5, 8], [6, 8], [6, 9], [7, 9]]
            sage: C = Graph(\'DJ{\')
            sage: C.cliques_maximal()
            [[0, 4], [1, 2, 3, 4]]

        Comparing the two implementations::

            sage: g = graphs.RandomGNP(20,.7)
            sage: s1 = Set(map(Set, g.cliques_maximal(algorithm="NetworkX")))           # needs networkx
            sage: s2 = Set(map(Set, g.cliques_maximal(algorithm=\'native\')))
            sage: s1 == s2                                                              # needs networkx
            True
        '''
    def clique_maximum(self, algorithm: str = 'Cliquer', solver=None, verbose: int = 0, *, integrality_tolerance: float = 0.001):
        '''
        Return the vertex set of a maximal order complete subgraph.

        INPUT:

        - ``algorithm`` -- the algorithm to be used :

          - If ``algorithm = "Cliquer"`` (default), wraps the C program
            Cliquer [NO2003]_.

          - If ``algorithm = "MILP"``, the problem is solved through a Mixed
            Integer Linear Program.

            (see :class:`~sage.numerical.mip.MixedIntegerLinearProgram`)

          - If ``algorithm = "mcqd"``, uses the MCQD solver
            (`<http://www.sicmm.org/~konc/maxclique/>`_). Note that the MCQD
            package must be installed.

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

        Parameters ``solver`` and ``verbose`` are used only when
        ``algorithm="MILP"``.

        .. NOTE::

            Currently only implemented for undirected graphs. Use to_undirected
            to convert a digraph to an undirected graph.

        ALGORITHM:

        This function is based on Cliquer [NO2003]_.

        EXAMPLES:

        Using Cliquer (default)::

            sage: C = graphs.PetersenGraph()
            sage: C.clique_maximum()
            [7, 9]
            sage: C = Graph(\'DJ{\')
            sage: C.clique_maximum()
            [1, 2, 3, 4]

        Through a Linear Program::

            sage: len(C.clique_maximum(algorithm=\'MILP\'))
            4

        TESTS:

        Wrong algorithm::

            sage: C.clique_maximum(algorithm=\'BFS\')
            Traceback (most recent call last):
            ...
            NotImplementedError: Only \'MILP\', \'Cliquer\' and \'mcqd\' are supported.
        '''
    def clique_number(self, algorithm: str = 'Cliquer', cliques=None, solver=None, verbose: int = 0, *, integrality_tolerance: float = 0.001):
        '''
        Return the order of the largest clique of the graph.

        This is also called as the clique number.

        .. NOTE::

            Currently only implemented for undirected graphs. Use ``to_undirected``
            to convert a digraph to an undirected graph.

        INPUT:

        - ``algorithm`` -- the algorithm to be used :

          - If ``algorithm = "Cliquer"``, wraps the C program Cliquer
            [NO2003]_.

          - If ``algorithm = "networkx"``, uses the NetworkX\'s implementation of
            the Bron and Kerbosch Algorithm [BK1973]_.

          - If ``algorithm = "MILP"``, the problem is solved through a Mixed
            Integer Linear Program.

            (see :class:`~sage.numerical.mip.MixedIntegerLinearProgram`)

          - If ``algorithm = "mcqd"``, uses the MCQD solver
            (`<http://insilab.org/maxclique/>`_). Note that the MCQD
            package must be installed.

        - ``cliques`` -- an optional list of cliques that can be input if
          already computed. Ignored unless ``algorithm=="networkx"``.

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

        This function is based on Cliquer [NO2003]_ and [BK1973]_.

        EXAMPLES::

            sage: C = Graph(\'DJ{\')
            sage: C.clique_number()
            4
            sage: G = Graph({0:[1,2,3], 1:[2], 3:[0,1]})
            sage: G.show(figsize=[2,2])                                                 # needs sage.plot
            sage: G.clique_number()
            3

        By definition the clique number of a complete graph is its order::

            sage: all(graphs.CompleteGraph(i).clique_number() == i for i in range(1,15))
            True

        A non-empty graph without edges has a clique number of 1::

            sage: all((i*graphs.CompleteGraph(1)).clique_number() == 1
            ....:     for i in range(1,15))
            True

        A complete multipartite graph with k parts has clique number k::

            sage: all((i*graphs.CompleteMultipartiteGraph(i*[5])).clique_number() == i
            ....:     for i in range(1,6))
            True

        TESTS::

            sage: g = graphs.PetersenGraph()
            sage: g.clique_number(algorithm=\'MILP\')                                     # needs sage.numerical.mip
            2
            sage: for i in range(10):           # optional - mcqd                       # needs sage.numerical.mip
            ....:     g = graphs.RandomGNP(15,.5)
            ....:     if g.clique_number() != g.clique_number(algorithm=\'mcqd\'):
            ....:         print("This is dead wrong !")
        '''
    def cliques_number_of(self, vertices=None, cliques=None):
        """
        Return a dictionary of the number of maximal cliques containing each
        vertex, keyed by vertex.

        This returns a single value if only one input vertex.

        .. NOTE::

            Currently only implemented for undirected graphs. Use to_undirected
            to convert a digraph to an undirected graph.

        INPUT:

        - ``vertices`` -- the vertices to inspect (default: entire graph)

        - ``cliques`` -- list of cliques (if already computed)

        EXAMPLES::

            sage: C = Graph('DJ{')
            sage: C.cliques_number_of()
            {0: 1, 1: 1, 2: 1, 3: 1, 4: 2}
            sage: E = C.cliques_maximal(); E
            [[0, 4], [1, 2, 3, 4]]
            sage: C.cliques_number_of(cliques=E)
            {0: 1, 1: 1, 2: 1, 3: 1, 4: 2}
            sage: F = graphs.Grid2dGraph(2,3)
            sage: F.cliques_number_of()
            {(0, 0): 2, (0, 1): 3, (0, 2): 2, (1, 0): 2, (1, 1): 3, (1, 2): 2}
            sage: F.cliques_number_of(vertices=[(0, 1), (1, 2)])
            {(0, 1): 3, (1, 2): 2}
            sage: F.cliques_number_of(vertices=(0, 1))
            3
            sage: G = Graph({0:[1,2,3], 1:[2], 3:[0,1]})
            sage: G.show(figsize=[2,2])                                                 # needs sage.plot
            sage: G.cliques_number_of()
            {0: 2, 1: 2, 2: 1, 3: 1}
        """
    def cliques_get_max_clique_graph(self):
        """
        Return the clique graph.

        Vertices of the result are the maximal cliques of the graph, and edges
        of the result are between maximal cliques with common members in the
        original graph.

        For more information, see the :wikipedia:`Clique_graph`.

        .. NOTE::

            Currently only implemented for undirected graphs. Use to_undirected
            to convert a digraph to an undirected graph.

        EXAMPLES::

            sage: MCG = graphs.ChvatalGraph().cliques_get_max_clique_graph(); MCG
            Graph on 24 vertices
            sage: MCG.show(figsize=[2,2], vertex_size=20, vertex_labels=False)          # needs sage.plot
            sage: G = Graph({0:[1,2,3], 1:[2], 3:[0,1]})
            sage: G.show(figsize=[2,2])                                                 # needs sage.plot
            sage: G.cliques_get_max_clique_graph()
            Graph on 2 vertices
            sage: G.cliques_get_max_clique_graph().show(figsize=[2,2])                  # needs sage.plot

        TESTS::

            sage: # needs networkx
            sage: import networkx
            sage: CG = graphs.ChvatalGraph()
            sage: S = CG.cliques_get_max_clique_graph()
            sage: N = Graph(networkx.make_max_clique_graph(CG.networkx_graph(),
            ....:                                          create_using=networkx.MultiGraph()),
            ....:           multiedges=False)
            sage: S.is_isomorphic(N)
            True
        """
    def cliques_get_clique_bipartite(self, **kwds):
        """
        Return the vertex-clique bipartite graph of ``self``.

        In the returned bipartite graph, the ``left`` vertices are the vertices
        of ``self`` and the ``right`` vertices represent the maximal cliques of
        ``self``.  There is an edge from vertex `v` to clique `C` in the
        bipartite graph if and only if `v` belongs to `C`.

        .. NOTE::

            Currently only implemented for undirected graphs. Use to_undirected
            to convert a digraph to an undirected graph.

        EXAMPLES::

            sage: CBG = graphs.ChvatalGraph().cliques_get_clique_bipartite(); CBG
            Bipartite graph on 36 vertices
            sage: CBG.show(figsize=[2,2], vertex_size=20, vertex_labels=False)          # needs sage.plot
            sage: G = Graph({0:[1,2,3], 1:[2], 3:[0,1]})
            sage: G.show(figsize=[2,2])                                                 # needs sage.plot
            sage: G.cliques_get_clique_bipartite()
            Bipartite graph on 6 vertices
            sage: G.cliques_get_clique_bipartite().show(figsize=[2,2])                  # needs sage.plot

        TESTS::

            sage: # needs networkx
            sage: import networkx
            sage: CG = graphs.ChvatalGraph()
            sage: S = CG.cliques_get_clique_bipartite()
            sage: N = BipartiteGraph(networkx.make_clique_bipartite(CG.networkx_graph()))
            sage: S.is_isomorphic(N)
            True
        """
    def independent_set(self, algorithm: str = 'Cliquer', value_only: bool = False, reduction_rules: bool = True, solver=None, verbose: int = 0, *, integrality_tolerance: float = 0.001):
        '''
        Return a maximum independent set.

        An independent set of a graph is a set of pairwise non-adjacent
        vertices. A maximum independent set is an independent set of maximum
        cardinality.  It induces an empty subgraph.

        Equivalently, an independent set is defined as the complement of a
        vertex cover.

        For more information, see the
        :wikipedia:`Independent_set_(graph_theory)` and the
        :wikipedia:`Vertex_cover`.

        INPUT:

        - ``algorithm`` -- the algorithm to be used

          * If ``algorithm = "Cliquer"`` (default), the problem is solved
            using Cliquer [NO2003]_.

            (see the :mod:`Cliquer modules <sage.graphs.cliquer>`)

          * If ``algorithm = "MILP"``, the problem is solved through a Mixed
            Integer Linear Program.

            (see :class:`~sage.numerical.mip.MixedIntegerLinearProgram`)

         * If ``algorithm = "mcqd"``, uses the MCQD solver
           (`<http://www.sicmm.org/~konc/maxclique/>`_). Note that the MCQD
           package must be installed.

        - ``value_only`` -- boolean (default: ``False``); if set to ``True``,
          only the size of a maximum independent set is returned. Otherwise,
          a maximum independent set is returned as a list of vertices.

        - ``reduction_rules`` -- (default: ``True``) specify if the reductions
          rules from kernelization must be applied as pre-processing or not.
          See [ACFLSS04]_ for more details. Note that depending on the instance,
          it might be faster to disable reduction rules.

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

        .. NOTE::

            While Cliquer/MCAD are usually (and by far) the most efficient
            implementations, the MILP formulation sometimes proves faster on
            very "symmetrical" graphs.

        EXAMPLES:

        Using Cliquer::

            sage: C = graphs.PetersenGraph()
            sage: C.independent_set()
            [0, 3, 6, 7]

        As a linear program::

            sage: C = graphs.PetersenGraph()
            sage: len(C.independent_set(algorithm=\'MILP\'))                              # needs sage.numerical.mip
            4

        .. PLOT::

            g = graphs.PetersenGraph()
            sphinx_plot(g.plot(partition=[g.independent_set()]))
        '''
    def vertex_cover(self, algorithm: str = 'Cliquer', value_only: bool = False, reduction_rules: bool = True, solver=None, verbose: int = 0, *, integrality_tolerance: float = 0.001):
        '''
        Return a minimum vertex cover of ``self`` represented by a set of vertices.

        A minimum vertex cover of a graph is a set `S` of vertices such that
        each edge is incident to at least one element of `S`, and such that `S`
        is of minimum cardinality. For more information, see the
        :wikipedia:`Vertex_cover`.

        Equivalently, a vertex cover is defined as the complement of an
        independent set.

        As an optimization problem, it can be expressed as follows:

        .. MATH::

            \\mbox{Minimize : }&\\sum_{v\\in G} b_v\\\\\n            \\mbox{Such that : }&\\forall (u,v) \\in G.edges(), b_u+b_v\\geq 1\\\\\n            &\\forall x\\in G, b_x\\mbox{ is a binary variable}

        INPUT:

        - ``algorithm`` -- string (default: ``\'Cliquer\'``); indicating which
          algorithm to use. It can be one of those values.

          - ``\'Cliquer\'`` will compute a minimum vertex cover using the Cliquer
            package

          - ``\'MILP\'`` will compute a minimum vertex cover through a mixed
            integer linear program

          - ``\'mcqd\'`` will use the MCQD solver
            (`<http://www.sicmm.org/~konc/maxclique/>`_). Note that the MCQD
            package must be installed.

        - ``value_only`` -- boolean (default: ``False``); if set to ``True``,
          only the size of a minimum vertex cover is returned. Otherwise,
          a minimum vertex cover is returned as a list of vertices.

        - ``reduction_rules`` -- (default: ``True``) specify if the reductions
          rules from kernelization must be applied as pre-processing or not.
          See [ACFLSS04]_ for more details. Note that depending on the instance,
          it might be faster to disable reduction rules.

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

        On the Pappus graph::

           sage: g = graphs.PappusGraph()
           sage: g.vertex_cover(value_only=True)
           9

        .. PLOT::

            g = graphs.PappusGraph()
            sphinx_plot(g.plot(partition=[g.vertex_cover()]))

        TESTS:

        The two algorithms should return the same result::

           sage: g = graphs.RandomGNP(10, .5)
           sage: vc1 = g.vertex_cover(algorithm=\'MILP\')                                 # needs sage.numerical.mip
           sage: vc2 = g.vertex_cover(algorithm=\'Cliquer\')
           sage: len(vc1) == len(vc2)                                                   # needs sage.numerical.mip
           True

        The cardinality of the vertex cover is unchanged when reduction rules
        are used. First for trees::

           sage: for i in range(20):
           ....:     g = graphs.RandomTree(20)
           ....:     vc1_set = g.vertex_cover()
           ....:     vc1 = len(vc1_set)
           ....:     vc2 = g.vertex_cover(value_only=True, reduction_rules=False)
           ....:     if vc1 != vc2:
           ....:         print("Error :", vc1, vc2)
           ....:         print("With reduction rules :", vc1)
           ....:         print("Without reduction rules :", vc2)
           ....:         break
           ....:     g.delete_vertices(vc1_set)
           ....:     if g.size():
           ....:         print("This thing is not a vertex cover !")

        Then for random GNP graphs::

           sage: for i in range(20):
           ....:     g = graphs.RandomGNP(50, 0.08)
           ....:     vc1_set = g.vertex_cover()
           ....:     vc1 = len(vc1_set)
           ....:     vc2 = g.vertex_cover(value_only=True, reduction_rules=False)
           ....:     if vc1 != vc2:
           ....:         print("Error :", vc1, vc2)
           ....:         print("With reduction rules :", vc1)
           ....:         print("Without reduction rules :", vc2)
           ....:         break
           ....:     g.delete_vertices(vc1_set)
           ....:     if g.size():
           ....:         print("This thing is not a vertex cover !")

        Testing mcqd::

            sage: graphs.PetersenGraph().vertex_cover(algorithm=\'mcqd\', value_only=True)  # optional - mcqd
            6

        Given a wrong algorithm::

            sage: graphs.PetersenGraph().vertex_cover(algorithm=\'guess\')
            Traceback (most recent call last):
            ...
            ValueError: the algorithm must be "Cliquer", "MILP" or "mcqd"

        Issue :issue:`24287` is fixed::

            sage: G = Graph([(0,1)]*5 + [(1,2)]*2, multiedges=True)
            sage: G.vertex_cover(reduction_rules=True, algorithm=\'MILP\')                # needs sage.numerical.mip
            [1]
            sage: G.vertex_cover(reduction_rules=False)                                 # needs sage.numerical.mip
            [1]

        Issue :issue:`25988` is fixed::

            sage: B = BipartiteGraph(graphs.CycleGraph(6))
            sage: B.vertex_cover(algorithm=\'Cliquer\', reduction_rules=True)
            [1, 3, 5]
        '''
    def ear_decomposition(self):
        """
        Return an Ear decomposition of the graph.

        An ear of an undirected graph `G` is a path `P` where the two endpoints
        of the path may coincide (i.e., form a cycle), but where otherwise no
        repetition of edges or vertices is allowed, so every internal vertex of
        `P` has degree two in `P`.

        An ear decomposition of an undirected graph `G` is a partition of its
        set of edges into a sequence of ears, such that the one or two endpoints
        of each ear belong to earlier ears in the sequence and such that the
        internal vertices of each ear do not belong to any earlier ear.

        For more information, see the :wikipedia:`Ear_decomposition`.

        This method implements the linear time algorithm presented in
        [Sch2013]_.

        OUTPUT:

        - A nested list representing the cycles and chains of the ear
          decomposition of the graph.

        EXAMPLES:

        Ear decomposition of an outer planar graph of order 13::

            sage: g = Graph('LlCG{O@?GBOMW?')
            sage: g.ear_decomposition()
            [[0, 3, 2, 1, 0],
             [0, 7, 4, 3],
             [0, 11, 9, 8, 7],
             [1, 12, 2],
             [3, 6, 5, 4],
             [4, 6],
             [7, 10, 8],
             [7, 11],
             [8, 11]]

        Ear decomposition of a biconnected graph::

            sage: g = graphs.CycleGraph(4)
            sage: g.ear_decomposition()
            [[0, 3, 2, 1, 0]]

        Ear decomposition of a connected but not biconnected graph::

            sage: G = Graph()
            sage: G.add_cycle([0,1,2])
            sage: G.add_edge(0,3)
            sage: G.add_cycle([3,4,5,6])
            sage: G.ear_decomposition()
            [[0, 2, 1, 0], [3, 6, 5, 4, 3]]

        The ear decomposition of a multigraph with loops is the same as the ear
        decomposition of the underlying simple graph::

            sage: g = graphs.BullGraph()
            sage: g.allow_multiple_edges(True)
            sage: g.add_edges(g.edges(sort=False))
            sage: g.allow_loops(True)
            sage: u = g.random_vertex()
            sage: g.add_edge(u, u)
            sage: g
            Bull graph: Looped multi-graph on 5 vertices
            sage: h = g.to_simple()
            sage: g.ear_decomposition() == h.ear_decomposition()
            True

        TESTS::

            sage: g=Graph()
            sage: g
            Graph on 0 vertices
            sage: g.ear_decomposition()
            Traceback (most recent call last):
            ...
            ValueError: ear decomposition is defined for graphs of order at least 3
        """
    def cliques_vertex_clique_number(self, algorithm: str = 'cliquer', vertices=None, cliques=None):
        """
        Return a dictionary of sizes of the largest maximal cliques containing
        each vertex, keyed by vertex.

        Returns a single value if only one input vertex.

        .. NOTE::

            Currently only implemented for undirected graphs. Use :meth:`to_undirected`
            to convert a digraph to an undirected graph.

        INPUT:

        - ``algorithm`` -- either ``cliquer`` or ``networkx``

           - ``cliquer`` -- this wraps the C program Cliquer [NO2003]_

           - ``networkx`` -- this function is based on NetworkX's implementation
             of the Bron and Kerbosch Algorithm [BK1973]_

        - ``vertices`` -- the vertices to inspect (default: entire graph).
          Ignored unless ``algorithm=='networkx'``.

        - ``cliques`` -- list of cliques (if already computed).  Ignored unless
          ``algorithm=='networkx'``.

        EXAMPLES::

            sage: C = Graph('DJ{')
            sage: C.cliques_vertex_clique_number()                                      # needs sage.plot
            {0: 2, 1: 4, 2: 4, 3: 4, 4: 4}
            sage: E = C.cliques_maximal(); E
            [[0, 4], [1, 2, 3, 4]]
            sage: C.cliques_vertex_clique_number(cliques=E, algorithm='networkx')       # needs networkx
            {0: 2, 1: 4, 2: 4, 3: 4, 4: 4}

            sage: F = graphs.Grid2dGraph(2,3)
            sage: F.cliques_vertex_clique_number(algorithm='networkx')                  # needs networkx
            {(0, 0): 2, (0, 1): 2, (0, 2): 2, (1, 0): 2, (1, 1): 2, (1, 2): 2}
            sage: F.cliques_vertex_clique_number(vertices=[(0, 1), (1, 2)])             # needs sage.plot
            {(0, 1): 2, (1, 2): 2}

            sage: G = Graph({0:[1,2,3], 1:[2], 3:[0,1]})
            sage: G.show(figsize=[2,2])                                                 # needs sage.plot
            sage: G.cliques_vertex_clique_number()                                      # needs sage.plot
            {0: 3, 1: 3, 2: 3, 3: 3}
        """
    def cliques_containing_vertex(self, vertices=None, cliques=None):
        """
        Return the cliques containing each vertex, represented as a dictionary
        of lists of lists, keyed by vertex.

        Returns a single list if only one input vertex.

        .. NOTE::

            Currently only implemented for undirected graphs. Use to_undirected
            to convert a digraph to an undirected graph.

        INPUT:

        - ``vertices`` -- the vertices to inspect (default: entire graph)

        - ``cliques`` -- list of cliques (if already computed)

        EXAMPLES::

            sage: # needs networkx
            sage: C = Graph('DJ{')
            sage: C.cliques_containing_vertex()
            {0: [[0, 4]],
             1: [[1, 2, 3, 4]],
             2: [[1, 2, 3, 4]],
             3: [[1, 2, 3, 4]],
             4: [[0, 4], [1, 2, 3, 4]]}
            sage: C.cliques_containing_vertex(4)
            [[0, 4], [1, 2, 3, 4]]
            sage: C.cliques_containing_vertex([0, 1])
            {0: [[0, 4]], 1: [[1, 2, 3, 4]]}
            sage: E = C.cliques_maximal(); E
            [[0, 4], [1, 2, 3, 4]]
            sage: C.cliques_containing_vertex(cliques=E)
            {0: [[0, 4]],
             1: [[1, 2, 3, 4]],
             2: [[1, 2, 3, 4]],
             3: [[1, 2, 3, 4]],
             4: [[0, 4], [1, 2, 3, 4]]}

            sage: G = Graph({0:[1,2,3], 1:[2], 3:[0,1]})
            sage: G.show(figsize=[2,2])                                                 # needs sage.plot
            sage: G.cliques_containing_vertex()                                         # needs networkx
            {0: [[0, 1, 2], [0, 1, 3]],
             1: [[0, 1, 2], [0, 1, 3]],
             2: [[0, 1, 2]],
             3: [[0, 1, 3]]}

        Since each clique of a 2 dimensional grid corresponds to an edge, the
        number of cliques in which a vertex is involved equals its degree::

            sage: # needs networkx
            sage: F = graphs.Grid2dGraph(2,3)
            sage: d = F.cliques_containing_vertex()
            sage: all(F.degree(u) == len(cliques) for u,cliques in d.items())
            True
            sage: d = F.cliques_containing_vertex(vertices=[(0, 1)])
            sage: list(d)
            [(0, 1)]
            sage: sorted(sorted(x for x in L) for L in d[(0, 1)])
            [[(0, 0), (0, 1)], [(0, 1), (0, 2)], [(0, 1), (1, 1)]]
        """
    def clique_complex(self):
        """
        Return the clique complex of ``self``.

        This is the largest simplicial complex on the vertices of ``self`` whose
        1-skeleton is ``self``.

        This is only makes sense for undirected simple graphs.

        EXAMPLES::

            sage: g = Graph({0:[1,2],1:[2],4:[]})
            sage: g.clique_complex()
            Simplicial complex with vertex set (0, 1, 2, 4) and facets {(4,), (0, 1, 2)}

            sage: h = Graph({0:[1,2,3,4],1:[2,3,4],2:[3]})
            sage: x = h.clique_complex()
            sage: x
            Simplicial complex with vertex set (0, 1, 2, 3, 4) and facets {(0, 1, 4), (0, 1, 2, 3)}
            sage: i = x.graph()
            sage: i==h
            True
            sage: x==i.clique_complex()
            True
        """
    def clique_polynomial(self, t=None):
        """
        Return the clique polynomial of ``self``.

        This is the polynomial where the coefficient of `t^n` is the number of
        cliques in the graph with `n` vertices. The constant term of the clique
        polynomial is always taken to be one.

        EXAMPLES::

            sage: g = Graph()
            sage: g.clique_polynomial()
            1
            sage: g = Graph({0:[1]})
            sage: g.clique_polynomial()
            t^2 + 2*t + 1
            sage: g = graphs.CycleGraph(4)
            sage: g.clique_polynomial()
            4*t^2 + 4*t + 1
        """
    def cores(self, k=None, with_labels: bool = False):
        """
        Return the core number for each vertex in an ordered list.

        (for homomorphisms cores, see the :meth:`Graph.has_homomorphism_to`
        method)

        DEFINITIONS:

        * *K-cores* in graph theory were introduced by Seidman in 1983 and by
          Bollobas in 1984 as a method of (destructively) simplifying graph
          topology to aid in analysis and visualization. They have been more
          recently defined as the following by Batagelj et al:

          *Given a graph `G` with vertices set `V` and edges set `E`, the
          `k`-core of `G` is the graph obtained from `G` by recursively removing
          the vertices with degree less than `k`, for as long as there are any.*

          This operation can be useful to filter or to study some properties of
          the graphs. For instance, when you compute the 2-core of graph G, you
          are cutting all the vertices which are in a tree part of graph.  (A
          tree is a graph with no loops). See the :wikipedia:`K-core`.

          [PSW1996]_ defines a `k`-core of `G` as the largest subgraph (it is
          unique) of `G` with minimum degree at least `k`.

        * Core number of a vertex

          The core number of a vertex `v` is the largest integer `k` such that
          `v` belongs to the `k`-core of `G`.

        * Degeneracy

          The *degeneracy* of a graph `G`, usually denoted `\\delta^*(G)`, is the
          smallest integer `k` such that the graph `G` can be reduced to the
          empty graph by iteratively removing vertices of degree `\\leq k`.
          Equivalently, `\\delta^*(G) = k - 1` if `k` is the smallest integer
          such that the `k`-core of `G` is empty.

        IMPLEMENTATION:

        This implementation is based on the NetworkX implementation of the
        algorithm described in [BZ2003]_.

        INPUT:

        - ``k`` -- integer (default: ``None``)

            * If ``k = None`` (default), returns the core number for each vertex.

            * If ``k`` is an integer, returns a pair ``(ordering, core)``, where
              ``core`` is the list of vertices in the `k`-core of ``self``, and
              ``ordering`` is an elimination order for the other vertices such
              that each vertex is of degree strictly less than `k` when it is to
              be eliminated from the graph.

        - ``with_labels`` -- boolean (default: ``False``); when set to
          ``False``, and ``k = None``, the method returns a list whose `i` th
          element is the core number of the `i` th vertex. When set to ``True``,
          the method returns a dictionary whose keys are vertices, and whose
          values are the corresponding core numbers.

        .. SEEALSO::

            * Graph cores is also a notion related to graph homomorphisms. For
              this second meaning, see :meth:`Graph.has_homomorphism_to`.
            * :wikipedia:`Degeneracy_(graph_theory)`

        EXAMPLES::

            sage: (graphs.FruchtGraph()).cores()
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
            sage: (graphs.FruchtGraph()).cores(with_labels=True)
            {0: 3, 1: 3, 2: 3, 3: 3, 4: 3, 5: 3, 6: 3, 7: 3, 8: 3, 9: 3, 10: 3, 11: 3}

            sage: # needs sage.modules
            sage: set_random_seed(0)
            sage: a = random_matrix(ZZ, 20, x=2, sparse=True, density=.1)
            sage: b = Graph(20)
            sage: b.add_edges(a.nonzero_positions(), loops=False)
            sage: cores = b.cores(with_labels=True); cores
            {0: 3, 1: 3, 2: 3, 3: 3, 4: 2, 5: 2, 6: 3, 7: 1, 8: 3, 9: 3, 10: 3,
             11: 3, 12: 3, 13: 3, 14: 2, 15: 3, 16: 3, 17: 3, 18: 3, 19: 3}
            sage: [v for v,c in cores.items() if c >= 2]  # the vertices in the 2-core
            [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

        Checking the 2-core of a random lobster is indeed the empty set::

            sage: g = graphs.RandomLobster(20, .5, .5)                                  # needs networkx
            sage: ordering, core = g.cores(2)                                           # needs networkx
            sage: len(core) == 0                                                        # needs networkx
            True

        Checking the cores of a bull graph::

            sage: G = graphs.BullGraph()
            sage: G.cores(with_labels=True)
            {0: 2, 1: 2, 2: 2, 3: 1, 4: 1}
            sage: G.cores(k=2)
            ([3, 4], [0, 1, 2])

        Graphs with multiple edges::

            sage: G.allow_multiple_edges(True)
            sage: G.add_edges(G.edges(sort=False))
            sage: G.cores(with_labels=True)
            {0: 4, 1: 4, 2: 4, 3: 2, 4: 2}
            sage: G.cores(k=4)
            ([3, 4], [0, 1, 2])
        """
    def is_module(self, vertices):
        """
        Check whether ``vertices`` is a module of ``self``.

        A subset `M` of the vertices of a graph is a module if for every
        vertex `v` outside of `M`, either all vertices of `M` are neighbors of
        `v` or all vertices of `M` are not neighbors of `v`.

        INPUT:

        - ``vertices`` -- iterable; a subset of vertices of ``self``

        EXAMPLES:

        The whole graph, the empty set and singletons are trivial modules::

            sage: G = graphs.PetersenGraph()
            sage: G.is_module([])
            True
            sage: G.is_module([G.random_vertex()])
            True
            sage: G.is_module(G)
            True

        Prime graphs only have trivial modules::

            sage: G = graphs.PathGraph(5)
            sage: G.is_prime()
            True
            sage: all(not G.is_module(S) for S in subsets(G)
            ....:                       if len(S) > 1 and len(S) < G.order())
            True

        For edgeless graphs and complete graphs, all subsets are modules::

            sage: G = Graph(5)
            sage: all(G.is_module(S) for S in subsets(G))
            True
            sage: G = graphs.CompleteGraph(5)
            sage: all(G.is_module(S) for S in subsets(G))
            True

        The modules of a graph and of its complements are the same::

            sage: G = graphs.TuranGraph(10, 3)
            sage: G.is_module([0,1,2])
            True
            sage: G.complement().is_module([0,1,2])
            True
            sage: G.is_module([3,4,5])
            True
            sage: G.complement().is_module([3,4,5])
            True
            sage: G.is_module([2,3,4])
            False
            sage: G.complement().is_module([2,3,4])
            False
            sage: G.is_module([3,4,5,6,7,8,9])
            True
            sage: G.complement().is_module([3,4,5,6,7,8,9])
            True

        Elements of ``vertices`` must be in ``self``::

            sage: G = graphs.PetersenGraph()
            sage: G.is_module(['Terry'])
            Traceback (most recent call last):
            ...
            LookupError: vertex (Terry) is not a vertex of the graph
            sage: G.is_module([1, 'Graham'])
            Traceback (most recent call last):
            ...
            LookupError: vertex (Graham) is not a vertex of the graph
        """
    def modular_decomposition(self, algorithm=None, style: str = 'tuple'):
        '''
        Return the modular decomposition of the current graph.

        A module of an undirected graph is a subset of vertices such that every
        vertex outside the module is either connected to all members of the
        module or to none of them. Every graph that has a nontrivial module can
        be partitioned into modules, and the increasingly fine partitions into
        modules form a tree. The ``modular_decomposition`` method returns
        that tree.

        INPUT:

        - ``algorithm`` -- string (default: ``None``); the algorithm to use
          among:

          - ``None`` or ``\'corneil_habib_paul_tedder\'`` -- will use the
            Corneil-Habib-Paul-Tedder algorithm from [TCHP2008]_, its complexity
            is linear in the number of vertices and edges.

          - ``\'habib_maurer\'`` -- will use the Habib-Maurer algorithm from
            [HM1979]_, its complexity is cubic in the number of vertices.

        - ``style`` -- string (default: ``\'tuple\'``); specifies the output
          format:

          - ``\'tuple\'`` -- as nested tuples

          - ``\'tree\'`` -- as :class:`~sage.combinat.rooted_tree.LabelledRootedTree`

        OUTPUT:

        The modular decomposition tree, either as nested tuples (if
        ``style=\'tuple\'``) or as an object of
        :class:`~sage.combinat.rooted_tree.LabelledRootedTree` (if
        ``style=\'tree\'``)

        Crash course on modular decomposition:

        A module `M` of a graph `G` is a proper subset of its vertices such
        that for all `u \\in V(G)-M, v,w\\in M` the relation `u \\sim v
        \\Leftrightarrow u \\sim w` holds, where `\\sim` denotes the adjacency
        relation in `G`. Equivalently, `M \\subset V(G)` is a module if all its
        vertices have the same adjacency relations with each vertex outside of
        the module (vertex by vertex).

        Hence, for a set like a module, it is very easy to encode the
        information of the adjacencies between the vertices inside and outside
        the module -- we can actually add a new vertex `v_M` to our graph
        representing our module `M`, and let `v_M` be adjacent to `u\\in V(G)-M`
        if and only if some `v\\in M` (and hence all the vertices contained in
        the module) is adjacent to `u`. We can now independently (and
        recursively) study the structure of our module `M` and the new graph
        `G-M+\\{v_M\\}`, without any loss of information.

        Here are two very simple modules :

        * A connected component `C` (or the union of some --but not all-- of
          them) of a disconnected graph `G`, for instance, is a module, as no
          vertex of `C` has a neighbor outside of it.

        * An anticomponent `C` (or the union of some --but not all-- of them) of
          a non-anticonnected graph `G`, for the same reason (it is just the
          complement of the previous graph !).

        These modules being of special interest, the disjoint union of graphs is
        called a Parallel composition, and the complement of a disjoint union is
        called a Series composition. A graph whose only modules are singletons
        is called Prime.

        For more information on modular decomposition, in particular for an
        explanation of the terms "Parallel," "Prime" and "Series," see the
        :wikipedia:`Modular_decomposition`.

        You may also be interested in the survey from Michel Habib and
        Christophe Paul entitled "A survey on Algorithmic aspects of modular
        decomposition" [HP2010]_.

        EXAMPLES:

        The Bull Graph is prime::

            sage: graphs.BullGraph().modular_decomposition()
            (PRIME, [1, 2, 0, 3, 4])

        The Petersen Graph too::

            sage: graphs.PetersenGraph().modular_decomposition()
            (PRIME, [1, 4, 5, 0, 6, 2, 3, 9, 7, 8])

        Graph from the :wikipedia:`Modular_decomposition`::

            sage: G = Graph(\'Jv\\\\zoKF@wN?\', format=\'graph6\')
            sage: G.relabel([1..11])
            sage: G.modular_decomposition()
            (PRIME,
             [(SERIES, [4, (PARALLEL, [2, 3])]),
              1,
              5,
              (PARALLEL, [6, 7]),
              (SERIES, [(PARALLEL, [10, 11]), 9, 8])])

        This a clique on 5 vertices with 2 pendant edges, though, has a more
        interesting decomposition::

            sage: g = graphs.CompleteGraph(5)
            sage: g.add_edge(0,5)
            sage: g.add_edge(0,6)
            sage: g.modular_decomposition()
            (SERIES, [(PARALLEL, [(SERIES, [3, 4, 2, 1]), 5, 6]), 0])

        Turán graphs are co-graphs::

            sage: graphs.TuranGraph(11, 3).modular_decomposition()
            (SERIES,
             [(PARALLEL, [7, 8, 9, 10]), (PARALLEL, [3, 4, 5, 6]), (PARALLEL, [0, 1, 2])])

        We can choose output to be a
        :class:`~sage.combinat.rooted_tree.LabelledRootedTree`::

            sage: g.modular_decomposition(style=\'tree\')
            SERIES[0[], PARALLEL[5[], 6[], SERIES[1[], 2[], 3[], 4[]]]]
            sage: ascii_art(g.modular_decomposition(algorithm="habib_maurer",style=\'tree\'))
              __SERIES
             /      /
            0   ___PARALLEL
               / /     /
              5 6   __SERIES
                   / / / /
                  1 2 3 4

        ALGORITHM:

        This function can use either the algorithm of D. Corneil, M. Habib, C.
        Paul and M. Tedder [TCHP2008]_ or the algorithm of M. Habib and M.
        Maurer [HM1979]_.

        .. SEEALSO::

            - :meth:`is_prime` -- tests whether a graph is prime

            - :class:`~sage.combinat.rooted_tree.LabelledRootedTree`.

            - :func:`~sage.graphs.graph_decompositions.modular_decomposition.corneil_habib_paul_tedder_algorithm`

            - :func:`~sage.graphs.graph_decompositions.modular_decomposition.habib_maurer_algorithm`

        .. NOTE::

            A buggy implementation of the linear time algorithm from [TCHP2008]_
            was removed in Sage 9.7, see :issue:`25872`. A new implementation
            was reintroduced in Sage 10.6 after some corrections to the original
            algorithm, see :issue:`39038`.

        TESTS:

        Empty graph::

            sage: graphs.EmptyGraph().modular_decomposition()
            ()
            sage: graphs.EmptyGraph().modular_decomposition(style=\'tree\')
            None[]

        Singleton Vertex::

            sage: Graph(1).modular_decomposition()
            0
            sage: Graph(1).modular_decomposition(style=\'tree\')
            0[]

        Vertices may be arbitrary --- check that :issue:`24898` is fixed::

            sage: md = Graph({(1,2):[(2,3)],(2,3):[(1,2)]}).modular_decomposition()
            sage: md[0]
            SERIES
            sage: sorted(md[1])
            [(1, 2), (2, 3)]

        Unknown style::

            sage: graphs.PathGraph(2).modular_decomposition(style=\'xyz\')
            Traceback (most recent call last):
            ...
            ValueError: style must be \'tuple\' or \'tree\'

        Check that :issue:`25872` is fixed::

            sage: G1 = Graph(\'FwA]w\')
            sage: G2 = Graph(\'F@Nfg\')
            sage: G1.is_isomorphic(G2)
            True
            sage: G1.modular_decomposition(algorithm="habib_maurer")
            (PRIME, [1, 2, 5, 6, 0, (PARALLEL, [3, 4])])
            sage: G2.modular_decomposition(algorithm="habib_maurer")
            (PRIME, [5, 6, 3, 4, 2, (PARALLEL, [0, 1])])
            sage: G1.modular_decomposition(algorithm="corneil_habib_paul_tedder")
            (PRIME, [6, 5, 1, 2, 0, (PARALLEL, [3, 4])])
            sage: G2.modular_decomposition(algorithm="corneil_habib_paul_tedder")
            (PRIME, [6, 5, (PARALLEL, [0, 1]), 2, 3, 4])

        Check that :issue:`37631` is fixed::

            sage: G = Graph(\'GxJEE?\')
            sage: G.modular_decomposition(algorithm="habib_maurer",style=\'tree\')
            PRIME[2[], SERIES[0[], 1[]], PARALLEL[3[], 4[]],
                  PARALLEL[5[], 6[], 7[]]]
        '''
    def is_polyhedral(self) -> bool:
        """
        Check whether the graph is the graph of the polyhedron.

        By a theorem of Steinitz (Satz 43, p. 77 of [St1922]_), graphs of
        three-dimensional polyhedra are exactly the simple 3-vertex-connected
        planar graphs.

        EXAMPLES::

            sage: C = graphs.CubeGraph(3)
            sage: C.is_polyhedral()
            True
            sage: K33=graphs.CompleteBipartiteGraph(3, 3)
            sage: K33.is_polyhedral()
            False
            sage: graphs.CycleGraph(17).is_polyhedral()
            False
            sage: [i for i in range(9) if graphs.CompleteGraph(i).is_polyhedral()]
            [4]

        .. SEEALSO::

            * :meth:`~sage.graphs.generic_graph.GenericGraph.vertex_connectivity`
            * :meth:`~sage.graphs.generic_graph.GenericGraph.is_planar`
            * :meth:`is_circumscribable`
            * :meth:`is_inscribable`
            * :wikipedia:`Polyhedral_graph`

        TESTS::

            sage: G = Graph([[1, 2, 3, 4], [[1, 2], [1,1]]], loops=True)
            sage: G.is_polyhedral()
            False

            sage: G = Graph([[1, 2, 3], [[1, 2], [3, 1], [1, 2], [2, 3]]], multiedges=True)
            sage: G.is_polyhedral()
            False
        """
    def is_circumscribable(self, solver: str = 'ppl', verbose: int = 0):
        """
        Test whether the graph is the graph of a circumscribed polyhedron.

        A polyhedron is circumscribed if all of its facets are tangent to a
        sphere. By a theorem of Rivin ([HRS1993]_), this can be checked by
        solving a linear program that assigns weights between 0 and 1/2 on each
        edge of the polyhedron, so that the weights on any face add to exactly
        one and the weights on any non-facial cycle add to more than one.  If
        and only if this can be done, the polyhedron can be circumscribed.

        INPUT:

        - ``solver`` -- (default: ``'ppl'``) specify a Linear Program (LP)
          solver to be used. If set to ``None``, the default one is used. For
          more information on LP solvers and which default solver is used, see
          the method :meth:`solve
          <sage.numerical.mip.MixedIntegerLinearProgram.solve>` of the class
          :class:`MixedIntegerLinearProgram
          <sage.numerical.mip.MixedIntegerLinearProgram>`.

        - ``verbose`` -- integer (default: 0); sets the level of
          verbosity. Set to 0 by default, which means quiet.

        EXAMPLES::

            sage: C = graphs.CubeGraph(3)
            sage: C.is_circumscribable()                                                # needs sage.numerical.mip
            True

            sage: O = graphs.OctahedralGraph()
            sage: O.is_circumscribable()                                                # needs sage.numerical.mip
            True

            sage: TT = polytopes.truncated_tetrahedron().graph()                        # needs sage.geometry.polyhedron
            sage: TT.is_circumscribable()                                               # needs sage.geometry.polyhedron sage.numerical.mip
            False

        Stellating in a face of the octahedral graph is not circumscribable::

            sage: f = set(flatten(choice(O.faces())))
            sage: O.add_edges([[6, i] for i in f])
            sage: O.is_circumscribable()                                                # needs sage.numerical.mip
            False

        .. SEEALSO::

            * :meth:`is_polyhedral`
            * :meth:`is_inscribable`

        TESTS::

            sage: G = graphs.CompleteGraph(5)
            sage: G.is_circumscribable()
            Traceback (most recent call last):
            ...
            NotImplementedError: this method only works for polyhedral graphs

        .. TODO::

            Allow the use of other, inexact but faster solvers.
        """
    def is_inscribable(self, solver: str = 'ppl', verbose: int = 0):
        """
        Test whether the graph is the graph of an inscribed polyhedron.

        A polyhedron is inscribed if all of its vertices are on a sphere.
        This is dual to the notion of circumscribed polyhedron: A Polyhedron is
        inscribed if and only if its polar dual is circumscribed and hence a
        graph is inscribable if and only if its planar dual is circumscribable.

        INPUT:

        - ``solver`` -- (default: ``'ppl'``) specify a Linear Program (LP)
          solver to be used. If set to ``None``, the default one is used. For
          more information on LP solvers and which default solver is used, see
          the method :meth:`solve
          <sage.numerical.mip.MixedIntegerLinearProgram.solve>` of the class
          :class:`MixedIntegerLinearProgram
          <sage.numerical.mip.MixedIntegerLinearProgram>`.

        - ``verbose`` -- integer (default: 0); sets the level of
          verbosity. Set to 0 by default, which means quiet.

        EXAMPLES::

            sage: H = graphs.HerschelGraph()
            sage: H.is_inscribable()            # long time (> 1 sec)                   # needs sage.numerical.mip
            False
            sage: H.planar_dual().is_inscribable()      # long time (> 1 sec)           # needs sage.numerical.mip
            True

            sage: C = graphs.CubeGraph(3)
            sage: C.is_inscribable()                                                    # needs sage.numerical.mip
            True

        Cutting off a vertex from the cube yields an uninscribable graph::

            sage: C = graphs.CubeGraph(3)
            sage: v = next(C.vertex_iterator())
            sage: triangle = [_ + v for _ in C.neighbors(v)]
            sage: C.add_edges(Combinations(triangle, 2))
            sage: C.add_edges(zip(triangle, C.neighbors(v)))
            sage: C.delete_vertex(v)
            sage: C.is_inscribable()                                                    # needs sage.numerical.mip
            False

        Breaking a face of the cube yields an uninscribable graph::

            sage: C = graphs.CubeGraph(3)
            sage: face = choice(C.faces())
            sage: C.add_edge([face[0][0], face[2][0]])
            sage: C.is_inscribable()                                                    # needs sage.numerical.mip
            False


        .. SEEALSO::

            * :meth:`is_polyhedral`
            * :meth:`is_circumscribable`

        TESTS::

            sage: G = graphs.CompleteBipartiteGraph(3,3)
            sage: G.is_inscribable()
            Traceback (most recent call last):
            ...
            NotImplementedError: this method only works for polyhedral graphs
        """
    def is_prime(self, algorithm=None):
        """
        Test whether the current graph is prime.

        A graph is prime if all its modules are trivial (i.e. empty, all of the
        graph or singletons) -- see :meth:`modular_decomposition`.
        This method computes the modular decomposition tree using
        :meth:`~sage.graphs.graph.Graph.modular_decomposition`.

        INPUT:

        - ``algorithm`` -- string (default: ``None``); the algorithm used to
          compute the modular decomposition tree; the value is forwarded
          directly to :meth:`~sage.graphs.graph.Graph.modular_decomposition`.

        EXAMPLES:

        The Petersen Graph and the Bull Graph are both prime::

            sage: graphs.PetersenGraph().is_prime()
            True
            sage: graphs.BullGraph().is_prime()
            True

        Though quite obviously, the disjoint union of them is not::

            sage: (graphs.PetersenGraph() + graphs.BullGraph()).is_prime()
            False

        TESTS::

            sage: graphs.EmptyGraph().is_prime()
            True
        """
    def gomory_hu_tree(self, algorithm=None, solver=None, verbose: int = 0, *, integrality_tolerance: float = 0.001):
        '''
        Return a Gomory-Hu tree of ``self``.

        Given a tree `T` with labeled edges representing capacities, it is very
        easy to determine the maximum flow between any pair of vertices :
        it is the minimal label on the edges of the unique path between them.

        Given a graph `G`, a Gomory-Hu tree `T` of `G` is a tree with the same
        set of vertices, and such that the maximum flow between any two vertices
        is the same in `G` as in `T`. See the :wikipedia:`Gomory–Hu_tree`. Note
        that, in general, a graph admits more than one Gomory-Hu tree.

        See also 15.4 (Gomory-Hu trees) from [Sch2003]_.

        INPUT:

        - ``algorithm`` -- select the algorithm used by the :meth:`edge_cut`
          method. Refer to its documentation for allowed values and default
          behaviour.

        - ``solver`` -- string (default: ``None``); specifies a Mixed Integer
          Linear Programming (MILP) solver to be used. If set to ``None``, the
          default one is used. For more information on MILP solvers and which
          default solver is used, see the method :meth:`solve
          <sage.numerical.mip.MixedIntegerLinearProgram.solve>` of the class
          :class:`MixedIntegerLinearProgram
          <sage.numerical.mip.MixedIntegerLinearProgram>`.

          Only useful when ``algorithm == "LP"``.

        - ``verbose`` -- integer (default: 0); sets the level of
          verbosity. Set to 0 by default, which means quiet.

          Only useful when ``algorithm == "LP"``.

        - ``integrality_tolerance`` -- float; parameter for use with MILP
          solvers over an inexact base ring; see
          :meth:`MixedIntegerLinearProgram.get_values`.

          Only useful when ``algorithm == "LP"``.

        OUTPUT: a graph with labeled edges

        EXAMPLES:

        Taking the Petersen graph::

            sage: g = graphs.PetersenGraph()
            sage: t = g.gomory_hu_tree()

        Obviously, this graph is a tree::

            sage: t.is_tree()
            True

        Note that if the original graph is not connected, then the Gomory-Hu
        tree is in fact a forest::

            sage: (2*g).gomory_hu_tree().is_forest()
            True
            sage: (2*g).gomory_hu_tree().is_connected()
            False

        On the other hand, such a tree has lost nothing of the initial graph
        connectedness::

            sage: all(t.flow(u,v) == g.flow(u,v) for u,v in Subsets(g.vertices(sort=False), 2))
            True

        Just to make sure, we can check that the same is true for two vertices
        in a random graph::

            sage: g = graphs.RandomGNP(20,.3)
            sage: t = g.gomory_hu_tree()
            sage: g.flow(0,1) == t.flow(0,1)
            True

        And also the min cut::

            sage: g.edge_connectivity() == min(t.edge_labels()) or not g.is_connected()
            True

        If the graph has an edge whose removal increases the number of connected
        components, the flow between the parts separated by this edge is one::

            sage: g = Graph()
            sage: g.add_clique([1, 2, 3, 4])
            sage: g.add_clique([5, 6, 7, 8])
            sage: g.add_edge(1, 5)
            sage: t = g.gomory_hu_tree()
            sage: t.edge_label(1, 5)
            1
            sage: g.flow(randint(1, 4), randint(5, 8)) == t.edge_label(1, 5)
            True
            sage: for u, v in g.edge_iterator(labels=False):
            ....:     g.set_edge_label(u, v, 3)
            sage: t = g.gomory_hu_tree()
            sage: t.edge_label(1, 5)
            3
            sage: g.flow(randint(1, 4), randint(5, 8)) == t.edge_label(1, 5)
            True

        TESTS:

        :issue:`16475`::

            sage: G = graphs.PetersenGraph()
            sage: for u,v in G.edge_iterator(labels=False):
            ....:     G.set_edge_label(u, v, 1)
            sage: for u, v in [(0, 1), (0, 4), (0, 5), (1, 2), (1, 6), (3, 4), (5, 7), (5, 8)]:
            ....:     G.set_edge_label(u, v, 2)
            sage: T = G.gomory_hu_tree()
            sage: from itertools import combinations
            sage: for u,v in combinations(G,2):
            ....:     assert T.flow(u,v,use_edge_labels=True) == G.flow(u,v,use_edge_labels=True)

            sage: graphs.EmptyGraph().gomory_hu_tree()
            Graph on 0 vertices
        '''
    def two_factor_petersen(self, solver=None, verbose: int = 0, *, integrality_tolerance: float = 0.001):
        """
        Return a decomposition of the graph into 2-factors.

        Petersen's 2-factor decomposition theorem asserts that any `2r`-regular
        graph `G` can be decomposed into 2-factors.  Equivalently, it means that
        the edges of any `2r`-regular graphs can be partitioned in `r` sets
        `C_1,\\dots,C_r` such that for all `i`, the set `C_i` is a disjoint union
        of cycles (a 2-regular graph).

        As any graph of maximal degree `\\Delta` can be completed into a regular
        graph of degree `2\\lceil\\frac\\Delta 2\\rceil`, this result also means
        that the edges of any graph of degree `\\Delta` can be partitioned in
        `r=2\\lceil\\frac\\Delta 2\\rceil` sets `C_1,\\dots,C_r` such that for all
        `i`, the set `C_i` is a graph of maximal degree `2` (a disjoint union of
        paths and cycles).

        INPUT:

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

        The Complete Graph on `7` vertices is a `6`-regular graph, so it can be
        edge-partitionned into `2`-regular graphs::

            sage: g = graphs.CompleteGraph(7)
            sage: classes = g.two_factor_petersen()                                     # needs sage.numerical.mip
            sage: for c in classes:                                                     # needs sage.numerical.mip
            ....:     gg = Graph()
            ....:     gg.add_edges(c)
            ....:     print(max(gg.degree())<=2)
            True
            True
            True
            sage: Set(set(classes[0])                                                   # needs sage.numerical.mip
            ....:     | set(classes[1])
            ....:     | set(classes[2])).cardinality() == g.size()
            True

        ::

            sage: g = graphs.CirculantGraph(24, [7, 11])
            sage: cl = g.two_factor_petersen()                                          # needs sage.numerical.mip
            sage: g.plot(edge_colors={'black':cl[0], 'red':cl[1]})                      # needs sage.numerical.mip sage.plot
            Graphics object consisting of 73 graphics primitives
        """
    def kirchhoff_symanzik_polynomial(self, name: str = 't'):
        """
        Return the Kirchhoff-Symanzik polynomial of a graph.

        This is a polynomial in variables `t_e` (each of them representing an
        edge of the graph `G`) defined as a sum over all spanning trees:

        .. MATH::

            \\Psi_G(t) = \\sum_{\\substack{T\\subseteq V \\\\ \\text{a spanning tree}}} \\prod_{e \\not\\in E(T)} t_e

        This is also called the first Symanzik polynomial or the Kirchhoff
        polynomial.

        INPUT:

        - ``name`` -- name of the variables (default: ``'t'``)

        OUTPUT: a polynomial with integer coefficients

        ALGORITHM:

            This is computed here using a determinant, as explained in Section
            3.1 of [Mar2009a]_.

            As an intermediate step, one computes a cycle basis `\\mathcal C` of
            `G` and a rectangular `|\\mathcal C| \\times |E(G)|` matrix with
            entries in `\\{-1,0,1\\}`, which describes which edge belong to which
            cycle of `\\mathcal C` and their respective orientations.

            More precisely, after fixing an arbitrary orientation for each edge
            `e\\in E(G)` and each cycle `C\\in\\mathcal C`, one gets a sign for
            every incident pair (edge, cycle) which is `1` if the orientation
            coincide and `-1` otherwise.

        EXAMPLES:

        For the cycle of length 5::

            sage: G = graphs.CycleGraph(5)
            sage: G.kirchhoff_symanzik_polynomial()                                     # needs networkx sage.modules
            t0 + t1 + t2 + t3 + t4

        One can use another letter for variables::

            sage: G.kirchhoff_symanzik_polynomial(name='u')                             # needs networkx sage.modules
            u0 + u1 + u2 + u3 + u4

        For the 'coffee bean' graph::

            sage: G = Graph([(0,1,'a'),(0,1,'b'),(0,1,'c')], multiedges=True)
            sage: G.kirchhoff_symanzik_polynomial()                                     # needs networkx sage.modules
            t0*t1 + t0*t2 + t1*t2

        For the 'parachute' graph::

            sage: G = Graph([(0,2,'a'),(0,2,'b'),(0,1,'c'),(1,2,'d')], multiedges=True)
            sage: G.kirchhoff_symanzik_polynomial()                                     # needs networkx sage.modules
            t0*t1 + t0*t2 + t1*t2 + t1*t3 + t2*t3

        For the complete graph with 4 vertices::

            sage: G = graphs.CompleteGraph(4)
            sage: G.kirchhoff_symanzik_polynomial()                                     # needs networkx sage.modules
            t0*t1*t3 + t0*t2*t3 + t1*t2*t3 + t0*t1*t4 + t0*t2*t4 + t1*t2*t4
            + t1*t3*t4 + t2*t3*t4 + t0*t1*t5 + t0*t2*t5 + t1*t2*t5 + t0*t3*t5
            + t2*t3*t5 + t0*t4*t5 + t1*t4*t5 + t3*t4*t5

        REFERENCES:

        [Bro2011]_
        """
    def magnitude_function(self):
        """
        Return the magnitude function of the graph as a rational function.

        This is defined as the sum of all coefficients in the inverse of the
        matrix `Z` whose coefficient `Z_{i,j}` indexed by a pair of vertices
        `(i,j)` is `q^d(i,j)` where `d` is the distance function in the graph.

        By convention, if the distance from `i` to `j` is infinite (for two
        vertices not path connected) then `Z_{i,j}=0`.

        The value of the magnitude function at `q=0` is the cardinality of the
        graph. The magnitude function of a disjoint union is the sum of the
        magnitudes functions of the connected components. The magnitude function
        of a Cartesian product is the product of the magnitudes functions of the
        factors.

        EXAMPLES::

            sage: g = Graph({1:[], 2:[]})
            sage: g.magnitude_function()                                                # needs sage.modules
            2

            sage: g = graphs.CycleGraph(4)
            sage: g.magnitude_function()                                                # needs sage.modules
            4/(q^2 + 2*q + 1)

            sage: g = graphs.CycleGraph(5)
            sage: m = g.magnitude_function(); m                                         # needs sage.modules
            5/(2*q^2 + 2*q + 1)

        One can expand the magnitude as a power series in `q` as follows::

            sage: q = QQ[['q']].gen()
            sage: m(q)                                                                  # needs sage.modules
            5 - 10*q + 10*q^2 - 20*q^4 + 40*q^5 - 40*q^6 + ...

        One can also use the substitution `q = exp(-t)` to obtain the magnitude
        function as a function of `t`::

            sage: g = graphs.CycleGraph(6)
            sage: m = g.magnitude_function()                                            # needs sage.modules
            sage: t = var('t')                                                          # needs sage.modules sage.symbolic
            sage: m(exp(-t))                                                            # needs sage.modules sage.symbolic
            6/(2*e^(-t) + 2*e^(-2*t) + e^(-3*t) + 1)

        TESTS::

            sage: g = Graph()
            sage: g.magnitude_function()                                                # needs sage.modules
            0

            sage: g = Graph({1:[]})
            sage: g.magnitude_function()                                                # needs sage.modules
            1

            sage: g = graphs.PathGraph(4)
            sage: g.magnitude_function()                                                # needs sage.modules
            (-2*q + 4)/(q + 1)

        REFERENCES:

        .. [Lein] Tom Leinster, *The magnitude of metric spaces*.
           Doc. Math. 18 (2013), 857-905.
        """
    def ihara_zeta_function_inverse(self):
        """
        Compute the inverse of the Ihara zeta function of the graph.

        This is a polynomial in one variable with integer coefficients. The
        Ihara zeta function itself is the inverse of this polynomial.

        See the :wikipedia:`Ihara zeta function` for more information.

        ALGORITHM:

        This is computed here as the (reversed) characteristic polynomial of a
        square matrix of size twice the number of edges, related to the
        adjacency matrix of the line graph, see for example Proposition 9 in
        [SS2008]_ and Def. 4.1 in [Ter2011]_.

        The graph is first replaced by its 2-core, as this does not change the
        Ihara zeta function.

        EXAMPLES::

            sage: G = graphs.CompleteGraph(4)
            sage: factor(G.ihara_zeta_function_inverse())                               # needs sage.libs.pari sage.modules
            (2*t - 1) * (t + 1)^2 * (t - 1)^3 * (2*t^2 + t + 1)^3

            sage: G = graphs.CompleteGraph(5)
            sage: factor(G.ihara_zeta_function_inverse())                               # needs sage.libs.pari sage.modules
            (-1) * (3*t - 1) * (t + 1)^5 * (t - 1)^6 * (3*t^2 + t + 1)^4

            sage: G = graphs.PetersenGraph()
            sage: factor(G.ihara_zeta_function_inverse())                               # needs sage.libs.pari sage.modules
            (-1) * (2*t - 1) * (t + 1)^5 * (t - 1)^6 * (2*t^2 + 2*t + 1)^4
            * (2*t^2 - t + 1)^5

            sage: G = graphs.RandomTree(10)
            sage: G.ihara_zeta_function_inverse()                                       # needs sage.libs.pari sage.modules
            1

        REFERENCES:

        [HST2001]_
        """
    def effective_resistance(self, i, j, *, base_ring=None):
        """
        Return the effective resistance between nodes `i` and `j`.

        The resistance distance between vertices `i` and `j` of a simple
        connected graph `G` is defined as the effective resistance between the
        two vertices on an electrical network constructed from `G` replacing
        each edge of the graph by a unit (1 ohm) resistor.

        See the :wikipedia:`Resistance_distance` for more information.

        INPUT:

        - ``i``, ``j`` -- vertices of the graph

        - ``base_ring`` -- a ring (default: ``None``); the base ring
          of the matrix space to use

        OUTPUT: rational number denoting resistance between nodes `i` and `j`

        EXAMPLES:

        Effective resistances in a straight linear 2-tree on 6 vertices ::

            sage: # needs sage.modules
            sage: G = Graph([(0,1),(0,2),(1,2),(1,3),(3,5),(2,4),(2,3),(3,4),(4,5)])
            sage: G.effective_resistance(0,1)
            34/55
            sage: G.effective_resistance(0,3)
            49/55
            sage: G.effective_resistance(1,4)
            9/11
            sage: G.effective_resistance(0,5)
            15/11

        Effective resistances in a fan on 6 vertices ::

            sage: # needs sage.modules
            sage: H = Graph([(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(1,2),(2,3),(3,4),(4,5)])
            sage: H.effective_resistance(1,5)
            6/5
            sage: H.effective_resistance(1,3)
            49/55
            sage: H.effective_resistance(1,1)
            0

        Using a different base ring::

            sage: H.effective_resistance(1, 5, base_ring=RDF)   # abs tol 1e-14         # needs numpy sage.modules
            1.2000000000000000
            sage: H.effective_resistance(1, 1, base_ring=RDF)                           # needs sage.modules
            0.0

        .. SEEALSO::

            * :meth:`effective_resistance_matrix` --
              a similar method giving a matrix full of all effective
              resistances between all nodes

            * :meth:`least_effective_resistance` --
              gives node pairs with least effective resistances

            * See :wikipedia:`Resistance_distance` for more details.

        TESTS::

            sage: # needs sage.modules
            sage: G = graphs.CompleteGraph(4)
            sage: all(G.effective_resistance(u, v) == 1/2
            ....:     for u,v in G.edge_iterator(labels=False))
            True
            sage: Graph(1).effective_resistance(0,0)
            0
            sage: G = Graph([(0,1),(1,2)])
            sage: G.effective_resistance(0,2)
            2
            sage: G = Graph([(0,1),(1,2),(2,0)])
            sage: G.effective_resistance(0,2)
            2/3
            sage: G = Graph([(0,1),(0,2),(0,3),(0,4),(0,5),(1,2),(2,3),(3,4),(4,5),(5,1)])
            sage: r = G.effective_resistance(0,3)
            sage: r == fibonacci(2*(5-3)+1)*fibonacci(2*3-1)/fibonacci(2*5)             # needs sage.libs.pari
            True
            sage: G = graphs.PathGraph(4)
            sage: G.delete_edge(2,3)
            sage: G.effective_resistance(0,2)
            2
            sage: G.effective_resistance(0,3)
            +Infinity
        """
    def effective_resistance_matrix(self, vertices=None, nonedgesonly: bool = True, *, base_ring=None, **kwds):
        """
        Return a matrix whose (`i` , `j`) entry gives the effective resistance
        between vertices `i` and `j`.

        The resistance distance between vertices `i` and `j` of a simple
        connected graph `G` is defined as the effective resistance between the
        two vertices on an electrical network constructed from `G` replacing
        each edge of the graph by a unit (1 ohm) resistor.

        By default, the matrix returned is over the rationals.

        INPUT:

        - ``nonedgesonly`` -- boolean (default: ``True``); if ``True`` assign
          zero resistance to pairs of adjacent vertices.

        - ``vertices`` -- list (default: ``None``); the ordering of the
          vertices defining how they should appear in the matrix. By default,
          the ordering given by :meth:`GenericGraph.vertices` is used.

        - ``base_ring`` -- a ring (default: ``None``); the base ring
          of the matrix space to use

        - ``**kwds`` -- other keywords to pass to
          :func:`~sage.matrix.constructor.matrix`

        OUTPUT: matrix

        EXAMPLES:

        The effective resistance matrix  for a straight linear 2-tree counting
        only non-adjacent vertex pairs ::

            sage: G = Graph([(0,1),(0,2),(1,2),(1,3),(3,5),(2,4),(2,3),(3,4),(4,5)])
            sage: G.effective_resistance_matrix()                                       # needs sage.modules
            [    0     0     0 49/55 59/55 15/11]
            [    0     0     0     0  9/11 59/55]
            [    0     0     0     0     0 49/55]
            [49/55     0     0     0     0     0]
            [59/55  9/11     0     0     0     0]
            [15/11 59/55 49/55     0     0     0]

        The same effective resistance matrix, this time including adjacent
        vertices ::

            sage: G.effective_resistance_matrix(nonedgesonly=False)                     # needs sage.modules
            [    0 34/55 34/55 49/55 59/55 15/11]
            [34/55     0 26/55 31/55  9/11 59/55]
            [34/55 26/55     0  5/11 31/55 49/55]
            [49/55 31/55  5/11     0 26/55 34/55]
            [59/55  9/11 31/55 26/55     0 34/55]
            [15/11 59/55 49/55 34/55 34/55     0]

        This example illustrates the common neighbors matrix  for a fan on 6
        vertices counting only non-adjacent vertex pairs ::

            sage: H = Graph([(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(1,2),(2,3),(3,4),(4,5)])
            sage: H.effective_resistance_matrix()                                       # needs sage.modules
            [    0     0     0     0     0     0     0]
            [    0     0     0 49/55 56/55   6/5 89/55]
            [    0     0     0     0   4/5 56/55 81/55]
            [    0 49/55     0     0     0 49/55 16/11]
            [    0 56/55   4/5     0     0     0 81/55]
            [    0   6/5 56/55 49/55     0     0 89/55]
            [    0 89/55 81/55 16/11 81/55 89/55     0]

        A different base ring::

            sage: H.effective_resistance_matrix(base_ring=RDF)[0, 0].parent()           # needs numpy sage.modules
            Real Double Field

        .. SEEALSO::

            * :meth:`least_effective_resistance` --
              gives node pairs with least effective resistances

            * :meth:`effective_resistance` --
              computes effective resistance for a single node pair

            * See :wikipedia:`Resistance_Distance` for more details.

        TESTS::

            sage: graphs.CompleteGraph(4).effective_resistance_matrix()                 # needs sage.modules
            [0 0 0 0]
            [0 0 0 0]
            [0 0 0 0]
            [0 0 0 0]

            sage: G = Graph(multiedges=True, sparse=True)
            sage: G.add_edges([(0, 1)] * 3)
            sage: G.effective_resistance_matrix()                                       # needs sage.modules
            Traceback (most recent call last):
            ...
            ValueError: This method is not known to work on graphs with
            multiedges. Perhaps this method can be updated to handle them, but
            in the meantime if you want to use it please disallow multiedges
            using allow_multiple_edges().

            sage: # needs sage.modules
            sage: graphs.CompleteGraph(4).effective_resistance_matrix(nonedgesonly=False)
            [  0 1/2 1/2 1/2]
            [1/2   0 1/2 1/2]
            [1/2 1/2   0 1/2]
            [1/2 1/2 1/2   0]
            sage: Graph(1).effective_resistance_matrix()
            [0]
            sage: Graph().effective_resistance_matrix()
            Traceback (most recent call last):
            ...
            ValueError: unable to compute effective resistance for an empty Graph object
            sage: G = Graph([(0,1),(1,2),(2,3),(3,0),(0,2)])
            sage: G.effective_resistance_matrix()
            [0 0 0 0]
            [0 0 0 1]
            [0 0 0 0]
            [0 1 0 0]
            sage: G = Graph([(0,1),(0,2),(0,3),(0,4),(0,5),(1,2),(2,3),(3,4),(4,5),(5,1)])
            sage: r = G.effective_resistance_matrix(nonedgesonly=False)[0,3]
            sage: r == fibonacci(2*(5-3)+1)*fibonacci(2*3-1)/fibonacci(2*5)             # needs sage.libs.pari
            True

        Ask for an immutable matrix::

            sage: # needs sage.modules
            sage: G = Graph([(0, 1)])
            sage: M = G.effective_resistance_matrix(immutable=False)
            sage: M.is_immutable()
            False
            sage: M = G.effective_resistance_matrix(immutable=True)
            sage: M.is_immutable()
            True
        """
    def least_effective_resistance(self, nonedgesonly: bool = True):
        """
        Return a list of pairs of nodes with the least effective resistance.

        The resistance distance between vertices `i` and `j` of a simple
        connected graph `G` is defined as the effective resistance between the
        two vertices on an electrical network constructed from `G` replacing
        each edge of the graph by a unit (1 ohm) resistor.

        INPUT:

        - ``nonedgesonly`` -- boolean (default: ``True``); if ``True``, assign zero
          resistance to pairs of adjacent vertices

        OUTPUT: list

        EXAMPLES:

        Pairs of non-adjacent nodes with least effective resistance in a
        straight linear 2-tree on 6 vertices::

            sage: G = Graph([(0,1),(0,2),(1,2),(1,3),(3,5),(2,4),(2,3),(3,4),(4,5)])
            sage: G.least_effective_resistance()                                        # needs sage.modules
            [(1, 4)]

        Pairs of (adjacent or non-adjacent) nodes with least effective
        resistance in a straight linear 2-tree on 6 vertices ::

            sage: G.least_effective_resistance(nonedgesonly=False)                      # needs sage.modules
            [(2, 3)]

        Pairs of non-adjacent nodes with least effective resistance in a fan on
        6 vertices counting only non-adjacent vertex pairs ::

            sage: H = Graph([(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(1,2),(2,3),(3,4),(4,5)])
            sage: H.least_effective_resistance()                                        # needs sage.modules
            [(2, 4)]

        .. SEEALSO::

            * :meth:`effective_resistance_matrix` --
              a similar method giving a matrix full of all effective
              resistances

            * :meth:`effective_resistance` --
              computes effective resistance for a single node pair

            * See :wikipedia:`Resistance_distance` for more details.


        TESTS::

            sage: # needs sage.modules
            sage: graphs.CompleteGraph(4).least_effective_resistance()
            []
            sage: graphs.CompleteGraph(4).least_effective_resistance(nonedgesonly=False)
            [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
            sage: Graph(1).least_effective_resistance()
            []
            sage: G = Graph([(0,1),(1,2),(2,3),(3,0),(0,2)])
            sage: G.least_effective_resistance()
            [(1, 3)]
        """
    def common_neighbors_matrix(self, vertices=None, nonedgesonly: bool = True, *, base_ring=None, **kwds):
        """
        Return a matrix of numbers of common neighbors between each pairs.

        The `(i , j)` entry of the matrix gives the number of common
        neighbors between vertices `i` and `j`.

        This method is only valid for simple (no loops, no multiple edges)
        graphs.

        INPUT:

        - ``nonedgesonly`` -- boolean (default: ``True``); if ``True``, assigns
          `0` value to adjacent vertices.

        - ``vertices`` -- list (default: ``None``); the ordering of the
          vertices defining how they should appear in the matrix. By default,
          the ordering given by :meth:`GenericGraph.vertices` is used.

        - ``base_ring`` -- a ring (default: ``None``); the base ring
          of the matrix space to use

        - ``**kwds`` -- other keywords to pass to
          :func:`~sage.matrix.constructor.matrix`

        OUTPUT: matrix

        EXAMPLES:

        The common neighbors matrix  for a straight linear 2-tree counting
        only non-adjacent vertex pairs ::

            sage: G1 = Graph()
            sage: G1.add_edges([(0,1),(0,2),(1,2),(1,3),(3,5),(2,4),(2,3),(3,4),(4,5)])
            sage: G1.common_neighbors_matrix(nonedgesonly=True)                         # needs sage.modules
            [0 0 0 2 1 0]
            [0 0 0 0 2 1]
            [0 0 0 0 0 2]
            [2 0 0 0 0 0]
            [1 2 0 0 0 0]
            [0 1 2 0 0 0]

        We now show the common neighbors matrix which includes adjacent
        vertices ::

            sage: G1.common_neighbors_matrix(nonedgesonly=False)                        # needs sage.modules
            [0 1 1 2 1 0]
            [1 0 2 1 2 1]
            [1 2 0 2 1 2]
            [2 1 2 0 2 1]
            [1 2 1 2 0 1]
            [0 1 2 1 1 0]

        The common neighbors matrix  for a fan on 6 vertices counting only
        non-adjacent vertex pairs ::

            sage: H = Graph([(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(1,2),(2,3),(3,4),(4,5)])
            sage: H.common_neighbors_matrix()                                           # needs sage.modules
            [0 0 0 0 0 0 0]
            [0 0 0 2 1 1 1]
            [0 0 0 0 2 1 1]
            [0 2 0 0 0 2 1]
            [0 1 2 0 0 0 1]
            [0 1 1 2 0 0 1]
            [0 1 1 1 1 1 0]

        A different base ring::

            sage: H.common_neighbors_matrix(base_ring=RDF)                              # needs sage.modules
            [0.0 0.0 0.0 0.0 0.0 0.0 0.0]
            [0.0 0.0 0.0 2.0 1.0 1.0 1.0]
            [0.0 0.0 0.0 0.0 2.0 1.0 1.0]
            [0.0 2.0 0.0 0.0 0.0 2.0 1.0]
            [0.0 1.0 2.0 0.0 0.0 0.0 1.0]
            [0.0 1.0 1.0 2.0 0.0 0.0 1.0]
            [0.0 1.0 1.0 1.0 1.0 1.0 0.0]

        It is an error to input anything other than a simple graph::

            sage: G = Graph([(0,0)], loops=True)
            sage: G.common_neighbors_matrix()                                           # needs sage.modules
            Traceback (most recent call last):
            ...
            ValueError: This method is not known to work on graphs with loops.
            Perhaps this method can be updated to handle them, but in the
            meantime if you want to use it please disallow loops using
            allow_loops().

        .. SEEALSO::

            * :meth:`most_common_neighbors` --
              returns node pairs with most shared neighbors

        TESTS::

            sage: # needs sage.modules
            sage: G = graphs.CompleteGraph(4)
            sage: M = G.common_neighbors_matrix()
            sage: M.is_zero()
            True
            sage: Graph(1).common_neighbors_matrix()
            [0]
            sage: Graph().common_neighbors_matrix()
            []
            sage: G = Graph([(0,1),(1,2),(2,3),(3,0),(0,2)])
            sage: G.common_neighbors_matrix()
            [0 0 0 0]
            [0 0 0 2]
            [0 0 0 0]
            [0 2 0 0]

        Asking for an immutable matrix::

            sage: # needs sage.modules
            sage: G = Graph([(0, 1)])
            sage: M = G.common_neighbors_matrix()
            sage: M.is_immutable()
            False
            sage: M = G.common_neighbors_matrix(immutable=True)
            sage: M.is_immutable()
            True
        """
    def most_common_neighbors(self, nonedgesonly: bool = True):
        """
        Return vertex pairs with maximal number of common neighbors.

        This method is only valid for simple (no loops, no multiple edges)
        graphs with order `\\geq 2`

        INPUT:

        - ``nonedgesonly`` -- boolean (default: ``True``); if ``True``, assigns
          `0` value to adjacent vertices

        OUTPUT: list of tuples of edge pairs

        EXAMPLES:

        The maximum common neighbor (non-adjacent) pairs for a straight
        linear 2-tree ::

            sage: G1 = Graph([(0,1),(0,2),(1,2),(1,3),(3,5),(2,4),(2,3),(3,4),(4,5)])
            sage: G1.most_common_neighbors()                                            # needs sage.modules
            [(0, 3), (1, 4), (2, 5)]

        If we include non-adjacent pairs ::

            sage: G1.most_common_neighbors(nonedgesonly=False)                          # needs sage.modules
            [(0, 3), (1, 2), (1, 4), (2, 3), (2, 5), (3, 4)]

        The common neighbors matrix  for a fan on 6 vertices counting only
        non-adjacent vertex pairs ::

            sage: H = Graph([(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(1,2),(2,3),(3,4),(4,5)])
            sage: H.most_common_neighbors()                                             # needs sage.modules
            [(1, 3), (2, 4), (3, 5)]

        .. SEEALSO::

            * :meth:`common_neighbors_matrix` --
              a similar method giving a matrix of number of common neighbors

        TESTS::

            sage: # needs sage.modules
            sage: G = graphs.CompleteGraph(4)
            sage: G.most_common_neighbors()
            []
            sage: G.most_common_neighbors(nonedgesonly=False)
            [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
            sage: Graph(1).most_common_neighbors()
            Traceback (most recent call last):
            ...
            ValueError: this method is defined for graphs with at least 2 vertices
            sage: Graph().most_common_neighbors()
            Traceback (most recent call last):
            ...
            ValueError: this method is defined for graphs with at least 2 vertices
            sage: G = Graph([(0,1),(1,2),(2,3),(3,0),(0,2)])
            sage: G.most_common_neighbors()
            [(1, 3)]
            sage: G.most_common_neighbors(nonedgesonly=False)
            [(0, 2), (1, 3)]
        """
    def arboricity(self, certificate: bool = False):
        """
        Return the arboricity of the graph and an optional certificate.

        The arboricity is the minimum number of forests that covers the
        graph.

        See :wikipedia:`Arboricity`

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); whether to return
          a certificate

        OUTPUT:

        When ``certificate = True``, then the function returns `(a, F)`
        where `a` is the arboricity and `F` is a list of `a` disjoint forests
        that partitions the edge set of `g`. The forests are represented as
        subgraphs of the original graph.

        If ``certificate = False``, the function returns just a integer
        indicating the arboricity.

        ALGORITHM:

        Represent the graph as a graphical matroid, then apply matroid
        :meth:`sage.matroid.partition` algorithm from the matroids module.

        EXAMPLES::

            sage: G = graphs.PetersenGraph()
            sage: a, F = G.arboricity(True)                                             # needs sage.modules
            sage: a                                                                     # needs sage.modules
            2
            sage: all([f.is_forest() for f in F])                                       # needs sage.modules
            True
            sage: len(set.union(*[set(f.edges(sort=False)) for f in F])) == G.size()    # needs sage.modules
            True

        TESTS::

            sage: g = Graph()
            sage: g.arboricity(True)                                                    # needs sage.modules
            (0, [])
        """
    def is_antipodal(self):
        """
        Check whether this graph is antipodal.

        A graph `G` of diameter `d` is said to be antipodal if its distance-`d`
        graph is a disjoint union of cliques.

        EXAMPLES::

            sage: G = graphs.JohnsonGraph(10, 5)
            sage: G.is_antipodal()
            True
            sage: H = G.folded_graph()
            sage: H.is_antipodal()
            False

        REFERENCES:

        See [BCN1989]_ p. 438 or [Sam2012]_ for this definition of antipodal
        graphs.

        TESTS::

            sage: G = graphs.PetersenGraph()
            sage: G.is_antipodal()
            False
            sage: G = graphs.HammingGraph(7, 2)
            sage: G.is_antipodal()
            True
            sage: G = Graph([(0,1), (2, 3)])
            sage: G.is_antipodal()
            False
            sage: G = Graph(4)
            sage: G.is_antipodal()
            True
            sage: graphs.CompleteGraph(5).is_antipodal()
            True
            sage: G = Graph()
            sage: G.is_antipodal()
            Traceback (most recent call last):
            ...
            ValueError: diameter is not defined for the empty graph
            sage: G = Graph(1)
            sage: G.is_antipodal()
            True
        """
    def folded_graph(self, check: bool = False):
        """
        Return the antipodal fold of this graph.

        Given an antipodal graph `G` let `G_d` be its distance-`d` graph.
        Then the folded graph of `G` has a vertex for each maximal clique
        of `G_d` and two cliques are adjacent if there is an edge in `G`
        connecting the two.

        .. SEEALSO::

            :meth:`sage.graphs.graph.is_antipodal`

        INPUT:

        - ``check`` -- boolean (default: ``False``); whether to check if the
          graph is antipodal. If ``check`` is ``True`` and the graph is not
          antipodal, then return ``False``.

        OUTPUT: this function returns a new graph and ``self`` is not touched

        .. NOTE::

            The input is expected to be an antipodal graph.
            You can check that a graph is antipodal using
            :meth:`sage.graphs.graph.is_antipodal`.

        EXAMPLES::

            sage: G = graphs.JohnsonGraph(10, 5)
            sage: H = G.folded_graph(); H
            Folded Johnson graph with parameters 10,5: Graph on 126 vertices
            sage: Gd = G.distance_graph(G.diameter())
            sage: all(i == 1 for i in Gd.degree())
            True
            sage: H.is_distance_regular(True)
            ([25, 16, None], [None, 1, 4])

        This method doesn't check if the graph is antipodal::

            sage: G = graphs.PetersenGraph()
            sage: G.is_antipodal()
            False
            sage: G.folded_graph()  # some garbage
            Folded Petersen graph: Graph on 2 vertices
            sage: G.folded_graph(check=True)
            False

        REFERENCES:

        See [BCN1989]_ p. 438 or [Sam2012]_ for this definition of folded graph.

        TESTS::

            sage: G = Graph(5)
            sage: G.folded_graph()
            Folded Graph: Graph on 1 vertex
            sage: G = graphs.CompleteGraph(5)
            sage: G.folded_graph()
            Folded Complete graph: Graph on 1 vertex
            sage: G = Graph()
            sage: G.folded_graph()
            Traceback (most recent call last):
            ...
            ValueError: diameter is not defined for the empty graph
            sage: G = Graph(1)
            sage: G.folded_graph()
            Folded Graph: Graph on 1 vertex
        """
    def antipodal_graph(self):
        """
        Return the antipodal graph of ``self``.

        The antipodal graph of a graph `G` has the same vertex set of `G` and
        two vertices are adjacent if their distance in `G` is equal to the
        diameter of `G`.

        OUTPUT: a new graph. ``self`` is not touched

        EXAMPLES::

            sage: G = graphs.JohnsonGraph(10, 5)
            sage: G.antipodal_graph()
            Antipodal graph of Johnson graph with parameters 10,5: Graph on 252 vertices
            sage: G = graphs.HammingGraph(8, 2)
            sage: G.antipodal_graph()
            Antipodal graph of Hamming Graph with parameters 8,2: Graph on 256 vertices

        The antipodal graph of a disconnected graph is its complement::

            sage: G = Graph(5)
            sage: H = G.antipodal_graph()
            sage: H.is_isomorphic(G.complement())
            True

        TESTS::

            sage: G = Graph([(0, 1), (2, 3)])
            sage: H = G.antipodal_graph()
            sage: H.is_isomorphic(Graph([(0, 2), (0, 3), (1, 2), (1, 3)]))
            True
            sage: G = Graph()
            sage: G.antipodal_graph()
            Traceback (most recent call last):
            ...
            ValueError: diameter is not defined for the empty graph
            sage: G = Graph(1)
            sage: G.antipodal_graph()
            Antipodal graph of Graph: Looped graph on 1 vertex
        """
    def bipartite_double(self, extended: bool = False):
        """
        Return the (extended) bipartite double of this graph.

        The bipartite double of a graph `G` has vertex set
        `\\{ (v,0), (v,1) : v \\in G\\}` and for any edge `(u, v)` in `G`
        it has edges `((u,0),(v,1))` and `((u,1),(v,0))`.
        Note that this is the tensor product of `G` with `K_2`.

        The extended bipartite double of `G` is the bipartite double of
        `G` after added all edges `((v,0),(v,1))` for all vertices `v`.

        INPUT:

        - ``extended`` -- boolean (default: ``False``); whether to return the
          extended bipartite double, or only the bipartite double (default)

        OUTPUT: a graph; ``self`` is left untouched

        EXAMPLES::

            sage: G = graphs.PetersenGraph()
            sage: H = G.bipartite_double()
            sage: G == graphs.PetersenGraph()  # G is left invariant
            True
            sage: H.order() == 2 * G.order()
            True
            sage: H.size() == 2 * G.size()
            True
            sage: H.is_bipartite()
            True
            sage: H.bipartite_sets() == (set([(v, 0) for v in G]),
            ....: set([(v, 1) for v in G]))
            True
            sage: H.is_isomorphic(G.tensor_product(graphs.CompleteGraph(2)))
            True

        Behaviour with disconnected graphs::

            sage: G1 = graphs.PetersenGraph()
            sage: G2 = graphs.HoffmanGraph()
            sage: G = G1.disjoint_union(G2)
            sage: H = G.bipartite_double()
            sage: H1 = G1.bipartite_double()
            sage: H2 = G2.bipartite_double()
            sage: H.is_isomorphic(H1.disjoint_union(H2))
            True

        .. SEEALSO::

            :wikipedia:`Bipartite_double_cover`,
            `WolframAlpha Bipartite Double
            <https://mathworld.wolfram.com/BipartiteDoubleGraph.html>`_,
            [VDKT2016]_ p. 20 for the extended bipartite double.

        TESTS::

            sage: G = graphs.PetersenGraph()
            sage: H = G.bipartite_double(True)
            sage: G == graphs.PetersenGraph()  # G is left invariant
            True
            sage: H.order() == 2 * G.order()
            True
            sage: H.size() == 2 * G.size() + G.order()
            True
            sage: H.is_bipartite()
            True
            sage: H.bipartite_sets() == (set([(v, 0) for v in G]),
            ....: set([(v, 1) for v in G]))
            True
            sage: H.is_isomorphic(G.tensor_product(graphs.CompleteGraph(2)))
            False

        Test edge cases::

            sage: G = Graph()
            sage: H = G.bipartite_double()
            sage: H.size() + H.order()
            0
            sage: H = G.bipartite_double(True)
            sage: H.size() + H.order()
            0
            sage: G = Graph(1)
            sage: H = G.bipartite_double()
            sage: H.size() == 0 and H.order() == 2
            True
            sage: H = G.bipartite_double(True)
            sage: H.is_isomorphic(Graph([(0, 1)]))
            True
        """
    def is_projective_planar(self, return_map: bool = False):
        """
        Check whether ``self`` is projective planar.

        A graph is projective planar if it can be embedded in the projective
        plane.  The approach is to check that the graph does not contain any
        of the known forbidden minors.

        INPUT:

        - ``return_map`` -- boolean (default: ``False``); whether to return
          a map indicating one of the forbidden graph minors if in fact the
          graph is not projective planar, or only True/False.

        OUTPUT:

        Return ``True`` if the graph is projective planar and ``False`` if not.  If the
        parameter ``map_flag`` is ``True`` and the graph is not projective planar, then
        the method returns ``False`` and a map from :meth:`~Graph.minor`
        indicating one of the forbidden graph minors.

        EXAMPLES:

        The Peterson graph is a known projective planar graph::

            sage: P = graphs.PetersenGraph()
            sage: P.is_projective_planar()  # long time
            True

        `K_{4,4}` has a projective plane crossing number of 2. One of the
        minimal forbidden minors is `K_{4,4} - e`, so we get a one-to-one
        dictionary from :meth:`~Graph.minor`::

            sage: K44 = graphs.CompleteBipartiteGraph(4, 4)
            sage: K44.is_projective_planar(return_map=True)
            (False,
             {0: [0], 1: [1], 2: [2], 3: [3], 4: [4], 5: [5], 6: [6], 7: [7]})

        .. SEEALSO::

            - :meth:`~Graph.minor`

        TESTS::

            sage: len(graphs.p2_forbidden_minors())
            35
        """
    chromatic_polynomial: Incomplete
    rank_decomposition: Incomplete
    matching_polynomial: Incomplete
    geodetic_closure: Incomplete

__doc__: Incomplete
