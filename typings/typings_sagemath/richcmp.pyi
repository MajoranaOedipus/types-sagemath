from typing import Literal, Protocol

type CmpOperator = Literal[0, 1, 2, 3, 4, 5]

class SupportsRichCmp[_T](Protocol):
    def __richcmp__(self, other, op: CmpOperator) -> _T:
        ...

class RichCmpMixin[_T]:
    def __eq__(self: SupportsRichCmp[_T], other) -> _T: ...  # type: ignore[reportIncompatibleMethodOverride]
    def __ne__(self: SupportsRichCmp[_T], other) -> _T: ...  # type: ignore[reportIncompatibleMethodOverride]
    def __lt__(self: SupportsRichCmp[_T], other) -> _T: ...  # type: ignore[reportIncompatibleMethodOverride]
    def __le__(self: SupportsRichCmp[_T], other) -> _T: ...  # type: ignore[reportIncompatibleMethodOverride]
    def __gt__(self: SupportsRichCmp[_T], other) -> _T: ...  # type: ignore[reportIncompatibleMethodOverride]
    def __ge__(self: SupportsRichCmp[_T], other) -> _T: ...  # type: ignore[reportIncompatibleMethodOverride]