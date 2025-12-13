from sage.categories.category_with_axiom import CategoryWithAxiom as CategoryWithAxiom

class InfiniteEnumeratedSets(CategoryWithAxiom):
    """
    The category of infinite enumerated sets.

    An infinite enumerated sets is a countable set together with a
    canonical enumeration of its elements.

    EXAMPLES::

        sage: InfiniteEnumeratedSets()
        Category of infinite enumerated sets
        sage: InfiniteEnumeratedSets().super_categories()
        [Category of enumerated sets, Category of infinite sets]
        sage: InfiniteEnumeratedSets().all_super_categories()
        [Category of infinite enumerated sets,
         Category of enumerated sets,
         Category of infinite sets,
         Category of sets,
         Category of sets with partial maps,
         Category of objects]

    TESTS::

        sage: C = InfiniteEnumeratedSets()
        sage: TestSuite(C).run()
    """
    class ParentMethods:
        def random_element(self) -> None:
            """
            Raise an error because ``self`` is an infinite enumerated set.

            EXAMPLES::

                sage: NN = InfiniteEnumeratedSets().example()
                sage: NN.random_element()
                Traceback (most recent call last):
                ...
                NotImplementedError: infinite set

            TODO: should this be an optional abstract_method instead?
            """
        def tuple(self) -> None:
            """
            Raise an error because ``self`` is an infinite enumerated set.

            EXAMPLES::

                sage: NN = InfiniteEnumeratedSets().example()
                sage: NN.tuple()
                Traceback (most recent call last):
                ...
                NotImplementedError: cannot list an infinite set
            """
        def list(self) -> None:
            """
            Raise an error because ``self`` is an infinite enumerated set.

            EXAMPLES::

                sage: NN = InfiniteEnumeratedSets().example()
                sage: NN.list()
                Traceback (most recent call last):
                ...
                NotImplementedError: cannot list an infinite set
            """
