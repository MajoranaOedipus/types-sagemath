import _cython_3_2_1
from typing import Any, ClassVar, overload

lazy_list: _cython_3_2_1.cython_function_or_method
lazy_list_formatter: _cython_3_2_1.cython_function_or_method
slice_unpickle: _cython_3_2_1.cython_function_or_method

class lazy_list_from_function(lazy_list_generic):
    """lazy_list_from_function(function, cache=None, stop=None)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, function, cache=..., stop=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/misc/lazy_list.pyx (starting at line 1000)

                INPUT:

                - ``function`` -- a function that maps ``n`` to the element
                  at position ``n`` (this function only needs to be defined for length
                  larger than the length of the cache)

                - ``cache`` -- an optional list to be used as the cache. Be careful that
                  there is no copy

                - ``stop`` -- an optional integer to specify the length of this lazy list
                  (Otherwise it is considered infinite)

                EXAMPLES::

                    sage: from sage.misc.lazy_list import lazy_list_from_function
                    sage: lazy_list_from_function(euler_phi)                                    # needs sage.libs.pari
                    lazy list [0, 1, 1, ...]
                    sage: lazy_list_from_function(divisors, [None])
                    lazy list [None, [1], [1, 2], ...]

                TESTS::

                    sage: def f(n):
                    ....:     if n >= 5: raise StopIteration
                    ....:     return 5 - n
                    sage: list(lazy_list_from_function(f))
                    [5, 4, 3, 2, 1]
        """
    def __reduce__(self) -> Any:
        """lazy_list_from_function.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_list.pyx (starting at line 1065)

        TESTS::

            sage: from sage.misc.lazy_list import lazy_list_from_function
            sage: loads(dumps(lazy_list_from_function(euler_phi)))                      # needs sage.libs.pari
            lazy list [0, 1, 1, ...]
            sage: loads(dumps(lazy_list_from_function(divisors, [None])))
            lazy list [None, [1], [1, 2], ...]"""

class lazy_list_from_iterator(lazy_list_generic):
    """lazy_list_from_iterator(iterator, cache=None, stop=None)

    File: /build/sagemath/src/sage/src/sage/misc/lazy_list.pyx (starting at line 896)

    Lazy list built from an iterator.

    EXAMPLES::

        sage: from sage.misc.lazy_list import lazy_list
        sage: from itertools import count
        sage: m = lazy_list(count()); m
        lazy list [0, 1, 2, ...]

        sage: m2 = lazy_list(count())[8:20551:2]
        sage: m2
        lazy list [8, 10, 12, ...]

        sage: x = iter(m)
        sage: [next(x), next(x), next(x)]
        [0, 1, 2]
        sage: y = iter(m)
        sage: [next(y), next(y), next(y)]
        [0, 1, 2]
        sage: [next(x), next(y)]
        [3, 3]
        sage: loads(dumps(m))
        lazy list [0, 1, 2, ...]"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, iterator, cache=..., stop=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/misc/lazy_list.pyx (starting at line 923)

                INPUT:

                - ``iterator`` -- an iterator

                - ``cache`` -- an optional list to be used as the cache; be careful that
                  there is no copy

                - ``stop`` -- an optional stop point

                TESTS::

                    sage: from sage.misc.lazy_list import lazy_list_from_iterator
                    sage: from itertools import count
                    sage: lazy_list_from_iterator(count())
                    lazy list [0, 1, 2, ...]
                    sage: lazy_list_from_iterator(count(), ['a'], 10)
                    lazy list ['a', 0, 1, ...]
                    sage: _._info()
                    cache length 4
                    start        0
                    stop         10
                    step         1
        """
    def __reduce__(self) -> Any:
        """lazy_list_from_iterator.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_list.pyx (starting at line 984)

        TESTS::

            sage: from sage.misc.lazy_list import lazy_list_from_iterator
            sage: from itertools import count
            sage: loads(dumps(lazy_list_from_iterator(count())))
            lazy list [0, 1, 2, ...]
            sage: loads(dumps(lazy_list_from_iterator(count(), ['a'])))
            lazy list ['a', 0, 1, ...]"""

class lazy_list_from_update_function(lazy_list_generic):
    """lazy_list_from_update_function(function, cache=None, stop=None)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, function, cache=..., stop=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/misc/lazy_list.pyx (starting at line 1082)

                INPUT:

                - ``function`` -- a function that updates a list of precomputed values
                  The update function should take as input a list and make it longer
                  (using either the methods ``append`` or ``extend``). If after a call
                  to the update function the list of values is shorter a
                  :exc:`RuntimeError` will occur. If no value is added then the lazy list
                  is considered finite.

                - ``cache`` -- an optional list to be used as the cache. Be careful that
                  there is no copy

                - ``stop`` -- an optional integer to specify the length of this lazy list
                  (otherwise it is considered infinite)

                TESTS::

                    sage: from sage.misc.lazy_list import lazy_list_from_update_function
                    sage: def update_function(values):
                    ....:     n = len(values)+1
                    ....:     values.extend([n]*n)
                    sage: l = lazy_list_from_update_function(update_function)
                    sage: l[:20].list()
                    [1, 2, 2, 4, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 16, 16, 16, 16, 16]
        """
    def __reduce__(self) -> Any:
        '''lazy_list_from_update_function.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_list.pyx (starting at line 1152)

        TESTS::

            sage: from sage.misc.lazy_list import lazy_list

            sage: def my_update_function(values): values.append(ZZ(len(values)).is_prime())
            sage: l = lazy_list(update_function=my_update_function)
            sage: l[4]
            False
            sage: loads(dumps(l))   # not tested (works in console though)
            lazy list [False, False, True, ...]

            sage: def say_hey(cache): print("hey")
            sage: l = lazy_list(update_function=say_hey, initial_values=range(10))
            sage: l._fit(10)
            hey
            1
            sage: l._info()
            cache length 10
            start        0
            stop         10
            step         1
            sage: l2 = loads(dumps(l))   # not tested
            sage: l2._info()             # not tested
            sage: l2._info()             # not tested
            cache length 10
            start        0
            stop         10
            step         1
            sage: l.list() == l2.list()  # not tested
            True'''

class lazy_list_generic:
    """lazy_list_generic(cache=None, start=None, stop=None, step=None)

    File: /build/sagemath/src/sage/src/sage/misc/lazy_list.pyx (starting at line 350)

    A lazy list.

    EXAMPLES::

        sage: from sage.misc.lazy_list import lazy_list
        sage: l = lazy_list(Primes())
        sage: l                                                                         # needs sage.libs.pari
        lazy list [2, 3, 5, ...]
        sage: l[200]                                                                    # needs sage.libs.pari
        1229"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, cache=..., start=..., stop=..., step=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/misc/lazy_list.pyx (starting at line 364)

                No check is performed on input and bad input can result in a Sage crash.
                You are advised to use the function :func:`lazy_list` instead. The only
                case where you might want to use directly this constructor is if you
                have a list that you want to wrap (without copy) into a lazy list.
                See in the example below.

                INPUT:

                - ``cache`` -- an optional list to be used as the cache. Be careful that
                  there is no copy

                - ``start``, ``stop``, ``step`` -- for slices

                .. NOTE::

                    Everywhere the constant ``PY_SSIZE_T_MAX`` plays the role of infinity

                EXAMPLES::

                    sage: from sage.misc.lazy_list import lazy_list_generic
                    sage: l = [0,1,2]
                    sage: ll = lazy_list_generic(l, 0, 2, None)
                    sage: ll
                    lazy list [0, 1]

                The above code may be dangerous since the lazy list holds a reference
                to the initial list::

                    sage: l[0] = 'haha'
                    sage: ll
                    lazy list ['haha', 1]
        """
    def get(self, Py_ssize_ti) -> Any:
        """lazy_list_generic.get(self, Py_ssize_t i)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_list.pyx (starting at line 611)

        Return the element at position ``i``.

        If the index is not an integer, then raise a :exc:`TypeError`.  If the
        argument is negative then raise a :exc:`ValueError`.  Finally, if the
        argument is beyond the size of that lazy list it raises a
        :exc:`IndexError`.

        EXAMPLES::

            sage: from sage.misc.lazy_list import lazy_list
            sage: from itertools import chain, repeat
            sage: f = lazy_list(chain(iter([1,2,3]), repeat('a')))
            sage: f.get(0)
            1
            sage: f.get(3)
            'a'
            sage: f.get(0)
            1
            sage: f.get(4)
            'a'

            sage: g = f[:10]
            sage: g.get(5)
            'a'
            sage: g.get(10)
            Traceback (most recent call last):
            ...
            IndexError: lazy list index out of range
            sage: g.get(1/2)
            Traceback (most recent call last):
            ...
            TypeError: unable to convert rational 1/2 to an integer"""
    @overload
    def list(self) -> Any:
        """lazy_list_generic.list(self)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_list.pyx (starting at line 403)

        Return the list made of the elements of ``self``.

        .. NOTE::

            If the iterator is sufficiently large, this will build a list
            of length ``PY_SSIZE_T_MAX`` which should be beyond the capacity of
            your RAM!

        EXAMPLES::

            sage: from sage.misc.lazy_list import lazy_list
            sage: P = lazy_list(Primes())
            sage: P[2:143:5].list()                                                     # needs sage.libs.pari
            [5, 19, 41, 61, 83, 107, 137, 163, 191, 223, 241, 271, 307, 337, 367,
             397, 431, 457, 487, 521, 563, 593, 617, 647, 677, 719, 751, 787, 823]
            sage: P = lazy_list(iter([1,2,3]))
            sage: P.list()
            [1, 2, 3]
            sage: P[:100000].list()
            [1, 2, 3]
            sage: P[1:7:2].list()
            [2]

        TESTS:

        Check that the cache is immutable::

            sage: lazy = lazy_list(iter(Primes()))[:5]
            sage: l = lazy.list(); l                                                    # needs sage.libs.pari
            [2, 3, 5, 7, 11]
            sage: l[0] = -1; l                                                          # needs sage.libs.pari
            [-1, 3, 5, 7, 11]
            sage: lazy.list()                                                           # needs sage.libs.pari
            [2, 3, 5, 7, 11]"""
    @overload
    def list(self) -> Any:
        """lazy_list_generic.list(self)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_list.pyx (starting at line 403)

        Return the list made of the elements of ``self``.

        .. NOTE::

            If the iterator is sufficiently large, this will build a list
            of length ``PY_SSIZE_T_MAX`` which should be beyond the capacity of
            your RAM!

        EXAMPLES::

            sage: from sage.misc.lazy_list import lazy_list
            sage: P = lazy_list(Primes())
            sage: P[2:143:5].list()                                                     # needs sage.libs.pari
            [5, 19, 41, 61, 83, 107, 137, 163, 191, 223, 241, 271, 307, 337, 367,
             397, 431, 457, 487, 521, 563, 593, 617, 647, 677, 719, 751, 787, 823]
            sage: P = lazy_list(iter([1,2,3]))
            sage: P.list()
            [1, 2, 3]
            sage: P[:100000].list()
            [1, 2, 3]
            sage: P[1:7:2].list()
            [2]

        TESTS:

        Check that the cache is immutable::

            sage: lazy = lazy_list(iter(Primes()))[:5]
            sage: l = lazy.list(); l                                                    # needs sage.libs.pari
            [2, 3, 5, 7, 11]
            sage: l[0] = -1; l                                                          # needs sage.libs.pari
            [-1, 3, 5, 7, 11]
            sage: lazy.list()                                                           # needs sage.libs.pari
            [2, 3, 5, 7, 11]"""
    @overload
    def list(self) -> Any:
        """lazy_list_generic.list(self)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_list.pyx (starting at line 403)

        Return the list made of the elements of ``self``.

        .. NOTE::

            If the iterator is sufficiently large, this will build a list
            of length ``PY_SSIZE_T_MAX`` which should be beyond the capacity of
            your RAM!

        EXAMPLES::

            sage: from sage.misc.lazy_list import lazy_list
            sage: P = lazy_list(Primes())
            sage: P[2:143:5].list()                                                     # needs sage.libs.pari
            [5, 19, 41, 61, 83, 107, 137, 163, 191, 223, 241, 271, 307, 337, 367,
             397, 431, 457, 487, 521, 563, 593, 617, 647, 677, 719, 751, 787, 823]
            sage: P = lazy_list(iter([1,2,3]))
            sage: P.list()
            [1, 2, 3]
            sage: P[:100000].list()
            [1, 2, 3]
            sage: P[1:7:2].list()
            [2]

        TESTS:

        Check that the cache is immutable::

            sage: lazy = lazy_list(iter(Primes()))[:5]
            sage: l = lazy.list(); l                                                    # needs sage.libs.pari
            [2, 3, 5, 7, 11]
            sage: l[0] = -1; l                                                          # needs sage.libs.pari
            [-1, 3, 5, 7, 11]
            sage: lazy.list()                                                           # needs sage.libs.pari
            [2, 3, 5, 7, 11]"""
    @overload
    def list(self) -> Any:
        """lazy_list_generic.list(self)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_list.pyx (starting at line 403)

        Return the list made of the elements of ``self``.

        .. NOTE::

            If the iterator is sufficiently large, this will build a list
            of length ``PY_SSIZE_T_MAX`` which should be beyond the capacity of
            your RAM!

        EXAMPLES::

            sage: from sage.misc.lazy_list import lazy_list
            sage: P = lazy_list(Primes())
            sage: P[2:143:5].list()                                                     # needs sage.libs.pari
            [5, 19, 41, 61, 83, 107, 137, 163, 191, 223, 241, 271, 307, 337, 367,
             397, 431, 457, 487, 521, 563, 593, 617, 647, 677, 719, 751, 787, 823]
            sage: P = lazy_list(iter([1,2,3]))
            sage: P.list()
            [1, 2, 3]
            sage: P[:100000].list()
            [1, 2, 3]
            sage: P[1:7:2].list()
            [2]

        TESTS:

        Check that the cache is immutable::

            sage: lazy = lazy_list(iter(Primes()))[:5]
            sage: l = lazy.list(); l                                                    # needs sage.libs.pari
            [2, 3, 5, 7, 11]
            sage: l[0] = -1; l                                                          # needs sage.libs.pari
            [-1, 3, 5, 7, 11]
            sage: lazy.list()                                                           # needs sage.libs.pari
            [2, 3, 5, 7, 11]"""
    @overload
    def list(self) -> Any:
        """lazy_list_generic.list(self)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_list.pyx (starting at line 403)

        Return the list made of the elements of ``self``.

        .. NOTE::

            If the iterator is sufficiently large, this will build a list
            of length ``PY_SSIZE_T_MAX`` which should be beyond the capacity of
            your RAM!

        EXAMPLES::

            sage: from sage.misc.lazy_list import lazy_list
            sage: P = lazy_list(Primes())
            sage: P[2:143:5].list()                                                     # needs sage.libs.pari
            [5, 19, 41, 61, 83, 107, 137, 163, 191, 223, 241, 271, 307, 337, 367,
             397, 431, 457, 487, 521, 563, 593, 617, 647, 677, 719, 751, 787, 823]
            sage: P = lazy_list(iter([1,2,3]))
            sage: P.list()
            [1, 2, 3]
            sage: P[:100000].list()
            [1, 2, 3]
            sage: P[1:7:2].list()
            [2]

        TESTS:

        Check that the cache is immutable::

            sage: lazy = lazy_list(iter(Primes()))[:5]
            sage: l = lazy.list(); l                                                    # needs sage.libs.pari
            [2, 3, 5, 7, 11]
            sage: l[0] = -1; l                                                          # needs sage.libs.pari
            [-1, 3, 5, 7, 11]
            sage: lazy.list()                                                           # needs sage.libs.pari
            [2, 3, 5, 7, 11]"""
    @overload
    def list(self) -> Any:
        """lazy_list_generic.list(self)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_list.pyx (starting at line 403)

        Return the list made of the elements of ``self``.

        .. NOTE::

            If the iterator is sufficiently large, this will build a list
            of length ``PY_SSIZE_T_MAX`` which should be beyond the capacity of
            your RAM!

        EXAMPLES::

            sage: from sage.misc.lazy_list import lazy_list
            sage: P = lazy_list(Primes())
            sage: P[2:143:5].list()                                                     # needs sage.libs.pari
            [5, 19, 41, 61, 83, 107, 137, 163, 191, 223, 241, 271, 307, 337, 367,
             397, 431, 457, 487, 521, 563, 593, 617, 647, 677, 719, 751, 787, 823]
            sage: P = lazy_list(iter([1,2,3]))
            sage: P.list()
            [1, 2, 3]
            sage: P[:100000].list()
            [1, 2, 3]
            sage: P[1:7:2].list()
            [2]

        TESTS:

        Check that the cache is immutable::

            sage: lazy = lazy_list(iter(Primes()))[:5]
            sage: l = lazy.list(); l                                                    # needs sage.libs.pari
            [2, 3, 5, 7, 11]
            sage: l[0] = -1; l                                                          # needs sage.libs.pari
            [-1, 3, 5, 7, 11]
            sage: lazy.list()                                                           # needs sage.libs.pari
            [2, 3, 5, 7, 11]"""
    @overload
    def list(self) -> Any:
        """lazy_list_generic.list(self)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_list.pyx (starting at line 403)

        Return the list made of the elements of ``self``.

        .. NOTE::

            If the iterator is sufficiently large, this will build a list
            of length ``PY_SSIZE_T_MAX`` which should be beyond the capacity of
            your RAM!

        EXAMPLES::

            sage: from sage.misc.lazy_list import lazy_list
            sage: P = lazy_list(Primes())
            sage: P[2:143:5].list()                                                     # needs sage.libs.pari
            [5, 19, 41, 61, 83, 107, 137, 163, 191, 223, 241, 271, 307, 337, 367,
             397, 431, 457, 487, 521, 563, 593, 617, 647, 677, 719, 751, 787, 823]
            sage: P = lazy_list(iter([1,2,3]))
            sage: P.list()
            [1, 2, 3]
            sage: P[:100000].list()
            [1, 2, 3]
            sage: P[1:7:2].list()
            [2]

        TESTS:

        Check that the cache is immutable::

            sage: lazy = lazy_list(iter(Primes()))[:5]
            sage: l = lazy.list(); l                                                    # needs sage.libs.pari
            [2, 3, 5, 7, 11]
            sage: l[0] = -1; l                                                          # needs sage.libs.pari
            [-1, 3, 5, 7, 11]
            sage: lazy.list()                                                           # needs sage.libs.pari
            [2, 3, 5, 7, 11]"""
    def __add__(self, other) -> Any:
        """lazy_list_generic.__add__(self, other)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_list.pyx (starting at line 469)

        If ``self`` is a list then return the lazy_list that consists of the
        concatenation of ``self`` and ``other``.

        TESTS::

            sage: from sage.misc.lazy_list import lazy_list
            sage: from itertools import count
            sage: l = lazy_list(i**3 - i + 1 for i in count()); l
            lazy list [1, 1, 7, ...]
            sage: p = ['huit', 'douze']
            sage: ll = p + l; ll
            lazy list ['huit', 'douze', 1, ...]
            sage: l[:10].list() == ll[2:12].list()
            True
            sage: p
            ['huit', 'douze']
            sage: ([0,2] + lazy_list([0,1])).list()
            [0, 2, 0, 1]"""
    def __call__(self, i) -> Any:
        """lazy_list_generic.__call__(self, i)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_list.pyx (starting at line 654)

        An alias for :meth:`get`.

        TESTS::

            sage: from sage.misc.lazy_list import lazy_list
            sage: from itertools import chain, repeat
            sage: f = lazy_list(chain(iter([1,2,3]), repeat('a')))
            sage: f(2)
            3
            sage: f(3)
            'a'"""
    def __getitem__(self, key) -> Any:
        """lazy_list_generic.__getitem__(self, key)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_list.pyx (starting at line 701)

        Return a lazy list which shares the same cache.

        EXAMPLES::

            sage: from sage.misc.lazy_list import lazy_list
            sage: f = lazy_list(iter([1,2,3]))
            sage: f0 = f[0:]
            sage: [f.get(0), f.get(1), f.get(2)]
            [1, 2, 3]
            sage: f1 = f[1:]
            sage: [f1.get(0), f1.get(1)]
            [2, 3]
            sage: f2 = f[2:]
            sage: f2.get(0)
            3
            sage: f3 = f[3:]
            sage: f3.get(0)
            Traceback (most recent call last):
            ...
            IndexError: lazy list index out of range

            sage: l = lazy_list([0]*12)[1::2]
            sage: l[2::3]
            lazy list [0, 0]
            sage: l[3::2]
            lazy list [0, 0]

        A lazy list automatically adjusts the indices in order that start and
        stop are congruent modulo step::

            sage: P = lazy_list(iter(Primes()))
            sage: P[1:12:4]._info()
            cache length 0
            start        1
            stop         13
            step         4
            sage: P[1:13:4]._info()
            cache length 0
            start        1
            stop         13
            step         4
            sage: P[1:14:4]._info()
            cache length 0
            start        1
            stop         17
            step         4
            sage: Q = P[100:1042233:12]
            sage: Q._info()
            cache length 0
            start        100
            stop         1042240
            step         12
            sage: R = Q[233::3]
            sage: R._info()
            cache length 0
            start        2896
            stop         1042252
            step         36
            sage: 1042252%36 == 2896%36
            True

        We check commutation::

            sage: l = lazy_list(iter(range(10000)))
            sage: l1 = l[::2][:3001]
            sage: l2 = l[:6002][::2]
            sage: l1._info()
            cache length 0
            start        0
            stop         6002
            step         2
            sage: l2._info()
            cache length 0
            start        0
            stop         6002
            step         2
            sage: l3 = l1[13::2][:50:2]
            sage: l4 = l1[:200][13:113:4]
            sage: l3._info()
            cache length 0
            start        26
            stop         226
            step         8
            sage: l4._info()
            cache length 0
            start        26
            stop         226
            step         8

        Further tests::

            sage: l = lazy_list(iter([0]*25))
            sage: l[2::3][2::3][4::5]
            lazy list []
            sage: l[2::5][3::][1::]
            lazy list [0]
            sage: l[3:24:2][1::][1:7:3]
            lazy list [0, 0]
            sage: l[::2][2::][2::3]
            lazy list [0, 0, 0]
            sage: l[4:3][:] is l[18:2]   # *the* empty_lazy_list
            True"""
    def __iter__(self) -> Any:
        """lazy_list_generic.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_list.pyx (starting at line 670)

        Return an iterator.

        TESTS::

            sage: from itertools import count
            sage: from sage.misc.lazy_list import lazy_list
            sage: iter(lazy_list(count()))
            <...generator object at 0x...>

        ::

            sage: l = lazy_list(i ** 2 for i in range(5))
            sage: list(l)
            [0, 1, 4, 9, 16]
            sage: l._info()
            cache length 5
            start        0
            stop         5
            step         1"""
    def __radd__(self, other):
        """Return value+self."""
    def __reduce__(self) -> Any:
        '''lazy_list_generic.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_list.pyx (starting at line 531)

        Pickling support.

        EXAMPLES::

            sage: from itertools import count
            sage: from sage.misc.lazy_list import lazy_list
            sage: m = lazy_list(count())
            sage: x = loads(dumps(m))
            sage: y = iter(x)
            sage: print("{} {} {}".format(next(y), next(y), next(y)))
            0 1 2
            sage: m2 = m[3::2]
            sage: loads(dumps(m2))
            lazy list [3, 5, 7, ...]'''
