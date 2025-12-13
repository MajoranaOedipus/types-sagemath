from _typeshed import Incomplete
from collections.abc import Generator

def breadth_first_level_search(G, start) -> Generator[Incomplete]:
    """
    Generate a sequence of dictionaries, each mapping the vertices at
    distance ``i`` from ``start`` to the set of their neighbours at
    distance ``i+1``.

    Originally written by D. Eppstein for the PADS library
    (http://www.ics.uci.edu/~eppstein/PADS/).

    INPUT:

    - ``G`` -- a graph to perform the search on

    - ``start`` -- vertex or list of vertices from which to start the traversal

    EXAMPLES::

        sage: H = digraphs.DeBruijn(3,2)                                                # needs sage.combinat
        sage: list(sage.graphs.partial_cube.breadth_first_level_search(H, '00'))        # needs sage.combinat
        [{'00': {'01', '02'}},
         {'01': {'10', '11', '12'}, '02': {'20', '21', '22'}},
         {'10': set(),
          '11': set(),
          '12': set(),
          '20': set(),
          '21': set(),
          '22': set()}]
    """
def depth_first_traversal(G, start) -> Generator[Incomplete]:
    """
    Generate a sequence of triples (v,w,edgetype) for DFS of graph G.

    Originally written by D. Eppstein for the PADS library
    (http://www.ics.uci.edu/~eppstein/PADS/).

    INPUT:

    - ``G`` -- a graph to perform the search on

    - ``start`` -- vertex or list of vertices from which to start the traversal

    OUTPUT:

    - a generator of triples ``(v,w,edgetype)``, where ``edgetype`` is ``True``
      if the algorithm is progressing via the edge ``vw``, or ``False`` if the
      algorithm is backtracking via the edge ``wv``.

    EXAMPLES::

        sage: H = digraphs.DeBruijn(3,2)                                                # needs sage.combinat
        sage: t = list(sage.graphs.partial_cube.depth_first_traversal(H, '00'))         # needs sage.combinat
        sage: len(t)                                                                    # needs sage.combinat
        16
    """
def is_partial_cube(G, certificate: bool = False):
    """
    Test whether the given graph is a partial cube.

    A partial cube is a graph that can be isometrically embedded into a
    hypercube, i.e., its vertices can be labelled with (0,1)-vectors of some
    fixed length such that the distance between any two vertices in the graph
    equals the Hamming distance of their labels.

    Originally written by D. Eppstein for the PADS library
    (http://www.ics.uci.edu/~eppstein/PADS/), see also
    [Epp2008]_.  The algorithm runs in `O(n^2)` time, where `n`
    is the number of vertices. See the documentation of
    :mod:`~sage.graphs.partial_cube` for an overview of the algorithm.

    INPUT:

    - ``certificate`` -- boolean (default: ``False``); this function returns
      ``True`` or ``False`` according to the graph, when ``certificate =
      False``. When ``certificate = True`` and the graph is a partial cube, the
      function returns ``(True, mapping)``, where ``mapping`` is an isometric
      mapping of the vertices of the graph to the vertices of a hypercube
      ((0, 1)-strings of a fixed length). When ``certificate = True`` and the
      graph is not a partial cube, ``(False, None)`` is returned.

    EXAMPLES:

    The Petersen graph is not a partial cube::

        sage: g = graphs.PetersenGraph()
        sage: g.is_partial_cube()
        False

    All prisms are partial cubes::

        sage: g = graphs.CycleGraph(10).cartesian_product(graphs.CompleteGraph(2))
        sage: g.is_partial_cube()
        True

    TESTS:

    The returned mapping is an isometric embedding into a hypercube::

        sage: g = graphs.DesarguesGraph()
        sage: _, m = g.is_partial_cube(certificate=True)
        sage: m # random
        {0: '00000',
         1: '00001',
         2: '00011',
         3: '01011',
         4: '11011',
         5: '11111',
         6: '11110',
         7: '11100',
         8: '10100',
         9: '00100',
         10: '01000',
         11: '10001',
         12: '00111',
         13: '01010',
         14: '11001',
         15: '10111',
         16: '01110',
         17: '11000',
         18: '10101',
         19: '00110'}
        sage: all(all(g.distance(u, v) == len([i for i in range(len(m[u])) if m[u][i] != m[v][i]]) for v in m) for u in m)
        True

    A graph without vertices is trivially a partial cube::

        sage: Graph().is_partial_cube(certificate=True)
        (True, {})
    """
