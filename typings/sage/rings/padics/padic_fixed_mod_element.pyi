import _cython_3_2_1
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

make_pAdicFixedModElement: _cython_3_2_1.cython_function_or_method
unpickle_fme_v2: _cython_3_2_1.cython_function_or_method

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

class FMElement(pAdicTemplateElement):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def add_bigoh(self, absprec) -> Any:
        """FMElement.add_bigoh(self, absprec)

        File: /build/sagemath/src/sage/src/sage/rings/padics/FM_template.pxi (starting at line 463)

        Return a new element truncated modulo `\\pi^{\\mbox{absprec}}`.

        INPUT:

        - ``absprec`` -- integer or infinity

        OUTPUT: a new element truncated modulo `\\pi^{\\mbox{absprec}}`

        EXAMPLES::

            sage: R = Zp(7,4,'fixed-mod','series'); a = R(8); a.add_bigoh(1)
            1

        TESTS:

        We handle very large and very small values for ``absprec`` correctly::

            sage: a = R(7)
            sage: a.add_bigoh(2^1000)
            7
            sage: a.add_bigoh(-2^1000)
            0"""
    def is_equal_to(self, _right, absprec=...) -> Any:
        """FMElement.is_equal_to(self, _right, absprec=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/FM_template.pxi (starting at line 579)

        Return whether this element is equal to ``right`` modulo `p^{\\mbox{absprec}}`.

        If ``absprec`` is ``None``, returns if ``self == 0``.

        INPUT:

        - ``right`` -- a `p`-adic element with the same parent
        - ``absprec`` -- positive integer or ``None`` (default: ``None``)

        EXAMPLES::

            sage: R = ZpFM(2, 6)
            sage: R(13).is_equal_to(R(13))
            True
            sage: R(13).is_equal_to(R(13+2^10))
            True
            sage: R(13).is_equal_to(R(17), 2)
            True
            sage: R(13).is_equal_to(R(17), 5)
            False"""
    def is_zero(self, absprec=...) -> Any:
        """FMElement.is_zero(self, absprec=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/FM_template.pxi (starting at line 536)

        Return whether ``self`` is zero modulo `\\pi^{\\mbox{absprec}}`.

        INPUT:

        - ``absprec`` -- integer

        EXAMPLES::

            sage: R = ZpFM(17, 6)
            sage: R(0).is_zero()
            True
            sage: R(17^6).is_zero()
            True
            sage: R(17^2).is_zero(absprec=2)
            True"""
    @overload
    def polynomial(self, var=...) -> Any:
        """FMElement.polynomial(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/padics/FM_template.pxi (starting at line 727)

        Return a polynomial over the base ring that yields this element
        when evaluated at the generator of the parent.

        INPUT:

        - ``var`` -- string, the variable name for the polynomial

        EXAMPLES::

            sage: # needs sage.libs.flint
            sage: R.<a> = ZqFM(5^3)
            sage: a.polynomial()
            x
            sage: a.polynomial(var='y')
            y
            sage: (5*a^2 + 25).polynomial()
            5*x^2 + 5^2"""
    @overload
    def polynomial(self) -> Any:
        """FMElement.polynomial(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/padics/FM_template.pxi (starting at line 727)

        Return a polynomial over the base ring that yields this element
        when evaluated at the generator of the parent.

        INPUT:

        - ``var`` -- string, the variable name for the polynomial

        EXAMPLES::

            sage: # needs sage.libs.flint
            sage: R.<a> = ZqFM(5^3)
            sage: a.polynomial()
            x
            sage: a.polynomial(var='y')
            y
            sage: (5*a^2 + 25).polynomial()
            5*x^2 + 5^2"""
    @overload
    def polynomial(self, var=...) -> Any:
        """FMElement.polynomial(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/padics/FM_template.pxi (starting at line 727)

        Return a polynomial over the base ring that yields this element
        when evaluated at the generator of the parent.

        INPUT:

        - ``var`` -- string, the variable name for the polynomial

        EXAMPLES::

            sage: # needs sage.libs.flint
            sage: R.<a> = ZqFM(5^3)
            sage: a.polynomial()
            x
            sage: a.polynomial(var='y')
            y
            sage: (5*a^2 + 25).polynomial()
            5*x^2 + 5^2"""
    @overload
    def polynomial(self) -> Any:
        """FMElement.polynomial(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/padics/FM_template.pxi (starting at line 727)

        Return a polynomial over the base ring that yields this element
        when evaluated at the generator of the parent.

        INPUT:

        - ``var`` -- string, the variable name for the polynomial

        EXAMPLES::

            sage: # needs sage.libs.flint
            sage: R.<a> = ZqFM(5^3)
            sage: a.polynomial()
            x
            sage: a.polynomial(var='y')
            y
            sage: (5*a^2 + 25).polynomial()
            5*x^2 + 5^2"""
    @overload
    def precision_absolute(self) -> Any:
        """FMElement.precision_absolute(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/FM_template.pxi (starting at line 751)

        The absolute precision of this element.

        EXAMPLES::

            sage: R = Zp(7,4,'fixed-mod'); a = R(7); a.precision_absolute()
            4"""
    @overload
    def precision_absolute(self) -> Any:
        """FMElement.precision_absolute(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/FM_template.pxi (starting at line 751)

        The absolute precision of this element.

        EXAMPLES::

            sage: R = Zp(7,4,'fixed-mod'); a = R(7); a.precision_absolute()
            4"""
    @overload
    def precision_relative(self) -> Any:
        """FMElement.precision_relative(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/FM_template.pxi (starting at line 764)

        The relative precision of this element.

        EXAMPLES::

            sage: R = Zp(7,4,'fixed-mod'); a = R(7); a.precision_relative()
            3
            sage: a = R(0); a.precision_relative()
            0"""
    @overload
    def precision_relative(self) -> Any:
        """FMElement.precision_relative(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/FM_template.pxi (starting at line 764)

        The relative precision of this element.

        EXAMPLES::

            sage: R = Zp(7,4,'fixed-mod'); a = R(7); a.precision_relative()
            3
            sage: a = R(0); a.precision_relative()
            0"""
    @overload
    def precision_relative(self) -> Any:
        """FMElement.precision_relative(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/FM_template.pxi (starting at line 764)

        The relative precision of this element.

        EXAMPLES::

            sage: R = Zp(7,4,'fixed-mod'); a = R(7); a.precision_relative()
            3
            sage: a = R(0); a.precision_relative()
            0"""
    @overload
    def unit_part(self) -> pAdicTemplateElement:
        """FMElement.unit_part(self) -> pAdicTemplateElement

        File: /build/sagemath/src/sage/src/sage/rings/padics/FM_template.pxi (starting at line 779)

        Return the unit part of ``self``.

        If the valuation of ``self`` is positive, then the high digits of the
        result will be zero.

        EXAMPLES::

            sage: R = Zp(17, 4, 'fixed-mod')
            sage: R(5).unit_part()
            5
            sage: R(18*17).unit_part()
            1 + 17
            sage: R(0).unit_part()
            0
            sage: type(R(5).unit_part())
            <class 'sage.rings.padics.padic_fixed_mod_element.pAdicFixedModElement'>
            sage: R = ZpFM(5, 5); a = R(75); a.unit_part()
            3"""
    @overload
    def unit_part(self) -> Any:
        """FMElement.unit_part(self) -> pAdicTemplateElement

        File: /build/sagemath/src/sage/src/sage/rings/padics/FM_template.pxi (starting at line 779)

        Return the unit part of ``self``.

        If the valuation of ``self`` is positive, then the high digits of the
        result will be zero.

        EXAMPLES::

            sage: R = Zp(17, 4, 'fixed-mod')
            sage: R(5).unit_part()
            5
            sage: R(18*17).unit_part()
            1 + 17
            sage: R(0).unit_part()
            0
            sage: type(R(5).unit_part())
            <class 'sage.rings.padics.padic_fixed_mod_element.pAdicFixedModElement'>
            sage: R = ZpFM(5, 5); a = R(75); a.unit_part()
            3"""
    @overload
    def unit_part(self) -> Any:
        """FMElement.unit_part(self) -> pAdicTemplateElement

        File: /build/sagemath/src/sage/src/sage/rings/padics/FM_template.pxi (starting at line 779)

        Return the unit part of ``self``.

        If the valuation of ``self`` is positive, then the high digits of the
        result will be zero.

        EXAMPLES::

            sage: R = Zp(17, 4, 'fixed-mod')
            sage: R(5).unit_part()
            5
            sage: R(18*17).unit_part()
            1 + 17
            sage: R(0).unit_part()
            0
            sage: type(R(5).unit_part())
            <class 'sage.rings.padics.padic_fixed_mod_element.pAdicFixedModElement'>
            sage: R = ZpFM(5, 5); a = R(75); a.unit_part()
            3"""
    @overload
    def unit_part(self) -> Any:
        """FMElement.unit_part(self) -> pAdicTemplateElement

        File: /build/sagemath/src/sage/src/sage/rings/padics/FM_template.pxi (starting at line 779)

        Return the unit part of ``self``.

        If the valuation of ``self`` is positive, then the high digits of the
        result will be zero.

        EXAMPLES::

            sage: R = Zp(17, 4, 'fixed-mod')
            sage: R(5).unit_part()
            5
            sage: R(18*17).unit_part()
            1 + 17
            sage: R(0).unit_part()
            0
            sage: type(R(5).unit_part())
            <class 'sage.rings.padics.padic_fixed_mod_element.pAdicFixedModElement'>
            sage: R = ZpFM(5, 5); a = R(75); a.unit_part()
            3"""
    @overload
    def unit_part(self) -> Any:
        """FMElement.unit_part(self) -> pAdicTemplateElement

        File: /build/sagemath/src/sage/src/sage/rings/padics/FM_template.pxi (starting at line 779)

        Return the unit part of ``self``.

        If the valuation of ``self`` is positive, then the high digits of the
        result will be zero.

        EXAMPLES::

            sage: R = Zp(17, 4, 'fixed-mod')
            sage: R(5).unit_part()
            5
            sage: R(18*17).unit_part()
            1 + 17
            sage: R(0).unit_part()
            0
            sage: type(R(5).unit_part())
            <class 'sage.rings.padics.padic_fixed_mod_element.pAdicFixedModElement'>
            sage: R = ZpFM(5, 5); a = R(75); a.unit_part()
            3"""
    @overload
    def unit_part(self) -> Any:
        """FMElement.unit_part(self) -> pAdicTemplateElement

        File: /build/sagemath/src/sage/src/sage/rings/padics/FM_template.pxi (starting at line 779)

        Return the unit part of ``self``.

        If the valuation of ``self`` is positive, then the high digits of the
        result will be zero.

        EXAMPLES::

            sage: R = Zp(17, 4, 'fixed-mod')
            sage: R(5).unit_part()
            5
            sage: R(18*17).unit_part()
            1 + 17
            sage: R(0).unit_part()
            0
            sage: type(R(5).unit_part())
            <class 'sage.rings.padics.padic_fixed_mod_element.pAdicFixedModElement'>
            sage: R = ZpFM(5, 5); a = R(75); a.unit_part()
            3"""
    @overload
    def val_unit(self) -> Any:
        """FMElement.val_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/FM_template.pxi (starting at line 835)

        Return a 2-tuple, the first element set to the valuation of
        ``self``, and the second to the unit part of ``self``.

        If ``self == 0``, then the unit part is ``O(p^self.parent().precision_cap())``.

        EXAMPLES::

            sage: R = ZpFM(5,5)
            sage: a = R(75); b = a - a
            sage: a.val_unit()
            (2, 3)
            sage: b.val_unit()
            (5, 0)"""
    @overload
    def val_unit(self) -> Any:
        """FMElement.val_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/FM_template.pxi (starting at line 835)

        Return a 2-tuple, the first element set to the valuation of
        ``self``, and the second to the unit part of ``self``.

        If ``self == 0``, then the unit part is ``O(p^self.parent().precision_cap())``.

        EXAMPLES::

            sage: R = ZpFM(5,5)
            sage: a = R(75); b = a - a
            sage: a.val_unit()
            (2, 3)
            sage: b.val_unit()
            (5, 0)"""
    @overload
    def val_unit(self) -> Any:
        """FMElement.val_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/FM_template.pxi (starting at line 835)

        Return a 2-tuple, the first element set to the valuation of
        ``self``, and the second to the unit part of ``self``.

        If ``self == 0``, then the unit part is ``O(p^self.parent().precision_cap())``.

        EXAMPLES::

            sage: R = ZpFM(5,5)
            sage: a = R(75); b = a - a
            sage: a.val_unit()
            (2, 3)
            sage: b.val_unit()
            (5, 0)"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __copy__(self) -> Any:
        """FMElement.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/FM_template.pxi (starting at line 139)

        Return a copy of this element.

        EXAMPLES::

            sage: a = ZpFM(5,6)(17); b = copy(a)
            sage: a == b
            True
            sage: a is b
            False"""
    def __hash__(self) -> Any:
        """FMElement.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/FM_template.pxi (starting at line 856)

        Hashing.

        EXAMPLES::

            sage: R = ZpFM(11, 5)
            sage: hash(R(3)) == hash(3)
            True"""
    def __invert__(self) -> Any:
        """FMElement.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/FM_template.pxi (starting at line 237)

        Return multiplicative inverse of this element. The valuation
        of ``self`` must be zero.

        EXAMPLES::

            sage: R = Zp(7, 4, 'fixed-mod', 'series')
            sage: ~R(2)
            4 + 3*7 + 3*7^2 + 3*7^3
            sage: ~R(0)
            Traceback (most recent call last):
            ...
            ValueError: cannot invert non-unit
            sage: ~R(7)
            Traceback (most recent call last):
            ...
            ValueError: cannot invert non-unit"""
    def __pow__(self, FMElementself, _right, dummy) -> Any:
        """FMElement.__pow__(FMElement self, _right, dummy)

        File: /build/sagemath/src/sage/src/sage/rings/padics/FM_template.pxi (starting at line 349)

        Exponentiation by an integer

        EXAMPLES::

            sage: R = ZpFM(11, 5)
            sage: R(1/2)^5
            10 + 7*11 + 11^2 + 5*11^3 + 4*11^4
            sage: R(1/32)
            10 + 7*11 + 11^2 + 5*11^3 + 4*11^4
            sage: R(1/2)^5 == R(1/32)
            True
            sage: R(3)^1000  # indirect doctest
            1 + 4*11^2 + 3*11^3 + 7*11^4

        TESTS:

        We check that :issue:`15640` is resolved::

            sage: R(11)^-1
            Traceback (most recent call last):
            ...
            ValueError: cannot invert non-unit"""
    def __reduce__(self) -> Any:
        """FMElement.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/FM_template.pxi (starting at line 167)

        Return a tuple of a function and data that can be used to unpickle this
        element.

        EXAMPLES::

            sage: a = ZpFM(5)(-3)
            sage: type(a)
            <class 'sage.rings.padics.padic_fixed_mod_element.pAdicFixedModElement'>
            sage: loads(dumps(a)) == a
            True"""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""

class PowComputer_(sage.rings.padics.pow_computer.PowComputer_base):
    """PowComputer_(Integer prime, long cache_limit, long prec_cap, long ram_prec_cap, bool in_field)

    File: /build/sagemath/src/sage/src/sage/rings/padics/padic_fixed_mod_element.pyx (starting at line 35)

    A PowComputer for a fixed-modulus `p`-adic ring."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, Integerprime, longcache_limit, longprec_cap, longram_prec_cap, boolin_field) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/padic_fixed_mod_element.pyx (starting at line 39)

                Initialization.

                EXAMPLES::

                    sage: R = ZpFM(5)
                    sage: type(R.prime_pow)
                    <class 'sage.rings.padics.padic_fixed_mod_element.PowComputer_'>
                    sage: R.prime_pow._prec_type
                    'fixed-mod'
        """

class pAdicCoercion_FM_frac_field(sage.rings.morphism.RingHomomorphism):
    """pAdicCoercion_FM_frac_field(R, K)

    File: /build/sagemath/src/sage/src/sage/rings/padics/FM_template.pxi (starting at line 1174)

    The canonical inclusion of `\\ZZ_q` into its fraction field.

    EXAMPLES::

        sage: # needs sage.libs.flint
        sage: R.<a> = ZqFM(27, implementation='FLINT')
        sage: K = R.fraction_field()
        sage: f = K.coerce_map_from(R); f
        Ring morphism:
          From: 3-adic Unramified Extension Ring in a defined by x^3 + 2*x + 1
          To:   3-adic Unramified Extension Field in a defined by x^3 + 2*x + 1

    TESTS::

        sage: TestSuite(f).run()                                                        # needs sage.libs.flint"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, R, K) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/FM_template.pxi (starting at line 1192)

                Initialization.

                EXAMPLES::

                    sage: # needs sage.libs.flint
                    sage: R.<a> = ZqFM(27)
                    sage: K = R.fraction_field()
                    sage: f = K.coerce_map_from(R); type(f)
                    <class 'sage.rings.padics.qadic_flint_FM.pAdicCoercion_FM_frac_field'>
        """
    @overload
    def is_injective(self) -> Any:
        """pAdicCoercion_FM_frac_field.is_injective(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/FM_template.pxi (starting at line 1360)

        Return whether this map is injective.

        EXAMPLES::

            sage: # needs sage.libs.flint
            sage: R.<a> = ZqFM(9)
            sage: K = R.fraction_field()
            sage: f = K.coerce_map_from(R)
            sage: f.is_injective()
            True"""
    @overload
    def is_injective(self) -> Any:
        """pAdicCoercion_FM_frac_field.is_injective(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/FM_template.pxi (starting at line 1360)

        Return whether this map is injective.

        EXAMPLES::

            sage: # needs sage.libs.flint
            sage: R.<a> = ZqFM(9)
            sage: K = R.fraction_field()
            sage: f = K.coerce_map_from(R)
            sage: f.is_injective()
            True"""
    @overload
    def is_surjective(self) -> Any:
        """pAdicCoercion_FM_frac_field.is_surjective(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/FM_template.pxi (starting at line 1375)

        Return whether this map is surjective.

        EXAMPLES::

            sage: # needs sage.libs.flint
            sage: R.<a> = ZqFM(9)
            sage: K = R.fraction_field()
            sage: f = K.coerce_map_from(R)
            sage: f.is_surjective()
            False"""
    @overload
    def is_surjective(self) -> Any:
        """pAdicCoercion_FM_frac_field.is_surjective(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/FM_template.pxi (starting at line 1375)

        Return whether this map is surjective.

        EXAMPLES::

            sage: # needs sage.libs.flint
            sage: R.<a> = ZqFM(9)
            sage: K = R.fraction_field()
            sage: f = K.coerce_map_from(R)
            sage: f.is_surjective()
            False"""
    @overload
    def section(self) -> Any:
        """pAdicCoercion_FM_frac_field.section(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/FM_template.pxi (starting at line 1283)

        Return a map back to the ring that converts elements of
        nonnegative valuation.

        EXAMPLES::

            sage: # needs sage.libs.flint
            sage: R.<a> = ZqFM(27)
            sage: K = R.fraction_field()
            sage: f = K.coerce_map_from(R)
            sage: f.section()(K.gen())
            a"""
    @overload
    def section(self) -> Any:
        """pAdicCoercion_FM_frac_field.section(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/FM_template.pxi (starting at line 1283)

        Return a map back to the ring that converts elements of
        nonnegative valuation.

        EXAMPLES::

            sage: # needs sage.libs.flint
            sage: R.<a> = ZqFM(27)
            sage: K = R.fraction_field()
            sage: f = K.coerce_map_from(R)
            sage: f.section()(K.gen())
            a"""

class pAdicCoercion_ZZ_FM(sage.rings.morphism.RingHomomorphism):
    """pAdicCoercion_ZZ_FM(R)

    File: /build/sagemath/src/sage/src/sage/rings/padics/FM_template.pxi (starting at line 868)

    The canonical inclusion from `\\ZZ` to a fixed modulus ring.

    EXAMPLES::

        sage: f = ZpFM(5).coerce_map_from(ZZ); f
        Ring morphism:
          From: Integer Ring
          To:   5-adic Ring of fixed modulus 5^20

    TESTS::

        sage: TestSuite(f).run()"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, R) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/FM_template.pxi (starting at line 883)

                Initialization.

                EXAMPLES::

                    sage: f = ZpFM(5).coerce_map_from(ZZ); type(f)
                    <class 'sage.rings.padics.padic_fixed_mod_element.pAdicCoercion_ZZ_FM'>
        """
    def section(self) -> Any:
        """pAdicCoercion_ZZ_FM.section(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/FM_template.pxi (starting at line 992)

        Return a map back to `\\ZZ` that approximates an element of this
        `p`-adic ring by an integer.

        EXAMPLES::

            sage: f = ZpFM(5).coerce_map_from(ZZ).section()
            sage: f(ZpFM(5)(-1)) - 5^20
            -1"""

class pAdicConvert_FM_ZZ(sage.rings.morphism.RingMap):
    """pAdicConvert_FM_ZZ(R)

    File: /build/sagemath/src/sage/src/sage/rings/padics/FM_template.pxi (starting at line 1009)

    The map from a fixed modulus ring back to `\\ZZ` that returns the smallest
    nonnegative integer approximation to its input which is accurate up to the precision.

    If the input is not in the closure of the image of `\\ZZ`, raises a :exc:`ValueError`.

    EXAMPLES::

        sage: f = ZpFM(5).coerce_map_from(ZZ).section(); f
        Set-theoretic ring morphism:
          From: 5-adic Ring of fixed modulus 5^20
          To:   Integer Ring"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, R) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/FM_template.pxi (starting at line 1023)

                Initialization.

                EXAMPLES::

                    sage: f = ZpFM(5).coerce_map_from(ZZ).section(); type(f)
                    <class 'sage.rings.padics.padic_fixed_mod_element.pAdicConvert_FM_ZZ'>
                    sage: f.category()
                    Category of homsets of sets
        """

class pAdicConvert_FM_frac_field(sage.categories.morphism.Morphism):
    """pAdicConvert_FM_frac_field(K, R)

    File: /build/sagemath/src/sage/src/sage/rings/padics/FM_template.pxi (starting at line 1391)

    The section of the inclusion from `\\ZZ_q` to its fraction field.

    EXAMPLES::

        sage: # needs sage.libs.flint
        sage: R.<a> = ZqFM(27)
        sage: K = R.fraction_field()
        sage: f = R.convert_map_from(K); f
        Generic morphism:
          From: 3-adic Unramified Extension Field in a defined by x^3 + 2*x + 1
          To:   3-adic Unramified Extension Ring in a defined by x^3 + 2*x + 1"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, K, R) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/FM_template.pxi (starting at line 1405)

                Initialization.

                EXAMPLES::

                    sage: # needs sage.libs.flint
                    sage: R.<a> = ZqFM(27)
                    sage: K = R.fraction_field()
                    sage: f = R.convert_map_from(K); type(f)
                    <class 'sage.rings.padics.qadic_flint_FM.pAdicConvert_FM_frac_field'>
        """

class pAdicConvert_QQ_FM(sage.categories.morphism.Morphism):
    """pAdicConvert_QQ_FM(R)

    File: /build/sagemath/src/sage/src/sage/rings/padics/FM_template.pxi (starting at line 1056)

    The inclusion map from `\\QQ` to a fixed modulus ring that is defined
    on all elements with nonnegative `p`-adic valuation.

    EXAMPLES::

        sage: f = ZpFM(5).convert_map_from(QQ); f
        Generic morphism:
          From: Rational Field
          To:   5-adic Ring of fixed modulus 5^20"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, R) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/FM_template.pxi (starting at line 1068)

                Initialization.

                EXAMPLES::

                    sage: f = ZpFM(5).convert_map_from(QQ); type(f)
                    <class 'sage.rings.padics.padic_fixed_mod_element.pAdicConvert_QQ_FM'>
        """

class pAdicFixedModElement(FMElement):
    """File: /build/sagemath/src/sage/src/sage/rings/padics/padic_fixed_mod_element.pyx (starting at line 54)

        INPUT:

        - ``parent`` -- a ``pAdicRingFixedMod`` object

        - ``x`` -- input data to be converted into the parent

        - ``absprec`` -- ignored; for compatibility with other `p`-adic rings

        - ``relprec`` -- ignored; for compatibility with other `p`-adic rings

        .. NOTE::

            The following types are currently supported for x:

            - Integers
            - Rationals -- denominator must be relatively prime to `p`
            - FixedMod `p`-adics
            - Elements of ``IntegerModRing(p^k)`` for ``k`` less than or equal
              to the modulus

            The following types should be supported eventually:

            - Finite precision `p`-adics
            - Lazy `p`-adics
            - Elements of local extensions of THIS `p`-adic ring that actually
              lie in `\\ZZ_p`

        EXAMPLES::

            sage: R = Zp(5, 20, 'fixed-mod', 'terse')

        Construct from integers::

            sage: R(3)
            3
            sage: R(75)
            75
            sage: R(0)
            0

            sage: R(-1)
            95367431640624
            sage: R(-5)
            95367431640620

        Construct from rationals::

            sage: R(1/2)
            47683715820313
            sage: R(-7875/874)
            9493096742250
            sage: R(15/425)
            Traceback (most recent call last):
            ...
            ValueError: p divides denominator

        Construct from IntegerMod::

            sage: R(Integers(125)(3))
            3
            sage: R(Integers(5)(3))
            3
            sage: R(Integers(5^30)(3))
            3
            sage: R(Integers(5^30)(1+5^23))
            1
            sage: R(Integers(49)(3))
            Traceback (most recent call last):
            ...
            TypeError: p does not divide modulus 49

            sage: R(Integers(48)(3))
            Traceback (most recent call last):
            ...
            TypeError: p does not divide modulus 48

        Some other conversions::

            sage: R(R(5))
            5

        .. TODO:: doctests for converting from other types of `p`-adic rings
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def lift(self) -> Any:
        """pAdicFixedModElement.lift(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_fixed_mod_element.pyx (starting at line 139)

        Return an integer congruent to ``self`` modulo the precision.

        .. WARNING::

            Since fixed modulus elements don't track their precision,
            the result may not be correct modulo
            `i^{\\mathrm{prec_cap}}` if the element was defined by
            constructions that lost precision.

        EXAMPLES::

            sage: R = Zp(7,4,'fixed-mod'); a = R(8); a.lift()
            8
            sage: type(a.lift())
            <class 'sage.rings.integer.Integer'>"""
    def multiplicative_order(self) -> Any:
        """pAdicFixedModElement.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_fixed_mod_element.pyx (starting at line 328)

        Return the minimum possible multiplicative order of ``self``.

        OUTPUT:

        an integer -- the multiplicative order of this element.  This is the
        minimum multiplicative order of all elements of `\\ZZ_p` lifting this
        element to infinite precision.

         EXAMPLES::

            sage: R = ZpFM(7, 6)
            sage: R(1/3)
            5 + 4*7 + 4*7^2 + 4*7^3 + 4*7^4 + 4*7^5
            sage: R(1/3).multiplicative_order()
            +Infinity
            sage: R(7).multiplicative_order()
            +Infinity
            sage: R(1).multiplicative_order()
            1
            sage: R(-1).multiplicative_order()
            2
            sage: R.teichmuller(3).multiplicative_order()
            6"""
    def residue(self, absprec=..., field=..., check_prec=...) -> Any:
        """pAdicFixedModElement.residue(self, absprec=1, field=None, check_prec=False)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_fixed_mod_element.pyx (starting at line 247)

        Reduce ``self`` modulo `p^\\mathrm{absprec}`.

        INPUT:

        - ``absprec`` -- integer (default: 1)

        - ``field`` -- boolean (default: ``None``); whether to return an
          element of GF(p) or Zmod(p)

        - ``check_prec`` -- boolean (default: ``False``); no effect (for
          compatibility with other types)

        OUTPUT:

        This element reduced modulo `p^\\mathrm{absprec}` as an element of
        `\\ZZ/p^\\mathrm{absprec}\\ZZ`.

        EXAMPLES::

            sage: R = Zp(7,4,'fixed-mod')
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
            1 + 7
            sage: c.parent()
            7-adic Ring of fixed modulus 7^4

        TESTS::

            sage: R = Zp(7,4,'fixed-mod')
            sage: a = R(8)
            sage: a.residue(0)
            0
            sage: a.residue(-1)
            Traceback (most recent call last):
            ...
            ValueError: cannot reduce modulo a negative power of p
            sage: a.residue(5)
            8

            sage: a.residue(field=True).parent()
            Finite Field of size 7

        .. SEEALSO::

            :meth:`_mod_`"""
    def __pari__(self) -> Any:
        """pAdicFixedModElement.__pari__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_fixed_mod_element.pyx (starting at line 179)

        Conversion to PARI.

        EXAMPLES::

            sage: R = ZpCA(5)
            sage: pari(R(1777))  # indirect doctest                                     # needs sage.libs.pari
            2 + 5^2 + 4*5^3 + 2*5^4 + O(5^20)"""

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
