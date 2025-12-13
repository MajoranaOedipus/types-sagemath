from sage.categories.category import ZZ as ZZ
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

class Matrix:
    """File: /build/sagemath/src/sage/src/sage/libs/eclib/mat.pyx (starting at line 14)

        A Cremona Matrix.

        EXAMPLES::

            sage: M = CremonaModularSymbols(225)
            sage: t = M.hecke_matrix(2)
            sage: type(t)
            <class 'sage.libs.eclib.mat.Matrix'>
            sage: t
            61 x 61 Cremona matrix over Rational Field

        TESTS::

            sage: t = CremonaModularSymbols(11).hecke_matrix(2); t
            3 x 3 Cremona matrix over Rational Field
            sage: type(t)
            <class 'sage.libs.eclib.mat.Matrix'>
    """
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def add_scalar(self, scalars) -> Any:
        """Matrix.add_scalar(self, scalar s)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mat.pyx (starting at line 151)

        Return new matrix obtained by adding `s` to each diagonal entry of ``self``.

        EXAMPLES::

            sage: M = CremonaModularSymbols(23, cuspidal=True, sign=1)
            sage: t = M.hecke_matrix(2); print(t.str())
            [ 0  1]
            [ 1 -1]
            sage: w = t.add_scalar(3); print(w.str())
            [3 1]
            [1 2]"""
    def charpoly(self, var=...) -> Any:
        """Matrix.charpoly(self, var='x')

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mat.pyx (starting at line 167)

        Return the characteristic polynomial of this matrix, viewed as
        as a matrix over the integers.

        ALGORITHM:

        Note that currently, this function converts this matrix into a
        dense matrix over the integers, then calls the charpoly
        algorithm on that, which I think is LinBox's.

        EXAMPLES::

            sage: M = CremonaModularSymbols(33, cuspidal=True, sign=1)
            sage: t = M.hecke_matrix(2)
            sage: t.charpoly()
            x^3 + 3*x^2 - 4
            sage: t.charpoly().factor()
            (x - 1) * (x + 2)^2"""
    @overload
    def ncols(self) -> Any:
        """Matrix.ncols(self)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mat.pyx (starting at line 113)

        Return the number of columns of this matrix.

        EXAMPLES::

            sage: M = CremonaModularSymbols(1234, sign=1)
            sage: t = M.hecke_matrix(3); t.ncols()
            156
            sage: M.dimension()
            156"""
    @overload
    def ncols(self) -> Any:
        """Matrix.ncols(self)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mat.pyx (starting at line 113)

        Return the number of columns of this matrix.

        EXAMPLES::

            sage: M = CremonaModularSymbols(1234, sign=1)
            sage: t = M.hecke_matrix(3); t.ncols()
            156
            sage: M.dimension()
            156"""
    @overload
    def nrows(self) -> Any:
        """Matrix.nrows(self)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mat.pyx (starting at line 99)

        Return the number of rows of this matrix.

        EXAMPLES::

            sage: M = CremonaModularSymbols(19, sign=1)
            sage: t = M.hecke_matrix(13); t
            2 x 2 Cremona matrix over Rational Field
            sage: t.nrows()
            2"""
    @overload
    def nrows(self) -> Any:
        """Matrix.nrows(self)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mat.pyx (starting at line 99)

        Return the number of rows of this matrix.

        EXAMPLES::

            sage: M = CremonaModularSymbols(19, sign=1)
            sage: t = M.hecke_matrix(13); t
            2 x 2 Cremona matrix over Rational Field
            sage: t.nrows()
            2"""
    @overload
    def sage_matrix_over_ZZ(self, sparse=...) -> Any:
        """Matrix.sage_matrix_over_ZZ(self, sparse=True)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mat.pyx (starting at line 189)

        Return corresponding Sage matrix over the integers.

        INPUT:

        - ``sparse`` -- boolean (default: ``True``); whether the return matrix has
          a sparse representation

        EXAMPLES::

            sage: M = CremonaModularSymbols(23, cuspidal=True, sign=1)
            sage: t = M.hecke_matrix(2)
            sage: s = t.sage_matrix_over_ZZ(); s
            [ 0  1]
            [ 1 -1]
            sage: type(s)
            <class 'sage.matrix.matrix_integer_sparse.Matrix_integer_sparse'>
            sage: s = t.sage_matrix_over_ZZ(sparse=False); s
            [ 0  1]
            [ 1 -1]
            sage: type(s)
            <class 'sage.matrix.matrix_integer_dense.Matrix_integer_dense'>"""
    @overload
    def sage_matrix_over_ZZ(self) -> Any:
        """Matrix.sage_matrix_over_ZZ(self, sparse=True)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mat.pyx (starting at line 189)

        Return corresponding Sage matrix over the integers.

        INPUT:

        - ``sparse`` -- boolean (default: ``True``); whether the return matrix has
          a sparse representation

        EXAMPLES::

            sage: M = CremonaModularSymbols(23, cuspidal=True, sign=1)
            sage: t = M.hecke_matrix(2)
            sage: s = t.sage_matrix_over_ZZ(); s
            [ 0  1]
            [ 1 -1]
            sage: type(s)
            <class 'sage.matrix.matrix_integer_sparse.Matrix_integer_sparse'>
            sage: s = t.sage_matrix_over_ZZ(sparse=False); s
            [ 0  1]
            [ 1 -1]
            sage: type(s)
            <class 'sage.matrix.matrix_integer_dense.Matrix_integer_dense'>"""
    @overload
    def sage_matrix_over_ZZ(self, sparse=...) -> Any:
        """Matrix.sage_matrix_over_ZZ(self, sparse=True)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mat.pyx (starting at line 189)

        Return corresponding Sage matrix over the integers.

        INPUT:

        - ``sparse`` -- boolean (default: ``True``); whether the return matrix has
          a sparse representation

        EXAMPLES::

            sage: M = CremonaModularSymbols(23, cuspidal=True, sign=1)
            sage: t = M.hecke_matrix(2)
            sage: s = t.sage_matrix_over_ZZ(); s
            [ 0  1]
            [ 1 -1]
            sage: type(s)
            <class 'sage.matrix.matrix_integer_sparse.Matrix_integer_sparse'>
            sage: s = t.sage_matrix_over_ZZ(sparse=False); s
            [ 0  1]
            [ 1 -1]
            sage: type(s)
            <class 'sage.matrix.matrix_integer_dense.Matrix_integer_dense'>"""
    @overload
    def str(self) -> Any:
        """Matrix.str(self)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mat.pyx (starting at line 53)

        Return full string representation of this matrix, never in compact form.

        EXAMPLES::

            sage: M = CremonaModularSymbols(22, sign=1)
            sage: t = M.hecke_matrix(13)
            sage: t.str()
            '[14  0  0  0  0]\\n[-4 12  0  8  4]\\n[ 0 -6  4 -6  0]\\n[ 4  2  0  6 -4]\\n[ 0  0  0  0 14]'"""
    @overload
    def str(self) -> Any:
        """Matrix.str(self)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mat.pyx (starting at line 53)

        Return full string representation of this matrix, never in compact form.

        EXAMPLES::

            sage: M = CremonaModularSymbols(22, sign=1)
            sage: t = M.hecke_matrix(13)
            sage: t.str()
            '[14  0  0  0  0]\\n[-4 12  0  8  4]\\n[ 0 -6  4 -6  0]\\n[ 4  2  0  6 -4]\\n[ 0  0  0  0 14]'"""
    def __getitem__(self, ij) -> Any:
        """Matrix.__getitem__(self, ij)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/mat.pyx (starting at line 69)

        Return the (i,j) entry of this matrix.

        Here, ij is a 2-tuple (i,j) and the row and column indices start
        at 1 and not 0.

        EXAMPLES::

            sage: M = CremonaModularSymbols(19, sign=1)
            sage: t = M.hecke_matrix(13); t
            2 x 2 Cremona matrix over Rational Field
            sage: t.sage_matrix_over_ZZ()
            [ 28   0]
            [-12  -8]
            sage: [[t.__getitem__((i,j)) for j in [1,2]] for i in [1,2]]
            [[28, 0], [-12, -8]]
            sage: t.__getitem__((0,0))
            Traceback (most recent call last):
            ...
            IndexError: matrix indices out of range"""

class MatrixFactory:
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
