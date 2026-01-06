r"""
Time Series

This is a module for working with discrete floating point time series.
It is designed so that every operation is very fast, typically much
faster than with other generic code, e.g., Python lists of doubles or
even NumPy arrays.  The semantics of time series is more similar to
Python lists of doubles than Sage real double vectors or NumPy 1-D
arrays.   In particular, time series are not endowed with much
algebraic structure and are always mutable.

.. NOTE::

    NumPy arrays are faster at slicing, since slices return
    references, and NumPy arrays have strides.  However, this speed at
    slicing makes NumPy slower at certain other operations.

EXAMPLES::

    sage: set_random_seed(1)
    sage: t = stats.TimeSeries([random()-0.5 for _ in range(10)]); t
    [0.3294, 0.0959, -0.0706, -0.4646, 0.4311, 0.2275, -0.3840, -0.3528, -0.4119, -0.2933]
    sage: t.sums()
    [0.3294, 0.4253, 0.3547, -0.1099, 0.3212, 0.5487, 0.1647, -0.1882, -0.6001, -0.8933]
    sage: t.exponential_moving_average(0.7)
    [0.0000, 0.3294, 0.1660, 0.0003, -0.3251, 0.2042, 0.2205, -0.2027, -0.3078, -0.3807]
    sage: t.standard_deviation()
    0.33729638212891383
    sage: t.mean()
    -0.08933425506929439
    sage: t.variance()
    0.1137688493972542...

AUTHOR:

- William Stein
"""

from collections.abc import Iterable
from typing import Any, Literal, Self, overload
from typings_sagemath import Int, Real
from sage.plot.graphics import Graphics
from sage.modules.vector_real_double_dense import Vector_real_double_dense
from numpy import ndarray

from sage.categories.category import RDF as RDF
from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.rings.integer import Integer as Integer
from sage.structure.element import (
    have_same_parent as have_same_parent,
    parent as parent,
)
from sage.structure.richcmp import (
    revop as revop,
    rich_to_bool as rich_to_bool,
    rich_to_bool_sgn as rich_to_bool_sgn,
    richcmp as richcmp,
    richcmp_not_equal as richcmp_not_equal,
)

def autoregressive_fit(acvs: TimeSeries | Vector_real_double_dense | ndarray) -> TimeSeries:
    r"""
    Given a sequence of lagged autocovariances of length `M` produce
    `a_1,\dots,a_p` so that the first `M` autocovariance coefficients
    of the autoregressive processes `X_t=a_1X_{t_1}+\cdots+a_pX_{t-p}+Z_t`
    are the same as the input sequence.

    The function works by solving the Yule-Walker equations
    `\Gamma a =\gamma`, where `\gamma=(\gamma(1),\dots,\gamma(M))`,
    `a=(a_1,\dots,a_M)`, with `\gamma(i)` the autocovariance of lag `i`
    and `\Gamma_{ij}=\gamma(i-j)`.
    """
digits: int = 4
max_print: int = 10
def unpickle_time_series_v1(v: bytes , n: int):
    r"""
    Version 1 unpickle method.

    INPUT:

    - ``v`` -- a raw char buffer

    EXAMPLES::

        sage: v = stats.TimeSeries([1,2,3])
        sage: s = v.__reduce__()[1][0]
        sage: type(s)
        <class 'bytes'>
        sage: sage.stats.time_series.unpickle_time_series_v1(s,3)
        [1.0000, 2.0000, 3.0000]
        sage: sage.stats.time_series.unpickle_time_series_v1(s+s,6)
        [1.0000, 2.0000, 3.0000, 1.0000, 2.0000, 3.0000]
        sage: sage.stats.time_series.unpickle_time_series_v1(b'',0)
        []
    """

class TimeSeries:
    def __init__(
        self,
        values: int | Integer | Vector_real_double_dense | ndarray,
        initialize: bool = True,
    ):
        """
        Initialize new time series.

        INPUT:

        - ``values`` -- integer (number of values) or an iterable of
          floats

        - ``initialize`` -- boolean (default: ``True``); if ``False``, do not
          bother to zero out the entries of the new time series.
          For large series that you are going to just fill in,
          this can be way faster.

        EXAMPLES:

        This implicitly calls init::

            sage: stats.TimeSeries([pi, 3, 18.2])                                       # needs sage.symbolic
            [3.1416, 3.0000, 18.2000]

        Conversion from a NumPy 1-D array, which is very fast::

            sage: v = stats.TimeSeries([1..5])
            sage: w = v.numpy()
            sage: stats.TimeSeries(w)
            [1.0000, 2.0000, 3.0000, 4.0000, 5.0000]

        Conversion from an n-dimensional NumPy array also works::

            sage: import numpy
            sage: v = numpy.array([[1,2], [3,4]], dtype=float); v
            array([[1., 2.],
                   [3., 4.]])
            sage: stats.TimeSeries(v)
            [1.0000, 2.0000, 3.0000, 4.0000]
            sage: stats.TimeSeries(v[:,0])
            [1.0000, 3.0000]
            sage: u = numpy.array([[1,2],[3,4]])
            sage: stats.TimeSeries(u)
            [1.0000, 2.0000, 3.0000, 4.0000]

        For speed purposes we don't initialize (so value is garbage)::

            sage: t = stats.TimeSeries(10, initialize=False)
        """
    def abs(self) -> TimeSeries:
        """
        Return new time series got by replacing all entries
        of ``self`` by their absolute value.

        OUTPUT: a new time series

        EXAMPLES::

            sage: v = stats.TimeSeries([1,3.1908439,-4,5.93932])
            sage: v
            [1.0000, 3.1908, -4.0000, 5.9393]
            sage: v.abs()
            [1.0000, 3.1908, 4.0000, 5.9393]"""
    def add_entries(self, t: TimeSeries) -> TimeSeries:
        """
        Add corresponding entries of ``self`` and ``t`` together,
        extending either ``self`` or ``t`` by 0s if they do
        not have the same length.

        .. NOTE::

            To add a single number to the entries of a time series,
            use the ``add_scalar`` method.

        INPUT:

        - ``t`` -- a time series

        OUTPUT:

        A time series with length the maximum of the lengths of
        ``self`` and ``t``.

        EXAMPLES::

            sage: v = stats.TimeSeries([1,2,-5]); v
            [1.0000, 2.0000, -5.0000]
            sage: v.add_entries([3,4])
            [4.0000, 6.0000, -5.0000]
            sage: v.add_entries(v)
            [2.0000, 4.0000, -10.0000]
            sage: v.add_entries([3,4,7,18.5])
            [4.0000, 6.0000, 2.0000, 18.5000]"""
    def add_scalar(self, s: Real) -> TimeSeries:
        """
        Return new time series obtained by adding a scalar to every
        value in the series.

        .. NOTE::

            To add componentwise, use the :meth:`add_entries` method.

        INPUT:

        - ``s`` -- a float

        OUTPUT: a new time series with ``s`` added to all values

        EXAMPLES::

            sage: v = stats.TimeSeries([5,4,1.3,2,8,10,3,-5]); v
            [5.0000, 4.0000, 1.3000, 2.0000, 8.0000, 10.0000, 3.0000, -5.0000]
            sage: v.add_scalar(0.5)
            [5.5000, 4.5000, 1.8000, 2.5000, 8.5000, 10.5000, 3.5000, -4.5000]"""
    def autocorrelation(self, k: Int = 1) -> Real:
        """
        Return the `k`-th sample autocorrelation of this time series
        `x_i`.

        Let `\\mu` be the sample mean.  Then the sample autocorrelation
        function is

        .. MATH::

            \\frac{\\sum_{t=0}^{n-k-1} (x_t - \\mu)(x_{t+k} - \\mu) }
                 {\\sum_{t=0}^{n-1}   (x_t - \\mu)^2}.

        Note that the variance must be nonzero or you will get a
        :exc:`ZeroDivisionError`.

        INPUT:

        - ``k`` -- nonnegative integer (default: 1)

        OUTPUT: a time series

        EXAMPLES::

            sage: v = stats.TimeSeries([13,8,15,4,4,12,11,7,14,12])
            sage: v.autocorrelation()
            -0.1875
            sage: v.autocorrelation(1)
            -0.1875
            sage: v.autocorrelation(0)
            1.0
            sage: v.autocorrelation(2)
            -0.20138888888888887
            sage: v.autocorrelation(3)
            0.18055555555555555

            sage: stats.TimeSeries([1..1000]).autocorrelation()
            0.997"""
    def autocovariance(self, k: Int = 0) -> Real:
        """
        Return the `k`-th autocovariance function `\\gamma(k)` of ``self``.

        This is the covariance of ``self`` with ``self`` shifted by `k`, i.e.,

        .. MATH::

            \\left.
            \\left( \\sum_{t=0}^{n-k-1} (x_t - \\mu)(x_{t + k} - \\mu) \\right)
            \\right/ n,

        where `n` is the length of ``self``.

        Note the denominator of `n`, which gives a "better" sample
        estimator.

        INPUT:

        - ``k`` -- nonnegative integer (default: 0)

        OUTPUT: float

        EXAMPLES::

            sage: v = stats.TimeSeries([13,8,15,4,4,12,11,7,14,12])
            sage: v.autocovariance(0)
            14.4
            sage: mu = v.mean(); sum([(a-mu)^2 for a in v])/len(v)
            14.4
            sage: v.autocovariance(1)
            -2.7
            sage: mu = v.mean()
            sage: sum((v[i]-mu)*(v[i+1]-mu) for i in range(len(v)-1))/len(v)
            -2.7
            sage: v.autocovariance(1)
            -2.7

        We illustrate with a random sample that an independently and
        identically distributed distribution with zero mean and
        variance `\\sigma^2` has autocovariance function `\\gamma(h)`
        with `\\gamma(0) = \\sigma^2` and `\\gamma(h) = 0` for `h\\neq 0`. ::

            sage: set_random_seed(0)
            sage: v = stats.TimeSeries(10^6)
            sage: v.randomize(\'normal\', 0, 5)
            [3.3835, -2.0055, 1.7882, -2.9319, -4.6827 ...
             -5.1868, 9.2613, 0.9274, -6.2282, -8.7652]
            sage: v.autocovariance(0)
            24.95410689...
            sage: v.autocovariance(1)
            -0.00508390...
            sage: v.autocovariance(2)
            0.022056325...
            sage: v.autocovariance(3)
            -0.01902000..."""
    def autoregressive_fit(self, M: Int) -> TimeSeries:
        """
        This method fits the time series to an autoregressive process
        of order ``M``. That is, we assume the process is given by
        `X_t-\\mu=a_1(X_{t-1}-\\mu)+a_2(X_{t-1}-\\mu)+\\cdots+a_M(X_{t-M}-\\mu)+Z_t`
        where `\\mu` is the mean of the process and `Z_t` is noise.
        This method returns estimates for `a_1,\\dots,a_M`.

        The method works by solving the Yule-Walker equations
        `\\Gamma a =\\gamma`, where `\\gamma=(\\gamma(1),\\dots,\\gamma(M))`,
        `a=(a_1,\\dots,a_M)`  with `\\gamma(i)` the autocovariance of lag `i`
        and `\\Gamma_{ij}=\\gamma(i-j)`.


        .. WARNING::

            The input sequence is assumed to be stationary, which
            means that the autocovariance `\\langle y_j y_k \\rangle` depends
            only on the difference `|j-k|`.

        INPUT:

        - ``M`` -- integer

        OUTPUT: a time series -- the coefficients of the autoregressive process

        EXAMPLES::

            sage: set_random_seed(0)
            sage: v = stats.TimeSeries(10^4).randomize('normal').sums()
            sage: F = v.autoregressive_fit(100)
            sage: v
            [0.6767, 0.2756, 0.6332, 0.0469, -0.8897 ... 87.6759, 87.6825, 87.4120, 87.6639, 86.3194]
            sage: v.autoregressive_forecast(F)
            86.0177285042...
            sage: F
            [1.0148, -0.0029, -0.0105, 0.0067, -0.0232 ... -0.0106, -0.0068, 0.0085, -0.0131, 0.0092]

            sage: set_random_seed(0)
            sage: t = stats.TimeSeries(2000)
            sage: z = stats.TimeSeries(2000)
            sage: z.randomize('normal',1)
            [1.6767, 0.5989, 1.3576, 0.4136, 0.0635 ... 1.0057, -1.1467, 1.2809, 1.5705, 1.1095]
            sage: t[0]=1
            sage: t[1]=2
            sage: for i in range(2,2000):
            ....:     t[i]=t[i-1]-0.5*t[i-2]+z[i]
            sage: c=t[0:-1].autoregressive_fit(2)  #recovers recurrence relation
            sage: c #should be close to [1,-0.5]
            [1.0371, -0.5199]"""
        ...
    def autoregressive_forecast(self, filter: TimeSeries) -> float:
        """
        Given the autoregression coefficients as outputted by the
        :meth:`autoregressive_fit` command, compute the forecast for the next
        term in the series.

        INPUT:

        - ``filter`` -- a time series outputted by the ``autoregressive_fit``
          command

        EXAMPLES::

            sage: set_random_seed(0)
            sage: v = stats.TimeSeries(100).randomize('normal').sums()
            sage: F = v[:-1].autoregressive_fit(5); F
            [1.0019, -0.0524, -0.0643, 0.1323, -0.0539]
            sage: v.autoregressive_forecast(F)
            11.7820298611...
            sage: v
            [0.6767, 0.2756, 0.6332, 0.0469, -0.8897 ... 9.2447, 9.6709, 10.4037, 10.4836, 12.1960]
        """
    def central_moment(self, k: Int) -> Real:
        """
        Return the `k`-th central moment of ``self``, which is just the mean
        of the `k`-th powers of the differences ``self[i] - mu``, where ``mu`` is
        the mean of ``self``.

        INPUT:

        - ``k`` -- positive integer

        OUTPUT: double

        EXAMPLES::

            sage: v = stats.TimeSeries([1,2,3])
            sage: v.central_moment(2)
            0.6666666666666666

        Note that the central moment is different from the moment
        here, since the mean is not `0`::

            sage: v.moment(2)     # doesn't subtract off mean
            4.666666666666667

        We compute the central moment directly::

            sage: mu = v.mean(); mu
            2.0
            sage: ((1-mu)^2 + (2-mu)^2 + (3-mu)^2) / 3
            0.6666666666666666"""
    def clip_remove(self, min: Real | None = None, max: Real | None = None) -> TimeSeries:
        """
        Return new time series obtained from ``self`` by removing all
        values that are less than or equal to a certain minimum value
        or greater than or equal to a certain maximum.

        INPUT:

        - ``min`` -- (default: ``None``) ``None`` or double

        - ``max`` -- (default: ``None``) ``None`` or double

        OUTPUT: a time series

        EXAMPLES::

            sage: v = stats.TimeSeries([1..10])
            sage: v.clip_remove(3,7)
            [3.0000, 4.0000, 5.0000, 6.0000, 7.0000]
            sage: v.clip_remove(3)
            [3.0000, 4.0000, 5.0000, 6.0000, 7.0000, 8.0000, 9.0000, 10.0000]
            sage: v.clip_remove(max=7)
            [1.0000, 2.0000, 3.0000, 4.0000, 5.0000, 6.0000, 7.0000]"""
    @overload
    def correlation(self, other: TimeSeries) -> Real:
        """
        Return the correlation of ``self`` and ``other``, which is the
        covariance of ``self`` and ``other`` divided by the product of their
        standard deviation.

        INPUT:

        - ``self``, ``other`` -- time series

        Whichever time series has more terms is truncated.

        EXAMPLES::

            sage: v = stats.TimeSeries([1,-2,3]); w = stats.TimeSeries([4,5,-10])
            sage: v.correlation(w)
            -0.558041609...
            sage: v.covariance(w)/(v.standard_deviation() * w.standard_deviation())
            -0.558041609..."""
    @overload
    def correlation(self, w) -> Any:
        """
        Return the correlation of ``self`` and ``other``, which is the
        covariance of ``self`` and ``other`` divided by the product of their
        standard deviation.

        INPUT:

        - ``self``, ``other`` -- time series

        Whichever time series has more terms is truncated.

        EXAMPLES::

            sage: v = stats.TimeSeries([1,-2,3]); w = stats.TimeSeries([4,5,-10])
            sage: v.correlation(w)
            -0.558041609...
            sage: v.covariance(w)/(v.standard_deviation() * w.standard_deviation())
            -0.558041609..."""
    def covariance(self, other: TimeSeries) -> Real:
        """
        Return the covariance of the time series ``self`` and ``other``.

        INPUT:

        - ``self``, ``other`` -- time series

        Whichever time series has more terms is truncated.

        EXAMPLES::

            sage: v = stats.TimeSeries([1,-2,3]); w = stats.TimeSeries([4,5,-10])
            sage: v.covariance(w)
            -11.777777777777779"""
    def diffs(self, k: Int = 1) -> TimeSeries:
        """
        Return the new time series got by taking the differences of
        successive terms in the time series.  So if ``self`` is the time
        series `X_0, X_1, X_2, \\dots`, then this function outputs the
        series `X_1 - X_0, X_2 - X_1, \\dots`.  The output series has one
        less term than the input series.  If the optional parameter
        `k` is given, return `X_k - X_0, X_{2k} - X_k, \\dots`.

        INPUT:

        - ``k`` -- positive integer (default: 1)

        OUTPUT: a new time series

        EXAMPLES::

            sage: v = stats.TimeSeries([5,4,1.3,2,8]); v
            [5.0000, 4.0000, 1.3000, 2.0000, 8.0000]
            sage: v.diffs()
            [-1.0000, -2.7000, 0.7000, 6.0000]"""
    def exp(self) -> TimeSeries:
        """
        Return new time series got by applying the exponential map to
        all the terms in the time series.

        OUTPUT: a new time series

        EXAMPLES::

            sage: v = stats.TimeSeries([1..5]); v
            [1.0000, 2.0000, 3.0000, 4.0000, 5.0000]
            sage: v.exp()
            [2.7183, 7.3891, 20.0855, 54.5982, 148.4132]
            sage: v.exp().log()
            [1.0000, 2.0000, 3.0000, 4.0000, 5.0000]"""
    def exponential_moving_average(self, alpha: Real) -> TimeSeries:
        """
        Return the exponential moving average time series.

        Assumes the input time series was constant with its starting
        value for negative time.  The `t`-th step of the output is the
        sum of the previous `k-1` steps of ``self`` and the `k`-th
        step divided by `k`.

        The 0-th term is formally undefined, so we define it to be 0,
        and we define the first term to be ``self[0]``.

        INPUT:

        - ``alpha`` -- float; a smoothing factor with ``0 <= alpha <= 1``

        OUTPUT: a time series with the same number of steps as ``self``

        EXAMPLES::

            sage: v = stats.TimeSeries([1,1,1,2,3]); v
            [1.0000, 1.0000, 1.0000, 2.0000, 3.0000]
            sage: v.exponential_moving_average(0)
            [0.0000, 1.0000, 1.0000, 1.0000, 1.0000]
            sage: v.exponential_moving_average(1)
            [0.0000, 1.0000, 1.0000, 1.0000, 2.0000]
            sage: v.exponential_moving_average(0.5)
            [0.0000, 1.0000, 1.0000, 1.0000, 1.5000]

        Some more examples::

            sage: v = stats.TimeSeries([1,2,3,4,5])
            sage: v.exponential_moving_average(1)
            [0.0000, 1.0000, 2.0000, 3.0000, 4.0000]
            sage: v.exponential_moving_average(0)
            [0.0000, 1.0000, 1.0000, 1.0000, 1.0000]"""
    def extend(self, right: TimeSeries | int | Integer | Vector_real_double_dense | ndarray) -> None:
        """
        Extend this time series by appending elements from the iterable
        ``right``.

        INPUT:

        - ``right`` -- iterable that can be converted to a time series

        EXAMPLES::

            sage: v = stats.TimeSeries([1,2,-5]); v
            [1.0000, 2.0000, -5.0000]
            sage: v.extend([-3.5, 2])
            sage: v
            [1.0000, 2.0000, -5.0000, -3.5000, 2.0000]"""
    def fft(self, overwrite: bool = False) -> Self:
        """
        Return the real discrete fast Fourier transform of ``self``, as a
        real time series:

        .. MATH::

            [y(0),\\Re(y(1)),\\Im(y(1)),\\dots,\\Re(y(n/2))]  \\text{ if $n$ is even}

            [y(0),\\Re(y(1)),\\Im(y(1)),\\dots,\\Re(y(n/2)),\\Im(y(n/2))] \\text{ if $n$ is odd}

        where

        .. MATH::

            y(j) = \\sum_{k=0}^{n-1} x[k] \\cdot \\exp(-\\sqrt{-1} \\cdot jk \\cdot 2\\pi/n)

        for `j = 0,\\dots,n-1`.  Note that `y(-j) = y(n-j)`.

        EXAMPLES::

            sage: v = stats.TimeSeries([1..9]); v
            [1.0000, 2.0000, 3.0000, 4.0000, 5.0000, 6.0000, 7.0000, 8.0000, 9.0000]
            sage: w = v.fft(); w
            [45.0000, -4.5000, 12.3636, -4.5000, 5.3629, -4.5000, 2.5981, -4.5000, 0.7935]

        We get just the series of real parts of ::

            sage: stats.TimeSeries([w[0]]) + w[1:].scale_time(2)
            [45.0000, -4.5000, -4.5000, -4.5000, -4.5000]

        An example with an even number of terms::

            sage: v = stats.TimeSeries([1..10]); v
            [1.0000, 2.0000, 3.0000, 4.0000, 5.0000, 6.0000, 7.0000, 8.0000, 9.0000, 10.0000]
            sage: w = v.fft(); w
            [55.0000, -5.0000, 15.3884, -5.0000, 6.8819, -5.0000, 3.6327, -5.0000, 1.6246, -5.0000]
            sage: v.fft().ifft()
            [1.0000, 2.0000, 3.0000, 4.0000, 5.0000, 6.0000, 7.0000, 8.0000, 9.0000, 10.0000]
        """
    def histogram(self, bins: Int = 50, normalize: bool = False
        ) -> tuple[list[int], list[tuple[Real, Real]]]:
        """
        Return the frequency histogram of the values in
        this time series divided up into the given
        number of bins.

        INPUT:

        - ``bins`` -- positive integer (default: 50)

        - ``normalize`` -- boolean (default: ``False``); whether to normalize so the
          total area in the bars of the histogram is 1

        OUTPUT:

        - counts -- list of counts of numbers of elements in each bin

        - endpoints -- list of 2-tuples (a,b) that give the endpoints of the bins

        EXAMPLES::

            sage: v = stats.TimeSeries([5,4,1.3,2,8,10,3,-5]); v
            [5.0000, 4.0000, 1.3000, 2.0000, 8.0000, 10.0000, 3.0000, -5.0000]
            sage: v.histogram(3)
            ([1, 4, 3], [(-5.0, 0.0), (0.0, 5.0), (5.0, 10.0)])"""
    def hurst_exponent(self) -> Real:
        """
        Return an estimate of the Hurst exponent of this time series.

        We use the algorithm from pages 61 -- 63 of [Peteres, Fractal
        Market Analysis (1994); see Google Books].

        We define the Hurst exponent of a constant time series to be 1.

        EXAMPLES:

        The Hurst exponent of Brownian motion is 1/2.  We approximate
        it with some specific samples.  Note that the estimator is
        biased and slightly overestimates. ::

            sage: set_random_seed(0)
            sage: bm = stats.TimeSeries(10^5).randomize('normal').sums(); bm
            [0.6767, 0.2756, 0.6332, 0.0469, -0.8897 ...
             152.2437, 151.5327, 152.7629, 152.9169, 152.9084]
            sage: bm.hurst_exponent()
            0.527450972..."""
    def ifft(self, overwrite: bool = False) -> Self:
        """
        Return the real discrete inverse fast Fourier transform of
        ``self``, which is also a real time series.

        This is the inverse of ``fft()``.

        The returned real array contains

        .. MATH::

            [y(0),y(1),\\dots,y(n-1)]

        where for `n` is even

        .. MATH::

            y(j)
            =
            1/n \\left(
            \\sum_{k=1}^{n/2-1}
            (x[2k-1]+\\sqrt{-1} \\cdot x[2k])
            \\cdot \\exp(\\sqrt{-1} \\cdot jk \\cdot 2pi/n)
            + c.c. + x[0] + (-1)^j x[n-1]
            \\right)

        and for `n` is odd

        .. MATH::

            y(j)
            =
            1/n \\left(
            \\sum_{k=1}^{(n-1)/2}
            (x[2k-1]+\\sqrt{-1} \\cdot x[2k])
            \\cdot \\exp(\\sqrt{-1} \\cdot jk \\cdot 2pi/n)
            + c.c. + x[0]
            \\right)

        where `c.c.` denotes complex conjugate of preceding expression.

        EXAMPLES::

            sage: v = stats.TimeSeries([1..10]); v
            [1.0000, 2.0000, 3.0000, 4.0000, 5.0000, 6.0000, 7.0000, 8.0000, 9.0000, 10.0000]
            sage: v.ifft()
            [5.1000, -5.6876, 1.4764, -1.0774, 0.4249, -0.1000, -0.2249, 0.6663, -1.2764, 1.6988]
            sage: v.ifft().fft()
            [1.0000, 2.0000, 3.0000, 4.0000, 5.0000, 6.0000, 7.0000, 8.0000, 9.0000, 10.0000]
        """
    def list(self) -> list[float]:
        """
        Return list of elements of ``self``.

        EXAMPLES::

            sage: v = stats.TimeSeries([1,-4,3,-2.5,-4,3])
            sage: v.list()
            [1.0, -4.0, 3.0, -2.5, -4.0, 3.0]"""
    def log(self) -> TimeSeries:
        """
        Return new time series got by taking the logarithms of all the
        terms in the time series.

        OUTPUT: a new time series

        EXAMPLES:

        We exponentiate then log a time series and get back
        the original series::

            sage: v = stats.TimeSeries([1,-4,3,-2.5,-4,3]); v
            [1.0000, -4.0000, 3.0000, -2.5000, -4.0000, 3.0000]
            sage: v.exp()
            [2.7183, 0.0183, 20.0855, 0.0821, 0.0183, 20.0855]
            sage: v.exp().log()
            [1.0000, -4.0000, 3.0000, -2.5000, -4.0000, 3.0000]

        Log of 0 gives ``-inf``::

            sage: stats.TimeSeries([1,0,3]).log()[1]
            -inf"""
    @overload
    def max(self, index: Literal[True]) -> tuple[Real, int]: ...
    @overload
    def max(self, index: Literal[False] = False) -> Real:
        """
        Return the largest value in this time series. If this series
        has length 0 we raise a :exc:`ValueError`.

        INPUT:

        - ``index`` -- boolean (default: ``False``); if ``True``, also return
          index of maximum entry

        OUTPUT:

        - float; largest value

        - integer; index of largest value (only returned if ``index=True``)

        EXAMPLES::

            sage: v = stats.TimeSeries([1,-4,3,-2.5,-4,3])
            sage: v.max()
            3.0
            sage: v.max(index=True)
            (3.0, 2)"""
    def mean(self) -> Real:
        """
        Return the mean (average) of the elements of ``self``.

        OUTPUT: double

        EXAMPLES::

            sage: v = stats.TimeSeries([1,1,1,2,3]); v
            [1.0000, 1.0000, 1.0000, 2.0000, 3.0000]
            sage: v.mean()
            1.6"""
    @overload
    def min(self, index: Literal[True]) -> tuple[Real, int]: ...
    @overload
    def min(self, index: Literal[False] = False) -> Real:
        """
        Return the smallest value in this time series.

        If this series has length 0, we raise a :exc:`ValueError`.

        INPUT:

        - ``index`` -- boolean (default: ``False``); if ``True``, also return
          index of minimal entry

        OUTPUT:

        - float; smallest value

        - integer; index of smallest value (only returned if ``index=True``)

        EXAMPLES::

            sage: v = stats.TimeSeries([1,-4,3,-2.5,-4])
            sage: v.min()
            -4.0
            sage: v.min(index=True)
            (-4.0, 1)"""
    def moment(self, k: Int) -> Real:
        """
        Return the `k`-th moment of ``self``, which is just the
        mean of the `k`-th powers of the elements of ``self``.

        INPUT:

        - ``k`` -- positive integer

        OUTPUT: double

        EXAMPLES::

            sage: v = stats.TimeSeries([1,1,1,2,3]); v
            [1.0000, 1.0000, 1.0000, 2.0000, 3.0000]
            sage: v.moment(1)
            1.6
            sage: v.moment(2)
            3.2"""
    def numpy(self, copy: bool = True) -> ndarray:
        """
        Return a NumPy version of this time series.

        .. NOTE::

            If copy is ``False``, return a NumPy 1-D array reference to
            exactly the same block of memory as this time series.  This is
            very, very fast and makes it easy to quickly use all
            NumPy/SciPy functionality on ``self``.  However, it is dangerous
            because when this time series goes out of scope and is garbage
            collected, the corresponding NumPy reference object will point
            to garbage.

        INPUT:

        - ``copy`` -- boolean (default: ``True``)

        OUTPUT: a numpy 1-D array

        EXAMPLES::

            sage: v = stats.TimeSeries([1,-3,4.5,-2])
            sage: w = v.numpy(copy=False); w
            array([ 1. , -3. ,  4.5, -2. ])
            sage: type(w)
            <... 'numpy.ndarray'>
            sage: w.shape
            (4,)

        Notice that changing ``w`` also changes ``v`` too! ::

            sage: w[0] = 20
            sage: w
            array([20. , -3. ,  4.5, -2. ])
            sage: v
            [20.0000, -3.0000, 4.5000, -2.0000]

        If you want a separate copy do not give the ``copy=False`` option. ::

            sage: z = v.numpy(); z
            array([20. , -3. ,  4.5, -2. ])
            sage: z[0] = -10
            sage: v
            [20.0000, -3.0000, 4.5000, -2.0000]"""
    def plot(
        self, 
        plot_points: Int = 1000, 
        points: bool = False, 
        **kwds
    ) -> Any:
        """TimeSeries.plot(self, Py_ssize_t plot_points=1000, points=False, **kwds)

        File: /build/sagemath/src/sage/src/sage/stats/time_series.pyx (starting at line 1011)

        Return a plot of this time series.

        The plot shows a line or points through
        `(i,T(i))`, where `i` ranges over nonnegative integers up to the
        length of ``self``.

        INPUT:

        - ``plot_points`` -- (default: 1000) 0 or positive integer. Only
          plot the given number of equally spaced points in the time series.
          If 0, plot all points.

        - ``points`` -- boolean (default: ``False``); if ``True``, return just
          the points of the time series

        - ``**kwds`` -- passed to the line or point command

        EXAMPLES::

            sage: # needs sage.plot
            sage: v = stats.TimeSeries([5,4,1.3,2,8,10,3,-5]); v
            [5.0000, 4.0000, 1.3000, 2.0000, 8.0000, 10.0000, 3.0000, -5.0000]
            sage: v.plot()
            Graphics object consisting of 1 graphics primitive
            sage: v.plot(points=True)
            Graphics object consisting of 1 graphics primitive
            sage: v.plot() + v.plot(points=True, rgbcolor='red')
            Graphics object consisting of 2 graphics primitives
            sage: v.plot() + v.plot(points=True, rgbcolor='red', pointsize=50)
            Graphics object consisting of 2 graphics primitives"""
    def plot_candlestick(self, bins: Int = 30) -> Graphics:
        """
        Return a candlestick plot of this time series with the given number
        of bins.

        A candlestick plot is a style of bar-chart used to view open, high,
        low, and close stock data. At each bin, the line represents the
        high / low range. The bar represents the open / close range. The
        interval is colored blue if the open for that bin is less than the
        close. If the close is less than the open, then that bin is colored
        red instead.

        INPUT:

        - ``bins`` -- positive integer (default: 30); the number of bins
          or candles

        OUTPUT: a candlestick plot

        EXAMPLES:

        Here we look at the candlestick plot for Brownian motion::

            sage: v = stats.TimeSeries(1000).randomize()
            sage: v.plot_candlestick(bins=20)                                           # needs sage.plot
            Graphics object consisting of 40 graphics primitives"""
    def plot_histogram(self, bins: Int = 50, normalize: bool = True, **kwds) -> Graphics:
        """
        Return histogram plot of this time series with given number of bins.

        INPUT:

        - ``bins`` -- positive integer (default: 50)

        - ``normalize`` -- boolean (default: ``True``); whether to normalize so the
          total area in the bars of the histogram is 1

        OUTPUT: a histogram plot

        EXAMPLES::

            sage: v = stats.TimeSeries([1..50])
            sage: v.plot_histogram(bins=10)                                             # needs sage.plot
            Graphics object consisting of 10 graphics primitives

        ::

            sage: v.plot_histogram(bins=3,normalize=False,aspect_ratio=1)               # needs sage.plot
            Graphics object consisting of 3 graphics primitives"""
    def pow(self, k: Real) -> TimeSeries:
        """
        Return a new time series with all elements of ``self`` raised to the
        `k`-th power.

        INPUT:

        - ``k`` -- a float

        OUTPUT: a time series

        EXAMPLES::

            sage: v = stats.TimeSeries([1,1,1,2,3]); v
            [1.0000, 1.0000, 1.0000, 2.0000, 3.0000]
            sage: v.pow(2)
            [1.0000, 1.0000, 1.0000, 4.0000, 9.0000]"""
    def prod(self) -> Real:
        """
        Return the product of all the entries of ``self``.

        If ``self`` has length 0, returns 1.

        OUTPUT: double

        EXAMPLES::

            sage: v = stats.TimeSeries([1,1,1,2,3]); v
            [1.0000, 1.0000, 1.0000, 2.0000, 3.0000]
            sage: v.prod()
            6.0"""
    def randomize(
        self, 
        distribution: Literal["uniform", "normal", "semicircle", "lognormal"]="uniform", 
        loc: Real = 0, scale: Real = 1, 
        **kwds
    ) -> Self:
        """
        Randomize the entries in this time series, and return a reference
        to ``self``.  Thus this function both changes ``self`` in place, and
        returns a copy of ``self``, for convenience.

        INPUT:

        - ``distribution`` -- (default: ``\'uniform\'``) supported values are:

          - ``\'uniform\'`` -- from ``loc`` to ``loc + scale``

          - ``\'normal\'`` -- mean ``loc`` and standard deviation ``scale``

          - ``\'semicircle\'`` -- with center at ``loc`` (``scale`` is ignored)

          - ``\'lognormal\'`` -- mean ``loc`` and standard deviation ``scale``

        - ``loc`` -- float (default: 0)

        - ``scale`` -- float (default: 1)

        .. NOTE::

            All random numbers are generated using algorithms that
            build on the high quality GMP random number function
            gmp_urandomb_ui.  Thus this function fully respects the Sage
            ``set_random_state`` command.  It\'s not quite as fast as the C
            library random number generator, but is of course much better
            quality, and is platform independent.

        EXAMPLES:

        We generate 5 uniform random numbers in the interval [0,1]::

            sage: set_random_seed(0)
            sage: stats.TimeSeries(5).randomize()
            [0.8685, 0.2816, 0.0229, 0.1456, 0.7314]

        We generate 5 uniform random numbers from 5 to `5+2=7`::

            sage: set_random_seed(0)
            sage: stats.TimeSeries(10).randomize(\'uniform\', 5, 2)
            [6.7369, 5.5632, 5.0459, 5.2911, 6.4628, 5.2412, 5.2010, 5.2761, 5.5813, 5.5439]

        We generate 5 normal random values with mean 0 and variance 1. ::

            sage: set_random_seed(0)
            sage: stats.TimeSeries(5).randomize(\'normal\')
            [0.6767, -0.4011, 0.3576, -0.5864, -0.9365]

        We generate 10 normal random values with mean 5 and variance 2. ::

            sage: set_random_seed(0)
            sage: stats.TimeSeries(10).randomize(\'normal\', 5, 2)
            [6.3534, 4.1978, 5.7153, 3.8273, 3.1269, 2.9598, 3.7484, 6.7472, 3.8986, 4.6271]

        We generate 5 values using the semicircle distribution. ::

            sage: set_random_seed(0)
            sage: stats.TimeSeries(5).randomize(\'semicircle\')
            [0.7369, -0.9541, 0.4628, -0.7990, -0.4187]

        We generate 1 million normal random values and create a frequency
        histogram. ::

            sage: set_random_seed(0)
            sage: a = stats.TimeSeries(10^6).randomize(\'normal\')
            sage: a.histogram(10)[0]
            [36, 1148, 19604, 130699, 340054, 347870, 137953, 21290, 1311, 35]

        We take the above values, and compute the proportion that lie within
        1, 2, 3, 5, and 6 standard deviations of the mean (0)::

            sage: s = a.standard_deviation()
            sage: len(a.clip_remove(-s,s))/float(len(a))
            0.683094
            sage: len(a.clip_remove(-2*s,2*s))/float(len(a))
            0.954559
            sage: len(a.clip_remove(-3*s,3*s))/float(len(a))
            0.997228
            sage: len(a.clip_remove(-5*s,5*s))/float(len(a))
            0.999998

        There were no "six sigma events"::

            sage: len(a.clip_remove(-6*s,6*s))/float(len(a))
            1.0"""
    def range_statistic(self, b: Int | None = None) -> Real:
        """
        Return the rescaled range statistic `R/S` of ``self``, which is
        defined as follows (see Hurst 1951).  If the optional
        parameter ``b`` is given, return the average of `R/S` range
        statistics of disjoint blocks of size ``b``.

        Let `\\sigma` be the standard deviation of the sequence of
        differences of ``self``, and let `Y_k` be the `k`-th term of ``self``.
        Let `n` be the number of terms of ``self``, and set
        `Z_k = Y_k - ((k+1)/n) \\cdot Y_n`. Then

        .. MATH::

            R/S = \\big( \\max(Z_k) - \\min(Z_k) \\big) / \\sigma

        where the max and min are over all `Z_k`.
        Basically replacing `Y_k` by `Z_k` allows us to measure
        the difference from the line from the origin to `(n,Y_n)`.

        INPUT:

        - ``self`` -- a time series  (*not* the series of differences)

        - ``b`` -- integer (default: ``None``); if given instead divide the
          input time series up into ``j = floor(n/b)`` disjoint
          blocks, compute the `R/S` statistic for each block,
          and return the average of those `R/S` statistics.

        OUTPUT: float

        EXAMPLES:

        Notice that if we make a Brownian motion random walk, there
        is no difference if we change the standard deviation. ::

            sage: set_random_seed(0); stats.TimeSeries(10^6).randomize('normal').sums().range_statistic()
            1897.8392602...
            sage: set_random_seed(0); stats.TimeSeries(10^6).randomize('normal',0,100).sums().range_statistic()
            1897.8392602..."""
    def rescale(self, s: Real) -> None:
        """
        Change ``self`` by multiplying every value in the series by ``s``.

        INPUT:

        - ``s`` -- a float

        EXAMPLES::

            sage: v = stats.TimeSeries([5,4,1.3,2,8,10,3,-5]); v
            [5.0000, 4.0000, 1.3000, 2.0000, 8.0000, 10.0000, 3.0000, -5.0000]
            sage: v.rescale(0.5)
            sage: v
            [2.5000, 2.0000, 0.6500, 1.0000, 4.0000, 5.0000, 1.5000, -2.5000]"""
    def reversed(self) -> TimeSeries:
        """
        Return new time series obtain from this time series by
        reversing the order of the entries in this time series.

        OUTPUT: a time series

        EXAMPLES::

            sage: v = stats.TimeSeries([1..5])
            sage: v.reversed()
            [5.0000, 4.0000, 3.0000, 2.0000, 1.0000]"""
    def scale(self, s: Real) -> TimeSeries:
        """
        Return new time series obtained by multiplying every value in the
        series by ``s``.

        INPUT:

        - ``s`` -- a float

        OUTPUT: a new time series with all values multiplied by ``s``

        EXAMPLES::

            sage: v = stats.TimeSeries([5,4,1.3,2,8,10,3,-5]); v
            [5.0000, 4.0000, 1.3000, 2.0000, 8.0000, 10.0000, 3.0000, -5.0000]
            sage: v.scale(0.5)
            [2.5000, 2.0000, 0.6500, 1.0000, 4.0000, 5.0000, 1.5000, -2.5000]"""
    def scale_time(self, k: Int) -> TimeSeries:
        """
        Return the new time series at scale ``k``.  If the input
        time series is `X_0, X_1, X_2, \\dots`, then this function
        returns the shorter time series `X_0, X_k, X_{2k}, \\dots`.

        INPUT:

        - ``k`` -- positive integer

        OUTPUT: a new time series

        EXAMPLES::

            sage: v = stats.TimeSeries([5,4,1.3,2,8,10,3,-5]); v
            [5.0000, 4.0000, 1.3000, 2.0000, 8.0000, 10.0000, 3.0000, -5.0000]
            sage: v.scale_time(1)
            [5.0000, 4.0000, 1.3000, 2.0000, 8.0000, 10.0000, 3.0000, -5.0000]
            sage: v.scale_time(2)
            [5.0000, 1.3000, 8.0000, 3.0000]
            sage: v.scale_time(3)
            [5.0000, 2.0000]
            sage: v.scale_time(10)
            []

        A series of odd length::

            sage: v = stats.TimeSeries([1..5]); v
            [1.0000, 2.0000, 3.0000, 4.0000, 5.0000]
            sage: v.scale_time(2)
            [1.0000, 3.0000, 5.0000]

        TESTS::

            sage: v.scale_time(0)
            Traceback (most recent call last):
            ...
            ValueError: k must be positive
            sage: v.scale_time(-1)
            Traceback (most recent call last):
            ...
            ValueError: k must be positive"""
    def show(self) -> Graphics:
        """
        Return a plot of this time series.

        This is an alias of :meth:`plot`.

        EXAMPLES:

        Draw a plot of a time series::

            sage: stats.TimeSeries([1..10]).show()                                      # needs sage.plot
            Graphics object consisting of 1 graphics primitive"""
    def simple_moving_average(self, k: Int) -> TimeSeries:
        """
        Return the moving average time series over the last `k` time units.

        Assumes the input time series was constant with its starting value
        for negative time.  The `t`-th step of the output is the sum of
        the previous `k - 1` steps of ``self`` and the `k`-th step
        divided by `k`. Thus `k` values are averaged at each point.

        INPUT:

        - ``k`` -- positive integer

        OUTPUT: a time series with the same number of steps as ``self``

        EXAMPLES::

            sage: v = stats.TimeSeries([1,1,1,2,3]); v
            [1.0000, 1.0000, 1.0000, 2.0000, 3.0000]
            sage: v.simple_moving_average(0)
            [1.0000, 1.0000, 1.0000, 2.0000, 3.0000]
            sage: v.simple_moving_average(1)
            [1.0000, 1.0000, 1.0000, 2.0000, 3.0000]
            sage: v.simple_moving_average(2)
            [1.0000, 1.0000, 1.0000, 1.5000, 2.5000]
            sage: v.simple_moving_average(3)
            [1.0000, 1.0000, 1.0000, 1.3333, 2.0000]"""
    def standard_deviation(self) -> Real:
        """
        Return the standard deviation of the entries of ``self``.

        INPUT:

        - ``bias`` -- boolean (default: ``False``); if ``False``, divide by
          ``self.length() - 1`` instead of ``self.length()`` to give a less
          biased estimator for the variance.

        OUTPUT: double

        EXAMPLES::

            sage: v = stats.TimeSeries([1,1,1,2,3]); v
            [1.0000, 1.0000, 1.0000, 2.0000, 3.0000]
            sage: v.standard_deviation()
            0.8944271909...
            sage: v.standard_deviation(bias=True)
            0.8

        TESTS::

            sage: stats.TimeSeries([1]).standard_deviation()
            0.0
            sage: stats.TimeSeries([]).standard_deviation()
            0.0"""
    def sum(self) -> Real:
        """
        Return the sum of all the entries of ``self``.

        If ``self`` has length 0, returns 0.

        OUTPUT: double

        EXAMPLES::

            sage: v = stats.TimeSeries([1,1,1,2,3]); v
            [1.0000, 1.0000, 1.0000, 2.0000, 3.0000]
            sage: v.sum()
            8.0"""
    def sums(self, s: Real = 0) -> TimeSeries:
        """
        Return the new time series got by taking the running partial
        sums of the terms of this time series.

        INPUT:

        - ``s`` -- starting value for partial sums

        OUTPUT: a time series

        EXAMPLES::

            sage: v = stats.TimeSeries([1,1,1,2,3]); v
            [1.0000, 1.0000, 1.0000, 2.0000, 3.0000]
            sage: v.sums()
            [1.0000, 2.0000, 3.0000, 5.0000, 8.0000]"""
    def variance(self, bias: bool = False) -> Real:
        """
        Return the variance of the elements of ``self``, which is the mean
        of the squares of the differences from the mean.

        INPUT:

        - ``bias`` -- boolean (default: ``False``); if ``False``, divide by
          ``self.length() - 1`` instead of ``self.length()`` to give a less
          biased estimator for the variance.

        OUTPUT: double

        EXAMPLES::

            sage: v = stats.TimeSeries([1,1,1,2,3]); v
            [1.0000, 1.0000, 1.0000, 2.0000, 3.0000]
            sage: v.variance()
            0.8
            sage: v.variance(bias=True)
            0.64

        TESTS::

            sage: stats.TimeSeries([1]).variance()
            0.0
            sage: stats.TimeSeries([]).variance()
            0.0"""
    def vector(self) -> Vector_real_double_dense:
        """TimeSeries.vector(self)

        File: /build/sagemath/src/sage/src/sage/stats/time_series.pyx (starting at line 240)

        Return real double vector whose entries are the values of this
        time series.  This is useful since vectors have standard
        algebraic structure and play well with matrices.

        OUTPUT: a real double vector

        EXAMPLES::

            sage: v = stats.TimeSeries([1..10])
            sage: v.vector()
            (1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0)"""
    def __add__(self, right: TimeSeries) -> TimeSeries:
        """
        Concatenate the time series ``self`` and ``right``.

        .. NOTE::

            To add a single number to the entries of a time series,
            use the ``add_scalar`` method, and to add componentwise use
            the ``add_entries`` method.

        INPUT:

        - ``right`` -- a time series

        OUTPUT: a time series

        EXAMPLES::

            sage: v = stats.TimeSeries([1,2,3]); w = stats.TimeSeries([1,2])
            sage: v + w
            [1.0000, 2.0000, 3.0000, 1.0000, 2.0000]
            sage: v = stats.TimeSeries([1,2,-5]); v
            [1.0000, 2.0000, -5.0000]

        Note that both summands must be a time series::

            sage: v + list(range(4))
            Traceback (most recent call last):
            ...
            TypeError: right operand must be a time series
            sage: [1,5] + v
            Traceback (most recent call last):
            ...
            TypeError: left operand must be a time series"""
    def __copy__(self) -> TimeSeries:
        """
        Return a copy of ``self``.

        EXAMPLES::

            sage: v = stats.TimeSeries([1,-4,3,-2.5,-4,3])
            sage: v.__copy__()
            [1.0000, -4.0000, 3.0000, -2.5000, -4.0000, 3.0000]
            sage: copy(v)
            [1.0000, -4.0000, 3.0000, -2.5000, -4.0000, 3.0000]
            sage: copy(v) is v
            False"""
    def __dealloc__(self) -> None:
        r"""
        Free up memory used by a time series.

        EXAMPLES:

        This tests ``__dealloc__`` implicitly::

            sage: v = stats.TimeSeries([1,3,-4,5])
            sage: del v
        """
    def __delitem__(self, other) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __getitem__(self, i: Int | slice) -> Any:
        """
        Return `i`-th entry or slice of ``self``.

        EXAMPLES::

            sage: v = stats.TimeSeries([1,-4,3,-2.5,-4,3])
            sage: v[2]
            3.0
            sage: v[-1]
            3.0
            sage: v[-10]
            Traceback (most recent call last):
            ...
            IndexError: TimeSeries index out of range
            sage: v[5]
            3.0
            sage: v[6]
            Traceback (most recent call last):
            ...
            IndexError: TimeSeries index out of range

        Some slice examples::

            sage: v[-3:]
            [-2.5000, -4.0000, 3.0000]
            sage: v[-3:-1]
            [-2.5000, -4.0000]
            sage: v[::2]
            [1.0000, 3.0000, -4.0000]
            sage: v[3:20]
            [-2.5000, -4.0000, 3.0000]
            sage: v[3:2]
            []

        Make a copy::

            sage: v[:]
            [1.0000, -4.0000, 3.0000, -2.5000, -4.0000, 3.0000]

        Reverse the time series::

            sage: v[::-1]
            [3.0000, -4.0000, -2.5000, 3.0000, -4.0000, 1.0000]"""
    def __gt__(self, other: object) -> bool: ...
    def __le__(self, other: object) -> bool: ...
    def __len__(self) -> int:
        r"""
        Return the number of entries in this time series.

        OUTPUT: Python integer

        EXAMPLES::

            sage: v = stats.TimeSeries([1,3.1908439,-4,5.93932])
            sage: v.__len__()
            4
            sage: len(v)
            4
        """
    def __lt__(self, other: object) -> bool: ...
    def __mul__(self, right: Int) -> TimeSeries:
        """
        Multiply a time series by an integer n, which (like for lists)
        results in the time series concatenated with itself n times.

        .. NOTE::

            To multiply all the entries of a time series by a single
            scalar, use the ``scale`` method.

        INPUT:

        - ``left``, ``right`` -- integer and a time series

        OUTPUT: a time series

        EXAMPLES::

            sage: v = stats.TimeSeries([1,2,-5]); v
            [1.0000, 2.0000, -5.0000]
            sage: v*3
            [1.0000, 2.0000, -5.0000, 1.0000, 2.0000, -5.0000, 1.0000, 2.0000, -5.0000]
            sage: 3*v
            [1.0000, 2.0000, -5.0000, 1.0000, 2.0000, -5.0000, 1.0000, 2.0000, -5.0000]
            sage: v*v
            Traceback (most recent call last):
            ...
            TypeError: 'sage.stats.time_series.TimeSeries' object cannot be interpreted as an integer
        """
    def __ne__(self, other: object) -> bool: ...
    def __radd__(self, other: TimeSeries) -> TimeSeries: ...
    def __reduce__(self) -> tuple:
        """
        Used in pickling time series.

        EXAMPLES::

            sage: v = stats.TimeSeries([1,-3.5])
            sage: v.__reduce__()
            (<cyfunction unpickle_time_series_v1 at ...>, (..., 2))
            sage: loads(dumps(v)) == v
            True

        Note that dumping and loading with compress ``False`` is much faster,
        though dumping with compress ``True`` can save a lot of space::

            sage: v = stats.TimeSeries([1..10^5])
            sage: loads(dumps(v, compress=False),compress=False) == v
            True"""
    def __repr__(self) -> str:
        r"""
        Return string representation of ``self``.

        EXAMPLES::

            sage: v = stats.TimeSeries([1,3.1908439,-4,5.93932])
            sage: v.__repr__()
            '[1.0000, 3.1908, -4.0000, 5.9393]'

        By default 4 digits after the decimal point are displayed.  To
        change this, change ``sage.stats.time_series.digits``. ::

            sage: sage.stats.time_series.digits = 2
            sage: v.__repr__()
            '[1.00, 3.19, -4.00, 5.94]'
            sage: v
            [1.00, 3.19, -4.00, 5.94]
            sage: sage.stats.time_series.digits = 4
            sage: v
            [1.0000, 3.1908, -4.0000, 5.9393]
        """
    def __richcmp__(self, other: object, op: int) -> bool:
        r"""
        Compare ``self`` and ``other``.  This has the same semantics
        as list comparison.

        EXAMPLES::

            sage: v = stats.TimeSeries([1,2,3]); w = stats.TimeSeries([1,2])
            sage: v < w
            False
            sage: w < v
            True
            sage: v == v
            True
            sage: w == w
            True
        """
    def __rmul__(self, other: Int) -> TimeSeries: ...
    def __setitem__(self, i: int, x: float) -> Any:
        """
        Set the `i`-th entry of ``self`` to ``x``.

        INPUT:

        - ``i`` -- nonnegative integer

        - ``x`` -- a float

        EXAMPLES::

            sage: v = stats.TimeSeries([1,3,-4,5.93932]); v
            [1.0000, 3.0000, -4.0000, 5.9393]
            sage: v[0] = -5.5; v
            [-5.5000, 3.0000, -4.0000, 5.9393]
            sage: v[-1] = 3.2; v
            [-5.5000, 3.0000, -4.0000, 3.2000]
            sage: v[10]
            Traceback (most recent call last):
            ...
            IndexError: TimeSeries index out of range
            sage: v[-5]
            Traceback (most recent call last):
            ...
            IndexError: TimeSeries index out of range"""
