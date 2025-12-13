import sage.categories.map
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import ClassVar

class CCtoCDF(sage.categories.map.Map):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
