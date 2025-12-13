from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.combinat.combinat import bell_number as bell_number
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class RestrictedGrowthArrays(UniqueRepresentation, Parent):
    def __init__(self, n) -> None:
        """
        EXAMPLES::

            sage: from sage.combinat.restricted_growth import RestrictedGrowthArrays
            sage: R = RestrictedGrowthArrays(3)
            sage: R == loads(dumps(R))
            True
            sage: TestSuite(R).run(skip=['_test_an_element',                            # needs sage.libs.flint
            ....:   '_test_enumerated_set_contains', '_test_some_elements'])
        """
    def __iter__(self):
        """
        EXAMPLES::

            sage: from sage.combinat.restricted_growth import RestrictedGrowthArrays
            sage: R = RestrictedGrowthArrays(3)
            sage: R.list()
            [[1, 0, 0], [2, 0, 1], [2, 1, 0], [2, 1, 1], [3, 1, 2]]
        """
    def cardinality(self):
        """
        EXAMPLES::

            sage: from sage.combinat.restricted_growth import RestrictedGrowthArrays
            sage: R = RestrictedGrowthArrays(6)
            sage: R.cardinality()                                                       # needs sage.libs.flint
            203
        """
