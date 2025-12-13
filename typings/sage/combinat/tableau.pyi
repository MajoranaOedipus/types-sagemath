from _typeshed import Incomplete
from collections.abc import Generator
from sage.arith.misc import binomial as binomial, factorial as factorial, multinomial as multinomial
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.categories.infinite_enumerated_sets import InfiniteEnumeratedSets as InfiniteEnumeratedSets
from sage.categories.sets_cat import Sets as Sets
from sage.combinat import permutation as permutation
from sage.combinat.combinatorial_map import combinatorial_map as combinatorial_map
from sage.combinat.composition import Composition as Composition, Compositions as Compositions
from sage.combinat.integer_vector import IntegerVectors as IntegerVectors, integer_vectors_nk_fast_iter as integer_vectors_nk_fast_iter
from sage.combinat.subset import powerset as powerset
from sage.misc.inherit_comparison import InheritComparisonClasscallMetaclass as InheritComparisonClasscallMetaclass
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod
from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as IntegerModRing
from sage.rings.infinity import PlusInfinity as PlusInfinity
from sage.rings.integer import Integer as Integer
from sage.sets.disjoint_union_enumerated_sets import DisjointUnionEnumeratedSets as DisjointUnionEnumeratedSets
from sage.sets.family import Family as Family
from sage.sets.non_negative_integers import NonNegativeIntegers as NonNegativeIntegers
from sage.structure.global_options import GlobalOptions as GlobalOptions
from sage.structure.list_clone import ClonableList as ClonableList
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import richcmp as richcmp, richcmp_method as richcmp_method
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class Tableau(ClonableList, metaclass=InheritComparisonClasscallMetaclass):
    """
    A class to model a tableau.

    INPUT:

    - ``t`` -- a Tableau, a list of iterables, or an empty list

    OUTPUT: a Tableau object constructed from ``t``

    A tableau is abstractly a mapping from the cells in a partition to
    arbitrary objects (called entries). It is often represented as a
    finite list of nonempty lists (or, more generally an iterator of
    iterables) of weakly decreasing lengths. This list,
    in particular, can be empty, representing the empty tableau.

    Note that Sage uses the English convention for partitions and
    tableaux; the longer rows are displayed on top.

    EXAMPLES::

        sage: t = Tableau([[1,2,3],[4,5]]); t
        [[1, 2, 3], [4, 5]]
        sage: t.shape()
        [3, 2]
        sage: t.pp() # pretty printing
        1 2 3
        4 5
        sage: t.is_standard()
        True

        sage: Tableau([['a','c','b'],[[],(2,1)]])
        [['a', 'c', 'b'], [[], (2, 1)]]
        sage: Tableau([]) # The empty tableau
        []

    When using code that will generate a lot of tableaux, it is slightly more
    efficient to construct a Tableau from the appropriate Parent object::

        sage: T = Tableaux()
        sage: T([[1, 2, 3], [4, 5]])
        [[1, 2, 3], [4, 5]]

    .. SEEALSO::

        - :class:`Tableaux`
        - :class:`SemistandardTableaux`
        - :class:`SemistandardTableau`
        - :class:`StandardTableaux`
        - :class:`StandardTableau`

    TESTS::

        sage: Tableau([[1],[2,3]])
        Traceback (most recent call last):
        ...
        ValueError: a tableau must be a list of iterables of weakly decreasing length
        sage: Tableau([1,2,3])
        Traceback (most recent call last):
        ...
        ValueError: a tableau must be a list of iterables
    """
    @staticmethod
    def __classcall_private__(cls, t):
        """
        This ensures that a tableau is only ever constructed as an
        ``element_class`` call of an appropriate parent.

        TESTS::

            sage: t = Tableau([[1,1],[1]])
            sage: TestSuite(t).run()

            sage: t.parent()
            Tableaux
            sage: t.category()
            Category of elements of Tableaux
            sage: type(t)
            <class 'sage.combinat.tableau.Tableaux_all_with_category.element_class'>
        """
    def __init__(self, parent, t, check: bool = True) -> None:
        """
        Initialize a tableau.

        TESTS::

            sage: t = Tableaux()([[1,1],[1]])
            sage: s = Tableaux(3)([[1,1],[1]])
            sage: s == t
            True
            sage: t.parent()
            Tableaux
            sage: s.parent()
            Tableaux of size 3
            sage: r = Tableaux()(s); r.parent()
            Tableaux
            sage: s is t # identical tableaux are distinct objects
            False

        A tableau is shallowly immutable. See :issue:`15862`. The entries
        themselves may be mutable objects, though in that case the
        resulting Tableau should be unhashable. ::

            sage: T = Tableau([[1,2],[2]])
            sage: t0 = T[0]
            sage: t0[1] = 3
            Traceback (most recent call last):
            ...
            TypeError: 'tuple' object does not support item assignment
            sage: T[0][1] = 5
            Traceback (most recent call last):
            ...
            TypeError: 'tuple' object does not support item assignment
        """
    def __richcmp__(self, other, op):
        """
        Compare ``self`` to ``other``.

        .. TODO::

            This overwrites the comparison check of
            :class:`~sage.structure.list_clone.ClonableList`
            in order to circumvent the coercion framework.
            Eventually this should be solved more elegantly,
            for example along the lines of what was done for
            `k`-tableaux.

            For now, this compares two elements by their underlying
            defining lists.

        INPUT:

        - ``other`` -- the element that ``self`` is compared to

        OUTPUT: boolean

        TESTS::

            sage: t = Tableau([[1,2]])
            sage: t == 0
            False
            sage: t == Tableaux(2)([[1,2]])
            True

            sage: s = Tableau([[2,3],[1]])
            sage: s != []
            True

            sage: t < s
            True
            sage: s < t
            False
            sage: s > t
            True
        """
    def __hash__(self):
        """
        Return the hash of ``self``.

        EXAMPLES::

            sage: t = Tableau([[1,1],[2]])
            sage: hash(tuple(t)) == hash(t)
            True
        """
    def check(self) -> None:
        """
        Check that ``self`` is a valid straight-shape tableau.

        EXAMPLES::

            sage: t = Tableau([[1,1],[2]])
            sage: t.check()

            sage: t = Tableau([[None, None, 1], [2, 4], [3, 4, 5]])  # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: a tableau must be a list of iterables of weakly decreasing length
        """
    def __truediv__(self, t):
        """
        Return the skew tableau ``self``/``t``, where ``t`` is a partition
        contained in the shape of ``self``.

        EXAMPLES::

            sage: t = Tableau([[1,2,3],[3,4],[5]])
            sage: t/[1,1]
            [[None, 2, 3], [None, 4], [5]]
            sage: t/[3,1]
            [[None, None, None], [None, 4], [5]]
            sage: t/[2,1,1,1]
            Traceback (most recent call last):
            ...
            ValueError: the shape of the tableau must contain the partition
        """
    def __call__(self, *cell):
        """

        INPUT:

        - ``cell`` -- a pair of integers, tuple, or list specifying a cell in
          the tableau

        OUTPUT: the value in the corresponding cell

        EXAMPLES::

            sage: t = Tableau([[1,2,3],[4,5]])
            sage: t(1,0)
            4
            sage: t((1,0))
            4
            sage: t(3,3)
            Traceback (most recent call last):
            ...
            IndexError: the cell (3,3) is not contained in [[1, 2, 3], [4, 5]]
        """
    def level(self):
        """
        Return the level of ``self``, which is always 1.

        This function exists mainly for compatibility with
        :class:`TableauTuple`.

        EXAMPLES::

            sage: Tableau([[1,2,3],[4,5]]).level()
            1
        """
    def components(self):
        """
        This function returns a list containing itself. It exists mainly for
        compatibility with :class:`TableauTuple` as it allows constructions
        like the example below.

        EXAMPLES::

            sage: t = Tableau([[1,2,3],[4,5]])
            sage: for s in t.components(): print(s.to_list())
            [[1, 2, 3], [4, 5]]
        """
    def shape(self):
        """
        Return the shape of a tableau ``self``.

        EXAMPLES::

            sage: Tableau([[1,2,3],[4,5],[6]]).shape()
            [3, 2, 1]
        """
    def size(self):
        """
        Return the size of the shape of the tableau ``self``.

        EXAMPLES::

            sage: Tableau([[1, 4, 6], [2, 5], [3]]).size()
            6
            sage: Tableau([[1, 3], [2, 4]]).size()
            4
        """
    def corners(self):
        """
        Return the corners of the tableau ``self``.

        EXAMPLES::

            sage: Tableau([[1, 4, 6], [2, 5], [3]]).corners()
            [(0, 2), (1, 1), (2, 0)]
            sage: Tableau([[1, 3], [2, 4]]).corners()
            [(1, 1)]
        """
    def conjugate(self):
        """
        Return the conjugate of ``self``.

        EXAMPLES::

            sage: Tableau([[1,2],[3,4]]).conjugate()
            [[1, 3], [2, 4]]
            sage: c = StandardTableau([[1,2],[3,4]]).conjugate()
            sage: c.parent()
            Standard tableaux
        """
    def pp(self) -> None:
        '''
        Pretty print a string of the tableau.

        EXAMPLES::

            sage: T = Tableau([[1,2,3],[3,4],[5]])
            sage: T.pp()
              1  2  3
              3  4
              5
            sage: Tableaux.options.convention="french"
            sage: T.pp()
              5
              3  4
              1  2  3
            sage: Tableaux.options.convention="russian"
            sage: T.pp()
             5    4    3
                3    2
                   1
            sage: Tableaux.options._reset()
        '''
    def plot(self, descents: bool = False):
        '''
        Return a plot ``self``.

        If English notation is set then the first row of the tableau is on the
        top:

        .. PLOT::
            :width: 200 px

            t = Tableau([[1,2,3,4],[2,3],[5]])
            Tableaux.options.convention="english"
            sphinx_plot(t.plot())

        If French notation is set, the first row of the tableau is on
        the bottom:

        .. PLOT::
            :width: 200 px

            t = Tableau([[1,2,3,4],[2,3],[5]])
            Tableaux.options.convention="french"
            sphinx_plot(t.plot())
            Tableaux.options.convention="english"

        If Russian notation is set, we tilt the French notation by 45 degrees:

        .. PLOT::
            :width: 200 px

            t = Tableau([[1,2,3,4],[2,3],[5]])
            Tableaux.options.convention="russian"
            sphinx_plot(t.plot())
            Tableaux.options.convention="english"

        INPUT:

        - ``descents`` -- boolean (default: ``False``); if ``True``,
          then the descents are marked in the tableau; only valid if
          ``self`` is a standard tableau

        EXAMPLES::

            sage: t = Tableau([[1,2,4],[3]])
            sage: t.plot()                                                              # needs sage.plot
            Graphics object consisting of 11 graphics primitives
            sage: t.plot(descents=True)                                                 # needs sage.plot
            Graphics object consisting of 12 graphics primitives

            sage: t = Tableau([[2,2,4],[3]])
            sage: t.plot()                                                              # needs sage.plot
            Graphics object consisting of 11 graphics primitives
            sage: t.plot(descents=True)                                                 # needs sage.plot
            Traceback (most recent call last):
            ...
            ValueError: the tableau must be standard for \'descents=True\'
        '''
    def to_word_by_row(self):
        """
        Return the word obtained from a row reading of the tableau ``self``
        (starting with the lowermost row, reading every row from left
        to right).

        EXAMPLES::

            sage: Tableau([[1,2],[3,4]]).to_word_by_row()
            word: 3412
            sage: Tableau([[1, 4, 6], [2, 5], [3]]).to_word_by_row()
            word: 325146
        """
    def to_word_by_column(self):
        """
        Return the word obtained from a column reading of the tableau ``self``
        (starting with the leftmost column, reading every column from bottom
        to top).

        EXAMPLES::

            sage: Tableau([[1,2],[3,4]]).to_word_by_column()
            word: 3142
            sage: Tableau([[1, 4, 6], [2, 5], [3]]).to_word_by_column()
            word: 321546
        """
    def to_word(self):
        """
        An alias for :meth:`to_word_by_row`.

        EXAMPLES::

            sage: Tableau([[1,2],[3,4]]).to_word()
            word: 3412
            sage: Tableau([[1, 4, 6], [2, 5], [3]]).to_word()
            word: 325146
        """
    def descents(self):
        """
        Return a list of the cells ``(i,j)`` such that
        ``self[i][j] > self[i-1][j]``.

        .. WARNING::

            This is not to be confused with the descents of a standard tableau.

        EXAMPLES::

            sage: Tableau( [[1,4],[2,3]] ).descents()
            [(1, 0)]
            sage: Tableau( [[1,2],[3,4]] ).descents()
            [(1, 0), (1, 1)]
            sage: Tableau( [[1,2,3],[4,5]] ).descents()
            [(1, 0), (1, 1)]
        """
    def major_index(self):
        """
        Return the major index of ``self``.

        The major index of a tableau `T` is defined to be the sum of the number
        of descents of ``T`` (defined in :meth:`descents`) with the sum of
        their legs' lengths.

        .. WARNING::

            This is not to be confused with the major index of a
            standard tableau.

        EXAMPLES::

            sage: Tableau( [[1,4],[2,3]] ).major_index()
            1
            sage: Tableau( [[1,2],[3,4]] ).major_index()
            2

        If the major index would be defined in the sense of standard tableaux
        theory, then the following would give 3 for a result::

            sage: Tableau( [[1,2,3],[4,5]] ).major_index()
            2
        """
    def inversions(self):
        """
        Return a list of the inversions of ``self``.

        Let `T` be a tableau. An inversion is an attacking pair `(c,d)` of
        the shape of `T` (see
        :meth:`~sage.combinat.partition.Partition.attacking_pairs` for
        a definition of this) such that the entry of `c` in `T` is
        greater than the entry of `d`.

        .. WARNING::

            Do not mistake this for the inversions of a standard tableau.

        EXAMPLES::

            sage: t = Tableau([[1,2,3],[2,5]])
            sage: t.inversions()
            [((1, 1), (0, 0))]
            sage: t = Tableau([[1,4,3],[5,2],[2,6],[3]])
            sage: t.inversions()
            [((0, 1), (0, 2)), ((1, 0), (1, 1)), ((1, 1), (0, 0)), ((2, 1), (1, 0))]
        """
    def inversion_number(self):
        '''
        Return the inversion number of ``self``.

        The inversion number is defined to be the number of inversions of
        ``self`` minus the sum of the arm lengths of the descents of ``self``
        (see the :meth:`inversions` and :meth:`descents` methods for the
        relevant definitions).

        .. WARNING::

            This has none of the meanings in which the word "inversion"
            is used in the theory of standard tableaux.

        EXAMPLES::

            sage: t = Tableau([[1,2,3],[2,5]])
            sage: t.inversion_number()
            0
            sage: t = Tableau([[1,2,4],[3,5]])
            sage: t.inversion_number()
            0
        '''
    def to_sign_matrix(self, max_entry=None):
        """
        Return the sign matrix of ``self``.

        A sign matrix is an `m \\times n` matrix of 0s, 1s, and -1s such that the
        partial sums of each column is either 0 or 1 and the partial sums of
        each row is nonnegative. [Ava2007]_

        INPUT:

        - ``max_entry`` -- nonnegative integer; the maximum allowable number in
          the tableau (defaults to the largest entry in the tableau if not specified)

        EXAMPLES::

            sage: t = SemistandardTableau([[1,1,1,2,4],[3,3,4],[4,5],[6,6]])
            sage: t.to_sign_matrix(6)                                                   # needs sage.modules
            [ 0  0  0  1  0  0]
            [ 0  1  0 -1  0  0]
            [ 1 -1  0  1  0  0]
            [ 0  0  1 -1  1  1]
            [ 0  0  0  1 -1  0]
            sage: t = Tableau([[1,2,4],[3,5]])
            sage: t.to_sign_matrix(7)                                                   # needs sage.modules
            [ 0  0  0  1  0  0  0]
            [ 0  1  0 -1  1  0  0]
            [ 1 -1  1  0 -1  0  0]
            sage: t = Tableau([(4,5,4,3),(2,1,3)])
            sage: t.to_sign_matrix(5)                                                   # needs sage.modules
            [ 0  0  1  0  0]
            [ 0  0  0  1  0]
            [ 1  0 -1 -1  1]
            [-1  1  0  1 -1]
            sage: s = Tableau([(1,0,-2,4),(3,4,5)])
            sage: s.to_sign_matrix(6)
            Traceback (most recent call last):
            ...
            ValueError: the entries must be nonnegative integers
        """
    def schuetzenberger_involution(self, n=None, check: bool = True):
        """
        Return the Schuetzenberger involution of the tableau ``self``.

        This method relies on the analogous method on words, which reverts the
        word and then complements all letters within the underlying ordered
        alphabet. If `n` is specified, the underlying alphabet is assumed to
        be `[1, 2, \\ldots, n]`. If no alphabet is specified, `n` is the maximal
        letter appearing in ``self``.

        INPUT:

        - ``n`` -- integer specifying the maximal letter in the
          alphabet (optional)
        - ``check`` -- boolean (default: ``True``); check to make sure ``self``
          is semistandard

        OUTPUT: a tableau, the Schuetzenberger involution of ``self``

        EXAMPLES::

            sage: t = Tableau([[1,1,1],[2,2]])
            sage: t.schuetzenberger_involution(3)
            [[2, 2, 3], [3, 3]]

            sage: t = Tableau([[1,2,3],[4,5]])
            sage: t.schuetzenberger_involution()
            [[1, 2, 5], [3, 4]]

            sage: t = Tableau([[1,3,5,7],[2,4,6],[8,9]])
            sage: t.schuetzenberger_involution()
            [[1, 2, 6, 8], [3, 4, 9], [5, 7]]

            sage: t = Tableau([])
            sage: t.schuetzenberger_involution()
            []

            sage: t = StandardTableau([[1,2,3],[4,5]])
            sage: s = t.schuetzenberger_involution()
            sage: s.parent()
            Standard tableaux
        """
    def evacuation(self, n=None, check: bool = True):
        """
        Return the evacuation of the tableau ``self``.

        This is an alias for :meth:`schuetzenberger_involution`.

        This method relies on the analogous method on words, which reverts the
        word and then complements all letters within the underlying ordered
        alphabet. If `n` is specified, the underlying alphabet is assumed to
        be `[1, 2, \\ldots, n]`. If no alphabet is specified, `n` is the maximal
        letter appearing in ``self``.

        INPUT:

        - ``n`` -- integer specifying the maximal letter in the
          alphabet (optional)
        - ``check`` -- boolean (default: ``True``); check to make sure ``self``
          is semistandard

        OUTPUT: a tableau, the evacuation of ``self``

        EXAMPLES::

            sage: t = Tableau([[1,1,1],[2,2]])
            sage: t.evacuation(3)
            [[2, 2, 3], [3, 3]]

            sage: t = Tableau([[1,2,3],[4,5]])
            sage: t.evacuation()
            [[1, 2, 5], [3, 4]]

            sage: t = Tableau([[1,3,5,7],[2,4,6],[8,9]])
            sage: t.evacuation()
            [[1, 2, 6, 8], [3, 4, 9], [5, 7]]

            sage: t = Tableau([])
            sage: t.evacuation()
            []

            sage: t = StandardTableau([[1,2,3],[4,5]])
            sage: s = t.evacuation()
            sage: s.parent()
            Standard tableaux
        """
    def standardization(self, check: bool = True):
        """
        Return the standardization of ``self``, assuming ``self`` is a
        semistandard tableau.

        The standardization of a semistandard tableau `T` is the standard
        tableau `\\mathrm{st}(T)` of the same shape as `T` whose
        reversed reading word is the standardization of the reversed reading
        word of `T`.

        The standardization of a word `w` can be formed by replacing all `1`'s in
        `w` by `1, 2, \\ldots, k_1` from left to right, all `2`'s in `w` by
        `k_1 + 1, k_1 + 2, \\ldots, k_2`, and repeating for all letters which
        appear in `w`.
        See also :meth:`Word.standard_permutation()`.

        INPUT:

        - ``check`` -- (default: ``True``) check to make sure ``self`` is
          semistandard; set to ``False`` to avoid this check

        EXAMPLES::

            sage: t = Tableau([[1,3,3,4],[2,4,4],[5,16]])
            sage: t.standardization()
            [[1, 3, 4, 7], [2, 5, 6], [8, 9]]

        Standard tableaux are fixed under standardization::

            sage: all((t == t.standardization() for t in StandardTableaux(6)))
            True
            sage: t = Tableau([])
            sage: t.standardization()
            []

        The reading word of the standardization is the standardization of
        the reading word::

            sage: T = SemistandardTableaux(shape=[5,2,2,1], max_entry=4)
            sage: all(t.to_word().standard_permutation() == t.standardization().reading_word_permutation() for t in T) # long time
            True
        """
    def bender_knuth_involution(self, k, rows=None, check: bool = True):
        """
        Return the image of ``self`` under the `k`-th Bender--Knuth
        involution, assuming ``self`` is a semistandard tableau.

        Let `T` be a tableau, then a *lower free `k` in `T`* means a cell of
        `T` which is filled with the integer `k` and whose direct lower
        neighbor is not filled with the integer `k + 1` (in particular,
        this lower neighbor might not exist at all). Let an *upper free `k + 1`
        in `T`* mean a cell of `T` which is filled with the integer `k + 1`
        and whose direct upper neighbor is not filled with the integer `k`
        (in particular, this neighbor might not exist at all). It is clear
        that for any row `r` of `T`, the lower free `k`'s and the upper
        free `k + 1`'s in `r` together form a contiguous interval or `r`.

        The *`k`-th Bender--Knuth switch at row `i`* changes the entries of
        the cells in this interval in such a way that if it used to have
        `a` entries of `k` and `b` entries of `k + 1`, it will now
        have `b` entries of `k` and `a` entries of `k + 1`. For fixed `k`, the
        `k`-th Bender--Knuth switches for different `i` commute. The
        composition of the `k`-th Bender--Knuth switches for all rows is
        called the *`k`-th Bender-Knuth involution*. This is used to show that
        the Schur functions defined by semistandard tableaux are symmetric
        functions.

        INPUT:

        - ``k`` -- integer

        - ``rows`` -- (default: ``None``) when set to ``None``, the method
          computes the `k`-th Bender--Knuth involution as defined above.
          When an iterable, this computes the composition of the `k`-th
          Bender--Knuth switches at row `i` over all `i` in ``rows``. When set
          to an integer `i`, the method computes the `k`-th Bender--Knuth
          switch at row `i`. Note the indexing of the rows starts with `1`.

        - ``check`` -- (default: ``True``) check to make sure ``self`` is
          semistandard; Set to ``False`` to avoid this check

        OUTPUT:

        The image of ``self`` under either the `k`-th Bender--Knuth
        involution, the `k`-th Bender--Knuth switch at a certain row, or
        the composition of such switches, as detailed in the INPUT section.

        EXAMPLES::

            sage: t = Tableau([[1,1,3,4,4,5,6,7],[2,2,4,6,7,7,7],[3,4,5,8,8,9],[6,6,7,10],[7,8,8,11],[8]])
            sage: t.bender_knuth_involution(1) == t
            True
            sage: t.bender_knuth_involution(2)
            [[1, 1, 2, 4, 4, 5, 6, 7], [2, 3, 4, 6, 7, 7, 7], [3, 4, 5, 8, 8, 9], [6, 6, 7, 10], [7, 8, 8, 11], [8]]
            sage: t.bender_knuth_involution(3)
            [[1, 1, 3, 3, 3, 5, 6, 7], [2, 2, 4, 6, 7, 7, 7], [3, 4, 5, 8, 8, 9], [6, 6, 7, 10], [7, 8, 8, 11], [8]]
            sage: t.bender_knuth_involution(4)
            [[1, 1, 3, 4, 5, 5, 6, 7], [2, 2, 4, 6, 7, 7, 7], [3, 5, 5, 8, 8, 9], [6, 6, 7, 10], [7, 8, 8, 11], [8]]
            sage: t.bender_knuth_involution(5)
            [[1, 1, 3, 4, 4, 5, 6, 7], [2, 2, 4, 5, 7, 7, 7], [3, 4, 6, 8, 8, 9], [5, 5, 7, 10], [7, 8, 8, 11], [8]]
            sage: t.bender_knuth_involution(666) == t
            True
            sage: t.bender_knuth_involution(4, 2) == t
            True
            sage: t.bender_knuth_involution(4, 3)
            [[1, 1, 3, 4, 4, 5, 6, 7], [2, 2, 4, 6, 7, 7, 7], [3, 5, 5, 8, 8, 9], [6, 6, 7, 10], [7, 8, 8, 11], [8]]

        The ``rows`` keyword can be an iterator::

            sage: t.bender_knuth_involution(6, iter([1,2])) == t
            False
            sage: t.bender_knuth_involution(6, iter([3,4])) == t
            True

        The Bender--Knuth involution is an involution::

            sage: T = SemistandardTableaux(shape=[3,1,1], max_entry=4)
            sage: all(t.bender_knuth_involution(k).bender_knuth_involution(k) == t      # needs sage.modules
            ....:     for k in range(1, 5) for t in T)
            True

        The same holds for the single switches::

            sage: all(t.bender_knuth_involution(k, j).bender_knuth_involution(k, j) == t            # needs sage.modules
            ....:     for k in range(1, 5) for j in range(1, 5) for t in T)
            True

        Locality of the Bender--Knuth involutions::

            sage: all(t.bender_knuth_involution(k).bender_knuth_involution(l)           # needs sage.modules
            ....:       == t.bender_knuth_involution(l).bender_knuth_involution(k)
            ....:     for k in range(1, 5) for l in range(1, 5) if abs(k - l) > 1
            ....:     for t in T)
            True

        Berenstein and Kirillov [KB1995]_ have shown that
        `(s_1 s_2)^6 = id` (for tableaux of straight shape)::

            sage: p = lambda t, k: t.bender_knuth_involution(k).bender_knuth_involution(k + 1)
            sage: all(p(p(p(p(p(p(t,1),1),1),1),1),1) == t for t in T)                  # needs sage.modules
            True

        However, `(s_2 s_3)^6 = id` is false::

            sage: p = lambda t, k: t.bender_knuth_involution(k).bender_knuth_involution(k + 1)
            sage: t = Tableau([[1,2,2],[3,4]])
            sage: x = t
            sage: for i in range(6): x = p(x, 2)
            sage: x
            [[1, 2, 3], [2, 4]]
            sage: x == t
            False

        TESTS::

            sage: t = Tableau([])
            sage: t.bender_knuth_involution(3)
            []
        """
    def reading_word_permutation(self):
        """
        Return the permutation obtained by reading the entries of the
        standardization of ``self`` row by row, starting with the
        bottommost row (in English notation).

        EXAMPLES::

            sage: StandardTableau([[1,2],[3,4]]).reading_word_permutation()
            [3, 4, 1, 2]

        Check that :issue:`14724` is fixed::

            sage: SemistandardTableau([[1,1]]).reading_word_permutation()
            [1, 2]
        """
    def entries(self):
        """
        Return the tuple of all entries of ``self``, in the order obtained
        by reading across the rows from top to bottom (in English
        notation).

        EXAMPLES::

            sage: t = Tableau([[1,3], [2]])
            sage: t.entries()
            (1, 3, 2)
        """
    def entry(self, cell):
        """
        Return the entry of cell ``cell`` in the tableau ``self``. Here,
        ``cell`` should be given as a tuple `(i,j)` of zero-based
        coordinates (so the northwesternmost cell in English notation
        is `(0,0)`).

        EXAMPLES::

            sage: t = Tableau([[1,2],[3,4]])
            sage: t.entry( (0,0) )
            1
            sage: t.entry( (1,1) )
            4
        """
    def weight(self):
        """
        Return the weight of the tableau ``self``. Trailing zeroes are
        omitted when returning the weight.

        The weight of a tableau `T` is the sequence `(a_1, a_2, a_3, \\ldots )`,
        where `a_k` is the number of entries of `T` equal to `k`. This
        sequence contains only finitely many nonzero entries.

        The weight of a tableau `T` is the same as the weight of the
        reading word of `T`, for any reading order.

        EXAMPLES::

            sage: Tableau([[1,2],[3,4]]).weight()
            [1, 1, 1, 1]

            sage: Tableau([]).weight()
            []

            sage: Tableau([[1,3,3,7],[4,2],[2,3]]).weight()
            [1, 2, 3, 1, 0, 0, 1]

        TESTS:

        We check that this agrees with going to the word::

            sage: t = Tableau([[1,3,4,7],[6,2],[2,3]])
            sage: def by_word(T):
            ....:     ed = T.to_word().evaluation_dict()
            ....:     m = max(ed) + 1
            ....:     return [ed.get(k, 0) for k in range(1, m)]
            sage: by_word(t) == t.weight()
            True
            sage: SST = SemistandardTableaux(shape=[3,1,1])
            sage: all(by_word(t) == t.weight() for t in SST)                            # needs sage.modules
            True
        """
    evaluation = weight
    def is_row_strict(self) -> bool:
        """
        Return ``True`` if ``self`` is a row strict tableau and ``False``
        otherwise.

        A tableau is row strict if the entries in each row are in
        (strictly) increasing order.

        EXAMPLES::

            sage: Tableau([[1, 3], [2, 4]]).is_row_strict()
            True
            sage: Tableau([[1, 2], [2, 4]]).is_row_strict()
            True
            sage: Tableau([[2, 3], [2, 4]]).is_row_strict()
            True
            sage: Tableau([[5, 3], [2, 4]]).is_row_strict()
            False
        """
    def is_row_increasing(self, weak: bool = False) -> bool:
        """
        Return ``True`` if the entries in each row are in increasing order,
        and ``False`` otherwise.

        By default, this checks for strictly increasing rows. Set ``weak``
        to ``True`` to test for weakly increasing rows.

        EXAMPLES::

            sage: T = Tableau([[1, 1, 3], [1, 2]])
            sage: T.is_row_increasing(weak=True)
            True
            sage: T.is_row_increasing()
            False
            sage: Tableau([[2, 1]]).is_row_increasing(weak=True)
            False
        """
    def is_column_increasing(self, weak: bool = False) -> bool:
        """
        Return ``True`` if the entries in each column are in increasing order,
        and ``False`` otherwise.

        By default, this checks for strictly increasing columns. Set ``weak``
        to ``True`` to test for weakly increasing columns.

        EXAMPLES::

            sage: T = Tableau([[1, 1, 3], [1, 2]])
            sage: T.is_column_increasing(weak=True)
            True
            sage: T.is_column_increasing()
            False
            sage: Tableau([[2], [1]]).is_column_increasing(weak=True)
            False
        """
    def is_column_strict(self) -> bool:
        """
        Return ``True`` if ``self`` is a column strict tableau and ``False``
        otherwise.

        A tableau is column strict if the entries in each column are in
        (strictly) increasing order.

        EXAMPLES::

            sage: Tableau([[1, 3], [2, 4]]).is_column_strict()
            True
            sage: Tableau([[1, 2], [2, 4]]).is_column_strict()
            True
            sage: Tableau([[2, 3], [2, 4]]).is_column_strict()
            False
            sage: Tableau([[5, 3], [2, 4]]).is_column_strict()
            False
            sage: Tableau([]).is_column_strict()
            True
            sage: Tableau([[1, 4, 2]]).is_column_strict()
            True
            sage: Tableau([[1, 4, 2], [2, 5]]).is_column_strict()
            True
            sage: Tableau([[1, 4, 2], [2, 3]]).is_column_strict()
            False
        """
    def is_semistandard(self) -> bool:
        """
        Return ``True`` if ``self`` is a semistandard tableau, and ``False``
        otherwise.

        A tableau is semistandard if its rows weakly increase and its columns
        strictly increase.

        EXAMPLES::

            sage: Tableau([[1,1],[1,2]]).is_semistandard()
            False
            sage: Tableau([[1,2],[1,2]]).is_semistandard()
            False
            sage: Tableau([[1,1],[2,2]]).is_semistandard()
            True
            sage: Tableau([[1,2],[2,3]]).is_semistandard()
            True
            sage: Tableau([[4,1],[3,2]]).is_semistandard()
            False
        """
    def is_standard(self) -> bool:
        """
        Return ``True`` if ``self`` is a standard tableau and ``False``
        otherwise.

        EXAMPLES::

            sage: Tableau([[1, 3], [2, 4]]).is_standard()
            True
            sage: Tableau([[1, 2], [2, 4]]).is_standard()
            False
            sage: Tableau([[2, 3], [2, 4]]).is_standard()
            False
            sage: Tableau([[5, 3], [2, 4]]).is_standard()
            False
        """
    def is_increasing(self) -> bool:
        """
        Return ``True`` if ``self`` is an increasing tableau and
        ``False`` otherwise.

        A tableau is increasing if it is both row strict and column strict.

        EXAMPLES::

            sage: Tableau([[1, 3], [2, 4]]).is_increasing()
            True
            sage: Tableau([[1, 2], [2, 4]]).is_increasing()
            True
            sage: Tableau([[2, 3], [2, 4]]).is_increasing()
            False
            sage: Tableau([[5, 3], [2, 4]]).is_increasing()
            False
            sage: Tableau([[1, 2, 3], [2, 3], [3]]).is_increasing()
            True
        """
    def is_rectangular(self) -> bool:
        """
        Return ``True`` if the tableau ``self`` is rectangular and
        ``False`` otherwise.

        EXAMPLES::

            sage: Tableau([[1,2],[3,4]]).is_rectangular()
            True
            sage: Tableau([[1,2,3],[4,5],[6]]).is_rectangular()
            False
            sage: Tableau([]).is_rectangular()
            True
        """
    def vertical_flip(self):
        """
        Return the tableau obtained by vertically flipping the tableau
        ``self``.

        This only works for rectangular tableaux.

        EXAMPLES::

            sage: Tableau([[1,2],[3,4]]).vertical_flip()
            [[3, 4], [1, 2]]
        """
    def rotate_180(self):
        """
        Return the tableau obtained by rotating ``self`` by `180` degrees.

        This only works for rectangular tableaux.

        EXAMPLES::

            sage: Tableau([[1,2],[3,4]]).rotate_180()
            [[4, 3], [2, 1]]
        """
    def cells(self):
        """
        Return a list of the coordinates of the cells of ``self``.

        Coordinates start at `0`, so the northwesternmost cell (in
        English notation) has coordinates `(0, 0)`.

        EXAMPLES::

            sage: Tableau([[1,2],[3,4]]).cells()
            [(0, 0), (0, 1), (1, 0), (1, 1)]
        """
    def cells_containing(self, i):
        """
        Return the list of cells in which the letter `i` appears in the
        tableau ``self``. The list is ordered with cells appearing from
        left to right.

        Cells are given as pairs of coordinates `(a, b)`, where both
        rows and columns are counted from `0` (so `a = 0` means the cell
        lies in the leftmost column of the tableau, etc.).

        EXAMPLES::

            sage: t = Tableau([[1,1,3],[2,3,5],[4,5]])
            sage: t.cells_containing(5)
            [(2, 1), (1, 2)]
            sage: t.cells_containing(4)
            [(2, 0)]
            sage: t.cells_containing(6)
            []

            sage: t = Tableau([[1,1,2,4],[2,4,4],[4]])
            sage: t.cells_containing(4)
            [(2, 0), (1, 1), (1, 2), (0, 3)]

            sage: t = Tableau([[1,1,2,8,9],[2,5,6,11],[3,7,7,13],[4,8,9],[5],[13],[14]])
            sage: t.cells_containing(8)
            [(3, 1), (0, 3)]

            sage: Tableau([]).cells_containing(3)
            []
        """
    def leq(self, secondtab):
        """
        Check whether each entry of ``self`` is less-or-equal to the
        corresponding entry of a further tableau ``secondtab``.

        INPUT:

        - ``secondtab`` -- a tableau of the same shape as ``self``

        EXAMPLES::

            sage: T = Tableau([[1, 2], [3]])
            sage: S = Tableau([[1, 3], [3]])
            sage: G = Tableau([[2, 1], [4]])
            sage: H = Tableau([[1, 2], [4]])
            sage: T.leq(S)
            True
            sage: T.leq(T)
            True
            sage: T.leq(G)
            False
            sage: T.leq(H)
            True
            sage: S.leq(T)
            False
            sage: S.leq(G)
            False
            sage: S.leq(H)
            False
            sage: G.leq(H)
            False
            sage: H.leq(G)
            False

        TESTS::

            sage: StandardTableau(T).leq(S)
            True
            sage: T.leq(SemistandardTableau(S))
            True
        """
    def k_weight(self, k):
        """
        Return the `k`-weight of ``self``.

        A tableau has `k`-weight `\\alpha = (\\alpha_1, ..., \\alpha_n)`
        if there are exactly `\\alpha_i` distinct residues for the
        cells occupied by the letter `i` for each `i`.  The residue
        of a cell in position `(a,b)` is `a-b` modulo `k+1`.

        This definition is the one used in [Ive2012]_ (p. 12).

        EXAMPLES::

            sage: Tableau([[1,2],[2,3]]).k_weight(1)
            [1, 1, 1]
            sage: Tableau([[1,2],[2,3]]).k_weight(2)
            [1, 2, 1]
            sage: t = Tableau([[1,1,1,2,5],[2,3,6],[3],[4]])
            sage: t.k_weight(1)
            [2, 1, 1, 1, 1, 1]
            sage: t.k_weight(2)
            [3, 2, 2, 1, 1, 1]
            sage: t.k_weight(3)
            [3, 1, 2, 1, 1, 1]
            sage: t.k_weight(4)
            [3, 2, 2, 1, 1, 1]
            sage: t.k_weight(5)
            [3, 2, 2, 1, 1, 1]
        """
    def is_k_tableau(self, k) -> bool:
        """
        Check whether ``self`` is a valid weak `k`-tableau.

        EXAMPLES::

            sage: t = Tableau([[1,2,3],[2,3],[3]])
            sage: t.is_k_tableau(3)
            True
            sage: t = Tableau([[1,1,3],[2,2],[3]])
            sage: t.is_k_tableau(3)
            False
        """
    def restrict(self, n):
        """
        Return the restriction of the semistandard tableau ``self``
        to ``n``. If possible, the restricted tableau will have the same
        parent as this tableau.

        If `T` is a semistandard tableau and `n` is a nonnegative integer,
        then the restriction of `T` to `n` is defined as the
        (semistandard) tableau obtained by removing all cells filled with
        entries greater than `n` from `T`.

        .. NOTE::

            If only the shape of the restriction, rather than the whole
            restriction, is needed, then the faster method
            :meth:`restriction_shape` is preferred.

        EXAMPLES::

            sage: Tableau([[1,2],[3],[4]]).restrict(3)
            [[1, 2], [3]]
            sage: StandardTableau([[1,2],[3],[4]]).restrict(2)
            [[1, 2]]
            sage: Tableau([[1,2,3],[2,4,4],[3]]).restrict(0)
            []
            sage: Tableau([[1,2,3],[2,4,4],[3]]).restrict(2)
            [[1, 2], [2]]
            sage: Tableau([[1,2,3],[2,4,4],[3]]).restrict(3)
            [[1, 2, 3], [2], [3]]
            sage: Tableau([[1,2,3],[2,4,4],[3]]).restrict(5)
            [[1, 2, 3], [2, 4, 4], [3]]

        If possible the restricted tableau will belong to the same category as
        the original tableau::

            sage: S = StandardTableau([[1,2,4,7],[3,5],[6]]); S.category()
            Category of elements of Standard tableaux
            sage: S.restrict(4).category()
            Category of elements of Standard tableaux
            sage: SS=StandardTableaux([4,2,1])([[1,2,4,7],[3,5],[6]]); SS.category()
            Category of elements of Standard tableaux of shape [4, 2, 1]
            sage: SS.restrict(4).category()
            Category of elements of Standard tableaux

            sage: Tableau([[1,2],[3],[4]]).restrict(3)
            [[1, 2], [3]]
            sage: Tableau([[1,2],[3],[4]]).restrict(2)
            [[1, 2]]
            sage: SemistandardTableau([[1,1],[2]]).restrict(1)
            [[1, 1]]
            sage: _.category()
            Category of elements of Semistandard tableaux
        """
    def restriction_shape(self, n):
        """
        Return the shape of the restriction of the semistandard tableau
        ``self`` to ``n``.

        If `T` is a semistandard tableau and `n` is a nonnegative integer,
        then the restriction of `T` to `n` is defined as the
        (semistandard) tableau obtained by removing all cells filled with
        entries greater than `n` from `T`.

        This method computes merely the shape of the restriction. For
        the restriction itself, use :meth:`restrict`.

        EXAMPLES::

            sage: Tableau([[1,2],[2,3],[3,4]]).restriction_shape(3)
            [2, 2, 1]
            sage: StandardTableau([[1,2],[3],[4],[5]]).restriction_shape(2)
            [2]
            sage: Tableau([[1,3,3,5],[2,4,4],[17]]).restriction_shape(0)
            []
            sage: Tableau([[1,3,3,5],[2,4,4],[17]]).restriction_shape(2)
            [1, 1]
            sage: Tableau([[1,3,3,5],[2,4,4],[17]]).restriction_shape(3)
            [3, 1]
            sage: Tableau([[1,3,3,5],[2,4,4],[17]]).restriction_shape(5)
            [4, 3]

            sage: all( T.restriction_shape(i) == T.restrict(i).shape()
            ....:      for T in StandardTableaux(5) for i in range(1, 5) )
            True
        """
    def to_chain(self, max_entry=None):
        """
        Return the chain of partitions corresponding to the (semi)standard
        tableau ``self``.

        The optional keyword parameter ``max_entry`` can be used to
        customize the length of the chain. Specifically, if this parameter
        is set to a nonnegative integer ``n``, then the chain is
        constructed from the positions of the letters `1, 2, \\ldots, n`
        in the tableau.

        EXAMPLES::

            sage: Tableau([[1,2],[3],[4]]).to_chain()
            [[], [1], [2], [2, 1], [2, 1, 1]]
            sage: Tableau([[1,1],[2]]).to_chain()
            [[], [2], [2, 1]]
            sage: Tableau([[1,1],[3]]).to_chain()
            [[], [2], [2], [2, 1]]
            sage: Tableau([]).to_chain()
            [[]]
            sage: Tableau([[1,1],[2],[3]]).to_chain(max_entry=2)
            [[], [2], [2, 1]]
            sage: Tableau([[1,1],[2],[3]]).to_chain(max_entry=3)
            [[], [2], [2, 1], [2, 1, 1]]
            sage: Tableau([[1,1],[2],[3]]).to_chain(max_entry=4)
            [[], [2], [2, 1], [2, 1, 1], [2, 1, 1]]
            sage: Tableau([[1,1,2],[2,3],[4,5]]).to_chain(max_entry=6)
            [[], [2], [3, 1], [3, 2], [3, 2, 1], [3, 2, 2], [3, 2, 2]]
        """
    def to_Gelfand_Tsetlin_pattern(self):
        """
        Return the :class:`Gelfand-Tsetlin pattern <GelfandTsetlinPattern>`
        corresponding to ``self`` when semistandard.

        EXAMPLES::

            sage: T = Tableau([[1,2,3],[2,3],[3]])
            sage: G = T.to_Gelfand_Tsetlin_pattern(); G
            [[3, 2, 1], [2, 1], [1]]
            sage: G.to_tableau() == T
            True
            sage: T = Tableau([[1,3],[2]])
            sage: T.to_Gelfand_Tsetlin_pattern()
            [[2, 1, 0], [1, 1], [1]]
        """
    def anti_restrict(self, n):
        """
        Return the skew tableau formed by removing all of the cells from
        ``self`` that are filled with a number at most `n`.

        EXAMPLES::

            sage: t = Tableau([[1,2,3],[4,5]]); t
            [[1, 2, 3], [4, 5]]
            sage: t.anti_restrict(1)
            [[None, 2, 3], [4, 5]]
            sage: t.anti_restrict(2)
            [[None, None, 3], [4, 5]]
            sage: t.anti_restrict(3)
            [[None, None, None], [4, 5]]
            sage: t.anti_restrict(4)
            [[None, None, None], [None, 5]]
            sage: t.anti_restrict(5)
            [[None, None, None], [None, None]]
        """
    def to_list(self):
        """
        Return ``self`` as a list of lists (not tuples!).

        EXAMPLES::

            sage: t = Tableau([[1,2],[3,4]])
            sage: l = t.to_list(); l
            [[1, 2], [3, 4]]
            sage: l[0][0] = 2
            sage: t
            [[1, 2], [3, 4]]
        """
    def bump(self, x):
        """
        Insert ``x`` into ``self`` using Schensted's row-bumping (or
        row-insertion) algorithm.

        EXAMPLES::

            sage: t = Tableau([[1,2],[3]])
            sage: t.bump(1)
            [[1, 1], [2], [3]]
            sage: t
            [[1, 2], [3]]
            sage: t.bump(2)
            [[1, 2, 2], [3]]
            sage: t.bump(3)
            [[1, 2, 3], [3]]
            sage: t
            [[1, 2], [3]]
            sage: t = Tableau([[1,2,2,3],[2,3,5,5],[4,4,6],[5,6]])
            sage: t.bump(2)
            [[1, 2, 2, 2], [2, 3, 3, 5], [4, 4, 5], [5, 6, 6]]
            sage: t.bump(1)
            [[1, 1, 2, 3], [2, 2, 5, 5], [3, 4, 6], [4, 6], [5]]
        """
    def schensted_insert(self, i, left: bool = False):
        """
        Insert ``i`` into ``self`` using Schensted's row-bumping (or
        row-insertion) algorithm.

        INPUT:

        - ``i`` -- a number to insert
        - ``left`` -- boolean (default: ``False``); if set to
          ``True``, the insertion will be done from the left. That
          is, if one thinks of the algorithm as appending a letter
          to the reading word of ``self``, we append the letter to
          the left instead of the right

        EXAMPLES::

            sage: t = Tableau([[3,5],[7]])
            sage: t.schensted_insert(8)
            [[3, 5, 8], [7]]
            sage: t.schensted_insert(8, left=True)
            [[3, 5], [7], [8]]
        """
    def insert_word(self, w, left: bool = False):
        """
        Insert the word ``w`` into the tableau ``self`` letter by letter
        using Schensted insertion. By default, the word ``w`` is being
        processed from left to right, and the insertion used is row
        insertion. If the optional keyword ``left`` is set to ``True``,
        the word ``w`` is being processed from right to left, and column
        insertion is used instead.

        EXAMPLES::

            sage: t0 = Tableau([])
            sage: w = [1,1,2,3,3,3,3]
            sage: t0.insert_word(w)
            [[1, 1, 2, 3, 3, 3, 3]]
            sage: t0.insert_word(w,left=True)
            [[1, 1, 2, 3, 3, 3, 3]]
            sage: w.reverse()
            sage: t0.insert_word(w)
            [[1, 1, 3, 3], [2, 3], [3]]
            sage: t0.insert_word(w,left=True)
            [[1, 1, 3, 3], [2, 3], [3]]
            sage: t1 = Tableau([[1,3],[2]])
            sage: t1.insert_word([4,5])
            [[1, 3, 4, 5], [2]]
            sage: t1.insert_word([4,5], left=True)
            [[1, 3], [2, 5], [4]]
        """
    def reverse_bump(self, loc):
        """
        Reverse row bump the entry of ``self`` at the specified
        location ``loc`` (given as a row index or a
        corner ``(r, c)`` of the tableau).

        This is the reverse of Schensted's row-insertion algorithm.
        See Section 1.1, page 8, of Fulton's [Ful1997]_.

        INPUT:

        - ``loc`` -- can be either of the following:

          - The coordinates ``(r, c)`` of the square to reverse-bump
            (which must be a corner of the tableau);
          - The row index ``r`` of this square.

          Note that both ``r`` and ``c`` are `0`-based, i.e., the
          topmost row and the leftmost column are the `0`-th row
          and the `0`-th column.

        OUTPUT: an ordered pair consisting of:

        1. The resulting (smaller) tableau;
        2. The entry bumped out at the end of the process.

        .. SEEALSO::

            :meth:`bump`

        EXAMPLES:

        This is the reverse of Schensted's bump::

            sage: T = Tableau([[1, 1, 2, 2, 4], [2, 3, 3], [3, 4], [4]])
            sage: T.reverse_bump(2)
            ([[1, 1, 2, 3, 4], [2, 3, 4], [3], [4]], 2)
            sage: T == T.reverse_bump(2)[0].bump(2)
            True
            sage: T.reverse_bump((3, 0))
            ([[1, 2, 2, 2, 4], [3, 3, 3], [4, 4]], 1)

        Some errors caused by wrong input::

            sage: T.reverse_bump((3, 1))
            Traceback (most recent call last):
            ...
            ValueError: invalid corner
            sage: T.reverse_bump(4)
            Traceback (most recent call last):
            ...
            IndexError: list index out of range
            sage: Tableau([[2, 2, 1], [3, 3]]).reverse_bump(0)
            Traceback (most recent call last):
            ...
            ValueError: reverse bumping is only defined for semistandard tableaux

        Some edge cases::

            sage: Tableau([[1]]).reverse_bump(0)
            ([], 1)
            sage: Tableau([[1,1]]).reverse_bump(0)
            ([[1]], 1)
            sage: Tableau([]).reverse_bump(0)
            Traceback (most recent call last):
            ...
            IndexError: list index out of range

        .. NOTE::

            Reverse row bumping is only implemented for tableaux with weakly increasing
            and strictly increasing columns (though the tableau does not need to be an
            instance of class :class:`SemistandardTableau`).
        """
    def bump_multiply(self, other):
        """
        Multiply two tableaux using Schensted's bump.

        This product makes the set of semistandard tableaux into an
        associative monoid. The empty tableau is the unit in this monoid.
        See pp. 11-12 of [Ful1997]_.

        The same product operation is implemented in a different way in
        :meth:`slide_multiply`.

        EXAMPLES::

            sage: t = Tableau([[1,2,2,3],[2,3,5,5],[4,4,6],[5,6]])
            sage: t2 = Tableau([[1,2],[3]])
            sage: t.bump_multiply(t2)
            [[1, 1, 2, 2, 3], [2, 2, 3, 5], [3, 4, 5], [4, 6, 6], [5]]
        """
    def slide_multiply(self, other):
        """
        Multiply two tableaux using jeu de taquin.

        This product makes the set of semistandard tableaux into an
        associative monoid. The empty tableau is the unit in this monoid.

        See pp. 15 of [Ful1997]_.

        The same product operation is implemented in a different way in
        :meth:`bump_multiply`.

        EXAMPLES::

            sage: t = Tableau([[1,2,2,3],[2,3,5,5],[4,4,6],[5,6]])
            sage: t2 = Tableau([[1,2],[3]])
            sage: t.slide_multiply(t2)
            [[1, 1, 2, 2, 3], [2, 2, 3, 5], [3, 4, 5], [4, 6, 6], [5]]
        """
    def promotion_inverse(self, n):
        '''
        Return the image of ``self`` under the inverse promotion operator.

        .. WARNING::

            You might know this operator as the promotion operator
            (without "inverse") -- literature does not agree on the
            name.

        The inverse promotion operator, applied to a tableau `t`, does the
        following:

        Iterate over all letters `1` in the tableau `t`, from right to left.
        For each of these letters, do the following:

        - Remove the letter from `t`, thus leaving a hole where it used to be.

        - Apply jeu de taquin to move this hole northeast (in French notation)
          until it reaches the outer boundary of `t`.

        - Fill `n+2` into the hole once jeu de taquin has completed.

        Once this all is done, subtract `1` from each letter in the tableau.
        This is not always well-defined. Restricted to the class of
        semistandard tableaux whose entries are all `\\leq n + 1`, this is the
        usual inverse promotion operator defined on this class.

        When ``self`` is a standard tableau of size ``n + 1``, this definition of
        inverse promotion is the map called "promotion" in [Sag2011]_ (p. 23) and
        in [Stan2009]_, and is the inverse of the map called "promotion" in
        [Hai1992]_ (p. 90).

        .. WARNING::

            To my (Darij\'s) knowledge, the fact that the above "inverse
            promotion operator" really is the inverse of the promotion
            operator :meth:`promotion` for semistandard tableaux has never
            been proven in literature. Corrections are welcome.

        EXAMPLES::

            sage: t = Tableau([[1,2],[3,3]])
            sage: t.promotion_inverse(2)
            [[1, 2], [2, 3]]

            sage: t = Tableau([[1,2],[2,3]])
            sage: t.promotion_inverse(2)
            [[1, 1], [2, 3]]

            sage: t = Tableau([[1,2,5],[3,3,6],[4,7]])
            sage: t.promotion_inverse(8)
            [[1, 2, 4], [2, 5, 9], [3, 6]]

            sage: t = Tableau([])
            sage: t.promotion_inverse(2)
            []

        TESTS:

        We check the equivalence of two definitions of inverse promotion
        on semistandard tableaux::

            sage: ST = SemistandardTableaux(shape=[4,2,1], max_entry=7)
            sage: def bk_promotion_inverse7(st):
            ....:     st2 = st
            ....:     for i in range(1, 7):
            ....:         st2 = st2.bender_knuth_involution(i, check=False)
            ....:     return st2
            sage: all( bk_promotion_inverse7(st) == st.promotion_inverse(6) for st in ST ) # long time
            True
            sage: ST = SemistandardTableaux(shape=[2,2,2], max_entry=7)
            sage: all( bk_promotion_inverse7(st) == st.promotion_inverse(6) for st in ST ) # long time
            True

        A test for :issue:`13203`::

            sage: T = Tableau([[1]])
            sage: type(T.promotion_inverse(2)[0][0])
            <class \'sage.rings.integer.Integer\'>
        '''
    def promotion(self, n):
        '''
        Return the image of ``self`` under the promotion operator.

        .. WARNING::

            You might know this operator as the inverse promotion
            operator -- literature does not agree on the name. You
            might also be looking for the Lapointe-Lascoux-Morse
            promotion operator (:meth:`promotion_operator`).

        The promotion operator, applied to a tableau `t`, does the following:

        Iterate over all letters `n+1` in the tableau `t`, from left to right.
        For each of these letters, do the following:

        - Remove the letter from `t`, thus leaving a hole where it used to be.

        - Apply jeu de taquin to move this hole southwest (in French notation)
          until it reaches the inner boundary of `t`.

        - Fill `0` into the hole once jeu de taquin has completed.

        Once this all is done, add `1` to each letter in the tableau.
        This is not always well-defined. Restricted to the class of
        semistandard tableaux whose entries are all `\\leq n + 1`, this is the
        usual promotion operator defined on this class.

        When ``self`` is a standard tableau of size ``n + 1``, this definition of
        promotion is precisely the one given in [Hai1992]_ (p. 90). It is the
        inverse of the maps called "promotion" in [Sag2011]_ (p. 23) and in [Stan2009]_.

        .. WARNING::

            To my (Darij\'s) knowledge, the fact that the above promotion
            operator really is the inverse of the "inverse promotion
            operator" :meth:`promotion_inverse` for semistandard tableaux
            has never been proven in literature. Corrections are welcome.

        REFERENCES:

        - [Hai1992]_

        - [Sag2011]_

        EXAMPLES::

            sage: t = Tableau([[1,2],[3,3]])
            sage: t.promotion(2)
            [[1, 1], [2, 3]]

            sage: t = Tableau([[1,1,1],[2,2,3],[3,4,4]])
            sage: t.promotion(3)
            [[1, 1, 2], [2, 2, 3], [3, 4, 4]]

            sage: t = Tableau([[1,2],[2]])
            sage: t.promotion(3)
            [[2, 3], [3]]

            sage: t = Tableau([[1,1,3],[2,2]])
            sage: t.promotion(2)
            [[1, 2, 2], [3, 3]]

            sage: t = Tableau([[1,1,3],[2,3]])
            sage: t.promotion(2)
            [[1, 1, 2], [2, 3]]

            sage: t = Tableau([])
            sage: t.promotion(2)
            []

        TESTS:

        We check the equivalence of two definitions of promotion on
        semistandard tableaux::

            sage: ST = SemistandardTableaux(shape=[3,2,2,1], max_entry=6)
            sage: def bk_promotion6(st):
            ....:     st2 = st
            ....:     for i in range(5, 0, -1):
            ....:         st2 = st2.bender_knuth_involution(i, check=False)
            ....:     return st2
            sage: all( bk_promotion6(st) == st.promotion(5) for st in ST ) # long time
            True
            sage: ST = SemistandardTableaux(shape=[4,4], max_entry=6)
            sage: all( bk_promotion6(st) == st.promotion(5) for st in ST ) # long time
            True

        We also check :meth:`promotion_inverse()` is the inverse
        of :meth:`promotion()`::

            sage: ST = SemistandardTableaux(shape=[3,2,1], max_entry=7)
            sage: all( st.promotion(6).promotion_inverse(6) == st for st in ST ) # long time
            True
        '''
    def row_stabilizer(self):
        """
        Return the PermutationGroup corresponding to the row stabilizer of
        ``self``.

        This assumes that every integer from `1` to the size of ``self``
        appears exactly once in ``self``.

        EXAMPLES::

            sage: # needs sage.groups
            sage: rs = Tableau([[1,2,3],[4,5]]).row_stabilizer()
            sage: rs.order() == factorial(3)*factorial(2)
            True
            sage: PermutationGroupElement([(1,3,2),(4,5)]) in rs
            True
            sage: PermutationGroupElement([(1,4)]) in rs
            False
            sage: rs = Tableau([[1, 2],[3]]).row_stabilizer()
            sage: PermutationGroupElement([(1,2),(3,)]) in rs
            True
            sage: rs.one().domain()
            [1, 2, 3]
            sage: rs = Tableau([[1],[2],[3]]).row_stabilizer()
            sage: rs.order()
            1
            sage: rs = Tableau([[2,4,5],[1,3]]).row_stabilizer()
            sage: rs.order()
            12
            sage: rs = Tableau([]).row_stabilizer()
            sage: rs.order()
            1
        """
    def column_stabilizer(self):
        """
        Return the PermutationGroup corresponding to the column stabilizer
        of ``self``.

        This assumes that every integer from `1` to the size of ``self``
        appears exactly once in ``self``.

        EXAMPLES::

            sage: # needs sage.groups
            sage: cs = Tableau([[1,2,3],[4,5]]).column_stabilizer()
            sage: cs.order() == factorial(2)*factorial(2)
            True
            sage: PermutationGroupElement([(1,3,2),(4,5)]) in cs
            False
            sage: PermutationGroupElement([(1,4)]) in cs
            True
        """
    def height(self):
        """
        Return the height of ``self``.

        EXAMPLES::

            sage: Tableau([[1,2,3],[4,5]]).height()
            2
            sage: Tableau([[1,2,3]]).height()
            1
            sage: Tableau([]).height()
            0
        """
    def last_letter_lequal(self, tab2):
        """
        Return ``True`` if ``self`` is less than or equal to ``tab2`` in the last
        letter ordering.

        EXAMPLES::

            sage: st = StandardTableaux([3,2])
            sage: f = lambda b: 1 if b else 0
            sage: matrix([[f(t1.last_letter_lequal(t2)) for t2 in st] for t1 in st])    # needs sage.modules
            [1 1 1 1 1]
            [0 1 1 1 1]
            [0 0 1 1 1]
            [0 0 0 1 1]
            [0 0 0 0 1]
        """
    def charge(self):
        """
        Return the charge of the reading word of ``self``.  See
        :meth:`~sage.combinat.words.finite_word.FiniteWord_class.charge` for more information.

        EXAMPLES::

            sage: Tableau([[1,1],[2,2],[3]]).charge()
            0
            sage: Tableau([[1,1,3],[2,2]]).charge()
            1
            sage: Tableau([[1,1,2],[2],[3]]).charge()
            1
            sage: Tableau([[1,1,2],[2,3]]).charge()
            2
            sage: Tableau([[1,1,2,3],[2]]).charge()
            2
            sage: Tableau([[1,1,2,2],[3]]).charge()
            3
            sage: Tableau([[1,1,2,2,3]]).charge()
            4
        """
    def cocharge(self):
        """
        Return the cocharge of the reading word of ``self``.  See
        :meth:`~sage.combinat.words.finite_word.FiniteWord_class.cocharge` for more information.

        EXAMPLES::

            sage: Tableau([[1,1],[2,2],[3]]).cocharge()
            4
            sage: Tableau([[1,1,3],[2,2]]).cocharge()
            3
            sage: Tableau([[1,1,2],[2],[3]]).cocharge()
            3
            sage: Tableau([[1,1,2],[2,3]]).cocharge()
            2
            sage: Tableau([[1,1,2,3],[2]]).cocharge()
            2
            sage: Tableau([[1,1,2,2],[3]]).cocharge()
            1
            sage: Tableau([[1,1,2,2,3]]).cocharge()
            0
        """
    def add_entry(self, cell, m):
        """
        Return the result of setting the entry in cell ``cell`` equal
        to ``m`` in the tableau ``self``.

        This tableau has larger size than ``self`` if ``cell`` does not
        belong to the shape of ``self``; otherwise, the tableau has the
        same shape as ``self`` and has the appropriate entry replaced.

        INPUT:

        - ``cell`` -- a pair of nonnegative integers

        OUTPUT:

        The tableau ``self`` with the entry in cell ``cell`` set to ``m``. This
        entry overwrites an existing entry if ``cell`` already belongs to
        ``self``, or is added to the tableau if ``cell`` is a cocorner of the
        shape ``self``. (Either way, the input is not modified.)

        .. NOTE::

            Both coordinates of ``cell`` are interpreted as starting at `0`.
            So, ``cell == (0, 0)`` corresponds to the northwesternmost cell.

        EXAMPLES::

            sage: s = StandardTableau([[1,2,5],[3,4]]); s.pp()
              1  2  5
              3  4
            sage: t = s.add_entry( (1,2), 6); t.pp()
              1  2  5
              3  4  6
            sage: t.category()
            Category of elements of Standard tableaux
            sage: s.add_entry( (2,0), 6).pp()
              1  2  5
              3  4
              6
            sage: u = s.add_entry( (1,2), 3); u.pp()
              1  2  5
              3  4  3
            sage: u.category()
            Category of elements of Tableaux
            sage: s.add_entry( (2,2),3)
            Traceback (most recent call last):
            ...
            IndexError: (2, 2) is not an addable cell of the tableau
        """
    def catabolism(self):
        """
        Remove the top row of ``self`` and insert it back in using
        column Schensted insertion (starting with the largest letter).

        EXAMPLES::

            sage: Tableau([]).catabolism()
            []
            sage: Tableau([[1,2,3,4,5]]).catabolism()
            [[1, 2, 3, 4, 5]]
            sage: Tableau([[1,1,3,3],[2,3],[3]]).catabolism()
            [[1, 1, 2, 3, 3, 3], [3]]
            sage: Tableau([[1, 1, 2, 3, 3, 3], [3]]).catabolism()
            [[1, 1, 2, 3, 3, 3, 3]]
        """
    def catabolism_sequence(self):
        """
        Perform :meth:`catabolism` on ``self`` until it returns a
        tableau consisting of a single row.

        EXAMPLES::

            sage: t = Tableau([[1,2,3,4,5,6,8],[7,9]])
            sage: t.catabolism_sequence()
            [[[1, 2, 3, 4, 5, 6, 8], [7, 9]],
             [[1, 2, 3, 4, 5, 6, 7, 9], [8]],
             [[1, 2, 3, 4, 5, 6, 7, 8], [9]],
             [[1, 2, 3, 4, 5, 6, 7, 8, 9]]]
            sage: Tableau([]).catabolism_sequence()
            [[]]
        """
    def lambda_catabolism(self, part):
        """
        Return the ``part``-catabolism of ``self``, where ``part`` is a
        partition (which can be just given as an array).

        For a partition `\\lambda` and a tableau `T`, the
        `\\lambda`-catabolism of `T` is defined by performing the following
        steps.

        1. Truncate the parts of `\\lambda` so that `\\lambda` is contained
           in the shape of `T`.  Let `m` be the length of this partition.

        2. Let `T_a` be the first `m` rows of `T`, and `T_b` be the
           remaining rows.

        3. Let `S_a` be the skew tableau `T_a / \\lambda`.

        4. Concatenate the reading words of `S_a` and `T_b`, and insert
           into a tableau.

        EXAMPLES::

            sage: Tableau([[1,1,3],[2,4,5]]).lambda_catabolism([2,1])
            [[3, 5], [4]]
            sage: t = Tableau([[1,1,3,3],[2,3],[3]])
            sage: t.lambda_catabolism([])
            [[1, 1, 3, 3], [2, 3], [3]]
            sage: t.lambda_catabolism([1])
            [[1, 2, 3, 3, 3], [3]]
            sage: t.lambda_catabolism([1,1])
            [[1, 3, 3, 3], [3]]
            sage: t.lambda_catabolism([2,1])
            [[3, 3, 3, 3]]
            sage: t.lambda_catabolism([4,2,1])
            []
            sage: t.lambda_catabolism([5,1])
            [[3, 3]]
            sage: t.lambda_catabolism([4,1])
            [[3, 3]]
        """
    def reduced_lambda_catabolism(self, part):
        """
        EXAMPLES::

            sage: t = Tableau([[1,1,3,3],[2,3],[3]])
            sage: t.reduced_lambda_catabolism([])
            [[1, 1, 3, 3], [2, 3], [3]]
            sage: t.reduced_lambda_catabolism([1])
            [[1, 2, 3, 3, 3], [3]]
            sage: t.reduced_lambda_catabolism([1,1])
            [[1, 3, 3, 3], [3]]
            sage: t.reduced_lambda_catabolism([2,1])
            [[3, 3, 3, 3]]
            sage: t.reduced_lambda_catabolism([4,2,1])
            []
            sage: t.reduced_lambda_catabolism([5,1])
            0
            sage: t.reduced_lambda_catabolism([4,1])
            0
        """
    def catabolism_projector(self, parts):
        """
        EXAMPLES::

            sage: t = Tableau([[1,1,3,3],[2,3],[3]])
            sage: t.catabolism_projector([[4,2,1]])
            [[1, 1, 3, 3], [2, 3], [3]]
            sage: t.catabolism_projector([[1]])
            []
            sage: t.catabolism_projector([[2,1],[1]])
            []
            sage: t.catabolism_projector([[1,1],[4,1]])
            [[1, 1, 3, 3], [2, 3], [3]]
        """
    def promotion_operator(self, i):
        """
        Return a list of semistandard tableaux obtained by the `i`-th
        Lapointe-Lascoux-Morse promotion operator from the
        semistandard tableau ``self``.

        .. WARNING::

            This is not Schuetzenberger's jeu de taquin promotion!
            For the latter, see :meth:`promotion` and
            :meth:`promotion_inverse`.

        This operator is defined by taking the maximum entry `m` of
        `T`, then adding a horizontal `i`-strip to `T` in all possible
        ways, each time filling this strip with `m+1`'s, and finally
        letting the permutation
        `\\sigma_1 \\sigma_2 \\cdots \\sigma_m = (2, 3, \\ldots, m+1, 1)`
        act on each of the resulting tableaux via the
        Lascoux-Schuetzenberger action
        (:meth:`symmetric_group_action_on_values`). This method
        returns the list of all resulting tableaux. See [LLM2003]_ for
        the purpose of this operator.

        EXAMPLES::

            sage: t = Tableau([[1,2],[3]])
            sage: t.promotion_operator(1)
            [[[1, 2, 4], [3]], [[1, 2], [3, 4]], [[1, 2], [3], [4]]]
            sage: t.promotion_operator(2)
            [[[1, 1, 2, 4], [3]],
             [[1, 1, 4], [2, 3]],
             [[1, 1, 2], [3], [4]],
             [[1, 1], [2, 3], [4]]]
            sage: Tableau([[1]]).promotion_operator(2)
            [[[1, 1, 2]], [[1, 1], [2]]]
            sage: Tableau([[1,1],[2]]).promotion_operator(3)
            [[[1, 1, 1, 2, 3], [2]],
             [[1, 1, 1, 3], [2, 2]],
             [[1, 1, 1, 2], [2], [3]],
             [[1, 1, 1], [2, 2], [3]]]

        The example from [LLM2003]_ p. 12::

            sage: Tableau([[1,1],[2,2]]).promotion_operator(3)
            [[[1, 1, 1, 3, 3], [2, 2]],
             [[1, 1, 1, 3], [2, 2], [3]],
             [[1, 1, 1], [2, 2], [3, 3]]]

        TESTS::

            sage: Tableau([]).promotion_operator(2)
            [[[1, 1]]]
            sage: Tableau([]).promotion_operator(1)
            [[[1]]]
        """
    def raise_action_from_words(self, f, *args):
        """
        EXAMPLES::

            sage: from sage.combinat.tableau import symmetric_group_action_on_values
            sage: import functools
            sage: t = Tableau([[1,1,3,3],[2,3],[3]])
            sage: f = functools.partial(t.raise_action_from_words, symmetric_group_action_on_values)
            sage: f([1,2,3])
            [[1, 1, 3, 3], [2, 3], [3]]
            sage: f([3,2,1])
            [[1, 1, 1, 1], [2, 3], [3]]
            sage: f([1,3,2])
            [[1, 1, 2, 2], [2, 2], [3]]
        """
    def symmetric_group_action_on_values(self, perm):
        """
        Return the image of the semistandard tableau ``self`` under the
        action of the permutation ``perm`` using the
        Lascoux-Schuetzenberger action of the symmetric group `S_n` on
        the semistandard tableaux with ceiling `n`.

        If `n` is a nonnegative integer, then the
        Lascoux-Schuetzenberger action is a group action of the
        symmetric group `S_n` on the set of semistandard Young tableaux
        with ceiling `n` (that is, with entries taken from the set
        `\\{1, 2, \\ldots, n\\}`). It is defined as follows:

        Let `i \\in \\{1, 2, \\ldots, n-1\\}`, and let `T` be a
        semistandard tableau with ceiling `n`. Let `w` be the reading
        word (:meth:`to_word`) of `T`. Replace all letters `i` in `w`
        by closing parentheses, and all letters `i+1` in `w` by
        opening parentheses. Whenever an opening parenthesis stands
        left of a closing parenthesis without there being any
        parentheses in between (it is allowed to have letters
        in-between as long as they are not parentheses), consider these
        two parentheses as matched with each other, and replace them
        back by the letters `i+1` and `i`. Repeat this procedure until
        there are no more opening parentheses standing left of closing
        parentheses. Then, let `a` be the number of opening
        parentheses in the word, and `b` the number of closing
        parentheses (notice that all opening parentheses are right of
        all closing parentheses). Replace the first `a` parentheses
        by the letters `i`, and replace the remaining `b` parentheses
        by the letters `i+1`. Let `w'` be the resulting word. Let
        `T'` be the tableau with the same shape as `T` but with reading
        word `w'`. This tableau `T'` can be shown to be semistandard.
        We define the image of `T` under the action of the simple
        transposition `s_i = (i, i+1) \\in S_n` to be this tableau `T'`.
        It can be shown that these actions of the transpositions
        `s_1, s_2, \\ldots, s_{n-1}` satisfy the Moore-Coxeter relations
        of `S_n`, and thus this extends to a unique action of the
        symmetric group `S_n` on the set of semistandard tableaux with
        ceiling `n`. This is the Lascoux-Schuetzenberger action.

        This action of the symmetric group `S_n` on the set of all
        semistandard tableaux of given shape `\\lambda` with entries
        in `\\{ 1, 2, \\ldots, n \\}` is the one defined in
        [Loth02]_ Theorem 5.6.3. In particular, the action of `s_i`
        is denoted by `\\sigma_i` in said source. (Beware of the typo
        in the definition of `\\sigma_i`: it should say
        `\\sigma_i ( a_i^r a_{i+1}^s ) = a_i^s a_{i+1}^r`, not
        `\\sigma_i ( a_i^r a_{i+1}^s ) = a_i^s a_{i+1}^s`.)

        EXAMPLES::

            sage: t = Tableau([[1,1,3,3],[2,3],[3]])
            sage: t.symmetric_group_action_on_values([1,2,3])
            [[1, 1, 3, 3], [2, 3], [3]]
            sage: t.symmetric_group_action_on_values([2,1,3])
            [[1, 2, 3, 3], [2, 3], [3]]
            sage: t.symmetric_group_action_on_values([3,1,2])
            [[1, 2, 2, 2], [2, 3], [3]]
            sage: t.symmetric_group_action_on_values([2,3,1])
            [[1, 1, 1, 1], [2, 2], [3]]
            sage: t.symmetric_group_action_on_values([3,2,1])
            [[1, 1, 1, 1], [2, 3], [3]]
            sage: t.symmetric_group_action_on_values([1,3,2])
            [[1, 1, 2, 2], [2, 2], [3]]

        TESTS::

            sage: t = Tableau([])
            sage: t.symmetric_group_action_on_values([])
            []
        """
    def socle(self):
        """
        EXAMPLES::

            sage: Tableau([[1,2],[3,4]]).socle()
            2
            sage: Tableau([[1,2,3,4]]).socle()
            4
        """
    def atom(self):
        """
        EXAMPLES::

            sage: Tableau([[1,2],[3,4]]).atom()
            [2, 2]
            sage: Tableau([[1,2,3],[4,5],[6]]).atom()
            [3, 2, 1]
        """
    def symmetric_group_action_on_entries(self, w):
        """
        Return the tableau obtained form this tableau by acting by the
        permutation ``w``.

        Let `T` be a standard tableau of size `n`, then the action of
        `w \\in S_n` is defined by permuting the entries of `T` (recall they
        are `1, 2, \\ldots, n`). In particular, suppose the entry at cell
        `(i, j)` is `a`, then the entry becomes `w(a)`. In general, the
        resulting tableau `wT` may *not* be standard.

        .. NOTE::

            This is different than :meth:`symmetric_group_action_on_values`
            which is defined on semistandard tableaux and is guaranteed to
            return a semistandard tableau.

        INPUT:

        - ``w`` -- a permutation

        EXAMPLES::

            sage: StandardTableau([[1,2,4],[3,5]]).symmetric_group_action_on_entries( Permutation(((4,5))) )
            [[1, 2, 5], [3, 4]]
            sage: _.category()
            Category of elements of Standard tableaux
            sage: StandardTableau([[1,2,4],[3,5]]).symmetric_group_action_on_entries( Permutation(((1,2))) )
            [[2, 1, 4], [3, 5]]
            sage: _.category()
            Category of elements of Tableaux
        """
    def is_key_tableau(self) -> bool:
        """
        Return ``True`` if ``self`` is a key tableau or ``False`` otherwise.

        A tableau is a *key tableau* if the set of entries in the `j`-th
        column is a subset of the set of entries in the `(j-1)`-st column.

        REFERENCES:

        - [LS1990]_

        - [Wil2010]_

        EXAMPLES::

            sage: t = Tableau([[1,1,1],[2,3],[3]])
            sage: t.is_key_tableau()
            True

            sage: t = Tableau([[1,1,2],[2,3],[3]])
            sage: t.is_key_tableau()
            False
        """
    def right_key_tableau(self):
        """
        Return the right key tableau of ``self``.

        The right key tableau of a tableau `T` is a key tableau whose entries
        are weakly greater than the corresponding entries in `T`, and whose column
        reading word is subject to certain conditions. See [LS1990]_ for the full definition.

        ALGORITHM:

        The following algorithm follows [Wil2010]_. Note that if `T` is a key tableau
        then the output of the algorithm is `T`.

        To compute the right key tableau `R` of a tableau `T` we iterate over the columns
        of `T`. Let `T_j` be the `j`-th column of `T` and iterate over the entries
        in `T_j` from bottom to top. Initialize the corresponding entry `k` in `R` to be
        the largest entry in `T_j`. Scan the bottom of each column of `T` to the right of
        `T_j`, updating `k` to be the scanned entry whenever the scanned entry is weakly
        greater than `k`. Update `T_j` and all columns to the right by removing all
        scanned entries.

        .. SEEALSO::

            - :meth:`is_key_tableau()`

        EXAMPLES::

            sage: t = Tableau([[1,2],[2,3]])
            sage: t.right_key_tableau()
            [[2, 2], [3, 3]]
            sage: t = Tableau([[1,1,2,4],[2,3,3],[4],[5]])
            sage: t.right_key_tableau()
            [[2, 2, 2, 4], [3, 4, 4], [4], [5]]

        TESTS:

        We check that if we have a key tableau, we return the same tableau::

            sage: t = Tableau([[1,1,1,2], [2,2,2], [4], [5]])
            sage: t.is_key_tableau()
            True
            sage: t.right_key_tableau() == t
            True

        We check that the empty tableau, which is a key tableau, yields itself::

            sage: Tableau([]).right_key_tableau()
            []
        """
    def left_key_tableau(self):
        """
        Return the left key tableau of ``self``.

        The left key tableau of a tableau `T` is the key tableau whose entries
        are weakly less than the corresponding entries in `T`, and whose column
        reading word is subject to certain conditions. See [LS1990]_ for the full definition.

        ALGORITHM:

        The following algorithm follows [Wil2010]_. Note that if `T` is a key tableau
        then the output of the algorithm is `T`.

        To compute the left key tableau `L` of a tableau `T` we iterate over the columns
        of `T`. Let `T_j` be the `j`-th column of `T` and iterate over the entries
        in `T_j` from bottom to top. Initialize the corresponding entry `k` in `L` as the
        largest entry in `T_j`. Scan the columns to the left of `T_j` and with each column
        update `k` to be the lowest entry in that column which is weakly less than `k`.
        Update `T_j` and all columns to the left by removing all scanned entries.

        .. SEEALSO::

            - :meth:`is_key_tableau()`

        EXAMPLES::

            sage: t = Tableau([[1,2],[2,3]])
            sage: t.left_key_tableau()
            [[1, 1], [2, 2]]
            sage: t = Tableau([[1,1,2,4],[2,3,3],[4],[5]])
            sage: t.left_key_tableau()
            [[1, 1, 1, 2], [2, 2, 2], [4], [5]]

        TESTS:

        We check that if we have a key tableau, we return the same tableau::

            sage: t = Tableau([[1,1,1,2], [2,2,2], [4], [5]])
            sage: t.is_key_tableau()
            True
            sage: t.left_key_tableau() == t
            True

        We check that the empty tableau, which is a key tableau, yields itself::

            sage: Tableau([]).left_key_tableau()
            []
        """
    def seg(self):
        '''
        Return the total number of segments in ``self``, as in [Sal2014]_.

        Let `T` be a tableaux.  We define a `k`-*segment* of `T` (in the `i`-th
        row) to be a maximal consecutive sequence of `k`-boxes in the `i`-th
        row for any `i+1 \\le k \\le r+1`.  Denote the total number of
        `k`-segments in `T` by `\\mathrm{seg}(T)`.

        REFERENCES:

        - [Sal2014]_

        EXAMPLES::

            sage: t = Tableau([[1,1,2,3,5],[2,3,5,5],[3,4]])
            sage: t.seg()
            6

            sage: B = crystals.Tableaux("A4", shape=[4,3,2,1])                          # needs sage.modules
            sage: t = B[31].to_tableau()                                                # needs sage.modules
            sage: t.seg()                                                               # needs sage.modules
            3
        '''
    def flush(self):
        '''
        Return the number of flush segments in ``self``, as in [Sal2014]_.

        Let `1 \\le i < k \\le r+1` and suppose `\\ell` is the smallest integer
        greater than `k` such that there exists an `\\ell`-segment in the
        `(i+1)`-st row of `T`.  A `k`-segment in the `i`-th row of `T` is
        called *flush* if the leftmost box in the `k`-segment and the leftmost
        box of the `\\ell`-segment are in the same column of `T`.  If, however,
        no such `\\ell` exists, then this `k`-segment is said to be *flush* if
        the number of boxes in the `k`-segment is equal to `\\theta_i`, where
        `\\theta_i = \\lambda_i - \\lambda_{i+1}` and the shape of `T` is
        `\\lambda = (\\lambda_1 > \\lambda_2 > \\cdots > \\lambda_r)`.  Denote the
        number of flush `k`-segments in `T` by `\\mathrm{flush}(T)`.

        EXAMPLES::

            sage: t = Tableau([[1,1,2,3,5],[2,3,5,5],[3,4]])
            sage: t.flush()
            3

            sage: B = crystals.Tableaux("A4", shape=[4,3,2,1])                          # needs sage.modules
            sage: t = B[32].to_tableau()                                                # needs sage.modules
            sage: t.flush()                                                             # needs sage.modules
            4
        '''
    def content(self, k, multicharge=[0]):
        """
        Return the content of ``k`` in the standard tableau ``self``.

        The content of `k` is `c - r` if `k` appears in row `r` and
        column `c` of the tableau.

        The ``multicharge`` is a list of length 1 which gives an offset for
        all of the contents. It is included mainly for compatibility with
        :meth:`sage.combinat.tableau_tuple.TableauTuple`.

        EXAMPLES::

            sage: StandardTableau([[1,2],[3,4]]).content(3)
            -1

            sage: StandardTableau([[1,2],[3,4]]).content(6)
            Traceback (most recent call last):
            ...
            ValueError: 6 does not appear in tableau
        """
    def residue(self, k, e, multicharge=(0,)):
        """
        Return the residue of the integer ``k`` in the tableau ``self``.

        The *residue* of `k` in a standard tableau is `c - r + m`
        in `\\ZZ / e\\ZZ`, where `k` appears in row `r` and column `c`
        of the tableau with multicharge `m`.

        INPUT:

        - ``k`` -- integer in `\\{1, 2, \\ldots, n\\}`
        - ``e`` -- integer in `\\{0, 2, 3, 4, 5, \\ldots\\}`
        - ``multicharge`` -- (default: ``[0]``) a list of length 1

        Here `n` is its size of ``self``.

        The ``multicharge`` is a list of length 1 which gives an offset for
        all of the contents. It is included mainly for compatibility with
        :meth:`~sage.combinat.tableau_tuples.TableauTuple.residue`.

        OUTPUT: the residue in `\\ZZ / e\\ZZ`

        EXAMPLES::

            sage: StandardTableau([[1,2,5],[3,4]]).residue(1,3)
            0
            sage: StandardTableau([[1,2,5],[3,4]]).residue(2,3)
            1
            sage: StandardTableau([[1,2,5],[3,4]]).residue(3,3)
            2
            sage: StandardTableau([[1,2,5],[3,4]]).residue(4,3)
            0
            sage: StandardTableau([[1,2,5],[3,4]]).residue(5,3)
            2
            sage: StandardTableau([[1,2,5],[3,4]]).residue(6,3)
            Traceback (most recent call last):
            ...
            ValueError: 6 does not appear in the tableau
        """
    def residue_sequence(self, e, multicharge=(0,)):
        """
        Return the :class:`sage.combinat.tableau_residues.ResidueSequence`
        of the tableau ``self``.

        INPUT:

        - ``e`` -- integer in `\\{0, 2, 3, 4, 5, \\ldots\\}`
        - ``multicharge`` -- (default: ``[0]``) a sequence of integers
          of length 1

        The `multicharge` is a list of length 1 which gives an offset for
        all of the contents. It is included mainly for compatibility with
        :meth:`~sage.combinat.tableau_tuples.StandardTableauTuple.residue`.

        OUTPUT:

        The corresponding residue sequence of the tableau;
        see :class:`ResidueSequence`.

        EXAMPLES::

            sage: StandardTableauTuple([[1,2],[3,4]]).residue_sequence(2)               # needs sage.groups
            2-residue sequence (0,1,1,0) with multicharge (0)
            sage: StandardTableauTuple([[1,2],[3,4]]).residue_sequence(3)               # needs sage.groups
            3-residue sequence (0,1,2,0) with multicharge (0)
            sage: StandardTableauTuple([[1,2],[3,4]]).residue_sequence(4)               # needs sage.groups
            4-residue sequence (0,1,3,0) with multicharge (0)
        """
    def degree(self, e, multicharge=(0,)):
        """
        Return the Brundan-Kleshchev-Wang [BKW2011]_ degree of ``self``.

        The *degree* is an integer that is defined recursively by successively
        stripping off the number `k`, for `k = n, n-1, \\ldots, 1` and at stage
        adding the number of addable cell of the same residue minus the number
        of removable cells of the same residue as `k` and which are below `k`
        in the diagram.

        The degrees of the tableau `T` gives the degree of the homogeneous
        basis element of the graded Specht module that is indexed by `T`.

        INPUT:

        - ``e`` -- the *quantum characteristic*
        - ``multicharge`` -- (default: ``[0]``) the multicharge

        OUTPUT: the degree of the tableau ``self``, which is an integer

        EXAMPLES::

            sage: StandardTableau([[1,2,5],[3,4]]).degree(3)                            # needs sage.groups
            0
            sage: StandardTableau([[1,2,5],[3,4]]).degree(4)                            # needs sage.groups
            1
        """
    def codegree(self, e, multicharge=(0,)):
        '''
        Return the Brundan-Kleshchev-Wang [BKW2011]_ codegree of the
        standard tableau ``self``.

        The *codegree* of a tableau is an integer that is defined recursively by
        successively stripping off the number `k`, for `k = n, n-1, \\ldots, 1`
        and at stage adding the number of addable cell of the same residue
        minus the number of removable cells of the same residue as `k` and
        are above `k` in the diagram.

        The codegree of the tableau `T` gives the degree of  "dual"
        homogeneous basis element of the Graded Specht module that
        is indexed by `T`.

        INPUT:

        - ``e`` -- the *quantum characteristic*
        - ``multicharge`` -- (default: ``[0]``) the multicharge

        OUTPUT: the codegree of the tableau ``self``, which is an integer

        EXAMPLES::

            sage: StandardTableau([[1,3,5],[2,4]]).codegree(3)                          # needs sage.groups
            0
            sage: StandardTableau([[1,2,5],[3,4]]).codegree(3)                          # needs sage.groups
            1
            sage: StandardTableau([[1,2,5],[3,4]]).codegree(4)                          # needs sage.groups
            0
        '''
    def first_row_descent(self):
        """
        Return the first cell where the tableau ``self`` is not row standard.

        Cells are ordered left to right along the rows and then top to bottom.
        That is, the cell `(r,c)` with `r` and `c` minimal such that the entry
        in position `(r,c)` is bigger than the entry in position `(r, c+1)`.
        If there is no such cell then ``None`` is returned - in this case the
        tableau is row strict.

        OUTPUT:

        The first cell which there is a descent or ``None`` if no such
        cell exists.

        EXAMPLES::

            sage: t = Tableau([[1,3,2],[4]]); t.first_row_descent()
            (0, 1)
            sage: Tableau([[1,2,3],[4]]).first_row_descent() is  None
            True
        """
    def first_column_descent(self):
        """
        Return the first cell where ``self`` is not column standard.

        Cells are ordered left to right along the rows and then top to bottom.
        That is, the cell `(r, c)` with `r` and `c` minimal such that
        the entry in position `(r, c)` is bigger than the entry in position
        `(r, c+1)`. If there is no such cell then ``None`` is returned - in
        this case the tableau is column strict.

        OUTPUT:

        The first cell which there is a descent or ``None`` if no such
        cell exists.

        EXAMPLES::

            sage: Tableau([[1,4,5],[2,3]]).first_column_descent()
            (0, 1)
            sage: Tableau([[1,2,3],[4]]).first_column_descent() is None
            True
        """
    def reduced_row_word(self):
        """
        Return the lexicographically minimal reduced expression for the
        permutation that maps the :meth:`initial_tableau` to ``self``.

        Ths reduced expression is a minimal length coset representative for the
        corresponding Young subgroup.  In one line notation, the permutation is
        obtained by concatenating the rows of the tableau in order from top to
        bottom.

        EXAMPLES::

            sage: StandardTableau([[1,2,3],[4,5],[6]]).reduced_row_word()
            []
            sage: StandardTableau([[1,2,3],[4,6],[5]]).reduced_row_word()
            [5]
            sage: StandardTableau([[1,2,4],[3,6],[5]]).reduced_row_word()
            [3, 5]
            sage: StandardTableau([[1,2,5],[3,6],[4]]).reduced_row_word()
            [3, 5, 4]
            sage: StandardTableau([[1,2,6],[3,5],[4]]).reduced_row_word()
            [3, 4, 5, 4]
        """
    def reduced_column_word(self):
        """
        Return the lexicographically minimal reduced expression for the
        permutation that maps the conjugate of the :meth:`initial_tableau`
        to ``self``.

        Ths reduced expression is a minimal length coset representative for
        the corresponding Young subgroup.  In one line notation, the
        permutation is obtained by concatenating the columns of the
        tableau in order from top to bottom.

        EXAMPLES::

            sage: StandardTableau([[1,4,6],[2,5],[3]]).reduced_column_word()
            []
            sage: StandardTableau([[1,4,5],[2,6],[3]]).reduced_column_word()
            [5]
            sage: StandardTableau([[1,3,6],[2,5],[4]]).reduced_column_word()
            [3]
            sage: StandardTableau([[1,3,5],[2,6],[4]]).reduced_column_word()
            [3, 5]
            sage: StandardTableau([[1,2,5],[3,6],[4]]).reduced_column_word()
            [3, 2, 5]
        """
    def hillman_grassl(self):
        """
        Return the image of the `\\lambda`-array ``self`` under the
        Hillman-Grassl correspondence (as a
        :class:`~sage.combinat.hillman_grassl.WeakReversePlanePartition`).

        This relies on interpreting ``self`` as a `\\lambda`-array
        in the sense of :mod:`~sage.combinat.hillman_grassl`.

        Fix a partition `\\lambda`
        (see :meth:`~sage.combinat.partition.Partition`).
        We draw all partitions and tableaux in English notation.

        A `\\lambda`-*array* will mean a tableau of shape `\\lambda` whose
        entries are nonnegative integers. (No conditions on the order of
        these entries are made. Note that `0` is allowed.)

        A *weak reverse plane partition of shape* `\\lambda` (short:
        `\\lambda`-*rpp*) will mean a `\\lambda`-array whose entries weakly
        increase along each row and weakly increase along each column.

        The Hillman-Grassl correspondence `H` is the map that sends a
        `\\lambda`-array `M` to a `\\lambda`-rpp `H(M)` defined recursively
        as follows:

        * If all entries of `M` are `0`, then `H(M) = M`.

        * Otherwise, let `s` be the index of the leftmost column of `M`
          containing a nonzero entry.
          Let `r` be the index of the bottommost nonzero entry in the
          `s`-th column of `M`. Let `M'` be the `\\lambda`-array obtained
          from `M` by subtracting `1` from the `(r, s)`-th entry of `M`.
          Let `Q = (q_{i, j})` be the image `H(M')` (which is already
          defined by recursion).

        * Define a sequence `((i_1, j_1), (i_2, j_2), \\ldots,
          (i_n, j_n))` of boxes in the diagram of `\\lambda` (actually a
          lattice path made of southward and westward steps) as follows:
          Set `(i_1, j_1) = (r, \\lambda_r)` (the rightmost box in the
          `r`-th row of `\\lambda`). If `(i_k, j_k)` is defined for some
          `k \\geq 1`, then `(i_{k+1}, j_{k+1})` is constructed as follows:
          If `q_{i_k + 1, j_k}` is well-defined and equals `q_{i_k, j_k}`,
          then we set `(i_{k+1}, j_{k+1}) = (i_k + 1, j_k)`.
          Otherwise, if `j_k = s`, then the sequence ends here.
          Otherwise, we set `(i_{k+1}, j_{k+1}) = (i_k, j_k - 1)`.

        * Let `H(M)` be the array obtained from `Q` by adding `1` to
          the `(i_k, j_k)`-th entry of `Q` for each
          `k \\in \\{1, 2, \\ldots, n\\}`.

        See [Gans1981]_ (Section 3) for this construction.

        .. SEEALSO::

            :meth:`~sage.combinat.hillman_grassl.hillman_grassl`
            for the Hillman-Grassl correspondence as a standalone
            function.

            :meth:`~sage.combinat.hillman_grassl.WeakReversePlanePartition.hillman_grassl_inverse`
            for the inverse map.

        EXAMPLES::

            sage: a = Tableau([[2, 1, 1], [0, 2, 0], [1, 1]])
            sage: A = a.hillman_grassl(); A
            [[2, 2, 4], [2, 3, 4], [3, 5]]
            sage: A.parent(), a.parent()
            (Weak Reverse Plane Partitions, Tableaux)
        """
    def sulzgruber_correspondence(self):
        """
        Return the image of the `\\lambda`-array ``self`` under the
        Sulzgruber correspondence (as a
        :class:`~sage.combinat.hillman_grassl.WeakReversePlanePartition`).

        This relies on interpreting ``self`` as a `\\lambda`-array
        in the sense of :mod:`~sage.combinat.hillman_grassl`.
        See :mod:`~sage.combinat.hillman_grassl` for definitions
        of the objects involved.

        The Sulzgruber correspondence is the map `\\Phi_\\lambda`
        from [Sulzgr2017]_ Section 7, and is the map
        `\\xi_\\lambda^{-1}` from [Pak2002]_ Section 5.
        It is denoted by `\\mathcal{RSK}` in [Hopkins2017]_.
        It is the inverse of the Pak correspondence
        (:meth:`pak_correspondence`).
        The following description of the Sulzgruber correspondence
        follows [Hopkins2017]_ (which denotes it by `\\mathcal{RSK}`):

        Fix a partition `\\lambda`
        (see :meth:`~sage.combinat.partition.Partition`).
        We draw all partitions and tableaux in English notation.

        A `\\lambda`-*array* will mean a tableau of shape `\\lambda` whose
        entries are nonnegative integers. (No conditions on the order of
        these entries are made. Note that `0` is allowed.)

        A *weak reverse plane partition of shape* `\\lambda` (short:
        `\\lambda`-*rpp*) will mean a `\\lambda`-array whose entries weakly
        increase along each row and weakly increase along each column.

        We shall also use the following notation:
        If `(u, v)` is a cell of `\\lambda`, and if `\\pi` is a
        `\\lambda`-rpp, then:

        * the *lower bound* of `\\pi` at `(u, v)` (denoted by
          `\\pi_{<(u, v)}`) is defined to be
          `\\max \\{ \\pi_{u-1, v} , \\pi_{u, v-1} \\}` (where
          `\\pi_{0, v}` and `\\pi_{u, 0}` are understood to mean `0`).

        * the *upper bound* of `\\pi` at `(u, v)` (denoted by
          `\\pi_{>(u, v)}`) is defined to be
          `\\min \\{ \\pi_{u+1, v} , \\pi_{u, v+1} \\}`
          (where `\\pi_{i, j}` is understood to mean `+ \\infty`
          if `(i, j)` is not in `\\lambda`; thus, the upper
          bound at a corner cell is `+ \\infty`).

        * *toggling* `\\pi` at `(u, v)` means replacing the entry
          `\\pi_{u, v}` of `\\pi` at `(u, v)` by
          `\\pi_{<(u, v)} + \\pi_{>(u, v)} - \\pi_{u, v}`
          (this is well-defined as long as `(u, v)` is not a
          corner of `\\lambda`).

        Note that every `\\lambda`-rpp `\\pi` and every cell
        `(u, v)` of `\\lambda` satisfy
        `\\pi_{<(u, v)} \\leq \\pi_{u, v} \\leq \\pi_{>(u, v)}`.
        Note that toggling a `\\lambda`-rpp (at a cell that is not
        a corner) always results in a `\\lambda`-rpp. Also,
        toggling is an involution).

        The Pak correspondence `\\xi_\\lambda` sends a `\\lambda`-rpp `\\pi`
        to a `\\lambda`-array `\\xi_\\lambda(\\pi)`. It is defined by
        recursion on `\\lambda` (that is, we assume that `\\xi_\\mu` is
        already defined for every partition `\\mu` smaller than
        `\\lambda`), and its definition proceeds as follows:

        * If `\\lambda = \\varnothing`, then `\\xi_\\lambda` is the
          obvious bijection sending the only `\\varnothing`-rpp
          to the only `\\varnothing`-array.

        * Pick any corner `c = (i, j)` of `\\lambda`, and let `\\mu`
          be the result of removing this corner `c` from the partition
          `\\lambda`.
          (The exact choice of `c` is immaterial.)

        * Let `\\pi'` be what remains of `\\pi` when the corner cell `c`
          is removed.

        * For each positive integer `k` such that `(i-k, j-k)` is a
          cell of `\\lambda`, toggle `\\pi'` at `(i-k, j-k)`.
          (All these togglings commute, so the order in which they
          are made is immaterial.)

        * Let `M = \\xi_\\mu(\\pi')`.

        * Extend the `\\mu`-array `M` to a `\\lambda`-array `M'` by
          adding the cell `c` and writing the number
          `\\pi_{i, j} - \\pi_{<(i, j)}` into this cell.

        * Set `\\xi_\\lambda(\\pi) = M'`.

        .. SEEALSO::

            :meth:`~sage.combinat.hillman_grassl.sulzgruber_correspondence`
            for the Sulzgruber correspondence as a standalone function.

            :meth:`~sage.combinat.hillman_grassl.WeakReversePlanePartition.pak_correspondence`
            for the inverse map.

        EXAMPLES::

            sage: a = Tableau([[2, 1, 1], [0, 2, 0], [1, 1]])
            sage: A = a.sulzgruber_correspondence(); A
            [[0, 1, 4], [1, 5, 5], [3, 6]]
            sage: A.parent(), a.parent()
            (Weak Reverse Plane Partitions, Tableaux)

            sage: a = Tableau([[1, 3], [0, 1]])
            sage: a.sulzgruber_correspondence()
            [[0, 4], [1, 5]]
        """

class SemistandardTableau(Tableau):
    """
    A class to model a semistandard tableau.

    INPUT:

    - ``t`` -- a tableau, a list of iterables, or an empty list

    OUTPUT: a SemistandardTableau object constructed from ``t``

    A semistandard tableau is a tableau whose entries are positive integers,
    which are weakly increasing in rows and strictly increasing down columns.

    EXAMPLES::

        sage: t = SemistandardTableau([[1,2,3],[2,3]]); t
        [[1, 2, 3], [2, 3]]
        sage: t.shape()
        [3, 2]
        sage: t.pp() # pretty printing
        1 2 3
        2 3
        sage: t = Tableau([[1,2],[2]])
        sage: s = SemistandardTableau(t); s
        [[1, 2], [2]]
        sage: SemistandardTableau([]) # The empty tableau
        []

    When using code that will generate a lot of tableaux, it is slightly more
    efficient to construct a SemistandardTableau from the appropriate
    :class:`Parent` object::

        sage: SST = SemistandardTableaux()
        sage: SST([[1, 2, 3], [4, 5]])
        [[1, 2, 3], [4, 5]]

    .. SEEALSO::

        - :class:`Tableaux`
        - :class:`Tableau`
        - :class:`SemistandardTableaux`
        - :class:`StandardTableaux`
        - :class:`StandardTableau`

    TESTS::

        sage: t = Tableaux()([[1,1],[2]])
        sage: s = SemistandardTableaux(3)([[1,1],[2]])
        sage: s == t
        True
        sage: s.parent()
        Semistandard tableaux of size 3 and maximum entry 3
        sage: r = SemistandardTableaux(3)(t); r.parent()
        Semistandard tableaux of size 3 and maximum entry 3
        sage: isinstance(r, Tableau)
        True
        sage: s2 = SemistandardTableaux(3)([(1,1),(2,)])
        sage: s2 == s
        True
        sage: s2.parent()
        Semistandard tableaux of size 3 and maximum entry 3
    """
    @staticmethod
    def __classcall_private__(self, t):
        """
        This ensures that a SemistandardTableau is only ever constructed as an
        element_class call of an appropriate parent.

        TESTS::

            sage: t = SemistandardTableau([[1,1],[2]])
            sage: TestSuite(t).run()

            sage: t.parent()
            Semistandard tableaux
            sage: t.category()
            Category of elements of Semistandard tableaux
            sage: type(t)
            <class 'sage.combinat.tableau.SemistandardTableaux_all_with_category.element_class'>
        """
    def check(self) -> None:
        """
        Check that ``self`` is a valid semistandard tableau.

        TESTS::

            sage: SemistandardTableau([[1,2,3],[1]])  # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: column (0) is not strictly increasing between rows (0, 1)

            sage: SemistandardTableau([[1,2,1]])  # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: row (0) is not weakly increasing between columns (1, 2)

            sage: SemistandardTableau([[0,1]])  # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: expected entry to be a positive integer at (row=0, col=0). Found (0)
        """

class RowStandardTableau(Tableau):
    """
    A class to model a row standard tableau.

    A row standard tableau is a tableau whose entries are
    positive integers from 1 to `m` that increase along rows.

    INPUT:

    - ``t`` -- a Tableau, a list of iterables, or an empty list

    EXAMPLES::

        sage: t = RowStandardTableau([[3,4,5],[1,2]]); t
        [[3, 4, 5], [1, 2]]
        sage: t.shape()
        [3, 2]
        sage: t.pp() # pretty printing
        3  4  5
        1  2
        sage: t.is_standard()
        False
        sage: RowStandardTableau([]) # The empty tableau
        []
        sage: RowStandardTableau([[3,4,5],[1,2]]) in StandardTableaux()
        False
        sage: RowStandardTableau([[1,2,5],[3,4]]) in StandardTableaux()
        True

    When using code that will generate a lot of tableaux, it is more
    efficient to construct a :class:`RowStandardTableau` from the
    appropriate :class:`Parent` object::

        sage: ST = RowStandardTableaux()
        sage: ST([[3, 4, 5], [1, 2]])
        [[3, 4, 5], [1, 2]]

    .. SEEALSO::

        - :class:`Tableau`
        - :class:`StandardTableau`
        - :class:`SemistandardTableau`
        - :class:`Tableaux`
        - :class:`StandardTableaux`
        - :class:`RowStandardTableaux`
        - :class:`SemistandardTableaux`

    TESTS::

        sage: t = Tableaux()([[1,2],[3]])
        sage: s = RowStandardTableaux(3)([[1,2],[3]])
        sage: s == t
        True
        sage: u = RowStandardTableaux(3)([[2, 3], [1]])
        sage: s == u
        False
        sage: u.parent()
        Row standard tableaux of size 3
        sage: u = RowStandardTableaux(3)(u)
        sage: u.parent()
        Row standard tableaux of size 3
        sage: isinstance(u, Tableau)
        True
    """
    @staticmethod
    def __classcall_private__(self, t):
        """
        This ensures that a :class:`RowStandardTableau` is only
        constructed as an ``element_class`` call of an appropriate parent.

        TESTS::

            sage: t = RowStandardTableau([[2,3],[1]])
            sage: TestSuite(t).run()

            sage: t.parent()
            Row standard tableaux
            sage: type(t)
            <class 'sage.combinat.tableau.RowStandardTableaux_all_with_category.element_class'>
        """
    def check(self) -> None:
        """
        Check that ``self`` is a valid row standard tableau.

        TESTS::

            sage: RowStandardTableau([[1,4,4],[2,3]])  # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: the entries in a row standard tableau must increase
             along rows and contain the numbers 1,2,...,n

            sage: RowStandardTableau([[1,3,2]])  # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: the entries in a row standard tableau must increase
             along rows and contain the numbers 1,2,...,n
        """

class StandardTableau(SemistandardTableau):
    """
    A class to model a standard tableau.

    INPUT:

    - ``t`` -- a Tableau, a list of iterables, or an empty list

    A standard tableau is a semistandard tableau whose entries are exactly the
    positive integers from 1 to `n`, where `n` is the size of the tableau.

    EXAMPLES::

        sage: t = StandardTableau([[1,2,3],[4,5]]); t
        [[1, 2, 3], [4, 5]]
        sage: t.shape()
        [3, 2]
        sage: t.pp() # pretty printing
        1 2 3
        4 5
        sage: t.is_standard()
        True
        sage: StandardTableau([]) # The empty tableau
        []
        sage: StandardTableau([[1,2,3],[4,5]]) in RowStandardTableaux()
        True

    When using code that will generate a lot of tableaux, it is more
    efficient to construct a StandardTableau from the appropriate
    :class:`Parent` object::

        sage: ST = StandardTableaux()
        sage: ST([[1, 2, 3], [4, 5]])
        [[1, 2, 3], [4, 5]]

    .. SEEALSO::

        - :class:`Tableaux`
        - :class:`Tableau`
        - :class:`SemistandardTableaux`
        - :class:`SemistandardTableau`
        - :class:`StandardTableaux`

    TESTS::

        sage: t = Tableaux()([[1,2],[3]])
        sage: s = StandardTableaux(3)([[1,2],[3]])
        sage: s == t
        True
        sage: s.parent()
        Standard tableaux of size 3
        sage: r = StandardTableaux(3)(t); r.parent()
        Standard tableaux of size 3
        sage: isinstance(r, Tableau)
        True
    """
    @staticmethod
    def __classcall_private__(self, t):
        """
        This ensures that a :class:`StandardTableau` is only ever constructed
        as an ``element_class`` call of an appropriate parent.

        TESTS::

            sage: t = StandardTableau([[1,2],[3]])
            sage: TestSuite(t).run()

            sage: t.parent()
            Standard tableaux
            sage: type(t)
            <class 'sage.combinat.tableau.StandardTableaux_all_with_category.element_class'>
        """
    def check(self) -> None:
        """
        Check that ``self`` is a standard tableau.

        TESTS::

            sage: StandardTableau([[1,2,3],[4,4]])  # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: the entries in a standard tableau must be in bijection with 1,2,...,n

            sage: StandardTableau([[1,3,2]])  # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: the entries in each row of a semistandard tableau must be weakly increasing
        """
    def dominates(self, t):
        """
        Return ``True`` if ``self`` dominates the tableau ``t``.

        That is, if the shape of the tableau restricted to `k`
        dominates the shape of ``t`` restricted to `k`, for `k = 1, 2,
        \\ldots, n`.

        When the two tableaux have the same shape, then this ordering
        coincides with the Bruhat ordering for the corresponding permutations.

        INPUT:

        - ``t`` -- a tableau

        EXAMPLES::

            sage: s = StandardTableau([[1,2,3],[4,5]])
            sage: t = StandardTableau([[1,2],[3,5],[4]])
            sage: s.dominates(t)
            True
            sage: t.dominates(s)
            False
            sage: all(StandardTableau(s).dominates(t) for t in StandardTableaux([3,2]))
            True
            sage: s.dominates([[1,2,3,4,5]])
            False
        """
    def is_standard(self) -> bool:
        """
        Return ``True`` since ``self`` is a standard tableau.

        EXAMPLES::

            sage: StandardTableau([[1, 3], [2, 4]]).is_standard()
            True
        """
    def up(self) -> Generator[Incomplete]:
        """
        An iterator for all the standard tableaux that can be
        obtained from ``self`` by adding a cell.

        EXAMPLES::

            sage: t = StandardTableau([[1,2]])
            sage: [x for x in t.up()]
            [[[1, 2, 3]], [[1, 2], [3]]]
        """
    def up_list(self):
        """
        Return a list of all the standard tableaux that can be obtained
        from ``self`` by adding a cell.

        EXAMPLES::

            sage: t = StandardTableau([[1,2]])
            sage: t.up_list()
            [[[1, 2, 3]], [[1, 2], [3]]]
        """
    def down(self) -> Generator[Incomplete]:
        """
        An iterator for all the standard tableaux that can be obtained
        from ``self`` by removing a cell. Note that this iterates just
        over a single tableau (or nothing if ``self`` is empty).

        EXAMPLES::

            sage: t = StandardTableau([[1,2],[3]])
            sage: [x for x in t.down()]
            [[[1, 2]]]
            sage: t = StandardTableau([])
            sage: [x for x in t.down()]
            []
        """
    def down_list(self):
        """
        Return a list of all the standard tableaux that can be obtained
        from ``self`` by removing a cell. Note that this is just a singleton
        list if ``self`` is nonempty, and an empty list otherwise.

        EXAMPLES::

            sage: t = StandardTableau([[1,2],[3]])
            sage: t.down_list()
            [[[1, 2]]]
            sage: t = StandardTableau([])
            sage: t.down_list()
            []
        """
    def standard_descents(self):
        """
        Return a list of the integers `i` such that `i` appears
        strictly further north than `i + 1` in ``self`` (this is not
        to say that `i` and `i + 1` must be in the same column). The
        list is sorted in increasing order.

        EXAMPLES::

            sage: StandardTableau( [[1,3,4],[2,5]] ).standard_descents()
            [1, 4]
            sage: StandardTableau( [[1,2],[3,4]] ).standard_descents()
            [2]
            sage: StandardTableau( [[1,2,5],[3,4],[6,7],[8],[9]] ).standard_descents()
            [2, 5, 7, 8]
            sage: StandardTableau( [] ).standard_descents()
            []
        """
    def standard_number_of_descents(self):
        """
        Return the number of all integers `i` such that `i` appears
        strictly further north than `i + 1` in ``self`` (this is not
        to say that `i` and `i + 1` must be in the same column). A
        list of these integers can be obtained using the
        :meth:`standard_descents` method.

        EXAMPLES::

            sage: StandardTableau( [[1,2],[3,4],[5]] ).standard_number_of_descents()
            2
            sage: StandardTableau( [] ).standard_number_of_descents()
            0
            sage: tabs = StandardTableaux(5)
            sage: all( t.standard_number_of_descents() == t.schuetzenberger_involution().standard_number_of_descents() for t in tabs )
            True
        """
    def standard_major_index(self):
        """
        Return the major index of the standard tableau ``self`` in the
        standard meaning of the word. The major index is defined to be
        the sum of the descents of ``self`` (see :meth:`standard_descents`
        for their definition).

        EXAMPLES::

            sage: StandardTableau( [[1,4,5],[2,6],[3]] ).standard_major_index()
            8
            sage: StandardTableau( [[1,2],[3,4]] ).standard_major_index()
            2
            sage: StandardTableau( [[1,2,3],[4,5]] ).standard_major_index()
            3
        """
    def promotion_inverse(self, n=None):
        '''
        Return the image of ``self`` under the inverse promotion operator.
        The optional variable `m` should be set to the size of ``self`` minus
        `1` for a minimal speedup; otherwise, it defaults to this number.

        The inverse promotion operator, applied to a standard tableau `t`,
        does the following:

        Remove the letter `1` from `t`, thus leaving a hole where it used to be.
        Apply jeu de taquin to move this hole northeast (in French notation)
        until it reaches the outer boundary of `t`. Fill `n + 1` into this hole,
        where `n` is the size of `t`. Finally, subtract `1` from each letter in
        the tableau. This yields a new standard tableau.

        This definition of inverse promotion is the map called "promotion" in
        [Sag2011]_ (p. 23) and in [Stan2009]_, and is the inverse of the map
        called "promotion" in [Hai1992]_ (p. 90).

        See the :meth:`~sage.combinat.tableau.promotion_inverse` method for a
        more general operator.

        EXAMPLES::

            sage: t = StandardTableau([[1,3],[2,4]])
            sage: t.promotion_inverse()
            [[1, 2], [3, 4]]

        We check the equivalence of two definitions of inverse promotion on
        standard tableaux::

            sage: ST = StandardTableaux(7)
            sage: def bk_promotion_inverse7(st):
            ....:     st2 = st
            ....:     for i in range(1, 7):
            ....:         st2 = st2.bender_knuth_involution(i, check=False)
            ....:     return st2
            sage: all( bk_promotion_inverse7(st) == st.promotion_inverse() for st in ST ) # long time
            True
        '''
    def promotion(self, n=None):
        '''
        Return the image of ``self`` under the promotion operator.

        The promotion operator, applied to a standard tableau `t`, does the
        following:

        Remove the letter `n` from `t`, thus leaving a hole where it used to be.
        Apply jeu de taquin to move this hole southwest (in French notation)
        until it reaches the inner boundary of `t`. Fill `0` into the hole once
        jeu de taquin has completed. Finally, add `1` to each letter in the
        tableau. The resulting standard tableau is the image of `t` under the
        promotion operator.

        This definition of promotion is precisely the one given in [Hai1992]_
        (p. 90). It is the inverse of the maps called "promotion" in [Sag2011]_
        (p. 23) and in [Stan2009]_.

        See the :meth:`~sage.combinat.tableau.promotion` method for a
        more general operator.

        EXAMPLES::

            sage: ST = StandardTableaux(7)
            sage: all( st.promotion().promotion_inverse() == st for st in ST ) # long time
            True
            sage: all( st.promotion_inverse().promotion() == st for st in ST ) # long time
            True
            sage: st = StandardTableau([[1,2,5],[3,4]])
            sage: parent(st.promotion())
            Standard tableaux
        '''

def from_chain(chain):
    """
    Return a semistandard tableau from a chain of partitions.

    EXAMPLES::

        sage: from sage.combinat.tableau import from_chain
        sage: from_chain([[], [2], [2, 1], [3, 2, 1]])
        [[1, 1, 3], [2, 3], [3]]
    """
def from_shape_and_word(shape, w, convention: str = 'French'):
    """
    Return a tableau from a shape and word.

    INPUT:

    - ``shape`` -- a partition

    - ``w`` -- a word whose length equals that of the partition

    - ``convention`` -- string (default: ``'French'``); can take values
      ``'French'`` or ``'English'``

    OUTPUT:

    A tableau, whose shape is ``shape`` and whose reading word is ``w``.
    If the ``convention`` is specified as ``'French'``, the reading word is to be read
    starting from the top row in French convention (= the bottom row in English
    convention). If the ``convention`` is specified as ``'English'``, the reading word
    is to be read starting with the top row in English convention.

    EXAMPLES::

        sage: from sage.combinat.tableau import from_shape_and_word
        sage: t = Tableau([[1, 3], [2], [4]])
        sage: shape = t.shape(); shape
        [2, 1, 1]
        sage: word = t.to_word(); word
        word: 4213
        sage: from_shape_and_word(shape, word)
        [[1, 3], [2], [4]]
        sage: word = Word(flatten(t))
        sage: from_shape_and_word(shape, word, convention='English')
        [[1, 3], [2], [4]]
    """

class IncreasingTableau(Tableau):
    """
    A class to model an increasing tableau.

    INPUT:

    - ``t`` -- a tableau, a list of iterables, or an empty list

    An *increasing tableau* is a tableau whose entries are positive
    integers that are strictly increasing across rows and strictly
    increasing down columns.

    EXAMPLES::

        sage: t = IncreasingTableau([[1,2,3],[2,3]]); t
        [[1, 2, 3], [2, 3]]
        sage: t.shape()
        [3, 2]
        sage: t.pp() # pretty printing
        1 2 3
        2 3
        sage: t = Tableau([[1,2],[2]])
        sage: s = IncreasingTableau(t); s
        [[1, 2], [2]]
        sage: IncreasingTableau([]) # The empty tableau
        []

    You can also construct an :class:`IncreasingTableau` from the
    appropriate :class:`Parent` object::

        sage: IT = IncreasingTableaux()
        sage: IT([[1, 2, 3], [4, 5]])
        [[1, 2, 3], [4, 5]]

    .. SEEALSO::

        - :class:`Tableaux`
        - :class:`Tableau`
        - :class:`SemistandardTableaux`
        - :class:`SemistandardTableau`
        - :class:`StandardTableaux`
        - :class:`StandardTableau`
        - :class:`IncreasingTableaux`

    TESTS::

        sage: t = Tableaux()([[1,2],[2]])
        sage: s = IncreasingTableaux(3)([[1,2],[2]])
        sage: s == t
        True
        sage: s.parent()
        Increasing tableaux of size 3 and maximum entry 3
        sage: r = IncreasingTableaux(3)(t); r.parent()
        Increasing tableaux of size 3 and maximum entry 3
        sage: isinstance(r, Tableau)
        True
        sage: s2 = IncreasingTableaux(3)([(1,2),(2,)])
        sage: s2 == s
        True
        sage: s2.parent()
        Increasing tableaux of size 3 and maximum entry 3
    """
    @staticmethod
    def __classcall_private__(self, t):
        """
        Construct an :class:`IncreasingTableau` from the appropriate parent.

        TESTS::

            sage: t = IncreasingTableau([[1,2],[2]])
            sage: TestSuite(t).run()

            sage: t.parent()
            Increasing tableaux
            sage: t.category()
            Category of elements of Increasing tableaux
            sage: type(t)
            <class 'sage.combinat.tableau.IncreasingTableaux_all_with_category.element_class'>
        """
    def check(self) -> None:
        """
        Check that ``self`` is a valid increasing tableau.

        TESTS::

            sage: IncreasingTableau([[1,2,3],[1]])  # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: the entries of each column of an increasing tableau must be strictly increasing

            sage: IncreasingTableau([[1,2,2]])  # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: the entries in each row of an increasing tableau must be strictly increasing

            sage: IncreasingTableau([[0,1]])  # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: the entries of an increasing tableau must be nonnegative integers
        """
    def descent_set(self):
        """
        Compute the descents of the increasing tableau ``self``
        as defined in [DPS2017]_.

        The number `i` is a *descent* of an increasing tableau if some
        instance of `i + 1` appears in a lower row than some instance
        of `i`.

        .. NOTE::

            This notion is close to the notion of descent for a standard
            tableau but is unrelated to the notion for semistandard tableaux.

        EXAMPLES::

            sage: T = IncreasingTableau([[1,2,4],[3,5,6]])
            sage: T.descent_set()
            [2, 4]
            sage: U = IncreasingTableau([[1,3,4],[2,4,5]])
            sage: U.descent_set()
            [1, 3, 4]
            sage: V = IncreasingTableau([[1,3,4],[3,4,5],[4,5]])
            sage: V.descent_set()
            [3, 4]
        """
    def K_bender_knuth(self, i):
        """
        Return the ``i``-th K-Bender-Knuth operator (as defined in
        [DPS2017]_) applied to ``self``.

        The `i`-th K-Bender-Knuth operator swaps the letters `i` and
        `i + 1` everywhere where doing so would not break increasingness.

        EXAMPLES::

            sage: T = IncreasingTableau([[1,3,4],[2,4,5]])
            sage: T.K_bender_knuth(2)
            [[1, 2, 4], [3, 4, 5]]
            sage: T.K_bender_knuth(3)
            [[1, 3, 4], [2, 4, 5]]
        """
    def K_promotion(self, ceiling=None):
        """
        Return the K-promotion operator from [Pec2014]_ applied to ``self``.

        EXAMPLES::

            sage: T = IncreasingTableau([[1,3,4],[2,4,5]])
            sage: T.K_promotion()
            [[1, 2, 3], [3, 4, 5]]
            sage: T.K_promotion(6)
            [[1, 2, 3], [3, 4, 6]]
            sage: U = IncreasingTableau([[1,3,4],[3,4,5],[5]])
            sage: U.K_promotion()
            [[2, 3, 4], [3, 4, 5], [4]]
        """
    def K_promotion_inverse(self, ceiling=None):
        """
        Return the inverse of K-promotion operator applied to ``self``.

        EXAMPLES::

            sage: T = IncreasingTableau([[1,3,4],[2,4,5]])
            sage: T.K_promotion_inverse()
            [[1, 2, 4], [3, 4, 5]]
            sage: T.K_promotion_inverse(6)
            [[2, 4, 5], [3, 5, 6]]
            sage: U = IncreasingTableau([[1,3,4],[3,4,5],[5]])
            sage: U.K_promotion_inverse()
            [[1, 2, 4], [2, 4, 5], [4]]

        TESTS::

            sage: V = IncreasingTableau([[1,3,4],[3,4,5],[5,6]])
            sage: V == V.K_promotion().K_promotion_inverse()
            True
            sage: V == V.K_promotion_inverse().K_promotion()
            True
        """
    def K_evacuation(self, ceiling=None):
        """
        Return the K-evacuation involution from [TY2009]_ to ``self``.

        EXAMPLES::

            sage: T = IncreasingTableau([[1,3,4],[2,4,5]])
            sage: T.K_evacuation()
            [[1, 2, 4], [2, 3, 5]]
            sage: T.K_evacuation(6)
            [[2, 3, 5], [3, 4, 6]]
            sage: U = IncreasingTableau([[1,3,4],[3,4,5],[5]])
            sage: U.K_evacuation()
            [[1, 2, 3], [2, 3, 5], [3]]

        TESTS::

            sage: V = IncreasingTableau([[1,3,4],[3,4,5],[5,6]])
            sage: V == V.K_evacuation().K_evacuation()
            True
            sage: V.K_promotion().K_evacuation() == V.K_evacuation().K_promotion_inverse()
            True
        """
    def dual_K_evacuation(self, ceiling=None):
        """
        Return the dual K-evacuation involution applied to ``self``.

        EXAMPLES::

            sage: T = IncreasingTableau([[1,3,4],[2,4,5]])
            sage: T.dual_K_evacuation()
            [[1, 2, 4], [2, 3, 5]]
            sage: T.dual_K_evacuation(6)
            [[2, 3, 5], [3, 4, 6]]
            sage: U = IncreasingTableau([[1,3,4],[3,4,5],[5]])
            sage: U.dual_K_evacuation()
            [[1, 2, 3], [2, 3, 5], [3]]

        TESTS::

            sage: V = IncreasingTableau([[1,3,4],[3,4,5],[5,6]])
            sage: V == V.dual_K_evacuation().dual_K_evacuation()
            True
            sage: W = IncreasingTableau([[1,2,4],[2,3,5]])
            sage: W.K_evacuation() == W.dual_K_evacuation()
            True
            sage: X = IncreasingTableau([[1,2,4,7],[3,5,6,8],[5,7,8,10],[7,9,10,11]])
            sage: X.K_evacuation() == X.dual_K_evacuation()
            False
            sage: X.K_promotion().dual_K_evacuation() == X.dual_K_evacuation().K_promotion_inverse()
            True
        """

class Tableaux(UniqueRepresentation, Parent):
    """
    A factory class for the various classes of tableaux.

    INPUT:

    - ``n`` -- (optional) nonnegative integer

    OUTPUT:

    - If ``n`` is specified, the class of tableaux of size ``n``. Otherwise,
      the class of all tableaux.

    A tableau in Sage is a finite list of lists, whose lengths are weakly
    decreasing, or an empty list, representing the empty tableau.  The entries
    of a tableau can be any Sage objects. Because of this, no enumeration
    through the set of Tableaux is possible.

    EXAMPLES::

        sage: T = Tableaux(); T
        Tableaux
        sage: T3 = Tableaux(3); T3
        Tableaux of size 3
        sage: [['a','b']] in T
        True
        sage: [['a','b']] in T3
        False
        sage: t = T3([[1,1,1]]); t
        [[1, 1, 1]]
        sage: t in T
        True
        sage: t.parent()
        Tableaux of size 3
        sage: T([]) # the empty tableau
        []
        sage: T.category()
        Category of sets

    .. SEEALSO::

        - :class:`Tableau`
        - :class:`SemistandardTableaux`
        - :class:`SemistandardTableau`
        - :class:`StandardTableaux`
        - :class:`StandardTableau`

    TESTS::

        sage: TestSuite( Tableaux() ).run()
        sage: TestSuite( Tableaux(5) ).run()
        sage: t = Tableaux(3)([[1,2],[3]])
        sage: t.parent()
        Tableaux of size 3
        sage: Tableaux(t)
        Traceback (most recent call last):
        ...
        ValueError: the argument to Tableaux() must be a nonnegative integer
        sage: Tableaux(3)([[1, 1]])
        Traceback (most recent call last):
        ...
        ValueError: [[1, 1]] is not an element of Tableaux of size 3

        sage: t0 = Tableau([[1]])
        sage: t1 = Tableaux()([[1]])
        sage: t2 = Tableaux()(t1)
        sage: t0 == t1 == t2
        True
        sage: t1 in Tableaux()
        True
        sage: t1 in Tableaux(1)
        True
        sage: t1 in Tableaux(2)
        False

        sage: [[1]] in Tableaux()
        True
        sage: [] in Tableaux(0)
        True

    Check that :issue:`14145` has been fixed::

        sage: 1 in Tableaux()
        False
    """
    @staticmethod
    def __classcall_private__(cls, *args, **kwargs):
        """
        This is a factory class which returns the appropriate parent based on
        arguments.  See the documentation for :class:`Tableaux` for more
        information.

        TESTS::

            sage: Tableaux()
            Tableaux
            sage: Tableaux(3)
            Tableaux of size 3
            sage: Tableaux(n=3)
            Tableaux of size 3
        """
    Element = Tableau
    class options(GlobalOptions):
        '''
        Set the global options for elements of the tableau, skew_tableau,
        and tableau tuple classes. The defaults are for tableau to be
        displayed as a list, latexed as a Young diagram using the English
        convention.

        @OPTIONS@

        .. NOTE::

            Changing the ``convention`` for tableaux also changes the
            ``convention`` for partitions.

        If no parameters are set, then the function returns a copy of the
        options dictionary.

        EXAMPLES::

            sage: T = Tableau([[1,2,3],[4,5]])
            sage: T
            [[1, 2, 3], [4, 5]]
            sage: Tableaux.options.display="array"
            sage: T
              1  2  3
              4  5
            sage: Tableaux.options.convention="french"
            sage: T
              4  5
              1  2  3

        Changing the ``convention`` for tableaux also changes the ``convention``
        for partitions and vice versa::

            sage: P = Partition([3,3,1])
            sage: print(P.ferrers_diagram())
            *
            ***
            ***
            sage: Partitions.options.convention="english"
            sage: print(P.ferrers_diagram())
            ***
            ***
            *
            sage: T
              1  2  3
              4  5

        The ASCII art can also be changed::

            sage: t = Tableau([[1,2,3],[4,5]])
            sage: ascii_art(t)
              1  2  3
              4  5
            sage: Tableaux.options.ascii_art = "table"
            sage: ascii_art(t)
            +---+---+---+
            | 1 | 2 | 3 |
            +---+---+---+
            | 4 | 5 |
            +---+---+
            sage: Tableaux.options.ascii_art = "compact"
            sage: ascii_art(t)
            |1|2|3|
            |4|5|
            sage: Tableaux.options._reset()
        '''
        NAME: str
        module: str
        display: Incomplete
        ascii_art: Incomplete
        latex: Incomplete
        convention: Incomplete
        notation: Incomplete
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: T = sage.combinat.tableau.Tableaux()
            sage: [[1,2],[3,4]] in T
            True
            sage: [[1,2],[3]] in T
            True
            sage: [] in T
            True
            sage: [['a','b']] in T
            True
            sage: Tableau([['a']]) in T
            True

            sage: [1,2,3] in T
            False
            sage: [[1],[1,2]] in T
            False

        Check that :issue:`14145` is fixed::

            sage: 1 in sage.combinat.tableau.Tableaux()
            False
        """

class Tableaux_all(Tableaux):
    def __init__(self) -> None:
        """
        Initialize the class of all tableaux.

        TESTS::

            sage: T = sage.combinat.tableau.Tableaux_all()
            sage: TestSuite(T).run()
        """

class Tableaux_size(Tableaux):
    """
    Tableaux of a fixed size `n`.
    """
    size: Incomplete
    def __init__(self, n) -> None:
        """
        Initialize the class of tableaux of size `n`.

        TESTS::

            sage: T = sage.combinat.tableau.Tableaux_size(3)
            sage: TestSuite(T).run()

            sage: T = sage.combinat.tableau.Tableaux_size(0)
            sage: TestSuite(T).run()
        """
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: T = sage.combinat.tableau.Tableaux_size(3)
            sage: [[2,4], [1]] in T
            True

            sage: [[2,4],[1,3]] in T
            False

        Check that :issue:`14145` is fixed::

            sage: 1 in sage.combinat.tableau.Tableaux_size(3)
            False
        """

class SemistandardTableaux(Tableaux):
    """
    A factory class for the various classes of semistandard tableaux.

    INPUT:

    Keyword arguments:

    - ``size`` -- the size of the tableaux
    - ``shape`` -- the shape of the tableaux
    - ``eval`` -- the weight (also called content or evaluation) of
      the tableaux
    - ``max_entry`` -- a maximum entry for the tableaux.  This can be a
      positive integer or infinity (``oo``). If ``size`` or ``shape`` are
      specified, ``max_entry`` defaults to be ``size`` or the size of
      ``shape``.

    Positional arguments:

    - The first argument is interpreted as either ``size`` or ``shape``
      according to whether it is an integer or a partition
    - The second keyword argument will always be interpreted as ``eval``

    OUTPUT:

    - The appropriate class, after checking basic consistency tests. (For
      example, specifying ``eval`` implies a value for ``max_entry``).

    A semistandard tableau is a tableau whose entries are positive integers,
    which are weakly increasing in rows and strictly increasing down columns.
    Note that Sage uses the English convention for partitions and tableaux;
    the longer rows are displayed on top.

    Classes of semistandard tableaux can be iterated over if and only if there
    is some restriction.

    EXAMPLES::

        sage: SST = SemistandardTableaux([2,1]); SST
        Semistandard tableaux of shape [2, 1] and maximum entry 3
        sage: SST.list()                                                                # needs sage.modules
        [[[1, 1], [2]],
         [[1, 1], [3]],
         [[1, 2], [2]],
         [[1, 2], [3]],
         [[1, 3], [2]],
         [[1, 3], [3]],
         [[2, 2], [3]],
         [[2, 3], [3]]]

        sage: SST = SemistandardTableaux(3); SST
        Semistandard tableaux of size 3 and maximum entry 3
        sage: SST.list()                                                                # needs sage.modules
        [[[1, 1, 1]],
         [[1, 1, 2]],
         [[1, 1, 3]],
         [[1, 2, 2]],
         [[1, 2, 3]],
         [[1, 3, 3]],
         [[2, 2, 2]],
         [[2, 2, 3]],
         [[2, 3, 3]],
         [[3, 3, 3]],
         [[1, 1], [2]],
         [[1, 1], [3]],
         [[1, 2], [2]],
         [[1, 2], [3]],
         [[1, 3], [2]],
         [[1, 3], [3]],
         [[2, 2], [3]],
         [[2, 3], [3]],
         [[1], [2], [3]]]

        sage: SST = SemistandardTableaux(3, max_entry=2); SST
        Semistandard tableaux of size 3 and maximum entry 2
        sage: SST.list()                                                                # needs sage.modules
        [[[1, 1, 1]],
         [[1, 1, 2]],
         [[1, 2, 2]],
         [[2, 2, 2]],
         [[1, 1], [2]],
         [[1, 2], [2]]]

        sage: SST = SemistandardTableaux(3, max_entry=oo); SST
        Semistandard tableaux of size 3
        sage: SST[123]                                                                  # needs sage.modules
        [[3, 4], [6]]

        sage: SemistandardTableaux(max_entry=2)[11]                                     # needs sage.modules
        [[1, 1], [2]]

        sage: SemistandardTableaux()[0]                                                 # needs sage.modules
        []

    .. SEEALSO::

        - :class:`Tableaux`
        - :class:`Tableau`
        - :class:`SemistandardTableau`
        - :class:`StandardTableaux`
        - :class:`StandardTableau`
    """
    @staticmethod
    def __classcall_private__(cls, *args, **kwargs):
        """
        This is a factory class which returns the appropriate parent based on
        arguments.  See the documentation for :class:`SemistandardTableaux`
        for more information.

        TESTS::

            sage: SemistandardTableaux()
            Semistandard tableaux
            sage: SemistandardTableaux(3)
            Semistandard tableaux of size 3 and maximum entry 3
            sage: SemistandardTableaux(size=3)
            Semistandard tableaux of size 3 and maximum entry 3
            sage: SemistandardTableaux(0)
            Semistandard tableaux of size 0 and maximum entry 0
            sage: SemistandardTableaux([2,1])
            Semistandard tableaux of shape [2, 1] and maximum entry 3
            sage: SemistandardTableaux(shape=[2,1])
            Semistandard tableaux of shape [2, 1] and maximum entry 3
            sage: SemistandardTableaux([])
            Semistandard tableaux of shape [] and maximum entry 0
            sage: SemistandardTableaux(eval=[2,1])
            Semistandard tableaux of size 3 and weight [2, 1]
            sage: SemistandardTableaux(max_entry=3)
            Semistandard tableaux with maximum entry 3
            sage: SemistandardTableaux(3, [2,1])
            Semistandard tableaux of size 3 and weight [2, 1]
            sage: SemistandardTableaux(3, shape=[2,1])
            Semistandard tableaux of shape [2, 1] and maximum entry 3
            sage: SemistandardTableaux(3, [2,1], shape=[2,1])
            Semistandard tableaux of shape [2, 1] and weight [2, 1]
            sage: SemistandardTableaux(3, max_entry=4)
            Semistandard tableaux of size 3 and maximum entry 4
            sage: SemistandardTableaux(3, max_entry=oo)
            Semistandard tableaux of size 3
            sage: SemistandardTableaux([2, 1], max_entry=oo)
            Semistandard tableaux of shape [2, 1]
            sage: SemistandardTableaux([2, 1], [2, 1])
            Semistandard tableaux of shape [2, 1] and weight [2, 1]
            sage: mu = Partition([2,1]); SemistandardTableaux(mu, mu)
            Semistandard tableaux of shape [2, 1] and weight [2, 1]
            sage: SemistandardTableaux(3, [2, 1], max_entry=2)
            Semistandard tableaux of size 3 and weight [2, 1]

            sage: SemistandardTableaux(3, shape=[2])
            Traceback (most recent call last):
            ...
            ValueError: size and shape are different sizes

            sage: SemistandardTableaux(3, [2])
            Traceback (most recent call last):
            ...
            ValueError: size and eval are different sizes

            sage: SemistandardTableaux([2],[3])
            Traceback (most recent call last):
            ...
            ValueError: shape and eval are different sizes

            sage: SemistandardTableaux(2,[2], max_entry=4)
            Traceback (most recent call last):
            ...
            ValueError: the maximum entry must match the weight

            sage: SemistandardTableaux(eval=[2], max_entry=oo)
            Traceback (most recent call last):
            ...
            ValueError: the maximum entry must match the weight

            sage: # needs sage.modules
            sage: SemistandardTableaux([[1]])
            Traceback (most recent call last):
            ...
            ValueError: shape must be a (skew) partition
        """
    Element = SemistandardTableau
    max_entry: Incomplete
    def __init__(self, **kwds) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: S = SemistandardTableaux()
            sage: TestSuite(S).run()                                                    # needs sage.modules
        """
    def __getitem__(self, r):
        """
        The default implementation of ``__getitem__`` for enumerated sets
        does not allow slices so we override it.

        EXAMPLES::

            sage: StandardTableaux([4,3,3,2])[10:20]     # indirect doctest
            [[[1, 3, 9, 12], [2, 5, 10], [4, 6, 11], [7, 8]],
             [[1, 2, 9, 12], [3, 5, 10], [4, 6, 11], [7, 8]],
             [[1, 3, 9, 12], [2, 4, 10], [5, 6, 11], [7, 8]],
             [[1, 2, 9, 12], [3, 4, 10], [5, 6, 11], [7, 8]],
             [[1, 5, 8, 12], [2, 6, 10], [3, 7, 11], [4, 9]],
             [[1, 4, 8, 12], [2, 6, 10], [3, 7, 11], [5, 9]],
             [[1, 3, 8, 12], [2, 6, 10], [4, 7, 11], [5, 9]],
             [[1, 2, 8, 12], [3, 6, 10], [4, 7, 11], [5, 9]],
             [[1, 4, 8, 12], [2, 5, 10], [3, 7, 11], [6, 9]],
             [[1, 3, 8, 12], [2, 5, 10], [4, 7, 11], [6, 9]]]

            sage: SemistandardTableaux(size=2, max_entry=oo)[5]                         # needs sage.modules
            [[2, 3]]

            sage: SemistandardTableaux([2,1], max_entry=oo)[3]                          # needs sage.modules
            [[1, 2], [3]]

            sage: SemistandardTableaux(3, max_entry=2)[0:5]    # indirect doctest       # needs sage.modules
            [[[1, 1, 1]],
            [[1, 1, 2]],
            [[1, 2, 2]],
            [[2, 2, 2]],
            [[1, 1], [2]]]

            sage: SemistandardTableaux([2,2], [2, 1, 1])[0]    # indirect doctest       # needs sage.modules
            [[1, 1], [2, 3]]

            sage: SemistandardTableaux([1,1,1], max_entry=4)[0:4]                       # needs sage.modules
            [[[1], [2], [3]],
             [[1], [2], [4]],
             [[1], [3], [4]],
             [[2], [3], [4]]]

            sage: SemistandardTableaux(3, [2,1])[1]    # indirect doctest               # needs sage.modules
            [[1, 1], [2]]

            sage: StandardTableaux(3)[:]  # indirect doctest                            # needs sage.modules
            [[[1, 2, 3]], [[1, 3], [2]], [[1, 2], [3]], [[1], [2], [3]]]

            sage: StandardTableaux([2,2])[1]   # indirect doctest                       # needs sage.modules
            [[1, 2], [3, 4]]

        TESTS::

            sage: SemistandardTableaux()[5]                                             # needs sage.modules
            [[1], [2]]

            sage: SemistandardTableaux(max_entry=2)[5]                                  # needs sage.modules
            [[2, 2]]

            sage: SemistandardTableaux()[:]                                             # needs sage.modules
            Traceback (most recent call last):
            ...
            ValueError: infinite set

            sage: SemistandardTableaux(size=2, max_entry=oo)[:]                         # needs sage.modules
            Traceback (most recent call last):
            ...
            ValueError: infinite set
        """
    def __contains__(self, t) -> bool:
        """
        Return ``True`` if ``t`` can be interpreted as a
        :class:`SemistandardTableau`.

        TESTS::

            sage: T = sage.combinat.tableau.SemistandardTableaux_all()
            sage: [[1,2],[2]] in T
            True
            sage: [] in T
            True
            sage: Tableau([[1]]) in T
            True
            sage: StandardTableau([[1]]) in T
            True

            sage: [[1,2],[1]] in T
            False
            sage: [[1,1],[5]] in T
            True
            sage: [[1,3,2]] in T
            False

        Check that :issue:`14145` is fixed::

            sage: 1 in sage.combinat.tableau.SemistandardTableaux()
            False
        """

class SemistandardTableaux_all(SemistandardTableaux, DisjointUnionEnumeratedSets):
    """
    All semistandard tableaux.
    """
    max_entry: Incomplete
    def __init__(self, max_entry=None) -> None:
        """
        Initialize the class of all semistandard tableaux.

        .. WARNING::

            Input is not checked; please use :class:`SemistandardTableaux` to
            ensure the options are properly parsed.

        TESTS::

            sage: T = sage.combinat.tableau.SemistandardTableaux_all()
            sage: TestSuite(T).run()                                                    # needs sage.modules

            sage: T = sage.combinat.tableau.SemistandardTableaux_all(max_entry=3)
            sage: TestSuite(T).run()            # long time                             # needs sage.modules
        """
    def list(self) -> None:
        """
        TESTS::

            sage: SemistandardTableaux().list()
            Traceback (most recent call last):
            ...
            NotImplementedError
        """

class SemistandardTableaux_size_inf(SemistandardTableaux):
    """
    Semistandard tableaux of fixed size `n` with no maximum entry.
    """
    size: Incomplete
    def __init__(self, n) -> None:
        """
        Initialize the class of semistandard tableaux of size ``n`` with no
        maximum entry.

        .. WARNING::

            Input is not checked; please use :class:`SemistandardTableaux` to
            ensure the options are properly parsed.

        TESTS::

            sage: T = sage.combinat.tableau.SemistandardTableaux_size_inf(3)
            sage: TestSuite(T).run()                                                    # needs sage.modules
        """
    def __contains__(self, t) -> bool:
        """
        Return ``True`` if ``t`` can be interpreted as an element of this
        class.

        TESTS::

            sage: T = SemistandardTableaux(3, max_entry=oo)
            sage: [[1,2],[5]] in T
            True
            sage: StandardTableau([[1, 2], [3]]) in T
            True

            sage: [] in T
            False
            sage: Tableau([[1]]) in T
            False

        Check that :issue:`14145` is fixed::

            sage: 1 in SemistandardTableaux(3, max_entry=oo)
            False
        """
    def __iter__(self):
        """
        EXAMPLES::

            sage: sst = SemistandardTableaux(3, max_entry=oo)
            sage: [sst[t] for t in range(5)]                                            # needs sage.modules
            [[[1, 1, 1]],
             [[1, 1, 2]],
             [[1, 2, 2]],
             [[2, 2, 2]],
             [[1, 1], [2]]]
            sage: sst[1000]                                                             # needs sage.modules
            [[2, 12], [7]]
            sage: sst[0].parent() is sst                                                # needs sage.modules
            True
        """
    def list(self) -> None:
        """
        TESTS::

            sage: SemistandardTableaux(3, max_entry=oo).list()
            Traceback (most recent call last):
            ...
            NotImplementedError
        """

class SemistandardTableaux_shape_inf(SemistandardTableaux):
    """
    Semistandard tableaux of fixed shape `p` and no maximum entry.
    """
    shape: Incomplete
    def __init__(self, p) -> None:
        """
        Initialize the class of semistandard tableaux of shape ``p`` and no
        maximum entry.

        .. WARNING::

            Input is not checked; please use :class:`SemistandardTableaux` to
            ensure the options are properly parsed.

        TESTS::

            sage: SST = SemistandardTableaux([2,1], max_entry=oo)
            sage: type(SST)
            <class 'sage.combinat.tableau.SemistandardTableaux_shape_inf_with_category'>
            sage: TestSuite(SST).run()                                                  # needs sage.modules
        """
    def __contains__(self, x) -> bool:
        """
        EXAMPLES::

            sage: SST = SemistandardTableaux([2,1], max_entry=oo)
            sage: [[13, 67], [1467]] in SST
            True
            sage: SST = SemistandardTableaux([3,1], max_entry=oo)
            sage: [[13, 67], [1467]] in SST
            False

        Check that :issue:`14145` is fixed::

            sage: SST = SemistandardTableaux([3,1], max_entry=oo)
            sage: 1 in SST
            False
        """
    def __iter__(self):
        """
        An iterator for the semistandard partitions of shape ``p`` and no
        maximum entry. Iterates through with maximum entry as order.

        EXAMPLES::

            sage: SST = SemistandardTableaux([3, 1], max_entry=oo)
            sage: SST[1000]                                                             # needs sage.modules
            [[1, 1, 10], [6]]
            sage: [ SST[t] for t in range(5) ]                                          # needs sage.modules
            [[[1, 1, 1], [2]],
             [[1, 1, 2], [2]],
             [[1, 2, 2], [2]],
             [[1, 1, 1], [3]],
             [[1, 1, 2], [3]]]
            sage: SST[0].parent() is SST                                                # needs sage.modules
            True
        """

class SemistandardTableaux_size(SemistandardTableaux):
    """
    Semistandard tableaux of fixed size `n`.
    """
    size: Incomplete
    def __init__(self, n, max_entry=None) -> None:
        """
        Initialize the class of semistandard tableaux of size `n`.

        .. WARNING::

            Input is not checked; please use :class:`SemistandardTableaux`
            to ensure the options are properly parsed.

        TESTS::

            sage: SST = SemistandardTableaux(3); SST
            Semistandard tableaux of size 3 and maximum entry 3
            sage: type(SST)
            <class 'sage.combinat.tableau.SemistandardTableaux_size_with_category'>
            sage: TestSuite(SST).run()                                                  # needs sage.modules

            sage: SST = SemistandardTableaux(3, max_entry=6)
            sage: type(SST)
            <class 'sage.combinat.tableau.SemistandardTableaux_size_with_category'>
            sage: TestSuite(SST).run()                                                  # needs sage.modules
        """
    def __contains__(self, x) -> bool:
        """
        EXAMPLES::

            sage: [[1,2],[3,3]] in SemistandardTableaux(3)
            False
            sage: [[1,2],[3,3]] in SemistandardTableaux(4)
            True
            sage: [[1,2],[3,3]] in SemistandardTableaux(4, max_entry=2)
            False
            sage: SST = SemistandardTableaux(4)
            sage: all(sst in SST for sst in SST)                                        # needs sage.modules
            True

        Check that :issue:`14145` is fixed::

            sage: SST = SemistandardTableaux(4)
            sage: 1 in SST
            False
        """
    def random_element(self):
        """
        Generate a random :class:`SemistandardTableau` with uniform probability.

        The RSK algorithm gives a bijection between symmetric `k\\times k` matrices
        of nonnegative integers that sum to `n` and semistandard tableaux with size `n`
        and maximum entry `k`.

        The number of `k\\times k` symmetric matrices of nonnegative integers
        having sum of elements on the diagonal `i` and sum of elements above
        the diagonal `j` is `\\binom{k + i - 1}{k - 1}\\binom{\\binom{k}{2} + j - 1}{\\binom{k}{2} - 1}`.
        We first choose the sum of the elements on the diagonal randomly weighted by the
        number of matrices having that trace.  We then create random integer vectors
        of length `k` having that sum and use them to generate a `k\\times k` diagonal matrix.
        Then we take a random integer vector of length `\\binom{k}{2}` summing to half the
        remainder and distribute it symmetrically to the remainder of the matrix.

        Applying RSK to the random symmetric matrix gives us a pair of identical
        :class:`SemistandardTableau` of which we choose the first.

        EXAMPLES::

            sage: SemistandardTableaux(6).random_element()  # random                    # needs sage.modules
            [[1, 1, 2], [3, 5, 5]]
            sage: SemistandardTableaux(6, max_entry=7).random_element()  # random       # needs sage.modules
            [[2, 4, 4, 6, 6, 6]]
        """
    def cardinality(self):
        """
        Return the cardinality of ``self``.

        EXAMPLES::

            sage: SemistandardTableaux(3).cardinality()
            19
            sage: SemistandardTableaux(4).cardinality()
            116
            sage: SemistandardTableaux(4, max_entry=2).cardinality()
            9
            sage: SemistandardTableaux(4, max_entry=10).cardinality()
            4225
            sage: ns = list(range(1, 6))
            sage: ssts = [ SemistandardTableaux(n) for n in ns ]
            sage: all(sst.cardinality() == len(sst.list()) for sst in ssts)             # needs sage.modules
            True
        """
    def __iter__(self):
        """
        EXAMPLES::

            sage: [ t for t in SemistandardTableaux(2) ]                                # needs sage.modules
            [[[1, 1]], [[1, 2]], [[2, 2]], [[1], [2]]]
            sage: [ t for t in SemistandardTableaux(3) ]                                # needs sage.modules
            [[[1, 1, 1]],
             [[1, 1, 2]],
             [[1, 1, 3]],
             [[1, 2, 2]],
             [[1, 2, 3]],
             [[1, 3, 3]],
             [[2, 2, 2]],
             [[2, 2, 3]],
             [[2, 3, 3]],
             [[3, 3, 3]],
             [[1, 1], [2]],
             [[1, 1], [3]],
             [[1, 2], [2]],
             [[1, 2], [3]],
             [[1, 3], [2]],
             [[1, 3], [3]],
             [[2, 2], [3]],
             [[2, 3], [3]],
             [[1], [2], [3]]]

            sage: [ t for t in SemistandardTableaux(3, max_entry=2) ]                   # needs sage.modules
            [[[1, 1, 1]],
             [[1, 1, 2]],
             [[1, 2, 2]],
             [[2, 2, 2]],
             [[1, 1], [2]],
             [[1, 2], [2]]]

            sage: sst = SemistandardTableaux(3)
            sage: sst[0].parent() is sst                                                # needs sage.modules
            True
        """

class SemistandardTableaux_shape(SemistandardTableaux):
    """
    Semistandard tableaux of fixed shape `p` with a given max entry.

    A semistandard tableau with max entry `i` is required to have all
    its entries less or equal to `i`. It is not required to actually
    contain an entry `i`.

    INPUT:

    - ``p`` -- a partition
    - ``max_entry`` -- the max entry; defaults to the size of `p`
    """
    shape: Incomplete
    def __init__(self, p, max_entry=None) -> None:
        """
        Initialize the class of semistandard tableaux of shape `p`, with a
        given ``max_entry``.

        .. WARNING::

            Input is not checked; please use :class:`SemistandardTableaux` to
            ensure the options are properly parsed.

        TESTS::

            sage: SST = SemistandardTableaux([2,1])
            sage: TestSuite(SST).run()                                                  # needs sage.modules

            sage: SST = SemistandardTableaux([2,1], max_entry=5)
            sage: TestSuite(SST).run()                                                  # needs sage.modules
        """
    def __iter__(self):
        """
        An iterator for the semistandard tableaux of the specified shape
        with the specified max entry.

        EXAMPLES::

            sage: [ t for t in SemistandardTableaux([3]) ]                              # needs sage.modules
            [[[1, 1, 1]],
             [[1, 1, 2]],
             [[1, 1, 3]],
             [[1, 2, 2]],
             [[1, 2, 3]],
             [[1, 3, 3]],
             [[2, 2, 2]],
             [[2, 2, 3]],
             [[2, 3, 3]],
             [[3, 3, 3]]]
            sage: [ t for t in SemistandardTableaux([2,1]) ]                            # needs sage.modules
            [[[1, 1], [2]],
             [[1, 1], [3]],
             [[1, 2], [2]],
             [[1, 2], [3]],
             [[1, 3], [2]],
             [[1, 3], [3]],
             [[2, 2], [3]],
             [[2, 3], [3]]]
            sage: [ t for t in SemistandardTableaux([1,1,1]) ]                          # needs sage.modules
            [[[1], [2], [3]]]

            sage: [ t for t in SemistandardTableaux([1,1,1], max_entry=4) ]             # needs sage.modules
            [[[1], [2], [3]],
             [[1], [2], [4]],
             [[1], [3], [4]],
             [[2], [3], [4]]]

            sage: sst = SemistandardTableaux([3])
            sage: sst[0].parent() is sst                                                # needs sage.modules
            True
        """
    def __contains__(self, x) -> bool:
        """
        EXAMPLES::

            sage: SST = SemistandardTableaux([2,1])
            sage: all(sst in SST for sst in SST)                                        # needs sage.modules
            True
            sage: len([x for x in SemistandardTableaux(3) if x in SST])                 # needs sage.modules
            8
            sage: SST.cardinality()
            8

            sage: SST = SemistandardTableaux([2,1], max_entry=4)
            sage: all(sst in SST for sst in SST)                                        # needs sage.modules
            True
            sage: SST.cardinality()
            20
        """
    def random_element(self):
        """
        Return a uniformly distributed random tableau of the given ``shape`` and ``max_entry``.

        Uses the algorithm from [Kra1999]_ based on the Novelli-Pak-Stoyanovskii bijection
           http://www.sciencedirect.com/science/article/pii/0012365X9290368P

        EXAMPLES::

            sage: S = SemistandardTableaux([2, 2, 1, 1])
            sage: S.random_element() in S
            True
            sage: S = SemistandardTableaux([2, 2, 1, 1], max_entry=7)
            sage: S.random_element() in S
            True
        """
    def cardinality(self, algorithm: str = 'hook'):
        """
        Return the cardinality of ``self``.

        INPUT:

        - ``algorithm`` -- (default: ``'hook'``) any one of the following:

          - ``'hook'`` -- use Stanley's hook length formula

          - ``'sum'`` -- sum over the compositions of ``max_entry`` the
            number of semistandard tableau with ``shape`` and given
            weight vector

        This is computed using *Stanley's hook length formula*:

        .. MATH::

           f_{\\lambda} = \\prod_{u\\in\\lambda} \\frac{n+c(u)}{h(u)}.

        where `n` is the ``max_entry``, `c(u)` is the content of `u`,
        and `h(u)` is the hook length of `u`.
        See [Sta-EC2]_ Corollary 7.21.4.

        EXAMPLES::

            sage: SemistandardTableaux([2,1]).cardinality()
            8
            sage: SemistandardTableaux([2,2,1]).cardinality()
            75
            sage: SymmetricFunctions(QQ).schur()([2,2,1]).expand(5)(1,1,1,1,1)  # cross check       # needs sage.modules
            75
            sage: SemistandardTableaux([5]).cardinality()
            126
            sage: SemistandardTableaux([3,2,1]).cardinality()
            896
            sage: SemistandardTableaux([3,2,1], max_entry=7).cardinality()
            2352
            sage: SemistandardTableaux([6,5,4,3,2,1], max_entry=30).cardinality()
            208361017592001331200
            sage: ssts = [SemistandardTableaux(p, max_entry=6) for p in Partitions(5)]
            sage: all(sst.cardinality() == sst.cardinality(algorithm='sum')             # needs sage.modules
            ....:     for sst in ssts)
            True
        """

class SemistandardTableaux_shape_weight(SemistandardTableaux_shape):
    """
    Semistandard tableaux of fixed shape `p` and weight `\\mu`.
    """
    weight: Incomplete
    def __init__(self, p, mu) -> None:
        """
        Initialize the class of all semistandard tableaux of shape ``p`` and
        weight ``mu``.

        .. WARNING::

            Input is not checked; please use :class:`SemistandardTableaux` to
            ensure the options are properly parsed.

        TESTS::

            sage: SST = SemistandardTableaux([2,1], [2,1])
            sage: TestSuite(SST).run()                                                  # needs sage.modules
        """
    def __contains__(self, x) -> bool:
        """
        EXAMPLES::

            sage: SST = SemistandardTableaux([2,1], [2,1])
            sage: all(sst in SST for sst in SST)                                        # needs sage.modules
            True
            sage: len([x for x in SemistandardTableaux(3) if x in SST])                 # needs sage.modules
            1
            sage: SST.cardinality()                                                     # needs sage.modules
            1
        """
    def cardinality(self):
        """
        Return the number of semistandard tableaux of the given shape and
        weight, as computed by ``kostka_number`` function of ``symmetrica``.

        EXAMPLES::

            sage: # needs sage.modules
            sage: SemistandardTableaux([2,2], [2, 1, 1]).cardinality()
            1
            sage: SemistandardTableaux([2,2,2], [2, 2, 1,1]).cardinality()
            1
            sage: SemistandardTableaux([2,2,2], [2, 2, 2]).cardinality()
            1
            sage: SemistandardTableaux([3,2,1], [2, 2, 2]).cardinality()
            2
        """
    def __iter__(self):
        """
        TESTS::

            sage: sst = SemistandardTableaux([3,1],[2,1,1])
            sage: [sst[i] for i in range(2)]                                            # needs sage.modules
            [[[1, 1, 2], [3]], [[1, 1, 3], [2]]]
            sage: sst[0].parent() is sst                                                # needs sage.modules
            True
        """
    def list(self):
        """
        Return a list of all semistandard tableaux in ``self`` generated
        by symmetrica.

        EXAMPLES::

            sage: # needs sage.modules
            sage: SemistandardTableaux([2,2], [2, 1, 1]).list()
            [[[1, 1], [2, 3]]]
            sage: SemistandardTableaux([2,2,2], [2, 2, 1,1]).list()
            [[[1, 1], [2, 2], [3, 4]]]
            sage: SemistandardTableaux([2,2,2], [2, 2, 2]).list()
            [[[1, 1], [2, 2], [3, 3]]]
            sage: SemistandardTableaux([3,2,1], [2, 2, 2]).list()
            [[[1, 1, 2], [2, 3], [3]], [[1, 1, 3], [2, 2], [3]]]
        """

class SemistandardTableaux_size_weight(SemistandardTableaux):
    """
    Semistandard tableaux of fixed size `n` and weight `\\mu`.
    """
    size: Incomplete
    weight: Incomplete
    def __init__(self, n, mu) -> None:
        """
        Initialize the class of semistandard tableaux of size ``n`` and
        weight ``mu``.

        .. WARNING::

            Input is not checked; please use :class:`SemistandardTableaux` to
            ensure the options are properly parsed.

        TESTS::

            sage: SST = SemistandardTableaux(3, [2,1])
            sage: TestSuite(SST).run()                                                  # needs sage.modules
        """
    def __iter__(self):
        """
        EXAMPLES::

            sage: # needs sage.modules
            sage: [ t for t in SemistandardTableaux(3, [2,1]) ]
            [[[1, 1, 2]], [[1, 1], [2]]]
            sage: [ t for t in SemistandardTableaux(4, [2,2]) ]
            [[[1, 1, 2, 2]], [[1, 1, 2], [2]], [[1, 1], [2, 2]]]
            sage: sst = SemistandardTableaux(4, [2,2])
            sage: sst[0].parent() is sst
            True
        """
    def cardinality(self):
        """
        Return the cardinality of ``self``.

        EXAMPLES::

            sage: SemistandardTableaux(3, [2,1]).cardinality()                          # needs sage.modules
            2
            sage: SemistandardTableaux(4, [2,2]).cardinality()                          # needs sage.modules
            3
        """
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: SST = SemistandardTableaux(6, [2,2,2])
            sage: all(sst in SST for sst in SST)                                        # needs sage.modules
            True
            sage: all(sst in SST for sst in SemistandardTableaux([3,2,1],[2,2,2]))      # needs sage.modules
            True
        """

class RowStandardTableaux(Tableaux):
    """
    A factory for the various classes of row standard tableaux.

    INPUT:

    - either a nonnegative integer (possibly specified with the keyword
      ``n``) or a partition

    OUTPUT: with no argument, the class of all standard tableaux

    - with a nonnegative integer argument, ``n``, the class of all standard
      tableaux of size ``n``

    - with a partition argument, the class of all standard tableaux of that
      shape

    A row standard tableau is a tableau that contains each of the
    entries from `1` to `n` exactly once and is increasing along rows.

    All classes of row standard tableaux are iterable.

    EXAMPLES::

        sage: ST = RowStandardTableaux(3); ST
        Row standard tableaux of size 3
        sage: ST.first()                                                                # needs sage.graphs
        [[1, 2, 3]]
        sage: ST.last()                                                                 # needs sage.graphs sage.modules
        [[3], [1], [2]]
        sage: ST.cardinality()                                                          # needs sage.graphs sage.modules
        10
        sage: ST.list()                                                                 # needs sage.graphs sage.modules
        [[[1, 2, 3]],
         [[2, 3], [1]],
         [[1, 2], [3]],
         [[1, 3], [2]],
         [[3], [2], [1]],
         [[2], [3], [1]],
         [[1], [3], [2]],
         [[1], [2], [3]],
         [[2], [1], [3]],
         [[3], [1], [2]]]

    .. SEEALSO::

        - :class:`Tableaux`
        - :class:`Tableau`
        - :class:`SemistandardTableaux`
        - :class:`SemistandardTableau`
        - :class:`RowStandardTableau`
        - :class:`StandardSkewTableaux`

    TESTS::

        sage: RowStandardTableaux()([])
        []
        sage: ST = RowStandardTableaux([2,2]); ST
        Row standard tableaux of shape [2, 2]
        sage: ST.first()                                                                # needs sage.graphs
        [[2, 4], [1, 3]]
        sage: ST.last()                                                                 # needs sage.graphs sage.modules
        [[2, 3], [1, 4]]
        sage: ST.cardinality()                                                          # needs sage.graphs sage.modules
        6
        sage: ST.list()                                                                 # needs sage.graphs sage.modules
        [[[2, 4], [1, 3]],
         [[3, 4], [1, 2]],
         [[1, 4], [2, 3]],
         [[1, 3], [2, 4]],
         [[1, 2], [3, 4]],
         [[2, 3], [1, 4]]]
        sage: RowStandardTableau([[3,4,5],[1,2]]).residue_sequence(3).standard_tableaux()
        Standard tableaux with 3-residue sequence (2,0,0,1,2) and multicharge (0)
    """
    @staticmethod
    def __classcall_private__(cls, *args, **kwargs):
        """
        This is a factory class which returns the appropriate parent based on
        arguments.  See the documentation for :class:`RowStandardTableaux` for
        more information.

        TESTS::

            sage: RowStandardTableaux()
            Row standard tableaux
            sage: RowStandardTableaux(3)
            Row standard tableaux of size 3
            sage: RowStandardTableaux([2,1])
            Row standard tableaux of shape [2, 1]
            sage: RowStandardTableaux(0)
            Row standard tableaux of size 0

            sage: RowStandardTableaux(-1)
            Traceback (most recent call last):
            ...
            ValueError: the argument must be a nonnegative integer or a partition
            sage: RowStandardTableaux([[1]])
            Traceback (most recent call last):
            ...
            ValueError: the argument must be a nonnegative integer or a partition
        """
    Element = RowStandardTableau
    def __contains__(self, x) -> bool:
        """
        EXAMPLES::

            sage: [[1,1],[2,3]] in RowStandardTableaux()
            False
            sage: [[1,2],[3,4]] in RowStandardTableaux()
            True
            sage: [[1,3],[2,4]] in RowStandardTableaux()
            True
            sage: [[1,3],[2,5]] in RowStandardTableaux()
            False
            sage: [] in RowStandardTableaux()
            True

        Check that integers are not contained in ``self``
        (see :issue:`14145`)::

            sage: 1 in RowStandardTableaux()
            False
        """

class RowStandardTableaux_all(RowStandardTableaux, DisjointUnionEnumeratedSets):
    """
    All row standard tableaux.
    """
    def __init__(self) -> None:
        """
        Initialize the class of all standard tableaux.

        .. WARNING::

            Input is not checked; please use :class:`RowStandardTableaux` to
            ensure the options are properly parsed.

        TESTS::

            sage: ST = RowStandardTableaux()
            sage: TestSuite(ST).run()                                                   # needs sage.graphs
        """

class RowStandardTableaux_size(RowStandardTableaux, DisjointUnionEnumeratedSets):
    """
    Row standard tableaux of fixed size `n`.

    EXAMPLES::

        sage: [t for t in RowStandardTableaux(1)]                                       # needs sage.graphs
        [[[1]]]
        sage: [t for t in RowStandardTableaux(2)]                                       # needs sage.graphs
        [[[1, 2]], [[2], [1]], [[1], [2]]]
        sage: list(RowStandardTableaux(3))                                              # needs sage.graphs
        [[[1, 2, 3]],
         [[2, 3], [1]],
         [[1, 2], [3]],
         [[1, 3], [2]],
         [[3], [2], [1]],
         [[2], [3], [1]],
         [[1], [3], [2]],
         [[1], [2], [3]],
         [[2], [1], [3]],
         [[3], [1], [2]]]

    TESTS::

        sage: TestSuite(RowStandardTableaux(4)).run()                                   # needs sage.graphs

        sage: RowStandardTableaux(3).cardinality()                                      # needs sage.libs.flint
        10
        sage: ns = [1,2,3,4,5,6]
        sage: sts = [RowStandardTableaux(n) for n in ns]
        sage: all(st.cardinality() == len(st.list()) for st in sts)                     # needs sage.graphs
        True
        sage: RowStandardTableaux(40).cardinality()  # not tested, too long
        2063837185739279909309355007659204891024472174278
    """
    def __init__(self, n) -> None:
        """
        Initialize the class of all row standard tableaux of size ``n``.

        .. WARNING::

            Input is not checked; please use :class:`RowStandardTableaux` to
            ensure the options are properly parsed.

        TESTS::

            sage: TestSuite(RowStandardTableaux(0)).run()                               # needs sage.graphs
            sage: TestSuite(RowStandardTableaux(3)).run()                               # needs sage.graphs
        """
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: ST3 = RowStandardTableaux(3)
            sage: all(st in ST3 for st in ST3)                                          # needs sage.graphs
            True
            sage: ST4 = RowStandardTableaux(4)
            sage: [x for x in ST4 if x in ST3]                                          # needs sage.graphs
            []

        Check that :issue:`14145` is fixed::

            sage: 1 in RowStandardTableaux(4)
            False
        """

class RowStandardTableaux_shape(RowStandardTableaux):
    """
    Row Standard tableaux of a fixed shape `p`.
    """
    shape: Incomplete
    def __init__(self, p) -> None:
        """
        Initialize the class of all row standard tableaux of a given shape.

        .. WARNING::

            Input is not checked; please use :class:`RowStandardTableaux` to
            ensure the options are properly parsed.

        TESTS::

            sage: TestSuite( RowStandardTableaux([2,1,1]) ).run()                       # needs sage.graphs
        """
    def __contains__(self, x) -> bool:
        """
        EXAMPLES::

            sage: ST = RowStandardTableaux([2,1,1])
            sage: all(st in ST for st in ST)                                            # needs sage.graphs
            True
            sage: len([x for x in RowStandardTableaux(4) if x in ST])                   # needs sage.graphs
            12
            sage: ST.cardinality()
            12
        """
    def __iter__(self):
        """
        An iterator for the row standard Young tableaux associated to the
        shape `p` of ``self``.

        EXAMPLES::

            sage: [t for t in RowStandardTableaux([2,2])]                               # needs sage.graphs
            [[[2, 4], [1, 3]],
             [[3, 4], [1, 2]],
             [[1, 4], [2, 3]],
             [[1, 3], [2, 4]],
             [[1, 2], [3, 4]],
             [[2, 3], [1, 4]]]
            sage: [t for t in RowStandardTableaux([3,2])]                               # needs sage.graphs
            [[[2, 4, 5], [1, 3]],
             [[3, 4, 5], [1, 2]],
             [[1, 4, 5], [2, 3]],
             [[1, 3, 5], [2, 4]],
             [[1, 2, 5], [3, 4]],
             [[1, 2, 3], [4, 5]],
             [[1, 2, 4], [3, 5]],
             [[1, 3, 4], [2, 5]],
             [[2, 3, 4], [1, 5]],
             [[2, 3, 5], [1, 4]]]
            sage: st = RowStandardTableaux([2,1])
            sage: st[0].parent() is st                                                  # needs sage.graphs
            True
        """
    def cardinality(self):
        """
        Return the number of row standard tableaux of this shape.

        This is just the index of the corresponding Young subgroup in
        the full symmetric group.

        EXAMPLES::

            sage: RowStandardTableaux([3,2,1]).cardinality()
            60
            sage: RowStandardTableaux([2,2]).cardinality()
            6
            sage: RowStandardTableaux([5]).cardinality()
            1
            sage: RowStandardTableaux([6,5,5,3]).cardinality()
            1955457504
            sage: RowStandardTableaux([]).cardinality()
            1
        """

class StandardTableaux(SemistandardTableaux):
    """
    A factory for the various classes of standard tableaux.

    INPUT:

    - Either a nonnegative integer (possibly specified with the keyword ``n``)
      or a partition.

    OUTPUT: with no argument, the class of all standard tableaux

    - With a nonnegative integer argument, ``n``, the class of all standard
      tableaux of size ``n``

    - With a partition argument, the class of all standard tableaux of that
      shape.

    A standard tableau is a semistandard tableaux which contains each of the
    entries from 1 to ``n`` exactly once.

    All classes of standard tableaux are iterable.

    EXAMPLES::

        sage: ST = StandardTableaux(3); ST
        Standard tableaux of size 3
        sage: ST.first()
        [[1, 2, 3]]
        sage: ST.last()
        [[1], [2], [3]]
        sage: ST.cardinality()
        4
        sage: ST.list()
        [[[1, 2, 3]], [[1, 3], [2]], [[1, 2], [3]], [[1], [2], [3]]]

    .. SEEALSO::

        - :class:`Tableaux`
        - :class:`Tableau`
        - :class:`SemistandardTableaux`
        - :class:`SemistandardTableau`
        - :class:`StandardTableau`
        - :class:`StandardSkewTableaux`

    TESTS::

        sage: StandardTableaux()([])
        []
        sage: ST = StandardTableaux([2,2]); ST
        Standard tableaux of shape [2, 2]
        sage: ST.first()
        [[1, 3], [2, 4]]
        sage: ST.last()
        [[1, 2], [3, 4]]
        sage: ST.cardinality()
        2
        sage: ST.list()
        [[[1, 3], [2, 4]], [[1, 2], [3, 4]]]
        sage: StandardTableau([[1,2,3],[4,5]]).residue_sequence(3).standard_tableaux()  # needs sage.groups
        Standard tableaux with 3-residue sequence (0,1,2,2,0) and multicharge (0)
    """
    @staticmethod
    def __classcall_private__(cls, *args, **kwargs):
        """
        This is a factory class which returns the appropriate parent based on
        arguments.  See the documentation for :class:`StandardTableaux` for
        more information.

        TESTS::

            sage: StandardTableaux()
            Standard tableaux
            sage: StandardTableaux(3)
            Standard tableaux of size 3
            sage: StandardTableaux([2,1])
            Standard tableaux of shape [2, 1]
            sage: StandardTableaux(0)
            Standard tableaux of size 0
            sage: StandardTableaux(n=3)
            Standard tableaux of size 3

            sage: StandardTableaux(-1)
            Traceback (most recent call last):
            ...
            ValueError: the argument must be a nonnegative integer or a partition
            sage: StandardTableaux([[1]])
            Traceback (most recent call last):
            ...
            ValueError: the argument must be a nonnegative integer or a partition
        """
    Element = StandardTableau
    def __contains__(self, x) -> bool:
        """
        EXAMPLES::

            sage: [[1,1],[2,3]] in StandardTableaux()
            False
            sage: [[1,2],[3,4]] in StandardTableaux()
            True
            sage: [[1,3],[2,4]] in StandardTableaux()
            True
            sage: [[1,3],[2,5]] in StandardTableaux()
            False
            sage: [] in StandardTableaux()
            True

        Check that :issue:`14145` is fixed::

            sage: 1 in StandardTableaux()
            False
        """

class StandardTableaux_all(StandardTableaux, DisjointUnionEnumeratedSets):
    """
    All standard tableaux.
    """
    def __init__(self) -> None:
        """
        Initialize the class of all standard tableaux.

        TESTS::

            sage: ST = StandardTableaux()
            sage: TestSuite(ST).run()
        """

class StandardTableaux_size(StandardTableaux, DisjointUnionEnumeratedSets):
    """
    Standard tableaux of fixed size `n`.

    EXAMPLES::

        sage: [ t for t in StandardTableaux(1) ]
        [[[1]]]
        sage: [ t for t in StandardTableaux(2) ]
        [[[1, 2]], [[1], [2]]]
        sage: [ t for t in StandardTableaux(3) ]
        [[[1, 2, 3]], [[1, 3], [2]], [[1, 2], [3]], [[1], [2], [3]]]
        sage: StandardTableaux(4)[:]
        [[[1, 2, 3, 4]],
         [[1, 3, 4], [2]],
         [[1, 2, 4], [3]],
         [[1, 2, 3], [4]],
         [[1, 3], [2, 4]],
         [[1, 2], [3, 4]],
         [[1, 4], [2], [3]],
         [[1, 3], [2], [4]],
         [[1, 2], [3], [4]],
         [[1], [2], [3], [4]]]

    TESTS::

        sage: TestSuite( StandardTableaux(4) ).run()
    """
    size: Incomplete
    def __init__(self, n) -> None:
        """
        Initialize the class of all standard tableaux of size `n`.

        .. WARNING::

            Input is not checked; please use :class:`StandardTableaux` to
            ensure the options are properly parsed.

        TESTS::

            sage: TestSuite( StandardTableaux(0) ).run()
            sage: TestSuite( StandardTableaux(3) ).run()
        """
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: ST3 = StandardTableaux(3)
            sage: all(st in ST3 for st in ST3)
            True
            sage: ST4 = StandardTableaux(4)
            sage: [x for x in ST4 if x in ST3]
            []

        Check that :issue:`14145` is fixed::

            sage: 1 in StandardTableaux(4)
            False
        """
    def cardinality(self):
        """
        Return the number of all standard tableaux of size ``n``.

        The number of standard tableaux of size `n` is equal to the
        number of involutions in the symmetric group `S_n`.
        This is a consequence of the symmetry of the RSK
        correspondence, that if `\\sigma \\mapsto (P, Q)`, then
        `\\sigma^{-1} \\mapsto (Q, P)`. For more information, see
        :wikipedia:`Robinson-Schensted-Knuth_correspondence#Symmetry`.

        ALGORITHM:

        The algorithm uses the fact that standard tableaux of size
        ``n`` are in bijection with the involutions of size ``n``,
        (see page 41 in section 4.1 of [Ful1997]_).  For each number of
        fixed points, you count the number of ways to choose those
        fixed points multiplied by the number of perfect matchings on
        the remaining values.

        EXAMPLES::

            sage: StandardTableaux(3).cardinality()
            4
            sage: ns = [1,2,3,4,5,6]
            sage: sts = [StandardTableaux(n) for n in ns]
            sage: all(st.cardinality() == len(st.list()) for st in sts)
            True

        The cardinality can be computed without constructing all elements in
        this set, so this computation is fast (see also :issue:`28273`)::

            sage: StandardTableaux(500).cardinality()
            423107565308608549951551753690...221285999236657443927937253376

        TESTS::

            sage: def cardinality_using_hook_formula(n):
            ....:     c = 0
            ....:     for p in Partitions(n):
            ....:         c += StandardTableaux(p).cardinality()
            ....:     return c
            sage: all(cardinality_using_hook_formula(i) == StandardTableaux(i).cardinality() for i in range(10))
            True
        """
    def random_element(self):
        """
        Return a random ``StandardTableau`` with uniform probability.

        This algorithm uses the fact that the Robinson-Schensted
        correspondence returns a pair of identical standard Young
        tableaux (SYTs) if and only if the permutation was an involution.
        Thus, generating a random SYT is equivalent to generating a
        random involution.

        To generate an involution, we first need to choose its number of
        fixed points `k` (if the size of the involution is even, the
        number of fixed points will be even, and if the size is odd, the
        number of fixed points will be odd). To do this, we choose a
        random integer `r` between 0 and the number `N` of all
        involutions of size `n`. We then decompose the interval
        `\\{ 1, 2, \\ldots, N \\}` into subintervals whose lengths are the
        numbers of involutions of size `n` with respectively `0`, `1`,
        `\\ldots`, `\\left \\lfloor N/2 \\right \\rfloor` fixed points. The
        interval in which our random integer `r` lies then decides how
        many fixed points our random involution will have. We then
        place those fixed points randomly and then compute a perfect
        matching (an involution without fixed points) on the remaining
        values.

        EXAMPLES::

            sage: StandardTableaux(10).random_element() # random
            [[1, 3, 6], [2, 5, 7], [4, 8], [9], [10]]
            sage: StandardTableaux(0).random_element()
            []
            sage: StandardTableaux(1).random_element()
            [[1]]

        TESTS::

            sage: all(StandardTableaux(10).random_element() in StandardTableaux(10) for i in range(20))
            True
        """

class StandardTableaux_shape(StandardTableaux):
    """
    Semistandard tableaux of a fixed shape `p`.
    """
    shape: Incomplete
    def __init__(self, p) -> None:
        """
        Initialize the class of all semistandard tableaux of a given shape.

        .. WARNING::

            Input is not checked; please use :class:`StandardTableaux` to
            ensure the options are properly parsed.

        TESTS::

            sage: TestSuite( StandardTableaux([2,1,1]) ).run()
        """
    def __contains__(self, x) -> bool:
        """
        EXAMPLES::

            sage: ST = StandardTableaux([2,1,1])
            sage: all(st in ST for st in ST)
            True
            sage: len([x for x in StandardTableaux(4) if x in ST])
            3
            sage: ST.cardinality()
            3

        Check that :issue:`14145` is fixed::

            sage: 1 in StandardTableaux([2,1,1])
            False
        """
    def cardinality(self):
        """
        Return the number of standard Young tableaux of this shape.

        This method uses the so-called *hook length formula*, a formula
        for the number of Young tableaux associated with a given
        partition. The formula says the following: Let `\\lambda` be a
        partition. For each cell `c` of the Young diagram of `\\lambda`,
        let the *hook length* of `c` be defined as `1` plus the number of
        cells horizontally to the right of `c` plus the number of cells
        vertically below `c`. The number of standard Young tableaux of
        shape `\\lambda` is then `n!` divided by the product of the hook
        lengths of the shape of `\\lambda`, where `n = |\\lambda|`.

        For example, consider the partition ``[3,2,1]`` of ``6`` with
        Ferrers diagram::

            # # #
            # #
            #

        When we fill in the cells with their respective hook lengths, we
        obtain::

            5 3 1
            3 1
            1

        The hook length formula returns

        .. MATH::

            \\frac{6!}{5 \\cdot 3 \\cdot 1 \\cdot 3 \\cdot 1 \\cdot 1} = 16.

        EXAMPLES::

            sage: StandardTableaux([3,2,1]).cardinality()
            16
            sage: StandardTableaux([2,2]).cardinality()
            2
            sage: StandardTableaux([5]).cardinality()
            1
            sage: StandardTableaux([6,5,5,3]).cardinality()
            6651216
            sage: StandardTableaux([]).cardinality()
            1

        REFERENCES:

        - http://mathworld.wolfram.com/HookLengthFormula.html
        """
    def __iter__(self):
        """
        An iterator for the standard Young tableaux associated to the
        shape `p` of ``self``.

        EXAMPLES::

            sage: [t for t in StandardTableaux([2,2])]
            [[[1, 3], [2, 4]], [[1, 2], [3, 4]]]
            sage: [t for t in StandardTableaux([3,2])]
            [[[1, 3, 5], [2, 4]],
             [[1, 2, 5], [3, 4]],
             [[1, 3, 4], [2, 5]],
             [[1, 2, 4], [3, 5]],
             [[1, 2, 3], [4, 5]]]
            sage: st = StandardTableaux([2,1])
            sage: st[0].parent() is st
            True
        """
    def list(self):
        """
        Return a list of the standard Young tableaux of the specified shape.

        EXAMPLES::

            sage: StandardTableaux([2,2]).list()
            [[[1, 3], [2, 4]], [[1, 2], [3, 4]]]
            sage: StandardTableaux([5]).list()
            [[[1, 2, 3, 4, 5]]]
            sage: StandardTableaux([3,2,1]).list()
            [[[1, 4, 6], [2, 5], [3]],
             [[1, 3, 6], [2, 5], [4]],
             [[1, 2, 6], [3, 5], [4]],
             [[1, 3, 6], [2, 4], [5]],
             [[1, 2, 6], [3, 4], [5]],
             [[1, 4, 5], [2, 6], [3]],
             [[1, 3, 5], [2, 6], [4]],
             [[1, 2, 5], [3, 6], [4]],
             [[1, 3, 4], [2, 6], [5]],
             [[1, 2, 4], [3, 6], [5]],
             [[1, 2, 3], [4, 6], [5]],
             [[1, 3, 5], [2, 4], [6]],
             [[1, 2, 5], [3, 4], [6]],
             [[1, 3, 4], [2, 5], [6]],
             [[1, 2, 4], [3, 5], [6]],
             [[1, 2, 3], [4, 5], [6]]]
        """
    def random_element(self):
        """
        Return a random standard tableau of the given shape using the
        Greene-Nijenhuis-Wilf Algorithm.

        EXAMPLES::

            sage: t = StandardTableaux([2,2]).random_element()
            sage: t.shape()
            [2, 2]
            sage: StandardTableaux([]).random_element()
            []
        """

def unmatched_places(w, open, close):
    """
    Given a word ``w`` and two letters ``open`` and
    ``close`` to be treated as opening and closing
    parentheses (respectively), return a pair ``(xs, ys)``
    that encodes the positions of the unmatched
    parentheses after the standard parenthesis matching
    procedure is applied to ``w``.

    More precisely, ``xs`` will be the list of all ``i``
    such that ``w[i]`` is an unmatched closing parenthesis,
    while ``ys`` will be the list of all ``i`` such that
    ``w[i]`` is an unmatched opening parenthesis. Both
    lists returned are in increasing order.

    EXAMPLES::

        sage: from sage.combinat.tableau import unmatched_places
        sage: unmatched_places([2,2,2,1,1,1],2,1)
        ([], [])
        sage: unmatched_places([1,1,1,2,2,2],2,1)
        ([0, 1, 2], [3, 4, 5])
        sage: unmatched_places([], 2, 1)
        ([], [])
        sage: unmatched_places([1,2,4,6,2,1,5,3],2,1)
        ([0], [1])
        sage: unmatched_places([2,2,1,2,4,6,2,1,5,3], 2, 1)
        ([], [0, 3])
        sage: unmatched_places([3,1,1,1,2,1,2], 2, 1)
        ([1, 2, 3], [6])
    """
def symmetric_group_action_on_values(word, perm):
    """
    Return the image of the word ``word`` under the
    Lascoux-Schuetzenberger action of the permutation
    ``perm``.

    See :meth:`Tableau.symmetric_group_action_on_values`
    for the definition of the Lascoux-Schuetzenberger
    action on semistandard tableaux. The transformation that
    the reading word of the tableau undergoes in said
    definition is precisely the Lascoux-Schuetzenberger
    action on words.

    EXAMPLES::

        sage: from sage.combinat.tableau import symmetric_group_action_on_values
        sage: symmetric_group_action_on_values([1,1,1],[1,3,2])
        [1, 1, 1]
        sage: symmetric_group_action_on_values([1,1,1],[2,1,3])
        [2, 2, 2]
        sage: symmetric_group_action_on_values([1,2,1],[2,1,3])
        [2, 2, 1]
        sage: symmetric_group_action_on_values([2,2,2],[2,1,3])
        [1, 1, 1]
        sage: symmetric_group_action_on_values([2,1,2],[2,1,3])
        [2, 1, 1]
        sage: symmetric_group_action_on_values([2,2,3,1,1,2,2,3],[1,3,2])
        [2, 3, 3, 1, 1, 2, 3, 3]
        sage: symmetric_group_action_on_values([2,1,1],[2,1])
        [2, 1, 2]
        sage: symmetric_group_action_on_values([2,2,1],[2,1])
        [1, 2, 1]
        sage: symmetric_group_action_on_values([1,2,1],[2,1])
        [2, 2, 1]
    """

class Tableau_class(Tableau):
    """
    This exists solely for unpickling ``Tableau_class`` objects.
    """

class IncreasingTableaux(Tableaux):
    """
    A factory class for the various classes of increasing tableaux.

    An *increasing tableau* is a tableau whose entries are positive
    integers that are strictly increasing across rows and strictly
    increasing down columns. Note that Sage uses the English convention
    for partitions and tableaux; the longer rows are displayed on top.

    INPUT:

    Keyword arguments:

    - ``size`` -- the size of the tableaux
    - ``shape`` -- the shape of the tableaux
    - ``eval`` -- the weight (also called binary content) of
      the tableaux, where values can be either `0` or `1` with position
      `i` being `1` if and only if `i` can appear in the tableaux
    - ``max_entry`` -- positive integer or infinity (``oo``); the maximum
      entry for the tableaux; if ``size`` or ``shape`` are specified,
      ``max_entry`` defaults to be ``size`` or the size of ``shape``

    Positional arguments:

    - the first argument is interpreted as either ``size`` or ``shape``
      according to whether it is an integer or a partition
    - the second keyword argument will always be interpreted as ``eval``

    .. WARNING::

        The ``eval`` is not the usual notion of ``eval`` or ``weight``,
        where the `i`-th entry counts how many `i`'s appear in the tableau.

    EXAMPLES::

        sage: IT = IncreasingTableaux([2,1]); IT
        Increasing tableaux of shape [2, 1] and maximum entry 3
        sage: IT.list()
        [[[1, 3], [2]], [[1, 2], [3]], [[1, 2], [2]], [[1, 3], [3]], [[2, 3], [3]]]

        sage: IT = IncreasingTableaux(3); IT
        Increasing tableaux of size 3 and maximum entry 3
        sage: IT.list()
        [[[1, 2, 3]],
         [[1, 3], [2]],
         [[1, 2], [3]],
         [[1, 2], [2]],
         [[1, 3], [3]],
         [[2, 3], [3]],
         [[1], [2], [3]]]

        sage: IT = IncreasingTableaux(3, max_entry=2); IT
        Increasing tableaux of size 3 and maximum entry 2
        sage: IT.list()
        [[[1, 2], [2]]]

        sage: IT = IncreasingTableaux(3, max_entry=4); IT
        Increasing tableaux of size 3 and maximum entry 4
        sage: IT.list()
        [[[1, 2, 3]],
         [[1, 2, 4]],
         [[1, 3, 4]],
         [[2, 3, 4]],
         [[1, 3], [2]],
         [[1, 2], [3]],
         [[1, 4], [2]],
         [[1, 2], [4]],
         [[1, 2], [2]],
         [[1, 4], [3]],
         [[1, 3], [4]],
         [[1, 3], [3]],
         [[1, 4], [4]],
         [[2, 4], [3]],
         [[2, 3], [4]],
         [[2, 3], [3]],
         [[2, 4], [4]],
         [[3, 4], [4]],
         [[1], [2], [3]],
         [[1], [2], [4]],
         [[1], [3], [4]],
         [[2], [3], [4]]]

        sage: IT = IncreasingTableaux(3, max_entry=oo); IT
        Increasing tableaux of size 3
        sage: IT[123]
        [[5, 7], [6]]

        sage: IT = IncreasingTableaux(max_entry=2)
        sage: list(IT)
        [[], [[1]], [[2]], [[1, 2]], [[1], [2]]]
        sage: IT[4]
        [[1], [2]]

        sage: IncreasingTableaux()[0]
        []

    .. SEEALSO::

        - :class:`Tableaux`
        - :class:`Tableau`
        - :class:`SemistandardTableaux`
        - :class:`SemistandardTableau`
        - :class:`StandardTableaux`
        - :class:`StandardTableau`
        - :class:`IncreasingTableau`
    """
    @staticmethod
    def __classcall_private__(cls, *args, **kwargs):
        """
        This is a factory class which returns the appropriate parent based on
        arguments.  See the documentation for :class:`IncreasingTableaux`
        for more information.

        TESTS::

            sage: IncreasingTableaux()
            Increasing tableaux
            sage: IncreasingTableaux(3)
            Increasing tableaux of size 3 and maximum entry 3
            sage: IncreasingTableaux(size=3)
            Increasing tableaux of size 3 and maximum entry 3
            sage: IncreasingTableaux(0)
            Increasing tableaux of size 0 and maximum entry 0
            sage: IncreasingTableaux([2,1])
            Increasing tableaux of shape [2, 1] and maximum entry 3
            sage: IncreasingTableaux(shape=[2,1])
            Increasing tableaux of shape [2, 1] and maximum entry 3
            sage: IncreasingTableaux([])
            Increasing tableaux of shape [] and maximum entry 0
            sage: IncreasingTableaux(eval=(1,0,1))
            Increasing tableaux of size 2 and weight (1, 0, 1)
            sage: IncreasingTableaux(max_entry=3)
            Increasing tableaux with maximum entry 3
            sage: IncreasingTableaux(3, (1,0,1))
            Increasing tableaux of size 3 and weight (1, 0, 1)
            sage: IncreasingTableaux(3, shape=[2,1])
            Increasing tableaux of shape [2, 1] and maximum entry 3
            sage: IncreasingTableaux(3, (1,0,1), shape=[2,1])
            Increasing tableaux of shape [2, 1] and weight (1, 0, 1)
            sage: IncreasingTableaux(3, max_entry=4)
            Increasing tableaux of size 3 and maximum entry 4
            sage: IncreasingTableaux(3, max_entry=oo)
            Increasing tableaux of size 3
            sage: IncreasingTableaux([2, 1], max_entry=oo)
            Increasing tableaux of shape [2, 1]
            sage: IncreasingTableaux([2, 1], (1,0,1))
            Increasing tableaux of shape [2, 1] and weight (1, 0, 1)
            sage: mu = Partition([2,1]); IncreasingTableaux(mu, (1,0,1))
            Increasing tableaux of shape [2, 1] and weight (1, 0, 1)
            sage: IncreasingTableaux(3, (1,0,1), max_entry=3)
            Increasing tableaux of size 3 and weight (1, 0, 1)

            sage: IncreasingTableaux(3, shape=[2])
            Traceback (most recent call last):
            ...
            ValueError: size and shape are different sizes

            sage: IncreasingTableaux(3, (1,0,1,1,1))
            Traceback (most recent call last):
            ...
            ValueError: size is smaller than the number of labels

            sage: IncreasingTableaux([2],(1,0,1,1))
            Traceback (most recent call last):
            ...
            ValueError: number of boxes is smaller than the number of labels

            sage: IncreasingTableaux(2,(1,0,1), max_entry=4)
            Traceback (most recent call last):
            ...
            ValueError: the maximum entry must match the weight

            sage: IncreasingTableaux(eval=(1,0,1), max_entry=oo)
            Traceback (most recent call last):
            ...
            ValueError: the maximum entry must match the weight

            sage: IncreasingTableaux([[1]])
            Traceback (most recent call last):
            ...
            ValueError: shape must be a (skew) partition
        """
    Element = IncreasingTableau
    max_entry: Incomplete
    def __init__(self, **kwds) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: S = IncreasingTableaux()
            sage: TestSuite(S).run()  # long time
        """
    def __getitem__(self, r):
        """
        The default implementation of ``__getitem__`` for enumerated sets
        does not allow slices so we override it.

        EXAMPLES::

            sage: IncreasingTableaux([4,3,3,2])[10:20]     # long time
            [[[1, 5, 8, 10], [2, 6, 9], [3, 7, 12], [4, 11]],
             [[1, 5, 8, 10], [2, 6, 9], [3, 7, 11], [4, 12]],
             [[1, 5, 8, 9], [2, 6, 11], [3, 7, 12], [4, 10]],
             [[1, 5, 8, 9], [2, 6, 10], [3, 7, 12], [4, 11]],
             [[1, 5, 8, 9], [2, 6, 10], [3, 7, 11], [4, 12]],
             [[1, 5, 7, 12], [2, 6, 10], [3, 8, 11], [4, 9]],
             [[1, 5, 7, 11], [2, 6, 10], [3, 8, 12], [4, 9]],
             [[1, 5, 7, 10], [2, 6, 11], [3, 8, 12], [4, 9]],
             [[1, 5, 7, 12], [2, 6, 9], [3, 8, 11], [4, 10]],
             [[1, 5, 7, 11], [2, 6, 9], [3, 8, 12], [4, 10]]]

            sage: IncreasingTableaux(size=2, max_entry=oo)[5]
            [[2], [3]]

            sage: IncreasingTableaux([2,1], max_entry=oo)[3]
            [[1, 2], [4]]

            sage: IncreasingTableaux(3, max_entry=4)[0:5]    # indirect doctest
            [[[1, 2, 3]], [[1, 2, 4]], [[1, 3, 4]], [[2, 3, 4]], [[1, 3], [2]]]

            sage: IncreasingTableaux([2,2], (1,0,1,1,1))[0]    # indirect doctest
            [[1, 4], [3, 5]]

            sage: IncreasingTableaux([1,1,1], max_entry=4)[0:4]
            [[[1], [2], [3]], [[1], [2], [4]], [[1], [3], [4]], [[2], [3], [4]]]

            sage: IncreasingTableaux(3, (1,0,1,1))[1]    # indirect doctest
            [[1, 4], [3]]

            sage: IncreasingTableaux(3)[:]  # indirect doctest
            [[[1, 2, 3]],
             [[1, 3], [2]],
             [[1, 2], [3]],
             [[1, 2], [2]],
             [[1, 3], [3]],
             [[2, 3], [3]],
             [[1], [2], [3]]]

            sage: IncreasingTableaux([2,2])[1]   # indirect doctest
            [[1, 2], [3, 4]]

        TESTS::

            sage: IncreasingTableaux()[5]
            [[1, 3], [2]]

            sage: IncreasingTableaux(max_entry=4)[5]
            [[1, 2]]

            sage: IncreasingTableaux()[:]
            Traceback (most recent call last):
            ...
            ValueError: infinite set

            sage: IncreasingTableaux(size=2, max_entry=oo)[:]
            Traceback (most recent call last):
            ...
            ValueError: infinite set
        """
    def __contains__(self, t) -> bool:
        """
        Return ``True`` if ``t`` can be interpreted as an
        :class:`IncreasingTableau`.

        TESTS::

            sage: T = sage.combinat.tableau.IncreasingTableaux_all()
            sage: [[1,2],[2]] in T
            True
            sage: [] in T
            True
            sage: Tableau([[1]]) in T
            True
            sage: StandardTableau([[1]]) in T
            True

            sage: [[1,2],[1]] in T
            False
            sage: [[1,1],[5]] in T
            False
            sage: [[1,7],[5]] in T
            True
            sage: [[1,3,2]] in T
            False

            sage: None in T
            False
        """

class IncreasingTableaux_all(IncreasingTableaux, DisjointUnionEnumeratedSets):
    """
    All increasing tableaux.

    EXAMPLES::

        sage: T = IncreasingTableaux()
        sage: T.cardinality()
        +Infinity

        sage: T = IncreasingTableaux(max_entry=3)
        sage: list(T)
        [[],
         [[1]],
         [[2]],
         [[3]],
         [[1, 2]],
         [[1, 3]],
         [[2, 3]],
         [[1], [2]],
         [[1], [3]],
         [[2], [3]],
         [[1, 2, 3]],
         [[1, 3], [2]],
         [[1, 2], [3]],
         [[1, 2], [2]],
         [[1, 3], [3]],
         [[2, 3], [3]],
         [[1], [2], [3]]]

    TESTS::

        sage: T = IncreasingTableaux(max_entry=0)
        sage: list(T)
        [[]]
    """
    max_entry: Incomplete
    def __init__(self, max_entry=None) -> None:
        """
        Initialize the class of all increasing tableaux.

        .. WARNING::

            Input is not checked; please use :class:`IncreasingTableaux` to
            ensure the options are properly parsed.

        TESTS::

            sage: from sage.combinat.tableau import IncreasingTableaux_all
            sage: T = IncreasingTableaux_all()
            sage: TestSuite(T).run()  # long time

            sage: T = IncreasingTableaux_all(max_entry=3)
            sage: TestSuite(T).run()

            sage: T = IncreasingTableaux_all(max_entry=0)
            sage: TestSuite(T).run()
        """

class IncreasingTableaux_size_inf(IncreasingTableaux):
    """
    Increasing tableaux of fixed size `n` with no maximum entry.
    """
    size: Incomplete
    def __init__(self, n) -> None:
        """
        Initialize the class of increasing tableaux of size `n` with no
        maximum entry.

        .. WARNING::

            Input is not checked; please use :class:`IncreasingTableaux` to
            ensure the options are properly parsed.

        TESTS::

            sage: from sage.combinat.tableau import IncreasingTableaux_size_inf
            sage: T = IncreasingTableaux_size_inf(3)
            sage: TestSuite(T).run()
        """
    def __contains__(self, t) -> bool:
        """
        Return ``True`` if ``t`` can be interpreted as an element of ``self``.

        TESTS::

            sage: T = IncreasingTableaux(3, max_entry=oo)
            sage: [[1,2],[5]] in T
            True
            sage: StandardTableau([[1, 2], [3]]) in T
            True

            sage: [] in T
            False
            sage: Tableau([[1]]) in T
            False
        """
    def __iter__(self):
        """
        EXAMPLES::

            sage: IT = IncreasingTableaux(3, max_entry=oo)
            sage: [IT[t] for t in range(5)]
            [[[1, 2, 3]], [[1, 3], [2]], [[1, 2], [3]], [[1], [2], [3]], [[1, 2, 4]]]
            sage: IT[1000]
            [[3, 13], [10]]
            sage: IT[0].parent() is IT
            True
        """

class IncreasingTableaux_shape_inf(IncreasingTableaux):
    """
    Increasing tableaux of fixed shape `p` and no maximum entry.
    """
    shape: Incomplete
    def __init__(self, p) -> None:
        """
        Initialize the class of increasing tableaux of shape `p` and no
        maximum entry.

        .. WARNING::

            Input is not checked; please use :class:`IncreasingTableaux` to
            ensure the options are properly parsed.

        TESTS::

            sage: IT = IncreasingTableaux([2,1], max_entry=oo)
            sage: type(IT)
            <class 'sage.combinat.tableau.IncreasingTableaux_shape_inf_with_category'>
            sage: TestSuite(IT).run()
        """
    def __contains__(self, x) -> bool:
        """
        EXAMPLES::

            sage: IT = IncreasingTableaux([2,1], max_entry=oo)
            sage: [[13, 67], [1467]] in IT
            True
            sage: IT = IncreasingTableaux([3,1], max_entry=oo)
            sage: [[13, 67], [1467]] in IT
            False
        """
    def __iter__(self):
        """
        An iterator for the increasing partitions of shape ``p`` and no
        maximum entry. Iterates through with maximum entry as order.

        EXAMPLES::

            sage: IT = IncreasingTableaux([3, 1], max_entry=oo)
            sage: IT[1000]
            [[1, 2, 12], [6]]
            sage: [IT[t] for t in range(5)]
            [[[1, 3, 4], [2]],
             [[1, 2, 4], [3]],
             [[1, 2, 3], [4]],
             [[1, 3, 5], [2]],
             [[1, 2, 5], [3]]]
            sage: IT[0].parent() is IT
            True
        """

class IncreasingTableaux_size(IncreasingTableaux):
    """
    Increasing tableaux of fixed size `n`.
    """
    size: Incomplete
    def __init__(self, n, max_entry=None) -> None:
        """
        Initialize the class of increasing tableaux of size `n`.

        .. WARNING::

            Input is not checked; please use :class:`IncreasingTableaux`
            to ensure the options are properly parsed.

        TESTS::

            sage: IT = IncreasingTableaux(3); IT
            Increasing tableaux of size 3 and maximum entry 3
            sage: type(IT)
            <class 'sage.combinat.tableau.IncreasingTableaux_size_with_category'>
            sage: TestSuite(IT).run()

            sage: IT = IncreasingTableaux(3, max_entry=6)
            sage: type(IT)
            <class 'sage.combinat.tableau.IncreasingTableaux_size_with_category'>
            sage: TestSuite(IT).run()
        """
    def __contains__(self, x) -> bool:
        """
        EXAMPLES::

            sage: [[1,2],[2,3]] in IncreasingTableaux(3)
            False
            sage: [[1,2],[2,3]] in IncreasingTableaux(4)
            True
            sage: [[1,2],[2,3]] in IncreasingTableaux(4, max_entry=2)
            False
            sage: IT = IncreasingTableaux(4)
            sage: all(it in IT for it in IT)
            True
        """
    def __iter__(self):
        """
        EXAMPLES::

            sage: [ t for t in IncreasingTableaux(2) ]
            [[[1, 2]], [[1], [2]]]
            sage: [ t for t in IncreasingTableaux(3) ]
            [[[1, 2, 3]],
             [[1, 3], [2]],
             [[1, 2], [3]],
             [[1, 2], [2]],
             [[1, 3], [3]],
             [[2, 3], [3]],
             [[1], [2], [3]]]

            sage: [ t for t in IncreasingTableaux(4, max_entry=3) ]
            [[[1, 2, 3], [2]],
             [[1, 2, 3], [3]],
             [[1, 2], [2, 3]],
             [[1, 2], [2], [3]],
             [[1, 3], [2], [3]]]

            sage: IT = IncreasingTableaux(3)
            sage: IT[0].parent() is IT
            True

            sage: list(IncreasingTableaux(size=4, max_entry=2))
            []
            sage: list(IncreasingTableaux(size=3, max_entry=2))
            [[[1, 2], [2]]]
            sage: list(IncreasingTableaux(0, max_entry=4))
            [[]]
            sage: list(IncreasingTableaux(3, max_entry=0))
            []
        """

class IncreasingTableaux_shape(IncreasingTableaux):
    """
    Increasing tableaux of fixed shape `p` with a given max entry.

    An increasing tableau with max entry `i` is required to have all
    its entries less or equal to `i`. It is not required to actually
    contain an entry `i`.

    INPUT:

    - ``p`` -- a partition
    - ``max_entry`` -- the max entry; defaults to the size of ``p``
    """
    shape: Incomplete
    def __init__(self, p, max_entry=None) -> None:
        """
        Initialize the class of increasing tableaux of shape `p`, with a
        given ``max_entry``.

        .. WARNING::

            Input is not checked; please use :class:`IncreasingTableaux` to
            ensure the options are properly parsed.

        TESTS::

            sage: IT = IncreasingTableaux([2,1])
            sage: TestSuite(IT).run()

            sage: IT = IncreasingTableaux([2,1], max_entry=5)
            sage: TestSuite(IT).run()
        """
    def __iter__(self):
        """
        An iterator for the increasing tableaux of the specified shape
        with the specified max entry.

        EXAMPLES::

            sage: [ t for t in IncreasingTableaux([3]) ]
            [[[1, 2, 3]]]
            sage: [ t for t in IncreasingTableaux([2,1]) ]
            [[[1, 3], [2]], [[1, 2], [3]], [[1, 2], [2]], [[1, 3], [3]], [[2, 3], [3]]]
            sage: [ t for t in IncreasingTableaux([3,1]) ]
            [[[1, 3, 4], [2]],
             [[1, 2, 4], [3]],
             [[1, 2, 3], [4]],
             [[1, 2, 3], [2]],
             [[1, 2, 3], [3]],
             [[1, 2, 4], [2]],
             [[1, 2, 4], [4]],
             [[1, 3, 4], [3]],
             [[1, 3, 4], [4]],
             [[2, 3, 4], [3]],
             [[2, 3, 4], [4]]]

            sage: [ t for t in IncreasingTableaux([3,1], max_entry=3) ]
            [[[1, 2, 3], [2]], [[1, 2, 3], [3]]]

            sage: IT = IncreasingTableaux([3])
            sage: IT[0].parent() is IT
            True

            sage: list(IncreasingTableaux(shape=[4,2], max_entry=2))
            []
            sage: list(IncreasingTableaux(shape=[2,1], max_entry=0))
            []
            sage: list(IncreasingTableaux(shape=[], max_entry=4))
            [[]]
        """
    def __contains__(self, x) -> bool:
        """
        EXAMPLES::

            sage: IT = IncreasingTableaux([2,1])
            sage: all(it in IT for it in IT)
            True
            sage: len([x for x in IncreasingTableaux(3) if x in IT])
            5
            sage: IT.cardinality()
            5

            sage: IT = IncreasingTableaux([2,1], max_entry=4)
            sage: all(it in IT for it in IT)
            True
            sage: IT.cardinality()
            14
        """

class IncreasingTableaux_shape_weight(IncreasingTableaux_shape):
    """
    Increasing tableaux of fixed shape `p` and binary weight `wt`.
    """
    weight: Incomplete
    def __init__(self, p, wt) -> None:
        """
        Initialize the class of all increasing tableaux of shape ``p`` and
        weight ``mu``.

        .. WARNING::

            Input is not checked; please use :class:`IncreasingTableaux` to
            ensure the options are properly parsed.

        TESTS::

            sage: IT = IncreasingTableaux([2,1], (1,0,1))
            sage: TestSuite(IT).run()
        """
    def __contains__(self, x) -> bool:
        """
        EXAMPLES::

            sage: IT = IncreasingTableaux([2,1], (1,0,1))
            sage: all(it in IT for it in IT)
            True
            sage: len([x for x in IncreasingTableaux(3) if x in IT])
            1
            sage: IT.cardinality()
            1
            sage: None in IT
            False

        Corner case check::

            sage: IT = IncreasingTableaux([], ())
            sage: [] in IT
            True
            sage: None in IT
            False
        """
    def __iter__(self):
        """
        Iterate over ``self``.

        EXAMPLES::

            sage: IncreasingTableaux([2,2], (1,0,1,1)).list()
            [[[1, 3], [3, 4]]]
            sage: IncreasingTableaux([2,2,2], (1,0,1,1,0,1,1)).list()
            [[[1, 3], [3, 6], [4, 7]],
             [[1, 3], [3, 4], [6, 7]],
             [[1, 4], [3, 6], [4, 7]],
             [[1, 4], [3, 6], [6, 7]],
             [[1, 3], [4, 6], [6, 7]]]

        TESTS::

            sage: IT = IncreasingTableaux([3,1], (1,0,1,1))
            sage: [IT[i] for i in range(2)]
            [[[1, 3, 4], [3]], [[1, 3, 4], [4]]]
            sage: IT[0].parent() is IT
            True

            sage: list(IncreasingTableaux(shape=[], eval=(0,0,0)))
            [[]]

        We explicitly check a corner case::

            sage: from sage.combinat.tableau import IncreasingTableaux_shape_weight
            sage: list(IncreasingTableaux_shape_weight(Partition([]), (0,1,1)))
            []
        """

class IncreasingTableaux_size_weight(IncreasingTableaux):
    """
    Increasing tableaux of fixed size `n` and weight `wt`.
    """
    size: Incomplete
    weight: Incomplete
    def __init__(self, n, wt) -> None:
        """
        Initialize the class of increasing tableaux of size `n` and
        weight ``wt``.

        .. WARNING::

            Input is not checked; please use :class:`IncreasingTableaux` to
            ensure the options are properly parsed.

        TESTS::

            sage: IT = IncreasingTableaux(3, (1,0,1))
            sage: TestSuite(IT).run()
        """
    def __iter__(self):
        """
        EXAMPLES::

            sage: [ T for T in IncreasingTableaux(3, (1,0,1)) ]
            [[[1, 3], [3]]]
            sage: [ T for T in IncreasingTableaux(4, (1,0,1,1)) ]
            [[[1, 3, 4], [3]],
             [[1, 3, 4], [4]],
             [[1, 3], [3, 4]],
             [[1, 3], [3], [4]],
             [[1, 4], [3], [4]]]
            sage: IT = IncreasingTableaux(4, (1,0,1,1))
            sage: IT[0].parent() is IT
            True
        """
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: IT = IncreasingTableaux(4, (1,0,1,1))
            sage: all(it in IT for it in IT)
            True
            sage: all(it in IT for it in IncreasingTableaux([2,2], (1,0,1,1)))
            True
        """
