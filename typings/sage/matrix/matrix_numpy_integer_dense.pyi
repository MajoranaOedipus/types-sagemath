import sage.matrix.matrix_numpy_dense
from sage.categories.category import ZZ as ZZ
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import ClassVar

numpy: None
scipy: None

class Matrix_numpy_integer_dense(sage.matrix.matrix_numpy_dense.Matrix_numpy_dense):
    """File: /build/sagemath/src/sage/src/sage/matrix/matrix_numpy_integer_dense.pyx (starting at line 40)

        TESTS::

            sage: from sage.matrix.matrix_numpy_integer_dense import Matrix_numpy_integer_dense
            sage: M = Matrix_numpy_integer_dense(MatrixSpace(ZZ, 2, 3))
            sage: TestSuite(M).run()
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
