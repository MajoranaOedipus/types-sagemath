from _typeshed import Incomplete
from collections.abc import Generator
from sage.arith.misc import binomial as binomial
from sage.categories.classical_crystals import ClassicalCrystals as ClassicalCrystals
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.categories.infinite_enumerated_sets import InfiniteEnumeratedSets as InfiniteEnumeratedSets
from sage.categories.tensor import tensor as tensor
from sage.combinat.combinatorial_map import combinatorial_map as combinatorial_map
from sage.combinat.composition import Composition as Composition, Compositions as Compositions, composition_iterator_fast as composition_iterator_fast
from sage.combinat.integer_lists.invlex import IntegerListsLex as IntegerListsLex
from sage.combinat.permutation import Permutations_mset as Permutations_mset
from sage.combinat.shuffle import ShuffleProduct as ShuffleProduct, ShuffleProduct_overlapping as ShuffleProduct_overlapping
from sage.combinat.subset import Subsets_sk as Subsets_sk
from sage.misc.inherit_comparison import InheritComparisonClasscallMetaclass as InheritComparisonClasscallMetaclass
from sage.misc.latex import latex as latex
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod, running_total as running_total
from sage.rings.infinity import infinity as infinity
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.power_series_ring import PowerSeriesRing as PowerSeriesRing
from sage.sets.set import Set_object as Set_object
from sage.structure.element_wrapper import ElementWrapper as ElementWrapper
from sage.structure.list_clone import ClonableArray as ClonableArray
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class OrderedMultisetPartitionIntoSets(ClonableArray, metaclass=InheritComparisonClasscallMetaclass):
    """
    Ordered Multiset Partition into sets.

    An *ordered multiset partition into sets* `c` of a multiset `X` is a list
    `[c_1, \\ldots, c_r]` of nonempty subsets of `X` (note: not
    sub-multisets), called the *blocks* of `c`, whose multi-union is `X`.

    EXAMPLES:

    The simplest way to create an ordered multiset partition into sets is by
    specifying its blocks as a list or tuple::

        sage: OrderedMultisetPartitionIntoSets([[3],[2,1]])
        [{3}, {1,2}]
        sage: OrderedMultisetPartitionIntoSets(((3,), (1,2)))
        [{3}, {1,2}]
        sage: OrderedMultisetPartitionIntoSets([set([i]) for i in range(2,5)])
        [{2}, {3}, {4}]

    REFERENCES:

    - [HRW2015]_
    - [HRS2016]_
    - [LM2018]_
    """
    @staticmethod
    def __classcall_private__(cls, co):
        """
        Create an ordered multiset partition into sets (i.e., a list of sets)
        from the passed arguments with the appropriate parent.

        EXAMPLES::

            sage: OrderedMultisetPartitionIntoSets([[3], [2,1]])
            [{3}, {1,2}]
            sage: c = OrderedMultisetPartitionsIntoSets()([{2}, {3}, {4}, {5}]); c
            [{2}, {3}, {4}, {5}]
            sage: d = OrderedMultisetPartitionsIntoSets((1,1,1,2,3,5))([{1}, {5, 1, 3}, {2, 1}]); d
            [{1}, {1,3,5}, {1,2}]

        TESTS::

            sage: c.parent() == OrderedMultisetPartitionsIntoSets([2,3,4,5])
            False
            sage: d.parent() == OrderedMultisetPartitionsIntoSets([1,1,1,2,3,5])
            True
            sage: repr(OrderedMultisetPartitionIntoSets([]).parent())
            'Ordered Multiset Partitions into Sets of multiset {{}}'
        """
    def __init__(self, parent, data) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: c = OrderedMultisetPartitionsIntoSets(7)([[1,3], [1,2]])
            sage: OrderedMultisetPartitionIntoSets([[1,3], [1,2]]) == c
            True
            sage: c.weight()
            {1: 2, 2: 1, 3: 1}

        TESTS::

            sage: OMP = OrderedMultisetPartitionIntoSets
            sage: c0 = OMP([])
            sage: OMP([[]]) == c0
            True
            sage: TestSuite(c0).run()

            sage: d = OMP([[1, 3], [1, 'a', 'b']])
            sage: TestSuite(d).run()

            sage: OMPs = OrderedMultisetPartitionsIntoSets()
            sage: d = OMPs([['a','b','c'],['a','b'],['a']])
            sage: TestSuite(d).run()

            sage: c.size() == 7
            True
            sage: d.size() == None
            True
        """
    def check(self) -> None:
        """
        Check that we are a valid ordered multiset partition into sets.

        EXAMPLES::

            sage: c = OrderedMultisetPartitionsIntoSets(4)([[1], [1,2]])
            sage: c.check()

            sage: OMPs = OrderedMultisetPartitionsIntoSets()
            sage: c = OMPs([[1], [1], ['a']])
            sage: c.check()

        TESTS::

            sage: c = OMPs([[1, 1], [1, 4]])
            Traceback (most recent call last):
            ...
            ValueError: cannot convert [[1, 1], [1, 4]] into an element
             of Ordered Multiset Partitions into Sets
        """
    def __hash__(self):
        """
        Return the hash of ``self``.

        The parent is not included as part of the hash.

        EXAMPLES::

            sage: OMP = OrderedMultisetPartitionsIntoSets(4)
            sage: A = OMP([[1], [1, 2]])
            sage: B = OMP([{1}, {1, 2}])
            sage: hash(A) == hash(B)
            True
        """
    def __eq__(self, y):
        """
        Check equality of ``self`` and ``y``.

        The parent is not included as part of the equality check.

        TESTS::

            sage: OMP_n = OrderedMultisetPartitionsIntoSets(4)
            sage: OMP_X = OrderedMultisetPartitionsIntoSets([1,1,2])
            sage: OMP_Ad = OrderedMultisetPartitionsIntoSets(2, 3)
            sage: mu = [[1], [1, 2]]
            sage: OMP_n(mu) == OMP_X(mu) == OMP_Ad(mu)
            True
            sage: OMP_n(mu) == mu
            False
            sage: OMP_n(mu) == OMP_n([{1}, {3}])
            False
            sage: OMP_n(mu) == OMP_X([[1], [1,2]])
            True
        """
    def __ne__(self, y):
        """
        Check lack of equality of ``self`` and ``y``.

        The parent is not included as part of the equality check.

        TESTS::

            sage: OMP = OrderedMultisetPartitionsIntoSets(4)
            sage: mu = [[1], [1, 2]]
            sage: OMP(mu).__ne__(mu)
            True
            sage: nu = [[1], [2], [1]]
            sage: OMP(mu).__ne__(OMP(nu))
            True
        """
    def __add__(self, other):
        """
        Return the concatenation of two ordered multiset partitions into sets.

        This operation represents the product in Hopf algebra of ordered multiset
        partitions into sets in its natural basis [LM2018]_.

        EXAMPLES::

            sage: OMP = OrderedMultisetPartitionIntoSets
            sage: OMP([[1],[1],[1,3]]) + OMP([[4,1],[2]])
            [{1}, {1}, {1,3}, {1,4}, {2}]

        TESTS::

            sage: OMP([]) + OMP([]) == OMP([])
            True
            sage: OMP([[1],[1],[1,3]]) + OMP([]) == OMP([[1],[1],[1,3]])
            True
        """
    def reversal(self):
        """
        Return the reverse ordered multiset partition into sets of ``self``.

        Given an ordered multiset partition into sets `(B_1, B_2, \\ldots, B_k)`,
        its reversal is defined to be the ordered multiset partition into sets
        `(B_k, \\ldots, B_2, B_1)`.

        EXAMPLES::

            sage: C = OrderedMultisetPartitionIntoSets([[1], [1, 3], [2, 3, 4]]); C
            [{1}, {1,3}, {2,3,4}]
            sage: C.reversal()
            [{2,3,4}, {1,3}, {1}]
        """
    def shape_from_cardinality(self):
        """
        Return a composition that records the cardinality of each block of ``self``.

        EXAMPLES::

            sage: C = OrderedMultisetPartitionIntoSets([[3, 4, 1], [2], [1, 2, 3, 7]]); C
            [{1,3,4}, {2}, {1,2,3,7}]
            sage: C.shape_from_cardinality()
            [3, 1, 4]
            sage: OrderedMultisetPartitionIntoSets([]).shape_from_cardinality() == Composition([])
            True
        """
    def shape_from_size(self):
        """
        Return a composition that records the sum of entries of each
        block of ``self``.

        EXAMPLES::

            sage: C = OrderedMultisetPartitionIntoSets([[3, 4, 1], [2], [1, 2, 3, 7]]); C
            [{1,3,4}, {2}, {1,2,3,7}]
            sage: C.shape_from_size()
            [8, 2, 13]

        TESTS::

            sage: OrderedMultisetPartitionIntoSets([]).shape_from_size() == Composition([])
            True
            sage: D = OrderedMultisetPartitionIntoSets([['a', 'b'], ['a']]); D
            [{'a','b'}, {'a'}]
            sage: D.shape_from_size() == None
            True
        """
    def letters(self):
        """
        Return the set of distinct elements occurring within the blocks
        of ``self``.

        EXAMPLES::

            sage: C = OrderedMultisetPartitionIntoSets([[3, 4, 1], [2], [1, 2, 3, 7]]); C
            [{1,3,4}, {2}, {1,2,3,7}]
            sage: C.letters()
            frozenset({1, 2, 3, 4, 7})
        """
    def multiset(self, as_dict: bool = False):
        """
        Return the multiset corresponding to ``self``.

        INPUT:

        - ``as_dict`` -- boolean (default: ``False``); whether to return the multiset
          as a tuple of a dict of multiplicities

        EXAMPLES::

            sage: C = OrderedMultisetPartitionIntoSets([[3, 4, 1], [2], [1, 2, 3, 7]]); C
            [{1,3,4}, {2}, {1,2,3,7}]
            sage: C.multiset()
            (1, 1, 2, 2, 3, 3, 4, 7)
            sage: C.multiset(as_dict=True)
            {1: 2, 2: 2, 3: 2, 4: 1, 7: 1}
            sage: OrderedMultisetPartitionIntoSets([]).multiset() == ()
            True
        """
    def max_letter(self):
        """
        Return the maximum letter appearing in ``self.letters()`` of ``self``.

        EXAMPLES::

            sage: C = OrderedMultisetPartitionIntoSets([[3, 4, 1], [2], [1, 2, 3, 7]])
            sage: C.max_letter()
            7
            sage: D = OrderedMultisetPartitionIntoSets([['a','b','c'],['a','b'],['a'],['b','c','f'],['c','d']])
            sage: D.max_letter()
            'f'
            sage: C = OrderedMultisetPartitionIntoSets([])
            sage: C.max_letter()
        """
    def size(self):
        """
        Return the size of ``self`` (that is, the sum of all integers in
        all blocks) if ``self`` is a list of subsets of positive integers.

        Else, return ``None``.

        EXAMPLES::

            sage: C = OrderedMultisetPartitionIntoSets([[3, 4, 1], [2], [1, 2, 3, 7]]); C
            [{1,3,4}, {2}, {1,2,3,7}]
            sage: C.size()
            23
            sage: C.size() == sum(k for k in C.shape_from_size())
            True
            sage: OrderedMultisetPartitionIntoSets([[7,1],[3]]).size()
            11

        TESTS::

            sage: OrderedMultisetPartitionIntoSets([]).size() == 0
            True
            sage: OrderedMultisetPartitionIntoSets([['a','b'],['a','b','c']]).size() is None
            True
        """
    def order(self):
        """
        Return the total number of elements in all blocks of ``self``.

        EXAMPLES::

            sage: C = OrderedMultisetPartitionIntoSets([[3, 4, 1], [2], [1, 2, 3, 7]]); C
            [{1,3,4}, {2}, {1,2,3,7}]
            sage: C.order()
            8
            sage: C.order() == sum(C.weight().values())
            True
            sage: C.order() == sum(k for k in C.shape_from_cardinality())
            True
            sage: OrderedMultisetPartitionIntoSets([[7,1],[3]]).order()
            3
        """
    def length(self):
        """
        Return the number of blocks of ``self``.

        EXAMPLES::

            sage: OrderedMultisetPartitionIntoSets([[7,1],[3]]).length()
            2
        """
    def weight(self, as_weak_comp: bool = False):
        """
        Return a dictionary, with keys being the letters in ``self.letters()``
        and values being their (positive) frequency.

        Alternatively, if ``as_weak_comp`` is ``True``, count the number of instances
        `n_i` for each distinct positive integer `i` across all blocks of ``self``.
        Return as a list `[n_1, n_2, n_3, ..., n_k]`, where `k` is the max letter
        appearing in ``self.letters()``.

        EXAMPLES::

            sage: c = OrderedMultisetPartitionIntoSets([[6,1],[1,3],[1,3,6]])
            sage: c.weight()
            {1: 3, 3: 2, 6: 2}
            sage: c.weight(as_weak_comp=True)
            [3, 0, 2, 0, 0, 2]

        TESTS::

            sage: OrderedMultisetPartitionIntoSets([]).weight() == {}
            True

            sage: c = OrderedMultisetPartitionIntoSets([['a','b'],['a','b','c'],['b'],['b'],['c']])
            sage: c.weight()
            {'a': 2, 'b': 4, 'c': 2}
            sage: c.weight(as_weak_comp=True)
            Traceback (most recent call last):
            ...
            ValueError: {'a': 2, 'b': 4, 'c': 2} is not a numeric multiset
        """
    def deconcatenate(self, k: int = 2):
        """
        Return the list of `k`-deconcatenations of ``self``.

        A `k`-tuple `(C_1, \\ldots, C_k)` of ordered multiset partitions into sets
        represents a `k`-deconcatenation of an ordered multiset partition into sets
        `C` if `C_1 + \\cdots + C_k = C`.

        .. NOTE::

            This is not to be confused with ``self.split_blocks()``,
            which splits each block of ``self`` before making `k`-tuples
            of ordered multiset partitions into sets.

        EXAMPLES::

            sage: OrderedMultisetPartitionIntoSets([[7,1],[3,4,5]]).deconcatenate()
            [([{1,7}, {3,4,5}], []), ([{1,7}], [{3,4,5}]), ([], [{1,7}, {3,4,5}])]
            sage: OrderedMultisetPartitionIntoSets([['b','c'],['a']]).deconcatenate()
            [([{'b','c'}, {'a'}], []), ([{'b','c'}], [{'a'}]), ([], [{'b','c'}, {'a'}])]
            sage: OrderedMultisetPartitionIntoSets([['a','b','c']]).deconcatenate(3)
            [([{'a','b','c'}], [], []),
             ([], [{'a','b','c'}], []),
             ([], [], [{'a','b','c'}])]

        TESTS::

            sage: C = OrderedMultisetPartitionIntoSets([['a'],['b'],['c'],['d'],['e']]); C
            [{'a'}, {'b'}, {'c'}, {'d'}, {'e'}]
            sage: all( len(C.deconcatenate(k))
            ....:      == binomial(C.length() + k-1, k-1)
            ....:      for k in range(1, 5) )
            True
        """
    def split_blocks(self, k: int = 2):
        """
        Return a dictionary representing the `k`-splittings of ``self``.

        A `k`-tuple `(A^1, \\ldots, A^k)` of ordered multiset partitions into sets
        represents a `k`-splitting of an ordered multiset partition into sets
        `A = [b_1, \\ldots, b_r]` if one can express each block `b_i` as
        an (ordered) disjoint union of sets `b_i = b^1_i \\sqcup \\cdots
        \\sqcup b^k_i` (some possibly empty) so that each `A^j` is the
        ordered multiset partition into sets corresponding to the list `[b^j_1,
        b^j_2, \\ldots, b^j_r]`, excising empty sets appearing therein.

        This operation represents the coproduct in Hopf algebra of ordered
        multiset partitions into sets in its natural basis [LM2018]_.

        EXAMPLES::

            sage: sorted(OrderedMultisetPartitionIntoSets([[1,2],[3,4]]).split_blocks(), key=str)
            [([], [{1,2}, {3,4}]),
             ([{1,2}, {3,4}], []),
             ([{1,2}, {3}], [{4}]),
             ([{1,2}, {4}], [{3}]),
             ([{1,2}], [{3,4}]),
             ([{1}, {3,4}], [{2}]),
             ([{1}, {3}], [{2}, {4}]),
             ([{1}, {4}], [{2}, {3}]),
             ([{1}], [{2}, {3,4}]),
             ([{2}, {3,4}], [{1}]),
             ([{2}, {3}], [{1}, {4}]),
             ([{2}, {4}], [{1}, {3}]),
             ([{2}], [{1}, {3,4}]),
             ([{3,4}], [{1,2}]),
             ([{3}], [{1,2}, {4}]),
             ([{4}], [{1,2}, {3}])]
            sage: sorted(OrderedMultisetPartitionIntoSets([[1,2]]).split_blocks(3), key=str)
            [([], [], [{1,2}]), ([], [{1,2}], []), ([], [{1}], [{2}]),
             ([], [{2}], [{1}]), ([{1,2}], [], []), ([{1}], [], [{2}]),
             ([{1}], [{2}], []), ([{2}], [], [{1}]), ([{2}], [{1}], [])]
            sage: OrderedMultisetPartitionIntoSets([[4],[4]]).split_blocks()
            {([], [{4}, {4}]): 1, ([{4}], [{4}]): 2, ([{4}, {4}], []): 1}

        TESTS::

            sage: C = OrderedMultisetPartitionIntoSets([[1,2],[4,5,6]]); C
            [{1,2}, {4,5,6}]
            sage: sum(C.split_blocks().values()) == 2**len(C[0]) * 2**len(C[1])
            True
            sage: sum(C.split_blocks(3).values()) == (1+2)**len(C[0]) * (1+2)**len(C[1])
            True
            sage: C = OrderedMultisetPartitionIntoSets([])
            sage: C.split_blocks(3) == {(C, C, C): 1}
            True
        """
    def finer(self, strong: bool = False):
        """
        Return the set of ordered multiset partitions into sets that are finer
        than ``self``.

        An ordered multiset partition into sets `A` is finer than another `B`
        if, reading left-to-right, every block of `B` is the union of some
        consecutive blocks of `A`.

        If optional argument ``strong`` is set to ``True``, then return
        only those `A` whose blocks are deconcatenations of blocks of `B`.
        (Here, we view blocks of `B` as sorted lists instead of sets.)

        EXAMPLES::

            sage: C = OrderedMultisetPartitionIntoSets([[3,2]]).finer()
            sage: len(C)
            3
            sage: sorted(C, key=str)
            [[{2,3}], [{2}, {3}], [{3}, {2}]]
            sage: OrderedMultisetPartitionIntoSets([]).finer()
            {[]}
            sage: O = OrderedMultisetPartitionsIntoSets([1, 1, 'a', 'b'])
            sage: o = O([{1}, {'a', 'b'}, {1}])
            sage: sorted(o.finer(), key=str)
            [[{1}, {'a','b'}, {1}], [{1}, {'a'}, {'b'}, {1}], [{1}, {'b'}, {'a'}, {1}]]
            sage: o.finer() & o.fatter() == set([o])
            True
        """
    def is_finer(self, co):
        """
        Return ``True`` if the ordered multiset partition into sets ``self``
        is finer than the composition ``co``; otherwise, return ``False``.

        EXAMPLES::

            sage: OrderedMultisetPartitionIntoSets([[4],[1],[2]]).is_finer([[1,4],[2]])
            True
            sage: OrderedMultisetPartitionIntoSets([[1],[4],[2]]).is_finer([[1,4],[2]])
            True
            sage: OrderedMultisetPartitionIntoSets([[1,4],[1],[1]]).is_finer([[1,4],[2]])
            False
        """
    def fatten(self, grouping):
        """
        Return the ordered multiset partition into sets fatter than ``self``,
        obtained by grouping together consecutive parts according to ``grouping``
        (whenever this does not violate the strictness condition).

        INPUT:

        - ``grouping`` -- a composition (or list) whose sum is the length
          of ``self``

        EXAMPLES:

        Let us start with the composition::

            sage: C = OrderedMultisetPartitionIntoSets([[4,1,5], [2], [7,1]]); C
            [{1,4,5}, {2}, {1,7}]

        With ``grouping`` equal to `(1, 1, 1)`, `C` is left unchanged::

            sage: C.fatten([1,1,1])
            [{1,4,5}, {2}, {1,7}]

        With ``grouping`` equal to `(2,1)` or `(1,2)`, a union of consecutive
        parts is achieved::

            sage: C.fatten([2,1])
            [{1,2,4,5}, {1,7}]
            sage: C.fatten([1,2])
            [{1,4,5}, {1,2,7}]

        However, the ``grouping`` `(3)` will throw an error, as `1` cannot
        appear twice in any block of ``C``::

            sage: C.fatten(Composition([3]))
            Traceback (most recent call last):
            ...
            ValueError: [{1,4,5,2,1,7}] is not a valid ordered multiset partition into sets
        """
    def fatter(self):
        """
        Return the set of ordered multiset partitions into sets which are fatter
        than ``self``.

        An ordered multiset partition into sets `A` is fatter than another `B`
        if, reading left-to-right, every block of `A` is the union of some
        consecutive blocks of `B`.

        EXAMPLES::

            sage: C = OrderedMultisetPartitionIntoSets([{1,4,5}, {2}, {1,7}]).fatter()
            sage: len(C)
            3
            sage: sorted(C)
            [[{1,4,5}, {2}, {1,7}], [{1,4,5}, {1,2,7}], [{1,2,4,5}, {1,7}]]
            sage: sorted(OrderedMultisetPartitionIntoSets([['a','b'],['c'],['a']]).fatter())
            [[{'a','b'}, {'c'}, {'a'}], [{'a','b'}, {'a','c'}], [{'a','b','c'}, {'a'}]]

        Some extreme cases::

            sage: list(OrderedMultisetPartitionIntoSets([['a','b','c']]).fatter())
            [[{'a','b','c'}]]
            sage: list(OrderedMultisetPartitionIntoSets([]).fatter())
            [[]]
            sage: A = OrderedMultisetPartitionIntoSets([[1], [2], [3], [4]])
            sage: B = OrderedMultisetPartitionIntoSets([[1,2,3,4]])
            sage: A.fatter().issubset(B.finer())
            True
        """
    def minimaj(self):
        """
        Return the minimaj statistic on ordered multiset partitions into sets.

        We define `minimaj` via an example:

        1. Sort the block in ``self`` as prescribed by ``self.minimaj_word()``,
           keeping track of the original separation into blocks::

             in:   [{1,5,7}, {2,4}, {5,6}, {4,6,8}, {1,3}, {1,2,3}]
             out:  ( 5,7,1 /  2,4 /  5,6 /  4,6,8 /  3,1 /  1,2,3 )

        2. Record the indices where descents in this word occur::

             word:      (5, 7, 1 / 2, 4 / 5, 6 / 4, 6, 8 / 3, 1 / 1, 2, 3)
             indices:    1  2  3   4  5   6  7   8  9 10  11 12  13 14 15
             descents:  {   2,               7,       10, 11             }

        3. Compute the sum of the descents::

             minimaj = 2 + 7 + 10 + 11 = 30

        REFERENCES:

        - [HRW2015]_

        EXAMPLES::

            sage: C = OrderedMultisetPartitionIntoSets([{1,5,7}, {2,4}, {5,6}, {4,6,8}, {1,3}, {1,2,3}])
            sage: C, C.minimaj_word()
            ([{1,5,7}, {2,4}, {5,6}, {4,6,8}, {1,3}, {1,2,3}],
             (5, 7, 1, 2, 4, 5, 6, 4, 6, 8, 3, 1, 1, 2, 3))
            sage: C.minimaj()
            30
            sage: C = OrderedMultisetPartitionIntoSets([{2,4}, {1,2,3}, {1,6,8}, {2,3}])
            sage: C, C.minimaj_word()
            ([{2,4}, {1,2,3}, {1,6,8}, {2,3}], (2, 4, 1, 2, 3, 6, 8, 1, 2, 3))
            sage: C.minimaj()
            9
            sage: OrderedMultisetPartitionIntoSets([]).minimaj()
            0
            sage: C = OrderedMultisetPartitionIntoSets([['b','d'],['a','b','c'],['b']])
            sage: C, C.minimaj_word()
            ([{'b','d'}, {'a','b','c'}, {'b'}], ('d', 'b', 'c', 'a', 'b', 'b'))
            sage: C.minimaj()
            4
        """
    def minimaj_word(self):
        """
        Return an ordering of ``self._multiset`` derived from the minimaj
        ordering on blocks of ``self``.

        .. SEEALSO::

            :meth:`OrderedMultisetPartitionIntoSets.minimaj_blocks()`.

        EXAMPLES::

            sage: C = OrderedMultisetPartitionIntoSets([[2,1], [1,2,3], [1,2], [3], [1]]); C
            [{1,2}, {1,2,3}, {1,2}, {3}, {1}]
            sage: C.minimaj_blocks()
            ((1, 2), (2, 3, 1), (1, 2), (3,), (1,))
            sage: C.minimaj_word()
            (1, 2, 2, 3, 1, 1, 2, 3, 1)
        """
    def minimaj_blocks(self):
        """
        Return the minimaj ordering on blocks of ``self``.

        We define the ordering via the example below.

        Sort the blocks `[B_1,...,B_k]` of ``self`` from right to left via:

        1. Sort the last block `B_k` in increasing order, call it the word `W_k`

        2. If blocks `B_{i+1}, \\ldots, B_k` have been converted to words
           `W_{i+1}, \\ldots, W_k`, use the letters in `B_i` to make the unique
           word `W_i` that has a factorization `W_i = (u, v)` satisfying:

           - letters of `u` and `v` appear in increasing order, with `v`
             possibly empty;
           - letters in `vu` appear in increasing order;
           - ``v[-1]`` is the largest letter `a \\in B_i` satisfying
             ``a <= W_{i+1}[0]``.

        EXAMPLES::

            sage: OrderedMultisetPartitionIntoSets([[1,5,7], [2,4], [5,6], [4,6,8], [1,3], [1,2,3]])
            [{1,5,7}, {2,4}, {5,6}, {4,6,8}, {1,3}, {1,2,3}]
            sage: _.minimaj_blocks()
            ((5, 7, 1), (2, 4), (5, 6), (4, 6, 8), (3, 1), (1, 2, 3))
            sage: OrderedMultisetPartitionIntoSets([]).minimaj_blocks()
            ()
        """
    def to_tableaux_words(self):
        """
        Return a sequence of lists corresponding to row words
        of (skew-)tableaux.

        OUTPUT:

        The minimaj bijection `\\phi` of [BCHOPSY2017]_
        applied to ``self``.

        .. TODO::

            Implement option for mapping to sequence of (skew-)tableaux?

        EXAMPLES::

            sage: co = ((1,2,4),(4,5),(3,),(4,6,1),(2,3,1),(1,),(2,5))
            sage: OrderedMultisetPartitionIntoSets(co).to_tableaux_words()
            [[5, 1], [3, 1], [6], [5, 4, 2], [1, 4, 3, 4, 2, 1, 2]]
        """
    def major_index(self):
        """
        Return the major index of ``self``.

        The major index is a statistic on ordered multiset partitions into sets,
        which we define here via an example.

        1. Sort each block in the list ``self`` in descending order to create
           a word `w`, keeping track of the original separation into blocks::

             in:  [{3,4,5}, {2,3,4}, {1}, {4,5}]
             out: [ 5,4,3 /  4,3,2 /  1 /  5,4 ]

        2. Create a sequence `v = (v_0, v_1, v_2, \\ldots)`  of length
           ``self.order()+1``, built recursively by:

           1. `v_0 = 0`
           2. `v_j = v_{j-1} + \\delta(j)`, where `\\delta(j) = 1` if `j` is
              the index of an end of a block, and zero otherwise.

           ::

             in:    [ 5,4,3 /  4,3,2 /  1 /  5,4]
             out: (0, 0,0,1,   1,1,2,   3,   3,4)

        3. Compute `\\sum_j v_j`, restricted to descent positions in `w`, i.e.,
           sum over those `j` with `w_j > w_{j+1}`::

             in:  w:   [5, 4, 3, 4, 3, 2, 1, 5, 4]
                  v: (0 0, 0, 1, 1, 1, 2, 3, 3, 4)
             maj :=     0 +0    +1 +1 +2    +3     = 7

        REFERENCES:

        - [HRW2015]_

        EXAMPLES::

            sage: C = OrderedMultisetPartitionIntoSets([{1,5,7}, {2,4}, {5,6}, {4,6,8}, {1,3}, {1,2,3}])
            sage: C.major_index()
            27
            sage: C = OrderedMultisetPartitionIntoSets([{3,4,5}, {2,3,4}, {1}, {4,5}])
            sage: C.major_index()
            7
        """
    def shuffle_product(self, other, overlap: bool = False) -> Generator[Incomplete]:
        """
        Return the shuffles (with multiplicity) of blocks of ``self``
        with blocks of ``other``.

        In case optional argument ``overlap`` is ``True``, instead return
        the allowable overlapping shuffles. An overlapping shuffle `C` is
        allowable if, whenever one of its blocks `c` comes from the union
        `c = a \\cup b` of a block of ``self`` and a block of ``other``,
        then this union is disjoint.

        .. SEEALSO::

            :meth:`Composition.shuffle_product()`

        EXAMPLES::

            sage: A = OrderedMultisetPartitionIntoSets([[2,1,3], [1,2]]); A
            [{1,2,3}, {1,2}]
            sage: B = OrderedMultisetPartitionIntoSets([[3,4]]); B
            [{3,4}]
            sage: C = OrderedMultisetPartitionIntoSets([[4,5]]); C
            [{4,5}]
            sage: list(A.shuffle_product(B))
            [[{1,2,3}, {1,2}, {3,4}], [{3,4}, {1,2,3}, {1,2}], [{1,2,3}, {3,4}, {1,2}]]
            sage: list(A.shuffle_product(B, overlap=True))
            [[{1,2,3}, {1,2}, {3,4}], [{1,2,3}, {3,4}, {1,2}],
             [{3,4}, {1,2,3}, {1,2}], [{1,2,3}, {1,2,3,4}]]
            sage: list(A.shuffle_product(C, overlap=True))
            [[{1,2,3}, {1,2}, {4,5}], [{1,2,3}, {4,5}, {1,2}], [{4,5}, {1,2,3}, {1,2}],
             [{1,2,3,4,5}, {1,2}], [{1,2,3}, {1,2,4,5}]]
        """

class OrderedMultisetPartitionsIntoSets(UniqueRepresentation, Parent):
    """
    Ordered Multiset Partitions into Sets.

    An *ordered multiset partition into sets* `c` of a multiset `X` is
    a list of nonempty subsets (not multisets), called the *blocks* of `c`,
    whose multi-union is `X`.

    The number of blocks of `c` is called its *length*. The *order* of `c`
    is the cardinality of the multiset `X`. If, additionally, `X` is a
    multiset of positive integers, then the *size* of `c` is the sum of
    all elements of `X`.

    The user may wish to focus on ordered multiset partitions into sets
    of a given size, or over a given alphabet. Hence, this class allows
    a variety of arguments as input.

    INPUT:

    Expects one or two arguments, with different behaviors resulting:

    - One Argument:

      + `X` -- a dictionary or list or tuple
        (representing a multiset for `c`),
        or an integer (representing the size of `c`)

    - Two Arguments:

      + `A` -- list (representing allowable letters within blocks of `c`),
        or a positive integer (representing the maximal allowable letter)
      + `n` -- a nonnegative integer (the total number of letters within `c`)

    Optional keyword arguments are as follows:
    (See corresponding methods in see :class:`OrderedMultisetPartitionIntoSets` for more details.)

    - ``weight=X``     (list or dictionary `X`) specifies the multiset for `c`
    - ``size=n``       (integer `n`) specifies the size of `c`
    - ``alphabet=A``   (iterable `A`) specifies allowable elements for the blocks of `c`
    - ``length=k``     (integer `k`) specifies the number of blocks in the partition
    - ``min_length=k`` (integer `k`) specifies minimum number of blocks in the partition
    - ``max_length=k`` (integer `k`) specifies maximum number of blocks in the partition
    - ``order=n``      (integer `n`) specifies the cardinality of the multiset that `c` partitions
    - ``min_order=n``  (integer `n`) specifies minimum number of elements in the partition
    - ``max_order=n``  (integer `n`) specifies maximum number of elements in the partition

    EXAMPLES:

    Passing one argument to :class:`OrderedMultisetPartitionsIntoSets`:

    There are 5 ordered multiset partitions into sets of the multiset
    `\\{\\{1, 1, 4\\}\\}`::

        sage: OrderedMultisetPartitionsIntoSets([1,1,4]).cardinality()
        5

    Here is the list of them::

        sage: OrderedMultisetPartitionsIntoSets([1,1,4]).list()
        [[{1}, {1}, {4}], [{1}, {1,4}], [{1}, {4}, {1}], [{1,4}, {1}], [{4}, {1}, {1}]]

    By chance, there are also 5 ordered multiset partitions into sets of
    the integer 3::

        sage: OrderedMultisetPartitionsIntoSets(3).cardinality()
        5

    Here is the list of them::

        sage: OrderedMultisetPartitionsIntoSets(3).list()
        [[{3}], [{1,2}], [{2}, {1}], [{1}, {2}], [{1}, {1}, {1}]]

    Passing two arguments to :class:`OrderedMultisetPartitionsIntoSets`:

    There are also 5 ordered multiset partitions into sets of order 2
    over the alphabet `\\{1, 4\\}`::

        sage: OrderedMultisetPartitionsIntoSets([1, 4], 2)
        Ordered Multiset Partitions into Sets of order 2 over alphabet {1, 4}
        sage: OrderedMultisetPartitionsIntoSets([1, 4], 2).cardinality()
        5

    Here is the list of them::

        sage: OrderedMultisetPartitionsIntoSets([1, 4], 2).list()
        [[{1,4}], [{1}, {1}], [{1}, {4}], [{4}, {1}], [{4}, {4}]]

    If no arguments are passed to :class:`OrderedMultisetPartitionsIntoSets`,
    then the code returns all ordered multiset partitions into sets::

        sage: OrderedMultisetPartitionsIntoSets()
        Ordered Multiset Partitions into Sets
        sage: [] in OrderedMultisetPartitionsIntoSets()
        True
        sage: [[2,3], [1]] in OrderedMultisetPartitionsIntoSets()
        True
        sage: [['a','b'], ['a']] in OrderedMultisetPartitionsIntoSets()
        True
        sage: [[-2,3], [3]] in OrderedMultisetPartitionsIntoSets()
        True
        sage: [[2], [3,3]] in OrderedMultisetPartitionsIntoSets()
        False

    The following examples show how to test whether or not an object
    is an ordered multiset partition into sets::

        sage: [[3,2],[2]] in OrderedMultisetPartitionsIntoSets()
        True
        sage: [[3,2],[2]] in OrderedMultisetPartitionsIntoSets(7)
        True
        sage: [[3,2],[2]] in OrderedMultisetPartitionsIntoSets([2,2,3])
        True
        sage: [[3,2],[2]] in OrderedMultisetPartitionsIntoSets(5)
        False

    .. RUBRIC:: Optional keyword arguments

    Passing keyword arguments that are incompatible with required requirements
    results in an error; otherwise, the collection of ordered multiset partitions
    into sets is restricted accordingly:

    *The* ``weight`` *keyword:*

    This is used to specify which multiset `X` is to be considered,
    if this multiset was not passed as one of the required arguments for
    :class:`OrderedMultisetPartitionsIntoSets`. In principle, it is a dictionary,
    but weak compositions are also allowed. For example, the ordered multiset
    partitions into sets of integer 4 are listed by weight below::

        sage: OrderedMultisetPartitionsIntoSets(4, weight=[0,0,0,1])
        Ordered Multiset Partitions into Sets of integer 4 with constraint: weight={4: 1}
        sage: OrderedMultisetPartitionsIntoSets(4, weight=[0,0,0,1]).list()
        [[{4}]]
        sage: OrderedMultisetPartitionsIntoSets(4, weight=[1,0,1]).list()
        [[{1}, {3}], [{1,3}], [{3}, {1}]]
        sage: OrderedMultisetPartitionsIntoSets(4, weight=[0,2]).list()
        [[{2}, {2}]]
        sage: OrderedMultisetPartitionsIntoSets(4, weight=[0,1,1]).list()
        []
        sage: OrderedMultisetPartitionsIntoSets(4, weight=[2,1]).list()
        [[{1}, {1}, {2}], [{1}, {1,2}], [{1}, {2}, {1}], [{1,2}, {1}], [{2}, {1}, {1}]]
        sage: O1 = OrderedMultisetPartitionsIntoSets(weight=[2,0,1])
        sage: O2 = OrderedMultisetPartitionsIntoSets(weight={1:2, 3:1})
        sage: O1 == O2
        True
        sage: OrderedMultisetPartitionsIntoSets(4, weight=[4]).list()
        [[{1}, {1}, {1}, {1}]]

    *The* ``size`` *keyword:*

    This is used to constrain the sum of entries across all blocks of the ordered
    multiset partition into sets. (This size is not pre-determined when alphabet
    `A` and order `d` are passed as required arguments.) For example, the ordered
    multiset partitions into sets of order 3 over the alphabet `[1,2,4]` that have
    size equal to 5 are as follows::

        sage: OMPs = OrderedMultisetPartitionsIntoSets
        sage: OMPs([1,2,4], 3, size=5).list()
        [[{1,2}, {2}], [{2}, {1,2}], [{2}, {2}, {1}],
         [{2}, {1}, {2}], [{1}, {2}, {2}]]

    *The* ``alphabet`` *option:*

    This is used to constrain which integers appear across all blocks of the
    ordered multiset partition into sets. For example, the ordered multiset
    partitions into sets of integer 4 are listed for different choices of alphabet
    below. Note that ``alphabet`` is allowed to be an integer or an iterable::

        sage: OMPs = OrderedMultisetPartitionsIntoSets
        sage: OMPs(4, alphabet=3).list()
        [[{1,3}], [{3}, {1}],
         [{1,2}, {1}], [{2}, {2}],
         [{2}, {1}, {1}], [{1}, {3}],
         [{1}, {1,2}], [{1}, {2}, {1}],
         [{1}, {1}, {2}], [{1}, {1}, {1}, {1}]]
        sage: OMPs(4, alphabet=3) == OMPs(4, alphabet=[1,2,3])
        True
        sage: OMPs(4, alphabet=[3]).list()
        []
        sage: OMPs(4, alphabet=[1,3]).list()
        [[{1,3}], [{3}, {1}], [{1}, {3}], [{1}, {1}, {1}, {1}]]
        sage: OMPs(4, alphabet=[2]).list()
        [[{2}, {2}]]
        sage: OMPs(4, alphabet=[1,2]).list()
        [[{1,2}, {1}], [{2}, {2}], [{2}, {1}, {1}], [{1}, {1,2}],
         [{1}, {2}, {1}], [{1}, {1}, {2}], [{1}, {1}, {1}, {1}]]
        sage: OMPs(4, alphabet=4).list() == OMPs(4).list()
        True

    *The* ``length``, ``min_length``, *and* ``max_length`` *options:*

    These are used to constrain the number of blocks within the ordered multiset
    partitions into sets. For example, the ordered multiset partitions into sets
    of integer 4 of length exactly 2, at least 2, and at most 2 are given by::

        sage: OrderedMultisetPartitionsIntoSets(4, length=2).list()
        [[{3}, {1}], [{1,2}, {1}], [{2}, {2}], [{1}, {3}], [{1}, {1,2}]]
        sage: OrderedMultisetPartitionsIntoSets(4, min_length=3).list()
        [[{2}, {1}, {1}], [{1}, {2}, {1}], [{1}, {1}, {2}], [{1}, {1}, {1}, {1}]]
        sage: OrderedMultisetPartitionsIntoSets(4, max_length=2).list()
        [[{4}], [{1,3}], [{3}, {1}], [{1,2}, {1}], [{2}, {2}], [{1}, {3}],
         [{1}, {1,2}]]

    *The* ``order``, ``min_order``, *and* ``max_order`` *options:*

    These are used to constrain the number of elements across all blocks of the
    ordered multiset partitions into sets. For example, the ordered multiset
    partitions into sets of integer 4 are listed by order below::

        sage: OrderedMultisetPartitionsIntoSets(4, order=1).list()
        [[{4}]]
        sage: OrderedMultisetPartitionsIntoSets(4, order=2).list()
        [[{1,3}], [{3}, {1}], [{2}, {2}], [{1}, {3}]]
        sage: OrderedMultisetPartitionsIntoSets(4, order=3).list()
        [[{1,2}, {1}], [{2}, {1}, {1}], [{1}, {1,2}], [{1}, {2}, {1}], [{1}, {1}, {2}]]
        sage: OrderedMultisetPartitionsIntoSets(4, order=4).list()
        [[{1}, {1}, {1}, {1}]]

    Also, here is a use of ``max_order``, giving the ordered multiset
    partitions into sets of integer 4 with order 1 or 2::

        sage: OrderedMultisetPartitionsIntoSets(4, max_order=2).list()
        [[{4}], [{1,3}], [{3}, {1}], [{2}, {2}], [{1}, {3}]]

    TESTS::

        sage: C = OrderedMultisetPartitionsIntoSets(8, length=3); C.cardinality()
        72
        sage: TestSuite(C).run()
    """
    @staticmethod
    def __classcall_private__(self, *args, **constraints):
        """
        Return the correct parent based upon the input:

        EXAMPLES::

            sage: OrderedMultisetPartitionsIntoSets()
            Ordered Multiset Partitions into Sets
            sage: OrderedMultisetPartitionsIntoSets(4)
            Ordered Multiset Partitions into Sets of integer 4
            sage: OrderedMultisetPartitionsIntoSets(4, max_order=2)
            Ordered Multiset Partitions into Sets of integer 4 with constraint: max_order=2

            sage: OrderedMultisetPartitionsIntoSets({1:2, 3:1})
            Ordered Multiset Partitions into Sets of multiset {{1, 1, 3}}
            sage: OrderedMultisetPartitionsIntoSets({1:2, 3:1}) == OrderedMultisetPartitionsIntoSets([1,1,3])
            True
            sage: OrderedMultisetPartitionsIntoSets({'a':2, 'c':1}, length=2)
            Ordered Multiset Partitions into Sets of multiset {{a, a, c}} with constraint: length=2
            sage: OrderedMultisetPartitionsIntoSets({'a':2, 'c':1}, length=4).list()
            []

            sage: OrderedMultisetPartitionsIntoSets(4, 3)
            Ordered Multiset Partitions into Sets of order 3 over alphabet {1, 2, 3, 4}
            sage: OrderedMultisetPartitionsIntoSets(['a', 'd'], 3)
            Ordered Multiset Partitions into Sets of order 3 over alphabet {a, d}
            sage: OrderedMultisetPartitionsIntoSets([2,4], 3, min_length=2)
            Ordered Multiset Partitions into Sets of order 3 over alphabet {2, 4}
             with constraint: min_length=2

        TESTS:

        The alphabet and order keywords cannot be used if they are also passed
        as required arguments, even if the values are compatible::

            sage: OrderedMultisetPartitionsIntoSets([1,2,4], 4, alphabet=[2,4], order=3)
            Traceback (most recent call last):
            ...
            ValueError: cannot pass alphabet as first argument and keyword argument
            sage: OrderedMultisetPartitionsIntoSets([1,2,4], 4, order=4)
            Traceback (most recent call last):
            ...
            ValueError: cannot pass order as second argument and keyword argument

        The weight, size, and order keywords cannot be used if a multiset is
        passed as a required argument, even if the values are compatible::

            sage: OrderedMultisetPartitionsIntoSets([1,1,4], weight={1:3, 2:1}).list()
            Traceback (most recent call last):
            ...
            ValueError: cannot pass multiset as first argument and weight as keyword argument
            sage: OrderedMultisetPartitionsIntoSets([1,1,4], size=6).list()
            Traceback (most recent call last):
            ...
            ValueError: cannot pass multiset as first argument and size as keyword argument
            sage: OrderedMultisetPartitionsIntoSets([1,1,4], weight={1:3, 2:1}, order=2).list()
            Traceback (most recent call last):
            ...
            ValueError: cannot pass multiset as first argument and ['order', 'weight'] as keyword arguments

        The size keyword cannot be used if it is also passed as a required argument,
        even if the value is compatible::

            sage: OrderedMultisetPartitionsIntoSets(5, size=5)
            Traceback (most recent call last):
            ...
            ValueError: cannot pass size as first argument and keyword argument
        """
    constraints: Incomplete
    full_constraints: Incomplete
    def __init__(self, is_finite=None, **constraints) -> None:
        '''
        Initialize ``self``.

        TESTS::

            sage: c = {"length":4, "max_order":6, "alphabet":[2,4,5,6]}
            sage: OrderedMultisetPartitionsIntoSets(**c).constraints
            {\'alphabet\': frozenset({2, 4, 5, 6}), \'length\': 4, \'max_order\': 6}
            sage: OrderedMultisetPartitionsIntoSets(17, **c).constraints
            {\'alphabet\': frozenset({2, 4, 5, 6}), \'length\': 4, \'max_order\': 6}
            sage: OrderedMultisetPartitionsIntoSets(17, **c).full_constraints
            {\'alphabet\': frozenset({2, 4, 5, 6}), \'length\': 4, \'max_order\': 6, \'size\': 17}

            sage: c = {"length":4, "min_length":5, "max_order":6, "order":5, "alphabet":4}
            sage: OrderedMultisetPartitionsIntoSets(**c).full_constraints
            {\'alphabet\': frozenset({1, 2, 3, 4}), \'length\': 4, \'order\': 5}
            sage: OrderedMultisetPartitionsIntoSets(**c).constraints
            {\'length\': 4}
            sage: OrderedMultisetPartitionsIntoSets(4, 5, **c).constraints
            Traceback (most recent call last):
            ...
            ValueError: cannot pass alphabet as first argument and keyword argument

            sage: c = {"weight":[2,2,0,3], "min_length":5, "max_order":6, "order":5, "alphabet":4}
            sage: OrderedMultisetPartitionsIntoSets(**c).constraints
            Traceback (most recent call last):
            ...
            ValueError: cannot pass multiset as first argument and [\'alphabet\', \'max_order\', \'order\'] as keyword arguments
        '''
    Element = OrderedMultisetPartitionIntoSets
    def __contains__(self, x) -> bool:
        """
        Return if ``x`` is contained in ``self``.

        TESTS::

            sage: [[2,1], [1,3]] in OrderedMultisetPartitionsIntoSets()
            True
            sage: [[2,1], [1,3]] in OrderedMultisetPartitionsIntoSets(7)
            True
            sage: [[2,2], [1,3]] in OrderedMultisetPartitionsIntoSets()
            False
            sage: [] in OrderedMultisetPartitionsIntoSets()
            True
            sage: [] in OrderedMultisetPartitionsIntoSets(0)
            True
            sage: [] in OrderedMultisetPartitionsIntoSets(2)
            False
            sage: [[2, 1]] in OrderedMultisetPartitionsIntoSets(3, length=2)
            False
            sage: [[2, -1]] in OrderedMultisetPartitionsIntoSets()
            True
        """
    def __iter__(self):
        """
        Iterate over ordered multiset partitions into sets.

        EXAMPLES::

            sage: OrderedMultisetPartitionsIntoSets(3).list()
            [[{3}], [{1,2}], [{2}, {1}], [{1}, {2}], [{1}, {1}, {1}]]
            sage: OrderedMultisetPartitionsIntoSets(0).list()
            [[]]
            sage: C = OrderedMultisetPartitionsIntoSets()
            sage: it = C.__iter__()
            sage: [next(it) for i in range(16)]
            [[], [{1}], [{2}], [{1}, {1}], [{3}], [{1,2}], [{2}, {1}],
             [{1}, {2}], [{1}, {1}, {1}], [{4}], [{1,3}], [{3}, {1}],
             [{1,2}, {1}], [{2}, {2}], [{2}, {1}, {1}], [{1}, {3}]]

        TESTS::

            sage: OrderedMultisetPartitionsIntoSets(alphabet=[1,3], max_length=2).list()
            [[], [{1}], [{3}], [{1,3}], [{1}, {1}], [{1}, {3}],
             [{3}, {1}], [{3}, {3}], [{1,3}, {1}], [{1,3}, {3}],
             [{1}, {1,3}], [{3}, {1,3}], [{1,3}, {1,3}]]
            sage: C = OrderedMultisetPartitionsIntoSets(min_length=2, max_order=2)
            sage: it = C.__iter__()
            sage: [next(it) for i in range(15)]
            [[{1}, {1}], [{2}, {1}], [{1}, {2}], [{3}, {1}], [{2}, {2}],
             [{1}, {3}], [{4}, {1}], [{3}, {2}], [{2}, {3}], [{1}, {4}],
             [{5}, {1}], [{4}, {2}], [{3}, {3}], [{2}, {4}], [{1}, {5}]]
            sage: OrderedMultisetPartitionsIntoSets(alphabet=[1,3], min_length=2).list()
            Traceback (most recent call last):
            ...
            NotImplementedError: cannot list an infinite set
        """
    def subset(self, size):
        """
        Return a subset of all ordered multiset partitions into sets.

        INPUT:

        - ``size`` -- integer representing a slice of all ordered
          multiset partitions into sets

        The slice alluded to above is taken with respect to length, or
        to order, or to size, depending on the constraints of  ``self``.

        EXAMPLES::

            sage: C = OrderedMultisetPartitionsIntoSets(weight={2:2, 3:1, 5:1})
            sage: C.subset(3)
            Ordered Multiset Partitions into Sets of multiset {{2, 2, 3, 5}} with constraint: length=3
            sage: C = OrderedMultisetPartitionsIntoSets(weight={2:2, 3:1, 5:1}, min_length=2)
            sage: C.subset(3)
            Ordered Multiset Partitions into Sets of multiset {{2, 2, 3, 5}} with constraint: length=3
            sage: C = OrderedMultisetPartitionsIntoSets(alphabet=[2,3,5])
            sage: C.subset(3)
            Ordered Multiset Partitions into Sets of order 3 over alphabet {2, 3, 5}
            sage: C = OrderedMultisetPartitionsIntoSets(order=5)
            sage: C.subset(3)
            Ordered Multiset Partitions into Sets of integer 3 with constraint: order=5
            sage: C = OrderedMultisetPartitionsIntoSets(alphabet=[2,3,5], order=5, length=3)
            sage: C.subset(3)
            Ordered Multiset Partitions into Sets of order 3 over alphabet {2, 3, 5} with constraint: length=3
            sage: C = OrderedMultisetPartitionsIntoSets()
            sage: C.subset(3)
            Ordered Multiset Partitions into Sets of integer 3
            sage: C.subset(3) == OrderedMultisetPartitionsIntoSets(3)
            True
        """

class OrderedMultisetPartitionsIntoSets_all_constraints(OrderedMultisetPartitionsIntoSets):
    """
    All ordered multiset partitions into sets (with or without constraints).

    EXAMPLES::

        sage: C = OrderedMultisetPartitionsIntoSets(); C
        Ordered Multiset Partitions into Sets
        sage: [[1],[1,'a']] in C
        True

        sage: OrderedMultisetPartitionsIntoSets(weight=[2,0,1], length=2)
        Ordered Multiset Partitions into Sets of multiset {{1, 1, 3}} with constraint: length=2

    TESTS::

        sage: OMP = OrderedMultisetPartitionsIntoSets()
        sage: TestSuite(OMP).run()  # long time

        sage: C = OrderedMultisetPartitionsIntoSets(weight=[2,0,1], length=2)
        sage: TestSuite(C).run()

        sage: D1 = OrderedMultisetPartitionsIntoSets(weight={1:2, 3:1}, min_length=2, max_length=2)
        sage: D2 = OrderedMultisetPartitionsIntoSets({1:2, 3:1}, min_length=2, max_length=2)
        sage: D3 = OrderedMultisetPartitionsIntoSets(5, weight={1:2, 3:1}, length=2)
        sage: D4 = OrderedMultisetPartitionsIntoSets([1,3], 3, weight={1:2, 3:1}, length=2)
        sage: D5 = OrderedMultisetPartitionsIntoSets([1,3], 3, size=5, length=2)
        sage: all(C != D for D in [D1, D2, D3, D4, D5])
        True
        sage: all(Set(C) == Set(D) for D in [D1, D2, D3, D4, D5])
        True
        sage: E = OrderedMultisetPartitionsIntoSets({1:2, 3:1}, min_length=2)
        sage: Set(C) == Set(E)
        False
    """

class OrderedMultisetPartitionsIntoSets_n(OrderedMultisetPartitionsIntoSets):
    """
    Ordered multiset partitions into sets of a fixed integer `n`.
    """
    def __init__(self, n) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: C = OrderedMultisetPartitionsIntoSets(Integer(4))
            sage: TestSuite(C).run()
            sage: C2 = OrderedMultisetPartitionsIntoSets(int(4))
            sage: C is C2
            True
            sage: C3 = OrderedMultisetPartitionsIntoSets(7/2)
            Traceback (most recent call last):
            ...
            ValueError:  7/2 must be a nonnegative integer or a list or
             dictionary representing a multiset
        """
    def cardinality(self):
        """
        Return the number of elements in ``self``.

        TESTS::

            sage: len(OrderedMultisetPartitionsIntoSets(10).list())
            1500
            sage: OrderedMultisetPartitionsIntoSets(10).cardinality()
            1500
        """
    def random_element(self):
        """
        Return a random element of ``self``.

        This method does not return elements of ``self`` with uniform probability,
        but it does cover all elements. The scheme is as follows:

        - produce a random composition `C`;
        - choose a random partition of `c` into distinct parts for each `c` in `C`.

        EXAMPLES::

            sage: OrderedMultisetPartitionsIntoSets(5).random_element()  # random
            [{1,2}, {1}, {1}]
            sage: OrderedMultisetPartitionsIntoSets(5).random_element()  # random
            [{2}, {1,2}]

            sage: OMP = OrderedMultisetPartitionsIntoSets(5)
            sage: d = {}
            sage: for _ in range(1100):
            ....:     x = OMP.random_element()
            ....:     d[x] = d.get(x, 0) + 1
            sage: d.values()  # random
            [72, 73, 162, 78, 135, 75, 109, 65, 135, 134, 62]
        """
    def __iter__(self):
        """
        Iterate over ``self``.

        TESTS::

            sage: O = OrderedMultisetPartitionsIntoSets(6)
            sage: it = O.__iter__()
            sage: [next(it) for _ in range(10)]
            [[{6}], [{2,4}], [{1,5}], [{1,2,3}],
             [{5}, {1}], [{2,3}, {1}], [{1,4}, {1}],
             [{4}, {2}], [{1,3}, {2}], [{4}, {1}, {1}]]
        """

class OrderedMultisetPartitionsIntoSets_n_constraints(OrderedMultisetPartitionsIntoSets):
    """
    Class of ordered multiset partitions into sets of a fixed integer `n`
    satisfying constraints.
    """
    def __init__(self, n, **constraints) -> None:
        """
        Mimic class ``OrderedMultisetPartitionsIntoSets_n`` to initialize.

        TESTS::

            sage: C = OrderedMultisetPartitionsIntoSets(6, length=3)
            sage: TestSuite(C).run()

            sage: C = OrderedMultisetPartitionsIntoSets(6, weight=[3,0,1], length=3)
            sage: TestSuite(C).run()
        """

class OrderedMultisetPartitionsIntoSets_X(OrderedMultisetPartitionsIntoSets):
    """
    Class of ordered multiset partitions into sets of a fixed multiset `X`.
    """
    def __init__(self, X) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: C = OrderedMultisetPartitionsIntoSets([1,1,4])
            sage: TestSuite(C).run()

            sage: C2 = OrderedMultisetPartitionsIntoSets({1:2, 4:1})
            sage: C is C2
            True
        """
    def __contains__(self, x) -> bool:
        """
        Return if ``x`` is contained in ``self``.

        TESTS::

            sage: from sage.combinat.multiset_partition_into_sets_ordered import OrderedMultisetPartitionsIntoSets_X as OMPX
            sage: [[2,1], [1,3]] in OMPX(((1,2), (2,1), (3,1)))
            True
            sage: co = OrderedMultisetPartitionIntoSets([[2,1], [1,3]])
            sage: co in OMPX(((1,2), (2,1), (3,1)))
            True
            sage: [[2,1], [2,3]] in OMPX(((1,2), (2,1), (3,1)))
            False
            sage: [] in OMPX(())
            True
            sage: [[2, -1], [2,'a']] in OMPX(((2,2), (-1,1), ('a',1)))
            True
        """
    def cardinality(self):
        """
        Return the number of ordered partitions of multiset ``X``.

        TESTS::

            sage: len(OrderedMultisetPartitionsIntoSets([2,2,2,3,4,5]).list())
            535
            sage: OrderedMultisetPartitionsIntoSets([2,2,2,3,4,5]).cardinality()
            535
        """
    def random_element(self):
        """
        Return a random element of ``self``.

        This method does not return elements of ``self`` with uniform probability,
        but it does cover all elements. The scheme is as follows:

        - produce a random permutation ``p`` of the multiset;
        - create blocks of an OMP ``fat`` by breaking ``p`` after non-ascents;
        - take a random element of ``fat.finer()``.

        EXAMPLES::

            sage: OrderedMultisetPartitionsIntoSets([1,1,3]).random_element()  # random
            [{1}, {1,3}]
            sage: OrderedMultisetPartitionsIntoSets([1,1,3]).random_element()  # random
            [{3}, {1}, {1}]

            sage: OMP = OrderedMultisetPartitionsIntoSets([1,1,3,3])
            sage: d = {}
            sage: for _ in range(1000):
            ....:     x = OMP.random_element()
            ....:     d[x] = d.get(x, 0) + 1
            sage: d.values()  # random
            [102, 25, 76, 24, 66, 88, 327, 27, 83, 83, 239, 72, 88]
        """
    def __iter__(self):
        """
        Iterate over ``self``.

        TESTS::

            sage: O = OrderedMultisetPartitionsIntoSets(['a', 'b', 'a'])
            sage: sorted(O, key=str)
            [[{'a','b'}, {'a'}],
             [{'a'}, {'a','b'}],
             [{'a'}, {'a'}, {'b'}],
             [{'a'}, {'b'}, {'a'}],
             [{'b'}, {'a'}, {'a'}]]

            sage: O = OrderedMultisetPartitionsIntoSets([1, 1, 2])
            sage: list(O)
            [[{1}, {1}, {2}], [{1}, {1,2}], [{1}, {2}, {1}],
            [{1,2}, {1}], [{2}, {1}, {1}]]
        """

class OrderedMultisetPartitionsIntoSets_X_constraints(OrderedMultisetPartitionsIntoSets):
    """
    Class of ordered multiset partitions into sets of a fixed multiset `X`
    satisfying constraints.
    """
    def __init__(self, X, **constraints) -> None:
        """
        Mimic class ``OrderedMultisetPartitionsIntoSets_X`` to initialize.

        TESTS::

            sage: C = OrderedMultisetPartitionsIntoSets([1,1,2,4], length=3)
            sage: TestSuite(C).run()

            sage: C = OrderedMultisetPartitionsIntoSets([1,1,2,4], max_length=3)
            sage: TestSuite(C).run()
        """

class OrderedMultisetPartitionsIntoSets_alph_d(OrderedMultisetPartitionsIntoSets):
    """
    Class of ordered multiset partitions into sets of specified order `d`
    over a fixed alphabet `A`.
    """
    def __init__(self, A, d) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: C = OrderedMultisetPartitionsIntoSets(3, 2)
            sage: TestSuite(C).run()

            sage: C2 = OrderedMultisetPartitionsIntoSets([1,2,3], 2)
            sage: C is C2
            True

            sage: list(OrderedMultisetPartitionsIntoSets([1,2,3], 2))
            [[{1,2}], [{1,3}], [{2,3}], [{1}, {1}], [{1}, {2}], [{1}, {3}], [{2}, {1}],
             [{2}, {2}], [{2}, {3}], [{3}, {1}], [{3}, {2}], [{3}, {3}]]
        """
    def random_element(self):
        """
        Return a random element of ``self``.

        This method does not return elements of ``self`` with uniform probability,
        but it does cover all elements. The scheme is as follows:

        - produce a random composition `C`;
        - choose random subsets of ``self._alphabet`` of size `c` for each `c` in `C`.

        EXAMPLES::

            sage: OrderedMultisetPartitionsIntoSets([1,4], 3).random_element()  # random
            [{4}, {1,4}]
            sage: OrderedMultisetPartitionsIntoSets([1,3], 4).random_element()  # random
            [{1,3}, {1}, {3}]

            sage: OMP = OrderedMultisetPartitionsIntoSets([2,3,4], 2)
            sage: d = {}
            sage: for _ in range(1200):
            ....:     x = OMP.random_element()
            ....:     d[x] = d.get(x, 0) + 1
            sage: d.values()  # random
            [192, 68, 73, 61, 69, 60, 77, 204, 210, 66, 53, 67]
        """
    def __iter__(self):
        """
        Iterate over ``self``.

        TESTS::

            sage: O = OrderedMultisetPartitionsIntoSets(['a', 'b'], 3)
            sage: it = O.__iter__()
            sage: sorted([next(it) for _ in range(O.cardinality())], key=str)
            [[{'a','b'}, {'a'}], [{'a','b'}, {'b'}], [{'a'}, {'a','b'}],
             [{'a'}, {'a'}, {'a'}], [{'a'}, {'a'}, {'b'}], [{'a'}, {'b'}, {'a'}],
             [{'a'}, {'b'}, {'b'}], [{'b'}, {'a','b'}], [{'b'}, {'a'}, {'a'}],
             [{'b'}, {'a'}, {'b'}], [{'b'}, {'b'}, {'a'}], [{'b'}, {'b'}, {'b'}]]
        """
    def cardinality(self):
        """
        Return the number of ordered partitions of order ``self._order`` on
        alphabet ``self._alphabet``.

        TESTS::

            sage: len(OrderedMultisetPartitionsIntoSets([1, 'a'], 3).list())
            12
            sage: OrderedMultisetPartitionsIntoSets([1, 'a'], 3).cardinality()
            12
        """

class OrderedMultisetPartitionsIntoSets_alph_d_constraints(OrderedMultisetPartitionsIntoSets):
    """
    Class of ordered multiset partitions into sets of specified order `d`
    over a fixed alphabet `A` satisfying constraints.
    """
    def __init__(self, A, d, **constraints) -> None:
        """
        Mimic class ``OrderedMultisetPartitionsIntoSets_alph_d`` to initialize.

        EXAMPLES::

            sage: list(OrderedMultisetPartitionsIntoSets(3, 2, length=3))
            []
            sage: list(OrderedMultisetPartitionsIntoSets([1,2,4], 2, length=1))
            [[{1,2}], [{1,4}], [{2,4}]]

        TESTS::

            sage: C = OrderedMultisetPartitionsIntoSets(3, 2, length=3)
            sage: TestSuite(C).run()

            sage: C = OrderedMultisetPartitionsIntoSets([1,2,4], 4, min_length=3)
            sage: TestSuite(C).run()
        """

class MinimajCrystal(UniqueRepresentation, Parent):
    """
    Crystal of ordered multiset partitions into sets with `ell` letters from
    alphabet `\\{1, 2, \\ldots, n\\}` divided into `k` blocks.

    Elements are represented in the minimaj ordering of blocks as in
    Benkart et al. [BCHOPSY2017]_.

    .. NOTE::

        Elements are not stored internally as ordered multiset partitions
        into sets, but as certain (pairs of) words stemming from the minimaj
        bijection `\\phi` of [BCHOPSY2017]_. See
        :class:`sage.combinat.multiset_partition_into_sets_ordered.MinimajCrystal.Element`
        for further details.

    AUTHORS:

    - Anne Schilling (2018): initial draft
    - Aaron Lauve (2018): changed to use ``Letters`` crystal for elements

    EXAMPLES::

        sage: list(crystals.Minimaj(2,3,2))                                             # needs sage.modules
        [((2, 1), (1,)), ((2,), (1, 2)), ((1,), (1, 2)), ((1, 2), (2,))]

        sage: b = crystals.Minimaj(3, 5, 2).an_element(); b                             # needs sage.modules
        ((2, 3, 1), (1, 2))
        sage: b.f(2)                                                                    # needs sage.modules
        ((2, 3, 1), (1, 3))
        sage: b.e(2)                                                                    # needs sage.modules
    """
    n: Incomplete
    ell: Incomplete
    k: Incomplete
    module_generators: Incomplete
    def __init__(self, n, ell, k) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: # needs sage.modules
            sage: B = crystals.Minimaj(2,3,2)
            sage: TestSuite(B).run()
            sage: B = crystals.Minimaj(3, 5, 2)
            sage: TestSuite(B).run()
            sage: list(crystals.Minimaj(2,6,3))
            [((1, 2), (2, 1), (1, 2))]
            sage: list(crystals.Minimaj(2,5,2))  # blocks too fat for alphabet
            []
            sage: list(crystals.Minimaj(4,2,3))  # more blocks than letters
            Traceback (most recent call last):
            ...
            ValueError: n (=4), ell (=2), and k (=3) must all be positive integers
        """
    def __contains__(self, x) -> bool:
        """
        Return ``True`` if ``x`` is an element of ``self`` or an ordered
        multiset partition into sets.

        EXAMPLES::

            sage: # needs sage.modules
            sage: B1 = crystals.Minimaj(2,5,3); b1 = B1.an_element(); b1
            ((1, 2), (2, 1), (1,))
            sage: B2 = crystals.Minimaj(5,5,3); b2 = B2.an_element(); b2
            ((2, 3, 1), (1,), (1,))
            sage: b2a = B2(((1,2), (1,), (1,2))); b2a
            ((2, 1), (1,), (1, 2))
            sage: b1 in B2
            True
            sage: b2 in B1
            False
            sage: b2a in B1
            True
        """
    def from_tableau(self, t):
        """
        Return the bijection `\\phi^{-1}` of [BCHOPSY2017]_ applied to ``t``.

        INPUT:

        - ``t`` -- a sequence of column tableaux and a ribbon tableau

        EXAMPLES::

            sage: # needs sage.modules
            sage: B = crystals.Minimaj(3,6,3)
            sage: b = B.an_element(); b
            ((3, 1, 2), (2, 1), (1,))
            sage: t = b.to_tableaux_words(); t
            [[1], [2, 1], [], [3, 2, 1]]
            sage: B.from_tableau(t)
            ((3, 1, 2), (2, 1), (1,))
            sage: B.from_tableau(t) == b
            True

        TESTS::

            sage: # needs sage.modules
            sage: B = crystals.Minimaj(3,6,3)
            sage: all(mu == B.from_tableau(mu.to_tableaux_words()) for mu in B)
            True
            sage: t = B.an_element().to_tableaux_words()
            sage: B1 = crystals.Minimaj(3,6,2)
            sage: B1.from_tableau(t)
            Traceback (most recent call last):
            ...
            ValueError: ((3, 1, 2), (2, 1), (1,)) is not an element of
             Minimaj Crystal of type A_2 of words of length 6 into 2 blocks
        """
    def val(self, q: str = 'q'):
        """
        Return the `Val` polynomial corresponding to ``self``.

        EXAMPLES:

        Verifying Example 4.5 from [BCHOPSY2017]_::

            sage: B = crystals.Minimaj(3, 4, 2)  # for `Val_{4,1}^{(3)}`                # needs sage.modules
            sage: B.val()                                                               # needs sage.modules
            (q^2+q+1)*s[2, 1, 1] + q*s[2, 2]
        """
    class Element(ElementWrapper):
        """
        An element of a Minimaj crystal.

        .. NOTE::

            Minimaj elements `b` are stored internally as pairs
            ``(w, breaks)``, where:

            - ``w`` -- a word of length ``self.parent().ell`` over the
              letters `1` up to ``self.parent().n``;
            - ``breaks`` is a list of de-concatenation points to turn ``w``
              into a list of row words of (skew-)tableaux that represent
              `b` under the minimaj bijection `\\phi` of [BCHOPSY2017]_.

            The pair ``(w, breaks)`` may be recovered via ``b.value``.
        """
        def __iter__(self):
            """
            Iterate over ``self._minimaj_blocks_from_word_pair()``.

            EXAMPLES::

                sage: b = crystals.Minimaj(4,5,3).an_element(); b                       # needs sage.modules
                ((2, 3, 1), (1,), (1,))
                sage: b.value                                                           # needs sage.modules
                ([1, 3, 2, 1, 1], (0, 1, 2, 5))
                sage: list(b)                                                           # needs sage.modules
                [(2, 3, 1), (1,), (1,)]
            """
        def to_tableaux_words(self):
            """
            Return the image of the ordered multiset partition into sets ``self``
            under the minimaj bijection `\\phi` of [BCHOPSY2017]_.

            EXAMPLES::

                sage: # needs sage.modules
                sage: B = crystals.Minimaj(4,5,3)
                sage: b = B.an_element(); b
                ((2, 3, 1), (1,), (1,))
                sage: b.to_tableaux_words()
                [[1], [3], [2, 1, 1]]
                sage: b = B([[1,3,4], [3], [3]]); b
                ((4, 1, 3), (3,), (3,))
                sage: b.to_tableaux_words()
                [[3, 1], [], [4, 3, 3]]
            """
        def e(self, i):
            """
            Return `e_i` on ``self``.

            EXAMPLES::

                sage: B = crystals.Minimaj(4,3,2)                                       # needs sage.modules
                sage: b = B([[2,3], [3]]); b                                            # needs sage.modules
                ((2, 3), (3,))
                sage: [b.e(i) for i in range(1,4)]                                      # needs sage.modules
                [((1, 3), (3,)), ((2,), (2, 3)), None]
            """
        def f(self, i):
            """
            Return `f_i` on ``self``.

            EXAMPLES::

                sage: B = crystals.Minimaj(4,3,2)                                       # needs sage.modules
                sage: b = B([[2,3], [3]]); b                                            # needs sage.modules
                ((2, 3), (3,))
                sage: [b.f(i) for i in range(1,4)]                                      # needs sage.modules
                [None, None, ((2, 3), (4,))]
            """
