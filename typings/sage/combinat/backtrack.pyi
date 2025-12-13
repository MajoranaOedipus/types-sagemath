from sage.categories.commutative_additive_semigroups import CommutativeAdditiveSemigroups as CommutativeAdditiveSemigroups
from sage.categories.infinite_enumerated_sets import InfiniteEnumeratedSets as InfiniteEnumeratedSets
from sage.categories.monoids import Monoids as Monoids
from sage.rings.integer_ring import ZZ as ZZ
from sage.sets.recursively_enumerated_set import RecursivelyEnumeratedSet_forest as RecursivelyEnumeratedSet_forest
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class GenericBacktracker:
    """
    A generic backtrack tool for exploring a search space organized as a tree,
    with branch pruning, etc.

    See also :class:`RecursivelyEnumeratedSet_forest` for
    handling simple special cases.
    """
    def __init__(self, initial_data, initial_state) -> None:
        """
        EXAMPLES::

            sage: from sage.combinat.backtrack import GenericBacktracker
            sage: p = GenericBacktracker([], 1)
            sage: loads(dumps(p))
            <sage.combinat.backtrack.GenericBacktracker object at 0x...>
        """
    def __iter__(self):
        """
        EXAMPLES::

            sage: from sage.combinat.permutation import PatternAvoider
            sage: p = PatternAvoider(Permutations(4), [[1,3,2]])
            sage: len(list(p))                                                          # needs sage.combinat
            14
        """

class PositiveIntegerSemigroup(UniqueRepresentation, RecursivelyEnumeratedSet_forest):
    """
    The commutative additive semigroup of positive integers.

    This class provides an example of algebraic structure which
    inherits from :class:`RecursivelyEnumeratedSet_forest`. It builds the positive
    integers a la Peano, and endows it with its natural commutative
    additive semigroup structure.

    EXAMPLES::

        sage: from sage.combinat.backtrack import PositiveIntegerSemigroup
        sage: PP = PositiveIntegerSemigroup()
        sage: PP.category()
        Join of Category of monoids and Category of commutative additive semigroups and Category of infinite enumerated sets and Category of facade sets
        sage: PP.cardinality()
        +Infinity
        sage: PP.one()
        1
        sage: PP.an_element()
        1
        sage: some_elements = list(PP.some_elements()); some_elements
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

    TESTS::

        sage: from sage.combinat.backtrack import PositiveIntegerSemigroup
        sage: PP = PositiveIntegerSemigroup()

    We factor out the long test from the ``TestSuite``::

        sage: TestSuite(PP).run(skip='_test_enumerated_set_contains')
        sage: PP._test_enumerated_set_contains()  # long time
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.combinat.backtrack import PositiveIntegerSemigroup
            sage: PP = PositiveIntegerSemigroup()
        """
    def roots(self):
        """
        Return the single root of ``self``.

        EXAMPLES::

            sage: from sage.combinat.backtrack import PositiveIntegerSemigroup
            sage: PP = PositiveIntegerSemigroup()
            sage: list(PP.roots())
            [1]
        """
    def children(self, x):
        """
        Return the single child ``x+1`` of the integer ``x``.

        EXAMPLES::

            sage: from sage.combinat.backtrack import PositiveIntegerSemigroup
            sage: PP = PositiveIntegerSemigroup()
            sage: list(PP.children(1))
            [2]
            sage: list(PP.children(42))
            [43]
        """
    def one(self):
        """
        Return the unit of ``self``.

        EXAMPLES::

            sage: from sage.combinat.backtrack import PositiveIntegerSemigroup
            sage: PP = PositiveIntegerSemigroup()
            sage: PP.one()
            1
        """
