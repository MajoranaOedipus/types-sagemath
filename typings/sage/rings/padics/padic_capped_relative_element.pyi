import _cython_3_2_1
import cypari2.pari_instance
import sage as sage
import sage.categories.morphism
import sage.rings.morphism
import sage.rings.padics.padic_generic_element
import sage.rings.padics.pow_computer
from sage.categories.category import ZZ as ZZ
from sage.categories.homset import Hom as Hom
from sage.categories.sets_cat import Sets as Sets
from sage.categories.sets_with_partial_maps import SetsWithPartialMaps as SetsWithPartialMaps
from sage.rings.finite_rings.finite_field_base import FiniteField as FiniteField
from sage.rings.finite_rings.integer_mod import Mod as Mod
from sage.rings.infinity import infinity as infinity
from sage.rings.padics.misc import trim_zeros as trim_zeros
from sage.rings.padics.precision_error import PrecisionError as PrecisionError
from sage.rings.polynomial.polynomial_element import Polynomial as Polynomial
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import canonical_coercion as canonical_coercion, have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

base_p_list: _cython_3_2_1.cython_function_or_method
pari: cypari2.pari_instance.Pari
unpickle_cre_v2: _cython_3_2_1.cython_function_or_method
unpickle_pcre_v1: _cython_3_2_1.cython_function_or_method

class CRElement(pAdicTemplateElement):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def add_bigoh(self, absprec) -> Any:
        """CRElement.add_bigoh(self, absprec)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 885)

        Return a new element with absolute precision decreased to
        ``absprec``.

        INPUT:

        - ``absprec`` -- integer or infinity

        OUTPUT:

        an equal element with precision set to the minimum of ``self``'s
        precision and ``absprec``

        EXAMPLES::

            sage: R = Zp(7,4,'capped-rel','series'); a = R(8); a.add_bigoh(1)
            1 + O(7)
            sage: b = R(0); b.add_bigoh(3)
            O(7^3)
            sage: R = Qp(7,4); a = R(8); a.add_bigoh(1)
            1 + O(7)
            sage: b = R(0); b.add_bigoh(3)
            O(7^3)

        The precision never increases::

            sage: R(4).add_bigoh(2).add_bigoh(4)
            4 + O(7^2)

        Another example that illustrates that the precision does
        not increase::

            sage: k = Qp(3,5)
            sage: a = k(1234123412/3^70); a
            2*3^-70 + 3^-69 + 3^-68 + 3^-67 + O(3^-65)
            sage: a.add_bigoh(2)
            2*3^-70 + 3^-69 + 3^-68 + 3^-67 + O(3^-65)

            sage: k = Qp(5,10)
            sage: a = k(1/5^3 + 5^2); a
            5^-3 + 5^2 + O(5^7)
            sage: a.add_bigoh(2)
            5^-3 + O(5^2)
            sage: a.add_bigoh(-1)
            5^-3 + O(5^-1)"""
    def is_equal_to(self, _right, absprec=...) -> Any:
        """CRElement.is_equal_to(self, _right, absprec=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 1056)

        Return whether ``self`` is equal to ``right`` modulo
        `\\pi^{\\mbox{absprec}}`.

        If ``absprec`` is ``None``, returns ``True`` if ``self`` and ``right`` are
        equal to the minimum of their precisions.

        INPUT:

        - ``right`` -- a `p`-adic element
        - ``absprec`` -- integer, infinity, or ``None``

        EXAMPLES::

            sage: R = Zp(5, 10); a = R(0); b = R(0, 3); c = R(75, 5)
            sage: aa = a + 625; bb = b + 625; cc = c + 625
            sage: a.is_equal_to(aa), a.is_equal_to(aa, 4), a.is_equal_to(aa, 5)
            (False, True, False)
            sage: a.is_equal_to(aa, 15)
            Traceback (most recent call last):
            ...
            PrecisionError: elements not known to enough precision

            sage: a.is_equal_to(a, 50000)
            True

            sage: a.is_equal_to(b), a.is_equal_to(b, 2)
            (True, True)
            sage: a.is_equal_to(b, 5)
            Traceback (most recent call last):
            ...
            PrecisionError: elements not known to enough precision

            sage: b.is_equal_to(b, 5)
            Traceback (most recent call last):
            ...
            PrecisionError: elements not known to enough precision

            sage: b.is_equal_to(bb, 3)
            True
            sage: b.is_equal_to(bb, 4)
            Traceback (most recent call last):
            ...
            PrecisionError: elements not known to enough precision

            sage: c.is_equal_to(b, 2), c.is_equal_to(b, 3)
            (True, False)
            sage: c.is_equal_to(b, 4)
            Traceback (most recent call last):
            ...
            PrecisionError: elements not known to enough precision

            sage: c.is_equal_to(cc, 2), c.is_equal_to(cc, 4), c.is_equal_to(cc, 5)
            (True, True, False)

        TESTS::

            sage: aa.is_equal_to(a), aa.is_equal_to(a, 4), aa.is_equal_to(a, 5)
            (False, True, False)
            sage: aa.is_equal_to(a, 15)
            Traceback (most recent call last):
            ...
            PrecisionError: elements not known to enough precision

            sage: b.is_equal_to(a), b.is_equal_to(a, 2)
            (True, True)
            sage: b.is_equal_to(a, 5)
            Traceback (most recent call last):
            ...
            PrecisionError: elements not known to enough precision

            sage: bb.is_equal_to(b, 3)
            True
            sage: bb.is_equal_to(b, 4)
            Traceback (most recent call last):
            ...
            PrecisionError: elements not known to enough precision

            sage: b.is_equal_to(c, 2), b.is_equal_to(c, 3)
            (True, False)
            sage: b.is_equal_to(c, 4)
            Traceback (most recent call last):
            ...
            PrecisionError: elements not known to enough precision

            sage: cc.is_equal_to(c, 2), cc.is_equal_to(c, 4), cc.is_equal_to(c, 5)
            (True, True, False)"""
    def is_zero(self, absprec=...) -> Any:
        """CRElement.is_zero(self, absprec=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 995)

        Determine whether this element is zero modulo
        `\\pi^{\\mbox{absprec}}`.

        If ``absprec`` is ``None``, returns ``True`` if this element is
        indistinguishable from zero.

        INPUT:

        - ``absprec`` -- integer, infinity, or ``None``

        EXAMPLES::

            sage: R = Zp(5); a = R(0); b = R(0,5); c = R(75)
            sage: a.is_zero(), a.is_zero(6)
            (True, True)
            sage: b.is_zero(), b.is_zero(5)
            (True, True)
            sage: c.is_zero(), c.is_zero(2), c.is_zero(3)
            (False, True, False)
            sage: b.is_zero(6)
            Traceback (most recent call last):
            ...
            PrecisionError: not enough precision to determine if element is zero"""
    @overload
    def polynomial(self, var=...) -> Any:
        """CRElement.polynomial(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 1346)

        Return a polynomial over the base ring that yields this element
        when evaluated at the generator of the parent.

        INPUT:

        - ``var`` -- string, the variable name for the polynomial

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: K.<a> = Qq(5^3)
            sage: a.polynomial()
            (1 + O(5^20))*x + O(5^20)
            sage: a.polynomial(var='y')
            (1 + O(5^20))*y + O(5^20)
            sage: (5*a^2 + K(25, 4)).polynomial()
            (5 + O(5^4))*x^2 + O(5^4)*x + 5^2 + O(5^4)"""
    @overload
    def polynomial(self) -> Any:
        """CRElement.polynomial(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 1346)

        Return a polynomial over the base ring that yields this element
        when evaluated at the generator of the parent.

        INPUT:

        - ``var`` -- string, the variable name for the polynomial

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: K.<a> = Qq(5^3)
            sage: a.polynomial()
            (1 + O(5^20))*x + O(5^20)
            sage: a.polynomial(var='y')
            (1 + O(5^20))*y + O(5^20)
            sage: (5*a^2 + K(25, 4)).polynomial()
            (5 + O(5^4))*x^2 + O(5^4)*x + 5^2 + O(5^4)"""
    @overload
    def polynomial(self, var=...) -> Any:
        """CRElement.polynomial(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 1346)

        Return a polynomial over the base ring that yields this element
        when evaluated at the generator of the parent.

        INPUT:

        - ``var`` -- string, the variable name for the polynomial

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: K.<a> = Qq(5^3)
            sage: a.polynomial()
            (1 + O(5^20))*x + O(5^20)
            sage: a.polynomial(var='y')
            (1 + O(5^20))*y + O(5^20)
            sage: (5*a^2 + K(25, 4)).polynomial()
            (5 + O(5^4))*x^2 + O(5^4)*x + 5^2 + O(5^4)"""
    @overload
    def polynomial(self) -> Any:
        """CRElement.polynomial(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 1346)

        Return a polynomial over the base ring that yields this element
        when evaluated at the generator of the parent.

        INPUT:

        - ``var`` -- string, the variable name for the polynomial

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: K.<a> = Qq(5^3)
            sage: a.polynomial()
            (1 + O(5^20))*x + O(5^20)
            sage: a.polynomial(var='y')
            (1 + O(5^20))*y + O(5^20)
            sage: (5*a^2 + K(25, 4)).polynomial()
            (5 + O(5^4))*x^2 + O(5^4)*x + 5^2 + O(5^4)"""
    @overload
    def precision_absolute(self) -> Any:
        """CRElement.precision_absolute(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 1370)

        Return the absolute precision of this element.

        This is the power of the maximal ideal modulo which this
        element is defined.

        EXAMPLES::

            sage: R = Zp(7,3,'capped-rel'); a = R(7); a.precision_absolute()
            4
            sage: R = Qp(7,3); a = R(7); a.precision_absolute()
            4
            sage: R(7^-3).precision_absolute()
            0

            sage: R(0).precision_absolute()
            +Infinity
            sage: R(0,7).precision_absolute()
            7"""
    @overload
    def precision_absolute(self) -> Any:
        """CRElement.precision_absolute(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 1370)

        Return the absolute precision of this element.

        This is the power of the maximal ideal modulo which this
        element is defined.

        EXAMPLES::

            sage: R = Zp(7,3,'capped-rel'); a = R(7); a.precision_absolute()
            4
            sage: R = Qp(7,3); a = R(7); a.precision_absolute()
            4
            sage: R(7^-3).precision_absolute()
            0

            sage: R(0).precision_absolute()
            +Infinity
            sage: R(0,7).precision_absolute()
            7"""
    @overload
    def precision_absolute(self) -> Any:
        """CRElement.precision_absolute(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 1370)

        Return the absolute precision of this element.

        This is the power of the maximal ideal modulo which this
        element is defined.

        EXAMPLES::

            sage: R = Zp(7,3,'capped-rel'); a = R(7); a.precision_absolute()
            4
            sage: R = Qp(7,3); a = R(7); a.precision_absolute()
            4
            sage: R(7^-3).precision_absolute()
            0

            sage: R(0).precision_absolute()
            +Infinity
            sage: R(0,7).precision_absolute()
            7"""
    @overload
    def precision_absolute(self) -> Any:
        """CRElement.precision_absolute(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 1370)

        Return the absolute precision of this element.

        This is the power of the maximal ideal modulo which this
        element is defined.

        EXAMPLES::

            sage: R = Zp(7,3,'capped-rel'); a = R(7); a.precision_absolute()
            4
            sage: R = Qp(7,3); a = R(7); a.precision_absolute()
            4
            sage: R(7^-3).precision_absolute()
            0

            sage: R(0).precision_absolute()
            +Infinity
            sage: R(0,7).precision_absolute()
            7"""
    @overload
    def precision_absolute(self) -> Any:
        """CRElement.precision_absolute(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 1370)

        Return the absolute precision of this element.

        This is the power of the maximal ideal modulo which this
        element is defined.

        EXAMPLES::

            sage: R = Zp(7,3,'capped-rel'); a = R(7); a.precision_absolute()
            4
            sage: R = Qp(7,3); a = R(7); a.precision_absolute()
            4
            sage: R(7^-3).precision_absolute()
            0

            sage: R(0).precision_absolute()
            +Infinity
            sage: R(0,7).precision_absolute()
            7"""
    @overload
    def precision_absolute(self) -> Any:
        """CRElement.precision_absolute(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 1370)

        Return the absolute precision of this element.

        This is the power of the maximal ideal modulo which this
        element is defined.

        EXAMPLES::

            sage: R = Zp(7,3,'capped-rel'); a = R(7); a.precision_absolute()
            4
            sage: R = Qp(7,3); a = R(7); a.precision_absolute()
            4
            sage: R(7^-3).precision_absolute()
            0

            sage: R(0).precision_absolute()
            +Infinity
            sage: R(0,7).precision_absolute()
            7"""
    @overload
    def precision_relative(self) -> Any:
        """CRElement.precision_relative(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 1397)

        Return the relative precision of this element.

        This is the power of the maximal ideal modulo which the unit
        part of ``self`` is defined.

        EXAMPLES::

            sage: R = Zp(7,3,'capped-rel'); a = R(7); a.precision_relative()
            3
            sage: R = Qp(7,3); a = R(7); a.precision_relative()
            3
            sage: a = R(7^-2, -1); a.precision_relative()
            1
            sage: a
            7^-2 + O(7^-1)

            sage: R(0).precision_relative()
            0
            sage: R(0,7).precision_relative()
            0"""
    @overload
    def precision_relative(self) -> Any:
        """CRElement.precision_relative(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 1397)

        Return the relative precision of this element.

        This is the power of the maximal ideal modulo which the unit
        part of ``self`` is defined.

        EXAMPLES::

            sage: R = Zp(7,3,'capped-rel'); a = R(7); a.precision_relative()
            3
            sage: R = Qp(7,3); a = R(7); a.precision_relative()
            3
            sage: a = R(7^-2, -1); a.precision_relative()
            1
            sage: a
            7^-2 + O(7^-1)

            sage: R(0).precision_relative()
            0
            sage: R(0,7).precision_relative()
            0"""
    @overload
    def precision_relative(self) -> Any:
        """CRElement.precision_relative(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 1397)

        Return the relative precision of this element.

        This is the power of the maximal ideal modulo which the unit
        part of ``self`` is defined.

        EXAMPLES::

            sage: R = Zp(7,3,'capped-rel'); a = R(7); a.precision_relative()
            3
            sage: R = Qp(7,3); a = R(7); a.precision_relative()
            3
            sage: a = R(7^-2, -1); a.precision_relative()
            1
            sage: a
            7^-2 + O(7^-1)

            sage: R(0).precision_relative()
            0
            sage: R(0,7).precision_relative()
            0"""
    @overload
    def precision_relative(self) -> Any:
        """CRElement.precision_relative(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 1397)

        Return the relative precision of this element.

        This is the power of the maximal ideal modulo which the unit
        part of ``self`` is defined.

        EXAMPLES::

            sage: R = Zp(7,3,'capped-rel'); a = R(7); a.precision_relative()
            3
            sage: R = Qp(7,3); a = R(7); a.precision_relative()
            3
            sage: a = R(7^-2, -1); a.precision_relative()
            1
            sage: a
            7^-2 + O(7^-1)

            sage: R(0).precision_relative()
            0
            sage: R(0,7).precision_relative()
            0"""
    @overload
    def precision_relative(self) -> Any:
        """CRElement.precision_relative(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 1397)

        Return the relative precision of this element.

        This is the power of the maximal ideal modulo which the unit
        part of ``self`` is defined.

        EXAMPLES::

            sage: R = Zp(7,3,'capped-rel'); a = R(7); a.precision_relative()
            3
            sage: R = Qp(7,3); a = R(7); a.precision_relative()
            3
            sage: a = R(7^-2, -1); a.precision_relative()
            1
            sage: a
            7^-2 + O(7^-1)

            sage: R(0).precision_relative()
            0
            sage: R(0,7).precision_relative()
            0"""
    @overload
    def precision_relative(self) -> Any:
        """CRElement.precision_relative(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 1397)

        Return the relative precision of this element.

        This is the power of the maximal ideal modulo which the unit
        part of ``self`` is defined.

        EXAMPLES::

            sage: R = Zp(7,3,'capped-rel'); a = R(7); a.precision_relative()
            3
            sage: R = Qp(7,3); a = R(7); a.precision_relative()
            3
            sage: a = R(7^-2, -1); a.precision_relative()
            1
            sage: a
            7^-2 + O(7^-1)

            sage: R(0).precision_relative()
            0
            sage: R(0,7).precision_relative()
            0"""
    def unit_part(self) -> pAdicTemplateElement:
        """CRElement.unit_part(self) -> pAdicTemplateElement

        File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 1424)

        Return `u`, where this element is `\\pi^v u`.

        EXAMPLES::

            sage: R = Zp(17,4,'capped-rel')
            sage: a = R(18*17)
            sage: a.unit_part()
            1 + 17 + O(17^4)
            sage: type(a)
            <class 'sage.rings.padics.padic_capped_relative_element.pAdicCappedRelativeElement'>
            sage: R = Qp(17,4,'capped-rel')
            sage: a = R(18*17)
            sage: a.unit_part()
            1 + 17 + O(17^4)
            sage: type(a)
            <class 'sage.rings.padics.padic_capped_relative_element.pAdicCappedRelativeElement'>
            sage: a = R(2*17^2); a
            2*17^2 + O(17^6)
            sage: a.unit_part()
            2 + O(17^4)
            sage: b=1/a; b
            9*17^-2 + 8*17^-1 + 8 + 8*17 + O(17^2)
            sage: b.unit_part()
            9 + 8*17 + 8*17^2 + 8*17^3 + O(17^4)
            sage: Zp(5)(75).unit_part()
            3 + O(5^20)

            sage: R(0).unit_part()
            Traceback (most recent call last):
            ...
            ValueError: unit part of 0 not defined
            sage: R(0,7).unit_part()
            O(17^0)"""
    @overload
    def val_unit(self, p=...) -> Any:
        """CRElement.val_unit(self, p=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 1487)

        Return a pair ``(self.valuation(), self.unit_part())``.

        INPUT:

        - ``p`` -- a prime (default: ``None``); if specified, will make sure
          that ``p == self.parent().prime()``

        .. NOTE::

            The optional argument ``p`` is used for consistency with the
            valuation methods on integers and rationals.

        EXAMPLES::

            sage: R = Zp(5); a = R(75, 20); a
            3*5^2 + O(5^20)
            sage: a.val_unit()
            (2, 3 + O(5^18))
            sage: R(0).val_unit()
            Traceback (most recent call last):
            ...
            ValueError: unit part of 0 not defined
            sage: R(0, 10).val_unit()
            (10, O(5^0))"""
    @overload
    def val_unit(self) -> Any:
        """CRElement.val_unit(self, p=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 1487)

        Return a pair ``(self.valuation(), self.unit_part())``.

        INPUT:

        - ``p`` -- a prime (default: ``None``); if specified, will make sure
          that ``p == self.parent().prime()``

        .. NOTE::

            The optional argument ``p`` is used for consistency with the
            valuation methods on integers and rationals.

        EXAMPLES::

            sage: R = Zp(5); a = R(75, 20); a
            3*5^2 + O(5^20)
            sage: a.val_unit()
            (2, 3 + O(5^18))
            sage: R(0).val_unit()
            Traceback (most recent call last):
            ...
            ValueError: unit part of 0 not defined
            sage: R(0, 10).val_unit()
            (10, O(5^0))"""
    @overload
    def val_unit(self) -> Any:
        """CRElement.val_unit(self, p=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 1487)

        Return a pair ``(self.valuation(), self.unit_part())``.

        INPUT:

        - ``p`` -- a prime (default: ``None``); if specified, will make sure
          that ``p == self.parent().prime()``

        .. NOTE::

            The optional argument ``p`` is used for consistency with the
            valuation methods on integers and rationals.

        EXAMPLES::

            sage: R = Zp(5); a = R(75, 20); a
            3*5^2 + O(5^20)
            sage: a.val_unit()
            (2, 3 + O(5^18))
            sage: R(0).val_unit()
            Traceback (most recent call last):
            ...
            ValueError: unit part of 0 not defined
            sage: R(0, 10).val_unit()
            (10, O(5^0))"""
    @overload
    def val_unit(self) -> Any:
        """CRElement.val_unit(self, p=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 1487)

        Return a pair ``(self.valuation(), self.unit_part())``.

        INPUT:

        - ``p`` -- a prime (default: ``None``); if specified, will make sure
          that ``p == self.parent().prime()``

        .. NOTE::

            The optional argument ``p`` is used for consistency with the
            valuation methods on integers and rationals.

        EXAMPLES::

            sage: R = Zp(5); a = R(75, 20); a
            3*5^2 + O(5^20)
            sage: a.val_unit()
            (2, 3 + O(5^18))
            sage: R(0).val_unit()
            Traceback (most recent call last):
            ...
            ValueError: unit part of 0 not defined
            sage: R(0, 10).val_unit()
            (10, O(5^0))"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __copy__(self) -> Any:
        """CRElement.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 241)

        Return a copy of this element.

        EXAMPLES::

            sage: a = Zp(5,6)(17); b = copy(a)
            sage: a == b
            True
            sage: a is b
            False"""
    def __hash__(self) -> Any:
        """CRElement.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 1527)

        Hashing.

        .. WARNING::

            Hashing of `p`-adic elements will likely be deprecated soon.  See :issue:`11895`.

        EXAMPLES::

            sage: R = Zp(5)
            sage: hash(R(17))  # indirect doctest
            17

            sage: hash(R(-1))
            1977844648            # 32-bit
            95367431640624        # 64-bit"""
    def __invert__(self) -> Any:
        """CRElement.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 425)

        Return the multiplicative inverse of this element.

        .. NOTE::

            The result of inversion always lives in the fraction
            field, even if the element to be inverted is a unit.

        EXAMPLES::

            sage: R = Qp(7,4,'capped-rel','series'); a = R(3); a
            3 + O(7^4)
            sage: ~a   # indirect doctest
            5 + 4*7 + 4*7^2 + 4*7^3 + O(7^4)"""
    def __pow__(self, CRElementself, _right, dummy) -> Any:
        """CRElement.__pow__(CRElement self, _right, dummy)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 525)

        Exponentiation.

        When ``right`` is divisible by `p` then one can get more
        precision than expected.

        Lemma 2.1 [Pau2006]_:

        Let `\\alpha` be in `\\mathcal{O}_K`.  Let

        .. MATH::

            p = -\\pi_K^{e_K} \\epsilon

        be the factorization of `p` where `\\epsilon` is a unit.  Then
        the `p`-th power of `1 + \\alpha \\pi_K^{\\lambda}` satisfies

        .. MATH::

            (1 + \\alpha \\pi^{\\lambda})^p \\equiv \\left{ \\begin{array}{lll}
            1 + \\alpha^p \\pi_K^{p \\lambda} &
             \\mod \\mathfrak{p}_K^{p \\lambda + 1} &
             \\mbox{if $1 \\le \\lambda < \\frac{e_K}{p-1}$} \\\\\n            1 + (\\alpha^p - \\epsilon \\alpha) \\pi_K^{p \\lambda} &
             \\mod \\mathfrak{p}_K^{p \\lambda + 1} &
             \\mbox{if $\\lambda = \\frac{e_K}{p-1}$} \\\\\n            1 - \\epsilon \\alpha \\pi_K^{\\lambda + e} &
             \\mod \\mathfrak{p}_K^{\\lambda + e + 1} &
             \\mbox{if $\\lambda > \\frac{e_K}{p-1}$}
            \\end{array} \\right.


        So if ``right`` is divisible by `p^k` we can multiply the
        relative precision by `p` until we exceed `e/(p-1)`, then add
        `e` until we have done a total of `k` things: the precision of
        the result can therefore be greater than the precision of
        ``self``.

        For `\\alpha` in `\\ZZ_p` we can simplify the result a bit.  In
        this case, the `p`-th power of `1 + \\alpha p^{\\lambda}`
        satisfies

        .. MATH::

            (1 + \\alpha p^{\\lambda})^p \\equiv 1 + \\alpha p^{\\lambda + 1} mod p^{\\lambda + 2}

        unless `\\lambda = 1` and `p = 2`, in which case

        .. MATH::

            (1 + 2 \\alpha)^2 \\equiv 1 + 4(\\alpha^2 + \\alpha) mod 8

        So for `p \\ne 2`, if right is divisible by `p^k` then we add
        `k` to the relative precision of the answer.

        For `p = 2`, if we start with something of relative precision
        1 (ie `2^m + O(2^{m+1})`), `\\alpha^2 + \\alpha \\equiv 0 \\mod
        2`, so the precision of the result is `k + 2`:

        .. MATH::

            (2^m + O(2^{m+1}))^{2^k} = 2^{m 2^k} + O(2^{m 2^k + k + 2})

        For `p`-adic exponents, we define `\\alpha^\\beta` as
        `\\exp(\\beta \\log(\\alpha))`.  The precision of the result is
        determined using the power series expansions for the
        exponential and logarithm maps, together with the notes above.

        .. NOTE::

            For `p`-adic exponents we always need that `a` is a unit.
            For unramified extensions `a^b` will converge as long as
            `b` is integral (though it may converge for non-integral
            `b` as well depending on the value of `a`).  However, in
            highly ramified extensions some bases may be sufficiently
            close to `1` that `exp(b log(a))` does not converge even
            though `b` is integral.

        .. WARNING::

            If `\\alpha` is a unit, but not congruent to `1` modulo
            `\\pi_K`, the result will not be the limit over integers
            `b` converging to `\\beta` since this limit does not exist.
            Rather, the logarithm kills torsion in `\\ZZ_p^\\times`, and
            `\\alpha^\\beta` will equal `(\\alpha')^\\beta`, where
            `\\alpha'` is the quotient of `\\alpha` by the Teichmuller
            representative congruent to `\\alpha` modulo `\\pi_K`.  Thus
            the result will always be congruent to `1` modulo `\\pi_K`.

        REFERENCES:

        - [Pau2006]_

        INPUT:

        - ``_right`` -- currently integers and `p`-adic exponents are
          supported

        - ``dummy`` -- not used (Python's ``__pow__`` signature
          includes it)

        EXAMPLES::

            sage: R = Zp(19, 5, 'capped-rel','series')
            sage: a = R(-1); a
            18 + 18*19 + 18*19^2 + 18*19^3 + 18*19^4 + O(19^5)
            sage: a^2    # indirect doctest
            1 + O(19^5)
            sage: a^3
            18 + 18*19 + 18*19^2 + 18*19^3 + 18*19^4 + O(19^5)
            sage: R(5)^30
            11 + 14*19 + 19^2 + 7*19^3 + O(19^5)
            sage: K = Qp(19, 5, 'capped-rel','series')
            sage: a = K(-1); a
            18 + 18*19 + 18*19^2 + 18*19^3 + 18*19^4 + O(19^5)
            sage: a^2
            1 + O(19^5)
            sage: a^3
            18 + 18*19 + 18*19^2 + 18*19^3 + 18*19^4 + O(19^5)
            sage: K(5)^30
            11 + 14*19 + 19^2 + 7*19^3 + O(19^5)
            sage: K(5, 3)^19  # indirect doctest
            5 + 3*19 + 11*19^3 + O(19^4)

        `p`-adic exponents are also supported::

            sage: a = K(8/5,4); a
            13 + 7*19 + 11*19^2 + 7*19^3 + O(19^4)
            sage: a^(K(19/7))
            1 + 14*19^2 + 11*19^3 + 13*19^4 + O(19^5)
            sage: (a // K.teichmuller(13))^(K(19/7))
            1 + 14*19^2 + 11*19^3 + 13*19^4 + O(19^5)
            sage: (a.log() * 19/7).exp()
            1 + 14*19^2 + 11*19^3 + 13*19^4 + O(19^5)

        TESTS:

        Check that :issue:`31875` is fixed::

            sage: R(1)^R(0)
            1 + O(19^5)

            sage: # needs sage.libs.ntl
            sage: S.<a> = ZqCR(4)
            sage: S(1)^S(0)
            1 + O(2^20)"""
    def __reduce__(self) -> Any:
        """CRElement.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 294)

        Return a tuple of a function and data that can be used to unpickle this
        element.

        TESTS::

            sage: a = ZpCR(5)(-3)
            sage: type(a)
            <class 'sage.rings.padics.padic_capped_relative_element.pAdicCappedRelativeElement'>
            sage: loads(dumps(a)) == a  # indirect doctest
            True"""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""

class ExpansionIter:
    """File: /build/sagemath/src/sage/src/sage/rings/padics/padic_template_element.pxi (starting at line 906)

        An iterator over a `p`-adic expansion.

        This class should not be instantiated directly, but instead
        using :meth:`expansion`.

        INPUT:

        - ``elt`` -- the `p`-adic element
        - ``prec`` -- the number of terms to be emitted
        - ``mode`` -- either ``simple_mode``, ``smallest_mode`` or ``teichmuller_mode``

        EXAMPLES::

            sage: E = Zp(5,4)(373).expansion()
            sage: I = iter(E)  # indirect doctest
            sage: type(I)
            <class 'sage.rings.padics.padic_capped_relative_element.ExpansionIter'>
    """
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def __iter__(self) -> Any:
        """ExpansionIter.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_template_element.pxi (starting at line 973)

        Characteristic property of an iterator: ``__iter__`` returns itself.

        TESTS::

            sage: E = Zp(5,4)(373).expansion()
            sage: I = iter(E)
            sage: I is iter(I)
            True"""
    def __len__(self) -> Any:
        """ExpansionIter.__len__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_template_element.pxi (starting at line 986)

        Return the number of terms that will be emitted.

        TESTS::

            sage: E = Zp(5,4)(373).expansion()
            sage: I = iter(E)
            sage: len(I)
            4
            sage: c = next(I); len(I)
            3"""
    def __next__(self) -> Any:
        """ExpansionIter.__next__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_template_element.pxi (starting at line 1001)

        Provide the next coefficient in the `p`-adic expansion.

        EXAMPLES::

            sage: E = Zp(5,4)(373).expansion()
            sage: I = iter(E)
            sage: next(I)
            3
            sage: next(I), next(I), next(I)
            (4, 4, 2)"""

class ExpansionIterable:
    """File: /build/sagemath/src/sage/src/sage/rings/padics/padic_template_element.pxi (starting at line 1035)

        An iterable storing a `p`-adic expansion of an element.

        This class should not be instantiated directly, but instead using :meth:`expansion`.

        INPUT:

        - ``elt`` -- the `p`-adic element
        - ``prec`` -- the number of terms to be emitted
        - ``val_shift`` -- how many zeros to add at the beginning of the expansion,
          or the number of initial terms to truncate (if negative)
        - ``mode`` -- one of the following:

          * ``'simple_mode'``
          * ``'smallest_mode'``
          * ``'teichmuller_mode'``

        EXAMPLES::

            sage: E = Zp(5,4)(373).expansion()  # indirect doctest
            sage: type(E)
            <class 'sage.rings.padics.padic_capped_relative_element.ExpansionIterable'>
    """
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def __getitem__(self, n) -> Any:
        """ExpansionIterable.__getitem__(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_template_element.pxi (starting at line 1145)

        Return the ``n``-th entry in the expansion.

        Negative indices are not allowed.

        EXAMPLES::

            sage: E = Zp(5,4)(373).expansion()
            sage: E[0]
            3
            sage: E[3]
            2
            sage: list(E[::2])
            [3, 4]
            sage: a = E[-1]
            Traceback (most recent call last):
            ...
            ValueError: negative indices not supported
            sage: Zp(5,4)(373).expansion(lift_mode='smallest')[3]
            -2"""
    def __iter__(self) -> Any:
        """ExpansionIterable.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_template_element.pxi (starting at line 1097)

        Return an iterator, based on a corresponding :class:`ExpansionIter`.

        If ``val_shift`` is positive, will first emit that many zeros
        (of the appropriate type: ``[]`` instead when the inertia degree
        is larger than one.

        If ``val_shift`` is negative, will truncate that many terms at
        the start of the expansion.

        EXAMPLES::

            sage: E = Zp(5,4)(373).expansion()
            sage: type(iter(E))
            <class 'sage.rings.padics.padic_capped_relative_element.ExpansionIter'>
            sage: E = Zp(5,4)(373).expansion(start_val=-1)
            sage: type(iter(E))
            <class 'itertools.chain'>
            sage: E = Zp(5,4)(373).expansion(start_val=1)
            sage: type(iter(E))
            <class 'itertools.islice'>"""
    def __len__(self) -> Any:
        """ExpansionIterable.__len__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_template_element.pxi (starting at line 1128)

        Return the number of terms that will be emitted.

        TESTS::

            sage: len(Zp(5,4)(373).expansion())
            4
            sage: len(Zp(5,4)(373).expansion(start_val=-1))
            5
            sage: len(Zp(5,4)(373).expansion(start_val=1))
            3
            sage: len(Zp(5,4)(0).expansion())
            0"""

class PowComputer_(sage.rings.padics.pow_computer.PowComputer_base):
    """PowComputer_(Integer prime, long cache_limit, long prec_cap, long ram_prec_cap, bool in_field)

    File: /build/sagemath/src/sage/src/sage/rings/padics/padic_capped_relative_element.pyx (starting at line 38)

    A PowComputer for a capped-relative `p`-adic ring or field."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, Integerprime, longcache_limit, longprec_cap, longram_prec_cap, boolin_field) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/padic_capped_relative_element.pyx (starting at line 42)

                Initialization.

                EXAMPLES::

                    sage: R = ZpCR(5)
                    sage: type(R.prime_pow)
                    <class 'sage.rings.padics.padic_capped_relative_element.PowComputer_'>
                    sage: R.prime_pow._prec_type
                    'capped-rel'
        """

class pAdicCappedRelativeElement(CRElement):
    """File: /build/sagemath/src/sage/src/sage/rings/padics/padic_capped_relative_element.pyx (starting at line 57)

        Construct new element with given parent and value.

        INPUT:

        - ``x`` -- value to coerce into a capped relative ring or field

        - ``absprec`` -- maximum number of digits of absolute precision

        - ``relprec`` -- maximum number of digits of relative precision

        EXAMPLES::

            sage: R = Zp(5, 10, 'capped-rel')

        Construct from integers::

            sage: R(3)
            3 + O(5^10)
            sage: R(75)
            3*5^2 + O(5^12)
            sage: R(0)
            0
            sage: R(-1)
            4 + 4*5 + 4*5^2 + 4*5^3 + 4*5^4 + 4*5^5 + 4*5^6 + 4*5^7 + 4*5^8 + 4*5^9 + O(5^10)
            sage: R(-5)
            4*5 + 4*5^2 + 4*5^3 + 4*5^4 + 4*5^5 + 4*5^6 + 4*5^7 + 4*5^8 + 4*5^9 + 4*5^10 + O(5^11)
            sage: R(-7*25)
            3*5^2 + 3*5^3 + 4*5^4 + 4*5^5 + 4*5^6 + 4*5^7 + 4*5^8 + 4*5^9 + 4*5^10 + 4*5^11 + O(5^12)

        Construct from rationals::

            sage: R(1/2)
            3 + 2*5 + 2*5^2 + 2*5^3 + 2*5^4 + 2*5^5 + 2*5^6 + 2*5^7 + 2*5^8 + 2*5^9 + O(5^10)
            sage: R(-7875/874)
            3*5^3 + 2*5^4 + 2*5^5 + 5^6 + 3*5^7 + 2*5^8 + 3*5^10 + 3*5^11 + 3*5^12 + O(5^13)
            sage: R(15/425)
            Traceback (most recent call last):
            ...
            ValueError: p divides the denominator

        Construct from IntegerMod::

            sage: R(Integers(125)(3))
            3 + O(5^3)
            sage: R(Integers(5)(3))
            3 + O(5)
            sage: R(Integers(5^30)(3))
            3 + O(5^10)
            sage: R(Integers(5^30)(1+5^23))
            1 + O(5^10)
            sage: R(Integers(49)(3))
            Traceback (most recent call last):
            ...
            TypeError: p does not divide modulus 49

        ::

            sage: R(Integers(48)(3))
            Traceback (most recent call last):
            ...
            TypeError: p does not divide modulus 48

        Some other conversions::

            sage: R(R(5))
            5 + O(5^11)

        Construct from Pari objects::

            sage: R = Zp(5)
            sage: x = pari(123123) ; R(x)                                                   # needs sage.libs.pari
            3 + 4*5 + 4*5^2 + 4*5^3 + 5^4 + 4*5^5 + 2*5^6 + 5^7 + O(5^20)
            sage: R(pari(R(5252)))
            2 + 2*5^3 + 3*5^4 + 5^5 + O(5^20)
            sage: R = Zp(5,prec=5)
            sage: R(pari(-1))
            4 + 4*5 + 4*5^2 + 4*5^3 + 4*5^4 + O(5^5)
            sage: pari(R(-1))                                                               # needs sage.libs.pari
            4 + 4*5 + 4*5^2 + 4*5^3 + 4*5^4 + O(5^5)
            sage: pari(R(0))                                                                # needs sage.libs.pari
            0
            sage: R(pari(R(0,5)))
            O(5^5)

        .. TODO:: doctests for converting from other types of `p`-adic rings
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def lift(self) -> Any:
        """pAdicCappedRelativeElement.lift(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_capped_relative_element.pyx (starting at line 145)

        Return an integer or rational congruent to ``self`` modulo ``self``'s
        precision.  If a rational is returned, its denominator will equal
        ``p^ordp(self)``.

        EXAMPLES::

            sage: R = Zp(7,4,'capped-rel'); a = R(8); a.lift()
            8
            sage: R = Qp(7,4); a = R(8); a.lift()
            8
            sage: R = Qp(7,4); a = R(8/7); a.lift()
            8/7"""
    def residue(self, absprec=..., field=..., check_prec=...) -> Any:
        """pAdicCappedRelativeElement.residue(self, absprec=1, field=None, check_prec=True)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_capped_relative_element.pyx (starting at line 252)

        Reduce this element modulo `p^{\\mathrm{absprec}}`.

        INPUT:

        - ``absprec`` -- nonnegative integer (default: 1)

        - ``field`` -- boolean (default: ``None``); whether to return an element
          of `\\GF{p}` or `\\ZZ / p\\ZZ`

        - ``check_prec`` -- boolean (default: ``True``); whether to raise
          an error if this element has insufficient precision to determine
          the reduction

        OUTPUT:

        This element reduced modulo `p^\\mathrm{absprec}` as an element of
        `\\ZZ/p^\\mathrm{absprec}\\ZZ`.

        EXAMPLES::

            sage: R = Zp(7,4)
            sage: a = R(8)
            sage: a.residue(1)
            1

        This is different from applying ``% p^n`` which returns an element in
        the same ring::

            sage: b = a.residue(2); b
            8
            sage: b.parent()
            Ring of integers modulo 49
            sage: c = a % 7^2; c
            1 + 7 + O(7^4)
            sage: c.parent()
            7-adic Ring with capped relative precision 4

        For elements in a field, application of ``% p^n`` always returns
        zero, the remainder of the division by ``p^n``::

            sage: K = Qp(7,4)
            sage: a = K(8)
            sage: a.residue(2)
            8
            sage: a % 7^2
            1 + 7 + O(7^4)

            sage: b = K(1/7)
            sage: b.residue()
            Traceback (most recent call last):
            ...
            ValueError: element must have nonnegative valuation in order to compute residue

        TESTS::

            sage: R = Zp(7,4)
            sage: a = R(8)
            sage: a.residue(0)
            0
            sage: a.residue(-1)
            Traceback (most recent call last):
            ...
            ValueError: cannot reduce modulo a negative power of p
            sage: a.residue(5)
            Traceback (most recent call last):
            ...
            PrecisionError: not enough precision known in order to compute residue
            sage: a.residue(5, check_prec=False)
            8

            sage: a.residue(field=True).parent()
            Finite Field of size 7

        .. SEEALSO::

            :meth:`_mod_`"""
    def __pari__(self) -> Any:
        """pAdicCappedRelativeElement.__pari__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_capped_relative_element.pyx (starting at line 197)

        Convert this element to an equivalent pari element.

        EXAMPLES::

            sage: R = Zp(17, 10); a = ~R(14); pari(a)  # indirect doctest
            11 + 3*17 + 17^2 + 6*17^3 + 13*17^4 + 15*17^5 + 10*17^6 + 3*17^7 + 17^8 + 6*17^9 + O(17^10)
            sage: pari(R(0))                                                            # needs sage.libs.pari
            0
            sage: pari(R(0,5))                                                          # needs sage.libs.pari
            O(17^5)"""

class pAdicCoercion_CR_frac_field(sage.rings.morphism.RingHomomorphism):
    """pAdicCoercion_CR_frac_field(R, K)

    File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 2135)

    The canonical inclusion of `\\ZZ_q` into its fraction field.

    EXAMPLES::

        sage: # needs sage.libs.flint
        sage: R.<a> = ZqCR(27, implementation='FLINT')
        sage: K = R.fraction_field()
        sage: f = K.coerce_map_from(R); f
        Ring morphism:
          From: 3-adic Unramified Extension Ring in a defined by x^3 + 2*x + 1
          To:   3-adic Unramified Extension Field in a defined by x^3 + 2*x + 1

    TESTS::

        sage: TestSuite(f).run()                                                        # needs sage.libs.flint"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, R, K) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 2153)

                Initialization.

                EXAMPLES::

                    sage: # needs sage.libs.flint
                    sage: R.<a> = ZqCR(27, implementation='FLINT')
                    sage: K = R.fraction_field()
                    sage: f = K.coerce_map_from(R); type(f)
                    <class 'sage.rings.padics.qadic_flint_CR.pAdicCoercion_CR_frac_field'>
        """
    @overload
    def is_injective(self) -> Any:
        """pAdicCoercion_CR_frac_field.is_injective(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 2334)

        Return whether this map is injective.

        EXAMPLES::

            sage: # needs sage.libs.flint
            sage: R.<a> = ZqCR(9, implementation='FLINT')
            sage: K = R.fraction_field()
            sage: f = K.coerce_map_from(R)
            sage: f.is_injective()
            True"""
    @overload
    def is_injective(self) -> Any:
        """pAdicCoercion_CR_frac_field.is_injective(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 2334)

        Return whether this map is injective.

        EXAMPLES::

            sage: # needs sage.libs.flint
            sage: R.<a> = ZqCR(9, implementation='FLINT')
            sage: K = R.fraction_field()
            sage: f = K.coerce_map_from(R)
            sage: f.is_injective()
            True"""
    @overload
    def is_surjective(self) -> Any:
        """pAdicCoercion_CR_frac_field.is_surjective(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 2349)

        Return whether this map is surjective.

        EXAMPLES::

            sage: # needs sage.libs.flint
            sage: R.<a> = ZqCR(9, implementation='FLINT')
            sage: K = R.fraction_field()
            sage: f = K.coerce_map_from(R)
            sage: f.is_surjective()
            False"""
    @overload
    def is_surjective(self) -> Any:
        """pAdicCoercion_CR_frac_field.is_surjective(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 2349)

        Return whether this map is surjective.

        EXAMPLES::

            sage: # needs sage.libs.flint
            sage: R.<a> = ZqCR(9, implementation='FLINT')
            sage: K = R.fraction_field()
            sage: f = K.coerce_map_from(R)
            sage: f.is_surjective()
            False"""
    @overload
    def section(self) -> Any:
        """pAdicCoercion_CR_frac_field.section(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 2253)

        Return a map back to the ring that converts elements of
        nonnegative valuation.

        EXAMPLES::

            sage: # needs sage.libs.flint
            sage: R.<a> = ZqCR(27, implementation='FLINT')
            sage: K = R.fraction_field()
            sage: f = K.coerce_map_from(R)
            sage: f(K.gen())
            a + O(3^20)
            sage: f.section()
            Generic morphism:
              From: 3-adic Unramified Extension Field in a defined by x^3 + 2*x + 1
              To:   3-adic Unramified Extension Ring in a defined by x^3 + 2*x + 1"""
    @overload
    def section(self) -> Any:
        """pAdicCoercion_CR_frac_field.section(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 2253)

        Return a map back to the ring that converts elements of
        nonnegative valuation.

        EXAMPLES::

            sage: # needs sage.libs.flint
            sage: R.<a> = ZqCR(27, implementation='FLINT')
            sage: K = R.fraction_field()
            sage: f = K.coerce_map_from(R)
            sage: f(K.gen())
            a + O(3^20)
            sage: f.section()
            Generic morphism:
              From: 3-adic Unramified Extension Field in a defined by x^3 + 2*x + 1
              To:   3-adic Unramified Extension Ring in a defined by x^3 + 2*x + 1"""

class pAdicCoercion_QQ_CR(sage.rings.morphism.RingHomomorphism):
    """pAdicCoercion_QQ_CR(R)

    File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 1765)

    The canonical inclusion from the rationals to a capped relative field.

    EXAMPLES::

        sage: f = Qp(5).coerce_map_from(QQ); f
        Ring morphism:
          From: Rational Field
          To:   5-adic Field with capped relative precision 20

    TESTS::

        sage: TestSuite(f).run()"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, R) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 1780)

                Initialization.

                EXAMPLES::

                    sage: f = Qp(5).coerce_map_from(QQ); type(f)
                    <class 'sage.rings.padics.padic_capped_relative_element.pAdicCoercion_QQ_CR'>
        """
    @overload
    def section(self) -> Any:
        """pAdicCoercion_QQ_CR.section(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 1912)

        Return a map back to the rationals that approximates an element by
        a rational number.

        EXAMPLES::

            sage: f = Qp(5).coerce_map_from(QQ).section()
            sage: f(Qp(5)(1/4))
            1/4
            sage: f(Qp(5)(1/5))
            1/5"""
    @overload
    def section(self) -> Any:
        """pAdicCoercion_QQ_CR.section(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 1912)

        Return a map back to the rationals that approximates an element by
        a rational number.

        EXAMPLES::

            sage: f = Qp(5).coerce_map_from(QQ).section()
            sage: f(Qp(5)(1/4))
            1/4
            sage: f(Qp(5)(1/5))
            1/5"""

class pAdicCoercion_ZZ_CR(sage.rings.morphism.RingHomomorphism):
    """pAdicCoercion_ZZ_CR(R)

    File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 1549)

    The canonical inclusion from the integer ring to a capped relative ring.

    EXAMPLES::

        sage: f = Zp(5).coerce_map_from(ZZ); f
        Ring morphism:
          From: Integer Ring
          To:   5-adic Ring with capped relative precision 20

    TESTS::

        sage: TestSuite(f).run()"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, R) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 1564)

                Initialization.

                EXAMPLES::

                    sage: f = Zp(5).coerce_map_from(ZZ); type(f)
                    <class 'sage.rings.padics.padic_capped_relative_element.pAdicCoercion_ZZ_CR'>
        """
    @overload
    def section(self) -> Any:
        """pAdicCoercion_ZZ_CR.section(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 1692)

        Return a map back to the ring of integers that approximates an element
        by an integer.

        EXAMPLES::

            sage: f = Zp(5).coerce_map_from(ZZ).section()
            sage: f(Zp(5)(-1)) - 5^20
            -1"""
    @overload
    def section(self) -> Any:
        """pAdicCoercion_ZZ_CR.section(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 1692)

        Return a map back to the ring of integers that approximates an element
        by an integer.

        EXAMPLES::

            sage: f = Zp(5).coerce_map_from(ZZ).section()
            sage: f(Zp(5)(-1)) - 5^20
            -1"""

class pAdicConvert_CR_QQ(sage.rings.morphism.RingMap):
    """pAdicConvert_CR_QQ(R)

    File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 1931)

    The map from the capped relative ring back to the rationals that returns a
    rational approximation of its input.

    EXAMPLES::

        sage: f = Qp(5).coerce_map_from(QQ).section(); f
        Set-theoretic ring morphism:
          From: 5-adic Field with capped relative precision 20
          To:   Rational Field"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, R) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 1943)

                Initialization.

                EXAMPLES::

                    sage: f = Qp(5).coerce_map_from(QQ).section(); type(f)
                    <class 'sage.rings.padics.padic_capped_relative_element.pAdicConvert_CR_QQ'>
                    sage: f.category()
                    Category of homsets of sets
        """

class pAdicConvert_CR_ZZ(sage.rings.morphism.RingMap):
    """pAdicConvert_CR_ZZ(R)

    File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 1709)

    The map from a capped relative ring back to the ring of integers that
    returns the smallest nonnegative integer approximation to its input
    which is accurate up to the precision.

    Raises a :exc:`ValueError`, if the input is not in the closure of the image of
    the integers.

    EXAMPLES::

        sage: f = Zp(5).coerce_map_from(ZZ).section(); f
        Set-theoretic ring morphism:
          From: 5-adic Ring with capped relative precision 20
          To:   Integer Ring"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, R) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 1725)

                Initialization.

                EXAMPLES::

                    sage: f = Qp(5).coerce_map_from(ZZ).section(); type(f)
                    <class 'sage.rings.padics.padic_capped_relative_element.pAdicConvert_CR_ZZ'>
                    sage: f.category()
                    Category of homsets of sets with partial maps
                    sage: Zp(5).coerce_map_from(ZZ).section().category()
                    Category of homsets of sets
        """

class pAdicConvert_CR_frac_field(sage.categories.morphism.Morphism):
    """pAdicConvert_CR_frac_field(K, R)

    File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 2365)

    The section of the inclusion from `\\ZZ_q` to its fraction field.

    EXAMPLES::

        sage: # needs sage.libs.flint
        sage: R.<a> = ZqCR(27, implementation='FLINT')
        sage: K = R.fraction_field()
        sage: f = R.convert_map_from(K); f
        Generic morphism:
          From: 3-adic Unramified Extension Field in a defined by x^3 + 2*x + 1
          To:   3-adic Unramified Extension Ring in a defined by x^3 + 2*x + 1"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, K, R) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 2379)

                Initialization.

                EXAMPLES::

                    sage: # needs sage.libs.flint
                    sage: R.<a> = ZqCR(27, implementation='FLINT')
                    sage: K = R.fraction_field()
                    sage: f = R.convert_map_from(K); type(f)
                    <class 'sage.rings.padics.qadic_flint_CR.pAdicConvert_CR_frac_field'>
        """

class pAdicConvert_QQ_CR(sage.categories.morphism.Morphism):
    """pAdicConvert_QQ_CR(R)

    File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 1981)

    The inclusion map from the rationals to a capped relative ring that is
    defined on all elements with nonnegative `p`-adic valuation.

    EXAMPLES::

        sage: f = Zp(5).convert_map_from(QQ); f
        Generic morphism:
          From: Rational Field
          To:   5-adic Ring with capped relative precision 20"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, R) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 1993)

                Initialization.

                EXAMPLES::

                    sage: f = Zp(5).convert_map_from(QQ); type(f)
                    <class 'sage.rings.padics.padic_capped_relative_element.pAdicConvert_QQ_CR'>
        """
    @overload
    def section(self) -> Any:
        """pAdicConvert_QQ_CR.section(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 2117)

        Return the map back to the rationals that returns the smallest
        nonnegative integer approximation to its input which is accurate up to
        the precision.

        EXAMPLES::

            sage: f = Zp(5,4).convert_map_from(QQ).section()
            sage: f(Zp(5,4)(-1))
            -1"""
    @overload
    def section(self) -> Any:
        """pAdicConvert_QQ_CR.section(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CR_template.pxi (starting at line 2117)

        Return the map back to the rationals that returns the smallest
        nonnegative integer approximation to its input which is accurate up to
        the precision.

        EXAMPLES::

            sage: f = Zp(5,4).convert_map_from(QQ).section()
            sage: f(Zp(5,4)(-1))
            -1"""

class pAdicTemplateElement(sage.rings.padics.padic_generic_element.pAdicGenericElement):
    """pAdicTemplateElement(parent, x, absprec=infinity, relprec=infinity)

    File: /build/sagemath/src/sage/src/sage/rings/padics/padic_template_element.pxi (starting at line 58)

    A class for common functionality among the `p`-adic template classes.

    INPUT:

    - ``parent`` -- a local ring or field

    - ``x`` -- data defining this element.  Various types are supported,
      including ints, Integers, Rationals, PARI `p`-adics, integers mod `p^k`
      and other Sage `p`-adics.

    - ``absprec`` -- a cap on the absolute precision of this element

    - ``relprec`` -- a cap on the relative precision of this element

    EXAMPLES::

        sage: Zp(17)(17^3, 8, 4)
        17^3 + O(17^7)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, x, absprec=..., relprec=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/padic_template_element.pxi (starting at line 79)

                Initialization.

                .. NOTE::

                    This initialization function is not called for Integers
                    and Rationals since a conversion morphism has been
                    implemented.  It is, however, used for python ints and longs.

                EXAMPLES::

                    sage: a = Zp(5)(1/2,3); a
                    3 + 2*5 + 2*5^2 + O(5^3)
                    sage: type(a)
                    <class 'sage.rings.padics.padic_capped_relative_element.pAdicCappedRelativeElement'>
                    sage: TestSuite(a).run()

                TESTS::

                    sage: # needs sage.libs.ntl
                    sage: QQq.<zz> = Qq(25,4)
                    sage: FFp = Zp(5,5).residue_field()
                    sage: QQq(FFp.zero())
                    O(5)
                    sage: QQq(FFp.one())
                    1 + O(5)
                    sage: QQq(IntegerModRing(25)(15))
                    3*5 + O(5^2)
                    sage: QQq(IntegerModRing(9)(0))
                    Traceback (most recent call last):
                    ...
                    TypeError: p does not divide modulus 9

                ::

                    sage: Zp(2)(Zp(5)(1))
                    Traceback (most recent call last):
                    ...
                    TypeError: no conversion between padics when prime numbers differ

                Check that bug :issue:`28555` is fixed::

                    sage: A.<a> = Qq(5^2)
                    sage: A.base_ring()(A(1))
                    1 + O(5^20)
                    sage: A.base_ring()(a)
                    Traceback (most recent call last):
                    ...
                    TypeError: element in a proper extension

                Check that bug :issue:`33527` is fixed::

                    sage: K = Qq(25, names='a')
                    sage: K0 = K.base_ring()
                    sage: K0(K(1))
                    1 + O(5^20)
        """
    def expansion(self, n=..., lift_mode=..., start_val=...) -> Any:
        """pAdicTemplateElement.expansion(self, n=None, lift_mode='simple', start_val=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_template_element.pxi (starting at line 407)

        Return the coefficients in a `\\pi`-adic expansion.
        If this is a field element, start at
        `\\pi^{\\mbox{valuation}}`, if a ring element at `\\pi^0`.

        For each lift mode, this function returns a list of `a_i` so
        that this element can be expressed as

        .. MATH::

            \\pi^v \\cdot \\sum_{i=0}^\\infty a_i \\pi^i,

        where `v` is the valuation of this element when the parent is
        a field, and `v = 0` otherwise.

        Different lift modes affect the choice of `a_i`.  When
        ``lift_mode`` is ``'simple'``, the resulting `a_i` will be
        nonnegative: if the residue field is `\\GF{p}` then they
        will be integers with `0 \\le a_i < p`; otherwise they will be
        a list of integers in the same range giving the coefficients
        of a polynomial in the indeterminant representing the maximal
        unramified subextension.

        Choosing ``lift_mode`` as ``'smallest'`` is similar to
        ``'simple'``, but uses a balanced representation `-p/2 < a_i
        \\le p/2`.

        Finally, setting ``lift_mode = 'teichmuller'`` will yield
        Teichmuller representatives for the `a_i`: `a_i^q = a_i`.  In
        this case the `a_i` will lie in the ring of integers of the
        maximal unramified subextension of the parent of this element.

        INPUT:

        - ``n`` -- integer (default: ``None``); if given, returns the
          corresponding entry in the expansion. Can also accept a slice (see
          :meth:`slice`).

        - ``lift_mode`` -- ``'simple'``, ``'smallest'`` or
          ``'teichmuller'`` (default: ``'simple'``)

        - ``start_val`` -- start at this valuation rather than the
          default (`0` or the valuation of this element)

        OUTPUT:

        - If ``n`` is ``None``, an iterable giving a `\\pi`-adic expansion of this
          element.  For base elements the contents will be integers if
          ``lift_mode`` is ``'simple'`` or ``'smallest'``, and
          elements of ``self.parent()`` if ``lift_mode`` is
          ``'teichmuller'``.

        - If ``n`` is an integer, the coefficient of `\\pi^n` in the
          `\\pi`-adic expansion of this element.

        .. NOTE::

            Use slice operators to get a particular range.

        EXAMPLES::

            sage: R = Zp(7,6); a = R(12837162817); a
            3 + 4*7 + 4*7^2 + 4*7^4 + O(7^6)
            sage: E = a.expansion(); E
            7-adic expansion of 3 + 4*7 + 4*7^2 + 4*7^4 + O(7^6)
            sage: list(E)
            [3, 4, 4, 0, 4, 0]
            sage: sum([c * 7^i for i, c in enumerate(E)]) == a
            True
            sage: E = a.expansion(lift_mode='smallest'); E
            7-adic expansion of 3 + 4*7 + 4*7^2 + 4*7^4 + O(7^6) (balanced)
            sage: list(E)
            [3, -3, -2, 1, -3, 1]
            sage: sum([c * 7^i for i, c in enumerate(E)]) == a
            True
            sage: E = a.expansion(lift_mode='teichmuller'); E
            7-adic expansion of 3 + 4*7 + 4*7^2 + 4*7^4 + O(7^6) (teichmuller)
            sage: list(E)
            [3 + 4*7 + 6*7^2 + 3*7^3 + 2*7^5 + O(7^6),
            0,
            5 + 2*7 + 3*7^3 + O(7^4),
            1 + O(7^3),
            3 + 4*7 + O(7^2),
            5 + O(7)]
            sage: sum(c * 7^i for i, c in enumerate(E))
            3 + 4*7 + 4*7^2 + 4*7^4 + O(7^6)

        If the element has positive valuation then the list will start
        with some zeros::

            sage: a = R(7^3 * 17)
            sage: E = a.expansion(); E
            7-adic expansion of 3*7^3 + 2*7^4 + O(7^9)
            sage: list(E)
            [0, 0, 0, 3, 2, 0, 0, 0, 0]

        The expansion of 0 is truncated::

            sage: E = R(0, 7).expansion(); E
            7-adic expansion of O(7^7)
            sage: len(E)
            0
            sage: list(E)
            []

        In fields, on the other hand, the expansion starts at the valuation::

            sage: R = Qp(7,4); a = R(6*7+7**2); E = a.expansion(); E
            7-adic expansion of 6*7 + 7^2 + O(7^5)
            sage: list(E)
            [6, 1, 0, 0]
            sage: list(a.expansion(lift_mode='smallest'))
            [-1, 2, 0, 0]
            sage: list(a.expansion(lift_mode='teichmuller'))
            [6 + 6*7 + 6*7^2 + 6*7^3 + O(7^4),
            2 + 4*7 + 6*7^2 + O(7^3),
            3 + 4*7 + O(7^2),
            3 + O(7)]

        You can ask for a specific entry in the expansion::

            sage: a.expansion(1)
            6
            sage: a.expansion(1, lift_mode='smallest')
            -1
            sage: a.expansion(2, lift_mode='teichmuller')
            2 + 4*7 + 6*7^2 + O(7^3)

        TESTS:

        Check to see that :issue:`10292` is resolved::

            sage: # needs sage.schemes
            sage: E = EllipticCurve('37a')
            sage: R = E.padic_regulator(7)
            sage: len(R.expansion())
            19"""
    @overload
    def lift_to_precision(self, absprec=...) -> Any:
        """pAdicTemplateElement.lift_to_precision(self, absprec=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_template_element.pxi (starting at line 347)

        Return another element of the same parent with absolute precision at
        least ``absprec``, congruent to this `p`-adic element modulo the
        precision of this element.

        INPUT:

        - ``absprec`` -- integer or ``None`` (default: ``None``); the
          absolute precision of the result. If ``None``, lifts to the maximum
          precision allowed.

        .. NOTE::

            If setting ``absprec`` that high would violate the precision cap,
            raises a precision error.  Note that the new digits will not
            necessarily be zero.

        EXAMPLES::

            sage: R = ZpCA(17)
            sage: R(-1,2).lift_to_precision(10)
            16 + 16*17 + O(17^10)
            sage: R(1,15).lift_to_precision(10)
            1 + O(17^15)
            sage: R(1,15).lift_to_precision(30)
            Traceback (most recent call last):
            ...
            PrecisionError: precision higher than allowed by the precision cap
            sage: R(-1,2).lift_to_precision().precision_absolute() == R.precision_cap()
            True

            sage: R = Zp(5); c = R(17,3); c.lift_to_precision(8)
            2 + 3*5 + O(5^8)
            sage: c.lift_to_precision().precision_relative() == R.precision_cap()
            True

        Fixed modulus elements don't raise errors::

            sage: R = ZpFM(5); a = R(5); a.lift_to_precision(7)
            5
            sage: a.lift_to_precision(10000)
            5"""
    @overload
    def lift_to_precision(self) -> Any:
        """pAdicTemplateElement.lift_to_precision(self, absprec=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_template_element.pxi (starting at line 347)

        Return another element of the same parent with absolute precision at
        least ``absprec``, congruent to this `p`-adic element modulo the
        precision of this element.

        INPUT:

        - ``absprec`` -- integer or ``None`` (default: ``None``); the
          absolute precision of the result. If ``None``, lifts to the maximum
          precision allowed.

        .. NOTE::

            If setting ``absprec`` that high would violate the precision cap,
            raises a precision error.  Note that the new digits will not
            necessarily be zero.

        EXAMPLES::

            sage: R = ZpCA(17)
            sage: R(-1,2).lift_to_precision(10)
            16 + 16*17 + O(17^10)
            sage: R(1,15).lift_to_precision(10)
            1 + O(17^15)
            sage: R(1,15).lift_to_precision(30)
            Traceback (most recent call last):
            ...
            PrecisionError: precision higher than allowed by the precision cap
            sage: R(-1,2).lift_to_precision().precision_absolute() == R.precision_cap()
            True

            sage: R = Zp(5); c = R(17,3); c.lift_to_precision(8)
            2 + 3*5 + O(5^8)
            sage: c.lift_to_precision().precision_relative() == R.precision_cap()
            True

        Fixed modulus elements don't raise errors::

            sage: R = ZpFM(5); a = R(5); a.lift_to_precision(7)
            5
            sage: a.lift_to_precision(10000)
            5"""
    @overload
    def lift_to_precision(self) -> Any:
        """pAdicTemplateElement.lift_to_precision(self, absprec=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_template_element.pxi (starting at line 347)

        Return another element of the same parent with absolute precision at
        least ``absprec``, congruent to this `p`-adic element modulo the
        precision of this element.

        INPUT:

        - ``absprec`` -- integer or ``None`` (default: ``None``); the
          absolute precision of the result. If ``None``, lifts to the maximum
          precision allowed.

        .. NOTE::

            If setting ``absprec`` that high would violate the precision cap,
            raises a precision error.  Note that the new digits will not
            necessarily be zero.

        EXAMPLES::

            sage: R = ZpCA(17)
            sage: R(-1,2).lift_to_precision(10)
            16 + 16*17 + O(17^10)
            sage: R(1,15).lift_to_precision(10)
            1 + O(17^15)
            sage: R(1,15).lift_to_precision(30)
            Traceback (most recent call last):
            ...
            PrecisionError: precision higher than allowed by the precision cap
            sage: R(-1,2).lift_to_precision().precision_absolute() == R.precision_cap()
            True

            sage: R = Zp(5); c = R(17,3); c.lift_to_precision(8)
            2 + 3*5 + O(5^8)
            sage: c.lift_to_precision().precision_relative() == R.precision_cap()
            True

        Fixed modulus elements don't raise errors::

            sage: R = ZpFM(5); a = R(5); a.lift_to_precision(7)
            5
            sage: a.lift_to_precision(10000)
            5"""
    def residue(self, absprec=..., field=..., check_prec=...) -> Any:
        """pAdicTemplateElement.residue(self, absprec=1, field=None, check_prec=True)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_template_element.pxi (starting at line 695)

        Reduce this element modulo `p^\\mathrm{absprec}`.

        INPUT:

        - ``absprec`` -- ``0`` or ``1``

        - ``field`` -- boolean (default: ``None``); for precision 1, whether to return
          an element of the residue field or a residue ring.  Currently unused.

        - ``check_prec`` -- boolean (default: ``True``); whether to raise an error if this
          element has insufficient precision to determine the reduction.  Errors are never
          raised for fixed-mod or floating-point types.

        OUTPUT:

        This element reduced modulo `p^\\mathrm{absprec}` as an element of the
        residue field or the null ring.

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: R.<a> = Zq(27, 4)
            sage: (3 + 3*a).residue()
            0
            sage: (a + 1).residue()
            a0 + 1

        TESTS::

            sage: # needs sage.libs.ntl
            sage: a.residue(0)
            0
            sage: a.residue(2)
            Traceback (most recent call last):
            ...
            NotImplementedError: reduction modulo p^n with n>1
            sage: a.residue(10)
            Traceback (most recent call last):
            ...
            PrecisionError: insufficient precision to reduce modulo p^10
            sage: a.residue(10, check_prec=False)
            Traceback (most recent call last):
            ...
            NotImplementedError: reduction modulo p^n with n>1

            sage: # needs sage.libs.flint
            sage: R.<a> = ZqCA(27, 4)
            sage: (3 + 3*a).residue()
            0
            sage: (a + 1).residue()
            a0 + 1

            sage: # needs sage.libs.ntl
            sage: R.<a> = Qq(27, 4)
            sage: (3 + 3*a).residue()
            0
            sage: (a + 1).residue()
            a0 + 1
            sage: (a/3).residue()
            Traceback (most recent call last):
            ...
            ValueError: element must have nonnegative valuation in order to compute residue"""
    def teichmuller_expansion(self, n=...) -> Any:
        """pAdicTemplateElement.teichmuller_expansion(self, n=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_template_element.pxi (starting at line 584)

        Return an iterator over coefficients `a_0, a_1, \\dots, a_n` such that

        - `a_i^q = a_i`, where `q` is the cardinality of the residue field,

        - this element can be expressed as

        .. MATH::

            \\pi^v \\cdot \\sum_{i=0}^\\infty a_i \\pi^i

        where `v` is the valuation of this element when the parent is
        a field, and `v = 0` otherwise.

        - if `a_i \\ne 0`, the precision of `a_i` is `i` less
          than the precision of this element (relative in the case that
          the parent is a field, absolute otherwise)

        .. NOTE::

            The coefficients will lie in the ring of integers of the
            maximal unramified subextension.

        INPUT:

        - ``n`` -- integer (default: ``None``); if given, returns the
          coefficient of `\\pi^n` in the expansion

        EXAMPLES:

        For fields, the expansion starts at the valuation::

            sage: R = Qp(5,5); list(R(70).teichmuller_expansion())
            [4 + 4*5 + 4*5^2 + 4*5^3 + 4*5^4 + O(5^5),
            3 + 3*5 + 2*5^2 + 3*5^3 + O(5^4),
            2 + 5 + 2*5^2 + O(5^3),
            1 + O(5^2),
            4 + O(5)]

        But if you specify ``n``, you get the coefficient of `\\pi^n`::

            sage: R(70).teichmuller_expansion(2)
            3 + 3*5 + 2*5^2 + 3*5^3 + O(5^4)"""
    def unit_part(self) -> pAdicTemplateElement:
        """pAdicTemplateElement.unit_part(self) -> pAdicTemplateElement

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_template_element.pxi (starting at line 648)

        Return the unit part of this element.

        This is the `p`-adic element `u` in the same ring so that this
        element is `\\pi^v u`, where `\\pi` is a uniformizer and `v` is
        the valuation of this element.

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: R.<a> = Zq(125)
            sage: (5*a).unit_part()
            a + O(5^20)"""
    def __lshift__(self, pAdicTemplateElementself, shift) -> Any:
        """pAdicTemplateElement.__lshift__(pAdicTemplateElement self, shift)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_template_element.pxi (starting at line 224)

        Multiply ``self`` by ``pi^shift``.

        If ``shift`` is negative and this element does not lie in a field,
        digits may be truncated.  See ``__rshift__`` for details.

        EXAMPLES:

        We create some `p`-adic rings::

            sage: R = Zp(5, 20, 'capped-abs'); a = R(1000); a
            3*5^3 + 5^4 + O(5^20)
            sage: S = Zp(5); b = S(1000); b
            3*5^3 + 5^4 + O(5^23)

        Shifting to the right is the same as dividing by a power of
        the uniformizer `p` of the `p`-adic ring.::

            sage: a >> 1
            3*5^2 + 5^3 + O(5^19)
            sage: b >> 1
            3*5^2 + 5^3 + O(5^22)

        Shifting to the left is the same as multiplying by a power of
        `p`::

            sage: a << 2
            3*5^5 + 5^6 + O(5^20)
            sage: a*5^2
            3*5^5 + 5^6 + O(5^20)
            sage: b << 2
            3*5^5 + 5^6 + O(5^25)
            sage: b*5^2
            3*5^5 + 5^6 + O(5^25)

        Shifting by a negative integer to the left is the same as
        right shifting by the absolute value::

            sage: a << -3
            3 + 5 + O(5^17)
            sage: a >> 3
            3 + 5 + O(5^17)
            sage: b << -3
            3 + 5 + O(5^20)
            sage: b >> 3
            3 + 5 + O(5^20)"""
    def __rlshift__(self, other):
        """Return value<<self."""
    def __rrshift__(self, other):
        """Return value>>self."""
    def __rshift__(self, pAdicTemplateElementself, shift) -> Any:
        """pAdicTemplateElement.__rshift__(pAdicTemplateElement self, shift)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_template_element.pxi (starting at line 289)

        Divide by ``p^shift``, and truncate (if the parent is not a field).

        EXAMPLES::

            sage: R = Zp(997, 7, 'capped-abs'); a = R(123456878908); a
            964*997 + 572*997^2 + 124*997^3 + O(997^7)
            sage: S = Zp(5); K = Qp(5); b = S(17); b
            2 + 3*5 + O(5^20)

        Shifting to the right divides by a power of `p`, but drops
        terms with negative valuation::

            sage: a >> 3
            124 + O(997^4)
            sage: b >> 1
            3 + O(5^19)
            sage: b >> 40
            O(5^0)

        If the parent is a field no truncation is performed::

            sage: K(17) >> 1
            2*5^-1 + 3 + O(5^19)

        A negative shift multiplies by that power of `p`::

            sage: a >> -3
            964*997^4 + 572*997^5 + 124*997^6 + O(997^7)
            sage: K(17) >> -5
            2*5^5 + 3*5^6 + O(5^25)"""
