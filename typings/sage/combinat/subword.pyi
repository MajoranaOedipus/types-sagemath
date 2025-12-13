from collections.abc import Iterator
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.rings.integer import Integer as Integer
from sage.sets.finite_enumerated_set import FiniteEnumeratedSet as FiniteEnumeratedSet
from sage.structure.parent import Parent as Parent

def Subwords(w, k=None, element_constructor=None):
    """
    Return the set of subwords of ``w``.

    INPUT:

    - ``w`` -- a word (can be a list, a string, a tuple or a word)

    - ``k`` -- an optional integer to specify the length of subwords

    - ``element_constructor`` -- an optional function that will be used
      to build the subwords

    EXAMPLES::

        sage: S = Subwords(['a','b','c']); S
        Subwords of ['a', 'b', 'c']
        sage: S.first()
        []
        sage: S.last()
        ['a', 'b', 'c']
        sage: S.list()
        [[], ['a'], ['b'], ['c'], ['a', 'b'], ['a', 'c'], ['b', 'c'], ['a', 'b', 'c']]

    The same example using string, tuple or a word::

        sage: S = Subwords('abc'); S
        Subwords of 'abc'
        sage: S.list()
        ['', 'a', 'b', 'c', 'ab', 'ac', 'bc', 'abc']

        sage: S = Subwords((1,2,3)); S
        Subwords of (1, 2, 3)
        sage: S.list()
        [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]

        sage: w = Word([1,2,3])
        sage: S = Subwords(w); S
        Subwords of word: 123
        sage: S.list()
        [word: , word: 1, word: 2, word: 3, word: 12, word: 13, word: 23, word: 123]

    Using word with specified length::

        sage: S = Subwords(['a','b','c'], 2); S
        Subwords of ['a', 'b', 'c'] of length 2
        sage: S.list()
        [['a', 'b'], ['a', 'c'], ['b', 'c']]

    An example that uses the ``element_constructor`` argument::

        sage: p = Permutation([3,2,1])
        sage: Subwords(p, element_constructor=tuple).list()
        [(), (3,), (2,), (1,), (3, 2), (3, 1), (2, 1), (3, 2, 1)]
        sage: Subwords(p, 2, element_constructor=tuple).list()
        [(3, 2), (3, 1), (2, 1)]
    """

class Subwords_w(Parent):
    """
    Subwords of a given word.
    """
    def __init__(self, w, element_constructor) -> None:
        """
        TESTS::

            sage: TestSuite(Subwords([1,2,3])).run()
            sage: TestSuite(Subwords('sage')).run()
        """
    def __eq__(self, other) -> bool:
        """
        Equality test.

        TESTS::

            sage: Subwords([1,2,3]) == Subwords([1,2,3])
            True
            sage: Subwords([1,2,3]) == Subwords([1,3,2])
            False
        """
    def __ne__(self, other) -> bool:
        """
        TESTS::

            sage: Subwords([1,2,3]) != Subwords([1,2,3])
            False
            sage: Subwords([1,2,3]) != Subwords([1,3,2])
            True
        """
    def __reduce__(self):
        """
        Pickle (how to construct back the object).

        TESTS::

            sage: S = Subwords((1,2,3))
            sage: S == loads(dumps(S))
            True
            sage: S = Subwords('123')
            sage: S == loads(dumps(S))
            True
            sage: S = Subwords(('a',(1,2,3),('a','b'),'ir'))
            sage: S == loads(dumps(S))
            True
        """
    def __contains__(self, w) -> bool:
        """
        TESTS::

            sage: [] in Subwords([1,2,3,4,3,4,4])
            True
            sage: [2,3,3,4] in Subwords([1,2,3,4,3,4,4])
            True
            sage: [5,5,3] in Subwords([1,3,3,5,4,5,3,5])
            True
            sage: [3,5,5,3] in Subwords([1,3,3,5,4,5,3,5])
            True
            sage: [3,5,5,3,4] in Subwords([1,3,3,5,4,5,3,5])
            False
            sage: [2,3,3,4] in Subwords([1,2,3,4,3,4,4])
            True
            sage: [2,3,3,1] in Subwords([1,2,3,4,3,4,4])
            False
        """
    def cardinality(self) -> Integer:
        """
        EXAMPLES::

            sage: Subwords([1,2,3]).cardinality()
            8
        """
    def first(self):
        """
        EXAMPLES::

            sage: Subwords([1,2,3]).first()
            []
            sage: Subwords((1,2,3)).first()
            ()
            sage: Subwords('123').first()
            ''
        """
    def last(self):
        """
        EXAMPLES::

            sage: Subwords([1,2,3]).last()
            [1, 2, 3]
            sage: Subwords((1,2,3)).last()
            (1, 2, 3)
            sage: Subwords('123').last()
            '123'
        """
    def random_element(self):
        """
        Return a random subword with uniform law.

        EXAMPLES::

            sage: S1 = Subwords([1,2,3,2,1,3])
            sage: S2 = Subwords([4,6,6,6,7,4,5,5])
            sage: for i in range(100):
            ....:   w = S1.random_element()
            ....:   if w in S2:
            ....:       assert not w
            sage: for i in range(100):
            ....:   w = S2.random_element()
            ....:   if w in S1:
            ....:       assert not w
        """
    def __iter__(self) -> Iterator:
        """
        EXAMPLES::

            sage: Subwords([1,2,3]).list()
            [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
            sage: Subwords((1,2,3)).list()
            [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
            sage: Subwords('123').list()
            ['', '1', '2', '3', '12', '13', '23', '123']
        """

class Subwords_wk(Subwords_w):
    """
    Subwords with fixed length of a given word.
    """
    def __init__(self, w, k, element_constructor) -> None:
        """
        TESTS::

            sage: S = Subwords([1,2,3],2)
            sage: S == loads(dumps(S))
            True
            sage: TestSuite(S).run()
        """
    def __eq__(self, other) -> bool:
        """
        Equality test.

        TESTS::

            sage: Subwords([1,2,3],2) == Subwords([1,2,3],2)
            True
            sage: Subwords([1,2,3],2) == Subwords([1,3,2],2)
            False
            sage: Subwords([1,2,3],2) == Subwords([1,2,3],3)
            False
        """
    def __ne__(self, other) -> bool:
        """
        TESTS::

            sage: Subwords([1,2,3], 2) != Subwords([1,2,3], 2)
            False
            sage: Subwords([1,2,3], 2) != Subwords([1,3,2], 1)
            True
        """
    def __reduce__(self):
        """
        Pickle (how to construct back the object).

        TESTS::

            sage: S = Subwords('abc',2)
            sage: S == loads(dumps(S))
            True
            sage: S = Subwords(('a',1,'45',(1,2)))
            sage: S == loads(dumps(S))
            True
        """
    def __contains__(self, w) -> bool:
        """
        TESTS::

            sage: [] in Subwords([1, 3, 3, 5, 4, 5, 3, 5],0)
            True
            sage: [2,3,3,4] in Subwords([1,2,3,4,3,4,4],4)
            True
            sage: [2,3,3,4] in Subwords([1,2,3,4,3,4,4],3)
            False
            sage: [5,5,3] in Subwords([1,3,3,5,4,5,3,5],3)
            True
            sage: [5,5,3] in Subwords([1,3,3,5,4,5,3,5],4)
            False
        """
    def cardinality(self) -> Integer:
        """
        Return the number of subwords of w of length k.

        EXAMPLES::

            sage: Subwords([1,2,3], 2).cardinality()
            3
        """
    def first(self):
        """
        EXAMPLES::

            sage: Subwords([1,2,3],2).first()
            [1, 2]
            sage: Subwords([1,2,3],0).first()
            []
            sage: Subwords((1,2,3),2).first()
            (1, 2)
            sage: Subwords((1,2,3),0).first()
            ()
            sage: Subwords('123',2).first()
            '12'
            sage: Subwords('123',0).first()
            ''
        """
    def last(self):
        """
        EXAMPLES::

            sage: Subwords([1,2,3],2).last()
            [2, 3]
            sage: Subwords([1,2,3],0).last()
            []
            sage: Subwords((1,2,3),2).last()
            (2, 3)
            sage: Subwords((1,2,3),0).last()
            ()
            sage: Subwords('123',2).last()
            '23'
            sage: Subwords('123',0).last()
            ''

        TESTS::

            sage: Subwords('123', 0).last()  # trac 10534
            ''
        """
    def random_element(self):
        """
        Return a random subword of given length with uniform law.

        EXAMPLES::

            sage: S1 = Subwords([1,2,3,2,1],3)
            sage: S2 = Subwords([4,4,5,5,4,5,4,4],3)
            sage: for i in range(100):
            ....:   w = S1.random_element()
            ....:   if w in S2:
            ....:       assert not w
            sage: for i in range(100):
            ....:   w = S2.random_element()
            ....:   if w in S1:
            ....:       assert not w
        """
    def __iter__(self) -> Iterator:
        """
        EXAMPLES::

            sage: Subwords([1,2,3],2).list()
            [[1, 2], [1, 3], [2, 3]]
            sage: Subwords([1,2,3],0).list()
            [[]]
            sage: Subwords((1,2,3),2).list()
            [(1, 2), (1, 3), (2, 3)]
            sage: Subwords((1,2,3),0).list()
            [()]
            sage: Subwords('abc',2).list()
            ['ab', 'ac', 'bc']
            sage: Subwords('abc',0).list()
            ['']
        """

def smallest_positions(word, subword, pos: int = 0) -> list | bool:
    '''
    Return the smallest positions for which ``subword`` appears as a
    subword of ``word``.

    If ``pos`` is specified, then it returns the positions
    of the first appearance of subword starting at ``pos``.

    If ``subword`` is not found in ``word``, then return ``False``.

    EXAMPLES::

        sage: sage.combinat.subword.smallest_positions([1,2,3,4], [2,4])
        [1, 3]
        sage: sage.combinat.subword.smallest_positions([1,2,3,4,4], [2,4])
        [1, 3]
        sage: sage.combinat.subword.smallest_positions([1,2,3,3,4,4], [3,4])
        [2, 4]
        sage: sage.combinat.subword.smallest_positions([1,2,3,3,4,4], [3,4],2)
        [2, 4]
        sage: sage.combinat.subword.smallest_positions([1,2,3,3,4,4], [3,4],3)
        [3, 4]
        sage: sage.combinat.subword.smallest_positions([1,2,3,4], [2,3])
        [1, 2]
        sage: sage.combinat.subword.smallest_positions([1,2,3,4], [5,5])
        False
        sage: sage.combinat.subword.smallest_positions([1,3,3,4,5],[3,5])
        [1, 4]
        sage: sage.combinat.subword.smallest_positions([1,3,3,5,4,5,3,5],[3,5,3])
        [1, 3, 6]
        sage: sage.combinat.subword.smallest_positions([1,3,3,5,4,5,3,5],[3,5,3],2)
        [2, 3, 6]
        sage: sage.combinat.subword.smallest_positions([1,2,3,4,3,4,4],[2,3,3,1])
        False
        sage: sage.combinat.subword.smallest_positions([1,3,3,5,4,5,3,5],[3,5,3],3)
        False

    TESTS:

    We check for :issue:`5534`::

        sage: w = ["a", "b", "c", "d"]; ww = ["b", "d"]
        sage: x = sage.combinat.subword.smallest_positions(w, ww); ww
        [\'b\', \'d\']
    '''
