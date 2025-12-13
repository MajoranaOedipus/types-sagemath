import _cython_3_2_1
import cypari2.pari_instance
import sage.rings.polynomial.polynomial_element
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.fraction_field_element import FractionFieldElement as FractionFieldElement
from sage.structure.element import coerce_binop as coerce_binop, have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

GF2X_BuildIrred_list: _cython_3_2_1.cython_function_or_method
GF2X_BuildRandomIrred_list: _cython_3_2_1.cython_function_or_method
GF2X_BuildSparseIrred_list: _cython_3_2_1.cython_function_or_method
make_element: _cython_3_2_1.cython_function_or_method
pari: cypari2.pari_instance.Pari

class Polynomial_GF2X(Polynomial_template):
    """Polynomial_GF2X(parent, x=None, check=True, is_gen=False, construct=False)

    File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_gf2x.pyx (starting at line 36)

    Univariate Polynomials over `\\GF{2}` via NTL's GF2X.

    EXAMPLES::

        sage: P.<x> = GF(2)[]
        sage: x^3 + x^2 + 1
        x^3 + x^2 + 1"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, x=..., check=..., is_gen=..., construct=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_gf2x.pyx (starting at line 46)

                Create a new univariate polynomials over `\\GF{2}`.

                EXAMPLES::

                    sage: P.<x> = GF(2)[]
                    sage: x^3 + x^2 + 1
                    x^3 + x^2 + 1

                We check that the bug noted at :issue:`12724` is fixed::

                    sage: R.<x> = Zmod(2)[]
                    sage: R([2^80])
                    0
        """
    def compose_mod(self, *args, **kwargs):
        """Polynomial_GF2X.modular_composition(self, Polynomial_GF2X g, Polynomial_GF2X h, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_gf2x.pyx (starting at line 109)

        Compute `f(g) \\pmod h`.

        Both implementations use Brent-Kung's Algorithm 2.1 (*Fast Algorithms
        for Manipulation of Formal Power Series*, JACM 1978).

        INPUT:

        - ``g`` -- a polynomial
        - ``h`` -- a polynomial
        - ``algorithm`` -- either ``'native'`` or ``'ntl'`` (default: ``'native'``)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: r = 279
            sage: f = x^r + x +1
            sage: g = x^r
            sage: g.modular_composition(g, f) == g(g) % f
            True

            sage: P.<x> = GF(2)[]
            sage: f = x^29 + x^24 + x^22 + x^21 + x^20 + x^16 + x^15 + x^14 + x^10 + x^9 + x^8 + x^7 + x^6 + x^5 + x^2
            sage: g = x^31 + x^30 + x^28 + x^26 + x^24 + x^21 + x^19 + x^18 + x^11 + x^10 + x^9 + x^8 + x^5 + x^2 + 1
            sage: h = x^30 + x^28 + x^26 + x^25 + x^24 + x^22 + x^21 + x^18 + x^17 + x^15 + x^13 + x^12 + x^11 + x^10 + x^9 + x^4
            sage: f.modular_composition(g, h) == f(g) % h
            True

        AUTHORS:

        - Paul Zimmermann (2008-10) initial implementation
        - Martin Albrecht (2008-10) performance improvements"""
    def is_irreducible(self) -> Any:
        """Polynomial_GF2X.is_irreducible(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_gf2x.pyx (starting at line 268)

        Return whether this polynomial is irreducible over `\\GF{2}`.

        EXAMPLES::

            sage: R.<x> = GF(2)[]
            sage: (x^2 + 1).is_irreducible()
            False
            sage: (x^3 + x + 1).is_irreducible()
            True

        Test that caching works::

            sage: R.<x> = GF(2)[]
            sage: f = x^2 + 1
            sage: f.is_irreducible()
            False
            sage: f.is_irreducible.cache
            False"""
    def modular_composition(self, Polynomial_GF2Xg, Polynomial_GF2Xh, algorithm=...) -> Any:
        """Polynomial_GF2X.modular_composition(self, Polynomial_GF2X g, Polynomial_GF2X h, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_gf2x.pyx (starting at line 109)

        Compute `f(g) \\pmod h`.

        Both implementations use Brent-Kung's Algorithm 2.1 (*Fast Algorithms
        for Manipulation of Formal Power Series*, JACM 1978).

        INPUT:

        - ``g`` -- a polynomial
        - ``h`` -- a polynomial
        - ``algorithm`` -- either ``'native'`` or ``'ntl'`` (default: ``'native'``)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: r = 279
            sage: f = x^r + x +1
            sage: g = x^r
            sage: g.modular_composition(g, f) == g(g) % f
            True

            sage: P.<x> = GF(2)[]
            sage: f = x^29 + x^24 + x^22 + x^21 + x^20 + x^16 + x^15 + x^14 + x^10 + x^9 + x^8 + x^7 + x^6 + x^5 + x^2
            sage: g = x^31 + x^30 + x^28 + x^26 + x^24 + x^21 + x^19 + x^18 + x^11 + x^10 + x^9 + x^8 + x^5 + x^2 + 1
            sage: h = x^30 + x^28 + x^26 + x^25 + x^24 + x^22 + x^21 + x^18 + x^17 + x^15 + x^13 + x^12 + x^11 + x^10 + x^9 + x^4
            sage: f.modular_composition(g, h) == f(g) % h
            True

        AUTHORS:

        - Paul Zimmermann (2008-10) initial implementation
        - Martin Albrecht (2008-10) performance improvements"""
    def __pari__(self, variable=...) -> Any:
        """Polynomial_GF2X.__pari__(self, variable=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_gf2x.pyx (starting at line 94)

        EXAMPLES::

            sage: P.<x> = GF(2)[]
            sage: f = x^3 + x^2 + 1
            sage: pari(f)
            Mod(1, 2)*x^3 + Mod(1, 2)*x^2 + Mod(1, 2)"""

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
