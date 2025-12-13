import _cython_3_2_1
import sage.categories.map
import sage.rings.fraction_field
import sage.rings.morphism
import sage.structure.element
from sage.categories.category import ZZ as ZZ
from sage.rings.fraction_field import FractionField_1poly_field as FractionField_1poly_field
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

unpickle_FpT_element: _cython_3_2_1.cython_function_or_method

class FpT(sage.rings.fraction_field.FractionField_1poly_field):
    """File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 27)

        This class represents the fraction field `\\GF{p}(T)` for `2 < p < \\sqrt{2^31-1}`.

        EXAMPLES::

            sage: R.<T> = GF(71)[]
            sage: K = FractionField(R); K
            Fraction Field of Univariate Polynomial Ring in T over Finite Field of size 71
            sage: 1-1/T
            (T + 70)/T
            sage: parent(1-1/T) is K
            True
    """
    INTEGER_LIMIT: ClassVar[int] = ...
    def __init__(self, R, names=...) -> Any:
        """FpT.__init__(self, R, names=None)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 43)

        INPUT:

        - ``R`` -- a dense polynomial ring over a finite field of prime order
          `p` with `2 < p < 2^{16}`

        EXAMPLES::

            sage: R.<x> = GF(31)[]
            sage: K = R.fraction_field(); K
            Fraction Field of Univariate Polynomial Ring in x over Finite Field of size 31

        TESTS::

            sage: from sage.rings.fraction_field_FpT import FpT
            sage: FpT(PolynomialRing(GF(37), ['x'], sparse=True))
            Traceback (most recent call last):
            ...
            TypeError: unsupported polynomial ring"""
    def iter(self, bound=..., start=...) -> Any:
        """FpT.iter(self, bound=None, start=None)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 85)

        EXAMPLES::

            sage: from sage.rings.fraction_field_FpT import *
            sage: R.<t> = FpT(GF(5)['t'])
            sage: list(R.iter(2))[350:355]
            [(t^2 + t + 1)/(t + 2),
             (t^2 + t + 2)/(t + 2),
             (t^2 + t + 4)/(t + 2),
             (t^2 + 2*t + 1)/(t + 2),
             (t^2 + 2*t + 2)/(t + 2)]"""
    def __iter__(self) -> Any:
        """FpT.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 73)

        Return an iterator over this fraction field.

        EXAMPLES::

            sage: R.<t> = GF(3)[]; K = R.fraction_field()
            sage: iter(K)
            <sage.rings.fraction_field_FpT.FpT_iter object at ...>"""

class FpTElement(sage.structure.element.FieldElement):
    """FpTElement(parent, numer, denom=1, coerce=True, reduce=True)

    File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 101)

    An element of an :class:`FpT` fraction field.

    TESTS::

        sage: R.<t> = GF(5)[]
        sage: K = R.fraction_field()
        sage: A.<x> = K[]
        sage: x.divides(x)  # Testing issue #27064
        True"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, numer, denom=..., coerce=..., reduce=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 114)

                INPUT:

                - ``parent`` -- the Fraction field containing this element
                - ``numer`` -- something that can be converted into the polynomial
                  ring, giving the numerator
                - ``denom`` -- something that can be converted into the polynomial
                  ring, giving the numerator (default: 1)

                EXAMPLES::

                    sage: from sage.rings.fraction_field_FpT import *
                    sage: R.<t> = FpT(GF(5)['t'])
                    sage: R(7)
                    2
        """
    @overload
    def denom(self) -> Any:
        """FpTElement.denom(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 235)

        Return the denominator of this element, as an element of the polynomial ring.

        EXAMPLES::

            sage: K = GF(11)['t'].fraction_field()
            sage: t = K.gen(0); a = (t + 1/t)^3 - 1
            sage: a.denom()
            t^3"""
    @overload
    def denom(self) -> Any:
        """FpTElement.denom(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 235)

        Return the denominator of this element, as an element of the polynomial ring.

        EXAMPLES::

            sage: K = GF(11)['t'].fraction_field()
            sage: t = K.gen(0); a = (t + 1/t)^3 - 1
            sage: a.denom()
            t^3"""
    @overload
    def denominator(self) -> Any:
        """FpTElement.denominator(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 248)

        Return the denominator of this element, as an element of the polynomial ring.

        EXAMPLES::

            sage: K = GF(11)['t'].fraction_field()
            sage: t = K.gen(0); a = (t + 1/t)^3 - 1
            sage: a.denominator()
            t^3"""
    @overload
    def denominator(self) -> Any:
        """FpTElement.denominator(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 248)

        Return the denominator of this element, as an element of the polynomial ring.

        EXAMPLES::

            sage: K = GF(11)['t'].fraction_field()
            sage: t = K.gen(0); a = (t + 1/t)^3 - 1
            sage: a.denominator()
            t^3"""
    @overload
    def factor(self) -> Any:
        """FpTElement.factor(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 317)

        EXAMPLES::

            sage: K = Frac(GF(5)['t'])
            sage: t = K.gen()
            sage: f = 2 * (t+1) * (t^2+t+1)^2 / (t-1)
            sage: factor(f)
            (2) * (t + 4)^-1 * (t + 1) * (t^2 + t + 1)^2"""
    @overload
    def factor(self, f) -> Any:
        """FpTElement.factor(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 317)

        EXAMPLES::

            sage: K = Frac(GF(5)['t'])
            sage: t = K.gen()
            sage: f = 2 * (t+1) * (t^2+t+1)^2 / (t-1)
            sage: factor(f)
            (2) * (t + 4)^-1 * (t + 1) * (t^2 + t + 1)^2"""
    @overload
    def is_square(self) -> bool:
        """FpTElement.is_square(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 782)

        Return ``True`` if this element is the square of another element of the fraction field.

        EXAMPLES::

            sage: K = GF(13)['t'].fraction_field(); t = K.gen()
            sage: t.is_square()
            False
            sage: (1/t^2).is_square()
            True
            sage: K(0).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """FpTElement.is_square(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 782)

        Return ``True`` if this element is the square of another element of the fraction field.

        EXAMPLES::

            sage: K = GF(13)['t'].fraction_field(); t = K.gen()
            sage: t.is_square()
            False
            sage: (1/t^2).is_square()
            True
            sage: K(0).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """FpTElement.is_square(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 782)

        Return ``True`` if this element is the square of another element of the fraction field.

        EXAMPLES::

            sage: K = GF(13)['t'].fraction_field(); t = K.gen()
            sage: t.is_square()
            False
            sage: (1/t^2).is_square()
            True
            sage: K(0).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """FpTElement.is_square(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 782)

        Return ``True`` if this element is the square of another element of the fraction field.

        EXAMPLES::

            sage: K = GF(13)['t'].fraction_field(); t = K.gen()
            sage: t.is_square()
            False
            sage: (1/t^2).is_square()
            True
            sage: K(0).is_square()
            True"""
    @overload
    def next(self) -> FpTElement:
        '''FpTElement.next(self) -> FpTElement

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 604)

        Iterate through all polynomials, returning the "next" polynomial after this one.

        The strategy is as follows:

        - We always leave the denominator monic.

        - We progress through the elements with both numerator and denominator monic, and with the denominator less than the numerator.
          For each such, we output all the scalar multiples of it, then all of the scalar multiples of its inverse.

        - So if the leading coefficient of the numerator is less than `p-1`, we scale the numerator to increase it by 1.

        - Otherwise, we consider the multiple with numerator and denominator monic.

          - If the numerator is less than the denominator (lexicographically), we return the inverse of that element.

          - If the numerator is greater than the denominator, we invert, and then increase the numerator (remaining monic) until we either get something relatively prime to the new denominator, or we reach the new denominator.  In this case, we increase the denominator and set the numerator to 1.

        EXAMPLES::

            sage: from sage.rings.fraction_field_FpT import *
            sage: R.<t> = FpT(GF(3)[\'t\'])
            sage: a = R(0)
            sage: for _ in range(30):
            ....:     a = a.next()
            ....:     print(a)
            1
            2
            1/t
            2/t
            t
            2*t
            1/(t + 1)
            2/(t + 1)
            t + 1
            2*t + 2
            t/(t + 1)
            2*t/(t + 1)
            (t + 1)/t
            (2*t + 2)/t
            1/(t + 2)
            2/(t + 2)
            t + 2
            2*t + 1
            t/(t + 2)
            2*t/(t + 2)
            (t + 2)/t
            (2*t + 1)/t
            (t + 1)/(t + 2)
            (2*t + 2)/(t + 2)
            (t + 2)/(t + 1)
            (2*t + 1)/(t + 1)
            1/t^2
            2/t^2
            t^2
            2*t^2'''
    @overload
    def next(self) -> Any:
        '''FpTElement.next(self) -> FpTElement

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 604)

        Iterate through all polynomials, returning the "next" polynomial after this one.

        The strategy is as follows:

        - We always leave the denominator monic.

        - We progress through the elements with both numerator and denominator monic, and with the denominator less than the numerator.
          For each such, we output all the scalar multiples of it, then all of the scalar multiples of its inverse.

        - So if the leading coefficient of the numerator is less than `p-1`, we scale the numerator to increase it by 1.

        - Otherwise, we consider the multiple with numerator and denominator monic.

          - If the numerator is less than the denominator (lexicographically), we return the inverse of that element.

          - If the numerator is greater than the denominator, we invert, and then increase the numerator (remaining monic) until we either get something relatively prime to the new denominator, or we reach the new denominator.  In this case, we increase the denominator and set the numerator to 1.

        EXAMPLES::

            sage: from sage.rings.fraction_field_FpT import *
            sage: R.<t> = FpT(GF(3)[\'t\'])
            sage: a = R(0)
            sage: for _ in range(30):
            ....:     a = a.next()
            ....:     print(a)
            1
            2
            1/t
            2/t
            t
            2*t
            1/(t + 1)
            2/(t + 1)
            t + 1
            2*t + 2
            t/(t + 1)
            2*t/(t + 1)
            (t + 1)/t
            (2*t + 2)/t
            1/(t + 2)
            2/(t + 2)
            t + 2
            2*t + 1
            t/(t + 2)
            2*t/(t + 2)
            (t + 2)/t
            (2*t + 1)/t
            (t + 1)/(t + 2)
            (2*t + 2)/(t + 2)
            (t + 2)/(t + 1)
            (2*t + 1)/(t + 1)
            1/t^2
            2/t^2
            t^2
            2*t^2'''
    @overload
    def numer(self) -> Any:
        """FpTElement.numer(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 204)

        Return the numerator of this element, as an element of the polynomial ring.

        EXAMPLES::

            sage: K = GF(11)['t'].fraction_field()
            sage: t = K.gen(0); a = (t + 1/t)^3 - 1
            sage: a.numer()
            t^6 + 3*t^4 + 10*t^3 + 3*t^2 + 1"""
    @overload
    def numer(self) -> Any:
        """FpTElement.numer(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 204)

        Return the numerator of this element, as an element of the polynomial ring.

        EXAMPLES::

            sage: K = GF(11)['t'].fraction_field()
            sage: t = K.gen(0); a = (t + 1/t)^3 - 1
            sage: a.numer()
            t^6 + 3*t^4 + 10*t^3 + 3*t^2 + 1"""
    @overload
    def numerator(self) -> Any:
        """FpTElement.numerator(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 217)

        Return the numerator of this element, as an element of the polynomial ring.

        EXAMPLES::

            sage: K = GF(11)['t'].fraction_field()
            sage: t = K.gen(0); a = (t + 1/t)^3 - 1
            sage: a.numerator()
            t^6 + 3*t^4 + 10*t^3 + 3*t^2 + 1"""
    @overload
    def numerator(self) -> Any:
        """FpTElement.numerator(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 217)

        Return the numerator of this element, as an element of the polynomial ring.

        EXAMPLES::

            sage: K = GF(11)['t'].fraction_field()
            sage: t = K.gen(0); a = (t + 1/t)^3 - 1
            sage: a.numerator()
            t^6 + 3*t^4 + 10*t^3 + 3*t^2 + 1"""
    @overload
    def sqrt(self, extend=..., all=...) -> Any:
        """FpTElement.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 798)

        Return the square root of this element.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square is not in the base ring.

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of self, instead of just one

        EXAMPLES::

            sage: from sage.rings.fraction_field_FpT import *
            sage: K = GF(7)['t'].fraction_field(); t = K.gen(0)
            sage: p = (t + 2)^2/(3*t^3 + 1)^4
            sage: p.sqrt()
            (3*t + 6)/(t^6 + 3*t^3 + 4)
            sage: p.sqrt()^2 == p
            True"""
    @overload
    def sqrt(self) -> Any:
        """FpTElement.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 798)

        Return the square root of this element.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square is not in the base ring.

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of self, instead of just one

        EXAMPLES::

            sage: from sage.rings.fraction_field_FpT import *
            sage: K = GF(7)['t'].fraction_field(); t = K.gen(0)
            sage: p = (t + 2)^2/(3*t^3 + 1)^4
            sage: p.sqrt()
            (3*t + 6)/(t^6 + 3*t^3 + 4)
            sage: p.sqrt()^2 == p
            True"""
    @overload
    def sqrt(self) -> Any:
        """FpTElement.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 798)

        Return the square root of this element.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square is not in the base ring.

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of self, instead of just one

        EXAMPLES::

            sage: from sage.rings.fraction_field_FpT import *
            sage: K = GF(7)['t'].fraction_field(); t = K.gen(0)
            sage: p = (t + 2)^2/(3*t^3 + 1)^4
            sage: p.sqrt()
            (3*t + 6)/(t^6 + 3*t^3 + 4)
            sage: p.sqrt()^2 == p
            True"""
    @overload
    def subs(self, in_dict=..., *args, **kwds) -> Any:
        """FpTElement.subs(self, in_dict=None, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 286)

        EXAMPLES::

            sage: K = Frac(GF(11)['t'])
            sage: t = K.gen()
            sage: f = (t+1)/(t-1)
            sage: f.subs(t=2)
            3
            sage: f.subs(X=2)
            (t + 1)/(t + 10)"""
    @overload
    def subs(self, t=...) -> Any:
        """FpTElement.subs(self, in_dict=None, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 286)

        EXAMPLES::

            sage: K = Frac(GF(11)['t'])
            sage: t = K.gen()
            sage: f = (t+1)/(t-1)
            sage: f.subs(t=2)
            3
            sage: f.subs(X=2)
            (t + 1)/(t + 10)"""
    @overload
    def subs(self, X=...) -> Any:
        """FpTElement.subs(self, in_dict=None, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 286)

        EXAMPLES::

            sage: K = Frac(GF(11)['t'])
            sage: t = K.gen()
            sage: f = (t+1)/(t-1)
            sage: f.subs(t=2)
            3
            sage: f.subs(X=2)
            (t + 1)/(t + 10)"""
    @overload
    def valuation(self, v) -> Any:
        """FpTElement.valuation(self, v)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 300)

        Return the valuation of ``self`` at `v`.

        EXAMPLES::

            sage: R.<t> = GF(5)[]
            sage: f = (t+1)^2 * (t^2+t+1) / (t-1)^3
            sage: f.valuation(t+1)
            2
            sage: f.valuation(t-1)
            -3
            sage: f.valuation(t)
            0"""
    @overload
    def valuation(self, t) -> Any:
        """FpTElement.valuation(self, v)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 300)

        Return the valuation of ``self`` at `v`.

        EXAMPLES::

            sage: R.<t> = GF(5)[]
            sage: f = (t+1)^2 * (t^2+t+1) / (t-1)^3
            sage: f.valuation(t+1)
            2
            sage: f.valuation(t-1)
            -3
            sage: f.valuation(t)
            0"""
    def __call__(self, *args, **kwds) -> Any:
        """FpTElement.__call__(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 266)

        EXAMPLES::

            sage: K = Frac(GF(5)['t'])
            sage: t = K.gen()
            sage: t(3)
            3
            sage: f = t^2/(1-t)
            sage: f(2)
            1
            sage: f(t)
            4*t^2/(t + 4)
            sage: f(t^3)
            4*t^6/(t^3 + 4)
            sage: f((t+1)/t^3)
            (t^2 + 2*t + 1)/(t^6 + 4*t^4 + 4*t^3)"""
    def __hash__(self) -> Any:
        """FpTElement.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 428)

        Return a hash value for this element.

        TESTS::

            sage: from sage.rings.fraction_field_FpT import *
            sage: K.<t> = FpT(GF(7)['t'])
            sage: hash(K(0))
            0
            sage: hash(K(5))
            5
            sage: set([1, t, 1/t, t, t, 1/t, 1+1/t, t/t])
            {1, 1/t, t, (t + 1)/t}
            sage: a = (t+1)/(t^2-1); hash(a) == hash((a.numer(),a.denom()))
            True"""
    def __invert__(self) -> Any:
        """FpTElement.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 464)

        Return the multiplicative inverse of this element.

        EXAMPLES::

            sage: K = GF(5)['t'].fraction_field(); t = K.gen(0)
            sage: a = (t^2 + 2)/(t-1)
            sage: ~a # indirect doctest
            (t + 4)/(t^2 + 2)"""
    def __neg__(self) -> Any:
        """FpTElement.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 449)

        Negate this element.

        EXAMPLES::

            sage: K = GF(5)['t'].fraction_field(); t = K.gen(0)
            sage: a = (t^2 + 2)/(t-1)
            sage: -a # indirect doctest
            (4*t^2 + 3)/(t + 4)"""
    def __pow__(self, FpTElementself, Py_ssize_te, dummy) -> Any:
        """FpTElement.__pow__(FpTElement self, Py_ssize_t e, dummy)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 836)

        Return the `e`-th power of this element.

        EXAMPLES::

            sage: from sage.rings.fraction_field_FpT import *
            sage: R.<t> = FpT(GF(7)['t'])
            sage: t^5
            t^5
            sage: t^-5
            1/t^5

            sage: a = (t+1)/(t-1); a
            (t + 1)/(t + 6)
            sage: a^5
            (t^5 + 5*t^4 + 3*t^3 + 3*t^2 + 5*t + 1)/(t^5 + 2*t^4 + 3*t^3 + 4*t^2 + 5*t + 6)
            sage: a^7
            (t^7 + 1)/(t^7 + 6)
            sage: a^14
            (t^14 + 2*t^7 + 1)/(t^14 + 5*t^7 + 1)

            sage: (a^2)^2 == a^4
            True
            sage: a^3 * a^2 == a^5
            True
            sage: a^47 * a^92 == a^(47+92)
            True"""
    def __reduce__(self) -> Any:
        """FpTElement.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 161)

        For pickling.

        TESTS::

            sage: K = GF(11)['t'].fraction_field()
            sage: loads(dumps(K.gen()))
            t
            sage: loads(dumps(1/K.gen()))
            1/t"""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""

class FpT_Fp_section(sage.categories.map.Section):
    """FpT_Fp_section(Fp_FpT_coerce f)

    File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 1552)

    This class represents the section from GF(p)(t) back to GF(p)[t].

    EXAMPLES::

        sage: R.<t> = GF(5)[]
        sage: K = R.fraction_field()
        sage: f = GF(5).convert_map_from(K); f
        Section map:
          From: Fraction Field of Univariate Polynomial Ring in t over Finite Field of size 5
          To:   Finite Field of size 5
        sage: type(f)
        <class 'sage.rings.fraction_field_FpT.FpT_Fp_section'>

    .. WARNING::

        Comparison of ``FpT_Fp_section`` objects is not currently
        implemented. See :issue:`23469`. ::

            sage: fprime = loads(dumps(f))
            sage: fprime == f
            False

            sage: fprime(3) == f(3)
            True

    TESTS::

        sage: TestSuite(f).run(skip='_test_pickling')"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, Fp_FpT_coercef) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 1585)

                INPUT:

                - ``f`` -- an ``Fp_FpT_coerce`` homomorphism

                EXAMPLES::

                    sage: R.<t> = GF(next_prime(2000))[]
                    sage: K = R.fraction_field()
                    sage: GF(next_prime(2000))(K(127)) # indirect doctest
                    127
        """

class FpT_Polyring_section(sage.categories.map.Section):
    """FpT_Polyring_section(Polyring_FpT_coerce f)

    File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 1252)

    This class represents the section from GF(p)(t) back to GF(p)[t].

    EXAMPLES::

        sage: R.<t> = GF(5)[]
        sage: K = R.fraction_field()
        sage: f = R.convert_map_from(K); f
        Section map:
          From: Fraction Field of Univariate Polynomial Ring in t over Finite Field of size 5
          To:   Univariate Polynomial Ring in t over Finite Field of size 5
        sage: type(f)
        <class 'sage.rings.fraction_field_FpT.FpT_Polyring_section'>

    .. WARNING::

        Comparison of ``FpT_Polyring_section`` objects is not currently
        implemented. See :issue:`23469`. ::

            sage: fprime = loads(dumps(f))
            sage: fprime == f
            False

            sage: fprime(1+t) == f(1+t)
            True

    TESTS::

        sage: TestSuite(f).run(skip='_test_pickling')"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, Polyring_FpT_coercef) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 1285)

                INPUT:

                - ``f`` -- a Polyring_FpT_coerce homomorphism

                EXAMPLES::

                    sage: R.<t> = GF(next_prime(2000))[]
                    sage: K = R.fraction_field()
                    sage: R(K.gen(0)) # indirect doctest
                    t
        """

class FpT_iter:
    """FpT_iter(parent, degree=None, FpTElement start=None)

    File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 881)

    Return a class that iterates over all elements of an FpT.

    EXAMPLES::

        sage: K = GF(3)['t'].fraction_field()
        sage: I = K.iter(1)
        sage: list(I)
        [0,
         1,
         2,
         t,
         t + 1,
         t + 2,
         2*t,
         2*t + 1,
         2*t + 2,
         1/t,
         2/t,
         (t + 1)/t,
         (t + 2)/t,
         (2*t + 1)/t,
         (2*t + 2)/t,
         1/(t + 1),
         2/(t + 1),
         t/(t + 1),
         (t + 2)/(t + 1),
         2*t/(t + 1),
         (2*t + 1)/(t + 1),
         1/(t + 2),
         2/(t + 2),
         t/(t + 2),
         (t + 1)/(t + 2),
         2*t/(t + 2),
         (2*t + 2)/(t + 2)]"""
    def __init__(self, parent, degree=..., FpTElementstart=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 918)

                INPUT:

                - ``parent`` -- the FpT that we're iterating over

                - ``degree`` -- the maximum degree of the numerator and denominator of
                  the elements over which we iterate

                - ``start`` -- (default: 0) the element on which to start

                EXAMPLES::

                    sage: K = GF(11)['t'].fraction_field()
                    sage: I = K.iter(2) # indirect doctest
                    sage: for a in I:
                    ....:     if a.denom()[0] == 3 and a.numer()[1] == 2:
                    ....:         print(a); break
                    2*t/(t + 3)
        """
    def __iter__(self) -> Any:
        """FpT_iter.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 971)

        Return this iterator.

        TESTS::

            sage: from sage.rings.fraction_field_FpT import FpT_iter
            sage: K = GF(3)['t'].fraction_field()
            sage: I = FpT_iter(K, 3)
            sage: for a in I: # indirect doctest
            ....:     if a.numer()[1] == 1 and a.denom()[1] == 2 and a.is_square():
            ....:          print(a); break
            (t^2 + t + 1)/(t^2 + 2*t + 1)"""
    def __next__(self) -> Any:
        """FpT_iter.__next__(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 987)

        Return the next element to iterate over.

        This is achieved by iterating over monic denominators, and for each denominator,
        iterating over all numerators relatively prime to the given denominator.

        EXAMPLES::

            sage: from sage.rings.fraction_field_FpT import *
            sage: K.<t> = FpT(GF(3)['t'])
            sage: list(K.iter(1)) # indirect doctest
            [0,
             1,
             2,
             t,
             t + 1,
             t + 2,
             2*t,
             2*t + 1,
             2*t + 2,
             1/t,
             2/t,
             (t + 1)/t,
             (t + 2)/t,
             (2*t + 1)/t,
             (2*t + 2)/t,
             1/(t + 1),
             2/(t + 1),
             t/(t + 1),
             (t + 2)/(t + 1),
             2*t/(t + 1),
             (2*t + 1)/(t + 1),
             1/(t + 2),
             2/(t + 2),
             t/(t + 2),
             (t + 1)/(t + 2),
             2*t/(t + 2),
             (2*t + 2)/(t + 2)]

            sage: len(list(K.iter(3)))
            2187

            sage: K.<t> = FpT(GF(5)['t'])
            sage: L = list(K.iter(3)); len(L)
            78125
            sage: L[:10]
            [0, 1, 2, 3, 4, t, t + 1, t + 2, t + 3, t + 4]
            sage: L[2000]
            (3*t^3 + 3*t^2 + 3*t + 4)/(t + 2)
            sage: L[-1]
            (4*t^3 + 4*t^2 + 4*t + 4)/(t^3 + 4*t^2 + 4*t + 4)"""

class Fp_FpT_coerce(sage.rings.morphism.RingHomomorphism):
    """Fp_FpT_coerce(R)

    File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 1380)

    This class represents the coercion map from GF(p) to GF(p)(t).

    EXAMPLES::

        sage: R.<t> = GF(5)[]
        sage: K = R.fraction_field()
        sage: f = K.coerce_map_from(GF(5)); f
        Ring morphism:
          From: Finite Field of size 5
          To:   Fraction Field of Univariate Polynomial Ring in t over Finite Field of size 5
        sage: type(f)
        <class 'sage.rings.fraction_field_FpT.Fp_FpT_coerce'>

    TESTS::

        sage: TestSuite(f).run()"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, R) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 1401)

                INPUT:

                - ``R`` -- an FpT

                EXAMPLES::

                    sage: R.<t> = GF(next_prime(3000))[]
                    sage: K = R.fraction_field() # indirect doctest
        """
    @overload
    def section(self) -> Any:
        """Fp_FpT_coerce.section(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 1524)

        Return the section of this inclusion: the partially defined map from ``GF(p)(t)``
        back to ``GF(p)``, defined on constant elements.

        EXAMPLES::

            sage: R.<t> = GF(5)[]
            sage: K = R.fraction_field()
            sage: f = K.coerce_map_from(GF(5))
            sage: g = f.section(); g
            Section map:
              From: Fraction Field of Univariate Polynomial Ring in t over Finite Field of size 5
              To:   Finite Field of size 5
            sage: t = K.gen()
            sage: g(f(1,3,reduce=False))
            2
            sage: g(t)
            Traceback (most recent call last):
            ...
            ValueError: not constant
            sage: g(1/t)
            Traceback (most recent call last):
            ...
            ValueError: not integral"""
    @overload
    def section(self) -> Any:
        """Fp_FpT_coerce.section(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 1524)

        Return the section of this inclusion: the partially defined map from ``GF(p)(t)``
        back to ``GF(p)``, defined on constant elements.

        EXAMPLES::

            sage: R.<t> = GF(5)[]
            sage: K = R.fraction_field()
            sage: f = K.coerce_map_from(GF(5))
            sage: g = f.section(); g
            Section map:
              From: Fraction Field of Univariate Polynomial Ring in t over Finite Field of size 5
              To:   Finite Field of size 5
            sage: t = K.gen()
            sage: g(f(1,3,reduce=False))
            2
            sage: g(t)
            Traceback (most recent call last):
            ...
            ValueError: not constant
            sage: g(1/t)
            Traceback (most recent call last):
            ...
            ValueError: not integral"""

class Polyring_FpT_coerce(sage.rings.morphism.RingHomomorphism):
    """Polyring_FpT_coerce(R)

    File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 1064)

    This class represents the coercion map from GF(p)[t] to GF(p)(t).

    EXAMPLES::

        sage: R.<t> = GF(5)[]
        sage: K = R.fraction_field()
        sage: f = K.coerce_map_from(R); f
        Ring morphism:
          From: Univariate Polynomial Ring in t over Finite Field of size 5
          To:   Fraction Field of Univariate Polynomial Ring in t over Finite Field of size 5
        sage: type(f)
        <class 'sage.rings.fraction_field_FpT.Polyring_FpT_coerce'>

    TESTS::

        TestSuite(f).run()"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, R) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 1085)

                INPUT:

                - ``R`` -- an FpT

                EXAMPLES::

                    sage: R.<t> = GF(next_prime(2000))[]
                    sage: K = R.fraction_field() # indirect doctest
        """
    @overload
    def section(self) -> Any:
        """Polyring_FpT_coerce.section(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 1228)

        Return the section of this inclusion: the partially defined map from ``GF(p)(t)``
        back to ``GF(p)[t]``, defined on elements with unit denominator.

        EXAMPLES::

            sage: R.<t> = GF(5)[]
            sage: K = R.fraction_field()
            sage: f = K.coerce_map_from(R)
            sage: g = f.section(); g
            Section map:
              From: Fraction Field of Univariate Polynomial Ring in t over Finite Field of size 5
              To:   Univariate Polynomial Ring in t over Finite Field of size 5
            sage: t = K.gen()
            sage: g(t)
            t
            sage: g(1/t)
            Traceback (most recent call last):
            ...
            ValueError: not integral"""
    @overload
    def section(self) -> Any:
        """Polyring_FpT_coerce.section(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 1228)

        Return the section of this inclusion: the partially defined map from ``GF(p)(t)``
        back to ``GF(p)[t]``, defined on elements with unit denominator.

        EXAMPLES::

            sage: R.<t> = GF(5)[]
            sage: K = R.fraction_field()
            sage: f = K.coerce_map_from(R)
            sage: g = f.section(); g
            Section map:
              From: Fraction Field of Univariate Polynomial Ring in t over Finite Field of size 5
              To:   Univariate Polynomial Ring in t over Finite Field of size 5
            sage: t = K.gen()
            sage: g(t)
            t
            sage: g(1/t)
            Traceback (most recent call last):
            ...
            ValueError: not integral"""

class ZZ_FpT_coerce(sage.rings.morphism.RingHomomorphism):
    """ZZ_FpT_coerce(R)

    File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 1699)

    This class represents the coercion map from ZZ to GF(p)(t).

    EXAMPLES::

        sage: R.<t> = GF(17)[]
        sage: K = R.fraction_field()
        sage: f = K.coerce_map_from(ZZ); f
        Ring morphism:
          From: Integer Ring
          To:   Fraction Field of Univariate Polynomial Ring in t over Finite Field of size 17
        sage: type(f)
        <class 'sage.rings.fraction_field_FpT.ZZ_FpT_coerce'>

    TESTS::

        sage: TestSuite(f).run()"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, R) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 1720)

                INPUT:

                - ``R`` -- an FpT

                EXAMPLES::

                    sage: R.<t> = GF(next_prime(3000))[]
                    sage: K = R.fraction_field() # indirect doctest
        """
    def section(self, *args, **kwargs):
        """ZZ_FpT_coerce.section(self)

        File: /build/sagemath/src/sage/src/sage/rings/fraction_field_FpT.pyx (starting at line 1849)

        Return the section of this inclusion: the partially defined map from ``GF(p)(t)``
        back to ``ZZ``, defined on constant elements.

        EXAMPLES::

            sage: R.<t> = GF(5)[]
            sage: K = R.fraction_field()
            sage: f = K.coerce_map_from(ZZ)
            sage: g = f.section(); g
            Composite map:
              From: Fraction Field of Univariate Polynomial Ring in t over Finite Field of size 5
              To:   Integer Ring
              Defn:   Section map:
                      From: Fraction Field of Univariate Polynomial Ring in t over Finite Field of size 5
                      To:   Finite Field of size 5
                    then
                      Lifting map:
                      From: Finite Field of size 5
                      To:   Integer Ring
            sage: t = K.gen()
            sage: g(f(1,3,reduce=False))
            2
            sage: g(t)
            Traceback (most recent call last):
            ...
            ValueError: not constant
            sage: g(1/t)
            Traceback (most recent call last):
            ...
            ValueError: not integral"""
