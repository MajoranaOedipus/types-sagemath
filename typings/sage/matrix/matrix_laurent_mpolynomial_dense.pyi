import sage.matrix.matrix_generic_dense
from sage.matrix.special import identity_matrix as identity_matrix
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

class Matrix_Laurent_mpolynomial_dense(sage.matrix.matrix_generic_dense.Matrix_generic_dense):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class Matrix_laurent_mpolynomial_dense(sage.matrix.matrix_generic_dense.Matrix_generic_dense):
    """File: /build/sagemath/src/sage/src/sage/matrix/matrix_laurent_mpolynomial_dense.pyx (starting at line 20)

        Dense matrix over a Laurent multivariate polynomial ring over a field.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def laurent_matrix_reduction(self) -> Any:
        """Matrix_laurent_mpolynomial_dense.laurent_matrix_reduction(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_laurent_mpolynomial_dense.pyx (starting at line 24)

        From a matrix ``self`` of Laurent polynomials, apply elementary operations
        to obtain a matrix ``P`` of polynomials such that the variables do not divide
        any column and any row.

        OUTPUT:

        Three matrices ``L``, ``P``, ``R`` such that ``self`` equals ``L P R``,
        where ``L`` and ``R`` are diagonal with monomial entries.

        EXAMPLES:

            sage: R.<x, y> = LaurentPolynomialRing(QQ)
            sage: L = [1/3*x^-1*y - 6*x^-2*y^2 - 1/2*x^-2*y, 1/5*x + 1/2*y + 1/6]
            sage: L += [1/2 - 5*x^-1*y - 2*x^-1, -1/3*y^-2 - 4*x^-1*y^-1 + 11*x^-1*y^-2]
            sage: A = matrix(R, 2, L)
            sage: lf, P, rg = A.laurent_matrix_reduction()
            sage: lf
            [     x^-2         0]
            [        0 x^-1*y^-2]
            sage: P
            [            1/3*x - 6*y - 1/2 1/5*x^3 + 1/2*x^2*y + 1/6*x^2]
            [        1/2*x*y - 5*y^2 - 2*y             -1/3*x - 4*y + 11]
            sage: rg
            [y 0]
            [0 1]"""
    @overload
    def laurent_matrix_reduction(self) -> Any:
        """Matrix_laurent_mpolynomial_dense.laurent_matrix_reduction(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_laurent_mpolynomial_dense.pyx (starting at line 24)

        From a matrix ``self`` of Laurent polynomials, apply elementary operations
        to obtain a matrix ``P`` of polynomials such that the variables do not divide
        any column and any row.

        OUTPUT:

        Three matrices ``L``, ``P``, ``R`` such that ``self`` equals ``L P R``,
        where ``L`` and ``R`` are diagonal with monomial entries.

        EXAMPLES:

            sage: R.<x, y> = LaurentPolynomialRing(QQ)
            sage: L = [1/3*x^-1*y - 6*x^-2*y^2 - 1/2*x^-2*y, 1/5*x + 1/2*y + 1/6]
            sage: L += [1/2 - 5*x^-1*y - 2*x^-1, -1/3*y^-2 - 4*x^-1*y^-1 + 11*x^-1*y^-2]
            sage: A = matrix(R, 2, L)
            sage: lf, P, rg = A.laurent_matrix_reduction()
            sage: lf
            [     x^-2         0]
            [        0 x^-1*y^-2]
            sage: P
            [            1/3*x - 6*y - 1/2 1/5*x^3 + 1/2*x^2*y + 1/6*x^2]
            [        1/2*x*y - 5*y^2 - 2*y             -1/3*x - 4*y + 11]
            sage: rg
            [y 0]
            [0 1]"""
