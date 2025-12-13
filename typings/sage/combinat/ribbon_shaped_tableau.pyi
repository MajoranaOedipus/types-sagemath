from _typeshed import Incomplete
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.categories.infinite_enumerated_sets import InfiniteEnumeratedSets as InfiniteEnumeratedSets
from sage.categories.sets_cat import Sets as Sets
from sage.combinat.permutation import descents_composition_first as descents_composition_first, descents_composition_last as descents_composition_last, descents_composition_list as descents_composition_list
from sage.combinat.skew_tableau import SkewTableau as SkewTableau, SkewTableaux as SkewTableaux, StandardSkewTableaux as StandardSkewTableaux
from sage.combinat.tableau import Tableaux as Tableaux
from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.rings.integer import Integer as Integer

class RibbonShapedTableau(SkewTableau):
    """
    A ribbon shaped tableau.

    For the purposes of this class, a ribbon shaped tableau is a skew
    tableau whose shape is a skew partition which:

    - has at least one cell in row `1`;

    - has at least one cell in column `1`;

    - has exactly one cell in each of `q` consecutive diagonals, for
      some nonnegative integer `q`.

    A ribbon is given by a list of the rows from top to bottom.

    EXAMPLES::

        sage: x = RibbonShapedTableau([[None, None, None, 2, 3], [None, 1, 4, 5], [3, 2]]); x
        [[None, None, None, 2, 3], [None, 1, 4, 5], [3, 2]]
        sage: x.pp()
          .  .  .  2  3
          .  1  4  5
          3  2
        sage: x.shape()
        [5, 4, 2] / [3, 1]

    The entries labeled by ``None`` correspond to the inner partition.
    Using ``None`` is optional; the entries will be shifted accordingly.  ::

        sage: x = RibbonShapedTableau([[2,3],[1,4,5],[3,2]]); x.pp()
          .  .  .  2  3
          .  1  4  5
          3  2

    TESTS::

        sage: r = RibbonShapedTableau([[1], [2,3], [4, 5, 6]])
        sage: r.to_permutation()
        [4, 5, 6, 2, 3, 1]

        sage: RibbonShapedTableau([[1,2],[3,4]]).evaluation()
        [1, 1, 1, 1]
    """
    @staticmethod
    def __classcall_private__(cls, rows):
        """
        Return a ribbon shaped tableau object.

        EXAMPLES::

            sage: RibbonShapedTableau([[2,3],[1,4,5]])
            [[None, None, 2, 3], [1, 4, 5]]

        TESTS::

            sage: RibbonShapedTableau([4,5])
            Traceback (most recent call last):
            ...
            TypeError: rows must be lists of positive integers

            sage: RibbonShapedTableau([[2,3],[-4,5]])
            Traceback (most recent call last):
            ...
            TypeError: r must be a list of positive integers
        """
    def __init__(self, parent, t) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: R = RibbonShapedTableau([[2,3],[1,4,5]])
            sage: TestSuite(R).run()
        """
    def height(self):
        """
        Return the height of ``self``.

        The height is given by the number of rows in the outer partition.

        EXAMPLES::

            sage: RibbonShapedTableau([[2,3],[1,4,5]]).height()
            2
        """
    def spin(self):
        """
        Return the spin of ``self``.

        EXAMPLES::

            sage: RibbonShapedTableau([[2,3],[1,4,5]]).spin()
            1/2
        """
    def width(self):
        """
        Return the width of the ribbon.

        This is given by the length of the longest row in the outer partition.

        EXAMPLES::

            sage: RibbonShapedTableau([[2,3],[1,4,5]]).width()
            4
            sage: RibbonShapedTableau([]).width()
            0
        """

class RibbonShapedTableaux(SkewTableaux):
    """
    The set of all ribbon shaped tableaux.
    """
    @staticmethod
    def __classcall_private__(cls, shape=None, **kwds):
        """
        Normalize input to ensure a unique representation and pick the correct
        class based on input.

        The ``shape`` parameter is currently ignored.

        EXAMPLES::

            sage: S1 = RibbonShapedTableaux([4, 2, 2, 1])
            sage: S2 = RibbonShapedTableaux((4, 2, 2, 1))
            sage: S1 is S2
            True
        """
    def __init__(self, category=None) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: S = RibbonShapedTableaux()                                            # needs sage.graphs
            sage: TestSuite(S).run()                                                    # needs sage.graphs
        """
    Element = RibbonShapedTableau
    options = Tableaux.options
    def from_shape_and_word(self, shape, word):
        """
        Return the ribbon corresponding to the given ribbon shape and word.

        EXAMPLES::

            sage: RibbonShapedTableaux().from_shape_and_word([1,3],[1,3,3,7])
            [[None, None, 1], [3, 3, 7]]
        """

class StandardRibbonShapedTableaux(StandardSkewTableaux):
    """
    The set of all standard ribbon shaped tableaux.

    INPUT:

    - ``shape`` -- (optional) the composition shape of the rows
    """
    @staticmethod
    def __classcall_private__(cls, shape=None, **kwds):
        """
        Normalize input to ensure a unique representation and pick the correct
        class based on input.

        EXAMPLES::

            sage: S1 = StandardRibbonShapedTableaux([4, 2, 2, 1])
            sage: S2 = StandardRibbonShapedTableaux((4, 2, 2, 1))
            sage: S1 is S2
            True
        """
    def __init__(self, category=None) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: # needs sage.graphs sage.modules
            sage: S = StandardRibbonShapedTableaux()
            sage: TestSuite(S).run()
        """
    def __iter__(self):
        """
        Iterate through ``self``.

        EXAMPLES::

            sage: # needs sage.graphs sage.modules
            sage: it = StandardRibbonShapedTableaux().__iter__()
            sage: [next(it) for x in range(10)]
            [[],
             [[1]],
             [[1, 2]],
             [[1], [2]],
             [[1, 2, 3]],
             [[None, 1], [2, 3]],
             [[None, 2], [1, 3]],
             [[1], [2], [3]],
             [[1, 2, 3, 4]],
             [[None, None, 1], [2, 3, 4]]]
        """
    Element = RibbonShapedTableau
    options = Tableaux.options
    def from_shape_and_word(self, shape, word):
        """
        Return the ribbon corresponding to the given ribbon shape and word.

        EXAMPLES::

            sage: StandardRibbonShapedTableaux().from_shape_and_word([2,3],[1,2,3,4,5])
            [[None, None, 1, 2], [3, 4, 5]]
        """
    def from_permutation(self, p):
        """
        Return a standard ribbon of size ``len(p)`` from a permutation ``p``. The
        lengths of each row are given by the distance between the descents
        of the permutation ``p``.

        EXAMPLES::

            sage: import sage.combinat.ribbon_shaped_tableau as rst
            sage: [StandardRibbonShapedTableaux().from_permutation(p)
            ....:  for p in Permutations(3)]
            [[[1, 2, 3]],
             [[None, 2], [1, 3]],
             [[1, 3], [2]],
             [[None, 1], [2, 3]],
             [[1, 2], [3]],
             [[1], [2], [3]]]
        """

class StandardRibbonShapedTableaux_shape(StandardRibbonShapedTableaux):
    """
    Class of standard ribbon shaped tableaux of ribbon shape ``shape``.

    EXAMPLES::

        sage: StandardRibbonShapedTableaux([2,2])
        Standard ribbon shaped tableaux of shape [2, 2]
        sage: StandardRibbonShapedTableaux([2,2]).first()
        [[None, 2, 4], [1, 3]]
        sage: StandardRibbonShapedTableaux([2,2]).last()
        [[None, 1, 2], [3, 4]]

        sage: # needs sage.graphs sage.modules
        sage: StandardRibbonShapedTableaux([2,2]).cardinality()
        5
        sage: StandardRibbonShapedTableaux([2,2]).list()
        [[[None, 1, 3], [2, 4]],
         [[None, 1, 2], [3, 4]],
         [[None, 2, 3], [1, 4]],
         [[None, 2, 4], [1, 3]],
         [[None, 1, 4], [2, 3]]]
        sage: StandardRibbonShapedTableaux([3,2,2]).cardinality()
        155
    """
    @staticmethod
    def __classcall_private__(cls, shape):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: S = StandardRibbonShapedTableaux([2,2])
            sage: S2 = StandardRibbonShapedTableaux((2,2))
            sage: S is S2
            True
        """
    shape: Incomplete
    def __init__(self, shape) -> None:
        """
        TESTS::

            sage: S = StandardRibbonShapedTableaux([2,2])
            sage: TestSuite(S).run()                                                    # needs sage.graphs
        """
    def first(self):
        """
        Return the first standard ribbon of ``self``.

        EXAMPLES::

            sage: StandardRibbonShapedTableaux([2,2]).first()
            [[None, 2, 4], [1, 3]]
        """
    def last(self):
        """
        Return the last standard ribbon of ``self``.

        EXAMPLES::

            sage: StandardRibbonShapedTableaux([2,2]).last()
            [[None, 1, 2], [3, 4]]
        """
    def __iter__(self):
        """
        An iterator for the standard ribbon of ``self``.

        EXAMPLES::

            sage: [t for t in StandardRibbonShapedTableaux([2,2])]                      # needs sage.graphs
            [[[None, 1, 3], [2, 4]],
             [[None, 1, 2], [3, 4]],
             [[None, 2, 3], [1, 4]],
             [[None, 2, 4], [1, 3]],
             [[None, 1, 4], [2, 3]]]
        """

class Ribbon_class(RibbonShapedTableau):
    """
    This exists solely for unpickling ``Ribbon_class`` objects.
    """
