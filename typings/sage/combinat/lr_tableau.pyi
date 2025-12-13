from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.combinat.partition import Partition as Partition, Partitions as Partitions
from sage.combinat.tableau import SemistandardTableau as SemistandardTableau, SemistandardTableaux as SemistandardTableaux

class LittlewoodRichardsonTableau(SemistandardTableau):
    """
    A semistandard tableau is Littlewood-Richardson with respect to
    the sequence of partitions `(\\mu^{(1)}, \\ldots, \\mu^{(k)})` if,
    when restricted to each alphabet `\\{|\\mu^{(1)}|+\\cdots+|\\mu^{(i-1)}|+1,
    \\ldots, |\\mu^{(1)}|+\\cdots+|\\mu^{(i)}|-1\\}`, is Yamanouchi.

    INPUT:

    - ``t`` -- Littlewood-Richardson tableau; the input is supposed to be
      a list of lists specifying the rows of the tableau

    EXAMPLES::

        sage: from sage.combinat.lr_tableau import LittlewoodRichardsonTableau
        sage: LittlewoodRichardsonTableau([[1,1,3],[2,3],[4]], [[2,1],[2,1]])
        [[1, 1, 3], [2, 3], [4]]
    """
    @staticmethod
    def __classcall_private__(cls, t, weight):
        """
        Implement the shortcut ``LittlewoodRichardsonTableau(t, weight)`` to
        ``LittlewoodRichardsonTableaux(shape , weight)(t)``
        where ``shape`` is the shape of the tableau.

        TESTS::

            sage: LR = LittlewoodRichardsonTableaux([3,2,1],[[2,1],[2,1]])
            sage: t = LR([[1, 1, 3], [2, 3], [4]])
            sage: t.check()
            sage: type(t)
            <class 'sage.combinat.lr_tableau.LittlewoodRichardsonTableaux_with_category.element_class'>
            sage: TestSuite(t).run()
            sage: from sage.combinat.lr_tableau import LittlewoodRichardsonTableau
            sage: LittlewoodRichardsonTableau([[1,1,3],[2,3],[4]], [[2,1],[2,1]])
            [[1, 1, 3], [2, 3], [4]]
        """
    def __init__(self, parent, t) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: LR = LittlewoodRichardsonTableaux([3,2,1],[[2,1],[2,1]])
            sage: t = LR([[1, 1, 3], [2, 3], [4]])
            sage: from sage.combinat.lr_tableau import LittlewoodRichardsonTableau
            sage: s = LittlewoodRichardsonTableau([[1,1,3],[2,3],[4]], [[2,1],[2,1]])
            sage: s == t
            True
            sage: type(t)
            <class 'sage.combinat.lr_tableau.LittlewoodRichardsonTableaux_with_category.element_class'>
            sage: t.parent()
            Littlewood-Richardson Tableaux of shape [3, 2, 1] and weight ([2, 1], [2, 1])
            sage: TestSuite(t).run()
        """
    def check(self) -> None:
        """
        Check that ``self`` is a valid Littlewood-Richardson tableau.

        EXAMPLES::

            sage: from sage.combinat.lr_tableau import LittlewoodRichardsonTableau
            sage: t = LittlewoodRichardsonTableau([[1,1,3],[2,3],[4]], [[2,1],[2,1]])
            sage: t.check()

        TESTS::

            sage: LR = LittlewoodRichardsonTableaux([3,2,1],[[2,1],[2,1]])
            sage: LR([[1, 1, 2], [3, 3], [4]])
            Traceback (most recent call last):
            ...
            ValueError: [[1, 1, 2], [3, 3], [4]] is not an element of
             Littlewood-Richardson Tableaux of shape [3, 2, 1] and weight ([2, 1], [2, 1])
            sage: LR([[1, 1, 2, 3], [3], [4]])
            Traceback (most recent call last):
            ...
            ValueError: [[1, 1, 2, 3], [3], [4]] is not an element of
             Littlewood-Richardson Tableaux of shape [3, 2, 1] and weight ([2, 1], [2, 1])
            sage: LR([[1, 1, 3], [3, 3], [4]])
            Traceback (most recent call last):
            ...
            ValueError: weight of the parent does not agree with the weight of the tableau
        """

class LittlewoodRichardsonTableaux(SemistandardTableaux):
    """
    Littlewood-Richardson tableaux.

    A semistandard tableau `t` is *Littlewood-Richardson* with respect to
    the sequence of partitions `(\\mu^{(1)}, \\ldots, \\mu^{(k)})` (called
    the weight) if `t` is Yamanouchi when restricted to each alphabet
    `\\{|\\mu^{(1)}| + \\cdots + |\\mu^{(i-1)}| + 1, \\ldots,
    |\\mu^{(1)}| + \\cdots + |\\mu^{(i)}| - 1\\}`.

    INPUT:

    - ``shape`` -- the shape of the Littlewood-Richardson tableaux
    - ``weight`` -- the weight is a sequence of partitions

    EXAMPLES::

        sage: LittlewoodRichardsonTableaux([3,2,1],[[2,1],[2,1]])
        Littlewood-Richardson Tableaux of shape [3, 2, 1] and weight ([2, 1], [2, 1])
    """
    @staticmethod
    def __classcall_private__(cls, shape, weight):
        """
        Straighten arguments before unique representation.

        TESTS::

            sage: LR = LittlewoodRichardsonTableaux([3,2,1],[[2,1],[2,1]])
            sage: TestSuite(LR).run()
            sage: LittlewoodRichardsonTableaux([3,2,1],[[2,1]])
            Traceback (most recent call last):
            ...
            ValueError: the sizes of shapes and sequence of weights do not match
        """
    def __init__(self, shape, weight) -> None:
        """
        Initialize the parent class of Littlewood-Richardson tableaux.

        INPUT:

        - ``shape`` -- the shape of the Littlewood-Richardson tableaux
        - ``weight`` -- the weight is a sequence of partitions

        TESTS::

            sage: LR = LittlewoodRichardsonTableaux([3,2,1],[[2,1],[2,1]])
            sage: TestSuite(LR).run()
        """
    def __iter__(self):
        """
        TESTS::

            sage: LR = LittlewoodRichardsonTableaux([3,2,1], [[2,1],[2,1]])
            sage: LR.list()
            [[[1, 1, 3], [2, 3], [4]], [[1, 1, 3], [2, 4], [3]]]
        """
    def __contains__(self, t) -> bool:
        """
        Check if ``t`` is contained in ``self``.

        TESTS::

            sage: LR = LittlewoodRichardsonTableaux([3,2,1], [[2,1],[2,1]])
            sage: SST = SemistandardTableaux([3,2,1], [2,1,2,1])
            sage: [t for t in SST if t in LR]
            [[[1, 1, 3], [2, 3], [4]], [[1, 1, 3], [2, 4], [3]]]
            sage: [t for t in SST if t in LR] == LR.list()
            True

            sage: LR = LittlewoodRichardsonTableaux([3,2,1], [[2,1],[2,1]])
            sage: T = [[1,1,3], [2,3], [4]]
            sage: T in LR
            True
        """
    Element = LittlewoodRichardsonTableau

def is_littlewood_richardson(t, heights):
    """
    Return whether semistandard tableau ``t`` is Littleword-Richardson
    with respect to ``heights``.

    A tableau is Littlewood-Richardson with respect to ``heights`` given
    by `(h_1, h_2, \\ldots)` if each subtableau with respect to the
    alphabets `\\{1, 2, \\ldots, h_1\\}`, `\\{h_1+1, \\ldots, h_1+h_2\\}`,
    etc. is Yamanouchi.

    EXAMPLES::

        sage: from sage.combinat.lr_tableau import is_littlewood_richardson
        sage: t = Tableau([[1,1,2,3,4],[2,3,3],[3]])
        sage: is_littlewood_richardson(t,[2,2])
        False
        sage: t = Tableau([[1,1,3],[2,3],[4,4]])
        sage: is_littlewood_richardson(t,[2,2])
        True
        sage: t = Tableau([[7],[8]])
        sage: is_littlewood_richardson(t,[2,3,3])
        False
        sage: is_littlewood_richardson([[2],[3]],[3,3])
        False
    """
