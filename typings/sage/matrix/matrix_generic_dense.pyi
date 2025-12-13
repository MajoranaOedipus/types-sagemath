import sage.matrix.matrix_dense
import sage.matrix.matrix_dense as matrix_dense
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

class Matrix_generic_dense(sage.matrix.matrix_dense.Matrix_dense):
    """Matrix_generic_dense(parent, entries=None, copy=None, bool coerce=True)

    File: /build/sagemath/src/sage/src/sage/matrix/matrix_generic_dense.pyx (starting at line 17)

    The ``Matrix_generic_dense`` class derives from
    ``Matrix``, and defines functionality for dense
    matrices over any base ring. Matrices are represented by a list of
    elements in the base ring, and element access operations are
    implemented in this class.

    EXAMPLES::

        sage: A = random_matrix(Integers(25)['x'], 2)
        sage: type(A)
        <class 'sage.matrix.matrix_generic_dense.Matrix_generic_dense'>
        sage: TestSuite(A).run(skip='_test_minpoly')

    Test comparisons::

        sage: A = random_matrix(Integers(25)['x'], 2)
        sage: A == A
        True
        sage: A < A + 1 or A[0, 0].coefficients()[0] == 24
        True
        sage: A+1 < A and A[0, 0].coefficients()[0] != 24
        False

    Test hashing::

        sage: A = random_matrix(Integers(25)['x'], 2)
        sage: hash(A)
        Traceback (most recent call last):
        ...
        TypeError: mutable matrices are unhashable
        sage: A.set_immutable()
        sage: H = hash(A)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, entries=..., copy=..., boolcoerce=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matrix/matrix_generic_dense.pyx (starting at line 52)

                Initialize a dense matrix.

                INPUT:

                - ``parent`` -- a matrix space

                - ``entries`` -- see :func:`matrix`

                - ``copy`` -- ignored (for backwards compatibility)

                - ``coerce`` -- if ``False``, assume without checking that the
                  entries lie in the base ring

                TESTS:

                We check that the problem related to :issue:`9049` is not an issue any
                more::

                    sage: # needs sage.rings.number_field
                    sage: S.<t> = PolynomialRing(QQ)
                    sage: F.<q> = QQ.extension(t^4 + 1)
                    sage: R.<x,y> = PolynomialRing(F)
                    sage: M = MatrixSpace(R, 1, 2)
                    sage: from sage.matrix.matrix_generic_dense import Matrix_generic_dense
                    sage: Matrix_generic_dense(M, (x, y), True, True)
                    [x y]
        """
    @overload
    def __copy__(self) -> Any:
        """Matrix_generic_dense.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_generic_dense.pyx (starting at line 193)

        Create a copy of self, which may be changed without altering
        ``self``.

        EXAMPLES::

            sage: A = matrix(ZZ[['t']], 2,3,range(6)); A
            [0 1 2]
            [3 4 5]
            sage: A.subdivide(1,1); A
            [0|1 2]
            [-+---]
            [3|4 5]
            sage: B = A.__copy__(); B
            [0|1 2]
            [-+---]
            [3|4 5]
            sage: B == A
            True
            sage: B[0,0] = 100
            sage: B
            [100|  1   2]
            [---+-------]
            [  3|  4   5]
            sage: A
            [0|1 2]
            [-+---]
            [3|4 5]
            sage: R.<x> = QQ['x']
            sage: a = matrix(R,2,[x+1,2/3,  x^2/2, 1+x^3]); a
            [  x + 1     2/3]
            [1/2*x^2 x^3 + 1]
            sage: b = copy(a)
            sage: b[0,0] = 5
            sage: b
            [      5     2/3]
            [1/2*x^2 x^3 + 1]
            sage: a
            [  x + 1     2/3]
            [1/2*x^2 x^3 + 1]

        ::

            sage: b = copy(a)
            sage: f = b[0,0]; f[0] = 10
            Traceback (most recent call last):
            ...
            IndexError: polynomials are immutable"""
    @overload
    def __copy__(self) -> Any:
        """Matrix_generic_dense.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_generic_dense.pyx (starting at line 193)

        Create a copy of self, which may be changed without altering
        ``self``.

        EXAMPLES::

            sage: A = matrix(ZZ[['t']], 2,3,range(6)); A
            [0 1 2]
            [3 4 5]
            sage: A.subdivide(1,1); A
            [0|1 2]
            [-+---]
            [3|4 5]
            sage: B = A.__copy__(); B
            [0|1 2]
            [-+---]
            [3|4 5]
            sage: B == A
            True
            sage: B[0,0] = 100
            sage: B
            [100|  1   2]
            [---+-------]
            [  3|  4   5]
            sage: A
            [0|1 2]
            [-+---]
            [3|4 5]
            sage: R.<x> = QQ['x']
            sage: a = matrix(R,2,[x+1,2/3,  x^2/2, 1+x^3]); a
            [  x + 1     2/3]
            [1/2*x^2 x^3 + 1]
            sage: b = copy(a)
            sage: b[0,0] = 5
            sage: b
            [      5     2/3]
            [1/2*x^2 x^3 + 1]
            sage: a
            [  x + 1     2/3]
            [1/2*x^2 x^3 + 1]

        ::

            sage: b = copy(a)
            sage: f = b[0,0]; f[0] = 10
            Traceback (most recent call last):
            ...
            IndexError: polynomials are immutable"""
