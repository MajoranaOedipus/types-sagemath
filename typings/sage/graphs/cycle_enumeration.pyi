from _typeshed import Incomplete
from collections.abc import Generator

def all_cycles_iterator(self, starting_vertices=None, simple: bool = False, rooted: bool = False, max_length=None, trivial: bool = False, weight_function=None, by_weight: bool = False, check_weight: bool = True, report_weight: bool = False, algorithm: str = 'A') -> Generator[Incomplete, None, Incomplete]:
    """
    Return an iterator over all the cycles of ``self`` starting with one of
    the given vertices. Each edge must have a positive weight.

    The cycles are enumerated in increasing length order.

    INPUT:

    - ``starting_vertices`` -- iterable (default: ``None``); vertices from
      which the cycles must start. If ``None``, then all vertices of the
      graph can be starting points. This argument is necessary if ``rooted``
      is set to ``True``.

    - ``simple`` -- boolean (default: ``False``); if set to ``True``, then
      only simple cycles are considered. A cycle is simple if the only
      vertex occurring twice in it is the starting and ending one.

    - ``rooted`` -- boolean (default: ``False``); if set to False, then
      cycles differing only by their starting vertex are considered the same
      (e.g. ``['a', 'b', 'c', 'a']`` and ``['b', 'c', 'a',
      'b']``). Otherwise, all cycles are enumerated.

    - ``max_length`` -- nonnegative integer (default: ``None``); the
      maximum length of the enumerated paths. If set to ``None``, then all
      lengths are allowed.

    - ``trivial`` -- boolean (default: ``False``); if set to ``True``, then
      the empty paths are also enumerated

    - ``weight_function`` -- function (default: ``None``); a function that
      takes as input an edge ``(u, v, l)`` and outputs its weight. If not
      ``None``, ``by_weight`` is automatically set to ``True``. If ``None``
      and ``by_weight`` is ``True``, we use the edge label ``l`` as a
      weight.

    - ``by_weight`` -- boolean (default: ``False``); if ``True``, the edges
      in the graph are weighted, otherwise all edges have weight 1

    - ``check_weight`` -- boolean (default: ``True``); whether to check that
      the ``weight_function`` outputs a number for each edge

    - ``report_weight`` -- boolean (default: ``False``); if ``False``, just
      a cycle is returned. Otherwise a tuple of cycle length and cycle is
      returned.

    - ``algorithm`` -- string (default: ``'A'``); the algorithm used to
      enumerate the cycles.

        - The algorithm ``'A'`` holds cycle iterators starting with each vertex,
          and output them in increasing length order.

        - The algorithm ``'B'`` holds cycle iterators starting with each edge,
          and output them in increasing length order. It depends on the k-shortest
          simple paths algorithm. Thus, it is not available if ``simple=False``.

    OUTPUT: iterator

    .. SEEALSO::

        - :meth:`all_simple_cycles`
        - :meth:`~sage.graphs.path_enumeration.shortest_simple_paths`

    AUTHOR:

        Alexandre Blondin Masse

    EXAMPLES::

        sage: g = DiGraph({'a': ['a', 'b'], 'b': ['c'], 'c': ['d'], 'd': ['c']}, loops=True)
        sage: it = g.all_cycles_iterator()
        sage: for _ in range(7): print(next(it))
        ['a', 'a']
        ['a', 'a', 'a']
        ['c', 'd', 'c']
        ['a', 'a', 'a', 'a']
        ['a', 'a', 'a', 'a', 'a']
        ['c', 'd', 'c', 'd', 'c']
        ['a', 'a', 'a', 'a', 'a', 'a']

    There are no cycles in the empty graph and in acyclic graphs::

        sage: g = DiGraph()
        sage: it = g.all_cycles_iterator()
        sage: list(it)
        []
        sage: g = DiGraph({0:[1]})
        sage: it = g.all_cycles_iterator()
        sage: list(it)
        []

    It is possible to restrict the starting vertices of the cycles::

        sage: g = DiGraph({'a': ['a', 'b'], 'b': ['c'], 'c': ['d'], 'd': ['c']}, loops=True)
        sage: it = g.all_cycles_iterator(starting_vertices=['b', 'c'])
        sage: for _ in range(3): print(next(it))
        ['c', 'd', 'c']
        ['c', 'd', 'c', 'd', 'c']
        ['c', 'd', 'c', 'd', 'c', 'd', 'c']

    Also, one can bound the length of the cycles::

        sage: it = g.all_cycles_iterator(max_length=3)
        sage: list(it)
        [['a', 'a'], ['a', 'a', 'a'], ['c', 'd', 'c'],
         ['a', 'a', 'a', 'a']]

    By default, cycles differing only by their starting point are not all
    enumerated, but this may be parametrized::

        sage: it = g.all_cycles_iterator(max_length=3, rooted=False)
        sage: list(it)
        [['a', 'a'], ['a', 'a', 'a'], ['c', 'd', 'c'],
         ['a', 'a', 'a', 'a']]
        sage: it = g.all_cycles_iterator(max_length=3, rooted=True)
        sage: list(it)
        [['a', 'a'], ['a', 'a', 'a'], ['c', 'd', 'c'], ['d', 'c', 'd'],
         ['a', 'a', 'a', 'a']]

    One may prefer to enumerate simple cycles, i.e. cycles such that the only
    vertex occurring twice in it is the starting and ending one (see also
    :meth:`all_simple_cycles`)::

        sage: it = g.all_cycles_iterator(simple=True)
        sage: list(it)
        [['a', 'a'], ['c', 'd', 'c']]
        sage: g = digraphs.Circuit(4)
        sage: list(g.all_cycles_iterator(simple=True))
        [[0, 1, 2, 3, 0]]

    A cycle is enumerated in increasing length order for a weighted graph::

        sage: g = DiGraph()
        sage: g.add_edges([('a', 'b', 2), ('a', 'e', 2), ('b', 'a', 1), ('b', 'c', 1),
        ....:              ('c', 'd', 2), ('d', 'b', 1), ('e', 'a', 2)])
        sage: it = g.all_cycles_iterator(simple=False, max_length=None,
        ....:                            by_weight=True, report_weight=True)
        sage: for i in range(9): print(next(it))
        (3, ['a', 'b', 'a'])
        (4, ['a', 'e', 'a'])
        (4, ['b', 'c', 'd', 'b'])
        (6, ['a', 'b', 'a', 'b', 'a'])
        (7, ['a', 'b', 'a', 'e', 'a'])
        (7, ['a', 'b', 'c', 'd', 'b', 'a'])
        (7, ['a', 'e', 'a', 'b', 'a'])
        (8, ['a', 'e', 'a', 'e', 'a'])
        (8, ['b', 'c', 'd', 'b', 'c', 'd', 'b'])

    Each edge must have a positive weight::

        sage: g = DiGraph()
        sage: g.add_edges([('a', 'b', -2), ('b', 'a', 1)])
        sage: next(g.all_cycles_iterator(simple=False, max_length=None,
        ....:                            by_weight=True, report_weight=True))
        Traceback (most recent call last):
        ...
        ValueError: negative weight is not allowed

    The algorithm ``'B'`` works for undirected graphs as well::

        sage: g = Graph({0: [1, 2], 1: [0, 2], 2: [0, 1, 3, 5], 3: [2, 4], 4: [3, 5], 5: [4, 2]})
        sage: for cycle in g.all_cycles_iterator(algorithm='B', simple=True, by_weight=True):
        ....:     print(cycle)
        [0, 1, 2, 0]
        [2, 3, 4, 5, 2]

    The algorithm ``'B'`` is available only when `simple=True`::

        sage: g = DiGraph()
        sage: g.add_edges([('a', 'b', 1), ('b', 'a', 1)])
        sage: next(g.all_cycles_iterator(algorithm='B', simple=False))
        ....:
        Traceback (most recent call last):
        ...
        ValueError: The algorithm 'B' is available only when simple=True.

    The algorithm ``'A'`` is available only for directed graphs::

        sage: g = Graph({0: [1, 2], 1: [0, 2], 2: [0, 1]})
        sage: next(g.all_cycles_iterator(algorithm='A', simple=True))
        Traceback (most recent call last):
        ...
        ValueError: The algorithm 'A' is available only for directed graphs.
    """
def all_simple_cycles(self, starting_vertices=None, rooted: bool = False, max_length=None, trivial: bool = False, weight_function=None, by_weight: bool = False, check_weight: bool = True, report_weight: bool = False, algorithm: str = 'A'):
    """
    Return a list of all simple cycles of ``self``. The cycles are
    enumerated in increasing length order. Each edge must have a
    positive weight.

    INPUT:

    - ``starting_vertices`` -- iterable (default: ``None``); vertices from
      which the cycles must start. If ``None``, then all vertices of the
      graph can be starting points. This argument is necessary if ``rooted``
      is set to ``True``.

    - ``rooted`` -- boolean (default: ``False``); if set to False, then
      cycles differing only by their starting vertex are considered the same
      (e.g. ``['a', 'b', 'c', 'a']`` and ``['b', 'c', 'a',
      'b']``). Otherwise, all cycles are enumerated.

    - ``max_length`` -- nonnegative integer (default: ``None``); the
      maximum length of the enumerated paths. If set to ``None``, then all
      lengths are allowed.

    - ``trivial`` -- boolean (default: ``False``); if set to ``True``, then
      the empty paths are also enumerated

    - ``weight_function`` -- function (default: ``None``); a function that
      takes as input an edge ``(u, v, l)`` and outputs its weight. If not
      ``None``, ``by_weight`` is automatically set to ``True``. If ``None``
      and ``by_weight`` is ``True``, we use the edge label ``l`` as a
      weight.

    - ``by_weight`` -- boolean (default: ``False``); if ``True``, the edges
      in the graph are weighted, otherwise all edges have weight 1

    - ``check_weight`` -- boolean (default: ``True``); whether to check that
      the ``weight_function`` outputs a number for each edge

    - ``report_weight`` -- boolean (default: ``False``); if ``False``, just
      a cycle is returned. Otherwise a tuple of cycle length and cycle is
      returned.

    - ``algorithm`` -- string (default: ``'A'``); the algorithm used to
      enumerate the cycles.

        - The algorithm ``'A'`` holds cycle iterators starting with each vertex,
          and output them in increasing length order.

        - The algorithm ``'B'`` holds cycle iterators starting with each edge,
          and output them in increasing length order.

    OUTPUT: list

    .. NOTE::

        Although the number of simple cycles of a finite graph is always
        finite, computing all its cycles may take a very long time.

    EXAMPLES::

        sage: g = DiGraph({'a': ['a', 'b'], 'b': ['c'], 'c': ['d'], 'd': ['c']}, loops=True)
        sage: g.all_simple_cycles()
        [['a', 'a'], ['c', 'd', 'c']]

    The directed version of the Petersen graph::

        sage: g = graphs.PetersenGraph().to_directed()
        sage: g.all_simple_cycles(max_length=4)
        [[0, 1, 0], [0, 4, 0], [0, 5, 0], [1, 2, 1], [1, 6, 1], [2, 3, 2],
         [2, 7, 2], [3, 4, 3], [3, 8, 3], [4, 9, 4], [5, 7, 5], [5, 8, 5],
         [6, 8, 6], [6, 9, 6], [7, 9, 7]]
        sage: g.all_simple_cycles(max_length=6)
        [[0, 1, 0], [0, 4, 0], [0, 5, 0], [1, 2, 1], [1, 6, 1], [2, 3, 2],
         [2, 7, 2], [3, 4, 3], [3, 8, 3], [4, 9, 4], [5, 7, 5], [5, 8, 5],
         [6, 8, 6], [6, 9, 6], [7, 9, 7], [0, 1, 2, 3, 4, 0],
         [0, 1, 2, 7, 5, 0], [0, 1, 6, 8, 5, 0], [0, 1, 6, 9, 4, 0],
         [0, 4, 3, 2, 1, 0], [0, 4, 3, 8, 5, 0], [0, 4, 9, 6, 1, 0],
         [0, 4, 9, 7, 5, 0], [0, 5, 7, 2, 1, 0], [0, 5, 7, 9, 4, 0],
         [0, 5, 8, 3, 4, 0], [0, 5, 8, 6, 1, 0], [1, 2, 3, 8, 6, 1],
         [1, 2, 7, 9, 6, 1], [1, 6, 8, 3, 2, 1], [1, 6, 9, 7, 2, 1],
         [2, 3, 4, 9, 7, 2], [2, 3, 8, 5, 7, 2], [2, 7, 5, 8, 3, 2],
         [2, 7, 9, 4, 3, 2], [3, 4, 9, 6, 8, 3], [3, 8, 6, 9, 4, 3],
         [5, 7, 9, 6, 8, 5], [5, 8, 6, 9, 7, 5], [0, 1, 2, 3, 8, 5, 0],
         [0, 1, 2, 7, 9, 4, 0], [0, 1, 6, 8, 3, 4, 0],
         [0, 1, 6, 9, 7, 5, 0], [0, 4, 3, 2, 7, 5, 0],
         [0, 4, 3, 8, 6, 1, 0], [0, 4, 9, 6, 8, 5, 0],
         [0, 4, 9, 7, 2, 1, 0], [0, 5, 7, 2, 3, 4, 0],
         [0, 5, 7, 9, 6, 1, 0], [0, 5, 8, 3, 2, 1, 0],
         [0, 5, 8, 6, 9, 4, 0], [1, 2, 3, 4, 9, 6, 1],
         [1, 2, 7, 5, 8, 6, 1], [1, 6, 8, 5, 7, 2, 1],
         [1, 6, 9, 4, 3, 2, 1], [2, 3, 8, 6, 9, 7, 2],
         [2, 7, 9, 6, 8, 3, 2], [3, 4, 9, 7, 5, 8, 3],
         [3, 8, 5, 7, 9, 4, 3]]

    The complete graph (without loops) on `4` vertices::

        sage: g = graphs.CompleteGraph(4).to_directed()
        sage: g.all_simple_cycles()
        [[0, 1, 0], [0, 2, 0], [0, 3, 0], [1, 2, 1], [1, 3, 1], [2, 3, 2],
         [0, 1, 2, 0], [0, 1, 3, 0], [0, 2, 1, 0], [0, 2, 3, 0],
         [0, 3, 1, 0], [0, 3, 2, 0], [1, 2, 3, 1], [1, 3, 2, 1],
         [0, 1, 2, 3, 0], [0, 1, 3, 2, 0], [0, 2, 1, 3, 0],
         [0, 2, 3, 1, 0], [0, 3, 1, 2, 0], [0, 3, 2, 1, 0]]

    If the graph contains a large number of cycles, one can bound the length
    of the cycles, or simply restrict the possible starting vertices of the
    cycles::

        sage: g = graphs.CompleteGraph(20).to_directed()
        sage: g.all_simple_cycles(max_length=2)
        [[0, 1, 0], [0, 2, 0], [0, 3, 0], [0, 4, 0], [0, 5, 0], [0, 6, 0], [0, 7, 0],
         [0, 8, 0], [0, 9, 0], [0, 10, 0], [0, 11, 0], [0, 12, 0], [0, 13, 0],
         [0, 14, 0], [0, 15, 0], [0, 16, 0], [0, 17, 0], [0, 18, 0], [0, 19, 0],
         [1, 2, 1], [1, 3, 1], [1, 4, 1], [1, 5, 1], [1, 6, 1], [1, 7, 1], [1, 8, 1],
         [1, 9, 1], [1, 10, 1], [1, 11, 1], [1, 12, 1], [1, 13, 1], [1, 14, 1],
         [1, 15, 1], [1, 16, 1], [1, 17, 1], [1, 18, 1], [1, 19, 1], [2, 3, 2],
         [2, 4, 2], [2, 5, 2], [2, 6, 2], [2, 7, 2], [2, 8, 2], [2, 9, 2], [2, 10, 2],
         [2, 11, 2], [2, 12, 2], [2, 13, 2], [2, 14, 2], [2, 15, 2], [2, 16, 2],
         [2, 17, 2], [2, 18, 2], [2, 19, 2], [3, 4, 3], [3, 5, 3], [3, 6, 3],
         [3, 7, 3], [3, 8, 3], [3, 9, 3], [3, 10, 3], [3, 11, 3], [3, 12, 3],
         [3, 13, 3], [3, 14, 3], [3, 15, 3], [3, 16, 3], [3, 17, 3], [3, 18, 3],
         [3, 19, 3], [4, 5, 4], [4, 6, 4], [4, 7, 4], [4, 8, 4], [4, 9, 4], [4, 10, 4],
         [4, 11, 4], [4, 12, 4], [4, 13, 4], [4, 14, 4], [4, 15, 4], [4, 16, 4],
         [4, 17, 4], [4, 18, 4], [4, 19, 4], [5, 6, 5], [5, 7, 5], [5, 8, 5],
         [5, 9, 5], [5, 10, 5], [5, 11, 5], [5, 12, 5], [5, 13, 5], [5, 14, 5],
         [5, 15, 5], [5, 16, 5], [5, 17, 5], [5, 18, 5], [5, 19, 5], [6, 7, 6],
         [6, 8, 6], [6, 9, 6], [6, 10, 6], [6, 11, 6], [6, 12, 6], [6, 13, 6],
         [6, 14, 6], [6, 15, 6], [6, 16, 6], [6, 17, 6], [6, 18, 6], [6, 19, 6],
         [7, 8, 7], [7, 9, 7], [7, 10, 7], [7, 11, 7], [7, 12, 7], [7, 13, 7],
         [7, 14, 7], [7, 15, 7], [7, 16, 7], [7, 17, 7], [7, 18, 7], [7, 19, 7],
         [8, 9, 8], [8, 10, 8], [8, 11, 8], [8, 12, 8], [8, 13, 8], [8, 14, 8],
         [8, 15, 8], [8, 16, 8], [8, 17, 8], [8, 18, 8], [8, 19, 8], [9, 10, 9],
         [9, 11, 9], [9, 12, 9], [9, 13, 9], [9, 14, 9], [9, 15, 9], [9, 16, 9],
         [9, 17, 9], [9, 18, 9], [9, 19, 9], [10, 11, 10], [10, 12, 10], [10, 13, 10],
         [10, 14, 10], [10, 15, 10], [10, 16, 10], [10, 17, 10], [10, 18, 10],
         [10, 19, 10], [11, 12, 11], [11, 13, 11], [11, 14, 11], [11, 15, 11],
         [11, 16, 11], [11, 17, 11], [11, 18, 11], [11, 19, 11], [12, 13, 12],
         [12, 14, 12], [12, 15, 12], [12, 16, 12], [12, 17, 12], [12, 18, 12],
         [12, 19, 12], [13, 14, 13], [13, 15, 13], [13, 16, 13], [13, 17, 13],
         [13, 18, 13], [13, 19, 13], [14, 15, 14], [14, 16, 14], [14, 17, 14],
         [14, 18, 14], [14, 19, 14], [15, 16, 15], [15, 17, 15], [15, 18, 15],
         [15, 19, 15], [16, 17, 16], [16, 18, 16], [16, 19, 16], [17, 18, 17],
         [17, 19, 17], [18, 19, 18]]

        sage: g = graphs.CompleteGraph(20).to_directed()
        sage: g.all_simple_cycles(max_length=2, starting_vertices=[0])
        [[0, 1, 0], [0, 2, 0], [0, 3, 0], [0, 4, 0], [0, 5, 0],
         [0, 6, 0], [0, 7, 0], [0, 8, 0], [0, 9, 0], [0, 10, 0],
         [0, 11, 0], [0, 12, 0], [0, 13, 0], [0, 14, 0], [0, 15, 0],
         [0, 16, 0], [0, 17, 0], [0, 18, 0], [0, 19, 0]]

    One may prefer to distinguish equivalent cycles having distinct starting
    vertices (compare the following examples)::

        sage: g = graphs.CompleteGraph(4).to_directed()
        sage: g.all_simple_cycles(max_length=2, rooted=False)
        [[0, 1, 0], [0, 2, 0], [0, 3, 0], [1, 2, 1], [1, 3, 1], [2, 3, 2]]
        sage: g.all_simple_cycles(max_length=2, rooted=True)
        [[0, 1, 0], [0, 2, 0], [0, 3, 0], [1, 0, 1], [1, 2, 1], [1, 3, 1],
         [2, 0, 2], [2, 1, 2], [2, 3, 2], [3, 0, 3], [3, 1, 3], [3, 2, 3]]

    A cycle is enumerated in increasing length order for a weighted graph::

        sage: cycles = g.all_simple_cycles(weight_function=lambda e:e[0]+e[1],
        ....:                              by_weight=True, report_weight=True)
        sage: cycles
        [(2, [0, 1, 0]), (4, [0, 2, 0]), (6, [0, 1, 2, 0]), (6, [0, 2, 1, 0]),
         (6, [0, 3, 0]), (6, [1, 2, 1]), (8, [0, 1, 3, 0]), (8, [0, 3, 1, 0]),
         (8, [1, 3, 1]), (10, [0, 2, 3, 0]), (10, [0, 3, 2, 0]), (10, [2, 3, 2]),
         (12, [0, 1, 2, 3, 0]), (12, [0, 1, 3, 2, 0]), (12, [0, 2, 1, 3, 0]),
         (12, [0, 2, 3, 1, 0]), (12, [0, 3, 1, 2, 0]), (12, [0, 3, 2, 1, 0]),
         (12, [1, 2, 3, 1]), (12, [1, 3, 2, 1])]

    The algorithm ``'B'`` can be used::

        sage: cycles_B = g.all_simple_cycles(weight_function=lambda e:e[0]+e[1], by_weight=True,
        ....:                                report_weight=True, algorithm='B')
        sage: cycles_B
        [(2, [0, 1, 0]), (4, [0, 2, 0]), (6, [0, 1, 2, 0]), (6, [0, 2, 1, 0]),
         (6, [0, 3, 0]), (6, [1, 2, 1]), (8, [0, 1, 3, 0]), (8, [0, 3, 1, 0]),
         (8, [1, 3, 1]), (10, [0, 2, 3, 0]), (10, [0, 3, 2, 0]), (10, [2, 3, 2]),
         (12, [0, 1, 3, 2, 0]), (12, [0, 1, 2, 3, 0]), (12, [0, 2, 3, 1, 0]),
         (12, [0, 2, 1, 3, 0]), (12, [0, 3, 2, 1, 0]), (12, [0, 3, 1, 2, 0]),
         (12, [1, 2, 3, 1]), (12, [1, 3, 2, 1])]
        sage: cycles.sort() == cycles_B.sort()
        True

    The algorithm ``'A'`` is available only for directed graphs::

        sage: g = Graph({0: [1, 2], 1: [0, 2], 2: [0, 1]})
        sage: g.all_simple_cycles(algorithm='A')
        Traceback (most recent call last):
        ...
        ValueError: The algorithm 'A' is available only for directed graphs.
    """
