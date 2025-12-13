from .partition import Partition as Partition, Partitions as Partitions
from .partition_tuple import PartitionTuple as PartitionTuple, PartitionTuples as PartitionTuples
from _typeshed import Incomplete
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.categories.infinite_enumerated_sets import InfiniteEnumeratedSets as InfiniteEnumeratedSets
from sage.cpython.getattr import getattr_from_other_class as getattr_from_other_class
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as IntegerModRing
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.semirings.non_negative_integer_semiring import NN as NN

class KleshchevPartition(Partition):
    """
    Abstract base class for Kleshchev partitions. See
    :class:`~KleshchevPartitions`.
    """
    def conormal_cells(self, i=None):
        """
        Return a dictionary of the cells of ``self`` which are conormal.

        Following [Kle1995]_, the *conormal* cells are computed by
        reading up (or down) the rows of the partition and marking all
        of the addable and removable cells of `e`-residue `i` and then
        recursively removing all adjacent pairs of removable and addable
        cells (in that order) from this list. The addable `i`-cells that
        remain at the end of the this process are the conormal `i`-cells.

        When computing conormal cells you can either read the cells in order
        from top to bottom (this corresponds to labeling the simple modules
        of the symmetric group by regular partitions) or from bottom to top
        (corresponding to labeling the simples by restricted partitions).
        By default we read down the partition but this can be changed by
        setting ``convention = 'RS'``.

        INPUT:

        - ``i`` -- (optional) a residue

        OUTPUT:

        If no residue ``i`` is specified then a dictionary of conormal cells
        is returned, which gives the conormal cells for ``0 <= i < e``.

        EXAMPLES::

            sage: KP = KleshchevPartitions(3, convention='regular')
            sage: KP([5,4,4,3,2]).conormal_cells()
            {0: [(1, 4)], 1: [(5, 0), (4, 2)]}
            sage: KP([5,4,4,3,2]).conormal_cells(0)
            [(1, 4)]
            sage: KP([5,4,4,3,2]).conormal_cells(1)
            [(5, 0), (4, 2)]
            sage: KP = KleshchevPartitions(3, convention='restricted')
            sage: KP([5,4,4,3,2]).conormal_cells()
            {0: [(1, 4), (3, 3)], 2: [(0, 5)]}
        """
    def cogood_cells(self, i=None):
        """
        Return a list of the cells of ``self`` that are cogood.

        The cogood `i`-cell is the 'last' conormal `i`-cell. As with the
        conormal cells we can choose to read either up or down the partition as
        specified by :meth:`~KleshchevPartitions.convention`.

        INPUT:

        - ``i`` -- (optional) a residue

        OUTPUT:

        If no residue ``i`` is specified then a dictionary of cogood cells
        is returned, which gives the cogood cells for ``0 <= i < e``.

        EXAMPLES::

            sage: KP = KleshchevPartitions(3, convention='regular')
            sage: KP([5,4,4,3,2]).cogood_cells()
            {0: (1, 4), 1: (4, 2)}
            sage: KP([5,4,4,3,2]).cogood_cells(0)
            (1, 4)
            sage: KP([5,4,4,3,2]).cogood_cells(1)
            (4, 2)
            sage: KP = KleshchevPartitions(4, convention='restricted')
            sage: KP([5,4,4,3,2]).cogood_cells()
            {1: (0, 5), 2: (4, 2), 3: (1, 4)}
            sage: KP([5,4,4,3,2]).cogood_cells(0)
            sage: KP([5,4,4,3,2]).cogood_cells(2)
            (4, 2)
        """
    def normal_cells(self, i=None):
        """
        Return a dictionary of the cells of the partition that are normal.

        Following [Kle1995]_, the *normal* cells are computed by
        reading up (or down) the rows of the partition and marking all
        of the addable and removable cells of `e`-residue `i` and then
        recursively removing all adjacent pairs of removable and
        addable cells (in that order) from this list. The removable
        `i`-cells that remain at the end of the this process are the
        normal `i`-cells.

        When computing normal cells you can either read the cells in order
        from top to bottom (this corresponds to labeling the simple modules
        of the symmetric group by regular partitions) or from bottom to top
        (corresponding to labeling the simples by restricted partitions).
        By default we read down the partition but this can be changed by
        setting ``convention = 'RS'``.

        INPUT:

        - ``i`` -- (optional) a residue

        OUTPUT:

        If no residue ``i`` is specified then a dictionary of normal cells
        is returned, which gives the normal cells for ``0 <= i < e``.

        EXAMPLES::

            sage: KP = KleshchevPartitions(3, convention='regular')
            sage: KP([5,4,4,3,2]).normal_cells()
            {1: [(2, 3), (0, 4)]}
            sage: KP([5,4,4,3,2]).normal_cells(1)
            [(2, 3), (0, 4)]
            sage: KP = KleshchevPartitions(3, convention='restricted')
            sage: KP([5,4,4,3,2]).normal_cells()
            {0: [(4, 1)], 2: [(3, 2)]}
            sage: KP([5,4,4,3,2]).normal_cells(2)
            [(3, 2)]
        """
    def good_cells(self, i=None):
        """
        Return a list of the cells of ``self`` that are good.

        The good `i`-cell is the 'first' normal `i`-cell. As with the normal
        cells we can choose to read either up or down the partition as
        specified by :meth:`~KleshchevPartitions.convention`.

        INPUT:

        - ``i`` -- (optional) a residue

        OUTPUT:

        If no residue ``i`` is specified then a dictionary of good cells
        is returned, which gives the good cells for ``0 <= i < e``.

        EXAMPLES::

            sage: KP3 = KleshchevPartitions(3, convention='regular')
            sage: KP3([5,4,4,3,2]).good_cells()
            {1: (2, 3)}
            sage: KP3([5,4,4,3,2]).good_cells(1)
            (2, 3)
            sage: KP4 = KleshchevPartitions(4, convention='restricted')
            sage: KP4([5,4,4,3,2]).good_cells()
            {1: (2, 3)}
            sage: KP4([5,4,4,3,2]).good_cells(0)
            sage: KP4([5,4,4,3,2]).good_cells(1)
            (2, 3)
        """
    def good_residue_sequence(self):
        """
        Return a sequence of good nodes from the empty partition
        to ``self``, or ``None`` if no such sequence exists.

        EXAMPLES::

            sage: KP = KleshchevPartitions(3, convention='regular')
            sage: KP([5,4,4,3,2]).good_residue_sequence()
            [0, 2, 1, 1, 0, 2, 0, 2, 1, 1, 0, 2, 0, 2, 2, 0, 1, 1]
            sage: KP = KleshchevPartitions(3, convention='restricted')
            sage: KP([5,4,4,3,2]).good_residue_sequence()
            [0, 1, 2, 2, 0, 1, 0, 2, 1, 2, 0, 1, 0, 2, 1, 2, 1, 0]
        """
    def good_cell_sequence(self):
        """
        Return a sequence of good nodes from the empty partition
        to ``self``, or ``None`` if no such sequence exists.

        EXAMPLES::

            sage: KP = KleshchevPartitions(3, convention='regular')
            sage: KP([5,4,4,3,2]).good_cell_sequence()
            [(0, 0), (1, 0), (0, 1), (2, 0), (1, 1), (0, 2),
             (3, 0), (2, 1), (1, 2), (3, 1), (0, 3), (1, 3),
             (2, 2), (3, 2), (4, 0), (4, 1), (0, 4), (2, 3)]
            sage: KP = KleshchevPartitions(3, convention='restricted')
            sage: KP([5,4,4,3,2]).good_cell_sequence()
            [(0, 0), (0, 1), (1, 0), (0, 2), (1, 1), (2, 0),
             (0, 3), (2, 1), (1, 2), (1, 3), (3, 0), (3, 1),
             (2, 2), (4, 0), (2, 3), (3, 2), (0, 4), (4, 1)]
        """
    def mullineux_conjugate(self):
        """
        Return the partition tuple that is the Mullineux conjugate of ``self``.

        It follows from results in [BK2009]_, [Mat2015]_ that if `\\nu` is the
        Mullineux conjugate of the Kleshchev partition tuple `\\mu` then the
        simple module `D^\\nu =(D^\\mu)^{\\text{sgn}}` is obtained from `D^\\mu`
        by twisting by the `\\text{sgn}`-automorphism with is the
        Iwahori-Hecke algebra analogue of tensoring with the one
        dimensional sign representation.

        EXAMPLES::

            sage: KP = KleshchevPartitions(3, convention='regular')
            sage: KP([5,4,4,3,2]).mullineux_conjugate()
            [9, 7, 1, 1]
            sage: KP = KleshchevPartitions(3, convention='restricted')
            sage: KP([5,4,4,3,2]).mullineux_conjugate()
            [3, 2, 2, 2, 2, 2, 2, 1, 1, 1]
            sage: KP = KleshchevPartitions(3, [2], convention='regular')
            sage: mc = KP([5,4,4,3,2]).mullineux_conjugate(); mc
            [9, 7, 1, 1]
            sage: mc.parent().multicharge()
            (1,)
            sage: KP = KleshchevPartitions(3, [2], convention='restricted')
            sage: mc = KP([5,4,4,3,2]).mullineux_conjugate(); mc
            [3, 2, 2, 2, 2, 2, 2, 1, 1, 1]
            sage: mc.parent().multicharge()
            (1,)
        """
    def is_regular(self):
        """
        Return ``True`` if ``self`` is a `e`-regular partition tuple.

        A partition tuple is `e`-regular if we can get to the empty partition
        tuple by successively removing a sequence of good cells in the down
        direction. Equivalently, all partitions are `0`-regular and if `e > 0`
        then a partition is `e`-regular if no `e` nonzero parts of ``self``
        are equal.

        EXAMPLES::

            sage: KP = KleshchevPartitions(2)
            sage: KP([2,1,1]).is_regular()
            False
            sage: KP = KleshchevPartitions(3)
            sage: KP([2,1,1]).is_regular()
            True
            sage: KP([]).is_regular()
            True
        """
    def is_restricted(self):
        """
        Return ``True`` if ``self`` is an `e`-restricted partition tuple.

        A partition tuple is `e`-restricted if we can get to the empty
        partition tuple by successively removing a sequence of good cells in
        the up direction. Equivalently, all partitions are `0`-restricted and
        if `e > 0` then a partition is `e`-restricted if the difference of
        successive parts of ``self`` are always strictly less than `e`.

        EXAMPLES::

            sage: KP = KleshchevPartitions(2, convention='regular')
            sage: KP([3,1]).is_restricted()
            False
            sage: KP = KleshchevPartitions(3, convention='regular')
            sage: KP([3,1]).is_restricted()
            True
            sage: KP([]).is_restricted()
            True
        """

class KleshchevPartitionTuple(PartitionTuple):
    """
    Abstract base class for Kleshchev partition tuples. See
    :class:`~KleshchevPartitions`.
    """
    def conormal_cells(self, i=None):
        '''
        Return a dictionary of the cells of the partition that are conormal.

        Following [Kle1995]_, the *conormal* cells are computed by
        reading up (or down) the rows of the partition and marking all
        of the addable and removable cells of `e`-residue `i` and then
        recursively removing all adjacent pairs of removable and addable
        cells (in that order) from this list. The addable `i`-cells that
        remain at the end of the this process are the conormal `i`-cells.

        When computing conormal cells you can either read the cells in order
        from top to bottom (this corresponds to labeling the simple modules
        of the symmetric group by regular partitions) or from bottom to top
        (corresponding to labeling the simples by restricted partitions).
        By default we read down the partition but this can be changed by
        setting ``convention = \'RS\'``.

        INPUT:

        - ``i`` -- (optional) a residue

        OUTPUT:

        If no residue ``i`` is specified then a dictionary of conormal cells
        is returned, which gives the conormal cells for ``0 <= i < e``.

        EXAMPLES::

            sage: KP = KleshchevPartitions(3, [0,1], convention="left regular")
            sage: KP([[4, 2], [5, 3, 1]]).conormal_cells()
            {0: [(1, 2, 1), (1, 1, 3), (1, 0, 5)],
            1: [(1, 3, 0), (0, 2, 0), (0, 1, 2), (0, 0, 4)]}
            sage: KP([[4, 2], [5, 3, 1]]).conormal_cells(1)
            [(1, 3, 0), (0, 2, 0), (0, 1, 2), (0, 0, 4)]
            sage: KP([[4, 2], [5, 3, 1]]).conormal_cells(2)
            []
            sage: KP = KleshchevPartitions(3, [0,1], convention="right restricted")
            sage: KP([[4, 2], [5, 3, 1]]).conormal_cells(0)
            [(1, 0, 5), (1, 1, 3), (1, 2, 1)]
        '''
    def cogood_cells(self, i=None):
        '''
        Return a list of the cells of the partition that are cogood.

        The cogood `i`-cell is the \'last\' conormal `i`-cell. As with the
        conormal cells we can choose to read either up or down the partition
        as specified by :meth:`~KleshchevPartitions.convention`.

        INPUT:

        - ``i`` -- (optional) a residue

        OUTPUT:

        If no residue ``i`` is specified then a dictionary of cogood cells
        is returned, which gives the cogood cells for ``0 <= i < e``.

        EXAMPLES::

            sage: KP = KleshchevPartitions(3, [0,1])
            sage: pt = KP([[4, 2], [5, 3, 1]])
            sage: pt.cogood_cells()
            {0: (1, 2, 1), 1: (1, 3, 0)}
            sage: pt.cogood_cells(0)
            (1, 2, 1)
            sage: KP = KleshchevPartitions(4, [0,1], convention="left regular")
            sage: pt = KP([[5, 2, 2], [6, 1, 1]])
            sage: pt.cogood_cells()
            {1: (0, 0, 5), 2: (1, 3, 0)}
            sage: pt.cogood_cells(0) is None
            True
            sage: pt.cogood_cells(1) is None
            False
        '''
    def normal_cells(self, i=None):
        '''
        Return a dictionary of the removable cells of the partition that
        are normal.

        Following [Kle1995]_, the *normal* cells are computed by
        reading up (or down) the rows of the partition and marking all
        of the addable and removable cells of `e`-residue `i` and then
        recursively removing all adjacent pairs of removable and
        addable cells (in that order) from this list. The removable
        `i`-cells that remain at the end of the this process are the
        normal `i`-cells.

        When computing normal cells you can either read the cells in order
        from top to bottom (this corresponds to labeling the simple modules
        of the symmetric group by regular partitions) or from bottom to top
        (corresponding to labeling the simples by restricted partitions).
        By default we read down the partition but this can be changed by
        setting ``convention = \'RS\'``.

        INPUT:

        - ``i`` -- (optional) a residue

        OUTPUT:

        If no residue ``i`` is specified then a dictionary of normal cells
        is returned, which gives the normal cells for ``0 <= i < e``.

        EXAMPLES::

            sage: KP = KleshchevPartitions(3, [0,1], convention="left restricted")
            sage: KP([[4, 2], [5, 3, 1]]).normal_cells()
            {2: [(1, 0, 4), (1, 1, 2), (1, 2, 0)]}
            sage: KP([[4, 2], [5, 3, 1]]).normal_cells(1)
            []
            sage: KP = KleshchevPartitions(3, [0,1], convention="left regular")
            sage: KP([[4, 2], [5, 3, 1]]).normal_cells()
            {0: [(0, 1, 1), (0, 0, 3)], 2: [(1, 2, 0), (1, 1, 2), (1, 0, 4)]}
            sage: KP = KleshchevPartitions(3, [0,1], convention="right regular")
            sage: KP([[4, 2], [5, 3, 1]]).normal_cells()
            {2: [(1, 2, 0), (1, 1, 2), (1, 0, 4)]}
            sage: KP = KleshchevPartitions(3, [0,1], convention="right restricted")
            sage: KP([[4, 2], [5, 3, 1]]).normal_cells()
            {0: [(0, 0, 3), (0, 1, 1)], 2: [(1, 0, 4), (1, 1, 2), (1, 2, 0)]}
        '''
    def good_cells(self, i=None):
        '''
        Return a list of the cells of the partition tuple which are good.

        The good `i`-cell is the \'first\' normal `i`-cell. As with the normal
        cells we can choose to read either up or down the partition as specified
        by :meth:`~KleshchevPartitions.convention`.

        INPUT:

        - ``i`` -- (optional) a residue

        OUTPUT:

        If no residue ``i`` is specified then a dictionary of good cells
        is returned, which gives the good cells for ``0 <= i < e``.

        EXAMPLES::

            sage: KP = KleshchevPartitions(3, [0,1])
            sage: pt = KP([[4, 2], [5, 3, 1]])
            sage: pt.good_cells()
            {2: (1, 0, 4)}
            sage: pt.good_cells(2)
            (1, 0, 4)
            sage: KP = KleshchevPartitions(4, [0,1], convention="left regular")
            sage: pt = KP([[5, 2, 2], [6, 2, 1]])
            sage: pt.good_cells()
            {0: (0, 0, 4), 2: (1, 0, 5), 3: (0, 2, 1)}
            sage: pt.good_cells(1) is None
            True
        '''
    def good_residue_sequence(self):
        """
        Return a sequence of good nodes from the empty partition to ``self``.

        EXAMPLES::

            sage: KP = KleshchevPartitions(3, [0,1])
            sage: KP([[4, 2], [5, 3, 1]]).good_residue_sequence()
            [0, 1, 2, 1, 2, 0, 1, 0, 2, 2, 0, 1, 0, 2, 2]
        """
    def good_cell_sequence(self):
        """
        Return a sequence of good nodes from the empty partition to ``self``.

        EXAMPLES::

            sage: KP = KleshchevPartitions(3,[0,1])
            sage: KP([[4, 2], [5, 3, 1]]).good_cell_sequence()
            [(0, 0, 0), (1, 0, 0), (1, 0, 1), (0, 0, 1), (0, 1, 0),
             (1, 1, 0), (1, 1, 1), (1, 0, 2), (1, 2, 0), (0, 0, 2),
             (0, 1, 1), (1, 0, 3), (0, 0, 3), (1, 1, 2), (1, 0, 4)]
        """
    def mullineux_conjugate(self):
        """
        Return the partition that is the Mullineux conjugate of ``self``.

        It follows from results in [Kle1996]_ [Bru1998]_ that if `\\nu` is the
        Mullineux conjugate of the Kleshchev partition tuple `\\mu` then the
        simple module `D^\\nu =(D^\\mu)^{\\text{sgn}}` is obtained from `D^\\mu`
        by twisting by the `\\text{sgn}`-automorphism with is the Hecke algebra
        analogue of tensoring with the one dimensional sign representation.

        EXAMPLES::

            sage: KP = KleshchevPartitions(3, [0,1])
            sage: mc = KP([[4, 2], [5, 3, 1]]).mullineux_conjugate(); mc
            ([2, 2, 1, 1], [3, 2, 2, 1, 1])
            sage: mc.parent()
            Kleshchev partitions with e=3 and multicharge=(0,2)
        """
    def is_regular(self):
        '''
        Return ``True`` if ``self`` is a `e`-regular partition tuple.

        A partition tuple is `e`-regular if we can get to the
        empty partition tuple by successively removing a sequence
        of good cells in the down direction.

        EXAMPLES::

            sage: KP = KleshchevPartitions(2, [0,2], convention="right restricted")
            sage: KP([[3,2,1], [2,1,1]]).is_regular()
            False
            sage: KP = KleshchevPartitions(4, [0,2], convention="right restricted")
            sage: KP([[3,2,1], [2,1,1]]).is_regular()
            True
            sage: KP([[], []]).is_regular()
            True
        '''
    def is_restricted(self):
        '''
        Return ``True`` if ``self`` is an `e`-restricted partition tuple.

        A partition tuple is `e`-restricted if we can get to the
        empty partition tuple by successively removing a sequence
        of good cells in the up direction.

        EXAMPLES::

            sage: KP = KleshchevPartitions(2, [0,2], convention="left regular")
            sage: KP([[3,2,1], [3,1]]).is_restricted()
            False
            sage: KP = KleshchevPartitions(3, [0,2], convention="left regular")
            sage: KP([[3,2,1], [3,1]]).is_restricted()
            True
            sage: KP([[], []]).is_restricted()
            True
        '''

class KleshchevCrystalMixin:
    """
    Mixin class for the crystal structure of a Kleshchev partition.
    """
    def epsilon(self, i):
        '''
        Return the Kashiwara crystal operator `\\varepsilon_i` applied to ``self``.

        INPUT:

        - ``i`` -- an element of the index set

        EXAMPLES::

            sage: C = crystals.KleshchevPartitions(3, [0,2], convention="left regular")
            sage: x = C([[5,4,1],[3,2,1,1]])
            sage: [x.epsilon(i) for i in C.index_set()]
            [0, 3, 0]
        '''
    def phi(self, i):
        '''
        Return the Kashiwara crystal operator `\\varphi_i` applied to ``self``.

        INPUT:

        - ``i`` -- an element of the index set

        EXAMPLES::

            sage: C = crystals.KleshchevPartitions(3, [0,2], convention="left regular")
            sage: x = C([[5,4,1],[3,2,1,1]])
            sage: [x.phi(i) for i in C.index_set()]
            [3, 2, 0]
        '''
    def Epsilon(self):
        '''
        Return `\\varepsilon` of ``self``.

        EXAMPLES::

            sage: C = crystals.KleshchevPartitions(3, [0,2], convention="left regular")
            sage: x = C([[5,4,1],[3,2,1,1]])
            sage: x.Epsilon()
            3*Lambda[1]
        '''
    def Phi(self):
        '''
        Return `\\phi` of ``self``.

        EXAMPLES::

            sage: C = crystals.KleshchevPartitions(3, [0,2], convention="left regular")
            sage: x = C([[5,4,1],[3,2,1,1]])
            sage: x.Phi()
            3*Lambda[0] + 2*Lambda[1]
        '''
    def weight(self):
        '''
        Return the weight of ``self``.

        EXAMPLES::

            sage: C = crystals.KleshchevPartitions(3, [0,2], convention="left regular")
            sage: x = C([[5,4,1], [3,2,1,1]])
            sage: x.weight()
            3*Lambda[0] - Lambda[1] - 5*delta
            sage: x.Phi() - x.Epsilon()
            3*Lambda[0] - Lambda[1]

            sage: C = crystals.KleshchevPartitions(3, [0,2], convention="right regular")
            sage: y = C([[5,1,1], [4,2,2,1,1]])
            sage: y.weight()
            6*Lambda[0] - 4*Lambda[1] - 4*delta
            sage: y.Phi() - y.Epsilon()
            6*Lambda[0] - 4*Lambda[1]

            sage: C = crystals.KleshchevPartitions(3, [0,2], convention="left regular")
            sage: y = C([[5,1,1], [4,2,2,1,1]])
            sage: y.weight()
            6*Lambda[0] - 4*Lambda[1] - 4*delta
            sage: y.Phi() - y.Epsilon()
            6*Lambda[0] - 4*Lambda[1]
        '''

class KleshchevPartitionCrystal(KleshchevPartition, KleshchevCrystalMixin):
    """
    Kleshchev partition with the crystal structure.
    """
    def e(self, i):
        '''
        Return the action of `e_i` on ``self``.

        INPUT:

        - ``i`` -- an element of the index set

        EXAMPLES::

            sage: C = crystals.KleshchevPartitions(3, convention="left regular")
            sage: x = C([5,4,1])
            sage: x.e(0)
            sage: x.e(1)
            [5, 4]
        '''
    def f(self, i):
        '''
        Return the action of `f_i` on ``self``.

        INPUT:

        - ``i`` -- an element of the index set

        EXAMPLES::

            sage: C = crystals.KleshchevPartitions(3, convention="left regular")
            sage: x = C([5,4,1])
            sage: x.f(0)
            [5, 5, 1]
            sage: x.f(1)
            sage: x.f(2)
            [5, 4, 2]
        '''

class KleshchevPartitionTupleCrystal(KleshchevPartitionTuple, KleshchevCrystalMixin):
    """
    Kleshchev partition tuple with the crystal structure.
    """
    def e(self, i):
        '''
        Return the action of `e_i` on ``self``.

        INPUT:

        - ``i`` -- an element of the index set

        EXAMPLES::

            sage: C = crystals.KleshchevPartitions(3, [0,2], convention="left regular")
            sage: x = C([[5,4,1],[3,2,1,1]])
            sage: x.e(0)
            sage: x.e(1)
            ([5, 4, 1], [2, 2, 1, 1])
        '''
    def f(self, i):
        '''
        Return the action of `f_i` on ``self``.

        INPUT:

        - ``i`` -- an element of the index set

        EXAMPLES::

            sage: C = crystals.KleshchevPartitions(3, [0,2], convention="left regular")
            sage: x = C([[5,4,1],[3,2,1,1]])
            sage: x.f(0)
            ([5, 5, 1], [3, 2, 1, 1])
            sage: x.f(1)
            ([5, 4, 1], [3, 2, 2, 1])
            sage: x.f(2)
        '''

class KleshchevPartitions(PartitionTuples):
    '''
    Kleshchev partitions.

    A partition (tuple) `\\mu` is Kleshchev if it can be recursively
    obtained by adding a sequence of good nodes to the empty
    :class:`PartitionTuple` of the same :meth:`~PartitionTuple.level`
    and multicharge.

    There are four different conventions that are used in the literature for
    Kleshchev partitions, depending on whether we read partitions from top
    to bottom (regular) or bottom to top (restricted) and whether we read
    partition tuples from left to right or right to left. All of these
    conventions are supported::

        sage: KleshchevPartitions(2, [0,0], size=2, convention=\'left regular\')[:]
        [([1], [1]), ([2], [])]
        sage: KleshchevPartitions(2, [0,0], size=2, convention=\'left restricted\')[:]
        [([1], [1]), ([], [1, 1])]
        sage: KleshchevPartitions(2, [0,0], size=2, convention=\'right regular\')[:]
        [([1], [1]), ([], [2])]
        sage: KleshchevPartitions(2, [0,0], size=2, convention=\'right restricted\')[:]
        [([1], [1]), ([1, 1], [])]

    By default, the ``left restricted`` convention is used. As a shorthand,
    ``LG``, ``LS``, ``RG`` and ``RS``, respectively, can be used to specify
    the ``convention``. With the ``left`` convention the partition tuples
    should be ordered with the most dominant partitions in the partition
    tuple on the left and with the ``right`` convention the most dominant
    partition is on the right.

    The :class:`~KleshchevPartitions` class will automatically convert
    between these four different conventions::

        sage: KPlg = KleshchevPartitions(2, [0,0], size=2, convention=\'left regular\')
        sage: KPls = KleshchevPartitions(2, [0,0], size=2, convention=\'left restricted\')
        sage: [KPlg(mu) for mu in KPls]
        [([1], [1]), ([2], [])]

    EXAMPLES::

        sage: sorted(KleshchevPartitions(5,[3,2,1],1, convention=\'RS\'))
        [([], [], [1]), ([], [1], []), ([1], [], [])]
        sage: sorted(KleshchevPartitions(5, [3,2,1], 1, convention=\'LS\'))
        [([], [], [1]), ([], [1], []), ([1], [], [])]
        sage: sorted(KleshchevPartitions(5, [3,2,1], 3))
        [([], [], [1, 1, 1]),
         ([], [], [2, 1]),
         ([], [], [3]),
         ([], [1], [1, 1]),
         ([], [1], [2]),
         ([], [1, 1], [1]),
         ([], [2], [1]),
         ([], [3], []),
         ([1], [], [1, 1]),
         ([1], [], [2]),
         ([1], [1], [1]),
         ([1], [2], []),
         ([1, 1], [1], []),
         ([2], [], [1]),
         ([2], [1], []),
         ([3], [], [])]
        sage: sorted(KleshchevPartitions(5, [3,2,1], 3, convention="left regular"))
        [([], [], [1, 1, 1]),
         ([], [1], [1, 1]),
         ([], [1], [2]),
         ([], [1, 1], [1]),
         ([], [1, 1, 1], []),
         ([1], [], [1, 1]),
         ([1], [1], [1]),
         ([1], [1, 1], []),
         ([1], [2], []),
         ([1, 1], [], [1]),
         ([1, 1], [1], []),
         ([1, 1, 1], [], []),
         ([2], [], [1]),
         ([2], [1], []),
         ([2, 1], [], []),
         ([3], [], [])]

    REFERENCES:

    - [AM2000]_
    - [Ariki2001]_
    - [BK2009]_
    - [Kle2009]_
    '''
    @staticmethod
    def __classcall_private__(cls, e, multicharge=(0,), size=None, convention: str = 'left restricted'):
        """
        This is a factory class which returns the appropriate parent based on
        the values of `level` and `size`.

        EXAMPLES::

            sage: sorted(KleshchevPartitions(5, [3,2,1], 1, convention='RS'))
            [([], [], [1]), ([], [1], []), ([1], [], [])]
            sage: sorted(KleshchevPartitions(5, [3,2,1], 1, convention='LS'))
            [([], [], [1]), ([], [1], []), ([1], [], [])]
        """
    def multicharge(self):
        """
        Return the multicharge of ``self``.

        EXAMPLES::

            sage: KP = KleshchevPartitions(6, [2])
            sage: KP.multicharge()
            (2,)
            sage: KP = KleshchevPartitions(5, [3,0,1], 1, convention='LS')
            sage: KP.multicharge()
            (3, 0, 1)
        """
    def convention(self):
        '''
        Return the convention of ``self``.

        EXAMPLES::

            sage: KP = KleshchevPartitions(4)
            sage: KP.convention()
            \'restricted\'
            sage: KP = KleshchevPartitions(6, [4], 3, convention="right regular")
            sage: KP.convention()
            \'regular\'
            sage: KP = KleshchevPartitions(5, [3,0,1], 1)
            sage: KP.convention()
            \'left restricted\'
            sage: KP = KleshchevPartitions(5, [3,0,1], 1, convention=\'right regular\')
            sage: KP.convention()
            \'right regular\'
        '''

class KleshchevPartitions_all(KleshchevPartitions):
    '''
    Class of all Kleshchev partitions.

    .. RUBRIC:: Crystal structure

    We consider type `A_{e-1}^{(1)}` crystals, and let `r = (r_i |
    r_i \\in \\ZZ / e \\ZZ)` be a finite sequence of length `k`, which
    is the *level*, and `\\lambda = \\sum_i \\Lambda_{r_i}`. We will
    model the highest weight `U_q(\\mathfrak{g})`-crystal `B(\\lambda)`
    by a particular subset of partition tuples of level `k`.

    Consider a partition tuple `\\mu` with multicharge `r`.
    We define `e_i(\\mu)` as the partition tuple obtained after the
    deletion of the `i`-:meth:`good cell
    <~sage.combinat.partition_kleshchev.KleshchevPartitionTuple.good_cell>`
    to `\\mu` and `0` if there is no `i`-good cell. We define `f_i(\\mu)` as
    the partition tuple obtained by the addition of the `i`-:meth:`cogood cell
    <~sage.combinat.partition_kleshchev.KleshchevPartitionTuple.cogood_cell>`
    to `\\mu` and `0` if there is no `i`-good cell.

    The crystal `B(\\lambda)` is the crystal generated by the empty
    partition tuple. We can compute the weight of an element `\\mu` by taking
    `\\lambda - \\sum_{i=0}^n c_i \\alpha_i` where `c_i` is the number of cells
    of `n`-residue `i` in `\\mu`. Partition tuples in the crystal are known
    as *Kleshchev partitions*.

    .. NOTE::

        We can describe normal (not restricted) Kleshchev partition tuples
        in `B(\\lambda)` as partition tuples `\\mu` such that
        `\\mu^{(t)}_{r_t - r_{t+1} + x} < \\mu^{(t+1)}_x`
        for all `x \\geq 1` and `1 \\leq t \\leq k - 1`.

    INPUT:

    - ``e`` -- for type `A_{e-1}^{(1)}` or `0`
    - ``multicharge`` -- the multicharge sequence `r`
    - ``convention`` -- (default: ``\'LS\'``) the reading convention

    EXAMPLES:

    We first do an example of a level 1 crystal::

        sage: C = crystals.KleshchevPartitions(3, [0], convention="left restricted")
        sage: C
        Kleshchev partitions with e=3
        sage: mg = C.highest_weight_vector()
        sage: mg
        []
        sage: mg.f(0)
        [1]
        sage: mg.f(1)
        sage: mg.f(2)
        sage: mg.f_string([0,2,1,0])
        [1, 1, 1, 1]
        sage: mg.f_string([0,1,2,0])
        [2, 2]
        sage: GC = C.subcrystal(max_depth=5).digraph()
        sage: B = crystals.LSPaths([\'A\',2,1], [1,0,0])
        sage: GB = B.subcrystal(max_depth=5).digraph()
        sage: GC.is_isomorphic(GB, edge_labels=True)
        True

    Now a higher level crystal::

        sage: C = crystals.KleshchevPartitions(3, [0,2], convention="right restricted")
        sage: mg = C.highest_weight_vector()
        sage: mg
        ([], [])
        sage: mg.f(0)
        ([1], [])
        sage: mg.f(2)
        ([], [1])
        sage: mg.f_string([0,1,2,0])
        ([2, 2], [])
        sage: mg.f_string([0,2,1,0])
        ([1, 1, 1, 1], [])
        sage: mg.f_string([2,0,1,0])
        ([2], [2])
        sage: GC = C.subcrystal(max_depth=5).digraph()
        sage: B = crystals.LSPaths([\'A\',2,1], [1,0,1])
        sage: GB = B.subcrystal(max_depth=5).digraph()
        sage: GC.is_isomorphic(GB, edge_labels=True)
        True

    The ordering of the residues gives a different representation of the
    higher level crystals (but it is still isomorphic)::

        sage: C2 = crystals.KleshchevPartitions(3, [2,0], convention="right restricted")
        sage: mg2 = C2.highest_weight_vector()
        sage: mg2.f_string([0,1,2,0])
        ([2], [2])
        sage: mg2.f_string([0,2,1,0])
        ([1, 1, 1], [1])
        sage: mg2.f_string([2,0,1,0])
        ([2, 1], [1])
        sage: GC2 = C2.subcrystal(max_depth=5).digraph()
        sage: GC.is_isomorphic(GC2, edge_labels=True)
        True

    TESTS:

    We check that all conventions give isomorphic crystals::

        sage: CLS = crystals.KleshchevPartitions(3, [2,0], convention="left restricted")
        sage: CRS = crystals.KleshchevPartitions(3, [2,0], convention="right restricted")
        sage: CLG = crystals.KleshchevPartitions(3, [2,0], convention="left regular")
        sage: CRG = crystals.KleshchevPartitions(3, [2,0], convention="right regular")
        sage: C = [CLS, CRS, CLG, CRG]
        sage: G = [B.subcrystal(max_depth=6).digraph() for B in C]
        sage: G[0].is_isomorphic(G[1], edge_labels=True)
        True
        sage: G[0].is_isomorphic(G[2], edge_labels=True)
        True
        sage: G[0].is_isomorphic(G[3], edge_labels=True)
        True

    REFERENCES:

    - [Ariki1996]_
    - [Ariki2001]_
    - [Tingley2007]_
    - [TingleyLN]_
    - [Vazirani2002]_
    '''
    Element: Incomplete
    module_generators: Incomplete
    def __init__(self, e, multicharge, convention) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: K = KleshchevPartitions(4, [2])
            sage: TestSuite(K).run()  # long time
            sage: K = KleshchevPartitions(4, [0,2,1])
            sage: TestSuite(K).run()  # long time

            sage: K = KleshchevPartitions(0, [2])
            sage: TestSuite(K).run()
            sage: K = KleshchevPartitions(0, [0,2,1])
            sage: TestSuite(K).run()  # long time
        """
    def __contains__(self, mu) -> bool:
        """
        Containment test for Kleshchev partitions.

        EXAMPLES::

            sage: PartitionTuple([[3,2],[2]]) in KleshchevPartitions(2, [0,0], 7)
            False
            sage: PartitionTuple([[],[2,1],[3,2]]) in KleshchevPartitions(5, [0,0,1], 7)
            False
            sage: PartitionTuple([[],[2,1],[3,2]]) in KleshchevPartitions(5, [0,1,1], 7)
            False
            sage: PartitionTuple([[],[2,1],[3,2]]) in KleshchevPartitions(5, [0,1,1], 8)
            True
            sage: all(mu in PartitionTuples(3,8) for mu in KleshchevPartitions(2, [0,0,0], 8))
            True
        """
    def __iter__(self):
        """
        Iterate over ``self``.

        EXAMPLES::

            sage: it = iter(KleshchevPartitions(2))
            sage: [next(it) for _ in range(10)]
            [[], [1], [1, 1], [2, 1], [1, 1, 1], [2, 1, 1],
             [1, 1, 1, 1], [2, 2, 1], [2, 1, 1, 1], [1, 1, 1, 1, 1]]
            sage: it = iter(KleshchevPartitions(2, convention='LG'))
            sage: [next(it) for _ in range(10)]
            [[], [1], [2], [3], [2, 1], [4], [3, 1], [5], [4, 1], [3, 2]]

            sage: it = iter(KleshchevPartitions(2, [0,1], convention='LS'))
            sage: [next(it) for _ in range(10)]
            [([], []),
             ([1], []),
             ([], [1]),
             ([1], [1]),
             ([], [1, 1]),
             ([1, 1], [1]),
             ([1], [1, 1]),
             ([], [2, 1]),
             ([], [1, 1, 1]),
             ([2, 1], [1])]
            sage: it = iter(KleshchevPartitions(2, [0,1], convention='RS'))
            sage: [next(it) for _ in range(10)]
            [([], []),
             ([1], []),
             ([], [1]),
             ([1, 1], []),
             ([1], [1]),
             ([2, 1], []),
             ([1, 1, 1], []),
             ([1, 1], [1]),
             ([1], [1, 1]),
             ([2, 1, 1], [])]
            sage: it = iter(KleshchevPartitions(2, [0,1], convention='LG'))
            sage: [next(it) for _ in range(10)]
            [([], []),
             ([1], []),
             ([], [1]),
             ([2], []),
             ([1], [1]),
             ([3], []),
             ([2, 1], []),
             ([2], [1]),
             ([1], [2]),
             ([4], [])]
            sage: it = iter(KleshchevPartitions(2, [0,1], convention='RG'))
            sage: [next(it) for _ in range(10)]
            [([], []),
             ([1], []),
             ([], [1]),
             ([1], [1]),
             ([], [2]),
             ([2], [1]),
             ([1], [2]),
             ([], [3]),
             ([], [2, 1]),
             ([2, 1], [1])]

            sage: it = iter(KleshchevPartitions(3, [0,1,2]))
            sage: [next(it) for _ in range(10)]
            [([], [], []), ([1], [], []), ([], [1], []), ([], [], [1]),
             ([1], [1], []), ([1], [], [1]), ([], [1, 1], []),
             ([], [1], [1]), ([], [], [2]), ([], [], [1, 1])]
        """

class KleshchevPartitions_size(KleshchevPartitions):
    """
    Kleshchev partitions of a fixed size.
    """
    Element: Incomplete
    def __init__(self, e, multicharge=(0,), size: int = 0, convention: str = 'RS') -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: K = KleshchevPartitions(4, 2)
            sage: TestSuite(K).run()
            sage: K = KleshchevPartitions(4, 4, convention='left regular')
            sage: TestSuite(K).run()
            sage: K = KleshchevPartitions(4, 4, convention='left restricted')
            sage: TestSuite(K).run()
            sage: K = KleshchevPartitions(4, [0,2,1], 4, convention='left regular')
            sage: TestSuite(K).run()
            sage: K = KleshchevPartitions(0, 2, convention='right restricted')
            sage: TestSuite(K).run()
            sage: K = KleshchevPartitions(0, [0,2,1], 4, convention='left restricted')
            sage: TestSuite(K).run()
            sage: K = KleshchevPartitions(0, [0,2,1], 4, convention='left regular')
            sage: TestSuite(K).run()

        We verify that we obtain the same size for all conventions
        and that the result is equal to the number of elements in
        the crystal at the corresponding depth::

            sage: B = crystals.LSPaths(['A',2,1], [1,0,1])
            sage: nd4 = (B.subcrystal(max_depth=4).cardinality()
            ....:        - B.subcrystal(max_depth=3).cardinality())
            sage: K = KleshchevPartitions(3, [0,2], 4, convention='RS')
            sage: K.cardinality() == nd4
            True
            sage: K = KleshchevPartitions(3, [0,2], 4, convention='RG')
            sage: K.cardinality() == nd4
            True
            sage: K = KleshchevPartitions(3, [0,2], 4, convention='LS')
            sage: K.cardinality() == nd4
            True
            sage: K = KleshchevPartitions(3, [0,2], 4, convention='LG')
            sage: K.cardinality() == nd4
            True
        """
    def __contains__(self, mu) -> bool:
        """
        Check if ``mu`` is in ``self``.

        TESTS::

            sage: PartitionTuple([[3,2],[2]]) in KleshchevPartitions(2,[0,0],7)
            False
            sage: PartitionTuple([[3,2],[],[],[],[2]]) in KleshchevPartitions(5,[0,0,0,0,0],7)
            False
            sage: PartitionTuple([[2,1],[],[1,1],[],[2]]) in KleshchevPartitions(5,[0,0,0,0,0],7, convention='RG')
            False
            sage: PartitionTuple([[2,1],[],[1,1],[],[3]]) in KleshchevPartitions(2,[0,0,0,0,0],9, convention='RS')
            False
            sage: all(mu in PartitionTuples(3,8) for mu in KleshchevPartitions(0,[0,0,0],8))
            True
        """
    @lazy_attribute
    def __iter__(self):
        """
        Wrapper to return the correct iterator which is different for
        :class:`Partitions` (level 1) and for :class:PartitionTuples`
        (higher levels).

        EXAMPLES::

            sage: KleshchevPartitions(3, 3, convention='RS')[:]
            [[2, 1], [1, 1, 1]]
            sage: KleshchevPartitions(3, 3, convention='RG')[:]
            [[3], [2, 1]]
            sage: KleshchevPartitions(3, [0], 3)[:]
            [[2, 1], [1, 1, 1]]
            sage: KleshchevPartitions(3, [0,0], 3)[:]
            [([1], [2]), ([1], [1, 1]), ([], [2, 1]), ([], [1, 1, 1])]
            sage: KleshchevPartitions(2, [0,1], size=0)[:]
            [([], [])]
            sage: KleshchevPartitions(2, [0,1], size=1)[:]
            [([1], []), ([], [1])]
            sage: KleshchevPartitions(2, [0,1], size=2)[:]
            [([1], [1]), ([], [1, 1])]
            sage: KleshchevPartitions(3, [0,1,2], size=2)[:]
            [([1], [1], []), ([1], [], [1]), ([], [1, 1], []),
             ([], [1], [1]), ([], [], [2]), ([], [], [1, 1])]
        """
    Element = KleshchevPartitionTuple
