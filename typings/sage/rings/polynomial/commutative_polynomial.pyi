import sage.structure.element
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import ClassVar

class CommutativePolynomial(sage.structure.element.CommutativeAlgebraElement):
    """File: /build/sagemath/src/sage/src/sage/rings/polynomial/commutative_polynomial.pyx (starting at line 1)

        Abstract base class for commutative polynomials in any number of variables.

        It is a common base for :class:`~sage.rings.polynomial.polynomial_element.Polynomial`,
        :class:`~sage.rings.polynomial.multi_polynomial.MPolynomial`, and
        :class:`~sage.rings.polynomial.infinite_polynomial_element.InfinitePolynomial`.

        EXAMPLES::

            sage: from sage.rings.polynomial.commutative_polynomial import CommutativePolynomial
            sage: K.<x> = PolynomialRing(QQ)
            sage: isinstance(x, CommutativePolynomial)
            True
            sage: K.<x,y> = PolynomialRing(QQ)
            sage: isinstance(x, CommutativePolynomial)
            True
            sage: X.<x,y> = InfinitePolynomialRing(ZZ, implementation='sparse')
            sage: isinstance(x[2], CommutativePolynomial)
            True
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
