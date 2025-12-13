import _cython_3_2_1
import sage as sage
import sage.arith.all as arith
import sage.structure.element
from sage.categories.fields import Fields as Fields
from sage.misc.derivative import multi_derivative as multi_derivative
from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as IntegerModRing
from sage.rings.infinity import infinity as infinity
from sage.rings.integer import Integer as Integer
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import InfinityElement as InfinityElement, have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

is_PowerSeries: _cython_3_2_1.cython_function_or_method
make_element_from_parent_v0: _cython_3_2_1.cython_function_or_method
make_powerseries_poly_v0: _cython_3_2_1.cython_function_or_method

class PowerSeries(sage.structure.element.AlgebraElement):
    """PowerSeries(parent, prec, is_gen=False)

    File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 148)

    A power series. Base class of univariate and
    multivariate power series. The following methods
    are available with both types of objects."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, prec, is_gen=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 154)

                Initialize a power series. Not for public use.
                It gets called by the ``PowerSeries_poly`` and
                ``MPowerSeries`` constructors.

                EXAMPLES::

                    sage: PowerSeriesRing(CC, 'q')                                              # needs sage.rings.real_mpfr
                    Power Series Ring in q over Complex Field with 53 bits of precision
                    sage: T = PowerSeriesRing(GF(3), 5, 't'); T
                    Multivariate Power Series Ring in t0, t1, t2, t3, t4
                     over Finite Field of size 3
        """
    def O(self, prec) -> Any:
        """PowerSeries.O(self, prec)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2376)

        Return this series plus `O(x^\\text{prec})`. Does not change
        ``self``.

        EXAMPLES::

            sage: R.<x> = PowerSeriesRing(ZZ)
            sage: p = 1 + x^2 + x^10; p
            1 + x^2 + x^10
            sage: p.O(15)
            1 + x^2 + x^10 + O(x^15)
            sage: p.O(5)
            1 + x^2 + O(x^5)
            sage: p.O(-5)
            Traceback (most recent call last):
            ...
            ValueError: prec (= -5) must be nonnegative"""
    def V(self, n) -> Any:
        """PowerSeries.V(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2671)

        If `f = \\sum a_m x^m`, then this function returns
        `\\sum a_m x^{nm}`.

        EXAMPLES::

            sage: R.<x> = PowerSeriesRing(ZZ)
            sage: p = 1 + x^2 + x^10; p
            1 + x^2 + x^10
            sage: p.V(3)
            1 + x^6 + x^30
            sage: (p + O(x^20)).V(3)
            1 + x^6 + x^30 + O(x^60)"""
    def add_bigoh(self, prec) -> Any:
        """PowerSeries.add_bigoh(self, prec)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 821)

        Return the power series of precision at most ``prec`` got by adding
        `O(q^\\text{prec})` to `f`, where `q` is the variable.

        EXAMPLES::

            sage: R.<A> = RDF[[]]
            sage: f = (1+A+O(A^5))^5; f
            1.0 + 5.0*A + 10.0*A^2 + 10.0*A^3 + 5.0*A^4 + O(A^5)
            sage: f.add_bigoh(3)
            1.0 + 5.0*A + 10.0*A^2 + O(A^3)
            sage: f.add_bigoh(5)
            1.0 + 5.0*A + 10.0*A^2 + 10.0*A^3 + 5.0*A^4 + O(A^5)"""
    def base_extend(self, R) -> Any:
        """PowerSeries.base_extend(self, R)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 264)

        Return a copy of this power series but with coefficients in R.

        The following coercion uses ``base_extend`` implicitly::

            sage: R.<t> = ZZ[['t']]
            sage: (t - t^2) * Mod(1, 3)
            t + 2*t^2"""
    @overload
    def base_ring(self) -> Any:
        """PowerSeries.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 526)

        Return the base ring that this power series is defined over.

        EXAMPLES::

            sage: R.<t> = GF(49,'alpha')[[]]                                            # needs sage.rings.finite_rings
            sage: (t^2 + O(t^3)).base_ring()                                            # needs sage.rings.finite_rings
            Finite Field in alpha of size 7^2"""
    @overload
    def base_ring(self) -> Any:
        """PowerSeries.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 526)

        Return the base ring that this power series is defined over.

        EXAMPLES::

            sage: R.<t> = GF(49,'alpha')[[]]                                            # needs sage.rings.finite_rings
            sage: (t^2 + O(t^3)).base_ring()                                            # needs sage.rings.finite_rings
            Finite Field in alpha of size 7^2"""
    @overload
    def change_ring(self, R) -> Any:
        """PowerSeries.change_ring(self, R)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 277)

        Change if possible the coefficients of ``self`` to lie in R.

        EXAMPLES::

            sage: R.<T> = QQ[[]]; R
            Power Series Ring in T over Rational Field
            sage: f = 1 - 1/2*T + 1/3*T^2 + O(T^3)
            sage: f.base_extend(GF(5))
            Traceback (most recent call last):
            ...
            TypeError: no base extension defined
            sage: f.change_ring(GF(5))
            1 + 2*T + 2*T^2 + O(T^3)
            sage: f.change_ring(GF(3))
            Traceback (most recent call last):
            ...
            ZeroDivisionError: inverse of Mod(0, 3) does not exist

        We can only change the ring if there is a ``__call__`` coercion
        defined. The following succeeds because ``ZZ(K(4))`` is defined.

        ::

            sage: K.<a> = NumberField(cyclotomic_polynomial(3), 'a')                    # needs sage.rings.number_field
            sage: R.<t> = K[['t']]                                                      # needs sage.rings.number_field
            sage: (4*t).change_ring(ZZ)                                                 # needs sage.rings.number_field
            4*t

        This does not succeed because ``ZZ(K(a+1))`` is not defined.

        ::

            sage: K.<a> = NumberField(cyclotomic_polynomial(3), 'a')                    # needs sage.rings.number_field
            sage: R.<t> = K[['t']]                                                      # needs sage.rings.number_field
            sage: ((a+1)*t).change_ring(ZZ)                                             # needs sage.rings.number_field
            Traceback (most recent call last):
            ...
            TypeError: Unable to coerce a + 1 to an integer"""
    @overload
    def change_ring(self, ZZ) -> Any:
        """PowerSeries.change_ring(self, R)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 277)

        Change if possible the coefficients of ``self`` to lie in R.

        EXAMPLES::

            sage: R.<T> = QQ[[]]; R
            Power Series Ring in T over Rational Field
            sage: f = 1 - 1/2*T + 1/3*T^2 + O(T^3)
            sage: f.base_extend(GF(5))
            Traceback (most recent call last):
            ...
            TypeError: no base extension defined
            sage: f.change_ring(GF(5))
            1 + 2*T + 2*T^2 + O(T^3)
            sage: f.change_ring(GF(3))
            Traceback (most recent call last):
            ...
            ZeroDivisionError: inverse of Mod(0, 3) does not exist

        We can only change the ring if there is a ``__call__`` coercion
        defined. The following succeeds because ``ZZ(K(4))`` is defined.

        ::

            sage: K.<a> = NumberField(cyclotomic_polynomial(3), 'a')                    # needs sage.rings.number_field
            sage: R.<t> = K[['t']]                                                      # needs sage.rings.number_field
            sage: (4*t).change_ring(ZZ)                                                 # needs sage.rings.number_field
            4*t

        This does not succeed because ``ZZ(K(a+1))`` is not defined.

        ::

            sage: K.<a> = NumberField(cyclotomic_polynomial(3), 'a')                    # needs sage.rings.number_field
            sage: R.<t> = K[['t']]                                                      # needs sage.rings.number_field
            sage: ((a+1)*t).change_ring(ZZ)                                             # needs sage.rings.number_field
            Traceback (most recent call last):
            ...
            TypeError: Unable to coerce a + 1 to an integer"""
    @overload
    def change_ring(self, ZZ) -> Any:
        """PowerSeries.change_ring(self, R)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 277)

        Change if possible the coefficients of ``self`` to lie in R.

        EXAMPLES::

            sage: R.<T> = QQ[[]]; R
            Power Series Ring in T over Rational Field
            sage: f = 1 - 1/2*T + 1/3*T^2 + O(T^3)
            sage: f.base_extend(GF(5))
            Traceback (most recent call last):
            ...
            TypeError: no base extension defined
            sage: f.change_ring(GF(5))
            1 + 2*T + 2*T^2 + O(T^3)
            sage: f.change_ring(GF(3))
            Traceback (most recent call last):
            ...
            ZeroDivisionError: inverse of Mod(0, 3) does not exist

        We can only change the ring if there is a ``__call__`` coercion
        defined. The following succeeds because ``ZZ(K(4))`` is defined.

        ::

            sage: K.<a> = NumberField(cyclotomic_polynomial(3), 'a')                    # needs sage.rings.number_field
            sage: R.<t> = K[['t']]                                                      # needs sage.rings.number_field
            sage: (4*t).change_ring(ZZ)                                                 # needs sage.rings.number_field
            4*t

        This does not succeed because ``ZZ(K(a+1))`` is not defined.

        ::

            sage: K.<a> = NumberField(cyclotomic_polynomial(3), 'a')                    # needs sage.rings.number_field
            sage: R.<t> = K[['t']]                                                      # needs sage.rings.number_field
            sage: ((a+1)*t).change_ring(ZZ)                                             # needs sage.rings.number_field
            Traceback (most recent call last):
            ...
            TypeError: Unable to coerce a + 1 to an integer"""
    @overload
    def coefficients(self) -> Any:
        """PowerSeries.coefficients(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 411)

        Return the nonzero coefficients of ``self``.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(QQ)
            sage: f = t + t^2 - 10/3*t^3
            sage: f.coefficients()
            [1, 1, -10/3]"""
    @overload
    def coefficients(self) -> Any:
        """PowerSeries.coefficients(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 411)

        Return the nonzero coefficients of ``self``.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(QQ)
            sage: f = t + t^2 - 10/3*t^3
            sage: f.coefficients()
            [1, 1, -10/3]"""
    @overload
    def common_prec(self, f) -> Any:
        """PowerSeries.common_prec(self, f)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 883)

        Return minimum precision of `f` and ``self``.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(QQ)

        ::

            sage: f = t + t^2 + O(t^3)
            sage: g = t + t^3 + t^4 + O(t^4)
            sage: f.common_prec(g)
            3
            sage: g.common_prec(f)
            3

        ::

            sage: f = t + t^2 + O(t^3)
            sage: g = t^2
            sage: f.common_prec(g)
            3
            sage: g.common_prec(f)
            3

        ::

            sage: f = t + t^2
            sage: f = t^2
            sage: f.common_prec(g)
            +Infinity"""
    @overload
    def common_prec(self, g) -> Any:
        """PowerSeries.common_prec(self, f)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 883)

        Return minimum precision of `f` and ``self``.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(QQ)

        ::

            sage: f = t + t^2 + O(t^3)
            sage: g = t + t^3 + t^4 + O(t^4)
            sage: f.common_prec(g)
            3
            sage: g.common_prec(f)
            3

        ::

            sage: f = t + t^2 + O(t^3)
            sage: g = t^2
            sage: f.common_prec(g)
            3
            sage: g.common_prec(f)
            3

        ::

            sage: f = t + t^2
            sage: f = t^2
            sage: f.common_prec(g)
            +Infinity"""
    @overload
    def common_prec(self, f) -> Any:
        """PowerSeries.common_prec(self, f)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 883)

        Return minimum precision of `f` and ``self``.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(QQ)

        ::

            sage: f = t + t^2 + O(t^3)
            sage: g = t + t^3 + t^4 + O(t^4)
            sage: f.common_prec(g)
            3
            sage: g.common_prec(f)
            3

        ::

            sage: f = t + t^2 + O(t^3)
            sage: g = t^2
            sage: f.common_prec(g)
            3
            sage: g.common_prec(f)
            3

        ::

            sage: f = t + t^2
            sage: f = t^2
            sage: f.common_prec(g)
            +Infinity"""
    @overload
    def common_prec(self, g) -> Any:
        """PowerSeries.common_prec(self, f)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 883)

        Return minimum precision of `f` and ``self``.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(QQ)

        ::

            sage: f = t + t^2 + O(t^3)
            sage: g = t + t^3 + t^4 + O(t^4)
            sage: f.common_prec(g)
            3
            sage: g.common_prec(f)
            3

        ::

            sage: f = t + t^2 + O(t^3)
            sage: g = t^2
            sage: f.common_prec(g)
            3
            sage: g.common_prec(f)
            3

        ::

            sage: f = t + t^2
            sage: f = t^2
            sage: f.common_prec(g)
            +Infinity"""
    @overload
    def common_prec(self, f) -> Any:
        """PowerSeries.common_prec(self, f)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 883)

        Return minimum precision of `f` and ``self``.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(QQ)

        ::

            sage: f = t + t^2 + O(t^3)
            sage: g = t + t^3 + t^4 + O(t^4)
            sage: f.common_prec(g)
            3
            sage: g.common_prec(f)
            3

        ::

            sage: f = t + t^2 + O(t^3)
            sage: g = t^2
            sage: f.common_prec(g)
            3
            sage: g.common_prec(f)
            3

        ::

            sage: f = t + t^2
            sage: f = t^2
            sage: f.common_prec(g)
            +Infinity"""
    @overload
    def common_prec(self, g) -> Any:
        """PowerSeries.common_prec(self, f)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 883)

        Return minimum precision of `f` and ``self``.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(QQ)

        ::

            sage: f = t + t^2 + O(t^3)
            sage: g = t + t^3 + t^4 + O(t^4)
            sage: f.common_prec(g)
            3
            sage: g.common_prec(f)
            3

        ::

            sage: f = t + t^2 + O(t^3)
            sage: g = t^2
            sage: f.common_prec(g)
            3
            sage: g.common_prec(f)
            3

        ::

            sage: f = t + t^2
            sage: f = t^2
            sage: f.common_prec(g)
            +Infinity"""
    @overload
    def cos(self, prec=...) -> Any:
        """PowerSeries.cos(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1912)

        Apply cos to the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT: a new power series

        EXAMPLES:

        For one variable::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: f = (t + t**2).O(4)
            sage: cos(f)
            1 - 1/2*t^2 - t^3 + O(t^4)

        For several variables::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(3)
            sage: cos(f)
            1 - 1/2*a^2 - a*b - 1/2*b^2 + O(a, b)^3
            sage: f.cos()
            1 - 1/2*a^2 - a*b - 1/2*b^2 + O(a, b)^3
            sage: f.cos(prec=2)
            1 + O(a, b)^2

        If the power series has a nonzero constant coefficient `c`,
        one raises an error::

            sage: g = 2+f
            sage: cos(g)
            Traceback (most recent call last):
            ...
            ValueError: can only apply cos to formal power series with zero constant term

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: cos(a)
            1 - 1/2*a^2 + 1/24*a^4 - 1/720*a^6 + 1/40320*a^8 - 1/3628800*a^10 + O(a, b)^12
            sage: a.cos(prec=5)
            1 - 1/2*a^2 + 1/24*a^4 + O(a, b)^5
            sage: cos(a + T.O(5))
            1 - 1/2*a^2 + 1/24*a^4 + O(a, b)^5

        TESTS::

            sage: cos(a^2 + T.O(5))
            1 - 1/2*a^4 + O(a, b)^5"""
    @overload
    def cos(self, f) -> Any:
        """PowerSeries.cos(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1912)

        Apply cos to the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT: a new power series

        EXAMPLES:

        For one variable::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: f = (t + t**2).O(4)
            sage: cos(f)
            1 - 1/2*t^2 - t^3 + O(t^4)

        For several variables::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(3)
            sage: cos(f)
            1 - 1/2*a^2 - a*b - 1/2*b^2 + O(a, b)^3
            sage: f.cos()
            1 - 1/2*a^2 - a*b - 1/2*b^2 + O(a, b)^3
            sage: f.cos(prec=2)
            1 + O(a, b)^2

        If the power series has a nonzero constant coefficient `c`,
        one raises an error::

            sage: g = 2+f
            sage: cos(g)
            Traceback (most recent call last):
            ...
            ValueError: can only apply cos to formal power series with zero constant term

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: cos(a)
            1 - 1/2*a^2 + 1/24*a^4 - 1/720*a^6 + 1/40320*a^8 - 1/3628800*a^10 + O(a, b)^12
            sage: a.cos(prec=5)
            1 - 1/2*a^2 + 1/24*a^4 + O(a, b)^5
            sage: cos(a + T.O(5))
            1 - 1/2*a^2 + 1/24*a^4 + O(a, b)^5

        TESTS::

            sage: cos(a^2 + T.O(5))
            1 - 1/2*a^4 + O(a, b)^5"""
    @overload
    def cos(self, f) -> Any:
        """PowerSeries.cos(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1912)

        Apply cos to the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT: a new power series

        EXAMPLES:

        For one variable::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: f = (t + t**2).O(4)
            sage: cos(f)
            1 - 1/2*t^2 - t^3 + O(t^4)

        For several variables::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(3)
            sage: cos(f)
            1 - 1/2*a^2 - a*b - 1/2*b^2 + O(a, b)^3
            sage: f.cos()
            1 - 1/2*a^2 - a*b - 1/2*b^2 + O(a, b)^3
            sage: f.cos(prec=2)
            1 + O(a, b)^2

        If the power series has a nonzero constant coefficient `c`,
        one raises an error::

            sage: g = 2+f
            sage: cos(g)
            Traceback (most recent call last):
            ...
            ValueError: can only apply cos to formal power series with zero constant term

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: cos(a)
            1 - 1/2*a^2 + 1/24*a^4 - 1/720*a^6 + 1/40320*a^8 - 1/3628800*a^10 + O(a, b)^12
            sage: a.cos(prec=5)
            1 - 1/2*a^2 + 1/24*a^4 + O(a, b)^5
            sage: cos(a + T.O(5))
            1 - 1/2*a^2 + 1/24*a^4 + O(a, b)^5

        TESTS::

            sage: cos(a^2 + T.O(5))
            1 - 1/2*a^4 + O(a, b)^5"""
    @overload
    def cos(self) -> Any:
        """PowerSeries.cos(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1912)

        Apply cos to the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT: a new power series

        EXAMPLES:

        For one variable::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: f = (t + t**2).O(4)
            sage: cos(f)
            1 - 1/2*t^2 - t^3 + O(t^4)

        For several variables::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(3)
            sage: cos(f)
            1 - 1/2*a^2 - a*b - 1/2*b^2 + O(a, b)^3
            sage: f.cos()
            1 - 1/2*a^2 - a*b - 1/2*b^2 + O(a, b)^3
            sage: f.cos(prec=2)
            1 + O(a, b)^2

        If the power series has a nonzero constant coefficient `c`,
        one raises an error::

            sage: g = 2+f
            sage: cos(g)
            Traceback (most recent call last):
            ...
            ValueError: can only apply cos to formal power series with zero constant term

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: cos(a)
            1 - 1/2*a^2 + 1/24*a^4 - 1/720*a^6 + 1/40320*a^8 - 1/3628800*a^10 + O(a, b)^12
            sage: a.cos(prec=5)
            1 - 1/2*a^2 + 1/24*a^4 + O(a, b)^5
            sage: cos(a + T.O(5))
            1 - 1/2*a^2 + 1/24*a^4 + O(a, b)^5

        TESTS::

            sage: cos(a^2 + T.O(5))
            1 - 1/2*a^4 + O(a, b)^5"""
    @overload
    def cos(self, prec=...) -> Any:
        """PowerSeries.cos(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1912)

        Apply cos to the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT: a new power series

        EXAMPLES:

        For one variable::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: f = (t + t**2).O(4)
            sage: cos(f)
            1 - 1/2*t^2 - t^3 + O(t^4)

        For several variables::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(3)
            sage: cos(f)
            1 - 1/2*a^2 - a*b - 1/2*b^2 + O(a, b)^3
            sage: f.cos()
            1 - 1/2*a^2 - a*b - 1/2*b^2 + O(a, b)^3
            sage: f.cos(prec=2)
            1 + O(a, b)^2

        If the power series has a nonzero constant coefficient `c`,
        one raises an error::

            sage: g = 2+f
            sage: cos(g)
            Traceback (most recent call last):
            ...
            ValueError: can only apply cos to formal power series with zero constant term

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: cos(a)
            1 - 1/2*a^2 + 1/24*a^4 - 1/720*a^6 + 1/40320*a^8 - 1/3628800*a^10 + O(a, b)^12
            sage: a.cos(prec=5)
            1 - 1/2*a^2 + 1/24*a^4 + O(a, b)^5
            sage: cos(a + T.O(5))
            1 - 1/2*a^2 + 1/24*a^4 + O(a, b)^5

        TESTS::

            sage: cos(a^2 + T.O(5))
            1 - 1/2*a^4 + O(a, b)^5"""
    @overload
    def cos(self, g) -> Any:
        """PowerSeries.cos(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1912)

        Apply cos to the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT: a new power series

        EXAMPLES:

        For one variable::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: f = (t + t**2).O(4)
            sage: cos(f)
            1 - 1/2*t^2 - t^3 + O(t^4)

        For several variables::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(3)
            sage: cos(f)
            1 - 1/2*a^2 - a*b - 1/2*b^2 + O(a, b)^3
            sage: f.cos()
            1 - 1/2*a^2 - a*b - 1/2*b^2 + O(a, b)^3
            sage: f.cos(prec=2)
            1 + O(a, b)^2

        If the power series has a nonzero constant coefficient `c`,
        one raises an error::

            sage: g = 2+f
            sage: cos(g)
            Traceback (most recent call last):
            ...
            ValueError: can only apply cos to formal power series with zero constant term

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: cos(a)
            1 - 1/2*a^2 + 1/24*a^4 - 1/720*a^6 + 1/40320*a^8 - 1/3628800*a^10 + O(a, b)^12
            sage: a.cos(prec=5)
            1 - 1/2*a^2 + 1/24*a^4 + O(a, b)^5
            sage: cos(a + T.O(5))
            1 - 1/2*a^2 + 1/24*a^4 + O(a, b)^5

        TESTS::

            sage: cos(a^2 + T.O(5))
            1 - 1/2*a^4 + O(a, b)^5"""
    @overload
    def cos(self, a) -> Any:
        """PowerSeries.cos(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1912)

        Apply cos to the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT: a new power series

        EXAMPLES:

        For one variable::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: f = (t + t**2).O(4)
            sage: cos(f)
            1 - 1/2*t^2 - t^3 + O(t^4)

        For several variables::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(3)
            sage: cos(f)
            1 - 1/2*a^2 - a*b - 1/2*b^2 + O(a, b)^3
            sage: f.cos()
            1 - 1/2*a^2 - a*b - 1/2*b^2 + O(a, b)^3
            sage: f.cos(prec=2)
            1 + O(a, b)^2

        If the power series has a nonzero constant coefficient `c`,
        one raises an error::

            sage: g = 2+f
            sage: cos(g)
            Traceback (most recent call last):
            ...
            ValueError: can only apply cos to formal power series with zero constant term

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: cos(a)
            1 - 1/2*a^2 + 1/24*a^4 - 1/720*a^6 + 1/40320*a^8 - 1/3628800*a^10 + O(a, b)^12
            sage: a.cos(prec=5)
            1 - 1/2*a^2 + 1/24*a^4 + O(a, b)^5
            sage: cos(a + T.O(5))
            1 - 1/2*a^2 + 1/24*a^4 + O(a, b)^5

        TESTS::

            sage: cos(a^2 + T.O(5))
            1 - 1/2*a^4 + O(a, b)^5"""
    @overload
    def cos(self, prec=...) -> Any:
        """PowerSeries.cos(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1912)

        Apply cos to the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT: a new power series

        EXAMPLES:

        For one variable::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: f = (t + t**2).O(4)
            sage: cos(f)
            1 - 1/2*t^2 - t^3 + O(t^4)

        For several variables::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(3)
            sage: cos(f)
            1 - 1/2*a^2 - a*b - 1/2*b^2 + O(a, b)^3
            sage: f.cos()
            1 - 1/2*a^2 - a*b - 1/2*b^2 + O(a, b)^3
            sage: f.cos(prec=2)
            1 + O(a, b)^2

        If the power series has a nonzero constant coefficient `c`,
        one raises an error::

            sage: g = 2+f
            sage: cos(g)
            Traceback (most recent call last):
            ...
            ValueError: can only apply cos to formal power series with zero constant term

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: cos(a)
            1 - 1/2*a^2 + 1/24*a^4 - 1/720*a^6 + 1/40320*a^8 - 1/3628800*a^10 + O(a, b)^12
            sage: a.cos(prec=5)
            1 - 1/2*a^2 + 1/24*a^4 + O(a, b)^5
            sage: cos(a + T.O(5))
            1 - 1/2*a^2 + 1/24*a^4 + O(a, b)^5

        TESTS::

            sage: cos(a^2 + T.O(5))
            1 - 1/2*a^4 + O(a, b)^5"""
    @overload
    def cosh(self, prec=...) -> Any:
        """PowerSeries.cosh(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2227)

        Apply cosh to the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT: a new power series

        EXAMPLES:

        For one variable::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: f = (t + t**2).O(4)
            sage: cosh(f)
            1 + 1/2*t^2 + t^3 + O(t^4)

        For several variables::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(3)
            sage: cosh(f)
            1 + 1/2*a^2 + a*b + 1/2*b^2 + O(a, b)^3
            sage: f.cosh()
            1 + 1/2*a^2 + a*b + 1/2*b^2 + O(a, b)^3
            sage: f.cosh(prec=2)
            1 + O(a, b)^2

        If the power series has a nonzero constant coefficient `c`,
        one raises an error::

            sage: g = 2 + f
            sage: cosh(g)
            Traceback (most recent call last):
            ...
            ValueError: can only apply cosh to formal power series with zero
            constant term

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: cosh(a)
            1 + 1/2*a^2 + 1/24*a^4 + 1/720*a^6 + 1/40320*a^8 + 1/3628800*a^10 +
             O(a, b)^12
            sage: a.cosh(prec=5)
            1 + 1/2*a^2 + 1/24*a^4 + O(a, b)^5
            sage: cosh(a + T.O(5))
            1 + 1/2*a^2 + 1/24*a^4 + O(a, b)^5

        TESTS::

            sage: cosh(a^2 + T.O(5))
            1 + 1/2*a^4 + O(a, b)^5"""
    @overload
    def cosh(self, f) -> Any:
        """PowerSeries.cosh(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2227)

        Apply cosh to the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT: a new power series

        EXAMPLES:

        For one variable::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: f = (t + t**2).O(4)
            sage: cosh(f)
            1 + 1/2*t^2 + t^3 + O(t^4)

        For several variables::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(3)
            sage: cosh(f)
            1 + 1/2*a^2 + a*b + 1/2*b^2 + O(a, b)^3
            sage: f.cosh()
            1 + 1/2*a^2 + a*b + 1/2*b^2 + O(a, b)^3
            sage: f.cosh(prec=2)
            1 + O(a, b)^2

        If the power series has a nonzero constant coefficient `c`,
        one raises an error::

            sage: g = 2 + f
            sage: cosh(g)
            Traceback (most recent call last):
            ...
            ValueError: can only apply cosh to formal power series with zero
            constant term

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: cosh(a)
            1 + 1/2*a^2 + 1/24*a^4 + 1/720*a^6 + 1/40320*a^8 + 1/3628800*a^10 +
             O(a, b)^12
            sage: a.cosh(prec=5)
            1 + 1/2*a^2 + 1/24*a^4 + O(a, b)^5
            sage: cosh(a + T.O(5))
            1 + 1/2*a^2 + 1/24*a^4 + O(a, b)^5

        TESTS::

            sage: cosh(a^2 + T.O(5))
            1 + 1/2*a^4 + O(a, b)^5"""
    @overload
    def cosh(self, f) -> Any:
        """PowerSeries.cosh(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2227)

        Apply cosh to the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT: a new power series

        EXAMPLES:

        For one variable::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: f = (t + t**2).O(4)
            sage: cosh(f)
            1 + 1/2*t^2 + t^3 + O(t^4)

        For several variables::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(3)
            sage: cosh(f)
            1 + 1/2*a^2 + a*b + 1/2*b^2 + O(a, b)^3
            sage: f.cosh()
            1 + 1/2*a^2 + a*b + 1/2*b^2 + O(a, b)^3
            sage: f.cosh(prec=2)
            1 + O(a, b)^2

        If the power series has a nonzero constant coefficient `c`,
        one raises an error::

            sage: g = 2 + f
            sage: cosh(g)
            Traceback (most recent call last):
            ...
            ValueError: can only apply cosh to formal power series with zero
            constant term

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: cosh(a)
            1 + 1/2*a^2 + 1/24*a^4 + 1/720*a^6 + 1/40320*a^8 + 1/3628800*a^10 +
             O(a, b)^12
            sage: a.cosh(prec=5)
            1 + 1/2*a^2 + 1/24*a^4 + O(a, b)^5
            sage: cosh(a + T.O(5))
            1 + 1/2*a^2 + 1/24*a^4 + O(a, b)^5

        TESTS::

            sage: cosh(a^2 + T.O(5))
            1 + 1/2*a^4 + O(a, b)^5"""
    @overload
    def cosh(self) -> Any:
        """PowerSeries.cosh(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2227)

        Apply cosh to the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT: a new power series

        EXAMPLES:

        For one variable::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: f = (t + t**2).O(4)
            sage: cosh(f)
            1 + 1/2*t^2 + t^3 + O(t^4)

        For several variables::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(3)
            sage: cosh(f)
            1 + 1/2*a^2 + a*b + 1/2*b^2 + O(a, b)^3
            sage: f.cosh()
            1 + 1/2*a^2 + a*b + 1/2*b^2 + O(a, b)^3
            sage: f.cosh(prec=2)
            1 + O(a, b)^2

        If the power series has a nonzero constant coefficient `c`,
        one raises an error::

            sage: g = 2 + f
            sage: cosh(g)
            Traceback (most recent call last):
            ...
            ValueError: can only apply cosh to formal power series with zero
            constant term

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: cosh(a)
            1 + 1/2*a^2 + 1/24*a^4 + 1/720*a^6 + 1/40320*a^8 + 1/3628800*a^10 +
             O(a, b)^12
            sage: a.cosh(prec=5)
            1 + 1/2*a^2 + 1/24*a^4 + O(a, b)^5
            sage: cosh(a + T.O(5))
            1 + 1/2*a^2 + 1/24*a^4 + O(a, b)^5

        TESTS::

            sage: cosh(a^2 + T.O(5))
            1 + 1/2*a^4 + O(a, b)^5"""
    @overload
    def cosh(self, prec=...) -> Any:
        """PowerSeries.cosh(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2227)

        Apply cosh to the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT: a new power series

        EXAMPLES:

        For one variable::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: f = (t + t**2).O(4)
            sage: cosh(f)
            1 + 1/2*t^2 + t^3 + O(t^4)

        For several variables::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(3)
            sage: cosh(f)
            1 + 1/2*a^2 + a*b + 1/2*b^2 + O(a, b)^3
            sage: f.cosh()
            1 + 1/2*a^2 + a*b + 1/2*b^2 + O(a, b)^3
            sage: f.cosh(prec=2)
            1 + O(a, b)^2

        If the power series has a nonzero constant coefficient `c`,
        one raises an error::

            sage: g = 2 + f
            sage: cosh(g)
            Traceback (most recent call last):
            ...
            ValueError: can only apply cosh to formal power series with zero
            constant term

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: cosh(a)
            1 + 1/2*a^2 + 1/24*a^4 + 1/720*a^6 + 1/40320*a^8 + 1/3628800*a^10 +
             O(a, b)^12
            sage: a.cosh(prec=5)
            1 + 1/2*a^2 + 1/24*a^4 + O(a, b)^5
            sage: cosh(a + T.O(5))
            1 + 1/2*a^2 + 1/24*a^4 + O(a, b)^5

        TESTS::

            sage: cosh(a^2 + T.O(5))
            1 + 1/2*a^4 + O(a, b)^5"""
    @overload
    def cosh(self, g) -> Any:
        """PowerSeries.cosh(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2227)

        Apply cosh to the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT: a new power series

        EXAMPLES:

        For one variable::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: f = (t + t**2).O(4)
            sage: cosh(f)
            1 + 1/2*t^2 + t^3 + O(t^4)

        For several variables::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(3)
            sage: cosh(f)
            1 + 1/2*a^2 + a*b + 1/2*b^2 + O(a, b)^3
            sage: f.cosh()
            1 + 1/2*a^2 + a*b + 1/2*b^2 + O(a, b)^3
            sage: f.cosh(prec=2)
            1 + O(a, b)^2

        If the power series has a nonzero constant coefficient `c`,
        one raises an error::

            sage: g = 2 + f
            sage: cosh(g)
            Traceback (most recent call last):
            ...
            ValueError: can only apply cosh to formal power series with zero
            constant term

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: cosh(a)
            1 + 1/2*a^2 + 1/24*a^4 + 1/720*a^6 + 1/40320*a^8 + 1/3628800*a^10 +
             O(a, b)^12
            sage: a.cosh(prec=5)
            1 + 1/2*a^2 + 1/24*a^4 + O(a, b)^5
            sage: cosh(a + T.O(5))
            1 + 1/2*a^2 + 1/24*a^4 + O(a, b)^5

        TESTS::

            sage: cosh(a^2 + T.O(5))
            1 + 1/2*a^4 + O(a, b)^5"""
    @overload
    def cosh(self, a) -> Any:
        """PowerSeries.cosh(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2227)

        Apply cosh to the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT: a new power series

        EXAMPLES:

        For one variable::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: f = (t + t**2).O(4)
            sage: cosh(f)
            1 + 1/2*t^2 + t^3 + O(t^4)

        For several variables::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(3)
            sage: cosh(f)
            1 + 1/2*a^2 + a*b + 1/2*b^2 + O(a, b)^3
            sage: f.cosh()
            1 + 1/2*a^2 + a*b + 1/2*b^2 + O(a, b)^3
            sage: f.cosh(prec=2)
            1 + O(a, b)^2

        If the power series has a nonzero constant coefficient `c`,
        one raises an error::

            sage: g = 2 + f
            sage: cosh(g)
            Traceback (most recent call last):
            ...
            ValueError: can only apply cosh to formal power series with zero
            constant term

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: cosh(a)
            1 + 1/2*a^2 + 1/24*a^4 + 1/720*a^6 + 1/40320*a^8 + 1/3628800*a^10 +
             O(a, b)^12
            sage: a.cosh(prec=5)
            1 + 1/2*a^2 + 1/24*a^4 + O(a, b)^5
            sage: cosh(a + T.O(5))
            1 + 1/2*a^2 + 1/24*a^4 + O(a, b)^5

        TESTS::

            sage: cosh(a^2 + T.O(5))
            1 + 1/2*a^4 + O(a, b)^5"""
    @overload
    def cosh(self, prec=...) -> Any:
        """PowerSeries.cosh(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2227)

        Apply cosh to the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT: a new power series

        EXAMPLES:

        For one variable::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: f = (t + t**2).O(4)
            sage: cosh(f)
            1 + 1/2*t^2 + t^3 + O(t^4)

        For several variables::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(3)
            sage: cosh(f)
            1 + 1/2*a^2 + a*b + 1/2*b^2 + O(a, b)^3
            sage: f.cosh()
            1 + 1/2*a^2 + a*b + 1/2*b^2 + O(a, b)^3
            sage: f.cosh(prec=2)
            1 + O(a, b)^2

        If the power series has a nonzero constant coefficient `c`,
        one raises an error::

            sage: g = 2 + f
            sage: cosh(g)
            Traceback (most recent call last):
            ...
            ValueError: can only apply cosh to formal power series with zero
            constant term

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: cosh(a)
            1 + 1/2*a^2 + 1/24*a^4 + 1/720*a^6 + 1/40320*a^8 + 1/3628800*a^10 +
             O(a, b)^12
            sage: a.cosh(prec=5)
            1 + 1/2*a^2 + 1/24*a^4 + O(a, b)^5
            sage: cosh(a + T.O(5))
            1 + 1/2*a^2 + 1/24*a^4 + O(a, b)^5

        TESTS::

            sage: cosh(a^2 + T.O(5))
            1 + 1/2*a^4 + O(a, b)^5"""
    @overload
    def degree(self) -> Any:
        """PowerSeries.degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2744)

        Return the degree of this power series, which is by definition the
        degree of the underlying polynomial.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(QQ, sparse=True)
            sage: f = t^100000 + O(t^10000000)
            sage: f.degree()
            100000"""
    @overload
    def degree(self) -> Any:
        """PowerSeries.degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2744)

        Return the degree of this power series, which is by definition the
        degree of the underlying polynomial.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(QQ, sparse=True)
            sage: f = t^100000 + O(t^10000000)
            sage: f.degree()
            100000"""
    @overload
    def derivative(self, *args) -> Any:
        """PowerSeries.derivative(self, *args)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2758)

        The formal derivative of this power series, with respect to
        variables supplied in args.

        Multiple variables and iteration counts may be supplied; see
        documentation for the global derivative() function for more
        details.

        .. SEEALSO::

           :meth:`_derivative`

        EXAMPLES::

            sage: R.<x> = PowerSeriesRing(QQ)
            sage: g = -x + x^2/2 - x^4 + O(x^6)
            sage: g.derivative()
            -1 + x - 4*x^3 + O(x^5)
            sage: g.derivative(x)
            -1 + x - 4*x^3 + O(x^5)
            sage: g.derivative(x, x)
            1 - 12*x^2 + O(x^4)
            sage: g.derivative(x, 2)
            1 - 12*x^2 + O(x^4)"""
    @overload
    def derivative(self) -> Any:
        """PowerSeries.derivative(self, *args)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2758)

        The formal derivative of this power series, with respect to
        variables supplied in args.

        Multiple variables and iteration counts may be supplied; see
        documentation for the global derivative() function for more
        details.

        .. SEEALSO::

           :meth:`_derivative`

        EXAMPLES::

            sage: R.<x> = PowerSeriesRing(QQ)
            sage: g = -x + x^2/2 - x^4 + O(x^6)
            sage: g.derivative()
            -1 + x - 4*x^3 + O(x^5)
            sage: g.derivative(x)
            -1 + x - 4*x^3 + O(x^5)
            sage: g.derivative(x, x)
            1 - 12*x^2 + O(x^4)
            sage: g.derivative(x, 2)
            1 - 12*x^2 + O(x^4)"""
    @overload
    def derivative(self) -> Any:
        """PowerSeries.derivative(self, *args)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2758)

        The formal derivative of this power series, with respect to
        variables supplied in args.

        Multiple variables and iteration counts may be supplied; see
        documentation for the global derivative() function for more
        details.

        .. SEEALSO::

           :meth:`_derivative`

        EXAMPLES::

            sage: R.<x> = PowerSeriesRing(QQ)
            sage: g = -x + x^2/2 - x^4 + O(x^6)
            sage: g.derivative()
            -1 + x - 4*x^3 + O(x^5)
            sage: g.derivative(x)
            -1 + x - 4*x^3 + O(x^5)
            sage: g.derivative(x, x)
            1 - 12*x^2 + O(x^4)
            sage: g.derivative(x, 2)
            1 - 12*x^2 + O(x^4)"""
    @overload
    def derivative(self, x) -> Any:
        """PowerSeries.derivative(self, *args)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2758)

        The formal derivative of this power series, with respect to
        variables supplied in args.

        Multiple variables and iteration counts may be supplied; see
        documentation for the global derivative() function for more
        details.

        .. SEEALSO::

           :meth:`_derivative`

        EXAMPLES::

            sage: R.<x> = PowerSeriesRing(QQ)
            sage: g = -x + x^2/2 - x^4 + O(x^6)
            sage: g.derivative()
            -1 + x - 4*x^3 + O(x^5)
            sage: g.derivative(x)
            -1 + x - 4*x^3 + O(x^5)
            sage: g.derivative(x, x)
            1 - 12*x^2 + O(x^4)
            sage: g.derivative(x, 2)
            1 - 12*x^2 + O(x^4)"""
    @overload
    def egf_to_ogf(self) -> Any:
        """PowerSeries.egf_to_ogf(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2817)

        Return the ordinary generating function power series,
        assuming ``self`` is an exponential generating function power series.

        This is a formal Laplace transform.

        This function is known as :pari:`serlaplace` in PARI/GP.

        .. SEEALSO:: :meth:`ogf_to_egf` for the inverse method.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(QQ)
            sage: f = t + t^2/factorial(2) + 2*t^3/factorial(3)
            sage: f.egf_to_ogf()
            t + t^2 + 2*t^3"""
    @overload
    def egf_to_ogf(self) -> Any:
        """PowerSeries.egf_to_ogf(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2817)

        Return the ordinary generating function power series,
        assuming ``self`` is an exponential generating function power series.

        This is a formal Laplace transform.

        This function is known as :pari:`serlaplace` in PARI/GP.

        .. SEEALSO:: :meth:`ogf_to_egf` for the inverse method.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(QQ)
            sage: f = t + t^2/factorial(2) + 2*t^3/factorial(3)
            sage: f.egf_to_ogf()
            t + t^2 + 2*t^3"""
    def exp(self, prec=...) -> Any:
        '''PowerSeries.exp(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2507)

        Return exp of this power series to the indicated precision.

        INPUT:

        - ``prec`` -- integer (default: ``self.parent().default_prec``)

        ALGORITHM: See :meth:`.solve_linear_de`.

        .. NOTE::

           - Screwy things can happen if the coefficient ring is not a
             field of characteristic zero. See :meth:`.solve_linear_de`.

        AUTHORS:

        - David Harvey (2006-09-08): rewrote to use simplest possible "lazy" algorithm.

        - David Harvey (2006-09-10): rewrote to use divide-and-conquer
          strategy.

        - David Harvey (2006-09-11): factored functionality out to
          solve_linear_de().

        - Sourav Sen Gupta, David Harvey (2008-11): handle constant
          term

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(QQ, default_prec=10)

        Check that `\\exp(t)` is, well, `\\exp(t)`::

            sage: (t + O(t^10)).exp()
            1 + t + 1/2*t^2 + 1/6*t^3 + 1/24*t^4 + 1/120*t^5 + 1/720*t^6
              + 1/5040*t^7 + 1/40320*t^8 + 1/362880*t^9 + O(t^10)

        Check that `\\exp(\\log(1+t))` is `1+t`::

            sage: (sum([-(-t)^n/n for n in range(1, 10)]) + O(t^10)).exp()
            1 + t + O(t^10)

        Check that `\\exp(2t + t^2 - t^5)` is whatever it is::

            sage: (2*t + t^2 - t^5 + O(t^10)).exp()
            1 + 2*t + 3*t^2 + 10/3*t^3 + 19/6*t^4 + 8/5*t^5 - 7/90*t^6
              - 538/315*t^7 - 425/168*t^8 - 30629/11340*t^9 + O(t^10)

        Check requesting lower precision::

            sage: (t + t^2 - t^5 + O(t^10)).exp(5)
            1 + t + 3/2*t^2 + 7/6*t^3 + 25/24*t^4 + O(t^5)

        Can\'t get more precision than the input::

            sage: (t + t^2 + O(t^3)).exp(10)
            1 + t + 3/2*t^2 + O(t^3)

        Check some boundary cases::

            sage: (t + O(t^2)).exp(1)
            1 + O(t)
            sage: (t + O(t^2)).exp(0)
            O(t^0)

        Handle nonzero constant term (fixes :issue:`4477`)::

            sage: # needs sage.rings.real_mpfr
            sage: R.<x> = PowerSeriesRing(RR)
            sage: (1 + x + x^2 + O(x^3)).exp()
            2.71828182845905 + 2.71828182845905*x + 4.07742274268857*x^2 + O(x^3)

        ::

            sage: R.<x> = PowerSeriesRing(ZZ)
            sage: (1 + x + O(x^2)).exp()                                                # needs sage.symbolic
            Traceback (most recent call last):
            ...
            ArithmeticError: exponential of constant term does not belong
            to coefficient ring (consider working in a larger ring)

        ::

            sage: R.<x> = PowerSeriesRing(GF(5))
            sage: (1 + x + O(x^2)).exp()
            Traceback (most recent call last):
            ...
            ArithmeticError: constant term of power series does not support exponentiation'''
    @overload
    def exponents(self) -> Any:
        """PowerSeries.exponents(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 425)

        Return the exponents appearing in ``self`` with nonzero coefficients.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(QQ)
            sage: f = t + t^2 - 10/3*t^3
            sage: f.exponents()
            [1, 2, 3]"""
    @overload
    def exponents(self) -> Any:
        """PowerSeries.exponents(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 425)

        Return the exponents appearing in ``self`` with nonzero coefficients.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(QQ)
            sage: f = t + t^2 - 10/3*t^3
            sage: f.exponents()
            [1, 2, 3]"""
    @overload
    def inverse(self) -> Any:
        """PowerSeries.inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 995)

        Return the inverse of self, i.e., self^(-1).

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(QQ, sparse=True)
            sage: t.inverse()
            t^-1
            sage: type(_)
            <class 'sage.rings.laurent_series_ring_element.LaurentSeries'>
            sage: (1-t).inverse()
            1 + t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + ..."""
    @overload
    def inverse(self) -> Any:
        """PowerSeries.inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 995)

        Return the inverse of self, i.e., self^(-1).

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(QQ, sparse=True)
            sage: t.inverse()
            t^-1
            sage: type(_)
            <class 'sage.rings.laurent_series_ring_element.LaurentSeries'>
            sage: (1-t).inverse()
            1 + t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + ..."""
    @overload
    def inverse(self) -> Any:
        """PowerSeries.inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 995)

        Return the inverse of self, i.e., self^(-1).

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(QQ, sparse=True)
            sage: t.inverse()
            t^-1
            sage: type(_)
            <class 'sage.rings.laurent_series_ring_element.LaurentSeries'>
            sage: (1-t).inverse()
            1 + t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + ..."""
    @overload
    def is_dense(self) -> Any:
        """PowerSeries.is_dense(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 208)

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(ZZ)
            sage: t.is_dense()
            True
            sage: R.<t> = PowerSeriesRing(ZZ, sparse=True)
            sage: t.is_dense()
            False"""
    @overload
    def is_dense(self) -> Any:
        """PowerSeries.is_dense(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 208)

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(ZZ)
            sage: t.is_dense()
            True
            sage: R.<t> = PowerSeriesRing(ZZ, sparse=True)
            sage: t.is_dense()
            False"""
    @overload
    def is_dense(self) -> Any:
        """PowerSeries.is_dense(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 208)

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(ZZ)
            sage: t.is_dense()
            True
            sage: R.<t> = PowerSeriesRing(ZZ, sparse=True)
            sage: t.is_dense()
            False"""
    @overload
    def is_gen(self) -> Any:
        """PowerSeries.is_gen(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 221)

        Return ``True`` if this is the generator (the variable) of the power
        series ring.

        EXAMPLES::

            sage: R.<t> = QQ[[]]
            sage: t.is_gen()
            True
            sage: (1 + 2*t).is_gen()
            False

        Note that this only returns ``True`` on the actual generator, not on
        something that happens to be equal to it.

        ::

            sage: (1*t).is_gen()
            False
            sage: 1*t == t
            True"""
    @overload
    def is_gen(self) -> Any:
        """PowerSeries.is_gen(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 221)

        Return ``True`` if this is the generator (the variable) of the power
        series ring.

        EXAMPLES::

            sage: R.<t> = QQ[[]]
            sage: t.is_gen()
            True
            sage: (1 + 2*t).is_gen()
            False

        Note that this only returns ``True`` on the actual generator, not on
        something that happens to be equal to it.

        ::

            sage: (1*t).is_gen()
            False
            sage: 1*t == t
            True"""
    @overload
    def is_gen(self) -> Any:
        """PowerSeries.is_gen(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 221)

        Return ``True`` if this is the generator (the variable) of the power
        series ring.

        EXAMPLES::

            sage: R.<t> = QQ[[]]
            sage: t.is_gen()
            True
            sage: (1 + 2*t).is_gen()
            False

        Note that this only returns ``True`` on the actual generator, not on
        something that happens to be equal to it.

        ::

            sage: (1*t).is_gen()
            False
            sage: 1*t == t
            True"""
    @overload
    def is_gen(self) -> Any:
        """PowerSeries.is_gen(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 221)

        Return ``True`` if this is the generator (the variable) of the power
        series ring.

        EXAMPLES::

            sage: R.<t> = QQ[[]]
            sage: t.is_gen()
            True
            sage: (1 + 2*t).is_gen()
            False

        Note that this only returns ``True`` on the actual generator, not on
        something that happens to be equal to it.

        ::

            sage: (1*t).is_gen()
            False
            sage: 1*t == t
            True"""
    @overload
    def is_monomial(self) -> Any:
        """PowerSeries.is_monomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1233)

        Return ``True`` if this element is a monomial.  That is, if ``self`` is
        `x^n` for some nonnegative integer `n`.

        EXAMPLES::

            sage: k.<z> = PowerSeriesRing(QQ, 'z')
            sage: z.is_monomial()
            True
            sage: k(1).is_monomial()
            True
            sage: (z+1).is_monomial()
            False
            sage: (z^2909).is_monomial()
            True
            sage: (3*z^2909).is_monomial()
            False"""
    @overload
    def is_monomial(self) -> Any:
        """PowerSeries.is_monomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1233)

        Return ``True`` if this element is a monomial.  That is, if ``self`` is
        `x^n` for some nonnegative integer `n`.

        EXAMPLES::

            sage: k.<z> = PowerSeriesRing(QQ, 'z')
            sage: z.is_monomial()
            True
            sage: k(1).is_monomial()
            True
            sage: (z+1).is_monomial()
            False
            sage: (z^2909).is_monomial()
            True
            sage: (3*z^2909).is_monomial()
            False"""
    @overload
    def is_monomial(self) -> Any:
        """PowerSeries.is_monomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1233)

        Return ``True`` if this element is a monomial.  That is, if ``self`` is
        `x^n` for some nonnegative integer `n`.

        EXAMPLES::

            sage: k.<z> = PowerSeriesRing(QQ, 'z')
            sage: z.is_monomial()
            True
            sage: k(1).is_monomial()
            True
            sage: (z+1).is_monomial()
            False
            sage: (z^2909).is_monomial()
            True
            sage: (3*z^2909).is_monomial()
            False"""
    @overload
    def is_monomial(self) -> Any:
        """PowerSeries.is_monomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1233)

        Return ``True`` if this element is a monomial.  That is, if ``self`` is
        `x^n` for some nonnegative integer `n`.

        EXAMPLES::

            sage: k.<z> = PowerSeriesRing(QQ, 'z')
            sage: z.is_monomial()
            True
            sage: k(1).is_monomial()
            True
            sage: (z+1).is_monomial()
            False
            sage: (z^2909).is_monomial()
            True
            sage: (3*z^2909).is_monomial()
            False"""
    @overload
    def is_monomial(self) -> Any:
        """PowerSeries.is_monomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1233)

        Return ``True`` if this element is a monomial.  That is, if ``self`` is
        `x^n` for some nonnegative integer `n`.

        EXAMPLES::

            sage: k.<z> = PowerSeriesRing(QQ, 'z')
            sage: z.is_monomial()
            True
            sage: k(1).is_monomial()
            True
            sage: (z+1).is_monomial()
            False
            sage: (z^2909).is_monomial()
            True
            sage: (3*z^2909).is_monomial()
            False"""
    @overload
    def is_monomial(self) -> Any:
        """PowerSeries.is_monomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1233)

        Return ``True`` if this element is a monomial.  That is, if ``self`` is
        `x^n` for some nonnegative integer `n`.

        EXAMPLES::

            sage: k.<z> = PowerSeriesRing(QQ, 'z')
            sage: z.is_monomial()
            True
            sage: k(1).is_monomial()
            True
            sage: (z+1).is_monomial()
            False
            sage: (z^2909).is_monomial()
            True
            sage: (3*z^2909).is_monomial()
            False"""
    @overload
    def is_sparse(self) -> Any:
        """PowerSeries.is_sparse(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 195)

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(ZZ)
            sage: t.is_sparse()
            False
            sage: R.<t> = PowerSeriesRing(ZZ, sparse=True)
            sage: t.is_sparse()
            True"""
    @overload
    def is_sparse(self) -> Any:
        """PowerSeries.is_sparse(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 195)

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(ZZ)
            sage: t.is_sparse()
            False
            sage: R.<t> = PowerSeriesRing(ZZ, sparse=True)
            sage: t.is_sparse()
            True"""
    @overload
    def is_sparse(self) -> Any:
        """PowerSeries.is_sparse(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 195)

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(ZZ)
            sage: t.is_sparse()
            False
            sage: R.<t> = PowerSeriesRing(ZZ, sparse=True)
            sage: t.is_sparse()
            True"""
    @overload
    def is_square(self) -> Any:
        """PowerSeries.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1540)

        Return ``True`` if this function has a square root in this ring, e.g.,
        there is an element `y` in ``self.parent()``
        such that `y^2` equals ``self``.

        ALGORITHM: If the base ring is a field, this is true whenever the
        power series has even valuation and the leading coefficient is a
        perfect square.

        For an integral domain, it attempts the square root in the
        fraction field and tests whether or not the result lies in the
        original ring.

        EXAMPLES::

            sage: K.<t> = PowerSeriesRing(QQ, 't', 5)
            sage: (1+t).is_square()
            True
            sage: (2+t).is_square()
            False
            sage: (2+t.change_ring(RR)).is_square()
            True
            sage: t.is_square()
            False
            sage: K.<t> = PowerSeriesRing(ZZ, 't', 5)
            sage: (1+t).is_square()
            False
            sage: f = (1+t)^100
            sage: f.is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """PowerSeries.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1540)

        Return ``True`` if this function has a square root in this ring, e.g.,
        there is an element `y` in ``self.parent()``
        such that `y^2` equals ``self``.

        ALGORITHM: If the base ring is a field, this is true whenever the
        power series has even valuation and the leading coefficient is a
        perfect square.

        For an integral domain, it attempts the square root in the
        fraction field and tests whether or not the result lies in the
        original ring.

        EXAMPLES::

            sage: K.<t> = PowerSeriesRing(QQ, 't', 5)
            sage: (1+t).is_square()
            True
            sage: (2+t).is_square()
            False
            sage: (2+t.change_ring(RR)).is_square()
            True
            sage: t.is_square()
            False
            sage: K.<t> = PowerSeriesRing(ZZ, 't', 5)
            sage: (1+t).is_square()
            False
            sage: f = (1+t)^100
            sage: f.is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """PowerSeries.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1540)

        Return ``True`` if this function has a square root in this ring, e.g.,
        there is an element `y` in ``self.parent()``
        such that `y^2` equals ``self``.

        ALGORITHM: If the base ring is a field, this is true whenever the
        power series has even valuation and the leading coefficient is a
        perfect square.

        For an integral domain, it attempts the square root in the
        fraction field and tests whether or not the result lies in the
        original ring.

        EXAMPLES::

            sage: K.<t> = PowerSeriesRing(QQ, 't', 5)
            sage: (1+t).is_square()
            True
            sage: (2+t).is_square()
            False
            sage: (2+t.change_ring(RR)).is_square()
            True
            sage: t.is_square()
            False
            sage: K.<t> = PowerSeriesRing(ZZ, 't', 5)
            sage: (1+t).is_square()
            False
            sage: f = (1+t)^100
            sage: f.is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """PowerSeries.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1540)

        Return ``True`` if this function has a square root in this ring, e.g.,
        there is an element `y` in ``self.parent()``
        such that `y^2` equals ``self``.

        ALGORITHM: If the base ring is a field, this is true whenever the
        power series has even valuation and the leading coefficient is a
        perfect square.

        For an integral domain, it attempts the square root in the
        fraction field and tests whether or not the result lies in the
        original ring.

        EXAMPLES::

            sage: K.<t> = PowerSeriesRing(QQ, 't', 5)
            sage: (1+t).is_square()
            True
            sage: (2+t).is_square()
            False
            sage: (2+t.change_ring(RR)).is_square()
            True
            sage: t.is_square()
            False
            sage: K.<t> = PowerSeriesRing(ZZ, 't', 5)
            sage: (1+t).is_square()
            False
            sage: f = (1+t)^100
            sage: f.is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """PowerSeries.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1540)

        Return ``True`` if this function has a square root in this ring, e.g.,
        there is an element `y` in ``self.parent()``
        such that `y^2` equals ``self``.

        ALGORITHM: If the base ring is a field, this is true whenever the
        power series has even valuation and the leading coefficient is a
        perfect square.

        For an integral domain, it attempts the square root in the
        fraction field and tests whether or not the result lies in the
        original ring.

        EXAMPLES::

            sage: K.<t> = PowerSeriesRing(QQ, 't', 5)
            sage: (1+t).is_square()
            True
            sage: (2+t).is_square()
            False
            sage: (2+t.change_ring(RR)).is_square()
            True
            sage: t.is_square()
            False
            sage: K.<t> = PowerSeriesRing(ZZ, 't', 5)
            sage: (1+t).is_square()
            False
            sage: f = (1+t)^100
            sage: f.is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """PowerSeries.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1540)

        Return ``True`` if this function has a square root in this ring, e.g.,
        there is an element `y` in ``self.parent()``
        such that `y^2` equals ``self``.

        ALGORITHM: If the base ring is a field, this is true whenever the
        power series has even valuation and the leading coefficient is a
        perfect square.

        For an integral domain, it attempts the square root in the
        fraction field and tests whether or not the result lies in the
        original ring.

        EXAMPLES::

            sage: K.<t> = PowerSeriesRing(QQ, 't', 5)
            sage: (1+t).is_square()
            True
            sage: (2+t).is_square()
            False
            sage: (2+t.change_ring(RR)).is_square()
            True
            sage: t.is_square()
            False
            sage: K.<t> = PowerSeriesRing(ZZ, 't', 5)
            sage: (1+t).is_square()
            False
            sage: f = (1+t)^100
            sage: f.is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """PowerSeries.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1540)

        Return ``True`` if this function has a square root in this ring, e.g.,
        there is an element `y` in ``self.parent()``
        such that `y^2` equals ``self``.

        ALGORITHM: If the base ring is a field, this is true whenever the
        power series has even valuation and the leading coefficient is a
        perfect square.

        For an integral domain, it attempts the square root in the
        fraction field and tests whether or not the result lies in the
        original ring.

        EXAMPLES::

            sage: K.<t> = PowerSeriesRing(QQ, 't', 5)
            sage: (1+t).is_square()
            True
            sage: (2+t).is_square()
            False
            sage: (2+t.change_ring(RR)).is_square()
            True
            sage: t.is_square()
            False
            sage: K.<t> = PowerSeriesRing(ZZ, 't', 5)
            sage: (1+t).is_square()
            False
            sage: f = (1+t)^100
            sage: f.is_square()
            True"""
    @overload
    def is_unit(self) -> Any:
        """PowerSeries.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 969)

        Return ``True`` if this power series is invertible.

        A power series is invertible precisely when the
        constant term is invertible.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(ZZ)
            sage: (-1 + t - t^5).is_unit()
            True
            sage: (3 + t - t^5).is_unit()
            False
            sage: O(t^0).is_unit()
            False

        AUTHORS:

        - David Harvey (2006-09-03)"""
    @overload
    def is_unit(self) -> Any:
        """PowerSeries.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 969)

        Return ``True`` if this power series is invertible.

        A power series is invertible precisely when the
        constant term is invertible.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(ZZ)
            sage: (-1 + t - t^5).is_unit()
            True
            sage: (3 + t - t^5).is_unit()
            False
            sage: O(t^0).is_unit()
            False

        AUTHORS:

        - David Harvey (2006-09-03)"""
    @overload
    def is_unit(self) -> Any:
        """PowerSeries.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 969)

        Return ``True`` if this power series is invertible.

        A power series is invertible precisely when the
        constant term is invertible.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(ZZ)
            sage: (-1 + t - t^5).is_unit()
            True
            sage: (3 + t - t^5).is_unit()
            False
            sage: O(t^0).is_unit()
            False

        AUTHORS:

        - David Harvey (2006-09-03)"""
    @overload
    def is_unit(self) -> Any:
        """PowerSeries.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 969)

        Return ``True`` if this power series is invertible.

        A power series is invertible precisely when the
        constant term is invertible.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(ZZ)
            sage: (-1 + t - t^5).is_unit()
            True
            sage: (3 + t - t^5).is_unit()
            False
            sage: O(t^0).is_unit()
            False

        AUTHORS:

        - David Harvey (2006-09-03)"""
    def jacobi_continued_fraction(self) -> Any:
        """PowerSeries.jacobi_continued_fraction(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1318)

        Return the Jacobi continued fraction of ``self``.

        The J-fraction or Jacobi continued fraction of a power series
        is a continued fraction expansion with steps of size two. We use
        the following convention

        .. MATH::

            1 / (1 + A_0 t + B_0 t^2 / (1 + A_1 t + B_1 t^2 / (1 + \\cdots)))

        OUTPUT:

        tuple of pairs `(A_n, B_n)` for `n \\geq 0`

        The expansion is done as long as possible given the precision.
        Whenever the expansion is not well-defined, because it would
        require to divide by zero, an exception is raised.

        See section 2.7 of [Kra1999det]_ for the close relationship
        of this kind of expansion with Hankel determinants and
        orthogonal polynomials.

        EXAMPLES::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: s = sum(factorial(k) * t**k for k in range(12)).O(12)
            sage: s.jacobi_continued_fraction()
            ((-1, -1), (-3, -4), (-5, -9), (-7, -16), (-9, -25))

        Another example::

            sage: (log(1+t)/t).jacobi_continued_fraction()
            ((1/2, -1/12),
             (1/2, -1/15),
             (1/2, -9/140),
             (1/2, -4/63),
             (1/2, -25/396),
             (1/2, -9/143),
             (1/2, -49/780),
             (1/2, -16/255),
             (1/2, -81/1292))

        TESTS::

             sage: (t).jacobi_continued_fraction()
             Traceback (most recent call last):
             ...
             ValueError: vanishing constant term, no expansion
             sage: (1/(1+3*t)).jacobi_continued_fraction()
             Traceback (most recent call last):
             ...
             ValueError: vanishing term, no further expansion"""
    @overload
    def laurent_series(self) -> Any:
        """PowerSeries.laurent_series(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2801)

        Return the Laurent series associated to this power series, i.e.,
        this series considered as a Laurent series.

        EXAMPLES::

            sage: k.<w> = QQ[[]]
            sage: f = 1 + 17*w + 15*w^3 + O(w^5)
            sage: parent(f)
            Power Series Ring in w over Rational Field
            sage: g = f.laurent_series(); g
            1 + 17*w + 15*w^3 + O(w^5)"""
    @overload
    def laurent_series(self) -> Any:
        """PowerSeries.laurent_series(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2801)

        Return the Laurent series associated to this power series, i.e.,
        this series considered as a Laurent series.

        EXAMPLES::

            sage: k.<w> = QQ[[]]
            sage: f = 1 + 17*w + 15*w^3 + O(w^5)
            sage: parent(f)
            Power Series Ring in w over Rational Field
            sage: g = f.laurent_series(); g
            1 + 17*w + 15*w^3 + O(w^5)"""
    @overload
    def lift_to_precision(self, absprec=...) -> Any:
        """PowerSeries.lift_to_precision(self, absprec=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 482)

        Return a congruent power series with absolute precision at least
        ``absprec``.

        INPUT:

        - ``absprec`` -- integer or ``None`` (default: ``None``); the
          absolute precision of the result. If ``None``, lifts to an exact
          element.

        EXAMPLES::

            sage: A.<t> = PowerSeriesRing(GF(5))
            sage: x = t + t^2 + O(t^5)
            sage: x.lift_to_precision(10)
            t + t^2 + O(t^10)
            sage: x.lift_to_precision()
            t + t^2"""
    @overload
    def lift_to_precision(self) -> Any:
        """PowerSeries.lift_to_precision(self, absprec=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 482)

        Return a congruent power series with absolute precision at least
        ``absprec``.

        INPUT:

        - ``absprec`` -- integer or ``None`` (default: ``None``); the
          absolute precision of the result. If ``None``, lifts to an exact
          element.

        EXAMPLES::

            sage: A.<t> = PowerSeriesRing(GF(5))
            sage: x = t + t^2 + O(t^5)
            sage: x.lift_to_precision(10)
            t + t^2 + O(t^10)
            sage: x.lift_to_precision()
            t + t^2"""
    def list(self) -> Any:
        """PowerSeries.list(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 440)

        See this method in derived classes:

        - :meth:`sage.rings.power_series_poly.PowerSeries_poly.list`,

        - :meth:`sage.rings.multi_power_series_ring_element.MPowerSeries.list`

        Implementations *MUST* override this in the derived class.

        EXAMPLES::

            sage: from sage.rings.power_series_ring_element import PowerSeries
            sage: R.<x> = PowerSeriesRing(ZZ)
            sage: PowerSeries.list(1 + x^2)
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def log(self, prec=...) -> Any:
        """PowerSeries.log(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2615)

        Return log of this power series to the indicated precision.

        This works only if the constant term of the power series is 1
        or the base ring can take the logarithm of the constant coefficient.

        INPUT:

        - ``prec`` -- integer (default: ``self.parent().default_prec()``)

        ALGORITHM: See :meth:`solve_linear_de()`.

        .. WARNING::

            Screwy things can happen if the coefficient ring is not a
            field of characteristic zero. See :meth:`solve_linear_de()`.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(QQ, default_prec=10)
            sage: (1 + t + O(t^10)).log()
            t - 1/2*t^2 + 1/3*t^3 - 1/4*t^4 + 1/5*t^5 - 1/6*t^6 + 1/7*t^7
              - 1/8*t^8 + 1/9*t^9 + O(t^10)

            sage: t.exp().log()
            t + O(t^10)

            sage: (1 + t).log().exp()
            1 + t + O(t^10)

            sage: (-1 + t + O(t^10)).log()
            Traceback (most recent call last):
            ...
            ArithmeticError: constant term of power series is not 1

            sage: # needs sage.rings.real_mpfr
            sage: R.<t> = PowerSeriesRing(RR)
            sage: (2 + t).log().exp()
            2.00000000000000 + 1.00000000000000*t + O(t^20)"""
    @overload
    def log(self) -> Any:
        """PowerSeries.log(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2615)

        Return log of this power series to the indicated precision.

        This works only if the constant term of the power series is 1
        or the base ring can take the logarithm of the constant coefficient.

        INPUT:

        - ``prec`` -- integer (default: ``self.parent().default_prec()``)

        ALGORITHM: See :meth:`solve_linear_de()`.

        .. WARNING::

            Screwy things can happen if the coefficient ring is not a
            field of characteristic zero. See :meth:`solve_linear_de()`.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(QQ, default_prec=10)
            sage: (1 + t + O(t^10)).log()
            t - 1/2*t^2 + 1/3*t^3 - 1/4*t^4 + 1/5*t^5 - 1/6*t^6 + 1/7*t^7
              - 1/8*t^8 + 1/9*t^9 + O(t^10)

            sage: t.exp().log()
            t + O(t^10)

            sage: (1 + t).log().exp()
            1 + t + O(t^10)

            sage: (-1 + t + O(t^10)).log()
            Traceback (most recent call last):
            ...
            ArithmeticError: constant term of power series is not 1

            sage: # needs sage.rings.real_mpfr
            sage: R.<t> = PowerSeriesRing(RR)
            sage: (2 + t).log().exp()
            2.00000000000000 + 1.00000000000000*t + O(t^20)"""
    @overload
    def log(self) -> Any:
        """PowerSeries.log(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2615)

        Return log of this power series to the indicated precision.

        This works only if the constant term of the power series is 1
        or the base ring can take the logarithm of the constant coefficient.

        INPUT:

        - ``prec`` -- integer (default: ``self.parent().default_prec()``)

        ALGORITHM: See :meth:`solve_linear_de()`.

        .. WARNING::

            Screwy things can happen if the coefficient ring is not a
            field of characteristic zero. See :meth:`solve_linear_de()`.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(QQ, default_prec=10)
            sage: (1 + t + O(t^10)).log()
            t - 1/2*t^2 + 1/3*t^3 - 1/4*t^4 + 1/5*t^5 - 1/6*t^6 + 1/7*t^7
              - 1/8*t^8 + 1/9*t^9 + O(t^10)

            sage: t.exp().log()
            t + O(t^10)

            sage: (1 + t).log().exp()
            1 + t + O(t^10)

            sage: (-1 + t + O(t^10)).log()
            Traceback (most recent call last):
            ...
            ArithmeticError: constant term of power series is not 1

            sage: # needs sage.rings.real_mpfr
            sage: R.<t> = PowerSeriesRing(RR)
            sage: (2 + t).log().exp()
            2.00000000000000 + 1.00000000000000*t + O(t^20)"""
    @overload
    def log(self) -> Any:
        """PowerSeries.log(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2615)

        Return log of this power series to the indicated precision.

        This works only if the constant term of the power series is 1
        or the base ring can take the logarithm of the constant coefficient.

        INPUT:

        - ``prec`` -- integer (default: ``self.parent().default_prec()``)

        ALGORITHM: See :meth:`solve_linear_de()`.

        .. WARNING::

            Screwy things can happen if the coefficient ring is not a
            field of characteristic zero. See :meth:`solve_linear_de()`.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(QQ, default_prec=10)
            sage: (1 + t + O(t^10)).log()
            t - 1/2*t^2 + 1/3*t^3 - 1/4*t^4 + 1/5*t^5 - 1/6*t^6 + 1/7*t^7
              - 1/8*t^8 + 1/9*t^9 + O(t^10)

            sage: t.exp().log()
            t + O(t^10)

            sage: (1 + t).log().exp()
            1 + t + O(t^10)

            sage: (-1 + t + O(t^10)).log()
            Traceback (most recent call last):
            ...
            ArithmeticError: constant term of power series is not 1

            sage: # needs sage.rings.real_mpfr
            sage: R.<t> = PowerSeriesRing(RR)
            sage: (2 + t).log().exp()
            2.00000000000000 + 1.00000000000000*t + O(t^20)"""
    @overload
    def log(self) -> Any:
        """PowerSeries.log(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2615)

        Return log of this power series to the indicated precision.

        This works only if the constant term of the power series is 1
        or the base ring can take the logarithm of the constant coefficient.

        INPUT:

        - ``prec`` -- integer (default: ``self.parent().default_prec()``)

        ALGORITHM: See :meth:`solve_linear_de()`.

        .. WARNING::

            Screwy things can happen if the coefficient ring is not a
            field of characteristic zero. See :meth:`solve_linear_de()`.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(QQ, default_prec=10)
            sage: (1 + t + O(t^10)).log()
            t - 1/2*t^2 + 1/3*t^3 - 1/4*t^4 + 1/5*t^5 - 1/6*t^6 + 1/7*t^7
              - 1/8*t^8 + 1/9*t^9 + O(t^10)

            sage: t.exp().log()
            t + O(t^10)

            sage: (1 + t).log().exp()
            1 + t + O(t^10)

            sage: (-1 + t + O(t^10)).log()
            Traceback (most recent call last):
            ...
            ArithmeticError: constant term of power series is not 1

            sage: # needs sage.rings.real_mpfr
            sage: R.<t> = PowerSeriesRing(RR)
            sage: (2 + t).log().exp()
            2.00000000000000 + 1.00000000000000*t + O(t^20)"""
    @overload
    def log(self) -> Any:
        """PowerSeries.log(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2615)

        Return log of this power series to the indicated precision.

        This works only if the constant term of the power series is 1
        or the base ring can take the logarithm of the constant coefficient.

        INPUT:

        - ``prec`` -- integer (default: ``self.parent().default_prec()``)

        ALGORITHM: See :meth:`solve_linear_de()`.

        .. WARNING::

            Screwy things can happen if the coefficient ring is not a
            field of characteristic zero. See :meth:`solve_linear_de()`.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(QQ, default_prec=10)
            sage: (1 + t + O(t^10)).log()
            t - 1/2*t^2 + 1/3*t^3 - 1/4*t^4 + 1/5*t^5 - 1/6*t^6 + 1/7*t^7
              - 1/8*t^8 + 1/9*t^9 + O(t^10)

            sage: t.exp().log()
            t + O(t^10)

            sage: (1 + t).log().exp()
            1 + t + O(t^10)

            sage: (-1 + t + O(t^10)).log()
            Traceback (most recent call last):
            ...
            ArithmeticError: constant term of power series is not 1

            sage: # needs sage.rings.real_mpfr
            sage: R.<t> = PowerSeriesRing(RR)
            sage: (2 + t).log().exp()
            2.00000000000000 + 1.00000000000000*t + O(t^20)"""
    @overload
    def map_coefficients(self, f, new_base_ring=...) -> Any:
        """PowerSeries.map_coefficients(self, f, new_base_ring=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1255)

        Return the series obtained by applying ``f`` to the nonzero
        coefficients of ``self``.

        If ``f`` is a :class:`sage.categories.map.Map`, then the resulting
        series will be defined over the codomain of ``f``. Otherwise, the
        resulting polynomial will be over the same ring as ``self``. Set
        ``new_base_ring`` to override this behaviour.

        INPUT:

        - ``f`` -- a callable that will be applied to the coefficients of ``self``

        - ``new_base_ring`` -- (optional) if given, the resulting polynomial
          will be defined over this ring

        EXAMPLES::

            sage: R.<x> = SR[[]]                                                        # needs sage.symbolic
            sage: f = (1+I)*x^2 + 3*x - I                                               # needs sage.symbolic
            sage: f.map_coefficients(lambda z: z.conjugate())                           # needs sage.symbolic
            I + 3*x + (-I + 1)*x^2
            sage: R.<x> = ZZ[[]]
            sage: f = x^2 + 2
            sage: f.map_coefficients(lambda a: a + 42)
            44 + 43*x^2

        Examples with different base ring::

            sage: R.<x> = ZZ[[]]
            sage: k = GF(2)
            sage: residue = lambda x: k(x)
            sage: f = 4*x^2+x+3
            sage: g = f.map_coefficients(residue); g
            1 + x
            sage: g.parent()
            Power Series Ring in x over Integer Ring
            sage: g = f.map_coefficients(residue, new_base_ring=k); g
            1 + x
            sage: g.parent()
            Power Series Ring in x over Finite Field of size 2
            sage: residue = k.coerce_map_from(ZZ)
            sage: g = f.map_coefficients(residue); g
            1 + x
            sage: g.parent()
            Power Series Ring in x over Finite Field of size 2

        Tests other implementations::

            sage: # needs sage.libs.pari
            sage: R.<q> = PowerSeriesRing(GF(11), implementation='pari')
            sage: f = q - q^3 + O(q^10)
            sage: f.map_coefficients(lambda c: c - 2)
            10*q + 8*q^3 + O(q^10)"""
    @overload
    def map_coefficients(self, lambdaz) -> Any:
        """PowerSeries.map_coefficients(self, f, new_base_ring=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1255)

        Return the series obtained by applying ``f`` to the nonzero
        coefficients of ``self``.

        If ``f`` is a :class:`sage.categories.map.Map`, then the resulting
        series will be defined over the codomain of ``f``. Otherwise, the
        resulting polynomial will be over the same ring as ``self``. Set
        ``new_base_ring`` to override this behaviour.

        INPUT:

        - ``f`` -- a callable that will be applied to the coefficients of ``self``

        - ``new_base_ring`` -- (optional) if given, the resulting polynomial
          will be defined over this ring

        EXAMPLES::

            sage: R.<x> = SR[[]]                                                        # needs sage.symbolic
            sage: f = (1+I)*x^2 + 3*x - I                                               # needs sage.symbolic
            sage: f.map_coefficients(lambda z: z.conjugate())                           # needs sage.symbolic
            I + 3*x + (-I + 1)*x^2
            sage: R.<x> = ZZ[[]]
            sage: f = x^2 + 2
            sage: f.map_coefficients(lambda a: a + 42)
            44 + 43*x^2

        Examples with different base ring::

            sage: R.<x> = ZZ[[]]
            sage: k = GF(2)
            sage: residue = lambda x: k(x)
            sage: f = 4*x^2+x+3
            sage: g = f.map_coefficients(residue); g
            1 + x
            sage: g.parent()
            Power Series Ring in x over Integer Ring
            sage: g = f.map_coefficients(residue, new_base_ring=k); g
            1 + x
            sage: g.parent()
            Power Series Ring in x over Finite Field of size 2
            sage: residue = k.coerce_map_from(ZZ)
            sage: g = f.map_coefficients(residue); g
            1 + x
            sage: g.parent()
            Power Series Ring in x over Finite Field of size 2

        Tests other implementations::

            sage: # needs sage.libs.pari
            sage: R.<q> = PowerSeriesRing(GF(11), implementation='pari')
            sage: f = q - q^3 + O(q^10)
            sage: f.map_coefficients(lambda c: c - 2)
            10*q + 8*q^3 + O(q^10)"""
    @overload
    def map_coefficients(self, lambdaa) -> Any:
        """PowerSeries.map_coefficients(self, f, new_base_ring=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1255)

        Return the series obtained by applying ``f`` to the nonzero
        coefficients of ``self``.

        If ``f`` is a :class:`sage.categories.map.Map`, then the resulting
        series will be defined over the codomain of ``f``. Otherwise, the
        resulting polynomial will be over the same ring as ``self``. Set
        ``new_base_ring`` to override this behaviour.

        INPUT:

        - ``f`` -- a callable that will be applied to the coefficients of ``self``

        - ``new_base_ring`` -- (optional) if given, the resulting polynomial
          will be defined over this ring

        EXAMPLES::

            sage: R.<x> = SR[[]]                                                        # needs sage.symbolic
            sage: f = (1+I)*x^2 + 3*x - I                                               # needs sage.symbolic
            sage: f.map_coefficients(lambda z: z.conjugate())                           # needs sage.symbolic
            I + 3*x + (-I + 1)*x^2
            sage: R.<x> = ZZ[[]]
            sage: f = x^2 + 2
            sage: f.map_coefficients(lambda a: a + 42)
            44 + 43*x^2

        Examples with different base ring::

            sage: R.<x> = ZZ[[]]
            sage: k = GF(2)
            sage: residue = lambda x: k(x)
            sage: f = 4*x^2+x+3
            sage: g = f.map_coefficients(residue); g
            1 + x
            sage: g.parent()
            Power Series Ring in x over Integer Ring
            sage: g = f.map_coefficients(residue, new_base_ring=k); g
            1 + x
            sage: g.parent()
            Power Series Ring in x over Finite Field of size 2
            sage: residue = k.coerce_map_from(ZZ)
            sage: g = f.map_coefficients(residue); g
            1 + x
            sage: g.parent()
            Power Series Ring in x over Finite Field of size 2

        Tests other implementations::

            sage: # needs sage.libs.pari
            sage: R.<q> = PowerSeriesRing(GF(11), implementation='pari')
            sage: f = q - q^3 + O(q^10)
            sage: f.map_coefficients(lambda c: c - 2)
            10*q + 8*q^3 + O(q^10)"""
    @overload
    def map_coefficients(self, residue) -> Any:
        """PowerSeries.map_coefficients(self, f, new_base_ring=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1255)

        Return the series obtained by applying ``f`` to the nonzero
        coefficients of ``self``.

        If ``f`` is a :class:`sage.categories.map.Map`, then the resulting
        series will be defined over the codomain of ``f``. Otherwise, the
        resulting polynomial will be over the same ring as ``self``. Set
        ``new_base_ring`` to override this behaviour.

        INPUT:

        - ``f`` -- a callable that will be applied to the coefficients of ``self``

        - ``new_base_ring`` -- (optional) if given, the resulting polynomial
          will be defined over this ring

        EXAMPLES::

            sage: R.<x> = SR[[]]                                                        # needs sage.symbolic
            sage: f = (1+I)*x^2 + 3*x - I                                               # needs sage.symbolic
            sage: f.map_coefficients(lambda z: z.conjugate())                           # needs sage.symbolic
            I + 3*x + (-I + 1)*x^2
            sage: R.<x> = ZZ[[]]
            sage: f = x^2 + 2
            sage: f.map_coefficients(lambda a: a + 42)
            44 + 43*x^2

        Examples with different base ring::

            sage: R.<x> = ZZ[[]]
            sage: k = GF(2)
            sage: residue = lambda x: k(x)
            sage: f = 4*x^2+x+3
            sage: g = f.map_coefficients(residue); g
            1 + x
            sage: g.parent()
            Power Series Ring in x over Integer Ring
            sage: g = f.map_coefficients(residue, new_base_ring=k); g
            1 + x
            sage: g.parent()
            Power Series Ring in x over Finite Field of size 2
            sage: residue = k.coerce_map_from(ZZ)
            sage: g = f.map_coefficients(residue); g
            1 + x
            sage: g.parent()
            Power Series Ring in x over Finite Field of size 2

        Tests other implementations::

            sage: # needs sage.libs.pari
            sage: R.<q> = PowerSeriesRing(GF(11), implementation='pari')
            sage: f = q - q^3 + O(q^10)
            sage: f.map_coefficients(lambda c: c - 2)
            10*q + 8*q^3 + O(q^10)"""
    @overload
    def map_coefficients(self, residue, new_base_ring=...) -> Any:
        """PowerSeries.map_coefficients(self, f, new_base_ring=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1255)

        Return the series obtained by applying ``f`` to the nonzero
        coefficients of ``self``.

        If ``f`` is a :class:`sage.categories.map.Map`, then the resulting
        series will be defined over the codomain of ``f``. Otherwise, the
        resulting polynomial will be over the same ring as ``self``. Set
        ``new_base_ring`` to override this behaviour.

        INPUT:

        - ``f`` -- a callable that will be applied to the coefficients of ``self``

        - ``new_base_ring`` -- (optional) if given, the resulting polynomial
          will be defined over this ring

        EXAMPLES::

            sage: R.<x> = SR[[]]                                                        # needs sage.symbolic
            sage: f = (1+I)*x^2 + 3*x - I                                               # needs sage.symbolic
            sage: f.map_coefficients(lambda z: z.conjugate())                           # needs sage.symbolic
            I + 3*x + (-I + 1)*x^2
            sage: R.<x> = ZZ[[]]
            sage: f = x^2 + 2
            sage: f.map_coefficients(lambda a: a + 42)
            44 + 43*x^2

        Examples with different base ring::

            sage: R.<x> = ZZ[[]]
            sage: k = GF(2)
            sage: residue = lambda x: k(x)
            sage: f = 4*x^2+x+3
            sage: g = f.map_coefficients(residue); g
            1 + x
            sage: g.parent()
            Power Series Ring in x over Integer Ring
            sage: g = f.map_coefficients(residue, new_base_ring=k); g
            1 + x
            sage: g.parent()
            Power Series Ring in x over Finite Field of size 2
            sage: residue = k.coerce_map_from(ZZ)
            sage: g = f.map_coefficients(residue); g
            1 + x
            sage: g.parent()
            Power Series Ring in x over Finite Field of size 2

        Tests other implementations::

            sage: # needs sage.libs.pari
            sage: R.<q> = PowerSeriesRing(GF(11), implementation='pari')
            sage: f = q - q^3 + O(q^10)
            sage: f.map_coefficients(lambda c: c - 2)
            10*q + 8*q^3 + O(q^10)"""
    @overload
    def map_coefficients(self, residue) -> Any:
        """PowerSeries.map_coefficients(self, f, new_base_ring=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1255)

        Return the series obtained by applying ``f`` to the nonzero
        coefficients of ``self``.

        If ``f`` is a :class:`sage.categories.map.Map`, then the resulting
        series will be defined over the codomain of ``f``. Otherwise, the
        resulting polynomial will be over the same ring as ``self``. Set
        ``new_base_ring`` to override this behaviour.

        INPUT:

        - ``f`` -- a callable that will be applied to the coefficients of ``self``

        - ``new_base_ring`` -- (optional) if given, the resulting polynomial
          will be defined over this ring

        EXAMPLES::

            sage: R.<x> = SR[[]]                                                        # needs sage.symbolic
            sage: f = (1+I)*x^2 + 3*x - I                                               # needs sage.symbolic
            sage: f.map_coefficients(lambda z: z.conjugate())                           # needs sage.symbolic
            I + 3*x + (-I + 1)*x^2
            sage: R.<x> = ZZ[[]]
            sage: f = x^2 + 2
            sage: f.map_coefficients(lambda a: a + 42)
            44 + 43*x^2

        Examples with different base ring::

            sage: R.<x> = ZZ[[]]
            sage: k = GF(2)
            sage: residue = lambda x: k(x)
            sage: f = 4*x^2+x+3
            sage: g = f.map_coefficients(residue); g
            1 + x
            sage: g.parent()
            Power Series Ring in x over Integer Ring
            sage: g = f.map_coefficients(residue, new_base_ring=k); g
            1 + x
            sage: g.parent()
            Power Series Ring in x over Finite Field of size 2
            sage: residue = k.coerce_map_from(ZZ)
            sage: g = f.map_coefficients(residue); g
            1 + x
            sage: g.parent()
            Power Series Ring in x over Finite Field of size 2

        Tests other implementations::

            sage: # needs sage.libs.pari
            sage: R.<q> = PowerSeriesRing(GF(11), implementation='pari')
            sage: f = q - q^3 + O(q^10)
            sage: f.map_coefficients(lambda c: c - 2)
            10*q + 8*q^3 + O(q^10)"""
    @overload
    def map_coefficients(self, lambdac) -> Any:
        """PowerSeries.map_coefficients(self, f, new_base_ring=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1255)

        Return the series obtained by applying ``f`` to the nonzero
        coefficients of ``self``.

        If ``f`` is a :class:`sage.categories.map.Map`, then the resulting
        series will be defined over the codomain of ``f``. Otherwise, the
        resulting polynomial will be over the same ring as ``self``. Set
        ``new_base_ring`` to override this behaviour.

        INPUT:

        - ``f`` -- a callable that will be applied to the coefficients of ``self``

        - ``new_base_ring`` -- (optional) if given, the resulting polynomial
          will be defined over this ring

        EXAMPLES::

            sage: R.<x> = SR[[]]                                                        # needs sage.symbolic
            sage: f = (1+I)*x^2 + 3*x - I                                               # needs sage.symbolic
            sage: f.map_coefficients(lambda z: z.conjugate())                           # needs sage.symbolic
            I + 3*x + (-I + 1)*x^2
            sage: R.<x> = ZZ[[]]
            sage: f = x^2 + 2
            sage: f.map_coefficients(lambda a: a + 42)
            44 + 43*x^2

        Examples with different base ring::

            sage: R.<x> = ZZ[[]]
            sage: k = GF(2)
            sage: residue = lambda x: k(x)
            sage: f = 4*x^2+x+3
            sage: g = f.map_coefficients(residue); g
            1 + x
            sage: g.parent()
            Power Series Ring in x over Integer Ring
            sage: g = f.map_coefficients(residue, new_base_ring=k); g
            1 + x
            sage: g.parent()
            Power Series Ring in x over Finite Field of size 2
            sage: residue = k.coerce_map_from(ZZ)
            sage: g = f.map_coefficients(residue); g
            1 + x
            sage: g.parent()
            Power Series Ring in x over Finite Field of size 2

        Tests other implementations::

            sage: # needs sage.libs.pari
            sage: R.<q> = PowerSeriesRing(GF(11), implementation='pari')
            sage: f = q - q^3 + O(q^10)
            sage: f.map_coefficients(lambda c: c - 2)
            10*q + 8*q^3 + O(q^10)"""
    def nth_root(self, n, prec=...) -> Any:
        """PowerSeries.nth_root(self, n, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1822)

        Return the ``n``-th root of this power series.

        INPUT:

        - ``n`` -- integer

        - ``prec`` -- integer (optional); precision of the result. Though, if
          this series has finite precision, then the result cannot have larger
          precision.

        EXAMPLES::

            sage: R.<x> = QQ[[]]
            sage: (1+x).nth_root(5)
            1 + 1/5*x - 2/25*x^2 + ... + 12039376311816/2384185791015625*x^19 + O(x^20)

            sage: (1 + x + O(x^5)).nth_root(5)
            1 + 1/5*x - 2/25*x^2 + 6/125*x^3 - 21/625*x^4 + O(x^5)

        Check that the results are consistent with taking log and exponential::

            sage: R.<x> = PowerSeriesRing(QQ, default_prec=100)
            sage: p = (1 + 2*x - x^4)**200
            sage: p1 = p.nth_root(1000, prec=100)
            sage: p2 = (p.log()/1000).exp()
            sage: p1.prec() == p2.prec() == 100
            True
            sage: p1.polynomial() == p2.polynomial()
            True

        Positive characteristic::

            sage: R.<u> = GF(3)[[]]
            sage: p = 1 + 2 * u^2
            sage: p.nth_root(4)
            1 + 2*u^2 + u^6 + 2*u^8 + u^12 + 2*u^14 + O(u^20)
            sage: p.nth_root(4)**4
            1 + 2*u^2 + O(u^20)

        TESTS:

        Check that exact roots show infinite precision::

            sage: ((1+x)^5).nth_root(5)
            1 + x

        Check precision on `O(x^r)`::

            sage: O(x^4).nth_root(2)
            O(x^2)
            sage: O(x^4).nth_root(3)
            O(x^1)
            sage: O(x^4).nth_root(4)
            O(x^1)

        Check precision on higher valuation series::

            sage: (x^5+x^6+O(x^7)).nth_root(5)
            x + 1/5*x^2 + O(x^3)"""
    @overload
    def ogf_to_egf(self) -> Any:
        """PowerSeries.ogf_to_egf(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2837)

        Return the exponential generating function power series,
        assuming ``self`` is an ordinary generating function power series.

        This is a formal Borel transform.

        This can also be computed as ``serconvol(f,exp(t))`` in PARI/GP.

        .. SEEALSO:: :meth:`egf_to_ogf` for the inverse method.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(QQ)
            sage: f = t + t^2 + 2*t^3
            sage: f.ogf_to_egf()
            t + 1/2*t^2 + 1/3*t^3"""
    @overload
    def ogf_to_egf(self) -> Any:
        """PowerSeries.ogf_to_egf(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2837)

        Return the exponential generating function power series,
        assuming ``self`` is an ordinary generating function power series.

        This is a formal Borel transform.

        This can also be computed as ``serconvol(f,exp(t))`` in PARI/GP.

        .. SEEALSO:: :meth:`egf_to_ogf` for the inverse method.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(QQ)
            sage: f = t + t^2 + 2*t^3
            sage: f.ogf_to_egf()
            t + 1/2*t^2 + 1/3*t^3"""
    @overload
    def padded_list(self, n=...) -> Any:
        """PowerSeries.padded_list(self, n=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 538)

        Return a list of coefficients of ``self`` up to (but not including)
        `q^n`.

        Includes 0s in the list on the right so that the list has length `n`.

        INPUT:

        - ``n`` -- (optional) an integer that is at least 0. If ``n`` is
          not given, it will be taken to be the precision of ``self``,
          unless this is ``+Infinity``, in which case we just return
          ``self.list()``.

        EXAMPLES::

            sage: R.<q> = PowerSeriesRing(QQ)
            sage: f = 1 - 17*q + 13*q^2 + 10*q^4 + O(q^7)
            sage: f.list()
            [1, -17, 13, 0, 10]
            sage: f.padded_list(7)
            [1, -17, 13, 0, 10, 0, 0]
            sage: f.padded_list(10)
            [1, -17, 13, 0, 10, 0, 0, 0, 0, 0]
            sage: f.padded_list(3)
            [1, -17, 13]
            sage: f.padded_list()
            [1, -17, 13, 0, 10, 0, 0]
            sage: g = 1 - 17*q + 13*q^2 + 10*q^4
            sage: g.list()
            [1, -17, 13, 0, 10]
            sage: g.padded_list()
            [1, -17, 13, 0, 10]
            sage: g.padded_list(10)
            [1, -17, 13, 0, 10, 0, 0, 0, 0, 0]"""
    @overload
    def padded_list(self) -> Any:
        """PowerSeries.padded_list(self, n=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 538)

        Return a list of coefficients of ``self`` up to (but not including)
        `q^n`.

        Includes 0s in the list on the right so that the list has length `n`.

        INPUT:

        - ``n`` -- (optional) an integer that is at least 0. If ``n`` is
          not given, it will be taken to be the precision of ``self``,
          unless this is ``+Infinity``, in which case we just return
          ``self.list()``.

        EXAMPLES::

            sage: R.<q> = PowerSeriesRing(QQ)
            sage: f = 1 - 17*q + 13*q^2 + 10*q^4 + O(q^7)
            sage: f.list()
            [1, -17, 13, 0, 10]
            sage: f.padded_list(7)
            [1, -17, 13, 0, 10, 0, 0]
            sage: f.padded_list(10)
            [1, -17, 13, 0, 10, 0, 0, 0, 0, 0]
            sage: f.padded_list(3)
            [1, -17, 13]
            sage: f.padded_list()
            [1, -17, 13, 0, 10, 0, 0]
            sage: g = 1 - 17*q + 13*q^2 + 10*q^4
            sage: g.list()
            [1, -17, 13, 0, 10]
            sage: g.padded_list()
            [1, -17, 13, 0, 10]
            sage: g.padded_list(10)
            [1, -17, 13, 0, 10, 0, 0, 0, 0, 0]"""
    @overload
    def padded_list(self) -> Any:
        """PowerSeries.padded_list(self, n=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 538)

        Return a list of coefficients of ``self`` up to (but not including)
        `q^n`.

        Includes 0s in the list on the right so that the list has length `n`.

        INPUT:

        - ``n`` -- (optional) an integer that is at least 0. If ``n`` is
          not given, it will be taken to be the precision of ``self``,
          unless this is ``+Infinity``, in which case we just return
          ``self.list()``.

        EXAMPLES::

            sage: R.<q> = PowerSeriesRing(QQ)
            sage: f = 1 - 17*q + 13*q^2 + 10*q^4 + O(q^7)
            sage: f.list()
            [1, -17, 13, 0, 10]
            sage: f.padded_list(7)
            [1, -17, 13, 0, 10, 0, 0]
            sage: f.padded_list(10)
            [1, -17, 13, 0, 10, 0, 0, 0, 0, 0]
            sage: f.padded_list(3)
            [1, -17, 13]
            sage: f.padded_list()
            [1, -17, 13, 0, 10, 0, 0]
            sage: g = 1 - 17*q + 13*q^2 + 10*q^4
            sage: g.list()
            [1, -17, 13, 0, 10]
            sage: g.padded_list()
            [1, -17, 13, 0, 10]
            sage: g.padded_list(10)
            [1, -17, 13, 0, 10, 0, 0, 0, 0, 0]"""
    def polynomial(self) -> Any:
        """PowerSeries.polynomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 461)

        See this method in derived classes:

        - :meth:`sage.rings.power_series_poly.PowerSeries_poly.polynomial`,

        - :meth:`sage.rings.multi_power_series_ring_element.MPowerSeries.polynomial`

        Implementations *MUST* override this in the derived class.

        EXAMPLES::

            sage: from sage.rings.power_series_ring_element import PowerSeries
            sage: R.<x> = PowerSeriesRing(ZZ)
            sage: PowerSeries.polynomial(1 + x^2)
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def prec(self) -> Any:
        """PowerSeries.prec(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 588)

        The precision of `...+O(x^r)` is by definition
        `r`.

        EXAMPLES::

            sage: R.<t> = ZZ[[]]
            sage: (t^2 + O(t^3)).prec()
            3
            sage: (1 - t^2 + O(t^100)).prec()
            100"""
    @overload
    def prec(self) -> Any:
        """PowerSeries.prec(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 588)

        The precision of `...+O(x^r)` is by definition
        `r`.

        EXAMPLES::

            sage: R.<t> = ZZ[[]]
            sage: (t^2 + O(t^3)).prec()
            3
            sage: (1 - t^2 + O(t^100)).prec()
            100"""
    @overload
    def prec(self) -> Any:
        """PowerSeries.prec(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 588)

        The precision of `...+O(x^r)` is by definition
        `r`.

        EXAMPLES::

            sage: R.<t> = ZZ[[]]
            sage: (t^2 + O(t^3)).prec()
            3
            sage: (1 - t^2 + O(t^100)).prec()
            100"""
    @overload
    def precision_absolute(self) -> Any:
        """PowerSeries.precision_absolute(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 603)

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
        """PowerSeries.precision_absolute(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 603)

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
        """PowerSeries.precision_absolute(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 603)

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
        """PowerSeries.precision_relative(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 620)

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
        """PowerSeries.precision_relative(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 620)

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
        """PowerSeries.precision_relative(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 620)

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
        """PowerSeries.precision_relative(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 620)

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
    def shift(self, n) -> Any:
        """PowerSeries.shift(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1156)

        Return this power series multiplied by the power `t^n`.

        If `n` is negative, terms below `t^{-n}` are discarded.

        This power series is left unchanged.

        .. NOTE::

           Despite the fact that higher order terms are printed to the
           right in a power series, right shifting decreases the
           powers of `t`, while left shifting increases them.
           This is to be consistent with polynomials, integers, etc.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(QQ['y'], 't', 5)
            sage: f = ~(1+t); f
            1 - t + t^2 - t^3 + t^4 + O(t^5)
            sage: f.shift(3)
            t^3 - t^4 + t^5 - t^6 + t^7 + O(t^8)
            sage: f >> 2
            1 - t + t^2 + O(t^3)
            sage: f << 10
            t^10 - t^11 + t^12 - t^13 + t^14 + O(t^15)
            sage: t << 29
            t^30

        AUTHORS:

        - Robert Bradshaw (2007-04-18)"""
    @overload
    def sin(self, prec=...) -> Any:
        """PowerSeries.sin(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1995)

        Apply sin to the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT: a new power series

        EXAMPLES:

        For one variable::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: f = (t + t**2).O(4)
            sage: sin(f)
            t + t^2 - 1/6*t^3 + O(t^4)

        For several variables::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(3)
            sage: sin(f)
            a + b + a*b + O(a, b)^3
            sage: f.sin()
            a + b + a*b + O(a, b)^3
            sage: f.sin(prec=2)
            a + b + O(a, b)^2

        If the power series has a nonzero constant coefficient `c`,
        one raises an error::

            sage: g = 2+f
            sage: sin(g)
            Traceback (most recent call last):
            ...
            ValueError: can only apply sin to formal power series with zero constant term

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: sin(a)
            a - 1/6*a^3 + 1/120*a^5 - 1/5040*a^7 + 1/362880*a^9 - 1/39916800*a^11 + O(a, b)^12
            sage: a.sin(prec=5)
            a - 1/6*a^3 + O(a, b)^5
            sage: sin(a + T.O(5))
            a - 1/6*a^3 + O(a, b)^5

        TESTS::

            sage: sin(a^2 + T.O(5))
            a^2 + O(a, b)^5"""
    @overload
    def sin(self, f) -> Any:
        """PowerSeries.sin(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1995)

        Apply sin to the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT: a new power series

        EXAMPLES:

        For one variable::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: f = (t + t**2).O(4)
            sage: sin(f)
            t + t^2 - 1/6*t^3 + O(t^4)

        For several variables::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(3)
            sage: sin(f)
            a + b + a*b + O(a, b)^3
            sage: f.sin()
            a + b + a*b + O(a, b)^3
            sage: f.sin(prec=2)
            a + b + O(a, b)^2

        If the power series has a nonzero constant coefficient `c`,
        one raises an error::

            sage: g = 2+f
            sage: sin(g)
            Traceback (most recent call last):
            ...
            ValueError: can only apply sin to formal power series with zero constant term

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: sin(a)
            a - 1/6*a^3 + 1/120*a^5 - 1/5040*a^7 + 1/362880*a^9 - 1/39916800*a^11 + O(a, b)^12
            sage: a.sin(prec=5)
            a - 1/6*a^3 + O(a, b)^5
            sage: sin(a + T.O(5))
            a - 1/6*a^3 + O(a, b)^5

        TESTS::

            sage: sin(a^2 + T.O(5))
            a^2 + O(a, b)^5"""
    @overload
    def sin(self, f) -> Any:
        """PowerSeries.sin(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1995)

        Apply sin to the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT: a new power series

        EXAMPLES:

        For one variable::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: f = (t + t**2).O(4)
            sage: sin(f)
            t + t^2 - 1/6*t^3 + O(t^4)

        For several variables::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(3)
            sage: sin(f)
            a + b + a*b + O(a, b)^3
            sage: f.sin()
            a + b + a*b + O(a, b)^3
            sage: f.sin(prec=2)
            a + b + O(a, b)^2

        If the power series has a nonzero constant coefficient `c`,
        one raises an error::

            sage: g = 2+f
            sage: sin(g)
            Traceback (most recent call last):
            ...
            ValueError: can only apply sin to formal power series with zero constant term

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: sin(a)
            a - 1/6*a^3 + 1/120*a^5 - 1/5040*a^7 + 1/362880*a^9 - 1/39916800*a^11 + O(a, b)^12
            sage: a.sin(prec=5)
            a - 1/6*a^3 + O(a, b)^5
            sage: sin(a + T.O(5))
            a - 1/6*a^3 + O(a, b)^5

        TESTS::

            sage: sin(a^2 + T.O(5))
            a^2 + O(a, b)^5"""
    @overload
    def sin(self) -> Any:
        """PowerSeries.sin(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1995)

        Apply sin to the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT: a new power series

        EXAMPLES:

        For one variable::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: f = (t + t**2).O(4)
            sage: sin(f)
            t + t^2 - 1/6*t^3 + O(t^4)

        For several variables::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(3)
            sage: sin(f)
            a + b + a*b + O(a, b)^3
            sage: f.sin()
            a + b + a*b + O(a, b)^3
            sage: f.sin(prec=2)
            a + b + O(a, b)^2

        If the power series has a nonzero constant coefficient `c`,
        one raises an error::

            sage: g = 2+f
            sage: sin(g)
            Traceback (most recent call last):
            ...
            ValueError: can only apply sin to formal power series with zero constant term

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: sin(a)
            a - 1/6*a^3 + 1/120*a^5 - 1/5040*a^7 + 1/362880*a^9 - 1/39916800*a^11 + O(a, b)^12
            sage: a.sin(prec=5)
            a - 1/6*a^3 + O(a, b)^5
            sage: sin(a + T.O(5))
            a - 1/6*a^3 + O(a, b)^5

        TESTS::

            sage: sin(a^2 + T.O(5))
            a^2 + O(a, b)^5"""
    @overload
    def sin(self, prec=...) -> Any:
        """PowerSeries.sin(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1995)

        Apply sin to the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT: a new power series

        EXAMPLES:

        For one variable::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: f = (t + t**2).O(4)
            sage: sin(f)
            t + t^2 - 1/6*t^3 + O(t^4)

        For several variables::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(3)
            sage: sin(f)
            a + b + a*b + O(a, b)^3
            sage: f.sin()
            a + b + a*b + O(a, b)^3
            sage: f.sin(prec=2)
            a + b + O(a, b)^2

        If the power series has a nonzero constant coefficient `c`,
        one raises an error::

            sage: g = 2+f
            sage: sin(g)
            Traceback (most recent call last):
            ...
            ValueError: can only apply sin to formal power series with zero constant term

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: sin(a)
            a - 1/6*a^3 + 1/120*a^5 - 1/5040*a^7 + 1/362880*a^9 - 1/39916800*a^11 + O(a, b)^12
            sage: a.sin(prec=5)
            a - 1/6*a^3 + O(a, b)^5
            sage: sin(a + T.O(5))
            a - 1/6*a^3 + O(a, b)^5

        TESTS::

            sage: sin(a^2 + T.O(5))
            a^2 + O(a, b)^5"""
    @overload
    def sin(self, g) -> Any:
        """PowerSeries.sin(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1995)

        Apply sin to the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT: a new power series

        EXAMPLES:

        For one variable::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: f = (t + t**2).O(4)
            sage: sin(f)
            t + t^2 - 1/6*t^3 + O(t^4)

        For several variables::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(3)
            sage: sin(f)
            a + b + a*b + O(a, b)^3
            sage: f.sin()
            a + b + a*b + O(a, b)^3
            sage: f.sin(prec=2)
            a + b + O(a, b)^2

        If the power series has a nonzero constant coefficient `c`,
        one raises an error::

            sage: g = 2+f
            sage: sin(g)
            Traceback (most recent call last):
            ...
            ValueError: can only apply sin to formal power series with zero constant term

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: sin(a)
            a - 1/6*a^3 + 1/120*a^5 - 1/5040*a^7 + 1/362880*a^9 - 1/39916800*a^11 + O(a, b)^12
            sage: a.sin(prec=5)
            a - 1/6*a^3 + O(a, b)^5
            sage: sin(a + T.O(5))
            a - 1/6*a^3 + O(a, b)^5

        TESTS::

            sage: sin(a^2 + T.O(5))
            a^2 + O(a, b)^5"""
    @overload
    def sin(self, a) -> Any:
        """PowerSeries.sin(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1995)

        Apply sin to the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT: a new power series

        EXAMPLES:

        For one variable::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: f = (t + t**2).O(4)
            sage: sin(f)
            t + t^2 - 1/6*t^3 + O(t^4)

        For several variables::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(3)
            sage: sin(f)
            a + b + a*b + O(a, b)^3
            sage: f.sin()
            a + b + a*b + O(a, b)^3
            sage: f.sin(prec=2)
            a + b + O(a, b)^2

        If the power series has a nonzero constant coefficient `c`,
        one raises an error::

            sage: g = 2+f
            sage: sin(g)
            Traceback (most recent call last):
            ...
            ValueError: can only apply sin to formal power series with zero constant term

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: sin(a)
            a - 1/6*a^3 + 1/120*a^5 - 1/5040*a^7 + 1/362880*a^9 - 1/39916800*a^11 + O(a, b)^12
            sage: a.sin(prec=5)
            a - 1/6*a^3 + O(a, b)^5
            sage: sin(a + T.O(5))
            a - 1/6*a^3 + O(a, b)^5

        TESTS::

            sage: sin(a^2 + T.O(5))
            a^2 + O(a, b)^5"""
    @overload
    def sin(self, prec=...) -> Any:
        """PowerSeries.sin(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1995)

        Apply sin to the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT: a new power series

        EXAMPLES:

        For one variable::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: f = (t + t**2).O(4)
            sage: sin(f)
            t + t^2 - 1/6*t^3 + O(t^4)

        For several variables::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(3)
            sage: sin(f)
            a + b + a*b + O(a, b)^3
            sage: f.sin()
            a + b + a*b + O(a, b)^3
            sage: f.sin(prec=2)
            a + b + O(a, b)^2

        If the power series has a nonzero constant coefficient `c`,
        one raises an error::

            sage: g = 2+f
            sage: sin(g)
            Traceback (most recent call last):
            ...
            ValueError: can only apply sin to formal power series with zero constant term

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: sin(a)
            a - 1/6*a^3 + 1/120*a^5 - 1/5040*a^7 + 1/362880*a^9 - 1/39916800*a^11 + O(a, b)^12
            sage: a.sin(prec=5)
            a - 1/6*a^3 + O(a, b)^5
            sage: sin(a + T.O(5))
            a - 1/6*a^3 + O(a, b)^5

        TESTS::

            sage: sin(a^2 + T.O(5))
            a^2 + O(a, b)^5"""
    @overload
    def sinh(self, prec=...) -> Any:
        """PowerSeries.sinh(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2141)

        Apply sinh to the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT: a new power series

        EXAMPLES:

        For one variable::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: f = (t + t**2).O(4)
            sage: sinh(f)
            t + t^2 + 1/6*t^3 + O(t^4)

        For several variables::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(3)
            sage: sinh(f)
            a + b + a*b + O(a, b)^3
            sage: f.sinh()
            a + b + a*b + O(a, b)^3
            sage: f.sinh(prec=2)
            a + b + O(a, b)^2

        If the power series has a nonzero constant coefficient `c`,
        one raises an error::

            sage: g = 2 + f
            sage: sinh(g)
            Traceback (most recent call last):
            ...
            ValueError: can only apply sinh to formal power series with zero
            constant term

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: sinh(a)
            a + 1/6*a^3 + 1/120*a^5 + 1/5040*a^7 + 1/362880*a^9 +
             1/39916800*a^11 + O(a, b)^12
            sage: a.sinh(prec=5)
            a + 1/6*a^3 + O(a, b)^5
            sage: sinh(a + T.O(5))
            a + 1/6*a^3 + O(a, b)^5

        TESTS::

            sage: sinh(a^2 + T.O(5))
            a^2 + O(a, b)^5"""
    @overload
    def sinh(self, f) -> Any:
        """PowerSeries.sinh(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2141)

        Apply sinh to the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT: a new power series

        EXAMPLES:

        For one variable::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: f = (t + t**2).O(4)
            sage: sinh(f)
            t + t^2 + 1/6*t^3 + O(t^4)

        For several variables::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(3)
            sage: sinh(f)
            a + b + a*b + O(a, b)^3
            sage: f.sinh()
            a + b + a*b + O(a, b)^3
            sage: f.sinh(prec=2)
            a + b + O(a, b)^2

        If the power series has a nonzero constant coefficient `c`,
        one raises an error::

            sage: g = 2 + f
            sage: sinh(g)
            Traceback (most recent call last):
            ...
            ValueError: can only apply sinh to formal power series with zero
            constant term

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: sinh(a)
            a + 1/6*a^3 + 1/120*a^5 + 1/5040*a^7 + 1/362880*a^9 +
             1/39916800*a^11 + O(a, b)^12
            sage: a.sinh(prec=5)
            a + 1/6*a^3 + O(a, b)^5
            sage: sinh(a + T.O(5))
            a + 1/6*a^3 + O(a, b)^5

        TESTS::

            sage: sinh(a^2 + T.O(5))
            a^2 + O(a, b)^5"""
    @overload
    def sinh(self, f) -> Any:
        """PowerSeries.sinh(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2141)

        Apply sinh to the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT: a new power series

        EXAMPLES:

        For one variable::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: f = (t + t**2).O(4)
            sage: sinh(f)
            t + t^2 + 1/6*t^3 + O(t^4)

        For several variables::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(3)
            sage: sinh(f)
            a + b + a*b + O(a, b)^3
            sage: f.sinh()
            a + b + a*b + O(a, b)^3
            sage: f.sinh(prec=2)
            a + b + O(a, b)^2

        If the power series has a nonzero constant coefficient `c`,
        one raises an error::

            sage: g = 2 + f
            sage: sinh(g)
            Traceback (most recent call last):
            ...
            ValueError: can only apply sinh to formal power series with zero
            constant term

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: sinh(a)
            a + 1/6*a^3 + 1/120*a^5 + 1/5040*a^7 + 1/362880*a^9 +
             1/39916800*a^11 + O(a, b)^12
            sage: a.sinh(prec=5)
            a + 1/6*a^3 + O(a, b)^5
            sage: sinh(a + T.O(5))
            a + 1/6*a^3 + O(a, b)^5

        TESTS::

            sage: sinh(a^2 + T.O(5))
            a^2 + O(a, b)^5"""
    @overload
    def sinh(self) -> Any:
        """PowerSeries.sinh(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2141)

        Apply sinh to the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT: a new power series

        EXAMPLES:

        For one variable::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: f = (t + t**2).O(4)
            sage: sinh(f)
            t + t^2 + 1/6*t^3 + O(t^4)

        For several variables::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(3)
            sage: sinh(f)
            a + b + a*b + O(a, b)^3
            sage: f.sinh()
            a + b + a*b + O(a, b)^3
            sage: f.sinh(prec=2)
            a + b + O(a, b)^2

        If the power series has a nonzero constant coefficient `c`,
        one raises an error::

            sage: g = 2 + f
            sage: sinh(g)
            Traceback (most recent call last):
            ...
            ValueError: can only apply sinh to formal power series with zero
            constant term

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: sinh(a)
            a + 1/6*a^3 + 1/120*a^5 + 1/5040*a^7 + 1/362880*a^9 +
             1/39916800*a^11 + O(a, b)^12
            sage: a.sinh(prec=5)
            a + 1/6*a^3 + O(a, b)^5
            sage: sinh(a + T.O(5))
            a + 1/6*a^3 + O(a, b)^5

        TESTS::

            sage: sinh(a^2 + T.O(5))
            a^2 + O(a, b)^5"""
    @overload
    def sinh(self, prec=...) -> Any:
        """PowerSeries.sinh(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2141)

        Apply sinh to the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT: a new power series

        EXAMPLES:

        For one variable::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: f = (t + t**2).O(4)
            sage: sinh(f)
            t + t^2 + 1/6*t^3 + O(t^4)

        For several variables::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(3)
            sage: sinh(f)
            a + b + a*b + O(a, b)^3
            sage: f.sinh()
            a + b + a*b + O(a, b)^3
            sage: f.sinh(prec=2)
            a + b + O(a, b)^2

        If the power series has a nonzero constant coefficient `c`,
        one raises an error::

            sage: g = 2 + f
            sage: sinh(g)
            Traceback (most recent call last):
            ...
            ValueError: can only apply sinh to formal power series with zero
            constant term

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: sinh(a)
            a + 1/6*a^3 + 1/120*a^5 + 1/5040*a^7 + 1/362880*a^9 +
             1/39916800*a^11 + O(a, b)^12
            sage: a.sinh(prec=5)
            a + 1/6*a^3 + O(a, b)^5
            sage: sinh(a + T.O(5))
            a + 1/6*a^3 + O(a, b)^5

        TESTS::

            sage: sinh(a^2 + T.O(5))
            a^2 + O(a, b)^5"""
    @overload
    def sinh(self, g) -> Any:
        """PowerSeries.sinh(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2141)

        Apply sinh to the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT: a new power series

        EXAMPLES:

        For one variable::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: f = (t + t**2).O(4)
            sage: sinh(f)
            t + t^2 + 1/6*t^3 + O(t^4)

        For several variables::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(3)
            sage: sinh(f)
            a + b + a*b + O(a, b)^3
            sage: f.sinh()
            a + b + a*b + O(a, b)^3
            sage: f.sinh(prec=2)
            a + b + O(a, b)^2

        If the power series has a nonzero constant coefficient `c`,
        one raises an error::

            sage: g = 2 + f
            sage: sinh(g)
            Traceback (most recent call last):
            ...
            ValueError: can only apply sinh to formal power series with zero
            constant term

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: sinh(a)
            a + 1/6*a^3 + 1/120*a^5 + 1/5040*a^7 + 1/362880*a^9 +
             1/39916800*a^11 + O(a, b)^12
            sage: a.sinh(prec=5)
            a + 1/6*a^3 + O(a, b)^5
            sage: sinh(a + T.O(5))
            a + 1/6*a^3 + O(a, b)^5

        TESTS::

            sage: sinh(a^2 + T.O(5))
            a^2 + O(a, b)^5"""
    @overload
    def sinh(self, a) -> Any:
        """PowerSeries.sinh(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2141)

        Apply sinh to the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT: a new power series

        EXAMPLES:

        For one variable::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: f = (t + t**2).O(4)
            sage: sinh(f)
            t + t^2 + 1/6*t^3 + O(t^4)

        For several variables::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(3)
            sage: sinh(f)
            a + b + a*b + O(a, b)^3
            sage: f.sinh()
            a + b + a*b + O(a, b)^3
            sage: f.sinh(prec=2)
            a + b + O(a, b)^2

        If the power series has a nonzero constant coefficient `c`,
        one raises an error::

            sage: g = 2 + f
            sage: sinh(g)
            Traceback (most recent call last):
            ...
            ValueError: can only apply sinh to formal power series with zero
            constant term

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: sinh(a)
            a + 1/6*a^3 + 1/120*a^5 + 1/5040*a^7 + 1/362880*a^9 +
             1/39916800*a^11 + O(a, b)^12
            sage: a.sinh(prec=5)
            a + 1/6*a^3 + O(a, b)^5
            sage: sinh(a + T.O(5))
            a + 1/6*a^3 + O(a, b)^5

        TESTS::

            sage: sinh(a^2 + T.O(5))
            a^2 + O(a, b)^5"""
    @overload
    def sinh(self, prec=...) -> Any:
        """PowerSeries.sinh(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2141)

        Apply sinh to the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT: a new power series

        EXAMPLES:

        For one variable::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: f = (t + t**2).O(4)
            sage: sinh(f)
            t + t^2 + 1/6*t^3 + O(t^4)

        For several variables::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(3)
            sage: sinh(f)
            a + b + a*b + O(a, b)^3
            sage: f.sinh()
            a + b + a*b + O(a, b)^3
            sage: f.sinh(prec=2)
            a + b + O(a, b)^2

        If the power series has a nonzero constant coefficient `c`,
        one raises an error::

            sage: g = 2 + f
            sage: sinh(g)
            Traceback (most recent call last):
            ...
            ValueError: can only apply sinh to formal power series with zero
            constant term

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: sinh(a)
            a + 1/6*a^3 + 1/120*a^5 + 1/5040*a^7 + 1/362880*a^9 +
             1/39916800*a^11 + O(a, b)^12
            sage: a.sinh(prec=5)
            a + 1/6*a^3 + O(a, b)^5
            sage: sinh(a + T.O(5))
            a + 1/6*a^3 + O(a, b)^5

        TESTS::

            sage: sinh(a^2 + T.O(5))
            a^2 + O(a, b)^5"""
    def solve_linear_de(self, prec=..., b=..., f0=...) -> Any:
        '''PowerSeries.solve_linear_de(self, prec=infinity, b=None, f0=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2400)

        Obtain a power series solution to an inhomogeneous linear
        differential equation of the form:

        .. MATH::

              f\'(t) = a(t) f(t) + b(t).

        INPUT:

        - ``self`` -- the power series `a(t)`

        - ``b`` -- the power series `b(t)` (default: zero)

        - ``f0`` -- the constant term of `f` ("initial condition")
          (default: 1)

        - ``prec`` -- desired precision of result (this will be
          reduced if either a or b have less precision available)

        OUTPUT: the power series `f`, to indicated precision

        ALGORITHM: A divide-and-conquer strategy; see the source code.
        Running time is approximately `M(n) \\log n`, where
        `M(n)` is the time required for a polynomial multiplication
        of length `n` over the coefficient ring. (If you\'re working
        over something like `\\QQ`, running time analysis can be a
        little complicated because the coefficients tend to explode.)

        .. NOTE::

           - If the coefficient ring is a field of characteristic
             zero, then the solution will exist and is unique.

           - For other coefficient rings, things are more
             complicated. A solution may not exist, and if it does it
             may not be unique. Generally, by the time the `n`-th term
             has been computed, the algorithm will have attempted
             divisions by `n!` in the coefficient ring. So if
             your coefficient ring has enough \'precision\', and if your
             coefficient ring can perform divisions even when the
             answer is not unique, and if you know in advance that a
             solution exists, then this function will find a solution
             (otherwise it will probably crash).

        AUTHORS:

        - David Harvey (2006-09-11): factored functionality out from
          exp() function, cleaned up precision tests a bit

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(QQ, default_prec=10)

        ::

            sage: a = 2 - 3*t + 4*t^2 + O(t^10)
            sage: b = 3 - 4*t^2 + O(t^7)
            sage: f = a.solve_linear_de(prec=5, b=b, f0=3/5)
            sage: f
             3/5 + 21/5*t + 33/10*t^2 - 38/15*t^3 + 11/24*t^4 + O(t^5)
            sage: f.derivative() - a*f - b
             O(t^4)

        ::

            sage: a = 2 - 3*t + 4*t^2
            sage: b = b = 3 - 4*t^2
            sage: f = a.solve_linear_de(b=b, f0=3/5)
            Traceback (most recent call last):
            ...
            ValueError: cannot solve differential equation to infinite precision

        ::

            sage: a.solve_linear_de(prec=5, b=b, f0=3/5)
             3/5 + 21/5*t + 33/10*t^2 - 38/15*t^3 + 11/24*t^4 + O(t^5)'''
    def sqrt(self, prec=..., extend=..., all=..., name=...) -> Any:
        """PowerSeries.sqrt(self, prec=None, extend=False, all=False, name=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1586)

        Return a square root of ``self``.

        INPUT:

          - ``prec`` -- integer (default: ``None``); if not ``None`` and the
            series has infinite precision, truncates series at precision ``prec``

          - ``extend`` -- boolean (default: ``False``); if ``True``, return a
            square root in an extension ring, if necessary. Otherwise, raise
            a :exc:`ValueError` if the square root is not in the base power series
            ring. For example, if ``extend`` is ``True``, the square root of a
            power series with odd degree leading coefficient is
            defined as an element of a formal extension ring.

          - ``name`` -- string; if ``extend`` is ``True``, you must also
            specify the print name of the formal square root

          - ``all`` -- boolean (default: ``False``); if ``True``, return all
            square roots of ``self``, instead of just one

        ALGORITHM: Newton's method

        .. MATH::

           x_{i+1} = \\frac{1}{2}( x_i + \\mathrm{self}/x_i )

        EXAMPLES::

            sage: K.<t> = PowerSeriesRing(QQ, 't', 5)
            sage: sqrt(t^2)
            t
            sage: sqrt(1 + t)
            1 + 1/2*t - 1/8*t^2 + 1/16*t^3 - 5/128*t^4 + O(t^5)
            sage: sqrt(4 + t)
            2 + 1/4*t - 1/64*t^2 + 1/512*t^3 - 5/16384*t^4 + O(t^5)
            sage: u = sqrt(2 + t, prec=2, extend=True, name = 'alpha'); u
            alpha
            sage: u^2
            2 + t
            sage: u.parent()
            Univariate Quotient Polynomial Ring in alpha
             over Power Series Ring in t over Rational Field
             with modulus x^2 - 2 - t
            sage: K.<t> = PowerSeriesRing(QQ, 't', 50)
            sage: sqrt(1 + 2*t + t^2)
            1 + t
            sage: sqrt(t^2 + 2*t^4 + t^6)
            t + t^3
            sage: sqrt(1 + t + t^2 + 7*t^3)^2
            1 + t + t^2 + 7*t^3 + O(t^50)
            sage: sqrt(K(0))
            0
            sage: sqrt(t^2)
            t

        ::

            sage: # needs sage.rings.complex_double
            sage: K.<t> = PowerSeriesRing(CDF, 5)
            sage: v = sqrt(-1 + t + t^3, all=True); v
            [1.0*I - 0.5*I*t - 0.125*I*t^2 - 0.5625*I*t^3 - 0.2890625*I*t^4 + O(t^5),
             -1.0*I + 0.5*I*t + 0.125*I*t^2 + 0.5625*I*t^3 + 0.2890625*I*t^4 + O(t^5)]
            sage: [a^2 for a in v]
            [-1.0 + 1.0*t + 0.0*t^2 + 1.0*t^3 + O(t^5), -1.0 + 1.0*t + 0.0*t^2 + 1.0*t^3 + O(t^5)]

        A formal square root::

            sage: K.<t> = PowerSeriesRing(QQ, 5)
            sage: f = 2*t + t^3 + O(t^4)
            sage: s = f.sqrt(extend=True, name='sqrtf'); s
            sqrtf
            sage: s^2
            2*t + t^3 + O(t^4)
            sage: parent(s)
            Univariate Quotient Polynomial Ring in sqrtf
             over Power Series Ring in t over Rational Field
             with modulus x^2 - 2*t - t^3 + O(t^4)

        TESTS::

            sage: R.<x> = QQ[[]]
            sage: (x^10/2).sqrt()
            Traceback (most recent call last):
            ...
            ValueError: unable to take the square root of 1/2

        Check :issue:`30655`::

            sage: t = polygen(QQ, 't')
            sage: x = t.parent()[['x']].0
            sage: W = (t*x + 1 - x).O(3)
            sage: W.sqrt()
            1 + (1/2*t - 1/2)*x + (-1/8*t^2 + 1/4*t - 1/8)*x^2 + O(x^3)

        AUTHORS:

        - Robert Bradshaw

        - William Stein"""
    @overload
    def square_root(self) -> Any:
        """PowerSeries.square_root(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1771)

        Return the square root of ``self`` in this ring. If this cannot be done,
        then an error will be raised.

        This function succeeds if and only if
        ``self``. :meth:`.is_square`

        EXAMPLES::

            sage: K.<t> = PowerSeriesRing(QQ, 't', 5)
            sage: (1 + t).square_root()
            1 + 1/2*t - 1/8*t^2 + 1/16*t^3 - 5/128*t^4 + O(t^5)
            sage: (2 + t).square_root()
            Traceback (most recent call last):
            ...
            ValueError: Square root does not live in this ring.
            sage: (2 + t.change_ring(RR)).square_root()                                 # needs sage.rings.real_mpfr
            1.41421356237309 + 0.353553390593274*t - 0.0441941738241592*t^2
             + 0.0110485434560398*t^3 - 0.00345266983001244*t^4 + O(t^5)
            sage: t.square_root()
            Traceback (most recent call last):
            ...
            ValueError: Square root not defined for power series of odd valuation.
            sage: K.<t> = PowerSeriesRing(ZZ, 't', 5)
            sage: f = (1+t)^20
            sage: f.square_root()
            1 + 10*t + 45*t^2 + 120*t^3 + 210*t^4 + O(t^5)
            sage: f = 1 + t
            sage: f.square_root()
            Traceback (most recent call last):
            ...
            ValueError: Square root does not live in this ring.

        AUTHORS:

        - Robert Bradshaw"""
    @overload
    def square_root(self) -> Any:
        """PowerSeries.square_root(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1771)

        Return the square root of ``self`` in this ring. If this cannot be done,
        then an error will be raised.

        This function succeeds if and only if
        ``self``. :meth:`.is_square`

        EXAMPLES::

            sage: K.<t> = PowerSeriesRing(QQ, 't', 5)
            sage: (1 + t).square_root()
            1 + 1/2*t - 1/8*t^2 + 1/16*t^3 - 5/128*t^4 + O(t^5)
            sage: (2 + t).square_root()
            Traceback (most recent call last):
            ...
            ValueError: Square root does not live in this ring.
            sage: (2 + t.change_ring(RR)).square_root()                                 # needs sage.rings.real_mpfr
            1.41421356237309 + 0.353553390593274*t - 0.0441941738241592*t^2
             + 0.0110485434560398*t^3 - 0.00345266983001244*t^4 + O(t^5)
            sage: t.square_root()
            Traceback (most recent call last):
            ...
            ValueError: Square root not defined for power series of odd valuation.
            sage: K.<t> = PowerSeriesRing(ZZ, 't', 5)
            sage: f = (1+t)^20
            sage: f.square_root()
            1 + 10*t + 45*t^2 + 120*t^3 + 210*t^4 + O(t^5)
            sage: f = 1 + t
            sage: f.square_root()
            Traceback (most recent call last):
            ...
            ValueError: Square root does not live in this ring.

        AUTHORS:

        - Robert Bradshaw"""
    @overload
    def square_root(self) -> Any:
        """PowerSeries.square_root(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1771)

        Return the square root of ``self`` in this ring. If this cannot be done,
        then an error will be raised.

        This function succeeds if and only if
        ``self``. :meth:`.is_square`

        EXAMPLES::

            sage: K.<t> = PowerSeriesRing(QQ, 't', 5)
            sage: (1 + t).square_root()
            1 + 1/2*t - 1/8*t^2 + 1/16*t^3 - 5/128*t^4 + O(t^5)
            sage: (2 + t).square_root()
            Traceback (most recent call last):
            ...
            ValueError: Square root does not live in this ring.
            sage: (2 + t.change_ring(RR)).square_root()                                 # needs sage.rings.real_mpfr
            1.41421356237309 + 0.353553390593274*t - 0.0441941738241592*t^2
             + 0.0110485434560398*t^3 - 0.00345266983001244*t^4 + O(t^5)
            sage: t.square_root()
            Traceback (most recent call last):
            ...
            ValueError: Square root not defined for power series of odd valuation.
            sage: K.<t> = PowerSeriesRing(ZZ, 't', 5)
            sage: f = (1+t)^20
            sage: f.square_root()
            1 + 10*t + 45*t^2 + 120*t^3 + 210*t^4 + O(t^5)
            sage: f = 1 + t
            sage: f.square_root()
            Traceback (most recent call last):
            ...
            ValueError: Square root does not live in this ring.

        AUTHORS:

        - Robert Bradshaw"""
    @overload
    def square_root(self) -> Any:
        """PowerSeries.square_root(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1771)

        Return the square root of ``self`` in this ring. If this cannot be done,
        then an error will be raised.

        This function succeeds if and only if
        ``self``. :meth:`.is_square`

        EXAMPLES::

            sage: K.<t> = PowerSeriesRing(QQ, 't', 5)
            sage: (1 + t).square_root()
            1 + 1/2*t - 1/8*t^2 + 1/16*t^3 - 5/128*t^4 + O(t^5)
            sage: (2 + t).square_root()
            Traceback (most recent call last):
            ...
            ValueError: Square root does not live in this ring.
            sage: (2 + t.change_ring(RR)).square_root()                                 # needs sage.rings.real_mpfr
            1.41421356237309 + 0.353553390593274*t - 0.0441941738241592*t^2
             + 0.0110485434560398*t^3 - 0.00345266983001244*t^4 + O(t^5)
            sage: t.square_root()
            Traceback (most recent call last):
            ...
            ValueError: Square root not defined for power series of odd valuation.
            sage: K.<t> = PowerSeriesRing(ZZ, 't', 5)
            sage: f = (1+t)^20
            sage: f.square_root()
            1 + 10*t + 45*t^2 + 120*t^3 + 210*t^4 + O(t^5)
            sage: f = 1 + t
            sage: f.square_root()
            Traceback (most recent call last):
            ...
            ValueError: Square root does not live in this ring.

        AUTHORS:

        - Robert Bradshaw"""
    @overload
    def square_root(self) -> Any:
        """PowerSeries.square_root(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1771)

        Return the square root of ``self`` in this ring. If this cannot be done,
        then an error will be raised.

        This function succeeds if and only if
        ``self``. :meth:`.is_square`

        EXAMPLES::

            sage: K.<t> = PowerSeriesRing(QQ, 't', 5)
            sage: (1 + t).square_root()
            1 + 1/2*t - 1/8*t^2 + 1/16*t^3 - 5/128*t^4 + O(t^5)
            sage: (2 + t).square_root()
            Traceback (most recent call last):
            ...
            ValueError: Square root does not live in this ring.
            sage: (2 + t.change_ring(RR)).square_root()                                 # needs sage.rings.real_mpfr
            1.41421356237309 + 0.353553390593274*t - 0.0441941738241592*t^2
             + 0.0110485434560398*t^3 - 0.00345266983001244*t^4 + O(t^5)
            sage: t.square_root()
            Traceback (most recent call last):
            ...
            ValueError: Square root not defined for power series of odd valuation.
            sage: K.<t> = PowerSeriesRing(ZZ, 't', 5)
            sage: f = (1+t)^20
            sage: f.square_root()
            1 + 10*t + 45*t^2 + 120*t^3 + 210*t^4 + O(t^5)
            sage: f = 1 + t
            sage: f.square_root()
            Traceback (most recent call last):
            ...
            ValueError: Square root does not live in this ring.

        AUTHORS:

        - Robert Bradshaw"""
    @overload
    def square_root(self) -> Any:
        """PowerSeries.square_root(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1771)

        Return the square root of ``self`` in this ring. If this cannot be done,
        then an error will be raised.

        This function succeeds if and only if
        ``self``. :meth:`.is_square`

        EXAMPLES::

            sage: K.<t> = PowerSeriesRing(QQ, 't', 5)
            sage: (1 + t).square_root()
            1 + 1/2*t - 1/8*t^2 + 1/16*t^3 - 5/128*t^4 + O(t^5)
            sage: (2 + t).square_root()
            Traceback (most recent call last):
            ...
            ValueError: Square root does not live in this ring.
            sage: (2 + t.change_ring(RR)).square_root()                                 # needs sage.rings.real_mpfr
            1.41421356237309 + 0.353553390593274*t - 0.0441941738241592*t^2
             + 0.0110485434560398*t^3 - 0.00345266983001244*t^4 + O(t^5)
            sage: t.square_root()
            Traceback (most recent call last):
            ...
            ValueError: Square root not defined for power series of odd valuation.
            sage: K.<t> = PowerSeriesRing(ZZ, 't', 5)
            sage: f = (1+t)^20
            sage: f.square_root()
            1 + 10*t + 45*t^2 + 120*t^3 + 210*t^4 + O(t^5)
            sage: f = 1 + t
            sage: f.square_root()
            Traceback (most recent call last):
            ...
            ValueError: Square root does not live in this ring.

        AUTHORS:

        - Robert Bradshaw"""
    @overload
    def square_root(self) -> Any:
        """PowerSeries.square_root(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1771)

        Return the square root of ``self`` in this ring. If this cannot be done,
        then an error will be raised.

        This function succeeds if and only if
        ``self``. :meth:`.is_square`

        EXAMPLES::

            sage: K.<t> = PowerSeriesRing(QQ, 't', 5)
            sage: (1 + t).square_root()
            1 + 1/2*t - 1/8*t^2 + 1/16*t^3 - 5/128*t^4 + O(t^5)
            sage: (2 + t).square_root()
            Traceback (most recent call last):
            ...
            ValueError: Square root does not live in this ring.
            sage: (2 + t.change_ring(RR)).square_root()                                 # needs sage.rings.real_mpfr
            1.41421356237309 + 0.353553390593274*t - 0.0441941738241592*t^2
             + 0.0110485434560398*t^3 - 0.00345266983001244*t^4 + O(t^5)
            sage: t.square_root()
            Traceback (most recent call last):
            ...
            ValueError: Square root not defined for power series of odd valuation.
            sage: K.<t> = PowerSeriesRing(ZZ, 't', 5)
            sage: f = (1+t)^20
            sage: f.square_root()
            1 + 10*t + 45*t^2 + 120*t^3 + 210*t^4 + O(t^5)
            sage: f = 1 + t
            sage: f.square_root()
            Traceback (most recent call last):
            ...
            ValueError: Square root does not live in this ring.

        AUTHORS:

        - Robert Bradshaw"""
    def stieltjes_continued_fraction(self) -> Any:
        """PowerSeries.stieltjes_continued_fraction(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1467)

        Return the Stieltjes continued fraction of ``self``.

        The S-fraction or Stieltjes continued fraction of a power series
        is a continued fraction expansion with steps of size one. We use
        the following convention

        .. MATH::

            1 / (1 - A_1 t / (1 - A_2 t / (1 - A_3 t / (1 - \\cdots))))

        OUTPUT: `A_n` for `n \\geq 1`

        The expansion is done as long as possible given the precision.
        Whenever the expansion is not well-defined, because it would
        require to divide by zero, an exception is raised.

        EXAMPLES::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: s = sum(catalan_number(k) * t**k for k in range(12)).O(12)
            sage: s.stieltjes_continued_fraction()
            (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)

        Another example::

            sage: (exp(t)).stieltjes_continued_fraction()
            (1,
             -1/2,
             1/6,
             -1/6,
             1/10,
             -1/10,
             1/14,
             -1/14,
             1/18,
             -1/18,
             1/22,
             -1/22,
             1/26,
             -1/26,
             1/30,
             -1/30,
             1/34,
             -1/34,
             1/38)

        TESTS::

             sage: (t).stieltjes_continued_fraction()
             Traceback (most recent call last):
             ...
             ValueError: vanishing constant term, no expansion
             sage: (1/(1+3*t)).stieltjes_continued_fraction()
             Traceback (most recent call last):
             ...
             ValueError: vanishing term, no further expansion"""
    def super_delta_fraction(self, delta) -> Any:
        """PowerSeries.super_delta_fraction(self, delta)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1387)

        Return the super delta continued fraction of ``self``.

        This is a continued fraction of the following shape:

        .. MATH::

            \\cfrac{v_0 x^{k_0}} {U_1(x) -
            \\cfrac{v_1 x^{k_0 + k_1 + \\delta}} {U_2(x) -
            \\cfrac{v_2 x^{k_0 + k_1 + k_2 + \\delta}} {U_3(x) - \\cdots} } }

        where each `U_j(x) = 1 + u_j(x) x`.

        INPUT:

        - ``delta`` -- positive integer, usually 2

        OUTPUT: list of `(v_j, k_j, U_{j+1}(x))_{j \\geq 0}`

        REFERENCES:

        - [Han2016]_

        EXAMPLES::

            sage: deg = 30
            sage: PS = PowerSeriesRing(QQ, 'q', default_prec=deg+1)
            sage: q = PS.gen()
            sage: F = prod([(1+q**k).add_bigoh(deg+1) for k in range(1,deg)])
            sage: F.super_delta_fraction(2)
            [(1, 0, -q + 1),
             (1, 1, q + 1),
             (-1, 2, -q^3 + q^2 - q + 1),
             (1, 1, q^2 + q + 1),
             (-1, 0, -q + 1),
             (-1, 1, q^2 + q + 1),
             (-1, 0, -q + 1),
             (1, 1, 3*q^2 + 2*q + 1),
             (-4, 0, -q + 1)]

        A Jacobi continued fraction::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: s = sum(factorial(k) * t**k for k in range(12)).O(12)
            sage: s.super_delta_fraction(2)
            [(1, 0, -t + 1),
            (1, 0, -3*t + 1),
            (4, 0, -5*t + 1),
            (9, 0, -7*t + 1),
            (16, 0, -9*t + 1),
            (25, 0, -11*t + 1)]"""
    @overload
    def tan(self, prec=...) -> Any:
        """PowerSeries.tan(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2079)

        Apply tan to the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT: a new power series

        EXAMPLES:

        For one variable::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: f = (t + t**2).O(4)
            sage: tan(f)
            t + t^2 + 1/3*t^3 + O(t^4)

        For several variables::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(3)
            sage: tan(f)
            a + b + a*b + O(a, b)^3
            sage: f.tan()
            a + b + a*b + O(a, b)^3
            sage: f.tan(prec=2)
            a + b + O(a, b)^2

        If the power series has a nonzero constant coefficient `c`,
        one raises an error::

            sage: g = 2 + f
            sage: tan(g)
            Traceback (most recent call last):
            ...
            ValueError: can only apply tan to formal power series with zero constant term

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: tan(a)
            a + 1/3*a^3 + 2/15*a^5 + 17/315*a^7 + 62/2835*a^9 + 1382/155925*a^11 + O(a, b)^12
            sage: a.tan(prec=5)
            a + 1/3*a^3 + O(a, b)^5
            sage: tan(a + T.O(5))
            a + 1/3*a^3 + O(a, b)^5

        TESTS::

            sage: tan(a^2 + T.O(5))
            a^2 + O(a, b)^5"""
    @overload
    def tan(self, f) -> Any:
        """PowerSeries.tan(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2079)

        Apply tan to the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT: a new power series

        EXAMPLES:

        For one variable::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: f = (t + t**2).O(4)
            sage: tan(f)
            t + t^2 + 1/3*t^3 + O(t^4)

        For several variables::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(3)
            sage: tan(f)
            a + b + a*b + O(a, b)^3
            sage: f.tan()
            a + b + a*b + O(a, b)^3
            sage: f.tan(prec=2)
            a + b + O(a, b)^2

        If the power series has a nonzero constant coefficient `c`,
        one raises an error::

            sage: g = 2 + f
            sage: tan(g)
            Traceback (most recent call last):
            ...
            ValueError: can only apply tan to formal power series with zero constant term

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: tan(a)
            a + 1/3*a^3 + 2/15*a^5 + 17/315*a^7 + 62/2835*a^9 + 1382/155925*a^11 + O(a, b)^12
            sage: a.tan(prec=5)
            a + 1/3*a^3 + O(a, b)^5
            sage: tan(a + T.O(5))
            a + 1/3*a^3 + O(a, b)^5

        TESTS::

            sage: tan(a^2 + T.O(5))
            a^2 + O(a, b)^5"""
    @overload
    def tan(self, f) -> Any:
        """PowerSeries.tan(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2079)

        Apply tan to the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT: a new power series

        EXAMPLES:

        For one variable::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: f = (t + t**2).O(4)
            sage: tan(f)
            t + t^2 + 1/3*t^3 + O(t^4)

        For several variables::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(3)
            sage: tan(f)
            a + b + a*b + O(a, b)^3
            sage: f.tan()
            a + b + a*b + O(a, b)^3
            sage: f.tan(prec=2)
            a + b + O(a, b)^2

        If the power series has a nonzero constant coefficient `c`,
        one raises an error::

            sage: g = 2 + f
            sage: tan(g)
            Traceback (most recent call last):
            ...
            ValueError: can only apply tan to formal power series with zero constant term

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: tan(a)
            a + 1/3*a^3 + 2/15*a^5 + 17/315*a^7 + 62/2835*a^9 + 1382/155925*a^11 + O(a, b)^12
            sage: a.tan(prec=5)
            a + 1/3*a^3 + O(a, b)^5
            sage: tan(a + T.O(5))
            a + 1/3*a^3 + O(a, b)^5

        TESTS::

            sage: tan(a^2 + T.O(5))
            a^2 + O(a, b)^5"""
    @overload
    def tan(self) -> Any:
        """PowerSeries.tan(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2079)

        Apply tan to the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT: a new power series

        EXAMPLES:

        For one variable::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: f = (t + t**2).O(4)
            sage: tan(f)
            t + t^2 + 1/3*t^3 + O(t^4)

        For several variables::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(3)
            sage: tan(f)
            a + b + a*b + O(a, b)^3
            sage: f.tan()
            a + b + a*b + O(a, b)^3
            sage: f.tan(prec=2)
            a + b + O(a, b)^2

        If the power series has a nonzero constant coefficient `c`,
        one raises an error::

            sage: g = 2 + f
            sage: tan(g)
            Traceback (most recent call last):
            ...
            ValueError: can only apply tan to formal power series with zero constant term

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: tan(a)
            a + 1/3*a^3 + 2/15*a^5 + 17/315*a^7 + 62/2835*a^9 + 1382/155925*a^11 + O(a, b)^12
            sage: a.tan(prec=5)
            a + 1/3*a^3 + O(a, b)^5
            sage: tan(a + T.O(5))
            a + 1/3*a^3 + O(a, b)^5

        TESTS::

            sage: tan(a^2 + T.O(5))
            a^2 + O(a, b)^5"""
    @overload
    def tan(self, prec=...) -> Any:
        """PowerSeries.tan(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2079)

        Apply tan to the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT: a new power series

        EXAMPLES:

        For one variable::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: f = (t + t**2).O(4)
            sage: tan(f)
            t + t^2 + 1/3*t^3 + O(t^4)

        For several variables::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(3)
            sage: tan(f)
            a + b + a*b + O(a, b)^3
            sage: f.tan()
            a + b + a*b + O(a, b)^3
            sage: f.tan(prec=2)
            a + b + O(a, b)^2

        If the power series has a nonzero constant coefficient `c`,
        one raises an error::

            sage: g = 2 + f
            sage: tan(g)
            Traceback (most recent call last):
            ...
            ValueError: can only apply tan to formal power series with zero constant term

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: tan(a)
            a + 1/3*a^3 + 2/15*a^5 + 17/315*a^7 + 62/2835*a^9 + 1382/155925*a^11 + O(a, b)^12
            sage: a.tan(prec=5)
            a + 1/3*a^3 + O(a, b)^5
            sage: tan(a + T.O(5))
            a + 1/3*a^3 + O(a, b)^5

        TESTS::

            sage: tan(a^2 + T.O(5))
            a^2 + O(a, b)^5"""
    @overload
    def tan(self, g) -> Any:
        """PowerSeries.tan(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2079)

        Apply tan to the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT: a new power series

        EXAMPLES:

        For one variable::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: f = (t + t**2).O(4)
            sage: tan(f)
            t + t^2 + 1/3*t^3 + O(t^4)

        For several variables::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(3)
            sage: tan(f)
            a + b + a*b + O(a, b)^3
            sage: f.tan()
            a + b + a*b + O(a, b)^3
            sage: f.tan(prec=2)
            a + b + O(a, b)^2

        If the power series has a nonzero constant coefficient `c`,
        one raises an error::

            sage: g = 2 + f
            sage: tan(g)
            Traceback (most recent call last):
            ...
            ValueError: can only apply tan to formal power series with zero constant term

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: tan(a)
            a + 1/3*a^3 + 2/15*a^5 + 17/315*a^7 + 62/2835*a^9 + 1382/155925*a^11 + O(a, b)^12
            sage: a.tan(prec=5)
            a + 1/3*a^3 + O(a, b)^5
            sage: tan(a + T.O(5))
            a + 1/3*a^3 + O(a, b)^5

        TESTS::

            sage: tan(a^2 + T.O(5))
            a^2 + O(a, b)^5"""
    @overload
    def tan(self, a) -> Any:
        """PowerSeries.tan(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2079)

        Apply tan to the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT: a new power series

        EXAMPLES:

        For one variable::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: f = (t + t**2).O(4)
            sage: tan(f)
            t + t^2 + 1/3*t^3 + O(t^4)

        For several variables::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(3)
            sage: tan(f)
            a + b + a*b + O(a, b)^3
            sage: f.tan()
            a + b + a*b + O(a, b)^3
            sage: f.tan(prec=2)
            a + b + O(a, b)^2

        If the power series has a nonzero constant coefficient `c`,
        one raises an error::

            sage: g = 2 + f
            sage: tan(g)
            Traceback (most recent call last):
            ...
            ValueError: can only apply tan to formal power series with zero constant term

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: tan(a)
            a + 1/3*a^3 + 2/15*a^5 + 17/315*a^7 + 62/2835*a^9 + 1382/155925*a^11 + O(a, b)^12
            sage: a.tan(prec=5)
            a + 1/3*a^3 + O(a, b)^5
            sage: tan(a + T.O(5))
            a + 1/3*a^3 + O(a, b)^5

        TESTS::

            sage: tan(a^2 + T.O(5))
            a^2 + O(a, b)^5"""
    @overload
    def tan(self, prec=...) -> Any:
        """PowerSeries.tan(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2079)

        Apply tan to the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT: a new power series

        EXAMPLES:

        For one variable::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: f = (t + t**2).O(4)
            sage: tan(f)
            t + t^2 + 1/3*t^3 + O(t^4)

        For several variables::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(3)
            sage: tan(f)
            a + b + a*b + O(a, b)^3
            sage: f.tan()
            a + b + a*b + O(a, b)^3
            sage: f.tan(prec=2)
            a + b + O(a, b)^2

        If the power series has a nonzero constant coefficient `c`,
        one raises an error::

            sage: g = 2 + f
            sage: tan(g)
            Traceback (most recent call last):
            ...
            ValueError: can only apply tan to formal power series with zero constant term

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: tan(a)
            a + 1/3*a^3 + 2/15*a^5 + 17/315*a^7 + 62/2835*a^9 + 1382/155925*a^11 + O(a, b)^12
            sage: a.tan(prec=5)
            a + 1/3*a^3 + O(a, b)^5
            sage: tan(a + T.O(5))
            a + 1/3*a^3 + O(a, b)^5

        TESTS::

            sage: tan(a^2 + T.O(5))
            a^2 + O(a, b)^5"""
    @overload
    def tanh(self, prec=...) -> Any:
        """PowerSeries.tanh(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2312)

        Apply tanh to the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT: a new power series

        EXAMPLES:

        For one variable::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: f = (t + t**2).O(4)
            sage: tanh(f)
            t + t^2 - 1/3*t^3 + O(t^4)

        For several variables::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(3)
            sage: tanh(f)
            a + b + a*b + O(a, b)^3
            sage: f.tanh()
            a + b + a*b + O(a, b)^3
            sage: f.tanh(prec=2)
            a + b + O(a, b)^2

        If the power series has a nonzero constant coefficient `c`,
        one raises an error::

            sage: g = 2 + f
            sage: tanh(g)
            Traceback (most recent call last):
            ...
            ValueError: can only apply tanh to formal power series with zero
             constant term

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: tanh(a)
            a - 1/3*a^3 + 2/15*a^5 - 17/315*a^7 + 62/2835*a^9 -
            1382/155925*a^11 + O(a, b)^12
            sage: a.tanh(prec=5)
            a - 1/3*a^3 + O(a, b)^5
            sage: tanh(a + T.O(5))
            a - 1/3*a^3 + O(a, b)^5

        TESTS::

            sage: tanh(a^2 + T.O(5))
            a^2 + O(a, b)^5"""
    @overload
    def tanh(self, f) -> Any:
        """PowerSeries.tanh(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2312)

        Apply tanh to the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT: a new power series

        EXAMPLES:

        For one variable::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: f = (t + t**2).O(4)
            sage: tanh(f)
            t + t^2 - 1/3*t^3 + O(t^4)

        For several variables::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(3)
            sage: tanh(f)
            a + b + a*b + O(a, b)^3
            sage: f.tanh()
            a + b + a*b + O(a, b)^3
            sage: f.tanh(prec=2)
            a + b + O(a, b)^2

        If the power series has a nonzero constant coefficient `c`,
        one raises an error::

            sage: g = 2 + f
            sage: tanh(g)
            Traceback (most recent call last):
            ...
            ValueError: can only apply tanh to formal power series with zero
             constant term

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: tanh(a)
            a - 1/3*a^3 + 2/15*a^5 - 17/315*a^7 + 62/2835*a^9 -
            1382/155925*a^11 + O(a, b)^12
            sage: a.tanh(prec=5)
            a - 1/3*a^3 + O(a, b)^5
            sage: tanh(a + T.O(5))
            a - 1/3*a^3 + O(a, b)^5

        TESTS::

            sage: tanh(a^2 + T.O(5))
            a^2 + O(a, b)^5"""
    @overload
    def tanh(self, f) -> Any:
        """PowerSeries.tanh(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2312)

        Apply tanh to the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT: a new power series

        EXAMPLES:

        For one variable::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: f = (t + t**2).O(4)
            sage: tanh(f)
            t + t^2 - 1/3*t^3 + O(t^4)

        For several variables::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(3)
            sage: tanh(f)
            a + b + a*b + O(a, b)^3
            sage: f.tanh()
            a + b + a*b + O(a, b)^3
            sage: f.tanh(prec=2)
            a + b + O(a, b)^2

        If the power series has a nonzero constant coefficient `c`,
        one raises an error::

            sage: g = 2 + f
            sage: tanh(g)
            Traceback (most recent call last):
            ...
            ValueError: can only apply tanh to formal power series with zero
             constant term

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: tanh(a)
            a - 1/3*a^3 + 2/15*a^5 - 17/315*a^7 + 62/2835*a^9 -
            1382/155925*a^11 + O(a, b)^12
            sage: a.tanh(prec=5)
            a - 1/3*a^3 + O(a, b)^5
            sage: tanh(a + T.O(5))
            a - 1/3*a^3 + O(a, b)^5

        TESTS::

            sage: tanh(a^2 + T.O(5))
            a^2 + O(a, b)^5"""
    @overload
    def tanh(self) -> Any:
        """PowerSeries.tanh(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2312)

        Apply tanh to the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT: a new power series

        EXAMPLES:

        For one variable::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: f = (t + t**2).O(4)
            sage: tanh(f)
            t + t^2 - 1/3*t^3 + O(t^4)

        For several variables::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(3)
            sage: tanh(f)
            a + b + a*b + O(a, b)^3
            sage: f.tanh()
            a + b + a*b + O(a, b)^3
            sage: f.tanh(prec=2)
            a + b + O(a, b)^2

        If the power series has a nonzero constant coefficient `c`,
        one raises an error::

            sage: g = 2 + f
            sage: tanh(g)
            Traceback (most recent call last):
            ...
            ValueError: can only apply tanh to formal power series with zero
             constant term

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: tanh(a)
            a - 1/3*a^3 + 2/15*a^5 - 17/315*a^7 + 62/2835*a^9 -
            1382/155925*a^11 + O(a, b)^12
            sage: a.tanh(prec=5)
            a - 1/3*a^3 + O(a, b)^5
            sage: tanh(a + T.O(5))
            a - 1/3*a^3 + O(a, b)^5

        TESTS::

            sage: tanh(a^2 + T.O(5))
            a^2 + O(a, b)^5"""
    @overload
    def tanh(self, prec=...) -> Any:
        """PowerSeries.tanh(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2312)

        Apply tanh to the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT: a new power series

        EXAMPLES:

        For one variable::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: f = (t + t**2).O(4)
            sage: tanh(f)
            t + t^2 - 1/3*t^3 + O(t^4)

        For several variables::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(3)
            sage: tanh(f)
            a + b + a*b + O(a, b)^3
            sage: f.tanh()
            a + b + a*b + O(a, b)^3
            sage: f.tanh(prec=2)
            a + b + O(a, b)^2

        If the power series has a nonzero constant coefficient `c`,
        one raises an error::

            sage: g = 2 + f
            sage: tanh(g)
            Traceback (most recent call last):
            ...
            ValueError: can only apply tanh to formal power series with zero
             constant term

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: tanh(a)
            a - 1/3*a^3 + 2/15*a^5 - 17/315*a^7 + 62/2835*a^9 -
            1382/155925*a^11 + O(a, b)^12
            sage: a.tanh(prec=5)
            a - 1/3*a^3 + O(a, b)^5
            sage: tanh(a + T.O(5))
            a - 1/3*a^3 + O(a, b)^5

        TESTS::

            sage: tanh(a^2 + T.O(5))
            a^2 + O(a, b)^5"""
    @overload
    def tanh(self, g) -> Any:
        """PowerSeries.tanh(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2312)

        Apply tanh to the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT: a new power series

        EXAMPLES:

        For one variable::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: f = (t + t**2).O(4)
            sage: tanh(f)
            t + t^2 - 1/3*t^3 + O(t^4)

        For several variables::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(3)
            sage: tanh(f)
            a + b + a*b + O(a, b)^3
            sage: f.tanh()
            a + b + a*b + O(a, b)^3
            sage: f.tanh(prec=2)
            a + b + O(a, b)^2

        If the power series has a nonzero constant coefficient `c`,
        one raises an error::

            sage: g = 2 + f
            sage: tanh(g)
            Traceback (most recent call last):
            ...
            ValueError: can only apply tanh to formal power series with zero
             constant term

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: tanh(a)
            a - 1/3*a^3 + 2/15*a^5 - 17/315*a^7 + 62/2835*a^9 -
            1382/155925*a^11 + O(a, b)^12
            sage: a.tanh(prec=5)
            a - 1/3*a^3 + O(a, b)^5
            sage: tanh(a + T.O(5))
            a - 1/3*a^3 + O(a, b)^5

        TESTS::

            sage: tanh(a^2 + T.O(5))
            a^2 + O(a, b)^5"""
    @overload
    def tanh(self, a) -> Any:
        """PowerSeries.tanh(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2312)

        Apply tanh to the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT: a new power series

        EXAMPLES:

        For one variable::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: f = (t + t**2).O(4)
            sage: tanh(f)
            t + t^2 - 1/3*t^3 + O(t^4)

        For several variables::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(3)
            sage: tanh(f)
            a + b + a*b + O(a, b)^3
            sage: f.tanh()
            a + b + a*b + O(a, b)^3
            sage: f.tanh(prec=2)
            a + b + O(a, b)^2

        If the power series has a nonzero constant coefficient `c`,
        one raises an error::

            sage: g = 2 + f
            sage: tanh(g)
            Traceback (most recent call last):
            ...
            ValueError: can only apply tanh to formal power series with zero
             constant term

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: tanh(a)
            a - 1/3*a^3 + 2/15*a^5 - 17/315*a^7 + 62/2835*a^9 -
            1382/155925*a^11 + O(a, b)^12
            sage: a.tanh(prec=5)
            a - 1/3*a^3 + O(a, b)^5
            sage: tanh(a + T.O(5))
            a - 1/3*a^3 + O(a, b)^5

        TESTS::

            sage: tanh(a^2 + T.O(5))
            a^2 + O(a, b)^5"""
    @overload
    def tanh(self, prec=...) -> Any:
        """PowerSeries.tanh(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2312)

        Apply tanh to the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT: a new power series

        EXAMPLES:

        For one variable::

            sage: t = PowerSeriesRing(QQ, 't').gen()
            sage: f = (t + t**2).O(4)
            sage: tanh(f)
            t + t^2 - 1/3*t^3 + O(t^4)

        For several variables::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(3)
            sage: tanh(f)
            a + b + a*b + O(a, b)^3
            sage: f.tanh()
            a + b + a*b + O(a, b)^3
            sage: f.tanh(prec=2)
            a + b + O(a, b)^2

        If the power series has a nonzero constant coefficient `c`,
        one raises an error::

            sage: g = 2 + f
            sage: tanh(g)
            Traceback (most recent call last):
            ...
            ValueError: can only apply tanh to formal power series with zero
             constant term

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: tanh(a)
            a - 1/3*a^3 + 2/15*a^5 - 17/315*a^7 + 62/2835*a^9 -
            1382/155925*a^11 + O(a, b)^12
            sage: a.tanh(prec=5)
            a - 1/3*a^3 + O(a, b)^5
            sage: tanh(a + T.O(5))
            a - 1/3*a^3 + O(a, b)^5

        TESTS::

            sage: tanh(a^2 + T.O(5))
            a^2 + O(a, b)^5"""
    def truncate(self, prec=...) -> Any:
        """PowerSeries.truncate(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 800)

        The polynomial obtained from power series by truncation.

        EXAMPLES::

            sage: R.<I> = GF(2)[[]]
            sage: f = 1/(1+I+O(I^8)); f
            1 + I + I^2 + I^3 + I^4 + I^5 + I^6 + I^7 + O(I^8)
            sage: f.truncate(5)
            I^4 + I^3 + I^2 + I + 1"""
    @overload
    def valuation(self) -> Any:
        """PowerSeries.valuation(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2698)

        Return the valuation of this power series.

        This is equal to the valuation of the underlying polynomial.

        EXAMPLES:

        Sparse examples::

            sage: R.<t> = PowerSeriesRing(QQ, sparse=True)
            sage: f = t^100000 + O(t^10000000)
            sage: f.valuation()
            100000
            sage: R(0).valuation()
            +Infinity

        Dense examples::

            sage: R.<t> = PowerSeriesRing(ZZ)
            sage: f = 17*t^100 + O(t^110)
            sage: f.valuation()
            100
            sage: t.valuation()
            1"""
    @overload
    def valuation(self) -> Any:
        """PowerSeries.valuation(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2698)

        Return the valuation of this power series.

        This is equal to the valuation of the underlying polynomial.

        EXAMPLES:

        Sparse examples::

            sage: R.<t> = PowerSeriesRing(QQ, sparse=True)
            sage: f = t^100000 + O(t^10000000)
            sage: f.valuation()
            100000
            sage: R(0).valuation()
            +Infinity

        Dense examples::

            sage: R.<t> = PowerSeriesRing(ZZ)
            sage: f = 17*t^100 + O(t^110)
            sage: f.valuation()
            100
            sage: t.valuation()
            1"""
    @overload
    def valuation(self) -> Any:
        """PowerSeries.valuation(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2698)

        Return the valuation of this power series.

        This is equal to the valuation of the underlying polynomial.

        EXAMPLES:

        Sparse examples::

            sage: R.<t> = PowerSeriesRing(QQ, sparse=True)
            sage: f = t^100000 + O(t^10000000)
            sage: f.valuation()
            100000
            sage: R(0).valuation()
            +Infinity

        Dense examples::

            sage: R.<t> = PowerSeriesRing(ZZ)
            sage: f = 17*t^100 + O(t^110)
            sage: f.valuation()
            100
            sage: t.valuation()
            1"""
    @overload
    def valuation(self) -> Any:
        """PowerSeries.valuation(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2698)

        Return the valuation of this power series.

        This is equal to the valuation of the underlying polynomial.

        EXAMPLES:

        Sparse examples::

            sage: R.<t> = PowerSeriesRing(QQ, sparse=True)
            sage: f = t^100000 + O(t^10000000)
            sage: f.valuation()
            100000
            sage: R(0).valuation()
            +Infinity

        Dense examples::

            sage: R.<t> = PowerSeriesRing(ZZ)
            sage: f = 17*t^100 + O(t^110)
            sage: f.valuation()
            100
            sage: t.valuation()
            1"""
    @overload
    def valuation(self) -> Any:
        """PowerSeries.valuation(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2698)

        Return the valuation of this power series.

        This is equal to the valuation of the underlying polynomial.

        EXAMPLES:

        Sparse examples::

            sage: R.<t> = PowerSeriesRing(QQ, sparse=True)
            sage: f = t^100000 + O(t^10000000)
            sage: f.valuation()
            100000
            sage: R(0).valuation()
            +Infinity

        Dense examples::

            sage: R.<t> = PowerSeriesRing(ZZ)
            sage: f = 17*t^100 + O(t^110)
            sage: f.valuation()
            100
            sage: t.valuation()
            1"""
    def valuation_zero_part(self) -> Any:
        """PowerSeries.valuation_zero_part(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1011)

        Factor ``self`` as `q^n \\cdot (a_0 + a_1 q + \\cdots)` with
        `a_0` nonzero. Then this function returns
        `a_0 + a_1 q + \\cdots` .

        .. NOTE::

           This valuation zero part need not be a unit if, e.g.,
           `a_0` is not invertible in the base ring.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(QQ)
            sage: ((1/3)*t^5*(17-2/3*t^3)).valuation_zero_part()
            17/3 - 2/9*t^3

        In this example the valuation 0 part is not a unit::

            sage: R.<t> = PowerSeriesRing(ZZ, sparse=True)
            sage: u = (-2*t^5*(17-t^3)).valuation_zero_part(); u
            -34 + 2*t^3
            sage: u.is_unit()
            False
            sage: u.valuation()
            0"""
    @overload
    def variable(self) -> Any:
        """PowerSeries.variable(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2726)

        Return a string with the name of the variable
        of this power series.

        EXAMPLES::

            sage: R.<x> = PowerSeriesRing(Rationals())
            sage: f = x^2 + 3*x^4 + O(x^7)
            sage: f.variable()
            'x'

        AUTHORS:

        - David Harvey (2006-08-08)"""
    @overload
    def variable(self) -> Any:
        """PowerSeries.variable(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2726)

        Return a string with the name of the variable
        of this power series.

        EXAMPLES::

            sage: R.<x> = PowerSeriesRing(Rationals())
            sage: f = x^2 + 3*x^4 + O(x^7)
            sage: f.variable()
            'x'

        AUTHORS:

        - David Harvey (2006-08-08)"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __call__(self, x) -> Any:
        """PowerSeries.__call__(self, x)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 396)

        Implementations *MUST* override this in the derived class.

        EXAMPLES::

            sage: from sage.rings.power_series_ring_element import PowerSeries
            sage: R.<x> = PowerSeriesRing(ZZ)
            sage: PowerSeries.__call__(1+x^2,x)
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    def __copy__(self) -> Any:
        """PowerSeries.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 511)

        Return this power series. Power series are immutable so copy can
        safely just return the same polynomial.

        EXAMPLES::

            sage: R.<q> = ZZ[[ ]]; R
            Power Series Ring in q over Integer Ring
            sage: f = 1 + 3*q + O(q^10)
            sage: copy(f) is f       # !!! ok since power series are immutable.
            True"""
    def __delitem__(self, other) -> None:
        """Delete self[key]."""
    def __getitem__(self, n) -> Any:
        """PowerSeries.__getitem__(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 842)

        Return the coefficient of `t^n` in this power series, where
        `t` is the indeterminate of the power series ring.

        If `n` is negative return 0. If `n` is beyond the precision, raise an
        :exc:`IndexError`.

        EXAMPLES::

            sage: # needs sage.rings.complex_double sage.symbolic
            sage: R.<m> = CDF[[]]
            sage: f = CDF(pi)^2 + m^3 + CDF(e)*m^4 + O(m^10); f   # abs tol 5e-16
            9.869604401089358 + 0.0*m + 0.0*m^2 + 1.0*m^3 + 2.718281828459045*m^4 + O(m^10)
            sage: f[-5]
            0.0
            sage: f[0]
            9.869604401089358
            sage: f[4]   # abs tol 5e-16
            2.718281828459045
            sage: f[9]
            0.0
            sage: f[10]
            Traceback (most recent call last):
            ...
            IndexError: coefficient not known
            sage: f[1000]
            Traceback (most recent call last):
            ...
            IndexError: coefficient not known"""
    @overload
    def __hash__(self) -> Any:
        """PowerSeries.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 172)

        Compute a hash of ``self``.

        EXAMPLES::

            sage: R.<x> = PowerSeriesRing(ZZ)
            sage: (1+x^2).__hash__()     # random
            15360174650385709"""
    @overload
    def __hash__(self) -> Any:
        """PowerSeries.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 172)

        Compute a hash of ``self``.

        EXAMPLES::

            sage: R.<x> = PowerSeriesRing(ZZ)
            sage: (1+x^2).__hash__()     # random
            15360174650385709"""
    def __lshift__(self, n) -> Any:
        """PowerSeries.__lshift__(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1194)

        Left-shift this power series by `n`, i.e., multiply by `t^n`.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: R.<x> = PowerSeriesRing(QQ, implementation='pari')
            sage: f = exp(x) + O(x^7); f
            1 + x + 1/2*x^2 + 1/6*x^3 + 1/24*x^4 + 1/120*x^5 + 1/720*x^6 + O(x^7)
            sage: f << 2
            x^2 + x^3 + 1/2*x^4 + 1/6*x^5 + 1/24*x^6 + 1/120*x^7 + 1/720*x^8 + O(x^9)
            sage: (f << 99) >> 99
            1 + x + 1/2*x^2 + 1/6*x^3 + 1/24*x^4 + 1/120*x^5 + 1/720*x^6 + O(x^7)"""
    def __mod__(self, other) -> Any:
        """PowerSeries.__mod__(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1107)

        EXAMPLES::

            sage: R.<T> = Qp(7)[[]]                                                     # needs sage.rings.padics
            sage: f = (48*67 + 46*67^2)*T + (1 + 42*67 + 5*67^3)*T^2 + O(T^3)           # needs sage.rings.padics
            sage: f % 67                                                                # needs sage.rings.padics
            T^2 + O(T^3)"""
    def __pari__(self) -> Any:
        """PowerSeries.__pari__(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2857)

        Return a PARI representation of this series.

        There are currently limits to the possible base rings over which this
        function works.  See the documentation for
        :meth:`~sage.rings.polynomial.polynomial_element.Polynomial.__pari__`

        EXAMPLES::

            sage: k.<w> = QQ[[]]
            sage: f = 1 + 17*w + 15*w^3 + O(w^5)
            sage: pari(f)  # indirect doctest                                           # needs sage.libs.pari
            1 + 17*w + 15*w^3 + O(w^5)
            sage: pari(1 - 19*w + w^5)  # indirect doctest                              # needs sage.libs.pari
            w^5 - 19*w + 1
            sage: R.<x> = Zmod(6)[[]]
            sage: pari(1 + x + 8*x^3 + O(x^8))  # indirect doctest                      # needs sage.libs.pari
            Mod(1, 6) + Mod(1, 6)*x + Mod(2, 6)*x^3 + O(x^8)

        TESTS::

            sage: pari(1 + O(x^1))                                                      # needs sage.libs.pari
            Mod(1, 6) + O(x)
            sage: pari(O(x^1))                                                          # needs sage.libs.pari
            O(x)
            sage: pari(O(x^0))                                                          # needs sage.libs.pari
            O(x^0)"""
    def __pow__(self, r, dummy) -> Any:
        """PowerSeries.__pow__(self, r, dummy)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1121)

        EXAMPLES::

            sage: x = QQ[['x']].0
            sage: f = x^2 + x^4 + O(x^6)
            sage: f^(1/2)
            x + 1/2*x^3 + O(x^5)
            sage: f^7
            x^14 + 7*x^16 + O(x^18)
            sage: f^(7/2)
            x^7 + 7/2*x^9 + O(x^11)
            sage: h = x^2 + 2*x^4 + x^6
            sage: h^(1/2)
            x + x^3
            sage: O(x^4)^(1/2)
            O(x^2)"""
    def __reduce__(self) -> Any:
        """PowerSeries.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 184)

        EXAMPLES::

            sage: K.<t> = PowerSeriesRing(QQ, 5)
            sage: f = 1 + t - t^3 + O(t^12)
            sage: loads(dumps(f)) == f
            True"""
    def __rlshift__(self, other):
        """Return value<<self."""
    def __rmod__(self, other):
        """Return value%self."""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
    def __rrshift__(self, other):
        """Return value>>self."""
    def __rshift__(self, n) -> Any:
        """PowerSeries.__rshift__(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 1211)

        Right-shift this power series by `n`, i.e., divide by `t^n`.

        Terms below `t^n` are discarded.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: R.<x> = PowerSeriesRing(QQ, implementation='pari')
            sage: f = exp(x) + O(x^7)
            sage: f >> 3
            1/6 + 1/24*x + 1/120*x^2 + 1/720*x^3 + O(x^4)
            sage: f >> 7
            O(x^0)
            sage: f >> 99
            O(x^0)
            sage: (f >> 99) << 99
            O(x^99)"""
    def __setitem__(self, n, value) -> Any:
        """PowerSeries.__setitem__(self, n, value)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_ring_element.pyx (starting at line 2786)

        Called when an attempt is made to change a power series.

        EXAMPLES::

            sage: R.<t> = ZZ[[]]
            sage: f = 3 - t^3 + O(t^5)
            sage: f[1] = 5
            Traceback (most recent call last):
            ...
            IndexError: power series are immutable"""
