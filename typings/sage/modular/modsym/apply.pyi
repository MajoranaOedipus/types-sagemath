import _cython_3_2_1
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import ClassVar

apply_to_monomial: _cython_3_2_1.cython_function_or_method

class Apply:
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
