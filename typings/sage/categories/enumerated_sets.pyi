from _typeshed import Incomplete
from collections.abc import Generator
from sage.categories.cartesian_product import CartesianProductsCategory as CartesianProductsCategory
from sage.categories.category_with_axiom import CategoryWithAxiom as CategoryWithAxiom
from sage.categories.sets_cat import EmptySetError as EmptySetError, Sets as Sets
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import LazyImport as LazyImport, lazy_import as lazy_import

class EnumeratedSets(CategoryWithAxiom):
    """
    The category of enumerated sets.

    An *enumerated set* is a *finite* or *countable* set or multiset `S`
    together with a canonical enumeration of its elements;
    conceptually, this is very similar to an immutable list. The main
    difference lies in the names and the return type of the methods,
    and of course the fact that the list of elements is not supposed to
    be expanded in memory. Whenever possible one should use one of the
    two sub-categories :class:`FiniteEnumeratedSets` or
    :class:`InfiniteEnumeratedSets`.

    The purpose of this category is threefold:

    - to fix a common interface for all these sets;
    - to provide a bunch of default implementations;
    - to provide consistency tests.

    The standard methods for an enumerated set ``S`` are:

    - ``S.cardinality()`` -- the number of elements of the set. This
      is the equivalent for ``len`` on a list except that the
      return value is specified to be a Sage :class:`Integer` or
      ``infinity``, instead of a Python ``int``.

    - ``iter(S)`` -- an iterator for the elements of the set;

    - ``S.list()`` -- a fresh list of the elements of the set, when
      possible; raises a :exc:`NotImplementedError` if the list is
      predictably too large to be expanded in memory.

    - ``S.tuple()`` -- a tuple of the elements of the set, when
      possible; raises a :exc:`NotImplementedError` if the tuple is
      predictably too large to be expanded in memory.

    - ``S.unrank(n)`` -- the  ``n``-th element of the set when ``n`` is a sage
      ``Integer``. This is the equivalent for ``l[n]`` on a list.

    - ``S.rank(e)`` -- the position of the element ``e`` in the set;
      This is equivalent to ``l.index(e)`` for a list except that
      the return value is specified to be a Sage :class:`Integer`,
      instead of a Python ``int``.

    - ``S.first()`` -- the first object of the set; it is equivalent to
      ``S.unrank(0)``.

    - ``S.next(e)`` -- the object of the set which follows ``e``; it is
      equivalent to ``S.unrank(S.rank(e) + 1)``.

    - ``S.random_element()`` -- a random generator for an element of
      the set. Unless otherwise stated, and for finite enumerated
      sets, the probability is uniform.

    For examples and tests see:

    - ``FiniteEnumeratedSets().example()``
    - ``InfiniteEnumeratedSets().example()``

    EXAMPLES::

        sage: EnumeratedSets()
        Category of enumerated sets
        sage: EnumeratedSets().super_categories()
        [Category of sets]
        sage: EnumeratedSets().all_super_categories()
        [Category of enumerated sets, Category of sets,
         Category of sets with partial maps, Category of objects]

    TESTS::

        sage: C = EnumeratedSets()
        sage: TestSuite(C).run()
    """
    def super_categories(self):
        """
        EXAMPLES::

            sage: EnumeratedSets().super_categories()
            [Category of sets]
        """
    def additional_structure(self) -> None:
        """
        Return ``None``.

        Indeed, morphisms of enumerated sets are not required to
        preserve the enumeration.

        .. SEEALSO:: :meth:`Category.additional_structure`

        EXAMPLES::

            sage: EnumeratedSets().additional_structure()
        """
    class ParentMethods:
        def __iter__(self):
            """
            An iterator for the enumerated set.

            ``iter(self)`` allows the combinatorial class to be treated as an
            iterable. This is the default implementation from the category
            ``EnumeratedSets()``; it just goes through the iterator of the set
            to count the number of objects.

            By decreasing order of priority, the second column of the
            following array shows which method is used to define
            ``__iter__``, when the methods of the first column are overloaded:

            +------------------------+---------------------------------+
            | Needed methods         | Default ``__iterator`` provided |
            +========================+=================================+
            | ``first`` and ``next`` | ``_iterator_from_next``         |
            +------------------------+---------------------------------+
            | ``unrank``             | ``_iterator_from_unrank``       |
            +------------------------+---------------------------------+
            | ``list``               | ``_iterator_from_next``         |
            +------------------------+---------------------------------+

            It is also possible to override ``__iter__`` method itself. Then
            the methods of the first column are defined using  ``__iter__``

            If none of these are provided, this raises
            a :exc:`NotImplementedError`.

            EXAMPLES:

            We start with an example where nothing is implemented::

                sage: class broken(UniqueRepresentation, Parent):
                ....:     def __init__(self):
                ....:         Parent.__init__(self, category = EnumeratedSets())
                sage: it = iter(broken()); [next(it), next(it), next(it)]
                Traceback (most recent call last):
                ...
                NotImplementedError: iterator called but not implemented

            Here is what happens when ``first`` and ``next`` are implemented::

                sage: class set_first_next(UniqueRepresentation, Parent):
                ....:     def __init__(self):
                ....:         Parent.__init__(self, category = EnumeratedSets())
                ....:     def first(self):
                ....:         return 0
                ....:     def next(self, elt):
                ....:         return elt+1
                sage: it = iter(set_first_next()); [next(it), next(it), next(it)]
                [0, 1, 2]

            Let us try with ``unrank``::

                sage: class set_unrank(UniqueRepresentation, Parent):
                ....:     def __init__(self):
                ....:         Parent.__init__(self, category = EnumeratedSets())
                ....:     def unrank(self, i):
                ....:         return i + 5
                sage: it = iter(set_unrank()); [next(it), next(it), next(it)]
                [5, 6, 7]

            Let us finally try with ``list``::

                sage: class set_list(UniqueRepresentation, Parent):
                ....:     def __init__(self):
                ....:         Parent.__init__(self, category = EnumeratedSets())
                ....:     def list(self):
                ....:         return [5, 6, 7]
                sage: it = iter(set_list()); [next(it), next(it), next(it)]
                [5, 6, 7]
            """
        def is_empty(self):
            """
            Return whether this set is empty.

            EXAMPLES::

                sage: F = FiniteEnumeratedSet([1,2,3])
                sage: F.is_empty()
                False
                sage: F = FiniteEnumeratedSet([])
                sage: F.is_empty()
                True

            TESTS::

                sage: F.is_empty.__module__
                'sage.categories.enumerated_sets'
            """
        def iterator_range(self, start=None, stop=None, step=None) -> Generator[Incomplete, Incomplete]:
            """
            Iterate over the range of elements of ``self`` starting
            at ``start``, ending at ``stop``, and stepping by ``step``.

            .. SEEALSO::

                ``unrank()``, ``unrank_range()``

            EXAMPLES::

                sage: # needs sage.combinat
                sage: P = Partitions()
                sage: list(P.iterator_range(stop=5))
                [[], [1], [2], [1, 1], [3]]
                sage: list(P.iterator_range(0, 5))
                [[], [1], [2], [1, 1], [3]]
                sage: list(P.iterator_range(3, 5))
                [[1, 1], [3]]
                sage: list(P.iterator_range(3, 10))
                [[1, 1], [3], [2, 1], [1, 1, 1], [4], [3, 1], [2, 2]]
                sage: list(P.iterator_range(3, 10, 2))
                [[1, 1], [2, 1], [4], [2, 2]]
                sage: it = P.iterator_range(3)
                sage: [next(it) for x in range(10)]
                [[1, 1],
                 [3], [2, 1], [1, 1, 1],
                 [4], [3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1],
                 [5]]
                sage: it = P.iterator_range(3, step=2)
                sage: [next(it) for x in range(5)]
                [[1, 1],
                 [2, 1],
                 [4], [2, 2], [1, 1, 1, 1]]
                sage: next(P.iterator_range(stop=-3))
                Traceback (most recent call last):
                ...
                NotImplementedError: cannot list an infinite set
                sage: next(P.iterator_range(start=-3))
                Traceback (most recent call last):
                ...
                NotImplementedError: cannot list an infinite set
            """
        def unrank_range(self, start=None, stop=None, step=None):
            """
            Return the range of elements of ``self`` starting at ``start``,
            ending at ``stop``, and stepping by ``step``.

            .. SEEALSO::

                ``unrank()``, ``iterator_range()``

            EXAMPLES::

                sage: # needs sage.combinat
                sage: P = Partitions()
                sage: P.unrank_range(stop=5)
                [[], [1], [2], [1, 1], [3]]
                sage: P.unrank_range(0, 5)
                [[], [1], [2], [1, 1], [3]]
                sage: P.unrank_range(3, 5)
                [[1, 1], [3]]
                sage: P.unrank_range(3, 10)
                [[1, 1], [3], [2, 1], [1, 1, 1], [4], [3, 1], [2, 2]]
                sage: P.unrank_range(3, 10, 2)
                [[1, 1], [2, 1], [4], [2, 2]]
                sage: P.unrank_range(3)
                Traceback (most recent call last):
                ...
                NotImplementedError: cannot list an infinite set
                sage: P.unrank_range(stop=-3)
                Traceback (most recent call last):
                ...
                NotImplementedError: cannot list an infinite set
                sage: P.unrank_range(start=-3)
                Traceback (most recent call last):
                ...
                NotImplementedError: cannot list an infinite set
            """
        def __getitem__(self, i):
            """
            Return the item indexed by ``i``.

            .. WARNING::

                This method is only meant as a convenience shorthand for
                ``self.unrank(i)`` and
                ``self.unrank_range(start, stop, step)`` respectively, for
                casual use (e.g. in interactive sessions). Subclasses are
                hereby explicitly permitted to overload ``__getitem__``
                with a different semantic, typically for enumerated sets
                that are naturally indexed by some `I` not of the
                form `\\{0, 1, \\ldots\\}`. In particular, generic code
                *should not* use this shorthand.

            EXAMPLES::

                sage: # needs sage.combinat
                sage: P = Partitions()
                sage: P[:5]
                [[], [1], [2], [1, 1], [3]]
                sage: P[0:5]
                [[], [1], [2], [1, 1], [3]]
                sage: P[3:5]
                [[1, 1], [3]]
                sage: P[3:10]
                [[1, 1], [3], [2, 1], [1, 1, 1], [4], [3, 1], [2, 2]]
                sage: P[3:10:2]
                [[1, 1], [2, 1], [4], [2, 2]]
                sage: P[3:]
                Traceback (most recent call last):
                ...
                NotImplementedError: cannot list an infinite set
                sage: P[3]
                [1, 1]
                sage: P[-1]
                Traceback (most recent call last):
                ...
                ValueError: infinite list

            ::

                sage: C = FiniteEnumeratedSets().example()
                sage: C.list()
                [1, 2, 3]
                sage: C[1]
                2
                sage: C[:]
                [1, 2, 3]
                sage: C[1:]
                [2, 3]
                sage: C[0:1:2]
                [1]

                sage: F = FiniteEnumeratedSet([1,2,3])
                sage: F[1:]
                [2, 3]
                sage: F[:2]
                [1, 2]
                sage: F[:2:2]
                [1]
                sage: F[1::2]
                [2]

            TESTS:

            Verify that an infinite index raises an error::

                sage: F = FiniteEnumeratedSet([1,2,3,4,5])
                sage: F[oo]
                Traceback (most recent call last):
                ...
                TypeError: unable to coerce <class 'sage.rings.infinity.PlusInfinity'>
                to an integer
            """
        def __len__(self) -> int:
            """
            Return the number of elements of ``self``.

            EXAMPLES::

                sage: len(GF(5))
                5
                sage: len(MatrixSpace(GF(2), 3, 3))                                     # needs sage.modules
                512
            """
        def tuple(self):
            """
            Return a tuple of the elements of ``self``.

            The tuple of elements of ``x`` is created and cached on the first call
            of ``x.tuple()``. Each following call of ``x.tuple()`` returns the same tuple.

            For looping, it may be better to do ``for e in x:``, not ``for e in x.tuple():``.

            If ``x`` is not known to be finite, then an exception is raised.

            EXAMPLES::

                sage: (GF(3)^2).tuple()                                                 # needs sage.modules
                ((0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2))
                sage: R = Integers(11)
                sage: l = R.tuple(); l
                (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
                sage: l is R.tuple()
                True
            """
        def list(self):
            """
            Return a list of the elements of ``self``.

            The elements of set ``x`` are created and cached on the first call
            of ``x.list()``. Then each call of ``x.list()`` returns a new list
            from the cached result. Thus in looping, it may be better to do
            ``for e in x:``, not ``for e in x.list():``.

            If ``x`` is not known to be finite, then an exception is raised.

            EXAMPLES::

                sage: (GF(3)^2).list()                                                  # needs sage.modules
                [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)]
                sage: R = Integers(11)
                sage: R.list()
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                sage: l = R.list(); l
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                sage: l.remove(0); l
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                sage: R.list()
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

                sage: C = FiniteEnumeratedSets().example()
                sage: C.list()
                [1, 2, 3]
            """
        first: Incomplete
        next: Incomplete
        unrank: Incomplete
        rank: Incomplete
        some_elements: Incomplete
        def random_element(self) -> None:
            """
            Return a random element in ``self``.

            Unless otherwise stated, and for finite enumerated sets,
            the probability is uniform.

            This is a generic implementation from the category
            ``EnumeratedSets()``. It raises a :exc:`NotImplementedError`
            since one does not know whether the set is finite.

            EXAMPLES::

                sage: class broken(UniqueRepresentation, Parent):
                ....:  def __init__(self):
                ....:      Parent.__init__(self, category = EnumeratedSets())
                sage: broken().random_element()
                Traceback (most recent call last):
                ...
                NotImplementedError: unknown cardinality
            """
        def map(self, f, name=None, *, is_injective: bool = True):
            """
            Return the image `\\{f(x) | x \\in \\text{self}\\}` of this
            enumerated set by `f`, as an enumerated set.

            INPUT:

            - ``is_injective`` -- boolean (default: ``True``); whether to assume
              that `f` is injective

            EXAMPLES::

                sage: R = Compositions(4).map(attrcall('partial_sums')); R
                Image of Compositions of 4 by The map *.partial_sums()
                 from Compositions of 4
                sage: R.cardinality()
                8
                sage: R.list()
                [[1, 2, 3, 4], [1, 2, 4], [1, 3, 4], [1, 4], [2, 3, 4], [2, 4], [3, 4], [4]]
                sage: [r for r in R]
                [[1, 2, 3, 4], [1, 2, 4], [1, 3, 4], [1, 4], [2, 3, 4], [2, 4], [3, 4], [4]]
                sage: R.category()
                Category of finite enumerated subobjects of sets

            .. WARNING::

                If the function is not injective, then there may be
                repeated elements::

                    sage: P = Compositions(4)
                    sage: P.list()
                    [[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [1, 3], [2, 1, 1], [2, 2], [3, 1], [4]]
                    sage: P.map(attrcall('major_index')).list()
                    [6, 3, 4, 1, 5, 2, 3, 0]

                Pass ``is_injective=False`` to get a correct result in this case::

                    sage: P.map(attrcall('major_index'), is_injective=False).list()
                    [6, 3, 4, 1, 5, 2, 0]

            TESTS::

                sage: TestSuite(R).run(skip=['_test_an_element',
                ....:                        '_test_enumerated_set_contains',
                ....:                        '_test_some_elements'])
            """
    class ElementMethods:
        def rank(self):
            """
            Return the rank of ``self`` in its parent.

            See also :meth:`EnumeratedSets.ElementMethods.rank`

            EXAMPLES::

                sage: F = FiniteSemigroups().example(('a','b','c'))
                sage: L = list(F)
                sage: L[7].rank()
                7
                sage: all(x.rank() == i for i,x in enumerate(L))
                True
            """
    Finite: Incomplete
    Infinite: Incomplete
    class CartesianProducts(CartesianProductsCategory):
        class ParentMethods:
            def first(self):
                """
                Return the first element.

                EXAMPLES::

                    sage: cartesian_product([ZZ]*10).first()
                    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                """
