from sage.categories.enumerated_sets import EnumeratedSets as EnumeratedSets
from sage.categories.monoids import Monoids as Monoids
from sage.categories.sets_cat import EmptySetError as EmptySetError, Sets as Sets
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.integer import Integer as Integer
from sage.sets.finite_enumerated_set import FiniteEnumeratedSet as FiniteEnumeratedSet
from sage.sets.finite_set_map_cy import FiniteSetEndoMap_N as FiniteSetEndoMap_N, FiniteSetEndoMap_Set as FiniteSetEndoMap_Set, FiniteSetMap_MN as FiniteSetMap_MN, FiniteSetMap_Set as FiniteSetMap_Set
from sage.sets.integer_range import IntegerRange as IntegerRange
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class FiniteSetMaps(UniqueRepresentation, Parent):
    '''
    Maps between finite sets.

    Constructs the set of all maps between two sets. The sets can be
    given using any of the three following ways:

    1. an object in the category ``Sets()``.

    2. a finite iterable. In this case, an object of the class
       :class:`~sage.sets.finite_enumerated_set.FiniteEnumeratedSet`
       is constructed from the iterable.

    3. an integer ``n`` designing the set `\\{0, 1, \\dots, n-1\\}`. In this case
       an object of the class :class:`~sage.sets.integer_range.IntegerRange` is
       constructed.

    INPUT:

    - ``domain`` -- set, finite iterable, or integer

    - ``codomain`` -- set, finite iterable, integer, or ``None``
      (default). In this last case, the maps are endo-maps of the domain.

    - ``action`` -- ``\'left\'`` (default) or ``\'right\'``. The side
      where the maps act on the domain. This is used in particular to
      define the meaning of the product (composition) of two maps.

    - ``category`` -- the category in which the sets of maps is
      constructed. By default, this is ``FiniteMonoids()`` if the domain and
      codomain coincide, and ``FiniteEnumeratedSets()`` otherwise.

    OUTPUT:

        an instance of a subclass of :class:`FiniteSetMaps` modeling
        the set of all maps between ``domain`` and ``codomain``.

    EXAMPLES:

    We construct the set ``M`` of all maps from `\\{a,b\\}` to `\\{3,4,5\\}`::

        sage: M = FiniteSetMaps(["a", "b"], [3, 4, 5]); M
        Maps from {\'a\', \'b\'} to {3, 4, 5}
        sage: M.cardinality()
        9
        sage: M.domain()
        {\'a\', \'b\'}
        sage: M.codomain()
        {3, 4, 5}
        sage: for f in M: print(f)
        map: a -> 3, b -> 3
        map: a -> 3, b -> 4
        map: a -> 3, b -> 5
        map: a -> 4, b -> 3
        map: a -> 4, b -> 4
        map: a -> 4, b -> 5
        map: a -> 5, b -> 3
        map: a -> 5, b -> 4
        map: a -> 5, b -> 5

    Elements can be constructed from functions and dictionaries::

        sage: M(lambda c: ord(c)-94)
        map: a -> 3, b -> 4

        sage: M.from_dict({\'a\':3, \'b\':5})
        map: a -> 3, b -> 5

    If the domain is equal to the codomain, then maps can be
    composed::

        sage: M = FiniteSetMaps([1, 2, 3])
        sage: f = M.from_dict({1:2, 2:1, 3:3}); f
        map: 1 -> 2, 2 -> 1, 3 -> 3
        sage: g = M.from_dict({1:2, 2:3, 3:1}); g
        map: 1 -> 2, 2 -> 3, 3 -> 1

        sage: f * g
        map: 1 -> 1, 2 -> 3, 3 -> 2

    This makes `M` into a monoid::

        sage: M.category()
        Category of finite enumerated monoids
        sage: M.one()
        map: 1 -> 1, 2 -> 2, 3 -> 3

    By default, composition is from right to left, which corresponds
    to an action on the left. If one specifies ``action`` to right,
    then the composition is from left to right::

        sage: M = FiniteSetMaps([1, 2, 3], action = \'right\')
        sage: f = M.from_dict({1:2, 2:1, 3:3})
        sage: g = M.from_dict({1:2, 2:3, 3:1})
        sage: f * g
        map: 1 -> 3, 2 -> 2, 3 -> 1

    If the domains and codomains are both of the form `\\{0,\\dots\\}`,
    then one can use the shortcut::

        sage: M = FiniteSetMaps(2,3); M
        Maps from {0, 1} to {0, 1, 2}
        sage: M.cardinality()
        9

    For a compact notation, the elements are then printed as lists
    `[f(i), i=0,\\dots]`::

        sage: list(M)
        [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]

    TESTS::

        sage: TestSuite(FiniteSetMaps(0)).run()
        sage: TestSuite(FiniteSetMaps(0, 2)).run()
        sage: TestSuite(FiniteSetMaps(2, 0)).run()
        sage: TestSuite(FiniteSetMaps([], [])).run()
        sage: TestSuite(FiniteSetMaps([1, 2], [])).run()
        sage: TestSuite(FiniteSetMaps([], [1, 2])).run()
    '''
    @staticmethod
    def __classcall_private__(cls, domain, codomain=None, action: str = 'left', category=None):
        '''
        TESTS::

            sage: FiniteSetMaps(3)
            Maps from {0, 1, 2} to itself
            sage: FiniteSetMaps(4, 2)
            Maps from {0, 1, 2, 3} to {0, 1}
            sage: FiniteSetMaps(4, ["a","b","c"])
            Maps from {0, 1, 2, 3} to {\'a\', \'b\', \'c\'}
            sage: FiniteSetMaps([1,2], ["a","b","c"])
            Maps from {1, 2} to {\'a\', \'b\', \'c\'}
            sage: FiniteSetMaps([1,2,4], 3)
            Maps from {1, 2, 4} to {0, 1, 2}
        '''
    def cardinality(self):
        """
        The cardinality of ``self``.

        EXAMPLES::

            sage: FiniteSetMaps(4, 3).cardinality()
            81
        """

class FiniteSetMaps_MN(FiniteSetMaps):
    """
    The set of all maps from `\\{1, 2, \\dots, m\\}` to `\\{1, 2, \\dots, n\\}`.

    Users should use the factory class :class:`FiniteSetMaps` to
    create instances of this class.

    INPUT:

    - ``m``, ``n`` -- integers

    - ``category`` -- the category in which the sets of maps is
      constructed. It must be a sub-category of
      ``EnumeratedSets().Finite()`` which is the default value.
    """
    def __init__(self, m, n, category=None) -> None:
        """
        TESTS::

            sage: M = FiniteSetMaps(2,3)
            sage: M.category()
            Category of finite enumerated sets
            sage: M.__class__
            <class 'sage.sets.finite_set_maps.FiniteSetMaps_MN_with_category'>
            sage: TestSuite(M).run()
        """
    def domain(self):
        """
        The domain of ``self``.

        EXAMPLES::

            sage: FiniteSetMaps(3,2).domain()
            {0, 1, 2}
        """
    def codomain(self):
        """
        The codomain of ``self``.

        EXAMPLES::

            sage: FiniteSetMaps(3,2).codomain()
            {0, 1}
        """
    def __contains__(self, x) -> bool:
        """
        EXAMPLES::

            sage: M = FiniteSetMaps(3,2)
            sage: [0,1,1] in M
            True
            sage: [1,2,4] in M
            False
        """
    def an_element(self):
        """
        Return a map in ``self``.

        EXAMPLES::

            sage: M = FiniteSetMaps(4, 2)
            sage: M.an_element()
            [0, 0, 0, 0]

            sage: M = FiniteSetMaps(0, 0)
            sage: M.an_element()
            []

        An exception :class:`~sage.categories.sets_cat.EmptySetError`
        is raised if this set is empty, that is if the codomain is
        empty and the domain is not. ::

            sage: M = FiniteSetMaps(4, 0)
            sage: M.cardinality()
            0
            sage: M.an_element()
            Traceback (most recent call last):
            ...
            EmptySetError
        """
    def __iter__(self):
        """
        EXAMPLES::

            sage: M = FiniteSetMaps(2,2)
            sage: M.list()
            [[0, 0], [0, 1], [1, 0], [1, 1]]

        TESTS::

            sage: FiniteSetMaps(0,0).list()
            [[]]
            sage: FiniteSetMaps(0,1).list()
            [[]]
            sage: FiniteSetMaps(0,10).list()
            [[]]
            sage: FiniteSetMaps(1,0).list()
            []
            sage: FiniteSetMaps(1,1).list()
            [[0]]
        """
    Element = FiniteSetMap_MN

class FiniteSetMaps_Set(FiniteSetMaps_MN):
    """
    The sets of all maps between two sets.

    Users should use the factory class :class:`FiniteSetMaps` to
    create instances of this class.

    INPUT:

    - ``domain`` -- an object in the category ``FiniteSets()``

    - ``codomain`` -- an object in the category ``FiniteSets()``

    - ``category`` -- the category in which the sets of maps is
      constructed. It must be a sub-category of
      ``EnumeratedSets().Finite()`` which is the default value.
    """
    def __init__(self, domain, codomain, category=None) -> None:
        '''
        EXAMPLES::

            sage: M = FiniteSetMaps(["a", "b"], [3, 4, 5])
            sage: M
            Maps from {\'a\', \'b\'} to {3, 4, 5}
            sage: M.cardinality()
            9
            sage: for f in M: print(f)
            map: a -> 3, b -> 3
            map: a -> 3, b -> 4
            map: a -> 3, b -> 5
            map: a -> 4, b -> 3
            map: a -> 4, b -> 4
            map: a -> 4, b -> 5
            map: a -> 5, b -> 3
            map: a -> 5, b -> 4
            map: a -> 5, b -> 5

        TESTS::

            sage: M.__class__
            <class \'sage.sets.finite_set_maps.FiniteSetMaps_Set_with_category\'>
            sage: M.category()
            Category of finite enumerated sets
            sage: TestSuite(M).run()
        '''
    def domain(self):
        '''
        The domain of ``self``.

        EXAMPLES::

            sage: FiniteSetMaps(["a", "b"], [3, 4, 5]).domain()
            {\'a\', \'b\'}
        '''
    def codomain(self):
        '''
        The codomain of ``self``.

        EXAMPLES::

            sage: FiniteSetMaps(["a", "b"], [3, 4, 5]).codomain()
            {3, 4, 5}
        '''
    def from_dict(self, d):
        '''
        Create a map from a dictionary.

        EXAMPLES::

            sage: M = FiniteSetMaps(["a", "b"], [3, 4, 5])
            sage: M.from_dict({"a": 4, "b": 3})
            map: a -> 4, b -> 3
        '''
    Element = FiniteSetMap_Set

class FiniteSetEndoMaps_N(FiniteSetMaps_MN):
    """
    The sets of all maps from `\\{1, 2, \\dots, n\\}` to itself.

    Users should use the factory class :class:`FiniteSetMaps` to
    create instances of this class.

    INPUT:

    - ``n`` -- integer

    - ``category`` -- the category in which the sets of maps is
      constructed. It must be a sub-category of ``Monoids().Finite()``
      and ``EnumeratedSets().Finite()`` which is the default value.
    """
    def __init__(self, n, action, category=None) -> None:
        """
        EXAMPLES::

            sage: M = FiniteSetMaps(3)
            sage: M.category()
            Category of finite enumerated monoids
            sage: M.__class__
            <class 'sage.sets.finite_set_maps.FiniteSetEndoMaps_N_with_category'>
            sage: TestSuite(M).run()
        """
    @cached_method
    def one(self):
        """
        EXAMPLES::

            sage: M = FiniteSetMaps(4)
            sage: M.one()
            [0, 1, 2, 3]
        """
    def an_element(self):
        """
        Return a map in ``self``.

        EXAMPLES::

            sage: M = FiniteSetMaps(4)
            sage: M.an_element()
            [3, 2, 1, 0]
        """
    Element = FiniteSetEndoMap_N

class FiniteSetEndoMaps_Set(FiniteSetMaps_Set, FiniteSetEndoMaps_N):
    """
    The sets of all maps from a set to itself.

    Users should use the factory class :class:`FiniteSetMaps` to
    create instances of this class.

    INPUT:

    - ``domain`` -- an object in the category ``FiniteSets()``

    - ``category`` -- the category in which the sets of maps is
      constructed. It must be a sub-category of ``Monoids().Finite()``
      and ``EnumeratedSets().Finite()`` which is the default value.
    """
    def __init__(self, domain, action, category=None) -> None:
        '''
        TESTS::

            sage: M = FiniteSetMaps(["a", "b", "c"])
            sage: M.category()
            Category of finite enumerated monoids
            sage: M.__class__
            <class \'sage.sets.finite_set_maps.FiniteSetEndoMaps_Set_with_category\'>
            sage: TestSuite(M).run()
        '''
    Element = FiniteSetEndoMap_Set
