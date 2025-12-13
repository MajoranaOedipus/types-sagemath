from sage.categories.monoids import Monoids as Monoids
from sage.categories.sets_cat import Sets as Sets
from sage.rings.infinity import infinity as infinity
from sage.rings.integer_ring import ZZ as ZZ
from sage.sets.finite_enumerated_set import FiniteEnumeratedSet as FiniteEnumeratedSet
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class PositiveIntegerMonoid(UniqueRepresentation, Parent):
    """

    An example of a facade parent: the positive integers viewed as a
    multiplicative monoid

    This class illustrates a minimal implementation of a facade parent
    which models a subset of a set.

    EXAMPLES::

        sage: S = Sets().Facade().example(); S
        An example of facade set: the monoid of positive integers

    TESTS::

        sage: TestSuite(S).run(verbose = True)
        running ._test_an_element() . . . pass
        running ._test_associativity() . . . pass
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
        running ._test_one() . . . pass
        running ._test_pickling() . . . pass
        running ._test_prod() . . . pass
        running ._test_some_elements() . . . pass
    """
    def __init__(self) -> None:
        """
        EXAMPLES::

            sage: from sage.categories.examples.facade_sets import PositiveIntegerMonoid
            sage: S = PositiveIntegerMonoid(); S
            An example of facade set: the monoid of positive integers

        TESTS::

            sage: TestSuite(S).run()
        """

class IntegersCompletion(UniqueRepresentation, Parent):
    '''
    An example of a facade parent: the set of integers completed with
    `+-\\infty`

    This class illustrates a minimal implementation of a facade parent
    that models the union of several other parents.

    EXAMPLES::

        sage: S = Sets().Facade().example("union"); S
        An example of a facade set: the integers completed by +-infinity

    TESTS::

        sage: TestSuite(S).run(verbose = True)
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
        EXAMPLES::

            sage: from sage.categories.examples.facade_sets import IntegersCompletion
            sage: S = IntegersCompletion(); S
            An example of a facade set: the integers completed by +-infinity

        TESTS::

            sage: TestSuite(S).run()
        """
