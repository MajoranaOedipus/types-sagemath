import sage.structure.parent_old
from sage.structure.coerce_exceptions import CoercionException as CoercionException
from typing import Any, ClassVar

class ParentWithBase(sage.structure.parent_old.Parent):
    """ParentWithBase(base, *args, **kwds)

    File: /build/sagemath/src/sage/src/sage/structure/parent_base.pyx (starting at line 23)

    This class is being deprecated, see parent.Parent for the new model."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, base, *args, **kwds) -> Any:
        """File: /build/sagemath/src/sage/src/sage/structure/parent_base.pyx (starting at line 27)"""
    def base_extend(self, X) -> Any:
        """ParentWithBase.base_extend(self, X)

        File: /build/sagemath/src/sage/src/sage/structure/parent_base.pyx (starting at line 41)"""
