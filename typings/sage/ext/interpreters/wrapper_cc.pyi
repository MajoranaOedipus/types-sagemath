from collections.abc import Callable, Sequence
from typing import Any, TypedDict
from typings_sagemath import Num
from sage.ext.fast_callable import Wrapper
from sage.rings.complex_mpfr import ComplexNumber

import sage.ext.fast_callable
from sage.ext.fast_callable import CompilerInstrSpec as CompilerInstrSpec, InterpreterMetadata as InterpreterMetadata
from sage.structure.element import have_same_parent as have_same_parent, parent as parent

metadata: sage.ext.fast_callable.InterpreterMetadata

class _Args(TypedDict):
    args: int
    constants: Sequence[Num]
    py_constants: Sequence[object]
    stack: int
    code: Sequence[int]
    domain: Callable[[Any], Num]

class Wrapper_cc(Wrapper):
    def __init__(self, args: _Args): ...
    def __dealloc__(self) -> None: ...
    def __call__(self, *args: Num) -> ComplexNumber: ...