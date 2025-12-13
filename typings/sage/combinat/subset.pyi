from . import combination as combination
from _typeshed import Incomplete
from collections.abc import Generator
from sage.arith.misc import binomial as binomial
from sage.categories.enumerated_sets import EnumeratedSets as EnumeratedSets
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.categories.sets_cat import EmptySetError as EmptySetError, Sets as Sets
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.sets.set import Set as Set, Set_object_enumerated as Set_object_enumerated
from sage.structure.element import Element as Element
from sage.structure.parent import Parent as Parent

ZZ_0: Incomplete

def Subsets(s, k=None, submultiset: bool = False):
    """
    Return the combinatorial class of the subsets of the finite set
    ``s``. The set can be given as a list, Set or any iterable
    convertible to a set. Alternatively, a nonnegative integer `n`
    can be provided in place of ``s``; in this case, the result is
    the combinatorial class of the subsets of the set
    `\\{1,2,\\dots,n\\}` (i.e. of the Sage ``range(1,n+1)``).

    A second optional parameter ``k`` can be given. In this case,
    ``Subsets`` returns the combinatorial class of subsets of ``s``
    of size ``k``.

    .. WARNING::

        The subsets are returned as Sets. Do not assume that
        these Sets are ordered; they often are not!
        (E.g., ``Subsets(10).list()[619]`` returns
        ``{10, 4, 5, 6, 7}`` on my system.)
        See :class:`SubsetsSorted` for a similar class which
        returns the subsets as sorted tuples.

    Finally the option ``submultiset`` allows one to deal with sets with
    repeated elements, usually called multisets. The method then
    returns the class of all multisets in which every element is
    contained at most as often as it is contained in ``s``. These
    multisets are encoded as lists.

    EXAMPLES::

        sage: S = Subsets([1, 2, 3]); S
        Subsets of {1, 2, 3}
        sage: S.cardinality()
        8
        sage: S.first()
        {}
        sage: S.last()
        {1, 2, 3}
        sage: S.random_element() in S
        True
        sage: S.list()
        [{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}]

    Here is the same example where the set is given as an integer::

        sage: S = Subsets(3)
        sage: S.list()
        [{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}]

    We demonstrate various the effect of the various options::

        sage: S = Subsets(3, 2); S
        Subsets of {1, 2, 3} of size 2
        sage: S.list()
        [{1, 2}, {1, 3}, {2, 3}]

        sage: S = Subsets([1, 2, 2], submultiset=True); S
        SubMultiset of [1, 2, 2]
        sage: S.list()
        [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]

        sage: S = Subsets([1, 2, 2, 3], 3, submultiset=True); S
        SubMultiset of [1, 2, 2, 3] of size 3
        sage: S.list()
        [[1, 2, 2], [1, 2, 3], [2, 2, 3]]

        sage: S = Subsets(['a','b','a','b'], 2, submultiset=True); S.list()
        [['a', 'a'], ['a', 'b'], ['b', 'b']]


    And it is possible to play with subsets of subsets::

        sage: S = Subsets(3)
        sage: S2 = Subsets(S); S2
        Subsets of Subsets of {1, 2, 3}
        sage: S2.cardinality()
        256
        sage: it = iter(S2)
        sage: [next(it) for _ in range(8)]
        [{}, {{}}, {{1}}, {{2}}, {{3}}, {{1, 2}},  {{1, 3}}, {{2, 3}}]
        sage: S2.random_element()     # random
        {{2}, {1, 2, 3}, {}}
        sage: [S2.unrank(k) for k in range(256)] == S2.list()
        True

        sage: S3 = Subsets(S2)
        sage: S3.cardinality()
        115792089237316195423570985008687907853269984665640564039457584007913129639936
        sage: S3.unrank(14123091480)  # random
        {{{2}, {1, 2, 3}, {1, 2}, {3}, {}},
         {{1, 2, 3}, {2}, {1}, {1, 3}},
         {{}, {2}, {2, 3}, {1, 2}},
         {{}, {2}, {1, 2, 3}, {1, 2}},
         {},
         {{}, {1}, {1, 2, 3}}}

        sage: T = Subsets(S2, 10)
        sage: T.cardinality()
        278826214642518400
        sage: T.unrank(1441231049)  # random
        {{{1, 2, 3}, {2}, {2, 3}}, {{3}, {1, 3}, ..., {3}, {1}, {}, {1, 3}}}
    """

class Subsets_s(Parent):
    """
    Subsets of a given set.

    EXAMPLES::

        sage: S = Subsets(4); S
        Subsets of {1, 2, 3, 4}
        sage: S.cardinality()
        16
        sage: Subsets(4).list()
        [{}, {1}, {2}, {3}, {4},
         {1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4},
         {1, 2, 3}, {1, 2, 4}, {1, 3, 4}, {2, 3, 4},
         {1, 2, 3, 4}]

        sage: S = Subsets(Subsets(Subsets(GF(3)))); S
        Subsets of Subsets of Subsets of Finite Field of size 3
        sage: S.cardinality()
        115792089237316195423570985008687907853269984665640564039457584007913129639936
        sage: S.unrank(3149254230)  # random
        {{{1}, {0, 2}}, {{0, 1, 2}, {0, 1}, {1}, {1, 2}},
         {{2}, {1, 2}, {0, 1, 2}, {0, 2}, {1}, {}},
         {{1, 2}, {0}},
         {{0, 1, 2}, {0, 1}, {0, 2}, {1, 2}}}
    """
    element_class = Set_object_enumerated
    def __init__(self, s) -> None:
        '''
        TESTS::

            sage: s = Subsets(Set([1]))
            sage: e = s.first()
            sage: isinstance(e, s.element_class)
            True

        In the following "_test_elements" is temporarily disabled
        until :class:`sage.sets.set.Set_object_enumerated` objects
        pass the category tests::

            sage: S = Subsets([1,2,3])
            sage: TestSuite(S).run(skip=["_test_elements"])

            sage: S = sage.sets.set.Set_object_enumerated([1,2])
            sage: TestSuite(S).run()
        '''
    def underlying_set(self):
        """
        Return the set of elements.

        EXAMPLES::

            sage: Subsets(GF(13)).underlying_set()
            {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
        """
    def __eq__(self, other):
        """
        Equality test.

        TESTS::

            sage: Subsets([0,1,2]) == Subsets([1,2,3])
            False
            sage: Subsets([0,1,2]) == Subsets([0,1,2])
            True
            sage: Subsets([0,1,2]) == Subsets([0,1,2],2)
            False
        """
    def __ne__(self, other):
        """
        Difference test.

        TESTS::

            sage: Subsets([0,1,2]) != Subsets([1,2,3])
            True
            sage: Subsets([0,1,2]) != Subsets([0,1,2])
            False
            sage: Subsets([0,1,2]) != Subsets([0,1,2],2)
            True
        """
    def __hash__(self):
        """
        Return the hash of ``self``.

        TESTS::

            sage: hash(Subsets([0,1,2])) == hash(Subsets([1,2,3]))
            False
            sage: hash(Subsets([0,1,2])) == hash(Subsets([0,1,2]))
            True
            sage: hash(Subsets([0,1,2])) == hash(Subsets([0,1,2],2))
            False
        """
    def __contains__(self, value) -> bool:
        """
        TESTS::

            sage: S = Subsets([1,2,3])
            sage: Set([1,2]) in S
            True
            sage: Set([1,4]) in S
            False
            sage: Set([]) in S
            True
            sage: 2 in S
            False
            sage: {1, 2} in S
            True
        """
    def cardinality(self):
        """
        Return the number of subsets of the set ``s``.

        This is given by `2^{|s|}`.

        EXAMPLES::

            sage: Subsets(Set([1,2,3])).cardinality()
            8
            sage: Subsets([1,2,3,3]).cardinality()
            8
            sage: Subsets(3).cardinality()
            8

        TESTS:

        ``__len__`` should return a Python int::

            sage: S = Subsets(Set([1,2,3]))
            sage: len(S)
            8
            sage: type(len(S)) is int
            True
        """
    __len__ = cardinality
    def first(self):
        """
        Return the first subset of ``s``. Since we aren't restricted to
        subsets of a certain size, this is always the empty set.

        EXAMPLES::

            sage: Subsets([1,2,3]).first()
            {}
            sage: Subsets(3).first()
            {}
        """
    def last(self):
        """
        Return the last subset of ``s``. Since we aren't restricted to
        subsets of a certain size, this is always the set ``s`` itself.

        EXAMPLES::

            sage: Subsets([1,2,3]).last()
            {1, 2, 3}
            sage: Subsets(3).last()
            {1, 2, 3}
        """
    def __iter__(self):
        """
        Iterate through the subsets of ``s``.

        EXAMPLES::

            sage: [sub for sub in Subsets(Set([1,2,3]))]
            [{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}]
            sage: [sub for sub in Subsets(3)]
            [{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}]
            sage: [sub for sub in Subsets([1,2,3,3])]
            [{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}]
        """
    def random_element(self):
        """
        Return a random element of the class of subsets of ``s`` (in other
        words, a random subset of ``s``).

        EXAMPLES::

            sage: Subsets(3).random_element()           # random
            {2}
            sage: Subsets([4,5,6]).random_element()     # random
            {5}

            sage: S = Subsets(Subsets(Subsets([0,1,2])))
            sage: S.cardinality()
            115792089237316195423570985008687907853269984665640564039457584007913129639936
            sage: s = S.random_element()
            sage: s     # random
            {{{1, 2}, {2}, {0}, {1}}, {{1, 2}, {0, 1, 2}, {0, 2}, {0}, {0, 1}}, ..., {{1, 2}, {2}, {1}}, {{2}, {0, 2}, {}, {1}}}
            sage: s in S
            True
        """
    def rank(self, sub):
        """
        Return the rank of ``sub`` as a subset of ``s``.

        EXAMPLES::

            sage: Subsets(3).rank([])
            0
            sage: Subsets(3).rank([1,2])
            4
            sage: Subsets(3).rank([1,2,3])
            7
            sage: Subsets(3).rank([2,3,4])
            Traceback (most recent call last):
            ...
            ValueError: {2, 3, 4} is not a subset of {1, 2, 3}
        """
    def unrank(self, r):
        """
        Return the subset of ``s`` that has rank ``k``.

        EXAMPLES::

            sage: Subsets(3).unrank(0)
            {}
            sage: Subsets([2,4,5]).unrank(1)
            {2}
            sage: Subsets([1,2,3]).unrank(257)
            Traceback (most recent call last):
            ...
            IndexError: index out of range
        """
    def __call__(self, el):
        """
        Workaround for returning non elements.

        See the extensive documentation in
        :meth:`sage.sets.finite_enumerated_set.FiniteEnumeratedSet.__call__`.

        TESTS::

            sage: sorted(Subsets(['a','b','c'])(['a','b']))  # indirect doctest
            ['a', 'b']
        """
    def lattice(self):
        """
        Return the lattice of subsets ordered by containment.

        EXAMPLES::

            sage: X = Subsets([7,8,9])
            sage: X.lattice()                                                           # needs sage.combinat sage.graphs
            Finite lattice containing 8 elements
            sage: Y = Subsets(0)
            sage: Y.lattice()                                                           # needs sage.combinat sage.graphs
            Finite lattice containing 1 elements
        """

class Subsets_sk(Subsets_s):
    """
    Subsets of fixed size of a set.

    EXAMPLES::

        sage: S = Subsets([0,1,2,5,7], 3); S
        Subsets of {0, 1, 2, 5, 7} of size 3
        sage: S.cardinality()
        10
        sage: S.first(), S.last()
        ({0, 1, 2}, {2, 5, 7})
        sage: S.random_element()  # random
        {0, 5, 7}
        sage: S([0,2,7])
        {0, 2, 7}
        sage: S([0,3,5])
        Traceback (most recent call last):
        ...
        ValueError: {0, 3, 5} not in Subsets of {0, 1, 2, 5, 7} of size 3
        sage: S([0])
        Traceback (most recent call last):
        ...
        ValueError: {0} not in Subsets of {0, 1, 2, 5, 7} of size 3
    """
    def __init__(self, s, k) -> None:
        '''
        TESTS::

            sage: s = Subsets(Set([1]))
            sage: e = s.first()
            sage: isinstance(e, s.element_class)
            True

        In the following "_test_elements" is temporarily disabled
        until :class:`sage.sets.set.Set_object_enumerated` objects
        pass the category tests::

            sage: S = Subsets(3,2)
            sage: TestSuite(S).run(skip=["_test_elements"])
        '''
    def __contains__(self, value) -> bool:
        """
        TESTS::

            sage: S = Subsets([1,2,3], 2)
            sage: Set([1,2]) in S
            True
            sage: Set([1,4]) in S
            False
            sage: Set([]) in S
            False
        """
    def __eq__(self, other):
        """
        Equality test.

        TESTS::

            sage: Subsets(5,3) == Subsets(5,3)
            True
            sage: Subsets(4,2) == Subsets(5,2) or Subsets(4,2) == Subsets(4,3)
            False
        """
    def __ne__(self, other):
        """
        Difference test.

        TESTS::

            sage: Subsets(5,3) != Subsets(5,3)
            False
            sage: Subsets(4,2) != Subsets(5,2) and Subsets(4,2) != Subsets(4,3)
            True
        """
    def __hash__(self):
        """
        Return the hash of ``self``.

        TESTS::

            sage: hash(Subsets(5,3)) == hash(Subsets(5,3))
            True
            sage: hash(Subsets(4,2)) == hash(Subsets(5,2))
            False
        """
    def cardinality(self):
        """
        EXAMPLES::

            sage: Subsets(Set([1,2,3]), 2).cardinality()
            3
            sage: Subsets([1,2,3,3], 2).cardinality()
            3
            sage: Subsets([1,2,3], 1).cardinality()
            3
            sage: Subsets([1,2,3], 3).cardinality()
            1
            sage: Subsets([1,2,3], 0).cardinality()
            1
            sage: Subsets([1,2,3], 4).cardinality()
            0
            sage: Subsets(3,2).cardinality()
            3
            sage: Subsets(3,4).cardinality()
            0
        """
    __len__ = cardinality
    def first(self):
        """
        Return the first subset of s of size k.

        EXAMPLES::

            sage: Subsets(Set([1,2,3]), 2).first()
            {1, 2}
            sage: Subsets([1,2,3,3], 2).first()
            {1, 2}
            sage: Subsets(3,2).first()
            {1, 2}
            sage: Subsets(3,4).first()
            Traceback (most recent call last):
            ...
            EmptySetError
        """
    def last(self):
        """
        Return the last subset of s of size k.

        EXAMPLES::

            sage: Subsets(Set([1,2,3]), 2).last()
            {2, 3}
            sage: Subsets([1,2,3,3], 2).last()
            {2, 3}
            sage: Subsets(3,2).last()
            {2, 3}
            sage: Subsets(3,4).last()
            Traceback (most recent call last):
            ...
            EmptySetError
        """
    def __iter__(self):
        """
        Iterate through the subsets of s of size k.

        EXAMPLES::

            sage: Subsets(Set([1,2,3]), 2).list()
            [{1, 2}, {1, 3}, {2, 3}]
            sage: Subsets([1,2,3,3], 2).list()
            [{1, 2}, {1, 3}, {2, 3}]
            sage: Subsets(3,2).list()
            [{1, 2}, {1, 3}, {2, 3}]
            sage: Subsets(3,3).list()
            [{1, 2, 3}]
        """
    def random_element(self):
        """
        Return a random element of the class of subsets of ``s`` of size
        ``k`` (in other words, a random subset of ``s`` of size ``k``).

        EXAMPLES::

            sage: s = Subsets(3, 2).random_element()
            sage: s in Subsets(3, 2)
            True

            sage: Subsets(3,4).random_element()
            Traceback (most recent call last):
            ...
            EmptySetError
        """
    def rank(self, sub):
        """
        Return the rank of ``sub`` as a subset of ``s`` of size ``k``.

        EXAMPLES::

            sage: Subsets(3,2).rank([1,2])
            0
            sage: Subsets([2,3,4],2).rank([3,4])
            2
            sage: Subsets([2,3,4],2).rank([2])
            Traceback (most recent call last):
            ...
            ValueError: {2} is not a subset of length 2 of {2, 3, 4}
            sage: Subsets([2,3,4],4).rank([2,3,4,5])
            Traceback (most recent call last):
            ...
            ValueError: {2, 3, 4, 5} is not a subset of length 4 of {2, 3, 4}
        """
    def unrank(self, r):
        """
        Return the subset of ``s`` of size ``k`` that has rank ``r``.

        EXAMPLES::

            sage: Subsets(3,2).unrank(0)
            {1, 2}
            sage: Subsets([2,4,5],2).unrank(0)
            {2, 4}
            sage: Subsets([1,2,8],3).unrank(42)
            Traceback (most recent call last):
            ...
            IndexError: index out of range
        """

def dict_to_list(d):
    """
    Return a list whose elements are the elements of ``i`` of ``d`` repeated with
    multiplicity ``d[i]``.

    EXAMPLES::

        sage: from sage.combinat.subset import dict_to_list
        sage: dict_to_list({'a':1, 'b':3})
        ['a', 'b', 'b', 'b']
    """
def list_to_dict(l):
    """
    Return a dictionary of multiplicities and the list of its keys.

    INPUT:

    - ``l`` -- list with possibly repeated elements

    The keys are the elements of ``l`` (in the same order in which they appear)
    and values are the multiplicities of each element in ``l``.

    EXAMPLES::

        sage: from sage.combinat.subset import list_to_dict
        sage: list_to_dict(['a', 'b', 'b', 'b'])
        ({'a': 1, 'b': 3}, ['a', 'b'])
    """

class SubMultiset_s(Parent):
    """
    The combinatorial class of the sub multisets of ``s``.

    EXAMPLES::

        sage: S = Subsets([1,2,2,3], submultiset=True)
        sage: S.cardinality()
        12
        sage: S.list()
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
        sage: S.first()
        []
        sage: S.last()
        [1, 2, 2, 3]
    """
    element_class = list
    def __init__(self, s) -> None:
        """
        Construct the combinatorial class of the sub multisets of s.

        EXAMPLES::

            sage: S = Subsets([1,2,2,3], submultiset=True)
            sage: Subsets([1,2,3,3], submultiset=True).cardinality()
            12
            sage: TestSuite(S).run()

        TESTS::

            sage: from sage.combinat.subset import SubMultiset_s
            sage: T = SubMultiset_s({'a':2,'b':1,'c':2})
            sage: T.cardinality()
            18
        """
    def __eq__(self, other):
        """
        TESTS::

            sage: Subsets([1,2,2,3], submultiset=True) == Subsets([1,2,2,3], submultiset=True)
            True
            sage: Subsets([1,2,2,3], submultiset=True) == Subsets([1,2,3,3], submultiset=True)
            False
        """
    def __ne__(self, other):
        """
        TESTS::

            sage: Subsets([1,2,2,3], submultiset=True) != Subsets([1,2,2,3], submultiset=True)
            False
            sage: Subsets([1,2,2,3], submultiset=True) != Subsets([1,2,3,3], submultiset=True)
            True
        """
    def __contains__(self, s) -> bool:
        """
        TESTS::

            sage: S = Subsets([1,2,2,3], submultiset=True)
            sage: [] in S
            True
            sage: [1, 2, 2] in S
            True
            sage: all(i in S for i in S)
            True
            sage: [1, 2, 2, 2] in S
            False
            sage: [1, 3, 2, 2] in S
            True
            sage: [4] in S
            False
        """
    def cardinality(self):
        """
        Return the cardinality of ``self``.

        EXAMPLES::

            sage: S = Subsets([1,1,2,3],submultiset=True)
            sage: S.cardinality()
            12
            sage: len(S.list())
            12

            sage: S = Subsets([1,1,2,2,3],submultiset=True)
            sage: S.cardinality()
            18
            sage: len(S.list())
            18

            sage: S = Subsets([1,1,1,2,2,3],submultiset=True)
            sage: S.cardinality()
            24
            sage: len(S.list())
            24
        """
    def random_element(self):
        """
        Return a random element of ``self`` with uniform law.

        EXAMPLES::

            sage: S = Subsets([1,1,2,3], submultiset=True)
            sage: s = S.random_element()
            sage: s in S
            True
        """
    def generating_serie(self, variable: str = 'x'):
        """
        Return the polynomial associated to the counting of the
        elements of ``self`` weighted by the number of element they contain.

        EXAMPLES::

            sage: Subsets([1,1],submultiset=True).generating_serie()
            x^2 + x + 1
            sage: Subsets([1,1,2,3],submultiset=True).generating_serie()
            x^4 + 3*x^3 + 4*x^2 + 3*x + 1
            sage: Subsets([1,1,1,2,2,3,3,4],submultiset=True).generating_serie()
            x^8 + 4*x^7 + 9*x^6 + 14*x^5 + 16*x^4 + 14*x^3 + 9*x^2 + 4*x + 1

            sage: S = Subsets([1,1,1,2,2,3,3,4],submultiset=True)
            sage: S.cardinality()
            72
            sage: sum(S.generating_serie())
            72
        """
    def __iter__(self):
        """
        Iterate through the subsets of ``self``.

        Note that each subset is represented by a list of its elements
        rather than a set since we can have multiplicities (no
        multiset data structure yet in sage).

        EXAMPLES::

            sage: S = Subsets([1,2,2,3], submultiset=True)
            sage: S.list()
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
        """
    def __call__(self, el):
        """
        Workaround for returning non elements.

        See the extensive documentation in
        :meth:`sage.sets.finite_enumerated_set.FiniteEnumeratedSet.__call__`.

        TESTS::

            sage: Subsets(['a','b','b','c'], submultiset=True)(['a','b'])  # indirect doctest
            ['a', 'b']
        """

class SubMultiset_sk(SubMultiset_s):
    """
    The combinatorial class of the subsets of size ``k`` of a multiset ``s``.  Note
    that each subset is represented by a list of the elements rather than a
    set since we can have multiplicities (no multiset data structure yet in
    sage).

    EXAMPLES::

        sage: S = Subsets([1,2,3,3],2,submultiset=True)
        sage: S._k
        2
        sage: S.cardinality()
        4
        sage: S.first()
        [1, 2]
        sage: S.last()
        [3, 3]
        sage: [sub for sub in S]
        [[1, 2], [1, 3], [2, 3], [3, 3]]
    """
    def __init__(self, s, k) -> None:
        """
        TESTS::

            sage: S = Subsets([1,2,3,3],2,submultiset=True)
            sage: [sub for sub in S]
            [[1, 2], [1, 3], [2, 3], [3, 3]]
            sage: TestSuite(S).run()
        """
    def __eq__(self, other):
        """
        TESTS::

            sage: Subsets([1,2,2,3], submultiset=True) == Subsets([1,2,2,3], submultiset=True)
            True
            sage: Subsets([1,2,2,3], submultiset=True) == Subsets([1,2,3,3], submultiset=True)
            False
        """
    def generating_serie(self, variable: str = 'x'):
        """
        Return the polynomial associated to the counting of the
        elements of ``self`` weighted by the number of elements they contains

        EXAMPLES::

            sage: x = ZZ['x'].gen()
            sage: l = [1,1,1,1,2,2,3]
            sage: for k in range(len(l)):
            ....:    S = Subsets(l,k,submultiset=True)
            ....:    print(S.generating_serie('x') == S.cardinality()*x**k)
            True
            True
            True
            True
            True
            True
            True
        """
    def cardinality(self):
        """
        Return the cardinality of ``self``.

        EXAMPLES::

            sage: S = Subsets([1,2,2,3,3,3],4,submultiset=True)
            sage: S.cardinality()
            5
            sage: len(list(S))
            5

            sage: S = Subsets([1,2,2,3,3,3],3,submultiset=True)
            sage: S.cardinality()
            6
            sage: len(list(S))
            6
        """
    def __contains__(self, s) -> bool:
        """
        TESTS::

            sage: S = Subsets([1,2,2,3], 2, submultiset=True)
            sage: [] in S
            False
            sage: [1, 2, 2] in S
            False
            sage: all(i in S for i in S)
            True
            sage: [2, 2] in S
            True
            sage: [1, 3] in S
            True
            sage: [4] in S
            False
            sage: [3, 3] in S
            False
        """
    def random_element(self):
        """
        Return a random submultiset of given length.

        EXAMPLES::

            sage: s = Subsets(7,3).random_element()
            sage: s in Subsets(7,3)
            True

            sage: s = Subsets(7,5).random_element()
            sage: s in Subsets(7,5)
            True
        """
    def __iter__(self):
        """
        Iterate through the subsets of size ``self._k`` of the multiset
        ``self._s``.

        Note that each subset is represented by a list of the
        elements rather than a set since we can have multiplicities (no
        multiset data structure yet in sage).

        EXAMPLES::

            sage: S = Subsets([1,2,2,3],2, submultiset=True)
            sage: S.list()
            [[1, 2], [1, 3], [2, 2], [2, 3]]

        Check that :issue:`28588` is fixed::

            sage: Subsets([3,2,2], submultiset=True).list()
            [[], [3], [2], [3, 2], [2, 2], [3, 2, 2]]
        """

class SubsetsSorted(Subsets_s):
    """
    Lightweight class of all subsets of some set `S`, with each
    subset being encoded as a sorted tuple.

    Used to model indices of algebras given by subsets (so we don't
    have to explicitly build all `2^n` subsets in memory).
    For example, :class:`CliffordAlgebra`.
    """
    element_class = tuple
    def __contains__(self, value) -> bool:
        """
        TESTS::

            sage: from sage.combinat.subset import SubsetsSorted
            sage: S = SubsetsSorted(range(3))
            sage: Set([1,2]) in S
            True
            sage: Set([1,4]) in S
            False
            sage: Set([]) in S
            True
            sage: (0,2) in S
            True
            sage: 2 in S
            False
        """
    def __iter__(self):
        """
        Iterate over ``self``.

        EXAMPLES::

            sage: from sage.combinat.subset import SubsetsSorted
            sage: S = SubsetsSorted(range(3))
            sage: [s for s in S]
            [(), (0,), (1,), (2,), (0, 1), (0, 2), (1, 2), (0, 1, 2)]
        """
    def first(self):
        """
        Return the first element of ``self``.

        EXAMPLES::

            sage: from sage.combinat.subset import SubsetsSorted
            sage: S = SubsetsSorted(range(3))
            sage: S.first()
            ()
        """
    def last(self):
        """
        Return the last element of ``self``.

        EXAMPLES::

            sage: from sage.combinat.subset import SubsetsSorted
            sage: S = SubsetsSorted(range(3))
            sage: S.last()
            (0, 1, 2)
        """
    def random_element(self):
        """
        Return a random element of ``self``.

        EXAMPLES::

            sage: from sage.combinat.subset import SubsetsSorted
            sage: S = SubsetsSorted(range(3))
            sage: isinstance(S.random_element(), tuple)
            True
        """
    def unrank(self, r):
        """
        Return the subset which has rank ``r``.

        EXAMPLES::

            sage: from sage.combinat.subset import SubsetsSorted
            sage: S = SubsetsSorted(range(3))
            sage: S.unrank(4)
            (0, 1)
        """

def powerset(X) -> Generator[Incomplete]:
    '''
    Iterator over the *list* of all subsets of the iterable ``X``, in no
    particular order. Each list appears exactly once, up to order.

    INPUT:

    - ``X`` -- an iterable

    OUTPUT: iterator of lists

    EXAMPLES::

        sage: list(powerset([1,2,3]))
        [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        sage: [z for z in powerset([0,[1,2]])]
        [[], [0], [[1, 2]], [0, [1, 2]]]

    Iterating over the power set of an infinite set is also allowed::

        sage: i = 0
        sage: L = []
        sage: for x in powerset(ZZ):
        ....:     if i > 10:
        ....:         break
        ....:     else:
        ....:         i += 1
        ....:     L.append(x)
        sage: print(" ".join(str(x) for x in L))
        [] [0] [1] [0, 1] [-1] [0, -1] [1, -1] [0, 1, -1] [2] [0, 2] [1, 2]

    You may also use subsets as an alias for powerset::

        sage: subsets([1,2,3])
        <generator object ...powerset at 0x...>
        sage: list(subsets([1,2,3]))
        [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

        The reason we return lists instead of sets is that the elements of
        sets must be hashable and many structures on which one wants the
        powerset consist of non-hashable objects.

    AUTHORS:

    - William Stein

    - Nils Bruin (2006-12-19): rewrite to work for not-necessarily
      finite objects X.
    '''
subsets = powerset

def uniq(L) -> Generator[Incomplete]:
    """
    Iterate over the elements of ``L``, yielding every element at most
    once: keep only the first occurrence of any item.

    The items must be hashable.

    INPUT:

    - ``L`` -- iterable

    EXAMPLES::

        sage: L = [1, 1, 8, -5, 3, -5, 'a', 'x', 'a']
        sage: it = uniq(L); it
        <generator object uniq at ...>
        sage: list(it)
        [1, 8, -5, 3, 'a', 'x']
    """
