from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.misc.cachefunc import cached_method as cached_method
from typing import Any, overload

class IndependentSets:
    """IndependentSets(G, maximal=False, complement=False)

    File: /build/sagemath/src/sage/src/sage/graphs/independent_sets.pyx (starting at line 31)

    The set of independent sets of a graph.

    For more information on independent sets, see the
    :wikipedia:`Independent_set_(graph_theory)`.

    INPUT:

    - ``G`` -- a graph

    - ``maximal`` -- boolean (default: ``False``); whether to only consider
      (inclusionwise) maximal independent sets

    - ``complement`` -- boolean (default: ``False``); whether to consider the
      graph's complement (i.e. cliques instead of independent sets)

    ALGORITHM:

    The enumeration of independent sets is done naively : given an independent
    set, this implementation considers all ways to add a new vertex to it
    (while keeping it an independent set), and then creates new independent
    sets from all those that were created this way.

    The implementation, however, is not recursive.

    .. NOTE::

        This implementation of the enumeration of *maximal* independent sets is
        not much faster than NetworkX', which is surprising as it is written in
        Cython. This being said, the algorithm from NetworkX appears to be
        slightly different from this one, and that would be a good thing to
        explore if one wants to improve the implementation.

        A simple generalization can also be done without too much modifications:
        iteration through independent sets with given size bounds
        (minimum and maximum number of vertices allowed).

    EXAMPLES:

    Listing all independent sets of the Claw graph::

        sage: from sage.graphs.independent_sets import IndependentSets
        sage: g = graphs.ClawGraph()
        sage: I = IndependentSets(g)
        sage: list(I)
        [[0], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3], []]

    Count them::

        sage: I.cardinality()
        9

    List only the maximal independent sets::

        sage: Im = IndependentSets(g, maximal=True)
        sage: list(Im)
        [[0], [1, 2, 3]]

    And count them::

        sage: Im.cardinality()
        2

    One can easily count the number of independent sets of each cardinality::

        sage: g = graphs.PetersenGraph()
        sage: number_of = [0] * g.order()
        sage: for x in IndependentSets(g):
        ....:     number_of[len(x)] += 1
        sage: number_of
        [1, 10, 30, 30, 5, 0, 0, 0, 0, 0]

    It is also possible to define an iterator over all independent sets of a
    given cardinality. Note, however, that Sage will generate them *all*, to
    return only those that satisfy the cardinality constraints. Getting the list
    of independent sets of size 4 in this way can thus take a very long time::

        sage: is4 = (x for x in IndependentSets(g) if len(x) == 4)
        sage: list(is4)
        [[0, 2, 8, 9], [0, 3, 6, 7], [1, 3, 5, 9], [1, 4, 7, 8], [2, 4, 5, 6]]

    Given a subset of the vertices, it is possible to test whether it is an
    independent set::

        sage: g = graphs.DurerGraph()
        sage: I = IndependentSets(g)
        sage: [0, 2] in I
        True
        sage: [0, 3, 5] in I
        False

    If an element of the subset is not a vertex, then an error is raised::

        sage: [0, 'a', 'b', 'c'] in I
        Traceback (most recent call last):
        ...
        ValueError: a is not a vertex of the graph"""
    def __init__(self, G, maximal=..., complement=...) -> Any:
        '''File: /build/sagemath/src/sage/src/sage/graphs/independent_sets.pyx (starting at line 130)

                Constructor for this class.

                TESTS::

                    sage: from sage.graphs.independent_sets import IndependentSets
                    sage: IndependentSets(graphs.PetersenGraph())
                    <sage.graphs.independent_sets.IndependentSets object...

                Compute the number of matchings, and check with Sage\'s implementation::

                    sage: from sage.graphs.independent_sets import IndependentSets
                    sage: from sage.graphs.matchpoly import matching_polynomial                 # needs sage.libs.flint
                    sage: def check_matching(G):
                    ....:     number_of_matchings = sum(map(abs, matching_polynomial(G).coefficients(sparse=False)))
                    ....:     if number_of_matchings != IndependentSets(G.line_graph()).cardinality():
                    ....:         raise ValueError("something goes wrong")
                    sage: for i in range(30):                                                   # needs sage.libs.flint
                    ....:     check_matching(graphs.RandomGNP(11, .3))

                Compare the result with the output of :meth:`subgraph_search`::

                    sage: from sage.sets.set import Set
                    sage: def check_with_subgraph_search(G):
                    ....:     IS = set(map(Set, list(IndependentSets(G))))
                    ....:     if not all(G.subgraph(l).is_independent_set() for l in IS):
                    ....:        print("Gloops")
                    ....:     alpha = max(map(len, IS))
                    ....:     IS2 = [Set([x]) for x in range(G.order())] + [Set()]
                    ....:     for n in range(2, alpha + 1):
                    ....:         IS2.extend(map(Set, list(G.subgraph_search_iterator(Graph(n), induced=True, return_graphs=False))))
                    ....:     if len(IS) != len(set(IS2)):
                    ....:        raise ValueError("something goes wrong")
                    sage: for i in range(5):                                                    # needs sage.modules
                    ....:     check_with_subgraph_search(graphs.RandomGNP(11, .3))

                Empty graph::

                    sage: IS0 = IndependentSets(graphs.EmptyGraph())
                    sage: list(IS0)
                    [[]]
                    sage: IS0.cardinality()
                    1
        '''
    @overload
    def cardinality(self) -> Any:
        """IndependentSets.cardinality(self)

        File: /build/sagemath/src/sage/src/sage/graphs/independent_sets.pyx (starting at line 301)

        Compute and return the number of independent sets.

        TESTS::

            sage: from sage.graphs.independent_sets import IndependentSets
            sage: IndependentSets(graphs.PetersenGraph()).cardinality()
            76

        Only maximal ones::

            sage: from sage.graphs.independent_sets import IndependentSets
            sage: IndependentSets(graphs.PetersenGraph(), maximal=True).cardinality()
            15"""
    @overload
    def cardinality(self) -> Any:
        """IndependentSets.cardinality(self)

        File: /build/sagemath/src/sage/src/sage/graphs/independent_sets.pyx (starting at line 301)

        Compute and return the number of independent sets.

        TESTS::

            sage: from sage.graphs.independent_sets import IndependentSets
            sage: IndependentSets(graphs.PetersenGraph()).cardinality()
            76

        Only maximal ones::

            sage: from sage.graphs.independent_sets import IndependentSets
            sage: IndependentSets(graphs.PetersenGraph(), maximal=True).cardinality()
            15"""
    @overload
    def cardinality(self) -> Any:
        """IndependentSets.cardinality(self)

        File: /build/sagemath/src/sage/src/sage/graphs/independent_sets.pyx (starting at line 301)

        Compute and return the number of independent sets.

        TESTS::

            sage: from sage.graphs.independent_sets import IndependentSets
            sage: IndependentSets(graphs.PetersenGraph()).cardinality()
            76

        Only maximal ones::

            sage: from sage.graphs.independent_sets import IndependentSets
            sage: IndependentSets(graphs.PetersenGraph(), maximal=True).cardinality()
            15"""
    def __contains__(self, S) -> Any:
        """IndependentSets.__contains__(self, S)

        File: /build/sagemath/src/sage/src/sage/graphs/independent_sets.pyx (starting at line 331)

        Check whether the set is an independent set (possibly maximal).

        INPUT:

        - ``S`` -- set of vertices to be tested

        TESTS:

        All independent sets of PetersenGraph are... independent sets::

            sage: from sage.graphs.independent_sets import IndependentSets
            sage: G = graphs.PetersenGraph()
            sage: IS = IndependentSets(graphs.PetersenGraph())
            sage: all(s in IS for s in IS)
            True

        And only them are::

            sage: IS2 = [x for x in subsets(G) if x in IS]
            sage: sorted(IS) == sorted(IS2)
            True

        Same with maximal independent sets::

            sage: IS = IndependentSets(graphs.PetersenGraph(), maximal=True)
            sage: S = Subsets(G)
            sage: all(s in IS for s in IS)
            True
            sage: IS2 = [x for x in subsets(G) if x in IS]
            sage: sorted(IS) == sorted(IS2)
            True

        Check that the empty graph is dealt with correctly::

            sage: IS = IndependentSets(Graph())
            sage: [] in IS
            True"""
    def __iter__(self) -> Any:
        """IndependentSets.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/graphs/independent_sets.pyx (starting at line 192)

        Return an iterator over the independent sets of ``self``.

        TESTS::

            sage: from sage.graphs.independent_sets import IndependentSets
            sage: I = IndependentSets(graphs.PetersenGraph())
            sage: iter1 = iter(I)
            sage: iter2 = iter(I)
            sage: next(iter1)      # indirect doctest
            [0]
            sage: next(iter2)      # indirect doctest
            [0]
            sage: next(iter2)
            [0, 2]
            sage: next(iter1)
            [0, 2]"""
