import _cython_3_2_1
import sage.modules.vector_double_dense
from sage.categories.category import CDF as CDF
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar

unpickle_v0: _cython_3_2_1.cython_function_or_method
unpickle_v1: _cython_3_2_1.cython_function_or_method

class Vector_complex_double_dense(sage.modules.vector_double_dense.Vector_double_dense):
    """File: /build/sagemath/src/sage/src/sage/modules/vector_complex_double_dense.pyx (starting at line 49)

        Vectors over the Complex Double Field.  These are supposed to be
        fast vector operations using C doubles. Most operations are
        implemented using numpy which will call the underlying BLAS, if
        needed, on the system.

        EXAMPLES::

            sage: v = vector(CDF, [(1,-1), (2,pi), (3,5)]); v                               # needs sage.symbolic
            (1.0 - 1.0*I, 2.0 + 3.141592653589793*I, 3.0 + 5.0*I)
            sage: v*v  # rel tol 1e-15                                                      # needs sage.symbolic
            -21.86960440108936 + 40.56637061435917*I
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def __reduce__(self) -> Any:
        """Vector_complex_double_dense.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/modules/vector_complex_double_dense.pyx (starting at line 72)

        Pickling.

        EXAMPLES::

            sage: a = vector(CDF, range(9))
            sage: loads(dumps(a)) == a
            True"""
