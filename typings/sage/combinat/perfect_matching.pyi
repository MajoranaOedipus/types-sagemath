from _typeshed import Incomplete
from collections.abc import Generator
from sage.combinat.combinat_cython import perfect_matchings_iterator as perfect_matchings_iterator
from sage.combinat.partition import Partition as Partition
from sage.combinat.permutation import Permutation as Permutation, Permutations as Permutations
from sage.combinat.set_partition import SetPartition as SetPartition, SetPartitions_set as SetPartitions_set
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod
from sage.rings.infinity import infinity as infinity
from sage.rings.integer import Integer as Integer
from sage.sets.set import Set as Set
from sage.structure.list_clone import ClonableArray as ClonableArray

class PerfectMatching(SetPartition):
    """
    A perfect matching.

    A *perfect matching* of a set `X` is a set partition of `X` where
    all parts have size 2.

    A perfect matching can be created from a list of pairs or from a
    fixed point-free involution as follows::

        sage: m = PerfectMatching([('a','e'),('b','c'),('d','f')]);m
        [('a', 'e'), ('b', 'c'), ('d', 'f')]
        sage: n = PerfectMatching([3,8,1,7,6,5,4,2]);n
        [(1, 3), (2, 8), (4, 7), (5, 6)]
        sage: isinstance(m,PerfectMatching)
        True

    The parent, which is the set of perfect matchings of the ground set, is
    automatically created::

        sage: n.parent()
        Perfect matchings of {1, 2, 3, 4, 5, 6, 7, 8}

    If the ground set is ordered, one can, for example, ask if the matching is
    non crossing::

        sage: PerfectMatching([(1, 4), (2, 3), (5, 6)]).is_noncrossing()
        True

    TESTS::

        sage: m = PerfectMatching([]); m
        []
        sage: m.parent()
        Perfect matchings of {}
    """
    @staticmethod
    def __classcall_private__(cls, parts):
        """
        Create a perfect matching from ``parts`` with the appropriate parent.

        This function tries to recognize the input (it can be either a list or
        a tuple of pairs, or a fix-point free involution given as a list or as
        a permutation), constructs the parent (enumerated set of
        PerfectMatchings of the ground set) and calls the __init__ function to
        construct our object.

        EXAMPLES::

            sage: m = PerfectMatching([('a','e'),('b','c'),('d','f')]);m
            [('a', 'e'), ('b', 'c'), ('d', 'f')]
            sage: isinstance(m, PerfectMatching)
            True
            sage: n = PerfectMatching([3, 8, 1, 7, 6, 5, 4, 2]);n
            [(1, 3), (2, 8), (4, 7), (5, 6)]
            sage: n.parent()
            Perfect matchings of {1, 2, 3, 4, 5, 6, 7, 8}
            sage: PerfectMatching([(1, 4), (2, 3), (5, 6)]).is_noncrossing()
            True

        The function checks that the given list or permutation is
        a valid perfect matching (i.e. a list of pairs with pairwise
        disjoint elements or a fix point free involution) and raises
        a :exc:`ValueError` otherwise::

            sage: PerfectMatching([(1, 2, 3), (4, 5)])
            Traceback (most recent call last):
            ...
            ValueError: [(1, 2, 3), (4, 5)] is not an element of
             Perfect matchings of {1, 2, 3, 4, 5}

        TESTS::

            sage: m = PerfectMatching([('a','e'),('b','c'),('d','f')])
            sage: TestSuite(m).run()
            sage: m = PerfectMatching([])
            sage: TestSuite(m).run()
            sage: PerfectMatching(6)
            Traceback (most recent call last):
            ...
            TypeError: 'sage.rings.integer.Integer' object is not iterable
            sage: PerfectMatching([(1,2,3)])
            Traceback (most recent call last):
            ...
            ValueError: [(1, 2, 3)] is not an element of
             Perfect matchings of {1, 2, 3}

            sage: PerfectMatching([(1,1)])
            Traceback (most recent call last):
            ...
            ValueError: [(1)] is not an element of Perfect matchings of {1}

            sage: PerfectMatching(Permutation([4,2,1,3]))
            Traceback (most recent call last):
            ...
            ValueError: permutation p (= [4, 2, 1, 3]) is not a
             fixed point free involution
        """
    def __init__(self, parent, s, check: bool = True, sort: bool = True) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: PM = PerfectMatchings(6)
            sage: x = PM.element_class(PM, [[5,6],[3,4],[1,2]])

        Use the ``sort`` argument when you do not care if the result
        is sorted. Be careful with its use as you can get inconsistent
        results when then input is not sorted::

            sage: y = PM.element_class(PM, [[5,6],[3,4],[1,2]], sort=False)
            sage: y
            [(5, 6), (3, 4), (1, 2)]
            sage: x == y
            False
        """
    def standardization(self):
        """
        Return the standardization of ``self``.

        See :meth:`SetPartition.standardization` for details.

        EXAMPLES::

            sage: n = PerfectMatching([('c','b'),('d','f'),('e','a')])
            sage: n.standardization()
            [(1, 5), (2, 3), (4, 6)]
        """
    def partner(self, x):
        """
        Return the element in the same pair than ``x``
        in the matching ``self``.

        EXAMPLES::

            sage: m = PerfectMatching([(-3, 1), (2, 4), (-2, 7)])
            sage: m.partner(4)
            2
            sage: n = PerfectMatching([('c','b'),('d','f'),('e','a')])
            sage: n.partner('c')
            'b'
        """
    def loops_iterator(self, other=None) -> Generator[Incomplete]:
        """
        Iterate through the loops of ``self``.

        INPUT:

        - ``other`` -- a perfect matching of the same set of ``self``
          (if the second argument is empty, the method :meth:`an_element` is
          called on the parent of the first)

        OUTPUT:

        If we draw the two perfect matchings simultaneously as edges of a
        graph, the graph obtained is a union of cycles of even lengths.
        The function returns an iterator for these cycles (each cycle is
        given as a list).

        EXAMPLES::

            sage: o = PerfectMatching([(1, 7), (2, 4), (3, 8), (5, 6)])
            sage: p = PerfectMatching([(1, 6), (2, 7), (3, 4), (5, 8)])
            sage: it = o.loops_iterator(p)
            sage: next(it)
            [1, 7, 2, 4, 3, 8, 5, 6]
            sage: next(it)
            Traceback (most recent call last):
            ...
            StopIteration
        """
    def loops(self, other=None):
        """
        Return the loops of ``self``.

        INPUT:

        - ``other`` -- a perfect matching of the same set of ``self``
          (if the second argument is empty, the method :meth:`an_element` is
          called on the parent of the first)

        OUTPUT:

        If we draw the two perfect matchings simultaneously as edges of a
        graph, the graph obtained is a union of cycles of even lengths.
        The function returns the list of these cycles (each cycle is given
        as a list).

        EXAMPLES::

            sage: m = PerfectMatching([('a','e'),('b','c'),('d','f')])
            sage: n = PerfectMatching([('a','b'),('d','f'),('e','c')])
            sage: loops = m.loops(n)
            sage: loops # random
            [['a', 'e', 'c', 'b'], ['d', 'f']]

            sage: o = PerfectMatching([(1, 7), (2, 4), (3, 8), (5, 6)])
            sage: p = PerfectMatching([(1, 6), (2, 7), (3, 4), (5, 8)])
            sage: o.loops(p)
            [[1, 7, 2, 4, 3, 8, 5, 6]]

        TESTS:

        Test whether the shorter element of ``loops`` is ``['d', 'f']``
        and the longer element is the cycle ``['a', 'e', 'c', 'b']`` or
        its reverse, or one of their cyclic permutations::

            sage: loops = sorted(loops, key=len)
            sage: sorted(loops[0])
            ['d', 'f']
            sage: G = SymmetricGroup(4)                                                 # needs sage.groups
            sage: g = G([(1,2,3,4)])                                                    # needs sage.groups
            sage: ((loops[1] in [permutation_action(g**i, ['a', 'e', 'c', 'b'])         # needs sage.groups
            ....:                for i in range(4)])
            ....:      or (loops[1] in [permutation_action(g**i, ['a', 'b', 'c', 'e'])
            ....:                       for i in range(4)]))
            True
        """
    def loop_type(self, other=None):
        """
        Return the loop type of ``self``.

        INPUT:

        - ``other`` -- a perfect matching of the same set of ``self``
          (if the second argument is empty, the method :meth:`an_element` is
          called on the parent of the first)

        OUTPUT:

        If we draw the two perfect matchings simultaneously as edges of a
        graph, the graph obtained is a union of cycles of even
        lengths. The function returns the ordered list of the semi-length
        of these cycles (considered as a partition)

        EXAMPLES::

            sage: m = PerfectMatching([('a','e'),('b','c'),('d','f')])
            sage: n = PerfectMatching([('a','b'),('d','f'),('e','c')])
            sage: m.loop_type(n)
            [2, 1]

        TESTS::

            sage: m = PerfectMatching([]); m.loop_type()
            []
        """
    def number_of_loops(self, other=None):
        """
        Return the number of loops of ``self``.

        INPUT:

        - ``other`` -- a perfect matching of the same set of ``self``
          (if the second argument is empty, the method :meth:`an_element` is
          called on the parent of the first)

        OUTPUT:

        If we draw the two perfect matchings simultaneously as edges of a
        graph, the graph obtained is a union of cycles of even lengths.
        The function returns their numbers.

        EXAMPLES::

            sage: m = PerfectMatching([('a','e'),('b','c'),('d','f')])
            sage: n = PerfectMatching([('a','b'),('d','f'),('e','c')])
            sage: m.number_of_loops(n)
            2
        """
    def Weingarten_function(self, d, other=None):
        """
        Return the Weingarten function of two pairings.

        This function is the value of some integrals over the orthogonal
        groups `O_N`.  With the convention of [CM]_, the method returns
        `Wg^{O(d)}(other,self)`.

        EXAMPLES::

            sage: var('N')                                                              # needs sage.symbolic
            N
            sage: m = PerfectMatching([(1,3),(2,4)])
            sage: n = PerfectMatching([(1,2),(3,4)])
            sage: factor(m.Weingarten_function(N, n))                                   # needs sage.symbolic
            -1/((N + 2)*(N - 1)*N)
        """
    def to_graph(self):
        """
        Return the graph corresponding to the perfect matching.

        OUTPUT: the realization of ``self`` as a graph

        EXAMPLES::

            sage: PerfectMatching([[1,3], [4,2]]).to_graph().edges(sort=True,           # needs sage.graphs
            ....:                                                  labels=False)
            [(1, 3), (2, 4)]
            sage: PerfectMatching([[1,4], [3,2]]).to_graph().edges(sort=True,           # needs sage.graphs
            ....:                                                  labels=False)
            [(1, 4), (2, 3)]
            sage: PerfectMatching([]).to_graph().edges(sort=True, labels=False)         # needs sage.graphs
            []
        """
    def to_noncrossing_set_partition(self):
        """
        Return the noncrossing set partition (on half as many elements)
        corresponding to the perfect matching if the perfect matching is
        noncrossing, and otherwise gives an error.

        OUTPUT: the realization of ``self`` as a noncrossing set partition

        EXAMPLES::

            sage: PerfectMatching([[1,3], [4,2]]).to_noncrossing_set_partition()
            Traceback (most recent call last):
            ...
            ValueError: matching must be non-crossing
            sage: PerfectMatching([[1,4], [3,2]]).to_noncrossing_set_partition()
            {{1, 2}}
            sage: PerfectMatching([]).to_noncrossing_set_partition()
            {}
        """

class PerfectMatchings(SetPartitions_set):
    """
    Perfect matchings of a ground set.

    INPUT:

    - ``s`` -- an iterable of hashable objects or an integer

    EXAMPLES:

    If the argument ``s`` is an integer `n`, it will be transformed
    into the set `\\{1, \\ldots, n\\}`::

        sage: M = PerfectMatchings(6); M
        Perfect matchings of {1, 2, 3, 4, 5, 6}
        sage: PerfectMatchings([-1, -3, 1, 2])
        Perfect matchings of {1, 2, -3, -1}

    One can ask for the list, the cardinality or an element of a set of
    perfect matching::

        sage: PerfectMatchings(4).list()
        [[(1, 2), (3, 4)], [(1, 3), (2, 4)], [(1, 4), (2, 3)]]
        sage: PerfectMatchings(8).cardinality()
        105
        sage: M = PerfectMatchings(('a', 'e', 'b', 'f', 'c', 'd'))
        sage: x = M.an_element()
        sage: x # random
        [('a', 'c'), ('b', 'e'), ('d', 'f')]
        sage: all(PerfectMatchings(i).an_element() in PerfectMatchings(i)
        ....:     for i in range(2,11,2))
        True

    TESTS:

    Test that ``x = M.an_element()`` is actually a perfect matching::

        sage: set().union(*x) == M.base_set()
        True
        sage: sum([len(a) for a in x]) == M.base_set().cardinality()
        True

        sage: M = PerfectMatchings(6)
        sage: TestSuite(M).run()

        sage: M = PerfectMatchings([])
        sage: M.list()
        [[]]
        sage: TestSuite(M).run()

        sage: PerfectMatchings(0).list()
        [[]]

        sage: M = PerfectMatchings(5)
        sage: M.list()
        []
        sage: TestSuite(M).run()

    ::

        sage: S = PerfectMatchings(4)
        sage: elt = S([[1,3],[2,4]]); elt
        [(1, 3), (2, 4)]
        sage: S = PerfectMatchings([])
        sage: S([])
        []
    """
    @staticmethod
    def __classcall_private__(cls, s):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: S = PerfectMatchings(4)
            sage: T = PerfectMatchings([1,2,3,4])
            sage: S is T
            True
        """
    def __iter__(self):
        """
        Iterate over ``self``.

        EXAMPLES::

            sage: PerfectMatchings(4).list()
            [[(1, 2), (3, 4)], [(1, 3), (2, 4)], [(1, 4), (2, 3)]]
        """
    def __contains__(self, x) -> bool:
        """
        Test if ``x`` is an element of ``self``.

        EXAMPLES::

            sage: m = PerfectMatching([(1,2),(4,3)])
            sage: m in PerfectMatchings(4)
            True
            sage: m in PerfectMatchings((0, 1, 2, 3))
            False
            sage: all(m in PerfectMatchings(6) for m in PerfectMatchings(6))
            True

        Note that the class of ``x`` does not need to be ``PerfectMatching``:
        if the data defines a perfect matching of the good set, the function
        returns ``True``::

            sage: [(1, 4), (2, 3)] in PerfectMatchings(4)
            True
            sage: [(1, 3, 6), (2, 4), (5,)] in PerfectMatchings(6)
            False
            sage: [('a', 'b'), ('a', 'c')] in PerfectMatchings(
            ....:      ('a', 'b', 'c', 'd'))
            False

        TESTS::

            sage: SA = PerfectMatchings([1,2,3,7])
            sage: Set([Set([1,2]),Set([3,7])]) in SA
            True
            sage: Set([Set([1,2]),Set([2,3])]) in SA
            False
            sage: Set([]) in SA
            False
        """
    def base_set(self):
        """
        Return the base set of ``self``.

        EXAMPLES::

            sage: PerfectMatchings(3).base_set()
            {1, 2, 3}
        """
    def base_set_cardinality(self):
        """
        Return the cardinality of the base set of ``self``.

        EXAMPLES::

            sage: PerfectMatchings(3).base_set_cardinality()
            3
        """
    def cardinality(self):
        """
        Return the cardinality of the set of perfect matchings ``self``.

        This is `1*3*5*...*(2n-1)`, where `2n` is the size of the ground set.

        EXAMPLES::

            sage: PerfectMatchings(8).cardinality()
            105
            sage: PerfectMatchings([1,2,3,4]).cardinality()
            3
            sage: PerfectMatchings(3).cardinality()
            0
            sage: PerfectMatchings([]).cardinality()
            1
        """
    def random_element(self):
        """
        Return a random element of ``self``.

        EXAMPLES::

            sage: M = PerfectMatchings(('a', 'e', 'b', 'f', 'c', 'd'))
            sage: x = M.random_element()
            sage: x # random
            [('a', 'b'), ('c', 'd'), ('e', 'f')]

        TESTS::

            sage: x in M
            True
            sage: p = PerfectMatchings(13).random_element()
            Traceback (most recent call last):
            ...
            ValueError: there is no perfect matching on an odd number of elements
        """
    @cached_method
    def Weingarten_matrix(self, N):
        """
        Return the Weingarten matrix corresponding to the set of
        PerfectMatchings ``self``.

        It is a useful theoretical tool to compute polynomial integrals
        over the orthogonal group `O_N` (see [CM]_).

        EXAMPLES::

            sage: M = PerfectMatchings(4).Weingarten_matrix(var('N'))                   # needs sage.symbolic
            sage: N*(N-1)*(N+2)*M.apply_map(factor)                                     # needs sage.symbolic
            [N + 1    -1    -1]
            [   -1 N + 1    -1]
            [   -1    -1 N + 1]
        """
    Element = PerfectMatching
