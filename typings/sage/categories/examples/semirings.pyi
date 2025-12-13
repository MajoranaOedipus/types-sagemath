from sage.categories.semirings import Semirings as Semirings
from sage.structure.element import Element as Element
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class Ternary(Element):
    """
    Elements of the ternary-logic ring.

    The semantic is as follows:

    - 0 -- the integer 0
    - 1 -- the integer 1
    - 2 -- some integer greater than 1

    An alternative semantic is:

    - 0 -- an empty set
    - 1 -- a connected set
    - 2 -- a disconnected set

    The same semantic works for graphs instead of sets.
    """
    def __init__(self, parent, n) -> None:
        """
        Initialize one element.

        TESTS::

            sage: from sage.categories.examples.semirings import TernaryLogic
            sage: S = TernaryLogic()
            sage: S(4)
            Traceback (most recent call last):
            ...
            ValueError: input not in (0,1,2)
        """
    def __eq__(self, other):
        """
        Test for equality.

        TESTS::

            sage: from sage.categories.examples.semirings import TernaryLogic
            sage: S = TernaryLogic()
            sage: S(1) == S(2)
            False
            sage: S(0) == 3
            False
        """
    def __ne__(self, other):
        """
        Test for non-equality.

        TESTS::

            sage: from sage.categories.examples.semirings import TernaryLogic
            sage: S = TernaryLogic()
            sage: S(1) != S(2)
            True
        """

class TernaryLogic(UniqueRepresentation, Parent):
    """
    An example of a semiring.

    This class illustrates a minimal implementation of a semiring.

    EXAMPLES::

        sage: S = Semirings().example(); S
        An example of a semiring: the ternary-logic semiring

    This is the semiring that contains 3 objects::

        sage: S.some_elements()
        [0, 1, many]

    The product rule is as expected::

        sage: S(1) * S(1)
        1
        sage: S(1) + S(1)
        many

    TESTS::

        sage: TestSuite(S).run(verbose=True)
        running ._test_additive_associativity() . . . pass
        running ._test_an_element() . . . pass
        running ._test_associativity() . . . pass
        running ._test_cardinality() . . . pass
        running ._test_category() . . . pass
        running ._test_construction() . . . pass
        running ._test_distributivity() . . . pass
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
        running ._test_zero() . . . pass
    """
    def __init__(self) -> None:
        """
        The ternary-logic semiring.

        EXAMPLES::

            sage: S = Semirings().example(); S
            An example of a semiring: the ternary-logic semiring
        """
    def summation(self, x, y):
        """
        Return the sum of ``x`` and ``y`` in the semiring as per
        :meth:`Semirings.ParentMethods.summation`.

        EXAMPLES::

            sage: S = Semirings().example()
            sage: S(1) + S(1)
            many
        """
    def one(self):
        """
        Return the unit of ``self``.

        EXAMPLES::

            sage: S = Semirings().example()
            sage: S.one()
            1
        """
    def product(self, x, y):
        """
        Return the product of ``x`` and ``y`` in the semiring as per
        :meth:`Semirings.ParentMethods.product`.

        EXAMPLES::

            sage: S = Semirings().example()
            sage: S(1) * S(2)
            many
        """
    def an_element(self):
        """
        Return an element of the semiring.

        EXAMPLES::

            sage: Semirings().example().an_element()
            many
        """
    def some_elements(self):
        """
        Return a list of some elements of the semiring.

        EXAMPLES::

            sage: Semirings().example().some_elements()
            [0, 1, many]
        """
    Element = Ternary
Example = TernaryLogic
