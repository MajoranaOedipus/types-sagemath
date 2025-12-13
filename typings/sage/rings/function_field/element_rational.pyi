import sage.rings.function_field.element
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

class FunctionFieldElement_rational(sage.rings.function_field.element.FunctionFieldElement):
    """FunctionFieldElement_rational(parent, x, reduce=True)

    File: /build/sagemath/src/sage/src/sage/rings/function_field/element_rational.pyx (starting at line 29)

    Elements of a rational function field.

    EXAMPLES::

        sage: K.<t> = FunctionField(QQ); K
        Rational function field in t over Rational Field
        sage: t^2 + 3/2*t
        t^2 + 3/2*t
        sage: FunctionField(QQ,'t').gen()^3
        t^3"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, x, reduce=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/function_field/element_rational.pyx (starting at line 42)

                Initialize.

                EXAMPLES::

                    sage: K.<t> = FunctionField(QQ)
                    sage: x = t^3
                    sage: TestSuite(x).run()
        """
    @overload
    def denominator(self) -> Any:
        """FunctionFieldElement_rational.denominator(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element_rational.pyx (starting at line 264)

        Return the denominator of the rational function.

        EXAMPLES::

            sage: K.<t> = FunctionField(QQ)
            sage: f = (t+1) / (t^2 - 1/3); f
            (t + 1)/(t^2 - 1/3)
            sage: f.denominator()
            t^2 - 1/3"""
    @overload
    def denominator(self) -> Any:
        """FunctionFieldElement_rational.denominator(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element_rational.pyx (starting at line 264)

        Return the denominator of the rational function.

        EXAMPLES::

            sage: K.<t> = FunctionField(QQ)
            sage: f = (t+1) / (t^2 - 1/3); f
            (t + 1)/(t^2 - 1/3)
            sage: f.denominator()
            t^2 - 1/3"""
    @overload
    def element(self) -> Any:
        """FunctionFieldElement_rational.element(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element_rational.pyx (starting at line 67)

        Return the underlying fraction field element that represents the element.

        EXAMPLES::

            sage: K.<t> = FunctionField(GF(7))
            sage: t.element()
            t
            sage: type(t.element())                                                     # needs sage.libs.ntl
            <... 'sage.rings.fraction_field_FpT.FpTElement'>

            sage: # needs sage.rings.finite_rings
            sage: K.<t> = FunctionField(GF(131101))
            sage: t.element()
            t
            sage: type(t.element())
            <... 'sage.rings.fraction_field_element.FractionFieldElement_1poly_field'>"""
    @overload
    def element(self) -> Any:
        """FunctionFieldElement_rational.element(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element_rational.pyx (starting at line 67)

        Return the underlying fraction field element that represents the element.

        EXAMPLES::

            sage: K.<t> = FunctionField(GF(7))
            sage: t.element()
            t
            sage: type(t.element())                                                     # needs sage.libs.ntl
            <... 'sage.rings.fraction_field_FpT.FpTElement'>

            sage: # needs sage.rings.finite_rings
            sage: K.<t> = FunctionField(GF(131101))
            sage: t.element()
            t
            sage: type(t.element())
            <... 'sage.rings.fraction_field_element.FractionFieldElement_1poly_field'>"""
    @overload
    def element(self) -> Any:
        """FunctionFieldElement_rational.element(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element_rational.pyx (starting at line 67)

        Return the underlying fraction field element that represents the element.

        EXAMPLES::

            sage: K.<t> = FunctionField(GF(7))
            sage: t.element()
            t
            sage: type(t.element())                                                     # needs sage.libs.ntl
            <... 'sage.rings.fraction_field_FpT.FpTElement'>

            sage: # needs sage.rings.finite_rings
            sage: K.<t> = FunctionField(GF(131101))
            sage: t.element()
            t
            sage: type(t.element())
            <... 'sage.rings.fraction_field_element.FractionFieldElement_1poly_field'>"""
    @overload
    def element(self) -> Any:
        """FunctionFieldElement_rational.element(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element_rational.pyx (starting at line 67)

        Return the underlying fraction field element that represents the element.

        EXAMPLES::

            sage: K.<t> = FunctionField(GF(7))
            sage: t.element()
            t
            sage: type(t.element())                                                     # needs sage.libs.ntl
            <... 'sage.rings.fraction_field_FpT.FpTElement'>

            sage: # needs sage.rings.finite_rings
            sage: K.<t> = FunctionField(GF(131101))
            sage: t.element()
            t
            sage: type(t.element())
            <... 'sage.rings.fraction_field_element.FractionFieldElement_1poly_field'>"""
    @overload
    def element(self) -> Any:
        """FunctionFieldElement_rational.element(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element_rational.pyx (starting at line 67)

        Return the underlying fraction field element that represents the element.

        EXAMPLES::

            sage: K.<t> = FunctionField(GF(7))
            sage: t.element()
            t
            sage: type(t.element())                                                     # needs sage.libs.ntl
            <... 'sage.rings.fraction_field_FpT.FpTElement'>

            sage: # needs sage.rings.finite_rings
            sage: K.<t> = FunctionField(GF(131101))
            sage: t.element()
            t
            sage: type(t.element())
            <... 'sage.rings.fraction_field_element.FractionFieldElement_1poly_field'>"""
    @overload
    def factor(self) -> Any:
        """FunctionFieldElement_rational.factor(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element_rational.pyx (starting at line 471)

        Factor the rational function.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: K.<t> = FunctionField(QQ)
            sage: f = (t+1) / (t^2 - 1/3)
            sage: f.factor()
            (t + 1) * (t^2 - 1/3)^-1
            sage: (7*f).factor()
            (7) * (t + 1) * (t^2 - 1/3)^-1
            sage: ((7*f).factor()).unit()
            7
            sage: (f^3).factor()
            (t + 1)^3 * (t^2 - 1/3)^-3"""
    @overload
    def factor(self) -> Any:
        """FunctionFieldElement_rational.factor(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element_rational.pyx (starting at line 471)

        Factor the rational function.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: K.<t> = FunctionField(QQ)
            sage: f = (t+1) / (t^2 - 1/3)
            sage: f.factor()
            (t + 1) * (t^2 - 1/3)^-1
            sage: (7*f).factor()
            (7) * (t + 1) * (t^2 - 1/3)^-1
            sage: ((7*f).factor()).unit()
            7
            sage: (f^3).factor()
            (t + 1)^3 * (t^2 - 1/3)^-3"""
    @overload
    def factor(self) -> Any:
        """FunctionFieldElement_rational.factor(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element_rational.pyx (starting at line 471)

        Factor the rational function.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: K.<t> = FunctionField(QQ)
            sage: f = (t+1) / (t^2 - 1/3)
            sage: f.factor()
            (t + 1) * (t^2 - 1/3)^-1
            sage: (7*f).factor()
            (7) * (t + 1) * (t^2 - 1/3)^-1
            sage: ((7*f).factor()).unit()
            7
            sage: (f^3).factor()
            (t + 1)^3 * (t^2 - 1/3)^-3"""
    @overload
    def factor(self) -> Any:
        """FunctionFieldElement_rational.factor(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element_rational.pyx (starting at line 471)

        Factor the rational function.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: K.<t> = FunctionField(QQ)
            sage: f = (t+1) / (t^2 - 1/3)
            sage: f.factor()
            (t + 1) * (t^2 - 1/3)^-1
            sage: (7*f).factor()
            (7) * (t + 1) * (t^2 - 1/3)^-1
            sage: ((7*f).factor()).unit()
            7
            sage: (f^3).factor()
            (t + 1)^3 * (t^2 - 1/3)^-3"""
    @overload
    def factor(self) -> Any:
        """FunctionFieldElement_rational.factor(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element_rational.pyx (starting at line 471)

        Factor the rational function.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: K.<t> = FunctionField(QQ)
            sage: f = (t+1) / (t^2 - 1/3)
            sage: f.factor()
            (t + 1) * (t^2 - 1/3)^-1
            sage: (7*f).factor()
            (7) * (t + 1) * (t^2 - 1/3)^-1
            sage: ((7*f).factor()).unit()
            7
            sage: (f^3).factor()
            (t + 1)^3 * (t^2 - 1/3)^-3"""
    @overload
    def inverse_mod(self, I) -> Any:
        """FunctionFieldElement_rational.inverse_mod(self, I)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element_rational.pyx (starting at line 494)

        Return an inverse of the element modulo the integral ideal `I`, if `I`
        and the element together generate the unit ideal.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ)
            sage: O = K.maximal_order(); I = O.ideal(x^2 + 1)
            sage: t = O(x + 1).inverse_mod(I); t
            -1/2*x + 1/2
            sage: (t*(x+1) - 1) in I
            True"""
    @overload
    def inverse_mod(self, I) -> Any:
        """FunctionFieldElement_rational.inverse_mod(self, I)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element_rational.pyx (starting at line 494)

        Return an inverse of the element modulo the integral ideal `I`, if `I`
        and the element together generate the unit ideal.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ)
            sage: O = K.maximal_order(); I = O.ideal(x^2 + 1)
            sage: t = O(x + 1).inverse_mod(I); t
            -1/2*x + 1/2
            sage: (t*(x+1) - 1) in I
            True"""
    def is_nth_power(self, n) -> bool:
        """FunctionFieldElement_rational.is_nth_power(self, n) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element_rational.pyx (starting at line 362)

        Return whether this element is an ``n``-th power in the rational
        function field.

        INPUT:

        - ``n`` -- integer

        OUTPUT:

        Returns ``True`` if there is an element `a` in the function field such
        that this element equals `a^n`.

        ALGORITHM:

        If ``n`` is a power of the characteristic of the field and the constant
        base field is perfect, then this uses the algorithm described in Lemma
        3 of [GiTr1996]_.

        .. SEEALSO::

            :meth:`nth_root`

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(3))
            sage: f = (x+1)/(x-1)
            sage: f.is_nth_power(1)
            True
            sage: f.is_nth_power(3)                                                     # needs sage.modules
            False
            sage: (f^3).is_nth_power(3)                                                 # needs sage.modules
            True
            sage: (f^9).is_nth_power(-9)                                                # needs sage.modules
            True"""
    @overload
    def is_square(self) -> Any:
        """FunctionFieldElement_rational.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element_rational.pyx (starting at line 316)

        Return whether the element is a square.

        EXAMPLES::

            sage: K.<t> = FunctionField(QQ)
            sage: t.is_square()
            False
            sage: (t^2/4).is_square()
            True
            sage: f = 9 * (t+1)^6 / (t^2 - 2*t + 1); f.is_square()
            True

            sage: K.<t> = FunctionField(GF(5))
            sage: (-t^2).is_square()                                                    # needs sage.libs.pari
            True
            sage: (-t^2).sqrt()                                                         # needs sage.libs.pari
            2*t"""
    @overload
    def is_square(self) -> Any:
        """FunctionFieldElement_rational.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element_rational.pyx (starting at line 316)

        Return whether the element is a square.

        EXAMPLES::

            sage: K.<t> = FunctionField(QQ)
            sage: t.is_square()
            False
            sage: (t^2/4).is_square()
            True
            sage: f = 9 * (t+1)^6 / (t^2 - 2*t + 1); f.is_square()
            True

            sage: K.<t> = FunctionField(GF(5))
            sage: (-t^2).is_square()                                                    # needs sage.libs.pari
            True
            sage: (-t^2).sqrt()                                                         # needs sage.libs.pari
            2*t"""
    @overload
    def is_square(self) -> Any:
        """FunctionFieldElement_rational.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element_rational.pyx (starting at line 316)

        Return whether the element is a square.

        EXAMPLES::

            sage: K.<t> = FunctionField(QQ)
            sage: t.is_square()
            False
            sage: (t^2/4).is_square()
            True
            sage: f = 9 * (t+1)^6 / (t^2 - 2*t + 1); f.is_square()
            True

            sage: K.<t> = FunctionField(GF(5))
            sage: (-t^2).is_square()                                                    # needs sage.libs.pari
            True
            sage: (-t^2).sqrt()                                                         # needs sage.libs.pari
            2*t"""
    @overload
    def is_square(self) -> Any:
        """FunctionFieldElement_rational.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element_rational.pyx (starting at line 316)

        Return whether the element is a square.

        EXAMPLES::

            sage: K.<t> = FunctionField(QQ)
            sage: t.is_square()
            False
            sage: (t^2/4).is_square()
            True
            sage: f = 9 * (t+1)^6 / (t^2 - 2*t + 1); f.is_square()
            True

            sage: K.<t> = FunctionField(GF(5))
            sage: (-t^2).is_square()                                                    # needs sage.libs.pari
            True
            sage: (-t^2).sqrt()                                                         # needs sage.libs.pari
            2*t"""
    @overload
    def is_square(self) -> Any:
        """FunctionFieldElement_rational.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element_rational.pyx (starting at line 316)

        Return whether the element is a square.

        EXAMPLES::

            sage: K.<t> = FunctionField(QQ)
            sage: t.is_square()
            False
            sage: (t^2/4).is_square()
            True
            sage: f = 9 * (t+1)^6 / (t^2 - 2*t + 1); f.is_square()
            True

            sage: K.<t> = FunctionField(GF(5))
            sage: (-t^2).is_square()                                                    # needs sage.libs.pari
            True
            sage: (-t^2).sqrt()                                                         # needs sage.libs.pari
            2*t"""
    @overload
    def list(self) -> list:
        """FunctionFieldElement_rational.list(self) -> list

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element_rational.pyx (starting at line 88)

        Return a list with just the element.

        The list represents the element when the rational function field is
        viewed as a (one-dimensional) vector space over itself.

        EXAMPLES::

            sage: K.<t> = FunctionField(QQ)
            sage: t.list()
            [t]"""
    @overload
    def list(self) -> Any:
        """FunctionFieldElement_rational.list(self) -> list

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element_rational.pyx (starting at line 88)

        Return a list with just the element.

        The list represents the element when the rational function field is
        viewed as a (one-dimensional) vector space over itself.

        EXAMPLES::

            sage: K.<t> = FunctionField(QQ)
            sage: t.list()
            [t]"""
    def nth_root(self, n) -> FunctionFieldElement:
        """FunctionFieldElement_rational.nth_root(self, n) -> FunctionFieldElement

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element_rational.pyx (starting at line 415)

        Return an ``n``-th root of this element in the function field.

        INPUT:

        - ``n`` -- integer

        OUTPUT:

        Returns an element ``a`` in the rational function field such that this
        element equals `a^n`. Raises an error if no such element exists.

        ALGORITHM:

        If ``n`` is a power of the characteristic of the field and the constant
        base field is perfect, then this uses the algorithm described in
        Corollary 3 of [GiTr1996]_.

        .. SEEALSO::

            :meth:`is_nth_power`

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(3))
            sage: f = (x+1)/(x+2)
            sage: f.nth_root(1)
            (x + 1)/(x + 2)
            sage: f.nth_root(3)
            Traceback (most recent call last):
            ...
            ValueError: element is not an n-th power
            sage: (f^3).nth_root(3)                                                     # needs sage.modules
            (x + 1)/(x + 2)
            sage: (f^9).nth_root(-9)                                                    # needs sage.modules
            (x + 2)/(x + 1)"""
    @overload
    def numerator(self) -> Any:
        """FunctionFieldElement_rational.numerator(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element_rational.pyx (starting at line 250)

        Return the numerator of the rational function.

        EXAMPLES::

            sage: K.<t> = FunctionField(QQ)
            sage: f = (t+1) / (t^2 - 1/3); f
            (t + 1)/(t^2 - 1/3)
            sage: f.numerator()
            t + 1"""
    @overload
    def numerator(self) -> Any:
        """FunctionFieldElement_rational.numerator(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element_rational.pyx (starting at line 250)

        Return the numerator of the rational function.

        EXAMPLES::

            sage: K.<t> = FunctionField(QQ)
            sage: f = (t+1) / (t^2 - 1/3); f
            (t + 1)/(t^2 - 1/3)
            sage: f.numerator()
            t + 1"""
    @overload
    def sqrt(self, all=...) -> Any:
        """FunctionFieldElement_rational.sqrt(self, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element_rational.pyx (starting at line 338)

        Return the square root of the rational function.

        EXAMPLES::

            sage: K.<t> = FunctionField(QQ)
            sage: f = t^2 - 2 + 1/t^2; f.sqrt()
            (t^2 - 1)/t
            sage: f = t^2; f.sqrt(all=True)
            [t, -t]

        TESTS::

            sage: K(4/9).sqrt()
            2/3
            sage: K(0).sqrt(all=True)
            [0]"""
    @overload
    def sqrt(self) -> Any:
        """FunctionFieldElement_rational.sqrt(self, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element_rational.pyx (starting at line 338)

        Return the square root of the rational function.

        EXAMPLES::

            sage: K.<t> = FunctionField(QQ)
            sage: f = t^2 - 2 + 1/t^2; f.sqrt()
            (t^2 - 1)/t
            sage: f = t^2; f.sqrt(all=True)
            [t, -t]

        TESTS::

            sage: K(4/9).sqrt()
            2/3
            sage: K(0).sqrt(all=True)
            [0]"""
    @overload
    def sqrt(self, all=...) -> Any:
        """FunctionFieldElement_rational.sqrt(self, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element_rational.pyx (starting at line 338)

        Return the square root of the rational function.

        EXAMPLES::

            sage: K.<t> = FunctionField(QQ)
            sage: f = t^2 - 2 + 1/t^2; f.sqrt()
            (t^2 - 1)/t
            sage: f = t^2; f.sqrt(all=True)
            [t, -t]

        TESTS::

            sage: K(4/9).sqrt()
            2/3
            sage: K(0).sqrt(all=True)
            [0]"""
    @overload
    def sqrt(self) -> Any:
        """FunctionFieldElement_rational.sqrt(self, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element_rational.pyx (starting at line 338)

        Return the square root of the rational function.

        EXAMPLES::

            sage: K.<t> = FunctionField(QQ)
            sage: f = t^2 - 2 + 1/t^2; f.sqrt()
            (t^2 - 1)/t
            sage: f = t^2; f.sqrt(all=True)
            [t, -t]

        TESTS::

            sage: K(4/9).sqrt()
            2/3
            sage: K(0).sqrt(all=True)
            [0]"""
    @overload
    def sqrt(self, all=...) -> Any:
        """FunctionFieldElement_rational.sqrt(self, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element_rational.pyx (starting at line 338)

        Return the square root of the rational function.

        EXAMPLES::

            sage: K.<t> = FunctionField(QQ)
            sage: f = t^2 - 2 + 1/t^2; f.sqrt()
            (t^2 - 1)/t
            sage: f = t^2; f.sqrt(all=True)
            [t, -t]

        TESTS::

            sage: K(4/9).sqrt()
            2/3
            sage: K(0).sqrt(all=True)
            [0]"""
    @overload
    def valuation(self, place) -> Any:
        """FunctionFieldElement_rational.valuation(self, place)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element_rational.pyx (starting at line 278)

        Return the valuation of the rational function at the place.

        Rational function field places are associated with irreducible
        polynomials.

        INPUT:

        - ``place`` -- a place or an irreducible polynomial

        EXAMPLES::

            sage: K.<t> = FunctionField(QQ)
            sage: f = (t - 1)^2*(t + 1)/(t^2 - 1/3)^3
            sage: f.valuation(t - 1)
            2
            sage: f.valuation(t)
            0
            sage: f.valuation(t^2 - 1/3)
            -3

            sage: K.<x> = FunctionField(GF(2))
            sage: p = K.places_finite()[0]                                              # needs sage.libs.pari
            sage: (1/x^2).valuation(p)                                                  # needs sage.libs.pari
            -2"""
    @overload
    def valuation(self, t) -> Any:
        """FunctionFieldElement_rational.valuation(self, place)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element_rational.pyx (starting at line 278)

        Return the valuation of the rational function at the place.

        Rational function field places are associated with irreducible
        polynomials.

        INPUT:

        - ``place`` -- a place or an irreducible polynomial

        EXAMPLES::

            sage: K.<t> = FunctionField(QQ)
            sage: f = (t - 1)^2*(t + 1)/(t^2 - 1/3)^3
            sage: f.valuation(t - 1)
            2
            sage: f.valuation(t)
            0
            sage: f.valuation(t^2 - 1/3)
            -3

            sage: K.<x> = FunctionField(GF(2))
            sage: p = K.places_finite()[0]                                              # needs sage.libs.pari
            sage: (1/x^2).valuation(p)                                                  # needs sage.libs.pari
            -2"""
    @overload
    def valuation(self, p) -> Any:
        """FunctionFieldElement_rational.valuation(self, place)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element_rational.pyx (starting at line 278)

        Return the valuation of the rational function at the place.

        Rational function field places are associated with irreducible
        polynomials.

        INPUT:

        - ``place`` -- a place or an irreducible polynomial

        EXAMPLES::

            sage: K.<t> = FunctionField(QQ)
            sage: f = (t - 1)^2*(t + 1)/(t^2 - 1/3)^3
            sage: f.valuation(t - 1)
            2
            sage: f.valuation(t)
            0
            sage: f.valuation(t^2 - 1/3)
            -3

            sage: K.<x> = FunctionField(GF(2))
            sage: p = K.places_finite()[0]                                              # needs sage.libs.pari
            sage: (1/x^2).valuation(p)                                                  # needs sage.libs.pari
            -2"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __hash__(self) -> Any:
        """FunctionFieldElement_rational.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element_rational.pyx (starting at line 131)

        Return the hash of the element.

        TESTS:

        It would be nice if the following would produce a list of
        15 distinct hashes::

            sage: K.<t> = FunctionField(QQ)
            sage: len({hash(t^i+t^j) for i in [-2..2] for j in [i..2]}) >= 10
            True"""
    @overload
    def __pari__(self) -> Any:
        """FunctionFieldElement_rational.__pari__(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element_rational.pyx (starting at line 55)

        Coerce the element to PARI.

        EXAMPLES::

            sage: K.<a> = FunctionField(QQ)
            sage: ((a+1)/(a-1)).__pari__()                                              # needs sage.libs.pari
            (a + 1)/(a - 1)"""
    @overload
    def __pari__(self) -> Any:
        """FunctionFieldElement_rational.__pari__(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element_rational.pyx (starting at line 55)

        Coerce the element to PARI.

        EXAMPLES::

            sage: K.<a> = FunctionField(QQ)
            sage: ((a+1)/(a-1)).__pari__()                                              # needs sage.libs.pari
            (a + 1)/(a - 1)"""
