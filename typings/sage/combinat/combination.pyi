from .integer_vector import IntegerVectors as IntegerVectors
from _typeshed import Incomplete
from sage.arith.misc import binomial as binomial
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.parent import Parent as Parent

def Combinations(mset, k=None, *, as_tuples: bool = False):
    '''
    Return the combinatorial class of combinations of the multiset
    ``mset``. If ``k`` is specified, then it returns the combinatorial
    class of combinations of ``mset`` of size ``k``.

    A *combination* of a multiset `M` is an unordered selection of `k`
    objects of `M`, where every object can appear at most as many
    times as it appears in `M`.

    The boolean keyword ``as_tuples`` (default: ``False``) determines whether
    each combination is represented as a tuple or as a list.

    The combinatorial classes correctly handle the cases where ``mset`` has
    duplicate elements.

    EXAMPLES::

        sage: C = Combinations(range(4)); C
        Combinations of [0, 1, 2, 3]
        sage: C.list()
        [[],
         [0],
         [1],
         [2],
         [3],
         [0, 1],
         [0, 2],
         [0, 3],
         [1, 2],
         [1, 3],
         [2, 3],
         [0, 1, 2],
         [0, 1, 3],
         [0, 2, 3],
         [1, 2, 3],
         [0, 1, 2, 3]]
         sage: C.cardinality()
         16

    ::

        sage: C2 = Combinations(range(4),2); C2
        Combinations of [0, 1, 2, 3] of length 2
        sage: C2.list()
        [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]
        sage: C2.cardinality()
        6

    ::

        sage: C3 = Combinations(range(4),2,as_tuples=True)
        sage: C3
        Combinations of [0, 1, 2, 3] of length 2
        sage: C3.list()
        [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
        sage: C3.cardinality()
        6

    ::

        sage: Combinations([1,2,2,3]).list()
        [[],
         [1],
         [2],
         [3],
         [1, 2],
         [1, 3],
         [2, 2],
         [2, 3],
         [1, 2, 2],
         [1, 2, 3],
         [2, 2, 3],
         [1, 2, 2, 3]]

    ::

        sage: Combinations([1,2,3], 2).list()
        [[1, 2], [1, 3], [2, 3]]

    ::

        sage: mset = [1,1,2,3,4,4,5]
        sage: Combinations(mset,2).list()
        [[1, 1],
         [1, 2],
         [1, 3],
         [1, 4],
         [1, 5],
         [2, 3],
         [2, 4],
         [2, 5],
         [3, 4],
         [3, 5],
         [4, 4],
         [4, 5]]

    ::

        sage: mset = ["d","a","v","i","d"]
        sage: Combinations(mset,3).list()
        [[\'d\', \'d\', \'a\'],
         [\'d\', \'d\', \'v\'],
         [\'d\', \'d\', \'i\'],
         [\'d\', \'a\', \'v\'],
         [\'d\', \'a\', \'i\'],
         [\'d\', \'v\', \'i\'],
         [\'a\', \'v\', \'i\']]

    ::

        sage: X = Combinations([1,2,3,4,5],3)
        sage: [x for x in X]
        [[1, 2, 3],
         [1, 2, 4],
         [1, 2, 5],
         [1, 3, 4],
         [1, 3, 5],
         [1, 4, 5],
         [2, 3, 4],
         [2, 3, 5],
         [2, 4, 5],
         [3, 4, 5]]

    It is possible to take combinations of Sage objects::

        sage: Combinations([vector([1,1]), vector([2,2]), vector([3,3])], 2).list()     # needs sage.modules
        [[(1, 1), (2, 2)], [(1, 1), (3, 3)], [(2, 2), (3, 3)]]

    TESTS:

    Run the test suites::

        sage: C = Combinations([2,3])
        sage: TestSuite(C).run()
        sage: C = Combinations([2,3], 1)
        sage: TestSuite(C).run()

    We check that the code works even for non mutable objects::

        sage: l = [vector((0,0)), vector((0,1))]                                        # needs sage.modules
        sage: Combinations(l).list()                                                    # needs sage.modules
        [[], [(0, 0)], [(0, 1)], [(0, 0), (0, 1)]]
    '''

class Combinations_mset(Parent):
    mset: Incomplete
    as_tuples: Incomplete
    def __init__(self, mset, as_tuples: bool = False) -> None:
        """
        TESTS::

            sage: C = Combinations(range(4))
            sage: C == loads(dumps(C))
            True
        """
    def __contains__(self, x) -> bool:
        """
        EXAMPLES::

            sage: c = Combinations(range(4))
            sage: all( i in c for i in c )
            True
            sage: [3,4] in c
            False
            sage: [0,0] in c
            False
        """
    def __eq__(self, other) -> bool:
        """
        Test for equality.

        EXAMPLES::

            sage: c = Combinations([1,2,2,3])
            sage: c == Combinations((1,2,2,3))
            True
            sage: c == Combinations([3,4,4,6])
            False
        """
    def __ne__(self, other) -> bool:
        """
        Test for unequality.

        EXAMPLES::

            sage: c = Combinations([1,2,2])
            sage: c != Combinations([1,2,3,3])
            True
        """
    def __iter__(self):
        """
        TESTS::

            sage: Combinations(['a','a','b']).list() #indirect doctest
            [[], ['a'], ['b'], ['a', 'a'], ['a', 'b'], ['a', 'a', 'b']]
            sage: Combinations(['a','a','b'],as_tuples=True).list()
            [(), ('a',), ('b',), ('a', 'a'), ('a', 'b'), ('a', 'a', 'b')]
        """
    def cardinality(self) -> Integer:
        """
        TESTS::

            sage: Combinations([1,2,3]).cardinality()
            8
            sage: Combinations(['a','a','b']).cardinality()                             # needs sage.libs.gap
            6
        """

class Combinations_set(Combinations_mset):
    def __iter__(self):
        """
        EXAMPLES::

            sage: Combinations([1,2,3]).list() #indirect doctest
            [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
            sage: Combinations([1,2,3],as_tuples=True).list()
            [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
        """
    def unrank(self, r):
        """
        EXAMPLES::

            sage: c = Combinations([1,2,3])
            sage: c.list() == list(map(c.unrank, range(c.cardinality())))
            True
        """
    def rank(self, x):
        """
        EXAMPLES::

            sage: c = Combinations([1,2,3])
            sage: list(range(c.cardinality())) == list(map(c.rank, c))
            True
        """
    def cardinality(self):
        """
        Return the size of Combinations(set).

        EXAMPLES::

            sage: Combinations(range(16000)).cardinality() == 2^16000
            True
        """

class Combinations_msetk(Parent):
    mset: Incomplete
    k: Incomplete
    as_tuples: Incomplete
    def __init__(self, mset, k, as_tuples: bool = False) -> None:
        """
        TESTS::

            sage: C = Combinations([1,2,3],2)
            sage: C == loads(dumps(C))
            True
        """
    def __contains__(self, x) -> bool:
        """
        EXAMPLES::

            sage: c = Combinations(range(4),2)
            sage: all( i in c for i in c )
            True
            sage: [0,1] in c
            True
            sage: [0,1,2] in c
            False
            sage: [3,4] in c
            False
            sage: [0,0] in c
            False
        """
    def __eq__(self, other) -> bool:
        """
        Test for equality.

        EXAMPLES::

            sage: c = Combinations([1,2,2,3],3)
            sage: c == Combinations((1,2,2,3), 3)
            True
            sage: c == Combinations([1,2,2,3], 2)
            False
        """
    def __ne__(self, other) -> bool:
        """
        Test for unequality.

        EXAMPLES::

            sage: c = Combinations([1,2,2,3],3)
            sage: c != Combinations((1,2,2,3), 2)
            True
        """
    def __iter__(self):
        """
        EXAMPLES::

            sage: Combinations(['a','a','b'],2).list() # indirect doctest
            [['a', 'a'], ['a', 'b']]
        """
    def cardinality(self) -> Integer:
        """
        Return the size of combinations(mset, k).

        IMPLEMENTATION: Wraps GAP's NrCombinations.

        EXAMPLES::

            sage: mset = [1,1,2,3,4,4,5]
            sage: Combinations(mset,2).cardinality()                                    # needs sage.libs.gap
            12
        """

class Combinations_setk(Combinations_msetk):
    def __iter__(self):
        """
        Uses Python's :func:`itertools.combinations` to iterate through all
        of the combinations.

        EXAMPLES::

            sage: Combinations([1,2,3,4,5],3).list() # indirect doctest
            [[1, 2, 3],
             [1, 2, 4],
             [1, 2, 5],
             [1, 3, 4],
             [1, 3, 5],
             [1, 4, 5],
             [2, 3, 4],
             [2, 3, 5],
             [2, 4, 5],
             [3, 4, 5]]
             sage: Combinations([1,2,3,4,5],3,as_tuples=True).list()
             [(1, 2, 3),
             (1, 2, 4),
             (1, 2, 5),
             (1, 3, 4),
             (1, 3, 5),
             (1, 4, 5),
             (2, 3, 4),
             (2, 3, 5),
             (2, 4, 5),
             (3, 4, 5)]
        """
    def list(self) -> list:
        """
        EXAMPLES::

            sage: Combinations([1,2,3,4,5],3).list()
            [[1, 2, 3],
             [1, 2, 4],
             [1, 2, 5],
             [1, 3, 4],
             [1, 3, 5],
             [1, 4, 5],
             [2, 3, 4],
             [2, 3, 5],
             [2, 4, 5],
             [3, 4, 5]]
        """
    def unrank(self, r):
        """
        EXAMPLES::

            sage: c = Combinations([1,2,3], 2)
            sage: c.list() == list(map(c.unrank, range(c.cardinality())))
            True
        """
    def rank(self, x):
        """
        EXAMPLES::

            sage: c = Combinations([1,2,3], 2)
            sage: list(range(c.cardinality())) == list(map(c.rank, c.list()))
            True
        """
    def cardinality(self) -> Integer:
        """
        Return the size of combinations(set, k).

        EXAMPLES::

            sage: Combinations(range(16000), 5).cardinality()
            8732673194560003200
        """

def rank(comb, n, check: bool = True):
    """
    Return the rank of ``comb`` in the subsets of ``range(n)`` of size ``k``
    where ``k`` is the length of ``comb``.

    The algorithm used is based on combinadics and James McCaffrey's
    MSDN article. See: :wikipedia:`Combinadic`.

    EXAMPLES::

        sage: import sage.combinat.combination as combination
        sage: combination.rank((), 3)
        0
        sage: combination.rank((0,), 3)
        0
        sage: combination.rank((1,), 3)
        1
        sage: combination.rank((2,), 3)
        2
        sage: combination.rank((0,1), 3)
        0
        sage: combination.rank((0,2), 3)
        1
        sage: combination.rank((1,2), 3)
        2
        sage: combination.rank((0,1,2), 3)
        0

        sage: combination.rank((0,1,2,3), 3)
        Traceback (most recent call last):
        ...
        ValueError: len(comb) must be <= n
        sage: combination.rank((0,0), 2)
        Traceback (most recent call last):
        ...
        ValueError: comb must be a subword of (0,1,...,n)

        sage: combination.rank([1,2], 3)
        2
        sage: combination.rank([0,1,2], 3)
        0
    """
def from_rank(r, n, k):
    """
    Return the combination of rank ``r`` in the subsets of
    ``range(n)`` of size ``k`` when listed in lexicographic order.

    The algorithm used is based on factoradics and presented in [DGH2020]_.
    It is there compared to the other from the literature.

    EXAMPLES::

        sage: import sage.combinat.combination as combination
        sage: combination.from_rank(0,3,0)
        ()
        sage: combination.from_rank(0,3,1)
        (0,)
        sage: combination.from_rank(1,3,1)
        (1,)
        sage: combination.from_rank(2,3,1)
        (2,)
        sage: combination.from_rank(0,3,2)
        (0, 1)
        sage: combination.from_rank(1,3,2)
        (0, 2)
        sage: combination.from_rank(2,3,2)
        (1, 2)
        sage: combination.from_rank(0,3,3)
        (0, 1, 2)

    TESTS::

        sage: from sage.combinat.combination import from_rank
        sage: def _comb_largest(a, b, x):
        ....:     w = a - 1
        ....:     while binomial(w,b) > x:
        ....:         w -= 1
        ....:     return w
        sage: def from_rank_comb_largest(r, n, k):
        ....:     a = n
        ....:     b = k
        ....:     x = binomial(n, k) - 1 - r  # x is the 'dual' of m
        ....:     comb = [None] * k
        ....:     for i in range(k):
        ....:         comb[i] = _comb_largest(a, b, x)
        ....:         x = x - binomial(comb[i], b)
        ....:         a = comb[i]
        ....:         b = b - 1
        ....:     for i in range(k):
        ....:         comb[i] = (n - 1) - comb[i]
        ....:     return tuple(comb)
        sage: all(from_rank(r, n, k) == from_rank_comb_largest(r, n, k)                 # needs sage.symbolic
        ....:     for n in range(10) for k in range(n+1) for r in range(binomial(n,k)))
        True
    """

class ChooseNK(Combinations_setk): ...
