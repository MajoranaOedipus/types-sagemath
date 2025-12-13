from .combinat import CombinatorialElement as CombinatorialElement
from .integer_vector import IntegerVectors as IntegerVectors
from .partition import Partition as Partition, Partitions as Partitions, Partitions_n as Partitions_n, RegularPartitions_all as RegularPartitions_all, RegularPartitions_n as RegularPartitions_n
from _typeshed import Incomplete
from collections.abc import Generator
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.categories.infinite_enumerated_sets import InfiniteEnumeratedSets as InfiniteEnumeratedSets
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as IntegerModRing
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.semirings.non_negative_integer_semiring import NN as NN
from sage.sets.positive_integers import PositiveIntegers as PositiveIntegers
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class PartitionTuple(CombinatorialElement):
    """
    A tuple of :class:`Partition`.

    A tuple of partition comes equipped with many of methods available to
    partitions. The ``level`` of the PartitionTuple is the length of the tuple.

    This is an ordered `k`-tuple of partitions
    `\\mu=(\\mu^{(1)},\\mu^{(2)},...,\\mu^{(k)})`. If

    .. MATH::

        n = \\lvert \\mu \\rvert = \\lvert \\mu^{(1)} \\rvert +
        \\lvert \\mu^{(2)} \\rvert + \\cdots + \\lvert \\mu^{(k)} \\rvert

    then `\\mu` is a `k`-partition of `n`.

    In representation theory PartitionTuples arise as the natural indexing
    set for the ordinary irreducible representations of:

    - the wreath products of cyclic groups with symmetric groups
    - the Ariki-Koike algebras, or the cyclotomic Hecke algebras of
      the complex reflection groups of type `G(r,1,n)`
    - the degenerate cyclotomic Hecke algebras of type `G(r,1,n)`

    When these algebras are not semisimple, partition tuples index an important
    class of modules for the algebras which are generalisations of the Specht
    modules of the symmetric groups.

    Tuples of partitions also index the standard basis of the higher level
    combinatorial Fock spaces. As a consequence, the combinatorics of partition
    tuples encapsulates the canonical bases of crystal graphs for the irreducible
    integrable highest weight modules of the (quantized) affine special linear
    groups and the (quantized) affine general linear groups. By the
    categorification theorems of Ariki, Varagnolo-Vasserot, Stroppel-Webster and
    others, in characteristic zero the degenerate and non-degenerate cyclotomic
    Hecke algebras, via their Khovanov-Lauda-Rouquier grading, categorify the
    canonical bases of the quantum affine special and general linear groups.

    Partitions are naturally in bijection with 1-tuples of partitions. Most of the
    combinatorial operations defined on partitions extend to PartitionTuples in
    a meaningful way. For example, the semisimple branching rules for the Specht
    modules are described by adding and removing cells from partition tuples and
    the modular branching rules correspond to adding and removing good and
    cogood nodes, which is the underlying combinatorics for the associated
    crystal graphs.

    .. WARNING::

        In the literature, the cells of a partition tuple are usually written
        in the form `(r,c,k)`, where `r` is the row index, `c` is the column
        index, and `k` is the component index. In sage, if ``mu`` is a
        partition tuple then ``mu[k]`` most naturally refers to the `k`-th
        component of ``mu``, so we use the convention of the `(k,r,c)`-th cell
        in a partition tuple refers to the cell in component `k`, row `r`, and
        column `c`.

    INPUT:

    Anything which can reasonably be interpreted as a tuple of partitions.
    That is, a list or tuple of partitions or valid input to
    :class:`Partition`.

    EXAMPLES::

        sage: mu=PartitionTuple( [[3,2],[2,1],[],[1,1,1,1]] ); mu
        ([3, 2], [2, 1], [], [1, 1, 1, 1])
        sage: nu=PartitionTuple( ([3,2],[2,1],[],[1,1,1,1]) ); nu
        ([3, 2], [2, 1], [], [1, 1, 1, 1])
        sage: mu == nu
        True
        sage: mu is nu
        False
        sage: mu in PartitionTuples()
        True
        sage: mu.parent()
        Partition tuples

        sage: lam=PartitionTuples(3)([[3,2],[],[1,1,1,1]]); lam
        ([3, 2], [], [1, 1, 1, 1])
        sage: lam.level()
        3
        sage: lam.size()
        9
        sage: lam.category()
        Category of elements of Partition tuples of level 3
        sage: lam.parent()
        Partition tuples of level 3
        sage: lam[0]
        [3, 2]
        sage: lam[1]
        []
        sage: lam[2]
        [1, 1, 1, 1]
        sage: lam.pp()
           ***   -   *
           **        *
                     *
                     *
        sage: lam.removable_cells()
        [(0, 0, 2), (0, 1, 1), (2, 3, 0)]
        sage: lam.down_list()
        [([2, 2], [], [1, 1, 1, 1]), ([3, 1], [], [1, 1, 1, 1]), ([3, 2], [], [1, 1, 1])]
        sage: lam.addable_cells()
        [(0, 0, 3), (0, 1, 2), (0, 2, 0), (1, 0, 0), (2, 0, 1), (2, 4, 0)]
        sage: lam.up_list()
        [([4, 2], [], [1, 1, 1, 1]), ([3, 3], [], [1, 1, 1, 1]), ([3, 2, 1], [], [1, 1, 1, 1]), ([3, 2], [1], [1, 1, 1, 1]), ([3, 2], [], [2, 1, 1, 1]), ([3, 2], [], [1, 1, 1, 1, 1])]
        sage: lam.conjugate()
        ([4], [], [2, 2, 1])
        sage: lam.dominates( PartitionTuple([[3],[1],[2,2,1]]) )
        False
        sage: lam.dominates( PartitionTuple([[3],[2],[1,1,1]]))
        True

    TESTS::

        sage: TestSuite( PartitionTuple([4,3,2]) ).run()
        sage: TestSuite( PartitionTuple([[4,3,2],[],[],[3,2,1]]) ).run()

    .. SEEALSO::

        - :class:`PartitionTuples`
        - :class:`Partitions`
    """
    Element = Partition
    @staticmethod
    def __classcall_private__(self, mu):
        """
        This delegates the construction of a :class:`PartitionTuple` to the
        ``element_class()`` call of the appropriate
        :class:`PartitionTuples_level`.

        TESTS::

            sage: mu=PartitionTuple([[1,1],[1]])
            sage: mu.category()
            Category of elements of Partition tuples
            sage: type(mu)
            <class 'sage.combinat.partition_tuple.PartitionTuples_all_with_category.element_class'>
        """
    def __init__(self, parent, mu) -> None:
        """
        Initialize ``self`` and checks that the input determines a tuple of
        partitions.

        EXAMPLES::

            sage: PartitionTuple([])
            []
            sage: P = PartitionTuple([[2,1,1,0],[2,1]]); P
            ([2, 1, 1], [2, 1])
            sage: TestSuite(P).run()
            sage: PartitionTuple([[],[],[2,1,2,1]])
            Traceback (most recent call last):
            ...
            ValueError: [[], [], [2, 1, 2, 1]] is not a tuple of Partitions
        """
    def level(self):
        """
        Return the level of this partition tuple.

        The level is the length of the tuple.

        EXAMPLES::

            sage: PartitionTuple([[2,1,1,0],[2,1]]).level()
            2
            sage: PartitionTuple([[],[],[2,1,1]]).level()
            3
        """
    def __len__(self) -> int:
        """
        Return the length of this partition tuple.

        The length is also known as the level.

        EXAMPLES::

            sage: len( PartitionTuple([[2,1],[3,2],[1,1,1]]) )
            3
        """
    def components(self):
        '''
        Return a list containing the shape of this partition.

        This function exists in order to give a uniform way of iterating over
        the \\"components\\" of partition tuples of level 1 (partitions) and for
        higher levels.

        EXAMPLES::

            sage: for t in PartitionTuple([[2,1],[3,2],[3]]).components():
            ....:     print(\'%s\\n\' % t.ferrers_diagram())
            **
            *
            <BLANKLINE>
            ***
            **
            <BLANKLINE>
            ***
            <BLANKLINE>
            sage: for t in PartitionTuple([3,2]).components():
            ....:     print(\'%s\\n\' % t.ferrers_diagram())
            ***
            **
        '''
    def diagram(self):
        """
        Return a string for the Ferrers diagram of ``self``.

        EXAMPLES::

            sage: print(PartitionTuple([[2,1],[3,2],[1,1,1]]).diagram())
               **   ***   *
               *    **    *
                          *
            sage: print(PartitionTuple([[3,2],[2,1],[],[1,1,1,1]]).diagram())
               ***   **   -   *
               **    *        *
                              *
                              *
            sage: PartitionTuples.options(convention='french')
            sage: print(PartitionTuple([[3,2],[2,1],[],[1,1,1,1]]).diagram())
                              *
                              *
               **    *        *
               ***   **   -   *
            sage: PartitionTuples.options._reset()
        """
    ferrers_diagram = diagram
    def pp(self) -> None:
        """
        Pretty print this partition tuple. See :meth:`diagram`.

        EXAMPLES::

            sage: PartitionTuple([[5,5,2,1],[3,2]]).pp()
            *****   ***
            *****   **
            **
            *
        """
    def size(self):
        """
        Return the size of a partition tuple.

        EXAMPLES::

            sage: PartitionTuple([[2,1],[],[2,2]]).size()
            7
            sage: PartitionTuple([[],[],[1],[3,2,1]]).size()
            7
        """
    def row_standard_tableaux(self):
        """
        Return the :class:`row standard tableau tuples
        <sage.combinat.tableau_tuple.RowStandardTableauTuples>`
        of shape ``self``.

        EXAMPLES::

            sage: PartitionTuple([[],[3,2,2,1],[2,2,1],[3]]).row_standard_tableaux()
            Row standard tableau tuples of shape ([], [3, 2, 2, 1], [2, 2, 1], [3])
        """
    def standard_tableaux(self):
        """
        Return the :class:`standard tableau tuples<StandardTableauTuples>`
        of shape ``self``.

        EXAMPLES::

            sage: PartitionTuple([[],[3,2,2,1],[2,2,1],[3]]).standard_tableaux()
            Standard tableau tuples of shape ([], [3, 2, 2, 1], [2, 2, 1], [3])
        """
    def up(self) -> Generator[Incomplete]:
        """
        Generator (iterator) for the partition tuples that are obtained from
        ``self`` by adding a cell.

        EXAMPLES::

            sage: [mu for mu in PartitionTuple([[],[3,1],[1,1]]).up()]
            [([1], [3, 1], [1, 1]), ([], [4, 1], [1, 1]), ([], [3, 2], [1, 1]), ([], [3, 1, 1], [1, 1]), ([], [3, 1], [2, 1]), ([], [3, 1], [1, 1, 1])]
            sage: [mu for mu in PartitionTuple([[],[],[],[]]).up()]
            [([1], [], [], []), ([], [1], [], []), ([], [], [1], []), ([], [], [], [1])]
        """
    def up_list(self):
        """
        Return a list of the partition tuples that can be formed from ``self``
        by adding a cell.

        EXAMPLES::

            sage: PartitionTuple([[],[3,1],[1,1]]).up_list()
            [([1], [3, 1], [1, 1]), ([], [4, 1], [1, 1]), ([], [3, 2], [1, 1]), ([], [3, 1, 1], [1, 1]), ([], [3, 1], [2, 1]), ([], [3, 1], [1, 1, 1])]
            sage: PartitionTuple([[],[],[],[]]).up_list()
            [([1], [], [], []), ([], [1], [], []), ([], [], [1], []), ([], [], [], [1])]
        """
    def down(self) -> Generator[Incomplete]:
        """
        Generator (iterator) for the partition tuples that are obtained from
        ``self`` by removing a cell.

        EXAMPLES::

            sage: [mu for mu in PartitionTuple([[],[3,1],[1,1]]).down()]
            [([], [2, 1], [1, 1]), ([], [3], [1, 1]), ([], [3, 1], [1])]
            sage: [mu for mu in PartitionTuple([[],[],[]]).down()]
            []
        """
    def down_list(self):
        """
        Return a list of the partition tuples that can be formed from ``self``
        by removing a cell.

        EXAMPLES::

            sage: PartitionTuple([[],[3,1],[1,1]]).down_list()
            [([], [2, 1], [1, 1]), ([], [3], [1, 1]), ([], [3, 1], [1])]
            sage: PartitionTuple([[],[],[]]).down_list()
            []
        """
    def cells(self):
        """
        Return the coordinates of the cells of ``self``. Coordinates are given
        as (component index, row index, column index) and are 0 based.

        EXAMPLES::

            sage: PartitionTuple([[2,1],[1],[1,1,1]]).cells()
            [(0, 0, 0), (0, 0, 1), (0, 1, 0), (1, 0, 0), (2, 0, 0), (2, 1, 0), (2, 2, 0)]
        """
    def content(self, k, r, c, multicharge):
        """
        Return the content of the cell.

        Let `m_k =` ``multicharge[k]``, then the content of a cell is
        `m_k + c - r`.

        If the ``multicharge`` is a list of integers then it simply offsets the
        values of the contents in each component. On the other hand, if the
        ``multicharge`` belongs to `\\ZZ/e\\ZZ` then the corresponding
        `e`-residue is returned (that is, the content mod `e`).

        As with the content method for partitions, the content of a cell does
        not technically depend on the partition tuple, but this method is
        included because it is often useful.

        EXAMPLES::

            sage: PartitionTuple([[2,1],[2],[1,1,1]]).content(0,1,0, [0,0,0])
            -1
            sage: PartitionTuple([[2,1],[2],[1,1,1]]).content(0,1,0, [1,0,0])
            0
            sage: PartitionTuple([[2,1],[2],[1,1,1]]).content(2,1,0, [0,0,0])
            -1

        and now we return the 3-residue of a cell::

            sage: multicharge = [IntegerModRing(3)(c) for c in [0,0,0]]
            sage: PartitionTuple([[2,1],[2],[1,1,1]]).content(0,1,0, multicharge)
            2
        """
    def content_tableau(self, multicharge):
        """
        Return the tableau which has (k,r,c)th entry equal to the content
        ``multicharge[k]-r+c`` of this cell.

        As with the content function, by setting the ``multicharge``
        appropriately the tableau containing the residues is returned.

        EXAMPLES::

            sage: PartitionTuple([[2,1],[2],[1,1,1]]).content_tableau([0,0,0])
            ([[0, 1], [-1]], [[0, 1]], [[0], [-1], [-2]])
            sage: PartitionTuple([[2,1],[2],[1,1,1]]).content_tableau([0,0,1]).pp()
                0  1     0  1     1
               -1                 0
                                 -1

        as with the content function the multicharge can be used to return the
        tableau containing the residues of the cells::

            sage: multicharge=[ IntegerModRing(3)(c) for c in [0,0,1] ]
            sage: PartitionTuple([[2,1],[2],[1,1,1]]).content_tableau(multicharge).pp()
                0  1     0  1     1
                2                 0
                                  2
        """
    def conjugate(self):
        """
        Return the conjugate partition tuple of ``self``.

        The conjugate partition tuple is obtained by reversing the order of the
        components and then swapping the rows and columns in each component.

        EXAMPLES::

            sage: PartitionTuple([[2,1],[1],[1,1,1]]).conjugate()
            ([3], [1], [2, 1])
        """
    def dominates(self, mu):
        """
        Return ``True`` if the PartitionTuple dominates or equals `\\mu` and
        ``False`` otherwise.

        Given partition tuples `\\mu=(\\mu^{(1)},...,\\mu^{(m)})` and `\\nu=(\\nu^{(1)},...,\\nu^{(n)})`
        then `\\mu` dominates `\\nu` if

        .. MATH::

            \\sum_{k=1}^{l-1} |\\mu^{(k)}| +\\sum_{r \\geq 1} \\mu^{(l)}_r
               \\geq \\sum_{k=1}^{l-1} |\\nu^{(k)}| + \\sum_{r \\geq 1} \\nu^{(l)}_r

        EXAMPLES::

            sage: mu=PartitionTuple([[1,1],[2],[2,1]])
            sage: nu=PartitionTuple([[1,1],[1,1],[2,1]])
            sage: mu.dominates(mu)
            True
            sage: mu.dominates(nu)
            True
            sage: nu.dominates(mu)
            False
            sage: tau=PartitionTuple([[],[2,1],[]])
            sage: tau.dominates([[2,1],[],[]])
            False
            sage: tau.dominates([[],[],[2,1]])
            True
        """
    @cached_method
    def initial_tableau(self):
        """
        Return the :class:`StandardTableauTuple` which has the numbers
        `1, 2, \\ldots, n`, where `n` is the :meth:`size` of ``self``,
        entered in order from left to right along the rows of each component,
        where the components are ordered from left to right.

        EXAMPLES::

            sage: PartitionTuple([ [2,1],[3,2] ]).initial_tableau()
            ([[1, 2], [3]], [[4, 5, 6], [7, 8]])
        """
    @cached_method
    def initial_column_tableau(self):
        """
        Return the initial column tableau of shape ``self``.

        The initial column tableau of shape `\\lambda` is the standard tableau
        that has the numbers `1` to `n`, where `n` is the :meth:`size`
        of `\\lambda`, entered in order from top to bottom, and then left
        to right, down the columns of each component, starting from the
        rightmost component and working to the left.

        EXAMPLES::

            sage: PartitionTuple([ [3,1],[3,2] ]).initial_column_tableau()
            ([[6, 8, 9], [7]], [[1, 3, 5], [2, 4]])
        """
    def garnir_tableau(self, *cell):
        '''
        Return the Garnir tableau of shape ``self`` corresponding to the cell
        ``cell``.

        If ``cell`` `= (k,a,c)` then `(k,a+1,c)` must belong to the diagram of
        the :class:`PartitionTuple`. If this is not the case then we return
        ``False``.

        .. NOTE::

            The function also sets ``g._garnir_cell`` equal to ``cell``
            which is used by some other functions.

        The Garnir tableaux play an important role in integral and
        non-semisimple representation theory because they determine the
        "straightening" rules for the Specht modules over an arbitrary ring.

        The Garnir tableau are the "first" non-standard tableaux which arise
        when you act by simple transpositions. If `(k,a,c)` is a cell in the
        Young diagram of a partition, which is not at the bottom of its
        column, then the corresponding Garnir tableau has the integers
        `1, 2, \\ldots, n` entered in order from left to right along the rows
        of the diagram up to the cell `(k,a,c-1)`, then along the cells
        `(k,a+1,1)` to `(k,a+1,c)`, then `(k,a,c)` until the end of row `a`
        and then continuing from left to right in the remaining positions.
        The examples below probably make this clearer!

        EXAMPLES::

            sage: PartitionTuple([[5,3],[2,2],[4,3]]).garnir_tableau((0,0,2)).pp()
                 1  2  6  7  8     9 10    13 14 15 16
                 3  4  5          11 12    17 18 19
            sage: PartitionTuple([[5,3,3],[2,2],[4,3]]).garnir_tableau((0,0,2)).pp()
                 1  2  6  7  8    12 13    16 17 18 19
                 3  4  5          14 15    20 21 22
                 9 10 11
            sage: PartitionTuple([[5,3,3],[2,2],[4,3]]).garnir_tableau((0,1,2)).pp()
                 1  2  3  4  5    12 13    16 17 18 19
                 6  7 11          14 15    20 21 22
                 8  9 10
            sage: PartitionTuple([[5,3,3],[2,2],[4,3]]).garnir_tableau((1,0,0)).pp()
                 1  2  3  4  5    13 14    16 17 18 19
                 6  7  8          12 15    20 21 22
                 9 10 11
            sage: PartitionTuple([[5,3,3],[2,2],[4,3]]).garnir_tableau((1,0,1)).pp()
                 1  2  3  4  5    12 15    16 17 18 19
                 6  7  8          13 14    20 21 22
                 9 10 11
            sage: PartitionTuple([[5,3,3],[2,2],[4,3]]).garnir_tableau((2,0,1)).pp()
                 1  2  3  4  5    12 13    16 19 20 21
                 6  7  8          14 15    17 18 22
                 9 10 11
            sage: PartitionTuple([[5,3,3],[2,2],[4,3]]).garnir_tableau((2,1,1)).pp()
            Traceback (most recent call last):
            ...
            ValueError: (comp, row+1, col) must be inside the diagram

        .. SEEALSO::

            - :meth:`top_garnir_tableau`
        '''
    def top_garnir_tableau(self, e, cell):
        '''
        Return the most dominant *standard* tableau which dominates the
        corresponding Garnir tableau and has the same residue that has shape
        ``self`` and is determined by ``e`` and ``cell``.

        The Garnir tableau play an important role in integral and
        non-semisimple representation theory because they determine the
        "straightening" rules for the Specht modules over an arbitrary ring.
        The *top Garnir tableaux* arise in the graded representation theory of
        the symmetric groups and higher level Hecke algebras. They were
        introduced in [KMR2012]_.

        If the Garnir node is ``cell=(k,r,c)`` and `m` and `M` are the entries
        in the cells ``(k,r,c)`` and ``(k,r+1,c)``, respectively, in the
        initial tableau then the top ``e``-Garnir tableau is obtained by
        inserting the numbers `m, m+1, \\ldots, M` in order from left to right
        first in the cells in row ``r+1`` which are not in the ``e``-Garnir
        belt, then in the cell in rows ``r`` and ``r+1`` which are in the
        Garnir belt and then, finally, in the remaining cells in row ``r``
        which are not in the Garnir belt. All other entries in the tableau
        remain unchanged.

        If ``e = 0``, or if there are no ``e``-bricks in either row ``r`` or
        ``r+1``, then the top Garnir tableau is the corresponding Garnir
        tableau.

        EXAMPLES::

            sage: PartitionTuple([[3,3,2],[5,4,3,2]]).top_garnir_tableau(2,(1,0,2)).pp()
                1  2  3     9 10 12 13 16
                4  5  6    11 14 15 17
                7  8       18 19 20
                           21 22
            sage: PartitionTuple([[3,3,2],[5,4,3,2]]).top_garnir_tableau(2,(1,0,1)).pp()
                1  2  3     9 10 11 12 13
                4  5  6    14 15 16 17
                7  8       18 19 20
                           21 22
            sage: PartitionTuple([[3,3,2],[5,4,3,2]]).top_garnir_tableau(3,(1,0,1)).pp()
                1  2  3     9 12 13 14 15
                4  5  6    10 11 16 17
                7  8       18 19 20
                           21 22

            sage: PartitionTuple([[3,3,2],[5,4,3,2]]).top_garnir_tableau(3,(3,0,1)).pp()
            Traceback (most recent call last):
            ...
            ValueError: (comp, row+1, col) must be inside the diagram

        .. SEEALSO::

            - :meth:`~sage.combinat.partition.Partition_tuple.garnir_tableau`
        '''
    def arm_length(self, k, r, c):
        """
        Return the length of the arm of cell ``(k, r, c)`` in ``self``.

        INPUT:

        - ``k`` -- the component
        - ``r`` -- the row
        - ``c`` -- the cell

        OUTPUT: the arm length as an integer

        The arm of cell ``(k, r, c)`` is the number of cells in the ``k``-th
        component which are to the right of the cell in row ``r`` and column
        ``c``.

        EXAMPLES::

            sage: PartitionTuple([[],[2,1],[2,2,1],[3]]).arm_length(2,0,0)
            1
            sage: PartitionTuple([[],[2,1],[2,2,1],[3]]).arm_length(2,0,1)
            0
            sage: PartitionTuple([[],[2,1],[2,2,1],[3]]).arm_length(2,2,0)
            0
        """
    def leg_length(self, k, r, c):
        """
        Return the length of the leg of cell ``(k, r, c)`` in ``self``.

        INPUT:

        - ``k`` -- the component
        - ``r`` -- the row
        - ``c`` -- the cell

        OUTPUT: the leg length as an integer

        The leg of cell ``(k, r, c)`` is the number of cells in the ``k``-th
        component which are below the node in row ``r`` and column ``c``.

        EXAMPLES::

            sage: PartitionTuple([[],[2,1],[2,2,1],[3]]).leg_length(2,0,0)
            2
            sage: PartitionTuple([[],[2,1],[2,2,1],[3]]).leg_length(2,0,1)
            1
            sage: PartitionTuple([[],[2,1],[2,2,1],[3]]).leg_length(2,2,0)
            0
        """
    def contains(self, mu):
        """
        Return ``True`` if this partition tuple contains `\\mu`.

        If `\\lambda=(\\lambda^{(1)}, \\ldots, \\lambda^{(l)})` and
        `\\mu=(\\mu^{(1)}, \\ldots, \\mu^{(m)})` are two partition tuples then
        `\\lambda` contains `\\mu` if `m \\leq l` and
        `\\mu^{(i)}_r \\leq \\lambda^{(i)}_r` for `1 \\leq i \\leq m` and `r \\geq 0`.

        EXAMPLES::

            sage: PartitionTuple([[1,1],[2],[2,1]]).contains( PartitionTuple([[1,1],[2],[2,1]]) )
            True
        """
    def hook_length(self, k, r, c):
        """
        Return the length of the hook of cell ``(k, r, c)`` in the partition.

        The hook of cell ``(k, r, c)`` is defined as the cells to the right or
        below (in the English convention). If your coordinates are in the
        form ``(k,r,c)``, use Python's \\*-operator.

        EXAMPLES::

            sage: mu=PartitionTuple([[1,1],[2],[2,1]])
            sage: [ mu.hook_length(*c) for c in mu.cells()]
            [2, 1, 2, 1, 3, 1, 1]
        """
    def to_exp(self, k: int = 0):
        """
        Return a tuple of the multiplicities of the parts of a partition.

        Use the optional parameter ``k`` to get a return list of length at
        least ``k``.

        EXAMPLES::

            sage: PartitionTuple([[1,1],[2],[2,1]]).to_exp()
            ([2], [0, 1], [1, 1])
            sage: PartitionTuple([[1,1],[2,2,2,2],[2,1]]).to_exp()
            ([2], [0, 4], [1, 1])
        """
    def removable_cells(self):
        """
        Return a list of the removable cells of this partition tuple.

        All indices are of the form ``(k, r, c)``, where ``r`` is the
        row-index, ``c`` is the column index and ``k`` is the component.

        EXAMPLES::

            sage: PartitionTuple([[1,1],[2],[2,1]]).removable_cells()
            [(0, 1, 0), (1, 0, 1), (2, 0, 1), (2, 1, 0)]
            sage: PartitionTuple([[1,1],[4,3],[2,1,1]]).removable_cells()
            [(0, 1, 0), (1, 0, 3), (1, 1, 2), (2, 0, 1), (2, 2, 0)]
        """
    corners = removable_cells
    def addable_cells(self):
        """
        Return a list of the removable cells of this partition tuple.

        All indices are of the form ``(k, r, c)``, where ``r`` is the
        row-index, ``c`` is the column index and ``k`` is the component.

        EXAMPLES::

            sage: PartitionTuple([[1,1],[2],[2,1]]).addable_cells()
            [(0, 0, 1), (0, 2, 0), (1, 0, 2), (1, 1, 0), (2, 0, 2), (2, 1, 1), (2, 2, 0)]
            sage: PartitionTuple([[1,1],[4,3],[2,1,1]]).addable_cells()
            [(0, 0, 1), (0, 2, 0), (1, 0, 4), (1, 1, 3), (1, 2, 0), (2, 0, 2), (2, 1, 1), (2, 3, 0)]
        """
    outside_corners = addable_cells
    def add_cell(self, k, r, c):
        """
        Return the partition tuple obtained by adding a cell in row ``r``,
        column ``c``, and component ``k``.

        This does not change ``self``.

        EXAMPLES::

            sage: PartitionTuple([[1,1],[4,3],[2,1,1]]).add_cell(0,0,1)
            ([2, 1], [4, 3], [2, 1, 1])
        """
    def remove_cell(self, k, r, c):
        """
        Return the partition tuple obtained by removing a cell in row ``r``,
        column ``c``, and component ``k``.

        This does not change ``self``.

        EXAMPLES::

            sage: PartitionTuple([[1,1],[4,3],[2,1,1]]).remove_cell(0,1,0)
            ([1], [4, 3], [2, 1, 1])
        """
    def to_list(self):
        """
        Return ``self`` as a list of lists.

        EXAMPLES::

            sage: PartitionTuple([[1,1],[4,3],[2,1,1]]).to_list()
            [[1, 1], [4, 3], [2, 1, 1]]

        TESTS::

            sage: all(mu==PartitionTuple(mu.to_list()) for mu in PartitionTuples(4,4))  # needs sage.libs.flint
            True
        """
    def young_subgroup(self):
        """
        Return the corresponding Young, or parabolic, subgroup of the
        symmetric group.

        EXAMPLES::

            sage: PartitionTuple([[2,1],[4,2],[1]]).young_subgroup()                    # needs sage.groups
            Permutation Group with generators [(), (8,9), (6,7), (5,6), (4,5), (1,2)]
        """
    def young_subgroup_generators(self):
        """
        Return an indexing set for the generators of the corresponding Young
        subgroup.

        EXAMPLES::

            sage: PartitionTuple([[2,1],[4,2],[1]]).young_subgroup_generators()
            [1, 4, 5, 6, 8]
        """
    def degree(self, e):
        '''
        Return the ``e``-th degree of ``self``.

        The `e`-th degree is the sum of the degrees of the standard
        tableaux of shape `\\lambda`. The `e`-th degree is the exponent
        of `\\Phi_e(q)` in the Gram determinant of the Specht module for a
        semisimple cyclotomic Hecke algebra of type `A` with parameter `q`.

        For this calculation the multicharge `(\\kappa_1, \\ldots, \\kappa_l)`
        is chosen so that `\\kappa_{r+1} - \\kappa_r > n`, where `n` is
        the :meth:`size` of `\\lambda` as this ensures that the Hecke algebra
        is semisimple.

        INPUT:

        - ``e`` -- integer `e > 1`

        OUTPUT: nonnegative integer

        EXAMPLES::

            sage: PartitionTuple([[2,1],[2,2]]).degree(2)
            532
            sage: PartitionTuple([[2,1],[2,2]]).degree(3)
            259
            sage: PartitionTuple([[2,1],[2,2]]).degree(4)
            196
            sage: PartitionTuple([[2,1],[2,2]]).degree(5)
            105
            sage: PartitionTuple([[2,1],[2,2]]).degree(6)
            105
            sage: PartitionTuple([[2,1],[2,2]]).degree(7)
            0

        Therefore,  the Gram determinant of `S(2,1|2,2)` when the Hecke parameter
        `q` is "generic" is

        .. MATH::

            q^N \\Phi_2(q)^{532}\\Phi_3(q)^{259}\\Phi_4(q)^{196}\\Phi_5(q)^{105}\\Phi_6(q)^{105}

        for some integer `N`.  Compare with :meth:`prime_degree`.
        '''
    def prime_degree(self, p):
        """
        Return the ``p``-th prime degree of ``self``.

        The degree of a partition `\\lambda` is the sum of the `e`-degrees`
        of the standard tableaux of shape `\\lambda` (see :meth:`degree`),
        for `e` a power of the prime `p`. The prime degree gives the
        exponent of `p` in the Gram determinant of the integral Specht
        module of the symmetric group.

        The `p`-th degree is the sum of the degrees of the standard tableaux
        of shape `\\lambda`. The `p`-th degree is the exponent of `p` in the
        Gram determinant of a semisimple cyclotomic Hecke algebra of type `A`
        with parameter `q = 1`.

        As with :meth:`degree`, for this calculation the multicharge
        `(\\kappa_1, \\ldots, \\kappa_l)` is chosen so that
        `\\kappa_{r+1} - \\kappa_r > n`, where `n` is the :meth:`size`
        of `\\lambda` as this ensures that the Hecke algebra is semisimple.

        INPUT:

        - ``e`` -- an  integer `e > 1`
        - ``multicharge`` -- an `l`-tuple of integers, where `l` is
          the :meth:`level` of ``self``

        OUTPUT: nonnegative integer

        EXAMPLES::

            sage: PartitionTuple([[2,1],[2,2]]).prime_degree(2)
            728
            sage: PartitionTuple([[2,1],[2,2]]).prime_degree(3)
            259
            sage: PartitionTuple([[2,1],[2,2]]).prime_degree(5)
            105
            sage: PartitionTuple([[2,1],[2,2]]).prime_degree(7)
            0

        Therefore, the Gram determinant of `S(2,1|2,2)` when `q=1` is
        `2^{728} 3^{259}5^{105}`. Compare with :meth:`degree`.
        """
    @cached_method
    def block(self, e, multicharge):
        """
        Return a dictionary `\\beta` that determines the block associated to
        the partition ``self`` and the
        :meth:`~sage.combinat.tableau_residues.ResidueSequence.quantum_characteristic` ``e``.

        INPUT:

        - ``e`` -- the quantum characteristic

        - ``multicharge`` -- the multicharge (default: `(0,)`)

        OUTPUT:

        - a dictionary giving the multiplicities of the residues in the
          partition tuple ``self``

        In more detail, the value ``beta[i]`` is equal to the
        number of nodes of residue ``i``. This corresponds to
        the positive root

        .. MATH::

            \\sum_{i\\in I} \\beta_i \\alpha_i \\in Q^+,

        a element of the positive root lattice of the corresponding
        Kac-Moody algebra. See [DJM1998]_ and [BK2009]_ for more details.

        This is a useful statistics because two Specht modules for a cyclotomic
        Hecke algebra of type `A` belong to the same block if and only if they
        correspond to same element `\\beta` of the root lattice, given above.

        We return a dictionary because when the quantum characteristic is `0`,
        the Cartan type is `A_{\\infty}`, in which case the simple roots are
        indexed by the integers.

        EXAMPLES::

            sage: PartitionTuple([[2,2],[2,2]]).block(0,(0,0))
            {-1: 2, 0: 4, 1: 2}
            sage: PartitionTuple([[2,2],[2,2]]).block(2,(0,0))
            {0: 4, 1: 4}
            sage: PartitionTuple([[2,2],[2,2]]).block(2,(0,1))
            {0: 4, 1: 4}
            sage: PartitionTuple([[2,2],[2,2]]).block(3,(0,2))
            {0: 3, 1: 2, 2: 3}
            sage: PartitionTuple([[2,2],[2,2]]).block(3,(0,2))
            {0: 3, 1: 2, 2: 3}
            sage: PartitionTuple([[2,2],[2,2]]).block(3,(3,2))
            {0: 3, 1: 2, 2: 3}
            sage: PartitionTuple([[2,2],[2,2]]).block(4,(0,0))
            {0: 4, 1: 2, 3: 2}
        """
    def defect(self, e, multicharge):
        """
        Return the ``e``-defect or the ``e``-weight ``self``.

        The `e`-defect is the number of (connected) `e`-rim hooks
        that can be removed from the partition.

        The defect of a partition tuple is given by

        .. MATH::

            \\text{defect}(\\beta) = (\\Lambda, \\beta) - \\tfrac12(\\beta, \\beta),

        where `\\Lambda = \\sum_r \\Lambda_{\\kappa_r}` for the multicharge
        `(\\kappa_1, \\ldots, \\kappa_{\\ell})` and
        `\\beta = \\sum_{(r,c)} \\alpha_{(c-r) \\pmod e}`, with the sum
        being over the cells in the partition.

        INPUT:

        - ``e`` -- the quantum characteristic

        - ``multicharge`` -- the multicharge (default: `(0,)`)

        OUTPUT: a nonnegative integer, which is the defect of the block
        containing the partition tuple ``self``

        EXAMPLES::

            sage: PartitionTuple([[2,2],[2,2]]).defect(0,(0,0))
            0
            sage: PartitionTuple([[2,2],[2,2]]).defect(2,(0,0))
            8
            sage: PartitionTuple([[2,2],[2,2]]).defect(2,(0,1))
            8
            sage: PartitionTuple([[2,2],[2,2]]).defect(3,(0,2))
            5
            sage: PartitionTuple([[2,2],[2,2]]).defect(3,(0,2))
            5
            sage: PartitionTuple([[2,2],[2,2]]).defect(3,(3,2))
            2
            sage: PartitionTuple([[2,2],[2,2]]).defect(4,(0,0))
            0
        """

class PartitionTuples(UniqueRepresentation, Parent):
    """
    Class of all partition tuples.

    For more information about partition tuples, see :class:`PartitionTuple`.

    This is a factory class which returns the appropriate parent based on
    the values of ``level``, ``size``, and ``regular``

    INPUT:

    - ``level`` -- the length of the tuple

    - ``size`` -- the total number of cells

    - ``regular`` -- positive integer or a tuple of nonnegative
      integers; if an integer, the highest multiplicity an entry may
      have in a component plus `1`

    If a level `k` is specified and ``regular`` is a tuple of integers
    `\\ell_1, \\ldots, \\ell_k`, then this specifies partition tuples `\\mu`
    such that `\\mu_i` is `\\ell_i`-regular, where `0` here
    represents `\\infty`-regular partitions (equivalently, partitions
    without restrictions). If ``regular`` is an integer `\\ell`, then
    we set `\\ell_i = \\ell` for all `i`.

    TESTS::

        sage: [ [2,1],[],[3] ] in PartitionTuples()
        True
        sage: ( [2,1],[],[3] ) in PartitionTuples()
        True
        sage: ( [] ) in PartitionTuples()
        True
        sage: PartitionTuples(level=1, regular=(0,))
        Partitions
        sage: PartitionTuples(level=1, size=3, regular=(0,))
        Partitions of the integer 3

    Check that :issue:`14145` has been fixed::

        sage: 1 in PartitionTuples()
        False
    """
    @staticmethod
    def __classcall_private__(klass, level=None, size=None, regular=None):
        """
        Return the correct parent object based upon the input.

        TESTS::

            sage: PartitionTuples()
            Partition tuples
            sage: PartitionTuples(3)
            Partition tuples of level 3
            sage: PartitionTuples(size=3)
            Partition tuples of size 3
            sage: PartitionTuples(3,8)
            Partition tuples of level 3 and size 8
            sage: PartitionTuples(level=3, regular=(0,2,4))
            (0, 2, 4)-Regular partition tuples of level 3
            sage: PartitionTuples(level=1,regular=(4,)) is PartitionTuples(level=1, regular=4)
            True
        """
    Element = PartitionTuple
    options = Partitions.options
    def __contains__(self, mu) -> bool:
        """
        Return ``True`` if `\\mu` is in ``self``.

        TESTS::

            sage: PartitionTuple([[3,2],[2]]) in PartitionTuples()
            True
            sage: PartitionTuple([[3,2],[],[],[],[2]]) in PartitionTuples()
            True
            sage: PartitionTuple([[2,1],[],[1,1],[],[2]]) in PartitionTuples()
            True
            sage: PartitionTuple([[2,1],[],[1,1],[],[3]]) in PartitionTuples()
            True
            sage: all(mu in PartitionTuples() for mu in PartitionTuples(3,8))           # needs sage.libs.flint
            True
            sage: [5,1,1] in PartitionTuples()
            True
            sage: [[5,1,1]] in PartitionTuples()
            True
            sage: la = Partition([3,3,1])
            sage: PT = PartitionTuples()
            sage: la in PT
            True
            sage: PT(la)
            ([3, 3, 1])

        Check that :issue:`14145` is fixed::

            sage: 1 in PartitionTuples()
            False
        """
    def __getitem__(self, r):
        """
        The default implementation of ``__getitem__()`` for enumerated sets
        does not allow slices, so we override it.

        EXAMPLES::

            sage: PartitionTuples()[10:20]                                              # needs sage.libs.flint
            [([1, 1, 1]),
             ([2], []),
             ([1, 1], []),
             ([1], [1]),
             ([], [2]),
             ([], [1, 1]),
             ([1], [], []),
             ([], [1], []),
             ([], [], [1]),
             ([], [], [], [])]
        """
    def level(self):
        """
        Return the level or ``None`` if it is not defined.

        EXAMPLES::

            sage: PartitionTuples().level() is None
            True
            sage: PartitionTuples(7).level()
            7
        """
    def size(self):
        """
        Return the size or ``None`` if it is not defined.

        EXAMPLES::

            sage: PartitionTuples().size() is None
            True
            sage: PartitionTuples(size=7).size()
            7
        """

class PartitionTuples_all(PartitionTuples):
    """
    Class of partition tuples of a arbitrary level and arbitrary sum.
    """
    def __init__(self) -> None:
        """
        Initialize the class.

        EXAMPLES::

            sage: TestSuite( PartitionTuples() ).run()                                  # needs sage.libs.flint
        """
    def __iter__(self):
        """
        Iterate through the infinite class of partition tuples of arbitrary
        level and size.

        EXAMPLES::

            sage: PartitionTuples()[:20]                                                # needs sage.libs.flint
            [([]),
             ([1]),
             ([], []),
             ([2]),
             ([1, 1]),
             ([1], []),
             ([], [1]),
             ([], [], []),
             ([3]),
             ([2, 1]),
             ([1, 1, 1]),
             ([2], []),
             ([1, 1], []),
             ([1], [1]),
             ([], [2]),
             ([], [1, 1]),
             ([1], [], []),
             ([], [1], []),
             ([], [], [1]),
             ([], [], [], [])]
        """

class PartitionTuples_level(PartitionTuples):
    """
    Class of partition tuples of a fixed level, but summing to an arbitrary
    integer.
    """
    def __init__(self, level, category=None) -> None:
        """
        Initialize this class.

        EXAMPLES::

            sage: PartitionTuples(4)
            Partition tuples of level 4
            sage: PartitionTuples(level=6)
            Partition tuples of level 6
            sage: TestSuite( PartitionTuples(level=4) ).run()                           # needs sage.libs.flint
        """
    def __contains__(self, mu) -> bool:
        """
        Return ``True`` if `\\mu` is in ``self``.

        TESTS::

            sage: PartitionTuple([[3,2],[2]]) in PartitionTuples(2)
            True
            sage: PartitionTuple([[3,2],[2]]) in PartitionTuples(level=2)
            True
            sage: PartitionTuple([[2,2,1],[2]]) in PartitionTuples(level=2)
            True
            sage: PartitionTuple([[2,2,1],[],[2]]) in PartitionTuples(level=2)
            False
            sage: all(mu in PartitionTuples(3) for mu in PartitionTuples(3,8))          # needs sage.libs.flint
            True

        Check that :issue:`14145` is fixed::

            sage: 1 in PartitionTuples(level=2)
            False
        """
    def __iter__(self):
        """
        Iterate through the infinite class of partition tuples of fixed level.

        EXAMPLES::

            sage: parts = PartitionTuples(3)
            sage: [parts[k] for k in range(20)]                                         # needs sage.libs.flint
            [([], [], []),
             ([1], [], []),
             ([], [1], []),
             ([], [], [1]),
             ([2], [], []),
             ([1, 1], [], []),
             ([1], [1], []),
             ([1], [], [1]),
             ([], [2], []),
             ([], [1, 1], []),
             ([], [1], [1]),
             ([], [], [2]),
             ([], [], [1, 1]),
             ([3], [], []),
             ([2, 1], [], []),
             ([1, 1, 1], [], []),
             ([2], [1], []),
             ([1, 1], [1], []),
             ([2], [], [1]),
             ([1, 1], [], [1])]
        """

class PartitionTuples_size(PartitionTuples):
    """
    Class of partition tuples of a fixed size, but arbitrary level.
    """
    def __init__(self, size) -> None:
        """
        Initialize this class.

        EXAMPLES::

            sage: PartitionTuples(size=4)
            Partition tuples of size 4
            sage: PartitionTuples(size=6)
            Partition tuples of size 6

            sage: TestSuite( PartitionTuples(size=6) ).run()                            # needs sage.libs.flint
        """
    def __contains__(self, mu) -> bool:
        """
        Return ``True`` if `\\mu` is in ``self``.

        TESTS::

            sage: PartitionTuple([[3,2],[2]]) in PartitionTuples(size=7)
            True
            sage: PartitionTuple([[3,2],[],[],[],[2]]) in PartitionTuples(size=7)
            True
            sage: PartitionTuple([[2,1],[],[1,1],[],[2]]) in PartitionTuples(size=7)
            True
            sage: PartitionTuple([[2,1],[],[1,1],[],[3]]) in PartitionTuples(size=7)
            False
            sage: all(mu in PartitionTuples(size=8) for mu in PartitionTuples(3,8))     # needs sage.libs.flint
            True
            sage: [3, 2, 1] in PartitionTuples(size=7)
            False

        Check that :issue:`14145` is fixed::

            sage: 1 in PartitionTuples(size=7)
            False
        """
    def __iter__(self):
        """
        Iterate through the infinite class of partition tuples of a fixed size.

        EXAMPLES::

            sage: PartitionTuples(size=3)[:20]                                          # needs sage.libs.flint
            [([3]),
             ([2, 1]),
             ([1, 1, 1]),
             ([3], []),
             ([2, 1], []),
             ([1, 1, 1], []),
             ([2], [1]),
             ([1, 1], [1]),
             ([1], [2]),
             ([1], [1, 1]),
             ([], [3]),
             ([], [2, 1]),
             ([], [1, 1, 1]),
             ([3], [], []),
             ([2, 1], [], []),
             ([1, 1, 1], [], []),
             ([2], [1], []),
             ([1, 1], [1], []),
             ([2], [], [1]),
             ([1, 1], [], [1])]
        """

class PartitionTuples_level_size(PartitionTuples):
    """
    Class of partition tuples with a fixed level and a fixed size.
    """
    def __init__(self, level, size) -> None:
        """
        Initialize this class.

        EXAMPLES::

            sage: TestSuite( PartitionTuples(4,2) ).run()                               # needs sage.libs.flint sage.libs.pari
            sage: TestSuite( PartitionTuples(level=4, size=5) ).run()                   # needs sage.libs.flint sage.libs.pari
        """
    def __contains__(self, mu) -> bool:
        """
        Return ``True`` if ``mu`` is in ``self``.

        TESTS::

            sage: PartitionTuple([[3,2],[2]]) in PartitionTuples(2,7)
            True
            sage: PartitionTuple([[3,2],[],[],[],[2]]) in PartitionTuples(5,7)
            True
            sage: PartitionTuple([[2,1],[],[1,1],[],[2]]) in PartitionTuples(5,7)
            True
            sage: PartitionTuple([[2,1],[],[1,1],[],[3]]) in PartitionTuples(2,8)
            False
            sage: all(mu in PartitionTuples(3,8) for mu in PartitionTuples(3,8))        # needs sage.libs.flint
            True

        Check that :issue:`14145` is fixed::

            sage: 1 in PartitionTuples(5,7)
            False
        """
    def __iter__(self):
        """
        Iterate through the finite class of partition tuples of a fixed level
        and a fixed size.

        EXAMPLES::

            sage: # needs sage.libs.flint
            sage: PartitionTuples(2,0).list() #indirect doctest
            [([], [])]
            sage: PartitionTuples(2,1).list() #indirect doctest
            [([1], []), ([], [1])]
            sage: PartitionTuples(2,2).list() #indirect doctest
            [([2], []), ([1, 1], []), ([1], [1]), ([], [2]), ([], [1, 1])]
            sage: PartitionTuples(3,2).list() #indirect doctest
            [([2], [], []),
             ([1, 1], [], []),
             ([1], [1], []),
             ([1], [], [1]),
             ([], [2], []),
             ([], [1, 1], []),
             ([], [1], [1]),
             ([], [], [2]),
             ([], [], [1, 1])]
        """
    def cardinality(self):
        """
        Return the number of ``level``-tuples of partitions of size ``n``.

        Wraps a pari function call using :pari:`eta`.

        EXAMPLES::

            sage: PartitionTuples(2,3).cardinality()                                    # needs sage.libs.pari
            10
            sage: PartitionTuples(2,8).cardinality()                                    # needs sage.libs.pari
            185

        TESTS:

        The following calls used to fail (:issue:`11476`)::

            sage: # needs sage.libs.pari
            sage: PartitionTuples(17,2).cardinality()
            170
            sage: PartitionTuples(2,17).cardinality()
            8470
            sage: PartitionTuples(100,13).cardinality()
            110320020147886800
            sage: PartitionTuples(13,90).cardinality()
            91506473741200186152352843611

        These answers were checked against Gap4 (the last of which takes an
        awful long time for gap to compute).
        """

class RegularPartitionTuples(PartitionTuples):
    """
    Abstract base class for `\\ell`-regular partition tuples.
    """
    def __init__(self, regular, **kwds) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: RPT = PartitionTuples(regular=3)
            sage: TestSuite(RPT).run()                                                  # needs sage.libs.flint
        """
    def __contains__(self, mu) -> bool:
        """
        Check if ``mu`` is an `\\ell`-regular partition tuple.

        TESTS::

            sage: RPT = PartitionTuples(regular=2)
            sage: [[11,1], [2]] in RPT
            True
            sage: Partition([4,1]) in RPT
            True
            sage: [5,4,3,2,1] in RPT
            True
            sage: [[6,3,1], [], [], [3,1], [1], [1], [1]] in RPT
            True
            sage: [[10], [1], [1,1], [4,2]] in RPT
            False
            sage: [[5,2], [17, 1], [], [3,3,1], [1,1]] in RPT
            False
            sage: RPT = PartitionTuples(4,2,3)
            sage: elt = RPT([[1], [], [], [1]])
            sage: elt in RPT
            True
        """

class RegularPartitionTuples_all(RegularPartitionTuples):
    """
    Class of `\\ell`-regular partition tuples.
    """
    def __init__(self, regular) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: RPT = PartitionTuples(regular=3)
            sage: TestSuite(RPT).run()                                                  # needs sage.libs.flint
        """
    def __iter__(self):
        """
        Iterate through the class of `\\ell`-regular partition tuples.

        EXAMPLES::

            sage: PartitionTuples(regular=2)[:20]                                       # needs sage.libs.flint
            [([]),
             ([], []),
             ([1]),
             ([], [], []),
             ([1], []),
             ([], [1]),
             ([2]),
             ([], [], [], []),
             ([1], [], []),
             ([], [1], []),
             ([], [], [1]),
             ([2], []),
             ([1], [1]),
             ([], [2]),
             ([3]),
             ([2, 1]),
             ([], [], [], [], []),
             ([1], [], [], []),
             ([], [1], [], []),
             ([], [], [1], [])]
        """

class RegularPartitionTuples_level(PartitionTuples_level):
    """
    Regular Partition tuples of a fixed level.

    INPUT:

    - ``level`` -- nonnegative integer; the level
    - ``regular`` -- positive integer or a tuple of nonnegative
      integers; if an integer, the highest multiplicity an entry may
      have in a component plus `1` with `0` representing `\\infty`-regular
      (equivalently, partitions without restrictions)

    ``regular`` is a tuple of integers `(\\ell_1, \\ldots, \\ell_k)` that
    specifies partition tuples `\\mu` such that `\\mu_i` is `\\ell_i`-regular.
    If ``regular`` is an integer `\\ell`, then we set `\\ell_i = \\ell` for
    all `i`.

    EXAMPLES::

        sage: RPT = PartitionTuples(level=4, regular=(2,3,0,2))
        sage: RPT[:24]                                                                  # needs sage.libs.flint
        [([], [], [], []),
         ([1], [], [], []),
         ([], [1], [], []),
         ([], [], [1], []),
         ([], [], [], [1]),
         ([2], [], [], []),
         ([1], [1], [], []),
         ([1], [], [1], []),
         ([1], [], [], [1]),
         ([], [2], [], []),
         ([], [1, 1], [], []),
         ([], [1], [1], []),
         ([], [1], [], [1]),
         ([], [], [2], []),
         ([], [], [1, 1], []),
         ([], [], [1], [1]),
         ([], [], [], [2]),
         ([3], [], [], []),
         ([2, 1], [], [], []),
         ([2], [1], [], []),
         ([2], [], [1], []),
         ([2], [], [], [1]),
         ([1], [2], [], []),
         ([1], [1, 1], [], [])]
        sage: [[1,1],[3],[5,5,5],[7,2]] in RPT
        False
        sage: [[3,1],[3],[5,5,5],[7,2]] in RPT
        True
        sage: [[3,1],[3],[5,5,5]] in RPT
        False
    """
    def __init__(self, level, regular) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: RPT = PartitionTuples(level=2, regular=(0,0))
            sage: RPT.category()
            Category of infinite enumerated sets
            sage: RPT = PartitionTuples(level=4, regular=3)
            sage: TestSuite(RPT).run()                                                  # needs sage.libs.flint
        """
    def __contains__(self, mu) -> bool:
        """
        Return ``True`` if ``mu`` is in ``self``.

        TESTS::

            sage: RPT = PartitionTuples(level=4, regular=2)
            sage: [[4,2,1], [], [2], [2]] in RPT
            True
            sage: [[10], [1], [1,1], [4,2]] in RPT
            False
            sage: [[5,2], [], [3,3,1], [1,1]] in RPT
            False
            sage: [4, 3, 2] in RPT
            False

            sage: RPT = PartitionTuples(level=3, regular=(2,1,4))
            sage: [[4], [2], [5]] in RPT
            False
            sage: [[4], [], [5]] in RPT
            True
            sage: [[4,3], [], [5]] in RPT
            True
            sage: [[4,4], [], [5]] in RPT
            False
            sage: [[4,3], [5]] in RPT
            False
            sage: [5, 4, 3] in RPT
            False
            sage: [] in RPT
            False
            sage: [[], [], []] in RPT
            True
            sage: [[], [], [], [2]] in RPT
            False

            sage: from sage.combinat.partition_tuple import RegularPartitionTuples_level
            sage: RPT = RegularPartitionTuples_level(1, (3,)); RPT
            3-Regular partition tuples of level 1
            sage: [[2,2]] in RPT
            True
            sage: [[2,2,2]] in RPT
            False
        """
    def __iter__(self):
        """
        Iterate through the class of `\\ell`-regular partition tuples
        of a fixed level.

        EXAMPLES::

            sage: PartitionTuples(level=3, regular=(2,1,4))[:24]                        # needs sage.libs.flint
            [([], [], []),
             ([1], [], []),
             ([], [], [1]),
             ([2], [], []),
             ([1], [], [1]),
             ([], [], [2]),
             ([], [], [1, 1]),
             ([3], [], []),
             ([2, 1], [], []),
             ([2], [], [1]),
             ([1], [], [2]),
             ([1], [], [1, 1]),
             ([], [], [3]),
             ([], [], [2, 1]),
             ([], [], [1, 1, 1]),
             ([4], [], []),
             ([3, 1], [], []),
             ([3], [], [1]),
             ([2, 1], [], [1]),
             ([2], [], [2]),
             ([2], [], [1, 1]),
             ([1], [], [3]),
             ([1], [], [2, 1]),
             ([1], [], [1, 1, 1])]
            sage: PartitionTuples(level=4, regular=2)[:20]                              # needs sage.libs.flint
            [([], [], [], []),
             ([1], [], [], []),
             ([], [1], [], []),
             ([], [], [1], []),
             ([], [], [], [1]),
             ([2], [], [], []),
             ([1], [1], [], []),
             ([1], [], [1], []),
             ([1], [], [], [1]),
             ([], [2], [], []),
             ([], [1], [1], []),
             ([], [1], [], [1]),
             ([], [], [2], []),
             ([], [], [1], [1]),
             ([], [], [], [2]),
             ([3], [], [], []),
             ([2, 1], [], [], []),
             ([2], [1], [], []),
             ([2], [], [1], []),
             ([2], [], [], [1])]
        """

class RegularPartitionTuples_size(RegularPartitionTuples):
    """
    Class of `\\ell`-regular partition tuples with a fixed size.
    """
    def __init__(self, size, regular) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: RPT = PartitionTuples(size=4, regular=3)
            sage: TestSuite(RPT).run()                                                  # needs sage.libs.flint
        """
    def __contains__(self, mu) -> bool:
        """
        Return ``True`` if ``mu`` is in ``self``.

        TESTS::

            sage: RPT = PartitionTuples(size=4, regular=2)
            sage: [[2, 1], [1]] in RPT
            True
            sage: [3, 1] in RPT
            True
            sage: [[1], [], [], [2,1]] in RPT
            True
            sage: [[1], [1], [1], [1]] in RPT
            True
            sage: [[1], [1,1,1]] in RPT
            False
            sage: [[2,1,1]] in RPT
            False
            sage: [2,1,1] in RPT
            False
            sage: RPT = PartitionTuples(size=7, regular=2)
            sage: [[], [3,2,2,1], [1], [1]] in RPT
            False
            sage: RPT = PartitionTuples(size=9, regular=2)
            sage: [4, 3, 2] in RPT
            True
        """
    def __iter__(self):
        """
        Iterate through the class of `\\ell`-regular partition tuples
        of a fixed size.

        EXAMPLES::

            sage: PartitionTuples(size=4, regular=2)[:10]                               # needs sage.libs.flint
            [([4]),
             ([3, 1]),
             ([4], []),
             ([3, 1], []),
             ([3], [1]),
             ([2, 1], [1]),
             ([2], [2]),
             ([1], [3]),
             ([1], [2, 1]),
             ([], [4])]
        """

class RegularPartitionTuples_level_size(PartitionTuples_level_size):
    """
    Class of `\\ell`-regular partition tuples with a fixed level and
    a fixed size.

    INPUT:

    - ``level`` -- nonnegative integer; the level
    - ``size`` -- nonnegative integer; the size
    - ``regular`` -- positive integer or a tuple of nonnegative
      integers; if an integer, the highest multiplicity an entry may
      have in a component plus `1` with `0` representing `\\infty`-regular
      (equivalently, partitions without restrictions)

    ``regular`` is a tuple of integers `(\\ell_1, \\ldots, \\ell_k)` that
    specifies partition tuples `\\mu` such that `\\mu_i` is `\\ell_i`-regular.
    If ``regular`` is an integer `\\ell`, then we set `\\ell_i = \\ell` for
    all `i`.

    EXAMPLES::

        sage: PartitionTuples(level=3, size=7, regular=(2,1,3))[0:24]                   # needs sage.libs.flint
        [([7], [], []),
         ([6, 1], [], []),
         ([5, 2], [], []),
         ([4, 3], [], []),
         ([4, 2, 1], [], []),
         ([6], [], [1]),
         ([5, 1], [], [1]),
         ([4, 2], [], [1]),
         ([3, 2, 1], [], [1]),
         ([5], [], [2]),
         ([5], [], [1, 1]),
         ([4, 1], [], [2]),
         ([4, 1], [], [1, 1]),
         ([3, 2], [], [2]),
         ([3, 2], [], [1, 1]),
         ([4], [], [3]),
         ([4], [], [2, 1]),
         ([3, 1], [], [3]),
         ([3, 1], [], [2, 1]),
         ([3], [], [4]),
         ([3], [], [3, 1]),
         ([3], [], [2, 2]),
         ([3], [], [2, 1, 1]),
         ([2, 1], [], [4])]
    """
    def __init__(self, level, size, regular) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: RPT = PartitionTuples(4,2,3)
            sage: TestSuite(RPT).run()                                                  # needs sage.libs.flint sage.libs.pari
        """
    def __contains__(self, mu) -> bool:
        """
        Return ``True`` if `\\mu` is in ``self``.

        TESTS::

            sage: RPT = PartitionTuples(level=3, size=7, regular=(2,1,4))
            sage: RPT
            (2, 1, 4)-Regular partition tuples of level 3 and size 7
            sage: [[3,1],[],[3]] in RPT
            True
            sage: [[3],[1],[3]] in RPT
            False
            sage: [[3,2],[],[3]] in RPT
            False
            sage: [[3,3],[],[1]] in RPT
            False
            sage: RPT = PartitionTuples(4,3,2)
            sage: [[], [], [2], [1]] in RPT
            True
            sage: [[1], [1], [], [1]] in RPT
            True
            sage: [[1,1,1], [], [], []] in RPT
            False
            sage: RPT = PartitionTuples(9, 3, 2)
            sage: [4, 3, 2] in RPT
            False
        """
    def __iter__(self):
        """
        Iterate through the finite class of `\\ell`-regular partition tuples
        of a fixed level and a fixed size.

        EXAMPLES::

            sage: list(PartitionTuples(3,3,2))                                          # needs sage.libs.pari
            [([3], [], []),
             ([2, 1], [], []),
             ([2], [1], []),
             ([2], [], [1]),
             ([1], [2], []),
             ([1], [1], [1]),
             ([1], [], [2]),
             ([], [3], []),
             ([], [2, 1], []),
             ([], [2], [1]),
             ([], [1], [2]),
             ([], [], [3]),
             ([], [], [2, 1])]
        """
