import _cython_3_2_1
from sage.rings.complex_mpfr import ComplexNumber as ComplexNumber
from sage.rings.integer import Integer as Integer
from typing import Any, overload

FFT: _cython_3_2_1.cython_function_or_method
FastFourierTransform: _cython_3_2_1.cython_function_or_method

class FastFourierTransform_base:
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class FastFourierTransform_complex(FastFourierTransform_base):
    """FastFourierTransform_complex(size_t n, size_t stride=1)

    File: /build/sagemath/src/sage/src/sage/calculus/transforms/fft.pyx (starting at line 85)

    Wrapper class for GSL's fast Fourier transform."""
    def __init__(self, size_tn, size_tstride=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/calculus/transforms/fft.pyx (starting at line 90)

                Create an array-like object of fixed size that will contain the vector to
                apply the Fast Fourier Transform.

                INPUT:

                - ``n`` -- integer, the size of the array
                - ``stride`` -- the stride to be applied when manipulating the array

                EXAMPLES::

                    sage: a = FastFourierTransform(1) # indirect doctest
                    sage: a
                    [(0.0, 0.0)]
        """
    @overload
    def backward_transform(self) -> Any:
        """FastFourierTransform_complex.backward_transform(self)

        File: /build/sagemath/src/sage/src/sage/calculus/transforms/fft.pyx (starting at line 436)

        Compute the in-place backwards Fourier transform of this data
        using the Cooley-Tukey algorithm.

        OUTPUT: none, the transformation is done in-place

        This is the same as :meth:`inverse_transform` but lacks normalization
        so that ``f.forward_transform().backward_transform() == n*f``. Where
        ``n`` is the size of the array.

        EXAMPLES::

            sage: a = FastFourierTransform(125)
            sage: b = FastFourierTransform(125)
            sage: for i in range(1, 60): a[i]=1
            sage: for i in range(1, 60): b[i]=1
            sage: a.forward_transform()
            sage: a.backward_transform()
            sage: (a.plot() + b.plot()).show(ymin=0)    # long time (2s on sage.math, 2011), needs sage.plot
            sage: abs(sum([CDF(a[i])/125-CDF(b[i]) for i in range(125)])) < 2**-16
            True

        Here we check it with a power of two::

            sage: a = FastFourierTransform(128)
            sage: b = FastFourierTransform(128)
            sage: for i in range(1, 60): a[i]=1
            sage: for i in range(1, 60): b[i]=1
            sage: a.forward_transform()
            sage: a.backward_transform()
            sage: (a.plot() + b.plot()).show(ymin=0)                                    # needs sage.plot"""
    @overload
    def backward_transform(self) -> Any:
        """FastFourierTransform_complex.backward_transform(self)

        File: /build/sagemath/src/sage/src/sage/calculus/transforms/fft.pyx (starting at line 436)

        Compute the in-place backwards Fourier transform of this data
        using the Cooley-Tukey algorithm.

        OUTPUT: none, the transformation is done in-place

        This is the same as :meth:`inverse_transform` but lacks normalization
        so that ``f.forward_transform().backward_transform() == n*f``. Where
        ``n`` is the size of the array.

        EXAMPLES::

            sage: a = FastFourierTransform(125)
            sage: b = FastFourierTransform(125)
            sage: for i in range(1, 60): a[i]=1
            sage: for i in range(1, 60): b[i]=1
            sage: a.forward_transform()
            sage: a.backward_transform()
            sage: (a.plot() + b.plot()).show(ymin=0)    # long time (2s on sage.math, 2011), needs sage.plot
            sage: abs(sum([CDF(a[i])/125-CDF(b[i]) for i in range(125)])) < 2**-16
            True

        Here we check it with a power of two::

            sage: a = FastFourierTransform(128)
            sage: b = FastFourierTransform(128)
            sage: for i in range(1, 60): a[i]=1
            sage: for i in range(1, 60): b[i]=1
            sage: a.forward_transform()
            sage: a.backward_transform()
            sage: (a.plot() + b.plot()).show(ymin=0)                                    # needs sage.plot"""
    @overload
    def backward_transform(self) -> Any:
        """FastFourierTransform_complex.backward_transform(self)

        File: /build/sagemath/src/sage/src/sage/calculus/transforms/fft.pyx (starting at line 436)

        Compute the in-place backwards Fourier transform of this data
        using the Cooley-Tukey algorithm.

        OUTPUT: none, the transformation is done in-place

        This is the same as :meth:`inverse_transform` but lacks normalization
        so that ``f.forward_transform().backward_transform() == n*f``. Where
        ``n`` is the size of the array.

        EXAMPLES::

            sage: a = FastFourierTransform(125)
            sage: b = FastFourierTransform(125)
            sage: for i in range(1, 60): a[i]=1
            sage: for i in range(1, 60): b[i]=1
            sage: a.forward_transform()
            sage: a.backward_transform()
            sage: (a.plot() + b.plot()).show(ymin=0)    # long time (2s on sage.math, 2011), needs sage.plot
            sage: abs(sum([CDF(a[i])/125-CDF(b[i]) for i in range(125)])) < 2**-16
            True

        Here we check it with a power of two::

            sage: a = FastFourierTransform(128)
            sage: b = FastFourierTransform(128)
            sage: for i in range(1, 60): a[i]=1
            sage: for i in range(1, 60): b[i]=1
            sage: a.forward_transform()
            sage: a.backward_transform()
            sage: (a.plot() + b.plot()).show(ymin=0)                                    # needs sage.plot"""
    @overload
    def backward_transform(self) -> Any:
        """FastFourierTransform_complex.backward_transform(self)

        File: /build/sagemath/src/sage/src/sage/calculus/transforms/fft.pyx (starting at line 436)

        Compute the in-place backwards Fourier transform of this data
        using the Cooley-Tukey algorithm.

        OUTPUT: none, the transformation is done in-place

        This is the same as :meth:`inverse_transform` but lacks normalization
        so that ``f.forward_transform().backward_transform() == n*f``. Where
        ``n`` is the size of the array.

        EXAMPLES::

            sage: a = FastFourierTransform(125)
            sage: b = FastFourierTransform(125)
            sage: for i in range(1, 60): a[i]=1
            sage: for i in range(1, 60): b[i]=1
            sage: a.forward_transform()
            sage: a.backward_transform()
            sage: (a.plot() + b.plot()).show(ymin=0)    # long time (2s on sage.math, 2011), needs sage.plot
            sage: abs(sum([CDF(a[i])/125-CDF(b[i]) for i in range(125)])) < 2**-16
            True

        Here we check it with a power of two::

            sage: a = FastFourierTransform(128)
            sage: b = FastFourierTransform(128)
            sage: for i in range(1, 60): a[i]=1
            sage: for i in range(1, 60): b[i]=1
            sage: a.forward_transform()
            sage: a.backward_transform()
            sage: (a.plot() + b.plot()).show(ymin=0)                                    # needs sage.plot"""
    @overload
    def forward_transform(self) -> Any:
        """FastFourierTransform_complex.forward_transform(self)

        File: /build/sagemath/src/sage/src/sage/calculus/transforms/fft.pyx (starting at line 353)

        Compute the in-place forward Fourier transform of this data
        using the Cooley-Tukey algorithm.

        OUTPUT: none, the transformation is done in-place

        If the number of sample points in the input is a power of 2 then the
        gsl function ``gsl_fft_complex_radix2_forward`` is automatically called.
        Otherwise, ``gsl_fft_complex_forward`` is called.

        EXAMPLES::

            sage: a = FastFourierTransform(4)
            sage: for i in range(4): a[i] = i
            sage: a.forward_transform()
            sage: a #abs tol 1e-2
            [(6.0, 0.0), (-2.0, 2.0), (-2.0, 0.0), (-2.0, -2.0)]"""
    @overload
    def forward_transform(self) -> Any:
        """FastFourierTransform_complex.forward_transform(self)

        File: /build/sagemath/src/sage/src/sage/calculus/transforms/fft.pyx (starting at line 353)

        Compute the in-place forward Fourier transform of this data
        using the Cooley-Tukey algorithm.

        OUTPUT: none, the transformation is done in-place

        If the number of sample points in the input is a power of 2 then the
        gsl function ``gsl_fft_complex_radix2_forward`` is automatically called.
        Otherwise, ``gsl_fft_complex_forward`` is called.

        EXAMPLES::

            sage: a = FastFourierTransform(4)
            sage: for i in range(4): a[i] = i
            sage: a.forward_transform()
            sage: a #abs tol 1e-2
            [(6.0, 0.0), (-2.0, 2.0), (-2.0, 0.0), (-2.0, -2.0)]"""
    @overload
    def inverse_transform(self) -> Any:
        """FastFourierTransform_complex.inverse_transform(self)

        File: /build/sagemath/src/sage/src/sage/calculus/transforms/fft.pyx (starting at line 385)

        Compute the in-place inverse Fourier transform of this data
        using the Cooley-Tukey algorithm.

        OUTPUT: none, the transformation is done in-place

        If the number of sample points in the input is a power of 2 then the
        function ``gsl_fft_complex_radix2_inverse`` is automatically called.
        Otherwise, ``gsl_fft_complex_inverse`` is called.

        This transform is normalized so ``f.forward_transform().inverse_transform() == f``
        modulo round-off errors. See also :meth:`backward_transform`.

        EXAMPLES::

            sage: a = FastFourierTransform(125)
            sage: b = FastFourierTransform(125)
            sage: for i in range(1, 60): a[i]=1
            sage: for i in range(1, 60): b[i]=1
            sage: a.forward_transform()
            sage: a.inverse_transform()
            sage: a.plot() + b.plot()                                                   # needs sage.plot
            Graphics object consisting of 250 graphics primitives
            sage: abs(sum([CDF(a[i])-CDF(b[i]) for i in range(125)])) < 2**-16
            True

        Here we check it with a power of two::

            sage: a = FastFourierTransform(128)
            sage: b = FastFourierTransform(128)
            sage: for i in range(1, 60): a[i]=1
            sage: for i in range(1, 60): b[i]=1
            sage: a.forward_transform()
            sage: a.inverse_transform()
            sage: a.plot() + b.plot()                                                   # needs sage.plot
            Graphics object consisting of 256 graphics primitives"""
    @overload
    def inverse_transform(self) -> Any:
        """FastFourierTransform_complex.inverse_transform(self)

        File: /build/sagemath/src/sage/src/sage/calculus/transforms/fft.pyx (starting at line 385)

        Compute the in-place inverse Fourier transform of this data
        using the Cooley-Tukey algorithm.

        OUTPUT: none, the transformation is done in-place

        If the number of sample points in the input is a power of 2 then the
        function ``gsl_fft_complex_radix2_inverse`` is automatically called.
        Otherwise, ``gsl_fft_complex_inverse`` is called.

        This transform is normalized so ``f.forward_transform().inverse_transform() == f``
        modulo round-off errors. See also :meth:`backward_transform`.

        EXAMPLES::

            sage: a = FastFourierTransform(125)
            sage: b = FastFourierTransform(125)
            sage: for i in range(1, 60): a[i]=1
            sage: for i in range(1, 60): b[i]=1
            sage: a.forward_transform()
            sage: a.inverse_transform()
            sage: a.plot() + b.plot()                                                   # needs sage.plot
            Graphics object consisting of 250 graphics primitives
            sage: abs(sum([CDF(a[i])-CDF(b[i]) for i in range(125)])) < 2**-16
            True

        Here we check it with a power of two::

            sage: a = FastFourierTransform(128)
            sage: b = FastFourierTransform(128)
            sage: for i in range(1, 60): a[i]=1
            sage: for i in range(1, 60): b[i]=1
            sage: a.forward_transform()
            sage: a.inverse_transform()
            sage: a.plot() + b.plot()                                                   # needs sage.plot
            Graphics object consisting of 256 graphics primitives"""
    @overload
    def inverse_transform(self) -> Any:
        """FastFourierTransform_complex.inverse_transform(self)

        File: /build/sagemath/src/sage/src/sage/calculus/transforms/fft.pyx (starting at line 385)

        Compute the in-place inverse Fourier transform of this data
        using the Cooley-Tukey algorithm.

        OUTPUT: none, the transformation is done in-place

        If the number of sample points in the input is a power of 2 then the
        function ``gsl_fft_complex_radix2_inverse`` is automatically called.
        Otherwise, ``gsl_fft_complex_inverse`` is called.

        This transform is normalized so ``f.forward_transform().inverse_transform() == f``
        modulo round-off errors. See also :meth:`backward_transform`.

        EXAMPLES::

            sage: a = FastFourierTransform(125)
            sage: b = FastFourierTransform(125)
            sage: for i in range(1, 60): a[i]=1
            sage: for i in range(1, 60): b[i]=1
            sage: a.forward_transform()
            sage: a.inverse_transform()
            sage: a.plot() + b.plot()                                                   # needs sage.plot
            Graphics object consisting of 250 graphics primitives
            sage: abs(sum([CDF(a[i])-CDF(b[i]) for i in range(125)])) < 2**-16
            True

        Here we check it with a power of two::

            sage: a = FastFourierTransform(128)
            sage: b = FastFourierTransform(128)
            sage: for i in range(1, 60): a[i]=1
            sage: for i in range(1, 60): b[i]=1
            sage: a.forward_transform()
            sage: a.inverse_transform()
            sage: a.plot() + b.plot()                                                   # needs sage.plot
            Graphics object consisting of 256 graphics primitives"""
    @overload
    def inverse_transform(self) -> Any:
        """FastFourierTransform_complex.inverse_transform(self)

        File: /build/sagemath/src/sage/src/sage/calculus/transforms/fft.pyx (starting at line 385)

        Compute the in-place inverse Fourier transform of this data
        using the Cooley-Tukey algorithm.

        OUTPUT: none, the transformation is done in-place

        If the number of sample points in the input is a power of 2 then the
        function ``gsl_fft_complex_radix2_inverse`` is automatically called.
        Otherwise, ``gsl_fft_complex_inverse`` is called.

        This transform is normalized so ``f.forward_transform().inverse_transform() == f``
        modulo round-off errors. See also :meth:`backward_transform`.

        EXAMPLES::

            sage: a = FastFourierTransform(125)
            sage: b = FastFourierTransform(125)
            sage: for i in range(1, 60): a[i]=1
            sage: for i in range(1, 60): b[i]=1
            sage: a.forward_transform()
            sage: a.inverse_transform()
            sage: a.plot() + b.plot()                                                   # needs sage.plot
            Graphics object consisting of 250 graphics primitives
            sage: abs(sum([CDF(a[i])-CDF(b[i]) for i in range(125)])) < 2**-16
            True

        Here we check it with a power of two::

            sage: a = FastFourierTransform(128)
            sage: b = FastFourierTransform(128)
            sage: for i in range(1, 60): a[i]=1
            sage: for i in range(1, 60): b[i]=1
            sage: a.forward_transform()
            sage: a.inverse_transform()
            sage: a.plot() + b.plot()                                                   # needs sage.plot
            Graphics object consisting of 256 graphics primitives"""
    @overload
    def plot(self, style=..., xmin=..., xmax=..., **args) -> Any:
        """FastFourierTransform_complex.plot(self, style='rect', xmin=None, xmax=None, **args)

        File: /build/sagemath/src/sage/src/sage/calculus/transforms/fft.pyx (starting at line 301)

        Plot a slice of the array.

        - ``style`` -- style of the plot, options are ``'rect'`` or ``'polar'``

          - ``'rect'`` -- height represents real part, color represents
            imaginary part
          - ``'polar'`` -- height represents absolute value, color
            represents argument

        - ``xmin`` -- the lower bound of the slice to plot; 0 by default
        - ``xmax`` -- the upper bound of the slice to plot; ``len(self)`` by default
        - ``**args`` -- passed on to the line plotting function

        OUTPUT: a plot of the array

        EXAMPLES::

            sage: # needs sage.plot
            sage: a = FastFourierTransform(16)
            sage: for i in range(16): a[i] = (random(),random())
            sage: A = plot(a)
            sage: B = plot(a, style='polar')                                            # needs sage.symbolic
            sage: type(A)
            <class 'sage.plot.graphics.Graphics'>
            sage: type(B)                                                               # needs sage.symbolic
            <class 'sage.plot.graphics.Graphics'>
            sage: a = FastFourierTransform(125)
            sage: b = FastFourierTransform(125)
            sage: for i in range(1, 60): a[i]=1
            sage: for i in range(1, 60): b[i]=1
            sage: a.forward_transform()
            sage: a.inverse_transform()
            sage: a.plot() + b.plot()
            Graphics object consisting of 250 graphics primitives"""
    @overload
    def plot(self, a) -> Any:
        """FastFourierTransform_complex.plot(self, style='rect', xmin=None, xmax=None, **args)

        File: /build/sagemath/src/sage/src/sage/calculus/transforms/fft.pyx (starting at line 301)

        Plot a slice of the array.

        - ``style`` -- style of the plot, options are ``'rect'`` or ``'polar'``

          - ``'rect'`` -- height represents real part, color represents
            imaginary part
          - ``'polar'`` -- height represents absolute value, color
            represents argument

        - ``xmin`` -- the lower bound of the slice to plot; 0 by default
        - ``xmax`` -- the upper bound of the slice to plot; ``len(self)`` by default
        - ``**args`` -- passed on to the line plotting function

        OUTPUT: a plot of the array

        EXAMPLES::

            sage: # needs sage.plot
            sage: a = FastFourierTransform(16)
            sage: for i in range(16): a[i] = (random(),random())
            sage: A = plot(a)
            sage: B = plot(a, style='polar')                                            # needs sage.symbolic
            sage: type(A)
            <class 'sage.plot.graphics.Graphics'>
            sage: type(B)                                                               # needs sage.symbolic
            <class 'sage.plot.graphics.Graphics'>
            sage: a = FastFourierTransform(125)
            sage: b = FastFourierTransform(125)
            sage: for i in range(1, 60): a[i]=1
            sage: for i in range(1, 60): b[i]=1
            sage: a.forward_transform()
            sage: a.inverse_transform()
            sage: a.plot() + b.plot()
            Graphics object consisting of 250 graphics primitives"""
    @overload
    def plot(self, a, style=...) -> Any:
        """FastFourierTransform_complex.plot(self, style='rect', xmin=None, xmax=None, **args)

        File: /build/sagemath/src/sage/src/sage/calculus/transforms/fft.pyx (starting at line 301)

        Plot a slice of the array.

        - ``style`` -- style of the plot, options are ``'rect'`` or ``'polar'``

          - ``'rect'`` -- height represents real part, color represents
            imaginary part
          - ``'polar'`` -- height represents absolute value, color
            represents argument

        - ``xmin`` -- the lower bound of the slice to plot; 0 by default
        - ``xmax`` -- the upper bound of the slice to plot; ``len(self)`` by default
        - ``**args`` -- passed on to the line plotting function

        OUTPUT: a plot of the array

        EXAMPLES::

            sage: # needs sage.plot
            sage: a = FastFourierTransform(16)
            sage: for i in range(16): a[i] = (random(),random())
            sage: A = plot(a)
            sage: B = plot(a, style='polar')                                            # needs sage.symbolic
            sage: type(A)
            <class 'sage.plot.graphics.Graphics'>
            sage: type(B)                                                               # needs sage.symbolic
            <class 'sage.plot.graphics.Graphics'>
            sage: a = FastFourierTransform(125)
            sage: b = FastFourierTransform(125)
            sage: for i in range(1, 60): a[i]=1
            sage: for i in range(1, 60): b[i]=1
            sage: a.forward_transform()
            sage: a.inverse_transform()
            sage: a.plot() + b.plot()
            Graphics object consisting of 250 graphics primitives"""
    @overload
    def plot(self) -> Any:
        """FastFourierTransform_complex.plot(self, style='rect', xmin=None, xmax=None, **args)

        File: /build/sagemath/src/sage/src/sage/calculus/transforms/fft.pyx (starting at line 301)

        Plot a slice of the array.

        - ``style`` -- style of the plot, options are ``'rect'`` or ``'polar'``

          - ``'rect'`` -- height represents real part, color represents
            imaginary part
          - ``'polar'`` -- height represents absolute value, color
            represents argument

        - ``xmin`` -- the lower bound of the slice to plot; 0 by default
        - ``xmax`` -- the upper bound of the slice to plot; ``len(self)`` by default
        - ``**args`` -- passed on to the line plotting function

        OUTPUT: a plot of the array

        EXAMPLES::

            sage: # needs sage.plot
            sage: a = FastFourierTransform(16)
            sage: for i in range(16): a[i] = (random(),random())
            sage: A = plot(a)
            sage: B = plot(a, style='polar')                                            # needs sage.symbolic
            sage: type(A)
            <class 'sage.plot.graphics.Graphics'>
            sage: type(B)                                                               # needs sage.symbolic
            <class 'sage.plot.graphics.Graphics'>
            sage: a = FastFourierTransform(125)
            sage: b = FastFourierTransform(125)
            sage: for i in range(1, 60): a[i]=1
            sage: for i in range(1, 60): b[i]=1
            sage: a.forward_transform()
            sage: a.inverse_transform()
            sage: a.plot() + b.plot()
            Graphics object consisting of 250 graphics primitives"""
    def __delitem__(self, other) -> None:
        """Delete self[key]."""
    def __getitem__(self, i) -> Any:
        """FastFourierTransform_complex.__getitem__(self, i)

        File: /build/sagemath/src/sage/src/sage/calculus/transforms/fft.pyx (starting at line 187)

        Get the `i`-th element of the array.

        INPUT:

        - ``i`` -- integer

        OUTPUT: the `i`-th element of the array ``self[i]``

        EXAMPLES::

            sage: a = FastFourierTransform(4)
            sage: a[0]
            (0.0, 0.0)
            sage: a[0] = 1
            sage: a[0] == (1,0)
            True"""
    def __len__(self) -> Any:
        """FastFourierTransform_complex.__len__(self)

        File: /build/sagemath/src/sage/src/sage/calculus/transforms/fft.pyx (starting at line 124)

        Return the size of the array.

        OUTPUT: the size of the array

        EXAMPLES::

            sage: a = FastFourierTransform(48)
            sage: len(a)
            48"""
    def __setitem__(self, size_ti, xy) -> Any:
        """FastFourierTransform_complex.__setitem__(self, size_t i, xy)

        File: /build/sagemath/src/sage/src/sage/calculus/transforms/fft.pyx (starting at line 138)

        Assign a value to an index of the array.

        Currently the input has to be en element that can be coerced
        to ``float`` or a ``ComplexNumber`` element.

        INPUT:

        - ``i`` -- integer; the index
        - ``xy`` -- an object to store as `i`-th element of the array ``self[i]``

        EXAMPLES::

            sage: # needs sage.rings.mpfr sage.symbolic
            sage: I = CC(I)
            sage: a = FastFourierTransform(4)
            sage: a[0] = 1
            sage: a[1] = I
            sage: a[2] = 1+I
            sage: a[3] = (2,2)
            sage: a
            [(1.0, 0.0), (0.0, 1.0), (1.0, 1.0), (2.0, 2.0)]
            sage: I = CDF(I)
            sage: a[1] = I
            Traceback (most recent call last):
            ...
            TypeError: unable to convert 1.0*I to float; use abs() or real_part() as desired

        TESTS:

        Verify that :issue:`10758` is fixed. ::

            sage: F = FFT(1)
            sage: F[0] = (1,1)
            sage: F[0] = 1
            sage: F[0]
            (1.0, 0.0)"""

class FourierTransform_complex:
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class FourierTransform_real:
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
