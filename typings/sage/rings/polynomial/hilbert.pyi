import _cython_3_2_1
import sage as sage
from sage.structure.element import have_same_parent as have_same_parent, parent as parent

first_hilbert_series: _cython_3_2_1.cython_function_or_method
hilbert_poincare_series: _cython_3_2_1.cython_function_or_method

class Node:
    """File: /build/sagemath/src/sage/src/sage/rings/polynomial/hilbert.pyx (starting at line 36)

        A node of a binary tree

        It has slots for data that allow to recursively compute
        the first Hilbert series of a monomial ideal.
    """
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
