import sage.structure.element
from sage.arith.functions import lcm as lcm
from sage.arith.misc import gcd as gcd
from sage.categories.category import ZZ as ZZ
from sage.rings.infinity import infinity as infinity
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

class PuiseuxSeries(sage.structure.element.AlgebraElement):
    """PuiseuxSeries(parent, f, e=1)

    File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 116)

    A Puiseux series.

    .. MATH::

        \\sum_{n=-N}^\\infty a_n x^{n/e}

    It is stored as a Laurent series:

    .. MATH::

        \\sum_{n=-N}^\\infty a_n t^n

    where `t = x^{1/e}`.

    INPUT:

    - ``parent`` -- the parent ring

    - ``f`` -- one of the following types of inputs:

      * instance of :class:`PuiseuxSeries`
      * instance that can be coerced into the Laurent series ring of the parent

    - ``e`` -- integer (default: 1); the ramification index

    EXAMPLES::

        sage: R.<x> = PuiseuxSeriesRing(QQ)
        sage: p = x^(1/2) + x**3; p
        x^(1/2) + x^3
        sage: q = x**(1/2) - x**(-1/2)
        sage: r = q.add_bigoh(7/2); r
        -x^(-1/2) + x^(1/2) + O(x^(7/2))
        sage: r**2
        x^-1 - 2 + x + O(x^3)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, f, e=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 155)

                Initialize ``self``.

                TESTS::

                    sage: R.<x> = PuiseuxSeriesRing(QQ)
                    sage: p = x^(1/2) + x**3
                    sage: TestSuite(p).run()
        """
    def add_bigoh(self, prec) -> Any:
        """PuiseuxSeries.add_bigoh(self, prec)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 713)

        Return the truncated series at chosen precision ``prec``.

        INPUT:

        - ``prec`` -- the precision of the series as a rational number

        EXAMPLES::

            sage: R.<x> = PuiseuxSeriesRing(QQ)
            sage: p = x^(-7/2) + 3 + 5*x^(1/2) - 7*x**3
            sage: p.add_bigoh(2)
            x^(-7/2) + 3 + 5*x^(1/2) + O(x^2)
            sage: p.add_bigoh(0)
            x^(-7/2) + O(1)
            sage: p.add_bigoh(-1)
            x^(-7/2) + O(x^-1)

        .. NOTE::

            The precision passed to the method is adapted to the common
            ramification index::

                sage: R.<x> = PuiseuxSeriesRing(ZZ)
                sage: p = x**(-1/3) + 2*x**(1/5)
                sage: p.add_bigoh(1/2)
                x^(-1/3) + 2*x^(1/5) + O(x^(7/15))"""
    @overload
    def change_ring(self, R) -> Any:
        """PuiseuxSeries.change_ring(self, R)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 749)

        Return ``self`` over a the new ring ``R``.

        EXAMPLES::

            sage: R.<x> = PuiseuxSeriesRing(ZZ)
            sage: p = x^(-7/2) + 3 + 5*x^(1/2) - 7*x**3
            sage: q = p.change_ring(QQ); q
            x^(-7/2) + 3 + 5*x^(1/2) - 7*x^3
            sage: q.parent()
            Puiseux Series Ring in x over Rational Field"""
    @overload
    def change_ring(self, QQ) -> Any:
        """PuiseuxSeries.change_ring(self, R)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 749)

        Return ``self`` over a the new ring ``R``.

        EXAMPLES::

            sage: R.<x> = PuiseuxSeriesRing(ZZ)
            sage: p = x^(-7/2) + 3 + 5*x^(1/2) - 7*x**3
            sage: q = p.change_ring(QQ); q
            x^(-7/2) + 3 + 5*x^(1/2) - 7*x^3
            sage: q.parent()
            Puiseux Series Ring in x over Rational Field"""
    @overload
    def coefficients(self) -> Any:
        """PuiseuxSeries.coefficients(self)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 833)

        Return the list of coefficients.

        EXAMPLES::

            sage: R.<x> = PuiseuxSeriesRing(ZZ)
            sage: p = x^(3/4) + 2*x^(4/5) + 3* x^(5/6)
            sage: p.coefficients()
            [1, 2, 3]"""
    @overload
    def coefficients(self) -> Any:
        """PuiseuxSeries.coefficients(self)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 833)

        Return the list of coefficients.

        EXAMPLES::

            sage: R.<x> = PuiseuxSeriesRing(ZZ)
            sage: p = x^(3/4) + 2*x^(4/5) + 3* x^(5/6)
            sage: p.coefficients()
            [1, 2, 3]"""
    @overload
    def common_prec(self, p) -> Any:
        """PuiseuxSeries.common_prec(self, p)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 963)

        Return the minimum precision of `p` and ``self``.

        EXAMPLES::

            sage: R.<x> = PuiseuxSeriesRing(ZZ)
            sage: p = (x**(-1/3) + 2*x**3)**2
            sage: q5 = p.add_bigoh(5); q5
            x^(-2/3) + 4*x^(8/3) + O(x^5)
            sage: q7 = p.add_bigoh(7); q7
            x^(-2/3) + 4*x^(8/3) + 4*x^6 + O(x^7)
            sage: q5.common_prec(q7)
            5
            sage: q7.common_prec(q5)
            5"""
    @overload
    def common_prec(self, q7) -> Any:
        """PuiseuxSeries.common_prec(self, p)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 963)

        Return the minimum precision of `p` and ``self``.

        EXAMPLES::

            sage: R.<x> = PuiseuxSeriesRing(ZZ)
            sage: p = (x**(-1/3) + 2*x**3)**2
            sage: q5 = p.add_bigoh(5); q5
            x^(-2/3) + 4*x^(8/3) + O(x^5)
            sage: q7 = p.add_bigoh(7); q7
            x^(-2/3) + 4*x^(8/3) + 4*x^6 + O(x^7)
            sage: q5.common_prec(q7)
            5
            sage: q7.common_prec(q5)
            5"""
    @overload
    def common_prec(self, q5) -> Any:
        """PuiseuxSeries.common_prec(self, p)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 963)

        Return the minimum precision of `p` and ``self``.

        EXAMPLES::

            sage: R.<x> = PuiseuxSeriesRing(ZZ)
            sage: p = (x**(-1/3) + 2*x**3)**2
            sage: q5 = p.add_bigoh(5); q5
            x^(-2/3) + 4*x^(8/3) + O(x^5)
            sage: q7 = p.add_bigoh(7); q7
            x^(-2/3) + 4*x^(8/3) + 4*x^6 + O(x^7)
            sage: q5.common_prec(q7)
            5
            sage: q7.common_prec(q5)
            5"""
    @overload
    def degree(self) -> Any:
        """PuiseuxSeries.degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 872)

        Return the degree of ``self``.

        EXAMPLES::

            sage: P.<y> = PolynomialRing(GF(5))
            sage: R.<x> = PuiseuxSeriesRing(P)
            sage: p = 3*y*x**(-2/3) + 2*y**2*x**(1/5); p
            3*y*x^(-2/3) + 2*y^2*x^(1/5)
            sage: p.degree()
            1/5"""
    @overload
    def degree(self) -> Any:
        """PuiseuxSeries.degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 872)

        Return the degree of ``self``.

        EXAMPLES::

            sage: P.<y> = PolynomialRing(GF(5))
            sage: R.<x> = PuiseuxSeriesRing(P)
            sage: p = 3*y*x**(-2/3) + 2*y**2*x**(1/5); p
            3*y*x^(-2/3) + 2*y^2*x^(1/5)
            sage: p.degree()
            1/5"""
    @overload
    def exponents(self) -> Any:
        """PuiseuxSeries.exponents(self)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 846)

        Return the list of exponents.

        EXAMPLES::

            sage: R.<x> = PuiseuxSeriesRing(ZZ)
            sage: p = x^(3/4) + 2*x^(4/5) + 3* x^(5/6)
            sage: p.exponents()
            [3/4, 4/5, 5/6]"""
    @overload
    def exponents(self) -> Any:
        """PuiseuxSeries.exponents(self)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 846)

        Return the list of exponents.

        EXAMPLES::

            sage: R.<x> = PuiseuxSeriesRing(ZZ)
            sage: p = x^(3/4) + 2*x^(4/5) + 3* x^(5/6)
            sage: p.exponents()
            [3/4, 4/5, 5/6]"""
    def inverse(self) -> Any:
        """PuiseuxSeries.inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 1042)

        Return the inverse of ``self``.

        EXAMPLES::

            sage: R.<x> = PuiseuxSeriesRing(QQ)
            sage: p = x^(-7/2) + 3 + 5*x^(1/2) - 7*x**3
            sage: 1/p
            x^(7/2) - 3*x^7 - 5*x^(15/2) + 7*x^10 + 9*x^(21/2) + 30*x^11 +
            25*x^(23/2) + O(x^(27/2))"""
    @overload
    def is_monomial(self) -> Any:
        """PuiseuxSeries.is_monomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 797)

        Return whether ``self`` is a monomial.

        This is ``True`` if and only if ``self`` is `x^p` for
        some rational `p`.

        EXAMPLES::

            sage: R.<x> = PuiseuxSeriesRing(QQ)
            sage: p = x^(1/2) + 3/4 * x^(2/3)
            sage: p.is_monomial()
            False
            sage: q = x**(11/13)
            sage: q.is_monomial()
            True
            sage: q = 4*x**(11/13)
            sage: q.is_monomial()
            False"""
    @overload
    def is_monomial(self) -> Any:
        """PuiseuxSeries.is_monomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 797)

        Return whether ``self`` is a monomial.

        This is ``True`` if and only if ``self`` is `x^p` for
        some rational `p`.

        EXAMPLES::

            sage: R.<x> = PuiseuxSeriesRing(QQ)
            sage: p = x^(1/2) + 3/4 * x^(2/3)
            sage: p.is_monomial()
            False
            sage: q = x**(11/13)
            sage: q.is_monomial()
            True
            sage: q = 4*x**(11/13)
            sage: q.is_monomial()
            False"""
    @overload
    def is_monomial(self) -> Any:
        """PuiseuxSeries.is_monomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 797)

        Return whether ``self`` is a monomial.

        This is ``True`` if and only if ``self`` is `x^p` for
        some rational `p`.

        EXAMPLES::

            sage: R.<x> = PuiseuxSeriesRing(QQ)
            sage: p = x^(1/2) + 3/4 * x^(2/3)
            sage: p.is_monomial()
            False
            sage: q = x**(11/13)
            sage: q.is_monomial()
            True
            sage: q = 4*x**(11/13)
            sage: q.is_monomial()
            False"""
    @overload
    def is_monomial(self) -> Any:
        """PuiseuxSeries.is_monomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 797)

        Return whether ``self`` is a monomial.

        This is ``True`` if and only if ``self`` is `x^p` for
        some rational `p`.

        EXAMPLES::

            sage: R.<x> = PuiseuxSeriesRing(QQ)
            sage: p = x^(1/2) + 3/4 * x^(2/3)
            sage: p.is_monomial()
            False
            sage: q = x**(11/13)
            sage: q.is_monomial()
            True
            sage: q = 4*x**(11/13)
            sage: q.is_monomial()
            False"""
    @overload
    def is_unit(self) -> Any:
        """PuiseuxSeries.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 764)

        Return whether ``self`` is a unit.

        A Puiseux series is a unit if and only if its leading coefficient is.

        EXAMPLES::

            sage: R.<x> = PuiseuxSeriesRing(ZZ)
            sage: p = x^(-7/2) + 3 + 5*x^(1/2) - 7*x**3
            sage: p.is_unit()
            True
            sage: q = 4 * x^(-7/2) + 3 * x**4
            sage: q.is_unit()
            False"""
    @overload
    def is_unit(self) -> Any:
        """PuiseuxSeries.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 764)

        Return whether ``self`` is a unit.

        A Puiseux series is a unit if and only if its leading coefficient is.

        EXAMPLES::

            sage: R.<x> = PuiseuxSeriesRing(ZZ)
            sage: p = x^(-7/2) + 3 + 5*x^(1/2) - 7*x**3
            sage: p.is_unit()
            True
            sage: q = 4 * x^(-7/2) + 3 * x**4
            sage: q.is_unit()
            False"""
    @overload
    def is_unit(self) -> Any:
        """PuiseuxSeries.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 764)

        Return whether ``self`` is a unit.

        A Puiseux series is a unit if and only if its leading coefficient is.

        EXAMPLES::

            sage: R.<x> = PuiseuxSeriesRing(ZZ)
            sage: p = x^(-7/2) + 3 + 5*x^(1/2) - 7*x**3
            sage: p.is_unit()
            True
            sage: q = 4 * x^(-7/2) + 3 * x**4
            sage: q.is_unit()
            False"""
    @overload
    def is_zero(self) -> Any:
        """PuiseuxSeries.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 782)

        Return whether ``self`` is zero.

        EXAMPLES::

            sage: R.<x> = PuiseuxSeriesRing(QQ)
            sage: p = x^(1/2) + 3/4 * x^(2/3)
            sage: p.is_zero()
            False
            sage: R.zero().is_zero()
            True"""
    @overload
    def is_zero(self) -> Any:
        """PuiseuxSeries.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 782)

        Return whether ``self`` is zero.

        EXAMPLES::

            sage: R.<x> = PuiseuxSeriesRing(QQ)
            sage: p = x^(1/2) + 3/4 * x^(2/3)
            sage: p.is_zero()
            False
            sage: R.zero().is_zero()
            True"""
    @overload
    def is_zero(self) -> Any:
        """PuiseuxSeries.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 782)

        Return whether ``self`` is zero.

        EXAMPLES::

            sage: R.<x> = PuiseuxSeriesRing(QQ)
            sage: p = x^(1/2) + 3/4 * x^(2/3)
            sage: p.is_zero()
            False
            sage: R.zero().is_zero()
            True"""
    @overload
    def laurent_part(self) -> Any:
        """PuiseuxSeries.laurent_part(self)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 669)

        Return the underlying Laurent series.

        EXAMPLES::

            sage: R.<x> = PuiseuxSeriesRing(QQ)
            sage: p = x^(1/2) + 3/4 * x^(2/3)
            sage: p.laurent_part()
            x^3 + 3/4*x^4"""
    @overload
    def laurent_part(self) -> Any:
        """PuiseuxSeries.laurent_part(self)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 669)

        Return the underlying Laurent series.

        EXAMPLES::

            sage: R.<x> = PuiseuxSeriesRing(QQ)
            sage: p = x^(1/2) + 3/4 * x^(2/3)
            sage: p.laurent_part()
            x^3 + 3/4*x^4"""
    @overload
    def laurent_series(self) -> Any:
        """PuiseuxSeries.laurent_series(self)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 999)

        If ``self`` is a Laurent series, return it as a Laurent series.

        EXAMPLES::

            sage: R.<x> = PuiseuxSeriesRing(ZZ)
            sage: p = x**(1/2) - x**(-1/2)
            sage: p.laurent_series()
            Traceback (most recent call last):
            ...
            ArithmeticError: self is not a Laurent series
            sage: q = p**2
            sage: q.laurent_series()
            x^-1 - 2 + x"""
    @overload
    def laurent_series(self) -> Any:
        """PuiseuxSeries.laurent_series(self)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 999)

        If ``self`` is a Laurent series, return it as a Laurent series.

        EXAMPLES::

            sage: R.<x> = PuiseuxSeriesRing(ZZ)
            sage: p = x**(1/2) - x**(-1/2)
            sage: p.laurent_series()
            Traceback (most recent call last):
            ...
            ArithmeticError: self is not a Laurent series
            sage: q = p**2
            sage: q.laurent_series()
            x^-1 - 2 + x"""
    @overload
    def laurent_series(self) -> Any:
        """PuiseuxSeries.laurent_series(self)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 999)

        If ``self`` is a Laurent series, return it as a Laurent series.

        EXAMPLES::

            sage: R.<x> = PuiseuxSeriesRing(ZZ)
            sage: p = x**(1/2) - x**(-1/2)
            sage: p.laurent_series()
            Traceback (most recent call last):
            ...
            ArithmeticError: self is not a Laurent series
            sage: q = p**2
            sage: q.laurent_series()
            x^-1 - 2 + x"""
    @overload
    def list(self) -> Any:
        """PuiseuxSeries.list(self)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 819)

        Return the list of coefficients indexed by the exponents of the
        the corresponding Laurent series.

        EXAMPLES::

            sage: R.<x> = PuiseuxSeriesRing(ZZ)
            sage: p = x^(3/4) + 2*x^(4/5) + 3* x^(5/6)
            sage: p.list()
            [1, 0, 0, 2, 0, 3]"""
    @overload
    def list(self) -> Any:
        """PuiseuxSeries.list(self)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 819)

        Return the list of coefficients indexed by the exponents of the
        the corresponding Laurent series.

        EXAMPLES::

            sage: R.<x> = PuiseuxSeriesRing(ZZ)
            sage: p = x^(3/4) + 2*x^(4/5) + 3* x^(5/6)
            sage: p.list()
            [1, 0, 0, 2, 0, 3]"""
    @overload
    def power_series(self) -> Any:
        """PuiseuxSeries.power_series(self)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 1019)

        If ``self`` is a power series, return it as a power series.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<x> = PuiseuxSeriesRing(QQbar)
            sage: p = x**(3/2) - QQbar(I)*x**(1/2)
            sage: p.power_series()
            Traceback (most recent call last):
            ...
            ArithmeticError: self is not a power series
            sage: q = p**2
            sage: q.power_series()
            -x - 2*I*x^2 + x^3"""
    @overload
    def power_series(self) -> Any:
        """PuiseuxSeries.power_series(self)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 1019)

        If ``self`` is a power series, return it as a power series.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<x> = PuiseuxSeriesRing(QQbar)
            sage: p = x**(3/2) - QQbar(I)*x**(1/2)
            sage: p.power_series()
            Traceback (most recent call last):
            ...
            ArithmeticError: self is not a power series
            sage: q = p**2
            sage: q.power_series()
            -x - 2*I*x^2 + x^3"""
    @overload
    def power_series(self) -> Any:
        """PuiseuxSeries.power_series(self)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 1019)

        If ``self`` is a power series, return it as a power series.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<x> = PuiseuxSeriesRing(QQbar)
            sage: p = x**(3/2) - QQbar(I)*x**(1/2)
            sage: p.power_series()
            Traceback (most recent call last):
            ...
            ArithmeticError: self is not a power series
            sage: q = p**2
            sage: q.power_series()
            -x - 2*I*x^2 + x^3"""
    @overload
    def prec(self) -> Any:
        """PuiseuxSeries.prec(self)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 922)

        Return the precision of ``self``.

        EXAMPLES::

            sage: R.<x> = PuiseuxSeriesRing(ZZ)
            sage: p = (x**(-1/3) + 2*x**3)**2; p
            x^(-2/3) + 4*x^(8/3) + 4*x^6
            sage: q = p.add_bigoh(5); q
            x^(-2/3) + 4*x^(8/3) + O(x^5)
            sage: q.prec()
            5"""
    @overload
    def prec(self) -> Any:
        """PuiseuxSeries.prec(self)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 922)

        Return the precision of ``self``.

        EXAMPLES::

            sage: R.<x> = PuiseuxSeriesRing(ZZ)
            sage: p = (x**(-1/3) + 2*x**3)**2; p
            x^(-2/3) + 4*x^(8/3) + 4*x^6
            sage: q = p.add_bigoh(5); q
            x^(-2/3) + 4*x^(8/3) + O(x^5)
            sage: q.prec()
            5"""
    def precision_absolute(self, *args, **kwargs):
        """PuiseuxSeries.prec(self)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 922)

        Return the precision of ``self``.

        EXAMPLES::

            sage: R.<x> = PuiseuxSeriesRing(ZZ)
            sage: p = (x**(-1/3) + 2*x**3)**2; p
            x^(-2/3) + 4*x^(8/3) + 4*x^6
            sage: q = p.add_bigoh(5); q
            x^(-2/3) + 4*x^(8/3) + O(x^5)
            sage: q.prec()
            5"""
    @overload
    def precision_relative(self) -> Any:
        """PuiseuxSeries.precision_relative(self)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 942)

        Return the relative precision of the series.

        The relative precision of the Puiseux series is the difference
        between its absolute precision and its valuation.

        EXAMPLES::

            sage: R.<x> = PuiseuxSeriesRing(GF(3))
            sage: p = (x**(-1/3) + 2*x**3)**2; p
            x^(-2/3) + x^(8/3) + x^6
            sage: q = p.add_bigoh(7); q
            x^(-2/3) + x^(8/3) + x^6 + O(x^7)
            sage: q.precision_relative()
            23/3"""
    @overload
    def precision_relative(self) -> Any:
        """PuiseuxSeries.precision_relative(self)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 942)

        Return the relative precision of the series.

        The relative precision of the Puiseux series is the difference
        between its absolute precision and its valuation.

        EXAMPLES::

            sage: R.<x> = PuiseuxSeriesRing(GF(3))
            sage: p = (x**(-1/3) + 2*x**3)**2; p
            x^(-2/3) + x^(8/3) + x^6
            sage: q = p.add_bigoh(7); q
            x^(-2/3) + x^(8/3) + x^6 + O(x^7)
            sage: q.precision_relative()
            23/3"""
    @overload
    def ramification_index(self) -> Any:
        """PuiseuxSeries.ramification_index(self)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 682)

        Return the ramification index.

        EXAMPLES::

            sage: R.<x> = PuiseuxSeriesRing(QQ)
            sage: p = x^(1/2) + 3/4 * x^(2/3)
            sage: p.ramification_index()
            6"""
    @overload
    def ramification_index(self) -> Any:
        """PuiseuxSeries.ramification_index(self)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 682)

        Return the ramification index.

        EXAMPLES::

            sage: R.<x> = PuiseuxSeriesRing(QQ)
            sage: p = x^(1/2) + 3/4 * x^(2/3)
            sage: p.ramification_index()
            6"""
    def shift(self, r) -> Any:
        """PuiseuxSeries.shift(self, r)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 887)

        Return this Puiseux series multiplied by `x^r`.

        EXAMPLES::

            sage: P.<y> = LaurentPolynomialRing(ZZ)
            sage: R.<x> = PuiseuxSeriesRing(P)
            sage: p = y*x**(-1/3) + 2*y^(-2)*x**(1/2); p
            y*x^(-1/3) + (2*y^-2)*x^(1/2)
            sage: p.shift(3)
            y*x^(8/3) + (2*y^-2)*x^(7/2)"""
    def truncate(self, r) -> Any:
        """PuiseuxSeries.truncate(self, r)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 903)

        Return the Puiseux series of degree `< r`.

        This is equivalent to ``self`` modulo `x^r`.

        EXAMPLES::

            sage: R.<x> = PuiseuxSeriesRing(ZZ)
            sage: p = (x**(-1/3) + 2*x**3)**2; p
            x^(-2/3) + 4*x^(8/3) + 4*x^6
            sage: q = p.truncate(5); q
            x^(-2/3) + 4*x^(8/3)
            sage: q == p.add_bigoh(5)
            True"""
    @overload
    def valuation(self) -> Any:
        """PuiseuxSeries.valuation(self)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 695)

        Return the valuation of ``self``.

        EXAMPLES::

            sage: R.<x> = PuiseuxSeriesRing(QQ)
            sage: p = x^(-7/2) + 3 + 5*x^(1/2) - 7*x**3
            sage: p.valuation()
            -7/2

        TESTS::

            sage: R.zero().valuation()
            +Infinity"""
    @overload
    def valuation(self) -> Any:
        """PuiseuxSeries.valuation(self)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 695)

        Return the valuation of ``self``.

        EXAMPLES::

            sage: R.<x> = PuiseuxSeriesRing(QQ)
            sage: p = x^(-7/2) + 3 + 5*x^(1/2) - 7*x**3
            sage: p.valuation()
            -7/2

        TESTS::

            sage: R.zero().valuation()
            +Infinity"""
    @overload
    def valuation(self) -> Any:
        """PuiseuxSeries.valuation(self)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 695)

        Return the valuation of ``self``.

        EXAMPLES::

            sage: R.<x> = PuiseuxSeriesRing(QQ)
            sage: p = x^(-7/2) + 3 + 5*x^(1/2) - 7*x**3
            sage: p.valuation()
            -7/2

        TESTS::

            sage: R.zero().valuation()
            +Infinity"""
    @overload
    def variable(self) -> Any:
        """PuiseuxSeries.variable(self)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 986)

        Return the variable of ``self``.

        EXAMPLES::

            sage: R.<x> = PuiseuxSeriesRing(QQ)
            sage: p = x^(-7/2) + 3 + 5*x^(1/2) - 7*x**3
            sage: p.variable()
            'x'"""
    @overload
    def variable(self) -> Any:
        """PuiseuxSeries.variable(self)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 986)

        Return the variable of ``self``.

        EXAMPLES::

            sage: R.<x> = PuiseuxSeriesRing(QQ)
            sage: p = x^(-7/2) + 3 + 5*x^(1/2) - 7*x**3
            sage: p.variable()
            'x'"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __call__(self, x) -> Any:
        """PuiseuxSeries.__call__(self, x)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 290)

        Evaluate this Puiseux series.

        INPUT:

        - ``x`` -- element of a ring

        EXAMPLES::

            sage: R.<x> = PuiseuxSeriesRing(QQ)
            sage: p = x^(1/2) + x**3-x**(-1/4)
            sage: p(16)
            8199/2
            sage: p(pi.n())                                                             # needs sage.symbolic
            32.0276049867404"""
    def __copy__(self) -> Any:
        """PuiseuxSeries.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 652)

        Since this is immutable, return ``self``.

        EXAMPLES::

            sage: R.<x> = PuiseuxSeriesRing(ZZ)
            sage: p = x^(3/4) + 2*x^(4/5) + 3* x^(5/6)
            sage: p2 = copy(p); p2
            x^(3/4) + 2*x^(4/5) + 3*x^(5/6)
            sage: p == p2
            True
            sage: p is p2
            True"""
    def __delitem__(self, other) -> None:
        """Delete self[key]."""
    def __getitem__(self, r) -> Any:
        """PuiseuxSeries.__getitem__(self, r)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 612)

        Return the coefficient with exponent ``r``.

        EXAMPLES::

            sage: R.<x> = PuiseuxSeriesRing(QQ)
            sage: p = x^(-7/2) + 3 + 5*x^(1/2) - 7*x**3
            sage: p[-7/2]
            1
            sage: p[0]
            3
            sage: p[1/2]
            5
            sage: p[3]
            -7
            sage: p[100]
            0"""
    def __hash__(self) -> Any:
        """PuiseuxSeries.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 598)

        Return a hash of ``self``.

        EXAMPLES::

            sage: from operator import xor
            sage: R.<x> = PuiseuxSeriesRing(QQ)
            sage: p = x^(-7/2) + 3 + 5*x^(1/2) - 7*x**3
            sage: hash(p) == xor(hash(p.laurent_part()), 2)  # indirect doctest
            True"""
    def __iter__(self) -> Any:
        """PuiseuxSeries.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 639)

        Return an iterator over the coefficients.

        EXAMPLES::

            sage: R.<x> = PuiseuxSeriesRing(QQ)
            sage: p = x^(-7/2) + 3 + 5*x^(1/2) - 7*x**3
            sage: list(p)
            [1, 0, 0, 0, 0, 0, 0, 3, 5, 0, 0, 0, 0, -7]"""
    def __lshift__(self, r) -> Any:
        """PuiseuxSeries.__lshift__(self, r)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 555)

        Apply :meth:`shift` using the operator `<<`.

        EXAMPLES::

            sage: P.<y> = LaurentPolynomialRing(ZZ)
            sage: R.<x> = PuiseuxSeriesRing(P)
            sage: p = y*x**(-1/3) + 2*y^(-2)*x**(1/2)
            sage: p << 1/3                             # indirect doctest
            y + (2*y^-2)*x^(5/6)"""
    def __pow__(self, _self, r, dummy) -> Any:
        """PuiseuxSeries.__pow__(_self, r, dummy)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 480)

        Return the power.

        EXAMPLES::

            sage: R.<x> = PuiseuxSeriesRing(QQ)
            sage: p = x^(1/2) + 3/4 * x^(2/3)
            sage: p ** 3
            x^(3/2) + 9/4*x^(5/3) + 27/16*x^(11/6) + 27/64*x^2"""
    def __reduce__(self) -> Any:
        """PuiseuxSeries.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 206)

        EXAMPLES::

            sage: R.<x> = PuiseuxSeriesRing(ZZ)
            sage: p = x^(1/2) + x**3-x**(-1/4)
            sage: loads(dumps(p)) == p    # indirect doctest
            True"""
    def __rlshift__(self, other):
        """Return value<<self."""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
    def __rrshift__(self, other):
        """Return value>>self."""
    def __rshift__(self, r) -> Any:
        """PuiseuxSeries.__rshift__(self, r)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 569)

        Apply :meth:`shift` with negative argument using the operator `>>`.

        EXAMPLES::

            sage: P.<y> = LaurentPolynomialRing(ZZ)
            sage: R.<x> = PuiseuxSeriesRing(P)
            sage: p = y*x**(-1/3) + 2*y^(-2)*x**(1/2)
            sage: p >> 1/3                             # indirect doctest
            y*x^(-2/3) + (2*y^-2)*x^(1/6)"""
    def __setitem__(self, n, value) -> Any:
        """PuiseuxSeries.__setitem__(self, n, value)

        File: /build/sagemath/src/sage/src/sage/rings/puiseux_series_ring_element.pyx (starting at line 859)

        EXAMPLES::

            sage: R.<t> = PuiseuxSeriesRing(QQ)
            sage: f = t^2 + t^3 + O(t^10)
            sage: f[2] = 5
            Traceback (most recent call last):
            ...
            IndexError: Puiseux series are immutable"""
