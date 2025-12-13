import _cython_3_2_1
import sage.structure.sage_object
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.structure.test_factory import test_factory as test_factory
from typing import Any, ClassVar, overload

factory_unpickles: dict
generic_factory_reduce: _cython_3_2_1.cython_function_or_method
generic_factory_unpickle: _cython_3_2_1.cython_function_or_method
i: int
lookup_global: _cython_3_2_1.cython_function_or_method
register_factory_unpickle: _cython_3_2_1.cython_function_or_method

class UniqueFactory(sage.structure.sage_object.SageObject):
    '''UniqueFactory(name)

    File: /build/sagemath/src/sage/src/sage/structure/factory.pyx (starting at line 77)

    This class is intended to make it easy to cache objects.

    It is based on the idea that the object is uniquely defined by a set of
    defining data (the key). There is also the possibility of some
    non-defining data (extra args) which will be used in initial creation,
    but not affect the caching.

    .. WARNING::

        This class only provides *cached representation behaviour*. Hence,
        using :class:`UniqueFactory`, it is still possible to create distinct
        objects that evaluate equal. Unique representation behaviour can be
        added, for example, by additionally inheriting from
        :class:`sage.misc.fast_methods.WithEqualityById`.

    The objects created are cached (using weakrefs) based on their key and
    returned directly rather than re-created if requested again. Pickling is
    taken care of by the factory, and will return the same object for the same
    version of Sage, and distinct (but hopefully equal) objects for different
    versions of Sage.

    .. WARNING::

        The objects returned by a :class:`UniqueFactory` must be instances of
        new style classes (hence, they must be instances of :class:`object`)
        that must not only allow a weak reference, but must accept general
        attribute assignment. Otherwise, pickling won\'t work.

    USAGE:

    A *unique factory* provides a way to create objects from parameters
    (the type of these objects can depend on the parameters, and is often
    determined only at runtime) and to cache them by a certain key
    derived from these parameters, so that when the factory is being
    called again with the same parameters (or just with parameters which
    yield the same key), the object is being returned from cache rather
    than constructed anew.

    An implementation of a unique factory consists of a factory class and
    an instance of this factory class.

    The factory class has to be a class inheriting from ``UniqueFactory``.
    Typically it only needs to implement :meth:`create_key` (a method that
    creates a key from the given parameters, under which key the object
    will be stored in the cache) and :meth:`create_object` (a method that
    returns the actual object from the key). Sometimes, one would also
    implement :meth:`create_key_and_extra_args` (this differs from
    :meth:`create_key` in allowing to also create some additional
    arguments from the given parameters, which arguments then get passed
    to :meth:`create_object` and thus can have an effect on the initial
    creation of the object, but do *not* affect the key) or
    :meth:`other_keys`. Other methods are not supposed to be overloaded.

    The factory class itself cannot be called to create objects. Instead,
    an instance of the factory class has to be created first. For
    technical reasons, this instance has to be provided with a name that
    allows Sage to find its definition. Specifically, the name of the
    factory instance (or the full path to it, if it is not in the global
    namespace) has to be passed to the factory class as a string variable.
    So, if our factory class has been called ``A`` and is located in
    ``sage/spam/battletoads.py``, then we need to define an instance (say,
    ``B``) of ``A`` by writing ``B = A("sage.spam.battletoads.B")``
    (or ``B = A("B")`` if this ``B`` will be imported into global
    namespace). This instance can then be used to create objects (by
    calling ``B(*parameters)``).

    Notice that the objects created by the factory don\'t inherit from the
    factory class. They *do* know about the factory that created them (this
    information, along with the keys under which this factory caches them,
    is stored in the ``_factory_data`` attributes of the objects), but not
    via inheritance.

    EXAMPLES:

    The below examples are rather artificial and illustrate particular
    aspects. For a "real-life" usage case of ``UniqueFactory``, see
    the finite field factory in :mod:`sage.rings.finite_rings.finite_field_constructor`.

    In many cases, a factory class is implemented by providing the two
    methods :meth:`create_key` and :meth:`create_object`. In our example,
    we want to demonstrate how to use "extra arguments" to choose a specific
    implementation, with preference given to an instance found in the cache,
    even if its implementation is different. Hence, we implement
    :meth:`create_key_and_extra_args` rather than :meth:`create_key`, putting
    the chosen implementation into the extra arguments. Then, in the
    :meth:`create_object` method, we create and return instances of the
    specified implementation.
    ::

        sage: from sage.structure.factory import UniqueFactory
        sage: class MyFactory(UniqueFactory):
        ....:     def create_key_and_extra_args(self, *args, **kwds):
        ....:         return args, {\'impl\':kwds.get(\'impl\', None)}
        ....:     def create_object(self, version, key, **extra_args):
        ....:         impl = extra_args[\'impl\']
        ....:         if impl == \'C\':
        ....:             return C(*key)
        ....:         if impl == \'D\':
        ....:             return D(*key)
        ....:         return E(*key)
        ....:

    Now we can create a factory instance. It is supposed to be found under the
    name ``\'F\'`` in the ``__main__`` module. Note that in an interactive
    session, ``F`` would automatically be in the ``__main__`` module. Hence,
    the second and third of the following four lines are only needed in
    doctests.  ::

        sage: F = MyFactory("__main__.F")
        sage: import __main__
        sage: __main__.F = F
        sage: loads(dumps(F)) is F
        True

    Now we create three classes ``C``, ``D`` and ``E``. The first is a Cython
    extension-type class that does not allow weak references nor attribute
    assignment. The second is a Python class that is not derived from
    :class:`object`. The third allows attribute assignment and is derived
    from :class:`object`.  ::

        sage: cython("cdef class C: pass")                                              # needs sage.misc.cython
        sage: class D:
        ....:     def __init__(self, *args):
        ....:         self.t = args
        ....:     def __repr__(self):
        ....:         return "D%s"%repr(self.t)
        ....:
        sage: class E(D, object): pass

    Again, being in a doctest, we need to put the class ``D`` into the
    ``__main__`` module, so that Python can find it::

        sage: import __main__
        sage: __main__.D = D

    It is impossible to create an instance of ``C`` with our factory, since it
    does not allow weak references::

        sage: F(1, impl=\'C\')                                                            # needs sage.misc.cython
        Traceback (most recent call last):
        ...
        TypeError: cannot create weak reference to \'....C\' object

    Let us try again, with a Cython class that does allow weak
    references. Now, creation of an instance using the factory works::

        sage: cython(                                                                   # needs sage.misc.cython
        ....: \'\'\'
        ....: cdef class C:
        ....:     cdef __weakref__
        ....: \'\'\')
        ....:
        sage: c = F(1, impl=\'C\')                                                        # needs sage.misc.cython
        sage: isinstance(c, C)                                                          # needs sage.misc.cython
        True

    The cache is used when calling the factory again---even if it is suggested
    to use a different implementation. This is because the implementation is
    only considered an "extra argument" that does not count for the key.
    ::

        sage: c is F(1, impl=\'C\') is F(1, impl=\'D\') is F(1)                             # needs sage.misc.cython
        True

    However, pickling and unpickling does not use the cache. This is because
    the factory has tried to assign an attribute to the instance that provides
    information on the key used to create the instance, but failed::

        sage: loads(dumps(c)) is c                                                      # needs sage.misc.cython
        False
        sage: hasattr(c, \'_factory_data\')                                               # needs sage.misc.cython
        False

    We have already seen that our factory will only take the requested
    implementation into account if the arguments used as key have not been
    used yet. So, we use other arguments to create an instance of class
    ``D``::

        sage: d = F(2, impl=\'D\')
        sage: isinstance(d, D)
        True

    The factory only knows about the pickling protocol used by new style
    classes. Hence, again, pickling and unpickling fails to use the cache,
    even though the "factory data" are now available (this is not the case
    on Python 3 which *only* has new style classes)::

        sage: loads(dumps(d)) is d
        True
        sage: d._factory_data
        (<__main__.MyFactory object at ...>,
         (...),
         (2,),
         {\'impl\': \'D\'})

    Only when we have a new style class that can be weak referenced and allows
    for attribute assignment, everything works::

        sage: e = F(3)
        sage: isinstance(e, E)
        True
        sage: loads(dumps(e)) is e
        True
        sage: e._factory_data
        (<__main__.MyFactory object at ...>,
         (...),
         (3,),
         {\'impl\': None})'''
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, name) -> Any:
        """File: /build/sagemath/src/sage/src/sage/structure/factory.pyx (starting at line 291)

                INPUT:

                - ``name`` -- string; a name in the global namespace referring to
                  ``self`` or a fully qualified path name to ``self``, which is used to
                  locate the factory on unpickling

                EXAMPLES::

                    sage: from sage.structure.factory import UniqueFactory
                    sage: fake_factory = UniqueFactory('ZZ')
                    sage: loads(dumps(fake_factory))
                    Integer Ring
                    sage: fake_factory = UniqueFactory('sage.rings.rational_field.QQ')
                    sage: loads(dumps(fake_factory))
                    Rational Field
        """
    def create_key(self, *args, **kwds) -> Any:
        """UniqueFactory.create_key(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/structure/factory.pyx (starting at line 477)

        Given the parameters (arguments and keywords), create a key
        that uniquely determines this object.

        EXAMPLES::

            sage: from sage.structure.test_factory import test_factory
            sage: test_factory.create_key(1, 2, key=5)
            (1, 2)"""
    def create_key_and_extra_args(self, *args, **kwds) -> Any:
        """UniqueFactory.create_key_and_extra_args(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/structure/factory.pyx (starting at line 460)

        Return a tuple containing the key (uniquely defining data)
        and any extra arguments (empty by default).

        Defaults to :meth:`create_key`.

        EXAMPLES::

            sage: from sage.structure.test_factory import test_factory
            sage: test_factory.create_key_and_extra_args(1, 2, key=5)
            ((1, 2), {})
            sage: GF.create_key_and_extra_args(3)
            ((3, ('x',), None, 'modn', 3, 1, True, None, None, None, True, False), {})"""
    def create_object(self, version, key, **extra_args) -> Any:
        """UniqueFactory.create_object(self, version, key, **extra_args)

        File: /build/sagemath/src/sage/src/sage/structure/factory.pyx (starting at line 490)

        Create the object from the key and extra arguments. This is only
        called if the object was not found in the cache.

        EXAMPLES::

            sage: from sage.structure.test_factory import test_factory
            sage: test_factory.create_object(0, (1,2,3))
            Making object (1, 2, 3)
            <sage.structure.test_factory.A object at ...>
            sage: test_factory('a')
            Making object ('a',)
            <sage.structure.test_factory.A object at ...>
            sage: test_factory('a') # NOT called again
            <sage.structure.test_factory.A object at ...>"""
    def get_object(self, version, key, extra_args) -> Any:
        """UniqueFactory.get_object(self, version, key, extra_args)

        File: /build/sagemath/src/sage/src/sage/structure/factory.pyx (starting at line 375)

        Return the object corresponding to ``key``, creating it with
        ``extra_args`` if necessary (for example, it isn't in the cache
        or it is unpickling from an older version of Sage).

        EXAMPLES::

            sage: from sage.structure.test_factory import test_factory
            sage: a = test_factory.get_object(3.0, 'a', {}); a
            Making object a
            <sage.structure.test_factory.A object at ...>
            sage: test_factory.get_object(3.0, 'a', {}) is test_factory.get_object(3.0, 'a', {})
            True
            sage: test_factory.get_object(3.0, 'a', {}) is test_factory.get_object(3.1, 'a', {})
            Making object a
            False
            sage: test_factory.get_object(3.0, 'a', {}) is test_factory.get_object(3.0, 'b', {})
            Making object b
            False

        TESTS:

        Check that :issue:`16317` has been fixed, i.e., caching works for
        unhashable objects::

            sage: K.<u> = Qq(4)                                                         # needs sage.rings.padics
            sage: d = test_factory.get_object(3.0, (K(1), 'c'), {})                     # needs sage.rings.padics
            Making object (1 + O(2^20), 'c')
            sage: d is test_factory.get_object(3.0, (K(1), 'c'), {})                    # needs sage.rings.padics
            True"""
    def get_version(self, sage_version) -> Any:
        """UniqueFactory.get_version(self, sage_version)

        File: /build/sagemath/src/sage/src/sage/structure/factory.pyx (starting at line 438)

        This is provided to allow more or less granular control over
        pickle versioning. Objects pickled in the same version of Sage
        will unpickle to the same rather than simply equal objects. This
        can provide significant gains as arithmetic must be performed on
        objects with identical parents. However, if there has been an
        incompatible change (e.g. in element representation) we want the
        version number to change so coercion is forced between the two
        parents.

        Defaults to the Sage version that is passed in, but coarser
        granularity can be provided.

        EXAMPLES::

            sage: from sage.structure.test_factory import test_factory
            sage: test_factory.get_version((3,1,0))
            (3, 1, 0)"""
    @overload
    def other_keys(self, key, obj) -> Any:
        """UniqueFactory.other_keys(self, key, obj)

        File: /build/sagemath/src/sage/src/sage/structure/factory.pyx (starting at line 509)

        Sometimes during object creation, certain defaults are chosen which
        may result in a new (more specific) key. This allows the more specific
        key to be regarded as equivalent to the original key returned by
        :meth:`create_key` for the purpose of lookup in the cache, and is used
        for pickling.

        EXAMPLES:

        The ``GF`` factory used to have a custom :meth:`other_keys`
        method, but this was removed in :issue:`16934`::

            sage: # needs sage.libs.linbox sage.rings.finite_rings
            sage: key, _ = GF.create_key_and_extra_args(27, 'k'); key
            (27, ('k',), x^3 + 2*x + 1, 'givaro', 3, 3, True, None, 'poly', True, True, True)
            sage: K = GF.create_object(0, key); K
            Finite Field in k of size 3^3
            sage: GF.other_keys(key, K)
            []

            sage: K = GF(7^40, 'a')                                                     # needs sage.rings.finite_rings
            sage: loads(dumps(K)) is K                                                  # needs sage.rings.finite_rings
            True"""
    @overload
    def other_keys(self, key, K) -> Any:
        """UniqueFactory.other_keys(self, key, obj)

        File: /build/sagemath/src/sage/src/sage/structure/factory.pyx (starting at line 509)

        Sometimes during object creation, certain defaults are chosen which
        may result in a new (more specific) key. This allows the more specific
        key to be regarded as equivalent to the original key returned by
        :meth:`create_key` for the purpose of lookup in the cache, and is used
        for pickling.

        EXAMPLES:

        The ``GF`` factory used to have a custom :meth:`other_keys`
        method, but this was removed in :issue:`16934`::

            sage: # needs sage.libs.linbox sage.rings.finite_rings
            sage: key, _ = GF.create_key_and_extra_args(27, 'k'); key
            (27, ('k',), x^3 + 2*x + 1, 'givaro', 3, 3, True, None, 'poly', True, True, True)
            sage: K = GF.create_object(0, key); K
            Finite Field in k of size 3^3
            sage: GF.other_keys(key, K)
            []

            sage: K = GF(7^40, 'a')                                                     # needs sage.rings.finite_rings
            sage: loads(dumps(K)) is K                                                  # needs sage.rings.finite_rings
            True"""
    @overload
    def reduce_data(self, obj) -> Any:
        """UniqueFactory.reduce_data(self, obj)

        File: /build/sagemath/src/sage/src/sage/structure/factory.pyx (starting at line 536)

        The results of this function can be returned from
        :meth:`__reduce__`. This is here so the factory internals can
        change without having to re-write :meth:`__reduce__` methods
        that use it.

        EXAMPLES::

            sage: # needs sage.modules
            sage: from sage.modules.free_module import FreeModuleFactory_with_standard_basis as F
            sage: V = F(ZZ, 5)
            sage: factory, data = F.reduce_data(V)
            sage: factory(*data)
            Ambient free module of rank 5 over the principal ideal domain Integer Ring
            sage: factory(*data) is V
            True

            sage: from sage.structure.test_factory import test_factory
            sage: a = test_factory(1, 2)
            Making object (1, 2)
            sage: test_factory.reduce_data(a)
            (<cyfunction generic_factory_unpickle at ...>,
             (<sage.structure.test_factory.UniqueFactoryTester object at ...>,
              (...),
              (1, 2),
              {}))

        Note that the ellipsis ``(...)`` here stands for the Sage
        version."""
    @overload
    def reduce_data(self, V) -> Any:
        """UniqueFactory.reduce_data(self, obj)

        File: /build/sagemath/src/sage/src/sage/structure/factory.pyx (starting at line 536)

        The results of this function can be returned from
        :meth:`__reduce__`. This is here so the factory internals can
        change without having to re-write :meth:`__reduce__` methods
        that use it.

        EXAMPLES::

            sage: # needs sage.modules
            sage: from sage.modules.free_module import FreeModuleFactory_with_standard_basis as F
            sage: V = F(ZZ, 5)
            sage: factory, data = F.reduce_data(V)
            sage: factory(*data)
            Ambient free module of rank 5 over the principal ideal domain Integer Ring
            sage: factory(*data) is V
            True

            sage: from sage.structure.test_factory import test_factory
            sage: a = test_factory(1, 2)
            Making object (1, 2)
            sage: test_factory.reduce_data(a)
            (<cyfunction generic_factory_unpickle at ...>,
             (<sage.structure.test_factory.UniqueFactoryTester object at ...>,
              (...),
              (1, 2),
              {}))

        Note that the ellipsis ``(...)`` here stands for the Sage
        version."""
    @overload
    def reduce_data(self, a) -> Any:
        """UniqueFactory.reduce_data(self, obj)

        File: /build/sagemath/src/sage/src/sage/structure/factory.pyx (starting at line 536)

        The results of this function can be returned from
        :meth:`__reduce__`. This is here so the factory internals can
        change without having to re-write :meth:`__reduce__` methods
        that use it.

        EXAMPLES::

            sage: # needs sage.modules
            sage: from sage.modules.free_module import FreeModuleFactory_with_standard_basis as F
            sage: V = F(ZZ, 5)
            sage: factory, data = F.reduce_data(V)
            sage: factory(*data)
            Ambient free module of rank 5 over the principal ideal domain Integer Ring
            sage: factory(*data) is V
            True

            sage: from sage.structure.test_factory import test_factory
            sage: a = test_factory(1, 2)
            Making object (1, 2)
            sage: test_factory.reduce_data(a)
            (<cyfunction generic_factory_unpickle at ...>,
             (<sage.structure.test_factory.UniqueFactoryTester object at ...>,
              (...),
              (1, 2),
              {}))

        Note that the ellipsis ``(...)`` here stands for the Sage
        version."""
    def __call__(self, *args, **kwds) -> Any:
        """UniqueFactory.__call__(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/structure/factory.pyx (starting at line 341)

        This is the method invoked to create objects. It first creates a key
        from the given parameters, then if an object with that key already
        exists returns it, and otherwise creates one and stores a weak reference
        to it in its dictionary.

        Do not override this method. Instead, override ``create_key`` and
        ``create_object`` and put the docstring in the body of the class.

        EXAMPLES::

            sage: from sage.structure.test_factory import test_factory
            sage: _ = test_factory(1,2,3); _
            Making object (1, 2, 3)
            <sage.structure.test_factory.A object at ...>

        It already created one, so don't re-create::

            sage: test_factory(1,2,3)
            <sage.structure.test_factory.A object at ...>
            sage: test_factory(1,2,3) is test_factory(1,2,3)
            True

        Of course, with a different key, a new object will be created::

            sage: test_factory(1,2,3) is test_factory(1,2,4)
            Making object (1, 2, 4)
            False"""
    def __reduce__(self) -> Any:
        """UniqueFactory.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/structure/factory.pyx (starting at line 312)

        EXAMPLES::

            sage: A = FiniteField(127)
            sage: A is loads(dumps(A)) # indirect doctest
            True

            sage: # needs sage.rings.finite_rings
            sage: B = FiniteField(3^3,'b')
            sage: B is loads(dumps(B))
            True
            sage: C = FiniteField(2^16,'c')
            sage: C is loads(dumps(C))
            True
            sage: D = FiniteField(3^20,'d')
            sage: D is loads(dumps(D))
            True

        TESTS::

            sage: loads(dumps(FiniteField)) is FiniteField
            True
            sage: from sage.structure.test_factory import test_factory
            sage: loads(dumps(test_factory)) is test_factory
            True"""
