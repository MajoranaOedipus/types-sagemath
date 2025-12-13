import sage.structure.element
from sage.rings.infinity import infinity as infinity
from sage.structure.element import coerce_binop as coerce_binop, have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

class LocalGenericElement(sage.structure.element.CommutativeRingElement):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def add_bigoh(self, absprec) -> Any:
        """LocalGenericElement.add_bigoh(self, absprec)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 447)

        Return a copy of this element with absolute precision decreased to
        ``absprec``.

        INPUT:

        - ``absprec`` -- integer or positive infinity

        EXAMPLES::

            sage: K = QpCR(3,4)
            sage: o = K(1); o
            1 + O(3^4)
            sage: o.add_bigoh(2)
            1 + O(3^2)
            sage: o.add_bigoh(-5)
            O(3^-5)

        One cannot use ``add_bigoh`` to lift to a higher precision; this
        can be accomplished with :meth:`lift_to_precision`::

            sage: o.add_bigoh(5)
            1 + O(3^4)

        Negative values of ``absprec`` return an element in the fraction field
        of the element's parent::

            sage: R = ZpCA(3,4)
            sage: R(3).add_bigoh(-5)
            O(3^-5)

        For fixed-mod elements this method truncates the element::

            sage: R = ZpFM(3,4)
            sage: R(3).add_bigoh(1)
            0

        If ``absprec`` exceeds the precision of the element, then this method
        has no effect::

            sage: R(3).add_bigoh(5)
            3

        A negative value for ``absprec`` returns an element in the fraction field::

            sage: R(3).add_bigoh(-1).parent()
            3-adic Field with floating precision 4

        TESTS:

        Test that this also works for infinity::

            sage: R = ZpCR(3,4)
            sage: R(3).add_bigoh(infinity)
            3 + O(3^5)
            sage: R(0).add_bigoh(infinity)
            0

        Check that :issue:`23464` has been resolved::

            sage: x = polygen(QQ)
            sage: R.<pi> = Qp(7).extension(x^3 - 7)                                     # needs sage.libs.ntl
            sage: (pi^93).add_bigoh(-10)                                                # needs sage.libs.ntl sage.symbolic
            O(pi^-10)"""
    @overload
    def euclidean_degree(self) -> Any:
        """LocalGenericElement.euclidean_degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 871)

        Return the degree of this element as an element of a Euclidean domain.

        EXAMPLES:

        For a field, this is always zero except for the zero element::

            sage: K = Qp(2)
            sage: K.one().euclidean_degree()
            0
            sage: K.gen().euclidean_degree()
            0
            sage: K.zero().euclidean_degree()
            Traceback (most recent call last):
            ...
            ValueError: euclidean degree not defined for the zero element

        For a ring which is not a field, this is the valuation of the element::

            sage: R = Zp(2)
            sage: R.one().euclidean_degree()
            0
            sage: R.gen().euclidean_degree()
            1
            sage: R.zero().euclidean_degree()
            Traceback (most recent call last):
            ...
            ValueError: euclidean degree not defined for the zero element"""
    @overload
    def euclidean_degree(self) -> Any:
        """LocalGenericElement.euclidean_degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 871)

        Return the degree of this element as an element of a Euclidean domain.

        EXAMPLES:

        For a field, this is always zero except for the zero element::

            sage: K = Qp(2)
            sage: K.one().euclidean_degree()
            0
            sage: K.gen().euclidean_degree()
            0
            sage: K.zero().euclidean_degree()
            Traceback (most recent call last):
            ...
            ValueError: euclidean degree not defined for the zero element

        For a ring which is not a field, this is the valuation of the element::

            sage: R = Zp(2)
            sage: R.one().euclidean_degree()
            0
            sage: R.gen().euclidean_degree()
            1
            sage: R.zero().euclidean_degree()
            Traceback (most recent call last):
            ...
            ValueError: euclidean degree not defined for the zero element"""
    @overload
    def euclidean_degree(self) -> Any:
        """LocalGenericElement.euclidean_degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 871)

        Return the degree of this element as an element of a Euclidean domain.

        EXAMPLES:

        For a field, this is always zero except for the zero element::

            sage: K = Qp(2)
            sage: K.one().euclidean_degree()
            0
            sage: K.gen().euclidean_degree()
            0
            sage: K.zero().euclidean_degree()
            Traceback (most recent call last):
            ...
            ValueError: euclidean degree not defined for the zero element

        For a ring which is not a field, this is the valuation of the element::

            sage: R = Zp(2)
            sage: R.one().euclidean_degree()
            0
            sage: R.gen().euclidean_degree()
            1
            sage: R.zero().euclidean_degree()
            Traceback (most recent call last):
            ...
            ValueError: euclidean degree not defined for the zero element"""
    @overload
    def euclidean_degree(self) -> Any:
        """LocalGenericElement.euclidean_degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 871)

        Return the degree of this element as an element of a Euclidean domain.

        EXAMPLES:

        For a field, this is always zero except for the zero element::

            sage: K = Qp(2)
            sage: K.one().euclidean_degree()
            0
            sage: K.gen().euclidean_degree()
            0
            sage: K.zero().euclidean_degree()
            Traceback (most recent call last):
            ...
            ValueError: euclidean degree not defined for the zero element

        For a ring which is not a field, this is the valuation of the element::

            sage: R = Zp(2)
            sage: R.one().euclidean_degree()
            0
            sage: R.gen().euclidean_degree()
            1
            sage: R.zero().euclidean_degree()
            Traceback (most recent call last):
            ...
            ValueError: euclidean degree not defined for the zero element"""
    @overload
    def euclidean_degree(self) -> Any:
        """LocalGenericElement.euclidean_degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 871)

        Return the degree of this element as an element of a Euclidean domain.

        EXAMPLES:

        For a field, this is always zero except for the zero element::

            sage: K = Qp(2)
            sage: K.one().euclidean_degree()
            0
            sage: K.gen().euclidean_degree()
            0
            sage: K.zero().euclidean_degree()
            Traceback (most recent call last):
            ...
            ValueError: euclidean degree not defined for the zero element

        For a ring which is not a field, this is the valuation of the element::

            sage: R = Zp(2)
            sage: R.one().euclidean_degree()
            0
            sage: R.gen().euclidean_degree()
            1
            sage: R.zero().euclidean_degree()
            Traceback (most recent call last):
            ...
            ValueError: euclidean degree not defined for the zero element"""
    @overload
    def euclidean_degree(self) -> Any:
        """LocalGenericElement.euclidean_degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 871)

        Return the degree of this element as an element of a Euclidean domain.

        EXAMPLES:

        For a field, this is always zero except for the zero element::

            sage: K = Qp(2)
            sage: K.one().euclidean_degree()
            0
            sage: K.gen().euclidean_degree()
            0
            sage: K.zero().euclidean_degree()
            Traceback (most recent call last):
            ...
            ValueError: euclidean degree not defined for the zero element

        For a ring which is not a field, this is the valuation of the element::

            sage: R = Zp(2)
            sage: R.one().euclidean_degree()
            0
            sage: R.gen().euclidean_degree()
            1
            sage: R.zero().euclidean_degree()
            Traceback (most recent call last):
            ...
            ValueError: euclidean degree not defined for the zero element"""
    @overload
    def euclidean_degree(self) -> Any:
        """LocalGenericElement.euclidean_degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 871)

        Return the degree of this element as an element of a Euclidean domain.

        EXAMPLES:

        For a field, this is always zero except for the zero element::

            sage: K = Qp(2)
            sage: K.one().euclidean_degree()
            0
            sage: K.gen().euclidean_degree()
            0
            sage: K.zero().euclidean_degree()
            Traceback (most recent call last):
            ...
            ValueError: euclidean degree not defined for the zero element

        For a ring which is not a field, this is the valuation of the element::

            sage: R = Zp(2)
            sage: R.one().euclidean_degree()
            0
            sage: R.gen().euclidean_degree()
            1
            sage: R.zero().euclidean_degree()
            Traceback (most recent call last):
            ...
            ValueError: euclidean degree not defined for the zero element"""
    @overload
    def inverse_of_unit(self) -> Any:
        """LocalGenericElement.inverse_of_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 64)

        Return the inverse of ``self`` if ``self`` is a unit.

        OUTPUT: an element in the same ring as ``self``

        EXAMPLES::

            sage: R = ZpCA(3,5)
            sage: a = R(2); a
            2 + O(3^5)
            sage: b = a.inverse_of_unit(); b
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)

        A :exc:`ZeroDivisionError` is raised if an element has no inverse in the
        ring::

            sage: R(3).inverse_of_unit()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: inverse of 3 + O(3^5) does not exist

        Unlike the usual inverse of an element, the result is in the same ring
        as ``self`` and not just in its fraction field::

            sage: c = ~a; c
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: a.parent()
            3-adic Ring with capped absolute precision 5
            sage: b.parent()
            3-adic Ring with capped absolute precision 5
            sage: c.parent()
            3-adic Field with capped relative precision 5

        For fields this does of course not make any difference::

            sage: R = QpCR(3,5)
            sage: a = R(2)
            sage: b = a.inverse_of_unit()
            sage: c = ~a
            sage: a.parent()
            3-adic Field with capped relative precision 5
            sage: b.parent()
            3-adic Field with capped relative precision 5
            sage: c.parent()
            3-adic Field with capped relative precision 5

        TESTS:

        Test that this works for all kinds of `p`-adic base elements::

            sage: ZpCA(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: ZpCR(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: ZpFM(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4
            sage: ZpFP(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4
            sage: QpCR(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)

        Over unramified extensions::


            sage: # needs sage.libs.ntl
            sage: R = ZpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)
            sage: R = QpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)

            sage: # needs sage.libs.flint
            sage: R = ZpCA(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)
            sage: R = ZpFM(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4
            sage: R = ZpFP(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4


        Over Eisenstein extensions::

            sage: # needs sage.libs.ntl
            sage: R = ZpCA(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)
            sage: R = ZpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)
            sage: R = ZpFM(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9
            sage: R = QpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)"""
    @overload
    def inverse_of_unit(self) -> Any:
        """LocalGenericElement.inverse_of_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 64)

        Return the inverse of ``self`` if ``self`` is a unit.

        OUTPUT: an element in the same ring as ``self``

        EXAMPLES::

            sage: R = ZpCA(3,5)
            sage: a = R(2); a
            2 + O(3^5)
            sage: b = a.inverse_of_unit(); b
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)

        A :exc:`ZeroDivisionError` is raised if an element has no inverse in the
        ring::

            sage: R(3).inverse_of_unit()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: inverse of 3 + O(3^5) does not exist

        Unlike the usual inverse of an element, the result is in the same ring
        as ``self`` and not just in its fraction field::

            sage: c = ~a; c
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: a.parent()
            3-adic Ring with capped absolute precision 5
            sage: b.parent()
            3-adic Ring with capped absolute precision 5
            sage: c.parent()
            3-adic Field with capped relative precision 5

        For fields this does of course not make any difference::

            sage: R = QpCR(3,5)
            sage: a = R(2)
            sage: b = a.inverse_of_unit()
            sage: c = ~a
            sage: a.parent()
            3-adic Field with capped relative precision 5
            sage: b.parent()
            3-adic Field with capped relative precision 5
            sage: c.parent()
            3-adic Field with capped relative precision 5

        TESTS:

        Test that this works for all kinds of `p`-adic base elements::

            sage: ZpCA(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: ZpCR(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: ZpFM(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4
            sage: ZpFP(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4
            sage: QpCR(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)

        Over unramified extensions::


            sage: # needs sage.libs.ntl
            sage: R = ZpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)
            sage: R = QpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)

            sage: # needs sage.libs.flint
            sage: R = ZpCA(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)
            sage: R = ZpFM(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4
            sage: R = ZpFP(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4


        Over Eisenstein extensions::

            sage: # needs sage.libs.ntl
            sage: R = ZpCA(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)
            sage: R = ZpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)
            sage: R = ZpFM(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9
            sage: R = QpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)"""
    @overload
    def inverse_of_unit(self) -> Any:
        """LocalGenericElement.inverse_of_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 64)

        Return the inverse of ``self`` if ``self`` is a unit.

        OUTPUT: an element in the same ring as ``self``

        EXAMPLES::

            sage: R = ZpCA(3,5)
            sage: a = R(2); a
            2 + O(3^5)
            sage: b = a.inverse_of_unit(); b
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)

        A :exc:`ZeroDivisionError` is raised if an element has no inverse in the
        ring::

            sage: R(3).inverse_of_unit()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: inverse of 3 + O(3^5) does not exist

        Unlike the usual inverse of an element, the result is in the same ring
        as ``self`` and not just in its fraction field::

            sage: c = ~a; c
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: a.parent()
            3-adic Ring with capped absolute precision 5
            sage: b.parent()
            3-adic Ring with capped absolute precision 5
            sage: c.parent()
            3-adic Field with capped relative precision 5

        For fields this does of course not make any difference::

            sage: R = QpCR(3,5)
            sage: a = R(2)
            sage: b = a.inverse_of_unit()
            sage: c = ~a
            sage: a.parent()
            3-adic Field with capped relative precision 5
            sage: b.parent()
            3-adic Field with capped relative precision 5
            sage: c.parent()
            3-adic Field with capped relative precision 5

        TESTS:

        Test that this works for all kinds of `p`-adic base elements::

            sage: ZpCA(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: ZpCR(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: ZpFM(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4
            sage: ZpFP(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4
            sage: QpCR(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)

        Over unramified extensions::


            sage: # needs sage.libs.ntl
            sage: R = ZpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)
            sage: R = QpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)

            sage: # needs sage.libs.flint
            sage: R = ZpCA(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)
            sage: R = ZpFM(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4
            sage: R = ZpFP(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4


        Over Eisenstein extensions::

            sage: # needs sage.libs.ntl
            sage: R = ZpCA(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)
            sage: R = ZpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)
            sage: R = ZpFM(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9
            sage: R = QpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)"""
    @overload
    def inverse_of_unit(self) -> Any:
        """LocalGenericElement.inverse_of_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 64)

        Return the inverse of ``self`` if ``self`` is a unit.

        OUTPUT: an element in the same ring as ``self``

        EXAMPLES::

            sage: R = ZpCA(3,5)
            sage: a = R(2); a
            2 + O(3^5)
            sage: b = a.inverse_of_unit(); b
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)

        A :exc:`ZeroDivisionError` is raised if an element has no inverse in the
        ring::

            sage: R(3).inverse_of_unit()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: inverse of 3 + O(3^5) does not exist

        Unlike the usual inverse of an element, the result is in the same ring
        as ``self`` and not just in its fraction field::

            sage: c = ~a; c
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: a.parent()
            3-adic Ring with capped absolute precision 5
            sage: b.parent()
            3-adic Ring with capped absolute precision 5
            sage: c.parent()
            3-adic Field with capped relative precision 5

        For fields this does of course not make any difference::

            sage: R = QpCR(3,5)
            sage: a = R(2)
            sage: b = a.inverse_of_unit()
            sage: c = ~a
            sage: a.parent()
            3-adic Field with capped relative precision 5
            sage: b.parent()
            3-adic Field with capped relative precision 5
            sage: c.parent()
            3-adic Field with capped relative precision 5

        TESTS:

        Test that this works for all kinds of `p`-adic base elements::

            sage: ZpCA(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: ZpCR(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: ZpFM(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4
            sage: ZpFP(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4
            sage: QpCR(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)

        Over unramified extensions::


            sage: # needs sage.libs.ntl
            sage: R = ZpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)
            sage: R = QpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)

            sage: # needs sage.libs.flint
            sage: R = ZpCA(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)
            sage: R = ZpFM(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4
            sage: R = ZpFP(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4


        Over Eisenstein extensions::

            sage: # needs sage.libs.ntl
            sage: R = ZpCA(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)
            sage: R = ZpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)
            sage: R = ZpFM(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9
            sage: R = QpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)"""
    @overload
    def inverse_of_unit(self) -> Any:
        """LocalGenericElement.inverse_of_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 64)

        Return the inverse of ``self`` if ``self`` is a unit.

        OUTPUT: an element in the same ring as ``self``

        EXAMPLES::

            sage: R = ZpCA(3,5)
            sage: a = R(2); a
            2 + O(3^5)
            sage: b = a.inverse_of_unit(); b
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)

        A :exc:`ZeroDivisionError` is raised if an element has no inverse in the
        ring::

            sage: R(3).inverse_of_unit()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: inverse of 3 + O(3^5) does not exist

        Unlike the usual inverse of an element, the result is in the same ring
        as ``self`` and not just in its fraction field::

            sage: c = ~a; c
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: a.parent()
            3-adic Ring with capped absolute precision 5
            sage: b.parent()
            3-adic Ring with capped absolute precision 5
            sage: c.parent()
            3-adic Field with capped relative precision 5

        For fields this does of course not make any difference::

            sage: R = QpCR(3,5)
            sage: a = R(2)
            sage: b = a.inverse_of_unit()
            sage: c = ~a
            sage: a.parent()
            3-adic Field with capped relative precision 5
            sage: b.parent()
            3-adic Field with capped relative precision 5
            sage: c.parent()
            3-adic Field with capped relative precision 5

        TESTS:

        Test that this works for all kinds of `p`-adic base elements::

            sage: ZpCA(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: ZpCR(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: ZpFM(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4
            sage: ZpFP(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4
            sage: QpCR(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)

        Over unramified extensions::


            sage: # needs sage.libs.ntl
            sage: R = ZpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)
            sage: R = QpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)

            sage: # needs sage.libs.flint
            sage: R = ZpCA(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)
            sage: R = ZpFM(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4
            sage: R = ZpFP(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4


        Over Eisenstein extensions::

            sage: # needs sage.libs.ntl
            sage: R = ZpCA(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)
            sage: R = ZpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)
            sage: R = ZpFM(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9
            sage: R = QpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)"""
    @overload
    def inverse_of_unit(self) -> Any:
        """LocalGenericElement.inverse_of_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 64)

        Return the inverse of ``self`` if ``self`` is a unit.

        OUTPUT: an element in the same ring as ``self``

        EXAMPLES::

            sage: R = ZpCA(3,5)
            sage: a = R(2); a
            2 + O(3^5)
            sage: b = a.inverse_of_unit(); b
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)

        A :exc:`ZeroDivisionError` is raised if an element has no inverse in the
        ring::

            sage: R(3).inverse_of_unit()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: inverse of 3 + O(3^5) does not exist

        Unlike the usual inverse of an element, the result is in the same ring
        as ``self`` and not just in its fraction field::

            sage: c = ~a; c
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: a.parent()
            3-adic Ring with capped absolute precision 5
            sage: b.parent()
            3-adic Ring with capped absolute precision 5
            sage: c.parent()
            3-adic Field with capped relative precision 5

        For fields this does of course not make any difference::

            sage: R = QpCR(3,5)
            sage: a = R(2)
            sage: b = a.inverse_of_unit()
            sage: c = ~a
            sage: a.parent()
            3-adic Field with capped relative precision 5
            sage: b.parent()
            3-adic Field with capped relative precision 5
            sage: c.parent()
            3-adic Field with capped relative precision 5

        TESTS:

        Test that this works for all kinds of `p`-adic base elements::

            sage: ZpCA(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: ZpCR(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: ZpFM(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4
            sage: ZpFP(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4
            sage: QpCR(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)

        Over unramified extensions::


            sage: # needs sage.libs.ntl
            sage: R = ZpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)
            sage: R = QpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)

            sage: # needs sage.libs.flint
            sage: R = ZpCA(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)
            sage: R = ZpFM(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4
            sage: R = ZpFP(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4


        Over Eisenstein extensions::

            sage: # needs sage.libs.ntl
            sage: R = ZpCA(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)
            sage: R = ZpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)
            sage: R = ZpFM(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9
            sage: R = QpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)"""
    @overload
    def inverse_of_unit(self) -> Any:
        """LocalGenericElement.inverse_of_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 64)

        Return the inverse of ``self`` if ``self`` is a unit.

        OUTPUT: an element in the same ring as ``self``

        EXAMPLES::

            sage: R = ZpCA(3,5)
            sage: a = R(2); a
            2 + O(3^5)
            sage: b = a.inverse_of_unit(); b
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)

        A :exc:`ZeroDivisionError` is raised if an element has no inverse in the
        ring::

            sage: R(3).inverse_of_unit()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: inverse of 3 + O(3^5) does not exist

        Unlike the usual inverse of an element, the result is in the same ring
        as ``self`` and not just in its fraction field::

            sage: c = ~a; c
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: a.parent()
            3-adic Ring with capped absolute precision 5
            sage: b.parent()
            3-adic Ring with capped absolute precision 5
            sage: c.parent()
            3-adic Field with capped relative precision 5

        For fields this does of course not make any difference::

            sage: R = QpCR(3,5)
            sage: a = R(2)
            sage: b = a.inverse_of_unit()
            sage: c = ~a
            sage: a.parent()
            3-adic Field with capped relative precision 5
            sage: b.parent()
            3-adic Field with capped relative precision 5
            sage: c.parent()
            3-adic Field with capped relative precision 5

        TESTS:

        Test that this works for all kinds of `p`-adic base elements::

            sage: ZpCA(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: ZpCR(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: ZpFM(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4
            sage: ZpFP(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4
            sage: QpCR(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)

        Over unramified extensions::


            sage: # needs sage.libs.ntl
            sage: R = ZpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)
            sage: R = QpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)

            sage: # needs sage.libs.flint
            sage: R = ZpCA(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)
            sage: R = ZpFM(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4
            sage: R = ZpFP(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4


        Over Eisenstein extensions::

            sage: # needs sage.libs.ntl
            sage: R = ZpCA(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)
            sage: R = ZpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)
            sage: R = ZpFM(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9
            sage: R = QpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)"""
    @overload
    def inverse_of_unit(self) -> Any:
        """LocalGenericElement.inverse_of_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 64)

        Return the inverse of ``self`` if ``self`` is a unit.

        OUTPUT: an element in the same ring as ``self``

        EXAMPLES::

            sage: R = ZpCA(3,5)
            sage: a = R(2); a
            2 + O(3^5)
            sage: b = a.inverse_of_unit(); b
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)

        A :exc:`ZeroDivisionError` is raised if an element has no inverse in the
        ring::

            sage: R(3).inverse_of_unit()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: inverse of 3 + O(3^5) does not exist

        Unlike the usual inverse of an element, the result is in the same ring
        as ``self`` and not just in its fraction field::

            sage: c = ~a; c
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: a.parent()
            3-adic Ring with capped absolute precision 5
            sage: b.parent()
            3-adic Ring with capped absolute precision 5
            sage: c.parent()
            3-adic Field with capped relative precision 5

        For fields this does of course not make any difference::

            sage: R = QpCR(3,5)
            sage: a = R(2)
            sage: b = a.inverse_of_unit()
            sage: c = ~a
            sage: a.parent()
            3-adic Field with capped relative precision 5
            sage: b.parent()
            3-adic Field with capped relative precision 5
            sage: c.parent()
            3-adic Field with capped relative precision 5

        TESTS:

        Test that this works for all kinds of `p`-adic base elements::

            sage: ZpCA(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: ZpCR(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: ZpFM(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4
            sage: ZpFP(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4
            sage: QpCR(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)

        Over unramified extensions::


            sage: # needs sage.libs.ntl
            sage: R = ZpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)
            sage: R = QpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)

            sage: # needs sage.libs.flint
            sage: R = ZpCA(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)
            sage: R = ZpFM(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4
            sage: R = ZpFP(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4


        Over Eisenstein extensions::

            sage: # needs sage.libs.ntl
            sage: R = ZpCA(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)
            sage: R = ZpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)
            sage: R = ZpFM(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9
            sage: R = QpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)"""
    @overload
    def inverse_of_unit(self) -> Any:
        """LocalGenericElement.inverse_of_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 64)

        Return the inverse of ``self`` if ``self`` is a unit.

        OUTPUT: an element in the same ring as ``self``

        EXAMPLES::

            sage: R = ZpCA(3,5)
            sage: a = R(2); a
            2 + O(3^5)
            sage: b = a.inverse_of_unit(); b
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)

        A :exc:`ZeroDivisionError` is raised if an element has no inverse in the
        ring::

            sage: R(3).inverse_of_unit()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: inverse of 3 + O(3^5) does not exist

        Unlike the usual inverse of an element, the result is in the same ring
        as ``self`` and not just in its fraction field::

            sage: c = ~a; c
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: a.parent()
            3-adic Ring with capped absolute precision 5
            sage: b.parent()
            3-adic Ring with capped absolute precision 5
            sage: c.parent()
            3-adic Field with capped relative precision 5

        For fields this does of course not make any difference::

            sage: R = QpCR(3,5)
            sage: a = R(2)
            sage: b = a.inverse_of_unit()
            sage: c = ~a
            sage: a.parent()
            3-adic Field with capped relative precision 5
            sage: b.parent()
            3-adic Field with capped relative precision 5
            sage: c.parent()
            3-adic Field with capped relative precision 5

        TESTS:

        Test that this works for all kinds of `p`-adic base elements::

            sage: ZpCA(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: ZpCR(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: ZpFM(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4
            sage: ZpFP(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4
            sage: QpCR(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)

        Over unramified extensions::


            sage: # needs sage.libs.ntl
            sage: R = ZpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)
            sage: R = QpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)

            sage: # needs sage.libs.flint
            sage: R = ZpCA(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)
            sage: R = ZpFM(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4
            sage: R = ZpFP(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4


        Over Eisenstein extensions::

            sage: # needs sage.libs.ntl
            sage: R = ZpCA(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)
            sage: R = ZpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)
            sage: R = ZpFM(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9
            sage: R = QpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)"""
    @overload
    def inverse_of_unit(self) -> Any:
        """LocalGenericElement.inverse_of_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 64)

        Return the inverse of ``self`` if ``self`` is a unit.

        OUTPUT: an element in the same ring as ``self``

        EXAMPLES::

            sage: R = ZpCA(3,5)
            sage: a = R(2); a
            2 + O(3^5)
            sage: b = a.inverse_of_unit(); b
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)

        A :exc:`ZeroDivisionError` is raised if an element has no inverse in the
        ring::

            sage: R(3).inverse_of_unit()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: inverse of 3 + O(3^5) does not exist

        Unlike the usual inverse of an element, the result is in the same ring
        as ``self`` and not just in its fraction field::

            sage: c = ~a; c
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: a.parent()
            3-adic Ring with capped absolute precision 5
            sage: b.parent()
            3-adic Ring with capped absolute precision 5
            sage: c.parent()
            3-adic Field with capped relative precision 5

        For fields this does of course not make any difference::

            sage: R = QpCR(3,5)
            sage: a = R(2)
            sage: b = a.inverse_of_unit()
            sage: c = ~a
            sage: a.parent()
            3-adic Field with capped relative precision 5
            sage: b.parent()
            3-adic Field with capped relative precision 5
            sage: c.parent()
            3-adic Field with capped relative precision 5

        TESTS:

        Test that this works for all kinds of `p`-adic base elements::

            sage: ZpCA(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: ZpCR(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: ZpFM(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4
            sage: ZpFP(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4
            sage: QpCR(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)

        Over unramified extensions::


            sage: # needs sage.libs.ntl
            sage: R = ZpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)
            sage: R = QpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)

            sage: # needs sage.libs.flint
            sage: R = ZpCA(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)
            sage: R = ZpFM(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4
            sage: R = ZpFP(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4


        Over Eisenstein extensions::

            sage: # needs sage.libs.ntl
            sage: R = ZpCA(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)
            sage: R = ZpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)
            sage: R = ZpFM(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9
            sage: R = QpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)"""
    @overload
    def inverse_of_unit(self) -> Any:
        """LocalGenericElement.inverse_of_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 64)

        Return the inverse of ``self`` if ``self`` is a unit.

        OUTPUT: an element in the same ring as ``self``

        EXAMPLES::

            sage: R = ZpCA(3,5)
            sage: a = R(2); a
            2 + O(3^5)
            sage: b = a.inverse_of_unit(); b
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)

        A :exc:`ZeroDivisionError` is raised if an element has no inverse in the
        ring::

            sage: R(3).inverse_of_unit()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: inverse of 3 + O(3^5) does not exist

        Unlike the usual inverse of an element, the result is in the same ring
        as ``self`` and not just in its fraction field::

            sage: c = ~a; c
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: a.parent()
            3-adic Ring with capped absolute precision 5
            sage: b.parent()
            3-adic Ring with capped absolute precision 5
            sage: c.parent()
            3-adic Field with capped relative precision 5

        For fields this does of course not make any difference::

            sage: R = QpCR(3,5)
            sage: a = R(2)
            sage: b = a.inverse_of_unit()
            sage: c = ~a
            sage: a.parent()
            3-adic Field with capped relative precision 5
            sage: b.parent()
            3-adic Field with capped relative precision 5
            sage: c.parent()
            3-adic Field with capped relative precision 5

        TESTS:

        Test that this works for all kinds of `p`-adic base elements::

            sage: ZpCA(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: ZpCR(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: ZpFM(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4
            sage: ZpFP(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4
            sage: QpCR(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)

        Over unramified extensions::


            sage: # needs sage.libs.ntl
            sage: R = ZpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)
            sage: R = QpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)

            sage: # needs sage.libs.flint
            sage: R = ZpCA(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)
            sage: R = ZpFM(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4
            sage: R = ZpFP(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4


        Over Eisenstein extensions::

            sage: # needs sage.libs.ntl
            sage: R = ZpCA(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)
            sage: R = ZpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)
            sage: R = ZpFM(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9
            sage: R = QpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)"""
    @overload
    def inverse_of_unit(self) -> Any:
        """LocalGenericElement.inverse_of_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 64)

        Return the inverse of ``self`` if ``self`` is a unit.

        OUTPUT: an element in the same ring as ``self``

        EXAMPLES::

            sage: R = ZpCA(3,5)
            sage: a = R(2); a
            2 + O(3^5)
            sage: b = a.inverse_of_unit(); b
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)

        A :exc:`ZeroDivisionError` is raised if an element has no inverse in the
        ring::

            sage: R(3).inverse_of_unit()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: inverse of 3 + O(3^5) does not exist

        Unlike the usual inverse of an element, the result is in the same ring
        as ``self`` and not just in its fraction field::

            sage: c = ~a; c
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: a.parent()
            3-adic Ring with capped absolute precision 5
            sage: b.parent()
            3-adic Ring with capped absolute precision 5
            sage: c.parent()
            3-adic Field with capped relative precision 5

        For fields this does of course not make any difference::

            sage: R = QpCR(3,5)
            sage: a = R(2)
            sage: b = a.inverse_of_unit()
            sage: c = ~a
            sage: a.parent()
            3-adic Field with capped relative precision 5
            sage: b.parent()
            3-adic Field with capped relative precision 5
            sage: c.parent()
            3-adic Field with capped relative precision 5

        TESTS:

        Test that this works for all kinds of `p`-adic base elements::

            sage: ZpCA(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: ZpCR(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: ZpFM(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4
            sage: ZpFP(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4
            sage: QpCR(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)

        Over unramified extensions::


            sage: # needs sage.libs.ntl
            sage: R = ZpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)
            sage: R = QpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)

            sage: # needs sage.libs.flint
            sage: R = ZpCA(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)
            sage: R = ZpFM(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4
            sage: R = ZpFP(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4


        Over Eisenstein extensions::

            sage: # needs sage.libs.ntl
            sage: R = ZpCA(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)
            sage: R = ZpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)
            sage: R = ZpFM(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9
            sage: R = QpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)"""
    @overload
    def inverse_of_unit(self) -> Any:
        """LocalGenericElement.inverse_of_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 64)

        Return the inverse of ``self`` if ``self`` is a unit.

        OUTPUT: an element in the same ring as ``self``

        EXAMPLES::

            sage: R = ZpCA(3,5)
            sage: a = R(2); a
            2 + O(3^5)
            sage: b = a.inverse_of_unit(); b
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)

        A :exc:`ZeroDivisionError` is raised if an element has no inverse in the
        ring::

            sage: R(3).inverse_of_unit()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: inverse of 3 + O(3^5) does not exist

        Unlike the usual inverse of an element, the result is in the same ring
        as ``self`` and not just in its fraction field::

            sage: c = ~a; c
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: a.parent()
            3-adic Ring with capped absolute precision 5
            sage: b.parent()
            3-adic Ring with capped absolute precision 5
            sage: c.parent()
            3-adic Field with capped relative precision 5

        For fields this does of course not make any difference::

            sage: R = QpCR(3,5)
            sage: a = R(2)
            sage: b = a.inverse_of_unit()
            sage: c = ~a
            sage: a.parent()
            3-adic Field with capped relative precision 5
            sage: b.parent()
            3-adic Field with capped relative precision 5
            sage: c.parent()
            3-adic Field with capped relative precision 5

        TESTS:

        Test that this works for all kinds of `p`-adic base elements::

            sage: ZpCA(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: ZpCR(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: ZpFM(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4
            sage: ZpFP(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4
            sage: QpCR(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)

        Over unramified extensions::


            sage: # needs sage.libs.ntl
            sage: R = ZpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)
            sage: R = QpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)

            sage: # needs sage.libs.flint
            sage: R = ZpCA(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)
            sage: R = ZpFM(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4
            sage: R = ZpFP(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4


        Over Eisenstein extensions::

            sage: # needs sage.libs.ntl
            sage: R = ZpCA(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)
            sage: R = ZpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)
            sage: R = ZpFM(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9
            sage: R = QpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)"""
    @overload
    def inverse_of_unit(self) -> Any:
        """LocalGenericElement.inverse_of_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 64)

        Return the inverse of ``self`` if ``self`` is a unit.

        OUTPUT: an element in the same ring as ``self``

        EXAMPLES::

            sage: R = ZpCA(3,5)
            sage: a = R(2); a
            2 + O(3^5)
            sage: b = a.inverse_of_unit(); b
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)

        A :exc:`ZeroDivisionError` is raised if an element has no inverse in the
        ring::

            sage: R(3).inverse_of_unit()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: inverse of 3 + O(3^5) does not exist

        Unlike the usual inverse of an element, the result is in the same ring
        as ``self`` and not just in its fraction field::

            sage: c = ~a; c
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: a.parent()
            3-adic Ring with capped absolute precision 5
            sage: b.parent()
            3-adic Ring with capped absolute precision 5
            sage: c.parent()
            3-adic Field with capped relative precision 5

        For fields this does of course not make any difference::

            sage: R = QpCR(3,5)
            sage: a = R(2)
            sage: b = a.inverse_of_unit()
            sage: c = ~a
            sage: a.parent()
            3-adic Field with capped relative precision 5
            sage: b.parent()
            3-adic Field with capped relative precision 5
            sage: c.parent()
            3-adic Field with capped relative precision 5

        TESTS:

        Test that this works for all kinds of `p`-adic base elements::

            sage: ZpCA(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: ZpCR(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: ZpFM(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4
            sage: ZpFP(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4
            sage: QpCR(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)

        Over unramified extensions::


            sage: # needs sage.libs.ntl
            sage: R = ZpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)
            sage: R = QpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)

            sage: # needs sage.libs.flint
            sage: R = ZpCA(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)
            sage: R = ZpFM(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4
            sage: R = ZpFP(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4


        Over Eisenstein extensions::

            sage: # needs sage.libs.ntl
            sage: R = ZpCA(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)
            sage: R = ZpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)
            sage: R = ZpFM(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9
            sage: R = QpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)"""
    @overload
    def inverse_of_unit(self) -> Any:
        """LocalGenericElement.inverse_of_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 64)

        Return the inverse of ``self`` if ``self`` is a unit.

        OUTPUT: an element in the same ring as ``self``

        EXAMPLES::

            sage: R = ZpCA(3,5)
            sage: a = R(2); a
            2 + O(3^5)
            sage: b = a.inverse_of_unit(); b
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)

        A :exc:`ZeroDivisionError` is raised if an element has no inverse in the
        ring::

            sage: R(3).inverse_of_unit()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: inverse of 3 + O(3^5) does not exist

        Unlike the usual inverse of an element, the result is in the same ring
        as ``self`` and not just in its fraction field::

            sage: c = ~a; c
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: a.parent()
            3-adic Ring with capped absolute precision 5
            sage: b.parent()
            3-adic Ring with capped absolute precision 5
            sage: c.parent()
            3-adic Field with capped relative precision 5

        For fields this does of course not make any difference::

            sage: R = QpCR(3,5)
            sage: a = R(2)
            sage: b = a.inverse_of_unit()
            sage: c = ~a
            sage: a.parent()
            3-adic Field with capped relative precision 5
            sage: b.parent()
            3-adic Field with capped relative precision 5
            sage: c.parent()
            3-adic Field with capped relative precision 5

        TESTS:

        Test that this works for all kinds of `p`-adic base elements::

            sage: ZpCA(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: ZpCR(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: ZpFM(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4
            sage: ZpFP(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4
            sage: QpCR(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)

        Over unramified extensions::


            sage: # needs sage.libs.ntl
            sage: R = ZpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)
            sage: R = QpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)

            sage: # needs sage.libs.flint
            sage: R = ZpCA(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)
            sage: R = ZpFM(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4
            sage: R = ZpFP(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4


        Over Eisenstein extensions::

            sage: # needs sage.libs.ntl
            sage: R = ZpCA(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)
            sage: R = ZpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)
            sage: R = ZpFM(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9
            sage: R = QpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)"""
    @overload
    def inverse_of_unit(self) -> Any:
        """LocalGenericElement.inverse_of_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 64)

        Return the inverse of ``self`` if ``self`` is a unit.

        OUTPUT: an element in the same ring as ``self``

        EXAMPLES::

            sage: R = ZpCA(3,5)
            sage: a = R(2); a
            2 + O(3^5)
            sage: b = a.inverse_of_unit(); b
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)

        A :exc:`ZeroDivisionError` is raised if an element has no inverse in the
        ring::

            sage: R(3).inverse_of_unit()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: inverse of 3 + O(3^5) does not exist

        Unlike the usual inverse of an element, the result is in the same ring
        as ``self`` and not just in its fraction field::

            sage: c = ~a; c
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: a.parent()
            3-adic Ring with capped absolute precision 5
            sage: b.parent()
            3-adic Ring with capped absolute precision 5
            sage: c.parent()
            3-adic Field with capped relative precision 5

        For fields this does of course not make any difference::

            sage: R = QpCR(3,5)
            sage: a = R(2)
            sage: b = a.inverse_of_unit()
            sage: c = ~a
            sage: a.parent()
            3-adic Field with capped relative precision 5
            sage: b.parent()
            3-adic Field with capped relative precision 5
            sage: c.parent()
            3-adic Field with capped relative precision 5

        TESTS:

        Test that this works for all kinds of `p`-adic base elements::

            sage: ZpCA(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: ZpCR(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: ZpFM(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4
            sage: ZpFP(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4
            sage: QpCR(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)

        Over unramified extensions::


            sage: # needs sage.libs.ntl
            sage: R = ZpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)
            sage: R = QpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)

            sage: # needs sage.libs.flint
            sage: R = ZpCA(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)
            sage: R = ZpFM(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4
            sage: R = ZpFP(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4


        Over Eisenstein extensions::

            sage: # needs sage.libs.ntl
            sage: R = ZpCA(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)
            sage: R = ZpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)
            sage: R = ZpFM(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9
            sage: R = QpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)"""
    @overload
    def inverse_of_unit(self) -> Any:
        """LocalGenericElement.inverse_of_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 64)

        Return the inverse of ``self`` if ``self`` is a unit.

        OUTPUT: an element in the same ring as ``self``

        EXAMPLES::

            sage: R = ZpCA(3,5)
            sage: a = R(2); a
            2 + O(3^5)
            sage: b = a.inverse_of_unit(); b
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)

        A :exc:`ZeroDivisionError` is raised if an element has no inverse in the
        ring::

            sage: R(3).inverse_of_unit()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: inverse of 3 + O(3^5) does not exist

        Unlike the usual inverse of an element, the result is in the same ring
        as ``self`` and not just in its fraction field::

            sage: c = ~a; c
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: a.parent()
            3-adic Ring with capped absolute precision 5
            sage: b.parent()
            3-adic Ring with capped absolute precision 5
            sage: c.parent()
            3-adic Field with capped relative precision 5

        For fields this does of course not make any difference::

            sage: R = QpCR(3,5)
            sage: a = R(2)
            sage: b = a.inverse_of_unit()
            sage: c = ~a
            sage: a.parent()
            3-adic Field with capped relative precision 5
            sage: b.parent()
            3-adic Field with capped relative precision 5
            sage: c.parent()
            3-adic Field with capped relative precision 5

        TESTS:

        Test that this works for all kinds of `p`-adic base elements::

            sage: ZpCA(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: ZpCR(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: ZpFM(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4
            sage: ZpFP(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4
            sage: QpCR(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)

        Over unramified extensions::


            sage: # needs sage.libs.ntl
            sage: R = ZpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)
            sage: R = QpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)

            sage: # needs sage.libs.flint
            sage: R = ZpCA(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)
            sage: R = ZpFM(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4
            sage: R = ZpFP(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4


        Over Eisenstein extensions::

            sage: # needs sage.libs.ntl
            sage: R = ZpCA(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)
            sage: R = ZpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)
            sage: R = ZpFM(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9
            sage: R = QpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)"""
    @overload
    def inverse_of_unit(self) -> Any:
        """LocalGenericElement.inverse_of_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 64)

        Return the inverse of ``self`` if ``self`` is a unit.

        OUTPUT: an element in the same ring as ``self``

        EXAMPLES::

            sage: R = ZpCA(3,5)
            sage: a = R(2); a
            2 + O(3^5)
            sage: b = a.inverse_of_unit(); b
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)

        A :exc:`ZeroDivisionError` is raised if an element has no inverse in the
        ring::

            sage: R(3).inverse_of_unit()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: inverse of 3 + O(3^5) does not exist

        Unlike the usual inverse of an element, the result is in the same ring
        as ``self`` and not just in its fraction field::

            sage: c = ~a; c
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: a.parent()
            3-adic Ring with capped absolute precision 5
            sage: b.parent()
            3-adic Ring with capped absolute precision 5
            sage: c.parent()
            3-adic Field with capped relative precision 5

        For fields this does of course not make any difference::

            sage: R = QpCR(3,5)
            sage: a = R(2)
            sage: b = a.inverse_of_unit()
            sage: c = ~a
            sage: a.parent()
            3-adic Field with capped relative precision 5
            sage: b.parent()
            3-adic Field with capped relative precision 5
            sage: c.parent()
            3-adic Field with capped relative precision 5

        TESTS:

        Test that this works for all kinds of `p`-adic base elements::

            sage: ZpCA(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: ZpCR(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)
            sage: ZpFM(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4
            sage: ZpFP(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4
            sage: QpCR(3,5)(2).inverse_of_unit()
            2 + 3 + 3^2 + 3^3 + 3^4 + O(3^5)

        Over unramified extensions::


            sage: # needs sage.libs.ntl
            sage: R = ZpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)
            sage: R = QpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)

            sage: # needs sage.libs.flint
            sage: R = ZpCA(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4 + O(3^5)
            sage: R = ZpFM(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4
            sage: R = ZpFP(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 + 1 )
            sage: t.inverse_of_unit()
            2*t + 2*t*3 + 2*t*3^2 + 2*t*3^3 + 2*t*3^4


        Over Eisenstein extensions::

            sage: # needs sage.libs.ntl
            sage: R = ZpCA(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)
            sage: R = ZpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)
            sage: R = ZpFM(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9
            sage: R = QpCR(3,5); S.<t> = R[]; W.<t> = R.extension( t^2 - 3 )
            sage: (t - 1).inverse_of_unit()
            2 + 2*t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)"""
    @overload
    def is_integral(self) -> Any:
        """LocalGenericElement.is_integral(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 526)

        Return whether ``self`` is an integral element.

        INPUT:

        - ``self`` -- a local ring element

        OUTPUT: boolean; whether ``self`` is an integral element

        EXAMPLES::

            sage: R = Qp(3,20)
            sage: a = R(7/3); a.is_integral()
            False
            sage: b = R(7/5); b.is_integral()
            True"""
    @overload
    def is_integral(self) -> Any:
        """LocalGenericElement.is_integral(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 526)

        Return whether ``self`` is an integral element.

        INPUT:

        - ``self`` -- a local ring element

        OUTPUT: boolean; whether ``self`` is an integral element

        EXAMPLES::

            sage: R = Qp(3,20)
            sage: a = R(7/3); a.is_integral()
            False
            sage: b = R(7/5); b.is_integral()
            True"""
    @overload
    def is_integral(self) -> Any:
        """LocalGenericElement.is_integral(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 526)

        Return whether ``self`` is an integral element.

        INPUT:

        - ``self`` -- a local ring element

        OUTPUT: boolean; whether ``self`` is an integral element

        EXAMPLES::

            sage: R = Qp(3,20)
            sage: a = R(7/3); a.is_integral()
            False
            sage: b = R(7/5); b.is_integral()
            True"""
    @overload
    def is_padic_unit(self) -> Any:
        """LocalGenericElement.is_padic_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 549)

        Return whether ``self`` is a `p`-adic unit. That is, whether it has
        zero valuation.

        INPUT:

        - ``self`` -- a local ring element

        OUTPUT: boolean; whether ``self`` is a unit

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel'); K = Qp(3,20,'capped-rel')
            sage: R(0).is_padic_unit()
            False
            sage: R(1).is_padic_unit()
            True
            sage: R(2).is_padic_unit()
            True
            sage: R(3).is_padic_unit()
            False
            sage: Qp(5,5)(5).is_padic_unit()
            False

        TESTS::

            sage: R(4).is_padic_unit()
            True
            sage: R(6).is_padic_unit()
            False
            sage: R(9).is_padic_unit()
            False
            sage: K(0).is_padic_unit()
            False
            sage: K(1).is_padic_unit()
            True
            sage: K(2).is_padic_unit()
            True
            sage: K(3).is_padic_unit()
            False
            sage: K(4).is_padic_unit()
            True
            sage: K(6).is_padic_unit()
            False
            sage: K(9).is_padic_unit()
            False
            sage: K(1/3).is_padic_unit()
            False
            sage: K(1/9).is_padic_unit()
            False
            sage: Qq(3^2,5,names='a')(3).is_padic_unit()                                # needs sage.libs.ntl
            False"""
    @overload
    def is_padic_unit(self) -> Any:
        """LocalGenericElement.is_padic_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 549)

        Return whether ``self`` is a `p`-adic unit. That is, whether it has
        zero valuation.

        INPUT:

        - ``self`` -- a local ring element

        OUTPUT: boolean; whether ``self`` is a unit

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel'); K = Qp(3,20,'capped-rel')
            sage: R(0).is_padic_unit()
            False
            sage: R(1).is_padic_unit()
            True
            sage: R(2).is_padic_unit()
            True
            sage: R(3).is_padic_unit()
            False
            sage: Qp(5,5)(5).is_padic_unit()
            False

        TESTS::

            sage: R(4).is_padic_unit()
            True
            sage: R(6).is_padic_unit()
            False
            sage: R(9).is_padic_unit()
            False
            sage: K(0).is_padic_unit()
            False
            sage: K(1).is_padic_unit()
            True
            sage: K(2).is_padic_unit()
            True
            sage: K(3).is_padic_unit()
            False
            sage: K(4).is_padic_unit()
            True
            sage: K(6).is_padic_unit()
            False
            sage: K(9).is_padic_unit()
            False
            sage: K(1/3).is_padic_unit()
            False
            sage: K(1/9).is_padic_unit()
            False
            sage: Qq(3^2,5,names='a')(3).is_padic_unit()                                # needs sage.libs.ntl
            False"""
    @overload
    def is_padic_unit(self) -> Any:
        """LocalGenericElement.is_padic_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 549)

        Return whether ``self`` is a `p`-adic unit. That is, whether it has
        zero valuation.

        INPUT:

        - ``self`` -- a local ring element

        OUTPUT: boolean; whether ``self`` is a unit

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel'); K = Qp(3,20,'capped-rel')
            sage: R(0).is_padic_unit()
            False
            sage: R(1).is_padic_unit()
            True
            sage: R(2).is_padic_unit()
            True
            sage: R(3).is_padic_unit()
            False
            sage: Qp(5,5)(5).is_padic_unit()
            False

        TESTS::

            sage: R(4).is_padic_unit()
            True
            sage: R(6).is_padic_unit()
            False
            sage: R(9).is_padic_unit()
            False
            sage: K(0).is_padic_unit()
            False
            sage: K(1).is_padic_unit()
            True
            sage: K(2).is_padic_unit()
            True
            sage: K(3).is_padic_unit()
            False
            sage: K(4).is_padic_unit()
            True
            sage: K(6).is_padic_unit()
            False
            sage: K(9).is_padic_unit()
            False
            sage: K(1/3).is_padic_unit()
            False
            sage: K(1/9).is_padic_unit()
            False
            sage: Qq(3^2,5,names='a')(3).is_padic_unit()                                # needs sage.libs.ntl
            False"""
    @overload
    def is_padic_unit(self) -> Any:
        """LocalGenericElement.is_padic_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 549)

        Return whether ``self`` is a `p`-adic unit. That is, whether it has
        zero valuation.

        INPUT:

        - ``self`` -- a local ring element

        OUTPUT: boolean; whether ``self`` is a unit

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel'); K = Qp(3,20,'capped-rel')
            sage: R(0).is_padic_unit()
            False
            sage: R(1).is_padic_unit()
            True
            sage: R(2).is_padic_unit()
            True
            sage: R(3).is_padic_unit()
            False
            sage: Qp(5,5)(5).is_padic_unit()
            False

        TESTS::

            sage: R(4).is_padic_unit()
            True
            sage: R(6).is_padic_unit()
            False
            sage: R(9).is_padic_unit()
            False
            sage: K(0).is_padic_unit()
            False
            sage: K(1).is_padic_unit()
            True
            sage: K(2).is_padic_unit()
            True
            sage: K(3).is_padic_unit()
            False
            sage: K(4).is_padic_unit()
            True
            sage: K(6).is_padic_unit()
            False
            sage: K(9).is_padic_unit()
            False
            sage: K(1/3).is_padic_unit()
            False
            sage: K(1/9).is_padic_unit()
            False
            sage: Qq(3^2,5,names='a')(3).is_padic_unit()                                # needs sage.libs.ntl
            False"""
    @overload
    def is_padic_unit(self) -> Any:
        """LocalGenericElement.is_padic_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 549)

        Return whether ``self`` is a `p`-adic unit. That is, whether it has
        zero valuation.

        INPUT:

        - ``self`` -- a local ring element

        OUTPUT: boolean; whether ``self`` is a unit

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel'); K = Qp(3,20,'capped-rel')
            sage: R(0).is_padic_unit()
            False
            sage: R(1).is_padic_unit()
            True
            sage: R(2).is_padic_unit()
            True
            sage: R(3).is_padic_unit()
            False
            sage: Qp(5,5)(5).is_padic_unit()
            False

        TESTS::

            sage: R(4).is_padic_unit()
            True
            sage: R(6).is_padic_unit()
            False
            sage: R(9).is_padic_unit()
            False
            sage: K(0).is_padic_unit()
            False
            sage: K(1).is_padic_unit()
            True
            sage: K(2).is_padic_unit()
            True
            sage: K(3).is_padic_unit()
            False
            sage: K(4).is_padic_unit()
            True
            sage: K(6).is_padic_unit()
            False
            sage: K(9).is_padic_unit()
            False
            sage: K(1/3).is_padic_unit()
            False
            sage: K(1/9).is_padic_unit()
            False
            sage: Qq(3^2,5,names='a')(3).is_padic_unit()                                # needs sage.libs.ntl
            False"""
    @overload
    def is_padic_unit(self) -> Any:
        """LocalGenericElement.is_padic_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 549)

        Return whether ``self`` is a `p`-adic unit. That is, whether it has
        zero valuation.

        INPUT:

        - ``self`` -- a local ring element

        OUTPUT: boolean; whether ``self`` is a unit

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel'); K = Qp(3,20,'capped-rel')
            sage: R(0).is_padic_unit()
            False
            sage: R(1).is_padic_unit()
            True
            sage: R(2).is_padic_unit()
            True
            sage: R(3).is_padic_unit()
            False
            sage: Qp(5,5)(5).is_padic_unit()
            False

        TESTS::

            sage: R(4).is_padic_unit()
            True
            sage: R(6).is_padic_unit()
            False
            sage: R(9).is_padic_unit()
            False
            sage: K(0).is_padic_unit()
            False
            sage: K(1).is_padic_unit()
            True
            sage: K(2).is_padic_unit()
            True
            sage: K(3).is_padic_unit()
            False
            sage: K(4).is_padic_unit()
            True
            sage: K(6).is_padic_unit()
            False
            sage: K(9).is_padic_unit()
            False
            sage: K(1/3).is_padic_unit()
            False
            sage: K(1/9).is_padic_unit()
            False
            sage: Qq(3^2,5,names='a')(3).is_padic_unit()                                # needs sage.libs.ntl
            False"""
    @overload
    def is_padic_unit(self) -> Any:
        """LocalGenericElement.is_padic_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 549)

        Return whether ``self`` is a `p`-adic unit. That is, whether it has
        zero valuation.

        INPUT:

        - ``self`` -- a local ring element

        OUTPUT: boolean; whether ``self`` is a unit

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel'); K = Qp(3,20,'capped-rel')
            sage: R(0).is_padic_unit()
            False
            sage: R(1).is_padic_unit()
            True
            sage: R(2).is_padic_unit()
            True
            sage: R(3).is_padic_unit()
            False
            sage: Qp(5,5)(5).is_padic_unit()
            False

        TESTS::

            sage: R(4).is_padic_unit()
            True
            sage: R(6).is_padic_unit()
            False
            sage: R(9).is_padic_unit()
            False
            sage: K(0).is_padic_unit()
            False
            sage: K(1).is_padic_unit()
            True
            sage: K(2).is_padic_unit()
            True
            sage: K(3).is_padic_unit()
            False
            sage: K(4).is_padic_unit()
            True
            sage: K(6).is_padic_unit()
            False
            sage: K(9).is_padic_unit()
            False
            sage: K(1/3).is_padic_unit()
            False
            sage: K(1/9).is_padic_unit()
            False
            sage: Qq(3^2,5,names='a')(3).is_padic_unit()                                # needs sage.libs.ntl
            False"""
    @overload
    def is_padic_unit(self) -> Any:
        """LocalGenericElement.is_padic_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 549)

        Return whether ``self`` is a `p`-adic unit. That is, whether it has
        zero valuation.

        INPUT:

        - ``self`` -- a local ring element

        OUTPUT: boolean; whether ``self`` is a unit

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel'); K = Qp(3,20,'capped-rel')
            sage: R(0).is_padic_unit()
            False
            sage: R(1).is_padic_unit()
            True
            sage: R(2).is_padic_unit()
            True
            sage: R(3).is_padic_unit()
            False
            sage: Qp(5,5)(5).is_padic_unit()
            False

        TESTS::

            sage: R(4).is_padic_unit()
            True
            sage: R(6).is_padic_unit()
            False
            sage: R(9).is_padic_unit()
            False
            sage: K(0).is_padic_unit()
            False
            sage: K(1).is_padic_unit()
            True
            sage: K(2).is_padic_unit()
            True
            sage: K(3).is_padic_unit()
            False
            sage: K(4).is_padic_unit()
            True
            sage: K(6).is_padic_unit()
            False
            sage: K(9).is_padic_unit()
            False
            sage: K(1/3).is_padic_unit()
            False
            sage: K(1/9).is_padic_unit()
            False
            sage: Qq(3^2,5,names='a')(3).is_padic_unit()                                # needs sage.libs.ntl
            False"""
    @overload
    def is_padic_unit(self) -> Any:
        """LocalGenericElement.is_padic_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 549)

        Return whether ``self`` is a `p`-adic unit. That is, whether it has
        zero valuation.

        INPUT:

        - ``self`` -- a local ring element

        OUTPUT: boolean; whether ``self`` is a unit

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel'); K = Qp(3,20,'capped-rel')
            sage: R(0).is_padic_unit()
            False
            sage: R(1).is_padic_unit()
            True
            sage: R(2).is_padic_unit()
            True
            sage: R(3).is_padic_unit()
            False
            sage: Qp(5,5)(5).is_padic_unit()
            False

        TESTS::

            sage: R(4).is_padic_unit()
            True
            sage: R(6).is_padic_unit()
            False
            sage: R(9).is_padic_unit()
            False
            sage: K(0).is_padic_unit()
            False
            sage: K(1).is_padic_unit()
            True
            sage: K(2).is_padic_unit()
            True
            sage: K(3).is_padic_unit()
            False
            sage: K(4).is_padic_unit()
            True
            sage: K(6).is_padic_unit()
            False
            sage: K(9).is_padic_unit()
            False
            sage: K(1/3).is_padic_unit()
            False
            sage: K(1/9).is_padic_unit()
            False
            sage: Qq(3^2,5,names='a')(3).is_padic_unit()                                # needs sage.libs.ntl
            False"""
    @overload
    def is_padic_unit(self) -> Any:
        """LocalGenericElement.is_padic_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 549)

        Return whether ``self`` is a `p`-adic unit. That is, whether it has
        zero valuation.

        INPUT:

        - ``self`` -- a local ring element

        OUTPUT: boolean; whether ``self`` is a unit

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel'); K = Qp(3,20,'capped-rel')
            sage: R(0).is_padic_unit()
            False
            sage: R(1).is_padic_unit()
            True
            sage: R(2).is_padic_unit()
            True
            sage: R(3).is_padic_unit()
            False
            sage: Qp(5,5)(5).is_padic_unit()
            False

        TESTS::

            sage: R(4).is_padic_unit()
            True
            sage: R(6).is_padic_unit()
            False
            sage: R(9).is_padic_unit()
            False
            sage: K(0).is_padic_unit()
            False
            sage: K(1).is_padic_unit()
            True
            sage: K(2).is_padic_unit()
            True
            sage: K(3).is_padic_unit()
            False
            sage: K(4).is_padic_unit()
            True
            sage: K(6).is_padic_unit()
            False
            sage: K(9).is_padic_unit()
            False
            sage: K(1/3).is_padic_unit()
            False
            sage: K(1/9).is_padic_unit()
            False
            sage: Qq(3^2,5,names='a')(3).is_padic_unit()                                # needs sage.libs.ntl
            False"""
    @overload
    def is_padic_unit(self) -> Any:
        """LocalGenericElement.is_padic_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 549)

        Return whether ``self`` is a `p`-adic unit. That is, whether it has
        zero valuation.

        INPUT:

        - ``self`` -- a local ring element

        OUTPUT: boolean; whether ``self`` is a unit

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel'); K = Qp(3,20,'capped-rel')
            sage: R(0).is_padic_unit()
            False
            sage: R(1).is_padic_unit()
            True
            sage: R(2).is_padic_unit()
            True
            sage: R(3).is_padic_unit()
            False
            sage: Qp(5,5)(5).is_padic_unit()
            False

        TESTS::

            sage: R(4).is_padic_unit()
            True
            sage: R(6).is_padic_unit()
            False
            sage: R(9).is_padic_unit()
            False
            sage: K(0).is_padic_unit()
            False
            sage: K(1).is_padic_unit()
            True
            sage: K(2).is_padic_unit()
            True
            sage: K(3).is_padic_unit()
            False
            sage: K(4).is_padic_unit()
            True
            sage: K(6).is_padic_unit()
            False
            sage: K(9).is_padic_unit()
            False
            sage: K(1/3).is_padic_unit()
            False
            sage: K(1/9).is_padic_unit()
            False
            sage: Qq(3^2,5,names='a')(3).is_padic_unit()                                # needs sage.libs.ntl
            False"""
    @overload
    def is_padic_unit(self) -> Any:
        """LocalGenericElement.is_padic_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 549)

        Return whether ``self`` is a `p`-adic unit. That is, whether it has
        zero valuation.

        INPUT:

        - ``self`` -- a local ring element

        OUTPUT: boolean; whether ``self`` is a unit

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel'); K = Qp(3,20,'capped-rel')
            sage: R(0).is_padic_unit()
            False
            sage: R(1).is_padic_unit()
            True
            sage: R(2).is_padic_unit()
            True
            sage: R(3).is_padic_unit()
            False
            sage: Qp(5,5)(5).is_padic_unit()
            False

        TESTS::

            sage: R(4).is_padic_unit()
            True
            sage: R(6).is_padic_unit()
            False
            sage: R(9).is_padic_unit()
            False
            sage: K(0).is_padic_unit()
            False
            sage: K(1).is_padic_unit()
            True
            sage: K(2).is_padic_unit()
            True
            sage: K(3).is_padic_unit()
            False
            sage: K(4).is_padic_unit()
            True
            sage: K(6).is_padic_unit()
            False
            sage: K(9).is_padic_unit()
            False
            sage: K(1/3).is_padic_unit()
            False
            sage: K(1/9).is_padic_unit()
            False
            sage: Qq(3^2,5,names='a')(3).is_padic_unit()                                # needs sage.libs.ntl
            False"""
    @overload
    def is_padic_unit(self) -> Any:
        """LocalGenericElement.is_padic_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 549)

        Return whether ``self`` is a `p`-adic unit. That is, whether it has
        zero valuation.

        INPUT:

        - ``self`` -- a local ring element

        OUTPUT: boolean; whether ``self`` is a unit

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel'); K = Qp(3,20,'capped-rel')
            sage: R(0).is_padic_unit()
            False
            sage: R(1).is_padic_unit()
            True
            sage: R(2).is_padic_unit()
            True
            sage: R(3).is_padic_unit()
            False
            sage: Qp(5,5)(5).is_padic_unit()
            False

        TESTS::

            sage: R(4).is_padic_unit()
            True
            sage: R(6).is_padic_unit()
            False
            sage: R(9).is_padic_unit()
            False
            sage: K(0).is_padic_unit()
            False
            sage: K(1).is_padic_unit()
            True
            sage: K(2).is_padic_unit()
            True
            sage: K(3).is_padic_unit()
            False
            sage: K(4).is_padic_unit()
            True
            sage: K(6).is_padic_unit()
            False
            sage: K(9).is_padic_unit()
            False
            sage: K(1/3).is_padic_unit()
            False
            sage: K(1/9).is_padic_unit()
            False
            sage: Qq(3^2,5,names='a')(3).is_padic_unit()                                # needs sage.libs.ntl
            False"""
    @overload
    def is_padic_unit(self) -> Any:
        """LocalGenericElement.is_padic_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 549)

        Return whether ``self`` is a `p`-adic unit. That is, whether it has
        zero valuation.

        INPUT:

        - ``self`` -- a local ring element

        OUTPUT: boolean; whether ``self`` is a unit

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel'); K = Qp(3,20,'capped-rel')
            sage: R(0).is_padic_unit()
            False
            sage: R(1).is_padic_unit()
            True
            sage: R(2).is_padic_unit()
            True
            sage: R(3).is_padic_unit()
            False
            sage: Qp(5,5)(5).is_padic_unit()
            False

        TESTS::

            sage: R(4).is_padic_unit()
            True
            sage: R(6).is_padic_unit()
            False
            sage: R(9).is_padic_unit()
            False
            sage: K(0).is_padic_unit()
            False
            sage: K(1).is_padic_unit()
            True
            sage: K(2).is_padic_unit()
            True
            sage: K(3).is_padic_unit()
            False
            sage: K(4).is_padic_unit()
            True
            sage: K(6).is_padic_unit()
            False
            sage: K(9).is_padic_unit()
            False
            sage: K(1/3).is_padic_unit()
            False
            sage: K(1/9).is_padic_unit()
            False
            sage: Qq(3^2,5,names='a')(3).is_padic_unit()                                # needs sage.libs.ntl
            False"""
    @overload
    def is_padic_unit(self) -> Any:
        """LocalGenericElement.is_padic_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 549)

        Return whether ``self`` is a `p`-adic unit. That is, whether it has
        zero valuation.

        INPUT:

        - ``self`` -- a local ring element

        OUTPUT: boolean; whether ``self`` is a unit

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel'); K = Qp(3,20,'capped-rel')
            sage: R(0).is_padic_unit()
            False
            sage: R(1).is_padic_unit()
            True
            sage: R(2).is_padic_unit()
            True
            sage: R(3).is_padic_unit()
            False
            sage: Qp(5,5)(5).is_padic_unit()
            False

        TESTS::

            sage: R(4).is_padic_unit()
            True
            sage: R(6).is_padic_unit()
            False
            sage: R(9).is_padic_unit()
            False
            sage: K(0).is_padic_unit()
            False
            sage: K(1).is_padic_unit()
            True
            sage: K(2).is_padic_unit()
            True
            sage: K(3).is_padic_unit()
            False
            sage: K(4).is_padic_unit()
            True
            sage: K(6).is_padic_unit()
            False
            sage: K(9).is_padic_unit()
            False
            sage: K(1/3).is_padic_unit()
            False
            sage: K(1/9).is_padic_unit()
            False
            sage: Qq(3^2,5,names='a')(3).is_padic_unit()                                # needs sage.libs.ntl
            False"""
    @overload
    def is_padic_unit(self) -> Any:
        """LocalGenericElement.is_padic_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 549)

        Return whether ``self`` is a `p`-adic unit. That is, whether it has
        zero valuation.

        INPUT:

        - ``self`` -- a local ring element

        OUTPUT: boolean; whether ``self`` is a unit

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel'); K = Qp(3,20,'capped-rel')
            sage: R(0).is_padic_unit()
            False
            sage: R(1).is_padic_unit()
            True
            sage: R(2).is_padic_unit()
            True
            sage: R(3).is_padic_unit()
            False
            sage: Qp(5,5)(5).is_padic_unit()
            False

        TESTS::

            sage: R(4).is_padic_unit()
            True
            sage: R(6).is_padic_unit()
            False
            sage: R(9).is_padic_unit()
            False
            sage: K(0).is_padic_unit()
            False
            sage: K(1).is_padic_unit()
            True
            sage: K(2).is_padic_unit()
            True
            sage: K(3).is_padic_unit()
            False
            sage: K(4).is_padic_unit()
            True
            sage: K(6).is_padic_unit()
            False
            sage: K(9).is_padic_unit()
            False
            sage: K(1/3).is_padic_unit()
            False
            sage: K(1/9).is_padic_unit()
            False
            sage: Qq(3^2,5,names='a')(3).is_padic_unit()                                # needs sage.libs.ntl
            False"""
    @overload
    def is_padic_unit(self) -> Any:
        """LocalGenericElement.is_padic_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 549)

        Return whether ``self`` is a `p`-adic unit. That is, whether it has
        zero valuation.

        INPUT:

        - ``self`` -- a local ring element

        OUTPUT: boolean; whether ``self`` is a unit

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel'); K = Qp(3,20,'capped-rel')
            sage: R(0).is_padic_unit()
            False
            sage: R(1).is_padic_unit()
            True
            sage: R(2).is_padic_unit()
            True
            sage: R(3).is_padic_unit()
            False
            sage: Qp(5,5)(5).is_padic_unit()
            False

        TESTS::

            sage: R(4).is_padic_unit()
            True
            sage: R(6).is_padic_unit()
            False
            sage: R(9).is_padic_unit()
            False
            sage: K(0).is_padic_unit()
            False
            sage: K(1).is_padic_unit()
            True
            sage: K(2).is_padic_unit()
            True
            sage: K(3).is_padic_unit()
            False
            sage: K(4).is_padic_unit()
            True
            sage: K(6).is_padic_unit()
            False
            sage: K(9).is_padic_unit()
            False
            sage: K(1/3).is_padic_unit()
            False
            sage: K(1/9).is_padic_unit()
            False
            sage: Qq(3^2,5,names='a')(3).is_padic_unit()                                # needs sage.libs.ntl
            False"""
    @overload
    def is_padic_unit(self) -> Any:
        """LocalGenericElement.is_padic_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 549)

        Return whether ``self`` is a `p`-adic unit. That is, whether it has
        zero valuation.

        INPUT:

        - ``self`` -- a local ring element

        OUTPUT: boolean; whether ``self`` is a unit

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel'); K = Qp(3,20,'capped-rel')
            sage: R(0).is_padic_unit()
            False
            sage: R(1).is_padic_unit()
            True
            sage: R(2).is_padic_unit()
            True
            sage: R(3).is_padic_unit()
            False
            sage: Qp(5,5)(5).is_padic_unit()
            False

        TESTS::

            sage: R(4).is_padic_unit()
            True
            sage: R(6).is_padic_unit()
            False
            sage: R(9).is_padic_unit()
            False
            sage: K(0).is_padic_unit()
            False
            sage: K(1).is_padic_unit()
            True
            sage: K(2).is_padic_unit()
            True
            sage: K(3).is_padic_unit()
            False
            sage: K(4).is_padic_unit()
            True
            sage: K(6).is_padic_unit()
            False
            sage: K(9).is_padic_unit()
            False
            sage: K(1/3).is_padic_unit()
            False
            sage: K(1/9).is_padic_unit()
            False
            sage: Qq(3^2,5,names='a')(3).is_padic_unit()                                # needs sage.libs.ntl
            False"""
    @overload
    def is_padic_unit(self) -> Any:
        """LocalGenericElement.is_padic_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 549)

        Return whether ``self`` is a `p`-adic unit. That is, whether it has
        zero valuation.

        INPUT:

        - ``self`` -- a local ring element

        OUTPUT: boolean; whether ``self`` is a unit

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel'); K = Qp(3,20,'capped-rel')
            sage: R(0).is_padic_unit()
            False
            sage: R(1).is_padic_unit()
            True
            sage: R(2).is_padic_unit()
            True
            sage: R(3).is_padic_unit()
            False
            sage: Qp(5,5)(5).is_padic_unit()
            False

        TESTS::

            sage: R(4).is_padic_unit()
            True
            sage: R(6).is_padic_unit()
            False
            sage: R(9).is_padic_unit()
            False
            sage: K(0).is_padic_unit()
            False
            sage: K(1).is_padic_unit()
            True
            sage: K(2).is_padic_unit()
            True
            sage: K(3).is_padic_unit()
            False
            sage: K(4).is_padic_unit()
            True
            sage: K(6).is_padic_unit()
            False
            sage: K(9).is_padic_unit()
            False
            sage: K(1/3).is_padic_unit()
            False
            sage: K(1/9).is_padic_unit()
            False
            sage: Qq(3^2,5,names='a')(3).is_padic_unit()                                # needs sage.libs.ntl
            False"""
    def is_unit(self) -> Any:
        """LocalGenericElement.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 605)

        Return whether ``self`` is a unit.

        INPUT:

        - ``self`` -- a local ring element

        OUTPUT: boolean; whether ``self`` is a unit

        .. NOTE::

            For fields all nonzero elements are units. For DVR's, only
            those elements of valuation 0 are. An older implementation
            ignored the case of fields, and returned always the
            negation of self.valuation()==0. This behavior is now
            supported with self.is_padic_unit().

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel'); K = Qp(3,20,'capped-rel')
            sage: R(0).is_unit()
            False
            sage: R(1).is_unit()
            True
            sage: R(2).is_unit()
            True
            sage: R(3).is_unit()
            False
            sage: Qp(5,5)(5).is_unit()  # Note that 5 is invertible in `QQ_5`, even if it has positive valuation!
            True
            sage: Qp(5,5)(5).is_padic_unit()
            False

        TESTS::

            sage: R(4).is_unit()
            True
            sage: R(6).is_unit()
            False
            sage: R(9).is_unit()
            False
            sage: K(0).is_unit()
            False
            sage: K(1).is_unit()
            True
            sage: K(2).is_unit()
            True
            sage: K(3).is_unit()
            True
            sage: K(4).is_unit()
            True
            sage: K(6).is_unit()
            True
            sage: K(9).is_unit()
            True
            sage: K(1/3).is_unit()
            True
            sage: K(1/9).is_unit()
            True
            sage: Qq(3^2,5,names='a')(3).is_unit()                                      # needs sage.libs.ntl
            True
            sage: R(0,0).is_unit()
            False
            sage: K(0,0).is_unit()
            False"""
    @overload
    def normalized_valuation(self) -> Any:
        """LocalGenericElement.normalized_valuation(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 827)

        Return the normalized valuation of this local ring element,
        i.e., the valuation divided by the absolute ramification index.

        INPUT:

        - ``self`` -- a local ring element

        OUTPUT: rational; the normalized valuation of ``self``

        EXAMPLES::

            sage: Q7 = Qp(7)
            sage: R.<x> = Q7[]                                                          # needs sage.libs.ntl
            sage: F.<z> = Q7.ext(x^3+7*x+7)                                             # needs sage.libs.ntl
            sage: z.normalized_valuation()                                              # needs sage.libs.ntl
            1/3"""
    @overload
    def normalized_valuation(self) -> Any:
        """LocalGenericElement.normalized_valuation(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 827)

        Return the normalized valuation of this local ring element,
        i.e., the valuation divided by the absolute ramification index.

        INPUT:

        - ``self`` -- a local ring element

        OUTPUT: rational; the normalized valuation of ``self``

        EXAMPLES::

            sage: Q7 = Qp(7)
            sage: R.<x> = Q7[]                                                          # needs sage.libs.ntl
            sage: F.<z> = Q7.ext(x^3+7*x+7)                                             # needs sage.libs.ntl
            sage: z.normalized_valuation()                                              # needs sage.libs.ntl
            1/3"""
    def quo_rem(self, other, integral=...) -> Any:
        """LocalGenericElement.quo_rem(self, other, integral=False)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 910)

        Return the quotient with remainder of the division of this element by
        ``other``.

        INPUT:

        - ``other`` -- an element in the same ring
        - ``integral`` -- if ``True``, use integral-style remainders even when
          the parent is a field. Namely, the remainder will have no terms in
          its `p`-adic expansion above the valuation of ``other``.

        EXAMPLES::

            sage: R = Zp(3, 5)
            sage: R(12).quo_rem(R(2))
            (2*3 + O(3^6), 0)
            sage: R(2).quo_rem(R(12))
            (O(3^4), 2 + O(3^5))

            sage: K = Qp(3, 5)
            sage: K(12).quo_rem(K(2))
            (2*3 + O(3^6), 0)
            sage: K(2).quo_rem(K(12))
            (2*3^-1 + 1 + 3 + 3^2 + 3^3 + O(3^4), 0)

        You can get the same behavior for fields as for rings
        by using integral=True::

            sage: K(12).quo_rem(K(2), integral=True)
            (2*3 + O(3^6), 0)
            sage: K(2).quo_rem(K(12), integral=True)
            (O(3^4), 2 + O(3^5))"""
    def slice(self, i, j, k=..., lift_mode=...) -> Any:
        """LocalGenericElement.slice(self, i, j, k=1, lift_mode='simple')

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 197)

        Return the sum of the `pi^{i + l \\cdot k}` terms of the series
        expansion of this element, where pi is the uniformizer,
        for `i + l \\cdot k` between ``i`` and ``j-1`` inclusive, and
        nonnegative integers `l`. Behaves analogously to the slice
        function for lists.

        INPUT:

        - ``i`` -- integer; if set to ``None``, the sum will start with the
          first nonzero term of the series

        - ``j`` -- integer; if set to ``None`` or `\\infty`, this method
          behaves as if it was set to the absolute precision of this element

        - ``k`` -- (default: 1) a positive integer

        EXAMPLES::

            sage: R = Zp(5, 6, 'capped-rel')
            sage: a = R(1/2); a
            3 + 2*5 + 2*5^2 + 2*5^3 + 2*5^4 + 2*5^5 + O(5^6)
            sage: a.slice(2, 4)
            2*5^2 + 2*5^3 + O(5^4)
            sage: a.slice(1, 6, 2)
            2*5 + 2*5^3 + 2*5^5 + O(5^6)

        The step size ``k`` has to be positive::

            sage: a.slice(0, 3, 0)
            Traceback (most recent call last):
            ...
            ValueError: slice step must be positive
            sage: a.slice(0, 3, -1)
            Traceback (most recent call last):
            ...
            ValueError: slice step must be positive

        If ``i`` exceeds ``j``, then the result will be zero, with the
        precision given by ``j``::

            sage: a.slice(5, 4)
            O(5^4)
            sage: a.slice(6, 5)
            O(5^5)

        However, the precision cannot exceed the precision of the element::

            sage: a.slice(101,100)
            O(5^6)
            sage: a.slice(0,5,2)
            3 + 2*5^2 + 2*5^4 + O(5^5)
            sage: a.slice(0,6,2)
            3 + 2*5^2 + 2*5^4 + O(5^6)
            sage: a.slice(0,7,2)
            3 + 2*5^2 + 2*5^4 + O(5^6)

        If start is left blank, it is set to the valuation::

            sage: K = Qp(5, 6)
            sage: x = K(1/25 + 5); x
            5^-2 + 5 + O(5^4)
            sage: x.slice(None, 3)
            5^-2 + 5 + O(5^3)
            sage: x[:3]
            doctest:warning
            ...
            DeprecationWarning: __getitem__ is changing to match the behavior of number fields. Please use expansion instead.
            See https://github.com/sagemath/sage/issues/14825 for details.
            5^-2 + 5 + O(5^3)

        TESTS:

        Test that slices also work over fields::

            sage: a = K(1/25); a
            5^-2 + O(5^4)
            sage: b = K(25); b
            5^2 + O(5^8)

            sage: a.slice(2, 4)
            O(5^4)
            sage: b.slice(2, 4)
            5^2 + O(5^4)
            sage: a.slice(-3, -1)
            5^-2 + O(5^-1)
            sage: b.slice(-1, 1)
            O(5)
            sage: b.slice(-3, -1)
            O(5^-1)
            sage: b.slice(101, 100)
            O(5^8)
            sage: b.slice(0,7,2)
            5^2 + O(5^7)
            sage: b.slice(0,8,2)
            5^2 + O(5^8)
            sage: b.slice(0,9,2)
            5^2 + O(5^8)

        Test that slices also work over eisenstein extensions::

            sage: # needs sage.libs.ntl
            sage: F = Qp(5)
            sage: H.<x> = F[]
            sage: T.<t> = F.extension(x^2 - 5)
            sage: a = T(3*t^-2 + 1 + 4*t + 2*t^2)
            sage: a.slice(0, 1)
            1 + O(t)
            sage: a.slice(-3, 4)
            3*t^-2 + 1 + 4*t + 2*t^2 + O(t^4)
            sage: a.slice(-2, 6, 3)
            3*t^-2 + 4*t + O(t^6)

        Test that slices also work over unramified extensions::

            sage: # needs sage.libs.ntl
            sage: F = Qp(5)
            sage: H.<x> = F[]
            sage: T.<t> = F.extension(x^2 - 2)
            sage: a = T(3*5^-1 + 1 + (3*t + 4)*5^2)
            sage: a.slice(0, 1)
            1 + O(5)
            sage: a.slice(-3, 4)
            3*5^-1 + 1 + (3*t + 4)*5^2 + O(5^4)
            sage: a.slice(-1, 6, 3)
            3*5^-1 + (3*t + 4)*5^2 + O(5^6)

        Test that slices also work over 2-step extensions (unramified followed by eisenstein)::

            sage: # needs sage.libs.ntl
            sage: F = Qp(5)
            sage: H.<x> = F[]
            sage: T.<t> = F.extension(x^2 - 3)
            sage: D.<y> = T[]
            sage: W.<w> = T.extension((4*5^-2 + 2*5^-1 + 4 + (2*t + 2)*5 + 3*t*5^3 + 4*5^4 + 3*5^5 + (2*t + 2)*5^8 + (4*t + 3)*5^9 + 2*t*5^10 + (3*t + 3)*5^11 + (3*t + 1)*5^12 + (3*t + 2)*5^13 + 4*5^14 + (2*t + 4)*5^15 + (4*t + 1)*5^16 + (t + 1)*5^17 + O(5^18))*y^2 + (t + 2*t*5 + t*5^2 + 4*t*5^3 + (2*t + 4)*5^4 + (3*t + 4)*5^5 + (t + 1)*5^6 + t*5^7 + (2*t + 4)*5^8 + 3*5^9 + 2*5^10 + 5^12 + (4*t + 2)*5^13 + 5^14 + 5^15 + 3*t*5^16 + (t + 2)*5^17 + 4*5^18 + (3*t + 1)*5^19 + O(5^20))*y + (2*t + 2)*5^-1 + 3 + 5 + t*5^2 + (4*t + 2)*5^3 + (4*t + 1)*5^4 + (3*t + 4)*5^5 + (4*t + 4)*5^6 + (3*t + 2)*5^7 + (4*t + 4)*5^8 + 3*5^9 + (t + 3)*5^10 + (4*t + 3)*5^11 + 5^12 + (2*t + 2)*5^14 + 4*t*5^15 + (2*t + 2)*5^16 + (4*t + 4)*5^17 + O(5^18))
            sage: a = W(3*w^-36 + (2*t + 2)*w^-23)
            sage: a.slice(-25,2)
            (2*t + 2)*w^-23 + O(w^2)
            sage: a.slice(0, 1)
            O(w)

        Verify that :issue:`14106` has been fixed::

            sage: R = Zp(5,7)
            sage: a = R(300)
            sage: a
            2*5^2 + 2*5^3 + O(5^9)
            sage: a[:5]
            2*5^2 + 2*5^3 + O(5^5)
            sage: a.slice(None, 5, None)
            2*5^2 + 2*5^3 + O(5^5)

        Verify that :issue:`30695` has been fixed::

            sage: F = Qp(3)
            sage: a = F(0)
            sage: a.slice(0,None)
            0"""
    @overload
    def sqrt(self, extend=..., all=..., algorithm=...) -> Any:
        """LocalGenericElement.sqrt(self, extend=True, all=False, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 708)

        Return the square root of this element.

        INPUT:

        - ``self`` -- a `p`-adic element

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension if necessary; if ``False`` and no root
          exists in the given ring or field, raise a :exc:`ValueError`.

        - ``all`` -- boolean (default: ``False``); if ``True``, return a
          list of all square roots

        - ``algorithm`` -- ``'pari'``, ``'sage'`` or ``None`` (default:
          ``None``); Sage provides an implementation for any extension of
          `Q_p` whereas only square roots over `Q_p` is implemented in Pari;
          the default is ``'pari'`` if the ground field is `Q_p`, ``'sage'``
          otherwise.

        OUTPUT: the square root or the list of all square roots of this element

        .. NOTE::

            The square root is chosen (resp. the square roots are ordered) in
            a deterministic way, which is compatible with change of precision.

        EXAMPLES::

            sage: R = Zp(3, 20)
            sage: sqrt(R(0))
            0

            sage: sqrt(R(1))
            1 + O(3^20)

            sage: R(2).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: element is not a square

            sage: s = sqrt(R(4)); -s
            2 + O(3^20)

            sage: s = sqrt(R(9)); s
            3 + O(3^21)

        Over the `2`-adics, the precision of the square root is less
        than the input::

            sage: R2 = Zp(2, 20)
            sage: sqrt(R2(1))
            1 + O(2^19)
            sage: sqrt(R2(4))
            2 + O(2^20)

            sage: R.<t> = Zq(2^10, 10)                                                  # needs sage.libs.ntl
            sage: u = 1 + 8*t                                                           # needs sage.libs.ntl
            sage: sqrt(u)                                                               # needs sage.libs.ntl
            1 + t*2^2 + t^2*2^3 + t^2*2^4 + (t^4 + t^3 + t^2)*2^5 + (t^4 + t^2)*2^6
              + (t^5 + t^2)*2^7 + (t^6 + t^5 + t^4 + t^2)*2^8 + O(2^9)

            sage: R.<a> = Zp(2).extension(x^3 - 2)
            sage: u = R(1 + a^4 + a^5 + a^7 + a^8, 10); u
            1 + a^4 + a^5 + a^7 + a^8 + O(a^10)
            sage: v = sqrt(u); v                                                        # needs sage.libs.ntl
            1 + a^2 + a^4 + a^6 + O(a^7)

        However, observe that the precision increases to its original value
        when we recompute the square of the square root::

            sage: v^2                                                                   # needs sage.libs.ntl
            1 + a^4 + a^5 + a^7 + a^8 + O(a^10)

        If the input does not have enough precision in order to determine if
        the given element has a square root in the ground field, an error is
        raised::

            sage: R(1, 6).sqrt()
            Traceback (most recent call last):
            ...
            PrecisionError: not enough precision to be sure that this element has a square root

            sage: R(1, 7).sqrt()
            1 + O(a^4)

            sage: R(1+a^6, 7).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: element is not a square

        In particular, an error is raised when we try to compute the square
        root of an inexact

        TESTS::

            sage: R = Qp(5, 100)
            sage: c = R.random_element()
            sage: s = sqrt(c^2)
            sage: s == c or s == -c
            True

            sage: c2 = c^2
            sage: c2 = c2.add_bigoh(c2.valuation() + 50)
            sage: s == sqrt(c2)
            True"""
    @overload
    def sqrt(self, extend=...) -> Any:
        """LocalGenericElement.sqrt(self, extend=True, all=False, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 708)

        Return the square root of this element.

        INPUT:

        - ``self`` -- a `p`-adic element

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension if necessary; if ``False`` and no root
          exists in the given ring or field, raise a :exc:`ValueError`.

        - ``all`` -- boolean (default: ``False``); if ``True``, return a
          list of all square roots

        - ``algorithm`` -- ``'pari'``, ``'sage'`` or ``None`` (default:
          ``None``); Sage provides an implementation for any extension of
          `Q_p` whereas only square roots over `Q_p` is implemented in Pari;
          the default is ``'pari'`` if the ground field is `Q_p`, ``'sage'``
          otherwise.

        OUTPUT: the square root or the list of all square roots of this element

        .. NOTE::

            The square root is chosen (resp. the square roots are ordered) in
            a deterministic way, which is compatible with change of precision.

        EXAMPLES::

            sage: R = Zp(3, 20)
            sage: sqrt(R(0))
            0

            sage: sqrt(R(1))
            1 + O(3^20)

            sage: R(2).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: element is not a square

            sage: s = sqrt(R(4)); -s
            2 + O(3^20)

            sage: s = sqrt(R(9)); s
            3 + O(3^21)

        Over the `2`-adics, the precision of the square root is less
        than the input::

            sage: R2 = Zp(2, 20)
            sage: sqrt(R2(1))
            1 + O(2^19)
            sage: sqrt(R2(4))
            2 + O(2^20)

            sage: R.<t> = Zq(2^10, 10)                                                  # needs sage.libs.ntl
            sage: u = 1 + 8*t                                                           # needs sage.libs.ntl
            sage: sqrt(u)                                                               # needs sage.libs.ntl
            1 + t*2^2 + t^2*2^3 + t^2*2^4 + (t^4 + t^3 + t^2)*2^5 + (t^4 + t^2)*2^6
              + (t^5 + t^2)*2^7 + (t^6 + t^5 + t^4 + t^2)*2^8 + O(2^9)

            sage: R.<a> = Zp(2).extension(x^3 - 2)
            sage: u = R(1 + a^4 + a^5 + a^7 + a^8, 10); u
            1 + a^4 + a^5 + a^7 + a^8 + O(a^10)
            sage: v = sqrt(u); v                                                        # needs sage.libs.ntl
            1 + a^2 + a^4 + a^6 + O(a^7)

        However, observe that the precision increases to its original value
        when we recompute the square of the square root::

            sage: v^2                                                                   # needs sage.libs.ntl
            1 + a^4 + a^5 + a^7 + a^8 + O(a^10)

        If the input does not have enough precision in order to determine if
        the given element has a square root in the ground field, an error is
        raised::

            sage: R(1, 6).sqrt()
            Traceback (most recent call last):
            ...
            PrecisionError: not enough precision to be sure that this element has a square root

            sage: R(1, 7).sqrt()
            1 + O(a^4)

            sage: R(1+a^6, 7).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: element is not a square

        In particular, an error is raised when we try to compute the square
        root of an inexact

        TESTS::

            sage: R = Qp(5, 100)
            sage: c = R.random_element()
            sage: s = sqrt(c^2)
            sage: s == c or s == -c
            True

            sage: c2 = c^2
            sage: c2 = c2.add_bigoh(c2.valuation() + 50)
            sage: s == sqrt(c2)
            True"""
    @overload
    def sqrt(self, u) -> Any:
        """LocalGenericElement.sqrt(self, extend=True, all=False, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 708)

        Return the square root of this element.

        INPUT:

        - ``self`` -- a `p`-adic element

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension if necessary; if ``False`` and no root
          exists in the given ring or field, raise a :exc:`ValueError`.

        - ``all`` -- boolean (default: ``False``); if ``True``, return a
          list of all square roots

        - ``algorithm`` -- ``'pari'``, ``'sage'`` or ``None`` (default:
          ``None``); Sage provides an implementation for any extension of
          `Q_p` whereas only square roots over `Q_p` is implemented in Pari;
          the default is ``'pari'`` if the ground field is `Q_p`, ``'sage'``
          otherwise.

        OUTPUT: the square root or the list of all square roots of this element

        .. NOTE::

            The square root is chosen (resp. the square roots are ordered) in
            a deterministic way, which is compatible with change of precision.

        EXAMPLES::

            sage: R = Zp(3, 20)
            sage: sqrt(R(0))
            0

            sage: sqrt(R(1))
            1 + O(3^20)

            sage: R(2).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: element is not a square

            sage: s = sqrt(R(4)); -s
            2 + O(3^20)

            sage: s = sqrt(R(9)); s
            3 + O(3^21)

        Over the `2`-adics, the precision of the square root is less
        than the input::

            sage: R2 = Zp(2, 20)
            sage: sqrt(R2(1))
            1 + O(2^19)
            sage: sqrt(R2(4))
            2 + O(2^20)

            sage: R.<t> = Zq(2^10, 10)                                                  # needs sage.libs.ntl
            sage: u = 1 + 8*t                                                           # needs sage.libs.ntl
            sage: sqrt(u)                                                               # needs sage.libs.ntl
            1 + t*2^2 + t^2*2^3 + t^2*2^4 + (t^4 + t^3 + t^2)*2^5 + (t^4 + t^2)*2^6
              + (t^5 + t^2)*2^7 + (t^6 + t^5 + t^4 + t^2)*2^8 + O(2^9)

            sage: R.<a> = Zp(2).extension(x^3 - 2)
            sage: u = R(1 + a^4 + a^5 + a^7 + a^8, 10); u
            1 + a^4 + a^5 + a^7 + a^8 + O(a^10)
            sage: v = sqrt(u); v                                                        # needs sage.libs.ntl
            1 + a^2 + a^4 + a^6 + O(a^7)

        However, observe that the precision increases to its original value
        when we recompute the square of the square root::

            sage: v^2                                                                   # needs sage.libs.ntl
            1 + a^4 + a^5 + a^7 + a^8 + O(a^10)

        If the input does not have enough precision in order to determine if
        the given element has a square root in the ground field, an error is
        raised::

            sage: R(1, 6).sqrt()
            Traceback (most recent call last):
            ...
            PrecisionError: not enough precision to be sure that this element has a square root

            sage: R(1, 7).sqrt()
            1 + O(a^4)

            sage: R(1+a^6, 7).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: element is not a square

        In particular, an error is raised when we try to compute the square
        root of an inexact

        TESTS::

            sage: R = Qp(5, 100)
            sage: c = R.random_element()
            sage: s = sqrt(c^2)
            sage: s == c or s == -c
            True

            sage: c2 = c^2
            sage: c2 = c2.add_bigoh(c2.valuation() + 50)
            sage: s == sqrt(c2)
            True"""
    @overload
    def sqrt(self, u) -> Any:
        """LocalGenericElement.sqrt(self, extend=True, all=False, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 708)

        Return the square root of this element.

        INPUT:

        - ``self`` -- a `p`-adic element

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension if necessary; if ``False`` and no root
          exists in the given ring or field, raise a :exc:`ValueError`.

        - ``all`` -- boolean (default: ``False``); if ``True``, return a
          list of all square roots

        - ``algorithm`` -- ``'pari'``, ``'sage'`` or ``None`` (default:
          ``None``); Sage provides an implementation for any extension of
          `Q_p` whereas only square roots over `Q_p` is implemented in Pari;
          the default is ``'pari'`` if the ground field is `Q_p`, ``'sage'``
          otherwise.

        OUTPUT: the square root or the list of all square roots of this element

        .. NOTE::

            The square root is chosen (resp. the square roots are ordered) in
            a deterministic way, which is compatible with change of precision.

        EXAMPLES::

            sage: R = Zp(3, 20)
            sage: sqrt(R(0))
            0

            sage: sqrt(R(1))
            1 + O(3^20)

            sage: R(2).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: element is not a square

            sage: s = sqrt(R(4)); -s
            2 + O(3^20)

            sage: s = sqrt(R(9)); s
            3 + O(3^21)

        Over the `2`-adics, the precision of the square root is less
        than the input::

            sage: R2 = Zp(2, 20)
            sage: sqrt(R2(1))
            1 + O(2^19)
            sage: sqrt(R2(4))
            2 + O(2^20)

            sage: R.<t> = Zq(2^10, 10)                                                  # needs sage.libs.ntl
            sage: u = 1 + 8*t                                                           # needs sage.libs.ntl
            sage: sqrt(u)                                                               # needs sage.libs.ntl
            1 + t*2^2 + t^2*2^3 + t^2*2^4 + (t^4 + t^3 + t^2)*2^5 + (t^4 + t^2)*2^6
              + (t^5 + t^2)*2^7 + (t^6 + t^5 + t^4 + t^2)*2^8 + O(2^9)

            sage: R.<a> = Zp(2).extension(x^3 - 2)
            sage: u = R(1 + a^4 + a^5 + a^7 + a^8, 10); u
            1 + a^4 + a^5 + a^7 + a^8 + O(a^10)
            sage: v = sqrt(u); v                                                        # needs sage.libs.ntl
            1 + a^2 + a^4 + a^6 + O(a^7)

        However, observe that the precision increases to its original value
        when we recompute the square of the square root::

            sage: v^2                                                                   # needs sage.libs.ntl
            1 + a^4 + a^5 + a^7 + a^8 + O(a^10)

        If the input does not have enough precision in order to determine if
        the given element has a square root in the ground field, an error is
        raised::

            sage: R(1, 6).sqrt()
            Traceback (most recent call last):
            ...
            PrecisionError: not enough precision to be sure that this element has a square root

            sage: R(1, 7).sqrt()
            1 + O(a^4)

            sage: R(1+a^6, 7).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: element is not a square

        In particular, an error is raised when we try to compute the square
        root of an inexact

        TESTS::

            sage: R = Qp(5, 100)
            sage: c = R.random_element()
            sage: s = sqrt(c^2)
            sage: s == c or s == -c
            True

            sage: c2 = c^2
            sage: c2 = c2.add_bigoh(c2.valuation() + 50)
            sage: s == sqrt(c2)
            True"""
    @overload
    def sqrt(self) -> Any:
        """LocalGenericElement.sqrt(self, extend=True, all=False, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 708)

        Return the square root of this element.

        INPUT:

        - ``self`` -- a `p`-adic element

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension if necessary; if ``False`` and no root
          exists in the given ring or field, raise a :exc:`ValueError`.

        - ``all`` -- boolean (default: ``False``); if ``True``, return a
          list of all square roots

        - ``algorithm`` -- ``'pari'``, ``'sage'`` or ``None`` (default:
          ``None``); Sage provides an implementation for any extension of
          `Q_p` whereas only square roots over `Q_p` is implemented in Pari;
          the default is ``'pari'`` if the ground field is `Q_p`, ``'sage'``
          otherwise.

        OUTPUT: the square root or the list of all square roots of this element

        .. NOTE::

            The square root is chosen (resp. the square roots are ordered) in
            a deterministic way, which is compatible with change of precision.

        EXAMPLES::

            sage: R = Zp(3, 20)
            sage: sqrt(R(0))
            0

            sage: sqrt(R(1))
            1 + O(3^20)

            sage: R(2).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: element is not a square

            sage: s = sqrt(R(4)); -s
            2 + O(3^20)

            sage: s = sqrt(R(9)); s
            3 + O(3^21)

        Over the `2`-adics, the precision of the square root is less
        than the input::

            sage: R2 = Zp(2, 20)
            sage: sqrt(R2(1))
            1 + O(2^19)
            sage: sqrt(R2(4))
            2 + O(2^20)

            sage: R.<t> = Zq(2^10, 10)                                                  # needs sage.libs.ntl
            sage: u = 1 + 8*t                                                           # needs sage.libs.ntl
            sage: sqrt(u)                                                               # needs sage.libs.ntl
            1 + t*2^2 + t^2*2^3 + t^2*2^4 + (t^4 + t^3 + t^2)*2^5 + (t^4 + t^2)*2^6
              + (t^5 + t^2)*2^7 + (t^6 + t^5 + t^4 + t^2)*2^8 + O(2^9)

            sage: R.<a> = Zp(2).extension(x^3 - 2)
            sage: u = R(1 + a^4 + a^5 + a^7 + a^8, 10); u
            1 + a^4 + a^5 + a^7 + a^8 + O(a^10)
            sage: v = sqrt(u); v                                                        # needs sage.libs.ntl
            1 + a^2 + a^4 + a^6 + O(a^7)

        However, observe that the precision increases to its original value
        when we recompute the square of the square root::

            sage: v^2                                                                   # needs sage.libs.ntl
            1 + a^4 + a^5 + a^7 + a^8 + O(a^10)

        If the input does not have enough precision in order to determine if
        the given element has a square root in the ground field, an error is
        raised::

            sage: R(1, 6).sqrt()
            Traceback (most recent call last):
            ...
            PrecisionError: not enough precision to be sure that this element has a square root

            sage: R(1, 7).sqrt()
            1 + O(a^4)

            sage: R(1+a^6, 7).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: element is not a square

        In particular, an error is raised when we try to compute the square
        root of an inexact

        TESTS::

            sage: R = Qp(5, 100)
            sage: c = R.random_element()
            sage: s = sqrt(c^2)
            sage: s == c or s == -c
            True

            sage: c2 = c^2
            sage: c2 = c2.add_bigoh(c2.valuation() + 50)
            sage: s == sqrt(c2)
            True"""
    @overload
    def sqrt(self) -> Any:
        """LocalGenericElement.sqrt(self, extend=True, all=False, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 708)

        Return the square root of this element.

        INPUT:

        - ``self`` -- a `p`-adic element

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension if necessary; if ``False`` and no root
          exists in the given ring or field, raise a :exc:`ValueError`.

        - ``all`` -- boolean (default: ``False``); if ``True``, return a
          list of all square roots

        - ``algorithm`` -- ``'pari'``, ``'sage'`` or ``None`` (default:
          ``None``); Sage provides an implementation for any extension of
          `Q_p` whereas only square roots over `Q_p` is implemented in Pari;
          the default is ``'pari'`` if the ground field is `Q_p`, ``'sage'``
          otherwise.

        OUTPUT: the square root or the list of all square roots of this element

        .. NOTE::

            The square root is chosen (resp. the square roots are ordered) in
            a deterministic way, which is compatible with change of precision.

        EXAMPLES::

            sage: R = Zp(3, 20)
            sage: sqrt(R(0))
            0

            sage: sqrt(R(1))
            1 + O(3^20)

            sage: R(2).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: element is not a square

            sage: s = sqrt(R(4)); -s
            2 + O(3^20)

            sage: s = sqrt(R(9)); s
            3 + O(3^21)

        Over the `2`-adics, the precision of the square root is less
        than the input::

            sage: R2 = Zp(2, 20)
            sage: sqrt(R2(1))
            1 + O(2^19)
            sage: sqrt(R2(4))
            2 + O(2^20)

            sage: R.<t> = Zq(2^10, 10)                                                  # needs sage.libs.ntl
            sage: u = 1 + 8*t                                                           # needs sage.libs.ntl
            sage: sqrt(u)                                                               # needs sage.libs.ntl
            1 + t*2^2 + t^2*2^3 + t^2*2^4 + (t^4 + t^3 + t^2)*2^5 + (t^4 + t^2)*2^6
              + (t^5 + t^2)*2^7 + (t^6 + t^5 + t^4 + t^2)*2^8 + O(2^9)

            sage: R.<a> = Zp(2).extension(x^3 - 2)
            sage: u = R(1 + a^4 + a^5 + a^7 + a^8, 10); u
            1 + a^4 + a^5 + a^7 + a^8 + O(a^10)
            sage: v = sqrt(u); v                                                        # needs sage.libs.ntl
            1 + a^2 + a^4 + a^6 + O(a^7)

        However, observe that the precision increases to its original value
        when we recompute the square of the square root::

            sage: v^2                                                                   # needs sage.libs.ntl
            1 + a^4 + a^5 + a^7 + a^8 + O(a^10)

        If the input does not have enough precision in order to determine if
        the given element has a square root in the ground field, an error is
        raised::

            sage: R(1, 6).sqrt()
            Traceback (most recent call last):
            ...
            PrecisionError: not enough precision to be sure that this element has a square root

            sage: R(1, 7).sqrt()
            1 + O(a^4)

            sage: R(1+a^6, 7).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: element is not a square

        In particular, an error is raised when we try to compute the square
        root of an inexact

        TESTS::

            sage: R = Qp(5, 100)
            sage: c = R.random_element()
            sage: s = sqrt(c^2)
            sage: s == c or s == -c
            True

            sage: c2 = c^2
            sage: c2 = c2.add_bigoh(c2.valuation() + 50)
            sage: s == sqrt(c2)
            True"""
    @overload
    def sqrt(self, extend=...) -> Any:
        """LocalGenericElement.sqrt(self, extend=True, all=False, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 708)

        Return the square root of this element.

        INPUT:

        - ``self`` -- a `p`-adic element

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension if necessary; if ``False`` and no root
          exists in the given ring or field, raise a :exc:`ValueError`.

        - ``all`` -- boolean (default: ``False``); if ``True``, return a
          list of all square roots

        - ``algorithm`` -- ``'pari'``, ``'sage'`` or ``None`` (default:
          ``None``); Sage provides an implementation for any extension of
          `Q_p` whereas only square roots over `Q_p` is implemented in Pari;
          the default is ``'pari'`` if the ground field is `Q_p`, ``'sage'``
          otherwise.

        OUTPUT: the square root or the list of all square roots of this element

        .. NOTE::

            The square root is chosen (resp. the square roots are ordered) in
            a deterministic way, which is compatible with change of precision.

        EXAMPLES::

            sage: R = Zp(3, 20)
            sage: sqrt(R(0))
            0

            sage: sqrt(R(1))
            1 + O(3^20)

            sage: R(2).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: element is not a square

            sage: s = sqrt(R(4)); -s
            2 + O(3^20)

            sage: s = sqrt(R(9)); s
            3 + O(3^21)

        Over the `2`-adics, the precision of the square root is less
        than the input::

            sage: R2 = Zp(2, 20)
            sage: sqrt(R2(1))
            1 + O(2^19)
            sage: sqrt(R2(4))
            2 + O(2^20)

            sage: R.<t> = Zq(2^10, 10)                                                  # needs sage.libs.ntl
            sage: u = 1 + 8*t                                                           # needs sage.libs.ntl
            sage: sqrt(u)                                                               # needs sage.libs.ntl
            1 + t*2^2 + t^2*2^3 + t^2*2^4 + (t^4 + t^3 + t^2)*2^5 + (t^4 + t^2)*2^6
              + (t^5 + t^2)*2^7 + (t^6 + t^5 + t^4 + t^2)*2^8 + O(2^9)

            sage: R.<a> = Zp(2).extension(x^3 - 2)
            sage: u = R(1 + a^4 + a^5 + a^7 + a^8, 10); u
            1 + a^4 + a^5 + a^7 + a^8 + O(a^10)
            sage: v = sqrt(u); v                                                        # needs sage.libs.ntl
            1 + a^2 + a^4 + a^6 + O(a^7)

        However, observe that the precision increases to its original value
        when we recompute the square of the square root::

            sage: v^2                                                                   # needs sage.libs.ntl
            1 + a^4 + a^5 + a^7 + a^8 + O(a^10)

        If the input does not have enough precision in order to determine if
        the given element has a square root in the ground field, an error is
        raised::

            sage: R(1, 6).sqrt()
            Traceback (most recent call last):
            ...
            PrecisionError: not enough precision to be sure that this element has a square root

            sage: R(1, 7).sqrt()
            1 + O(a^4)

            sage: R(1+a^6, 7).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: element is not a square

        In particular, an error is raised when we try to compute the square
        root of an inexact

        TESTS::

            sage: R = Qp(5, 100)
            sage: c = R.random_element()
            sage: s = sqrt(c^2)
            sage: s == c or s == -c
            True

            sage: c2 = c^2
            sage: c2 = c2.add_bigoh(c2.valuation() + 50)
            sage: s == sqrt(c2)
            True"""
    @overload
    def sqrt(self, c2) -> Any:
        """LocalGenericElement.sqrt(self, extend=True, all=False, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 708)

        Return the square root of this element.

        INPUT:

        - ``self`` -- a `p`-adic element

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension if necessary; if ``False`` and no root
          exists in the given ring or field, raise a :exc:`ValueError`.

        - ``all`` -- boolean (default: ``False``); if ``True``, return a
          list of all square roots

        - ``algorithm`` -- ``'pari'``, ``'sage'`` or ``None`` (default:
          ``None``); Sage provides an implementation for any extension of
          `Q_p` whereas only square roots over `Q_p` is implemented in Pari;
          the default is ``'pari'`` if the ground field is `Q_p`, ``'sage'``
          otherwise.

        OUTPUT: the square root or the list of all square roots of this element

        .. NOTE::

            The square root is chosen (resp. the square roots are ordered) in
            a deterministic way, which is compatible with change of precision.

        EXAMPLES::

            sage: R = Zp(3, 20)
            sage: sqrt(R(0))
            0

            sage: sqrt(R(1))
            1 + O(3^20)

            sage: R(2).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: element is not a square

            sage: s = sqrt(R(4)); -s
            2 + O(3^20)

            sage: s = sqrt(R(9)); s
            3 + O(3^21)

        Over the `2`-adics, the precision of the square root is less
        than the input::

            sage: R2 = Zp(2, 20)
            sage: sqrt(R2(1))
            1 + O(2^19)
            sage: sqrt(R2(4))
            2 + O(2^20)

            sage: R.<t> = Zq(2^10, 10)                                                  # needs sage.libs.ntl
            sage: u = 1 + 8*t                                                           # needs sage.libs.ntl
            sage: sqrt(u)                                                               # needs sage.libs.ntl
            1 + t*2^2 + t^2*2^3 + t^2*2^4 + (t^4 + t^3 + t^2)*2^5 + (t^4 + t^2)*2^6
              + (t^5 + t^2)*2^7 + (t^6 + t^5 + t^4 + t^2)*2^8 + O(2^9)

            sage: R.<a> = Zp(2).extension(x^3 - 2)
            sage: u = R(1 + a^4 + a^5 + a^7 + a^8, 10); u
            1 + a^4 + a^5 + a^7 + a^8 + O(a^10)
            sage: v = sqrt(u); v                                                        # needs sage.libs.ntl
            1 + a^2 + a^4 + a^6 + O(a^7)

        However, observe that the precision increases to its original value
        when we recompute the square of the square root::

            sage: v^2                                                                   # needs sage.libs.ntl
            1 + a^4 + a^5 + a^7 + a^8 + O(a^10)

        If the input does not have enough precision in order to determine if
        the given element has a square root in the ground field, an error is
        raised::

            sage: R(1, 6).sqrt()
            Traceback (most recent call last):
            ...
            PrecisionError: not enough precision to be sure that this element has a square root

            sage: R(1, 7).sqrt()
            1 + O(a^4)

            sage: R(1+a^6, 7).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: element is not a square

        In particular, an error is raised when we try to compute the square
        root of an inexact

        TESTS::

            sage: R = Qp(5, 100)
            sage: c = R.random_element()
            sage: s = sqrt(c^2)
            sage: s == c or s == -c
            True

            sage: c2 = c^2
            sage: c2 = c2.add_bigoh(c2.valuation() + 50)
            sage: s == sqrt(c2)
            True"""
    def __iter__(self) -> Any:
        """LocalGenericElement.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/local_generic_element.pyx (starting at line 169)

        Local elements should not be iterable, so this method correspondingly
        raises a :exc:`TypeError`.

        .. NOTE::

            Typically, local elements provide a implementation for
            ``__getitem__``. If they do not provide a method ``__iter__``, then
            iterating over them is realized by calling ``__getitem__``,
            starting from index 0. However, there are several issues with this.
            For example, terms with negative valuation would be excluded from
            the iteration, and an exact value of zero would lead to an infinite
            iterable.

            There doesn't seem to be an obvious behaviour that iteration over
            such elements should produce, so it is disabled; see :issue:`13592`.

        TESTS::

            sage: x = Qp(3).zero()
            sage: for v in x: pass
            Traceback (most recent call last):
            ...
            TypeError: this local element is not iterable"""
