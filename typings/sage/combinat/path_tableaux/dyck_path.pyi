from sage.combinat.combinatorial_map import combinatorial_map as combinatorial_map
from sage.combinat.dyck_word import DyckWord as DyckWord
from sage.combinat.path_tableaux.path_tableau import PathTableau as PathTableau, PathTableaux as PathTableaux
from sage.combinat.perfect_matching import PerfectMatching as PerfectMatching
from sage.combinat.skew_tableau import SkewTableau as SkewTableau
from sage.combinat.tableau import StandardTableau as StandardTableau, Tableau as Tableau
from sage.rings.integer import Integer as Integer

class DyckPath(PathTableau):
    """
    An instance is the sequence of nonnegative
    integers given by the heights of a Dyck word.

    INPUT:

    - a sequence of nonnegative integers
    - a two row standard skew tableau
    - a Dyck word
    - a noncrossing perfect matching

    EXAMPLES::

        sage: path_tableaux.DyckPath([0,1,2,1,0])
        [0, 1, 2, 1, 0]

        sage: w = DyckWord([1,1,0,0])
        sage: path_tableaux.DyckPath(w)
        [0, 1, 2, 1, 0]

        sage: p = PerfectMatching([(1,2), (3,4)])
        sage: path_tableaux.DyckPath(p)
        [0, 1, 0, 1, 0]

        sage: t = Tableau([[1,2,4],[3,5,6]])
        sage: path_tableaux.DyckPath(t)
        [0, 1, 2, 1, 2, 1, 0]

        sage: st = SkewTableau([[None, 1,4],[2,3]])
        sage: path_tableaux.DyckPath(st)
        [1, 2, 1, 0, 1]

    Here we illustrate the slogan that promotion = rotation::

        sage: t = path_tableaux.DyckPath([0,1,2,3,2,1,0])
        sage: t.to_perfect_matching()
        [(0, 5), (1, 4), (2, 3)]

        sage: t = t.promotion()
        sage: t.to_perfect_matching()
        [(0, 3), (1, 2), (4, 5)]

        sage: t = t.promotion()
        sage: t.to_perfect_matching()
        [(0, 1), (2, 5), (3, 4)]

        sage: t = t.promotion()
        sage: t.to_perfect_matching()
        [(0, 5), (1, 4), (2, 3)]
    """
    @staticmethod
    def __classcall_private__(cls, ot):
        """
        This ensures that a tableau is only ever constructed as an
        ``element_class`` call of an appropriate parent.

        TESTS::

            sage: t = path_tableaux.DyckPath([0,1,2,1,0])

            sage: t.parent()
            <sage.combinat.path_tableaux.dyck_path.DyckPaths_with_category object at ...>
        """
    def __init__(self, parent, ot, check: bool = True) -> None:
        """
        Initialize a Dyck path.

        TESTS::

            sage: D = path_tableaux.DyckPath(Tableau([[1,2], [3,4]]))
            sage: TestSuite(D).run()

            sage: D = path_tableaux.DyckPath(PerfectMatching([(1,4), (2,3), (5,6)]))
            sage: TestSuite(D).run()

            sage: t = path_tableaux.DyckPath([0,1,2,3,2,1,0])
            sage: TestSuite(t).run()

            sage: path_tableaux.DyckPath(PerfectMatching([(1, 3), (2, 4), (5, 6)]))
            Traceback (most recent call last):
            ...
            ValueError: the perfect matching must be non crossing
            sage: path_tableaux.DyckPath(Tableau([[1,2,5],[3,5,6]]))
            Traceback (most recent call last):
            ...
            ValueError: the tableau must be standard
            sage: path_tableaux.DyckPath(Tableau([[1,2,4],[3,5,6],[7]]))
            Traceback (most recent call last):
            ...
            ValueError: the tableau must have at most two rows
            sage: path_tableaux.DyckPath(SkewTableau([[None, 1,4],[2,3],[5]]))
            Traceback (most recent call last):
            ...
            ValueError: the skew tableau must have at most two rows
            sage: path_tableaux.DyckPath([0,1,2.5,1,0])
            Traceback (most recent call last):
            ...
            ValueError: [0, 1, 2.50000000000000, 1, 0] is not a sequence of integers
            sage: path_tableaux.DyckPath(Partition([3,2,1]))
            Traceback (most recent call last):
            ...
            ValueError: invalid input [3, 2, 1]
        """
    def check(self) -> None:
        """
        Check that ``self`` is a valid path.

        EXAMPLES::

            sage: path_tableaux.DyckPath([0,1,0,-1,0]) # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: [0, 1, 0, -1, 0] has a negative entry

            sage: path_tableaux.DyckPath([0,1,3,1,0]) # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: [0, 1, 3, 1, 0] is not a Dyck path
        """
    def local_rule(self, i):
        """
        This has input a list of objects. This method first takes
        the list of objects of length three consisting of the `(i-1)`-st,
        `i`-th and `(i+1)`-term and applies the rule. It then replaces
        the `i`-th object  by the object returned by the rule.

        EXAMPLES::

            sage: t = path_tableaux.DyckPath([0,1,2,3,2,1,0])
            sage: t.local_rule(3)
            [0, 1, 2, 1, 2, 1, 0]

        TESTS::

            sage: t = path_tableaux.DyckPath([0,1,2,3,2,1,0])
            sage: t.local_rule(0)
            Traceback (most recent call last):
            ...
            ValueError: 0 is not a valid integer
            sage: t.local_rule(5)
            [0, 1, 2, 3, 2, 1, 0]
            sage: t.local_rule(6)
            Traceback (most recent call last):
            ...
            ValueError: 6 is not a valid integer
        """
    def is_skew(self):
        """
        Return ``True`` if ``self`` is skew and ``False`` if not.

        EXAMPLES::

            sage: path_tableaux.DyckPath([0,1,2,1]).is_skew()
            False

            sage: path_tableaux.DyckPath([1,0,1,2,1]).is_skew()
            True
        """
    def to_DyckWord(self):
        """
        Convert ``self`` to a Dyck word.

        EXAMPLES::

            sage: c = path_tableaux.DyckPath([0,1,2,1,0])
            sage: c.to_DyckWord()
            [1, 1, 0, 0]
        """
    def descents(self):
        """
        Return the descent set of ``self``.

        EXAMPLES::

            sage: path_tableaux.DyckPath([0,1,2,1,2,1,0,1,0]).descents()
            {3, 6}
        """
    def to_word(self):
        """
        Return the word in the alphabet `\\{0,1\\}` associated to ``self``.

        EXAMPLES::

            sage: path_tableaux.DyckPath([1,0,1,2,1]).to_word()
            [0, 1, 1, 0]
        """
    def to_perfect_matching(self):
        """
        Return the perfect matching associated to ``self``.

        EXAMPLES::

            sage: path_tableaux.DyckPath([0,1,2,1,2,1,0,1,0]).to_perfect_matching()
            [(0, 5), (1, 2), (3, 4), (6, 7)]

        TESTS::

            sage: path_tableaux.DyckPath([1,2,1,2,1,0,1]).to_perfect_matching()
            Traceback (most recent call last):
            ...
            ValueError: [1, 2, 1, 2, 1, 0, 1] does not start at 0
        """
    def to_tableau(self):
        """
        Return the skew tableau associated to ``self``.

        EXAMPLES::

            sage: T = path_tableaux.DyckPath([0,1,2,3,2,3])
            sage: T.to_tableau()
            [[1, 2, 3, 5], [4]]

            sage: U = path_tableaux.DyckPath([2,3,2,3])
            sage: U.to_tableau()
            [[None, None, 1, 3], [2]]
        """

class DyckPaths(PathTableaux):
    """
    The parent class for DyckPath.
    """
    Element = DyckPath
