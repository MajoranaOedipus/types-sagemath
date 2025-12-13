from sage.categories.infinite_enumerated_sets import InfiniteEnumeratedSets as InfiniteEnumeratedSets
from sage.rings.integer import Integer as Integer
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class NonNegativeIntegers(UniqueRepresentation, Parent):
    """
    An example of infinite enumerated set: the nonnegative integers.

    This class provides a minimal implementation of an infinite enumerated set.

    EXAMPLES::

        sage: NN = InfiniteEnumeratedSets().example()
        sage: NN
        An example of an infinite enumerated set: the nonnegative integers
        sage: NN.cardinality()
        +Infinity
        sage: NN.list()
        Traceback (most recent call last):
        ...
        NotImplementedError: cannot list an infinite set
        sage: NN.element_class
        <class 'sage.rings.integer.Integer'>
        sage: it = iter(NN)
        sage: [next(it), next(it), next(it), next(it), next(it)]
        [0, 1, 2, 3, 4]
        sage: x = next(it); type(x)
        <class 'sage.rings.integer.Integer'>
        sage: x.parent()
        Integer Ring
        sage: x+3
        8
        sage: NN(15)
        15
        sage: NN.first()
        0

    This checks that the different methods of `NN` return consistent
    results::

        sage: TestSuite(NN).run(verbose = True)
        running ._test_an_element() . . . pass
        running ._test_cardinality() . . . pass
        running ._test_category() . . . pass
        running ._test_construction() . . . pass
        running ._test_elements() . . .
          Running the test suite of self.an_element()
          running ._test_category() . . . pass
          running ._test_eq() . . . pass
          running ._test_new() . . . pass
          running ._test_nonzero_equal() . . . pass
          running ._test_not_implemented_methods() . . . pass
          running ._test_pickling() . . . pass
          pass
        running ._test_elements_eq_reflexive() . . . pass
        running ._test_elements_eq_symmetric() . . . pass
        running ._test_elements_eq_transitive() . . . pass
        running ._test_elements_neq() . . . pass
        running ._test_enumerated_set_contains() . . . pass
        running ._test_enumerated_set_iter_cardinality() . . . pass
        running ._test_enumerated_set_iter_list() . . . pass
        running ._test_eq() . . . pass
        running ._test_new() . . . pass
        running ._test_not_implemented_methods() . . . pass
        running ._test_pickling() . . . pass
        running ._test_some_elements() . . . pass
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: NN = InfiniteEnumeratedSets().example()
            sage: NN
            An example of an infinite enumerated set: the nonnegative integers
            sage: NN.category()
            Category of infinite enumerated sets
            sage: TestSuite(NN).run()
        """
    def __contains__(self, elt) -> bool:
        """
        EXAMPLES::

            sage: NN = InfiniteEnumeratedSets().example()
            sage: 1 in NN
            True
            sage: -1 in NN
            False
        """
    def __iter__(self):
        """
        EXAMPLES::

            sage: NN = InfiniteEnumeratedSets().example()
            sage: g = iter(NN)
            sage: next(g), next(g), next(g), next(g)
            (0, 1, 2, 3)
        """
    def __call__(self, elt):
        """
        EXAMPLES::

            sage: NN = InfiniteEnumeratedSets().example()
            sage: NN(3)         # indirect doctest
            3
            sage: NN(3).parent()
            Integer Ring
            sage: NN(-1)
            Traceback (most recent call last):
            ...
            ValueError: Value -1 is not a nonnegative integer.
        """
    def an_element(self):
        """
        EXAMPLES::

            sage: InfiniteEnumeratedSets().example().an_element()
            42
        """
    def next(self, o):
        """
        EXAMPLES::

            sage: NN = InfiniteEnumeratedSets().example()
            sage: NN.next(3)
            4
        """
    Element = Integer
Example = NonNegativeIntegers
