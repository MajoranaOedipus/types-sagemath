import _cython_3_2_1
import sage.matrix.matrix_dense
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.misc.verbose import get_verbose as get_verbose, verbose as verbose
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

FS_ENCODING: str
VectorSpace: None
from_png: _cython_3_2_1.cython_function_or_method
parity: _cython_3_2_1.cython_function_or_method
ple: _cython_3_2_1.cython_function_or_method
pluq: _cython_3_2_1.cython_function_or_method
to_png: _cython_3_2_1.cython_function_or_method
unpickle_matrix_mod2_dense_v2: _cython_3_2_1.cython_function_or_method

class Matrix_mod2_dense(sage.matrix.matrix_dense.Matrix_dense):
    """Matrix_mod2_dense(parent, entries=None, copy=None, bool coerce=True)

    File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 148)

    Dense matrix over GF(2)."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, entries=..., copy=..., boolcoerce=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 214)

                Construct a dense matrix over GF(2).

                INPUT:

                - ``parent`` -- a matrix space over ``GF(2)``

                - ``entries`` -- see :func:`matrix`

                - ``copy`` -- ignored (for backwards compatibility)

                - ``coerce`` -- if ``False``, assume without checking that the
                  entries lie in the base ring

                EXAMPLES::

                    sage: type(random_matrix(GF(2),2,2))
                    <class 'sage.matrix.matrix_mod2_dense.Matrix_mod2_dense'>

                    sage: Matrix(GF(2),3,3,1)
                    [1 0 0]
                    [0 1 0]
                    [0 0 1]

                    sage: Matrix(GF(2),2,2,[1,1,1,0])
                    [1 1]
                    [1 0]

                    sage: Matrix(GF(2),2,2,4)
                    [0 0]
                    [0 0]

                    sage: Matrix(GF(2),1,1, 1/3)
                    [1]
                    sage: Matrix(GF(2),1,1, [1/3])
                    [1]

                TESTS::

                    sage: Matrix(GF(2),0,0)
                    []
                    sage: Matrix(GF(2),2,0)
                    []
                    sage: Matrix(GF(2),0,2)
                    []

                Make sure construction from numpy array is reasonably fast::

                    sage: # needs numpy
                    sage: import numpy as np
                    sage: n = 5000
                    sage: M = matrix(GF(2), np.random.randint(0, 2, (n, n)))  # around 700ms

                Unsupported numpy data types (slower but still works)::

                    sage: # needs numpy
                    sage: n = 100
                    sage: M = matrix(GF(2), np.random.randint(0, 2, (n, n)).astype(np.float32))
        """
    @overload
    def augment(self, right, subdivide=...) -> Any:
        """Matrix_mod2_dense.augment(self, right, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 1594)

        Augments ``self`` with ``right``.

        EXAMPLES::

            sage: MS = MatrixSpace(GF(2),3,3)
            sage: A = MS([0, 1, 0, 1, 1, 0, 1, 1, 1]); A
            [0 1 0]
            [1 1 0]
            [1 1 1]
            sage: B = A.augment(MS(1)); B
            [0 1 0 1 0 0]
            [1 1 0 0 1 0]
            [1 1 1 0 0 1]
            sage: B.echelonize(); B
            [1 0 0 1 1 0]
            [0 1 0 1 0 0]
            [0 0 1 0 1 1]
            sage: C = B.matrix_from_columns([3,4,5]); C
            [1 1 0]
            [1 0 0]
            [0 1 1]
            sage: C == ~A
            True
            sage: C*A == MS(1)
            True

        A vector may be augmented to a matrix. ::

            sage: A = matrix(GF(2), 3, 4, range(12))
            sage: v = vector(GF(2), 3, range(3))
            sage: A.augment(v)
            [0 1 0 1 0]
            [0 1 0 1 1]
            [0 1 0 1 0]

        The ``subdivide`` option will add a natural subdivision between
        ``self`` and ``right``.  For more details about how subdivisions
        are managed when augmenting, see
        :meth:`sage.matrix.matrix1.Matrix.augment`.  ::

            sage: A = matrix(GF(2), 3, 5, range(15))
            sage: B = matrix(GF(2), 3, 3, range(9))
            sage: A.augment(B, subdivide=True)
            [0 1 0 1 0|0 1 0]
            [1 0 1 0 1|1 0 1]
            [0 1 0 1 0|0 1 0]

        TESTS::

            sage: A = random_matrix(GF(2),2,3)
            sage: B = random_matrix(GF(2),2,0)
            sage: A.augment(B) == A
            True

            sage: B.augment(A) == A
            True

            sage: M = Matrix(GF(2), 0, 0, 0)
            sage: N = Matrix(GF(2), 0, 19, 0)
            sage: W = M.augment(N)
            sage: W.ncols()
            19
            sage: M = Matrix(GF(2), 0, 1, 0)
            sage: N = Matrix(GF(2), 0, 1, 0)
            sage: M.augment(N)
            []

        Check that :issue:`19165` is solved::

            sage: m = matrix(GF(2), 2, range(4))
            sage: m.augment(matrix(GF(2), 2, range(4), sparse=True))
            [0 1 0 1]
            [0 1 0 1]

            sage: m.augment(1)
            Traceback (most recent call last):
            ...
            TypeError: right must either be a matrix or a vector. Not
            <class 'sage.rings.integer.Integer'>"""
    @overload
    def augment(self, v) -> Any:
        """Matrix_mod2_dense.augment(self, right, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 1594)

        Augments ``self`` with ``right``.

        EXAMPLES::

            sage: MS = MatrixSpace(GF(2),3,3)
            sage: A = MS([0, 1, 0, 1, 1, 0, 1, 1, 1]); A
            [0 1 0]
            [1 1 0]
            [1 1 1]
            sage: B = A.augment(MS(1)); B
            [0 1 0 1 0 0]
            [1 1 0 0 1 0]
            [1 1 1 0 0 1]
            sage: B.echelonize(); B
            [1 0 0 1 1 0]
            [0 1 0 1 0 0]
            [0 0 1 0 1 1]
            sage: C = B.matrix_from_columns([3,4,5]); C
            [1 1 0]
            [1 0 0]
            [0 1 1]
            sage: C == ~A
            True
            sage: C*A == MS(1)
            True

        A vector may be augmented to a matrix. ::

            sage: A = matrix(GF(2), 3, 4, range(12))
            sage: v = vector(GF(2), 3, range(3))
            sage: A.augment(v)
            [0 1 0 1 0]
            [0 1 0 1 1]
            [0 1 0 1 0]

        The ``subdivide`` option will add a natural subdivision between
        ``self`` and ``right``.  For more details about how subdivisions
        are managed when augmenting, see
        :meth:`sage.matrix.matrix1.Matrix.augment`.  ::

            sage: A = matrix(GF(2), 3, 5, range(15))
            sage: B = matrix(GF(2), 3, 3, range(9))
            sage: A.augment(B, subdivide=True)
            [0 1 0 1 0|0 1 0]
            [1 0 1 0 1|1 0 1]
            [0 1 0 1 0|0 1 0]

        TESTS::

            sage: A = random_matrix(GF(2),2,3)
            sage: B = random_matrix(GF(2),2,0)
            sage: A.augment(B) == A
            True

            sage: B.augment(A) == A
            True

            sage: M = Matrix(GF(2), 0, 0, 0)
            sage: N = Matrix(GF(2), 0, 19, 0)
            sage: W = M.augment(N)
            sage: W.ncols()
            19
            sage: M = Matrix(GF(2), 0, 1, 0)
            sage: N = Matrix(GF(2), 0, 1, 0)
            sage: M.augment(N)
            []

        Check that :issue:`19165` is solved::

            sage: m = matrix(GF(2), 2, range(4))
            sage: m.augment(matrix(GF(2), 2, range(4), sparse=True))
            [0 1 0 1]
            [0 1 0 1]

            sage: m.augment(1)
            Traceback (most recent call last):
            ...
            TypeError: right must either be a matrix or a vector. Not
            <class 'sage.rings.integer.Integer'>"""
    @overload
    def augment(self, B, subdivide=...) -> Any:
        """Matrix_mod2_dense.augment(self, right, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 1594)

        Augments ``self`` with ``right``.

        EXAMPLES::

            sage: MS = MatrixSpace(GF(2),3,3)
            sage: A = MS([0, 1, 0, 1, 1, 0, 1, 1, 1]); A
            [0 1 0]
            [1 1 0]
            [1 1 1]
            sage: B = A.augment(MS(1)); B
            [0 1 0 1 0 0]
            [1 1 0 0 1 0]
            [1 1 1 0 0 1]
            sage: B.echelonize(); B
            [1 0 0 1 1 0]
            [0 1 0 1 0 0]
            [0 0 1 0 1 1]
            sage: C = B.matrix_from_columns([3,4,5]); C
            [1 1 0]
            [1 0 0]
            [0 1 1]
            sage: C == ~A
            True
            sage: C*A == MS(1)
            True

        A vector may be augmented to a matrix. ::

            sage: A = matrix(GF(2), 3, 4, range(12))
            sage: v = vector(GF(2), 3, range(3))
            sage: A.augment(v)
            [0 1 0 1 0]
            [0 1 0 1 1]
            [0 1 0 1 0]

        The ``subdivide`` option will add a natural subdivision between
        ``self`` and ``right``.  For more details about how subdivisions
        are managed when augmenting, see
        :meth:`sage.matrix.matrix1.Matrix.augment`.  ::

            sage: A = matrix(GF(2), 3, 5, range(15))
            sage: B = matrix(GF(2), 3, 3, range(9))
            sage: A.augment(B, subdivide=True)
            [0 1 0 1 0|0 1 0]
            [1 0 1 0 1|1 0 1]
            [0 1 0 1 0|0 1 0]

        TESTS::

            sage: A = random_matrix(GF(2),2,3)
            sage: B = random_matrix(GF(2),2,0)
            sage: A.augment(B) == A
            True

            sage: B.augment(A) == A
            True

            sage: M = Matrix(GF(2), 0, 0, 0)
            sage: N = Matrix(GF(2), 0, 19, 0)
            sage: W = M.augment(N)
            sage: W.ncols()
            19
            sage: M = Matrix(GF(2), 0, 1, 0)
            sage: N = Matrix(GF(2), 0, 1, 0)
            sage: M.augment(N)
            []

        Check that :issue:`19165` is solved::

            sage: m = matrix(GF(2), 2, range(4))
            sage: m.augment(matrix(GF(2), 2, range(4), sparse=True))
            [0 1 0 1]
            [0 1 0 1]

            sage: m.augment(1)
            Traceback (most recent call last):
            ...
            TypeError: right must either be a matrix or a vector. Not
            <class 'sage.rings.integer.Integer'>"""
    @overload
    def augment(self, B) -> Any:
        """Matrix_mod2_dense.augment(self, right, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 1594)

        Augments ``self`` with ``right``.

        EXAMPLES::

            sage: MS = MatrixSpace(GF(2),3,3)
            sage: A = MS([0, 1, 0, 1, 1, 0, 1, 1, 1]); A
            [0 1 0]
            [1 1 0]
            [1 1 1]
            sage: B = A.augment(MS(1)); B
            [0 1 0 1 0 0]
            [1 1 0 0 1 0]
            [1 1 1 0 0 1]
            sage: B.echelonize(); B
            [1 0 0 1 1 0]
            [0 1 0 1 0 0]
            [0 0 1 0 1 1]
            sage: C = B.matrix_from_columns([3,4,5]); C
            [1 1 0]
            [1 0 0]
            [0 1 1]
            sage: C == ~A
            True
            sage: C*A == MS(1)
            True

        A vector may be augmented to a matrix. ::

            sage: A = matrix(GF(2), 3, 4, range(12))
            sage: v = vector(GF(2), 3, range(3))
            sage: A.augment(v)
            [0 1 0 1 0]
            [0 1 0 1 1]
            [0 1 0 1 0]

        The ``subdivide`` option will add a natural subdivision between
        ``self`` and ``right``.  For more details about how subdivisions
        are managed when augmenting, see
        :meth:`sage.matrix.matrix1.Matrix.augment`.  ::

            sage: A = matrix(GF(2), 3, 5, range(15))
            sage: B = matrix(GF(2), 3, 3, range(9))
            sage: A.augment(B, subdivide=True)
            [0 1 0 1 0|0 1 0]
            [1 0 1 0 1|1 0 1]
            [0 1 0 1 0|0 1 0]

        TESTS::

            sage: A = random_matrix(GF(2),2,3)
            sage: B = random_matrix(GF(2),2,0)
            sage: A.augment(B) == A
            True

            sage: B.augment(A) == A
            True

            sage: M = Matrix(GF(2), 0, 0, 0)
            sage: N = Matrix(GF(2), 0, 19, 0)
            sage: W = M.augment(N)
            sage: W.ncols()
            19
            sage: M = Matrix(GF(2), 0, 1, 0)
            sage: N = Matrix(GF(2), 0, 1, 0)
            sage: M.augment(N)
            []

        Check that :issue:`19165` is solved::

            sage: m = matrix(GF(2), 2, range(4))
            sage: m.augment(matrix(GF(2), 2, range(4), sparse=True))
            [0 1 0 1]
            [0 1 0 1]

            sage: m.augment(1)
            Traceback (most recent call last):
            ...
            TypeError: right must either be a matrix or a vector. Not
            <class 'sage.rings.integer.Integer'>"""
    @overload
    def augment(self, A) -> Any:
        """Matrix_mod2_dense.augment(self, right, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 1594)

        Augments ``self`` with ``right``.

        EXAMPLES::

            sage: MS = MatrixSpace(GF(2),3,3)
            sage: A = MS([0, 1, 0, 1, 1, 0, 1, 1, 1]); A
            [0 1 0]
            [1 1 0]
            [1 1 1]
            sage: B = A.augment(MS(1)); B
            [0 1 0 1 0 0]
            [1 1 0 0 1 0]
            [1 1 1 0 0 1]
            sage: B.echelonize(); B
            [1 0 0 1 1 0]
            [0 1 0 1 0 0]
            [0 0 1 0 1 1]
            sage: C = B.matrix_from_columns([3,4,5]); C
            [1 1 0]
            [1 0 0]
            [0 1 1]
            sage: C == ~A
            True
            sage: C*A == MS(1)
            True

        A vector may be augmented to a matrix. ::

            sage: A = matrix(GF(2), 3, 4, range(12))
            sage: v = vector(GF(2), 3, range(3))
            sage: A.augment(v)
            [0 1 0 1 0]
            [0 1 0 1 1]
            [0 1 0 1 0]

        The ``subdivide`` option will add a natural subdivision between
        ``self`` and ``right``.  For more details about how subdivisions
        are managed when augmenting, see
        :meth:`sage.matrix.matrix1.Matrix.augment`.  ::

            sage: A = matrix(GF(2), 3, 5, range(15))
            sage: B = matrix(GF(2), 3, 3, range(9))
            sage: A.augment(B, subdivide=True)
            [0 1 0 1 0|0 1 0]
            [1 0 1 0 1|1 0 1]
            [0 1 0 1 0|0 1 0]

        TESTS::

            sage: A = random_matrix(GF(2),2,3)
            sage: B = random_matrix(GF(2),2,0)
            sage: A.augment(B) == A
            True

            sage: B.augment(A) == A
            True

            sage: M = Matrix(GF(2), 0, 0, 0)
            sage: N = Matrix(GF(2), 0, 19, 0)
            sage: W = M.augment(N)
            sage: W.ncols()
            19
            sage: M = Matrix(GF(2), 0, 1, 0)
            sage: N = Matrix(GF(2), 0, 1, 0)
            sage: M.augment(N)
            []

        Check that :issue:`19165` is solved::

            sage: m = matrix(GF(2), 2, range(4))
            sage: m.augment(matrix(GF(2), 2, range(4), sparse=True))
            [0 1 0 1]
            [0 1 0 1]

            sage: m.augment(1)
            Traceback (most recent call last):
            ...
            TypeError: right must either be a matrix or a vector. Not
            <class 'sage.rings.integer.Integer'>"""
    @overload
    def augment(self, N) -> Any:
        """Matrix_mod2_dense.augment(self, right, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 1594)

        Augments ``self`` with ``right``.

        EXAMPLES::

            sage: MS = MatrixSpace(GF(2),3,3)
            sage: A = MS([0, 1, 0, 1, 1, 0, 1, 1, 1]); A
            [0 1 0]
            [1 1 0]
            [1 1 1]
            sage: B = A.augment(MS(1)); B
            [0 1 0 1 0 0]
            [1 1 0 0 1 0]
            [1 1 1 0 0 1]
            sage: B.echelonize(); B
            [1 0 0 1 1 0]
            [0 1 0 1 0 0]
            [0 0 1 0 1 1]
            sage: C = B.matrix_from_columns([3,4,5]); C
            [1 1 0]
            [1 0 0]
            [0 1 1]
            sage: C == ~A
            True
            sage: C*A == MS(1)
            True

        A vector may be augmented to a matrix. ::

            sage: A = matrix(GF(2), 3, 4, range(12))
            sage: v = vector(GF(2), 3, range(3))
            sage: A.augment(v)
            [0 1 0 1 0]
            [0 1 0 1 1]
            [0 1 0 1 0]

        The ``subdivide`` option will add a natural subdivision between
        ``self`` and ``right``.  For more details about how subdivisions
        are managed when augmenting, see
        :meth:`sage.matrix.matrix1.Matrix.augment`.  ::

            sage: A = matrix(GF(2), 3, 5, range(15))
            sage: B = matrix(GF(2), 3, 3, range(9))
            sage: A.augment(B, subdivide=True)
            [0 1 0 1 0|0 1 0]
            [1 0 1 0 1|1 0 1]
            [0 1 0 1 0|0 1 0]

        TESTS::

            sage: A = random_matrix(GF(2),2,3)
            sage: B = random_matrix(GF(2),2,0)
            sage: A.augment(B) == A
            True

            sage: B.augment(A) == A
            True

            sage: M = Matrix(GF(2), 0, 0, 0)
            sage: N = Matrix(GF(2), 0, 19, 0)
            sage: W = M.augment(N)
            sage: W.ncols()
            19
            sage: M = Matrix(GF(2), 0, 1, 0)
            sage: N = Matrix(GF(2), 0, 1, 0)
            sage: M.augment(N)
            []

        Check that :issue:`19165` is solved::

            sage: m = matrix(GF(2), 2, range(4))
            sage: m.augment(matrix(GF(2), 2, range(4), sparse=True))
            [0 1 0 1]
            [0 1 0 1]

            sage: m.augment(1)
            Traceback (most recent call last):
            ...
            TypeError: right must either be a matrix or a vector. Not
            <class 'sage.rings.integer.Integer'>"""
    @overload
    def augment(self, N) -> Any:
        """Matrix_mod2_dense.augment(self, right, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 1594)

        Augments ``self`` with ``right``.

        EXAMPLES::

            sage: MS = MatrixSpace(GF(2),3,3)
            sage: A = MS([0, 1, 0, 1, 1, 0, 1, 1, 1]); A
            [0 1 0]
            [1 1 0]
            [1 1 1]
            sage: B = A.augment(MS(1)); B
            [0 1 0 1 0 0]
            [1 1 0 0 1 0]
            [1 1 1 0 0 1]
            sage: B.echelonize(); B
            [1 0 0 1 1 0]
            [0 1 0 1 0 0]
            [0 0 1 0 1 1]
            sage: C = B.matrix_from_columns([3,4,5]); C
            [1 1 0]
            [1 0 0]
            [0 1 1]
            sage: C == ~A
            True
            sage: C*A == MS(1)
            True

        A vector may be augmented to a matrix. ::

            sage: A = matrix(GF(2), 3, 4, range(12))
            sage: v = vector(GF(2), 3, range(3))
            sage: A.augment(v)
            [0 1 0 1 0]
            [0 1 0 1 1]
            [0 1 0 1 0]

        The ``subdivide`` option will add a natural subdivision between
        ``self`` and ``right``.  For more details about how subdivisions
        are managed when augmenting, see
        :meth:`sage.matrix.matrix1.Matrix.augment`.  ::

            sage: A = matrix(GF(2), 3, 5, range(15))
            sage: B = matrix(GF(2), 3, 3, range(9))
            sage: A.augment(B, subdivide=True)
            [0 1 0 1 0|0 1 0]
            [1 0 1 0 1|1 0 1]
            [0 1 0 1 0|0 1 0]

        TESTS::

            sage: A = random_matrix(GF(2),2,3)
            sage: B = random_matrix(GF(2),2,0)
            sage: A.augment(B) == A
            True

            sage: B.augment(A) == A
            True

            sage: M = Matrix(GF(2), 0, 0, 0)
            sage: N = Matrix(GF(2), 0, 19, 0)
            sage: W = M.augment(N)
            sage: W.ncols()
            19
            sage: M = Matrix(GF(2), 0, 1, 0)
            sage: N = Matrix(GF(2), 0, 1, 0)
            sage: M.augment(N)
            []

        Check that :issue:`19165` is solved::

            sage: m = matrix(GF(2), 2, range(4))
            sage: m.augment(matrix(GF(2), 2, range(4), sparse=True))
            [0 1 0 1]
            [0 1 0 1]

            sage: m.augment(1)
            Traceback (most recent call last):
            ...
            TypeError: right must either be a matrix or a vector. Not
            <class 'sage.rings.integer.Integer'>"""
    @overload
    def columns(self, copy=...) -> Any:
        """Matrix_mod2_dense.columns(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 585)

        Return list of the columns of ``self``.

        INPUT:

        - ``copy`` -- (default: ``True``) if True, return a copy so you can
          modify it safely

        EXAMPLES:

        An example with a small 3x3 matrix::

            sage: M2 = Matrix(GF(2), [[1, 0, 0], [0, 1, 0], [0, 1, 1]])
            sage: M2.columns()
            [(1, 0, 0), (0, 1, 1), (0, 0, 1)]"""
    @overload
    def columns(self) -> Any:
        """Matrix_mod2_dense.columns(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 585)

        Return list of the columns of ``self``.

        INPUT:

        - ``copy`` -- (default: ``True``) if True, return a copy so you can
          modify it safely

        EXAMPLES:

        An example with a small 3x3 matrix::

            sage: M2 = Matrix(GF(2), [[1, 0, 0], [0, 1, 0], [0, 1, 1]])
            sage: M2.columns()
            [(1, 0, 0), (0, 1, 1), (0, 0, 1)]"""
    @overload
    def density(self, approx=...) -> Any:
        """Matrix_mod2_dense.density(self, approx=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 1943)

        Return the density of this matrix.

        By density we understand the ratio of the number of nonzero
        positions and the self.nrows() * self.ncols(), i.e. the number
        of possible nonzero positions.

        INPUT:

        - ``approx`` -- return floating point approximation (default: ``False``)

        EXAMPLES::

            sage: A = random_matrix(GF(2), 1000, 1000)
            sage: d = A.density()
            sage: float(d) == A.density(approx=True)
            True
            sage: len(A.nonzero_positions())/1000^2 == d
            True

            sage: total = 1.0
            sage: density_sum = A.density()
            sage: while abs(density_sum/total - 0.5) > 0.001:
            ....:     A = random_matrix(GF(2), 1000, 1000)
            ....:     total += 1
            ....:     density_sum += A.density()"""
    @overload
    def density(self) -> Any:
        """Matrix_mod2_dense.density(self, approx=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 1943)

        Return the density of this matrix.

        By density we understand the ratio of the number of nonzero
        positions and the self.nrows() * self.ncols(), i.e. the number
        of possible nonzero positions.

        INPUT:

        - ``approx`` -- return floating point approximation (default: ``False``)

        EXAMPLES::

            sage: A = random_matrix(GF(2), 1000, 1000)
            sage: d = A.density()
            sage: float(d) == A.density(approx=True)
            True
            sage: len(A.nonzero_positions())/1000^2 == d
            True

            sage: total = 1.0
            sage: density_sum = A.density()
            sage: while abs(density_sum/total - 0.5) > 0.001:
            ....:     A = random_matrix(GF(2), 1000, 1000)
            ....:     total += 1
            ....:     density_sum += A.density()"""
    @overload
    def density(self, approx=...) -> Any:
        """Matrix_mod2_dense.density(self, approx=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 1943)

        Return the density of this matrix.

        By density we understand the ratio of the number of nonzero
        positions and the self.nrows() * self.ncols(), i.e. the number
        of possible nonzero positions.

        INPUT:

        - ``approx`` -- return floating point approximation (default: ``False``)

        EXAMPLES::

            sage: A = random_matrix(GF(2), 1000, 1000)
            sage: d = A.density()
            sage: float(d) == A.density(approx=True)
            True
            sage: len(A.nonzero_positions())/1000^2 == d
            True

            sage: total = 1.0
            sage: density_sum = A.density()
            sage: while abs(density_sum/total - 0.5) > 0.001:
            ....:     A = random_matrix(GF(2), 1000, 1000)
            ....:     total += 1
            ....:     density_sum += A.density()"""
    @overload
    def density(self) -> Any:
        """Matrix_mod2_dense.density(self, approx=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 1943)

        Return the density of this matrix.

        By density we understand the ratio of the number of nonzero
        positions and the self.nrows() * self.ncols(), i.e. the number
        of possible nonzero positions.

        INPUT:

        - ``approx`` -- return floating point approximation (default: ``False``)

        EXAMPLES::

            sage: A = random_matrix(GF(2), 1000, 1000)
            sage: d = A.density()
            sage: float(d) == A.density(approx=True)
            True
            sage: len(A.nonzero_positions())/1000^2 == d
            True

            sage: total = 1.0
            sage: density_sum = A.density()
            sage: while abs(density_sum/total - 0.5) > 0.001:
            ....:     A = random_matrix(GF(2), 1000, 1000)
            ....:     total += 1
            ....:     density_sum += A.density()"""
    @overload
    def density(self) -> Any:
        """Matrix_mod2_dense.density(self, approx=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 1943)

        Return the density of this matrix.

        By density we understand the ratio of the number of nonzero
        positions and the self.nrows() * self.ncols(), i.e. the number
        of possible nonzero positions.

        INPUT:

        - ``approx`` -- return floating point approximation (default: ``False``)

        EXAMPLES::

            sage: A = random_matrix(GF(2), 1000, 1000)
            sage: d = A.density()
            sage: float(d) == A.density(approx=True)
            True
            sage: len(A.nonzero_positions())/1000^2 == d
            True

            sage: total = 1.0
            sage: density_sum = A.density()
            sage: while abs(density_sum/total - 0.5) > 0.001:
            ....:     A = random_matrix(GF(2), 1000, 1000)
            ....:     total += 1
            ....:     density_sum += A.density()"""
    @overload
    def determinant(self) -> Any:
        """Matrix_mod2_dense.determinant(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 1481)

        Return the determinant of this matrix over GF(2).

        EXAMPLES::

            sage: matrix(GF(2),2,[1,1,0,1]).determinant()
            1
            sage: matrix(GF(2),2,[1,1,1,1]).determinant()
            0"""
    @overload
    def determinant(self) -> Any:
        """Matrix_mod2_dense.determinant(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 1481)

        Return the determinant of this matrix over GF(2).

        EXAMPLES::

            sage: matrix(GF(2),2,[1,1,0,1]).determinant()
            1
            sage: matrix(GF(2),2,[1,1,1,1]).determinant()
            0"""
    @overload
    def determinant(self) -> Any:
        """Matrix_mod2_dense.determinant(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 1481)

        Return the determinant of this matrix over GF(2).

        EXAMPLES::

            sage: matrix(GF(2),2,[1,1,0,1]).determinant()
            1
            sage: matrix(GF(2),2,[1,1,1,1]).determinant()
            0"""
    def doubly_lexical_ordering(self, inplace=...) -> Any:
        """Matrix_mod2_dense.doubly_lexical_ordering(self, inplace=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 2205)

        Return a doubly lexical ordering of the matrix.

        A doubly lexical ordering of a matrix is an ordering of the rows
        and of the columns of the matrix so that both the rows and the
        columns, as vectors, are lexically increasing. See [Lub1987]_.
        A lexical ordering of vectors is the standard dictionary ordering,
        except that vectors will be read from highest to lowest coordinate.
        Thus row vectors will be compared from right to left, and column
        vectors from bottom to top.

        INPUT:

        - ``inplace`` -- boolean (default: ``False``); using ``inplace=True``
          will permute the rows and columns of the current matrix
          according to a doubly lexical ordering; this will modify the matrix

        OUTPUT:

        A pair ``(row_ordering, col_ordering)`` of
        :class:`~sage.groups.perm_gps.constructor.PermutationGroupElement`
        that represents a doubly lexical ordering of the rows or columns.

        .. SEEALSO::

            :meth:`~sage.matrix.matrix2.Matrix.permutation_normal_form`;
            a similar matrix normal form

        ALGORITHM:

        The algorithm is adapted from section 3 of [HAM1985]_. The time
        complexity of this algorithm is `O(n \\cdot m^2)` for a `n \\times m`
        matrix.

        EXAMPLES::

            sage: A = Matrix(GF(2), [[0, 1],
            ....:                    [1, 0]])
            sage: r, c = A.doubly_lexical_ordering()
            sage: r
            (1,2)
            sage: c
            ()
            sage: A.permute_rows_and_columns(r, c); A
            [1 0]
            [0 1]

        ::

            sage: A = Matrix(GF(2), [[0, 1],
            ....:                    [1, 0]])
            sage: r, c = A.doubly_lexical_ordering(inplace=True); A
            [1 0]
            [0 1]

        TESTS:

        This algorithm works correctly for the matrix in
        Example 3.7 in [HAM1985]_::

            sage: A = Matrix(GF(2), [[1, 1, 0, 0, 0, 0, 0],
            ....:                    [1, 1, 0, 0, 0, 0, 0],
            ....:                    [1, 1, 0, 1, 0, 0, 0],
            ....:                    [0, 0, 1, 1, 0, 0, 0],
            ....:                    [0, 1, 1, 1, 1, 0, 0],
            ....:                    [0, 0, 0, 0, 0, 1, 1],
            ....:                    [0, 0, 0, 0, 0, 1, 1],
            ....:                    [0, 0, 0, 0, 1, 1, 1],
            ....:                    [0, 0, 0, 1, 1, 1, 0]])
            sage: r, c = A.doubly_lexical_ordering()
            sage: B = A.with_permuted_rows_and_columns(r, c)
            sage: for i in range(B.ncols()):
            ....:     for j in range(i):
            ....:         for k in reversed(range(B.nrows())):
            ....:             assert B[k][j] <= B[k][i]
            ....:             if B[k][j] < B[k][i]:
            ....:                 break
            sage: for i in range(B.nrows()):
            ....:     for j in range(i):
            ....:         for k in reversed(range(B.ncols())):
            ....:             assert B[j][k] <= B[i][k]
            ....:             if B[j][k] < B[i][k]:
            ....:                 break
            sage: r, c = A.doubly_lexical_ordering(inplace=True)
            sage: A == B
            True

        An immutable matrix calling with ``inplace=True`` will raise an error::

            sage: A = Matrix(GF(2), [[0, 1], [1, 0]], immutable=True)
            sage: r, c = A.doubly_lexical_ordering(inplace=True)
            Traceback (most recent call last):
            ...
            TypeError: this matrix is immutable;
             use inplace=False or apply to a mutable copy.

        The algorithm works collectly for a matrix with nrows=0 or ncols=0::

            sage: A = Matrix(GF(2), 0, 2, [])
            sage: A.doubly_lexical_ordering()
            ((), ())
            sage: B = Matrix(GF(2), 2, 0, [])
            sage: B.doubly_lexical_ordering()
            ((), ())"""
    @overload
    def echelonize(self, algorithm=..., cutoff=..., reduced=..., **kwds) -> Any:
        """Matrix_mod2_dense.echelonize(self, algorithm='heuristic', cutoff=0, reduced=True, **kwds)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 1115)

        Puts ``self`` in (reduced) row echelon form.

        INPUT:

        - ``self`` -- a mutable matrix
        - ``algorithm`` -- string; one of

          - ``'heuristic'`` -- uses M4RI and PLUQ (default)
          - ``'m4ri'`` -- uses M4RI
          - ``'pluq'`` -- uses PLUQ factorization
          - ``'classical'`` -- uses classical Gaussian elimination

        - ``k`` -- the parameter 'k' of the M4RI algorithm. It MUST be between 1
          and 16 (inclusive). If it is not specified it will be calculated as
          3/4 * log_2( min(nrows, ncols) ) as suggested in the M4RI paper.
        - ``reduced`` -- return reduced row echelon form (default: ``True``)

        EXAMPLES::

             sage: A = random_matrix(GF(2), 10, 10)
             sage: B = A.__copy__(); B.echelonize() # fastest
             sage: C = A.__copy__(); C.echelonize(k=2) # force k
             sage: E = A.__copy__(); E.echelonize(algorithm='classical') # force Gaussian elimination
             sage: B == C == E
             True

        TESTS::

             sage: VF2 = VectorSpace(GF(2),2)
             sage: WF2 = VF2.submodule([VF2([1,1])])
             sage: WF2
             Vector space of degree 2 and dimension 1 over Finite Field of size 2
             Basis matrix:
             [1 1]

             sage: A2 = matrix(GF(2),2,[1,0,0,1])
             sage: A2.kernel()
             Vector space of degree 2 and dimension 0 over Finite Field of size 2
             Basis matrix:
             []

        ALGORITHM:

        Uses M4RI library

        REFERENCES:

        - [Bar2006]_"""
    @overload
    def echelonize(self) -> Any:
        """Matrix_mod2_dense.echelonize(self, algorithm='heuristic', cutoff=0, reduced=True, **kwds)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 1115)

        Puts ``self`` in (reduced) row echelon form.

        INPUT:

        - ``self`` -- a mutable matrix
        - ``algorithm`` -- string; one of

          - ``'heuristic'`` -- uses M4RI and PLUQ (default)
          - ``'m4ri'`` -- uses M4RI
          - ``'pluq'`` -- uses PLUQ factorization
          - ``'classical'`` -- uses classical Gaussian elimination

        - ``k`` -- the parameter 'k' of the M4RI algorithm. It MUST be between 1
          and 16 (inclusive). If it is not specified it will be calculated as
          3/4 * log_2( min(nrows, ncols) ) as suggested in the M4RI paper.
        - ``reduced`` -- return reduced row echelon form (default: ``True``)

        EXAMPLES::

             sage: A = random_matrix(GF(2), 10, 10)
             sage: B = A.__copy__(); B.echelonize() # fastest
             sage: C = A.__copy__(); C.echelonize(k=2) # force k
             sage: E = A.__copy__(); E.echelonize(algorithm='classical') # force Gaussian elimination
             sage: B == C == E
             True

        TESTS::

             sage: VF2 = VectorSpace(GF(2),2)
             sage: WF2 = VF2.submodule([VF2([1,1])])
             sage: WF2
             Vector space of degree 2 and dimension 1 over Finite Field of size 2
             Basis matrix:
             [1 1]

             sage: A2 = matrix(GF(2),2,[1,0,0,1])
             sage: A2.kernel()
             Vector space of degree 2 and dimension 0 over Finite Field of size 2
             Basis matrix:
             []

        ALGORITHM:

        Uses M4RI library

        REFERENCES:

        - [Bar2006]_"""
    @overload
    def echelonize(self, k=...) -> Any:
        """Matrix_mod2_dense.echelonize(self, algorithm='heuristic', cutoff=0, reduced=True, **kwds)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 1115)

        Puts ``self`` in (reduced) row echelon form.

        INPUT:

        - ``self`` -- a mutable matrix
        - ``algorithm`` -- string; one of

          - ``'heuristic'`` -- uses M4RI and PLUQ (default)
          - ``'m4ri'`` -- uses M4RI
          - ``'pluq'`` -- uses PLUQ factorization
          - ``'classical'`` -- uses classical Gaussian elimination

        - ``k`` -- the parameter 'k' of the M4RI algorithm. It MUST be between 1
          and 16 (inclusive). If it is not specified it will be calculated as
          3/4 * log_2( min(nrows, ncols) ) as suggested in the M4RI paper.
        - ``reduced`` -- return reduced row echelon form (default: ``True``)

        EXAMPLES::

             sage: A = random_matrix(GF(2), 10, 10)
             sage: B = A.__copy__(); B.echelonize() # fastest
             sage: C = A.__copy__(); C.echelonize(k=2) # force k
             sage: E = A.__copy__(); E.echelonize(algorithm='classical') # force Gaussian elimination
             sage: B == C == E
             True

        TESTS::

             sage: VF2 = VectorSpace(GF(2),2)
             sage: WF2 = VF2.submodule([VF2([1,1])])
             sage: WF2
             Vector space of degree 2 and dimension 1 over Finite Field of size 2
             Basis matrix:
             [1 1]

             sage: A2 = matrix(GF(2),2,[1,0,0,1])
             sage: A2.kernel()
             Vector space of degree 2 and dimension 0 over Finite Field of size 2
             Basis matrix:
             []

        ALGORITHM:

        Uses M4RI library

        REFERENCES:

        - [Bar2006]_"""
    @overload
    def echelonize(self, algorithm=...) -> Any:
        """Matrix_mod2_dense.echelonize(self, algorithm='heuristic', cutoff=0, reduced=True, **kwds)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 1115)

        Puts ``self`` in (reduced) row echelon form.

        INPUT:

        - ``self`` -- a mutable matrix
        - ``algorithm`` -- string; one of

          - ``'heuristic'`` -- uses M4RI and PLUQ (default)
          - ``'m4ri'`` -- uses M4RI
          - ``'pluq'`` -- uses PLUQ factorization
          - ``'classical'`` -- uses classical Gaussian elimination

        - ``k`` -- the parameter 'k' of the M4RI algorithm. It MUST be between 1
          and 16 (inclusive). If it is not specified it will be calculated as
          3/4 * log_2( min(nrows, ncols) ) as suggested in the M4RI paper.
        - ``reduced`` -- return reduced row echelon form (default: ``True``)

        EXAMPLES::

             sage: A = random_matrix(GF(2), 10, 10)
             sage: B = A.__copy__(); B.echelonize() # fastest
             sage: C = A.__copy__(); C.echelonize(k=2) # force k
             sage: E = A.__copy__(); E.echelonize(algorithm='classical') # force Gaussian elimination
             sage: B == C == E
             True

        TESTS::

             sage: VF2 = VectorSpace(GF(2),2)
             sage: WF2 = VF2.submodule([VF2([1,1])])
             sage: WF2
             Vector space of degree 2 and dimension 1 over Finite Field of size 2
             Basis matrix:
             [1 1]

             sage: A2 = matrix(GF(2),2,[1,0,0,1])
             sage: A2.kernel()
             Vector space of degree 2 and dimension 0 over Finite Field of size 2
             Basis matrix:
             []

        ALGORITHM:

        Uses M4RI library

        REFERENCES:

        - [Bar2006]_"""
    def is_Gamma_free(self, certificate=...) -> Any:
        """Matrix_mod2_dense.is_Gamma_free(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 2380)

        Return True if the matrix is `\\Gamma`-free.

        A matrix is `\\Gamma`-free if it does not contain a 2x2 submatrix
        of the form:

        .. MATH::

            \\begin{pmatrix}
                1 & 1 \\\\\n                1 & 0
            \\end{pmatrix}

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); whether to return a
          certificate for no-answers (see OUTPUT section)

        OUTPUT:

        When ``certificate`` is set to ``False`` (default) this method only
        returns ``True`` or ``False`` answers. When ``certificate`` is set to
        ``True``, the method either returns ``(True, None)`` or ``(False,
        (r1, c1, r2, c2))`` where ``r1``, ``r2``-th rows and ``c1``,
        ``c2``-th columns of the matrix constitute the `\\Gamma`-submatrix.

        ALGORITHM:

        For each 1 entry, the algorithm finds the next 1 in the same row and
        the next 1 in the same column, and check the 2x2 submatrix that contains
        these entries forms `\\Gamma` submatrix. The time complexity of
        this algorithm is `O(n \\cdot m)` for a `n \\times m` matrix.

        EXAMPLES::

            sage: A = Matrix(GF(2), [[1, 1],
            ....:                    [0, 0]])
            sage: A.is_Gamma_free()
            True
            sage: B = Matrix(GF(2), [[1, 1],
            ....:                    [1, 0]])
            sage: B.is_Gamma_free(certificate=True)
            (False, (0, 0, 1, 1))

        TESTS:

        The algorithm works collectly for larger matrices::

            sage: A = Matrix(GF(2), [[1, 0, 1],
            ....:                    [0, 0, 0],
            ....:                    [1, 0, 0]])
            sage: A.is_Gamma_free(certificate=True)
            (False, (0, 0, 2, 2))
            sage: B = Matrix(GF(2), [[1, 0, 1],
            ....:                    [0, 0, 0],
            ....:                    [1, 0, 1]])
            sage: B.is_Gamma_free(certificate=True)
            (True, None)"""
    @overload
    def randomize(self, density=..., nonzero=...) -> Any:
        """Matrix_mod2_dense.randomize(self, density=1, nonzero=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 1273)

        Randomize ``density`` proportion of the entries of this matrix,
        leaving the rest unchanged.

        INPUT:

        - ``density`` -- float; proportion (roughly) to be considered for
          changes
        - ``nonzero`` -- boolean (default: ``False``); whether the new entries
          are forced to be nonzero

        OUTPUT: None, the matrix is modified in-space

        EXAMPLES::

            sage: A = matrix(GF(2), 5, 5, 0)
            sage: A.randomize(0.5)
            sage: A.density() < 0.5
            True
            sage: expected = 0.5
            sage: A = matrix(GF(2), 5, 5, 0)
            sage: A.randomize()
            sage: density_sum = float(A.density())
            sage: total = 1
            sage: while abs(density_sum/total - expected) > 0.001:
            ....:     A = matrix(GF(2), 5, 5, 0)
            ....:     A.randomize()
            ....:     density_sum += float(A.density())
            ....:     total += 1

        TESTS:

        With the libc random number generator random(), we had problems
        where the ranks of all of these matrices would be the same
        (and they would all be far too low).  This verifies that the
        problem is gone, with Mersenne Twister::

            sage: MS2 = MatrixSpace(GF(2), 1000)
            sage: from collections import defaultdict
            sage: found = defaultdict(bool)
            sage: while not all(found[i] for i in range(997, 1001)):
            ....:     found[MS2.random_element().rank()] = True

        Testing corner case::

            sage: A = random_matrix(GF(2),3,0)
            sage: A
            []"""
    @overload
    def randomize(self) -> Any:
        """Matrix_mod2_dense.randomize(self, density=1, nonzero=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 1273)

        Randomize ``density`` proportion of the entries of this matrix,
        leaving the rest unchanged.

        INPUT:

        - ``density`` -- float; proportion (roughly) to be considered for
          changes
        - ``nonzero`` -- boolean (default: ``False``); whether the new entries
          are forced to be nonzero

        OUTPUT: None, the matrix is modified in-space

        EXAMPLES::

            sage: A = matrix(GF(2), 5, 5, 0)
            sage: A.randomize(0.5)
            sage: A.density() < 0.5
            True
            sage: expected = 0.5
            sage: A = matrix(GF(2), 5, 5, 0)
            sage: A.randomize()
            sage: density_sum = float(A.density())
            sage: total = 1
            sage: while abs(density_sum/total - expected) > 0.001:
            ....:     A = matrix(GF(2), 5, 5, 0)
            ....:     A.randomize()
            ....:     density_sum += float(A.density())
            ....:     total += 1

        TESTS:

        With the libc random number generator random(), we had problems
        where the ranks of all of these matrices would be the same
        (and they would all be far too low).  This verifies that the
        problem is gone, with Mersenne Twister::

            sage: MS2 = MatrixSpace(GF(2), 1000)
            sage: from collections import defaultdict
            sage: found = defaultdict(bool)
            sage: while not all(found[i] for i in range(997, 1001)):
            ....:     found[MS2.random_element().rank()] = True

        Testing corner case::

            sage: A = random_matrix(GF(2),3,0)
            sage: A
            []"""
    @overload
    def randomize(self) -> Any:
        """Matrix_mod2_dense.randomize(self, density=1, nonzero=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 1273)

        Randomize ``density`` proportion of the entries of this matrix,
        leaving the rest unchanged.

        INPUT:

        - ``density`` -- float; proportion (roughly) to be considered for
          changes
        - ``nonzero`` -- boolean (default: ``False``); whether the new entries
          are forced to be nonzero

        OUTPUT: None, the matrix is modified in-space

        EXAMPLES::

            sage: A = matrix(GF(2), 5, 5, 0)
            sage: A.randomize(0.5)
            sage: A.density() < 0.5
            True
            sage: expected = 0.5
            sage: A = matrix(GF(2), 5, 5, 0)
            sage: A.randomize()
            sage: density_sum = float(A.density())
            sage: total = 1
            sage: while abs(density_sum/total - expected) > 0.001:
            ....:     A = matrix(GF(2), 5, 5, 0)
            ....:     A.randomize()
            ....:     density_sum += float(A.density())
            ....:     total += 1

        TESTS:

        With the libc random number generator random(), we had problems
        where the ranks of all of these matrices would be the same
        (and they would all be far too low).  This verifies that the
        problem is gone, with Mersenne Twister::

            sage: MS2 = MatrixSpace(GF(2), 1000)
            sage: from collections import defaultdict
            sage: found = defaultdict(bool)
            sage: while not all(found[i] for i in range(997, 1001)):
            ....:     found[MS2.random_element().rank()] = True

        Testing corner case::

            sage: A = random_matrix(GF(2),3,0)
            sage: A
            []"""
    @overload
    def rank(self, algorithm=...) -> Any:
        '''Matrix_mod2_dense.rank(self, algorithm=\'ple\')

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 1977)

        Return the rank of this matrix.

        On average \'ple\' should be faster than \'m4ri\' and hence it is
        the default choice. However, for small - i.e. quite few
        thousand rows & columns - and sparse matrices \'m4ri\' might be
        a better choice.

        INPUT:

        - ``algorithm`` -- either "ple" or "m4ri"

        EXAMPLES::

            sage: while random_matrix(GF(2), 1000, 1000).rank() != 999:
            ....:     pass

            sage: A = matrix(GF(2),10, 0)
            sage: A.rank()
            0'''
    @overload
    def rank(self) -> Any:
        '''Matrix_mod2_dense.rank(self, algorithm=\'ple\')

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 1977)

        Return the rank of this matrix.

        On average \'ple\' should be faster than \'m4ri\' and hence it is
        the default choice. However, for small - i.e. quite few
        thousand rows & columns - and sparse matrices \'m4ri\' might be
        a better choice.

        INPUT:

        - ``algorithm`` -- either "ple" or "m4ri"

        EXAMPLES::

            sage: while random_matrix(GF(2), 1000, 1000).rank() != 999:
            ....:     pass

            sage: A = matrix(GF(2),10, 0)
            sage: A.rank()
            0'''
    @overload
    def rank(self) -> Any:
        '''Matrix_mod2_dense.rank(self, algorithm=\'ple\')

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 1977)

        Return the rank of this matrix.

        On average \'ple\' should be faster than \'m4ri\' and hence it is
        the default choice. However, for small - i.e. quite few
        thousand rows & columns - and sparse matrices \'m4ri\' might be
        a better choice.

        INPUT:

        - ``algorithm`` -- either "ple" or "m4ri"

        EXAMPLES::

            sage: while random_matrix(GF(2), 1000, 1000).rank() != 999:
            ....:     pass

            sage: A = matrix(GF(2),10, 0)
            sage: A.rank()
            0'''
    def row(self, Py_ssize_ti, from_list=...) -> Any:
        """Matrix_mod2_dense.row(self, Py_ssize_t i, from_list=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 535)

        Return the ``i``-th row of this matrix as a vector.

        This row is a dense vector if and only if the matrix is a dense
        matrix.

        INPUT:

        - ``i`` -- integer

        - ``from_list`` -- boolean (default: ``False``); if ``True``,
          returns the ``i``-th element of ``self.rows()`` (see
          :func:`rows`), which may be faster, but requires building a
          list of all rows the first time it is called after an entry
          of the matrix is changed.

        EXAMPLES::

            sage: l = [GF(2).random_element() for _ in range(100)]
            sage: A = matrix(GF(2), 10, 10 , l)
            sage: list(A.row(0)) == l[:10]
            True
            sage: list(A.row(-1)) == l[-10:]
            True

            sage: list(A.row(2, from_list=True)) == l[20:30]
            True

            sage: A = Matrix(GF(2),1,0)
            sage: A.row(0)
            ()"""
    @overload
    def str(self, rep_mapping=..., zero=..., plus_one=..., minus_one=..., unicode=..., shape=..., character_art=..., left_border=..., right_border=..., top_border=..., bottom_border=...) -> Any:
        """Matrix_mod2_dense.str(self, rep_mapping=None, zero=None, plus_one=None, minus_one=None, *, unicode=False, shape=None, character_art=False, left_border=None, right_border=None, top_border=None, bottom_border=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 403)

        Return a nice string representation of the matrix.

        INPUT:

        - ``rep_mapping`` -- dictionary or callable used to override
          the usual representation of elements.  For a dictionary,
          keys should be elements of the base ring and values the
          desired string representation.

        - ``zero`` -- string (default: ``None``); if not ``None`` use
          the value of ``zero`` as the representation of the zero
          element.

        - ``plus_one`` -- string (default: ``None``); if not ``None``
          use the value of ``plus_one`` as the representation of the
          one element.

        - ``minus_one`` -- ignored.  Only for compatibility with
          generic matrices.

        - ``unicode`` -- boolean (default: ``False``);
          whether to use Unicode symbols instead of ASCII symbols
          for brackets and subdivision lines

        - ``shape`` -- one of ``'square'`` or ``'round'`` (default: ``None``).
          Switches between round and square brackets.
          The default depends on the setting of the ``unicode`` keyword
          argument. For Unicode symbols, the default is round brackets
          in accordance with the TeX rendering,
          while the ASCII rendering defaults to square brackets.

        - ``character_art`` -- boolean (default: ``False``); if ``True``, the
          result will be of type :class:`~sage.typeset.ascii_art.AsciiArt` or
          :class:`~sage.typeset.unicode_art.UnicodeArt` which support line
          breaking of wide matrices that exceed the window width

        - ``left_border``, ``right_border`` -- sequence (default: ``None``);
          if not ``None``, call :func:`str` on the elements and use the
          results as labels for the rows of the matrix. The labels appear
          outside of the parentheses.

        - ``top_border``, ``bottom_border`` -- sequence (default: ``None``);
          if not ``None``, call :func:`str` on the elements and use the
          results as labels for the columns of the matrix. The labels appear
          outside of the parentheses.

        EXAMPLES::

            sage: B = matrix(GF(2), 3, 3, [0, 1, 0, 0, 1, 1, 0, 0, 0])
            sage: B  # indirect doctest
            [0 1 0]
            [0 1 1]
            [0 0 0]
            sage: block_matrix([[B, 1], [0, B]])
            [0 1 0|1 0 0]
            [0 1 1|0 1 0]
            [0 0 0|0 0 1]
            [-----+-----]
            [0 0 0|0 1 0]
            [0 0 0|0 1 1]
            [0 0 0|0 0 0]
            sage: B.str(zero='.')
            '[. 1 .]\\n[. 1 1]\\n[. . .]'

            sage: M = matrix.identity(GF(2), 3)
            sage: M.subdivide(None, 2)
            sage: print(M.str(unicode=True, shape='square'))
            ⎡1 0│0⎤
            ⎢0 1│0⎥
            ⎣0 0│1⎦
            sage: print(unicode_art(M))  # indirect doctest
            ⎛1 0│0⎞
            ⎜0 1│0⎟
            ⎝0 0│1⎠"""
    @overload
    def str(self, zero=...) -> Any:
        """Matrix_mod2_dense.str(self, rep_mapping=None, zero=None, plus_one=None, minus_one=None, *, unicode=False, shape=None, character_art=False, left_border=None, right_border=None, top_border=None, bottom_border=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 403)

        Return a nice string representation of the matrix.

        INPUT:

        - ``rep_mapping`` -- dictionary or callable used to override
          the usual representation of elements.  For a dictionary,
          keys should be elements of the base ring and values the
          desired string representation.

        - ``zero`` -- string (default: ``None``); if not ``None`` use
          the value of ``zero`` as the representation of the zero
          element.

        - ``plus_one`` -- string (default: ``None``); if not ``None``
          use the value of ``plus_one`` as the representation of the
          one element.

        - ``minus_one`` -- ignored.  Only for compatibility with
          generic matrices.

        - ``unicode`` -- boolean (default: ``False``);
          whether to use Unicode symbols instead of ASCII symbols
          for brackets and subdivision lines

        - ``shape`` -- one of ``'square'`` or ``'round'`` (default: ``None``).
          Switches between round and square brackets.
          The default depends on the setting of the ``unicode`` keyword
          argument. For Unicode symbols, the default is round brackets
          in accordance with the TeX rendering,
          while the ASCII rendering defaults to square brackets.

        - ``character_art`` -- boolean (default: ``False``); if ``True``, the
          result will be of type :class:`~sage.typeset.ascii_art.AsciiArt` or
          :class:`~sage.typeset.unicode_art.UnicodeArt` which support line
          breaking of wide matrices that exceed the window width

        - ``left_border``, ``right_border`` -- sequence (default: ``None``);
          if not ``None``, call :func:`str` on the elements and use the
          results as labels for the rows of the matrix. The labels appear
          outside of the parentheses.

        - ``top_border``, ``bottom_border`` -- sequence (default: ``None``);
          if not ``None``, call :func:`str` on the elements and use the
          results as labels for the columns of the matrix. The labels appear
          outside of the parentheses.

        EXAMPLES::

            sage: B = matrix(GF(2), 3, 3, [0, 1, 0, 0, 1, 1, 0, 0, 0])
            sage: B  # indirect doctest
            [0 1 0]
            [0 1 1]
            [0 0 0]
            sage: block_matrix([[B, 1], [0, B]])
            [0 1 0|1 0 0]
            [0 1 1|0 1 0]
            [0 0 0|0 0 1]
            [-----+-----]
            [0 0 0|0 1 0]
            [0 0 0|0 1 1]
            [0 0 0|0 0 0]
            sage: B.str(zero='.')
            '[. 1 .]\\n[. 1 1]\\n[. . .]'

            sage: M = matrix.identity(GF(2), 3)
            sage: M.subdivide(None, 2)
            sage: print(M.str(unicode=True, shape='square'))
            ⎡1 0│0⎤
            ⎢0 1│0⎥
            ⎣0 0│1⎦
            sage: print(unicode_art(M))  # indirect doctest
            ⎛1 0│0⎞
            ⎜0 1│0⎟
            ⎝0 0│1⎠"""
    @overload
    def str(self, unicode=..., shape=...) -> Any:
        """Matrix_mod2_dense.str(self, rep_mapping=None, zero=None, plus_one=None, minus_one=None, *, unicode=False, shape=None, character_art=False, left_border=None, right_border=None, top_border=None, bottom_border=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 403)

        Return a nice string representation of the matrix.

        INPUT:

        - ``rep_mapping`` -- dictionary or callable used to override
          the usual representation of elements.  For a dictionary,
          keys should be elements of the base ring and values the
          desired string representation.

        - ``zero`` -- string (default: ``None``); if not ``None`` use
          the value of ``zero`` as the representation of the zero
          element.

        - ``plus_one`` -- string (default: ``None``); if not ``None``
          use the value of ``plus_one`` as the representation of the
          one element.

        - ``minus_one`` -- ignored.  Only for compatibility with
          generic matrices.

        - ``unicode`` -- boolean (default: ``False``);
          whether to use Unicode symbols instead of ASCII symbols
          for brackets and subdivision lines

        - ``shape`` -- one of ``'square'`` or ``'round'`` (default: ``None``).
          Switches between round and square brackets.
          The default depends on the setting of the ``unicode`` keyword
          argument. For Unicode symbols, the default is round brackets
          in accordance with the TeX rendering,
          while the ASCII rendering defaults to square brackets.

        - ``character_art`` -- boolean (default: ``False``); if ``True``, the
          result will be of type :class:`~sage.typeset.ascii_art.AsciiArt` or
          :class:`~sage.typeset.unicode_art.UnicodeArt` which support line
          breaking of wide matrices that exceed the window width

        - ``left_border``, ``right_border`` -- sequence (default: ``None``);
          if not ``None``, call :func:`str` on the elements and use the
          results as labels for the rows of the matrix. The labels appear
          outside of the parentheses.

        - ``top_border``, ``bottom_border`` -- sequence (default: ``None``);
          if not ``None``, call :func:`str` on the elements and use the
          results as labels for the columns of the matrix. The labels appear
          outside of the parentheses.

        EXAMPLES::

            sage: B = matrix(GF(2), 3, 3, [0, 1, 0, 0, 1, 1, 0, 0, 0])
            sage: B  # indirect doctest
            [0 1 0]
            [0 1 1]
            [0 0 0]
            sage: block_matrix([[B, 1], [0, B]])
            [0 1 0|1 0 0]
            [0 1 1|0 1 0]
            [0 0 0|0 0 1]
            [-----+-----]
            [0 0 0|0 1 0]
            [0 0 0|0 1 1]
            [0 0 0|0 0 0]
            sage: B.str(zero='.')
            '[. 1 .]\\n[. 1 1]\\n[. . .]'

            sage: M = matrix.identity(GF(2), 3)
            sage: M.subdivide(None, 2)
            sage: print(M.str(unicode=True, shape='square'))
            ⎡1 0│0⎤
            ⎢0 1│0⎥
            ⎣0 0│1⎦
            sage: print(unicode_art(M))  # indirect doctest
            ⎛1 0│0⎞
            ⎜0 1│0⎟
            ⎝0 0│1⎠"""
    def submatrix(self, Py_ssize_trow=..., Py_ssize_tcol=..., Py_ssize_tnrows=..., Py_ssize_tncols=...) -> Any:
        """Matrix_mod2_dense.submatrix(self, Py_ssize_t row=0, Py_ssize_t col=0, Py_ssize_t nrows=-1, Py_ssize_t ncols=-1)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 1779)

        Return submatrix from the index row, col (inclusive) with
        dimension nrows x ncols.

        INPUT:

        - ``row`` -- index of start row
        - ``col`` -- index of start column
        - ``nrows`` -- number of rows of submatrix
        - ``ncols`` -- number of columns of submatrix

        EXAMPLES::

             sage: A = random_matrix(GF(2),200,200)
             sage: A[0:2,0:2] == A.submatrix(0,0,2,2)
             True
             sage: A[0:100,0:100] == A.submatrix(0,0,100,100)
             True
             sage: A == A.submatrix(0,0,200,200)
             True

             sage: A[1:3,1:3] == A.submatrix(1,1,2,2)
             True
             sage: A[1:100,1:100] == A.submatrix(1,1,99,99)
             True
             sage: A[1:200,1:200] == A.submatrix(1,1,199,199)
             True

        TESTS for handling of default arguments (:issue:`18761`)::

             sage: A.submatrix(17,15) == A.submatrix(17,15,183,185)
             True
             sage: A.submatrix(row=100,col=37,nrows=1,ncols=3) == A.submatrix(100,37,1,3)
             True"""
    @overload
    def transpose(self) -> Any:
        """Matrix_mod2_dense.transpose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 1496)

        Return transpose of ``self`` and leaves ``self`` untouched.

        EXAMPLES::

            sage: A = Matrix(GF(2),3,5,[1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0])
            sage: A
            [1 0 1 0 0]
            [0 1 1 0 0]
            [1 1 0 1 0]
            sage: B = A.transpose(); B
            [1 0 1]
            [0 1 1]
            [1 1 0]
            [0 0 1]
            [0 0 0]
            sage: B.transpose() == A
            True

        ``.T`` is a convenient shortcut for the transpose::

            sage: A.T
            [1 0 1]
            [0 1 1]
            [1 1 0]
            [0 0 1]
            [0 0 0]

        TESTS::

            sage: A = random_matrix(GF(2),0,40)
            sage: A.transpose()
            40 x 0 dense matrix over Finite Field of size 2 (use the '.str()' method to see the entries)

            sage: A = Matrix(GF(2), [1,0])
            sage: B = A.transpose()
            sage: A[0,0] = 0
            sage: B[0,0]
            1

            sage: m = matrix(GF(2),0,2)
            sage: m.subdivide([],[1])
            sage: m.subdivisions()
            ([], [1])
            sage: m.transpose().subdivisions()
            ([1], [])

            sage: m = matrix(GF(2),2,0)
            sage: m.subdivide([1],[])
            sage: m.subdivisions()
            ([1], [])
            sage: m.transpose().subdivisions()
            ([], [1])"""
    @overload
    def transpose(self) -> Any:
        """Matrix_mod2_dense.transpose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 1496)

        Return transpose of ``self`` and leaves ``self`` untouched.

        EXAMPLES::

            sage: A = Matrix(GF(2),3,5,[1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0])
            sage: A
            [1 0 1 0 0]
            [0 1 1 0 0]
            [1 1 0 1 0]
            sage: B = A.transpose(); B
            [1 0 1]
            [0 1 1]
            [1 1 0]
            [0 0 1]
            [0 0 0]
            sage: B.transpose() == A
            True

        ``.T`` is a convenient shortcut for the transpose::

            sage: A.T
            [1 0 1]
            [0 1 1]
            [1 1 0]
            [0 0 1]
            [0 0 0]

        TESTS::

            sage: A = random_matrix(GF(2),0,40)
            sage: A.transpose()
            40 x 0 dense matrix over Finite Field of size 2 (use the '.str()' method to see the entries)

            sage: A = Matrix(GF(2), [1,0])
            sage: B = A.transpose()
            sage: A[0,0] = 0
            sage: B[0,0]
            1

            sage: m = matrix(GF(2),0,2)
            sage: m.subdivide([],[1])
            sage: m.subdivisions()
            ([], [1])
            sage: m.transpose().subdivisions()
            ([1], [])

            sage: m = matrix(GF(2),2,0)
            sage: m.subdivide([1],[])
            sage: m.subdivisions()
            ([1], [])
            sage: m.transpose().subdivisions()
            ([], [1])"""
    @overload
    def transpose(self) -> Any:
        """Matrix_mod2_dense.transpose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 1496)

        Return transpose of ``self`` and leaves ``self`` untouched.

        EXAMPLES::

            sage: A = Matrix(GF(2),3,5,[1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0])
            sage: A
            [1 0 1 0 0]
            [0 1 1 0 0]
            [1 1 0 1 0]
            sage: B = A.transpose(); B
            [1 0 1]
            [0 1 1]
            [1 1 0]
            [0 0 1]
            [0 0 0]
            sage: B.transpose() == A
            True

        ``.T`` is a convenient shortcut for the transpose::

            sage: A.T
            [1 0 1]
            [0 1 1]
            [1 1 0]
            [0 0 1]
            [0 0 0]

        TESTS::

            sage: A = random_matrix(GF(2),0,40)
            sage: A.transpose()
            40 x 0 dense matrix over Finite Field of size 2 (use the '.str()' method to see the entries)

            sage: A = Matrix(GF(2), [1,0])
            sage: B = A.transpose()
            sage: A[0,0] = 0
            sage: B[0,0]
            1

            sage: m = matrix(GF(2),0,2)
            sage: m.subdivide([],[1])
            sage: m.subdivisions()
            ([], [1])
            sage: m.transpose().subdivisions()
            ([1], [])

            sage: m = matrix(GF(2),2,0)
            sage: m.subdivide([1],[])
            sage: m.subdivisions()
            ([1], [])
            sage: m.transpose().subdivisions()
            ([], [1])"""
    @overload
    def transpose(self) -> Any:
        """Matrix_mod2_dense.transpose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 1496)

        Return transpose of ``self`` and leaves ``self`` untouched.

        EXAMPLES::

            sage: A = Matrix(GF(2),3,5,[1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0])
            sage: A
            [1 0 1 0 0]
            [0 1 1 0 0]
            [1 1 0 1 0]
            sage: B = A.transpose(); B
            [1 0 1]
            [0 1 1]
            [1 1 0]
            [0 0 1]
            [0 0 0]
            sage: B.transpose() == A
            True

        ``.T`` is a convenient shortcut for the transpose::

            sage: A.T
            [1 0 1]
            [0 1 1]
            [1 1 0]
            [0 0 1]
            [0 0 0]

        TESTS::

            sage: A = random_matrix(GF(2),0,40)
            sage: A.transpose()
            40 x 0 dense matrix over Finite Field of size 2 (use the '.str()' method to see the entries)

            sage: A = Matrix(GF(2), [1,0])
            sage: B = A.transpose()
            sage: A[0,0] = 0
            sage: B[0,0]
            1

            sage: m = matrix(GF(2),0,2)
            sage: m.subdivide([],[1])
            sage: m.subdivisions()
            ([], [1])
            sage: m.transpose().subdivisions()
            ([1], [])

            sage: m = matrix(GF(2),2,0)
            sage: m.subdivide([1],[])
            sage: m.subdivisions()
            ([1], [])
            sage: m.transpose().subdivisions()
            ([], [1])"""
    @overload
    def transpose(self) -> Any:
        """Matrix_mod2_dense.transpose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 1496)

        Return transpose of ``self`` and leaves ``self`` untouched.

        EXAMPLES::

            sage: A = Matrix(GF(2),3,5,[1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0])
            sage: A
            [1 0 1 0 0]
            [0 1 1 0 0]
            [1 1 0 1 0]
            sage: B = A.transpose(); B
            [1 0 1]
            [0 1 1]
            [1 1 0]
            [0 0 1]
            [0 0 0]
            sage: B.transpose() == A
            True

        ``.T`` is a convenient shortcut for the transpose::

            sage: A.T
            [1 0 1]
            [0 1 1]
            [1 1 0]
            [0 0 1]
            [0 0 0]

        TESTS::

            sage: A = random_matrix(GF(2),0,40)
            sage: A.transpose()
            40 x 0 dense matrix over Finite Field of size 2 (use the '.str()' method to see the entries)

            sage: A = Matrix(GF(2), [1,0])
            sage: B = A.transpose()
            sage: A[0,0] = 0
            sage: B[0,0]
            1

            sage: m = matrix(GF(2),0,2)
            sage: m.subdivide([],[1])
            sage: m.subdivisions()
            ([], [1])
            sage: m.transpose().subdivisions()
            ([1], [])

            sage: m = matrix(GF(2),2,0)
            sage: m.subdivide([1],[])
            sage: m.subdivisions()
            ([1], [])
            sage: m.transpose().subdivisions()
            ([], [1])"""
    @overload
    def transpose(self) -> Any:
        """Matrix_mod2_dense.transpose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 1496)

        Return transpose of ``self`` and leaves ``self`` untouched.

        EXAMPLES::

            sage: A = Matrix(GF(2),3,5,[1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0])
            sage: A
            [1 0 1 0 0]
            [0 1 1 0 0]
            [1 1 0 1 0]
            sage: B = A.transpose(); B
            [1 0 1]
            [0 1 1]
            [1 1 0]
            [0 0 1]
            [0 0 0]
            sage: B.transpose() == A
            True

        ``.T`` is a convenient shortcut for the transpose::

            sage: A.T
            [1 0 1]
            [0 1 1]
            [1 1 0]
            [0 0 1]
            [0 0 0]

        TESTS::

            sage: A = random_matrix(GF(2),0,40)
            sage: A.transpose()
            40 x 0 dense matrix over Finite Field of size 2 (use the '.str()' method to see the entries)

            sage: A = Matrix(GF(2), [1,0])
            sage: B = A.transpose()
            sage: A[0,0] = 0
            sage: B[0,0]
            1

            sage: m = matrix(GF(2),0,2)
            sage: m.subdivide([],[1])
            sage: m.subdivisions()
            ([], [1])
            sage: m.transpose().subdivisions()
            ([1], [])

            sage: m = matrix(GF(2),2,0)
            sage: m.subdivide([1],[])
            sage: m.subdivisions()
            ([1], [])
            sage: m.transpose().subdivisions()
            ([], [1])"""
    @overload
    def transpose(self) -> Any:
        """Matrix_mod2_dense.transpose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 1496)

        Return transpose of ``self`` and leaves ``self`` untouched.

        EXAMPLES::

            sage: A = Matrix(GF(2),3,5,[1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0])
            sage: A
            [1 0 1 0 0]
            [0 1 1 0 0]
            [1 1 0 1 0]
            sage: B = A.transpose(); B
            [1 0 1]
            [0 1 1]
            [1 1 0]
            [0 0 1]
            [0 0 0]
            sage: B.transpose() == A
            True

        ``.T`` is a convenient shortcut for the transpose::

            sage: A.T
            [1 0 1]
            [0 1 1]
            [1 1 0]
            [0 0 1]
            [0 0 0]

        TESTS::

            sage: A = random_matrix(GF(2),0,40)
            sage: A.transpose()
            40 x 0 dense matrix over Finite Field of size 2 (use the '.str()' method to see the entries)

            sage: A = Matrix(GF(2), [1,0])
            sage: B = A.transpose()
            sage: A[0,0] = 0
            sage: B[0,0]
            1

            sage: m = matrix(GF(2),0,2)
            sage: m.subdivide([],[1])
            sage: m.subdivisions()
            ([], [1])
            sage: m.transpose().subdivisions()
            ([1], [])

            sage: m = matrix(GF(2),2,0)
            sage: m.subdivide([1],[])
            sage: m.subdivisions()
            ([1], [])
            sage: m.transpose().subdivisions()
            ([], [1])"""
    @overload
    def __copy__(self) -> Any:
        """Matrix_mod2_dense.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 1043)

        Return a copy of ``self``.

        EXAMPLES::

             sage: MS = MatrixSpace(GF(2),3,3)
             sage: A = MS(1)
             sage: A.__copy__() == A
             True
             sage: A.__copy__() is A
             False

             sage: A = random_matrix(GF(2),100,100)
             sage: A.__copy__() == A
             True
             sage: A.__copy__() is A
             False

             sage: A.echelonize()
             sage: A.__copy__() == A
             True"""
    @overload
    def __copy__(self) -> Any:
        """Matrix_mod2_dense.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 1043)

        Return a copy of ``self``.

        EXAMPLES::

             sage: MS = MatrixSpace(GF(2),3,3)
             sage: A = MS(1)
             sage: A.__copy__() == A
             True
             sage: A.__copy__() is A
             False

             sage: A = random_matrix(GF(2),100,100)
             sage: A.__copy__() == A
             True
             sage: A.__copy__() is A
             False

             sage: A.echelonize()
             sage: A.__copy__() == A
             True"""
    @overload
    def __copy__(self) -> Any:
        """Matrix_mod2_dense.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 1043)

        Return a copy of ``self``.

        EXAMPLES::

             sage: MS = MatrixSpace(GF(2),3,3)
             sage: A = MS(1)
             sage: A.__copy__() == A
             True
             sage: A.__copy__() is A
             False

             sage: A = random_matrix(GF(2),100,100)
             sage: A.__copy__() == A
             True
             sage: A.__copy__() is A
             False

             sage: A.echelonize()
             sage: A.__copy__() == A
             True"""
    @overload
    def __copy__(self) -> Any:
        """Matrix_mod2_dense.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 1043)

        Return a copy of ``self``.

        EXAMPLES::

             sage: MS = MatrixSpace(GF(2),3,3)
             sage: A = MS(1)
             sage: A.__copy__() == A
             True
             sage: A.__copy__() is A
             False

             sage: A = random_matrix(GF(2),100,100)
             sage: A.__copy__() == A
             True
             sage: A.__copy__() is A
             False

             sage: A.echelonize()
             sage: A.__copy__() == A
             True"""
    @overload
    def __copy__(self) -> Any:
        """Matrix_mod2_dense.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 1043)

        Return a copy of ``self``.

        EXAMPLES::

             sage: MS = MatrixSpace(GF(2),3,3)
             sage: A = MS(1)
             sage: A.__copy__() == A
             True
             sage: A.__copy__() is A
             False

             sage: A = random_matrix(GF(2),100,100)
             sage: A.__copy__() == A
             True
             sage: A.__copy__() is A
             False

             sage: A.echelonize()
             sage: A.__copy__() == A
             True"""
    @overload
    def __copy__(self) -> Any:
        """Matrix_mod2_dense.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 1043)

        Return a copy of ``self``.

        EXAMPLES::

             sage: MS = MatrixSpace(GF(2),3,3)
             sage: A = MS(1)
             sage: A.__copy__() == A
             True
             sage: A.__copy__() is A
             False

             sage: A = random_matrix(GF(2),100,100)
             sage: A.__copy__() == A
             True
             sage: A.__copy__() is A
             False

             sage: A.echelonize()
             sage: A.__copy__() == A
             True"""
    def __invert__(self) -> Any:
        """Matrix_mod2_dense.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 993)

        Invert ``self`` using the 'Method of the Four Russians'
        inversion.

        If ``self`` is not invertible a :exc:`ZeroDivisionError` is
        raised.

        EXAMPLES::

            sage: A = Matrix(GF(2),3,3, [0, 0, 1, 0, 1, 1, 1, 0, 1])
            sage: MS = A.parent()
            sage: A
            [0 0 1]
            [0 1 1]
            [1 0 1]
            sage: ~A
            [1 0 1]
            [1 1 0]
            [1 0 0]
            sage: A * ~A == ~A * A == MS(1)
            True

        TESTS::

            sage: A = matrix(GF(2),0,0)
            sage: A^(-1)
            []"""
    def __neg__(self) -> Any:
        """Matrix_mod2_dense.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 983)

        EXAMPLES::

            sage: A = random_matrix(GF(2),100,100)
            sage: A - A == A - -A
            True"""
    @overload
    def __reduce__(self) -> Any:
        """Matrix_mod2_dense.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 1851)

        Serialize ``self``.

        EXAMPLES::

            sage: A = random_matrix(GF(2),10,10)
            sage: f,s = A.__reduce__()
            sage: f(*s) == A
            True

        TESTS:

        Check that :issue:`24589` is fixed::

            sage: A = random_matrix(GF(2),10,10)
            sage: loads(dumps(A)).is_immutable()
            False
            sage: A.set_immutable()
            sage: loads(dumps(A)).is_immutable()
            True

        Check that :issue:`39367` is achieved::

            sage: l = len(dumps(random_matrix(GF(2), 2000, 2000))); l  # random   # previously ~ 785000
            610207
            sage: assert l < 650000"""
    @overload
    def __reduce__(self) -> Any:
        """Matrix_mod2_dense.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mod2_dense.pyx (starting at line 1851)

        Serialize ``self``.

        EXAMPLES::

            sage: A = random_matrix(GF(2),10,10)
            sage: f,s = A.__reduce__()
            sage: f(*s) == A
            True

        TESTS:

        Check that :issue:`24589` is fixed::

            sage: A = random_matrix(GF(2),10,10)
            sage: loads(dumps(A)).is_immutable()
            False
            sage: A.set_immutable()
            sage: loads(dumps(A)).is_immutable()
            True

        Check that :issue:`39367` is achieved::

            sage: l = len(dumps(random_matrix(GF(2), 2000, 2000))); l  # random   # previously ~ 785000
            610207
            sage: assert l < 650000"""
