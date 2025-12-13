import _cython_3_2_1
import sage.misc.persist as persist
import sage.rings.padics.padic_generic_element
from sage.categories.category import ZZ as ZZ
from sage.misc.prandom import randint as randint
from sage.rings.finite_rings.finite_field_constructor import GF as GF
from sage.rings.infinity import Infinity as Infinity
from sage.rings.padics.padic_relaxed_errors import raise_error as raise_error
from sage.rings.padics.precision_error import PrecisionError as PrecisionError
from sage.structure.element import coerce_binop as coerce_binop, have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

__pyx_capi__: dict
unpickle_unknown: _cython_3_2_1.cython_function_or_method

class ExpansionIter:
    """ExpansionIter(RelaxedElement elt, expansion_mode mode, long start, long stop)

    File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 4020)

    An iterator over a `p`-adic expansion.

    This class should not be instantiated directly, but instead using
    :meth:`RelaxedElement.expansion`."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, RelaxedElementelt, expansion_modemode, longstart, longstop) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 4039)

                Initialize this iterator.

                INPUT:

                - ``elt`` -- a relaxed `p`-adic number

                - ``mode`` -- either ``simple_mode``, ``smallest_mode`` or ``teichmuller_mode``

                - ``start`` -- integer; the position where the expansion starts

                - ``stop`` -- integer; the position where the expansion stops

                TESTS::

                    sage: E = ZpER(5,4)(373).expansion()
                    sage: I = iter(E)   # indirect doctest
                    sage: type(I)
                    <class 'sage.rings.padics.padic_relaxed_element.ExpansionIter'>
        """
    def __iter__(self) -> Any:
        """ExpansionIter.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 4130)

        Return itself (as any iterator is supposed to do).

        TESTS::

            sage: E = ZpER(5)(373).expansion()
            sage: I = iter(E)
            sage: I is iter(I)
            True"""
    def __len__(self) -> Any:
        """ExpansionIter.__len__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 4102)

        Return the length of this expansion.

        EXAMPLES::

            sage: R = ZpER(7)
            sage: x = R(1/2021, 5)
            sage: x
            3 + 6*7 + 4*7^2 + 3*7^3 + 6*7^4 + O(7^5)
            sage: E = x.expansion()
            sage: len(E)
            5

        For unbounded elements, the expansion is infinite and this method
        raises an error::

            sage: y = R(1/2021)
            sage: E = y.expansion()
            sage: len(E)
            Traceback (most recent call last):
            ...
            NotImplementedError: infinite sequence"""
    def __next__(self) -> Any:
        """ExpansionIter.__next__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 4187)

        Return the next digit of this expansion.

        EXAMPLES::

            sage: R = ZpER(11, 10)
            sage: x = R(20/21); x
            2 + 2*11 + 4*11^2 + 8*11^3 + 5*11^4 + 11^6 + 2*11^7 + 4*11^8 + 8*11^9 + ...
            sage: E = x.expansion()
            sage: next(E)
            2
            sage: next(E)
            2

        TESTS::

            sage: def check_expansion(x, mode):
            ....:     R = x.parent()
            ....:     E = x.expansion(lift_mode=mode)
            ....:     y = 0
            ....:     for i in range(len(E)):
            ....:         digit = next(E)
            ....:         if mode == 'teichmuller':
            ....:             y += R.teichmuller(digit) << i
            ....:         else:
            ....:             y += R(digit) << i
            ....:     assert(x == y)

            sage: for p in primes(100):
            ....:     x = ZpER(p).random_element()[:20]
            ....:     for mode in [ 'simple', 'smallest', 'teichmuller' ]:
            ....:         check_expansion(x, mode)"""

class RelaxedElement(sage.rings.padics.padic_generic_element.pAdicGenericElement):
    """RelaxedElement(parent)

    File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 66)

    Template class for relaxed `p`-adic elements.

    EXAMPLES:

        sage: from sage.rings.padics.padic_relaxed_element import RelaxedElement
        sage: R = ZpER(5)
        sage: a = R(1)
        sage: isinstance(a, RelaxedElement)
        True"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 78)

                Initialize this element.

                TESTS::

                    sage: R = ZpER(5)
                    sage: a = R(1/2)  # indirect doctest
                    sage: TestSuite(a).run()
        """
    def add_bigoh(self, absprec) -> Any:
        """RelaxedElement.add_bigoh(self, absprec)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 1112)

        Return a new element with absolute precision decreased to ``absprec``.

        INPUT:

        - ``absprec`` -- integer or infinity

        EXAMPLES::

            sage: R = ZpER(7, prec=10)
            sage: a = R(1/2021); a
            3 + 6*7 + 4*7^2 + 3*7^3 + 6*7^4 + 7^5 + 6*7^6 + 3*7^7 + 6*7^8 + 5*7^9 + ...
            sage: a.add_bigoh(5)
            3 + 6*7 + 4*7^2 + 3*7^3 + 6*7^4 + O(7^5)

        When ``absprec`` is negative, we return an element in the fraction
        field::

            sage: b = a.add_bigoh(-1)
            sage: b
            O(7^-1)
            sage: b.parent()
            7-adic Field handled with relaxed arithmetics

        .. SEEALSO::

            :meth:`at_precision_absolute`, :meth:`at_precision_relative`"""
    def at_precision_absolute(self, prec=..., permissive=...) -> Any:
        """RelaxedElement.at_precision_absolute(self, prec=None, permissive=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 1043)

        Return this element bounded at the given precision.

        INPUT:

        - ``prec`` -- integer or ``None`` (default: ``None``);
          if ``None``, use the default precision of the parent

        - ``permissive`` -- boolean (default: ``False`` if ``prec``
          is given, ``True`` otherwise); if ``False``, raise an error
          if the precision of this element is not sufficient

        EXAMPLES::

            sage: R = ZpER(7, prec=10)
            sage: a = R(1/2021); a
            3 + 6*7 + 4*7^2 + 3*7^3 + 6*7^4 + 7^5 + 6*7^6 + 3*7^7 + 6*7^8 + 5*7^9 + ...
            sage: a.at_precision_absolute(5)
            3 + 6*7 + 4*7^2 + 3*7^3 + 6*7^4 + O(7^5)
            sage: a.at_precision_absolute(10)
            3 + 6*7 + 4*7^2 + 3*7^3 + 6*7^4 + 7^5 + 6*7^6 + 3*7^7 + 6*7^8 + 5*7^9 + O(7^10)

            sage: b = a.add_bigoh(5)
            sage: b.at_precision_absolute(10)
            Traceback (most recent call last):
            ...
            PrecisionError: not enough precision

            sage: b.at_precision_absolute(10, permissive=True)
            3 + 6*7 + 4*7^2 + 3*7^3 + 6*7^4 + O(7^5)

        Bounding at a negative precision is not permitted over `\\ZZ_p`::

            sage: a.at_precision_absolute(-1)
            Traceback (most recent call last):
            ...
            ValueError: precision must be nonnegative

        but, of course, it is over `\\QQ_p`::

            sage: K = R.fraction_field()
            sage: K(a).at_precision_absolute(-1)
            O(7^-1)

        .. SEEALSO::

            :meth:`at_precision_relative`, :meth:`add_bigoh`"""
    def at_precision_relative(self, prec=..., halt=..., permissive=...) -> Any:
        """RelaxedElement.at_precision_relative(self, prec=None, halt=True, permissive=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 1145)

        Return this element bounded at the given precision.

        INPUT:

        - ``prec`` -- integer or ``None`` (default: ``None``);
          if ``None``, use the default precision of the parent

        - ``halt`` -- integer or boolean (default: ``True``);
          the absolute precision after which the computation is abandoned
          if the first significant digit has not been found yet.
          If ``True``, the default halting precision of the parent is used.
          If ``False``, the computation is never abandoned.

        - ``permissive`` -- boolean (default: ``False`` if ``prec``
          is given, ``True`` otherwise); if ``False``, raise an error
          if the precision of this element is not sufficient

        EXAMPLES::

            sage: R = ZpER(5, prec=10, halt=10)
            sage: a = R(20/21); a
            4*5 + 4*5^2 + 5^4 + 4*5^6 + 3*5^7 + 4*5^8 + ...
            sage: a.at_precision_relative(5)
            4*5 + 4*5^2 + 5^4 + O(5^6)

        We illustrate the behaviour of the parameter ``halt``.
        We create a very small number whose first significant is far beyond
        the default precision::

            sage: b = R(5^20)
            sage: b
            0 + ...

        Without any help, Sage does not run the computation far enough to determine
        the valuation and an error is raised::

            sage: b.at_precision_relative(5)
            Traceback (most recent call last):
            ...
            PrecisionError: computation has been abandoned; try to increase precision

        By setting the argument ``halt``, one can force the computation to continue
        until a prescribed limit::

            sage: b.at_precision_relative(5, halt=20)   # not enough to find the valuation
            Traceback (most recent call last):
            ...
            PrecisionError: computation has been abandoned; try to increase precision

            sage: b.at_precision_relative(5, halt=21)   # now, we're okay
            5^20 + O(5^25)

        .. NOTE::

            It is also possible to pass in ``halt=False`` but it is not recommended
            because the computation can hang forever if this element is `0`.

        .. SEEALSO::

            :meth:`at_precision_absolute`, :meth:`add_bigoh`

        TESTS::

            sage: a.at_precision_relative(-1)
            Traceback (most recent call last):
            ...
            ValueError: precision must be nonnegative"""
    def digit(self, i) -> Any:
        """RelaxedElement.digit(self, i)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 267)

        Return the coefficient of `p^i` in the `p`-adic expansion
        of this number.

        INPUT:

        - ``i`` -- integer

        EXAMPLES::

            sage: R = ZpER(5, prec=10)
            sage: a = R(20/21)
            sage: a
            4*5 + 4*5^2 + 5^4 + 4*5^6 + 3*5^7 + 4*5^8 + ...
            sage: a.digit(0)
            0
            sage: a.digit(1)
            4
            sage: a.digit(7)
            3
            sage: a.digit(100)
            1

        As a shortcut, one can use the bracket operator::

            sage: a[100]
            1

        If the digit is not known, an error is raised::

            sage: b = a.add_bigoh(10)
            sage: b.digit(20)
            Traceback (most recent call last):
            ...
            PrecisionError: not enough precision

        TESTS::

            sage: a.digit(-1)
            0"""
    def expansion(self, n=..., lift_mode=..., start_val=...) -> Any:
        """RelaxedElement.expansion(self, n=None, lift_mode='simple', start_val=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 314)

        Return an iterator over the list of coefficients in a `p`-adic
        expansion of this element, that is the list of `a_i` so that
        this element can be expressed as

        .. MATH::

            \\pi^v \\cdot \\sum_{i=0}^\\infty a_i \\pi^i

        where `v` is the valuation of this element when the parent is
        a field, and `v = 0` otherwise and the `a_i` are between `0`
        and `p - 1`.

        INPUT:

        - ``n`` -- integer or ``None`` (default: ``None``); if
          given, return the corresponding entries in the expansion

        - ``lift_mode`` -- ``'simple'``, ``'smallest'`` or
          ``'teichmuller'`` (default: ``'simple'``)

        - ``start_val`` -- start at this valuation rather than the
          default (`0` or the valuation of this element)

        OUTPUT:

        - If ``n`` is ``None``, an iterable giving the `p`-adic expansion
          of this element.

        - If ``n`` is an integer, the coefficient of `p^n` in the
          `p`-adic expansion of this element.

        EXAMPLES::

            sage: R = ZpER(7, print_mode='digits')
            sage: a = R(1/2021); a
            ...23615224635636163463

        Without any argument, this method returns an iterator over the
        digits of this number::

            sage: E = a.expansion()
            sage: E
            7-adic expansion of ...23615224635636163463
            sage: next(E)
            3
            sage: next(E)
            6
            sage: next(E)
            4

        On the contrary, passing in an integer returns the digit at the
        given position::

            sage: a.expansion(5)
            1

        Over a field, the expansion starts at the valuation of the element::

            sage: K = R.fraction_field()
            sage: b = K(20/21); b
            ...2222222222222222223.2
            sage: E = b.expansion()
            sage: next(E)
            2
            sage: next(E)
            3

            sage: c = 1/b; c
            ...564356435643564356440
            sage: E = c.expansion()
            sage: next(E)
            4
            sage: next(E)
            4

        When ``start_val`` is given, the expansion starts at this position
        instead:

            sage: E = c.expansion(start_val=0)
            sage: next(E)
            0
            sage: next(E)
            4

            sage: E = c.expansion(start_val=5)
            sage: next(E)
            3
            sage: next(E)
            4"""
    @overload
    def inverse_of_unit(self) -> Any:
        """RelaxedElement.inverse_of_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 1862)

        Return the multiplicative inverse of this element if
        it is a unit.

        EXAMPLES::

            sage: R = ZpER(3, 5)
            sage: a = R(2)
            sage: b = a.inverse_of_unit()
            sage: b
            2 + 3 + 3^2 + 3^3 + 3^4 + ...

        A :exc:`ZeroDivisionError` is raised if an element has no inverse in the
        ring::

            sage: R(3).inverse_of_unit()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: denominator is not invertible

        Unlike the usual inverse of an element, the result is in the same ring
        as this element and not in its fraction field (for fields this does of
        course not make any difference)::

            sage: c = ~a; c
            2 + 3 + 3^2 + 3^3 + 3^4 + ...
            sage: a.parent()
            3-adic Ring handled with relaxed arithmetics
            sage: b.parent()
            3-adic Ring handled with relaxed arithmetics
            sage: c.parent()
            3-adic Field handled with relaxed arithmetics

        This method also works for self-referent numbers
        (see :meth:`sage.rings.padics.generic_nodes.pAdicRelaxedGeneric.unknown`)::

            sage: x = R.unknown(); x
            O(3^0)
            sage: x.inverse_of_unit()
            O(3^0)
            sage: x.set(1 + 3 * x.inverse_of_unit())
            True
            sage: x
            1 + 3 + 2*3^2 + 3^3 + 3^4 + ...

        Actually, in many cases, it is preferable to use it than an actual
        division. Indeed, compare::

            sage: y = R.unknown()
            sage: y.set(1 + 3/y)
            Traceback (most recent call last):
            ...
            RecursionError: definition looks circular"""
    @overload
    def inverse_of_unit(self) -> Any:
        """RelaxedElement.inverse_of_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 1862)

        Return the multiplicative inverse of this element if
        it is a unit.

        EXAMPLES::

            sage: R = ZpER(3, 5)
            sage: a = R(2)
            sage: b = a.inverse_of_unit()
            sage: b
            2 + 3 + 3^2 + 3^3 + 3^4 + ...

        A :exc:`ZeroDivisionError` is raised if an element has no inverse in the
        ring::

            sage: R(3).inverse_of_unit()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: denominator is not invertible

        Unlike the usual inverse of an element, the result is in the same ring
        as this element and not in its fraction field (for fields this does of
        course not make any difference)::

            sage: c = ~a; c
            2 + 3 + 3^2 + 3^3 + 3^4 + ...
            sage: a.parent()
            3-adic Ring handled with relaxed arithmetics
            sage: b.parent()
            3-adic Ring handled with relaxed arithmetics
            sage: c.parent()
            3-adic Field handled with relaxed arithmetics

        This method also works for self-referent numbers
        (see :meth:`sage.rings.padics.generic_nodes.pAdicRelaxedGeneric.unknown`)::

            sage: x = R.unknown(); x
            O(3^0)
            sage: x.inverse_of_unit()
            O(3^0)
            sage: x.set(1 + 3 * x.inverse_of_unit())
            True
            sage: x
            1 + 3 + 2*3^2 + 3^3 + 3^4 + ...

        Actually, in many cases, it is preferable to use it than an actual
        division. Indeed, compare::

            sage: y = R.unknown()
            sage: y.set(1 + 3/y)
            Traceback (most recent call last):
            ...
            RecursionError: definition looks circular"""
    @overload
    def inverse_of_unit(self) -> Any:
        """RelaxedElement.inverse_of_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 1862)

        Return the multiplicative inverse of this element if
        it is a unit.

        EXAMPLES::

            sage: R = ZpER(3, 5)
            sage: a = R(2)
            sage: b = a.inverse_of_unit()
            sage: b
            2 + 3 + 3^2 + 3^3 + 3^4 + ...

        A :exc:`ZeroDivisionError` is raised if an element has no inverse in the
        ring::

            sage: R(3).inverse_of_unit()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: denominator is not invertible

        Unlike the usual inverse of an element, the result is in the same ring
        as this element and not in its fraction field (for fields this does of
        course not make any difference)::

            sage: c = ~a; c
            2 + 3 + 3^2 + 3^3 + 3^4 + ...
            sage: a.parent()
            3-adic Ring handled with relaxed arithmetics
            sage: b.parent()
            3-adic Ring handled with relaxed arithmetics
            sage: c.parent()
            3-adic Field handled with relaxed arithmetics

        This method also works for self-referent numbers
        (see :meth:`sage.rings.padics.generic_nodes.pAdicRelaxedGeneric.unknown`)::

            sage: x = R.unknown(); x
            O(3^0)
            sage: x.inverse_of_unit()
            O(3^0)
            sage: x.set(1 + 3 * x.inverse_of_unit())
            True
            sage: x
            1 + 3 + 2*3^2 + 3^3 + 3^4 + ...

        Actually, in many cases, it is preferable to use it than an actual
        division. Indeed, compare::

            sage: y = R.unknown()
            sage: y.set(1 + 3/y)
            Traceback (most recent call last):
            ...
            RecursionError: definition looks circular"""
    @overload
    def inverse_of_unit(self) -> Any:
        """RelaxedElement.inverse_of_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 1862)

        Return the multiplicative inverse of this element if
        it is a unit.

        EXAMPLES::

            sage: R = ZpER(3, 5)
            sage: a = R(2)
            sage: b = a.inverse_of_unit()
            sage: b
            2 + 3 + 3^2 + 3^3 + 3^4 + ...

        A :exc:`ZeroDivisionError` is raised if an element has no inverse in the
        ring::

            sage: R(3).inverse_of_unit()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: denominator is not invertible

        Unlike the usual inverse of an element, the result is in the same ring
        as this element and not in its fraction field (for fields this does of
        course not make any difference)::

            sage: c = ~a; c
            2 + 3 + 3^2 + 3^3 + 3^4 + ...
            sage: a.parent()
            3-adic Ring handled with relaxed arithmetics
            sage: b.parent()
            3-adic Ring handled with relaxed arithmetics
            sage: c.parent()
            3-adic Field handled with relaxed arithmetics

        This method also works for self-referent numbers
        (see :meth:`sage.rings.padics.generic_nodes.pAdicRelaxedGeneric.unknown`)::

            sage: x = R.unknown(); x
            O(3^0)
            sage: x.inverse_of_unit()
            O(3^0)
            sage: x.set(1 + 3 * x.inverse_of_unit())
            True
            sage: x
            1 + 3 + 2*3^2 + 3^3 + 3^4 + ...

        Actually, in many cases, it is preferable to use it than an actual
        division. Indeed, compare::

            sage: y = R.unknown()
            sage: y.set(1 + 3/y)
            Traceback (most recent call last):
            ...
            RecursionError: definition looks circular"""
    @overload
    def inverse_of_unit(self) -> Any:
        """RelaxedElement.inverse_of_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 1862)

        Return the multiplicative inverse of this element if
        it is a unit.

        EXAMPLES::

            sage: R = ZpER(3, 5)
            sage: a = R(2)
            sage: b = a.inverse_of_unit()
            sage: b
            2 + 3 + 3^2 + 3^3 + 3^4 + ...

        A :exc:`ZeroDivisionError` is raised if an element has no inverse in the
        ring::

            sage: R(3).inverse_of_unit()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: denominator is not invertible

        Unlike the usual inverse of an element, the result is in the same ring
        as this element and not in its fraction field (for fields this does of
        course not make any difference)::

            sage: c = ~a; c
            2 + 3 + 3^2 + 3^3 + 3^4 + ...
            sage: a.parent()
            3-adic Ring handled with relaxed arithmetics
            sage: b.parent()
            3-adic Ring handled with relaxed arithmetics
            sage: c.parent()
            3-adic Field handled with relaxed arithmetics

        This method also works for self-referent numbers
        (see :meth:`sage.rings.padics.generic_nodes.pAdicRelaxedGeneric.unknown`)::

            sage: x = R.unknown(); x
            O(3^0)
            sage: x.inverse_of_unit()
            O(3^0)
            sage: x.set(1 + 3 * x.inverse_of_unit())
            True
            sage: x
            1 + 3 + 2*3^2 + 3^3 + 3^4 + ...

        Actually, in many cases, it is preferable to use it than an actual
        division. Indeed, compare::

            sage: y = R.unknown()
            sage: y.set(1 + 3/y)
            Traceback (most recent call last):
            ...
            RecursionError: definition looks circular"""
    def is_equal_at_precision(self, right, prec) -> Any:
        """RelaxedElement.is_equal_at_precision(self, right, prec)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 657)

        Compare this element with ``right`` at precision ``prec``.

        INPUT:

        - ``right`` -- a relaxed `p`-adic number

        - ``prec`` -- integer

        EXAMPLES::

            sage: R = ZpER(7, prec=10)
            sage: a = R(1/2); a
            4 + 3*7 + 3*7^2 + 3*7^3 + 3*7^4 + 3*7^5 + 3*7^6 + 3*7^7 + 3*7^8 + 3*7^9 + ...
            sage: b = R(99/2); b
            4 + 3*7 + 4*7^2 + 3*7^3 + 3*7^4 + 3*7^5 + 3*7^6 + 3*7^7 + 3*7^8 + 3*7^9 + ...

            sage: a.is_equal_at_precision(b, 1)
            True
            sage: a.is_equal_at_precision(b, 2)
            True
            sage: a.is_equal_at_precision(b, 3)
            False"""
    @overload
    def is_equal_to(self, RelaxedElementright, prec=..., secure=...) -> Any:
        """RelaxedElement.is_equal_to(self, RelaxedElement right, prec=None, secure=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 685)

        Compare this element with ``right``.

        INPUT:

        - ``right`` -- a relaxed `p`-adic number

        - ``prec`` -- integer or ``None`` (default: ``None``); if
          given, compare the two elements at this precision. Otherwise
          use the default halting precision of the parent.

        - ``secure`` -- boolean (default: ``False`` if ``prec`` is given,
          ``True`` otherwise); when the elements cannot be distinguished
          at the given precision, raise an error if ``secure`` is ``True``,
          return ``True`` otherwise.

        EXAMPLES::

            sage: R = ZpER(7)
            sage: a = R(1/2)
            sage: b = R(1/3)
            sage: c = R(1/6)

            sage: a.is_equal_to(b)
            False

        When equality indeed holds, it is not possible to conclude by
        comparing more and more accurate approximations.
        In this case, an error is raised::

            sage: a.is_equal_to(b + c)
            Traceback (most recent call last):
            ...
            PrecisionError: unable to decide equality; try to bound precision

        You can get around this behaviour by passing ``secure=False``::

            sage: a.is_equal_to(b + c, secure=False)
            True

        Another option (which is actually recommended) is to provide an explicit
        bound on the precision::

            sage: s = b + c + 7^50
            sage: a.is_equal_to(s, prec=20)
            True
            sage: a.is_equal_to(s, prec=100)
            False"""
    @overload
    def is_equal_to(self, b) -> Any:
        """RelaxedElement.is_equal_to(self, RelaxedElement right, prec=None, secure=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 685)

        Compare this element with ``right``.

        INPUT:

        - ``right`` -- a relaxed `p`-adic number

        - ``prec`` -- integer or ``None`` (default: ``None``); if
          given, compare the two elements at this precision. Otherwise
          use the default halting precision of the parent.

        - ``secure`` -- boolean (default: ``False`` if ``prec`` is given,
          ``True`` otherwise); when the elements cannot be distinguished
          at the given precision, raise an error if ``secure`` is ``True``,
          return ``True`` otherwise.

        EXAMPLES::

            sage: R = ZpER(7)
            sage: a = R(1/2)
            sage: b = R(1/3)
            sage: c = R(1/6)

            sage: a.is_equal_to(b)
            False

        When equality indeed holds, it is not possible to conclude by
        comparing more and more accurate approximations.
        In this case, an error is raised::

            sage: a.is_equal_to(b + c)
            Traceback (most recent call last):
            ...
            PrecisionError: unable to decide equality; try to bound precision

        You can get around this behaviour by passing ``secure=False``::

            sage: a.is_equal_to(b + c, secure=False)
            True

        Another option (which is actually recommended) is to provide an explicit
        bound on the precision::

            sage: s = b + c + 7^50
            sage: a.is_equal_to(s, prec=20)
            True
            sage: a.is_equal_to(s, prec=100)
            False"""
    @overload
    def is_equal_to(self, s, prec=...) -> Any:
        """RelaxedElement.is_equal_to(self, RelaxedElement right, prec=None, secure=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 685)

        Compare this element with ``right``.

        INPUT:

        - ``right`` -- a relaxed `p`-adic number

        - ``prec`` -- integer or ``None`` (default: ``None``); if
          given, compare the two elements at this precision. Otherwise
          use the default halting precision of the parent.

        - ``secure`` -- boolean (default: ``False`` if ``prec`` is given,
          ``True`` otherwise); when the elements cannot be distinguished
          at the given precision, raise an error if ``secure`` is ``True``,
          return ``True`` otherwise.

        EXAMPLES::

            sage: R = ZpER(7)
            sage: a = R(1/2)
            sage: b = R(1/3)
            sage: c = R(1/6)

            sage: a.is_equal_to(b)
            False

        When equality indeed holds, it is not possible to conclude by
        comparing more and more accurate approximations.
        In this case, an error is raised::

            sage: a.is_equal_to(b + c)
            Traceback (most recent call last):
            ...
            PrecisionError: unable to decide equality; try to bound precision

        You can get around this behaviour by passing ``secure=False``::

            sage: a.is_equal_to(b + c, secure=False)
            True

        Another option (which is actually recommended) is to provide an explicit
        bound on the precision::

            sage: s = b + c + 7^50
            sage: a.is_equal_to(s, prec=20)
            True
            sage: a.is_equal_to(s, prec=100)
            False"""
    @overload
    def is_equal_to(self, s, prec=...) -> Any:
        """RelaxedElement.is_equal_to(self, RelaxedElement right, prec=None, secure=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 685)

        Compare this element with ``right``.

        INPUT:

        - ``right`` -- a relaxed `p`-adic number

        - ``prec`` -- integer or ``None`` (default: ``None``); if
          given, compare the two elements at this precision. Otherwise
          use the default halting precision of the parent.

        - ``secure`` -- boolean (default: ``False`` if ``prec`` is given,
          ``True`` otherwise); when the elements cannot be distinguished
          at the given precision, raise an error if ``secure`` is ``True``,
          return ``True`` otherwise.

        EXAMPLES::

            sage: R = ZpER(7)
            sage: a = R(1/2)
            sage: b = R(1/3)
            sage: c = R(1/6)

            sage: a.is_equal_to(b)
            False

        When equality indeed holds, it is not possible to conclude by
        comparing more and more accurate approximations.
        In this case, an error is raised::

            sage: a.is_equal_to(b + c)
            Traceback (most recent call last):
            ...
            PrecisionError: unable to decide equality; try to bound precision

        You can get around this behaviour by passing ``secure=False``::

            sage: a.is_equal_to(b + c, secure=False)
            True

        Another option (which is actually recommended) is to provide an explicit
        bound on the precision::

            sage: s = b + c + 7^50
            sage: a.is_equal_to(s, prec=20)
            True
            sage: a.is_equal_to(s, prec=100)
            False"""
    @overload
    def is_exact(self) -> Any:
        """RelaxedElement.is_exact(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 883)

        Return ``True`` if this element is exact, that is if its
        precision is unbounded.

        EXAMPLES::

            sage: R = ZpER(5, prec=10)
            sage: a = R(20/21)
            sage: a
            4*5 + 4*5^2 + 5^4 + 4*5^6 + 3*5^7 + 4*5^8 + ...
            sage: a.is_exact()
            True

            sage: b = a.add_bigoh(10)
            sage: b
            4*5 + 4*5^2 + 5^4 + 4*5^6 + 3*5^7 + 4*5^8 + O(5^10)
            sage: b.is_exact()
            False"""
    @overload
    def is_exact(self) -> Any:
        """RelaxedElement.is_exact(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 883)

        Return ``True`` if this element is exact, that is if its
        precision is unbounded.

        EXAMPLES::

            sage: R = ZpER(5, prec=10)
            sage: a = R(20/21)
            sage: a
            4*5 + 4*5^2 + 5^4 + 4*5^6 + 3*5^7 + 4*5^8 + ...
            sage: a.is_exact()
            True

            sage: b = a.add_bigoh(10)
            sage: b
            4*5 + 4*5^2 + 5^4 + 4*5^6 + 3*5^7 + 4*5^8 + O(5^10)
            sage: b.is_exact()
            False"""
    @overload
    def is_exact(self) -> Any:
        """RelaxedElement.is_exact(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 883)

        Return ``True`` if this element is exact, that is if its
        precision is unbounded.

        EXAMPLES::

            sage: R = ZpER(5, prec=10)
            sage: a = R(20/21)
            sage: a
            4*5 + 4*5^2 + 5^4 + 4*5^6 + 3*5^7 + 4*5^8 + ...
            sage: a.is_exact()
            True

            sage: b = a.add_bigoh(10)
            sage: b
            4*5 + 4*5^2 + 5^4 + 4*5^6 + 3*5^7 + 4*5^8 + O(5^10)
            sage: b.is_exact()
            False"""
    def lift(self, absprec=...) -> Any:
        """RelaxedElement.lift(self, absprec=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 1576)

        Return a rational number which is congruent to this element modulo
        `p^\\mathrm{prec}`.

        INPUT:

        - ``absprec`` -- integer or ``None`` (default: ``None``); if ``None``,
          the absolute precision of this element is used

        EXAMPLES::

            sage: R = ZpER(7, 10)
            sage: a = R(1/2021, 5); a
            3 + 6*7 + 4*7^2 + 3*7^3 + 6*7^4 + O(7^5)
            sage: a.lift()
            15676
            sage: a.lift(2)
            45

        Here is another example with an element of negative valuation::

            sage: K = R.fraction_field()
            sage: b = K(20/21, 5); b
            2*7^-1 + 3 + 2*7 + 2*7^2 + 2*7^3 + 2*7^4 + O(7^5)
            sage: b.lift()
            39223/7

        For unbounded elements, we must specify a precision::

            sage: c = R(1/2021)
            sage: c.lift()
            Traceback (most recent call last):
            ...
            ValueError: you must specify a precision for unbounded elements

            sage: c.lift(5)
            15676"""
    @overload
    def lift_to_precision(self, absprec=...) -> Any:
        """RelaxedElement.lift_to_precision(self, absprec=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 1242)

        Return another element of the same parent, lifting this element
        and having absolute precision at least ``absprec``.

        INPUT:

        - ``absprec`` -- integer or ``None`` (default: ``None``); the
          absolute precision of the result. If ``None``, the default
          precision of the parent is used.

        EXAMPLES::

            sage: R = ZpER(5, prec=10)
            sage: a = R(20/21, 5); a
            4*5 + 4*5^2 + 5^4 + O(5^5)

            sage: a.lift_to_precision(20)
            4*5 + 4*5^2 + 5^4 + O(5^20)

        When the precision is omitted, the default precision of the parent
        is used::

            sage: a.lift_to_precision()
            4*5 + 4*5^2 + 5^4 + O(5^10)

        When the parent is a field, the behaviour is slightly different since
        the default precision of the parent becomes the relative precision
        of the lifted element::

            sage: K = R.fraction_field()
            sage: K(a).lift_to_precision()
            4*5 + 4*5^2 + 5^4 + O(5^11)

        Note that the precision never decreases::

            sage: a.lift_to_precision(2)
            4*5 + 4*5^2 + 5^4 + O(5^5)

        In particular, unbounded element are not affected by this method::

            sage: b = R(20/21); b
            4*5 + 4*5^2 + 5^4 + 4*5^6 + 3*5^7 + 4*5^8 + ...
            sage: b.lift_to_precision()
            4*5 + 4*5^2 + 5^4 + 4*5^6 + 3*5^7 + 4*5^8 + ...
            sage: b.lift_to_precision(2)
            4*5 + 4*5^2 + 5^4 + 4*5^6 + 3*5^7 + 4*5^8 + ..."""
    @overload
    def lift_to_precision(self) -> Any:
        """RelaxedElement.lift_to_precision(self, absprec=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 1242)

        Return another element of the same parent, lifting this element
        and having absolute precision at least ``absprec``.

        INPUT:

        - ``absprec`` -- integer or ``None`` (default: ``None``); the
          absolute precision of the result. If ``None``, the default
          precision of the parent is used.

        EXAMPLES::

            sage: R = ZpER(5, prec=10)
            sage: a = R(20/21, 5); a
            4*5 + 4*5^2 + 5^4 + O(5^5)

            sage: a.lift_to_precision(20)
            4*5 + 4*5^2 + 5^4 + O(5^20)

        When the precision is omitted, the default precision of the parent
        is used::

            sage: a.lift_to_precision()
            4*5 + 4*5^2 + 5^4 + O(5^10)

        When the parent is a field, the behaviour is slightly different since
        the default precision of the parent becomes the relative precision
        of the lifted element::

            sage: K = R.fraction_field()
            sage: K(a).lift_to_precision()
            4*5 + 4*5^2 + 5^4 + O(5^11)

        Note that the precision never decreases::

            sage: a.lift_to_precision(2)
            4*5 + 4*5^2 + 5^4 + O(5^5)

        In particular, unbounded element are not affected by this method::

            sage: b = R(20/21); b
            4*5 + 4*5^2 + 5^4 + 4*5^6 + 3*5^7 + 4*5^8 + ...
            sage: b.lift_to_precision()
            4*5 + 4*5^2 + 5^4 + 4*5^6 + 3*5^7 + 4*5^8 + ...
            sage: b.lift_to_precision(2)
            4*5 + 4*5^2 + 5^4 + 4*5^6 + 3*5^7 + 4*5^8 + ..."""
    @overload
    def lift_to_precision(self) -> Any:
        """RelaxedElement.lift_to_precision(self, absprec=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 1242)

        Return another element of the same parent, lifting this element
        and having absolute precision at least ``absprec``.

        INPUT:

        - ``absprec`` -- integer or ``None`` (default: ``None``); the
          absolute precision of the result. If ``None``, the default
          precision of the parent is used.

        EXAMPLES::

            sage: R = ZpER(5, prec=10)
            sage: a = R(20/21, 5); a
            4*5 + 4*5^2 + 5^4 + O(5^5)

            sage: a.lift_to_precision(20)
            4*5 + 4*5^2 + 5^4 + O(5^20)

        When the precision is omitted, the default precision of the parent
        is used::

            sage: a.lift_to_precision()
            4*5 + 4*5^2 + 5^4 + O(5^10)

        When the parent is a field, the behaviour is slightly different since
        the default precision of the parent becomes the relative precision
        of the lifted element::

            sage: K = R.fraction_field()
            sage: K(a).lift_to_precision()
            4*5 + 4*5^2 + 5^4 + O(5^11)

        Note that the precision never decreases::

            sage: a.lift_to_precision(2)
            4*5 + 4*5^2 + 5^4 + O(5^5)

        In particular, unbounded element are not affected by this method::

            sage: b = R(20/21); b
            4*5 + 4*5^2 + 5^4 + 4*5^6 + 3*5^7 + 4*5^8 + ...
            sage: b.lift_to_precision()
            4*5 + 4*5^2 + 5^4 + 4*5^6 + 3*5^7 + 4*5^8 + ...
            sage: b.lift_to_precision(2)
            4*5 + 4*5^2 + 5^4 + 4*5^6 + 3*5^7 + 4*5^8 + ..."""
    @overload
    def lift_to_precision(self) -> Any:
        """RelaxedElement.lift_to_precision(self, absprec=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 1242)

        Return another element of the same parent, lifting this element
        and having absolute precision at least ``absprec``.

        INPUT:

        - ``absprec`` -- integer or ``None`` (default: ``None``); the
          absolute precision of the result. If ``None``, the default
          precision of the parent is used.

        EXAMPLES::

            sage: R = ZpER(5, prec=10)
            sage: a = R(20/21, 5); a
            4*5 + 4*5^2 + 5^4 + O(5^5)

            sage: a.lift_to_precision(20)
            4*5 + 4*5^2 + 5^4 + O(5^20)

        When the precision is omitted, the default precision of the parent
        is used::

            sage: a.lift_to_precision()
            4*5 + 4*5^2 + 5^4 + O(5^10)

        When the parent is a field, the behaviour is slightly different since
        the default precision of the parent becomes the relative precision
        of the lifted element::

            sage: K = R.fraction_field()
            sage: K(a).lift_to_precision()
            4*5 + 4*5^2 + 5^4 + O(5^11)

        Note that the precision never decreases::

            sage: a.lift_to_precision(2)
            4*5 + 4*5^2 + 5^4 + O(5^5)

        In particular, unbounded element are not affected by this method::

            sage: b = R(20/21); b
            4*5 + 4*5^2 + 5^4 + 4*5^6 + 3*5^7 + 4*5^8 + ...
            sage: b.lift_to_precision()
            4*5 + 4*5^2 + 5^4 + 4*5^6 + 3*5^7 + 4*5^8 + ...
            sage: b.lift_to_precision(2)
            4*5 + 4*5^2 + 5^4 + 4*5^6 + 3*5^7 + 4*5^8 + ..."""
    def precision_absolute(self) -> Any:
        """RelaxedElement.precision_absolute(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 905)

        Return the absolute precision of this element.

        This is the power of `p` modulo which this element is known.
        For unbounded elements, this methods return `+\\infty`.

        EXAMPLES::

            sage: R = ZpER(5, prec=10)
            sage: a = R(20/21)
            sage: a
            4*5 + 4*5^2 + 5^4 + 4*5^6 + 3*5^7 + 4*5^8 + ...
            sage: a.precision_absolute()
            +Infinity

            sage: b = a.add_bigoh(10)
            sage: b
            4*5 + 4*5^2 + 5^4 + 4*5^6 + 3*5^7 + 4*5^8 + O(5^10)
            sage: b.precision_absolute()
            10

        TESTS::

            sage: s = R.unknown()
            sage: (1/s).precision_absolute()
            Traceback (most recent call last):
            ...
            PrecisionError: no lower bound on the valuation is known"""
    @overload
    def precision_current(self) -> Any:
        """RelaxedElement.precision_current(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 993)

        Return the internal absolute precision at which this relaxed `p`-adic
        number is known at the current stage of the computation.

        EXAMPLES::

            sage: R = ZpER(5, prec=10)
            sage: x = R(20/21)
            sage: y = R(21/22)
            sage: z = x + y

        When the elements are just defined, the computation has not started::

            sage: x.precision_current()
            0
            sage: y.precision_current()
            0
            sage: z.precision_current()
            0

        When elements are printed, the relevant digits are computed::

            sage: x
            4*5 + 4*5^2 + 5^4 + 4*5^6 + 3*5^7 + 4*5^8 + ...
            sage: x.precision_current()
            10

        If we ask for more digits of `z`, the current precision of `z`
        increases accordingly::

            sage: z[:15]
            3 + 2*5 + 2*5^3 + 5^4 + 2*5^5 + 2*5^6 + 4*5^7 + 5^9 + 3*5^10 + 3*5^11 + 4*5^12 + 4*5^13 + 4*5^14 + O(5^15)
            sage: z.precision_current()
            15

        and similarly the current precision of `x` and `y` increases because
        those digits are needed to carry out the computation::

            sage: x.precision_current()
            15
            sage: y.precision_current()
            15"""
    @overload
    def precision_current(self) -> Any:
        """RelaxedElement.precision_current(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 993)

        Return the internal absolute precision at which this relaxed `p`-adic
        number is known at the current stage of the computation.

        EXAMPLES::

            sage: R = ZpER(5, prec=10)
            sage: x = R(20/21)
            sage: y = R(21/22)
            sage: z = x + y

        When the elements are just defined, the computation has not started::

            sage: x.precision_current()
            0
            sage: y.precision_current()
            0
            sage: z.precision_current()
            0

        When elements are printed, the relevant digits are computed::

            sage: x
            4*5 + 4*5^2 + 5^4 + 4*5^6 + 3*5^7 + 4*5^8 + ...
            sage: x.precision_current()
            10

        If we ask for more digits of `z`, the current precision of `z`
        increases accordingly::

            sage: z[:15]
            3 + 2*5 + 2*5^3 + 5^4 + 2*5^5 + 2*5^6 + 4*5^7 + 5^9 + 3*5^10 + 3*5^11 + 4*5^12 + 4*5^13 + 4*5^14 + O(5^15)
            sage: z.precision_current()
            15

        and similarly the current precision of `x` and `y` increases because
        those digits are needed to carry out the computation::

            sage: x.precision_current()
            15
            sage: y.precision_current()
            15"""
    @overload
    def precision_current(self) -> Any:
        """RelaxedElement.precision_current(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 993)

        Return the internal absolute precision at which this relaxed `p`-adic
        number is known at the current stage of the computation.

        EXAMPLES::

            sage: R = ZpER(5, prec=10)
            sage: x = R(20/21)
            sage: y = R(21/22)
            sage: z = x + y

        When the elements are just defined, the computation has not started::

            sage: x.precision_current()
            0
            sage: y.precision_current()
            0
            sage: z.precision_current()
            0

        When elements are printed, the relevant digits are computed::

            sage: x
            4*5 + 4*5^2 + 5^4 + 4*5^6 + 3*5^7 + 4*5^8 + ...
            sage: x.precision_current()
            10

        If we ask for more digits of `z`, the current precision of `z`
        increases accordingly::

            sage: z[:15]
            3 + 2*5 + 2*5^3 + 5^4 + 2*5^5 + 2*5^6 + 4*5^7 + 5^9 + 3*5^10 + 3*5^11 + 4*5^12 + 4*5^13 + 4*5^14 + O(5^15)
            sage: z.precision_current()
            15

        and similarly the current precision of `x` and `y` increases because
        those digits are needed to carry out the computation::

            sage: x.precision_current()
            15
            sage: y.precision_current()
            15"""
    @overload
    def precision_current(self) -> Any:
        """RelaxedElement.precision_current(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 993)

        Return the internal absolute precision at which this relaxed `p`-adic
        number is known at the current stage of the computation.

        EXAMPLES::

            sage: R = ZpER(5, prec=10)
            sage: x = R(20/21)
            sage: y = R(21/22)
            sage: z = x + y

        When the elements are just defined, the computation has not started::

            sage: x.precision_current()
            0
            sage: y.precision_current()
            0
            sage: z.precision_current()
            0

        When elements are printed, the relevant digits are computed::

            sage: x
            4*5 + 4*5^2 + 5^4 + 4*5^6 + 3*5^7 + 4*5^8 + ...
            sage: x.precision_current()
            10

        If we ask for more digits of `z`, the current precision of `z`
        increases accordingly::

            sage: z[:15]
            3 + 2*5 + 2*5^3 + 5^4 + 2*5^5 + 2*5^6 + 4*5^7 + 5^9 + 3*5^10 + 3*5^11 + 4*5^12 + 4*5^13 + 4*5^14 + O(5^15)
            sage: z.precision_current()
            15

        and similarly the current precision of `x` and `y` increases because
        those digits are needed to carry out the computation::

            sage: x.precision_current()
            15
            sage: y.precision_current()
            15"""
    @overload
    def precision_current(self) -> Any:
        """RelaxedElement.precision_current(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 993)

        Return the internal absolute precision at which this relaxed `p`-adic
        number is known at the current stage of the computation.

        EXAMPLES::

            sage: R = ZpER(5, prec=10)
            sage: x = R(20/21)
            sage: y = R(21/22)
            sage: z = x + y

        When the elements are just defined, the computation has not started::

            sage: x.precision_current()
            0
            sage: y.precision_current()
            0
            sage: z.precision_current()
            0

        When elements are printed, the relevant digits are computed::

            sage: x
            4*5 + 4*5^2 + 5^4 + 4*5^6 + 3*5^7 + 4*5^8 + ...
            sage: x.precision_current()
            10

        If we ask for more digits of `z`, the current precision of `z`
        increases accordingly::

            sage: z[:15]
            3 + 2*5 + 2*5^3 + 5^4 + 2*5^5 + 2*5^6 + 4*5^7 + 5^9 + 3*5^10 + 3*5^11 + 4*5^12 + 4*5^13 + 4*5^14 + O(5^15)
            sage: z.precision_current()
            15

        and similarly the current precision of `x` and `y` increases because
        those digits are needed to carry out the computation::

            sage: x.precision_current()
            15
            sage: y.precision_current()
            15"""
    @overload
    def precision_current(self) -> Any:
        """RelaxedElement.precision_current(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 993)

        Return the internal absolute precision at which this relaxed `p`-adic
        number is known at the current stage of the computation.

        EXAMPLES::

            sage: R = ZpER(5, prec=10)
            sage: x = R(20/21)
            sage: y = R(21/22)
            sage: z = x + y

        When the elements are just defined, the computation has not started::

            sage: x.precision_current()
            0
            sage: y.precision_current()
            0
            sage: z.precision_current()
            0

        When elements are printed, the relevant digits are computed::

            sage: x
            4*5 + 4*5^2 + 5^4 + 4*5^6 + 3*5^7 + 4*5^8 + ...
            sage: x.precision_current()
            10

        If we ask for more digits of `z`, the current precision of `z`
        increases accordingly::

            sage: z[:15]
            3 + 2*5 + 2*5^3 + 5^4 + 2*5^5 + 2*5^6 + 4*5^7 + 5^9 + 3*5^10 + 3*5^11 + 4*5^12 + 4*5^13 + 4*5^14 + O(5^15)
            sage: z.precision_current()
            15

        and similarly the current precision of `x` and `y` increases because
        those digits are needed to carry out the computation::

            sage: x.precision_current()
            15
            sage: y.precision_current()
            15"""
    @overload
    def precision_current(self) -> Any:
        """RelaxedElement.precision_current(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 993)

        Return the internal absolute precision at which this relaxed `p`-adic
        number is known at the current stage of the computation.

        EXAMPLES::

            sage: R = ZpER(5, prec=10)
            sage: x = R(20/21)
            sage: y = R(21/22)
            sage: z = x + y

        When the elements are just defined, the computation has not started::

            sage: x.precision_current()
            0
            sage: y.precision_current()
            0
            sage: z.precision_current()
            0

        When elements are printed, the relevant digits are computed::

            sage: x
            4*5 + 4*5^2 + 5^4 + 4*5^6 + 3*5^7 + 4*5^8 + ...
            sage: x.precision_current()
            10

        If we ask for more digits of `z`, the current precision of `z`
        increases accordingly::

            sage: z[:15]
            3 + 2*5 + 2*5^3 + 5^4 + 2*5^5 + 2*5^6 + 4*5^7 + 5^9 + 3*5^10 + 3*5^11 + 4*5^12 + 4*5^13 + 4*5^14 + O(5^15)
            sage: z.precision_current()
            15

        and similarly the current precision of `x` and `y` increases because
        those digits are needed to carry out the computation::

            sage: x.precision_current()
            15
            sage: y.precision_current()
            15"""
    @overload
    def precision_current(self) -> Any:
        """RelaxedElement.precision_current(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 993)

        Return the internal absolute precision at which this relaxed `p`-adic
        number is known at the current stage of the computation.

        EXAMPLES::

            sage: R = ZpER(5, prec=10)
            sage: x = R(20/21)
            sage: y = R(21/22)
            sage: z = x + y

        When the elements are just defined, the computation has not started::

            sage: x.precision_current()
            0
            sage: y.precision_current()
            0
            sage: z.precision_current()
            0

        When elements are printed, the relevant digits are computed::

            sage: x
            4*5 + 4*5^2 + 5^4 + 4*5^6 + 3*5^7 + 4*5^8 + ...
            sage: x.precision_current()
            10

        If we ask for more digits of `z`, the current precision of `z`
        increases accordingly::

            sage: z[:15]
            3 + 2*5 + 2*5^3 + 5^4 + 2*5^5 + 2*5^6 + 4*5^7 + 5^9 + 3*5^10 + 3*5^11 + 4*5^12 + 4*5^13 + 4*5^14 + O(5^15)
            sage: z.precision_current()
            15

        and similarly the current precision of `x` and `y` increases because
        those digits are needed to carry out the computation::

            sage: x.precision_current()
            15
            sage: y.precision_current()
            15"""
    def precision_relative(self) -> Any:
        """RelaxedElement.precision_relative(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 943)

        Return the relative precision of this element.

        This is the power of `p` modulo which the unit part of this
        element is known.

        For unbounded nonzero elements, this methods return `+\\infty`.

        EXAMPLES::

            sage: R = ZpER(5, prec=10)
            sage: a = R(20/21)
            sage: a
            4*5 + 4*5^2 + 5^4 + 4*5^6 + 3*5^7 + 4*5^8 + ...
            sage: a.precision_relative()
            +Infinity

            sage: b = a.add_bigoh(10)
            sage: b
            4*5 + 4*5^2 + 5^4 + 4*5^6 + 3*5^7 + 4*5^8 + O(5^10)
            sage: b.precision_relative()
            9

        The relative precision of (exact and inexact) `0` is `0`::

            sage: x = R(0); x
            0
            sage: x.precision_relative()
            0

            sage: y = R(0, 10); y
            O(5^10)
            sage: y.precision_relative()
            0

        TESTS::

            sage: s = R.unknown()
            sage: (1/s).precision_relative()
            Traceback (most recent call last):
            ...
            PrecisionError: no lower bound on the valuation is known"""
    def residue(self, absprec=..., field=..., check_prec=...) -> Any:
        """RelaxedElement.residue(self, absprec=1, field=True, check_prec=True)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 1522)

        Return the image of this element in the quotient
        `\\ZZ/p^\\mathrm{absprec}\\ZZ`.

        INPUT:

        - ``absprec`` -- nonnegative integer (default: 1)

        - ``field`` -- boolean (default: ``True``); when ``absprec`` is ``1``,
          whether to return an element of GF(p) or Zmod(p)

        - ``check_prec`` -- boolean (default: ``True``); whether to raise an error
          if this element has insufficient precision to determine the reduction

        EXAMPLES::

            sage: R = ZpER(7, 10)
            sage: a = R(1/2021); a
            3 + 6*7 + 4*7^2 + 3*7^3 + 6*7^4 + 7^5 + 6*7^6 + 3*7^7 + 6*7^8 + 5*7^9 + ...
            sage: a.residue()
            3
            sage: a.residue(2)
            45

        If this element has negative valuation, an error is raised::

            sage: K = R.fraction_field()
            sage: b = K(20/21)
            sage: b.residue()
            Traceback (most recent call last):
            ...
            ValueError: element must have nonnegative valuation in order to compute residue"""
    @overload
    def slice(self, start=..., stop=..., bound=...) -> Any:
        """RelaxedElement.slice(self, start=None, stop=None, bound=False)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 482)

        Return a slice of this number.

        INPUT:

        - ``start`` -- integer or ``None`` (default: ``None``);
          the first position of the slice

        - ``stop`` -- integer or ``None`` (default: ``None``);
          the first position not included in the slice

        - ``bound`` -- boolean (default: ``False``); whether the
          precision on the output should be bounded or unbounded

        EXAMPLES::

            sage: K = QpER(7, prec=10)
            sage: a = K(1/2021); a
            3 + 6*7 + 4*7^2 + 3*7^3 + 6*7^4 + 7^5 + 6*7^6 + 3*7^7 + 6*7^8 + 5*7^9 + ...

            sage: s = a.slice(3, 6)
            sage: s
            3*7^3 + 6*7^4 + 7^5 + ...

        In the above example, the precision on `b` remains unbounded::

            sage: s.precision_absolute()
            +Infinity

        Passing in ``bound=True`` changes this behaviour::

            sage: a.slice(3, 6, bound=True)
            3*7^3 + 6*7^4 + 7^5 + O(7^6)

        When ``start`` is omitted, the slice starts at the beginning of the number:

            sage: a.slice(stop=6)
            3 + 6*7 + 4*7^2 + 3*7^3 + 6*7^4 + 7^5 + ...

            sage: b = K(20/21); b
            2*7^-1 + 3 + 2*7 + 2*7^2 + 2*7^3 + 2*7^4 + 2*7^5 + 2*7^6 + 2*7^7 + 2*7^8 + ...
            sage: b.slice(stop=6)
            2*7^-1 + 3 + 2*7 + 2*7^2 + 2*7^3 + 2*7^4 + 2*7^5 + ...

        As a shortcut, one can use the bracket operator.
        However, in this case, the precision is bounded::

            sage: a[3:6]
            3*7^3 + 6*7^4 + 7^5 + O(7^6)
            sage: b[:6]
            2*7^-1 + 3 + 2*7 + 2*7^2 + 2*7^3 + 2*7^4 + 2*7^5 + O(7^6)

        TESTS::

            sage: x = a[:3]
            sage: x.slice(stop=3)
            3 + 6*7 + 4*7^2 + ...
            sage: x.slice(stop=4)
            3 + 6*7 + 4*7^2 + O(7^3)

        Taking slices of slices work as expected::

            sage: a1 = a.slice(5, 10); a1
            7^5 + 6*7^6 + 3*7^7 + 6*7^8 + 5*7^9 + ...
            sage: a2 = a1.slice(3, 8); a2
            7^5 + 6*7^6 + 3*7^7 + ...
            sage: a2 == a.slice(5, 8)
            True"""
    @overload
    def slice(self, stop=...) -> Any:
        """RelaxedElement.slice(self, start=None, stop=None, bound=False)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 482)

        Return a slice of this number.

        INPUT:

        - ``start`` -- integer or ``None`` (default: ``None``);
          the first position of the slice

        - ``stop`` -- integer or ``None`` (default: ``None``);
          the first position not included in the slice

        - ``bound`` -- boolean (default: ``False``); whether the
          precision on the output should be bounded or unbounded

        EXAMPLES::

            sage: K = QpER(7, prec=10)
            sage: a = K(1/2021); a
            3 + 6*7 + 4*7^2 + 3*7^3 + 6*7^4 + 7^5 + 6*7^6 + 3*7^7 + 6*7^8 + 5*7^9 + ...

            sage: s = a.slice(3, 6)
            sage: s
            3*7^3 + 6*7^4 + 7^5 + ...

        In the above example, the precision on `b` remains unbounded::

            sage: s.precision_absolute()
            +Infinity

        Passing in ``bound=True`` changes this behaviour::

            sage: a.slice(3, 6, bound=True)
            3*7^3 + 6*7^4 + 7^5 + O(7^6)

        When ``start`` is omitted, the slice starts at the beginning of the number:

            sage: a.slice(stop=6)
            3 + 6*7 + 4*7^2 + 3*7^3 + 6*7^4 + 7^5 + ...

            sage: b = K(20/21); b
            2*7^-1 + 3 + 2*7 + 2*7^2 + 2*7^3 + 2*7^4 + 2*7^5 + 2*7^6 + 2*7^7 + 2*7^8 + ...
            sage: b.slice(stop=6)
            2*7^-1 + 3 + 2*7 + 2*7^2 + 2*7^3 + 2*7^4 + 2*7^5 + ...

        As a shortcut, one can use the bracket operator.
        However, in this case, the precision is bounded::

            sage: a[3:6]
            3*7^3 + 6*7^4 + 7^5 + O(7^6)
            sage: b[:6]
            2*7^-1 + 3 + 2*7 + 2*7^2 + 2*7^3 + 2*7^4 + 2*7^5 + O(7^6)

        TESTS::

            sage: x = a[:3]
            sage: x.slice(stop=3)
            3 + 6*7 + 4*7^2 + ...
            sage: x.slice(stop=4)
            3 + 6*7 + 4*7^2 + O(7^3)

        Taking slices of slices work as expected::

            sage: a1 = a.slice(5, 10); a1
            7^5 + 6*7^6 + 3*7^7 + 6*7^8 + 5*7^9 + ...
            sage: a2 = a1.slice(3, 8); a2
            7^5 + 6*7^6 + 3*7^7 + ...
            sage: a2 == a.slice(5, 8)
            True"""
    @overload
    def slice(self, stop=...) -> Any:
        """RelaxedElement.slice(self, start=None, stop=None, bound=False)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 482)

        Return a slice of this number.

        INPUT:

        - ``start`` -- integer or ``None`` (default: ``None``);
          the first position of the slice

        - ``stop`` -- integer or ``None`` (default: ``None``);
          the first position not included in the slice

        - ``bound`` -- boolean (default: ``False``); whether the
          precision on the output should be bounded or unbounded

        EXAMPLES::

            sage: K = QpER(7, prec=10)
            sage: a = K(1/2021); a
            3 + 6*7 + 4*7^2 + 3*7^3 + 6*7^4 + 7^5 + 6*7^6 + 3*7^7 + 6*7^8 + 5*7^9 + ...

            sage: s = a.slice(3, 6)
            sage: s
            3*7^3 + 6*7^4 + 7^5 + ...

        In the above example, the precision on `b` remains unbounded::

            sage: s.precision_absolute()
            +Infinity

        Passing in ``bound=True`` changes this behaviour::

            sage: a.slice(3, 6, bound=True)
            3*7^3 + 6*7^4 + 7^5 + O(7^6)

        When ``start`` is omitted, the slice starts at the beginning of the number:

            sage: a.slice(stop=6)
            3 + 6*7 + 4*7^2 + 3*7^3 + 6*7^4 + 7^5 + ...

            sage: b = K(20/21); b
            2*7^-1 + 3 + 2*7 + 2*7^2 + 2*7^3 + 2*7^4 + 2*7^5 + 2*7^6 + 2*7^7 + 2*7^8 + ...
            sage: b.slice(stop=6)
            2*7^-1 + 3 + 2*7 + 2*7^2 + 2*7^3 + 2*7^4 + 2*7^5 + ...

        As a shortcut, one can use the bracket operator.
        However, in this case, the precision is bounded::

            sage: a[3:6]
            3*7^3 + 6*7^4 + 7^5 + O(7^6)
            sage: b[:6]
            2*7^-1 + 3 + 2*7 + 2*7^2 + 2*7^3 + 2*7^4 + 2*7^5 + O(7^6)

        TESTS::

            sage: x = a[:3]
            sage: x.slice(stop=3)
            3 + 6*7 + 4*7^2 + ...
            sage: x.slice(stop=4)
            3 + 6*7 + 4*7^2 + O(7^3)

        Taking slices of slices work as expected::

            sage: a1 = a.slice(5, 10); a1
            7^5 + 6*7^6 + 3*7^7 + 6*7^8 + 5*7^9 + ...
            sage: a2 = a1.slice(3, 8); a2
            7^5 + 6*7^6 + 3*7^7 + ...
            sage: a2 == a.slice(5, 8)
            True"""
    @overload
    def slice(self, stop=...) -> Any:
        """RelaxedElement.slice(self, start=None, stop=None, bound=False)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 482)

        Return a slice of this number.

        INPUT:

        - ``start`` -- integer or ``None`` (default: ``None``);
          the first position of the slice

        - ``stop`` -- integer or ``None`` (default: ``None``);
          the first position not included in the slice

        - ``bound`` -- boolean (default: ``False``); whether the
          precision on the output should be bounded or unbounded

        EXAMPLES::

            sage: K = QpER(7, prec=10)
            sage: a = K(1/2021); a
            3 + 6*7 + 4*7^2 + 3*7^3 + 6*7^4 + 7^5 + 6*7^6 + 3*7^7 + 6*7^8 + 5*7^9 + ...

            sage: s = a.slice(3, 6)
            sage: s
            3*7^3 + 6*7^4 + 7^5 + ...

        In the above example, the precision on `b` remains unbounded::

            sage: s.precision_absolute()
            +Infinity

        Passing in ``bound=True`` changes this behaviour::

            sage: a.slice(3, 6, bound=True)
            3*7^3 + 6*7^4 + 7^5 + O(7^6)

        When ``start`` is omitted, the slice starts at the beginning of the number:

            sage: a.slice(stop=6)
            3 + 6*7 + 4*7^2 + 3*7^3 + 6*7^4 + 7^5 + ...

            sage: b = K(20/21); b
            2*7^-1 + 3 + 2*7 + 2*7^2 + 2*7^3 + 2*7^4 + 2*7^5 + 2*7^6 + 2*7^7 + 2*7^8 + ...
            sage: b.slice(stop=6)
            2*7^-1 + 3 + 2*7 + 2*7^2 + 2*7^3 + 2*7^4 + 2*7^5 + ...

        As a shortcut, one can use the bracket operator.
        However, in this case, the precision is bounded::

            sage: a[3:6]
            3*7^3 + 6*7^4 + 7^5 + O(7^6)
            sage: b[:6]
            2*7^-1 + 3 + 2*7 + 2*7^2 + 2*7^3 + 2*7^4 + 2*7^5 + O(7^6)

        TESTS::

            sage: x = a[:3]
            sage: x.slice(stop=3)
            3 + 6*7 + 4*7^2 + ...
            sage: x.slice(stop=4)
            3 + 6*7 + 4*7^2 + O(7^3)

        Taking slices of slices work as expected::

            sage: a1 = a.slice(5, 10); a1
            7^5 + 6*7^6 + 3*7^7 + 6*7^8 + 5*7^9 + ...
            sage: a2 = a1.slice(3, 8); a2
            7^5 + 6*7^6 + 3*7^7 + ...
            sage: a2 == a.slice(5, 8)
            True"""
    @overload
    def slice(self, stop=...) -> Any:
        """RelaxedElement.slice(self, start=None, stop=None, bound=False)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 482)

        Return a slice of this number.

        INPUT:

        - ``start`` -- integer or ``None`` (default: ``None``);
          the first position of the slice

        - ``stop`` -- integer or ``None`` (default: ``None``);
          the first position not included in the slice

        - ``bound`` -- boolean (default: ``False``); whether the
          precision on the output should be bounded or unbounded

        EXAMPLES::

            sage: K = QpER(7, prec=10)
            sage: a = K(1/2021); a
            3 + 6*7 + 4*7^2 + 3*7^3 + 6*7^4 + 7^5 + 6*7^6 + 3*7^7 + 6*7^8 + 5*7^9 + ...

            sage: s = a.slice(3, 6)
            sage: s
            3*7^3 + 6*7^4 + 7^5 + ...

        In the above example, the precision on `b` remains unbounded::

            sage: s.precision_absolute()
            +Infinity

        Passing in ``bound=True`` changes this behaviour::

            sage: a.slice(3, 6, bound=True)
            3*7^3 + 6*7^4 + 7^5 + O(7^6)

        When ``start`` is omitted, the slice starts at the beginning of the number:

            sage: a.slice(stop=6)
            3 + 6*7 + 4*7^2 + 3*7^3 + 6*7^4 + 7^5 + ...

            sage: b = K(20/21); b
            2*7^-1 + 3 + 2*7 + 2*7^2 + 2*7^3 + 2*7^4 + 2*7^5 + 2*7^6 + 2*7^7 + 2*7^8 + ...
            sage: b.slice(stop=6)
            2*7^-1 + 3 + 2*7 + 2*7^2 + 2*7^3 + 2*7^4 + 2*7^5 + ...

        As a shortcut, one can use the bracket operator.
        However, in this case, the precision is bounded::

            sage: a[3:6]
            3*7^3 + 6*7^4 + 7^5 + O(7^6)
            sage: b[:6]
            2*7^-1 + 3 + 2*7 + 2*7^2 + 2*7^3 + 2*7^4 + 2*7^5 + O(7^6)

        TESTS::

            sage: x = a[:3]
            sage: x.slice(stop=3)
            3 + 6*7 + 4*7^2 + ...
            sage: x.slice(stop=4)
            3 + 6*7 + 4*7^2 + O(7^3)

        Taking slices of slices work as expected::

            sage: a1 = a.slice(5, 10); a1
            7^5 + 6*7^6 + 3*7^7 + 6*7^8 + 5*7^9 + ...
            sage: a2 = a1.slice(3, 8); a2
            7^5 + 6*7^6 + 3*7^7 + ...
            sage: a2 == a.slice(5, 8)
            True"""
    @overload
    def sqrt(self) -> Any:
        """RelaxedElement.sqrt(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 1924)

        Return the square root of this element.

        EXAMPLES::

            sage: R = ZpER(7, 10)
            sage: x = R(8)
            sage: x.sqrt()
            1 + 4*7 + 2*7^2 + 7^3 + 3*7^4 + 2*7^5 + 4*7^6 + 2*7^7 + 5*7^8 + ...

        When the element is not a square, an error is raised::

            sage: x = R(10)
            sage: x.sqrt()
            Traceback (most recent call last):
            ...
            ValueError: not a square

        For bounded elements, the precision is tracked::

            sage: x = R(8, 5); x
            1 + 7 + O(7^5)
            sage: x.sqrt()
            1 + 4*7 + 2*7^2 + 7^3 + 3*7^4 + O(7^5)

        Note that, when `p = 2`, a digit of precision is lost::

            sage: S = ZpER(2)
            sage: x = S(17, 5)
            sage: x.sqrt()
            1 + 2^3 + O(2^4)

        This method also work for self-referent numbers
        (see :meth:`sage.rings.padics.generic_nodes.pAdicRelaxedGeneric.unknown`)::

            sage: x = R.unknown(); x
            O(7^0)
            sage: x.sqrt()
            O(7^0)
            sage: x.set(1 + 7*sqrt(x))
            True
            sage: x
            1 + 7 + 4*7^2 + 4*7^3 + 2*7^4 + 3*7^8 + 3*7^9 + ...

        TESTS::

            sage: for p in [ 7, 11, 1009 ]:
            ....:     R = ZpER(p)
            ....:     x = 1 + p * R.random_element()
            ....:     y = x.sqrt()
            ....:     assert(x == y^2)"""
    @overload
    def sqrt(self) -> Any:
        """RelaxedElement.sqrt(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 1924)

        Return the square root of this element.

        EXAMPLES::

            sage: R = ZpER(7, 10)
            sage: x = R(8)
            sage: x.sqrt()
            1 + 4*7 + 2*7^2 + 7^3 + 3*7^4 + 2*7^5 + 4*7^6 + 2*7^7 + 5*7^8 + ...

        When the element is not a square, an error is raised::

            sage: x = R(10)
            sage: x.sqrt()
            Traceback (most recent call last):
            ...
            ValueError: not a square

        For bounded elements, the precision is tracked::

            sage: x = R(8, 5); x
            1 + 7 + O(7^5)
            sage: x.sqrt()
            1 + 4*7 + 2*7^2 + 7^3 + 3*7^4 + O(7^5)

        Note that, when `p = 2`, a digit of precision is lost::

            sage: S = ZpER(2)
            sage: x = S(17, 5)
            sage: x.sqrt()
            1 + 2^3 + O(2^4)

        This method also work for self-referent numbers
        (see :meth:`sage.rings.padics.generic_nodes.pAdicRelaxedGeneric.unknown`)::

            sage: x = R.unknown(); x
            O(7^0)
            sage: x.sqrt()
            O(7^0)
            sage: x.set(1 + 7*sqrt(x))
            True
            sage: x
            1 + 7 + 4*7^2 + 4*7^3 + 2*7^4 + 3*7^8 + 3*7^9 + ...

        TESTS::

            sage: for p in [ 7, 11, 1009 ]:
            ....:     R = ZpER(p)
            ....:     x = 1 + p * R.random_element()
            ....:     y = x.sqrt()
            ....:     assert(x == y^2)"""
    @overload
    def sqrt(self) -> Any:
        """RelaxedElement.sqrt(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 1924)

        Return the square root of this element.

        EXAMPLES::

            sage: R = ZpER(7, 10)
            sage: x = R(8)
            sage: x.sqrt()
            1 + 4*7 + 2*7^2 + 7^3 + 3*7^4 + 2*7^5 + 4*7^6 + 2*7^7 + 5*7^8 + ...

        When the element is not a square, an error is raised::

            sage: x = R(10)
            sage: x.sqrt()
            Traceback (most recent call last):
            ...
            ValueError: not a square

        For bounded elements, the precision is tracked::

            sage: x = R(8, 5); x
            1 + 7 + O(7^5)
            sage: x.sqrt()
            1 + 4*7 + 2*7^2 + 7^3 + 3*7^4 + O(7^5)

        Note that, when `p = 2`, a digit of precision is lost::

            sage: S = ZpER(2)
            sage: x = S(17, 5)
            sage: x.sqrt()
            1 + 2^3 + O(2^4)

        This method also work for self-referent numbers
        (see :meth:`sage.rings.padics.generic_nodes.pAdicRelaxedGeneric.unknown`)::

            sage: x = R.unknown(); x
            O(7^0)
            sage: x.sqrt()
            O(7^0)
            sage: x.set(1 + 7*sqrt(x))
            True
            sage: x
            1 + 7 + 4*7^2 + 4*7^3 + 2*7^4 + 3*7^8 + 3*7^9 + ...

        TESTS::

            sage: for p in [ 7, 11, 1009 ]:
            ....:     R = ZpER(p)
            ....:     x = 1 + p * R.random_element()
            ....:     y = x.sqrt()
            ....:     assert(x == y^2)"""
    @overload
    def sqrt(self) -> Any:
        """RelaxedElement.sqrt(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 1924)

        Return the square root of this element.

        EXAMPLES::

            sage: R = ZpER(7, 10)
            sage: x = R(8)
            sage: x.sqrt()
            1 + 4*7 + 2*7^2 + 7^3 + 3*7^4 + 2*7^5 + 4*7^6 + 2*7^7 + 5*7^8 + ...

        When the element is not a square, an error is raised::

            sage: x = R(10)
            sage: x.sqrt()
            Traceback (most recent call last):
            ...
            ValueError: not a square

        For bounded elements, the precision is tracked::

            sage: x = R(8, 5); x
            1 + 7 + O(7^5)
            sage: x.sqrt()
            1 + 4*7 + 2*7^2 + 7^3 + 3*7^4 + O(7^5)

        Note that, when `p = 2`, a digit of precision is lost::

            sage: S = ZpER(2)
            sage: x = S(17, 5)
            sage: x.sqrt()
            1 + 2^3 + O(2^4)

        This method also work for self-referent numbers
        (see :meth:`sage.rings.padics.generic_nodes.pAdicRelaxedGeneric.unknown`)::

            sage: x = R.unknown(); x
            O(7^0)
            sage: x.sqrt()
            O(7^0)
            sage: x.set(1 + 7*sqrt(x))
            True
            sage: x
            1 + 7 + 4*7^2 + 4*7^3 + 2*7^4 + 3*7^8 + 3*7^9 + ...

        TESTS::

            sage: for p in [ 7, 11, 1009 ]:
            ....:     R = ZpER(p)
            ....:     x = 1 + p * R.random_element()
            ....:     y = x.sqrt()
            ....:     assert(x == y^2)"""
    @overload
    def sqrt(self) -> Any:
        """RelaxedElement.sqrt(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 1924)

        Return the square root of this element.

        EXAMPLES::

            sage: R = ZpER(7, 10)
            sage: x = R(8)
            sage: x.sqrt()
            1 + 4*7 + 2*7^2 + 7^3 + 3*7^4 + 2*7^5 + 4*7^6 + 2*7^7 + 5*7^8 + ...

        When the element is not a square, an error is raised::

            sage: x = R(10)
            sage: x.sqrt()
            Traceback (most recent call last):
            ...
            ValueError: not a square

        For bounded elements, the precision is tracked::

            sage: x = R(8, 5); x
            1 + 7 + O(7^5)
            sage: x.sqrt()
            1 + 4*7 + 2*7^2 + 7^3 + 3*7^4 + O(7^5)

        Note that, when `p = 2`, a digit of precision is lost::

            sage: S = ZpER(2)
            sage: x = S(17, 5)
            sage: x.sqrt()
            1 + 2^3 + O(2^4)

        This method also work for self-referent numbers
        (see :meth:`sage.rings.padics.generic_nodes.pAdicRelaxedGeneric.unknown`)::

            sage: x = R.unknown(); x
            O(7^0)
            sage: x.sqrt()
            O(7^0)
            sage: x.set(1 + 7*sqrt(x))
            True
            sage: x
            1 + 7 + 4*7^2 + 4*7^3 + 2*7^4 + 3*7^8 + 3*7^9 + ...

        TESTS::

            sage: for p in [ 7, 11, 1009 ]:
            ....:     R = ZpER(p)
            ....:     x = 1 + p * R.random_element()
            ....:     y = x.sqrt()
            ....:     assert(x == y^2)"""
    @overload
    def sqrt(self) -> Any:
        """RelaxedElement.sqrt(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 1924)

        Return the square root of this element.

        EXAMPLES::

            sage: R = ZpER(7, 10)
            sage: x = R(8)
            sage: x.sqrt()
            1 + 4*7 + 2*7^2 + 7^3 + 3*7^4 + 2*7^5 + 4*7^6 + 2*7^7 + 5*7^8 + ...

        When the element is not a square, an error is raised::

            sage: x = R(10)
            sage: x.sqrt()
            Traceback (most recent call last):
            ...
            ValueError: not a square

        For bounded elements, the precision is tracked::

            sage: x = R(8, 5); x
            1 + 7 + O(7^5)
            sage: x.sqrt()
            1 + 4*7 + 2*7^2 + 7^3 + 3*7^4 + O(7^5)

        Note that, when `p = 2`, a digit of precision is lost::

            sage: S = ZpER(2)
            sage: x = S(17, 5)
            sage: x.sqrt()
            1 + 2^3 + O(2^4)

        This method also work for self-referent numbers
        (see :meth:`sage.rings.padics.generic_nodes.pAdicRelaxedGeneric.unknown`)::

            sage: x = R.unknown(); x
            O(7^0)
            sage: x.sqrt()
            O(7^0)
            sage: x.set(1 + 7*sqrt(x))
            True
            sage: x
            1 + 7 + 4*7^2 + 4*7^3 + 2*7^4 + 3*7^8 + 3*7^9 + ...

        TESTS::

            sage: for p in [ 7, 11, 1009 ]:
            ....:     R = ZpER(p)
            ....:     x = 1 + p * R.random_element()
            ....:     y = x.sqrt()
            ....:     assert(x == y^2)"""
    @overload
    def sqrt(self, x) -> Any:
        """RelaxedElement.sqrt(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 1924)

        Return the square root of this element.

        EXAMPLES::

            sage: R = ZpER(7, 10)
            sage: x = R(8)
            sage: x.sqrt()
            1 + 4*7 + 2*7^2 + 7^3 + 3*7^4 + 2*7^5 + 4*7^6 + 2*7^7 + 5*7^8 + ...

        When the element is not a square, an error is raised::

            sage: x = R(10)
            sage: x.sqrt()
            Traceback (most recent call last):
            ...
            ValueError: not a square

        For bounded elements, the precision is tracked::

            sage: x = R(8, 5); x
            1 + 7 + O(7^5)
            sage: x.sqrt()
            1 + 4*7 + 2*7^2 + 7^3 + 3*7^4 + O(7^5)

        Note that, when `p = 2`, a digit of precision is lost::

            sage: S = ZpER(2)
            sage: x = S(17, 5)
            sage: x.sqrt()
            1 + 2^3 + O(2^4)

        This method also work for self-referent numbers
        (see :meth:`sage.rings.padics.generic_nodes.pAdicRelaxedGeneric.unknown`)::

            sage: x = R.unknown(); x
            O(7^0)
            sage: x.sqrt()
            O(7^0)
            sage: x.set(1 + 7*sqrt(x))
            True
            sage: x
            1 + 7 + 4*7^2 + 4*7^3 + 2*7^4 + 3*7^8 + 3*7^9 + ...

        TESTS::

            sage: for p in [ 7, 11, 1009 ]:
            ....:     R = ZpER(p)
            ....:     x = 1 + p * R.random_element()
            ....:     y = x.sqrt()
            ....:     assert(x == y^2)"""
    @overload
    def sqrt(self) -> Any:
        """RelaxedElement.sqrt(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 1924)

        Return the square root of this element.

        EXAMPLES::

            sage: R = ZpER(7, 10)
            sage: x = R(8)
            sage: x.sqrt()
            1 + 4*7 + 2*7^2 + 7^3 + 3*7^4 + 2*7^5 + 4*7^6 + 2*7^7 + 5*7^8 + ...

        When the element is not a square, an error is raised::

            sage: x = R(10)
            sage: x.sqrt()
            Traceback (most recent call last):
            ...
            ValueError: not a square

        For bounded elements, the precision is tracked::

            sage: x = R(8, 5); x
            1 + 7 + O(7^5)
            sage: x.sqrt()
            1 + 4*7 + 2*7^2 + 7^3 + 3*7^4 + O(7^5)

        Note that, when `p = 2`, a digit of precision is lost::

            sage: S = ZpER(2)
            sage: x = S(17, 5)
            sage: x.sqrt()
            1 + 2^3 + O(2^4)

        This method also work for self-referent numbers
        (see :meth:`sage.rings.padics.generic_nodes.pAdicRelaxedGeneric.unknown`)::

            sage: x = R.unknown(); x
            O(7^0)
            sage: x.sqrt()
            O(7^0)
            sage: x.set(1 + 7*sqrt(x))
            True
            sage: x
            1 + 7 + 4*7^2 + 4*7^3 + 2*7^4 + 3*7^8 + 3*7^9 + ...

        TESTS::

            sage: for p in [ 7, 11, 1009 ]:
            ....:     R = ZpER(p)
            ....:     x = 1 + p * R.random_element()
            ....:     y = x.sqrt()
            ....:     assert(x == y^2)"""
    @overload
    def unit_part(self, halt=...) -> Any:
        """RelaxedElement.unit_part(self, halt=True)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 1433)

        Return the unit part of this element.

        INPUT:

        - ``halt`` -- integer or boolean (default: ``True``);
          the absolute precision after which the computation is abandoned
          if the first significant digit has not been found yet.
          If ``True``, the default halting precision of the parent is used.
          If ``False``, the computation is never abandoned.

        EXAMPLES::

            sage: R = ZpER(5, prec=10, halt=10)
            sage: a = R(20/21); a
            4*5 + 4*5^2 + 5^4 + 4*5^6 + 3*5^7 + 4*5^8 + ...
            sage: a.unit_part()
            4 + 4*5 + 5^3 + 4*5^5 + 3*5^6 + 4*5^7 + 5^9 + ...

            sage: b = 1/a; b
            4*5^-1 + 4 + 3*5 + 3*5^2 + 3*5^3 + 3*5^4 + 3*5^5 + 3*5^6 + 3*5^7 + 3*5^8 + ...
            sage: b.unit_part()
            4 + 4*5 + 3*5^2 + 3*5^3 + 3*5^4 + 3*5^5 + 3*5^6 + 3*5^7 + 3*5^8 + 3*5^9 + ...

        The unit part of `0` is not defined::

            sage: R(0).unit_part()
            Traceback (most recent call last):
            ...
            ValueError: unit part of 0 not defined

            sage: R(0, 20).unit_part()
            Traceback (most recent call last):
            ...
            ValueError: unit part of 0 not defined

        See :meth:`valuation` for more details on the parameter ``halt``."""
    @overload
    def unit_part(self) -> Any:
        """RelaxedElement.unit_part(self, halt=True)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 1433)

        Return the unit part of this element.

        INPUT:

        - ``halt`` -- integer or boolean (default: ``True``);
          the absolute precision after which the computation is abandoned
          if the first significant digit has not been found yet.
          If ``True``, the default halting precision of the parent is used.
          If ``False``, the computation is never abandoned.

        EXAMPLES::

            sage: R = ZpER(5, prec=10, halt=10)
            sage: a = R(20/21); a
            4*5 + 4*5^2 + 5^4 + 4*5^6 + 3*5^7 + 4*5^8 + ...
            sage: a.unit_part()
            4 + 4*5 + 5^3 + 4*5^5 + 3*5^6 + 4*5^7 + 5^9 + ...

            sage: b = 1/a; b
            4*5^-1 + 4 + 3*5 + 3*5^2 + 3*5^3 + 3*5^4 + 3*5^5 + 3*5^6 + 3*5^7 + 3*5^8 + ...
            sage: b.unit_part()
            4 + 4*5 + 3*5^2 + 3*5^3 + 3*5^4 + 3*5^5 + 3*5^6 + 3*5^7 + 3*5^8 + 3*5^9 + ...

        The unit part of `0` is not defined::

            sage: R(0).unit_part()
            Traceback (most recent call last):
            ...
            ValueError: unit part of 0 not defined

            sage: R(0, 20).unit_part()
            Traceback (most recent call last):
            ...
            ValueError: unit part of 0 not defined

        See :meth:`valuation` for more details on the parameter ``halt``."""
    @overload
    def unit_part(self) -> Any:
        """RelaxedElement.unit_part(self, halt=True)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 1433)

        Return the unit part of this element.

        INPUT:

        - ``halt`` -- integer or boolean (default: ``True``);
          the absolute precision after which the computation is abandoned
          if the first significant digit has not been found yet.
          If ``True``, the default halting precision of the parent is used.
          If ``False``, the computation is never abandoned.

        EXAMPLES::

            sage: R = ZpER(5, prec=10, halt=10)
            sage: a = R(20/21); a
            4*5 + 4*5^2 + 5^4 + 4*5^6 + 3*5^7 + 4*5^8 + ...
            sage: a.unit_part()
            4 + 4*5 + 5^3 + 4*5^5 + 3*5^6 + 4*5^7 + 5^9 + ...

            sage: b = 1/a; b
            4*5^-1 + 4 + 3*5 + 3*5^2 + 3*5^3 + 3*5^4 + 3*5^5 + 3*5^6 + 3*5^7 + 3*5^8 + ...
            sage: b.unit_part()
            4 + 4*5 + 3*5^2 + 3*5^3 + 3*5^4 + 3*5^5 + 3*5^6 + 3*5^7 + 3*5^8 + 3*5^9 + ...

        The unit part of `0` is not defined::

            sage: R(0).unit_part()
            Traceback (most recent call last):
            ...
            ValueError: unit part of 0 not defined

            sage: R(0, 20).unit_part()
            Traceback (most recent call last):
            ...
            ValueError: unit part of 0 not defined

        See :meth:`valuation` for more details on the parameter ``halt``."""
    @overload
    def unit_part(self) -> Any:
        """RelaxedElement.unit_part(self, halt=True)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 1433)

        Return the unit part of this element.

        INPUT:

        - ``halt`` -- integer or boolean (default: ``True``);
          the absolute precision after which the computation is abandoned
          if the first significant digit has not been found yet.
          If ``True``, the default halting precision of the parent is used.
          If ``False``, the computation is never abandoned.

        EXAMPLES::

            sage: R = ZpER(5, prec=10, halt=10)
            sage: a = R(20/21); a
            4*5 + 4*5^2 + 5^4 + 4*5^6 + 3*5^7 + 4*5^8 + ...
            sage: a.unit_part()
            4 + 4*5 + 5^3 + 4*5^5 + 3*5^6 + 4*5^7 + 5^9 + ...

            sage: b = 1/a; b
            4*5^-1 + 4 + 3*5 + 3*5^2 + 3*5^3 + 3*5^4 + 3*5^5 + 3*5^6 + 3*5^7 + 3*5^8 + ...
            sage: b.unit_part()
            4 + 4*5 + 3*5^2 + 3*5^3 + 3*5^4 + 3*5^5 + 3*5^6 + 3*5^7 + 3*5^8 + 3*5^9 + ...

        The unit part of `0` is not defined::

            sage: R(0).unit_part()
            Traceback (most recent call last):
            ...
            ValueError: unit part of 0 not defined

            sage: R(0, 20).unit_part()
            Traceback (most recent call last):
            ...
            ValueError: unit part of 0 not defined

        See :meth:`valuation` for more details on the parameter ``halt``."""
    @overload
    def unit_part(self) -> Any:
        """RelaxedElement.unit_part(self, halt=True)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 1433)

        Return the unit part of this element.

        INPUT:

        - ``halt`` -- integer or boolean (default: ``True``);
          the absolute precision after which the computation is abandoned
          if the first significant digit has not been found yet.
          If ``True``, the default halting precision of the parent is used.
          If ``False``, the computation is never abandoned.

        EXAMPLES::

            sage: R = ZpER(5, prec=10, halt=10)
            sage: a = R(20/21); a
            4*5 + 4*5^2 + 5^4 + 4*5^6 + 3*5^7 + 4*5^8 + ...
            sage: a.unit_part()
            4 + 4*5 + 5^3 + 4*5^5 + 3*5^6 + 4*5^7 + 5^9 + ...

            sage: b = 1/a; b
            4*5^-1 + 4 + 3*5 + 3*5^2 + 3*5^3 + 3*5^4 + 3*5^5 + 3*5^6 + 3*5^7 + 3*5^8 + ...
            sage: b.unit_part()
            4 + 4*5 + 3*5^2 + 3*5^3 + 3*5^4 + 3*5^5 + 3*5^6 + 3*5^7 + 3*5^8 + 3*5^9 + ...

        The unit part of `0` is not defined::

            sage: R(0).unit_part()
            Traceback (most recent call last):
            ...
            ValueError: unit part of 0 not defined

            sage: R(0, 20).unit_part()
            Traceback (most recent call last):
            ...
            ValueError: unit part of 0 not defined

        See :meth:`valuation` for more details on the parameter ``halt``."""
    @overload
    def val_unit(self, halt=...) -> Any:
        """RelaxedElement.val_unit(self, halt=True)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 1477)

        Return the valuation and the unit part of this element.

        INPUT:

        - ``halt`` -- integer or boolean (default: ``True``);
          the absolute precision after which the computation is abandoned
          if the first significant digit has not been found yet.
          If ``True``, the default halting precision of the parent is used.
          If ``False``, the computation is never abandoned.

        EXAMPLES::

            sage: R = ZpER(5, 10)
            sage: a = R(20/21); a
            4*5 + 4*5^2 + 5^4 + 4*5^6 + 3*5^7 + 4*5^8 + ...
            sage: a.val_unit()
            (1, 4 + 4*5 + 5^3 + 4*5^5 + 3*5^6 + 4*5^7 + 5^9 + ...)

            sage: b = 1/a; b
            4*5^-1 + 4 + 3*5 + 3*5^2 + 3*5^3 + 3*5^4 + 3*5^5 + 3*5^6 + 3*5^7 + 3*5^8 + ...
            sage: b.val_unit()
            (-1, 4 + 4*5 + 3*5^2 + 3*5^3 + 3*5^4 + 3*5^5 + 3*5^6 + 3*5^7 + 3*5^8 + 3*5^9 + ...)

        If this element is indistinguishable from zero, an error is raised
        since the unit part of `0` is not defined::

            sage: R(0).unit_part()
            Traceback (most recent call last):
            ...
            ValueError: unit part of 0 not defined

            sage: R(0, 20).unit_part()
            Traceback (most recent call last):
            ...
            ValueError: unit part of 0 not defined

        See :meth:`valuation` for more details on the parameter ``halt``."""
    @overload
    def val_unit(self) -> Any:
        """RelaxedElement.val_unit(self, halt=True)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 1477)

        Return the valuation and the unit part of this element.

        INPUT:

        - ``halt`` -- integer or boolean (default: ``True``);
          the absolute precision after which the computation is abandoned
          if the first significant digit has not been found yet.
          If ``True``, the default halting precision of the parent is used.
          If ``False``, the computation is never abandoned.

        EXAMPLES::

            sage: R = ZpER(5, 10)
            sage: a = R(20/21); a
            4*5 + 4*5^2 + 5^4 + 4*5^6 + 3*5^7 + 4*5^8 + ...
            sage: a.val_unit()
            (1, 4 + 4*5 + 5^3 + 4*5^5 + 3*5^6 + 4*5^7 + 5^9 + ...)

            sage: b = 1/a; b
            4*5^-1 + 4 + 3*5 + 3*5^2 + 3*5^3 + 3*5^4 + 3*5^5 + 3*5^6 + 3*5^7 + 3*5^8 + ...
            sage: b.val_unit()
            (-1, 4 + 4*5 + 3*5^2 + 3*5^3 + 3*5^4 + 3*5^5 + 3*5^6 + 3*5^7 + 3*5^8 + 3*5^9 + ...)

        If this element is indistinguishable from zero, an error is raised
        since the unit part of `0` is not defined::

            sage: R(0).unit_part()
            Traceback (most recent call last):
            ...
            ValueError: unit part of 0 not defined

            sage: R(0, 20).unit_part()
            Traceback (most recent call last):
            ...
            ValueError: unit part of 0 not defined

        See :meth:`valuation` for more details on the parameter ``halt``."""
    @overload
    def val_unit(self) -> Any:
        """RelaxedElement.val_unit(self, halt=True)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 1477)

        Return the valuation and the unit part of this element.

        INPUT:

        - ``halt`` -- integer or boolean (default: ``True``);
          the absolute precision after which the computation is abandoned
          if the first significant digit has not been found yet.
          If ``True``, the default halting precision of the parent is used.
          If ``False``, the computation is never abandoned.

        EXAMPLES::

            sage: R = ZpER(5, 10)
            sage: a = R(20/21); a
            4*5 + 4*5^2 + 5^4 + 4*5^6 + 3*5^7 + 4*5^8 + ...
            sage: a.val_unit()
            (1, 4 + 4*5 + 5^3 + 4*5^5 + 3*5^6 + 4*5^7 + 5^9 + ...)

            sage: b = 1/a; b
            4*5^-1 + 4 + 3*5 + 3*5^2 + 3*5^3 + 3*5^4 + 3*5^5 + 3*5^6 + 3*5^7 + 3*5^8 + ...
            sage: b.val_unit()
            (-1, 4 + 4*5 + 3*5^2 + 3*5^3 + 3*5^4 + 3*5^5 + 3*5^6 + 3*5^7 + 3*5^8 + 3*5^9 + ...)

        If this element is indistinguishable from zero, an error is raised
        since the unit part of `0` is not defined::

            sage: R(0).unit_part()
            Traceback (most recent call last):
            ...
            ValueError: unit part of 0 not defined

            sage: R(0, 20).unit_part()
            Traceback (most recent call last):
            ...
            ValueError: unit part of 0 not defined

        See :meth:`valuation` for more details on the parameter ``halt``."""
    @overload
    def valuation(self, halt=..., secure=...) -> Any:
        """RelaxedElement.valuation(self, halt=True, secure=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 1329)

        Return the valuation of this element.

        INPUT:

        - ``halt`` -- integer or boolean (default: ``True``);
          the absolute precision after which the computation is abandoned
          if the first significant digit has not been found yet.
          If ``True``, the default halting precision of the parent is used.
          If ``False``, the computation is never abandoned.

        - ``secure`` -- boolean (default: the value given at the creation
          of the parent); when the valuation cannot be determined for sure,
          raise an error if ``secure`` is ``True``, return the best known
          lower bound on the valuation otherwise

        EXAMPLES::

            sage: R = ZpER(5, prec=10, halt=10)
            sage: a = R(2001); a
            1 + 5^3 + 3*5^4 + ...
            sage: a.valuation()
            0

            sage: b = a - 1/a; b
            2*5^3 + 5^4 + 5^5 + 4*5^6 + 3*5^7 + 4*5^8 + 3*5^9 + 3*5^10 + 3*5^11 + 5^12 + ...
            sage: b.valuation()
            3

        The valuation of an exact zero is `+\\infty`::

            sage: R(0).valuation()
            +Infinity

        The valuation of an inexact zero is its absolute precision::

            sage: R(0, 20).valuation()
            20

        We illustrate the behaviour of the parameter ``halt``.
        We create a very small number whose first significant is far beyond
        the default precision::

            sage: z = R(5^20)
            sage: z
            0 + ...

        Without any help, Sage does not run the computation far enough to determine
        the valuation and outputs only a lower bound::

            sage: z.valuation()
            10

        With ``secure=True``, an error is raised::

            sage: z.valuation(secure=True)
            Traceback (most recent call last):
            ...
            PrecisionError: cannot determine the valuation; try to increase the halting precision

        By setting the argument ``halt``, one can force the computation to continue
        until a prescribed limit::

            sage: z.valuation(halt=15)   # not enough to find the correct valuation
            15
            sage: z.valuation(halt=20, secure=True)
            Traceback (most recent call last):
            ...
            PrecisionError: cannot determine the valuation; try to increase the halting precision

            sage: z.valuation(halt=21)   # now, we're okay
            20

        .. NOTE::

            It is also possible to pass in ``halt=False`` but it is not recommended
            because the computation can hang forever if this element is `0`.

        TESTS::

            sage: x = R.unknown()
            sage: (~x).valuation()
            Traceback (most recent call last):
            ...
            PrecisionError: no lower bound on the valuation is known"""
    @overload
    def valuation(self) -> Any:
        """RelaxedElement.valuation(self, halt=True, secure=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 1329)

        Return the valuation of this element.

        INPUT:

        - ``halt`` -- integer or boolean (default: ``True``);
          the absolute precision after which the computation is abandoned
          if the first significant digit has not been found yet.
          If ``True``, the default halting precision of the parent is used.
          If ``False``, the computation is never abandoned.

        - ``secure`` -- boolean (default: the value given at the creation
          of the parent); when the valuation cannot be determined for sure,
          raise an error if ``secure`` is ``True``, return the best known
          lower bound on the valuation otherwise

        EXAMPLES::

            sage: R = ZpER(5, prec=10, halt=10)
            sage: a = R(2001); a
            1 + 5^3 + 3*5^4 + ...
            sage: a.valuation()
            0

            sage: b = a - 1/a; b
            2*5^3 + 5^4 + 5^5 + 4*5^6 + 3*5^7 + 4*5^8 + 3*5^9 + 3*5^10 + 3*5^11 + 5^12 + ...
            sage: b.valuation()
            3

        The valuation of an exact zero is `+\\infty`::

            sage: R(0).valuation()
            +Infinity

        The valuation of an inexact zero is its absolute precision::

            sage: R(0, 20).valuation()
            20

        We illustrate the behaviour of the parameter ``halt``.
        We create a very small number whose first significant is far beyond
        the default precision::

            sage: z = R(5^20)
            sage: z
            0 + ...

        Without any help, Sage does not run the computation far enough to determine
        the valuation and outputs only a lower bound::

            sage: z.valuation()
            10

        With ``secure=True``, an error is raised::

            sage: z.valuation(secure=True)
            Traceback (most recent call last):
            ...
            PrecisionError: cannot determine the valuation; try to increase the halting precision

        By setting the argument ``halt``, one can force the computation to continue
        until a prescribed limit::

            sage: z.valuation(halt=15)   # not enough to find the correct valuation
            15
            sage: z.valuation(halt=20, secure=True)
            Traceback (most recent call last):
            ...
            PrecisionError: cannot determine the valuation; try to increase the halting precision

            sage: z.valuation(halt=21)   # now, we're okay
            20

        .. NOTE::

            It is also possible to pass in ``halt=False`` but it is not recommended
            because the computation can hang forever if this element is `0`.

        TESTS::

            sage: x = R.unknown()
            sage: (~x).valuation()
            Traceback (most recent call last):
            ...
            PrecisionError: no lower bound on the valuation is known"""
    @overload
    def valuation(self) -> Any:
        """RelaxedElement.valuation(self, halt=True, secure=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 1329)

        Return the valuation of this element.

        INPUT:

        - ``halt`` -- integer or boolean (default: ``True``);
          the absolute precision after which the computation is abandoned
          if the first significant digit has not been found yet.
          If ``True``, the default halting precision of the parent is used.
          If ``False``, the computation is never abandoned.

        - ``secure`` -- boolean (default: the value given at the creation
          of the parent); when the valuation cannot be determined for sure,
          raise an error if ``secure`` is ``True``, return the best known
          lower bound on the valuation otherwise

        EXAMPLES::

            sage: R = ZpER(5, prec=10, halt=10)
            sage: a = R(2001); a
            1 + 5^3 + 3*5^4 + ...
            sage: a.valuation()
            0

            sage: b = a - 1/a; b
            2*5^3 + 5^4 + 5^5 + 4*5^6 + 3*5^7 + 4*5^8 + 3*5^9 + 3*5^10 + 3*5^11 + 5^12 + ...
            sage: b.valuation()
            3

        The valuation of an exact zero is `+\\infty`::

            sage: R(0).valuation()
            +Infinity

        The valuation of an inexact zero is its absolute precision::

            sage: R(0, 20).valuation()
            20

        We illustrate the behaviour of the parameter ``halt``.
        We create a very small number whose first significant is far beyond
        the default precision::

            sage: z = R(5^20)
            sage: z
            0 + ...

        Without any help, Sage does not run the computation far enough to determine
        the valuation and outputs only a lower bound::

            sage: z.valuation()
            10

        With ``secure=True``, an error is raised::

            sage: z.valuation(secure=True)
            Traceback (most recent call last):
            ...
            PrecisionError: cannot determine the valuation; try to increase the halting precision

        By setting the argument ``halt``, one can force the computation to continue
        until a prescribed limit::

            sage: z.valuation(halt=15)   # not enough to find the correct valuation
            15
            sage: z.valuation(halt=20, secure=True)
            Traceback (most recent call last):
            ...
            PrecisionError: cannot determine the valuation; try to increase the halting precision

            sage: z.valuation(halt=21)   # now, we're okay
            20

        .. NOTE::

            It is also possible to pass in ``halt=False`` but it is not recommended
            because the computation can hang forever if this element is `0`.

        TESTS::

            sage: x = R.unknown()
            sage: (~x).valuation()
            Traceback (most recent call last):
            ...
            PrecisionError: no lower bound on the valuation is known"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __eq__(self, other) -> Any:
        """RelaxedElement.__eq__(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 758)

        Return ``True`` of this element is equal to ``other``.

        TESTS::

            sage: R = ZpER(5)
            sage: x = R(1/2)
            sage: y = R(1/3)
            sage: z = R(1/6)

            sage: x == y + z
            True

        We illustrate the effect of the keyword ``secure``::

            sage: R.is_secure()
            False
            sage: s = y + z + 5^50
            sage: x == s
            True

            sage: S = ZpER(5, secure=True)
            sage: S(x) == S(s)
            Traceback (most recent call last):
            ...
            PrecisionError: unable to decide equality; try to bound precision

        Note that, when ``secure=False``, once more digits have been
        computed, the answer can change::

            sage: x[:100] == s
            False
            sage: x == s
            False

        .. SEEALSO::

            :meth:`is_equal_to`"""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __getitem__(self, n) -> Any:
        """RelaxedElement.__getitem__(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 434)

        Return the `n`-th digit of this relaxed `p`-adic number if `n` is an integer
        or return a bounded relaxed `p`-adic corresponding to the given slice if `n` is a slice.

        INPUT:

        - ``n`` -- integer or a slice

        EXAMPLES::

            sage: R = ZpER(7, 10)
            sage: a = R(1/2021); a
            3 + 6*7 + 4*7^2 + 3*7^3 + 6*7^4 + 7^5 + 6*7^6 + 3*7^7 + 6*7^8 + 5*7^9 + ...

            sage: a[3]
            3
            sage: a[3:6]
            3*7^3 + 6*7^4 + 7^5 + O(7^6)

        Unbounded slices are allowed::

            sage: a[:3]
            3 + 6*7 + 4*7^2 + O(7^3)
            sage: a[3:]
            3*7^3 + 6*7^4 + 7^5 + 6*7^6 + 3*7^7 + 6*7^8 + 5*7^9 + ...

        .. SEEALSO::

            :meth:`digit`, :meth:`slice`

        TESTS::

            sage: a[3:6:2]
            Traceback (most recent call last):
            ...
            NotImplementedError: step is not allowed"""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __invert__(self) -> Any:
        """RelaxedElement.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 1824)

        Return the multiplicative inverse of this element.

        .. NOTE::

            The result always lives in the fraction field, even if this element
            is a unit.

        EXAMPLES::

            sage: R = ZpER(7, 10)
            sage: x = ~R(3)
            sage: x
            5 + 4*7 + 4*7^2 + 4*7^3 + 4*7^4 + 4*7^5 + 4*7^6 + 4*7^7 + 4*7^8 + 4*7^9 + ...
            sage: x.parent()
            7-adic Field handled with relaxed arithmetics

        TESTS::

            sage: ~R(0)
            Traceback (most recent call last):
            ...
            ZeroDivisionError: cannot divide by zero

            sage: ~R(0, 10)
            Traceback (most recent call last):
            ...
            ZeroDivisionError: cannot divide by something indistinguishable from zero

            sage: y = R.unknown()
            sage: ~y
            O(7^-Infinity)"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lshift__(self, s) -> Any:
        """RelaxedElement.__lshift__(self, s)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 1672)

        Return this element multiplied by `\\pi^s`.

        If `s` is negative and this element does not lie in a field,
        digits may be truncated.  See ``__rshift__`` for details.

        EXAMPLES::

            sage: R = ZpER(997)
            sage: K = R.fraction_field()
            sage: a = R(123456878908); a
            964*997 + 572*997^2 + 124*997^3 + ...

        Shifting to the right divides by a power of `p`, but drops
        terms with negative valuation::

            sage: a << 2
            964*997^3 + 572*997^4 + 124*997^5 + ...

        A negative shift may result in a truncation when the base
        ring is not a field::

            sage: a << -3
            124 + ...

            sage: K(a) << -3
            964*997^-2 + 572*997^-1 + 124 + ..."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __reduce__(self) -> Any:
        """RelaxedElement.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 94)

        Return a tuple of a function and data that can be used to unpickle
        this element.

        TESTS::

            sage: R = ZpER(5)
            sage: a = R(0)
            sage: loads(dumps(a)) == a
            True"""
    def __rlshift__(self, other):
        """Return value<<self."""
    def __rrshift__(self, other):
        """Return value>>self."""
    def __rshift__(self, s) -> Any:
        """RelaxedElement.__rshift__(self, s)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 1633)

        Return this element divided by `\\pi^s`, and truncated
        if the parent is not a field.

        EXAMPLES::

            sage: R = ZpER(997)
            sage: K = R.fraction_field()
            sage: a = R(123456878908); a
            964*997 + 572*997^2 + 124*997^3 + ...

        Shifting to the right divides by a power of `p`, but drops
        terms with negative valuation::

            sage: a >> 3
            124 + ...

        If the parent is a field no truncation is performed::

            sage: K(a) >> 3
            964*997^-2 + 572*997^-1 + 124 + ...

        A negative shift multiplies by that power of `p`::

            sage: a >> -3
            964*997^4 + 572*997^5 + 124*997^6 + ..."""

class RelaxedElementWithDigits(RelaxedElement):
    """File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 2059)

        A generic class for relaxed `p`-adic elements that stores
        the sequence of its digits.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class RelaxedElement_abandon(RelaxedElement):
    """RelaxedElement_abandon()

    File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 2021)

    A special class for relaxed `p`-adic with all digits unknown.

    This class is used for setting temporary definition of
    some self-referent numbers."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 2028)

                Initialize this element.

                TESTS::

                    sage: from sage.rings.padics.padic_relaxed_element import RelaxedElement_abandon
                    sage: x = RelaxedElement_abandon()
                    sage: x.valuation()
                    Traceback (most recent call last):
                    ...
                    PrecisionError: no lower bound on the valuation is known

                    sage: x[0]
                    Traceback (most recent call last):
                    ...
                    PrecisionError: computation has been abandoned; try to increase precision
        """

class RelaxedElement_add(RelaxedElementWithDigits):
    """RelaxedElement_add(parent, RelaxedElement x, RelaxedElement y)

    File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 2836)

    A class for relaxed `p`-adic numbers defined as sums.

    TESTS::

        sage: R = ZpER(11)
        sage: x = R.random_element() + R.random_element()
        sage: TestSuite(x).run()"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, RelaxedElementx, RelaxedElementy) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 2846)

                Initialize this element.

                INPUT:

                - ``parent`` -- the parent of this element

                - ``x`` -- a relaxed `p`-adic element, the first summand

                - ``y`` -- a relaxed `p`-adic element, the second summand

                TESTS::

                    sage: R = ZpER(11)
                    sage: x = R.random_element() + R.random_element()
                    sage: type(x)
                    <class 'sage.rings.padics.padic_relaxed_element.pAdicRelaxedElement_add'>
        """
    def __reduce__(self) -> Any:
        """RelaxedElement_add.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 2873)

        Return a tuple of a function and data that can be used to unpickle this
        element.

        TESTS::

            sage: R = ZpER(5)
            sage: x = R.random_element() + R.random_element()
            sage: x == loads(dumps(x))  # indirect doctest
            True"""

class RelaxedElement_bound(RelaxedElement):
    """RelaxedElement_bound(parent, RelaxedElement x, precbound=None)

    File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 2296)

    A class for `p`-adic relaxed elements which are defined by bounding the
    precision of another `p`-adic relaxed element.

    TESTS::

        sage: R = ZpER(5)
        sage: x = R.random_element()
        sage: y = x[:20]
        sage: TestSuite(y).run()"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, RelaxedElementx, precbound=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 2308)

                Initialize this element.

                INPUT:

                - ``parent`` -- the parent of this element

                - ``x`` -- a relaxed `p`-adics, the element to bound

                - ``precbound`` -- integer or ``None`` (default: ``None``);
                  the bound on the precision

                .. NOTE::

                    The digits of ``x`` are not copied!

                TESTS::

                    sage: R = ZpER(5)
                    sage: x = R(20/21)
                    sage: y = x.add_bigoh(20)
                    sage: type(y)
                    <class 'sage.rings.padics.padic_relaxed_element.pAdicRelaxedElement_bound'>
        """
    def __reduce__(self) -> Any:
        """RelaxedElement_bound.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 2343)

        Return a tuple of a function and data that can be used to unpickle this
        element.

        TESTS::

            sage: a = ZpER(5)(1).add_bigoh(20)
            sage: type(a)
            <class 'sage.rings.padics.padic_relaxed_element.pAdicRelaxedElement_bound'>
            sage: a == loads(dumps(a))   # indirect doctest
            True"""

class RelaxedElement_div(RelaxedElementWithDigits):
    """RelaxedElement_div(parent, RelaxedElement num, RelaxedElement denom, long minval=-maxordp, precbound=None)

    File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 3271)

    A class for relaxed `p`-adic numbers defined as quotients.

    ALGORITHM:

    We compute the quotient `x = a/b` as the self-referent number defined by

    .. MATH::

        x = ac + (1 - bc) x

    where `c` is congruent to `b^{-1}` modulo the uniformizer.

    TESTS::

        sage: R = ZpER(5)
        sage: x = R(20) / R(21)
        sage: TestSuite(x).run()"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, RelaxedElementnum, RelaxedElementdenom, longminval=..., precbound=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 3303)

                Initialize this element.

                INPUT:

                - ``parent`` -- the parent of this element

                - ``num`` -- a relaxed `p`-adic element, the dividend

                - ``denom`` -- a relaxed `p`-adic element, the divisor

                - ``minval`` -- integer; the minimal valuation allowed for this element

                - ``precbound`` -- integer or ``None`` (default: ``None``);
                  the bound on the precision

                TESTS::

                    sage: R = ZpER(5)
                    sage: x = R(20) / R(21)
                    sage: type(x)
                    <class 'sage.rings.padics.padic_relaxed_element.pAdicRelaxedElement_div'>

                    sage: y = R.unknown()
                    sage: 1/y
                    O(5^-Infinity)
                    sage: y.inverse_of_unit()
                    O(5^0)
        """
    def __reduce__(self) -> Any:
        """RelaxedElement_div.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 3356)

        Return a tuple of a function and data that can be used to unpickle this
        element.

        TESTS::

            sage: R = ZpER(5)
            sage: x = R(20) / R(21)
            sage: x == loads(dumps(x))  # indirect doctest
            True"""

class RelaxedElement_mul(RelaxedElementWithDigits):
    """RelaxedElement_mul(parent, RelaxedElement x, RelaxedElement y)

    File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 3051)

    A class for relaxed `p`-adic numbers defined as products.

    ALGORITHM:

    We compute digits using relaxed arithmetic by var der Hoeven et al.,
    whose cost is quasi-linear with respect to the precision.

    The algorithm uses the entries behind the current position in the table
    ``self._digits`` to store carries.

    TESTS::

        sage: R = ZpER(11)
        sage: x = R.random_element() * R.random_element()
        sage: TestSuite(x).run()"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, RelaxedElementx, RelaxedElementy) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 3083)

                Initialize this element.

                INPUT:

                - ``parent`` -- the parent of this element

                - ``x`` -- a relaxed `p`-adic element, the first factor

                - ``y`` -- a relaxed `p`-adic element, the second factor

                TESTS::

                    sage: R = ZpER(11)
                    sage: x = R.random_element() * R.random_element()
                    sage: type(x)
                    <class 'sage.rings.padics.padic_relaxed_element.pAdicRelaxedElement_mul'>
        """
    def __reduce__(self) -> Any:
        """RelaxedElement_mul.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 3115)

        Return a tuple of a function and data that can be used to unpickle this
        element.

        TESTS::

            sage: R = ZpER(5)
            sage: x = R.random_element() * R.random_element()
            sage: x == loads(dumps(x))  # indirect doctest
            True"""

class RelaxedElement_muldigit(RelaxedElementWithDigits):
    """RelaxedElement_muldigit(parent, RelaxedElement_div x, RelaxedElement y)

    File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 3223)

    A class for relaxed `p`-adic numbers defined as products
    of a relaxed `p`-adic number by a digit.

    This class is not exposed to the user; it is only used
    internally for division."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, RelaxedElement_divx, RelaxedElementy) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 3231)

                Initialize this element.

                INPUT:

                - ``parent`` -- the parent of this element

                - ``x`` -- a relaxed `p`-adic element, whose first significant
                  digit is the first factor

                - ``y`` -- a relaxed `p`-adic element, the second factor
        """

class RelaxedElement_one(RelaxedElementWithDigits):
    """RelaxedElement_one(parent)

    File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 2218)

    A class for representation a relaxed `p`-adic number which is
    exactly one.

    TESTS::

        sage: R = ZpER(7)
        sage: a = R.one()
        sage: TestSuite(a).run()"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 2229)

                Initialize this element.

                INPUT:

                - ``parent`` -- the parent of this element

                TESTS::

                    sage: R = ZpER(5)
                    sage: x = R(1)  # indirect doctest
                    sage: x
                    1 + ...

                    sage: type(x)
                    <class 'sage.rings.padics.padic_relaxed_element.pAdicRelaxedElement_one'>
        """
    def __reduce__(self) -> Any:
        """RelaxedElement_one.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 2251)

        Return a tuple of a function and data that can be used to unpickle this
        element.

        TESTS::

            sage: a = ZpER(5)(1)
            sage: type(a)
            <class 'sage.rings.padics.padic_relaxed_element.pAdicRelaxedElement_one'>
            sage: a[:20] == loads(dumps(a))   # indirect doctest
            True"""

class RelaxedElement_random(RelaxedElementWithDigits):
    """RelaxedElement_random(parent, valuation, precbound=None, seed=None)

    File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 2555)

    A class for random relaxed `p`-adic numbers.

    TESTS::

        sage: R = ZpER(5)
        sage: x = R.random_element()
        sage: TestSuite(x).run()"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, valuation, precbound=..., seed=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 2565)

                Initialize this element.

                INPUT:

                - ``parent`` -- the parent of this element

                - ``valuation`` -- integer or ``None``; the position from which
                  random digits are picked;
                  if ``None``, it is randomly chosen if the parent is a field and
                  set to `0` otherwise

                - ``precbound`` -- integer or ``None`` (default: ``None``);
                  the bound on the precision

                - ``seed`` -- integer or ``None`` (default: ``None``); the
                  seed of the random generator

                .. NOTE::

                    The argument ``valuation`` can be different from the real
                    valuation of this number since the first randomly picked
                    digit could vanish.

                TESTS::

                    sage: R = ZpER(7)
                    sage: x = R.random_element()
                    sage: type(x)
                    <class 'sage.rings.padics.padic_relaxed_element.pAdicRelaxedElement_random'>
        """
    def __reduce__(self) -> Any:
        """RelaxedElement_random.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 2612)

        Return a tuple of a function and data that can be used to unpickle this
        element.

        TESTS::

            sage: R = ZpER(5, print_mode='digits')
            sage: a = R.random_element()
            sage: a   # random
            ...32220241412003314311

            sage: b = loads(dumps(a))
            sage: b   # random
            ...32220241412003314311

        It is guaranteed that `a` and `b` are equal at any precision::

            sage: a[:30]   # random
            ...?343214211432220241412003314311
            sage: b[:30]   # random
            ...?343214211432220241412003314311

            sage: a == b
            True"""

class RelaxedElement_slice(RelaxedElement):
    """RelaxedElement_slice(parent, RelaxedElement x, long start, long stop, long shift)

    File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 2665)

    A class for relaxed `p`-adic numbers defined as slices.

    TESTS::

        sage: R = ZpER(5)
        sage: x = R(20/21)
        sage: y = x.slice(3, 6)
        sage: TestSuite(y).run()"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, RelaxedElementx, longstart, longstop, longshift) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 2676)

                Initialize this element.

                INPUT:

                - ``parent`` -- the parent of this element

                - ``x`` -- a relaxed `p`-adic element, the element from which the
                  slice is extracted

                - ``start`` -- integer; the position of the first digit of `x`
                  in the slice

                - ``stop`` -- integer; the position of the first digit of `x`
                  after the slice

                - ``shift`` -- integer such that ``self[i] = x[i+shift]``

                .. NOTE::

                    The digits of ``x`` are not copied!

                TESTS::

                    sage: R = ZpER(5)
                    sage: x = R(20/21)
                    sage: y = x.slice(3, 6)
                    sage: type(y)
                    <class 'sage.rings.padics.padic_relaxed_element.pAdicRelaxedElement_slice'>
        """
    def __reduce__(self) -> Any:
        """RelaxedElement_slice.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 2723)

        Return a tuple of a function and data that can be used to unpickle this
        element.

        TESTS::

            sage: R = ZpER(5, print_mode='digits')
            sage: x = R(20/21)
            sage: y = x.slice(3, 6)
            sage: y == loads(dumps(y))  # indirect doctest
            True"""

class RelaxedElement_sqrt(RelaxedElementWithDigits):
    """RelaxedElement_sqrt(parent, RelaxedElement x)

    File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 3444)

    A class for relaxed `p`-adic numbers defined as square roots.

    ALGORITHM:

    When `p \\neq 2`, we compute `y = \\sqrt{x}` as the self-referent number
    defined by

    .. MATH::

        y = \\frac{x - (y-a)^2 + a^2}{2a}

    where `a^2` is congruent to `x` modulo the uniformizer.

    When `p = 2`, we use a variant of this construction.

    TESTS::

        sage: R = ZpER(5)
        sage: x = R(6).sqrt()
        sage: TestSuite(x).run()"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, RelaxedElementx) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 3467)

                Initialize this element.

                INPUT:

                - ``parent`` -- the parent of this element

                - ``x`` -- a relaxed `p`-adic element

                TESTS::

                    sage: R = ZpER(5)
                    sage: x = R(6).sqrt()
                    sage: type(x)
                    <class 'sage.rings.padics.padic_relaxed_element.pAdicRelaxedElement_sqrt'>
        """
    def __reduce__(self) -> Any:
        """RelaxedElement_sqrt.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 3501)

        Return a tuple of a function and data that can be used to unpickle this
        element.

        TESTS::

            sage: R = ZpER(5)
            sage: x = R(6).sqrt()
            sage: x == loads(dumps(x))  # indirect doctest
            True"""

class RelaxedElement_sub(RelaxedElementWithDigits):
    """RelaxedElement_sub(parent, RelaxedElement x, RelaxedElement y)

    File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 2944)

    A class for relaxed `p`-adic numbers defined as differences.

    TESTS::

        sage: R = ZpER(11)
        sage: x = R.random_element() - R.random_element()
        sage: TestSuite(x).run()"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, RelaxedElementx, RelaxedElementy) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 2954)

                Initialize this element.

                INPUT:

                - ``parent`` -- the parent of this element

                - ``x`` -- a relaxed `p`-adic element, the minuend

                - ``y`` -- a relaxed `p`-adic element, the subtrahend

                TESTS::

                    sage: R = ZpER(11)
                    sage: x = R.random_element() - R.random_element()
                    sage: type(x)
                    <class 'sage.rings.padics.padic_relaxed_element.pAdicRelaxedElement_sub'>
        """
    def __reduce__(self) -> Any:
        """RelaxedElement_sub.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 2980)

        Return a tuple of a function and data that can be used to unpickle this
        element.

        TESTS::

            sage: R = ZpER(5)
            sage: x = R.random_element() - R.random_element()
            sage: x == loads(dumps(x))  # indirect doctest
            True"""

class RelaxedElement_teichmuller(RelaxedElementWithDigits):
    """RelaxedElement_teichmuller(parent, xbar)

    File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 3618)

    A class for relaxed `p`-adic numbers defined as teichmüller representatives.

    ALGORITHM:

    We compute `x = [a]` as the unique self-referent number with last
    digit `a` and `x = x^p`.
    Note that `x^p` is known with one more digit than `x` itself.

    TESTS::

        sage: R = ZpER(7)
        sage: x = R.teichmuller(2)
        sage: TestSuite(x).run()"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, xbar) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 3634)

                Initialize this element.

                INPUT:

                - ``parent`` -- the parent of this element

                - ``xbar`` -- an element in the exact subring, which is congruent
                  to this Teichmüller modulo this uniformizer

                TESTS::

                    sage: R = ZpER(7)
                    sage: x = R.teichmuller(2)
                    sage: type(x)
                    <class 'sage.rings.padics.padic_relaxed_element.pAdicRelaxedElement_teichmuller'>
        """
    def __reduce__(self) -> Any:
        """RelaxedElement_teichmuller.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 3685)

        Return a tuple of a function and data that can be used to unpickle this
        element.

        TESTS::

            sage: R = ZpER(7)
            sage: x = R.teichmuller(2)
            sage: x == loads(dumps(x))  # indirect doctest
            True"""

class RelaxedElement_unknown(RelaxedElementWithDigits):
    """RelaxedElement_unknown(parent, long valuation, digits=None)

    File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 3748)

    A class for self-referent relaxed `p`-adic numbers.

    TESTS::

        sage: R = ZpER(7)
        sage: x = R.unknown()
        sage: TestSuite(x).run()

        sage: x.set(1 + 7*x^2)
        True
        sage: TestSuite(x).run()"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, longvaluation, digits=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 3762)

                Initialize this element.

                INPUT:

                - ``parent`` -- the parent of this element

                - ``valuation`` -- integer; a lower bound on the valuation of
                  this number

                - ``digits`` -- list or ``None`` (default: ``None``); the first
                  significant digits of this number

                TESTS::

                    sage: R = ZpER(7)
                    sage: x = R.unknown()
                    sage: type(x)
                    <class 'sage.rings.padics.padic_relaxed_element.pAdicRelaxedElement_unknown'>
        """
    def set(self, RelaxedElementdefinition) -> Any:
        """RelaxedElement_unknown.set(self, RelaxedElement definition)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 3827)

        Set the recursive definition of this self-referent number.

        INPUT:

        - ``definition`` -- a relaxed `p`-adic number, to which this
          number is equal

        OUTPUT:

        A boolean indicating if the definition is coherent with the
        already known digits of this number.

        EXAMPLES::

            sage: R = ZpER(5, 10)
            sage: x = R.unknown()
            sage: x.set(1 + 5*x)
            True
            sage: x
            1 + 5 + 5^2 + 5^3 + 5^4 + 5^5 + 5^6 + 5^7 + 5^8 + 5^9 + ...

        The previous construction works because the relation we gave defines
        the `n`-th digit of `x` in terms of its digits at precision strictly
        less than `n` (this is due to the multiplication by `5`).

        On the contrary, the following does not work::

            sage: y = R.unknown()
            sage: y.set(1 + 3*y)
            True
            sage: y
            O(5^0)
            sage: y[:20]
            Traceback (most recent call last):
            ...
            RecursionError: definition looks circular

        In the next example, we give explicit values for the first digits
        and then a recursive definition for the next digits. However, the
        recursive definition does not hold for the first digits; that is the
        reason why the call to :meth:`set` returns ``False``::

            sage: z = R.unknown(digits=[2])
            sage: z
            2 + O(5)
            sage: z.set(1 + 5*z)
            False
            sage: z
            2 + 2*5 + 2*5^2 + 2*5^3 + 2*5^4 + 2*5^5 + 2*5^6 + 2*5^7 + 2*5^8 + 2*5^9 + ...

        .. SEEALSO::

            :meth:`sage.rings.padics.generic_nodes.pAdicRelaxedGeneric.unknown`"""
    def __reduce__(self) -> Any:
        """RelaxedElement_unknown.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 3804)

        Return a tuple of a function and data that can be used to unpickle this
        element.

        TESTS::

            sage: R = ZpER(7)
            sage: x = R.unknown()
            sage: x.set(1 + 7*x^2)
            True
            sage: x == loads(dumps(x))  # indirect doctest
            True"""

class RelaxedElement_value(RelaxedElementWithDigits):
    """RelaxedElement_value(parent, value, long shift=0, precbound=None)

    File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 2436)

    A class for relaxed `p`-adics defined by the datum of a value in
    the exact subring.

    TESTS::

        sage: R = ZpER(5)
        sage: x = R(2)
        sage: TestSuite(x).run()"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, value, longshift=..., precbound=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 2447)

                Initialize this element.

                INPUT:

                - ``parent`` -- the parent of this element

                - ``value`` -- the value in the exact subring

                - ``shift`` -- integer (default: `0`); the position at which
                  the given value is written

                - ``precbound`` -- integer or ``None`` (default: ``None``);
                  the bound on the precision

                TESTS::

                    sage: R = ZpER(5)
                    sage: x = R(2)
                    sage: type(x)
                    <class 'sage.rings.padics.padic_relaxed_element.pAdicRelaxedElement_value'>

                    sage: y = R(2, 10)
                    sage: type(y)
                    <class 'sage.rings.padics.padic_relaxed_element.pAdicRelaxedElement_value'>
        """
    def __reduce__(self) -> Any:
        """RelaxedElement_value.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 2484)

        Return a tuple of a function and data that can be used to unpickle this
        element.

        TESTS::

            sage: a = ZpER(5)(2, 20)
            sage: type(a)
            <class 'sage.rings.padics.padic_relaxed_element.pAdicRelaxedElement_value'>
            sage: a == loads(dumps(a))   # indirect doctest
            True"""

class RelaxedElement_zero(RelaxedElement):
    """RelaxedElement_zero(parent)

    File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 2116)

    A class for representation a relaxed `p`-adic number which is
    exactly zero.

    TESTS::

        sage: R = ZpER(7)
        sage: a = R.zero()
        sage: TestSuite(a).run()"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 2127)

                Initialize this element.

                INPUT:

                - ``parent`` -- the parent of this element

                TESTS::

                    sage: R = ZpER(5)
                    sage: x = R(0)  # indirect doctest
                    sage: x
                    0

                    sage: type(x)
                    <class 'sage.rings.padics.padic_relaxed_element.pAdicRelaxedElement_zero'>
        """
    def __reduce__(self) -> Any:
        """RelaxedElement_zero.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 2148)

        Return a tuple of a function and data that can be used to unpickle this
        element.

        TESTS::

            sage: a = ZpER(5)(0)
            sage: type(a)
            <class 'sage.rings.padics.padic_relaxed_element.pAdicRelaxedElement_zero'>
            sage: loads(dumps(a)) == a   # indirect doctest
            True"""

class RelaxedElement_zeroone(RelaxedElementWithDigits):
    """RelaxedElement_zeroone(parent, long valuation)

    File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 3959)

    A special class for `p`-adic relaxed elements with only
    `0` and `1` as digits.

    This class is used for computing expansion in Teichmuller mode.
    It is not supposed to be instantiated in other situations."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, longvaluation) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/relaxed_template.pxi (starting at line 3967)

                Instantiate this element.

                INPUT:

                - ``parent`` -- the parent of this element

                - ``valuation`` -- the valuation of this number
        """

class pAdicRelaxedElement(RelaxedElement):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class pAdicRelaxedElement_add(RelaxedElement_add):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class pAdicRelaxedElement_bound(RelaxedElement_bound):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class pAdicRelaxedElement_div(RelaxedElement_div):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class pAdicRelaxedElement_mul(RelaxedElement_mul):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class pAdicRelaxedElement_muldigit(RelaxedElement_muldigit):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class pAdicRelaxedElement_one(RelaxedElement_one):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class pAdicRelaxedElement_random(RelaxedElement_random):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class pAdicRelaxedElement_slice(RelaxedElement_slice):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class pAdicRelaxedElement_sqrt(RelaxedElement_sqrt):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class pAdicRelaxedElement_sub(RelaxedElement_sub):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class pAdicRelaxedElement_teichmuller(RelaxedElement_teichmuller):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class pAdicRelaxedElement_unknown(RelaxedElement_unknown):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class pAdicRelaxedElement_value(RelaxedElement_value):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class pAdicRelaxedElement_zero(RelaxedElement_zero):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
