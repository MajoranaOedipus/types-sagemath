import _cython_3_2_1
import sage as sage
import sage.structure.element
from sage.misc.derivative import multi_derivative as multi_derivative
from sage.rings.infinity import infinity as infinity
from sage.rings.polynomial.laurent_polynomial import LaurentPolynomial_univariate as LaurentPolynomial_univariate
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

is_LaurentSeries: _cython_3_2_1.cython_function_or_method

class LaurentSeries(sage.structure.element.AlgebraElement):
    """LaurentSeries(parent, f, n=0)

    File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 89)

    A Laurent Series.

    We consider a Laurent series of the form `f = t^n \\cdot u` where `u` is a
    power series with nonzero constant term.

    INPUT:

    - ``parent`` -- a Laurent series ring

    - ``f`` -- a power series (or something can be coerced
      to one); note that ``f`` does *not* have to be a unit

    - ``n`` -- (default: 0) integer"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, f, n=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 105)

                Initialize ``self``.

                OUTPUT: a Laurent series

                EXAMPLES::

                    sage: R.<q> = LaurentSeriesRing(ZZ)
                    sage: R([1,2,3])
                    1 + 2*q + 3*q^2
                    sage: R([1,2,3], -5)
                    q^-5 + 2*q^-4 + 3*q^-3

                ::

                    sage: # needs sage.rings.finite_rings sage.rings.padics
                    sage: S.<s> = LaurentSeriesRing(GF(5))
                    sage: T.<t> = PowerSeriesRing(pAdicRing(5))
                    sage: S(t)
                    s
                    sage: parent(S(t))
                    Laurent Series Ring in s over Finite Field of size 5
                    sage: parent(S(t)[1])
                    Finite Field of size 5
        """
    def O(self, prec) -> Any:
        """LaurentSeries.O(self, prec)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 865)

        Return the Laurent series of precision at most ``prec`` obtained by
        adding `O(q^\\text{prec})`, where `q` is the variable.

        The precision of ``self`` and the integer ``prec`` can be arbitrary. The
        resulting Laurent series will have precision equal to the minimum of
        the precision of ``self`` and ``prec``. The term `O(q^\\text{prec})` is the
        zero series with precision ``prec``.

        See also :meth:`add_bigoh`.

        EXAMPLES::

            sage: R.<t> = LaurentSeriesRing(QQ)
            sage: f = t^-5 + t^-4 + t^3 + O(t^10); f
            t^-5 + t^-4 + t^3 + O(t^10)
            sage: f.O(-4)
            t^-5 + O(t^-4)
            sage: f.O(15)
            t^-5 + t^-4 + t^3 + O(t^10)"""
    def V(self, *args, **kwargs):
        """LaurentSeries.verschiebung(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 375)

        Return the ``n``-th Verschiebung of ``self``.

        If `f = \\sum a_m x^m` then this function returns `\\sum a_m x^{mn}`.

        EXAMPLES::

            sage: R.<x> = LaurentSeriesRing(QQ)
            sage: f = -1/x + 1 + 2*x^2 + 5*x^5
            sage: f.V(2)
            -x^-2 + 1 + 2*x^4 + 5*x^10
            sage: f.V(-1)
            5*x^-5 + 2*x^-2 + 1 - x
            sage: h = f.add_bigoh(7)
            sage: h.V(2)
            -x^-2 + 1 + 2*x^4 + 5*x^10 + O(x^14)
            sage: h.V(-2)
            Traceback (most recent call last):
            ...
            ValueError: For finite precision only positive arguments allowed

        TESTS::

            sage: R.<x> = LaurentSeriesRing(QQ)
            sage: f = x
            sage: f.V(3)
            x^3
            sage: f.V(-3)
            x^-3
            sage: g = 2*x^(-1) + 3 + 5*x
            sage: g.V(-1)
            5*x^-1 + 3 + 2*x"""
    def add_bigoh(self, prec) -> Any:
        """LaurentSeries.add_bigoh(self, prec)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 828)

        Return the truncated series at chosen precision ``prec``.

        See also :meth:`O`.

        INPUT:

        - ``prec`` -- the precision of the series as an integer

        EXAMPLES::

            sage: R.<t> = LaurentSeriesRing(QQ)
            sage: f = t^2 + t^3 + O(t^10); f
            t^2 + t^3 + O(t^10)
            sage: f.add_bigoh(5)
            t^2 + t^3 + O(t^5)

        TESTS:

        Check that :issue:`28239` is fixed::

            sage: (t^(-2)).add_bigoh(-1)
            t^-2 + O(t^-1)
            sage: (t^(-2)).add_bigoh(-2)
            O(t^-2)
            sage: (t^(-2)).add_bigoh(-3)
            O(t^-3)"""
    def change_ring(self, R) -> Any:
        """LaurentSeries.change_ring(self, R)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 180)

        Change the base ring of ``self``.

        EXAMPLES::

            sage: R.<q> = LaurentSeriesRing(ZZ)
            sage: p = R([1,2,3]); p
            1 + 2*q + 3*q^2
            sage: p.change_ring(GF(2))
            1 + q^2"""
    @overload
    def coefficients(self) -> Any:
        """LaurentSeries.coefficients(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 588)

        Return the nonzero coefficients of ``self``.

        EXAMPLES::

            sage: R.<t> = LaurentSeriesRing(QQ)
            sage: f = -5/t^(2) + t + t^2 - 10/3*t^3
            sage: f.coefficients()
            [-5, 1, 1, -10/3]"""
    @overload
    def coefficients(self) -> Any:
        """LaurentSeries.coefficients(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 588)

        Return the nonzero coefficients of ``self``.

        EXAMPLES::

            sage: R.<t> = LaurentSeriesRing(QQ)
            sage: f = -5/t^(2) + t + t^2 - 10/3*t^3
            sage: f.coefficients()
            [-5, 1, 1, -10/3]"""
    @overload
    def common_prec(self, other) -> Any:
        """LaurentSeries.common_prec(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1127)

        Return the minimum precision of ``self`` and ``other``.

        EXAMPLES::

            sage: R.<t> = LaurentSeriesRing(QQ)

        ::

            sage: f = t^(-1) + t + t^2 + O(t^3)
            sage: g = t + t^3 + t^4 + O(t^4)
            sage: f.common_prec(g)
            3
            sage: g.common_prec(f)
            3

        ::

            sage: f = t + t^2 + O(t^3)
            sage: g = t^(-3) + t^2
            sage: f.common_prec(g)
            3
            sage: g.common_prec(f)
            3

        ::

            sage: f = t + t^2
            sage: g = t^2
            sage: f.common_prec(g)
            +Infinity

        ::

            sage: f = t^(-3) + O(t^(-2))
            sage: g = t^(-5) + O(t^(-1))
            sage: f.common_prec(g)
            -2

        ::

            sage: f = O(t^2)
            sage: g = O(t^5)
            sage: f.common_prec(g)
            2"""
    @overload
    def common_prec(self, g) -> Any:
        """LaurentSeries.common_prec(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1127)

        Return the minimum precision of ``self`` and ``other``.

        EXAMPLES::

            sage: R.<t> = LaurentSeriesRing(QQ)

        ::

            sage: f = t^(-1) + t + t^2 + O(t^3)
            sage: g = t + t^3 + t^4 + O(t^4)
            sage: f.common_prec(g)
            3
            sage: g.common_prec(f)
            3

        ::

            sage: f = t + t^2 + O(t^3)
            sage: g = t^(-3) + t^2
            sage: f.common_prec(g)
            3
            sage: g.common_prec(f)
            3

        ::

            sage: f = t + t^2
            sage: g = t^2
            sage: f.common_prec(g)
            +Infinity

        ::

            sage: f = t^(-3) + O(t^(-2))
            sage: g = t^(-5) + O(t^(-1))
            sage: f.common_prec(g)
            -2

        ::

            sage: f = O(t^2)
            sage: g = O(t^5)
            sage: f.common_prec(g)
            2"""
    @overload
    def common_prec(self, f) -> Any:
        """LaurentSeries.common_prec(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1127)

        Return the minimum precision of ``self`` and ``other``.

        EXAMPLES::

            sage: R.<t> = LaurentSeriesRing(QQ)

        ::

            sage: f = t^(-1) + t + t^2 + O(t^3)
            sage: g = t + t^3 + t^4 + O(t^4)
            sage: f.common_prec(g)
            3
            sage: g.common_prec(f)
            3

        ::

            sage: f = t + t^2 + O(t^3)
            sage: g = t^(-3) + t^2
            sage: f.common_prec(g)
            3
            sage: g.common_prec(f)
            3

        ::

            sage: f = t + t^2
            sage: g = t^2
            sage: f.common_prec(g)
            +Infinity

        ::

            sage: f = t^(-3) + O(t^(-2))
            sage: g = t^(-5) + O(t^(-1))
            sage: f.common_prec(g)
            -2

        ::

            sage: f = O(t^2)
            sage: g = O(t^5)
            sage: f.common_prec(g)
            2"""
    @overload
    def common_prec(self, g) -> Any:
        """LaurentSeries.common_prec(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1127)

        Return the minimum precision of ``self`` and ``other``.

        EXAMPLES::

            sage: R.<t> = LaurentSeriesRing(QQ)

        ::

            sage: f = t^(-1) + t + t^2 + O(t^3)
            sage: g = t + t^3 + t^4 + O(t^4)
            sage: f.common_prec(g)
            3
            sage: g.common_prec(f)
            3

        ::

            sage: f = t + t^2 + O(t^3)
            sage: g = t^(-3) + t^2
            sage: f.common_prec(g)
            3
            sage: g.common_prec(f)
            3

        ::

            sage: f = t + t^2
            sage: g = t^2
            sage: f.common_prec(g)
            +Infinity

        ::

            sage: f = t^(-3) + O(t^(-2))
            sage: g = t^(-5) + O(t^(-1))
            sage: f.common_prec(g)
            -2

        ::

            sage: f = O(t^2)
            sage: g = O(t^5)
            sage: f.common_prec(g)
            2"""
    @overload
    def common_prec(self, f) -> Any:
        """LaurentSeries.common_prec(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1127)

        Return the minimum precision of ``self`` and ``other``.

        EXAMPLES::

            sage: R.<t> = LaurentSeriesRing(QQ)

        ::

            sage: f = t^(-1) + t + t^2 + O(t^3)
            sage: g = t + t^3 + t^4 + O(t^4)
            sage: f.common_prec(g)
            3
            sage: g.common_prec(f)
            3

        ::

            sage: f = t + t^2 + O(t^3)
            sage: g = t^(-3) + t^2
            sage: f.common_prec(g)
            3
            sage: g.common_prec(f)
            3

        ::

            sage: f = t + t^2
            sage: g = t^2
            sage: f.common_prec(g)
            +Infinity

        ::

            sage: f = t^(-3) + O(t^(-2))
            sage: g = t^(-5) + O(t^(-1))
            sage: f.common_prec(g)
            -2

        ::

            sage: f = O(t^2)
            sage: g = O(t^5)
            sage: f.common_prec(g)
            2"""
    @overload
    def common_prec(self, g) -> Any:
        """LaurentSeries.common_prec(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1127)

        Return the minimum precision of ``self`` and ``other``.

        EXAMPLES::

            sage: R.<t> = LaurentSeriesRing(QQ)

        ::

            sage: f = t^(-1) + t + t^2 + O(t^3)
            sage: g = t + t^3 + t^4 + O(t^4)
            sage: f.common_prec(g)
            3
            sage: g.common_prec(f)
            3

        ::

            sage: f = t + t^2 + O(t^3)
            sage: g = t^(-3) + t^2
            sage: f.common_prec(g)
            3
            sage: g.common_prec(f)
            3

        ::

            sage: f = t + t^2
            sage: g = t^2
            sage: f.common_prec(g)
            +Infinity

        ::

            sage: f = t^(-3) + O(t^(-2))
            sage: g = t^(-5) + O(t^(-1))
            sage: f.common_prec(g)
            -2

        ::

            sage: f = O(t^2)
            sage: g = O(t^5)
            sage: f.common_prec(g)
            2"""
    @overload
    def common_prec(self, g) -> Any:
        """LaurentSeries.common_prec(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1127)

        Return the minimum precision of ``self`` and ``other``.

        EXAMPLES::

            sage: R.<t> = LaurentSeriesRing(QQ)

        ::

            sage: f = t^(-1) + t + t^2 + O(t^3)
            sage: g = t + t^3 + t^4 + O(t^4)
            sage: f.common_prec(g)
            3
            sage: g.common_prec(f)
            3

        ::

            sage: f = t + t^2 + O(t^3)
            sage: g = t^(-3) + t^2
            sage: f.common_prec(g)
            3
            sage: g.common_prec(f)
            3

        ::

            sage: f = t + t^2
            sage: g = t^2
            sage: f.common_prec(g)
            +Infinity

        ::

            sage: f = t^(-3) + O(t^(-2))
            sage: g = t^(-5) + O(t^(-1))
            sage: f.common_prec(g)
            -2

        ::

            sage: f = O(t^2)
            sage: g = O(t^5)
            sage: f.common_prec(g)
            2"""
    @overload
    def common_prec(self, g) -> Any:
        """LaurentSeries.common_prec(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1127)

        Return the minimum precision of ``self`` and ``other``.

        EXAMPLES::

            sage: R.<t> = LaurentSeriesRing(QQ)

        ::

            sage: f = t^(-1) + t + t^2 + O(t^3)
            sage: g = t + t^3 + t^4 + O(t^4)
            sage: f.common_prec(g)
            3
            sage: g.common_prec(f)
            3

        ::

            sage: f = t + t^2 + O(t^3)
            sage: g = t^(-3) + t^2
            sage: f.common_prec(g)
            3
            sage: g.common_prec(f)
            3

        ::

            sage: f = t + t^2
            sage: g = t^2
            sage: f.common_prec(g)
            +Infinity

        ::

            sage: f = t^(-3) + O(t^(-2))
            sage: g = t^(-5) + O(t^(-1))
            sage: f.common_prec(g)
            -2

        ::

            sage: f = O(t^2)
            sage: g = O(t^5)
            sage: f.common_prec(g)
            2"""
    @overload
    def common_valuation(self, other) -> Any:
        """LaurentSeries.common_valuation(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1176)

        Return the minimum valuation of ``self`` and ``other``.

        EXAMPLES::

            sage: R.<t> = LaurentSeriesRing(QQ)

        ::

            sage: f = t^(-1) + t + t^2 + O(t^3)
            sage: g = t + t^3 + t^4 + O(t^4)
            sage: f.common_valuation(g)
            -1
            sage: g.common_valuation(f)
            -1

        ::

            sage: f = t + t^2 + O(t^3)
            sage: g = t^(-3) + t^2
            sage: f.common_valuation(g)
            -3
            sage: g.common_valuation(f)
            -3

        ::

            sage: f = t + t^2
            sage: g = t^2
            sage: f.common_valuation(g)
            1

        ::

            sage: f = t^(-3) + O(t^(-2))
            sage: g = t^(-5) + O(t^(-1))
            sage: f.common_valuation(g)
            -5

        ::

            sage: f = O(t^2)
            sage: g = O(t^5)
            sage: f.common_valuation(g)
            +Infinity"""
    @overload
    def common_valuation(self, g) -> Any:
        """LaurentSeries.common_valuation(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1176)

        Return the minimum valuation of ``self`` and ``other``.

        EXAMPLES::

            sage: R.<t> = LaurentSeriesRing(QQ)

        ::

            sage: f = t^(-1) + t + t^2 + O(t^3)
            sage: g = t + t^3 + t^4 + O(t^4)
            sage: f.common_valuation(g)
            -1
            sage: g.common_valuation(f)
            -1

        ::

            sage: f = t + t^2 + O(t^3)
            sage: g = t^(-3) + t^2
            sage: f.common_valuation(g)
            -3
            sage: g.common_valuation(f)
            -3

        ::

            sage: f = t + t^2
            sage: g = t^2
            sage: f.common_valuation(g)
            1

        ::

            sage: f = t^(-3) + O(t^(-2))
            sage: g = t^(-5) + O(t^(-1))
            sage: f.common_valuation(g)
            -5

        ::

            sage: f = O(t^2)
            sage: g = O(t^5)
            sage: f.common_valuation(g)
            +Infinity"""
    @overload
    def common_valuation(self, f) -> Any:
        """LaurentSeries.common_valuation(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1176)

        Return the minimum valuation of ``self`` and ``other``.

        EXAMPLES::

            sage: R.<t> = LaurentSeriesRing(QQ)

        ::

            sage: f = t^(-1) + t + t^2 + O(t^3)
            sage: g = t + t^3 + t^4 + O(t^4)
            sage: f.common_valuation(g)
            -1
            sage: g.common_valuation(f)
            -1

        ::

            sage: f = t + t^2 + O(t^3)
            sage: g = t^(-3) + t^2
            sage: f.common_valuation(g)
            -3
            sage: g.common_valuation(f)
            -3

        ::

            sage: f = t + t^2
            sage: g = t^2
            sage: f.common_valuation(g)
            1

        ::

            sage: f = t^(-3) + O(t^(-2))
            sage: g = t^(-5) + O(t^(-1))
            sage: f.common_valuation(g)
            -5

        ::

            sage: f = O(t^2)
            sage: g = O(t^5)
            sage: f.common_valuation(g)
            +Infinity"""
    @overload
    def common_valuation(self, g) -> Any:
        """LaurentSeries.common_valuation(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1176)

        Return the minimum valuation of ``self`` and ``other``.

        EXAMPLES::

            sage: R.<t> = LaurentSeriesRing(QQ)

        ::

            sage: f = t^(-1) + t + t^2 + O(t^3)
            sage: g = t + t^3 + t^4 + O(t^4)
            sage: f.common_valuation(g)
            -1
            sage: g.common_valuation(f)
            -1

        ::

            sage: f = t + t^2 + O(t^3)
            sage: g = t^(-3) + t^2
            sage: f.common_valuation(g)
            -3
            sage: g.common_valuation(f)
            -3

        ::

            sage: f = t + t^2
            sage: g = t^2
            sage: f.common_valuation(g)
            1

        ::

            sage: f = t^(-3) + O(t^(-2))
            sage: g = t^(-5) + O(t^(-1))
            sage: f.common_valuation(g)
            -5

        ::

            sage: f = O(t^2)
            sage: g = O(t^5)
            sage: f.common_valuation(g)
            +Infinity"""
    @overload
    def common_valuation(self, f) -> Any:
        """LaurentSeries.common_valuation(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1176)

        Return the minimum valuation of ``self`` and ``other``.

        EXAMPLES::

            sage: R.<t> = LaurentSeriesRing(QQ)

        ::

            sage: f = t^(-1) + t + t^2 + O(t^3)
            sage: g = t + t^3 + t^4 + O(t^4)
            sage: f.common_valuation(g)
            -1
            sage: g.common_valuation(f)
            -1

        ::

            sage: f = t + t^2 + O(t^3)
            sage: g = t^(-3) + t^2
            sage: f.common_valuation(g)
            -3
            sage: g.common_valuation(f)
            -3

        ::

            sage: f = t + t^2
            sage: g = t^2
            sage: f.common_valuation(g)
            1

        ::

            sage: f = t^(-3) + O(t^(-2))
            sage: g = t^(-5) + O(t^(-1))
            sage: f.common_valuation(g)
            -5

        ::

            sage: f = O(t^2)
            sage: g = O(t^5)
            sage: f.common_valuation(g)
            +Infinity"""
    @overload
    def common_valuation(self, g) -> Any:
        """LaurentSeries.common_valuation(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1176)

        Return the minimum valuation of ``self`` and ``other``.

        EXAMPLES::

            sage: R.<t> = LaurentSeriesRing(QQ)

        ::

            sage: f = t^(-1) + t + t^2 + O(t^3)
            sage: g = t + t^3 + t^4 + O(t^4)
            sage: f.common_valuation(g)
            -1
            sage: g.common_valuation(f)
            -1

        ::

            sage: f = t + t^2 + O(t^3)
            sage: g = t^(-3) + t^2
            sage: f.common_valuation(g)
            -3
            sage: g.common_valuation(f)
            -3

        ::

            sage: f = t + t^2
            sage: g = t^2
            sage: f.common_valuation(g)
            1

        ::

            sage: f = t^(-3) + O(t^(-2))
            sage: g = t^(-5) + O(t^(-1))
            sage: f.common_valuation(g)
            -5

        ::

            sage: f = O(t^2)
            sage: g = O(t^5)
            sage: f.common_valuation(g)
            +Infinity"""
    @overload
    def common_valuation(self, g) -> Any:
        """LaurentSeries.common_valuation(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1176)

        Return the minimum valuation of ``self`` and ``other``.

        EXAMPLES::

            sage: R.<t> = LaurentSeriesRing(QQ)

        ::

            sage: f = t^(-1) + t + t^2 + O(t^3)
            sage: g = t + t^3 + t^4 + O(t^4)
            sage: f.common_valuation(g)
            -1
            sage: g.common_valuation(f)
            -1

        ::

            sage: f = t + t^2 + O(t^3)
            sage: g = t^(-3) + t^2
            sage: f.common_valuation(g)
            -3
            sage: g.common_valuation(f)
            -3

        ::

            sage: f = t + t^2
            sage: g = t^2
            sage: f.common_valuation(g)
            1

        ::

            sage: f = t^(-3) + O(t^(-2))
            sage: g = t^(-5) + O(t^(-1))
            sage: f.common_valuation(g)
            -5

        ::

            sage: f = O(t^2)
            sage: g = O(t^5)
            sage: f.common_valuation(g)
            +Infinity"""
    @overload
    def common_valuation(self, g) -> Any:
        """LaurentSeries.common_valuation(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1176)

        Return the minimum valuation of ``self`` and ``other``.

        EXAMPLES::

            sage: R.<t> = LaurentSeriesRing(QQ)

        ::

            sage: f = t^(-1) + t + t^2 + O(t^3)
            sage: g = t + t^3 + t^4 + O(t^4)
            sage: f.common_valuation(g)
            -1
            sage: g.common_valuation(f)
            -1

        ::

            sage: f = t + t^2 + O(t^3)
            sage: g = t^(-3) + t^2
            sage: f.common_valuation(g)
            -3
            sage: g.common_valuation(f)
            -3

        ::

            sage: f = t + t^2
            sage: g = t^2
            sage: f.common_valuation(g)
            1

        ::

            sage: f = t^(-3) + O(t^(-2))
            sage: g = t^(-5) + O(t^(-1))
            sage: f.common_valuation(g)
            -5

        ::

            sage: f = O(t^2)
            sage: g = O(t^5)
            sage: f.common_valuation(g)
            +Infinity"""
    @overload
    def degree(self) -> Any:
        """LaurentSeries.degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 889)

        Return the degree of a polynomial equivalent to this power series
        modulo big oh of the precision.

        EXAMPLES::

            sage: x = Frac(QQ[['x']]).0
            sage: g = x^2 - x^4 + O(x^8)
            sage: g.degree()
            4
            sage: g = -10/x^5 + x^2 - x^4 + O(x^8)
            sage: g.degree()
            4
            sage: (x^-2 + O(x^0)).degree()
            -2"""
    @overload
    def degree(self) -> Any:
        """LaurentSeries.degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 889)

        Return the degree of a polynomial equivalent to this power series
        modulo big oh of the precision.

        EXAMPLES::

            sage: x = Frac(QQ[['x']]).0
            sage: g = x^2 - x^4 + O(x^8)
            sage: g.degree()
            4
            sage: g = -10/x^5 + x^2 - x^4 + O(x^8)
            sage: g.degree()
            4
            sage: (x^-2 + O(x^0)).degree()
            -2"""
    @overload
    def degree(self) -> Any:
        """LaurentSeries.degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 889)

        Return the degree of a polynomial equivalent to this power series
        modulo big oh of the precision.

        EXAMPLES::

            sage: x = Frac(QQ[['x']]).0
            sage: g = x^2 - x^4 + O(x^8)
            sage: g.degree()
            4
            sage: g = -10/x^5 + x^2 - x^4 + O(x^8)
            sage: g.degree()
            4
            sage: (x^-2 + O(x^0)).degree()
            -2"""
    @overload
    def degree(self) -> Any:
        """LaurentSeries.degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 889)

        Return the degree of a polynomial equivalent to this power series
        modulo big oh of the precision.

        EXAMPLES::

            sage: x = Frac(QQ[['x']]).0
            sage: g = x^2 - x^4 + O(x^8)
            sage: g.degree()
            4
            sage: g = -10/x^5 + x^2 - x^4 + O(x^8)
            sage: g.degree()
            4
            sage: (x^-2 + O(x^0)).degree()
            -2"""
    @overload
    def derivative(self, *args) -> Any:
        """LaurentSeries.derivative(self, *args)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1550)

        The formal derivative of this Laurent series, with respect to
        variables supplied in args.

        Multiple variables and iteration counts may be supplied; see
        documentation for the global derivative() function for more
        details.

        .. SEEALSO::

           :meth:`_derivative`

        EXAMPLES::

            sage: R.<x> = LaurentSeriesRing(QQ)
            sage: g = 1/x^10 - x + x^2 - x^4 + O(x^8)
            sage: g.derivative()
            -10*x^-11 - 1 + 2*x - 4*x^3 + O(x^7)
            sage: g.derivative(x)
            -10*x^-11 - 1 + 2*x - 4*x^3 + O(x^7)

        ::

            sage: R.<t> = PolynomialRing(ZZ)
            sage: S.<x> = LaurentSeriesRing(R)
            sage: f = 2*t/x + (3*t^2 + 6*t)*x + O(x^2)
            sage: f.derivative()
            -2*t*x^-2 + (3*t^2 + 6*t) + O(x)
            sage: f.derivative(x)
            -2*t*x^-2 + (3*t^2 + 6*t) + O(x)
            sage: f.derivative(t)
            2*x^-1 + (6*t + 6)*x + O(x^2)"""
    @overload
    def derivative(self) -> Any:
        """LaurentSeries.derivative(self, *args)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1550)

        The formal derivative of this Laurent series, with respect to
        variables supplied in args.

        Multiple variables and iteration counts may be supplied; see
        documentation for the global derivative() function for more
        details.

        .. SEEALSO::

           :meth:`_derivative`

        EXAMPLES::

            sage: R.<x> = LaurentSeriesRing(QQ)
            sage: g = 1/x^10 - x + x^2 - x^4 + O(x^8)
            sage: g.derivative()
            -10*x^-11 - 1 + 2*x - 4*x^3 + O(x^7)
            sage: g.derivative(x)
            -10*x^-11 - 1 + 2*x - 4*x^3 + O(x^7)

        ::

            sage: R.<t> = PolynomialRing(ZZ)
            sage: S.<x> = LaurentSeriesRing(R)
            sage: f = 2*t/x + (3*t^2 + 6*t)*x + O(x^2)
            sage: f.derivative()
            -2*t*x^-2 + (3*t^2 + 6*t) + O(x)
            sage: f.derivative(x)
            -2*t*x^-2 + (3*t^2 + 6*t) + O(x)
            sage: f.derivative(t)
            2*x^-1 + (6*t + 6)*x + O(x^2)"""
    @overload
    def derivative(self) -> Any:
        """LaurentSeries.derivative(self, *args)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1550)

        The formal derivative of this Laurent series, with respect to
        variables supplied in args.

        Multiple variables and iteration counts may be supplied; see
        documentation for the global derivative() function for more
        details.

        .. SEEALSO::

           :meth:`_derivative`

        EXAMPLES::

            sage: R.<x> = LaurentSeriesRing(QQ)
            sage: g = 1/x^10 - x + x^2 - x^4 + O(x^8)
            sage: g.derivative()
            -10*x^-11 - 1 + 2*x - 4*x^3 + O(x^7)
            sage: g.derivative(x)
            -10*x^-11 - 1 + 2*x - 4*x^3 + O(x^7)

        ::

            sage: R.<t> = PolynomialRing(ZZ)
            sage: S.<x> = LaurentSeriesRing(R)
            sage: f = 2*t/x + (3*t^2 + 6*t)*x + O(x^2)
            sage: f.derivative()
            -2*t*x^-2 + (3*t^2 + 6*t) + O(x)
            sage: f.derivative(x)
            -2*t*x^-2 + (3*t^2 + 6*t) + O(x)
            sage: f.derivative(t)
            2*x^-1 + (6*t + 6)*x + O(x^2)"""
    @overload
    def derivative(self, x) -> Any:
        """LaurentSeries.derivative(self, *args)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1550)

        The formal derivative of this Laurent series, with respect to
        variables supplied in args.

        Multiple variables and iteration counts may be supplied; see
        documentation for the global derivative() function for more
        details.

        .. SEEALSO::

           :meth:`_derivative`

        EXAMPLES::

            sage: R.<x> = LaurentSeriesRing(QQ)
            sage: g = 1/x^10 - x + x^2 - x^4 + O(x^8)
            sage: g.derivative()
            -10*x^-11 - 1 + 2*x - 4*x^3 + O(x^7)
            sage: g.derivative(x)
            -10*x^-11 - 1 + 2*x - 4*x^3 + O(x^7)

        ::

            sage: R.<t> = PolynomialRing(ZZ)
            sage: S.<x> = LaurentSeriesRing(R)
            sage: f = 2*t/x + (3*t^2 + 6*t)*x + O(x^2)
            sage: f.derivative()
            -2*t*x^-2 + (3*t^2 + 6*t) + O(x)
            sage: f.derivative(x)
            -2*t*x^-2 + (3*t^2 + 6*t) + O(x)
            sage: f.derivative(t)
            2*x^-1 + (6*t + 6)*x + O(x^2)"""
    @overload
    def derivative(self) -> Any:
        """LaurentSeries.derivative(self, *args)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1550)

        The formal derivative of this Laurent series, with respect to
        variables supplied in args.

        Multiple variables and iteration counts may be supplied; see
        documentation for the global derivative() function for more
        details.

        .. SEEALSO::

           :meth:`_derivative`

        EXAMPLES::

            sage: R.<x> = LaurentSeriesRing(QQ)
            sage: g = 1/x^10 - x + x^2 - x^4 + O(x^8)
            sage: g.derivative()
            -10*x^-11 - 1 + 2*x - 4*x^3 + O(x^7)
            sage: g.derivative(x)
            -10*x^-11 - 1 + 2*x - 4*x^3 + O(x^7)

        ::

            sage: R.<t> = PolynomialRing(ZZ)
            sage: S.<x> = LaurentSeriesRing(R)
            sage: f = 2*t/x + (3*t^2 + 6*t)*x + O(x^2)
            sage: f.derivative()
            -2*t*x^-2 + (3*t^2 + 6*t) + O(x)
            sage: f.derivative(x)
            -2*t*x^-2 + (3*t^2 + 6*t) + O(x)
            sage: f.derivative(t)
            2*x^-1 + (6*t + 6)*x + O(x^2)"""
    @overload
    def derivative(self, x) -> Any:
        """LaurentSeries.derivative(self, *args)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1550)

        The formal derivative of this Laurent series, with respect to
        variables supplied in args.

        Multiple variables and iteration counts may be supplied; see
        documentation for the global derivative() function for more
        details.

        .. SEEALSO::

           :meth:`_derivative`

        EXAMPLES::

            sage: R.<x> = LaurentSeriesRing(QQ)
            sage: g = 1/x^10 - x + x^2 - x^4 + O(x^8)
            sage: g.derivative()
            -10*x^-11 - 1 + 2*x - 4*x^3 + O(x^7)
            sage: g.derivative(x)
            -10*x^-11 - 1 + 2*x - 4*x^3 + O(x^7)

        ::

            sage: R.<t> = PolynomialRing(ZZ)
            sage: S.<x> = LaurentSeriesRing(R)
            sage: f = 2*t/x + (3*t^2 + 6*t)*x + O(x^2)
            sage: f.derivative()
            -2*t*x^-2 + (3*t^2 + 6*t) + O(x)
            sage: f.derivative(x)
            -2*t*x^-2 + (3*t^2 + 6*t) + O(x)
            sage: f.derivative(t)
            2*x^-1 + (6*t + 6)*x + O(x^2)"""
    @overload
    def derivative(self, t) -> Any:
        """LaurentSeries.derivative(self, *args)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1550)

        The formal derivative of this Laurent series, with respect to
        variables supplied in args.

        Multiple variables and iteration counts may be supplied; see
        documentation for the global derivative() function for more
        details.

        .. SEEALSO::

           :meth:`_derivative`

        EXAMPLES::

            sage: R.<x> = LaurentSeriesRing(QQ)
            sage: g = 1/x^10 - x + x^2 - x^4 + O(x^8)
            sage: g.derivative()
            -10*x^-11 - 1 + 2*x - 4*x^3 + O(x^7)
            sage: g.derivative(x)
            -10*x^-11 - 1 + 2*x - 4*x^3 + O(x^7)

        ::

            sage: R.<t> = PolynomialRing(ZZ)
            sage: S.<x> = LaurentSeriesRing(R)
            sage: f = 2*t/x + (3*t^2 + 6*t)*x + O(x^2)
            sage: f.derivative()
            -2*t*x^-2 + (3*t^2 + 6*t) + O(x)
            sage: f.derivative(x)
            -2*t*x^-2 + (3*t^2 + 6*t) + O(x)
            sage: f.derivative(t)
            2*x^-1 + (6*t + 6)*x + O(x^2)"""
    @overload
    def exponents(self) -> Any:
        """LaurentSeries.exponents(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 631)

        Return the exponents appearing in ``self`` with nonzero coefficients.

        EXAMPLES::

            sage: R.<t> = LaurentSeriesRing(QQ)
            sage: f = -5/t^(2) + t + t^2 - 10/3*t^3
            sage: f.exponents()
            [-2, 1, 2, 3]"""
    @overload
    def exponents(self) -> Any:
        """LaurentSeries.exponents(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 631)

        Return the exponents appearing in ``self`` with nonzero coefficients.

        EXAMPLES::

            sage: R.<t> = LaurentSeriesRing(QQ)
            sage: f = -5/t^(2) + t + t^2 - 10/3*t^3
            sage: f.exponents()
            [-2, 1, 2, 3]"""
    @overload
    def integral(self) -> Any:
        """LaurentSeries.integral(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1645)

        The formal integral of this Laurent series with 0 constant term.

        EXAMPLES: The integral may or may not be defined if the base ring
        is not a field.

        ::

            sage: t = LaurentSeriesRing(ZZ, 't').0
            sage: f = 2*t^-3 + 3*t^2 + O(t^4)
            sage: f.integral()
            -t^-2 + t^3 + O(t^5)

        ::

            sage: f = t^3
            sage: f.integral()
            Traceback (most recent call last):
            ...
            ArithmeticError: Coefficients of integral cannot be coerced into the base ring

        The integral of 1/t is `\\log(t)`, which is not given by a
        Laurent series::

            sage: t = Frac(QQ[['t']]).0
            sage: f = -1/t^3 - 31/t + O(t^3)
            sage: f.integral()
            Traceback (most recent call last):
            ...
            ArithmeticError: The integral of is not a Laurent series, since t^-1 has nonzero coefficient.

        Another example with just one negative coefficient::

            sage: A.<t> = QQ[[]]
            sage: f = -2*t^(-4) + O(t^8)
            sage: f.integral()
            2/3*t^-3 + O(t^9)
            sage: f.integral().derivative() == f
            True"""
    @overload
    def integral(self) -> Any:
        """LaurentSeries.integral(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1645)

        The formal integral of this Laurent series with 0 constant term.

        EXAMPLES: The integral may or may not be defined if the base ring
        is not a field.

        ::

            sage: t = LaurentSeriesRing(ZZ, 't').0
            sage: f = 2*t^-3 + 3*t^2 + O(t^4)
            sage: f.integral()
            -t^-2 + t^3 + O(t^5)

        ::

            sage: f = t^3
            sage: f.integral()
            Traceback (most recent call last):
            ...
            ArithmeticError: Coefficients of integral cannot be coerced into the base ring

        The integral of 1/t is `\\log(t)`, which is not given by a
        Laurent series::

            sage: t = Frac(QQ[['t']]).0
            sage: f = -1/t^3 - 31/t + O(t^3)
            sage: f.integral()
            Traceback (most recent call last):
            ...
            ArithmeticError: The integral of is not a Laurent series, since t^-1 has nonzero coefficient.

        Another example with just one negative coefficient::

            sage: A.<t> = QQ[[]]
            sage: f = -2*t^(-4) + O(t^8)
            sage: f.integral()
            2/3*t^-3 + O(t^9)
            sage: f.integral().derivative() == f
            True"""
    @overload
    def integral(self) -> Any:
        """LaurentSeries.integral(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1645)

        The formal integral of this Laurent series with 0 constant term.

        EXAMPLES: The integral may or may not be defined if the base ring
        is not a field.

        ::

            sage: t = LaurentSeriesRing(ZZ, 't').0
            sage: f = 2*t^-3 + 3*t^2 + O(t^4)
            sage: f.integral()
            -t^-2 + t^3 + O(t^5)

        ::

            sage: f = t^3
            sage: f.integral()
            Traceback (most recent call last):
            ...
            ArithmeticError: Coefficients of integral cannot be coerced into the base ring

        The integral of 1/t is `\\log(t)`, which is not given by a
        Laurent series::

            sage: t = Frac(QQ[['t']]).0
            sage: f = -1/t^3 - 31/t + O(t^3)
            sage: f.integral()
            Traceback (most recent call last):
            ...
            ArithmeticError: The integral of is not a Laurent series, since t^-1 has nonzero coefficient.

        Another example with just one negative coefficient::

            sage: A.<t> = QQ[[]]
            sage: f = -2*t^(-4) + O(t^8)
            sage: f.integral()
            2/3*t^-3 + O(t^9)
            sage: f.integral().derivative() == f
            True"""
    @overload
    def inverse(self) -> Any:
        """LaurentSeries.inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1809)

        Return the inverse of self, i.e., self^(-1).

        EXAMPLES::

            sage: R.<t> = LaurentSeriesRing(ZZ)
            sage: t.inverse()
            t^-1
            sage: (1-t).inverse()
            1 + t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + ..."""
    @overload
    def inverse(self) -> Any:
        """LaurentSeries.inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1809)

        Return the inverse of self, i.e., self^(-1).

        EXAMPLES::

            sage: R.<t> = LaurentSeriesRing(ZZ)
            sage: t.inverse()
            t^-1
            sage: (1-t).inverse()
            1 + t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + ..."""
    @overload
    def inverse(self) -> Any:
        """LaurentSeries.inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1809)

        Return the inverse of self, i.e., self^(-1).

        EXAMPLES::

            sage: R.<t> = LaurentSeriesRing(ZZ)
            sage: t.inverse()
            t^-1
            sage: (1-t).inverse()
            1 + t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + ..."""
    @overload
    def is_monomial(self) -> Any:
        """LaurentSeries.is_monomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 237)

        Return ``True`` if this element is a monomial.  That is, if ``self`` is
        `x^n` for some integer `n`.

        EXAMPLES::

            sage: k.<z> = LaurentSeriesRing(QQ, 'z')
            sage: (30*z).is_monomial()
            False
            sage: k(1).is_monomial()
            True
            sage: (z+1).is_monomial()
            False
            sage: (z^-2909).is_monomial()
            True
            sage: (3*z^-2909).is_monomial()
            False"""
    @overload
    def is_monomial(self) -> Any:
        """LaurentSeries.is_monomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 237)

        Return ``True`` if this element is a monomial.  That is, if ``self`` is
        `x^n` for some integer `n`.

        EXAMPLES::

            sage: k.<z> = LaurentSeriesRing(QQ, 'z')
            sage: (30*z).is_monomial()
            False
            sage: k(1).is_monomial()
            True
            sage: (z+1).is_monomial()
            False
            sage: (z^-2909).is_monomial()
            True
            sage: (3*z^-2909).is_monomial()
            False"""
    @overload
    def is_monomial(self) -> Any:
        """LaurentSeries.is_monomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 237)

        Return ``True`` if this element is a monomial.  That is, if ``self`` is
        `x^n` for some integer `n`.

        EXAMPLES::

            sage: k.<z> = LaurentSeriesRing(QQ, 'z')
            sage: (30*z).is_monomial()
            False
            sage: k(1).is_monomial()
            True
            sage: (z+1).is_monomial()
            False
            sage: (z^-2909).is_monomial()
            True
            sage: (3*z^-2909).is_monomial()
            False"""
    @overload
    def is_monomial(self) -> Any:
        """LaurentSeries.is_monomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 237)

        Return ``True`` if this element is a monomial.  That is, if ``self`` is
        `x^n` for some integer `n`.

        EXAMPLES::

            sage: k.<z> = LaurentSeriesRing(QQ, 'z')
            sage: (30*z).is_monomial()
            False
            sage: k(1).is_monomial()
            True
            sage: (z+1).is_monomial()
            False
            sage: (z^-2909).is_monomial()
            True
            sage: (3*z^-2909).is_monomial()
            False"""
    @overload
    def is_monomial(self) -> Any:
        """LaurentSeries.is_monomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 237)

        Return ``True`` if this element is a monomial.  That is, if ``self`` is
        `x^n` for some integer `n`.

        EXAMPLES::

            sage: k.<z> = LaurentSeriesRing(QQ, 'z')
            sage: (30*z).is_monomial()
            False
            sage: k(1).is_monomial()
            True
            sage: (z+1).is_monomial()
            False
            sage: (z^-2909).is_monomial()
            True
            sage: (3*z^-2909).is_monomial()
            False"""
    @overload
    def is_monomial(self) -> Any:
        """LaurentSeries.is_monomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 237)

        Return ``True`` if this element is a monomial.  That is, if ``self`` is
        `x^n` for some integer `n`.

        EXAMPLES::

            sage: k.<z> = LaurentSeriesRing(QQ, 'z')
            sage: (30*z).is_monomial()
            False
            sage: k(1).is_monomial()
            True
            sage: (z+1).is_monomial()
            False
            sage: (z^-2909).is_monomial()
            True
            sage: (3*z^-2909).is_monomial()
            False"""
    @overload
    def is_unit(self) -> Any:
        '''LaurentSeries.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 194)

        Return ``True`` if this is Laurent series is a unit in this ring.

        EXAMPLES::

            sage: R.<t> = LaurentSeriesRing(QQ)
            sage: (2 + t).is_unit()
            True
            sage: f = 2 + t^2 + O(t^10); f.is_unit()
            True
            sage: 1/f
            1/2 - 1/4*t^2 + 1/8*t^4 - 1/16*t^6 + 1/32*t^8 + O(t^10)
            sage: R(0).is_unit()
            False
            sage: R.<s> = LaurentSeriesRing(ZZ)
            sage: f = 2 + s^2 + O(s^10)
            sage: f.is_unit()
            False
            sage: 1/f
            Traceback (most recent call last):
            ...
            ValueError: constant term 2 is not a unit

        ALGORITHM: A Laurent series is a unit if and only if its "unit
        part" is a unit.'''
    @overload
    def is_unit(self) -> Any:
        '''LaurentSeries.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 194)

        Return ``True`` if this is Laurent series is a unit in this ring.

        EXAMPLES::

            sage: R.<t> = LaurentSeriesRing(QQ)
            sage: (2 + t).is_unit()
            True
            sage: f = 2 + t^2 + O(t^10); f.is_unit()
            True
            sage: 1/f
            1/2 - 1/4*t^2 + 1/8*t^4 - 1/16*t^6 + 1/32*t^8 + O(t^10)
            sage: R(0).is_unit()
            False
            sage: R.<s> = LaurentSeriesRing(ZZ)
            sage: f = 2 + s^2 + O(s^10)
            sage: f.is_unit()
            False
            sage: 1/f
            Traceback (most recent call last):
            ...
            ValueError: constant term 2 is not a unit

        ALGORITHM: A Laurent series is a unit if and only if its "unit
        part" is a unit.'''
    @overload
    def is_unit(self) -> Any:
        '''LaurentSeries.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 194)

        Return ``True`` if this is Laurent series is a unit in this ring.

        EXAMPLES::

            sage: R.<t> = LaurentSeriesRing(QQ)
            sage: (2 + t).is_unit()
            True
            sage: f = 2 + t^2 + O(t^10); f.is_unit()
            True
            sage: 1/f
            1/2 - 1/4*t^2 + 1/8*t^4 - 1/16*t^6 + 1/32*t^8 + O(t^10)
            sage: R(0).is_unit()
            False
            sage: R.<s> = LaurentSeriesRing(ZZ)
            sage: f = 2 + s^2 + O(s^10)
            sage: f.is_unit()
            False
            sage: 1/f
            Traceback (most recent call last):
            ...
            ValueError: constant term 2 is not a unit

        ALGORITHM: A Laurent series is a unit if and only if its "unit
        part" is a unit.'''
    @overload
    def is_unit(self) -> Any:
        '''LaurentSeries.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 194)

        Return ``True`` if this is Laurent series is a unit in this ring.

        EXAMPLES::

            sage: R.<t> = LaurentSeriesRing(QQ)
            sage: (2 + t).is_unit()
            True
            sage: f = 2 + t^2 + O(t^10); f.is_unit()
            True
            sage: 1/f
            1/2 - 1/4*t^2 + 1/8*t^4 - 1/16*t^6 + 1/32*t^8 + O(t^10)
            sage: R(0).is_unit()
            False
            sage: R.<s> = LaurentSeriesRing(ZZ)
            sage: f = 2 + s^2 + O(s^10)
            sage: f.is_unit()
            False
            sage: 1/f
            Traceback (most recent call last):
            ...
            ValueError: constant term 2 is not a unit

        ALGORITHM: A Laurent series is a unit if and only if its "unit
        part" is a unit.'''
    @overload
    def is_unit(self) -> Any:
        '''LaurentSeries.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 194)

        Return ``True`` if this is Laurent series is a unit in this ring.

        EXAMPLES::

            sage: R.<t> = LaurentSeriesRing(QQ)
            sage: (2 + t).is_unit()
            True
            sage: f = 2 + t^2 + O(t^10); f.is_unit()
            True
            sage: 1/f
            1/2 - 1/4*t^2 + 1/8*t^4 - 1/16*t^6 + 1/32*t^8 + O(t^10)
            sage: R(0).is_unit()
            False
            sage: R.<s> = LaurentSeriesRing(ZZ)
            sage: f = 2 + s^2 + O(s^10)
            sage: f.is_unit()
            False
            sage: 1/f
            Traceback (most recent call last):
            ...
            ValueError: constant term 2 is not a unit

        ALGORITHM: A Laurent series is a unit if and only if its "unit
        part" is a unit.'''
    @overload
    def is_zero(self) -> Any:
        """LaurentSeries.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 223)

        EXAMPLES::

            sage: x = Frac(QQ[['x']]).0
            sage: f = 1/x + x + x^2 + 3*x^4 + O(x^7)
            sage: f.is_zero()
            0
            sage: z = 0*f
            sage: z.is_zero()
            1"""
    @overload
    def is_zero(self) -> Any:
        """LaurentSeries.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 223)

        EXAMPLES::

            sage: x = Frac(QQ[['x']]).0
            sage: f = 1/x + x + x^2 + 3*x^4 + O(x^7)
            sage: f.is_zero()
            0
            sage: z = 0*f
            sage: z.is_zero()
            1"""
    @overload
    def is_zero(self) -> Any:
        """LaurentSeries.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 223)

        EXAMPLES::

            sage: x = Frac(QQ[['x']]).0
            sage: f = 1/x + x + x^2 + 3*x^4 + O(x^7)
            sage: f.is_zero()
            0
            sage: z = 0*f
            sage: z.is_zero()
            1"""
    @overload
    def laurent_polynomial(self) -> Any:
        """LaurentSeries.laurent_polynomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 646)

        Return the corresponding Laurent polynomial.

        EXAMPLES::

            sage: R.<t> = LaurentSeriesRing(QQ)
            sage: f = t^-3 + t + 7*t^2 + O(t^5)
            sage: g = f.laurent_polynomial(); g
            t^-3 + t + 7*t^2
            sage: g.parent()
            Univariate Laurent Polynomial Ring in t over Rational Field"""
    @overload
    def laurent_polynomial(self) -> Any:
        """LaurentSeries.laurent_polynomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 646)

        Return the corresponding Laurent polynomial.

        EXAMPLES::

            sage: R.<t> = LaurentSeriesRing(QQ)
            sage: f = t^-3 + t + 7*t^2 + O(t^5)
            sage: g = f.laurent_polynomial(); g
            t^-3 + t + 7*t^2
            sage: g.parent()
            Univariate Laurent Polynomial Ring in t over Rational Field"""
    @overload
    def lift_to_precision(self, absprec=...) -> Any:
        """LaurentSeries.lift_to_precision(self, absprec=None)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 662)

        Return a congruent Laurent series with absolute precision at least
        ``absprec``.

        INPUT:

        - ``absprec`` -- integer or ``None`` (default: ``None``); the
          absolute precision of the result. If ``None``, lifts to an exact
          element.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: A.<t> = LaurentSeriesRing(GF(5))
            sage: x = t^(-1) + t^2 + O(t^5)
            sage: x.lift_to_precision(10)
            t^-1 + t^2 + O(t^10)
            sage: x.lift_to_precision()
            t^-1 + t^2"""
    @overload
    def lift_to_precision(self) -> Any:
        """LaurentSeries.lift_to_precision(self, absprec=None)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 662)

        Return a congruent Laurent series with absolute precision at least
        ``absprec``.

        INPUT:

        - ``absprec`` -- integer or ``None`` (default: ``None``); the
          absolute precision of the result. If ``None``, lifts to an exact
          element.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: A.<t> = LaurentSeriesRing(GF(5))
            sage: x = t^(-1) + t^2 + O(t^5)
            sage: x.lift_to_precision(10)
            t^-1 + t^2 + O(t^10)
            sage: x.lift_to_precision()
            t^-1 + t^2"""
    @overload
    def list(self) -> Any:
        """LaurentSeries.list(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 577)

        EXAMPLES::

            sage: R.<t> = LaurentSeriesRing(QQ)
            sage: f = -5/t^(2) + t + t^2 - 10/3*t^3
            sage: f.list()
            [-5, 0, 0, 1, 1, -10/3]"""
    @overload
    def list(self) -> Any:
        """LaurentSeries.list(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 577)

        EXAMPLES::

            sage: R.<t> = LaurentSeriesRing(QQ)
            sage: f = -5/t^(2) + t + t^2 - 10/3*t^3
            sage: f.list()
            [-5, 0, 0, 1, 1, -10/3]"""
    def nth_root(self, longn, prec=...) -> Any:
        """LaurentSeries.nth_root(self, long n, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1702)

        Return the ``n``-th root of this Laurent power series.

        INPUT:

        - ``n`` -- integer

        - ``prec`` -- integer (optional); precision of the result. Though, if
          this series has finite precision, then the result cannot have larger
          precision.

        EXAMPLES::

            sage: R.<x> = LaurentSeriesRing(QQ)
            sage: (x^-2 + 1 + x).nth_root(2)
            x^-1 + 1/2*x + 1/2*x^2 - ... - 19437/65536*x^18 + O(x^19)
            sage: (x^-2 + 1 + x).nth_root(2)**2
            x^-2 + 1 + x + O(x^18)

            sage: # needs sage.modular
            sage: j = j_invariant_qexp()
            sage: q = j.parent().gen()
            sage: j(q^3).nth_root(3)
            q^-1 + 248*q^2 + 4124*q^5 + ... + O(q^29)
            sage: (j(q^2) - 1728).nth_root(2)
            q^-1 - 492*q - 22590*q^3 - ... + O(q^19)"""
    @overload
    def power_series(self) -> Any:
        """LaurentSeries.power_series(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1747)

        Convert this Laurent series to a power series.

        An error is raised if the Laurent series has a term (or an error
        term `O(x^k)`) whose exponent is negative.

        EXAMPLES::

            sage: R.<t> = LaurentSeriesRing(ZZ)
            sage: f = 1/(1-t+O(t^10)); f.parent()
            Laurent Series Ring in t over Integer Ring
            sage: g = f.power_series(); g
            1 + t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)
            sage: parent(g)
            Power Series Ring in t over Integer Ring
            sage: f = 3/t^2 +  t^2 + t^3 + O(t^10)
            sage: f.power_series()
            Traceback (most recent call last):
            ...
            TypeError: self is not a power series

        TESTS:

        Check whether a polynomial over a Laurent series ring is contained in the
        polynomial ring over the power series ring (see :issue:`19459`):

            sage: # needs sage.rings.finite_rings
            sage: L.<t> = LaurentSeriesRing(GF(2))
            sage: R.<x,y> = PolynomialRing(L)
            sage: S.<x,y> = PolynomialRing(L._power_series_ring)
            sage: t**(-1)*x*y in S
            False

        There used to be an issue with non-canonical representations of zero,
        see :issue:`31383`::

            sage: S.<x> = PowerSeriesRing(QQ)
            sage: L = Frac(S)
            sage: s = L(O(x^2))
            sage: (s*x^(-1)).power_series()
            O(x^1)
            sage: (s*x^(-2)).power_series()
            O(x^0)
            sage: (s*x^(-3)).power_series()
            Traceback (most recent call last):
            ...
            TypeError: self is not a power series

        Test for :issue:`32440`::

            sage: L.<x> = LaurentSeriesRing(QQ, implementation='pari')                  # needs sage.libs.pari
            sage: (x + O(x^3)).power_series()                                           # needs sage.libs.pari
            x + O(x^3)"""
    @overload
    def power_series(self) -> Any:
        """LaurentSeries.power_series(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1747)

        Convert this Laurent series to a power series.

        An error is raised if the Laurent series has a term (or an error
        term `O(x^k)`) whose exponent is negative.

        EXAMPLES::

            sage: R.<t> = LaurentSeriesRing(ZZ)
            sage: f = 1/(1-t+O(t^10)); f.parent()
            Laurent Series Ring in t over Integer Ring
            sage: g = f.power_series(); g
            1 + t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)
            sage: parent(g)
            Power Series Ring in t over Integer Ring
            sage: f = 3/t^2 +  t^2 + t^3 + O(t^10)
            sage: f.power_series()
            Traceback (most recent call last):
            ...
            TypeError: self is not a power series

        TESTS:

        Check whether a polynomial over a Laurent series ring is contained in the
        polynomial ring over the power series ring (see :issue:`19459`):

            sage: # needs sage.rings.finite_rings
            sage: L.<t> = LaurentSeriesRing(GF(2))
            sage: R.<x,y> = PolynomialRing(L)
            sage: S.<x,y> = PolynomialRing(L._power_series_ring)
            sage: t**(-1)*x*y in S
            False

        There used to be an issue with non-canonical representations of zero,
        see :issue:`31383`::

            sage: S.<x> = PowerSeriesRing(QQ)
            sage: L = Frac(S)
            sage: s = L(O(x^2))
            sage: (s*x^(-1)).power_series()
            O(x^1)
            sage: (s*x^(-2)).power_series()
            O(x^0)
            sage: (s*x^(-3)).power_series()
            Traceback (most recent call last):
            ...
            TypeError: self is not a power series

        Test for :issue:`32440`::

            sage: L.<x> = LaurentSeriesRing(QQ, implementation='pari')                  # needs sage.libs.pari
            sage: (x + O(x^3)).power_series()                                           # needs sage.libs.pari
            x + O(x^3)"""
    @overload
    def power_series(self) -> Any:
        """LaurentSeries.power_series(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1747)

        Convert this Laurent series to a power series.

        An error is raised if the Laurent series has a term (or an error
        term `O(x^k)`) whose exponent is negative.

        EXAMPLES::

            sage: R.<t> = LaurentSeriesRing(ZZ)
            sage: f = 1/(1-t+O(t^10)); f.parent()
            Laurent Series Ring in t over Integer Ring
            sage: g = f.power_series(); g
            1 + t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)
            sage: parent(g)
            Power Series Ring in t over Integer Ring
            sage: f = 3/t^2 +  t^2 + t^3 + O(t^10)
            sage: f.power_series()
            Traceback (most recent call last):
            ...
            TypeError: self is not a power series

        TESTS:

        Check whether a polynomial over a Laurent series ring is contained in the
        polynomial ring over the power series ring (see :issue:`19459`):

            sage: # needs sage.rings.finite_rings
            sage: L.<t> = LaurentSeriesRing(GF(2))
            sage: R.<x,y> = PolynomialRing(L)
            sage: S.<x,y> = PolynomialRing(L._power_series_ring)
            sage: t**(-1)*x*y in S
            False

        There used to be an issue with non-canonical representations of zero,
        see :issue:`31383`::

            sage: S.<x> = PowerSeriesRing(QQ)
            sage: L = Frac(S)
            sage: s = L(O(x^2))
            sage: (s*x^(-1)).power_series()
            O(x^1)
            sage: (s*x^(-2)).power_series()
            O(x^0)
            sage: (s*x^(-3)).power_series()
            Traceback (most recent call last):
            ...
            TypeError: self is not a power series

        Test for :issue:`32440`::

            sage: L.<x> = LaurentSeriesRing(QQ, implementation='pari')                  # needs sage.libs.pari
            sage: (x + O(x^3)).power_series()                                           # needs sage.libs.pari
            x + O(x^3)"""
    @overload
    def power_series(self) -> Any:
        """LaurentSeries.power_series(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1747)

        Convert this Laurent series to a power series.

        An error is raised if the Laurent series has a term (or an error
        term `O(x^k)`) whose exponent is negative.

        EXAMPLES::

            sage: R.<t> = LaurentSeriesRing(ZZ)
            sage: f = 1/(1-t+O(t^10)); f.parent()
            Laurent Series Ring in t over Integer Ring
            sage: g = f.power_series(); g
            1 + t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)
            sage: parent(g)
            Power Series Ring in t over Integer Ring
            sage: f = 3/t^2 +  t^2 + t^3 + O(t^10)
            sage: f.power_series()
            Traceback (most recent call last):
            ...
            TypeError: self is not a power series

        TESTS:

        Check whether a polynomial over a Laurent series ring is contained in the
        polynomial ring over the power series ring (see :issue:`19459`):

            sage: # needs sage.rings.finite_rings
            sage: L.<t> = LaurentSeriesRing(GF(2))
            sage: R.<x,y> = PolynomialRing(L)
            sage: S.<x,y> = PolynomialRing(L._power_series_ring)
            sage: t**(-1)*x*y in S
            False

        There used to be an issue with non-canonical representations of zero,
        see :issue:`31383`::

            sage: S.<x> = PowerSeriesRing(QQ)
            sage: L = Frac(S)
            sage: s = L(O(x^2))
            sage: (s*x^(-1)).power_series()
            O(x^1)
            sage: (s*x^(-2)).power_series()
            O(x^0)
            sage: (s*x^(-3)).power_series()
            Traceback (most recent call last):
            ...
            TypeError: self is not a power series

        Test for :issue:`32440`::

            sage: L.<x> = LaurentSeriesRing(QQ, implementation='pari')                  # needs sage.libs.pari
            sage: (x + O(x^3)).power_series()                                           # needs sage.libs.pari
            x + O(x^3)"""
    @overload
    def power_series(self) -> Any:
        """LaurentSeries.power_series(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1747)

        Convert this Laurent series to a power series.

        An error is raised if the Laurent series has a term (or an error
        term `O(x^k)`) whose exponent is negative.

        EXAMPLES::

            sage: R.<t> = LaurentSeriesRing(ZZ)
            sage: f = 1/(1-t+O(t^10)); f.parent()
            Laurent Series Ring in t over Integer Ring
            sage: g = f.power_series(); g
            1 + t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)
            sage: parent(g)
            Power Series Ring in t over Integer Ring
            sage: f = 3/t^2 +  t^2 + t^3 + O(t^10)
            sage: f.power_series()
            Traceback (most recent call last):
            ...
            TypeError: self is not a power series

        TESTS:

        Check whether a polynomial over a Laurent series ring is contained in the
        polynomial ring over the power series ring (see :issue:`19459`):

            sage: # needs sage.rings.finite_rings
            sage: L.<t> = LaurentSeriesRing(GF(2))
            sage: R.<x,y> = PolynomialRing(L)
            sage: S.<x,y> = PolynomialRing(L._power_series_ring)
            sage: t**(-1)*x*y in S
            False

        There used to be an issue with non-canonical representations of zero,
        see :issue:`31383`::

            sage: S.<x> = PowerSeriesRing(QQ)
            sage: L = Frac(S)
            sage: s = L(O(x^2))
            sage: (s*x^(-1)).power_series()
            O(x^1)
            sage: (s*x^(-2)).power_series()
            O(x^0)
            sage: (s*x^(-3)).power_series()
            Traceback (most recent call last):
            ...
            TypeError: self is not a power series

        Test for :issue:`32440`::

            sage: L.<x> = LaurentSeriesRing(QQ, implementation='pari')                  # needs sage.libs.pari
            sage: (x + O(x^3)).power_series()                                           # needs sage.libs.pari
            x + O(x^3)"""
    @overload
    def power_series(self) -> Any:
        """LaurentSeries.power_series(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1747)

        Convert this Laurent series to a power series.

        An error is raised if the Laurent series has a term (or an error
        term `O(x^k)`) whose exponent is negative.

        EXAMPLES::

            sage: R.<t> = LaurentSeriesRing(ZZ)
            sage: f = 1/(1-t+O(t^10)); f.parent()
            Laurent Series Ring in t over Integer Ring
            sage: g = f.power_series(); g
            1 + t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)
            sage: parent(g)
            Power Series Ring in t over Integer Ring
            sage: f = 3/t^2 +  t^2 + t^3 + O(t^10)
            sage: f.power_series()
            Traceback (most recent call last):
            ...
            TypeError: self is not a power series

        TESTS:

        Check whether a polynomial over a Laurent series ring is contained in the
        polynomial ring over the power series ring (see :issue:`19459`):

            sage: # needs sage.rings.finite_rings
            sage: L.<t> = LaurentSeriesRing(GF(2))
            sage: R.<x,y> = PolynomialRing(L)
            sage: S.<x,y> = PolynomialRing(L._power_series_ring)
            sage: t**(-1)*x*y in S
            False

        There used to be an issue with non-canonical representations of zero,
        see :issue:`31383`::

            sage: S.<x> = PowerSeriesRing(QQ)
            sage: L = Frac(S)
            sage: s = L(O(x^2))
            sage: (s*x^(-1)).power_series()
            O(x^1)
            sage: (s*x^(-2)).power_series()
            O(x^0)
            sage: (s*x^(-3)).power_series()
            Traceback (most recent call last):
            ...
            TypeError: self is not a power series

        Test for :issue:`32440`::

            sage: L.<x> = LaurentSeriesRing(QQ, implementation='pari')                  # needs sage.libs.pari
            sage: (x + O(x^3)).power_series()                                           # needs sage.libs.pari
            x + O(x^3)"""
    @overload
    def power_series(self) -> Any:
        """LaurentSeries.power_series(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1747)

        Convert this Laurent series to a power series.

        An error is raised if the Laurent series has a term (or an error
        term `O(x^k)`) whose exponent is negative.

        EXAMPLES::

            sage: R.<t> = LaurentSeriesRing(ZZ)
            sage: f = 1/(1-t+O(t^10)); f.parent()
            Laurent Series Ring in t over Integer Ring
            sage: g = f.power_series(); g
            1 + t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + O(t^10)
            sage: parent(g)
            Power Series Ring in t over Integer Ring
            sage: f = 3/t^2 +  t^2 + t^3 + O(t^10)
            sage: f.power_series()
            Traceback (most recent call last):
            ...
            TypeError: self is not a power series

        TESTS:

        Check whether a polynomial over a Laurent series ring is contained in the
        polynomial ring over the power series ring (see :issue:`19459`):

            sage: # needs sage.rings.finite_rings
            sage: L.<t> = LaurentSeriesRing(GF(2))
            sage: R.<x,y> = PolynomialRing(L)
            sage: S.<x,y> = PolynomialRing(L._power_series_ring)
            sage: t**(-1)*x*y in S
            False

        There used to be an issue with non-canonical representations of zero,
        see :issue:`31383`::

            sage: S.<x> = PowerSeriesRing(QQ)
            sage: L = Frac(S)
            sage: s = L(O(x^2))
            sage: (s*x^(-1)).power_series()
            O(x^1)
            sage: (s*x^(-2)).power_series()
            O(x^0)
            sage: (s*x^(-3)).power_series()
            Traceback (most recent call last):
            ...
            TypeError: self is not a power series

        Test for :issue:`32440`::

            sage: L.<x> = LaurentSeriesRing(QQ, implementation='pari')                  # needs sage.libs.pari
            sage: (x + O(x^3)).power_series()                                           # needs sage.libs.pari
            x + O(x^3)"""
    def prec(self) -> Any:
        """LaurentSeries.prec(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1354)

        This function returns the n so that the Laurent series is of the
        form (stuff) + `O(t^n)`. It doesn't matter how many
        negative powers appear in the expansion. In particular, prec could
        be negative.

        EXAMPLES::

            sage: x = Frac(QQ[['x']]).0
            sage: f = x^2 + 3*x^4 + O(x^7)
            sage: f.prec()
            7
            sage: g = 1/x^10 - x + x^2 - x^4 + O(x^8)
            sage: g.prec()
            8"""
    @overload
    def precision_absolute(self) -> Any:
        """LaurentSeries.precision_absolute(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1373)

        Return the absolute precision of this series.

        By definition, the absolute precision of
        `...+O(x^r)` is `r`.

        EXAMPLES::

            sage: R.<t> = ZZ[[]]
            sage: (t^2 + O(t^3)).precision_absolute()
            3
            sage: (1 - t^2 + O(t^100)).precision_absolute()
            100"""
    @overload
    def precision_absolute(self) -> Any:
        """LaurentSeries.precision_absolute(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1373)

        Return the absolute precision of this series.

        By definition, the absolute precision of
        `...+O(x^r)` is `r`.

        EXAMPLES::

            sage: R.<t> = ZZ[[]]
            sage: (t^2 + O(t^3)).precision_absolute()
            3
            sage: (1 - t^2 + O(t^100)).precision_absolute()
            100"""
    @overload
    def precision_absolute(self) -> Any:
        """LaurentSeries.precision_absolute(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1373)

        Return the absolute precision of this series.

        By definition, the absolute precision of
        `...+O(x^r)` is `r`.

        EXAMPLES::

            sage: R.<t> = ZZ[[]]
            sage: (t^2 + O(t^3)).precision_absolute()
            3
            sage: (1 - t^2 + O(t^100)).precision_absolute()
            100"""
    @overload
    def precision_relative(self) -> Any:
        """LaurentSeries.precision_relative(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1390)

        Return the relative precision of this series, that
        is the difference between its absolute precision
        and its valuation.

        By convention, the relative precision of `0` (or
        `O(x^r)` for any `r`) is `0`.

        EXAMPLES::

            sage: R.<t> = ZZ[[]]
            sage: (t^2 + O(t^3)).precision_relative()
            1
            sage: (1 - t^2 + O(t^100)).precision_relative()
            100
            sage: O(t^4).precision_relative()
            0"""
    @overload
    def precision_relative(self) -> Any:
        """LaurentSeries.precision_relative(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1390)

        Return the relative precision of this series, that
        is the difference between its absolute precision
        and its valuation.

        By convention, the relative precision of `0` (or
        `O(x^r)` for any `r`) is `0`.

        EXAMPLES::

            sage: R.<t> = ZZ[[]]
            sage: (t^2 + O(t^3)).precision_relative()
            1
            sage: (1 - t^2 + O(t^100)).precision_relative()
            100
            sage: O(t^4).precision_relative()
            0"""
    @overload
    def precision_relative(self) -> Any:
        """LaurentSeries.precision_relative(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1390)

        Return the relative precision of this series, that
        is the difference between its absolute precision
        and its valuation.

        By convention, the relative precision of `0` (or
        `O(x^r)` for any `r`) is `0`.

        EXAMPLES::

            sage: R.<t> = ZZ[[]]
            sage: (t^2 + O(t^3)).precision_relative()
            1
            sage: (1 - t^2 + O(t^100)).precision_relative()
            100
            sage: O(t^4).precision_relative()
            0"""
    @overload
    def precision_relative(self) -> Any:
        """LaurentSeries.precision_relative(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1390)

        Return the relative precision of this series, that
        is the difference between its absolute precision
        and its valuation.

        By convention, the relative precision of `0` (or
        `O(x^r)` for any `r`) is `0`.

        EXAMPLES::

            sage: R.<t> = ZZ[[]]
            sage: (t^2 + O(t^3)).precision_relative()
            1
            sage: (1 - t^2 + O(t^100)).precision_relative()
            100
            sage: O(t^4).precision_relative()
            0"""
    def residue(self) -> Any:
        """LaurentSeries.residue(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 602)

        Return the residue of ``self``.

        Consider the Laurent series

        .. MATH::

            f = \\sum_{n \\in \\ZZ} a_n t^n
            = \\cdots + \\frac{a_{-2}}{t^2} + \\frac{a_{-1}}{t} + a_0
            + a_1 t + a_2 t^2 + \\cdots,

        then the residue of `f` is `a_{-1}`. Alternatively this is the
        coefficient of `1/t`.

        EXAMPLES::

            sage: t = LaurentSeriesRing(ZZ,'t').gen()
            sage: f = 1/t**2 + 2/t + 3 + 4*t
            sage: f.residue()
            2
            sage: f = t + t**2
            sage: f.residue()
            0
            sage: f.residue().parent()
            Integer Ring"""
    @overload
    def reverse(self, precision=...) -> Any:
        """LaurentSeries.reverse(self, precision=None)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1417)

        Return the reverse of f, i.e., the series g such that g(f(x)) = x.
        Given an optional argument ``precision``, return the reverse with given
        precision (note that the reverse can have precision at most
        ``f.prec()``).  If ``f`` has infinite precision, and the argument
        ``precision`` is not given, then the precision of the reverse defaults
        to the default precision of ``f.parent()``.

        Note that this is only possible if the valuation of ``self`` is exactly
        1.

        The implementation depends on the underlying power series element
        implementing a reverse method.

        EXAMPLES::

            sage: R.<x> = Frac(QQ[['x']])
            sage: f = 2*x + 3*x^2 - x^4 + O(x^5)
            sage: g = f.reverse()
            sage: g
            1/2*x - 3/8*x^2 + 9/16*x^3 - 131/128*x^4 + O(x^5)
            sage: f(g)
            x + O(x^5)
            sage: g(f)
            x + O(x^5)

            sage: A.<t> = LaurentSeriesRing(ZZ)
            sage: a = t - t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + t^2 + 2*t^3 + 7*t^4 + 25*t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

            sage: B.<b,c> = ZZ[ ]
            sage: A.<t> = LaurentSeriesRing(B)
            sage: f = t + b*t^2 + c*t^3 + O(t^4)
            sage: g = f.reverse(); g
            t - b*t^2 + (2*b^2 - c)*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: B.<s> = LaurentSeriesRing(A)
            sage: f = (1 - 3*t + 4*t^3 + O(t^4))*s + (2 + t + t^2 + O(t^3))*s^2 + O(s^3)
            sage: set_verbose(1)
            sage: g = f.reverse(); g
            verbose 1 (<module>) passing to pari failed; trying Lagrange inversion
            (1 + 3*t + 9*t^2 + 23*t^3 + O(t^4))*s + (-2 - 19*t - 118*t^2 + O(t^3))*s^2 + O(s^3)
            sage: set_verbose(0)
            sage: f(g) == g(f) == s
            True

        If the leading coefficient is not a unit, we pass to its fraction
        field if possible::

            sage: A.<t> = LaurentSeriesRing(ZZ)
            sage: a = 2*t - 4*t^2 + t^4 - t^5 + O(t^6)
            sage: a.reverse()
            1/2*t + 1/2*t^2 + t^3 + 79/32*t^4 + 437/64*t^5 + O(t^6)

            sage: B.<b> = PolynomialRing(ZZ)
            sage: A.<t> = LaurentSeriesRing(B)
            sage: f = 2*b*t + b*t^2 + 3*b^2*t^3 + O(t^4)
            sage: g = f.reverse(); g
            1/(2*b)*t - 1/(8*b^2)*t^2 + ((-3*b + 1)/(16*b^3))*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

        We can handle some base rings of positive characteristic::

            sage: A8.<t> = LaurentSeriesRing(Zmod(8))
            sage: a = t - 15*t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + 7*t^2 + 2*t^3 + 5*t^4 + t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

        The optional argument ``precision`` sets the precision of the output::

            sage: R.<x> = LaurentSeriesRing(QQ)
            sage: f = 2*x + 3*x^2 - 7*x^3 + x^4 + O(x^5)
            sage: g = f.reverse(precision=3); g
            1/2*x - 3/8*x^2 + O(x^3)
            sage: f(g)
            x + O(x^3)
            sage: g(f)
            x + O(x^3)

        If the input series has infinite precision, the precision of the
        output is automatically set to the default precision of the parent
        ring::

            sage: R.<x> = LaurentSeriesRing(QQ, default_prec=20)
            sage: (x - x^2).reverse()  # get some Catalan numbers
            x + x^2 + 2*x^3 + 5*x^4 + 14*x^5 + 42*x^6 + 132*x^7 + 429*x^8 + 1430*x^9
             + 4862*x^10 + 16796*x^11 + 58786*x^12 + 208012*x^13 + 742900*x^14
             + 2674440*x^15 + 9694845*x^16 + 35357670*x^17 + 129644790*x^18
             + 477638700*x^19 + O(x^20)
            sage: (x - x^2).reverse(precision=3)
            x + x^2 + O(x^3)

        TESTS::

            sage: R.<x> = LaurentSeriesRing(QQ)
            sage: f = 1 + 2*x + 3*x^2 - x^4 + O(x^5)
            sage: f.reverse()
            Traceback (most recent call last):
            ...
            ValueError: Series must have valuation one for reversion."""
    @overload
    def reverse(self) -> Any:
        """LaurentSeries.reverse(self, precision=None)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1417)

        Return the reverse of f, i.e., the series g such that g(f(x)) = x.
        Given an optional argument ``precision``, return the reverse with given
        precision (note that the reverse can have precision at most
        ``f.prec()``).  If ``f`` has infinite precision, and the argument
        ``precision`` is not given, then the precision of the reverse defaults
        to the default precision of ``f.parent()``.

        Note that this is only possible if the valuation of ``self`` is exactly
        1.

        The implementation depends on the underlying power series element
        implementing a reverse method.

        EXAMPLES::

            sage: R.<x> = Frac(QQ[['x']])
            sage: f = 2*x + 3*x^2 - x^4 + O(x^5)
            sage: g = f.reverse()
            sage: g
            1/2*x - 3/8*x^2 + 9/16*x^3 - 131/128*x^4 + O(x^5)
            sage: f(g)
            x + O(x^5)
            sage: g(f)
            x + O(x^5)

            sage: A.<t> = LaurentSeriesRing(ZZ)
            sage: a = t - t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + t^2 + 2*t^3 + 7*t^4 + 25*t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

            sage: B.<b,c> = ZZ[ ]
            sage: A.<t> = LaurentSeriesRing(B)
            sage: f = t + b*t^2 + c*t^3 + O(t^4)
            sage: g = f.reverse(); g
            t - b*t^2 + (2*b^2 - c)*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: B.<s> = LaurentSeriesRing(A)
            sage: f = (1 - 3*t + 4*t^3 + O(t^4))*s + (2 + t + t^2 + O(t^3))*s^2 + O(s^3)
            sage: set_verbose(1)
            sage: g = f.reverse(); g
            verbose 1 (<module>) passing to pari failed; trying Lagrange inversion
            (1 + 3*t + 9*t^2 + 23*t^3 + O(t^4))*s + (-2 - 19*t - 118*t^2 + O(t^3))*s^2 + O(s^3)
            sage: set_verbose(0)
            sage: f(g) == g(f) == s
            True

        If the leading coefficient is not a unit, we pass to its fraction
        field if possible::

            sage: A.<t> = LaurentSeriesRing(ZZ)
            sage: a = 2*t - 4*t^2 + t^4 - t^5 + O(t^6)
            sage: a.reverse()
            1/2*t + 1/2*t^2 + t^3 + 79/32*t^4 + 437/64*t^5 + O(t^6)

            sage: B.<b> = PolynomialRing(ZZ)
            sage: A.<t> = LaurentSeriesRing(B)
            sage: f = 2*b*t + b*t^2 + 3*b^2*t^3 + O(t^4)
            sage: g = f.reverse(); g
            1/(2*b)*t - 1/(8*b^2)*t^2 + ((-3*b + 1)/(16*b^3))*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

        We can handle some base rings of positive characteristic::

            sage: A8.<t> = LaurentSeriesRing(Zmod(8))
            sage: a = t - 15*t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + 7*t^2 + 2*t^3 + 5*t^4 + t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

        The optional argument ``precision`` sets the precision of the output::

            sage: R.<x> = LaurentSeriesRing(QQ)
            sage: f = 2*x + 3*x^2 - 7*x^3 + x^4 + O(x^5)
            sage: g = f.reverse(precision=3); g
            1/2*x - 3/8*x^2 + O(x^3)
            sage: f(g)
            x + O(x^3)
            sage: g(f)
            x + O(x^3)

        If the input series has infinite precision, the precision of the
        output is automatically set to the default precision of the parent
        ring::

            sage: R.<x> = LaurentSeriesRing(QQ, default_prec=20)
            sage: (x - x^2).reverse()  # get some Catalan numbers
            x + x^2 + 2*x^3 + 5*x^4 + 14*x^5 + 42*x^6 + 132*x^7 + 429*x^8 + 1430*x^9
             + 4862*x^10 + 16796*x^11 + 58786*x^12 + 208012*x^13 + 742900*x^14
             + 2674440*x^15 + 9694845*x^16 + 35357670*x^17 + 129644790*x^18
             + 477638700*x^19 + O(x^20)
            sage: (x - x^2).reverse(precision=3)
            x + x^2 + O(x^3)

        TESTS::

            sage: R.<x> = LaurentSeriesRing(QQ)
            sage: f = 1 + 2*x + 3*x^2 - x^4 + O(x^5)
            sage: f.reverse()
            Traceback (most recent call last):
            ...
            ValueError: Series must have valuation one for reversion."""
    @overload
    def reverse(self) -> Any:
        """LaurentSeries.reverse(self, precision=None)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1417)

        Return the reverse of f, i.e., the series g such that g(f(x)) = x.
        Given an optional argument ``precision``, return the reverse with given
        precision (note that the reverse can have precision at most
        ``f.prec()``).  If ``f`` has infinite precision, and the argument
        ``precision`` is not given, then the precision of the reverse defaults
        to the default precision of ``f.parent()``.

        Note that this is only possible if the valuation of ``self`` is exactly
        1.

        The implementation depends on the underlying power series element
        implementing a reverse method.

        EXAMPLES::

            sage: R.<x> = Frac(QQ[['x']])
            sage: f = 2*x + 3*x^2 - x^4 + O(x^5)
            sage: g = f.reverse()
            sage: g
            1/2*x - 3/8*x^2 + 9/16*x^3 - 131/128*x^4 + O(x^5)
            sage: f(g)
            x + O(x^5)
            sage: g(f)
            x + O(x^5)

            sage: A.<t> = LaurentSeriesRing(ZZ)
            sage: a = t - t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + t^2 + 2*t^3 + 7*t^4 + 25*t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

            sage: B.<b,c> = ZZ[ ]
            sage: A.<t> = LaurentSeriesRing(B)
            sage: f = t + b*t^2 + c*t^3 + O(t^4)
            sage: g = f.reverse(); g
            t - b*t^2 + (2*b^2 - c)*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: B.<s> = LaurentSeriesRing(A)
            sage: f = (1 - 3*t + 4*t^3 + O(t^4))*s + (2 + t + t^2 + O(t^3))*s^2 + O(s^3)
            sage: set_verbose(1)
            sage: g = f.reverse(); g
            verbose 1 (<module>) passing to pari failed; trying Lagrange inversion
            (1 + 3*t + 9*t^2 + 23*t^3 + O(t^4))*s + (-2 - 19*t - 118*t^2 + O(t^3))*s^2 + O(s^3)
            sage: set_verbose(0)
            sage: f(g) == g(f) == s
            True

        If the leading coefficient is not a unit, we pass to its fraction
        field if possible::

            sage: A.<t> = LaurentSeriesRing(ZZ)
            sage: a = 2*t - 4*t^2 + t^4 - t^5 + O(t^6)
            sage: a.reverse()
            1/2*t + 1/2*t^2 + t^3 + 79/32*t^4 + 437/64*t^5 + O(t^6)

            sage: B.<b> = PolynomialRing(ZZ)
            sage: A.<t> = LaurentSeriesRing(B)
            sage: f = 2*b*t + b*t^2 + 3*b^2*t^3 + O(t^4)
            sage: g = f.reverse(); g
            1/(2*b)*t - 1/(8*b^2)*t^2 + ((-3*b + 1)/(16*b^3))*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

        We can handle some base rings of positive characteristic::

            sage: A8.<t> = LaurentSeriesRing(Zmod(8))
            sage: a = t - 15*t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + 7*t^2 + 2*t^3 + 5*t^4 + t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

        The optional argument ``precision`` sets the precision of the output::

            sage: R.<x> = LaurentSeriesRing(QQ)
            sage: f = 2*x + 3*x^2 - 7*x^3 + x^4 + O(x^5)
            sage: g = f.reverse(precision=3); g
            1/2*x - 3/8*x^2 + O(x^3)
            sage: f(g)
            x + O(x^3)
            sage: g(f)
            x + O(x^3)

        If the input series has infinite precision, the precision of the
        output is automatically set to the default precision of the parent
        ring::

            sage: R.<x> = LaurentSeriesRing(QQ, default_prec=20)
            sage: (x - x^2).reverse()  # get some Catalan numbers
            x + x^2 + 2*x^3 + 5*x^4 + 14*x^5 + 42*x^6 + 132*x^7 + 429*x^8 + 1430*x^9
             + 4862*x^10 + 16796*x^11 + 58786*x^12 + 208012*x^13 + 742900*x^14
             + 2674440*x^15 + 9694845*x^16 + 35357670*x^17 + 129644790*x^18
             + 477638700*x^19 + O(x^20)
            sage: (x - x^2).reverse(precision=3)
            x + x^2 + O(x^3)

        TESTS::

            sage: R.<x> = LaurentSeriesRing(QQ)
            sage: f = 1 + 2*x + 3*x^2 - x^4 + O(x^5)
            sage: f.reverse()
            Traceback (most recent call last):
            ...
            ValueError: Series must have valuation one for reversion."""
    @overload
    def reverse(self) -> Any:
        """LaurentSeries.reverse(self, precision=None)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1417)

        Return the reverse of f, i.e., the series g such that g(f(x)) = x.
        Given an optional argument ``precision``, return the reverse with given
        precision (note that the reverse can have precision at most
        ``f.prec()``).  If ``f`` has infinite precision, and the argument
        ``precision`` is not given, then the precision of the reverse defaults
        to the default precision of ``f.parent()``.

        Note that this is only possible if the valuation of ``self`` is exactly
        1.

        The implementation depends on the underlying power series element
        implementing a reverse method.

        EXAMPLES::

            sage: R.<x> = Frac(QQ[['x']])
            sage: f = 2*x + 3*x^2 - x^4 + O(x^5)
            sage: g = f.reverse()
            sage: g
            1/2*x - 3/8*x^2 + 9/16*x^3 - 131/128*x^4 + O(x^5)
            sage: f(g)
            x + O(x^5)
            sage: g(f)
            x + O(x^5)

            sage: A.<t> = LaurentSeriesRing(ZZ)
            sage: a = t - t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + t^2 + 2*t^3 + 7*t^4 + 25*t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

            sage: B.<b,c> = ZZ[ ]
            sage: A.<t> = LaurentSeriesRing(B)
            sage: f = t + b*t^2 + c*t^3 + O(t^4)
            sage: g = f.reverse(); g
            t - b*t^2 + (2*b^2 - c)*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: B.<s> = LaurentSeriesRing(A)
            sage: f = (1 - 3*t + 4*t^3 + O(t^4))*s + (2 + t + t^2 + O(t^3))*s^2 + O(s^3)
            sage: set_verbose(1)
            sage: g = f.reverse(); g
            verbose 1 (<module>) passing to pari failed; trying Lagrange inversion
            (1 + 3*t + 9*t^2 + 23*t^3 + O(t^4))*s + (-2 - 19*t - 118*t^2 + O(t^3))*s^2 + O(s^3)
            sage: set_verbose(0)
            sage: f(g) == g(f) == s
            True

        If the leading coefficient is not a unit, we pass to its fraction
        field if possible::

            sage: A.<t> = LaurentSeriesRing(ZZ)
            sage: a = 2*t - 4*t^2 + t^4 - t^5 + O(t^6)
            sage: a.reverse()
            1/2*t + 1/2*t^2 + t^3 + 79/32*t^4 + 437/64*t^5 + O(t^6)

            sage: B.<b> = PolynomialRing(ZZ)
            sage: A.<t> = LaurentSeriesRing(B)
            sage: f = 2*b*t + b*t^2 + 3*b^2*t^3 + O(t^4)
            sage: g = f.reverse(); g
            1/(2*b)*t - 1/(8*b^2)*t^2 + ((-3*b + 1)/(16*b^3))*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

        We can handle some base rings of positive characteristic::

            sage: A8.<t> = LaurentSeriesRing(Zmod(8))
            sage: a = t - 15*t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + 7*t^2 + 2*t^3 + 5*t^4 + t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

        The optional argument ``precision`` sets the precision of the output::

            sage: R.<x> = LaurentSeriesRing(QQ)
            sage: f = 2*x + 3*x^2 - 7*x^3 + x^4 + O(x^5)
            sage: g = f.reverse(precision=3); g
            1/2*x - 3/8*x^2 + O(x^3)
            sage: f(g)
            x + O(x^3)
            sage: g(f)
            x + O(x^3)

        If the input series has infinite precision, the precision of the
        output is automatically set to the default precision of the parent
        ring::

            sage: R.<x> = LaurentSeriesRing(QQ, default_prec=20)
            sage: (x - x^2).reverse()  # get some Catalan numbers
            x + x^2 + 2*x^3 + 5*x^4 + 14*x^5 + 42*x^6 + 132*x^7 + 429*x^8 + 1430*x^9
             + 4862*x^10 + 16796*x^11 + 58786*x^12 + 208012*x^13 + 742900*x^14
             + 2674440*x^15 + 9694845*x^16 + 35357670*x^17 + 129644790*x^18
             + 477638700*x^19 + O(x^20)
            sage: (x - x^2).reverse(precision=3)
            x + x^2 + O(x^3)

        TESTS::

            sage: R.<x> = LaurentSeriesRing(QQ)
            sage: f = 1 + 2*x + 3*x^2 - x^4 + O(x^5)
            sage: f.reverse()
            Traceback (most recent call last):
            ...
            ValueError: Series must have valuation one for reversion."""
    @overload
    def reverse(self) -> Any:
        """LaurentSeries.reverse(self, precision=None)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1417)

        Return the reverse of f, i.e., the series g such that g(f(x)) = x.
        Given an optional argument ``precision``, return the reverse with given
        precision (note that the reverse can have precision at most
        ``f.prec()``).  If ``f`` has infinite precision, and the argument
        ``precision`` is not given, then the precision of the reverse defaults
        to the default precision of ``f.parent()``.

        Note that this is only possible if the valuation of ``self`` is exactly
        1.

        The implementation depends on the underlying power series element
        implementing a reverse method.

        EXAMPLES::

            sage: R.<x> = Frac(QQ[['x']])
            sage: f = 2*x + 3*x^2 - x^4 + O(x^5)
            sage: g = f.reverse()
            sage: g
            1/2*x - 3/8*x^2 + 9/16*x^3 - 131/128*x^4 + O(x^5)
            sage: f(g)
            x + O(x^5)
            sage: g(f)
            x + O(x^5)

            sage: A.<t> = LaurentSeriesRing(ZZ)
            sage: a = t - t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + t^2 + 2*t^3 + 7*t^4 + 25*t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

            sage: B.<b,c> = ZZ[ ]
            sage: A.<t> = LaurentSeriesRing(B)
            sage: f = t + b*t^2 + c*t^3 + O(t^4)
            sage: g = f.reverse(); g
            t - b*t^2 + (2*b^2 - c)*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: B.<s> = LaurentSeriesRing(A)
            sage: f = (1 - 3*t + 4*t^3 + O(t^4))*s + (2 + t + t^2 + O(t^3))*s^2 + O(s^3)
            sage: set_verbose(1)
            sage: g = f.reverse(); g
            verbose 1 (<module>) passing to pari failed; trying Lagrange inversion
            (1 + 3*t + 9*t^2 + 23*t^3 + O(t^4))*s + (-2 - 19*t - 118*t^2 + O(t^3))*s^2 + O(s^3)
            sage: set_verbose(0)
            sage: f(g) == g(f) == s
            True

        If the leading coefficient is not a unit, we pass to its fraction
        field if possible::

            sage: A.<t> = LaurentSeriesRing(ZZ)
            sage: a = 2*t - 4*t^2 + t^4 - t^5 + O(t^6)
            sage: a.reverse()
            1/2*t + 1/2*t^2 + t^3 + 79/32*t^4 + 437/64*t^5 + O(t^6)

            sage: B.<b> = PolynomialRing(ZZ)
            sage: A.<t> = LaurentSeriesRing(B)
            sage: f = 2*b*t + b*t^2 + 3*b^2*t^3 + O(t^4)
            sage: g = f.reverse(); g
            1/(2*b)*t - 1/(8*b^2)*t^2 + ((-3*b + 1)/(16*b^3))*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

        We can handle some base rings of positive characteristic::

            sage: A8.<t> = LaurentSeriesRing(Zmod(8))
            sage: a = t - 15*t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + 7*t^2 + 2*t^3 + 5*t^4 + t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

        The optional argument ``precision`` sets the precision of the output::

            sage: R.<x> = LaurentSeriesRing(QQ)
            sage: f = 2*x + 3*x^2 - 7*x^3 + x^4 + O(x^5)
            sage: g = f.reverse(precision=3); g
            1/2*x - 3/8*x^2 + O(x^3)
            sage: f(g)
            x + O(x^3)
            sage: g(f)
            x + O(x^3)

        If the input series has infinite precision, the precision of the
        output is automatically set to the default precision of the parent
        ring::

            sage: R.<x> = LaurentSeriesRing(QQ, default_prec=20)
            sage: (x - x^2).reverse()  # get some Catalan numbers
            x + x^2 + 2*x^3 + 5*x^4 + 14*x^5 + 42*x^6 + 132*x^7 + 429*x^8 + 1430*x^9
             + 4862*x^10 + 16796*x^11 + 58786*x^12 + 208012*x^13 + 742900*x^14
             + 2674440*x^15 + 9694845*x^16 + 35357670*x^17 + 129644790*x^18
             + 477638700*x^19 + O(x^20)
            sage: (x - x^2).reverse(precision=3)
            x + x^2 + O(x^3)

        TESTS::

            sage: R.<x> = LaurentSeriesRing(QQ)
            sage: f = 1 + 2*x + 3*x^2 - x^4 + O(x^5)
            sage: f.reverse()
            Traceback (most recent call last):
            ...
            ValueError: Series must have valuation one for reversion."""
    @overload
    def reverse(self) -> Any:
        """LaurentSeries.reverse(self, precision=None)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1417)

        Return the reverse of f, i.e., the series g such that g(f(x)) = x.
        Given an optional argument ``precision``, return the reverse with given
        precision (note that the reverse can have precision at most
        ``f.prec()``).  If ``f`` has infinite precision, and the argument
        ``precision`` is not given, then the precision of the reverse defaults
        to the default precision of ``f.parent()``.

        Note that this is only possible if the valuation of ``self`` is exactly
        1.

        The implementation depends on the underlying power series element
        implementing a reverse method.

        EXAMPLES::

            sage: R.<x> = Frac(QQ[['x']])
            sage: f = 2*x + 3*x^2 - x^4 + O(x^5)
            sage: g = f.reverse()
            sage: g
            1/2*x - 3/8*x^2 + 9/16*x^3 - 131/128*x^4 + O(x^5)
            sage: f(g)
            x + O(x^5)
            sage: g(f)
            x + O(x^5)

            sage: A.<t> = LaurentSeriesRing(ZZ)
            sage: a = t - t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + t^2 + 2*t^3 + 7*t^4 + 25*t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

            sage: B.<b,c> = ZZ[ ]
            sage: A.<t> = LaurentSeriesRing(B)
            sage: f = t + b*t^2 + c*t^3 + O(t^4)
            sage: g = f.reverse(); g
            t - b*t^2 + (2*b^2 - c)*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: B.<s> = LaurentSeriesRing(A)
            sage: f = (1 - 3*t + 4*t^3 + O(t^4))*s + (2 + t + t^2 + O(t^3))*s^2 + O(s^3)
            sage: set_verbose(1)
            sage: g = f.reverse(); g
            verbose 1 (<module>) passing to pari failed; trying Lagrange inversion
            (1 + 3*t + 9*t^2 + 23*t^3 + O(t^4))*s + (-2 - 19*t - 118*t^2 + O(t^3))*s^2 + O(s^3)
            sage: set_verbose(0)
            sage: f(g) == g(f) == s
            True

        If the leading coefficient is not a unit, we pass to its fraction
        field if possible::

            sage: A.<t> = LaurentSeriesRing(ZZ)
            sage: a = 2*t - 4*t^2 + t^4 - t^5 + O(t^6)
            sage: a.reverse()
            1/2*t + 1/2*t^2 + t^3 + 79/32*t^4 + 437/64*t^5 + O(t^6)

            sage: B.<b> = PolynomialRing(ZZ)
            sage: A.<t> = LaurentSeriesRing(B)
            sage: f = 2*b*t + b*t^2 + 3*b^2*t^3 + O(t^4)
            sage: g = f.reverse(); g
            1/(2*b)*t - 1/(8*b^2)*t^2 + ((-3*b + 1)/(16*b^3))*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

        We can handle some base rings of positive characteristic::

            sage: A8.<t> = LaurentSeriesRing(Zmod(8))
            sage: a = t - 15*t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + 7*t^2 + 2*t^3 + 5*t^4 + t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

        The optional argument ``precision`` sets the precision of the output::

            sage: R.<x> = LaurentSeriesRing(QQ)
            sage: f = 2*x + 3*x^2 - 7*x^3 + x^4 + O(x^5)
            sage: g = f.reverse(precision=3); g
            1/2*x - 3/8*x^2 + O(x^3)
            sage: f(g)
            x + O(x^3)
            sage: g(f)
            x + O(x^3)

        If the input series has infinite precision, the precision of the
        output is automatically set to the default precision of the parent
        ring::

            sage: R.<x> = LaurentSeriesRing(QQ, default_prec=20)
            sage: (x - x^2).reverse()  # get some Catalan numbers
            x + x^2 + 2*x^3 + 5*x^4 + 14*x^5 + 42*x^6 + 132*x^7 + 429*x^8 + 1430*x^9
             + 4862*x^10 + 16796*x^11 + 58786*x^12 + 208012*x^13 + 742900*x^14
             + 2674440*x^15 + 9694845*x^16 + 35357670*x^17 + 129644790*x^18
             + 477638700*x^19 + O(x^20)
            sage: (x - x^2).reverse(precision=3)
            x + x^2 + O(x^3)

        TESTS::

            sage: R.<x> = LaurentSeriesRing(QQ)
            sage: f = 1 + 2*x + 3*x^2 - x^4 + O(x^5)
            sage: f.reverse()
            Traceback (most recent call last):
            ...
            ValueError: Series must have valuation one for reversion."""
    @overload
    def reverse(self) -> Any:
        """LaurentSeries.reverse(self, precision=None)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1417)

        Return the reverse of f, i.e., the series g such that g(f(x)) = x.
        Given an optional argument ``precision``, return the reverse with given
        precision (note that the reverse can have precision at most
        ``f.prec()``).  If ``f`` has infinite precision, and the argument
        ``precision`` is not given, then the precision of the reverse defaults
        to the default precision of ``f.parent()``.

        Note that this is only possible if the valuation of ``self`` is exactly
        1.

        The implementation depends on the underlying power series element
        implementing a reverse method.

        EXAMPLES::

            sage: R.<x> = Frac(QQ[['x']])
            sage: f = 2*x + 3*x^2 - x^4 + O(x^5)
            sage: g = f.reverse()
            sage: g
            1/2*x - 3/8*x^2 + 9/16*x^3 - 131/128*x^4 + O(x^5)
            sage: f(g)
            x + O(x^5)
            sage: g(f)
            x + O(x^5)

            sage: A.<t> = LaurentSeriesRing(ZZ)
            sage: a = t - t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + t^2 + 2*t^3 + 7*t^4 + 25*t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

            sage: B.<b,c> = ZZ[ ]
            sage: A.<t> = LaurentSeriesRing(B)
            sage: f = t + b*t^2 + c*t^3 + O(t^4)
            sage: g = f.reverse(); g
            t - b*t^2 + (2*b^2 - c)*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: B.<s> = LaurentSeriesRing(A)
            sage: f = (1 - 3*t + 4*t^3 + O(t^4))*s + (2 + t + t^2 + O(t^3))*s^2 + O(s^3)
            sage: set_verbose(1)
            sage: g = f.reverse(); g
            verbose 1 (<module>) passing to pari failed; trying Lagrange inversion
            (1 + 3*t + 9*t^2 + 23*t^3 + O(t^4))*s + (-2 - 19*t - 118*t^2 + O(t^3))*s^2 + O(s^3)
            sage: set_verbose(0)
            sage: f(g) == g(f) == s
            True

        If the leading coefficient is not a unit, we pass to its fraction
        field if possible::

            sage: A.<t> = LaurentSeriesRing(ZZ)
            sage: a = 2*t - 4*t^2 + t^4 - t^5 + O(t^6)
            sage: a.reverse()
            1/2*t + 1/2*t^2 + t^3 + 79/32*t^4 + 437/64*t^5 + O(t^6)

            sage: B.<b> = PolynomialRing(ZZ)
            sage: A.<t> = LaurentSeriesRing(B)
            sage: f = 2*b*t + b*t^2 + 3*b^2*t^3 + O(t^4)
            sage: g = f.reverse(); g
            1/(2*b)*t - 1/(8*b^2)*t^2 + ((-3*b + 1)/(16*b^3))*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

        We can handle some base rings of positive characteristic::

            sage: A8.<t> = LaurentSeriesRing(Zmod(8))
            sage: a = t - 15*t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + 7*t^2 + 2*t^3 + 5*t^4 + t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

        The optional argument ``precision`` sets the precision of the output::

            sage: R.<x> = LaurentSeriesRing(QQ)
            sage: f = 2*x + 3*x^2 - 7*x^3 + x^4 + O(x^5)
            sage: g = f.reverse(precision=3); g
            1/2*x - 3/8*x^2 + O(x^3)
            sage: f(g)
            x + O(x^3)
            sage: g(f)
            x + O(x^3)

        If the input series has infinite precision, the precision of the
        output is automatically set to the default precision of the parent
        ring::

            sage: R.<x> = LaurentSeriesRing(QQ, default_prec=20)
            sage: (x - x^2).reverse()  # get some Catalan numbers
            x + x^2 + 2*x^3 + 5*x^4 + 14*x^5 + 42*x^6 + 132*x^7 + 429*x^8 + 1430*x^9
             + 4862*x^10 + 16796*x^11 + 58786*x^12 + 208012*x^13 + 742900*x^14
             + 2674440*x^15 + 9694845*x^16 + 35357670*x^17 + 129644790*x^18
             + 477638700*x^19 + O(x^20)
            sage: (x - x^2).reverse(precision=3)
            x + x^2 + O(x^3)

        TESTS::

            sage: R.<x> = LaurentSeriesRing(QQ)
            sage: f = 1 + 2*x + 3*x^2 - x^4 + O(x^5)
            sage: f.reverse()
            Traceback (most recent call last):
            ...
            ValueError: Series must have valuation one for reversion."""
    @overload
    def reverse(self) -> Any:
        """LaurentSeries.reverse(self, precision=None)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1417)

        Return the reverse of f, i.e., the series g such that g(f(x)) = x.
        Given an optional argument ``precision``, return the reverse with given
        precision (note that the reverse can have precision at most
        ``f.prec()``).  If ``f`` has infinite precision, and the argument
        ``precision`` is not given, then the precision of the reverse defaults
        to the default precision of ``f.parent()``.

        Note that this is only possible if the valuation of ``self`` is exactly
        1.

        The implementation depends on the underlying power series element
        implementing a reverse method.

        EXAMPLES::

            sage: R.<x> = Frac(QQ[['x']])
            sage: f = 2*x + 3*x^2 - x^4 + O(x^5)
            sage: g = f.reverse()
            sage: g
            1/2*x - 3/8*x^2 + 9/16*x^3 - 131/128*x^4 + O(x^5)
            sage: f(g)
            x + O(x^5)
            sage: g(f)
            x + O(x^5)

            sage: A.<t> = LaurentSeriesRing(ZZ)
            sage: a = t - t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + t^2 + 2*t^3 + 7*t^4 + 25*t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

            sage: B.<b,c> = ZZ[ ]
            sage: A.<t> = LaurentSeriesRing(B)
            sage: f = t + b*t^2 + c*t^3 + O(t^4)
            sage: g = f.reverse(); g
            t - b*t^2 + (2*b^2 - c)*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: B.<s> = LaurentSeriesRing(A)
            sage: f = (1 - 3*t + 4*t^3 + O(t^4))*s + (2 + t + t^2 + O(t^3))*s^2 + O(s^3)
            sage: set_verbose(1)
            sage: g = f.reverse(); g
            verbose 1 (<module>) passing to pari failed; trying Lagrange inversion
            (1 + 3*t + 9*t^2 + 23*t^3 + O(t^4))*s + (-2 - 19*t - 118*t^2 + O(t^3))*s^2 + O(s^3)
            sage: set_verbose(0)
            sage: f(g) == g(f) == s
            True

        If the leading coefficient is not a unit, we pass to its fraction
        field if possible::

            sage: A.<t> = LaurentSeriesRing(ZZ)
            sage: a = 2*t - 4*t^2 + t^4 - t^5 + O(t^6)
            sage: a.reverse()
            1/2*t + 1/2*t^2 + t^3 + 79/32*t^4 + 437/64*t^5 + O(t^6)

            sage: B.<b> = PolynomialRing(ZZ)
            sage: A.<t> = LaurentSeriesRing(B)
            sage: f = 2*b*t + b*t^2 + 3*b^2*t^3 + O(t^4)
            sage: g = f.reverse(); g
            1/(2*b)*t - 1/(8*b^2)*t^2 + ((-3*b + 1)/(16*b^3))*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

        We can handle some base rings of positive characteristic::

            sage: A8.<t> = LaurentSeriesRing(Zmod(8))
            sage: a = t - 15*t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + 7*t^2 + 2*t^3 + 5*t^4 + t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

        The optional argument ``precision`` sets the precision of the output::

            sage: R.<x> = LaurentSeriesRing(QQ)
            sage: f = 2*x + 3*x^2 - 7*x^3 + x^4 + O(x^5)
            sage: g = f.reverse(precision=3); g
            1/2*x - 3/8*x^2 + O(x^3)
            sage: f(g)
            x + O(x^3)
            sage: g(f)
            x + O(x^3)

        If the input series has infinite precision, the precision of the
        output is automatically set to the default precision of the parent
        ring::

            sage: R.<x> = LaurentSeriesRing(QQ, default_prec=20)
            sage: (x - x^2).reverse()  # get some Catalan numbers
            x + x^2 + 2*x^3 + 5*x^4 + 14*x^5 + 42*x^6 + 132*x^7 + 429*x^8 + 1430*x^9
             + 4862*x^10 + 16796*x^11 + 58786*x^12 + 208012*x^13 + 742900*x^14
             + 2674440*x^15 + 9694845*x^16 + 35357670*x^17 + 129644790*x^18
             + 477638700*x^19 + O(x^20)
            sage: (x - x^2).reverse(precision=3)
            x + x^2 + O(x^3)

        TESTS::

            sage: R.<x> = LaurentSeriesRing(QQ)
            sage: f = 1 + 2*x + 3*x^2 - x^4 + O(x^5)
            sage: f.reverse()
            Traceback (most recent call last):
            ...
            ValueError: Series must have valuation one for reversion."""
    @overload
    def reverse(self, precision=...) -> Any:
        """LaurentSeries.reverse(self, precision=None)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1417)

        Return the reverse of f, i.e., the series g such that g(f(x)) = x.
        Given an optional argument ``precision``, return the reverse with given
        precision (note that the reverse can have precision at most
        ``f.prec()``).  If ``f`` has infinite precision, and the argument
        ``precision`` is not given, then the precision of the reverse defaults
        to the default precision of ``f.parent()``.

        Note that this is only possible if the valuation of ``self`` is exactly
        1.

        The implementation depends on the underlying power series element
        implementing a reverse method.

        EXAMPLES::

            sage: R.<x> = Frac(QQ[['x']])
            sage: f = 2*x + 3*x^2 - x^4 + O(x^5)
            sage: g = f.reverse()
            sage: g
            1/2*x - 3/8*x^2 + 9/16*x^3 - 131/128*x^4 + O(x^5)
            sage: f(g)
            x + O(x^5)
            sage: g(f)
            x + O(x^5)

            sage: A.<t> = LaurentSeriesRing(ZZ)
            sage: a = t - t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + t^2 + 2*t^3 + 7*t^4 + 25*t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

            sage: B.<b,c> = ZZ[ ]
            sage: A.<t> = LaurentSeriesRing(B)
            sage: f = t + b*t^2 + c*t^3 + O(t^4)
            sage: g = f.reverse(); g
            t - b*t^2 + (2*b^2 - c)*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: B.<s> = LaurentSeriesRing(A)
            sage: f = (1 - 3*t + 4*t^3 + O(t^4))*s + (2 + t + t^2 + O(t^3))*s^2 + O(s^3)
            sage: set_verbose(1)
            sage: g = f.reverse(); g
            verbose 1 (<module>) passing to pari failed; trying Lagrange inversion
            (1 + 3*t + 9*t^2 + 23*t^3 + O(t^4))*s + (-2 - 19*t - 118*t^2 + O(t^3))*s^2 + O(s^3)
            sage: set_verbose(0)
            sage: f(g) == g(f) == s
            True

        If the leading coefficient is not a unit, we pass to its fraction
        field if possible::

            sage: A.<t> = LaurentSeriesRing(ZZ)
            sage: a = 2*t - 4*t^2 + t^4 - t^5 + O(t^6)
            sage: a.reverse()
            1/2*t + 1/2*t^2 + t^3 + 79/32*t^4 + 437/64*t^5 + O(t^6)

            sage: B.<b> = PolynomialRing(ZZ)
            sage: A.<t> = LaurentSeriesRing(B)
            sage: f = 2*b*t + b*t^2 + 3*b^2*t^3 + O(t^4)
            sage: g = f.reverse(); g
            1/(2*b)*t - 1/(8*b^2)*t^2 + ((-3*b + 1)/(16*b^3))*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

        We can handle some base rings of positive characteristic::

            sage: A8.<t> = LaurentSeriesRing(Zmod(8))
            sage: a = t - 15*t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + 7*t^2 + 2*t^3 + 5*t^4 + t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

        The optional argument ``precision`` sets the precision of the output::

            sage: R.<x> = LaurentSeriesRing(QQ)
            sage: f = 2*x + 3*x^2 - 7*x^3 + x^4 + O(x^5)
            sage: g = f.reverse(precision=3); g
            1/2*x - 3/8*x^2 + O(x^3)
            sage: f(g)
            x + O(x^3)
            sage: g(f)
            x + O(x^3)

        If the input series has infinite precision, the precision of the
        output is automatically set to the default precision of the parent
        ring::

            sage: R.<x> = LaurentSeriesRing(QQ, default_prec=20)
            sage: (x - x^2).reverse()  # get some Catalan numbers
            x + x^2 + 2*x^3 + 5*x^4 + 14*x^5 + 42*x^6 + 132*x^7 + 429*x^8 + 1430*x^9
             + 4862*x^10 + 16796*x^11 + 58786*x^12 + 208012*x^13 + 742900*x^14
             + 2674440*x^15 + 9694845*x^16 + 35357670*x^17 + 129644790*x^18
             + 477638700*x^19 + O(x^20)
            sage: (x - x^2).reverse(precision=3)
            x + x^2 + O(x^3)

        TESTS::

            sage: R.<x> = LaurentSeriesRing(QQ)
            sage: f = 1 + 2*x + 3*x^2 - x^4 + O(x^5)
            sage: f.reverse()
            Traceback (most recent call last):
            ...
            ValueError: Series must have valuation one for reversion."""
    @overload
    def reverse(self) -> Any:
        """LaurentSeries.reverse(self, precision=None)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1417)

        Return the reverse of f, i.e., the series g such that g(f(x)) = x.
        Given an optional argument ``precision``, return the reverse with given
        precision (note that the reverse can have precision at most
        ``f.prec()``).  If ``f`` has infinite precision, and the argument
        ``precision`` is not given, then the precision of the reverse defaults
        to the default precision of ``f.parent()``.

        Note that this is only possible if the valuation of ``self`` is exactly
        1.

        The implementation depends on the underlying power series element
        implementing a reverse method.

        EXAMPLES::

            sage: R.<x> = Frac(QQ[['x']])
            sage: f = 2*x + 3*x^2 - x^4 + O(x^5)
            sage: g = f.reverse()
            sage: g
            1/2*x - 3/8*x^2 + 9/16*x^3 - 131/128*x^4 + O(x^5)
            sage: f(g)
            x + O(x^5)
            sage: g(f)
            x + O(x^5)

            sage: A.<t> = LaurentSeriesRing(ZZ)
            sage: a = t - t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + t^2 + 2*t^3 + 7*t^4 + 25*t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

            sage: B.<b,c> = ZZ[ ]
            sage: A.<t> = LaurentSeriesRing(B)
            sage: f = t + b*t^2 + c*t^3 + O(t^4)
            sage: g = f.reverse(); g
            t - b*t^2 + (2*b^2 - c)*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: B.<s> = LaurentSeriesRing(A)
            sage: f = (1 - 3*t + 4*t^3 + O(t^4))*s + (2 + t + t^2 + O(t^3))*s^2 + O(s^3)
            sage: set_verbose(1)
            sage: g = f.reverse(); g
            verbose 1 (<module>) passing to pari failed; trying Lagrange inversion
            (1 + 3*t + 9*t^2 + 23*t^3 + O(t^4))*s + (-2 - 19*t - 118*t^2 + O(t^3))*s^2 + O(s^3)
            sage: set_verbose(0)
            sage: f(g) == g(f) == s
            True

        If the leading coefficient is not a unit, we pass to its fraction
        field if possible::

            sage: A.<t> = LaurentSeriesRing(ZZ)
            sage: a = 2*t - 4*t^2 + t^4 - t^5 + O(t^6)
            sage: a.reverse()
            1/2*t + 1/2*t^2 + t^3 + 79/32*t^4 + 437/64*t^5 + O(t^6)

            sage: B.<b> = PolynomialRing(ZZ)
            sage: A.<t> = LaurentSeriesRing(B)
            sage: f = 2*b*t + b*t^2 + 3*b^2*t^3 + O(t^4)
            sage: g = f.reverse(); g
            1/(2*b)*t - 1/(8*b^2)*t^2 + ((-3*b + 1)/(16*b^3))*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

        We can handle some base rings of positive characteristic::

            sage: A8.<t> = LaurentSeriesRing(Zmod(8))
            sage: a = t - 15*t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + 7*t^2 + 2*t^3 + 5*t^4 + t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

        The optional argument ``precision`` sets the precision of the output::

            sage: R.<x> = LaurentSeriesRing(QQ)
            sage: f = 2*x + 3*x^2 - 7*x^3 + x^4 + O(x^5)
            sage: g = f.reverse(precision=3); g
            1/2*x - 3/8*x^2 + O(x^3)
            sage: f(g)
            x + O(x^3)
            sage: g(f)
            x + O(x^3)

        If the input series has infinite precision, the precision of the
        output is automatically set to the default precision of the parent
        ring::

            sage: R.<x> = LaurentSeriesRing(QQ, default_prec=20)
            sage: (x - x^2).reverse()  # get some Catalan numbers
            x + x^2 + 2*x^3 + 5*x^4 + 14*x^5 + 42*x^6 + 132*x^7 + 429*x^8 + 1430*x^9
             + 4862*x^10 + 16796*x^11 + 58786*x^12 + 208012*x^13 + 742900*x^14
             + 2674440*x^15 + 9694845*x^16 + 35357670*x^17 + 129644790*x^18
             + 477638700*x^19 + O(x^20)
            sage: (x - x^2).reverse(precision=3)
            x + x^2 + O(x^3)

        TESTS::

            sage: R.<x> = LaurentSeriesRing(QQ)
            sage: f = 1 + 2*x + 3*x^2 - x^4 + O(x^5)
            sage: f.reverse()
            Traceback (most recent call last):
            ...
            ValueError: Series must have valuation one for reversion."""
    @overload
    def reverse(self, precision=...) -> Any:
        """LaurentSeries.reverse(self, precision=None)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1417)

        Return the reverse of f, i.e., the series g such that g(f(x)) = x.
        Given an optional argument ``precision``, return the reverse with given
        precision (note that the reverse can have precision at most
        ``f.prec()``).  If ``f`` has infinite precision, and the argument
        ``precision`` is not given, then the precision of the reverse defaults
        to the default precision of ``f.parent()``.

        Note that this is only possible if the valuation of ``self`` is exactly
        1.

        The implementation depends on the underlying power series element
        implementing a reverse method.

        EXAMPLES::

            sage: R.<x> = Frac(QQ[['x']])
            sage: f = 2*x + 3*x^2 - x^4 + O(x^5)
            sage: g = f.reverse()
            sage: g
            1/2*x - 3/8*x^2 + 9/16*x^3 - 131/128*x^4 + O(x^5)
            sage: f(g)
            x + O(x^5)
            sage: g(f)
            x + O(x^5)

            sage: A.<t> = LaurentSeriesRing(ZZ)
            sage: a = t - t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + t^2 + 2*t^3 + 7*t^4 + 25*t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

            sage: B.<b,c> = ZZ[ ]
            sage: A.<t> = LaurentSeriesRing(B)
            sage: f = t + b*t^2 + c*t^3 + O(t^4)
            sage: g = f.reverse(); g
            t - b*t^2 + (2*b^2 - c)*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: B.<s> = LaurentSeriesRing(A)
            sage: f = (1 - 3*t + 4*t^3 + O(t^4))*s + (2 + t + t^2 + O(t^3))*s^2 + O(s^3)
            sage: set_verbose(1)
            sage: g = f.reverse(); g
            verbose 1 (<module>) passing to pari failed; trying Lagrange inversion
            (1 + 3*t + 9*t^2 + 23*t^3 + O(t^4))*s + (-2 - 19*t - 118*t^2 + O(t^3))*s^2 + O(s^3)
            sage: set_verbose(0)
            sage: f(g) == g(f) == s
            True

        If the leading coefficient is not a unit, we pass to its fraction
        field if possible::

            sage: A.<t> = LaurentSeriesRing(ZZ)
            sage: a = 2*t - 4*t^2 + t^4 - t^5 + O(t^6)
            sage: a.reverse()
            1/2*t + 1/2*t^2 + t^3 + 79/32*t^4 + 437/64*t^5 + O(t^6)

            sage: B.<b> = PolynomialRing(ZZ)
            sage: A.<t> = LaurentSeriesRing(B)
            sage: f = 2*b*t + b*t^2 + 3*b^2*t^3 + O(t^4)
            sage: g = f.reverse(); g
            1/(2*b)*t - 1/(8*b^2)*t^2 + ((-3*b + 1)/(16*b^3))*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

        We can handle some base rings of positive characteristic::

            sage: A8.<t> = LaurentSeriesRing(Zmod(8))
            sage: a = t - 15*t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + 7*t^2 + 2*t^3 + 5*t^4 + t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

        The optional argument ``precision`` sets the precision of the output::

            sage: R.<x> = LaurentSeriesRing(QQ)
            sage: f = 2*x + 3*x^2 - 7*x^3 + x^4 + O(x^5)
            sage: g = f.reverse(precision=3); g
            1/2*x - 3/8*x^2 + O(x^3)
            sage: f(g)
            x + O(x^3)
            sage: g(f)
            x + O(x^3)

        If the input series has infinite precision, the precision of the
        output is automatically set to the default precision of the parent
        ring::

            sage: R.<x> = LaurentSeriesRing(QQ, default_prec=20)
            sage: (x - x^2).reverse()  # get some Catalan numbers
            x + x^2 + 2*x^3 + 5*x^4 + 14*x^5 + 42*x^6 + 132*x^7 + 429*x^8 + 1430*x^9
             + 4862*x^10 + 16796*x^11 + 58786*x^12 + 208012*x^13 + 742900*x^14
             + 2674440*x^15 + 9694845*x^16 + 35357670*x^17 + 129644790*x^18
             + 477638700*x^19 + O(x^20)
            sage: (x - x^2).reverse(precision=3)
            x + x^2 + O(x^3)

        TESTS::

            sage: R.<x> = LaurentSeriesRing(QQ)
            sage: f = 1 + 2*x + 3*x^2 - x^4 + O(x^5)
            sage: f.reverse()
            Traceback (most recent call last):
            ...
            ValueError: Series must have valuation one for reversion."""
    @overload
    def reverse(self) -> Any:
        """LaurentSeries.reverse(self, precision=None)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1417)

        Return the reverse of f, i.e., the series g such that g(f(x)) = x.
        Given an optional argument ``precision``, return the reverse with given
        precision (note that the reverse can have precision at most
        ``f.prec()``).  If ``f`` has infinite precision, and the argument
        ``precision`` is not given, then the precision of the reverse defaults
        to the default precision of ``f.parent()``.

        Note that this is only possible if the valuation of ``self`` is exactly
        1.

        The implementation depends on the underlying power series element
        implementing a reverse method.

        EXAMPLES::

            sage: R.<x> = Frac(QQ[['x']])
            sage: f = 2*x + 3*x^2 - x^4 + O(x^5)
            sage: g = f.reverse()
            sage: g
            1/2*x - 3/8*x^2 + 9/16*x^3 - 131/128*x^4 + O(x^5)
            sage: f(g)
            x + O(x^5)
            sage: g(f)
            x + O(x^5)

            sage: A.<t> = LaurentSeriesRing(ZZ)
            sage: a = t - t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + t^2 + 2*t^3 + 7*t^4 + 25*t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

            sage: B.<b,c> = ZZ[ ]
            sage: A.<t> = LaurentSeriesRing(B)
            sage: f = t + b*t^2 + c*t^3 + O(t^4)
            sage: g = f.reverse(); g
            t - b*t^2 + (2*b^2 - c)*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: B.<s> = LaurentSeriesRing(A)
            sage: f = (1 - 3*t + 4*t^3 + O(t^4))*s + (2 + t + t^2 + O(t^3))*s^2 + O(s^3)
            sage: set_verbose(1)
            sage: g = f.reverse(); g
            verbose 1 (<module>) passing to pari failed; trying Lagrange inversion
            (1 + 3*t + 9*t^2 + 23*t^3 + O(t^4))*s + (-2 - 19*t - 118*t^2 + O(t^3))*s^2 + O(s^3)
            sage: set_verbose(0)
            sage: f(g) == g(f) == s
            True

        If the leading coefficient is not a unit, we pass to its fraction
        field if possible::

            sage: A.<t> = LaurentSeriesRing(ZZ)
            sage: a = 2*t - 4*t^2 + t^4 - t^5 + O(t^6)
            sage: a.reverse()
            1/2*t + 1/2*t^2 + t^3 + 79/32*t^4 + 437/64*t^5 + O(t^6)

            sage: B.<b> = PolynomialRing(ZZ)
            sage: A.<t> = LaurentSeriesRing(B)
            sage: f = 2*b*t + b*t^2 + 3*b^2*t^3 + O(t^4)
            sage: g = f.reverse(); g
            1/(2*b)*t - 1/(8*b^2)*t^2 + ((-3*b + 1)/(16*b^3))*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

        We can handle some base rings of positive characteristic::

            sage: A8.<t> = LaurentSeriesRing(Zmod(8))
            sage: a = t - 15*t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + 7*t^2 + 2*t^3 + 5*t^4 + t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

        The optional argument ``precision`` sets the precision of the output::

            sage: R.<x> = LaurentSeriesRing(QQ)
            sage: f = 2*x + 3*x^2 - 7*x^3 + x^4 + O(x^5)
            sage: g = f.reverse(precision=3); g
            1/2*x - 3/8*x^2 + O(x^3)
            sage: f(g)
            x + O(x^3)
            sage: g(f)
            x + O(x^3)

        If the input series has infinite precision, the precision of the
        output is automatically set to the default precision of the parent
        ring::

            sage: R.<x> = LaurentSeriesRing(QQ, default_prec=20)
            sage: (x - x^2).reverse()  # get some Catalan numbers
            x + x^2 + 2*x^3 + 5*x^4 + 14*x^5 + 42*x^6 + 132*x^7 + 429*x^8 + 1430*x^9
             + 4862*x^10 + 16796*x^11 + 58786*x^12 + 208012*x^13 + 742900*x^14
             + 2674440*x^15 + 9694845*x^16 + 35357670*x^17 + 129644790*x^18
             + 477638700*x^19 + O(x^20)
            sage: (x - x^2).reverse(precision=3)
            x + x^2 + O(x^3)

        TESTS::

            sage: R.<x> = LaurentSeriesRing(QQ)
            sage: f = 1 + 2*x + 3*x^2 - x^4 + O(x^5)
            sage: f.reverse()
            Traceback (most recent call last):
            ...
            ValueError: Series must have valuation one for reversion."""
    def shift(self, k) -> Any:
        """LaurentSeries.shift(self, k)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 990)

        Return this Laurent series multiplied by the power `t^n`.
        Does not change this series.

        .. NOTE::

           Despite the fact that higher order terms are printed to the
           right in a power series, right shifting decreases the
           powers of `t`, while left shifting increases
           them. This is to be consistent with polynomials, integers,
           etc.

        EXAMPLES::

            sage: R.<t> = LaurentSeriesRing(QQ['y'])
            sage: f = (t+t^-1)^4; f
            t^-4 + 4*t^-2 + 6 + 4*t^2 + t^4
            sage: f.shift(10)
            t^6 + 4*t^8 + 6*t^10 + 4*t^12 + t^14
            sage: f >> 10
            t^-14 + 4*t^-12 + 6*t^-10 + 4*t^-8 + t^-6
            sage: t << 4
            t^5
            sage: t + O(t^3) >> 4
            t^-3 + O(t^-1)

        AUTHORS:

        - Robert Bradshaw (2007-04-18)"""
    def truncate(self, longn) -> Any:
        """LaurentSeries.truncate(self, long n)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1029)

        Return the Laurent series of degree ` < n` which is
        equivalent to ``self`` modulo `x^n`.

        EXAMPLES::

            sage: A.<x> = LaurentSeriesRing(ZZ)
            sage: f = 1/(1-x)
            sage: f
            1 + x + x^2 + x^3 + x^4 + x^5 + x^6 + x^7 + x^8 + x^9 + x^10 + x^11
             + x^12 + x^13 + x^14 + x^15 + x^16 + x^17 + x^18 + x^19 + O(x^20)
            sage: f.truncate(10)
            1 + x + x^2 + x^3 + x^4 + x^5 + x^6 + x^7 + x^8 + x^9"""
    def truncate_laurentseries(self, longn) -> Any:
        """LaurentSeries.truncate_laurentseries(self, long n)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1049)

        Replace any terms of degree >= n by big oh.

        EXAMPLES::

            sage: A.<x> = LaurentSeriesRing(ZZ)
            sage: f = 1/(1-x)
            sage: f
            1 + x + x^2 + x^3 + x^4 + x^5 + x^6 + x^7 + x^8 + x^9 + x^10 + x^11
             + x^12 + x^13 + x^14 + x^15 + x^16 + x^17 + x^18 + x^19 + O(x^20)
            sage: f.truncate_laurentseries(10)
            1 + x + x^2 + x^3 + x^4 + x^5 + x^6 + x^7 + x^8 + x^9 + O(x^10)"""
    def truncate_neg(self, longn) -> Any:
        '''LaurentSeries.truncate_neg(self, long n)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1068)

        Return the Laurent series equivalent to ``self`` except without any
        degree ``n`` terms.

        This is equivalent to::

            ``self - self.truncate(n)``

        EXAMPLES::

            sage: A.<t> = LaurentSeriesRing(ZZ)
            sage: f = 1/(1-t)
            sage: f.truncate_neg(15)
            t^15 + t^16 + t^17 + t^18 + t^19 + O(t^20)

        TESTS:

        Check that :issue:`39710` is fixed::

            sage: S.<t> = LaurentSeriesRing(QQ)
            sage: (t+t^2).truncate_neg(-1)
            t + t^2
            sage: (t+t^2).truncate_neg(-2)
            t + t^2

        Check that :issue:`39842` is fixed::

            sage: f = LaurentSeriesRing(QQ, "t")(LaurentPolynomialRing(QQ, "t")([1, 2, 3]))
            sage: f
            1 + 2*t + 3*t^2
            sage: f.truncate_neg(1)
            2*t + 3*t^2'''
    @overload
    def valuation(self) -> Any:
        """LaurentSeries.valuation(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1310)

        EXAMPLES::

            sage: R.<x> = LaurentSeriesRing(QQ)
            sage: f = 1/x + x^2 + 3*x^4 + O(x^7)
            sage: g = 1 - x + x^2 - x^4 + O(x^8)
            sage: f.valuation()
            -1
            sage: g.valuation()
            0

        Note that the valuation of an element indistinguishable from
        zero is infinite::

            sage: h = f - f; h
            O(x^7)
            sage: h.valuation()
            +Infinity

        TESTS:

        The valuation of the zero element is ``+Infinity``
        (see :issue:`15088`)::

            sage: zero = R(0)
            sage: zero.valuation()
            +Infinity"""
    @overload
    def valuation(self) -> Any:
        """LaurentSeries.valuation(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1310)

        EXAMPLES::

            sage: R.<x> = LaurentSeriesRing(QQ)
            sage: f = 1/x + x^2 + 3*x^4 + O(x^7)
            sage: g = 1 - x + x^2 - x^4 + O(x^8)
            sage: f.valuation()
            -1
            sage: g.valuation()
            0

        Note that the valuation of an element indistinguishable from
        zero is infinite::

            sage: h = f - f; h
            O(x^7)
            sage: h.valuation()
            +Infinity

        TESTS:

        The valuation of the zero element is ``+Infinity``
        (see :issue:`15088`)::

            sage: zero = R(0)
            sage: zero.valuation()
            +Infinity"""
    @overload
    def valuation(self) -> Any:
        """LaurentSeries.valuation(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1310)

        EXAMPLES::

            sage: R.<x> = LaurentSeriesRing(QQ)
            sage: f = 1/x + x^2 + 3*x^4 + O(x^7)
            sage: g = 1 - x + x^2 - x^4 + O(x^8)
            sage: f.valuation()
            -1
            sage: g.valuation()
            0

        Note that the valuation of an element indistinguishable from
        zero is infinite::

            sage: h = f - f; h
            O(x^7)
            sage: h.valuation()
            +Infinity

        TESTS:

        The valuation of the zero element is ``+Infinity``
        (see :issue:`15088`)::

            sage: zero = R(0)
            sage: zero.valuation()
            +Infinity"""
    @overload
    def valuation(self) -> Any:
        """LaurentSeries.valuation(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1310)

        EXAMPLES::

            sage: R.<x> = LaurentSeriesRing(QQ)
            sage: f = 1/x + x^2 + 3*x^4 + O(x^7)
            sage: g = 1 - x + x^2 - x^4 + O(x^8)
            sage: f.valuation()
            -1
            sage: g.valuation()
            0

        Note that the valuation of an element indistinguishable from
        zero is infinite::

            sage: h = f - f; h
            O(x^7)
            sage: h.valuation()
            +Infinity

        TESTS:

        The valuation of the zero element is ``+Infinity``
        (see :issue:`15088`)::

            sage: zero = R(0)
            sage: zero.valuation()
            +Infinity"""
    @overload
    def valuation(self) -> Any:
        """LaurentSeries.valuation(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1310)

        EXAMPLES::

            sage: R.<x> = LaurentSeriesRing(QQ)
            sage: f = 1/x + x^2 + 3*x^4 + O(x^7)
            sage: g = 1 - x + x^2 - x^4 + O(x^8)
            sage: f.valuation()
            -1
            sage: g.valuation()
            0

        Note that the valuation of an element indistinguishable from
        zero is infinite::

            sage: h = f - f; h
            O(x^7)
            sage: h.valuation()
            +Infinity

        TESTS:

        The valuation of the zero element is ``+Infinity``
        (see :issue:`15088`)::

            sage: zero = R(0)
            sage: zero.valuation()
            +Infinity"""
    @overload
    def valuation_zero_part(self) -> Any:
        """LaurentSeries.valuation_zero_part(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1294)

        EXAMPLES::

            sage: x = Frac(QQ[['x']]).0
            sage: f = x + x^2 + 3*x^4 + O(x^7)
            sage: f/x
            1 + x + 3*x^3 + O(x^6)
            sage: f.valuation_zero_part()
            1 + x + 3*x^3 + O(x^6)
            sage: g = 1/x^7 - x + x^2 - x^4 + O(x^8)
            sage: g.valuation_zero_part()
            1 - x^8 + x^9 - x^11 + O(x^15)"""
    @overload
    def valuation_zero_part(self) -> Any:
        """LaurentSeries.valuation_zero_part(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1294)

        EXAMPLES::

            sage: x = Frac(QQ[['x']]).0
            sage: f = x + x^2 + 3*x^4 + O(x^7)
            sage: f/x
            1 + x + 3*x^3 + O(x^6)
            sage: f.valuation_zero_part()
            1 + x + 3*x^3 + O(x^6)
            sage: g = 1/x^7 - x + x^2 - x^4 + O(x^8)
            sage: g.valuation_zero_part()
            1 - x^8 + x^9 - x^11 + O(x^15)"""
    @overload
    def valuation_zero_part(self) -> Any:
        """LaurentSeries.valuation_zero_part(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1294)

        EXAMPLES::

            sage: x = Frac(QQ[['x']]).0
            sage: f = x + x^2 + 3*x^4 + O(x^7)
            sage: f/x
            1 + x + 3*x^3 + O(x^6)
            sage: f.valuation_zero_part()
            1 + x + 3*x^3 + O(x^6)
            sage: g = 1/x^7 - x + x^2 - x^4 + O(x^8)
            sage: g.valuation_zero_part()
            1 - x^8 + x^9 - x^11 + O(x^15)"""
    @overload
    def variable(self) -> Any:
        """LaurentSeries.variable(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1343)

        EXAMPLES::

            sage: x = Frac(QQ[['x']]).0
            sage: f = 1/x + x^2 + 3*x^4 + O(x^7)
            sage: f.variable()
            'x'"""
    @overload
    def variable(self) -> Any:
        """LaurentSeries.variable(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1343)

        EXAMPLES::

            sage: x = Frac(QQ[['x']]).0
            sage: f = 1/x + x^2 + 3*x^4 + O(x^7)
            sage: f.variable()
            'x'"""
    def verschiebung(self, n) -> Any:
        """LaurentSeries.verschiebung(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 375)

        Return the ``n``-th Verschiebung of ``self``.

        If `f = \\sum a_m x^m` then this function returns `\\sum a_m x^{mn}`.

        EXAMPLES::

            sage: R.<x> = LaurentSeriesRing(QQ)
            sage: f = -1/x + 1 + 2*x^2 + 5*x^5
            sage: f.V(2)
            -x^-2 + 1 + 2*x^4 + 5*x^10
            sage: f.V(-1)
            5*x^-5 + 2*x^-2 + 1 - x
            sage: h = f.add_bigoh(7)
            sage: h.V(2)
            -x^-2 + 1 + 2*x^4 + 5*x^10 + O(x^14)
            sage: h.V(-2)
            Traceback (most recent call last):
            ...
            ValueError: For finite precision only positive arguments allowed

        TESTS::

            sage: R.<x> = LaurentSeriesRing(QQ)
            sage: f = x
            sage: f.V(3)
            x^3
            sage: f.V(-3)
            x^-3
            sage: g = 2*x^(-1) + 3 + 5*x
            sage: g.V(-1)
            5*x^-1 + 3 + 2*x"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __call__(self, *x, **kwds) -> Any:
        """LaurentSeries.__call__(self, *x, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1823)

        Compute value of this Laurent series at x.

        EXAMPLES::

            sage: P.<x, y> = ZZ[]
            sage: R.<t> = LaurentSeriesRing(P)
            sage: f = x*t^-2 + y*t^2 + O(t^8)
            sage: f(t^3)
            x*t^-6 + y*t^6 + O(t^24)
            sage: f(t=t^3)
            x*t^-6 + y*t^6 + O(t^24)
            sage: f(t + O(t^5))
            x*t^-2 + O(t^2)
            sage: f(y=x)
            x*t^-2 + x*t^2 + O(t^8)
            sage: f(t^3, x=2, y=x + x^2)
            2*t^-6 + (x^2 + x)*t^6 + O(t^24)
            sage: f(t^3, 2, x+x^2)
            2*t^-6 + (x^2 + x)*t^6 + O(t^24)
            sage: f(x=2, t=t^3, y=x + x^2)
            2*t^-6 + (x^2 + x)*t^6 + O(t^24)
            sage: f(2, x + x^2, t=t^3)
            Traceback (most recent call last):
            ...
            ValueError: must not specify t keyword and positional argument

        It is only possible to substitute elements of positive valuation::

            sage: f(t^-2)
            Traceback (most recent call last):
            ...
            ValueError: Can only substitute elements of positive valuation

        Test for :issue:`23928`::

            sage: R.<x> = LaurentSeriesRing(QQ, implementation='pari')                  # needs sage.libs.pari
            sage: f = x.add_bigoh(7)                                                    # needs sage.libs.pari
            sage: f(x)                                                                  # needs sage.libs.pari
            x + O(x^7)
    """
    def __copy__(self) -> Any:
        """LaurentSeries.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1414)"""
    def __delitem__(self, other) -> None:
        """Delete self[key]."""
    def __getitem__(self, i) -> Any:
        """LaurentSeries.__getitem__(self, i)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 509)

        EXAMPLES::

            sage: R.<t> = LaurentSeriesRing(QQ)
            sage: f = -5/t^(10) + t + t^2 - 10/3*t^3; f
            -5*t^-10 + t + t^2 - 10/3*t^3
            sage: f[-10]
            -5
            sage: f[1]
            1
            sage: f[3]
            -10/3
            sage: f[-9]
            0
            sage: f = -5/t^(10) + 1/3 + t + t^2 - 10/3*t^3 + O(t^5); f
            -5*t^-10 + 1/3 + t + t^2 - 10/3*t^3 + O(t^5)

        Slicing can be used to truncate, keeping the same precision::

            sage: f[:2]
            -5*t^-10 + 1/3 + t + O(t^5)

        Any other kind of slicing is an error, see :issue:`18940`::

            sage: f[-10:2:2]
            Traceback (most recent call last):
            ...
            IndexError: polynomial slicing with a step is not defined

            sage: f[0:]
            Traceback (most recent call last):
            ...
            IndexError: polynomial slicing with a start is not defined"""
    def __hash__(self) -> Any:
        """LaurentSeries.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 506)"""
    def __iter__(self) -> Any:
        """LaurentSeries.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 557)

        Iterate through the coefficients from the first nonzero one to the
        last nonzero one.

        EXAMPLES::

            sage: R.<t> = LaurentSeriesRing(QQ)
            sage: f = -5/t^(2) + t + t^2 - 10/3*t^3; f
            -5*t^-2 + t + t^2 - 10/3*t^3
            sage: for a in f: print(a)
            -5
            0
            0
            1
            1
            -10/3"""
    def __lshift__(self, LaurentSeriesself, k) -> Any:
        """LaurentSeries.__lshift__(LaurentSeries self, k)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1023)"""
    def __neg__(self) -> Any:
        """LaurentSeries.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 908)

        EXAMPLES::

            sage: R.<t> = LaurentSeriesRing(QQ)
            sage: -(1+t^5)
            -1 - t^5
            sage: -(1/(1+t+O(t^5)))
            -1 + t - t^2 + t^3 - t^4 + O(t^5)"""
    @overload
    def __pari__(self) -> Any:
        """LaurentSeries.__pari__(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1893)

        Convert ``self`` to a PARI object.

        TESTS::

            sage: L.<x> = LaurentSeriesRing(QQ)
            sage: f = x + 1/x + O(x^2); f
            x^-1 + x + O(x^2)
            sage: f.__pari__()                                                          # needs sage.libs.pari
            x^-1 + x + O(x^2)

        Check that :issue:`32437` is fixed::

            sage: # needs sage.rings.finite_rings
            sage: F.<u> = GF(257^2)
            sage: R.<t> = LaurentSeriesRing(F)
            sage: g = t + O(t^99)
            sage: f = u*t + O(t^99)
            sage: g(f)  # indirect doctest                                              # needs sage.libs.pari
            u*t + O(t^99)"""
    @overload
    def __pari__(self) -> Any:
        """LaurentSeries.__pari__(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1893)

        Convert ``self`` to a PARI object.

        TESTS::

            sage: L.<x> = LaurentSeriesRing(QQ)
            sage: f = x + 1/x + O(x^2); f
            x^-1 + x + O(x^2)
            sage: f.__pari__()                                                          # needs sage.libs.pari
            x^-1 + x + O(x^2)

        Check that :issue:`32437` is fixed::

            sage: # needs sage.rings.finite_rings
            sage: F.<u> = GF(257^2)
            sage: R.<t> = LaurentSeriesRing(F)
            sage: g = t + O(t^99)
            sage: f = u*t + O(t^99)
            sage: g(f)  # indirect doctest                                              # needs sage.libs.pari
            u*t + O(t^99)"""
    def __pow__(self, _self, r, dummy) -> Any:
        """LaurentSeries.__pow__(_self, r, dummy)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 941)

        EXAMPLES::

            sage: x = Frac(QQ[['x']]).0
            sage: f = x + x^2 + 3*x^4 + O(x^7)
            sage: g = 1/x^10 - x + x^2 - x^4 + O(x^8)
            sage: f^7
            x^7 + 7*x^8 + 21*x^9 + 56*x^10 + 161*x^11 + 336*x^12 + O(x^13)
            sage: g^7
            x^-70 - 7*x^-59 + 7*x^-58 - 7*x^-56 + O(x^-52)
            sage: g^(1/2)
            x^-5 - 1/2*x^6 + 1/2*x^7 - 1/2*x^9 + O(x^13)
            sage: g^(1/5)
            x^-2 - 1/5*x^9 + 1/5*x^10 - 1/5*x^12 + O(x^16)
            sage: g^(2/5)
            x^-4 - 2/5*x^7 + 2/5*x^8 - 2/5*x^10 + O(x^14)
            sage: h = x^2 + 2*x^4 + x^6
            sage: h^(1/2)
            x + x^3"""
    def __reduce__(self) -> Any:
        """LaurentSeries.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 177)"""
    def __rlshift__(self, other):
        """Return value<<self."""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
    def __rrshift__(self, other):
        """Return value>>self."""
    def __rshift__(self, LaurentSeriesself, k) -> Any:
        """LaurentSeries.__rshift__(LaurentSeries self, k)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 1026)"""
    def __setitem__(self, n, value) -> Any:
        """LaurentSeries.__setitem__(self, n, value)

        File: /build/sagemath/src/sage/src/sage/rings/laurent_series_ring_element.pyx (starting at line 692)

        EXAMPLES::

            sage: R.<t> = LaurentSeriesRing(QQ)
            sage: f = t^2 + t^3 + O(t^10)
            sage: f[2] = 5
            Traceback (most recent call last):
            ...
            IndexError: Laurent series are immutable"""
