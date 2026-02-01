import _cython_3_2_1
import sage as sage
import sage.misc.latex as latex
import sage.structure.element
from sage.categories.category import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

from sage.structure.parent_old import Parent

is_FractionFieldElement: _cython_3_2_1.cython_function_or_method
make_element: _cython_3_2_1.cython_function_or_method
make_element_old: _cython_3_2_1.cython_function_or_method

class FractionFieldElement[P: Parent](sage.structure.element.FieldElement[P]):
    """FractionFieldElement(parent, numerator, denominator=1, coerce=True, reduce=True)

    File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 58)

    EXAMPLES::

        sage: K = FractionField(PolynomialRing(QQ, 'x'))
        sage: K
        Fraction Field of Univariate Polynomial Ring in x over Rational Field
        sage: loads(K.dumps()) == K
        True
        sage: x = K.gen()
        sage: f = (x^3 + x)/(17 - x^19); f
        (-x^3 - x)/(x^19 - 17)
        sage: loads(f.dumps()) == f
        True

    TESTS:

    Test if :issue:`5451` is fixed::

        sage: A = FiniteField(9,'theta')['t']                                           # needs sage.rings.finite_rings
        sage: K.<t> = FractionField(A)                                                  # needs sage.rings.finite_rings
        sage: f = 2/(t^2 + 2*t); g = t^9/(t^18 + t^10 + t^2); f + g                     # needs sage.rings.finite_rings
        (2*t^15 + 2*t^14 + 2*t^13 + 2*t^12 + 2*t^11 + 2*t^10 + 2*t^9 + t^7 + t^6 + t^5 + t^4 + t^3 + t^2 + t + 1)/(t^17 + t^9 + t)

    Test if :issue:`8671` is fixed::

        sage: P.<n> = QQ[]
        sage: F = P.fraction_field()
        sage: P.one()//F.one()
        1
        sage: F.one().quo_rem(F.one())
        (1, 0)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, numerator, denominator=..., coerce=..., reduce=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 95)

                Initialize ``self``.

                EXAMPLES::

                    sage: from sage.rings.fraction_field_element import FractionFieldElement
                    sage: K.<x> = Frac(ZZ['x'])
                    sage: FractionFieldElement(K, x, 4)
                    x/4
                    sage: FractionFieldElement(K, x, x, reduce=False)
                    x/x
                    sage: f = FractionFieldElement(K, 'hi', 1, coerce=False, reduce=False)
                    sage: f.numerator()
                    'hi'

                    sage: x = var('x')                                                          # needs sage.symbolic
                    sage: K((x + 1)/(x^2 + x + 1))
                    (x + 1)/(x^2 + x + 1)
                    sage: K(355/113)
                    355/113
        """
    @overload
    def denominator(self) -> Any:
        """FractionFieldElement.denominator(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 253)

        Return the denominator of ``self``.

        EXAMPLES::

            sage: R.<x,y> = ZZ[]
            sage: f = x/y + 1; f
            (x + y)/y
            sage: f.denominator()
            y"""
    @overload
    def denominator(self) -> Any:
        """FractionFieldElement.denominator(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 253)

        Return the denominator of ``self``.

        EXAMPLES::

            sage: R.<x,y> = ZZ[]
            sage: f = x/y + 1; f
            (x + y)/y
            sage: f.denominator()
            y"""
    @overload
    def is_one(self) -> Any:
        """FractionFieldElement.is_one(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 1076)

        Return ``True`` if this element is equal to one.

        EXAMPLES::

            sage: F = ZZ['x,y'].fraction_field()
            sage: x,y = F.gens()
            sage: (x/x).is_one()
            True
            sage: (x/y).is_one()
            False"""
    @overload
    def is_one(self) -> Any:
        """FractionFieldElement.is_one(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 1076)

        Return ``True`` if this element is equal to one.

        EXAMPLES::

            sage: F = ZZ['x,y'].fraction_field()
            sage: x,y = F.gens()
            sage: (x/x).is_one()
            True
            sage: (x/y).is_one()
            False"""
    @overload
    def is_one(self) -> Any:
        """FractionFieldElement.is_one(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 1076)

        Return ``True`` if this element is equal to one.

        EXAMPLES::

            sage: F = ZZ['x,y'].fraction_field()
            sage: x,y = F.gens()
            sage: (x/x).is_one()
            True
            sage: (x/y).is_one()
            False"""
    @overload
    def is_square(self, root=...) -> Any:
        """FractionFieldElement.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 267)

        Return whether or not ``self`` is a perfect square.

        If the optional
        argument ``root`` is ``True``, then also returns a square root (or
        ``None``, if the fraction field element is not square).

        INPUT:

        - ``root`` -- whether or not to also return a square
          root (default: ``False``)

        OUTPUT:

        - boolean; whether or not a square

        - object (optional); an actual square root if found, and ``None``
          otherwise

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: (1/t).is_square()
            False
            sage: (1/t^6).is_square()
            True
            sage: ((1+t)^4/t^6).is_square()
            True
            sage: (4*(1+t)^4/t^6).is_square()
            True
            sage: (2*(1+t)^4/t^6).is_square()
            False
            sage: ((1+t)/t^6).is_square()
            False

            sage: (4*(1+t)^4/t^6).is_square(root=True)
            (True, (2*t^2 + 4*t + 2)/t^3)
            sage: (2*(1+t)^4/t^6).is_square(root=True)
            (False, None)

            sage: R.<x> = QQ[]
            sage: a = 2*(x+1)^2 / (2*(x-1)^2); a
            (x^2 + 2*x + 1)/(x^2 - 2*x + 1)
            sage: a.is_square()
            True
            sage: (0/x).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """FractionFieldElement.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 267)

        Return whether or not ``self`` is a perfect square.

        If the optional
        argument ``root`` is ``True``, then also returns a square root (or
        ``None``, if the fraction field element is not square).

        INPUT:

        - ``root`` -- whether or not to also return a square
          root (default: ``False``)

        OUTPUT:

        - boolean; whether or not a square

        - object (optional); an actual square root if found, and ``None``
          otherwise

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: (1/t).is_square()
            False
            sage: (1/t^6).is_square()
            True
            sage: ((1+t)^4/t^6).is_square()
            True
            sage: (4*(1+t)^4/t^6).is_square()
            True
            sage: (2*(1+t)^4/t^6).is_square()
            False
            sage: ((1+t)/t^6).is_square()
            False

            sage: (4*(1+t)^4/t^6).is_square(root=True)
            (True, (2*t^2 + 4*t + 2)/t^3)
            sage: (2*(1+t)^4/t^6).is_square(root=True)
            (False, None)

            sage: R.<x> = QQ[]
            sage: a = 2*(x+1)^2 / (2*(x-1)^2); a
            (x^2 + 2*x + 1)/(x^2 - 2*x + 1)
            sage: a.is_square()
            True
            sage: (0/x).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """FractionFieldElement.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 267)

        Return whether or not ``self`` is a perfect square.

        If the optional
        argument ``root`` is ``True``, then also returns a square root (or
        ``None``, if the fraction field element is not square).

        INPUT:

        - ``root`` -- whether or not to also return a square
          root (default: ``False``)

        OUTPUT:

        - boolean; whether or not a square

        - object (optional); an actual square root if found, and ``None``
          otherwise

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: (1/t).is_square()
            False
            sage: (1/t^6).is_square()
            True
            sage: ((1+t)^4/t^6).is_square()
            True
            sage: (4*(1+t)^4/t^6).is_square()
            True
            sage: (2*(1+t)^4/t^6).is_square()
            False
            sage: ((1+t)/t^6).is_square()
            False

            sage: (4*(1+t)^4/t^6).is_square(root=True)
            (True, (2*t^2 + 4*t + 2)/t^3)
            sage: (2*(1+t)^4/t^6).is_square(root=True)
            (False, None)

            sage: R.<x> = QQ[]
            sage: a = 2*(x+1)^2 / (2*(x-1)^2); a
            (x^2 + 2*x + 1)/(x^2 - 2*x + 1)
            sage: a.is_square()
            True
            sage: (0/x).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """FractionFieldElement.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 267)

        Return whether or not ``self`` is a perfect square.

        If the optional
        argument ``root`` is ``True``, then also returns a square root (or
        ``None``, if the fraction field element is not square).

        INPUT:

        - ``root`` -- whether or not to also return a square
          root (default: ``False``)

        OUTPUT:

        - boolean; whether or not a square

        - object (optional); an actual square root if found, and ``None``
          otherwise

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: (1/t).is_square()
            False
            sage: (1/t^6).is_square()
            True
            sage: ((1+t)^4/t^6).is_square()
            True
            sage: (4*(1+t)^4/t^6).is_square()
            True
            sage: (2*(1+t)^4/t^6).is_square()
            False
            sage: ((1+t)/t^6).is_square()
            False

            sage: (4*(1+t)^4/t^6).is_square(root=True)
            (True, (2*t^2 + 4*t + 2)/t^3)
            sage: (2*(1+t)^4/t^6).is_square(root=True)
            (False, None)

            sage: R.<x> = QQ[]
            sage: a = 2*(x+1)^2 / (2*(x-1)^2); a
            (x^2 + 2*x + 1)/(x^2 - 2*x + 1)
            sage: a.is_square()
            True
            sage: (0/x).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """FractionFieldElement.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 267)

        Return whether or not ``self`` is a perfect square.

        If the optional
        argument ``root`` is ``True``, then also returns a square root (or
        ``None``, if the fraction field element is not square).

        INPUT:

        - ``root`` -- whether or not to also return a square
          root (default: ``False``)

        OUTPUT:

        - boolean; whether or not a square

        - object (optional); an actual square root if found, and ``None``
          otherwise

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: (1/t).is_square()
            False
            sage: (1/t^6).is_square()
            True
            sage: ((1+t)^4/t^6).is_square()
            True
            sage: (4*(1+t)^4/t^6).is_square()
            True
            sage: (2*(1+t)^4/t^6).is_square()
            False
            sage: ((1+t)/t^6).is_square()
            False

            sage: (4*(1+t)^4/t^6).is_square(root=True)
            (True, (2*t^2 + 4*t + 2)/t^3)
            sage: (2*(1+t)^4/t^6).is_square(root=True)
            (False, None)

            sage: R.<x> = QQ[]
            sage: a = 2*(x+1)^2 / (2*(x-1)^2); a
            (x^2 + 2*x + 1)/(x^2 - 2*x + 1)
            sage: a.is_square()
            True
            sage: (0/x).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """FractionFieldElement.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 267)

        Return whether or not ``self`` is a perfect square.

        If the optional
        argument ``root`` is ``True``, then also returns a square root (or
        ``None``, if the fraction field element is not square).

        INPUT:

        - ``root`` -- whether or not to also return a square
          root (default: ``False``)

        OUTPUT:

        - boolean; whether or not a square

        - object (optional); an actual square root if found, and ``None``
          otherwise

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: (1/t).is_square()
            False
            sage: (1/t^6).is_square()
            True
            sage: ((1+t)^4/t^6).is_square()
            True
            sage: (4*(1+t)^4/t^6).is_square()
            True
            sage: (2*(1+t)^4/t^6).is_square()
            False
            sage: ((1+t)/t^6).is_square()
            False

            sage: (4*(1+t)^4/t^6).is_square(root=True)
            (True, (2*t^2 + 4*t + 2)/t^3)
            sage: (2*(1+t)^4/t^6).is_square(root=True)
            (False, None)

            sage: R.<x> = QQ[]
            sage: a = 2*(x+1)^2 / (2*(x-1)^2); a
            (x^2 + 2*x + 1)/(x^2 - 2*x + 1)
            sage: a.is_square()
            True
            sage: (0/x).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """FractionFieldElement.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 267)

        Return whether or not ``self`` is a perfect square.

        If the optional
        argument ``root`` is ``True``, then also returns a square root (or
        ``None``, if the fraction field element is not square).

        INPUT:

        - ``root`` -- whether or not to also return a square
          root (default: ``False``)

        OUTPUT:

        - boolean; whether or not a square

        - object (optional); an actual square root if found, and ``None``
          otherwise

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: (1/t).is_square()
            False
            sage: (1/t^6).is_square()
            True
            sage: ((1+t)^4/t^6).is_square()
            True
            sage: (4*(1+t)^4/t^6).is_square()
            True
            sage: (2*(1+t)^4/t^6).is_square()
            False
            sage: ((1+t)/t^6).is_square()
            False

            sage: (4*(1+t)^4/t^6).is_square(root=True)
            (True, (2*t^2 + 4*t + 2)/t^3)
            sage: (2*(1+t)^4/t^6).is_square(root=True)
            (False, None)

            sage: R.<x> = QQ[]
            sage: a = 2*(x+1)^2 / (2*(x-1)^2); a
            (x^2 + 2*x + 1)/(x^2 - 2*x + 1)
            sage: a.is_square()
            True
            sage: (0/x).is_square()
            True"""
    @overload
    def is_square(self, root=...) -> Any:
        """FractionFieldElement.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 267)

        Return whether or not ``self`` is a perfect square.

        If the optional
        argument ``root`` is ``True``, then also returns a square root (or
        ``None``, if the fraction field element is not square).

        INPUT:

        - ``root`` -- whether or not to also return a square
          root (default: ``False``)

        OUTPUT:

        - boolean; whether or not a square

        - object (optional); an actual square root if found, and ``None``
          otherwise

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: (1/t).is_square()
            False
            sage: (1/t^6).is_square()
            True
            sage: ((1+t)^4/t^6).is_square()
            True
            sage: (4*(1+t)^4/t^6).is_square()
            True
            sage: (2*(1+t)^4/t^6).is_square()
            False
            sage: ((1+t)/t^6).is_square()
            False

            sage: (4*(1+t)^4/t^6).is_square(root=True)
            (True, (2*t^2 + 4*t + 2)/t^3)
            sage: (2*(1+t)^4/t^6).is_square(root=True)
            (False, None)

            sage: R.<x> = QQ[]
            sage: a = 2*(x+1)^2 / (2*(x-1)^2); a
            (x^2 + 2*x + 1)/(x^2 - 2*x + 1)
            sage: a.is_square()
            True
            sage: (0/x).is_square()
            True"""
    @overload
    def is_square(self, root=...) -> Any:
        """FractionFieldElement.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 267)

        Return whether or not ``self`` is a perfect square.

        If the optional
        argument ``root`` is ``True``, then also returns a square root (or
        ``None``, if the fraction field element is not square).

        INPUT:

        - ``root`` -- whether or not to also return a square
          root (default: ``False``)

        OUTPUT:

        - boolean; whether or not a square

        - object (optional); an actual square root if found, and ``None``
          otherwise

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: (1/t).is_square()
            False
            sage: (1/t^6).is_square()
            True
            sage: ((1+t)^4/t^6).is_square()
            True
            sage: (4*(1+t)^4/t^6).is_square()
            True
            sage: (2*(1+t)^4/t^6).is_square()
            False
            sage: ((1+t)/t^6).is_square()
            False

            sage: (4*(1+t)^4/t^6).is_square(root=True)
            (True, (2*t^2 + 4*t + 2)/t^3)
            sage: (2*(1+t)^4/t^6).is_square(root=True)
            (False, None)

            sage: R.<x> = QQ[]
            sage: a = 2*(x+1)^2 / (2*(x-1)^2); a
            (x^2 + 2*x + 1)/(x^2 - 2*x + 1)
            sage: a.is_square()
            True
            sage: (0/x).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """FractionFieldElement.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 267)

        Return whether or not ``self`` is a perfect square.

        If the optional
        argument ``root`` is ``True``, then also returns a square root (or
        ``None``, if the fraction field element is not square).

        INPUT:

        - ``root`` -- whether or not to also return a square
          root (default: ``False``)

        OUTPUT:

        - boolean; whether or not a square

        - object (optional); an actual square root if found, and ``None``
          otherwise

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: (1/t).is_square()
            False
            sage: (1/t^6).is_square()
            True
            sage: ((1+t)^4/t^6).is_square()
            True
            sage: (4*(1+t)^4/t^6).is_square()
            True
            sage: (2*(1+t)^4/t^6).is_square()
            False
            sage: ((1+t)/t^6).is_square()
            False

            sage: (4*(1+t)^4/t^6).is_square(root=True)
            (True, (2*t^2 + 4*t + 2)/t^3)
            sage: (2*(1+t)^4/t^6).is_square(root=True)
            (False, None)

            sage: R.<x> = QQ[]
            sage: a = 2*(x+1)^2 / (2*(x-1)^2); a
            (x^2 + 2*x + 1)/(x^2 - 2*x + 1)
            sage: a.is_square()
            True
            sage: (0/x).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """FractionFieldElement.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 267)

        Return whether or not ``self`` is a perfect square.

        If the optional
        argument ``root`` is ``True``, then also returns a square root (or
        ``None``, if the fraction field element is not square).

        INPUT:

        - ``root`` -- whether or not to also return a square
          root (default: ``False``)

        OUTPUT:

        - boolean; whether or not a square

        - object (optional); an actual square root if found, and ``None``
          otherwise

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: (1/t).is_square()
            False
            sage: (1/t^6).is_square()
            True
            sage: ((1+t)^4/t^6).is_square()
            True
            sage: (4*(1+t)^4/t^6).is_square()
            True
            sage: (2*(1+t)^4/t^6).is_square()
            False
            sage: ((1+t)/t^6).is_square()
            False

            sage: (4*(1+t)^4/t^6).is_square(root=True)
            (True, (2*t^2 + 4*t + 2)/t^3)
            sage: (2*(1+t)^4/t^6).is_square(root=True)
            (False, None)

            sage: R.<x> = QQ[]
            sage: a = 2*(x+1)^2 / (2*(x-1)^2); a
            (x^2 + 2*x + 1)/(x^2 - 2*x + 1)
            sage: a.is_square()
            True
            sage: (0/x).is_square()
            True"""
    @overload
    def is_zero(self) -> Any:
        """FractionFieldElement.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 1057)

        Return ``True`` if this element is equal to zero.

        EXAMPLES::

            sage: F = ZZ['x,y'].fraction_field()
            sage: x,y = F.gens()
            sage: t = F(0)/x
            sage: t.is_zero()
            True
            sage: u = 1/x - 1/x
            sage: u.is_zero()
            True
            sage: u.parent() is F
            True"""
    @overload
    def is_zero(self) -> Any:
        """FractionFieldElement.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 1057)

        Return ``True`` if this element is equal to zero.

        EXAMPLES::

            sage: F = ZZ['x,y'].fraction_field()
            sage: x,y = F.gens()
            sage: t = F(0)/x
            sage: t.is_zero()
            True
            sage: u = 1/x - 1/x
            sage: u.is_zero()
            True
            sage: u.parent() is F
            True"""
    @overload
    def is_zero(self) -> Any:
        """FractionFieldElement.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 1057)

        Return ``True`` if this element is equal to zero.

        EXAMPLES::

            sage: F = ZZ['x,y'].fraction_field()
            sage: x,y = F.gens()
            sage: t = F(0)/x
            sage: t.is_zero()
            True
            sage: u = 1/x - 1/x
            sage: u.is_zero()
            True
            sage: u.parent() is F
            True"""
    def nth_root(self, n) -> Any:
        """FractionFieldElement.nth_root(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 325)

        Return a ``n``-th root of this element.

        EXAMPLES::

            sage: R = QQ['t'].fraction_field()
            sage: t = R.gen()
            sage: p = (t+1)^3 / (t^2+t-1)^3
            sage: p.nth_root(3)
            (t + 1)/(t^2 + t - 1)

            sage: p = (t+1) / (t-1)
            sage: p.nth_root(2)
            Traceback (most recent call last):
            ...
            ValueError: not a 2nd power"""
    @overload
    def numerator(self) -> Any:
        """FractionFieldElement.numerator(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 239)

        Return the numerator of ``self``.

        EXAMPLES::

            sage: R.<x,y> = ZZ[]
            sage: f = x/y + 1; f
            (x + y)/y
            sage: f.numerator()
            x + y"""
    @overload
    def numerator(self) -> Any:
        """FractionFieldElement.numerator(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 239)

        Return the numerator of ``self``.

        EXAMPLES::

            sage: R.<x,y> = ZZ[]
            sage: f = x/y + 1; f
            (x + y)/y
            sage: f.numerator()
            x + y"""
    @overload
    def reduce(self) -> Any:
        """FractionFieldElement.reduce(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 171)

        Reduce this fraction.

        Divides out the gcd of the numerator and denominator. If the
        denominator becomes a unit, it becomes 1. Additionally, depending on
        the base ring, the leading coefficients of the numerator and the
        denominator may be normalized to 1.

        Automatically called for exact rings, but because it may be
        numerically unstable for inexact rings it must be called manually
        in that case.

        EXAMPLES::

            sage: R.<x> = RealField(10)[]                                               # needs sage.rings.real_mpfr
            sage: f = (x^2+2*x+1)/(x+1); f                                              # needs sage.rings.real_mpfr
            (x^2 + 2.0*x + 1.0)/(x + 1.0)
            sage: f.reduce(); f                                                         # needs sage.rings.real_mpfr
            x + 1.0

        TESTS:

        Check that :issue:`8111` is fixed::

            sage: K.<k>= QQ[]
            sage: frac = (64*k^2+128)/(64*k^3+256)
            sage: frac.reduce(); frac
            (k^2 + 2)/(k^3 + 4)"""
    @overload
    def reduce(self) -> Any:
        """FractionFieldElement.reduce(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 171)

        Reduce this fraction.

        Divides out the gcd of the numerator and denominator. If the
        denominator becomes a unit, it becomes 1. Additionally, depending on
        the base ring, the leading coefficients of the numerator and the
        denominator may be normalized to 1.

        Automatically called for exact rings, but because it may be
        numerically unstable for inexact rings it must be called manually
        in that case.

        EXAMPLES::

            sage: R.<x> = RealField(10)[]                                               # needs sage.rings.real_mpfr
            sage: f = (x^2+2*x+1)/(x+1); f                                              # needs sage.rings.real_mpfr
            (x^2 + 2.0*x + 1.0)/(x + 1.0)
            sage: f.reduce(); f                                                         # needs sage.rings.real_mpfr
            x + 1.0

        TESTS:

        Check that :issue:`8111` is fixed::

            sage: K.<k>= QQ[]
            sage: frac = (64*k^2+128)/(64*k^3+256)
            sage: frac.reduce(); frac
            (k^2 + 2)/(k^3 + 4)"""
    @overload
    def reduce(self) -> Any:
        """FractionFieldElement.reduce(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 171)

        Reduce this fraction.

        Divides out the gcd of the numerator and denominator. If the
        denominator becomes a unit, it becomes 1. Additionally, depending on
        the base ring, the leading coefficients of the numerator and the
        denominator may be normalized to 1.

        Automatically called for exact rings, but because it may be
        numerically unstable for inexact rings it must be called manually
        in that case.

        EXAMPLES::

            sage: R.<x> = RealField(10)[]                                               # needs sage.rings.real_mpfr
            sage: f = (x^2+2*x+1)/(x+1); f                                              # needs sage.rings.real_mpfr
            (x^2 + 2.0*x + 1.0)/(x + 1.0)
            sage: f.reduce(); f                                                         # needs sage.rings.real_mpfr
            x + 1.0

        TESTS:

        Check that :issue:`8111` is fixed::

            sage: K.<k>= QQ[]
            sage: frac = (64*k^2+128)/(64*k^3+256)
            sage: frac.reduce(); frac
            (k^2 + 2)/(k^3 + 4)"""
    def specialization(self, D=..., phi=...) -> Any:
        """FractionFieldElement.specialization(self, D=None, phi=None)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 1198)

        Return the specialization of a fraction element of a polynomial ring."""
    @overload
    def subs(self, in_dict=..., *args, **kwds) -> Any:
        '''FractionFieldElement.subs(self, in_dict=None, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 475)

        Substitute variables in the numerator and denominator of ``self``.

        If a dictionary is passed, the keys are mapped to generators
        of the parent ring.  Otherwise, the arguments are transmitted
        unchanged to the method ``subs`` of the numerator and the
        denominator.

        EXAMPLES::

            sage: x, y = PolynomialRing(ZZ, 2, \'xy\').gens()
            sage: f = x^2 + y + x^2*y^2 + 5
            sage: (1/f).subs(x=5)
            1/(25*y^2 + y + 30)

        TESTS:

        Check that :issue:`37122` is fixed::

            sage: P = PolynomialRing(QQ, ["x%s" % i for i in range(10000)])
            sage: PF = P.fraction_field()
            sage: p = sum(i*P.gen(i) for i in range(5)) / sum(i*P.gen(i) for i in range(8))
            sage: v = P.gen(4)
            sage: p.subs({v: 100})
            (x1 + 2*x2 + 3*x3 + 400)/(x1 + 2*x2 + 3*x3 + 5*x5 + 6*x6 + 7*x7 + 400)'''
    @overload
    def subs(self, x=...) -> Any:
        '''FractionFieldElement.subs(self, in_dict=None, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 475)

        Substitute variables in the numerator and denominator of ``self``.

        If a dictionary is passed, the keys are mapped to generators
        of the parent ring.  Otherwise, the arguments are transmitted
        unchanged to the method ``subs`` of the numerator and the
        denominator.

        EXAMPLES::

            sage: x, y = PolynomialRing(ZZ, 2, \'xy\').gens()
            sage: f = x^2 + y + x^2*y^2 + 5
            sage: (1/f).subs(x=5)
            1/(25*y^2 + y + 30)

        TESTS:

        Check that :issue:`37122` is fixed::

            sage: P = PolynomialRing(QQ, ["x%s" % i for i in range(10000)])
            sage: PF = P.fraction_field()
            sage: p = sum(i*P.gen(i) for i in range(5)) / sum(i*P.gen(i) for i in range(8))
            sage: v = P.gen(4)
            sage: p.subs({v: 100})
            (x1 + 2*x2 + 3*x3 + 400)/(x1 + 2*x2 + 3*x3 + 5*x5 + 6*x6 + 7*x7 + 400)'''
    @overload
    def valuation(self, v=...) -> Any:
        """FractionFieldElement.valuation(self, v=None)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 1020)

        Return the valuation of ``self``, assuming that the numerator and
        denominator have valuation functions defined on them.

        EXAMPLES::

            sage: x = PolynomialRing(RationalField(),'x').gen()
            sage: f = (x^3 + x)/(x^2 - 2*x^3)
            sage: f
            (-1/2*x^2 - 1/2)/(x^2 - 1/2*x)
            sage: f.valuation()
            -1
            sage: f.valuation(x^2 + 1)
            1"""
    @overload
    def valuation(self) -> Any:
        """FractionFieldElement.valuation(self, v=None)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 1020)

        Return the valuation of ``self``, assuming that the numerator and
        denominator have valuation functions defined on them.

        EXAMPLES::

            sage: x = PolynomialRing(RationalField(),'x').gen()
            sage: f = (x^3 + x)/(x^2 - 2*x^3)
            sage: f
            (-1/2*x^2 - 1/2)/(x^2 - 1/2*x)
            sage: f.valuation()
            -1
            sage: f.valuation(x^2 + 1)
            1"""
    def __abs__(self) -> Any:
        """FractionFieldElement.__abs__(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 970)

        EXAMPLES::

            sage: from sage.rings.fraction_field_element import FractionFieldElement
            sage: abs(FractionFieldElement(QQ, -2, 3, coerce=False))
            2/3"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __call__(self, *x, **kwds) -> Any:
        """FractionFieldElement.__call__(self, *x, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 450)

        Evaluate the fraction at the given arguments.

        This assumes that a
        call function is defined for the numerator and denominator.

        EXAMPLES::

            sage: x = PolynomialRing(RationalField(),'x',3).gens()
            sage: f = x[0] + x[1] - 2*x[1]*x[2]
            sage: f
            -2*x1*x2 + x0 + x1
            sage: f(1,2,5)
            -17
            sage: h = f / (x[1] + x[2])
            sage: h
            (-2*x1*x2 + x0 + x1)/(x1 + x2)
            sage: h(1,2,5)
            -17/7
            sage: h(x0=1)
            (-2*x1*x2 + x1 + 1)/(x1 + x2)"""
    def __complex__(self) -> Any:
        """FractionFieldElement.__complex__(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 822)

        EXAMPLES::

            sage: K.<x,y> = Frac(I.parent()['x,y'])                                     # needs sage.symbolic
            sage: complex(x/(I*x) + (I*y)/y)                                            # needs sage.symbolic
            0j"""
    def __copy__(self) -> Any:
        """FractionFieldElement.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 224)

        Make a copy of ``self``.

        EXAMPLES::

            sage: R.<x,y> = ZZ[]
            sage: f = x/y + 1; f
            (x + y)/y
            sage: copy(f)
            (x + y)/y"""
    def __float__(self) -> Any:
        """FractionFieldElement.__float__(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 812)

        EXAMPLES::

            sage: K.<x,y> = Frac(ZZ['x,y'])
            sage: float(x/x + y/y)
            2.0"""
    def __hash__(self) -> Any:
        """FractionFieldElement.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 347)

        This function hashes in a special way to ensure that generators of
        a ring `R` and generators of a fraction field of `R` have the same
        hash. This enables them to be used as keys interchangeably in a
        dictionary (since ``==`` will claim them equal).

        This is useful for substitution using dicts.

        EXAMPLES::

            sage: R.<x> = ZZ[]
            sage: hash(R.0) == hash(FractionField(R).0)
            True
            sage: ((x+1)/(x^2+1)).subs({x:1})
            1
            sage: d={x:1}
            sage: d[FractionField(R).0]
            1
            sage: R.<x>=QQ[] # this probably has a separate implementation from ZZ[]
            sage: hash(R.0)==hash(FractionField(R).0)
            True
            sage: d={x:1}
            sage: d[FractionField(R).0]
            1
            sage: R.<x,y,z>=ZZ[] # this probably has a separate implementation from ZZ[]
            sage: hash(R.0)==hash(FractionField(R).0)
            True
            sage: d={x:1}
            sage: d[FractionField(R).0]
            1
            sage: R.<x,y,z>=QQ[] # this probably has a separate implementation from ZZ[]
            sage: hash(R.0)==hash(FractionField(R).0)
            True
            sage: ((x+1)/(x^2+1)).subs({x:1})
            1
            sage: d={x:1}
            sage: d[FractionField(R).0]
            1
            sage: hash(R(1)/R(2))==hash(1/2)
            True

        Check that :issue:`16268` is fixed::

            sage: ku.<u> = FractionField(PolynomialRing(QQ,'u'))
            sage: a = 27*u^2+81*u+243
            sage: b = 27*u-81
            sage: c = u^2 + 3*u + 9
            sage: d = u-3
            sage: s = a/b
            sage: t = c/d
            sage: s == t
            True
            sage: len(set([s,t]))
            1

        Check that :issue:`25199` is fixed::

            sage: R.<x,y,z> = QQbar[]                                                   # needs sage.rings.number_field
            sage: hash(R.0) == hash(FractionField(R).0)
            True
            sage: ((x+1)/(x^2+1)).subs({x: 1})
            1

        Check that :issue:`35238` is fixed::

            sage: K.<x,y>=ZZ[]
            sage: hash(x/y) == hash((-x)/(-y))
            True"""
    def __int__(self) -> Any:
        """FractionFieldElement.__int__(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 790)

        EXAMPLES::

            sage: K = Frac(ZZ['x'])
            sage: int(K(-3))
            -3
            sage: K.<x> = Frac(RR['x'])
            sage: x/x
            x/x
            sage: int(x/x)
            1
            sage: int(K(.5))
            0"""
    def __invert__(self) -> Any:
        """FractionFieldElement.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 980)

        EXAMPLES::

            sage: K.<t> = Frac(GF(7)['t'])
            sage: f = (t^2+5)/(t-1)
            sage: ~f
            (t + 6)/(t^2 + 5)"""
    def __neg__(self) -> Any:
        """FractionFieldElement.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 956)

        EXAMPLES::

            sage: K.<t> = Frac(GF(5)['t'])
            sage: f = (t^2+t)/(t+2); f
            (t^2 + t)/(t + 2)
            sage: -f
            (4*t^2 + 4*t)/(t + 2)"""
    def __pow__(self, right, dummy) -> Any:
        """FractionFieldElement.__pow__(self, right, dummy)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 905)

        Return ``self`` raised to the ``right``-th power.

        Note that we need to check whether or not right is negative so we
        don't set ``_numerator`` or ``_denominator`` to an element of the
        fraction field instead of the underlying ring.

        EXAMPLES::

            sage: R = QQ['x','y']
            sage: FR = R.fraction_field()
            sage: x,y = FR.gens()
            sage: a = x^2; a
            x^2
            sage: type(a.numerator())                                                   # needs sage.libs.singular
            <class 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>
            sage: type(a.denominator())                                                 # needs sage.libs.singular
            <class 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>
            sage: a = x^(-2); a
            1/x^2
            sage: type(a.numerator())                                                   # needs sage.libs.singular
            <class 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>
            sage: type(a.denominator())                                                 # needs sage.libs.singular
            <class 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>
            sage: x^0
            1
            sage: ((x+y)/(x-y))^2
            (x^2 + 2*x*y + y^2)/(x^2 - 2*x*y + y^2)
            sage: ((x+y)/(x-y))^-2
            (x^2 - 2*x*y + y^2)/(x^2 + 2*x*y + y^2)
            sage: ((x+y)/(x-y))^0
            1"""
    def __reduce__(self) -> Any:
        """FractionFieldElement.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 1110)

        For pickling.

        EXAMPLES::

            sage: F = ZZ['x,y'].fraction_field()
            sage: f = F.random_element()
            sage: loads(f.dumps()) == f
            True"""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""

class FractionFieldElement_1poly_field(FractionFieldElement):
    """FractionFieldElement_1poly_field(parent, numerator, denominator=1, coerce=True, reduce=True)

    File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 1206)

    A fraction field element where the parent is the fraction field of a
    univariate polynomial ring over a field.

    Many of the functions here are included for coherence with number fields."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, numerator, denominator=..., coerce=..., reduce=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 1214)

                TESTS:

                    sage: P.<x> = QQ[]
                    sage: a = (2*x^2)/x
                    sage: ~a
                    1/2/x
                    sage: 1/a
                    1/2/x
        """
    @overload
    def is_integral(self) -> Any:
        """FractionFieldElement_1poly_field.is_integral(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 1239)

        Return whether this element is actually a polynomial.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: elt = (t^2 + t - 2) / (t + 2); elt # == (t + 2)*(t - 1)/(t + 2)
            t - 1
            sage: elt.is_integral()
            True
            sage: elt = (t^2 - t) / (t+2); elt # == t*(t - 1)/(t + 2)
            (t^2 - t)/(t + 2)
            sage: elt.is_integral()
            False"""
    @overload
    def is_integral(self) -> Any:
        """FractionFieldElement_1poly_field.is_integral(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 1239)

        Return whether this element is actually a polynomial.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: elt = (t^2 + t - 2) / (t + 2); elt # == (t + 2)*(t - 1)/(t + 2)
            t - 1
            sage: elt.is_integral()
            True
            sage: elt = (t^2 - t) / (t+2); elt # == t*(t - 1)/(t + 2)
            (t^2 - t)/(t + 2)
            sage: elt.is_integral()
            False"""
    @overload
    def is_integral(self) -> Any:
        """FractionFieldElement_1poly_field.is_integral(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 1239)

        Return whether this element is actually a polynomial.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: elt = (t^2 + t - 2) / (t + 2); elt # == (t + 2)*(t - 1)/(t + 2)
            t - 1
            sage: elt.is_integral()
            True
            sage: elt = (t^2 - t) / (t+2); elt # == t*(t - 1)/(t + 2)
            (t^2 - t)/(t + 2)
            sage: elt.is_integral()
            False"""
    def reduce(self) -> Any:
        """FractionFieldElement_1poly_field.reduce(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 1276)

        Pick a normalized representation of ``self``.

        In particular, for any a == b, after normalization they will have the
        same numerator and denominator.

        EXAMPLES:

        For univariate rational functions over a field, we have::

            sage: R.<x> = QQ[]
            sage: (2 + 2*x) / (4*x) # indirect doctest
            (1/2*x + 1/2)/x

        Compare with::

            sage: R.<x> = ZZ[]
            sage: (2 + 2*x) / (4*x)
            (x + 1)/(2*x)"""
    @overload
    def support(self) -> Any:
        """FractionFieldElement_1poly_field.support(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 1259)

        Return a sorted list of primes dividing either the numerator or
        denominator of this element.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: h = (t^14 + 2*t^12 - 4*t^11 - 8*t^9 + 6*t^8 + 12*t^6 - 4*t^5
            ....:      - 8*t^3 + t^2 + 2)/(t^6 + 6*t^5 + 9*t^4 - 2*t^2 - 12*t - 18)
            sage: h.support()                                                           # needs sage.libs.pari
            [t - 1, t + 3, t^2 + 2, t^2 + t + 1, t^4 - 2]"""
    @overload
    def support(self) -> Any:
        """FractionFieldElement_1poly_field.support(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_element.pyx (starting at line 1259)

        Return a sorted list of primes dividing either the numerator or
        denominator of this element.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: h = (t^14 + 2*t^12 - 4*t^11 - 8*t^9 + 6*t^8 + 12*t^6 - 4*t^5
            ....:      - 8*t^3 + t^2 + 2)/(t^6 + 6*t^5 + 9*t^4 - 2*t^2 - 12*t - 18)
            sage: h.support()                                                           # needs sage.libs.pari
            [t - 1, t + 3, t^2 + 2, t^2 + t + 1, t^4 - 2]"""
