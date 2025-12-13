from _typeshed import Incomplete

def abstract_method(f=None, optional: bool = False):
    '''
    Abstract methods.

    INPUT:

    - ``f`` -- a function
    - ``optional`` -- boolean (default: ``False``)

    The decorator :obj:`abstract_method` can be used to declare
    methods that should be implemented by all concrete derived
    classes. This declaration should typically include documentation
    for the specification for this method.

    The purpose is to enforce a consistent and visual syntax for such
    declarations. It is used by the Sage categories for automated
    tests (see ``Sets.Parent.test_not_implemented``).

    EXAMPLES:

    We create a class with an abstract method::

        sage: class A():
        ....:
        ....:     @abstract_method
        ....:     def my_method(self):
        ....:         \'\'\'
        ....:         The method :meth:`my_method` computes my_method
        ....:
        ....:         EXAMPLES::
        ....:
        ....:         \'\'\'
        ....:         pass

        sage: A.my_method
        <abstract method my_method at ...>

    The current policy is that a :exc:`NotImplementedError` is raised
    when accessing the method through an instance, even before the
    method is called::

        sage: x = A()
        sage: x.my_method
        Traceback (most recent call last):
        ...
        NotImplementedError: <abstract method my_method at ...>

    It is also possible to mark abstract methods as optional::

        sage: class A():
        ....:
        ....:     @abstract_method(optional = True)
        ....:     def my_method(self):
        ....:         \'\'\'
        ....:         The method :meth:`my_method` computes my_method
        ....:
        ....:         EXAMPLES::
        ....:
        ....:         \'\'\'
        ....:         pass

        sage: A.my_method
        <optional abstract method my_method at ...>

        sage: x = A()
        sage: x.my_method
        NotImplemented

    The official mantra for testing whether an optional abstract
    method is implemented is::

        sage: if x.my_method is not NotImplemented:
        ....:     x.my_method()
        ....: else:
        ....:     print("x.my_method is not available.")
        x.my_method is not available.

    .. rubric:: Discussion

    The policy details are not yet fixed. The purpose of this first
    implementation is to let developers experiment with it and give
    feedback on what\'s most practical.

    The advantage of the current policy is that attempts at using a
    non implemented methods are caught as early as possible. On the
    other hand, one cannot use introspection directly to fetch the
    documentation::

        sage: x.my_method?      # todo: not implemented

    Instead one needs to do::

        sage: A._my_method?     # todo: not implemented

    This could probably be fixed in :mod:`sage.misc.sageinspect`.

    .. TODO:: what should be the recommended mantra for existence testing from the class?

    .. TODO::

        should extra information appear in the output? The name of the
        class? That of the super class where the abstract method is
        defined?

    .. TODO:: look for similar decorators on the web, and merge

    .. rubric:: Implementation details

    Technically, an abstract_method is a non-data descriptor (see
    Invoking Descriptors in the Python reference manual).

    The syntax ``@abstract_method`` w.r.t. @abstract_method(optional = True)
    is achieved by a little trick which we test here::

        sage: abstract_method(optional = True)
        <function abstract_method.<locals>.<lambda> at ...>
        sage: abstract_method(optional = True)(version)
        <optional abstract method version at ...>
        sage: abstract_method(version, optional = True)
        <optional abstract method version at ...>
    '''

class AbstractMethod:
    __doc__: Incomplete
    __module__: Incomplete
    def __init__(self, f, optional: bool = False) -> None:
        '''
        Constructor for abstract methods.

        EXAMPLES::

            sage: def f(x):
            ....:     "doc of f"
            ....:     return 1
            sage: x = abstract_method(f); x
            <abstract method f at ...>
            sage: x.__doc__
            \'doc of f\'
            sage: x.__name__
            \'f\'
            sage: x.__module__
            \'__main__\'
        '''
    def __get__(self, instance, cls):
        """
        Implement the attribute access protocol.

        EXAMPLES::

            sage: class A: pass
            sage: def f(x): return 1
            sage: f = abstract_method(f)
            sage: f.__get__(A(), A)
            Traceback (most recent call last):
            ...
            NotImplementedError: <abstract method f at ...>
        """
    def is_optional(self):
        """
        Return whether an abstract method is optional or not.

        EXAMPLES::

            sage: class AbstractClass:
            ....:     @abstract_method
            ....:     def required(): pass
            ....:
            ....:     @abstract_method(optional = True)
            ....:     def optional(): pass
            sage: AbstractClass.required.is_optional()
            False
            sage: AbstractClass.optional.is_optional()
            True
        """

def abstract_methods_of_class(cls):
    """
    Return the required and optional abstract methods of the class.

    EXAMPLES::

        sage: class AbstractClass:
        ....:     @abstract_method
        ....:     def required1(): pass
        ....:
        ....:     @abstract_method(optional = True)
        ....:     def optional2(): pass
        ....:
        ....:     @abstract_method(optional = True)
        ....:     def optional1(): pass
        ....:
        ....:     @abstract_method
        ....:     def required2(): pass

        sage: sage.misc.abstract_method.abstract_methods_of_class(AbstractClass)
        {'optional': ['optional1', 'optional2'],
         'required': ['required1', 'required2']}
    """
