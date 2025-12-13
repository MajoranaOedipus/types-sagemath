import _cython_3_2_1
import sage.matrix.matrix_sparse
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar

Matrix_sparse_from_rows: _cython_3_2_1.cython_function_or_method

class Matrix_generic_sparse(sage.matrix.matrix_sparse.Matrix_sparse):
    """Matrix_generic_sparse(parent, entries=None, copy=None, bool coerce=True)

    File: /build/sagemath/src/sage/src/sage/matrix/matrix_generic_sparse.pyx (starting at line 62)

    Generic sparse matrix.

    The ``Matrix_generic_sparse`` class derives from
    :class:`~sage.matrix.matrix_sparse.Matrix_sparse`, and defines functionality
    for sparse matrices over any base ring. A generic sparse matrix is
    represented using a dictionary whose keys are pairs of integers `(i,j)` and
    values in the base ring. The values of the dictionary must never be zero.

    EXAMPLES::

        sage: R.<a,b> = PolynomialRing(ZZ,'a,b')
        sage: M = MatrixSpace(R,5,5,sparse=True)
        sage: M({(0,0):5*a+2*b, (3,4): -a})
        [5*a + 2*b         0         0         0         0]
        [        0         0         0         0         0]
        [        0         0         0         0         0]
        [        0         0         0         0        -a]
        [        0         0         0         0         0]
        sage: M(3)
        [3 0 0 0 0]
        [0 3 0 0 0]
        [0 0 3 0 0]
        [0 0 0 3 0]
        [0 0 0 0 3]
        sage: V = FreeModule(ZZ, 5,sparse=True)
        sage: m = M([V({0:3}), V({2:2, 4:-1}), V(0), V(0), V({1:2})])
        sage: m
        [ 3  0  0  0  0]
        [ 0  0  2  0 -1]
        [ 0  0  0  0  0]
        [ 0  0  0  0  0]
        [ 0  2  0  0  0]

    .. NOTE::

        The datastructure can potentially be optimized. Firstly, as noticed in
        :issue:`17663`, we lose time in using 2-tuples to store indices.
        Secondly, there is no fast way to access nonzero elements in a given
        row/column."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, entries=..., copy=..., boolcoerce=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matrix/matrix_generic_sparse.pyx (starting at line 108)

                Create a sparse matrix over the given base ring.

                INPUT:

                - ``parent`` -- a matrix space

                - ``entries`` -- see :func:`matrix`

                - ``copy`` -- ignored (for backwards compatibility)

                - ``coerce`` -- if ``False``, assume without checking that the
                  entries lie in the base ring

                TESTS::

                    sage: R.<a> = PolynomialRing(ZZ,'a')
                    sage: M = MatrixSpace(R,2,3,sparse=True)
                    sage: m = M([4,1,0,0,0,2]); m
                    [4 1 0]
                    [0 0 2]
                    sage: m2 = copy(m)
                    sage: m2[0,0] = -1
                    sage: m[0,0]
                    4
                    sage: loads(dumps(m)) == m
                    True

                    sage: R2.<a,b> = PolynomialRing(QQ)
                    sage: M2 = MatrixSpace(R2,2,3,sparse=True)
                    sage: M2(m)
                    [4 1 0]
                    [0 0 2]
                    sage: M2.has_coerce_map_from(M)
                    True

                    sage: M3 = M2.change_ring(R2.fraction_field())
                    sage: M3.has_coerce_map_from(M2)
                    True

                Check that it is not possible to use wrong indices::

                    sage: M = MatrixSpace(R,2,2,sparse=True)
                    sage: M({(3,0): 1})
                    Traceback (most recent call last):
                    ...
                    IndexError: invalid row index 3
                    sage: M({(0,-3): 1})
                    Traceback (most recent call last):
                    ...
                    IndexError: invalid column index -3

                But negative indices are valid and wrap around::

                    sage: M({(-1,-1): 1})
                    [0 0]
                    [0 1]
        """
    def __bool__(self) -> bool:
        """True if self else False"""
    def __copy__(self) -> Any:
        """Matrix_generic_sparse.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_generic_sparse.pyx (starting at line 384)"""
