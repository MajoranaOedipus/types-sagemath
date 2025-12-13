from _typeshed import Incomplete
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.combinat.integer_vector import IntegerVectors as IntegerVectors
from sage.combinat.words.abstract_word import Word_class as Word_class
from sage.rings.integer import Integer as Integer
from sage.structure.parent import Parent as Parent

class ShuffleProduct_abstract(Parent):
    """
    Abstract base class for shuffle products.
    """
    def __init__(self, l1, l2, element_constructor=None) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: from sage.combinat.shuffle import ShuffleProduct
            sage: SP = ShuffleProduct([1,2],[4,5,7,8,9])
            sage: TestSuite(SP).run(skip='_test_an_element')
        """
    def __eq__(self, other):
        """
        Test for equality.

        TESTS::

            sage: from sage.combinat.shuffle import ShuffleProduct
            sage: SP = ShuffleProduct([1,2],[4,5,7,8,9])
            sage: loads(dumps(SP)) == SP
            True
            sage: SP == ShuffleProduct([1,2],[4,5,7])
            False
        """
    def __ne__(self, other):
        """
        Test for unequality.

        EXAMPLES::

            sage: from sage.combinat.shuffle import ShuffleProduct_overlapping_r
            sage: w, u = map(Words(range(20)), [[2, 9], [9, 1]])
            sage: A = ShuffleProduct_overlapping_r(w,u,1)
            sage: B = ShuffleProduct_overlapping_r(u,w,2)
            sage: A != A
            False
            sage: A != B
            True
        """
    def __contains__(self, x) -> bool:
        """
        Check containment.

        TESTS::

            sage: from sage.combinat.shuffle import ShuffleProduct
            sage: SP = ShuffleProduct([1,2],[4,5,7])
            sage: [1,4,5,2,7] in SP
            True
            sage: (1,4,5,2,7) in SP
            False
            sage: [2,1,4,5,7] in SP
            False
        """

class SetShuffleProduct(ShuffleProduct_abstract):
    """
    The union of all possible shuffle products of two sets of iterables.

    EXAMPLES::

        sage: from sage.combinat.shuffle import SetShuffleProduct
        sage: sorted(SetShuffleProduct({(1,), (2,3)}, {(4,5), (6,)}))
        [[1, 4, 5],
         [1, 6],
         [2, 3, 4, 5],
         [2, 3, 6],
         [2, 4, 3, 5],
         [2, 4, 5, 3],
         [2, 6, 3],
         [4, 1, 5],
         [4, 2, 3, 5],
         [4, 2, 5, 3],
         [4, 5, 1],
         [4, 5, 2, 3],
         [6, 1],
         [6, 2, 3]]
    """
    def __init__(self, l1, l2, element_constructor=None) -> None:
        """
        Construct the set of all possible shuffle products of two sets of iterables.

        INPUT:

        - ``l1``, ``l2`` -- iterable: the sets to shuffle

        - ``element_constructor`` -- constructor for the returned elements

        TESTS::

            sage: from sage.combinat.shuffle import SetShuffleProduct
            sage: X = SetShuffleProduct({(1,2,3), (2,3,4)}, {(5,)})
            sage: X   # random
            Shuffle set product of: [(2, 3, 4), (1, 2, 3)] and [(5,)]
            sage: TestSuite(X).run(skip='_test_an_element')

            sage: list(SetShuffleProduct({(1,2,3), (2,3,4)}, {(5,)}))   # random
            [[2, 3, 4, 5], [2, 5, 3, 4], [5, 2, 3, 4], [2, 3, 5, 4],
             [1, 2, 3, 5], [1, 5, 2, 3], [5, 1, 2, 3], [1, 2, 5, 3]]
        """
    def __iter__(self):
        """
        TESTS::

            sage: from sage.combinat.shuffle import SetShuffleProduct
            sage: list(SetShuffleProduct([[],[]], [[]]))
            [[], []]
            sage: list(SetShuffleProduct([[1,2],[3]], [[4]]))
            [[1, 2, 4], [4, 1, 2], [1, 4, 2], [3, 4], [4, 3]]
            sage: list(SetShuffleProduct([[1,2],[3,4]], [[1,4]], element_constructor=set))
            [{1, 2, 4},
             {1, 2, 4},
             {1, 2, 4},
             {1, 2, 4},
             {1, 2, 4},
             {1, 2, 4},
             {1, 3, 4},
             {1, 3, 4},
             {1, 3, 4},
             {1, 3, 4},
             {1, 3, 4},
             {1, 3, 4}]
        """
    def cardinality(self):
        """
        The cardinality is defined by the sum of the cardinality of all shuffles.
        That means by a sum of binomials.

        TESTS::

            sage: from sage.combinat.shuffle import SetShuffleProduct
            sage: SetShuffleProduct([[1,2],[3,4]], [[1,4]], element_constructor=set).cardinality()
            12
        """

class ShuffleProduct(ShuffleProduct_abstract):
    '''
    Shuffle product of two iterables.

    EXAMPLES::

        sage: from sage.combinat.shuffle import ShuffleProduct
        sage: list(ShuffleProduct("abc", "de", element_constructor="".join))
        [\'abcde\',
         \'adbce\',
         \'dabce\',
         \'abdce\',
         \'adebc\',
         \'daebc\',
         \'deabc\',
         \'adbec\',
         \'dabec\',
         \'abdec\']
        sage: list(ShuffleProduct("", "de", element_constructor="".join))
        [\'de\']
    '''
    def __init__(self, l1, l2, element_constructor=None) -> None:
        '''
        Construct the shuffle product of two iterable.

        INPUT:

        - ``l1``, ``l2`` -- iterable: iterables to shuffle

        - ``element_constructor`` -- constructor for the returned elements

        TESTS::

            sage: from sage.combinat.shuffle import ShuffleProduct
            sage: SP = ShuffleProduct([1,2,3],[4,5])
            sage: SP
            Shuffle product of: [1, 2, 3] and [4, 5]
            sage: TestSuite(SP).run(skip=\'_test_an_element\')

            sage: list(ShuffleProduct(Word("aa"), Word("bbb"), Word))
            [word: aabbb, word: baabb, word: ababb, word: bbaab, word: babab, word: abbab,
             word: bbbaa, word: bbaba, word: babba, word: abbba]
        '''
    def __iter__(self):
        """
        Efficient iteration from a gray code on binary words in `B(n,k)`.

        (with `B(n,k)` the number of binary words of size `n` with `k` one.

        TESTS::

            sage: from sage.combinat.shuffle import ShuffleProduct
            sage: list(ShuffleProduct([1,2,3],[4,5]))
            [[1, 2, 3, 4, 5], [1, 4, 2, 3, 5], [4, 1, 2, 3, 5], [1, 2, 4, 3, 5], [1, 4, 5, 2, 3],
             [4, 1, 5, 2, 3], [4, 5, 1, 2, 3], [1, 4, 2, 5, 3], [4, 1, 2, 5, 3], [1, 2, 4, 5, 3]]
            sage: B = BinaryTree                                                        # needs sage.graphs
            sage: ascii_art(list(ShuffleProduct([B([]), B([[],[]])],                    # needs sage.graphs
            ....:   [B([[[],[]],[[],None]])])))
            [ [ o,   o  ,     __o__   ]  [     __o__  , o,   o   ]
            [ [     / \\      /     \\  ]  [    /     \\       / \\  ]
            [ [    o   o    o       o ]  [   o       o     o   o ]
            [ [            / \\     /  ]  [  / \\     /            ]
            [ [           o   o   o   ], [ o   o   o             ],
            <BLANKLINE>
             [ o,     __o__  ,   o   ] ]
             [       /     \\    / \\  ] ]
             [      o       o  o   o ] ]
             [     / \\     /         ] ]
             [    o   o   o          ] ]
        """
    def __contains__(self, iterable) -> bool:
        """
        TESTS::

            sage: from sage.combinat.shuffle import ShuffleProduct
            sage: sh = ShuffleProduct([1,2,3],[4,5])
            sage: list(range(1,6)) in sh
            True
            sage: list(range(1,7)) in sh
            False
            sage: [3,4,5,1,2] in sh
            False
            sage: [1,4,2,5,3] in sh
            True
            sage: [1,4,2,2,5,3] in sh
            False
        """
    def cardinality(self):
        """
        Return the number of shuffles of `l_1` and `l_2`, respectively of
        lengths `m` and `n`, which is `\\binom{m+n}{n}`.

        TESTS::

            sage: from sage.combinat.shuffle import ShuffleProduct
            sage: ShuffleProduct([3,1,2], [4,2,1,3]).cardinality()
            35
            sage: ShuffleProduct([3,1,2,5,6,4], [4,2,1,3]).cardinality() == binomial(10,4)
            True
        """

class ShuffleProduct_overlapping_r(ShuffleProduct_abstract):
    """
    The overlapping shuffle product of the two words ``w1`` and ``w2``
    with precisely ``r`` overlaps.

    See :class:`ShuffleProduct_overlapping` for a definition.

    EXAMPLES::

        sage: from sage.combinat.shuffle import ShuffleProduct_overlapping_r
        sage: w, u = map(Words(range(20)), [[2, 9], [9, 1]])
        sage: S = ShuffleProduct_overlapping_r(w,u,1)
        sage: list(S)
        [word: 11,9,1,
         word: 2,18,1,
         word: 11,1,9,
         word: 2,9,10,
         word: 939,
         word: 9,2,10]
    """
    r: Incomplete
    add: Incomplete
    def __init__(self, w1, w2, r, element_constructor=None, add=...) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: from sage.combinat.shuffle import ShuffleProduct_overlapping_r
            sage: w, u = map(Words(range(20)), [[2, 9], [9, 1]])
            sage: S = ShuffleProduct_overlapping_r(w,u,1)
            sage: TestSuite(S).run(skip='_test_an_element')
        """
    def __eq__(self, other):
        """
        Check equality.

        EXAMPLES::

            sage: from sage.combinat.shuffle import ShuffleProduct_overlapping_r
            sage: w, u = map(Words(range(20)), [[2, 9], [9, 1]])
            sage: A = ShuffleProduct_overlapping_r(w,u,1)
            sage: B = ShuffleProduct_overlapping_r(u,w,2)
            sage: A == A
            True
            sage: A == B
            False
        """
    def __iter__(self):
        """
        EXAMPLES::

            sage: from sage.combinat.shuffle import ShuffleProduct_overlapping_r
            sage: w, u = Word([1,2]), Word([3,4])
            sage: ShuffleProduct_overlapping_r(w,u,1).list()
            [word: 424, word: 154, word: 442, word: 136, word: 352, word: 316]
            sage: w, u = map(Words(range(1,7)), [[1,2], [3,4]])
            sage: W = Words(range(1,7))
            sage: w, u = W([1,2]), W([3,4])
            sage: ShuffleProduct_overlapping_r(w, u, 1).list() #indirect doctest
            [word: 424, word: 154, word: 442, word: 136, word: 352, word: 316]

            sage: I, J = Composition([2, 2]), Composition([1, 1])
            sage: S = ShuffleProduct_overlapping_r(I, J, 1)
            sage: S.list()
            [[3, 2, 1], [2, 3, 1], [3, 1, 2], [2, 1, 3], [1, 3, 2], [1, 2, 3]]

        TESTS:

        We need to be explicitly more generic about the resulting parent
        when shuffling two compositions `I` and `J` (:issue:`15131`)::

            sage: I, J = Compositions(4)([2, 2]), Composition([1, 1])
            sage: S = ShuffleProduct_overlapping_r(I, J, 1, Compositions())
            sage: S.list()
            [[3, 2, 1], [2, 3, 1], [3, 1, 2], [2, 1, 3], [1, 3, 2], [1, 2, 3]]
        """

class ShuffleProduct_overlapping(ShuffleProduct_abstract):
    """
    The overlapping shuffle product of the two words ``w1`` and
    ``w2``.

    If `u` and `v` are two words whose letters belong to an
    additive monoid or to another kind of alphabet on which addition
    is well-defined, then the *overlapping shuffle product* of
    `u` and `v` is a certain multiset of words defined as follows:
    Let `a` and `b` be the lengths of `u` and `v`, respectively.
    Let `A` be the set `\\{(0, 1), (0, 2), \\cdots, (0, a)\\}`, and
    let `B` be the set `\\{(1, 1), (1, 2), \\cdots, (1, b)\\}`.
    Notice that the sets `A` and `B` are disjoint. We can make
    `A` and `B` into posets by setting `(k, i) \\leq (k, j)` for
    all `k \\in \\{0, 1\\}` and `i \\leq j`. Then, `A \\cup B` becomes
    a poset by disjoint union (we don't set `(0, i) \\leq (1, i)`).
    Let `p` be the map from `A \\cup B` to the set of all letters
    which sends every `(0, i)` to the `i`-th letter of `u`, and
    every `(1, j)` to the `j`-th letter of `v`. For every
    nonnegative integer `c` and every surjective map
    `f : A \\cup B \\to \\{ 1, 2, \\cdots, c \\}` for which both
    restrictions `f \\mid_A` and `f \\mid_B` are strictly increasing,
    let `w(f)` be the length-`c` word such that for every
    `1 \\leq k \\leq c`, the `k`-th letter of `w(f)` equals
    `\\sum_{j \\in f^{-1}(k)} p(j)` (this sum always has either
    one or two addends). The overlapping shuffle product of `u`
    and `v` is then the multiset of all `w(f)` with `c` ranging
    over all nonnegative integers and `f` ranging
    over the surjective maps
    `f : A \\cup B \\to \\{ 1, 2, \\cdots, c \\}` for which both
    restrictions `f \\mid_A` and `f \\mid_B` are strictly increasing.

    If one restricts `c` to a particular fixed nonnegative
    integer, then the multiset is instead called the *overlapping
    shuffle product with precisely `a + b - c` overlaps*. This is
    nonempty only if `\\max \\{a, b\\} \\leq c \\leq a + b`.

    If `c = a + b`, then the overlapping shuffle product with
    precisely `a + b - c` overlaps is plainly the shuffle product
    (:class:`ShuffleProduct_w1w2`).

    INPUT:

    - ``w1``, ``w2`` -- iterables
    - ``element_constructor`` -- (default: the parent of ``w1``)
      the function used to construct the output
    - ``add`` -- (default: ``+``) the addition function

    EXAMPLES::

        sage: from sage.combinat.shuffle import ShuffleProduct_overlapping
        sage: w, u = [[2, 9], [9, 1]]
        sage: S = ShuffleProduct_overlapping(w, u)
        sage: sorted(S)
        [[2, 9, 1, 9],
         [2, 9, 9, 1],
         [2, 9, 9, 1],
         [2, 9, 10],
         [2, 18, 1],
         [9, 1, 2, 9],
         [9, 2, 1, 9],
         [9, 2, 9, 1],
         [9, 2, 10],
         [9, 3, 9],
         [11, 1, 9],
         [11, 9, 1],
         [11, 10]]
        sage: A = [{1,2}, {3,4}]
        sage: B = [{2,3}, {4,5,6}]
        sage: S = ShuffleProduct_overlapping(A, B, add=lambda X,Y: X.union(Y))
        sage: list(S)
        [[{1, 2}, {3, 4}, {2, 3}, {4, 5, 6}],
         [{1, 2}, {2, 3}, {3, 4}, {4, 5, 6}],
         [{1, 2}, {2, 3}, {4, 5, 6}, {3, 4}],
         [{2, 3}, {1, 2}, {3, 4}, {4, 5, 6}],
         [{2, 3}, {1, 2}, {4, 5, 6}, {3, 4}],
         [{2, 3}, {4, 5, 6}, {1, 2}, {3, 4}],
         [{1, 2, 3}, {3, 4}, {4, 5, 6}],
         [{1, 2}, {2, 3, 4}, {4, 5, 6}],
         [{1, 2, 3}, {4, 5, 6}, {3, 4}],
         [{1, 2}, {2, 3}, {3, 4, 5, 6}],
         [{2, 3}, {1, 2, 4, 5, 6}, {3, 4}],
         [{2, 3}, {1, 2}, {3, 4, 5, 6}],
         [{1, 2, 3}, {3, 4, 5, 6}]]
    """
    def __init__(self, w1, w2, element_constructor=None, add=...) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: from sage.combinat.shuffle import ShuffleProduct_overlapping
            sage: w, u = map(Words(range(20)), [[2, 9], [9, 1]])
            sage: S = ShuffleProduct_overlapping(w,u)
            sage: TestSuite(S).run(skip='_test_an_element')
        """
    def __iter__(self):
        """
        EXAMPLES::

            sage: from sage.combinat.shuffle import ShuffleProduct_overlapping
            sage: w, u = map(Words(range(10)), [[0,1],[2,3]])
            sage: S = ShuffleProduct_overlapping(w,u)
            sage: S.list()
            [word: 0123, word: 0213, word: 0231, word: 2013, word: 2031,
             word: 2301, word: 213, word: 033, word: 231, word: 024,
             word: 231, word: 204, word: 24]

            sage: w, u = map(Words(range(1,10)), [[1,2],[3,4]])
            sage: S = ShuffleProduct_overlapping(w,u)
            sage: S.list()
            [word: 1234, word: 1324, word: 1342, word: 3124, word: 3142,
             word: 3412, word: 424, word: 154, word: 442, word: 136,
             word: 352, word: 316, word: 46]
        """
