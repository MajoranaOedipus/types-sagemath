from typing import Protocol, Self
from sage.structure.parent_gens import ParentWithGens

class ElementWithGens(Protocol):
    def parent(self) -> ParentWithGens: ...

class CallableArgs[Arg, ReturnT](Protocol):
    def __call__(self, *args: Arg) -> ReturnT:
        ...

class StrictlyComparable(Protocol):
    def __lt__(self, other: Self) -> bool: ...
    def __gt__(self, other: Self) -> bool: ...

class NonStrictlyComparable(Protocol):
    def __le__(self, other: Self) -> bool: ...
    def __ge__(self, other: Self) -> bool: ...

class Comparable(NonStrictlyComparable, StrictlyComparable):
    ...


class Addable(Protocol):
    def __add__(self, other: Self) -> Self:
        ...

class AddableWith[A](Protocol):
    def __add__(self, a: A) -> Self:
        ...

class AddableWithExt[A, S](Protocol):
    def __add__(self, a: A) -> S:
        ...

class Multiplicable(Protocol):
    def __mul__(self, other: Self) -> Self:
        ...

class MultiplicableWith[M](Protocol):
    def __mul__(self, m: M) -> Self:
        ...

class MultiplicableWithExt[M, P](Protocol):
    def __mul__(self, a: M) -> P:
        ...
