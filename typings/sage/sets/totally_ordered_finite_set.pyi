from _typeshed import Incomplete
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.categories.posets import Posets as Posets
from sage.sets.finite_enumerated_set import FiniteEnumeratedSet as FiniteEnumeratedSet
from sage.structure.element import Element as Element
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import rich_to_bool as rich_to_bool, richcmp as richcmp

class TotallyOrderedFiniteSetElement(Element):
    """
    Element of a finite totally ordered set.

    EXAMPLES::

        sage: S = TotallyOrderedFiniteSet([2,7], facade=False)
        sage: x = S(2)
        sage: print(x)
        2
        sage: x.parent()
        {2, 7}
    """
    value: Incomplete
    def __init__(self, parent, data) -> None:
        """
        TESTS::

            sage: T = TotallyOrderedFiniteSet([3,2,1], facade=False)
            sage: TestSuite(T.an_element()).run()
        """
    def __eq__(self, other):
        """
        Equality.

        EXAMPLES::

            sage: A = TotallyOrderedFiniteSet(['gaga',1], facade=False)
            sage: A('gaga') == 'gaga' #indirect doctest
            False
            sage: 'gaga' == A('gaga')
            False
            sage: A('gaga') == A('gaga')
            True
        """
    def __ne__(self, other):
        """
        Non-equality.

        EXAMPLES::

            sage: A = TotallyOrderedFiniteSet(['gaga',1], facade=False)
            sage: A('gaga') != 'gaga' #indirect doctest
            True
        """

class TotallyOrderedFiniteSet(FiniteEnumeratedSet):
    """
    Totally ordered finite set.

    This is a finite enumerated set assuming that the elements are
    ordered based upon their rank (i.e. their position in the set).

    INPUT:

    - ``elements`` -- list of elements in the set

    - ``facade`` -- boolean (default: ``True``); if ``True``, a facade is used.
      It should be set to ``False`` if the elements do not inherit from
      :class:`~sage.structure.element.Element` or if you want a funny order. See
      examples for more details.

    .. SEEALSO::

        :class:`FiniteEnumeratedSet`

    EXAMPLES::

        sage: S = TotallyOrderedFiniteSet([1,2,3])
        sage: S
        {1, 2, 3}
        sage: S.cardinality()
        3

    By default, totally ordered finite set behaves as a facade::

        sage: S(1).parent()
        Integer Ring

    It makes comparison fails when it is not the standard order::

        sage: T1 = TotallyOrderedFiniteSet([3,2,5,1])
        sage: T1(3) < T1(1)
        False
        sage: T2 = TotallyOrderedFiniteSet([3, x])                                      # needs sage.symbolic
        sage: T2(3) < T2(x)                                                             # needs sage.symbolic
        3 < x

    To make the above example work, you should set the argument facade to
    ``False`` in the constructor. In that case, the elements of the set have a
    dedicated class::

        sage: A = TotallyOrderedFiniteSet([3,2,0,'a',7,(0,0),1], facade=False)
        sage: A
        {3, 2, 0, 'a', 7, (0, 0), 1}
        sage: x = A.an_element()
        sage: x
        3
        sage: x.parent()
        {3, 2, 0, 'a', 7, (0, 0), 1}
        sage: A(3) < A(2)
        True
        sage: A('a') < A(7)
        True
        sage: A(3) > A(2)
        False
        sage: A(1) < A(3)
        False
        sage: A(3) == A(3)
        True

    But then, the equality comparison is always False with elements outside of
    the set::

        sage: A(1) == 1
        False
        sage: 1 == A(1)
        False
        sage: 'a' == A('a')
        False
        sage: A('a') == 'a'
        False

    Since :issue:`16280`, totally ordered sets support elements that do
    not inherit from :class:`sage.structure.element.Element`, whether
    they are facade or not::

        sage: S = TotallyOrderedFiniteSet(['a','b'])
        sage: S('a')
        'a'
        sage: S = TotallyOrderedFiniteSet(['a','b'], facade = False)
        sage: S('a')
        'a'

    Multiple elements are automatically deleted::

        sage: TotallyOrderedFiniteSet([1,1,2,1,2,2,5,4])
        {1, 2, 5, 4}
    """
    Element = TotallyOrderedFiniteSetElement
    @staticmethod
    def __classcall__(cls, iterable, facade: bool = True):
        """
        Standard trick to expand the iterable upon input, and
        guarantees unique representation, independently of the type of
        the iterable. See ``UniqueRepresentation``.

        TESTS::

            sage: S1 = TotallyOrderedFiniteSet([1, 2, 3])
            sage: S2 = TotallyOrderedFiniteSet((1, 2, 3))
            sage: S3 = TotallyOrderedFiniteSet(range(1,4))
            sage: S1 is S2
            True
            sage: S2 is S3
            True
        """
    def __init__(self, elements, facade: bool = True) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: TestSuite(TotallyOrderedFiniteSet([1,2,3])).run()
            sage: TestSuite(TotallyOrderedFiniteSet([1,2,3],facade=False)).run()
            sage: TestSuite(TotallyOrderedFiniteSet([1,3,2],facade=False)).run()
            sage: TestSuite(TotallyOrderedFiniteSet([])).run()
        """
    def le(self, x, y):
        """
        Return ``True`` if `x \\le y` for the order of ``self``.

        EXAMPLES::

            sage: T = TotallyOrderedFiniteSet([1,3,2], facade=False)
            sage: T1, T3, T2 = T.list()
            sage: T.le(T1,T3)
            True
            sage: T.le(T3,T2)
            True
        """
