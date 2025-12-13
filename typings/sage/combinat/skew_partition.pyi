from _typeshed import Incomplete
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.categories.infinite_enumerated_sets import InfiniteEnumeratedSets as InfiniteEnumeratedSets
from sage.combinat.combinat import CombinatorialElement as CombinatorialElement
from sage.combinat.composition import Compositions as Compositions
from sage.combinat.partition import Partitions as Partitions
from sage.combinat.tableau import Tableaux as Tableaux
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.sets.set import Set as Set
from sage.structure.global_options import GlobalOptions as GlobalOptions
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class SkewPartition(CombinatorialElement):
    """
    A skew partition.

    A skew partition of shape `\\lambda / \\mu` is the Young diagram from the
    partition `\\lambda` and removing the partition `\\mu` from the upper-left
    corner in English convention.
    """
    @staticmethod
    def __classcall_private__(cls, skp):
        """
        Return the skew partition object corresponding to ``skp``.

        EXAMPLES::

            sage: skp = SkewPartition([[3,2,1],[2,1]]); skp
            [3, 2, 1] / [2, 1]
            sage: skp.inner()
            [2, 1]
            sage: skp.outer()
            [3, 2, 1]
        """
    def __init__(self, parent, skp) -> None:
        """
        TESTS::

            sage: skp = SkewPartition([[3,2,1],[2,1]])
            sage: TestSuite(skp).run()
        """
    def ferrers_diagram(self):
        """
        Return the Ferrers diagram of ``self``.

        EXAMPLES::

            sage: print(SkewPartition([[5,4,3,1],[3,3,1]]).ferrers_diagram())
               **
               *
             **
            *
            sage: print(SkewPartition([[5,4,3,1],[3,1]]).diagram())
               **
             ***
            ***
            *
            sage: SkewPartitions.options(diagram_str='#', convention='French')
            sage: print(SkewPartition([[5,4,3,1],[3,1]]).diagram())
            #
            ###
             ###
               ##
            sage: SkewPartitions.options._reset()
        """
    diagram = ferrers_diagram
    def pp(self) -> None:
        """
        Pretty-print ``self``.

        EXAMPLES::

            sage: SkewPartition([[5,4,3,1],[3,3,1]]).pp()
               **
               *
             **
            *
        """
    def inner(self):
        """
        Return the inner partition of ``self``.

        EXAMPLES::

            sage: SkewPartition([[3,2,1],[1,1]]).inner()
            [1, 1]
        """
    def outer(self):
        """
        Return the outer partition of ``self``.

        EXAMPLES::

            sage: SkewPartition([[3,2,1],[1,1]]).outer()
            [3, 2, 1]
        """
    def column_lengths(self):
        """
        Return the column lengths of ``self``.

        EXAMPLES::

            sage: SkewPartition([[3,2,1],[1,1]]).column_lengths()
            [1, 2, 1]
            sage: SkewPartition([[5,2,2,2],[2,1]]).column_lengths()
            [2, 3, 1, 1, 1]
        """
    def row_lengths(self):
        """
        Return the row lengths of ``self``.

        EXAMPLES::

            sage: SkewPartition([[3,2,1],[1,1]]).row_lengths()
            [2, 1, 1]
        """
    def size(self):
        """
        Return the size of ``self``.

        EXAMPLES::

            sage: SkewPartition([[3,2,1],[1,1]]).size()
            4
        """
    def is_connected(self):
        """
        Return ``True`` if ``self`` is a connected skew partition.

        A skew partition is said to be *connected* if for each pair of
        consecutive rows, there are at least two cells (one in each row)
        which have a common edge.

        EXAMPLES::

            sage: SkewPartition([[5,4,3,1],[3,3,1]]).is_connected()
            False
            sage: SkewPartition([[5,4,3,1],[3,1]]).is_connected()
            True
        """
    def overlap(self):
        """
        Return the overlap of ``self``.

        The overlap of two consecutive rows in a skew partition is the
        number of pairs of cells (one in each row) that share a common
        edge. This number can be positive, zero, or negative.

        The overlap of a skew partition is the minimum of the overlap of
        the consecutive rows, or infinity in the case of at most one row.
        If the overlap is positive, then the skew partition is called
        *connected*.

        EXAMPLES::

            sage: SkewPartition([[],[]]).overlap()
            +Infinity
            sage: SkewPartition([[1],[]]).overlap()
            +Infinity
            sage: SkewPartition([[10],[]]).overlap()
            +Infinity
            sage: SkewPartition([[10],[2]]).overlap()
            +Infinity
            sage: SkewPartition([[10,1],[2]]).overlap()
            -1
            sage: SkewPartition([[10,10],[1]]).overlap()
            9
        """
    def is_overlap(self, n):
        """
        Return ``True`` if the overlap of ``self`` is at most ``n``.

        .. SEEALSO::

           :meth:`overlap`

        EXAMPLES::

            sage: SkewPartition([[5,4,3,1],[3,1]]).is_overlap(1)
            True
        """
    def is_ribbon(self):
        """
        Return ``True`` if and only if ``self`` is a ribbon.

        This means that if it has exactly one cell in each of `q`
        consecutive diagonals for some nonnegative integer `q`.

        EXAMPLES::

            sage: P = SkewPartition([[4,4,3,3],[3,2,2]])
            sage: P.pp()
               *
              **
              *
            ***
            sage: P.is_ribbon()
            True

            sage: P = SkewPartition([[4,3,3],[1,1]])
            sage: P.pp()
             ***
             **
            ***
            sage: P.is_ribbon()
            False

            sage: P = SkewPartition([[4,4,3,2],[3,2,2]])
            sage: P.pp()
               *
              **
              *
            **
            sage: P.is_ribbon()
            False

            sage: P = SkewPartition([[4,4,3,3],[4,2,2,1]])
            sage: P.pp()
            <BLANKLINE>
              **
              *
             **
            sage: P.is_ribbon()
            True

            sage: P = SkewPartition([[4,4,3,3],[4,2,2]])
            sage: P.pp()
            <BLANKLINE>
              **
              *
            ***
            sage: P.is_ribbon()
            True

            sage: SkewPartition([[2,2,1],[2,2,1]]).is_ribbon()
            True
        """
    def conjugate(self):
        """
        Return the conjugate of the skew partition skp.

        EXAMPLES::

            sage: SkewPartition([[3,2,1],[2]]).conjugate()
            [3, 2, 1] / [1, 1]
        """
    def outer_corners(self):
        '''
        Return a list of the outer corners of ``self``.

        These are corners that are contained inside of the shape.
        For the corners which are outside of the shape,
        use :meth:`outside_corners`.

        .. WARNING::

            In the case that ``self`` is an honest (rather than skew) partition,
            these are the :meth:`~sage.combinat.partition.Partition.corners`
            of the outer partition. In the language of [Sag2001]_ these would
            be the "inner corners" of the outer partition.

        .. SEEALSO::

            - :meth:`sage.combinat.skew_partition.SkewPartition.outside_corners`
            - :meth:`sage.combinat.partition.Partition.outside_corners`

        EXAMPLES::

            sage: SkewPartition([[4, 3, 1], [2]]).outer_corners()
            [(0, 3), (1, 2), (2, 0)]
        '''
    def inner_corners(self):
        """
        Return a list of the inner corners of ``self``.

        EXAMPLES::

            sage: SkewPartition([[4, 3, 1], [2]]).inner_corners()
            [(0, 2), (1, 0)]
            sage: SkewPartition([[4, 3, 1], []]).inner_corners()
            [(0, 0)]
        """
    def cell_poset(self, orientation: str = 'SE'):
        '''
        Return the Young diagram of ``self`` as a poset. The optional
        keyword variable ``orientation`` determines the order relation
        of the poset.

        The poset always uses the set of cells of the Young diagram
        of ``self`` as its ground set. The order relation of the poset
        depends on the ``orientation`` variable (which defaults to
        ``\'SE\'``). Concretely, ``orientation`` has to be specified to
        one of the strings ``\'NW\'``, ``\'NE\'``, ``\'SW\'``, and ``\'SE\'``,
        standing for "northwest", "northeast", "southwest" and
        "southeast", respectively. If ``orientation`` is ``\'SE\'``, then
        the order relation of the poset is such that a cell `u` is
        greater or equal to a cell `v` in the poset if and only if `u`
        lies weakly southeast of `v` (this means that `u` can be
        reached from `v` by a sequence of south and east steps; the
        sequence is allowed to consist of south steps only, or of east
        steps only, or even be empty). Similarly the order relation is
        defined for the other three orientations. The Young diagram is
        supposed to be drawn in English notation.

        The elements of the poset are the cells of the Young diagram
        of ``self``, written as tuples of zero-based coordinates (so
        that `(3, 7)` stands for the `8`-th cell of the `4`-th row,
        etc.).

        EXAMPLES::

            sage: # needs sage.graphs
            sage: p = SkewPartition([[3,3,1], [2,1]])
            sage: Q = p.cell_poset(); Q
            Finite poset containing 4 elements
            sage: sorted(Q)
            [(0, 2), (1, 1), (1, 2), (2, 0)]
            sage: sorted(Q.maximal_elements())
            [(1, 2), (2, 0)]
            sage: sorted(Q.minimal_elements())
            [(0, 2), (1, 1), (2, 0)]
            sage: sorted(Q.upper_covers((1, 1)))
            [(1, 2)]
            sage: sorted(Q.upper_covers((0, 2)))
            [(1, 2)]

            sage: # needs sage.graphs
            sage: P = p.cell_poset(orientation="NW"); P
            Finite poset containing 4 elements
            sage: sorted(P)
            [(0, 2), (1, 1), (1, 2), (2, 0)]
            sage: sorted(P.minimal_elements())
            [(1, 2), (2, 0)]
            sage: sorted(P.maximal_elements())
            [(0, 2), (1, 1), (2, 0)]
            sage: sorted(P.upper_covers((1, 2)))
            [(0, 2), (1, 1)]

            sage: # needs sage.graphs
            sage: R = p.cell_poset(orientation="NE"); R
            Finite poset containing 4 elements
            sage: sorted(R)
            [(0, 2), (1, 1), (1, 2), (2, 0)]
            sage: R.maximal_elements()
            [(0, 2)]
            sage: R.minimal_elements()
            [(2, 0)]
            sage: R.upper_covers((2, 0))
            [(1, 1)]
            sage: sorted([len(R.upper_covers(v)) for v in R])
            [0, 1, 1, 1]

        TESTS:

        We check that the posets are really what they should be for size
        up to `6`::

            sage: def check_NW(n):
            ....:     for p in SkewPartitions(n):
            ....:         P = p.cell_poset(orientation="NW")
            ....:         for c in p.cells():
            ....:             for d in p.cells():
            ....:                 if P.le(c, d) != (c[0] >= d[0]
            ....:                                   and c[1] >= d[1]):
            ....:                     return False
            ....:     return True
            sage: all( check_NW(n) for n in range(7) )                                  # needs sage.graphs
            True

            sage: def check_NE(n):
            ....:     for p in SkewPartitions(n):
            ....:         P = p.cell_poset(orientation="NE")
            ....:         for c in p.cells():
            ....:             for d in p.cells():
            ....:                 if P.le(c, d) != (c[0] >= d[0]
            ....:                                   and c[1] <= d[1]):
            ....:                     return False
            ....:     return True
            sage: all( check_NE(n) for n in range(7) )                                  # needs sage.graphs
            True

            sage: def test_duality(n, ori1, ori2):
            ....:     for p in SkewPartitions(n):
            ....:         P = p.cell_poset(orientation=ori1)
            ....:         Q = p.cell_poset(orientation=ori2)
            ....:         for c in p.cells():
            ....:             for d in p.cells():
            ....:                 if P.lt(c, d) != Q.lt(d, c):
            ....:                     return False
            ....:     return True
            sage: all( test_duality(n, "NW", "SE") for n in range(7) )                  # needs sage.graphs
            True
            sage: all( test_duality(n, "NE", "SW") for n in range(7) )                  # needs sage.graphs
            True
            sage: all( test_duality(n, "NE", "SE") for n in range(4) )                  # needs sage.graphs
            False
        '''
    def frobenius_rank(self):
        """
        Return the Frobenius rank of the skew partition ``self``.

        The Frobenius rank of a skew partition `\\lambda / \\mu` can be
        defined in various ways. The quickest one is probably the
        following: Writing `\\lambda` as
        `(\\lambda_1, \\lambda_2, \\cdots , \\lambda_N)`, and writing `\\mu`
        as `(\\mu_1, \\mu_2, \\cdots , \\mu_N)`, we define the Frobenius
        rank of `\\lambda / \\mu` to be the number of all
        `1 \\leq i \\leq N` such that

        .. MATH::

            \\lambda_i - i
            \\not\\in \\{ \\mu_1 - 1, \\mu_2 - 2, \\cdots , \\mu_N - N \\}.

        In other words, the Frobenius rank of `\\lambda / \\mu` is the
        number of rows in the Jacobi-Trudi matrix of `\\lambda / \\mu`
        which don't contain `h_0`. Further definitions have been
        considered in [Sta2002]_ (where Frobenius rank is just being
        called rank).

        If `\\mu` is the empty shape, then the Frobenius rank of
        `\\lambda / \\mu` is just the usual Frobenius rank of the
        partition `\\lambda` (see
        :meth:`~sage.combinat.partition.Partition.frobenius_rank()`).

        EXAMPLES::

            sage: SkewPartition([[8,8,7,4], [4,1,1]]).frobenius_rank()
            4
            sage: SkewPartition([[2,1], [1]]).frobenius_rank()
            2
            sage: SkewPartition([[2,1,1], [1]]).frobenius_rank()
            2
            sage: SkewPartition([[2,1,1], [1,1]]).frobenius_rank()
            2
            sage: SkewPartition([[5,4,3,2], [2,1,1]]).frobenius_rank()
            3
            sage: SkewPartition([[4,2,1], [3,1,1]]).frobenius_rank()
            2
            sage: SkewPartition([[4,2,1], [3,2,1]]).frobenius_rank()
            1

        If the inner shape is empty, then the Frobenius rank of the skew
        partition is just the standard Frobenius rank of the partition::

            sage: all( SkewPartition([lam, Partition([])]).frobenius_rank()
            ....:      == lam.frobenius_rank() for i in range(6)
            ....:      for lam in Partitions(i) )
            True

        If the inner and outer shapes are equal, then the Frobenius rank
        is zero::

            sage: all( SkewPartition([lam, lam]).frobenius_rank() == 0
            ....:      for i in range(6) for lam in Partitions(i) )
            True
        """
    def cells(self):
        """
        Return the coordinates of the cells of ``self``. Coordinates are
        given as ``(row-index, column-index)`` and are 0 based.

        EXAMPLES::

            sage: SkewPartition([[4, 3, 1], [2]]).cells()
            [(0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (2, 0)]
            sage: SkewPartition([[4, 3, 1], []]).cells()
            [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (2, 0)]
            sage: SkewPartition([[2], []]).cells()
            [(0, 0), (0, 1)]
        """
    def to_list(self):
        """
        Return ``self`` as a list of lists.

        EXAMPLES::

            sage: s = SkewPartition([[4,3,1],[2]])
            sage: s.to_list()
            [[4, 3, 1], [2]]
            sage: type(s.to_list())
            <class 'list'>
        """
    def to_dag(self, format: str = 'string'):
        """
        Return a directed acyclic graph corresponding to the skew
        partition ``self``.

        The directed acyclic graph corresponding to a skew partition
        `p` is the digraph whose vertices are the cells of `p`, and
        whose edges go from each cell to its lower and right
        neighbors (in English notation).

        INPUT:

        - ``format`` -- either ``'string'`` or ``'tuple'`` (default:
          ``'string'``); determines whether the vertices of the
          resulting dag will be strings or 2-tuples of coordinates

        EXAMPLES::

            sage: # needs sage.graphs
            sage: dag = SkewPartition([[3, 3, 1], [1, 1]]).to_dag()
            sage: dag.edges(sort=True)
            [('0,1', '0,2', None),
            ('0,1', '1,1', None),
            ('0,2', '1,2', None),
            ('1,1', '1,2', None)]
            sage: dag.vertices(sort=True)
            ['0,1', '0,2', '1,1', '1,2', '2,0']
            sage: dag = SkewPartition([[3, 2, 1], [1, 1]]).to_dag(format='tuple')
            sage: dag.edges(sort=True)
            [((0, 1), (0, 2), None), ((0, 1), (1, 1), None)]
            sage: dag.vertices(sort=True)
            [(0, 1), (0, 2), (1, 1), (2, 0)]
        """
    def quotient(self, k):
        """
        The quotient map extended to skew partitions.

        EXAMPLES::

            sage: SkewPartition([[3, 3, 2, 1], [2, 1]]).quotient(2)
            [[3] / [], [] / []]
        """
    def rows_intersection_set(self):
        """
        Return the set of cells in the rows of the outer shape of
        ``self`` which rows intersect the skew diagram of ``self``.

        EXAMPLES::

            sage: skp = SkewPartition([[3,2,1],[2,1]])
            sage: cells = Set([ (0,0), (0, 1), (0,2), (1, 0), (1, 1), (2, 0)])
            sage: skp.rows_intersection_set() == cells
            True
        """
    def columns_intersection_set(self):
        """
        Return the set of cells in the columns of the outer shape of
        ``self`` which columns intersect the skew diagram of ``self``.

        EXAMPLES::

            sage: skp = SkewPartition([[3,2,1],[2,1]])
            sage: cells = Set([ (0,0), (0, 1), (0,2), (1, 0), (1, 1), (2, 0)])
            sage: skp.columns_intersection_set() == cells
            True
        """
    def pieri_macdonald_coeffs(self):
        """
        Computation of the coefficients which appear in the Pieri formula
        for Macdonald polynomials given in his book ( Chapter 6.6 formula
        6.24(ii) )

        EXAMPLES::

            sage: SkewPartition([[3,2,1],[2,1]]).pieri_macdonald_coeffs()
            1
            sage: SkewPartition([[3,2,1],[2,2]]).pieri_macdonald_coeffs()
            (q^2*t^3 - q^2*t - t^2 + 1)/(q^2*t^3 - q*t^2 - q*t + 1)
            sage: SkewPartition([[3,2,1],[2,2,1]]).pieri_macdonald_coeffs()
            (q^6*t^8 - q^6*t^6 - q^4*t^7 - q^5*t^5 + q^4*t^5 - q^3*t^6 + q^5*t^3 + 2*q^3*t^4 + q*t^5 - q^3*t^2 + q^2*t^3 - q*t^3 - q^2*t - t^2 + 1)/(q^6*t^8 - q^5*t^7 - q^5*t^6 - q^4*t^6 + q^3*t^5 + 2*q^3*t^4 + q^3*t^3 - q^2*t^2 - q*t^2 - q*t + 1)
            sage: SkewPartition([[3,3,2,2],[3,2,2,1]]).pieri_macdonald_coeffs()
            (q^5*t^6 - q^5*t^5 + q^4*t^6 - q^4*t^5 - q^4*t^3 + q^4*t^2 - q^3*t^3 - q^2*t^4 + q^3*t^2 + q^2*t^3 - q*t^4 + q*t^3 + q*t - q + t - 1)/(q^5*t^6 - q^4*t^5 - q^3*t^4 - q^3*t^3 + q^2*t^3 + q^2*t^2 + q*t - 1)
        """
    def k_conjugate(self, k):
        """
        Return the `k`-conjugate of the skew partition.

        EXAMPLES::

            sage: SkewPartition([[3,2,1],[2,1]]).k_conjugate(3)
            [2, 1, 1, 1, 1] / [2, 1]
            sage: SkewPartition([[3,2,1],[2,1]]).k_conjugate(4)
            [2, 2, 1, 1] / [2, 1]
            sage: SkewPartition([[3,2,1],[2,1]]).k_conjugate(5)
            [3, 2, 1] / [2, 1]
        """
    def jacobi_trudi(self):
        """
        Return the Jacobi-Trudi matrix of ``self``.

        EXAMPLES::

            sage: SkewPartition([[3,2,1],[2,1]]).jacobi_trudi()                         # needs sage.modules
            [h[1]    0    0]
            [h[3] h[1]    0]
            [h[5] h[3] h[1]]
            sage: SkewPartition([[4,3,2],[2,1]]).jacobi_trudi()                         # needs sage.modules
            [h[2]  h[]    0]
            [h[4] h[2]  h[]]
            [h[6] h[4] h[2]]
        """
    def outside_corners(self):
        """
        Return the outside corners of ``self``.

        The outside corners are corners which are outside of the shape. This
        should not be confused with :meth:`outer_corners` which consists of
        corners inside the shape. It returns a result analogous to the
        ``.outside_corners()`` method on (non-skew) ``Partitions``.

        .. SEEALSO::

            - :meth:`sage.combinat.skew_partition.SkewPartition.outer_corners`
            - :meth:`sage.combinat.partition.Partition.outside_corners`

        EXAMPLES::

            sage: mu = SkewPartition([[3,2,1],[2,1]])
            sage: mu.pp()
              *
             *
            *
            sage: mu.outside_corners()
            [(0, 3), (1, 2), (2, 1), (3, 0)]
        """
    def specht_module(self, base_ring=None):
        """
        Return the Specht module corresponding to ``self``.

        EXAMPLES::

            sage: mu = SkewPartition([[3,2,1], [2]])
            sage: SM = mu.specht_module(QQ)                                             # needs sage.modules
            sage: s = SymmetricFunctions(QQ).s()                                        # needs sage.modules
            sage: s(SM.frobenius_image())                                               # needs sage.modules
            s[2, 1, 1] + s[2, 2] + s[3, 1]

        We verify that the Frobenius image is the corresponding
        skew Schur function::

            sage: s[3,2,1].skew_by(s[2])                                                # needs sage.modules
            s[2, 1, 1] + s[2, 2] + s[3, 1]

        ::

            sage: mu = SkewPartition([[4,2,1], [2,1]])
            sage: SM = mu.specht_module(QQ)                                             # needs sage.modules
            sage: s(SM.frobenius_image())                                               # needs sage.modules
            s[2, 1, 1] + s[2, 2] + 2*s[3, 1] + s[4]
            sage: s(mu)                                                                 # needs sage.modules
            s[2, 1, 1] + s[2, 2] + 2*s[3, 1] + s[4]
        """
    def specht_module_dimension(self, base_ring=None):
        """
        Return the dimension of the Specht module corresponding to ``self``.

        This is equal to the number of standard (skew) tableaux of
        shape ``self``.

        EXAMPLES::

            sage: mu = SkewPartition([[3,2,1], [2]])
            sage: mu.specht_module_dimension()                                          # needs sage.modules
            8
            sage: mu.specht_module_dimension(GF(2))                                     # needs sage.modules sage.rings.finite_rings
            8
        """

def row_lengths_aux(skp):
    """
    EXAMPLES::

        sage: from sage.combinat.skew_partition import row_lengths_aux
        sage: row_lengths_aux([[5,4,3,1],[3,3,1]])
        [2, 1, 2]
        sage: row_lengths_aux([[5,4,3,1],[3,1]])
        [2, 3]
    """

class SkewPartitions(UniqueRepresentation, Parent):
    """
    Skew partitions.

    .. WARNING::

        The iterator of this class only yields skew partitions which
        are reduced, in the sense that there are no empty rows
        before the last nonempty row, and there are no empty columns
        before the last nonempty column.

    EXAMPLES::

        sage: SkewPartitions(4)
        Skew partitions of 4
        sage: SkewPartitions(4).cardinality()
        28
        sage: SkewPartitions(row_lengths=[2,1,2])
        Skew partitions with row lengths [2, 1, 2]
        sage: SkewPartitions(4, overlap=2)
        Skew partitions of 4 with a minimum overlap of 2
        sage: SkewPartitions(4, overlap=2).list()
        [[4] / [], [2, 2] / []]
    """
    @staticmethod
    def __classcall_private__(self, n=None, row_lengths=None, overlap: int = 0):
        """
        Return the correct parent based upon the input.

        EXAMPLES::

            sage: SP1 = SkewPartitions(row_lengths=(2,1,2))
            sage: SP2 = SkewPartitions(row_lengths=[2,1,2])
            sage: SP1 is SP2
            True
        """
    def __init__(self, is_infinite: bool = False) -> None:
        """
        TESTS::

            sage: S = SkewPartitions()
            sage: TestSuite(S).run()
        """
    class options(GlobalOptions):
        '''
        Set and display the options for elements of the skew partition
        classes.  If no parameters are set, then the function returns a copy of
        the options dictionary.

        The ``options`` to skew partitions can be accessed as the method
        :obj:`SkewPartitions.options` of :class:`SkewPartitions` and
        related parent classes.

        @OPTIONS@

        EXAMPLES::

            sage: SP = SkewPartition([[4,2,2,1], [3, 1, 1]])
            sage: SP
            [4, 2, 2, 1] / [3, 1, 1]
            sage: SkewPartitions.options.display="lists"
            sage: SP
            [[4, 2, 2, 1], [3, 1, 1]]

        Changing the ``convention`` for skew partitions also changes the
        ``convention`` option for partitions and tableaux and vice versa::

            sage: SkewPartitions.options(display=\'diagram\', convention=\'French\')
            sage: SP
            *
             *
             *
               *
            sage: T = Tableau([[1,2,3],[4,5]])
            sage: T.pp()
              4  5
              1  2  3
            sage: P = Partition([4, 2, 2, 1])
            sage: P.pp()
            *
            **
            **
            ****
            sage: Tableaux.options.convention="english"
            sage: SP
               *
             *
             *
            *
            sage: T.pp()
              1  2  3
              4  5
            sage: SkewPartitions.options._reset()
        '''
        NAME: str
        module: str
        display: Incomplete
        latex: Incomplete
        diagram_str: Incomplete
        latex_diagram_str: Incomplete
        latex_marking_str: Incomplete
        convention: Incomplete
        notation: Incomplete
    Element = SkewPartition
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: [[], []] in SkewPartitions()
            True
            sage: [[], [1]] in SkewPartitions()
            False
            sage: [[], [-1]] in SkewPartitions()
            False
            sage: [[], [0]] in SkewPartitions()
            True
            sage: [[3,2,1],[]] in SkewPartitions()
            True
            sage: [[3,2,1],[1]] in SkewPartitions()
            True
            sage: [[3,2,1],[2]] in SkewPartitions()
            True
            sage: [[3,2,1],[3]] in SkewPartitions()
            True
            sage: [[3,2,1],[4]] in SkewPartitions()
            False
            sage: [[3,2,1],[1,1]] in SkewPartitions()
            True
            sage: [[3,2,1],[1,2]] in SkewPartitions()
            False
            sage: [[3,2,1],[2,1]] in SkewPartitions()
            True
            sage: [[3,2,1],[2,2]] in SkewPartitions()
            True
            sage: [[3,2,1],[3,2]] in SkewPartitions()
            True
            sage: [[3,2,1],[1,1,1]] in SkewPartitions()
            True
            sage: [[7, 4, 3, 2], [8, 2, 1]] in SkewPartitions()
            False
            sage: [[7, 4, 3, 2], [5, 2, 1]] in SkewPartitions()
            True
            sage: [[4,2,1],[1,1,1,1]] in SkewPartitions()
            False
            sage: [[1,1,1,0],[1,1,0,0]] in SkewPartitions()
            True
        """
    def from_row_and_column_length(self, rowL, colL):
        """
        Construct a partition from its row lengths and column lengths.

        INPUT:

        - ``rowL`` -- a composition or a list of positive integers

        - ``colL`` -- a composition or a list of positive integers

        OUTPUT:

        - If it exists the unique skew-partitions with row lengths ``rowL``
          and column lengths ``colL``.
        - Raise a :exc:`ValueError` if ``rowL`` and ``colL`` are not compatible.

        EXAMPLES::

            sage: S = SkewPartitions()
            sage: print(S.from_row_and_column_length([3,1,2,2],[2,3,1,1,1]).diagram())
              ***
             *
            **
            **
            sage: S.from_row_and_column_length([],[])
            [] / []
            sage: S.from_row_and_column_length([1],[1])
            [1] / []
            sage: S.from_row_and_column_length([2,1],[2,1])
            [2, 1] / []
            sage: S.from_row_and_column_length([1,2],[1,2])
            [2, 2] / [1]
            sage: S.from_row_and_column_length([1,2],[1,3])
            Traceback (most recent call last):
            ...
            ValueError: sum mismatch: [1, 2] and [1, 3]
            sage: S.from_row_and_column_length([3,2,1,2],[2,3,1,1,1])
            Traceback (most recent call last):
            ...
            ValueError: incompatible row and column length : [3, 2, 1, 2] and [2, 3, 1, 1, 1]

        .. WARNING::

            If some rows and columns have length zero, there is no way to retrieve
            unambiguously the skew partition. We therefore raise
            a :exc:`ValueError`.
            For examples here are two skew partitions with the same row and column
            lengths::

                sage: skp1 = SkewPartition([[2,2],[2,2]])
                sage: skp2 = SkewPartition([[2,1],[2,1]])
                sage: skp1.row_lengths(), skp1.column_lengths()
                ([0, 0], [0, 0])
                sage: skp2.row_lengths(), skp2.column_lengths()
                ([0, 0], [0, 0])
                sage: SkewPartitions().from_row_and_column_length([0,0], [0,0])
                Traceback (most recent call last):
                ...
                ValueError: row and column length must be positive

        TESTS::

            sage: all(SkewPartitions().from_row_and_column_length(p.row_lengths(), p.column_lengths()) == p
            ....:       for i in range(7) for p in SkewPartitions(i))
            True
        """

class SkewPartitions_all(SkewPartitions):
    """
    Class of all skew partitions.
    """
    def __init__(self) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: S = SkewPartitions()
            sage: TestSuite(S).run()
        """
    def __iter__(self):
        """
        Iterate over ``self``.

        EXAMPLES::

            sage: SP = SkewPartitions()
            sage: it = SP.__iter__()
            sage: [next(it) for x in range(10)]
            [[] / [],
             [1] / [],
             [2] / [],
             [1, 1] / [],
             [2, 1] / [1],
             [3] / [],
             [2, 1] / [],
             [3, 1] / [1],
             [2, 2] / [1],
             [3, 2] / [2]]
        """

class SkewPartitions_n(SkewPartitions):
    '''
    The set of skew partitions of ``n`` with overlap at least
    ``overlap`` and no empty row.

    INPUT:

    - ``n`` -- nonnegative integer

    - ``overlap`` -- integer (default: `0`)

    Caveat: this set is stable under conjugation only for ``overlap`` equal
    to 0 or 1. What exactly happens for negative overlaps is not yet
    well specified and subject to change (we may want to
    introduce vertical overlap constraints as well).

    .. TODO::

        As is, this set is essentially the composition of
        ``Compositions(n)`` (which give the row lengths) and
        ``SkewPartition(n, row_lengths=...)``, and one would want to
        "inherit" list and cardinality from this composition.
    '''
    @staticmethod
    def __classcall_private__(cls, n, overlap: int = 0):
        """
        Normalize input so we have a unique representation.

        EXAMPLES::

            sage: S = SkewPartitions(3, overlap=1)
            sage: S2 = SkewPartitions(int(3), overlap='connected')
            sage: S is S2
            True
        """
    n: Incomplete
    overlap: Incomplete
    def __init__(self, n, overlap) -> None:
        '''
        Return the set of the skew partitions of ``n`` with overlap
        at least ``overlap``, and no empty row.

        The iteration order is not specified yet.

        Caveat: this set is stable under conjugation only for overlap=
        0 or 1. What exactly happens for negative overlaps is not yet
        well specified, and subject to change (we may want to
        introduce vertical overlap constraints as well). ``overlap`` would
        also better be named ``min_overlap``.

        Todo: as is, this set is essentially the composition of
        ``Compositions(n)`` (which give the row lengths) and
        ``SkewPartition(n, row_lengths=...)``, and one would want to
        "inherit" list and cardinality from this composition.

        INPUT:

        - ``n`` -- nonnegative integer
        - ``overlap`` -- integer

        TESTS::

            sage: S = SkewPartitions(3)
            sage: TestSuite(S).run()
            sage: S = SkewPartitions(3, overlap=1)
            sage: TestSuite(S).run()
        '''
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: [[],[]] in SkewPartitions(0)
            True
            sage: [[3,2,1], []] in SkewPartitions(6)
            True
            sage: [[3,2,1], []] in SkewPartitions(7)
            False
            sage: [[3,2,1], []] in SkewPartitions(5)
            False
            sage: [[7, 4, 3, 2], [8, 2, 1]] in SkewPartitions(8)
            False
            sage: [[7, 4, 3, 2], [5, 2, 1]] in SkewPartitions(8)
            False
            sage: [[7, 4, 3, 2], [5, 2, 1]] in SkewPartitions(5)
            False
            sage: [[7, 4, 3, 2], [5, 2, 1]] in SkewPartitions(5, overlap=-1)
            False
            sage: [[7, 4, 3, 2], [5, 2, 1]] in SkewPartitions(8, overlap=-1)
            True
            sage: [[7, 4, 3, 2], [5, 2, 1]] in SkewPartitions(8, overlap=0)
            False
            sage: [[7, 4, 3, 2], [5, 2, 1]] in SkewPartitions(8, overlap='connected')
            False
            sage: [[7, 4, 3, 2], [5, 2, 1]] in SkewPartitions(8, overlap=-2)
            True
        """
    def cardinality(self):
        """
        Return the number of skew partitions of the integer `n`
        (with given overlap, if specified; and with no empty rows before
        the last row).

        EXAMPLES::

            sage: SkewPartitions(0).cardinality()
            1
            sage: SkewPartitions(4).cardinality()
            28
            sage: SkewPartitions(5).cardinality()
            87
            sage: SkewPartitions(4, overlap=1).cardinality()
            9
            sage: SkewPartitions(5, overlap=1).cardinality()
            20
            sage: s = SkewPartitions(5, overlap=-1)
            sage: s.cardinality() == len(s.list())
            True
        """
    def __iter__(self):
        """
        Iterate through the skew partitions of `n`
        (with given overlap, if specified; and with no empty rows before
        the last row).

        EXAMPLES::

            sage: SkewPartitions(3).list()
            [[3] / [],
             [2, 1] / [],
             [3, 1] / [1],
             [2, 2] / [1],
             [3, 2] / [2],
             [1, 1, 1] / [],
             [2, 2, 1] / [1, 1],
             [2, 1, 1] / [1],
             [3, 2, 1] / [2, 1]]

            sage: SkewPartitions(3, overlap=0).list()
            [[3] / [],
             [2, 1] / [],
             [3, 1] / [1],
             [2, 2] / [1],
             [3, 2] / [2],
             [1, 1, 1] / [],
             [2, 2, 1] / [1, 1],
             [2, 1, 1] / [1],
             [3, 2, 1] / [2, 1]]
            sage: SkewPartitions(3, overlap=1).list()
            [[3] / [],
             [2, 1] / [],
             [2, 2] / [1],
             [1, 1, 1] / []]
            sage: SkewPartitions(3, overlap=2).list()
            [[3] / []]
            sage: SkewPartitions(3, overlap=3).list()
            [[3] / []]
            sage: SkewPartitions(3, overlap=4).list()
            []
        """

class SkewPartitions_rowlengths(SkewPartitions):
    """
    All skew partitions with given row lengths.
    """
    @staticmethod
    def __classcall_private__(cls, co, overlap: int = 0):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: S = SkewPartitions(row_lengths=[2,1], overlap=1)
            sage: S2 = SkewPartitions(row_lengths=(2,1), overlap='connected')
            sage: S is S2
            True
        """
    co: Incomplete
    overlap: Incomplete
    def __init__(self, co, overlap) -> None:
        """
        TESTS::

            sage: S = SkewPartitions(row_lengths=[2,1])
            sage: TestSuite(S).run()
        """
    def __contains__(self, x) -> bool:
        """
        EXAMPLES::

            sage: [[4,3,1],[2]] in SkewPartitions(row_lengths=[2,3,1])
            True
            sage: [[4,3,1],[2]] in SkewPartitions(row_lengths=[2,1,3])
            False
            sage: [[5,4,3,1],[3,3,1]] in SkewPartitions(row_lengths=[2,1,1,2])
            False
            sage: [[5,4,3,1],[3,3,1]] in SkewPartitions(row_lengths=[2,1,2,1])
            True
        """
    def __iter__(self):
        """
        Iterate through all the skew partitions that have row lengths
        given by the composition ``self.co``.

        EXAMPLES::

            sage: SkewPartitions(row_lengths=[2,2]).list()
            [[2, 2] / [], [3, 2] / [1], [4, 2] / [2]]
            sage: SkewPartitions(row_lengths=[2,2], overlap=1).list()
            [[2, 2] / [], [3, 2] / [1]]
        """
