import _cython_3_2_1
from sage.rings.integer import Integer as Integer
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

max_print: int
unpickle_intlist_v1: _cython_3_2_1.cython_function_or_method

class IntList:
    """IntList(values)

    File: /build/sagemath/src/sage/src/sage/stats/intlist.pyx (starting at line 43)

    A list of C int's."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, values) -> Any:
        """File: /build/sagemath/src/sage/src/sage/stats/intlist.pyx (starting at line 58)

                Create an initialized list of C ints.

                INPUT:

                - ``values`` -- int, long, Integer, list of integers, or a TimeSeries

                If the input is a time series or list of floats, then the
                integer parts of the entries are taken (not the floor).

                EXAMPLES::

                    sage: stats.IntList(8)
                    [0, 0, 0, 0, 0, 0, 0, 0]

                    sage: stats.IntList([1,5,-39392])
                    [1, 5, -39392]

                We check for overflow when creating the IntList::

                    sage: stats.IntList([1, 3, 2^32])
                    Traceback (most recent call last):
                    ...
                    OverflowError: ... too large to convert to C long  # 32-bit
                    OverflowError: ... too large to convert to int     # 64-bit

                Printing omits entries::

                    sage: stats.IntList(1000)
                    [0, 0, 0, 0, 0 ... 0, 0, 0, 0, 0]

                Floats are truncated to their integer parts::

                    sage: stats.IntList([1.1, -2.6])
                    [1, -2]
                    sage: stats.IntList(stats.TimeSeries([1.1, -2.6]))
                    [1, -2]
        """
    @overload
    def list(self) -> Any:
        """IntList.list(self)

        File: /build/sagemath/src/sage/src/sage/stats/intlist.pyx (starting at line 307)

        Return Python list version of ``self`` with Python ints as entries.

        EXAMPLES::

            sage: a = stats.IntList([1..15]); a
            [1, 2, 3, 4, 5 ... 11, 12, 13, 14, 15]
            sage: a.list()
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
            sage: list(a) == a.list()
            True
            sage: type(a.list()[0])
            <... 'int'>"""
    @overload
    def list(self) -> Any:
        """IntList.list(self)

        File: /build/sagemath/src/sage/src/sage/stats/intlist.pyx (starting at line 307)

        Return Python list version of ``self`` with Python ints as entries.

        EXAMPLES::

            sage: a = stats.IntList([1..15]); a
            [1, 2, 3, 4, 5 ... 11, 12, 13, 14, 15]
            sage: a.list()
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
            sage: list(a) == a.list()
            True
            sage: type(a.list()[0])
            <... 'int'>"""
    @overload
    def list(self, a) -> Any:
        """IntList.list(self)

        File: /build/sagemath/src/sage/src/sage/stats/intlist.pyx (starting at line 307)

        Return Python list version of ``self`` with Python ints as entries.

        EXAMPLES::

            sage: a = stats.IntList([1..15]); a
            [1, 2, 3, 4, 5 ... 11, 12, 13, 14, 15]
            sage: a.list()
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
            sage: list(a) == a.list()
            True
            sage: type(a.list()[0])
            <... 'int'>"""
    @overload
    def list(self) -> Any:
        """IntList.list(self)

        File: /build/sagemath/src/sage/src/sage/stats/intlist.pyx (starting at line 307)

        Return Python list version of ``self`` with Python ints as entries.

        EXAMPLES::

            sage: a = stats.IntList([1..15]); a
            [1, 2, 3, 4, 5 ... 11, 12, 13, 14, 15]
            sage: a.list()
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
            sage: list(a) == a.list()
            True
            sage: type(a.list()[0])
            <... 'int'>"""
    @overload
    def max(self, boolindex=...) -> Any:
        """IntList.max(self, bool index=False)

        File: /build/sagemath/src/sage/src/sage/stats/intlist.pyx (starting at line 452)

        Return the largest value in this time series. If this series
        has length 0 we raise a :exc:`ValueError`

        INPUT:

        - ``index`` -- boolean (default: ``False``); if ``True``, also return
          index of maximum entry

        OUTPUT:

        - integer -- largest value
        - integer -- index of largest value; only returned if ``index=True``

        EXAMPLES::

            sage: v = stats.IntList([1,-4,3,-2,-4,3])
            sage: v.max()
            3
            sage: v.max(index=True)
            (3, 2)"""
    @overload
    def max(self) -> Any:
        """IntList.max(self, bool index=False)

        File: /build/sagemath/src/sage/src/sage/stats/intlist.pyx (starting at line 452)

        Return the largest value in this time series. If this series
        has length 0 we raise a :exc:`ValueError`

        INPUT:

        - ``index`` -- boolean (default: ``False``); if ``True``, also return
          index of maximum entry

        OUTPUT:

        - integer -- largest value
        - integer -- index of largest value; only returned if ``index=True``

        EXAMPLES::

            sage: v = stats.IntList([1,-4,3,-2,-4,3])
            sage: v.max()
            3
            sage: v.max(index=True)
            (3, 2)"""
    @overload
    def max(self, index=...) -> Any:
        """IntList.max(self, bool index=False)

        File: /build/sagemath/src/sage/src/sage/stats/intlist.pyx (starting at line 452)

        Return the largest value in this time series. If this series
        has length 0 we raise a :exc:`ValueError`

        INPUT:

        - ``index`` -- boolean (default: ``False``); if ``True``, also return
          index of maximum entry

        OUTPUT:

        - integer -- largest value
        - integer -- index of largest value; only returned if ``index=True``

        EXAMPLES::

            sage: v = stats.IntList([1,-4,3,-2,-4,3])
            sage: v.max()
            3
            sage: v.max(index=True)
            (3, 2)"""
    @overload
    def min(self, boolindex=...) -> Any:
        """IntList.min(self, bool index=False)

        File: /build/sagemath/src/sage/src/sage/stats/intlist.pyx (starting at line 414)

        Return the smallest value in this integer list.  If this
        series has length 0 we raise a :exc:`ValueError`.

        INPUT:

        - ``index`` -- boolean (default: ``False``); if ``True``, also return
          index of minimal entry

        OUTPUT:

        - ``float`` -- smallest value
        - ``integer`` -- index of smallest value; only returned if
          ``index=True``

        EXAMPLES::

            sage: v = stats.IntList([1,-4,3,-2,-4])
            sage: v.min()
            -4
            sage: v.min(index=True)
            (-4, 1)"""
    @overload
    def min(self) -> Any:
        """IntList.min(self, bool index=False)

        File: /build/sagemath/src/sage/src/sage/stats/intlist.pyx (starting at line 414)

        Return the smallest value in this integer list.  If this
        series has length 0 we raise a :exc:`ValueError`.

        INPUT:

        - ``index`` -- boolean (default: ``False``); if ``True``, also return
          index of minimal entry

        OUTPUT:

        - ``float`` -- smallest value
        - ``integer`` -- index of smallest value; only returned if
          ``index=True``

        EXAMPLES::

            sage: v = stats.IntList([1,-4,3,-2,-4])
            sage: v.min()
            -4
            sage: v.min(index=True)
            (-4, 1)"""
    @overload
    def min(self, index=...) -> Any:
        """IntList.min(self, bool index=False)

        File: /build/sagemath/src/sage/src/sage/stats/intlist.pyx (starting at line 414)

        Return the smallest value in this integer list.  If this
        series has length 0 we raise a :exc:`ValueError`.

        INPUT:

        - ``index`` -- boolean (default: ``False``); if ``True``, also return
          index of minimal entry

        OUTPUT:

        - ``float`` -- smallest value
        - ``integer`` -- index of smallest value; only returned if
          ``index=True``

        EXAMPLES::

            sage: v = stats.IntList([1,-4,3,-2,-4])
            sage: v.min()
            -4
            sage: v.min(index=True)
            (-4, 1)"""
    @overload
    def plot(self, *args, **kwds) -> Any:
        """IntList.plot(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/stats/intlist.pyx (starting at line 510)

        Return a plot of this :class:`IntList`.

        This just constructs the
        corresponding double-precision floating point :class:`TimeSeries`
        object, passing on all arguments.

        EXAMPLES::

            sage: stats.IntList([3,7,19,-2]).plot()                                     # needs sage.plot
            Graphics object consisting of 1 graphics primitive
            sage: stats.IntList([3,7,19,-2]).plot(color='red',                          # needs sage.plot
            ....:                                 pointsize=50, points=True)
            Graphics object consisting of 1 graphics primitive"""
    @overload
    def plot(self) -> Any:
        """IntList.plot(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/stats/intlist.pyx (starting at line 510)

        Return a plot of this :class:`IntList`.

        This just constructs the
        corresponding double-precision floating point :class:`TimeSeries`
        object, passing on all arguments.

        EXAMPLES::

            sage: stats.IntList([3,7,19,-2]).plot()                                     # needs sage.plot
            Graphics object consisting of 1 graphics primitive
            sage: stats.IntList([3,7,19,-2]).plot(color='red',                          # needs sage.plot
            ....:                                 pointsize=50, points=True)
            Graphics object consisting of 1 graphics primitive"""
    @overload
    def plot(self, color=..., # needs sage.plot
....: pointsize = ..., points=...) -> Any:
        """IntList.plot(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/stats/intlist.pyx (starting at line 510)

        Return a plot of this :class:`IntList`.

        This just constructs the
        corresponding double-precision floating point :class:`TimeSeries`
        object, passing on all arguments.

        EXAMPLES::

            sage: stats.IntList([3,7,19,-2]).plot()                                     # needs sage.plot
            Graphics object consisting of 1 graphics primitive
            sage: stats.IntList([3,7,19,-2]).plot(color='red',                          # needs sage.plot
            ....:                                 pointsize=50, points=True)
            Graphics object consisting of 1 graphics primitive"""
    @overload
    def plot_histogram(self, *args, **kwds) -> Any:
        """IntList.plot_histogram(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/stats/intlist.pyx (starting at line 528)

        Return a histogram plot of this :class:`IntList`.

        This just constructs
        the corresponding double-precision floating point :class:`TimeSeries` object,
        and plots it, passing on all arguments.

        EXAMPLES::

            sage: stats.IntList([1..15]).plot_histogram()                               # needs sage.plot
            Graphics object consisting of 50 graphics primitives"""
    @overload
    def plot_histogram(self) -> Any:
        """IntList.plot_histogram(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/stats/intlist.pyx (starting at line 528)

        Return a histogram plot of this :class:`IntList`.

        This just constructs
        the corresponding double-precision floating point :class:`TimeSeries` object,
        and plots it, passing on all arguments.

        EXAMPLES::

            sage: stats.IntList([1..15]).plot_histogram()                               # needs sage.plot
            Graphics object consisting of 50 graphics primitives"""
    @overload
    def prod(self) -> int:
        """IntList.prod(self) -> int

        File: /build/sagemath/src/sage/src/sage/stats/intlist.pyx (starting at line 349)

        Return the product of the entries of ``self``.

        EXAMPLES::

            sage: a = stats.IntList([1..10]); a
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            sage: a.prod()
            3628800
            sage: factorial(10)
            3628800

        Note that there can be overflow::

            sage: a = stats.IntList([2^30, 2]); a
            [1073741824, 2]
            sage: a.prod()
            -2147483648
 """
    @overload
    def prod(self) -> Any:
        """IntList.prod(self) -> int

        File: /build/sagemath/src/sage/src/sage/stats/intlist.pyx (starting at line 349)

        Return the product of the entries of ``self``.

        EXAMPLES::

            sage: a = stats.IntList([1..10]); a
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            sage: a.prod()
            3628800
            sage: factorial(10)
            3628800

        Note that there can be overflow::

            sage: a = stats.IntList([2^30, 2]); a
            [1073741824, 2]
            sage: a.prod()
            -2147483648
 """
    @overload
    def prod(self) -> Any:
        """IntList.prod(self) -> int

        File: /build/sagemath/src/sage/src/sage/stats/intlist.pyx (starting at line 349)

        Return the product of the entries of ``self``.

        EXAMPLES::

            sage: a = stats.IntList([1..10]); a
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            sage: a.prod()
            3628800
            sage: factorial(10)
            3628800

        Note that there can be overflow::

            sage: a = stats.IntList([2^30, 2]); a
            [1073741824, 2]
            sage: a.prod()
            -2147483648
 """
    @overload
    def sum(self) -> int:
        """IntList.sum(self) -> int

        File: /build/sagemath/src/sage/src/sage/stats/intlist.pyx (starting at line 325)

        Return the sum of the entries of ``self``.

        EXAMPLES::

            sage: stats.IntList([1..100]).sum()
            5050

        Note that there can be overflow, since the entries are C ints::

            sage: a = stats.IntList([2^30,2^30]); a
            [1073741824, 1073741824]
            sage: a.sum()
            -2147483648"""
    @overload
    def sum(self) -> Any:
        """IntList.sum(self) -> int

        File: /build/sagemath/src/sage/src/sage/stats/intlist.pyx (starting at line 325)

        Return the sum of the entries of ``self``.

        EXAMPLES::

            sage: stats.IntList([1..100]).sum()
            5050

        Note that there can be overflow, since the entries are C ints::

            sage: a = stats.IntList([2^30,2^30]); a
            [1073741824, 1073741824]
            sage: a.sum()
            -2147483648"""
    @overload
    def sum(self) -> Any:
        """IntList.sum(self) -> int

        File: /build/sagemath/src/sage/src/sage/stats/intlist.pyx (starting at line 325)

        Return the sum of the entries of ``self``.

        EXAMPLES::

            sage: stats.IntList([1..100]).sum()
            5050

        Note that there can be overflow, since the entries are C ints::

            sage: a = stats.IntList([2^30,2^30]); a
            [1073741824, 1073741824]
            sage: a.sum()
            -2147483648"""
    @overload
    def time_series(self) -> Any:
        """IntList.time_series(self)

        File: /build/sagemath/src/sage/src/sage/stats/intlist.pyx (starting at line 488)

        Return :class:`TimeSeries` version of ``self``, which involves changing
        each entry to a double.

        EXAMPLES::

            sage: T = stats.IntList([-2,3,5]).time_series(); T
            [-2.0000, 3.0000, 5.0000]
            sage: type(T)
            <... 'sage.stats.time_series.TimeSeries'>"""
    @overload
    def time_series(self) -> Any:
        """IntList.time_series(self)

        File: /build/sagemath/src/sage/src/sage/stats/intlist.pyx (starting at line 488)

        Return :class:`TimeSeries` version of ``self``, which involves changing
        each entry to a double.

        EXAMPLES::

            sage: T = stats.IntList([-2,3,5]).time_series(); T
            [-2.0000, 3.0000, 5.0000]
            sage: type(T)
            <... 'sage.stats.time_series.TimeSeries'>"""
    def __add__(self, left, right) -> Any:
        """IntList.__add__(left, right)

        File: /build/sagemath/src/sage/src/sage/stats/intlist.pyx (starting at line 394)

        Concatenate the integer lists ``self`` and ``right``.

        EXAMPLES::

            sage: stats.IntList([-2,3,5]) + stats.IntList([1,1,17])
            [-2, 3, 5, 1, 1, 17]"""
    def __delitem__(self, other) -> None:
        """Delete self[key]."""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __getitem__(self, i) -> Any:
        """IntList.__getitem__(self, i)

        File: /build/sagemath/src/sage/src/sage/stats/intlist.pyx (starting at line 182)

        Return i-th entry or slice of self, following standard Python
        semantics.  The returned slice is an intlist, and the returned
        entry is a Python int.

        INPUT:

        - ``i`` -- integer or slice

        EXAMPLES::

            sage: a = stats.IntList([0..9]); a
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            sage: a[5]
            5
            sage: a[-2]
            8
            sage: a[5:-2]
            [5, 6, 7]
            sage: type(a[5:-2])
            <... 'sage.stats.intlist.IntList'>
            sage: type(a[5])
            <... 'int'>"""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __len__(self) -> Any:
        """IntList.__len__(self)

        File: /build/sagemath/src/sage/src/sage/stats/intlist.pyx (starting at line 377)

        Return the number of entries in this time series.

        OUTPUT: Python integer

        EXAMPLES::

            sage: len(stats.IntList([1..15]))
            15
            sage: len(stats.IntList([]))
            0
            sage: len(stats.IntList(10^6))
            1000000"""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __radd__(self, other):
        """Return value+self."""
    @overload
    def __reduce__(self) -> Any:
        """IntList.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/stats/intlist.pyx (starting at line 281)

        Used in pickling int lists.

        EXAMPLES::

            sage: a = stats.IntList([-2,3,7,-4])
            sage: loads(dumps(a)) == a
            True

            sage: v = stats.IntList([1,-3])
            sage: v.__reduce__()
            (<cyfunction unpickle_intlist_v1 at ...>, (..., 2))
            sage: loads(dumps(v)) == v
            True

        Note that dumping and loading with compress ``False`` is much faster,
        though dumping with compress ``True`` can save a lot of space::

            sage: v = stats.IntList([1..10^5])
            sage: loads(dumps(v, compress=False),compress=False) == v
            True"""
    @overload
    def __reduce__(self) -> Any:
        """IntList.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/stats/intlist.pyx (starting at line 281)

        Used in pickling int lists.

        EXAMPLES::

            sage: a = stats.IntList([-2,3,7,-4])
            sage: loads(dumps(a)) == a
            True

            sage: v = stats.IntList([1,-3])
            sage: v.__reduce__()
            (<cyfunction unpickle_intlist_v1 at ...>, (..., 2))
            sage: loads(dumps(v)) == v
            True

        Note that dumping and loading with compress ``False`` is much faster,
        though dumping with compress ``True`` can save a lot of space::

            sage: v = stats.IntList([1..10^5])
            sage: loads(dumps(v, compress=False),compress=False) == v
            True"""
    def __setitem__(self, Py_ssize_ti, intx) -> Any:
        """IntList.__setitem__(self, Py_ssize_t i, int x)

        File: /build/sagemath/src/sage/src/sage/stats/intlist.pyx (starting at line 248)

        Set the i-th entry of self, following standard Python semantics.

        INPUT:

            - ``i`` -- integer
            - ``x`` -- integer

        EXAMPLES::

            sage: a = stats.IntList([-2,3,7,-4])
            sage: a[1] = 10393; a
            [-2, 10393, 7, -4]
            sage: a[-1] = -10; a
            [-2, 10393, 7, -10]
            sage: a[100]
            Traceback (most recent call last):
            ...
            IndexError: IntList index out of range
            sage: a[-100]
            Traceback (most recent call last):
            ...
            IndexError: IntList index out of range"""
