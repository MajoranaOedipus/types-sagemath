import _cython_3_2_1
import sage.modules.vector_double_dense
from sage.categories.category import RDF as RDF
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

unpickle_v0: _cython_3_2_1.cython_function_or_method
unpickle_v1: _cython_3_2_1.cython_function_or_method

class Vector_real_double_dense(sage.modules.vector_double_dense.Vector_double_dense):
    """File: /build/sagemath/src/sage/src/sage/modules/vector_real_double_dense.pyx (starting at line 40)

        Vectors over the Real Double Field.  These are supposed to be fast
        vector operations using C doubles. Most operations are implemented
        using numpy which will call the underlying BLAS, if needed, on the
        system.

        EXAMPLES::

            sage: v = vector(RDF, [1,2,3,4]); v
            (1.0, 2.0, 3.0, 4.0)
            sage: v*v
            30.0
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def stats_skew(self) -> Any:
        """Vector_real_double_dense.stats_skew(self)

        File: /build/sagemath/src/sage/src/sage/modules/vector_real_double_dense.pyx (starting at line 63)

        Compute the skewness of a data set.

        For normally distributed data, the skewness should be about
        0. A skewness value > 0 means that there is more weight in the
        left tail of the distribution. (Paragraph from the scipy.stats
        docstring.)

        EXAMPLES::

            sage: v = vector(RDF, range(9))
            sage: v.stats_skew()                                                        # needs scipy
            0.0"""
    @overload
    def stats_skew(self) -> Any:
        """Vector_real_double_dense.stats_skew(self)

        File: /build/sagemath/src/sage/src/sage/modules/vector_real_double_dense.pyx (starting at line 63)

        Compute the skewness of a data set.

        For normally distributed data, the skewness should be about
        0. A skewness value > 0 means that there is more weight in the
        left tail of the distribution. (Paragraph from the scipy.stats
        docstring.)

        EXAMPLES::

            sage: v = vector(RDF, range(9))
            sage: v.stats_skew()                                                        # needs scipy
            0.0"""
    def __reduce__(self) -> Any:
        """Vector_real_double_dense.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/modules/vector_real_double_dense.pyx (starting at line 81)

        Pickling.

        EXAMPLES::

            sage: a = vector(RDF, range(9))
            sage: loads(dumps(a)) == a
            True"""
