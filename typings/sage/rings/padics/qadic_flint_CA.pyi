import _cython_3_2_1
import sage as sage
import sage.categories.morphism
import sage.rings.morphism
import sage.rings.padics.padic_generic_element
import sage.rings.padics.pow_computer_flint
from sage.categories.category import ZZ as ZZ
from sage.categories.homset import Hom as Hom
from sage.categories.sets_cat import Sets as Sets
from sage.categories.sets_with_partial_maps import SetsWithPartialMaps as SetsWithPartialMaps
from sage.rings.finite_rings.finite_field_base import FiniteField as FiniteField
from sage.rings.finite_rings.integer_mod_ring import Zmod as Zmod
from sage.rings.infinity import infinity as infinity
from sage.rings.padics.misc import trim_zeros as trim_zeros
from sage.rings.padics.precision_error import PrecisionError as PrecisionError
from sage.rings.polynomial.polynomial_element import Polynomial as Polynomial
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import canonical_coercion as canonical_coercion, have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

frobenius_unram: _cython_3_2_1.cython_function_or_method
norm_unram: _cython_3_2_1.cython_function_or_method
trace_unram: _cython_3_2_1.cython_function_or_method
unpickle_cae_v2: _cython_3_2_1.cython_function_or_method

class CAElement(pAdicTemplateElement):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def add_bigoh(self, absprec) -> Any:
        """CAElement.add_bigoh(self, absprec)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CA_template.pxi (starting at line 599)

        Return a new element with absolute precision decreased to
        ``absprec``.  The precision never increases.

        INPUT:

        - ``absprec`` -- integer or infinity

        OUTPUT: ``self`` with precision set to the minimum of ``self``'s
        precision and ``prec``

        EXAMPLES::

            sage: R = Zp(7,4,'capped-abs','series'); a = R(8); a.add_bigoh(1)
            1 + O(7)

            sage: k = ZpCA(3,5)
            sage: a = k(41); a
            2 + 3 + 3^2 + 3^3 + O(3^5)
            sage: a.add_bigoh(7)
            2 + 3 + 3^2 + 3^3 + O(3^5)
            sage: a.add_bigoh(3)
            2 + 3 + 3^2 + O(3^3)

        TESTS:

        Verify that :issue:`13591` has been resolved::

            sage: k(3).add_bigoh(-1)
            O(3^-1)"""
    def is_equal_to(self, _right, absprec=...) -> Any:
        """CAElement.is_equal_to(self, _right, absprec=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CA_template.pxi (starting at line 748)

        Determine whether the inputs are equal modulo
        `\\pi^{\\mbox{absprec}}`.

        INPUT:

        - ``right`` -- a `p`-adic element with the same parent

        - ``absprec`` -- integer, infinity, or ``None``

        EXAMPLES::

            sage: R = ZpCA(2, 6)
            sage: R(13).is_equal_to(R(13))
            True
            sage: R(13).is_equal_to(R(13+2^10))
            True
            sage: R(13).is_equal_to(R(17), 2)
            True
            sage: R(13).is_equal_to(R(17), 5)
            False
            sage: R(13).is_equal_to(R(13+2^10),absprec=10)
            Traceback (most recent call last):
            ...
            PrecisionError: elements not known to enough precision"""
    def is_zero(self, absprec=...) -> Any:
        """CAElement.is_zero(self, absprec=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CA_template.pxi (starting at line 687)

        Determine whether this element is zero modulo
        `\\pi^{\\mbox{absprec}}`.

        If ``absprec is None``, returns ``True`` if this element is
        indistinguishable from zero.

        INPUT:

        - ``absprec`` -- integer, infinity, or ``None``

        EXAMPLES::

            sage: R = ZpCA(17, 6)
            sage: R(0).is_zero()
            True
            sage: R(17^6).is_zero()
            True
            sage: R(17^2).is_zero(absprec=2)
            True
            sage: R(17^6).is_zero(absprec=10)
            Traceback (most recent call last):
            ...
            PrecisionError: not enough precision to determine if element is zero"""

    def polynomial(self, var=...) -> Any:
        """CAElement.polynomial(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/padics/CA_template.pxi (starting at line 943)

        Return a polynomial over the base ring that yields this element
        when evaluated at the generator of the parent.

        INPUT:

        - ``var`` -- string; the variable name for the polynomial

        EXAMPLES::

            sage: # needs sage.libs.flint
            sage: R.<a> = ZqCA(5^3)
            sage: a.polynomial()
            (1 + O(5^20))*x + O(5^20)
            sage: a.polynomial(var='y')
            (1 + O(5^20))*y + O(5^20)
            sage: (5*a^2 + R(25, 4)).polynomial()
            (5 + O(5^4))*x^2 + O(5^4)*x + 5^2 + O(5^4)"""
    @overload
    def polynomial(self) -> Any:
        """CAElement.polynomial(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/padics/CA_template.pxi (starting at line 943)

        Return a polynomial over the base ring that yields this element
        when evaluated at the generator of the parent.

        INPUT:

        - ``var`` -- string; the variable name for the polynomial

        EXAMPLES::

            sage: # needs sage.libs.flint
            sage: R.<a> = ZqCA(5^3)
            sage: a.polynomial()
            (1 + O(5^20))*x + O(5^20)
            sage: a.polynomial(var='y')
            (1 + O(5^20))*y + O(5^20)
            sage: (5*a^2 + R(25, 4)).polynomial()
            (5 + O(5^4))*x^2 + O(5^4)*x + 5^2 + O(5^4)"""

    def precision_absolute(self) -> Any:
        """CAElement.precision_absolute(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CA_template.pxi (starting at line 967)

        The absolute precision of this element.

        This is the power of the maximal ideal modulo which this
        element is defined.

        EXAMPLES::

            sage: R = Zp(7,4,'capped-abs'); a = R(7); a.precision_absolute()
            4"""

    def precision_relative(self) -> Any:
        """CAElement.precision_relative(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CA_template.pxi (starting at line 983)

        The relative precision of this element.

        This is the power of the maximal ideal modulo which the unit
        part of this element is defined.

        EXAMPLES::

            sage: R = Zp(7,4,'capped-abs'); a = R(7); a.precision_relative()
            3"""
    @overload
    def unit_part(self) -> pAdicTemplateElement:
        """CAElement.unit_part(self) -> pAdicTemplateElement

        File: /build/sagemath/src/sage/src/sage/rings/padics/CA_template.pxi (starting at line 999)

        Return the unit part of this element.

        EXAMPLES::

            sage: R = Zp(17,4,'capped-abs', 'val-unit')
            sage: a = R(18*17)
            sage: a.unit_part()
            18 + O(17^3)
            sage: type(a)
            <class 'sage.rings.padics.padic_capped_absolute_element.pAdicCappedAbsoluteElement'>
            sage: R(0).unit_part()
            O(17^0)"""

    def unit_part(self) -> Any:
        """CAElement.unit_part(self) -> pAdicTemplateElement

        File: /build/sagemath/src/sage/src/sage/rings/padics/CA_template.pxi (starting at line 999)

        Return the unit part of this element.

        EXAMPLES::

            sage: R = Zp(17,4,'capped-abs', 'val-unit')
            sage: a = R(18*17)
            sage: a.unit_part()
            18 + O(17^3)
            sage: type(a)
            <class 'sage.rings.padics.padic_capped_absolute_element.pAdicCappedAbsoluteElement'>
            sage: R(0).unit_part()
            O(17^0)"""

    def val_unit(self) -> Any:
        """CAElement.val_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CA_template.pxi (starting at line 1047)

        Return a 2-tuple, the first element set to the valuation of this
        element, and the second to the unit part of this element.

        For a zero element, the unit part is ``O(p^0)``.

        EXAMPLES::

            sage: R = ZpCA(5)
            sage: a = R(75, 6); b = a - a
            sage: a.val_unit()
            (2, 3 + O(5^4))
            sage: b.val_unit()
            (6, O(5^0))"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __copy__(self) -> Any:
        """CAElement.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CA_template.pxi (starting at line 156)

        Return a copy of this element.

        EXAMPLES::

            sage: a = ZpCA(5,6)(17); b = copy(a)
            sage: a == b
            True
            sage: a is b
            False"""
    def __hash__(self) -> Any:
        """CAElement.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CA_template.pxi (starting at line 1070)

        Hashing.

        .. WARNING::

            Hashing of `p`-adic elements will likely be deprecated soon.  See :issue:`11895`.

        EXAMPLES::

            sage: R = ZpCA(11, 5)
            sage: hash(R(3)) == hash(3)
            True"""
    def __invert__(self) -> Any:
        """CAElement.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CA_template.pxi (starting at line 260)

        Return the multiplicative inverse of this element.

        .. NOTE::

            The result always lives in the fraction field, even if this element
            is a unit.

        EXAMPLES::

            sage: R = ZpCA(17)
            sage: ~R(-1) == R(-1)
            True
            sage: ~R(5) * 5
            1 + O(17^20)
            sage: ~R(5)
            7 + 3*17 + 10*17^2 + 13*17^3 + 6*17^4 + 3*17^5 + 10*17^6 + 13*17^7
             + 6*17^8 + 3*17^9 + 10*17^10 + 13*17^11 + 6*17^12 + 3*17^13
             + 10*17^14 + 13*17^15 + 6*17^16 + 3*17^17 + 10*17^18 + 13*17^19 + O(17^20)
            sage: ~R(-1) == R(-1)  # indirect doctest
            True"""
    def __pow__(self, CAElementself, _right, dummy) -> Any:
        """CAElement.__pow__(CAElement self, _right, dummy)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CA_template.pxi (starting at line 399)

        Exponentiation.

        When ``right`` is divisible by `p` then one can get more
        precision than expected.  See the documentation in
        :mod:`sage.rings.padics.CR_template.pxi` for more details.

        For `p`-adic exponents, `a^b` is defined as `\\exp(b \\log(a))`.
        Since the `p`-adic logarithm is defined for `a` a unit, the
        same is true of exponentiation.

        INPUT:

        - ``_right`` -- currently integers and `p`-adic exponents are supported

        - ``dummy`` -- not used (Python's ``__pow__`` signature includes it)

        EXAMPLES::

            sage: R = ZpCA(11, 5)
            sage: R(1/2)^5
            10 + 7*11 + 11^2 + 5*11^3 + 4*11^4 + O(11^5)
            sage: R(1/32)
            10 + 7*11 + 11^2 + 5*11^3 + 4*11^4 + O(11^5)
            sage: R(1/2)^5 == R(1/32)
            True
            sage: R(3)^1000
            1 + 4*11^2 + 3*11^3 + 7*11^4 + O(11^5)

        `p`-adic exponents are supported::

            sage: R = ZpCA(11, 5, print_mode='terse')
            sage: a = R(3/14, 3); b = R(8/9); c = R(11,2)
            sage: a
            1046 + O(11^3)
            sage: b
            35790 + O(11^5)
            sage: a^b
            177 + O(11^3)
            sage: a^35790
            177 + O(11^3)
            sage: a^c
            848 + O(11^3)
            sage: (a.log()*c).exp()
            848 + O(11^3)

            sage: R = ZpCA(19, 5, print_mode='series')
            sage: a = R(8/5,4); a
            13 + 7*19 + 11*19^2 + 7*19^3 + O(19^4)
            sage: a^(R(19/7))
            1 + 14*19^2 + 11*19^3 + 13*19^4 + O(19^5)
            sage: (a // R.teichmuller(13))^(R(19/7))
            1 + 14*19^2 + 11*19^3 + 13*19^4 + O(19^5)
            sage: (a.log() * 19/7).exp()
            1 + 14*19^2 + 11*19^3 + 13*19^4 + O(19^5)

        Check that :issue:`31875` is fixed::

            sage: R(1)^R(0)
            1 + O(19^5)

            sage: # needs sage.libs.flint
            sage: S.<a> = ZqCA(4)
            sage: S(1)^S(0)
            1 + O(2^20)"""
    def __reduce__(self) -> Any:
        """CAElement.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CA_template.pxi (starting at line 185)

        Return a tuple of a function and data that can be used to unpickle this
        element.

        TESTS::

            sage: a = ZpCA(5)(-3)
            sage: type(a)
            <class 'sage.rings.padics.padic_capped_absolute_element.pAdicCappedAbsoluteElement'>
            sage: loads(dumps(a)) == a
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

class PowComputer_(sage.rings.padics.pow_computer_flint.PowComputer_flint_unram):
    """PowComputer_(Integer prime, long cache_limit, long prec_cap, long ram_prec_cap, bool in_field, poly=None)

    File: /build/sagemath/src/sage/src/sage/rings/padics/qadic_flint_CA.pyx (starting at line 5)

    A PowComputer for a capped-absolute unramified ring."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, Integerprime, longcache_limit, longprec_cap, longram_prec_cap, boolin_field, poly=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/qadic_flint_CA.pyx (starting at line 9)

                Initialization.

                EXAMPLES::

                    sage: R.<a> = ZqCA(125)
                    sage: type(R.prime_pow)
                    <class 'sage.rings.padics.qadic_flint_CA.PowComputer_'>
                    sage: R.prime_pow._prec_type
                    'capped-abs'
        """

class pAdicCoercion_CA_frac_field(sage.rings.morphism.RingHomomorphism):
    """pAdicCoercion_CA_frac_field(R, K)

    File: /build/sagemath/src/sage/src/sage/rings/padics/CA_template.pxi (starting at line 1413)

    The canonical inclusion of Zq into its fraction field.

    EXAMPLES::

        sage: # needs sage.libs.flint
        sage: R.<a> = ZqCA(27, implementation='FLINT')
        sage: K = R.fraction_field()
        sage: f = K.coerce_map_from(R); f
        Ring morphism:
          From: 3-adic Unramified Extension Ring in a defined by x^3 + 2*x + 1
          To:   3-adic Unramified Extension Field in a defined by x^3 + 2*x + 1

    TESTS::

        sage: TestSuite(f).run()                                                        # needs sage.libs.flint"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, R, K) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/CA_template.pxi (starting at line 1431)

                Initialization.

                EXAMPLES::

                    sage: # needs sage.libs.flint
                    sage: R.<a> = ZqCA(27, implementation='FLINT')
                    sage: K = R.fraction_field()
                    sage: f = K.coerce_map_from(R); type(f)
                    <class 'sage.rings.padics.qadic_flint_CA.pAdicCoercion_CA_frac_field'>
        """

    def is_injective(self) -> Any:
        """pAdicCoercion_CA_frac_field.is_injective(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CA_template.pxi (starting at line 1607)

        Return whether this map is injective.

        EXAMPLES::

            sage: # needs sage.libs.flint
            sage: R.<a> = ZqCA(9, implementation='FLINT')
            sage: K = R.fraction_field()
            sage: f = K.coerce_map_from(R)
            sage: f.is_injective()
            True"""

    def is_surjective(self) -> Any:
        """pAdicCoercion_CA_frac_field.is_surjective(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CA_template.pxi (starting at line 1622)

        Return whether this map is surjective.

        EXAMPLES::

            sage: # needs sage.libs.flint
            sage: R.<a> = ZqCA(9, implementation='FLINT')
            sage: K = R.fraction_field()
            sage: f = K.coerce_map_from(R)
            sage: f.is_surjective()
            False"""

    def section(self) -> Any:
        """pAdicCoercion_CA_frac_field.section(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CA_template.pxi (starting at line 1526)

        Return a map back to the ring that converts elements of
        nonnegative valuation.

        EXAMPLES::

            sage: # needs sage.libs.flint
            sage: R.<a> = ZqCA(27, implementation='FLINT')
            sage: K = R.fraction_field()
            sage: f = K.coerce_map_from(R)
            sage: f(K.gen())
            a + O(3^20)
            sage: f.section()
            Generic morphism:
              From: 3-adic Unramified Extension Field in a defined by x^3 + 2*x + 1
              To:   3-adic Unramified Extension Ring in a defined by x^3 + 2*x + 1"""

class pAdicCoercion_ZZ_CA(sage.rings.morphism.RingHomomorphism):
    """pAdicCoercion_ZZ_CA(R)

    File: /build/sagemath/src/sage/src/sage/rings/padics/CA_template.pxi (starting at line 1086)

    The canonical inclusion from the ring of integers to a capped absolute
    ring.

    EXAMPLES::

        sage: f = ZpCA(5).coerce_map_from(ZZ); f
        Ring morphism:
          From: Integer Ring
          To:   5-adic Ring with capped absolute precision 20

    TESTS::

        sage: TestSuite(f).run()"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, R) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/CA_template.pxi (starting at line 1102)

                Initialization.

                EXAMPLES::

                    sage: f = ZpCA(5).coerce_map_from(ZZ); type(f)
                    <class 'sage.rings.padics.padic_capped_absolute_element.pAdicCoercion_ZZ_CA'>
        """

    def section(self) -> Any:
        """pAdicCoercion_ZZ_CA.section(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/CA_template.pxi (starting at line 1219)

        Return a map back to the ring of integers that approximates an element
        by an integer.

        EXAMPLES::

            sage: f = ZpCA(5).coerce_map_from(ZZ).section()
            sage: f(ZpCA(5)(-1)) - 5^20
            -1"""

class pAdicConvert_CA_ZZ(sage.rings.morphism.RingMap):
    """pAdicConvert_CA_ZZ(R)

    File: /build/sagemath/src/sage/src/sage/rings/padics/CA_template.pxi (starting at line 1236)

    The map from a capped absolute ring back to the ring of integers that
    returns the smallest nonnegative integer approximation to its input
    which is accurate up to the precision.

    Raises a :exc:`ValueError` if the input is not in the closure of the image
    of the ring of integers.

    EXAMPLES::

        sage: f = ZpCA(5).coerce_map_from(ZZ).section(); f
        Set-theoretic ring morphism:
          From: 5-adic Ring with capped absolute precision 20
          To:   Integer Ring"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, R) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/CA_template.pxi (starting at line 1252)

                Initialization.

                EXAMPLES::

                    sage: f = ZpCA(5).coerce_map_from(ZZ).section(); type(f)
                    <class 'sage.rings.padics.padic_capped_absolute_element.pAdicConvert_CA_ZZ'>
                    sage: f.category()
                    Category of homsets of sets
        """

class pAdicConvert_CA_frac_field(sage.categories.morphism.Morphism):
    """pAdicConvert_CA_frac_field(K, R)

    File: /build/sagemath/src/sage/src/sage/rings/padics/CA_template.pxi (starting at line 1638)

    The section of the inclusion from `\\ZZ_q` to its fraction field.

    EXAMPLES::

        sage: # needs sage.libs.flint
        sage: R.<a> = ZqCA(27, implementation='FLINT')
        sage: K = R.fraction_field()
        sage: f = R.convert_map_from(K); f
        Generic morphism:
          From: 3-adic Unramified Extension Field in a defined by x^3 + 2*x + 1
          To:   3-adic Unramified Extension Ring in a defined by x^3 + 2*x + 1"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, K, R) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/CA_template.pxi (starting at line 1652)

                Initialization.

                EXAMPLES::

                    sage: # needs sage.libs.flint
                    sage: R.<a> = ZqCA(27, implementation='FLINT')
                    sage: K = R.fraction_field()
                    sage: f = R.convert_map_from(K); type(f)
                    <class 'sage.rings.padics.qadic_flint_CA.pAdicConvert_CA_frac_field'>
        """

class pAdicConvert_QQ_CA(sage.categories.morphism.Morphism):
    """pAdicConvert_QQ_CA(R)

    File: /build/sagemath/src/sage/src/sage/rings/padics/CA_template.pxi (starting at line 1285)

    The inclusion map from the rationals to a capped absolute ring that is
    defined on all elements with nonnegative `p`-adic valuation.

    EXAMPLES::

        sage: f = ZpCA(5).convert_map_from(QQ); f
        Generic morphism:
          From: Rational Field
          To:   5-adic Ring with capped absolute precision 20"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, R) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/CA_template.pxi (starting at line 1297)

                Initialization.

                EXAMPLES::

                    sage: f = ZpCA(5).convert_map_from(QQ); type(f)
                    <class 'sage.rings.padics.padic_capped_absolute_element.pAdicConvert_QQ_CA'>
        """

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

class qAdicCappedAbsoluteElement(CAElement):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

    def frobenius(self) -> Any:
        """frobenius_unram(self, arithmetic=True)

        File: /build/sagemath/src/sage/src/sage/libs/linkages/padics/unram_shared.pxi (starting at line 4)

        Return the image of this element under the Frobenius automorphism
        applied to its parent.

        INPUT:

        - ``self`` -- an element of an unramified extension
        - ``arithmetic`` -- whether to apply the arithmetic Frobenius (acting
          by raising to the `p`-th power on the residue field). If ``False`` is
          provided, the image of geometric Frobenius (raising to the `(1/p)`-th
          power on the residue field) will be returned instead.

        EXAMPLES::

            sage: R.<a> = Zq(5^4,3)
            sage: a.frobenius()
            (a^3 + a^2 + 3*a) + (3*a + 1)*5 + (2*a^3 + 2*a^2 + 2*a)*5^2 + O(5^3)
            sage: f = R.defining_polynomial()
            sage: f(a)
            O(5^3)
            sage: f(a.frobenius())
            O(5^3)
            sage: for i in range(4): a = a.frobenius()
            sage: a
            a + O(5^3)

            sage: R.<a> = Zq(5^4,3)
            sage: a.frobenius(arithmetic=False)
            (3*a^3 + 3*a^2 + a) + (a^3 + 4*a^2 + a + 4)*5 + (3*a^2 + 2*a + 3)*5^2 + O(5^3)

            sage: K.<a> = Qq(7^3,4)
            sage: b = (a+1)/7
            sage: c = b.frobenius(); c
            (3*a^2 + 5*a + 1)*7^-1 + (6*a^2 + 6*a + 6) + (4*a^2 + 3*a + 4)*7 + (6*a^2 + a + 6)*7^2 + O(7^3)
            sage: c.frobenius().frobenius()
            (a + 1)*7^-1 + O(7^3)

        An error will be raised if the parent of ``self`` is a ramified extension::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = Qp(5).extension(x^2 - 5)
            sage: a.frobenius()
            Traceback (most recent call last):
            ...
            NotImplementedError: Frobenius automorphism only implemented for unramified extensions

        TESTS:

        We check that :issue:`23575` is resolved::

            sage: x = R.random_element()
            sage: x.frobenius(arithmetic=false).frobenius() == x
            True"""
    @overload
    def frobenius(self, arithmetic=...) -> Any:
        """frobenius_unram(self, arithmetic=True)

        File: /build/sagemath/src/sage/src/sage/libs/linkages/padics/unram_shared.pxi (starting at line 4)

        Return the image of this element under the Frobenius automorphism
        applied to its parent.

        INPUT:

        - ``self`` -- an element of an unramified extension
        - ``arithmetic`` -- whether to apply the arithmetic Frobenius (acting
          by raising to the `p`-th power on the residue field). If ``False`` is
          provided, the image of geometric Frobenius (raising to the `(1/p)`-th
          power on the residue field) will be returned instead.

        EXAMPLES::

            sage: R.<a> = Zq(5^4,3)
            sage: a.frobenius()
            (a^3 + a^2 + 3*a) + (3*a + 1)*5 + (2*a^3 + 2*a^2 + 2*a)*5^2 + O(5^3)
            sage: f = R.defining_polynomial()
            sage: f(a)
            O(5^3)
            sage: f(a.frobenius())
            O(5^3)
            sage: for i in range(4): a = a.frobenius()
            sage: a
            a + O(5^3)

            sage: R.<a> = Zq(5^4,3)
            sage: a.frobenius(arithmetic=False)
            (3*a^3 + 3*a^2 + a) + (a^3 + 4*a^2 + a + 4)*5 + (3*a^2 + 2*a + 3)*5^2 + O(5^3)

            sage: K.<a> = Qq(7^3,4)
            sage: b = (a+1)/7
            sage: c = b.frobenius(); c
            (3*a^2 + 5*a + 1)*7^-1 + (6*a^2 + 6*a + 6) + (4*a^2 + 3*a + 4)*7 + (6*a^2 + a + 6)*7^2 + O(7^3)
            sage: c.frobenius().frobenius()
            (a + 1)*7^-1 + O(7^3)

        An error will be raised if the parent of ``self`` is a ramified extension::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = Qp(5).extension(x^2 - 5)
            sage: a.frobenius()
            Traceback (most recent call last):
            ...
            NotImplementedError: Frobenius automorphism only implemented for unramified extensions

        TESTS:

        We check that :issue:`23575` is resolved::

            sage: x = R.random_element()
            sage: x.frobenius(arithmetic=false).frobenius() == x
            True"""

    def frobenius(self) -> Any:
        """frobenius_unram(self, arithmetic=True)

        File: /build/sagemath/src/sage/src/sage/libs/linkages/padics/unram_shared.pxi (starting at line 4)

        Return the image of this element under the Frobenius automorphism
        applied to its parent.

        INPUT:

        - ``self`` -- an element of an unramified extension
        - ``arithmetic`` -- whether to apply the arithmetic Frobenius (acting
          by raising to the `p`-th power on the residue field). If ``False`` is
          provided, the image of geometric Frobenius (raising to the `(1/p)`-th
          power on the residue field) will be returned instead.

        EXAMPLES::

            sage: R.<a> = Zq(5^4,3)
            sage: a.frobenius()
            (a^3 + a^2 + 3*a) + (3*a + 1)*5 + (2*a^3 + 2*a^2 + 2*a)*5^2 + O(5^3)
            sage: f = R.defining_polynomial()
            sage: f(a)
            O(5^3)
            sage: f(a.frobenius())
            O(5^3)
            sage: for i in range(4): a = a.frobenius()
            sage: a
            a + O(5^3)

            sage: R.<a> = Zq(5^4,3)
            sage: a.frobenius(arithmetic=False)
            (3*a^3 + 3*a^2 + a) + (a^3 + 4*a^2 + a + 4)*5 + (3*a^2 + 2*a + 3)*5^2 + O(5^3)

            sage: K.<a> = Qq(7^3,4)
            sage: b = (a+1)/7
            sage: c = b.frobenius(); c
            (3*a^2 + 5*a + 1)*7^-1 + (6*a^2 + 6*a + 6) + (4*a^2 + 3*a + 4)*7 + (6*a^2 + a + 6)*7^2 + O(7^3)
            sage: c.frobenius().frobenius()
            (a + 1)*7^-1 + O(7^3)

        An error will be raised if the parent of ``self`` is a ramified extension::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = Qp(5).extension(x^2 - 5)
            sage: a.frobenius()
            Traceback (most recent call last):
            ...
            NotImplementedError: Frobenius automorphism only implemented for unramified extensions

        TESTS:

        We check that :issue:`23575` is resolved::

            sage: x = R.random_element()
            sage: x.frobenius(arithmetic=false).frobenius() == x
            True"""
    @overload
    def frobenius(self, arithmetic=...) -> Any:
        """frobenius_unram(self, arithmetic=True)

        File: /build/sagemath/src/sage/src/sage/libs/linkages/padics/unram_shared.pxi (starting at line 4)

        Return the image of this element under the Frobenius automorphism
        applied to its parent.

        INPUT:

        - ``self`` -- an element of an unramified extension
        - ``arithmetic`` -- whether to apply the arithmetic Frobenius (acting
          by raising to the `p`-th power on the residue field). If ``False`` is
          provided, the image of geometric Frobenius (raising to the `(1/p)`-th
          power on the residue field) will be returned instead.

        EXAMPLES::

            sage: R.<a> = Zq(5^4,3)
            sage: a.frobenius()
            (a^3 + a^2 + 3*a) + (3*a + 1)*5 + (2*a^3 + 2*a^2 + 2*a)*5^2 + O(5^3)
            sage: f = R.defining_polynomial()
            sage: f(a)
            O(5^3)
            sage: f(a.frobenius())
            O(5^3)
            sage: for i in range(4): a = a.frobenius()
            sage: a
            a + O(5^3)

            sage: R.<a> = Zq(5^4,3)
            sage: a.frobenius(arithmetic=False)
            (3*a^3 + 3*a^2 + a) + (a^3 + 4*a^2 + a + 4)*5 + (3*a^2 + 2*a + 3)*5^2 + O(5^3)

            sage: K.<a> = Qq(7^3,4)
            sage: b = (a+1)/7
            sage: c = b.frobenius(); c
            (3*a^2 + 5*a + 1)*7^-1 + (6*a^2 + 6*a + 6) + (4*a^2 + 3*a + 4)*7 + (6*a^2 + a + 6)*7^2 + O(7^3)
            sage: c.frobenius().frobenius()
            (a + 1)*7^-1 + O(7^3)

        An error will be raised if the parent of ``self`` is a ramified extension::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = Qp(5).extension(x^2 - 5)
            sage: a.frobenius()
            Traceback (most recent call last):
            ...
            NotImplementedError: Frobenius automorphism only implemented for unramified extensions

        TESTS:

        We check that :issue:`23575` is resolved::

            sage: x = R.random_element()
            sage: x.frobenius(arithmetic=false).frobenius() == x
            True"""
    def matrix_mod_pn(self) -> Any:
        """qAdicCappedAbsoluteElement.matrix_mod_pn(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/qadic_flint_CA.pyx (starting at line 29)

        Return the matrix of right multiplication by the element on
        the power basis `1, x, x^2, \\ldots, x^{d-1}` for this
        extension field.  Thus the *rows* of this matrix give the
        images of each of the `x^i`.  The entries of the matrices are
        IntegerMod elements, defined modulo ``p^(self.absprec() / e)``.

        EXAMPLES::

            sage: R.<a> = ZqCA(5^5,5)
            sage: b = (5 + 15*a)^3
            sage: b.matrix_mod_pn()
            [ 125 1125  250  250    0]
            [   0  125 1125  250  250]
            [2375 2125  125 1125  250]
            [2375 1375 2125  125 1125]
            [2875 1000 1375 2125  125]

            sage: M = R(0,3).matrix_mod_pn(); M == 0
            True
            sage: M.base_ring()
            Ring of integers modulo 125"""
    def norm(self, *args, **kwargs):
        """norm_unram(self, base=None)

        File: /build/sagemath/src/sage/src/sage/libs/linkages/padics/unram_shared.pxi (starting at line 85)

        Return the absolute or relative norm of this element.

        .. WARNING::

            This is not the `p`-adic absolute value.  This is a
            field theoretic norm down to a ground ring.  If you want the
            `p`-adic absolute value, use the ``abs()`` function instead.

        INPUT:

        - ``base`` -- a subfield of the parent `L` of this element; the norm is the
          relative norm from ``L`` to ``base``. Defaults to the absolute norm down
          to `\\QQ_p` or `\\ZZ_p`.

        EXAMPLES::

            sage: R = ZpCR(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 +125*x - 5
            sage: W.<w> = R.ext(f)
            sage: ((1+2*w)^5).norm()
            1 + 5^2 + O(5^5)
            sage: ((1+2*w)).norm()^5
            1 + 5^2 + O(5^5)

        TESTS::

            sage: R = ZpCA(5,5)
            sage: S.<x> = ZZ[]
            sage: f = x^5 + 75*x^3 - 15*x^2 +125*x - 5
            sage: W.<w> = R.ext(f)
            sage: ((1+2*w)^5).norm()
            1 + 5^2 + O(5^5)
            sage: ((1+2*w)).norm()^5
            1 + 5^2 + O(5^5)
            sage: R = ZpFM(5,5)
            sage: S.<x> = ZZ[]
            sage: f = x^5 + 75*x^3 - 15*x^2 +125*x - 5
            sage: W.<w> = R.ext(f)
            sage: ((1+2*w)^5).norm()
            1 + 5^2
            sage: ((1+2*w)).norm()^5
            1 + 5^2

        TESTS:

        Check that :issue:`11586` has been resolved::

            sage: R.<x> = QQ[]
            sage: f = x^2 + 3*x + 1
            sage: M.<a> = Qp(7).extension(f)
            sage: M(7).norm()
            7^2 + O(7^22)
            sage: b = 7*a + 35
            sage: b.norm()
            4*7^2 + 7^3 + O(7^22)
            sage: b*b.frobenius()
            4*7^2 + 7^3 + O(7^22)

        Check that :issue:`31845` is fixed::

            sage: R.<a> = Zq(4)
            sage: (a - a).norm()
            O(2^20)"""
    def trace(self, *args, **kwargs):
        """trace_unram(self, base=None)

        File: /build/sagemath/src/sage/src/sage/libs/linkages/padics/unram_shared.pxi (starting at line 172)

        Return the absolute or relative trace of this element.

        If ``base`` is given then ``base`` must be a subfield of the
        parent `L` of ``self``, in which case the trace is the relative
        trace from `L` to ``base``.

        In all other cases, the trace is the absolute trace down to
        `\\QQ_p` or `\\ZZ_p`.

        EXAMPLES::

            sage: R = ZpCR(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 +125*x - 5
            sage: W.<w> = R.ext(f)
            sage: a = (2+3*w)^7
            sage: b = (6+w^3)^5
            sage: a.trace()
            3*5 + 2*5^2 + 3*5^3 + 2*5^4 + O(5^5)
            sage: a.trace() + b.trace()
            4*5 + 5^2 + 5^3 + 2*5^4 + O(5^5)
            sage: (a+b).trace()
            4*5 + 5^2 + 5^3 + 2*5^4 + O(5^5)

        TESTS::

            sage: R = ZpCA(5,5)
            sage: S.<x> = ZZ[]
            sage: f = x^5 + 75*x^3 - 15*x^2 +125*x - 5
            sage: W.<w> = R.ext(f)
            sage: a = (2+3*w)^7
            sage: b = (6+w^3)^5
            sage: a.trace()
            3*5 + 2*5^2 + 3*5^3 + 2*5^4 + O(5^5)
            sage: a.trace() + b.trace()
            4*5 + 5^2 + 5^3 + 2*5^4 + O(5^5)
            sage: (a+b).trace()
            4*5 + 5^2 + 5^3 + 2*5^4 + O(5^5)
            sage: R = ZpFM(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 +125*x - 5
            sage: W.<w> = R.ext(f)
            sage: a = (2+3*w)^7
            sage: b = (6+w^3)^5
            sage: a.trace()
            3*5 + 2*5^2 + 3*5^3 + 2*5^4
            sage: a.trace() + b.trace()
            4*5 + 5^2 + 5^3 + 2*5^4
            sage: (a+b).trace()
            4*5 + 5^2 + 5^3 + 2*5^4

        Check that :issue:`31845` is fixed::

            sage: R.<a> = Zq(4)
            sage: (a - a).trace()
            O(2^20)"""
    def __hash__(self) -> Any:
        """qAdicCappedAbsoluteElement.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/qadic_flint_CA.pyx (starting at line 111)

        Raise a :exc:`TypeError` since this element is not hashable
        (:issue:`11895`).

        TESTS::

            sage: K.<a> = ZqCA(9)
            sage: hash(a)
            Traceback (most recent call last):
            ...
            TypeError: unhashable type: 'sage.rings.padics.qadic_flint_CA.qAdicCappedAbsoluteElement'"""

class qAdicCoercion_Zq_Qq(sage.rings.morphism.RingHomomorphism):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class qAdicConvert_Qq_Zq(sage.categories.morphism.Morphism):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
