from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.categories.infinite_enumerated_sets import InfiniteEnumeratedSets as InfiniteEnumeratedSets
from sage.rings.infinity import Infinity as Infinity, MinusInfinity as MinusInfinity, PlusInfinity as PlusInfinity
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import IntegerRing as IntegerRing
from sage.sets.finite_enumerated_set import FiniteEnumeratedSet as FiniteEnumeratedSet
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class IntegerRange(UniqueRepresentation, Parent):
    """
    The class of :class:`Integer <sage.rings.integer.Integer>` ranges.

    Returns an enumerated set containing an arithmetic progression of integers.

    INPUT:

    - ``begin`` -- integer, Infinity or -Infinity
    - ``end`` -- integer, Infinity or -Infinity
    - ``step`` -- a nonzero integer (default: 1)
    - ``middle_point`` -- integer inside the set (default: ``None``)

    OUTPUT:

    A parent in the category :class:`FiniteEnumeratedSets()
    <sage.categories.finite_enumerated_sets.FiniteEnumeratedSets>` or
    :class:`InfiniteEnumeratedSets()
    <sage.categories.infinite_enumerated_sets.InfiniteEnumeratedSets>`
    depending on the arguments defining ``self``.

    ``IntegerRange(i, j)`` returns the set of `\\{i, i+1, i+2, \\dots , j-1\\}`.
    ``start`` (!) defaults to 0. When ``step`` is given, it specifies the
    increment. The default increment is `1`. IntegerRange allows ``begin`` and
    ``end`` to be infinite.

    ``IntegerRange`` is designed to have similar interface Python
    range. However, whereas ``range`` accept and returns Python ``int``,
    ``IntegerRange`` deals with :class:`Integer <sage.rings.integer.Integer>`.

    If ``middle_point`` is given, then the elements are generated starting
    from it, in a alternating way: `\\{m, m+1, m-2, m+2, m-2 \\dots \\}`.

    EXAMPLES::

        sage: list(IntegerRange(5))
        [0, 1, 2, 3, 4]
        sage: list(IntegerRange(2,5))
        [2, 3, 4]
        sage: I = IntegerRange(2,100,5); I
        {2, 7, ..., 97}
        sage: list(I)
        [2, 7, 12, 17, 22, 27, 32, 37, 42, 47, 52, 57, 62, 67, 72, 77, 82, 87, 92, 97]
        sage: I.category()
        Category of facade finite enumerated sets
        sage: I[1].parent()
        Integer Ring

    When ``begin`` and ``end`` are both finite, ``IntegerRange(begin, end,
    step)`` is the set whose list of elements is equivalent to the python
    construction ``range(begin, end, step)``::

        sage: list(IntegerRange(4,105,3)) == list(range(4,105,3))
        True
        sage: list(IntegerRange(-54,13,12)) == list(range(-54,13,12))
        True

    Except for the type of the numbers::

        sage: type(IntegerRange(-54,13,12)[0]), type(list(range(-54,13,12))[0])
        (<... 'sage.rings.integer.Integer'>, <... 'int'>)

    When ``begin`` is finite and ``end`` is +Infinity, ``self`` is the infinite
    arithmetic progression starting from the ``begin`` by step ``step``::

        sage: I = IntegerRange(54,Infinity,3); I
        {54, 57, ...}
        sage: I.category()
        Category of facade infinite enumerated sets
        sage: p = iter(I)
        sage: (next(p), next(p), next(p), next(p), next(p), next(p))
        (54, 57, 60, 63, 66, 69)

        sage: I = IntegerRange(54,-Infinity,-3); I
        {54, 51, ...}
        sage: I.category()
        Category of facade infinite enumerated sets
        sage: p = iter(I)
        sage: (next(p), next(p), next(p), next(p), next(p), next(p))
        (54, 51, 48, 45, 42, 39)

    When ``begin`` and ``end`` are both infinite, you will have to specify the
    extra argument ``middle_point``. ``self`` is then defined by a point
    and a progression/regression setting by ``step``. The enumeration
    is done this way: (let us call `m` the ``middle_point``)
    `\\{m, m+step, m-step, m+2step, m-2step, m+3step, \\dots \\}`::

        sage: I = IntegerRange(-Infinity,Infinity,37,-12); I
        Integer progression containing -12 with increment 37 and bounded with -Infinity and +Infinity
        sage: I.category()
        Category of facade infinite enumerated sets
        sage: -12 in I
        True
        sage: -15 in I
        False
        sage: p = iter(I)
        sage: (next(p), next(p), next(p), next(p), next(p), next(p), next(p), next(p))
        (-12, 25, -49, 62, -86, 99, -123, 136)

    It is also possible to use the argument ``middle_point`` for other cases, finite
    or infinite. The set will be the same as if you didn't give this extra argument
    but the enumeration will begin with this ``middle_point``::

        sage: I = IntegerRange(123,-12,-14); I
        {123, 109, ..., -3}
        sage: list(I)
        [123, 109, 95, 81, 67, 53, 39, 25, 11, -3]
        sage: J = IntegerRange(123,-12,-14,25); J
        Integer progression containing 25 with increment -14 and bounded with 123 and -12
        sage: list(J)
        [25, 11, 39, -3, 53, 67, 81, 95, 109, 123]

    Remember that, like for range, if you define a non empty set, ``begin`` is
    supposed to be included and ``end`` is supposed to be excluded. In the same
    way, when you define a set with a ``middle_point``, the ``begin`` bound will
    be supposed to be included and the ``end`` bound supposed to be excluded::

        sage: I = IntegerRange(-100,100,10,0)
        sage: J = list(range(-100,100,10))
        sage: 100 in I
        False
        sage: 100 in J
        False
        sage: -100 in I
        True
        sage: -100 in J
        True
        sage: list(I)
        [0, 10, -10, 20, -20, 30, -30, 40, -40, 50, -50, 60, -60, 70, -70, 80, -80, 90, -90, -100]


    .. NOTE::

       The input is normalized so that::

        sage: IntegerRange(1, 6, 2) is IntegerRange(1, 7, 2)
        True
        sage: IntegerRange(1, 8, 3) is IntegerRange(1, 10, 3)
        True

    TESTS::

        sage: # Some category automatic tests
        sage: TestSuite(IntegerRange(2,100,3)).run()
        sage: TestSuite(IntegerRange(564,-12,-46)).run()
        sage: TestSuite(IntegerRange(2,Infinity,3)).run()
        sage: TestSuite(IntegerRange(732,-Infinity,-13)).run()
        sage: TestSuite(IntegerRange(-Infinity,Infinity,3,2)).run()
        sage: TestSuite(IntegerRange(56,Infinity,12,80)).run()
        sage: TestSuite(IntegerRange(732,-12,-2743,732)).run()
        sage: # 20 random tests: range and IntegerRange give the same set for finite cases
        sage: for i in range(20):
        ....:     begin = Integer(randint(-300,300))
        ....:     end = Integer(randint(-300,300))
        ....:     step = Integer(randint(-20,20))
        ....:     if step == 0:
        ....:         step = Integer(1)
        ....:     assert list(IntegerRange(begin, end, step)) == list(range(begin, end, step))
        sage: # 20 random tests: range and IntegerRange with middle point for finite cases
        sage: for i in range(20):
        ....:     begin = Integer(randint(-300,300))
        ....:     end = Integer(randint(-300,300))
        ....:     step = Integer(randint(-15,15))
        ....:     if step == 0:
        ....:         step = Integer(-3)
        ....:     I = IntegerRange(begin, end, step)
        ....:     if I.cardinality() == 0:
        ....:         assert len(range(begin, end, step)) == 0
        ....:     else:
        ....:         TestSuite(I).run()
        ....:         L1 = list(IntegerRange(begin, end, step, I.an_element()))
        ....:         L2 = list(range(begin, end, step))
        ....:         L1.sort()
        ....:         L2.sort()
        ....:         assert L1 == L2

    Thanks to :issue:`8543` empty integer range are allowed::

        sage: TestSuite(IntegerRange(0, 5, -1)).run()
    """
    @staticmethod
    def __classcall_private__(cls, begin, end=None, step=..., middle_point=None):
        """
        TESTS::

            sage: IntegerRange(2,5,0)
            Traceback (most recent call last):
            ...
            ValueError: IntegerRange() step argument must not be zero
            sage: IntegerRange(2) is IntegerRange(0, 2)
            True
            sage: IntegerRange(1.0)                                                     # needs sage.rings.real_mpfr
            Traceback (most recent call last):
            ...
            TypeError: end must be Integer or Infinity, not <... 'sage.rings.real_mpfr.RealLiteral'>
        """
    element_class = Integer

class IntegerRangeEmpty(IntegerRange, FiniteEnumeratedSet):
    """
    A singleton class for empty integer ranges.

    See :class:`IntegerRange` for more details.
    """
    @staticmethod
    def __classcall__(cls, *args):
        """
        TESTS::

            sage: from sage.sets.integer_range import IntegerRangeEmpty
            sage: I = IntegerRangeEmpty(); I
            {}
            sage: I.category()
            Category of facade finite enumerated sets
            sage: TestSuite(I).run()
            sage: I(0)
            Traceback (most recent call last):
            ...
            ValueError: 0 not in {}
        """

class IntegerRangeFinite(IntegerRange):
    """
    The class of finite enumerated sets of integers defined by finite
    arithmetic progressions

    See :class:`IntegerRange` for more details.
    """
    def __init__(self, begin, end, step=...) -> None:
        """
        TESTS::

            sage: I = IntegerRange(123,12,-4)
            sage: I.category()
            Category of facade finite enumerated sets
            sage: TestSuite(I).run()
        """
    def __contains__(self, elt) -> bool:
        """
        Return ``True`` if ``elt`` is in ``self``.

        EXAMPLES::

            sage: I = IntegerRange(123,12,-4)
            sage: 123 in I
            True
            sage: 127 in I
            False
            sage: 12 in I
            False
            sage: 13 in I
            False
            sage: 14 in I
            False
            sage: 15 in I
            True
            sage: 11 in I
            False
        """
    def cardinality(self):
        """
        Return the cardinality of ``self``.

        EXAMPLES::

            sage: IntegerRange(123,12,-4).cardinality()
            28
            sage: IntegerRange(-57,12,8).cardinality()
            9
            sage: IntegerRange(123,12,4).cardinality()
            0
        """
    def rank(self, x):
        """
        EXAMPLES::

            sage: I = IntegerRange(-57,36,8)
            sage: I.rank(23)
            10
            sage: I.unrank(10)
            23
            sage: I.rank(22)
            Traceback (most recent call last):
            ...
            IndexError: 22 not in self
            sage: I.rank(87)
            Traceback (most recent call last):
            ...
            IndexError: 87 not in self
        """
    def __getitem__(self, i):
        """
        Return the i-th element of this integer range.

        EXAMPLES::

            sage: I = IntegerRange(1,13,5)
            sage: I[0], I[1], I[2]
            (1, 6, 11)
            sage: I[3]
            Traceback (most recent call last):
            ...
            IndexError: out of range
            sage: I[-1]
            11
            sage: I[-4]
            Traceback (most recent call last):
            ...
            IndexError: out of range

            sage: I = IntegerRange(13,1,-1)
            sage: l = I.list()
            sage: [I[i] for i in range(I.cardinality())] == l
            True
            sage: l.reverse()
            sage: [I[i] for i in range(-1,-I.cardinality()-1,-1)] == l
            True
        """
    unrank = __getitem__
    def __iter__(self):
        """
        Return an iterator over the elements of ``self``.

        EXAMPLES::

            sage: I = IntegerRange(123,12,-4)
            sage: p = iter(I)
            sage: [next(p) for i in range(8)]
            [123, 119, 115, 111, 107, 103, 99, 95]
            sage: I = IntegerRange(-57,12,8)
            sage: p = iter(I)
            sage: [next(p) for i in range(8)]
            [-57, -49, -41, -33, -25, -17, -9, -1]
        """

class IntegerRangeInfinite(IntegerRange):
    """ The class of infinite enumerated sets of integers defined by infinite
    arithmetic progressions.

    See :class:`IntegerRange` for more details.
    """
    def __init__(self, begin, step=...) -> None:
        """
        TESTS::

            sage: I = IntegerRange(-57,Infinity,8)
            sage: I.category()
            Category of facade infinite enumerated sets
            sage: TestSuite(I).run()
        """
    def __contains__(self, elt) -> bool:
        """
        Return ``True`` if ``elt`` is in ``self``.

        EXAMPLES::

            sage: I = IntegerRange(-57,Infinity,8)
            sage: -57 in I
            True
            sage: -65 in I
            False
            sage: -49 in I
            True
            sage: 743 in I
            True
        """
    def rank(self, x):
        """
        EXAMPLES::

            sage: I = IntegerRange(-57,Infinity,8)
            sage: I.rank(23)
            10
            sage: I.unrank(10)
            23
            sage: I.rank(22)
            Traceback (most recent call last):
            ...
            IndexError: 22 not in self
        """
    def __getitem__(self, i):
        """
        Return the ``i``-th element of ``self``.

        EXAMPLES::

            sage: I = IntegerRange(-8,Infinity,3)
            sage: I.unrank(1)
            -5
        """
    unrank = __getitem__
    def __iter__(self):
        """
        Return an iterator over the elements of ``self``.

        EXAMPLES::

            sage: I = IntegerRange(-57,Infinity,8)
            sage: p = iter(I)
            sage: [next(p) for i in range(8)]
            [-57, -49, -41, -33, -25, -17, -9, -1]

            sage: I = IntegerRange(-112,-Infinity,-13)
            sage: p = iter(I)
            sage: [next(p) for i in range(8)]
            [-112, -125, -138, -151, -164, -177, -190, -203]
        """

class IntegerRangeFromMiddle(IntegerRange):
    """
    The class of finite or infinite enumerated sets defined with
    an inside point, a progression and two limits.

    See :class:`IntegerRange` for more details.
    """
    def __init__(self, begin, end, step=..., middle_point=...) -> None:
        """
        TESTS::

            sage: from sage.sets.integer_range import IntegerRangeFromMiddle
            sage: I = IntegerRangeFromMiddle(-100,100,10,0)
            sage: I.category()
            Category of facade finite enumerated sets
            sage: TestSuite(I).run()
            sage: I = IntegerRangeFromMiddle(Infinity,-Infinity,-37,0)
            sage: I.category()
            Category of facade infinite enumerated sets
            sage: TestSuite(I).run()

            sage: IntegerRange(0, 5, 1, -3)
            Traceback (most recent call last):
            ...
            ValueError: middle_point is not in the interval
        """
    def __contains__(self, elt) -> bool:
        """
        Return ``True`` if ``elt`` is in ``self``.

        EXAMPLES::

            sage: from sage.sets.integer_range import IntegerRangeFromMiddle
            sage: I = IntegerRangeFromMiddle(-100,100,10,0)
            sage: -110 in I
            False
            sage: -100 in I
            True
            sage: 30 in I
            True
            sage: 90 in I
            True
            sage: 100 in I
            False
        """
    def next(self, elt):
        """
        Return the next element of ``elt`` in ``self``.

        EXAMPLES::

            sage: from sage.sets.integer_range import IntegerRangeFromMiddle
            sage: I = IntegerRangeFromMiddle(-100,100,10,0)
            sage: (I.next(0), I.next(10), I.next(-10), I.next(20), I.next(-100))
            (10, -10, 20, -20, None)
            sage: I = IntegerRangeFromMiddle(-Infinity,Infinity,10,0)
            sage: (I.next(0), I.next(10), I.next(-10), I.next(20), I.next(-100))
            (10, -10, 20, -20, 110)
            sage: I.next(1)
            Traceback (most recent call last):
            ...
            LookupError: 1 not in Integer progression containing 0 with increment 10 and bounded with -Infinity and +Infinity
        """
    def __iter__(self):
        """
        Return an iterator over the elements of ``self``.

        EXAMPLES::

            sage: from sage.sets.integer_range import IntegerRangeFromMiddle
            sage: I = IntegerRangeFromMiddle(Infinity,-Infinity,-37,0)
            sage: p = iter(I)
            sage: (next(p), next(p), next(p), next(p), next(p), next(p), next(p), next(p))
            (0, -37, 37, -74, 74, -111, 111, -148)
            sage: I = IntegerRangeFromMiddle(-12,214,10,0)
            sage: p = iter(I)
            sage: (next(p), next(p), next(p), next(p), next(p), next(p), next(p), next(p))
            (0, 10, -10, 20, 30, 40, 50, 60)
        """
