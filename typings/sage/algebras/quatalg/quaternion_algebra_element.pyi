import _cython_3_2_1
import sage.structure.element
from sage.matrix.constructor import matrix as matrix
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

unpickle_QuaternionAlgebraElement_generic_v0: _cython_3_2_1.cython_function_or_method
unpickle_QuaternionAlgebraElement_number_field_v0: _cython_3_2_1.cython_function_or_method
unpickle_QuaternionAlgebraElement_rational_field_v0: _cython_3_2_1.cython_function_or_method

class QuaternionAlgebraElement_abstract(sage.structure.element.AlgebraElement):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def coefficient_tuple(self) -> Any:
        """QuaternionAlgebraElement_abstract.coefficient_tuple(self)

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 644)

        Return 4-tuple of coefficients of this quaternion.

        EXAMPLES::

            sage: K.<x> = QQ['x']
            sage: Q.<i,j,k> = QuaternionAlgebra(Frac(K),-5,-2)
            sage: a = 1/2*x^2 + 2/3*x*i - 3/4*j + 5/7*k
            sage: type(a)
            <class 'sage.algebras.quatalg.quaternion_algebra_element.QuaternionAlgebraElement_generic'>
            sage: a.coefficient_tuple()
            (1/2*x^2, 2/3*x, -3/4, 5/7)"""
    @overload
    def coefficient_tuple(self) -> Any:
        """QuaternionAlgebraElement_abstract.coefficient_tuple(self)

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 644)

        Return 4-tuple of coefficients of this quaternion.

        EXAMPLES::

            sage: K.<x> = QQ['x']
            sage: Q.<i,j,k> = QuaternionAlgebra(Frac(K),-5,-2)
            sage: a = 1/2*x^2 + 2/3*x*i - 3/4*j + 5/7*k
            sage: type(a)
            <class 'sage.algebras.quatalg.quaternion_algebra_element.QuaternionAlgebraElement_generic'>
            sage: a.coefficient_tuple()
            (1/2*x^2, 2/3*x, -3/4, 5/7)"""
    def conjugate(self) -> Any:
        '''QuaternionAlgebraElement_abstract.conjugate(self)

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 415)

        Return the conjugate of the quaternion: if `\\theta = x + yi + zj + wk`,
        return `x - yi - zj - wk`; that is, return theta.reduced_trace() - theta.

        EXAMPLES::

            sage: A.<i,j,k> = QuaternionAlgebra(QQ,-5,-2)
            sage: a = 3*i - j + 2
            sage: type(a)
            <class \'sage.algebras.quatalg.quaternion_algebra_element.QuaternionAlgebraElement_rational_field\'>
            sage: a.conjugate()
            2 - 3*i + j

        The "universal" test::

            sage: K.<x,y,z,w,a,b> = QQ[]
            sage: Q.<i,j,k> = QuaternionAlgebra(a,b)
            sage: theta = x+y*i+z*j+w*k
            sage: theta.conjugate()
            x + (-y)*i + (-z)*j + (-w)*k'''
    @overload
    def is_constant(self) -> bool:
        """QuaternionAlgebraElement_abstract.is_constant(self) -> bool

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 223)

        Return ``True`` if this quaternion is constant, i.e., has no `i`, `j`,
        or `k` term.

        OUTPUT: boolean

        EXAMPLES::

            sage: A.<i,j,k> = QuaternionAlgebra(-1,-2)
            sage: A(1).is_constant()
            True
            sage: A(1+i).is_constant()
            False
            sage: A(i).is_constant()
            False"""
    @overload
    def is_constant(self) -> Any:
        """QuaternionAlgebraElement_abstract.is_constant(self) -> bool

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 223)

        Return ``True`` if this quaternion is constant, i.e., has no `i`, `j`,
        or `k` term.

        OUTPUT: boolean

        EXAMPLES::

            sage: A.<i,j,k> = QuaternionAlgebra(-1,-2)
            sage: A(1).is_constant()
            True
            sage: A(1+i).is_constant()
            False
            sage: A(i).is_constant()
            False"""
    @overload
    def is_constant(self) -> Any:
        """QuaternionAlgebraElement_abstract.is_constant(self) -> bool

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 223)

        Return ``True`` if this quaternion is constant, i.e., has no `i`, `j`,
        or `k` term.

        OUTPUT: boolean

        EXAMPLES::

            sage: A.<i,j,k> = QuaternionAlgebra(-1,-2)
            sage: A(1).is_constant()
            True
            sage: A(1+i).is_constant()
            False
            sage: A(i).is_constant()
            False"""
    @overload
    def is_constant(self) -> Any:
        """QuaternionAlgebraElement_abstract.is_constant(self) -> bool

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 223)

        Return ``True`` if this quaternion is constant, i.e., has no `i`, `j`,
        or `k` term.

        OUTPUT: boolean

        EXAMPLES::

            sage: A.<i,j,k> = QuaternionAlgebra(-1,-2)
            sage: A(1).is_constant()
            True
            sage: A(1+i).is_constant()
            False
            sage: A(i).is_constant()
            False"""
    @overload
    def matrix(self, action=...) -> Any:
        """QuaternionAlgebraElement_abstract.matrix(self, action='right')

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 586)

        Return the matrix of right or left multiplication of ``self`` on
        the basis for the ambient quaternion algebra.

        In particular, if action is ``'right'`` (the default), returns the
        matrix of the mapping sending ``x`` to ``x*self``.

        INPUT:

        - ``action`` -- (default: ``'right'``) ``'right'`` or ``'left'``

        OUTPUT: a matrix

        EXAMPLES::

            sage: Q.<i,j,k> = QuaternionAlgebra(-3,-19)
            sage: a = 2/3 -1/2*i + 3/5*j - 4/3*k
            sage: a.matrix()
            [  2/3  -1/2   3/5  -4/3]
            [  3/2   2/3     4   3/5]
            [-57/5 -76/3   2/3   1/2]
            [   76 -57/5  -3/2   2/3]
            sage: a.matrix() == a.matrix(action='right')
            True
            sage: a.matrix(action='left')
            [  2/3  -1/2   3/5  -4/3]
            [  3/2   2/3    -4  -3/5]
            [-57/5  76/3   2/3  -1/2]
            [   76  57/5   3/2   2/3]
            sage: (i*a,j*a,k*a)
            (3/2 + 2/3*i + 4*j + 3/5*k, -57/5 - 76/3*i + 2/3*j + 1/2*k, 76 - 57/5*i - 3/2*j + 2/3*k)
            sage: a.matrix(action='foo')
            Traceback (most recent call last):
            ...
            ValueError: action must be either 'left' or 'right'

        We test over a more generic base field::

            sage: K.<x> = QQ['x']
            sage: Q.<i,j,k> = QuaternionAlgebra(Frac(K),-5,-2)
            sage: a = 1/2*x^2 + 2/3*x*i - 3/4*j + 5/7*k
            sage: type(a)
            <class 'sage.algebras.quatalg.quaternion_algebra_element.QuaternionAlgebraElement_generic'>
            sage: a.matrix()
            [1/2*x^2   2/3*x    -3/4     5/7]
            [-10/3*x 1/2*x^2   -25/7    -3/4]
            [    3/2    10/7 1/2*x^2  -2/3*x]
            [  -50/7     3/2  10/3*x 1/2*x^2]"""
    @overload
    def matrix(self) -> Any:
        """QuaternionAlgebraElement_abstract.matrix(self, action='right')

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 586)

        Return the matrix of right or left multiplication of ``self`` on
        the basis for the ambient quaternion algebra.

        In particular, if action is ``'right'`` (the default), returns the
        matrix of the mapping sending ``x`` to ``x*self``.

        INPUT:

        - ``action`` -- (default: ``'right'``) ``'right'`` or ``'left'``

        OUTPUT: a matrix

        EXAMPLES::

            sage: Q.<i,j,k> = QuaternionAlgebra(-3,-19)
            sage: a = 2/3 -1/2*i + 3/5*j - 4/3*k
            sage: a.matrix()
            [  2/3  -1/2   3/5  -4/3]
            [  3/2   2/3     4   3/5]
            [-57/5 -76/3   2/3   1/2]
            [   76 -57/5  -3/2   2/3]
            sage: a.matrix() == a.matrix(action='right')
            True
            sage: a.matrix(action='left')
            [  2/3  -1/2   3/5  -4/3]
            [  3/2   2/3    -4  -3/5]
            [-57/5  76/3   2/3  -1/2]
            [   76  57/5   3/2   2/3]
            sage: (i*a,j*a,k*a)
            (3/2 + 2/3*i + 4*j + 3/5*k, -57/5 - 76/3*i + 2/3*j + 1/2*k, 76 - 57/5*i - 3/2*j + 2/3*k)
            sage: a.matrix(action='foo')
            Traceback (most recent call last):
            ...
            ValueError: action must be either 'left' or 'right'

        We test over a more generic base field::

            sage: K.<x> = QQ['x']
            sage: Q.<i,j,k> = QuaternionAlgebra(Frac(K),-5,-2)
            sage: a = 1/2*x^2 + 2/3*x*i - 3/4*j + 5/7*k
            sage: type(a)
            <class 'sage.algebras.quatalg.quaternion_algebra_element.QuaternionAlgebraElement_generic'>
            sage: a.matrix()
            [1/2*x^2   2/3*x    -3/4     5/7]
            [-10/3*x 1/2*x^2   -25/7    -3/4]
            [    3/2    10/7 1/2*x^2  -2/3*x]
            [  -50/7     3/2  10/3*x 1/2*x^2]"""
    @overload
    def matrix(self, action=...) -> Any:
        """QuaternionAlgebraElement_abstract.matrix(self, action='right')

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 586)

        Return the matrix of right or left multiplication of ``self`` on
        the basis for the ambient quaternion algebra.

        In particular, if action is ``'right'`` (the default), returns the
        matrix of the mapping sending ``x`` to ``x*self``.

        INPUT:

        - ``action`` -- (default: ``'right'``) ``'right'`` or ``'left'``

        OUTPUT: a matrix

        EXAMPLES::

            sage: Q.<i,j,k> = QuaternionAlgebra(-3,-19)
            sage: a = 2/3 -1/2*i + 3/5*j - 4/3*k
            sage: a.matrix()
            [  2/3  -1/2   3/5  -4/3]
            [  3/2   2/3     4   3/5]
            [-57/5 -76/3   2/3   1/2]
            [   76 -57/5  -3/2   2/3]
            sage: a.matrix() == a.matrix(action='right')
            True
            sage: a.matrix(action='left')
            [  2/3  -1/2   3/5  -4/3]
            [  3/2   2/3    -4  -3/5]
            [-57/5  76/3   2/3  -1/2]
            [   76  57/5   3/2   2/3]
            sage: (i*a,j*a,k*a)
            (3/2 + 2/3*i + 4*j + 3/5*k, -57/5 - 76/3*i + 2/3*j + 1/2*k, 76 - 57/5*i - 3/2*j + 2/3*k)
            sage: a.matrix(action='foo')
            Traceback (most recent call last):
            ...
            ValueError: action must be either 'left' or 'right'

        We test over a more generic base field::

            sage: K.<x> = QQ['x']
            sage: Q.<i,j,k> = QuaternionAlgebra(Frac(K),-5,-2)
            sage: a = 1/2*x^2 + 2/3*x*i - 3/4*j + 5/7*k
            sage: type(a)
            <class 'sage.algebras.quatalg.quaternion_algebra_element.QuaternionAlgebraElement_generic'>
            sage: a.matrix()
            [1/2*x^2   2/3*x    -3/4     5/7]
            [-10/3*x 1/2*x^2   -25/7    -3/4]
            [    3/2    10/7 1/2*x^2  -2/3*x]
            [  -50/7     3/2  10/3*x 1/2*x^2]"""
    @overload
    def matrix(self, action=...) -> Any:
        """QuaternionAlgebraElement_abstract.matrix(self, action='right')

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 586)

        Return the matrix of right or left multiplication of ``self`` on
        the basis for the ambient quaternion algebra.

        In particular, if action is ``'right'`` (the default), returns the
        matrix of the mapping sending ``x`` to ``x*self``.

        INPUT:

        - ``action`` -- (default: ``'right'``) ``'right'`` or ``'left'``

        OUTPUT: a matrix

        EXAMPLES::

            sage: Q.<i,j,k> = QuaternionAlgebra(-3,-19)
            sage: a = 2/3 -1/2*i + 3/5*j - 4/3*k
            sage: a.matrix()
            [  2/3  -1/2   3/5  -4/3]
            [  3/2   2/3     4   3/5]
            [-57/5 -76/3   2/3   1/2]
            [   76 -57/5  -3/2   2/3]
            sage: a.matrix() == a.matrix(action='right')
            True
            sage: a.matrix(action='left')
            [  2/3  -1/2   3/5  -4/3]
            [  3/2   2/3    -4  -3/5]
            [-57/5  76/3   2/3  -1/2]
            [   76  57/5   3/2   2/3]
            sage: (i*a,j*a,k*a)
            (3/2 + 2/3*i + 4*j + 3/5*k, -57/5 - 76/3*i + 2/3*j + 1/2*k, 76 - 57/5*i - 3/2*j + 2/3*k)
            sage: a.matrix(action='foo')
            Traceback (most recent call last):
            ...
            ValueError: action must be either 'left' or 'right'

        We test over a more generic base field::

            sage: K.<x> = QQ['x']
            sage: Q.<i,j,k> = QuaternionAlgebra(Frac(K),-5,-2)
            sage: a = 1/2*x^2 + 2/3*x*i - 3/4*j + 5/7*k
            sage: type(a)
            <class 'sage.algebras.quatalg.quaternion_algebra_element.QuaternionAlgebraElement_generic'>
            sage: a.matrix()
            [1/2*x^2   2/3*x    -3/4     5/7]
            [-10/3*x 1/2*x^2   -25/7    -3/4]
            [    3/2    10/7 1/2*x^2  -2/3*x]
            [  -50/7     3/2  10/3*x 1/2*x^2]"""
    @overload
    def matrix(self, action=...) -> Any:
        """QuaternionAlgebraElement_abstract.matrix(self, action='right')

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 586)

        Return the matrix of right or left multiplication of ``self`` on
        the basis for the ambient quaternion algebra.

        In particular, if action is ``'right'`` (the default), returns the
        matrix of the mapping sending ``x`` to ``x*self``.

        INPUT:

        - ``action`` -- (default: ``'right'``) ``'right'`` or ``'left'``

        OUTPUT: a matrix

        EXAMPLES::

            sage: Q.<i,j,k> = QuaternionAlgebra(-3,-19)
            sage: a = 2/3 -1/2*i + 3/5*j - 4/3*k
            sage: a.matrix()
            [  2/3  -1/2   3/5  -4/3]
            [  3/2   2/3     4   3/5]
            [-57/5 -76/3   2/3   1/2]
            [   76 -57/5  -3/2   2/3]
            sage: a.matrix() == a.matrix(action='right')
            True
            sage: a.matrix(action='left')
            [  2/3  -1/2   3/5  -4/3]
            [  3/2   2/3    -4  -3/5]
            [-57/5  76/3   2/3  -1/2]
            [   76  57/5   3/2   2/3]
            sage: (i*a,j*a,k*a)
            (3/2 + 2/3*i + 4*j + 3/5*k, -57/5 - 76/3*i + 2/3*j + 1/2*k, 76 - 57/5*i - 3/2*j + 2/3*k)
            sage: a.matrix(action='foo')
            Traceback (most recent call last):
            ...
            ValueError: action must be either 'left' or 'right'

        We test over a more generic base field::

            sage: K.<x> = QQ['x']
            sage: Q.<i,j,k> = QuaternionAlgebra(Frac(K),-5,-2)
            sage: a = 1/2*x^2 + 2/3*x*i - 3/4*j + 5/7*k
            sage: type(a)
            <class 'sage.algebras.quatalg.quaternion_algebra_element.QuaternionAlgebraElement_generic'>
            sage: a.matrix()
            [1/2*x^2   2/3*x    -3/4     5/7]
            [-10/3*x 1/2*x^2   -25/7    -3/4]
            [    3/2    10/7 1/2*x^2  -2/3*x]
            [  -50/7     3/2  10/3*x 1/2*x^2]"""
    @overload
    def matrix(self) -> Any:
        """QuaternionAlgebraElement_abstract.matrix(self, action='right')

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 586)

        Return the matrix of right or left multiplication of ``self`` on
        the basis for the ambient quaternion algebra.

        In particular, if action is ``'right'`` (the default), returns the
        matrix of the mapping sending ``x`` to ``x*self``.

        INPUT:

        - ``action`` -- (default: ``'right'``) ``'right'`` or ``'left'``

        OUTPUT: a matrix

        EXAMPLES::

            sage: Q.<i,j,k> = QuaternionAlgebra(-3,-19)
            sage: a = 2/3 -1/2*i + 3/5*j - 4/3*k
            sage: a.matrix()
            [  2/3  -1/2   3/5  -4/3]
            [  3/2   2/3     4   3/5]
            [-57/5 -76/3   2/3   1/2]
            [   76 -57/5  -3/2   2/3]
            sage: a.matrix() == a.matrix(action='right')
            True
            sage: a.matrix(action='left')
            [  2/3  -1/2   3/5  -4/3]
            [  3/2   2/3    -4  -3/5]
            [-57/5  76/3   2/3  -1/2]
            [   76  57/5   3/2   2/3]
            sage: (i*a,j*a,k*a)
            (3/2 + 2/3*i + 4*j + 3/5*k, -57/5 - 76/3*i + 2/3*j + 1/2*k, 76 - 57/5*i - 3/2*j + 2/3*k)
            sage: a.matrix(action='foo')
            Traceback (most recent call last):
            ...
            ValueError: action must be either 'left' or 'right'

        We test over a more generic base field::

            sage: K.<x> = QQ['x']
            sage: Q.<i,j,k> = QuaternionAlgebra(Frac(K),-5,-2)
            sage: a = 1/2*x^2 + 2/3*x*i - 3/4*j + 5/7*k
            sage: type(a)
            <class 'sage.algebras.quatalg.quaternion_algebra_element.QuaternionAlgebraElement_generic'>
            sage: a.matrix()
            [1/2*x^2   2/3*x    -3/4     5/7]
            [-10/3*x 1/2*x^2   -25/7    -3/4]
            [    3/2    10/7 1/2*x^2  -2/3*x]
            [  -50/7     3/2  10/3*x 1/2*x^2]"""
    @overload
    def pair(self, right) -> Any:
        """QuaternionAlgebraElement_abstract.pair(self, right)

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 660)

        Return the result of pairing ``self`` and ``right``, which should both
        be elements of a quaternion algebra.  The pairing is
        ``(x,y) = (x.conjugate()*y).reduced_trace()``.

        INPUT:

        - ``right`` -- quaternion

        EXAMPLES::

            sage: A.<i,j,k>=QuaternionAlgebra(-1,-2)
            sage: (1+i+j-2*k).pair(2/3+5*i-3*j+k)
            -26/3
            sage: x = 1+i+j-2*k; y = 2/3+5*i-3*j+k
            sage: x.pair(y)
            -26/3
            sage: y.pair(x)
            -26/3
            sage: (x.conjugate()*y).reduced_trace()
            -26/3"""
    @overload
    def pair(self, y) -> Any:
        """QuaternionAlgebraElement_abstract.pair(self, right)

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 660)

        Return the result of pairing ``self`` and ``right``, which should both
        be elements of a quaternion algebra.  The pairing is
        ``(x,y) = (x.conjugate()*y).reduced_trace()``.

        INPUT:

        - ``right`` -- quaternion

        EXAMPLES::

            sage: A.<i,j,k>=QuaternionAlgebra(-1,-2)
            sage: (1+i+j-2*k).pair(2/3+5*i-3*j+k)
            -26/3
            sage: x = 1+i+j-2*k; y = 2/3+5*i-3*j+k
            sage: x.pair(y)
            -26/3
            sage: y.pair(x)
            -26/3
            sage: (x.conjugate()*y).reduced_trace()
            -26/3"""
    @overload
    def pair(self, x) -> Any:
        """QuaternionAlgebraElement_abstract.pair(self, right)

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 660)

        Return the result of pairing ``self`` and ``right``, which should both
        be elements of a quaternion algebra.  The pairing is
        ``(x,y) = (x.conjugate()*y).reduced_trace()``.

        INPUT:

        - ``right`` -- quaternion

        EXAMPLES::

            sage: A.<i,j,k>=QuaternionAlgebra(-1,-2)
            sage: (1+i+j-2*k).pair(2/3+5*i-3*j+k)
            -26/3
            sage: x = 1+i+j-2*k; y = 2/3+5*i-3*j+k
            sage: x.pair(y)
            -26/3
            sage: y.pair(x)
            -26/3
            sage: (x.conjugate()*y).reduced_trace()
            -26/3"""
    @overload
    def reduced_characteristic_polynomial(self, var=...) -> Any:
        """QuaternionAlgebraElement_abstract.reduced_characteristic_polynomial(self, var='x')

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 558)

        Return the reduced characteristic polynomial of this
        quaternion algebra element, which is `X^2 - tX + n`, where `t`
        is the reduced trace and `n` is the reduced norm.

        INPUT:

        - ``var`` -- string (default: ``'x'``); indeterminate of characteristic
          polynomial

        EXAMPLES::

            sage: A.<i,j,k>=QuaternionAlgebra(-1,-2)
            sage: i.reduced_characteristic_polynomial()
            x^2 + 1
            sage: j.reduced_characteristic_polynomial()
            x^2 + 2
            sage: (i+j).reduced_characteristic_polynomial()
            x^2 + 3
            sage: (2+j+k).reduced_trace()
            4
            sage: (2+j+k).reduced_characteristic_polynomial('T')
            T^2 - 4*T + 8"""
    @overload
    def reduced_characteristic_polynomial(self) -> Any:
        """QuaternionAlgebraElement_abstract.reduced_characteristic_polynomial(self, var='x')

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 558)

        Return the reduced characteristic polynomial of this
        quaternion algebra element, which is `X^2 - tX + n`, where `t`
        is the reduced trace and `n` is the reduced norm.

        INPUT:

        - ``var`` -- string (default: ``'x'``); indeterminate of characteristic
          polynomial

        EXAMPLES::

            sage: A.<i,j,k>=QuaternionAlgebra(-1,-2)
            sage: i.reduced_characteristic_polynomial()
            x^2 + 1
            sage: j.reduced_characteristic_polynomial()
            x^2 + 2
            sage: (i+j).reduced_characteristic_polynomial()
            x^2 + 3
            sage: (2+j+k).reduced_trace()
            4
            sage: (2+j+k).reduced_characteristic_polynomial('T')
            T^2 - 4*T + 8"""
    @overload
    def reduced_characteristic_polynomial(self) -> Any:
        """QuaternionAlgebraElement_abstract.reduced_characteristic_polynomial(self, var='x')

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 558)

        Return the reduced characteristic polynomial of this
        quaternion algebra element, which is `X^2 - tX + n`, where `t`
        is the reduced trace and `n` is the reduced norm.

        INPUT:

        - ``var`` -- string (default: ``'x'``); indeterminate of characteristic
          polynomial

        EXAMPLES::

            sage: A.<i,j,k>=QuaternionAlgebra(-1,-2)
            sage: i.reduced_characteristic_polynomial()
            x^2 + 1
            sage: j.reduced_characteristic_polynomial()
            x^2 + 2
            sage: (i+j).reduced_characteristic_polynomial()
            x^2 + 3
            sage: (2+j+k).reduced_trace()
            4
            sage: (2+j+k).reduced_characteristic_polynomial('T')
            T^2 - 4*T + 8"""
    @overload
    def reduced_characteristic_polynomial(self) -> Any:
        """QuaternionAlgebraElement_abstract.reduced_characteristic_polynomial(self, var='x')

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 558)

        Return the reduced characteristic polynomial of this
        quaternion algebra element, which is `X^2 - tX + n`, where `t`
        is the reduced trace and `n` is the reduced norm.

        INPUT:

        - ``var`` -- string (default: ``'x'``); indeterminate of characteristic
          polynomial

        EXAMPLES::

            sage: A.<i,j,k>=QuaternionAlgebra(-1,-2)
            sage: i.reduced_characteristic_polynomial()
            x^2 + 1
            sage: j.reduced_characteristic_polynomial()
            x^2 + 2
            sage: (i+j).reduced_characteristic_polynomial()
            x^2 + 3
            sage: (2+j+k).reduced_trace()
            4
            sage: (2+j+k).reduced_characteristic_polynomial('T')
            T^2 - 4*T + 8"""
    def reduced_norm(self) -> Any:
        """QuaternionAlgebraElement_abstract.reduced_norm(self)

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 454)

        Return the reduced norm of self: if `\\theta = x + yi + zj +
        wk`, then `\\theta` has reduced norm `x^2 - ay^2 - bz^2 +
        abw^2`.

        EXAMPLES::

            sage: K.<x,y,z,w,a,b> = QQ[]
            sage: Q.<i,j,k> = QuaternionAlgebra(a,b)
            sage: theta = x+y*i+z*j+w*k
            sage: theta.reduced_norm()
            w^2*a*b - y^2*a - z^2*b + x^2"""
    def reduced_trace(self) -> Any:
        """QuaternionAlgebraElement_abstract.reduced_trace(self)

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 439)

        Return the reduced trace of self: if `\\theta = x + yi + zj +
        wk`, then `\\theta` has reduced trace `2x`.

        EXAMPLES::

            sage: K.<x,y,z,w,a,b> = QQ[]
            sage: Q.<i,j,k> = QuaternionAlgebra(a,b)
            sage: theta = x+y*i+z*j+w*k
            sage: theta.reduced_trace()
            2*x"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __float__(self) -> Any:
        """QuaternionAlgebraElement_abstract.__float__(self)

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 262)

        Try to coerce this quaternion to a Python float.

        EXAMPLES::

            sage: A.<i,j,k>=QuaternionAlgebra(-1,-2)
            sage: float(A(-3/2))
            -1.5
            sage: float(A(-3))
            -3.0
            sage: float(-3 + i)
            Traceback (most recent call last):
            ...
            TypeError"""
    def __hash__(self) -> Any:
        """QuaternionAlgebraElement_abstract.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 196)

        TESTS::

            sage: from itertools import product
            sage: for K in [QQ, QuadraticField(2), AA, Frac(QQ['x'])]:
            ....:     Q.<i,j,k> = QuaternionAlgebra(K,-5,-2)
            ....:     assert hash(Q.one()) == hash(K.one())
            ....:     assert hash(Q(2)) == hash(K(2))
            ....:     elts = []
            ....:     for (x,y,z,w) in product([K(0), K(1), K(2), K(-1)], repeat=4):
            ....:         elts.append(x + y*i + z*j + w*k)
            ....:     assert len(set(map(hash, elts))) == len(elts)"""
    def __int__(self) -> Any:
        """QuaternionAlgebraElement_abstract.__int__(self)

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 242)

        Try to coerce this quaternion to a Python int.

        EXAMPLES::

            sage: A.<i,j,k>=QuaternionAlgebra(-1,-2)
            sage: int(A(-3))
            -3
            sage: int(A(-3/2))
            -1
            sage: int(-3 + i)
            Traceback (most recent call last):
            ...
            TypeError"""
    def __invert__(self) -> Any:
        """QuaternionAlgebraElement_abstract.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 472)

        Return the inverse of ``self``.

        EXAMPLES::

            sage: Q.<i,j,k> = QuaternionAlgebra(QQ,-7,-13)
            sage: theta = 1/3 - 2/3*i + 4/19*j - 17/3*k
            sage: (1/theta) * theta
            1
            sage: type(theta)
            <class 'sage.algebras.quatalg.quaternion_algebra_element.QuaternionAlgebraElement_rational_field'>
            sage: 1/Q(0)
            Traceback (most recent call last):
            ...
            ZeroDivisionError: rational division by zero

        Note that the quaternion algebra need not be a division
        algebra, in which case we can get a ZeroDivisionException::

            sage: Q.<i,j,k> = QuaternionAlgebra(QQ,4,9)
            sage: theta = 2-i
            sage: theta.reduced_norm()
            0
            sage: 1/theta
            Traceback (most recent call last):
            ...
            ZeroDivisionError: rational division by zero

        The ``universal`` test:

            sage: K.<x,y,z,w,a,b> = QQ[]
            sage: Q.<i,j,k> = QuaternionAlgebra(a,b)
            sage: theta = x+y*i+z*j+w*k
            sage: 1/theta == theta.conjugate()/theta.reduced_norm()
            True"""

class QuaternionAlgebraElement_generic(QuaternionAlgebraElement_abstract):
    """QuaternionAlgebraElement_generic(parent, v, bool check=True)

    File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 710)

    TESTS:

    Test operations on quaternions over a base ring that is not a field::

        sage: A.<t> = LaurentPolynomialRing(GF(3))
        sage: B = QuaternionAlgebra(A, -1, t)
        sage: i, j, k = B.gens()
        sage: i*j
        k
        sage: (j + k).reduced_norm()
        t

    Inverting an element is currently only possible if its reduced
    norm is a unit::

        sage: ~k
        (t^-1)*k
        sage: ~(i + j)
        Traceback (most recent call last):
        ...
        TypeError: unsupported operand parent(s) for *: 'Fraction Field of Univariate Polynomial Ring in t over Finite Field of size 3' and 'Quaternion Algebra (2, t) with base ring Univariate Laurent Polynomial Ring in t over Finite Field of size 3'

    We test pickling::

        sage: R.<x> = Frac(QQ['x']); Q.<i,j,k> = QuaternionAlgebra(R,-5*x,-2)
        sage: theta = x + i*x^3 + j*x^2 + k*x
        sage: theta == loads(dumps(theta))
        True"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, v, boolcheck=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 741)

                Create a quaternion over a general base ring.

                EXAMPLES::

                    sage: K.<x> = Frac(QQ['x']); Q.<i,j,k> = QuaternionAlgebra(K,-5,-2)
                    sage: sage.algebras.quatalg.quaternion_algebra_element.QuaternionAlgebraElement_generic(Q, (x,1,-7,2/3*x^3))
                    x + i + (-7)*j + 2/3*x^3*k
        """
    def __getitem__(self, inti) -> Any:
        """QuaternionAlgebraElement_generic.__getitem__(self, int i)

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 757)

        EXAMPLES::

            sage: Q.<i,j,k> = QuaternionAlgebra(Frac(QQ['x']),-5,-2)
            sage: theta = 1/2 + 2/3*i - 3/4*j + 5/7*k
            sage: type(theta)
            <class 'sage.algebras.quatalg.quaternion_algebra_element.QuaternionAlgebraElement_generic'>
            sage: list(theta)
            [1/2, 2/3, -3/4, 5/7]"""
    def __reduce__(self) -> Any:
        """QuaternionAlgebraElement_generic.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 779)

        Used for pickling.

        TESTS::

            sage: K.<x> = Frac(QQ['x']); Q.<i,j,k> = QuaternionAlgebra(K,-5,-2)
            sage: theta = 1/x + x*i - (x+1)*j + 2/(3*x^3+5)*k
            sage: loads(dumps(theta)) == theta
            True
            sage: type(theta)
            <class 'sage.algebras.quatalg.quaternion_algebra_element.QuaternionAlgebraElement_generic'>"""

class QuaternionAlgebraElement_number_field(QuaternionAlgebraElement_abstract):
    """QuaternionAlgebraElement_number_field(parent, v, bool check=True)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, v, boolcheck=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 1704)

                EXAMPLES::

                    sage: K.<a> = QQ[2^(1/3)]; Q.<i,j,k> = QuaternionAlgebra(K,-a,a+1)          # needs sage.symbolic
                    sage: Q([a,-2/3,a^2-1/2,a*2])           # implicit doctest                  # needs sage.symbolic
                    a + (-2/3)*i + (a^2 - 1/2)*j + 2*a*k
        """
    def __getitem__(self, inti) -> Any:
        """QuaternionAlgebraElement_number_field.__getitem__(self, int i)

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 1748)

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: K.<a> = QQ[2^(1/3)]; Q.<i,j,k> = QuaternionAlgebra(K,-a,a+1)
            sage: Q([a,-2/3,a^2-1/2,a*2])
            a + (-2/3)*i + (a^2 - 1/2)*j + 2*a*k
            sage: x = Q([a,-2/3,a^2-1/2,a*2])
            sage: type(x)
            <class 'sage.algebras.quatalg.quaternion_algebra_element.QuaternionAlgebraElement_number_field'>
            sage: x[0]
            a
            sage: x[1]
            -2/3
            sage: x[2]
            a^2 - 1/2
            sage: x[3]
            2*a
            sage: list(x)
            [a, -2/3, a^2 - 1/2, 2*a]"""
    @overload
    def __reduce__(self) -> Any:
        """QuaternionAlgebraElement_number_field.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 1790)

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: K.<a> = QQ[2^(1/3)]; Q.<i,j,k> = QuaternionAlgebra(K, -3, a)
            sage: z = (i+j+k+a)^2; z
            a^2 + 4*a - 3 + 2*a*i + 2*a*j + 2*a*k
            sage: f, t = z.__reduce__()
            sage: f(*t)
            a^2 + 4*a - 3 + 2*a*i + 2*a*j + 2*a*k
            sage: loads(dumps(z)) == z
            True"""
    @overload
    def __reduce__(self) -> Any:
        """QuaternionAlgebraElement_number_field.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 1790)

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: K.<a> = QQ[2^(1/3)]; Q.<i,j,k> = QuaternionAlgebra(K, -3, a)
            sage: z = (i+j+k+a)^2; z
            a^2 + 4*a - 3 + 2*a*i + 2*a*j + 2*a*k
            sage: f, t = z.__reduce__()
            sage: f(*t)
            a^2 + 4*a - 3 + 2*a*i + 2*a*j + 2*a*k
            sage: loads(dumps(z)) == z
            True"""

class QuaternionAlgebraElement_rational_field(QuaternionAlgebraElement_abstract):
    """QuaternionAlgebraElement_rational_field(parent, v, bool check=True)

    File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 883)

    TESTS:

    We test pickling::

        sage: Q.<i,j,k> = QuaternionAlgebra(QQ,-5,-2)
        sage: i + j + k == loads(dumps(i+j+k))
        True"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, v, boolcheck=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 1028)

                Setup element data from parent and coordinates.

                EXAMPLES::

                    sage: A.<i,j,k>=QuaternionAlgebra(-4,-5)
                    sage: A(2/3)
                    2/3
                    sage: type(A(2/3))
                    <class 'sage.algebras.quatalg.quaternion_algebra_element.QuaternionAlgebraElement_rational_field'>

                    sage: A([-1/2,-10/3,-2/3,-4/5])     # implicit doctest
                    -1/2 - 10/3*i - 2/3*j - 4/5*k
                    sage: A(vector([1,2/3,3/4,4/5]))
                    1 + 2/3*i + 3/4*j + 4/5*k

                ::

                    sage: QA = QuaternionAlgebra(QQ, -1, -1)
                    sage: foo = QA(3.0); foo
                    3
                    sage: parent(foo)
                    Quaternion Algebra (-1, -1) with base ring Rational Field
                    sage: foo[0]
                    3
                    sage: parent(foo[0])
                    Rational Field
        """
    @overload
    def coefficient_tuple(self) -> Any:
        """QuaternionAlgebraElement_rational_field.coefficient_tuple(self)

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 1568)

        Return 4-tuple of rational numbers which are the coefficients of this quaternion.

        EXAMPLES::

            sage: A.<i,j,k> = QuaternionAlgebra(-1,-2)
            sage: (2/3 + 3/5*i + 4/3*j - 5/7*k).coefficient_tuple()
            (2/3, 3/5, 4/3, -5/7)"""
    @overload
    def coefficient_tuple(self) -> Any:
        """QuaternionAlgebraElement_rational_field.coefficient_tuple(self)

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 1568)

        Return 4-tuple of rational numbers which are the coefficients of this quaternion.

        EXAMPLES::

            sage: A.<i,j,k> = QuaternionAlgebra(-1,-2)
            sage: (2/3 + 3/5*i + 4/3*j - 5/7*k).coefficient_tuple()
            (2/3, 3/5, 4/3, -5/7)"""
    @overload
    def conjugate(self) -> Any:
        """QuaternionAlgebraElement_rational_field.conjugate(self)

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 1400)

        Return the conjugate of this quaternion.

        EXAMPLES::

            sage: A.<i,j,k> = QuaternionAlgebra(QQ,-5,-2)
            sage: a = 3*i - j + 2
            sage: type(a)
            <class 'sage.algebras.quatalg.quaternion_algebra_element.QuaternionAlgebraElement_rational_field'>
            sage: a.conjugate()
            2 - 3*i + j
            sage: b = 1 + 1/3*i + 1/5*j - 1/7*k
            sage: b.conjugate()
            1 - 1/3*i - 1/5*j + 1/7*k"""
    @overload
    def conjugate(self) -> Any:
        """QuaternionAlgebraElement_rational_field.conjugate(self)

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 1400)

        Return the conjugate of this quaternion.

        EXAMPLES::

            sage: A.<i,j,k> = QuaternionAlgebra(QQ,-5,-2)
            sage: a = 3*i - j + 2
            sage: type(a)
            <class 'sage.algebras.quatalg.quaternion_algebra_element.QuaternionAlgebraElement_rational_field'>
            sage: a.conjugate()
            2 - 3*i + j
            sage: b = 1 + 1/3*i + 1/5*j - 1/7*k
            sage: b.conjugate()
            1 - 1/3*i - 1/5*j + 1/7*k"""
    @overload
    def conjugate(self) -> Any:
        """QuaternionAlgebraElement_rational_field.conjugate(self)

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 1400)

        Return the conjugate of this quaternion.

        EXAMPLES::

            sage: A.<i,j,k> = QuaternionAlgebra(QQ,-5,-2)
            sage: a = 3*i - j + 2
            sage: type(a)
            <class 'sage.algebras.quatalg.quaternion_algebra_element.QuaternionAlgebraElement_rational_field'>
            sage: a.conjugate()
            2 - 3*i + j
            sage: b = 1 + 1/3*i + 1/5*j - 1/7*k
            sage: b.conjugate()
            1 - 1/3*i - 1/5*j + 1/7*k"""
    @overload
    def denominator(self) -> Any:
        """QuaternionAlgebraElement_rational_field.denominator(self)

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 1491)

        Return the lowest common multiple of the denominators of the coefficients
        of i, j and k for this quaternion.

        EXAMPLES::

            sage: A = QuaternionAlgebra(QQ, -1, -1)
            sage: A.<i,j,k> = QuaternionAlgebra(QQ, -1, -1)
            sage: a = (1/2) + (1/5)*i + (5/12)*j + (1/13)*k
            sage: a
            1/2 + 1/5*i + 5/12*j + 1/13*k
            sage: a.denominator()
            780
            sage: lcm([2, 5, 12, 13])
            780
            sage: (a * a).denominator()
            608400
            sage: (a + a).denominator()
            390"""
    @overload
    def denominator(self) -> Any:
        """QuaternionAlgebraElement_rational_field.denominator(self)

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 1491)

        Return the lowest common multiple of the denominators of the coefficients
        of i, j and k for this quaternion.

        EXAMPLES::

            sage: A = QuaternionAlgebra(QQ, -1, -1)
            sage: A.<i,j,k> = QuaternionAlgebra(QQ, -1, -1)
            sage: a = (1/2) + (1/5)*i + (5/12)*j + (1/13)*k
            sage: a
            1/2 + 1/5*i + 5/12*j + 1/13*k
            sage: a.denominator()
            780
            sage: lcm([2, 5, 12, 13])
            780
            sage: (a * a).denominator()
            608400
            sage: (a + a).denominator()
            390"""
    @overload
    def denominator(self) -> Any:
        """QuaternionAlgebraElement_rational_field.denominator(self)

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 1491)

        Return the lowest common multiple of the denominators of the coefficients
        of i, j and k for this quaternion.

        EXAMPLES::

            sage: A = QuaternionAlgebra(QQ, -1, -1)
            sage: A.<i,j,k> = QuaternionAlgebra(QQ, -1, -1)
            sage: a = (1/2) + (1/5)*i + (5/12)*j + (1/13)*k
            sage: a
            1/2 + 1/5*i + 5/12*j + 1/13*k
            sage: a.denominator()
            780
            sage: lcm([2, 5, 12, 13])
            780
            sage: (a * a).denominator()
            608400
            sage: (a + a).denominator()
            390"""
    @overload
    def denominator(self) -> Any:
        """QuaternionAlgebraElement_rational_field.denominator(self)

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 1491)

        Return the lowest common multiple of the denominators of the coefficients
        of i, j and k for this quaternion.

        EXAMPLES::

            sage: A = QuaternionAlgebra(QQ, -1, -1)
            sage: A.<i,j,k> = QuaternionAlgebra(QQ, -1, -1)
            sage: a = (1/2) + (1/5)*i + (5/12)*j + (1/13)*k
            sage: a
            1/2 + 1/5*i + 5/12*j + 1/13*k
            sage: a.denominator()
            780
            sage: lcm([2, 5, 12, 13])
            780
            sage: (a * a).denominator()
            608400
            sage: (a + a).denominator()
            390"""
    @overload
    def denominator_and_integer_coefficient_tuple(self) -> Any:
        """QuaternionAlgebraElement_rational_field.denominator_and_integer_coefficient_tuple(self)

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 1516)

        Return 5-tuple d, x, y, z, w, where this rational quaternion
        is equal to `(x + yi + zj + wk)/d` and x, y, z, w do not share
        a common factor with d.

        OUTPUT: 5-tuple of Integers

        EXAMPLES::

            sage: A.<i,j,k>=QuaternionAlgebra(-1,-2)
            sage: (2 + 3*i + 4/3*j - 5*k).denominator_and_integer_coefficient_tuple()
            (3, 6, 9, 4, -15)"""
    @overload
    def denominator_and_integer_coefficient_tuple(self) -> Any:
        """QuaternionAlgebraElement_rational_field.denominator_and_integer_coefficient_tuple(self)

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 1516)

        Return 5-tuple d, x, y, z, w, where this rational quaternion
        is equal to `(x + yi + zj + wk)/d` and x, y, z, w do not share
        a common factor with d.

        OUTPUT: 5-tuple of Integers

        EXAMPLES::

            sage: A.<i,j,k>=QuaternionAlgebra(-1,-2)
            sage: (2 + 3*i + 4/3*j - 5*k).denominator_and_integer_coefficient_tuple()
            (3, 6, 9, 4, -15)"""
    @overload
    def integer_coefficient_tuple(self) -> Any:
        """QuaternionAlgebraElement_rational_field.integer_coefficient_tuple(self)

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 1544)

        Return the integer part of this quaternion, ignoring the common denominator.

        OUTPUT: 4-tuple of Integers

        EXAMPLES::

            sage: A.<i,j,k>=QuaternionAlgebra(-1,-2)
            sage: (2 + 3*i + 4/3*j - 5*k).integer_coefficient_tuple()
            (6, 9, 4, -15)"""
    @overload
    def integer_coefficient_tuple(self) -> Any:
        """QuaternionAlgebraElement_rational_field.integer_coefficient_tuple(self)

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 1544)

        Return the integer part of this quaternion, ignoring the common denominator.

        OUTPUT: 4-tuple of Integers

        EXAMPLES::

            sage: A.<i,j,k>=QuaternionAlgebra(-1,-2)
            sage: (2 + 3*i + 4/3*j - 5*k).integer_coefficient_tuple()
            (6, 9, 4, -15)"""
    @overload
    def is_constant(self) -> bool:
        """QuaternionAlgebraElement_rational_field.is_constant(self) -> bool

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 954)

        Return ``True`` if this quaternion is constant, i.e., has no `i`, `j`,
        or `k` term.

        OUTPUT: boolean

        EXAMPLES::

            sage: A.<i,j,k>=QuaternionAlgebra(-1,-2)
            sage: A(1/3).is_constant()
            True
            sage: A(-1).is_constant()
            True
            sage: (1+i).is_constant()
            False
            sage: j.is_constant()
            False"""
    @overload
    def is_constant(self) -> Any:
        """QuaternionAlgebraElement_rational_field.is_constant(self) -> bool

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 954)

        Return ``True`` if this quaternion is constant, i.e., has no `i`, `j`,
        or `k` term.

        OUTPUT: boolean

        EXAMPLES::

            sage: A.<i,j,k>=QuaternionAlgebra(-1,-2)
            sage: A(1/3).is_constant()
            True
            sage: A(-1).is_constant()
            True
            sage: (1+i).is_constant()
            False
            sage: j.is_constant()
            False"""
    @overload
    def is_constant(self) -> Any:
        """QuaternionAlgebraElement_rational_field.is_constant(self) -> bool

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 954)

        Return ``True`` if this quaternion is constant, i.e., has no `i`, `j`,
        or `k` term.

        OUTPUT: boolean

        EXAMPLES::

            sage: A.<i,j,k>=QuaternionAlgebra(-1,-2)
            sage: A(1/3).is_constant()
            True
            sage: A(-1).is_constant()
            True
            sage: (1+i).is_constant()
            False
            sage: j.is_constant()
            False"""
    @overload
    def is_constant(self) -> Any:
        """QuaternionAlgebraElement_rational_field.is_constant(self) -> bool

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 954)

        Return ``True`` if this quaternion is constant, i.e., has no `i`, `j`,
        or `k` term.

        OUTPUT: boolean

        EXAMPLES::

            sage: A.<i,j,k>=QuaternionAlgebra(-1,-2)
            sage: A(1/3).is_constant()
            True
            sage: A(-1).is_constant()
            True
            sage: (1+i).is_constant()
            False
            sage: j.is_constant()
            False"""
    @overload
    def is_constant(self) -> Any:
        """QuaternionAlgebraElement_rational_field.is_constant(self) -> bool

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 954)

        Return ``True`` if this quaternion is constant, i.e., has no `i`, `j`,
        or `k` term.

        OUTPUT: boolean

        EXAMPLES::

            sage: A.<i,j,k>=QuaternionAlgebra(-1,-2)
            sage: A(1/3).is_constant()
            True
            sage: A(-1).is_constant()
            True
            sage: (1+i).is_constant()
            False
            sage: j.is_constant()
            False"""
    @overload
    def reduced_norm(self) -> Any:
        """QuaternionAlgebraElement_rational_field.reduced_norm(self)

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 1359)

        Return the reduced norm of ``self``.

        Given a quaternion `x+yi+zj+wk`, this is `x^2 - ay^2 - bz^2 + abw^2`.

        EXAMPLES::

            sage: K.<i,j,k> = QuaternionAlgebra(QQ, -5, -2)
            sage: i.reduced_norm()
            5
            sage: j.reduced_norm()
            2
            sage: a = 1/3 + 1/5*i + 1/7*j + k
            sage: a.reduced_norm()
            22826/2205"""
    @overload
    def reduced_norm(self) -> Any:
        """QuaternionAlgebraElement_rational_field.reduced_norm(self)

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 1359)

        Return the reduced norm of ``self``.

        Given a quaternion `x+yi+zj+wk`, this is `x^2 - ay^2 - bz^2 + abw^2`.

        EXAMPLES::

            sage: K.<i,j,k> = QuaternionAlgebra(QQ, -5, -2)
            sage: i.reduced_norm()
            5
            sage: j.reduced_norm()
            2
            sage: a = 1/3 + 1/5*i + 1/7*j + k
            sage: a.reduced_norm()
            22826/2205"""
    @overload
    def reduced_norm(self) -> Any:
        """QuaternionAlgebraElement_rational_field.reduced_norm(self)

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 1359)

        Return the reduced norm of ``self``.

        Given a quaternion `x+yi+zj+wk`, this is `x^2 - ay^2 - bz^2 + abw^2`.

        EXAMPLES::

            sage: K.<i,j,k> = QuaternionAlgebra(QQ, -5, -2)
            sage: i.reduced_norm()
            5
            sage: j.reduced_norm()
            2
            sage: a = 1/3 + 1/5*i + 1/7*j + k
            sage: a.reduced_norm()
            22826/2205"""
    @overload
    def reduced_norm(self) -> Any:
        """QuaternionAlgebraElement_rational_field.reduced_norm(self)

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 1359)

        Return the reduced norm of ``self``.

        Given a quaternion `x+yi+zj+wk`, this is `x^2 - ay^2 - bz^2 + abw^2`.

        EXAMPLES::

            sage: K.<i,j,k> = QuaternionAlgebra(QQ, -5, -2)
            sage: i.reduced_norm()
            5
            sage: j.reduced_norm()
            2
            sage: a = 1/3 + 1/5*i + 1/7*j + k
            sage: a.reduced_norm()
            22826/2205"""
    @overload
    def reduced_trace(self) -> Any:
        """QuaternionAlgebraElement_rational_field.reduced_trace(self)

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 1431)

        Return the reduced trace of ``self``.

        This is `2x` if ``self`` is `x+iy+zj+wk`.

        EXAMPLES::

            sage: K.<i,j,k> = QuaternionAlgebra(QQ, -5, -2)
            sage: i.reduced_trace()
            0
            sage: j.reduced_trace()
            0
            sage: a = 1/3 + 1/5*i + 1/7*j + k
            sage: a.reduced_trace()
            2/3"""
    @overload
    def reduced_trace(self) -> Any:
        """QuaternionAlgebraElement_rational_field.reduced_trace(self)

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 1431)

        Return the reduced trace of ``self``.

        This is `2x` if ``self`` is `x+iy+zj+wk`.

        EXAMPLES::

            sage: K.<i,j,k> = QuaternionAlgebra(QQ, -5, -2)
            sage: i.reduced_trace()
            0
            sage: j.reduced_trace()
            0
            sage: a = 1/3 + 1/5*i + 1/7*j + k
            sage: a.reduced_trace()
            2/3"""
    @overload
    def reduced_trace(self) -> Any:
        """QuaternionAlgebraElement_rational_field.reduced_trace(self)

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 1431)

        Return the reduced trace of ``self``.

        This is `2x` if ``self`` is `x+iy+zj+wk`.

        EXAMPLES::

            sage: K.<i,j,k> = QuaternionAlgebra(QQ, -5, -2)
            sage: i.reduced_trace()
            0
            sage: j.reduced_trace()
            0
            sage: a = 1/3 + 1/5*i + 1/7*j + k
            sage: a.reduced_trace()
            2/3"""
    @overload
    def reduced_trace(self) -> Any:
        """QuaternionAlgebraElement_rational_field.reduced_trace(self)

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 1431)

        Return the reduced trace of ``self``.

        This is `2x` if ``self`` is `x+iy+zj+wk`.

        EXAMPLES::

            sage: K.<i,j,k> = QuaternionAlgebra(QQ, -5, -2)
            sage: i.reduced_trace()
            0
            sage: j.reduced_trace()
            0
            sage: a = 1/3 + 1/5*i + 1/7*j + k
            sage: a.reduced_trace()
            2/3"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __getitem__(self, inti) -> Any:
        """QuaternionAlgebraElement_rational_field.__getitem__(self, int i)

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 1106)

        TESTS::

            sage: Q.<i,j,k> = QuaternionAlgebra(QQ,-5,-2)
            sage: theta = 1/2 + 2/3*i - 3/4*j + 5/7*k
            sage: type(theta)
            <class 'sage.algebras.quatalg.quaternion_algebra_element.QuaternionAlgebraElement_rational_field'>
            sage: list(theta)
            [1/2, 2/3, -3/4, 5/7]"""
    def __reduce__(self) -> Any:
        """QuaternionAlgebraElement_rational_field.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/algebras/quatalg/quaternion_algebra_element.pyx (starting at line 1132)

        Used for pickling.

        TESTS::

            sage: K.<x> = QQ[]
            sage: Q.<i,j,k> = QuaternionAlgebra(Frac(K),-5,-19)
            sage: theta = 1/2 + 2/3*i - 3/4*j + 5/7*k
            sage: type(theta)
            <class 'sage.algebras.quatalg.quaternion_algebra_element.QuaternionAlgebraElement_generic'>
            sage: loads(dumps(theta)) == theta
            True"""
