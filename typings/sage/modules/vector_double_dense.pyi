import sage.modules.vector_numpy_dense
from sage.categories.category import CDF as CDF, RDF as RDF
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

class Vector_double_dense(sage.modules.vector_numpy_dense.Vector_numpy_dense):
    """File: /build/sagemath/src/sage/src/sage/modules/vector_double_dense.pyx (starting at line 65)

        Base class for vectors over the Real Double Field and the Complex
        Double Field.  These are supposed to be fast vector operations
        using C doubles. Most operations are implemented using numpy which
        will call the underlying BLAS, if needed, on the system.

        This class cannot be instantiated on its own.  The numpy vector
        creation depends on several variables that are set in the
        subclasses.

        EXAMPLES::

            sage: v = vector(RDF, [1,2,3,4]); v
            (1.0, 2.0, 3.0, 4.0)
            sage: v*v
            30.0
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def complex_vector(self) -> Any:
        """Vector_double_dense.complex_vector(self)

        File: /build/sagemath/src/sage/src/sage/modules/vector_double_dense.pyx (starting at line 295)

        Return the associated complex vector, i.e., this vector but with
        coefficients viewed as complex numbers.

        EXAMPLES::

            sage: v = vector(RDF,4,range(4)); v
            (0.0, 1.0, 2.0, 3.0)
            sage: v.complex_vector()
            (0.0, 1.0, 2.0, 3.0)
            sage: v = vector(RDF,0)
            sage: v.complex_vector()
            ()"""
    @overload
    def complex_vector(self) -> Any:
        """Vector_double_dense.complex_vector(self)

        File: /build/sagemath/src/sage/src/sage/modules/vector_double_dense.pyx (starting at line 295)

        Return the associated complex vector, i.e., this vector but with
        coefficients viewed as complex numbers.

        EXAMPLES::

            sage: v = vector(RDF,4,range(4)); v
            (0.0, 1.0, 2.0, 3.0)
            sage: v.complex_vector()
            (0.0, 1.0, 2.0, 3.0)
            sage: v = vector(RDF,0)
            sage: v.complex_vector()
            ()"""
    @overload
    def complex_vector(self) -> Any:
        """Vector_double_dense.complex_vector(self)

        File: /build/sagemath/src/sage/src/sage/modules/vector_double_dense.pyx (starting at line 295)

        Return the associated complex vector, i.e., this vector but with
        coefficients viewed as complex numbers.

        EXAMPLES::

            sage: v = vector(RDF,4,range(4)); v
            (0.0, 1.0, 2.0, 3.0)
            sage: v.complex_vector()
            (0.0, 1.0, 2.0, 3.0)
            sage: v = vector(RDF,0)
            sage: v.complex_vector()
            ()"""
    def fft(self, direction=..., algorithm=..., inplace=...) -> Any:
        """Vector_double_dense.fft(self, direction='forward', algorithm='radix2', inplace=False)

        File: /build/sagemath/src/sage/src/sage/modules/vector_double_dense.pyx (starting at line 222)

        This performs a fast Fourier transform on the vector.

        INPUT:

        - ``direction`` -- string; ``'forward'`` (default) or ``'backward'``

        The algorithm and inplace arguments are ignored.

        This function is fastest if the vector's length is a power of 2.

        EXAMPLES::

            sage: # needs scipy
            sage: v = vector(CDF,[1+2*I,2,3*I,4])
            sage: v.fft()
            (7.0 + 5.0*I, 1.0 + 1.0*I, -5.0 + 5.0*I, 1.0 - 3.0*I)
            sage: v.fft(direction='backward')
            (1.75 + 1.25*I, 0.25 - 0.75*I, -1.25 + 1.25*I, 0.25 + 0.25*I)
            sage: v.fft().fft(direction='backward')
            (1.0 + 2.0*I, 2.0, 3.0*I, 4.0)
            sage: v.fft().parent()
            Vector space of dimension 4 over Complex Double Field
            sage: v.fft(inplace=True)
            sage: v
            (7.0 + 5.0*I, 1.0 + 1.0*I, -5.0 + 5.0*I, 1.0 - 3.0*I)

            sage: # needs scipy
            sage: v = vector(RDF,4,range(4)); v
            (0.0, 1.0, 2.0, 3.0)
            sage: v.fft()
            (6.0, -2.0 + 2.0*I, -2.0, -2.0 - 2.0*I)
            sage: v.fft(direction='backward')
            (1.5, -0.5 - 0.5*I, -0.5, -0.5 + 0.5*I)
            sage: v.fft().fft(direction='backward')
            (0.0, 1.0, 2.0, 3.0)
            sage: v.fft().parent()
            Vector space of dimension 4 over Complex Double Field
            sage: v.fft(inplace=True)
            Traceback (most recent call last):
            ...
            ValueError: inplace can only be True for CDF vectors"""
    def inv_fft(self, algorithm=..., inplace=...) -> Any:
        """Vector_double_dense.inv_fft(self, algorithm='radix2', inplace=False)

        File: /build/sagemath/src/sage/src/sage/modules/vector_double_dense.pyx (starting at line 203)

        This performs the inverse fast Fourier transform on the vector.

        The Fourier transform can be done in place using the keyword
        inplace=True

        This will be fastest if the vector's length is a power of 2.

        EXAMPLES::

            sage: # needs scipy
            sage: v = vector(CDF,[1,2,3,4])
            sage: w = v.fft()
            sage: max(v - w.inv_fft()) < 1e-12
            True"""
    @overload
    def mean(self) -> Any:
        """Vector_double_dense.mean(self)

        File: /build/sagemath/src/sage/src/sage/modules/vector_double_dense.pyx (starting at line 478)

        Calculate the arithmetic mean of the vector.

        EXAMPLES::

            sage: v = vector(RDF, range(9))
            sage: w = vector(CDF, [k+(9-k)*I for k in range(9)])
            sage: v.mean()
            4.0
            sage: w.mean()
            4.0 + 5.0*I"""
    @overload
    def mean(self) -> Any:
        """Vector_double_dense.mean(self)

        File: /build/sagemath/src/sage/src/sage/modules/vector_double_dense.pyx (starting at line 478)

        Calculate the arithmetic mean of the vector.

        EXAMPLES::

            sage: v = vector(RDF, range(9))
            sage: w = vector(CDF, [k+(9-k)*I for k in range(9)])
            sage: v.mean()
            4.0
            sage: w.mean()
            4.0 + 5.0*I"""
    @overload
    def mean(self) -> Any:
        """Vector_double_dense.mean(self)

        File: /build/sagemath/src/sage/src/sage/modules/vector_double_dense.pyx (starting at line 478)

        Calculate the arithmetic mean of the vector.

        EXAMPLES::

            sage: v = vector(RDF, range(9))
            sage: w = vector(CDF, [k+(9-k)*I for k in range(9)])
            sage: v.mean()
            4.0
            sage: w.mean()
            4.0 + 5.0*I"""
    @overload
    def norm(self, p=...) -> Any:
        '''Vector_double_dense.norm(self, p=2)

        File: /build/sagemath/src/sage/src/sage/modules/vector_double_dense.pyx (starting at line 360)

        Return the norm (or related computations) of the vector.

        INPUT:

        - ``p`` -- (default: 2) controls which norm is computed,
          allowable values are any real number and positive and
          negative infinity.  See output discussion for specifics.

        OUTPUT:

        Returned value is a double precision floating point value
        in ``RDF`` (or an integer when ``p=0``).  The default value
        of ``p = 2`` is the "usual" Euclidean norm.  For other values:

        - ``p = Infinity`` or ``p = oo``: the maximum of the
          absolute values of the entries, where the absolute value
          of the complex number `a+bi` is `\\sqrt{a^2+b^2}`
        - ``p = -Infinity`` or ``p = -oo``: the minimum of the
          absolute values of the entries
        - ``p = 0``: the number of nonzero entries in the vector
        - ``p`` any other real number: for a vector `\\vec{x}` this method computes

          .. MATH::

                \\left(\\sum_i x_i^p\\right)^{1/p}

          For ``p < 0`` this function is not a norm, but the above
          computation may be useful for other purposes.

        ALGORITHM:

        Computation is performed by the :func:`~scipy:scipy.linalg.norm`
        function of the SciPy/NumPy library.

        EXAMPLES:

        First over the reals.  ::

            sage: v = vector(RDF, range(9))
            sage: v.norm()
            14.28285685...
            sage: v.norm(p=2)
            14.28285685...
            sage: v.norm(p=6)
            8.744039097...
            sage: v.norm(p=Infinity)
            8.0
            sage: v.norm(p=-oo)
            0.0
            sage: v.norm(p=0)
            8.0
            sage: v.norm(p=0.3)
            4099.153615...

        And over the complex numbers.  ::

            sage: w = vector(CDF, [3-4*I, 0, 5+12*I])
            sage: w.norm()
            13.9283882...
            sage: w.norm(p=2)
            13.9283882...
            sage: w.norm(p=0)
            2.0
            sage: w.norm(p=4.2)
            13.0555695...
            sage: w.norm(p=oo)
            13.0

        Negative values of ``p`` are allowed and will
        provide the same computation as for positive values.
        A zero entry in the vector will raise a warning and return
        zero. ::

            sage: v = vector(CDF, range(1,10))
            sage: v.norm(p=-3.2)
            0.953760808...
            sage: w = vector(CDF, [-1,0,1])
            sage: w.norm(p=-1.6)
            doctest:...: RuntimeWarning: divide by zero encountered in power
            0.0

        Return values are in ``RDF``, or an integer when ``p = 0``.  ::

            sage: v = vector(RDF, [1,2,4,8])
            sage: v.norm() in RDF
            True
            sage: v.norm(p=0) in ZZ
            True

        Improper values of ``p`` are caught.  ::

            sage: w = vector(CDF, [-1,0,1])
            sage: w.norm(p=\'junk\')
            Traceback (most recent call last):
            ...
            ValueError: vector norm \'p\' must be +/- infinity or a real number, not junk'''
    @overload
    def norm(self, orrelatedcomputations) -> Any:
        '''Vector_double_dense.norm(self, p=2)

        File: /build/sagemath/src/sage/src/sage/modules/vector_double_dense.pyx (starting at line 360)

        Return the norm (or related computations) of the vector.

        INPUT:

        - ``p`` -- (default: 2) controls which norm is computed,
          allowable values are any real number and positive and
          negative infinity.  See output discussion for specifics.

        OUTPUT:

        Returned value is a double precision floating point value
        in ``RDF`` (or an integer when ``p=0``).  The default value
        of ``p = 2`` is the "usual" Euclidean norm.  For other values:

        - ``p = Infinity`` or ``p = oo``: the maximum of the
          absolute values of the entries, where the absolute value
          of the complex number `a+bi` is `\\sqrt{a^2+b^2}`
        - ``p = -Infinity`` or ``p = -oo``: the minimum of the
          absolute values of the entries
        - ``p = 0``: the number of nonzero entries in the vector
        - ``p`` any other real number: for a vector `\\vec{x}` this method computes

          .. MATH::

                \\left(\\sum_i x_i^p\\right)^{1/p}

          For ``p < 0`` this function is not a norm, but the above
          computation may be useful for other purposes.

        ALGORITHM:

        Computation is performed by the :func:`~scipy:scipy.linalg.norm`
        function of the SciPy/NumPy library.

        EXAMPLES:

        First over the reals.  ::

            sage: v = vector(RDF, range(9))
            sage: v.norm()
            14.28285685...
            sage: v.norm(p=2)
            14.28285685...
            sage: v.norm(p=6)
            8.744039097...
            sage: v.norm(p=Infinity)
            8.0
            sage: v.norm(p=-oo)
            0.0
            sage: v.norm(p=0)
            8.0
            sage: v.norm(p=0.3)
            4099.153615...

        And over the complex numbers.  ::

            sage: w = vector(CDF, [3-4*I, 0, 5+12*I])
            sage: w.norm()
            13.9283882...
            sage: w.norm(p=2)
            13.9283882...
            sage: w.norm(p=0)
            2.0
            sage: w.norm(p=4.2)
            13.0555695...
            sage: w.norm(p=oo)
            13.0

        Negative values of ``p`` are allowed and will
        provide the same computation as for positive values.
        A zero entry in the vector will raise a warning and return
        zero. ::

            sage: v = vector(CDF, range(1,10))
            sage: v.norm(p=-3.2)
            0.953760808...
            sage: w = vector(CDF, [-1,0,1])
            sage: w.norm(p=-1.6)
            doctest:...: RuntimeWarning: divide by zero encountered in power
            0.0

        Return values are in ``RDF``, or an integer when ``p = 0``.  ::

            sage: v = vector(RDF, [1,2,4,8])
            sage: v.norm() in RDF
            True
            sage: v.norm(p=0) in ZZ
            True

        Improper values of ``p`` are caught.  ::

            sage: w = vector(CDF, [-1,0,1])
            sage: w.norm(p=\'junk\')
            Traceback (most recent call last):
            ...
            ValueError: vector norm \'p\' must be +/- infinity or a real number, not junk'''
    @overload
    def prod(self) -> Any:
        """Vector_double_dense.prod(self)

        File: /build/sagemath/src/sage/src/sage/modules/vector_double_dense.pyx (starting at line 568)

        Return the product of the entries of ``self``.

        EXAMPLES::

            sage: v = vector(RDF, range(9))
            sage: w = vector(CDF, [k+(9-k)*I for k in range(9)])
            sage: v.prod()
            0.0
            sage: w.prod()
            57204225.0*I"""
    @overload
    def prod(self) -> Any:
        """Vector_double_dense.prod(self)

        File: /build/sagemath/src/sage/src/sage/modules/vector_double_dense.pyx (starting at line 568)

        Return the product of the entries of ``self``.

        EXAMPLES::

            sage: v = vector(RDF, range(9))
            sage: w = vector(CDF, [k+(9-k)*I for k in range(9)])
            sage: v.prod()
            0.0
            sage: w.prod()
            57204225.0*I"""
    @overload
    def prod(self) -> Any:
        """Vector_double_dense.prod(self)

        File: /build/sagemath/src/sage/src/sage/modules/vector_double_dense.pyx (starting at line 568)

        Return the product of the entries of ``self``.

        EXAMPLES::

            sage: v = vector(RDF, range(9))
            sage: w = vector(CDF, [k+(9-k)*I for k in range(9)])
            sage: v.prod()
            0.0
            sage: w.prod()
            57204225.0*I"""
    @overload
    def standard_deviation(self, population=...) -> Any:
        """Vector_double_dense.standard_deviation(self, population=True)

        File: /build/sagemath/src/sage/src/sage/modules/vector_double_dense.pyx (starting at line 519)

        Calculate the standard deviation of entries of the vector.

        INPUT:

        - ``population`` -- If ``False``, calculate the sample standard
          deviation

        EXAMPLES::

            sage: v = vector(RDF, range(9))
            sage: w = vector(CDF, [k+(9-k)*I for k in range(9)])
            sage: v.standard_deviation()
            2.7386127875258306
            sage: v.standard_deviation(population=False)
            2.581988897471611
            sage: w.standard_deviation()
            3.872983346207417
            sage: w.standard_deviation(population=False)
            3.6514837167011076"""
    @overload
    def standard_deviation(self) -> Any:
        """Vector_double_dense.standard_deviation(self, population=True)

        File: /build/sagemath/src/sage/src/sage/modules/vector_double_dense.pyx (starting at line 519)

        Calculate the standard deviation of entries of the vector.

        INPUT:

        - ``population`` -- If ``False``, calculate the sample standard
          deviation

        EXAMPLES::

            sage: v = vector(RDF, range(9))
            sage: w = vector(CDF, [k+(9-k)*I for k in range(9)])
            sage: v.standard_deviation()
            2.7386127875258306
            sage: v.standard_deviation(population=False)
            2.581988897471611
            sage: w.standard_deviation()
            3.872983346207417
            sage: w.standard_deviation(population=False)
            3.6514837167011076"""
    @overload
    def standard_deviation(self, population=...) -> Any:
        """Vector_double_dense.standard_deviation(self, population=True)

        File: /build/sagemath/src/sage/src/sage/modules/vector_double_dense.pyx (starting at line 519)

        Calculate the standard deviation of entries of the vector.

        INPUT:

        - ``population`` -- If ``False``, calculate the sample standard
          deviation

        EXAMPLES::

            sage: v = vector(RDF, range(9))
            sage: w = vector(CDF, [k+(9-k)*I for k in range(9)])
            sage: v.standard_deviation()
            2.7386127875258306
            sage: v.standard_deviation(population=False)
            2.581988897471611
            sage: w.standard_deviation()
            3.872983346207417
            sage: w.standard_deviation(population=False)
            3.6514837167011076"""
    @overload
    def standard_deviation(self) -> Any:
        """Vector_double_dense.standard_deviation(self, population=True)

        File: /build/sagemath/src/sage/src/sage/modules/vector_double_dense.pyx (starting at line 519)

        Calculate the standard deviation of entries of the vector.

        INPUT:

        - ``population`` -- If ``False``, calculate the sample standard
          deviation

        EXAMPLES::

            sage: v = vector(RDF, range(9))
            sage: w = vector(CDF, [k+(9-k)*I for k in range(9)])
            sage: v.standard_deviation()
            2.7386127875258306
            sage: v.standard_deviation(population=False)
            2.581988897471611
            sage: w.standard_deviation()
            3.872983346207417
            sage: w.standard_deviation(population=False)
            3.6514837167011076"""
    @overload
    def standard_deviation(self, population=...) -> Any:
        """Vector_double_dense.standard_deviation(self, population=True)

        File: /build/sagemath/src/sage/src/sage/modules/vector_double_dense.pyx (starting at line 519)

        Calculate the standard deviation of entries of the vector.

        INPUT:

        - ``population`` -- If ``False``, calculate the sample standard
          deviation

        EXAMPLES::

            sage: v = vector(RDF, range(9))
            sage: w = vector(CDF, [k+(9-k)*I for k in range(9)])
            sage: v.standard_deviation()
            2.7386127875258306
            sage: v.standard_deviation(population=False)
            2.581988897471611
            sage: w.standard_deviation()
            3.872983346207417
            sage: w.standard_deviation(population=False)
            3.6514837167011076"""
    def stats_kurtosis(self) -> Any:
        """Vector_double_dense.stats_kurtosis(self)

        File: /build/sagemath/src/sage/src/sage/modules/vector_double_dense.pyx (starting at line 546)

        Compute the kurtosis of a dataset.

        Kurtosis is the fourth central moment divided by the square of
        the variance. Since we use Fisher's definition, 3.0 is
        subtracted from the result to give 0.0 for a normal
        distribution. (Paragraph from the scipy.stats docstring.)

        EXAMPLES::

            sage: # needs scipy
            sage: v = vector(RDF, range(9))
            sage: w = vector(CDF, [k+(9-k)*I for k in range(9)])
            sage: v.stats_kurtosis()  # rel tol 5e-15
            -1.2300000000000000
            sage: w.stats_kurtosis()  # rel tol 5e-15
            -1.2300000000000000"""
    @overload
    def sum(self) -> Any:
        """Vector_double_dense.sum(self)

        File: /build/sagemath/src/sage/src/sage/modules/vector_double_dense.pyx (starting at line 583)

        Return the sum of the entries of ``self``.

        EXAMPLES::

            sage: v = vector(RDF, range(9))
            sage: w = vector(CDF, [k+(9-k)*I for k in range(9)])
            sage: v.sum()
            36.0
            sage: w.sum()
            36.0 + 45.0*I"""
    @overload
    def sum(self) -> Any:
        """Vector_double_dense.sum(self)

        File: /build/sagemath/src/sage/src/sage/modules/vector_double_dense.pyx (starting at line 583)

        Return the sum of the entries of ``self``.

        EXAMPLES::

            sage: v = vector(RDF, range(9))
            sage: w = vector(CDF, [k+(9-k)*I for k in range(9)])
            sage: v.sum()
            36.0
            sage: w.sum()
            36.0 + 45.0*I"""
    @overload
    def sum(self) -> Any:
        """Vector_double_dense.sum(self)

        File: /build/sagemath/src/sage/src/sage/modules/vector_double_dense.pyx (starting at line 583)

        Return the sum of the entries of ``self``.

        EXAMPLES::

            sage: v = vector(RDF, range(9))
            sage: w = vector(CDF, [k+(9-k)*I for k in range(9)])
            sage: v.sum()
            36.0
            sage: w.sum()
            36.0 + 45.0*I"""
    @overload
    def variance(self, population=...) -> Any:
        """Vector_double_dense.variance(self, population=True)

        File: /build/sagemath/src/sage/src/sage/modules/vector_double_dense.pyx (starting at line 493)

        Calculate the variance of entries of the vector.

        INPUT:

        - ``population`` -- if ``False``, calculate the sample variance

        EXAMPLES::

            sage: v = vector(RDF, range(9))
            sage: w = vector(CDF, [k+(9-k)*I for k in range(9)])
            sage: v.variance()
            7.5
            sage: v.variance(population=False)
            6.666666666666667
            sage: w.variance()
            15.0
            sage: w.variance(population=False)
            13.333333333333334"""
    @overload
    def variance(self) -> Any:
        """Vector_double_dense.variance(self, population=True)

        File: /build/sagemath/src/sage/src/sage/modules/vector_double_dense.pyx (starting at line 493)

        Calculate the variance of entries of the vector.

        INPUT:

        - ``population`` -- if ``False``, calculate the sample variance

        EXAMPLES::

            sage: v = vector(RDF, range(9))
            sage: w = vector(CDF, [k+(9-k)*I for k in range(9)])
            sage: v.variance()
            7.5
            sage: v.variance(population=False)
            6.666666666666667
            sage: w.variance()
            15.0
            sage: w.variance(population=False)
            13.333333333333334"""
    @overload
    def variance(self, population=...) -> Any:
        """Vector_double_dense.variance(self, population=True)

        File: /build/sagemath/src/sage/src/sage/modules/vector_double_dense.pyx (starting at line 493)

        Calculate the variance of entries of the vector.

        INPUT:

        - ``population`` -- if ``False``, calculate the sample variance

        EXAMPLES::

            sage: v = vector(RDF, range(9))
            sage: w = vector(CDF, [k+(9-k)*I for k in range(9)])
            sage: v.variance()
            7.5
            sage: v.variance(population=False)
            6.666666666666667
            sage: w.variance()
            15.0
            sage: w.variance(population=False)
            13.333333333333334"""
    @overload
    def variance(self) -> Any:
        """Vector_double_dense.variance(self, population=True)

        File: /build/sagemath/src/sage/src/sage/modules/vector_double_dense.pyx (starting at line 493)

        Calculate the variance of entries of the vector.

        INPUT:

        - ``population`` -- if ``False``, calculate the sample variance

        EXAMPLES::

            sage: v = vector(RDF, range(9))
            sage: w = vector(CDF, [k+(9-k)*I for k in range(9)])
            sage: v.variance()
            7.5
            sage: v.variance(population=False)
            6.666666666666667
            sage: w.variance()
            15.0
            sage: w.variance(population=False)
            13.333333333333334"""
    @overload
    def variance(self, population=...) -> Any:
        """Vector_double_dense.variance(self, population=True)

        File: /build/sagemath/src/sage/src/sage/modules/vector_double_dense.pyx (starting at line 493)

        Calculate the variance of entries of the vector.

        INPUT:

        - ``population`` -- if ``False``, calculate the sample variance

        EXAMPLES::

            sage: v = vector(RDF, range(9))
            sage: w = vector(CDF, [k+(9-k)*I for k in range(9)])
            sage: v.variance()
            7.5
            sage: v.variance(population=False)
            6.666666666666667
            sage: w.variance()
            15.0
            sage: w.variance(population=False)
            13.333333333333334"""
    def zero_at(self, eps) -> Any:
        """Vector_double_dense.zero_at(self, eps)

        File: /build/sagemath/src/sage/src/sage/modules/vector_double_dense.pyx (starting at line 312)

        Return a copy with small entries replaced by zeros.

        This is useful for modifying output from algorithms
        which have large relative errors when producing zero
        elements, e.g. to create reliable doctests.

        INPUT:

        - ``eps`` -- cutoff value

        OUTPUT:

        A modified copy of the vector.  Elements smaller than
        or equal to ``eps`` are replaced with zeroes.  For
        complex vectors, the real and imaginary parts are
        considered individually.

        EXAMPLES::

            sage: v = vector(RDF, [1.0, 2.0, 10^-10, 3.0])
            sage: v.zero_at(1e-8)
            (1.0, 2.0, 0.0, 3.0)
            sage: v.zero_at(1e-12)
            (1.0, 2.0, 1e-10, 3.0)

        For complex numbers the real and imaginary parts are considered
        separately.  ::

            sage: w = vector(CDF, [10^-6 + 5*I, 5 + 10^-6*I, 5 + 5*I, 10^-6 + 10^-6*I])
            sage: w.zero_at(1.0e-4)
            (5.0*I, 5.0, 5.0 + 5.0*I, 0.0)
            sage: w.zero_at(1.0e-8)
            (1e-06 + 5.0*I, 5.0 + 1e-06*I, 5.0 + 5.0*I, 1e-06 + 1e-06*I)"""
