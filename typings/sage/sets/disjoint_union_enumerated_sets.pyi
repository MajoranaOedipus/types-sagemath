from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.categories.infinite_enumerated_sets import InfiniteEnumeratedSets as InfiniteEnumeratedSets
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.rings.infinity import Infinity as Infinity
from sage.sets.family import Family as Family
from sage.structure.element import Element as Element
from sage.structure.element_wrapper import ElementWrapper as ElementWrapper
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class DisjointUnionEnumeratedSets(UniqueRepresentation, Parent):
    """
    A class for disjoint unions of enumerated sets.

    INPUT:

    - ``family`` -- list (or iterable or family) of enumerated sets
    - ``keepkey`` -- boolean
    - ``facade`` -- boolean

    This models the enumerated set obtained by concatenating together
    the specified ordered sets. The latter are supposed to be pairwise
    disjoint; otherwise, a multiset is created.

    The argument ``family`` can be a list, a tuple, a dictionary, or a
    family. If it is not a family it is first converted into a family
    (see :func:`sage.sets.family.Family`).

    Experimental options:

    By default, there is no way to tell from which set of the union an
    element is generated. The option ``keepkey=True`` keeps track of
    those by returning pairs ``(key, el)`` where ``key`` is the index
    of the set to which ``el`` belongs. When this option is specified,
    the enumerated sets need not be disjoint anymore.

    With the option ``facade=False`` the elements are wrapped in an
    object whose parent is the disjoint union itself. The wrapped
    object can then be recovered using the ``value`` attribute.

    The two options can be combined.

    The names of those options is imperfect, and subject to change in
    future versions. Feedback welcome.

    EXAMPLES:

    The input can be a list or a tuple of FiniteEnumeratedSets::

        sage: U1 = DisjointUnionEnumeratedSets((
        ....:       FiniteEnumeratedSet([1,2,3]),
        ....:       FiniteEnumeratedSet([4,5,6])))
        sage: U1
        Disjoint union of Family ({1, 2, 3}, {4, 5, 6})
        sage: U1.list()
        [1, 2, 3, 4, 5, 6]
        sage: U1.cardinality()
        6

    The input can also be a dictionary::

        sage: U2 = DisjointUnionEnumeratedSets({1: FiniteEnumeratedSet([1,2,3]),
        ....:                                   2: FiniteEnumeratedSet([4,5,6])})
        sage: U2
        Disjoint union of Finite family {1: {1, 2, 3}, 2: {4, 5, 6}}
        sage: U2.list()
        [1, 2, 3, 4, 5, 6]
        sage: U2.cardinality()
        6

    However in that case the enumeration order is not specified.

    In general the input can be any family::

        sage: # needs sage.combinat
        sage: U3 = DisjointUnionEnumeratedSets(
        ....:     Family([2,3,4], Permutations, lazy=True))
        sage: U3
        Disjoint union of Lazy family
         (<class 'sage.combinat.permutation.Permutations'>(i))_{i in [2, 3, 4]}
        sage: U3.cardinality()
        32
        sage: it = iter(U3)
        sage: [next(it), next(it), next(it), next(it), next(it), next(it)]
        [[1, 2], [2, 1], [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]]
        sage: U3.unrank(18)
        [2, 4, 1, 3]

    This allows for infinite unions::

        sage: # needs sage.combinat
        sage: U4 = DisjointUnionEnumeratedSets(
        ....:     Family(NonNegativeIntegers(), Permutations))
        sage: U4
        Disjoint union of Lazy family
         (<class 'sage.combinat.permutation.Permutations'>(i))_{i in Non negative integers}
        sage: U4.cardinality()
        +Infinity
        sage: it = iter(U4)
        sage: [next(it), next(it), next(it), next(it), next(it), next(it)]
        [[], [1], [1, 2], [2, 1], [1, 2, 3], [1, 3, 2]]
        sage: U4.unrank(18)
        [2, 3, 1, 4]

    .. WARNING::

        Beware that some of the operations assume in that case that infinitely
        many of the enumerated sets are non empty.


    .. RUBRIC:: Experimental options

    We demonstrate the ``keepkey`` option::

        sage: # needs sage.combinat
        sage: Ukeep = DisjointUnionEnumeratedSets(
        ....:            Family(list(range(4)), Permutations), keepkey=True)
        sage: it = iter(Ukeep)
        sage: [next(it) for i in range(6)]
        [(0, []), (1, [1]), (2, [1, 2]), (2, [2, 1]), (3, [1, 2, 3]), (3, [1, 3, 2])]
        sage: type(next(it)[1])
        <class 'sage.combinat.permutation.StandardPermutations_n_with_category.element_class'>

    We now demonstrate the ``facade`` option::

        sage: # needs sage.combinat
        sage: UNoFacade = DisjointUnionEnumeratedSets(
        ....:                Family(list(range(4)), Permutations), facade=False)
        sage: it = iter(UNoFacade)
        sage: [next(it) for i in range(6)]
        [[], [1], [1, 2], [2, 1], [1, 2, 3], [1, 3, 2]]
        sage: el = next(it); el
        [2, 1, 3]
        sage: type(el)
        <... 'sage.structure.element_wrapper.ElementWrapper'>
        sage: el.parent() == UNoFacade
        True
        sage: elv = el.value; elv
        [2, 1, 3]
        sage: type(elv)
        <class 'sage.combinat.permutation.StandardPermutations_n_with_category.element_class'>

    The elements ``el`` of the disjoint union are simple wrapped elements.
    So to access the methods, you need to do ``el.value``::

        sage: el[0]                                                                     # needs sage.combinat
        Traceback (most recent call last):
        ...
        TypeError: 'sage.structure.element_wrapper.ElementWrapper' object is not subscriptable

        sage: el.value[0]                                                               # needs sage.combinat
        2

    Possible extensions: the current enumeration order is not suitable
    for unions of infinite enumerated sets (except possibly for the
    last one). One could add options to specify alternative enumeration
    orders (anti-diagonal, round robin, ...) to handle this case.


    .. RUBRIC:: Inheriting from ``DisjointUnionEnumeratedSets``

    There are two different use cases for inheriting from
    :class:`DisjointUnionEnumeratedSets`: writing a parent which
    happens to be a disjoint union of some known parents, or writing
    generic disjoint unions for some particular classes of
    :class:`sage.categories.enumerated_sets.EnumeratedSets`.

    - In the first use case, the input of the ``__init__`` method is
      most likely different from that of
      :class:`DisjointUnionEnumeratedSets`. Then, one simply
      writes the ``__init__`` method as usual::

          sage: class MyUnion(DisjointUnionEnumeratedSets):
          ....:   def __init__(self):
          ....:       DisjointUnionEnumeratedSets.__init__(self,
          ....:            Family([1,2], Permutations))
          sage: pp = MyUnion()
          sage: pp.list()
          [[1], [1, 2], [2, 1]]

      In case the :meth:`__init__` method takes optional arguments,
      or does some normalization on them, a specific method
      ``__classcall_private__`` is required (see the
      documentation of :class:`UniqueRepresentation`).

    - In the second use case, the input of the ``__init__`` method
      is the same as that of :class:`DisjointUnionEnumeratedSets`;
      one therefore wants to inherit the :meth:`__classcall_private__`
      method as well, which can be achieved as follows::

          sage: class UnionOfSpecialSets(DisjointUnionEnumeratedSets):
          ....:     __classcall_private__ = staticmethod(DisjointUnionEnumeratedSets.__classcall_private__)
          sage: psp = UnionOfSpecialSets(Family([1,2], Permutations))
          sage: psp.list()
          [[1], [1, 2], [2, 1]]

    TESTS::

        sage: TestSuite(U1).run()
        sage: TestSuite(U2).run()
        sage: TestSuite(U3).run()                                                       # needs sage.combinat
        sage: TestSuite(U4).run()                                                       # needs sage.combinat
        doctest:...: UserWarning: Disjoint union of Lazy family
        (<class 'sage.combinat.permutation.Permutations'>(i))_{i in Non negative integers}
        is an infinite union
        The default implementation of __contains__ can loop forever. Please overload it.
        sage: TestSuite(UNoFacade).run()                                                # needs sage.combinat

    We skip ``_test_an_element`` because the coercion framework does not
    currently allow a tuple to be returned for facade parents::

        sage: TestSuite(Ukeep).run(skip='_test_an_element')                             # needs sage.combinat

    The following three lines are required for the pickling tests,
    because the classes ``MyUnion`` and ``UnionOfSpecialSets`` have
    been defined interactively::

        sage: import __main__
        sage: __main__.MyUnion = MyUnion
        sage: __main__.UnionOfSpecialSets = UnionOfSpecialSets

        sage: TestSuite(pp).run()
        sage: TestSuite(psp).run()
    """
    @staticmethod
    def __classcall_private__(cls, fam, facade: bool = True, keepkey: bool = False, category=None):
        """
        Normalization of arguments; see :class:`UniqueRepresentation`.

        TESTS:

        We check that disjoint unions have unique representation::

            sage: U1 = DisjointUnionEnumeratedSets({1: FiniteEnumeratedSet([1,2,3]),
            ....:                                   2: FiniteEnumeratedSet([4,5,6])})
            sage: U2 = DisjointUnionEnumeratedSets({1: FiniteEnumeratedSet([1,2,3]),
            ....:                                   2: FiniteEnumeratedSet([4,5,6])})
            sage: U1 == U2
            True
            sage: U1 is U2        # indirect doctest
            True
            sage: U3 = DisjointUnionEnumeratedSets({1: FiniteEnumeratedSet([1,2,3]),
            ....:                                   2: FiniteEnumeratedSet([4,5])})
            sage: U1 == U3
            False
        """
    def __init__(self, family, facade: bool = True, keepkey: bool = False, category=None) -> None:
        """
        TESTS::

            sage: U = DisjointUnionEnumeratedSets({1: FiniteEnumeratedSet([1,2,3]),
            ....:                                  2: FiniteEnumeratedSet([4,5,6])})
            sage: TestSuite(U).run()

            sage: X = DisjointUnionEnumeratedSets({i: Partitions(i) for i in range(5)})             # needs sage.combinat sage.libs.flint
            sage: TestSuite(X).run()                                                    # needs sage.combinat sage.libs.flint
        """
    def __contains__(self, x) -> bool:
        """
        Check containment.

        .. WARNING::

            If ``self`` is an infinite union and if the answer is
            logically False, this will loop forever and never answer
            ``False``. Therefore, a warning is issued.

        EXAMPLES::

            sage: U4 = DisjointUnionEnumeratedSets(                                     # needs sage.combinat
            ....:          Family(NonNegativeIntegers(), Partitions))
            sage: Partition([]) in U4                                                   # needs sage.combinat
            doctest:...: UserWarning: Disjoint union of Lazy family
            (<class 'sage.combinat.partition.Partitions'>(i))_{i in Non negative integers}
            is an infinite union
            The default implementation of __contains__ can loop forever. Please overload it.
            True

        Note: one has to use a different family from the previous one in this
        file otherwise the warning is not re-issued::

            sage: Partition([3,2,1,1]) in U4                                            # needs sage.combinat
            True

        The following call will loop forever::

            sage: 2 in U4 # not tested, loop forever
        """
    def __iter__(self):
        """
        TESTS::

            sage: U4 = DisjointUnionEnumeratedSets(
            ....:          Family(NonNegativeIntegers(), Permutations))
            sage: it = iter(U4)
            sage: [next(it), next(it), next(it), next(it), next(it), next(it)]
            [[], [1], [1, 2], [2, 1], [1, 2, 3], [1, 3, 2]]

            sage: # needs sage.combinat
            sage: U4 = DisjointUnionEnumeratedSets(
            ....:          Family(NonNegativeIntegers(), Permutations),
            ....:          keepkey=True, facade=False)
            sage: it = iter(U4)
            sage: [next(it), next(it), next(it), next(it), next(it), next(it)]
            [(0, []), (1, [1]), (2, [1, 2]), (2, [2, 1]), (3, [1, 2, 3]), (3, [1, 3, 2])]
            sage: el = next(it); el.parent() == U4
            True
            sage: el.value == (3, Permutation([2,1,3]))
            True
        """
    def an_element(self):
        """
        Return an element of this disjoint union, as per
        :meth:`Sets.ParentMethods.an_element`.

        EXAMPLES::

            sage: U4 = DisjointUnionEnumeratedSets(
            ....:          Family([3, 5, 7], Permutations))
            sage: U4.an_element()
            [1, 2, 3]
        """
    @cached_method
    def cardinality(self):
        """
        Return the cardinality of this disjoint union.

        EXAMPLES:

        For finite disjoint unions, the cardinality is computed by
        summing the cardinalities of the enumerated sets::

            sage: U = DisjointUnionEnumeratedSets(Family([0,1,2,3], Permutations))
            sage: U.cardinality()
            10

        For infinite disjoint unions, this makes the assumption that
        the result is infinite::

            sage: U = DisjointUnionEnumeratedSets(
            ....:         Family(NonNegativeIntegers(), Permutations))
            sage: U.cardinality()
            +Infinity

        .. WARNING::

            As pointed out in the main documentation, it is
            possible to construct examples where this is incorrect::

                sage: U = DisjointUnionEnumeratedSets(
                ....:         Family(NonNegativeIntegers(), lambda x: []))
                sage: U.cardinality()  # Should be 0!
                +Infinity
        """
    @lazy_attribute
    def Element(self):
        """
        TESTS::

            sage: # needs sage.combinat sage.libs.flint
            sage: U = DisjointUnionEnumeratedSets(
            ....:          Family([1,2,3], Partitions), facade=False)
            sage: U.Element
            <... 'sage.structure.element_wrapper.ElementWrapper'>
            sage: U = DisjointUnionEnumeratedSets(
            ....:          Family([1,2,3], Partitions), facade=True)
            sage: U.Element
            Traceback (most recent call last):
            ...
            AttributeError: 'DisjointUnionEnumeratedSets_with_category' object
            has no attribute 'Element'...
        """
