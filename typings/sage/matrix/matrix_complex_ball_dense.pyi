import sage.matrix.matrix_dense
import sage.rings.polynomial.polynomial_ring_constructor as polynomial_ring_constructor
from sage.matrix.constructor import matrix as matrix
from sage.misc.superseded import experimental as experimental
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.sequence import Sequence as Sequence
from typing import Any, Callable, ClassVar, overload

__pyx_capi__: dict

class Matrix_complex_ball_dense(sage.matrix.matrix_dense.Matrix_dense):
    """Matrix_complex_ball_dense(parent, entries=None, copy=None, bool coerce=True)

    File: /build/sagemath/src/sage/src/sage/matrix/matrix_complex_ball_dense.pyx (starting at line 120)

    Matrix over a complex ball field. Implemented using the
    ``acb_mat`` type of the FLINT library.

    EXAMPLES::

        sage: MatrixSpace(CBF, 3)(2)
        [2.000000000000000                 0                 0]
        [                0 2.000000000000000                 0]
        [                0                 0 2.000000000000000]
        sage: matrix(CBF, 1, 3, [1, 2, -3])
        [ 1.000000000000000  2.000000000000000 -3.000000000000000]"""
    eigenvalues: ClassVar[Callable] = ...
    eigenvectors_right: ClassVar[Callable] = ...
    eigenvectors_right_approx: ClassVar[Callable] = ...
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, entries=..., copy=..., boolcoerce=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matrix/matrix_complex_ball_dense.pyx (starting at line 172)

                Initialize a dense matrix over the complex ball field.

                INPUT:

                - ``parent`` -- a matrix space over a complex ball field

                - ``entries`` -- see :func:`matrix`

                - ``copy`` -- ignored (for backwards compatibility)

                - ``coerce`` -- if ``False``, assume without checking that the
                  entries lie in the base ring

                EXAMPLES:

                The ``__init__`` function is called implicitly in each of the
                examples below to actually fill in the values of the matrix.

                We create a `2 \\times 2` and a `1\\times 4` matrix::

                    sage: matrix(CBF, 2, 2, range(4))
                    [                0 1.000000000000000]
                    [2.000000000000000 3.000000000000000]
                    sage: Matrix(CBF, 1, 4, range(4))
                    [                0 1.000000000000000 2.000000000000000 3.000000000000000]

                If the number of columns isn't given, it is determined from the
                number of elements in the list. ::

                    sage: matrix(CBF, 2, range(4))
                    [                0 1.000000000000000]
                    [2.000000000000000 3.000000000000000]
                    sage: matrix(CBF, 2, range(6))
                    [                0 1.000000000000000 2.000000000000000]
                    [3.000000000000000 4.000000000000000 5.000000000000000]

                Another way to make a matrix is to create the space of matrices and
                convert lists into it. ::

                    sage: A = Mat(CBF, 2); A
                    Full MatrixSpace of 2 by 2 dense matrices over
                    Complex ball field with 53 bits of precision
                    sage: A(range(4))
                    [                0 1.000000000000000]
                    [2.000000000000000 3.000000000000000]

                Actually it is only necessary that the input can be converted to a
                list, so the following also works::

                    sage: v = reversed(range(4)); type(v)
                    <...iterator'>
                    sage: A(v)
                    [3.000000000000000 2.000000000000000]
                    [1.000000000000000                 0]

                Matrices can have many rows or columns (in fact, on a 64-bit
                machine they could have up to `2^{63}-1` rows or columns)::

                    sage: v = matrix(CBF, 1, 10^5, range(10^5))
                    sage: v.parent()
                    Full MatrixSpace of 1 by 100000 dense matrices over
                    Complex ball field with 53 bits of precision

                TESTS::

                    sage: MatrixSpace(CBF, 0, 0).one()
                    []
                    sage: Matrix(CBF, 0, 100)
                    0 x 100 dense matrix over Complex ball field with 53 bits
                    of precision (use the '.str()' method to see the entries)
                    sage: Matrix(CBF, 100, 0)
                    100 x 0 dense matrix over Complex ball field with 53 bits
                    of precision (use the '.str()' method to see the entries)
        """
    @overload
    def charpoly(self, var=..., algorithm=...) -> Any:
        """Matrix_complex_ball_dense.charpoly(self, var='x', algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_complex_ball_dense.pyx (starting at line 717)

        Compute the characteristic polynomial of this matrix.

        EXAMPLES::

            sage: from sage.matrix.benchmark import hilbert_matrix
            sage: mat = hilbert_matrix(5).change_ring(ComplexBallField(10))
            sage: mat.charpoly()
            x^5 + ([-1.8 +/- 0.0258])*x^4 + ([0.3 +/- 0.05...)*x^3 +
            ([+/- 0.0...])*x^2 + ([+/- 0.0...])*x + [+/- 0.0...]

        TESTS::

            sage: mat.charpoly(algorithm='hessenberg')
            x^5 + ([-1.8 +/- 0.04...])*x^4 + ([0.3 +/- 0.08...])*x^3
            + ([+/- 0.0...])*x^2 + ([+/- ...e-4])*x + [+/- ...e-6]
            sage: mat.charpoly('y')
            y^5 + ([-1.8 +/- 0.02...])*y^4 + ([0.3 +/- 0.05...])*y^3 +
            ([+/- 0.0...])*y^2 + ([+/- 0.0...])*y + [+/- 0.0...]"""
    @overload
    def charpoly(self) -> Any:
        """Matrix_complex_ball_dense.charpoly(self, var='x', algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_complex_ball_dense.pyx (starting at line 717)

        Compute the characteristic polynomial of this matrix.

        EXAMPLES::

            sage: from sage.matrix.benchmark import hilbert_matrix
            sage: mat = hilbert_matrix(5).change_ring(ComplexBallField(10))
            sage: mat.charpoly()
            x^5 + ([-1.8 +/- 0.0258])*x^4 + ([0.3 +/- 0.05...)*x^3 +
            ([+/- 0.0...])*x^2 + ([+/- 0.0...])*x + [+/- 0.0...]

        TESTS::

            sage: mat.charpoly(algorithm='hessenberg')
            x^5 + ([-1.8 +/- 0.04...])*x^4 + ([0.3 +/- 0.08...])*x^3
            + ([+/- 0.0...])*x^2 + ([+/- ...e-4])*x + [+/- ...e-6]
            sage: mat.charpoly('y')
            y^5 + ([-1.8 +/- 0.02...])*y^4 + ([0.3 +/- 0.05...])*y^3 +
            ([+/- 0.0...])*y^2 + ([+/- 0.0...])*y + [+/- 0.0...]"""
    def contains(self, Matrix_complex_ball_denseother) -> Any:
        """Matrix_complex_ball_dense.contains(self, Matrix_complex_ball_dense other)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_complex_ball_dense.pyx (starting at line 420)

        Test if the set of complex matrices represented by ``self`` is
        contained in that represented by ``other``.

        EXAMPLES::

            sage: b = CBF(0, RBF(0, rad=.1r)); b
            [+/- 0.101]*I
            sage: matrix(CBF, [0, b]).contains(matrix(CBF, [0, 0]))
            True
            sage: matrix(CBF, [0, b]).contains(matrix(CBF, [b, 0]))
            False
            sage: matrix(CBF, [b, b]).contains(matrix(CBF, [b, 0]))
            True"""
    @overload
    def determinant(self) -> Any:
        """Matrix_complex_ball_dense.determinant(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_complex_ball_dense.pyx (starting at line 671)

        Compute the determinant of this matrix.

        EXAMPLES::

            sage: matrix(CBF, [[1/2, 1/3], [1, 1]]).determinant()
            [0.1666666666666667 +/- ...e-17]
            sage: matrix(CBF, [[1/2, 1/3], [1, 1]]).det()
            [0.1666666666666667 +/- ...e-17]
            sage: matrix(CBF, [[1/2, 1/3]]).determinant()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix"""
    @overload
    def determinant(self) -> Any:
        """Matrix_complex_ball_dense.determinant(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_complex_ball_dense.pyx (starting at line 671)

        Compute the determinant of this matrix.

        EXAMPLES::

            sage: matrix(CBF, [[1/2, 1/3], [1, 1]]).determinant()
            [0.1666666666666667 +/- ...e-17]
            sage: matrix(CBF, [[1/2, 1/3], [1, 1]]).det()
            [0.1666666666666667 +/- ...e-17]
            sage: matrix(CBF, [[1/2, 1/3]]).determinant()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix"""
    @overload
    def determinant(self) -> Any:
        """Matrix_complex_ball_dense.determinant(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_complex_ball_dense.pyx (starting at line 671)

        Compute the determinant of this matrix.

        EXAMPLES::

            sage: matrix(CBF, [[1/2, 1/3], [1, 1]]).determinant()
            [0.1666666666666667 +/- ...e-17]
            sage: matrix(CBF, [[1/2, 1/3], [1, 1]]).det()
            [0.1666666666666667 +/- ...e-17]
            sage: matrix(CBF, [[1/2, 1/3]]).determinant()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix"""
    def eigenvectors_left(self, other=..., extend=...) -> Any:
        """Matrix_complex_ball_dense.eigenvectors_left(self, other=None, *, extend=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_complex_ball_dense.pyx (starting at line 981)

        (Experimental.) Compute rigorous enclosures of the eigenvalues and
        left eigenvectors of this matrix.

        INPUT:

        - ``self`` -- an `n \\times n` matrix
        - ``other`` -- unsupported (generalized eigenvalue problem), should be ``None``
        - ``extend`` -- ignored

        OUTPUT:

        A list of triples of the form ``(eigenvalue, [eigenvector], 1)``.

        Unlike :meth:`eigenvalues` and :meth:`eigenvectors_left_approx`, this
        method currently fails in the presence of multiple eigenvalues.

        Additionally, there is currently no guarantee that the algorithm
        converges as the working precision is increased.

        See the `FLINT documentation <https://flintlib.org/doc/acb_mat.html#c.acb_mat_eig_simple>`__
        for more information.

        EXAMPLES::

            sage: mat = matrix(CBF, 3, [2, 3, 5, 7, 11, 13, 17, 19, 23])
            sage: eigval, eigvec, _ = mat.eigenvectors_left()[0]
            sage: eigval
            [1.1052996349...] + [+/- ...]*I
            sage: eigvec[0]
            ([0.69817246751...] + [+/- ...]*I, [-0.67419514369...] + [+/- ...]*I, [0.240865343781...] + [+/- ...]*I)
            sage: eigvec[0] * (mat - eigval)
            ([+/- ...] + [+/- ...]*I, [+/- ...] + [+/- ...]*I, [+/- ...] + [+/- ...]*I)

        .. SEEALSO:: :meth:`eigenvectors_right`, :meth:`eigenvalues`, :meth:`eigenvectors_left_approx`"""
    def eigenvectors_left_approx(self, other=..., extend=...) -> Any:
        """Matrix_complex_ball_dense.eigenvectors_left_approx(self, other=None, *, extend=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_complex_ball_dense.pyx (starting at line 944)

        (Experimental.) Compute *non-rigorous* approximations of the
        left eigenvalues and eigenvectors of this matrix.

        INPUT:

        - ``self`` -- an `n \\times n` matrix
        - ``other`` -- unsupported (generalized eigenvalue problem), should be ``None``
        - ``extend`` -- ignored

        OUTPUT:

        A list of triples of the form ``(eigenvalue, [eigenvector], 1)``. The
        eigenvalue and the entries of the eigenvector are complex balls with
        zero radius.

        No guarantees are made about the accuracy of the output.

        See the `FLINT documentation <https://flintlib.org/doc/acb_mat.html#c.acb_mat_approx_eig_qr>`__
        for more information.

        EXAMPLES::

            sage: mat = matrix(CBF, 3, [2, 3, 5, 7, 11, 13, 17, 19, 23])
            sage: eigval, eigvec, _ = mat.eigenvectors_left_approx()[0]
            sage: eigval
            [1.1052996349... +/- ...]
            sage: eigvec[0]
            ([0.69817246751...], [-0.67419514369...], [0.240865343781...])
            sage: eigvec[0] * (mat - eigval)
            ([+/- ...], [+/- ...], [+/- ...])

        .. SEEALSO:: :meth:`eigenvectors_left`"""
    @overload
    def exp(self) -> Any:
        """Matrix_complex_ball_dense.exp(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_complex_ball_dense.pyx (starting at line 1020)

        Compute the exponential of this matrix.

        EXAMPLES::

            sage: matrix(CBF, [[i*pi, 1], [0, i*pi]]).exp()                             # needs sage.symbolic
            [[-1.00000000000000 +/- ...e-16] + [+/- ...e-16]*I [-1.00000000000000 +/- ...e-16] + [+/- ...e-16]*I]
            [                                                0 [-1.00000000000000 +/- ...e-16] + [+/- ...e-16]*I]
            sage: matrix(CBF, [[1/2, 1/3]]).exp()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix"""
    @overload
    def exp(self) -> Any:
        """Matrix_complex_ball_dense.exp(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_complex_ball_dense.pyx (starting at line 1020)

        Compute the exponential of this matrix.

        EXAMPLES::

            sage: matrix(CBF, [[i*pi, 1], [0, i*pi]]).exp()                             # needs sage.symbolic
            [[-1.00000000000000 +/- ...e-16] + [+/- ...e-16]*I [-1.00000000000000 +/- ...e-16] + [+/- ...e-16]*I]
            [                                                0 [-1.00000000000000 +/- ...e-16] + [+/- ...e-16]*I]
            sage: matrix(CBF, [[1/2, 1/3]]).exp()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix"""
    @overload
    def exp(self) -> Any:
        """Matrix_complex_ball_dense.exp(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_complex_ball_dense.pyx (starting at line 1020)

        Compute the exponential of this matrix.

        EXAMPLES::

            sage: matrix(CBF, [[i*pi, 1], [0, i*pi]]).exp()                             # needs sage.symbolic
            [[-1.00000000000000 +/- ...e-16] + [+/- ...e-16]*I [-1.00000000000000 +/- ...e-16] + [+/- ...e-16]*I]
            [                                                0 [-1.00000000000000 +/- ...e-16] + [+/- ...e-16]*I]
            sage: matrix(CBF, [[1/2, 1/3]]).exp()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix"""
    @overload
    def identical(self, Matrix_complex_ball_denseother) -> Any:
        """Matrix_complex_ball_dense.identical(self, Matrix_complex_ball_dense other)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_complex_ball_dense.pyx (starting at line 388)

        Test if the corresponding entries of two complex ball matrices
        represent the same balls.

        EXAMPLES::

            sage: a = matrix(CBF, [[1/3,2],[3,4]])
            sage: b = matrix(CBF, [[1/3,2],[3,4]])
            sage: a == b
            False
            sage: a.identical(b)
            True"""
    @overload
    def identical(self, b) -> Any:
        """Matrix_complex_ball_dense.identical(self, Matrix_complex_ball_dense other)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_complex_ball_dense.pyx (starting at line 388)

        Test if the corresponding entries of two complex ball matrices
        represent the same balls.

        EXAMPLES::

            sage: a = matrix(CBF, [[1/3,2],[3,4]])
            sage: b = matrix(CBF, [[1/3,2],[3,4]])
            sage: a == b
            False
            sage: a.identical(b)
            True"""
    def overlaps(self, Matrix_complex_ball_denseother) -> Any:
        """Matrix_complex_ball_dense.overlaps(self, Matrix_complex_ball_dense other)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_complex_ball_dense.pyx (starting at line 404)

        Test if two matrices with complex ball entries represent overlapping
        sets of complex matrices.

        EXAMPLES::

            sage: b = CBF(0, RBF(0, rad=0.1r)); b
            [+/- 0.101]*I
            sage: matrix(CBF, [0, b]).overlaps(matrix(CBF, [b, 0]))
            True
            sage: matrix(CBF, [1, 0]).overlaps(matrix(CBF, [b, 0]))
            False"""
    @overload
    def trace(self) -> Any:
        """Matrix_complex_ball_dense.trace(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_complex_ball_dense.pyx (starting at line 695)

        Compute the trace of this matrix.

        EXAMPLES::

            sage: matrix(CBF, [[1/3, 1/3], [1, 1]]).trace()
            [1.333333333333333 +/- ...e-16]
            sage: matrix(CBF, [[1/2, 1/3]]).trace()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix"""
    @overload
    def trace(self) -> Any:
        """Matrix_complex_ball_dense.trace(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_complex_ball_dense.pyx (starting at line 695)

        Compute the trace of this matrix.

        EXAMPLES::

            sage: matrix(CBF, [[1/3, 1/3], [1, 1]]).trace()
            [1.333333333333333 +/- ...e-16]
            sage: matrix(CBF, [[1/2, 1/3]]).trace()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix"""
    @overload
    def trace(self) -> Any:
        """Matrix_complex_ball_dense.trace(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_complex_ball_dense.pyx (starting at line 695)

        Compute the trace of this matrix.

        EXAMPLES::

            sage: matrix(CBF, [[1/3, 1/3], [1, 1]]).trace()
            [1.333333333333333 +/- ...e-16]
            sage: matrix(CBF, [[1/2, 1/3]]).trace()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix"""
    @overload
    def transpose(self) -> Any:
        """Matrix_complex_ball_dense.transpose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_complex_ball_dense.pyx (starting at line 595)

        Return the transpose of ``self``.

        EXAMPLES::

            sage: m = matrix(CBF, 2, 3, [1, 2, 3, 4, 5, 6])
            sage: m.transpose()
            [1.000000000000000 4.000000000000000]
            [2.000000000000000 5.000000000000000]
            [3.000000000000000 6.000000000000000]
            sage: m.transpose().parent()
            Full MatrixSpace of 3 by 2 dense matrices over Complex ball field with 53 bits of precision

        TESTS::

            sage: m = matrix(CBF,2,3,range(6))
            sage: m.subdivide([1],[2])
            sage: m
            [                0 1.000000000000000|2.000000000000000]
            [-----------------------------------+-----------------]
            [3.000000000000000 4.000000000000000|5.000000000000000]
            sage: m.transpose()
            [                0|3.000000000000000]
            [1.000000000000000|4.000000000000000]
            [-----------------+-----------------]
            [2.000000000000000|5.000000000000000]

            sage: m = matrix(CBF,0,2)
            sage: m.subdivide([],[1])
            sage: m.subdivisions()
            ([], [1])
            sage: m.transpose().subdivisions()
            ([1], [])

            sage: m = matrix(CBF,2,0)
            sage: m.subdivide([1],[])
            sage: m.subdivisions()
            ([1], [])
            sage: m.transpose().subdivisions()
            ([], [1])"""
    @overload
    def transpose(self) -> Any:
        """Matrix_complex_ball_dense.transpose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_complex_ball_dense.pyx (starting at line 595)

        Return the transpose of ``self``.

        EXAMPLES::

            sage: m = matrix(CBF, 2, 3, [1, 2, 3, 4, 5, 6])
            sage: m.transpose()
            [1.000000000000000 4.000000000000000]
            [2.000000000000000 5.000000000000000]
            [3.000000000000000 6.000000000000000]
            sage: m.transpose().parent()
            Full MatrixSpace of 3 by 2 dense matrices over Complex ball field with 53 bits of precision

        TESTS::

            sage: m = matrix(CBF,2,3,range(6))
            sage: m.subdivide([1],[2])
            sage: m
            [                0 1.000000000000000|2.000000000000000]
            [-----------------------------------+-----------------]
            [3.000000000000000 4.000000000000000|5.000000000000000]
            sage: m.transpose()
            [                0|3.000000000000000]
            [1.000000000000000|4.000000000000000]
            [-----------------+-----------------]
            [2.000000000000000|5.000000000000000]

            sage: m = matrix(CBF,0,2)
            sage: m.subdivide([],[1])
            sage: m.subdivisions()
            ([], [1])
            sage: m.transpose().subdivisions()
            ([1], [])

            sage: m = matrix(CBF,2,0)
            sage: m.subdivide([1],[])
            sage: m.subdivisions()
            ([1], [])
            sage: m.transpose().subdivisions()
            ([], [1])"""
    @overload
    def transpose(self) -> Any:
        """Matrix_complex_ball_dense.transpose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_complex_ball_dense.pyx (starting at line 595)

        Return the transpose of ``self``.

        EXAMPLES::

            sage: m = matrix(CBF, 2, 3, [1, 2, 3, 4, 5, 6])
            sage: m.transpose()
            [1.000000000000000 4.000000000000000]
            [2.000000000000000 5.000000000000000]
            [3.000000000000000 6.000000000000000]
            sage: m.transpose().parent()
            Full MatrixSpace of 3 by 2 dense matrices over Complex ball field with 53 bits of precision

        TESTS::

            sage: m = matrix(CBF,2,3,range(6))
            sage: m.subdivide([1],[2])
            sage: m
            [                0 1.000000000000000|2.000000000000000]
            [-----------------------------------+-----------------]
            [3.000000000000000 4.000000000000000|5.000000000000000]
            sage: m.transpose()
            [                0|3.000000000000000]
            [1.000000000000000|4.000000000000000]
            [-----------------+-----------------]
            [2.000000000000000|5.000000000000000]

            sage: m = matrix(CBF,0,2)
            sage: m.subdivide([],[1])
            sage: m.subdivisions()
            ([], [1])
            sage: m.transpose().subdivisions()
            ([1], [])

            sage: m = matrix(CBF,2,0)
            sage: m.subdivide([1],[])
            sage: m.subdivisions()
            ([1], [])
            sage: m.transpose().subdivisions()
            ([], [1])"""
    @overload
    def transpose(self) -> Any:
        """Matrix_complex_ball_dense.transpose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_complex_ball_dense.pyx (starting at line 595)

        Return the transpose of ``self``.

        EXAMPLES::

            sage: m = matrix(CBF, 2, 3, [1, 2, 3, 4, 5, 6])
            sage: m.transpose()
            [1.000000000000000 4.000000000000000]
            [2.000000000000000 5.000000000000000]
            [3.000000000000000 6.000000000000000]
            sage: m.transpose().parent()
            Full MatrixSpace of 3 by 2 dense matrices over Complex ball field with 53 bits of precision

        TESTS::

            sage: m = matrix(CBF,2,3,range(6))
            sage: m.subdivide([1],[2])
            sage: m
            [                0 1.000000000000000|2.000000000000000]
            [-----------------------------------+-----------------]
            [3.000000000000000 4.000000000000000|5.000000000000000]
            sage: m.transpose()
            [                0|3.000000000000000]
            [1.000000000000000|4.000000000000000]
            [-----------------+-----------------]
            [2.000000000000000|5.000000000000000]

            sage: m = matrix(CBF,0,2)
            sage: m.subdivide([],[1])
            sage: m.subdivisions()
            ([], [1])
            sage: m.transpose().subdivisions()
            ([1], [])

            sage: m = matrix(CBF,2,0)
            sage: m.subdivide([1],[])
            sage: m.subdivisions()
            ([1], [])
            sage: m.transpose().subdivisions()
            ([], [1])"""
    @overload
    def transpose(self) -> Any:
        """Matrix_complex_ball_dense.transpose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_complex_ball_dense.pyx (starting at line 595)

        Return the transpose of ``self``.

        EXAMPLES::

            sage: m = matrix(CBF, 2, 3, [1, 2, 3, 4, 5, 6])
            sage: m.transpose()
            [1.000000000000000 4.000000000000000]
            [2.000000000000000 5.000000000000000]
            [3.000000000000000 6.000000000000000]
            sage: m.transpose().parent()
            Full MatrixSpace of 3 by 2 dense matrices over Complex ball field with 53 bits of precision

        TESTS::

            sage: m = matrix(CBF,2,3,range(6))
            sage: m.subdivide([1],[2])
            sage: m
            [                0 1.000000000000000|2.000000000000000]
            [-----------------------------------+-----------------]
            [3.000000000000000 4.000000000000000|5.000000000000000]
            sage: m.transpose()
            [                0|3.000000000000000]
            [1.000000000000000|4.000000000000000]
            [-----------------+-----------------]
            [2.000000000000000|5.000000000000000]

            sage: m = matrix(CBF,0,2)
            sage: m.subdivide([],[1])
            sage: m.subdivisions()
            ([], [1])
            sage: m.transpose().subdivisions()
            ([1], [])

            sage: m = matrix(CBF,2,0)
            sage: m.subdivide([1],[])
            sage: m.subdivisions()
            ([1], [])
            sage: m.transpose().subdivisions()
            ([], [1])"""
    @overload
    def transpose(self) -> Any:
        """Matrix_complex_ball_dense.transpose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_complex_ball_dense.pyx (starting at line 595)

        Return the transpose of ``self``.

        EXAMPLES::

            sage: m = matrix(CBF, 2, 3, [1, 2, 3, 4, 5, 6])
            sage: m.transpose()
            [1.000000000000000 4.000000000000000]
            [2.000000000000000 5.000000000000000]
            [3.000000000000000 6.000000000000000]
            sage: m.transpose().parent()
            Full MatrixSpace of 3 by 2 dense matrices over Complex ball field with 53 bits of precision

        TESTS::

            sage: m = matrix(CBF,2,3,range(6))
            sage: m.subdivide([1],[2])
            sage: m
            [                0 1.000000000000000|2.000000000000000]
            [-----------------------------------+-----------------]
            [3.000000000000000 4.000000000000000|5.000000000000000]
            sage: m.transpose()
            [                0|3.000000000000000]
            [1.000000000000000|4.000000000000000]
            [-----------------+-----------------]
            [2.000000000000000|5.000000000000000]

            sage: m = matrix(CBF,0,2)
            sage: m.subdivide([],[1])
            sage: m.subdivisions()
            ([], [1])
            sage: m.transpose().subdivisions()
            ([1], [])

            sage: m = matrix(CBF,2,0)
            sage: m.subdivide([1],[])
            sage: m.subdivisions()
            ([1], [])
            sage: m.transpose().subdivisions()
            ([], [1])"""
    def __invert__(self) -> Any:
        """Matrix_complex_ball_dense.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_complex_ball_dense.pyx (starting at line 567)

        TESTS::

            sage: ~matrix(CBF, [[1/2, 1/3], [1, 1]])
            [ [6.00000000000000 +/- ...e-15] [-2.00000000000000 +/- ...e-15]]
            [[-6.00000000000000 +/- ...e-15]  [3.00000000000000 +/- ...e-15]]
            sage: ~matrix(CBF, [[1/2, 1/3]])
            Traceback (most recent call last):
            ...
            ArithmeticError: self must be a square matrix
            sage: mat = matrix(CBF, [[1/3, 1/2], [0, 1]]) - 1/3
            sage: ~mat
            Traceback (most recent call last):
            ...
            ZeroDivisionError: unable to compute the inverse, is the matrix singular?"""
    def __neg__(self) -> Any:
        """Matrix_complex_ball_dense.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_complex_ball_dense.pyx (starting at line 438)

        TESTS::

            sage: -matrix(CBF, [[1,2]])
            [-1.000000000000000 -2.000000000000000]"""
