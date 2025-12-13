import _cython_3_2_1
import sage.misc.sageinspect as sageinspect
from sage.features import FeatureNotPresentError as FeatureNotPresentError
from sage.misc.instancedoc import instancedoc as instancedoc
from typing import Any, ClassVar, overload

attributes: _cython_3_2_1.cython_function_or_method
clean_namespace: _cython_3_2_1.cython_function_or_method
ensure_startup_finished: _cython_3_2_1.cython_function_or_method
finish_startup: _cython_3_2_1.cython_function_or_method
get_star_imports: _cython_3_2_1.cython_function_or_method
is_during_startup: _cython_3_2_1.cython_function_or_method
lazy_import: _cython_3_2_1.cython_function_or_method
save_cache_file: _cython_3_2_1.cython_function_or_method
star_imports: dict
test_fake_startup: _cython_3_2_1.cython_function_or_method

class LazyImport:
    """LazyImport(module, name, as_name=None, at_startup=False, namespace=None, deprecation=None, feature=None)

    File: /build/sagemath/src/sage/src/sage/misc/lazy_import.pyx (starting at line 170)

    EXAMPLES::

        sage: from sage.misc.lazy_import import LazyImport
        sage: my_integer = LazyImport('sage.rings.integer', 'Integer')
        sage: my_integer(4)
        4
        sage: my_integer('101', base=2)
        5
        sage: my_integer(3/2)
        Traceback (most recent call last):
        ...
        TypeError: no conversion of this rational to integer"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, module, name, as_name=..., at_startup=..., namespace=..., deprecation=..., feature=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/misc/lazy_import.pyx (starting at line 186)

                EXAMPLES::

                    sage: from sage.misc.lazy_import import LazyImport
                    sage: lazy_ZZ = LazyImport('sage.rings.integer_ring', 'ZZ')
                    sage: type(lazy_ZZ)
                    <class 'sage.misc.lazy_import.LazyImport'>
                    sage: lazy_ZZ._get_object() is ZZ
                    True
                    sage: type(lazy_ZZ)
                    <class 'sage.misc.lazy_import.LazyImport'>
        """
    def __abs__(self) -> Any:
        """LazyImport.__abs__(self)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_import.pyx (starting at line 802)

        TESTS::

            sage: import sage.all__sagemath_objects
            sage: sage.all__sagemath_objects.foo = -1000
            sage: lazy_import('sage.all__sagemath_objects', 'foo')
            sage: abs(foo)
            1000"""
    def __add__(self, left, right) -> Any:
        """LazyImport.__add__(left, right)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_import.pyx (starting at line 618)

        TESTS::

            sage: import sage.all__sagemath_objects
            sage: sage.all__sagemath_objects.foo = 10
            sage: lazy_import('sage.all__sagemath_objects', 'foo')
            sage: foo + 1
            11"""
    def __and__(self, left, right) -> Any:
        """LazyImport.__and__(left, right)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_import.pyx (starting at line 742)

        TESTS::

            sage: import sage.all__sagemath_objects
            sage: sage.all__sagemath_objects.foo = 10
            sage: lazy_import('sage.all__sagemath_objects', 'foo')
            sage: foo & 7
            2"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __call__(self, *args, **kwds) -> Any:
        """LazyImport.__call__(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_import.pyx (starting at line 384)

        Calling ``self`` calls the wrapped object.

        EXAMPLES::

            sage: from sage.misc.lazy_import import LazyImport
            sage: my_isprime = LazyImport('sage.arith.misc', 'is_prime')
            sage: is_prime(12) == my_isprime(12)
            True
            sage: is_prime(13) == my_isprime(13)
            True"""
    def __complex__(self) -> Any:
        """LazyImport.__complex__(self)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_import.pyx (starting at line 826)

        TESTS::

            sage: import sage.all__sagemath_objects
            sage: sage.all__sagemath_objects.foo = 10
            sage: lazy_import('sage.all__sagemath_objects', 'foo')
            sage: complex(foo)
            (10+0j)"""
    def __contains__(self, item) -> Any:
        """LazyImport.__contains__(self, item)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_import.pyx (starting at line 602)

        TESTS::

            sage: import sys
            sage: py_version = sys.version_info[0]
            sage: lazy_import('sys', 'version_info')
            sage: py_version in version_info
            True

            sage: lazy_import('sys', 'version_info')
            sage: 2000 not in version_info
            True"""
    def __copy__(self) -> Any:
        """LazyImport.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_import.pyx (starting at line 898)

        Support ``copy()``.

        TESTS::

            sage: from sage.misc.lazy_import import LazyImport
            sage: import sage.all__sagemath_objects
            sage: sage.all__sagemath_objects.foo = [[1,2], 3]
            sage: lazy_foo = LazyImport('sage.all__sagemath_objects', 'foo')
            sage: a = copy(lazy_foo)
            sage: a is sage.all__sagemath_objects.foo        # copy
            False
            sage: a[0] is sage.all__sagemath_objects.foo[0]  # copy but not deep
            True
            sage: type(lazy_foo) is LazyImport
            True"""
    def __deepcopy__(self, memo=...) -> Any:
        """LazyImport.__deepcopy__(self, memo=None)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_import.pyx (starting at line 919)

        Support ``copy()``.

        TESTS::

            sage: from sage.misc.lazy_import import LazyImport
            sage: import sage.all__sagemath_objects
            sage: sage.all__sagemath_objects.foo = [[1,2], 3]
            sage: lazy_foo = LazyImport('sage.all__sagemath_objects', 'foo')
            sage: a = deepcopy(lazy_foo)
            sage: a is sage.all__sagemath_objects.foo        # copy
            False
            sage: a[0] is sage.all__sagemath_objects.foo[0]  # deep copy
            False
            sage: type(lazy_foo) is LazyImport
            True"""
    def __delitem__(self, key) -> Any:
        """LazyImport.__delitem__(self, key)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_import.pyx (starting at line 576)

        TESTS::

            sage: from sage.misc.lazy_import import LazyImport
            sage: import sage.all__sagemath_objects
            sage: sage.all__sagemath_objects.foo = list(range(10))
            sage: lazy_foo = LazyImport('sage.all__sagemath_objects', 'foo')
            sage: del lazy_foo[1]
            sage: print(lazy_foo)
            [0, 2, 3, 4, 5, 6, 7, 8, 9]
            sage: print(sage.all__sagemath_objects.foo)
            [0, 2, 3, 4, 5, 6, 7, 8, 9]"""
    def __dir__(self) -> Any:
        """LazyImport.__dir__(self)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_import.pyx (starting at line 370)

        Tab completion on ``self`` defers to completion on the wrapped
        object.

        EXAMPLES::

            sage: from sage.misc.lazy_import import LazyImport
            sage: lazy_ZZ = LazyImport('sage.rings.integer_ring', 'ZZ')
            sage: dir(lazy_ZZ) == dir(ZZ)
            True"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __float__(self) -> Any:
        """LazyImport.__float__(self)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_import.pyx (starting at line 850)

        TESTS::

            sage: import sage.all__sagemath_objects
            sage: sage.all__sagemath_objects.foo = 10
            sage: lazy_import('sage.all__sagemath_objects', 'foo')
            sage: float(foo)
            10.0"""
    def __floordiv__(self, left, right) -> Any:
        """LazyImport.__floordiv__(left, right)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_import.pyx (starting at line 670)

        TESTS::

            sage: import sage.all__sagemath_objects
            sage: sage.all__sagemath_objects.foo = 10
            sage: lazy_import('sage.all__sagemath_objects', 'foo')
            sage: foo  // 3
            3"""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __get__(self, instance, owner) -> Any:
        """LazyImport.__get__(self, instance, owner)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_import.pyx (starting at line 472)

        EXAMPLES:

        Here we show how to take a function in a module, and lazy
        import it as a method of a class. For the sake of this
        example, we add manually a function in :mod:`sage.all__sagemath_objects`::

            sage: def my_method(self): return self
            sage: import sage.all__sagemath_objects
            sage: sage.all__sagemath_objects.my_method = my_method

        Now we lazy import it as a method of a new class ``Foo``::

            sage: from sage.misc.lazy_import import LazyImport
            sage: class Foo():
            ....:     my_method = LazyImport('sage.all__sagemath_objects', 'my_method')

        Now we can use it as a usual method::

            sage: Foo().my_method()
            <__main__.Foo object at ...>
            sage: Foo.my_method
            <function my_method at 0x...>
            sage: Foo().my_method
            <bound method my_method of <__main__.Foo object at ...>>

        When a :class:`LazyImport` method is a method (or attribute)
        of a class, then extra work must be done to replace this
        :class:`LazyImport` object with the actual object. See the
        documentation of :meth:`_get_object` for an explanation of
        this.

        .. NOTE::

           For a :class:`LazyImport` object that appears in a class
           namespace, we need to do something special. Indeed, the
           class namespace dictionary at the time of the class
           definition is not the one that actually gets used. Thus,
           ``__get__`` needs to manually modify the class dict::

               sage: class Foo():
               ....:     lazy_import('sage.plot.plot', 'plot')
               sage: class Bar(Foo):
               ....:     pass
               sage: type(Foo.__dict__['plot'])
               <class 'sage.misc.lazy_import.LazyImport'>

           We access the ``plot`` method::

               sage: Bar.plot                                                           # needs sage.plot
               <function plot at 0x...>

           Now ``plot`` has been replaced in the dictionary of ``Foo``::

               sage: type(Foo.__dict__['plot'])                                         # needs sage.plot
               <... 'function'>"""
    def __getitem__(self, key) -> Any:
        """LazyImport.__getitem__(self, key)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_import.pyx (starting at line 548)

        TESTS::

            sage: import sys
            sage: py_version = sys.version_info[0]
            sage: lazy_import('sys', 'version_info')
            sage: version_info[0] == py_version
            True"""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __hash__(self) -> Any:
        """LazyImport.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_import.pyx (starting at line 436)

        TESTS::

            sage: from sage.misc.lazy_import import LazyImport
            sage: lazy_ZZ = LazyImport('sage.rings.integer_ring', 'ZZ')
            sage: hash(lazy_ZZ) == hash(ZZ)
            True"""
    def __hex__(self) -> Any:
        """LazyImport.__hex__(self)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_import.pyx (starting at line 874)

        TESTS::

            sage: import sage.all__sagemath_objects
            sage: sage.all__sagemath_objects.foo = 10
            sage: lazy_import('sage.all__sagemath_objects', 'foo')
            sage: hex(foo)
            '0xa'"""
    def __index__(self) -> Any:
        """LazyImport.__index__(self)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_import.pyx (starting at line 886)

        TESTS::

            sage: import sage.all__sagemath_objects
            sage: sage.all__sagemath_objects.foo = 10
            sage: lazy_import('sage.all__sagemath_objects', 'foo')
            sage: list(range(100))[foo]
            10"""
    def __instancecheck__(self, x) -> Any:
        """LazyImport.__instancecheck__(self, x)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_import.pyx (starting at line 940)

        Support ``isinstance()``.

        EXAMPLES::

            sage: lazy_import('sage.rings.rational_field', 'RationalField')
            sage: isinstance(QQ, RationalField)
            True

        No object is an instance of a class that cannot be imported::

            sage: lazy_import('sage.xxxxx_does_not_exist', 'DoesNotExist')
            sage: isinstance(QQ, DoesNotExist)
            False"""
    def __int__(self) -> Any:
        """LazyImport.__int__(self)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_import.pyx (starting at line 838)

        TESTS::

            sage: import sage.all__sagemath_objects
            sage: sage.all__sagemath_objects.foo = 10
            sage: lazy_import('sage.all__sagemath_objects', 'foo')
            sage: int(foo)
            10"""
    def __invert__(self) -> Any:
        """LazyImport.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_import.pyx (starting at line 814)

        TESTS::

            sage: import sage.all__sagemath_objects
            sage: sage.all__sagemath_objects.foo = 10
            sage: lazy_import('sage.all__sagemath_objects', 'foo')
            sage: ~foo
            1/10"""
    def __iter__(self) -> Any:
        """LazyImport.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_import.pyx (starting at line 592)

        TESTS::

            sage: lazy_import('sys', 'version_info')
            sage: iter(version_info)
            <...iterator object at ...>"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __len__(self) -> Any:
        """LazyImport.__len__(self)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_import.pyx (starting at line 460)

        TESTS::

            sage: lazy_import('sys', 'version_info')
            sage: type(version_info)
            <class 'sage.misc.lazy_import.LazyImport'>
            sage: len(version_info)
            5"""
    def __lshift__(self, left, right) -> Any:
        """LazyImport.__lshift__(left, right)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_import.pyx (starting at line 718)

        TESTS::

            sage: import sage.all__sagemath_objects
            sage: sage.all__sagemath_objects.foo = 10
            sage: lazy_import('sage.all__sagemath_objects', 'foo')
            sage: foo << 3
            80"""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    @overload
    def __matmul__(self, left, right) -> Any:
        """LazyImport.__matmul__(left, right)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_import.pyx (starting at line 654)

        TESTS::

            sage: # needs sympy
            sage: from sympy import Matrix
            sage: import sage.all__sagemath_objects
            sage: sage.all__sagemath_objects.foo = Matrix([[1,1], [0,1]])
            sage: lazy_import('sage.all__sagemath_objects', 'foo')
            sage: foo.__matmul__(foo)
            Matrix([
            [1, 2],
            [0, 1]])"""
    @overload
    def __matmul__(self, foo) -> Any:
        """LazyImport.__matmul__(left, right)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_import.pyx (starting at line 654)

        TESTS::

            sage: # needs sympy
            sage: from sympy import Matrix
            sage: import sage.all__sagemath_objects
            sage: sage.all__sagemath_objects.foo = Matrix([[1,1], [0,1]])
            sage: lazy_import('sage.all__sagemath_objects', 'foo')
            sage: foo.__matmul__(foo)
            Matrix([
            [1, 2],
            [0, 1]])"""
    def __mod__(self, left, right) -> Any:
        """LazyImport.__mod__(left, right)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_import.pyx (starting at line 706)

        TESTS::

            sage: import sage.all__sagemath_objects
            sage: sage.all__sagemath_objects.foo = 10
            sage: lazy_import('sage.all__sagemath_objects', 'foo')
            sage: foo % 7
            3"""
    def __mul__(self, left, right) -> Any:
        """LazyImport.__mul__(left, right)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_import.pyx (starting at line 642)

        TESTS::

            sage: import sage.all__sagemath_objects
            sage: sage.all__sagemath_objects.foo = 10
            sage: lazy_import('sage.all__sagemath_objects', 'foo')
            sage: foo * 2
            20"""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __neg__(self) -> Any:
        """LazyImport.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_import.pyx (starting at line 778)

        TESTS::

            sage: import sage.all__sagemath_objects
            sage: sage.all__sagemath_objects.foo = 10
            sage: lazy_import('sage.all__sagemath_objects', 'foo')
            sage: -foo
            -10"""
    def __oct__(self) -> Any:
        """LazyImport.__oct__(self)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_import.pyx (starting at line 862)

        TESTS::

            sage: import sage.all__sagemath_objects
            sage: sage.all__sagemath_objects.foo = 10
            sage: lazy_import('sage.all__sagemath_objects', 'foo')
            sage: oct(foo)
            '0o12'"""
    def __or__(self, left, right) -> Any:
        """LazyImport.__or__(left, right)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_import.pyx (starting at line 754)

        TESTS::

            sage: import sage.all__sagemath_objects
            sage: sage.all__sagemath_objects.foo = 10
            sage: lazy_import('sage.all__sagemath_objects', 'foo')
            sage: foo | 7
            15"""
    def __pos__(self) -> Any:
        """LazyImport.__pos__(self)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_import.pyx (starting at line 790)

        TESTS::

            sage: import sage.all__sagemath_objects
            sage: sage.all__sagemath_objects.foo = 10
            sage: lazy_import('sage.all__sagemath_objects', 'foo')
            sage: +foo
            10"""
    def __pow__(self, left, right, mod) -> Any:
        """LazyImport.__pow__(left, right, mod)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_import.pyx (starting at line 694)

        TESTS::

            sage: import sage.all__sagemath_objects
            sage: sage.all__sagemath_objects.foo = 10
            sage: lazy_import('sage.all__sagemath_objects', 'foo')
            sage: foo ** 2
            100"""
    def __radd__(self, other):
        """Return value+self."""
    def __rand__(self, other):
        """Return value&self."""
    def __rfloordiv__(self, other):
        """Return value//self."""
    def __rlshift__(self, other):
        """Return value<<self."""
    def __rmatmul__(self, *args, **kwargs):
        """Return value@self."""
    def __rmod__(self, other):
        """Return value%self."""
    def __rmul__(self, other):
        """Return value*self."""
    def __ror__(self, other):
        """Return value|self."""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
    def __rrshift__(self, other):
        """Return value>>self."""
    def __rshift__(self, left, right) -> Any:
        """LazyImport.__rshift__(left, right)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_import.pyx (starting at line 730)

        TESTS::

            sage: import sage.all__sagemath_objects
            sage: sage.all__sagemath_objects.foo = 10
            sage: lazy_import('sage.all__sagemath_objects', 'foo')
            sage: foo >> 2
            2"""
    def __rsub__(self, other):
        """Return value-self."""
    def __rtruediv__(self, other):
        """Return value/self."""
    def __rxor__(self, other):
        """Return value^self."""
    def __setitem__(self, key, value) -> Any:
        """LazyImport.__setitem__(self, key, value)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_import.pyx (starting at line 560)

        TESTS::

            sage: from sage.misc.lazy_import import LazyImport
            sage: import sage.all__sagemath_objects
            sage: sage.all__sagemath_objects.foo = list(range(10))
            sage: lazy_foo = LazyImport('sage.all__sagemath_objects', 'foo')
            sage: lazy_foo[1] = 100
            sage: print(lazy_foo)
            [0, 100, 2, 3, 4, 5, 6, 7, 8, 9]
            sage: sage.all__sagemath_objects.foo
            [0, 100, 2, 3, 4, 5, 6, 7, 8, 9]"""
    def __sub__(self, left, right) -> Any:
        """LazyImport.__sub__(left, right)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_import.pyx (starting at line 630)

        TESTS::

            sage: import sage.all__sagemath_objects
            sage: sage.all__sagemath_objects.foo = 10
            sage: lazy_import('sage.all__sagemath_objects', 'foo')
            sage: foo - 1
            9"""
    def __subclasscheck__(self, x) -> Any:
        """LazyImport.__subclasscheck__(self, x)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_import.pyx (starting at line 961)

        Support ``issubclass()``.

        EXAMPLES::

            sage: lazy_import('sage.structure.parent', 'Parent')
            sage: issubclass(RationalField, Parent)
            True

        No class is a subclass of a class that cannot be imported::

            sage: lazy_import('sage.xxxxx_does_not_exist', 'DoesNotExist')
            sage: issubclass(RationalField, DoesNotExist)
            False"""
    def __truediv__(self, left, right) -> Any:
        """LazyImport.__truediv__(left, right)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_import.pyx (starting at line 682)

        TESTS::

            sage: import sage.all__sagemath_objects
            sage: sage.all__sagemath_objects.foo = 10
            sage: lazy_import('sage.all__sagemath_objects', 'foo')
            sage: operator.truediv(foo, 3)
            10/3"""
    def __xor__(self, left, right) -> Any:
        """LazyImport.__xor__(left, right)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_import.pyx (starting at line 766)

        TESTS::

            sage: import sage.all__sagemath_objects
            sage: sage.all__sagemath_objects.foo = 10
            sage: lazy_import('sage.all__sagemath_objects', 'foo')
            sage: foo ^^ 7
            13"""
