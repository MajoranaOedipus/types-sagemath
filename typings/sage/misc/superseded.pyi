from _typeshed import Incomplete
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute

def deprecation(issue_number, message, stacklevel: int = 4) -> None:
    """
    Issue a deprecation warning.

    INPUT:

    - ``issue_number`` -- integer; the github issue number where the
      deprecation is introduced

    - ``message`` -- string; an explanation why things are deprecated
      and by what it should be replaced

    - ``stack_level`` -- integer (default: `4`); this is passed on to
      :func:`warnings.warn`

    EXAMPLES::

        sage: def foo():
        ....:  sage.misc.superseded.deprecation(13109, 'the function foo is replaced by bar')
        sage: foo()
        doctest:...: DeprecationWarning: the function foo is replaced by bar
        See https://github.com/sagemath/sage/issues/13109 for details.

    .. SEEALSO::

        :func:`experimental`,
        :func:`warning`.
    """
def deprecation_cython(issue_number, message, stacklevel: int = 3) -> None:
    '''
    Issue a deprecation warning -- for use in cython functions.

    TESTS:

    We check that ``deprecation_cython`` in a cython function generates a warning
    with the same callsite reference as `deprecation` in a python function, whereas
    `deprecation` in a cython function does not::

        sage: # needs sage.misc.cython
        sage: cython(
        ....: \'\'\'
        ....: from sage.misc.superseded import deprecation_cython, deprecation
        ....: def foo1():
        ....:     deprecation_cython(100, "boo")
        ....: def foo2():
        ....:     deprecation(100, "boo")
        ....: \'\'\')
        sage: def foo3():
        ....:     deprecation(100, "boo")
        sage: if True:  # Execute the three "with" blocks as one doctest
        ....:     with warnings.catch_warnings(record=True) as w1:
        ....:        warnings.simplefilter("always")
        ....:        foo1()
        ....:     with warnings.catch_warnings(record=True) as w2:
        ....:        warnings.simplefilter("always")
        ....:        foo2()
        ....:     with warnings.catch_warnings(record=True) as w3:
        ....:        warnings.simplefilter("always")
        ....:        foo3()
        sage: w1[0].filename == w3[0].filename
        True
        sage: w2[0].filename == w3[0].filename
        False
    '''
def warning(issue_number, message, warning_class=..., stacklevel: int = 3) -> None:
    """
    Issue a warning.

    INPUT:

    - ``issue_number`` -- integer; the github issue number where the
      deprecation is introduced

    - ``message`` -- string; an explanation what is going on

    - ``warning_class`` -- (default: ``Warning``) a class inherited
      from a Python :class:`~exceptions.Warning`

    - ``stack_level`` -- integer (default: `3`); this is passed on to
      :func:`warnings.warn`

    EXAMPLES::

        sage: def foo():
        ....:     sage.misc.superseded.warning(
        ....:         99999,
        ....:         'The syntax will change in future.',
        ....:         FutureWarning)
        sage: foo()
        doctest:...: FutureWarning: The syntax will change in future.
        See https://github.com/sagemath/sage/issues/99999 for details.

    .. SEEALSO::

        :func:`deprecation`,
        :func:`experimental`,
        :class:`exceptions.Warning`.
    """
def experimental_warning(issue_number, message, stacklevel: int = 4) -> None:
    """
    Issue a warning that the functionality or class is experimental
    and might change in future.

    INPUT:

    - ``issue_number`` -- integer; the github issue number where the
      experimental functionality was introduced

    - ``message`` -- string; an explanation what is going on

    - ``stack_level`` -- integer (default: `4`); this is passed on to
      :func:`warnings.warn`

    EXAMPLES::

        sage: def foo():
        ....:    sage.misc.superseded.experimental_warning(
        ....:        66666, 'This function is experimental and '
        ....:               'might change in future.')
        sage: foo()
        doctest:...: FutureWarning: This function is experimental and
        might change in future.
        See https://github.com/sagemath/sage/issues/66666 for details.

    .. SEEALSO::

        :class:`mark_as_experimental`,
        :func:`warning`,
        :func:`deprecation`.
    """

class experimental:
    issue_number: Incomplete
    stacklevel: Incomplete
    def __init__(self, issue_number, stacklevel: int = 4) -> None:
        '''
        A decorator which warns about the experimental/unstable status of
        the decorated class/method/function.

        INPUT:

        - ``issue_number`` -- integer; the github issue number where this
          code was introduced

        - ``stack_level`` -- integer (default: `4`); this is passed on to
          :func:`warnings.warn`

        EXAMPLES::

            sage: @sage.misc.superseded.experimental(issue_number=79997)
            ....: def foo(*args, **kwargs):
            ....:     print("{} {}".format(args, kwargs))
            sage: foo(7, what=\'Hello\')
            doctest:...: FutureWarning: This class/method/function is
            marked as experimental. It, its functionality or its
            interface might change without a formal deprecation.
            See https://github.com/sagemath/sage/issues/79997 for details.
            (7,) {\'what\': \'Hello\'}

        ::

            sage: class bird(SageObject):
            ....:     @sage.misc.superseded.experimental(issue_number=99999)
            ....:     def __init__(self, *args, **kwargs):
            ....:         print("piep {} {}".format(args, kwargs))
            sage: _ = bird(99)
            doctest:...: FutureWarning: This class/method/function is
            marked as experimental. It, its functionality or its
            interface might change without a formal deprecation.
            See https://github.com/sagemath/sage/issues/99999 for details.
            piep (99,) {}

        TESTS:

        The following test works together with the doc-test for
        :meth:`__experimental_self_test` to demonstrate that warnings are issued only
        once, even in doc-tests (see :issue:`20601`).
        ::

            sage: from sage.misc.superseded import __experimental_self_test
            sage: _ = __experimental_self_test("A")
            doctest:...: FutureWarning: This class/method/function is
            marked as experimental. It, its functionality or its
            interface might change without a formal deprecation.
            See https://github.com/sagemath/sage/issues/88888 for details.
            I\'m A

        .. SEEALSO::

            :func:`experimental`,
            :func:`warning`,
            :func:`deprecation`.
        '''
    def __call__(self, func):
        '''
        Print experimental warning.

        INPUT:

        - ``func`` -- the function to decorate

        OUTPUT: the wrapper to this function

        TESTS::

            sage: def foo(*args, **kwargs):
            ....:     print("{} {}".format(args, kwargs))
            sage: from sage.misc.superseded import experimental
            sage: ex_foo = experimental(issue_number=99399)(foo)
            sage: ex_foo(3, what=\'Hello\')
            doctest:...: FutureWarning: This class/method/function is
            marked as experimental. It, its functionality or its
            interface might change without a formal deprecation.
            See https://github.com/sagemath/sage/issues/99399 for details.
            (3,) {\'what\': \'Hello\'}
        '''

class __experimental_self_test:
    '''
    This is a class only to demonstrate with a doc-test that the @experimental
    decorator only issues a warning message once (see :issue:`20601`).

    The test below does not issue a warning message because that warning has
    already been issued by a previous doc-test in the @experimental code. Note
    that this behaviour cannot be demonstrated within a single documentation
    string: Sphinx will itself suppress multiple issued warnings.

    TESTS::

        sage: from sage.misc.superseded import __experimental_self_test
        sage: _ = __experimental_self_test("B")
        I\'m B
    '''
    def __init__(self, x) -> None: ...

class DeprecatedFunctionAlias:
    """
    A wrapper around methods or functions which automatically prints a
    deprecation message. See :func:`deprecated_function_alias`.

    AUTHORS:

    - Florent Hivert (2009-11-23), with the help of Mike Hansen.
    - Luca De Feo (2011-07-11), printing the full module path when different from old path
    """
    func: Incomplete
    issue_number: Incomplete
    instance: Incomplete
    unbound: Incomplete
    __module__: Incomplete
    __doc__: Incomplete
    def __init__(self, issue_number, func, module, instance=None, unbound=None) -> None:
        """
        TESTS::

            sage: from sage.misc.superseded import deprecated_function_alias
            sage: g = deprecated_function_alias(13109, number_of_partitions)            # needs sage.combinat
            sage: from sage.misc.superseded import deprecated_function_alias
            sage: g.__doc__                                                             # needs sage.combinat
            'Deprecated: Use :func:`number_of_partitions` instead.\\nSee :issue:`13109` for details.\\n\\n'
        """
    def __call__(self, *args, **kwds):
        """
        TESTS::

            sage: from sage.misc.superseded import deprecated_function_alias
            sage: def bla(): return 42
            sage: blo = deprecated_function_alias(13109, bla)
            sage: blo()
            doctest:...: DeprecationWarning: blo is deprecated. Please use bla instead.
            See https://github.com/sagemath/sage/issues/13109 for details.
            42
        """
    def __get__(self, inst, cls=None):
        """
        TESTS::

            sage: from sage.misc.superseded import deprecated_function_alias
            sage: class cls():
            ....:    def new_meth(self): return 42
            ....:    old_meth = deprecated_function_alias(13109, new_meth)
            sage: obj = cls()
            sage: obj.old_meth.instance is obj
            True

        :issue:`19125`::

            sage: from sage.misc.superseded import deprecated_function_alias
            sage: class A:
            ....:    def __init__(self, x):
            ....:        self.x = x
            ....:    def f(self, y):
            ....:        return self.x+y
            ....:    g = deprecated_function_alias(42, f)
            sage: a1 = A(1)
            sage: a2 = A(2)
            sage: a1.g(a2.g(0))
            doctest:...: DeprecationWarning: g is deprecated. Please use f instead.
            See https://github.com/sagemath/sage/issues/42 for details.
            3
            sage: a1.f(a2.f(0))
            3
        """

def deprecated_function_alias(issue_number, func):
    """
    Create an aliased version of a function or a method which raises a
    deprecation warning message.

    If f is a function or a method, write
    ``g = deprecated_function_alias(issue_number, f)``
    to make a deprecated aliased version of f.

    INPUT:

    - ``issue_number`` -- integer; the github issue number where the
      deprecation is introduced

    - ``func`` -- the function or method to be aliased

    EXAMPLES::

        sage: from sage.misc.superseded import deprecated_function_alias
        sage: g = deprecated_function_alias(13109, number_of_partitions)                # needs sage.combinat sage.libs.flint
        sage: g(5)                                                                      # needs sage.combinat sage.libs.flint
        doctest:...: DeprecationWarning: g is deprecated.
        Please use sage.combinat.partition.number_of_partitions instead.
        See https://github.com/sagemath/sage/issues/13109 for details.
        7

    This also works for methods::

        sage: class cls():
        ....:    def new_meth(self): return 42
        ....:    old_meth = deprecated_function_alias(13109, new_meth)
        sage: cls().old_meth()
        doctest:...: DeprecationWarning: old_meth is deprecated. Please use new_meth instead.
        See https://github.com/sagemath/sage/issues/13109 for details.
        42

    :issue:`11585`::

        sage: def a(): pass
        sage: b = deprecated_function_alias(13109, a)
        sage: b()
        doctest:...: DeprecationWarning: b is deprecated. Please use a instead.
        See https://github.com/sagemath/sage/issues/13109 for details.

    AUTHORS:

     - Florent Hivert (2009-11-23), with the help of Mike Hansen.
     - Luca De Feo (2011-07-11), printing the full module path when different from old path
    """
