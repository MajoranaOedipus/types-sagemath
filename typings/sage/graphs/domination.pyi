from _typeshed import Incomplete
from collections.abc import Generator
from sage.rings.integer import Integer as Integer

def is_dominating(G, dom, focus=None):
    """
    Check whether ``dom`` is a dominating set of ``G``.

    We say that a set `D` of vertices of a graph `G` dominates a set `S` if
    every vertex of `S` either belongs to `D` or is adjacent to a vertex of `D`.
    Also, `D` is a dominating set of `G` if it dominates `V(G)`.

    INPUT:

    - ``dom`` -- iterable of vertices of ``G``; the vertices of the supposed
      dominating set

    - ``focus`` -- iterable of vertices of ``G`` (default: ``None``); if
      specified, this method checks instead if ``dom`` dominates the vertices in
      ``focus``

    EXAMPLES::

        sage: g = graphs.CycleGraph(5)
        sage: g.is_dominating([0,1], [4, 2])
        True

        sage: g.is_dominating([0,1])
        False
    """
def is_redundant(G, dom, focus=None):
    """
    Check whether ``dom`` has redundant vertices.

    For a graph `G` and sets `D` and `S` of vertices, we say that a vertex `v
    \\in D` is *redundant* in `S` if `v` has no private neighbor with respect to
    `D` in `S`.  In other words, there is no vertex in `S` that is dominated by
    `v` but not by `D \\setminus \\{v\\}`.

    INPUT:

    - ``dom`` -- iterable of vertices of ``G``; where we look for redundant
      vertices

    - ``focus`` -- iterable of vertices of ``G`` (default: ``None``); if
      specified, this method checks instead whether ``dom`` has a redundant
      vertex in ``focus``

    .. WARNING::

        The assumption is made that ``focus`` (if provided) does not contain
        repeated vertices.

    EXAMPLES::

        sage: G = graphs.CubeGraph(3)
        sage: G.is_redundant(['000', '101'], ['011'])
        True
        sage: G.is_redundant(['000', '101'])
        False
    """
def private_neighbors(G, vertex, dom):
    """
    Return the private neighbors of a vertex with respect to other vertices.

    A private neighbor of a vertex `v` with respect to a vertex subset `D`
    is a closed neighbor of `v` that is not dominated by a vertex of `D
    \\setminus \\{v\\}`.

    INPUT:

    - ``vertex`` -- a vertex of ``G``

    - ``dom`` -- iterable of vertices of ``G``; the vertices possibly stealing
      private neighbors from ``vertex``

    OUTPUT:

    Return the closed neighbors of ``vertex`` that are not closed neighbors
    of any other vertex of ``dom``.

    EXAMPLES::

        sage: g = graphs.PathGraph(5)
        sage: list(g.private_neighbors(1, [1, 3, 4]))
        [1, 0]

        sage: list(g.private_neighbors(1, [3, 4]))
        [1, 0]

        sage: list(g.private_neighbors(1, [3, 4, 0]))
        []
    """
def dominating_sets(g, k: int = 1, independent: bool = False, total: bool = False, connected: bool = False, solver=None, verbose: int = 0, *, integrality_tolerance: float = 0.001) -> Generator[Incomplete]:
    """
    Return an iterator over the minimum distance-`k` dominating sets
    of the graph.

    A minimum dominating set `S` of a graph `G` is a set of its vertices of
    minimal cardinality such that any vertex of `G` is in `S` or has one of its
    neighbors in `S`. See the :wikipedia:`Dominating_set`.

    A minimum distance-`k` dominating set is a set `S` of vertices of `G` of
    minimal cardinality such that any vertex of `G` is in `S` or at distance at
    most `k` from a vertex in `S`. A distance-`0` dominating set is the set of
    vertices itself, and when `k` is the radius of the graph, any vertex
    dominates all the other vertices.

    As an optimization problem, it can be expressed as follows, where `N^k(u)`
    denotes the set of vertices at distance at most `k` from `u` (the set of
    neighbors when `k=1`):

    .. MATH::

        \\mbox{Minimize : }&\\sum_{v\\in G} b_v\\\\\n        \\mbox{Such that : }&\\forall v \\in G, b_v+\\sum_{u \\in N^k(v)} b_u\\geq 1\\\\\n        &\\forall x\\in G, b_x\\mbox{ is a binary variable}

    We use constraints generation to iterate over the minimum distance-`k`
    dominating sets. That is, after reporting a solution, we add a constraint to
    discard it and solve the problem again until no more solution can be found.

    INPUT:

    - ``k`` -- nonnegative integer (default: `1`); the domination distance

    - ``independent`` -- boolean (default: ``False``); when ``True``, computes
      minimum independent dominating sets, that is minimum dominating sets that
      are also independent sets (see also
      :meth:`~sage.graphs.graph.independent_set`)

    - ``total`` -- boolean (default: ``False``); when ``True``, computes total
      dominating sets (see the See the :wikipedia:`Dominating_set`)

    - ``connected`` -- boolean (default: ``False``); when ``True``, computes
      connected dominating sets (see :wikipedia:`Connected_dominating_set`)

    - ``solver`` -- string (default: ``None``); specifies a Mixed Integer Linear
      Programming (MILP) solver to be used. If set to ``None``, the default one
      is used. For more information on MILP solvers and which default solver is
      used, see the method :meth:`solve
      <sage.numerical.mip.MixedIntegerLinearProgram.solve>` of the class
      :class:`MixedIntegerLinearProgram
      <sage.numerical.mip.MixedIntegerLinearProgram>`.

    - ``verbose`` -- integer (default: 0); sets the level of verbosity. Set
      to 0 by default, which means quiet.

    - ``integrality_tolerance`` -- float; parameter for use with MILP solvers
      over an inexact base ring; see
      :meth:`MixedIntegerLinearProgram.get_values`.

    EXAMPLES:

    Number of distance-`k` dominating sets of a Path graph of order 10::

        sage: g = graphs.PathGraph(10)
        sage: [sum(1 for _ in g.dominating_sets(k=k)) for k in range(11)]               # needs sage.numerical.mip
        [1, 13, 1, 13, 25, 2, 4, 6, 8, 10, 10]

    If we build a graph from two disjoint stars, then link their centers we will
    find a difference between the cardinality of an independent set and a stable
    independent set::

        sage: g = 2 * graphs.StarGraph(5)
        sage: g.add_edge(0, 6)
        sage: [sum(1 for _ in g.dominating_sets(k=k)) for k in range(11)]               # needs sage.numerical.mip
        [1, 1, 2, 12, 12, 12, 12, 12, 12, 12, 12]

    The total dominating set of the Petersen graph has cardinality 4::

        sage: G = graphs.PetersenGraph()
        sage: G.dominating_set(total=True, value_only=True)                             # needs sage.numerical.mip
        4
        sage: sorted(G.dominating_sets(k=1))                                            # needs sage.numerical.mip
        [[0, 2, 6],
         [0, 3, 9],
         [0, 7, 8],
         [1, 3, 7],
         [1, 4, 5],
         [1, 8, 9],
         [2, 4, 8],
         [2, 5, 9],
         [3, 5, 6],
         [4, 6, 7]]

    Independent distance-`k` dominating sets of a Path graph::

        sage: # needs sage.numerical.mip
        sage: G = graphs.PathGraph(6)
        sage: sorted(G.dominating_sets(k=1, independent=True))
        [[1, 4]]
        sage: sorted(G.dominating_sets(k=2, independent=True))
        [[0, 3], [0, 4], [0, 5], [1, 3], [1, 4], [1, 5], [2, 4], [2, 5]]
        sage: sorted(G.dominating_sets(k=3, independent=True))
        [[2], [3]]

    The dominating set is calculated for both the directed and undirected graphs
    (modification introduced in :issue:`17905`)::

        sage: # needs sage.numerical.mip
        sage: g = digraphs.Path(3)
        sage: g.dominating_set(value_only=True)
        2
        sage: list(g.dominating_sets())
        [[0, 1], [0, 2]]
        sage: list(g.dominating_sets(k=2))
        [[0]]
        sage: g = graphs.PathGraph(3)
        sage: g.dominating_set(value_only=True)
        1
        sage: next(g.dominating_sets())
        [1]

    Minimum connected dominating sets of the Petersen graph::

        sage: G = graphs.PetersenGraph()
        sage: G.dominating_set(total=True, value_only=True)                             # needs sage.numerical.mip
        4
        sage: sorted(G.dominating_sets(k=1, connected=True))                            # needs sage.numerical.mip
        [[0, 1, 2, 6],
         [0, 1, 4, 5],
         [0, 3, 4, 9],
         [0, 5, 7, 8],
         [1, 2, 3, 7],
         [1, 6, 8, 9],
         [2, 3, 4, 8],
         [2, 5, 7, 9],
         [3, 5, 6, 8],
         [4, 6, 7, 9]]

    Subgraph induced by the dominating set is connected::

        sage: G = graphs.PetersenGraph()
        sage: all(G.subgraph(vertices=dom).is_connected()
        ....:     for dom in G.dominating_set(k=1, connected=True))
        True

    Minimum distance-k connected dominating sets of the Tietze graph::

        sage: G = graphs.TietzeGraph()
        sage: sorted(G.dominating_sets(k=2, connected=True))
        [[0, 9], [1, 0], [2, 3], [4, 3], [5, 6], [7, 6], [8, 0], [10, 3], [11, 6]]
        sage: sorted(G.dominating_sets(k=3, connected=True))
        [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11]]

    TESTS::

        sage: g = Graph([(0, 1)])
        sage: next(g.dominating_sets(k=-1))
        Traceback (most recent call last):
        ...
        ValueError: the domination distance must be a nonnegative integer

    The method is robust to vertices with incomparable labels::

        sage: G = Graph([(1, 'A'), ('A', 2), (2, 3), (3, 1)])
        sage: L = list(G.dominating_sets())
        sage: len(L)
        6
    """
def dominating_set(g, k: int = 1, independent: bool = False, total: bool = False, connected: bool = False, value_only: bool = False, solver=None, verbose: int = 0, *, integrality_tolerance: float = 0.001):
    """
    Return a minimum distance-`k` dominating set of the graph.

    A minimum dominating set `S` of a graph `G` is a set of its vertices of
    minimal cardinality such that any vertex of `G` is in `S` or has one of its
    neighbors in `S`. See the :wikipedia:`Dominating_set`.

    A minimum distance-`k` dominating set is a set `S` of vertices of `G` of
    minimal cardinality such that any vertex of `G` is in `S` or at distance at
    most `k` from a vertex in `S`. A distance-`0` dominating set is the set of
    vertices itself, and when `k` is the radius of the graph, any vertex
    dominates all the other vertices.

    As an optimization problem, it can be expressed as follows, where `N^k(u)`
    denotes the set of vertices at distance at most `k` from `u` (the set of
    neighbors when `k=1`):

    .. MATH::

        \\mbox{Minimize : }&\\sum_{v\\in G} b_v\\\\\n        \\mbox{Such that : }&\\forall v \\in G, b_v+\\sum_{u \\in N^k(v)} b_u\\geq 1\\\\\n        &\\forall x\\in G, b_x\\mbox{ is a binary variable}

    INPUT:

    - ``k`` -- nonnegative integer (default: `1`); the domination distance

    - ``independent`` -- boolean (default: ``False``); when ``True``, computes a
      minimum independent dominating set, that is a minimum dominating set that
      is also an independent set (see also
      :meth:`~sage.graphs.graph.independent_set`)

    - ``total`` -- boolean (default: ``False``); when ``True``, computes a total
      dominating set (see the See the :wikipedia:`Dominating_set`)

    - ``connected`` -- boolean (default: ``False``); when ``True``, computes a
      connected dominating set (see :wikipedia:`Connected_dominating_set`)

    - ``value_only`` -- boolean (default: ``False``); whether to only return the
      cardinality of the computed dominating set, or to return its list of
      vertices (default)

    - ``solver`` -- string (default: ``None``); specifies a Mixed Integer Linear
      Programming (MILP) solver to be used. If set to ``None``, the default one
      is used. For more information on MILP solvers and which default solver is
      used, see the method :meth:`solve
      <sage.numerical.mip.MixedIntegerLinearProgram.solve>` of the class
      :class:`MixedIntegerLinearProgram
      <sage.numerical.mip.MixedIntegerLinearProgram>`.

    - ``verbose`` -- integer (default: 0); sets the level of verbosity. Set
      to 0 by default, which means quiet.

    - ``integrality_tolerance`` -- float; parameter for use with MILP solvers
      over an inexact base ring; see
      :meth:`MixedIntegerLinearProgram.get_values`.

    EXAMPLES:

    A basic illustration on a ``PappusGraph``::

        sage: g = graphs.PappusGraph()
        sage: g.dominating_set(value_only=True)                                         # needs sage.numerical.mip
        5

    If we build a graph from two disjoint stars, then link their centers we will
    find a difference between the cardinality of an independent set and a stable
    independent set::

        sage: g = 2 * graphs.StarGraph(5)
        sage: g.add_edge(0, 6)
        sage: len(g.dominating_set())                                                   # needs sage.numerical.mip
        2
        sage: len(g.dominating_set(independent=True))                                   # needs sage.numerical.mip
        6

    The total dominating set of the Petersen graph has cardinality 4::

        sage: G = graphs.PetersenGraph()
        sage: G.dominating_set(total=True, value_only=True)                             # needs sage.numerical.mip
        4

    The dominating set is calculated for both the directed and undirected graphs
    (modification introduced in :issue:`17905`)::

        sage: g = digraphs.Path(3)
        sage: g.dominating_set(value_only=True)                                         # needs sage.numerical.mip
        2
        sage: g = graphs.PathGraph(3)
        sage: g.dominating_set(value_only=True)                                         # needs sage.numerical.mip
        1

    Cardinality of distance-`k` dominating sets::

        sage: G = graphs.PetersenGraph()
        sage: [G.dominating_set(k=k, value_only=True) for k in range(G.radius() + 1)]   # needs sage.numerical.mip
        [10, 3, 1]
        sage: G = graphs.PathGraph(5)
        sage: [G.dominating_set(k=k, value_only=True) for k in range(G.radius() + 1)]   # needs sage.numerical.mip
        [5, 2, 1]
    """
def minimal_dominating_sets(G, to_dominate=None, work_on_copy: bool = True, k: int = 1) -> Generator[Incomplete]:
    """
    Return an iterator over the minimal dominating sets of a graph.

    INPUT:

    - ``G`` -- a graph

    - ``to_dominate`` -- vertex iterable or ``None`` (default: ``None``);
      the set of vertices to be dominated

    - ``work_on_copy`` -- boolean (default: ``True``); whether or not to work on
      a copy of the input graph; if set to ``False``, the input graph will be
      modified (relabeled)

    - ``k`` -- nonnegative integer (default: `1`); the domination distance

    OUTPUT:

    An iterator over the inclusion-minimal sets of vertices of ``G``.
    If ``to_dominate`` is provided, return an iterator over the
    inclusion-minimal sets of vertices that dominate the vertices of
    ``to_dominate``.

    ALGORITHM: The algorithm described in [BDHPR2019]_.

    AUTHOR: Jean-Florent Raymond (2019-03-04) -- initial version.

    EXAMPLES::

        sage: G = graphs.ButterflyGraph()
        sage: ll = list(G.minimal_dominating_sets())
        sage: pp = [{0, 1}, {1, 3}, {0, 2}, {2, 3}, {4}]
        sage: len(ll) == len(pp) and all(x in pp for x in ll) and all(x in ll for x in pp)
        True

        sage: ll = list(G.minimal_dominating_sets([0,3]))
        sage: pp = [{0}, {3}, {4}]
        sage: len(ll) == len(pp) and all(x in pp for x in ll) and all(x in ll for x in pp)
        True

        sage: ll = list(G.minimal_dominating_sets([4]))
        sage: pp = [{4}, {0}, {1}, {2}, {3}]
        sage: len(ll) == len(pp) and all(x in pp for x in ll) and all(x in ll for x in pp)
        True

    ::

        sage: ll = list(graphs.PetersenGraph().minimal_dominating_sets())
        sage: pp = [{0, 2, 6},
        ....:       {0, 9, 3},
        ....:       {0, 8, 7},
        ....:       {1, 3, 7},
        ....:       {1, 4, 5},
        ....:       {8, 1, 9},
        ....:       {8, 2, 4},
        ....:       {9, 2, 5},
        ....:       {3, 5, 6},
        ....:       {4, 6, 7},
        ....:       {0, 8, 2, 9},
        ....:       {0, 3, 6, 7},
        ....:       {1, 3, 5, 9},
        ....:       {8, 1, 4, 7},
        ....:       {2, 4, 5, 6},
        ....:       {0, 1, 2, 3, 4},
        ....:       {0, 1, 2, 5, 7},
        ....:       {0, 1, 4, 6, 9},
        ....:       {0, 1, 5, 6, 8},
        ....:       {0, 8, 3, 4, 5},
        ....:       {0, 9, 4, 5, 7},
        ....:       {8, 1, 2, 3, 6},
        ....:       {1, 2, 9, 6, 7},
        ....:       {9, 2, 3, 4, 7},
        ....:       {8, 2, 3, 5, 7},
        ....:       {8, 9, 3, 4, 6},
        ....:       {8, 9, 5, 6, 7}]
        sage: len(ll) == len(pp) and all(x in pp for x in ll) and all(x in ll for x in pp)
        True

    Listing minimal distance-`k` dominating sets::

        sage: G = graphs.Grid2dGraph(2, 3)
        sage: list(G.minimal_dominating_sets(k=0))
        [{(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)}]
        sage: list(G.minimal_dominating_sets(k=1))
        [{(0, 0), (0, 2), (1, 1)},
         {(0, 1), (1, 1)},
         {(0, 0), (0, 1), (0, 2)},
         {(0, 2), (1, 0)},
         {(0, 0), (1, 2)},
         {(0, 1), (1, 0), (1, 2)},
         {(1, 0), (1, 1), (1, 2)}]
        sage: list(G.minimal_dominating_sets(k=2))
        [{(0, 0), (1, 2)},
         {(0, 2), (1, 2)},
         {(1, 0), (1, 2)},
         {(0, 1)},
         {(0, 0), (0, 2)},
         {(0, 2), (1, 0)},
         {(0, 0), (1, 0)},
         {(1, 1)}]
        sage: list(G.minimal_dominating_sets(k=3))
        [{(0, 0)}, {(0, 1)}, {(0, 2)}, {(1, 0)}, {(1, 1)}, {(1, 2)}]

    When parameter ``work_on_copy`` is ``False``, the input graph is modified
    (relabeled)::

        sage: G = Graph([('A', 'B')])
        sage: _ = list(G.minimal_dominating_sets(work_on_copy=True))
        sage: set(G) == {'A', 'B'}
        True
        sage: _ = list(G.minimal_dominating_sets(work_on_copy=False))
        sage: set(G) == {'A', 'B'}
        False
        sage: set(G) == {0, 1}
        True

    TESTS:

    The empty graph is handled correctly::

        sage: list(Graph().minimal_dominating_sets())
        [set()]

    Test on all graphs on 6 vertices::

        sage: from sage.combinat.subset import Subsets
        sage: def minimal_dominating_sets_naive(G):
        ....:     return (S for S in Subsets(G.vertices(sort=False))
        ....:             if not(G.is_redundant(S)) and G.is_dominating(S))
        sage: def big_check(n):
        ....:     for G in graphs(n):
        ....:         ll = list(G.minimal_dominating_sets())
        ....:         pp = list(minimal_dominating_sets_naive(G))
        ....:         if (len(pp) != len(pp)
        ....:             or any(x not in pp for x in ll)
        ....:             or any(x not in ll for x in pp)):
        ....:             return False
        ....:     return True
        sage: big_check(6)  # long time
        True

    Outputs are unique::

        sage: def check_uniqueness(g):
        ....:     counter_1 = 0
        ....:     for dom_1 in g.minimal_dominating_sets():
        ....:         counter_1 += 1
        ....:         counter_2 = 0
        ....:         for dom_2 in g.minimal_dominating_sets():
        ....:             counter_2 += 1
        ....:             if counter_2 >= counter_1:
        ....:                 break
        ....:             if dom_1 == dom_2:
        ....:                 return False
        ....:     return True
        sage: check_uniqueness(graphs.RandomGNP(9, 0.5))
        True

    Asking for a negative distance::

        sage: next(Graph(1).minimal_dominating_sets(k=-1))
        Traceback (most recent call last):
        ...
        ValueError: the domination distance must be a nonnegative integer

    Trying to dominate vertices that are not part of the graph::

        sage: next(Graph(1).minimal_dominating_sets(to_dominate=['foo']))
        Traceback (most recent call last):
        ...
        ValueError: vertex (foo) is not a vertex of the graph

    The method is robust to vertices with incomparable labels::

        sage: G = Graph([(1, 'A'), ('A', 2), (2, 3), (3, 1)])
        sage: L = list(G.minimal_dominating_sets())
        sage: len(L)
        6
        sage: {3, 'A'} in L
        True
    """
def greedy_dominating_set(G, k: int = 1, vertices=None, ordering=None, return_sets: bool = False, closest: bool = False):
    '''
    Return a greedy distance-`k` dominating set of the graph.

    A distance-`k` dominating set `S` of a graph `G` is a set of its vertices of
    minimal cardinality such that any vertex of `G` is in `S` or is at distance
    at most `k` from a vertex in `S`. See the :wikipedia:`Dominating_set`.

    When `G` is directed, vertex `u` can be a dominator of vertex `v` if there
    is a directed path of length at most `k` from `u` to `v`.

    This method implements a greedy heuristic to find a minimal dominatic set.

    INPUT:

    - ``G`` -- a Graph

    - ``k`` -- integer (default: `1`); the domination distance to consider

    - ``vertices`` -- iterable container of vertices (default: ``None``); when
      specified, return a dominating set of the specified vertices only

    - ``ordering`` -- string (default: ``None``); specify the order in which to
      consider the vertices

      - ``None`` -- if ``vertices`` is ``None``, then consider the vertices in
        the order given by ``list(G)``. Otherwise, consider the vertices in the
        order of iteration of ``vertices``.

      - ``\'degree_min\'`` -- consider the vertices by increasing degree

      - ``\'degree_max\'`` -- consider the vertices by decreasing degree

    - ``return_sets`` -- boolean (default: ``False``); whether to return the
      vertices of the dominating set only (default), or a dictionary mapping
      each vertex of the dominating set to the set of vertices it dominates.

    - ``closest`` -- boolean (default: ``False``); whether to attach a vertex to
      its closest dominator or not. This parameter is use only when
      ``return_sets`` is ``True``.

    EXAMPLES:

    Dominating sets of a path::

        sage: from sage.graphs.domination import greedy_dominating_set
        sage: G = graphs.PathGraph(5)
        sage: sorted(greedy_dominating_set(G, ordering=None))
        [0, 2, 4]
        sage: sorted(greedy_dominating_set(G, ordering=\'degree_min\'))
        [0, 2, 4]
        sage: sorted(greedy_dominating_set(G, ordering=\'degree_max\'))
        [1, 3]
        sage: sorted(greedy_dominating_set(G, k=2, ordering=None))
        [0, 3]
        sage: sorted(greedy_dominating_set(G, k=2, ordering=\'degree_min\'))
        [0, 4]
        sage: sorted(greedy_dominating_set(G, k=2, ordering=\'degree_max\'))
        [1, 4]
        sage: greedy_dominating_set(G, k=3, ordering=\'degree_min\', return_sets=True, closest=False)
        {0: {0, 1, 2, 3}, 4: {4}}
        sage: greedy_dominating_set(G, k=3, ordering=\'degree_min\', return_sets=True, closest=True)
        {0: {0, 2, 3}, 4: {1, 4}}

    Asking for a dominating set of a subset of vertices::

        sage: from sage.graphs.domination import greedy_dominating_set
        sage: from sage.graphs.domination import is_dominating
        sage: G = graphs.PetersenGraph()
        sage: vertices = {0, 1, 2, 3, 4, 5}
        sage: dom = greedy_dominating_set(G, vertices=vertices, return_sets=True)
        sage: sorted(dom)
        [0, 2]
        sage: is_dominating(G, dom, focus=vertices)
        True
        sage: is_dominating(G, dom)
        False
        sage: dominated = [u for v in dom for u in dom[v]]
        sage: sorted(dominated) == sorted(vertices)
        True

    Influence of the ordering of the vertices on the result::

        sage: from sage.graphs.domination import greedy_dominating_set
        sage: G = graphs.StarGraph(4)
        sage: greedy_dominating_set(G, vertices=[0, 1, 2, 3, 4])
        [0]
        sage: sorted(greedy_dominating_set(G, vertices=[1, 2, 3, 4, 0]))
        [1, 2, 3, 4]

    Dominating set of a directed graph::

        sage: from sage.graphs.domination import greedy_dominating_set
        sage: D = digraphs.Path(3)
        sage: sorted(greedy_dominating_set(D, vertices=[0, 1, 2]))
        [0, 2]

    TESTS:

    Random tests::

        sage: from sage.graphs.domination import greedy_dominating_set
        sage: from sage.graphs.domination import is_dominating
        sage: G = graphs.RandomGNP(15, .2)
        sage: for o in [None, "degree_min", "degree_max"]:
        ....:     for c in [True, False]:
        ....:         dom = greedy_dominating_set(G, ordering=o, closest=c)
        ....:         if not is_dominating(G, dom):
        ....:             print("something goes wrong")

    Corner cases::

        sage: greedy_dominating_set(Graph())
        []
        sage: greedy_dominating_set(Graph(1))
        [0]
        sage: greedy_dominating_set(Graph(2))
        [0, 1]
        sage: G = graphs.PathGraph(5)
        sage: dom = greedy_dominating_set(G, vertices=[0, 1, 3, 4])

    The method is robust to vertices with incomparable labels::

        sage: G = Graph([(1, \'A\')])
        sage: len(greedy_dominating_set(G))
        1

    Check parameters::

        sage: greedy_dominating_set(G, ordering=\'foo\')
        Traceback (most recent call last):
        ...
        ValueError: ordering must be None, "degree_min" or "degree_max"
    '''
def maximum_leaf_number(G, solver=None, verbose: int = 0, integrality_tolerance: float = 0.001):
    """
    Return the maximum leaf number of the graph.

    The maximum leaf number is the maximum possible number of leaves of a
    spanning tree of `G`. This is also the cardinality of the complement of a
    minimum connected dominating set.
    See the :wikipedia:`Connected_dominating_set`.

    The MLN of a graph with less than 2 vertices is 0, while the MLN of a connected
    graph with 2 or 3 vertices is 1 or 2 respectively.

    INPUT:

    - ``G`` -- a Graph

    - ``solver`` -- string (default: ``None``); specifies a Mixed Integer Linear
      Programming (MILP) solver to be used. If set to ``None``, the default one
      is used. For more information on MILP solvers and which default solver is
      used, see the method :meth:`solve
      <sage.numerical.mip.MixedIntegerLinearProgram.solve>` of the class
      :class:`MixedIntegerLinearProgram
      <sage.numerical.mip.MixedIntegerLinearProgram>`.

    - ``verbose`` -- integer (default: 0); sets the level of verbosity. Set
      to 0 by default, which means quiet.

    - ``integrality_tolerance`` -- float; parameter for use with MILP solvers
      over an inexact base ring; see
      :meth:`MixedIntegerLinearProgram.get_values`.

    EXAMPLES:

    Empty graph::

        sage: G = Graph()
        sage: G.maximum_leaf_number()
        0

    Petersen graph::

        sage: G = graphs.PetersenGraph()
        sage: G.maximum_leaf_number()
        6

    TESTS:

    One vertex::

        sage: G = Graph(1)
        sage: G.maximum_leaf_number()
        0

    Two vertices::

        sage: G = graphs.PathGraph(2)
        sage: G.maximum_leaf_number()
        1

    Unconnected graph::

        sage: G = Graph(2)
        sage: G.maximum_leaf_number()
        Traceback (most recent call last):
        ...
        ValueError: the graph must be connected
    """
