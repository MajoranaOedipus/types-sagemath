from sage.categories.sets_with_grading import SetsWithGrading as SetsWithGrading
from sage.rings.integer_ring import IntegerRing as IntegerRing
from sage.sets.finite_enumerated_set import FiniteEnumeratedSet as FiniteEnumeratedSet
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class NonNegativeIntegers(UniqueRepresentation, Parent):
    """
    Non negative integers graded by themselves.

    EXAMPLES::

        sage: E = SetsWithGrading().example(); E
        Non negative integers
        sage: E in Sets().Infinite()
        True
        sage: E.graded_component(0)
        {0}
        sage: E.graded_component(100)
        {100}
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: TestSuite(SetsWithGrading().example()).run()
        """
    def an_element(self):
        """
        Return 0.

        EXAMPLES::

            sage: SetsWithGrading().example().an_element()
            0
        """
    def graded_component(self, grade):
        """
        Return the component with grade ``grade``.

        EXAMPLES::

            sage: N = SetsWithGrading().example()
            sage: N.graded_component(65)
            {65}
        """
    def grading(self, elt):
        """
        Return the grade of ``elt``.

        EXAMPLES::

            sage: N = SetsWithGrading().example()
            sage: N.grading(10)
            10
        """
    def generating_series(self, var: str = 'z'):
        """
        Return `1 / (1-z)`.

        EXAMPLES::

            sage: N = SetsWithGrading().example(); N
            Non negative integers
            sage: f = N.generating_series(); f
            1/(-z + 1)
            sage: LaurentSeriesRing(ZZ,'z')(f)
            1 + z + z^2 + z^3 + z^4 + z^5 + z^6 + z^7 + z^8 + z^9 + z^10 + z^11 + z^12 + z^13 + z^14 + z^15 + z^16 + z^17 + z^18 + z^19 + O(z^20)
        """
Example = NonNegativeIntegers
