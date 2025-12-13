from sage.graphs.graph import Graph as Graph

def IntervalGraph(intervals, points_ordered: bool = False):
    """
    Return the graph corresponding to the given intervals.

    An interval graph is built from a list `(a_i,b_i)_{1\\leq i \\leq n}` of
    intervals : to each interval of the list is associated one vertex, two
    vertices being adjacent if the two corresponding (closed) intervals
    intersect.

    INPUT:

    - ``intervals`` -- the list of pairs `(a_i,b_i)` defining the graph

    - ``points_ordered`` -- states whether every interval `(a_i,b_i)` of
      `intervals` satisfies `a_i<b_i`. If satisfied then setting
      ``points_ordered`` to ``True`` will speed up the creation of the graph.

    .. NOTE::

        * The vertices are named 0, 1, 2, and so on. The intervals used
          to create the graph are saved with the graph and can be recovered
          using ``get_vertex()`` or ``get_vertices()``.

    EXAMPLES:

    The following line creates the sequence of intervals
    `(i, i+2)` for i in `[0, ..., 8]`::

        sage: intervals = [(i,i+2) for i in range(9)]

    In the corresponding graph ::

        sage: g = graphs.IntervalGraph(intervals)
        sage: g.get_vertex(3)
        (3, 5)
        sage: neigh = g.neighbors(3)
        sage: for v in neigh: print(g.get_vertex(v))
        (1, 3)
        (2, 4)
        (4, 6)
        (5, 7)

    The is_interval() method verifies that this graph is an interval graph. ::

        sage: g.is_interval()
        True

    The intervals in the list need not be distinct. ::

        sage: intervals = [ (1,2), (1,2), (1,2), (2,3), (3,4) ]
        sage: g = graphs.IntervalGraph(intervals,True)
        sage: g.clique_maximum()
        [0, 1, 2, 3]
        sage: g.get_vertices()
        {0: (1, 2), 1: (1, 2), 2: (1, 2), 3: (2, 3), 4: (3, 4)}

    The endpoints of the intervals are not ordered we get the same graph
    (except for the vertex labels). ::

        sage: rev_intervals = [ (2,1), (2,1), (2,1), (3,2), (4,3) ]
        sage: h = graphs.IntervalGraph(rev_intervals,False)
        sage: h.get_vertices()
        {0: (2, 1), 1: (2, 1), 2: (2, 1), 3: (3, 2), 4: (4, 3)}
        sage: g.edges(sort=True) == h.edges(sort=True)
        True
    """
def PermutationGraph(second_permutation, first_permutation=None):
    '''
    Build a permutation graph from one permutation or from two lists.

    Definition:

    If `\\sigma` is a permutation of `\\{ 1, 2, \\ldots, n \\}`, then the
    permutation graph of `\\sigma` is the graph on vertex set
    `\\{ 1, 2, \\ldots, n \\}` in which two vertices `i` and `j` satisfying
    `i < j` are connected by an edge if and only if
    `\\sigma^{-1}(i) > \\sigma^{-1}(j)`. A visual way to construct this
    graph is as follows:

      Take two horizontal lines in the euclidean plane, and mark points
      `1, ..., n` from left to right on the first of them. On the second
      one, still from left to right, mark `n` points
      `\\sigma(1), \\sigma(2), \\ldots, \\sigma(n)`.
      Now, link by a segment the two points marked with `1`, then link
      together the points marked with `2`, and so on. The permutation
      graph of `\\sigma` is the intersection graph of those segments: there
      exists a vertex in this graph for each element from `1` to `n`, two
      vertices `i, j` being adjacent if the segments `i` and `j` cross
      each other.

    The set of edges of the permutation graph can thus be identified with
    the set of inversions of the inverse of the given permutation
    `\\sigma`.

    A more general notion of permutation graph can be defined as
    follows: If `S` is a set, and `(a_1, a_2, \\ldots, a_n)` and
    `(b_1, b_2, \\ldots, b_n)` are two lists of elements of `S`, each of
    which lists contains every element of `S` exactly once, then the
    permutation graph defined by these two lists is the graph on the
    vertex set `S` in which two vertices `i` and `j` are connected by an
    edge if and only if the order in which these vertices appear in the
    list `(a_1, a_2, \\ldots, a_n)` is the opposite of the order in which
    they appear in the list `(b_1, b_2, \\ldots, b_n)`. When
    `(a_1, a_2, \\ldots, a_n) = (1, 2, \\ldots, n)`, this graph is the
    permutation graph of the permutation
    `(b_1, b_2, \\ldots, b_n) \\in S_n`. Notice that `S` does not have to
    be a set of integers here, but can be a set of strings, tuples, or
    anything else. We can still use the above visual description to
    construct the permutation graph, but now we have to mark points
    `a_1, a_2, \\ldots, a_n` from left to right on the first horizontal
    line and points `b_1, b_2, \\ldots, b_n` from left to right on the
    second horizontal line.

    INPUT:

    - ``second_permutation`` -- the unique permutation/list defining the graph,
      or the second of the two (if the graph is to be built from two
      permutations/lists)

    - ``first_permutation`` -- (optional) the first of the two
      permutations/lists from which the graph should be built, if it is to be
      built from two permutations/lists

      When ``first_permutation is None`` (default), it is set to be equal to
      ``sorted(second_permutation)``, which yields the expected ordering when
      the elements of the graph are integers.

    .. SEEALSO::

      - Recognition of Permutation graphs in the :mod:`comparability module
        <sage.graphs.comparability>`.

      - Drawings of permutation graphs as intersection graphs of segments is
        possible through the
        :meth:`~sage.combinat.permutation.Permutation.show` method of
        :class:`~sage.combinat.permutation.Permutation` objects.

        The correct argument to use in this case is ``show(representation =
        "braid")``.

      - :meth:`~sage.combinat.permutation.Permutation.inversions`

    EXAMPLES::

        sage: p = Permutations(5).random_element()
        sage: PG = graphs.PermutationGraph(p)
        sage: edges = PG.edges(sort=True, labels=False)
        sage: set(edges) == set(p.inverse().inversions())
        True

        sage: PG = graphs.PermutationGraph([3,4,5,1,2])
        sage: sorted(PG.edges(sort=True))
        [(1, 3, None),
         (1, 4, None),
         (1, 5, None),
         (2, 3, None),
         (2, 4, None),
         (2, 5, None)]
        sage: PG = graphs.PermutationGraph([3,4,5,1,2], [1,4,2,5,3])
        sage: sorted(PG.edges(sort=True))
        [(1, 3, None),
         (1, 4, None),
         (1, 5, None),
         (2, 3, None),
         (2, 5, None),
         (3, 4, None),
         (3, 5, None)]
        sage: PG = graphs.PermutationGraph([1,4,2,5,3], [3,4,5,1,2])
        sage: sorted(PG.edges(sort=True))
        [(1, 3, None),
         (1, 4, None),
         (1, 5, None),
         (2, 3, None),
         (2, 5, None),
         (3, 4, None),
         (3, 5, None)]

        sage: PG = graphs.PermutationGraph(Permutation([1,3,2]), Permutation([1,2,3]))
        sage: sorted(PG.edges(sort=True))
        [(2, 3, None)]

        sage: graphs.PermutationGraph([]).edges(sort=True)
        []
        sage: graphs.PermutationGraph([], []).edges(sort=True)
        []

        sage: PG = graphs.PermutationGraph("graph", "phrag")
        sage: sorted(PG.edges(sort=True))
        [(\'a\', \'g\', None),
         (\'a\', \'h\', None),
         (\'a\', \'p\', None),
         (\'g\', \'h\', None),
         (\'g\', \'p\', None),
         (\'g\', \'r\', None),
         (\'h\', \'r\', None),
         (\'p\', \'r\', None)]

    TESTS::

        sage: graphs.PermutationGraph([1, 2, 3], [4, 5, 6])
        Traceback (most recent call last):
        ...
        ValueError: The two permutations do not contain the same set of elements ...
    '''
def ToleranceGraph(tolrep):
    """
    Return the graph generated by the tolerance representation ``tolrep``.

    The tolerance representation ``tolrep`` is described by the list
    `((l_0,r_0,t_0), (l_1,r_1,t_1), \\ldots, (l_k,r_k,t_k))` where `I_i =
    (l_i,r_i)` denotes a closed interval on the real line with `l_i < r_i` and
    `t_i` a strictly positive value, called tolerance. This representation
    generates the tolerance graph with the vertex set `\\{0,1, \\ldots, k\\}` and
    the edge set `\\{(i,j): |I_i \\cap I_j| \\ge \\min\\{t_i, t_j\\}\\}` where `|I_i
    \\cap I_j|` denotes the length of the intersection of `I_i` and `I_j`.

    INPUT:

    - ``tolrep`` -- list of triples `(l_i,r_i,t_i)` where `(l_i,r_i)` denotes a
      closed interval on the real line and `t_i` a positive value

    .. NOTE::

        The vertices are named `0, 1, \\ldots, k`. The tolerance representation
        used to create the graph is saved with the graph and can be recovered
        using ``get_vertex()`` or ``get_vertices()``.

    EXAMPLES:

    The following code creates a tolerance representation ``tolrep``, generates
    its tolerance graph ``g``, and applies some checks::

        sage: tolrep = [(1,4,3),(1,2,1),(2,3,1),(0,3,3)]
        sage: g = graphs.ToleranceGraph(tolrep)
        sage: g.get_vertex(3)
        (0, 3, 3)
        sage: neigh = g.neighbors(3)
        sage: for v in neigh: print(g.get_vertex(v))
        (1, 2, 1)
        (2, 3, 1)
        sage: g.is_interval()
        False
        sage: g.is_weakly_chordal()
        True

    The intervals in the list need not be distinct ::

        sage: tolrep2 = [(0,4,5),(1,2,1),(2,3,1),(0,4,5)]
        sage: g2 = graphs.ToleranceGraph(tolrep2)
        sage: g2.get_vertices()
        {0: (0, 4, 5), 1: (1, 2, 1), 2: (2, 3, 1), 3: (0, 4, 5)}
        sage: g2.is_isomorphic(g)
        True

    Real values are also allowed ::

        sage: tolrep = [(0.1,3.3,4.4),(1.1,2.5,1.1),(1.4,4.4,3.3)]
        sage: g = graphs.ToleranceGraph(tolrep)
        sage: g.is_isomorphic(graphs.PathGraph(3))
        True

    TESTS:

    Giving negative third value::

        sage: tolrep = [(0.1,3.3,-4.4),(1.1,2.5,1.1),(1.4,4.4,3.3)]
        sage: g = graphs.ToleranceGraph(tolrep)
        Traceback (most recent call last):
        ...
        ValueError: Invalid tolerance representation at position 0; third value must be > 0
        sage: g = graphs.ToleranceGraph([(1, 2, 0)])
        Traceback (most recent call last):
        ...
        ValueError: Invalid tolerance representation at position 0; third value must be  > 0
    """
def OrthogonalArrayBlockGraph(k, n, OA=None):
    """
    Return the graph of an `OA(k,n)`.

    The intersection graph of the blocks of a transversal design with parameters
    `(k,n)`, or `TD(k,n)` for short, is a strongly regular graph (unless it is a
    complete graph). Its parameters `(v,k',\\lambda,\\mu)` are determined by the
    parameters `k,n` via:

    .. MATH::

        v=n^2, k'=k(n-1), \\lambda=(k-1)(k-2)+n-2, \\mu=k(k-1)

    As transversal designs and orthogonal arrays (OA for short) are equivalent
    objects, this graph can also be built from the blocks of an `OA(k,n)`, two
    of them being adjacent if one of their coordinates match.

    For more information on these graphs, see `Andries Brouwer's page
    on Orthogonal Array graphs <https://www.win.tue.nl/~aeb/graphs/OA.html>`_.

    .. WARNING::

        - Brouwer's website uses the notation `OA(n,k)` instead of `OA(k,n)`

        - For given parameters `k` and `n` there can be many `OA(k,n)` : the
          graphs returned are not uniquely defined by their parameters (see the
          examples below).

        - If the function is called only with the parameter ``k`` and ``n`` the
          results might be different with two versions of Sage, or even worse :
          some could not be available anymore.

    .. SEEALSO::

        :mod:`sage.combinat.designs.orthogonal_arrays`

    INPUT:

    - ``k``, ``n`` -- integers

    - ``OA`` -- an orthogonal array; if set to ``None`` (default) then
      :func:`~sage.combinat.designs.orthogonal_arrays.orthogonal_array` is
      called to compute an `OA(k,n)`

    EXAMPLES::

        sage: # needs sage.modules
        sage: G = graphs.OrthogonalArrayBlockGraph(5,5); G                              # needs sage.schemes
        OA(5,5): Graph on 25 vertices
        sage: G.is_strongly_regular(parameters=True)                                    # needs sage.schemes
        (25, 20, 15, 20)
        sage: G = graphs.OrthogonalArrayBlockGraph(4,10); G
        OA(4,10): Graph on 100 vertices
        sage: G.is_strongly_regular(parameters=True)
        (100, 36, 14, 12)

    Two graphs built from different orthogonal arrays are also different::

        sage: # needs sage.modules
        sage: k = 4; n = 10
        sage: OAa = designs.orthogonal_arrays.build(k,n)
        sage: OAb = [[(x+1)%n for x in R] for R in OAa]
        sage: set(map(tuple,OAa)) == set(map(tuple,OAb))
        False
        sage: Ga = graphs.OrthogonalArrayBlockGraph(k, n, OAa)
        sage: Gb = graphs.OrthogonalArrayBlockGraph(k, n, OAb)
        sage: Ga == Gb
        False

    As ``OAb`` was obtained from ``OAa`` by a relabelling the two graphs are
    isomorphic::

        sage: Ga.is_isomorphic(Gb)                                                      # needs sage.modules
        True

    But there are examples of `OA(k,n)` for which the resulting graphs are not
    isomorphic::

        sage: oa0 = [[0, 0, 1], [0, 1, 3], [0, 2, 0], [0, 3, 2],
        ....:        [1, 0, 3], [1, 1, 1], [1, 2, 2], [1, 3, 0],
        ....:        [2, 0, 0], [2, 1, 2], [2, 2, 1], [2, 3, 3],
        ....:        [3, 0, 2], [3, 1, 0], [3, 2, 3], [3, 3, 1]]
        sage: oa1 = [[0, 0, 1], [0, 1, 0], [0, 2, 3], [0, 3, 2],
        ....:        [1, 0, 3], [1, 1, 2], [1, 2, 0], [1, 3, 1],
        ....:        [2, 0, 0], [2, 1, 1], [2, 2, 2], [2, 3, 3],
        ....:        [3, 0, 2], [3, 1, 3], [3, 2, 1], [3, 3, 0]]
        sage: g0 = graphs.OrthogonalArrayBlockGraph(3, 4, oa0)                          # needs sage.modules
        sage: g1 = graphs.OrthogonalArrayBlockGraph(3, 4, oa1)                          # needs sage.modules
        sage: g0.is_isomorphic(g1)                                                      # needs sage.modules
        False

    But nevertheless isospectral::

        sage: g0.spectrum()                                                             # needs sage.modules sage.rings.number_field
        [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, -3, -3, -3, -3, -3, -3]
        sage: g1.spectrum()                                                             # needs sage.modules sage.rings.number_field
        [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, -3, -3, -3, -3, -3, -3]

    Note that the graph ``g0`` is actually isomorphic to the affine polar graph
    `VO^+(4,2)`::

        sage: graphs.AffineOrthogonalPolarGraph(4,2,'+').is_isomorphic(g0)              # needs sage.libs.gap sage.modules
        True

    TESTS::

        sage: G = graphs.OrthogonalArrayBlockGraph(4,6)                                 # needs sage.modules sage.schemes
        Traceback (most recent call last):
        ...
        NotImplementedError: I don't know how to build an OA(4,6)!
        sage: G = graphs.OrthogonalArrayBlockGraph(8,2)                                 # needs sage.modules
        Traceback (most recent call last):
        ...
        ValueError: There is no OA(8,2). Beware, Brouwer's website uses OA(n,k) instead of OA(k,n) !
    """
def IntersectionGraph(S):
    """
    Return the intersection graph of the family `S`.

    The intersection graph of a family `S` is a graph `G` with `V(G)=S` such
    that two elements `s_1,s_2\\in S` are adjacent in `G` if and only if `s_1\\cap
    s_2\\neq \\emptyset`.

    INPUT:

    - ``S`` -- list of sets/tuples/iterables

        .. NOTE::

            The elements of `S` must be finite, hashable, and the elements of
            any `s\\in S` must be hashable too.

    EXAMPLES::

        sage: graphs.IntersectionGraph([(1,2,3),(3,4,5),(5,6,7)])
        Intersection Graph: Graph on 3 vertices

    TESTS::

        sage: graphs.IntersectionGraph([(1,2,[1])])
        Traceback (most recent call last):
        ...
        TypeError: The elements of S must be hashable, and this one is not: (1, 2, [1])
    """
