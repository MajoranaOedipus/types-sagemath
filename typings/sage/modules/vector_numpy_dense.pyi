import sage.modules.free_module_element
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

class Vector_numpy_dense(sage.modules.free_module_element.FreeModuleElement):
    """Vector_numpy_dense(parent, entries, coerce=True, copy=True)

    File: /build/sagemath/src/sage/src/sage/modules/vector_numpy_dense.pyx (starting at line 38)

    Base class for vectors implemented using numpy arrays.

    This class cannot be instantiated on its own.  The numpy vector
    creation depends on several variables that are set in the
    subclasses.

    EXAMPLES::

        sage: v = vector(RDF, [1,2,3,4]); v
        (1.0, 2.0, 3.0, 4.0)
        sage: v*v
        30.0"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, entries, coerce=..., copy=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/modules/vector_numpy_dense.pyx (starting at line 131)

                Fill the vector with entries.

                The numpy array must have already been allocated.

                EXAMPLES::

                    sage: vector(RDF, range(9))
                    (0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0)
                    sage: vector(CDF, 5)
                    (0.0, 0.0, 0.0, 0.0, 0.0)

                TESTS::

                    sage: vector(CDF, 0)
                    ()
                    sage: vector(RDF, 0)
                    ()
                    sage: vector(CDF, 4)
                    (0.0, 0.0, 0.0, 0.0)
                    sage: vector(RDF, 4)
                    (0.0, 0.0, 0.0, 0.0)
                    sage: vector(CDF, [CDF(1+I)*j for j in range(4)])                           # needs sage.symbolic
                    (0.0, 1.0 + 1.0*I, 2.0 + 2.0*I, 3.0 + 3.0*I)
                    sage: vector(RDF, 4, range(4))
                    (0.0, 1.0, 2.0, 3.0)

                    sage: V = RDF^2
                    sage: V.element_class(V, 5)
                    Traceback (most recent call last):
                    ...
                    TypeError: entries must be a list or 0
                    sage: V.element_class(V, 0)
                    (0.0, 0.0)
        """
    @overload
    def numpy(self, dtype=...) -> Any:
        """Vector_numpy_dense.numpy(self, dtype=None)

        File: /build/sagemath/src/sage/src/sage/modules/vector_numpy_dense.pyx (starting at line 263)

        Return numpy array corresponding to this vector.

        INPUT:

        - ``dtype`` -- if specified, the `numpy dtype
          <http://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html>`_ of
          the returned array

        EXAMPLES::

            sage: v = vector(CDF,4,range(4))
            sage: v.numpy()
            array([0.+0.j, 1.+0.j, 2.+0.j, 3.+0.j])
            sage: v = vector(CDF,0)
            sage: v.numpy()
            array([], dtype=complex128)
            sage: v = vector(RDF,4,range(4))
            sage: v.numpy()
            array([0., 1., 2., 3.])
            sage: v = vector(RDF,0)
            sage: v.numpy()
            array([], dtype=float64)

        A numpy dtype may be requested manually::

            sage: import numpy
            sage: v = vector(CDF, 3, range(3))
            sage: v.numpy()
            array([0.+0.j, 1.+0.j, 2.+0.j])
            sage: v.numpy(dtype=numpy.float64)
            array([0., 1., 2.])
            sage: v.numpy(dtype=numpy.float32)
            array([0., 1., 2.], dtype=float32)"""
    @overload
    def numpy(self) -> Any:
        """Vector_numpy_dense.numpy(self, dtype=None)

        File: /build/sagemath/src/sage/src/sage/modules/vector_numpy_dense.pyx (starting at line 263)

        Return numpy array corresponding to this vector.

        INPUT:

        - ``dtype`` -- if specified, the `numpy dtype
          <http://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html>`_ of
          the returned array

        EXAMPLES::

            sage: v = vector(CDF,4,range(4))
            sage: v.numpy()
            array([0.+0.j, 1.+0.j, 2.+0.j, 3.+0.j])
            sage: v = vector(CDF,0)
            sage: v.numpy()
            array([], dtype=complex128)
            sage: v = vector(RDF,4,range(4))
            sage: v.numpy()
            array([0., 1., 2., 3.])
            sage: v = vector(RDF,0)
            sage: v.numpy()
            array([], dtype=float64)

        A numpy dtype may be requested manually::

            sage: import numpy
            sage: v = vector(CDF, 3, range(3))
            sage: v.numpy()
            array([0.+0.j, 1.+0.j, 2.+0.j])
            sage: v.numpy(dtype=numpy.float64)
            array([0., 1., 2.])
            sage: v.numpy(dtype=numpy.float32)
            array([0., 1., 2.], dtype=float32)"""
    @overload
    def numpy(self) -> Any:
        """Vector_numpy_dense.numpy(self, dtype=None)

        File: /build/sagemath/src/sage/src/sage/modules/vector_numpy_dense.pyx (starting at line 263)

        Return numpy array corresponding to this vector.

        INPUT:

        - ``dtype`` -- if specified, the `numpy dtype
          <http://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html>`_ of
          the returned array

        EXAMPLES::

            sage: v = vector(CDF,4,range(4))
            sage: v.numpy()
            array([0.+0.j, 1.+0.j, 2.+0.j, 3.+0.j])
            sage: v = vector(CDF,0)
            sage: v.numpy()
            array([], dtype=complex128)
            sage: v = vector(RDF,4,range(4))
            sage: v.numpy()
            array([0., 1., 2., 3.])
            sage: v = vector(RDF,0)
            sage: v.numpy()
            array([], dtype=float64)

        A numpy dtype may be requested manually::

            sage: import numpy
            sage: v = vector(CDF, 3, range(3))
            sage: v.numpy()
            array([0.+0.j, 1.+0.j, 2.+0.j])
            sage: v.numpy(dtype=numpy.float64)
            array([0., 1., 2.])
            sage: v.numpy(dtype=numpy.float32)
            array([0., 1., 2.], dtype=float32)"""
    @overload
    def numpy(self) -> Any:
        """Vector_numpy_dense.numpy(self, dtype=None)

        File: /build/sagemath/src/sage/src/sage/modules/vector_numpy_dense.pyx (starting at line 263)

        Return numpy array corresponding to this vector.

        INPUT:

        - ``dtype`` -- if specified, the `numpy dtype
          <http://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html>`_ of
          the returned array

        EXAMPLES::

            sage: v = vector(CDF,4,range(4))
            sage: v.numpy()
            array([0.+0.j, 1.+0.j, 2.+0.j, 3.+0.j])
            sage: v = vector(CDF,0)
            sage: v.numpy()
            array([], dtype=complex128)
            sage: v = vector(RDF,4,range(4))
            sage: v.numpy()
            array([0., 1., 2., 3.])
            sage: v = vector(RDF,0)
            sage: v.numpy()
            array([], dtype=float64)

        A numpy dtype may be requested manually::

            sage: import numpy
            sage: v = vector(CDF, 3, range(3))
            sage: v.numpy()
            array([0.+0.j, 1.+0.j, 2.+0.j])
            sage: v.numpy(dtype=numpy.float64)
            array([0., 1., 2.])
            sage: v.numpy(dtype=numpy.float32)
            array([0., 1., 2.], dtype=float32)"""
    @overload
    def numpy(self) -> Any:
        """Vector_numpy_dense.numpy(self, dtype=None)

        File: /build/sagemath/src/sage/src/sage/modules/vector_numpy_dense.pyx (starting at line 263)

        Return numpy array corresponding to this vector.

        INPUT:

        - ``dtype`` -- if specified, the `numpy dtype
          <http://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html>`_ of
          the returned array

        EXAMPLES::

            sage: v = vector(CDF,4,range(4))
            sage: v.numpy()
            array([0.+0.j, 1.+0.j, 2.+0.j, 3.+0.j])
            sage: v = vector(CDF,0)
            sage: v.numpy()
            array([], dtype=complex128)
            sage: v = vector(RDF,4,range(4))
            sage: v.numpy()
            array([0., 1., 2., 3.])
            sage: v = vector(RDF,0)
            sage: v.numpy()
            array([], dtype=float64)

        A numpy dtype may be requested manually::

            sage: import numpy
            sage: v = vector(CDF, 3, range(3))
            sage: v.numpy()
            array([0.+0.j, 1.+0.j, 2.+0.j])
            sage: v.numpy(dtype=numpy.float64)
            array([0., 1., 2.])
            sage: v.numpy(dtype=numpy.float32)
            array([0., 1., 2.], dtype=float32)"""
    @overload
    def numpy(self) -> Any:
        """Vector_numpy_dense.numpy(self, dtype=None)

        File: /build/sagemath/src/sage/src/sage/modules/vector_numpy_dense.pyx (starting at line 263)

        Return numpy array corresponding to this vector.

        INPUT:

        - ``dtype`` -- if specified, the `numpy dtype
          <http://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html>`_ of
          the returned array

        EXAMPLES::

            sage: v = vector(CDF,4,range(4))
            sage: v.numpy()
            array([0.+0.j, 1.+0.j, 2.+0.j, 3.+0.j])
            sage: v = vector(CDF,0)
            sage: v.numpy()
            array([], dtype=complex128)
            sage: v = vector(RDF,4,range(4))
            sage: v.numpy()
            array([0., 1., 2., 3.])
            sage: v = vector(RDF,0)
            sage: v.numpy()
            array([], dtype=float64)

        A numpy dtype may be requested manually::

            sage: import numpy
            sage: v = vector(CDF, 3, range(3))
            sage: v.numpy()
            array([0.+0.j, 1.+0.j, 2.+0.j])
            sage: v.numpy(dtype=numpy.float64)
            array([0., 1., 2.])
            sage: v.numpy(dtype=numpy.float32)
            array([0., 1., 2.], dtype=float32)"""
    @overload
    def numpy(self, dtype=...) -> Any:
        """Vector_numpy_dense.numpy(self, dtype=None)

        File: /build/sagemath/src/sage/src/sage/modules/vector_numpy_dense.pyx (starting at line 263)

        Return numpy array corresponding to this vector.

        INPUT:

        - ``dtype`` -- if specified, the `numpy dtype
          <http://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html>`_ of
          the returned array

        EXAMPLES::

            sage: v = vector(CDF,4,range(4))
            sage: v.numpy()
            array([0.+0.j, 1.+0.j, 2.+0.j, 3.+0.j])
            sage: v = vector(CDF,0)
            sage: v.numpy()
            array([], dtype=complex128)
            sage: v = vector(RDF,4,range(4))
            sage: v.numpy()
            array([0., 1., 2., 3.])
            sage: v = vector(RDF,0)
            sage: v.numpy()
            array([], dtype=float64)

        A numpy dtype may be requested manually::

            sage: import numpy
            sage: v = vector(CDF, 3, range(3))
            sage: v.numpy()
            array([0.+0.j, 1.+0.j, 2.+0.j])
            sage: v.numpy(dtype=numpy.float64)
            array([0., 1., 2.])
            sage: v.numpy(dtype=numpy.float32)
            array([0., 1., 2.], dtype=float32)"""
    @overload
    def numpy(self, dtype=...) -> Any:
        """Vector_numpy_dense.numpy(self, dtype=None)

        File: /build/sagemath/src/sage/src/sage/modules/vector_numpy_dense.pyx (starting at line 263)

        Return numpy array corresponding to this vector.

        INPUT:

        - ``dtype`` -- if specified, the `numpy dtype
          <http://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html>`_ of
          the returned array

        EXAMPLES::

            sage: v = vector(CDF,4,range(4))
            sage: v.numpy()
            array([0.+0.j, 1.+0.j, 2.+0.j, 3.+0.j])
            sage: v = vector(CDF,0)
            sage: v.numpy()
            array([], dtype=complex128)
            sage: v = vector(RDF,4,range(4))
            sage: v.numpy()
            array([0., 1., 2., 3.])
            sage: v = vector(RDF,0)
            sage: v.numpy()
            array([], dtype=float64)

        A numpy dtype may be requested manually::

            sage: import numpy
            sage: v = vector(CDF, 3, range(3))
            sage: v.numpy()
            array([0.+0.j, 1.+0.j, 2.+0.j])
            sage: v.numpy(dtype=numpy.float64)
            array([0., 1., 2.])
            sage: v.numpy(dtype=numpy.float32)
            array([0., 1., 2.], dtype=float32)"""
    def __copy__(self, copy=...) -> Any:
        """Vector_numpy_dense.__copy__(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/modules/vector_numpy_dense.pyx (starting at line 116)

        Return a copy of the vector.

        EXAMPLES::

            sage: a = vector(RDF, range(9))
            sage: a == copy(a)
            True"""
    @overload
    def __create_vector__(self) -> Any:
        """Vector_numpy_dense.__create_vector__(self)

        File: /build/sagemath/src/sage/src/sage/modules/vector_numpy_dense.pyx (starting at line 84)

        Create a new uninitialized numpy array to hold the data for the class.

        This function assumes that self._numpy_dtypeint and
        self._nrows and self._ncols have already been initialized.

        EXAMPLES:

        In this example, we throw away the current array and make a
        new uninitialized array representing the data for the class. ::

            sage: a=vector(RDF, range(9))
            sage: a.__create_vector__()"""
    @overload
    def __create_vector__(self) -> Any:
        """Vector_numpy_dense.__create_vector__(self)

        File: /build/sagemath/src/sage/src/sage/modules/vector_numpy_dense.pyx (starting at line 84)

        Create a new uninitialized numpy array to hold the data for the class.

        This function assumes that self._numpy_dtypeint and
        self._nrows and self._ncols have already been initialized.

        EXAMPLES:

        In this example, we throw away the current array and make a
        new uninitialized array representing the data for the class. ::

            sage: a=vector(RDF, range(9))
            sage: a.__create_vector__()"""
    def __len__(self) -> Any:
        """Vector_numpy_dense.__len__(self)

        File: /build/sagemath/src/sage/src/sage/modules/vector_numpy_dense.pyx (starting at line 197)

        Return the length of the vector.

        EXAMPLES::

            sage: v = vector(RDF, 5); v
            (0.0, 0.0, 0.0, 0.0, 0.0)
            sage: len(v)
            5"""
