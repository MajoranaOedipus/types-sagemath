import sage.modules.vector_numpy_dense
from sage.categories.category import ZZ as ZZ
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import ClassVar

class Vector_numpy_integer_dense(sage.modules.vector_numpy_dense.Vector_numpy_dense):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
