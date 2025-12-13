import sage.structure.element
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import ClassVar

class NumberFieldElement_base(sage.structure.element.FieldElement):
    """File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_base.pyx (starting at line 14)

        Abstract base class for
        :class:`~sage.rings.number_field.number_field_element.NumberFieldElement`.

        This class is defined for the purpose of :func:`isinstance` tests.
        It should not be instantiated.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: k.<a> = NumberField(x^3 + x + 1)                                          # needs sage.rings.number_field
            sage: isinstance(a, sage.rings.number_field.number_field_element_base.NumberFieldElement_base)                  # needs sage.rings.number_field
            True

        By design, there is a unique direct subclass::

            sage: len(sage.rings.number_field.number_field_element_base.NumberFieldElement_base.__subclasses__()) <= 1
            True
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
