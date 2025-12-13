from _typeshed import Incomplete
from collections.abc import Generator
from sage.categories.cartesian_product import CartesianProductsCategory as CartesianProductsCategory
from sage.categories.category_with_axiom import CategoryWithAxiom as CategoryWithAxiom
from sage.categories.enumerated_sets import EnumeratedSets as EnumeratedSets
from sage.categories.isomorphic_objects import IsomorphicObjectsCategory as IsomorphicObjectsCategory
from sage.categories.sets_cat import Sets as Sets
from sage.cpython.getattr import raw_getattr as raw_getattr
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import lazy_import as lazy_import

class FiniteEnumeratedSets(CategoryWithAxiom):
    """
    The category of finite enumerated sets.

    EXAMPLES::

        sage: FiniteEnumeratedSets()
        Category of finite enumerated sets
        sage: FiniteEnumeratedSets().super_categories()
        [Category of enumerated sets, Category of finite sets]
        sage: FiniteEnumeratedSets().all_super_categories()
        [Category of finite enumerated sets,
         Category of enumerated sets,
         Category of finite sets,
         Category of sets,
         Category of sets with partial maps,
         Category of objects]

    TESTS::

        sage: C = FiniteEnumeratedSets()
        sage: TestSuite(C).run()
        sage: sorted(C.Algebras(QQ).super_categories(), key=str)
        [Category of finite dimensional vector spaces with basis over Rational Field,
         Category of set algebras over Rational Field]

    .. TODO::

        :class:`sage.combinat.debruijn_sequence.DeBruijnSequences` should
        not inherit from this class. If that is solved, then
        :class:`FiniteEnumeratedSets` shall be turned into a subclass of
        :class:`~sage.categories.category_singleton.Category_singleton`.
    """
    class ParentMethods:
        def __len__(self) -> int:
            """
            Return the number of elements of ``self``.

            EXAMPLES::

                sage: len(GF(5))
                5
                sage: len(MatrixSpace(GF(2), 3, 3))                                     # needs sage.modules
                512
            """
        cardinality: Incomplete
        def tuple(self):
            """
            Return a :class:`tuple`of the elements of ``self``.

            EXAMPLES::

                sage: C = FiniteEnumeratedSets().example()
                sage: C.tuple()
                (1, 2, 3)
                sage: C.tuple() is C.tuple()
                True
            """
        def unrank_range(self, start=None, stop=None, step=None):
            """
            Return the range of elements of ``self`` starting at ``start``,
            ending at ``stop``, and stepping by ``step``.

            See also ``unrank()``.

            EXAMPLES::

                sage: F = FiniteEnumeratedSet([1,2,3])
                sage: F.unrank_range(1)
                [2, 3]
                sage: F.unrank_range(stop=2)
                [1, 2]
                sage: F.unrank_range(stop=2, step=2)
                [1]
                sage: F.unrank_range(start=1, step=2)
                [2]
                sage: F.unrank_range(stop=-1)
                [1, 2]

                sage: F = FiniteEnumeratedSet([1,2,3,4])
                sage: F.unrank_range(stop=10)
                [1, 2, 3, 4]
            """
        def iterator_range(self, start=None, stop=None, step=None) -> Generator[Incomplete, Incomplete]:
            """
            Iterate over the range of elements of ``self`` starting
            at ``start``, ending at ``stop``, and stepping by ``step``.

            .. SEEALSO::

                ``unrank()``, ``unrank_range()``

            EXAMPLES::

                sage: F = FiniteEnumeratedSet([1,2,3])
                sage: list(F.iterator_range(1))
                [2, 3]
                sage: list(F.iterator_range(stop=2))
                [1, 2]
                sage: list(F.iterator_range(stop=2, step=2))
                [1]
                sage: list(F.iterator_range(start=1, step=2))
                [2]
                sage: list(F.iterator_range(start=1, stop=2))
                [2]
                sage: list(F.iterator_range(start=0, stop=1))
                [1]
                sage: list(F.iterator_range(start=0, stop=3, step=2))
                [1, 3]
                sage: list(F.iterator_range(stop=-1))
                [1, 2]

                sage: F = FiniteEnumeratedSet([1,2,3,4])
                sage: list(F.iterator_range(start=1, stop=3))
                [2, 3]
                sage: list(F.iterator_range(stop=10))
                [1, 2, 3, 4]
            """
        random_element: Incomplete
        last: Incomplete
    class CartesianProducts(CartesianProductsCategory):
        def extra_super_categories(self):
            """
            A Cartesian product of finite enumerated sets is a finite
            enumerated set.

            EXAMPLES::

                sage: C = FiniteEnumeratedSets().CartesianProducts()
                sage: C.extra_super_categories()
                [Category of finite enumerated sets]
            """
        class ParentMethods:
            """
            TESTS:

            Ideally, these tests should be just after the declaration of the
            associated attributes. But doing this way, Sage will not consider
            them as a doctest.

            We check that Cartesian products of finite enumerated sets
            inherit various methods from `Sets.CartesianProducts`
            and not from :class:`EnumeratedSets.Finite`::

                sage: C = cartesian_product([Partitions(10), Permutations(20)])         # needs sage.combinat
                sage: C in EnumeratedSets().Finite()                                    # needs sage.combinat
                True

                sage: C.random_element.__module__                                       # needs sage.combinat
                'sage.categories.sets_cat'

                sage: C.cardinality.__module__                                          # needs sage.combinat
                'sage.categories.sets_cat'

                sage: C.__iter__.__module__                                             # needs sage.combinat
                'sage.categories.sets_cat'
            """
            random_element: Incomplete
            cardinality: Incomplete
            __iter__: Incomplete
            def last(self):
                """
                Return the last element.

                EXAMPLES::

                    sage: C = cartesian_product([Zmod(42), Partitions(10),              # needs sage.combinat
                    ....:                        IntegerRange(5)])
                    sage: C.last()                                                      # needs sage.combinat
                    (41, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 4)
                """
            def rank(self, x):
                """
                Return the rank of an element of this Cartesian product.

                The *rank* of ``x`` is its position in the
                enumeration. It is an integer between ``0`` and
                ``n-1`` where ``n`` is the cardinality of this set.

                .. SEEALSO::

                    - :meth:`EnumeratedSets.ParentMethods.rank`
                    - :meth:`unrank`

                EXAMPLES::

                    sage: C = cartesian_product([GF(2), GF(11), GF(7)])
                    sage: C.rank(C((1,2,5)))
                    96
                    sage: C.rank(C((0,0,0)))
                    0

                    sage: for c in C: print(C.rank(c))
                    0
                    1
                    2
                    3
                    4
                    5
                    ...
                    150
                    151
                    152
                    153

                    sage: # needs sage.combinat
                    sage: F1 = FiniteEnumeratedSet('abcdefgh')
                    sage: F2 = IntegerRange(250)
                    sage: F3 = Partitions(20)
                    sage: C = cartesian_product([F1, F2, F3])
                    sage: c = C(('a', 86, [7,5,4,4]))
                    sage: C.rank(c)
                    54213
                    sage: C.unrank(54213)
                    ('a', 86, [7, 5, 4, 4])
                """
            def unrank(self, i):
                """
                Return the `i`-th element of this Cartesian product.

                INPUT:

                - ``i`` -- integer between `0` and `n-1` where
                  `n` is the cardinality of this set

                .. SEEALSO::

                    - :meth:`EnumeratedSets.ParentMethods.unrank`
                    - :meth:`rank`

                EXAMPLES::

                    sage: C = cartesian_product([GF(3), GF(11), GF(7), GF(5)])
                    sage: c = C.unrank(123); c
                    (0, 3, 3, 3)
                    sage: C.rank(c)
                    123

                    sage: c = C.unrank(857); c
                    (2, 2, 3, 2)
                    sage: C.rank(c)
                    857

                    sage: C.unrank(2500)
                    Traceback (most recent call last):
                    ...
                    IndexError: index i (=2) is greater than the cardinality
                """
    class IsomorphicObjects(IsomorphicObjectsCategory):
        def example(self):
            """
            Return an example of isomorphic object of a finite
            enumerated set, as per :meth:`Category.example
            <sage.categories.category.Category.example>`.

            EXAMPLES::

                sage: FiniteEnumeratedSets().IsomorphicObjects().example()
                The image by some isomorphism of An example of a finite enumerated set: {1,2,3}
            """
        class ParentMethods:
            def cardinality(self):
                """
                Return the cardinality of ``self`` which is the same
                as that of the ambient set ``self`` is isomorphic to.

                EXAMPLES::

                    sage: A = FiniteEnumeratedSets().IsomorphicObjects().example(); A
                    The image by some isomorphism of An example of a finite enumerated set: {1,2,3}
                    sage: A.cardinality()
                    3
                """
            def __iter__(self):
                """
                Return an iterator over ``self``, using the bijection
                with the ambient space.

                EXAMPLES::

                    sage: A = FiniteEnumeratedSets().IsomorphicObjects().example(); A
                    The image by some isomorphism of An example of a finite enumerated set: {1,2,3}
                    sage: list(A)                  # indirect doctest
                    [1, 4, 9]
                """
