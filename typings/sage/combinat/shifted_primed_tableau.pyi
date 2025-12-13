from _typeshed import Incomplete
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.categories.infinite_enumerated_sets import InfiniteEnumeratedSets as InfiniteEnumeratedSets
from sage.categories.regular_crystals import RegularCrystals as RegularCrystals
from sage.categories.regular_supercrystals import RegularSuperCrystals as RegularSuperCrystals
from sage.categories.sets_cat import Sets as Sets
from sage.combinat.combination import Combinations as Combinations
from sage.combinat.integer_vector import IntegerVectors as IntegerVectors
from sage.combinat.partition import OrderedPartitions as OrderedPartitions, Partition as Partition, Partitions as Partitions
from sage.combinat.partitions import ZS1_iterator as ZS1_iterator
from sage.combinat.skew_partition import SkewPartition as SkewPartition
from sage.combinat.tableau import Tableaux as Tableaux
from sage.misc.inherit_comparison import InheritComparisonClasscallMetaclass as InheritComparisonClasscallMetaclass
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.integer import Integer as Integer
from sage.rings.rational_field import QQ as QQ
from sage.structure.list_clone import ClonableArray as ClonableArray
from sage.structure.parent import Parent as Parent
from sage.structure.sage_object import SageObject as SageObject
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class ShiftedPrimedTableau(ClonableArray, metaclass=InheritComparisonClasscallMetaclass):
    '''
    A shifted primed tableau.

    A primed tableau is a tableau of shifted shape in the alphabet
    `X\' = \\{1\' < 1 < 2\' < 2 < \\cdots < n\' < n\\}` such that

    1. the entries are weakly increasing along rows and columns;
    2. a row cannot have two repeated primed elements, and a column
       cannot have two repeated non-primed elements;

    Skew shape of the shifted primed tableaux is specified either
    with an optional argument ``skew`` or with ``None`` entries.

    Primed entries in the main diagonal can be allowed with the optional
    boolean parameter ``primed_diagonal``(default: ``False``).

    EXAMPLES::

        sage: T = ShiftedPrimedTableaux([4,2])
        sage: T([[1,"2\'","3\'",3],[2,"3\'"]])[1]
        (2, 3\')
        sage: t = ShiftedPrimedTableau([[1,"2p",2.5,3],[2,2.5]])
        sage: t[1]
        (2, 3\')
        sage: ShiftedPrimedTableau([["2p",2,3],["2p","3p"],[2]], skew=[2,1])
        [(None, None, 2\', 2, 3), (None, 2\', 3\'), (2,)]
        sage: ShiftedPrimedTableau([[None,None,"2p"],[None,"2p"]])
        [(None, None, 2\'), (None, 2\')]
        sage: T = ShiftedPrimedTableaux([4,2], primed_diagonal=True)
        sage: T([[1,"2\'","3\'",3],["2\'","3\'"]])[1] # With primed diagonal entry
        (2\', 3\')

    TESTS::

        sage: t = ShiftedPrimedTableau([[1,2,2.5,3],[2,2.5]])
        Traceback (most recent call last):
        ...
        ValueError: [[1, 2, 2.50000000000000, 3], [2, 2.50000000000000]]
         is not an element of Shifted Primed Tableaux

        sage: ShiftedPrimedTableau([[1,1,2.5],[1.5,2.5]])
        Traceback (most recent call last):
        ...
        ValueError: [[1, 1, 2.50000000000000], [1.50000000000000, 2.50000000000000]]
         is not an element of Shifted Primed Tableaux

        sage: ShiftedPrimedTableau([[1,1,2.5],[1.5,2.5]], primed_diagonal=True)
        [(1, 1, 3\'), (2\', 3\')]
    '''
    @staticmethod
    def __classcall_private__(cls, T, skew=None, primed_diagonal: bool = False):
        '''
        Ensure that a shifted tableau is only ever constructed as an
        ``element_class`` call of an appropriate parent.

        EXAMPLES::

            sage: data = [[1,"2\'","2",3],[2,"3\'"]]
            sage: t = ShiftedPrimedTableau(data)
            sage: T = ShiftedPrimedTableaux(shape=[4,2],weight=(1,3,2))
            sage: t == T(data)
            True
            sage: S = ShiftedPrimedTableaux(shape=[4,2])
            sage: t == S(data)
            True
            sage: t = ShiftedPrimedTableau([["2p",2,3],["2p"]],skew=[2,1])
            sage: t.parent()
            Shifted Primed Tableaux skewed by [2, 1]
            sage: s = ShiftedPrimedTableau([[None, None,"2p",2,3],[None,"2p"]])
            sage: s.parent()
            Shifted Primed Tableaux skewed by [2, 1]

        TESTS::

            sage: ShiftedPrimedTableau([])
            []
            sage: ShiftedPrimedTableau([tuple()])
            []
            sage: ShiftedPrimedTableau([], primed_diagonal=True)
            []
            sage: ShiftedPrimedTableau([tuple()], primed_diagonal=True)
            []
        '''
    def __init__(self, parent, T, skew=None, check: bool = True, preprocessed: bool = False) -> None:
        '''
        Initialize a shifted tableau.

        TESTS::

            sage: s = ShiftedPrimedTableau([[1,"2\'","3\'",3], [2,"3\'"]])
            sage: t = ShiftedPrimedTableaux([4,2])([[1,"2p","3p",3], [2,"3p"]])
            sage: s == t
            True
            sage: t.parent()
            Shifted Primed Tableaux of shape [4, 2]
            sage: s.parent()
            Shifted Primed Tableaux
            sage: r = ShiftedPrimedTableaux([4, 2])(s); r.parent()
            Shifted Primed Tableaux of shape [4, 2]
            sage: s is t  # identical shifted tableaux are distinct objects
            False

        A shifted primed tableau is deeply immutable as the rows are
        stored as tuples::

            sage: t = ShiftedPrimedTableau([[1,"2p","3p",3],[2,"3p"]])
            sage: t[0][1] = 3
            Traceback (most recent call last):
            ...
            TypeError: \'tuple\' object does not support item assignment
        '''
    def check(self) -> None:
        '''
        Check that ``self`` is a valid primed tableau.

        EXAMPLES::

            sage: T = ShiftedPrimedTableaux([4,2])
            sage: t = T([[1,\'2p\',2,2],[2,\'3p\']])
            sage: t.check()
            sage: s = ShiftedPrimedTableau([["2p",2,3],["2p"],[2]],skew=[2,1])
            sage: s.check()
            sage: t = T([[\'1p\',\'2p\',2,2],[2,\'3p\']])
            Traceback (most recent call last):
            ...
            ValueError: [[\'1p\', \'2p\', 2, 2], [2, \'3p\']] is not an element of
             Shifted Primed Tableaux of shape [4, 2]

            sage: T = ShiftedPrimedTableaux([4,2], primed_diagonal=True)
            sage: t = T([[\'1p\',\'2p\',2,2],[2,\'3p\']])  # primed_diagonal allowed
            sage: t.check()
            sage: t = T([[\'1p\',\'1p\',2,2],[2,\'3p\']])
            Traceback (most recent call last):
            ...
            ValueError: [[\'1p\', \'1p\', 2, 2], [2, \'3p\']] is not an element of
             Shifted Primed Tableaux of shape [4, 2] and maximum entry 6
        '''
    def is_standard(self):
        '''
        Return ``True`` if the entries of ``self`` are in bijection with
        positive primed integers `1\', 1, 2\', \\ldots, n`.

        EXAMPLES::

            sage: ShiftedPrimedTableau([["1\'", 1, "2\'"], [2, "3\'"]],
            ....:                      primed_diagonal=True).is_standard()
            True
            sage: ShiftedPrimedTableau([["1\'", 1, 2], ["2\'", "3\'"]],
            ....:                      primed_diagonal=True).is_standard()
            True
            sage: ShiftedPrimedTableau([["1\'", 1, 1], ["2\'", 2]],
            ....:                      primed_diagonal=True).is_standard()
            False
            sage: ShiftedPrimedTableau([[1, "2\'"], [2]]).is_standard()
            False
            sage: s = ShiftedPrimedTableau([[None, None,"1p","2p",2],[None,"1"]])
            sage: s.is_standard()
            True
        '''
    def __eq__(self, other):
        '''
        Check whether ``self`` is equal to ``other``.

        INPUT:

        - ``other`` -- the element that ``self`` is compared to

        OUTPUT: boolean

        EXAMPLES::

            sage: t = ShiftedPrimedTableau([[1,"2p"]])
            sage: t == ShiftedPrimedTableaux([2])([[1,3/2]])
            True
            sage: s = ShiftedPrimedTableau([["2p",3]], skew=[1])
            sage: s == [[None, "2p", 3]]
            True
        '''
    def __ne__(self, other):
        '''
        Check whether ``self`` is not equal to ``other``.

        INPUT:

        - ``other`` -- the element that ``self`` is compared to

        OUTPUT: boolean

        EXAMPLES::

            sage: t = ShiftedPrimedTableau([[1,"2p"]])
            sage: t != ShiftedPrimedTableaux([2])([[1,1]])
            True
            sage: s = ShiftedPrimedTableau([["2p",3]], skew=[1])
            sage: s != [[None, "2p", 3]]
            False
        '''
    def __hash__(self):
        '''
        Return the hash of ``self``.

        EXAMPLES::

            sage: t = ShiftedPrimedTableau([[1,"2p"]])
            sage: hash(t) == hash(ShiftedPrimedTableaux([2])([[1,3/2]]))
            True
        '''
    def pp(self) -> None:
        """
        Pretty print ``self``.

        EXAMPLES::

            sage: t = ShiftedPrimedTableau([[1,'2p',2,2],[2,'3p']])
            sage: t.pp()
            1  2' 2  2
               2  3'
            sage: t = ShiftedPrimedTableau([[10,'11p',11,11],[11,'12']])
            sage: t.pp()
            10  11' 11  11
                11  12
            sage: s = ShiftedPrimedTableau([['2p',2,3],['2p']],skew=[2,1])
            sage: s.pp()
             .  .  2' 2  3
                .  2'

        TESTS::

            sage: ShiftedPrimedTableau([],skew=[1]).pp()
            .
            sage: ShiftedPrimedTableau([]).pp()
            <BLANKLINE>
        """
    def max_entry(self):
        '''
        Return the minimum unprimed letter `x > y` for all `y` in ``self``.

        EXAMPLES::

            sage: Tab = ShiftedPrimedTableau([(1,1,\'2p\',\'3p\'),(2,2)])
            sage: Tab.max_entry()
            3

        TESTS::

            sage: Tab = ShiftedPrimedTableau([], skew=[2,1])
            sage: Tab.max_entry()
            0
            sage: Tab = ShiftedPrimedTableau([["1p"]], skew=[2,1])
            sage: Tab.max_entry()
            1
        '''
    def shape(self):
        '''
        Return the shape of the underlying partition of ``self``.

        EXAMPLES::

            sage: t = ShiftedPrimedTableau([[1,\'2p\',2,2],[2,\'3p\']])
            sage: t.shape()
            [4, 2]
            sage: s = ShiftedPrimedTableau([["2p",2,3],["2p"]],skew=[2,1])
            sage: s.shape()
            [5, 2] / [2, 1]
        '''
    def restrict(self, n):
        '''
        Return the restriction of the shifted tableau to all
        the numbers less than or equal to ``n``.

        .. NOTE::

            If only the outer shape of the restriction, rather than
            the whole restriction, is needed, then the faster method
            :meth:`restriction_outer_shape` is preferred. Similarly if
            only the skew shape is needed, use :meth:`restriction_shape`.

        EXAMPLES::

            sage: t = ShiftedPrimedTableau([[1,\'2p\',2,2],[2,\'3p\']])
            sage: t.restrict(2).pp()
            1  2\' 2  2
               2

            sage: t.restrict("2p").pp()
            1  2\'

            sage: s = ShiftedPrimedTableau([["2p",2,3],["2p"]], skew=[2,1])
            sage: s.restrict(2).pp()
            .  .  2\' 2
               .  2\'
            sage: s.restrict(1.5).pp()
            .  .  2\'
               .  2\'
        '''
    def restriction_outer_shape(self, n):
        '''
        Return the outer shape of the restriction of the shifted
        tableau ``self`` to `n`.

        If `T` is a (skew) shifted tableau and `n` is a half-integer,
        then the restriction of `T` to `n` is defined as the (skew)
        shifted tableau obtained by removing all cells filled with
        entries greater than `n` from `T`.

        This method computes merely the outer shape of the restriction.
        For the restriction itself, use :meth:`restrict`.

        EXAMPLES::

            sage: s = ShiftedPrimedTableau([["2p",2,3],["2p"]], skew=[2,1])
            sage: s.pp()
            .  .  2\' 2  3
               .  2\'
            sage: s.restriction_outer_shape(2)
            [4, 2]
            sage: s.restriction_outer_shape("2p")
            [3, 2]
        '''
    def restriction_shape(self, n):
        '''
        Return the skew shape of the restriction of the skew tableau
        ``self`` to ``n``.

        If `T` is a shifted tableau and `n` is a half-integer, then
        the restriction of `T` to `n` is defined as the
        (skew) shifted tableau obtained by removing all cells
        filled with entries greater than `n` from `T`.

        This method computes merely the skew shape of the restriction.
        For the restriction itself, use :meth:`restrict`.

        EXAMPLES::

            sage: s = ShiftedPrimedTableau([["2p",2,3],["2p"]], skew=[2,1])
            sage: s.pp()
             .  .  2\' 2  3
                .  2\'

            sage: s.restriction_shape(2)
            [4, 2] / [2, 1]
        '''
    def to_chain(self):
        '''
        Return the chain of partitions corresponding to the (skew)
        shifted tableau ``self``, interlaced by one of the colours
        ``1`` is the added cell is on the diagonal, ``2`` if an
        ordinary entry is added and ``3`` if a primed entry is added.

        EXAMPLES::

            sage: s = ShiftedPrimedTableau([(1, 2, 3.5, 5, 6.5), (3, 5.5)])
            sage: s.pp()
             1  2  4\' 5  7\'
                3  6\'

            sage: s.to_chain()
            [[], 1, [1], 2, [2], 1, [2, 1], 3, [3, 1], 2, [4, 1], 3, [4, 2], 3, [5, 2]]


            sage: s = ShiftedPrimedTableau([(1, 3.5), (2.5,), (6,)], skew=[2,1])
            sage: s.pp()
             .  .  1  4\'
                .  3\'
                   6

            sage: s.to_chain()
            [[2, 1], 2, [3, 1], 0, [3, 1], 3, [3, 2], 3, [4, 2], 0, [4, 2], 1, [4, 2, 1]]

        TESTS::

            sage: s = ShiftedPrimedTableau([["2p",2,3],["2p"]], skew=[2,1])
            sage: s.pp()
             .  .  2\' 2  3
                .  2\'
            sage: s.to_chain()
            Traceback (most recent call last):
            ...
            ValueError: can compute a chain of partitions only for
             skew shifted tableaux without repeated entries
        '''
    def weight(self):
        """
        Return the weight of ``self``.

        The weight of a shifted primed tableau is defined to be the vector
        with `i`-th component equal to the number of entries `i` and `i'`
        in the tableau.

        EXAMPLES::

           sage: t = ShiftedPrimedTableau([['2p',2,2],[2,'3p']], skew=[1])
           sage: t.weight()
           (0, 4, 1)
        """

class CrystalElementShiftedPrimedTableau(ShiftedPrimedTableau):
    """
    Class for elements of ``crystals.ShiftedPrimedTableau``.
    """
    def reading_word(self):
        """
        Return the reading word of ``self``.

        The reading word of a shifted primed tableau is constructed
        as follows:

        1. List all primed entries in the tableau, column by
           column, in decreasing order within each column, moving
           from the rightmost column to the left, and with all
           the primes removed (i.e. all entries are increased by
           half a unit).

        2. Then list all unprimed entries, row by row, in
           increasing order within each row, moving from the
           bottommost row to the top.

        EXAMPLES::

            sage: SPT = ShiftedPrimedTableaux([4,2])
            sage: t = SPT([[1,'2p',2,2],[2,'3p']])
            sage: t.reading_word()
            [3, 2, 2, 1, 2, 2]
        """
    def f(self, ind):
        """
        Compute the action of the crystal operator `f_i` on a shifted primed
        tableau using cases from the papers [HPS2017]_ and [AO2018]_.

        INPUT:

        - ``ind`` -- element in the index set of the crystal

        OUTPUT: primed tableau or ``None``

        EXAMPLES::

            sage: SPT = ShiftedPrimedTableaux([5,4,2])
            sage: t = SPT([[1,1,1,1,'3p'],[2,2,2,'3p'],[3,3]])
            sage: t.pp()
            1  1  1  1  3'
               2  2  2  3'
                  3  3
            sage: s = t.f(2)
            sage: s is None
            True

            sage: t = SPT([[1,1,1,'2p','3p'],[2,2,3,3],[3,4]])
            sage: t.pp()
            1  1  1  2' 3'
               2  2  3  3
                  3  4
            sage: s = t.f(2)
            sage: s.pp()
            1  1  1  2' 3'
               2  3' 3  3
                  3  4

            sage: SPT = ShiftedPrimedTableaux([2,1])
            sage: t = SPT([[1,1],[2]])
            sage: t.f(-1).pp()
            1  2'
               2
            sage: t.f(1).pp()
            1  2'
               2
            sage: t.f(2).pp()
            1  1
               3

            sage: r = SPT([[1,'2p'],[2]])
            sage: r.f(-1) is None
            True
            sage: r.f(1) is None
            True
            sage: r.f(2).pp()
            1  2'
               3

            sage: r = SPT([[1,1],[3]])
            sage: r.f(-1).pp()
            1  2'
               3
            sage: r.f(1).pp()
            1  2
               3
            sage: r.f(2) is None
            True

            sage: r = SPT([[1,2],[3]])
            sage: r.f(-1).pp()
            2  2
               3
            sage: r.f(1).pp()
            2  2
               3
            sage: r.f(2) is None
            True

            sage: t = SPT([[1,1],[2]])
            sage: t.f(-1).f(2).f(2).f(-1) == t.f(2).f(1).f(-1).f(2)
            True
            sage: t.f(-1).f(2).f(2).f(-1).pp()
            2  3'
               3
            sage: all(t.f(-1).f(2).f(2).f(-1).f(i) is None for i in {-1, 1, 2})
            True

            sage: SPT = ShiftedPrimedTableaux([4])
            sage: t = SPT([[1,1,1,1]])
            sage: t.f(-1).pp()
            1  1  1  2'
            sage: t.f(1).pp()
            1  1  1  2
            sage: t.f(-1).f(-1) is None
            True
            sage: t.f(1).f(-1).pp()
            1  1  2' 2
            sage: t.f(1).f(1).pp()
            1  1  2  2
            sage: t.f(1).f(1).f(-1).pp()
            1  2' 2  2
            sage: t.f(1).f(1).f(1).pp()
            1  2  2  2
            sage: t.f(1).f(1).f(1).f(-1).pp()
            2  2  2  2
            sage: t.f(1).f(1).f(1).f(1).pp()
            2  2  2  2
            sage: t.f(1).f(1).f(1).f(1).f(-1) is None
            True
        """
    def e(self, ind):
        """
        Compute the action of the crystal operator `e_i` on a shifted primed
        tableau using cases from the papers [HPS2017]_ and [AO2018]_.

        INPUT:

        - ``ind`` -- an element in the index set of the crystal

        OUTPUT: primed tableau or ``None``

        EXAMPLES::

            sage: SPT = ShiftedPrimedTableaux([5,4,2])
            sage: t = SPT([[1,1,1,'2p','3p'], [2,'3p',3,3],[3,4]])
            sage: t.pp()
            1  1  1  2' 3'
               2  3' 3  3
                  3  4
            sage: s = t.e(2)
            sage: s.pp()
            1  1  1  2' 3'
               2  2  3  3
                  3  4
            sage: t == s.f(2)
            True

            sage: SPT = ShiftedPrimedTableaux([2,1])
            sage: t = SPT([[2,'3p'],[3]])
            sage: t.e(-1).pp()
            1  3'
               3
            sage: t.e(1).pp()
            1  3'
               3
            sage: t.e(2).pp()
            2  2
               3

            sage: r = SPT([[2, 2],[3]])
            sage: r.e(-1).pp()
            1  2
               3
            sage: r.e(1).pp()
            1  2
               3
            sage: r.e(2) is None
            True

            sage: r = SPT([[1,'3p'],[3]])
            sage: r.e(-1) is None
            True
            sage: r.e(1) is None
            True
            sage: r.e(2).pp()
            1  2'
               3
            sage: r = SPT([[1,'2p'],[3]])
            sage: r.e(-1).pp()
            1  1
               3
            sage: r.e(1) is None
            True
            sage: r.e(2).pp()
            1  2'
               2
            sage: t = SPT([[2,'3p'],[3]])
            sage: t.e(-1).e(2).e(2).e(-1) == t.e(2).e(1).e(1).e(2)
            True
            sage: t.e(-1).e(2).e(2).e(-1).pp()
            1  1
               2
            sage: all(t.e(-1).e(2).e(2).e(-1).e(i) is None for i in {-1, 1, 2})
            True

            sage: SPT = ShiftedPrimedTableaux([4])
            sage: t = SPT([[2,2,2,2]])
            sage: t.e(-1).pp()
            1  2  2  2
            sage: t.e(1).pp()
            1  2  2  2
            sage: t.e(-1).e(-1) is None
            True
            sage: t.e(1).e(1).pp()
            1  1  2  2
        """
    def is_highest_weight(self, index_set=None):
        '''
        Return whether ``self`` is a highest weight element of the crystal.

        An element is highest weight if it vanishes under all crystal
        operators `e_i`.

        EXAMPLES::

            sage: SPT = ShiftedPrimedTableaux([5,4,2])
            sage: t = SPT([(1, 1, 1, 1, 1), (2, 2, 2, "3p"), (3, 3)])
            sage: t.is_highest_weight()
            True

            sage: SPT = ShiftedPrimedTableaux([5,4])
            sage: s = SPT([(1, 1, 1, 1, 1), (2, 2, "3p", 3)])
            sage: s.is_highest_weight(index_set=[1])
            True
        '''
    def weight(self):
        """
        Return the weight of ``self``.

        The weight of a shifted primed tableau is defined to be the vector
        with `i`-th component equal to the number of entries `i` and `i'`
        in the tableau.

        EXAMPLES::

           sage: t = ShiftedPrimedTableau([[1,'2p',2,2],[2,'3p']])
           sage: t.weight()
           (1, 4, 1)
        """

class PrimedEntry(SageObject):
    """
    The class of entries in shifted primed tableaux.

    An entry in a shifted primed tableau is an element in
    the alphabet `\\{1' < 1 < 2' < 2 < \\cdots < n' < n\\}`.
    The difference between two elements `i` and `i-1` counts as a
    whole unit, whereas the difference between `i` and `i'` counts
    as half a unit.
    Internally, we represent an unprimed element `x` as `2x`
    and the primed elements as the corresponding odd integer
    that respects the total order.

    INPUT:

    - ``entry`` -- half integer or string of an integer
      possibly ending in ``p`` or ``'``
    - ``double`` -- the doubled value
    """
    def __init__(self, entry=None, double=None) -> None:
        '''
        Normalize the entry.

        TESTS::

            sage: from sage.combinat.shifted_primed_tableau import PrimedEntry
            sage: PrimedEntry(2)
            2
            sage: PrimedEntry("2p")
            2\'
            sage: PrimedEntry("2\'")
            2\'
            sage: a = PrimedEntry(2.5)
            sage: PrimedEntry(a)
            3\'
            sage: PrimedEntry(None)
            Traceback (most recent call last):
            ...
            ValueError: primed entry must not be None
        '''
    def __hash__(self):
        '''
        TESTS::

            sage: from sage.combinat.shifted_primed_tableau import PrimedEntry
            sage: a = PrimedEntry("2p")
            sage: b = PrimedEntry("2\'")
            sage: a == b
            True
        '''
    def integer(self):
        '''
        Return the corresponding integer `i` for primed entries
        of the form `i` or `i\'`.

        TESTS::

            sage: from sage.combinat.shifted_primed_tableau import PrimedEntry
            sage: b = PrimedEntry("2p").integer()
            sage: b
            2
            sage: b.category()
            Category of elements of Integer Ring
        '''
    def __eq__(self, other):
        '''
        TESTS::

            sage: from sage.combinat.shifted_primed_tableau import PrimedEntry
            sage: a = PrimedEntry("2p")
            sage: b = PrimedEntry("2\'")
            sage: a == b
            True
        '''
    def __ne__(self, other):
        '''
        TESTS::

            sage: from sage.combinat.shifted_primed_tableau import PrimedEntry
            sage: a = PrimedEntry("1")
            sage: b = PrimedEntry(1)
            sage: a != b
            False
        '''
    def __lt__(self, other):
        '''
        TESTS::

            sage: from sage.combinat.shifted_primed_tableau import PrimedEntry
            sage: a = PrimedEntry("2p")
            sage: b = PrimedEntry(2)
            sage: a < b
            True
        '''
    def __le__(self, other):
        '''
        TESTS::

            sage: from sage.combinat.shifted_primed_tableau import PrimedEntry
            sage: a = PrimedEntry(2)
            sage: b = PrimedEntry("3p")
            sage: a <= b
            True
        '''
    def __gt__(self, other):
        '''
        TESTS::

            sage: from sage.combinat.shifted_primed_tableau import PrimedEntry
            sage: a = PrimedEntry("2p")
            sage: b = PrimedEntry(2)
            sage: b > a
            True
        '''
    def __ge__(self, other):
        '''
        TESTS::

            sage: from sage.combinat.shifted_primed_tableau import PrimedEntry
            sage: a = PrimedEntry(2)
            sage: b = PrimedEntry("3p")
            sage: a >= b
            False
        '''
    def is_unprimed(self):
        '''
        Check if ``self`` is an unprimed element.

        TESTS::

            sage: from sage.combinat.shifted_primed_tableau import PrimedEntry
            sage: a = PrimedEntry("2p")
            sage: a.is_unprimed()
            False
        '''
    def is_primed(self):
        '''
        Check if ``self`` is a primed element.

        TESTS::

            sage: from sage.combinat.shifted_primed_tableau import PrimedEntry
            sage: a = PrimedEntry("3p")
            sage: a.is_primed()
            True
        '''
    def unprimed(self):
        '''
        Unprime ``self`` if it is a primed element.

        TESTS::

            sage: from sage.combinat.shifted_primed_tableau import PrimedEntry
            sage: a = PrimedEntry("2p")
            sage: a.unprimed()
            2
        '''
    def primed(self):
        """
        Prime ``self`` if it is an unprimed element.

        TESTS::

            sage: from sage.combinat.shifted_primed_tableau import PrimedEntry
            sage: a = PrimedEntry(1)
            sage: a.primed()
            1'
        """
    def increase_half(self):
        """
        Increase ``self`` by half a unit.

        TESTS::

            sage: from sage.combinat.shifted_primed_tableau import PrimedEntry
            sage: a = PrimedEntry(1)
            sage: a.increase_half()
            2'
        """
    def decrease_half(self):
        """
        Decrease ``self`` by half a unit.

        TESTS::

            sage: from sage.combinat.shifted_primed_tableau import PrimedEntry
            sage: a = PrimedEntry(1)
            sage: a.decrease_half()
            1'
        """
    def increase_one(self):
        '''
        Increase ``self`` by one unit.

        TESTS::

            sage: from sage.combinat.shifted_primed_tableau import PrimedEntry
            sage: a = PrimedEntry("2p")
            sage: a.increase_one()
            3\'
        '''
    def decrease_one(self):
        '''
        Decrease ``self`` by one unit.

        TESTS::

            sage: from sage.combinat.shifted_primed_tableau import PrimedEntry
            sage: a = PrimedEntry("2p")
            sage: a.decrease_one()
            1\'
        '''

class ShiftedPrimedTableaux(UniqueRepresentation, Parent):
    """
    Return the combinatorial class of shifted primed tableaux subject
    to the constraints given by the arguments.

    A primed tableau is a tableau of shifted shape on the alphabet
    `X' = \\{1' < 1 < 2' < 2 < \\cdots < n' < n\\}` such that

    1. the entries are weakly increasing along rows and columns

    2. a row cannot have two repeated primed entries, and a column
       cannot have two repeated non-primed entries

    INPUT:

    Valid optional keywords:

    - ``shape`` -- the (outer skew) shape of tableaux

    - ``weight`` -- the weight of tableaux

    - ``max_entry`` -- the maximum entry of tableaux

    - ``skew`` -- the inner skew shape of tableaux

    - ``primed_diagonal`` -- allow primed entries in main diagonal of tableaux

    The weight of a tableau is defined to be the vector with `i`-th
    component equal to the number of entries `i` and `i'` in the tableau.
    The sum of the coordinates in the weight vector must be equal to the
    number of entries in the partition.

    The ``shape`` and ``skew`` must be strictly decreasing partitions.
    The ``primed_diagonal`` is a boolean (default: ``False``).

    EXAMPLES::

        sage: SPT = ShiftedPrimedTableaux(weight=(1,2,2), shape=[3,2]); SPT
        Shifted Primed Tableaux of weight (1, 2, 2) and shape [3, 2]
        sage: SPT.list()
        [[(1, 2, 2), (3, 3)],
         [(1, 2', 3'), (2, 3)],
         [(1, 2', 3'), (2, 3')],
         [(1, 2', 2), (3, 3)]]
        sage: SPT = ShiftedPrimedTableaux(weight=(1,2,2), shape=[3,2],
        ....:                             primed_diagonal=True); SPT
        Shifted Primed Tableaux of weight (1, 2, 2) and shape [3, 2]
        sage: SPT.list()
        [[(1, 2, 2), (3, 3)],
         [(1, 2, 2), (3', 3)],
         [(1, 2', 3'), (2, 3)],
         [(1, 2', 3'), (2, 3')],
         [(1, 2', 3'), (2', 3)],
         [(1, 2', 3'), (2', 3')],
         [(1, 2', 2), (3, 3)],
         [(1, 2', 2), (3', 3)],
         [(1', 2, 2), (3, 3)],
         [(1', 2, 2), (3', 3)],
         [(1', 2', 3'), (2, 3)],
         [(1', 2', 3'), (2, 3')],
         [(1', 2', 3'), (2', 3)],
         [(1', 2', 3'), (2', 3')],
         [(1', 2', 2), (3, 3)],
         [(1', 2', 2), (3', 3)]]
        sage: SPT = ShiftedPrimedTableaux(weight=(1,2)); SPT
        Shifted Primed Tableaux of weight (1, 2)
        sage: list(SPT)
        [[(1, 2, 2)], [(1, 2', 2)], [(1, 2'), (2,)]]
        sage: SPT = ShiftedPrimedTableaux(weight=(1,2), primed_diagonal=True)
        sage: list(SPT)
        [[(1, 2, 2)],
         [(1, 2', 2)],
         [(1', 2, 2)],
         [(1', 2', 2)],
         [(1, 2'), (2,)],
         [(1, 2'), (2',)],
         [(1', 2'), (2,)],
         [(1', 2'), (2',)]]
        sage: SPT = ShiftedPrimedTableaux([3,2], max_entry=2); SPT
        Shifted Primed Tableaux of shape [3, 2] and maximum entry 2
        sage: list(SPT)
        [[(1, 1, 1), (2, 2)], [(1, 1, 2'), (2, 2)]]
        sage: SPT = ShiftedPrimedTableaux([3,2], max_entry=2,
        ....:                             primed_diagonal=True)
        sage: list(SPT)
        [[(1, 1, 1), (2, 2)],
         [(1, 1, 1), (2', 2)],
         [(1', 1, 1), (2, 2)],
         [(1', 1, 1), (2', 2)],
         [(1, 1, 2'), (2, 2)],
         [(1, 1, 2'), (2', 2)],
         [(1', 1, 2'), (2, 2)],
         [(1', 1, 2'), (2', 2)]]

    TESTS::

        sage: [(1,'2p',2,2),(2,'3p')] in ShiftedPrimedTableaux()
        True
        sage: [('1p','2p',2,2),(2,'3p')] in ShiftedPrimedTableaux()
        False
        sage: [(1,1),(2,2)] in ShiftedPrimedTableaux()
        False
        sage: [] in ShiftedPrimedTableaux()
        True
        sage: [('1p','2p',2,2),(2,'3p')] in ShiftedPrimedTableaux(
        ....:                                      primed_diagonal=True)
        True
        sage: [] in ShiftedPrimedTableaux(primed_diagonal=True)
        True

    .. SEEALSO::

        - :class:`ShiftedPrimedTableau`
    """
    Element = ShiftedPrimedTableau
    options = Tableaux.options
    @staticmethod
    def __classcall_private__(cls, shape=None, weight=None, max_entry=None, skew=None, primed_diagonal: bool = False):
        """
        Normalize and process input to return the correct parent and
        ensure a unique representation.

        TESTS::

            sage: ShiftedPrimedTableaux([])
            Shifted Primed Tableaux of shape []
            sage: ShiftedPrimedTableaux(3)
            Traceback (most recent call last):
            ...
            ValueError: invalid shape argument
            sage: ShiftedPrimedTableaux(weight=(2,2,2), shape=[3,2])
            Traceback (most recent call last):
            ...
            ValueError: weight and shape are incompatible
            sage: ShiftedPrimedTableaux([[1]])
            Traceback (most recent call last):
            ...
            ValueError: invalid shape argument
            sage: ShiftedPrimedTableaux(weight=(2,2,2), max_entry=2)
            Traceback (most recent call last):
            ...
            ValueError: maximum entry is incompatible with the weight
            sage: ShiftedPrimedTableaux(shape=[4,1],skew=[3,2])
            Traceback (most recent call last):
            ...
            ValueError: skew shape must be inside the given tableau shape

            sage: SPT1 = ShiftedPrimedTableaux(weight=())
            sage: SPT2 = ShiftedPrimedTableaux(weight=(0,0,0))
            sage: SPT1 is SPT2
            True
        """
    def __init__(self, skew=None, primed_diagonal: bool = False) -> None:
        """
        Initialization of the parent class with given skew shape.

        TESTS::

            sage: SPT = ShiftedPrimedTableaux(skew=[1])
            sage: TestSuite(SPT).run()  # known bug
        """

class ShiftedPrimedTableaux_all(ShiftedPrimedTableaux):
    """
    The class of all shifted primed tableaux.
    """
    def __init__(self, skew=None, primed_diagonal: bool = False) -> None:
        """
        Initialize the class of all shifted tableaux.

        TESTS::

            sage: SPT = ShiftedPrimedTableaux()
            sage: [[1,1.5],[2]] in SPT
            True
            sage: [[1,1.5],[1.5]] in SPT
            False
            sage: [[1,1],[1]] in SPT
            False
            sage: [[1,1],[2,2]] in SPT
            False
            sage: TestSuite(SPT).run()  # long time

            sage: Primed_SPT = ShiftedPrimedTableaux(primed_diagonal=True)
            sage: [[0.5,1.5],[2]] in Primed_SPT
            True
            sage: [[0.5,1.5],[1.5]] in Primed_SPT
            True
            sage: [[0.5,1],[1]] in Primed_SPT
            False
            sage: TestSuite(Primed_SPT).run()  # long time
        """
    def __iter__(self):
        """
        Iterate over ``self``.

        EXAMPLES::

            sage: Tabs = ShiftedPrimedTableaux()
            sage: Tabs[:5]
            [[], [(1,)], [(2,)], [(1, 2)], [(1, 2')]]
            sage: Tabs = ShiftedPrimedTableaux(primed_diagonal=True)
            sage: Tabs[:5]
            [[], [(1,)], [(1',)], [(2,)], [(2',)]]
        """

class ShiftedPrimedTableaux_shape(ShiftedPrimedTableaux):
    """
    Shifted primed tableaux of a fixed shape.

    Shifted primed tableaux admit a type `A_n` classical crystal structure
    with highest weights corresponding to a given shape.

    The list of module generators consists of all elements of the
    crystal with nonincreasing weight entries.

    The crystal is constructed following operations described in [HPS2017]_
    and [AO2018]_.

    The optional ``primed_diagonal`` allows primed entries in the main diagonal
    of all the Shifted primed tableaux of a fixed shape. If the ``max_entry``
    is ``None`` then ``max_entry`` is set to the total number of entries in the
    tableau if ``primed_diagonal`` is ``True``.

    EXAMPLES::

        sage: ShiftedPrimedTableaux([4,3,1], max_entry=4)
        Shifted Primed Tableaux of shape [4, 3, 1] and maximum entry 4
        sage: ShiftedPrimedTableaux([4,3,1], max_entry=4).cardinality()
        384

    We compute some of the crystal structure::

        sage: SPTC = crystals.ShiftedPrimedTableaux([3,2], 3)
        sage: T = SPTC.module_generators[-1]
        sage: T
        [(1, 1, 2'), (2, 3')]
        sage: T.f(2)
        [(1, 1, 3'), (2, 3')]
        sage: len(SPTC.module_generators)
        7
        sage: SPTC[0]
        [(1, 1, 1), (2, 2)]
        sage: SPTC.cardinality()
        24

    We compare this implementation with the `q(n)`-crystal
    on (tensor products) of letters::

        sage: tableau_crystal = crystals.ShiftedPrimedTableaux([4,1], 3)
        sage: tableau_digraph = tableau_crystal.digraph()
        sage: c = crystals.Letters(['Q', 3])
        sage: tensor_crystal = tensor([c]*5)
        sage: u = tensor_crystal(c(1), c(1), c(1), c(2), c(1))
        sage: subcrystal = tensor_crystal.subcrystal(generators=[u],
        ....:                                        index_set=[1,2,-1])
        sage: tensor_digraph = subcrystal.digraph()
        sage: tensor_digraph.is_isomorphic(tableau_digraph, edge_labels=True)
        True

    If we allow primed entries in the main diagonal::

        sage: ShiftedPrimedTableaux([4,3,1], max_entry=4,
        ....:                        primed_diagonal=True)
        Shifted Primed Tableaux of shape [4, 3, 1] and maximum entry 4
        sage: ShiftedPrimedTableaux([4,3,1], max_entry=4,
        ....:                       primed_diagonal=True).cardinality()
        3072
        sage: SPTC = ShiftedPrimedTableaux([3,2], max_entry=3,
        ....:                              primed_diagonal=True)
        sage: T = SPTC[-1]
        sage: T
        [(1', 2', 2), (3', 3)]
        sage: SPTC[0]
        [(1, 1, 1), (2, 2)]
        sage: SPTC.cardinality()
        96
    """
    @staticmethod
    def __classcall_private__(cls, shape, max_entry=None, skew=None, primed_diagonal: bool = False):
        """
        Normalize the attributes for the class.

        TESTS::

            sage: SPT = ShiftedPrimedTableaux(shape=[2,1])
            sage: SPT._shape.parent()
            Partitions

            sage: SPT1 = ShiftedPrimedTableaux(shape=(2,1), max_entry=3)
            sage: SPT2 = ShiftedPrimedTableaux(shape=[2,1], max_entry=3)
            sage: SPT1 is SPT2
            True
        """
    Element: Incomplete
    def __init__(self, shape, max_entry=None, skew=None, primed_diagonal: bool = False) -> None:
        """
        Initialize the class of shifted primed tableaux of a given shape.

        If ``max_elt`` is specified, a finite set with entries smaller
        or equal to ``max_elt``.

        TESTS::

            sage: SPT = ShiftedPrimedTableaux([4,2,1], max_entry=4)
            sage: TestSuite(SPT).run()  # long time
            sage: SPT.cartan_type()
            ['Q', 4]

            sage: SPT = ShiftedPrimedTableaux([4,2,1])
            sage: SPT.cartan_type()
            ['A', NN]
            sage: SPT = ShiftedPrimedTableaux([4,2,1], max_entry=4,
            ....:                             primed_diagonal=True)
            sage: TestSuite(SPT).run()  # long time
        """
    def __iter__(self):
        """
        Iterate over ``self``.

        EXAMPLES::

            sage: Tabs = ShiftedPrimedTableaux(shape=(3,2), max_entry=5)
            sage: Tabs[:4]
            [[(1, 1, 1), (2, 2)],
             [(1, 1, 1), (2, 3)],
             [(1, 1, 1), (2, 3')],
             [(1, 1, 2), (2, 3)]]
            sage: len(list(Tabs))
            376
            sage: Tabs = ShiftedPrimedTableaux(shape=(3,2), primed_diagonal=True)
            sage: Tabs[:4]
            [[(1, 1, 1), (2, 2)],
             [(1, 1, 1), (2', 2)],
             [(1', 1, 1), (2, 2)],
             [(1', 1, 1), (2', 2)]]
            sage: len(list(Tabs))
            1504
        """
    @lazy_attribute
    def module_generators(self):
        """
        Return the generators of ``self`` as a crystal.

        TESTS::

            sage: SPT = ShiftedPrimedTableaux(shape=[2,1])
            sage: SPT.module_generators
            ([(1, 1), (2,)], [(1, 2), (3,)], [(1, 2'), (3,)])
        """
    def shape(self):
        """
        Return the shape of the shifted tableaux ``self``.

        TESTS::

            sage: ShiftedPrimedTableaux([6,4,3,1]).shape()
            [6, 4, 3, 1]
        """

class ShiftedPrimedTableaux_weight(ShiftedPrimedTableaux):
    """
    Shifted primed tableaux of fixed weight.

    EXAMPLES::

        sage: ShiftedPrimedTableaux(weight=(2,3,1))
        Shifted Primed Tableaux of weight (2, 3, 1)
        sage: ShiftedPrimedTableaux(weight=(2,3,1)).cardinality()
        17
        sage: SPT = ShiftedPrimedTableaux(weight=(2,3,1), primed_diagonal=True)
        sage: SPT.cardinality()
        64
        sage: T = ShiftedPrimedTableaux(weight=(3,2), primed_diagonal=True)
        sage: T[:5]
        [[(1, 1, 1, 2, 2)],
         [(1, 1, 1, 2', 2)],
         [(1', 1, 1, 2, 2)],
         [(1', 1, 1, 2', 2)],
         [(1, 1, 1, 2), (2,)]]
        sage: T.cardinality()
        16
    """
    def __init__(self, weight, skew=None, primed_diagonal: bool = False) -> None:
        """
        Initialize the class of shifted primed tableaux of a given weight.

        TESTS::

            sage: TestSuite( ShiftedPrimedTableaux(weight=(3,2,1)) ).run()
            sage: TestSuite( ShiftedPrimedTableaux(weight=(3,2,1),
            ....:                               primed_diagonal=True) ).run()
        """
    def __iter__(self):
        """
        Iterate over ``self``.

        EXAMPLES::

            sage: Tabs = ShiftedPrimedTableaux(weight=(2,3))
            sage: Tabs[:4]
            [[(1, 1, 2, 2, 2)],
             [(1, 1, 2', 2, 2)],
             [(1, 1, 2, 2), (2,)],
             [(1, 1, 2', 2), (2,)]]
            sage: len(list(Tabs))
            5
            sage: Tabs = ShiftedPrimedTableaux(weight=(2,3),
            ....:                              primed_diagonal=True)
            sage: Tabs[:4]
            [[(1, 1, 2, 2, 2)],
             [(1, 1, 2', 2, 2)],
             [(1', 1, 2, 2, 2)],
             [(1', 1, 2', 2, 2)]]
            sage: len(list(Tabs))
            16
        """

class ShiftedPrimedTableaux_weight_shape(ShiftedPrimedTableaux):
    """
    Shifted primed tableaux of the fixed weight and shape.

    EXAMPLES::

        sage: ShiftedPrimedTableaux([4,2,1], weight=(2,3,2))
        Shifted Primed Tableaux of weight (2, 3, 2) and shape [4, 2, 1]
        sage: ShiftedPrimedTableaux([4,2,1], weight=(2,3,2)).cardinality()
        4
        sage: T = ShiftedPrimedTableaux([4,2,1], weight=(2,3,2),
        ....:                           primed_diagonal=True)
        sage: T[:6]
        [[(1, 1, 2, 2), (2, 3'), (3,)],
         [(1, 1, 2, 2), (2, 3'), (3',)],
         [(1, 1, 2, 2), (2', 3'), (3,)],
         [(1, 1, 2, 2), (2', 3'), (3',)],
         [(1, 1, 2', 3), (2, 2), (3,)],
         [(1, 1, 2', 3), (2, 2), (3',)]]
        sage: T.cardinality()
        32
    """
    def __init__(self, weight, shape, skew=None, primed_diagonal: bool = False) -> None:
        """
        Initialize the class of shifted primed tableaux of the given weight
        and shape.

        TESTS::

            sage: TestSuite( ShiftedPrimedTableaux([4,2,1],
            ....:                                  weight=(3,2,2)) ).run()
            sage: TestSuite( ShiftedPrimedTableaux([4,2,1],
            ....:                 weight=(3,2,2), primed_diagonal=True) ).run()
        """
    def __iter__(self):
        """
        Iterate over ``self``.

        EXAMPLES::

            sage: Tabs = ShiftedPrimedTableaux([3,2], weight=(1,2,2))
            sage: Tabs[:4]
            [[(1, 2, 2), (3, 3)],
             [(1, 2', 3'), (2, 3)],
             [(1, 2', 3'), (2, 3')],
             [(1, 2', 2), (3, 3)]]
            sage: len(list(Tabs))
            4
            sage: Tabs = ShiftedPrimedTableaux([3,2],weight=(1,2,2),
            ....:                              primed_diagonal=True)
            sage: Tabs[:4]
            [[(1, 2, 2), (3, 3)],
             [(1, 2, 2), (3', 3)],
             [(1, 2', 3'), (2, 3)],
             [(1, 2', 3'), (2, 3')]]
            sage: len(list(Tabs))
            16

        TESTS::

            sage: Tabs = ShiftedPrimedTableaux([3,2], weight=(1,4))
            sage: list(Tabs)
            []
        """
