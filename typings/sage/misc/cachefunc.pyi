import _cython_3_2_1
from sage.misc.decorators import decorator_keywords as decorator_keywords
from sage.misc.function_mangling import ArgumentFixer
from sage.misc.instancedoc import instancedoc as instancedoc
from sage.misc.sageinspect import sage_getargspec as sage_getargspec, sage_getfile_relative as sage_getfile_relative, sage_getsourcelines as sage_getsourcelines
from typing import Any, Callable, ClassVar, overload
from collections.abc import Hashable


__pyx_capi__: dict
def cache_key(o: Any) -> Hashable:
    r"""cache_key(o)

File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 579)

Helper function to return a hashable key for ``o`` which can be used for
caching.

This function is intended for objects which are not hashable such as
`p`-adic numbers. The difference from calling an object's ``_cache_key``
method directly, is that it also works for tuples and unpacks them
recursively (if necessary, i.e., if they are not hashable).

EXAMPLES::

    sage: from sage.misc.cachefunc import cache_key
    sage: K.<u> = Qq(9)                                                             # needs sage.rings.padics
    sage: a = K(1); a                                                               # needs sage.rings.padics
    1 + O(3^20)
    sage: cache_key(a)                                                              # needs sage.rings.padics
    (..., ((1,),), 0, 20)

This function works if ``o`` is a tuple. In this case it unpacks its
entries recursively::

    sage: o = (1, 2, (3, a))                                                        # needs sage.rings.padics
    sage: cache_key(o)                                                              # needs sage.rings.padics
    (1, 2, (3, (..., ((1,),), 0, 20)))

Note that tuples are only partially unpacked if some of its entries are
hashable::

    sage: o = (1/2, a)                                                              # needs sage.rings.padics
    sage: cache_key(o)                                                              # needs sage.rings.padics
    (1/2, (..., ((1,),), 0, 20))
"""

def cached_function(f: Callable, classmethod=False, *, name=None, key=None, do_pickle=None) -> CachedFunction:
    """CachedFunction(f, classmethod=False, *, name=None, key=None, do_pickle=None)

File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 632)

Create a cached version of a function, which only recomputes
values it hasn't already computed. Synonyme: ``cached_function``

INPUT:

- ``f`` -- a function
- ``name`` -- (optional string) name that the cached versi
  of ``f`` should be provided with
- ``key`` -- (optional callable) takes the input and returns a
  key for the cache, typically one would use this to normalize input
- ``do_pickle`` -- (optional boolean) whether or not the contents of the
  cache should be included when pickling this function; the default is not
  to include them.

If ``f`` is a function, do either ``g = CachedFunction(f)``
or ``g = cached_function(f)`` to make a cached version of ``f``,
or put ``@cached_function`` right before the definition of ``f``
(i.e., use Python decorators)::

    @cached_function
    def f(...):
        ....

The inputs to the function must be hashable or they must define
:meth:`sage.structure.sage_object.SageObject._cache_key`.

EXAMPLES::

    sage: @cached_function
    ....: def mul(x, y=2):
    ....:     return x*y
    sage: mul(3)
    6

We demonstrate that the result is cached, and that, moreover,
the cache takes into account the various ways of providing
default arguments::

    sage: mul(3) is mul(3,2)
    True
    sage: mul(3,y=2) is mul(3,2)
    True

The user can clear the cache::

    sage: a = mul(4)
    sage: mul.clear_cache()
    sage: a is mul(4)
    False

It is also possible to explicitly override the cache with
a different value::

    sage: mul.set_cache('foo',5)
    sage: mul(5,2)
    'foo'

The parameter ``key`` can be used to ignore parameters for
caching. In this example we ignore the parameter ``algorithm``::

    sage: @cached_function(key=lambda x,y,algorithm: (x,y))
    ....: def mul(x, y, algorithm='default'):
    ....:     return x*y
    sage: mul(1,1,algorithm='default') is mul(1,1,algorithm='algorithm') is mul(1,1) is mul(1,1,'default')
    True
"""

cached_in_parent_method: CachedInParentMethod


type Method = Callable
def cached_method(f: Method, name=None, key: Callable | None = None, do_pickle: bool=False) -> CachedMethod:
    r"""cached_method(f, name=None, key=None, do_pickle=None)

File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 3051)

A decorator for cached methods.

EXAMPLES:

In the following examples, one can see how a cached method works
in application. Below, we demonstrate what is done behind the scenes::

    sage: class C:
    ....:     @cached_method
    ....:     def __hash__(self):
    ....:         print("compute hash")
    ....:         return int(5)
    ....:     @cached_method
    ....:     def f(self, x):
    ....:         print("computing cached method")
    ....:         return x*2
    sage: c = C()
    sage: type(C.__hash__)
    <class 'sage.misc.cachefunc.CachedMethodCallerNoArgs'>
    sage: hash(c)
    compute hash
    5

When calling a cached method for the second time with the same arguments,
the value is gotten from the cache, so that a new computation is not
needed::

    sage: hash(c)
    5
    sage: c.f(4)
    computing cached method
    8
    sage: c.f(4) is c.f(4)
    True

Different instances have distinct caches::

    sage: d = C()
    sage: d.f(4) is c.f(4)
    computing cached method
    False
    sage: d.f.clear_cache()
    sage: c.f(4)
    8
    sage: d.f(4)
    computing cached method
    8

Using cached methods for the hash and other special methods was
implemented in :issue:`12601`, by means of :class:`CachedSpecialMethod`. We
show that it is used behind the scenes::

    sage: cached_method(c.__hash__)
    <sage.misc.cachefunc.CachedSpecialMethod object at ...>
    sage: cached_method(c.f)
    <sage.misc.cachefunc.CachedMethod object at ...>

The parameter ``do_pickle`` can be used if the contents of the cache should be
stored in a pickle of the cached method. This can be dangerous with special
methods such as ``__hash__``::

    sage: class C:
    ....:     @cached_method(do_pickle=True)
    ....:     def __hash__(self):
    ....:         return id(self)

    sage: import __main__
    sage: __main__.C = C
    sage: c = C()
    sage: hash(c)  # random output
    sage: d = loads(dumps(c))
    sage: hash(d) == hash(c)
    True

However, the contents of a method's cache are not pickled unless ``do_pickle``
is set::

    sage: class C:
    ....:     @cached_method
    ....:     def __hash__(self):
    ....:         return id(self)

    sage: __main__.C = C
    sage: c = C()
    sage: hash(c)  # random output
    sage: d = loads(dumps(c))
    sage: hash(d) == hash(c)
    False"""
    ...

def dict_key(o: Any) -> Hashable:
    r"""dict_key(o)

File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 554)

Return a key to cache object ``o`` in a dict.

This is different from ``cache_key`` since the ``cache_key`` might
get confused with the key of a hashable object. Therefore, such keys
include ``unhashable_key`` which acts as a unique marker which is
certainly not stored in the dictionary otherwise.

EXAMPLES::

    sage: from sage.misc.cachefunc import dict_key
    sage: dict_key(42)
    42
    sage: K.<u> = Qq(9)                                                             # needs sage.rings.padics
    sage: dict_key(u)                                                               # needs sage.rings.padics
    (<object object at ...>, (..., 20))
"""
    ...

weak_cached_function: WeakCachedFunction

class CacheDict(dict):
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class CachedFunction:
    """CachedFunction(f, classmethod=False, *, name=None, key=None, do_pickle=None)

    File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 632)

    Create a cached version of a function, which only recomputes
    values it hasn't already computed. Synonyme: ``cached_function``

    INPUT:

    - ``f`` -- a function
    - ``name`` -- (optional string) name that the cached version
      of ``f`` should be provided with
    - ``key`` -- (optional callable) takes the input and returns a
      key for the cache, typically one would use this to normalize input
    - ``do_pickle`` -- (optional boolean) whether or not the contents of the
      cache should be included when pickling this function; the default is not
      to include them.

    If ``f`` is a function, do either ``g = CachedFunction(f)``
    or ``g = cached_function(f)`` to make a cached version of ``f``,
    or put ``@cached_function`` right before the definition of ``f``
    (i.e., use Python decorators)::

        @cached_function
        def f(...):
            ....

    The inputs to the function must be hashable or they must define
    :meth:`sage.structure.sage_object.SageObject._cache_key`.

    EXAMPLES::

        sage: @cached_function
        ....: def mul(x, y=2):
        ....:     return x*y
        sage: mul(3)
        6

    We demonstrate that the result is cached, and that, moreover,
    the cache takes into account the various ways of providing
    default arguments::

        sage: mul(3) is mul(3,2)
        True
        sage: mul(3,y=2) is mul(3,2)
        True

    The user can clear the cache::

        sage: a = mul(4)
        sage: mul.clear_cache()
        sage: a is mul(4)
        False

    It is also possible to explicitly override the cache with
    a different value::

        sage: mul.set_cache('foo',5)
        sage: mul(5,2)
        'foo'

    The parameter ``key`` can be used to ignore parameters for
    caching. In this example we ignore the parameter ``algorithm``::

        sage: @cached_function(key=lambda x,y,algorithm: (x,y))
        ....: def mul(x, y, algorithm='default'):
        ....:     return x*y
        sage: mul(1,1,algorithm='default') is mul(1,1,algorithm='algorithm') is mul(1,1) is mul(1,1,'default')
        True"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    cache: dict | Any
    f: Callable
    _argument_fixer: ArgumentFixer
    __cached_module__: str
    do_pickle: int
    def __init__(self, f, classmethod=..., name=..., key=..., do_pickle=...):
        '''File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 700)

                Create a cached version of a function, which only recomputes
                values it hasn\'t already computed. A custom name can be
                provided by an optional argument "name".

                If ``f`` is a function, do either ``g = CachedFunction(f)``
                to make a cached version of ``f``, or put ``@CachedFunction``
                right before the definition of ``f`` (i.e., use Python decorators)::

                    @CachedFunction
                    def f(...):
                        ....

                The inputs to the function must be hashable or they must define
                :meth:`sage.structure.sage_object.SageObject._cache_key`.

                TESTS::

                    sage: # needs sage.combinat
                    sage: g = CachedFunction(number_of_partitions)
                    sage: g.__name__
                    \'number_of_partitions\'
                    sage: \'partitions\' in sage.misc.sageinspect.sage_getdoc(g)
                    True
                    sage: g(5)                                                                  # needs sage.libs.flint
                    7
                    sage: g.cache                                                               # needs sage.libs.flint
                    {((5, \'default\'), ()): 7}

                    sage: def f(t=1): print(t)
                    sage: h = CachedFunction(f)
                    sage: w = walltime()
                    sage: h(); h(1); h(t=1)
                    1
                    sage: walltime(w) < 2
                    True

                By default, the contents of the cache are not pickled::

                    sage: @cached_function
                    ....: def f(n): return None
                    sage: import __main__
                    sage: __main__.f = f
                    sage: for i in range(100): f(i)
                    sage: len(f.cache)
                    100

                    sage: s = dumps(f)
                    sage: f.clear_cache()
                    sage: f = loads(s)
                    sage: len(f.cache)
                    0

                If ``do_pickle`` is set, then the cache is pickled::

                    sage: @cached_function(do_pickle=True)
                    ....: def f(n): return None
                    sage: __main__.f = f
                    sage: for i in range(100): f(i)
                    sage: len(f.cache)
                    100

                    sage: s = dumps(f)
                    sage: f.clear_cache()
                    sage: f = loads(s)
                    sage: len(f.cache)
                    100
        '''
    def cached(self, *args, **kwds) -> Any:
        """CachedFunction.cached(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 1028)

        Return the result from the cache if available. If the value is
        not cached, raise :exc:`KeyError`.

        EXAMPLES::

            sage: @cached_function
            ....: def f(x):
            ....:     return x
            sage: f.cached(5)
            Traceback (most recent call last):
            ...
            KeyError: ((5,), ())
            sage: f(5)
            5
            sage: f.cached(5)
            5"""
    @overload
    def clear_cache(self) -> Any:
        """CachedFunction.clear_cache(self)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 1221)

        Clear the cache dictionary.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: g = CachedFunction(number_of_partitions)
            sage: a = g(5)                                                              # needs sage.libs.flint
            sage: g.cache                                                               # needs sage.libs.flint
            {((5, 'default'), ()): 7}
            sage: g.clear_cache()
            sage: g.cache
            {}"""
    @overload
    def clear_cache(self) -> Any:
        """CachedFunction.clear_cache(self)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 1221)

        Clear the cache dictionary.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: g = CachedFunction(number_of_partitions)
            sage: a = g(5)                                                              # needs sage.libs.flint
            sage: g.cache                                                               # needs sage.libs.flint
            {((5, 'default'), ()): 7}
            sage: g.clear_cache()
            sage: g.cache
            {}"""
    @overload
    def get_key(self, *args, **kwds) -> Any:
        """CachedFunction.get_key(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 1153)

        Return the key in the cache to be used when ``args``
        and ``kwds`` are passed in as parameters.

        EXAMPLES::

            sage: @cached_function
            ....: def foo(x):
            ....:     return x^2
            sage: foo(2)
            4
            sage: foo.get_key(2)
            ((2,), ())
            sage: foo.get_key(x=3)
            ((3,), ())

        Examples for cached methods::

            sage: class Foo:
            ....:     def __init__(self, x):
            ....:         self._x = x
            ....:     @cached_method
            ....:     def f(self, y, z=0):
            ....:         return self._x * y + z
            sage: a = Foo(2)
            sage: z = a.f(37)
            sage: k = a.f.get_key(37); k
            ((37, 0), ())
            sage: a.f.cache[k] is z
            True

        Note that the method does not test whether there are
        too many arguments, or wrong argument names::

            sage: a.f.get_key(1,2,3,x=4,y=5,z=6)
            ((1, 2, 3), (('x', 4), ('y', 5), ('z', 6)))

        It does, however, take into account the different
        ways of providing named arguments, possibly with a
        default value::

            sage: a.f.get_key(5)
            ((5, 0), ())
            sage: a.f.get_key(y=5)
            ((5, 0), ())
            sage: a.f.get_key(5,0)
            ((5, 0), ())
            sage: a.f.get_key(5,z=0)
            ((5, 0), ())
            sage: a.f.get_key(y=5,z=0)
            ((5, 0), ())"""
    @overload
    def get_key(self, x=...) -> Any:
        """CachedFunction.get_key(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 1153)

        Return the key in the cache to be used when ``args``
        and ``kwds`` are passed in as parameters.

        EXAMPLES::

            sage: @cached_function
            ....: def foo(x):
            ....:     return x^2
            sage: foo(2)
            4
            sage: foo.get_key(2)
            ((2,), ())
            sage: foo.get_key(x=3)
            ((3,), ())

        Examples for cached methods::

            sage: class Foo:
            ....:     def __init__(self, x):
            ....:         self._x = x
            ....:     @cached_method
            ....:     def f(self, y, z=0):
            ....:         return self._x * y + z
            sage: a = Foo(2)
            sage: z = a.f(37)
            sage: k = a.f.get_key(37); k
            ((37, 0), ())
            sage: a.f.cache[k] is z
            True

        Note that the method does not test whether there are
        too many arguments, or wrong argument names::

            sage: a.f.get_key(1,2,3,x=4,y=5,z=6)
            ((1, 2, 3), (('x', 4), ('y', 5), ('z', 6)))

        It does, however, take into account the different
        ways of providing named arguments, possibly with a
        default value::

            sage: a.f.get_key(5)
            ((5, 0), ())
            sage: a.f.get_key(y=5)
            ((5, 0), ())
            sage: a.f.get_key(5,0)
            ((5, 0), ())
            sage: a.f.get_key(5,z=0)
            ((5, 0), ())
            sage: a.f.get_key(y=5,z=0)
            ((5, 0), ())"""
    @overload
    def get_key(self, y=...) -> Any:
        """CachedFunction.get_key(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 1153)

        Return the key in the cache to be used when ``args``
        and ``kwds`` are passed in as parameters.

        EXAMPLES::

            sage: @cached_function
            ....: def foo(x):
            ....:     return x^2
            sage: foo(2)
            4
            sage: foo.get_key(2)
            ((2,), ())
            sage: foo.get_key(x=3)
            ((3,), ())

        Examples for cached methods::

            sage: class Foo:
            ....:     def __init__(self, x):
            ....:         self._x = x
            ....:     @cached_method
            ....:     def f(self, y, z=0):
            ....:         return self._x * y + z
            sage: a = Foo(2)
            sage: z = a.f(37)
            sage: k = a.f.get_key(37); k
            ((37, 0), ())
            sage: a.f.cache[k] is z
            True

        Note that the method does not test whether there are
        too many arguments, or wrong argument names::

            sage: a.f.get_key(1,2,3,x=4,y=5,z=6)
            ((1, 2, 3), (('x', 4), ('y', 5), ('z', 6)))

        It does, however, take into account the different
        ways of providing named arguments, possibly with a
        default value::

            sage: a.f.get_key(5)
            ((5, 0), ())
            sage: a.f.get_key(y=5)
            ((5, 0), ())
            sage: a.f.get_key(5,0)
            ((5, 0), ())
            sage: a.f.get_key(5,z=0)
            ((5, 0), ())
            sage: a.f.get_key(y=5,z=0)
            ((5, 0), ())"""
    @overload
    def get_key(self, y=..., z=...) -> Any:
        """CachedFunction.get_key(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 1153)

        Return the key in the cache to be used when ``args``
        and ``kwds`` are passed in as parameters.

        EXAMPLES::

            sage: @cached_function
            ....: def foo(x):
            ....:     return x^2
            sage: foo(2)
            4
            sage: foo.get_key(2)
            ((2,), ())
            sage: foo.get_key(x=3)
            ((3,), ())

        Examples for cached methods::

            sage: class Foo:
            ....:     def __init__(self, x):
            ....:         self._x = x
            ....:     @cached_method
            ....:     def f(self, y, z=0):
            ....:         return self._x * y + z
            sage: a = Foo(2)
            sage: z = a.f(37)
            sage: k = a.f.get_key(37); k
            ((37, 0), ())
            sage: a.f.cache[k] is z
            True

        Note that the method does not test whether there are
        too many arguments, or wrong argument names::

            sage: a.f.get_key(1,2,3,x=4,y=5,z=6)
            ((1, 2, 3), (('x', 4), ('y', 5), ('z', 6)))

        It does, however, take into account the different
        ways of providing named arguments, possibly with a
        default value::

            sage: a.f.get_key(5)
            ((5, 0), ())
            sage: a.f.get_key(y=5)
            ((5, 0), ())
            sage: a.f.get_key(5,0)
            ((5, 0), ())
            sage: a.f.get_key(5,z=0)
            ((5, 0), ())
            sage: a.f.get_key(y=5,z=0)
            ((5, 0), ())"""
    @overload
    def is_in_cache(self, *args, **kwds) -> Any:
        """CachedFunction.is_in_cache(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 1055)

        Check if the argument list is in the cache.

        EXAMPLES::

            sage: class Foo:
            ....:     def __init__(self, x):
            ....:         self._x = x
            ....:     @cached_method
            ....:     def f(self, z, y=0):
            ....:         return self._x*z+y
            sage: a = Foo(2)
            sage: a.f.is_in_cache(3)
            False
            sage: a.f(3)
            6
            sage: a.f.is_in_cache(3,y=0)
            True

        TESTS:

        Check that :issue:`16316` has been fixed, i.e., caching works for
        immutable unhashable objects which define
        :meth:`sage.structure.sage_object.SageObject._cache_key`::

            sage: # needs sage.rings.padics
            sage: @cached_function
            ....: def f(x): return x
            sage: K.<u> = Qq(4)
            sage: x = K(1,1); x
            1 + O(2)
            sage: f.is_in_cache(x)
            False
            sage: f(x)
            1 + O(2)
            sage: f.is_in_cache(x)
            True"""
    @overload
    def is_in_cache(self, x) -> Any:
        """CachedFunction.is_in_cache(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 1055)

        Check if the argument list is in the cache.

        EXAMPLES::

            sage: class Foo:
            ....:     def __init__(self, x):
            ....:         self._x = x
            ....:     @cached_method
            ....:     def f(self, z, y=0):
            ....:         return self._x*z+y
            sage: a = Foo(2)
            sage: a.f.is_in_cache(3)
            False
            sage: a.f(3)
            6
            sage: a.f.is_in_cache(3,y=0)
            True

        TESTS:

        Check that :issue:`16316` has been fixed, i.e., caching works for
        immutable unhashable objects which define
        :meth:`sage.structure.sage_object.SageObject._cache_key`::

            sage: # needs sage.rings.padics
            sage: @cached_function
            ....: def f(x): return x
            sage: K.<u> = Qq(4)
            sage: x = K(1,1); x
            1 + O(2)
            sage: f.is_in_cache(x)
            False
            sage: f(x)
            1 + O(2)
            sage: f.is_in_cache(x)
            True"""
    @overload
    def is_in_cache(self, x) -> Any:
        """CachedFunction.is_in_cache(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 1055)

        Check if the argument list is in the cache.

        EXAMPLES::

            sage: class Foo:
            ....:     def __init__(self, x):
            ....:         self._x = x
            ....:     @cached_method
            ....:     def f(self, z, y=0):
            ....:         return self._x*z+y
            sage: a = Foo(2)
            sage: a.f.is_in_cache(3)
            False
            sage: a.f(3)
            6
            sage: a.f.is_in_cache(3,y=0)
            True

        TESTS:

        Check that :issue:`16316` has been fixed, i.e., caching works for
        immutable unhashable objects which define
        :meth:`sage.structure.sage_object.SageObject._cache_key`::

            sage: # needs sage.rings.padics
            sage: @cached_function
            ....: def f(x): return x
            sage: K.<u> = Qq(4)
            sage: x = K(1,1); x
            1 + O(2)
            sage: f.is_in_cache(x)
            False
            sage: f(x)
            1 + O(2)
            sage: f.is_in_cache(x)
            True"""
    def precompute(self, arglist, num_processes=...) -> Any:
        """CachedFunction.precompute(self, arglist, num_processes=1)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 1238)

        Cache values for a number of inputs.  Do the computation
        in parallel, and only bother to compute values that we
        haven't already cached.

        INPUT:

        - ``arglist`` -- list (or iterables) of arguments for which
          the method shall be precomputed

        - ``num_processes`` -- number of processes used by
          :func:`~sage.parallel.decorate.parallel`

        EXAMPLES::

            sage: @cached_function
            ....: def oddprime_factors(n):
            ....:     l = [p for p,e in factor(n) if p != 2]
            ....:     return len(l)
            sage: oddprime_factors.precompute(range(1,100), 4)
            sage: oddprime_factors.cache[(25,),()]
            1"""
    def set_cache(self, value, *args, **kwds) -> Any:
        """CachedFunction.set_cache(self, value, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 1101)

        Set the value for those args and keyword args
        Mind the unintuitive syntax (value first).
        Any idea on how to improve that welcome!

        EXAMPLES::

            sage: # needs sage.combinat sage.libs.flint
            sage: g = CachedFunction(number_of_partitions)
            sage: a = g(5)
            sage: g.cache
            {((5, 'default'), ()): 7}
            sage: g.set_cache(17, 5)
            sage: g.cache
            {((5, 'default'), ()): 17}
            sage: g(5)
            17

        TESTS:

        Check that :issue:`16316` has been fixed, i.e., caching works for
        immutable unhashable objects which define
        :meth:`sage.structure.sage_object.SageObject._cache_key`::

            sage: # needs sage.rings.padics
            sage: @cached_function
            ....: def f(x): return x
            sage: K.<u> = Qq(4)
            sage: x = K(1,1); x
            1 + O(2)
            sage: f.set_cache(x, x)
            sage: f.is_in_cache(x)
            True

        DEVELOPER NOTE:

        Is there a way to use the following intuitive syntax?

        ::

            sage: g(5) = 19    # todo: not implemented
            sage: g(5)         # todo: not implemented
            19"""
    def __call__(self, *args, **kwds) -> Any:
        """CachedFunction.__call__(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 976)

        Return value from cache or call the wrapped function,
        caching the output.

        TESTS::

            sage: # needs sage.combinat sage.libs.flint
            sage: g = CachedFunction(number_of_partitions)
            sage: a = g(5)
            sage: g.cache
            {((5, 'default'), ()): 7}
            sage: a = g(10^5)   # indirect doctest
            sage: a == number_of_partitions(10^5)
            True
            sage: a is g(10^5)
            True
            sage: a is number_of_partitions(10^5)
            True

        Check that :issue:`16316` has been fixed, i.e., caching works for
        immutable unhashable objects which define
        :meth:`sage.structure.sage_object.SageObject._cache_key`::

            sage: # needs sage.rings.padics
            sage: @cached_function
            ....: def f(x): return x+x
            sage: K.<u> = Qq(4)
            sage: x = K(1,1); x
            1 + O(2)
            sage: y = K(1,2); y
            1 + O(2^2)
            sage: x == y
            True
            sage: f(x) is f(x)
            True
            sage: f(y) is not f(x)
            True"""
    def __reduce__(self) -> Any:
        """CachedFunction.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 854)

        Pickling of cached functions.

        TESTS::

            sage: type(hilbert_class_polynomial)                                        # needs sage.schemes
            <class 'sage.misc.cachefunc.CachedFunction'>
            sage: loads(dumps(hilbert_class_polynomial)) is hilbert_class_polynomial  #indirect doctest                 # needs sage.schemes
            True"""

class CachedInParentMethod(CachedMethod):
    """CachedInParentMethod(f, name=None, key=None, do_pickle=None)

    File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 3149)

    A decorator that creates a cached version of an instance
    method of a class.

    In contrast to :class:`CachedMethod`,
    the cache dictionary is an attribute of the parent of
    the instance to which the method belongs.

    ASSUMPTION:

    This way of caching works only if

    - the instances *have* a parent, and
    - the instances are hashable (they are part of the cache key) or they
      define :meth:`sage.structure.sage_object.SageObject._cache_key`

    NOTE:

    For proper behavior, the method must be a pure function (no side effects).
    If this decorator is used on a method, it will have identical output on
    equal elements. This is since the element is part of the hash key.
    Arguments to the method must be hashable or define
    :meth:`sage.structure.sage_object.SageObject._cache_key`.  The instance it
    is assigned to must be hashable.

    Examples can be found at :mod:`~sage.misc.cachefunc`."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @overload
    def __init__(self, x) -> Any:
        """File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 3178)

                Construct a new method with cache stored in the parent of the instance.

                See also ``cached_method`` and ``cached_function``.

                EXAMPLES::

                    sage: class MyParent(Parent):
                    ....:     pass
                    sage: class Foo:                         # indirect doctest
                    ....:     def __init__(self, x):
                    ....:         self._x = x
                    ....:         self._parent = MyParent()
                    ....:     def parent(self):
                    ....:         return self._parent
                    ....:     @cached_in_parent_method
                    ....:     def f(self):
                    ....:         return self._x^2
                    sage: a = Foo(2)
                    sage: a.f()
                    4
                    sage: b = Foo(3)
                    sage: b.f()
                    9
                    sage: hasattr(a.parent(), '_cache__element_f')
                    True

                For speeding up internal computations, this dictionary
                is also accessible as an attribute of the CachedMethodCaller
                (by :issue:`8611`)::

                    sage: a.parent()._cache__element_f is a.f.cache
                    True

                TESTS:

                Test that ``key`` works::

                    sage: class A():
                    ....:     def __init__(self):
                    ....:         self._parent = MyParent()
                    ....:     def parent(self): return self._parent
                    ....:     def _f_normalize(self, x, algorithm): return x
                    ....:     @cached_in_parent_method(key=_f_normalize)
                    ....:     def f(self, x, algorithm='default'): return x
                    sage: a = A()
                    sage: a.f(1, algorithm='default') is a.f(1) is a.f(1, algorithm='algorithm')
                    True

                Test that ``do_pickle`` works. Usually the contents of the cache are not
                pickled::

                    sage: class A():
                    ....:     def __init__(self):
                    ....:         self._parent = MyParent()
                    ....:     def parent(self): return self._parent
                    ....:     @cached_in_parent_method
                    ....:     def f(self, x): return x
                    sage: import __main__
                    sage: __main__.A = A
                    sage: __main__.MyParent = MyParent
                    sage: a = A()
                    sage: a.f(1)
                    1
                    sage: len(a.f.cache)
                    1
                    sage: b = loads(dumps(a))
                    sage: len(b.f.cache)
                    0

                Pickling can be enabled with ``do_pickle``::

                    sage: class A():
                    ....:     def __init__(self):
                    ....:         self._parent = MyParent()
                    ....:     def parent(self): return self._parent
                    ....:     @cached_in_parent_method(do_pickle=True)
                    ....:     def f(self, x): return x
                    sage: __main__.A = A
                    sage: a = A()
                    sage: a.f(1)
                    1
                    sage: len(a.f.cache)
                    1
                    sage: b = loads(dumps(a))
                    sage: len(b.f.cache)
                    1
        """
    @overload
    def __init__(self) -> Any:
        """File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 3178)

                Construct a new method with cache stored in the parent of the instance.

                See also ``cached_method`` and ``cached_function``.

                EXAMPLES::

                    sage: class MyParent(Parent):
                    ....:     pass
                    sage: class Foo:                         # indirect doctest
                    ....:     def __init__(self, x):
                    ....:         self._x = x
                    ....:         self._parent = MyParent()
                    ....:     def parent(self):
                    ....:         return self._parent
                    ....:     @cached_in_parent_method
                    ....:     def f(self):
                    ....:         return self._x^2
                    sage: a = Foo(2)
                    sage: a.f()
                    4
                    sage: b = Foo(3)
                    sage: b.f()
                    9
                    sage: hasattr(a.parent(), '_cache__element_f')
                    True

                For speeding up internal computations, this dictionary
                is also accessible as an attribute of the CachedMethodCaller
                (by :issue:`8611`)::

                    sage: a.parent()._cache__element_f is a.f.cache
                    True

                TESTS:

                Test that ``key`` works::

                    sage: class A():
                    ....:     def __init__(self):
                    ....:         self._parent = MyParent()
                    ....:     def parent(self): return self._parent
                    ....:     def _f_normalize(self, x, algorithm): return x
                    ....:     @cached_in_parent_method(key=_f_normalize)
                    ....:     def f(self, x, algorithm='default'): return x
                    sage: a = A()
                    sage: a.f(1, algorithm='default') is a.f(1) is a.f(1, algorithm='algorithm')
                    True

                Test that ``do_pickle`` works. Usually the contents of the cache are not
                pickled::

                    sage: class A():
                    ....:     def __init__(self):
                    ....:         self._parent = MyParent()
                    ....:     def parent(self): return self._parent
                    ....:     @cached_in_parent_method
                    ....:     def f(self, x): return x
                    sage: import __main__
                    sage: __main__.A = A
                    sage: __main__.MyParent = MyParent
                    sage: a = A()
                    sage: a.f(1)
                    1
                    sage: len(a.f.cache)
                    1
                    sage: b = loads(dumps(a))
                    sage: len(b.f.cache)
                    0

                Pickling can be enabled with ``do_pickle``::

                    sage: class A():
                    ....:     def __init__(self):
                    ....:         self._parent = MyParent()
                    ....:     def parent(self): return self._parent
                    ....:     @cached_in_parent_method(do_pickle=True)
                    ....:     def f(self, x): return x
                    sage: __main__.A = A
                    sage: a = A()
                    sage: a.f(1)
                    1
                    sage: len(a.f.cache)
                    1
                    sage: b = loads(dumps(a))
                    sage: len(b.f.cache)
                    1
        """
    @overload
    def __init__(self) -> Any:
        """File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 3178)

                Construct a new method with cache stored in the parent of the instance.

                See also ``cached_method`` and ``cached_function``.

                EXAMPLES::

                    sage: class MyParent(Parent):
                    ....:     pass
                    sage: class Foo:                         # indirect doctest
                    ....:     def __init__(self, x):
                    ....:         self._x = x
                    ....:         self._parent = MyParent()
                    ....:     def parent(self):
                    ....:         return self._parent
                    ....:     @cached_in_parent_method
                    ....:     def f(self):
                    ....:         return self._x^2
                    sage: a = Foo(2)
                    sage: a.f()
                    4
                    sage: b = Foo(3)
                    sage: b.f()
                    9
                    sage: hasattr(a.parent(), '_cache__element_f')
                    True

                For speeding up internal computations, this dictionary
                is also accessible as an attribute of the CachedMethodCaller
                (by :issue:`8611`)::

                    sage: a.parent()._cache__element_f is a.f.cache
                    True

                TESTS:

                Test that ``key`` works::

                    sage: class A():
                    ....:     def __init__(self):
                    ....:         self._parent = MyParent()
                    ....:     def parent(self): return self._parent
                    ....:     def _f_normalize(self, x, algorithm): return x
                    ....:     @cached_in_parent_method(key=_f_normalize)
                    ....:     def f(self, x, algorithm='default'): return x
                    sage: a = A()
                    sage: a.f(1, algorithm='default') is a.f(1) is a.f(1, algorithm='algorithm')
                    True

                Test that ``do_pickle`` works. Usually the contents of the cache are not
                pickled::

                    sage: class A():
                    ....:     def __init__(self):
                    ....:         self._parent = MyParent()
                    ....:     def parent(self): return self._parent
                    ....:     @cached_in_parent_method
                    ....:     def f(self, x): return x
                    sage: import __main__
                    sage: __main__.A = A
                    sage: __main__.MyParent = MyParent
                    sage: a = A()
                    sage: a.f(1)
                    1
                    sage: len(a.f.cache)
                    1
                    sage: b = loads(dumps(a))
                    sage: len(b.f.cache)
                    0

                Pickling can be enabled with ``do_pickle``::

                    sage: class A():
                    ....:     def __init__(self):
                    ....:         self._parent = MyParent()
                    ....:     def parent(self): return self._parent
                    ....:     @cached_in_parent_method(do_pickle=True)
                    ....:     def f(self, x): return x
                    sage: __main__.A = A
                    sage: a = A()
                    sage: a.f(1)
                    1
                    sage: len(a.f.cache)
                    1
                    sage: b = loads(dumps(a))
                    sage: len(b.f.cache)
                    1
        """
    @overload
    def __init__(self) -> Any:
        """File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 3178)

                Construct a new method with cache stored in the parent of the instance.

                See also ``cached_method`` and ``cached_function``.

                EXAMPLES::

                    sage: class MyParent(Parent):
                    ....:     pass
                    sage: class Foo:                         # indirect doctest
                    ....:     def __init__(self, x):
                    ....:         self._x = x
                    ....:         self._parent = MyParent()
                    ....:     def parent(self):
                    ....:         return self._parent
                    ....:     @cached_in_parent_method
                    ....:     def f(self):
                    ....:         return self._x^2
                    sage: a = Foo(2)
                    sage: a.f()
                    4
                    sage: b = Foo(3)
                    sage: b.f()
                    9
                    sage: hasattr(a.parent(), '_cache__element_f')
                    True

                For speeding up internal computations, this dictionary
                is also accessible as an attribute of the CachedMethodCaller
                (by :issue:`8611`)::

                    sage: a.parent()._cache__element_f is a.f.cache
                    True

                TESTS:

                Test that ``key`` works::

                    sage: class A():
                    ....:     def __init__(self):
                    ....:         self._parent = MyParent()
                    ....:     def parent(self): return self._parent
                    ....:     def _f_normalize(self, x, algorithm): return x
                    ....:     @cached_in_parent_method(key=_f_normalize)
                    ....:     def f(self, x, algorithm='default'): return x
                    sage: a = A()
                    sage: a.f(1, algorithm='default') is a.f(1) is a.f(1, algorithm='algorithm')
                    True

                Test that ``do_pickle`` works. Usually the contents of the cache are not
                pickled::

                    sage: class A():
                    ....:     def __init__(self):
                    ....:         self._parent = MyParent()
                    ....:     def parent(self): return self._parent
                    ....:     @cached_in_parent_method
                    ....:     def f(self, x): return x
                    sage: import __main__
                    sage: __main__.A = A
                    sage: __main__.MyParent = MyParent
                    sage: a = A()
                    sage: a.f(1)
                    1
                    sage: len(a.f.cache)
                    1
                    sage: b = loads(dumps(a))
                    sage: len(b.f.cache)
                    0

                Pickling can be enabled with ``do_pickle``::

                    sage: class A():
                    ....:     def __init__(self):
                    ....:         self._parent = MyParent()
                    ....:     def parent(self): return self._parent
                    ....:     @cached_in_parent_method(do_pickle=True)
                    ....:     def f(self, x): return x
                    sage: __main__.A = A
                    sage: a = A()
                    sage: a.f(1)
                    1
                    sage: len(a.f.cache)
                    1
                    sage: b = loads(dumps(a))
                    sage: len(b.f.cache)
                    1
        """
    def __get__(self, inst, cls) -> Any:
        """CachedInParentMethod.__get__(self, inst, cls)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 3344)

        Get a CachedMethodCaller bound to this specific instance of
        the class of the cached-in-parent method."""

class CachedMethod:
    '''CachedMethod(f, name=None, key=None, do_pickle=None)

    File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 2535)

    A decorator that creates a cached version of an instance
    method of a class.

    .. NOTE::

        For proper behavior, the method must be a pure function (no side
        effects). Arguments to the method must be hashable or transformed into
        something hashable using ``key`` or they must define
        :meth:`sage.structure.sage_object.SageObject._cache_key`.

    EXAMPLES::

        sage: class Foo():
        ....:     @cached_method
        ....:     def f(self, t, x=2):
        ....:         print(\'computing\')
        ....:         return t**x
        sage: a = Foo()

    The example shows that the actual computation
    takes place only once, and that the result is
    identical for equivalent input::

        sage: res = a.f(3, 2); res
        computing
        9
        sage: a.f(t = 3, x = 2) is res
        True
        sage: a.f(3) is res
        True

    Note, however, that accessing the attribute directly will call :meth:`__get__`,
    and returns a :class:`CachedMethodCaller` or :class:`CachedMethodCallerNoArgs`.

    ::

        sage: P.<a,b,c,d> = QQ[]
        sage: I = P*[a,b]
        sage: type(I.__class__.gens)
        <class \'sage.misc.cachefunc.CachedMethodCallerNoArgs\'>
        sage: type(I.__class__.__dict__["gens"])
        <class \'sage.misc.cachefunc.CachedMethod\'>

    The parameter ``key`` can be used to pass a function which creates a
    custom cache key for inputs. In the following example, this parameter is
    used to ignore the ``algorithm`` keyword for caching::

        sage: class A():
        ....:     def _f_normalize(self, x, algorithm): return x
        ....:     @cached_method(key=_f_normalize)
        ....:     def f(self, x, algorithm=\'default\'): return x
        sage: a = A()
        sage: a.f(1, algorithm=\'default\') is a.f(1) is a.f(1, algorithm=\'algorithm\')
        True

    The parameter ``do_pickle`` can be used to enable pickling of the cache.
    Usually the cache is not stored when pickling::

        sage: class A():
        ....:     @cached_method
        ....:     def f(self, x): return None
        sage: import __main__
        sage: __main__.A = A
        sage: a = A()
        sage: a.f(1)
        sage: len(a.f.cache)
        1
        sage: b = loads(dumps(a))
        sage: len(b.f.cache)
        0

    When ``do_pickle`` is set, the pickle contains the contents of the cache::

        sage: class A():
        ....:     @cached_method(do_pickle=True)
        ....:     def f(self, x): return None
        sage: __main__.A = A
        sage: a = A()
        sage: a.f(1)
        sage: len(a.f.cache)
        1
        sage: b = loads(dumps(a))
        sage: len(b.f.cache)
        1

    Cached methods cannot be copied like usual methods, see :issue:`12603`.
    Copying them can lead to very surprising results::

        sage: class A:
        ....:     @cached_method
        ....:     def f(self):
        ....:         return 1
        sage: class B:
        ....:     g=A.f
        ....:     def f(self):
        ....:         return 2

        sage: b=B()
        sage: b.f()
        2
        sage: b.g()
        1
        sage: b.f()
        1'''
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    __cached_module__: str
    def __init__(self, x):
        '''File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 2642)

                EXAMPLES::

                    sage: class Foo():
                    ....:     def __init__(self, x):
                    ....:         self._x = x
                    ....:     @cached_method
                    ....:     def f(self, n):
                    ....:         return self._x^n
                    ....:     @cached_method
                    ....:     def f0(self):
                    ....:         return self._x^2
                    sage: a = Foo(2)
                    sage: a.f(2)
                    4
                    sage: a.f0()
                    4

                For methods with parameters, the results of method ``f`` is attempted
                to be stored in a dictionary attribute of the instance ``a``::

                    sage: hasattr(a, \'_cache__f\')
                    True
                    sage: a._cache__f
                    {((2,), ()): 4}
                    sage: a._cache_f0
                    Traceback (most recent call last):
                    ...
                    AttributeError: \'Foo\' object has no attribute \'_cache_f0\'...

                As a shortcut, useful to speed up internal computations,
                the same dictionary is also available as an attribute
                of the ``CachedMethodCaller``::

                    sage: type(a.f)
                    <class \'sage.misc.cachefunc.CachedMethodCaller\'>
                    sage: a.f.cache is a._cache__f
                    True

                Note that if the instance ``a`` would not accept attribute
                assignment, the computations would still be cached in
                ``a.f.cache``, and they would in fact be preserved when
                pickling.

                The cached method ``f0`` accepts no arguments, which allows
                for an improved way of caching: By an attribute of the cached
                method itself. This cache is *only* available in that way, i.e.,
                it is not additionally stored as an attribute of ``a``::

                    sage: type(a.f0)
                    <class \'sage.misc.cachefunc.CachedMethodCallerNoArgs\'>
                    sage: a.f0.cache
                    4
                    sage: sorted(n for n in dir(a) if not n.startswith(\'__\'))
                    [\'_cache__f\', \'_x\', \'f\', \'f0\']

                The cached method has its name and module set::

                    sage: f = Foo.__dict__["f"]
                    sage: f.__name__
                    \'f\'
                    sage: f.__module__
                    \'__main__\'
        '''
    def __call__(self, inst, *args, **kwds) -> Any:
        """CachedMethod.__call__(self, inst, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 2716)

        Call the cached method as a function on an instance.
        This code path is not used directly except in a few rare cases,
        see examples for details.

        INPUT:

        - ``inst`` -- an instance on which the method is to be called
        - further positional or named arguments

        EXAMPLES::


            sage: from sage.misc.superseded import deprecated_function_alias
            sage: class Foo():
            ....:     def __init__(self, x):
            ....:         self._x = x
            ....:     @cached_method
            ....:     def f(self, n=2):
            ....:         return self._x^n
            ....:     g = deprecated_function_alias(57, f)
            sage: a = Foo(2)
            sage: Foo.__dict__['f'](a)
            4

        This uses the cache as usual::

            sage: Foo.__dict__['f'](a) is a.f()
            True

        This feature makes cached methods compatible with
        :meth:`sage.misc.superseded.deprecated_function_alias`::

            sage: a.g() is a.f()
            doctest:...: DeprecationWarning: g is deprecated. Please use f instead.
            See https://github.com/sagemath/sage/issues/57 for details.
            True
            sage: Foo.g(a) is a.f()
            True"""
    def __get__(self, inst, cls) -> Any:
        """CachedMethod.__get__(self, inst, cls)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 2821)

        Get a CachedMethodCaller bound to this specific instance of
        the class of the cached method.

        TESTS::

            sage: class Foo:
            ....:     @cached_method
            ....:     def f(self):
            ....:         return 1
            ....:     @cached_method
            ....:     def g(self, x, n=3):
            ....:         return x^n
            sage: a = Foo()
            sage: type(a.f)
            <class 'sage.misc.cachefunc.CachedMethodCallerNoArgs'>
            sage: type(a.g)
            <class 'sage.misc.cachefunc.CachedMethodCaller'>

        By :issue:`8611`, it is attempted to set the
        CachedMethodCaller as an attribute of the instance ``a``,
        replacing the original cached attribute. Therefore, the
        ``__get__`` method will be used only once, which saves much
        time. Hence, we have::

            sage: a.f is a.f
            True
            sage: a.g is a.g
            True

        Verify that :issue:`16337` has been resolved::

            sage: class Foo:
            ....:     @cached_method(key=lambda self, x:x+1)
            ....:     def f(self, x=0):
            ....:         return x

            sage: a = Foo()
            sage: a.f(0)
            0
            sage: a.f.cache
            {1: 0}"""

class CachedMethodCaller(CachedFunction):
    """CachedMethodCaller(CachedMethod cachedmethod, inst, cache=None, *, name=None, key=None, do_pickle=None)

    File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 1697)

    Utility class that is used by :class:`CachedMethod` to bind a
    cached method to an instance.

    .. NOTE::

        Since :issue:`11115`, there is a special implementation
        :class:`CachedMethodCallerNoArgs` for methods that do not take
        arguments.

    EXAMPLES::

        sage: class A:
        ....:    @cached_method
        ....:    def bar(self, x):
        ....:        return x^2
        sage: a = A()
        sage: a.bar
        Cached version of <function ...bar at 0x...>
        sage: type(a.bar)
        <class 'sage.misc.cachefunc.CachedMethodCaller'>
        sage: a.bar(2) is a.bar(x=2)
        True

    TESTS:

    As of :issue:`15692` the contents of the cache are not pickled anymore::

        sage: import __main__
        sage: __main__.A = A
        sage: len(a.bar.cache)
        1
        sage: b = loads(dumps(a))
        sage: len(b.bar.cache)
        0

    The parameter ``do_pickle`` can be used to change this behaviour::

        sage: class A:
        ....:    @cached_method(do_pickle=True)
        ....:    def bar(self, x):
        ....:        return x^2

        sage: __main__.A = A
        sage: a = A()
        sage: a.bar(2)
        4
        sage: len(a.bar.cache)
        1
        sage: b = loads(dumps(a))
        sage: len(b.bar.cache)
        1"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, x) -> Any:
        """File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 1751)

                EXAMPLES::

                    sage: class Foo:
                    ....:     def __init__(self, x):
                    ....:         self._x = x
                    ....:     @cached_method
                    ....:     def f(self, *args):
                    ....:         return self._x^2
                    sage: a = Foo(2)
                    sage: a.f.cache
                    {}
                    sage: a.f()
                    4
                    sage: a.f.cache
                    {((), ()): 4}
        """
    def cached(self, *args, **kwds) -> Any:
        """CachedMethodCaller.cached(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 1979)

        Return the result from the cache if available. If the value is
        not cached, raise :exc:`KeyError`.

        EXAMPLES::

            sage: class CachedMethodTest():
            ....:     @cached_method
            ....:     def f(self, x):
            ....:         return x
            sage: o = CachedMethodTest()
            sage: CachedMethodTest.f.cached(o, 5)
            Traceback (most recent call last):
            ...
            KeyError: ((5,), ())
            sage: o.f.cached(5)
            Traceback (most recent call last):
            ...
            KeyError: ((5,), ())
            sage: o.f(5)
            5
            sage: CachedMethodTest.f.cached(o, 5)
            5
            sage: o.f.cached(5)
            5"""
    def precompute(self, arglist, num_processes=...) -> Any:
        """CachedMethodCaller.precompute(self, arglist, num_processes=1)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 2124)

        Cache values for a number of inputs.  Do the computation
        in parallel, and only bother to compute values that we
        haven't already cached.

        INPUT:

        - ``arglist`` -- list (or iterables) of arguments for which
          the method shall be precomputed

        - ``num_processes`` -- number of processes used by
          :func:`~sage.parallel.decorate.parallel`

        EXAMPLES::

            sage: class Foo():
            ....:     @cached_method
            ....:     def f(self, i):
            ....:         return i^2
            sage: foo = Foo()
            sage: foo.f(3)
            9
            sage: foo.f(1)
            1
            sage: foo.f.precompute(range(2), 2)
            sage: foo.f.cache == {((0,), ()): 0, ((1,), ()): 1, ((3,), ()): 9}
            True"""
    def __call__(self, *args, **kwds) -> Any:
        """CachedMethodCaller.__call__(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 1876)

        Call the cached method.

        TESTS::

            sage: from sage.misc.superseded import deprecated_function_alias
            sage: class Foo:
            ....:     @cached_method
            ....:     def f(self, x, y=1):
            ....:         return x+y
            ....:     g = deprecated_function_alias(57, f)
            sage: a = Foo()
            sage: a.f(1)  #indirect doctest
            2

        The result is cached, taking into account
        the three ways of providing (named) arguments::

            sage: a.f(5) is a.f(5,1)
            True
            sage: a.f(5) is a.f(5,y=1)
            True
            sage: a.f(5) is a.f(y=1,x=5)
            True

        The method can be called as an unbound function using the same cache::

            sage: a.f(5) is Foo.f(a, 5)
            True
            sage: a.f(5) is Foo.f(a,5,1)
            True
            sage: a.f(5) is Foo.f(a, 5,y=1)
            True
            sage: a.f(5) is Foo.f(a, y=1,x=5)
            True

        Cached methods are compatible with
        :meth:`sage.misc.superseded.deprecated_function_alias`::

            sage: a.g(5) is a.f(5)
            doctest:...: DeprecationWarning: g is deprecated. Please use f instead.
            See https://github.com/sagemath/sage/issues/57 for details.
            True
            sage: Foo.g(a, 5) is a.f(5)
            True
            sage: Foo.g(a, y=1,x=5) is a.f(5)
            True

        We test that :issue:`5843` is fixed::

            sage: class Foo:
            ....:     def __init__(self, x):
            ....:         self._x = x
            ....:     @cached_method
            ....:     def f(self, y):
            ....:         return self._x
            sage: a = Foo(2)
            sage: b = Foo(3)
            sage: a.f(b.f)
            2

        Check that :issue:`16316` has been fixed, i.e., caching works for
        immutable unhashable objects which define
        :meth:`sage.structure.sage_object.SageObject._cache_key`::

            sage: # needs sage.rings.padics
            sage: K.<u> = Qq(4)
            sage: class A():
            ....:   @cached_method
            ....:   def f(self, x): return x+x
            sage: a = A()
            sage: x = K(1,1); x
            1 + O(2)
            sage: y = K(1,2); y
            1 + O(2^2)
            sage: x == y
            True
            sage: a.f(x) is a.f(x)
            True
            sage: a.f(y) is not a.f(x)
            True"""
    def __get__(self, inst, cls) -> Any:
        """CachedMethodCaller.__get__(self, inst, cls)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 2020)

        Get a :class:`CachedMethodCaller` bound to a specific
        instance of the class of the cached method.

        NOTE:

        :class:`CachedMethodCaller` has a separate ``__get__``
        since the categories framework creates and caches the
        return value of ``CachedMethod.__get__`` with
        ``inst==None``.

        This getter attempts to assign a bound method as an
        attribute to the given instance. If this is not
        possible (for example, for some extension classes),
        it is attempted to find an attribute ``_cached_methods``,
        and store/retrieve the bound method there. In that
        way, cached methods can be implemented for extension
        classes deriving from :class:`~sage.structure.parent.Parent`
        and :class:`~sage.structure.element.Element`.

        TESTS:

        Due to the separate ``__get__`` method, it is possible
        to define a cached method in one class and use it as
        an attribute of another class. ::

            sage: class Foo:
            ....:     @cached_method
            ....:     def f(self, y):
            ....:         return y - 1
            sage: class Bar:
            ....:     f = Foo.f
            sage: b1 = Bar()
            sage: b2 = Bar()

        The :class:`CachedMethod` is replaced by an instance
        of :class:`CachedMethodCaller` that (by :issue:`8611`)
        is set as an attribute. Hence, we have::

            sage: b1.f is b1.f
            True

        Any instance of ``Bar`` gets its own instance of
        :class:`CachedMethodCaller`::

            sage: b1.f is b2.f
            False

        The method caller knows the instance that it belongs
        to::

            sage: Foo.f._instance is None
            True
            sage: b1.f._instance is b1
            True
            sage: b2.f._instance is b2
            True

        An extension class can inherit a cached method from the
        parent or element class of a category (:issue:`11115`).
        See :class:`CachedMethodCaller` for examples.

        Verify that :issue:`16337` has been resolved::

            sage: class Foo:
            ....:     @cached_method(key=lambda self,y: y+1)
            ....:     def f(self, y):
            ....:         return y - 1
            sage: class Bar:
            ....:     f = Foo.f

            sage: b = Bar()
            sage: b.f(0)
            -1
            sage: b.f.cache
            {1: -1}"""
    def __reduce__(self) -> Any:
        '''CachedMethodCaller.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 1787)

        The pickle of a :class:`CachedMethodCaller` unpickles
        to a :class:`CachedMethodPickle`, that is able to replace
        itself by a copy of the original :class:`CachedMethodCaller`.

        TESTS::

            sage: R.<x, y, z> = PolynomialRing(QQ, 3)
            sage: I = R * (x^3 + y^3 + z^3, x^4 - y^4)
            sage: G = I.groebner_basis()                                                # needs sage.libs.singular
            sage: J = loads(dumps(I))  # indirect doctest
            sage: J.groebner_basis
            Pickle of the cached method "groebner_basis"
            sage: J.groebner_basis.is_in_cache()                                        # needs sage.libs.singular
            True
            sage: J.groebner_basis
            Cached version of <function ...groebner_basis at 0x...>'''

class CachedMethodCallerNoArgs(CachedFunction):
    """CachedMethodCallerNoArgs(inst, f, cache=None, name=None, do_pickle=None)

    File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 2164)

    Utility class that is used by :class:`CachedMethod` to bind a
    cached method to an instance, in the case of a method that does
    not accept any arguments except ``self``.

    .. NOTE::

        The return value ``None`` would not be cached. So, if you have
        a method that does not accept arguments and may return ``None``
        after a lengthy computation, then ``@cached_method`` should not
        be used.

    EXAMPLES::

        sage: P.<a,b,c,d> = QQ[]
        sage: I = P*[a,b]
        sage: I.gens
        Cached version of <function ...gens at 0x...>
        sage: type(I.gens)
        <class 'sage.misc.cachefunc.CachedMethodCallerNoArgs'>
        sage: I.gens is I.gens
        True
        sage: I.gens() is I.gens()
        True

    TESTS:

    As of :issue:`15692` the contents of the cache are not pickled anymore::

        sage: class A:
        ....:    @cached_method
        ....:    def bar(self):
        ....:        return 4
        sage: import __main__
        sage: __main__.A = A
        sage: a = A()
        sage: a.bar()
        4
        sage: a.bar.cache
        4
        sage: b = loads(dumps(a))
        sage: b.bar.cache

    The parameter ``do_pickle`` can be used to change this behaviour::

        sage: class A:
        ....:    @cached_method(do_pickle=True)
        ....:    def bar(self):
        ....:        return 4

        sage: __main__.A = A
        sage: a = A()
        sage: a.bar()
        4
        sage: a.bar.cache
        4
        sage: b = loads(dumps(a))
        sage: b.bar.cache
        4

    AUTHOR:

    - Simon King (2011-04)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, x) -> Any:
        """File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 2229)

                EXAMPLES::

                    sage: class Foo:
                    ....:     def __init__(self, x):
                    ....:         self._x = x
                    ....:     @cached_method
                    ....:     def f(self):
                    ....:         return self._x^2
                    sage: a = Foo(2)
                    sage: print(a.f.cache)
                    None
                    sage: a.f()
                    4
                    sage: a.f.cache
                    4
        """
    @overload
    def clear_cache(self) -> Any:
        """CachedMethodCallerNoArgs.clear_cache(self)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 2370)

        Clear the cache dictionary.

        EXAMPLES::

            sage: P.<a,b,c,d> = QQ[]
            sage: I = P*[a,b]
            sage: I.gens()
            [a, b]
            sage: I.gens.set_cache('bar')
            sage: I.gens()
            'bar'

        The cache can be emptied and thus the original value will
        be reconstructed::

            sage: I.gens.clear_cache()
            sage: I.gens()
            [a, b]"""
    @overload
    def clear_cache(self) -> Any:
        """CachedMethodCallerNoArgs.clear_cache(self)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 2370)

        Clear the cache dictionary.

        EXAMPLES::

            sage: P.<a,b,c,d> = QQ[]
            sage: I = P*[a,b]
            sage: I.gens()
            [a, b]
            sage: I.gens.set_cache('bar')
            sage: I.gens()
            'bar'

        The cache can be emptied and thus the original value will
        be reconstructed::

            sage: I.gens.clear_cache()
            sage: I.gens()
            [a, b]"""
    @overload
    def is_in_cache(self) -> Any:
        """CachedMethodCallerNoArgs.is_in_cache(self)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 2393)

        Answers whether the return value is already in the cache.

        .. NOTE::

            Recall that a cached method without arguments cannot cache
            the return value ``None``.

        EXAMPLES::

            sage: P.<x,y> = QQ[]
            sage: I = P*[x,y]
            sage: I.gens.is_in_cache()
            False
            sage: I.gens()
            [x, y]
            sage: I.gens.is_in_cache()
            True"""
    @overload
    def is_in_cache(self) -> Any:
        """CachedMethodCallerNoArgs.is_in_cache(self)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 2393)

        Answers whether the return value is already in the cache.

        .. NOTE::

            Recall that a cached method without arguments cannot cache
            the return value ``None``.

        EXAMPLES::

            sage: P.<x,y> = QQ[]
            sage: I = P*[x,y]
            sage: I.gens.is_in_cache()
            False
            sage: I.gens()
            [x, y]
            sage: I.gens.is_in_cache()
            True"""
    @overload
    def is_in_cache(self) -> Any:
        """CachedMethodCallerNoArgs.is_in_cache(self)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 2393)

        Answers whether the return value is already in the cache.

        .. NOTE::

            Recall that a cached method without arguments cannot cache
            the return value ``None``.

        EXAMPLES::

            sage: P.<x,y> = QQ[]
            sage: I = P*[x,y]
            sage: I.gens.is_in_cache()
            False
            sage: I.gens()
            [x, y]
            sage: I.gens.is_in_cache()
            True"""
    @overload
    def set_cache(self, value) -> Any:
        """CachedMethodCallerNoArgs.set_cache(self, value)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 2336)

        Override the cache with a specific value.

        .. NOTE::

            ``None`` is not suitable for a cached value. It would be
            interpreted as an empty cache, forcing a new computation.

        EXAMPLES::

            sage: P.<a,b,c,d> = QQ[]
            sage: I = P*[a,b]
            sage: I.gens()
            [a, b]
            sage: I.gens.set_cache('bar')
            sage: I.gens()
            'bar'

        The cache can be emptied and thus the original value will
        be reconstructed::

            sage: I.gens.clear_cache()
            sage: I.gens()
            [a, b]

        The attempt to assign ``None`` to the cache fails::

            sage: I.gens.set_cache(None)
            sage: I.gens()
            [a, b]"""
    @overload
    def set_cache(self, _None) -> Any:
        """CachedMethodCallerNoArgs.set_cache(self, value)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 2336)

        Override the cache with a specific value.

        .. NOTE::

            ``None`` is not suitable for a cached value. It would be
            interpreted as an empty cache, forcing a new computation.

        EXAMPLES::

            sage: P.<a,b,c,d> = QQ[]
            sage: I = P*[a,b]
            sage: I.gens()
            [a, b]
            sage: I.gens.set_cache('bar')
            sage: I.gens()
            'bar'

        The cache can be emptied and thus the original value will
        be reconstructed::

            sage: I.gens.clear_cache()
            sage: I.gens()
            [a, b]

        The attempt to assign ``None`` to the cache fails::

            sage: I.gens.set_cache(None)
            sage: I.gens()
            [a, b]"""
    def __call__(self) -> Any:
        """CachedMethodCallerNoArgs.__call__(self)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 2318)

        Call the cached method.

        EXAMPLES::

            sage: P.<a,b,c,d> = QQ[]
            sage: I = P*[a,b]
            sage: I.gens()    # indirect doctest
            [a, b]
            sage: I.gens() is I.gens()
            True"""
    def __get__(self, inst, cls) -> Any:
        """CachedMethodCallerNoArgs.__get__(self, inst, cls)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 2415)

        Get a :class:`CachedMethodCallerNoArgs` bound to a specific
        instance of the class of the cached method.

        NOTE:

        :class:`CachedMethodCallerNoArgs` has a separate ``__get__``
        since the categories framework creates and caches the
        return value of ``CachedMethod.__get__`` with
        ``inst==None``.

        This getter attempts to assign a bound method as an
        attribute to the given instance. If this is not
        possible (for example, for some extension classes),
        it is attempted to find an attribute ``_cached_methods``,
        and store/retrieve the bound method there. In that
        way, cached methods can be implemented for extension
        classes deriving from :class:`~sage.structure.parent.Parent`
        and :class:`~sage.structure.element.Element`.

        TESTS:

        Due to the separate ``__get__`` method, it is possible
        to define a cached method in one class and use it as
        an attribute of another class. ::

            sage: class Foo:
            ....:     def __init__(self, n):
            ....:         self.__n = n
            ....:     @cached_method
            ....:     def f(self):
            ....:         return self.__n^2
            sage: class Bar:
            ....:     f = Foo.f
            sage: b1 = Bar()
            sage: b2 = Bar()

        The :class:`CachedMethod` is replaced by an instance of
        :class:`CachedMethodCallerNoArgs` that is set as an
        attribute. Hence, we have::

            sage: b1.f is b1.f
            True
            sage: type(b1.f)
            <class 'sage.misc.cachefunc.CachedMethodCallerNoArgs'>

        Any instance of ``Bar`` gets its own instance of
        :class:`CachedMethodCaller`::

            sage: b1.f is b2.f
            False

        The method caller knows the instance that it belongs
        to::

            sage: Foo.f._instance is None
            True
            sage: b1.f._instance is b1
            True
            sage: b2.f._instance is b2
            True"""
    def __reduce__(self) -> Any:
        '''CachedMethodCallerNoArgs.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 2275)

        Since functions cannot be pickled, the cached method caller
        is pickled by a :class:`CachedMethodPickle`, that replaces
        itself by an actual :class:`CachedMethodCallerNoArgs` as soon
        as it is asked to do anything.

        TESTS::

            sage: P.<a,b,c,d> = QQ[]
            sage: I = P*[a,b]
            sage: I.gens()
            [a, b]
            sage: I.gens
            Cached version of <function ...gens at 0x...>
            sage: J = loads(dumps(I))
            sage: J.gens
            Pickle of the cached method "gens"
            sage: J.gens.cache  # the cache is dropped because gens is not marked with do_pickle=True
            sage: J.gens
            Cached version of <function ...gens at 0x...>'''

class CachedMethodPickle:
    '''File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 1468)

        This class helps to unpickle cached methods.

        .. NOTE::

            Since :issue:`8611`, a cached method is an attribute
            of the instance (provided that it has a ``__dict__``).
            Hence, when pickling the instance, it would be attempted
            to pickle that attribute as well, but this is a problem,
            since functions cannot be pickled, currently. Therefore,
            we replace the actual cached method by a place holder,
            that kills itself as soon as any attribute is requested.
            Then, the original cached attribute is reinstated. But the
            cached values are in fact saved (if ``do_pickle`` is set.)

        EXAMPLES::

            sage: R.<x, y, z> = PolynomialRing(QQ, 3)
            sage: I = R * (x^3 + y^3 + z^3, x^4 - y^4)
            sage: I.groebner_basis()                                                        # needs sage.libs.singular
            [y^5*z^3 - 1/4*x^2*z^6 + 1/2*x*y*z^6 + 1/4*y^2*z^6,
             x^2*y*z^3 - x*y^2*z^3 + 2*y^3*z^3 + z^6,
             x*y^3 + y^4 + x*z^3, x^3 + y^3 + z^3]
            sage: I.groebner_basis
            Cached version of <function ...groebner_basis at 0x...>

        We now pickle and unpickle the ideal. The cached method
        ``groebner_basis`` is replaced by a placeholder::

            sage: J = loads(dumps(I))
            sage: J.groebner_basis
            Pickle of the cached method "groebner_basis"

        But as soon as any other attribute is requested from the
        placeholder, it replaces itself by the cached method, and
        the entries of the cache are actually preserved::

            sage: J.groebner_basis.is_in_cache()                                            # needs sage.libs.singular
            True
            sage: J.groebner_basis
            Cached version of <function ...groebner_basis at 0x...>
            sage: J.groebner_basis() == I.groebner_basis()                                  # needs sage.libs.singular
            True

        TESTS:

        Since :issue:`11115`, there is a special implementation for
        cached methods that don\'t take arguments::

            sage: class A:
            ....:     @cached_method(do_pickle=True)
            ....:     def f(self): return 1
            ....:     @cached_method(do_pickle=True)
            ....:     def g(self, x): return x

            sage: import __main__
            sage: __main__.A = A
            sage: a = A()
            sage: type(a.f)
            <class \'sage.misc.cachefunc.CachedMethodCallerNoArgs\'>
            sage: type(a.g)
            <class \'sage.misc.cachefunc.CachedMethodCaller\'>

        We demonstrate that both implementations can be pickled and
        preserve the cache. For that purpose, we assign nonsense to the
        cache. Of course, it is a very bad idea to override the cache in
        that way.  So, please don\'t try this at home::

            sage: a.f.set_cache(0)
            sage: a.f()
            0
            sage: a.g.set_cache(0,x=1)
            sage: a.g(1)
            0
            sage: b = loads(dumps(a))
            sage: b.f()
            0
            sage: b.g(1)
            0

        Anyway, the cache will be automatically reconstructed after
        clearing it::

            sage: a.f.clear_cache()
            sage: a.f()
            1

            sage: a.g.clear_cache()
            sage: a.g(1)
            1

        AUTHOR:

        - Simon King (2011-01)
    '''
    def __init__(self, inst, name, cache=...) -> Any:
        '''CachedMethodPickle.__init__(self, inst, name, cache=None)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 1564)

        INPUT:

        - ``inst`` -- some instance
        - ``name`` -- string; usually the name of an attribute
          of ``inst`` to which ``self`` is assigned

        TESTS::

            sage: from sage.misc.cachefunc import CachedMethodPickle
            sage: P = CachedMethodPickle(1, \'foo\')
            sage: P
            Pickle of the cached method "foo"'''
    def __call__(self, *args, **kwds) -> Any:
        '''CachedMethodPickle.__call__(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 1627)

        The purpose of this call method is to kill ``self`` and to
        replace it by an actual :class:`CachedMethodCaller`. The last
        thing that ``self`` does before disappearing is to call the
        :class:`CachedMethodCaller` and return the result.

        EXAMPLES::

            sage: P.<a,b,c,d> = QQ[]
            sage: I = P*[a,b]
            sage: I.gens
            Cached version of <function ...gens at 0x...>
            sage: J = loads(dumps(I))
            sage: J.gens
            Pickle of the cached method "gens"
            sage: J.gens()   # indirect doctest
            [a, b]
            sage: J.gens
            Cached version of <function ...gens at 0x...>'''
    def __getattr__(self, s) -> Any:
        '''CachedMethodPickle.__getattr__(self, s)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 1658)

        TESTS::

            sage: R.<x, y, z> = PolynomialRing(QQ, 3)
            sage: I = R * (x^3 + y^3 + z^3, x^4 - y^4)
            sage: G = I.groebner_basis()                                                # needs sage.libs.singular
            sage: J = loads(dumps(I))
            sage: J.groebner_basis
            Pickle of the cached method "groebner_basis"

        If an attribute of name ``s`` is requested (say,
        ``is_in_cache``), the attribute ``self._name`` of
        ``self._instance`` is deleted. Then, the attribute
        of name ``s`` of the attribute ``self._name`` of
        ``self._instance`` is requested. Since ``self._name``
        is a cached method defined for the class of
        ``self._instance``, retrieving the just-deleted
        attribute ``self._name`` succeeds.

        In that way, the unpickling of the cached method is
        finally accomplished::

            sage: J.groebner_basis.is_in_cache()  # indirect doctest                    # needs sage.libs.singular
            True
            sage: J.groebner_basis
            Cached version of <function ...groebner_basis at 0x...>'''
    def __reduce__(self) -> Any:
        '''CachedMethodPickle.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 1596)

        This class is a pickle. However, sometimes, pickles
        need to be pickled another time.

        TESTS::

            sage: R.<x, y, z> = PolynomialRing(QQ, 3)
            sage: I = R * (x^3 + y^3 + z^3, x^4 - y^4)
            sage: I.groebner_basis()                                                    # needs sage.libs.singular
            [y^5*z^3 - 1/4*x^2*z^6 + 1/2*x*y*z^6 + 1/4*y^2*z^6,
             x^2*y*z^3 - x*y^2*z^3 + 2*y^3*z^3 + z^6,
             x*y^3 + y^4 + x*z^3, x^3 + y^3 + z^3]
            sage: J = loads(dumps(I))
            sage: J.groebner_basis
            Pickle of the cached method "groebner_basis"

        When we now pickle ``J``, the pickle of the cached method
        needs to be taken care of::

            sage: K = loads(dumps(J))  # indirect doctest
            sage: K.groebner_basis
            Pickle of the cached method "groebner_basis"
            sage: K.groebner_basis.cache                                                # needs sage.libs.singular
            {((\'\', None, None, False), ()):
            [y^5*z^3 - 1/4*x^2*z^6 + 1/2*x*y*z^6 + 1/4*y^2*z^6,
             x^2*y*z^3 - x*y^2*z^3 + 2*y^3*z^3 + z^6,
             x*y^3 + y^4 + x*z^3, x^3 + y^3 + z^3]}'''

class CachedSpecialMethod(CachedMethod):
    '''File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 2915)

        Cached version of *special* python methods.

        IMPLEMENTATION:

        For new style classes ``C``, it is not possible to override a special
        method, such as ``__hash__``, in the ``__dict__`` of an instance ``c`` of
        ``C``, because Python will always use what is provided by the class, not
        by the instance to avoid metaclass confusion. See
        `<https://docs.python.org/3/reference/datamodel.html#special-method-lookup>`_.

        By consequence, if ``__hash__`` would be wrapped by using
        :class:`CachedMethod`, then ``hash(c)`` will access ``C.__hash__`` and bind
        it to ``c``, which means that the ``__get__`` method of
        :class:`CachedMethod` will be called. But there, we assume that Python has
        already inspected ``__dict__``, and thus a :class:`CachedMethodCaller`
        will be created over and over again.

        Here, the ``__get__`` method will explicitly access the ``__dict__``, so that
        ``hash(c)`` will rely on a single :class:`CachedMethodCaller` stored in
        the ``__dict__``.

        EXAMPLES::

            sage: class C:
            ....:     @cached_method
            ....:     def __hash__(self):
            ....:         print("compute hash")
            ....:         return int(5)
            ....:
            sage: c = C()
            sage: type(C.__hash__)
            <class \'sage.misc.cachefunc.CachedMethodCallerNoArgs\'>

        The hash is computed only once, subsequent calls will use the value from
        the cache. This was implemented in :issue:`12601`.

        ::

            sage: hash(c)       # indirect doctest
            compute hash
            5
            sage: hash(c)
            5
    '''
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def __get__(self, inst, cls) -> Any:
        '''CachedSpecialMethod.__get__(self, inst, cls)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 2961)

        Bind a :class:`CachedMethodCaller` to a specific instance, using ``__dict__``.

        EXAMPLES::

            sage: class C:
            ....:     @cached_method
            ....:     def __hash__(self):
            ....:         print("compute hash")
            ....:         return int(5)
            sage: c = C()
            sage: type(C.__hash__)
            <class \'sage.misc.cachefunc.CachedMethodCallerNoArgs\'>
            sage: hash(c)       # indirect doctest
            compute hash
            5
            sage: hash(c)
            5

        Verify that :issue:`16337` has been resolved::

            sage: class Foo:
            ....:     @cached_method(key=lambda self, x:x+1)
            ....:     def __hash__(self, x=0):
            ....:         return x

            sage: a = Foo()
            sage: a.__hash__(0)
            0
            sage: a.__hash__.cache
            {1: 0}'''

class DiskCachedFunction(CachedFunction):
    """File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 3689)

        Works similar to CachedFunction, but instead, we keep the
        cache on disk (optionally, we keep it in memory too).

        EXAMPLES::

            sage: from sage.misc.cachefunc import DiskCachedFunction
            sage: dir = tmp_dir()
            sage: factor = DiskCachedFunction(factor, dir, memory_cache=True)
            sage: f = factor(2775); f
            3 * 5^2 * 37
            sage: f is factor(2775)
            True
    """
    def __init__(self, f, dir, memory_cache=..., key=...) -> Any:
        """DiskCachedFunction.__init__(self, f, dir, memory_cache=False, key=None)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 3704)

        EXAMPLES::

            sage: from sage.misc.cachefunc import DiskCachedFunction
            sage: def foo(x): sleep(x)
            sage: dir = tmp_dir()
            sage: bar = DiskCachedFunction(foo, dir, memory_cache = False)
            sage: w = walltime()
            sage: for i in range(10): bar(1)
            sage: walltime(w) < 2
            True"""

class FileCache:
    """File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 3360)

        :class:`FileCache` is a dictionary-like class which stores keys
        and values on disk.  The keys take the form of a tuple ``(A,K)``

        - ``A`` -- tuple of objects ``t`` where each ``t`` is an
          exact object which is uniquely identified by a short string

        - ``K`` -- tuple of tuples ``(s,v)`` where ``s`` is a valid
          variable name and ``v`` is an exact object which is uniquely
          identified by a short string with letters [a-zA-Z0-9-._]

        The primary use case is the :class:`DiskCachedFunction`.  If
        ``memory_cache == True``, we maintain a cache of objects seen
        during this session in memory -- but we don't load them from
        disk until necessary.  The keys and values are stored in a
        pair of files:

        - ``prefix-argstring.key.sobj`` contains the ``key`` only,
        - ``prefix-argstring.sobj`` contains the tuple ``(key,val)``

        where ``self[key] == val``.

        .. NOTE::

            We assume that each :class:`FileCache` lives in its own directory.
            Use **extreme** caution if you wish to break that assumption.
    """
    def __init__(self, dir, prefix=..., memory_cache=...) -> Any:
        """FileCache.__init__(self, dir, prefix='', memory_cache=False)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 3388)

        EXAMPLES::

            sage: from sage.misc.cachefunc import FileCache
            sage: dir = tmp_dir()
            sage: FC = FileCache(dir, memory_cache = True)
            sage: FC[((),())] = 1
            sage: FC[((1,2),())] = 2
            sage: FC[((),())]
            1"""
    @overload
    def clear(self) -> Any:
        """FileCache.clear(self)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 3520)

        Clear all key, value pairs from ``self`` and unlink the associated files
        from the file cache.

        EXAMPLES::

            sage: from sage.misc.cachefunc import FileCache
            sage: dir = tmp_dir()
            sage: FC1 = FileCache(dir, memory_cache=False, prefix='foo')
            sage: FC2 = FileCache(dir, memory_cache=False, prefix='foo')
            sage: k1 = ((), (('a', 1),))
            sage: t1 = randint(0, 1000)
            sage: k2 = ((), (('b', 1),))
            sage: t2 = randint(0, 1000)
            sage: FC1[k1] = t1
            sage: FC2[k2] = t2
            sage: FC2.clear()
            sage: k1 in FC1
            False
            sage: k2 in FC1
            False"""
    @overload
    def clear(self) -> Any:
        """FileCache.clear(self)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 3520)

        Clear all key, value pairs from ``self`` and unlink the associated files
        from the file cache.

        EXAMPLES::

            sage: from sage.misc.cachefunc import FileCache
            sage: dir = tmp_dir()
            sage: FC1 = FileCache(dir, memory_cache=False, prefix='foo')
            sage: FC2 = FileCache(dir, memory_cache=False, prefix='foo')
            sage: k1 = ((), (('a', 1),))
            sage: t1 = randint(0, 1000)
            sage: k2 = ((), (('b', 1),))
            sage: t2 = randint(0, 1000)
            sage: FC1[k1] = t1
            sage: FC2[k2] = t2
            sage: FC2.clear()
            sage: k1 in FC1
            False
            sage: k2 in FC1
            False"""
    @overload
    def file_list(self) -> Any:
        """FileCache.file_list(self)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 3412)

        Return the list of files corresponding to ``self``.

        EXAMPLES::

            sage: from sage.misc.cachefunc import FileCache
            sage: dir = tmp_dir()
            sage: FC = FileCache(dir, memory_cache = True, prefix='t')
            sage: FC[((),())] = 1
            sage: FC[((1,2),())] = 2
            sage: FC[((1,),(('a',1),))] = 3
            sage: for f in sorted(FC.file_list()): print(f[len(dir):])
            t-.key.sobj
            t-.sobj
            t-1_2.key.sobj
            t-1_2.sobj
            t-a-1.1.key.sobj
            t-a-1.1.sobj"""
    @overload
    def file_list(self) -> Any:
        """FileCache.file_list(self)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 3412)

        Return the list of files corresponding to ``self``.

        EXAMPLES::

            sage: from sage.misc.cachefunc import FileCache
            sage: dir = tmp_dir()
            sage: FC = FileCache(dir, memory_cache = True, prefix='t')
            sage: FC[((),())] = 1
            sage: FC[((1,2),())] = 2
            sage: FC[((1,),(('a',1),))] = 3
            sage: for f in sorted(FC.file_list()): print(f[len(dir):])
            t-.key.sobj
            t-.sobj
            t-1_2.key.sobj
            t-1_2.sobj
            t-a-1.1.key.sobj
            t-a-1.1.sobj"""
    @overload
    def items(self) -> Any:
        """FileCache.items(self)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 3441)

        Return a list of tuples ``(k,v)`` where ``self[k] = v``.

        EXAMPLES::

            sage: from sage.misc.cachefunc import FileCache
            sage: dir = tmp_dir()
            sage: FC = FileCache(dir, memory_cache = False)
            sage: FC[((),())] = 1
            sage: FC[((1,2),())] = 2
            sage: FC[((1,),(('a',1),))] = 3
            sage: I = FC.items()
            sage: I.sort(); I
            [(((), ()), 1), (((1,), (('a', 1),)), 3), (((1, 2), ()), 2)]"""
    @overload
    def items(self) -> Any:
        """FileCache.items(self)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 3441)

        Return a list of tuples ``(k,v)`` where ``self[k] = v``.

        EXAMPLES::

            sage: from sage.misc.cachefunc import FileCache
            sage: dir = tmp_dir()
            sage: FC = FileCache(dir, memory_cache = False)
            sage: FC[((),())] = 1
            sage: FC[((1,2),())] = 2
            sage: FC[((1,),(('a',1),))] = 3
            sage: I = FC.items()
            sage: I.sort(); I
            [(((), ()), 1), (((1,), (('a', 1),)), 3), (((1, 2), ()), 2)]"""
    @overload
    def keys(self) -> Any:
        """FileCache.keys(self)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 3497)

        Return a list of keys ``k`` where ``self[k]`` is defined.

        EXAMPLES::

            sage: from sage.misc.cachefunc import FileCache
            sage: dir = tmp_dir()
            sage: FC = FileCache(dir, memory_cache = False)
            sage: FC[((),())] = 1
            sage: FC[((1,2),())] = 2
            sage: FC[((1,),(('a',1),))] = 3
            sage: K = FC.keys()
            sage: K.sort(); K
            [((), ()), ((1,), (('a', 1),)), ((1, 2), ())]"""
    @overload
    def keys(self) -> Any:
        """FileCache.keys(self)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 3497)

        Return a list of keys ``k`` where ``self[k]`` is defined.

        EXAMPLES::

            sage: from sage.misc.cachefunc import FileCache
            sage: dir = tmp_dir()
            sage: FC = FileCache(dir, memory_cache = False)
            sage: FC[((),())] = 1
            sage: FC[((1,2),())] = 2
            sage: FC[((1,),(('a',1),))] = 3
            sage: K = FC.keys()
            sage: K.sort(); K
            [((), ()), ((1,), (('a', 1),)), ((1, 2), ())]"""
    @overload
    def values(self) -> Any:
        """FileCache.values(self)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 3459)

        Return a list of values that are stored in ``self``.

        EXAMPLES::

            sage: from sage.misc.cachefunc import FileCache
            sage: dir = tmp_dir()
            sage: FC = FileCache(dir, memory_cache = False)
            sage: FC[((),())] = 1
            sage: FC[((1,2),())] = 2
            sage: FC[((1,),(('a',1),))] = 3
            sage: FC[((),(('a',1),))] = 4
            sage: v = FC.values()
            sage: v.sort(); v
            [1, 2, 3, 4]"""
    @overload
    def values(self) -> Any:
        """FileCache.values(self)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 3459)

        Return a list of values that are stored in ``self``.

        EXAMPLES::

            sage: from sage.misc.cachefunc import FileCache
            sage: dir = tmp_dir()
            sage: FC = FileCache(dir, memory_cache = False)
            sage: FC[((),())] = 1
            sage: FC[((1,2),())] = 2
            sage: FC[((1,),(('a',1),))] = 3
            sage: FC[((),(('a',1),))] = 4
            sage: v = FC.values()
            sage: v.sort(); v
            [1, 2, 3, 4]"""
    def __contains__(self, key) -> Any:
        """FileCache.__contains__(self, key)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 3574)

        Return ``True`` if ``self[key]`` is defined and ``False`` otherwise.

        EXAMPLES::

            sage: from sage.misc.cachefunc import FileCache
            sage: dir = tmp_dir()
            sage: FC = FileCache(dir, memory_cache = False, prefix='foo')
            sage: k = ((),(('a',1),))
            sage: FC[k] = True
            sage: k in FC
            True
            sage: ((),()) in FC
            False"""
    def __delitem__(self, key) -> Any:
        """FileCache.__delitem__(self, key)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 3661)

        Delete the ``key, value`` pair from ``self`` and unlink the associated
        files from the file cache.

        EXAMPLES::

            sage: from sage.misc.cachefunc import FileCache
            sage: dir = tmp_dir()
            sage: FC1 = FileCache(dir, memory_cache = False, prefix='foo')
            sage: FC2 = FileCache(dir, memory_cache = False, prefix='foo')
            sage: k = ((),(('a',1),))
            sage: t = randint(0, 1000)
            sage: FC1[k] = t
            sage: del FC2[k]
            sage: k in FC1
            False"""
    def __getitem__(self, key) -> Any:
        """FileCache.__getitem__(self, key)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 3592)

        Return the value set by ``self[key] = val``, in this session
        or a previous one.

        EXAMPLES::

            sage: from sage.misc.cachefunc import FileCache
            sage: dir = tmp_dir()
            sage: FC1 = FileCache(dir, memory_cache = False, prefix='foo')
            sage: FC2 = FileCache(dir, memory_cache = False, prefix='foo')
            sage: k = ((),(('a',1),))
            sage: t = randint(0, 1000)
            sage: FC1[k] = t
            sage: FC2[k] == FC1[k] == t
            True
            sage: FC1[(1,2),(('a',4),('b',2))]
            Traceback (most recent call last):
            ...
            KeyError: ((1, 2), (('a', 4), ('b', 2)))"""
    def __iter__(self) -> Any:
        """FileCache.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 3478)

        Return a list of keys of ``self``.

        EXAMPLES::

            sage: from sage.misc.cachefunc import FileCache
            sage: dir = tmp_dir()
            sage: FC = FileCache(dir, memory_cache = False)
            sage: FC[((),())] = 1
            sage: FC[((1,2),())] = 2
            sage: FC[((1,),(('a',1),))] = 3
            sage: for k in sorted(FC): print(k)
            ((), ())
            ((1,), (('a', 1),))
            ((1, 2), ())"""
    def __setitem__(self, key, value) -> Any:
        """FileCache.__setitem__(self, key, value)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 3632)

        Set ``self[key] = value`` and stores both key and value on
        disk.

        EXAMPLES::

            sage: from sage.misc.cachefunc import FileCache
            sage: dir = tmp_dir()
            sage: FC1 = FileCache(dir, memory_cache = False, prefix='foo')
            sage: FC2 = FileCache(dir, memory_cache = False, prefix='foo')
            sage: k = ((),(('a',1),))
            sage: t = randint(0, 1000)
            sage: FC1[k] = t
            sage: FC2[k] == t
            True
            sage: FC1[k] = 2000
            sage: FC2[k]!= t
            True"""

class GloballyCachedMethodCaller(CachedMethodCaller):
    """File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 2499)

        Implementation of cached methods in case that the cache is not
        stored in the instance, but in some global object. In particular,
        it is used to implement :class:`CachedInParentMethod`.

        The only difference is that the instance is used as part of the
        key.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class NonpicklingDict(dict):
    """File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 525)

        A special dict which does not pickle its contents.

        EXAMPLES::

            sage: from sage.misc.cachefunc import NonpicklingDict
            sage: d = NonpicklingDict()
            sage: d[0] = 0
            sage: loads(dumps(d))
            {}
    """
    @classmethod
    def __init__(cls) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def __reduce__(self) -> Any:
        """NonpicklingDict.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 537)

        Return data required to unpickle this dictionary.

        EXAMPLES::

            sage: from sage.misc.cachefunc import NonpicklingDict
            sage: d = NonpicklingDict()
            sage: d[0] = 0
            sage: d.__reduce__()
            (<class 'sage.misc.cachefunc.NonpicklingDict'>, ())"""
    @overload
    def __reduce__(self) -> Any:
        """NonpicklingDict.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 537)

        Return data required to unpickle this dictionary.

        EXAMPLES::

            sage: from sage.misc.cachefunc import NonpicklingDict
            sage: d = NonpicklingDict()
            sage: d[0] = 0
            sage: d.__reduce__()
            (<class 'sage.misc.cachefunc.NonpicklingDict'>, ())"""

class WeakCachedFunction(CachedFunction):
    '''WeakCachedFunction(f, classmethod=False, *, name=None, key=None, **kwds)

    File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 1276)

    A version of :class:`CachedFunction` using weak references on the
    values.

    If ``f`` is a function, do either ``g = weak_cached_function(f)`` to make
    a cached version of ``f``, or put ``@weak_cached_function`` right before
    the definition of ``f`` (i.e., use Python decorators)::

        @weak_cached_function
        def f(...):
            ...

    As an exception meant to improve performance, the most recently
    computed values are strongly referenced. The number of strongly
    cached values can be controlled by the ``cache`` keyword.

    EXAMPLES::

        sage: from sage.misc.cachefunc import weak_cached_function
        sage: class A: pass
        sage: @weak_cached_function(cache=0)
        ....: def f():
        ....:     print("doing a computation")
        ....:     return A()
        sage: a = f()
        doing a computation

    The result is cached::

        sage: b = f()
        sage: a is b
        True

    However, if there are no strong references left, the result is
    deleted, and thus a new computation takes place::

        sage: del a
        sage: del b
        sage: a = f()
        doing a computation

    Above, we used the ``cache=0`` keyword. With a larger value, the
    most recently computed values are cached anyway, even if they are
    not referenced::

        sage: @weak_cached_function(cache=3)
        ....: def f(x):
        ....:     print("doing a computation for x={}".format(x))
        ....:     return A()
        sage: a = f(1); del a
        doing a computation for x=1
        sage: a = f(2), f(1); del a
        doing a computation for x=2
        sage: a = f(3), f(1); del a
        doing a computation for x=3
        sage: a = f(4), f(1); del a
        doing a computation for x=4
        doing a computation for x=1
        sage: a = f(5), f(1); del a
        doing a computation for x=5

    The parameter ``key`` can be used to ignore parameters for
    caching. In this example we ignore the parameter ``algorithm``::

        sage: @weak_cached_function(key=lambda x,algorithm: x)
        ....: def mod_ring(x, algorithm=\'default\'):
        ....:     return IntegerModRing(x)
        sage: mod_ring(1,algorithm=\'default\') is mod_ring(1,algorithm=\'algorithm\') is mod_ring(1) is mod_ring(1,\'default\')
        True

    TESTS:

    Check that :issue:`16316` has been fixed, i.e., caching works for
    immutable unhashable objects which define
    :meth:`sage.structure.sage_object.SageObject._cache_key`::

        sage: # needs sage.rings.padics
        sage: from sage.misc.cachefunc import weak_cached_function
        sage: @weak_cached_function
        ....: def f(x): return x+x
        sage: K.<u> = Qq(4)
        sage: R.<t> = K[]
        sage: x = t + K(1,1); x
        (1 + O(2^20))*t + 1 + O(2)
        sage: y = t + K(1,2); y
        (1 + O(2^20))*t + 1 + O(2^2)
        sage: x == y
        True
        sage: f(x) is f(x)
        True
        sage: f(y) is not f(x)
        True

    Examples and tests for ``is_in_cache``::

        sage: from sage.misc.cachefunc import weak_cached_function
        sage: class A:
        ....:     def __init__(self, x):
        ....:         self.x = x
        sage: @weak_cached_function(cache=0)
        ....: def f(n):
        ....:    return A(n)
        sage: a = f(5)

    The key 5 is in the cache, as long as there is a strong
    reference to the corresponding value::

        sage: f.is_in_cache(5)
        True

    However, if there are no strong references left, the cached
    item is removed from the cache::

        sage: del a
        sage: f.is_in_cache(5)
        False

    Check that :issue:`16316` has been fixed, i.e., caching works for
    immutable unhashable objects which define
    :meth:`sage.structure.sage_object.SageObject._cache_key`::

        sage: # needs sage.rings.padics
        sage: from sage.misc.cachefunc import weak_cached_function
        sage: @weak_cached_function
        ....: def f(x): return x
        sage: K.<u> = Qq(4)
        sage: R.<t> = K[]
        sage: f.is_in_cache(t)
        False
        sage: f(t)
        (1 + O(2^20))*t
        sage: f.is_in_cache(t)
        True

    Examples and tests for ``set_cache``::

        sage: from sage.misc.cachefunc import weak_cached_function
        sage: @weak_cached_function
        ....: def f(n):
        ....:     raise RuntimeError
        sage: f.set_cache(ZZ, 5)
        sage: f(5)
        Integer Ring

    Check that :issue:`16316` has been fixed, i.e., caching works for
    immutable unhashable objects which define
    :meth:`sage.structure.sage_object.SageObject._cache_key`::

        sage: # needs sage.rings.padics
        sage: from sage.misc.cachefunc import weak_cached_function
        sage: @weak_cached_function
        ....: def f(x): return x
        sage: K.<u> = Qq(4)
        sage: R.<t> = K[]
        sage: f.set_cache(t,t)
        sage: f.is_in_cache(t)
        True'''
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, f, classmethod=..., name=..., key=..., **kwds) -> Any:
        """File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 1435)

                The inputs to the function must be hashable or they must define
                :meth:`sage.structure.sage_object.SageObject._cache_key`.
                The outputs to the function must be weakly referenceable.

                TESTS::

                    sage: from sage.misc.cachefunc import weak_cached_function
                    sage: class A: pass
                    sage: @weak_cached_function
                    ....: def f():
                    ....:     return A()
                    sage: f
                    Cached version of <function f at ...>

                We demonstrate that pickling works, provided the uncached function
                is available::

                    sage: import __main__
                    sage: __main__.f = f
                    sage: loads(dumps(f))
                    Cached version of <function f at ...>
                    sage: str(f.cache)
                    '<CachedWeakValueDictionary at 0x...>'
        """

class disk_cached_function:
    """File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 3722)

        Decorator for :class:`DiskCachedFunction`.

        EXAMPLES::

            sage: dir = tmp_dir()
            sage: @disk_cached_function(dir)
            ....: def foo(x): return next_prime(2^x)%x
            sage: x = foo(200); x                                                           # needs sage.libs.pari
            11
            sage: @disk_cached_function(dir)
            ....: def foo(x): return 1/x
            sage: foo(200)                                                                  # needs sage.libs.pari
            11
            sage: foo.clear_cache()
            sage: foo(200)
            1/200
    """
    def __init__(self, dir, memory_cache=..., key=...) -> Any:
        """disk_cached_function.__init__(self, dir, memory_cache=False, key=None)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 3741)

        EXAMPLES::

            sage: dir = tmp_dir()
            sage: @disk_cached_function(dir, memory_cache=True)
            ....: def foo(x): return next_prime(2^x)
            sage: x = foo(200)                                                          # needs sage.libs.pari
            sage: x is foo(200)                                                         # needs sage.libs.pari
            True
            sage: @disk_cached_function(dir, memory_cache=False)
            ....: def foo(x): return next_prime(2^x)
            sage: x is foo(200)                                                         # needs sage.libs.pari
            False"""
    def __call__(self, f) -> Any:
        """disk_cached_function.__call__(self, f)

        File: /build/sagemath/src/sage/src/sage/misc/cachefunc.pyx (starting at line 3760)

        EXAMPLES::

            sage: dir = tmp_dir()
            sage: @disk_cached_function(dir)
            ....: def foo(x): return ModularSymbols(x)
            sage: foo(389)                                                              # needs sage.modular
            Modular Symbols space of dimension 65 for Gamma_0(389) of weight 2
             with sign 0 over Rational Field"""
