import _cython_3_2_1
import sage.categories.morphism
import sage.rings.number_field.number_field_element
from sage.categories.category import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

__pyx_capi__: dict
is_sqrt_disc: _cython_3_2_1.cython_function_or_method

class NumberFieldElement_gaussian(NumberFieldElement_quadratic_sqrt):
    """File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2532)

        An element of `\\QQ[i]`.

        Some methods of this class behave slightly differently than the
        corresponding methods of general elements of quadratic number fields,
        especially with regard to conversions to parents that can represent complex
        numbers in rectangular form.

        In addition, this class provides some convenience methods similar to methods
        of symbolic expressions to make the behavior of ``a + I*b`` with rational
        ``a``, ``b`` closer to that when ``a``, ``b`` are expressions.

        EXAMPLES::

            sage: type(I)
            <class 'sage.rings.number_field.number_field_element_quadratic.NumberFieldElement_gaussian'>

            sage: mi = QuadraticField(-1, embedding=CC(0,-1)).gen()
            sage: type(mi)
            <class 'sage.rings.number_field.number_field_element_quadratic.NumberFieldElement_gaussian'>
            sage: CC(mi)
            -1.00000000000000*I
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def imag(self) -> Any:
        """NumberFieldElement_gaussian.imag_part(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2633)

        Imaginary part.

        EXAMPLES::

            sage: (1 + 2*I).imag()
            2
            sage: (1 + 2*I).imag().parent()
            Rational Field

            sage: K.<mi> = QuadraticField(-1, embedding=CC(0,-1))
            sage: (1 - mi).imag()
            1"""
    @overload
    def imag(self) -> Any:
        """NumberFieldElement_gaussian.imag_part(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2633)

        Imaginary part.

        EXAMPLES::

            sage: (1 + 2*I).imag()
            2
            sage: (1 + 2*I).imag().parent()
            Rational Field

            sage: K.<mi> = QuadraticField(-1, embedding=CC(0,-1))
            sage: (1 - mi).imag()
            1"""
    @overload
    def imag(self) -> Any:
        """NumberFieldElement_gaussian.imag_part(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2633)

        Imaginary part.

        EXAMPLES::

            sage: (1 + 2*I).imag()
            2
            sage: (1 + 2*I).imag().parent()
            Rational Field

            sage: K.<mi> = QuadraticField(-1, embedding=CC(0,-1))
            sage: (1 - mi).imag()
            1"""
    def imag_part(self) -> Any:
        """NumberFieldElement_gaussian.imag_part(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2633)

        Imaginary part.

        EXAMPLES::

            sage: (1 + 2*I).imag()
            2
            sage: (1 + 2*I).imag().parent()
            Rational Field

            sage: K.<mi> = QuadraticField(-1, embedding=CC(0,-1))
            sage: (1 - mi).imag()
            1"""
    @overload
    def log(self, *args, **kwds) -> Any:
        """NumberFieldElement_gaussian.log(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2665)

        Complex logarithm (standard branch).

        EXAMPLES::

            sage: I.log()                                                               # needs sage.symbolic
            1/2*I*pi"""
    @overload
    def log(self) -> Any:
        """NumberFieldElement_gaussian.log(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2665)

        Complex logarithm (standard branch).

        EXAMPLES::

            sage: I.log()                                                               # needs sage.symbolic
            1/2*I*pi"""
    @overload
    def real(self) -> Any:
        """NumberFieldElement_gaussian.real_part(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2611)

        Real part.

        EXAMPLES::

            sage: (1 + 2*I).real()
            1
            sage: (1 + 2*I).real().parent()
            Rational Field"""
    @overload
    def real(self) -> Any:
        """NumberFieldElement_gaussian.real_part(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2611)

        Real part.

        EXAMPLES::

            sage: (1 + 2*I).real()
            1
            sage: (1 + 2*I).real().parent()
            Rational Field"""
    def real_part(self) -> Any:
        """NumberFieldElement_gaussian.real_part(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2611)

        Real part.

        EXAMPLES::

            sage: (1 + 2*I).real()
            1
            sage: (1 + 2*I).real().parent()
            Rational Field"""

class NumberFieldElement_quadratic(sage.rings.number_field.number_field_element.NumberFieldElement_absolute):
    """NumberFieldElement_quadratic(parent, f)

    File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 102)

    A :class:`NumberFieldElement_quadratic` object gives an efficient representation of
    an element of a quadratic extension of `\\QQ`.

    Elements are represented internally as triples `(a, b, c)` of integers,
    where `\\gcd(a, b, c) = 1` and `c > 0`, representing the element `(a +
    b \\sqrt{D}) / c`. Note that if the discriminant `D` is `1 \\bmod 4`,
    integral elements do not necessarily have `c = 1`.

    TESTS::

        sage: from sage.rings.number_field.number_field_element_quadratic import NumberFieldElement_quadratic
        sage: from sage.rings.number_field.number_field_element_quadratic import NumberFieldElement_quadratic_sqrt

    We set up some fields::

        sage: x = polygen(ZZ, 'x')
        sage: K.<a> = NumberField(x^2 + 23)
        sage: a.parts()
        (0, 1)
        sage: F.<b> = NumberField(x^2 - x + 7)
        sage: b.parts()
        (1/2, 3/2)

    We construct elements of these fields in various ways -- firstly, from
    polynomials::

        sage: NumberFieldElement_quadratic_sqrt(K, x - 1)
        a - 1
        sage: NumberFieldElement_quadratic(F, x - 1)
        b - 1

    From triples of Integers::

        sage: NumberFieldElement_quadratic_sqrt(K, (1,2,3))
        2/3*a + 1/3
        sage: NumberFieldElement_quadratic(F, (1,2,3))
        4/9*b + 1/9
        sage: NumberFieldElement_quadratic(F, (1,2,3)).parts()
        (1/3, 2/3)

    From pairs of Rationals::

        sage: NumberFieldElement_quadratic_sqrt(K, (1/2, 1/3))
        1/3*a + 1/2
        sage: NumberFieldElement_quadratic(F, (1/2, 1/3))
        2/9*b + 7/18
        sage: NumberFieldElement_quadratic(F, (1/2, 1/3)).parts()
        (1/2, 1/3)

    Direct from Rationals::

        sage: NumberFieldElement_quadratic_sqrt(K, 2/3)
        2/3
        sage: NumberFieldElement_quadratic(F, 2/3)
        2/3

    This checks a bug when converting from lists::

        sage: w = CyclotomicField(3)([1/2, 1])
        sage: w == w.__invert__().__invert__()
        True"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, f) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 167)

                Standard initialisation function.

                EXAMPLES::

                    sage: F.<a> = QuadraticField(-7)
                    sage: c = a + 7
                    sage: type(c) # indirect doctest
                    <class 'sage.rings.number_field.number_field_element_quadratic.NumberFieldElement_quadratic_sqrt'>
        """
    @overload
    def ceil(self) -> Any:
        """NumberFieldElement_quadratic.ceil(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2350)

        Return the ceil.

        EXAMPLES::

            sage: K.<sqrt7> = QuadraticField(7, name='sqrt7')
            sage: sqrt7.ceil()
            3
            sage: (-sqrt7).ceil()
            -2
            sage: (1022/313*sqrt7 - 14/23).ceil()
            9

        TESTS::

            sage: K2.<sqrt2> = QuadraticField(2)
            sage: K3.<sqrt3> = QuadraticField(3)
            sage: K5.<sqrt5> = QuadraticField(5)
            sage: for _ in range(100):
            ....:    a = QQ.random_element(1000,20)
            ....:    b = QQ.random_element(1000,20)
            ....:    assert ceil(a+b*sqrt(2.)) == ceil(a+b*sqrt2)
            ....:    assert ceil(a+b*sqrt(3.)) == ceil(a+b*sqrt3)
            ....:    assert ceil(a+b*sqrt(5.)) == ceil(a+b*sqrt5)

            sage: K = QuadraticField(-2)
            sage: l = [K(52), K(-3), K(43/12), K(-43/12)]
            sage: [x.ceil() for x in l]
            [52, -3, 4, -3]"""
    @overload
    def ceil(self) -> Any:
        """NumberFieldElement_quadratic.ceil(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2350)

        Return the ceil.

        EXAMPLES::

            sage: K.<sqrt7> = QuadraticField(7, name='sqrt7')
            sage: sqrt7.ceil()
            3
            sage: (-sqrt7).ceil()
            -2
            sage: (1022/313*sqrt7 - 14/23).ceil()
            9

        TESTS::

            sage: K2.<sqrt2> = QuadraticField(2)
            sage: K3.<sqrt3> = QuadraticField(3)
            sage: K5.<sqrt5> = QuadraticField(5)
            sage: for _ in range(100):
            ....:    a = QQ.random_element(1000,20)
            ....:    b = QQ.random_element(1000,20)
            ....:    assert ceil(a+b*sqrt(2.)) == ceil(a+b*sqrt2)
            ....:    assert ceil(a+b*sqrt(3.)) == ceil(a+b*sqrt3)
            ....:    assert ceil(a+b*sqrt(5.)) == ceil(a+b*sqrt5)

            sage: K = QuadraticField(-2)
            sage: l = [K(52), K(-3), K(43/12), K(-43/12)]
            sage: [x.ceil() for x in l]
            [52, -3, 4, -3]"""
    @overload
    def ceil(self) -> Any:
        """NumberFieldElement_quadratic.ceil(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2350)

        Return the ceil.

        EXAMPLES::

            sage: K.<sqrt7> = QuadraticField(7, name='sqrt7')
            sage: sqrt7.ceil()
            3
            sage: (-sqrt7).ceil()
            -2
            sage: (1022/313*sqrt7 - 14/23).ceil()
            9

        TESTS::

            sage: K2.<sqrt2> = QuadraticField(2)
            sage: K3.<sqrt3> = QuadraticField(3)
            sage: K5.<sqrt5> = QuadraticField(5)
            sage: for _ in range(100):
            ....:    a = QQ.random_element(1000,20)
            ....:    b = QQ.random_element(1000,20)
            ....:    assert ceil(a+b*sqrt(2.)) == ceil(a+b*sqrt2)
            ....:    assert ceil(a+b*sqrt(3.)) == ceil(a+b*sqrt3)
            ....:    assert ceil(a+b*sqrt(5.)) == ceil(a+b*sqrt5)

            sage: K = QuadraticField(-2)
            sage: l = [K(52), K(-3), K(43/12), K(-43/12)]
            sage: [x.ceil() for x in l]
            [52, -3, 4, -3]"""
    @overload
    def ceil(self) -> Any:
        """NumberFieldElement_quadratic.ceil(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2350)

        Return the ceil.

        EXAMPLES::

            sage: K.<sqrt7> = QuadraticField(7, name='sqrt7')
            sage: sqrt7.ceil()
            3
            sage: (-sqrt7).ceil()
            -2
            sage: (1022/313*sqrt7 - 14/23).ceil()
            9

        TESTS::

            sage: K2.<sqrt2> = QuadraticField(2)
            sage: K3.<sqrt3> = QuadraticField(3)
            sage: K5.<sqrt5> = QuadraticField(5)
            sage: for _ in range(100):
            ....:    a = QQ.random_element(1000,20)
            ....:    b = QQ.random_element(1000,20)
            ....:    assert ceil(a+b*sqrt(2.)) == ceil(a+b*sqrt2)
            ....:    assert ceil(a+b*sqrt(3.)) == ceil(a+b*sqrt3)
            ....:    assert ceil(a+b*sqrt(5.)) == ceil(a+b*sqrt5)

            sage: K = QuadraticField(-2)
            sage: l = [K(52), K(-3), K(43/12), K(-43/12)]
            sage: [x.ceil() for x in l]
            [52, -3, 4, -3]"""
    @overload
    def ceil(self) -> Any:
        """NumberFieldElement_quadratic.ceil(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2350)

        Return the ceil.

        EXAMPLES::

            sage: K.<sqrt7> = QuadraticField(7, name='sqrt7')
            sage: sqrt7.ceil()
            3
            sage: (-sqrt7).ceil()
            -2
            sage: (1022/313*sqrt7 - 14/23).ceil()
            9

        TESTS::

            sage: K2.<sqrt2> = QuadraticField(2)
            sage: K3.<sqrt3> = QuadraticField(3)
            sage: K5.<sqrt5> = QuadraticField(5)
            sage: for _ in range(100):
            ....:    a = QQ.random_element(1000,20)
            ....:    b = QQ.random_element(1000,20)
            ....:    assert ceil(a+b*sqrt(2.)) == ceil(a+b*sqrt2)
            ....:    assert ceil(a+b*sqrt(3.)) == ceil(a+b*sqrt3)
            ....:    assert ceil(a+b*sqrt(5.)) == ceil(a+b*sqrt5)

            sage: K = QuadraticField(-2)
            sage: l = [K(52), K(-3), K(43/12), K(-43/12)]
            sage: [x.ceil() for x in l]
            [52, -3, 4, -3]"""
    def charpoly(self, var=..., algorithm=...) -> Any:
        """NumberFieldElement_quadratic.charpoly(self, var='x', algorithm=None)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2203)

        The characteristic polynomial of this element over `\\QQ`.

        INPUT:

        - ``var`` -- the minimal polynomial is defined over a polynomial ring
          in a variable with this name; if not specified, this defaults to ``'x'``
        - ``algorithm`` -- for compatibility with general number field
          elements; ignored

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - x + 13)
            sage: a.charpoly()
            x^2 - x + 13
            sage: b = 3 - a/2
            sage: f = b.charpoly(); f
            x^2 - 11/2*x + 43/4
            sage: f(b)
            0"""
    @overload
    def continued_fraction(self) -> Any:
        """NumberFieldElement_quadratic.continued_fraction(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1289)

        Return the (finite or ultimately periodic) continued fraction of ``self``.

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2)
            sage: cf = sqrt2.continued_fraction(); cf
            [1; (2)*]
            sage: cf.n()
            1.41421356237310
            sage: sqrt2.n()
            1.41421356237309
            sage: cf.value()
            sqrt2

            sage: (sqrt2/3 + 1/4).continued_fraction()
            [0; 1, (2, 1, 1, 2, 3, 2, 1, 1, 2, 5, 1, 1, 14, 1, 1, 5)*]"""
    @overload
    def continued_fraction(self) -> Any:
        """NumberFieldElement_quadratic.continued_fraction(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1289)

        Return the (finite or ultimately periodic) continued fraction of ``self``.

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2)
            sage: cf = sqrt2.continued_fraction(); cf
            [1; (2)*]
            sage: cf.n()
            1.41421356237310
            sage: sqrt2.n()
            1.41421356237309
            sage: cf.value()
            sqrt2

            sage: (sqrt2/3 + 1/4).continued_fraction()
            [0; 1, (2, 1, 1, 2, 3, 2, 1, 1, 2, 5, 1, 1, 14, 1, 1, 5)*]"""
    @overload
    def continued_fraction(self) -> Any:
        """NumberFieldElement_quadratic.continued_fraction(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1289)

        Return the (finite or ultimately periodic) continued fraction of ``self``.

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2)
            sage: cf = sqrt2.continued_fraction(); cf
            [1; (2)*]
            sage: cf.n()
            1.41421356237310
            sage: sqrt2.n()
            1.41421356237309
            sage: cf.value()
            sqrt2

            sage: (sqrt2/3 + 1/4).continued_fraction()
            [0; 1, (2, 1, 1, 2, 3, 2, 1, 1, 2, 5, 1, 1, 14, 1, 1, 5)*]"""
    @overload
    def continued_fraction_list(self) -> Any:
        """NumberFieldElement_quadratic.continued_fraction_list(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1252)

        Return the preperiod and the period of the continued fraction expansion
        of ``self``.

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2)
            sage: sqrt2.continued_fraction_list()
            ((1,), (2,))
            sage: (1/2 + sqrt2/3).continued_fraction_list()
            ((0, 1, 33), (1, 32))

        For rational entries a pair of tuples is also returned but the second
        one is empty::

            sage: K(123/567).continued_fraction_list()
            ((0, 4, 1, 1, 1, 1, 3, 2), ())"""
    @overload
    def continued_fraction_list(self) -> Any:
        """NumberFieldElement_quadratic.continued_fraction_list(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1252)

        Return the preperiod and the period of the continued fraction expansion
        of ``self``.

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2)
            sage: sqrt2.continued_fraction_list()
            ((1,), (2,))
            sage: (1/2 + sqrt2/3).continued_fraction_list()
            ((0, 1, 33), (1, 32))

        For rational entries a pair of tuples is also returned but the second
        one is empty::

            sage: K(123/567).continued_fraction_list()
            ((0, 4, 1, 1, 1, 1, 3, 2), ())"""
    @overload
    def continued_fraction_list(self) -> Any:
        """NumberFieldElement_quadratic.continued_fraction_list(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1252)

        Return the preperiod and the period of the continued fraction expansion
        of ``self``.

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2)
            sage: sqrt2.continued_fraction_list()
            ((1,), (2,))
            sage: (1/2 + sqrt2/3).continued_fraction_list()
            ((0, 1, 33), (1, 32))

        For rational entries a pair of tuples is also returned but the second
        one is empty::

            sage: K(123/567).continued_fraction_list()
            ((0, 4, 1, 1, 1, 1, 3, 2), ())"""
    @overload
    def continued_fraction_list(self) -> Any:
        """NumberFieldElement_quadratic.continued_fraction_list(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1252)

        Return the preperiod and the period of the continued fraction expansion
        of ``self``.

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2)
            sage: sqrt2.continued_fraction_list()
            ((1,), (2,))
            sage: (1/2 + sqrt2/3).continued_fraction_list()
            ((0, 1, 33), (1, 32))

        For rational entries a pair of tuples is also returned but the second
        one is empty::

            sage: K(123/567).continued_fraction_list()
            ((0, 4, 1, 1, 1, 1, 3, 2), ())"""
    @overload
    def denominator(self) -> Any:
        """NumberFieldElement_quadratic.denominator(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1968)

        Return the denominator of ``self``.

        This is the LCM of the denominators of the coefficients of ``self``, and
        thus it may well be `> 1` even when the element is an algebraic integer.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - 5)
            sage: b = (a + 1)/2
            sage: b.denominator()
            2
            sage: b.is_integral()
            True

            sage: K.<c> = NumberField(x^2 - x + 7)
            sage: c.denominator()
            1"""
    @overload
    def denominator(self) -> Any:
        """NumberFieldElement_quadratic.denominator(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1968)

        Return the denominator of ``self``.

        This is the LCM of the denominators of the coefficients of ``self``, and
        thus it may well be `> 1` even when the element is an algebraic integer.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - 5)
            sage: b = (a + 1)/2
            sage: b.denominator()
            2
            sage: b.is_integral()
            True

            sage: K.<c> = NumberField(x^2 - x + 7)
            sage: c.denominator()
            1"""
    @overload
    def denominator(self) -> Any:
        """NumberFieldElement_quadratic.denominator(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1968)

        Return the denominator of ``self``.

        This is the LCM of the denominators of the coefficients of ``self``, and
        thus it may well be `> 1` even when the element is an algebraic integer.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - 5)
            sage: b = (a + 1)/2
            sage: b.denominator()
            2
            sage: b.is_integral()
            True

            sage: K.<c> = NumberField(x^2 - x + 7)
            sage: c.denominator()
            1"""
    @overload
    def floor(self) -> Any:
        """NumberFieldElement_quadratic.floor(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2284)

        Return the floor of ``self``.

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2, name='sqrt2')
            sage: sqrt2.floor()
            1
            sage: (-sqrt2).floor()
            -2
            sage: (13/197 + 3702/123*sqrt2).floor()
            42
            sage: (13/197 - 3702/123*sqrt2).floor()
            -43

        TESTS::

            sage: K2.<sqrt2> = QuadraticField(2)
            sage: K3.<sqrt3> = QuadraticField(3)
            sage: K5.<sqrt5> = QuadraticField(5)
            sage: for _ in range(100):
            ....:    a = QQ.random_element(1000,20)
            ....:    b = QQ.random_element(1000,20)
            ....:    assert floor(a+b*sqrt(2.)) == floor(a+b*sqrt2)
            ....:    assert floor(a+b*sqrt(3.)) == floor(a+b*sqrt3)
            ....:    assert floor(a+b*sqrt(5.)) == floor(a+b*sqrt5)

            sage: K = QuadraticField(-2)
            sage: l = [K(52), K(-3), K(43/12), K(-43/12)]
            sage: [x.floor() for x in l]
            [52, -3, 3, -4]"""
    @overload
    def floor(self) -> Any:
        """NumberFieldElement_quadratic.floor(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2284)

        Return the floor of ``self``.

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2, name='sqrt2')
            sage: sqrt2.floor()
            1
            sage: (-sqrt2).floor()
            -2
            sage: (13/197 + 3702/123*sqrt2).floor()
            42
            sage: (13/197 - 3702/123*sqrt2).floor()
            -43

        TESTS::

            sage: K2.<sqrt2> = QuadraticField(2)
            sage: K3.<sqrt3> = QuadraticField(3)
            sage: K5.<sqrt5> = QuadraticField(5)
            sage: for _ in range(100):
            ....:    a = QQ.random_element(1000,20)
            ....:    b = QQ.random_element(1000,20)
            ....:    assert floor(a+b*sqrt(2.)) == floor(a+b*sqrt2)
            ....:    assert floor(a+b*sqrt(3.)) == floor(a+b*sqrt3)
            ....:    assert floor(a+b*sqrt(5.)) == floor(a+b*sqrt5)

            sage: K = QuadraticField(-2)
            sage: l = [K(52), K(-3), K(43/12), K(-43/12)]
            sage: [x.floor() for x in l]
            [52, -3, 3, -4]"""
    @overload
    def floor(self) -> Any:
        """NumberFieldElement_quadratic.floor(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2284)

        Return the floor of ``self``.

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2, name='sqrt2')
            sage: sqrt2.floor()
            1
            sage: (-sqrt2).floor()
            -2
            sage: (13/197 + 3702/123*sqrt2).floor()
            42
            sage: (13/197 - 3702/123*sqrt2).floor()
            -43

        TESTS::

            sage: K2.<sqrt2> = QuadraticField(2)
            sage: K3.<sqrt3> = QuadraticField(3)
            sage: K5.<sqrt5> = QuadraticField(5)
            sage: for _ in range(100):
            ....:    a = QQ.random_element(1000,20)
            ....:    b = QQ.random_element(1000,20)
            ....:    assert floor(a+b*sqrt(2.)) == floor(a+b*sqrt2)
            ....:    assert floor(a+b*sqrt(3.)) == floor(a+b*sqrt3)
            ....:    assert floor(a+b*sqrt(5.)) == floor(a+b*sqrt5)

            sage: K = QuadraticField(-2)
            sage: l = [K(52), K(-3), K(43/12), K(-43/12)]
            sage: [x.floor() for x in l]
            [52, -3, 3, -4]"""
    @overload
    def floor(self) -> Any:
        """NumberFieldElement_quadratic.floor(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2284)

        Return the floor of ``self``.

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2, name='sqrt2')
            sage: sqrt2.floor()
            1
            sage: (-sqrt2).floor()
            -2
            sage: (13/197 + 3702/123*sqrt2).floor()
            42
            sage: (13/197 - 3702/123*sqrt2).floor()
            -43

        TESTS::

            sage: K2.<sqrt2> = QuadraticField(2)
            sage: K3.<sqrt3> = QuadraticField(3)
            sage: K5.<sqrt5> = QuadraticField(5)
            sage: for _ in range(100):
            ....:    a = QQ.random_element(1000,20)
            ....:    b = QQ.random_element(1000,20)
            ....:    assert floor(a+b*sqrt(2.)) == floor(a+b*sqrt2)
            ....:    assert floor(a+b*sqrt(3.)) == floor(a+b*sqrt3)
            ....:    assert floor(a+b*sqrt(5.)) == floor(a+b*sqrt5)

            sage: K = QuadraticField(-2)
            sage: l = [K(52), K(-3), K(43/12), K(-43/12)]
            sage: [x.floor() for x in l]
            [52, -3, 3, -4]"""
    @overload
    def floor(self) -> Any:
        """NumberFieldElement_quadratic.floor(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2284)

        Return the floor of ``self``.

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2, name='sqrt2')
            sage: sqrt2.floor()
            1
            sage: (-sqrt2).floor()
            -2
            sage: (13/197 + 3702/123*sqrt2).floor()
            42
            sage: (13/197 - 3702/123*sqrt2).floor()
            -43

        TESTS::

            sage: K2.<sqrt2> = QuadraticField(2)
            sage: K3.<sqrt3> = QuadraticField(3)
            sage: K5.<sqrt5> = QuadraticField(5)
            sage: for _ in range(100):
            ....:    a = QQ.random_element(1000,20)
            ....:    b = QQ.random_element(1000,20)
            ....:    assert floor(a+b*sqrt(2.)) == floor(a+b*sqrt2)
            ....:    assert floor(a+b*sqrt(3.)) == floor(a+b*sqrt3)
            ....:    assert floor(a+b*sqrt(5.)) == floor(a+b*sqrt5)

            sage: K = QuadraticField(-2)
            sage: l = [K(52), K(-3), K(43/12), K(-43/12)]
            sage: [x.floor() for x in l]
            [52, -3, 3, -4]"""
    @overload
    def floor(self) -> Any:
        """NumberFieldElement_quadratic.floor(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2284)

        Return the floor of ``self``.

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2, name='sqrt2')
            sage: sqrt2.floor()
            1
            sage: (-sqrt2).floor()
            -2
            sage: (13/197 + 3702/123*sqrt2).floor()
            42
            sage: (13/197 - 3702/123*sqrt2).floor()
            -43

        TESTS::

            sage: K2.<sqrt2> = QuadraticField(2)
            sage: K3.<sqrt3> = QuadraticField(3)
            sage: K5.<sqrt5> = QuadraticField(5)
            sage: for _ in range(100):
            ....:    a = QQ.random_element(1000,20)
            ....:    b = QQ.random_element(1000,20)
            ....:    assert floor(a+b*sqrt(2.)) == floor(a+b*sqrt2)
            ....:    assert floor(a+b*sqrt(3.)) == floor(a+b*sqrt3)
            ....:    assert floor(a+b*sqrt(5.)) == floor(a+b*sqrt5)

            sage: K = QuadraticField(-2)
            sage: l = [K(52), K(-3), K(43/12), K(-43/12)]
            sage: [x.floor() for x in l]
            [52, -3, 3, -4]"""
    @overload
    def galois_conjugate(self) -> NumberFieldElement:
        """NumberFieldElement_quadratic.galois_conjugate(self) -> NumberFieldElement

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1630)

        Return the image of this element under action of the nontrivial
        element of the Galois group of this field.

        EXAMPLES::

            sage: K.<a> = QuadraticField(23)
            sage: a.galois_conjugate()
            -a

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - 5*x + 1)
            sage: a.galois_conjugate()
            -a + 5
            sage: b = 5*a + 1/3
            sage: b.galois_conjugate()
            -5*a + 76/3
            sage: b.norm() ==  b * b.galois_conjugate()
            True
            sage: b.trace() ==  b + b.galois_conjugate()
            True"""
    @overload
    def galois_conjugate(self) -> Any:
        """NumberFieldElement_quadratic.galois_conjugate(self) -> NumberFieldElement

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1630)

        Return the image of this element under action of the nontrivial
        element of the Galois group of this field.

        EXAMPLES::

            sage: K.<a> = QuadraticField(23)
            sage: a.galois_conjugate()
            -a

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - 5*x + 1)
            sage: a.galois_conjugate()
            -a + 5
            sage: b = 5*a + 1/3
            sage: b.galois_conjugate()
            -5*a + 76/3
            sage: b.norm() ==  b * b.galois_conjugate()
            True
            sage: b.trace() ==  b + b.galois_conjugate()
            True"""
    @overload
    def galois_conjugate(self) -> Any:
        """NumberFieldElement_quadratic.galois_conjugate(self) -> NumberFieldElement

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1630)

        Return the image of this element under action of the nontrivial
        element of the Galois group of this field.

        EXAMPLES::

            sage: K.<a> = QuadraticField(23)
            sage: a.galois_conjugate()
            -a

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - 5*x + 1)
            sage: a.galois_conjugate()
            -a + 5
            sage: b = 5*a + 1/3
            sage: b.galois_conjugate()
            -5*a + 76/3
            sage: b.norm() ==  b * b.galois_conjugate()
            True
            sage: b.trace() ==  b + b.galois_conjugate()
            True"""
    @overload
    def galois_conjugate(self) -> Any:
        """NumberFieldElement_quadratic.galois_conjugate(self) -> NumberFieldElement

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1630)

        Return the image of this element under action of the nontrivial
        element of the Galois group of this field.

        EXAMPLES::

            sage: K.<a> = QuadraticField(23)
            sage: a.galois_conjugate()
            -a

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - 5*x + 1)
            sage: a.galois_conjugate()
            -a + 5
            sage: b = 5*a + 1/3
            sage: b.galois_conjugate()
            -5*a + 76/3
            sage: b.norm() ==  b * b.galois_conjugate()
            True
            sage: b.trace() ==  b + b.galois_conjugate()
            True"""
    @overload
    def galois_conjugate(self) -> Any:
        """NumberFieldElement_quadratic.galois_conjugate(self) -> NumberFieldElement

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1630)

        Return the image of this element under action of the nontrivial
        element of the Galois group of this field.

        EXAMPLES::

            sage: K.<a> = QuadraticField(23)
            sage: a.galois_conjugate()
            -a

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - 5*x + 1)
            sage: a.galois_conjugate()
            -a + 5
            sage: b = 5*a + 1/3
            sage: b.galois_conjugate()
            -5*a + 76/3
            sage: b.norm() ==  b * b.galois_conjugate()
            True
            sage: b.trace() ==  b + b.galois_conjugate()
            True"""
    @overload
    def galois_conjugate(self) -> Any:
        """NumberFieldElement_quadratic.galois_conjugate(self) -> NumberFieldElement

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1630)

        Return the image of this element under action of the nontrivial
        element of the Galois group of this field.

        EXAMPLES::

            sage: K.<a> = QuadraticField(23)
            sage: a.galois_conjugate()
            -a

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - 5*x + 1)
            sage: a.galois_conjugate()
            -a + 5
            sage: b = 5*a + 1/3
            sage: b.galois_conjugate()
            -5*a + 76/3
            sage: b.norm() ==  b * b.galois_conjugate()
            True
            sage: b.trace() ==  b + b.galois_conjugate()
            True"""
    @overload
    def imag(self) -> Any:
        """NumberFieldElement_quadratic.imag(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1860)

        Return the imaginary part of ``self``.

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2)
            sage: sqrt2.imag()
            0
            sage: parent(sqrt2.imag())
            Rational Field

            sage: K.<i> = QuadraticField(-1)
            sage: i.imag()
            1
            sage: parent(i.imag())
            Rational Field

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + x + 1, embedding=CDF.0)
            sage: a.imag()
            1/2*sqrt3
            sage: a.real()
            -1/2
            sage: SR(a)                                                                 # needs sage.symbolic
            1/2*I*sqrt(3) - 1/2
            sage: bool(QQbar(I)*QQbar(a.imag()) + QQbar(a.real()) == QQbar(a))
            True

        TESTS::

            sage: K.<a> = QuadraticField(-9, embedding=-CDF.0)
            sage: a.imag()
            -3
            sage: parent(a.imag())
            Rational Field

        Check that :issue:`22095` is fixed::

            sage: K.<a> = NumberField(x^2 + 2*x + 14, embedding=CC(-1,+3))
            sage: K13.<sqrt13> = QuadraticField(13)
            sage: K13.zero()
            0
            sage: a.imag()
            sqrt13
            sage: K13.zero()
            0"""
    @overload
    def imag(self) -> Any:
        """NumberFieldElement_quadratic.imag(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1860)

        Return the imaginary part of ``self``.

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2)
            sage: sqrt2.imag()
            0
            sage: parent(sqrt2.imag())
            Rational Field

            sage: K.<i> = QuadraticField(-1)
            sage: i.imag()
            1
            sage: parent(i.imag())
            Rational Field

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + x + 1, embedding=CDF.0)
            sage: a.imag()
            1/2*sqrt3
            sage: a.real()
            -1/2
            sage: SR(a)                                                                 # needs sage.symbolic
            1/2*I*sqrt(3) - 1/2
            sage: bool(QQbar(I)*QQbar(a.imag()) + QQbar(a.real()) == QQbar(a))
            True

        TESTS::

            sage: K.<a> = QuadraticField(-9, embedding=-CDF.0)
            sage: a.imag()
            -3
            sage: parent(a.imag())
            Rational Field

        Check that :issue:`22095` is fixed::

            sage: K.<a> = NumberField(x^2 + 2*x + 14, embedding=CC(-1,+3))
            sage: K13.<sqrt13> = QuadraticField(13)
            sage: K13.zero()
            0
            sage: a.imag()
            sqrt13
            sage: K13.zero()
            0"""
    @overload
    def imag(self) -> Any:
        """NumberFieldElement_quadratic.imag(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1860)

        Return the imaginary part of ``self``.

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2)
            sage: sqrt2.imag()
            0
            sage: parent(sqrt2.imag())
            Rational Field

            sage: K.<i> = QuadraticField(-1)
            sage: i.imag()
            1
            sage: parent(i.imag())
            Rational Field

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + x + 1, embedding=CDF.0)
            sage: a.imag()
            1/2*sqrt3
            sage: a.real()
            -1/2
            sage: SR(a)                                                                 # needs sage.symbolic
            1/2*I*sqrt(3) - 1/2
            sage: bool(QQbar(I)*QQbar(a.imag()) + QQbar(a.real()) == QQbar(a))
            True

        TESTS::

            sage: K.<a> = QuadraticField(-9, embedding=-CDF.0)
            sage: a.imag()
            -3
            sage: parent(a.imag())
            Rational Field

        Check that :issue:`22095` is fixed::

            sage: K.<a> = NumberField(x^2 + 2*x + 14, embedding=CC(-1,+3))
            sage: K13.<sqrt13> = QuadraticField(13)
            sage: K13.zero()
            0
            sage: a.imag()
            sqrt13
            sage: K13.zero()
            0"""
    @overload
    def imag(self) -> Any:
        """NumberFieldElement_quadratic.imag(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1860)

        Return the imaginary part of ``self``.

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2)
            sage: sqrt2.imag()
            0
            sage: parent(sqrt2.imag())
            Rational Field

            sage: K.<i> = QuadraticField(-1)
            sage: i.imag()
            1
            sage: parent(i.imag())
            Rational Field

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + x + 1, embedding=CDF.0)
            sage: a.imag()
            1/2*sqrt3
            sage: a.real()
            -1/2
            sage: SR(a)                                                                 # needs sage.symbolic
            1/2*I*sqrt(3) - 1/2
            sage: bool(QQbar(I)*QQbar(a.imag()) + QQbar(a.real()) == QQbar(a))
            True

        TESTS::

            sage: K.<a> = QuadraticField(-9, embedding=-CDF.0)
            sage: a.imag()
            -3
            sage: parent(a.imag())
            Rational Field

        Check that :issue:`22095` is fixed::

            sage: K.<a> = NumberField(x^2 + 2*x + 14, embedding=CC(-1,+3))
            sage: K13.<sqrt13> = QuadraticField(13)
            sage: K13.zero()
            0
            sage: a.imag()
            sqrt13
            sage: K13.zero()
            0"""
    @overload
    def imag(self) -> Any:
        """NumberFieldElement_quadratic.imag(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1860)

        Return the imaginary part of ``self``.

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2)
            sage: sqrt2.imag()
            0
            sage: parent(sqrt2.imag())
            Rational Field

            sage: K.<i> = QuadraticField(-1)
            sage: i.imag()
            1
            sage: parent(i.imag())
            Rational Field

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + x + 1, embedding=CDF.0)
            sage: a.imag()
            1/2*sqrt3
            sage: a.real()
            -1/2
            sage: SR(a)                                                                 # needs sage.symbolic
            1/2*I*sqrt(3) - 1/2
            sage: bool(QQbar(I)*QQbar(a.imag()) + QQbar(a.real()) == QQbar(a))
            True

        TESTS::

            sage: K.<a> = QuadraticField(-9, embedding=-CDF.0)
            sage: a.imag()
            -3
            sage: parent(a.imag())
            Rational Field

        Check that :issue:`22095` is fixed::

            sage: K.<a> = NumberField(x^2 + 2*x + 14, embedding=CC(-1,+3))
            sage: K13.<sqrt13> = QuadraticField(13)
            sage: K13.zero()
            0
            sage: a.imag()
            sqrt13
            sage: K13.zero()
            0"""
    @overload
    def imag(self) -> Any:
        """NumberFieldElement_quadratic.imag(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1860)

        Return the imaginary part of ``self``.

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2)
            sage: sqrt2.imag()
            0
            sage: parent(sqrt2.imag())
            Rational Field

            sage: K.<i> = QuadraticField(-1)
            sage: i.imag()
            1
            sage: parent(i.imag())
            Rational Field

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + x + 1, embedding=CDF.0)
            sage: a.imag()
            1/2*sqrt3
            sage: a.real()
            -1/2
            sage: SR(a)                                                                 # needs sage.symbolic
            1/2*I*sqrt(3) - 1/2
            sage: bool(QQbar(I)*QQbar(a.imag()) + QQbar(a.real()) == QQbar(a))
            True

        TESTS::

            sage: K.<a> = QuadraticField(-9, embedding=-CDF.0)
            sage: a.imag()
            -3
            sage: parent(a.imag())
            Rational Field

        Check that :issue:`22095` is fixed::

            sage: K.<a> = NumberField(x^2 + 2*x + 14, embedding=CC(-1,+3))
            sage: K13.<sqrt13> = QuadraticField(13)
            sage: K13.zero()
            0
            sage: a.imag()
            sqrt13
            sage: K13.zero()
            0"""
    @overload
    def imag(self) -> Any:
        """NumberFieldElement_quadratic.imag(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1860)

        Return the imaginary part of ``self``.

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2)
            sage: sqrt2.imag()
            0
            sage: parent(sqrt2.imag())
            Rational Field

            sage: K.<i> = QuadraticField(-1)
            sage: i.imag()
            1
            sage: parent(i.imag())
            Rational Field

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + x + 1, embedding=CDF.0)
            sage: a.imag()
            1/2*sqrt3
            sage: a.real()
            -1/2
            sage: SR(a)                                                                 # needs sage.symbolic
            1/2*I*sqrt(3) - 1/2
            sage: bool(QQbar(I)*QQbar(a.imag()) + QQbar(a.real()) == QQbar(a))
            True

        TESTS::

            sage: K.<a> = QuadraticField(-9, embedding=-CDF.0)
            sage: a.imag()
            -3
            sage: parent(a.imag())
            Rational Field

        Check that :issue:`22095` is fixed::

            sage: K.<a> = NumberField(x^2 + 2*x + 14, embedding=CC(-1,+3))
            sage: K13.<sqrt13> = QuadraticField(13)
            sage: K13.zero()
            0
            sage: a.imag()
            sqrt13
            sage: K13.zero()
            0"""
    @overload
    def imag(self) -> Any:
        """NumberFieldElement_quadratic.imag(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1860)

        Return the imaginary part of ``self``.

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2)
            sage: sqrt2.imag()
            0
            sage: parent(sqrt2.imag())
            Rational Field

            sage: K.<i> = QuadraticField(-1)
            sage: i.imag()
            1
            sage: parent(i.imag())
            Rational Field

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + x + 1, embedding=CDF.0)
            sage: a.imag()
            1/2*sqrt3
            sage: a.real()
            -1/2
            sage: SR(a)                                                                 # needs sage.symbolic
            1/2*I*sqrt(3) - 1/2
            sage: bool(QQbar(I)*QQbar(a.imag()) + QQbar(a.real()) == QQbar(a))
            True

        TESTS::

            sage: K.<a> = QuadraticField(-9, embedding=-CDF.0)
            sage: a.imag()
            -3
            sage: parent(a.imag())
            Rational Field

        Check that :issue:`22095` is fixed::

            sage: K.<a> = NumberField(x^2 + 2*x + 14, embedding=CC(-1,+3))
            sage: K13.<sqrt13> = QuadraticField(13)
            sage: K13.zero()
            0
            sage: a.imag()
            sqrt13
            sage: K13.zero()
            0"""
    @overload
    def imag(self) -> Any:
        """NumberFieldElement_quadratic.imag(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1860)

        Return the imaginary part of ``self``.

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2)
            sage: sqrt2.imag()
            0
            sage: parent(sqrt2.imag())
            Rational Field

            sage: K.<i> = QuadraticField(-1)
            sage: i.imag()
            1
            sage: parent(i.imag())
            Rational Field

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + x + 1, embedding=CDF.0)
            sage: a.imag()
            1/2*sqrt3
            sage: a.real()
            -1/2
            sage: SR(a)                                                                 # needs sage.symbolic
            1/2*I*sqrt(3) - 1/2
            sage: bool(QQbar(I)*QQbar(a.imag()) + QQbar(a.real()) == QQbar(a))
            True

        TESTS::

            sage: K.<a> = QuadraticField(-9, embedding=-CDF.0)
            sage: a.imag()
            -3
            sage: parent(a.imag())
            Rational Field

        Check that :issue:`22095` is fixed::

            sage: K.<a> = NumberField(x^2 + 2*x + 14, embedding=CC(-1,+3))
            sage: K13.<sqrt13> = QuadraticField(13)
            sage: K13.zero()
            0
            sage: a.imag()
            sqrt13
            sage: K13.zero()
            0"""
    @overload
    def imag(self) -> Any:
        """NumberFieldElement_quadratic.imag(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1860)

        Return the imaginary part of ``self``.

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2)
            sage: sqrt2.imag()
            0
            sage: parent(sqrt2.imag())
            Rational Field

            sage: K.<i> = QuadraticField(-1)
            sage: i.imag()
            1
            sage: parent(i.imag())
            Rational Field

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + x + 1, embedding=CDF.0)
            sage: a.imag()
            1/2*sqrt3
            sage: a.real()
            -1/2
            sage: SR(a)                                                                 # needs sage.symbolic
            1/2*I*sqrt(3) - 1/2
            sage: bool(QQbar(I)*QQbar(a.imag()) + QQbar(a.real()) == QQbar(a))
            True

        TESTS::

            sage: K.<a> = QuadraticField(-9, embedding=-CDF.0)
            sage: a.imag()
            -3
            sage: parent(a.imag())
            Rational Field

        Check that :issue:`22095` is fixed::

            sage: K.<a> = NumberField(x^2 + 2*x + 14, embedding=CC(-1,+3))
            sage: K13.<sqrt13> = QuadraticField(13)
            sage: K13.zero()
            0
            sage: a.imag()
            sqrt13
            sage: K13.zero()
            0"""
    @overload
    def is_integer(self) -> Any:
        """NumberFieldElement_quadratic.is_integer(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1800)

        Check whether this number field element is an integer.

        .. SEEALSO::

            - :meth:`is_rational` to test if this element is a rational number
            - :meth:`is_integral` to test if this element is an algebraic integer

        EXAMPLES::

            sage: K.<sqrt3> = QuadraticField(3)
            sage: sqrt3.is_integer()
            False
            sage: (sqrt3 - 1/2).is_integer()
            False
            sage: K(0).is_integer()
            True
            sage: K(-12).is_integer()
            True
            sage: K(1/3).is_integer()
            False"""
    @overload
    def is_integer(self) -> Any:
        """NumberFieldElement_quadratic.is_integer(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1800)

        Check whether this number field element is an integer.

        .. SEEALSO::

            - :meth:`is_rational` to test if this element is a rational number
            - :meth:`is_integral` to test if this element is an algebraic integer

        EXAMPLES::

            sage: K.<sqrt3> = QuadraticField(3)
            sage: sqrt3.is_integer()
            False
            sage: (sqrt3 - 1/2).is_integer()
            False
            sage: K(0).is_integer()
            True
            sage: K(-12).is_integer()
            True
            sage: K(1/3).is_integer()
            False"""
    @overload
    def is_integer(self) -> Any:
        """NumberFieldElement_quadratic.is_integer(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1800)

        Check whether this number field element is an integer.

        .. SEEALSO::

            - :meth:`is_rational` to test if this element is a rational number
            - :meth:`is_integral` to test if this element is an algebraic integer

        EXAMPLES::

            sage: K.<sqrt3> = QuadraticField(3)
            sage: sqrt3.is_integer()
            False
            sage: (sqrt3 - 1/2).is_integer()
            False
            sage: K(0).is_integer()
            True
            sage: K(-12).is_integer()
            True
            sage: K(1/3).is_integer()
            False"""
    @overload
    def is_integer(self) -> Any:
        """NumberFieldElement_quadratic.is_integer(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1800)

        Check whether this number field element is an integer.

        .. SEEALSO::

            - :meth:`is_rational` to test if this element is a rational number
            - :meth:`is_integral` to test if this element is an algebraic integer

        EXAMPLES::

            sage: K.<sqrt3> = QuadraticField(3)
            sage: sqrt3.is_integer()
            False
            sage: (sqrt3 - 1/2).is_integer()
            False
            sage: K(0).is_integer()
            True
            sage: K(-12).is_integer()
            True
            sage: K(1/3).is_integer()
            False"""
    @overload
    def is_integer(self) -> Any:
        """NumberFieldElement_quadratic.is_integer(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1800)

        Check whether this number field element is an integer.

        .. SEEALSO::

            - :meth:`is_rational` to test if this element is a rational number
            - :meth:`is_integral` to test if this element is an algebraic integer

        EXAMPLES::

            sage: K.<sqrt3> = QuadraticField(3)
            sage: sqrt3.is_integer()
            False
            sage: (sqrt3 - 1/2).is_integer()
            False
            sage: K(0).is_integer()
            True
            sage: K(-12).is_integer()
            True
            sage: K(1/3).is_integer()
            False"""
    @overload
    def is_integer(self) -> Any:
        """NumberFieldElement_quadratic.is_integer(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1800)

        Check whether this number field element is an integer.

        .. SEEALSO::

            - :meth:`is_rational` to test if this element is a rational number
            - :meth:`is_integral` to test if this element is an algebraic integer

        EXAMPLES::

            sage: K.<sqrt3> = QuadraticField(3)
            sage: sqrt3.is_integer()
            False
            sage: (sqrt3 - 1/2).is_integer()
            False
            sage: K(0).is_integer()
            True
            sage: K(-12).is_integer()
            True
            sage: K(1/3).is_integer()
            False"""
    @overload
    def is_integral(self) -> Any:
        """NumberFieldElement_quadratic.is_integral(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2110)

        Return whether this element is an algebraic integer.

        TESTS::

            sage: K.<a> = QuadraticField(-1)
            sage: a.is_integral()
            True
            sage: K(1).is_integral()
            True
            sage: K(1/2).is_integral()
            False
            sage: (a/2).is_integral()
            False
            sage: ((a+1)/2).is_integral()
            False
            sage: ((a+1)/3).is_integral()
            False

            sage: K.<a> = QuadraticField(-3)
            sage: a.is_integral()
            True
            sage: K(1).is_integral()
            True
            sage: K(1/2).is_integral()
            False
            sage: (a/2).is_integral()
            False
            sage: ((a+1)/2).is_integral()
            True
            sage: ((a+1)/3).is_integral()
            False

        This works for order elements too, see :issue:`24077`::

            sage: O.<w> = EisensteinIntegers()
            sage: w.is_integral()
            True
            sage: for _ in range(20):
            ....:     assert O.random_element().is_integral()

        Check that :issue:`34800` is fixed::

            sage: K.<t> = QuadraticField(-10007^2)
            sage: (t/10007).is_integral()
            True"""
    @overload
    def is_integral(self) -> Any:
        """NumberFieldElement_quadratic.is_integral(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2110)

        Return whether this element is an algebraic integer.

        TESTS::

            sage: K.<a> = QuadraticField(-1)
            sage: a.is_integral()
            True
            sage: K(1).is_integral()
            True
            sage: K(1/2).is_integral()
            False
            sage: (a/2).is_integral()
            False
            sage: ((a+1)/2).is_integral()
            False
            sage: ((a+1)/3).is_integral()
            False

            sage: K.<a> = QuadraticField(-3)
            sage: a.is_integral()
            True
            sage: K(1).is_integral()
            True
            sage: K(1/2).is_integral()
            False
            sage: (a/2).is_integral()
            False
            sage: ((a+1)/2).is_integral()
            True
            sage: ((a+1)/3).is_integral()
            False

        This works for order elements too, see :issue:`24077`::

            sage: O.<w> = EisensteinIntegers()
            sage: w.is_integral()
            True
            sage: for _ in range(20):
            ....:     assert O.random_element().is_integral()

        Check that :issue:`34800` is fixed::

            sage: K.<t> = QuadraticField(-10007^2)
            sage: (t/10007).is_integral()
            True"""
    @overload
    def is_integral(self) -> Any:
        """NumberFieldElement_quadratic.is_integral(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2110)

        Return whether this element is an algebraic integer.

        TESTS::

            sage: K.<a> = QuadraticField(-1)
            sage: a.is_integral()
            True
            sage: K(1).is_integral()
            True
            sage: K(1/2).is_integral()
            False
            sage: (a/2).is_integral()
            False
            sage: ((a+1)/2).is_integral()
            False
            sage: ((a+1)/3).is_integral()
            False

            sage: K.<a> = QuadraticField(-3)
            sage: a.is_integral()
            True
            sage: K(1).is_integral()
            True
            sage: K(1/2).is_integral()
            False
            sage: (a/2).is_integral()
            False
            sage: ((a+1)/2).is_integral()
            True
            sage: ((a+1)/3).is_integral()
            False

        This works for order elements too, see :issue:`24077`::

            sage: O.<w> = EisensteinIntegers()
            sage: w.is_integral()
            True
            sage: for _ in range(20):
            ....:     assert O.random_element().is_integral()

        Check that :issue:`34800` is fixed::

            sage: K.<t> = QuadraticField(-10007^2)
            sage: (t/10007).is_integral()
            True"""
    @overload
    def is_integral(self) -> Any:
        """NumberFieldElement_quadratic.is_integral(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2110)

        Return whether this element is an algebraic integer.

        TESTS::

            sage: K.<a> = QuadraticField(-1)
            sage: a.is_integral()
            True
            sage: K(1).is_integral()
            True
            sage: K(1/2).is_integral()
            False
            sage: (a/2).is_integral()
            False
            sage: ((a+1)/2).is_integral()
            False
            sage: ((a+1)/3).is_integral()
            False

            sage: K.<a> = QuadraticField(-3)
            sage: a.is_integral()
            True
            sage: K(1).is_integral()
            True
            sage: K(1/2).is_integral()
            False
            sage: (a/2).is_integral()
            False
            sage: ((a+1)/2).is_integral()
            True
            sage: ((a+1)/3).is_integral()
            False

        This works for order elements too, see :issue:`24077`::

            sage: O.<w> = EisensteinIntegers()
            sage: w.is_integral()
            True
            sage: for _ in range(20):
            ....:     assert O.random_element().is_integral()

        Check that :issue:`34800` is fixed::

            sage: K.<t> = QuadraticField(-10007^2)
            sage: (t/10007).is_integral()
            True"""
    @overload
    def is_integral(self) -> Any:
        """NumberFieldElement_quadratic.is_integral(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2110)

        Return whether this element is an algebraic integer.

        TESTS::

            sage: K.<a> = QuadraticField(-1)
            sage: a.is_integral()
            True
            sage: K(1).is_integral()
            True
            sage: K(1/2).is_integral()
            False
            sage: (a/2).is_integral()
            False
            sage: ((a+1)/2).is_integral()
            False
            sage: ((a+1)/3).is_integral()
            False

            sage: K.<a> = QuadraticField(-3)
            sage: a.is_integral()
            True
            sage: K(1).is_integral()
            True
            sage: K(1/2).is_integral()
            False
            sage: (a/2).is_integral()
            False
            sage: ((a+1)/2).is_integral()
            True
            sage: ((a+1)/3).is_integral()
            False

        This works for order elements too, see :issue:`24077`::

            sage: O.<w> = EisensteinIntegers()
            sage: w.is_integral()
            True
            sage: for _ in range(20):
            ....:     assert O.random_element().is_integral()

        Check that :issue:`34800` is fixed::

            sage: K.<t> = QuadraticField(-10007^2)
            sage: (t/10007).is_integral()
            True"""
    @overload
    def is_integral(self) -> Any:
        """NumberFieldElement_quadratic.is_integral(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2110)

        Return whether this element is an algebraic integer.

        TESTS::

            sage: K.<a> = QuadraticField(-1)
            sage: a.is_integral()
            True
            sage: K(1).is_integral()
            True
            sage: K(1/2).is_integral()
            False
            sage: (a/2).is_integral()
            False
            sage: ((a+1)/2).is_integral()
            False
            sage: ((a+1)/3).is_integral()
            False

            sage: K.<a> = QuadraticField(-3)
            sage: a.is_integral()
            True
            sage: K(1).is_integral()
            True
            sage: K(1/2).is_integral()
            False
            sage: (a/2).is_integral()
            False
            sage: ((a+1)/2).is_integral()
            True
            sage: ((a+1)/3).is_integral()
            False

        This works for order elements too, see :issue:`24077`::

            sage: O.<w> = EisensteinIntegers()
            sage: w.is_integral()
            True
            sage: for _ in range(20):
            ....:     assert O.random_element().is_integral()

        Check that :issue:`34800` is fixed::

            sage: K.<t> = QuadraticField(-10007^2)
            sage: (t/10007).is_integral()
            True"""
    @overload
    def is_integral(self) -> Any:
        """NumberFieldElement_quadratic.is_integral(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2110)

        Return whether this element is an algebraic integer.

        TESTS::

            sage: K.<a> = QuadraticField(-1)
            sage: a.is_integral()
            True
            sage: K(1).is_integral()
            True
            sage: K(1/2).is_integral()
            False
            sage: (a/2).is_integral()
            False
            sage: ((a+1)/2).is_integral()
            False
            sage: ((a+1)/3).is_integral()
            False

            sage: K.<a> = QuadraticField(-3)
            sage: a.is_integral()
            True
            sage: K(1).is_integral()
            True
            sage: K(1/2).is_integral()
            False
            sage: (a/2).is_integral()
            False
            sage: ((a+1)/2).is_integral()
            True
            sage: ((a+1)/3).is_integral()
            False

        This works for order elements too, see :issue:`24077`::

            sage: O.<w> = EisensteinIntegers()
            sage: w.is_integral()
            True
            sage: for _ in range(20):
            ....:     assert O.random_element().is_integral()

        Check that :issue:`34800` is fixed::

            sage: K.<t> = QuadraticField(-10007^2)
            sage: (t/10007).is_integral()
            True"""
    @overload
    def is_integral(self) -> Any:
        """NumberFieldElement_quadratic.is_integral(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2110)

        Return whether this element is an algebraic integer.

        TESTS::

            sage: K.<a> = QuadraticField(-1)
            sage: a.is_integral()
            True
            sage: K(1).is_integral()
            True
            sage: K(1/2).is_integral()
            False
            sage: (a/2).is_integral()
            False
            sage: ((a+1)/2).is_integral()
            False
            sage: ((a+1)/3).is_integral()
            False

            sage: K.<a> = QuadraticField(-3)
            sage: a.is_integral()
            True
            sage: K(1).is_integral()
            True
            sage: K(1/2).is_integral()
            False
            sage: (a/2).is_integral()
            False
            sage: ((a+1)/2).is_integral()
            True
            sage: ((a+1)/3).is_integral()
            False

        This works for order elements too, see :issue:`24077`::

            sage: O.<w> = EisensteinIntegers()
            sage: w.is_integral()
            True
            sage: for _ in range(20):
            ....:     assert O.random_element().is_integral()

        Check that :issue:`34800` is fixed::

            sage: K.<t> = QuadraticField(-10007^2)
            sage: (t/10007).is_integral()
            True"""
    @overload
    def is_integral(self) -> Any:
        """NumberFieldElement_quadratic.is_integral(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2110)

        Return whether this element is an algebraic integer.

        TESTS::

            sage: K.<a> = QuadraticField(-1)
            sage: a.is_integral()
            True
            sage: K(1).is_integral()
            True
            sage: K(1/2).is_integral()
            False
            sage: (a/2).is_integral()
            False
            sage: ((a+1)/2).is_integral()
            False
            sage: ((a+1)/3).is_integral()
            False

            sage: K.<a> = QuadraticField(-3)
            sage: a.is_integral()
            True
            sage: K(1).is_integral()
            True
            sage: K(1/2).is_integral()
            False
            sage: (a/2).is_integral()
            False
            sage: ((a+1)/2).is_integral()
            True
            sage: ((a+1)/3).is_integral()
            False

        This works for order elements too, see :issue:`24077`::

            sage: O.<w> = EisensteinIntegers()
            sage: w.is_integral()
            True
            sage: for _ in range(20):
            ....:     assert O.random_element().is_integral()

        Check that :issue:`34800` is fixed::

            sage: K.<t> = QuadraticField(-10007^2)
            sage: (t/10007).is_integral()
            True"""
    @overload
    def is_integral(self) -> Any:
        """NumberFieldElement_quadratic.is_integral(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2110)

        Return whether this element is an algebraic integer.

        TESTS::

            sage: K.<a> = QuadraticField(-1)
            sage: a.is_integral()
            True
            sage: K(1).is_integral()
            True
            sage: K(1/2).is_integral()
            False
            sage: (a/2).is_integral()
            False
            sage: ((a+1)/2).is_integral()
            False
            sage: ((a+1)/3).is_integral()
            False

            sage: K.<a> = QuadraticField(-3)
            sage: a.is_integral()
            True
            sage: K(1).is_integral()
            True
            sage: K(1/2).is_integral()
            False
            sage: (a/2).is_integral()
            False
            sage: ((a+1)/2).is_integral()
            True
            sage: ((a+1)/3).is_integral()
            False

        This works for order elements too, see :issue:`24077`::

            sage: O.<w> = EisensteinIntegers()
            sage: w.is_integral()
            True
            sage: for _ in range(20):
            ....:     assert O.random_element().is_integral()

        Check that :issue:`34800` is fixed::

            sage: K.<t> = QuadraticField(-10007^2)
            sage: (t/10007).is_integral()
            True"""
    @overload
    def is_integral(self) -> Any:
        """NumberFieldElement_quadratic.is_integral(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2110)

        Return whether this element is an algebraic integer.

        TESTS::

            sage: K.<a> = QuadraticField(-1)
            sage: a.is_integral()
            True
            sage: K(1).is_integral()
            True
            sage: K(1/2).is_integral()
            False
            sage: (a/2).is_integral()
            False
            sage: ((a+1)/2).is_integral()
            False
            sage: ((a+1)/3).is_integral()
            False

            sage: K.<a> = QuadraticField(-3)
            sage: a.is_integral()
            True
            sage: K(1).is_integral()
            True
            sage: K(1/2).is_integral()
            False
            sage: (a/2).is_integral()
            False
            sage: ((a+1)/2).is_integral()
            True
            sage: ((a+1)/3).is_integral()
            False

        This works for order elements too, see :issue:`24077`::

            sage: O.<w> = EisensteinIntegers()
            sage: w.is_integral()
            True
            sage: for _ in range(20):
            ....:     assert O.random_element().is_integral()

        Check that :issue:`34800` is fixed::

            sage: K.<t> = QuadraticField(-10007^2)
            sage: (t/10007).is_integral()
            True"""
    @overload
    def is_integral(self) -> Any:
        """NumberFieldElement_quadratic.is_integral(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2110)

        Return whether this element is an algebraic integer.

        TESTS::

            sage: K.<a> = QuadraticField(-1)
            sage: a.is_integral()
            True
            sage: K(1).is_integral()
            True
            sage: K(1/2).is_integral()
            False
            sage: (a/2).is_integral()
            False
            sage: ((a+1)/2).is_integral()
            False
            sage: ((a+1)/3).is_integral()
            False

            sage: K.<a> = QuadraticField(-3)
            sage: a.is_integral()
            True
            sage: K(1).is_integral()
            True
            sage: K(1/2).is_integral()
            False
            sage: (a/2).is_integral()
            False
            sage: ((a+1)/2).is_integral()
            True
            sage: ((a+1)/3).is_integral()
            False

        This works for order elements too, see :issue:`24077`::

            sage: O.<w> = EisensteinIntegers()
            sage: w.is_integral()
            True
            sage: for _ in range(20):
            ....:     assert O.random_element().is_integral()

        Check that :issue:`34800` is fixed::

            sage: K.<t> = QuadraticField(-10007^2)
            sage: (t/10007).is_integral()
            True"""
    @overload
    def is_integral(self) -> Any:
        """NumberFieldElement_quadratic.is_integral(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2110)

        Return whether this element is an algebraic integer.

        TESTS::

            sage: K.<a> = QuadraticField(-1)
            sage: a.is_integral()
            True
            sage: K(1).is_integral()
            True
            sage: K(1/2).is_integral()
            False
            sage: (a/2).is_integral()
            False
            sage: ((a+1)/2).is_integral()
            False
            sage: ((a+1)/3).is_integral()
            False

            sage: K.<a> = QuadraticField(-3)
            sage: a.is_integral()
            True
            sage: K(1).is_integral()
            True
            sage: K(1/2).is_integral()
            False
            sage: (a/2).is_integral()
            False
            sage: ((a+1)/2).is_integral()
            True
            sage: ((a+1)/3).is_integral()
            False

        This works for order elements too, see :issue:`24077`::

            sage: O.<w> = EisensteinIntegers()
            sage: w.is_integral()
            True
            sage: for _ in range(20):
            ....:     assert O.random_element().is_integral()

        Check that :issue:`34800` is fixed::

            sage: K.<t> = QuadraticField(-10007^2)
            sage: (t/10007).is_integral()
            True"""
    @overload
    def is_integral(self) -> Any:
        """NumberFieldElement_quadratic.is_integral(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2110)

        Return whether this element is an algebraic integer.

        TESTS::

            sage: K.<a> = QuadraticField(-1)
            sage: a.is_integral()
            True
            sage: K(1).is_integral()
            True
            sage: K(1/2).is_integral()
            False
            sage: (a/2).is_integral()
            False
            sage: ((a+1)/2).is_integral()
            False
            sage: ((a+1)/3).is_integral()
            False

            sage: K.<a> = QuadraticField(-3)
            sage: a.is_integral()
            True
            sage: K(1).is_integral()
            True
            sage: K(1/2).is_integral()
            False
            sage: (a/2).is_integral()
            False
            sage: ((a+1)/2).is_integral()
            True
            sage: ((a+1)/3).is_integral()
            False

        This works for order elements too, see :issue:`24077`::

            sage: O.<w> = EisensteinIntegers()
            sage: w.is_integral()
            True
            sage: for _ in range(20):
            ....:     assert O.random_element().is_integral()

        Check that :issue:`34800` is fixed::

            sage: K.<t> = QuadraticField(-10007^2)
            sage: (t/10007).is_integral()
            True"""
    @overload
    def is_integral(self) -> Any:
        """NumberFieldElement_quadratic.is_integral(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2110)

        Return whether this element is an algebraic integer.

        TESTS::

            sage: K.<a> = QuadraticField(-1)
            sage: a.is_integral()
            True
            sage: K(1).is_integral()
            True
            sage: K(1/2).is_integral()
            False
            sage: (a/2).is_integral()
            False
            sage: ((a+1)/2).is_integral()
            False
            sage: ((a+1)/3).is_integral()
            False

            sage: K.<a> = QuadraticField(-3)
            sage: a.is_integral()
            True
            sage: K(1).is_integral()
            True
            sage: K(1/2).is_integral()
            False
            sage: (a/2).is_integral()
            False
            sage: ((a+1)/2).is_integral()
            True
            sage: ((a+1)/3).is_integral()
            False

        This works for order elements too, see :issue:`24077`::

            sage: O.<w> = EisensteinIntegers()
            sage: w.is_integral()
            True
            sage: for _ in range(20):
            ....:     assert O.random_element().is_integral()

        Check that :issue:`34800` is fixed::

            sage: K.<t> = QuadraticField(-10007^2)
            sage: (t/10007).is_integral()
            True"""
    @overload
    def is_integral(self) -> Any:
        """NumberFieldElement_quadratic.is_integral(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2110)

        Return whether this element is an algebraic integer.

        TESTS::

            sage: K.<a> = QuadraticField(-1)
            sage: a.is_integral()
            True
            sage: K(1).is_integral()
            True
            sage: K(1/2).is_integral()
            False
            sage: (a/2).is_integral()
            False
            sage: ((a+1)/2).is_integral()
            False
            sage: ((a+1)/3).is_integral()
            False

            sage: K.<a> = QuadraticField(-3)
            sage: a.is_integral()
            True
            sage: K(1).is_integral()
            True
            sage: K(1/2).is_integral()
            False
            sage: (a/2).is_integral()
            False
            sage: ((a+1)/2).is_integral()
            True
            sage: ((a+1)/3).is_integral()
            False

        This works for order elements too, see :issue:`24077`::

            sage: O.<w> = EisensteinIntegers()
            sage: w.is_integral()
            True
            sage: for _ in range(20):
            ....:     assert O.random_element().is_integral()

        Check that :issue:`34800` is fixed::

            sage: K.<t> = QuadraticField(-10007^2)
            sage: (t/10007).is_integral()
            True"""
    @overload
    def is_one(self) -> bool:
        """NumberFieldElement_quadratic.is_one(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1751)

        Check whether this number field element is `1`.

        EXAMPLES::

            sage: K = QuadraticField(-2)
            sage: K(1).is_one()
            True
            sage: K(-1).is_one()
            False
            sage: K(2).is_one()
            False
            sage: K(0).is_one()
            False
            sage: K(1/2).is_one()
            False
            sage: K.gen().is_one()
            False"""
    @overload
    def is_one(self) -> Any:
        """NumberFieldElement_quadratic.is_one(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1751)

        Check whether this number field element is `1`.

        EXAMPLES::

            sage: K = QuadraticField(-2)
            sage: K(1).is_one()
            True
            sage: K(-1).is_one()
            False
            sage: K(2).is_one()
            False
            sage: K(0).is_one()
            False
            sage: K(1/2).is_one()
            False
            sage: K.gen().is_one()
            False"""
    @overload
    def is_one(self) -> Any:
        """NumberFieldElement_quadratic.is_one(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1751)

        Check whether this number field element is `1`.

        EXAMPLES::

            sage: K = QuadraticField(-2)
            sage: K(1).is_one()
            True
            sage: K(-1).is_one()
            False
            sage: K(2).is_one()
            False
            sage: K(0).is_one()
            False
            sage: K(1/2).is_one()
            False
            sage: K.gen().is_one()
            False"""
    @overload
    def is_one(self) -> Any:
        """NumberFieldElement_quadratic.is_one(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1751)

        Check whether this number field element is `1`.

        EXAMPLES::

            sage: K = QuadraticField(-2)
            sage: K(1).is_one()
            True
            sage: K(-1).is_one()
            False
            sage: K(2).is_one()
            False
            sage: K(0).is_one()
            False
            sage: K(1/2).is_one()
            False
            sage: K.gen().is_one()
            False"""
    @overload
    def is_one(self) -> Any:
        """NumberFieldElement_quadratic.is_one(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1751)

        Check whether this number field element is `1`.

        EXAMPLES::

            sage: K = QuadraticField(-2)
            sage: K(1).is_one()
            True
            sage: K(-1).is_one()
            False
            sage: K(2).is_one()
            False
            sage: K(0).is_one()
            False
            sage: K(1/2).is_one()
            False
            sage: K.gen().is_one()
            False"""
    @overload
    def is_one(self) -> Any:
        """NumberFieldElement_quadratic.is_one(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1751)

        Check whether this number field element is `1`.

        EXAMPLES::

            sage: K = QuadraticField(-2)
            sage: K(1).is_one()
            True
            sage: K(-1).is_one()
            False
            sage: K(2).is_one()
            False
            sage: K(0).is_one()
            False
            sage: K(1/2).is_one()
            False
            sage: K.gen().is_one()
            False"""
    @overload
    def is_one(self) -> Any:
        """NumberFieldElement_quadratic.is_one(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1751)

        Check whether this number field element is `1`.

        EXAMPLES::

            sage: K = QuadraticField(-2)
            sage: K(1).is_one()
            True
            sage: K(-1).is_one()
            False
            sage: K(2).is_one()
            False
            sage: K(0).is_one()
            False
            sage: K(1/2).is_one()
            False
            sage: K.gen().is_one()
            False"""
    @overload
    def is_rational(self) -> bool:
        """NumberFieldElement_quadratic.is_rational(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1775)

        Check whether this number field element is a rational number.

        .. SEEALSO::

            - :meth:`is_integer` to test if this element is an integer
            - :meth:`is_integral` to test if this element is an algebraic integer

        EXAMPLES::

            sage: K.<sqrt3> = QuadraticField(3)
            sage: sqrt3.is_rational()
            False
            sage: (sqrt3 - 1/2).is_rational()
            False
            sage: K(0).is_rational()
            True
            sage: K(-12).is_rational()
            True
            sage: K(1/3).is_rational()
            True"""
    @overload
    def is_rational(self) -> Any:
        """NumberFieldElement_quadratic.is_rational(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1775)

        Check whether this number field element is a rational number.

        .. SEEALSO::

            - :meth:`is_integer` to test if this element is an integer
            - :meth:`is_integral` to test if this element is an algebraic integer

        EXAMPLES::

            sage: K.<sqrt3> = QuadraticField(3)
            sage: sqrt3.is_rational()
            False
            sage: (sqrt3 - 1/2).is_rational()
            False
            sage: K(0).is_rational()
            True
            sage: K(-12).is_rational()
            True
            sage: K(1/3).is_rational()
            True"""
    @overload
    def is_rational(self) -> Any:
        """NumberFieldElement_quadratic.is_rational(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1775)

        Check whether this number field element is a rational number.

        .. SEEALSO::

            - :meth:`is_integer` to test if this element is an integer
            - :meth:`is_integral` to test if this element is an algebraic integer

        EXAMPLES::

            sage: K.<sqrt3> = QuadraticField(3)
            sage: sqrt3.is_rational()
            False
            sage: (sqrt3 - 1/2).is_rational()
            False
            sage: K(0).is_rational()
            True
            sage: K(-12).is_rational()
            True
            sage: K(1/3).is_rational()
            True"""
    @overload
    def is_rational(self) -> Any:
        """NumberFieldElement_quadratic.is_rational(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1775)

        Check whether this number field element is a rational number.

        .. SEEALSO::

            - :meth:`is_integer` to test if this element is an integer
            - :meth:`is_integral` to test if this element is an algebraic integer

        EXAMPLES::

            sage: K.<sqrt3> = QuadraticField(3)
            sage: sqrt3.is_rational()
            False
            sage: (sqrt3 - 1/2).is_rational()
            False
            sage: K(0).is_rational()
            True
            sage: K(-12).is_rational()
            True
            sage: K(1/3).is_rational()
            True"""
    @overload
    def is_rational(self) -> Any:
        """NumberFieldElement_quadratic.is_rational(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1775)

        Check whether this number field element is a rational number.

        .. SEEALSO::

            - :meth:`is_integer` to test if this element is an integer
            - :meth:`is_integral` to test if this element is an algebraic integer

        EXAMPLES::

            sage: K.<sqrt3> = QuadraticField(3)
            sage: sqrt3.is_rational()
            False
            sage: (sqrt3 - 1/2).is_rational()
            False
            sage: K(0).is_rational()
            True
            sage: K(-12).is_rational()
            True
            sage: K(1/3).is_rational()
            True"""
    @overload
    def is_rational(self) -> Any:
        """NumberFieldElement_quadratic.is_rational(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1775)

        Check whether this number field element is a rational number.

        .. SEEALSO::

            - :meth:`is_integer` to test if this element is an integer
            - :meth:`is_integral` to test if this element is an algebraic integer

        EXAMPLES::

            sage: K.<sqrt3> = QuadraticField(3)
            sage: sqrt3.is_rational()
            False
            sage: (sqrt3 - 1/2).is_rational()
            False
            sage: K(0).is_rational()
            True
            sage: K(-12).is_rational()
            True
            sage: K(1/3).is_rational()
            True"""
    def minpoly(self, var=..., algorithm=...) -> Any:
        """NumberFieldElement_quadratic.minpoly(self, var='x', algorithm=None)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2229)

        The minimal polynomial of this element over `\\QQ`.

        INPUT:

        - ``var`` -- the minimal polynomial is defined over a polynomial ring
          in a variable with this name; if not specified, this defaults to ``'x'``
        - ``algorithm`` -- for compatibility with general number field
          elements; ignored

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + 13)
            sage: a.minpoly()
            x^2 + 13
            sage: a.minpoly('T')
            T^2 + 13
            sage: (a + 1/2 - a).minpoly()
            x - 1/2"""
    def norm(self, K=...) -> Any:
        """NumberFieldElement_quadratic.norm(self, K=None)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2054)

        Return the norm of ``self``.

        If the second argument is ``None``, this is the
        norm down to `\\QQ`. Otherwise, return the norm down to `K` (which had
        better be either `\\QQ` or this number field).

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - x + 3)
            sage: a.norm()
            3
            sage: a.matrix()
            [ 0  1]
            [-3  1]
            sage: K.<a> = NumberField(x^2 + 5)
            sage: (1 + a).norm()
            6

        The norm is multiplicative::

            sage: K.<a> = NumberField(x^2 - 3)
            sage: a.norm()
            -3
            sage: K(3).norm()
            9
            sage: (3*a).norm()
            -27

        We test that the optional argument is handled sensibly::

            sage: (3*a).norm(QQ)
            -27
            sage: (3*a).norm(K)
            3*a
            sage: (3*a).norm(CyclotomicField(3))
            Traceback (most recent call last):
            ...
            ValueError: no way to embed L into parent's base ring K"""
    @overload
    def numerator(self) -> Any:
        """NumberFieldElement_quadratic.numerator(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1999)

        Return ``self * self.denominator()``.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + x + 41)
            sage: b = (2*a+1)/6
            sage: b.denominator()
            6
            sage: b.numerator()
            2*a + 1"""
    @overload
    def numerator(self) -> Any:
        """NumberFieldElement_quadratic.numerator(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1999)

        Return ``self * self.denominator()``.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + x + 41)
            sage: b = (2*a+1)/6
            sage: b.denominator()
            6
            sage: b.numerator()
            2*a + 1"""
    def parts(self) -> tuple:
        """NumberFieldElement_quadratic.parts(self) -> tuple

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 912)

        Return a pair of rationals `a` and `b` such that ``self`` `=
        a+b\\sqrt{D}`.

        This is much closer to the internal storage format of the
        elements than the polynomial representation coefficients (the output of
        ``self.list()``), unless the generator with which this number field was
        constructed was equal to `\\sqrt{D}`. See the last example below.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - 13)
            sage: K.discriminant()
            13
            sage: a.parts()
            (0, 1)
            sage: (a/2 - 4).parts()
            (-4, 1/2)
            sage: K.<a> = NumberField(x^2 - 7)
            sage: K.discriminant()
            28
            sage: a.parts()
            (0, 1)
            sage: K.<a> = NumberField(x^2 - x + 7)
            sage: a.parts()
            (1/2, 3/2)
            sage: a._coefficients()
            [0, 1]"""
    @overload
    def real(self) -> Any:
        """NumberFieldElement_quadratic.real(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1825)

        Return the real part of ``self``, which is either ``self`` (if
        ``self`` lives in a totally real field) or a rational number.

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2)
            sage: sqrt2.real()
            sqrt2
            sage: K.<a> = QuadraticField(-3)
            sage: a.real()
            0
            sage: (a + 1/2).real()
            1/2
            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + x + 1)
            sage: a.real()
            -1/2
            sage: parent(a.real())
            Rational Field
            sage: K.<i> = QuadraticField(-1)
            sage: i.real()
            0"""
    @overload
    def real(self) -> Any:
        """NumberFieldElement_quadratic.real(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1825)

        Return the real part of ``self``, which is either ``self`` (if
        ``self`` lives in a totally real field) or a rational number.

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2)
            sage: sqrt2.real()
            sqrt2
            sage: K.<a> = QuadraticField(-3)
            sage: a.real()
            0
            sage: (a + 1/2).real()
            1/2
            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + x + 1)
            sage: a.real()
            -1/2
            sage: parent(a.real())
            Rational Field
            sage: K.<i> = QuadraticField(-1)
            sage: i.real()
            0"""
    @overload
    def real(self) -> Any:
        """NumberFieldElement_quadratic.real(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1825)

        Return the real part of ``self``, which is either ``self`` (if
        ``self`` lives in a totally real field) or a rational number.

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2)
            sage: sqrt2.real()
            sqrt2
            sage: K.<a> = QuadraticField(-3)
            sage: a.real()
            0
            sage: (a + 1/2).real()
            1/2
            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + x + 1)
            sage: a.real()
            -1/2
            sage: parent(a.real())
            Rational Field
            sage: K.<i> = QuadraticField(-1)
            sage: i.real()
            0"""
    @overload
    def real(self) -> Any:
        """NumberFieldElement_quadratic.real(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1825)

        Return the real part of ``self``, which is either ``self`` (if
        ``self`` lives in a totally real field) or a rational number.

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2)
            sage: sqrt2.real()
            sqrt2
            sage: K.<a> = QuadraticField(-3)
            sage: a.real()
            0
            sage: (a + 1/2).real()
            1/2
            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + x + 1)
            sage: a.real()
            -1/2
            sage: parent(a.real())
            Rational Field
            sage: K.<i> = QuadraticField(-1)
            sage: i.real()
            0"""
    @overload
    def real(self) -> Any:
        """NumberFieldElement_quadratic.real(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1825)

        Return the real part of ``self``, which is either ``self`` (if
        ``self`` lives in a totally real field) or a rational number.

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2)
            sage: sqrt2.real()
            sqrt2
            sage: K.<a> = QuadraticField(-3)
            sage: a.real()
            0
            sage: (a + 1/2).real()
            1/2
            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + x + 1)
            sage: a.real()
            -1/2
            sage: parent(a.real())
            Rational Field
            sage: K.<i> = QuadraticField(-1)
            sage: i.real()
            0"""
    @overload
    def real(self) -> Any:
        """NumberFieldElement_quadratic.real(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1825)

        Return the real part of ``self``, which is either ``self`` (if
        ``self`` lives in a totally real field) or a rational number.

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2)
            sage: sqrt2.real()
            sqrt2
            sage: K.<a> = QuadraticField(-3)
            sage: a.real()
            0
            sage: (a + 1/2).real()
            1/2
            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + x + 1)
            sage: a.real()
            -1/2
            sage: parent(a.real())
            Rational Field
            sage: K.<i> = QuadraticField(-1)
            sage: i.real()
            0"""
    @overload
    def real(self) -> Any:
        """NumberFieldElement_quadratic.real(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1825)

        Return the real part of ``self``, which is either ``self`` (if
        ``self`` lives in a totally real field) or a rational number.

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2)
            sage: sqrt2.real()
            sqrt2
            sage: K.<a> = QuadraticField(-3)
            sage: a.real()
            0
            sage: (a + 1/2).real()
            1/2
            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + x + 1)
            sage: a.real()
            -1/2
            sage: parent(a.real())
            Rational Field
            sage: K.<i> = QuadraticField(-1)
            sage: i.real()
            0"""
    @overload
    def round(self) -> Any:
        """NumberFieldElement_quadratic.round(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2386)

        Return the round (nearest integer) of this number field element. In case
        of ties, this relies on the default rounding for rational numbers.

        EXAMPLES::

            sage: K.<sqrt7> = QuadraticField(7, name='sqrt7')
            sage: sqrt7.round()
            3
            sage: (-sqrt7).round()
            -3
            sage: (12/313*sqrt7 - 1745917/2902921).round()
            0
            sage: (12/313*sqrt7 - 1745918/2902921).round()
            -1

        TESTS::

            sage: K2.<sqrt2> = QuadraticField(2)
            sage: K3.<sqrt3> = QuadraticField(3)
            sage: K5.<sqrt5> = QuadraticField(5)
            sage: for _ in range(100):
            ....:    a = QQ.random_element(1000,20)
            ....:    b = QQ.random_element(1000,20)
            ....:    assert a.round() == round(K2(a)), a
            ....:    assert a.round() == round(K3(a)), a
            ....:    assert a.round() == round(K5(a)), a
            ....:    assert round(a+b*sqrt(2.)) == round(a+b*sqrt2), (a, b)
            ....:    assert round(a+b*sqrt(3.)) == round(a+b*sqrt3), (a, b)
            ....:    assert round(a+b*sqrt(5.)) == round(a+b*sqrt5), (a, b)"""
    @overload
    def round(self, nearestinteger) -> Any:
        """NumberFieldElement_quadratic.round(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2386)

        Return the round (nearest integer) of this number field element. In case
        of ties, this relies on the default rounding for rational numbers.

        EXAMPLES::

            sage: K.<sqrt7> = QuadraticField(7, name='sqrt7')
            sage: sqrt7.round()
            3
            sage: (-sqrt7).round()
            -3
            sage: (12/313*sqrt7 - 1745917/2902921).round()
            0
            sage: (12/313*sqrt7 - 1745918/2902921).round()
            -1

        TESTS::

            sage: K2.<sqrt2> = QuadraticField(2)
            sage: K3.<sqrt3> = QuadraticField(3)
            sage: K5.<sqrt5> = QuadraticField(5)
            sage: for _ in range(100):
            ....:    a = QQ.random_element(1000,20)
            ....:    b = QQ.random_element(1000,20)
            ....:    assert a.round() == round(K2(a)), a
            ....:    assert a.round() == round(K3(a)), a
            ....:    assert a.round() == round(K5(a)), a
            ....:    assert round(a+b*sqrt(2.)) == round(a+b*sqrt2), (a, b)
            ....:    assert round(a+b*sqrt(3.)) == round(a+b*sqrt3), (a, b)
            ....:    assert round(a+b*sqrt(5.)) == round(a+b*sqrt5), (a, b)"""
    @overload
    def round(self) -> Any:
        """NumberFieldElement_quadratic.round(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2386)

        Return the round (nearest integer) of this number field element. In case
        of ties, this relies on the default rounding for rational numbers.

        EXAMPLES::

            sage: K.<sqrt7> = QuadraticField(7, name='sqrt7')
            sage: sqrt7.round()
            3
            sage: (-sqrt7).round()
            -3
            sage: (12/313*sqrt7 - 1745917/2902921).round()
            0
            sage: (12/313*sqrt7 - 1745918/2902921).round()
            -1

        TESTS::

            sage: K2.<sqrt2> = QuadraticField(2)
            sage: K3.<sqrt3> = QuadraticField(3)
            sage: K5.<sqrt5> = QuadraticField(5)
            sage: for _ in range(100):
            ....:    a = QQ.random_element(1000,20)
            ....:    b = QQ.random_element(1000,20)
            ....:    assert a.round() == round(K2(a)), a
            ....:    assert a.round() == round(K3(a)), a
            ....:    assert a.round() == round(K5(a)), a
            ....:    assert round(a+b*sqrt(2.)) == round(a+b*sqrt2), (a, b)
            ....:    assert round(a+b*sqrt(3.)) == round(a+b*sqrt3), (a, b)
            ....:    assert round(a+b*sqrt(5.)) == round(a+b*sqrt5), (a, b)"""
    @overload
    def round(self) -> Any:
        """NumberFieldElement_quadratic.round(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2386)

        Return the round (nearest integer) of this number field element. In case
        of ties, this relies on the default rounding for rational numbers.

        EXAMPLES::

            sage: K.<sqrt7> = QuadraticField(7, name='sqrt7')
            sage: sqrt7.round()
            3
            sage: (-sqrt7).round()
            -3
            sage: (12/313*sqrt7 - 1745917/2902921).round()
            0
            sage: (12/313*sqrt7 - 1745918/2902921).round()
            -1

        TESTS::

            sage: K2.<sqrt2> = QuadraticField(2)
            sage: K3.<sqrt3> = QuadraticField(3)
            sage: K5.<sqrt5> = QuadraticField(5)
            sage: for _ in range(100):
            ....:    a = QQ.random_element(1000,20)
            ....:    b = QQ.random_element(1000,20)
            ....:    assert a.round() == round(K2(a)), a
            ....:    assert a.round() == round(K3(a)), a
            ....:    assert a.round() == round(K5(a)), a
            ....:    assert round(a+b*sqrt(2.)) == round(a+b*sqrt2), (a, b)
            ....:    assert round(a+b*sqrt(3.)) == round(a+b*sqrt3), (a, b)
            ....:    assert round(a+b*sqrt(5.)) == round(a+b*sqrt5), (a, b)"""
    @overload
    def round(self) -> Any:
        """NumberFieldElement_quadratic.round(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2386)

        Return the round (nearest integer) of this number field element. In case
        of ties, this relies on the default rounding for rational numbers.

        EXAMPLES::

            sage: K.<sqrt7> = QuadraticField(7, name='sqrt7')
            sage: sqrt7.round()
            3
            sage: (-sqrt7).round()
            -3
            sage: (12/313*sqrt7 - 1745917/2902921).round()
            0
            sage: (12/313*sqrt7 - 1745918/2902921).round()
            -1

        TESTS::

            sage: K2.<sqrt2> = QuadraticField(2)
            sage: K3.<sqrt3> = QuadraticField(3)
            sage: K5.<sqrt5> = QuadraticField(5)
            sage: for _ in range(100):
            ....:    a = QQ.random_element(1000,20)
            ....:    b = QQ.random_element(1000,20)
            ....:    assert a.round() == round(K2(a)), a
            ....:    assert a.round() == round(K3(a)), a
            ....:    assert a.round() == round(K5(a)), a
            ....:    assert round(a+b*sqrt(2.)) == round(a+b*sqrt2), (a, b)
            ....:    assert round(a+b*sqrt(3.)) == round(a+b*sqrt3), (a, b)
            ....:    assert round(a+b*sqrt(5.)) == round(a+b*sqrt5), (a, b)"""
    @overload
    def round(self) -> Any:
        """NumberFieldElement_quadratic.round(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2386)

        Return the round (nearest integer) of this number field element. In case
        of ties, this relies on the default rounding for rational numbers.

        EXAMPLES::

            sage: K.<sqrt7> = QuadraticField(7, name='sqrt7')
            sage: sqrt7.round()
            3
            sage: (-sqrt7).round()
            -3
            sage: (12/313*sqrt7 - 1745917/2902921).round()
            0
            sage: (12/313*sqrt7 - 1745918/2902921).round()
            -1

        TESTS::

            sage: K2.<sqrt2> = QuadraticField(2)
            sage: K3.<sqrt3> = QuadraticField(3)
            sage: K5.<sqrt5> = QuadraticField(5)
            sage: for _ in range(100):
            ....:    a = QQ.random_element(1000,20)
            ....:    b = QQ.random_element(1000,20)
            ....:    assert a.round() == round(K2(a)), a
            ....:    assert a.round() == round(K3(a)), a
            ....:    assert a.round() == round(K5(a)), a
            ....:    assert round(a+b*sqrt(2.)) == round(a+b*sqrt2), (a, b)
            ....:    assert round(a+b*sqrt(3.)) == round(a+b*sqrt3), (a, b)
            ....:    assert round(a+b*sqrt(5.)) == round(a+b*sqrt5), (a, b)"""
    @overload
    def sign(self) -> Any:
        """NumberFieldElement_quadratic.sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 964)

        Return the sign of ``self`` (`0` if zero, `+1` if positive, and `-1` if
        negative).

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2, name='sqrt2')
            sage: K(0).sign()
            0
            sage: sqrt2.sign()
            1
            sage: (sqrt2+1).sign()
            1
            sage: (sqrt2-1).sign()
            1
            sage: (sqrt2-2).sign()
            -1
            sage: (-sqrt2).sign()
            -1
            sage: (-sqrt2+1).sign()
            -1
            sage: (-sqrt2+2).sign()
            1

            sage: K.<a> = QuadraticField(2, embedding=-1.4142)
            sage: K(0).sign()
            0
            sage: a.sign()
            -1
            sage: (a+1).sign()
            -1
            sage: (a+2).sign()
            1
            sage: (a-1).sign()
            -1
            sage: (-a).sign()
            1
            sage: (-a-1).sign()
            1
            sage: (-a-2).sign()
            -1

            sage: # needs sage.symbolic
            sage: x = polygen(ZZ, 'x')
            sage: K.<b> = NumberField(x^2 + 2*x + 7, 'b', embedding=CC(-1,-sqrt(6)))
            sage: b.sign()
            Traceback (most recent call last):
            ...
            ValueError: a complex number has no sign!
            sage: K(1).sign()
            1
            sage: K(0).sign()
            0
            sage: K(-2/3).sign()
            -1"""
    @overload
    def sign(self) -> Any:
        """NumberFieldElement_quadratic.sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 964)

        Return the sign of ``self`` (`0` if zero, `+1` if positive, and `-1` if
        negative).

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2, name='sqrt2')
            sage: K(0).sign()
            0
            sage: sqrt2.sign()
            1
            sage: (sqrt2+1).sign()
            1
            sage: (sqrt2-1).sign()
            1
            sage: (sqrt2-2).sign()
            -1
            sage: (-sqrt2).sign()
            -1
            sage: (-sqrt2+1).sign()
            -1
            sage: (-sqrt2+2).sign()
            1

            sage: K.<a> = QuadraticField(2, embedding=-1.4142)
            sage: K(0).sign()
            0
            sage: a.sign()
            -1
            sage: (a+1).sign()
            -1
            sage: (a+2).sign()
            1
            sage: (a-1).sign()
            -1
            sage: (-a).sign()
            1
            sage: (-a-1).sign()
            1
            sage: (-a-2).sign()
            -1

            sage: # needs sage.symbolic
            sage: x = polygen(ZZ, 'x')
            sage: K.<b> = NumberField(x^2 + 2*x + 7, 'b', embedding=CC(-1,-sqrt(6)))
            sage: b.sign()
            Traceback (most recent call last):
            ...
            ValueError: a complex number has no sign!
            sage: K(1).sign()
            1
            sage: K(0).sign()
            0
            sage: K(-2/3).sign()
            -1"""
    @overload
    def sign(self) -> Any:
        """NumberFieldElement_quadratic.sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 964)

        Return the sign of ``self`` (`0` if zero, `+1` if positive, and `-1` if
        negative).

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2, name='sqrt2')
            sage: K(0).sign()
            0
            sage: sqrt2.sign()
            1
            sage: (sqrt2+1).sign()
            1
            sage: (sqrt2-1).sign()
            1
            sage: (sqrt2-2).sign()
            -1
            sage: (-sqrt2).sign()
            -1
            sage: (-sqrt2+1).sign()
            -1
            sage: (-sqrt2+2).sign()
            1

            sage: K.<a> = QuadraticField(2, embedding=-1.4142)
            sage: K(0).sign()
            0
            sage: a.sign()
            -1
            sage: (a+1).sign()
            -1
            sage: (a+2).sign()
            1
            sage: (a-1).sign()
            -1
            sage: (-a).sign()
            1
            sage: (-a-1).sign()
            1
            sage: (-a-2).sign()
            -1

            sage: # needs sage.symbolic
            sage: x = polygen(ZZ, 'x')
            sage: K.<b> = NumberField(x^2 + 2*x + 7, 'b', embedding=CC(-1,-sqrt(6)))
            sage: b.sign()
            Traceback (most recent call last):
            ...
            ValueError: a complex number has no sign!
            sage: K(1).sign()
            1
            sage: K(0).sign()
            0
            sage: K(-2/3).sign()
            -1"""
    @overload
    def sign(self) -> Any:
        """NumberFieldElement_quadratic.sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 964)

        Return the sign of ``self`` (`0` if zero, `+1` if positive, and `-1` if
        negative).

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2, name='sqrt2')
            sage: K(0).sign()
            0
            sage: sqrt2.sign()
            1
            sage: (sqrt2+1).sign()
            1
            sage: (sqrt2-1).sign()
            1
            sage: (sqrt2-2).sign()
            -1
            sage: (-sqrt2).sign()
            -1
            sage: (-sqrt2+1).sign()
            -1
            sage: (-sqrt2+2).sign()
            1

            sage: K.<a> = QuadraticField(2, embedding=-1.4142)
            sage: K(0).sign()
            0
            sage: a.sign()
            -1
            sage: (a+1).sign()
            -1
            sage: (a+2).sign()
            1
            sage: (a-1).sign()
            -1
            sage: (-a).sign()
            1
            sage: (-a-1).sign()
            1
            sage: (-a-2).sign()
            -1

            sage: # needs sage.symbolic
            sage: x = polygen(ZZ, 'x')
            sage: K.<b> = NumberField(x^2 + 2*x + 7, 'b', embedding=CC(-1,-sqrt(6)))
            sage: b.sign()
            Traceback (most recent call last):
            ...
            ValueError: a complex number has no sign!
            sage: K(1).sign()
            1
            sage: K(0).sign()
            0
            sage: K(-2/3).sign()
            -1"""
    @overload
    def sign(self) -> Any:
        """NumberFieldElement_quadratic.sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 964)

        Return the sign of ``self`` (`0` if zero, `+1` if positive, and `-1` if
        negative).

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2, name='sqrt2')
            sage: K(0).sign()
            0
            sage: sqrt2.sign()
            1
            sage: (sqrt2+1).sign()
            1
            sage: (sqrt2-1).sign()
            1
            sage: (sqrt2-2).sign()
            -1
            sage: (-sqrt2).sign()
            -1
            sage: (-sqrt2+1).sign()
            -1
            sage: (-sqrt2+2).sign()
            1

            sage: K.<a> = QuadraticField(2, embedding=-1.4142)
            sage: K(0).sign()
            0
            sage: a.sign()
            -1
            sage: (a+1).sign()
            -1
            sage: (a+2).sign()
            1
            sage: (a-1).sign()
            -1
            sage: (-a).sign()
            1
            sage: (-a-1).sign()
            1
            sage: (-a-2).sign()
            -1

            sage: # needs sage.symbolic
            sage: x = polygen(ZZ, 'x')
            sage: K.<b> = NumberField(x^2 + 2*x + 7, 'b', embedding=CC(-1,-sqrt(6)))
            sage: b.sign()
            Traceback (most recent call last):
            ...
            ValueError: a complex number has no sign!
            sage: K(1).sign()
            1
            sage: K(0).sign()
            0
            sage: K(-2/3).sign()
            -1"""
    @overload
    def sign(self) -> Any:
        """NumberFieldElement_quadratic.sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 964)

        Return the sign of ``self`` (`0` if zero, `+1` if positive, and `-1` if
        negative).

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2, name='sqrt2')
            sage: K(0).sign()
            0
            sage: sqrt2.sign()
            1
            sage: (sqrt2+1).sign()
            1
            sage: (sqrt2-1).sign()
            1
            sage: (sqrt2-2).sign()
            -1
            sage: (-sqrt2).sign()
            -1
            sage: (-sqrt2+1).sign()
            -1
            sage: (-sqrt2+2).sign()
            1

            sage: K.<a> = QuadraticField(2, embedding=-1.4142)
            sage: K(0).sign()
            0
            sage: a.sign()
            -1
            sage: (a+1).sign()
            -1
            sage: (a+2).sign()
            1
            sage: (a-1).sign()
            -1
            sage: (-a).sign()
            1
            sage: (-a-1).sign()
            1
            sage: (-a-2).sign()
            -1

            sage: # needs sage.symbolic
            sage: x = polygen(ZZ, 'x')
            sage: K.<b> = NumberField(x^2 + 2*x + 7, 'b', embedding=CC(-1,-sqrt(6)))
            sage: b.sign()
            Traceback (most recent call last):
            ...
            ValueError: a complex number has no sign!
            sage: K(1).sign()
            1
            sage: K(0).sign()
            0
            sage: K(-2/3).sign()
            -1"""
    @overload
    def sign(self) -> Any:
        """NumberFieldElement_quadratic.sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 964)

        Return the sign of ``self`` (`0` if zero, `+1` if positive, and `-1` if
        negative).

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2, name='sqrt2')
            sage: K(0).sign()
            0
            sage: sqrt2.sign()
            1
            sage: (sqrt2+1).sign()
            1
            sage: (sqrt2-1).sign()
            1
            sage: (sqrt2-2).sign()
            -1
            sage: (-sqrt2).sign()
            -1
            sage: (-sqrt2+1).sign()
            -1
            sage: (-sqrt2+2).sign()
            1

            sage: K.<a> = QuadraticField(2, embedding=-1.4142)
            sage: K(0).sign()
            0
            sage: a.sign()
            -1
            sage: (a+1).sign()
            -1
            sage: (a+2).sign()
            1
            sage: (a-1).sign()
            -1
            sage: (-a).sign()
            1
            sage: (-a-1).sign()
            1
            sage: (-a-2).sign()
            -1

            sage: # needs sage.symbolic
            sage: x = polygen(ZZ, 'x')
            sage: K.<b> = NumberField(x^2 + 2*x + 7, 'b', embedding=CC(-1,-sqrt(6)))
            sage: b.sign()
            Traceback (most recent call last):
            ...
            ValueError: a complex number has no sign!
            sage: K(1).sign()
            1
            sage: K(0).sign()
            0
            sage: K(-2/3).sign()
            -1"""
    @overload
    def sign(self) -> Any:
        """NumberFieldElement_quadratic.sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 964)

        Return the sign of ``self`` (`0` if zero, `+1` if positive, and `-1` if
        negative).

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2, name='sqrt2')
            sage: K(0).sign()
            0
            sage: sqrt2.sign()
            1
            sage: (sqrt2+1).sign()
            1
            sage: (sqrt2-1).sign()
            1
            sage: (sqrt2-2).sign()
            -1
            sage: (-sqrt2).sign()
            -1
            sage: (-sqrt2+1).sign()
            -1
            sage: (-sqrt2+2).sign()
            1

            sage: K.<a> = QuadraticField(2, embedding=-1.4142)
            sage: K(0).sign()
            0
            sage: a.sign()
            -1
            sage: (a+1).sign()
            -1
            sage: (a+2).sign()
            1
            sage: (a-1).sign()
            -1
            sage: (-a).sign()
            1
            sage: (-a-1).sign()
            1
            sage: (-a-2).sign()
            -1

            sage: # needs sage.symbolic
            sage: x = polygen(ZZ, 'x')
            sage: K.<b> = NumberField(x^2 + 2*x + 7, 'b', embedding=CC(-1,-sqrt(6)))
            sage: b.sign()
            Traceback (most recent call last):
            ...
            ValueError: a complex number has no sign!
            sage: K(1).sign()
            1
            sage: K(0).sign()
            0
            sage: K(-2/3).sign()
            -1"""
    @overload
    def sign(self) -> Any:
        """NumberFieldElement_quadratic.sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 964)

        Return the sign of ``self`` (`0` if zero, `+1` if positive, and `-1` if
        negative).

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2, name='sqrt2')
            sage: K(0).sign()
            0
            sage: sqrt2.sign()
            1
            sage: (sqrt2+1).sign()
            1
            sage: (sqrt2-1).sign()
            1
            sage: (sqrt2-2).sign()
            -1
            sage: (-sqrt2).sign()
            -1
            sage: (-sqrt2+1).sign()
            -1
            sage: (-sqrt2+2).sign()
            1

            sage: K.<a> = QuadraticField(2, embedding=-1.4142)
            sage: K(0).sign()
            0
            sage: a.sign()
            -1
            sage: (a+1).sign()
            -1
            sage: (a+2).sign()
            1
            sage: (a-1).sign()
            -1
            sage: (-a).sign()
            1
            sage: (-a-1).sign()
            1
            sage: (-a-2).sign()
            -1

            sage: # needs sage.symbolic
            sage: x = polygen(ZZ, 'x')
            sage: K.<b> = NumberField(x^2 + 2*x + 7, 'b', embedding=CC(-1,-sqrt(6)))
            sage: b.sign()
            Traceback (most recent call last):
            ...
            ValueError: a complex number has no sign!
            sage: K(1).sign()
            1
            sage: K(0).sign()
            0
            sage: K(-2/3).sign()
            -1"""
    @overload
    def sign(self) -> Any:
        """NumberFieldElement_quadratic.sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 964)

        Return the sign of ``self`` (`0` if zero, `+1` if positive, and `-1` if
        negative).

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2, name='sqrt2')
            sage: K(0).sign()
            0
            sage: sqrt2.sign()
            1
            sage: (sqrt2+1).sign()
            1
            sage: (sqrt2-1).sign()
            1
            sage: (sqrt2-2).sign()
            -1
            sage: (-sqrt2).sign()
            -1
            sage: (-sqrt2+1).sign()
            -1
            sage: (-sqrt2+2).sign()
            1

            sage: K.<a> = QuadraticField(2, embedding=-1.4142)
            sage: K(0).sign()
            0
            sage: a.sign()
            -1
            sage: (a+1).sign()
            -1
            sage: (a+2).sign()
            1
            sage: (a-1).sign()
            -1
            sage: (-a).sign()
            1
            sage: (-a-1).sign()
            1
            sage: (-a-2).sign()
            -1

            sage: # needs sage.symbolic
            sage: x = polygen(ZZ, 'x')
            sage: K.<b> = NumberField(x^2 + 2*x + 7, 'b', embedding=CC(-1,-sqrt(6)))
            sage: b.sign()
            Traceback (most recent call last):
            ...
            ValueError: a complex number has no sign!
            sage: K(1).sign()
            1
            sage: K(0).sign()
            0
            sage: K(-2/3).sign()
            -1"""
    @overload
    def sign(self) -> Any:
        """NumberFieldElement_quadratic.sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 964)

        Return the sign of ``self`` (`0` if zero, `+1` if positive, and `-1` if
        negative).

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2, name='sqrt2')
            sage: K(0).sign()
            0
            sage: sqrt2.sign()
            1
            sage: (sqrt2+1).sign()
            1
            sage: (sqrt2-1).sign()
            1
            sage: (sqrt2-2).sign()
            -1
            sage: (-sqrt2).sign()
            -1
            sage: (-sqrt2+1).sign()
            -1
            sage: (-sqrt2+2).sign()
            1

            sage: K.<a> = QuadraticField(2, embedding=-1.4142)
            sage: K(0).sign()
            0
            sage: a.sign()
            -1
            sage: (a+1).sign()
            -1
            sage: (a+2).sign()
            1
            sage: (a-1).sign()
            -1
            sage: (-a).sign()
            1
            sage: (-a-1).sign()
            1
            sage: (-a-2).sign()
            -1

            sage: # needs sage.symbolic
            sage: x = polygen(ZZ, 'x')
            sage: K.<b> = NumberField(x^2 + 2*x + 7, 'b', embedding=CC(-1,-sqrt(6)))
            sage: b.sign()
            Traceback (most recent call last):
            ...
            ValueError: a complex number has no sign!
            sage: K(1).sign()
            1
            sage: K(0).sign()
            0
            sage: K(-2/3).sign()
            -1"""
    @overload
    def sign(self) -> Any:
        """NumberFieldElement_quadratic.sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 964)

        Return the sign of ``self`` (`0` if zero, `+1` if positive, and `-1` if
        negative).

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2, name='sqrt2')
            sage: K(0).sign()
            0
            sage: sqrt2.sign()
            1
            sage: (sqrt2+1).sign()
            1
            sage: (sqrt2-1).sign()
            1
            sage: (sqrt2-2).sign()
            -1
            sage: (-sqrt2).sign()
            -1
            sage: (-sqrt2+1).sign()
            -1
            sage: (-sqrt2+2).sign()
            1

            sage: K.<a> = QuadraticField(2, embedding=-1.4142)
            sage: K(0).sign()
            0
            sage: a.sign()
            -1
            sage: (a+1).sign()
            -1
            sage: (a+2).sign()
            1
            sage: (a-1).sign()
            -1
            sage: (-a).sign()
            1
            sage: (-a-1).sign()
            1
            sage: (-a-2).sign()
            -1

            sage: # needs sage.symbolic
            sage: x = polygen(ZZ, 'x')
            sage: K.<b> = NumberField(x^2 + 2*x + 7, 'b', embedding=CC(-1,-sqrt(6)))
            sage: b.sign()
            Traceback (most recent call last):
            ...
            ValueError: a complex number has no sign!
            sage: K(1).sign()
            1
            sage: K(0).sign()
            0
            sage: K(-2/3).sign()
            -1"""
    @overload
    def sign(self) -> Any:
        """NumberFieldElement_quadratic.sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 964)

        Return the sign of ``self`` (`0` if zero, `+1` if positive, and `-1` if
        negative).

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2, name='sqrt2')
            sage: K(0).sign()
            0
            sage: sqrt2.sign()
            1
            sage: (sqrt2+1).sign()
            1
            sage: (sqrt2-1).sign()
            1
            sage: (sqrt2-2).sign()
            -1
            sage: (-sqrt2).sign()
            -1
            sage: (-sqrt2+1).sign()
            -1
            sage: (-sqrt2+2).sign()
            1

            sage: K.<a> = QuadraticField(2, embedding=-1.4142)
            sage: K(0).sign()
            0
            sage: a.sign()
            -1
            sage: (a+1).sign()
            -1
            sage: (a+2).sign()
            1
            sage: (a-1).sign()
            -1
            sage: (-a).sign()
            1
            sage: (-a-1).sign()
            1
            sage: (-a-2).sign()
            -1

            sage: # needs sage.symbolic
            sage: x = polygen(ZZ, 'x')
            sage: K.<b> = NumberField(x^2 + 2*x + 7, 'b', embedding=CC(-1,-sqrt(6)))
            sage: b.sign()
            Traceback (most recent call last):
            ...
            ValueError: a complex number has no sign!
            sage: K(1).sign()
            1
            sage: K(0).sign()
            0
            sage: K(-2/3).sign()
            -1"""
    @overload
    def sign(self) -> Any:
        """NumberFieldElement_quadratic.sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 964)

        Return the sign of ``self`` (`0` if zero, `+1` if positive, and `-1` if
        negative).

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2, name='sqrt2')
            sage: K(0).sign()
            0
            sage: sqrt2.sign()
            1
            sage: (sqrt2+1).sign()
            1
            sage: (sqrt2-1).sign()
            1
            sage: (sqrt2-2).sign()
            -1
            sage: (-sqrt2).sign()
            -1
            sage: (-sqrt2+1).sign()
            -1
            sage: (-sqrt2+2).sign()
            1

            sage: K.<a> = QuadraticField(2, embedding=-1.4142)
            sage: K(0).sign()
            0
            sage: a.sign()
            -1
            sage: (a+1).sign()
            -1
            sage: (a+2).sign()
            1
            sage: (a-1).sign()
            -1
            sage: (-a).sign()
            1
            sage: (-a-1).sign()
            1
            sage: (-a-2).sign()
            -1

            sage: # needs sage.symbolic
            sage: x = polygen(ZZ, 'x')
            sage: K.<b> = NumberField(x^2 + 2*x + 7, 'b', embedding=CC(-1,-sqrt(6)))
            sage: b.sign()
            Traceback (most recent call last):
            ...
            ValueError: a complex number has no sign!
            sage: K(1).sign()
            1
            sage: K(0).sign()
            0
            sage: K(-2/3).sign()
            -1"""
    @overload
    def sign(self) -> Any:
        """NumberFieldElement_quadratic.sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 964)

        Return the sign of ``self`` (`0` if zero, `+1` if positive, and `-1` if
        negative).

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2, name='sqrt2')
            sage: K(0).sign()
            0
            sage: sqrt2.sign()
            1
            sage: (sqrt2+1).sign()
            1
            sage: (sqrt2-1).sign()
            1
            sage: (sqrt2-2).sign()
            -1
            sage: (-sqrt2).sign()
            -1
            sage: (-sqrt2+1).sign()
            -1
            sage: (-sqrt2+2).sign()
            1

            sage: K.<a> = QuadraticField(2, embedding=-1.4142)
            sage: K(0).sign()
            0
            sage: a.sign()
            -1
            sage: (a+1).sign()
            -1
            sage: (a+2).sign()
            1
            sage: (a-1).sign()
            -1
            sage: (-a).sign()
            1
            sage: (-a-1).sign()
            1
            sage: (-a-2).sign()
            -1

            sage: # needs sage.symbolic
            sage: x = polygen(ZZ, 'x')
            sage: K.<b> = NumberField(x^2 + 2*x + 7, 'b', embedding=CC(-1,-sqrt(6)))
            sage: b.sign()
            Traceback (most recent call last):
            ...
            ValueError: a complex number has no sign!
            sage: K(1).sign()
            1
            sage: K(0).sign()
            0
            sage: K(-2/3).sign()
            -1"""
    @overload
    def sign(self) -> Any:
        """NumberFieldElement_quadratic.sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 964)

        Return the sign of ``self`` (`0` if zero, `+1` if positive, and `-1` if
        negative).

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2, name='sqrt2')
            sage: K(0).sign()
            0
            sage: sqrt2.sign()
            1
            sage: (sqrt2+1).sign()
            1
            sage: (sqrt2-1).sign()
            1
            sage: (sqrt2-2).sign()
            -1
            sage: (-sqrt2).sign()
            -1
            sage: (-sqrt2+1).sign()
            -1
            sage: (-sqrt2+2).sign()
            1

            sage: K.<a> = QuadraticField(2, embedding=-1.4142)
            sage: K(0).sign()
            0
            sage: a.sign()
            -1
            sage: (a+1).sign()
            -1
            sage: (a+2).sign()
            1
            sage: (a-1).sign()
            -1
            sage: (-a).sign()
            1
            sage: (-a-1).sign()
            1
            sage: (-a-2).sign()
            -1

            sage: # needs sage.symbolic
            sage: x = polygen(ZZ, 'x')
            sage: K.<b> = NumberField(x^2 + 2*x + 7, 'b', embedding=CC(-1,-sqrt(6)))
            sage: b.sign()
            Traceback (most recent call last):
            ...
            ValueError: a complex number has no sign!
            sage: K(1).sign()
            1
            sage: K(0).sign()
            0
            sage: K(-2/3).sign()
            -1"""
    @overload
    def sign(self) -> Any:
        """NumberFieldElement_quadratic.sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 964)

        Return the sign of ``self`` (`0` if zero, `+1` if positive, and `-1` if
        negative).

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2, name='sqrt2')
            sage: K(0).sign()
            0
            sage: sqrt2.sign()
            1
            sage: (sqrt2+1).sign()
            1
            sage: (sqrt2-1).sign()
            1
            sage: (sqrt2-2).sign()
            -1
            sage: (-sqrt2).sign()
            -1
            sage: (-sqrt2+1).sign()
            -1
            sage: (-sqrt2+2).sign()
            1

            sage: K.<a> = QuadraticField(2, embedding=-1.4142)
            sage: K(0).sign()
            0
            sage: a.sign()
            -1
            sage: (a+1).sign()
            -1
            sage: (a+2).sign()
            1
            sage: (a-1).sign()
            -1
            sage: (-a).sign()
            1
            sage: (-a-1).sign()
            1
            sage: (-a-2).sign()
            -1

            sage: # needs sage.symbolic
            sage: x = polygen(ZZ, 'x')
            sage: K.<b> = NumberField(x^2 + 2*x + 7, 'b', embedding=CC(-1,-sqrt(6)))
            sage: b.sign()
            Traceback (most recent call last):
            ...
            ValueError: a complex number has no sign!
            sage: K(1).sign()
            1
            sage: K(0).sign()
            0
            sage: K(-2/3).sign()
            -1"""
    @overload
    def sign(self) -> Any:
        """NumberFieldElement_quadratic.sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 964)

        Return the sign of ``self`` (`0` if zero, `+1` if positive, and `-1` if
        negative).

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2, name='sqrt2')
            sage: K(0).sign()
            0
            sage: sqrt2.sign()
            1
            sage: (sqrt2+1).sign()
            1
            sage: (sqrt2-1).sign()
            1
            sage: (sqrt2-2).sign()
            -1
            sage: (-sqrt2).sign()
            -1
            sage: (-sqrt2+1).sign()
            -1
            sage: (-sqrt2+2).sign()
            1

            sage: K.<a> = QuadraticField(2, embedding=-1.4142)
            sage: K(0).sign()
            0
            sage: a.sign()
            -1
            sage: (a+1).sign()
            -1
            sage: (a+2).sign()
            1
            sage: (a-1).sign()
            -1
            sage: (-a).sign()
            1
            sage: (-a-1).sign()
            1
            sage: (-a-2).sign()
            -1

            sage: # needs sage.symbolic
            sage: x = polygen(ZZ, 'x')
            sage: K.<b> = NumberField(x^2 + 2*x + 7, 'b', embedding=CC(-1,-sqrt(6)))
            sage: b.sign()
            Traceback (most recent call last):
            ...
            ValueError: a complex number has no sign!
            sage: K(1).sign()
            1
            sage: K(0).sign()
            0
            sage: K(-2/3).sign()
            -1"""
    @overload
    def sign(self) -> Any:
        """NumberFieldElement_quadratic.sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 964)

        Return the sign of ``self`` (`0` if zero, `+1` if positive, and `-1` if
        negative).

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2, name='sqrt2')
            sage: K(0).sign()
            0
            sage: sqrt2.sign()
            1
            sage: (sqrt2+1).sign()
            1
            sage: (sqrt2-1).sign()
            1
            sage: (sqrt2-2).sign()
            -1
            sage: (-sqrt2).sign()
            -1
            sage: (-sqrt2+1).sign()
            -1
            sage: (-sqrt2+2).sign()
            1

            sage: K.<a> = QuadraticField(2, embedding=-1.4142)
            sage: K(0).sign()
            0
            sage: a.sign()
            -1
            sage: (a+1).sign()
            -1
            sage: (a+2).sign()
            1
            sage: (a-1).sign()
            -1
            sage: (-a).sign()
            1
            sage: (-a-1).sign()
            1
            sage: (-a-2).sign()
            -1

            sage: # needs sage.symbolic
            sage: x = polygen(ZZ, 'x')
            sage: K.<b> = NumberField(x^2 + 2*x + 7, 'b', embedding=CC(-1,-sqrt(6)))
            sage: b.sign()
            Traceback (most recent call last):
            ...
            ValueError: a complex number has no sign!
            sage: K(1).sign()
            1
            sage: K(0).sign()
            0
            sage: K(-2/3).sign()
            -1"""
    @overload
    def sign(self) -> Any:
        """NumberFieldElement_quadratic.sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 964)

        Return the sign of ``self`` (`0` if zero, `+1` if positive, and `-1` if
        negative).

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2, name='sqrt2')
            sage: K(0).sign()
            0
            sage: sqrt2.sign()
            1
            sage: (sqrt2+1).sign()
            1
            sage: (sqrt2-1).sign()
            1
            sage: (sqrt2-2).sign()
            -1
            sage: (-sqrt2).sign()
            -1
            sage: (-sqrt2+1).sign()
            -1
            sage: (-sqrt2+2).sign()
            1

            sage: K.<a> = QuadraticField(2, embedding=-1.4142)
            sage: K(0).sign()
            0
            sage: a.sign()
            -1
            sage: (a+1).sign()
            -1
            sage: (a+2).sign()
            1
            sage: (a-1).sign()
            -1
            sage: (-a).sign()
            1
            sage: (-a-1).sign()
            1
            sage: (-a-2).sign()
            -1

            sage: # needs sage.symbolic
            sage: x = polygen(ZZ, 'x')
            sage: K.<b> = NumberField(x^2 + 2*x + 7, 'b', embedding=CC(-1,-sqrt(6)))
            sage: b.sign()
            Traceback (most recent call last):
            ...
            ValueError: a complex number has no sign!
            sage: K(1).sign()
            1
            sage: K(0).sign()
            0
            sage: K(-2/3).sign()
            -1"""
    @overload
    def sign(self) -> Any:
        """NumberFieldElement_quadratic.sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 964)

        Return the sign of ``self`` (`0` if zero, `+1` if positive, and `-1` if
        negative).

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2, name='sqrt2')
            sage: K(0).sign()
            0
            sage: sqrt2.sign()
            1
            sage: (sqrt2+1).sign()
            1
            sage: (sqrt2-1).sign()
            1
            sage: (sqrt2-2).sign()
            -1
            sage: (-sqrt2).sign()
            -1
            sage: (-sqrt2+1).sign()
            -1
            sage: (-sqrt2+2).sign()
            1

            sage: K.<a> = QuadraticField(2, embedding=-1.4142)
            sage: K(0).sign()
            0
            sage: a.sign()
            -1
            sage: (a+1).sign()
            -1
            sage: (a+2).sign()
            1
            sage: (a-1).sign()
            -1
            sage: (-a).sign()
            1
            sage: (-a-1).sign()
            1
            sage: (-a-2).sign()
            -1

            sage: # needs sage.symbolic
            sage: x = polygen(ZZ, 'x')
            sage: K.<b> = NumberField(x^2 + 2*x + 7, 'b', embedding=CC(-1,-sqrt(6)))
            sage: b.sign()
            Traceback (most recent call last):
            ...
            ValueError: a complex number has no sign!
            sage: K(1).sign()
            1
            sage: K(0).sign()
            0
            sage: K(-2/3).sign()
            -1"""
    @overload
    def trace(self) -> Any:
        """NumberFieldElement_quadratic.trace(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2019)

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + x + 41)
            sage: a.trace()
            -1
            sage: a.matrix()
            [  0   1]
            [-41  -1]

        The trace is additive::

            sage: K.<a> = NumberField(x^2 + 7)
            sage: (a + 1).trace()
            2
            sage: K(3).trace()
            6
            sage: (a + 4).trace()
            8
            sage: (a/3 + 1).trace()
            2"""
    @overload
    def trace(self) -> Any:
        """NumberFieldElement_quadratic.trace(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2019)

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + x + 41)
            sage: a.trace()
            -1
            sage: a.matrix()
            [  0   1]
            [-41  -1]

        The trace is additive::

            sage: K.<a> = NumberField(x^2 + 7)
            sage: (a + 1).trace()
            2
            sage: K(3).trace()
            6
            sage: (a + 4).trace()
            8
            sage: (a/3 + 1).trace()
            2"""
    @overload
    def trace(self) -> Any:
        """NumberFieldElement_quadratic.trace(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2019)

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + x + 41)
            sage: a.trace()
            -1
            sage: a.matrix()
            [  0   1]
            [-41  -1]

        The trace is additive::

            sage: K.<a> = NumberField(x^2 + 7)
            sage: (a + 1).trace()
            2
            sage: K(3).trace()
            6
            sage: (a + 4).trace()
            8
            sage: (a/3 + 1).trace()
            2"""
    @overload
    def trace(self) -> Any:
        """NumberFieldElement_quadratic.trace(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2019)

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + x + 41)
            sage: a.trace()
            -1
            sage: a.matrix()
            [  0   1]
            [-41  -1]

        The trace is additive::

            sage: K.<a> = NumberField(x^2 + 7)
            sage: (a + 1).trace()
            2
            sage: K(3).trace()
            6
            sage: (a + 4).trace()
            8
            sage: (a/3 + 1).trace()
            2"""
    @overload
    def trace(self) -> Any:
        """NumberFieldElement_quadratic.trace(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2019)

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + x + 41)
            sage: a.trace()
            -1
            sage: a.matrix()
            [  0   1]
            [-41  -1]

        The trace is additive::

            sage: K.<a> = NumberField(x^2 + 7)
            sage: (a + 1).trace()
            2
            sage: K(3).trace()
            6
            sage: (a + 4).trace()
            8
            sage: (a/3 + 1).trace()
            2"""
    @overload
    def trace(self) -> Any:
        """NumberFieldElement_quadratic.trace(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2019)

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + x + 41)
            sage: a.trace()
            -1
            sage: a.matrix()
            [  0   1]
            [-41  -1]

        The trace is additive::

            sage: K.<a> = NumberField(x^2 + 7)
            sage: (a + 1).trace()
            2
            sage: K(3).trace()
            6
            sage: (a + 4).trace()
            8
            sage: (a/3 + 1).trace()
            2"""
    def __abs__(self) -> Any:
        """NumberFieldElement_quadratic.__abs__(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2257)

        EXAMPLES::

            sage: K.<a> = QuadraticField(2, 'a', embedding=-1.4142)
            sage: abs(a)    # indirect test
            -a
            sage: abs(a+1)  # indirect test
            -a - 1
            sage: abs(a+2)  # indirect test
            a + 2

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + 1, embedding=CDF.gen())
            sage: abs(a+1)                                                              # needs sage.symbolic
            sqrt(2)"""
    def __bool__(self) -> bool:
        """True if self else False"""
    @overload
    def __copy__(self) -> Any:
        """NumberFieldElement_quadratic.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 374)

        TESTS::

            sage: K.<a> = QuadraticField(-3)
            sage: b = a + 3
            sage: c = b.__copy__()
            sage: b is c
            True"""
    @overload
    def __copy__(self) -> Any:
        """NumberFieldElement_quadratic.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 374)

        TESTS::

            sage: K.<a> = QuadraticField(-3)
            sage: b = a + 3
            sage: c = b.__copy__()
            sage: b is c
            True"""
    def __deepcopy__(self, memo) -> Any:
        """NumberFieldElement_quadratic.__deepcopy__(self, memo)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 387)

        TESTS::

            sage: K.<a> = QuadraticField(-3)
            sage: b = a + 3
            sage: c = deepcopy(b)
            sage: b is c
            True"""
    def __hash__(self) -> Any:
        """NumberFieldElement_quadratic.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1663)

        Return hash of this number field element.

        For elements in `\\ZZ` or `\\QQ` the hash coincides with the one in the
        native `\\ZZ` or `\\QQ`.

        EXAMPLES::

            sage: L.<a> = QuadraticField(-7)
            sage: hash(a)
            42082631
            sage: hash(L(1))
            1
            sage: hash(L(-3))
            -3
            sage: hash(L(-32/118)) == hash(-32/118)
            True"""
    def __invert__(self) -> Any:
        """NumberFieldElement_quadratic.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1563)

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - 5)
            sage: ~a
            1/5*a
            sage: ~(a+1)
            1/4*a - 1/4
            sage: (a-1)*(a+1)
            4
            sage: b = ~(5*a-3); b
            5/116*a + 3/116
            sage: b*(5*a-3)
            1
            sage: b = ~((3*a-2)/7); b
            21/41*a + 14/41
            sage: (3*a-2)/7 * b
            1

        This fixes issue :issue:`9357`::

            sage: K.<a> = NumberField(x^2+1)
            sage: d = K(0)
            sage: ~d
            Traceback (most recent call last):
            ...
            ZeroDivisionError: number field element division by zero
            sage: K.random_element() / d
            Traceback (most recent call last):
            ...
            ZeroDivisionError: number field element division by zero"""
    def __neg__(self) -> Any:
        """NumberFieldElement_quadratic.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 1442)

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + 163)
            sage: -a
            -a
            sage: -(a+4)
            -a - 4
            sage: b = (a-3)/2
            sage: -b
            -1/2*a + 3/2"""
    def __reduce__(self) -> Any:
        """NumberFieldElement_quadratic.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 418)

        Used for pickling.

        TESTS::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - 13)
            sage: loads(dumps(a)) == a
            True
            sage: loads(dumps(a/3+5)) == a/3+5
            True"""

class NumberFieldElement_quadratic_sqrt(NumberFieldElement_quadratic):
    """File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2430)

        A :class:`NumberFieldElement_quadratic_sqrt` object gives an efficient representation of
        an element of a quadratic extension of `\\QQ` for the case when
        :func:`is_sqrt_disc()` is ``True``.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def denominator(self) -> Any:
        """NumberFieldElement_quadratic_sqrt.denominator(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2436)

        Return the denominator of ``self``.

        This is the LCM of the denominators of the coefficients of ``self``, and
        thus it may well be `> 1` even when the element is an algebraic integer.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + x + 41)
            sage: a.denominator()
            1
            sage: b = (2*a+1)/6
            sage: b.denominator()
            6
            sage: K(1).denominator()
            1
            sage: K(1/2).denominator()
            2
            sage: K(0).denominator()
            1

            sage: K.<a> = NumberField(x^2 - 5)
            sage: b = (a + 1)/2
            sage: b.denominator()
            2
            sage: b.is_integral()
            True"""
    @overload
    def denominator(self) -> Any:
        """NumberFieldElement_quadratic_sqrt.denominator(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2436)

        Return the denominator of ``self``.

        This is the LCM of the denominators of the coefficients of ``self``, and
        thus it may well be `> 1` even when the element is an algebraic integer.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + x + 41)
            sage: a.denominator()
            1
            sage: b = (2*a+1)/6
            sage: b.denominator()
            6
            sage: K(1).denominator()
            1
            sage: K(1/2).denominator()
            2
            sage: K(0).denominator()
            1

            sage: K.<a> = NumberField(x^2 - 5)
            sage: b = (a + 1)/2
            sage: b.denominator()
            2
            sage: b.is_integral()
            True"""
    @overload
    def denominator(self) -> Any:
        """NumberFieldElement_quadratic_sqrt.denominator(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2436)

        Return the denominator of ``self``.

        This is the LCM of the denominators of the coefficients of ``self``, and
        thus it may well be `> 1` even when the element is an algebraic integer.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + x + 41)
            sage: a.denominator()
            1
            sage: b = (2*a+1)/6
            sage: b.denominator()
            6
            sage: K(1).denominator()
            1
            sage: K(1/2).denominator()
            2
            sage: K(0).denominator()
            1

            sage: K.<a> = NumberField(x^2 - 5)
            sage: b = (a + 1)/2
            sage: b.denominator()
            2
            sage: b.is_integral()
            True"""
    @overload
    def denominator(self) -> Any:
        """NumberFieldElement_quadratic_sqrt.denominator(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2436)

        Return the denominator of ``self``.

        This is the LCM of the denominators of the coefficients of ``self``, and
        thus it may well be `> 1` even when the element is an algebraic integer.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + x + 41)
            sage: a.denominator()
            1
            sage: b = (2*a+1)/6
            sage: b.denominator()
            6
            sage: K(1).denominator()
            1
            sage: K(1/2).denominator()
            2
            sage: K(0).denominator()
            1

            sage: K.<a> = NumberField(x^2 - 5)
            sage: b = (a + 1)/2
            sage: b.denominator()
            2
            sage: b.is_integral()
            True"""
    @overload
    def denominator(self) -> Any:
        """NumberFieldElement_quadratic_sqrt.denominator(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2436)

        Return the denominator of ``self``.

        This is the LCM of the denominators of the coefficients of ``self``, and
        thus it may well be `> 1` even when the element is an algebraic integer.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + x + 41)
            sage: a.denominator()
            1
            sage: b = (2*a+1)/6
            sage: b.denominator()
            6
            sage: K(1).denominator()
            1
            sage: K(1/2).denominator()
            2
            sage: K(0).denominator()
            1

            sage: K.<a> = NumberField(x^2 - 5)
            sage: b = (a + 1)/2
            sage: b.denominator()
            2
            sage: b.is_integral()
            True"""
    @overload
    def denominator(self) -> Any:
        """NumberFieldElement_quadratic_sqrt.denominator(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2436)

        Return the denominator of ``self``.

        This is the LCM of the denominators of the coefficients of ``self``, and
        thus it may well be `> 1` even when the element is an algebraic integer.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + x + 41)
            sage: a.denominator()
            1
            sage: b = (2*a+1)/6
            sage: b.denominator()
            6
            sage: K(1).denominator()
            1
            sage: K(1/2).denominator()
            2
            sage: K(0).denominator()
            1

            sage: K.<a> = NumberField(x^2 - 5)
            sage: b = (a + 1)/2
            sage: b.denominator()
            2
            sage: b.is_integral()
            True"""
    @overload
    def denominator(self) -> Any:
        """NumberFieldElement_quadratic_sqrt.denominator(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2436)

        Return the denominator of ``self``.

        This is the LCM of the denominators of the coefficients of ``self``, and
        thus it may well be `> 1` even when the element is an algebraic integer.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + x + 41)
            sage: a.denominator()
            1
            sage: b = (2*a+1)/6
            sage: b.denominator()
            6
            sage: K(1).denominator()
            1
            sage: K(1/2).denominator()
            2
            sage: K(0).denominator()
            1

            sage: K.<a> = NumberField(x^2 - 5)
            sage: b = (a + 1)/2
            sage: b.denominator()
            2
            sage: b.is_integral()
            True"""
    def __getitem__(self, n) -> Any:
        """NumberFieldElement_quadratic_sqrt.__getitem__(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2491)

        Return the ``n``-th coefficient of this number field element,
        written as a polynomial in the generator.

        Note that ``n`` must be either ``0`` or ``1``.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - 13)
            sage: elt = a/4 + 1/3
            sage: elt[0]
            1/3
            sage: elt[1]
            1/4

            sage: K.zero()[0]
            0
            sage: K.zero()[1]
            0

            sage: K.one()[0]
            1
            sage: K.one()[1]
            0

            sage: elt[2]
            Traceback (most recent call last):
            ...
            IndexError: index must be either 0 or 1

            sage: C.<z3> = CyclotomicField(3)
            sage: list(z3)
            [0, 1]"""

class OrderElement_quadratic(NumberFieldElement_quadratic):
    """OrderElement_quadratic(order, f)

    File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2677)

    Element of an order in a quadratic field.

    EXAMPLES::

        sage: x = polygen(ZZ, 'x')
        sage: K.<a> = NumberField(x^2 + 1)
        sage: O2 = K.order(2*a)
        sage: w = O2.1; w
        2*a
        sage: parent(w)
        Order of conductor 2 generated by 2*a in Number Field in a with defining polynomial x^2 + 1"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, order, f) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2691)

                Standard initialisation function.

                EXAMPLES::

                    sage: x = polygen(ZZ, 'x')
                    sage: OK.<y> = EquationOrder(x^2 + 5)
                    sage: v = OK.1 # indirect doctest
                    sage: type(v)
                    <class 'sage.rings.number_field.number_field_element_quadratic.OrderElement_quadratic'>
        """
    def charpoly(self, var=..., algorithm=...) -> Any:
        """OrderElement_quadratic.charpoly(self, var='x', algorithm=None)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2742)

        The characteristic polynomial of this element, which is over `\\ZZ`
        because this element is an algebraic integer.

        INPUT:

        - ``var`` -- the minimal polynomial is defined over a polynomial ring
          in a variable with this name; if not specified, this defaults to ``'x'``
        - ``algorithm`` -- for compatibility with general number field
          elements; ignored

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - 5)
            sage: R = K.ring_of_integers()
            sage: b = R((5+a)/2)
            sage: f = b.charpoly('x'); f
            x^2 - 5*x + 5
            sage: f.parent()
            Univariate Polynomial Ring in x over Integer Ring
            sage: f(b)
            0"""
    @overload
    def denominator(self) -> Any:
        """OrderElement_quadratic.denominator(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2920)

        Return the denominator of ``self``.

        This is the LCM of the denominators of the coefficients of ``self``, and
        thus it may well be `> 1` even when the element is an algebraic integer.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - 27)
            sage: R = K.ring_of_integers()
            sage: aa = R.gen(1)
            sage: aa.denominator()
            3"""
    @overload
    def denominator(self) -> Any:
        """OrderElement_quadratic.denominator(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2920)

        Return the denominator of ``self``.

        This is the LCM of the denominators of the coefficients of ``self``, and
        thus it may well be `> 1` even when the element is an algebraic integer.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - 27)
            sage: R = K.ring_of_integers()
            sage: aa = R.gen(1)
            sage: aa.denominator()
            3"""
    def inverse_mod(self, I) -> Any:
        """OrderElement_quadratic.inverse_mod(self, I)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2866)

        Return an inverse of ``self`` modulo the given ideal.

        INPUT:

        - ``I`` -- may be an ideal of ``self.parent()``, or an
          element or list of elements of ``self.parent()`` generating a nonzero
          ideal. A :exc:`ValueError` is raised if `I` is non-integral or is zero.
          A :exc:`ZeroDivisionError` is raised if `I + (x) \\neq (1)`.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: OE.<w> = EquationOrder(x^2 - x + 2)
            sage: w.inverse_mod(13) == 6*w - 6
            True
            sage: w*(6*w - 6) - 1
            -13
            sage: w.inverse_mod(13).parent() == OE
            True
            sage: w.inverse_mod(2)
            Traceback (most recent call last):
            ...
            ZeroDivisionError: w is not invertible modulo Fractional ideal (2)"""
    def minpoly(self, var=..., algorithm=...) -> Any:
        """OrderElement_quadratic.minpoly(self, var='x', algorithm=None)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2770)

        The minimal polynomial of this element over `\\ZZ`.

        INPUT:

        - ``var`` -- the minimal polynomial is defined over a polynomial ring
          in a variable with this name; if not specified, this defaults to ``'x'``
        - ``algorithm`` -- for compatibility with general number field
          elements; ignored

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + 163)
            sage: R = K.ring_of_integers()
            sage: f = R(a).minpoly('x'); f
            x^2 + 163
            sage: f.parent()
            Univariate Polynomial Ring in x over Integer Ring
            sage: R(5).minpoly()
            x - 5"""
    @overload
    def norm(self) -> Any:
        """OrderElement_quadratic.norm(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2707)

        The norm of an element of the ring of integers is an Integer.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + 3)
            sage: O2 = K.order(2*a)
            sage: w = O2.gen(1); w
            2*a
            sage: w.norm()
            12
            sage: parent(w.norm())
            Integer Ring"""
    @overload
    def norm(self) -> Any:
        """OrderElement_quadratic.norm(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2707)

        The norm of an element of the ring of integers is an Integer.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + 3)
            sage: O2 = K.order(2*a)
            sage: w = O2.gen(1); w
            2*a
            sage: w.norm()
            12
            sage: parent(w.norm())
            Integer Ring"""
    @overload
    def norm(self) -> Any:
        """OrderElement_quadratic.norm(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2707)

        The norm of an element of the ring of integers is an Integer.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + 3)
            sage: O2 = K.order(2*a)
            sage: w = O2.gen(1); w
            2*a
            sage: w.norm()
            12
            sage: parent(w.norm())
            Integer Ring"""
    @overload
    def trace(self) -> Any:
        """OrderElement_quadratic.trace(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2725)

        The trace of an element of the ring of integers is an Integer.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - 5)
            sage: R = K.ring_of_integers()
            sage: b = R((1+a)/2)
            sage: b.trace()
            1
            sage: parent(b.trace())
            Integer Ring"""
    @overload
    def trace(self) -> Any:
        """OrderElement_quadratic.trace(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2725)

        The trace of an element of the ring of integers is an Integer.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - 5)
            sage: R = K.ring_of_integers()
            sage: b = R((1+a)/2)
            sage: b.trace()
            1
            sage: parent(b.trace())
            Integer Ring"""
    @overload
    def trace(self) -> Any:
        """OrderElement_quadratic.trace(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2725)

        The trace of an element of the ring of integers is an Integer.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - 5)
            sage: R = K.ring_of_integers()
            sage: b = R((1+a)/2)
            sage: b.trace()
            1
            sage: parent(b.trace())
            Integer Ring"""
    def __invert__(self) -> Any:
        """OrderElement_quadratic.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2846)

        Implement inversion, checking that the return value has the right parent.
        See :issue:`4190`.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K = NumberField(x^2 - x + 2, 'a')
            sage: OK = K.ring_of_integers()
            sage: a = OK(K.gen())
            sage: (~a).parent() is K
            True
            sage: (~a) in OK
            False
            sage: a**(-1) in OK
            False"""

class Q_to_quadratic_field_element(sage.categories.morphism.Morphism):
    """Q_to_quadratic_field_element(K)

    File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 3057)

    Morphism that coerces from rationals to elements of a quadratic number
    field `K`.

    EXAMPLES::

        sage: K.<a> = QuadraticField(-3)
        sage: f = K.coerce_map_from(QQ); f
        Natural morphism:
          From: Rational Field
          To:   Number Field in a with defining polynomial x^2 + 3 with a = 1.732050807568878?*I
        sage: f(3/1)
        3
        sage: f(1/2).parent() is K
        True"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, K) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 3079)

                INPUT:

                - ``K`` -- the target quadratic field

                EXAMPLES::

                    sage: K.<a> = QuadraticField(3)
                    sage: phi = K.coerce_map_from(QQ) # indirect doctest
                    sage: type(phi)
                    <class 'sage.rings.number_field.number_field_element_quadratic.Q_to_quadratic_field_element'>
                    sage: phi == loads(dumps(phi))  # todo: comparison not implemented
                    True

                    sage: R.<b> = CyclotomicField(6)
                    sage: psi = R.coerce_map_from(QQ)
                    sage: type(psi)
                    <class 'sage.rings.number_field.number_field_element_quadratic.Q_to_quadratic_field_element'>
                    sage: psi == loads(dumps(psi))  # todo: comparison not implemented
                    True
        """

class Z_to_quadratic_field_element(sage.categories.morphism.Morphism):
    """Z_to_quadratic_field_element(K)

    File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2955)

    Morphism that coerces from integers to elements of a quadratic number
    field `K`.

    EXAMPLES::

        sage: K.<a> = QuadraticField(3)
        sage: phi = K.coerce_map_from(ZZ); phi
        Natural morphism:
          From: Integer Ring
          To:   Number Field in a with defining polynomial x^2 - 3 with a = 1.732050807568878?
        sage: phi(4)
        4
        sage: phi(5).parent() is K
        True"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, K) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2977)

                ``K`` is the target quadratic field.

                EXAMPLES::

                    sage: K.<a> = QuadraticField(3)
                    sage: phi = K.coerce_map_from(ZZ) # indirect doctest
                    sage: type(phi)
                    <class 'sage.rings.number_field.number_field_element_quadratic.Z_to_quadratic_field_element'>
                    sage: phi == loads(dumps(phi)) # todo: comparison not implemented
                    True

                    sage: R.<b> = CyclotomicField(6)
                    sage: psi = R.coerce_map_from(ZZ) # indirect doctest
                    sage: type(psi)
                    <class 'sage.rings.number_field.number_field_element_quadratic.Z_to_quadratic_field_element'>
                    sage: psi == loads(dumps(psi)) # todo: comparison not implemented
                    True
        """

I: NumberFieldElement_quadratic
r"""File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element_quadratic.pyx (starting at line 2532)

    An element of `\QQ[i]`.

    Some methods of this class behave slightly differently than the
    corresponding methods of general elements of quadratic number fields,
    especially with regard to conversions to parents that can represent complex
    numbers in rectangular form.

    In addition, this class provides some convenience methods similar to methods
    of symbolic expressions to make the behavior of ``a + I*b`` with rational
    ``a``, ``b`` closer to that when ``a``, ``b`` are expressions.

    EXAMPLES::

        sage: type(I)
        <class 'sage.rings.number_field.number_field_element_quadratic.NumberFieldElement_gaussian'>

        sage: mi = QuadraticField(-1, embedding=CC(0,-1)).gen()
        sage: type(mi)
        <class 'sage.rings.number_field.number_field_element_quadratic.NumberFieldElement_gaussian'>
        sage: CC(mi)
        -1.00000000000000*I
"""