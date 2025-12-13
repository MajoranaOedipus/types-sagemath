from sage.misc.cachefunc import weak_cached_function as weak_cached_function
from sage.misc.classcall_metaclass import ClasscallMetaclass as ClasscallMetaclass, typecall as typecall
from sage.misc.fast_methods import WithEqualityById as WithEqualityById

class WithPicklingByInitArgs(metaclass=ClasscallMetaclass):
    """
    Classes derived from :class:`WithPicklingByInitArgs` store the arguments
    passed to :meth:`__init__` to implement pickling.

    This class is for objects that are semantically immutable and determined
    by the class and the arguments passed to :meth:`__init__`.
    The class also provides implementations of :meth:`__copy__` and
    :func:`__deepcopy__`, which simply return the object.
    """
    @staticmethod
    def __classcall__(cls, *args, **options):
        """
        Construct a new object of this class and store the arguments passed to ``__init__``.

        TESTS::

            sage: from sage.structure.unique_representation import WithPicklingByInitArgs
            sage: class MyClass(WithPicklingByInitArgs):
            ....:     def __init__(self, value):
            ....:         self.value = value
            ....:     def __eq__(self, other):
            ....:         if type(self) != type(other):
            ....:             return False
            ....:         return self.value == other.value
            sage: import __main__
            sage: __main__.MyClass = MyClass  # This is only needed in doctests
            sage: x = MyClass(1)
            sage: x == loads(dumps(x))
            True
            sage: y = MyClass(1)
            sage: x is y                # No Cached/UniqueRepresentation behavior
            False
        """
    def __reduce__(self):
        """
        Return the arguments that have been passed to
        :meth:`__new__<object.__new__>` to construct this object,
        as per the pickle protocol.

        See also :class:`CachedRepresentation` and
        :class:`UniqueRepresentation` for a discussion.

        EXAMPLES::

            sage: x = UniqueRepresentation()
            sage: x.__reduce__()          # indirect doctest
            (<function unreduce at ...>, (<class 'sage.structure.unique_representation.UniqueRepresentation'>, (), {}))
        """
    def __copy__(self):
        """
        Return ``self``, as a semantic copy of ``self``.

        This assumes that the object is semantically immutable.

        EXAMPLES::

            sage: x = UniqueRepresentation()
            sage: x is copy(x)    # indirect doctest
            True
        """
    def __deepcopy__(self, memo):
        """
        Return ``self``, as a semantic deep copy of ``self``.

        This assumes that the object is semantically immutable.

        EXAMPLES::

            sage: from copy import deepcopy
            sage: x = UniqueRepresentation()
            sage: x is deepcopy(x)      # indirect doctest
            True
        """

def unreduce(cls, args, keywords):
    """
    Calls a class on the given arguments::

        sage: sage.structure.unique_representation.unreduce(Integer, (1,), {})
        1

    .. TODO::

        should reuse something preexisting ...

    """

class CachedRepresentation(WithPicklingByInitArgs):
    '''
    Classes derived from CachedRepresentation inherit a weak cache for their
    instances.

    .. NOTE::

        If this class is used as a base class, then instances are (weakly)
        cached, according to the arguments used to create the instance.
        Pickling is provided, of course by using the cache.

    .. NOTE::

        Using this class, one can have arbitrary hash and comparison.
        Hence, *unique* representation behaviour is *not* provided.

    .. SEEALSO::

        :class:`UniqueRepresentation`, :mod:`~sage.structure.unique_representation`

    EXAMPLES:

    Providing a class with a weak cache for the instances is easy: Just
    inherit from :class:`CachedRepresentation`::

        sage: from sage.structure.unique_representation import CachedRepresentation
        sage: class MyClass(CachedRepresentation):
        ....:     # all the rest as usual
        ....:     pass

    We start with a simple class whose constructor takes a single
    value as argument (TODO: find a more meaningful example)::

        sage: class MyClass(CachedRepresentation):
        ....:     def __init__(self, value):
        ....:         self.value = value
        ....:     def __eq__(self, other):
        ....:         if type(self) != type(other):
        ....:             return False
        ....:         return self.value == other.value

    Two coexisting instances of ``MyClass`` created with the same argument data
    are guaranteed to share the same identity. Since :issue:`12215`, this is
    only the case if there is some strong reference to the returned instance,
    since otherwise it may be garbage collected::

        sage: x = MyClass(1)
        sage: y = MyClass(1)
        sage: x is y               # There is a strong reference
        True
        sage: z = MyClass(2)
        sage: x is z
        False

    In particular, modifying any one of them modifies the other
    (reference effect)::

        sage: x.value = 3
        sage: x.value, y.value
        (3, 3)
        sage: y.value = 1
        sage: x.value, y.value
        (1, 1)

    The arguments can consist of any combination of positional or keyword
    arguments, as taken by a usual :meth:`__init__ <object.__init__>`
    function. However, all values passed in should be hashable::

        sage: MyClass(value = [1,2,3])
        Traceback (most recent call last):
        ...
        TypeError: unhashable type: \'list\'

    .. rubric:: Argument preprocessing

    Sometimes, one wants to do some preprocessing on the arguments, to
    put them in some canonical form. The following example illustrates
    how to achieve this; it takes as argument any iterable, and
    canonicalizes it into a tuple (which is hashable!)::

        sage: class MyClass2(CachedRepresentation):
        ....:     @staticmethod
        ....:     def __classcall__(cls, iterable):
        ....:         t = tuple(iterable)
        ....:         return super().__classcall__(cls, t)
        ....:
        ....:     def __init__(self, value):
        ....:         self.value = value
        sage: x = MyClass2([1,2,3])
        sage: y = MyClass2(tuple([1,2,3]))
        sage: z = MyClass2(i for i in [1,2,3])
        sage: x.value
        (1, 2, 3)
        sage: x is y, y is z
        (True, True)

    A similar situation arises when the constructor accepts default
    values for some of its parameters. Alas, the obvious
    implementation does not work::

        sage: class MyClass3(CachedRepresentation):
        ....:     def __init__(self, value=3):
        ....:         self.value = value
        sage: MyClass3(3) is MyClass3()
        False

    Instead, one should do::

        sage: class MyClass3(UniqueRepresentation):
        ....:     @staticmethod
        ....:     def __classcall__(cls, value=3):
        ....:         return super().__classcall__(cls, value)
        ....:
        ....:     def __init__(self, value):
        ....:         self.value = value
        sage: MyClass3(3) is MyClass3()
        True

    A bit of explanation is in order. First, the call ``MyClass2([1,2,3])``
    triggers a call to ``MyClass2.__classcall__(MyClass2, [1,2,3])``. This is
    an extension of the standard Python behavior, needed by
    :class:`CachedRepresentation`, and implemented by the
    :class:`~sage.misc.classcall_metaclass.ClasscallMetaclass`. Then,
    ``MyClass2.__classcall__`` does the desired transformations on the
    arguments. Finally, it uses ``super`` to call the default implementation
    of ``__classcall__`` provided by :class:`CachedRepresentation`. This one
    in turn handles the caching and, if needed, constructs and initializes a
    new object in the class using :meth:`__new__<object.__new__>` and
    :meth:`__init__<object.__init__>` as usual.

    Constraints:

    - :meth:`__classcall__` is a staticmethod (like, implicitly,
      :meth:`__new__<object.__new__>`)
    - the preprocessing on the arguments should be idempotent. That is, if
      ``MyClass2.__classcall__(<arguments>)`` calls
      ``CachedRepresentation.__classcall__(<preprocessed_arguments>)``, then
      ``MyClass2.__classcall__(<preprocessed_arguments>)`` should also result
      in a call to ``CachedRepresentation.__classcall__(<preprocessed_arguments>)``.
    - ``MyClass2.__classcall__`` should return the result of
      :meth:`CachedRepresentation.__classcall__` without modifying it.

    Other than that ``MyClass2.__classcall__`` may play any tricks, like
    acting as a factory and returning objects from other classes.

    .. WARNING::

        It is possible, but strongly discouraged, to let the ``__classcall__``
        method of a class ``C`` return objects that are not instances of
        ``C``. Of course, instances of a *subclass* of ``C`` are fine. Compare
        the examples in :mod:`~sage.structure.unique_representation`.

    We illustrate what is meant by an "idempotent" preprocessing. Imagine
    that one has instances that are created with an integer-valued argument,
    but only depend on the *square* of the argument. It would be a mistake to
    square the given argument during preprocessing::

        sage: class WrongUsage(CachedRepresentation):
        ....:     @staticmethod
        ....:     def __classcall__(cls, n):
        ....:         return super().__classcall__(cls, n^2)
        ....:     def __init__(self, n):
        ....:         self.n = n
        ....:     def __repr__(self):
        ....:         return "Something(%d)"%self.n
        sage: import __main__
        sage: __main__.WrongUsage = WrongUsage # This is only needed in doctests
        sage: w = WrongUsage(3); w
        Something(9)
        sage: w._reduction
        (<class \'__main__.WrongUsage\'>, (9,), {})

    Indeed, the reduction data are obtained from the preprocessed
    arguments. By consequence, if the resulting instance is pickled and
    unpickled, the argument gets squared *again*::

        sage: loads(dumps(w))
        Something(81)

    Instead, the preprocessing should only take the absolute value of the
    given argument, while the squaring should happen inside of the
    ``__init__`` method, where it won\'t mess with the cache::

        sage: class BetterUsage(CachedRepresentation):
        ....:     @staticmethod
        ....:     def __classcall__(cls, n):
        ....:         return super().__classcall__(cls, abs(n))
        ....:     def __init__(self, n):
        ....:         self.n = n^2
        ....:     def __repr__(self):
        ....:         return "SomethingElse(%d)"%self.n
        sage: __main__.BetterUsage = BetterUsage # This is only needed in doctests
        sage: b = BetterUsage(3); b
        SomethingElse(9)
        sage: loads(dumps(b)) is b
        True
        sage: b is BetterUsage(-3)
        True

    .. rubric:: Cached representation and mutability

    :class:`CachedRepresentation` is primarily intended for implementing
    objects which are (at least semantically) immutable. This is in
    particular assumed by the default implementations of ``copy`` and
    ``deepcopy``::

        sage: copy(x) is x
        True
        sage: from copy import deepcopy
        sage: deepcopy(x) is x
        True

    However, in contrast to :class:`UniqueRepresentation`, using
    :class:`CachedRepresentation` allows for a comparison that is not by
    identity::

        sage: t = MyClass(3)
        sage: z = MyClass(2)
        sage: t.value = 2

    Now ``t`` and ``z`` are non-identical, but equal::

        sage: t.value == z.value
        True
        sage: t == z
        True
        sage: t is z
        False

    .. rubric:: More on cached representation and identity

    :class:`CachedRepresentation` is implemented by means of a cache.
    This cache uses weak references in general, but strong references to
    the most recently created objects. Hence, when all other references
    to, say, ``MyClass(1)`` have been deleted, the instance is
    eventually deleted from memory (after enough other objects have been
    created to remove the strong reference to ``MyClass(1)``). A later
    call to ``MyClass(1)`` reconstructs the instance from scratch::

        sage: class SomeClass(UniqueRepresentation):
        ....:     def __init__(self, i):
        ....:         print("creating new instance for argument %s" % i)
        ....:         self.i = i
        ....:     def __del__(self):
        ....:         print("deleting instance for argument %s" % self.i)
        sage: class OtherClass(UniqueRepresentation):
        ....:     def __init__(self, i):
        ....:         pass
        sage: O = SomeClass(1)
        creating new instance for argument 1
        sage: O is SomeClass(1)
        True
        sage: O is SomeClass(2)
        creating new instance for argument 2
        False
        sage: L = [OtherClass(i) for i in range(200)]
        deleting instance for argument 2
        sage: del O
        deleting instance for argument 1
        sage: O = SomeClass(1)
        creating new instance for argument 1
        sage: del O
        sage: del L
        sage: L = [OtherClass(i) for i in range(200)]
        deleting instance for argument 1

    .. rubric:: Cached representation and pickling

    The default Python pickling implementation (by reconstructing an object
    from its class and dictionary, see "The pickle protocol" in the Python
    Library Reference) does not preserve cached representation, as Python has
    no chance to know whether and where the same object already exists.

    :class:`CachedRepresentation` tries to ensure appropriate pickling by
    implementing a :meth:`__reduce__ <object.__reduce__>` method returning the
    arguments passed to the constructor::

        sage: import __main__             # Fake MyClass being defined in a python module
        sage: __main__.MyClass = MyClass
        sage: x = MyClass(1)
        sage: loads(dumps(x)) is x
        True

    :class:`CachedRepresentation` uses the :meth:`__reduce__
    <object.__reduce__>` pickle protocol rather than :meth:`__getnewargs__
    <object.__getnewargs__>` because the latter does not handle keyword
    arguments::

        sage: x = MyClass(value = 1)
        sage: x.__reduce__()
        (<function unreduce at ...>, (<class \'__main__.MyClass\'>, (), {\'value\': 1}))
        sage: x is loads(dumps(x))
        True

    .. NOTE::

        The default implementation of :meth:`__reduce__ <object.__reduce__>`
        in :class:`CachedRepresentation` requires to store the constructor\'s
        arguments in the instance dictionary upon construction::

            sage: x.__dict__
            {\'_reduction\': (<class \'__main__.MyClass\'>, (), {\'value\': 1}), \'value\': 1}

        It is often easy in a derived subclass to reconstruct the constructor\'s
        arguments from the instance data structure. When this is the case,
        :meth:`__reduce__ <object.__reduce__>` should be overridden; automagically
        the arguments won\'t be stored anymore::

            sage: class MyClass3(UniqueRepresentation):
            ....:     def __init__(self, value):
            ....:         self.value = value
            ....:
            ....:     def __reduce__(self):
            ....:         return (MyClass3, (self.value,))
            sage: import __main__; __main__.MyClass3 = MyClass3  # Fake MyClass3 being defined in a python module
            sage: x = MyClass3(1)
            sage: loads(dumps(x)) is x
            True
            sage: x.__dict__
            {\'value\': 1}

    .. rubric:: Migrating classes to ``CachedRepresentation`` and unpickling

    We check that, when migrating a class to :class:`CachedRepresentation`,
    older pickles can still be reasonably unpickled. Let us create a
    (new style) class, and pickle one of its instances::

        sage: class MyClass4():
        ....:     def __init__(self, value):
        ....:         self.value = value
        sage: import __main__; __main__.MyClass4 = MyClass4  # Fake MyClass4 being defined in a python module
        sage: pickle = dumps(MyClass4(1))

    It can be unpickled::

        sage: y = loads(pickle)
        sage: y.value
        1

    Now, we upgrade the class to derive from :class:`UniqueRepresentation`,
    which inherits from :class:`CachedRepresentation`::

        sage: class MyClass4(UniqueRepresentation, object):
        ....:     def __init__(self, value):
        ....:         self.value = value
        sage: import __main__; __main__.MyClass4 = MyClass4  # Fake MyClass4 being defined in a python module
        sage: __main__.MyClass4 = MyClass4

    The pickle can still be unpickled::

        sage: y = loads(pickle)
        sage: y.value
        1

    Note however that, for the reasons explained above, unique
    representation is not guaranteed in this case::

        sage: y is MyClass4(1)
        False

    .. TODO::

        Illustrate how this can be fixed on a case by case basis.

    Now, we redo the same test for a class deriving from SageObject::

        sage: class MyClass4(SageObject):
        ....:     def __init__(self, value):
        ....:         self.value = value
        sage: import __main__; __main__.MyClass4 = MyClass4  # Fake MyClass4 being defined in a python module
        sage: pickle = dumps(MyClass4(1))

        sage: class MyClass4(UniqueRepresentation, SageObject):
        ....:     def __init__(self, value):
        ....:         self.value = value
        sage: __main__.MyClass4 = MyClass4
        sage: y = loads(pickle)
        sage: y.value
        1

    Caveat: unpickling instances of a formerly old-style class is not supported yet by default::

        sage: class MyClass4:
        ....:     def __init__(self, value):
        ....:         self.value = value
        sage: import __main__; __main__.MyClass4 = MyClass4  # Fake MyClass4 being defined in a python module
        sage: pickle = dumps(MyClass4(1))

        sage: class MyClass4(UniqueRepresentation, SageObject):
        ....:     def __init__(self, value):
        ....:         self.value = value
        sage: __main__.MyClass4 = MyClass4
        sage: y = loads(pickle)  # todo: not implemented
        sage: y.value            # todo: not implemented
        1

    .. rubric:: Rationale for the current implementation

    :class:`CachedRepresentation` and derived classes use the
    :class:`~sage.misc.classcall_metaclass.ClasscallMetaclass`
    of the standard Python type. The following example explains why.

    We define a variant of ``MyClass`` where the calls to
    :meth:`__init__<object.__init__>` are traced::

        sage: class MyClass(CachedRepresentation):
        ....:     def __init__(self, value):
        ....:         print("initializing object")
        ....:         self.value = value

    Let us create an object twice::

        sage: x = MyClass(1)
        initializing object
        sage: z = MyClass(1)

    As desired the :meth:`__init__<object.__init__>` method was only called
    the first time, which is an important feature.

    As far as we can tell, this is not achievable while just using
    :meth:`__new__<object.__new__>` and :meth:`__init__<object.__init__>` (as
    defined by type; see Section :python:`Basic Customization
    <reference/datamodel.html#basic-customization>` in the Python Reference
    Manual). Indeed, :meth:`__init__<object.__init__>` is called
    systematically on the result of :meth:`__new__<object.__new__>` whenever
    the result is an instance of the class.

    Another difficulty is that argument preprocessing (as in the example
    above) cannot be handled by :meth:`__new__<object.__new__>`, since the
    unprocessed arguments will be passed down to
    :meth:`__init__<object.__init__>`.
    '''
    def __classcall__(cls, *args, **options):
        """
        Construct a new object of this class or reuse an existing one.

        See also :class:`CachedRepresentation` and
        :class:`UniqueRepresentation` for a discussion.

        EXAMPLES::

            sage: x = UniqueRepresentation()
            sage: y = UniqueRepresentation()
            sage: x is y   # indirect doctest
            True
        """

class UniqueRepresentation(WithEqualityById, CachedRepresentation):
    """
    Classes derived from ``UniqueRepresentation`` inherit a unique
    representation behavior for their instances.

    .. SEEALSO::

        :mod:`~sage.structure.unique_representation`

    EXAMPLES:

    The short story: to construct a class whose instances have a
    unique representation behavior one just has to do::

        sage: class MyClass(UniqueRepresentation):
        ....:     # all the rest as usual
        ....:     pass

    Everything below is for the curious or for advanced usage.

    .. rubric:: What is unique representation?

    Instances of a class have a *unique representation behavior* when
    instances evaluate equal if and only if they are identical (i.e., share
    the same memory representation), if and only if they were created using
    equal arguments. For example, calling twice::

        sage: f = SymmetricFunctions(QQ)                                                # needs sage.combinat sage.modules
        sage: g = SymmetricFunctions(QQ)                                                # needs sage.combinat sage.modules

    to create the symmetric function algebra over `\\QQ` actually gives back the
    same object::

        sage: f == g                                                                    # needs sage.combinat sage.modules
        True
        sage: f is g                                                                    # needs sage.combinat sage.modules
        True

    This is a standard design pattern. It allows for sharing cached data (say
    representation theoretical information about a group) as well as for very
    fast hashing and equality testing. This behaviour is typically desirable
    for parents and categories. It can also be useful for intensive
    computations where one wants to cache all the operations on a small set of
    elements (say the multiplication table of a small group), and access this
    cache as quickly as possible.

    :class:`UniqueRepresentation` is very easy to use: a class just needs to
    derive from it, or make sure some of its super classes does. Also, it
    groups together the class and the factory in a single gadget::

        sage: isinstance(SymmetricFunctions(CC), SymmetricFunctions)                    # needs sage.combinat sage.modules
        True
        sage: issubclass(SymmetricFunctions, UniqueRepresentation)                      # needs sage.combinat sage.modules
        True

    This nice behaviour is not available when one just uses a factory::

        sage: isinstance(GF(7), GF)
        Traceback (most recent call last):
        ...
        TypeError: isinstance() arg 2 must be a type...

        sage: isinstance(GF, sage.structure.factory.UniqueFactory)
        True

    In addition, :class:`~sage.structure.factory.UniqueFactory` only provides
    the *cached* representation behaviour, but not the *unique* representation
    behaviour---the examples in :mod:`~sage.structure.unique_representation`
    explain this difference.

    On the other hand, the :class:`UniqueRepresentation` class is more
    intrusive, as it imposes a behavior (and a metaclass) on all the
    subclasses. In particular, the unique representation behaviour is imposed
    on *all* subclasses (unless the ``__classcall__`` method is overloaded and
    not called in the subclass, which is not recommended). Its implementation
    is also more technical, which leads to some subtleties.

    EXAMPLES:

    We start with a simple class whose constructor takes a single value as
    argument. This pattern is similar to what is done in
    :class:`sage.combinat.sf.sf.SymmetricFunctions`::

        sage: class MyClass(UniqueRepresentation):
        ....:     def __init__(self, value):
        ....:         self.value = value

    Two coexisting instances of ``MyClass`` created with the same argument
    data are guaranteed to share the same identity. Since :issue:`12215`, this
    is only the case if there is some strong reference to the returned
    instance, since otherwise it may be garbage collected::

        sage: x = MyClass(1)
        sage: y = MyClass(1)
        sage: x is y               # There is a strong reference
        True
        sage: z = MyClass(2)
        sage: x is z
        False

    In particular, modifying any one of them modifies the other
    (reference effect)::

        sage: x.value = 3
        sage: x.value, y.value
        (3, 3)
        sage: y.value = 1
        sage: x.value, y.value
        (1, 1)

    When comparing two instances of a unique representation with ``==``
    or ``!=`` comparison by identity is used::

        sage: x == y
        True
        sage: x is y
        True
        sage: z = MyClass(2)
        sage: x == z
        False
        sage: x is z
        False
        sage: x != y
        False
        sage: x != z
        True

    A hash function equivalent to :meth:`object.__hash__` is used, which is
    compatible with comparison by identity. However this means that the hash
    function may change in between Sage sessions, or even within the same Sage
    session.
    ::

        sage: hash(x) == object.__hash__(x)
        True

    .. WARNING::

        It is possible to inherit from
        :class:`~sage.structure.unique_representation.UniqueRepresentation`
        and then overload comparison in a way that destroys the unique
        representation property. We strongly recommend against it!  You should
        use :class:`~sage.structure.unique_representation.CachedRepresentation`
        instead.

    .. rubric:: Mixing super types and super classes

    TESTS:

    For the record, this test did fail with previous implementation
    attempts::

        sage: class bla(UniqueRepresentation, SageObject):
        ....:     pass
        sage: b = bla()
    """
