from _typeshed import Incomplete
from collections.abc import Generator
from sage.graphs.digraph import DiGraph as DiGraph

def orient(G, f, weighted=None, data_structure=None, sparse=None, immutable=None, hash_labels=None):
    '''
    Return an oriented version of `G` according the input function `f`.

    INPUT:

    - ``G`` -- an undirected graph

    - ``f`` -- a function that inputs an edge and outputs an orientation of this
      edge

    - ``weighted`` -- boolean (default: ``None``); weightedness for the oriented
      digraph. By default (``None``), the graph and its orientation will behave
      the same.

    - ``sparse`` -- boolean (default: ``None``); ``sparse=True`` is an alias for
      ``data_structure="sparse"``, and ``sparse=False`` is an alias for
      ``data_structure="dense"``. Only used when ``data_structure=None``.

    - ``data_structure`` -- string (default: ``None``); one of ``\'sparse\'``,
      ``\'static_sparse\'``, or ``\'dense\'``. See the documentation of
      :class:`DiGraph`.

    - ``immutable`` -- boolean (default: ``None``); whether to create a
      mutable/immutable digraph. Only used when ``data_structure=None``.

      * ``immutable=None`` (default) means that the graph and its orientation
        will behave the same way.

      * ``immutable=True`` is a shortcut for ``data_structure=\'static_sparse\'``

      * ``immutable=False`` means that the created digraph is mutable. When used
        to orient an immutable graph, the data structure used is ``\'sparse\'``
        unless anything else is specified.

    - ``hash_labels`` -- boolean (default: ``None``); whether to include edge
      labels during hashing of the oriented digraph. This parameter defaults to
      ``True`` if the graph is weighted. This parameter is ignored when
      parameter ``immutable`` is not ``True``. Beware that trying to hash
      unhashable labels will raise an error.

    OUTPUT: a :class:`DiGraph` object

    .. NOTE::

        This method behaves similarly to method
        :meth:`~sage.graphs.generic_graph.GenericGraph.copy`. That is, the
        returned digraph uses the same data structure by default, unless the
        user asks to use another data structure, and the attributes of the input
        graph are copied.

    EXAMPLES::

        sage: G = graphs.CycleGraph(4); G
        Cycle graph: Graph on 4 vertices
        sage: D = G.orient(lambda e:e if e[0] < e[1] else (e[1], e[0], e[2])); D
        Orientation of Cycle graph: Digraph on 4 vertices
        sage: sorted(D.edges(labels=False))
        [(0, 1), (0, 3), (1, 2), (2, 3)]

    TESTS:

    We make sure that one can get an immutable orientation by providing the
    ``data_structure`` optional argument::

        sage: def foo(e):
        ....:     return e if e[0] < e[1] else (e[1], e[0], e[2])
        sage: G = graphs.CycleGraph(4)
        sage: D = G.orient(foo, data_structure=\'static_sparse\')
        sage: D.is_immutable()
        True
        sage: D = G.orient(foo, immutable=True)
        sage: D.is_immutable()
        True

    Bad input::

        sage: G.orient(foo, data_structure=\'sparse\', sparse=False)
        Traceback (most recent call last):
        ...
        ValueError: you cannot define \'immutable\' or \'sparse\' when \'data_structure\' has a value
        sage: G.orient(foo, data_structure=\'sparse\', immutable=True)
        Traceback (most recent call last):
        ...
        ValueError: you cannot define \'immutable\' or \'sparse\' when \'data_structure\' has a value
        sage: G.orient(foo, immutable=True, sparse=False)
        Traceback (most recent call last):
        ...
        ValueError: there is no dense immutable backend at the moment

    Which backend? ::

        sage: G.orient(foo, data_structure=\'sparse\')._backend
        <sage.graphs.base.sparse_graph.SparseGraphBackend object at ...>
        sage: G.orient(foo, data_structure=\'dense\')._backend
        <sage.graphs.base.dense_graph.DenseGraphBackend object at ...>
        sage: G.orient(foo, data_structure=\'static_sparse\')._backend
        <sage.graphs.base.static_sparse_backend.StaticSparseBackend object at ...>
        sage: G.orient(foo, immutable=True)._backend
        <sage.graphs.base.static_sparse_backend.StaticSparseBackend object at ...>
        sage: G.orient(foo, immutable=True, sparse=True)._backend
        <sage.graphs.base.static_sparse_backend.StaticSparseBackend object at ...>
        sage: G.orient(foo, immutable=False, sparse=True)._backend
        <sage.graphs.base.sparse_graph.SparseGraphBackend object at ...>
        sage: G.orient(foo, immutable=False, sparse=False)._backend
        <sage.graphs.base.sparse_graph.SparseGraphBackend object at ...>
        sage: G.orient(foo, data_structure=None, immutable=None, sparse=True)._backend
        <sage.graphs.base.sparse_graph.SparseGraphBackend object at ...>
        sage: G.orient(foo, data_structure=None, immutable=None, sparse=False)._backend
        <sage.graphs.base.dense_graph.DenseGraphBackend object at ...>
        sage: G.orient(foo, data_structure=None, immutable=None, sparse=None)._backend
        <sage.graphs.base.sparse_graph.SparseGraphBackend object at ...>
        sage: H = Graph(data_structure=\'dense\')
        sage: H.orient(foo, data_structure=None, immutable=None, sparse=None)._backend
        <sage.graphs.base.dense_graph.DenseGraphBackend object at ...>
    '''
def orientations(G, data_structure=None, sparse=None) -> Generator[Incomplete]:
    '''
    Return an iterator over orientations of `G`.

    An *orientation* of an undirected graph is a directed graph such that
    every edge is assigned a direction.  Hence there are `2^s` oriented
    digraphs for a simple graph with `s` edges.

    INPUT:

    - ``G`` -- an undirected graph

    - ``data_structure`` -- one of ``\'sparse\'``, ``\'static_sparse\'``, or
      ``\'dense\'``; see the documentation of :class:`Graph` or :class:`DiGraph`;
      default is the data structure of `G`

    - ``sparse`` -- boolean (default: ``None``); ``sparse=True`` is an alias for
      ``data_structure="sparse"``, and ``sparse=False`` is an alias for
      ``data_structure="dense"``. By default (``None``), guess the most suitable
      data structure.

    .. WARNING::

        This always considers multiple edges of graphs as distinguishable, and
        hence, may have repeated digraphs.

    .. SEEALSO::

        - :meth:`~sage.graphs.graph.Graph.strong_orientation`
        - :meth:`~sage.graphs.orientations.strong_orientations_iterator`
        - :meth:`~sage.graphs.digraph_generators.DiGraphGenerators.nauty_directg`
        - :meth:`~sage.graphs.orientations.random_orientation`

    EXAMPLES::

        sage: G = Graph([[1,2,3], [(1, 2, \'a\'), (1, 3, \'b\')]], format=\'vertices_and_edges\')
        sage: it = G.orientations()
        sage: D = next(it)
        sage: D.edges(sort=True)
        [(1, 2, \'a\'), (1, 3, \'b\')]
        sage: D = next(it)
        sage: D.edges(sort=True)
        [(1, 2, \'a\'), (3, 1, \'b\')]

    TESTS::

        sage: G = Graph()
        sage: D = [g for g in G.orientations()]
        sage: len(D)
        1
        sage: D[0]
        Digraph on 0 vertices

        sage: G = Graph(5)
        sage: it = G.orientations()
        sage: D = next(it)
        sage: D.size()
        0

        sage: G = Graph([[1,2,\'a\'], [1,2,\'b\']], multiedges=True)
        sage: len(list(G.orientations()))
        4

        sage: G = Graph([[1,2], [1,1]], loops=True)
        sage: len(list(G.orientations()))
        2

        sage: G = Graph([[1,2],[2,3]])
        sage: next(G.orientations())
        Digraph on 3 vertices
        sage: G = graphs.PetersenGraph()
        sage: next(G.orientations())
        An orientation of Petersen graph: Digraph on 10 vertices

    An orientation must have the same ground set of vertices as the original
    graph (:issue:`24366`)::

        sage: G = Graph(1)
        sage: next(G.orientations())
        Digraph on 1 vertex

    Which backend? ::

        sage: next(G.orientations(data_structure=\'sparse\', sparse=True))._backend
        Traceback (most recent call last):
        ...
        ValueError: you cannot define \'immutable\' or \'sparse\' when \'data_structure\' has a value
        sage: next(G.orientations(sparse=True))._backend
        <sage.graphs.base.sparse_graph.SparseGraphBackend object at ...>
        sage: next(G.orientations(sparse=False))._backend
        <sage.graphs.base.dense_graph.DenseGraphBackend object at ...>
        sage: next(G.orientations())._backend
        <sage.graphs.base.sparse_graph.SparseGraphBackend object at ...>
        sage: G = Graph(1, data_structure=\'dense\')
        sage: next(G.orientations())._backend
        <sage.graphs.base.dense_graph.DenseGraphBackend object at ...>
        sage: G = Graph(1, data_structure=\'static_sparse\')
        sage: next(G.orientations())._backend
        <sage.graphs.base.static_sparse_backend.StaticSparseBackend object at ...>

    Check that the embedding is copied::

        sage: G = Graph([(0, 1), (0, 2), (1, 2)])
        sage: embedding = {0: [1, 2], 1: [2, 0], 2: [0, 1]}
        sage: G.set_embedding(embedding)
        sage: next(G.orientations()).get_embedding() == embedding
        True
        sage: G = Graph()
        sage: G.set_embedding({})
        sage: next(G.orientations()).get_embedding() == {}
        True
    '''
def acyclic_orientations(G) -> Generator[Incomplete, None, Incomplete]:
    """
    Return an iterator over all acyclic orientations of an undirected graph `G`.

    ALGORITHM:

    The algorithm is based on [Sq1998]_.
    It presents an efficient algorithm for listing the acyclic orientations of a
    graph. The algorithm is shown to require O(n) time per acyclic orientation
    generated, making it the most efficient known algorithm for generating acyclic
    orientations.

    The function uses a recursive approach to generate acyclic orientations of the
    graph. It reorders the vertices and edges of the graph, creating a new graph
    with updated labels. Then, it iteratively generates acyclic orientations by
    considering subsets of edges and checking whether they form upsets in a
    corresponding poset.

    INPUT:

    - ``G`` -- an undirected graph

    OUTPUT: an iterator over all acyclic orientations of the input graph

    .. NOTE::

        The function assumes that the input graph is undirected and the edges
        are unlabelled.

    EXAMPLES:

    To count the number of acyclic orientations for a graph::

        sage: g = Graph([(0, 3), (0, 4), (3, 4), (1, 3), (1, 2), (2, 3), (2, 4)])
        sage: it = g.acyclic_orientations()
        sage: len(list(it))
        54

    Test for arbitrary vertex labels::

        sage: g_str = Graph([('abc', 'def'), ('ghi', 'def'), ('xyz', 'abc'),
        ....:                ('xyz', 'uvw'), ('uvw', 'abc'), ('uvw', 'ghi')])
        sage: it = g_str.acyclic_orientations()
        sage: len(list(it))
        42

    Check that the method returns properly relabeled acyclic digraphs::

        sage: g = Graph([(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)])
        sage: orientations = set([frozenset(d.edges(labels=false)) for d in g.acyclic_orientations()])
        sage: len(orientations)
        18
        sage: all(d.is_directed_acyclic() for d in g.acyclic_orientations())
        True

    TESTS:

    To count the number of acyclic orientations for a graph with 0 vertices::

        sage: list(Graph().acyclic_orientations())
        []

    To count the number of acyclic orientations for a graph with 1 vertex::

        sage: list(Graph(1).acyclic_orientations())
        []

    To count the number of acyclic orientations for a graph with 2 vertices::

        sage: list(Graph(2).acyclic_orientations())
        []

    Acyclic orientations of a complete graph::

        sage: g = graphs.CompleteGraph(5)
        sage: it = g.acyclic_orientations()
        sage: len(list(it))
        120

    Graph with one edge::

        sage: list(Graph([(0, 1)]).acyclic_orientations())
        [Digraph on 2 vertices, Digraph on 2 vertices]

    Graph with two edges::

        sage: len(list(Graph([(0, 1), (1, 2)]).acyclic_orientations()))
        4

    Cycle graph::

        sage: len(list(Graph([(0, 1), (1, 2), (2, 0)]).acyclic_orientations()))
        6
    """
def strong_orientation(G):
    """
    Return a strongly connected orientation of the graph `G`.

    An orientation of an undirected graph is a digraph obtained by giving an
    unique direction to each of its edges. An orientation is said to be strong
    if there is a directed path between each pair of vertices. See also the
    :wikipedia:`Strongly_connected_component`.

    If the graph is 2-edge-connected, a strongly connected orientation can be
    found in linear time. If the given graph is not 2-connected, the orientation
    returned will ensure that each 2-connected component has a strongly
    connected orientation.

    INPUT:

    - ``G`` -- an undirected graph

    OUTPUT: a digraph representing an orientation of the current graph

    .. NOTE::

        - This method assumes that the input the graph is connected.
        - The time complexity is `O(n+m)` for ``SparseGraph`` and `O(n^2)` for
          ``DenseGraph`` .

    .. SEEALSO::

        - :meth:`~sage.graphs.graph.Graph.orientations`
        - :meth:`~sage.graphs.orientations.strong_orientations_iterator`
        - :meth:`~sage.graphs.digraph_generators.DiGraphGenerators.nauty_directg`
        - :meth:`~sage.graphs.orientations.random_orientation`

    EXAMPLES:

    For a 2-regular graph, a strong orientation gives to each vertex an
    out-degree equal to 1::

        sage: g = graphs.CycleGraph(5)
        sage: g.strong_orientation().out_degree()
        [1, 1, 1, 1, 1]

    The Petersen Graph is 2-edge connected. It then has a strongly connected
    orientation::

        sage: g = graphs.PetersenGraph()
        sage: o = g.strong_orientation()
        sage: len(o.strongly_connected_components())
        1

    The same goes for the CubeGraph in any dimension::

        sage: all(len(graphs.CubeGraph(i).strong_orientation().strongly_connected_components()) == 1
        ....:     for i in range(2,6))
        True

    A multigraph also has a strong orientation::

        sage: g = Graph([(0, 1), (0, 2), (1, 2)] * 2, multiedges=True)
        sage: g.strong_orientation()
        Multi-digraph on 3 vertices
    """
def strong_orientations_iterator(G) -> Generator[Incomplete, Incomplete]:
    """
    Return an iterator over all strong orientations of a graph `G`.

    A strong orientation of a graph is an orientation of its edges such that the
    obtained digraph is strongly connected (i.e. there exist a directed path
    between each pair of vertices). According to Robbins' theorem (see the
    :wikipedia:`Robbins_theorem`), the graphs that have strong orientations are
    exactly the 2-edge-connected graphs (i.e., the bridgeless graphs).

    ALGORITHM:

    It is an adaptation of the algorithm published in [CGMRV16]_.
    It runs in `O(mn)` amortized time, where `m` is the number of edges and
    `n` is the number of vertices. The amortized time can be improved to `O(m)`
    with a more involved method.
    In this function, first the graph is preprocessed and a spanning tree is
    generated. Then every orientation of the non-tree edges of the graph can be
    extended to at least one new strong orientation by orienting properly
    the edges of the spanning tree (this property is proved in [CGMRV16]_).
    Therefore, this function generates all partial orientations of the non-tree
    edges and then launches a helper function corresponding to the generation
    algorithm described in [CGMRV16]_.
    In order to avoid trivial symmetries, the orientation of an arbitrary edge
    is fixed before the start of the enumeration process.

    INPUT:

    - ``G`` -- an undirected graph

    OUTPUT: an iterator which will produce all strong orientations of this graph

    .. NOTE::

        Works only for simple graphs (no multiple edges).
        To avoid symmetries an orientation of an arbitrary edge is fixed.

    .. SEEALSO::

        - :meth:`~Graph.orientations`
        - :meth:`~Graph.strong_orientation`
        - :meth:`~sage.graphs.digraph_generators.DiGraphGenerators.nauty_directg`
        - :meth:`~sage.graphs.orientations.random_orientation`

    EXAMPLES:

    A cycle has one possible (non-symmetric) strong orientation::

        sage: g = graphs.CycleGraph(4)
        sage: it = g.strong_orientations_iterator()
        sage: len(list(it))
        1

    A tree cannot be strongly oriented::

        sage: g = graphs.RandomTree(10)
        sage: len(list(g.strong_orientations_iterator()))
        0

    Neither can be a disconnected graph::

        sage: g = graphs.CompleteGraph(6)
        sage: g.add_vertex(7)
        sage: len(list(g.strong_orientations_iterator()))
        0

    TESTS:

        sage: g = graphs.CompleteGraph(2)
        sage: len(list(g.strong_orientations_iterator()))
        0

        sage: g = graphs.CubeGraph(3)
        sage: b = True
        sage: for orientedGraph in g.strong_orientations_iterator():
        ....:     if not orientedGraph.is_strongly_connected():
        ....:         b = False
        sage: b
        True

    The total number of strong orientations of a graph can be counted using
    the Tutte polynomial evaluated at points (0,2)::

        sage: g = graphs.PetersenGraph()
        sage: nr1 = len(list(g.strong_orientations_iterator()))
        sage: nr2 = g.tutte_polynomial()(0,2)
        sage: nr1 == nr2/2  # The Tutte polynomial counts also the symmetrical orientations
        True
    """
def random_orientation(G):
    """
    Return a random orientation of a graph `G`.

    An *orientation* of an undirected graph is a directed graph such that every
    edge is assigned a direction. Hence there are `2^m` oriented digraphs for a
    simple graph with `m` edges.

    INPUT:

    - ``G`` -- a Graph

    EXAMPLES::

        sage: from sage.graphs.orientations import random_orientation
        sage: G = graphs.PetersenGraph()
        sage: D = random_orientation(G)
        sage: D.order() == G.order(), D.size() == G.size()
        (True, True)

    TESTS:

    Giving anything else than a Graph::

        sage: random_orientation([])
        Traceback (most recent call last):
        ...
        ValueError: the input parameter must be a Graph

    .. SEEALSO::

        - :meth:`~Graph.orientations`
        - :meth:`~Graph.strong_orientation`
        - :meth:`~sage.graphs.orientations.strong_orientations_iterator`
        - :meth:`~sage.graphs.digraph_generators.DiGraphGenerators.nauty_directg`
    """
def minimum_outdegree_orientation(G, use_edge_labels: bool = False, solver=None, verbose: int = 0, *, integrality_tolerance: float = 0.001):
    """
    Return an orientation of `G` with the smallest possible maximum outdegree.

    Given a Graph `G`, it is polynomial to compute an orientation `D` of the
    edges of `G` such that the maximum out-degree in `D` is minimized. This
    problem, though, is NP-complete in the weighted case [AMOZ2006]_.

    INPUT:

    - ``G`` -- an undirected graph

    - ``use_edge_labels`` -- boolean (default: ``False``)

      - When set to ``True``, uses edge labels as weights to compute the
        orientation and assumes a weight of `1` when there is no value available
        for a given edge.

      - When set to ``False`` (default), gives a weight of 1 to all the edges.

    - ``solver`` -- string (default: ``None``); specifies a Mixed Integer Linear
      Programming (MILP) solver to be used. If set to ``None``, the default one
      is used. For more information on MILP solvers and which default solver is
      used, see the method :meth:`solve
      <sage.numerical.mip.MixedIntegerLinearProgram.solve>` of the class
      :class:`MixedIntegerLinearProgram
      <sage.numerical.mip.MixedIntegerLinearProgram>`.

    - ``verbose`` -- integer (default: 0); sets the level of verbosity. Set to 0
      by default, which means quiet.

    - ``integrality_tolerance`` -- float; parameter for use with MILP solvers
      over an inexact base ring;
      see :meth:`MixedIntegerLinearProgram.get_values`.

    EXAMPLES:

    Given a complete bipartite graph `K_{n,m}`, the maximum out-degree of an
    optimal orientation is `\\left\\lceil \\frac {nm} {n+m}\\right\\rceil`::

        sage: g = graphs.CompleteBipartiteGraph(3,4)
        sage: o = g.minimum_outdegree_orientation()                                     # needs sage.numerical.mip
        sage: max(o.out_degree()) == integer_ceil((4*3)/(3+4))                          # needs sage.numerical.mip
        True

    Show the influence of edge labels on the solution::

        sage: # needs sage.numerical.mip
        sage: g = graphs.PetersenGraph()
        sage: o = g.minimum_outdegree_orientation(use_edge_labels=False)
        sage: max(o.out_degree())
        2
        sage: _ = [g.set_edge_label(u, v, 1) for u, v in g.edge_iterator(labels=False)]
        sage: o = g.minimum_outdegree_orientation(use_edge_labels=True)
        sage: max(o.out_degree())
        2
        sage: g.set_edge_label(0, 1, 100)
        sage: o = g.minimum_outdegree_orientation(use_edge_labels=True)
        sage: max(o.out_degree())
        3

    TESTS::

        sage: from sage.graphs.orientations import minimum_outdegree_orientation
        sage: minimum_outdegree_orientation(DiGraph())                                  # needs sage.numerical.mip
        Traceback (most recent call last):
        ...
        ValueError: Cannot compute an orientation of a DiGraph.
         Please convert it to a Graph if you really mean it.
    """
def bounded_outdegree_orientation(G, bound, solver=None, verbose: bool = False, *, integrality_tolerance: float = 0.001):
    '''
    Return an orientation of `G` such that every vertex `v` has out-degree less
    than `b(v)`.

    INPUT:

    - ``G`` -- an undirected graph

    - ``bound`` -- maximum bound on the out-degree. Can be of three
      different types :

      * An integer `k`. In this case, computes an orientation whose maximum
        out-degree is less than `k`.

      * A dictionary associating to each vertex its associated maximum
        out-degree.

      * A function associating to each vertex its associated maximum
        out-degree.

    - ``solver`` -- string (default: ``None``); specifies a Mixed Integer Linear
      Programming (MILP) solver to be used. If set to ``None``, the default one
      is used. For more information on MILP solvers and which default solver is
      used, see the method :meth:`solve
      <sage.numerical.mip.MixedIntegerLinearProgram.solve>` of the class
      :class:`MixedIntegerLinearProgram
      <sage.numerical.mip.MixedIntegerLinearProgram>`.

    - ``verbose`` -- integer (default: 0); sets the level of verbosity. Set to 0
      by default, which means quiet.

    - ``integrality_tolerance`` -- float; parameter for use with MILP solvers
      over an inexact base ring;
      see :meth:`MixedIntegerLinearProgram.get_values`.

    OUTPUT:

    A DiGraph representing the orientation if it exists.
    A :exc:`ValueError` exception is raised otherwise.

    ALGORITHM:

    The problem is solved through a maximum flow :

    Given a graph `G`, we create a ``DiGraph`` `D` defined on `E(G)\\cup V(G)\\cup
    \\{s,t\\}`. We then link `s` to all of `V(G)` (these edges having a capacity
    equal to the bound associated to each element of `V(G)`), and all the
    elements of `E(G)` to `t` . We then link each `v \\in V(G)` to each of its
    incident edges in `G`. A maximum integer flow of value `|E(G)|` corresponds
    to an admissible orientation of `G`. Otherwise, none exists.

    EXAMPLES:

    There is always an orientation of a graph `G` such that a vertex `v` has
    out-degree at most `\\lceil \\frac {d(v)} 2 \\rceil`::

        sage: g = graphs.RandomGNP(40, .4)
        sage: b = lambda v: integer_ceil(g.degree(v)/2)
        sage: D = g.bounded_outdegree_orientation(b)
        sage: all(D.out_degree(v) <= b(v) for v in g)
        True

    Chvatal\'s graph, being 4-regular, can be oriented in such a way that its
    maximum out-degree is 2::

        sage: g = graphs.ChvatalGraph()
        sage: D = g.bounded_outdegree_orientation(2)
        sage: max(D.out_degree())
        2

    For any graph `G`, it is possible to compute an orientation such that
    the maximum out-degree is at most the maximum average degree of `G`
    divided by 2. Anything less, though, is impossible.

        sage: g = graphs.RandomGNP(40, .4)
        sage: mad = g.maximum_average_degree()                                      # needs sage.numerical.mip

    Hence this is possible ::

        sage: d = g.bounded_outdegree_orientation(integer_ceil(mad/2))              # needs sage.numerical.mip

    While this is not::

        sage: try:                                                                  # needs sage.numerical.mip
        ....:     g.bounded_outdegree_orientation(integer_ceil(mad/2-1))
        ....:     print("Error")
        ....: except ValueError:
        ....:     pass

    The bounds can be specified in different ways::

        sage: g = graphs.PetersenGraph()
        sage: b = lambda v: integer_ceil(g.degree(v)/2)
        sage: D = g.bounded_outdegree_orientation(b)
        sage: b_dict = {u: b(u) for u in g}
        sage: D = g.bounded_outdegree_orientation(b_dict)
        sage: unique_bound = 2
        sage: D = g.bounded_outdegree_orientation(unique_bound)

    TESTS:

    As previously for random graphs, but more intensively::

        sage: for i in range(30):      # long time (up to 6s on sage.math, 2012)
        ....:     g = graphs.RandomGNP(40, .4)
        ....:     b = lambda v: integer_ceil(g.degree(v)/2)
        ....:     D = g.bounded_outdegree_orientation(b)
        ....:     if not (
        ....:          all( D.out_degree(v) <= b(v) for v in g ) or
        ....:          D.size() != g.size()):
        ....:         print("Something wrong happened")

    Empty graph::

        sage: Graph().bounded_outdegree_orientation(b)
        Digraph on 0 vertices
    '''
def eulerian_orientation(G):
    """
    Return an Eulerian orientation of the graph `G`.

    An Eulerian graph being a graph such that any vertex has an even degree, an
    Eulerian orientation of a graph is an orientation of its edges such that
    each vertex `v` verifies `d^+(v)=d^-(v)=d(v)/2`, where `d^+` and `d^-`
    respectively represent the out-degree and the in-degree of a vertex.

    If the graph is not Eulerian, the orientation verifies for any vertex `v`
    that `| d^+(v)-d^-(v) | \\leq 1`.

    INPUT:

    - ``G`` -- an undirected graph

    ALGORITHM:

    This algorithm is a random walk through the edges of the graph, which
    orients the edges according to the walk. When a vertex is reached which has
    no non-oriented edge (this vertex must have odd degree), the walk resumes at
    another vertex of odd degree, if any.

    This algorithm has time complexity in `O(n+m)` for ``SparseGraph`` and
    `O(n^2)` for ``DenseGraph``, where `m` is the number of edges in the graph
    and `n` is the number of vertices in the graph.

    EXAMPLES:

    The CubeGraph with parameter 4, which is regular of even degree, has an
    Eulerian orientation such that `d^+ = d^-`::

        sage: g = graphs.CubeGraph(4)
        sage: g.degree()
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
        sage: o = g.eulerian_orientation()
        sage: o.in_degree()
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        sage: o.out_degree()
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

    Secondly, the Petersen Graph, which is 3 regular has an orientation such
    that the difference between `d^+` and `d^-` is at most 1::

        sage: g = graphs.PetersenGraph()
        sage: o = g.eulerian_orientation()
        sage: o.in_degree()
        [2, 2, 2, 2, 2, 1, 1, 1, 1, 1]
        sage: o.out_degree()
        [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]

    TESTS::

        sage: E0 = Graph(); E4 = Graph(4)  # See trac #21741
        sage: E0.eulerian_orientation()
        Digraph on 0 vertices
        sage: E4.eulerian_orientation()
        Digraph on 4 vertices
    """
