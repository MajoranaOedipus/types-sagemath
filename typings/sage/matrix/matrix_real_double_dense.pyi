import sage.matrix.matrix_double_dense
from sage.categories.category import RDF as RDF
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import ClassVar

numpy: None
scipy: None

class Matrix_real_double_dense(sage.matrix.matrix_double_dense.Matrix_double_dense):
    """File: /build/sagemath/src/sage/src/sage/matrix/matrix_real_double_dense.pyx (starting at line 50)

        Class that implements matrices over the real double field. These
        are supposed to be fast matrix operations using C doubles. Most
        operations are implemented using numpy which will call the
        underlying BLAS on the system.

        EXAMPLES::

            sage: m = Matrix(RDF, [[1,2],[3,4]])
            sage: m**2
            [ 7.0 10.0]
            [15.0 22.0]
            sage: n = m^(-1); n     # rel tol 1e-15                                         # needs scipy
            [-1.9999999999999996  0.9999999999999998]
            [ 1.4999999999999998 -0.4999999999999999]

        To compute eigenvalues, use the method
        :meth:`~.Matrix_double_dense.left_eigenvectors` or
        :meth:`~.Matrix_double_dense.right_eigenvectors`.

        ::

            sage: p,e = m.right_eigenvectors()                                              # needs scipy

        The result is a pair ``(p,e)``, where ``p`` is a diagonal matrix of
        eigenvalues and ``e`` is a matrix whose columns are the
        eigenvectors.

        To solve a linear system `Ax = b` where ``A = [[1,2],[3,4]]`` and
        `b = [5,6]`::

            sage: b = vector(RDF,[5,6])
            sage: m.solve_right(b)  # rel tol 1e-15                                         # needs scipy
            (-3.9999999999999987, 4.499999999999999)

        See the methods :meth:`~.Matrix_double_dense.QR`,
        :meth:`~.Matrix_double_dense.LU`, and :meth:`.SVD` for QR, LU, and singular
        value decomposition.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
