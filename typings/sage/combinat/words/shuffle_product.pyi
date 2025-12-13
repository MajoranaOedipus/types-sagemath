from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.combinat.composition import Composition as Composition
from sage.combinat.integer_vector import IntegerVectors as IntegerVectors
from sage.combinat.words.word import Word as Word, Word_class as Word_class
from sage.rings.integer import Integer as Integer
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class ShuffleProduct_w1w2(Parent, UniqueRepresentation):
    def __init__(self, w1, w2, check: bool = True) -> None:
        """
        The shuffle product of the two words ``w1`` and ``w2``.

        If `u` and `v` are two words, then the *shuffle product* of
        `u` and `v` is a certain multiset of words defined as follows:
        Let `a` and `b` be the lengths of `u` and `v`, respectively.
        For every `a`-element subset `I` of `\\{1, 2, \\cdots, a+b\\}`,
        let `w(I)` be the length-`a+b` word such that:

        - for every `1 \\leq k \\leq a`, the `i_k`-th letter of `w(I)`
          is the `k`-th letter of `u`, where `i_k` is the
          `k`-th smallest element of `I`;

        - for every `1 \\leq l \\leq b`, the `j_l`-th letter of `w(I)`
          is the `l`-th letter of `v`, where `j_l` is the
          `l`-th smallest element of
          `\\{1, 2, \\cdots, a+b\\} \\setminus I`.

        The shuffle product of `u` and `v` is then the multiset of
        all `w(I)` with `I` ranging over the `a`-element subsets of
        `\\{1, 2, \\cdots, a+b\\}`.

        INPUT:

        - ``check`` -- boolean (default: ``True``); whether to check that
          all words in the shuffle product belong to the correct parent

        EXAMPLES::

            sage: from sage.combinat.words.shuffle_product import ShuffleProduct_w1w2
            sage: W = Words([1,2,3,4])
            sage: s = ShuffleProduct_w1w2(W([1,2]),W([3,4]))
            sage: sorted(s)
            [word: 1234, word: 1324, word: 1342, word: 3124,
             word: 3142, word: 3412]
            sage: s == loads(dumps(s))
            True
            sage: TestSuite(s).run()

            sage: s = ShuffleProduct_w1w2(W([1,4,3]),W([2]))
            sage: sorted(s)
            [word: 1243, word: 1423, word: 1432, word: 2143]

            sage: s = ShuffleProduct_w1w2(W([1,4,3]),W([]))
            sage: sorted(s)
            [word: 143]

        TESTS::

            sage: W = Words([1,2,3,4])
            sage: s = ShuffleProduct_w1w2(W([1,2]), W([3,4]), check=False)
            sage: len(list(s))
            6
        """
    def __contains__(self, x) -> bool:
        '''
        EXAMPLES::

            sage: from sage.combinat.words.shuffle_product import ShuffleProduct_w1w2
            sage: W = Words("abcd")
            sage: w = W("ab")
            sage: u = W("cd")
            sage: S = ShuffleProduct_w1w2(w,u)
            sage: w*u in S
            True
            sage: all(w.is_subword_of(x) for x in S)
            True
            sage: w in S
            False

        We check that :issue:`14121` is solved::

            sage: w = W(\'ab\')
            sage: x = W(\'ac\')
            sage: x*w in w.shuffle(x)
            True
        '''
    def cardinality(self):
        '''
        Return the number of words in the shuffle product
        of ``w1`` and ``w2``.

        This is understood as a multiset cardinality, not as a
        set cardinality; it does not count the distinct words only.

        It is given by `\\binom{l_1+l_2}{l_1}`, where `l_1` is the
        length of ``w1`` and where `l_2` is the length of ``w2``.

        EXAMPLES::

            sage: from sage.combinat.words.shuffle_product import ShuffleProduct_w1w2
            sage: w, u = map(Words("abcd"), ["ab", "cd"])
            sage: S = ShuffleProduct_w1w2(w,u)
            sage: S.cardinality()
            6

            sage: w, u = map(Words("ab"), ["ab", "ab"])
            sage: S = ShuffleProduct_w1w2(w,u)
            sage: S.cardinality()
            6
        '''
    def __iter__(self):
        '''
        Return an iterator for the words in the
        shuffle product of ``w1`` and ``w2``.

        EXAMPLES::

            sage: from sage.combinat.words.shuffle_product import ShuffleProduct_w1w2
            sage: w, u = map(Words("abcd"), ["ab", "cd"])
            sage: S = ShuffleProduct_w1w2(w,u)
            sage: S.list() #indirect test
            [word: abcd, word: acbd, word: acdb, word: cabd,
             word: cadb, word: cdab]

            sage: I = Composition([1, 1])
            sage: J = Composition([2])
            sage: S = ShuffleProduct_w1w2(I, J)
            sage: next(iter(S))
            [1, 1, 2]

        TESTS:

        Sage is no longer confused by a too-restrictive parent of `I`
        when shuffling compositions `I` and `J` (cf. :issue:`15131`)::

            sage: I = Compositions(2)([1, 1])
            sage: J = Composition([2])
            sage: S = ShuffleProduct_w1w2(I, J)
            sage: S.list()
            [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
        '''

class ShuffleProduct_shifted(ShuffleProduct_w1w2):
    def __init__(self, w1, w2, check: bool = True) -> None:
        """
        Shifted shuffle product of ``w1`` with ``w2``.

        This is the shuffle product of ``w1`` with the word
        obtained by adding the length of ``w1`` to every letter
        of ``w2``.

        Note that this class is meant to be used for words; it
        misbehaves when ``w1`` is a permutation or composition.

        INPUT:

        - ``check`` -- boolean (default: ``True``); whether to check that
          all words in the shuffle product belong to the correct parent

        EXAMPLES::

            sage: from sage.combinat.words.shuffle_product import ShuffleProduct_shifted
            sage: w, u = Word([1,2]), Word([3,4])
            sage: S = ShuffleProduct_shifted(w,u)
            sage: S == loads(dumps(S))
            True

        TESTS::

            sage: w, u = Word([1,2]), Word([3,4])
            sage: S = ShuffleProduct_shifted(w, u, check=False)
            sage: len(list(S))
            6
        """
