import sage.matrix.matrix_double_dense
from sage.categories.category import CDF as CDF
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import ClassVar

numpy: None

class Matrix_complex_double_dense(sage.matrix.matrix_double_dense.Matrix_double_dense):
    """File: /build/sagemath/src/sage/src/sage/matrix/matrix_complex_double_dense.pyx (starting at line 48)

        Class that implements matrices over the real double field. These
        are supposed to be fast matrix operations using C doubles. Most
        operations are implemented using numpy which will call the
        underlying BLAS on the system.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: m = Matrix(CDF, [[1,2*I],[3+I,4]])
            sage: m**2
            [-1.0 + 6.0*I       10.0*I]
            [15.0 + 5.0*I 14.0 + 6.0*I]
            sage: n= m^(-1); n  # abs tol 1e-15
            [  0.3333333333333333 + 0.3333333333333333*I 0.16666666666666669 - 0.16666666666666666*I]
            [-0.16666666666666666 - 0.3333333333333333*I 0.08333333333333331 + 0.08333333333333333*I]

        To compute eigenvalues, use the methods
        :meth:`~.Matrix_double_dense.left_eigenvectors` or
        :meth:`~.Matrix_double_dense.right_eigenvectors`::

            sage: p,e = m.right_eigenvectors()                                              # needs sage.symbolic

        The result is a pair ``(p,e)``, where ``p`` is a diagonal matrix of
        eigenvalues and ``e`` is a matrix whose columns are the
        eigenvectors.

        To solve a linear system `Ax = b` where ``A = [[1,2*I],[3+I,4]]`` and
        ``b = [5,6]``::

            sage: b = vector(CDF,[5,6])                                                     # needs sage.symbolic
            sage: m.solve_right(b)  # abs tol 1e-14                                         # needs sage.symbolic
            (2.6666666666666665 + 0.6666666666666669*I, -0.3333333333333333 - 1.1666666666666667*I)

        See the methods :meth:`~.Matrix_double_dense.QR`,
        :meth:`~.Matrix_double_dense.LU`, and :meth:`.SVD` for QR, LU, and singular
        value decomposition.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
