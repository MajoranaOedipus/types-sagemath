import sage.rings.function_field.element
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

class FunctionFieldElement_polymod(sage.rings.function_field.element.FunctionFieldElement):
    """FunctionFieldElement_polymod(parent, x, reduce=True)

    File: /build/sagemath/src/sage/src/sage/rings/function_field/element_polymod.pyx (starting at line 30)

    Elements of a finite extension of a function field.

    EXAMPLES::

        sage: K.<x> = FunctionField(QQ); R.<y> = K[]
        sage: L.<y> = K.extension(y^2 - x*y + 4*x^3)
        sage: x*y + 1/x^3
        x*y + 1/x^3"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, x, reduce=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/function_field/element_polymod.pyx (starting at line 41)

                Initialize.

                EXAMPLES::

                    sage: K.<x> = FunctionField(QQ); R.<y> = K[]
                    sage: L.<y> = K.extension(y^2 - x*y + 4*x^3)
                    sage: TestSuite(x*y + 1/x^3).run()
        """
    @overload
    def element(self) -> Any:
        """FunctionFieldElement_polymod.element(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element_polymod.pyx (starting at line 57)

        Return the underlying polynomial that represents the element.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ); R.<T> = K[]
            sage: L.<y> = K.extension(T^2 - x*T + 4*x^3)
            sage: f = y/x^2 + x/(x^2+1); f
            1/x^2*y + x/(x^2 + 1)
            sage: f.element()
            1/x^2*y + x/(x^2 + 1)"""
    @overload
    def element(self) -> Any:
        """FunctionFieldElement_polymod.element(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element_polymod.pyx (starting at line 57)

        Return the underlying polynomial that represents the element.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ); R.<T> = K[]
            sage: L.<y> = K.extension(T^2 - x*T + 4*x^3)
            sage: f = y/x^2 + x/(x^2+1); f
            1/x^2*y + x/(x^2 + 1)
            sage: f.element()
            1/x^2*y + x/(x^2 + 1)"""
    def is_nth_power(self, n) -> bool:
        """FunctionFieldElement_polymod.is_nth_power(self, n) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element_polymod.pyx (starting at line 319)

        Return whether this element is an ``n``-th power in the function field.

        INPUT:

        - ``n`` -- integer

        ALGORITHM:

        If ``n`` is a power of the characteristic of the field and the constant
        base field is perfect, then this uses the algorithm described in
        Proposition 12 of [GiTr1996]_.

        .. SEEALSO::

            :meth:`nth_root`

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(4))
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x)
            sage: y.is_nth_power(2)
            False
            sage: L(x).is_nth_power(2)
            True"""
    @overload
    def list(self) -> list:
        """FunctionFieldElement_polymod.list(self) -> list

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element_polymod.pyx (starting at line 234)

        Return the list of the coefficients representing the element.

        If the function field is `K[y]/(f(y))`, then return the coefficients of
        the reduced presentation of the element as a polynomial in `K[y]`.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3)
            sage: a = ~(2*y + 1/x); a
            (-1/8*x^2/(x^5 + 1/8*x^2 + 1/16))*y + (1/8*x^3 + 1/16*x)/(x^5 + 1/8*x^2 + 1/16)
            sage: a.list()
            [(1/8*x^3 + 1/16*x)/(x^5 + 1/8*x^2 + 1/16), -1/8*x^2/(x^5 + 1/8*x^2 + 1/16)]
            sage: (x*y).list()
            [0, x]"""
    @overload
    def list(self) -> Any:
        """FunctionFieldElement_polymod.list(self) -> list

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element_polymod.pyx (starting at line 234)

        Return the list of the coefficients representing the element.

        If the function field is `K[y]/(f(y))`, then return the coefficients of
        the reduced presentation of the element as a polynomial in `K[y]`.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3)
            sage: a = ~(2*y + 1/x); a
            (-1/8*x^2/(x^5 + 1/8*x^2 + 1/16))*y + (1/8*x^3 + 1/16*x)/(x^5 + 1/8*x^2 + 1/16)
            sage: a.list()
            [(1/8*x^3 + 1/16*x)/(x^5 + 1/8*x^2 + 1/16), -1/8*x^2/(x^5 + 1/8*x^2 + 1/16)]
            sage: (x*y).list()
            [0, x]"""
    @overload
    def list(self) -> Any:
        """FunctionFieldElement_polymod.list(self) -> list

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element_polymod.pyx (starting at line 234)

        Return the list of the coefficients representing the element.

        If the function field is `K[y]/(f(y))`, then return the coefficients of
        the reduced presentation of the element as a polynomial in `K[y]`.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3)
            sage: a = ~(2*y + 1/x); a
            (-1/8*x^2/(x^5 + 1/8*x^2 + 1/16))*y + (1/8*x^3 + 1/16*x)/(x^5 + 1/8*x^2 + 1/16)
            sage: a.list()
            [(1/8*x^3 + 1/16*x)/(x^5 + 1/8*x^2 + 1/16), -1/8*x^2/(x^5 + 1/8*x^2 + 1/16)]
            sage: (x*y).list()
            [0, x]"""
    def nth_root(self, n) -> FunctionFieldElement:
        """FunctionFieldElement_polymod.nth_root(self, n) -> FunctionFieldElement

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element_polymod.pyx (starting at line 254)

        Return an ``n``-th root of this element in the function field.

        INPUT:

        - ``n`` -- integer

        OUTPUT:

        Returns an element ``a`` in the function field such that this element
        equals `a^n`. Raises an error if no such element exists.

        ALGORITHM:

        If ``n`` is a power of the characteristic of the field and the constant
        base field is perfect, then this uses the algorithm described in
        Proposition 12 of [GiTr1996]_.

        .. SEEALSO::

            :meth:`is_nth_power`

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(3))
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x)
            sage: L(y^3).nth_root(3)
            y
            sage: L(y^9).nth_root(-9)
            1/x*y

        This also works for inseparable extensions::

            sage: K.<x> = FunctionField(GF(3))
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - x^2)
            sage: L(x).nth_root(3)^3
            x
            sage: L(x^9).nth_root(-27)^-27
            x^9"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __hash__(self) -> Any:
        """FunctionFieldElement_polymod.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element_polymod.pyx (starting at line 102)

        Return the hash of the element.

        TESTS::

            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3)
            sage: len({hash(y^i+x^j) for i in [-2..2] for j in [-2..2]}) >= 24
            True"""
    def __invert__(self) -> Any:
        """FunctionFieldElement_polymod.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/element_polymod.pyx (starting at line 216)

        Return the multiplicative inverse of the element.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3)
            sage: a = ~(2*y + 1/x); a                           # indirect doctest
            (-1/8*x^2/(x^5 + 1/8*x^2 + 1/16))*y + (1/8*x^3 + 1/16*x)/(x^5 + 1/8*x^2 + 1/16)
            sage: a*(2*y + 1/x)
            1"""
