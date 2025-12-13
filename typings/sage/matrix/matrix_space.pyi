from _typeshed import Incomplete
from collections.abc import Generator
from sage.categories.enumerated_sets import EnumeratedSets as EnumeratedSets
from sage.categories.fields import Fields as Fields
from sage.categories.rings import Rings as Rings
from sage.features.meataxe import Meataxe as Meataxe
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.misc.superseded import deprecated_function_alias as deprecated_function_alias
from sage.rings.finite_rings.finite_field_base import FiniteField as FiniteField
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

def is_MatrixSpace(x):
    """
    Return whether ``self`` is an instance of ``MatrixSpace``.

    EXAMPLES::

        sage: from sage.matrix.matrix_space import is_MatrixSpace
        sage: MS = MatrixSpace(QQ,2)
        sage: A = MS.random_element()
        sage: is_MatrixSpace(MS)
        doctest:warning...
        DeprecationWarning: the function is_MatrixSpace is deprecated;
        use 'isinstance(..., MatrixSpace)' instead
        See https://github.com/sagemath/sage/issues/37924 for details.
        True
        sage: is_MatrixSpace(A)
        False
        sage: is_MatrixSpace(5)
        False
    """
def get_matrix_class(R, nrows, ncols, sparse, implementation):
    """
    Return a matrix class according to the input.

    .. NOTE::

        This returns the base class without the category.

    INPUT:

    - ``R`` -- a base ring

    - ``nrows`` -- number of rows

    - ``ncols`` -- number of columns

    - ``sparse`` -- boolean; whether the matrix class should be sparse

    - ``implementation`` -- ``None`` or string or a matrix class; a possible
      implementation. See the documentation of the constructor of :class:`MatrixSpace`.

    EXAMPLES::

        sage: from sage.matrix.matrix_space import get_matrix_class

        sage: get_matrix_class(ZZ, 4, 5, False, None)                                   # needs sage.libs.linbox
        <class 'sage.matrix.matrix_integer_dense.Matrix_integer_dense'>
        sage: get_matrix_class(ZZ, 4, 5, True, None)                                    # needs sage.libs.linbox
        <class 'sage.matrix.matrix_integer_sparse.Matrix_integer_sparse'>

        sage: get_matrix_class(ZZ, 3, 3, False, 'flint')                                # needs sage.libs.linbox
        <class 'sage.matrix.matrix_integer_dense.Matrix_integer_dense'>
        sage: get_matrix_class(ZZ, 3, 3, False, 'gap')                                  # needs sage.libs.gap
        <class 'sage.matrix.matrix_gap.Matrix_gap'>
        sage: get_matrix_class(ZZ, 3, 3, False, 'generic')
        <class 'sage.matrix.matrix_generic_dense.Matrix_generic_dense'>

        sage: get_matrix_class(GF(2^15), 3, 3, False, None)                             # needs sage.rings.finite_rings
        <class 'sage.matrix.matrix_gf2e_dense.Matrix_gf2e_dense'>
        sage: get_matrix_class(GF(2^17), 3, 3, False, None)                             # needs sage.rings.finite_rings
        <class 'sage.matrix.matrix_generic_dense.Matrix_generic_dense'>

        sage: get_matrix_class(GF(2), 2, 2, False, 'm4ri')                              # needs sage.libs.m4ri
        <class 'sage.matrix.matrix_mod2_dense.Matrix_mod2_dense'>
        sage: get_matrix_class(GF(4), 2, 2, False, 'm4ri')                              # needs sage.libs.m4ri sage.rings.finite_rings
        <class 'sage.matrix.matrix_gf2e_dense.Matrix_gf2e_dense'>
        sage: get_matrix_class(GF(7), 2, 2, False, 'linbox-float')                      # needs sage.libs.linbox
        <class 'sage.matrix.matrix_modn_dense_float.Matrix_modn_dense_float'>
        sage: get_matrix_class(GF(7), 2, 2, False, 'linbox-double')                     # needs sage.libs.linbox
        <class 'sage.matrix.matrix_modn_dense_double.Matrix_modn_dense_double'>

        sage: get_matrix_class(RDF, 2, 2, False, 'numpy')                               # needs numpy
        <class 'sage.matrix.matrix_real_double_dense.Matrix_real_double_dense'>
        sage: get_matrix_class(CDF, 2, 3, False, 'numpy')                               # needs numpy sage.rings.complex_double
        <class 'sage.matrix.matrix_complex_double_dense.Matrix_complex_double_dense'>

        sage: get_matrix_class(GF(25,'x'), 4, 4, False, 'meataxe')          # optional - meataxe, needs sage.rings.finite_rings
        <class 'sage.matrix.matrix_gfpn_dense.Matrix_gfpn_dense'>
        sage: get_matrix_class(IntegerModRing(3), 4, 4, False, 'meataxe')   # optional - meataxe
        <class 'sage.matrix.matrix_gfpn_dense.Matrix_gfpn_dense'>
        sage: get_matrix_class(IntegerModRing(4), 4, 4, False, 'meataxe')
        Traceback (most recent call last):
        ...
        ValueError: 'meataxe' matrix can only deal with finite fields of order < 256
        sage: get_matrix_class(GF(next_prime(255)), 4, 4, False, 'meataxe')             # needs sage.rings.finite_rings
        Traceback (most recent call last):
        ...
        ValueError: 'meataxe' matrix can only deal with finite fields of order < 256

        sage: get_matrix_class(ZZ, 3, 5, False, 'crazy_matrix')
        Traceback (most recent call last):
        ...
        ValueError: unknown matrix implementation 'crazy_matrix' over Integer Ring
        sage: get_matrix_class(GF(3), 2, 2, False, 'm4ri')
        Traceback (most recent call last):
        ...
        ValueError: 'm4ri' matrices are only available for fields of characteristic 2
        and order <= 65536
        sage: get_matrix_class(Zmod(2**30), 2, 2, False, 'linbox-float')                # needs sage.libs.linbox
        Traceback (most recent call last):
        ...
        ValueError: 'linbox-float' matrices can only deal with order < 256
        sage: get_matrix_class(Zmod(2**30), 2, 2, False, 'linbox-double')               # needs sage.libs.linbox
        Traceback (most recent call last):
        ...
        ValueError: 'linbox-double' matrices can only deal with order < 94906266

        sage: type(matrix(SR, 2, 2, 0))                                                 # needs sage.symbolic
        <class 'sage.matrix.matrix_symbolic_dense.Matrix_symbolic_dense'>
        sage: type(matrix(SR, 2, 2, 0, sparse=True))                                    # needs sage.symbolic
        <class 'sage.matrix.matrix_symbolic_sparse.Matrix_symbolic_sparse'>
        sage: type(matrix(GF(7), 2, range(4)))                                          # needs sage.libs.linbox
        <class 'sage.matrix.matrix_modn_dense_float.Matrix_modn_dense_float'>
        sage: type(matrix(GF(16007), 2, range(4)))                                      # needs sage.libs.linbox
        <class 'sage.matrix.matrix_modn_dense_double.Matrix_modn_dense_double'>
        sage: type(matrix(CBF, 2, range(4)))                                            # needs sage.libs.flint
        <class 'sage.matrix.matrix_complex_ball_dense.Matrix_complex_ball_dense'>
        sage: type(matrix(GF(2), 2, range(4)))                                          # needs sage.libs.m4ri
        <class 'sage.matrix.matrix_mod2_dense.Matrix_mod2_dense'>
        sage: type(matrix(GF(64, 'z'), 2, range(4)))                                    # needs sage.libs.m4ri sage.rings.finite_rings
        <class 'sage.matrix.matrix_gf2e_dense.Matrix_gf2e_dense'>
        sage: type(matrix(GF(125, 'z'), 2, range(4)))                       # optional - meataxe, needs sage.rings.finite_rings
        <class 'sage.matrix.matrix_gfpn_dense.Matrix_gfpn_dense'>
    """

class MatrixSpace(UniqueRepresentation, Parent):
    """
    The space of matrices of given size and base ring.

    INPUT:

    - ``base_ring`` -- a ring

    - ``nrows`` or ``row_keys`` -- nonnegative integer; the number of rows, or
      a finite family of arbitrary objects that index the rows of the matrix

    - ``ncols`` or ``column_keys`` -- nonnegative integer (default: ``nrows``);
      the number of columns, or a finite family of arbitrary objects that index
      the columns of the matrix

    - ``sparse`` -- boolean (default: ``False``); whether or not matrices
      are given a sparse representation

    - ``implementation`` -- (optional)  string or matrix class; a possible
      implementation. Depending on the base ring, the string can be

      - ``'generic'`` -- on any base rings

      - ``'flint'`` -- for integers and rationals

      - ``'meataxe'`` -- finite fields using the optional package :ref:`spkg_meataxe`

      - ``'m4ri'`` -- for characteristic 2 using the :ref:`spkg_m4ri` library

      - ``'linbox-float'`` -- for integer mod rings up to `2^8 = 256`

      - ``'linbox-double'`` -- for integer mod rings up to
        `floor(2^26*sqrt(2) + 1/2) = 94906266`

      - ``'numpy'`` -- for real and complex floating point numbers

    OUTPUT: a matrix space or, more generally, a homspace between free modules

    This factory function creates instances of various specialized classes
    depending on the input.  Not all combinations of options are
    implemented.

    - If the parameters ``row_keys`` or ``column_keys`` are provided, they
      must be finite families of objects. In this case, instances of
      :class:`CombinatorialFreeModule` are created via the factory function
      :func:`FreeModule`. Then the homspace between these modules is returned.

    EXAMPLES::

        sage: MatrixSpace(QQ, 2)
        Full MatrixSpace of 2 by 2 dense matrices over Rational Field
        sage: MatrixSpace(ZZ, 3, 2)
        Full MatrixSpace of 3 by 2 dense matrices over Integer Ring
        sage: MatrixSpace(ZZ, 3, sparse=False)
        Full MatrixSpace of 3 by 3 dense matrices over Integer Ring

        sage: MatrixSpace(ZZ, 10, 5)
        Full MatrixSpace of 10 by 5 dense matrices over Integer Ring
        sage: MatrixSpace(ZZ, 10, 5).category()
        Category of infinite enumerated finite dimensional modules with basis over
         (Dedekind domains and euclidean domains
          and noetherian rings
          and infinite enumerated sets and metric spaces)
        sage: MatrixSpace(ZZ, 10, 10).category()
        Category of infinite enumerated finite dimensional algebras with basis over
         (Dedekind domains and euclidean domains
          and noetherian rings
          and infinite enumerated sets and metric spaces)
        sage: MatrixSpace(QQ, 10).category()
        Category of infinite finite dimensional algebras with basis over
         (number fields and quotient fields and metric spaces)

    Some examples of square 2 by 2 rational matrices::

        sage: MS = MatrixSpace(QQ, 2)
        sage: MS.dimension()
        4
        sage: MS.dims()
        (2, 2)
        sage: B = MS.basis()
        sage: list(B)
        [
        [1 0]  [0 1]  [0 0]  [0 0]
        [0 0], [0 0], [1 0], [0 1]
        ]
        sage: B[0,0]
        [1 0]
        [0 0]
        sage: B[0,1]
        [0 1]
        [0 0]
        sage: B[1,0]
        [0 0]
        [1 0]
        sage: B[1,1]
        [0 0]
        [0 1]
        sage: A = MS.matrix([1,2,3,4]); A
        [1 2]
        [3 4]

    The above matrix ``A`` can be multiplied by a 2 by 3 integer matrix::

        sage: MS2 = MatrixSpace(ZZ, 2, 3)
        sage: B = MS2.matrix([1,2,3,4,5,6])
        sage: A * B
        [ 9 12 15]
        [19 26 33]

    Using ``row_keys`` and ``column_keys``::

        sage: MS = MatrixSpace(ZZ, ['u', 'v'], ['a', 'b', 'c']); MS
        Set of Morphisms
         from Free module generated by {'a', 'b', 'c'} over Integer Ring
           to Free module generated by {'u', 'v'} over Integer Ring
           in Category of finite dimensional modules with basis over Integer Ring

    Check categories::

        sage: MatrixSpace(ZZ, 10, 5)
        Full MatrixSpace of 10 by 5 dense matrices over Integer Ring
        sage: MatrixSpace(ZZ, 10, 5).category()
        Category of infinite enumerated finite dimensional modules with basis over
         (Dedekind domains and euclidean domains
          and noetherian rings
          and infinite enumerated sets and metric spaces)
        sage: MatrixSpace(ZZ, 10, 10).category()
        Category of infinite enumerated finite dimensional algebras with basis over
         (Dedekind domains and euclidean domains
          and noetherian rings
          and infinite enumerated sets and metric spaces)
        sage: MatrixSpace(QQ, 10).category()
        Category of infinite finite dimensional algebras with basis over
         (number fields and quotient fields and metric spaces)

    TESTS::

        sage: MatrixSpace(ZZ, 1, 2^63)
        Traceback (most recent call last):
        ...
        OverflowError: number of rows and columns may be at most...
        sage: MatrixSpace(ZZ, 2^100, 10)
        Traceback (most recent call last):
        ...
        OverflowError: number of rows and columns may be at most...

    Check that different implementations play together as expected::

        sage: # needs sage.libs.linbox
        sage: M1 = MatrixSpace(ZZ, 2, implementation='flint')
        sage: M2 = MatrixSpace(ZZ, 2, implementation='generic')
        sage: type(M1(range(4)))
        <class 'sage.matrix.matrix_integer_dense.Matrix_integer_dense'>
        sage: type(M2(range(4)))
        <class 'sage.matrix.matrix_generic_dense.Matrix_generic_dense'>
        sage: M1(M2.an_element())
        [ 0  1]
        [-1  2]
        sage: M2(M1.an_element())
        [ 0  1]
        [-1  2]
        sage: all((A.get_action(B) is not None) == (A is B)
        ....:     for A in [M1, M2] for B in [M1, M2])
        True

    Check that libgap matrices over finite fields are working properly::

        sage: # needs sage.libs.gap
        sage: M2 = MatrixSpace(GF(2), 5, implementation='gap')
        sage: M2.one()
        [1 0 0 0 0]
        [0 1 0 0 0]
        [0 0 1 0 0]
        [0 0 0 1 0]
        [0 0 0 0 1]
        sage: m = M2.random_element()
        sage: M1 = MatrixSpace(GF(2), 5)
        sage: M1(m * m) == M1(m) * M1(m)
        True

    Check various combinations of dimensions and row/column keys::

        sage: M_ab_4 = MatrixSpace(QQ, ['a','b'], 4); M_ab_4
        Set of Morphisms (Linear Transformations)
         from Vector space of dimension 4 over Rational Field
           to Free module generated by {'a', 'b'} over Rational Field
        sage: TestSuite(M_ab_4).run()  # known bug
        sage: M_4_ab = MatrixSpace(QQ, 4, ['a','b']); M_4_ab
        Set of Morphisms
         from Free module generated by {'a', 'b'} over Rational Field
           to Vector space of dimension 4 over Rational Field
           in Category of finite dimensional vector spaces with basis
              over (number fields and quotient fields and metric spaces)
        sage: TestSuite(M_4_ab).run()  # known bug
        sage: M_ab_xy = MatrixSpace(QQ, ['a','b'], ['x','y'], nrows=2); M_ab_xy
        Set of Morphisms
         from Free module generated by {'x', 'y'} over Rational Field
           to Free module generated by {'a', 'b'} over Rational Field
           in Category of finite dimensional vector spaces with basis over Rational Field
        sage: TestSuite(M_ab_xy).run()  # known bug
        sage: MatrixSpace(QQ, ['a','b'], ['x','y'], nrows=4)
        Traceback (most recent call last):
        ...
        ValueError: inconsistent number of rows:
        should be cardinality of ['a', 'b'] but got 4
        sage: MatrixSpace(QQ, ['a','b'], ['x','y'], ncols=2)
        Set of Morphisms
         from Free module generated by {'x', 'y'} over Rational Field
           to Free module generated by {'a', 'b'} over Rational Field
           in Category of finite dimensional vector spaces with basis over Rational Field
        sage: MatrixSpace(QQ, ['a','b'], ['x','y'], ncols=4)
        Traceback (most recent call last):
        ...
        ValueError: inconsistent number of columns:
        should be cardinality of ['x', 'y'] but got 4
        sage: MatrixSpace(QQ, ['a','b'], ['x','y'], nrows=2, ncols=2)
        Set of Morphisms
         from Free module generated by {'x', 'y'} over Rational Field
           to Free module generated by {'a', 'b'} over Rational Field
           in Category of finite dimensional vector spaces with basis over Rational Field
        sage: MatrixSpace(QQ, ['a','b'], ['x','y'], nrows=2, ncols=4)
        Traceback (most recent call last):
        ...
        ValueError: inconsistent number of columns:
        should be cardinality of ['x', 'y'] but got 4
        sage: MatrixSpace(QQ, ['a','b'], ['x','y'], nrows=4, ncols=4)
        Traceback (most recent call last):
        ...
        ValueError: inconsistent number of columns:
        should be cardinality of ['x', 'y'] but got 4
        sage: MatrixSpace(QQ, 4, ['a','b'], nrows=4, ncols=2)
        Traceback (most recent call last):
        ...
        ValueError: duplicate values for nrows
    """
    @staticmethod
    def __classcall__(cls, base_ring, nrows_or_row_keys=None, ncols_or_column_keys=None, sparse: bool = False, implementation=None, *, nrows=None, ncols=None, row_keys=None, column_keys=None, **kwds):
        """
        Normalize the arguments to call the ``__init__`` constructor or delegate to another class.

        TESTS::

            sage: M1 = MatrixSpace(QQ, 2)
            sage: M2 = MatrixSpace(QQ, 2)
            sage: M1 is M2
            True
            sage: M3 = MatrixSpace(QQ, 2, implementation='flint')                       # needs sage.libs.flint
            sage: M1 is M3                                                              # needs sage.libs.flint
            True

        ::

            sage: M = MatrixSpace(ZZ, 10, implementation='flint')                       # needs sage.libs.flint
            sage: M                                                                     # needs sage.libs.flint
            Full MatrixSpace of 10 by 10 dense matrices over Integer Ring
            sage: loads(M.dumps()) is M                                                 # needs sage.libs.flint
            True

            sage: MatrixSpace(ZZ, 10, implementation='foobar')
            Traceback (most recent call last):
            ...
            ValueError: unknown matrix implementation 'foobar' over Integer Ring

        Check that :issue:`29466` is fixed::

            sage: class MyMatrixSpace(MatrixSpace):
            ....:     @staticmethod
            ....:     def __classcall__(cls, base_ring, nrows, ncols=None, my_option=True, sparse=False, implementation=None):
            ....:         return super().__classcall__(cls, base_ring, nrows, ncols=ncols, my_option=my_option, sparse=sparse, implementation=implementation)
            ....:
            ....:     def __init__(self, base_ring, nrows, ncols, sparse,  implementation, my_option=True):
            ....:         super().__init__(base_ring, nrows, ncols, sparse, implementation)
            ....:         self._my_option = my_option

            sage: MS1 = MyMatrixSpace(ZZ, 2)
            sage: MS1._my_option
            True
            sage: MS2 = MyMatrixSpace(ZZ, 2, my_option=False)
            sage: MS2._my_option
            False
        """
    Element: Incomplete
    def __init__(self, base_ring, nrows, ncols, sparse, implementation) -> None:
        """
        INPUT:

        - ``base_ring``

        - ``nrows`` -- positive integer; the number of rows

        - ``ncols`` -- positive integer (default: ``nrows``); the number of
          columns

        - ``sparse`` -- boolean (default: ``False``); whether or not matrices
          are given a sparse representation

        - ``implementation`` -- (optional) string or matrix class; a possible
          implementation. Depending on the base ring the string can be

           - ``'generic'`` -- on any base rings

           - ``'flint'`` -- for integers and rationals

           - ``'meataxe'`` -- finite fields, needs to install the optional package meataxe

           - ``m4ri`` -- for characteristic 2 using M4RI library

           - ``linbox-float`` -- for integer mod rings up to `2^8 = 256`

           - ``linbox-double`` -- for integer mod rings up to
             `floor(2^26*sqrt(2) + 1/2) = 94906266`

           - ``numpy`` -- for real and complex floating point numbers

        EXAMPLES::

            sage: MatrixSpace(QQ, 2)
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field
            sage: MatrixSpace(ZZ, 3, 2)
            Full MatrixSpace of 3 by 2 dense matrices over Integer Ring
            sage: MatrixSpace(ZZ, 3, sparse=False)
            Full MatrixSpace of 3 by 3 dense matrices over Integer Ring

            sage: MatrixSpace(ZZ,10,5)
            Full MatrixSpace of 10 by 5 dense matrices over Integer Ring
            sage: MatrixSpace(ZZ,10,5).category()
            Category of infinite enumerated finite dimensional modules with basis over
             (Dedekind domains and euclidean domains
              and noetherian rings
              and infinite enumerated sets and metric spaces)
            sage: MatrixSpace(ZZ,10,10).category()
            Category of infinite enumerated finite dimensional algebras with basis over
             (Dedekind domains and euclidean domains
              and noetherian rings
              and infinite enumerated sets and metric spaces)
            sage: MatrixSpace(QQ,10).category()
            Category of infinite finite dimensional algebras with basis over
             (number fields and quotient fields and metric spaces)

        TESTS:

        We test that in the real or complex double dense case,
        conversion from the base ring is done by a call morphism.
        Note that by :issue:`9138`, other algebras usually
        get a conversion map by multiplication with the one element.
        ::

            sage: MS = MatrixSpace(RDF, 2, 2)
            sage: MS.convert_map_from(RDF)
            Coercion map:
              From: Real Double Field
              To:   Full MatrixSpace of 2 by 2 dense matrices over Real Double Field
            sage: MS = MatrixSpace(CDF, 2, 2)
            sage: MS.convert_map_from(CDF)
            Coercion map:
              From: Complex Double Field
              To:   Full MatrixSpace of 2 by 2 dense matrices over Complex Double Field

        We check that :issue:`10095` is fixed::

            sage: M = Matrix(QQ, [[1 for dummy in range(125)]])
            sage: V = M.right_kernel()
            sage: V
            Vector space of degree 125 and dimension 124 over Rational Field
            Basis matrix:
            124 x 125 dense matrix over Rational Field
            sage: MatrixSpace(ZZ,20,20)(1).solve_right(MatrixSpace(ZZ,20,1).random_element())
            20 x 1 dense matrix over Rational Field (use the '.str()' method to see the entries)
            sage: MatrixSpace(ZZ,200,200)(1).solve_right(MatrixSpace(ZZ,200,1).random_element())
            200 x 1 dense matrix over Rational Field (use the '.str()' method to see the entries)
            sage: A = MatrixSpace(RDF,1000,1000).random_element()
            sage: B = MatrixSpace(RDF,1000,1000).random_element()

            sage: # needs numpy (otherwise timeout)
            sage: C = A * B

        We check that :issue:`18186` is fixed::

            sage: MatrixSpace(ZZ,0,3) in FiniteSets()
            True
            sage: MatrixSpace(Zmod(4),2) in FiniteSets()
            True
            sage: MatrixSpace(ZZ,2) in Sets().Infinite()
            True
        """
    def cardinality(self):
        """
        Return the number of elements in ``self``.

        EXAMPLES::

            sage: MatrixSpace(GF(3), 2, 3).cardinality()
            729
            sage: MatrixSpace(ZZ, 2).cardinality()
            +Infinity
            sage: MatrixSpace(ZZ, 0, 3).cardinality()
            1
        """
    def characteristic(self):
        """
        Return the characteristic.

        EXAMPLES::

            sage: MatrixSpace(ZZ, 2).characteristic()
            0
            sage: MatrixSpace(GF(9), 0).characteristic()                                # needs sage.rings.finite_rings
            3
        """
    def is_exact(self):
        """
        Test whether elements of this matrix space are represented exactly.

        OUTPUT:

        Return ``True`` if elements of this matrix space are represented exactly, i.e.,
        there is no precision loss when doing arithmetic.

        EXAMPLES::

            sage: MatrixSpace(ZZ, 3).is_exact()
            True
            sage: MatrixSpace(RR, 3).is_exact()
            False
        """
    @lazy_attribute
    def transposed(self):
        """
        The transposed matrix space, having the same base ring and sparseness,
        but number of columns and rows is swapped.

        EXAMPLES::

            sage: MS = MatrixSpace(GF(3), 7, 10)
            sage: MS.transposed
            Full MatrixSpace of 10 by 7 dense matrices over Finite Field of size 3
            sage: MS = MatrixSpace(GF(3), 7, 7)
            sage: MS.transposed is MS
            True

            sage: M = MatrixSpace(ZZ, 2, 3)
            sage: M.transposed
            Full MatrixSpace of 3 by 2 dense matrices over Integer Ring
        """
    def change_ring(self, R):
        """
        Return matrix space over R with otherwise same parameters as ``self``.

        INPUT:

        - ``R`` -- ring

        OUTPUT: a matrix space

        EXAMPLES::

            sage: Mat(QQ, 3, 5).change_ring(GF(7))
            Full MatrixSpace of 3 by 5 dense matrices
             over Finite Field of size 7
        """
    def base_extend(self, R):
        """
        Return base extension of this matrix space to R.

        INPUT:

        - ``R`` -- ring

        OUTPUT: a matrix space

        EXAMPLES::

            sage: Mat(ZZ, 3, 5).base_extend(QQ)
            Full MatrixSpace of 3 by 5 dense matrices over Rational Field
            sage: Mat(QQ, 3, 5).base_extend(GF(7))
            Traceback (most recent call last):
            ...
            TypeError: no base extension defined
        """
    def construction(self):
        """
        EXAMPLES::

            sage: A = matrix(ZZ, 2, [1..4], sparse=True)
            sage: A.parent().construction()
            (MatrixFunctor, Integer Ring)
            sage: A.parent().construction()[0](QQ['x'])
            Full MatrixSpace of 2 by 2 sparse matrices over
             Univariate Polynomial Ring in x over Rational Field
            sage: parent(A/2)
            Full MatrixSpace of 2 by 2 sparse matrices over Rational Field
        """
    def __len__(self) -> int:
        """
        Return number of elements of this matrix space if it fits in
        an int; raise a :exc:`TypeError` if there are infinitely many
        elements, and raise an :exc:`OverflowError` if there are finitely
        many but more than the size of an int.

        EXAMPLES::

            sage: len(MatrixSpace(GF(3), 3, 2))
            729
            sage: len(MatrixSpace(GF(3), 2, 3))
            729
            sage: 3^(2*3)
            729

            sage: len(MatrixSpace(GF(2003), 3, 2))                                      # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            OverflowError: cannot fit 'int' into an index-sized integer

            sage: len(MatrixSpace(QQ,3,2))
            Traceback (most recent call last):
            ...
            TypeError: len() of unsized object
        """
    def __iter__(self):
        """
        Return a generator object which iterates through the elements of
        ``self``. The order in which the elements are generated is based on a
        'weight' of a matrix which is the number of iterations on the base
        ring that are required to reach that matrix.

        The ordering is similar to a degree negative lexicographic order in
        monomials in a multivariate polynomial ring.

        EXAMPLES: Consider the case of 2 x 2 matrices over GF(5).

        ::

            sage: list(GF(5))
            [0, 1, 2, 3, 4]
            sage: MS = MatrixSpace(GF(5), 2, 2)
            sage: l = list(MS)

        Then, consider the following matrices::

            sage: A = MS([2,1,0,1]); A
            [2 1]
            [0 1]
            sage: B = MS([1,2,1,0]); B
            [1 2]
            [1 0]
            sage: C = MS([1,2,0,0]); C
            [1 2]
            [0 0]

        A appears before B since the weight of one of A's entries exceeds
        the weight of the corresponding entry in B earliest in the list.

        ::

            sage: l.index(A)
            41
            sage: l.index(B)
            46

        However, A would come after the matrix C since C has a lower weight
        than A.

        ::

            sage: l.index(A)
            41
            sage: l.index(C)
            19

        The weights of matrices over other base rings are not as obvious.
        For example, the weight of

        ::

            sage: MS = MatrixSpace(ZZ, 2, 2)
            sage: MS([-1,0,0,0])
            [-1  0]
            [ 0  0]

        is 2 since

        ::

            sage: i = iter(ZZ)
            sage: next(i)
            0
            sage: next(i)
            1
            sage: next(i)
            -1

        Some more examples::

            sage: MS = MatrixSpace(GF(2), 2)
            sage: a = list(MS)
            sage: len(a)
            16
            sage: for m in a:
            ....:     print(m)
            ....:     print('-')
            [0 0]
            [0 0]
            -
            [1 0]
            [0 0]
            -
            [0 1]
            [0 0]
            -
            [0 0]
            [1 0]
            -
            [0 0]
            [0 1]
            -
            [1 1]
            [0 0]
            -
            [1 0]
            [1 0]
            -
            [1 0]
            [0 1]
            -
            [0 1]
            [1 0]
            -
            [0 1]
            [0 1]
            -
            [0 0]
            [1 1]
            -
            [1 1]
            [1 0]
            -
            [1 1]
            [0 1]
            -
            [1 0]
            [1 1]
            -
            [0 1]
            [1 1]
            -
            [1 1]
            [1 1]
            -

        ::

            sage: MS = MatrixSpace(GF(2), 2, 3)
            sage: a = list(MS)
            sage: len(a)
            64
            sage: a[0]
            [0 0 0]
            [0 0 0]

        ::

            sage: MS = MatrixSpace(ZZ, 2, 3)
            sage: i = iter(MS)
            sage: a = [ next(i) for _ in range(6) ]
            sage: a[0]
            [0 0 0]
            [0 0 0]
            sage: a[4]
            [0 0 0]
            [1 0 0]

        For degenerate cases, where either the number of rows or columns
        (or both) are zero, then the single element of the space is
        returned.

        ::

            sage: list(MatrixSpace(GF(2), 2, 0))
            [[]]
            sage: list(MatrixSpace(GF(2), 0, 2))
            [[]]
            sage: list(MatrixSpace(GF(2), 0, 0))
            [[]]

        If the base ring does not support iteration (for example, with the
        reals), then the matrix space over that ring does not support
        iteration either.

        ::

            sage: MS = MatrixSpace(RR, 2)
            sage: a = list(MS)
            Traceback (most recent call last):
            ...
            NotImplementedError: len() of an infinite set
        """
    def __getitem__(self, x):
        """
        Return a polynomial ring over this ring or the `n`-th element of this ring.

        This method implements the syntax ``R['x']`` to define polynomial rings
        over matrix rings, while still allowing to get the `n`-th element of a
        finite matrix ring with ``R[n]`` for backward compatibility.

        (If this behaviour proves desirable for all finite enumerated rings, it
        should eventually be implemented in the corresponding category rather
        than here.)

        .. SEEALSO::

            :meth:`sage.categories.rings.Rings.ParentMethod.__getitem__`,
            :meth:`sage.structure.parent.Parent.__getitem__`

        EXAMPLES::

            sage: MS = MatrixSpace(GF(3), 2, 2)
            sage: MS['x']
            Univariate Polynomial Ring in x
             over Full MatrixSpace of 2 by 2 dense matrices
              over Finite Field of size 3
            sage: MS[0]
            [0 0]
            [0 0]
            sage: MS[9]
            [0 2]
            [0 0]

            sage: MS = MatrixSpace(QQ, 7)
            sage: MS['x']
            Univariate Polynomial Ring in x over Full MatrixSpace of 7 by 7 dense matrices over Rational Field
            sage: MS[2]
            Traceback (most recent call last):
            ...
            AttributeError: 'MatrixSpace_with_category' object has no attribute 'list'...
        """
    def basis(self):
        """
        Return a basis for this matrix space.

        .. WARNING::

            This will of course compute every generator of this matrix
            space. So for large dimensions, this could take a long time,
            waste a massive amount of memory (for dense matrices), and
            is likely not very useful. Don't use this on large matrix
            spaces.

        EXAMPLES::

            sage: list(Mat(ZZ,2,2).basis())
            [
            [1 0]  [0 1]  [0 0]  [0 0]
            [0 0], [0 0], [1 0], [0 1]
            ]
        """
    def dimension(self):
        """
        Return (m rows) \\* (n cols) of ``self`` as ``Integer``.

        EXAMPLES::

            sage: MS = MatrixSpace(ZZ,4,6)
            sage: u = MS.dimension()
            sage: u - 24 == 0
            True
        """
    def dims(self):
        """
        Return (m row, n col) representation of ``self`` dimension.

        EXAMPLES::

            sage: MS = MatrixSpace(ZZ,4,6)
            sage: MS.dims()
            (4, 6)
        """
    def submodule(self, gens, check: bool = True, already_echelonized: bool = False, unitriangular: bool = False, support_order=None, category=None, *args, **opts):
        """
        The submodule spanned by a finite set of matrices.

        INPUT:

        - ``gens`` -- list or family of elements of ``self``

        - ``check`` -- boolean (default: ``True``); whether to verify that the
          elements of ``gens`` are in ``self``

        - ``already_echelonized`` -- boolean (default: ``False``); whether
          the elements of ``gens`` are already in (not necessarily
          reduced) echelon form

        - ``unitriangular`` -- boolean (default: ``False``); whether
          the lift morphism is unitriangular

        - ``support_order`` -- (optional) either something that can
          be converted into a tuple or a key function

        If ``already_echelonized`` is ``False``, then the
        generators are put in reduced echelon form using
        :meth:`echelonize`, and reindexed by `0, 1, \\ldots`.

        .. WARNING::

            At this point, this method only works for finite
            dimensional submodules and if matrices can be
            echelonized over the base ring.

        If in addition ``unitriangular`` is ``True``, then
        the generators are made such that the coefficients of
        the pivots are 1, so that lifting map is unitriangular.

        The basis of the submodule uses the same index set as the
        generators, and the lifting map sends `y_i` to `gens[i]`.

        .. SEEALSO::

             :meth:`ModulesWithBasis.ParentMethods.submodule`

        EXAMPLES::

            sage: M = MatrixSpace(QQ, 2)
            sage: mat = M.matrix([[1, 2], [3, 4]])
            sage: X = M.submodule([mat], already_echelonized=True); X
            Free module generated by {0} over Rational Field

            sage: mat2 = M.matrix([[1, 0], [-3, 2]])
            sage: X = M.submodule([mat, mat2])
            sage: [X.lift(b) for b in X.basis()]
            [
            [ 1  0]  [0 1]
            [-3  2], [3 1]
            ]

            sage: A = matrix([[1, 1], [0, -1]])
            sage: B = matrix([[0, 1], [0, 2]])
            sage: X = M.submodule([A, B])
            sage: Xp = M.submodule([A, B], support_order=[(0,1), (1,1), (0,0)])
            sage: [X.lift(b) for b in X.basis()]
            [
            [ 1  0]  [0 1]
            [ 0 -3], [0 2]
            ]
            sage: [Xp.lift(b) for b in Xp.basis()]
            [
            [2/3   1]  [-1/3    0]
            [  0   0], [   0    1]
            ]
        """
    @cached_method
    def identity_matrix(self):
        """
        Return the identity matrix in ``self``.

        ``self`` must be a space of square
        matrices. The returned matrix is immutable. Please use ``copy`` if
        you want a modified copy.

        EXAMPLES::

            sage: MS1 = MatrixSpace(ZZ,4)
            sage: MS2 = MatrixSpace(QQ,3,4)
            sage: I = MS1.identity_matrix()
            sage: I
            [1 0 0 0]
            [0 1 0 0]
            [0 0 1 0]
            [0 0 0 1]
            sage: Er = MS2.identity_matrix()
            Traceback (most recent call last):
            ...
            TypeError: identity matrix must be square

        TESTS::

            sage: MS1.one()[1,2] = 3
            Traceback (most recent call last):
            ...
            ValueError: matrix is immutable; please change a copy instead (i.e., use copy(M) to change a copy of M).

        Check different implementations::

            sage: M1 = MatrixSpace(ZZ, 2, implementation='flint')                       # needs sage.libs.linbox
            sage: M2 = MatrixSpace(ZZ, 2, implementation='generic')

            sage: type(M1.identity_matrix())                                            # needs sage.libs.linbox
            <class 'sage.matrix.matrix_integer_dense.Matrix_integer_dense'>
            sage: type(M2.identity_matrix())
            <class 'sage.matrix.matrix_generic_dense.Matrix_generic_dense'>
        """
    one = identity_matrix
    def diagonal_matrix(self, entries):
        """
        Create a diagonal matrix in ``self`` using the specified elements.

        INPUT:

        - ``entries`` -- the elements to use as the diagonal entries

        ``self`` must be a space of square matrices. The length of
        ``entries`` must be less than or equal to the matrix
        dimensions. If the length of ``entries`` is less than the
        matrix dimensions, ``entries`` is padded with zeroes at the
        end.

        EXAMPLES::

            sage: MS1 = MatrixSpace(ZZ,4)
            sage: MS2 = MatrixSpace(QQ,3,4)
            sage: I = MS1.diagonal_matrix([1, 2, 3, 4])
            sage: I
            [1 0 0 0]
            [0 2 0 0]
            [0 0 3 0]
            [0 0 0 4]
            sage: MS2.diagonal_matrix([1, 2])
            Traceback (most recent call last):
            ...
            TypeError: diagonal matrix must be square
            sage: MS1.diagonal_matrix([1, 2, 3, 4, 5])
            Traceback (most recent call last):
            ...
            ValueError: number of diagonal matrix entries (5) exceeds the matrix size (4)
            sage: MS1.diagonal_matrix([1/2, 2, 3, 4])
            Traceback (most recent call last):
            ...
            TypeError: no conversion of this rational to integer

        Check different implementations::

            sage: M1 = MatrixSpace(ZZ, 2, implementation='flint')                       # needs sage.libs.linbox
            sage: M2 = MatrixSpace(ZZ, 2, implementation='generic')

            sage: type(M1.diagonal_matrix([1, 2]))                                      # needs sage.libs.linbox
            <class 'sage.matrix.matrix_integer_dense.Matrix_integer_dense'>
            sage: type(M2.diagonal_matrix([1, 2]))
            <class 'sage.matrix.matrix_generic_dense.Matrix_generic_dense'>
        """
    def is_dense(self):
        """
        Return whether matrices in ``self`` are dense.

        EXAMPLES::

            sage: Mat(RDF,2,3).is_sparse()
            False
            sage: Mat(RR,123456,22,sparse=True).is_sparse()
            True
        """
    def is_sparse(self):
        """
        Return whether matrices in ``self`` are sparse.

        EXAMPLES::

            sage: Mat(GF(2011), 10000).is_sparse()                                      # needs sage.rings.finite_rings
            False
            sage: Mat(GF(2011), 10000, sparse=True).is_sparse()                         # needs sage.rings.finite_rings
            True
        """
    def is_finite(self):
        """
        Return whether this matrix space is finite.

        EXAMPLES::

            sage: MatrixSpace(GF(101), 10000).is_finite()
            True
            sage: MatrixSpace(QQ, 2).is_finite()
            False
        """
    def gen(self, n):
        """
        Return the `n`-th generator of this matrix space.

        This does not compute all basis matrices, so it is reasonably
        intelligent.

        EXAMPLES::

            sage: M = Mat(GF(7), 10000, 5); M.ngens()
            50000
            sage: a = M.10
            sage: a[:4]
            [0 0 0 0 0]
            [0 0 0 0 0]
            [1 0 0 0 0]
            [0 0 0 0 0]
        """
    @cached_method
    def zero_matrix(self):
        """
        Return the zero matrix in ``self``.

        ``self`` must be a space of square matrices. The returned matrix is
        immutable. Please use ``copy`` if you want a modified copy.

        EXAMPLES::

            sage: z = MatrixSpace(GF(7), 2, 4).zero_matrix(); z
            [0 0 0 0]
            [0 0 0 0]
            sage: z.is_mutable()
            False

        TESTS::

            sage: MM = MatrixSpace(RDF,1,1,sparse=False); mat = MM.zero_matrix()
            sage: copy(mat)
            [0.0]
            sage: MM = MatrixSpace(RDF,0,0,sparse=False); mat = MM.zero_matrix()
            sage: copy(mat)
            []
            sage: mat.is_mutable()
            False
            sage: MM.zero().is_mutable()
            False

        Check that :issue:`38221` is fixed::

            sage: # needs sage.groups
            sage: G = CyclicPermutationGroup(7)
            sage: R = GF(2)
            sage: A = G.algebra(R)
            sage: S = MatrixSpace(A, 3, 3)
            sage: S.zero_matrix()
            [0 0 0]
            [0 0 0]
            [0 0 0]
        """
    zero = zero_matrix
    def ngens(self):
        """
        Return the number of generators of this matrix space.

        This is the number of entries in the matrices in this space.

        EXAMPLES::

            sage: M = Mat(GF(7), 100, 200); M.ngens()
            20000
        """
    def matrix(self, x=None, **kwds):
        '''
        Create a matrix in ``self``.

        INPUT:

        - ``x`` -- data to construct a new matrix from. See :func:`matrix`

        - ``coerce`` -- boolean (default: ``True``); if ``False``, assume
          without checking that the values in ``x`` lie in the base ring

        OUTPUT: a matrix in ``self``

        EXAMPLES::

            sage: M = MatrixSpace(ZZ, 2)
            sage: M.matrix([[1,0],[0,-1]])
            [ 1  0]
            [ 0 -1]
            sage: M.matrix([1,0,0,-1])
            [ 1  0]
            [ 0 -1]
            sage: M.matrix([1,2,3,4])
            [1 2]
            [3 4]

        Note that the last "flip" cannot be performed if ``x`` is a
        matrix, no matter what is ``rows`` (it used to be possible but
        was fixed by :issue:`10793`)::

            sage: projection = matrix(ZZ,[[1,0,0],[0,1,0]])
            sage: projection
            [1 0 0]
            [0 1 0]
            sage: projection.parent()
            Full MatrixSpace of 2 by 3 dense matrices over Integer Ring
            sage: M = MatrixSpace(ZZ, 3 , 2)
            sage: M
            Full MatrixSpace of 3 by 2 dense matrices over Integer Ring
            sage: M(projection)
            Traceback (most recent call last):
            ...
            ValueError: inconsistent number of rows: should be 3 but got 2

        If you really want to make from a matrix another matrix of different
        dimensions, use either transpose method or explicit conversion to a
        list::

            sage: M(projection.list())
            [1 0]
            [0 0]
            [1 0]

        TESTS:

        The following corner cases were problematic while working on
        :issue:`10628`::

            sage: MS = MatrixSpace(ZZ,2,1)
            sage: MS([[1],[2]])
            [1]
            [2]

            sage: # needs sage.rings.real_mpfr
            sage: MS = MatrixSpace(CC, 2, 1)
            sage: x = polygen(ZZ, \'x\')
            sage: F = NumberField(x^2 + 1, name=\'x\')                                    # needs sage.rings.number_field
            sage: MS([F(1), F(0)])                                                      # needs sage.rings.number_field
            [ 1.00000000000000]
            [0.000000000000000]

        :issue:`10628` allowed to provide the data as lists of matrices, but
        :issue:`13012` prohibited it::

            sage: MS = MatrixSpace(ZZ, 4,2)
            sage: MS0 = MatrixSpace(ZZ, 2)
            sage: MS.matrix([MS0([1,2,3,4]), MS0([5,6,7,8])])
            Traceback (most recent call last):
            ...
            TypeError: unable to coerce <class \'sage.matrix.matrix_integer_dense.Matrix_integer_dense\'> to an integer

        A mixed list of matrices and vectors is prohibited as well::

            sage: MS.matrix( [MS0([1,2,3,4])] + list(MS0([5,6,7,8])) )
            Traceback (most recent call last):
            ...
            TypeError: unable to coerce <class \'sage.matrix.matrix_integer_dense.Matrix_integer_dense\'> to an integer

        Check that :issue:`13302` is fixed::

            sage: MatrixSpace(Qp(3), 1,1)([Qp(3).zero()])                               # needs sage.rings.padics
            [0]
            sage: MatrixSpace(Qp(3), 1,1)([Qp(3)(4/3)])                                 # needs sage.rings.padics
            [3^-1 + 1 + O(3^19)]

        One-rowed matrices over combinatorial free modules used to break
        the constructor (:issue:`17124`). Check that this is fixed::

            sage: # needs sage.combinat
            sage: Sym = SymmetricFunctions(ZZ)
            sage: h = Sym.h()
            sage: MatrixSpace(h, 1,1)([h[1]])
            [h[1]]
            sage: MatrixSpace(h, 2,1)([h[1], h[2]])
            [h[1]]
            [h[2]]

        Converting sparse to dense matrices used to be too slow
        (:issue:`20470`). Check that this is fixed::

            sage: m = identity_matrix(GF(2), 2000, sparse=True)
            sage: MS = MatrixSpace(GF(2), 2000, sparse=False)
            sage: md = MS(m)
            sage: md.parent() is MS
            True
        '''
    def matrix_space(self, nrows=None, ncols=None, sparse: bool = False):
        """
        Return the matrix space with given number of rows, columns and
        sparsity over the same base ring as self, and defaults the same as
        ``self``.

        EXAMPLES::

            sage: M = Mat(GF(7), 100, 200)
            sage: M.matrix_space(5000)
            Full MatrixSpace of 5000 by 200 dense matrices over Finite Field of size 7
            sage: M.matrix_space(ncols=5000)
            Full MatrixSpace of 100 by 5000 dense matrices over Finite Field of size 7
            sage: M.matrix_space(sparse=True)
            Full MatrixSpace of 100 by 200 sparse matrices over Finite Field of size 7
        """
    def ncols(self):
        """
        Return the number of columns of matrices in this space.

        EXAMPLES::

            sage: M = Mat(ZZ['x'], 200000, 500000, sparse=True)
            sage: M.ncols()
            500000
        """
    def nrows(self):
        """
        Return the number of rows of matrices in this space.

        EXAMPLES::

            sage: M = Mat(ZZ, 200000, 500000)
            sage: M.nrows()
            200000
        """
    def row_space(self):
        """
        Return the module spanned by all rows of matrices in this matrix
        space. This is a free module of rank the number of rows. It will be
        sparse or dense as this matrix space is sparse or dense.

        EXAMPLES::

            sage: M = Mat(ZZ,20,5,sparse=False); M.row_space()
            Ambient free module of rank 5 over the principal ideal domain Integer Ring
        """
    def column_space(self):
        """
        Return the module spanned by all columns of matrices in this matrix
        space. This is a free module of rank the number of columns. It will
        be sparse or dense as this matrix space is sparse or dense.

        EXAMPLES::

            sage: M = Mat(GF(9,'a'), 20, 5, sparse=True); M.column_space()              # needs sage.rings.finite_rings
            Sparse vector space of dimension 20 over Finite Field in a of size 3^2
        """
    def random_element(self, density=None, *args, **kwds):
        '''
        Return a random element from this matrix space.

        INPUT:

        - ``density`` -- ``float`` or ``None`` (default: ``None``);  rough
          measure of the proportion of nonzero entries in the random matrix;
          if set to ``None``, all entries of the matrix are randomized,
          allowing for any element of the underlying ring, but if set to
          a ``float``, a proportion of entries is selected and randomized to
          nonzero elements of the ring

        - ``*args, **kwds`` -- remaining parameters, which may be passed to
          the random_element function of the base ring. ("may be", since this
          function calls the ``randomize`` function on the zero matrix, which
          need not call the ``random_element`` function of the base ring at
          all in general.)

        OUTPUT: Matrix

        .. NOTE::

            This method will randomize a proportion of roughly ``density`` entries
            in a newly allocated zero matrix.

            By default, if the user sets the value of ``density`` explicitly, this
            method will enforce that these entries are set to nonzero values.
            However, if the test for equality with zero in the base ring is too
            expensive, the user can override this behaviour by passing the
            argument ``nonzero=False`` to this method.

            Otherwise, if the user does not set the value of ``density``, the
            default value is taken to be 1, and the option ``nonzero=False`` is
            passed to the ``randomize`` method.

        EXAMPLES::

            sage: M = Mat(ZZ, 2, 5).random_element()
            sage: TestSuite(M).run()

            sage: M = Mat(QQ, 2, 5).random_element(density=0.5)
            sage: TestSuite(M).run()

            sage: M = Mat(QQ, 3, sparse=True).random_element()
            sage: TestSuite(M).run()                                                    # needs sage.libs.pari

            sage: M = Mat(GF(9,\'a\'), 3, sparse=True).random_element()                   # needs sage.rings.finite_rings
            sage: TestSuite(M).run()                                                    # needs sage.rings.finite_rings
        '''
    def some_elements(self) -> Generator[Incomplete, Incomplete]:
        """
        Return some elements of this matrix space.

        See :class:`TestSuite` for a typical use case.

        OUTPUT: an iterator

        EXAMPLES::

            sage: M = MatrixSpace(ZZ, 2, 2)
            sage: tuple(M.some_elements())
            (
            [ 0  1]  [1 0]  [0 1]  [0 0]  [0 0]
            [-1  2], [0 0], [0 0], [1 0], [0 1]
            )
            sage: M = MatrixSpace(QQ, 2, 3)
            sage: tuple(M.some_elements())
            (
            [ 1/2 -1/2    2]  [1 0 0]  [0 1 0]  [0 0 1]  [0 0 0]  [0 0 0]  [0 0 0]
            [  -2    0    1], [0 0 0], [0 0 0], [0 0 0], [1 0 0], [0 1 0], [0 0 1]
            )
            sage: M = MatrixSpace(SR, 2, 2)                                             # needs sage.symbolic
            sage: tuple(M.some_elements())                                              # needs sage.symbolic
            (
            [some_variable some_variable]  [1 0]  [0 1]  [0 0]  [0 0]
            [some_variable some_variable], [0 0], [0 0], [1 0], [0 1]
            )
        """
    def from_vector(self, vector, order=None, coerce: bool = True):
        """
        Build an element of ``self`` from a vector.

        EXAMPLES::

            sage: A = matrix([[1,2,3], [4,5,6]])
            sage: v = vector(A); v
            (1, 2, 3, 4, 5, 6)
            sage: MS = A.parent()
            sage: MS.from_vector(v)
            [1 2 3]
            [4 5 6]
            sage: order = [(1,2), (1,0), (0,1), (0,2), (0,0), (1,1)]
            sage: MS.from_vector(v, order=order)
            [5 3 4]
            [2 6 1]
        """

def dict_to_list(entries, nrows, ncols):
    """
    Given a dictionary of coordinate tuples, return the list given by
    reading off the nrows\\*ncols matrix in row order.

    EXAMPLES::

        sage: from sage.matrix.matrix_space import dict_to_list
        sage: d = {}
        sage: d[(0,0)] = 1
        sage: d[(1,1)] = 2
        sage: dict_to_list(d, 2, 2)
        [1, 0, 0, 2]
        sage: dict_to_list(d, 2, 3)
        [1, 0, 0, 0, 2, 0]
    """

test_trivial_matrices_inverse: Incomplete
