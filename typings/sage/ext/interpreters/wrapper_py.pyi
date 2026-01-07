from collections.abc import Sequence
from typing import Any, TypedDict
from sage.ext.fast_callable import Wrapper

from sage.ext.fast_callable import CompilerInstrSpec as CompilerInstrSpec, InterpreterMetadata as InterpreterMetadata

metadata: InterpreterMetadata

class _Args(TypedDict):
    args: int
    constants: Sequence[object]
    py_constants: Sequence[object]
    stack: int
    code: Sequence[int]
    domain: None

class Wrapper_py(Wrapper):
    def __init__(self, args: _Args): ...
    def __dealloc__(self) -> None: ...
    def __call__(self, *args: object) -> Any: ...