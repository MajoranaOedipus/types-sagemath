from _typeshed import Incomplete
from sage.categories.monoids import Monoids as Monoids
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.sets.family import Family as Family
from sage.structure.element_wrapper import ElementWrapper as ElementWrapper
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class IntegerModMonoid(UniqueRepresentation, Parent):
    """
    An example of a finite monoid: the integers mod `n`.

    This class illustrates a minimal implementation of a finite monoid.

    EXAMPLES::

        sage: S = FiniteMonoids().example(); S
        An example of a finite multiplicative monoid: the integers modulo 12

        sage: S.category()
        Category of finitely generated finite enumerated monoids

    We conclude by running systematic tests on this monoid::

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
        running ._test_one() . . . pass
        running ._test_pickling() . . . pass
        running ._test_prod() . . . pass
        running ._test_some_elements() . . . pass
    """
    n: Incomplete
    def __init__(self, n: int = 12) -> None:
        """
        EXAMPLES::

            sage: M = FiniteMonoids().example(6); M
            An example of a finite multiplicative monoid: the integers modulo 6

        TESTS::

            sage: TestSuite(M).run()
        """
    def semigroup_generators(self):
        """

        Returns a set of generators for ``self``, as per
        :meth:`Semigroups.ParentMethods.semigroup_generators`.
        Currently this returns all integers mod `n`, which is of
        course far from optimal!

        EXAMPLES::

            sage: M = FiniteMonoids().example()
            sage: M.semigroup_generators()
            Family (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
        """
    @cached_method
    def one(self):
        """
        Return the one of the monoid, as per :meth:`Monoids.ParentMethods.one`.

        EXAMPLES::

            sage: M = FiniteMonoids().example()
            sage: M.one()
            1
        """
    def product(self, x, y):
        """
        Return the product of two elements `x` and `y` of the monoid, as
        per :meth:`Semigroups.ParentMethods.product`.

        EXAMPLES::

            sage: M = FiniteMonoids().example()
            sage: M.product(M(3), M(5))
            3
        """
    def an_element(self):
        """
        Return an element of the monoid, as per :meth:`Sets.ParentMethods.an_element`.

        EXAMPLES::

            sage: M = FiniteMonoids().example()
            sage: M.an_element()
            6
        """
    class Element(ElementWrapper):
        wrapped_class = Integer
Example = IntegerModMonoid
