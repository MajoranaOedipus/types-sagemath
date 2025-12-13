from sage.misc.cachefunc import weak_cached_function as weak_cached_function
from sage.misc.classcall_metaclass import ClasscallMetaclass as ClasscallMetaclass
from sage.misc.inherit_comparison import InheritComparisonClasscallMetaclass as InheritComparisonClasscallMetaclass, InheritComparisonMetaclass as InheritComparisonMetaclass

def dynamic_class(name, bases, cls=None, reduction=None, doccls=None, prepend_cls_bases: bool = True, cache: bool = True):
    '''
    INPUT:

    - ``name`` -- string
    - ``bases`` -- tuple of classes
    - ``cls`` -- a class or ``None``
    - ``reduction`` -- tuple or ``None``
    - ``doccls`` -- a class or ``None``
    - ``prepend_cls_bases`` -- boolean (default: ``True``)
    - ``cache`` -- boolean or ``\'ignore_reduction\'`` (default: ``True``)

    Constructs dynamically a new class ``C`` with name ``name``, and
    bases ``bases``. If ``cls`` is provided, then its methods will be
    inserted into ``C``, and its bases will be prepended to ``bases``
    (unless ``prepend_cls_bases`` is ``False``).

    The module, documentation and source introspection is taken from
    ``doccls``, or ``cls`` if ``doccls`` is ``None``, or ``bases[0]``
    if both are ``None`` (therefore ``bases`` should be non empty if
    ``cls`` is ``None``).

    The constructed class can safely be pickled (assuming the
    arguments themselves can).

    Unless ``cache`` is ``False``, the result is cached, ensuring unique
    representation of dynamic classes.

    See :mod:`sage.structure.dynamic_class` for a discussion of the
    dynamic classes paradigm, and its relevance to Sage.

    EXAMPLES:

    To setup the stage, we create a class Foo with some methods,
    cached methods, and lazy attributes, and a class Bar::

        sage: from sage.misc.lazy_attribute import lazy_attribute
        sage: from sage.misc.cachefunc import cached_function
        sage: from sage.structure.dynamic_class import dynamic_class
        sage: class Foo():
        ....:     "The Foo class"
        ....:     def __init__(self, x):
        ....:         self._x = x
        ....:     @cached_method
        ....:     def f(self):
        ....:         return self._x^2
        ....:     def g(self):
        ....:         return self._x^2
        ....:     @lazy_attribute
        ....:     def x(self):
        ....:         return self._x
        sage: class Bar:
        ....:     def bar(self):
        ....:         return self._x^2

    We now create a class FooBar which is a copy of Foo, except that it
    also inherits from Bar::

        sage: FooBar = dynamic_class("FooBar", (Bar,), Foo)
        sage: x = FooBar(3)
        sage: x.f()
        9
        sage: x.f() is x.f()
        True
        sage: x.x
        3
        sage: x.bar()
        9
        sage: FooBar.__name__
        \'FooBar\'
        sage: FooBar.__module__
        \'__main__\'

        sage: Foo.__bases__
        (<class \'object\'>,)
        sage: FooBar.__bases__
        (<class \'__main__.Bar\'>,)
        sage: Foo.mro()
        [<class \'__main__.Foo\'>, <class \'object\'>]
        sage: FooBar.mro()
        [<class \'__main__.FooBar\'>, <class \'__main__.Bar\'>, <class \'object\'>]

    If all the base classes have a zero ``__dictoffset__``, the dynamic
    class also has a zero ``__dictoffset__``. This means that the
    instances of the class don\'t have a ``__dict__``
    (see :issue:`23435`)::

        sage: dyn = dynamic_class("dyn", (Integer,))
        sage: dyn.__dictoffset__
        0

    .. RUBRIC:: Pickling

    Dynamic classes are pickled by construction. Namely, upon
    unpickling, the class will be reconstructed by recalling
    dynamic_class with the same arguments::

        sage: type(FooBar).__reduce__(FooBar)
        (<function dynamic_class at ...>, (\'FooBar\', (<class \'__main__.Bar\'>,), <class \'__main__.Foo\'>, None, None))

    Technically, this is achieved by using a metaclass, since the
    Python pickling protocol for classes is to pickle by name::

        sage: type(FooBar)
        <class \'sage.structure.dynamic_class.DynamicMetaclass\'>

    The following (meaningless) example illustrates how to customize
    the result of the reduction::

        sage: BarFoo = dynamic_class(\'BarFoo\', (Foo,), Bar, reduction = (str, (3,)))
        sage: type(BarFoo).__reduce__(BarFoo)
        (<class \'str\'>, (3,))
        sage: loads(dumps(BarFoo))
        \'3\'

    .. RUBRIC:: Caching

    By default, the built class is cached::

         sage: dynamic_class("FooBar", (Bar,), Foo) is FooBar
         True
         sage: dynamic_class("FooBar", (Bar,), Foo, cache=True) is FooBar
         True

    and the result depends on the reduction::

        sage: dynamic_class(\'BarFoo\', (Foo,), Bar, reduction = (str, (3,))) is BarFoo
        True
        sage: dynamic_class(\'BarFoo\', (Foo,), Bar, reduction = (str, (2,))) is BarFoo
        False

    With ``cache=False``, a new class is created each time::

         sage: FooBar1 = dynamic_class("FooBar", (Bar,), Foo, cache=False); FooBar1
         <class \'__main__.FooBar\'>
         sage: FooBar2 = dynamic_class("FooBar", (Bar,), Foo, cache=False); FooBar2
         <class \'__main__.FooBar\'>
         sage: FooBar1 is FooBar
         False
         sage: FooBar2 is FooBar1
         False

    With ``cache="ignore_reduction"``, the class does not depend on
    the reduction::

        sage: BarFoo = dynamic_class(\'BarFoo\', (Foo,), Bar, reduction = (str, (3,)), cache=\'ignore_reduction\')
        sage: dynamic_class(\'BarFoo\', (Foo,), Bar, reduction = (str, (2,)), cache=\'ignore_reduction\') is BarFoo
        True

    In particular, the reduction used is that provided upon creating the
    first class::

        sage: dynamic_class(\'BarFoo\', (Foo,), Bar, reduction = (str, (2,)), cache=\'ignore_reduction\')._reduction
        (<class \'str\'>, (3,))

    .. WARNING::

        The behaviour upon creating several dynamic classes from the
        same data but with different values for ``cache`` option is
        currently left unspecified. In other words, for a given
        application, it is recommended to consistently use the same
        value for that option.

    TESTS::

        sage: import __main__
        sage: __main__.Foo = Foo
        sage: __main__.Bar = Bar
        sage: x = FooBar(3)
        sage: x.__dict__      # Breaks without the __dict__ deletion in dynamic_class_internal
        {\'_x\': 3}

        sage: type(FooBar).__reduce__(FooBar)
        (<function dynamic_class at ...>, (\'FooBar\', (<class \'__main__.Bar\'>,), <class \'__main__.Foo\'>, None, None))
        sage: import pickle
        sage: pickle.loads(pickle.dumps(FooBar)) == FooBar
        True

    We check that introspection works reasonably::

        sage: sage.misc.sageinspect.sage_getdoc(FooBar)
        \'The Foo class\\n\'

    Finally, we check that classes derived from UniqueRepresentation
    are handled gracefully (despite them also using a metaclass)::

        sage: FooUnique = dynamic_class("Foo", (Bar, UniqueRepresentation))
        sage: loads(dumps(FooUnique)) is FooUnique
        True
    '''
@weak_cached_function
def dynamic_class_internal(name, bases, cls=None, reduction=None, doccls=None, prepend_cls_bases: bool = True):
    '''
    See sage.structure.dynamic_class.dynamic_class? for indirect doctests.

    TESTS::

        sage: Foo1 = sage.structure.dynamic_class.dynamic_class_internal("Foo", (object,))
        sage: Foo2 = sage.structure.dynamic_class.dynamic_class_internal("Foo", (object,), doccls = sage.structure.dynamic_class.TestClass)
        sage: Foo3 = sage.structure.dynamic_class.dynamic_class_internal("Foo", (object,), cls    = sage.structure.dynamic_class.TestClass)
        sage: all(Foo.__name__  == \'Foo\'    for Foo in [Foo1, Foo2, Foo3])
        True
        sage: all(Foo.__bases__ == (object,) for Foo in [Foo1, Foo2, Foo3])
        True
        sage: Foo1.__module__ == object.__module__
        True
        sage: Foo2.__module__ == sage.structure.dynamic_class.TestClass.__module__
        True
        sage: Foo3.__module__ == sage.structure.dynamic_class.TestClass.__module__
        True
        sage: Foo1.__doc__ == object.__doc__
        True
        sage: Foo2.__doc__ == sage.structure.dynamic_class.TestClass.__doc__
        True
        sage: Foo3.__doc__ == sage.structure.dynamic_class.TestClass.__doc__
        True

    We check that introspection works reasonably::

        sage: from sage.misc.sageinspect import sage_getfile, sage_getsourcelines
        sage: sage_getfile(Foo2)
        \'.../sage/structure/dynamic_class.py\'
        sage: sage_getfile(Foo3)
        \'.../sage/structure/dynamic_class.py\'
        sage: sage_getsourcelines(Foo2)
        ([\'class TestClass:...\'], ...)
        sage: sage_getsourcelines(Foo3)
        ([\'class TestClass:...\'], ...)
        sage: sage_getsourcelines(Foo2())
        ([\'class TestClass:...\'], ...)
        sage: sage_getsourcelines(Foo3())
        ([\'class TestClass:...\'], ...)
        sage: sage_getsourcelines(Foo3().bla)
        ([\'    def bla():...\'], ...)

    We check that :issue:`21895` has been resolved::

        sage: C1 = sage.structure.dynamic_class.dynamic_class_internal("C1", (Morphism, UniqueRepresentation))
        sage: type(C1)
        <class \'sage.structure.dynamic_class.DynamicInheritComparisonClasscallMetaclass\'>
        sage: C2 = sage.structure.dynamic_class.dynamic_class_internal("C2", (UniqueRepresentation, Morphism))
        sage: type(C2)
        <class \'sage.structure.dynamic_class.DynamicInheritComparisonClasscallMetaclass\'>

    We check that :issue:`28392` has been resolved::

        sage: class A:
        ....:     pass
        sage: Foo1 = sage.structure.dynamic_class.dynamic_class("Foo", (), A)
        sage: "__weakref__" in Foo1.__dict__
        False
        sage: "__dict__" in Foo1.__dict__
        False
    '''

class DynamicMetaclass(type):
    """
    A metaclass implementing an appropriate reduce-by-construction method
    """
    def __reduce__(self):
        '''
        See :func:`sage.structure.dynamic_class.dynamic_class` for
        non-trivial tests.

        TESTS::

            sage: class Foo: pass
            sage: class DocClass: pass
            sage: C = sage.structure.dynamic_class.dynamic_class_internal("bla", (object,), Foo, doccls = DocClass)
            sage: type(C).__reduce__(C)
            (<function dynamic_class at ...>,
             (\'bla\', (<class \'object\'>,), <class \'__main__.Foo\'>, None, <class \'__main__.DocClass\'>))
            sage: C = sage.structure.dynamic_class.dynamic_class_internal("bla", (object,), Foo, doccls = DocClass, reduction = "blah")
            sage: type(C).__reduce__(C)
            \'blah\'
        '''

class DynamicClasscallMetaclass(DynamicMetaclass, ClasscallMetaclass): ...
class DynamicInheritComparisonMetaclass(DynamicMetaclass, InheritComparisonMetaclass): ...
class DynamicInheritComparisonClasscallMetaclass(DynamicMetaclass, InheritComparisonClasscallMetaclass): ...

class TestClass:
    """
    A class used for checking that introspection works
    """
    def bla() -> None:
        """
        bla ...
        """
