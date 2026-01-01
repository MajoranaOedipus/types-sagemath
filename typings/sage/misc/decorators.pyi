"""
Decorators

Python decorators for use in Sage.

AUTHORS:

- Tim Dumol (5 Dec 2009) -- initial version.
- Johan S. R. Nielsen (2010) -- collect decorators from various modules.
- Johan S. R. Nielsen (8 apr 2011) -- improve introspection on decorators.
- Simon King (2011-05-26) -- improve introspection of sage_wraps. Put this
  file into the reference manual.
- Julian Rueth (2014-03-19): added ``decorator_keywords`` decorator
"""
from _typeshed import Incomplete
from typing import Protocol
from collections.abc import Callable, Iterable
from sage.misc.sageinspect import sage_getargspec as sage_getargspec, sage_getsource as sage_getsource, sage_getsourcelines as sage_getsourcelines
from functools import WRAPPER_ASSIGNMENTS, WRAPPER_UPDATES, update_wrapper

class SageWrapped[**P, T](Protocol):
    def __call__(self, 
                 wrapper: Callable[P, T], 
                 assigned: Iterable[str] = WRAPPER_ASSIGNMENTS, 
                 updated: Iterable[str] = WRAPPER_UPDATES
    ) -> Callable[P, T]:
        ...


def sage_wraps[**P, ReturnT](
        wrapped: Callable[P, ReturnT], 
        assigned: Iterable[str] = WRAPPER_ASSIGNMENTS, 
        updated: Iterable[str] = WRAPPER_UPDATES
) -> SageWrapped[P, ReturnT]:
    '''
    Decorator factory which should be used in decorators for making sure that
    meta-information on the decorated callables are retained through the
    decorator, such that the introspection functions of
    ``sage.misc.sageinspect`` retrieves them correctly. This includes
    documentation string, source, and argument specification. This is an
    extension of the Python standard library decorator functools.wraps.

    That the argument specification is retained from the decorated functions
    implies, that if one uses ``sage_wraps`` in a decorator which intentionally
    changes the argument specification, one should add this information to
    the special attribute ``_sage_argspec_`` of the wrapping function (for an
    example, see e.g. ``@options`` decorator in this module).

    Note that in ``.pyx`` files which is compiled by Cython, because Sage uses
    ``binding=False`` compiler directive by default, you need to explicitly
    specify ``binding=True`` for all functions decorated with ``sage_wraps``::

        sage: import cython
        sage: def square(f):
        ....:     @sage_wraps(f)
        ....:     @cython.binding(True)
        ....:     def new_f(x):
        ....:         return f(x)*f(x)
        ....:     return new_f

    EXAMPLES:

    Demonstrate that documentation string and source are retained from the
    decorated function::

        sage: def square(f):
        ....:     @sage_wraps(f)
        ....:     def new_f(x):
        ....:         return f(x)*f(x)
        ....:     return new_f
        sage: @square
        ....: def g(x):
        ....:     "My little function"
        ....:     return x
        sage: g(2)
        4
        sage: g(x)                                                                      # needs sage.symbolic
        x^2
        sage: g.__doc__
        \'My little function\'
        sage: from sage.misc.sageinspect import sage_getsource, sage_getsourcelines, sage_getfile
        sage: sage_getsource(g)
        \'@square...def g(x)...\'

    Demonstrate that the argument description are retained from the
    decorated function through the special method (when left
    unchanged) (see :issue:`9976`)::

        sage: def diff_arg_dec(f):
        ....:     @sage_wraps(f)
        ....:     def new_f(y, some_def_arg=2):
        ....:         return f(y+some_def_arg)
        ....:     return new_f
        sage: @diff_arg_dec
        ....: def g(x):
        ....:     return x
        sage: g(1)
        3
        sage: g(1, some_def_arg=4)
        5
        sage: from sage.misc.sageinspect import sage_getargspec
        sage: sage_getargspec(g)
        FullArgSpec(args=[\'x\'], varargs=None, varkw=None, defaults=None,
                    kwonlyargs=[], kwonlydefaults=None, annotations={})

    Demonstrate that it correctly gets the source lines and the source
    file, which is essential for interactive code edition; note that we
    do not test the line numbers, as they may easily change::

        sage: P.<x,y> = QQ[]
        sage: I = P*[x,y]
        sage: sage_getfile(I.interreduced_basis)       # known bug
        \'.../sage/rings/polynomial/multi_polynomial_ideal.py\'
        sage: sage_getsourcelines(I.interreduced_basis)                                 # needs sage.libs.singular
        ([\'    @handle_AA_and_QQbar\\n\',
          \'    @singular_gb_standard_options\\n\',
          \'    @libsingular_gb_standard_options\\n\',
          \'    def interreduced_basis(self):\\n\',
          ...
          \'        return self.basis.reduced()\\n\'], ...)

    The ``f`` attribute of the decorated function refers to the
    original function::

        sage: foo = object()
        sage: @sage_wraps(foo)
        ....: def func():
        ....:     pass
        sage: wrapped = sage_wraps(foo)(func)
        sage: wrapped.f is foo
        True

    Demonstrate that sage_wraps works for non-function callables
    (:issue:`9919`)::

        sage: def square_for_met(f):
        ....:   @sage_wraps(f)
        ....:   def new_f(self, x):
        ....:       return f(self,x)*f(self,x)
        ....:   return new_f
        sage: class T:
        ....:   @square_for_met
        ....:   def g(self, x):
        ....:       "My little method"
        ....:       return x
        sage: t = T()
        sage: t.g(2)
        4
        sage: t.g.__doc__
        \'My little method\'

    The bug described in :issue:`11734` is fixed::

        sage: def square(f):
        ....:     @sage_wraps(f)
        ....:     def new_f(x):
        ....:         return f(x)*f(x)
        ....:     return new_f
        sage: f = lambda x:x^2
        sage: g = square(f)
        sage: g(3)  # this line used to fail for some people if these command were manually entered on the sage prompt
        81
    '''
    ...

class infix_operator:
    """
    A decorator for functions which allows for a hack that makes
    the function behave like an infix operator.

    This decorator exists as a convenience for interactive use.

    EXAMPLES:

    An infix dot product operator::

        sage: @infix_operator('multiply')
        ....: def dot(a, b):
        ....:     '''Dot product.'''
        ....:     return a.dot_product(b)
        sage: u = vector([1, 2, 3])                                                     # needs sage.modules
        sage: v = vector([5, 4, 3])                                                     # needs sage.modules
        sage: u *dot* v                                                                 # needs sage.modules
        22

    An infix element-wise addition operator::

        sage: # needs sage.modules
        sage: @infix_operator('add')
        ....: def eadd(a, b):
        ....:   return a.parent([i + j for i, j in zip(a, b)])
        sage: u = vector([1, 2, 3])
        sage: v = vector([5, 4, 3])
        sage: u +eadd+ v
        (6, 6, 6)
        sage: 2*u +eadd+ v
        (7, 8, 9)

    A hack to simulate a postfix operator::

        sage: @infix_operator('or')
        ....: def thendo(a, b):
        ....:     return b(a)
        sage: x |thendo| cos |thendo| (lambda x: x^2)                                   # needs sage.symbolic
        cos(x)^2
    """
    operators: Incomplete
    precedence: Incomplete
    def __init__(self, precedence) -> None:
        """
        INPUT:

        - ``precedence`` -- one of ``'add'``, ``'multiply'``, or ``'or'``
          indicating the new operator's precedence in the order of operations
        """
    def __call__(self, func):
        """Returns a function which acts as an inline operator."""

class _infix_wrapper:
    function: Incomplete
    left: Incomplete
    right: Incomplete
    def __init__(self, left=None, right=None) -> None:
        """
        Initialize the actual infix object, with possibly a specified left
        and/or right operand.
        """
    def __call__(self, *args, **kwds):
        """Call the passed function."""

def decorator_defaults(func):
    """
    This function allows a decorator to have default arguments.

    Normally, a decorator can be called with or without arguments.
    However, the two cases call for different types of return values.
    If a decorator is called with no parentheses, it should be run
    directly on the function.  However, if a decorator is called with
    parentheses (i.e., arguments), then it should return a function
    that is then in turn called with the defined function as an
    argument.

    This decorator allows us to have these default arguments without
    worrying about the return type.

    EXAMPLES::

        sage: from sage.misc.decorators import decorator_defaults
        sage: @decorator_defaults
        ....: def my_decorator(f, *args, **kwds):
        ....:   print(kwds)
        ....:   print(args)
        ....:   print(f.__name__)

        sage: @my_decorator
        ....: def my_fun(a, b):
        ....:   return a,b
        {}
        ()
        my_fun
        sage: @my_decorator(3,4,c=1,d=2)
        ....: def my_fun(a, b):
        ....:   return a,b
        {'c': 1, 'd': 2}
        (3, 4)
        my_fun
    """

class suboptions:
    name: Incomplete
    options: Incomplete
    def __init__(self, name, **options) -> None:
        """
        A decorator for functions which collects all keywords
        starting with ``name+'_'`` and collects them into a dictionary
        which will be passed on to the wrapped function as a
        dictionary called ``name_options``.

        The keyword arguments passed into the constructor are taken
        to be default for the ``name_options`` dictionary.

        EXAMPLES::

            sage: from sage.misc.decorators import suboptions
            sage: s = suboptions('arrow', size=2)
            sage: s.name
            'arrow_'
            sage: s.options
            {'size': 2}
        """
    def __call__(self, func):
        """
        Return a wrapper around ``func``.

        EXAMPLES::

            sage: from sage.misc.decorators import suboptions
            sage: def f(*args, **kwds): print(sorted(kwds.items()))
            sage: f = suboptions('arrow', size=2)(f)
            sage: f(size=2)
            [('arrow_options', {'size': 2}), ('size', 2)]
            sage: f(arrow_size=3)
            [('arrow_options', {'size': 3})]
            sage: f(arrow_options={'size':4})
            [('arrow_options', {'size': 4})]
            sage: f(arrow_options={'size':4}, arrow_size=5)
            [('arrow_options', {'size': 5})]

         Demonstrate that the introspected argument specification of the
         wrapped function is updated (see :issue:`9976`)::

            sage: from sage.misc.sageinspect import sage_getargspec
            sage: sage_getargspec(f)
            FullArgSpec(args=['arrow_size'], varargs='args', varkw='kwds', defaults=(2,),
                        kwonlyargs=[], kwonlydefaults=None, annotations={})
        """

class options:
    options: Incomplete
    original_opts: Incomplete
    def __init__(self, **options) -> None:
        '''
        A decorator for functions which allows for default options to be
        set and reset by the end user.  Additionally, if one needs to, one
        can get at the original keyword arguments passed into the
        decorator.

        TESTS::

            sage: from sage.misc.decorators import options
            sage: o = options(rgbcolor=(0,0,1))
            sage: o.options
            {\'rgbcolor\': (0, 0, 1)}
            sage: o = options(rgbcolor=(0,0,1), __original_opts=True)
            sage: o.original_opts
            True
            sage: loads(dumps(o)).options
            {\'rgbcolor\': (0, 0, 1)}

        Demonstrate that the introspected argument specification of the wrapped
        function is updated (see :issue:`9976`)::

            sage: from sage.misc.decorators import options
            sage: o = options(rgbcolor=(0,0,1))
            sage: def f(*args, **kwds):
            ....:     print("{} {}".format(args, sorted(kwds.items())))
            sage: f1 = o(f)
            sage: from sage.misc.sageinspect import sage_getargspec
            sage: sage_getargspec(f1)
            FullArgSpec(args=[\'rgbcolor\'], varargs=\'args\', varkw=\'kwds\', defaults=((0, 0, 1),),
                        kwonlyargs=[], kwonlydefaults=None, annotations={})
        '''
    def __call__(self, func):
        '''
        EXAMPLES::

            sage: from sage.misc.decorators import options
            sage: o = options(rgbcolor=(0,0,1))
            sage: def f(*args, **kwds):
            ....:     print("{} {}".format(args, sorted(kwds.items())))
            sage: f1 = o(f)
            sage: f1()
            () [(\'rgbcolor\', (0, 0, 1))]
            sage: f1(rgbcolor=1)
            () [(\'rgbcolor\', 1)]
            sage: o = options(rgbcolor=(0,0,1), __original_opts=True)
            sage: f2 = o(f)
            sage: f2(alpha=1)
            () [(\'__original_opts\', {\'alpha\': 1}), (\'alpha\', 1), (\'rgbcolor\', (0, 0, 1))]
        '''

class rename_keyword:
    renames: Incomplete
    deprecation: Incomplete
    def __init__(self, deprecated=None, deprecation=None, **renames) -> None:
        """
        A decorator which renames keyword arguments and optionally
        deprecates the new keyword.

        INPUT:

        - ``deprecation`` -- integer; the github issue number where the
          deprecation was introduced

        - the rest of the arguments is a list of keyword arguments in the
          form ``renamed_option='existing_option'``.  This will have the
          effect of renaming ``renamed_option`` so that the function only
          sees ``existing_option``.  If both ``renamed_option`` and
          ``existing_option`` are passed to the function, ``existing_option``
          will override the ``renamed_option`` value.

        EXAMPLES::

            sage: from sage.misc.decorators import rename_keyword
            sage: r = rename_keyword(color='rgbcolor')
            sage: r.renames
            {'color': 'rgbcolor'}
            sage: loads(dumps(r)).renames
            {'color': 'rgbcolor'}

        To deprecate an old keyword::

            sage: r = rename_keyword(deprecation=13109, color='rgbcolor')
        """
    def __call__(self, func):
        '''
        Rename keywords.

        EXAMPLES::

            sage: from sage.misc.decorators import rename_keyword
            sage: r = rename_keyword(color=\'rgbcolor\')
            sage: def f(*args, **kwds):
            ....:     print("{} {}".format(args, kwds))
            sage: f = r(f)
            sage: f()
            () {}
            sage: f(alpha=1)
            () {\'alpha\': 1}
            sage: f(rgbcolor=1)
            () {\'rgbcolor\': 1}
            sage: f(color=1)
            () {\'rgbcolor\': 1}

        We can also deprecate the renamed keyword::

            sage: r = rename_keyword(deprecation=13109, deprecated_option=\'new_option\')
            sage: def f(*args, **kwds):
            ....:     print("{} {}".format(args, kwds))
            sage: f = r(f)
            sage: f()
            () {}
            sage: f(alpha=1)
            () {\'alpha\': 1}
            sage: f(new_option=1)
            () {\'new_option\': 1}
            sage: f(deprecated_option=1)
            doctest:...: DeprecationWarning: use the option \'new_option\' instead of \'deprecated_option\'
            See https://github.com/sagemath/sage/issues/13109 for details.
            () {\'new_option\': 1}
        '''

class specialize:
    '''
    A decorator generator that returns a decorator that in turn
    returns a specialized function for function ``f``. In other words,
    it returns a function that acts like ``f`` with arguments
    ``*args`` and ``**kwargs`` supplied.

    INPUT:

    - ``*args``, ``**kwargs`` -- arguments to specialize the function for

    OUTPUT: a decorator that accepts a function ``f`` and specializes it
    with ``*args`` and ``**kwargs``

    EXAMPLES::

        sage: f = specialize(5)(lambda x, y: x+y)
        sage: f(10)
        15
        sage: f(5)
        10
        sage: @specialize("Bon Voyage")
        ....: def greet(greeting, name):
        ....:     print("{0}, {1}!".format(greeting, name))
        sage: greet("Monsieur Jean Valjean")
        Bon Voyage, Monsieur Jean Valjean!
        sage: greet(name = \'Javert\')
        Bon Voyage, Javert!
    '''
    args: Incomplete
    kwargs: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def __call__(self, f): ...

def decorator_keywords[**P, T](
        func: Callable[P, T]
) -> SageWrapped[P, T]:
    """
    A decorator for decorators with optional keyword arguments.

    EXAMPLES::

        sage: from sage.misc.decorators import decorator_keywords
        sage: @decorator_keywords
        ....: def preprocess(f=None, processor=None):
        ....:     def wrapper(*args, **kwargs):
        ....:         if processor is not None:
        ....:             args, kwargs = processor(*args, **kwargs)
        ....:         return f(*args, **kwargs)
        ....:     return wrapper

    This decorator can be called with and without arguments::

        sage: @preprocess
        ....: def foo(x): return x
        sage: foo(None)
        sage: foo(1)
        1

        sage: def normalize(x): return ((0,),{}) if x is None else ((x,),{})
        sage: @preprocess(processor=normalize)
        ....: def foo(x): return x
        sage: foo(None)
        0
        sage: foo(1)
        1
    """
