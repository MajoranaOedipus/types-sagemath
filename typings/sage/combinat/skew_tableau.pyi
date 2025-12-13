from _typeshed import Incomplete
from sage.arith.misc import factorial as factorial
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.categories.infinite_enumerated_sets import InfiniteEnumeratedSets as InfiniteEnumeratedSets
from sage.categories.sets_cat import Sets as Sets
from sage.combinat.integer_vector import IntegerVectors as IntegerVectors
from sage.combinat.partition import Partition as Partition
from sage.combinat.skew_partition import SkewPartition as SkewPartition, SkewPartitions as SkewPartitions
from sage.combinat.tableau import SemistandardTableau as SemistandardTableau, StandardTableau as StandardTableau, Tableau as Tableau, Tableaux as Tableaux
from sage.combinat.words.words import Words as Words
from sage.misc.inherit_comparison import InheritComparisonClasscallMetaclass as InheritComparisonClasscallMetaclass
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.rings.infinity import PlusInfinity as PlusInfinity
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.structure.list_clone import ClonableList as ClonableList
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class SkewTableau(ClonableList, metaclass=InheritComparisonClasscallMetaclass):
    """
    A skew tableau.

    Note that Sage by default uses the English convention for partitions and
    tableaux. To change this, see :meth:`Tableaux.options`.

    EXAMPLES::

         sage: st = SkewTableau([[None, 1],[2,3]]); st
         [[None, 1], [2, 3]]
         sage: st.inner_shape()
         [1]
         sage: st.outer_shape()
         [2, 2]

    The ``expr`` form of a skew tableau consists of the inner partition
    followed by a list of the entries in each row from bottom to top::

        sage: SkewTableau(expr=[[1,1],[[5],[3,4],[1,2]]])
        [[None, 1, 2], [None, 3, 4], [5]]

    The ``chain`` form of a skew tableau consists of a list of
    partitions `\\lambda_1,\\lambda_2,\\ldots,`, such that all cells in
    `\\lambda_{i+1}` that are not in `\\lambda_i` have entry `i`::

        sage: SkewTableau(chain=[[2], [2, 1], [3, 1], [4, 3, 2, 1]])
        [[None, None, 2, 3], [1, 3, 3], [3, 3], [3]]
    """
    @staticmethod
    def __classcall_private__(cls, st=None, expr=None, chain=None):
        """
        Return the skew tableau object corresponding to ``st``.

        EXAMPLES::

            sage: SkewTableau([[None,1],[2,3]])
            [[None, 1], [2, 3]]
            sage: SkewTableau(expr=[[1,1],[[5],[3,4],[1,2]]])
            [[None, 1, 2], [None, 3, 4], [5]]
        """
    def __init__(self, parent, st) -> None:
        """
        TESTS::

            sage: st = SkewTableau([[None, 1],[2,3]])
            sage: st = SkewTableau([[None,1,1],[None,2],[4]])
            sage: TestSuite(st).run()

        A skew tableau is immutable, see :issue:`15862`::

            sage: T = SkewTableau([[None,2],[2]])
            sage: t0 = T[0]
            sage: t0[1] = 3
            Traceback (most recent call last):
            ...
            TypeError: 'tuple' object does not support item assignment
            sage: T[0][1] = 5
            Traceback (most recent call last):
            ...
            TypeError: 'tuple' object does not support item assignment
        """
    def __eq__(self, other):
        """
        Check whether ``self`` is equal to ``other``.

        .. TODO::

            This overwrites the equality check of
            :class:`~sage.structure.list_clone.ClonableList`
            in order to circumvent the coercion framework.
            Eventually this should be solved more elegantly,
            for example along the lines of what was done for
            `k`-tableaux.

            For now, two elements are equal if their underlying
            defining lists compare equal.

        INPUT:

        - ``other`` -- the element that ``self`` is compared to

        OUTPUT: boolean

        TESTS::

            sage: t = SkewTableau([[None,1,2]])
            sage: t == 0
            False
            sage: t == SkewTableaux()([[None,1,2]])
            True
            sage: t == [(None,1,2)]
            True
            sage: t == [[None,1,2]]
            True

            sage: s = SkewTableau([[1,2]])
            sage: s == 0
            False
            sage: s == Tableau([[1,2]])
            True
        """
    def __ne__(self, other):
        """
        Check whether ``self`` is unequal to ``other``.

        See the documentation of :meth:`__eq__`.

        INPUT:

        - ``other`` -- the element that ``self`` is compared to

        OUTPUT: boolean

        TESTS::

            sage: t = SkewTableau([[None,1,2]])
            sage: t != []
            True
        """
    def __hash__(self):
        """
        Return the hash of ``self``.

        EXAMPLES:

        Check that :issue:`35137` is fixed::

            sage: t = SkewTableau([[None,1,2]])
            sage: hash(t) == hash(tuple(t))
            True
        """
    def check(self) -> None:
        """
        Check that ``self`` is a valid skew tableau. This is currently far too
        liberal, and only checks some trivial things.

        EXAMPLES::

            sage: t = SkewTableau([[None,1,1],[2]])
            sage: t.check()

            sage: t = SkewTableau([[None, None, 1], [2, 4], [], [3, 4, 5]])
            Traceback (most recent call last):
            ...
            TypeError: a skew tableau cannot have an empty list for a row

            sage: s = SkewTableau([[1, None, None],[2, None],[3]])
            Traceback (most recent call last):
            ...
            TypeError: not a valid skew tableau
        """
    def pp(self) -> None:
        """
        Return a pretty print string of the tableau.

        EXAMPLES::

            sage: SkewTableau([[None,2,3],[None,4],[5]]).pp()
              .  2  3
              .  4
              5
        """
    def outer_shape(self):
        """
        Return the outer shape of ``self``.

        EXAMPLES::

            sage: SkewTableau([[None,1,2],[None,3],[4]]).outer_shape()
            [3, 2, 1]
        """
    def inner_shape(self):
        """
        Return the inner shape of ``self``.

        EXAMPLES::

            sage: SkewTableau([[None,1,2],[None,3],[4]]).inner_shape()
            [1, 1]
            sage: SkewTableau([[1,2],[3,4],[7]]).inner_shape()
            []
            sage: SkewTableau([[None,None,None,2,3],[None,1],[None],[2]]).inner_shape()
            [3, 1, 1]
        """
    def shape(self):
        """
        Return the shape of ``self``.

        EXAMPLES::

            sage: SkewTableau([[None,1,2],[None,3],[4]]).shape()
            [3, 2, 1] / [1, 1]
        """
    def outer_size(self):
        """
        Return the size of the outer shape of ``self``.

        EXAMPLES::

            sage: SkewTableau([[None, 2, 4], [None, 3], [1]]).outer_size()
            6
            sage: SkewTableau([[None, 2], [1, 3]]).outer_size()
            4
        """
    def inner_size(self):
        """
        Return the size of the inner shape of ``self``.

        EXAMPLES::

            sage: SkewTableau([[None, 2, 4], [None, 3], [1]]).inner_size()
            2
            sage: SkewTableau([[None, 2], [1, 3]]).inner_size()
            1
        """
    def size(self):
        """
        Return the number of cells in ``self``.

        EXAMPLES::

            sage: SkewTableau([[None, 2, 4], [None, 3], [1]]).size()
            4
            sage: SkewTableau([[None, 2], [1, 3]]).size()
            3
        """
    def conjugate(self):
        """
        Return the conjugate of ``self``.

        EXAMPLES::

            sage: SkewTableau([[None,1],[2,3]]).conjugate()
            [[None, 2], [1, 3]]
        """
    def to_word_by_row(self):
        """
        Return a word obtained from a row reading of ``self``.

        This is the word obtained by concatenating the rows from
        the bottommost one (in English notation) to the topmost one.

        EXAMPLES::

            sage: s = SkewTableau([[None,1],[2,3]])
            sage: s.pp()
              .  1
              2  3
            sage: s.to_word_by_row()
            word: 231
            sage: s = SkewTableau([[None, 2, 4], [None, 3], [1]])
            sage: s.pp()
              .  2  4
              .  3
              1
            sage: s.to_word_by_row()
            word: 1324

        TESTS::

            sage: SkewTableau([[None, None, None], [None]]).to_word_by_row()
            word:
            sage: SkewTableau([]).to_word_by_row()
            word:
        """
    def to_word_by_column(self):
        """
        Return the word obtained from a column reading of the skew
        tableau.

        This is the word obtained by concatenating the columns from
        the rightmost one (in English notation) to the leftmost one.

        EXAMPLES::

            sage: s = SkewTableau([[None,1],[2,3]])
            sage: s.pp()
              .  1
              2  3
            sage: s.to_word_by_column()
            word: 132

        ::

            sage: s = SkewTableau([[None, 2, 4], [None, 3], [1]])
            sage: s.pp()
            .  2  4
            .  3
            1
            sage: s.to_word_by_column()
            word: 4231
        """
    to_word = to_word_by_row
    def to_permutation(self):
        """
        Return a permutation with the entries of ``self`` obtained by reading
        ``self`` row by row, from the bottommost to the topmost row, with
        each row being read from left to right, in English convention.
        See :meth:`to_word_by_row()`.

        EXAMPLES::

            sage: SkewTableau([[None,2],[3,4],[None],[1]]).to_permutation()
            [1, 3, 4, 2]
            sage: SkewTableau([[None,2],[None,4],[1],[3]]).to_permutation()
            [3, 1, 4, 2]
            sage: SkewTableau([[None]]).to_permutation()
            []
        """
    def weight(self):
        """
        Return the weight (aka evaluation) of the tableau ``self``.
        Trailing zeroes are omitted when returning the weight.

        The weight of a skew tableau `T` is the sequence
        `(a_1, a_2, a_3, \\ldots )`, where `a_k` is the number of
        entries of `T` equal to `k`. This sequence contains only
        finitely many nonzero entries.

        The weight of a skew tableau `T` is the same as the weight
        of the reading word of `T`, for any reading order.

        :meth:`evaluation` is a synonym for this method.

        EXAMPLES::

            sage: SkewTableau([[1,2],[3,4]]).weight()
            [1, 1, 1, 1]

            sage: SkewTableau([[None,2],[None,4],[None,5],[None]]).weight()
            [0, 1, 0, 1, 1]

            sage: SkewTableau([]).weight()
            []

            sage: SkewTableau([[None,None,None],[None]]).weight()
            []

            sage: SkewTableau([[None,3,4],[None,6,7],[4,8],[5,13],[6],[7]]).weight()
            [0, 0, 1, 2, 1, 2, 2, 1, 0, 0, 0, 0, 1]

        TESTS:

        We check that this agrees with going to the word::

            sage: t = SkewTableau([[None,None,4,7,15],[6,2,16],[2,3,19],[4,5],[7]])
            sage: def by_word(T):
            ....:     ed = T.to_word().evaluation_dict()
            ....:     m = max(ed) + 1
            ....:     return [ed.get(k, 0) for k in range(1, m)]
            sage: by_word(t) == t.weight()
            True
            sage: SST = SemistandardTableaux(shape=[3,1,1])
            sage: all(by_word(t) == SkewTableau(t).weight() for t in SST)               # needs sage.modules
            True
        """
    evaluation = weight
    def is_standard(self) -> bool:
        """
        Return ``True`` if ``self`` is a standard skew tableau and ``False``
        otherwise.

        EXAMPLES::

            sage: SkewTableau([[None, 2], [1, 3]]).is_standard()
            True
            sage: SkewTableau([[None, 2], [2, 4]]).is_standard()
            False
            sage: SkewTableau([[None, 3], [2, 4]]).is_standard()
            False
            sage: SkewTableau([[None, 2], [2, 4]]).is_standard()
            False
        """
    def is_semistandard(self) -> bool:
        """
        Return ``True`` if ``self`` is a semistandard skew tableau and
        ``False`` otherwise.

        EXAMPLES::

            sage: SkewTableau([[None, 2, 2], [1, 3]]).is_semistandard()
            True
            sage: SkewTableau([[None, 2], [2, 4]]).is_semistandard()
            True
            sage: SkewTableau([[None, 3], [2, 4]]).is_semistandard()
            True
            sage: SkewTableau([[None, 2], [1, 2]]).is_semistandard()
            False
            sage: SkewTableau([[None, 2, 3]]).is_semistandard()
            True
            sage: SkewTableau([[None, 3, 2]]).is_semistandard()
            False
            sage: SkewTableau([[None, 2, 3], [1, 4]]).is_semistandard()
            True
            sage: SkewTableau([[None, 2, 3], [1, 2]]).is_semistandard()
            False
            sage: SkewTableau([[None, 2, 3], [None, None, 4]]).is_semistandard()
            False
        """
    def to_tableau(self):
        """
        Return a tableau with the same filling. This only works if the
        inner shape of the skew tableau has size zero.

        EXAMPLES::

            sage: SkewTableau([[1,2],[3,4]]).to_tableau()
            [[1, 2], [3, 4]]
        """
    def restrict(self, n):
        """
        Return the restriction of the (semi)standard skew tableau to all
        the numbers less than or equal to ``n``.

        .. NOTE::

            If only the outer shape of the restriction, rather than
            the whole restriction, is needed, then the faster method
            :meth:`restriction_outer_shape` is preferred. Similarly if
            only the skew shape is needed, use :meth:`restriction_shape`.

        EXAMPLES::

            sage: SkewTableau([[None,1],[2],[3]]).restrict(2)
            [[None, 1], [2]]
            sage: SkewTableau([[None,1],[2],[3]]).restrict(1)
            [[None, 1]]
            sage: SkewTableau([[None,1],[1],[2]]).restrict(1)
            [[None, 1], [1]]
        """
    def restriction_outer_shape(self, n):
        """
        Return the outer shape of the restriction of the semistandard skew
        tableau ``self`` to `n`.

        If `T` is a semistandard skew tableau and `n` is a nonnegative
        integer, then the restriction of `T` to `n` is defined as the
        (semistandard) skew tableau obtained by removing all cells filled
        with entries greater than `n` from `T`.

        This method computes merely the outer shape of the restriction.
        For the restriction itself, use :meth:`restrict`.

        EXAMPLES::

            sage: SkewTableau([[None,None],[2,3],[3,4]]).restriction_outer_shape(3)
            [2, 2, 1]
            sage: SkewTableau([[None,2],[None],[4],[5]]).restriction_outer_shape(2)
            [2, 1]
            sage: T = SkewTableau([[None,None,3,5],[None,4,4],[17]])
            sage: T.restriction_outer_shape(0)
            [2, 1]
            sage: T.restriction_outer_shape(2)
            [2, 1]
            sage: T.restriction_outer_shape(3)
            [3, 1]
            sage: T.restriction_outer_shape(4)
            [3, 3]
            sage: T.restriction_outer_shape(19)
            [4, 3, 1]
        """
    def restriction_shape(self, n):
        """
        Return the skew shape of the restriction of the semistandard
        skew tableau ``self`` to ``n``.

        If `T` is a semistandard skew tableau and `n` is a nonnegative
        integer, then the restriction of `T` to `n` is defined as the
        (semistandard) skew tableau obtained by removing all cells filled
        with entries greater than `n` from `T`.

        This method computes merely the skew shape of the restriction.
        For the restriction itself, use :meth:`restrict`.

        EXAMPLES::

            sage: SkewTableau([[None,None],[2,3],[3,4]]).restriction_shape(3)
            [2, 2, 1] / [2]
            sage: SkewTableau([[None,2],[None],[4],[5]]).restriction_shape(2)
            [2, 1] / [1, 1]
            sage: T = SkewTableau([[None,None,3,5],[None,4,4],[17]])
            sage: T.restriction_shape(0)
            [2, 1] / [2, 1]
            sage: T.restriction_shape(2)
            [2, 1] / [2, 1]
            sage: T.restriction_shape(3)
            [3, 1] / [2, 1]
            sage: T.restriction_shape(4)
            [3, 3] / [2, 1]
        """
    def to_chain(self, max_entry=None):
        """
        Return the chain of partitions corresponding to the (semi)standard
        skew tableau ``self``.

        The optional keyword parameter ``max_entry`` can be used to
        customize the length of the chain. Specifically, if this parameter
        is set to a nonnegative integer ``n``, then the chain is
        constructed from the positions of the letters `1, 2, \\ldots, n`
        in the tableau.

        EXAMPLES::

            sage: SkewTableau([[None,1],[2],[3]]).to_chain()
            [[1], [2], [2, 1], [2, 1, 1]]
            sage: SkewTableau([[None,1],[1],[2]]).to_chain()
            [[1], [2, 1], [2, 1, 1]]
            sage: SkewTableau([[None,1],[1],[2]]).to_chain(max_entry=2)
            [[1], [2, 1], [2, 1, 1]]
            sage: SkewTableau([[None,1],[1],[2]]).to_chain(max_entry=3)
            [[1], [2, 1], [2, 1, 1], [2, 1, 1]]
            sage: SkewTableau([[None,1],[1],[2]]).to_chain(max_entry=1)
            [[1], [2, 1]]
            sage: SkewTableau([[None,None,2],[None,3],[None,5]]).to_chain(max_entry=6)
            [[2, 1, 1], [2, 1, 1], [3, 1, 1], [3, 2, 1], [3, 2, 1], [3, 2, 2], [3, 2, 2]]
            sage: SkewTableau([]).to_chain()
            [[]]
            sage: SkewTableau([]).to_chain(max_entry=1)
            [[], []]

        TESTS:

        Check that :meth:`to_chain()` does not skip letters::

            sage: t = SkewTableau([[None, 2, 3], [3]])
            sage: t.to_chain()
            [[1], [1], [2], [3, 1]]

            sage: T = SkewTableau([[None]])
            sage: T.to_chain()
            [[1]]
        """
    def slide(self, corner=None, return_vacated: bool = False):
        """
        Apply a jeu de taquin slide to ``self`` on the specified inner
        corner and return the resulting tableau.

        If no corner is given, the topmost inner corner is chosen.

        The optional parameter ``return_vacated=True`` causes
        the output to be the pair ``(t, (i, j))`` where ``t`` is the new
        tableau and ``(i, j)`` are the coordinates of the vacated square.

        See [Ful1997]_ p12-13.

        EXAMPLES::

            sage: st = SkewTableau([[None, None, None, None, 2], [None, None, None, None, 6], [None, 2, 4, 4], [2, 3, 6], [5, 5]])
            sage: st.slide((2, 0))
            [[None, None, None, None, 2], [None, None, None, None, 6], [2, 2, 4, 4], [3, 5, 6], [5]]
            sage: st2 = SkewTableau([[None, None, 3], [None, 2, 4], [1, 5]])
            sage: st2.slide((1, 0), True)
            ([[None, None, 3], [1, 2, 4], [5]], (2, 1))

        TESTS::

            sage: st
            [[None, None, None, None, 2], [None, None, None, None, 6],
             [None, 2, 4, 4], [2, 3, 6], [5, 5]]
        """
    def backward_slide(self, corner=None):
        '''
        Apply a backward jeu de taquin slide on the specified outside
        ``corner`` of ``self``.

        Backward jeu de taquin slides are defined in Section 3.7 of
        [Sag2001]_.

        .. WARNING::

            The :meth:`inner_corners` and :meth:`outer_corners` are the
            :meth:`sage.combinat.partition.Partition.corners` of the inner and
            outer partitions of the skew shape. They are different from the
            inner/outer corners defined in [Sag2001]_.

            The "inner corners" of [Sag2001]_ may be found by calling
            :meth:`outer_corners`. The "outer corners" of [Sag2001]_ may be
            found by calling ``self.outer_shape().outside_corners()``.

        EXAMPLES::

            sage: T = SkewTableaux()([[2, 2], [4, 4], [5]])
            sage: Tableaux.options.display=\'array\'
            sage: Q = T.backward_slide(); Q
            . 2 2
            4 4
            5
            sage: Q.backward_slide((1, 2))
            . 2 2
            . 4 4
            5
            sage: Q.reverse_slide((1, 2)) == Q.backward_slide((1, 2))
            True

            sage: T = SkewTableaux()([[1, 3],[3],[5]]); T
            1 3
            3
            5
            sage: T.reverse_slide((1,1))
            . 1
            3 3
            5

        TESTS::

            sage: T = SkewTableaux()([[2, 2], [4, 4], [5]])
            sage: Q = T.backward_slide((0, 2))
            sage: Q.backward_slide((2,1))
            . 2 2
            . 4
            4 5
            sage: Q.backward_slide((3,0))
            . 2 2
            . 4
            4
            5
            sage: Q = T.backward_slide((2,1)); Q
            . 2
            2 4
            4 5
            sage: Q.backward_slide((3,0))
            . 2
            . 4
            2 5
            4
            sage: Q = T.backward_slide((3,0)); Q
            . 2
            2 4
            4
            5
            sage: Q.backward_slide((4,0))
            . 2
            . 4
            2
            4
            5
            sage: Tableaux.options.display=\'list\'
        '''
    reverse_slide = backward_slide
    def rectify(self, algorithm=None):
        """
        Return a :class:`StandardTableau`, :class:`SemistandardTableau`,
        or just :class:`Tableau` formed by applying the jeu de taquin
        process to ``self``.

        See page 15 of [Ful1997]_.

        INPUT:

        - ``algorithm`` -- (optional) if set to ``'jdt'``, rectifies by jeu de
          taquin; if set to ``'schensted'``, rectifies by Schensted insertion
          of the reading word. Otherwise, guesses which will be faster.

        EXAMPLES::

            sage: S = SkewTableau([[None,1],[2,3]])
            sage: S.rectify()
            [[1, 3], [2]]
            sage: T = SkewTableau([[None, None, None, 4],[None,None,1,6],[None,None,5],[2,3]])
            sage: T.rectify()
            [[1, 3, 4, 6], [2, 5]]
            sage: T.rectify(algorithm='jdt')
            [[1, 3, 4, 6], [2, 5]]
            sage: T.rectify(algorithm='schensted')
            [[1, 3, 4, 6], [2, 5]]
            sage: T.rectify(algorithm='spaghetti')
            Traceback (most recent call last):
            ...
            ValueError: algorithm must be 'jdt', 'schensted', or None

        TESTS::

            sage: S
            [[None, 1], [2, 3]]
            sage: T
            [[None, None, None, 4], [None, None, 1, 6], [None, None, 5], [2, 3]]
        """
    def add_entry(self, cell, m):
        """
        Return the result of setting the entry in cell ``cell`` equal to ``m`` in the skew tableau ``self``.
        If the cell is already part of ``self``, it replaces the current entry.
        Otherwise, it attempts to add the cell to the skew tableau.

        INPUT:

        - ``cell`` -- a pair of nonnegative integers
        - ``m`` -- a nonnegative integer

        OUTPUT:

        The skew tableau ``self`` with entry in cell ``cell`` set to ``m``.
        This overwrites an existing entry if ``cell`` already belongs to ``self``,
        otherwise it adds the cell to the shape.

        .. NOTE::

            Both coordinates of ``cell`` are interpreted as starting at `0`.
            So, ``cell == (0, 0)`` corresponds to the northwesternmost cell

        EXAMPLES::

            sage: S = SkewTableau([[None, None,1],[1,2,5]]); S.pp()
            .  .  1
            1  2  5
            sage: T = S.add_entry([0,1],1); T.pp()
            .  1  1
            1  2  5
            sage: U = T.add_entry([2,0],3); U.pp()
            .  1  1
            1  2  5
            3
            sage: U.add_entry([1,3],4)
            Traceback (most recent call last):
            ...
            IndexError: (1, 3) is not an addable cell of the tableau
            sage: U.add_entry([0,3],4).pp()
            .  1  1  4
            1  2  5
            3

        TESTS::

            sage: S = SkewTableau([[None, None, 1]])
            sage: S.add_entry([0,0],1)
            Traceback (most recent call last):
            ...
            TypeError: not a valid skew tableau
            sage: S.add_entry([0,1],1)
            [[None, 1, 1]]
            sage: S.add_entry([1,0],1)
            [[None, None, 1], [1]]
            sage: S.add_entry([1,1],1)
            [[None, None, 1], [None, 1]]
            sage: S.add_entry([1,2],1)
            [[None, None, 1], [None, None, 1]]
            sage: S.add_entry([2,0],1)
            [[None, None, 1], [None], [1]]
            sage: S.add_entry([2,1],1)
            [[None, None, 1], [None, None], [None, 1]]
            sage: S.add_entry([2,2],1)
            Traceback (most recent call last):
            ...
            IndexError: (2, 2) is not an addable cell of the tableau
            sage: S.add_entry([2,3],1)
            Traceback (most recent call last):
            ...
            IndexError: (2, 3) is not an addable cell of the tableau
            sage: S.add_entry([1000,1000], 3)
            Traceback (most recent call last):
            ...
            IndexError: (1000, 1000) is not an addable cell of the tableau
            sage: S.add_entry([0,1000],3)
            Traceback (most recent call last):
            ...
            IndexError: (0, 1000) is not an addable cell of the tableau

        """
    def anti_restrict(self, n):
        """
        Return the skew tableau formed by removing all of the cells from
        ``self`` that are filled with a number at most ``n``.

        INPUT:

        - ``n`` -- a nonnegative integer

        OUTPUT:

        The skew tableau ``self`` with all entries less than or equal to ``n`` removed.

        EXAMPLES::

            sage: S = SkewTableau([[None,1,2,3],[4,5,6]])
            sage: S.anti_restrict(2)
            [[None, None, None, 3], [4, 5, 6]]
            sage: S.anti_restrict(1).anti_restrict(2) == S.anti_restrict(2)
            True
        """
    def to_list(self):
        """
        Return a (mutable) list representation of ``self``.

        EXAMPLES::

            sage: stlist = [[None, None, 3], [None, 1, 3], [2, 2]]
            sage: st = SkewTableau(stlist)
            sage: st.to_list()
            [[None, None, 3], [None, 1, 3], [2, 2]]
            sage: st.to_list() == stlist
            True
        """
    def row_stabilizer(self):
        """
        Return the :func:`PermutationGroup` corresponding to the row stabilizer of
        ``self``.

        This assumes that every integer from `1` to the size of ``self``
        appears exactly once in ``self``.

        EXAMPLES::

            sage: # needs sage.groups
            sage: rs = SkewTableau([[None,1,2,3],[4,5]]).row_stabilizer()
            sage: rs.order() == factorial(3) * factorial(2)
            True
            sage: PermutationGroupElement([(1,3,2),(4,5)]) in rs
            True
            sage: PermutationGroupElement([(1,4)]) in rs
            False
            sage: rs = SkewTableau([[None,1,2],[3]]).row_stabilizer()
            sage: PermutationGroupElement([(1,2),(3,)]) in rs
            True
            sage: rs.one().domain()
            [1, 2, 3]
            sage: rs = SkewTableau([[None,None,1],[None,2],[3]]).row_stabilizer()
            sage: rs.order()
            1
            sage: rs = SkewTableau([[None,None,2,4,5],[1,3]]).row_stabilizer()
            sage: rs.order()
            12
            sage: rs = SkewTableau([]).row_stabilizer()
            sage: rs.order()
            1
        """
    def column_stabilizer(self):
        """
        Return the :func:`PermutationGroup` corresponding to the column stabilizer
        of ``self``.

        This assumes that every integer from `1` to the size of ``self``
        appears exactly once in ``self``.

        EXAMPLES::

            sage: # needs sage.groups
            sage: cs = SkewTableau([[None,2,3],[1,5],[4]]).column_stabilizer()
            sage: cs.order() == factorial(2) * factorial(2)
            True
            sage: PermutationGroupElement([(1,3,2),(4,5)]) in cs
            False
            sage: PermutationGroupElement([(1,4)]) in cs
            True
        """
    def shuffle(self, t2):
        """
        Shuffle the standard tableaux ``self`` and ``t2``.

        Let ``t1 = self``. The shape of ``t2`` must extend the shape of
        ``t1``, that is, ``self.outer_shape() == t2.inner_shape()``. Then
        this function computes the pair of tableaux ``(t2_new, t1_new)``
        obtained by using jeu de taquin slides to move the boxes of ``t2``
        behind the boxes of ``self``.

        The entries of ``t2_new`` are obtained by performing successive
        inwards jeu de taquin slides on ``t2`` in the order indicated by
        the entries of ``t1``, from largest to smallest. The entries of
        ``t1`` then slide outwards one by one and land in the squares
        vacated successively by ``t2``, forming ``t1_new``.

        .. NOTE::

            Equivalently, the entries of ``t1_new`` are obtained by performing
            outer jeu de taquin slides on ``t1`` in the order indicated by the
            entries of ``t2``, from smallest to largest. In this case the
            entries of ``t2`` slide backwards and fill the squares
            successively vacated by ``t1`` and so form ``t2_new``.
            (This is not how the algorithm is implemented.)

        INPUT:

        - ``self``, ``t2`` -- a pair of standard SkewTableaux with
          ``self.outer_shape() == t2.inner_shape()``

        OUTPUT:

        - ``t2_new, t1_new`` -- a pair of standard :class:`SkewTableaux`
          with ``t2_new.outer_shape() == t1_new.inner_shape()``

        EXAMPLES::

            sage: t1 = SkewTableau([[None, 1, 2], [3, 4]])
            sage: t2 = SkewTableau([[None, None, None, 3], [None, None, 4], [1, 2, 5]])
            sage: (t2_new, t1_new) = t1.shuffle(t2)
            sage: t1_new
            [[None, None, None, 2], [None, None, 1], [None, 3, 4]]
            sage: t2_new
            [[None, 2, 3], [1, 4], [5]]
            sage: t1_new.outer_shape() == t2.outer_shape()
            True
            sage: t2_new.inner_shape() == t1.inner_shape()
            True

        Shuffling is an involution::

            sage: t1 = SkewTableau([[None, 1, 2], [3, 4]])
            sage: t2 = SkewTableau([[None, None, None, 3], [None, None, 4], [1, 2, 5]])
            sage: sh = lambda x,y : x.shuffle(y)
            sage: (t1, t2) == sh(*sh(t1, t2))
            True

        Both tableaux must be standard::

            sage: t1 = SkewTableau([[None, 1, 2], [2, 4]])
            sage: t2 = SkewTableau([[None, None, None, 3], [None, None, 4], [1, 2, 5]])
            sage: t1.shuffle(t2)
            Traceback (most recent call last):
            ...
            ValueError: the tableaux must be standard
            sage: t1 = SkewTableau([[None, 1, 2], [3, 4]])
            sage: t2 = SkewTableau([[None, None, None, 3], [None, None, 4], [1, 2, 6]])
            sage: t1.shuffle(t2)
            Traceback (most recent call last):
            ...
            ValueError: the tableaux must be standard

        The shapes (not just the nonempty cells) must be adjacent::

            sage: t1 = SkewTableau([[None, None, None], [1]])
            sage: t2 = SkewTableau([[None], [None], [1]])
            sage: t1.shuffle(t2)
            Traceback (most recent call last):
            ...
            ValueError: the shapes must be adjacent

        TESTS:

        A corner case, where one tableau has no cells::

            sage: t1 = SkewTableau([[None]])
            sage: t2 = SkewTableau([[None, 1, 2], [3, 4]])
            sage: (t2_new, t1_new) = t1.shuffle(t2)
            sage: t1_new
            [[None, None, None], [None, None]]
            sage: t2_new == t2
            True
            sage: t2_new.shuffle(t1_new) == (t1, t2)
            True
        """
    def standardization(self, check: bool = True):
        """
        Return the standardization of ``self``, assuming ``self`` is a
        semistandard skew tableau.

        The standardization of a semistandard skew tableau `T` is the standard
        skew tableau `\\mathrm{st}(T)` of the same shape as `T` whose
        reversed reading word is the standardization of the reversed reading
        word of `T`.

        The standardization of a word `w` can be formed by replacing all `1`'s
        in `w` by `1, 2, \\ldots, k_1` from left to right, all `2`'s in `w` by
        `k_1 + 1, k_1 + 2, \\ldots, k_2`, and repeating for all letters that
        appear in `w`.
        See also :meth:`Word.standard_permutation()`.

        INPUT:

        - ``check`` -- (default: ``True``) check to make sure ``self`` is
          semistandard; set to ``False`` to avoid this check

        EXAMPLES::

            sage: t = SkewTableau([[None,None,3,4,7,19],[None,4,4,8],[None,5,16,17],[None],[2],[3]])
            sage: t.standardization()
            [[None, None, 3, 6, 8, 12], [None, 4, 5, 9], [None, 7, 10, 11], [None], [1], [2]]

        Standard skew tableaux are fixed under standardization::

            sage: p = Partition([4,3,3,2])
            sage: q = Partitions(3).random_element()                                    # needs sage.libs.flint
            sage: all(t == t.standardization()                                          # needs sage.libs.flint
            ....:     for t in StandardSkewTableaux([p, q]))
            True

        The reading word of the standardization is the
        standardization of the reading word::

            sage: t = SkewTableau([[None,3,4,4],[None,6,10],[7,7,11],[18]])
            sage: t.to_word().standard_permutation() == t.standardization().to_permutation()
            True

        TESTS:

        Some corner cases::

            sage: t = SkewTableau([[None,None],[None]])
            sage: t.standardization()
            [[None, None], [None]]
            sage: t = SkewTableau([])
            sage: t.standardization()
            []
        """
    def bender_knuth_involution(self, k, rows=None, check: bool = True):
        """
        Return the image of ``self`` under the `k`-th Bender--Knuth
        involution, assuming ``self`` is a skew semistandard tableau.

        Let `T` be a tableau, then a *lower free `k` in `T`* means a cell of
        `T` which is filled with the integer `k` and whose direct lower
        neighbor is not filled with the integer `k + 1` (in particular,
        this lower neighbor might not exist at all). Let an *upper free `k + 1`
        in `T`* mean a cell of `T` which is filled with the integer `k + 1`
        and whose direct upper neighbor is not filled with the integer `k`
        (in particular, this neighbor might not exist at all). It is clear
        that for any row `r` of `T`, the lower free `k`'s and the upper
        free `k + 1`'s in `r` together form a contiguous interval or `r`.

        The *`k`-th Bender--Knuth switch at row `i`* changes the entries of
        the cells in this interval in such a way that if it used to have
        `a` entries of `k` and `b` entries of `k + 1`, it will now
        have `b` entries of `k` and `a` entries of `k + 1`. For fixed `k`, the
        `k`-th Bender--Knuth switches for different `i` commute. The
        composition of the `k`-th Bender--Knuth switches for all rows is
        called the *`k`-th Bender--Knuth involution*. This is used to show that
        the Schur functions defined by semistandard (skew) tableaux are
        symmetric functions.

        INPUT:

        - ``k`` -- integer

        - ``rows`` -- (default: ``None``) when set to ``None``, the method
          computes the `k`-th Bender--Knuth involution as defined above.
          When an iterable, this computes the composition of the `k`-th
          Bender--Knuth switches at row `i` over all `i` in ``rows``. When set
          to an integer `i`, the method computes the `k`-th Bender--Knuth
          switch at row `i`. Note the indexing of the rows starts with `1`.

        - ``check`` -- (default: ``True``) check to make sure ``self`` is
          semistandard; set to ``False`` to avoid this check

        OUTPUT:

        The image of ``self`` under either the `k`-th Bender--Knuth
        involution, the `k`-th Bender--Knuth switch at a certain row, or
        the composition of such switches, as detailed in the INPUT section.

        EXAMPLES::

            sage: t = SkewTableau([[None,None,None,4,4,5,6,7],[None,2,4,6,7,7,7],
            ....:                  [None,4,5,8,8,9],[None,6,7,10],[None,8,8,11],[None],[4]])
            sage: t
            [[None, None, None, 4, 4, 5, 6, 7], [None, 2, 4, 6, 7, 7, 7],
             [None, 4, 5, 8, 8, 9], [None, 6, 7, 10], [None, 8, 8, 11], [None], [4]]
            sage: t.bender_knuth_involution(1)
            [[None, None, None, 4, 4, 5, 6, 7], [None, 1, 4, 6, 7, 7, 7],
             [None, 4, 5, 8, 8, 9], [None, 6, 7, 10], [None, 8, 8, 11], [None], [4]]
            sage: t.bender_knuth_involution(4)
            [[None, None, None, 4, 5, 5, 6, 7], [None, 2, 4, 6, 7, 7, 7],
             [None, 5, 5, 8, 8, 9], [None, 6, 7, 10], [None, 8, 8, 11], [None], [5]]
            sage: t.bender_knuth_involution(5)
            [[None, None, None, 4, 4, 5, 6, 7], [None, 2, 4, 5, 7, 7, 7],
             [None, 4, 6, 8, 8, 9], [None, 5, 7, 10], [None, 8, 8, 11], [None], [4]]
            sage: t.bender_knuth_involution(6)
            [[None, None, None, 4, 4, 5, 6, 6], [None, 2, 4, 6, 6, 7, 7],
             [None, 4, 5, 8, 8, 9], [None, 6, 7, 10], [None, 8, 8, 11], [None], [4]]
            sage: t.bender_knuth_involution(666) == t
            True
            sage: t.bender_knuth_involution(4, 2) == t
            True
            sage: t.bender_knuth_involution(4, 3)
            [[None, None, None, 4, 4, 5, 6, 7], [None, 2, 4, 6, 7, 7, 7],
             [None, 5, 5, 8, 8, 9], [None, 6, 7, 10], [None, 8, 8, 11], [None], [4]]

        The Bender--Knuth involution is an involution::

            sage: t = SkewTableau([[None,3,4,4],[None,6,10],[7,7,11],[18]])
            sage: all(t.bender_knuth_involution(k).bender_knuth_involution(k)
            ....:     == t for k in range(1,4))
            True

        The same for the single switches::

            sage: all(t.bender_knuth_involution(k, j).bender_knuth_involution(k, j)
            ....:     == t for k in range(1,5) for j in range(1, 5))
            True

        Locality of the Bender--Knuth involutions::

            sage: all(t.bender_knuth_involution(k).bender_knuth_involution(l)
            ....:     == t.bender_knuth_involution(l).bender_knuth_involution(k)
            ....:     for k in range(1,5) for l in range(1,5) if abs(k - l) > 1)
            True

        TESTS::

            sage: t = SkewTableau([])
            sage: t.bender_knuth_involution(3)
            []
            sage: t = SkewTableau([[None,None],[None]])
            sage: t.bender_knuth_involution(3)
            [[None, None], [None]]

        The `(s_1 s_2)^6 = id` identity that holds for Bender--Knuth
        involutions on straight shapes does not generally hold for
        skew shapes::

            sage: p = lambda t, k: t.bender_knuth_involution(k).bender_knuth_involution(k + 1)
            sage: t = SkewTableau([[None,1,2],[2,3]])
            sage: x = t
            sage: for i in range(6): x = p(x, 1)
            sage: x
            [[None, 2, 2], [1, 3]]
            sage: x == t
            False

        AUTHORS:

        - Darij Grinberg (2013-05-14)
        """
    def to_expr(self):
        """
        The first list in a result corresponds to the inner partition of
        the skew shape. The second list is a list of the rows in the skew
        tableau read from the bottom up.

        Provided for compatibility with MuPAD-Combinat. In MuPAD-Combinat,
        if ``t`` is a skew tableau, then to_expr gives the same result as
        ``expr(t)`` would give in MuPAD-Combinat.

        EXAMPLES::

            sage: SkewTableau([[None,1,1,3],[None,2,2],[1]]).to_expr()
            [[1, 1], [[1], [2, 2], [1, 1, 3]]]
            sage: SkewTableau([]).to_expr()
            [[], []]
        """
    def is_ribbon(self) -> bool:
        """
        Return ``True`` if and only if the shape of ``self`` is a
        ribbon.

        This means that it has exactly one cell in each of `q`
        consecutive diagonals for some nonnegative integer `q`.

        EXAMPLES::

            sage: S = SkewTableau([[None, None, 1, 2],[None, None, 3],[1, 3, 4]])
            sage: S.pp()
              .  .  1  2
              .  .  3
              1  3  4
            sage: S.is_ribbon()
            True

            sage: S = SkewTableau([[None, 1, 1, 2],[None, 2, 3],[1, 3, 4]])
            sage: S.pp()
              .  1  1  2
              .  2  3
              1  3  4
            sage: S.is_ribbon()
            False

            sage: S = SkewTableau([[None, None, 1, 2],[None, None, 3],[1]])
            sage: S.pp()
              .  .  1  2
              .  .  3
              1
            sage: S.is_ribbon()
            False

            sage: S = SkewTableau([[None, None, None, None],[None, None, 3],[1, 2, 4]])
            sage: S.pp()
              .  .  .  .
              .  .  3
              1  2  4
            sage: S.is_ribbon()
            True

            sage: S = SkewTableau([[None, None, None, None],[None, None, 3],[None, 2, 4]])
            sage: S.pp()
              .  .  .  .
              .  .  3
              .  2  4
            sage: S.is_ribbon()
            True

            sage: S = SkewTableau([[None, None],[None]])
            sage: S.pp()
              .  .
              .
            sage: S.is_ribbon()
            True
        """
    def to_ribbon(self, check_input: bool = True):
        """
        Return ``self`` as a ribbon-shaped tableau
        (:class:`~sage.combinat.ribbon_shaped_tableau.RibbonShapedTableau`),
        provided that the shape of ``self`` is a ribbon.

        INPUT:

        - ``check_input`` -- boolean (default: ``True``); whether or not to
          check that ``self`` indeed has ribbon shape

        EXAMPLES::

            sage: SkewTableau([[None,1],[2,3]]).to_ribbon()
            [[None, 1], [2, 3]]
        """
    def filling(self):
        """
        Return a list of the non-empty entries in ``self``.

        EXAMPLES::

            sage: t = SkewTableau([[None,1],[2,3]])
            sage: t.filling()
            [[1], [2, 3]]
        """
    def cells_by_content(self, c):
        """
        Return the coordinates of the cells in ``self`` with content ``c``.

        EXAMPLES::

            sage: s = SkewTableau([[None,1,2],[3,4,5],[6]])
            sage: s.cells_by_content(0)
            [(1, 1)]
            sage: s.cells_by_content(1)
            [(0, 1), (1, 2)]
            sage: s.cells_by_content(2)
            [(0, 2)]
            sage: s.cells_by_content(-1)
            [(1, 0)]
            sage: s.cells_by_content(-2)
            [(2, 0)]
        """
    def entries_by_content(self, c):
        """
        Return the entries in ``self`` with content ``c``.

        EXAMPLES::

            sage: s = SkewTableau([[None,1,2],[3,4,5],[6]])
            sage: s.entries_by_content(0)
            [4]
            sage: s.entries_by_content(1)
            [1, 5]
            sage: s.entries_by_content(2)
            [2]
            sage: s.entries_by_content(-1)
            [3]
            sage: s.entries_by_content(-2)
            [6]
        """
    def cells(self):
        """
        Return the cells in ``self``.

        EXAMPLES::

            sage: s = SkewTableau([[None,1,2],[3],[6]])
            sage: s.cells()
            [(0, 1), (0, 2), (1, 0), (2, 0)]
        """
    def cells_containing(self, i):
        """
        Return the list of cells in which the letter ``i`` appears in the
        tableau ``self``. The list is ordered with cells appearing from
        left to right.

        Cells are given as pairs of coordinates `(a, b)`, where both
        rows and columns are counted from `0` (so `a = 0` means the cell
        lies in the leftmost column of the tableau, etc.).

        EXAMPLES::

            sage: t = SkewTableau([[None,None,3],[None,3,5],[4,5]])
            sage: t.cells_containing(5)
            [(2, 1), (1, 2)]
            sage: t.cells_containing(4)
            [(2, 0)]
            sage: t.cells_containing(2)
            []

            sage: t = SkewTableau([[None,None,None,None],[None,4,5],[None,5,6],[None,9],[None]])
            sage: t.cells_containing(2)
            []
            sage: t.cells_containing(4)
            [(1, 1)]
            sage: t.cells_containing(5)
            [(2, 1), (1, 2)]

            sage: SkewTableau([]).cells_containing(3)
            []

            sage: SkewTableau([[None,None],[None]]).cells_containing(3)
            []
        """
    def is_k_tableau(self, k) -> bool:
        """
        Check whether ``self`` is a valid skew weak `k`-tableau.

        EXAMPLES::

            sage: t = SkewTableau([[None,2,3],[2,3],[3]])
            sage: t.is_k_tableau(3)
            True
            sage: t = SkewTableau([[None,1,3],[2,2],[3]])
            sage: t.is_k_tableau(3)
            False
        """

class SkewTableaux(UniqueRepresentation, Parent):
    """
    Class of all skew tableaux.
    """
    def __init__(self, category=None) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: S = SkewTableaux()
            sage: TestSuite(S).run()
        """
    Element = SkewTableau
    options = Tableaux.options
    def __contains__(self, x) -> bool:
        """
        Check if ``x`` is a skew tableau.

        EXAMPLES::

            sage: T = SkewTableau([[None, None, 1], [3], [4]])
            sage: T in SkewTableaux()
            True
            sage: [[None,1],[2,3]] in SkewTableaux()
            True
        """
    def from_expr(self, expr):
        """
        Return a :class:`SkewTableau` from a MuPAD-Combinat expr for
        a skew tableau.

        The first list in ``expr`` is the inner shape of the skew
        tableau. The second list are the entries in the rows of the skew
        tableau from bottom to top.

        Provided primarily for compatibility with MuPAD-Combinat.

        EXAMPLES::

            sage: SkewTableaux().from_expr([[1,1],[[5],[3,4],[1,2]]])
            [[None, 1, 2], [None, 3, 4], [5]]
        """
    def from_chain(self, chain):
        """
        Return the tableau corresponding to the chain of partitions.

        EXAMPLES::

            sage: SkewTableaux().from_chain([[1,1],[2,1],[3,1],[3,2],[3,3],[3,3,1]])
            [[None, 1, 2], [None, 3, 4], [5]]
        """
    def from_shape_and_word(self, shape, word):
        """
        Return the skew tableau corresponding to the skew partition ``shape``
        and the word ``word`` obtained from the row reading.

        EXAMPLES::

            sage: t = SkewTableau([[None, 1, 3], [None, 2], [4]])
            sage: shape = t.shape()
            sage: word  = t.to_word()
            sage: SkewTableaux().from_shape_and_word(shape, word)
            [[None, 1, 3], [None, 2], [4]]
        """

class StandardSkewTableaux(SkewTableaux):
    """
    Standard skew tableaux.

    EXAMPLES::

        sage: S = StandardSkewTableaux(); S
        Standard skew tableaux
        sage: S.cardinality()
        +Infinity

    ::

        sage: S = StandardSkewTableaux(2); S
        Standard skew tableaux of size 2
        sage: S.cardinality()                                                           # needs sage.modules
        4

    ::

        sage: # needs sage.graphs sage.modules
        sage: StandardSkewTableaux([[3, 2, 1], [1, 1]]).list()
        [[[None, 2, 3], [None, 4], [1]],
         [[None, 1, 2], [None, 3], [4]],
         [[None, 1, 2], [None, 4], [3]],
         [[None, 1, 3], [None, 4], [2]],
         [[None, 1, 4], [None, 3], [2]],
         [[None, 1, 4], [None, 2], [3]],
         [[None, 1, 3], [None, 2], [4]],
         [[None, 2, 4], [None, 3], [1]]]
    """
    @staticmethod
    def __classcall_private__(cls, skp=None):
        """
        Return the class of standard skew tableaux of skew shape ``skp``.

        EXAMPLES::

            sage: SST1 = StandardSkewTableaux([[3, 2, 1], [1, 1]])
            sage: SST2 = StandardSkewTableaux(SkewPartition([[3, 2, 1], [1, 1]]))
            sage: SST1 is SST2
            True
        """
    def __contains__(self, x) -> bool:
        """
        EXAMPLES::

            sage: [[None, 2], [1, 3]] in StandardSkewTableaux()
            True
            sage: [[None, 2], [2, 4]] in StandardSkewTableaux()
            False
            sage: [[None, 3], [2, 4]] in StandardSkewTableaux()
            False
            sage: [[None, 2], [1, 4]] in StandardSkewTableaux()
            False
        """

class StandardSkewTableaux_all(StandardSkewTableaux):
    """
    Class of all standard skew tableaux.
    """
    def __init__(self) -> None:
        """
        EXAMPLES::

            sage: s = StandardSkewTableaux()
            sage: TestSuite(s).run()                                                    # needs sage.graphs
        """
    def __iter__(self):
        """
        Iterate through all standard skew tableaux having
        no empty rows (before nonempty rows) and no empty columns
        (before nonempty columns).

        EXAMPLES::

            sage: # needs sage.graphs sage.modules
            sage: it = StandardSkewTableaux().__iter__()
            sage: [next(it) for x in range(10)]
            [[],
             [[1]],
             [[1, 2]], [[1], [2]], [[None, 2], [1]], [[None, 1], [2]],
             [[1, 2, 3]], [[1, 2], [3]], [[1, 3], [2]], [[None, 2, 3], [1]]]
        """

class StandardSkewTableaux_size(StandardSkewTableaux):
    """
    Standard skew tableaux of a fixed size `n`.
    """
    n: Incomplete
    def __init__(self, n) -> None:
        """
        EXAMPLES::

            sage: # needs sage.graphs sage.modules
            sage: S = StandardSkewTableaux(3)
            sage: TestSuite(S).run()
        """
    def cardinality(self):
        """
        EXAMPLES::

            sage: # needs sage.modules
            sage: StandardSkewTableaux(1).cardinality()
            1
            sage: StandardSkewTableaux(2).cardinality()
            4
            sage: StandardSkewTableaux(3).cardinality()
            24
            sage: StandardSkewTableaux(4).cardinality()
            194
        """
    def __iter__(self):
        """
        Iterate through all standard skew tableaux of size `n` having
        no empty rows (before nonempty rows) and no empty columns
        (before nonempty columns). (The last two requirements
        ensure that the iterator terminates after finitely many steps.)

        EXAMPLES::

            sage: # needs sage.graphs sage.modules
            sage: StandardSkewTableaux(2).list()
            [[[1, 2]], [[1], [2]], [[None, 2], [1]], [[None, 1], [2]]]
            sage: StandardSkewTableaux(3).list()
            [[[1, 2, 3]],
             [[1, 2], [3]], [[1, 3], [2]],
             [[None, 2, 3], [1]], [[None, 1, 2], [3]], [[None, 1, 3], [2]],
             [[None, 2], [1, 3]], [[None, 1], [2, 3]],
             [[None, None, 2], [1, 3]], [[None, None, 3], [1, 2]],
             [[None, None, 1], [2, 3]],
             [[1], [2], [3]], [[None, 2], [None, 3], [1]],
             [[None, 1], [None, 2], [3]], [[None, 1], [None, 3], [2]],
             [[None, 2], [1], [3]], [[None, 3], [1], [2]],
             [[None, 1], [2], [3]], [[None, None, 3], [None, 2], [1]],
             [[None, None, 2], [None, 3], [1]],
             [[None, None, 1], [None, 3], [2]],
             [[None, None, 1], [None, 2], [3]],
             [[None, None, 2], [None, 1], [3]],
             [[None, None, 3], [None, 1], [2]]]
        """

class StandardSkewTableaux_shape(StandardSkewTableaux):
    """
    Standard skew tableaux of a fixed skew shape `\\lambda / \\mu`.
    """
    @staticmethod
    def __classcall_private__(cls, skp):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: S = StandardSkewTableaux([[3, 2, 1], [1, 1]])
            sage: S2 = StandardSkewTableaux(SkewPartition([[3, 2, 1], [1, 1]]))
            sage: S is S2
            True
        """
    skp: Incomplete
    def __init__(self, skp) -> None:
        """
        TESTS::

            sage: # needs sage.graphs sage.modules
            sage: S = StandardSkewTableaux([[3, 2, 1], [1, 1]])
            sage: TestSuite(S).run()
        """
    def cardinality(self):
        """
        Return the number of standard skew tableaux with shape of the skew
        partition ``skp``. This uses a formula due to Aitken
        (see Cor. 7.16.3 of [Sta-EC2]_).

        EXAMPLES::

            sage: StandardSkewTableaux([[3, 2, 1], [1, 1]]).cardinality()               # needs sage.modules
            8
        """
    def __iter__(self):
        """
        An iterator for all the standard skew tableaux whose shape is
        the skew partition ``skp``. The standard skew tableaux are
        ordered lexicographically by the word obtained from their row
        reading.

        EXAMPLES::

            sage: # needs sage.graphs sage.modules
            sage: StandardSkewTableaux([[3, 2, 1], [1, 1]]).list()
            [[[None, 2, 3], [None, 4], [1]],
             [[None, 1, 2], [None, 3], [4]],
             [[None, 1, 2], [None, 4], [3]],
             [[None, 1, 3], [None, 4], [2]],
             [[None, 1, 4], [None, 3], [2]],
             [[None, 1, 4], [None, 2], [3]],
             [[None, 1, 3], [None, 2], [4]],
             [[None, 2, 4], [None, 3], [1]]]
        """

class SemistandardSkewTableaux(SkewTableaux):
    '''
    Semistandard skew tableaux.

    This class can be initialized with several optional variables:
    the size of the skew tableaux (as a nameless integer variable),
    their shape (as a nameless skew partition variable), their
    weight (:meth:`~sage.combinat.skew_tableau.SkewTableau.weight`,
    as a nameless second variable after either the size or the
    shape) and their maximum entry (as an optional keyword variable
    called ``max_entry``, unless the weight has been specified). If
    neither the weight nor the maximum entry is specified, the
    maximum entry defaults to the size of the tableau.

    Note that "maximum entry" does not literally mean the highest
    entry; instead it is just an upper bound that no entry is
    allowed to surpass.

    EXAMPLES:

    The (infinite) class of all semistandard skew tableaux::

        sage: SemistandardSkewTableaux()
        Semistandard skew tableaux

    The (still infinite) class of all semistandard skew tableaux
    with maximum entry `2`::

        sage: SemistandardSkewTableaux(max_entry=2)
        Semistandard skew tableaux with maximum entry 2

    The class of all semistandard skew tableaux of given size `3`
    and maximum entry `3`::

        sage: SemistandardSkewTableaux(3)
        Semistandard skew tableaux of size 3 and maximum entry 3

    To set a different maximum entry::

        sage: SemistandardSkewTableaux(3, max_entry = 7)
        Semistandard skew tableaux of size 3 and maximum entry 7

    Specifying a shape::

        sage: SemistandardSkewTableaux([[2,1],[]])
        Semistandard skew tableaux of shape [2, 1] / [] and maximum entry 3

    Specifying both a shape and a maximum entry::

        sage: S = SemistandardSkewTableaux([[2,1],[1]], max_entry = 3); S
        Semistandard skew tableaux of shape [2, 1] / [1] and maximum entry 3
        sage: S.list()
        [[[None, 1], [1]],
         [[None, 2], [1]],
         [[None, 1], [2]],
         [[None, 3], [1]],
         [[None, 1], [3]],
         [[None, 2], [2]],
         [[None, 3], [2]],
         [[None, 2], [3]],
         [[None, 3], [3]]]

        sage: for n in range(5):
        ....:     print("{} {}".format(n, len(SemistandardSkewTableaux([[2,2,1],[1]], max_entry = n))))
        0 0
        1 0
        2 1
        3 9
        4 35

    Specifying a shape and a weight::

        sage: SemistandardSkewTableaux([[2,1],[]],[2,1])
        Semistandard skew tableaux of shape [2, 1] / [] and weight [2, 1]

    (the maximum entry is redundant in this case and thus is ignored).

    Specifying a size and a weight::

        sage: SemistandardSkewTableaux(3, [2,1])
        Semistandard skew tableaux of size 3 and weight [2, 1]

    .. WARNING::

        If the shape is not specified, the iterator of this class
        yields only skew tableaux whose shape is reduced, in the
        sense that there are no empty rows before the last nonempty
        row, and there are no empty columns before the last
        nonempty column. (Otherwise it would go on indefinitely.)

    .. WARNING::

        This class acts as a factory. The resulting classes are mainly
        useful for iteration. Do not rely on their containment tests,
        as they are not correct, e. g.::

            sage: SkewTableau([[None]]) in SemistandardSkewTableaux(2)
            True
    '''
    @staticmethod
    def __classcall_private__(cls, p=None, mu=None, max_entry=None):
        """
        Return the correct parent based upon the input.

        EXAMPLES::

            sage: SSST1 = SemistandardSkewTableaux([[3, 2, 1], [1, 1]])
            sage: SSST2 = SemistandardSkewTableaux(SkewPartition([[3, 2, 1], [1, 1]]))
            sage: SSST1 is SSST2
            True
        """
    def __contains__(self, x) -> bool:
        """
        EXAMPLES::

            sage: [[None, 2], [1, 3]] in SemistandardSkewTableaux()
            True
            sage: [[None, 2], [2, 4]] in SemistandardSkewTableaux()
            True
            sage: [[None, 3], [2, 4]] in SemistandardSkewTableaux()
            True
            sage: [[None, 2], [2, 4]] in SemistandardSkewTableaux()
            True
        """

class SemistandardSkewTableaux_all(SemistandardSkewTableaux):
    """
    Class of all semistandard skew tableaux, possibly with a given
    maximum entry.
    """
    max_entry: Incomplete
    def __init__(self, max_entry) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: S = SemistandardSkewTableaux()
            sage: TestSuite(S).run()

            sage: S = SemistandardSkewTableaux(3)
            sage: TestSuite(S).run()
        """
    def __iter__(self):
        """
        Iterate over the elements of ``self``.

        EXAMPLES::

            sage: it = SemistandardSkewTableaux(max_entry = 5).__iter__()
            sage: [next(it) for x in range(12)]
            [[],
             [[1]],
             [[2]],
             [[3]],
             [[4]],
             [[5]],
             [[1, 1]],
             [[1, 2]],
             [[1, 3]],
             [[1, 4]],
             [[1, 5]],
             [[2, 2]]]

        If no max entry is specified, the iteration goes over all
        semistandard skew tableaux of size `n` with max entry `n`,
        for all `n`::

            sage: it = SemistandardSkewTableaux().__iter__()
            sage: [next(it) for x in range(10)]
            [[],
             [[1]],
             [[1, 1]],
             [[1, 2]],
             [[2, 2]],
             [[1], [2]],
             [[None, 1], [1]],
             [[None, 2], [1]],
             [[None, 1], [2]],
             [[None, 2], [2]]]
        """

class SemistandardSkewTableaux_size(SemistandardSkewTableaux):
    """
    Class of all semistandard skew tableaux of a fixed size `n`,
    possibly with a given maximum entry.
    """
    n: Incomplete
    max_entry: Incomplete
    def __init__(self, n, max_entry) -> None:
        """
        EXAMPLES::

            sage: S = SemistandardSkewTableaux(3)
            sage: TestSuite(S).run()
        """
    def cardinality(self):
        """
        EXAMPLES::

            sage: SemistandardSkewTableaux(2).cardinality()
            8
        """
    def __iter__(self):
        """
        EXAMPLES::

            sage: SemistandardSkewTableaux(2).list()
            [[[1, 1]],
             [[1, 2]],
             [[2, 2]],
             [[1], [2]],
             [[None, 1], [1]],
             [[None, 2], [1]],
             [[None, 1], [2]],
             [[None, 2], [2]]]
        """

class SemistandardSkewTableaux_size_weight(SemistandardSkewTableaux):
    """
    Class of semistandard tableaux of a fixed size `n` and weight `\\mu`.
    """
    @staticmethod
    def __classcall_private__(cls, n, mu):
        """
        Normalize our input to ensure we have a unique representation.

        EXAMPLES::

            sage: S = SemistandardSkewTableaux(3, [2,1])
            sage: S2 = SemistandardSkewTableaux(int(3), (2,1))
            sage: S is S2
            True
        """
    n: Incomplete
    mu: Incomplete
    def __init__(self, n, mu) -> None:
        """
        EXAMPLES::

            sage: S = SemistandardSkewTableaux(3,[2,1])
            sage: TestSuite(S).run()
        """
    def cardinality(self):
        """
        EXAMPLES::

            sage: SemistandardSkewTableaux(2,[1,1]).cardinality()
            4
        """
    def __iter__(self):
        """
        EXAMPLES::

            sage: SemistandardSkewTableaux(2,[1,1]).list()
            [[[1, 2]], [[1], [2]], [[None, 2], [1]], [[None, 1], [2]]]
        """

class SemistandardSkewTableaux_shape(SemistandardSkewTableaux):
    """
    Class of semistandard skew tableaux of a fixed skew shape
    `\\lambda / \\mu` with a given max entry.

    A semistandard skew tableau with max entry `i` is required to have all
    its entries less or equal to `i`. It is not required to actually
    contain an entry `i`.

    INPUT:

    - ``p`` -- a skew partition

    - ``max_entry`` -- the max entry; defaults to the size of ``p``

    .. WARNING::

        Input is not checked; please use :class:`SemistandardSkewTableaux` to
        ensure the options are properly parsed.
    """
    @staticmethod
    def __classcall_private__(cls, p, max_entry=None):
        """
        Normalize our input to ensure we have a unique representation.

        EXAMPLES::

            sage: S = SemistandardSkewTableaux([[2,1],[]])
            sage: S2 = SemistandardSkewTableaux(SkewPartition([[2,1],[]]))
            sage: S is S2
            True
        """
    p: Incomplete
    max_entry: Incomplete
    def __init__(self, p, max_entry) -> None:
        """
        EXAMPLES::

            sage: S = SemistandardSkewTableaux([[2,1],[]])
            sage: S == loads(dumps(S))
            True
            sage: TestSuite(S).run()
        """
    def cardinality(self):
        """
        EXAMPLES::

            sage: SemistandardSkewTableaux([[2,1],[]]).cardinality()
            8
            sage: SemistandardSkewTableaux([[2,1],[]], max_entry=2).cardinality()
            2
        """
    def __iter__(self):
        """
        EXAMPLES::

            sage: SemistandardSkewTableaux([[2,1],[]]).list()
            [[[1, 1], [2]],
             [[1, 1], [3]],
             [[1, 2], [2]],
             [[1, 3], [2]],
             [[1, 2], [3]],
             [[1, 3], [3]],
             [[2, 2], [3]],
             [[2, 3], [3]]]
            sage: from sage.combinat.skew_tableau import SemistandardSkewTableaux_shape
            sage: SemistandardSkewTableaux_shape([[2,1],[]], max_entry=2).list()
            [[[1, 1], [2]], [[1, 2], [2]]]
        """

class SemistandardSkewTableaux_shape_weight(SemistandardSkewTableaux):
    """
    Class of semistandard skew tableaux of a fixed skew shape `\\lambda / \\nu`
    and weight `\\mu`.
    """
    @staticmethod
    def __classcall_private__(cls, p, mu):
        """
        Normalize our input to ensure we have a unique representation.

        EXAMPLES::

            sage: S = SemistandardSkewTableaux([[2,1],[]], [2,1])
            sage: S2 = SemistandardSkewTableaux(SkewPartition([[2,1],[]]), (2,1))
            sage: S is S2
            True
        """
    p: Incomplete
    mu: Incomplete
    def __init__(self, p, mu) -> None:
        """
        EXAMPLES::

            sage: S = SemistandardSkewTableaux([[2,1],[]],[2,1])
            sage: S == loads(dumps(S))
            True
            sage: TestSuite(S).run()
        """
    def __iter__(self):
        """
        Iterate over ``self``.

        EXAMPLES::

            sage: SemistandardSkewTableaux([[2,1],[]],[2,1]).list()
            [[[1, 1], [2]]]
        """

class SkewTableau_class(SkewTableau):
    """
    This exists solely for unpickling ``SkewTableau_class`` objects.
    """
