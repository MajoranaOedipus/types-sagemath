import _cython_3_2_1
import sage.structure.element
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.rings.integer import Integer as Integer
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

__pyx_capi__: dict
unpickle_FiniteDimensionalAlgebraElement: _cython_3_2_1.cython_function_or_method

class FiniteDimensionalAlgebraElement(sage.structure.element.AlgebraElement):
    """FiniteDimensionalAlgebraElement(A, elt=None, check=True)

    File: /build/sagemath/src/sage/src/sage/algebras/finite_dimensional_algebras/finite_dimensional_algebra_element.pyx (starting at line 41)

    Create an element of a :class:`FiniteDimensionalAlgebra` using a multiplication table.

    INPUT:

    - ``A`` -- a :class:`FiniteDimensionalAlgebra` which will be the parent

    - ``elt`` -- vector, matrix or element of the base field
      (default: ``None``)

    - ``check`` -- boolean (default: ``True``); if ``False`` and ``elt`` is a
      matrix, assume that it is known to be the matrix of an element

    If ``elt`` is a vector or a matrix consisting of a single row, it is
    interpreted as a vector of coordinates with respect to the given basis
    of ``A``.  If ``elt`` is a square matrix, it is interpreted as a
    multiplication matrix with respect to this basis.

    EXAMPLES::

        sage: A = FiniteDimensionalAlgebra(GF(3), [Matrix([[1,0], [0,1]]),
        ....:                                      Matrix([[0,1], [0,0]])])
        sage: A(17)
        2*e0
        sage: A([1,1])
        e0 + e1"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, A, elt=..., check=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/algebras/finite_dimensional_algebras/finite_dimensional_algebra_element.pyx (starting at line 69)

                TESTS::

                    sage: A = FiniteDimensionalAlgebra(GF(3), [Matrix([[1,0], [0,1]]),
                    ....:                                      Matrix([[0,1], [0,0]])])
                    sage: A(QQ(4))
                    Traceback (most recent call last):
                    ...
                    TypeError: elt should be a vector, a matrix, or an element of the base field

                    sage: B = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0], [0,1]]),
                    ....:                                   Matrix([[0,1], [-1,0]])])
                    sage: elt = B(Matrix([[1,1], [-1,1]])); elt
                    e0 + e1
                    sage: TestSuite(elt).run()
                    sage: B(Matrix([[0,1], [1,0]]))
                    Traceback (most recent call last):
                    ...
                    ValueError: matrix does not define an element of the algebra
        """
    @overload
    def characteristic_polynomial(self) -> Any:
        """FiniteDimensionalAlgebraElement.characteristic_polynomial(self)

        File: /build/sagemath/src/sage/src/sage/algebras/finite_dimensional_algebras/finite_dimensional_algebra_element.pyx (starting at line 681)

        Return the characteristic polynomial of ``self``.

        .. NOTE::

            This function just returns the characteristic polynomial
            of the matrix of right multiplication by ``self``.  This
            may not be a very meaningful invariant if the algebra is
            not unitary and associative.

        EXAMPLES::

            sage: B = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0,0], [0,1,0], [0,0,0]]),
            ....:                                   Matrix([[0,1,0], [0,0,0], [0,0,0]]),
            ....:                                   Matrix([[0,0,0], [0,0,0], [0,0,1]])])
            sage: B(0).characteristic_polynomial()                                      # needs sage.libs.pari
            x^3
            sage: b = B.random_element()
            sage: f = b.characteristic_polynomial(); f  # random                        # needs sage.libs.pari
            x^3 - 8*x^2 + 16*x
            sage: f(b) == 0                                                             # needs sage.libs.pari
            True"""
    @overload
    def characteristic_polynomial(self) -> Any:
        """FiniteDimensionalAlgebraElement.characteristic_polynomial(self)

        File: /build/sagemath/src/sage/src/sage/algebras/finite_dimensional_algebras/finite_dimensional_algebra_element.pyx (starting at line 681)

        Return the characteristic polynomial of ``self``.

        .. NOTE::

            This function just returns the characteristic polynomial
            of the matrix of right multiplication by ``self``.  This
            may not be a very meaningful invariant if the algebra is
            not unitary and associative.

        EXAMPLES::

            sage: B = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0,0], [0,1,0], [0,0,0]]),
            ....:                                   Matrix([[0,1,0], [0,0,0], [0,0,0]]),
            ....:                                   Matrix([[0,0,0], [0,0,0], [0,0,1]])])
            sage: B(0).characteristic_polynomial()                                      # needs sage.libs.pari
            x^3
            sage: b = B.random_element()
            sage: f = b.characteristic_polynomial(); f  # random                        # needs sage.libs.pari
            x^3 - 8*x^2 + 16*x
            sage: f(b) == 0                                                             # needs sage.libs.pari
            True"""
    @overload
    def characteristic_polynomial(self) -> Any:
        """FiniteDimensionalAlgebraElement.characteristic_polynomial(self)

        File: /build/sagemath/src/sage/src/sage/algebras/finite_dimensional_algebras/finite_dimensional_algebra_element.pyx (starting at line 681)

        Return the characteristic polynomial of ``self``.

        .. NOTE::

            This function just returns the characteristic polynomial
            of the matrix of right multiplication by ``self``.  This
            may not be a very meaningful invariant if the algebra is
            not unitary and associative.

        EXAMPLES::

            sage: B = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0,0], [0,1,0], [0,0,0]]),
            ....:                                   Matrix([[0,1,0], [0,0,0], [0,0,0]]),
            ....:                                   Matrix([[0,0,0], [0,0,0], [0,0,1]])])
            sage: B(0).characteristic_polynomial()                                      # needs sage.libs.pari
            x^3
            sage: b = B.random_element()
            sage: f = b.characteristic_polynomial(); f  # random                        # needs sage.libs.pari
            x^3 - 8*x^2 + 16*x
            sage: f(b) == 0                                                             # needs sage.libs.pari
            True"""
    @overload
    def inverse(self) -> Any:
        """FiniteDimensionalAlgebraElement.inverse(self)

        File: /build/sagemath/src/sage/src/sage/algebras/finite_dimensional_algebras/finite_dimensional_algebra_element.pyx (starting at line 591)

        Return the two-sided multiplicative inverse of ``self``, if it
        exists.

        This assumes that the algebra to which ``self`` belongs is
        associative.

        .. NOTE::

            If an element of a finite-dimensional unitary associative
            algebra over a field admits a left inverse, then this is the
            unique left inverse, and it is also a right inverse.

        EXAMPLES::

            sage: C = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0], [0,1]]),
            ....:                                   Matrix([[0,1], [-1,0]])])
            sage: C([1,2]).inverse()
            1/5*e0 - 2/5*e1"""
    @overload
    def inverse(self) -> Any:
        """FiniteDimensionalAlgebraElement.inverse(self)

        File: /build/sagemath/src/sage/src/sage/algebras/finite_dimensional_algebras/finite_dimensional_algebra_element.pyx (starting at line 591)

        Return the two-sided multiplicative inverse of ``self``, if it
        exists.

        This assumes that the algebra to which ``self`` belongs is
        associative.

        .. NOTE::

            If an element of a finite-dimensional unitary associative
            algebra over a field admits a left inverse, then this is the
            unique left inverse, and it is also a right inverse.

        EXAMPLES::

            sage: C = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0], [0,1]]),
            ....:                                   Matrix([[0,1], [-1,0]])])
            sage: C([1,2]).inverse()
            1/5*e0 - 2/5*e1"""
    @overload
    def is_invertible(self) -> Any:
        """FiniteDimensionalAlgebraElement.is_invertible(self)

        File: /build/sagemath/src/sage/src/sage/algebras/finite_dimensional_algebras/finite_dimensional_algebra_element.pyx (starting at line 532)

        Return ``True`` if ``self`` has a two-sided multiplicative
        inverse.

        This assumes that the algebra to which ``self`` belongs is
        associative.

        .. NOTE::

            If an element of a unitary finite-dimensional algebra over a field
            admits a left inverse, then this is the unique left
            inverse, and it is also a right inverse.

        EXAMPLES::

            sage: C = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0], [0,1]]),
            ....:                                   Matrix([[0,1], [-1,0]])])
            sage: C([1,2]).is_invertible()
            True
            sage: C(0).is_invertible()
            False"""
    @overload
    def is_invertible(self) -> Any:
        """FiniteDimensionalAlgebraElement.is_invertible(self)

        File: /build/sagemath/src/sage/src/sage/algebras/finite_dimensional_algebras/finite_dimensional_algebra_element.pyx (starting at line 532)

        Return ``True`` if ``self`` has a two-sided multiplicative
        inverse.

        This assumes that the algebra to which ``self`` belongs is
        associative.

        .. NOTE::

            If an element of a unitary finite-dimensional algebra over a field
            admits a left inverse, then this is the unique left
            inverse, and it is also a right inverse.

        EXAMPLES::

            sage: C = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0], [0,1]]),
            ....:                                   Matrix([[0,1], [-1,0]])])
            sage: C([1,2]).is_invertible()
            True
            sage: C(0).is_invertible()
            False"""
    @overload
    def is_invertible(self) -> Any:
        """FiniteDimensionalAlgebraElement.is_invertible(self)

        File: /build/sagemath/src/sage/src/sage/algebras/finite_dimensional_algebras/finite_dimensional_algebra_element.pyx (starting at line 532)

        Return ``True`` if ``self`` has a two-sided multiplicative
        inverse.

        This assumes that the algebra to which ``self`` belongs is
        associative.

        .. NOTE::

            If an element of a unitary finite-dimensional algebra over a field
            admits a left inverse, then this is the unique left
            inverse, and it is also a right inverse.

        EXAMPLES::

            sage: C = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0], [0,1]]),
            ....:                                   Matrix([[0,1], [-1,0]])])
            sage: C([1,2]).is_invertible()
            True
            sage: C(0).is_invertible()
            False"""
    @overload
    def is_nilpotent(self) -> Any:
        """FiniteDimensionalAlgebraElement.is_nilpotent(self)

        File: /build/sagemath/src/sage/src/sage/algebras/finite_dimensional_algebras/finite_dimensional_algebra_element.pyx (starting at line 635)

        Return ``True`` if ``self`` is nilpotent.

        EXAMPLES::

            sage: C = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0], [0,1]]),
            ....:                                   Matrix([[0,1], [0,0]])])
            sage: C([1,0]).is_nilpotent()
            False
            sage: C([0,1]).is_nilpotent()
            True

            sage: A = FiniteDimensionalAlgebra(QQ, [Matrix([0])])
            sage: A([1]).is_nilpotent()
            True"""
    @overload
    def is_nilpotent(self) -> Any:
        """FiniteDimensionalAlgebraElement.is_nilpotent(self)

        File: /build/sagemath/src/sage/src/sage/algebras/finite_dimensional_algebras/finite_dimensional_algebra_element.pyx (starting at line 635)

        Return ``True`` if ``self`` is nilpotent.

        EXAMPLES::

            sage: C = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0], [0,1]]),
            ....:                                   Matrix([[0,1], [0,0]])])
            sage: C([1,0]).is_nilpotent()
            False
            sage: C([0,1]).is_nilpotent()
            True

            sage: A = FiniteDimensionalAlgebra(QQ, [Matrix([0])])
            sage: A([1]).is_nilpotent()
            True"""
    @overload
    def is_nilpotent(self) -> Any:
        """FiniteDimensionalAlgebraElement.is_nilpotent(self)

        File: /build/sagemath/src/sage/src/sage/algebras/finite_dimensional_algebras/finite_dimensional_algebra_element.pyx (starting at line 635)

        Return ``True`` if ``self`` is nilpotent.

        EXAMPLES::

            sage: C = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0], [0,1]]),
            ....:                                   Matrix([[0,1], [0,0]])])
            sage: C([1,0]).is_nilpotent()
            False
            sage: C([0,1]).is_nilpotent()
            True

            sage: A = FiniteDimensionalAlgebra(QQ, [Matrix([0])])
            sage: A([1]).is_nilpotent()
            True"""
    @overload
    def is_nilpotent(self) -> Any:
        """FiniteDimensionalAlgebraElement.is_nilpotent(self)

        File: /build/sagemath/src/sage/src/sage/algebras/finite_dimensional_algebras/finite_dimensional_algebra_element.pyx (starting at line 635)

        Return ``True`` if ``self`` is nilpotent.

        EXAMPLES::

            sage: C = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0], [0,1]]),
            ....:                                   Matrix([[0,1], [0,0]])])
            sage: C([1,0]).is_nilpotent()
            False
            sage: C([0,1]).is_nilpotent()
            True

            sage: A = FiniteDimensionalAlgebra(QQ, [Matrix([0])])
            sage: A([1]).is_nilpotent()
            True"""
    @overload
    def is_zerodivisor(self) -> Any:
        """FiniteDimensionalAlgebraElement.is_zerodivisor(self)

        File: /build/sagemath/src/sage/src/sage/algebras/finite_dimensional_algebras/finite_dimensional_algebra_element.pyx (starting at line 620)

        Return ``True`` if ``self`` is a left or right zero-divisor.

        EXAMPLES::

            sage: C = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0], [0,1]]),
            ....:                                   Matrix([[0,1], [0,0]])])
            sage: C([1,0]).is_zerodivisor()
            False
            sage: C([0,1]).is_zerodivisor()
            True"""
    @overload
    def is_zerodivisor(self) -> Any:
        """FiniteDimensionalAlgebraElement.is_zerodivisor(self)

        File: /build/sagemath/src/sage/src/sage/algebras/finite_dimensional_algebras/finite_dimensional_algebra_element.pyx (starting at line 620)

        Return ``True`` if ``self`` is a left or right zero-divisor.

        EXAMPLES::

            sage: C = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0], [0,1]]),
            ....:                                   Matrix([[0,1], [0,0]])])
            sage: C([1,0]).is_zerodivisor()
            False
            sage: C([0,1]).is_zerodivisor()
            True"""
    @overload
    def is_zerodivisor(self) -> Any:
        """FiniteDimensionalAlgebraElement.is_zerodivisor(self)

        File: /build/sagemath/src/sage/src/sage/algebras/finite_dimensional_algebras/finite_dimensional_algebra_element.pyx (starting at line 620)

        Return ``True`` if ``self`` is a left or right zero-divisor.

        EXAMPLES::

            sage: C = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0], [0,1]]),
            ....:                                   Matrix([[0,1], [0,0]])])
            sage: C([1,0]).is_zerodivisor()
            False
            sage: C([0,1]).is_zerodivisor()
            True"""
    @overload
    def left_matrix(self) -> Any:
        """FiniteDimensionalAlgebraElement.left_matrix(self)

        File: /build/sagemath/src/sage/src/sage/algebras/finite_dimensional_algebras/finite_dimensional_algebra_element.pyx (starting at line 266)

        Return the matrix for multiplication by ``self`` from the left.

        EXAMPLES::

            sage: C = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0,0], [0,0,0], [0,0,0]]),
            ....:                                   Matrix([[0,1,0], [0,0,0], [0,0,0]]),
            ....:                                   Matrix([[0,0,0], [0,1,0], [0,0,1]])])
            sage: C([1,2,0]).left_matrix()
            [1 0 0]
            [0 1 0]
            [0 2 0]"""
    @overload
    def left_matrix(self) -> Any:
        """FiniteDimensionalAlgebraElement.left_matrix(self)

        File: /build/sagemath/src/sage/src/sage/algebras/finite_dimensional_algebras/finite_dimensional_algebra_element.pyx (starting at line 266)

        Return the matrix for multiplication by ``self`` from the left.

        EXAMPLES::

            sage: C = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0,0], [0,0,0], [0,0,0]]),
            ....:                                   Matrix([[0,1,0], [0,0,0], [0,0,0]]),
            ....:                                   Matrix([[0,0,0], [0,1,0], [0,0,1]])])
            sage: C([1,2,0]).left_matrix()
            [1 0 0]
            [0 1 0]
            [0 2 0]"""
    @overload
    def matrix(self) -> Any:
        """FiniteDimensionalAlgebraElement.matrix(self)

        File: /build/sagemath/src/sage/src/sage/algebras/finite_dimensional_algebras/finite_dimensional_algebra_element.pyx (starting at line 228)

        Return the matrix for multiplication by ``self`` from the right.

        EXAMPLES::

            sage: B = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0,0], [0,1,0], [0,0,0]]),
            ....:                                   Matrix([[0,1,0], [0,0,0], [0,0,0]]),
            ....:                                   Matrix([[0,0,0], [0,0,0], [0,0,1]])])
            sage: B(5).matrix()
            [5 0 0]
            [0 5 0]
            [0 0 5]"""
    @overload
    def matrix(self) -> Any:
        """FiniteDimensionalAlgebraElement.matrix(self)

        File: /build/sagemath/src/sage/src/sage/algebras/finite_dimensional_algebras/finite_dimensional_algebra_element.pyx (starting at line 228)

        Return the matrix for multiplication by ``self`` from the right.

        EXAMPLES::

            sage: B = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0,0], [0,1,0], [0,0,0]]),
            ....:                                   Matrix([[0,1,0], [0,0,0], [0,0,0]]),
            ....:                                   Matrix([[0,0,0], [0,0,0], [0,0,1]])])
            sage: B(5).matrix()
            [5 0 0]
            [0 5 0]
            [0 0 5]"""
    @overload
    def minimal_polynomial(self) -> Any:
        """FiniteDimensionalAlgebraElement.minimal_polynomial(self)

        File: /build/sagemath/src/sage/src/sage/algebras/finite_dimensional_algebras/finite_dimensional_algebra_element.pyx (starting at line 657)

        Return the minimal polynomial of ``self``.

        EXAMPLES::

            sage: B = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0,0], [0,1,0], [0,0,0]]),
            ....:                                   Matrix([[0,1,0], [0,0,0], [0,0,0]]),
            ....:                                   Matrix([[0,0,0], [0,0,0], [0,0,1]])])
            sage: B(0).minimal_polynomial()                                             # needs sage.libs.pari
            x
            sage: b = B.random_element()
            sage: f = b.minimal_polynomial(); f  # random                               # needs sage.libs.pari
            x^3 + 1/2*x^2 - 7/16*x + 1/16
            sage: f(b) == 0                                                             # needs sage.libs.pari
            True"""
    @overload
    def minimal_polynomial(self) -> Any:
        """FiniteDimensionalAlgebraElement.minimal_polynomial(self)

        File: /build/sagemath/src/sage/src/sage/algebras/finite_dimensional_algebras/finite_dimensional_algebra_element.pyx (starting at line 657)

        Return the minimal polynomial of ``self``.

        EXAMPLES::

            sage: B = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0,0], [0,1,0], [0,0,0]]),
            ....:                                   Matrix([[0,1,0], [0,0,0], [0,0,0]]),
            ....:                                   Matrix([[0,0,0], [0,0,0], [0,0,1]])])
            sage: B(0).minimal_polynomial()                                             # needs sage.libs.pari
            x
            sage: b = B.random_element()
            sage: f = b.minimal_polynomial(); f  # random                               # needs sage.libs.pari
            x^3 + 1/2*x^2 - 7/16*x + 1/16
            sage: f(b) == 0                                                             # needs sage.libs.pari
            True"""
    @overload
    def minimal_polynomial(self) -> Any:
        """FiniteDimensionalAlgebraElement.minimal_polynomial(self)

        File: /build/sagemath/src/sage/src/sage/algebras/finite_dimensional_algebras/finite_dimensional_algebra_element.pyx (starting at line 657)

        Return the minimal polynomial of ``self``.

        EXAMPLES::

            sage: B = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0,0], [0,1,0], [0,0,0]]),
            ....:                                   Matrix([[0,1,0], [0,0,0], [0,0,0]]),
            ....:                                   Matrix([[0,0,0], [0,0,0], [0,0,1]])])
            sage: B(0).minimal_polynomial()                                             # needs sage.libs.pari
            x
            sage: b = B.random_element()
            sage: f = b.minimal_polynomial(); f  # random                               # needs sage.libs.pari
            x^3 + 1/2*x^2 - 7/16*x + 1/16
            sage: f(b) == 0                                                             # needs sage.libs.pari
            True"""
    @overload
    def monomial_coefficients(self, boolcopy=...) -> dict:
        """FiniteDimensionalAlgebraElement.monomial_coefficients(self, bool copy=True) -> dict

        File: /build/sagemath/src/sage/src/sage/algebras/finite_dimensional_algebras/finite_dimensional_algebra_element.pyx (starting at line 244)

        Return a dictionary whose keys are indices of basis elements in
        the support of ``self`` and whose values are the corresponding
        coefficients.

        INPUT:

        - ``copy`` -- ignored

        EXAMPLES::

            sage: B = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0], [0,1]]),
            ....:                                   Matrix([[0,1], [-1,0]])])
            sage: elt = B(Matrix([[1,1], [-1,1]]))
            sage: elt.monomial_coefficients()
            {0: 1, 1: 1}
            sage: B.one().monomial_coefficients()
            {0: 1}"""
    @overload
    def monomial_coefficients(self) -> Any:
        """FiniteDimensionalAlgebraElement.monomial_coefficients(self, bool copy=True) -> dict

        File: /build/sagemath/src/sage/src/sage/algebras/finite_dimensional_algebras/finite_dimensional_algebra_element.pyx (starting at line 244)

        Return a dictionary whose keys are indices of basis elements in
        the support of ``self`` and whose values are the corresponding
        coefficients.

        INPUT:

        - ``copy`` -- ignored

        EXAMPLES::

            sage: B = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0], [0,1]]),
            ....:                                   Matrix([[0,1], [-1,0]])])
            sage: elt = B(Matrix([[1,1], [-1,1]]))
            sage: elt.monomial_coefficients()
            {0: 1, 1: 1}
            sage: B.one().monomial_coefficients()
            {0: 1}"""
    @overload
    def monomial_coefficients(self) -> Any:
        """FiniteDimensionalAlgebraElement.monomial_coefficients(self, bool copy=True) -> dict

        File: /build/sagemath/src/sage/src/sage/algebras/finite_dimensional_algebras/finite_dimensional_algebra_element.pyx (starting at line 244)

        Return a dictionary whose keys are indices of basis elements in
        the support of ``self`` and whose values are the corresponding
        coefficients.

        INPUT:

        - ``copy`` -- ignored

        EXAMPLES::

            sage: B = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0], [0,1]]),
            ....:                                   Matrix([[0,1], [-1,0]])])
            sage: elt = B(Matrix([[1,1], [-1,1]]))
            sage: elt.monomial_coefficients()
            {0: 1, 1: 1}
            sage: B.one().monomial_coefficients()
            {0: 1}"""
    @overload
    def vector(self) -> Any:
        """FiniteDimensionalAlgebraElement.vector(self)

        File: /build/sagemath/src/sage/src/sage/algebras/finite_dimensional_algebras/finite_dimensional_algebra_element.pyx (starting at line 211)

        Return ``self`` as a vector.

        EXAMPLES::

            sage: B = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0,0], [0,1,0], [0,0,0]]),
            ....:                                   Matrix([[0,1,0], [0,0,0], [0,0,0]]),
            ....:                                   Matrix([[0,0,0], [0,0,0], [0,0,1]])])
            sage: B(5).vector()
            (5, 0, 5)"""
    @overload
    def vector(self) -> Any:
        """FiniteDimensionalAlgebraElement.vector(self)

        File: /build/sagemath/src/sage/src/sage/algebras/finite_dimensional_algebras/finite_dimensional_algebra_element.pyx (starting at line 211)

        Return ``self`` as a vector.

        EXAMPLES::

            sage: B = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0,0], [0,1,0], [0,0,0]]),
            ....:                                   Matrix([[0,1,0], [0,0,0], [0,0,0]]),
            ....:                                   Matrix([[0,0,0], [0,0,0], [0,0,1]])])
            sage: B(5).vector()
            (5, 0, 5)"""
    def __getitem__(self, m) -> Any:
        """FiniteDimensionalAlgebraElement.__getitem__(self, m)

        File: /build/sagemath/src/sage/src/sage/algebras/finite_dimensional_algebras/finite_dimensional_algebra_element.pyx (starting at line 357)

        Return the `m`-th coefficient of ``self``.

        EXAMPLES::

            sage: A = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0,0], [0,1,0], [0,0,0]]),
            ....:                                   Matrix([[0,1,0], [0,0,0], [0,0,0]]),
            ....:                                   Matrix([[0,0,0], [0,0,0], [0,0,1]])])
            sage: A([2,1/4,3])[2]
            3"""
    def __hash__(self) -> Any:
        """FiniteDimensionalAlgebraElement.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/algebras/finite_dimensional_algebras/finite_dimensional_algebra_element.pyx (starting at line 340)

        Return the hash value for ``self``.

        EXAMPLES::

            sage: A = FiniteDimensionalAlgebra(GF(3), [Matrix([[1,0], [0,1]]),
            ....:                                      Matrix([[0,1], [0,0]])])
            sage: a = A([1,2])
            sage: b = A([2,3])
            sage: hash(a) == hash(A([1,2]))
            True
            sage: hash(a) == hash(b)
            False"""
    def __invert__(self) -> Any:
        """FiniteDimensionalAlgebraElement.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/algebras/finite_dimensional_algebras/finite_dimensional_algebra_element.pyx (starting at line 516)

        TESTS::

            sage: C = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0], [0,1]]),
            ....:                                   Matrix([[0,1], [-1,0]])])
            sage: x = C([1,2])
            sage: y = ~x; y                 # indirect doctest
            1/5*e0 - 2/5*e1
            sage: x*y
            e0
            sage: C.one()
            e0"""
    def __len__(self) -> Any:
        """FiniteDimensionalAlgebraElement.__len__(self)

        File: /build/sagemath/src/sage/src/sage/algebras/finite_dimensional_algebras/finite_dimensional_algebra_element.pyx (starting at line 371)

        Return the number of coefficients of ``self``,
        including the zero coefficients.

        EXAMPLES::

            sage: A = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0,0], [0,1,0], [0,0,0]]),
            ....:                                   Matrix([[0,1,0], [0,0,0], [0,0,0]]),
            ....:                                   Matrix([[0,0,0], [0,0,0], [0,0,1]])])
            sage: len(A([2,1/4,3]))
            3
            sage: len(A([2,0,3/4]))
            3"""
    def __pow__(self, n, m) -> Any:
        """FiniteDimensionalAlgebraElement.__pow__(self, n, m)

        File: /build/sagemath/src/sage/src/sage/algebras/finite_dimensional_algebras/finite_dimensional_algebra_element.pyx (starting at line 491)

        Return ``self`` raised to the power ``n``.

        EXAMPLES::

            sage: B = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0,0], [0,1,0], [0,0,0]]),
            ....:                                   Matrix([[0,1,0], [0,0,0], [0,0,0]]),
            ....:                                   Matrix([[0,0,0], [0,0,0], [0,0,1]])])
            sage: b = B([2,3,4])
            sage: b^6
            64*e0 + 576*e1 + 4096*e2"""
    def __reduce__(self) -> Any:
        """FiniteDimensionalAlgebraElement.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/algebras/finite_dimensional_algebras/finite_dimensional_algebra_element.pyx (starting at line 136)

        TESTS::

            sage: B = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0,0], [0,1,0], [0,0,0]]),
            ....:                                   Matrix([[1,1,0], [0,1,1], [0,1,1]]),
            ....:                                   Matrix([[0,0,1], [0,1,0], [1,0,0]])])
            sage: x = B([1,2,3])
            sage: loads(dumps(x)) == x      # indirect doctest
            True
            sage: loads(dumps(x)) is x
            False"""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
