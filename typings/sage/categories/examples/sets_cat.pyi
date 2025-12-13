from _typeshed import Incomplete
from sage.arith.misc import is_prime as is_prime
from sage.categories.sets_cat import Sets as Sets
from sage.misc.abstract_method import abstract_method as abstract_method
from sage.rings.integer import Integer as Integer, IntegerWrapper as IntegerWrapper
from sage.rings.integer_ring import IntegerRing as IntegerRing
from sage.structure.element import Element as Element
from sage.structure.element_wrapper import ElementWrapper as ElementWrapper
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class PrimeNumbers(UniqueRepresentation, Parent):
    '''
    An example of parent in the category of sets: the set of prime numbers.

    The elements are represented as plain integers in `\\ZZ` (facade
    implementation).

    This is a minimal implementations. For more advanced examples of
    implementations, see also::

        sage: P = Sets().example("facade")
        sage: P = Sets().example("inherits")
        sage: P = Sets().example("wrapper")

    EXAMPLES::

        sage: P = Sets().example()
        sage: P(12)
        Traceback (most recent call last):
        ...
        AssertionError: 12 is not a prime number
        sage: a = P.an_element()
        sage: a.parent()
        Integer Ring
        sage: x = P(13); x
        13
        sage: type(x)
        <class \'sage.rings.integer.Integer\'>
        sage: x.parent()
        Integer Ring
        sage: 13 in P
        True
        sage: 12 in P
        False
        sage: y = x+1; y
        14
        sage: type(y)
        <class \'sage.rings.integer.Integer\'>

        sage: TestSuite(P).run(verbose=True)
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
        running ._test_eq() . . . pass
        running ._test_new() . . . pass
        running ._test_not_implemented_methods() . . . pass
        running ._test_pickling() . . . pass
        running ._test_some_elements() . . . pass
    '''
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.categories.examples.sets_cat import PrimeNumbers
            sage: P = PrimeNumbers()
            sage: P.category()
            Category of facade sets
            sage: P is Sets().example()
            True
        """
    def an_element(self):
        """
        Implement :meth:`Sets.ParentMethods.an_element`.

        TESTS::

            sage: P = Sets().example()
            sage: x = P.an_element(); x
            47
            sage: x.parent()
            Integer Ring
        """
    def __contains__(self, p) -> bool:
        """
        TESTS::

            sage: P = Sets().example()
            sage: 13 in P
            True
            sage: 12 in P
            False
        """
    element_class = Integer

class PrimeNumbers_Abstract(UniqueRepresentation, Parent):
    '''
    This class shows how to write a parent while keeping the choice of the
    datastructure for the children open. Different class with fixed
    datastructure will then be constructed by inheriting from
    :class:`PrimeNumbers_Abstract`.

    This is used by::

        sage: P = Sets().example("facade")
        sage: P = Sets().example("inherits")
        sage: P = Sets().example("wrapper")
    '''
    def __init__(self) -> None:
        '''
        TESTS::

            sage: P = Sets().example("inherits")
        '''
    def an_element(self):
        '''
        Implement :meth:`Sets.ParentMethods.an_element`.

        TESTS::

            sage: P = Sets().example("inherits")
            sage: x = P.an_element(); x
            47
            sage: x.parent()
            Set of prime numbers
        '''
    def next(self, i):
        '''
        Return the next prime number.

        EXAMPLES::

            sage: P = Sets().example("inherits")
            sage: x = P.next(P.an_element()); x
            53
            sage: x.parent()
            Set of prime numbers
        '''
    def some_elements(self):
        '''
        Return some prime numbers.

        EXAMPLES::

            sage: P = Sets().example("inherits")
            sage: P.some_elements()
            [47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        '''
    class Element(Element):
        def is_prime(self):
            '''
            Return whether ``self`` is a prime number.

            EXAMPLES::

                sage: P = Sets().example("inherits")
                sage: x = P.an_element()
                sage: P.an_element().is_prime()
                True
            '''
        def next(self):
            '''
            Return the next prime number.

            EXAMPLES::

                sage: P = Sets().example("inherits")
                sage: p = P.an_element(); p
                47
                sage: p.next()
                53

            .. NOTE::

                This method is not meant to implement the protocol iterator,
                and thus not subject to Python 2 vs Python 3 incompatibilities.
            '''

class PrimeNumbers_Inherits(PrimeNumbers_Abstract):
    '''
    An example of parent in the category of sets: the set of prime numbers.
    In this implementation, the element are stored as object of a new class
    which inherits from the class Integer (technically :class:`IntegerWrapper`).

    EXAMPLES::

        sage: P = Sets().example("inherits")
        sage: P
        Set of prime numbers
        sage: P(12)
        Traceback (most recent call last):
        ...
        ValueError: 12 is not a prime number
        sage: a = P.an_element()
        sage: a.parent()
        Set of prime numbers
        sage: x = P(13); x
        13
        sage: x.is_prime()
        True
        sage: type(x)
        <class \'sage.categories.examples.sets_cat.PrimeNumbers_Inherits_with_category.element_class\'>
        sage: x.parent()
        Set of prime numbers
        sage: P(13) in P
        True
        sage: y = x+1; y
        14
        sage: type(y)
        <class \'sage.rings.integer.Integer\'>
        sage: y.parent()
        Integer Ring
        sage: type(P(13)+P(17))
        <class \'sage.rings.integer.Integer\'>
        sage: type(P(2)+P(3))
        <class \'sage.rings.integer.Integer\'>

        sage: z = P.next(x); z
        17
        sage: type(z)
        <class \'sage.categories.examples.sets_cat.PrimeNumbers_Inherits_with_category.element_class\'>
        sage: z.parent()
        Set of prime numbers

        sage: TestSuite(P).run(verbose=True)
        running ._test_an_element() . . . pass
        running ._test_cardinality() . . . pass
        running ._test_category() . . . pass
        running ._test_construction() . . . pass
        running ._test_elements() . . .
          Running the test suite of self.an_element()
          running ._test_category() . . . pass
          running ._test_eq() . . . pass
          running ._test_new() . . . pass
          running ._test_not_implemented_methods() . . . pass
          running ._test_pickling() . . . pass
          pass
        running ._test_elements_eq_reflexive() . . . pass
        running ._test_elements_eq_symmetric() . . . pass
        running ._test_elements_eq_transitive() . . . pass
        running ._test_elements_neq() . . . pass
        running ._test_eq() . . . pass
        running ._test_new() . . . pass
        running ._test_not_implemented_methods() . . . pass
        running ._test_pickling() . . . pass
        running ._test_some_elements() . . . pass

    See also::

        sage: P = Sets().example("facade")
        sage: P = Sets().example("inherits")
        sage: P = Sets().example("wrapper")
    '''
    def __init__(self) -> None:
        '''
        TESTS::

            sage: P = Sets().example("inherits")
            sage: type(P(13)+P(17))
            <class \'sage.rings.integer.Integer\'>
            sage: type(P(2)+P(3))
            <class \'sage.rings.integer.Integer\'>
        '''
    def __contains__(self, p) -> bool:
        '''
        TESTS::

            sage: P = Sets().example("inherits")
            sage: 13 in P, P(13) in P
            (True, True)
            sage: 12 in P
            False
        '''
    class Element(IntegerWrapper, PrimeNumbers_Abstract.Element):
        def __init__(self, parent, p) -> None:
            '''
            TESTS::

                sage: P = Sets().example("inherits")
                sage: P(12)
                Traceback (most recent call last):
                ...
                ValueError: 12 is not a prime number
                sage: x = P(13); type(x)
                <class \'sage.categories.examples.sets_cat.PrimeNumbers_Inherits_with_category.element_class\'>
                sage: x.parent() is P
                True
            '''

class PrimeNumbers_Wrapper(PrimeNumbers_Abstract):
    '''
    An example of parent in the category of sets: the set of prime numbers.

    In this second alternative implementation, the prime integer are stored as
    a attribute of a sage object by inheriting from :class:`ElementWrapper`.  In
    this case we need to ensure conversion and coercion from this parent and
    its element to ``ZZ`` and ``Integer``.

    EXAMPLES::

        sage: P = Sets().example("wrapper")
        sage: P(12)
        Traceback (most recent call last):
        ...
        ValueError: 12 is not a prime number
        sage: a = P.an_element()
        sage: a.parent()
        Set of prime numbers (wrapper implementation)
        sage: x = P(13); x
        13
        sage: type(x)
        <class \'sage.categories.examples.sets_cat.PrimeNumbers_Wrapper_with_category.element_class\'>
        sage: x.parent()
        Set of prime numbers (wrapper implementation)
        sage: 13 in P
        True
        sage: 12 in P
        False
        sage: y = x+1; y
        14
        sage: type(y)
        <class \'sage.rings.integer.Integer\'>

        sage: z = P.next(x); z
        17
        sage: type(z)
        <class \'sage.categories.examples.sets_cat.PrimeNumbers_Wrapper_with_category.element_class\'>
        sage: z.parent()
        Set of prime numbers (wrapper implementation)

    TESTS::

        sage: TestSuite(P).run()
    '''
    mor: Incomplete
    def __init__(self) -> None:
        '''
        TESTS::

            sage: P = Sets().example("wrapper")
            sage: P.category()
            Category of sets
            sage: P(13) == 13
            True
            sage: ZZ(P(13)) == 13
            True
            sage: P(13) + 1 == 14
            True
        '''
    def __contains__(self, p) -> bool:
        '''
        TESTS::

            sage: P = Sets().example("wrapper")
            sage: 13 in P
            True
            sage: 12 in P
            False
        '''
    class Element(ElementWrapper, PrimeNumbers_Abstract.Element): ...

class PrimeNumbers_Facade(PrimeNumbers_Abstract):
    '''
    An example of parent in the category of sets: the set of prime numbers.

    In this alternative implementation, the elements are represented
    as plain integers in `\\ZZ` (facade implementation).

    EXAMPLES::

        sage: P = Sets().example("facade")
        sage: P(12)
        Traceback (most recent call last):
        ...
        ValueError: 12 is not a prime number
        sage: a = P.an_element()
        sage: a.parent()
        Integer Ring
        sage: x = P(13); x
        13
        sage: type(x)
        <class \'sage.rings.integer.Integer\'>
        sage: x.parent()
        Integer Ring
        sage: 13 in P
        True
        sage: 12 in P
        False
        sage: y = x+1; y
        14
        sage: type(y)
        <class \'sage.rings.integer.Integer\'>

        sage: z = P.next(x); z
        17
        sage: type(z)
        <class \'sage.rings.integer.Integer\'>
        sage: z.parent()
        Integer Ring

    The disadvantage of this implementation is that the elements do not know
    that they are prime, so that prime testing is slow::

        sage: pf = Sets().example("facade").an_element()
        sage: timeit("pf.is_prime()") #    random
        625 loops, best of 3: 4.1 us per loop

    compared to the other implementations where prime testing is only done if
    needed during the construction of the element, and later on the elements
    "know" that they are prime::

        sage: pw = Sets().example("wrapper").an_element()
        sage: timeit("pw.is_prime()")    # random
        625 loops, best of 3: 859 ns per loop

        sage: pi = Sets().example("inherits").an_element()
        sage: timeit("pw.is_prime()")    # random
        625 loops, best of 3: 854 ns per loop

    Note also that the ``next`` method for the elements does not exist::

        sage: pf.next()
        Traceback (most recent call last):
        ...
        AttributeError: \'sage.rings.integer.Integer\' object has no attribute \'next\'...

    unlike in the other implementations::

        sage: pw.next()
        53
        sage: pi.next()
        53

    TESTS::

        sage: TestSuite(P).run(verbose = True)
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
        running ._test_eq() . . . pass
        running ._test_new() . . . pass
        running ._test_not_implemented_methods() . . . pass
        running ._test_pickling() . . . pass
        running ._test_some_elements() . . . pass
    '''
    def __init__(self) -> None:
        '''
        TESTS::

            sage: P = Sets().example("inherits")
        '''
    def __contains__(self, p) -> bool:
        '''
        TESTS::

            sage: P = Sets().example("facade")
            sage: 13 in P
            True
            sage: 12 in P
            False
        '''
    element_class = Integer
