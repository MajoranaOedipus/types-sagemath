from _typeshed import Incomplete
from collections.abc import Generator
from sage.graphs.views import EdgesView as EdgesView
from sage.rings.integer import Integer as Integer

def has_perfect_matching(G, algorithm: str = 'Edmonds', solver=None, verbose: int = 0, *, integrality_tolerance: float = 0.001):
    '''
    Return whether the graph has a perfect matching.

    INPUT:

    - ``algorithm`` -- string (default: ``\'Edmonds\'``)

      - ``\'Edmonds\'`` uses Edmonds\' algorithm as implemented in NetworkX to
        find a matching of maximal cardinality, then check whether this
        cardinality is half the number of vertices of the graph.

      - ``\'LP_matching\'`` uses a Linear Program to find a matching of
        maximal cardinality, then check whether this cardinality is half the
        number of vertices of the graph.

      - ``\'LP\'`` uses a Linear Program formulation of the perfect matching
        problem: put a binary variable ``b[e]`` on each edge `e`, and for
        each vertex `v`, require that the sum of the values of the edges
        incident to `v` is 1.

    - ``solver`` -- string (default: ``None``); specifies a Mixed Integer
      Linear Programming (MILP) solver to be used. If set to ``None``, the
      default one is used. For more information on MILP solvers and which
      default solver is used, see the method :meth:`solve
      <sage.numerical.mip.MixedIntegerLinearProgram.solve>` of the class
      :class:`MixedIntegerLinearProgram
      <sage.numerical.mip.MixedIntegerLinearProgram>`.

    - ``verbose`` -- integer (default: 0); sets the level of verbosity:
      set to 0 by default, which means quiet (only useful when
      ``algorithm == "LP_matching"`` or ``algorithm == "LP"``)

    - ``integrality_tolerance`` -- float; parameter for use with MILP
      solvers over an inexact base ring; see
      :meth:`MixedIntegerLinearProgram.get_values`.

    OUTPUT: boolean

    EXAMPLES::

        sage: graphs.PetersenGraph().has_perfect_matching()                         # needs networkx
        True
        sage: graphs.WheelGraph(6).has_perfect_matching()                           # needs networkx
        True
        sage: graphs.WheelGraph(5).has_perfect_matching()                           # needs networkx
        False
        sage: graphs.PetersenGraph().has_perfect_matching(algorithm=\'LP_matching\')  # needs sage.numerical.mip
        True
        sage: graphs.WheelGraph(6).has_perfect_matching(algorithm=\'LP_matching\')    # needs sage.numerical.mip
        True
        sage: graphs.WheelGraph(5).has_perfect_matching(algorithm=\'LP_matching\')
        False
        sage: graphs.PetersenGraph().has_perfect_matching(algorithm=\'LP_matching\')  # needs sage.numerical.mip
        True
        sage: graphs.WheelGraph(6).has_perfect_matching(algorithm=\'LP_matching\')    # needs sage.numerical.mip
        True
        sage: graphs.WheelGraph(5).has_perfect_matching(algorithm=\'LP_matching\')
        False

    TESTS::

        sage: G = graphs.EmptyGraph()
        sage: all(G.has_perfect_matching(algorithm=algo)                            # needs networkx
        ....:     for algo in [\'Edmonds\', \'LP_matching\', \'LP\'])
        True

    Be careful with isolated vertices::

        sage: G = graphs.PetersenGraph()
        sage: G.add_vertex(11)
        sage: any(G.has_perfect_matching(algorithm=algo)                            # needs networkx
        ....:     for algo in [\'Edmonds\', \'LP_matching\', \'LP\'])
        False
    '''
def is_bicritical(G, matching=None, algorithm: str = 'Edmonds', coNP_certificate: bool = False, solver=None, verbose: int = 0, *, integrality_tolerance: float = 0.001):
    """
    Check if the graph is bicritical.

    A nontrivial graph `G` is *bicritical* if `G - u - v` has a perfect
    matching for any two distinct vertices `u` and `v` of `G`. Bicritical
    graphs are special kind of matching covered graphs. Each maximal barrier of
    a bicritical graph is a singleton. Thus, for a bicritical graph, the
    canonical partition of the vertex set is the set of sets where each set is
    an individual vertex. Three-connected bicritical graphs, aka *bricks*, play
    an important role in the theory of matching covered graphs.

    This method implements the algorithm proposed in [LZ2001]_ and we
    assume that a connected graph of order two is bicritical, whereas a
    disconnected graph of the same order is not. The time complexity of
    the algorithm is `\\mathcal{O}(|V| \\cdot |E|)`, if a perfect matching of
    the graph is given, where `|V|` and `|E|` are the order and the size of
    the graph respectively. Otherwise, time complexity may be dominated by
    the time needed to compute a maximum matching of the graph.

    Note that a :class:`ValueError` is returned if the graph has loops or if
    the graph is trivial, i.e., it has at most one vertex.

    INPUT:

    - ``matching`` -- (default: ``None``); a perfect matching of the
      graph, that can be given using any valid input format of
      :class:`~sage.graphs.graph.Graph`.

      If set to ``None``, a matching is computed using the other parameters.

    - ``algorithm`` -- string (default: ``'Edmonds'``); the algorithm to be
      used to compute a maximum matching of the graph among

      - ``'Edmonds'`` selects Edmonds' algorithm as implemented in NetworkX,

      - ``'LP'`` uses a Linear Program formulation of the matching problem.

    - ``coNP_certificate`` -- boolean (default: ``False``); if set to
      ``True`` a set of pair of vertices (say `u` and `v`) is returned such
      that `G - u - v` does not have a perfect matching if `G` is not
      bicritical or otherwise ``None`` is returned.

    - ``solver`` -- string (default: ``None``); specify a Mixed Integer
      Linear Programming (MILP) solver to be used. If set to ``None``, the
      default one is used. For more information on MILP solvers and which
      default solver is used, see the method :meth:`solve
      <sage.numerical.mip.MixedIntegerLinearProgram.solve>` of the class
      :class:`MixedIntegerLinearProgram
      <sage.numerical.mip.MixedIntegerLinearProgram>`.

    - ``verbose`` -- integer (default: ``0``); sets the level of verbosity:
      set to 0 by default, which means quiet (only useful when ``algorithm
      == 'LP'``).

    - ``integrality_tolerance`` -- float; parameter for use with MILP
      solvers over an inexact base ring; see
      :meth:`MixedIntegerLinearProgram.get_values`.

    OUTPUT:

    - A boolean indicating whether the graph is bicritical or not.

    - If ``coNP_certificate`` is set to ``True``, a set of pair of vertices
      is returned in case the graph is not bicritical otherwise ``None`` is
      returned.

    EXAMPLES:

    The Petersen graph is bicritical::

        sage: G = graphs.PetersenGraph()
        sage: G.is_bicritical()
        True

    A graph (without a self-loop) is bicritical if and only if the underlying
    simple graph is bicritical::

        sage: G = graphs.PetersenGraph()
        sage: G.allow_multiple_edges(True)
        sage: G.add_edge(0, 5)
        sage: G.is_bicritical()
        True

    A nontrivial circular ladder graph whose order is not divisible by 4 is bicritical::

        sage: G = graphs.CircularLadderGraph(5)
        sage: G.is_bicritical()
        True

    The graph obtained by splicing two bicritical graph is also bicritical.
    For instance, `K_4` with one extra (multiple) edge (say `G := K_4^+`) is
    bicritical. Let `H := K_4^+ \\odot K_4^+` such that `H` is free of multiple
    edge. The graph `H` is also bicritical::

        sage: G = graphs.CompleteGraph(4)
        sage: G.allow_multiple_edges(True)
        sage: G.add_edge(0, 1)
        sage: G.is_bicritical()
        True
        sage: H = Graph()
        sage: H.add_edges([
        ....:    (0, 1), (0, 2), (0, 3), (0, 4), (1, 2),
        ....:    (1, 5), (2, 5), (3, 4), (3, 5), (4, 5)
        ....: ])
        sage: H.is_bicritical()
        True

    A graph (of order more than two) with more that one component is not bicritical::

        sage: G = graphs.CycleGraph(4)
        sage: G += graphs.CycleGraph(6)
        sage: G.connected_components_number()
        2
        sage: G.is_bicritical()
        False

    A graph (of order more than two) with a cut-vertex is not bicritical::

        sage: G = graphs.CycleGraph(6)
        sage: G.add_edges([(5, 6), (5, 7), (6, 7)])
        sage: G.is_cut_vertex(5)
        True
        sage: G.has_perfect_matching()
        True
        sage: G.is_bicritical()
        False

    A connected graph of order two is assumed to be bicritical, whereas the
    disconnected graph of the same order is not::

        sage: G = graphs.CompleteBipartiteGraph(1, 1)
        sage: G.is_bicritical()
        True
        sage: G = graphs.CompleteBipartiteGraph(2, 0)
        sage: G.is_bicritical()
        False

    A bipartite graph of order three or more is not bicritical::

        sage: G = graphs.CompleteBipartiteGraph(3, 3)
        sage: G.has_perfect_matching()
        True
        sage: G.is_bicritical()
        False

    One may specify a matching::

        sage: G = graphs.WheelGraph(10)
        sage: M = G.matching()
        sage: G.is_bicritical(matching=M)
        True
        sage: H = graphs.HexahedralGraph()
        sage: N = H.matching()
        sage: H.is_bicritical(matching=N)
        False

    One may ask for a co-`\\mathcal{NP}` certificate::

        sage: G = graphs.CompleteGraph(14)
        sage: G.is_bicritical(coNP_certificate=True)
        (True, None)
        sage: H = graphs.CircularLadderGraph(20)
        sage: M = H.matching()
        sage: H.is_bicritical(matching=M, coNP_certificate=True)
        (False, {0, 2})

    TESTS:

    If the graph is trivial::

        sage: G = Graph()
        sage: G.is_bicritical()
        Traceback (most recent call last):
        ...
        ValueError: the graph is trivial
        sage: H = graphs.CycleGraph(1)
        sage: H.is_bicritical()
        Traceback (most recent call last):
        ...
        ValueError: the graph is trivial

    Providing with a wrong matching::

        sage: G = graphs.CompleteGraph(6)
        sage: M = Graph(G.matching())
        sage: M.add_edges([(0, 1), (0, 2)])
        sage: G.is_bicritical(matching=M)
        Traceback (most recent call last):
        ...
        ValueError: the input is not a matching
        sage: N = Graph(G.matching())
        sage: N.add_edge(6, 7)
        sage: G.is_bicritical(matching=N)
        Traceback (most recent call last):
        ...
        ValueError: the input is not a matching of the graph
        sage: J = Graph()
        sage: J.add_edges([(0, 1), (2, 3)])
        sage: G.is_bicritical(matching=J)
        Traceback (most recent call last):
        ...
        ValueError: the input is not a perfect matching of the graph

    Providing with a graph with a self-loop::

        sage: G = graphs.CompleteGraph(4)
        sage: G.allow_loops(True)
        sage: G.add_edge(0, 0)
        sage: G.is_bicritical()
        Traceback (most recent call last):
        ...
        ValueError: This method is not known to work on graphs with loops.
        Perhaps this method can be updated to handle them, but in the meantime
        if you want to use it please disallow loops using allow_loops().

    REFERENCES:

    - [LM2024]_

    - [LZ2001]_

    .. SEEALSO::
        :meth:`~sage.graphs.graph.Graph.is_factor_critical`,
        :meth:`~sage.graphs.graph.Graph.is_matching_covered`

    AUTHORS:

    - Janmenjaya Panda (2024-06-17)
    """
def is_factor_critical(G, matching=None, algorithm: str = 'Edmonds', solver=None, verbose: int = 0, *, integrality_tolerance: float = 0.001):
    '''
    Check whether the graph is factor-critical.

    A graph of order `n` is *factor-critical* if every subgraph of `n-1`
    vertices have a perfect matching, hence `n` must be odd. See
    :wikipedia:`Factor-critical_graph` for more details.

    This method implements the algorithm proposed in [LR2004]_ and we assume
    that a graph of order one is factor-critical. The time complexity of the
    algorithm is linear if a near perfect matching is given as input (i.e.,
    a matching such that all vertices but one are incident to an edge of the
    matching). Otherwise, the time complexity is dominated by the time
    needed to compute a maximum matching of the graph.

    INPUT:

    - ``matching`` -- (default: ``None``); a near perfect matching of the
      graph, that is a matching such that all vertices of the graph but one
      are incident to an edge of the matching. It can be given using any
      valid input format of :class:`~sage.graphs.graph.Graph`.

      If set to ``None``, a matching is computed using the other parameters.

    - ``algorithm`` -- string (default: ``\'Edmonds\'``); the algorithm to use
      to compute a maximum matching of the graph among

      - ``\'Edmonds\'`` selects Edmonds\' algorithm as implemented in NetworkX

      - ``\'LP\'`` uses a Linear Program formulation of the matching problem

    - ``solver`` -- string (default: ``None``); specifies a Mixed Integer
      Linear Programming (MILP) solver to be used. If set to ``None``, the
      default one is used. For more information on MILP solvers and which
      default solver is used, see the method :meth:`solve
      <sage.numerical.mip.MixedIntegerLinearProgram.solve>` of the class
      :class:`MixedIntegerLinearProgram
      <sage.numerical.mip.MixedIntegerLinearProgram>`.

    - ``verbose`` -- integer (default: 0); sets the level of verbosity:
      set to 0 by default, which means quiet (only useful when ``algorithm
      == "LP"``)

    - ``integrality_tolerance`` -- float; parameter for use with MILP
      solvers over an inexact base ring; see
      :meth:`MixedIntegerLinearProgram.get_values`.

    EXAMPLES:

    Odd length cycles and odd cliques of order at least 3 are
    factor-critical graphs::

        sage: [graphs.CycleGraph(2*i + 1).is_factor_critical() for i in range(5)]   # needs networkx
        [True, True, True, True, True]
        sage: [graphs.CompleteGraph(2*i + 1).is_factor_critical() for i in range(5)]            # needs networkx
        [True, True, True, True, True]

    More generally, every Hamiltonian graph with an odd number of vertices
    is factor-critical::

        sage: G = graphs.RandomGNP(15, .2)
        sage: G.add_path([0..14])
        sage: G.add_edge(14, 0)
        sage: G.is_hamiltonian()
        True
        sage: G.is_factor_critical()                                                # needs networkx
        True

    Friendship graphs are non-Hamiltonian factor-critical graphs::

        sage: all(graphs.FriendshipGraph(i).is_factor_critical() for i in range(1, 5))             # needs networkx
        True

    Bipartite graphs are not factor-critical::

        sage: G = graphs.RandomBipartite(randint(1, 10), randint(1, 10), .5)        # needs numpy
        sage: G.is_factor_critical()                                                # needs numpy
        False

    Graphs with even order are not factor critical::

        sage: G = graphs.RandomGNP(10, .5)
        sage: G.is_factor_critical()
        False

    One can specify a matching::

        sage: F = graphs.FriendshipGraph(4)
        sage: M = F.matching()                                                      # needs networkx
        sage: F.is_factor_critical(matching=M)                                      # needs networkx
        True
        sage: F.is_factor_critical(matching=Graph(M))                               # needs networkx
        True

    TESTS:

    Giving a wrong matching::

        sage: G = graphs.RandomGNP(15, .3)
        sage: while not G.is_biconnected():
        ....:     G = graphs.RandomGNP(15, .3)
        sage: M = G.matching()                                                      # needs networkx
        sage: G.is_factor_critical(matching=M[:-1])                                 # needs networkx
        Traceback (most recent call last):
        ...
        ValueError: the input is not a near perfect matching of the graph
        sage: G.is_factor_critical(matching=G.edges(sort=True))
        Traceback (most recent call last):
        ...
        ValueError: the input is not a matching
        sage: M = [(2*i, 2*i + 1) for i in range(9)]
        sage: G.is_factor_critical(matching=M)
        Traceback (most recent call last):
        ...
        ValueError: the input is not a matching of the graph
    '''
def is_matching_covered(G, matching=None, algorithm: str = 'Edmonds', coNP_certificate: bool = False, solver=None, verbose: int = 0, *, integrality_tolerance: float = 0.001):
    """
    Check if the graph is matching covered.

    A connected nontrivial graph wherein each edge participates in some
    perfect matching is called a *matching* *covered* *graph*.

    If a perfect matching of the graph is provided, for bipartite graph,
    this method implements a linear time algorithm as proposed in [LM2024]_
    that is based on the following theorem:

    Given a connected bipartite graph `G[A, B]` with a perfect matching
    `M`. Construct a directed graph `D` from `G` such that `V(D) := V(G)`
    and for each edge in `G` direct the corresponding edge from `A` to `B`
    in `D`, if it is in `M` or otherwise direct it from `B` to `A`. The
    graph `G` is matching covered if and only if `D` is strongly connected.

    For nonbipartite graph, if a perfect matching of the graph is provided,
    this method implements an `\\mathcal{O}(|V| \\cdot |E|)` algorithm, where
    `|V|` and `|E|` are the order and the size of the graph respectively.
    This implementation is inspired by the `M`-`alternating` `tree` `search`
    method explained in [LZ2001]_. For nonbipartite graph, the
    implementation is based on the following theorem:

    Given a nonbipartite graph `G` with a perfect matching `M`. The
    graph `G` is matching covered if and only if for each edge `uv`
    not in `M`, there exists an `M`-`alternating` odd length `uv`-path
    starting and ending with edges not in `M`.

    The time complexity may be dominated by the time needed to compute a
    maximum matching of the graph, in case a perfect matching is not
    provided. Also, note that for a disconnected or a trivial or a
    graph with a loop, a :class:`ValueError` is returned.

    INPUT:

    - ``matching`` -- (default: ``None``); a perfect matching of the
      graph, that can be given using any valid input format of
      :class:`~sage.graphs.graph.Graph`.

      If set to ``None``, a matching is computed using the other parameters.

    - ``algorithm`` -- string (default: ``'Edmonds'``); the algorithm to be
      used to compute a maximum matching of the graph among

      - ``'Edmonds'`` selects Edmonds' algorithm as implemented in NetworkX,

      - ``'LP'`` uses a Linear Program formulation of the matching problem.

    - ``coNP_certificate`` -- boolean (default: ``False``); if set to
      ``True`` an edge of the graph, that does not participate in any
      perfect matching, is returned if `G` is not matching covered or
      otherwise ``None`` is returned.

    - ``solver`` -- string (default: ``None``); specify a Mixed Integer
      Linear Programming (MILP) solver to be used. If set to ``None``, the
      default one is used. For more information on MILP solvers and which
      default solver is used, see the method :meth:`solve
      <sage.numerical.mip.MixedIntegerLinearProgram.solve>` of the class
      :class:`MixedIntegerLinearProgram
      <sage.numerical.mip.MixedIntegerLinearProgram>`.

    - ``verbose`` -- integer (default: ``0``); sets the level of verbosity:
      set to 0 by default, which means quiet (only useful when ``algorithm
      == 'LP'``).

    - ``integrality_tolerance`` -- float; parameter for use with MILP
      solvers over an inexact base ring; see
      :meth:`MixedIntegerLinearProgram.get_values`.

    OUTPUT:

    - A boolean indicating whether the graph is matching covered or not.

    - If ``coNP_certificate`` is set to ``True``, an edge is returned in
      case the graph is not matching covered otherwise ``None`` is
      returned.

    EXAMPLES:

    The Petersen graph is matching covered::

        sage: G = graphs.PetersenGraph()
        sage: G.is_matching_covered()
        True

    A graph (without a self-loop) is matching covered if and only if the
    underlying simple graph is matching covered::

        sage: G = graphs.PetersenGraph()
        sage: G.allow_multiple_edges(True)
        sage: G.add_edge(0, 5)
        sage: G.is_matching_covered()
        True

    A corollary to Tutte's fundamental result [Tut1947]_, as a
    strengthening of Petersen's Theorem, states that every 2-connected
    cubic graph is matching covered::

        sage: G = Graph()
        sage: G.add_edges([
        ....:    (0, 1), (0, 2), (0, 3),
        ....:    (1, 2), (1, 4), (2, 4),
        ....:    (3, 5), (3, 6), (4, 7),
        ....:    (5, 6), (5, 7), (6, 7)
        ....: ])
        sage: G.vertex_connectivity()
        2
        sage: degree_sequence = G.degree_sequence()
        sage: min(degree_sequence) == max(degree_sequence) == 3
        True
        sage: G.is_matching_covered()
        True

    A connected bipartite graph `G[A, B]`, with `|A| = |B| \\geq 2`, is
    matching covered if and only if `|N(X)| \\geq |X| + 1`, for all
    `X \\subset A` such that `1 \\leq |X| \\leq |A| - 1`. For instance,
    the Hexahedral graph is matching covered, but not the path graphs on
    even number of vertices, even though they have a perfect matching::

        sage: G = graphs.HexahedralGraph()
        sage: G.is_bipartite()
        True
        sage: G.is_matching_covered()
        True
        sage: P = graphs.PathGraph(10)
        sage: P.is_bipartite()
        True
        sage: M = Graph(P.matching())
        sage: set(P) == set(M)
        True
        sage: P.is_matching_covered()
        False

    A connected bipartite graph `G[A, B]` of order six or more is matching
    covered if and only if `G - a - b` has a perfect matching for some
    vertex `a` in `A` and some vertex `b` in `B`::

        sage: G = graphs.CircularLadderGraph(8)
        sage: G.is_bipartite()
        True
        sage: G.is_matching_covered()
        True
        sage: A, B = G.bipartite_sets()
        sage: # needs random
        sage: import random
        sage: a = random.choice(list(A))
        sage: b = random.choice(list(B))
        sage: G.delete_vertices([a, b])
        sage: M = Graph(G.matching())
        sage: set(M) == set(G)
        True
        sage: cycle1 = graphs.CycleGraph(4)
        sage: cycle2 = graphs.CycleGraph(6)
        sage: cycle2.relabel(lambda v: v + 4)
        sage: H = Graph()
        sage: H.add_edges(cycle1.edges() + cycle2.edges())
        sage: H.add_edge(3, 4)
        sage: H.is_bipartite()
        True
        sage: H.is_matching_covered()
        False
        sage: H.delete_vertices([3, 4])
        sage: N = Graph(H.matching())
        sage: set(N) == set(H)
        False

    One may specify a matching::

        sage: G = graphs.WheelGraph(20)
        sage: M = Graph(G.matching())
        sage: G.is_matching_covered(matching=M)
        True
        sage: J = graphs.CycleGraph(4)
        sage: J.add_edge(0, 2)
        sage: N = J.matching()
        sage: J.is_matching_covered(matching=N)
        False

    One may ask for a co-`\\mathcal{NP}` certificate::

        sage: G = graphs.CompleteGraph(14)
        sage: G.is_matching_covered(coNP_certificate=True)
        (True, None)
        sage: H = graphs.PathGraph(20)
        sage: M = H.matching()
        sage: H.is_matching_covered(matching=M, coNP_certificate=True)
        (False, (2, 1, None))

    TESTS:

    If the graph is not connected::

        sage: cycle1 = graphs.CycleGraph(4)
        sage: cycle2 = graphs.CycleGraph(6)
        sage: cycle2.relabel(lambda v: v + 4)
        sage: G = Graph()
        sage: G.add_edges(cycle1.edges() + cycle2.edges())
        sage: len(G.connected_components(sort=False))
        2
        sage: G.is_matching_covered()
        Traceback (most recent call last):
        ...
        ValueError: the graph is not connected

    If the graph is trivial::

        sage: G = Graph()
        sage: G.is_matching_covered()
        Traceback (most recent call last):
        ...
        ValueError: the graph is trivial
        sage: H = graphs.CycleGraph(1)
        sage: H.is_matching_covered()
        Traceback (most recent call last):
        ...
        ValueError: the graph is trivial

    Providing with a wrong matching::

        sage: G = graphs.CompleteGraph(6)
        sage: M = Graph(G.matching())
        sage: M.add_edges([(0, 1), (0, 2)])
        sage: G.is_matching_covered(matching=M)
        Traceback (most recent call last):
        ...
        ValueError: the input is not a matching
        sage: N = Graph(G.matching())
        sage: N.add_edge(6, 7)
        sage: G.is_matching_covered(matching=N)
        Traceback (most recent call last):
        ...
        ValueError: the input is not a matching of the graph
        sage: J = Graph()
        sage: J.add_edges([(0, 1), (2, 3)])
        sage: G.is_matching_covered(matching=J)
        Traceback (most recent call last):
        ...
        ValueError: the input is not a perfect matching of the graph

    Providing with a graph with a self-loop::

        sage: G = graphs.PetersenGraph()
        sage: G.allow_loops(True)
        sage: G.add_edge(0, 0)
        sage: G.is_matching_covered()
        Traceback (most recent call last):
        ...
        ValueError: This method is not known to work on graphs with loops.
        Perhaps this method can be updated to handle them, but in the meantime
        if you want to use it please disallow loops using allow_loops().

    REFERENCES:

    - [LM2024]_

    - [LZ2001]_

    - [Tut1947]_

    .. SEEALSO::
        :meth:`~sage.graphs.graph.Graph.is_factor_critical`,
        :meth:`~sage.graphs.graph.Graph.is_bicritical`

    AUTHORS:

    - Janmenjaya Panda (2024-06-23)
    """
def matching(G, value_only: bool = False, algorithm: str = 'Edmonds', use_edge_labels: bool = False, solver=None, verbose: int = 0, *, integrality_tolerance: float = 0.001):
    '''
    Return a maximum weighted matching of the graph represented by the list
    of its edges.

    For more information, see the :wikipedia:`Matching_(graph_theory)`.

    Given a graph `G` such that each edge `e` has a weight `w_e`, a maximum
    matching is a subset `S` of the edges of `G` of maximum weight such that
    no two edges of `S` are incident with each other.

    As an optimization problem, it can be expressed as:

    .. MATH::

        \\mbox{Maximize : }&\\sum_{e\\in G.edges()} w_e b_e\\\\\n        \\mbox{Such that : }&\\forall v \\in G,
        \\sum_{(u,v)\\in G.edges()} b_{(u,v)}\\leq 1\\\\\n        &\\forall x\\in G, b_x\\mbox{ is a binary variable}

    INPUT:

    - ``value_only`` -- boolean (default: ``False``); when set to ``True``,
      only the cardinal (or the weight) of the matching is returned

    - ``algorithm`` -- string (default: ``\'Edmonds\'``)

      - ``\'Edmonds\'`` selects Edmonds\' algorithm as implemented in NetworkX

      - ``\'LP\'`` uses a Linear Program formulation of the matching problem

    - ``use_edge_labels`` -- boolean (default: ``False``)

      - when set to ``True``, computes a weighted matching where each edge
        is weighted by its label (if an edge has no label, `1` is assumed)

      - when set to ``False``, each edge has weight `1`

    - ``solver`` -- string (default: ``None``); specifies a Mixed Integer
      Linear Programming (MILP) solver to be used. If set to ``None``, the
      default one is used. For more information on MILP solvers and which
      default solver is used, see the method :meth:`solve
      <sage.numerical.mip.MixedIntegerLinearProgram.solve>` of the class
      :class:`MixedIntegerLinearProgram
      <sage.numerical.mip.MixedIntegerLinearProgram>`.

    - ``verbose`` -- integer (default: 0); sets the level of verbosity:
      set to 0 by default, which means quiet (only useful when ``algorithm
      == "LP"``)

    - ``integrality_tolerance`` -- float; parameter for use with MILP
      solvers over an inexact base ring; see
      :meth:`MixedIntegerLinearProgram.get_values`.

    OUTPUT:

    - When ``value_only=False`` (default), this method returns an
      :class:`EdgesView` containing the edges of a maximum matching of `G`.

    - When ``value_only=True``, this method returns the sum of the
      weights (default: ``1``) of the edges of a maximum matching of `G`.
      The type of the output may vary according to the type of the edge
      labels and the algorithm used.

    ALGORITHM:

    The problem is solved using Edmond\'s algorithm implemented in NetworkX,
    or using Linear Programming depending on the value of ``algorithm``.

    EXAMPLES:

    Maximum matching in a Pappus Graph::

        sage: g = graphs.PappusGraph()
        sage: g.matching(value_only=True)                                            # needs sage.networkx
        9

    Same test with the Linear Program formulation::

        sage: g = graphs.PappusGraph()
        sage: g.matching(algorithm=\'LP\', value_only=True)                            # needs sage.numerical.mip
        9

    .. PLOT::

        g = graphs.PappusGraph()
        sphinx_plot(g.plot(edge_colors={"red":g.matching()}))

    TESTS:

    When ``use_edge_labels`` is set to ``False``, with Edmonds\' algorithm
    and LP formulation::

        sage: g = Graph([(0,1,0), (1,2,999), (2,3,-5)])
        sage: sorted(g.matching())                                                  # needs sage.networkx
        [(0, 1, 0), (2, 3, -5)]
        sage: sorted(g.matching(algorithm=\'LP\'))                                    # needs sage.numerical.mip
        [(0, 1, 0), (2, 3, -5)]

    When ``use_edge_labels`` is set to ``True``, with Edmonds\' algorithm and
    LP formulation::

        sage: g = Graph([(0,1,0), (1,2,999), (2,3,-5)])
        sage: g.matching(use_edge_labels=True)                                      # needs sage.networkx
        [(1, 2, 999)]
        sage: g.matching(algorithm=\'LP\', use_edge_labels=True)                      # needs sage.numerical.mip
        [(1, 2, 999)]

    With loops and multiedges::

        sage: edge_list = [(0,0,5), (0,1,1), (0,2,2), (0,3,3), (1,2,6)
        ....: , (1,2,3), (1,3,3), (2,3,3)]
        sage: g = Graph(edge_list, loops=True, multiedges=True)
        sage: m = g.matching(use_edge_labels=True)                                  # needs sage.networkx
        sage: type(m)                                                               # needs sage.networkx
        <class \'sage.graphs.views.EdgesView\'>
        sage: sorted(m)                                                             # needs sage.networkx
        [(0, 3, 3), (1, 2, 6)]

    TESTS:

    If ``algorithm`` is set to anything different from ``\'Edmonds\'`` or
    ``\'LP\'``, an exception is raised::

        sage: g = graphs.PappusGraph()
        sage: g.matching(algorithm=\'somethingdifferent\')
        Traceback (most recent call last):
        ...
        ValueError: algorithm must be set to either "Edmonds" or "LP"
    '''
def perfect_matchings(G, labels: bool = False) -> Generator[Incomplete, Incomplete]:
    """
    Return an iterator over all perfect matchings of the graph.

    ALGORITHM:

    Choose a vertex `v`, then recurse through all edges incident to `v`,
    removing one edge at a time whenever an edge is added to a matching.

    INPUT:

    - ``labels`` -- boolean (default: ``False``); when ``True``, the edges
      in each perfect matching are triples (containing the label as the
      third element), otherwise the edges are pairs.

    .. SEEALSO::

        :meth:`matching`

    EXAMPLES::

        sage: G=graphs.GridGraph([2,3])
        sage: for m in G.perfect_matchings():
        ....:     print(sorted(m))
        [((0, 0), (0, 1)), ((0, 2), (1, 2)), ((1, 0), (1, 1))]
        [((0, 0), (1, 0)), ((0, 1), (0, 2)), ((1, 1), (1, 2))]
        [((0, 0), (1, 0)), ((0, 1), (1, 1)), ((0, 2), (1, 2))]

        sage: G = graphs.CompleteGraph(4)
        sage: for m in G.perfect_matchings(labels=True):
        ....:     print(sorted(m))
        [(0, 1, None), (2, 3, None)]
        [(0, 2, None), (1, 3, None)]
        [(0, 3, None), (1, 2, None)]

        sage: G = Graph([[1,-1,'a'], [2,-2, 'b'], [1,-2,'x'], [2,-1,'y']])
        sage: sorted(sorted(m) for m in G.perfect_matchings(labels=True))
        [[(-2, 1, 'x'), (-1, 2, 'y')], [(-2, 2, 'b'), (-1, 1, 'a')]]

        sage: G = graphs.CompleteGraph(8)
        sage: mpc = G.matching_polynomial().coefficients(sparse=False)[0]           # needs sage.libs.flint
        sage: len(list(G.perfect_matchings())) == mpc                               # needs sage.libs.flint
        True

        sage: G = graphs.PetersenGraph().copy(immutable=True)
        sage: [sorted(m) for m in G.perfect_matchings()]
        [[(0, 1), (2, 3), (4, 9), (5, 7), (6, 8)],
            [(0, 1), (2, 7), (3, 4), (5, 8), (6, 9)],
            [(0, 4), (1, 2), (3, 8), (5, 7), (6, 9)],
            [(0, 4), (1, 6), (2, 3), (5, 8), (7, 9)],
            [(0, 5), (1, 2), (3, 4), (6, 8), (7, 9)],
            [(0, 5), (1, 6), (2, 7), (3, 8), (4, 9)]]

        sage: list(Graph().perfect_matchings())
        [[]]

        sage: G = graphs.CompleteGraph(5)
        sage: list(G.perfect_matchings())
        []
    """
def M_alternating_even_mark(G, vertex, matching):
    """
    Return the vertices reachable from ``vertex`` via an even alternating path
    starting with a non-matching edge.

    This method implements the algorithm proposed in [LR2004]_. Note that
    the complexity of the algorithm is linear in number of edges.

    INPUT:

    - ``vertex`` -- a vertex of the graph

    - ``matching`` -- a matching of the graph; it can be given using any
      valid input format of :class:`~sage.graphs.graph.Graph`

    OUTPUT:

    - ``even`` -- the set of vertices each of which is reachable from the
      provided vertex through a path starting with an edge not in the
      matching and ending with an edge in the matching; note that a note that a
      :class:`ValueError` is returned if the graph is not simple

    EXAMPLES:

    Show the list of required vertices for a graph `G` with a matching `M`
    for a vertex `u`::

        sage: G = graphs.CycleGraph(3)
        sage: M = G.matching()
        sage: M
        [(0, 2, None)]
        sage: from sage.graphs.matching import M_alternating_even_mark
        sage: S0 = M_alternating_even_mark(G, 0, M)
        sage: S0
        {0}
        sage: S1 = M_alternating_even_mark(G, 1, M)
        sage: S1
        {0, 1, 2}

    The result is equivalent for the underlying simple graph of the provided
    graph, if the other parameters provided are the same::

        sage: G = graphs.CompleteBipartiteGraph(3, 3)
        sage: G.allow_multiple_edges(True)
        sage: G.add_edge(0, 3)
        sage: M = G.matching()
        sage: u = 0
        sage: from sage.graphs.matching import M_alternating_even_mark
        sage: S = M_alternating_even_mark(G, u, M)
        sage: S
        {0, 1, 2}
        sage: T = M_alternating_even_mark(G.to_simple(), u, M)
        sage: T
        {0, 1, 2}

    For a factor critical graph `G` (for instance, a wheel graph of an odd
    order) with a near perfect matching `M` and `u` being the (unique)
    `M`-exposed vertex, each vertex in `G` is reachable from `u` through an
    even length `M`-alternating path as described above::

        sage: G = graphs.WheelGraph(11)
        sage: M = Graph(G.matching())
        sage: G.is_factor_critical(M)
        True
        sage: for v in G:
        ....:     if v not in M:
        ....:          break
        ....:
        sage: from sage.graphs.matching import M_alternating_even_mark
        sage: S = M_alternating_even_mark(G, v, M)
        sage: S == set(G)
        True

    For a matching covered graph `G` (for instance, `K_4 \\odot K_{3,3}`) with a
    perfect matching `M` and for some vertex `u` with `v` being its `M`-matched
    neighbor, each neighbor of `v` is reachable from `u` through an even length
    `M`-alternating path as described above::

        sage: G = Graph()
        sage: G.add_edges([
        ....:    (0, 2), (0, 3), (0, 4), (1, 2),
        ....:    (1, 3), (1, 4), (2, 5), (3, 6),
        ....:    (4, 7), (5, 6), (5, 7), (6, 7)
        ....: ])
        sage: M = Graph(G.matching())
        sage: G.is_matching_covered(M)
        True
        sage: u = 0
        sage: v = next(M.neighbor_iterator(u))
        sage: from sage.graphs.matching import M_alternating_even_mark
        sage: S = M_alternating_even_mark(G, u, M)
        sage: (set(G.neighbor_iterator(v))).issubset(S)
        True

    For a bicritical graph `G` (for instance, the Petersen graph) with a
    perfect matching `M` and for some vertex `u` with its `M`-matched neighbor
    being `v`, each vertex of the graph distinct from `v` is reachable from `u`
    through an even length `M`-alternating path as described above::

        sage: G = graphs.PetersenGraph()
        sage: M = Graph(G.matching())
        sage: G.is_bicritical(M)
        True
        sage: import random
        sage: u = random.choice(list(G))                                            # needs random
        sage: v = next(M.neighbor_iterator(u))
        sage: from sage.graphs.matching import M_alternating_even_mark
        sage: S = M_alternating_even_mark(G, u, M)
        sage: S == (set(G) - {v})
        True

    TESTS:

    Giving a wrong vertex::

        sage: G = graphs.HexahedralGraph()
        sage: M = G.matching()
        sage: u = G.order()
        sage: from sage.graphs.matching import M_alternating_even_mark
        sage: S = M_alternating_even_mark(G, u, M)
        Traceback (most recent call last):
        ...
        ValueError: '8' is not a vertex of the graph

    Giving a wrong matching::

        sage: from sage.graphs.matching import M_alternating_even_mark
        sage: G = graphs.CompleteGraph(6)
        sage: M = [(0, 1), (0, 2)]
        sage: u = 0
        sage: S = M_alternating_even_mark(G, u, M)
        Traceback (most recent call last):
        ...
        ValueError: the input is not a matching
        sage: G = graphs.CompleteBipartiteGraph(3, 3)
        sage: M = [(2*i, 2*i + 1) for i in range(4)]
        sage: u = 0
        sage: S = M_alternating_even_mark(G, u, M)
        Traceback (most recent call last):
        ...
        ValueError: the input is not a matching of the graph

    REFERENCES:

    - [LR2004]_

    .. SEEALSO::
        :meth:`~sage.graphs.graph.Graph.is_factor_critical`,
        :meth:`~sage.graphs.graph.Graph.is_matching_covered`,
        :meth:`~sage.graphs.graph.Graph.is_bicritical`

    AUTHORS:

    - Janmenjaya Panda (2024-06-17)
    """
