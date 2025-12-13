from sage.misc.functional import sqrt as sqrt
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.superseded import deprecation as deprecation
from sage.rings.integer_ring import ZZ as ZZ

def mean(v):
    """
    Return the mean of the elements of `v`.

    We define the mean of the empty list to be the (symbolic) NaN,
    following the convention of MATLAB, Scipy, and R.

    This function is deprecated.  Use :func:`numpy.mean` or :func:`numpy.nanmean`
    instead.

    INPUT:

    - ``v`` -- list of numbers

    OUTPUT: a number

    EXAMPLES::

        sage: mean([pi, e])                                                             # needs sage.symbolic
        doctest:warning...
        DeprecationWarning: sage.stats.basic_stats.mean is deprecated;
        use numpy.mean or numpy.nanmean instead
        See https://github.com/sagemath/sage/issues/29662 for details.
        1/2*pi + 1/2*e
        sage: mean([])                                                                  # needs sage.symbolic
        NaN
        sage: mean([I, sqrt(2), 3/5])                                                   # needs sage.symbolic
        1/3*sqrt(2) + 1/3*I + 1/5
        sage: mean([RIF(1.0103,1.0103), RIF(2)])                                        # needs sage.rings.real_interval_field
        1.5051500000000000?
        sage: mean(range(4))
        3/2
        sage: v = stats.TimeSeries([1..100])                                            # needs numpy
        sage: mean(v)                                                                   # needs numpy
        50.5
    """
def mode(v):
    """
    Return the mode of `v`.

    The mode is the list of the most frequently occurring
    elements in `v`. If `n` is the most times that any element occurs
    in `v`, then the mode is the list of elements of `v` that
    occur `n` times. The list is sorted if possible.

    This function is deprecated.  Use :func:`scipy:scipy.stats.mode` or
    :func:`statistics.mode` instead.

    .. NOTE::

        The elements of `v` must be hashable.

    INPUT:

    - ``v`` -- list

    OUTPUT: list (sorted if possible)

    EXAMPLES::

        sage: v = [1,2,4,1,6,2,6,7,1]
        sage: mode(v)
        doctest:warning...
        DeprecationWarning: sage.stats.basic_stats.mode is deprecated;
        use scipy.stats.mode or statistics.mode instead
        See https://github.com/sagemath/sage/issues/29662 for details.
        [1]
        sage: v.count(1)
        3
        sage: mode([])
        []

        sage: mode([1,2,3,4,5])
        [1, 2, 3, 4, 5]
        sage: mode([3,1,2,1,2,3])
        [1, 2, 3]
        sage: mode([0, 2, 7, 7, 13, 20, 2, 13])
        [2, 7, 13]

        sage: mode(['sage', 'four', 'I', 'three', 'sage', 'pi'])
        ['sage']

        sage: class MyClass:
        ....:   def mode(self):
        ....:       return [1]
        sage: stats.mode(MyClass())
        [1]
    """
def std(v, bias: bool = False):
    '''
    Return the standard deviation of the elements of `v`.

    We define the standard deviation of the empty list to be NaN,
    following the convention of MATLAB, Scipy, and R.

    This function is deprecated.  Use :func:`numpy.std` or :func:`numpy.nanstd`
    instead.

    INPUT:

    - ``v`` -- list of numbers

    - ``bias`` -- boolean (default: ``False``); if ``False``, divide by
      ``len(v) - 1`` instead of ``len(v)`` to give a less biased
      estimator (sample) for the standard deviation.

    OUTPUT: a number

    EXAMPLES::

        sage: # needs sage.symbolic
        sage: std([1..6], bias=True)
        doctest:warning...
        DeprecationWarning: sage.stats.basic_stats.std is deprecated;
        use numpy.std or numpy.nanstd instead
        See https://github.com/sagemath/sage/issues/29662 for details.
        doctest:warning...
        DeprecationWarning: sage.stats.basic_stats.variance is deprecated;
        use numpy.var or numpy.nanvar instead
        See https://github.com/sagemath/sage/issues/29662 for details.
        doctest:warning...
        DeprecationWarning: sage.stats.basic_stats.mean is deprecated;
        use numpy.mean or numpy.nanmean instead
        See https://github.com/sagemath/sage/issues/29662 for details.
        1/2*sqrt(35/3)
        sage: std([1..6], bias=False)
        sqrt(7/2)
        sage: std([e, pi])
        sqrt(1/2)*abs(pi - e)
        sage: std([])
        NaN
        sage: std([I, sqrt(2), 3/5])
        1/15*sqrt(1/2)*sqrt((10*sqrt(2) - 5*I - 3)^2
        + (5*sqrt(2) - 10*I + 3)^2 + (5*sqrt(2) + 5*I - 6)^2)
        sage: std([RIF(1.0103, 1.0103), RIF(2)])
        0.6998235813403261?

        sage: # needs numpy
        sage: import numpy
        sage: if int(numpy.version.short_version[0]) > 1:
        ....:     _ = numpy.set_printoptions(legacy="1.25")
        sage: x = numpy.array([1,2,3,4,5])
        sage: std(x, bias=False)
        1.5811388300841898
        sage: x = stats.TimeSeries([1..100])
        sage: std(x)
        29.011491975882016

    TESTS::

        sage: data = [random() for i in [1 .. 20]]
        sage: std(data)  # random
        0.29487771726609185
    '''
def variance(v, bias: bool = False):
    '''
    Return the variance of the elements of `v`.

    We define the variance of the empty list to be NaN,
    following the convention of MATLAB, Scipy, and R.

    This function is deprecated.  Use :func:`numpy.var` or :func:`numpy.nanvar`
    instead.

    INPUT:

    - ``v`` -- list of numbers

    - ``bias`` -- boolean (default: ``False``); if ``False``, divide by
      ``len(v) - 1`` instead of ``len(v)`` to give a less biased
      estimator (sample) for the standard deviation.

    OUTPUT: a number

    EXAMPLES::

        sage: variance([1..6])
        doctest:warning...
        DeprecationWarning: sage.stats.basic_stats.variance is deprecated;
        use numpy.var or numpy.nanvar instead
        See https://github.com/sagemath/sage/issues/29662 for details.
        7/2
        sage: variance([1..6], bias=True)
        35/12
        sage: variance([e, pi])                                                         # needs sage.symbolic
        1/2*(pi - e)^2
        sage: variance([])
        NaN
        sage: variance([I, sqrt(2), 3/5])                                               # needs sage.symbolic
        1/450*(10*sqrt(2) - 5*I - 3)^2 + 1/450*(5*sqrt(2) - 10*I + 3)^2
        + 1/450*(5*sqrt(2) + 5*I - 6)^2
        sage: variance([RIF(1.0103, 1.0103), RIF(2)])
        0.4897530450000000?
        sage: import numpy                                                              # needs numpy
        sage: if int(numpy.version.short_version[0]) > 1:                               # needs numpy
        ....:     _ = numpy.set_printoptions(legacy="1.25")                                 # needs numpy
        sage: x = numpy.array([1,2,3,4,5])                                              # needs numpy
        sage: variance(x, bias=False)                                                   # needs numpy
        2.5
        sage: x = stats.TimeSeries([1..100])
        sage: variance(x)
        841.6666666666666
        sage: variance(x, bias=True)
        833.25
        sage: class MyClass:
        ....:   def variance(self, bias=False):
        ....:      return 1
        sage: stats.variance(MyClass())
        1
        sage: class SillyPythonList:
        ....:   def __init__(self):
        ....:       self.__list = [2, 4]
        ....:   def __len__(self):
        ....:       return len(self.__list)
        ....:   def __iter__(self):
        ....:       return self.__list.__iter__()
        ....:   def mean(self):
        ....:       return 3
        sage: R = SillyPythonList()
        sage: variance(R)
        2
        sage: variance(R, bias=True)
        1

    TESTS:

    The performance issue from :issue:`10019` is solved::

        sage: variance([1] * 2^18)
        0
    '''
def median(v):
    """
    Return the median (middle value) of the elements of `v`.

    If `v` is empty, we define the median to be NaN, which is
    consistent with NumPy (note that R returns NULL).
    If `v` is comprised of strings, :exc:`TypeError` occurs.
    For elements other than numbers, the median is a result of :func:`sorted`.

    This function is deprecated.  Use :func:`numpy.median` or :func:`numpy.nanmedian`
    instead.

    INPUT:

    - ``v`` -- list

    OUTPUT: median element of `v`

    EXAMPLES::

        sage: median([1,2,3,4,5])
        doctest:warning...
        DeprecationWarning: sage.stats.basic_stats.median is deprecated;
        use numpy.median or numpy.nanmedian instead
        See https://github.com/sagemath/sage/issues/29662 for details.
        3
        sage: median([e, pi])                                                           # needs sage.symbolic
        1/2*pi + 1/2*e
        sage: median(['sage', 'linux', 'python'])
        'python'
        sage: median([])                                                                # needs sage.symbolic
        NaN
        sage: class MyClass:
        ....:    def median(self):
        ....:       return 1
        sage: stats.median(MyClass())
        1
    """
def moving_average(v, n):
    """
    Return the moving average of a list `v`.

    The moving average of a list is often used to smooth out noisy data.

    If `v` is empty, we define the entries of the moving average to be NaN.

    This method is deprecated.  Use :meth:`pandas.Series.rolling` instead.

    INPUT:

    - ``v`` -- list

    - ``n`` -- the number of values used in computing each average

    OUTPUT: list of length ``len(v)-n+1``, since we do not fabric any values

    EXAMPLES::

        sage: moving_average([1..10], 1)
        doctest:warning...
        DeprecationWarning: sage.stats.basic_stats.moving_average is deprecated;
        use pandas.Series.rolling instead
        See https://github.com/sagemath/sage/issues/29662 for details.
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        sage: moving_average([1..10], 4)
        [5/2, 7/2, 9/2, 11/2, 13/2, 15/2, 17/2]
        sage: moving_average([], 1)
        []
        sage: moving_average([pi, e, I, sqrt(2), 3/5], 2)                               # needs sage.symbolic
        [1/2*pi + 1/2*e, 1/2*e + 1/2*I, 1/2*sqrt(2) + 1/2*I,
         1/2*sqrt(2) + 3/10]

    We check if the input is a time series, and if so use the
    optimized :meth:`simple_moving_average` method, but with (slightly
    different) meaning as defined above (the point is that the
    :meth:`simple_moving_average` on time series returns `n` values::

        sage: a = stats.TimeSeries([1..10])                                             # needs numpy
        sage: stats.moving_average(a, 3)                                                # needs numpy
        [2.0000, 3.0000, 4.0000, 5.0000, 6.0000, 7.0000, 8.0000, 9.0000]
        sage: stats.moving_average(list(a), 3)                                          # needs numpy
        [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
    """
