import cypari2.pari_instance
import sage.rings.power_series_ring_element
from sage.rings.infinity import infinity as infinity
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

pari: cypari2.pari_instance.Pari

class PowerSeries_pari(sage.rings.power_series_ring_element.PowerSeries):
    """PowerSeries_pari(parent, f=0, prec=infinity, check=None)

    File: /build/sagemath/src/sage/src/sage/rings/power_series_pari.pyx (starting at line 116)

    A power series implemented using PARI.

    INPUT:

    - ``parent`` -- the power series ring to use as the parent

    - ``f`` -- object from which to construct a power series

    - ``prec`` -- (default: infinity) precision of the element
      to be constructed

    - ``check`` -- ignored, but accepted for compatibility with
      :class:`~sage.rings.power_series_poly.PowerSeries_poly`"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, f=..., prec=..., check=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/power_series_pari.pyx (starting at line 132)

                Initialize ``self``.

                TESTS::

                    sage: # needs sage.rings.real_mpfr
                    sage: R.<q> = PowerSeriesRing(CC, implementation='pari')
                    sage: TestSuite(q).run()
                    sage: f = q - q^3 + O(q^10)
                    sage: TestSuite(f).run()
        """
    def dict(self) -> Any:
        """PowerSeries_pari.monomial_coefficients(self, copy=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_pari.pyx (starting at line 737)

        Return a dictionary of coefficients for ``self``.

        This is simply a dict for the underlying polynomial; it need
        not have keys corresponding to every number smaller than
        ``self.prec()``.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(ZZ, implementation='pari')
            sage: f = 1 + t^10 + O(t^12)
            sage: f.monomial_coefficients()
            {0: 1, 10: 1}

        ``dict`` is an alias::

            sage: f.dict()
            {0: 1, 10: 1}"""
    @overload
    def integral(self, var=...) -> Any:
        """PowerSeries_pari.integral(self, var=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_pari.pyx (starting at line 797)

        Return the formal integral of ``self``.

        By default, the integration variable is the variable of the
        power series.  Otherwise, the integration variable is the
        optional parameter ``var``.

        .. NOTE::

            The integral is always chosen so the constant term is 0.

        EXAMPLES::

            sage: k.<w> = PowerSeriesRing(QQ, implementation='pari')
            sage: (1+17*w+15*w^3+O(w^5)).integral()
            w + 17/2*w^2 + 15/4*w^4 + O(w^6)
            sage: (w^3 + 4*w^4 + O(w^7)).integral()
            1/4*w^4 + 4/5*w^5 + O(w^8)
            sage: (3*w^2).integral()
            w^3

        TESTS::

            sage: t = PowerSeriesRing(QQ, 't', implementation='pari').gen()
            sage: f = t + 5*t^2 + 21*t^3
            sage: g = f.integral() ; g
            1/2*t^2 + 5/3*t^3 + 21/4*t^4
            sage: g.parent()
            Power Series Ring in t over Rational Field

            sage: R.<a> = QQ[]
            sage: t = PowerSeriesRing(R, 't', implementation='pari').gen()
            sage: f = a*t +5*t^2
            sage: f.integral()
            1/2*a*t^2 + 5/3*t^3
            sage: f.integral(a)
            1/2*a^2*t + 5*a*t^2"""
    @overload
    def integral(self) -> Any:
        """PowerSeries_pari.integral(self, var=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_pari.pyx (starting at line 797)

        Return the formal integral of ``self``.

        By default, the integration variable is the variable of the
        power series.  Otherwise, the integration variable is the
        optional parameter ``var``.

        .. NOTE::

            The integral is always chosen so the constant term is 0.

        EXAMPLES::

            sage: k.<w> = PowerSeriesRing(QQ, implementation='pari')
            sage: (1+17*w+15*w^3+O(w^5)).integral()
            w + 17/2*w^2 + 15/4*w^4 + O(w^6)
            sage: (w^3 + 4*w^4 + O(w^7)).integral()
            1/4*w^4 + 4/5*w^5 + O(w^8)
            sage: (3*w^2).integral()
            w^3

        TESTS::

            sage: t = PowerSeriesRing(QQ, 't', implementation='pari').gen()
            sage: f = t + 5*t^2 + 21*t^3
            sage: g = f.integral() ; g
            1/2*t^2 + 5/3*t^3 + 21/4*t^4
            sage: g.parent()
            Power Series Ring in t over Rational Field

            sage: R.<a> = QQ[]
            sage: t = PowerSeriesRing(R, 't', implementation='pari').gen()
            sage: f = a*t +5*t^2
            sage: f.integral()
            1/2*a*t^2 + 5/3*t^3
            sage: f.integral(a)
            1/2*a^2*t + 5*a*t^2"""
    @overload
    def integral(self) -> Any:
        """PowerSeries_pari.integral(self, var=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_pari.pyx (starting at line 797)

        Return the formal integral of ``self``.

        By default, the integration variable is the variable of the
        power series.  Otherwise, the integration variable is the
        optional parameter ``var``.

        .. NOTE::

            The integral is always chosen so the constant term is 0.

        EXAMPLES::

            sage: k.<w> = PowerSeriesRing(QQ, implementation='pari')
            sage: (1+17*w+15*w^3+O(w^5)).integral()
            w + 17/2*w^2 + 15/4*w^4 + O(w^6)
            sage: (w^3 + 4*w^4 + O(w^7)).integral()
            1/4*w^4 + 4/5*w^5 + O(w^8)
            sage: (3*w^2).integral()
            w^3

        TESTS::

            sage: t = PowerSeriesRing(QQ, 't', implementation='pari').gen()
            sage: f = t + 5*t^2 + 21*t^3
            sage: g = f.integral() ; g
            1/2*t^2 + 5/3*t^3 + 21/4*t^4
            sage: g.parent()
            Power Series Ring in t over Rational Field

            sage: R.<a> = QQ[]
            sage: t = PowerSeriesRing(R, 't', implementation='pari').gen()
            sage: f = a*t +5*t^2
            sage: f.integral()
            1/2*a*t^2 + 5/3*t^3
            sage: f.integral(a)
            1/2*a^2*t + 5*a*t^2"""
    @overload
    def integral(self) -> Any:
        """PowerSeries_pari.integral(self, var=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_pari.pyx (starting at line 797)

        Return the formal integral of ``self``.

        By default, the integration variable is the variable of the
        power series.  Otherwise, the integration variable is the
        optional parameter ``var``.

        .. NOTE::

            The integral is always chosen so the constant term is 0.

        EXAMPLES::

            sage: k.<w> = PowerSeriesRing(QQ, implementation='pari')
            sage: (1+17*w+15*w^3+O(w^5)).integral()
            w + 17/2*w^2 + 15/4*w^4 + O(w^6)
            sage: (w^3 + 4*w^4 + O(w^7)).integral()
            1/4*w^4 + 4/5*w^5 + O(w^8)
            sage: (3*w^2).integral()
            w^3

        TESTS::

            sage: t = PowerSeriesRing(QQ, 't', implementation='pari').gen()
            sage: f = t + 5*t^2 + 21*t^3
            sage: g = f.integral() ; g
            1/2*t^2 + 5/3*t^3 + 21/4*t^4
            sage: g.parent()
            Power Series Ring in t over Rational Field

            sage: R.<a> = QQ[]
            sage: t = PowerSeriesRing(R, 't', implementation='pari').gen()
            sage: f = a*t +5*t^2
            sage: f.integral()
            1/2*a*t^2 + 5/3*t^3
            sage: f.integral(a)
            1/2*a^2*t + 5*a*t^2"""
    @overload
    def integral(self) -> Any:
        """PowerSeries_pari.integral(self, var=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_pari.pyx (starting at line 797)

        Return the formal integral of ``self``.

        By default, the integration variable is the variable of the
        power series.  Otherwise, the integration variable is the
        optional parameter ``var``.

        .. NOTE::

            The integral is always chosen so the constant term is 0.

        EXAMPLES::

            sage: k.<w> = PowerSeriesRing(QQ, implementation='pari')
            sage: (1+17*w+15*w^3+O(w^5)).integral()
            w + 17/2*w^2 + 15/4*w^4 + O(w^6)
            sage: (w^3 + 4*w^4 + O(w^7)).integral()
            1/4*w^4 + 4/5*w^5 + O(w^8)
            sage: (3*w^2).integral()
            w^3

        TESTS::

            sage: t = PowerSeriesRing(QQ, 't', implementation='pari').gen()
            sage: f = t + 5*t^2 + 21*t^3
            sage: g = f.integral() ; g
            1/2*t^2 + 5/3*t^3 + 21/4*t^4
            sage: g.parent()
            Power Series Ring in t over Rational Field

            sage: R.<a> = QQ[]
            sage: t = PowerSeriesRing(R, 't', implementation='pari').gen()
            sage: f = a*t +5*t^2
            sage: f.integral()
            1/2*a*t^2 + 5/3*t^3
            sage: f.integral(a)
            1/2*a^2*t + 5*a*t^2"""
    @overload
    def integral(self) -> Any:
        """PowerSeries_pari.integral(self, var=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_pari.pyx (starting at line 797)

        Return the formal integral of ``self``.

        By default, the integration variable is the variable of the
        power series.  Otherwise, the integration variable is the
        optional parameter ``var``.

        .. NOTE::

            The integral is always chosen so the constant term is 0.

        EXAMPLES::

            sage: k.<w> = PowerSeriesRing(QQ, implementation='pari')
            sage: (1+17*w+15*w^3+O(w^5)).integral()
            w + 17/2*w^2 + 15/4*w^4 + O(w^6)
            sage: (w^3 + 4*w^4 + O(w^7)).integral()
            1/4*w^4 + 4/5*w^5 + O(w^8)
            sage: (3*w^2).integral()
            w^3

        TESTS::

            sage: t = PowerSeriesRing(QQ, 't', implementation='pari').gen()
            sage: f = t + 5*t^2 + 21*t^3
            sage: g = f.integral() ; g
            1/2*t^2 + 5/3*t^3 + 21/4*t^4
            sage: g.parent()
            Power Series Ring in t over Rational Field

            sage: R.<a> = QQ[]
            sage: t = PowerSeriesRing(R, 't', implementation='pari').gen()
            sage: f = a*t +5*t^2
            sage: f.integral()
            1/2*a*t^2 + 5/3*t^3
            sage: f.integral(a)
            1/2*a^2*t + 5*a*t^2"""
    @overload
    def integral(self, a) -> Any:
        """PowerSeries_pari.integral(self, var=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_pari.pyx (starting at line 797)

        Return the formal integral of ``self``.

        By default, the integration variable is the variable of the
        power series.  Otherwise, the integration variable is the
        optional parameter ``var``.

        .. NOTE::

            The integral is always chosen so the constant term is 0.

        EXAMPLES::

            sage: k.<w> = PowerSeriesRing(QQ, implementation='pari')
            sage: (1+17*w+15*w^3+O(w^5)).integral()
            w + 17/2*w^2 + 15/4*w^4 + O(w^6)
            sage: (w^3 + 4*w^4 + O(w^7)).integral()
            1/4*w^4 + 4/5*w^5 + O(w^8)
            sage: (3*w^2).integral()
            w^3

        TESTS::

            sage: t = PowerSeriesRing(QQ, 't', implementation='pari').gen()
            sage: f = t + 5*t^2 + 21*t^3
            sage: g = f.integral() ; g
            1/2*t^2 + 5/3*t^3 + 21/4*t^4
            sage: g.parent()
            Power Series Ring in t over Rational Field

            sage: R.<a> = QQ[]
            sage: t = PowerSeriesRing(R, 't', implementation='pari').gen()
            sage: f = a*t +5*t^2
            sage: f.integral()
            1/2*a*t^2 + 5/3*t^3
            sage: f.integral(a)
            1/2*a^2*t + 5*a*t^2"""
    @overload
    def list(self) -> Any:
        """PowerSeries_pari.list(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_pari.pyx (starting at line 634)

        Return the list of known coefficients for ``self``.

        This is just the list of coefficients of the underlying
        polynomial; it need not have length equal to ``self.prec()``.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(ZZ, implementation='pari')
            sage: f = 1 - 5*t^3 + t^5 + O(t^7)
            sage: f.list()
            [1, 0, 0, -5, 0, 1]

            sage: # needs sage.rings.padics
            sage: S.<u> = PowerSeriesRing(pAdicRing(5), implementation='pari')
            sage: (2 + u).list()
            [2 + O(5^20), 1 + O(5^20)]"""
    @overload
    def list(self) -> Any:
        """PowerSeries_pari.list(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_pari.pyx (starting at line 634)

        Return the list of known coefficients for ``self``.

        This is just the list of coefficients of the underlying
        polynomial; it need not have length equal to ``self.prec()``.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(ZZ, implementation='pari')
            sage: f = 1 - 5*t^3 + t^5 + O(t^7)
            sage: f.list()
            [1, 0, 0, -5, 0, 1]

            sage: # needs sage.rings.padics
            sage: S.<u> = PowerSeriesRing(pAdicRing(5), implementation='pari')
            sage: (2 + u).list()
            [2 + O(5^20), 1 + O(5^20)]"""
    @overload
    def list(self) -> Any:
        """PowerSeries_pari.list(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_pari.pyx (starting at line 634)

        Return the list of known coefficients for ``self``.

        This is just the list of coefficients of the underlying
        polynomial; it need not have length equal to ``self.prec()``.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(ZZ, implementation='pari')
            sage: f = 1 - 5*t^3 + t^5 + O(t^7)
            sage: f.list()
            [1, 0, 0, -5, 0, 1]

            sage: # needs sage.rings.padics
            sage: S.<u> = PowerSeriesRing(pAdicRing(5), implementation='pari')
            sage: (2 + u).list()
            [2 + O(5^20), 1 + O(5^20)]"""
    @overload
    def monomial_coefficients(self, copy=...) -> Any:
        """PowerSeries_pari.monomial_coefficients(self, copy=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_pari.pyx (starting at line 737)

        Return a dictionary of coefficients for ``self``.

        This is simply a dict for the underlying polynomial; it need
        not have keys corresponding to every number smaller than
        ``self.prec()``.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(ZZ, implementation='pari')
            sage: f = 1 + t^10 + O(t^12)
            sage: f.monomial_coefficients()
            {0: 1, 10: 1}

        ``dict`` is an alias::

            sage: f.dict()
            {0: 1, 10: 1}"""
    @overload
    def monomial_coefficients(self) -> Any:
        """PowerSeries_pari.monomial_coefficients(self, copy=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_pari.pyx (starting at line 737)

        Return a dictionary of coefficients for ``self``.

        This is simply a dict for the underlying polynomial; it need
        not have keys corresponding to every number smaller than
        ``self.prec()``.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(ZZ, implementation='pari')
            sage: f = 1 + t^10 + O(t^12)
            sage: f.monomial_coefficients()
            {0: 1, 10: 1}

        ``dict`` is an alias::

            sage: f.dict()
            {0: 1, 10: 1}"""
    @overload
    def padded_list(self, n=...) -> Any:
        """PowerSeries_pari.padded_list(self, n=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_pari.pyx (starting at line 665)

        Return a list of coefficients of ``self`` up to (but not
        including) `q^n`.

        The list is padded with zeroes on the right so that it has
        length `n`.

        INPUT:

        - ``n`` -- nonnegative integer (optional); if `n` is not
          given, it will be taken to be the precision of ``self``,
          unless this is ``+Infinity``, in which case we just
          return ``self.list()``

        EXAMPLES::

            sage: R.<q> = PowerSeriesRing(QQ, implementation='pari')
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
        """PowerSeries_pari.padded_list(self, n=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_pari.pyx (starting at line 665)

        Return a list of coefficients of ``self`` up to (but not
        including) `q^n`.

        The list is padded with zeroes on the right so that it has
        length `n`.

        INPUT:

        - ``n`` -- nonnegative integer (optional); if `n` is not
          given, it will be taken to be the precision of ``self``,
          unless this is ``+Infinity``, in which case we just
          return ``self.list()``

        EXAMPLES::

            sage: R.<q> = PowerSeriesRing(QQ, implementation='pari')
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
        """PowerSeries_pari.padded_list(self, n=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_pari.pyx (starting at line 665)

        Return a list of coefficients of ``self`` up to (but not
        including) `q^n`.

        The list is padded with zeroes on the right so that it has
        length `n`.

        INPUT:

        - ``n`` -- nonnegative integer (optional); if `n` is not
          given, it will be taken to be the precision of ``self``,
          unless this is ``+Infinity``, in which case we just
          return ``self.list()``

        EXAMPLES::

            sage: R.<q> = PowerSeriesRing(QQ, implementation='pari')
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
    def polynomial(self) -> Any:
        """PowerSeries_pari.polynomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_pari.pyx (starting at line 245)

        Convert ``self`` to a polynomial.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(GF(7), implementation='pari')
            sage: f = 3 - t^3 + O(t^5)
            sage: f.polynomial()
            6*t^3 + 3"""
    @overload
    def polynomial(self) -> Any:
        """PowerSeries_pari.polynomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_pari.pyx (starting at line 245)

        Convert ``self`` to a polynomial.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(GF(7), implementation='pari')
            sage: f = 3 - t^3 + O(t^5)
            sage: f.polynomial()
            6*t^3 + 3"""
    @overload
    def reverse(self, precision=...) -> Any:
        """PowerSeries_pari.reverse(self, precision=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_pari.pyx (starting at line 840)

        Return the reverse of ``self``.

        The reverse of a power series `f` is the power series `g` such
        that `g(f(x)) = x`.  This exists if and only if the valuation
        of ``self`` is exactly 1 and the coefficient of `x` is a unit.

        If the optional argument ``precision`` is given, the reverse
        is returned with this precision.  If ``f`` has infinite
        precision and the argument ``precision`` is not given, then
        the reverse is returned with the default precision of
        ``f.parent()``.

        EXAMPLES::

            sage: R.<x> = PowerSeriesRing(QQ, implementation='pari')
            sage: f = 2*x + 3*x^2 - x^4 + O(x^5)
            sage: g = f.reverse()
            sage: g
            1/2*x - 3/8*x^2 + 9/16*x^3 - 131/128*x^4 + O(x^5)
            sage: f(g)
            x + O(x^5)
            sage: g(f)
            x + O(x^5)

            sage: A.<t> = PowerSeriesRing(ZZ, implementation='pari')
            sage: a = t - t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + t^2 + 2*t^3 + 7*t^4 + 25*t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

            sage: B.<b,c> = PolynomialRing(ZZ)
            sage: A.<t> = PowerSeriesRing(B, implementation='pari')
            sage: f = t + b*t^2 + c*t^3 + O(t^4)
            sage: g = f.reverse(); g
            t - b*t^2 + (2*b^2 - c)*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

            sage: A.<t> = PowerSeriesRing(ZZ, implementation='pari')
            sage: B.<x> = PowerSeriesRing(A, implementation='pari')
            sage: f = (1 - 3*t + 4*t^3 + O(t^4))*x + (2 + t + t^2 + O(t^3))*x^2 + O(x^3)
            sage: g = f.reverse(); g
            (1 + 3*t + 9*t^2 + 23*t^3 + O(t^4))*x + (-2 - 19*t - 118*t^2 + O(t^3))*x^2 + O(x^3)

        The optional argument ``precision`` sets the precision of the output::

            sage: R.<x> = PowerSeriesRing(QQ, implementation='pari')
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

            sage: R.<x> = PowerSeriesRing(QQ, default_prec=20, implementation='pari')
            sage: (x - x^2).reverse()  # get some Catalan numbers
            x + x^2 + 2*x^3 + 5*x^4 + 14*x^5 + 42*x^6 + 132*x^7 + 429*x^8
             + 1430*x^9 + 4862*x^10 + 16796*x^11 + 58786*x^12 + 208012*x^13
             + 742900*x^14 + 2674440*x^15 + 9694845*x^16 + 35357670*x^17
             + 129644790*x^18 + 477638700*x^19 + O(x^20)
            sage: (x - x^2).reverse(precision=3)
            x + x^2 + O(x^3)

        TESTS::

            sage: R.<x> = PowerSeriesRing(QQ, implementation='pari')
            sage: f = 1 + 2*x + 3*x^2 - x^4 + O(x^5)
            sage: f.reverse()
            Traceback (most recent call last):
            ...
            PariError: domain error in serreverse: valuation != 1"""
    @overload
    def reverse(self) -> Any:
        """PowerSeries_pari.reverse(self, precision=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_pari.pyx (starting at line 840)

        Return the reverse of ``self``.

        The reverse of a power series `f` is the power series `g` such
        that `g(f(x)) = x`.  This exists if and only if the valuation
        of ``self`` is exactly 1 and the coefficient of `x` is a unit.

        If the optional argument ``precision`` is given, the reverse
        is returned with this precision.  If ``f`` has infinite
        precision and the argument ``precision`` is not given, then
        the reverse is returned with the default precision of
        ``f.parent()``.

        EXAMPLES::

            sage: R.<x> = PowerSeriesRing(QQ, implementation='pari')
            sage: f = 2*x + 3*x^2 - x^4 + O(x^5)
            sage: g = f.reverse()
            sage: g
            1/2*x - 3/8*x^2 + 9/16*x^3 - 131/128*x^4 + O(x^5)
            sage: f(g)
            x + O(x^5)
            sage: g(f)
            x + O(x^5)

            sage: A.<t> = PowerSeriesRing(ZZ, implementation='pari')
            sage: a = t - t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + t^2 + 2*t^3 + 7*t^4 + 25*t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

            sage: B.<b,c> = PolynomialRing(ZZ)
            sage: A.<t> = PowerSeriesRing(B, implementation='pari')
            sage: f = t + b*t^2 + c*t^3 + O(t^4)
            sage: g = f.reverse(); g
            t - b*t^2 + (2*b^2 - c)*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

            sage: A.<t> = PowerSeriesRing(ZZ, implementation='pari')
            sage: B.<x> = PowerSeriesRing(A, implementation='pari')
            sage: f = (1 - 3*t + 4*t^3 + O(t^4))*x + (2 + t + t^2 + O(t^3))*x^2 + O(x^3)
            sage: g = f.reverse(); g
            (1 + 3*t + 9*t^2 + 23*t^3 + O(t^4))*x + (-2 - 19*t - 118*t^2 + O(t^3))*x^2 + O(x^3)

        The optional argument ``precision`` sets the precision of the output::

            sage: R.<x> = PowerSeriesRing(QQ, implementation='pari')
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

            sage: R.<x> = PowerSeriesRing(QQ, default_prec=20, implementation='pari')
            sage: (x - x^2).reverse()  # get some Catalan numbers
            x + x^2 + 2*x^3 + 5*x^4 + 14*x^5 + 42*x^6 + 132*x^7 + 429*x^8
             + 1430*x^9 + 4862*x^10 + 16796*x^11 + 58786*x^12 + 208012*x^13
             + 742900*x^14 + 2674440*x^15 + 9694845*x^16 + 35357670*x^17
             + 129644790*x^18 + 477638700*x^19 + O(x^20)
            sage: (x - x^2).reverse(precision=3)
            x + x^2 + O(x^3)

        TESTS::

            sage: R.<x> = PowerSeriesRing(QQ, implementation='pari')
            sage: f = 1 + 2*x + 3*x^2 - x^4 + O(x^5)
            sage: f.reverse()
            Traceback (most recent call last):
            ...
            PariError: domain error in serreverse: valuation != 1"""
    @overload
    def reverse(self) -> Any:
        """PowerSeries_pari.reverse(self, precision=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_pari.pyx (starting at line 840)

        Return the reverse of ``self``.

        The reverse of a power series `f` is the power series `g` such
        that `g(f(x)) = x`.  This exists if and only if the valuation
        of ``self`` is exactly 1 and the coefficient of `x` is a unit.

        If the optional argument ``precision`` is given, the reverse
        is returned with this precision.  If ``f`` has infinite
        precision and the argument ``precision`` is not given, then
        the reverse is returned with the default precision of
        ``f.parent()``.

        EXAMPLES::

            sage: R.<x> = PowerSeriesRing(QQ, implementation='pari')
            sage: f = 2*x + 3*x^2 - x^4 + O(x^5)
            sage: g = f.reverse()
            sage: g
            1/2*x - 3/8*x^2 + 9/16*x^3 - 131/128*x^4 + O(x^5)
            sage: f(g)
            x + O(x^5)
            sage: g(f)
            x + O(x^5)

            sage: A.<t> = PowerSeriesRing(ZZ, implementation='pari')
            sage: a = t - t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + t^2 + 2*t^3 + 7*t^4 + 25*t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

            sage: B.<b,c> = PolynomialRing(ZZ)
            sage: A.<t> = PowerSeriesRing(B, implementation='pari')
            sage: f = t + b*t^2 + c*t^3 + O(t^4)
            sage: g = f.reverse(); g
            t - b*t^2 + (2*b^2 - c)*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

            sage: A.<t> = PowerSeriesRing(ZZ, implementation='pari')
            sage: B.<x> = PowerSeriesRing(A, implementation='pari')
            sage: f = (1 - 3*t + 4*t^3 + O(t^4))*x + (2 + t + t^2 + O(t^3))*x^2 + O(x^3)
            sage: g = f.reverse(); g
            (1 + 3*t + 9*t^2 + 23*t^3 + O(t^4))*x + (-2 - 19*t - 118*t^2 + O(t^3))*x^2 + O(x^3)

        The optional argument ``precision`` sets the precision of the output::

            sage: R.<x> = PowerSeriesRing(QQ, implementation='pari')
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

            sage: R.<x> = PowerSeriesRing(QQ, default_prec=20, implementation='pari')
            sage: (x - x^2).reverse()  # get some Catalan numbers
            x + x^2 + 2*x^3 + 5*x^4 + 14*x^5 + 42*x^6 + 132*x^7 + 429*x^8
             + 1430*x^9 + 4862*x^10 + 16796*x^11 + 58786*x^12 + 208012*x^13
             + 742900*x^14 + 2674440*x^15 + 9694845*x^16 + 35357670*x^17
             + 129644790*x^18 + 477638700*x^19 + O(x^20)
            sage: (x - x^2).reverse(precision=3)
            x + x^2 + O(x^3)

        TESTS::

            sage: R.<x> = PowerSeriesRing(QQ, implementation='pari')
            sage: f = 1 + 2*x + 3*x^2 - x^4 + O(x^5)
            sage: f.reverse()
            Traceback (most recent call last):
            ...
            PariError: domain error in serreverse: valuation != 1"""
    @overload
    def reverse(self) -> Any:
        """PowerSeries_pari.reverse(self, precision=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_pari.pyx (starting at line 840)

        Return the reverse of ``self``.

        The reverse of a power series `f` is the power series `g` such
        that `g(f(x)) = x`.  This exists if and only if the valuation
        of ``self`` is exactly 1 and the coefficient of `x` is a unit.

        If the optional argument ``precision`` is given, the reverse
        is returned with this precision.  If ``f`` has infinite
        precision and the argument ``precision`` is not given, then
        the reverse is returned with the default precision of
        ``f.parent()``.

        EXAMPLES::

            sage: R.<x> = PowerSeriesRing(QQ, implementation='pari')
            sage: f = 2*x + 3*x^2 - x^4 + O(x^5)
            sage: g = f.reverse()
            sage: g
            1/2*x - 3/8*x^2 + 9/16*x^3 - 131/128*x^4 + O(x^5)
            sage: f(g)
            x + O(x^5)
            sage: g(f)
            x + O(x^5)

            sage: A.<t> = PowerSeriesRing(ZZ, implementation='pari')
            sage: a = t - t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + t^2 + 2*t^3 + 7*t^4 + 25*t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

            sage: B.<b,c> = PolynomialRing(ZZ)
            sage: A.<t> = PowerSeriesRing(B, implementation='pari')
            sage: f = t + b*t^2 + c*t^3 + O(t^4)
            sage: g = f.reverse(); g
            t - b*t^2 + (2*b^2 - c)*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

            sage: A.<t> = PowerSeriesRing(ZZ, implementation='pari')
            sage: B.<x> = PowerSeriesRing(A, implementation='pari')
            sage: f = (1 - 3*t + 4*t^3 + O(t^4))*x + (2 + t + t^2 + O(t^3))*x^2 + O(x^3)
            sage: g = f.reverse(); g
            (1 + 3*t + 9*t^2 + 23*t^3 + O(t^4))*x + (-2 - 19*t - 118*t^2 + O(t^3))*x^2 + O(x^3)

        The optional argument ``precision`` sets the precision of the output::

            sage: R.<x> = PowerSeriesRing(QQ, implementation='pari')
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

            sage: R.<x> = PowerSeriesRing(QQ, default_prec=20, implementation='pari')
            sage: (x - x^2).reverse()  # get some Catalan numbers
            x + x^2 + 2*x^3 + 5*x^4 + 14*x^5 + 42*x^6 + 132*x^7 + 429*x^8
             + 1430*x^9 + 4862*x^10 + 16796*x^11 + 58786*x^12 + 208012*x^13
             + 742900*x^14 + 2674440*x^15 + 9694845*x^16 + 35357670*x^17
             + 129644790*x^18 + 477638700*x^19 + O(x^20)
            sage: (x - x^2).reverse(precision=3)
            x + x^2 + O(x^3)

        TESTS::

            sage: R.<x> = PowerSeriesRing(QQ, implementation='pari')
            sage: f = 1 + 2*x + 3*x^2 - x^4 + O(x^5)
            sage: f.reverse()
            Traceback (most recent call last):
            ...
            PariError: domain error in serreverse: valuation != 1"""
    @overload
    def reverse(self) -> Any:
        """PowerSeries_pari.reverse(self, precision=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_pari.pyx (starting at line 840)

        Return the reverse of ``self``.

        The reverse of a power series `f` is the power series `g` such
        that `g(f(x)) = x`.  This exists if and only if the valuation
        of ``self`` is exactly 1 and the coefficient of `x` is a unit.

        If the optional argument ``precision`` is given, the reverse
        is returned with this precision.  If ``f`` has infinite
        precision and the argument ``precision`` is not given, then
        the reverse is returned with the default precision of
        ``f.parent()``.

        EXAMPLES::

            sage: R.<x> = PowerSeriesRing(QQ, implementation='pari')
            sage: f = 2*x + 3*x^2 - x^4 + O(x^5)
            sage: g = f.reverse()
            sage: g
            1/2*x - 3/8*x^2 + 9/16*x^3 - 131/128*x^4 + O(x^5)
            sage: f(g)
            x + O(x^5)
            sage: g(f)
            x + O(x^5)

            sage: A.<t> = PowerSeriesRing(ZZ, implementation='pari')
            sage: a = t - t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + t^2 + 2*t^3 + 7*t^4 + 25*t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

            sage: B.<b,c> = PolynomialRing(ZZ)
            sage: A.<t> = PowerSeriesRing(B, implementation='pari')
            sage: f = t + b*t^2 + c*t^3 + O(t^4)
            sage: g = f.reverse(); g
            t - b*t^2 + (2*b^2 - c)*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

            sage: A.<t> = PowerSeriesRing(ZZ, implementation='pari')
            sage: B.<x> = PowerSeriesRing(A, implementation='pari')
            sage: f = (1 - 3*t + 4*t^3 + O(t^4))*x + (2 + t + t^2 + O(t^3))*x^2 + O(x^3)
            sage: g = f.reverse(); g
            (1 + 3*t + 9*t^2 + 23*t^3 + O(t^4))*x + (-2 - 19*t - 118*t^2 + O(t^3))*x^2 + O(x^3)

        The optional argument ``precision`` sets the precision of the output::

            sage: R.<x> = PowerSeriesRing(QQ, implementation='pari')
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

            sage: R.<x> = PowerSeriesRing(QQ, default_prec=20, implementation='pari')
            sage: (x - x^2).reverse()  # get some Catalan numbers
            x + x^2 + 2*x^3 + 5*x^4 + 14*x^5 + 42*x^6 + 132*x^7 + 429*x^8
             + 1430*x^9 + 4862*x^10 + 16796*x^11 + 58786*x^12 + 208012*x^13
             + 742900*x^14 + 2674440*x^15 + 9694845*x^16 + 35357670*x^17
             + 129644790*x^18 + 477638700*x^19 + O(x^20)
            sage: (x - x^2).reverse(precision=3)
            x + x^2 + O(x^3)

        TESTS::

            sage: R.<x> = PowerSeriesRing(QQ, implementation='pari')
            sage: f = 1 + 2*x + 3*x^2 - x^4 + O(x^5)
            sage: f.reverse()
            Traceback (most recent call last):
            ...
            PariError: domain error in serreverse: valuation != 1"""
    @overload
    def reverse(self, precision=...) -> Any:
        """PowerSeries_pari.reverse(self, precision=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_pari.pyx (starting at line 840)

        Return the reverse of ``self``.

        The reverse of a power series `f` is the power series `g` such
        that `g(f(x)) = x`.  This exists if and only if the valuation
        of ``self`` is exactly 1 and the coefficient of `x` is a unit.

        If the optional argument ``precision`` is given, the reverse
        is returned with this precision.  If ``f`` has infinite
        precision and the argument ``precision`` is not given, then
        the reverse is returned with the default precision of
        ``f.parent()``.

        EXAMPLES::

            sage: R.<x> = PowerSeriesRing(QQ, implementation='pari')
            sage: f = 2*x + 3*x^2 - x^4 + O(x^5)
            sage: g = f.reverse()
            sage: g
            1/2*x - 3/8*x^2 + 9/16*x^3 - 131/128*x^4 + O(x^5)
            sage: f(g)
            x + O(x^5)
            sage: g(f)
            x + O(x^5)

            sage: A.<t> = PowerSeriesRing(ZZ, implementation='pari')
            sage: a = t - t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + t^2 + 2*t^3 + 7*t^4 + 25*t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

            sage: B.<b,c> = PolynomialRing(ZZ)
            sage: A.<t> = PowerSeriesRing(B, implementation='pari')
            sage: f = t + b*t^2 + c*t^3 + O(t^4)
            sage: g = f.reverse(); g
            t - b*t^2 + (2*b^2 - c)*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

            sage: A.<t> = PowerSeriesRing(ZZ, implementation='pari')
            sage: B.<x> = PowerSeriesRing(A, implementation='pari')
            sage: f = (1 - 3*t + 4*t^3 + O(t^4))*x + (2 + t + t^2 + O(t^3))*x^2 + O(x^3)
            sage: g = f.reverse(); g
            (1 + 3*t + 9*t^2 + 23*t^3 + O(t^4))*x + (-2 - 19*t - 118*t^2 + O(t^3))*x^2 + O(x^3)

        The optional argument ``precision`` sets the precision of the output::

            sage: R.<x> = PowerSeriesRing(QQ, implementation='pari')
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

            sage: R.<x> = PowerSeriesRing(QQ, default_prec=20, implementation='pari')
            sage: (x - x^2).reverse()  # get some Catalan numbers
            x + x^2 + 2*x^3 + 5*x^4 + 14*x^5 + 42*x^6 + 132*x^7 + 429*x^8
             + 1430*x^9 + 4862*x^10 + 16796*x^11 + 58786*x^12 + 208012*x^13
             + 742900*x^14 + 2674440*x^15 + 9694845*x^16 + 35357670*x^17
             + 129644790*x^18 + 477638700*x^19 + O(x^20)
            sage: (x - x^2).reverse(precision=3)
            x + x^2 + O(x^3)

        TESTS::

            sage: R.<x> = PowerSeriesRing(QQ, implementation='pari')
            sage: f = 1 + 2*x + 3*x^2 - x^4 + O(x^5)
            sage: f.reverse()
            Traceback (most recent call last):
            ...
            PariError: domain error in serreverse: valuation != 1"""
    @overload
    def reverse(self) -> Any:
        """PowerSeries_pari.reverse(self, precision=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_pari.pyx (starting at line 840)

        Return the reverse of ``self``.

        The reverse of a power series `f` is the power series `g` such
        that `g(f(x)) = x`.  This exists if and only if the valuation
        of ``self`` is exactly 1 and the coefficient of `x` is a unit.

        If the optional argument ``precision`` is given, the reverse
        is returned with this precision.  If ``f`` has infinite
        precision and the argument ``precision`` is not given, then
        the reverse is returned with the default precision of
        ``f.parent()``.

        EXAMPLES::

            sage: R.<x> = PowerSeriesRing(QQ, implementation='pari')
            sage: f = 2*x + 3*x^2 - x^4 + O(x^5)
            sage: g = f.reverse()
            sage: g
            1/2*x - 3/8*x^2 + 9/16*x^3 - 131/128*x^4 + O(x^5)
            sage: f(g)
            x + O(x^5)
            sage: g(f)
            x + O(x^5)

            sage: A.<t> = PowerSeriesRing(ZZ, implementation='pari')
            sage: a = t - t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + t^2 + 2*t^3 + 7*t^4 + 25*t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

            sage: B.<b,c> = PolynomialRing(ZZ)
            sage: A.<t> = PowerSeriesRing(B, implementation='pari')
            sage: f = t + b*t^2 + c*t^3 + O(t^4)
            sage: g = f.reverse(); g
            t - b*t^2 + (2*b^2 - c)*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

            sage: A.<t> = PowerSeriesRing(ZZ, implementation='pari')
            sage: B.<x> = PowerSeriesRing(A, implementation='pari')
            sage: f = (1 - 3*t + 4*t^3 + O(t^4))*x + (2 + t + t^2 + O(t^3))*x^2 + O(x^3)
            sage: g = f.reverse(); g
            (1 + 3*t + 9*t^2 + 23*t^3 + O(t^4))*x + (-2 - 19*t - 118*t^2 + O(t^3))*x^2 + O(x^3)

        The optional argument ``precision`` sets the precision of the output::

            sage: R.<x> = PowerSeriesRing(QQ, implementation='pari')
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

            sage: R.<x> = PowerSeriesRing(QQ, default_prec=20, implementation='pari')
            sage: (x - x^2).reverse()  # get some Catalan numbers
            x + x^2 + 2*x^3 + 5*x^4 + 14*x^5 + 42*x^6 + 132*x^7 + 429*x^8
             + 1430*x^9 + 4862*x^10 + 16796*x^11 + 58786*x^12 + 208012*x^13
             + 742900*x^14 + 2674440*x^15 + 9694845*x^16 + 35357670*x^17
             + 129644790*x^18 + 477638700*x^19 + O(x^20)
            sage: (x - x^2).reverse(precision=3)
            x + x^2 + O(x^3)

        TESTS::

            sage: R.<x> = PowerSeriesRing(QQ, implementation='pari')
            sage: f = 1 + 2*x + 3*x^2 - x^4 + O(x^5)
            sage: f.reverse()
            Traceback (most recent call last):
            ...
            PariError: domain error in serreverse: valuation != 1"""
    @overload
    def reverse(self, precision=...) -> Any:
        """PowerSeries_pari.reverse(self, precision=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_pari.pyx (starting at line 840)

        Return the reverse of ``self``.

        The reverse of a power series `f` is the power series `g` such
        that `g(f(x)) = x`.  This exists if and only if the valuation
        of ``self`` is exactly 1 and the coefficient of `x` is a unit.

        If the optional argument ``precision`` is given, the reverse
        is returned with this precision.  If ``f`` has infinite
        precision and the argument ``precision`` is not given, then
        the reverse is returned with the default precision of
        ``f.parent()``.

        EXAMPLES::

            sage: R.<x> = PowerSeriesRing(QQ, implementation='pari')
            sage: f = 2*x + 3*x^2 - x^4 + O(x^5)
            sage: g = f.reverse()
            sage: g
            1/2*x - 3/8*x^2 + 9/16*x^3 - 131/128*x^4 + O(x^5)
            sage: f(g)
            x + O(x^5)
            sage: g(f)
            x + O(x^5)

            sage: A.<t> = PowerSeriesRing(ZZ, implementation='pari')
            sage: a = t - t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + t^2 + 2*t^3 + 7*t^4 + 25*t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

            sage: B.<b,c> = PolynomialRing(ZZ)
            sage: A.<t> = PowerSeriesRing(B, implementation='pari')
            sage: f = t + b*t^2 + c*t^3 + O(t^4)
            sage: g = f.reverse(); g
            t - b*t^2 + (2*b^2 - c)*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

            sage: A.<t> = PowerSeriesRing(ZZ, implementation='pari')
            sage: B.<x> = PowerSeriesRing(A, implementation='pari')
            sage: f = (1 - 3*t + 4*t^3 + O(t^4))*x + (2 + t + t^2 + O(t^3))*x^2 + O(x^3)
            sage: g = f.reverse(); g
            (1 + 3*t + 9*t^2 + 23*t^3 + O(t^4))*x + (-2 - 19*t - 118*t^2 + O(t^3))*x^2 + O(x^3)

        The optional argument ``precision`` sets the precision of the output::

            sage: R.<x> = PowerSeriesRing(QQ, implementation='pari')
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

            sage: R.<x> = PowerSeriesRing(QQ, default_prec=20, implementation='pari')
            sage: (x - x^2).reverse()  # get some Catalan numbers
            x + x^2 + 2*x^3 + 5*x^4 + 14*x^5 + 42*x^6 + 132*x^7 + 429*x^8
             + 1430*x^9 + 4862*x^10 + 16796*x^11 + 58786*x^12 + 208012*x^13
             + 742900*x^14 + 2674440*x^15 + 9694845*x^16 + 35357670*x^17
             + 129644790*x^18 + 477638700*x^19 + O(x^20)
            sage: (x - x^2).reverse(precision=3)
            x + x^2 + O(x^3)

        TESTS::

            sage: R.<x> = PowerSeriesRing(QQ, implementation='pari')
            sage: f = 1 + 2*x + 3*x^2 - x^4 + O(x^5)
            sage: f.reverse()
            Traceback (most recent call last):
            ...
            PariError: domain error in serreverse: valuation != 1"""
    @overload
    def reverse(self) -> Any:
        """PowerSeries_pari.reverse(self, precision=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_pari.pyx (starting at line 840)

        Return the reverse of ``self``.

        The reverse of a power series `f` is the power series `g` such
        that `g(f(x)) = x`.  This exists if and only if the valuation
        of ``self`` is exactly 1 and the coefficient of `x` is a unit.

        If the optional argument ``precision`` is given, the reverse
        is returned with this precision.  If ``f`` has infinite
        precision and the argument ``precision`` is not given, then
        the reverse is returned with the default precision of
        ``f.parent()``.

        EXAMPLES::

            sage: R.<x> = PowerSeriesRing(QQ, implementation='pari')
            sage: f = 2*x + 3*x^2 - x^4 + O(x^5)
            sage: g = f.reverse()
            sage: g
            1/2*x - 3/8*x^2 + 9/16*x^3 - 131/128*x^4 + O(x^5)
            sage: f(g)
            x + O(x^5)
            sage: g(f)
            x + O(x^5)

            sage: A.<t> = PowerSeriesRing(ZZ, implementation='pari')
            sage: a = t - t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + t^2 + 2*t^3 + 7*t^4 + 25*t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

            sage: B.<b,c> = PolynomialRing(ZZ)
            sage: A.<t> = PowerSeriesRing(B, implementation='pari')
            sage: f = t + b*t^2 + c*t^3 + O(t^4)
            sage: g = f.reverse(); g
            t - b*t^2 + (2*b^2 - c)*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

            sage: A.<t> = PowerSeriesRing(ZZ, implementation='pari')
            sage: B.<x> = PowerSeriesRing(A, implementation='pari')
            sage: f = (1 - 3*t + 4*t^3 + O(t^4))*x + (2 + t + t^2 + O(t^3))*x^2 + O(x^3)
            sage: g = f.reverse(); g
            (1 + 3*t + 9*t^2 + 23*t^3 + O(t^4))*x + (-2 - 19*t - 118*t^2 + O(t^3))*x^2 + O(x^3)

        The optional argument ``precision`` sets the precision of the output::

            sage: R.<x> = PowerSeriesRing(QQ, implementation='pari')
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

            sage: R.<x> = PowerSeriesRing(QQ, default_prec=20, implementation='pari')
            sage: (x - x^2).reverse()  # get some Catalan numbers
            x + x^2 + 2*x^3 + 5*x^4 + 14*x^5 + 42*x^6 + 132*x^7 + 429*x^8
             + 1430*x^9 + 4862*x^10 + 16796*x^11 + 58786*x^12 + 208012*x^13
             + 742900*x^14 + 2674440*x^15 + 9694845*x^16 + 35357670*x^17
             + 129644790*x^18 + 477638700*x^19 + O(x^20)
            sage: (x - x^2).reverse(precision=3)
            x + x^2 + O(x^3)

        TESTS::

            sage: R.<x> = PowerSeriesRing(QQ, implementation='pari')
            sage: f = 1 + 2*x + 3*x^2 - x^4 + O(x^5)
            sage: f.reverse()
            Traceback (most recent call last):
            ...
            PariError: domain error in serreverse: valuation != 1"""
    @overload
    def valuation(self) -> Any:
        """PowerSeries_pari.valuation(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_pari.pyx (starting at line 258)

        Return the valuation of ``self``.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(QQ, implementation='pari')
            sage: (5 - t^8 + O(t^11)).valuation()
            0
            sage: (-t^8 + O(t^11)).valuation()
            8
            sage: O(t^7).valuation()
            7
            sage: R(0).valuation()
            +Infinity"""
    @overload
    def valuation(self) -> Any:
        """PowerSeries_pari.valuation(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_pari.pyx (starting at line 258)

        Return the valuation of ``self``.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(QQ, implementation='pari')
            sage: (5 - t^8 + O(t^11)).valuation()
            0
            sage: (-t^8 + O(t^11)).valuation()
            8
            sage: O(t^7).valuation()
            7
            sage: R(0).valuation()
            +Infinity"""
    @overload
    def valuation(self) -> Any:
        """PowerSeries_pari.valuation(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_pari.pyx (starting at line 258)

        Return the valuation of ``self``.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(QQ, implementation='pari')
            sage: (5 - t^8 + O(t^11)).valuation()
            0
            sage: (-t^8 + O(t^11)).valuation()
            8
            sage: O(t^7).valuation()
            7
            sage: R(0).valuation()
            +Infinity"""
    @overload
    def valuation(self) -> Any:
        """PowerSeries_pari.valuation(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_pari.pyx (starting at line 258)

        Return the valuation of ``self``.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(QQ, implementation='pari')
            sage: (5 - t^8 + O(t^11)).valuation()
            0
            sage: (-t^8 + O(t^11)).valuation()
            8
            sage: O(t^7).valuation()
            7
            sage: R(0).valuation()
            +Infinity"""
    @overload
    def valuation(self) -> Any:
        """PowerSeries_pari.valuation(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_pari.pyx (starting at line 258)

        Return the valuation of ``self``.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(QQ, implementation='pari')
            sage: (5 - t^8 + O(t^11)).valuation()
            0
            sage: (-t^8 + O(t^11)).valuation()
            8
            sage: O(t^7).valuation()
            7
            sage: R(0).valuation()
            +Infinity"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __call__(self, *x, **kwds) -> Any:
        """PowerSeries_pari.__call__(self, *x, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_pari.pyx (starting at line 294)

        Evaluate ``self`` at `x = a`.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(ZZ, implementation='pari')
            sage: f = t^2 + t^3 + O(t^6)
            sage: f(t^3)
            t^6 + t^9 + O(t^18)
            sage: f(t=t^3)
            t^6 + t^9 + O(t^18)
            sage: f(f)
            t^4 + 2*t^5 + 2*t^6 + 3*t^7 + O(t^8)
            sage: f(f)(f) == f(f(f))
            True

        The following demonstrates that the problems raised in
        :issue:`3979` and :issue:`5367` are solved::

            sage: [f(t^2 + O(t^n)) for n in [9, 10, 11]]
            [t^4 + t^6 + O(t^11), t^4 + t^6 + O(t^12), t^4 + t^6 + O(t^12)]
            sage: f(t^2)
            t^4 + t^6 + O(t^12)

        It is possible to substitute a series for which only
        the precision is defined::

            sage: f(O(t^5))
            O(t^10)

        or to substitute a polynomial (the result belonging to the power
        series ring over the same base ring)::

            sage: P.<z> = ZZ[]
            sage: g = f(z + z^3); g
            z^2 + z^3 + 2*z^4 + 3*z^5 + O(z^6)
            sage: g.parent()
            Power Series Ring in z over Integer Ring

        A series defined over another ring can be substituted::

            sage: S.<u> = PowerSeriesRing(GF(7), implementation='pari')
            sage: f(2*u + u^3 + O(u^5))
            4*u^2 + u^3 + 4*u^4 + 5*u^5 + O(u^6)

        Substituting `p`-adic numbers::

            sage: # needs sage.rings.padics
            sage: f(100 + O(5^7))
            5^4 + 3*5^5 + 4*5^6 + 2*5^7 + 2*5^8 + O(5^9)
            sage: ff = PowerSeriesRing(pAdicRing(5), 't', implementation='pari')(f)
            sage: ff
            (1 + O(5^20))*t^2 + (1 + O(5^20))*t^3 + O(t^6)
            sage: ff(100 + O(5^7))
            5^4 + 3*5^5 + 4*5^6 + 2*5^7 + 2*5^8 + O(5^9)
            sage: ff(100 + O(2^7))
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents:
             '5-adic Ring with capped relative precision 20' and
             '2-adic Ring with capped relative precision 20'

        The argument must have valuation at least 1, unless the series
        is actually a polynomial::

            sage: f(0)
            0
            sage: f(1 + t)
            Traceback (most recent call last):
            ...
            ValueError: can only substitute elements of positive valuation
            sage: f(t^-2)
            Traceback (most recent call last):
            ...
            ValueError: can only substitute elements of positive valuation
            sage: f(2 + O(5^3))                                                         # needs sage.rings.padics
            Traceback (most recent call last):
            ...
            ValueError: can only substitute elements of positive valuation
            sage: g = t^2 + t^3
            sage: g(1 + t + O(t^2))
            2 + 5*t + O(t^2)
            sage: g(3)
            36

        Substitution of variables belonging to the base ring can be
        done using keywords::

            sage: P.<a> = GF(5)[]
            sage: Q.<x> = PowerSeriesRing(P, implementation='pari')
            sage: h = (1 - a*x)^-1 + O(x^7); h
            1 + a*x + a^2*x^2 + a^3*x^3 + a^4*x^4 + a^5*x^5 + a^6*x^6 + O(x^7)
            sage: h(x^2, a=3)
            1 + 3*x^2 + 4*x^4 + 2*x^6 + x^8 + 3*x^10 + 4*x^12 + O(x^14)"""
    def __getitem__(self, n) -> Any:
        """PowerSeries_pari.__getitem__(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_pari.pyx (starting at line 449)

        Return the ``n``-th coefficient of ``self``.

        If ``n`` is a slice object, this returns a power series of the
        same precision, whose coefficients are the same as ``self``
        for those indices in the slice, and 0 otherwise.

        Returns 0 for negative coefficients.  Raises an :exc:`IndexError`
        if trying to access beyond known coefficients.

        EXAMPLES::

            sage: R.<t> = PowerSeriesRing(QQ, implementation='pari')
            sage: f = 3/2 - 17/5*t^3 + O(t^5)
            sage: f[3]
            -17/5
            sage: f[-2]
            0
            sage: f[4]
            0
            sage: f[5]
            Traceback (most recent call last):
            ...
            IndexError: index out of range

            sage: R.<t> = PowerSeriesRing(ZZ, implementation='pari')
            sage: f = (2-t)^5; f
            32 - 80*t + 80*t^2 - 40*t^3 + 10*t^4 - t^5
            sage: f[:4]
            32 - 80*t + 80*t^2 - 40*t^3

            sage: f = 1 + t^3 - 4*t^4 + O(t^7); f
            1 + t^3 - 4*t^4 + O(t^7)
            sage: f[:4]
            1 + t^3 + O(t^7)"""
    def __hash__(self) -> Any:
        """PowerSeries_pari.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_pari.pyx (starting at line 206)

        Return a hash of ``self``.

        TESTS::

            sage: R.<t> = PowerSeriesRing(ZZ, implementation='pari')
            sage: hash(t^2 + 1) == hash(pari(t^2 + 1))
            True"""
    def __invert__(self) -> Any:
        """PowerSeries_pari.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_pari.pyx (starting at line 500)

        Return the multiplicative inverse of ``self``.

        TESTS::

            sage: R.<t> = PowerSeriesRing(QQ, default_prec=6, implementation='pari')
            sage: ~(R(1-t))
            1 + t + t^2 + t^3 + t^4 + t^5 + O(t^6)"""
    def __neg__(self) -> Any:
        """PowerSeries_pari.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_pari.pyx (starting at line 515)

        Return the negative of ``self``.

        TESTS::

            sage: R.<t> = PowerSeriesRing(QQ, implementation='pari')
            sage: f = t + 17/5*t^3 + 2*t^4 + O(t^5)
            sage: -f
            -t - 17/5*t^3 - 2*t^4 + O(t^5)"""
    @overload
    def __pari__(self) -> Any:
        """PowerSeries_pari.__pari__(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_pari.pyx (starting at line 233)

        Convert ``self`` to a PARI object.

        TESTS::

            sage: R.<t> = PowerSeriesRing(GF(7), implementation='pari')
            sage: (3 - t^3 + O(t^5)).__pari__()
            Mod(3, 7) + Mod(6, 7)*t^3 + O(t^5)"""
    @overload
    def __pari__(self) -> Any:
        """PowerSeries_pari.__pari__(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_pari.pyx (starting at line 233)

        Convert ``self`` to a PARI object.

        TESTS::

            sage: R.<t> = PowerSeriesRing(GF(7), implementation='pari')
            sage: (3 - t^3 + O(t^5)).__pari__()
            Mod(3, 7) + Mod(6, 7)*t^3 + O(t^5)"""
    def __pow__(self, PowerSeries_pariself, n, m) -> Any:
        """PowerSeries_pari.__pow__(PowerSeries_pari self, n, m)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_pari.pyx (starting at line 528)

        Exponentiation of power series.

        TESTS::

            sage: R.<t> = PowerSeriesRing(QQ, implementation='pari')
            sage: f = 3 - t^3 + O(t^5)
            sage: a = f^3; a
            27 - 27*t^3 + O(t^5)
            sage: b = f^-3; b
            1/27 + 1/27*t^3 + O(t^5)"""
    def __reduce__(self) -> Any:
        """PowerSeries_pari.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_pari.pyx (starting at line 218)

        Used for pickling.

        EXAMPLES::

            sage: A.<z> = PowerSeriesRing(RR, implementation='pari')
            sage: f = z - z^3 + O(z^10)
            sage: z == loads(dumps(z))
            True
            sage: f == loads(dumps(f))
            True"""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
