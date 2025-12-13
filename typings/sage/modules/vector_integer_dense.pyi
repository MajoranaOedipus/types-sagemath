import _cython_3_2_1
import sage.modules.free_module_element
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

unpickle_v0: _cython_3_2_1.cython_function_or_method
unpickle_v1: _cython_3_2_1.cython_function_or_method

class Vector_integer_dense(sage.modules.free_module_element.FreeModuleElement):
    """Vector_integer_dense(parent, x, coerce=True, copy=True)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, x, coerce=..., copy=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/modules/vector_integer_dense.pyx (starting at line 113)"""
    @overload
    def list(self, copy=...) -> Any:
        """Vector_integer_dense.list(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/modules/vector_integer_dense.pyx (starting at line 193)

        The list of entries of the vector.

        INPUT:

        - ``copy`` -- ignored optional argument

        EXAMPLES::

            sage: v = vector([1,2,3,4])
            sage: a = v.list(copy=False); a
            [1, 2, 3, 4]
            sage: a[0] = 0
            sage: v
            (1, 2, 3, 4)"""
    @overload
    def list(self, copy=...) -> Any:
        """Vector_integer_dense.list(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/modules/vector_integer_dense.pyx (starting at line 193)

        The list of entries of the vector.

        INPUT:

        - ``copy`` -- ignored optional argument

        EXAMPLES::

            sage: v = vector([1,2,3,4])
            sage: a = v.list(copy=False); a
            [1, 2, 3, 4]
            sage: a[0] = 0
            sage: v
            (1, 2, 3, 4)"""
    def __copy__(self) -> Any:
        """Vector_integer_dense.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/modules/vector_integer_dense.pyx (starting at line 73)"""
    def __reduce__(self) -> Any:
        """Vector_integer_dense.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/modules/vector_integer_dense.pyx (starting at line 214)"""
