import sage.matrix.matrix_dense
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

numpy: None
scipy: None

class Matrix_numpy_dense(sage.matrix.matrix_dense.Matrix_dense):
    """Matrix_numpy_dense(parent, entries=None, copy=None, bool coerce=True)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, entries=..., copy=..., boolcoerce=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matrix/matrix_numpy_dense.pyx (starting at line 78)

                Fill the matrix with entries.

                The numpy matrix must have already been allocated.

                INPUT:

                - ``parent`` -- a matrix space over ``RDF``

                - ``entries`` -- see :func:`matrix`

                - ``copy`` -- ignored (for backwards compatibility)

                - ``coerce`` -- if ``True`` (the default), convert elements to the
                  base ring before passing them to NumPy. If ``False``, pass the
                  elements to NumPy as given.

                EXAMPLES::

                    sage: matrix(RDF,3,range(9))
                    [0.0 1.0 2.0]
                    [3.0 4.0 5.0]
                    [6.0 7.0 8.0]
                    sage: matrix(CDF,3,3,2)
                    [2.0 0.0 0.0]
                    [0.0 2.0 0.0]
                    [0.0 0.0 2.0]

                TESTS::

                    sage: matrix(RDF,3,0)
                    []
                    sage: matrix(RDF,3,3,0)
                    [0.0 0.0 0.0]
                    [0.0 0.0 0.0]
                    [0.0 0.0 0.0]
                    sage: matrix(RDF,3,3,1)
                    [1.0 0.0 0.0]
                    [0.0 1.0 0.0]
                    [0.0 0.0 1.0]
                    sage: matrix(RDF,3,3,2)
                    [2.0 0.0 0.0]
                    [0.0 2.0 0.0]
                    [0.0 0.0 2.0]
                    sage: matrix(CDF,3,0)
                    []
                    sage: matrix(CDF,3,3,0)
                    [0.0 0.0 0.0]
                    [0.0 0.0 0.0]
                    [0.0 0.0 0.0]
                    sage: matrix(CDF,3,3,1)
                    [1.0 0.0 0.0]
                    [0.0 1.0 0.0]
                    [0.0 0.0 1.0]
                    sage: matrix(CDF,3,3,range(9))
                    [0.0 1.0 2.0]
                    [3.0 4.0 5.0]
                    [6.0 7.0 8.0]
                    sage: matrix(CDF,2,2,[CDF(1+I)*j for j in range(4)])                        # needs sage.symbolic
                    [        0.0 1.0 + 1.0*I]
                    [2.0 + 2.0*I 3.0 + 3.0*I]
        """
    @overload
    def is_symmetric(self, tol=...) -> Any:
        """Matrix_numpy_dense.is_symmetric(self, tol=1e-12)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_numpy_dense.pyx (starting at line 348)

        Return whether this matrix is symmetric, to the given tolerance.

        EXAMPLES::

            sage: m = matrix(RDF,2,2,range(4)); m
            [0.0 1.0]
            [2.0 3.0]
            sage: m.is_symmetric()
            False
            sage: m[1,0] = 1.1; m
            [0.0 1.0]
            [1.1 3.0]
            sage: m.is_symmetric()
            False

        The tolerance inequality is strict::

            sage: m.is_symmetric(tol=0.1)
            False
            sage: m.is_symmetric(tol=0.11)
            True

        TESTS:

        Complex entries are supported (:issue:`27831`).  ::

            sage: a = matrix(CDF, [(21, 0.6 + 18.5*i), (0.6 - 18.5*i, 21)])             # needs sage.symbolic
            sage: a.is_symmetric()                                                      # needs sage.symbolic
            False"""
    @overload
    def is_symmetric(self) -> Any:
        """Matrix_numpy_dense.is_symmetric(self, tol=1e-12)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_numpy_dense.pyx (starting at line 348)

        Return whether this matrix is symmetric, to the given tolerance.

        EXAMPLES::

            sage: m = matrix(RDF,2,2,range(4)); m
            [0.0 1.0]
            [2.0 3.0]
            sage: m.is_symmetric()
            False
            sage: m[1,0] = 1.1; m
            [0.0 1.0]
            [1.1 3.0]
            sage: m.is_symmetric()
            False

        The tolerance inequality is strict::

            sage: m.is_symmetric(tol=0.1)
            False
            sage: m.is_symmetric(tol=0.11)
            True

        TESTS:

        Complex entries are supported (:issue:`27831`).  ::

            sage: a = matrix(CDF, [(21, 0.6 + 18.5*i), (0.6 - 18.5*i, 21)])             # needs sage.symbolic
            sage: a.is_symmetric()                                                      # needs sage.symbolic
            False"""
    @overload
    def is_symmetric(self) -> Any:
        """Matrix_numpy_dense.is_symmetric(self, tol=1e-12)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_numpy_dense.pyx (starting at line 348)

        Return whether this matrix is symmetric, to the given tolerance.

        EXAMPLES::

            sage: m = matrix(RDF,2,2,range(4)); m
            [0.0 1.0]
            [2.0 3.0]
            sage: m.is_symmetric()
            False
            sage: m[1,0] = 1.1; m
            [0.0 1.0]
            [1.1 3.0]
            sage: m.is_symmetric()
            False

        The tolerance inequality is strict::

            sage: m.is_symmetric(tol=0.1)
            False
            sage: m.is_symmetric(tol=0.11)
            True

        TESTS:

        Complex entries are supported (:issue:`27831`).  ::

            sage: a = matrix(CDF, [(21, 0.6 + 18.5*i), (0.6 - 18.5*i, 21)])             # needs sage.symbolic
            sage: a.is_symmetric()                                                      # needs sage.symbolic
            False"""
    @overload
    def is_symmetric(self, tol=...) -> Any:
        """Matrix_numpy_dense.is_symmetric(self, tol=1e-12)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_numpy_dense.pyx (starting at line 348)

        Return whether this matrix is symmetric, to the given tolerance.

        EXAMPLES::

            sage: m = matrix(RDF,2,2,range(4)); m
            [0.0 1.0]
            [2.0 3.0]
            sage: m.is_symmetric()
            False
            sage: m[1,0] = 1.1; m
            [0.0 1.0]
            [1.1 3.0]
            sage: m.is_symmetric()
            False

        The tolerance inequality is strict::

            sage: m.is_symmetric(tol=0.1)
            False
            sage: m.is_symmetric(tol=0.11)
            True

        TESTS:

        Complex entries are supported (:issue:`27831`).  ::

            sage: a = matrix(CDF, [(21, 0.6 + 18.5*i), (0.6 - 18.5*i, 21)])             # needs sage.symbolic
            sage: a.is_symmetric()                                                      # needs sage.symbolic
            False"""
    @overload
    def is_symmetric(self, tol=...) -> Any:
        """Matrix_numpy_dense.is_symmetric(self, tol=1e-12)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_numpy_dense.pyx (starting at line 348)

        Return whether this matrix is symmetric, to the given tolerance.

        EXAMPLES::

            sage: m = matrix(RDF,2,2,range(4)); m
            [0.0 1.0]
            [2.0 3.0]
            sage: m.is_symmetric()
            False
            sage: m[1,0] = 1.1; m
            [0.0 1.0]
            [1.1 3.0]
            sage: m.is_symmetric()
            False

        The tolerance inequality is strict::

            sage: m.is_symmetric(tol=0.1)
            False
            sage: m.is_symmetric(tol=0.11)
            True

        TESTS:

        Complex entries are supported (:issue:`27831`).  ::

            sage: a = matrix(CDF, [(21, 0.6 + 18.5*i), (0.6 - 18.5*i, 21)])             # needs sage.symbolic
            sage: a.is_symmetric()                                                      # needs sage.symbolic
            False"""
    @overload
    def is_symmetric(self) -> Any:
        """Matrix_numpy_dense.is_symmetric(self, tol=1e-12)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_numpy_dense.pyx (starting at line 348)

        Return whether this matrix is symmetric, to the given tolerance.

        EXAMPLES::

            sage: m = matrix(RDF,2,2,range(4)); m
            [0.0 1.0]
            [2.0 3.0]
            sage: m.is_symmetric()
            False
            sage: m[1,0] = 1.1; m
            [0.0 1.0]
            [1.1 3.0]
            sage: m.is_symmetric()
            False

        The tolerance inequality is strict::

            sage: m.is_symmetric(tol=0.1)
            False
            sage: m.is_symmetric(tol=0.11)
            True

        TESTS:

        Complex entries are supported (:issue:`27831`).  ::

            sage: a = matrix(CDF, [(21, 0.6 + 18.5*i), (0.6 - 18.5*i, 21)])             # needs sage.symbolic
            sage: a.is_symmetric()                                                      # needs sage.symbolic
            False"""
    @overload
    def numpy(self, dtype=...) -> Any:
        """Matrix_numpy_dense.numpy(self, dtype=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_numpy_dense.pyx (starting at line 434)

        Return a copy of the matrix as a numpy array.

        It uses the numpy C/api so is very fast.

        INPUT:

        - ``dtype`` -- the desired data-type for the array. If not given,
          then the type will be determined as the minimum type required
          to hold the objects in the sequence.

        EXAMPLES::

            sage: m = matrix(RDF,[[1,2],[3,4]])
            sage: n = m.numpy()
            sage: import numpy
            sage: tuple(numpy.linalg.eig(n))
            (array([-0.37228132,  5.37228132]),
             array([[-0.82456484, -0.41597356],
                   [ 0.56576746, -0.90937671]]))
            sage: m = matrix(RDF, 2, range(6)); m
            [0.0 1.0 2.0]
            [3.0 4.0 5.0]
            sage: m.numpy()
            array([[0., 1., 2.],
                   [3., 4., 5.]])

        Alternatively, numpy automatically calls this function (via
        the magic :meth:`__array__` method) to convert Sage matrices
        to numpy arrays::

            sage: import numpy
            sage: m = matrix(RDF, 2, range(6)); m
            [0.0 1.0 2.0]
            [3.0 4.0 5.0]
            sage: numpy.array(m)
            array([[0., 1., 2.],
                   [3., 4., 5.]])
            sage: numpy.array(m).dtype
            dtype('float64')
            sage: m = matrix(CDF, 2, range(6)); m
            [0.0 1.0 2.0]
            [3.0 4.0 5.0]
            sage: numpy.array(m)
            array([[0.+0.j, 1.+0.j, 2.+0.j],
                   [3.+0.j, 4.+0.j, 5.+0.j]])
            sage: numpy.array(m).dtype
            dtype('complex128')

        TESTS::

            sage: m = matrix(RDF,0,5,[]); m
            []
            sage: m.numpy()
            array([], shape=(0, 5), dtype=float64)
            sage: m = matrix(RDF,5,0,[]); m
            []
            sage: m.numpy()
            array([], shape=(5, 0), dtype=float64)"""
    @overload
    def numpy(self) -> Any:
        """Matrix_numpy_dense.numpy(self, dtype=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_numpy_dense.pyx (starting at line 434)

        Return a copy of the matrix as a numpy array.

        It uses the numpy C/api so is very fast.

        INPUT:

        - ``dtype`` -- the desired data-type for the array. If not given,
          then the type will be determined as the minimum type required
          to hold the objects in the sequence.

        EXAMPLES::

            sage: m = matrix(RDF,[[1,2],[3,4]])
            sage: n = m.numpy()
            sage: import numpy
            sage: tuple(numpy.linalg.eig(n))
            (array([-0.37228132,  5.37228132]),
             array([[-0.82456484, -0.41597356],
                   [ 0.56576746, -0.90937671]]))
            sage: m = matrix(RDF, 2, range(6)); m
            [0.0 1.0 2.0]
            [3.0 4.0 5.0]
            sage: m.numpy()
            array([[0., 1., 2.],
                   [3., 4., 5.]])

        Alternatively, numpy automatically calls this function (via
        the magic :meth:`__array__` method) to convert Sage matrices
        to numpy arrays::

            sage: import numpy
            sage: m = matrix(RDF, 2, range(6)); m
            [0.0 1.0 2.0]
            [3.0 4.0 5.0]
            sage: numpy.array(m)
            array([[0., 1., 2.],
                   [3., 4., 5.]])
            sage: numpy.array(m).dtype
            dtype('float64')
            sage: m = matrix(CDF, 2, range(6)); m
            [0.0 1.0 2.0]
            [3.0 4.0 5.0]
            sage: numpy.array(m)
            array([[0.+0.j, 1.+0.j, 2.+0.j],
                   [3.+0.j, 4.+0.j, 5.+0.j]])
            sage: numpy.array(m).dtype
            dtype('complex128')

        TESTS::

            sage: m = matrix(RDF,0,5,[]); m
            []
            sage: m.numpy()
            array([], shape=(0, 5), dtype=float64)
            sage: m = matrix(RDF,5,0,[]); m
            []
            sage: m.numpy()
            array([], shape=(5, 0), dtype=float64)"""
    @overload
    def numpy(self) -> Any:
        """Matrix_numpy_dense.numpy(self, dtype=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_numpy_dense.pyx (starting at line 434)

        Return a copy of the matrix as a numpy array.

        It uses the numpy C/api so is very fast.

        INPUT:

        - ``dtype`` -- the desired data-type for the array. If not given,
          then the type will be determined as the minimum type required
          to hold the objects in the sequence.

        EXAMPLES::

            sage: m = matrix(RDF,[[1,2],[3,4]])
            sage: n = m.numpy()
            sage: import numpy
            sage: tuple(numpy.linalg.eig(n))
            (array([-0.37228132,  5.37228132]),
             array([[-0.82456484, -0.41597356],
                   [ 0.56576746, -0.90937671]]))
            sage: m = matrix(RDF, 2, range(6)); m
            [0.0 1.0 2.0]
            [3.0 4.0 5.0]
            sage: m.numpy()
            array([[0., 1., 2.],
                   [3., 4., 5.]])

        Alternatively, numpy automatically calls this function (via
        the magic :meth:`__array__` method) to convert Sage matrices
        to numpy arrays::

            sage: import numpy
            sage: m = matrix(RDF, 2, range(6)); m
            [0.0 1.0 2.0]
            [3.0 4.0 5.0]
            sage: numpy.array(m)
            array([[0., 1., 2.],
                   [3., 4., 5.]])
            sage: numpy.array(m).dtype
            dtype('float64')
            sage: m = matrix(CDF, 2, range(6)); m
            [0.0 1.0 2.0]
            [3.0 4.0 5.0]
            sage: numpy.array(m)
            array([[0.+0.j, 1.+0.j, 2.+0.j],
                   [3.+0.j, 4.+0.j, 5.+0.j]])
            sage: numpy.array(m).dtype
            dtype('complex128')

        TESTS::

            sage: m = matrix(RDF,0,5,[]); m
            []
            sage: m.numpy()
            array([], shape=(0, 5), dtype=float64)
            sage: m = matrix(RDF,5,0,[]); m
            []
            sage: m.numpy()
            array([], shape=(5, 0), dtype=float64)"""
    @overload
    def numpy(self) -> Any:
        """Matrix_numpy_dense.numpy(self, dtype=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_numpy_dense.pyx (starting at line 434)

        Return a copy of the matrix as a numpy array.

        It uses the numpy C/api so is very fast.

        INPUT:

        - ``dtype`` -- the desired data-type for the array. If not given,
          then the type will be determined as the minimum type required
          to hold the objects in the sequence.

        EXAMPLES::

            sage: m = matrix(RDF,[[1,2],[3,4]])
            sage: n = m.numpy()
            sage: import numpy
            sage: tuple(numpy.linalg.eig(n))
            (array([-0.37228132,  5.37228132]),
             array([[-0.82456484, -0.41597356],
                   [ 0.56576746, -0.90937671]]))
            sage: m = matrix(RDF, 2, range(6)); m
            [0.0 1.0 2.0]
            [3.0 4.0 5.0]
            sage: m.numpy()
            array([[0., 1., 2.],
                   [3., 4., 5.]])

        Alternatively, numpy automatically calls this function (via
        the magic :meth:`__array__` method) to convert Sage matrices
        to numpy arrays::

            sage: import numpy
            sage: m = matrix(RDF, 2, range(6)); m
            [0.0 1.0 2.0]
            [3.0 4.0 5.0]
            sage: numpy.array(m)
            array([[0., 1., 2.],
                   [3., 4., 5.]])
            sage: numpy.array(m).dtype
            dtype('float64')
            sage: m = matrix(CDF, 2, range(6)); m
            [0.0 1.0 2.0]
            [3.0 4.0 5.0]
            sage: numpy.array(m)
            array([[0.+0.j, 1.+0.j, 2.+0.j],
                   [3.+0.j, 4.+0.j, 5.+0.j]])
            sage: numpy.array(m).dtype
            dtype('complex128')

        TESTS::

            sage: m = matrix(RDF,0,5,[]); m
            []
            sage: m.numpy()
            array([], shape=(0, 5), dtype=float64)
            sage: m = matrix(RDF,5,0,[]); m
            []
            sage: m.numpy()
            array([], shape=(5, 0), dtype=float64)"""
    @overload
    def numpy(self) -> Any:
        """Matrix_numpy_dense.numpy(self, dtype=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_numpy_dense.pyx (starting at line 434)

        Return a copy of the matrix as a numpy array.

        It uses the numpy C/api so is very fast.

        INPUT:

        - ``dtype`` -- the desired data-type for the array. If not given,
          then the type will be determined as the minimum type required
          to hold the objects in the sequence.

        EXAMPLES::

            sage: m = matrix(RDF,[[1,2],[3,4]])
            sage: n = m.numpy()
            sage: import numpy
            sage: tuple(numpy.linalg.eig(n))
            (array([-0.37228132,  5.37228132]),
             array([[-0.82456484, -0.41597356],
                   [ 0.56576746, -0.90937671]]))
            sage: m = matrix(RDF, 2, range(6)); m
            [0.0 1.0 2.0]
            [3.0 4.0 5.0]
            sage: m.numpy()
            array([[0., 1., 2.],
                   [3., 4., 5.]])

        Alternatively, numpy automatically calls this function (via
        the magic :meth:`__array__` method) to convert Sage matrices
        to numpy arrays::

            sage: import numpy
            sage: m = matrix(RDF, 2, range(6)); m
            [0.0 1.0 2.0]
            [3.0 4.0 5.0]
            sage: numpy.array(m)
            array([[0., 1., 2.],
                   [3., 4., 5.]])
            sage: numpy.array(m).dtype
            dtype('float64')
            sage: m = matrix(CDF, 2, range(6)); m
            [0.0 1.0 2.0]
            [3.0 4.0 5.0]
            sage: numpy.array(m)
            array([[0.+0.j, 1.+0.j, 2.+0.j],
                   [3.+0.j, 4.+0.j, 5.+0.j]])
            sage: numpy.array(m).dtype
            dtype('complex128')

        TESTS::

            sage: m = matrix(RDF,0,5,[]); m
            []
            sage: m.numpy()
            array([], shape=(0, 5), dtype=float64)
            sage: m = matrix(RDF,5,0,[]); m
            []
            sage: m.numpy()
            array([], shape=(5, 0), dtype=float64)"""
    @overload
    def transpose(self) -> Any:
        """Matrix_numpy_dense.transpose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_numpy_dense.pyx (starting at line 280)

        Return the transpose of this matrix, without changing ``self``.

        EXAMPLES::

            sage: m = matrix(RDF,2,3,range(6)); m
            [0.0 1.0 2.0]
            [3.0 4.0 5.0]
            sage: m2 = m.transpose()
            sage: m[0,0] = 2
            sage: m2           #note that m2 hasn't changed
            [0.0 3.0]
            [1.0 4.0]
            [2.0 5.0]

        ``.T`` is a convenient shortcut for the transpose::

            sage: m.T
            [2.0 3.0]
            [1.0 4.0]
            [2.0 5.0]

            sage: m = matrix(RDF,0,3); m
            []
            sage: m.transpose()
            []
            sage: m.transpose().parent()
            Full MatrixSpace of 3 by 0 dense matrices over Real Double Field

        TESTS::

            sage: m = matrix(RDF,2,3,range(6))
            sage: m.subdivide([1],[2])
            sage: m
            [0.0 1.0|2.0]
            [-------+---]
            [3.0 4.0|5.0]
            sage: m.transpose()
            [0.0|3.0]
            [1.0|4.0]
            [---+---]
            [2.0|5.0]

            sage: m = matrix(RDF,0,2)
            sage: m.subdivide([],[1])
            sage: m.subdivisions()
            ([], [1])
            sage: m.transpose().subdivisions()
            ([1], [])

            sage: m = matrix(RDF,2,0)
            sage: m.subdivide([1],[])
            sage: m.subdivisions()
            ([1], [])
            sage: m.transpose().subdivisions()
            ([], [1])"""
    @overload
    def transpose(self) -> Any:
        """Matrix_numpy_dense.transpose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_numpy_dense.pyx (starting at line 280)

        Return the transpose of this matrix, without changing ``self``.

        EXAMPLES::

            sage: m = matrix(RDF,2,3,range(6)); m
            [0.0 1.0 2.0]
            [3.0 4.0 5.0]
            sage: m2 = m.transpose()
            sage: m[0,0] = 2
            sage: m2           #note that m2 hasn't changed
            [0.0 3.0]
            [1.0 4.0]
            [2.0 5.0]

        ``.T`` is a convenient shortcut for the transpose::

            sage: m.T
            [2.0 3.0]
            [1.0 4.0]
            [2.0 5.0]

            sage: m = matrix(RDF,0,3); m
            []
            sage: m.transpose()
            []
            sage: m.transpose().parent()
            Full MatrixSpace of 3 by 0 dense matrices over Real Double Field

        TESTS::

            sage: m = matrix(RDF,2,3,range(6))
            sage: m.subdivide([1],[2])
            sage: m
            [0.0 1.0|2.0]
            [-------+---]
            [3.0 4.0|5.0]
            sage: m.transpose()
            [0.0|3.0]
            [1.0|4.0]
            [---+---]
            [2.0|5.0]

            sage: m = matrix(RDF,0,2)
            sage: m.subdivide([],[1])
            sage: m.subdivisions()
            ([], [1])
            sage: m.transpose().subdivisions()
            ([1], [])

            sage: m = matrix(RDF,2,0)
            sage: m.subdivide([1],[])
            sage: m.subdivisions()
            ([1], [])
            sage: m.transpose().subdivisions()
            ([], [1])"""
    @overload
    def transpose(self) -> Any:
        """Matrix_numpy_dense.transpose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_numpy_dense.pyx (starting at line 280)

        Return the transpose of this matrix, without changing ``self``.

        EXAMPLES::

            sage: m = matrix(RDF,2,3,range(6)); m
            [0.0 1.0 2.0]
            [3.0 4.0 5.0]
            sage: m2 = m.transpose()
            sage: m[0,0] = 2
            sage: m2           #note that m2 hasn't changed
            [0.0 3.0]
            [1.0 4.0]
            [2.0 5.0]

        ``.T`` is a convenient shortcut for the transpose::

            sage: m.T
            [2.0 3.0]
            [1.0 4.0]
            [2.0 5.0]

            sage: m = matrix(RDF,0,3); m
            []
            sage: m.transpose()
            []
            sage: m.transpose().parent()
            Full MatrixSpace of 3 by 0 dense matrices over Real Double Field

        TESTS::

            sage: m = matrix(RDF,2,3,range(6))
            sage: m.subdivide([1],[2])
            sage: m
            [0.0 1.0|2.0]
            [-------+---]
            [3.0 4.0|5.0]
            sage: m.transpose()
            [0.0|3.0]
            [1.0|4.0]
            [---+---]
            [2.0|5.0]

            sage: m = matrix(RDF,0,2)
            sage: m.subdivide([],[1])
            sage: m.subdivisions()
            ([], [1])
            sage: m.transpose().subdivisions()
            ([1], [])

            sage: m = matrix(RDF,2,0)
            sage: m.subdivide([1],[])
            sage: m.subdivisions()
            ([1], [])
            sage: m.transpose().subdivisions()
            ([], [1])"""
    @overload
    def transpose(self) -> Any:
        """Matrix_numpy_dense.transpose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_numpy_dense.pyx (starting at line 280)

        Return the transpose of this matrix, without changing ``self``.

        EXAMPLES::

            sage: m = matrix(RDF,2,3,range(6)); m
            [0.0 1.0 2.0]
            [3.0 4.0 5.0]
            sage: m2 = m.transpose()
            sage: m[0,0] = 2
            sage: m2           #note that m2 hasn't changed
            [0.0 3.0]
            [1.0 4.0]
            [2.0 5.0]

        ``.T`` is a convenient shortcut for the transpose::

            sage: m.T
            [2.0 3.0]
            [1.0 4.0]
            [2.0 5.0]

            sage: m = matrix(RDF,0,3); m
            []
            sage: m.transpose()
            []
            sage: m.transpose().parent()
            Full MatrixSpace of 3 by 0 dense matrices over Real Double Field

        TESTS::

            sage: m = matrix(RDF,2,3,range(6))
            sage: m.subdivide([1],[2])
            sage: m
            [0.0 1.0|2.0]
            [-------+---]
            [3.0 4.0|5.0]
            sage: m.transpose()
            [0.0|3.0]
            [1.0|4.0]
            [---+---]
            [2.0|5.0]

            sage: m = matrix(RDF,0,2)
            sage: m.subdivide([],[1])
            sage: m.subdivisions()
            ([], [1])
            sage: m.transpose().subdivisions()
            ([1], [])

            sage: m = matrix(RDF,2,0)
            sage: m.subdivide([1],[])
            sage: m.subdivisions()
            ([1], [])
            sage: m.transpose().subdivisions()
            ([], [1])"""
    @overload
    def transpose(self) -> Any:
        """Matrix_numpy_dense.transpose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_numpy_dense.pyx (starting at line 280)

        Return the transpose of this matrix, without changing ``self``.

        EXAMPLES::

            sage: m = matrix(RDF,2,3,range(6)); m
            [0.0 1.0 2.0]
            [3.0 4.0 5.0]
            sage: m2 = m.transpose()
            sage: m[0,0] = 2
            sage: m2           #note that m2 hasn't changed
            [0.0 3.0]
            [1.0 4.0]
            [2.0 5.0]

        ``.T`` is a convenient shortcut for the transpose::

            sage: m.T
            [2.0 3.0]
            [1.0 4.0]
            [2.0 5.0]

            sage: m = matrix(RDF,0,3); m
            []
            sage: m.transpose()
            []
            sage: m.transpose().parent()
            Full MatrixSpace of 3 by 0 dense matrices over Real Double Field

        TESTS::

            sage: m = matrix(RDF,2,3,range(6))
            sage: m.subdivide([1],[2])
            sage: m
            [0.0 1.0|2.0]
            [-------+---]
            [3.0 4.0|5.0]
            sage: m.transpose()
            [0.0|3.0]
            [1.0|4.0]
            [---+---]
            [2.0|5.0]

            sage: m = matrix(RDF,0,2)
            sage: m.subdivide([],[1])
            sage: m.subdivisions()
            ([], [1])
            sage: m.transpose().subdivisions()
            ([1], [])

            sage: m = matrix(RDF,2,0)
            sage: m.subdivide([1],[])
            sage: m.subdivisions()
            ([1], [])
            sage: m.transpose().subdivisions()
            ([], [1])"""
    @overload
    def transpose(self) -> Any:
        """Matrix_numpy_dense.transpose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_numpy_dense.pyx (starting at line 280)

        Return the transpose of this matrix, without changing ``self``.

        EXAMPLES::

            sage: m = matrix(RDF,2,3,range(6)); m
            [0.0 1.0 2.0]
            [3.0 4.0 5.0]
            sage: m2 = m.transpose()
            sage: m[0,0] = 2
            sage: m2           #note that m2 hasn't changed
            [0.0 3.0]
            [1.0 4.0]
            [2.0 5.0]

        ``.T`` is a convenient shortcut for the transpose::

            sage: m.T
            [2.0 3.0]
            [1.0 4.0]
            [2.0 5.0]

            sage: m = matrix(RDF,0,3); m
            []
            sage: m.transpose()
            []
            sage: m.transpose().parent()
            Full MatrixSpace of 3 by 0 dense matrices over Real Double Field

        TESTS::

            sage: m = matrix(RDF,2,3,range(6))
            sage: m.subdivide([1],[2])
            sage: m
            [0.0 1.0|2.0]
            [-------+---]
            [3.0 4.0|5.0]
            sage: m.transpose()
            [0.0|3.0]
            [1.0|4.0]
            [---+---]
            [2.0|5.0]

            sage: m = matrix(RDF,0,2)
            sage: m.subdivide([],[1])
            sage: m.subdivisions()
            ([], [1])
            sage: m.transpose().subdivisions()
            ([1], [])

            sage: m = matrix(RDF,2,0)
            sage: m.subdivide([1],[])
            sage: m.subdivisions()
            ([1], [])
            sage: m.transpose().subdivisions()
            ([], [1])"""
    @overload
    def transpose(self) -> Any:
        """Matrix_numpy_dense.transpose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_numpy_dense.pyx (starting at line 280)

        Return the transpose of this matrix, without changing ``self``.

        EXAMPLES::

            sage: m = matrix(RDF,2,3,range(6)); m
            [0.0 1.0 2.0]
            [3.0 4.0 5.0]
            sage: m2 = m.transpose()
            sage: m[0,0] = 2
            sage: m2           #note that m2 hasn't changed
            [0.0 3.0]
            [1.0 4.0]
            [2.0 5.0]

        ``.T`` is a convenient shortcut for the transpose::

            sage: m.T
            [2.0 3.0]
            [1.0 4.0]
            [2.0 5.0]

            sage: m = matrix(RDF,0,3); m
            []
            sage: m.transpose()
            []
            sage: m.transpose().parent()
            Full MatrixSpace of 3 by 0 dense matrices over Real Double Field

        TESTS::

            sage: m = matrix(RDF,2,3,range(6))
            sage: m.subdivide([1],[2])
            sage: m
            [0.0 1.0|2.0]
            [-------+---]
            [3.0 4.0|5.0]
            sage: m.transpose()
            [0.0|3.0]
            [1.0|4.0]
            [---+---]
            [2.0|5.0]

            sage: m = matrix(RDF,0,2)
            sage: m.subdivide([],[1])
            sage: m.subdivisions()
            ([], [1])
            sage: m.transpose().subdivisions()
            ([1], [])

            sage: m = matrix(RDF,2,0)
            sage: m.subdivide([1],[])
            sage: m.subdivisions()
            ([1], [])
            sage: m.transpose().subdivisions()
            ([], [1])"""
    @overload
    def __copy__(self) -> Any:
        """Matrix_numpy_dense.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_numpy_dense.pyx (starting at line 243)

        Return a new copy of this matrix.

        EXAMPLES::

            sage: a = matrix(RDF,1,3, [1,2,-3])
            sage: a
            [ 1.0  2.0 -3.0]
            sage: b = a.__copy__()
            sage: b
            [ 1.0  2.0 -3.0]
            sage: b is a
            False
            sage: b == a
            True
            sage: b[0,0] = 3
            sage: a[0,0] # note that a hasn't changed
            1.0

        ::

            sage: copy(MatrixSpace(RDF,0,0,sparse=False).zero_matrix())
            []"""
    @overload
    def __copy__(self) -> Any:
        """Matrix_numpy_dense.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_numpy_dense.pyx (starting at line 243)

        Return a new copy of this matrix.

        EXAMPLES::

            sage: a = matrix(RDF,1,3, [1,2,-3])
            sage: a
            [ 1.0  2.0 -3.0]
            sage: b = a.__copy__()
            sage: b
            [ 1.0  2.0 -3.0]
            sage: b is a
            False
            sage: b == a
            True
            sage: b[0,0] = 3
            sage: a[0,0] # note that a hasn't changed
            1.0

        ::

            sage: copy(MatrixSpace(RDF,0,0,sparse=False).zero_matrix())
            []"""
    @overload
    def __create_matrix__(self) -> Any:
        """Matrix_numpy_dense.__create_matrix__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_numpy_dense.pyx (starting at line 57)

        Create a new uninitialized numpy matrix to hold the data for the class.

        This function assumes that self._numpy_dtypeint and
        self._nrows and self._ncols have already been initialized.

        EXAMPLES:

        In this example, we throw away the current matrix and make a
        new uninitialized matrix representing the data for the class::

            sage: a = matrix(RDF, 3, range(9))
            sage: a.__create_matrix__()"""
    @overload
    def __create_matrix__(self) -> Any:
        """Matrix_numpy_dense.__create_matrix__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_numpy_dense.pyx (starting at line 57)

        Create a new uninitialized numpy matrix to hold the data for the class.

        This function assumes that self._numpy_dtypeint and
        self._nrows and self._ncols have already been initialized.

        EXAMPLES:

        In this example, we throw away the current matrix and make a
        new uninitialized matrix representing the data for the class::

            sage: a = matrix(RDF, 3, range(9))
            sage: a.__create_matrix__()"""
