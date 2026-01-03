"""
Variants of getattr()
"""
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from typing import Any


class AttributeErrorMessage[T]:
    """
    Try to emulate the standard Python :exc:`AttributeError` message.

    .. NOTE::

        The typical fate of an attribute error is being caught. Hence,
        under normal circumstances, nobody will ever see the error
        message. The idea for this class is to provide an object that
        is fast to create and whose string representation is an attribute
        error's message. That string representation is only created if
        someone wants to see it.

    EXAMPLES::

        sage: 1.bla  #indirect doctest
        Traceback (most recent call last):
        ...
        AttributeError: 'sage.rings.integer.Integer' object has no attribute 'bla'...
        sage: x = polygen(ZZ, 'x')
        sage: QQ[x].gen().bla                                                           # needs sage.libs.flint
        Traceback (most recent call last):
        ...
        AttributeError: 'sage.rings.polynomial.polynomial_rational_flint.Polynomial_rational_flint' object has no attribute 'bla'...

    ::

        sage: from sage.cpython.getattr import AttributeErrorMessage
        sage: AttributeErrorMessage(int(1), 'bla')
        'int' object has no attribute 'bla'

    TESTS:

    The error message used for the :exc:`AttributeError` is a unique object
    and is changed inplace. This is for reasons of efficiency.
    Hence, if one really needs the error message as a string, then one should
    make a copy of its string representation before it changes. ::

        sage: try:
        ....:     1.__bla
        ....: except AttributeError as exc:
        ....:     ElementError = exc
        sage: ElementError
        AttributeError('sage.rings.integer.Integer' object has no attribute '__bla'...)
        sage: try:
        ....:     x.__bla
        ....: except AttributeError as exc:
        ....:     ElementError2 = exc
        sage: ElementError
        AttributeError('sage.rings.polynomial...' object has no attribute '__bla'...)
        sage: ElementError2.args[0] is ElementError.args[0]
        True
        sage: isinstance(ElementError.args[0], sage.cpython.getattr.AttributeErrorMessage)
        True

    AUTHOR:

    - Simon King (2011-05-21)"""
    cls: type[T]
    name: str
    def __init__(self, obj: T = None, name: str = ""):
        ...


def raw_getattr(obj: object, name: str) -> Any:
    """
    Like ``getattr(obj, name)`` but without invoking the binding
    behavior of descriptors under normal attribute access.
    This can be used to easily get unbound methods or other
    descriptors.

    This ignores ``__getattribute__`` hooks but it does support
    ``__getattr__``.

    .. NOTE::

        For Cython classes, ``__getattr__`` is actually implemented as
        ``__getattribute__``, which means that it is not supported by
        ``raw_getattr``.

    EXAMPLES::

        sage: class X:
        ....:     @property
        ....:     def prop(self):
        ....:         return 42
        ....:     def method(self):
        ....:         pass
        ....:     def __getattr__(self, name):
        ....:         return "magic " + name
        sage: raw_getattr(X, "prop")
        <property object at ...>
        sage: raw_getattr(X, "method")
        <function ...method at ...>
        sage: raw_getattr(X, "attr")
        Traceback (most recent call last):
        ...
        AttributeError: '...' object has no attribute 'attr'...
        sage: x = X()
        sage: raw_getattr(x, "prop")
        <property object at ...>
        sage: raw_getattr(x, "method")
        <function ...method at ...>
        sage: raw_getattr(x, "attr")
        'magic attr'
        sage: x.__dict__["prop"] = 'no'
        sage: x.__dict__["method"] = 'yes'
        sage: x.__dict__["attr"] = 'ok'
        sage: raw_getattr(x, "prop")
        <property object at ...>
        sage: raw_getattr(x, "method")
        'yes'
        sage: raw_getattr(x, "attr")
        'ok'

    The same tests with an inherited new-style class::

        sage: class Y(X, object):
        ....:     pass
        sage: raw_getattr(Y, "prop")
        <property object at ...>
        sage: raw_getattr(Y, "method")
        <function ...method at ...>
        sage: raw_getattr(Y, "attr")
        Traceback (most recent call last):
        ...
        AttributeError: '...' object has no attribute 'attr'...
        sage: y = Y()
        sage: raw_getattr(y, "prop")
        <property object at ...>
        sage: raw_getattr(y, "method")
        <function ...method at ...>
        sage: raw_getattr(y, "attr")
        'magic attr'
        sage: y.__dict__["prop"] = 'no'
        sage: y.__dict__["method"] = 'yes'
        sage: y.__dict__["attr"] = 'ok'
        sage: raw_getattr(y, "prop")
        <property object at ...>
        sage: raw_getattr(y, "method")
        'yes'
        sage: raw_getattr(y, "attr")
        'ok'
    """
def getattr_from_other_class(self: object, cls: type, name: str) -> Any:
    """
    Emulate ``getattr(self, name)``, as if ``self`` was an instance of
    ``cls``.

    INPUT:

    - ``self`` -- some object

    - ``cls`` -- a new-style class

    - ``name`` -- string

    If ``self`` is an instance of cls, raises an :exc:`AttributeError`, to
    avoid a double lookup. This function is intended to be called from
    __getattr__, and so should not be called if name is an attribute
    of ``self``.

    EXAMPLES::

        sage: from sage.cpython.getattr import getattr_from_other_class
        sage: class A():
        ....:      def inc(self):
        ....:          return self + 1
        ....:
        ....:      @staticmethod
        ....:      def greeting():
        ....:          print("Hello World!")
        ....:
        ....:      @lazy_attribute
        ....:      def lazy_attribute(self):
        ....:          return repr(self)
        sage: getattr_from_other_class(1, A, "inc")
        <bound method A.inc of 1>
        sage: getattr_from_other_class(1, A, "inc")()
        2

    Static methods work::

        sage: getattr_from_other_class(1, A, "greeting")()
        Hello World!

    Caveat: lazy attributes work with extension types only
    if they allow attribute assignment or have a public attribute
    ``_cached_methods`` of type ``<dict>``. This condition
    is satisfied, e.g., by any class that is derived from
    :class:`Parent`::

        sage: getattr_from_other_class(1, A, "lazy_attribute")
        Traceback (most recent call last):
        ...
        AttributeError: 'sage.rings.integer.Integer' object has no attribute 'lazy_attribute'...

    The integer ring is a parent, so, lazy attributes work::

        sage: getattr_from_other_class(ZZ, A, "lazy_attribute")
        'Integer Ring'
        sage: getattr_from_other_class(PolynomialRing(QQ, name='x', sparse=True).one(), A, "lazy_attribute")
        '1'
        sage: getattr_from_other_class(17, A, "lazy_attribute")
        Traceback (most recent call last):
        ...
        AttributeError: 'sage.rings.integer.Integer' object has no attribute 'lazy_attribute'...

    In general, descriptors are not yet well supported, because they
    often do not accept to be cheated with the type of their instance::

        sage: A.__weakref__.__get__(1)
        Traceback (most recent call last):
        ...
        TypeError: descriptor '__weakref__' for 'A' objects doesn't apply
        to ...'sage.rings.integer.Integer' object

    When this occurs, an :exc:`AttributeError` is raised::

        sage: getattr_from_other_class(1, A, "__weakref__")
        Traceback (most recent call last):
        ...
        AttributeError: 'sage.rings.integer.Integer' object has no attribute '__weakref__'...

    This was caught by :issue:`8296` for which we do a couple more tests::

        sage: "__weakref__" in dir(A)
        True
        sage: 1.__weakref__
        Traceback (most recent call last):
        ...
        AttributeError: 'sage.rings.integer.Integer' object has no attribute '__weakref__'...

        sage: n = 1
        sage: ip = get_ipython()                 # not tested: only works in interactive shell
        sage: ip.magic_psearch('n.N')            # not tested: only works in interactive shell
        n.N
        sage: ip.magic_psearch('n.__weakref__')  # not tested: only works in interactive shell

    Caveat: When __call__ is not defined for instances, using
    ``A.__call__`` yields the method ``__call__`` of the class. We use
    a workaround but there is no guarantee for robustness.

        sage: getattr_from_other_class(1, A, "__call__")
        Traceback (most recent call last):
        ...
        AttributeError: 'sage.rings.integer.Integer' object has no attribute '__call__'...

    TESTS:

    Check that we do not pick up special attributes from the ``type``
    class, see :issue:`20686`::

        sage: getattr_from_other_class(1, type, "__name__")
        Traceback (most recent call last):
        ...
        AttributeError: 'sage.rings.integer.Integer' object has no attribute '__name__'...

    Non-strings as "name" are handled gracefully::

        sage: getattr_from_other_class(1, type, None)
        Traceback (most recent call last):
        ...
        AttributeError: 'sage.rings.integer.Integer' object has no attribute None...
    """

def dir_with_other_class(self: object, *cls: tuple[type]) -> list[str]:
    r"""
    Emulates ``dir(self)``, as if ``self`` was also an instance ``cls``,
    right after ``caller_class`` in the method resolution order
    (``self.__class__.mro()``)

    EXAMPLES::

        sage: class A():
        ....:    a = 1
        ....:    b = 2
        ....:    c = 3
        sage: class B():
        ....:    b = 2
        ....:    c = 3
        ....:    d = 4
        sage: x = A()
        sage: x.c = 1; x.e = 1
        sage: from sage.cpython.getattr import dir_with_other_class
        sage: dir_with_other_class(x, B)
        [..., 'a', 'b', 'c', 'd', 'e']
        sage: class C():
        ....:    f = 6
        sage: dir_with_other_class(x, B, C)
        [..., 'a', 'b', 'c', 'd', 'e', 'f']

    Check that objects without dicts are well handled::

        sage: # needs sage.misc.cython
        sage: cython("cdef class A:\n    cdef public int a")
        sage: cython("cdef class B:\n    cdef public int b")
        sage: x = A()
        sage: x.a = 1
        sage: hasattr(x,'__dict__')
        False
        sage: dir_with_other_class(x, B)
        [..., 'a', 'b']

    TESTS:

    Check that :issue:`13043` is fixed::

        sage: len(dir(RIF))==len(set(dir(RIF)))                                         # needs sage.rings.real_interval_field
        True
    """
