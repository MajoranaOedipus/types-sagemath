from collections.abc import Callable, Sequence
from typing import Any, TypedDict
from typings_sagemath import Real
from sage.ext.fast_callable import Wrapper

from sage.ext.fast_callable import CompilerInstrSpec as CompilerInstrSpec, InterpreterMetadata as InterpreterMetadata
from sage.structure.element import have_same_parent as have_same_parent, parent as parent

metadata: InterpreterMetadata

class _Args[_DomainElement](TypedDict):
    args: int
    constants: Sequence[Real]
    py_constants: Sequence[object]
    stack: int
    code: Sequence[int]
    domain: Callable[[Any], _DomainElement]

class Wrapper_rr[_DomainElement](Wrapper):
    def __init__(self, args: _Args[_DomainElement]): ...
    def __dealloc__(self) -> None: ...
    def __call__(self, *args: Real) -> _DomainElement: ...
