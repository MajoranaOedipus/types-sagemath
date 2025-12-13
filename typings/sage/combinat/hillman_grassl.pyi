from sage.categories.sets_cat import Sets as Sets
from sage.combinat.combinatorial_map import combinatorial_map as combinatorial_map
from sage.combinat.tableau import Tableau as Tableau, Tableaux as Tableaux

class WeakReversePlanePartition(Tableau):
    """
    A weak reverse plane partition (short: rpp).

    A weak reverse plane partition is a tableau with nonnegative
    entries that are weakly increasing in each row and weakly
    increasing in each column.

    EXAMPLES::

        sage: x = WeakReversePlanePartition([[0, 1, 1], [0, 1, 3], [1, 2, 2], [1, 2, 3], [2]]); x
        [[0, 1, 1], [0, 1, 3], [1, 2, 2], [1, 2, 3], [2]]
        sage: x.pp()
          0  1  1
          0  1  3
          1  2  2
          1  2  3
          2
        sage: x.shape()
        [3, 3, 3, 3, 1]
    """
    @staticmethod
    def __classcall_private__(cls, r):
        """
        Return an rpp object.

        EXAMPLES::

            sage: WeakReversePlanePartition([[1, 2], [1, 3], [1]])
            [[1, 2], [1, 3], [1]]

        TESTS::

            sage: a1 = [[1, 2], [1, 3], [1]]
            sage: a2 = [(1, 2), (1, 3), (1,)]
            sage: A1 = WeakReversePlanePartition(a1)
            sage: A2 = WeakReversePlanePartition(a2)
            sage: A3 = WeakReversePlanePartition(A1)
            sage: A4 = Tableau(A1)
            sage: A1 == A2 == A3 == A4
            True
        """
    def __init__(self, parent, t) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: R = WeakReversePlanePartition([[0, 1, 2], [0, 2]])
            sage: TestSuite(R).run()
        """
    def conjugate(self):
        """
        Return the conjugate of ``self``.

        EXAMPLES::

            sage: c = WeakReversePlanePartition([[1,1],[1,3],[2]]).conjugate(); c
            [[1, 1, 2], [1, 3]]
            sage: c.parent()
            Weak Reverse Plane Partitions
        """
    def hillman_grassl_inverse(self):
        '''
        Return the image of the `\\lambda`-rpp ``self`` under the
        inverse of the Hillman-Grassl correspondence (as a
        :class:`~sage.combinat.tableau.Tableau`).

        Fix a partition `\\lambda`
        (see :meth:`~sage.combinat.partition.Partition`).
        We draw all partitions and tableaux in English notation.

        A `\\lambda`-*array* will mean a tableau of shape `\\lambda` whose
        entries are nonnegative integers. (No conditions on the order of
        these entries are made. Note that `0` is allowed.)

        A *weak reverse plane partition of shape* `\\lambda` (short:
        `\\lambda`-*rpp*) will mean a `\\lambda`-array whose entries weakly
        increase along each row and weakly increase along each column.

        The inverse `H^{-1}` of the Hillman-Grassl correspondence (see
        (:meth:`~sage.combinat.tableau.Tableau.hillman_grassl` for the
        latter) sends a `\\lambda`-rpp `\\pi` to a `\\lambda`-array
        `H^{-1}(\\pi)` constructed recursively as follows:

        * If all entries of `\\pi` are `0`, then `H^{-1}(\\pi) = \\pi`.

        * Otherwise, let `s` be the index of the leftmost column of `\\pi`
          containing a nonzero entry. Write the `\\lambda`-array `M`
          as `(m_{i, j})`.

        * Define a sequence `((i_1, j_1), (i_2, j_2), \\ldots,
          (i_n, j_n))` of boxes in the diagram of `\\lambda` (actually a
          lattice path made of northward and eastward steps) as follows:
          Let `(i_1, j_1)` be the bottommost box in the `s`-th column
          of `\\pi`.
          If `(i_k, j_k)` is defined for some `k \\geq 1`, then
          `(i_{k+1}, j_{k+1})` is constructed as follows:
          If `q_{i_k - 1, j_k}` is well-defined and equals `q_{i_k, j_k}`,
          then we set `(i_{k+1}, j_{k+1}) = (i_k - 1, j_k)`. Otherwise,
          we set `(i_{k+1}, j_{k+1}) = (i_k, j_k + 1)` if this is still
          a box of `\\lambda`. Otherwise, the sequence ends here.

        * Let `\\pi\'` be the `\\lambda`-rpp obtained from `\\pi` by
          subtracting `1` from the `(i_k, j_k)`-th entry of `\\pi` for each
          `k \\in \\{1, 2, \\ldots, n\\}`.

        * Let `N\'` be the image `H^{-1}(\\pi\')` (which is already
          constructed by recursion).
          Then, `H^{-1}(\\pi)` is obtained from `N\'` by adding `1` to the
          `(i_n, s)`-th entry of `N\'`.

        This construction appears in [HilGra1976]_ Section 6 (where
        `\\lambda`-arrays are re-encoded as sequences of "hook number
        multiplicities") and [EnumComb2]_ Section 7.22.

        .. SEEALSO::

            :meth:`~sage.combinat.hillman_grassl.hillman_grassl_inverse`
            for the inverse of the Hillman-Grassl correspondence as a
            standalone function.

            :meth:`~sage.combinat.tableau.Tableau.hillman_grassl`
            for the inverse map.

        EXAMPLES::

            sage: a = WeakReversePlanePartition([[2, 2, 4], [2, 3, 4], [3, 5]])
            sage: a.hillman_grassl_inverse()
            [[2, 1, 1], [0, 2, 0], [1, 1]]
            sage: b = WeakReversePlanePartition([[1, 1, 2, 2], [1, 1, 2, 2], [2, 2, 3, 3], [2, 2, 3, 3]])
            sage: B = b.hillman_grassl_inverse(); B
            [[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1]]
            sage: b.parent(), B.parent()
            (Weak Reverse Plane Partitions, Tableaux)

        Applying the inverse of the Hillman-Grassl correspondence
        to the transpose of a `\\lambda`-rpp `M` yields the same
        result as applying it to `M` and then transposing the
        result ([Gans1981]_ Corollary 3.4)::

            sage: a = WeakReversePlanePartition([[1,3,5],[2,4]])
            sage: aic = a.hillman_grassl_inverse().conjugate()
            sage: aic == a.conjugate().hillman_grassl_inverse()
            True
        '''
    def pak_correspondence(self):
        """
        Return the image of the `\\lambda`-rpp ``self`` under the Pak
        correspondence (as a :class:`~sage.combinat.tableau.Tableau`).

        See :mod:`~sage.combinat.hillman_grassl`.

        The Pak correspondence is the map `\\xi_\\lambda`
        from [Sulzgr2017]_ Section 7, and is the map
        `\\xi_\\lambda` from [Pak2002]_ Section 4.
        It is the inverse of the Sulzgruber correspondence
        (:meth:`sulzgruber_correspondence`).
        The following description of the Pak correspondence follows
        [Hopkins2017]_ (which denotes it by `\\mathcal{RSK}^{-1}`):

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
          `\\max \\{ \\pi_{u-1, v} , \\pi_{u, v-1} \\}`
          (where `\\pi_{0, v}` and `\\pi_{u, 0}` are understood to
          mean `0`).

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

        Note also that the lower bound of `\\pi` at `(u, v)` is
        defined (and finite) even when `(u, v)` is not a cell of
        `\\lambda`, as long as both `(u-1, v)` and `(u, v-1)` are
        cells of `\\lambda`.

        The Pak correspondence `\\Phi_\\lambda` sends a `\\lambda`-array
        `M = (m_{i, j})` to a `\\lambda`-rpp `\\Phi_\\lambda(M)`. It
        is defined by recursion on `\\lambda` (that is, we assume that
        `\\Phi_\\mu` is already defined for every partition `\\mu`
        smaller than `\\lambda`), and its definition proceeds as
        follows:

        * If `\\lambda = \\varnothing`, then `\\Phi_\\lambda` is the
          obvious bijection sending the only `\\varnothing`-array
          to the only `\\varnothing`-rpp.

        * Pick any corner `c = (i, j)` of `\\lambda`, and let `\\mu`
          be the result of removing this corner `c` from the partition
          `\\lambda`. (The exact choice of `c` is immaterial.)

        * Let `M'` be what remains of `M` when the corner cell `c`
          is removed.

        * Let `\\pi' = \\Phi_\\mu(M')`.

        * For each positive integer `k` such that `(i-k, j-k)` is a
          cell of `\\lambda`, toggle `\\pi'` at `(i-k, j-k)`.
          (All these togglings commute, so the order in which they
          are made is immaterial.)

        * Extend the `\\mu`-rpp `\\pi'` to a `\\lambda`-rpp `\\pi` by
          adding the cell `c` and writing the number
          `m_{i, j} - \\pi'_{<(i, j)}` into this cell.

        * Set `\\Phi_\\lambda(M) = \\pi`.

        .. SEEALSO::

            :meth:`~sage.combinat.hillman_grassl.pak_correspondence`
            for the Pak correspondence as a standalone function.

            :meth:`~sage.combinat.tableau.Tableau.sulzgruber_correspondence`
            for the inverse map.

        EXAMPLES::

            sage: a = WeakReversePlanePartition([[1, 2, 3], [1, 2, 3], [2, 4, 4]])
            sage: A = a.pak_correspondence(); A
            [[1, 0, 2], [0, 2, 0], [1, 1, 0]]
            sage: a.parent(), A.parent()
            (Weak Reverse Plane Partitions, Tableaux)

        Applying the Pak correspondence to the transpose of a
        `\\lambda`-rpp `M` yields the same result as applying it to
        `M` and then transposing the result::

            sage: a = WeakReversePlanePartition([[1,3,5],[2,4]])
            sage: acc = a.pak_correspondence().conjugate()
            sage: acc == a.conjugate().pak_correspondence()
            True
        """

class WeakReversePlanePartitions(Tableaux):
    """
    The set of all weak reverse plane partitions.
    """
    @staticmethod
    def __classcall_private__(cls, shape=None, **kwds):
        """
        Normalize input to ensure a unique representation and
        return the correct class based on input.

        The ``shape`` parameter is currently not implemented.

        EXAMPLES::

            sage: S1 = WeakReversePlanePartitions()
            sage: S2 = WeakReversePlanePartitions()
            sage: S1 is S2
            True

            sage: S1 = WeakReversePlanePartitions([4, 2, 2, 1])  # not tested (not implemented)
            sage: S2 = WeakReversePlanePartitions((4, 2, 2, 1))  # not tested (not implemented)
            sage: S1 is S2  # not tested (not implemented)
            True
        """
    def __init__(self) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: S = WeakReversePlanePartitions()
            sage: TestSuite(S).run()
        """
    Element = WeakReversePlanePartition

def transpose(M):
    """
    Return the transpose of a `\\lambda`-array.

    The transpose of a `\\lambda`-array `(m_{i, j})` is the
    `\\lambda^t`-array `(m_{j, i})`
    (where `\\lambda^t` is the conjugate of the partition
    `\\lambda`).

    EXAMPLES::

        sage: from sage.combinat.hillman_grassl import transpose
        sage: transpose([[1, 2, 3], [4, 5]])
        [[1, 4], [2, 5], [3]]
        sage: transpose([[5, 0, 3], [4, 1, 0], [7]])
        [[5, 4, 7], [0, 1], [3, 0]]

    TESTS::

        sage: transpose(((2, 1), (3,)))
        [[2, 3], [1]]
        sage: transpose([])
        []
        sage: transpose(WeakReversePlanePartition([[1, 2, 3], [4, 5]]))
        [[1, 4], [2, 5], [3]]
        sage: transpose(WeakReversePlanePartition([]))
        []
    """
def hillman_grassl(M):
    """
    Return the image of the `\\lambda`-array ``M``
    under the Hillman-Grassl correspondence.

    The Hillman-Grassl correspondence is a bijection
    between the tableaux with nonnegative entries
    (otherwise arbitrary) and the weak reverse plane
    partitions with nonnegative entries.
    This bijection preserves the shape of the
    tableau. See :mod:`~sage.combinat.hillman_grassl`.

    See :meth:`~sage.combinat.tableau.Tableau.hillman_grassl`
    for a description of this map.

    .. SEEALSO::

        :meth:`hillman_grassl_inverse`

    EXAMPLES::

        sage: from sage.combinat.hillman_grassl import hillman_grassl
        sage: hillman_grassl([[2, 1, 1], [0, 2, 0], [1, 1]])
        [[2, 2, 4], [2, 3, 4], [3, 5]]
        sage: hillman_grassl([[1, 2, 0], [1, 0, 1], [1]])
        [[0, 1, 3], [2, 4, 4], [3]]
        sage: hillman_grassl([])
        []
        sage: hillman_grassl([[3, 1, 2]])
        [[3, 4, 6]]
        sage: hillman_grassl([[2, 2, 0], [1, 1, 1], [1]])
        [[1, 2, 4], [3, 5, 5], [4]]
        sage: hillman_grassl([[1, 1, 1, 1]]*3)
        [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]

    TESTS::

        sage: hillman_grassl(((2, 2, 0), (1, 1, 1), (1,)))
        [[1, 2, 4], [3, 5, 5], [4]]
    """
def hillman_grassl_inverse(M):
    """
    Return the image of the `\\lambda`-rpp ``M`` under the
    inverse of the Hillman-Grassl correspondence.

    See :mod:`~sage.combinat.hillman_grassl`.

    See
    :meth:`~sage.combinat.hillman_grassl.WeakReversePlanePartition.hillman_grassl_inverse`
    for a description of this map.

    .. SEEALSO::

        :meth:`hillman_grassl`

    EXAMPLES::

        sage: from sage.combinat.hillman_grassl import hillman_grassl_inverse
        sage: hillman_grassl_inverse([[2, 2, 4], [2, 3, 4], [3, 5]])
        [[2, 1, 1], [0, 2, 0], [1, 1]]
        sage: hillman_grassl_inverse([[0, 1, 3], [2, 4, 4], [3]])
        [[1, 2, 0], [1, 0, 1], [1]]

    Applying the inverse of the Hillman-Grassl correspondence
    to the transpose of a `\\lambda`-rpp `M` yields the same
    result as applying it to `M` and then transposing the
    result ([Gans1981]_ Corollary 3.4)::

        sage: hillman_grassl_inverse([[1,3,5],[2,4]])
        [[1, 2, 2], [1, 1]]
        sage: hillman_grassl_inverse([[1,2],[3,4],[5]])
        [[1, 1], [2, 1], [2]]
        sage: hillman_grassl_inverse([[1, 2, 3], [1, 2, 3], [2, 4, 4]])
        [[1, 2, 0], [0, 1, 1], [1, 0, 1]]
        sage: hillman_grassl_inverse([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]])
        [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]

    TESTS::

        sage: a = [[3], [4], [6]]
        sage: hillman_grassl_inverse(a)
        [[3], [1], [2]]
        sage: a
        [[3], [4], [6]]

        sage: hillman_grassl_inverse(((1,2),(3,4),(5,)))
        [[1, 1], [2, 1], [2]]
    """
def sulzgruber_correspondence(M):
    """
    Return the image of a `\\lambda`-array ``M``
    under the Sulzgruber correspondence.

    The Sulzgruber correspondence is the map `\\Phi_\\lambda`
    from [Sulzgr2017]_ Section 7, and is the map
    `\\xi_\\lambda^{-1}` from [Pak2002]_ Section 5.
    It is denoted by `\\mathcal{RSK}` in [Hopkins2017]_.
    It is the inverse of the Pak correspondence
    (:meth:`pak_correspondence`).

    See :meth:`~sage.combinat.tableau.Tableau.sulzgruber_correspondence`
    for a description of this map.

    EXAMPLES::

        sage: from sage.combinat.hillman_grassl import sulzgruber_correspondence
        sage: sulzgruber_correspondence([[1, 0, 2], [0, 2, 0], [1, 1, 0]])
        [[1, 2, 3], [1, 2, 3], [2, 4, 4]]
        sage: sulzgruber_correspondence([[1, 1, 2], [0, 1, 0], [3, 0, 0]])
        [[1, 1, 4], [2, 3, 4], [4, 4, 4]]
        sage: sulzgruber_correspondence([[1, 0, 2], [0, 2, 0], [1, 1]])
        [[0, 2, 3], [1, 3, 3], [2, 4]]
        sage: sulzgruber_correspondence([[0, 2, 2], [1, 1], [2]])
        [[1, 2, 4], [1, 3], [3]]
        sage: sulzgruber_correspondence([[1, 1, 1, 1]]*3)
        [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]

    The Sulzgruber correspondence can actually be
    extended (by the same definition) to arrays
    of nonnegative reals rather than nonnegative
    integers. This implementation supports this::

        sage: sulzgruber_correspondence([[1/2, 0, 1], [0, 1, 0], [1/2, 1/2]])
        [[0, 1, 3/2], [1/2, 3/2, 3/2], [1, 2]]

    TESTS::

        sage: sulzgruber_correspondence([])
        []
        sage: sulzgruber_correspondence(((0, 2, 2), (1, 1), (2,)))
        [[1, 2, 4], [1, 3], [3]]
    """
def pak_correspondence(M, copy: bool = True):
    '''
    Return the image of a `\\lambda`-rpp ``M``
    under the Pak correspondence.

    The Pak correspondence is the map `\\xi_\\lambda`
    from [Sulzgr2017]_ Section 7, and is the map
    `\\xi_\\lambda` from [Pak2002]_ Section 4.
    It is the inverse of the Sulzgruber correspondence
    (:meth:`sulzgruber_correspondence`).

    See
    :meth:`~sage.combinat.hillman_grassl.WeakReversePlanePartition.pak_correspondence`
    for a description of this map.

    INPUT:

    - ``copy`` -- boolean (default: ``True``); if set to ``False``, the
      algorithm will mutate the input (but be more efficient)

    EXAMPLES::

        sage: from sage.combinat.hillman_grassl import pak_correspondence
        sage: pak_correspondence([[1, 2, 3], [1, 2, 3], [2, 4, 4]])
        [[1, 0, 2], [0, 2, 0], [1, 1, 0]]
        sage: pak_correspondence([[1, 1, 4], [2, 3, 4], [4, 4, 4]])
        [[1, 1, 2], [0, 1, 0], [3, 0, 0]]
        sage: pak_correspondence([[0, 2, 3], [1, 3, 3], [2, 4]])
        [[1, 0, 2], [0, 2, 0], [1, 1]]
        sage: pak_correspondence([[1, 2, 4], [1, 3], [3]])
        [[0, 2, 2], [1, 1], [2]]
        sage: pak_correspondence([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]])
        [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]

    The Pak correspondence can actually be
    extended (by the same definition) to "rpps"
    of nonnegative reals rather than nonnegative
    integers. This implementation supports this::

        sage: pak_correspondence([[0, 1, 3/2], [1/2, 3/2, 3/2], [1, 2]])
        [[1/2, 0, 1], [0, 1, 0], [1/2, 1/2]]

    TESTS::

        sage: pak_correspondence([])
        []
        sage: pak_correspondence(((1, 2, 4), (1, 3), (3,)))
        [[0, 2, 2], [1, 1], [2]]

        sage: a = [[0, 2, 3], [1, 3, 3], [2, 4]]
        sage: pak_correspondence(a)
        [[1, 0, 2], [0, 2, 0], [1, 1]]
        sage: a
        [[0, 2, 3], [1, 3, 3], [2, 4]]
        sage: pak_correspondence(a, copy=False)
        [[1, 0, 2], [0, 2, 0], [1, 1]]
        sage: a
        []
    '''
