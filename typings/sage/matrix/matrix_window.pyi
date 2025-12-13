from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar

class MatrixWindow:
    """MatrixWindow(Matrix matrix, Py_ssize_t row, Py_ssize_t col, Py_ssize_t nrows, Py_ssize_t ncols)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, Matrixmatrix, Py_ssize_trow, Py_ssize_tcol, Py_ssize_tnrows, Py_ssize_tncols) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matrix/matrix_window.pyx (starting at line 42)"""
    def add(self, MatrixWindowA) -> Any:
        """MatrixWindow.add(self, MatrixWindow A)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_window.pyx (starting at line 163)"""
    def add_prod(self, MatrixWindowA, MatrixWindowB) -> Any:
        """MatrixWindow.add_prod(self, MatrixWindow A, MatrixWindow B)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_window.pyx (starting at line 206)"""
    def echelon_in_place(self) -> Any:
        """MatrixWindow.echelon_in_place(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_window.pyx (starting at line 231)

        Calculate the echelon form of this matrix, returning the list of pivot columns"""
    def element_is_zero(self, Py_ssize_ti, Py_ssize_tj) -> bool:
        """MatrixWindow.element_is_zero(self, Py_ssize_t i, Py_ssize_t j) -> bool

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_window.pyx (starting at line 240)"""
    def get_unsafe(self, Py_ssize_ti, Py_ssize_tj) -> Any:
        """MatrixWindow.get_unsafe(self, Py_ssize_t i, Py_ssize_t j)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_window.pyx (starting at line 85)"""
    def matrix(self) -> Any:
        """MatrixWindow.matrix(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_window.pyx (starting at line 122)

        Return the underlying matrix that this window is a view of."""
    def matrix_window(self, Py_ssize_trow, Py_ssize_tcol, Py_ssize_tn_rows, Py_ssize_tn_cols) -> MatrixWindow:
        """MatrixWindow.matrix_window(self, Py_ssize_t row, Py_ssize_t col, Py_ssize_t n_rows, Py_ssize_t n_cols) -> MatrixWindow

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_window.pyx (starting at line 55)

        Return a matrix window relative to this window of the
        underlying matrix."""
    def ncols(self) -> Any:
        """MatrixWindow.ncols(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_window.pyx (starting at line 141)"""
    def new_empty_window(self, Py_ssize_tnrows, Py_ssize_tncols) -> Any:
        """MatrixWindow.new_empty_window(self, Py_ssize_t nrows, Py_ssize_t ncols)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_window.pyx (starting at line 65)"""
    def new_matrix_window(self, Matrixmatrix, Py_ssize_trow, Py_ssize_tcol, Py_ssize_tn_rows, Py_ssize_tn_cols) -> MatrixWindow:
        """MatrixWindow.new_matrix_window(self, Matrix matrix, Py_ssize_t row, Py_ssize_t col, Py_ssize_t n_rows, Py_ssize_t n_cols) -> MatrixWindow

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_window.pyx (starting at line 23)

        This method is here only to provide a fast cdef way of
        constructing new matrix windows. The only implicit assumption
        is that self._matrix and matrix are over the same base ring
        (so share the zero)."""
    def nrows(self) -> Any:
        """MatrixWindow.nrows(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_window.pyx (starting at line 138)"""
    def set(self, MatrixWindowsrc) -> Any:
        """MatrixWindow.set(self, MatrixWindow src)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_window.pyx (starting at line 77)"""
    def set_to(self, MatrixWindowA) -> Any:
        """MatrixWindow.set_to(self, MatrixWindow A)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_window.pyx (starting at line 144)

        Change self, making it equal A."""
    def set_to_diff(self, MatrixWindowA, MatrixWindowB) -> Any:
        """MatrixWindow.set_to_diff(self, MatrixWindow A, MatrixWindow B)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_window.pyx (starting at line 189)"""
    def set_to_prod(self, MatrixWindowA, MatrixWindowB) -> Any:
        """MatrixWindow.set_to_prod(self, MatrixWindow A, MatrixWindow B)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_window.pyx (starting at line 195)"""
    def set_to_sum(self, MatrixWindowA, MatrixWindowB) -> Any:
        """MatrixWindow.set_to_sum(self, MatrixWindow A, MatrixWindow B)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_window.pyx (starting at line 179)"""
    def set_to_zero(self) -> Any:
        """MatrixWindow.set_to_zero(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_window.pyx (starting at line 156)"""
    def set_unsafe(self, Py_ssize_ti, Py_ssize_tj, x) -> Any:
        """MatrixWindow.set_unsafe(self, Py_ssize_t i, Py_ssize_t j, x)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_window.pyx (starting at line 82)"""
    def subtract(self, MatrixWindowA) -> Any:
        """MatrixWindow.subtract(self, MatrixWindow A)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_window.pyx (starting at line 171)"""
    def subtract_prod(self, MatrixWindowA, MatrixWindowB) -> Any:
        """MatrixWindow.subtract_prod(self, MatrixWindow A, MatrixWindow B)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_window.pyx (starting at line 217)"""
    def swap_rows(self, Py_ssize_ta, Py_ssize_tb) -> Any:
        """MatrixWindow.swap_rows(self, Py_ssize_t a, Py_ssize_t b)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_window.pyx (starting at line 228)"""
    def to_matrix(self) -> Any:
        """MatrixWindow.to_matrix(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_window.pyx (starting at line 128)

        Return an actual matrix object representing this view."""
    def __delitem__(self, other) -> None:
        """Delete self[key]."""
    def __getitem__(self, ij) -> Any:
        """MatrixWindow.__getitem__(self, ij)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_window.pyx (starting at line 105)"""
    def __setitem__(self, ij, x) -> Any:
        """MatrixWindow.__setitem__(self, ij, x)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_window.pyx (starting at line 88)"""
