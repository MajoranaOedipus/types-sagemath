from sage.categories.infinite_enumerated_sets import InfiniteEnumeratedSets as InfiniteEnumeratedSets
from sage.rings.integer import Integer as Integer
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class NonNegativeIntegers(UniqueRepresentation, Parent):
    '''
    The enumerated set of nonnegative integers.

    This class implements the set of nonnegative integers, as an
    enumerated set (see :class:`InfiniteEnumeratedSets
    <sage.categories.infinite_enumerated_sets.InfiniteEnumeratedSets>`).

    EXAMPLES::

        sage: NN = NonNegativeIntegers()
        sage: NN
        Non negative integers
        sage: NN.cardinality()
        +Infinity
        sage: TestSuite(NN).run()
        sage: NN.list()
        Traceback (most recent call last):
        ...
        NotImplementedError: cannot list an infinite set
        sage: NN.element_class
        <... \'sage.rings.integer.Integer\'>
        sage: it = iter(NN)
        sage: [next(it), next(it), next(it), next(it), next(it)]
        [0, 1, 2, 3, 4]
        sage: NN.first()
        0

    Currently, this is just a "facade" parent; namely its elements are
    plain Sage ``Integers`` with ``Integer Ring`` as parent::

        sage: x = NN(15); type(x)
        <... \'sage.rings.integer.Integer\'>
        sage: x.parent()
        Integer Ring
        sage: x+3
        18

    In a later version, there will be an option to specify whether the
    elements should have ``Integer Ring`` or ``Non negative integers``
    as parent::

        sage: NN = NonNegativeIntegers(facade = False) # todo: not implemented
        sage: x = NN(5)                                # todo: not implemented
        sage: x.parent()                               # todo: not implemented
        Non negative integers

    This runs generic sanity checks on ``NN``::

        sage: TestSuite(NN).run()

    TODO: do not use ``NN`` any more in the doctests for
    ``NonNegativeIntegers``.
    '''
    def __init__(self, category=None) -> None:
        """
        TESTS::

            sage: NN = NonNegativeIntegers()
            sage: NN
            Non negative integers
            sage: NN.category()
            Category of facade infinite enumerated sets
            sage: TestSuite(NN).run()
        """
    def __contains__(self, elt) -> bool:
        """
        EXAMPLES::

            sage: NN = NonNegativeIntegers()
            sage: 1 in NN
            True
            sage: -1 in NN
            False
            sage: x in NN                                                               # needs sage.symbolic
            False
            sage: None in NN
            False
            sage: QQbar(sqrt(2)) in NN                                                  # needs sage.rings.number_field sage.symbolic
            False
            sage: RIF(1,2) in NN                                                        # needs sage.rings.real_interval_field
            False
            sage: QQbar(2) in NN                                                        # needs sage.rings.number_field
            True
            sage: RIF(2) in NN                                                          # needs sage.rings.real_interval_field
            True
        """
    from_integer = Integer
    Element = Integer
    def __iter__(self):
        """
        EXAMPLES::

            sage: NN = NonNegativeIntegers()
            sage: g = iter(NN)
            sage: next(g), next(g), next(g), next(g)
            (0, 1, 2, 3)
        """
    def an_element(self):
        """
        EXAMPLES::

            sage: NonNegativeIntegers().an_element()
            42
        """
    def some_elements(self):
        """
        EXAMPLES::

            sage: NonNegativeIntegers().some_elements()
            [0, 1, 3, 42]
        """
    def next(self, o):
        """
        EXAMPLES::

            sage: NN = NonNegativeIntegers()
            sage: NN.next(3)
            4
        """
    def unrank(self, rnk):
        """
        EXAMPLES::

            sage: NN = NonNegativeIntegers()
            sage: NN.unrank(100)
            100
        """
