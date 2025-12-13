from .partition_tuple import PartitionTuple as PartitionTuple
from .tableau_tuple import RowStandardTableauTuples_residue as RowStandardTableauTuples_residue, RowStandardTableauTuples_residue_shape as RowStandardTableauTuples_residue_shape, StandardTableaux_residue as StandardTableaux_residue, StandardTableaux_residue_shape as StandardTableaux_residue_shape
from sage.categories.sets_cat import Sets as Sets
from sage.misc.inherit_comparison import InheritComparisonClasscallMetaclass as InheritComparisonClasscallMetaclass
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as IntegerModRing
from sage.structure.list_clone import ClonableArray as ClonableArray
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class ResidueSequence(ClonableArray, metaclass=InheritComparisonClasscallMetaclass):
    """
    A residue sequence.

    The *residue sequence* of a tableau `t` (of partition or partition tuple
    shape) is the sequence `(i_1, i_2, \\ldots, i_n)` where `i_k` is the
    residue of `l` in `t`, for `k = 1, 2, \\ldots, n`, where `n` is the
    size of `t`. Residue sequences are important in the representation
    theory of the cyclotomic Hecke algebras of type `G(r, 1, n)`, and
    of the cyclotomic quiver Hecke algebras, because they determine the
    eigenvalues of the Jucys-Murphy elements upon all modules. More precisely,
    they index and completely determine the irreducible representations
    of the (cyclotomic) Gelfand-Tsetlin algebras.

    Rather than being called directly, residue sequences are best accessed
    via the standard tableaux classes :class:`StandardTableau` and
    :class:`StandardTableauTuple`.

    INPUT:

    Can be of the form:

    - ``ResidueSequence(e, res)``,
    - ``ResidueSequence(e, multicharge, res)``,

    where ``e`` is a positive integer not equal to 1 and ``res`` is a
    sequence of integers (the residues).

    EXAMPLES::

        sage: res = StandardTableauTuple([[[1,3],[6]],[[2,7],[4],[5]]]).residue_sequence(3,(0,5))
        sage: res
        3-residue sequence (0,2,1,1,0,2,0) with multicharge (0,2)
        sage: res.quantum_characteristic()
        3
        sage: res.level()
        2
        sage: res.size()
        7
        sage: res.residues()
        [0, 2, 1, 1, 0, 2, 0]
        sage: res.restrict(2)
        3-residue sequence (0,2) with multicharge (0,2)
        sage: res.standard_tableaux([[2,1],[1],[2,1]])
        Standard (2,1|1|2,1)-tableaux with 3-residue sequence (0,2,1,1,0,2,0) and multicharge (0,2)
        sage: res.standard_tableaux([[2,2],[3]]).list()
        []
        sage: res.standard_tableaux([[2,2],[3]])[:]
        []
        sage: res.standard_tableaux()
        Standard tableaux with 3-residue sequence (0,2,1,1,0,2,0) and multicharge (0,2)
        sage: res.standard_tableaux()[:10]
        [([[1, 3, 6, 7], [2, 5], [4]], []),
         ([[1, 3, 6], [2, 5], [4], [7]], []),
         ([[1, 3], [2, 5], [4, 6], [7]], []),
         ([[1, 3], [2, 5], [4], [7]], [[6]]),
         ([[1, 3], [2, 5], [4]], [[6, 7]]),
         ([[1, 3, 6, 7], [2], [4], [5]], []),
         ([[1, 3, 6], [2, 7], [4], [5]], []),
         ([[1, 3], [2, 7], [4], [5], [6]], []),
         ([[1, 3], [2, 7], [4], [5]], [[6]]),
         ([[1, 3], [2], [4], [5]], [[6, 7]])]

    The TestSuite fails ``_test_pickling`` because ``__getitem__`` does
    not support slices, so we skip this.

    TESTS::

        sage: from sage.combinat.tableau_residues import ResidueSequence
        sage: TestSuite( ResidueSequence(3,(0,0,1), [0,1,2])).run(skip='_test_pickling')
    """
    @staticmethod
    def __classcall_private__(cls, e, multicharge, residues=None, check: bool = True):
        """
        Magic to allow class to accept a list (which is not hashable) instead
        of a partition (which is). At the same time we ensure that every
        residue sequence is constructed as an ``element_class`` call of
        an appropriate parent.

        The ``residues`` must always be specified and, instead, it is the
        ``multicharge`` which is the optional argument with default ``[0]``.
        This means that we have to perform some tricks when ``residues``
        is ``None``.

        EXAMPLES::

            sage: from sage.combinat.tableau_residues import ResidueSequence
            sage: ResidueSequence(3, [0,0,1], [0,0,1,1,2,2,3,3])  # indirect doctest
            3-residue sequence (0,0,1,1,2,2,0,0) with multicharge (0,0,1)
        """
    def __init__(self, parent, residues, check) -> None:
        """
        Initialize ``self``.

        The ``multicharge`` is the optional argument which, if omitted,
        defaults to ``(0,)``. On the other hand, the ``residue`` must
        always be specified so, below, we check to see whether or note
        ``residues`` is ``None`` and adjust accordingly in this case.

        EXAMPLES::

            sage: from sage.combinat.tableau_residues import ResidueSequence
            sage: ResidueSequence(3, (0,0,1), [0,0,1,1,2,2,3,3])
            3-residue sequence (0,0,1,1,2,2,0,0) with multicharge (0,0,1)

        The TestSuite fails ``_test_pickling`` because ``__getitem__`` does
        not support slices, so we skip this.

        TESTS::

            sage: from sage.combinat.tableau_residues import ResidueSequence
            sage: TestSuite(ResidueSequence(3,(0,0,1),[0,0,1,1,2,2,3,3])).run(skip='_test_pickling')
            sage: TestSuite( ResidueSequence(3, [0,1,2])).run(skip='_test_pickling')
            sage: TestSuite( ResidueSequence(3, [0], [0,1,2])).run(skip='_test_pickling')
            sage: TestSuite( ResidueSequence(3, [0,0], [0,0,1,2])).run(skip='_test_pickling')
            sage: TestSuite( ResidueSequence(3, [0,0,1,2])).run(skip='_test_pickling')
        """
    def check(self) -> None:
        """
        Raise a :exc:`ValueError` if ``self`` is not a residue sequence.

        EXAMPLES::

            sage: from sage.combinat.tableau_residues import ResidueSequence
            sage: ResidueSequence(3, [0,0,1], [0,0,1,1,2,2,3,3]).check()
            sage: ResidueSequence(3, [0,0,1], [2,0,1,1,2,2,3,3]).check()
        """
    def __getitem__(self, k):
        """
        Return the ``k``-th residue.

        INPUT:

        - ``k`` --- an integer between 1 and the length of the residue
          sequence ``self``

        The ``k``-th residue is the ``e``-residue (see
        :meth:`sage.combinat.tableau.StandardTable.residue`) of the
        integer ``k`` in some standard tableaux. As the entries of standard
        tableaux are always between `1` and `n`, the size of the tableau,
        the integer ``k`` must also be in this range (that is, this
        is **not** 0-based!).

        EXAMPLES::

            sage: from sage.combinat.tableau_residues import ResidueSequence
            sage: ResidueSequence(3,(0,0,1),[0,0,1,1,2,2,3,3])[4]
            1
            sage: ResidueSequence(3,(0,0,1),[0,0,1,1,2,2,3,3])[7]
            0
            sage: ResidueSequence(3,(0,0,1),[0,0,1,1,2,2,3,3])[9]
            Traceback (most recent call last):
            ...
            IndexError: k must be in the range 1, 2, ..., 8
        """
    def residues(self) -> list:
        """
        Return a list of the residue sequence.

        EXAMPLES::

            sage: from sage.combinat.tableau_residues import ResidueSequence
            sage: ResidueSequence(3,(0,0,1),[0,0,1,1,2,2,3,3]).residues()
            [0, 0, 1, 1, 2, 2, 0, 0]
        """
    def restrict(self, m):
        """
        Return the subsequence of this sequence of length `m`.

        The residue sequence ``self`` is of the form `(r_1, \\ldots, r_n)`.
        The function returns the residue sequence `(r_1, \\ldots, r_m)`, with
        the same  :meth:`quantum_characteristic` and :meth:`multicharge`.

        EXAMPLES::

            sage: from sage.combinat.tableau_residues import ResidueSequence
            sage: ResidueSequence(3,(0,0,1),[0,0,1,1,2,2,3,3]).restrict(7)
            3-residue sequence (0,0,1,1,2,2,0) with multicharge (0,0,1)
            sage: ResidueSequence(3,(0,0,1),[0,0,1,1,2,2,3,3]).restrict(6)
            3-residue sequence (0,0,1,1,2,2) with multicharge (0,0,1)
            sage: ResidueSequence(3,(0,0,1),[0,0,1,1,2,2,3,3]).restrict(4)
            3-residue sequence (0,0,1,1) with multicharge (0,0,1)
        """
    def restrict_row(self, cell, row):
        """
        Return a residue sequence for the tableau obtained by swapping the row
        in ending in `cell` with the row that is `row` rows above it and which
        has the same length.

        The residue sequence ``self`` is of the form `(r_1, \\ldots, r_n)`.
        The function returns the residue sequence `(r_1, \\ldots, r_m)`, with
        the same  :meth:`quantum_characteristic` and :meth:`multicharge`.

        EXAMPLES::

            sage: from sage.combinat.tableau_residues import ResidueSequence
            sage: ResidueSequence(3, [0,1,2,2,0,1]).restrict_row((1,2),1)
            3-residue sequence (2,0,1,0,1) with multicharge (0)
            sage: ResidueSequence(3, [1,0], [0,1,2,2,0,1]).restrict_row((1,1,2),1)
            3-residue sequence (2,0,1,0,1) with multicharge (1,0)
        """
    def swap_residues(self, i, j):
        """
        Return the *new* residue sequence obtained by swapping the residues
        for ``i`` and ``j``.

        INPUT:

        - ``i``, ``j`` -- two integers between `1` and the length of
          the residue sequence

        If residue sequence ``self`` is of the form `(r_1, \\ldots, r_n)`, and
        `i < j`, then the residue sequence
        `(r_1, \\ldots, r_j, \\ldots, r_i, \\ldots, r_m)`, with the same
        :meth:`quantum_characteristic` and :meth:`multicharge`, is returned.

        EXAMPLES::

            sage: from sage.combinat.tableau_residues import ResidueSequence
            sage: res = ResidueSequence(3,(0,0,1),[0,0,1,1,2,2,3,3]); res
            3-residue sequence (0,0,1,1,2,2,0,0) with multicharge (0,0,1)
            sage: ser = res.swap_residues(2,6); ser
            3-residue sequence (0,2,1,1,2,0,0,0) with multicharge (0,0,1)
            sage: res == ser
            False

        TESTS::

            sage: res.swap_residues(22,26)
            Traceback (most recent call last):
            ...
            IndexError: 22 and 26 must be between 1 and 8
        """
    def standard_tableaux(self, shape=None):
        """
        Return the residue-class of standard tableaux that have residue
        sequence ``self``.

        INPUT:

        - ``shape`` -- (optional) a partition or partition tuple of
          the correct level

        OUTPUT:

        An iterator for the standard tableaux with this residue sequence. If
        the ``shape`` is given then only tableaux of this shape are returned,
        otherwise all of the full residue-class of standard tableaux, or
        standard tableaux tuples, is returned. The residue sequence ``self``
        specifies the :meth:`multicharge` of the tableaux which, in turn,
        determines the :meth:`level` of the tableaux in the residue class.

        EXAMPLES::

            sage: from sage.combinat.tableau_residues import ResidueSequence
            sage: ResidueSequence(3,(0,0,0),[0,1,2,0,1,2,0,1,2]).standard_tableaux()
            Standard tableaux with 3-residue sequence (0,1,2,0,1,2,0,1,2) and multicharge (0,0,0)
            sage: ResidueSequence(3,(0,0,0),[0,1,2,0,1,2,0,1,2]).standard_tableaux([[3],[3],[3]])
            Standard (3|3|3)-tableaux with 3-residue sequence (0,1,2,0,1,2,0,1,2) and multicharge (0,0,0)
        """
    def row_standard_tableaux(self, shape=None):
        """
        Return the residue-class of row standard tableaux that have residue
        sequence ``self``.

        INPUT:

        - ``shape`` -- (optional) a partition or partition tuple of
          the correct level

        OUTPUT:

        An iterator for the row standard tableaux with this residue sequence. If
        the ``shape`` is given then only tableaux of this shape are returned,
        otherwise all of the full residue-class of row standard tableaux, or row
        standard tableaux tuples, is returned. The residue sequence ``self``
        specifies the :meth:`multicharge` of the tableaux which, in turn,
        determines the :meth:`level` of the tableaux in the residue class.

        EXAMPLES::

            sage: from sage.combinat.tableau_residues import ResidueSequence
            sage: ResidueSequence(3,(0,0,0),[0,1,2,0,1,2,0,1,2]).row_standard_tableaux()
            Row standard tableaux with 3-residue sequence (0,1,2,0,1,2,0,1,2) and multicharge (0,0,0)
            sage: ResidueSequence(3,(0,0,0),[0,1,2,0,1,2,0,1,2]).row_standard_tableaux([[3],[3],[3]])
            Row standard (3|3|3)-tableaux with 3-residue sequence (0,1,2,0,1,2,0,1,2) and multicharge (0,0,0)
        """
    def negative(self):
        """
        Return the negative of the residue sequence ``self``.

        That is, if ``self`` is the residue sequence `(i_1, \\ldots, i_n)`
        then return `(-i_1, \\ldots, -i_n)`. Taking the negative residue
        sequences is a shadow of tensoring with the sign representation
        from the cyclotomic Hecke algebras of type `A`.

        EXAMPLES::

            sage: from sage.combinat.tableau_residues import ResidueSequence
            sage: ResidueSequence(3,[0,0,1],[0,0,1,1,2,2,3,3]).negative()
            3-residue sequence (0,0,2,2,1,1,0,0) with multicharge (0,0,1)
        """
    def block(self):
        """
        Return a dictionary `\\beta` that determines the block associated to
        the residue sequence ``self``.

        Two Specht modules for a cyclotomic Hecke algebra of type `A` belong to
        the same block, in this sense, if and only if the residue sequences of
        their standard tableaux have the same block in this sense.  The blocks
        of these algebras are actually indexed by positive roots in the root
        lattice of an affine special linear group. Instead of than constructing
        the root lattice, this method simply returns a dictionary `\\beta` where
        the keys are residues `i` and where the value of the  key `i` is equal
        to the numbers of nodes in the residue sequence ``self`` that are equal
        to `i`. The dictionary `\\beta` corresponds to the positive root:

        .. MATH::

            \\sum_{i\\in I} \\beta_i \\alpha_i \\in Q^+,

        These positive roots also index the blocks of the cyclotomic KLR
        algebras of type `A`.

        We return a dictionary because when the :meth:`quantum_characteristic` is `0`,
        the Cartan type is `A_{\\infty}`, in which case the simple roots are
        indexed by the integers, which is infinite.

        EXAMPLES::

            sage: from sage.combinat.tableau_residues import ResidueSequence
            sage: ResidueSequence(3, [0,0,0], [0,1,2,0,1,2,0,1,2]).block()
            {0: 3, 1: 3, 2: 3}
        """
    def base_ring(self):
        """
        Return the base ring for the residue sequence.

        If the :meth:`quantum_characteristic` of the residue sequence ``self``
        is `e` then the base ring for the sequence is `\\ZZ / e\\ZZ`,
        or `\\ZZ` if `e=0`.

        EXAMPLES::

            sage: from sage.combinat.tableau_residues import ResidueSequence
            sage: ResidueSequence(3, (0,0,1), [0,0,1,1,2,2,3,3]).base_ring()
            Ring of integers modulo 3
        """
    def quantum_characteristic(self):
        """
        Return the quantum characteristic of the residue sequence ``self``.

        The `e`-residue sequences are associated with a cyclotomic Hecke
        algebra that has a parameter `q` of *quantum characteristic* `e`.
        This is the smallest positive integer such that
        `1 + q + \\cdots + q^{e-1} = 0`, or `e=0` if no such integer exists.

        EXAMPLES::

            sage: from sage.combinat.tableau_residues import ResidueSequence
            sage: ResidueSequence(3, (0,0,1), [0,0,1,1,2,2,3,3]).quantum_characteristic()
            3
        """
    def multicharge(self):
        """
        Return the multicharge for the residue sequence ``self``.

        The `e`-residue sequences are associated with a cyclotomic Hecke
        algebra with Hecke parameter `q` of :meth:`quantum_characteristic` `e`
        and multicharge `(\\kappa_1, \\ldots, \\kappa_l)`. This means that
        the cyclotomic parameters of the Hecke algebra are
        `q^{\\kappa_1}, \\ldots, q^{\\kappa_l}`. Equivalently, the Hecke
        algebra is determined by the dominant weight

        .. MATH::

            \\sum_{r \\in \\ZZ / e\\ZZ} \\kappa_r \\Lambda_r \\in P^+.

        EXAMPLES::

            sage: from sage.combinat.tableau_residues import ResidueSequence
            sage: ResidueSequence(3, (0,0,1), [0,0,1,1,2,2,3,3]).multicharge()
            (0, 0, 1)
        """
    def level(self):
        """
        Return the level of the residue sequence. That is, the level of the
        corresponding (tuples of) standard tableaux.

        The *level* of a residue sequence is the length of its
        :meth:`multicharge`. This is the same as the level  of the
        :meth:`standard_tableaux` that belong to the residue class of tableaux
        determined by ``self``.

        EXAMPLES::

            sage: from sage.combinat.tableau_residues import ResidueSequence
            sage: ResidueSequence(3, (0,0,1), [0,0,1,1,2,2,3,3]).level()
            3
        """
    def size(self):
        """
        Return the size of the residue sequence.

        This is the size, or length, of the residue sequence, which is the
        same as  the size of the :meth:`standard_tableaux` that belong to
        the residue class of tableaux determined by ``self``.

        EXAMPLES::

            sage: from sage.combinat.tableau_residues import ResidueSequence
            sage: ResidueSequence(3, (0,0,1), [0,0,1,1,2,2,3,3]).size()
            8
        """

class ResidueSequences(UniqueRepresentation, Parent):
    """
    A parent class for :class:`ResidueSequence`.

    This class exists because :class:`ResidueSequence` needs to have a parent.
    Apart form being a parent the only useful method that it provides is
    :meth:`cell_residue`, which is a short-hand for computing the residue
    of a cell using the :meth:`ResidueSequence.quantum_characteristic`
    and :meth:`ResidueSequence.multicharge` for the residue class.

    EXAMPLES::

        sage: from sage.combinat.tableau_residues import ResidueSequences
        sage: ResidueSequences(e=0, multicharge=(0,1,2))
        0-residue sequences with multicharge (0, 1, 2)
        sage: ResidueSequences(e=0, multicharge=(0,1,2)) == ResidueSequences(e=0, multicharge=(0,1,2))
        True
        sage: ResidueSequences(e=0, multicharge=(0,1,2)) == ResidueSequences(e=3, multicharge=(0,1,2))
        False
        sage: ResidueSequences(e=0, multicharge=(0,1,2)).element_class
        <class 'sage.combinat.tableau_residues.ResidueSequences_with_category.element_class'>
    """
    Element = ResidueSequence
    def __init__(self, e, multicharge=(0,)) -> None:
        """
        Initialise the parent class for residue sequences.

        EXAMPLES::

            sage: from sage.combinat.tableau_residues import ResidueSequences
            sage: ResidueSequences(e=0, multicharge=(0,1,2))
            0-residue sequences with multicharge (0, 1, 2)
            sage: ResidueSequences(e=0, multicharge=(0,1,2)) == ResidueSequences(e=0, multicharge=(0,1,2))
            True
            sage: ResidueSequences(e=0, multicharge=(0,1,2)) == ResidueSequences(e=3, multicharge=(0,1,2))
            False

        The TestSuite fails ``_test_pickling`` because ``__getitem__`` does
        not support slices, so we skip this::

            sage: R = ResidueSequences(e=0, multicharge=(0,1,2))
            sage: TestSuite(R).run(skip='_test_elements')
        """
    @lazy_attribute
    def cell_residue(self, *args):
        """
        Return the residue a cell with respect to the quantum characteristic
        and the multicharge of the residue sequence.

        INPUT:

        - ``r``, ``c`` -- the row and column indices in level one
        - ``k``, ``r``, ``c`` -- the component, row and column indices
          in higher levels

        EXAMPLES::

            sage: from sage.combinat.tableau_residues import ResidueSequences
            sage: ResidueSequences(3).cell_residue(1,1)
            0
            sage: ResidueSequences(3).cell_residue(2,1)
            2
            sage: ResidueSequences(3).cell_residue(3,1)
            1
            sage: ResidueSequences(3).cell_residue(3,2)
            2
            sage: ResidueSequences(3,(0,1,2)).cell_residue(0,0,0)
            0
            sage: ResidueSequences(3,(0,1,2)).cell_residue(0,1,0)
            2
            sage: ResidueSequences(3,(0,1,2)).cell_residue(0,1,2)
            1
            sage: ResidueSequences(3,(0,1,2)).cell_residue(1,0,0)
            1
            sage: ResidueSequences(3,(0,1,2)).cell_residue(1,1,0)
            0
            sage: ResidueSequences(3,(0,1,2)).cell_residue(1,0,1)
            2
            sage: ResidueSequences(3,(0,1,2)).cell_residue(2,0,0)
            2
            sage: ResidueSequences(3,(0,1,2)).cell_residue(2,1,0)
            1
            sage: ResidueSequences(3,(0,1,2)).cell_residue(2,0,1)
            0
        """
    def check_element(self, element) -> None:
        """
        Check that ``element`` is a residue sequence with
        multicharge ``self.multicharge()``.

        This is weak criteria in that we only require that ``element`` is
        a tuple of elements in the underlying base ring of ``self``. Such
        a sequence is always a valid residue sequence, although there may
        be no tableaux with this residue sequence.

        EXAMPLES::

            sage: from sage.combinat.tableau_residues import ResidueSequence
            sage: ResidueSequence(3,(0,0,1),[0,0,1,1,2,2,3,3]) # indirect doctest
            3-residue sequence (0,0,1,1,2,2,0,0) with multicharge (0,0,1)
            sage: ResidueSequence(3,(0,0,1),[2,0,1,4,2,2,5,3]) # indirect doctest
            3-residue sequence (2,0,1,1,2,2,2,0) with multicharge (0,0,1)
            sage: ResidueSequence(3,(0,0,1),[2,0,1,1,2,2,3,3]) # indirect doctest
            3-residue sequence (2,0,1,1,2,2,0,0) with multicharge (0,0,1)
        """
