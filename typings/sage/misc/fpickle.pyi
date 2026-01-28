"""
Function pickling

REFERENCE: The python cookbook.
"""

from typing import Any
from collections.abc import Callable
from types import CodeType, MethodWrapperType, ModuleType, FunctionType
from typings_sagemath import CallableArgs, Supports__code__

def code_ctor(*args) -> CodeType:
    """
    EXAMPLES:

    This indirectly tests this function. ::

        sage: def foo(a, b, c=10): return a+b+c
        sage: sage.misc.fpickle.reduce_code(foo.__code__)
        (<cyfunction code_ctor at ...>, ...)
        sage: unpickle_function(pickle_function(foo))
        <function foo at ...>
    """
    ...
def reduce_code(co: CodeType) -> tuple[CallableArgs[Any, CodeType], tuple[Any, ...]]:
    """
    EXAMPLES::

        sage: def foo(N): return N+1
        sage: sage.misc.fpickle.reduce_code(foo.__code__)
        (<cyfunction code_ctor at ...>, ...)

    Test that the constructed code matches the original code::

        sage: ctor, args = sage.misc.fpickle.reduce_code(foo.__code__)
        sage: ctor(*args) == foo.__code__
        True
    """
def pickle_function(func: Supports__code__) -> bytes:
    """
    Pickle the Python function func.  This is not a normal pickle; you
    must use the unpickle_function method to unpickle the pickled
    function.

    NOTE: This does not work on all functions, but does work on
    'surprisingly' many functions.  In particular, it does not
    work on functions that includes nested functions.

    INPUT:

    - ``func`` -- a Python function

    OUTPUT: string

    EXAMPLES::

        sage: def f(N): return N+1
        ...
        sage: g = pickle_function(f)
        sage: h = unpickle_function(g)
        sage: h(10)
        11
    """
def unpickle_function(pickled: bytes) -> FunctionType:
    """
    Unpickle a pickled function.

    EXAMPLES::

        sage: def f(N, M): return N*M
        ...
        sage: unpickle_function(pickle_function(f))(3,5)
        15
    """
def call_pickled_function(fpargs: tuple[bytes, tuple[tuple, dict]]) -> tuple[tuple[tuple, dict], Any]:
    ...
def pickleMethod(method: MethodWrapperType) -> tuple[Callable[[str, object, type], MethodWrapperType], type]:
    'support function for copyreg to pickle method refs'
    ...
def unpickleMethod(im_name: str,
                   __self__: object,
                   im_class: type) -> MethodWrapperType:
    'support function for copyreg to unpickle method refs'

oldModules: dict

def pickleModule(module: ModuleType) -> tuple[Callable[[str], ModuleType], str]:
    'support function for copyreg to pickle module refs'
def unpickleModule(name: str) -> ModuleType:
    'support function for copyreg to unpickle module refs'

