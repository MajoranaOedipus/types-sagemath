from .combinat import catalan_number as catalan_number
from _typeshed import Incomplete
from sage.categories.infinite_enumerated_sets import InfiniteEnumeratedSets as InfiniteEnumeratedSets
from sage.categories.monoids import Monoids as Monoids
from sage.categories.sets_with_grading import SetsWithGrading as SetsWithGrading
from sage.rings.integer import Integer as Integer
from sage.rings.semirings.non_negative_integer_semiring import NN as NN
from sage.structure.element import Element as Element
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import richcmp as richcmp
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

def NonDecreasingParkingFunctions(n=None):
    '''
    Return the set of Non-Decreasing Parking Functions.

    A *non-decreasing parking function* of size `n` is a non-decreasing
    function `f` from `\\{1,\\dots,n\\}` to itself such that for all `i`,
    one has `f(i) \\leq i`.

    EXAMPLES:

    Here are all the-non decreasing parking functions of size 5::

        sage: NonDecreasingParkingFunctions(3).list()
        [[1, 1, 1], [1, 1, 2], [1, 1, 3], [1, 2, 2], [1, 2, 3]]

    If no size is specified, then NonDecreasingParkingFunctions
    returns the set of all non-decreasing parking functions.

    ::

        sage: PF = NonDecreasingParkingFunctions(); PF
        Non-decreasing parking functions
        sage: [] in PF
        True
        sage: [1] in PF
        True
        sage: [2] in PF
        False
        sage: [1,1,3] in PF
        True
        sage: [1,1,4] in PF
        False

    If the size `n` is specified, then NonDecreasingParkingFunctions returns
    the set of all non-decreasing parking functions of size `n`.

    ::

        sage: PF = NonDecreasingParkingFunctions(0)
        sage: PF.list()
        [[]]
        sage: PF = NonDecreasingParkingFunctions(1)
        sage: PF.list()
        [[1]]
        sage: PF = NonDecreasingParkingFunctions(3)
        sage: PF.list()
        [[1, 1, 1], [1, 1, 2], [1, 1, 3], [1, 2, 2], [1, 2, 3]]

        sage: PF3 = NonDecreasingParkingFunctions(3); PF3
        Non-decreasing parking functions of size 3
        sage: [] in PF3
        False
        sage: [1] in PF3
        False
        sage: [1,1,3] in PF3
        True
        sage: [1,1,4] in PF3
        False

    TESTS::

        sage: PF = NonDecreasingParkingFunctions(5)
        sage: len(PF.list()) == PF.cardinality()
        True
        sage: NonDecreasingParkingFunctions("foo")
        Traceback (most recent call last):
        ...
        TypeError: unable to convert \'foo\' to an integer
    '''
def is_a(x, n=None) -> bool:
    """
    Check whether a list is a non-decreasing parking function.

    If a size `n` is specified, checks if a list is a non-decreasing
    parking function of size `n`.

    TESTS::

        sage: from sage.combinat.non_decreasing_parking_function import is_a
        sage: is_a([1,1,2])
        True
        sage: is_a([1,1,4])
        False
        sage: is_a([1,1,3], 3)
        True
    """

class NonDecreasingParkingFunction(Element):
    """
    A *non decreasing parking function* of size `n` is a non-decreasing
    function `f` from `\\{1,\\dots,n\\}` to itself such that for all `i`,
    one has `f(i) \\leq i`.

    EXAMPLES::

        sage: NonDecreasingParkingFunction([])
        []
        sage: NonDecreasingParkingFunction([1])
        [1]
        sage: NonDecreasingParkingFunction([2])
        Traceback (most recent call last):
        ...
        ValueError: [2] is not a non-decreasing parking function
        sage: NonDecreasingParkingFunction([1,2])
        [1, 2]
        sage: NonDecreasingParkingFunction([1,1,2])
        [1, 1, 2]
        sage: NonDecreasingParkingFunction([1,1,4])
        Traceback (most recent call last):
        ...
        ValueError: [1, 1, 4] is not a non-decreasing parking function
    """
    def __init__(self, lst) -> None:
        """
        TESTS::

            sage: NonDecreasingParkingFunction([1, 1, 2, 2, 5, 6])
            [1, 1, 2, 2, 5, 6]
        """
    def __getitem__(self, n):
        '''
        Return the `n`-th item in the underlying list.

        .. NOTE::

           Note that this is different than the image of `n` under
           function.  It is "off by one".

        EXAMPLES::

            sage: p = NonDecreasingParkingFunction([1, 1, 2, 2, 5, 6])
            sage: p[0]
            1
            sage: p[2]
            2
        '''
    def __call__(self, n):
        """
        Return the image of ``n`` under the parking function.

        EXAMPLES::

            sage: p = NonDecreasingParkingFunction([1, 1, 2, 2, 5, 6])
            sage: p(3)
            2
            sage: p(6)
            6
        """
    def to_dyck_word(self):
        """
        Implement the bijection to :class:`Dyck
        words<sage.combinat.dyck_word.DyckWords>`, which is defined as follows.
        Take a non decreasing parking function, say [1,1,2,4,5,5], and draw
        its graph::

                     ___
                    |  . 5
                   _|  . 5
               ___|  . . 4
             _|  . . . . 2
            |  . . . . . 1
            |  . . . . . 1

        The corresponding Dyck word [1,1,0,1,0,0,1,0,1,1,0,0] is then read off
        from the sequence of horizontal and vertical steps. The converse
        bijection is :meth:`.from_dyck_word`.

        EXAMPLES::

            sage: NonDecreasingParkingFunction([1,1,2,4,5,5]).to_dyck_word()
            [1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0]
            sage: NonDecreasingParkingFunction([]).to_dyck_word()
            []
            sage: NonDecreasingParkingFunction([1,1,1]).to_dyck_word()
            [1, 1, 1, 0, 0, 0]
            sage: NonDecreasingParkingFunction([1,2,3]).to_dyck_word()
            [1, 0, 1, 0, 1, 0]
            sage: NonDecreasingParkingFunction([1,1,3,3,4,6,6]).to_dyck_word()
            [1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0]

        TESTS::

            sage: ndpf = NonDecreasingParkingFunctions(5)
            sage: list(ndpf) == [pf.to_dyck_word().to_non_decreasing_parking_function() for pf in ndpf]
            True
        """
    def __len__(self) -> int:
        """
        Return the length of ``self``.

        EXAMPLES::

            sage: ndpf = NonDecreasingParkingFunctions(5)
            sage: len(ndpf.random_element())
            5
        """
    grade = __len__
    def __hash__(self) -> int:
        """
        Return the hash of ``self``.

        EXAMPLES::

            sage: a = NonDecreasingParkingFunction([1,1,1])
            sage: b = NonDecreasingParkingFunction([1,1,2])
            sage: hash(a) == hash(b)
            False
        """
    @classmethod
    def from_dyck_word(cls, dw) -> NonDecreasingParkingFunction:
        """
        Bijection from :class:`Dyck
        words<sage.combinat.dyck_word.DyckWords>`. It is the inverse of the
        bijection :meth:`.to_dyck_word`. You can find there the mathematical
        definition.

        EXAMPLES::

            sage: NonDecreasingParkingFunction.from_dyck_word([])
            []
            sage: NonDecreasingParkingFunction.from_dyck_word([1,0])
            [1]
            sage: NonDecreasingParkingFunction.from_dyck_word([1,1,0,0])
            [1, 1]
            sage: NonDecreasingParkingFunction.from_dyck_word([1,0,1,0])
            [1, 2]
            sage: NonDecreasingParkingFunction.from_dyck_word([1,0,1,1,0,1,0,0,1,0])
            [1, 2, 2, 3, 5]

        TESTS::

          sage: ndpf = NonDecreasingParkingFunctions(5)
          sage: list(ndpf) == [NonDecreasingParkingFunction.from_dyck_word(pf.to_dyck_word()) for pf in ndpf]
          True
        """

class NonDecreasingParkingFunctions_all(UniqueRepresentation, Parent):
    def __init__(self) -> None:
        """
        TESTS::

            sage: PF = NonDecreasingParkingFunctions()
            sage: PF == loads(dumps(PF))
            True
        """
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: [] in NonDecreasingParkingFunctions()
            True
            sage: [1] in NonDecreasingParkingFunctions()
            True
            sage: [2] in NonDecreasingParkingFunctions()
            False
            sage: [1,1,3] in NonDecreasingParkingFunctions()
            True
            sage: [1,1,4] in NonDecreasingParkingFunctions()
            False
        """
    def __iter__(self):
        """
        An iterator.

        TESTS::

            sage: it = iter(NonDecreasingParkingFunctions()) # indirect doctest
            sage: [next(it) for i in range(8)]
            [[], [1], [1, 1], [1, 2], [1, 1, 1], [1, 1, 2], [1, 1, 3], [1, 2, 2]]
        """
    def graded_component(self, n):
        """
        Return the graded component.

        EXAMPLES::

            sage: P = NonDecreasingParkingFunctions()
            sage: P.graded_component(4) == NonDecreasingParkingFunctions(4)
            True
        """

class NonDecreasingParkingFunctions_n(UniqueRepresentation, Parent):
    """
    The combinatorial class of non-decreasing parking functions of
    size `n`.

    A *non-decreasing parking function* of size `n` is a non-decreasing
    function `f` from `\\{1,\\dots,n\\}` to itself such that for all `i`,
    one has `f(i) \\leq i`.

    The number of non-decreasing parking functions of size `n` is the
    `n`-th Catalan number.

    EXAMPLES::

        sage: PF = NonDecreasingParkingFunctions(3)
        sage: PF.list()
        [[1, 1, 1], [1, 1, 2], [1, 1, 3], [1, 2, 2], [1, 2, 3]]
        sage: PF = NonDecreasingParkingFunctions(4)
        sage: PF.list()
        [[1, 1, 1, 1], [1, 1, 1, 2], [1, 1, 1, 3], [1, 1, 1, 4], [1, 1, 2, 2], [1, 1, 2, 3], [1, 1, 2, 4], [1, 1, 3, 3], [1, 1, 3, 4], [1, 2, 2, 2], [1, 2, 2, 3], [1, 2, 2, 4], [1, 2, 3, 3], [1, 2, 3, 4]]
        sage: [ NonDecreasingParkingFunctions(i).cardinality() for i in range(10)]
        [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862]

    .. warning::

       The precise order in which the parking function are generated or
       listed is not fixed, and may change in the future.

    AUTHORS:

    - Florent Hivert
    """
    n: Incomplete
    def __init__(self, n) -> None:
        """
        TESTS::

            sage: PF = NonDecreasingParkingFunctions(3)
            sage: PF == loads(dumps(PF))
            True
            sage: TestSuite(PF).run(skip='_test_elements')
        """
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: PF3 = NonDecreasingParkingFunctions(3); PF3
            Non-decreasing parking functions of size 3
            sage: [] in PF3
            False
            sage: [1] in PF3
            False
            sage: [1,1,3] in PF3
            True
            sage: [1,1,1] in PF3
            True
            sage: [1,1,4] in PF3
            False
            sage: all(p in PF3 for p in PF3)
            True
        """
    def cardinality(self) -> Integer:
        """
        Return the number of non-decreasing parking functions of size
        `n`.

        This number is the `n`-th :func:`Catalan
        number<sage.combinat.combinat.catalan_number>`.

        EXAMPLES::

            sage: PF = NonDecreasingParkingFunctions(0)
            sage: PF.cardinality()
            1
            sage: PF = NonDecreasingParkingFunctions(1)
            sage: PF.cardinality()
            1
            sage: PF = NonDecreasingParkingFunctions(3)
            sage: PF.cardinality()
            5
            sage: PF = NonDecreasingParkingFunctions(5)
            sage: PF.cardinality()
            42
        """
    def random_element(self) -> NonDecreasingParkingFunction:
        """
        Return a random parking function of the given size.

        EXAMPLES::

            sage: ndpf = NonDecreasingParkingFunctions(5)
            sage: x = ndpf.random_element(); x  # random
            [1, 2, 2, 4, 5]
            sage: x in ndpf
            True
        """
    def one(self) -> NonDecreasingParkingFunction:
        """
        Return the unit of this monoid.

        This is the non-decreasing parking function [1, 2, ..., n].

        EXAMPLES::

            sage: ndpf = NonDecreasingParkingFunctions(5)
            sage: x = ndpf.random_element(); x  # random
            sage: e = ndpf.one()
            sage: x == e*x == x*e
            True
        """
    def __iter__(self):
        """
        Return an iterator for non-decreasing parking functions of size `n`.

        .. warning::

           The precise order in which the parking function are
           generated is not fixed, and may change in the future.

        EXAMPLES::

            sage: PF = NonDecreasingParkingFunctions(0)
            sage: [e for e in PF]      # indirect doctest
            [[]]
            sage: PF = NonDecreasingParkingFunctions(1)
            sage: [e for e in PF]      # indirect doctest
            [[1]]
            sage: PF = NonDecreasingParkingFunctions(3)
            sage: [e for e in PF]      # indirect doctest
            [[1, 1, 1], [1, 1, 2], [1, 1, 3], [1, 2, 2], [1, 2, 3]]
            sage: PF = NonDecreasingParkingFunctions(4)
            sage: [e for e in PF]      # indirect doctest
            [[1, 1, 1, 1], [1, 1, 1, 2], [1, 1, 1, 3], [1, 1, 1, 4], [1, 1, 2, 2], [1, 1, 2, 3], [1, 1, 2, 4], [1, 1, 3, 3], [1, 1, 3, 4], [1, 2, 2, 2], [1, 2, 2, 3], [1, 2, 2, 4], [1, 2, 3, 3], [1, 2, 3, 4]]

        TESTS::

            sage: PF = NonDecreasingParkingFunctions(5)
            sage: [e for e in PF] == PF.list()
            True
            sage: PF = NonDecreasingParkingFunctions(6)
            sage: [e for e in PF] == PF.list()
            True

        Complexity: constant amortized time.
        """
    Element = NonDecreasingParkingFunction
