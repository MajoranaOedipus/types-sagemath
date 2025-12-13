from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.categories.sets_cat import EmptySetError as EmptySetError
from sage.rings.integer import Integer as Integer
from sage.structure.element import Element as Element
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class FiniteEnumeratedSet(UniqueRepresentation, Parent):
    """
    A class for finite enumerated set.

    Returns the finite enumerated set with elements in ``elements``
    where ``element`` is any (finite) iterable object.

    The main purpose is to provide a variant of ``list`` or ``tuple``,
    which is a parent with an interface consistent with
    ``EnumeratedSets`` and has unique representation.
    The list of the elements is expanded in memory.

    EXAMPLES::

        sage: S = FiniteEnumeratedSet([1, 2, 3])
        sage: S
        {1, 2, 3}
        sage: S.list()
        [1, 2, 3]
        sage: S.cardinality()
        3
        sage: S.random_element()  # random
        1
        sage: S.first()
        1
        sage: S.category()
        Category of facade finite enumerated sets
        sage: TestSuite(S).run()

    Note that being an enumerated set, the result depends on the order::

        sage: S1 = FiniteEnumeratedSet((1, 2, 3))
        sage: S1
        {1, 2, 3}
        sage: S1.list()
        [1, 2, 3]
        sage: S1 == S
        True
        sage: S2 = FiniteEnumeratedSet((2, 1, 3))
        sage: S2 == S
        False

    As an abuse, repeated entries in ``elements`` are allowed to model
    multisets::

        sage: S1 = FiniteEnumeratedSet((1, 2, 1, 2, 2, 3))
        sage: S1
        {1, 2, 1, 2, 2, 3}

    Finally, the elements are not aware of their parent::

        sage: S.first().parent()
        Integer Ring
    """
    @staticmethod
    def __classcall__(cls, iterable):
        """
        Standard trick to expand the iterable upon input, and
        guarantees unique representation, independently of the type of
        the iterable. See ``UniqueRepresentation``.

        TESTS::

            sage: S1 = FiniteEnumeratedSet([1, 2, 3])
            sage: S2 = FiniteEnumeratedSet((1, 2, 3))
            sage: S3 = FiniteEnumeratedSet((x for x in range(1,4)))
            sage: S1 is S2
            True
            sage: S2 is S3
            True
        """
    def __init__(self, elements) -> None:
        """
        TESTS::

            sage: TestSuite(FiniteEnumeratedSet([1,2,3])).run()
            sage: TestSuite(FiniteEnumeratedSet([])).run()
        """
    def __bool__(self) -> bool:
        """
        Conversion to boolean.

        EXAMPLES::

            sage: bool(FiniteEnumeratedSet('abc'))
            True
            sage: bool(FiniteEnumeratedSet([]))
            False
        """
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: S = FiniteEnumeratedSet([1,2,3])
            sage: 1 in S
            True
            sage: 2 in S
            True
            sage: 4 in S
            False
            sage: ZZ in S
            False

            sage: S.is_parent_of(2)
            True
            sage: S.is_parent_of(4)
            False
        """
    is_parent_of = __contains__
    def __iter__(self):
        """
        Iterator over the element of ``self``.

        EXAMPLES::

            sage: for i in FiniteEnumeratedSet([1,2,3]): print(i)
            1
            2
            3
        """
    def list(self):
        """
        TESTS::

            sage: S = FiniteEnumeratedSet([1,2,3])
            sage: S.list()
            [1, 2, 3]
        """
    def an_element(self):
        """
        TESTS::

            sage: S = FiniteEnumeratedSet([1,2,3])
            sage: S.an_element()
            1
        """
    def first(self):
        """
        Return the first element of the enumeration or raise an
        :exc:`EmptySetError` if the set is empty.

        EXAMPLES::

            sage: S = FiniteEnumeratedSet('abc')
            sage: S.first()
            'a'
        """
    def last(self):
        """
        Return the last element of the iteration or raise an
        :exc:`EmptySetError` if the set is empty.

        EXAMPLES::

            sage: S = FiniteEnumeratedSet([0,'a',1.23, 'd'])
            sage: S.last()
            'd'
        """
    def random_element(self):
        """
        Return a random element.

        EXAMPLES::

            sage: S = FiniteEnumeratedSet('abc')
            sage: S.random_element()   # random
            'b'

        TESTS::

            sage: S = FiniteEnumeratedSet([1,2,3])
            sage: S.random_element() in S
            True
        """
    def cardinality(self):
        """
        TESTS::

            sage: S = FiniteEnumeratedSet([1,2,3])
            sage: S.cardinality()
            3
        """
    def rank(self, x):
        """
        Return the index of ``x`` in this finite enumerated set.

        EXAMPLES::

            sage: S = FiniteEnumeratedSet(['a','b','c'])
            sage: S.index('b')
            1
        """
    index = rank
    def unrank(self, i):
        """
        Return the element at position ``i``.

        EXAMPLES::

            sage: S = FiniteEnumeratedSet([1,'a',-51])
            sage: S[0], S[1], S[2]
            (1, 'a', -51)
            sage: S[3]
            Traceback (most recent call last):
            ...
            IndexError: tuple index out of range
            sage: S[-1], S[-2], S[-3]
            (-51, 'a', 1)
            sage: S[-4]
            Traceback (most recent call last):
            ...
            IndexError: index out of range
        """
    def __call__(self, el):
        """
        Coerce or convert ``el`` into an element of ``self``.

        INPUT:

        - ``el`` -- some object

        As :meth:`Parent.__call__`, this tries to convert or coerce
        ``el`` into an element of ``self`` depending on the parent of
        ``el``. If no such conversion or coercion is available, this
        calls :meth:`_element_constructor_`.

        :meth:`Parent.__call__` enforces that
        :meth:`_element_constructor_` return an :class:`Element` (more
        precisely, it calls :meth:`_element_constructor_` through a
        :class:`sage.structure.coerce_maps.DefaultConvertMap_unique`,
        and any :class:`sage.categories.map.Map` requires its results
        to be instances of :class:`Element`).

        Since :class:`FiniteEnumeratedSets` is often a facade over
        plain Python objects, :issue:`16280` introduced this method
        which works around this limitation by calling directly
        :meth:`_element_constructor_` whenever ``el`` is not an
        :class:`Element`. Otherwise :meth:`Parent.__call__` is called
        as usual.

        .. WARNING::

            This workaround prevents conversions or coercions from
            facade parents over plain Python objects into ``self``.

        If the :meth:`Parent.__call__` fails, then we try
        :meth:`_element_constructor_` directly as the element returned
        may not be a subclass of :class:`Element`, which is currently
        not supported (see :issue:`19553`).

        EXAMPLES::

            sage: F = FiniteEnumeratedSet([1, 2, 'a', 'b'])
            sage: F(1)
            1
            sage: F('a')
            'a'

        We check that conversions are properly honored for usual
        parents; this is not the case for facade parents over plain
        Python objects::

            sage: F = FiniteEnumeratedSet([1, 2, 3, 'a', 'aa'])
            sage: phi = Hom(ZZ, F, Sets())(lambda i: i+i)
            sage: phi(1)
            2
            sage: phi.register_as_conversion()

            sage: from sage.sets.pythonclass import Set_PythonType_class
            sage: psi = Hom(Set_PythonType_class(str), F, Sets())(lambda s: ZZ(len(s)))
            sage: psi.register_as_conversion()
            sage: psi('a')
            1
            sage: F(1)
            2
            sage: F('a')
            'a'

        Check that :issue:`19554` is fixed::

            sage: S = FiniteEnumeratedSet(range(5))
            sage: S(1)
            1
            sage: type(S(1))
            <class 'int'>
        """
