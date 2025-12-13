import _cython_3_2_1
import sage.rings.polynomial.polynomial_element
from sage.libs.ntl.ntl_lzz_pX import ntl_zz_pX as ntl_zz_pX
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.superseded import deprecated_function_alias as deprecated_function_alias
from sage.rings.fraction_field_element import FractionFieldElement as FractionFieldElement
from sage.structure.element import canonical_coercion as canonical_coercion, coerce_binop as coerce_binop, have_same_parent as have_same_parent, parent as parent
from sage.structure.factorization import Factorization as Factorization
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

__pyx_capi__: dict
make_element: _cython_3_2_1.cython_function_or_method

class Polynomial_template(sage.rings.polynomial.polynomial_element.Polynomial):
    """Polynomial_template(parent, x=None, check=True, is_gen=False, construct=False)

    File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 60)

    Template for interfacing to external C / C++ libraries for implementations of polynomials.

    AUTHORS:

    - Robert Bradshaw (2008-10): original idea for templating
    - Martin Albrecht (2008-10): initial implementation

    This file implements a simple templating engine for linking univariate
    polynomials to their C/C++ library implementations. It requires a
    'linkage' file which implements the ``celement_`` functions (see
    :mod:`sage.libs.ntl.ntl_GF2X_linkage` for an example). Both parts are
    then plugged together by inclusion of the linkage file when inheriting from
    this class. See :mod:`sage.rings.polynomial.polynomial_gf2x` for an
    example.

    We illustrate the generic glueing using univariate polynomials over
    `\\mathop{\\mathrm{GF}}(2)`.

    .. NOTE::

        Implementations using this template MUST implement coercion from base
        ring elements and :meth:`get_unsafe`. See
        :class:`~sage.rings.polynomial.polynomial_gf2x.Polynomial_GF2X` for an
        example."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, x=..., check=..., is_gen=..., construct=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 87)

                EXAMPLES::

                    sage: P.<x> = GF(2)[]
                    sage: P(0)
                    0
                    sage: P(GF(2)(1))
                    1
                    sage: P(3)
                    1
                    sage: P([1,0,1])
                    x^2 + 1
                    sage: P(list(map(GF(2),[1,0,1])))
                    x^2 + 1
        """
    @overload
    def degree(self) -> Any:
        """Polynomial_template.degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 768)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: x.degree()
            1
            sage: P(1).degree()
            0
            sage: P(0).degree()
            -1"""
    @overload
    def degree(self) -> Any:
        """Polynomial_template.degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 768)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: x.degree()
            1
            sage: P(1).degree()
            0
            sage: P(0).degree()
            -1"""
    @overload
    def degree(self) -> Any:
        """Polynomial_template.degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 768)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: x.degree()
            1
            sage: P(1).degree()
            0
            sage: P(0).degree()
            -1"""
    @overload
    def degree(self) -> Any:
        """Polynomial_template.degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 768)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: x.degree()
            1
            sage: P(1).degree()
            0
            sage: P(0).degree()
            -1"""
    @overload
    def gcd(self, Polynomial_templateother) -> Any:
        """Polynomial_template.gcd(self, Polynomial_template other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 342)

        Return the greatest common divisor of ``self`` and ``other``.

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: f = x*(x+1)
            sage: f.gcd(x+1)
            x + 1
            sage: f.gcd(x^2)
            x

        TESTS:

        Ensure non-invertible elements does not crash Sage (:issue:`37317`)::

            sage: R.<x> = Zmod(4)[]
            sage: f = R(2 * x)
            sage: f.gcd(f)
            Traceback (most recent call last):
            ...
            ValueError: leading coefficient must be invertible

        ::

            sage: f = x^2 + 3 * x + 1
            sage: g = x^2 + x + 1
            sage: f.gcd(g)
            Traceback (most recent call last):
            ...
            RuntimeError: FLINT gcd calculation failed"""
    @overload
    def gcd(self, f) -> Any:
        """Polynomial_template.gcd(self, Polynomial_template other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 342)

        Return the greatest common divisor of ``self`` and ``other``.

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: f = x*(x+1)
            sage: f.gcd(x+1)
            x + 1
            sage: f.gcd(x^2)
            x

        TESTS:

        Ensure non-invertible elements does not crash Sage (:issue:`37317`)::

            sage: R.<x> = Zmod(4)[]
            sage: f = R(2 * x)
            sage: f.gcd(f)
            Traceback (most recent call last):
            ...
            ValueError: leading coefficient must be invertible

        ::

            sage: f = x^2 + 3 * x + 1
            sage: g = x^2 + x + 1
            sage: f.gcd(g)
            Traceback (most recent call last):
            ...
            RuntimeError: FLINT gcd calculation failed"""
    @overload
    def gcd(self, g) -> Any:
        """Polynomial_template.gcd(self, Polynomial_template other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 342)

        Return the greatest common divisor of ``self`` and ``other``.

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: f = x*(x+1)
            sage: f.gcd(x+1)
            x + 1
            sage: f.gcd(x^2)
            x

        TESTS:

        Ensure non-invertible elements does not crash Sage (:issue:`37317`)::

            sage: R.<x> = Zmod(4)[]
            sage: f = R(2 * x)
            sage: f.gcd(f)
            Traceback (most recent call last):
            ...
            ValueError: leading coefficient must be invertible

        ::

            sage: f = x^2 + 3 * x + 1
            sage: g = x^2 + x + 1
            sage: f.gcd(g)
            Traceback (most recent call last):
            ...
            RuntimeError: FLINT gcd calculation failed"""
    def get_cparent(self) -> Any:
        """Polynomial_template.get_cparent(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 179)"""
    @overload
    def is_gen(self) -> Any:
        """Polynomial_template.is_gen(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 692)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: x.is_gen()
            True
            sage: (x+1).is_gen()
            False"""
    @overload
    def is_gen(self) -> Any:
        """Polynomial_template.is_gen(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 692)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: x.is_gen()
            True
            sage: (x+1).is_gen()
            False"""
    @overload
    def is_gen(self) -> Any:
        """Polynomial_template.is_gen(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 692)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: x.is_gen()
            True
            sage: (x+1).is_gen()
            False"""
    @overload
    def is_one(self) -> bool:
        """Polynomial_template.is_one(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 758)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: P(1).is_one()
            True"""
    @overload
    def is_one(self) -> Any:
        """Polynomial_template.is_one(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 758)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: P(1).is_one()
            True"""
    @overload
    def is_zero(self) -> bool:
        """Polynomial_template.is_zero(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 748)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: x.is_zero()
            False"""
    @overload
    def is_zero(self) -> Any:
        """Polynomial_template.is_zero(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 748)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: x.is_zero()
            False"""
    @overload
    def list(self, boolcopy=...) -> list:
        """Polynomial_template.list(self, bool copy=True) -> list

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 192)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: x.list()
            [0, 1]
            sage: list(x)
            [0, 1]"""
    @overload
    def list(self) -> Any:
        """Polynomial_template.list(self, bool copy=True) -> list

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 192)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: x.list()
            [0, 1]
            sage: list(x)
            [0, 1]"""
    @overload
    def list(self, x) -> Any:
        """Polynomial_template.list(self, bool copy=True) -> list

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 192)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: x.list()
            [0, 1]
            sage: list(x)
            [0, 1]"""
    def quo_rem(self, Polynomial_templateright) -> Any:
        """Polynomial_template.quo_rem(self, Polynomial_template right)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 501)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: f = x^2 + x + 1
            sage: f.quo_rem(x + 1)
            (x, 1)"""
    def shift(self, intn) -> Any:
        """Polynomial_template.shift(self, int n)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 708)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: f = x^3 + x^2 + 1
            sage: f.shift(1)
            x^4 + x^3 + x
            sage: f.shift(-1)
            x^2 + x"""
    def truncate(self, longn) -> Polynomial:
        """Polynomial_template.truncate(self, long n) -> Polynomial

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 782)

        Return this polynomial mod `x^n`.

        EXAMPLES::

            sage: R.<x> =GF(2)[]
            sage: f = sum(x^n for n in range(10)); f
            x^9 + x^8 + x^7 + x^6 + x^5 + x^4 + x^3 + x^2 + x + 1
            sage: f.truncate(6)
            x^5 + x^4 + x^3 + x^2 + x + 1

        If the precision is higher than the degree of the polynomial then
        the polynomial itself is returned::

            sage: f.truncate(10) is f
            True

        If the precision is negative, the zero polynomial is returned::

            sage: f.truncate(-1)
            0"""
    def xgcd(self, Polynomial_templateother) -> Any:
        """Polynomial_template.xgcd(self, Polynomial_template other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 394)

        Compute extended gcd of ``self`` and ``other``.

        EXAMPLES::

            sage: P.<x> = GF(7)[]
            sage: f = x*(x+1)
            sage: f.xgcd(x+1)
            (x + 1, 0, 1)
            sage: f.xgcd(x^2)
            (x, 1, 6)"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __copy__(self) -> Any:
        """Polynomial_template.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 674)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: copy(x) is x
            False
            sage: copy(x) == x
            True"""
    def __hash__(self) -> Any:
        """Polynomial_template.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 556)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: {x:1}
            {x: 1}"""
    def __lshift__(self, intn) -> Any:
        """Polynomial_template.__lshift__(self, int n)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 721)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: f = x^3 + x^2 + 1
            sage: f << 1
            x^4 + x^3 + x
            sage: f << -1
            x^2 + x"""
    def __neg__(self) -> Any:
        """Polynomial_template.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 262)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: -x
            x"""
    def __pow__(self, ee, modulus) -> Any:
        """Polynomial_template.__pow__(self, ee, modulus)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 591)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: x^1000
            x^1000
            sage: (x+1)^2
            x^2 + 1
            sage: (x+1)^(-2)
            1/(x^2 + 1)
            sage: f = x^9 + x^7 + x^6 + x^5 + x^4 + x^2 + x
            sage: h = x^10 + x^7 + x^6 + x^5 + x^4 + x^3 + x^2 + 1
            sage: (f^2) % h
            x^9 + x^8 + x^7 + x^5 + x^3
            sage: pow(f, 2, h)
            x^9 + x^8 + x^7 + x^5 + x^3

        TESTS:

        Ensure modulo `0` and modulo `1` does not crash (:issue:`37169`)::

            sage: R.<x> = GF(2)[]
            sage: pow(x + 1, 2, R.zero())
            Traceback (most recent call last):
            ...
            ZeroDivisionError: modulus must be nonzero
            sage: pow(x + 1, 2, R.one())
            0

        ::

            sage: R.<x> = GF(2^8)[]
            sage: pow(x + 1, 2, R.zero())
            Traceback (most recent call last):
            ...
            ZeroDivisionError: modulus must be nonzero
            sage: pow(x + 1, 2, R.one())
            0"""
    def __reduce__(self) -> Any:
        """Polynomial_template.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 182)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: loads(dumps(x)) == x
            True"""
    def __rlshift__(self, other):
        """Return value<<self."""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
    def __rrshift__(self, other):
        """Return value>>self."""
    def __rshift__(self, intn) -> Any:
        """Polynomial_template.__rshift__(self, int n)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_template.pxi (starting at line 734)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: x>>1
            1
            sage: (x^2 + x)>>1
            x + 1
            sage: (x^2 + x) >> -1
            x^3 + x^2"""

class Polynomial_zmod_flint(Polynomial_template):
    """Polynomial_zmod_flint(parent, x=None, check=True, is_gen=False, construct=False)

    File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 71)

    Polynomial on `\\ZZ/n\\ZZ` implemented via FLINT.

    TESTS::

        sage: f = Integers(4)['x'].random_element()
        sage: from sage.rings.polynomial.polynomial_zmod_flint import Polynomial_zmod_flint
        sage: isinstance(f, Polynomial_zmod_flint)
        True

    .. automethod:: _add_
    .. automethod:: _sub_
    .. automethod:: _lmul_
    .. automethod:: _rmul_
    .. automethod:: _mul_
    .. automethod:: _mul_trunc_"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, x=..., check=..., is_gen=..., construct=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 89)

                EXAMPLES::

                    sage: P.<x> = GF(32003)[]
                    sage: f = 24998*x^2 + 29761*x + 2252
        """
    def compose_mod(self, other, modulus) -> Any:
        """Polynomial_zmod_flint.compose_mod(self, other, modulus)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 1013)

        Compute `f(g) \\bmod h`.

        To be precise about the order fo compostion, given ``self``, ``other``
        and ``modulus`` as `f(x)`, `g(x)` and `h(x)` compute `f(g(x)) \\bmod h(x)`.

        INPUT:

        - ``other`` -- a polynomial `g(x)`
        - ``modulus`` -- a polynomial `h(x)`

        EXAMPLES::

            sage: R.<x> = GF(163)[]
            sage: f = R.random_element()
            sage: g = R.random_element()
            sage: g.compose_mod(g, f) == g(g) % f
            True

            sage: f = R([i for i in range(100)])
            sage: g = R([i**2 for i in range(100)])
            sage: h = 1 + x + x**5
            sage: f.compose_mod(g, h)
            82*x^4 + 56*x^3 + 45*x^2 + 60*x + 127
            sage: f.compose_mod(g, h) == f(g) % h
            True

        AUTHORS:

        - Giacomo Pope (2024-08) initial implementation"""
    @overload
    def factor(self) -> Any:
        '''Polynomial_zmod_flint.factor(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 782)

        Return the factorization of the polynomial.

        EXAMPLES::

            sage: R.<x> = GF(5)[]
            sage: (x^2 + 1).factor()
            (x + 2) * (x + 3)

        It also works for prime-power moduli::

            sage: R.<x> = Zmod(23^5)[]
            sage: (x^3 + 1).factor()
            (x + 1) * (x^2 + 6436342*x + 1)

        TESTS::

            sage: R.<x> = GF(5)[]
            sage: (2*x^2 + 2).factor()
            (2) * (x + 2) * (x + 3)
            sage: P.<x> = Zmod(10)[]
            sage: (x^2).factor()
            Traceback (most recent call last):
            ...
            NotImplementedError: factorization of polynomials over rings with composite characteristic is not implemented

        Test that factorization can be interrupted::

            sage: R.<x> = PolynomialRing(GF(65537), implementation="FLINT")
            sage: f = R.random_element(9973) * R.random_element(10007)
            sage: from sage.doctest.util import ensure_interruptible_after
            sage: with ensure_interruptible_after(0.5): f.factor()

        Test zero polynomial::

            sage: R.<x> = PolynomialRing(GF(65537), implementation="FLINT")
            sage: R.zero().factor()
            Traceback (most recent call last):
            ...
            ArithmeticError: factorization of 0 is not defined'''
    @overload
    def factor(self) -> Any:
        '''Polynomial_zmod_flint.factor(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 782)

        Return the factorization of the polynomial.

        EXAMPLES::

            sage: R.<x> = GF(5)[]
            sage: (x^2 + 1).factor()
            (x + 2) * (x + 3)

        It also works for prime-power moduli::

            sage: R.<x> = Zmod(23^5)[]
            sage: (x^3 + 1).factor()
            (x + 1) * (x^2 + 6436342*x + 1)

        TESTS::

            sage: R.<x> = GF(5)[]
            sage: (2*x^2 + 2).factor()
            (2) * (x + 2) * (x + 3)
            sage: P.<x> = Zmod(10)[]
            sage: (x^2).factor()
            Traceback (most recent call last):
            ...
            NotImplementedError: factorization of polynomials over rings with composite characteristic is not implemented

        Test that factorization can be interrupted::

            sage: R.<x> = PolynomialRing(GF(65537), implementation="FLINT")
            sage: f = R.random_element(9973) * R.random_element(10007)
            sage: from sage.doctest.util import ensure_interruptible_after
            sage: with ensure_interruptible_after(0.5): f.factor()

        Test zero polynomial::

            sage: R.<x> = PolynomialRing(GF(65537), implementation="FLINT")
            sage: R.zero().factor()
            Traceback (most recent call last):
            ...
            ArithmeticError: factorization of 0 is not defined'''
    @overload
    def factor(self) -> Any:
        '''Polynomial_zmod_flint.factor(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 782)

        Return the factorization of the polynomial.

        EXAMPLES::

            sage: R.<x> = GF(5)[]
            sage: (x^2 + 1).factor()
            (x + 2) * (x + 3)

        It also works for prime-power moduli::

            sage: R.<x> = Zmod(23^5)[]
            sage: (x^3 + 1).factor()
            (x + 1) * (x^2 + 6436342*x + 1)

        TESTS::

            sage: R.<x> = GF(5)[]
            sage: (2*x^2 + 2).factor()
            (2) * (x + 2) * (x + 3)
            sage: P.<x> = Zmod(10)[]
            sage: (x^2).factor()
            Traceback (most recent call last):
            ...
            NotImplementedError: factorization of polynomials over rings with composite characteristic is not implemented

        Test that factorization can be interrupted::

            sage: R.<x> = PolynomialRing(GF(65537), implementation="FLINT")
            sage: f = R.random_element(9973) * R.random_element(10007)
            sage: from sage.doctest.util import ensure_interruptible_after
            sage: with ensure_interruptible_after(0.5): f.factor()

        Test zero polynomial::

            sage: R.<x> = PolynomialRing(GF(65537), implementation="FLINT")
            sage: R.zero().factor()
            Traceback (most recent call last):
            ...
            ArithmeticError: factorization of 0 is not defined'''
    @overload
    def factor(self) -> Any:
        '''Polynomial_zmod_flint.factor(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 782)

        Return the factorization of the polynomial.

        EXAMPLES::

            sage: R.<x> = GF(5)[]
            sage: (x^2 + 1).factor()
            (x + 2) * (x + 3)

        It also works for prime-power moduli::

            sage: R.<x> = Zmod(23^5)[]
            sage: (x^3 + 1).factor()
            (x + 1) * (x^2 + 6436342*x + 1)

        TESTS::

            sage: R.<x> = GF(5)[]
            sage: (2*x^2 + 2).factor()
            (2) * (x + 2) * (x + 3)
            sage: P.<x> = Zmod(10)[]
            sage: (x^2).factor()
            Traceback (most recent call last):
            ...
            NotImplementedError: factorization of polynomials over rings with composite characteristic is not implemented

        Test that factorization can be interrupted::

            sage: R.<x> = PolynomialRing(GF(65537), implementation="FLINT")
            sage: f = R.random_element(9973) * R.random_element(10007)
            sage: from sage.doctest.util import ensure_interruptible_after
            sage: with ensure_interruptible_after(0.5): f.factor()

        Test zero polynomial::

            sage: R.<x> = PolynomialRing(GF(65537), implementation="FLINT")
            sage: R.zero().factor()
            Traceback (most recent call last):
            ...
            ArithmeticError: factorization of 0 is not defined'''
    @overload
    def factor(self) -> Any:
        '''Polynomial_zmod_flint.factor(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 782)

        Return the factorization of the polynomial.

        EXAMPLES::

            sage: R.<x> = GF(5)[]
            sage: (x^2 + 1).factor()
            (x + 2) * (x + 3)

        It also works for prime-power moduli::

            sage: R.<x> = Zmod(23^5)[]
            sage: (x^3 + 1).factor()
            (x + 1) * (x^2 + 6436342*x + 1)

        TESTS::

            sage: R.<x> = GF(5)[]
            sage: (2*x^2 + 2).factor()
            (2) * (x + 2) * (x + 3)
            sage: P.<x> = Zmod(10)[]
            sage: (x^2).factor()
            Traceback (most recent call last):
            ...
            NotImplementedError: factorization of polynomials over rings with composite characteristic is not implemented

        Test that factorization can be interrupted::

            sage: R.<x> = PolynomialRing(GF(65537), implementation="FLINT")
            sage: f = R.random_element(9973) * R.random_element(10007)
            sage: from sage.doctest.util import ensure_interruptible_after
            sage: with ensure_interruptible_after(0.5): f.factor()

        Test zero polynomial::

            sage: R.<x> = PolynomialRing(GF(65537), implementation="FLINT")
            sage: R.zero().factor()
            Traceback (most recent call last):
            ...
            ArithmeticError: factorization of 0 is not defined'''
    @overload
    def factor(self) -> Any:
        '''Polynomial_zmod_flint.factor(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 782)

        Return the factorization of the polynomial.

        EXAMPLES::

            sage: R.<x> = GF(5)[]
            sage: (x^2 + 1).factor()
            (x + 2) * (x + 3)

        It also works for prime-power moduli::

            sage: R.<x> = Zmod(23^5)[]
            sage: (x^3 + 1).factor()
            (x + 1) * (x^2 + 6436342*x + 1)

        TESTS::

            sage: R.<x> = GF(5)[]
            sage: (2*x^2 + 2).factor()
            (2) * (x + 2) * (x + 3)
            sage: P.<x> = Zmod(10)[]
            sage: (x^2).factor()
            Traceback (most recent call last):
            ...
            NotImplementedError: factorization of polynomials over rings with composite characteristic is not implemented

        Test that factorization can be interrupted::

            sage: R.<x> = PolynomialRing(GF(65537), implementation="FLINT")
            sage: f = R.random_element(9973) * R.random_element(10007)
            sage: from sage.doctest.util import ensure_interruptible_after
            sage: with ensure_interruptible_after(0.5): f.factor()

        Test zero polynomial::

            sage: R.<x> = PolynomialRing(GF(65537), implementation="FLINT")
            sage: R.zero().factor()
            Traceback (most recent call last):
            ...
            ArithmeticError: factorization of 0 is not defined'''
    @overload
    def factor(self) -> Any:
        '''Polynomial_zmod_flint.factor(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 782)

        Return the factorization of the polynomial.

        EXAMPLES::

            sage: R.<x> = GF(5)[]
            sage: (x^2 + 1).factor()
            (x + 2) * (x + 3)

        It also works for prime-power moduli::

            sage: R.<x> = Zmod(23^5)[]
            sage: (x^3 + 1).factor()
            (x + 1) * (x^2 + 6436342*x + 1)

        TESTS::

            sage: R.<x> = GF(5)[]
            sage: (2*x^2 + 2).factor()
            (2) * (x + 2) * (x + 3)
            sage: P.<x> = Zmod(10)[]
            sage: (x^2).factor()
            Traceback (most recent call last):
            ...
            NotImplementedError: factorization of polynomials over rings with composite characteristic is not implemented

        Test that factorization can be interrupted::

            sage: R.<x> = PolynomialRing(GF(65537), implementation="FLINT")
            sage: f = R.random_element(9973) * R.random_element(10007)
            sage: from sage.doctest.util import ensure_interruptible_after
            sage: with ensure_interruptible_after(0.5): f.factor()

        Test zero polynomial::

            sage: R.<x> = PolynomialRing(GF(65537), implementation="FLINT")
            sage: R.zero().factor()
            Traceback (most recent call last):
            ...
            ArithmeticError: factorization of 0 is not defined'''
    @overload
    def is_irreducible(self) -> Any:
        """Polynomial_zmod_flint.is_irreducible(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 676)

        Return whether this polynomial is irreducible.

        EXAMPLES::

            sage: R.<x> = GF(5)[]
            sage: (x^2 + 1).is_irreducible()
            False
            sage: (x^3 + x + 1).is_irreducible()
            True

        Not implemented when the base ring is not a field::

            sage: S.<s> = Zmod(10)[]
            sage: (s^2).is_irreducible()
            Traceback (most recent call last):
            ...
            NotImplementedError: checking irreducibility of polynomials
            over rings with composite characteristic is not implemented

        TESTS::

            sage: R(0).is_irreducible()
            False
            sage: R(1).is_irreducible()
            False
            sage: R(2).is_irreducible()
            False

            sage: S(1).is_irreducible()
            False
            sage: S(2).is_irreducible()
            Traceback (most recent call last):
            ...
            NotImplementedError: checking irreducibility of polynomials
            over rings with composite characteristic is not implemented

        Test that caching works::

            sage: S.<s> = Zmod(7)[]
            sage: s.is_irreducible()
            True
            sage: s.is_irreducible.cache
            True"""
    @overload
    def is_irreducible(self) -> Any:
        """Polynomial_zmod_flint.is_irreducible(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 676)

        Return whether this polynomial is irreducible.

        EXAMPLES::

            sage: R.<x> = GF(5)[]
            sage: (x^2 + 1).is_irreducible()
            False
            sage: (x^3 + x + 1).is_irreducible()
            True

        Not implemented when the base ring is not a field::

            sage: S.<s> = Zmod(10)[]
            sage: (s^2).is_irreducible()
            Traceback (most recent call last):
            ...
            NotImplementedError: checking irreducibility of polynomials
            over rings with composite characteristic is not implemented

        TESTS::

            sage: R(0).is_irreducible()
            False
            sage: R(1).is_irreducible()
            False
            sage: R(2).is_irreducible()
            False

            sage: S(1).is_irreducible()
            False
            sage: S(2).is_irreducible()
            Traceback (most recent call last):
            ...
            NotImplementedError: checking irreducibility of polynomials
            over rings with composite characteristic is not implemented

        Test that caching works::

            sage: S.<s> = Zmod(7)[]
            sage: s.is_irreducible()
            True
            sage: s.is_irreducible.cache
            True"""
    @overload
    def is_irreducible(self) -> Any:
        """Polynomial_zmod_flint.is_irreducible(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 676)

        Return whether this polynomial is irreducible.

        EXAMPLES::

            sage: R.<x> = GF(5)[]
            sage: (x^2 + 1).is_irreducible()
            False
            sage: (x^3 + x + 1).is_irreducible()
            True

        Not implemented when the base ring is not a field::

            sage: S.<s> = Zmod(10)[]
            sage: (s^2).is_irreducible()
            Traceback (most recent call last):
            ...
            NotImplementedError: checking irreducibility of polynomials
            over rings with composite characteristic is not implemented

        TESTS::

            sage: R(0).is_irreducible()
            False
            sage: R(1).is_irreducible()
            False
            sage: R(2).is_irreducible()
            False

            sage: S(1).is_irreducible()
            False
            sage: S(2).is_irreducible()
            Traceback (most recent call last):
            ...
            NotImplementedError: checking irreducibility of polynomials
            over rings with composite characteristic is not implemented

        Test that caching works::

            sage: S.<s> = Zmod(7)[]
            sage: s.is_irreducible()
            True
            sage: s.is_irreducible.cache
            True"""
    @overload
    def is_irreducible(self) -> Any:
        """Polynomial_zmod_flint.is_irreducible(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 676)

        Return whether this polynomial is irreducible.

        EXAMPLES::

            sage: R.<x> = GF(5)[]
            sage: (x^2 + 1).is_irreducible()
            False
            sage: (x^3 + x + 1).is_irreducible()
            True

        Not implemented when the base ring is not a field::

            sage: S.<s> = Zmod(10)[]
            sage: (s^2).is_irreducible()
            Traceback (most recent call last):
            ...
            NotImplementedError: checking irreducibility of polynomials
            over rings with composite characteristic is not implemented

        TESTS::

            sage: R(0).is_irreducible()
            False
            sage: R(1).is_irreducible()
            False
            sage: R(2).is_irreducible()
            False

            sage: S(1).is_irreducible()
            False
            sage: S(2).is_irreducible()
            Traceback (most recent call last):
            ...
            NotImplementedError: checking irreducibility of polynomials
            over rings with composite characteristic is not implemented

        Test that caching works::

            sage: S.<s> = Zmod(7)[]
            sage: s.is_irreducible()
            True
            sage: s.is_irreducible.cache
            True"""
    @overload
    def is_irreducible(self) -> Any:
        """Polynomial_zmod_flint.is_irreducible(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 676)

        Return whether this polynomial is irreducible.

        EXAMPLES::

            sage: R.<x> = GF(5)[]
            sage: (x^2 + 1).is_irreducible()
            False
            sage: (x^3 + x + 1).is_irreducible()
            True

        Not implemented when the base ring is not a field::

            sage: S.<s> = Zmod(10)[]
            sage: (s^2).is_irreducible()
            Traceback (most recent call last):
            ...
            NotImplementedError: checking irreducibility of polynomials
            over rings with composite characteristic is not implemented

        TESTS::

            sage: R(0).is_irreducible()
            False
            sage: R(1).is_irreducible()
            False
            sage: R(2).is_irreducible()
            False

            sage: S(1).is_irreducible()
            False
            sage: S(2).is_irreducible()
            Traceback (most recent call last):
            ...
            NotImplementedError: checking irreducibility of polynomials
            over rings with composite characteristic is not implemented

        Test that caching works::

            sage: S.<s> = Zmod(7)[]
            sage: s.is_irreducible()
            True
            sage: s.is_irreducible.cache
            True"""
    @overload
    def is_irreducible(self) -> Any:
        """Polynomial_zmod_flint.is_irreducible(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 676)

        Return whether this polynomial is irreducible.

        EXAMPLES::

            sage: R.<x> = GF(5)[]
            sage: (x^2 + 1).is_irreducible()
            False
            sage: (x^3 + x + 1).is_irreducible()
            True

        Not implemented when the base ring is not a field::

            sage: S.<s> = Zmod(10)[]
            sage: (s^2).is_irreducible()
            Traceback (most recent call last):
            ...
            NotImplementedError: checking irreducibility of polynomials
            over rings with composite characteristic is not implemented

        TESTS::

            sage: R(0).is_irreducible()
            False
            sage: R(1).is_irreducible()
            False
            sage: R(2).is_irreducible()
            False

            sage: S(1).is_irreducible()
            False
            sage: S(2).is_irreducible()
            Traceback (most recent call last):
            ...
            NotImplementedError: checking irreducibility of polynomials
            over rings with composite characteristic is not implemented

        Test that caching works::

            sage: S.<s> = Zmod(7)[]
            sage: s.is_irreducible()
            True
            sage: s.is_irreducible.cache
            True"""
    @overload
    def is_irreducible(self) -> Any:
        """Polynomial_zmod_flint.is_irreducible(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 676)

        Return whether this polynomial is irreducible.

        EXAMPLES::

            sage: R.<x> = GF(5)[]
            sage: (x^2 + 1).is_irreducible()
            False
            sage: (x^3 + x + 1).is_irreducible()
            True

        Not implemented when the base ring is not a field::

            sage: S.<s> = Zmod(10)[]
            sage: (s^2).is_irreducible()
            Traceback (most recent call last):
            ...
            NotImplementedError: checking irreducibility of polynomials
            over rings with composite characteristic is not implemented

        TESTS::

            sage: R(0).is_irreducible()
            False
            sage: R(1).is_irreducible()
            False
            sage: R(2).is_irreducible()
            False

            sage: S(1).is_irreducible()
            False
            sage: S(2).is_irreducible()
            Traceback (most recent call last):
            ...
            NotImplementedError: checking irreducibility of polynomials
            over rings with composite characteristic is not implemented

        Test that caching works::

            sage: S.<s> = Zmod(7)[]
            sage: s.is_irreducible()
            True
            sage: s.is_irreducible.cache
            True"""
    @overload
    def is_irreducible(self) -> Any:
        """Polynomial_zmod_flint.is_irreducible(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 676)

        Return whether this polynomial is irreducible.

        EXAMPLES::

            sage: R.<x> = GF(5)[]
            sage: (x^2 + 1).is_irreducible()
            False
            sage: (x^3 + x + 1).is_irreducible()
            True

        Not implemented when the base ring is not a field::

            sage: S.<s> = Zmod(10)[]
            sage: (s^2).is_irreducible()
            Traceback (most recent call last):
            ...
            NotImplementedError: checking irreducibility of polynomials
            over rings with composite characteristic is not implemented

        TESTS::

            sage: R(0).is_irreducible()
            False
            sage: R(1).is_irreducible()
            False
            sage: R(2).is_irreducible()
            False

            sage: S(1).is_irreducible()
            False
            sage: S(2).is_irreducible()
            Traceback (most recent call last):
            ...
            NotImplementedError: checking irreducibility of polynomials
            over rings with composite characteristic is not implemented

        Test that caching works::

            sage: S.<s> = Zmod(7)[]
            sage: s.is_irreducible()
            True
            sage: s.is_irreducible.cache
            True"""
    @overload
    def is_irreducible(self) -> Any:
        """Polynomial_zmod_flint.is_irreducible(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 676)

        Return whether this polynomial is irreducible.

        EXAMPLES::

            sage: R.<x> = GF(5)[]
            sage: (x^2 + 1).is_irreducible()
            False
            sage: (x^3 + x + 1).is_irreducible()
            True

        Not implemented when the base ring is not a field::

            sage: S.<s> = Zmod(10)[]
            sage: (s^2).is_irreducible()
            Traceback (most recent call last):
            ...
            NotImplementedError: checking irreducibility of polynomials
            over rings with composite characteristic is not implemented

        TESTS::

            sage: R(0).is_irreducible()
            False
            sage: R(1).is_irreducible()
            False
            sage: R(2).is_irreducible()
            False

            sage: S(1).is_irreducible()
            False
            sage: S(2).is_irreducible()
            Traceback (most recent call last):
            ...
            NotImplementedError: checking irreducibility of polynomials
            over rings with composite characteristic is not implemented

        Test that caching works::

            sage: S.<s> = Zmod(7)[]
            sage: s.is_irreducible()
            True
            sage: s.is_irreducible.cache
            True"""
    @overload
    def is_irreducible(self) -> Any:
        """Polynomial_zmod_flint.is_irreducible(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 676)

        Return whether this polynomial is irreducible.

        EXAMPLES::

            sage: R.<x> = GF(5)[]
            sage: (x^2 + 1).is_irreducible()
            False
            sage: (x^3 + x + 1).is_irreducible()
            True

        Not implemented when the base ring is not a field::

            sage: S.<s> = Zmod(10)[]
            sage: (s^2).is_irreducible()
            Traceback (most recent call last):
            ...
            NotImplementedError: checking irreducibility of polynomials
            over rings with composite characteristic is not implemented

        TESTS::

            sage: R(0).is_irreducible()
            False
            sage: R(1).is_irreducible()
            False
            sage: R(2).is_irreducible()
            False

            sage: S(1).is_irreducible()
            False
            sage: S(2).is_irreducible()
            Traceback (most recent call last):
            ...
            NotImplementedError: checking irreducibility of polynomials
            over rings with composite characteristic is not implemented

        Test that caching works::

            sage: S.<s> = Zmod(7)[]
            sage: s.is_irreducible()
            True
            sage: s.is_irreducible.cache
            True"""
    def minpoly_mod(self, other) -> Any:
        """Polynomial_zmod_flint.minpoly_mod(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 993)

        Thin wrapper for
        :meth:`sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_mod_n.minpoly_mod`.

        EXAMPLES::

            sage: R.<x> = GF(127)[]
            sage: type(x)
            <class 'sage.rings.polynomial.polynomial_zmod_flint.Polynomial_zmod_flint'>
            sage: (x^5 - 3).minpoly_mod(x^3 + 5*x - 1)
            x^3 + 34*x^2 + 125*x + 95"""
    def modular_composition(self, *args, **kwargs):
        """Polynomial_zmod_flint.compose_mod(self, other, modulus)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 1013)

        Compute `f(g) \\bmod h`.

        To be precise about the order fo compostion, given ``self``, ``other``
        and ``modulus`` as `f(x)`, `g(x)` and `h(x)` compute `f(g(x)) \\bmod h(x)`.

        INPUT:

        - ``other`` -- a polynomial `g(x)`
        - ``modulus`` -- a polynomial `h(x)`

        EXAMPLES::

            sage: R.<x> = GF(163)[]
            sage: f = R.random_element()
            sage: g = R.random_element()
            sage: g.compose_mod(g, f) == g(g) % f
            True

            sage: f = R([i for i in range(100)])
            sage: g = R([i**2 for i in range(100)])
            sage: h = 1 + x + x**5
            sage: f.compose_mod(g, h)
            82*x^4 + 56*x^3 + 45*x^2 + 60*x + 127
            sage: f.compose_mod(g, h) == f(g) % h
            True

        AUTHORS:

        - Giacomo Pope (2024-08) initial implementation"""
    @overload
    def monic(self) -> Any:
        """Polynomial_zmod_flint.monic(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 843)

        Return this polynomial divided by its leading coefficient.

        Raises :exc:`ValueError` if the leading coefficient is not invertible in the
        base ring.

        EXAMPLES::

            sage: R.<x> = GF(5)[]
            sage: (2*x^2 + 1).monic()
            x^2 + 3

        TESTS::

            sage: R.<x> = Zmod(10)[]
            sage: (5*x).monic()
            Traceback (most recent call last):
            ...
            ValueError: leading coefficient must be invertible"""
    @overload
    def monic(self) -> Any:
        """Polynomial_zmod_flint.monic(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 843)

        Return this polynomial divided by its leading coefficient.

        Raises :exc:`ValueError` if the leading coefficient is not invertible in the
        base ring.

        EXAMPLES::

            sage: R.<x> = GF(5)[]
            sage: (2*x^2 + 1).monic()
            x^2 + 3

        TESTS::

            sage: R.<x> = Zmod(10)[]
            sage: (5*x).monic()
            Traceback (most recent call last):
            ...
            ValueError: leading coefficient must be invertible"""
    @overload
    def monic(self) -> Any:
        """Polynomial_zmod_flint.monic(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 843)

        Return this polynomial divided by its leading coefficient.

        Raises :exc:`ValueError` if the leading coefficient is not invertible in the
        base ring.

        EXAMPLES::

            sage: R.<x> = GF(5)[]
            sage: (2*x^2 + 1).monic()
            x^2 + 3

        TESTS::

            sage: R.<x> = Zmod(10)[]
            sage: (5*x).monic()
            Traceback (most recent call last):
            ...
            ValueError: leading coefficient must be invertible"""
    def rational_reconstruct(self, *args, **kwargs):
        """Deprecated: Use :meth:`rational_reconstruction` instead.
        See :issue:`12696` for details.

        """
    def rational_reconstruction(self, m, n_deg=..., d_deg=...) -> Any:
        """Polynomial_zmod_flint.rational_reconstruction(self, m, n_deg=0, d_deg=0)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 607)

        Construct a rational function `n/d` such that `p*d` is equivalent to `n`
        modulo `m` where `p` is this polynomial.

        EXAMPLES::

            sage: P.<x> = GF(5)[]
            sage: p = 4*x^5 + 3*x^4 + 2*x^3 + 2*x^2 + 4*x + 2
            sage: n, d = p.rational_reconstruction(x^9, 4, 4); n, d
            (3*x^4 + 2*x^3 + x^2 + 2*x, x^4 + 3*x^3 + x^2 + x)
            sage: (p*d % x^9) == n
            True

        Check that :issue:`37169` is fixed - it does not throw an error::

            sage: R.<x> = Zmod(4)[]
            sage: _.<z> = R.quotient_ring(x^2 - 1)
            sage: c = 2 * z + 1
            sage: c * Zmod(2).zero()
            Traceback (most recent call last):
            ...
            RuntimeError: Aborted"""
    @overload
    def resultant(self, Polynomial_zmod_flintother) -> Any:
        """Polynomial_zmod_flint.resultant(self, Polynomial_zmod_flint other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 325)

        Return the resultant of ``self`` and ``other``, which must lie in the same
        polynomial ring.

        INPUT:

        - ``other`` -- a polynomial

        OUTPUT: an element of the base ring of the polynomial ring

        EXAMPLES::

            sage: R.<x> = GF(19)['x']
            sage: f = x^3 + x + 1;  g = x^3 - x - 1
            sage: r = f.resultant(g); r
            11
            sage: r.parent() is GF(19)
            True

        The following example shows that :issue:`11782` has been fixed::

            sage: R.<x> = ZZ.quo(9)['x']
            sage: f = 2*x^3 + x^2 + x;  g = 6*x^2 + 2*x + 1
            sage: f.resultant(g)
            5"""
    @overload
    def resultant(self, g) -> Any:
        """Polynomial_zmod_flint.resultant(self, Polynomial_zmod_flint other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 325)

        Return the resultant of ``self`` and ``other``, which must lie in the same
        polynomial ring.

        INPUT:

        - ``other`` -- a polynomial

        OUTPUT: an element of the base ring of the polynomial ring

        EXAMPLES::

            sage: R.<x> = GF(19)['x']
            sage: f = x^3 + x + 1;  g = x^3 - x - 1
            sage: r = f.resultant(g); r
            11
            sage: r.parent() is GF(19)
            True

        The following example shows that :issue:`11782` has been fixed::

            sage: R.<x> = ZZ.quo(9)['x']
            sage: f = 2*x^3 + x^2 + x;  g = 6*x^2 + 2*x + 1
            sage: f.resultant(g)
            5"""
    @overload
    def resultant(self, g) -> Any:
        """Polynomial_zmod_flint.resultant(self, Polynomial_zmod_flint other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 325)

        Return the resultant of ``self`` and ``other``, which must lie in the same
        polynomial ring.

        INPUT:

        - ``other`` -- a polynomial

        OUTPUT: an element of the base ring of the polynomial ring

        EXAMPLES::

            sage: R.<x> = GF(19)['x']
            sage: f = x^3 + x + 1;  g = x^3 - x - 1
            sage: r = f.resultant(g); r
            11
            sage: r.parent() is GF(19)
            True

        The following example shows that :issue:`11782` has been fixed::

            sage: R.<x> = ZZ.quo(9)['x']
            sage: f = 2*x^3 + x^2 + x;  g = 6*x^2 + 2*x + 1
            sage: f.resultant(g)
            5"""
    @overload
    def reverse(self, degree=...) -> Any:
        """Polynomial_zmod_flint.reverse(self, degree=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 874)

        Return a polynomial with the coefficients of this polynomial reversed.

        If the optional argument ``degree`` is given, the coefficient list will be
        truncated or zero padded as necessary before computing the reverse.

        EXAMPLES::

            sage: R.<x> = GF(5)[]
            sage: p = R([1,2,3,4]); p
            4*x^3 + 3*x^2 + 2*x + 1
            sage: p.reverse()
            x^3 + 2*x^2 + 3*x + 4
            sage: p.reverse(degree=6)
            x^6 + 2*x^5 + 3*x^4 + 4*x^3
            sage: p.reverse(degree=2)
            x^2 + 2*x + 3

            sage: R.<x> = GF(101)[]
            sage: f = x^3 - x + 2; f
            x^3 + 100*x + 2
            sage: f.reverse()
            2*x^3 + 100*x^2 + 1
            sage: f.reverse() == f(1/x) * x^f.degree()
            True

        Note that if `f` has zero constant coefficient, its reverse will
        have lower degree.

        ::

            sage: f = x^3 + 2*x
            sage: f.reverse()
            2*x^2 + 1

        In this case, reverse is not an involution unless we explicitly
        specify a degree.

        ::

            sage: f
            x^3 + 2*x
            sage: f.reverse().reverse()
            x^2 + 2
            sage: f.reverse(5).reverse(5)
            x^3 + 2*x

        TESTS::

            sage: p.reverse(degree=1.5r)
            Traceback (most recent call last):
            ...
            ValueError: degree argument must be a nonnegative integer, got 1.5

        Check that this implementation is compatible with the generic one::

            sage: p = R([0,1,0,2])
            sage: all(p.reverse(d) == Polynomial.reverse(p, d)
            ....:     for d in [None, 0, 1, 2, 3, 4])
            True"""
    @overload
    def reverse(self) -> Any:
        """Polynomial_zmod_flint.reverse(self, degree=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 874)

        Return a polynomial with the coefficients of this polynomial reversed.

        If the optional argument ``degree`` is given, the coefficient list will be
        truncated or zero padded as necessary before computing the reverse.

        EXAMPLES::

            sage: R.<x> = GF(5)[]
            sage: p = R([1,2,3,4]); p
            4*x^3 + 3*x^2 + 2*x + 1
            sage: p.reverse()
            x^3 + 2*x^2 + 3*x + 4
            sage: p.reverse(degree=6)
            x^6 + 2*x^5 + 3*x^4 + 4*x^3
            sage: p.reverse(degree=2)
            x^2 + 2*x + 3

            sage: R.<x> = GF(101)[]
            sage: f = x^3 - x + 2; f
            x^3 + 100*x + 2
            sage: f.reverse()
            2*x^3 + 100*x^2 + 1
            sage: f.reverse() == f(1/x) * x^f.degree()
            True

        Note that if `f` has zero constant coefficient, its reverse will
        have lower degree.

        ::

            sage: f = x^3 + 2*x
            sage: f.reverse()
            2*x^2 + 1

        In this case, reverse is not an involution unless we explicitly
        specify a degree.

        ::

            sage: f
            x^3 + 2*x
            sage: f.reverse().reverse()
            x^2 + 2
            sage: f.reverse(5).reverse(5)
            x^3 + 2*x

        TESTS::

            sage: p.reverse(degree=1.5r)
            Traceback (most recent call last):
            ...
            ValueError: degree argument must be a nonnegative integer, got 1.5

        Check that this implementation is compatible with the generic one::

            sage: p = R([0,1,0,2])
            sage: all(p.reverse(d) == Polynomial.reverse(p, d)
            ....:     for d in [None, 0, 1, 2, 3, 4])
            True"""
    @overload
    def reverse(self, degree=...) -> Any:
        """Polynomial_zmod_flint.reverse(self, degree=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 874)

        Return a polynomial with the coefficients of this polynomial reversed.

        If the optional argument ``degree`` is given, the coefficient list will be
        truncated or zero padded as necessary before computing the reverse.

        EXAMPLES::

            sage: R.<x> = GF(5)[]
            sage: p = R([1,2,3,4]); p
            4*x^3 + 3*x^2 + 2*x + 1
            sage: p.reverse()
            x^3 + 2*x^2 + 3*x + 4
            sage: p.reverse(degree=6)
            x^6 + 2*x^5 + 3*x^4 + 4*x^3
            sage: p.reverse(degree=2)
            x^2 + 2*x + 3

            sage: R.<x> = GF(101)[]
            sage: f = x^3 - x + 2; f
            x^3 + 100*x + 2
            sage: f.reverse()
            2*x^3 + 100*x^2 + 1
            sage: f.reverse() == f(1/x) * x^f.degree()
            True

        Note that if `f` has zero constant coefficient, its reverse will
        have lower degree.

        ::

            sage: f = x^3 + 2*x
            sage: f.reverse()
            2*x^2 + 1

        In this case, reverse is not an involution unless we explicitly
        specify a degree.

        ::

            sage: f
            x^3 + 2*x
            sage: f.reverse().reverse()
            x^2 + 2
            sage: f.reverse(5).reverse(5)
            x^3 + 2*x

        TESTS::

            sage: p.reverse(degree=1.5r)
            Traceback (most recent call last):
            ...
            ValueError: degree argument must be a nonnegative integer, got 1.5

        Check that this implementation is compatible with the generic one::

            sage: p = R([0,1,0,2])
            sage: all(p.reverse(d) == Polynomial.reverse(p, d)
            ....:     for d in [None, 0, 1, 2, 3, 4])
            True"""
    @overload
    def reverse(self, degree=...) -> Any:
        """Polynomial_zmod_flint.reverse(self, degree=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 874)

        Return a polynomial with the coefficients of this polynomial reversed.

        If the optional argument ``degree`` is given, the coefficient list will be
        truncated or zero padded as necessary before computing the reverse.

        EXAMPLES::

            sage: R.<x> = GF(5)[]
            sage: p = R([1,2,3,4]); p
            4*x^3 + 3*x^2 + 2*x + 1
            sage: p.reverse()
            x^3 + 2*x^2 + 3*x + 4
            sage: p.reverse(degree=6)
            x^6 + 2*x^5 + 3*x^4 + 4*x^3
            sage: p.reverse(degree=2)
            x^2 + 2*x + 3

            sage: R.<x> = GF(101)[]
            sage: f = x^3 - x + 2; f
            x^3 + 100*x + 2
            sage: f.reverse()
            2*x^3 + 100*x^2 + 1
            sage: f.reverse() == f(1/x) * x^f.degree()
            True

        Note that if `f` has zero constant coefficient, its reverse will
        have lower degree.

        ::

            sage: f = x^3 + 2*x
            sage: f.reverse()
            2*x^2 + 1

        In this case, reverse is not an involution unless we explicitly
        specify a degree.

        ::

            sage: f
            x^3 + 2*x
            sage: f.reverse().reverse()
            x^2 + 2
            sage: f.reverse(5).reverse(5)
            x^3 + 2*x

        TESTS::

            sage: p.reverse(degree=1.5r)
            Traceback (most recent call last):
            ...
            ValueError: degree argument must be a nonnegative integer, got 1.5

        Check that this implementation is compatible with the generic one::

            sage: p = R([0,1,0,2])
            sage: all(p.reverse(d) == Polynomial.reverse(p, d)
            ....:     for d in [None, 0, 1, 2, 3, 4])
            True"""
    @overload
    def reverse(self) -> Any:
        """Polynomial_zmod_flint.reverse(self, degree=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 874)

        Return a polynomial with the coefficients of this polynomial reversed.

        If the optional argument ``degree`` is given, the coefficient list will be
        truncated or zero padded as necessary before computing the reverse.

        EXAMPLES::

            sage: R.<x> = GF(5)[]
            sage: p = R([1,2,3,4]); p
            4*x^3 + 3*x^2 + 2*x + 1
            sage: p.reverse()
            x^3 + 2*x^2 + 3*x + 4
            sage: p.reverse(degree=6)
            x^6 + 2*x^5 + 3*x^4 + 4*x^3
            sage: p.reverse(degree=2)
            x^2 + 2*x + 3

            sage: R.<x> = GF(101)[]
            sage: f = x^3 - x + 2; f
            x^3 + 100*x + 2
            sage: f.reverse()
            2*x^3 + 100*x^2 + 1
            sage: f.reverse() == f(1/x) * x^f.degree()
            True

        Note that if `f` has zero constant coefficient, its reverse will
        have lower degree.

        ::

            sage: f = x^3 + 2*x
            sage: f.reverse()
            2*x^2 + 1

        In this case, reverse is not an involution unless we explicitly
        specify a degree.

        ::

            sage: f
            x^3 + 2*x
            sage: f.reverse().reverse()
            x^2 + 2
            sage: f.reverse(5).reverse(5)
            x^3 + 2*x

        TESTS::

            sage: p.reverse(degree=1.5r)
            Traceback (most recent call last):
            ...
            ValueError: degree argument must be a nonnegative integer, got 1.5

        Check that this implementation is compatible with the generic one::

            sage: p = R([0,1,0,2])
            sage: all(p.reverse(d) == Polynomial.reverse(p, d)
            ....:     for d in [None, 0, 1, 2, 3, 4])
            True"""
    @overload
    def reverse(self) -> Any:
        """Polynomial_zmod_flint.reverse(self, degree=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 874)

        Return a polynomial with the coefficients of this polynomial reversed.

        If the optional argument ``degree`` is given, the coefficient list will be
        truncated or zero padded as necessary before computing the reverse.

        EXAMPLES::

            sage: R.<x> = GF(5)[]
            sage: p = R([1,2,3,4]); p
            4*x^3 + 3*x^2 + 2*x + 1
            sage: p.reverse()
            x^3 + 2*x^2 + 3*x + 4
            sage: p.reverse(degree=6)
            x^6 + 2*x^5 + 3*x^4 + 4*x^3
            sage: p.reverse(degree=2)
            x^2 + 2*x + 3

            sage: R.<x> = GF(101)[]
            sage: f = x^3 - x + 2; f
            x^3 + 100*x + 2
            sage: f.reverse()
            2*x^3 + 100*x^2 + 1
            sage: f.reverse() == f(1/x) * x^f.degree()
            True

        Note that if `f` has zero constant coefficient, its reverse will
        have lower degree.

        ::

            sage: f = x^3 + 2*x
            sage: f.reverse()
            2*x^2 + 1

        In this case, reverse is not an involution unless we explicitly
        specify a degree.

        ::

            sage: f
            x^3 + 2*x
            sage: f.reverse().reverse()
            x^2 + 2
            sage: f.reverse(5).reverse(5)
            x^3 + 2*x

        TESTS::

            sage: p.reverse(degree=1.5r)
            Traceback (most recent call last):
            ...
            ValueError: degree argument must be a nonnegative integer, got 1.5

        Check that this implementation is compatible with the generic one::

            sage: p = R([0,1,0,2])
            sage: all(p.reverse(d) == Polynomial.reverse(p, d)
            ....:     for d in [None, 0, 1, 2, 3, 4])
            True"""
    @overload
    def reverse(self) -> Any:
        """Polynomial_zmod_flint.reverse(self, degree=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 874)

        Return a polynomial with the coefficients of this polynomial reversed.

        If the optional argument ``degree`` is given, the coefficient list will be
        truncated or zero padded as necessary before computing the reverse.

        EXAMPLES::

            sage: R.<x> = GF(5)[]
            sage: p = R([1,2,3,4]); p
            4*x^3 + 3*x^2 + 2*x + 1
            sage: p.reverse()
            x^3 + 2*x^2 + 3*x + 4
            sage: p.reverse(degree=6)
            x^6 + 2*x^5 + 3*x^4 + 4*x^3
            sage: p.reverse(degree=2)
            x^2 + 2*x + 3

            sage: R.<x> = GF(101)[]
            sage: f = x^3 - x + 2; f
            x^3 + 100*x + 2
            sage: f.reverse()
            2*x^3 + 100*x^2 + 1
            sage: f.reverse() == f(1/x) * x^f.degree()
            True

        Note that if `f` has zero constant coefficient, its reverse will
        have lower degree.

        ::

            sage: f = x^3 + 2*x
            sage: f.reverse()
            2*x^2 + 1

        In this case, reverse is not an involution unless we explicitly
        specify a degree.

        ::

            sage: f
            x^3 + 2*x
            sage: f.reverse().reverse()
            x^2 + 2
            sage: f.reverse(5).reverse(5)
            x^3 + 2*x

        TESTS::

            sage: p.reverse(degree=1.5r)
            Traceback (most recent call last):
            ...
            ValueError: degree argument must be a nonnegative integer, got 1.5

        Check that this implementation is compatible with the generic one::

            sage: p = R([0,1,0,2])
            sage: all(p.reverse(d) == Polynomial.reverse(p, d)
            ....:     for d in [None, 0, 1, 2, 3, 4])
            True"""
    @overload
    def reverse(self) -> Any:
        """Polynomial_zmod_flint.reverse(self, degree=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 874)

        Return a polynomial with the coefficients of this polynomial reversed.

        If the optional argument ``degree`` is given, the coefficient list will be
        truncated or zero padded as necessary before computing the reverse.

        EXAMPLES::

            sage: R.<x> = GF(5)[]
            sage: p = R([1,2,3,4]); p
            4*x^3 + 3*x^2 + 2*x + 1
            sage: p.reverse()
            x^3 + 2*x^2 + 3*x + 4
            sage: p.reverse(degree=6)
            x^6 + 2*x^5 + 3*x^4 + 4*x^3
            sage: p.reverse(degree=2)
            x^2 + 2*x + 3

            sage: R.<x> = GF(101)[]
            sage: f = x^3 - x + 2; f
            x^3 + 100*x + 2
            sage: f.reverse()
            2*x^3 + 100*x^2 + 1
            sage: f.reverse() == f(1/x) * x^f.degree()
            True

        Note that if `f` has zero constant coefficient, its reverse will
        have lower degree.

        ::

            sage: f = x^3 + 2*x
            sage: f.reverse()
            2*x^2 + 1

        In this case, reverse is not an involution unless we explicitly
        specify a degree.

        ::

            sage: f
            x^3 + 2*x
            sage: f.reverse().reverse()
            x^2 + 2
            sage: f.reverse(5).reverse(5)
            x^3 + 2*x

        TESTS::

            sage: p.reverse(degree=1.5r)
            Traceback (most recent call last):
            ...
            ValueError: degree argument must be a nonnegative integer, got 1.5

        Check that this implementation is compatible with the generic one::

            sage: p = R([0,1,0,2])
            sage: all(p.reverse(d) == Polynomial.reverse(p, d)
            ....:     for d in [None, 0, 1, 2, 3, 4])
            True"""
    @overload
    def reverse(self, degree=...) -> Any:
        """Polynomial_zmod_flint.reverse(self, degree=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 874)

        Return a polynomial with the coefficients of this polynomial reversed.

        If the optional argument ``degree`` is given, the coefficient list will be
        truncated or zero padded as necessary before computing the reverse.

        EXAMPLES::

            sage: R.<x> = GF(5)[]
            sage: p = R([1,2,3,4]); p
            4*x^3 + 3*x^2 + 2*x + 1
            sage: p.reverse()
            x^3 + 2*x^2 + 3*x + 4
            sage: p.reverse(degree=6)
            x^6 + 2*x^5 + 3*x^4 + 4*x^3
            sage: p.reverse(degree=2)
            x^2 + 2*x + 3

            sage: R.<x> = GF(101)[]
            sage: f = x^3 - x + 2; f
            x^3 + 100*x + 2
            sage: f.reverse()
            2*x^3 + 100*x^2 + 1
            sage: f.reverse() == f(1/x) * x^f.degree()
            True

        Note that if `f` has zero constant coefficient, its reverse will
        have lower degree.

        ::

            sage: f = x^3 + 2*x
            sage: f.reverse()
            2*x^2 + 1

        In this case, reverse is not an involution unless we explicitly
        specify a degree.

        ::

            sage: f
            x^3 + 2*x
            sage: f.reverse().reverse()
            x^2 + 2
            sage: f.reverse(5).reverse(5)
            x^3 + 2*x

        TESTS::

            sage: p.reverse(degree=1.5r)
            Traceback (most recent call last):
            ...
            ValueError: degree argument must be a nonnegative integer, got 1.5

        Check that this implementation is compatible with the generic one::

            sage: p = R([0,1,0,2])
            sage: all(p.reverse(d) == Polynomial.reverse(p, d)
            ....:     for d in [None, 0, 1, 2, 3, 4])
            True"""
    def revert_series(self, n) -> Any:
        """Polynomial_zmod_flint.revert_series(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 949)

        Return a polynomial `f` such that ``f(self(x)) = self(f(x)) = x`` (mod `x^n`).

        EXAMPLES::

            sage: R.<t> =  GF(5)[]
            sage: f = t + 2*t^2 - t^3 - 3*t^4
            sage: f.revert_series(5)
            3*t^4 + 4*t^3 + 3*t^2 + t

            sage: f.revert_series(-1)
            Traceback (most recent call last):
            ...
            ValueError: argument n must be a nonnegative integer, got -1

            sage: g = - t^3 + t^5
            sage: g.revert_series(6)
            Traceback (most recent call last):
            ...
            ValueError: self must have constant coefficient 0 and a unit for coefficient t^1

            sage: g = t + 2*t^2 - t^3 -3*t^4 + t^5
            sage: g.revert_series(6)
            Traceback (most recent call last):
            ...
            ValueError: the integers 1 up to n=5 are required to be invertible over the base field"""
    @overload
    def small_roots(self, *args, **kwds) -> Any:
        """Polynomial_zmod_flint.small_roots(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 364)

        See :func:`sage.rings.polynomial.polynomial_modn_dense_ntl.small_roots`
        for the documentation of this function.

        EXAMPLES::

            sage: N = 10001
            sage: K = Zmod(10001)
            sage: P.<x> = PolynomialRing(K)
            sage: f = x^3 + 10*x^2 + 5000*x - 222
            sage: f.small_roots()
            [4]"""
    @overload
    def small_roots(self) -> Any:
        """Polynomial_zmod_flint.small_roots(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 364)

        See :func:`sage.rings.polynomial.polynomial_modn_dense_ntl.small_roots`
        for the documentation of this function.

        EXAMPLES::

            sage: N = 10001
            sage: K = Zmod(10001)
            sage: P.<x> = PolynomialRing(K)
            sage: f = x^3 + 10*x^2 + 5000*x - 222
            sage: f.small_roots()
            [4]"""
    @overload
    def squarefree_decomposition(self) -> Any:
        '''Polynomial_zmod_flint.squarefree_decomposition(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 739)

        Return the squarefree decomposition of this polynomial.

        EXAMPLES::

            sage: R.<x> = GF(5)[]
            sage: ((x+1)*(x^2+1)^2*x^3).squarefree_decomposition()
            (x + 1) * (x^2 + 1)^2 * x^3

        TESTS::

            sage: (2*x*(x+1)^2).squarefree_decomposition()
            (2) * x * (x + 1)^2
            sage: P.<x> = Zmod(10)[]
            sage: (x^2).squarefree_decomposition()
            Traceback (most recent call last):
            ...
            NotImplementedError: square free factorization of polynomials over rings with composite characteristic is not implemented

        :issue:`20003`::

            sage: P.<x> = GF(7)[]
            sage: (6*x+3).squarefree_decomposition()
            (6) * (x + 4)

        Test zero polynomial::

            sage: R.<x> = PolynomialRing(GF(65537), implementation="FLINT")
            sage: R.zero().squarefree_decomposition()
            Traceback (most recent call last):
            ...
            ArithmeticError: square-free decomposition of 0 is not defined'''
    @overload
    def squarefree_decomposition(self) -> Any:
        '''Polynomial_zmod_flint.squarefree_decomposition(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 739)

        Return the squarefree decomposition of this polynomial.

        EXAMPLES::

            sage: R.<x> = GF(5)[]
            sage: ((x+1)*(x^2+1)^2*x^3).squarefree_decomposition()
            (x + 1) * (x^2 + 1)^2 * x^3

        TESTS::

            sage: (2*x*(x+1)^2).squarefree_decomposition()
            (2) * x * (x + 1)^2
            sage: P.<x> = Zmod(10)[]
            sage: (x^2).squarefree_decomposition()
            Traceback (most recent call last):
            ...
            NotImplementedError: square free factorization of polynomials over rings with composite characteristic is not implemented

        :issue:`20003`::

            sage: P.<x> = GF(7)[]
            sage: (6*x+3).squarefree_decomposition()
            (6) * (x + 4)

        Test zero polynomial::

            sage: R.<x> = PolynomialRing(GF(65537), implementation="FLINT")
            sage: R.zero().squarefree_decomposition()
            Traceback (most recent call last):
            ...
            ArithmeticError: square-free decomposition of 0 is not defined'''
    @overload
    def squarefree_decomposition(self) -> Any:
        '''Polynomial_zmod_flint.squarefree_decomposition(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 739)

        Return the squarefree decomposition of this polynomial.

        EXAMPLES::

            sage: R.<x> = GF(5)[]
            sage: ((x+1)*(x^2+1)^2*x^3).squarefree_decomposition()
            (x + 1) * (x^2 + 1)^2 * x^3

        TESTS::

            sage: (2*x*(x+1)^2).squarefree_decomposition()
            (2) * x * (x + 1)^2
            sage: P.<x> = Zmod(10)[]
            sage: (x^2).squarefree_decomposition()
            Traceback (most recent call last):
            ...
            NotImplementedError: square free factorization of polynomials over rings with composite characteristic is not implemented

        :issue:`20003`::

            sage: P.<x> = GF(7)[]
            sage: (6*x+3).squarefree_decomposition()
            (6) * (x + 4)

        Test zero polynomial::

            sage: R.<x> = PolynomialRing(GF(65537), implementation="FLINT")
            sage: R.zero().squarefree_decomposition()
            Traceback (most recent call last):
            ...
            ArithmeticError: square-free decomposition of 0 is not defined'''
    @overload
    def squarefree_decomposition(self) -> Any:
        '''Polynomial_zmod_flint.squarefree_decomposition(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 739)

        Return the squarefree decomposition of this polynomial.

        EXAMPLES::

            sage: R.<x> = GF(5)[]
            sage: ((x+1)*(x^2+1)^2*x^3).squarefree_decomposition()
            (x + 1) * (x^2 + 1)^2 * x^3

        TESTS::

            sage: (2*x*(x+1)^2).squarefree_decomposition()
            (2) * x * (x + 1)^2
            sage: P.<x> = Zmod(10)[]
            sage: (x^2).squarefree_decomposition()
            Traceback (most recent call last):
            ...
            NotImplementedError: square free factorization of polynomials over rings with composite characteristic is not implemented

        :issue:`20003`::

            sage: P.<x> = GF(7)[]
            sage: (6*x+3).squarefree_decomposition()
            (6) * (x + 4)

        Test zero polynomial::

            sage: R.<x> = PolynomialRing(GF(65537), implementation="FLINT")
            sage: R.zero().squarefree_decomposition()
            Traceback (most recent call last):
            ...
            ArithmeticError: square-free decomposition of 0 is not defined'''
    @overload
    def squarefree_decomposition(self) -> Any:
        '''Polynomial_zmod_flint.squarefree_decomposition(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 739)

        Return the squarefree decomposition of this polynomial.

        EXAMPLES::

            sage: R.<x> = GF(5)[]
            sage: ((x+1)*(x^2+1)^2*x^3).squarefree_decomposition()
            (x + 1) * (x^2 + 1)^2 * x^3

        TESTS::

            sage: (2*x*(x+1)^2).squarefree_decomposition()
            (2) * x * (x + 1)^2
            sage: P.<x> = Zmod(10)[]
            sage: (x^2).squarefree_decomposition()
            Traceback (most recent call last):
            ...
            NotImplementedError: square free factorization of polynomials over rings with composite characteristic is not implemented

        :issue:`20003`::

            sage: P.<x> = GF(7)[]
            sage: (6*x+3).squarefree_decomposition()
            (6) * (x + 4)

        Test zero polynomial::

            sage: R.<x> = PolynomialRing(GF(65537), implementation="FLINT")
            sage: R.zero().squarefree_decomposition()
            Traceback (most recent call last):
            ...
            ArithmeticError: square-free decomposition of 0 is not defined'''
    @overload
    def squarefree_decomposition(self) -> Any:
        '''Polynomial_zmod_flint.squarefree_decomposition(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 739)

        Return the squarefree decomposition of this polynomial.

        EXAMPLES::

            sage: R.<x> = GF(5)[]
            sage: ((x+1)*(x^2+1)^2*x^3).squarefree_decomposition()
            (x + 1) * (x^2 + 1)^2 * x^3

        TESTS::

            sage: (2*x*(x+1)^2).squarefree_decomposition()
            (2) * x * (x + 1)^2
            sage: P.<x> = Zmod(10)[]
            sage: (x^2).squarefree_decomposition()
            Traceback (most recent call last):
            ...
            NotImplementedError: square free factorization of polynomials over rings with composite characteristic is not implemented

        :issue:`20003`::

            sage: P.<x> = GF(7)[]
            sage: (6*x+3).squarefree_decomposition()
            (6) * (x + 4)

        Test zero polynomial::

            sage: R.<x> = PolynomialRing(GF(65537), implementation="FLINT")
            sage: R.zero().squarefree_decomposition()
            Traceback (most recent call last):
            ...
            ArithmeticError: square-free decomposition of 0 is not defined'''
    def __call__(self, *x, **kwds) -> Any:
        """Polynomial_zmod_flint.__call__(self, *x, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 268)

        Evaluate polynomial at x=a.

        INPUT: **either**

        - ``a`` -- ring element; need not be in the coefficient ring of the
          polynomial
        - a dictionary for kwds:value pairs; if the variable name of the
          polynomial is a keyword it is substituted in, otherwise this
          polynomial is returned unchanged

        EXAMPLES::

            sage: P.<x> = PolynomialRing(GF(7))
            sage: f = x^2 + 1
            sage: f(0)
            1
            sage: f(2)
            5
            sage: f(3)
            3

            sage: f(x+1)
            x^2 + 2*x + 2

        Test some simple (but important) optimizations::

            sage: f(2) == f(P(2))
            True
            sage: f(x) is f
            True
            sage: f(1/x)
            (x^2 + 1)/x^2"""
    def __pow__(self, exp, modulus) -> Any:
        '''Polynomial_zmod_flint.__pow__(self, exp, modulus)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_zmod_flint.pyx (starting at line 481)

        Exponentiation of ``self``.

        If ``modulus`` is not ``None``, the exponentiation is performed
        modulo the polynomial ``modulus``.

        EXAMPLES::

            sage: R.<x> = GF(5)[]
            sage: pow(x+1, 5**50, x^5 + 4*x + 3)
            x + 1
            sage: pow(x+1, 5**64, x^5 + 4*x + 3)
            x + 4
            sage: pow(x, 5**64, x^5 + 4*x + 3)
            x + 3

        The modulus can have smaller degree than ``self``::

            sage: R.<x> = PolynomialRing(GF(5), implementation="FLINT")
            sage: pow(x^4, 6, x^2 + x + 1)
            1

        TESTS:

        Canonical coercion applies::

            sage: R.<x> = PolynomialRing(GF(5), implementation="FLINT")
            sage: x_ZZ = ZZ["x"].gen()
            sage: pow(x+1, 25, 2)
            0
            sage: pow(x+1, 4, x_ZZ^2 + x_ZZ + 1)
            4*x + 4
            sage: pow(x+1, int(4), x_ZZ^2 + x_ZZ + 1)
            4*x + 4
            sage: xx = polygen(GF(97))
            sage: pow(x + 1, 3, xx^3 + xx + 1)
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents: ...'''
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
