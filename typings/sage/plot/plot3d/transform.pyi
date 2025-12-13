import _cython_3_2_1
from sage.categories.category import RDF as RDF, pi as pi
from sage.matrix.constructor import matrix as matrix
from sage.modules.free_module_element import vector as vector
from typing import Any, ClassVar

rotate_arbitrary: _cython_3_2_1.cython_function_or_method

class Transformation:
    """Transformation(scale=(1, 1, 1), rot=None, trans=[0, 0, 0], m=None)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, scale=..., rot=..., trans=..., m=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/plot/plot3d/transform.pyx (starting at line 28)"""
    def avg_scale(self) -> Any:
        """Transformation.avg_scale(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/transform.pyx (starting at line 127)"""
    def get_matrix(self) -> Any:
        """Transformation.get_matrix(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/transform.pyx (starting at line 60)"""
    def is_skew(self, eps=...) -> Any:
        """Transformation.is_skew(self, eps=1e-5)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/transform.pyx (starting at line 63)"""
    def is_uniform(self, eps=...) -> Any:
        """Transformation.is_uniform(self, eps=1e-5)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/transform.pyx (starting at line 67)"""
    def is_uniform_on(self, basis, eps=...) -> Any:
        """Transformation.is_uniform_on(self, basis, eps=1e-5)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/transform.pyx (starting at line 72)"""
    def max_scale(self) -> Any:
        """Transformation.max_scale(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/transform.pyx (starting at line 122)"""
    def transform_bounding_box(self, box) -> Any:
        """Transformation.transform_bounding_box(self, box)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/transform.pyx (starting at line 90)"""
    def transform_point(self, x) -> Any:
        """Transformation.transform_point(self, x)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/transform.pyx (starting at line 78)"""
    def transform_vector(self, v) -> Any:
        """Transformation.transform_vector(self, v)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/transform.pyx (starting at line 84)"""
    def __call__(self, p) -> Any:
        """Transformation.__call__(self, p)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/transform.pyx (starting at line 119)"""
    def __invert__(self) -> Any:
        """Transformation.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/transform.pyx (starting at line 116)"""
    def __mul__(self, Transformationself, Transformationother) -> Any:
        """Transformation.__mul__(Transformation self, Transformation other)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/transform.pyx (starting at line 113)"""
    def __rmul__(self, other):
        """Return value*self."""
