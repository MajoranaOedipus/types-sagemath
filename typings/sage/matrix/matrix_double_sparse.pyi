import sage.matrix.matrix_generic_sparse
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar

class Matrix_double_sparse(sage.matrix.matrix_generic_sparse.Matrix_generic_sparse):
    """File: /build/sagemath/src/sage/src/sage/matrix/matrix_double_sparse.pyx (starting at line 5)

        Class for sparse RDF/CDF matrices.

        EXAMPLES::

            sage: A = matrix.random(RDF, ZZ.random_element(5), sparse=True)
            sage: A.__class__
            <class 'sage.matrix.matrix_double_sparse.Matrix_double_sparse'>
            sage: A = matrix.random(CDF, ZZ.random_element(5), sparse=True)
            sage: A.__class__
            <class 'sage.matrix.matrix_double_sparse.Matrix_double_sparse'>
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def cholesky(self) -> Any:
        '''Matrix_double_sparse.cholesky(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_double_sparse.pyx (starting at line 96)

        Return the Cholesky decomposition of a Hermitian matrix.

        Applies to a positive-definite matrix over ``RDF`` or ``CDF``.

        OUTPUT:

        For a matrix `A` the routine returns a lower triangular
        matrix `L` (over the same base ring as `A`) such that,

        .. MATH::

            A = LL^\\ast

        where `L^\\ast` is the conjugate-transpose. If the matrix is
        not positive-definite (for example, if it is not Hermitian)
        then a :exc:`ValueError` results.

        ALGORITHM:

        If cvxopt is available, we use its sparse `cholmod` routines
        to compute the factorization quickly. Otherwise, we fall back
        to the naive implementation used for dense matrices.

        EXAMPLES::

            sage: A = matrix(RDF, [[10, 0, 3, 0],
            ....:                  [ 0, 5, 0,-2],
            ....:                  [ 3, 0, 5, 0],
            ....:                  [ 0,-2, 0, 2]],
            ....:                 sparse=True)
            sage: L = A.cholesky()
            sage: L.is_triangular()
            True
            sage: (A - L*L.T).norm(1) < 1e-10
            True

        ::

            sage: # needs sage.rings.complex_double sage.symbolic
            sage: A = matrix(CDF, [[        2,   4 + 2*I,   6 - 4*I],
            ....:                  [ -2*I + 4,        11, 10 - 12*I],
            ....:                  [  4*I + 6, 10 + 12*I,        37]])
            sage: L = A.cholesky()
            sage: L.is_triangular()
            True
            sage: (A - L*L.H).norm(1) < 1e-10
            True

        TESTS:

        Test the properties of a Cholesky factorization using "random"
        symmetric/Hermitian positive-definite matrices. We also
        compare with the dense factorizations, which, when cvxopt is
        available, use a different implementation. This ensures that
        both implementations return comparable answers::

            sage: n = ZZ.random_element(1,5)
            sage: A = matrix.random(RDF, n, sparse=True)
            sage: I = matrix.identity(RDF, n, sparse=True)
            sage: A = A*A.transpose() + I
            sage: L = A.cholesky()
            sage: (A - L*L.T).norm(1) < 1e-10
            True
            sage: B = A.dense_matrix()
            sage: (B.cholesky() - L).norm(1) < 1e-10                                    # needs scipy
            True

        ::

            sage: # needs sage.rings.complex_double sage.symbolic
            sage: n = ZZ.random_element(1,5)
            sage: A = matrix.random(CDF, n, sparse=True)
            sage: I = matrix.identity(CDF, n, sparse=True)
            sage: A = A*A.conjugate_transpose() + I
            sage: L = A.cholesky()
            sage: (A - L*L.H).norm(1) < 1e-10
            True
            sage: B = A.dense_matrix()
            sage: (B.cholesky() - L).norm(1) < 1e-10                                    # needs scipy
            True'''
    def is_hermitian(self, tolerance=...) -> Any:
        """Matrix_double_sparse.is_hermitian(self, tolerance=1e-12)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_double_sparse.pyx (starting at line 19)

        Return whether or not the matrix is Hermitian, up to the
        entry-wise ``tolerance``.

        A matrix is said to be Hermitian if it is equal to its
        conjugate-transpose. We default to a small but nonzero
        entry-wise tolerance because, otherwise, numerical issues
        can cause false negatives (Issue #33023).

        Otherwise this method is identical to the superclass method,
        which simply defers to :meth:`_is_hermitian`.

        INPUT:

        - ``tolerance`` -- a real number; the maximum difference we'll
          tolerate between entries of the given matrix and its conjugate-
          transpose.

        OUTPUT: boolean

        EXAMPLES::

            sage: A = matrix(RDF,
            ....:            [ [1, 1e-13],
            ....:              [0, 1    ] ],
            ....:            sparse=True)
            sage: A.is_hermitian()
            True

        TESTS::

            sage: A = matrix.random(CDF, 2, sparse=True)
            sage: (A*A.conjugate_transpose()).is_hermitian()
            True"""
    def is_skew_hermitian(self, tolerance=...) -> Any:
        """Matrix_double_sparse.is_skew_hermitian(self, tolerance=1e-12)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_double_sparse.pyx (starting at line 57)

        Return whether or not the matrix is skew-Hermitian, up to the
        entry-wise ``tolerance``.

        A matrix is said to be skew-Hermitian if it is equal to the
        negation of its conjugate-transpose. We default to a small but
        nonzero entry-wise tolerance because, otherwise, numerical
        issues can cause false negatives (Issue #33023).

        Otherwise this method is identical to the superclass method,
        which simply defers to :meth:`_is_hermitian` (passing
        ``skew=True``).

        INPUT:

        - ``tolerance`` -- a real number; the maximum difference we'll
          tolerate between entries of the given matrix and the
          negation of its conjugate-transpose.

        OUTPUT: boolean

        EXAMPLES::

            sage: A = matrix(RDF,
            ....:            [ [0, 1e-13],
            ....:              [0, 0    ] ],
            ....:            sparse=True)
            sage: A.is_skew_hermitian()
            True

        TESTS::

            sage: A = matrix.random(CDF, 2, sparse=True)
            sage: (A - A.conjugate_transpose()).is_skew_hermitian()
            True"""
