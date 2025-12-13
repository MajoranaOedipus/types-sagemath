from enum import Enum
from sage.matrix.constructor import matrix as matrix
from sage.matrix.matrix_generic_dense import Matrix_generic_dense as Matrix_generic_dense
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.matrix.special import block_diagonal_matrix as block_diagonal_matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.verbose import verbose as verbose
from sage.rings.integer import Integer as Integer

class GenSign(Enum):
    """
    Enum class to select the braid generators sign.

    EXAMPLES::

        sage: import sage.algebras.hecke_algebras.cubic_hecke_matrix_rep as chmr
        sage: chmr.GenSign.pos
        <GenSign.pos: 1>
        sage: chmr.GenSign.neg
        <GenSign.neg: -1>
    """
    pos = 1
    neg = -1

class RepresentationType(Enum):
    """
    Enum class to select a representation type for the cubic Hecke algebra.

    - ``RegularLeft`` -- left regular representations
    - ``RegularRight`` -- right regular representations
    - ``SplitIrredMarin`` -- split irreducible representations obtained from
      Ivan Marin's data
    - ``SplitIrredChevie`` -- the split irreducible representations obtained
      from CHEVIE via the ``GAP3`` interface

    EXAMPLES::

        sage: import sage.algebras.hecke_algebras.cubic_hecke_matrix_rep as chmr
        sage: chmr.RepresentationType.RegularLeft.is_regular()
        True
    """
    def is_split(self):
        """
        Return ``True`` if this representation type is absolutely split,
        ``False`` else-wise.

        EXAMPLES::

            sage: import sage.algebras.hecke_algebras.cubic_hecke_matrix_rep as chmr
            sage: chevie = chmr.RepresentationType.SplitIrredChevie
            sage: chevie.is_split()
            True
        """
    def is_regular(self):
        """
        Return ``True`` if this representation type is regular, ``False``
        else-wise.

        EXAMPLES::

            sage: import sage.algebras.hecke_algebras.cubic_hecke_matrix_rep as chmr
            sage: reg_left = chmr.RepresentationType.RegularLeft
            sage: reg_left.is_regular()
            True
        """
    def data_section(self):
        """
        Return the name of the data file. For more information see
        :class:`~sage.databases.cubic_hecke_db.CubicHeckeDataBase`.

        EXAMPLES::

            sage: import sage.algebras.hecke_algebras.cubic_hecke_matrix_rep as chmr
            sage: reg_left = chmr.RepresentationType.RegularLeft
            sage: reg_left.data_section()
            <CubicHeckeDataSection.regular_left: 'regular_left'>
        """
    def number_of_representations(self, nstrands):
        """
        Return the number of representations existing to that type.

        EXAMPLES::

            sage: import sage.algebras.hecke_algebras.cubic_hecke_matrix_rep as chmr
            sage: chmr.RepresentationType.SplitIrredChevie.number_of_representations(4)
            24
            sage: chmr.RepresentationType.SplitIrredMarin.number_of_representations(4)
            24
        """
    RegularLeft = ...
    RegularRight = ...
    SplitIrredMarin = ...
    SplitIrredChevie = {'split': True, 'regular': False, 'data': None, 'num_rep': [1, 3, 7, 24, 30]}

class AbsIrreducibeRep(Enum):
    """
    Enum class to select an absolutely irreducible representation for the cubic
    Hecke algebra (``CHAn``) on `n`-strands.

    The names are build as follows: Take the determinant of one of the
    generators of the ``CHAn``. This is a monomial in the generic extension
    ring (``GER``) of ``CHA``, say ``a^ib^jc^k`` where ``a, b`` and ``c`` are
    the generators of ``GER``. This does not depend on the choice of the
    generator of ``CHA``, since these are conjugated to each other. This
    monomial might be looked as the weight of the representation. Therefore we
    use it as a name:

        ``Wn_ijk``

    The only ambiguity among the available irreducible representations occurs for the two nine-dimensional modules, which
    are conjugated to each other and distinguished by these names:

        ``W4_333`` and ``W4_333bar``

    Examples of names:

    - ``W2_100`` -- one dimensional representation of the cubic Hecke algebra on 2 strands corresponding to the first root
      of the cubic equation
    - ``W3_111`` -- three dimensional irreducible representation of the cubic Hecke algebra on 3 strands
    - ``W4_242`` -- eight dimensional irreducible representation of the cubic Hecke algebra on 4 strands having the second
      root of the cubic equation as weight of dimension 4

    Alternative names are taken from [MW2012]_ and can be shown by
    :meth:`alternative_name`.

    EXAMPLES::

        sage: import sage.algebras.hecke_algebras.cubic_hecke_matrix_rep as chmr
        sage: [irr.name for irr in chmr.AbsIrreducibeRep]
        ['W2_100', 'W2_001', 'W2_010', 'W3_100', 'W3_001', 'W3_010', 'W3_011', 'W3_110',
         'W3_101', 'W3_111', 'W4_100', 'W4_001', 'W4_010', 'W4_011', 'W4_110', 'W4_101',
         'W4_111', 'W4_120', 'W4_201', 'W4_012', 'W4_102', 'W4_210', 'W4_021', 'W4_213',
         'W4_132', 'W4_321', 'W4_231', 'W4_123', 'W4_312', 'W4_422', 'W4_224', 'W4_242',
         'W4_333', 'W4_333bar', 'W5_100', 'W5_001', 'W5_010', 'W5_013', 'W5_130', 'W5_301',
         'W5_031', 'W5_103', 'W5_310', 'W5_203', 'W5_032', 'W5_320', 'W5_230', 'W5_023',
         'W5_302', 'W5_033', 'W5_330', 'W5_303', 'W5_163', 'W5_631', 'W5_316', 'W5_136',
         'W5_613', 'W5_361', 'W5_366', 'W5_663', 'W5_636', 'W5_933', 'W5_339', 'W5_393']

    REFERENCES:

    - [MW2012]_
    """
    def alternative_name(self):
        """
        Return the name of the split irreducible representation for cubic Hecke
        algebras for up to four strands as given in [MW2012]_.

        EXAMPLES::

            sage: import sage.algebras.hecke_algebras.cubic_hecke_matrix_rep as chmr
            sage: chmr.AbsIrreducibeRep.W3_011.alternative_name()
            'Tbc'
        """
    def dimension(self):
        """
        Return the dimension of the representation.

        EXAMPLES::

            sage: import sage.algebras.hecke_algebras.cubic_hecke_matrix_rep as chmr
            sage: chmr.AbsIrreducibeRep.W3_111.dimension()
            3
        """
    def number_gens(self):
        """
        Return the number of generators of the underlying cubic Hecke algebra.

        EXAMPLES::

            sage: import sage.algebras.hecke_algebras.cubic_hecke_matrix_rep as chmr
            sage: chmr.AbsIrreducibeRep.W3_001.number_gens()
            2
            sage: chmr.AbsIrreducibeRep.W4_001.number_gens()
            3
        """
    def length_orbit(self):
        """
        Return the length of the orbit of this representation under the action
        of the Galois group of the cubic equation.

        EXAMPLES::

            sage: import sage.algebras.hecke_algebras.cubic_hecke_matrix_rep as chmr
            sage: chmr.AbsIrreducibeRep.W3_001.length_orbit()
            3
            sage: chmr.AbsIrreducibeRep.W3_111.length_orbit()
            1
        """
    def gap_index(self):
        """
        Return the array index of this representation for the access
        to the ``GAP3`` package ``CHEVIE``.

        EXAMPLES::

            sage: import sage.algebras.hecke_algebras.cubic_hecke_matrix_rep as chmr
            sage: chmr.AbsIrreducibeRep.W3_111.gap_index()
            6
        """
    def internal_index(self):
        """
        Return the array index of this representation for the internal access.

        EXAMPLES::

            sage: import sage.algebras.hecke_algebras.cubic_hecke_matrix_rep as chmr
            sage: chmr.AbsIrreducibeRep.W3_111.internal_index()
            6
        """
    W2_100 = {'alt_name': 'Sa', 'dim': 1, 'ngens': 1, 'len_orbit': 3, 'gap_ind': 0, 'intern_ind': 0}
    W2_001 = {'alt_name': 'Sc', 'dim': 1, 'ngens': 1, 'len_orbit': 3, 'gap_ind': 1, 'intern_ind': 1}
    W2_010 = {'alt_name': 'Sb', 'dim': 1, 'ngens': 1, 'len_orbit': 3, 'gap_ind': 2, 'intern_ind': 2}
    W3_100 = {'alt_name': 'Sa', 'dim': 1, 'ngens': 2, 'len_orbit': 3, 'gap_ind': 0, 'intern_ind': 0}
    W3_001 = {'alt_name': 'Sc', 'dim': 1, 'ngens': 2, 'len_orbit': 3, 'gap_ind': 1, 'intern_ind': 1}
    W3_010 = {'alt_name': 'Sb', 'dim': 1, 'ngens': 2, 'len_orbit': 3, 'gap_ind': 2, 'intern_ind': 2}
    W3_011 = {'alt_name': 'Tbc', 'dim': 2, 'ngens': 2, 'len_orbit': 3, 'gap_ind': 3, 'intern_ind': 3}
    W3_110 = {'alt_name': 'Tab', 'dim': 2, 'ngens': 2, 'len_orbit': 3, 'gap_ind': 4, 'intern_ind': 4}
    W3_101 = {'alt_name': 'Tac', 'dim': 2, 'ngens': 2, 'len_orbit': 3, 'gap_ind': 5, 'intern_ind': 5}
    W3_111 = {'alt_name': 'V', 'dim': 3, 'ngens': 2, 'len_orbit': 1, 'gap_ind': 6, 'intern_ind': 6}
    W4_100 = {'alt_name': 'Sa', 'dim': 1, 'ngens': 3, 'len_orbit': 3, 'gap_ind': 0, 'intern_ind': 0}
    W4_001 = {'alt_name': 'Sc', 'dim': 1, 'ngens': 3, 'len_orbit': 3, 'gap_ind': 1, 'intern_ind': 1}
    W4_010 = {'alt_name': 'Sb', 'dim': 1, 'ngens': 3, 'len_orbit': 3, 'gap_ind': 2, 'intern_ind': 2}
    W4_011 = {'alt_name': 'Tbc', 'dim': 2, 'ngens': 3, 'len_orbit': 3, 'gap_ind': 3, 'intern_ind': 3}
    W4_110 = {'alt_name': 'Tab', 'dim': 2, 'ngens': 3, 'len_orbit': 3, 'gap_ind': 4, 'intern_ind': 4}
    W4_101 = {'alt_name': 'Tac', 'dim': 2, 'ngens': 3, 'len_orbit': 3, 'gap_ind': 5, 'intern_ind': 5}
    W4_111 = {'alt_name': 'V', 'dim': 3, 'ngens': 3, 'len_orbit': 1, 'gap_ind': 6, 'intern_ind': 6}
    W4_120 = {'alt_name': 'Uba', 'dim': 3, 'ngens': 3, 'len_orbit': 6, 'gap_ind': 7, 'intern_ind': 7}
    W4_201 = {'alt_name': 'Uac', 'dim': 3, 'ngens': 3, 'len_orbit': 6, 'gap_ind': 8, 'intern_ind': 8}
    W4_012 = {'alt_name': 'Ucb', 'dim': 3, 'ngens': 3, 'len_orbit': 6, 'gap_ind': 9, 'intern_ind': 9}
    W4_102 = {'alt_name': 'Uca', 'dim': 3, 'ngens': 3, 'len_orbit': 6, 'gap_ind': 10, 'intern_ind': 10}
    W4_210 = {'alt_name': 'Uab', 'dim': 3, 'ngens': 3, 'len_orbit': 6, 'gap_ind': 11, 'intern_ind': 11}
    W4_021 = {'alt_name': 'Ubc', 'dim': 3, 'ngens': 3, 'len_orbit': 6, 'gap_ind': 12, 'intern_ind': 12}
    W4_213 = {'alt_name': 'Vcab', 'dim': 6, 'ngens': 3, 'len_orbit': 6, 'gap_ind': 13, 'intern_ind': 13}
    W4_132 = {'alt_name': 'Vbca', 'dim': 6, 'ngens': 3, 'len_orbit': 6, 'gap_ind': 14, 'intern_ind': 14}
    W4_321 = {'alt_name': 'Vabc', 'dim': 6, 'ngens': 3, 'len_orbit': 6, 'gap_ind': 15, 'intern_ind': 15}
    W4_231 = {'alt_name': 'Vbac', 'dim': 6, 'ngens': 3, 'len_orbit': 6, 'gap_ind': 16, 'intern_ind': 16}
    W4_123 = {'alt_name': 'Vcba', 'dim': 6, 'ngens': 3, 'len_orbit': 6, 'gap_ind': 17, 'intern_ind': 17}
    W4_312 = {'alt_name': 'Vacb', 'dim': 6, 'ngens': 3, 'len_orbit': 6, 'gap_ind': 18, 'intern_ind': 18}
    W4_422 = {'alt_name': 'Wa', 'dim': 8, 'ngens': 3, 'len_orbit': 3, 'gap_ind': 19, 'intern_ind': 19}
    W4_224 = {'alt_name': 'Wc', 'dim': 8, 'ngens': 3, 'len_orbit': 3, 'gap_ind': 20, 'intern_ind': 20}
    W4_242 = {'alt_name': 'Wb', 'dim': 8, 'ngens': 3, 'len_orbit': 3, 'gap_ind': 21, 'intern_ind': 21}
    W4_333 = {'alt_name': 'X', 'dim': 9, 'ngens': 3, 'len_orbit': 2, 'gap_ind': 22, 'intern_ind': 22}
    W4_333bar = {'alt_name': 'Xbar', 'dim': 9, 'ngens': 3, 'len_orbit': 2, 'gap_ind': 23, 'intern_ind': 23}
    W5_100 = {'alt_name': None, 'dim': 1, 'ngens': 4, 'len_orbit': 3, 'gap_ind': 0, 'intern_ind': 0}
    W5_001 = {'alt_name': None, 'dim': 1, 'ngens': 4, 'len_orbit': 3, 'gap_ind': 1, 'intern_ind': 1}
    W5_010 = {'alt_name': None, 'dim': 1, 'ngens': 4, 'len_orbit': 3, 'gap_ind': 2, 'intern_ind': 2}
    W5_013 = {'alt_name': None, 'dim': 4, 'ngens': 4, 'len_orbit': 6, 'gap_ind': 3, 'intern_ind': 3}
    W5_130 = {'alt_name': None, 'dim': 4, 'ngens': 4, 'len_orbit': 6, 'gap_ind': 4, 'intern_ind': 4}
    W5_301 = {'alt_name': None, 'dim': 4, 'ngens': 4, 'len_orbit': 6, 'gap_ind': 5, 'intern_ind': 5}
    W5_031 = {'alt_name': None, 'dim': 4, 'ngens': 4, 'len_orbit': 6, 'gap_ind': 6, 'intern_ind': 6}
    W5_103 = {'alt_name': None, 'dim': 4, 'ngens': 4, 'len_orbit': 6, 'gap_ind': 7, 'intern_ind': 7}
    W5_310 = {'alt_name': None, 'dim': 4, 'ngens': 4, 'len_orbit': 6, 'gap_ind': 8, 'intern_ind': 8}
    W5_203 = {'alt_name': None, 'dim': 5, 'ngens': 4, 'len_orbit': 6, 'gap_ind': 9, 'intern_ind': 9}
    W5_032 = {'alt_name': None, 'dim': 5, 'ngens': 4, 'len_orbit': 6, 'gap_ind': 10, 'intern_ind': 10}
    W5_320 = {'alt_name': None, 'dim': 5, 'ngens': 4, 'len_orbit': 6, 'gap_ind': 11, 'intern_ind': 11}
    W5_230 = {'alt_name': None, 'dim': 5, 'ngens': 4, 'len_orbit': 6, 'gap_ind': 12, 'intern_ind': 12}
    W5_023 = {'alt_name': None, 'dim': 5, 'ngens': 4, 'len_orbit': 6, 'gap_ind': 13, 'intern_ind': 13}
    W5_302 = {'alt_name': None, 'dim': 5, 'ngens': 4, 'len_orbit': 6, 'gap_ind': 14, 'intern_ind': 14}
    W5_033 = {'alt_name': None, 'dim': 6, 'ngens': 4, 'len_orbit': 3, 'gap_ind': 15, 'intern_ind': 15}
    W5_330 = {'alt_name': None, 'dim': 6, 'ngens': 4, 'len_orbit': 3, 'gap_ind': 16, 'intern_ind': 16}
    W5_303 = {'alt_name': None, 'dim': 6, 'ngens': 4, 'len_orbit': 3, 'gap_ind': 17, 'intern_ind': 17}
    W5_163 = {'alt_name': None, 'dim': 10, 'ngens': 4, 'len_orbit': 6, 'gap_ind': 18, 'intern_ind': 18}
    W5_631 = {'alt_name': None, 'dim': 10, 'ngens': 4, 'len_orbit': 6, 'gap_ind': 19, 'intern_ind': 19}
    W5_316 = {'alt_name': None, 'dim': 10, 'ngens': 4, 'len_orbit': 6, 'gap_ind': 20, 'intern_ind': 20}
    W5_136 = {'alt_name': None, 'dim': 10, 'ngens': 4, 'len_orbit': 6, 'gap_ind': 21, 'intern_ind': 21}
    W5_613 = {'alt_name': None, 'dim': 10, 'ngens': 4, 'len_orbit': 6, 'gap_ind': 22, 'intern_ind': 22}
    W5_361 = {'alt_name': None, 'dim': 10, 'ngens': 4, 'len_orbit': 6, 'gap_ind': 23, 'intern_ind': 23}
    W5_366 = {'alt_name': None, 'dim': 15, 'ngens': 4, 'len_orbit': 3, 'gap_ind': 24, 'intern_ind': 24}
    W5_663 = {'alt_name': None, 'dim': 15, 'ngens': 4, 'len_orbit': 3, 'gap_ind': 26, 'intern_ind': 25}
    W5_636 = {'alt_name': None, 'dim': 15, 'ngens': 4, 'len_orbit': 3, 'gap_ind': 27, 'intern_ind': 26}
    W5_933 = {'alt_name': None, 'dim': 15, 'ngens': 4, 'len_orbit': 3, 'gap_ind': 25, 'intern_ind': 27}
    W5_339 = {'alt_name': None, 'dim': 15, 'ngens': 4, 'len_orbit': 3, 'gap_ind': 28, 'intern_ind': 28}
    W5_393 = {'alt_name': None, 'dim': 15, 'ngens': 4, 'len_orbit': 3, 'gap_ind': 29, 'intern_ind': 29}

class CubicHeckeMatrixRep(Matrix_generic_dense):
    """
    Class to supervise the diagonal block matrix structure arising from
    cubic Hecke algebra-representations.

    EXAMPLES::

        sage: import sage.algebras.hecke_algebras.cubic_hecke_matrix_rep as chmr
        sage: CHA2.<c1> = algebras.CubicHecke(2)
        sage: MS = chmr.CubicHeckeMatrixSpace(CHA2)
        sage: m1 = MS(c1); m1
        [         a          0          0]
        [         0          b          0]
        [         0          0 -b - a + u]
        sage: type(m1)
        <class 'sage.algebras.hecke_algebras.cubic_hecke_matrix_rep.CubicHeckeMatrixSpace_with_category.element_class'>
        sage: m1.block_diagonal_list()
        [[a], [b], [-b - a + u]]

        sage: MSo = chmr.CubicHeckeMatrixSpace(CHA2, original=True)
        sage: MSo(c1)
        [a 0 0]
        [0 b 0]
        [0 0 c]

        sage: reg_left = chmr.RepresentationType.RegularLeft
        sage: MSreg = chmr.CubicHeckeMatrixSpace(CHA2, representation_type=reg_left)
        sage: MSreg(c1)
        [ 0 -v  1]
        [ 1  u  0]
        [ 0  w  0]
        sage: len(_.block_diagonal_list())
        1

    TESTS:

    The minpoly does not work over more generic rings::

        sage: TestSuite(m1).run(skip='_test_minpoly')
    """
    @cached_method
    def __getitem__(self, item):
        """
        Return the sub-matrix block of ``self`` considered as block diagonal
        matrix specified by `item`.

        Overloading builtin-method to select a list-item.

        INPUT:

        - ``item`` -- an :class:`AbsIrreducibeRep` specifying an
          absolute irreducible representation of the cubic Hecke algebra;
          alternatively, it can be specified by list index
          (see :meth:`internal_index` respectively :meth:`gap_index`)

        OUTPUT:

        An instance of :class:`Matrix_generic_dense` representing
        the specified block of ``self``.

        EXAMPLES::

            sage: CHA2.<c1> = algebras.CubicHecke(2)
            sage: m1 = c1.matrix()
            sage: m1[0]                       # indirect doctest
            [a]
            sage: m1[CHA2.irred_repr.W2_001]  # indirect doctest
            [b]
        """
    @cached_method
    def block_diagonal_list(self):
        """
        Return the list of sub-matrix blocks of ``self`` considered
        as block diagonal matrix.

        OUTPUT:

        A list of instances of :class:`Matrix_generic_dense` each of
        which represents a diagonal block of ``self``.

        EXAMPLES::

            sage: CHA2.<c1> = algebras.CubicHecke(2)
            sage: c1.matrix().block_diagonal_list()
            [[a], [b], [-b - a + u]]
        """
    @cached_method
    def reduce_to_irr_block(self, irr):
        """
        Return a copy of ``self`` with zeroes outside the block corresponding to
        ``irr`` but the block according to the input identical to that of ``self``.

        INPUT:

        - ``irr`` -- an :class:`AbsIrreducibeRep` specifying an
          absolute irreducible representation of the cubic Hecke algebra;
          alternatively, it can be specified by list index (see
          :meth:`internal_index` respectively :meth:`gap_index`)

        OUTPUT:

        An instance of :class:`Matrix_generic_dense` with exactly one nonzero block
        according to ``irr``.

        EXAMPLES::

            sage: CHA2.<c1> = algebras.CubicHecke(2)
            sage: m1 = c1.matrix()
            sage: m1.reduce_to_irr_block(0)
            [a 0 0]
            [0 0 0]
            [0 0 0]
            sage: m1.reduce_to_irr_block(CHA2.irred_repr.W2_001)
            [0 0 0]
            [0 b 0]
            [0 0 0]
        """

class CubicHeckeMatrixSpace(MatrixSpace):
    """
    The matrix space of cubic Hecke algebra representations.

    INPUT:

    - ``cubic_hecke_algebra`` -- (optional)
      :class:`~sage.algebras.hecke_algebras.cubic_hecke_algebra.CubicHeckeAlgebra`
      must be given if ``element`` fails to be an instance of its element class
    - ``representation_type`` -- (default: ``RepresentationType.SplitIrredChevie``)
      :class:`RepresentationType` specifying the type of the representation
    - ``subdivide`` -- boolean (default: ``False``); whether or not to subdivide
      the resulting matrices

    - ``original`` -- boolean (default: ``False``); if ``True``, the matrix
      will have coefficients in the generic base / extension ring

    EXAMPLES::

        sage: CHA2.<c1> = algebras.CubicHecke(2)
        sage: c1.matrix()      # indirect doctest
        [         a          0          0]
        [         0          b          0]
        [         0          0 -b - a + u]
        sage: c1.matrix(original=True)
        [a 0 0]
        [0 b 0]
        [0 0 c]
        sage: c1.matrix(representation_type = CHA2.repr_type.RegularLeft)   # indirect doctest
        [ 0 -v  1]
        [ 1  u  0]
        [ 0  w  0]
    """
    @staticmethod
    def __classcall_private__(cls, cubic_hecke_algebra, representation_type=None, subdivide: bool = False, original: bool = False):
        """
        Normalize the arguments to call the ``__init__`` constructor.

        See the documentation in ``__init__``.

        TESTS::

            sage: import sage.algebras.hecke_algebras.cubic_hecke_matrix_rep as chmr
            sage: CHA2.<c1> = algebras.CubicHecke(2)
            sage: MS = chmr.CubicHeckeMatrixSpace(CHA2)
            sage: MS2 = chmr.CubicHeckeMatrixSpace(CHA2, representation_type=CHA2.repr_type.SplitIrredMarin, subdivide=False)
            sage: MS is MS2
            True
        """
    def __init__(self, base_ring, dimension, cubic_hecke_algebra, representation_type, subdivide) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: import sage.algebras.hecke_algebras.cubic_hecke_matrix_rep as chmr
            sage: CHA3.<c1, c2> = algebras.CubicHecke(3)
            sage: MS = chmr.CubicHeckeMatrixSpace(CHA3, original=True)

        The minpoly does not work over more generic rings::

            sage: TestSuite(MS).run(skip='_test_elements')     # long time
        """
    def construction(self) -> None:
        """
        Return ``None`` since this construction is not functorial.

        EXAMPLES::

            sage: CHA2.<c1> = algebras.CubicHecke(2)
            sage: MS = c1.matrix().parent()
            sage: MS._test_category()   # indirect doctest
        """
    def __reduce__(self):
        """
        Used for pickling.

        EXAMPLES::

            sage: CHA2.<c1> = algebras.CubicHecke(2)
            sage: MS = c1.matrix().parent()
            sage: loads(dumps(MS)) == MS      # indirect doctest
            True
        """
    @cached_method
    def __call__(self, entries=None, coerce: bool = True, copy=None):
        """
        Construct an element of ``self``.

        This method needs to be overloaded here since
        :class:`MatrixSpace` has an own implementation of it.

        EXAMPLES::

            sage: import sage.algebras.hecke_algebras.cubic_hecke_matrix_rep as chmr
            sage: CHA2.<c1> = algebras.CubicHecke(2)
            sage: MS = chmr.CubicHeckeMatrixSpace(CHA2)
            sage: MS(c1)
            [         a          0          0]
            [         0          b          0]
            [         0          0 -b - a + u]
        """
    @cached_method
    def zero(self):
        """
        Return the zero element of ``self``.

        EXAMPLES::

            sage: CHA2.<c1> = algebras.CubicHecke(2)
            sage: m1   = c1.matrix()
            sage: m1rl = c1.matrix(representation_type = CHA2.repr_type.RegularLeft)
            sage: z   = m1.parent().zero()
            sage: zrl = m1rl.parent().zero()
            sage: matrix(z) == matrix(zrl), z.is_zero(), zrl.is_zero()
            (True, True, True)
            sage: z.block_diagonal_list()
            [[0], [0], [0]]
            sage: zrl.block_diagonal_list()
            [
            [0 0 0]
            [0 0 0]
            [0 0 0]
            ]
        """
    @cached_method
    def one(self):
        """
        Return the one element of ``self``.

        EXAMPLES::

            sage: CHA2.<c1> = algebras.CubicHecke(2)
            sage: m1   = c1.matrix()
            sage: m1rl = c1.matrix(representation_type = CHA2.repr_type.RegularLeft)
            sage: o   = m1.parent().one()
            sage: orl = m1rl.parent().one()
            sage: matrix(o) == matrix(orl), o.is_one(), orl.is_one()
            (True, True, True)
            sage: o.block_diagonal_list()
            [[1], [1], [1]]
            sage: orl.block_diagonal_list()
            [
            [1 0 0]
            [0 1 0]
            [0 0 1]
            ]
        """
    @cached_method
    def some_elements(self):
        """
        Return a generator of elements of ``self``.

        EXAMPLES::

            sage: CHA2.<c1> = algebras.CubicHecke(2, cubic_equation_roots=(2, 3, 5))
            sage: M = c1.matrix(); M
            [2 0 0]
            [0 3 0]
            [0 0 5]
            sage: MS = M.parent()
            sage: MS.some_elements()
            (
            [ 94/3     0     0]
            [    0 187/3     0]
            [    0     0 373/3]
            )
            sage: MS.some_elements() == tuple(MS(x) for x in CHA2.some_elements())
            True
        """
