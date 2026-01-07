from collections.abc import Callable, Sequence
from typing import Any, TypedDict, SupportsFloat
from sage.ext.fast_callable import Wrapper

from sage.ext.fast_callable import CompilerInstrSpec as CompilerInstrSpec, InterpreterMetadata as InterpreterMetadata

metadata: InterpreterMetadata

class _Args[_DomainElement](TypedDict):
    args: int
    constants: Sequence[SupportsFloat]
    py_constants: Sequence[object]
    stack: int
    code: Sequence[int]
    domain: Callable[[Any], _DomainElement]

class Wrapper_rdf[_DomainElement](Wrapper):
    def __init__(self, args: _Args[_DomainElement]): ...
    def __dealloc__(self) -> None: ...
    def __call__(self, *args: SupportsFloat) -> _DomainElement: ...