from collections.abc import Sequence
from typing import TypedDict
from typings_sagemath import Num
from sage.ext.fast_callable import Wrapper
from sage.rings.complex_double import ComplexDoubleElement

from sage.ext.fast_callable import CompilerInstrSpec as CompilerInstrSpec, InterpreterMetadata as InterpreterMetadata
from sage.structure.element import have_same_parent as have_same_parent, parent as parent

metadata: InterpreterMetadata

class _Args(TypedDict):
    args: int
    constants: Sequence[Num]
    py_constants: Sequence[object]
    stack: int
    code: Sequence[int]

class Wrapper_cdf(Wrapper):
    def __init__(self, args: _Args): ...
    def __dealloc__(self) -> None: ...
    def __call__(self, *args: Num) -> ComplexDoubleElement: ...