from sage.rings.integer import Integer as Integer
from sage.sets.integer_range import IntegerRangeInfinite as IntegerRangeInfinite

class PositiveIntegers(IntegerRangeInfinite):
    """
    The enumerated set of positive integers. To fix the ideas,
    we mean `\\{1, 2, 3, 4, 5, \\dots \\}`.

    This class implements the set of positive integers, as an
    enumerated set (see :class:`InfiniteEnumeratedSets
    <sage.categories.infinite_enumerated_sets.InfiniteEnumeratedSets>`).

    This set is an integer range set. The construction is
    therefore done by IntegerRange (see :class:`IntegerRange
    <sage.sets.integer_range.IntegerRange>`).

    EXAMPLES::

        sage: PP = PositiveIntegers()
        sage: PP
        Positive integers
        sage: PP.cardinality()
        +Infinity
        sage: TestSuite(PP).run()
        sage: PP.list()
        Traceback (most recent call last):
        ...
        NotImplementedError: cannot list an infinite set
        sage: it = iter(PP)
        sage: (next(it), next(it), next(it), next(it), next(it))
        (1, 2, 3, 4, 5)
        sage: PP.first()
        1

    TESTS::

        sage: TestSuite(PositiveIntegers()).run()
    """
    def __init__(self) -> None:
        """
        EXAMPLES::

            sage: PP = PositiveIntegers()
            sage: PP.category()
            Category of facade infinite enumerated sets
        """
    def an_element(self):
        """
        Return an element of ``self``.

        EXAMPLES::

            sage: PositiveIntegers().an_element()
            42
        """
