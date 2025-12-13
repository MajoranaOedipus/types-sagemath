from _typeshed import Incomplete
from collections.abc import Generator

def subsets_with_hereditary_property(f, X, max_obstruction_size=None, ncpus: int = 1) -> Generator[Incomplete, None, Incomplete]:
    """
    Return all subsets `S` of `X` such that `f(S)` is true.

    The boolean function `f` must be decreasing, i.e. `f(S)\\Rightarrow f(S')` if
    `S'\\subseteq S`.

    This function is implemented to call `f` as few times as possible. More
    precisely, `f` will be called on all sets `S` such that `f(S)` is true, as
    well as on all inclusionwise minimal sets `S` such that `f(S)` is false.

    The problem that this function answers is also known as the learning problem
    on monotone boolean functions, or as computing the set of winning coalitions
    in a simple game.

    INPUT:

    - ``f`` -- boolean function which takes as input a list of elements from
      ``X``

    - ``X`` -- list/iterable

    - ``max_obstruction_size`` -- integer; if you know that there is
      a `k` such that `f(S)` is true if and only if `f(S')` is true
      for all `S'\\subseteq S` with `S'\\leq k`, set
      ``max_obstruction_size=k``. It may dramatically decrease the
      number of calls to `f`. Set to ``None`` by default, meaning
      `k=|X|`.

    - ``ncpus`` -- number of cpus to use for this computation. Note that
      changing the value from `1` (default) to anything different *enables*
      parallel computations which can have a cost by itself, so it is not
      necessarily a good move. In some cases, however, it is a *great* move. Set
      to ``None`` to automatically detect and use the maximum number of cpus
      available.

      .. NOTE::

          Parallel computations are performed through the
          :func:`~sage.parallel.decorate.parallel` decorator. See its
          documentation for more information, in particular with respect to the
          memory context.

    EXAMPLES:

    Sets whose elements all have the same remainder mod 2::

        sage: from sage.combinat.subsets_hereditary import subsets_with_hereditary_property
        sage: def f(x):
        ....:     return (not x) or all(xx % 2 == x[0] % 2 for xx in x)
        sage: list(subsets_with_hereditary_property(f, range(4)))
        [[], [0], [1], [2], [3], [0, 2], [1, 3]]

    Same, on two threads::

        sage: sorted(subsets_with_hereditary_property(f, range(4), ncpus=2))
        [[], [0], [0, 2], [1], [1, 3], [2], [3]]

    One can use this function to compute the independent sets of a graph. We
    know, however, that in this case the maximum obstructions are the edges, and
    have size 2. We can thus set ``max_obstruction_size=2``, which reduces the
    number of calls to `f` from 91 to 56::

        sage: # needs sage.graphs
        sage: num_calls = 0
        sage: g = graphs.PetersenGraph()
        sage: def is_independent_set(S):
        ....:     global num_calls
        ....:     num_calls += 1
        ....:     return g.subgraph(S).size() == 0
        sage: l1 = list(subsets_with_hereditary_property(is_independent_set,
        ....:                                            g.vertices(sort=False)))
        sage: num_calls
        91
        sage: num_calls = 0
        sage: l2 = list(subsets_with_hereditary_property(is_independent_set,
        ....:                                            g.vertices(sort=False),
        ....:                                            max_obstruction_size=2))
        sage: num_calls
        56
        sage: l1 == l2
        True

    TESTS::

        sage: list(subsets_with_hereditary_property(lambda x: False, range(4)))
        []
        sage: list(subsets_with_hereditary_property(lambda x: len(x)<1, range(4)))
        [[]]
        sage: list(subsets_with_hereditary_property(lambda x: True, range(2)))
        [[], [0], [1], [0, 1]]
    """
