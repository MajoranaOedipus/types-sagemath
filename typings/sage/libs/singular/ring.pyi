import _cython_3_2_1
import sage as sage
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.rings.finite_rings.finite_field_base import FiniteField_generic as FiniteField_generic
from sage.rings.fraction_field import FractionField_generic as FractionField_generic
from sage.rings.polynomial.polynomial_ring import PolynomialRing_field as PolynomialRing_field
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.polynomial.term_order import TermOrder as TermOrder
from sage.rings.rational_field import RationalField as RationalField
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, overload

__pyx_capi__: dict
currRing_wrapper: _cython_3_2_1.cython_function_or_method
order_dict: dict
poison_currRing: _cython_3_2_1.cython_function_or_method
print_currRing: _cython_3_2_1.cython_function_or_method

class ring_wrapper_Py:
    """File: /build/sagemath/src/sage/src/sage/libs/singular/ring.pyx (starting at line 593)

        Python object wrapping the ring pointer.

        This is useful to store ring pointers in Python containers.

        You must not construct instances of this class yourself, use
        :func:`wrap_ring` instead.

        EXAMPLES::

            sage: from sage.libs.singular.ring import ring_wrapper_Py
            sage: ring_wrapper_Py
            <class 'sage.libs.singular.ring.ring_wrapper_Py'>
    """
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    @overload
    def __hash__(self) -> Any:
        """ring_wrapper_Py.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/libs/singular/ring.pyx (starting at line 628)

        Return a hash value so that instances can be used as dictionary keys.

        OUTPUT: integer

        EXAMPLES::

            sage: from sage.libs.singular.ring import ring_wrapper_Py
            sage: t = ring_wrapper_Py()
            sage: t.__hash__()
            0"""
    @overload
    def __hash__(self) -> Any:
        """ring_wrapper_Py.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/libs/singular/ring.pyx (starting at line 628)

        Return a hash value so that instances can be used as dictionary keys.

        OUTPUT: integer

        EXAMPLES::

            sage: from sage.libs.singular.ring import ring_wrapper_Py
            sage: t = ring_wrapper_Py()
            sage: t.__hash__()
            0"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
