import sage as sage
import sage.matrix.matrix2
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

class Matrix_dense(sage.matrix.matrix2.Matrix):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def antitranspose(self) -> Any:
        """Matrix_dense.antitranspose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_dense.pyx (starting at line 148)

        Return the antitranspose of ``self``, without changing ``self``.

        EXAMPLES::

            sage: A = matrix(2,3,range(6)); A
            [0 1 2]
            [3 4 5]
            sage: A.antitranspose()
            [5 2]
            [4 1]
            [3 0]

        ::

            sage: A.subdivide(1,2); A
            [0 1|2]
            [---+-]
            [3 4|5]
            sage: A.antitranspose()
            [5|2]
            [-+-]
            [4|1]
            [3|0]"""
    @overload
    def antitranspose(self) -> Any:
        """Matrix_dense.antitranspose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_dense.pyx (starting at line 148)

        Return the antitranspose of ``self``, without changing ``self``.

        EXAMPLES::

            sage: A = matrix(2,3,range(6)); A
            [0 1 2]
            [3 4 5]
            sage: A.antitranspose()
            [5 2]
            [4 1]
            [3 0]

        ::

            sage: A.subdivide(1,2); A
            [0 1|2]
            [---+-]
            [3 4|5]
            sage: A.antitranspose()
            [5|2]
            [-+-]
            [4|1]
            [3|0]"""
    @overload
    def antitranspose(self) -> Any:
        """Matrix_dense.antitranspose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_dense.pyx (starting at line 148)

        Return the antitranspose of ``self``, without changing ``self``.

        EXAMPLES::

            sage: A = matrix(2,3,range(6)); A
            [0 1 2]
            [3 4 5]
            sage: A.antitranspose()
            [5 2]
            [4 1]
            [3 0]

        ::

            sage: A.subdivide(1,2); A
            [0 1|2]
            [---+-]
            [3 4|5]
            sage: A.antitranspose()
            [5|2]
            [-+-]
            [4|1]
            [3|0]"""
    @overload
    def transpose(self) -> Any:
        """Matrix_dense.transpose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_dense.pyx (starting at line 98)

        Return the transpose of ``self``, without changing ``self``.

        EXAMPLES: We create a matrix, compute its transpose, and note that
        the original matrix is not changed.

        ::

            sage: M = MatrixSpace(QQ,  2)
            sage: A = M([1,2,3,4])
            sage: B = A.transpose()
            sage: print(B)
            [1 3]
            [2 4]
            sage: print(A)
            [1 2]
            [3 4]

        :attr:`~sage.matrix.matrix2.Matrix.T` is a convenient shortcut for the transpose::

           sage: A.T
           [1 3]
           [2 4]

        ::

            sage: A.subdivide(None, 1); A
            [1|2]
            [3|4]
            sage: A.transpose()
            [1 3]
            [---]
            [2 4]"""
    @overload
    def transpose(self) -> Any:
        """Matrix_dense.transpose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_dense.pyx (starting at line 98)

        Return the transpose of ``self``, without changing ``self``.

        EXAMPLES: We create a matrix, compute its transpose, and note that
        the original matrix is not changed.

        ::

            sage: M = MatrixSpace(QQ,  2)
            sage: A = M([1,2,3,4])
            sage: B = A.transpose()
            sage: print(B)
            [1 3]
            [2 4]
            sage: print(A)
            [1 2]
            [3 4]

        :attr:`~sage.matrix.matrix2.Matrix.T` is a convenient shortcut for the transpose::

           sage: A.T
           [1 3]
           [2 4]

        ::

            sage: A.subdivide(None, 1); A
            [1|2]
            [3|4]
            sage: A.transpose()
            [1 3]
            [---]
            [2 4]"""
    @overload
    def transpose(self) -> Any:
        """Matrix_dense.transpose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_dense.pyx (starting at line 98)

        Return the transpose of ``self``, without changing ``self``.

        EXAMPLES: We create a matrix, compute its transpose, and note that
        the original matrix is not changed.

        ::

            sage: M = MatrixSpace(QQ,  2)
            sage: A = M([1,2,3,4])
            sage: B = A.transpose()
            sage: print(B)
            [1 3]
            [2 4]
            sage: print(A)
            [1 2]
            [3 4]

        :attr:`~sage.matrix.matrix2.Matrix.T` is a convenient shortcut for the transpose::

           sage: A.T
           [1 3]
           [2 4]

        ::

            sage: A.subdivide(None, 1); A
            [1|2]
            [3|4]
            sage: A.transpose()
            [1 3]
            [---]
            [2 4]"""
    def __copy__(self) -> Any:
        """Matrix_dense.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_dense.pyx (starting at line 25)

        Return a copy of this matrix. Changing the entries of the copy will
        not change the entries of this matrix."""
