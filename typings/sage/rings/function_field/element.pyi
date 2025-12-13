import _cython_3_2_1
import sage.structure.element
from sage.categories.function_fields import FunctionFields as FunctionFields
from sage.misc.cachefunc import cached_method as cached_method
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

is_FunctionFieldElement: _cython_3_2_1.cython_function_or_method
make_FunctionFieldElement: _cython_3_2_1.cython_function_or_method

class FunctionFieldElement(sage.structure.element.FieldElement):
    """File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 117)

        Abstract base class for function field elements.

        EXAMPLES::

            sage: t = FunctionField(QQ,'t').gen()
            sage: isinstance(t, sage.rings.function_field.element.FunctionFieldElement)
            True
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def characteristic_polynomial(self, *args, **kwds) -> Any:
        """FunctionFieldElement.characteristic_polynomial(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 597)

        Return the characteristic polynomial of the element. Give an optional
        input string to name the variable in the characteristic polynomial.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: x.characteristic_polynomial('W')                                      # needs sage.modules
            W - x

            sage: # needs sage.rings.function_field
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3); R.<z> = L[]
            sage: M.<z> = L.extension(z^3 - y^2*z + x)
            sage: y.characteristic_polynomial('W')
            W^2 - x*W + 4*x^3
            sage: z.characteristic_polynomial('W')
            W^3 + (-x*y + 4*x^3)*W + x"""
    def charpoly(self, *args, **kwargs):
        """FunctionFieldElement.characteristic_polynomial(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 597)

        Return the characteristic polynomial of the element. Give an optional
        input string to name the variable in the characteristic polynomial.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: x.characteristic_polynomial('W')                                      # needs sage.modules
            W - x

            sage: # needs sage.rings.function_field
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3); R.<z> = L[]
            sage: M.<z> = L.extension(z^3 - y^2*z + x)
            sage: y.characteristic_polynomial('W')
            W^2 - x*W + 4*x^3
            sage: z.characteristic_polynomial('W')
            W^3 + (-x*y + 4*x^3)*W + x"""
    @overload
    def degree(self) -> Any:
        """FunctionFieldElement.degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 561)

        Return the max degree between the denominator and numerator.

        EXAMPLES::

            sage: FF.<t> = FunctionField(QQ)
            sage: f = (t^2 + 3) / (t^3 - 1/3); f
            (t^2 + 3)/(t^3 - 1/3)
            sage: f.degree()
            3

            sage: FF.<t> = FunctionField(QQ)
            sage: f = (t+8); f
            t + 8
            sage: f.degree()
            1

        TESTS::

            sage: FF.<t> = FunctionField(QQ)
            sage: f = FF(0); f
            0
            sage: f.degree()
            0
            sage: f = (t+1) / (t^2 - 1/3); f
            (t + 1)/(t^2 - 1/3)
            sage: f.degree()
            2
            sage: f = (t+1); f
            t + 1
            sage: f.degree()
            1"""
    @overload
    def degree(self) -> Any:
        """FunctionFieldElement.degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 561)

        Return the max degree between the denominator and numerator.

        EXAMPLES::

            sage: FF.<t> = FunctionField(QQ)
            sage: f = (t^2 + 3) / (t^3 - 1/3); f
            (t^2 + 3)/(t^3 - 1/3)
            sage: f.degree()
            3

            sage: FF.<t> = FunctionField(QQ)
            sage: f = (t+8); f
            t + 8
            sage: f.degree()
            1

        TESTS::

            sage: FF.<t> = FunctionField(QQ)
            sage: f = FF(0); f
            0
            sage: f.degree()
            0
            sage: f = (t+1) / (t^2 - 1/3); f
            (t + 1)/(t^2 - 1/3)
            sage: f.degree()
            2
            sage: f = (t+1); f
            t + 1
            sage: f.degree()
            1"""
    @overload
    def degree(self) -> Any:
        """FunctionFieldElement.degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 561)

        Return the max degree between the denominator and numerator.

        EXAMPLES::

            sage: FF.<t> = FunctionField(QQ)
            sage: f = (t^2 + 3) / (t^3 - 1/3); f
            (t^2 + 3)/(t^3 - 1/3)
            sage: f.degree()
            3

            sage: FF.<t> = FunctionField(QQ)
            sage: f = (t+8); f
            t + 8
            sage: f.degree()
            1

        TESTS::

            sage: FF.<t> = FunctionField(QQ)
            sage: f = FF(0); f
            0
            sage: f.degree()
            0
            sage: f = (t+1) / (t^2 - 1/3); f
            (t + 1)/(t^2 - 1/3)
            sage: f.degree()
            2
            sage: f = (t+1); f
            t + 1
            sage: f.degree()
            1"""
    @overload
    def degree(self) -> Any:
        """FunctionFieldElement.degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 561)

        Return the max degree between the denominator and numerator.

        EXAMPLES::

            sage: FF.<t> = FunctionField(QQ)
            sage: f = (t^2 + 3) / (t^3 - 1/3); f
            (t^2 + 3)/(t^3 - 1/3)
            sage: f.degree()
            3

            sage: FF.<t> = FunctionField(QQ)
            sage: f = (t+8); f
            t + 8
            sage: f.degree()
            1

        TESTS::

            sage: FF.<t> = FunctionField(QQ)
            sage: f = FF(0); f
            0
            sage: f.degree()
            0
            sage: f = (t+1) / (t^2 - 1/3); f
            (t + 1)/(t^2 - 1/3)
            sage: f.degree()
            2
            sage: f = (t+1); f
            t + 1
            sage: f.degree()
            1"""
    @overload
    def degree(self) -> Any:
        """FunctionFieldElement.degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 561)

        Return the max degree between the denominator and numerator.

        EXAMPLES::

            sage: FF.<t> = FunctionField(QQ)
            sage: f = (t^2 + 3) / (t^3 - 1/3); f
            (t^2 + 3)/(t^3 - 1/3)
            sage: f.degree()
            3

            sage: FF.<t> = FunctionField(QQ)
            sage: f = (t+8); f
            t + 8
            sage: f.degree()
            1

        TESTS::

            sage: FF.<t> = FunctionField(QQ)
            sage: f = FF(0); f
            0
            sage: f.degree()
            0
            sage: f = (t+1) / (t^2 - 1/3); f
            (t + 1)/(t^2 - 1/3)
            sage: f.degree()
            2
            sage: f = (t+1); f
            t + 1
            sage: f.degree()
            1"""
    @overload
    def degree(self) -> Any:
        """FunctionFieldElement.degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 561)

        Return the max degree between the denominator and numerator.

        EXAMPLES::

            sage: FF.<t> = FunctionField(QQ)
            sage: f = (t^2 + 3) / (t^3 - 1/3); f
            (t^2 + 3)/(t^3 - 1/3)
            sage: f.degree()
            3

            sage: FF.<t> = FunctionField(QQ)
            sage: f = (t+8); f
            t + 8
            sage: f.degree()
            1

        TESTS::

            sage: FF.<t> = FunctionField(QQ)
            sage: f = FF(0); f
            0
            sage: f.degree()
            0
            sage: f = (t+1) / (t^2 - 1/3); f
            (t + 1)/(t^2 - 1/3)
            sage: f.degree()
            2
            sage: f = (t+1); f
            t + 1
            sage: f.degree()
            1"""
    @overload
    def derivative(self) -> Any:
        """FunctionFieldElement.derivative(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 704)

        Return the derivative of the element.

        The derivative is with respect to the generator of the base rational
        function field, over which the function field is a separable extension.

        EXAMPLES::

            sage: K.<t> = FunctionField(QQ)
            sage: f = (t + 1) / (t^2 - 1/3)
            sage: f.derivative()                                                        # needs sage.modules
            (-t^2 - 2*t - 1/3)/(t^4 - 2/3*t^2 + 1/9)

            sage: K.<x> = FunctionField(GF(4)); _.<Y> = K[]                             # needs sage.rings.finite_rings
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)                                # needs sage.rings.finite_rings sage.rings.function_field
            sage: (y^3 + x).derivative()                                                # needs sage.rings.finite_rings sage.rings.function_field
            ((x^2 + 1)/x^2)*y + (x^4 + x^3 + 1)/x^3"""
    @overload
    def derivative(self) -> Any:
        """FunctionFieldElement.derivative(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 704)

        Return the derivative of the element.

        The derivative is with respect to the generator of the base rational
        function field, over which the function field is a separable extension.

        EXAMPLES::

            sage: K.<t> = FunctionField(QQ)
            sage: f = (t + 1) / (t^2 - 1/3)
            sage: f.derivative()                                                        # needs sage.modules
            (-t^2 - 2*t - 1/3)/(t^4 - 2/3*t^2 + 1/9)

            sage: K.<x> = FunctionField(GF(4)); _.<Y> = K[]                             # needs sage.rings.finite_rings
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)                                # needs sage.rings.finite_rings sage.rings.function_field
            sage: (y^3 + x).derivative()                                                # needs sage.rings.finite_rings sage.rings.function_field
            ((x^2 + 1)/x^2)*y + (x^4 + x^3 + 1)/x^3"""
    @overload
    def derivative(self) -> Any:
        """FunctionFieldElement.derivative(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 704)

        Return the derivative of the element.

        The derivative is with respect to the generator of the base rational
        function field, over which the function field is a separable extension.

        EXAMPLES::

            sage: K.<t> = FunctionField(QQ)
            sage: f = (t + 1) / (t^2 - 1/3)
            sage: f.derivative()                                                        # needs sage.modules
            (-t^2 - 2*t - 1/3)/(t^4 - 2/3*t^2 + 1/9)

            sage: K.<x> = FunctionField(GF(4)); _.<Y> = K[]                             # needs sage.rings.finite_rings
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)                                # needs sage.rings.finite_rings sage.rings.function_field
            sage: (y^3 + x).derivative()                                                # needs sage.rings.finite_rings sage.rings.function_field
            ((x^2 + 1)/x^2)*y + (x^4 + x^3 + 1)/x^3"""
    @overload
    def differential(self) -> Any:
        """FunctionFieldElement.differential(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 666)

        Return the differential `dx` where `x` is the element.

        EXAMPLES::

            sage: K.<t> = FunctionField(QQ)
            sage: f = 1 / t
            sage: f.differential()                                                      # needs sage.modules
            (-1/t^2) d(t)

            sage: K.<x> = FunctionField(GF(4)); _.<Y> = K[]                             # needs sage.rings.finite_rings
            sage: L.<y> = K.extension(Y^2 + Y + x +1/x)                                 # needs sage.rings.finite_rings sage.rings.function_field
            sage: (y^3 + x).differential()                                              # needs sage.rings.finite_rings sage.rings.function_field
            (((x^2 + 1)/x^2)*y + (x^4 + x^3 + 1)/x^3) d(x)

        TESTS:

        Verify that :issue:`27712` is resolved::

            sage: K.<x> = FunctionField(GF(31))
            sage: x.differential()                                                      # needs sage.modules
            d(x)

            sage: # needs sage.rings.function_field
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x)
            sage: R.<z> = L[]
            sage: M.<z> = L.extension(z^2 - y)
            sage: y.differential()
            (16/x*y) d(x)
            sage: z.differential()
            (8/x*z) d(x)"""
    @overload
    def differential(self) -> Any:
        """FunctionFieldElement.differential(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 666)

        Return the differential `dx` where `x` is the element.

        EXAMPLES::

            sage: K.<t> = FunctionField(QQ)
            sage: f = 1 / t
            sage: f.differential()                                                      # needs sage.modules
            (-1/t^2) d(t)

            sage: K.<x> = FunctionField(GF(4)); _.<Y> = K[]                             # needs sage.rings.finite_rings
            sage: L.<y> = K.extension(Y^2 + Y + x +1/x)                                 # needs sage.rings.finite_rings sage.rings.function_field
            sage: (y^3 + x).differential()                                              # needs sage.rings.finite_rings sage.rings.function_field
            (((x^2 + 1)/x^2)*y + (x^4 + x^3 + 1)/x^3) d(x)

        TESTS:

        Verify that :issue:`27712` is resolved::

            sage: K.<x> = FunctionField(GF(31))
            sage: x.differential()                                                      # needs sage.modules
            d(x)

            sage: # needs sage.rings.function_field
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x)
            sage: R.<z> = L[]
            sage: M.<z> = L.extension(z^2 - y)
            sage: y.differential()
            (16/x*y) d(x)
            sage: z.differential()
            (8/x*z) d(x)"""
    @overload
    def differential(self) -> Any:
        """FunctionFieldElement.differential(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 666)

        Return the differential `dx` where `x` is the element.

        EXAMPLES::

            sage: K.<t> = FunctionField(QQ)
            sage: f = 1 / t
            sage: f.differential()                                                      # needs sage.modules
            (-1/t^2) d(t)

            sage: K.<x> = FunctionField(GF(4)); _.<Y> = K[]                             # needs sage.rings.finite_rings
            sage: L.<y> = K.extension(Y^2 + Y + x +1/x)                                 # needs sage.rings.finite_rings sage.rings.function_field
            sage: (y^3 + x).differential()                                              # needs sage.rings.finite_rings sage.rings.function_field
            (((x^2 + 1)/x^2)*y + (x^4 + x^3 + 1)/x^3) d(x)

        TESTS:

        Verify that :issue:`27712` is resolved::

            sage: K.<x> = FunctionField(GF(31))
            sage: x.differential()                                                      # needs sage.modules
            d(x)

            sage: # needs sage.rings.function_field
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x)
            sage: R.<z> = L[]
            sage: M.<z> = L.extension(z^2 - y)
            sage: y.differential()
            (16/x*y) d(x)
            sage: z.differential()
            (8/x*z) d(x)"""
    @overload
    def differential(self) -> Any:
        """FunctionFieldElement.differential(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 666)

        Return the differential `dx` where `x` is the element.

        EXAMPLES::

            sage: K.<t> = FunctionField(QQ)
            sage: f = 1 / t
            sage: f.differential()                                                      # needs sage.modules
            (-1/t^2) d(t)

            sage: K.<x> = FunctionField(GF(4)); _.<Y> = K[]                             # needs sage.rings.finite_rings
            sage: L.<y> = K.extension(Y^2 + Y + x +1/x)                                 # needs sage.rings.finite_rings sage.rings.function_field
            sage: (y^3 + x).differential()                                              # needs sage.rings.finite_rings sage.rings.function_field
            (((x^2 + 1)/x^2)*y + (x^4 + x^3 + 1)/x^3) d(x)

        TESTS:

        Verify that :issue:`27712` is resolved::

            sage: K.<x> = FunctionField(GF(31))
            sage: x.differential()                                                      # needs sage.modules
            d(x)

            sage: # needs sage.rings.function_field
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x)
            sage: R.<z> = L[]
            sage: M.<z> = L.extension(z^2 - y)
            sage: y.differential()
            (16/x*y) d(x)
            sage: z.differential()
            (8/x*z) d(x)"""
    @overload
    def differential(self) -> Any:
        """FunctionFieldElement.differential(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 666)

        Return the differential `dx` where `x` is the element.

        EXAMPLES::

            sage: K.<t> = FunctionField(QQ)
            sage: f = 1 / t
            sage: f.differential()                                                      # needs sage.modules
            (-1/t^2) d(t)

            sage: K.<x> = FunctionField(GF(4)); _.<Y> = K[]                             # needs sage.rings.finite_rings
            sage: L.<y> = K.extension(Y^2 + Y + x +1/x)                                 # needs sage.rings.finite_rings sage.rings.function_field
            sage: (y^3 + x).differential()                                              # needs sage.rings.finite_rings sage.rings.function_field
            (((x^2 + 1)/x^2)*y + (x^4 + x^3 + 1)/x^3) d(x)

        TESTS:

        Verify that :issue:`27712` is resolved::

            sage: K.<x> = FunctionField(GF(31))
            sage: x.differential()                                                      # needs sage.modules
            d(x)

            sage: # needs sage.rings.function_field
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x)
            sage: R.<z> = L[]
            sage: M.<z> = L.extension(z^2 - y)
            sage: y.differential()
            (16/x*y) d(x)
            sage: z.differential()
            (8/x*z) d(x)"""
    @overload
    def differential(self) -> Any:
        """FunctionFieldElement.differential(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 666)

        Return the differential `dx` where `x` is the element.

        EXAMPLES::

            sage: K.<t> = FunctionField(QQ)
            sage: f = 1 / t
            sage: f.differential()                                                      # needs sage.modules
            (-1/t^2) d(t)

            sage: K.<x> = FunctionField(GF(4)); _.<Y> = K[]                             # needs sage.rings.finite_rings
            sage: L.<y> = K.extension(Y^2 + Y + x +1/x)                                 # needs sage.rings.finite_rings sage.rings.function_field
            sage: (y^3 + x).differential()                                              # needs sage.rings.finite_rings sage.rings.function_field
            (((x^2 + 1)/x^2)*y + (x^4 + x^3 + 1)/x^3) d(x)

        TESTS:

        Verify that :issue:`27712` is resolved::

            sage: K.<x> = FunctionField(GF(31))
            sage: x.differential()                                                      # needs sage.modules
            d(x)

            sage: # needs sage.rings.function_field
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x)
            sage: R.<z> = L[]
            sage: M.<z> = L.extension(z^2 - y)
            sage: y.differential()
            (16/x*y) d(x)
            sage: z.differential()
            (8/x*z) d(x)"""
    @overload
    def divisor(self) -> Any:
        """FunctionFieldElement.divisor(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 755)

        Return the divisor of the element.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(2))
            sage: f = 1/(x^3 + x^2 + x)
            sage: f.divisor()                                                           # needs sage.libs.pari sage.modules
            3*Place (1/x)
             - Place (x)
             - Place (x^2 + x + 1)

        ::

            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)                                # needs sage.rings.function_field
            sage: y.divisor()                                                           # needs sage.rings.function_field
            - Place (1/x, 1/x*y)
             - Place (x, x*y)
             + 2*Place (x + 1, x*y)"""
    @overload
    def divisor(self) -> Any:
        """FunctionFieldElement.divisor(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 755)

        Return the divisor of the element.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(2))
            sage: f = 1/(x^3 + x^2 + x)
            sage: f.divisor()                                                           # needs sage.libs.pari sage.modules
            3*Place (1/x)
             - Place (x)
             - Place (x^2 + x + 1)

        ::

            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)                                # needs sage.rings.function_field
            sage: y.divisor()                                                           # needs sage.rings.function_field
            - Place (1/x, 1/x*y)
             - Place (x, x*y)
             + 2*Place (x + 1, x*y)"""
    @overload
    def divisor(self) -> Any:
        """FunctionFieldElement.divisor(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 755)

        Return the divisor of the element.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(2))
            sage: f = 1/(x^3 + x^2 + x)
            sage: f.divisor()                                                           # needs sage.libs.pari sage.modules
            3*Place (1/x)
             - Place (x)
             - Place (x^2 + x + 1)

        ::

            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)                                # needs sage.rings.function_field
            sage: y.divisor()                                                           # needs sage.rings.function_field
            - Place (1/x, 1/x*y)
             - Place (x, x*y)
             + 2*Place (x + 1, x*y)"""
    @overload
    def divisor_of_poles(self) -> Any:
        """FunctionFieldElement.divisor_of_poles(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 812)

        Return the divisor of poles for the element.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(2))
            sage: f = 1/(x^3 + x^2 + x)
            sage: f.divisor_of_poles()                                                  # needs sage.libs.pari sage.modules
            Place (x)
             + Place (x^2 + x + 1)

        ::

            sage: K.<x> = FunctionField(GF(4)); _.<Y> = K[]                             # needs sage.rings.finite_rings
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)                                # needs sage.rings.finite_rings sage.rings.function_field
            sage: (x/y).divisor_of_poles()                                              # needs sage.rings.finite_rings sage.rings.function_field
            Place (1/x, 1/x*y) + 2*Place (x + 1, x*y)"""
    @overload
    def divisor_of_poles(self) -> Any:
        """FunctionFieldElement.divisor_of_poles(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 812)

        Return the divisor of poles for the element.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(2))
            sage: f = 1/(x^3 + x^2 + x)
            sage: f.divisor_of_poles()                                                  # needs sage.libs.pari sage.modules
            Place (x)
             + Place (x^2 + x + 1)

        ::

            sage: K.<x> = FunctionField(GF(4)); _.<Y> = K[]                             # needs sage.rings.finite_rings
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)                                # needs sage.rings.finite_rings sage.rings.function_field
            sage: (x/y).divisor_of_poles()                                              # needs sage.rings.finite_rings sage.rings.function_field
            Place (1/x, 1/x*y) + 2*Place (x + 1, x*y)"""
    @overload
    def divisor_of_poles(self) -> Any:
        """FunctionFieldElement.divisor_of_poles(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 812)

        Return the divisor of poles for the element.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(2))
            sage: f = 1/(x^3 + x^2 + x)
            sage: f.divisor_of_poles()                                                  # needs sage.libs.pari sage.modules
            Place (x)
             + Place (x^2 + x + 1)

        ::

            sage: K.<x> = FunctionField(GF(4)); _.<Y> = K[]                             # needs sage.rings.finite_rings
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)                                # needs sage.rings.finite_rings sage.rings.function_field
            sage: (x/y).divisor_of_poles()                                              # needs sage.rings.finite_rings sage.rings.function_field
            Place (1/x, 1/x*y) + 2*Place (x + 1, x*y)"""
    @overload
    def divisor_of_zeros(self) -> Any:
        """FunctionFieldElement.divisor_of_zeros(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 786)

        Return the divisor of zeros for the element.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(2))
            sage: f = 1/(x^3 + x^2 + x)
            sage: f.divisor_of_zeros()                                                  # needs sage.libs.pari sage.modules
            3*Place (1/x)

        ::

            sage: K.<x> = FunctionField(GF(4)); _.<Y> = K[]                             # needs sage.rings.finite_rings
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)                                # needs sage.rings.finite_rings sage.rings.function_field
            sage: (x/y).divisor_of_zeros()                                              # needs sage.rings.finite_rings sage.rings.function_field
            3*Place (x, x*y)"""
    @overload
    def divisor_of_zeros(self) -> Any:
        """FunctionFieldElement.divisor_of_zeros(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 786)

        Return the divisor of zeros for the element.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(2))
            sage: f = 1/(x^3 + x^2 + x)
            sage: f.divisor_of_zeros()                                                  # needs sage.libs.pari sage.modules
            3*Place (1/x)

        ::

            sage: K.<x> = FunctionField(GF(4)); _.<Y> = K[]                             # needs sage.rings.finite_rings
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)                                # needs sage.rings.finite_rings sage.rings.function_field
            sage: (x/y).divisor_of_zeros()                                              # needs sage.rings.finite_rings sage.rings.function_field
            3*Place (x, x*y)"""
    @overload
    def divisor_of_zeros(self) -> Any:
        """FunctionFieldElement.divisor_of_zeros(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 786)

        Return the divisor of zeros for the element.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(2))
            sage: f = 1/(x^3 + x^2 + x)
            sage: f.divisor_of_zeros()                                                  # needs sage.libs.pari sage.modules
            3*Place (1/x)

        ::

            sage: K.<x> = FunctionField(GF(4)); _.<Y> = K[]                             # needs sage.rings.finite_rings
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)                                # needs sage.rings.finite_rings sage.rings.function_field
            sage: (x/y).divisor_of_zeros()                                              # needs sage.rings.finite_rings sage.rings.function_field
            3*Place (x, x*y)"""
    @overload
    def evaluate(self, place) -> Any:
        """FunctionFieldElement.evaluate(self, place)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 909)

        Return the value of the element at the place.

        INPUT:

        - ``place`` -- a function field place

        OUTPUT:

        If the element is in the valuation ring at the place, then an element
        in the residue field at the place is returned. Otherwise, a
        :exc:`ValueError` is raised.

        EXAMPLES::

            sage: K.<t> = FunctionField(GF(5))
            sage: p = K.place_infinite()
            sage: f = 1/t^2 + 3
            sage: f.evaluate(p)
            3

        ::

            sage: # needs sage.rings.finite_rings sage.rings.function_field
            sage: K.<x> = FunctionField(GF(4)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: p, = L.places_infinite()
            sage: p, = L.places_infinite()
            sage: (y + x).evaluate(p)
            Traceback (most recent call last):
            ...
            ValueError: has a pole at the place
            sage: (y/x + 1).evaluate(p)
            1"""
    @overload
    def evaluate(self, p) -> Any:
        """FunctionFieldElement.evaluate(self, place)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 909)

        Return the value of the element at the place.

        INPUT:

        - ``place`` -- a function field place

        OUTPUT:

        If the element is in the valuation ring at the place, then an element
        in the residue field at the place is returned. Otherwise, a
        :exc:`ValueError` is raised.

        EXAMPLES::

            sage: K.<t> = FunctionField(GF(5))
            sage: p = K.place_infinite()
            sage: f = 1/t^2 + 3
            sage: f.evaluate(p)
            3

        ::

            sage: # needs sage.rings.finite_rings sage.rings.function_field
            sage: K.<x> = FunctionField(GF(4)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: p, = L.places_infinite()
            sage: p, = L.places_infinite()
            sage: (y + x).evaluate(p)
            Traceback (most recent call last):
            ...
            ValueError: has a pole at the place
            sage: (y/x + 1).evaluate(p)
            1"""
    @overload
    def evaluate(self, p) -> Any:
        """FunctionFieldElement.evaluate(self, place)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 909)

        Return the value of the element at the place.

        INPUT:

        - ``place`` -- a function field place

        OUTPUT:

        If the element is in the valuation ring at the place, then an element
        in the residue field at the place is returned. Otherwise, a
        :exc:`ValueError` is raised.

        EXAMPLES::

            sage: K.<t> = FunctionField(GF(5))
            sage: p = K.place_infinite()
            sage: f = 1/t^2 + 3
            sage: f.evaluate(p)
            3

        ::

            sage: # needs sage.rings.finite_rings sage.rings.function_field
            sage: K.<x> = FunctionField(GF(4)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: p, = L.places_infinite()
            sage: p, = L.places_infinite()
            sage: (y + x).evaluate(p)
            Traceback (most recent call last):
            ...
            ValueError: has a pole at the place
            sage: (y/x + 1).evaluate(p)
            1"""
    @overload
    def evaluate(self, p) -> Any:
        """FunctionFieldElement.evaluate(self, place)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 909)

        Return the value of the element at the place.

        INPUT:

        - ``place`` -- a function field place

        OUTPUT:

        If the element is in the valuation ring at the place, then an element
        in the residue field at the place is returned. Otherwise, a
        :exc:`ValueError` is raised.

        EXAMPLES::

            sage: K.<t> = FunctionField(GF(5))
            sage: p = K.place_infinite()
            sage: f = 1/t^2 + 3
            sage: f.evaluate(p)
            3

        ::

            sage: # needs sage.rings.finite_rings sage.rings.function_field
            sage: K.<x> = FunctionField(GF(4)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: p, = L.places_infinite()
            sage: p, = L.places_infinite()
            sage: (y + x).evaluate(p)
            Traceback (most recent call last):
            ...
            ValueError: has a pole at the place
            sage: (y/x + 1).evaluate(p)
            1"""
    def higher_derivative(self, i, separating_element=...) -> Any:
        """FunctionFieldElement.higher_derivative(self, i, separating_element=None)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 726)

        Return the `i`-th derivative of the element with respect to the
        separating element.

        INPUT:

        - ``i`` -- nonnegative integer

        - ``separating_element`` -- a separating element of the function field;
          the default is the generator of the rational function field

        EXAMPLES::

            sage: K.<t> = FunctionField(GF(2))
            sage: f = t^2
            sage: f.higher_derivative(2)                                                # needs sage.rings.function_field
            1

        ::

            sage: K.<x> = FunctionField(GF(4)); _.<Y> = K[]                             # needs sage.rings.finite_rings
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)                                # needs sage.rings.finite_rings sage.rings.function_field
            sage: (y^3 + x).higher_derivative(2)                                        # needs sage.rings.finite_rings sage.rings.function_field
            1/x^3*y + (x^6 + x^4 + x^3 + x^2 + x + 1)/x^5"""
    @overload
    def is_integral(self) -> Any:
        """FunctionFieldElement.is_integral(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 643)

        Determine if the element is integral over the maximal order of the base field.

        EXAMPLES::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3)
            sage: y.is_integral()
            True
            sage: (y/x).is_integral()
            True
            sage: (y/x)^2 - (y/x) + 4*x
            0
            sage: (y/x^2).is_integral()
            False
            sage: (y/x).minimal_polynomial('W')
            W^2 - W + 4*x"""
    @overload
    def is_integral(self) -> Any:
        """FunctionFieldElement.is_integral(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 643)

        Determine if the element is integral over the maximal order of the base field.

        EXAMPLES::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3)
            sage: y.is_integral()
            True
            sage: (y/x).is_integral()
            True
            sage: (y/x)^2 - (y/x) + 4*x
            0
            sage: (y/x^2).is_integral()
            False
            sage: (y/x).minimal_polynomial('W')
            W^2 - W + 4*x"""
    @overload
    def is_integral(self) -> Any:
        """FunctionFieldElement.is_integral(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 643)

        Determine if the element is integral over the maximal order of the base field.

        EXAMPLES::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3)
            sage: y.is_integral()
            True
            sage: (y/x).is_integral()
            True
            sage: (y/x)^2 - (y/x) + 4*x
            0
            sage: (y/x^2).is_integral()
            False
            sage: (y/x).minimal_polynomial('W')
            W^2 - W + 4*x"""
    @overload
    def is_integral(self) -> Any:
        """FunctionFieldElement.is_integral(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 643)

        Determine if the element is integral over the maximal order of the base field.

        EXAMPLES::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3)
            sage: y.is_integral()
            True
            sage: (y/x).is_integral()
            True
            sage: (y/x)^2 - (y/x) + 4*x
            0
            sage: (y/x^2).is_integral()
            False
            sage: (y/x).minimal_polynomial('W')
            W^2 - W + 4*x"""
    def is_nth_power(self, n) -> bool:
        """FunctionFieldElement.is_nth_power(self, n) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 955)

        Return whether this element is an ``n``-th power in the rational
        function field.

        INPUT:

        - ``n`` -- integer

        OUTPUT:

        Returns ``True`` if there is an element `a` in the function field such
        that this element equals `a^n`.

        .. SEEALSO::

            :meth:`nth_root`

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(3))
            sage: f = (x+1)/(x-1)
            sage: f.is_nth_power(2)
            False"""
    @overload
    def matrix(self, base=...) -> Any:
        """FunctionFieldElement.matrix(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 443)

        Return the matrix of multiplication by this element, interpreting this
        element as an element of a vector space over ``base``.

        INPUT:

        - ``base`` -- a function field (default: ``None``); if ``None``, then
          the matrix is formed over the base field of this function field

        EXAMPLES:

        A rational function field::

            sage: K.<t> = FunctionField(QQ)
            sage: t.matrix()                                                            # needs sage.modules
            [t]
            sage: (1/(t+1)).matrix()                                                    # needs sage.modules
            [1/(t + 1)]

        Now an example in a nontrivial extension of a rational function field::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3)
            sage: y.matrix()
            [     0      1]
            [-4*x^3      x]
            sage: y.matrix().charpoly('Z')
            Z^2 - x*Z + 4*x^3

        An example in a relative extension, where neither function
        field is rational::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3)
            sage: M.<T> = L[]
            sage: Z.<alpha> = L.extension(T^3 - y^2*T + x)
            sage: alpha.matrix()
            [          0           1           0]
            [          0           0           1]
            [         -x x*y - 4*x^3           0]
            sage: alpha.matrix(K)
            [           0            0            1            0            0            0]
            [           0            0            0            1            0            0]
            [           0            0            0            0            1            0]
            [           0            0            0            0            0            1]
            [          -x            0       -4*x^3            x            0            0]
            [           0           -x       -4*x^4 -4*x^3 + x^2            0            0]
            sage: alpha.matrix(Z)
            [alpha]

        We show that this matrix does indeed work as expected when making a
        vector space from a function field::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^5 - (x^3 + 2*x*y + 1/x))
            sage: V, from_V, to_V = L.vector_space()
            sage: y5 = to_V(y^5); y5
            ((x^4 + 1)/x, 2*x, 0, 0, 0)
            sage: y4y = to_V(y^4) * y.matrix(); y4y
            ((x^4 + 1)/x, 2*x, 0, 0, 0)
            sage: y5 == y4y
            True"""
    @overload
    def matrix(self) -> Any:
        """FunctionFieldElement.matrix(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 443)

        Return the matrix of multiplication by this element, interpreting this
        element as an element of a vector space over ``base``.

        INPUT:

        - ``base`` -- a function field (default: ``None``); if ``None``, then
          the matrix is formed over the base field of this function field

        EXAMPLES:

        A rational function field::

            sage: K.<t> = FunctionField(QQ)
            sage: t.matrix()                                                            # needs sage.modules
            [t]
            sage: (1/(t+1)).matrix()                                                    # needs sage.modules
            [1/(t + 1)]

        Now an example in a nontrivial extension of a rational function field::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3)
            sage: y.matrix()
            [     0      1]
            [-4*x^3      x]
            sage: y.matrix().charpoly('Z')
            Z^2 - x*Z + 4*x^3

        An example in a relative extension, where neither function
        field is rational::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3)
            sage: M.<T> = L[]
            sage: Z.<alpha> = L.extension(T^3 - y^2*T + x)
            sage: alpha.matrix()
            [          0           1           0]
            [          0           0           1]
            [         -x x*y - 4*x^3           0]
            sage: alpha.matrix(K)
            [           0            0            1            0            0            0]
            [           0            0            0            1            0            0]
            [           0            0            0            0            1            0]
            [           0            0            0            0            0            1]
            [          -x            0       -4*x^3            x            0            0]
            [           0           -x       -4*x^4 -4*x^3 + x^2            0            0]
            sage: alpha.matrix(Z)
            [alpha]

        We show that this matrix does indeed work as expected when making a
        vector space from a function field::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^5 - (x^3 + 2*x*y + 1/x))
            sage: V, from_V, to_V = L.vector_space()
            sage: y5 = to_V(y^5); y5
            ((x^4 + 1)/x, 2*x, 0, 0, 0)
            sage: y4y = to_V(y^4) * y.matrix(); y4y
            ((x^4 + 1)/x, 2*x, 0, 0, 0)
            sage: y5 == y4y
            True"""
    @overload
    def matrix(self) -> Any:
        """FunctionFieldElement.matrix(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 443)

        Return the matrix of multiplication by this element, interpreting this
        element as an element of a vector space over ``base``.

        INPUT:

        - ``base`` -- a function field (default: ``None``); if ``None``, then
          the matrix is formed over the base field of this function field

        EXAMPLES:

        A rational function field::

            sage: K.<t> = FunctionField(QQ)
            sage: t.matrix()                                                            # needs sage.modules
            [t]
            sage: (1/(t+1)).matrix()                                                    # needs sage.modules
            [1/(t + 1)]

        Now an example in a nontrivial extension of a rational function field::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3)
            sage: y.matrix()
            [     0      1]
            [-4*x^3      x]
            sage: y.matrix().charpoly('Z')
            Z^2 - x*Z + 4*x^3

        An example in a relative extension, where neither function
        field is rational::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3)
            sage: M.<T> = L[]
            sage: Z.<alpha> = L.extension(T^3 - y^2*T + x)
            sage: alpha.matrix()
            [          0           1           0]
            [          0           0           1]
            [         -x x*y - 4*x^3           0]
            sage: alpha.matrix(K)
            [           0            0            1            0            0            0]
            [           0            0            0            1            0            0]
            [           0            0            0            0            1            0]
            [           0            0            0            0            0            1]
            [          -x            0       -4*x^3            x            0            0]
            [           0           -x       -4*x^4 -4*x^3 + x^2            0            0]
            sage: alpha.matrix(Z)
            [alpha]

        We show that this matrix does indeed work as expected when making a
        vector space from a function field::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^5 - (x^3 + 2*x*y + 1/x))
            sage: V, from_V, to_V = L.vector_space()
            sage: y5 = to_V(y^5); y5
            ((x^4 + 1)/x, 2*x, 0, 0, 0)
            sage: y4y = to_V(y^4) * y.matrix(); y4y
            ((x^4 + 1)/x, 2*x, 0, 0, 0)
            sage: y5 == y4y
            True"""
    @overload
    def matrix(self) -> Any:
        """FunctionFieldElement.matrix(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 443)

        Return the matrix of multiplication by this element, interpreting this
        element as an element of a vector space over ``base``.

        INPUT:

        - ``base`` -- a function field (default: ``None``); if ``None``, then
          the matrix is formed over the base field of this function field

        EXAMPLES:

        A rational function field::

            sage: K.<t> = FunctionField(QQ)
            sage: t.matrix()                                                            # needs sage.modules
            [t]
            sage: (1/(t+1)).matrix()                                                    # needs sage.modules
            [1/(t + 1)]

        Now an example in a nontrivial extension of a rational function field::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3)
            sage: y.matrix()
            [     0      1]
            [-4*x^3      x]
            sage: y.matrix().charpoly('Z')
            Z^2 - x*Z + 4*x^3

        An example in a relative extension, where neither function
        field is rational::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3)
            sage: M.<T> = L[]
            sage: Z.<alpha> = L.extension(T^3 - y^2*T + x)
            sage: alpha.matrix()
            [          0           1           0]
            [          0           0           1]
            [         -x x*y - 4*x^3           0]
            sage: alpha.matrix(K)
            [           0            0            1            0            0            0]
            [           0            0            0            1            0            0]
            [           0            0            0            0            1            0]
            [           0            0            0            0            0            1]
            [          -x            0       -4*x^3            x            0            0]
            [           0           -x       -4*x^4 -4*x^3 + x^2            0            0]
            sage: alpha.matrix(Z)
            [alpha]

        We show that this matrix does indeed work as expected when making a
        vector space from a function field::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^5 - (x^3 + 2*x*y + 1/x))
            sage: V, from_V, to_V = L.vector_space()
            sage: y5 = to_V(y^5); y5
            ((x^4 + 1)/x, 2*x, 0, 0, 0)
            sage: y4y = to_V(y^4) * y.matrix(); y4y
            ((x^4 + 1)/x, 2*x, 0, 0, 0)
            sage: y5 == y4y
            True"""
    @overload
    def matrix(self) -> Any:
        """FunctionFieldElement.matrix(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 443)

        Return the matrix of multiplication by this element, interpreting this
        element as an element of a vector space over ``base``.

        INPUT:

        - ``base`` -- a function field (default: ``None``); if ``None``, then
          the matrix is formed over the base field of this function field

        EXAMPLES:

        A rational function field::

            sage: K.<t> = FunctionField(QQ)
            sage: t.matrix()                                                            # needs sage.modules
            [t]
            sage: (1/(t+1)).matrix()                                                    # needs sage.modules
            [1/(t + 1)]

        Now an example in a nontrivial extension of a rational function field::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3)
            sage: y.matrix()
            [     0      1]
            [-4*x^3      x]
            sage: y.matrix().charpoly('Z')
            Z^2 - x*Z + 4*x^3

        An example in a relative extension, where neither function
        field is rational::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3)
            sage: M.<T> = L[]
            sage: Z.<alpha> = L.extension(T^3 - y^2*T + x)
            sage: alpha.matrix()
            [          0           1           0]
            [          0           0           1]
            [         -x x*y - 4*x^3           0]
            sage: alpha.matrix(K)
            [           0            0            1            0            0            0]
            [           0            0            0            1            0            0]
            [           0            0            0            0            1            0]
            [           0            0            0            0            0            1]
            [          -x            0       -4*x^3            x            0            0]
            [           0           -x       -4*x^4 -4*x^3 + x^2            0            0]
            sage: alpha.matrix(Z)
            [alpha]

        We show that this matrix does indeed work as expected when making a
        vector space from a function field::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^5 - (x^3 + 2*x*y + 1/x))
            sage: V, from_V, to_V = L.vector_space()
            sage: y5 = to_V(y^5); y5
            ((x^4 + 1)/x, 2*x, 0, 0, 0)
            sage: y4y = to_V(y^4) * y.matrix(); y4y
            ((x^4 + 1)/x, 2*x, 0, 0, 0)
            sage: y5 == y4y
            True"""
    @overload
    def matrix(self) -> Any:
        """FunctionFieldElement.matrix(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 443)

        Return the matrix of multiplication by this element, interpreting this
        element as an element of a vector space over ``base``.

        INPUT:

        - ``base`` -- a function field (default: ``None``); if ``None``, then
          the matrix is formed over the base field of this function field

        EXAMPLES:

        A rational function field::

            sage: K.<t> = FunctionField(QQ)
            sage: t.matrix()                                                            # needs sage.modules
            [t]
            sage: (1/(t+1)).matrix()                                                    # needs sage.modules
            [1/(t + 1)]

        Now an example in a nontrivial extension of a rational function field::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3)
            sage: y.matrix()
            [     0      1]
            [-4*x^3      x]
            sage: y.matrix().charpoly('Z')
            Z^2 - x*Z + 4*x^3

        An example in a relative extension, where neither function
        field is rational::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3)
            sage: M.<T> = L[]
            sage: Z.<alpha> = L.extension(T^3 - y^2*T + x)
            sage: alpha.matrix()
            [          0           1           0]
            [          0           0           1]
            [         -x x*y - 4*x^3           0]
            sage: alpha.matrix(K)
            [           0            0            1            0            0            0]
            [           0            0            0            1            0            0]
            [           0            0            0            0            1            0]
            [           0            0            0            0            0            1]
            [          -x            0       -4*x^3            x            0            0]
            [           0           -x       -4*x^4 -4*x^3 + x^2            0            0]
            sage: alpha.matrix(Z)
            [alpha]

        We show that this matrix does indeed work as expected when making a
        vector space from a function field::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^5 - (x^3 + 2*x*y + 1/x))
            sage: V, from_V, to_V = L.vector_space()
            sage: y5 = to_V(y^5); y5
            ((x^4 + 1)/x, 2*x, 0, 0, 0)
            sage: y4y = to_V(y^4) * y.matrix(); y4y
            ((x^4 + 1)/x, 2*x, 0, 0, 0)
            sage: y5 == y4y
            True"""
    @overload
    def matrix(self, K) -> Any:
        """FunctionFieldElement.matrix(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 443)

        Return the matrix of multiplication by this element, interpreting this
        element as an element of a vector space over ``base``.

        INPUT:

        - ``base`` -- a function field (default: ``None``); if ``None``, then
          the matrix is formed over the base field of this function field

        EXAMPLES:

        A rational function field::

            sage: K.<t> = FunctionField(QQ)
            sage: t.matrix()                                                            # needs sage.modules
            [t]
            sage: (1/(t+1)).matrix()                                                    # needs sage.modules
            [1/(t + 1)]

        Now an example in a nontrivial extension of a rational function field::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3)
            sage: y.matrix()
            [     0      1]
            [-4*x^3      x]
            sage: y.matrix().charpoly('Z')
            Z^2 - x*Z + 4*x^3

        An example in a relative extension, where neither function
        field is rational::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3)
            sage: M.<T> = L[]
            sage: Z.<alpha> = L.extension(T^3 - y^2*T + x)
            sage: alpha.matrix()
            [          0           1           0]
            [          0           0           1]
            [         -x x*y - 4*x^3           0]
            sage: alpha.matrix(K)
            [           0            0            1            0            0            0]
            [           0            0            0            1            0            0]
            [           0            0            0            0            1            0]
            [           0            0            0            0            0            1]
            [          -x            0       -4*x^3            x            0            0]
            [           0           -x       -4*x^4 -4*x^3 + x^2            0            0]
            sage: alpha.matrix(Z)
            [alpha]

        We show that this matrix does indeed work as expected when making a
        vector space from a function field::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^5 - (x^3 + 2*x*y + 1/x))
            sage: V, from_V, to_V = L.vector_space()
            sage: y5 = to_V(y^5); y5
            ((x^4 + 1)/x, 2*x, 0, 0, 0)
            sage: y4y = to_V(y^4) * y.matrix(); y4y
            ((x^4 + 1)/x, 2*x, 0, 0, 0)
            sage: y5 == y4y
            True"""
    @overload
    def matrix(self, Z) -> Any:
        """FunctionFieldElement.matrix(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 443)

        Return the matrix of multiplication by this element, interpreting this
        element as an element of a vector space over ``base``.

        INPUT:

        - ``base`` -- a function field (default: ``None``); if ``None``, then
          the matrix is formed over the base field of this function field

        EXAMPLES:

        A rational function field::

            sage: K.<t> = FunctionField(QQ)
            sage: t.matrix()                                                            # needs sage.modules
            [t]
            sage: (1/(t+1)).matrix()                                                    # needs sage.modules
            [1/(t + 1)]

        Now an example in a nontrivial extension of a rational function field::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3)
            sage: y.matrix()
            [     0      1]
            [-4*x^3      x]
            sage: y.matrix().charpoly('Z')
            Z^2 - x*Z + 4*x^3

        An example in a relative extension, where neither function
        field is rational::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3)
            sage: M.<T> = L[]
            sage: Z.<alpha> = L.extension(T^3 - y^2*T + x)
            sage: alpha.matrix()
            [          0           1           0]
            [          0           0           1]
            [         -x x*y - 4*x^3           0]
            sage: alpha.matrix(K)
            [           0            0            1            0            0            0]
            [           0            0            0            1            0            0]
            [           0            0            0            0            1            0]
            [           0            0            0            0            0            1]
            [          -x            0       -4*x^3            x            0            0]
            [           0           -x       -4*x^4 -4*x^3 + x^2            0            0]
            sage: alpha.matrix(Z)
            [alpha]

        We show that this matrix does indeed work as expected when making a
        vector space from a function field::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^5 - (x^3 + 2*x*y + 1/x))
            sage: V, from_V, to_V = L.vector_space()
            sage: y5 = to_V(y^5); y5
            ((x^4 + 1)/x, 2*x, 0, 0, 0)
            sage: y4y = to_V(y^4) * y.matrix(); y4y
            ((x^4 + 1)/x, 2*x, 0, 0, 0)
            sage: y5 == y4y
            True"""
    @overload
    def matrix(self) -> Any:
        """FunctionFieldElement.matrix(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 443)

        Return the matrix of multiplication by this element, interpreting this
        element as an element of a vector space over ``base``.

        INPUT:

        - ``base`` -- a function field (default: ``None``); if ``None``, then
          the matrix is formed over the base field of this function field

        EXAMPLES:

        A rational function field::

            sage: K.<t> = FunctionField(QQ)
            sage: t.matrix()                                                            # needs sage.modules
            [t]
            sage: (1/(t+1)).matrix()                                                    # needs sage.modules
            [1/(t + 1)]

        Now an example in a nontrivial extension of a rational function field::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3)
            sage: y.matrix()
            [     0      1]
            [-4*x^3      x]
            sage: y.matrix().charpoly('Z')
            Z^2 - x*Z + 4*x^3

        An example in a relative extension, where neither function
        field is rational::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3)
            sage: M.<T> = L[]
            sage: Z.<alpha> = L.extension(T^3 - y^2*T + x)
            sage: alpha.matrix()
            [          0           1           0]
            [          0           0           1]
            [         -x x*y - 4*x^3           0]
            sage: alpha.matrix(K)
            [           0            0            1            0            0            0]
            [           0            0            0            1            0            0]
            [           0            0            0            0            1            0]
            [           0            0            0            0            0            1]
            [          -x            0       -4*x^3            x            0            0]
            [           0           -x       -4*x^4 -4*x^3 + x^2            0            0]
            sage: alpha.matrix(Z)
            [alpha]

        We show that this matrix does indeed work as expected when making a
        vector space from a function field::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^5 - (x^3 + 2*x*y + 1/x))
            sage: V, from_V, to_V = L.vector_space()
            sage: y5 = to_V(y^5); y5
            ((x^4 + 1)/x, 2*x, 0, 0, 0)
            sage: y4y = to_V(y^4) * y.matrix(); y4y
            ((x^4 + 1)/x, 2*x, 0, 0, 0)
            sage: y5 == y4y
            True"""
    def minimal_polynomial(self, *args, **kwds) -> Any:
        """FunctionFieldElement.minimal_polynomial(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 620)

        Return the minimal polynomial of the element. Give an optional input
        string to name the variable in the characteristic polynomial.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: x.minimal_polynomial('W')                                             # needs sage.modules
            W - x

            sage: # needs sage.rings.function_field
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3); R.<z> = L[]
            sage: M.<z> = L.extension(z^3 - y^2*z + x)
            sage: y.minimal_polynomial('W')
            W^2 - x*W + 4*x^3
            sage: z.minimal_polynomial('W')
            W^3 + (-x*y + 4*x^3)*W + x"""
    def minpoly(self, *args, **kwargs):
        """FunctionFieldElement.minimal_polynomial(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 620)

        Return the minimal polynomial of the element. Give an optional input
        string to name the variable in the characteristic polynomial.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: x.minimal_polynomial('W')                                             # needs sage.modules
            W - x

            sage: # needs sage.rings.function_field
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3); R.<z> = L[]
            sage: M.<z> = L.extension(z^3 - y^2*z + x)
            sage: y.minimal_polynomial('W')
            W^2 - x*W + 4*x^3
            sage: z.minimal_polynomial('W')
            W^3 + (-x*y + 4*x^3)*W + x"""
    @overload
    def norm(self) -> Any:
        """FunctionFieldElement.norm(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 538)

        Return the norm of the element.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3)                                # needs sage.rings.function_field
            sage: y.norm()                                                              # needs sage.rings.function_field
            4*x^3

        The norm is relative::

            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3); R.<z> = L[]                   # needs sage.rings.function_field
            sage: M.<z> = L.extension(z^3 - y^2*z + x)                                  # needs sage.rings.function_field
            sage: z.norm()                                                              # needs sage.rings.function_field
            -x
            sage: z.norm().parent()                                                     # needs sage.rings.function_field
            Function field in y defined by y^2 - x*y + 4*x^3"""
    @overload
    def norm(self) -> Any:
        """FunctionFieldElement.norm(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 538)

        Return the norm of the element.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3)                                # needs sage.rings.function_field
            sage: y.norm()                                                              # needs sage.rings.function_field
            4*x^3

        The norm is relative::

            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3); R.<z> = L[]                   # needs sage.rings.function_field
            sage: M.<z> = L.extension(z^3 - y^2*z + x)                                  # needs sage.rings.function_field
            sage: z.norm()                                                              # needs sage.rings.function_field
            -x
            sage: z.norm().parent()                                                     # needs sage.rings.function_field
            Function field in y defined by y^2 - x*y + 4*x^3"""
    @overload
    def norm(self) -> Any:
        """FunctionFieldElement.norm(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 538)

        Return the norm of the element.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3)                                # needs sage.rings.function_field
            sage: y.norm()                                                              # needs sage.rings.function_field
            4*x^3

        The norm is relative::

            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3); R.<z> = L[]                   # needs sage.rings.function_field
            sage: M.<z> = L.extension(z^3 - y^2*z + x)                                  # needs sage.rings.function_field
            sage: z.norm()                                                              # needs sage.rings.function_field
            -x
            sage: z.norm().parent()                                                     # needs sage.rings.function_field
            Function field in y defined by y^2 - x*y + 4*x^3"""
    @overload
    def norm(self) -> Any:
        """FunctionFieldElement.norm(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 538)

        Return the norm of the element.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3)                                # needs sage.rings.function_field
            sage: y.norm()                                                              # needs sage.rings.function_field
            4*x^3

        The norm is relative::

            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3); R.<z> = L[]                   # needs sage.rings.function_field
            sage: M.<z> = L.extension(z^3 - y^2*z + x)                                  # needs sage.rings.function_field
            sage: z.norm()                                                              # needs sage.rings.function_field
            -x
            sage: z.norm().parent()                                                     # needs sage.rings.function_field
            Function field in y defined by y^2 - x*y + 4*x^3"""
    def nth_root(self, n) -> FunctionFieldElement:
        """FunctionFieldElement.nth_root(self, n) -> FunctionFieldElement

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 982)

        Return an ``n``-th root of this element in the function field.

        INPUT:

        - ``n`` -- integer

        OUTPUT:

        Returns an element ``a`` in the function field such that this element
        equals `a^n`. Raises an error if no such element exists.

        .. SEEALSO::

            :meth:`is_nth_power`

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(3))
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x)                                          # needs sage.rings.function_field
            sage: L(y^27).nth_root(27)                                                  # needs sage.rings.function_field
            y"""
    @overload
    def poles(self) -> Any:
        """FunctionFieldElement.poles(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 859)

        Return the list of the poles of the element.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(2))
            sage: f = 1/(x^3 + x^2 + x)
            sage: f.poles()                                                             # needs sage.libs.pari sage.modules
            [Place (x), Place (x^2 + x + 1)]

        ::

            sage: K.<x> = FunctionField(GF(4)); _.<Y> = K[]                             # needs sage.rings.finite_rings
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)                                # needs sage.rings.finite_rings sage.rings.function_field
            sage: (x/y).poles()                                                         # needs sage.rings.finite_rings sage.rings.function_field
            [Place (1/x, 1/x*y), Place (x + 1, x*y)]"""
    @overload
    def poles(self) -> Any:
        """FunctionFieldElement.poles(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 859)

        Return the list of the poles of the element.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(2))
            sage: f = 1/(x^3 + x^2 + x)
            sage: f.poles()                                                             # needs sage.libs.pari sage.modules
            [Place (x), Place (x^2 + x + 1)]

        ::

            sage: K.<x> = FunctionField(GF(4)); _.<Y> = K[]                             # needs sage.rings.finite_rings
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)                                # needs sage.rings.finite_rings sage.rings.function_field
            sage: (x/y).poles()                                                         # needs sage.rings.finite_rings sage.rings.function_field
            [Place (1/x, 1/x*y), Place (x + 1, x*y)]"""
    @overload
    def poles(self) -> Any:
        """FunctionFieldElement.poles(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 859)

        Return the list of the poles of the element.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(2))
            sage: f = 1/(x^3 + x^2 + x)
            sage: f.poles()                                                             # needs sage.libs.pari sage.modules
            [Place (x), Place (x^2 + x + 1)]

        ::

            sage: K.<x> = FunctionField(GF(4)); _.<Y> = K[]                             # needs sage.rings.finite_rings
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)                                # needs sage.rings.finite_rings sage.rings.function_field
            sage: (x/y).poles()                                                         # needs sage.rings.finite_rings sage.rings.function_field
            [Place (1/x, 1/x*y), Place (x + 1, x*y)]"""
    @overload
    def subs(self, in_dict=..., **kwds) -> Any:
        """FunctionFieldElement.subs(self, in_dict=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 180)

        Substitute the given generators with given values while not touching
        other generators.

        INPUT:

        - ``in_dict`` -- (optional) dictionary of inputs

        - ``**kwds`` -- named parameters

        OUTPUT: new object if substitution is possible, otherwise ``self``

        EXAMPLES:

        Basic substitution::

            sage: K = GF(7)
            sage: Kx.<x> = FunctionField(K)
            sage: y = polygen(Kx)
            sage: f = x^6 + 3; f
            x^6 + 3

        We also substitute the generators in any base fields::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = 7 * t + 3*x*y
            sage: f.subs(t=9)
            3*x*y + 63
            sage: f.subs(x=2, y=4)
            7*t + 24
            sage: f.subs(t=1, x=2, y=3)
            25

        Because of the possibility of extension fields, a generator to
        substitute must be specified::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs(2)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

            sage: # needs sage.rings.function_field
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: f = x + y
            sage: f.subs(0)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

        We can also substitute using dictionary syntax::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = x + y + t
            sage: f.subs({x: 1, y: 3, t: 4})
            8
            sage: f.subs({x: 1, t: 4})
            y + 5

        TESTS:

        Check that we correctly handle extension fields::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = t + x*y
            sage: f.subs(x=1, y=3, t=5)
            8
            sage: f_sub = f.subs(x=1); f_sub
            t + y
            sage: f_sub.parent() == f.parent()
            True
            sage: f.subs(y=2)
            t + 2*x
            sage: f_sub = f.subs(x=1, y=1, t=1); f_sub
            2
            sage: f_sub.parent() == M
            True

        Test that substitution works for rational functions::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^4 - 3)
            sage: f = x / y
            sage: f.subs(x=2) == 2 / y
            True
            sage: f.subs(y=3)
            9*x
            sage: f.subs(t=-1) is f
            True
            sage: f.subs({x: 2, y: 4})
            128/3

        Make sure that we return the same object when there is no
        substitution::

            sage: K = GF(7)
            sage: Kx.<x> = FunctionField(K)
            sage: y = polygen(Kx)
            sage: f = x^6 + 3
            sage: g = f.subs(z=2)
            sage: g == f
            True
            sage: g is f
            True

        Same purpose as above but over an extension field over the rationals::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = t + x*y
            sage: f.subs() is f
            True
            sage: f.subs(w=7) is f
            True
            sage: f.subs(w=7) is f.subs(w=7)
            True
            sage: f.subs(y=y) is f
            True
            sage: f.subs({y: y}) is f
            True
            sage: f.subs(x=x, y=y, t=t) is f
            True

        Test proper handling of not making substitutions::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs() is f
            True
            sage: f.subs(dict()) is f
            True
            sage: f.subs(w=0) is f
            True
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: f = 3*y
            sage: f.subs(x=0)
            3*y
            sage: f = 3*y
            sage: f.subs(x=0, y=y)
            3*y

        Test error handling for wrong argument type::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs(0)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

        Test error handling for dictionary with keys that don't match
        generators::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs({1: 1})
            Traceback (most recent call last):
            ...
            TypeError: key does not match any field generators

        Test error handling with ambiguously named generators::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<x> = K[]
            sage: L.<x> = K.extension(x^3 - x)
            sage: str(L.gen()) == str(K.gen())
            True
            sage: f = K.gen() - L.gen()
            sage: f.subs(x=2)
            Traceback (most recent call last):
            ...
            TypeError: multiple generators have the same name, making substitution ambiguous. Rename generators or pass substitution values in using dictionary format
            sage: f.subs({K.gen(): 1})
            -x + 1
            sage: f.subs({L.gen(): 2})
            x - 2
            sage: f.subs({K.gen(): 1, L.gen(): 2})
            -1
            sage: f.subs({K.gen(): 2, L.gen(): 1})
            1"""
    @overload
    def subs(self, t=...) -> Any:
        """FunctionFieldElement.subs(self, in_dict=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 180)

        Substitute the given generators with given values while not touching
        other generators.

        INPUT:

        - ``in_dict`` -- (optional) dictionary of inputs

        - ``**kwds`` -- named parameters

        OUTPUT: new object if substitution is possible, otherwise ``self``

        EXAMPLES:

        Basic substitution::

            sage: K = GF(7)
            sage: Kx.<x> = FunctionField(K)
            sage: y = polygen(Kx)
            sage: f = x^6 + 3; f
            x^6 + 3

        We also substitute the generators in any base fields::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = 7 * t + 3*x*y
            sage: f.subs(t=9)
            3*x*y + 63
            sage: f.subs(x=2, y=4)
            7*t + 24
            sage: f.subs(t=1, x=2, y=3)
            25

        Because of the possibility of extension fields, a generator to
        substitute must be specified::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs(2)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

            sage: # needs sage.rings.function_field
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: f = x + y
            sage: f.subs(0)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

        We can also substitute using dictionary syntax::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = x + y + t
            sage: f.subs({x: 1, y: 3, t: 4})
            8
            sage: f.subs({x: 1, t: 4})
            y + 5

        TESTS:

        Check that we correctly handle extension fields::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = t + x*y
            sage: f.subs(x=1, y=3, t=5)
            8
            sage: f_sub = f.subs(x=1); f_sub
            t + y
            sage: f_sub.parent() == f.parent()
            True
            sage: f.subs(y=2)
            t + 2*x
            sage: f_sub = f.subs(x=1, y=1, t=1); f_sub
            2
            sage: f_sub.parent() == M
            True

        Test that substitution works for rational functions::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^4 - 3)
            sage: f = x / y
            sage: f.subs(x=2) == 2 / y
            True
            sage: f.subs(y=3)
            9*x
            sage: f.subs(t=-1) is f
            True
            sage: f.subs({x: 2, y: 4})
            128/3

        Make sure that we return the same object when there is no
        substitution::

            sage: K = GF(7)
            sage: Kx.<x> = FunctionField(K)
            sage: y = polygen(Kx)
            sage: f = x^6 + 3
            sage: g = f.subs(z=2)
            sage: g == f
            True
            sage: g is f
            True

        Same purpose as above but over an extension field over the rationals::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = t + x*y
            sage: f.subs() is f
            True
            sage: f.subs(w=7) is f
            True
            sage: f.subs(w=7) is f.subs(w=7)
            True
            sage: f.subs(y=y) is f
            True
            sage: f.subs({y: y}) is f
            True
            sage: f.subs(x=x, y=y, t=t) is f
            True

        Test proper handling of not making substitutions::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs() is f
            True
            sage: f.subs(dict()) is f
            True
            sage: f.subs(w=0) is f
            True
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: f = 3*y
            sage: f.subs(x=0)
            3*y
            sage: f = 3*y
            sage: f.subs(x=0, y=y)
            3*y

        Test error handling for wrong argument type::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs(0)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

        Test error handling for dictionary with keys that don't match
        generators::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs({1: 1})
            Traceback (most recent call last):
            ...
            TypeError: key does not match any field generators

        Test error handling with ambiguously named generators::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<x> = K[]
            sage: L.<x> = K.extension(x^3 - x)
            sage: str(L.gen()) == str(K.gen())
            True
            sage: f = K.gen() - L.gen()
            sage: f.subs(x=2)
            Traceback (most recent call last):
            ...
            TypeError: multiple generators have the same name, making substitution ambiguous. Rename generators or pass substitution values in using dictionary format
            sage: f.subs({K.gen(): 1})
            -x + 1
            sage: f.subs({L.gen(): 2})
            x - 2
            sage: f.subs({K.gen(): 1, L.gen(): 2})
            -1
            sage: f.subs({K.gen(): 2, L.gen(): 1})
            1"""
    @overload
    def subs(self, x=..., y=...) -> Any:
        """FunctionFieldElement.subs(self, in_dict=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 180)

        Substitute the given generators with given values while not touching
        other generators.

        INPUT:

        - ``in_dict`` -- (optional) dictionary of inputs

        - ``**kwds`` -- named parameters

        OUTPUT: new object if substitution is possible, otherwise ``self``

        EXAMPLES:

        Basic substitution::

            sage: K = GF(7)
            sage: Kx.<x> = FunctionField(K)
            sage: y = polygen(Kx)
            sage: f = x^6 + 3; f
            x^6 + 3

        We also substitute the generators in any base fields::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = 7 * t + 3*x*y
            sage: f.subs(t=9)
            3*x*y + 63
            sage: f.subs(x=2, y=4)
            7*t + 24
            sage: f.subs(t=1, x=2, y=3)
            25

        Because of the possibility of extension fields, a generator to
        substitute must be specified::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs(2)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

            sage: # needs sage.rings.function_field
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: f = x + y
            sage: f.subs(0)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

        We can also substitute using dictionary syntax::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = x + y + t
            sage: f.subs({x: 1, y: 3, t: 4})
            8
            sage: f.subs({x: 1, t: 4})
            y + 5

        TESTS:

        Check that we correctly handle extension fields::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = t + x*y
            sage: f.subs(x=1, y=3, t=5)
            8
            sage: f_sub = f.subs(x=1); f_sub
            t + y
            sage: f_sub.parent() == f.parent()
            True
            sage: f.subs(y=2)
            t + 2*x
            sage: f_sub = f.subs(x=1, y=1, t=1); f_sub
            2
            sage: f_sub.parent() == M
            True

        Test that substitution works for rational functions::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^4 - 3)
            sage: f = x / y
            sage: f.subs(x=2) == 2 / y
            True
            sage: f.subs(y=3)
            9*x
            sage: f.subs(t=-1) is f
            True
            sage: f.subs({x: 2, y: 4})
            128/3

        Make sure that we return the same object when there is no
        substitution::

            sage: K = GF(7)
            sage: Kx.<x> = FunctionField(K)
            sage: y = polygen(Kx)
            sage: f = x^6 + 3
            sage: g = f.subs(z=2)
            sage: g == f
            True
            sage: g is f
            True

        Same purpose as above but over an extension field over the rationals::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = t + x*y
            sage: f.subs() is f
            True
            sage: f.subs(w=7) is f
            True
            sage: f.subs(w=7) is f.subs(w=7)
            True
            sage: f.subs(y=y) is f
            True
            sage: f.subs({y: y}) is f
            True
            sage: f.subs(x=x, y=y, t=t) is f
            True

        Test proper handling of not making substitutions::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs() is f
            True
            sage: f.subs(dict()) is f
            True
            sage: f.subs(w=0) is f
            True
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: f = 3*y
            sage: f.subs(x=0)
            3*y
            sage: f = 3*y
            sage: f.subs(x=0, y=y)
            3*y

        Test error handling for wrong argument type::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs(0)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

        Test error handling for dictionary with keys that don't match
        generators::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs({1: 1})
            Traceback (most recent call last):
            ...
            TypeError: key does not match any field generators

        Test error handling with ambiguously named generators::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<x> = K[]
            sage: L.<x> = K.extension(x^3 - x)
            sage: str(L.gen()) == str(K.gen())
            True
            sage: f = K.gen() - L.gen()
            sage: f.subs(x=2)
            Traceback (most recent call last):
            ...
            TypeError: multiple generators have the same name, making substitution ambiguous. Rename generators or pass substitution values in using dictionary format
            sage: f.subs({K.gen(): 1})
            -x + 1
            sage: f.subs({L.gen(): 2})
            x - 2
            sage: f.subs({K.gen(): 1, L.gen(): 2})
            -1
            sage: f.subs({K.gen(): 2, L.gen(): 1})
            1"""
    @overload
    def subs(self, t=..., x=..., y=...) -> Any:
        """FunctionFieldElement.subs(self, in_dict=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 180)

        Substitute the given generators with given values while not touching
        other generators.

        INPUT:

        - ``in_dict`` -- (optional) dictionary of inputs

        - ``**kwds`` -- named parameters

        OUTPUT: new object if substitution is possible, otherwise ``self``

        EXAMPLES:

        Basic substitution::

            sage: K = GF(7)
            sage: Kx.<x> = FunctionField(K)
            sage: y = polygen(Kx)
            sage: f = x^6 + 3; f
            x^6 + 3

        We also substitute the generators in any base fields::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = 7 * t + 3*x*y
            sage: f.subs(t=9)
            3*x*y + 63
            sage: f.subs(x=2, y=4)
            7*t + 24
            sage: f.subs(t=1, x=2, y=3)
            25

        Because of the possibility of extension fields, a generator to
        substitute must be specified::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs(2)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

            sage: # needs sage.rings.function_field
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: f = x + y
            sage: f.subs(0)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

        We can also substitute using dictionary syntax::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = x + y + t
            sage: f.subs({x: 1, y: 3, t: 4})
            8
            sage: f.subs({x: 1, t: 4})
            y + 5

        TESTS:

        Check that we correctly handle extension fields::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = t + x*y
            sage: f.subs(x=1, y=3, t=5)
            8
            sage: f_sub = f.subs(x=1); f_sub
            t + y
            sage: f_sub.parent() == f.parent()
            True
            sage: f.subs(y=2)
            t + 2*x
            sage: f_sub = f.subs(x=1, y=1, t=1); f_sub
            2
            sage: f_sub.parent() == M
            True

        Test that substitution works for rational functions::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^4 - 3)
            sage: f = x / y
            sage: f.subs(x=2) == 2 / y
            True
            sage: f.subs(y=3)
            9*x
            sage: f.subs(t=-1) is f
            True
            sage: f.subs({x: 2, y: 4})
            128/3

        Make sure that we return the same object when there is no
        substitution::

            sage: K = GF(7)
            sage: Kx.<x> = FunctionField(K)
            sage: y = polygen(Kx)
            sage: f = x^6 + 3
            sage: g = f.subs(z=2)
            sage: g == f
            True
            sage: g is f
            True

        Same purpose as above but over an extension field over the rationals::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = t + x*y
            sage: f.subs() is f
            True
            sage: f.subs(w=7) is f
            True
            sage: f.subs(w=7) is f.subs(w=7)
            True
            sage: f.subs(y=y) is f
            True
            sage: f.subs({y: y}) is f
            True
            sage: f.subs(x=x, y=y, t=t) is f
            True

        Test proper handling of not making substitutions::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs() is f
            True
            sage: f.subs(dict()) is f
            True
            sage: f.subs(w=0) is f
            True
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: f = 3*y
            sage: f.subs(x=0)
            3*y
            sage: f = 3*y
            sage: f.subs(x=0, y=y)
            3*y

        Test error handling for wrong argument type::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs(0)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

        Test error handling for dictionary with keys that don't match
        generators::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs({1: 1})
            Traceback (most recent call last):
            ...
            TypeError: key does not match any field generators

        Test error handling with ambiguously named generators::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<x> = K[]
            sage: L.<x> = K.extension(x^3 - x)
            sage: str(L.gen()) == str(K.gen())
            True
            sage: f = K.gen() - L.gen()
            sage: f.subs(x=2)
            Traceback (most recent call last):
            ...
            TypeError: multiple generators have the same name, making substitution ambiguous. Rename generators or pass substitution values in using dictionary format
            sage: f.subs({K.gen(): 1})
            -x + 1
            sage: f.subs({L.gen(): 2})
            x - 2
            sage: f.subs({K.gen(): 1, L.gen(): 2})
            -1
            sage: f.subs({K.gen(): 2, L.gen(): 1})
            1"""
    @overload
    def subs(self, x=..., y=..., t=...) -> Any:
        """FunctionFieldElement.subs(self, in_dict=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 180)

        Substitute the given generators with given values while not touching
        other generators.

        INPUT:

        - ``in_dict`` -- (optional) dictionary of inputs

        - ``**kwds`` -- named parameters

        OUTPUT: new object if substitution is possible, otherwise ``self``

        EXAMPLES:

        Basic substitution::

            sage: K = GF(7)
            sage: Kx.<x> = FunctionField(K)
            sage: y = polygen(Kx)
            sage: f = x^6 + 3; f
            x^6 + 3

        We also substitute the generators in any base fields::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = 7 * t + 3*x*y
            sage: f.subs(t=9)
            3*x*y + 63
            sage: f.subs(x=2, y=4)
            7*t + 24
            sage: f.subs(t=1, x=2, y=3)
            25

        Because of the possibility of extension fields, a generator to
        substitute must be specified::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs(2)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

            sage: # needs sage.rings.function_field
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: f = x + y
            sage: f.subs(0)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

        We can also substitute using dictionary syntax::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = x + y + t
            sage: f.subs({x: 1, y: 3, t: 4})
            8
            sage: f.subs({x: 1, t: 4})
            y + 5

        TESTS:

        Check that we correctly handle extension fields::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = t + x*y
            sage: f.subs(x=1, y=3, t=5)
            8
            sage: f_sub = f.subs(x=1); f_sub
            t + y
            sage: f_sub.parent() == f.parent()
            True
            sage: f.subs(y=2)
            t + 2*x
            sage: f_sub = f.subs(x=1, y=1, t=1); f_sub
            2
            sage: f_sub.parent() == M
            True

        Test that substitution works for rational functions::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^4 - 3)
            sage: f = x / y
            sage: f.subs(x=2) == 2 / y
            True
            sage: f.subs(y=3)
            9*x
            sage: f.subs(t=-1) is f
            True
            sage: f.subs({x: 2, y: 4})
            128/3

        Make sure that we return the same object when there is no
        substitution::

            sage: K = GF(7)
            sage: Kx.<x> = FunctionField(K)
            sage: y = polygen(Kx)
            sage: f = x^6 + 3
            sage: g = f.subs(z=2)
            sage: g == f
            True
            sage: g is f
            True

        Same purpose as above but over an extension field over the rationals::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = t + x*y
            sage: f.subs() is f
            True
            sage: f.subs(w=7) is f
            True
            sage: f.subs(w=7) is f.subs(w=7)
            True
            sage: f.subs(y=y) is f
            True
            sage: f.subs({y: y}) is f
            True
            sage: f.subs(x=x, y=y, t=t) is f
            True

        Test proper handling of not making substitutions::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs() is f
            True
            sage: f.subs(dict()) is f
            True
            sage: f.subs(w=0) is f
            True
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: f = 3*y
            sage: f.subs(x=0)
            3*y
            sage: f = 3*y
            sage: f.subs(x=0, y=y)
            3*y

        Test error handling for wrong argument type::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs(0)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

        Test error handling for dictionary with keys that don't match
        generators::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs({1: 1})
            Traceback (most recent call last):
            ...
            TypeError: key does not match any field generators

        Test error handling with ambiguously named generators::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<x> = K[]
            sage: L.<x> = K.extension(x^3 - x)
            sage: str(L.gen()) == str(K.gen())
            True
            sage: f = K.gen() - L.gen()
            sage: f.subs(x=2)
            Traceback (most recent call last):
            ...
            TypeError: multiple generators have the same name, making substitution ambiguous. Rename generators or pass substitution values in using dictionary format
            sage: f.subs({K.gen(): 1})
            -x + 1
            sage: f.subs({L.gen(): 2})
            x - 2
            sage: f.subs({K.gen(): 1, L.gen(): 2})
            -1
            sage: f.subs({K.gen(): 2, L.gen(): 1})
            1"""
    @overload
    def subs(self, x=...) -> Any:
        """FunctionFieldElement.subs(self, in_dict=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 180)

        Substitute the given generators with given values while not touching
        other generators.

        INPUT:

        - ``in_dict`` -- (optional) dictionary of inputs

        - ``**kwds`` -- named parameters

        OUTPUT: new object if substitution is possible, otherwise ``self``

        EXAMPLES:

        Basic substitution::

            sage: K = GF(7)
            sage: Kx.<x> = FunctionField(K)
            sage: y = polygen(Kx)
            sage: f = x^6 + 3; f
            x^6 + 3

        We also substitute the generators in any base fields::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = 7 * t + 3*x*y
            sage: f.subs(t=9)
            3*x*y + 63
            sage: f.subs(x=2, y=4)
            7*t + 24
            sage: f.subs(t=1, x=2, y=3)
            25

        Because of the possibility of extension fields, a generator to
        substitute must be specified::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs(2)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

            sage: # needs sage.rings.function_field
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: f = x + y
            sage: f.subs(0)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

        We can also substitute using dictionary syntax::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = x + y + t
            sage: f.subs({x: 1, y: 3, t: 4})
            8
            sage: f.subs({x: 1, t: 4})
            y + 5

        TESTS:

        Check that we correctly handle extension fields::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = t + x*y
            sage: f.subs(x=1, y=3, t=5)
            8
            sage: f_sub = f.subs(x=1); f_sub
            t + y
            sage: f_sub.parent() == f.parent()
            True
            sage: f.subs(y=2)
            t + 2*x
            sage: f_sub = f.subs(x=1, y=1, t=1); f_sub
            2
            sage: f_sub.parent() == M
            True

        Test that substitution works for rational functions::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^4 - 3)
            sage: f = x / y
            sage: f.subs(x=2) == 2 / y
            True
            sage: f.subs(y=3)
            9*x
            sage: f.subs(t=-1) is f
            True
            sage: f.subs({x: 2, y: 4})
            128/3

        Make sure that we return the same object when there is no
        substitution::

            sage: K = GF(7)
            sage: Kx.<x> = FunctionField(K)
            sage: y = polygen(Kx)
            sage: f = x^6 + 3
            sage: g = f.subs(z=2)
            sage: g == f
            True
            sage: g is f
            True

        Same purpose as above but over an extension field over the rationals::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = t + x*y
            sage: f.subs() is f
            True
            sage: f.subs(w=7) is f
            True
            sage: f.subs(w=7) is f.subs(w=7)
            True
            sage: f.subs(y=y) is f
            True
            sage: f.subs({y: y}) is f
            True
            sage: f.subs(x=x, y=y, t=t) is f
            True

        Test proper handling of not making substitutions::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs() is f
            True
            sage: f.subs(dict()) is f
            True
            sage: f.subs(w=0) is f
            True
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: f = 3*y
            sage: f.subs(x=0)
            3*y
            sage: f = 3*y
            sage: f.subs(x=0, y=y)
            3*y

        Test error handling for wrong argument type::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs(0)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

        Test error handling for dictionary with keys that don't match
        generators::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs({1: 1})
            Traceback (most recent call last):
            ...
            TypeError: key does not match any field generators

        Test error handling with ambiguously named generators::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<x> = K[]
            sage: L.<x> = K.extension(x^3 - x)
            sage: str(L.gen()) == str(K.gen())
            True
            sage: f = K.gen() - L.gen()
            sage: f.subs(x=2)
            Traceback (most recent call last):
            ...
            TypeError: multiple generators have the same name, making substitution ambiguous. Rename generators or pass substitution values in using dictionary format
            sage: f.subs({K.gen(): 1})
            -x + 1
            sage: f.subs({L.gen(): 2})
            x - 2
            sage: f.subs({K.gen(): 1, L.gen(): 2})
            -1
            sage: f.subs({K.gen(): 2, L.gen(): 1})
            1"""
    @overload
    def subs(self, y=...) -> Any:
        """FunctionFieldElement.subs(self, in_dict=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 180)

        Substitute the given generators with given values while not touching
        other generators.

        INPUT:

        - ``in_dict`` -- (optional) dictionary of inputs

        - ``**kwds`` -- named parameters

        OUTPUT: new object if substitution is possible, otherwise ``self``

        EXAMPLES:

        Basic substitution::

            sage: K = GF(7)
            sage: Kx.<x> = FunctionField(K)
            sage: y = polygen(Kx)
            sage: f = x^6 + 3; f
            x^6 + 3

        We also substitute the generators in any base fields::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = 7 * t + 3*x*y
            sage: f.subs(t=9)
            3*x*y + 63
            sage: f.subs(x=2, y=4)
            7*t + 24
            sage: f.subs(t=1, x=2, y=3)
            25

        Because of the possibility of extension fields, a generator to
        substitute must be specified::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs(2)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

            sage: # needs sage.rings.function_field
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: f = x + y
            sage: f.subs(0)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

        We can also substitute using dictionary syntax::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = x + y + t
            sage: f.subs({x: 1, y: 3, t: 4})
            8
            sage: f.subs({x: 1, t: 4})
            y + 5

        TESTS:

        Check that we correctly handle extension fields::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = t + x*y
            sage: f.subs(x=1, y=3, t=5)
            8
            sage: f_sub = f.subs(x=1); f_sub
            t + y
            sage: f_sub.parent() == f.parent()
            True
            sage: f.subs(y=2)
            t + 2*x
            sage: f_sub = f.subs(x=1, y=1, t=1); f_sub
            2
            sage: f_sub.parent() == M
            True

        Test that substitution works for rational functions::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^4 - 3)
            sage: f = x / y
            sage: f.subs(x=2) == 2 / y
            True
            sage: f.subs(y=3)
            9*x
            sage: f.subs(t=-1) is f
            True
            sage: f.subs({x: 2, y: 4})
            128/3

        Make sure that we return the same object when there is no
        substitution::

            sage: K = GF(7)
            sage: Kx.<x> = FunctionField(K)
            sage: y = polygen(Kx)
            sage: f = x^6 + 3
            sage: g = f.subs(z=2)
            sage: g == f
            True
            sage: g is f
            True

        Same purpose as above but over an extension field over the rationals::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = t + x*y
            sage: f.subs() is f
            True
            sage: f.subs(w=7) is f
            True
            sage: f.subs(w=7) is f.subs(w=7)
            True
            sage: f.subs(y=y) is f
            True
            sage: f.subs({y: y}) is f
            True
            sage: f.subs(x=x, y=y, t=t) is f
            True

        Test proper handling of not making substitutions::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs() is f
            True
            sage: f.subs(dict()) is f
            True
            sage: f.subs(w=0) is f
            True
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: f = 3*y
            sage: f.subs(x=0)
            3*y
            sage: f = 3*y
            sage: f.subs(x=0, y=y)
            3*y

        Test error handling for wrong argument type::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs(0)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

        Test error handling for dictionary with keys that don't match
        generators::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs({1: 1})
            Traceback (most recent call last):
            ...
            TypeError: key does not match any field generators

        Test error handling with ambiguously named generators::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<x> = K[]
            sage: L.<x> = K.extension(x^3 - x)
            sage: str(L.gen()) == str(K.gen())
            True
            sage: f = K.gen() - L.gen()
            sage: f.subs(x=2)
            Traceback (most recent call last):
            ...
            TypeError: multiple generators have the same name, making substitution ambiguous. Rename generators or pass substitution values in using dictionary format
            sage: f.subs({K.gen(): 1})
            -x + 1
            sage: f.subs({L.gen(): 2})
            x - 2
            sage: f.subs({K.gen(): 1, L.gen(): 2})
            -1
            sage: f.subs({K.gen(): 2, L.gen(): 1})
            1"""
    @overload
    def subs(self, x=..., y=..., t=...) -> Any:
        """FunctionFieldElement.subs(self, in_dict=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 180)

        Substitute the given generators with given values while not touching
        other generators.

        INPUT:

        - ``in_dict`` -- (optional) dictionary of inputs

        - ``**kwds`` -- named parameters

        OUTPUT: new object if substitution is possible, otherwise ``self``

        EXAMPLES:

        Basic substitution::

            sage: K = GF(7)
            sage: Kx.<x> = FunctionField(K)
            sage: y = polygen(Kx)
            sage: f = x^6 + 3; f
            x^6 + 3

        We also substitute the generators in any base fields::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = 7 * t + 3*x*y
            sage: f.subs(t=9)
            3*x*y + 63
            sage: f.subs(x=2, y=4)
            7*t + 24
            sage: f.subs(t=1, x=2, y=3)
            25

        Because of the possibility of extension fields, a generator to
        substitute must be specified::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs(2)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

            sage: # needs sage.rings.function_field
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: f = x + y
            sage: f.subs(0)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

        We can also substitute using dictionary syntax::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = x + y + t
            sage: f.subs({x: 1, y: 3, t: 4})
            8
            sage: f.subs({x: 1, t: 4})
            y + 5

        TESTS:

        Check that we correctly handle extension fields::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = t + x*y
            sage: f.subs(x=1, y=3, t=5)
            8
            sage: f_sub = f.subs(x=1); f_sub
            t + y
            sage: f_sub.parent() == f.parent()
            True
            sage: f.subs(y=2)
            t + 2*x
            sage: f_sub = f.subs(x=1, y=1, t=1); f_sub
            2
            sage: f_sub.parent() == M
            True

        Test that substitution works for rational functions::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^4 - 3)
            sage: f = x / y
            sage: f.subs(x=2) == 2 / y
            True
            sage: f.subs(y=3)
            9*x
            sage: f.subs(t=-1) is f
            True
            sage: f.subs({x: 2, y: 4})
            128/3

        Make sure that we return the same object when there is no
        substitution::

            sage: K = GF(7)
            sage: Kx.<x> = FunctionField(K)
            sage: y = polygen(Kx)
            sage: f = x^6 + 3
            sage: g = f.subs(z=2)
            sage: g == f
            True
            sage: g is f
            True

        Same purpose as above but over an extension field over the rationals::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = t + x*y
            sage: f.subs() is f
            True
            sage: f.subs(w=7) is f
            True
            sage: f.subs(w=7) is f.subs(w=7)
            True
            sage: f.subs(y=y) is f
            True
            sage: f.subs({y: y}) is f
            True
            sage: f.subs(x=x, y=y, t=t) is f
            True

        Test proper handling of not making substitutions::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs() is f
            True
            sage: f.subs(dict()) is f
            True
            sage: f.subs(w=0) is f
            True
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: f = 3*y
            sage: f.subs(x=0)
            3*y
            sage: f = 3*y
            sage: f.subs(x=0, y=y)
            3*y

        Test error handling for wrong argument type::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs(0)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

        Test error handling for dictionary with keys that don't match
        generators::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs({1: 1})
            Traceback (most recent call last):
            ...
            TypeError: key does not match any field generators

        Test error handling with ambiguously named generators::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<x> = K[]
            sage: L.<x> = K.extension(x^3 - x)
            sage: str(L.gen()) == str(K.gen())
            True
            sage: f = K.gen() - L.gen()
            sage: f.subs(x=2)
            Traceback (most recent call last):
            ...
            TypeError: multiple generators have the same name, making substitution ambiguous. Rename generators or pass substitution values in using dictionary format
            sage: f.subs({K.gen(): 1})
            -x + 1
            sage: f.subs({L.gen(): 2})
            x - 2
            sage: f.subs({K.gen(): 1, L.gen(): 2})
            -1
            sage: f.subs({K.gen(): 2, L.gen(): 1})
            1"""
    @overload
    def subs(self, x=...) -> Any:
        """FunctionFieldElement.subs(self, in_dict=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 180)

        Substitute the given generators with given values while not touching
        other generators.

        INPUT:

        - ``in_dict`` -- (optional) dictionary of inputs

        - ``**kwds`` -- named parameters

        OUTPUT: new object if substitution is possible, otherwise ``self``

        EXAMPLES:

        Basic substitution::

            sage: K = GF(7)
            sage: Kx.<x> = FunctionField(K)
            sage: y = polygen(Kx)
            sage: f = x^6 + 3; f
            x^6 + 3

        We also substitute the generators in any base fields::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = 7 * t + 3*x*y
            sage: f.subs(t=9)
            3*x*y + 63
            sage: f.subs(x=2, y=4)
            7*t + 24
            sage: f.subs(t=1, x=2, y=3)
            25

        Because of the possibility of extension fields, a generator to
        substitute must be specified::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs(2)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

            sage: # needs sage.rings.function_field
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: f = x + y
            sage: f.subs(0)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

        We can also substitute using dictionary syntax::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = x + y + t
            sage: f.subs({x: 1, y: 3, t: 4})
            8
            sage: f.subs({x: 1, t: 4})
            y + 5

        TESTS:

        Check that we correctly handle extension fields::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = t + x*y
            sage: f.subs(x=1, y=3, t=5)
            8
            sage: f_sub = f.subs(x=1); f_sub
            t + y
            sage: f_sub.parent() == f.parent()
            True
            sage: f.subs(y=2)
            t + 2*x
            sage: f_sub = f.subs(x=1, y=1, t=1); f_sub
            2
            sage: f_sub.parent() == M
            True

        Test that substitution works for rational functions::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^4 - 3)
            sage: f = x / y
            sage: f.subs(x=2) == 2 / y
            True
            sage: f.subs(y=3)
            9*x
            sage: f.subs(t=-1) is f
            True
            sage: f.subs({x: 2, y: 4})
            128/3

        Make sure that we return the same object when there is no
        substitution::

            sage: K = GF(7)
            sage: Kx.<x> = FunctionField(K)
            sage: y = polygen(Kx)
            sage: f = x^6 + 3
            sage: g = f.subs(z=2)
            sage: g == f
            True
            sage: g is f
            True

        Same purpose as above but over an extension field over the rationals::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = t + x*y
            sage: f.subs() is f
            True
            sage: f.subs(w=7) is f
            True
            sage: f.subs(w=7) is f.subs(w=7)
            True
            sage: f.subs(y=y) is f
            True
            sage: f.subs({y: y}) is f
            True
            sage: f.subs(x=x, y=y, t=t) is f
            True

        Test proper handling of not making substitutions::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs() is f
            True
            sage: f.subs(dict()) is f
            True
            sage: f.subs(w=0) is f
            True
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: f = 3*y
            sage: f.subs(x=0)
            3*y
            sage: f = 3*y
            sage: f.subs(x=0, y=y)
            3*y

        Test error handling for wrong argument type::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs(0)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

        Test error handling for dictionary with keys that don't match
        generators::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs({1: 1})
            Traceback (most recent call last):
            ...
            TypeError: key does not match any field generators

        Test error handling with ambiguously named generators::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<x> = K[]
            sage: L.<x> = K.extension(x^3 - x)
            sage: str(L.gen()) == str(K.gen())
            True
            sage: f = K.gen() - L.gen()
            sage: f.subs(x=2)
            Traceback (most recent call last):
            ...
            TypeError: multiple generators have the same name, making substitution ambiguous. Rename generators or pass substitution values in using dictionary format
            sage: f.subs({K.gen(): 1})
            -x + 1
            sage: f.subs({L.gen(): 2})
            x - 2
            sage: f.subs({K.gen(): 1, L.gen(): 2})
            -1
            sage: f.subs({K.gen(): 2, L.gen(): 1})
            1"""
    @overload
    def subs(self, y=...) -> Any:
        """FunctionFieldElement.subs(self, in_dict=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 180)

        Substitute the given generators with given values while not touching
        other generators.

        INPUT:

        - ``in_dict`` -- (optional) dictionary of inputs

        - ``**kwds`` -- named parameters

        OUTPUT: new object if substitution is possible, otherwise ``self``

        EXAMPLES:

        Basic substitution::

            sage: K = GF(7)
            sage: Kx.<x> = FunctionField(K)
            sage: y = polygen(Kx)
            sage: f = x^6 + 3; f
            x^6 + 3

        We also substitute the generators in any base fields::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = 7 * t + 3*x*y
            sage: f.subs(t=9)
            3*x*y + 63
            sage: f.subs(x=2, y=4)
            7*t + 24
            sage: f.subs(t=1, x=2, y=3)
            25

        Because of the possibility of extension fields, a generator to
        substitute must be specified::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs(2)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

            sage: # needs sage.rings.function_field
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: f = x + y
            sage: f.subs(0)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

        We can also substitute using dictionary syntax::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = x + y + t
            sage: f.subs({x: 1, y: 3, t: 4})
            8
            sage: f.subs({x: 1, t: 4})
            y + 5

        TESTS:

        Check that we correctly handle extension fields::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = t + x*y
            sage: f.subs(x=1, y=3, t=5)
            8
            sage: f_sub = f.subs(x=1); f_sub
            t + y
            sage: f_sub.parent() == f.parent()
            True
            sage: f.subs(y=2)
            t + 2*x
            sage: f_sub = f.subs(x=1, y=1, t=1); f_sub
            2
            sage: f_sub.parent() == M
            True

        Test that substitution works for rational functions::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^4 - 3)
            sage: f = x / y
            sage: f.subs(x=2) == 2 / y
            True
            sage: f.subs(y=3)
            9*x
            sage: f.subs(t=-1) is f
            True
            sage: f.subs({x: 2, y: 4})
            128/3

        Make sure that we return the same object when there is no
        substitution::

            sage: K = GF(7)
            sage: Kx.<x> = FunctionField(K)
            sage: y = polygen(Kx)
            sage: f = x^6 + 3
            sage: g = f.subs(z=2)
            sage: g == f
            True
            sage: g is f
            True

        Same purpose as above but over an extension field over the rationals::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = t + x*y
            sage: f.subs() is f
            True
            sage: f.subs(w=7) is f
            True
            sage: f.subs(w=7) is f.subs(w=7)
            True
            sage: f.subs(y=y) is f
            True
            sage: f.subs({y: y}) is f
            True
            sage: f.subs(x=x, y=y, t=t) is f
            True

        Test proper handling of not making substitutions::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs() is f
            True
            sage: f.subs(dict()) is f
            True
            sage: f.subs(w=0) is f
            True
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: f = 3*y
            sage: f.subs(x=0)
            3*y
            sage: f = 3*y
            sage: f.subs(x=0, y=y)
            3*y

        Test error handling for wrong argument type::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs(0)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

        Test error handling for dictionary with keys that don't match
        generators::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs({1: 1})
            Traceback (most recent call last):
            ...
            TypeError: key does not match any field generators

        Test error handling with ambiguously named generators::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<x> = K[]
            sage: L.<x> = K.extension(x^3 - x)
            sage: str(L.gen()) == str(K.gen())
            True
            sage: f = K.gen() - L.gen()
            sage: f.subs(x=2)
            Traceback (most recent call last):
            ...
            TypeError: multiple generators have the same name, making substitution ambiguous. Rename generators or pass substitution values in using dictionary format
            sage: f.subs({K.gen(): 1})
            -x + 1
            sage: f.subs({L.gen(): 2})
            x - 2
            sage: f.subs({K.gen(): 1, L.gen(): 2})
            -1
            sage: f.subs({K.gen(): 2, L.gen(): 1})
            1"""
    @overload
    def subs(self, t=...) -> Any:
        """FunctionFieldElement.subs(self, in_dict=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 180)

        Substitute the given generators with given values while not touching
        other generators.

        INPUT:

        - ``in_dict`` -- (optional) dictionary of inputs

        - ``**kwds`` -- named parameters

        OUTPUT: new object if substitution is possible, otherwise ``self``

        EXAMPLES:

        Basic substitution::

            sage: K = GF(7)
            sage: Kx.<x> = FunctionField(K)
            sage: y = polygen(Kx)
            sage: f = x^6 + 3; f
            x^6 + 3

        We also substitute the generators in any base fields::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = 7 * t + 3*x*y
            sage: f.subs(t=9)
            3*x*y + 63
            sage: f.subs(x=2, y=4)
            7*t + 24
            sage: f.subs(t=1, x=2, y=3)
            25

        Because of the possibility of extension fields, a generator to
        substitute must be specified::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs(2)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

            sage: # needs sage.rings.function_field
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: f = x + y
            sage: f.subs(0)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

        We can also substitute using dictionary syntax::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = x + y + t
            sage: f.subs({x: 1, y: 3, t: 4})
            8
            sage: f.subs({x: 1, t: 4})
            y + 5

        TESTS:

        Check that we correctly handle extension fields::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = t + x*y
            sage: f.subs(x=1, y=3, t=5)
            8
            sage: f_sub = f.subs(x=1); f_sub
            t + y
            sage: f_sub.parent() == f.parent()
            True
            sage: f.subs(y=2)
            t + 2*x
            sage: f_sub = f.subs(x=1, y=1, t=1); f_sub
            2
            sage: f_sub.parent() == M
            True

        Test that substitution works for rational functions::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^4 - 3)
            sage: f = x / y
            sage: f.subs(x=2) == 2 / y
            True
            sage: f.subs(y=3)
            9*x
            sage: f.subs(t=-1) is f
            True
            sage: f.subs({x: 2, y: 4})
            128/3

        Make sure that we return the same object when there is no
        substitution::

            sage: K = GF(7)
            sage: Kx.<x> = FunctionField(K)
            sage: y = polygen(Kx)
            sage: f = x^6 + 3
            sage: g = f.subs(z=2)
            sage: g == f
            True
            sage: g is f
            True

        Same purpose as above but over an extension field over the rationals::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = t + x*y
            sage: f.subs() is f
            True
            sage: f.subs(w=7) is f
            True
            sage: f.subs(w=7) is f.subs(w=7)
            True
            sage: f.subs(y=y) is f
            True
            sage: f.subs({y: y}) is f
            True
            sage: f.subs(x=x, y=y, t=t) is f
            True

        Test proper handling of not making substitutions::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs() is f
            True
            sage: f.subs(dict()) is f
            True
            sage: f.subs(w=0) is f
            True
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: f = 3*y
            sage: f.subs(x=0)
            3*y
            sage: f = 3*y
            sage: f.subs(x=0, y=y)
            3*y

        Test error handling for wrong argument type::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs(0)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

        Test error handling for dictionary with keys that don't match
        generators::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs({1: 1})
            Traceback (most recent call last):
            ...
            TypeError: key does not match any field generators

        Test error handling with ambiguously named generators::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<x> = K[]
            sage: L.<x> = K.extension(x^3 - x)
            sage: str(L.gen()) == str(K.gen())
            True
            sage: f = K.gen() - L.gen()
            sage: f.subs(x=2)
            Traceback (most recent call last):
            ...
            TypeError: multiple generators have the same name, making substitution ambiguous. Rename generators or pass substitution values in using dictionary format
            sage: f.subs({K.gen(): 1})
            -x + 1
            sage: f.subs({L.gen(): 2})
            x - 2
            sage: f.subs({K.gen(): 1, L.gen(): 2})
            -1
            sage: f.subs({K.gen(): 2, L.gen(): 1})
            1"""
    @overload
    def subs(self, z=...) -> Any:
        """FunctionFieldElement.subs(self, in_dict=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 180)

        Substitute the given generators with given values while not touching
        other generators.

        INPUT:

        - ``in_dict`` -- (optional) dictionary of inputs

        - ``**kwds`` -- named parameters

        OUTPUT: new object if substitution is possible, otherwise ``self``

        EXAMPLES:

        Basic substitution::

            sage: K = GF(7)
            sage: Kx.<x> = FunctionField(K)
            sage: y = polygen(Kx)
            sage: f = x^6 + 3; f
            x^6 + 3

        We also substitute the generators in any base fields::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = 7 * t + 3*x*y
            sage: f.subs(t=9)
            3*x*y + 63
            sage: f.subs(x=2, y=4)
            7*t + 24
            sage: f.subs(t=1, x=2, y=3)
            25

        Because of the possibility of extension fields, a generator to
        substitute must be specified::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs(2)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

            sage: # needs sage.rings.function_field
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: f = x + y
            sage: f.subs(0)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

        We can also substitute using dictionary syntax::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = x + y + t
            sage: f.subs({x: 1, y: 3, t: 4})
            8
            sage: f.subs({x: 1, t: 4})
            y + 5

        TESTS:

        Check that we correctly handle extension fields::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = t + x*y
            sage: f.subs(x=1, y=3, t=5)
            8
            sage: f_sub = f.subs(x=1); f_sub
            t + y
            sage: f_sub.parent() == f.parent()
            True
            sage: f.subs(y=2)
            t + 2*x
            sage: f_sub = f.subs(x=1, y=1, t=1); f_sub
            2
            sage: f_sub.parent() == M
            True

        Test that substitution works for rational functions::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^4 - 3)
            sage: f = x / y
            sage: f.subs(x=2) == 2 / y
            True
            sage: f.subs(y=3)
            9*x
            sage: f.subs(t=-1) is f
            True
            sage: f.subs({x: 2, y: 4})
            128/3

        Make sure that we return the same object when there is no
        substitution::

            sage: K = GF(7)
            sage: Kx.<x> = FunctionField(K)
            sage: y = polygen(Kx)
            sage: f = x^6 + 3
            sage: g = f.subs(z=2)
            sage: g == f
            True
            sage: g is f
            True

        Same purpose as above but over an extension field over the rationals::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = t + x*y
            sage: f.subs() is f
            True
            sage: f.subs(w=7) is f
            True
            sage: f.subs(w=7) is f.subs(w=7)
            True
            sage: f.subs(y=y) is f
            True
            sage: f.subs({y: y}) is f
            True
            sage: f.subs(x=x, y=y, t=t) is f
            True

        Test proper handling of not making substitutions::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs() is f
            True
            sage: f.subs(dict()) is f
            True
            sage: f.subs(w=0) is f
            True
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: f = 3*y
            sage: f.subs(x=0)
            3*y
            sage: f = 3*y
            sage: f.subs(x=0, y=y)
            3*y

        Test error handling for wrong argument type::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs(0)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

        Test error handling for dictionary with keys that don't match
        generators::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs({1: 1})
            Traceback (most recent call last):
            ...
            TypeError: key does not match any field generators

        Test error handling with ambiguously named generators::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<x> = K[]
            sage: L.<x> = K.extension(x^3 - x)
            sage: str(L.gen()) == str(K.gen())
            True
            sage: f = K.gen() - L.gen()
            sage: f.subs(x=2)
            Traceback (most recent call last):
            ...
            TypeError: multiple generators have the same name, making substitution ambiguous. Rename generators or pass substitution values in using dictionary format
            sage: f.subs({K.gen(): 1})
            -x + 1
            sage: f.subs({L.gen(): 2})
            x - 2
            sage: f.subs({K.gen(): 1, L.gen(): 2})
            -1
            sage: f.subs({K.gen(): 2, L.gen(): 1})
            1"""
    @overload
    def subs(self) -> Any:
        """FunctionFieldElement.subs(self, in_dict=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 180)

        Substitute the given generators with given values while not touching
        other generators.

        INPUT:

        - ``in_dict`` -- (optional) dictionary of inputs

        - ``**kwds`` -- named parameters

        OUTPUT: new object if substitution is possible, otherwise ``self``

        EXAMPLES:

        Basic substitution::

            sage: K = GF(7)
            sage: Kx.<x> = FunctionField(K)
            sage: y = polygen(Kx)
            sage: f = x^6 + 3; f
            x^6 + 3

        We also substitute the generators in any base fields::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = 7 * t + 3*x*y
            sage: f.subs(t=9)
            3*x*y + 63
            sage: f.subs(x=2, y=4)
            7*t + 24
            sage: f.subs(t=1, x=2, y=3)
            25

        Because of the possibility of extension fields, a generator to
        substitute must be specified::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs(2)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

            sage: # needs sage.rings.function_field
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: f = x + y
            sage: f.subs(0)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

        We can also substitute using dictionary syntax::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = x + y + t
            sage: f.subs({x: 1, y: 3, t: 4})
            8
            sage: f.subs({x: 1, t: 4})
            y + 5

        TESTS:

        Check that we correctly handle extension fields::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = t + x*y
            sage: f.subs(x=1, y=3, t=5)
            8
            sage: f_sub = f.subs(x=1); f_sub
            t + y
            sage: f_sub.parent() == f.parent()
            True
            sage: f.subs(y=2)
            t + 2*x
            sage: f_sub = f.subs(x=1, y=1, t=1); f_sub
            2
            sage: f_sub.parent() == M
            True

        Test that substitution works for rational functions::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^4 - 3)
            sage: f = x / y
            sage: f.subs(x=2) == 2 / y
            True
            sage: f.subs(y=3)
            9*x
            sage: f.subs(t=-1) is f
            True
            sage: f.subs({x: 2, y: 4})
            128/3

        Make sure that we return the same object when there is no
        substitution::

            sage: K = GF(7)
            sage: Kx.<x> = FunctionField(K)
            sage: y = polygen(Kx)
            sage: f = x^6 + 3
            sage: g = f.subs(z=2)
            sage: g == f
            True
            sage: g is f
            True

        Same purpose as above but over an extension field over the rationals::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = t + x*y
            sage: f.subs() is f
            True
            sage: f.subs(w=7) is f
            True
            sage: f.subs(w=7) is f.subs(w=7)
            True
            sage: f.subs(y=y) is f
            True
            sage: f.subs({y: y}) is f
            True
            sage: f.subs(x=x, y=y, t=t) is f
            True

        Test proper handling of not making substitutions::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs() is f
            True
            sage: f.subs(dict()) is f
            True
            sage: f.subs(w=0) is f
            True
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: f = 3*y
            sage: f.subs(x=0)
            3*y
            sage: f = 3*y
            sage: f.subs(x=0, y=y)
            3*y

        Test error handling for wrong argument type::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs(0)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

        Test error handling for dictionary with keys that don't match
        generators::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs({1: 1})
            Traceback (most recent call last):
            ...
            TypeError: key does not match any field generators

        Test error handling with ambiguously named generators::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<x> = K[]
            sage: L.<x> = K.extension(x^3 - x)
            sage: str(L.gen()) == str(K.gen())
            True
            sage: f = K.gen() - L.gen()
            sage: f.subs(x=2)
            Traceback (most recent call last):
            ...
            TypeError: multiple generators have the same name, making substitution ambiguous. Rename generators or pass substitution values in using dictionary format
            sage: f.subs({K.gen(): 1})
            -x + 1
            sage: f.subs({L.gen(): 2})
            x - 2
            sage: f.subs({K.gen(): 1, L.gen(): 2})
            -1
            sage: f.subs({K.gen(): 2, L.gen(): 1})
            1"""
    @overload
    def subs(self, w=...) -> Any:
        """FunctionFieldElement.subs(self, in_dict=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 180)

        Substitute the given generators with given values while not touching
        other generators.

        INPUT:

        - ``in_dict`` -- (optional) dictionary of inputs

        - ``**kwds`` -- named parameters

        OUTPUT: new object if substitution is possible, otherwise ``self``

        EXAMPLES:

        Basic substitution::

            sage: K = GF(7)
            sage: Kx.<x> = FunctionField(K)
            sage: y = polygen(Kx)
            sage: f = x^6 + 3; f
            x^6 + 3

        We also substitute the generators in any base fields::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = 7 * t + 3*x*y
            sage: f.subs(t=9)
            3*x*y + 63
            sage: f.subs(x=2, y=4)
            7*t + 24
            sage: f.subs(t=1, x=2, y=3)
            25

        Because of the possibility of extension fields, a generator to
        substitute must be specified::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs(2)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

            sage: # needs sage.rings.function_field
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: f = x + y
            sage: f.subs(0)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

        We can also substitute using dictionary syntax::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = x + y + t
            sage: f.subs({x: 1, y: 3, t: 4})
            8
            sage: f.subs({x: 1, t: 4})
            y + 5

        TESTS:

        Check that we correctly handle extension fields::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = t + x*y
            sage: f.subs(x=1, y=3, t=5)
            8
            sage: f_sub = f.subs(x=1); f_sub
            t + y
            sage: f_sub.parent() == f.parent()
            True
            sage: f.subs(y=2)
            t + 2*x
            sage: f_sub = f.subs(x=1, y=1, t=1); f_sub
            2
            sage: f_sub.parent() == M
            True

        Test that substitution works for rational functions::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^4 - 3)
            sage: f = x / y
            sage: f.subs(x=2) == 2 / y
            True
            sage: f.subs(y=3)
            9*x
            sage: f.subs(t=-1) is f
            True
            sage: f.subs({x: 2, y: 4})
            128/3

        Make sure that we return the same object when there is no
        substitution::

            sage: K = GF(7)
            sage: Kx.<x> = FunctionField(K)
            sage: y = polygen(Kx)
            sage: f = x^6 + 3
            sage: g = f.subs(z=2)
            sage: g == f
            True
            sage: g is f
            True

        Same purpose as above but over an extension field over the rationals::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = t + x*y
            sage: f.subs() is f
            True
            sage: f.subs(w=7) is f
            True
            sage: f.subs(w=7) is f.subs(w=7)
            True
            sage: f.subs(y=y) is f
            True
            sage: f.subs({y: y}) is f
            True
            sage: f.subs(x=x, y=y, t=t) is f
            True

        Test proper handling of not making substitutions::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs() is f
            True
            sage: f.subs(dict()) is f
            True
            sage: f.subs(w=0) is f
            True
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: f = 3*y
            sage: f.subs(x=0)
            3*y
            sage: f = 3*y
            sage: f.subs(x=0, y=y)
            3*y

        Test error handling for wrong argument type::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs(0)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

        Test error handling for dictionary with keys that don't match
        generators::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs({1: 1})
            Traceback (most recent call last):
            ...
            TypeError: key does not match any field generators

        Test error handling with ambiguously named generators::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<x> = K[]
            sage: L.<x> = K.extension(x^3 - x)
            sage: str(L.gen()) == str(K.gen())
            True
            sage: f = K.gen() - L.gen()
            sage: f.subs(x=2)
            Traceback (most recent call last):
            ...
            TypeError: multiple generators have the same name, making substitution ambiguous. Rename generators or pass substitution values in using dictionary format
            sage: f.subs({K.gen(): 1})
            -x + 1
            sage: f.subs({L.gen(): 2})
            x - 2
            sage: f.subs({K.gen(): 1, L.gen(): 2})
            -1
            sage: f.subs({K.gen(): 2, L.gen(): 1})
            1"""
    @overload
    def subs(self, y=...) -> Any:
        """FunctionFieldElement.subs(self, in_dict=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 180)

        Substitute the given generators with given values while not touching
        other generators.

        INPUT:

        - ``in_dict`` -- (optional) dictionary of inputs

        - ``**kwds`` -- named parameters

        OUTPUT: new object if substitution is possible, otherwise ``self``

        EXAMPLES:

        Basic substitution::

            sage: K = GF(7)
            sage: Kx.<x> = FunctionField(K)
            sage: y = polygen(Kx)
            sage: f = x^6 + 3; f
            x^6 + 3

        We also substitute the generators in any base fields::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = 7 * t + 3*x*y
            sage: f.subs(t=9)
            3*x*y + 63
            sage: f.subs(x=2, y=4)
            7*t + 24
            sage: f.subs(t=1, x=2, y=3)
            25

        Because of the possibility of extension fields, a generator to
        substitute must be specified::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs(2)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

            sage: # needs sage.rings.function_field
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: f = x + y
            sage: f.subs(0)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

        We can also substitute using dictionary syntax::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = x + y + t
            sage: f.subs({x: 1, y: 3, t: 4})
            8
            sage: f.subs({x: 1, t: 4})
            y + 5

        TESTS:

        Check that we correctly handle extension fields::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = t + x*y
            sage: f.subs(x=1, y=3, t=5)
            8
            sage: f_sub = f.subs(x=1); f_sub
            t + y
            sage: f_sub.parent() == f.parent()
            True
            sage: f.subs(y=2)
            t + 2*x
            sage: f_sub = f.subs(x=1, y=1, t=1); f_sub
            2
            sage: f_sub.parent() == M
            True

        Test that substitution works for rational functions::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^4 - 3)
            sage: f = x / y
            sage: f.subs(x=2) == 2 / y
            True
            sage: f.subs(y=3)
            9*x
            sage: f.subs(t=-1) is f
            True
            sage: f.subs({x: 2, y: 4})
            128/3

        Make sure that we return the same object when there is no
        substitution::

            sage: K = GF(7)
            sage: Kx.<x> = FunctionField(K)
            sage: y = polygen(Kx)
            sage: f = x^6 + 3
            sage: g = f.subs(z=2)
            sage: g == f
            True
            sage: g is f
            True

        Same purpose as above but over an extension field over the rationals::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = t + x*y
            sage: f.subs() is f
            True
            sage: f.subs(w=7) is f
            True
            sage: f.subs(w=7) is f.subs(w=7)
            True
            sage: f.subs(y=y) is f
            True
            sage: f.subs({y: y}) is f
            True
            sage: f.subs(x=x, y=y, t=t) is f
            True

        Test proper handling of not making substitutions::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs() is f
            True
            sage: f.subs(dict()) is f
            True
            sage: f.subs(w=0) is f
            True
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: f = 3*y
            sage: f.subs(x=0)
            3*y
            sage: f = 3*y
            sage: f.subs(x=0, y=y)
            3*y

        Test error handling for wrong argument type::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs(0)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

        Test error handling for dictionary with keys that don't match
        generators::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs({1: 1})
            Traceback (most recent call last):
            ...
            TypeError: key does not match any field generators

        Test error handling with ambiguously named generators::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<x> = K[]
            sage: L.<x> = K.extension(x^3 - x)
            sage: str(L.gen()) == str(K.gen())
            True
            sage: f = K.gen() - L.gen()
            sage: f.subs(x=2)
            Traceback (most recent call last):
            ...
            TypeError: multiple generators have the same name, making substitution ambiguous. Rename generators or pass substitution values in using dictionary format
            sage: f.subs({K.gen(): 1})
            -x + 1
            sage: f.subs({L.gen(): 2})
            x - 2
            sage: f.subs({K.gen(): 1, L.gen(): 2})
            -1
            sage: f.subs({K.gen(): 2, L.gen(): 1})
            1"""
    @overload
    def subs(self, x=..., y=..., t=...) -> Any:
        """FunctionFieldElement.subs(self, in_dict=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 180)

        Substitute the given generators with given values while not touching
        other generators.

        INPUT:

        - ``in_dict`` -- (optional) dictionary of inputs

        - ``**kwds`` -- named parameters

        OUTPUT: new object if substitution is possible, otherwise ``self``

        EXAMPLES:

        Basic substitution::

            sage: K = GF(7)
            sage: Kx.<x> = FunctionField(K)
            sage: y = polygen(Kx)
            sage: f = x^6 + 3; f
            x^6 + 3

        We also substitute the generators in any base fields::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = 7 * t + 3*x*y
            sage: f.subs(t=9)
            3*x*y + 63
            sage: f.subs(x=2, y=4)
            7*t + 24
            sage: f.subs(t=1, x=2, y=3)
            25

        Because of the possibility of extension fields, a generator to
        substitute must be specified::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs(2)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

            sage: # needs sage.rings.function_field
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: f = x + y
            sage: f.subs(0)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

        We can also substitute using dictionary syntax::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = x + y + t
            sage: f.subs({x: 1, y: 3, t: 4})
            8
            sage: f.subs({x: 1, t: 4})
            y + 5

        TESTS:

        Check that we correctly handle extension fields::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = t + x*y
            sage: f.subs(x=1, y=3, t=5)
            8
            sage: f_sub = f.subs(x=1); f_sub
            t + y
            sage: f_sub.parent() == f.parent()
            True
            sage: f.subs(y=2)
            t + 2*x
            sage: f_sub = f.subs(x=1, y=1, t=1); f_sub
            2
            sage: f_sub.parent() == M
            True

        Test that substitution works for rational functions::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^4 - 3)
            sage: f = x / y
            sage: f.subs(x=2) == 2 / y
            True
            sage: f.subs(y=3)
            9*x
            sage: f.subs(t=-1) is f
            True
            sage: f.subs({x: 2, y: 4})
            128/3

        Make sure that we return the same object when there is no
        substitution::

            sage: K = GF(7)
            sage: Kx.<x> = FunctionField(K)
            sage: y = polygen(Kx)
            sage: f = x^6 + 3
            sage: g = f.subs(z=2)
            sage: g == f
            True
            sage: g is f
            True

        Same purpose as above but over an extension field over the rationals::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = t + x*y
            sage: f.subs() is f
            True
            sage: f.subs(w=7) is f
            True
            sage: f.subs(w=7) is f.subs(w=7)
            True
            sage: f.subs(y=y) is f
            True
            sage: f.subs({y: y}) is f
            True
            sage: f.subs(x=x, y=y, t=t) is f
            True

        Test proper handling of not making substitutions::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs() is f
            True
            sage: f.subs(dict()) is f
            True
            sage: f.subs(w=0) is f
            True
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: f = 3*y
            sage: f.subs(x=0)
            3*y
            sage: f = 3*y
            sage: f.subs(x=0, y=y)
            3*y

        Test error handling for wrong argument type::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs(0)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

        Test error handling for dictionary with keys that don't match
        generators::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs({1: 1})
            Traceback (most recent call last):
            ...
            TypeError: key does not match any field generators

        Test error handling with ambiguously named generators::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<x> = K[]
            sage: L.<x> = K.extension(x^3 - x)
            sage: str(L.gen()) == str(K.gen())
            True
            sage: f = K.gen() - L.gen()
            sage: f.subs(x=2)
            Traceback (most recent call last):
            ...
            TypeError: multiple generators have the same name, making substitution ambiguous. Rename generators or pass substitution values in using dictionary format
            sage: f.subs({K.gen(): 1})
            -x + 1
            sage: f.subs({L.gen(): 2})
            x - 2
            sage: f.subs({K.gen(): 1, L.gen(): 2})
            -1
            sage: f.subs({K.gen(): 2, L.gen(): 1})
            1"""
    @overload
    def subs(self) -> Any:
        """FunctionFieldElement.subs(self, in_dict=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 180)

        Substitute the given generators with given values while not touching
        other generators.

        INPUT:

        - ``in_dict`` -- (optional) dictionary of inputs

        - ``**kwds`` -- named parameters

        OUTPUT: new object if substitution is possible, otherwise ``self``

        EXAMPLES:

        Basic substitution::

            sage: K = GF(7)
            sage: Kx.<x> = FunctionField(K)
            sage: y = polygen(Kx)
            sage: f = x^6 + 3; f
            x^6 + 3

        We also substitute the generators in any base fields::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = 7 * t + 3*x*y
            sage: f.subs(t=9)
            3*x*y + 63
            sage: f.subs(x=2, y=4)
            7*t + 24
            sage: f.subs(t=1, x=2, y=3)
            25

        Because of the possibility of extension fields, a generator to
        substitute must be specified::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs(2)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

            sage: # needs sage.rings.function_field
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: f = x + y
            sage: f.subs(0)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

        We can also substitute using dictionary syntax::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = x + y + t
            sage: f.subs({x: 1, y: 3, t: 4})
            8
            sage: f.subs({x: 1, t: 4})
            y + 5

        TESTS:

        Check that we correctly handle extension fields::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = t + x*y
            sage: f.subs(x=1, y=3, t=5)
            8
            sage: f_sub = f.subs(x=1); f_sub
            t + y
            sage: f_sub.parent() == f.parent()
            True
            sage: f.subs(y=2)
            t + 2*x
            sage: f_sub = f.subs(x=1, y=1, t=1); f_sub
            2
            sage: f_sub.parent() == M
            True

        Test that substitution works for rational functions::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^4 - 3)
            sage: f = x / y
            sage: f.subs(x=2) == 2 / y
            True
            sage: f.subs(y=3)
            9*x
            sage: f.subs(t=-1) is f
            True
            sage: f.subs({x: 2, y: 4})
            128/3

        Make sure that we return the same object when there is no
        substitution::

            sage: K = GF(7)
            sage: Kx.<x> = FunctionField(K)
            sage: y = polygen(Kx)
            sage: f = x^6 + 3
            sage: g = f.subs(z=2)
            sage: g == f
            True
            sage: g is f
            True

        Same purpose as above but over an extension field over the rationals::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = t + x*y
            sage: f.subs() is f
            True
            sage: f.subs(w=7) is f
            True
            sage: f.subs(w=7) is f.subs(w=7)
            True
            sage: f.subs(y=y) is f
            True
            sage: f.subs({y: y}) is f
            True
            sage: f.subs(x=x, y=y, t=t) is f
            True

        Test proper handling of not making substitutions::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs() is f
            True
            sage: f.subs(dict()) is f
            True
            sage: f.subs(w=0) is f
            True
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: f = 3*y
            sage: f.subs(x=0)
            3*y
            sage: f = 3*y
            sage: f.subs(x=0, y=y)
            3*y

        Test error handling for wrong argument type::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs(0)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

        Test error handling for dictionary with keys that don't match
        generators::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs({1: 1})
            Traceback (most recent call last):
            ...
            TypeError: key does not match any field generators

        Test error handling with ambiguously named generators::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<x> = K[]
            sage: L.<x> = K.extension(x^3 - x)
            sage: str(L.gen()) == str(K.gen())
            True
            sage: f = K.gen() - L.gen()
            sage: f.subs(x=2)
            Traceback (most recent call last):
            ...
            TypeError: multiple generators have the same name, making substitution ambiguous. Rename generators or pass substitution values in using dictionary format
            sage: f.subs({K.gen(): 1})
            -x + 1
            sage: f.subs({L.gen(): 2})
            x - 2
            sage: f.subs({K.gen(): 1, L.gen(): 2})
            -1
            sage: f.subs({K.gen(): 2, L.gen(): 1})
            1"""
    @overload
    def subs(self, w=...) -> Any:
        """FunctionFieldElement.subs(self, in_dict=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 180)

        Substitute the given generators with given values while not touching
        other generators.

        INPUT:

        - ``in_dict`` -- (optional) dictionary of inputs

        - ``**kwds`` -- named parameters

        OUTPUT: new object if substitution is possible, otherwise ``self``

        EXAMPLES:

        Basic substitution::

            sage: K = GF(7)
            sage: Kx.<x> = FunctionField(K)
            sage: y = polygen(Kx)
            sage: f = x^6 + 3; f
            x^6 + 3

        We also substitute the generators in any base fields::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = 7 * t + 3*x*y
            sage: f.subs(t=9)
            3*x*y + 63
            sage: f.subs(x=2, y=4)
            7*t + 24
            sage: f.subs(t=1, x=2, y=3)
            25

        Because of the possibility of extension fields, a generator to
        substitute must be specified::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs(2)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

            sage: # needs sage.rings.function_field
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: f = x + y
            sage: f.subs(0)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

        We can also substitute using dictionary syntax::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = x + y + t
            sage: f.subs({x: 1, y: 3, t: 4})
            8
            sage: f.subs({x: 1, t: 4})
            y + 5

        TESTS:

        Check that we correctly handle extension fields::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = t + x*y
            sage: f.subs(x=1, y=3, t=5)
            8
            sage: f_sub = f.subs(x=1); f_sub
            t + y
            sage: f_sub.parent() == f.parent()
            True
            sage: f.subs(y=2)
            t + 2*x
            sage: f_sub = f.subs(x=1, y=1, t=1); f_sub
            2
            sage: f_sub.parent() == M
            True

        Test that substitution works for rational functions::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^4 - 3)
            sage: f = x / y
            sage: f.subs(x=2) == 2 / y
            True
            sage: f.subs(y=3)
            9*x
            sage: f.subs(t=-1) is f
            True
            sage: f.subs({x: 2, y: 4})
            128/3

        Make sure that we return the same object when there is no
        substitution::

            sage: K = GF(7)
            sage: Kx.<x> = FunctionField(K)
            sage: y = polygen(Kx)
            sage: f = x^6 + 3
            sage: g = f.subs(z=2)
            sage: g == f
            True
            sage: g is f
            True

        Same purpose as above but over an extension field over the rationals::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = t + x*y
            sage: f.subs() is f
            True
            sage: f.subs(w=7) is f
            True
            sage: f.subs(w=7) is f.subs(w=7)
            True
            sage: f.subs(y=y) is f
            True
            sage: f.subs({y: y}) is f
            True
            sage: f.subs(x=x, y=y, t=t) is f
            True

        Test proper handling of not making substitutions::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs() is f
            True
            sage: f.subs(dict()) is f
            True
            sage: f.subs(w=0) is f
            True
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: f = 3*y
            sage: f.subs(x=0)
            3*y
            sage: f = 3*y
            sage: f.subs(x=0, y=y)
            3*y

        Test error handling for wrong argument type::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs(0)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

        Test error handling for dictionary with keys that don't match
        generators::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs({1: 1})
            Traceback (most recent call last):
            ...
            TypeError: key does not match any field generators

        Test error handling with ambiguously named generators::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<x> = K[]
            sage: L.<x> = K.extension(x^3 - x)
            sage: str(L.gen()) == str(K.gen())
            True
            sage: f = K.gen() - L.gen()
            sage: f.subs(x=2)
            Traceback (most recent call last):
            ...
            TypeError: multiple generators have the same name, making substitution ambiguous. Rename generators or pass substitution values in using dictionary format
            sage: f.subs({K.gen(): 1})
            -x + 1
            sage: f.subs({L.gen(): 2})
            x - 2
            sage: f.subs({K.gen(): 1, L.gen(): 2})
            -1
            sage: f.subs({K.gen(): 2, L.gen(): 1})
            1"""
    @overload
    def subs(self, x=...) -> Any:
        """FunctionFieldElement.subs(self, in_dict=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 180)

        Substitute the given generators with given values while not touching
        other generators.

        INPUT:

        - ``in_dict`` -- (optional) dictionary of inputs

        - ``**kwds`` -- named parameters

        OUTPUT: new object if substitution is possible, otherwise ``self``

        EXAMPLES:

        Basic substitution::

            sage: K = GF(7)
            sage: Kx.<x> = FunctionField(K)
            sage: y = polygen(Kx)
            sage: f = x^6 + 3; f
            x^6 + 3

        We also substitute the generators in any base fields::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = 7 * t + 3*x*y
            sage: f.subs(t=9)
            3*x*y + 63
            sage: f.subs(x=2, y=4)
            7*t + 24
            sage: f.subs(t=1, x=2, y=3)
            25

        Because of the possibility of extension fields, a generator to
        substitute must be specified::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs(2)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

            sage: # needs sage.rings.function_field
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: f = x + y
            sage: f.subs(0)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

        We can also substitute using dictionary syntax::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = x + y + t
            sage: f.subs({x: 1, y: 3, t: 4})
            8
            sage: f.subs({x: 1, t: 4})
            y + 5

        TESTS:

        Check that we correctly handle extension fields::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = t + x*y
            sage: f.subs(x=1, y=3, t=5)
            8
            sage: f_sub = f.subs(x=1); f_sub
            t + y
            sage: f_sub.parent() == f.parent()
            True
            sage: f.subs(y=2)
            t + 2*x
            sage: f_sub = f.subs(x=1, y=1, t=1); f_sub
            2
            sage: f_sub.parent() == M
            True

        Test that substitution works for rational functions::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^4 - 3)
            sage: f = x / y
            sage: f.subs(x=2) == 2 / y
            True
            sage: f.subs(y=3)
            9*x
            sage: f.subs(t=-1) is f
            True
            sage: f.subs({x: 2, y: 4})
            128/3

        Make sure that we return the same object when there is no
        substitution::

            sage: K = GF(7)
            sage: Kx.<x> = FunctionField(K)
            sage: y = polygen(Kx)
            sage: f = x^6 + 3
            sage: g = f.subs(z=2)
            sage: g == f
            True
            sage: g is f
            True

        Same purpose as above but over an extension field over the rationals::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = t + x*y
            sage: f.subs() is f
            True
            sage: f.subs(w=7) is f
            True
            sage: f.subs(w=7) is f.subs(w=7)
            True
            sage: f.subs(y=y) is f
            True
            sage: f.subs({y: y}) is f
            True
            sage: f.subs(x=x, y=y, t=t) is f
            True

        Test proper handling of not making substitutions::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs() is f
            True
            sage: f.subs(dict()) is f
            True
            sage: f.subs(w=0) is f
            True
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: f = 3*y
            sage: f.subs(x=0)
            3*y
            sage: f = 3*y
            sage: f.subs(x=0, y=y)
            3*y

        Test error handling for wrong argument type::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs(0)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

        Test error handling for dictionary with keys that don't match
        generators::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs({1: 1})
            Traceback (most recent call last):
            ...
            TypeError: key does not match any field generators

        Test error handling with ambiguously named generators::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<x> = K[]
            sage: L.<x> = K.extension(x^3 - x)
            sage: str(L.gen()) == str(K.gen())
            True
            sage: f = K.gen() - L.gen()
            sage: f.subs(x=2)
            Traceback (most recent call last):
            ...
            TypeError: multiple generators have the same name, making substitution ambiguous. Rename generators or pass substitution values in using dictionary format
            sage: f.subs({K.gen(): 1})
            -x + 1
            sage: f.subs({L.gen(): 2})
            x - 2
            sage: f.subs({K.gen(): 1, L.gen(): 2})
            -1
            sage: f.subs({K.gen(): 2, L.gen(): 1})
            1"""
    @overload
    def subs(self, x=..., y=...) -> Any:
        """FunctionFieldElement.subs(self, in_dict=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 180)

        Substitute the given generators with given values while not touching
        other generators.

        INPUT:

        - ``in_dict`` -- (optional) dictionary of inputs

        - ``**kwds`` -- named parameters

        OUTPUT: new object if substitution is possible, otherwise ``self``

        EXAMPLES:

        Basic substitution::

            sage: K = GF(7)
            sage: Kx.<x> = FunctionField(K)
            sage: y = polygen(Kx)
            sage: f = x^6 + 3; f
            x^6 + 3

        We also substitute the generators in any base fields::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = 7 * t + 3*x*y
            sage: f.subs(t=9)
            3*x*y + 63
            sage: f.subs(x=2, y=4)
            7*t + 24
            sage: f.subs(t=1, x=2, y=3)
            25

        Because of the possibility of extension fields, a generator to
        substitute must be specified::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs(2)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

            sage: # needs sage.rings.function_field
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: f = x + y
            sage: f.subs(0)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

        We can also substitute using dictionary syntax::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = x + y + t
            sage: f.subs({x: 1, y: 3, t: 4})
            8
            sage: f.subs({x: 1, t: 4})
            y + 5

        TESTS:

        Check that we correctly handle extension fields::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = t + x*y
            sage: f.subs(x=1, y=3, t=5)
            8
            sage: f_sub = f.subs(x=1); f_sub
            t + y
            sage: f_sub.parent() == f.parent()
            True
            sage: f.subs(y=2)
            t + 2*x
            sage: f_sub = f.subs(x=1, y=1, t=1); f_sub
            2
            sage: f_sub.parent() == M
            True

        Test that substitution works for rational functions::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^4 - 3)
            sage: f = x / y
            sage: f.subs(x=2) == 2 / y
            True
            sage: f.subs(y=3)
            9*x
            sage: f.subs(t=-1) is f
            True
            sage: f.subs({x: 2, y: 4})
            128/3

        Make sure that we return the same object when there is no
        substitution::

            sage: K = GF(7)
            sage: Kx.<x> = FunctionField(K)
            sage: y = polygen(Kx)
            sage: f = x^6 + 3
            sage: g = f.subs(z=2)
            sage: g == f
            True
            sage: g is f
            True

        Same purpose as above but over an extension field over the rationals::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: S.<t> = L[]
            sage: M.<t> = L.extension(t^2 - x*y)
            sage: f = t + x*y
            sage: f.subs() is f
            True
            sage: f.subs(w=7) is f
            True
            sage: f.subs(w=7) is f.subs(w=7)
            True
            sage: f.subs(y=y) is f
            True
            sage: f.subs({y: y}) is f
            True
            sage: f.subs(x=x, y=y, t=t) is f
            True

        Test proper handling of not making substitutions::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs() is f
            True
            sage: f.subs(dict()) is f
            True
            sage: f.subs(w=0) is f
            True
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: f = 3*y
            sage: f.subs(x=0)
            3*y
            sage: f = 3*y
            sage: f.subs(x=0, y=y)
            3*y

        Test error handling for wrong argument type::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs(0)
            Traceback (most recent call last):
            ...
            TypeError: in_dict must be a dict

        Test error handling for dictionary with keys that don't match
        generators::

            sage: K.<x> = FunctionField(QQ)
            sage: f = x
            sage: f.subs({1: 1})
            Traceback (most recent call last):
            ...
            TypeError: key does not match any field generators

        Test error handling with ambiguously named generators::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<x> = K[]
            sage: L.<x> = K.extension(x^3 - x)
            sage: str(L.gen()) == str(K.gen())
            True
            sage: f = K.gen() - L.gen()
            sage: f.subs(x=2)
            Traceback (most recent call last):
            ...
            TypeError: multiple generators have the same name, making substitution ambiguous. Rename generators or pass substitution values in using dictionary format
            sage: f.subs({K.gen(): 1})
            -x + 1
            sage: f.subs({L.gen(): 2})
            x - 2
            sage: f.subs({K.gen(): 1, L.gen(): 2})
            -1
            sage: f.subs({K.gen(): 2, L.gen(): 1})
            1"""
    @overload
    def trace(self) -> Any:
        """FunctionFieldElement.trace(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 525)

        Return the trace of the element.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3)                                # needs sage.rings.function_field
            sage: y.trace()                                                             # needs sage.rings.function_field
            x"""
    @overload
    def trace(self) -> Any:
        """FunctionFieldElement.trace(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 525)

        Return the trace of the element.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3)                                # needs sage.rings.function_field
            sage: y.trace()                                                             # needs sage.rings.function_field
            x"""
    @overload
    def valuation(self, place) -> Any:
        """FunctionFieldElement.valuation(self, place)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 879)

        Return the valuation of the element at the place.

        INPUT:

        - ``place`` -- a place of the function field

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)                                # needs sage.rings.function_field
            sage: p = L.places_infinite()[0]                                            # needs sage.rings.function_field
            sage: y.valuation(p)                                                        # needs sage.rings.function_field
            -1

        ::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: O = L.maximal_order()
            sage: p = O.ideal(x - 1).place()
            sage: y.valuation(p)
            0"""
    @overload
    def valuation(self, p) -> Any:
        """FunctionFieldElement.valuation(self, place)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 879)

        Return the valuation of the element at the place.

        INPUT:

        - ``place`` -- a place of the function field

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)                                # needs sage.rings.function_field
            sage: p = L.places_infinite()[0]                                            # needs sage.rings.function_field
            sage: y.valuation(p)                                                        # needs sage.rings.function_field
            -1

        ::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: O = L.maximal_order()
            sage: p = O.ideal(x - 1).place()
            sage: y.valuation(p)
            0"""
    @overload
    def valuation(self, p) -> Any:
        """FunctionFieldElement.valuation(self, place)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 879)

        Return the valuation of the element at the place.

        INPUT:

        - ``place`` -- a place of the function field

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)                                # needs sage.rings.function_field
            sage: p = L.places_infinite()[0]                                            # needs sage.rings.function_field
            sage: y.valuation(p)                                                        # needs sage.rings.function_field
            -1

        ::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: O = L.maximal_order()
            sage: p = O.ideal(x - 1).place()
            sage: y.valuation(p)
            0"""
    @overload
    def zeros(self) -> Any:
        """FunctionFieldElement.zeros(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 839)

        Return the list of the zeros of the element.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(2))
            sage: f = 1/(x^3 + x^2 + x)
            sage: f.zeros()                                                             # needs sage.libs.pari sage.modules
            [Place (1/x)]

        ::

            sage: K.<x> = FunctionField(GF(4)); _.<Y> = K[]                             # needs sage.rings.finite_rings
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)                                # needs sage.rings.finite_rings sage.rings.function_field
            sage: (x/y).zeros()                                                         # needs sage.rings.finite_rings sage.rings.function_field
            [Place (x, x*y)]"""
    @overload
    def zeros(self) -> Any:
        """FunctionFieldElement.zeros(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 839)

        Return the list of the zeros of the element.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(2))
            sage: f = 1/(x^3 + x^2 + x)
            sage: f.zeros()                                                             # needs sage.libs.pari sage.modules
            [Place (1/x)]

        ::

            sage: K.<x> = FunctionField(GF(4)); _.<Y> = K[]                             # needs sage.rings.finite_rings
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)                                # needs sage.rings.finite_rings sage.rings.function_field
            sage: (x/y).zeros()                                                         # needs sage.rings.finite_rings sage.rings.function_field
            [Place (x, x*y)]"""
    @overload
    def zeros(self) -> Any:
        """FunctionFieldElement.zeros(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 839)

        Return the list of the zeros of the element.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(2))
            sage: f = 1/(x^3 + x^2 + x)
            sage: f.zeros()                                                             # needs sage.libs.pari sage.modules
            [Place (1/x)]

        ::

            sage: K.<x> = FunctionField(GF(4)); _.<Y> = K[]                             # needs sage.rings.finite_rings
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)                                # needs sage.rings.finite_rings sage.rings.function_field
            sage: (x/y).zeros()                                                         # needs sage.rings.finite_rings sage.rings.function_field
            [Place (x, x*y)]"""
    @overload
    def __pari__(self) -> Any:
        """FunctionFieldElement.__pari__(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 145)

        Coerce the element to PARI.

        PARI does not know about general function field elements, so this
        raises an Exception.

        TESTS:

        Check that :issue:`16369` has been resolved::

            sage: K.<a> = FunctionField(QQ)
            sage: R.<b> = K[]
            sage: L.<b> = K.extension(b^2 - a)                                          # needs sage.rings.function_field
            sage: b.__pari__()                                                          # needs sage.rings.function_field
            Traceback (most recent call last):
            ...
            NotImplementedError: PARI does not support general function field elements."""
    @overload
    def __pari__(self) -> Any:
        """FunctionFieldElement.__pari__(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 145)

        Coerce the element to PARI.

        PARI does not know about general function field elements, so this
        raises an Exception.

        TESTS:

        Check that :issue:`16369` has been resolved::

            sage: K.<a> = FunctionField(QQ)
            sage: R.<b> = K[]
            sage: L.<b> = K.extension(b^2 - a)                                          # needs sage.rings.function_field
            sage: b.__pari__()                                                          # needs sage.rings.function_field
            Traceback (most recent call last):
            ...
            NotImplementedError: PARI does not support general function field elements."""
    def __reduce__(self) -> Any:
        """FunctionFieldElement.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element.pyx (starting at line 127)

        EXAMPLES::

            sage: K = FunctionField(QQ,'x')
            sage: f = K.random_element()
            sage: loads(f.dumps()) == f
            True"""
