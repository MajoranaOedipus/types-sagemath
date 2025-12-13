import _cython_3_2_1
import sage.modules.free_module_element
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar

MAX_MODULUS: int
unpickle_v0: _cython_3_2_1.cython_function_or_method
unpickle_v1: _cython_3_2_1.cython_function_or_method

class Vector_modn_dense(sage.modules.free_module_element.FreeModuleElement):
    """Vector_modn_dense(parent, x, coerce=True, copy=True)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, x, coerce=..., copy=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/modules/vector_modn_dense.pyx (starting at line 170)

                Create an element.

                TESTS:

                Note that ``coerce=False`` is dangerous::

                    sage: V = VectorSpace(GF(7), 3)
                    sage: v = V([2, 9, -5], coerce=False)
                    sage: v[0] == v[1]
                    False
                    sage: v[0] + 1 == v[1] + 1
                    True
                    sage: v[0] == v[2]
                    False
        """
    def __copy__(self) -> Any:
        """Vector_modn_dense.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/modules/vector_modn_dense.pyx (starting at line 150)"""
    def __reduce__(self) -> Any:
        """Vector_modn_dense.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/modules/vector_modn_dense.pyx (starting at line 289)"""
