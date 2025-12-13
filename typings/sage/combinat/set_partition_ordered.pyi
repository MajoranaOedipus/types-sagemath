from _typeshed import Incomplete
from sage.arith.misc import factorial as factorial, multinomial as multinomial
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.categories.infinite_enumerated_sets import InfiniteEnumeratedSets as InfiniteEnumeratedSets
from sage.combinat.combinat import stirling_number2 as stirling_number2
from sage.combinat.combinatorial_map import combinatorial_map as combinatorial_map
from sage.combinat.composition import Composition as Composition, Compositions as Compositions
from sage.combinat.words.finite_word import FiniteWord_class as FiniteWord_class
from sage.combinat.words.words import Words as Words
from sage.misc.inherit_comparison import InheritComparisonClasscallMetaclass as InheritComparisonClasscallMetaclass
from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.sets.finite_enumerated_set import FiniteEnumeratedSet as FiniteEnumeratedSet
from sage.sets.set import Set as Set, Set_generic as Set_generic
from sage.structure.element import parent as parent
from sage.structure.list_clone import ClonableArray as ClonableArray
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import richcmp as richcmp
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class OrderedSetPartition(ClonableArray, metaclass=InheritComparisonClasscallMetaclass):
    """
    An ordered partition of a set.

    An ordered set partition `p` of a set `s` is a list of pairwise
    disjoint nonempty subsets of `s` such that the union of these
    subsets is `s`. These subsets are called the parts of the partition.

    We represent an ordered set partition as a list of sets. By
    extension, an ordered set partition of a nonnegative integer `n` is
    the set partition of the integers from `1` to `n`. The number of
    ordered set partitions of `n` is called the `n`-th ordered Bell
    number.

    There is a natural integer composition associated with an ordered
    set partition, that is the sequence of sizes of all its parts in
    order.

    The number `T_n` of ordered set partitions of
    `\\{ 1, 2, \\ldots, n \\}` is the so-called `n`-th *Fubini number*
    (also known as the `n`-th ordered Bell number; see
    :wikipedia:`Ordered Bell number`). Its exponential generating
    function is

    .. MATH::

        \\sum_n \\frac{T_n}{n!} x^n = \\frac{1}{2-e^x}.

    (See sequence :oeis:`A000670` in OEIS.)

    INPUT:

    - ``parts`` -- an object or iterable that defines an ordered set partition
      (e.g., a list of pairwise disjoint sets) or a packed word (e.g., a list
      of letters on some alphabet). If there is ambiguity and if the input should
      be treated as a packed word, the keyword ``from_word`` should be used.

    EXAMPLES:

    There are 13 ordered set partitions of `\\{1,2,3\\}`::

        sage: OrderedSetPartitions(3).cardinality()
        13

    Here is the list of them::

        sage: OrderedSetPartitions(3).list()
        [[{1}, {2}, {3}],
         [{1}, {3}, {2}],
         [{2}, {1}, {3}],
         [{3}, {1}, {2}],
         [{2}, {3}, {1}],
         [{3}, {2}, {1}],
         [{1}, {2, 3}],
         [{2}, {1, 3}],
         [{3}, {1, 2}],
         [{1, 2}, {3}],
         [{1, 3}, {2}],
         [{2, 3}, {1}],
         [{1, 2, 3}]]

    There are 12 ordered set partitions of `\\{1,2,3,4\\}` whose underlying
    composition is `[1,2,1]`::

        sage: OrderedSetPartitions(4,[1,2,1]).list()
        [[{1}, {2, 3}, {4}],
         [{1}, {2, 4}, {3}],
         [{1}, {3, 4}, {2}],
         [{2}, {1, 3}, {4}],
         [{2}, {1, 4}, {3}],
         [{3}, {1, 2}, {4}],
         [{4}, {1, 2}, {3}],
         [{3}, {1, 4}, {2}],
         [{4}, {1, 3}, {2}],
         [{2}, {3, 4}, {1}],
         [{3}, {2, 4}, {1}],
         [{4}, {2, 3}, {1}]]

    Since :issue:`14140`, we can create an ordered set partition directly by
    :class:`OrderedSetPartition` which creates the parent object by taking the
    union of the partitions passed in. However it is recommended and
    (marginally) faster to create the parent first and then create the ordered
    set partition from that. ::

        sage: s = OrderedSetPartition([[1,3],[2,4]]); s
        [{1, 3}, {2, 4}]
        sage: s.parent()
        Ordered set partitions of {1, 2, 3, 4}

    We can construct the ordered set partition from a word,
    which we consider as packed::

        sage: OrderedSetPartition([2,4,1,2])
        [{3}, {1, 4}, {2}]
        sage: OrderedSetPartition(from_word=[2,4,1,2])
        [{3}, {1, 4}, {2}]
        sage: OrderedSetPartition(from_word='bdab')
        [{3}, {1, 4}, {2}]

    .. WARNING::

        The elements of the underlying set should be hashable.

    REFERENCES:

    :wikipedia:`Ordered_partition_of_a_set`
    """
    @staticmethod
    def __classcall_private__(cls, parts=None, from_word=None, check: bool = True):
        """
        Create a set partition from ``parts`` with the appropriate parent.

        EXAMPLES::

            sage: s = OrderedSetPartition([[1,3],[2,4]]); s
            [{1, 3}, {2, 4}]
            sage: s.parent()
            Ordered set partitions of {1, 2, 3, 4}
            sage: t = OrderedSetPartition([[2,4],[1,3]]); t
            [{2, 4}, {1, 3}]
            sage: s != t
            True
            sage: OrderedSetPartition()
            []
            sage: OrderedSetPartition([])
            []
            sage: OrderedSetPartition('')
            []
            sage: OrderedSetPartition('bdab') == OrderedSetPartition(from_word='bdab')
            True
            sage: OrderedSetPartition('bdab') == OrderedSetPartition(Word('bdab'))
            True
        """
    def __init__(self, parent, s, check: bool = True) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: OS = OrderedSetPartitions(4)
            sage: s = OS([[1, 3], [2, 4]])
            sage: TestSuite(s).run()
        """
    def check(self) -> None:
        """
        Check that we are a valid ordered set partition.

        EXAMPLES::

            sage: OS = OrderedSetPartitions(4)
            sage: s = OS([[1, 3], [2, 4]])
            sage: s.check()
        """
    def base_set(self):
        """
        Return the base set of ``self``.

        This is the union of all parts of ``self``.

        EXAMPLES::

            sage: OrderedSetPartition([[1], [2,3], [4]]).base_set()
            frozenset({1, 2, 3, 4})
            sage: OrderedSetPartition([[1,2,3,4]]).base_set()
            frozenset({1, 2, 3, 4})
            sage: OrderedSetPartition([]).base_set()
            frozenset()

        TESTS::

            sage: S = OrderedSetPartitions()
            sage: x = S([['a', 'c', 'e'], ['b', 'd']])
            sage: x.base_set()
            frozenset({'a', 'b', 'c', 'd', 'e'})
        """
    def base_set_cardinality(self):
        """
        Return the cardinality of the base set of ``self``.

        This is the sum of the sizes of the parts of ``self``.

        This is also known as the *size* (sometimes the *weight*) of
        an ordered set partition.

        EXAMPLES::

            sage: OrderedSetPartition([[1], [2,3], [4]]).base_set_cardinality()
            4
            sage: OrderedSetPartition([[1,2,3,4]]).base_set_cardinality()
            4

        TESTS::

            sage: S = OrderedSetPartitions()
            sage: S([[1,4],[3],[2]]).base_set_cardinality()
            4
        """
    size = base_set_cardinality
    def length(self):
        """
        Return the number of parts of ``self``.

        EXAMPLES::

            sage: OS = OrderedSetPartitions(4)
            sage: s = OS([[1, 3], [2, 4]])
            sage: s.length()
            2
        """
    def to_composition(self):
        """
        Return the integer composition whose parts are the sizes of the sets
        in ``self``.

        EXAMPLES::

            sage: S = OrderedSetPartitions(5)
            sage: x = S([[3,5,4], [1, 2]])
            sage: x.to_composition()
            [3, 2]
            sage: y = S([[3,1], [2], [5,4]])
            sage: y.to_composition()
            [2, 1, 2]
        """
    @staticmethod
    def sum(osps):
        """
        Return the concatenation of the given ordered set partitions
        ``osps`` (provided they have no elements in common).

        INPUT:

        - ``osps`` -- list (or iterable) of ordered set partitions

        EXAMPLES::

            sage: OrderedSetPartition.sum([OrderedSetPartition([[4, 1], [3]]), OrderedSetPartition([[7], [2]]), OrderedSetPartition([[5, 6]])])
            [{1, 4}, {3}, {7}, {2}, {5, 6}]

        Any iterable can be provided as input::

            sage: OrderedSetPartition.sum([OrderedSetPartition([[2*i,2*i+1]]) for i in [4,1,3]])
            [{8, 9}, {2, 3}, {6, 7}]

        Empty inputs are handled gracefully::

            sage: OrderedSetPartition.sum([]) == OrderedSetPartition([])
            True

        TESTS::

            sage: A = OrderedSetPartitions(3)([[2], [1, 3]])
            sage: B = OrderedSetPartitions([5])([[5]])
            sage: C = OrderedSetPartition.sum([A, B]); C
            [{2}, {1, 3}, {5}]
            sage: C.parent()
            Ordered set partitions of {1, 2, 3, 5}
        """
    def reversed(self):
        """
        Return the reversal of the ordered set partition ``self``.

        The *reversal* of an ordered set partition
        `(P_1, P_2, \\ldots, P_k)` is defined to be the ordered
        set partition `(P_k, P_{k-1}, \\ldots, P_1)`.

        EXAMPLES::

            sage: OrderedSetPartition([[1, 3], [2]]).reversed()
            [{2}, {1, 3}]
            sage: OrderedSetPartition([[1, 5], [2, 4]]).reversed()
            [{2, 4}, {1, 5}]
            sage: OrderedSetPartition([[-1], [-2], [3, 4], [0]]).reversed()
            [{0}, {3, 4}, {-2}, {-1}]
            sage: OrderedSetPartition([]).reversed()
            []
        """
    def complement(self):
        """
        Return the complement of the ordered set partition ``self``.

        This assumes that ``self`` is an ordered set partition of
        an interval of `\\ZZ`.

        Let `(P_1, P_2, \\ldots, P_k)` be an ordered set partition
        of some interval `I` of `\\ZZ`. Let `\\omega` be the unique
        strictly decreasing bijection `I \\to I`. Then, the
        *complement* of `(P_1, P_2, \\ldots, P_k)` is defined to be
        the ordered set partition
        `(\\omega(P_1), \\omega(P_2), \\ldots, \\omega(P_k))`.

        EXAMPLES::

            sage: OrderedSetPartition([[1, 2], [3]]).complement()
            [{2, 3}, {1}]
            sage: OrderedSetPartition([[1, 3], [2]]).complement()
            [{1, 3}, {2}]
            sage: OrderedSetPartition([[2, 3]]).complement()
            [{2, 3}]
            sage: OrderedSetPartition([[1, 5], [2, 3], [4]]).complement()
            [{1, 5}, {3, 4}, {2}]
            sage: OrderedSetPartition([[-1], [-2], [1, 2], [0]]).complement()
            [{1}, {2}, {-2, -1}, {0}]
            sage: OrderedSetPartition([]).complement()
            []
        """
    def finer(self):
        '''
        Return the set of ordered set partitions which are finer
        than ``self``.

        See :meth:`is_finer` for the definition of "finer".

        EXAMPLES::

            sage: C = OrderedSetPartition([[1, 3], [2]]).finer()
            sage: C.cardinality()
            3
            sage: C.list()
            [[{1}, {3}, {2}], [{3}, {1}, {2}], [{1, 3}, {2}]]

            sage: OrderedSetPartition([]).finer()
            {[]}

            sage: W = OrderedSetPartition([[4, 9], [-1, 2]])
            sage: W.finer().list()
            [[{9}, {4}, {2}, {-1}],
             [{9}, {4}, {-1}, {2}],
             [{9}, {4}, {-1, 2}],
             [{4}, {9}, {2}, {-1}],
             [{4}, {9}, {-1}, {2}],
             [{4}, {9}, {-1, 2}],
             [{4, 9}, {2}, {-1}],
             [{4, 9}, {-1}, {2}],
             [{4, 9}, {-1, 2}]]
        '''
    def is_finer(self, co2):
        """
        Return ``True`` if the ordered set partition ``self`` is finer
        than the ordered set partition ``co2``; otherwise, return ``False``.

        If `A` and `B` are two ordered set partitions of the same set,
        then `A` is said to be *finer* than `B` if `B` can be obtained
        from `A` by (repeatedly) merging consecutive parts.
        In this case, we say that `B` is *fatter* than `A`.

        EXAMPLES::

            sage: A = OrderedSetPartition([[1, 3], [2]])
            sage: B = OrderedSetPartition([[1], [3], [2]])
            sage: A.is_finer(B)
            False
            sage: B.is_finer(A)
            True
            sage: C = OrderedSetPartition([[3], [1], [2]])
            sage: A.is_finer(C)
            False
            sage: C.is_finer(A)
            True
            sage: OrderedSetPartition([[2], [5], [1], [4]]).is_finer(OrderedSetPartition([[2, 5], [1, 4]]))
            True
            sage: OrderedSetPartition([[5], [2], [1], [4]]).is_finer(OrderedSetPartition([[2, 5], [1, 4]]))
            True
            sage: OrderedSetPartition([[2], [1], [5], [4]]).is_finer(OrderedSetPartition([[2, 5], [1, 4]]))
            False
            sage: OrderedSetPartition([[2, 5, 1], [4]]).is_finer(OrderedSetPartition([[2, 5], [1, 4]]))
            False
        """
    def fatten(self, grouping):
        '''
        Return the ordered set partition fatter than ``self``, obtained
        by grouping together consecutive parts according to the integer
        composition ``grouping``.

        See :meth:`finer` for the definition of "fatter".

        INPUT:

        - ``grouping`` -- a composition whose sum is the length of ``self``

        EXAMPLES:

        Let us start with the ordered set partition::

            sage: c = OrderedSetPartition([[2, 5], [1], [3, 4]])

        With ``grouping`` equal to `(1, \\ldots, 1)`, `c` is left unchanged::

            sage: c.fatten(Composition([1,1,1]))
            [{2, 5}, {1}, {3, 4}]

        With ``grouping`` equal to `(\\ell)` where `\\ell` is the length of
        `c`, this yields the coarsest ordered set partition above `c`::

            sage: c.fatten(Composition([3]))
            [{1, 2, 3, 4, 5}]

        Other values for ``grouping`` yield (all the) other ordered
        set partitions coarser than `c`::

            sage: c.fatten(Composition([2,1]))
            [{1, 2, 5}, {3, 4}]
            sage: c.fatten(Composition([1,2]))
            [{2, 5}, {1, 3, 4}]

        TESTS::

            sage: OrderedSetPartition([]).fatten(Composition([]))
            []
            sage: c.fatten(Composition([2,1])).__class__ == c.__class__
            True
        '''
    def fatter(self):
        '''
        Return the set of ordered set partitions which are fatter
        than ``self``.

        See :meth:`finer` for the definition of "fatter".

        EXAMPLES::

            sage: C = OrderedSetPartition([[2, 5], [1], [3, 4]]).fatter()
            sage: C.cardinality()
            4
            sage: sorted(C)
            [[{2, 5}, {1}, {3, 4}],
             [{2, 5}, {1, 3, 4}],
             [{1, 2, 5}, {3, 4}],
             [{1, 2, 3, 4, 5}]]

            sage: OrderedSetPartition([[4, 9], [-1, 2]]).fatter().list()
            [[{4, 9}, {-1, 2}], [{-1, 2, 4, 9}]]

        Some extreme cases::

            sage: list(OrderedSetPartition([[5]]).fatter())
            [[{5}]]
            sage: list(Composition([]).fatter())
            [[]]
            sage: sorted(OrderedSetPartition([[1], [2], [3], [4]]).fatter())
            [[{1}, {2}, {3}, {4}],
             [{1}, {2}, {3, 4}],
             [{1}, {2, 3}, {4}],
             [{1}, {2, 3, 4}],
             [{1, 2}, {3}, {4}],
             [{1, 2}, {3, 4}],
             [{1, 2, 3}, {4}],
             [{1, 2, 3, 4}]]
        '''
    @staticmethod
    def bottom_up_osp(X, comp):
        """
        Return the ordered set partition obtained by listing the
        elements of the set ``X`` in increasing order, and
        placing bars between some of them according to the
        integer composition ``comp`` (namely, the bars are placed
        in such a way that the lengths of the resulting blocks are
        exactly the entries of ``comp``).

        INPUT:

        - ``X`` -- a finite set (or list or tuple)

        - ``comp`` -- a composition whose sum is the size of ``X``
          (can be given as a list or tuple or composition)

        EXAMPLES::

            sage: buo = OrderedSetPartition.bottom_up_osp
            sage: buo(Set([1, 4, 7, 9]), [2, 1, 1])
            [{1, 4}, {7}, {9}]
            sage: buo(Set([1, 4, 7, 9]), [1, 3])
            [{1}, {4, 7, 9}]
            sage: buo(Set([1, 4, 7, 9]), [1, 1, 1, 1])
            [{1}, {4}, {7}, {9}]
            sage: buo(range(8), [1, 4, 2, 1])
            [{0}, {1, 2, 3, 4}, {5, 6}, {7}]
            sage: buo([], [])
            []

        TESTS::

            sage: buo = OrderedSetPartition.bottom_up_osp
            sage: parent(buo(Set([1, 4, 7, 9]), [2, 1, 1]))
            Ordered set partitions of {1, 4, 9, 7}
            sage: buo((3, 5, 6), (2, 1))
            [{3, 5}, {6}]
            sage: buo([3, 5, 6], Composition([1, 2]))
            [{3}, {5, 6}]
        """
    def strongly_finer(self):
        '''
        Return the set of ordered set partitions which are strongly
        finer than ``self``.

        See :meth:`is_strongly_finer` for the definition of "strongly
        finer".

        EXAMPLES::

            sage: C = OrderedSetPartition([[1, 3], [2]]).strongly_finer()
            sage: C.cardinality()
            2
            sage: C.list()
            [[{1}, {3}, {2}], [{1, 3}, {2}]]

            sage: OrderedSetPartition([]).strongly_finer()
            {[]}

            sage: W = OrderedSetPartition([[4, 9], [-1, 2]])
            sage: W.strongly_finer().list()
            [[{4}, {9}, {-1}, {2}],
             [{4}, {9}, {-1, 2}],
             [{4, 9}, {-1}, {2}],
             [{4, 9}, {-1, 2}]]
        '''
    def is_strongly_finer(self, co2):
        """
        Return ``True`` if the ordered set partition ``self`` is strongly
        finer than the ordered set partition ``co2``; otherwise, return
        ``False``.

        If `A` and `B` are two ordered set partitions of the same set,
        then `A` is said to be *strongly finer* than `B` if `B` can be
        obtained from `A` by (repeatedly) merging consecutive parts,
        provided that every time we merge two consecutive parts `C_i`
        and `C_{i+1}`, we have `\\max C_i < \\min C_{i+1}`.
        In this case, we say that `B` is *strongly fatter* than `A`.

        EXAMPLES::

            sage: A = OrderedSetPartition([[1, 3], [2]])
            sage: B = OrderedSetPartition([[1], [3], [2]])
            sage: A.is_strongly_finer(B)
            False
            sage: B.is_strongly_finer(A)
            True
            sage: C = OrderedSetPartition([[3], [1], [2]])
            sage: A.is_strongly_finer(C)
            False
            sage: C.is_strongly_finer(A)
            False
            sage: OrderedSetPartition([[2], [5], [1], [4]]).is_strongly_finer(OrderedSetPartition([[2, 5], [1, 4]]))
            True
            sage: OrderedSetPartition([[5], [2], [1], [4]]).is_strongly_finer(OrderedSetPartition([[2, 5], [1, 4]]))
            False
            sage: OrderedSetPartition([[2], [1], [5], [4]]).is_strongly_finer(OrderedSetPartition([[2, 5], [1, 4]]))
            False
            sage: OrderedSetPartition([[2, 5, 1], [4]]).is_strongly_finer(OrderedSetPartition([[2, 5], [1, 4]]))
            False
        """
    def strongly_fatter(self):
        '''
        Return the set of ordered set partitions which are strongly fatter
        than ``self``.

        See :meth:`strongly_finer` for the definition of "strongly fatter".

        EXAMPLES::

            sage: C = OrderedSetPartition([[2, 5], [1], [3, 4]]).strongly_fatter()
            sage: C.cardinality()
            2
            sage: sorted(C)
            [[{2, 5}, {1}, {3, 4}], [{2, 5}, {1, 3, 4}]]

            sage: OrderedSetPartition([[4, 9], [-1, 2]]).strongly_fatter().list()
            [[{4, 9}, {-1, 2}]]

        Some extreme cases::

            sage: list(OrderedSetPartition([[5]]).strongly_fatter())
            [[{5}]]
            sage: list(OrderedSetPartition([]).strongly_fatter())
            [[]]
            sage: sorted(OrderedSetPartition([[1], [2], [3], [4]]).strongly_fatter())
            [[{1}, {2}, {3}, {4}],
             [{1}, {2}, {3, 4}],
             [{1}, {2, 3}, {4}],
             [{1}, {2, 3, 4}],
             [{1, 2}, {3}, {4}],
             [{1, 2}, {3, 4}],
             [{1, 2, 3}, {4}],
             [{1, 2, 3, 4}]]
            sage: sorted(OrderedSetPartition([[1], [3], [2], [4]]).strongly_fatter())
            [[{1}, {3}, {2}, {4}],
             [{1}, {3}, {2, 4}],
             [{1, 3}, {2}, {4}],
             [{1, 3}, {2, 4}]]
            sage: sorted(OrderedSetPartition([[4], [1], [5], [3]]).strongly_fatter())
            [[{4}, {1}, {5}, {3}], [{4}, {1, 5}, {3}]]
        '''
    def to_packed_word(self):
        """
        Return the packed word on alphabet `\\{1,2,3,\\ldots\\}`
        corresponding to ``self``.

        A *packed word* on alphabet `\\{1,2,3,\\ldots\\}` is any word whose
        maximum letter is the same as its total number of distinct letters.
        Let `P` be an ordered set partition of a set `X`.
        The corresponding packed word `w_1 w_2 \\cdots w_n` is constructed
        by having letter `w_i = j` if the `i`-th smallest entry in `X`
        occurs in the `j`-th block of `P`.

        .. SEEALSO::

            :meth:`Word.to_ordered_set_partition`

        .. WARNING::

            This assumes there is a total order on the underlying
            set.

        EXAMPLES::

            sage: S = OrderedSetPartitions()
            sage: x = S([[3,5], [2], [1,4,6]])
            sage: x.to_packed_word()
            word: 321313

            sage: x = S([['a', 'c', 'e'], ['b', 'd']])
            sage: x.to_packed_word()
            word: 12121
        """
    def number_of_inversions(self):
        """
        Return the number of inversions in ``self``.

        An inversion of an ordered set partition with blocks
        `[B_1,B_2, \\ldots, B_k]` is a pair of letters `i` and `j` with `i < j`
        such that `i` is minimal in `B_m`, `j \\in B_l`, and `l < m`.

        REFERENCES:

        - [Wilson2016]_

        EXAMPLES::

            sage: OrderedSetPartition([{2,5},{4,6},{1,3}]).number_of_inversions()
            5
            sage: OrderedSetPartition([{1,3,8},{2,4},{5,6,7}]).number_of_inversions()
            3

        TESTS::

            sage: OrderedSetPartition([{1,3,8},{2,4},{5,6,7}]).number_of_inversions().parent()
            Integer Ring
        """

class OrderedSetPartitions(UniqueRepresentation, Parent):
    '''
    Return the combinatorial class of ordered set partitions of ``s``.

    The optional argument ``c``, if specified, restricts the parts of
    the partition to have certain sizes (the entries of ``c``).

    EXAMPLES::

        sage: OS = OrderedSetPartitions([1,2,3,4]); OS
        Ordered set partitions of {1, 2, 3, 4}
        sage: OS.cardinality()
        75
        sage: OS.first()
        [{1}, {2}, {3}, {4}]
        sage: OS.last()
        [{1, 2, 3, 4}]
        sage: OS.random_element().parent() is OS
        True

    ::

        sage: OS = OrderedSetPartitions([1,2,3,4], [2,2]); OS
        Ordered set partitions of {1, 2, 3, 4} into parts of size [2, 2]
        sage: OS.cardinality()
        6
        sage: OS.first()
        [{1, 2}, {3, 4}]
        sage: OS.last()
        [{3, 4}, {1, 2}]
        sage: OS.list()
        [[{1, 2}, {3, 4}],
         [{1, 3}, {2, 4}],
         [{1, 4}, {2, 3}],
         [{2, 3}, {1, 4}],
         [{2, 4}, {1, 3}],
         [{3, 4}, {1, 2}]]

    ::

        sage: OS = OrderedSetPartitions("cat")
        sage: OS  # random
        Ordered set partitions of {\'a\', \'t\', \'c\'}
        sage: sorted(OS.list(), key=str)
        [[{\'a\', \'c\', \'t\'}],
         [{\'a\', \'c\'}, {\'t\'}],
         [{\'a\', \'t\'}, {\'c\'}],
         [{\'a\'}, {\'c\', \'t\'}],
         [{\'a\'}, {\'c\'}, {\'t\'}],
         [{\'a\'}, {\'t\'}, {\'c\'}],
         [{\'c\', \'t\'}, {\'a\'}],
         [{\'c\'}, {\'a\', \'t\'}],
         [{\'c\'}, {\'a\'}, {\'t\'}],
         [{\'c\'}, {\'t\'}, {\'a\'}],
         [{\'t\'}, {\'a\', \'c\'}],
         [{\'t\'}, {\'a\'}, {\'c\'}],
         [{\'t\'}, {\'c\'}, {\'a\'}]]

    TESTS::

        sage: S = OrderedSetPartitions()
        sage: x = S([[3,5], [2], [1,4,6]])
        sage: x.parent()
        Ordered set partitions
    '''
    @staticmethod
    def __classcall_private__(cls, s=None, c=None):
        """
        Choose the correct parent based upon input.

        EXAMPLES::

            sage: OrderedSetPartitions(4)
            Ordered set partitions of {1, 2, 3, 4}
            sage: OrderedSetPartitions(4, [1, 2, 1])
            Ordered set partitions of {1, 2, 3, 4} into parts of size [1, 2, 1]
        """
    def __init__(self, s) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: OS = OrderedSetPartitions(4)
            sage: TestSuite(OS).run()
        """
    Element = OrderedSetPartition
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: OS = OrderedSetPartitions([1,2,3,4])
            sage: all(sp in OS for sp in OS)
            True
            sage: [[1,2], [], [3,4]] in OS
            False
            sage: [Set([1,2]), Set([3,4])] in OS
            True
            sage: [set([1,2]), set([3,4])] in OS
            True

        Make sure the set really matches::

            sage: [set([5,6]), set([3,4])] in OS
            False
        """
    def from_finite_word(self, w, check: bool = True):
        """
        Return the unique ordered set partition of `\\{1, 2, \\ldots, n\\}` corresponding
        to a word `w` of length `n`.

        .. SEEALSO::

            :meth:`Word.to_ordered_set_partition`

        EXAMPLES::

            sage: A = OrderedSetPartitions().from_finite_word('abcabcabd'); A
            [{1, 4, 7}, {2, 5, 8}, {3, 6}, {9}]
            sage: B = OrderedSetPartitions().from_finite_word([1,2,3,1,2,3,1,2,4])
            sage: A == B
            True

        TESTS::

            sage: A = OrderedSetPartitions().from_finite_word('abcabca')
            sage: A.parent()
            Ordered set partitions

            sage: A = OrderedSetPartitions(7).from_finite_word('abcabca')
            sage: A.parent()
            Ordered set partitions of {1, 2, 3, 4, 5, 6, 7}
        """

class OrderedSetPartitions_s(OrderedSetPartitions):
    """
    Class of ordered partitions of a set `S`.
    """
    def cardinality(self):
        """
        EXAMPLES::

            sage: OrderedSetPartitions(0).cardinality()
            1
            sage: OrderedSetPartitions(1).cardinality()
            1
            sage: OrderedSetPartitions(2).cardinality()
            3
            sage: OrderedSetPartitions(3).cardinality()
            13
            sage: OrderedSetPartitions([1,2,3]).cardinality()
            13
            sage: OrderedSetPartitions(4).cardinality()
            75
            sage: OrderedSetPartitions(5).cardinality()
            541
        """
    def __iter__(self):
        """
        EXAMPLES::

            sage: list(OrderedSetPartitions([1,2,3]))
            [[{1}, {2}, {3}],
             [{1}, {3}, {2}],
             [{2}, {1}, {3}],
             [{3}, {1}, {2}],
             [{2}, {3}, {1}],
             [{3}, {2}, {1}],
             [{1}, {2, 3}],
             [{2}, {1, 3}],
             [{3}, {1, 2}],
             [{1, 2}, {3}],
             [{1, 3}, {2}],
             [{2, 3}, {1}],
             [{1, 2, 3}]]

        TESTS:

        Test for :issue:`35654`::

            sage: OrderedSetPartitions(set(),[0,0,0]).list()
            [[{}, {}, {}]]
        """

class OrderedSetPartitions_sn(OrderedSetPartitions):
    n: Incomplete
    def __init__(self, s, n) -> None:
        """
        TESTS::

            sage: OS = OrderedSetPartitions([1,2,3,4], 2)
            sage: OS == loads(dumps(OS))
            True
        """
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: OS = OrderedSetPartitions([1,2,3,4], 2)
            sage: all(sp in OS for sp in OS)
            True
            sage: OS.cardinality()
            14
            sage: len([x for x in OrderedSetPartitions([1,2,3,4]) if x in OS])
            14
        """
    def cardinality(self):
        """
        Return the cardinality of ``self``.

        The number of ordered partitions of a set of size `n` into `k`
        parts is equal to `k! S(n,k)` where `S(n,k)` denotes the Stirling
        number of the second kind.

        EXAMPLES::

            sage: OrderedSetPartitions(4,2).cardinality()
            14
            sage: OrderedSetPartitions(4,1).cardinality()
            1
        """
    def __iter__(self):
        """
        EXAMPLES::

            sage: [ p for p in OrderedSetPartitions([1,2,3,4], 2) ]
            [[{1, 2, 3}, {4}],
             [{1, 2, 4}, {3}],
             [{1, 3, 4}, {2}],
             [{2, 3, 4}, {1}],
             [{1, 2}, {3, 4}],
             [{1, 3}, {2, 4}],
             [{1, 4}, {2, 3}],
             [{2, 3}, {1, 4}],
             [{2, 4}, {1, 3}],
             [{3, 4}, {1, 2}],
             [{1}, {2, 3, 4}],
             [{2}, {1, 3, 4}],
             [{3}, {1, 2, 4}],
             [{4}, {1, 2, 3}]]
        """

class OrderedSetPartitions_scomp(OrderedSetPartitions):
    c: Incomplete
    def __init__(self, s, comp) -> None:
        """
        TESTS::

            sage: OS = OrderedSetPartitions([1,2,3,4], [2,1,1])
            sage: OS == loads(dumps(OS))
            True
        """
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: OS = OrderedSetPartitions([1,2,3,4], [2,1,1])
            sage: all(sp in OS for sp in OS)
            True
            sage: OS.cardinality()
            12
            sage: len([x for x in OrderedSetPartitions([1,2,3,4]) if x in OS])
            12
        """
    def cardinality(self):
        """
        Return the cardinality of ``self``.

        The number of ordered set partitions of a set of length `k` with
        composition shape `\\mu` is equal to

        .. MATH::

            \\frac{k!}{\\prod_{\\mu_i \\neq 0} \\mu_i!}.

        EXAMPLES::

            sage: OrderedSetPartitions(5,[2,3]).cardinality()
            10
            sage: OrderedSetPartitions(0, []).cardinality()
            1
            sage: OrderedSetPartitions(0, [0]).cardinality()
            1
            sage: OrderedSetPartitions(0, [0,0]).cardinality()
            1
            sage: OrderedSetPartitions(5, [2,0,3]).cardinality()
            10
        """
    def __iter__(self):
        """
        TESTS::

            sage: [ p for p in OrderedSetPartitions([1,2,3,4], [2,1,1]) ]
            [[{1, 2}, {3}, {4}],
             [{1, 2}, {4}, {3}],
             [{1, 3}, {2}, {4}],
             [{1, 4}, {2}, {3}],
             [{1, 3}, {4}, {2}],
             [{1, 4}, {3}, {2}],
             [{2, 3}, {1}, {4}],
             [{2, 4}, {1}, {3}],
             [{3, 4}, {1}, {2}],
             [{2, 3}, {4}, {1}],
             [{2, 4}, {3}, {1}],
             [{3, 4}, {2}, {1}]]

            sage: len(OrderedSetPartitions([1,2,3,4], [1,1,1,1]))
            24

            sage: [ x for x in OrderedSetPartitions([1,4,7], [3]) ]
            [[{1, 4, 7}]]

            sage: [ x for x in OrderedSetPartitions([1,4,7], [1,2]) ]
            [[{1}, {4, 7}], [{4}, {1, 7}], [{7}, {1, 4}]]

            sage: [ p for p in OrderedSetPartitions([], []) ]
            [[]]

            sage: [ p for p in OrderedSetPartitions([1], [1]) ]
            [[{1}]]

        Let us check that it works for large size (:issue:`16646`)::

            sage: OrderedSetPartitions(42).first()
            [{1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12},
            {13}, {14}, {15}, {16}, {17}, {18}, {19}, {20}, {21}, {22}, {23},
            {24}, {25}, {26}, {27}, {28}, {29}, {30}, {31}, {32}, {33}, {34},
            {35}, {36}, {37}, {38}, {39}, {40}, {41}, {42}]

        EXAMPLES::

            sage: list(OrderedSetPartitions(range(5), [2,1,2]))
            [[{0, 1}, {2}, {3, 4}],
             [{0, 1}, {3}, {2, 4}],
            ...
             [{2, 4}, {3}, {0, 1}],
             [{3, 4}, {2}, {0, 1}]]
        """

def multiset_permutation_to_ordered_set_partition(l, m):
    """
    Convert a multiset permutation to an ordered set partition.

    INPUT:

    - ``l`` -- a multiset permutation
    - ``m`` -- number of parts

    EXAMPLES::

        sage: from sage.combinat.set_partition_ordered import multiset_permutation_to_ordered_set_partition
        sage: l = [0, 0, 1, 1, 2]
        sage: multiset_permutation_to_ordered_set_partition(l, 3)
        [[0, 1], [2, 3], [4]]
    """
def multiset_permutation_next_lex(l):
    """
    Return the next multiset permutation after ``l``.

    EXAMPLES::

        sage: from sage.combinat.set_partition_ordered import multiset_permutation_next_lex
        sage: l = [0, 0, 1, 1, 2]
        sage: while multiset_permutation_next_lex(l):
        ....:     print(l)
        [0, 0, 1, 2, 1]
        [0, 0, 2, 1, 1]
        [0, 1, 0, 1, 2]
        [0, 1, 0, 2, 1]
        [0, 1, 1, 0, 2]
        [0, 1, 1, 2, 0]
        ...
        [1, 1, 2, 0, 0]
        [1, 2, 0, 0, 1]
        [1, 2, 0, 1, 0]
        [1, 2, 1, 0, 0]
        [2, 0, 0, 1, 1]
        [2, 0, 1, 0, 1]
        [2, 0, 1, 1, 0]
        [2, 1, 0, 0, 1]
        [2, 1, 0, 1, 0]
        [2, 1, 1, 0, 0]

    TESTS:

    Test for :issue:`35654`::

        sage: multiset_permutation_next_lex([])
        0
    """

class OrderedSetPartitions_all(OrderedSetPartitions):
    """
    Ordered set partitions of `\\{1, \\ldots, n\\}` for all
    `n \\in \\ZZ_{\\geq 0}`.
    """
    def __init__(self) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: OS = OrderedSetPartitions()
            sage: TestSuite(OS).run()  # long time
        """
    def subset(self, size=None, **kwargs):
        """
        Return the subset of ordered set partitions of a given
        size and additional keyword arguments.

        EXAMPLES::

            sage: P = OrderedSetPartitions()
            sage: P.subset(4)
            Ordered set partitions of {1, 2, 3, 4}
        """
    def __iter__(self):
        """
        Iterate over ``self``.

        EXAMPLES::

            sage: it = iter(OrderedSetPartitions())
            sage: [next(it) for _ in range(10)]
            [[], [{1}], [{1}, {2}], [{2}, {1}], [{1, 2}],
             [{1}, {2}, {3}], [{1}, {3}, {2}], [{2}, {1}, {3}],
             [{3}, {1}, {2}], [{2}, {3}, {1}]]
        """
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: OS = OrderedSetPartitions([1,2,3,4])
            sage: AOS = OrderedSetPartitions()
            sage: all(sp in AOS for sp in OS)
            True
            sage: AOS.__contains__([[1,3], [4], [5,2]])
            True
            sage: AOS.__contains__([Set([1,3]), Set([4]), Set([5,2])])
            True
            sage: [Set([1,4]), Set([3])] in AOS
            False
            sage: [Set([1,3]), Set([4,2]), Set([2,5])] in AOS
            False
            sage: [Set([1,2]), Set()] in AOS
            False
        """
    class Element(OrderedSetPartition): ...

class SplitNK(OrderedSetPartitions_scomp): ...
