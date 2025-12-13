import sage as sage
import sage.matrix.matrix_sparse
from sage.categories.category import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

class Matrix_rational_sparse(sage.matrix.matrix_sparse.Matrix_sparse):
    """Matrix_rational_sparse(parent, entries=None, copy=None, bool coerce=True)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, entries=..., copy=..., boolcoerce=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_sparse.pyx (starting at line 73)

                Create a sparse matrix over the rational numbers.

                INPUT:

                - ``parent`` -- a matrix space over `\\QQ`

                - ``entries`` -- see :func:`matrix`

                - ``copy`` -- ignored (for backwards compatibility)

                - ``coerce`` -- if ``False``, assume without checking that the
                  entries are of type :class:`Rational`
        """
    def add_to_entry(self, Py_ssize_ti, Py_ssize_tj, elt) -> Any:
        """Matrix_rational_sparse.add_to_entry(self, Py_ssize_t i, Py_ssize_t j, elt)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_sparse.pyx (starting at line 161)

        Add ``elt`` to the entry at position ``(i, j)``.

        EXAMPLES::

            sage: m = matrix(QQ, 2, 2, sparse=True)
            sage: m.add_to_entry(0, 0, -1/3)
            sage: m
            [-1/3    0]
            [   0    0]
            sage: m.add_to_entry(0, 0, 1/3)
            sage: m
            [0 0]
            [0 0]
            sage: m.nonzero_positions()
            []"""
    @overload
    def denominator(self) -> Any:
        """Matrix_rational_sparse.denominator(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_sparse.pyx (starting at line 449)

        Return the denominator of this matrix.

        OUTPUT: Sage Integer

        EXAMPLES::

            sage: b = matrix(QQ,2,range(6)); b[0,0]=-5007/293; b
            [-5007/293         1         2]
            [        3         4         5]
            sage: b.denominator()
            293"""
    @overload
    def denominator(self) -> Any:
        """Matrix_rational_sparse.denominator(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_sparse.pyx (starting at line 449)

        Return the denominator of this matrix.

        OUTPUT: Sage Integer

        EXAMPLES::

            sage: b = matrix(QQ,2,range(6)); b[0,0]=-5007/293; b
            [-5007/293         1         2]
            [        3         4         5]
            sage: b.denominator()
            293"""
    @overload
    def dense_matrix(self) -> Any:
        """Matrix_rational_sparse.dense_matrix(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_sparse.pyx (starting at line 642)

        Return dense version of this matrix.

        EXAMPLES::

            sage: a = matrix(QQ,2,[1..4],sparse=True); type(a)
            <class 'sage.matrix.matrix_rational_sparse.Matrix_rational_sparse'>
            sage: type(a.dense_matrix())
            <class 'sage.matrix.matrix_rational_dense.Matrix_rational_dense'>
            sage: a.dense_matrix()
            [1 2]
            [3 4]

        Check that subdivisions are preserved when converting between
        dense and sparse matrices::

            sage: a.subdivide([1,1], [2])
            sage: b = a.dense_matrix().sparse_matrix().dense_matrix()
            sage: b.subdivisions() == a.subdivisions()
            True"""
    @overload
    def dense_matrix(self) -> Any:
        """Matrix_rational_sparse.dense_matrix(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_sparse.pyx (starting at line 642)

        Return dense version of this matrix.

        EXAMPLES::

            sage: a = matrix(QQ,2,[1..4],sparse=True); type(a)
            <class 'sage.matrix.matrix_rational_sparse.Matrix_rational_sparse'>
            sage: type(a.dense_matrix())
            <class 'sage.matrix.matrix_rational_dense.Matrix_rational_dense'>
            sage: a.dense_matrix()
            [1 2]
            [3 4]

        Check that subdivisions are preserved when converting between
        dense and sparse matrices::

            sage: a.subdivide([1,1], [2])
            sage: b = a.dense_matrix().sparse_matrix().dense_matrix()
            sage: b.subdivisions() == a.subdivisions()
            True"""
    @overload
    def dense_matrix(self) -> Any:
        """Matrix_rational_sparse.dense_matrix(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_sparse.pyx (starting at line 642)

        Return dense version of this matrix.

        EXAMPLES::

            sage: a = matrix(QQ,2,[1..4],sparse=True); type(a)
            <class 'sage.matrix.matrix_rational_sparse.Matrix_rational_sparse'>
            sage: type(a.dense_matrix())
            <class 'sage.matrix.matrix_rational_dense.Matrix_rational_dense'>
            sage: a.dense_matrix()
            [1 2]
            [3 4]

        Check that subdivisions are preserved when converting between
        dense and sparse matrices::

            sage: a.subdivide([1,1], [2])
            sage: b = a.dense_matrix().sparse_matrix().dense_matrix()
            sage: b.subdivisions() == a.subdivisions()
            True"""
    @overload
    def dense_matrix(self) -> Any:
        """Matrix_rational_sparse.dense_matrix(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_sparse.pyx (starting at line 642)

        Return dense version of this matrix.

        EXAMPLES::

            sage: a = matrix(QQ,2,[1..4],sparse=True); type(a)
            <class 'sage.matrix.matrix_rational_sparse.Matrix_rational_sparse'>
            sage: type(a.dense_matrix())
            <class 'sage.matrix.matrix_rational_dense.Matrix_rational_dense'>
            sage: a.dense_matrix()
            [1 2]
            [3 4]

        Check that subdivisions are preserved when converting between
        dense and sparse matrices::

            sage: a.subdivide([1,1], [2])
            sage: b = a.dense_matrix().sparse_matrix().dense_matrix()
            sage: b.subdivisions() == a.subdivisions()
            True"""
    @overload
    def echelon_form(self, algorithm=..., height_guess=..., proof=..., **kwds) -> Any:
        """Matrix_rational_sparse.echelon_form(self, algorithm='default', height_guess=None, proof=True, **kwds)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_sparse.pyx (starting at line 561)

        INPUT:

        - ``height_guess``, ``proof``, ``**kwds`` -- all passed to the multimodular
          algorithm; ignored by the `p`-adic algorithm

        OUTPUT: ``self`` is no in reduced row echelon form

        EXAMPLES::

            sage: a = matrix(QQ, 4, range(16), sparse=True); a[0,0] = 1/19; a[0,1] = 1/5; a
            [1/19  1/5    2    3]
            [   4    5    6    7]
            [   8    9   10   11]
            [  12   13   14   15]
            sage: a.echelon_form()
            [      1       0       0 -76/157]
            [      0       1       0  -5/157]
            [      0       0       1 238/157]
            [      0       0       0       0]"""
    @overload
    def echelon_form(self) -> Any:
        """Matrix_rational_sparse.echelon_form(self, algorithm='default', height_guess=None, proof=True, **kwds)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_sparse.pyx (starting at line 561)

        INPUT:

        - ``height_guess``, ``proof``, ``**kwds`` -- all passed to the multimodular
          algorithm; ignored by the `p`-adic algorithm

        OUTPUT: ``self`` is no in reduced row echelon form

        EXAMPLES::

            sage: a = matrix(QQ, 4, range(16), sparse=True); a[0,0] = 1/19; a[0,1] = 1/5; a
            [1/19  1/5    2    3]
            [   4    5    6    7]
            [   8    9   10   11]
            [  12   13   14   15]
            sage: a.echelon_form()
            [      1       0       0 -76/157]
            [      0       1       0  -5/157]
            [      0       0       1 238/157]
            [      0       0       0       0]"""
    @overload
    def echelonize(self, height_guess=..., proof=..., **kwds) -> Any:
        """Matrix_rational_sparse.echelonize(self, height_guess=None, proof=True, **kwds)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_sparse.pyx (starting at line 512)

        Transform the matrix ``self`` into reduced row echelon form
        in place.

        INPUT:

        - ``height_guess``, ``proof``, ``**kwds`` -- all passed to the multimodular
          algorithm; ignored by the `p`-adic algorithm

        OUTPUT:

        Nothing. The matrix ``self`` is transformed into reduced row
        echelon form in place.

        ALGORITHM: a multimodular algorithm.

        EXAMPLES::

            sage: a = matrix(QQ, 4, range(16), sparse=True); a[0,0] = 1/19; a[0,1] = 1/5; a
            [1/19  1/5    2    3]
            [   4    5    6    7]
            [   8    9   10   11]
            [  12   13   14   15]
            sage: a.echelonize(); a
            [      1       0       0 -76/157]
            [      0       1       0  -5/157]
            [      0       0       1 238/157]
            [      0       0       0       0]

        :issue:`10319` has been fixed::

            sage: m = Matrix(QQ, [1], sparse=True); m.echelonize()
            sage: m = Matrix(QQ, [1], sparse=True); m.echelonize(); m
            [1]"""
    @overload
    def echelonize(self) -> Any:
        """Matrix_rational_sparse.echelonize(self, height_guess=None, proof=True, **kwds)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_sparse.pyx (starting at line 512)

        Transform the matrix ``self`` into reduced row echelon form
        in place.

        INPUT:

        - ``height_guess``, ``proof``, ``**kwds`` -- all passed to the multimodular
          algorithm; ignored by the `p`-adic algorithm

        OUTPUT:

        Nothing. The matrix ``self`` is transformed into reduced row
        echelon form in place.

        ALGORITHM: a multimodular algorithm.

        EXAMPLES::

            sage: a = matrix(QQ, 4, range(16), sparse=True); a[0,0] = 1/19; a[0,1] = 1/5; a
            [1/19  1/5    2    3]
            [   4    5    6    7]
            [   8    9   10   11]
            [  12   13   14   15]
            sage: a.echelonize(); a
            [      1       0       0 -76/157]
            [      0       1       0  -5/157]
            [      0       0       1 238/157]
            [      0       0       0       0]

        :issue:`10319` has been fixed::

            sage: m = Matrix(QQ, [1], sparse=True); m.echelonize()
            sage: m = Matrix(QQ, [1], sparse=True); m.echelonize(); m
            [1]"""
    @overload
    def echelonize(self) -> Any:
        """Matrix_rational_sparse.echelonize(self, height_guess=None, proof=True, **kwds)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_sparse.pyx (starting at line 512)

        Transform the matrix ``self`` into reduced row echelon form
        in place.

        INPUT:

        - ``height_guess``, ``proof``, ``**kwds`` -- all passed to the multimodular
          algorithm; ignored by the `p`-adic algorithm

        OUTPUT:

        Nothing. The matrix ``self`` is transformed into reduced row
        echelon form in place.

        ALGORITHM: a multimodular algorithm.

        EXAMPLES::

            sage: a = matrix(QQ, 4, range(16), sparse=True); a[0,0] = 1/19; a[0,1] = 1/5; a
            [1/19  1/5    2    3]
            [   4    5    6    7]
            [   8    9   10   11]
            [  12   13   14   15]
            sage: a.echelonize(); a
            [      1       0       0 -76/157]
            [      0       1       0  -5/157]
            [      0       0       1 238/157]
            [      0       0       0       0]

        :issue:`10319` has been fixed::

            sage: m = Matrix(QQ, [1], sparse=True); m.echelonize()
            sage: m = Matrix(QQ, [1], sparse=True); m.echelonize(); m
            [1]"""
    @overload
    def echelonize(self) -> Any:
        """Matrix_rational_sparse.echelonize(self, height_guess=None, proof=True, **kwds)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_sparse.pyx (starting at line 512)

        Transform the matrix ``self`` into reduced row echelon form
        in place.

        INPUT:

        - ``height_guess``, ``proof``, ``**kwds`` -- all passed to the multimodular
          algorithm; ignored by the `p`-adic algorithm

        OUTPUT:

        Nothing. The matrix ``self`` is transformed into reduced row
        echelon form in place.

        ALGORITHM: a multimodular algorithm.

        EXAMPLES::

            sage: a = matrix(QQ, 4, range(16), sparse=True); a[0,0] = 1/19; a[0,1] = 1/5; a
            [1/19  1/5    2    3]
            [   4    5    6    7]
            [   8    9   10   11]
            [  12   13   14   15]
            sage: a.echelonize(); a
            [      1       0       0 -76/157]
            [      0       1       0  -5/157]
            [      0       0       1 238/157]
            [      0       0       0       0]

        :issue:`10319` has been fixed::

            sage: m = Matrix(QQ, [1], sparse=True); m.echelonize()
            sage: m = Matrix(QQ, [1], sparse=True); m.echelonize(); m
            [1]"""
    @overload
    def height(self) -> Any:
        """Matrix_rational_sparse.height(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_sparse.pyx (starting at line 396)

        Return the height of this matrix, which is the least common
        multiple of all numerators and denominators of elements of
        this matrix.

        OUTPUT: integer

        EXAMPLES::

            sage: b = matrix(QQ,2,range(6), sparse=True); b[0,0]=-5007/293; b
            [-5007/293         1         2]
            [        3         4         5]
            sage: b.height()
            5007"""
    @overload
    def height(self) -> Any:
        """Matrix_rational_sparse.height(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_sparse.pyx (starting at line 396)

        Return the height of this matrix, which is the least common
        multiple of all numerators and denominators of elements of
        this matrix.

        OUTPUT: integer

        EXAMPLES::

            sage: b = matrix(QQ,2,range(6), sparse=True); b[0,0]=-5007/293; b
            [-5007/293         1         2]
            [        3         4         5]
            sage: b.height()
            5007"""
    def set_row_to_multiple_of_row(self, i, j, s) -> Any:
        """Matrix_rational_sparse.set_row_to_multiple_of_row(self, i, j, s)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_sparse.pyx (starting at line 623)

        Set row i equal to s times row j.

        EXAMPLES::

            sage: a = matrix(QQ,2,3,range(6), sparse=True); a
            [0 1 2]
            [3 4 5]
            sage: a.set_row_to_multiple_of_row(1,0,-3)
            sage: a
            [ 0  1  2]
            [ 0 -3 -6]"""
