from _typeshed import Incomplete
from sage.categories.posets import Posets as Posets
from sage.sets.positive_integers import PositiveIntegers as PositiveIntegers
from sage.sets.set import Set as Set, Set_object_enumerated as Set_object_enumerated
from sage.structure.element_wrapper import ElementWrapper as ElementWrapper
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class FiniteSetsOrderedByInclusion(UniqueRepresentation, Parent):
    """
    An example of a poset: finite sets ordered by inclusion.

    This class provides a minimal implementation of a poset

    EXAMPLES::

        sage: P = Posets().example(); P
        An example of a poset: sets ordered by inclusion

    We conclude by running systematic tests on this poset::

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
    """
    def __init__(self) -> None:
        """
        EXAMPLES::

            sage: P = Posets().example(); P
            An example of a poset: sets ordered by inclusion
            sage: P.category()
            Category of posets
            sage: type(P)
            <class 'sage.categories.examples.posets.FiniteSetsOrderedByInclusion_with_category'>
            sage: TestSuite(P).run()
        """
    def le(self, x, y):
        """
        Return whether `x` is a subset of `y`.

        EXAMPLES::

            sage: P = Posets().example()
            sage: P.le( P(Set([1,3])), P(Set([1,2,3])) )
            True
            sage: P.le( P(Set([1,3])), P(Set([1,3])) )
            True
            sage: P.le( P(Set([1,2])), P(Set([1,3])) )
            False
        """
    def an_element(self):
        """
        Return an element of this poset.

        EXAMPLES::

            sage: B = Posets().example()
            sage: B.an_element()
            {1, 4, 6}
        """
    class Element(ElementWrapper):
        wrapped_class = Set_object_enumerated

class PositiveIntegersOrderedByDivisibilityFacade(UniqueRepresentation, Parent):
    '''
    An example of a facade poset: the positive integers ordered by divisibility.

    This class provides a minimal implementation of a facade poset

    EXAMPLES::

        sage: P = Posets().example("facade"); P
        An example of a facade poset: the positive integers ordered by divisibility

        sage: P(5)
        5
        sage: P(0)
        Traceback (most recent call last):
        ...
        ValueError: Can\'t coerce `0` in any parent `An example of a facade poset: the positive integers ordered by divisibility` is a facade for

        sage: 3 in P
        True
        sage: 0 in P
        False
    '''
    element_class: Incomplete
    def __init__(self) -> None:
        '''
        EXAMPLES::

            sage: P = Posets().example("facade"); P
            An example of a facade poset: the positive integers ordered by divisibility
            sage: P.category()
            Category of facade posets
            sage: type(P)
            <class \'sage.categories.examples.posets.PositiveIntegersOrderedByDivisibilityFacade_with_category\'>
            sage: TestSuite(P).run()
        '''
    def le(self, x, y):
        '''
        Return whether `x` is divisible by `y`.

        EXAMPLES::

            sage: P = Posets().example("facade")
            sage: P.le(3, 6)
            True
            sage: P.le(3, 3)
            True
            sage: P.le(3, 7)
            False
        '''
