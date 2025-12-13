from _typeshed import Incomplete
from sage.arith.misc import binomial as binomial
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.categories.infinite_enumerated_sets import InfiniteEnumeratedSets as InfiniteEnumeratedSets
from sage.combinat.enumeration_mod_permgroup import canonical_children as canonical_children, canonical_representative_of_orbit_of as canonical_representative_of_orbit_of, is_canonical as is_canonical, orbit as orbit
from sage.combinat.integer_vector import IntegerVectors as IntegerVectors
from sage.misc.misc_c import prod as prod
from sage.rings.integer import Integer as Integer
from sage.rings.power_series_ring import PowerSeriesRing as PowerSeriesRing
from sage.rings.rational_field import QQ as QQ
from sage.rings.semirings.non_negative_integer_semiring import NN as NN
from sage.sets.recursively_enumerated_set import RecursivelyEnumeratedSet_forest as RecursivelyEnumeratedSet_forest
from sage.structure.list_clone import ClonableIntArray as ClonableIntArray
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class IntegerVectorsModPermutationGroup(UniqueRepresentation):
    """
    Return an enumerated set containing integer vectors which are
    maximal in their orbit under the action of the permutation group
    ``G`` for the lexicographic order.

    In Sage, a permutation group `G` is viewed as a subgroup of the
    symmetric group `S_n` of degree `n` and `n` is said to be the degree
    of `G`.  Any integer vector `v` is said to be canonical if it
    is maximal in its orbit under the action of `G`. `v` is
    canonical if and only if

    .. MATH::

        v = \\max_{\\text{lex order}} \\{g \\cdot v | g \\in G \\}

    The action of `G` is on position. This means for example that the
    simple transposition `s_1 = (1, 2)` swaps the first and the second
    entries of any integer vector `v = [a_1, a_2, a_3, \\dots , a_n]`

    .. MATH::

        s_1 \\cdot v = [a_2, a_1, a_3, \\dots , a_n]

    This function returns a parent which contains, from each orbit
    orbit under the action of the permutation group `G`, a single
    canonical vector.  The canonical vector is the one that is maximal
    within the orbit according to lexicographic order.

    INPUT:

    - ``G`` -- a permutation group
    - ``sum`` -- (default: ``None``) - a nonnegative integer
    - ``max_part`` -- (default: ``None``) - a nonnegative integer setting the
      maximum value for every element
    - ``sgs`` -- (default: ``None``) - a strong generating system of the
      group `G`. If you do not provide it, it will be calculated at the
      creation of the parent

    OUTPUT:

    - If ``sum`` and ``max_part`` are None, it returns the infinite
      enumerated set of all integer vectors (lists of integers) maximal
      in their orbit for the lexicographic order.  Exceptionally, if
      the domain of ``G`` is empty, the result is a finite enumerated
      set that contains one element, namely the empty vector.

    - If ``sum`` is an integer, it returns a finite enumerated set
      containing all integer vectors maximal in their orbit for the
      lexicographic order and whose entries sum to ``sum``.

    EXAMPLES:

    Here is the set enumerating integer vectors modulo the action of the cyclic
    group of `3` elements::

        sage: I = IntegerVectorsModPermutationGroup(PermutationGroup([[(1,2,3)]]))
        sage: I.category()
        Category of infinite enumerated quotients of sets
        sage: I.cardinality()
        +Infinity
        sage: I.list()
        Traceback (most recent call last):
        ...
        NotImplementedError: cannot list an infinite set
        sage: p = iter(I)
        sage: for i in range(10): next(p)
        [0, 0, 0]
        [1, 0, 0]
        [2, 0, 0]
        [1, 1, 0]
        [3, 0, 0]
        [2, 1, 0]
        [2, 0, 1]
        [1, 1, 1]
        [4, 0, 0]
        [3, 1, 0]

    The method
    :meth:`~sage.combinat.integer_vectors_mod_permgroup.IntegerVectorsModPermutationGroup_All.is_canonical`
    tests if an integer vector is maximal in its orbit. This method
    is also used in the containment test::

        sage: I = IntegerVectorsModPermutationGroup(PermutationGroup([[(1,2,3,4)]]))
        sage: I.is_canonical([5,2,0,4])
        True
        sage: I.is_canonical([5,0,6,4])
        False
        sage: I.is_canonical([1,1,1,1])
        True
        sage: [2,3,1,0] in I
        False
        sage: [5,0,5,0] in I
        True
        sage: 'Bla' in I
        False
        sage: I.is_canonical('bla')
        Traceback (most recent call last):
        ...
        AssertionError: bla should be a list or an integer vector

    If you give a value to the extra argument ``sum``, the set returned
    will be a finite set containing only canonical vectors whose entries
    sum to ``sum``.::

        sage: I = IntegerVectorsModPermutationGroup(PermutationGroup([[(1,2,3)]]), sum=6)
        sage: I.cardinality()
        10
        sage: I.list()
        [[6, 0, 0], [5, 1, 0], [5, 0, 1], [4, 2, 0], [4, 1, 1],
         [4, 0, 2], [3, 3, 0], [3, 2, 1], [3, 1, 2], [2, 2, 2]]
        sage: I.category()
        Join of Category of finite enumerated sets
            and Category of subquotients of finite sets
            and Category of quotients of sets

    To get the orbit of any integer vector `v` under the action of the group,
    use the method :meth:`~sage.combinat.integer_vectors_mod_permgroup.IntegerVectorsModPermutationGroup_All.orbit`;
    we convert the returned set of vectors into a list in increasing lexicographic order,
    to get a reproducible test::

        sage: sorted(I.orbit([6,0,0]))
        [[0, 0, 6], [0, 6, 0], [6, 0, 0]]
        sage: sorted(I.orbit([5,1,0]))
        [[0, 5, 1], [1, 0, 5], [5, 1, 0]]
        sage: I.orbit([2,2,2])
        {[2, 2, 2]}

    Even without constraints, for an empty domain the result is
    a singleton set::

        sage: G = PermutationGroup([], domain=[])
        sage: sgs = tuple(tuple(s) for s in G.strong_generating_system())
        sage: list(IntegerVectorsModPermutationGroup(G, sgs=sgs))
        [[]]


    .. WARNING::

        Because of :issue:`36527`, permutation groups that have
        different domains but similar generators can be erroneously
        treated as the same group.  This will silently produce
        erroneous results.  To avoid this issue, compute a strong
        generating system for the group as::

            sgs = tuple(tuple(s) for s in G.strong_generating_system())

        and provide it as the optional ``sgs`` argument to the
        constructor.

    TESTS:

    Let us check that canonical integer vectors of the symmetric group
    are just nonincreasing lists of integers::

        sage: I = IntegerVectorsModPermutationGroup(SymmetricGroup(5))  # long time
        sage: p = iter(I)                                               # long time
        sage: for i in range(100):                                      # long time
        ....:     v = list(next(p))
        ....:     assert sorted(v, reverse=True) == v

    We now check that there are as many canonical vectors under the
    symmetric group `S_n` whose entries sum to `d` as there are
    partitions of `d` of at most `n` parts::

        sage: I = IntegerVectorsModPermutationGroup(SymmetricGroup(5))  # long time
        sage: for i in range(10):                                       # long time
        ....:     d1 = I.subset(i).cardinality()
        ....:     d2 = Partitions(i, max_length=5).cardinality()
        ....:     print(d1)
        ....:     assert d1 == d2
        1
        1
        2
        3
        5
        7
        10
        13
        18
        23

    Another corner case is trivial groups. For the trivial group ``G``
    acting on a list of length `n`, all integer vectors of length `n`
    are canonical::

        sage: # long time
        sage: G = PermutationGroup([[(6,)]])
        sage: G.cardinality()
        1
        sage: sgs = tuple(tuple(s) for s in G.strong_generating_system())
        sage: I = IntegerVectorsModPermutationGroup(G, sgs=sgs)
        sage: for i in range(10):
        ....:     d1 = I.subset(i).cardinality()
        ....:     d2 = IntegerVectors(i,6).cardinality()
        ....:     print(d1)
        ....:     assert d1 == d2
        1
        6
        21
        56
        126
        252
        462
        792
        1287
        2002
    """
    @staticmethod
    def __classcall__(cls, G, sum=None, max_part=None, sgs=None):
        """
        TESTS::

            sage: I = IntegerVectorsModPermutationGroup(PermutationGroup([[(1,2,3)]]))
            sage: I = IntegerVectorsModPermutationGroup(PermutationGroup([[(1,2,3)]]), None)
            sage: I = IntegerVectorsModPermutationGroup(PermutationGroup([[(1,2,3)]]), 2)
            sage: I = IntegerVectorsModPermutationGroup(PermutationGroup([[(1,2,3)]]), -2)
            Traceback (most recent call last):
            ...
            ValueError: Value -2 in not in Non negative integer semiring.
            sage: I = IntegerVectorsModPermutationGroup(PermutationGroup([[(1,2,3)]]), 8, max_part=5)
        """

class IntegerVectorsModPermutationGroup_All(UniqueRepresentation, RecursivelyEnumeratedSet_forest):
    """
    A class for integer vectors enumerated up to the action of a
    permutation group.

    A Sage permutation group is viewed as a subgroup of the symmetric
    group `S_n` for a certain `n`. This group has a natural action by
    position on vectors of length `n`. This class implements a set
    which keeps a single vector for each orbit. We say that a vector
    is canonical if it is the maximum in its orbit under the action of
    the permutation group for the lexicographic order.

    EXAMPLES::

        sage: I = IntegerVectorsModPermutationGroup(PermutationGroup([[(1,2,3,4)]])); I
        Integer vectors of length 4 enumerated up to the action of
         Permutation Group with generators [(1,2,3,4)]
        sage: I.cardinality()
        +Infinity
        sage: TestSuite(I).run()
        sage: it = iter(I)
        sage: [next(it), next(it), next(it), next(it), next(it)]
        [[0, 0, 0, 0],
         [1, 0, 0, 0],
         [2, 0, 0, 0],
         [1, 1, 0, 0],
         [1, 0, 1, 0]]
        sage: x = next(it); x
        [3, 0, 0, 0]
        sage: I.first()
        [0, 0, 0, 0]

    TESTS::

        sage: TestSuite(I).run()
    """
    n: Incomplete
    def __init__(self, G, sgs=None) -> None:
        """
        TESTS::

            sage: I = IntegerVectorsModPermutationGroup(PermutationGroup([[(1,2,3,4)]]))
            sage: I
            Integer vectors of length 4 enumerated up to the action of
             Permutation Group with generators [(1,2,3,4)]
            sage: I.category()
            Category of infinite enumerated quotients of sets
            sage: TestSuite(I).run()
        """
    def ambient(self):
        """
        Return the ambient space from which ``self`` is a quotient.

        EXAMPLES::

            sage: S = IntegerVectorsModPermutationGroup(PermutationGroup([[(1,2,3,4)]]))
            sage: S.ambient()
            Integer vectors of length 4
        """
    def lift(self, elt):
        """
        Lift the element ``elt`` inside the ambient space from which ``self`` is a quotient.

        EXAMPLES::

            sage: S = IntegerVectorsModPermutationGroup(PermutationGroup([[(1,2,3,4)]]))
            sage: v = S.lift(S([4,3,0,1])); v
            [4, 3, 0, 1]
            sage: type(v)
            <class 'list'>
        """
    def retract(self, elt):
        """
        Return the canonical representative of the orbit of the
        integer ``elt`` under the action of the permutation group
        defining ``self``.

        If the element ``elt`` is already maximal in its orbit for
        the lexicographic order, ``elt`` is thus the good
        representative for its orbit.

        EXAMPLES::

            sage: [0,0,0,0] in IntegerVectors(0,4)
            True
            sage: [1,0,0,0] in IntegerVectors(1,4)
            True
            sage: [0,1,0,0] in IntegerVectors(1,4)
            True
            sage: [1,0,1,0] in IntegerVectors(2,4)
            True
            sage: [0,1,0,1] in IntegerVectors(2,4)
            True
            sage: S = IntegerVectorsModPermutationGroup(PermutationGroup([[(1,2,3,4)]]))
            sage: S.retract([0,0,0,0])
            [0, 0, 0, 0]
            sage: S.retract([1,0,0,0])
            [1, 0, 0, 0]
            sage: S.retract([0,1,0,0])
            [1, 0, 0, 0]
            sage: S.retract([1,0,1,0])
            [1, 0, 1, 0]
            sage: S.retract([0,1,0,1])
            [1, 0, 1, 0]
        """
    def roots(self):
        """
        Return the root of generation of ``self``. This method is
        required to build the tree structure of ``self`` which
        inherits from the class :class:`~sage.sets.recursively_enumerated_set.RecursivelyEnumeratedSet_forest`.

        EXAMPLES::

            sage: I = IntegerVectorsModPermutationGroup(PermutationGroup([[(1,2,3,4)]]))
            sage: I.roots()
            [[0, 0, 0, 0]]
        """
    def children(self, x):
        """
        Return the list of children of the element ``x``. This method
        is required to build the tree structure of ``self`` which
        inherits from the class :class:`~sage.sets.recursively_enumerated_set.RecursivelyEnumeratedSet_forest`.

        EXAMPLES::

            sage: I = IntegerVectorsModPermutationGroup(PermutationGroup([[(1,2,3,4)]]))
            sage: I.children(I([2,1,0,0], check=False))
            [[2, 2, 0, 0], [2, 1, 1, 0], [2, 1, 0, 1]]
        """
    def permutation_group(self):
        """
        Return the permutation group given to define ``self``.

        EXAMPLES::

            sage: I = IntegerVectorsModPermutationGroup(PermutationGroup([[(1,2,3,4)]]))
            sage: I.permutation_group()
            Permutation Group with generators [(1,2,3,4)]
        """
    def is_canonical(self, v, check: bool = True):
        """
        Return ``True`` if the integer list ``v`` is maximal in its
        orbit under the action of the permutation group given to
        define ``self``.  Such integer vectors are said to be
        canonical. A vector `v` is canonical if and only if

        .. MATH::

            v = \\max_{\\text{lex order}} \\{g \\cdot v | g \\in G \\}

        EXAMPLES::

            sage: I = IntegerVectorsModPermutationGroup(PermutationGroup([[(1,2,3,4)]]))
            sage: I.is_canonical([4,3,2,1])
            True
            sage: I.is_canonical([4,0,0,1])
            True
            sage: I.is_canonical([4,0,3,3])
            True
            sage: I.is_canonical([4,0,4,4])
            False
        """
    def __contains__(self, v) -> bool:
        """
        EXAMPLES::

            sage: I = IntegerVectorsModPermutationGroup(PermutationGroup([[(1,2,3,4)]]))
            sage: [2,2,0,0] in I
            True
            sage: [2,0,1,0] in I
            True
            sage: [2,0,0,1] in I
            True
            sage: [2,0,0,2] in I
            False
            sage: [2,0,0,2,12] in I
            False
        """
    def __call__(self, v, check: bool = True):
        """
        Return an element of ``self`` constructed from ``v`` if
        possible.

        TESTS::

            sage: I = IntegerVectorsModPermutationGroup(PermutationGroup([[(1,2,3,4)]]))
            sage: I([3,2,1,0])
            [3, 2, 1, 0]
        """
    def orbit(self, v):
        """
        Return the orbit of the integer vector ``v`` under the action of the
        permutation group defining ``self``. The result is a set.

        EXAMPLES:

        In order to get reproducible doctests, we convert the returned sets
        into lists in increasing lexicographic order::

            sage: I = IntegerVectorsModPermutationGroup(PermutationGroup([[(1,2,3,4)]]))
            sage: sorted(I.orbit([2,2,0,0]))
            [[0, 0, 2, 2], [0, 2, 2, 0], [2, 0, 0, 2], [2, 2, 0, 0]]
            sage: sorted(I.orbit([2,1,0,0]))
            [[0, 0, 2, 1], [0, 2, 1, 0], [1, 0, 0, 2], [2, 1, 0, 0]]
            sage: sorted(I.orbit([2,0,1,0]))
            [[0, 1, 0, 2], [0, 2, 0, 1], [1, 0, 2, 0], [2, 0, 1, 0]]
            sage: sorted(I.orbit([2,0,2,0]))
            [[0, 2, 0, 2], [2, 0, 2, 0]]
            sage: I.orbit([1,1,1,1])
            {[1, 1, 1, 1]}
        """
    def subset(self, sum=None, max_part=None):
        """
        Return the subset of ``self`` containing integer vectors
        whose entries sum to ``sum``.

        EXAMPLES::

            sage: S = IntegerVectorsModPermutationGroup(PermutationGroup([[(1,2,3,4)]]))
            sage: S.subset(4)
            Integer vectors of length 4 and of sum 4 enumerated up to
            the action of Permutation Group with generators
            [(1,2,3,4)]
        """
    class Element(ClonableIntArray):
        """
        Element class for the set of integer vectors of given sum enumerated modulo
        the action of a permutation group. These vectors are clonable lists of integers
        which must satisfy conditions coming from the parent appearing in the method
        :meth:`~sage.structure.list_clone.ClonableIntArray.check`.

        TESTS::

            sage: I = IntegerVectorsModPermutationGroup(PermutationGroup([[(1,2,3,4)]]))
            sage: v = I.element_class(I, [4,3,2,1]); v
            [4, 3, 2, 1]
            sage: TestSuite(v).run()
            sage: I.element_class(I, [4,3,2,5])
            Traceback (most recent call last):
            ...
            AssertionError
        """
        def check(self) -> None:
            """
            Check that ``self`` verify the invariants needed for
            living in ``self.parent()``.

            EXAMPLES::

                sage: I = IntegerVectorsModPermutationGroup(PermutationGroup([[(1,2,3,4)]]))
                sage: v = I.an_element()
                sage: v.check()
                sage: w = I([0,4,0,0], check=False); w
                [0, 4, 0, 0]
                sage: w.check()
                Traceback (most recent call last):
                ...
                AssertionError
            """

class IntegerVectorsModPermutationGroup_with_constraints(UniqueRepresentation, RecursivelyEnumeratedSet_forest):
    """
    This class models finite enumerated sets of integer vectors with
    constraint enumerated up to the action of a permutation group.
    Integer vectors are enumerated modulo the action of the
    permutation group. To implement that, we keep a single integer
    vector by orbit under the action of the permutation
    group. Elements chosen are vectors maximal in their orbit for the
    lexicographic order.

    For more information see :class:`IntegerVectorsModPermutationGroup`.

    EXAMPLES::

        sage: I = IntegerVectorsModPermutationGroup(PermutationGroup([[(1,2,3,4)]]),
        ....:                                       max_part=1)
        sage: I.list()
        [[0, 0, 0, 0], [1, 0, 0, 0], [1, 1, 0, 0], [1, 0, 1, 0], [1, 1, 1, 0],
         [1, 1, 1, 1]]
        sage: I = IntegerVectorsModPermutationGroup(PermutationGroup([[(1,2,3,4)]]),
        ....:                                       sum=6, max_part=4)
        sage: I.list()
        [[4, 2, 0, 0], [4, 1, 1, 0], [4, 1, 0, 1], [4, 0, 2, 0], [4, 0, 1, 1],
         [4, 0, 0, 2], [3, 3, 0, 0], [3, 2, 1, 0], [3, 2, 0, 1], [3, 1, 2, 0],
         [3, 1, 1, 1], [3, 1, 0, 2], [3, 0, 3, 0], [3, 0, 2, 1], [3, 0, 1, 2],
         [2, 2, 2, 0], [2, 2, 1, 1], [2, 1, 2, 1]]

    Here is the enumeration of unlabeled graphs over 5 vertices::

        sage: G = IntegerVectorsModPermutationGroup(TransitiveGroup(10,12), max_part=1)
        sage: G.cardinality()
        34

    TESTS::

        sage: I = IntegerVectorsModPermutationGroup(PermutationGroup([[(1,2,3,4)]]),4)
        sage: TestSuite(I).run()
    """
    n: Incomplete
    def __init__(self, G, d, max_part, sgs=None) -> None:
        """
        TESTS::

            sage: I = IntegerVectorsModPermutationGroup(PermutationGroup([[(1,2,3,4)]]), 6, max_part=4)
        """
    def roots(self):
        """
        Return the root of generation of ``self``.

        This method is
        required to build the tree structure of ``self`` which
        inherits from the class
        :class:`~sage.sets.recursively_enumerated_set.RecursivelyEnumeratedSet_forest`.

        EXAMPLES::

            sage: I = IntegerVectorsModPermutationGroup(PermutationGroup([[(1,2,3,4)]]))
            sage: I.roots()
            [[0, 0, 0, 0]]
        """
    def children(self, x):
        """
        Return the list of children of the element ``x``.

        This method
        is required to build the tree structure of ``self`` which
        inherits from the class
        :class:`~sage.sets.recursively_enumerated_set.RecursivelyEnumeratedSet_forest`.

        EXAMPLES::

            sage: I = IntegerVectorsModPermutationGroup(PermutationGroup([[(1,2,3,4)]]))
            sage: I.children(I([2,1,0,0], check=False))
            [[2, 2, 0, 0], [2, 1, 1, 0], [2, 1, 0, 1]]
        """
    def permutation_group(self):
        """
        Return the permutation group given to define ``self``.

        EXAMPLES::

            sage: I = IntegerVectorsModPermutationGroup(PermutationGroup([[(1,2,3)]]), 5)
            sage: I.permutation_group()
            Permutation Group with generators [(1,2,3)]
        """
    def __contains__(self, v) -> bool:
        """
        TESTS::

            sage: I = IntegerVectorsModPermutationGroup(PermutationGroup([[(1,2,3,4)]]),6)
            sage: [6,0,0,0] in I
            True
            sage: [5,0,1,0] in I
            True
            sage: [0,5,1,0] in I
            False
            sage: [3,0,1,3] in I
            False
            sage: [3,3,1,0] in I
            False
        """
    def __call__(self, v, check: bool = True):
        """
        Make `v` an element living in ``self``.

        TESTS::

            sage: I = IntegerVectorsModPermutationGroup(PermutationGroup([[(1,2,3,4)]]), 4)
            sage: v = I([2,1,0,1]); v
            [2, 1, 0, 1]
            sage: v.parent()
            Integer vectors of length 4 and of sum 4 enumerated up to
            the action of Permutation Group with generators
            [(1,2,3,4)]
        """
    def __iter__(self):
        """
        TESTS::

            sage: I = IntegerVectorsModPermutationGroup(PermutationGroup([[(1,2,3,4)]]),4)
            sage: for i in I: i
            [4, 0, 0, 0]
            [3, 1, 0, 0]
            [3, 0, 1, 0]
            [3, 0, 0, 1]
            [2, 2, 0, 0]
            [2, 1, 1, 0]
            [2, 1, 0, 1]
            [2, 0, 2, 0]
            [2, 0, 1, 1]
            [1, 1, 1, 1]

            sage: I = IntegerVectorsModPermutationGroup(PermutationGroup([[(1,2,3,4)]]), sum=7, max_part=3)
            sage: for i in I: i
            [3, 3, 1, 0]
            [3, 3, 0, 1]
            [3, 2, 2, 0]
            [3, 2, 1, 1]
            [3, 2, 0, 2]
            [3, 1, 3, 0]
            [3, 1, 2, 1]
            [3, 1, 1, 2]
            [3, 0, 2, 2]
            [2, 2, 2, 1]

        Check that :issue:`36681` is fixed::

            sage: G = PermutationGroup([], domain=[])
            sage: I = IntegerVectorsModPermutationGroup(G, sum=0)
            sage: list(iter(I))
            [[]]

        Check that :issue:`36681` is fixed::

            sage: G = PermutationGroup([], domain=[])
            sage: I = IntegerVectorsModPermutationGroup(G, sum=3)
            sage: list(iter(I))
            []
        """
    def cardinality(self):
        """
        Return the number of integer vectors in the set.

        The algorithm utilises :wikipedia:`Cycle Index Theorem <Cycle_index>`, allowing
        for a faster than a plain enumeration computation.

        EXAMPLES:

        With a trivial group all vectors are canonical::

            sage: G = PermutationGroup([], domain=[1,2,3])
            sage: IntegerVectorsModPermutationGroup(G, 5).cardinality()
            21
            sage: IntegerVectors(5, 3).cardinality()
            21

        With two interchangeable elements, the smaller one
        ranges from zero to ``sum//2``::

            sage: G = PermutationGroup([(1,2)])
            sage: IntegerVectorsModPermutationGroup(G, 1000).cardinality()
            501

        Binary vectors up to full symmetry are first some ones and
        then some zeros::

            sage: G = SymmetricGroup(10)
            sage: I = IntegerVectorsModPermutationGroup(G, max_part=1)
            sage: I.cardinality()
            11

        Binary vectors of constant weight, up to PGL(2,17), which
        is 3-transitive, but not 4-transitive::

            sage: G=PGL(2,17)
            sage: I = IntegerVectorsModPermutationGroup(G, sum=3, max_part=1)
            sage: I.cardinality()
            1
            sage: I = IntegerVectorsModPermutationGroup(G, sum=4, max_part=1)
            sage: I.cardinality()
            3

        TESTS:

        Check that :issue:`36681` is fixed::

            sage: G = PermutationGroup([], domain=[])
            sage: sgs = tuple(tuple(t) for t in G.strong_generating_system())
            sage: V = IntegerVectorsModPermutationGroup(G, sum=1, sgs=sgs)
            sage: V.cardinality()
            0

        The case when both ``sum`` and ``max_part`` are specified::

            sage: G = PermutationGroup([(1,2,3)])
            sage: I = IntegerVectorsModPermutationGroup(G, sum=10, max_part=5)
            sage: I.cardinality()
            7

        All permutation groups of degree 4::

            sage: for G in SymmetricGroup(4).subgroups():
            ....:     sgs = tuple(tuple(t) for t in G.strong_generating_system())
            ....:     I1 = IntegerVectorsModPermutationGroup(G, sum=10, sgs=sgs)
            ....:     assert I1.cardinality() == len(list(I1))
            ....:     I2 = IntegerVectorsModPermutationGroup(G, max_part=3, sgs=sgs)
            ....:     assert I2.cardinality() == len(list(I2))
            ....:     I3 = IntegerVectorsModPermutationGroup(G, sum=10, max_part=3, sgs=sgs)
            ....:     assert I3.cardinality() == len(list(I3))

        Symmetric group with sums 0 and 1::

            sage: S10 = SymmetricGroup(10)
            sage: IntegerVectorsModPermutationGroup(S10, 0).cardinality()
            1
            sage: IntegerVectorsModPermutationGroup(S10, 1).cardinality()
            1

        Trivial group with sums 1 and 100::

            sage: T10 = PermutationGroup([], domain=range(1, 11))
            sage: IntegerVectorsModPermutationGroup(T10, 1).cardinality()
            10
            sage: IntegerVectorsModPermutationGroup(T10, 100).cardinality()
            4263421511271
        """
    def is_canonical(self, v, check: bool = True):
        """
        Return ``True`` if the integer list ``v`` is maximal in its
        orbit under the action of the permutation group given to
        define ``self``.  Such integer vectors are said to be
        canonical. A vector `v` is canonical if and only if

        .. MATH::

            v = \\max_{\\text{lex order}} \\{g \\cdot v | g \\in G \\}

        EXAMPLES::

            sage: I = IntegerVectorsModPermutationGroup(PermutationGroup([[(1,2,3,4)]]),
            ....:                                       max_part=3)
            sage: I.is_canonical([3,0,0,0])
            True
            sage: I.is_canonical([1,0,2,0])
            False
            sage: I.is_canonical([2,0,1,0])
            True
        """
    def ambient(self):
        """
        Return the ambient space from which ``self`` is a quotient.

        EXAMPLES::

            sage: S = IntegerVectorsModPermutationGroup(PermutationGroup([[(1,2,3,4)]]), 6)
            sage: S.ambient()
            Integer vectors that sum to 6
            sage: S = IntegerVectorsModPermutationGroup(PermutationGroup([[(1,2,3,4)]]),
            ....:                                       6, max_part=12)
            sage: S.ambient()
            Integer vectors that sum to 6 with constraints: max_part=12
            sage: S = IntegerVectorsModPermutationGroup(PermutationGroup([[(1,2,3,4)]]),
            ....:                                       max_part=12)
            sage: S.ambient()
            Integer vectors with constraints: max_part=12
        """
    def lift(self, elt):
        """
        Lift the element ``elt`` inside the ambient space from which ``self`` is a quotient.

        EXAMPLES::

            sage: S = IntegerVectorsModPermutationGroup(PermutationGroup([[(1,2,3,4)]]),
            ....:                                       max_part=1)
            sage: v = S.lift([1,0,1,0]); v
            [1, 0, 1, 0]
            sage: v in IntegerVectors(2,4,max_part=1)
            True
            sage: S = IntegerVectorsModPermutationGroup(PermutationGroup([[(1,2,3,4)]]),
            ....:                                       sum=6)
            sage: v = S.lift(S.list()[5]); v
            [4, 1, 1, 0]
            sage: v in IntegerVectors(n=6)
            True
        """
    def retract(self, elt):
        """
        Return the canonical representative of the orbit of the
        integer ``elt`` under the action of the permutation group
        defining ``self``.

        If the element ``elt`` is already maximal in its orbits for
        the lexicographic order, ``elt`` is thus the good
        representative for its orbit.

        EXAMPLES::

            sage: S = IntegerVectorsModPermutationGroup(PermutationGroup([[(1,2,3,4)]]),
            ....:                                       sum=2, max_part=1)
            sage: S.retract([1,1,0,0])
            [1, 1, 0, 0]
            sage: S.retract([1,0,1,0])
            [1, 0, 1, 0]
            sage: S.retract([1,0,0,1])
            [1, 1, 0, 0]
            sage: S.retract([0,1,1,0])
            [1, 1, 0, 0]
            sage: S.retract([0,1,0,1])
            [1, 0, 1, 0]
            sage: S.retract([0,0,1,1])
            [1, 1, 0, 0]
        """
    def orbit(self, v):
        """
        Return the orbit of the vector ``v`` under the action of the
        permutation group defining ``self``. The result is a set.

        INPUT:

        - ``v`` -- an element of ``self`` or any list of length the
          degree of the permutation group

        EXAMPLES:

        We convert the result in a list in increasing lexicographic
        order, to get a reproducible doctest::

            sage: I = IntegerVectorsModPermutationGroup(PermutationGroup([[(1,2,3,4)]]), 4)
            sage: I.orbit([1,1,1,1])
            {[1, 1, 1, 1]}
            sage: sorted(I.orbit([3,0,0,1]))
            [[0, 0, 1, 3], [0, 1, 3, 0], [1, 3, 0, 0], [3, 0, 0, 1]]
        """
    class Element(ClonableIntArray):
        """
        Element class for the set of integer vectors with constraints enumerated
        modulo the action of a permutation group. These vectors are clonable lists
        of integers which must satisfy conditions coming from the parent as in
        the method :meth:`~sage.combinat.integer_vectors_mod_permgroup.IntegerVectorsModPermutationGroup_with_constraints.Element.check`.

        TESTS::

            sage: I = IntegerVectorsModPermutationGroup(PermutationGroup([[(1,2,3,4)]]), 4)
            sage: v = I.element_class(I, [3,1,0,0]); v
            [3, 1, 0, 0]
            sage: TestSuite(v).run()
            sage: v = I.element_class(I, [3,2,0,0])
            Traceback (most recent call last):
            ...
            AssertionError: [3, 2, 0, 0] should be an integer vector of sum 4
        """
        def check(self) -> None:
            """
            Check that ``self`` meets the constraints of being an element of ``self.parent()``.

            EXAMPLES::

                sage: I = IntegerVectorsModPermutationGroup(PermutationGroup([[(1,2,3,4)]]), 4)
                sage: v = I.an_element()
                sage: v.check()
                sage: w = I([0,4,0,0], check=False); w
                [0, 4, 0, 0]
                sage: w.check()
                Traceback (most recent call last):
                ...
                AssertionError
            """
