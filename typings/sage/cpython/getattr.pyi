import _cython_3_2_1
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from typing import Any

__pyx_capi__: dict
dir_with_other_class: _cython_3_2_1.cython_function_or_method
getattr_from_other_class: _cython_3_2_1.cython_function_or_method
raw_getattr: _cython_3_2_1.cython_function_or_method

class AttributeErrorMessage:
    """AttributeErrorMessage(obj=None, name='')

    File: /build/sagemath/src/sage/src/sage/cpython/getattr.pyx (starting at line 39)

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
    cls: cls
    name: name
    def __init__(self, obj=..., name=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/cpython/getattr.pyx (starting at line 98)"""
