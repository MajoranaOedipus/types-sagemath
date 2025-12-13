from sage.combinat.combinatorial_map import combinatorial_map as combinatorial_map
from sage.combinat.gelfand_tsetlin_patterns import GelfandTsetlinPattern as GelfandTsetlinPattern
from sage.combinat.path_tableaux.path_tableau import PathTableau as PathTableau, PathTableaux as PathTableaux
from sage.combinat.skew_tableau import SkewTableau as SkewTableau, SkewTableaux as SkewTableaux
from sage.combinat.tableau import Tableau as Tableau
from sage.rings.semirings.non_negative_integer_semiring import NN as NN

class SemistandardPathTableau(PathTableau):
    """
    An instance is a sequence of lists. Usually the entries will be nonnegative integers
    in which case this is the chain of partitions of a (skew) semistandard tableau.
    In general the entries are elements of an ordered abelian group; each list is weakly
    decreasing and successive lists are interleaved.

    INPUT:

    Can be any of the following

    * a sequence of partitions
    * a sequence of lists/tuples
    * a semistandard tableau
    * a semistandard skew tableau
    * a Gelfand-Tsetlin pattern

    EXAMPLES::

        sage: path_tableaux.SemistandardPathTableau([[], [2], [2,1]])
        [(), (2,), (2, 1)]

        sage: gt = GelfandTsetlinPattern([[2,1], [2]])
        sage: path_tableaux.SemistandardPathTableau(gt)
        [(), (2,), (2, 1)]

        sage: st = SemistandardTableau([[1,1], [2]])
        sage: path_tableaux.SemistandardPathTableau(st)
        [(), (2,), (2, 1)]

        sage: st = SkewTableau([[1,1], [2]])
        sage: path_tableaux.SemistandardPathTableau(st)
        [(), (2,), (2, 1)]

        sage: st = SkewTableau([[None,1,1], [2]])
        sage: path_tableaux.SemistandardPathTableau(st)
        [(1,), (3, 0), (3, 1, 0)]

        sage: path_tableaux.SemistandardPathTableau([[], [5/2], [7/2,2]])
        [(), (5/2,), (7/2, 2)]

        sage: path_tableaux.SemistandardPathTableau([[], [2.5], [3.5,2]])
        [(), (2.50000000000000,), (3.50000000000000, 2)]
    """
    @staticmethod
    def __classcall_private__(cls, st, check: bool = True):
        """
        Ensure that a tableau is only ever constructed as an
        ``element_class`` call of an appropriate parent.

        EXAMPLES::

            sage: t = path_tableaux.SemistandardPathTableau([[], [2]])
            sage: t.parent()
            <sage.combinat.path_tableaux.semistandard.SemistandardPathTableaux_with_category object at ...>
        """
    def __init__(self, parent, st, check: bool = True) -> None:
        """
        Initialize a semistandard tableau.

        TESTS::

            sage: path_tableaux.SemistandardPathTableau([(), 3, (3, 2)])
            Traceback (most recent call last):
            ...
            ValueError: [(), 3, (3, 2)] is not a sequence of lists
        """
    def check(self) -> None:
        """
        Check that ``self`` is a valid path.

        EXAMPLES::

            sage: path_tableaux.SemistandardPathTableau([[], [3], [2,2]])       # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: [(), (3,), (2, 2)] does not satisfy
            the required inequalities in row 1

            sage: path_tableaux.SemistandardPathTableau([[], [3/2], [2,5/2]])   # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: [(), (3/2,), (2, 5/2)] does not satisfy
            the required inequalities in row 1


        TESTS::

            sage: path_tableaux.SemistandardPathTableau([[], [2], [1,2]])
            Traceback (most recent call last):
            ...
            ValueError: [(), (2,), (1, 2)] does not satisfy the required inequalities in row 1

            sage: path_tableaux.SemistandardPathTableau([[], [2], [1,2]], check=False)
            [(), (2,), (1, 2)]
        """
    def size(self):
        """
        Return the size or length of ``self``.

        EXAMPLES::

            sage: path_tableaux.SemistandardPathTableau([[], [3], [3,2], [3,3,1], [3,3,2,1]]).size()
            5
        """
    def is_skew(self):
        """
        Return ``True`` if ``self`` is skew.

        EXAMPLES::

            sage: path_tableaux.SemistandardPathTableau([[], [2]]).is_skew()
            False
            sage: path_tableaux.SemistandardPathTableau([[2,1]]).is_skew()
            True
        """
    def is_integral(self) -> bool:
        """
        Return ``True`` if all entries are nonnegative integers.

        EXAMPLES::

            sage: path_tableaux.SemistandardPathTableau([[], [3], [3,2]]).is_integral()
            True
            sage: path_tableaux.SemistandardPathTableau([[], [5/2], [7/2,2]]).is_integral()
            False
            sage: path_tableaux.SemistandardPathTableau([[], [3], [3,-2]]).is_integral()
            False
        """
    def local_rule(self, i):
        """
        This is the Bender-Knuth involution.

        This is implemented by toggling the entries of the `i`-th list.
        The allowed range for ``i`` is ``0 < i < len(self)-1`` so any row except
        the first and last can be changed.

        EXAMPLES::

            sage: pt = path_tableaux.SemistandardPathTableau([[], [3], [3,2],
            ....:                                             [3,3,1], [3,3,2,1]])
            sage: pt.local_rule(1)
            [(), (2,), (3, 2), (3, 3, 1), (3, 3, 2, 1)]
            sage: pt.local_rule(2)
            [(), (3,), (3, 2), (3, 3, 1), (3, 3, 2, 1)]
            sage: pt.local_rule(3)
            [(), (3,), (3, 2), (3, 2, 2), (3, 3, 2, 1)]

        TESTS::

            sage: pt = path_tableaux.SemistandardPathTableau([[], [3], [3,2],
            ....:                                             [3,3,1], [3,3,2,1]])
            sage: pt.local_rule(0)
            Traceback (most recent call last):
            ...
            ValueError: 0 is not defined on [(), (3,), (3, 2), (3, 3, 1), (3, 3, 2, 1)]
            sage: pt.local_rule(4)
            Traceback (most recent call last):
            ...
            ValueError: 4 is not defined on [(), (3,), (3, 2), (3, 3, 1), (3, 3, 2, 1)]
        """
    def rectify(self, inner=None, verbose: bool = False):
        """
        Rectify ``self``.

        This gives the usual rectification of a skew standard tableau and gives a
        generalisation to skew semistandard tableaux. The usual construction uses
        jeu de taquin but here we use the Bender-Knuth involutions.

        EXAMPLES::

            sage: st = SkewTableau([[None, None, None, 4], [None, None, 1, 6],
            ....:                   [None, None, 5], [2, 3]])
            sage: path_tableaux.SemistandardPathTableau(st).rectify()
            [(), (1,), (1, 1), (2, 1, 0), (3, 1, 0, 0), (3, 2, 0, 0, 0), (4, 2, 0, 0, 0, 0)]
            sage: path_tableaux.SemistandardPathTableau(st).rectify(verbose=True)
            [[(3, 2, 2), (3, 3, 2, 0), (3, 3, 2, 1, 0), (3, 3, 2, 2, 0, 0),
              (4, 3, 2, 2, 0, 0, 0), (4, 3, 3, 2, 0, 0, 0, 0), (4, 4, 3, 2, 0, 0, 0, 0, 0)],
             [(3, 2), (3, 3, 0), (3, 3, 1, 0), (3, 3, 2, 0, 0), (4, 3, 2, 0, 0, 0),
              (4, 3, 3, 0, 0, 0, 0), (4, 4, 3, 0, 0, 0, 0, 0)],
             [(3,), (3, 1), (3, 1, 1), (3, 2, 1, 0), (4, 2, 1, 0, 0), (4, 3, 1, 0, 0, 0),
              (4, 4, 1, 0, 0, 0, 0)],
             [(), (1,), (1, 1), (2, 1, 0), (3, 1, 0, 0), (3, 2, 0, 0, 0), (4, 2, 0, 0, 0, 0)]]

        TESTS::

            sage: S = SemistandardSkewTableaux([[5,3,3], [3,1]], [3,2,2])
            sage: LHS = [path_tableaux.SemistandardPathTableau(st.rectify()) for st in S]
            sage: RHS = [path_tableaux.SemistandardPathTableau(st).rectify() for st in S]
            sage: LHS == RHS
            True

            sage: st = SkewTableau([[None, None, None, 4], [None, None, 1, 6],
            ....:                   [None, None, 5], [2, 3]])
            sage: pt = path_tableaux.SemistandardPathTableau(st)
            sage: SP = [path_tableaux.SemistandardPathTableau(it)
            ....:       for it in StandardTableaux([3,2,2])]
            sage: len(set(pt.rectify(inner=ip) for ip in SP))
            1
        """
    def to_tableau(self):
        """
        Convert ``self`` to a :class:`SemistandardTableau`.

        The :class:`SemistandardSkewTableau` is not implemented so this returns a :class:`SkewTableau`

        EXAMPLES::

            sage: pt = path_tableaux.SemistandardPathTableau([[], [3], [3,2], [3,3,1],
            ....:                                             [3,3,2,1], [4,3,3,1,0]])
            sage: pt.to_tableau()
            [[1, 1, 1, 5], [2, 2, 3], [3, 4, 5], [4]]

        TESTS::

            sage: SST = SemistandardTableaux(shape=[5,5,3], eval=[2,2,3,4,2])
            sage: all(st == path_tableaux.SemistandardPathTableau(st).to_tableau()      # needs sage.modules
            ....:     for st in SST)
            True
        """
    def to_pattern(self):
        """
        Convert ``self`` to a Gelfand-Tsetlin pattern.

        EXAMPLES::

            sage: pt = path_tableaux.SemistandardPathTableau([[], [3], [3,2], [3,3,1],
            ....:                                             [3,3,2,1], [4,3,3,1]])
            sage: pt.to_pattern()
            [[4, 3, 3, 1, 0], [3, 3, 2, 1], [3, 3, 1], [3, 2], [3]]

        TESTS::

            sage: pt = path_tableaux.SemistandardPathTableau([[3,2], [3,3,1], [3,3,2,1], [4,3,3,1]])
            sage: pt.to_pattern()
            Traceback (most recent call last):
            ...
            ValueError: [(3, 2), (3, 3, 1), (3, 3, 2, 1), (4, 3, 3, 1, 0)] cannot be a skew tableau

            sage: GT = GelfandTsetlinPatterns(top_row=[5,5,3])
            sage: all(gt == path_tableaux.SemistandardPathTableau(gt).to_pattern() for gt in GT)
            True

            sage: GT = GelfandTsetlinPatterns(top_row=[5,5,3])
            sage: all(gt.to_tableau() == path_tableaux.SemistandardPathTableau(gt).to_tableau() for gt in GT)
            True
        """

class SemistandardPathTableaux(PathTableaux):
    """
    The parent class for :class:`SemistandardPathTableau`.
    """
    Element = SemistandardPathTableau
