import _cython_3_2_1
import sage.categories.action
import sage.rings.power_series_ring_element
from sage.rings.infinity import infinity as infinity
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

make_powerseries_poly_v0: _cython_3_2_1.cython_function_or_method

class BaseRingFloorDivAction(sage.categories.action.Action):
    """File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 1254)

        The floor division action of the base ring on a formal power series.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class PowerSeries_poly(sage.rings.power_series_ring_element.PowerSeries):
    """PowerSeries_poly(parent, f=0, prec=infinity, int check=1, is_gen=0)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, f=..., prec=..., intcheck=..., is_gen=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 20)

                EXAMPLES::

                    sage: R.<q> = PowerSeriesRing(CC); R                                        # needs sage.rings.real_mpfr
                    Power Series Ring in q over Complex Field with 53 bits of precision
                    sage: loads(q.dumps()) == q                                                 # needs sage.rings.real_mpfr
                    True

                    sage: R.<t> = QQ[[]]
                    sage: f = 3 - t^3 + O(t^5)
                    sage: a = f^3; a
                    27 - 27*t^3 + O(t^5)
                    sage: b = f^-3; b
                    1/27 + 1/27*t^3 + O(t^5)
                    sage: a*b
                    1 + O(t^5)

                Check that :issue:`22216` is fixed::

                    sage: R.<T> = PowerSeriesRing(QQ)
                    sage: R(pari('1 + O(T)'))                                                   # needs sage.libs.pari
                    1 + O(T)
                    sage: R(pari('1/T + O(T)'))                                                 # needs sage.libs.pari
                    Traceback (most recent call last):
                    ...
                    ValueError: series has negative valuation
        """
    @overload
    def degree(self) -> Any:
        """PowerSeries_poly.degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 140)

        Return the degree of the underlying polynomial of ``self``.

        That is, if ``self`` is of the form `f(x) + O(x^n)`, we return
        the degree of `f(x)`. Note that if `f(x)` is `0`, we return `-1`,
        just as with polynomials.

        EXAMPLES::

            sage: R.<t> = ZZ[[]]
            sage: (5 + t^3 + O(t^4)).degree()
            3
            sage: (5 + O(t^4)).degree()
            0
            sage: O(t^4).degree()
            -1"""
    @overload
    def degree(self) -> Any:
        """PowerSeries_poly.degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 140)

        Return the degree of the underlying polynomial of ``self``.

        That is, if ``self`` is of the form `f(x) + O(x^n)`, we return
        the degree of `f(x)`. Note that if `f(x)` is `0`, we return `-1`,
        just as with polynomials.

        EXAMPLES::

            sage: R.<t> = ZZ[[]]
            sage: (5 + t^3 + O(t^4)).degree()
            3
            sage: (5 + O(t^4)).degree()
            0
            sage: O(t^4).degree()
            -1"""
    @overload
    def degree(self) -> Any:
        """PowerSeries_poly.degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 140)

        Return the degree of the underlying polynomial of ``self``.

        That is, if ``self`` is of the form `f(x) + O(x^n)`, we return
        the degree of `f(x)`. Note that if `f(x)` is `0`, we return `-1`,
        just as with polynomials.

        EXAMPLES::

            sage: R.<t> = ZZ[[]]
            sage: (5 + t^3 + O(t^4)).degree()
            3
            sage: (5 + O(t^4)).degree()
            0
            sage: O(t^4).degree()
            -1"""
    @overload
    def degree(self) -> Any:
        """PowerSeries_poly.degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 140)

        Return the degree of the underlying polynomial of ``self``.

        That is, if ``self`` is of the form `f(x) + O(x^n)`, we return
        the degree of `f(x)`. Note that if `f(x)` is `0`, we return `-1`,
        just as with polynomials.

        EXAMPLES::

            sage: R.<t> = ZZ[[]]
            sage: (5 + t^3 + O(t^4)).degree()
            3
            sage: (5 + O(t^4)).degree()
            0
            sage: O(t^4).degree()
            -1"""
    def dict(self) -> Any:
        """PowerSeries_poly.monomial_coefficients(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 798)

        Return a dictionary of coefficients for ``self``.

        This is simply a dict for the underlying polynomial, so need
        not have keys corresponding to every number smaller than
        ``self.prec()``.

        EXAMPLES::

            sage: R.<t> = ZZ[[]]
            sage: f = 1 + t^10 + O(t^12)
            sage: f.monomial_coefficients()
            {0: 1, 10: 1}

        ``dict`` is an alias::

            sage: f.dict()
            {0: 1, 10: 1}"""
    @overload
    def integral(self, var=...) -> Any:
        """PowerSeries_poly.integral(self, var=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 878)

        Return the integral of this power series.

        By default, the integration variable is the variable of the
        power series.

        Otherwise, the integration variable is the optional parameter ``var``.

        .. NOTE::

            The integral is always chosen so the constant term is 0.

        EXAMPLES::

            sage: k.<w> = QQ[[]]
            sage: (1+17*w+15*w^3+O(w^5)).integral()
            w + 17/2*w^2 + 15/4*w^4 + O(w^6)
            sage: (w^3 + 4*w^4 + O(w^7)).integral()
            1/4*w^4 + 4/5*w^5 + O(w^8)
            sage: (3*w^2).integral()
            w^3

        TESTS::

            sage: t = PowerSeriesRing(QQ,'t').gen()
            sage: f = t + 5*t^2 + 21*t^3
            sage: g = f.integral(); g
            1/2*t^2 + 5/3*t^3 + 21/4*t^4
            sage: g.parent()
            Power Series Ring in t over Rational Field

            sage: R.<x> = QQ[]
            sage: t = PowerSeriesRing(R,'t').gen()
            sage: f = x*t +5*t^2
            sage: f.integral()
            1/2*x*t^2 + 5/3*t^3
            sage: f.integral(x)
            1/2*x^2*t + 5*x*t^2"""
    @overload
    def integral(self) -> Any:
        """PowerSeries_poly.integral(self, var=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 878)

        Return the integral of this power series.

        By default, the integration variable is the variable of the
        power series.

        Otherwise, the integration variable is the optional parameter ``var``.

        .. NOTE::

            The integral is always chosen so the constant term is 0.

        EXAMPLES::

            sage: k.<w> = QQ[[]]
            sage: (1+17*w+15*w^3+O(w^5)).integral()
            w + 17/2*w^2 + 15/4*w^4 + O(w^6)
            sage: (w^3 + 4*w^4 + O(w^7)).integral()
            1/4*w^4 + 4/5*w^5 + O(w^8)
            sage: (3*w^2).integral()
            w^3

        TESTS::

            sage: t = PowerSeriesRing(QQ,'t').gen()
            sage: f = t + 5*t^2 + 21*t^3
            sage: g = f.integral(); g
            1/2*t^2 + 5/3*t^3 + 21/4*t^4
            sage: g.parent()
            Power Series Ring in t over Rational Field

            sage: R.<x> = QQ[]
            sage: t = PowerSeriesRing(R,'t').gen()
            sage: f = x*t +5*t^2
            sage: f.integral()
            1/2*x*t^2 + 5/3*t^3
            sage: f.integral(x)
            1/2*x^2*t + 5*x*t^2"""
    @overload
    def integral(self) -> Any:
        """PowerSeries_poly.integral(self, var=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 878)

        Return the integral of this power series.

        By default, the integration variable is the variable of the
        power series.

        Otherwise, the integration variable is the optional parameter ``var``.

        .. NOTE::

            The integral is always chosen so the constant term is 0.

        EXAMPLES::

            sage: k.<w> = QQ[[]]
            sage: (1+17*w+15*w^3+O(w^5)).integral()
            w + 17/2*w^2 + 15/4*w^4 + O(w^6)
            sage: (w^3 + 4*w^4 + O(w^7)).integral()
            1/4*w^4 + 4/5*w^5 + O(w^8)
            sage: (3*w^2).integral()
            w^3

        TESTS::

            sage: t = PowerSeriesRing(QQ,'t').gen()
            sage: f = t + 5*t^2 + 21*t^3
            sage: g = f.integral(); g
            1/2*t^2 + 5/3*t^3 + 21/4*t^4
            sage: g.parent()
            Power Series Ring in t over Rational Field

            sage: R.<x> = QQ[]
            sage: t = PowerSeriesRing(R,'t').gen()
            sage: f = x*t +5*t^2
            sage: f.integral()
            1/2*x*t^2 + 5/3*t^3
            sage: f.integral(x)
            1/2*x^2*t + 5*x*t^2"""
    @overload
    def integral(self) -> Any:
        """PowerSeries_poly.integral(self, var=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 878)

        Return the integral of this power series.

        By default, the integration variable is the variable of the
        power series.

        Otherwise, the integration variable is the optional parameter ``var``.

        .. NOTE::

            The integral is always chosen so the constant term is 0.

        EXAMPLES::

            sage: k.<w> = QQ[[]]
            sage: (1+17*w+15*w^3+O(w^5)).integral()
            w + 17/2*w^2 + 15/4*w^4 + O(w^6)
            sage: (w^3 + 4*w^4 + O(w^7)).integral()
            1/4*w^4 + 4/5*w^5 + O(w^8)
            sage: (3*w^2).integral()
            w^3

        TESTS::

            sage: t = PowerSeriesRing(QQ,'t').gen()
            sage: f = t + 5*t^2 + 21*t^3
            sage: g = f.integral(); g
            1/2*t^2 + 5/3*t^3 + 21/4*t^4
            sage: g.parent()
            Power Series Ring in t over Rational Field

            sage: R.<x> = QQ[]
            sage: t = PowerSeriesRing(R,'t').gen()
            sage: f = x*t +5*t^2
            sage: f.integral()
            1/2*x*t^2 + 5/3*t^3
            sage: f.integral(x)
            1/2*x^2*t + 5*x*t^2"""
    @overload
    def integral(self) -> Any:
        """PowerSeries_poly.integral(self, var=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 878)

        Return the integral of this power series.

        By default, the integration variable is the variable of the
        power series.

        Otherwise, the integration variable is the optional parameter ``var``.

        .. NOTE::

            The integral is always chosen so the constant term is 0.

        EXAMPLES::

            sage: k.<w> = QQ[[]]
            sage: (1+17*w+15*w^3+O(w^5)).integral()
            w + 17/2*w^2 + 15/4*w^4 + O(w^6)
            sage: (w^3 + 4*w^4 + O(w^7)).integral()
            1/4*w^4 + 4/5*w^5 + O(w^8)
            sage: (3*w^2).integral()
            w^3

        TESTS::

            sage: t = PowerSeriesRing(QQ,'t').gen()
            sage: f = t + 5*t^2 + 21*t^3
            sage: g = f.integral(); g
            1/2*t^2 + 5/3*t^3 + 21/4*t^4
            sage: g.parent()
            Power Series Ring in t over Rational Field

            sage: R.<x> = QQ[]
            sage: t = PowerSeriesRing(R,'t').gen()
            sage: f = x*t +5*t^2
            sage: f.integral()
            1/2*x*t^2 + 5/3*t^3
            sage: f.integral(x)
            1/2*x^2*t + 5*x*t^2"""
    @overload
    def integral(self) -> Any:
        """PowerSeries_poly.integral(self, var=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 878)

        Return the integral of this power series.

        By default, the integration variable is the variable of the
        power series.

        Otherwise, the integration variable is the optional parameter ``var``.

        .. NOTE::

            The integral is always chosen so the constant term is 0.

        EXAMPLES::

            sage: k.<w> = QQ[[]]
            sage: (1+17*w+15*w^3+O(w^5)).integral()
            w + 17/2*w^2 + 15/4*w^4 + O(w^6)
            sage: (w^3 + 4*w^4 + O(w^7)).integral()
            1/4*w^4 + 4/5*w^5 + O(w^8)
            sage: (3*w^2).integral()
            w^3

        TESTS::

            sage: t = PowerSeriesRing(QQ,'t').gen()
            sage: f = t + 5*t^2 + 21*t^3
            sage: g = f.integral(); g
            1/2*t^2 + 5/3*t^3 + 21/4*t^4
            sage: g.parent()
            Power Series Ring in t over Rational Field

            sage: R.<x> = QQ[]
            sage: t = PowerSeriesRing(R,'t').gen()
            sage: f = x*t +5*t^2
            sage: f.integral()
            1/2*x*t^2 + 5/3*t^3
            sage: f.integral(x)
            1/2*x^2*t + 5*x*t^2"""
    @overload
    def integral(self, x) -> Any:
        """PowerSeries_poly.integral(self, var=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 878)

        Return the integral of this power series.

        By default, the integration variable is the variable of the
        power series.

        Otherwise, the integration variable is the optional parameter ``var``.

        .. NOTE::

            The integral is always chosen so the constant term is 0.

        EXAMPLES::

            sage: k.<w> = QQ[[]]
            sage: (1+17*w+15*w^3+O(w^5)).integral()
            w + 17/2*w^2 + 15/4*w^4 + O(w^6)
            sage: (w^3 + 4*w^4 + O(w^7)).integral()
            1/4*w^4 + 4/5*w^5 + O(w^8)
            sage: (3*w^2).integral()
            w^3

        TESTS::

            sage: t = PowerSeriesRing(QQ,'t').gen()
            sage: f = t + 5*t^2 + 21*t^3
            sage: g = f.integral(); g
            1/2*t^2 + 5/3*t^3 + 21/4*t^4
            sage: g.parent()
            Power Series Ring in t over Rational Field

            sage: R.<x> = QQ[]
            sage: t = PowerSeriesRing(R,'t').gen()
            sage: f = x*t +5*t^2
            sage: f.integral()
            1/2*x*t^2 + 5/3*t^3
            sage: f.integral(x)
            1/2*x^2*t + 5*x*t^2"""
    @overload
    def list(self) -> Any:
        """PowerSeries_poly.list(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 781)

        Return the list of known coefficients for ``self``.

        This is just the list of coefficients of the underlying
        polynomial, so in particular, need not have length equal to
        ``self.prec()``.

        EXAMPLES::

            sage: R.<t> = ZZ[[]]
            sage: f = 1 - 5*t^3 + t^5 + O(t^7)
            sage: f.list()
            [1, 0, 0, -5, 0, 1]"""
    @overload
    def list(self) -> Any:
        """PowerSeries_poly.list(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 781)

        Return the list of known coefficients for ``self``.

        This is just the list of coefficients of the underlying
        polynomial, so in particular, need not have length equal to
        ``self.prec()``.

        EXAMPLES::

            sage: R.<t> = ZZ[[]]
            sage: f = 1 - 5*t^3 + t^5 + O(t^7)
            sage: f.list()
            [1, 0, 0, -5, 0, 1]"""
    @overload
    def monomial_coefficients(self, copy=...) -> Any:
        """PowerSeries_poly.monomial_coefficients(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 798)

        Return a dictionary of coefficients for ``self``.

        This is simply a dict for the underlying polynomial, so need
        not have keys corresponding to every number smaller than
        ``self.prec()``.

        EXAMPLES::

            sage: R.<t> = ZZ[[]]
            sage: f = 1 + t^10 + O(t^12)
            sage: f.monomial_coefficients()
            {0: 1, 10: 1}

        ``dict`` is an alias::

            sage: f.dict()
            {0: 1, 10: 1}"""
    @overload
    def monomial_coefficients(self) -> Any:
        """PowerSeries_poly.monomial_coefficients(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 798)

        Return a dictionary of coefficients for ``self``.

        This is simply a dict for the underlying polynomial, so need
        not have keys corresponding to every number smaller than
        ``self.prec()``.

        EXAMPLES::

            sage: R.<t> = ZZ[[]]
            sage: f = 1 + t^10 + O(t^12)
            sage: f.monomial_coefficients()
            {0: 1, 10: 1}

        ``dict`` is an alias::

            sage: f.dict()
            {0: 1, 10: 1}"""
    def pade(self, m, n) -> Any:
        """PowerSeries_poly.pade(self, m, n)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 1112)

        Return the Padé approximant of ``self`` of index `(m, n)`.

        The Padé approximant of index `(m, n)` of a formal power
        series `f` is the quotient `Q/P` of two polynomials `Q` and `P`
        such that `\\deg(Q)\\leq m`, `\\deg(P)\\leq n` and

        .. MATH::

            f(z) - Q(z)/P(z) = O(z^{m+n+1}).

        The formal power series `f` must be known up to order `n + m`.

        See :wikipedia:`Padé\\_approximant`

        INPUT:

        - ``m``, ``n`` -- integers, describing the degrees of the polynomials

        OUTPUT: a ratio of two polynomials

        ALGORITHM:

        This method uses the formula as a quotient of two determinants.

        .. SEEALSO::

            * :mod:`sage.matrix.berlekamp_massey`,
            * :meth:`sage.rings.polynomial.polynomial_zmod_flint.Polynomial_zmod_flint.rational_reconstruction`

        EXAMPLES::

            sage: z = PowerSeriesRing(QQ, 'z').gen()
            sage: exp(z).pade(4, 0)
            1/24*z^4 + 1/6*z^3 + 1/2*z^2 + z + 1
            sage: exp(z).pade(1, 1)
            (-z - 2)/(z - 2)
            sage: exp(z).pade(3, 3)
            (-z^3 - 12*z^2 - 60*z - 120)/(z^3 - 12*z^2 + 60*z - 120)
            sage: log(1-z).pade(4, 4)
            (25/6*z^4 - 130/3*z^3 + 105*z^2 - 70*z)/(z^4 - 20*z^3 + 90*z^2
            - 140*z + 70)
            sage: sqrt(1+z).pade(3, 2)
            (1/6*z^3 + 3*z^2 + 8*z + 16/3)/(z^2 + 16/3*z + 16/3)
            sage: exp(2*z).pade(3, 3)
            (-z^3 - 6*z^2 - 15*z - 15)/(z^3 - 6*z^2 + 15*z - 15)

        TESTS:

        With real coefficients::

            sage: # needs sage.rings.real_mpfr
            sage: R.<z> = RR[[]]
            sage: f = exp(2*z)
            sage: f.pade(3, 3) # abs tol 1e-10
            (-z^3 - 6.0*z^2 - 15.0*z - 15.0)/(z^3 - 6.0*z^2 + 15.0*z - 15.0)

        When precision is too low::

            sage: # needs sage.rings.real_mpfr
            sage: f = z + O(z**6)
            sage: f.pade(4, 4)
            Traceback (most recent call last):
            ...
            ValueError: the precision of the series is not large enough

        Check that :issue:`21212` is fixed::

            sage: QQx.<x> = QQ[[]]
            sage: (1 + x + O(x^100)).pade(2,2)
            x + 1

        Check for correct precision::

            sage: QQx.<x> = QQ[[]]
            sage: (1 + x + O(x^2)).pade(0,1)
            -1/(x - 1)"""
    @overload
    def polynomial(self) -> Any:
        """PowerSeries_poly.polynomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 106)

        Return the underlying polynomial of ``self``.

        EXAMPLES::

            sage: R.<t> = GF(7)[[]]
            sage: f = 3 - t^3 + O(t^5)
            sage: f.polynomial()
            6*t^3 + 3"""
    @overload
    def polynomial(self) -> Any:
        """PowerSeries_poly.polynomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 106)

        Return the underlying polynomial of ``self``.

        EXAMPLES::

            sage: R.<t> = GF(7)[[]]
            sage: f = 3 - t^3 + O(t^5)
            sage: f.polynomial()
            6*t^3 + 3"""
    @overload
    def reverse(self, precision=...) -> Any:
        """PowerSeries_poly.reverse(self, precision=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 921)

        Return the reverse of `f`, i.e., the series `g` such that `g(f(x)) = x`.

        Given an optional argument ``precision``, return the reverse with given
        precision (note that the reverse can have precision at most
        ``f.prec()``).  If `f` has infinite precision, and the argument
        ``precision`` is not given, then the precision of the reverse defaults
        to the default precision of ``f.parent()``.

        Note that this is only possible if the valuation of ``self`` is exactly
        1.

        ALGORITHM:

        We first attempt to pass the computation to pari; if this fails, we
        use Lagrange inversion.  Using ``sage: set_verbose(1)`` will print
        a message if passing to pari fails.

        If the base ring has positive characteristic, then we attempt to
        lift to a characteristic zero ring and perform the reverse there.
        If this fails, an error is raised.

        EXAMPLES::

            sage: R.<x> = PowerSeriesRing(QQ)
            sage: f = 2*x + 3*x^2 - x^4 + O(x^5)
            sage: g = f.reverse()
            sage: g
            1/2*x - 3/8*x^2 + 9/16*x^3 - 131/128*x^4 + O(x^5)
            sage: f(g)
            x + O(x^5)
            sage: g(f)
            x + O(x^5)

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: a = t - t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + t^2 + 2*t^3 + 7*t^4 + 25*t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

            sage: B.<b,c> = PolynomialRing(ZZ)
            sage: A.<t> = PowerSeriesRing(B)
            sage: f = t + b*t^2 + c*t^3 + O(t^4)
            sage: g = f.reverse(); g
            t - b*t^2 + (2*b^2 - c)*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: B.<s> = A[[]]
            sage: f = (1 - 3*t + 4*t^3 + O(t^4))*s + (2 + t + t^2 + O(t^3))*s^2 + O(s^3)
            sage: from sage.misc.verbose import set_verbose
            sage: set_verbose(1)
            sage: g = f.reverse(); g
            verbose 1 (<module>) passing to pari failed; trying Lagrange inversion
            (1 + 3*t + 9*t^2 + 23*t^3 + O(t^4))*s + (-2 - 19*t - 118*t^2 + O(t^3))*s^2 + O(s^3)
            sage: set_verbose(0)
            sage: f(g) == g(f) == s
            True

        If the leading coefficient is not a unit, we pass to its fraction
        field if possible::

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: a = 2*t - 4*t^2 + t^4 - t^5 + O(t^6)
            sage: a.reverse()
            1/2*t + 1/2*t^2 + t^3 + 79/32*t^4 + 437/64*t^5 + O(t^6)

            sage: B.<b> = PolynomialRing(ZZ)
            sage: A.<t> = PowerSeriesRing(B)
            sage: f = 2*b*t + b*t^2 + 3*b^2*t^3 + O(t^4)
            sage: g = f.reverse(); g
            1/(2*b)*t - 1/(8*b^2)*t^2 + ((-3*b + 1)/(16*b^3))*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

        We can handle some base rings of positive characteristic::

            sage: A8.<t> = PowerSeriesRing(Zmod(8))
            sage: a = t - 15*t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + 7*t^2 + 2*t^3 + 5*t^4 + t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

        The optional argument ``precision`` sets the precision of the output::

            sage: R.<x> = PowerSeriesRing(QQ)
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

            sage: R.<x> = PowerSeriesRing(QQ, default_prec=20)
            sage: (x - x^2).reverse() # get some Catalan numbers
            x + x^2 + 2*x^3 + 5*x^4 + 14*x^5 + 42*x^6 + 132*x^7 + 429*x^8 + 1430*x^9
             + 4862*x^10 + 16796*x^11 + 58786*x^12 + 208012*x^13 + 742900*x^14
             + 2674440*x^15 + 9694845*x^16 + 35357670*x^17 + 129644790*x^18
             + 477638700*x^19 + O(x^20)
            sage: (x - x^2).reverse(precision=3)
            x + x^2 + O(x^3)

        TESTS::

            sage: R.<x> = PowerSeriesRing(QQ)
            sage: f = 1 + 2*x + 3*x^2 - x^4 + O(x^5)
            sage: f.reverse()
            Traceback (most recent call last):
            ...
            ValueError: Series must have valuation one for reversion.

            sage: Series = PowerSeriesRing(SR, 'x')                                     # needs sage.symbolic
            sage: ser = Series([0, pi]); ser                                            # needs sage.symbolic
            pi*x
            sage: ser.reverse()                                                         # needs sage.symbolic
            1/pi*x + O(x^20)"""
    @overload
    def reverse(self) -> Any:
        """PowerSeries_poly.reverse(self, precision=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 921)

        Return the reverse of `f`, i.e., the series `g` such that `g(f(x)) = x`.

        Given an optional argument ``precision``, return the reverse with given
        precision (note that the reverse can have precision at most
        ``f.prec()``).  If `f` has infinite precision, and the argument
        ``precision`` is not given, then the precision of the reverse defaults
        to the default precision of ``f.parent()``.

        Note that this is only possible if the valuation of ``self`` is exactly
        1.

        ALGORITHM:

        We first attempt to pass the computation to pari; if this fails, we
        use Lagrange inversion.  Using ``sage: set_verbose(1)`` will print
        a message if passing to pari fails.

        If the base ring has positive characteristic, then we attempt to
        lift to a characteristic zero ring and perform the reverse there.
        If this fails, an error is raised.

        EXAMPLES::

            sage: R.<x> = PowerSeriesRing(QQ)
            sage: f = 2*x + 3*x^2 - x^4 + O(x^5)
            sage: g = f.reverse()
            sage: g
            1/2*x - 3/8*x^2 + 9/16*x^3 - 131/128*x^4 + O(x^5)
            sage: f(g)
            x + O(x^5)
            sage: g(f)
            x + O(x^5)

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: a = t - t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + t^2 + 2*t^3 + 7*t^4 + 25*t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

            sage: B.<b,c> = PolynomialRing(ZZ)
            sage: A.<t> = PowerSeriesRing(B)
            sage: f = t + b*t^2 + c*t^3 + O(t^4)
            sage: g = f.reverse(); g
            t - b*t^2 + (2*b^2 - c)*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: B.<s> = A[[]]
            sage: f = (1 - 3*t + 4*t^3 + O(t^4))*s + (2 + t + t^2 + O(t^3))*s^2 + O(s^3)
            sage: from sage.misc.verbose import set_verbose
            sage: set_verbose(1)
            sage: g = f.reverse(); g
            verbose 1 (<module>) passing to pari failed; trying Lagrange inversion
            (1 + 3*t + 9*t^2 + 23*t^3 + O(t^4))*s + (-2 - 19*t - 118*t^2 + O(t^3))*s^2 + O(s^3)
            sage: set_verbose(0)
            sage: f(g) == g(f) == s
            True

        If the leading coefficient is not a unit, we pass to its fraction
        field if possible::

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: a = 2*t - 4*t^2 + t^4 - t^5 + O(t^6)
            sage: a.reverse()
            1/2*t + 1/2*t^2 + t^3 + 79/32*t^4 + 437/64*t^5 + O(t^6)

            sage: B.<b> = PolynomialRing(ZZ)
            sage: A.<t> = PowerSeriesRing(B)
            sage: f = 2*b*t + b*t^2 + 3*b^2*t^3 + O(t^4)
            sage: g = f.reverse(); g
            1/(2*b)*t - 1/(8*b^2)*t^2 + ((-3*b + 1)/(16*b^3))*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

        We can handle some base rings of positive characteristic::

            sage: A8.<t> = PowerSeriesRing(Zmod(8))
            sage: a = t - 15*t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + 7*t^2 + 2*t^3 + 5*t^4 + t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

        The optional argument ``precision`` sets the precision of the output::

            sage: R.<x> = PowerSeriesRing(QQ)
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

            sage: R.<x> = PowerSeriesRing(QQ, default_prec=20)
            sage: (x - x^2).reverse() # get some Catalan numbers
            x + x^2 + 2*x^3 + 5*x^4 + 14*x^5 + 42*x^6 + 132*x^7 + 429*x^8 + 1430*x^9
             + 4862*x^10 + 16796*x^11 + 58786*x^12 + 208012*x^13 + 742900*x^14
             + 2674440*x^15 + 9694845*x^16 + 35357670*x^17 + 129644790*x^18
             + 477638700*x^19 + O(x^20)
            sage: (x - x^2).reverse(precision=3)
            x + x^2 + O(x^3)

        TESTS::

            sage: R.<x> = PowerSeriesRing(QQ)
            sage: f = 1 + 2*x + 3*x^2 - x^4 + O(x^5)
            sage: f.reverse()
            Traceback (most recent call last):
            ...
            ValueError: Series must have valuation one for reversion.

            sage: Series = PowerSeriesRing(SR, 'x')                                     # needs sage.symbolic
            sage: ser = Series([0, pi]); ser                                            # needs sage.symbolic
            pi*x
            sage: ser.reverse()                                                         # needs sage.symbolic
            1/pi*x + O(x^20)"""
    @overload
    def reverse(self) -> Any:
        """PowerSeries_poly.reverse(self, precision=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 921)

        Return the reverse of `f`, i.e., the series `g` such that `g(f(x)) = x`.

        Given an optional argument ``precision``, return the reverse with given
        precision (note that the reverse can have precision at most
        ``f.prec()``).  If `f` has infinite precision, and the argument
        ``precision`` is not given, then the precision of the reverse defaults
        to the default precision of ``f.parent()``.

        Note that this is only possible if the valuation of ``self`` is exactly
        1.

        ALGORITHM:

        We first attempt to pass the computation to pari; if this fails, we
        use Lagrange inversion.  Using ``sage: set_verbose(1)`` will print
        a message if passing to pari fails.

        If the base ring has positive characteristic, then we attempt to
        lift to a characteristic zero ring and perform the reverse there.
        If this fails, an error is raised.

        EXAMPLES::

            sage: R.<x> = PowerSeriesRing(QQ)
            sage: f = 2*x + 3*x^2 - x^4 + O(x^5)
            sage: g = f.reverse()
            sage: g
            1/2*x - 3/8*x^2 + 9/16*x^3 - 131/128*x^4 + O(x^5)
            sage: f(g)
            x + O(x^5)
            sage: g(f)
            x + O(x^5)

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: a = t - t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + t^2 + 2*t^3 + 7*t^4 + 25*t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

            sage: B.<b,c> = PolynomialRing(ZZ)
            sage: A.<t> = PowerSeriesRing(B)
            sage: f = t + b*t^2 + c*t^3 + O(t^4)
            sage: g = f.reverse(); g
            t - b*t^2 + (2*b^2 - c)*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: B.<s> = A[[]]
            sage: f = (1 - 3*t + 4*t^3 + O(t^4))*s + (2 + t + t^2 + O(t^3))*s^2 + O(s^3)
            sage: from sage.misc.verbose import set_verbose
            sage: set_verbose(1)
            sage: g = f.reverse(); g
            verbose 1 (<module>) passing to pari failed; trying Lagrange inversion
            (1 + 3*t + 9*t^2 + 23*t^3 + O(t^4))*s + (-2 - 19*t - 118*t^2 + O(t^3))*s^2 + O(s^3)
            sage: set_verbose(0)
            sage: f(g) == g(f) == s
            True

        If the leading coefficient is not a unit, we pass to its fraction
        field if possible::

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: a = 2*t - 4*t^2 + t^4 - t^5 + O(t^6)
            sage: a.reverse()
            1/2*t + 1/2*t^2 + t^3 + 79/32*t^4 + 437/64*t^5 + O(t^6)

            sage: B.<b> = PolynomialRing(ZZ)
            sage: A.<t> = PowerSeriesRing(B)
            sage: f = 2*b*t + b*t^2 + 3*b^2*t^3 + O(t^4)
            sage: g = f.reverse(); g
            1/(2*b)*t - 1/(8*b^2)*t^2 + ((-3*b + 1)/(16*b^3))*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

        We can handle some base rings of positive characteristic::

            sage: A8.<t> = PowerSeriesRing(Zmod(8))
            sage: a = t - 15*t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + 7*t^2 + 2*t^3 + 5*t^4 + t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

        The optional argument ``precision`` sets the precision of the output::

            sage: R.<x> = PowerSeriesRing(QQ)
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

            sage: R.<x> = PowerSeriesRing(QQ, default_prec=20)
            sage: (x - x^2).reverse() # get some Catalan numbers
            x + x^2 + 2*x^3 + 5*x^4 + 14*x^5 + 42*x^6 + 132*x^7 + 429*x^8 + 1430*x^9
             + 4862*x^10 + 16796*x^11 + 58786*x^12 + 208012*x^13 + 742900*x^14
             + 2674440*x^15 + 9694845*x^16 + 35357670*x^17 + 129644790*x^18
             + 477638700*x^19 + O(x^20)
            sage: (x - x^2).reverse(precision=3)
            x + x^2 + O(x^3)

        TESTS::

            sage: R.<x> = PowerSeriesRing(QQ)
            sage: f = 1 + 2*x + 3*x^2 - x^4 + O(x^5)
            sage: f.reverse()
            Traceback (most recent call last):
            ...
            ValueError: Series must have valuation one for reversion.

            sage: Series = PowerSeriesRing(SR, 'x')                                     # needs sage.symbolic
            sage: ser = Series([0, pi]); ser                                            # needs sage.symbolic
            pi*x
            sage: ser.reverse()                                                         # needs sage.symbolic
            1/pi*x + O(x^20)"""
    @overload
    def reverse(self) -> Any:
        """PowerSeries_poly.reverse(self, precision=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 921)

        Return the reverse of `f`, i.e., the series `g` such that `g(f(x)) = x`.

        Given an optional argument ``precision``, return the reverse with given
        precision (note that the reverse can have precision at most
        ``f.prec()``).  If `f` has infinite precision, and the argument
        ``precision`` is not given, then the precision of the reverse defaults
        to the default precision of ``f.parent()``.

        Note that this is only possible if the valuation of ``self`` is exactly
        1.

        ALGORITHM:

        We first attempt to pass the computation to pari; if this fails, we
        use Lagrange inversion.  Using ``sage: set_verbose(1)`` will print
        a message if passing to pari fails.

        If the base ring has positive characteristic, then we attempt to
        lift to a characteristic zero ring and perform the reverse there.
        If this fails, an error is raised.

        EXAMPLES::

            sage: R.<x> = PowerSeriesRing(QQ)
            sage: f = 2*x + 3*x^2 - x^4 + O(x^5)
            sage: g = f.reverse()
            sage: g
            1/2*x - 3/8*x^2 + 9/16*x^3 - 131/128*x^4 + O(x^5)
            sage: f(g)
            x + O(x^5)
            sage: g(f)
            x + O(x^5)

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: a = t - t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + t^2 + 2*t^3 + 7*t^4 + 25*t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

            sage: B.<b,c> = PolynomialRing(ZZ)
            sage: A.<t> = PowerSeriesRing(B)
            sage: f = t + b*t^2 + c*t^3 + O(t^4)
            sage: g = f.reverse(); g
            t - b*t^2 + (2*b^2 - c)*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: B.<s> = A[[]]
            sage: f = (1 - 3*t + 4*t^3 + O(t^4))*s + (2 + t + t^2 + O(t^3))*s^2 + O(s^3)
            sage: from sage.misc.verbose import set_verbose
            sage: set_verbose(1)
            sage: g = f.reverse(); g
            verbose 1 (<module>) passing to pari failed; trying Lagrange inversion
            (1 + 3*t + 9*t^2 + 23*t^3 + O(t^4))*s + (-2 - 19*t - 118*t^2 + O(t^3))*s^2 + O(s^3)
            sage: set_verbose(0)
            sage: f(g) == g(f) == s
            True

        If the leading coefficient is not a unit, we pass to its fraction
        field if possible::

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: a = 2*t - 4*t^2 + t^4 - t^5 + O(t^6)
            sage: a.reverse()
            1/2*t + 1/2*t^2 + t^3 + 79/32*t^4 + 437/64*t^5 + O(t^6)

            sage: B.<b> = PolynomialRing(ZZ)
            sage: A.<t> = PowerSeriesRing(B)
            sage: f = 2*b*t + b*t^2 + 3*b^2*t^3 + O(t^4)
            sage: g = f.reverse(); g
            1/(2*b)*t - 1/(8*b^2)*t^2 + ((-3*b + 1)/(16*b^3))*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

        We can handle some base rings of positive characteristic::

            sage: A8.<t> = PowerSeriesRing(Zmod(8))
            sage: a = t - 15*t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + 7*t^2 + 2*t^3 + 5*t^4 + t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

        The optional argument ``precision`` sets the precision of the output::

            sage: R.<x> = PowerSeriesRing(QQ)
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

            sage: R.<x> = PowerSeriesRing(QQ, default_prec=20)
            sage: (x - x^2).reverse() # get some Catalan numbers
            x + x^2 + 2*x^3 + 5*x^4 + 14*x^5 + 42*x^6 + 132*x^7 + 429*x^8 + 1430*x^9
             + 4862*x^10 + 16796*x^11 + 58786*x^12 + 208012*x^13 + 742900*x^14
             + 2674440*x^15 + 9694845*x^16 + 35357670*x^17 + 129644790*x^18
             + 477638700*x^19 + O(x^20)
            sage: (x - x^2).reverse(precision=3)
            x + x^2 + O(x^3)

        TESTS::

            sage: R.<x> = PowerSeriesRing(QQ)
            sage: f = 1 + 2*x + 3*x^2 - x^4 + O(x^5)
            sage: f.reverse()
            Traceback (most recent call last):
            ...
            ValueError: Series must have valuation one for reversion.

            sage: Series = PowerSeriesRing(SR, 'x')                                     # needs sage.symbolic
            sage: ser = Series([0, pi]); ser                                            # needs sage.symbolic
            pi*x
            sage: ser.reverse()                                                         # needs sage.symbolic
            1/pi*x + O(x^20)"""
    @overload
    def reverse(self) -> Any:
        """PowerSeries_poly.reverse(self, precision=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 921)

        Return the reverse of `f`, i.e., the series `g` such that `g(f(x)) = x`.

        Given an optional argument ``precision``, return the reverse with given
        precision (note that the reverse can have precision at most
        ``f.prec()``).  If `f` has infinite precision, and the argument
        ``precision`` is not given, then the precision of the reverse defaults
        to the default precision of ``f.parent()``.

        Note that this is only possible if the valuation of ``self`` is exactly
        1.

        ALGORITHM:

        We first attempt to pass the computation to pari; if this fails, we
        use Lagrange inversion.  Using ``sage: set_verbose(1)`` will print
        a message if passing to pari fails.

        If the base ring has positive characteristic, then we attempt to
        lift to a characteristic zero ring and perform the reverse there.
        If this fails, an error is raised.

        EXAMPLES::

            sage: R.<x> = PowerSeriesRing(QQ)
            sage: f = 2*x + 3*x^2 - x^4 + O(x^5)
            sage: g = f.reverse()
            sage: g
            1/2*x - 3/8*x^2 + 9/16*x^3 - 131/128*x^4 + O(x^5)
            sage: f(g)
            x + O(x^5)
            sage: g(f)
            x + O(x^5)

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: a = t - t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + t^2 + 2*t^3 + 7*t^4 + 25*t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

            sage: B.<b,c> = PolynomialRing(ZZ)
            sage: A.<t> = PowerSeriesRing(B)
            sage: f = t + b*t^2 + c*t^3 + O(t^4)
            sage: g = f.reverse(); g
            t - b*t^2 + (2*b^2 - c)*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: B.<s> = A[[]]
            sage: f = (1 - 3*t + 4*t^3 + O(t^4))*s + (2 + t + t^2 + O(t^3))*s^2 + O(s^3)
            sage: from sage.misc.verbose import set_verbose
            sage: set_verbose(1)
            sage: g = f.reverse(); g
            verbose 1 (<module>) passing to pari failed; trying Lagrange inversion
            (1 + 3*t + 9*t^2 + 23*t^3 + O(t^4))*s + (-2 - 19*t - 118*t^2 + O(t^3))*s^2 + O(s^3)
            sage: set_verbose(0)
            sage: f(g) == g(f) == s
            True

        If the leading coefficient is not a unit, we pass to its fraction
        field if possible::

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: a = 2*t - 4*t^2 + t^4 - t^5 + O(t^6)
            sage: a.reverse()
            1/2*t + 1/2*t^2 + t^3 + 79/32*t^4 + 437/64*t^5 + O(t^6)

            sage: B.<b> = PolynomialRing(ZZ)
            sage: A.<t> = PowerSeriesRing(B)
            sage: f = 2*b*t + b*t^2 + 3*b^2*t^3 + O(t^4)
            sage: g = f.reverse(); g
            1/(2*b)*t - 1/(8*b^2)*t^2 + ((-3*b + 1)/(16*b^3))*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

        We can handle some base rings of positive characteristic::

            sage: A8.<t> = PowerSeriesRing(Zmod(8))
            sage: a = t - 15*t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + 7*t^2 + 2*t^3 + 5*t^4 + t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

        The optional argument ``precision`` sets the precision of the output::

            sage: R.<x> = PowerSeriesRing(QQ)
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

            sage: R.<x> = PowerSeriesRing(QQ, default_prec=20)
            sage: (x - x^2).reverse() # get some Catalan numbers
            x + x^2 + 2*x^3 + 5*x^4 + 14*x^5 + 42*x^6 + 132*x^7 + 429*x^8 + 1430*x^9
             + 4862*x^10 + 16796*x^11 + 58786*x^12 + 208012*x^13 + 742900*x^14
             + 2674440*x^15 + 9694845*x^16 + 35357670*x^17 + 129644790*x^18
             + 477638700*x^19 + O(x^20)
            sage: (x - x^2).reverse(precision=3)
            x + x^2 + O(x^3)

        TESTS::

            sage: R.<x> = PowerSeriesRing(QQ)
            sage: f = 1 + 2*x + 3*x^2 - x^4 + O(x^5)
            sage: f.reverse()
            Traceback (most recent call last):
            ...
            ValueError: Series must have valuation one for reversion.

            sage: Series = PowerSeriesRing(SR, 'x')                                     # needs sage.symbolic
            sage: ser = Series([0, pi]); ser                                            # needs sage.symbolic
            pi*x
            sage: ser.reverse()                                                         # needs sage.symbolic
            1/pi*x + O(x^20)"""
    @overload
    def reverse(self) -> Any:
        """PowerSeries_poly.reverse(self, precision=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 921)

        Return the reverse of `f`, i.e., the series `g` such that `g(f(x)) = x`.

        Given an optional argument ``precision``, return the reverse with given
        precision (note that the reverse can have precision at most
        ``f.prec()``).  If `f` has infinite precision, and the argument
        ``precision`` is not given, then the precision of the reverse defaults
        to the default precision of ``f.parent()``.

        Note that this is only possible if the valuation of ``self`` is exactly
        1.

        ALGORITHM:

        We first attempt to pass the computation to pari; if this fails, we
        use Lagrange inversion.  Using ``sage: set_verbose(1)`` will print
        a message if passing to pari fails.

        If the base ring has positive characteristic, then we attempt to
        lift to a characteristic zero ring and perform the reverse there.
        If this fails, an error is raised.

        EXAMPLES::

            sage: R.<x> = PowerSeriesRing(QQ)
            sage: f = 2*x + 3*x^2 - x^4 + O(x^5)
            sage: g = f.reverse()
            sage: g
            1/2*x - 3/8*x^2 + 9/16*x^3 - 131/128*x^4 + O(x^5)
            sage: f(g)
            x + O(x^5)
            sage: g(f)
            x + O(x^5)

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: a = t - t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + t^2 + 2*t^3 + 7*t^4 + 25*t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

            sage: B.<b,c> = PolynomialRing(ZZ)
            sage: A.<t> = PowerSeriesRing(B)
            sage: f = t + b*t^2 + c*t^3 + O(t^4)
            sage: g = f.reverse(); g
            t - b*t^2 + (2*b^2 - c)*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: B.<s> = A[[]]
            sage: f = (1 - 3*t + 4*t^3 + O(t^4))*s + (2 + t + t^2 + O(t^3))*s^2 + O(s^3)
            sage: from sage.misc.verbose import set_verbose
            sage: set_verbose(1)
            sage: g = f.reverse(); g
            verbose 1 (<module>) passing to pari failed; trying Lagrange inversion
            (1 + 3*t + 9*t^2 + 23*t^3 + O(t^4))*s + (-2 - 19*t - 118*t^2 + O(t^3))*s^2 + O(s^3)
            sage: set_verbose(0)
            sage: f(g) == g(f) == s
            True

        If the leading coefficient is not a unit, we pass to its fraction
        field if possible::

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: a = 2*t - 4*t^2 + t^4 - t^5 + O(t^6)
            sage: a.reverse()
            1/2*t + 1/2*t^2 + t^3 + 79/32*t^4 + 437/64*t^5 + O(t^6)

            sage: B.<b> = PolynomialRing(ZZ)
            sage: A.<t> = PowerSeriesRing(B)
            sage: f = 2*b*t + b*t^2 + 3*b^2*t^3 + O(t^4)
            sage: g = f.reverse(); g
            1/(2*b)*t - 1/(8*b^2)*t^2 + ((-3*b + 1)/(16*b^3))*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

        We can handle some base rings of positive characteristic::

            sage: A8.<t> = PowerSeriesRing(Zmod(8))
            sage: a = t - 15*t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + 7*t^2 + 2*t^3 + 5*t^4 + t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

        The optional argument ``precision`` sets the precision of the output::

            sage: R.<x> = PowerSeriesRing(QQ)
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

            sage: R.<x> = PowerSeriesRing(QQ, default_prec=20)
            sage: (x - x^2).reverse() # get some Catalan numbers
            x + x^2 + 2*x^3 + 5*x^4 + 14*x^5 + 42*x^6 + 132*x^7 + 429*x^8 + 1430*x^9
             + 4862*x^10 + 16796*x^11 + 58786*x^12 + 208012*x^13 + 742900*x^14
             + 2674440*x^15 + 9694845*x^16 + 35357670*x^17 + 129644790*x^18
             + 477638700*x^19 + O(x^20)
            sage: (x - x^2).reverse(precision=3)
            x + x^2 + O(x^3)

        TESTS::

            sage: R.<x> = PowerSeriesRing(QQ)
            sage: f = 1 + 2*x + 3*x^2 - x^4 + O(x^5)
            sage: f.reverse()
            Traceback (most recent call last):
            ...
            ValueError: Series must have valuation one for reversion.

            sage: Series = PowerSeriesRing(SR, 'x')                                     # needs sage.symbolic
            sage: ser = Series([0, pi]); ser                                            # needs sage.symbolic
            pi*x
            sage: ser.reverse()                                                         # needs sage.symbolic
            1/pi*x + O(x^20)"""
    @overload
    def reverse(self) -> Any:
        """PowerSeries_poly.reverse(self, precision=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 921)

        Return the reverse of `f`, i.e., the series `g` such that `g(f(x)) = x`.

        Given an optional argument ``precision``, return the reverse with given
        precision (note that the reverse can have precision at most
        ``f.prec()``).  If `f` has infinite precision, and the argument
        ``precision`` is not given, then the precision of the reverse defaults
        to the default precision of ``f.parent()``.

        Note that this is only possible if the valuation of ``self`` is exactly
        1.

        ALGORITHM:

        We first attempt to pass the computation to pari; if this fails, we
        use Lagrange inversion.  Using ``sage: set_verbose(1)`` will print
        a message if passing to pari fails.

        If the base ring has positive characteristic, then we attempt to
        lift to a characteristic zero ring and perform the reverse there.
        If this fails, an error is raised.

        EXAMPLES::

            sage: R.<x> = PowerSeriesRing(QQ)
            sage: f = 2*x + 3*x^2 - x^4 + O(x^5)
            sage: g = f.reverse()
            sage: g
            1/2*x - 3/8*x^2 + 9/16*x^3 - 131/128*x^4 + O(x^5)
            sage: f(g)
            x + O(x^5)
            sage: g(f)
            x + O(x^5)

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: a = t - t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + t^2 + 2*t^3 + 7*t^4 + 25*t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

            sage: B.<b,c> = PolynomialRing(ZZ)
            sage: A.<t> = PowerSeriesRing(B)
            sage: f = t + b*t^2 + c*t^3 + O(t^4)
            sage: g = f.reverse(); g
            t - b*t^2 + (2*b^2 - c)*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: B.<s> = A[[]]
            sage: f = (1 - 3*t + 4*t^3 + O(t^4))*s + (2 + t + t^2 + O(t^3))*s^2 + O(s^3)
            sage: from sage.misc.verbose import set_verbose
            sage: set_verbose(1)
            sage: g = f.reverse(); g
            verbose 1 (<module>) passing to pari failed; trying Lagrange inversion
            (1 + 3*t + 9*t^2 + 23*t^3 + O(t^4))*s + (-2 - 19*t - 118*t^2 + O(t^3))*s^2 + O(s^3)
            sage: set_verbose(0)
            sage: f(g) == g(f) == s
            True

        If the leading coefficient is not a unit, we pass to its fraction
        field if possible::

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: a = 2*t - 4*t^2 + t^4 - t^5 + O(t^6)
            sage: a.reverse()
            1/2*t + 1/2*t^2 + t^3 + 79/32*t^4 + 437/64*t^5 + O(t^6)

            sage: B.<b> = PolynomialRing(ZZ)
            sage: A.<t> = PowerSeriesRing(B)
            sage: f = 2*b*t + b*t^2 + 3*b^2*t^3 + O(t^4)
            sage: g = f.reverse(); g
            1/(2*b)*t - 1/(8*b^2)*t^2 + ((-3*b + 1)/(16*b^3))*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

        We can handle some base rings of positive characteristic::

            sage: A8.<t> = PowerSeriesRing(Zmod(8))
            sage: a = t - 15*t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + 7*t^2 + 2*t^3 + 5*t^4 + t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

        The optional argument ``precision`` sets the precision of the output::

            sage: R.<x> = PowerSeriesRing(QQ)
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

            sage: R.<x> = PowerSeriesRing(QQ, default_prec=20)
            sage: (x - x^2).reverse() # get some Catalan numbers
            x + x^2 + 2*x^3 + 5*x^4 + 14*x^5 + 42*x^6 + 132*x^7 + 429*x^8 + 1430*x^9
             + 4862*x^10 + 16796*x^11 + 58786*x^12 + 208012*x^13 + 742900*x^14
             + 2674440*x^15 + 9694845*x^16 + 35357670*x^17 + 129644790*x^18
             + 477638700*x^19 + O(x^20)
            sage: (x - x^2).reverse(precision=3)
            x + x^2 + O(x^3)

        TESTS::

            sage: R.<x> = PowerSeriesRing(QQ)
            sage: f = 1 + 2*x + 3*x^2 - x^4 + O(x^5)
            sage: f.reverse()
            Traceback (most recent call last):
            ...
            ValueError: Series must have valuation one for reversion.

            sage: Series = PowerSeriesRing(SR, 'x')                                     # needs sage.symbolic
            sage: ser = Series([0, pi]); ser                                            # needs sage.symbolic
            pi*x
            sage: ser.reverse()                                                         # needs sage.symbolic
            1/pi*x + O(x^20)"""
    @overload
    def reverse(self) -> Any:
        """PowerSeries_poly.reverse(self, precision=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 921)

        Return the reverse of `f`, i.e., the series `g` such that `g(f(x)) = x`.

        Given an optional argument ``precision``, return the reverse with given
        precision (note that the reverse can have precision at most
        ``f.prec()``).  If `f` has infinite precision, and the argument
        ``precision`` is not given, then the precision of the reverse defaults
        to the default precision of ``f.parent()``.

        Note that this is only possible if the valuation of ``self`` is exactly
        1.

        ALGORITHM:

        We first attempt to pass the computation to pari; if this fails, we
        use Lagrange inversion.  Using ``sage: set_verbose(1)`` will print
        a message if passing to pari fails.

        If the base ring has positive characteristic, then we attempt to
        lift to a characteristic zero ring and perform the reverse there.
        If this fails, an error is raised.

        EXAMPLES::

            sage: R.<x> = PowerSeriesRing(QQ)
            sage: f = 2*x + 3*x^2 - x^4 + O(x^5)
            sage: g = f.reverse()
            sage: g
            1/2*x - 3/8*x^2 + 9/16*x^3 - 131/128*x^4 + O(x^5)
            sage: f(g)
            x + O(x^5)
            sage: g(f)
            x + O(x^5)

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: a = t - t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + t^2 + 2*t^3 + 7*t^4 + 25*t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

            sage: B.<b,c> = PolynomialRing(ZZ)
            sage: A.<t> = PowerSeriesRing(B)
            sage: f = t + b*t^2 + c*t^3 + O(t^4)
            sage: g = f.reverse(); g
            t - b*t^2 + (2*b^2 - c)*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: B.<s> = A[[]]
            sage: f = (1 - 3*t + 4*t^3 + O(t^4))*s + (2 + t + t^2 + O(t^3))*s^2 + O(s^3)
            sage: from sage.misc.verbose import set_verbose
            sage: set_verbose(1)
            sage: g = f.reverse(); g
            verbose 1 (<module>) passing to pari failed; trying Lagrange inversion
            (1 + 3*t + 9*t^2 + 23*t^3 + O(t^4))*s + (-2 - 19*t - 118*t^2 + O(t^3))*s^2 + O(s^3)
            sage: set_verbose(0)
            sage: f(g) == g(f) == s
            True

        If the leading coefficient is not a unit, we pass to its fraction
        field if possible::

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: a = 2*t - 4*t^2 + t^4 - t^5 + O(t^6)
            sage: a.reverse()
            1/2*t + 1/2*t^2 + t^3 + 79/32*t^4 + 437/64*t^5 + O(t^6)

            sage: B.<b> = PolynomialRing(ZZ)
            sage: A.<t> = PowerSeriesRing(B)
            sage: f = 2*b*t + b*t^2 + 3*b^2*t^3 + O(t^4)
            sage: g = f.reverse(); g
            1/(2*b)*t - 1/(8*b^2)*t^2 + ((-3*b + 1)/(16*b^3))*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

        We can handle some base rings of positive characteristic::

            sage: A8.<t> = PowerSeriesRing(Zmod(8))
            sage: a = t - 15*t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + 7*t^2 + 2*t^3 + 5*t^4 + t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

        The optional argument ``precision`` sets the precision of the output::

            sage: R.<x> = PowerSeriesRing(QQ)
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

            sage: R.<x> = PowerSeriesRing(QQ, default_prec=20)
            sage: (x - x^2).reverse() # get some Catalan numbers
            x + x^2 + 2*x^3 + 5*x^4 + 14*x^5 + 42*x^6 + 132*x^7 + 429*x^8 + 1430*x^9
             + 4862*x^10 + 16796*x^11 + 58786*x^12 + 208012*x^13 + 742900*x^14
             + 2674440*x^15 + 9694845*x^16 + 35357670*x^17 + 129644790*x^18
             + 477638700*x^19 + O(x^20)
            sage: (x - x^2).reverse(precision=3)
            x + x^2 + O(x^3)

        TESTS::

            sage: R.<x> = PowerSeriesRing(QQ)
            sage: f = 1 + 2*x + 3*x^2 - x^4 + O(x^5)
            sage: f.reverse()
            Traceback (most recent call last):
            ...
            ValueError: Series must have valuation one for reversion.

            sage: Series = PowerSeriesRing(SR, 'x')                                     # needs sage.symbolic
            sage: ser = Series([0, pi]); ser                                            # needs sage.symbolic
            pi*x
            sage: ser.reverse()                                                         # needs sage.symbolic
            1/pi*x + O(x^20)"""
    @overload
    def reverse(self, precision=...) -> Any:
        """PowerSeries_poly.reverse(self, precision=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 921)

        Return the reverse of `f`, i.e., the series `g` such that `g(f(x)) = x`.

        Given an optional argument ``precision``, return the reverse with given
        precision (note that the reverse can have precision at most
        ``f.prec()``).  If `f` has infinite precision, and the argument
        ``precision`` is not given, then the precision of the reverse defaults
        to the default precision of ``f.parent()``.

        Note that this is only possible if the valuation of ``self`` is exactly
        1.

        ALGORITHM:

        We first attempt to pass the computation to pari; if this fails, we
        use Lagrange inversion.  Using ``sage: set_verbose(1)`` will print
        a message if passing to pari fails.

        If the base ring has positive characteristic, then we attempt to
        lift to a characteristic zero ring and perform the reverse there.
        If this fails, an error is raised.

        EXAMPLES::

            sage: R.<x> = PowerSeriesRing(QQ)
            sage: f = 2*x + 3*x^2 - x^4 + O(x^5)
            sage: g = f.reverse()
            sage: g
            1/2*x - 3/8*x^2 + 9/16*x^3 - 131/128*x^4 + O(x^5)
            sage: f(g)
            x + O(x^5)
            sage: g(f)
            x + O(x^5)

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: a = t - t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + t^2 + 2*t^3 + 7*t^4 + 25*t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

            sage: B.<b,c> = PolynomialRing(ZZ)
            sage: A.<t> = PowerSeriesRing(B)
            sage: f = t + b*t^2 + c*t^3 + O(t^4)
            sage: g = f.reverse(); g
            t - b*t^2 + (2*b^2 - c)*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: B.<s> = A[[]]
            sage: f = (1 - 3*t + 4*t^3 + O(t^4))*s + (2 + t + t^2 + O(t^3))*s^2 + O(s^3)
            sage: from sage.misc.verbose import set_verbose
            sage: set_verbose(1)
            sage: g = f.reverse(); g
            verbose 1 (<module>) passing to pari failed; trying Lagrange inversion
            (1 + 3*t + 9*t^2 + 23*t^3 + O(t^4))*s + (-2 - 19*t - 118*t^2 + O(t^3))*s^2 + O(s^3)
            sage: set_verbose(0)
            sage: f(g) == g(f) == s
            True

        If the leading coefficient is not a unit, we pass to its fraction
        field if possible::

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: a = 2*t - 4*t^2 + t^4 - t^5 + O(t^6)
            sage: a.reverse()
            1/2*t + 1/2*t^2 + t^3 + 79/32*t^4 + 437/64*t^5 + O(t^6)

            sage: B.<b> = PolynomialRing(ZZ)
            sage: A.<t> = PowerSeriesRing(B)
            sage: f = 2*b*t + b*t^2 + 3*b^2*t^3 + O(t^4)
            sage: g = f.reverse(); g
            1/(2*b)*t - 1/(8*b^2)*t^2 + ((-3*b + 1)/(16*b^3))*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

        We can handle some base rings of positive characteristic::

            sage: A8.<t> = PowerSeriesRing(Zmod(8))
            sage: a = t - 15*t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + 7*t^2 + 2*t^3 + 5*t^4 + t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

        The optional argument ``precision`` sets the precision of the output::

            sage: R.<x> = PowerSeriesRing(QQ)
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

            sage: R.<x> = PowerSeriesRing(QQ, default_prec=20)
            sage: (x - x^2).reverse() # get some Catalan numbers
            x + x^2 + 2*x^3 + 5*x^4 + 14*x^5 + 42*x^6 + 132*x^7 + 429*x^8 + 1430*x^9
             + 4862*x^10 + 16796*x^11 + 58786*x^12 + 208012*x^13 + 742900*x^14
             + 2674440*x^15 + 9694845*x^16 + 35357670*x^17 + 129644790*x^18
             + 477638700*x^19 + O(x^20)
            sage: (x - x^2).reverse(precision=3)
            x + x^2 + O(x^3)

        TESTS::

            sage: R.<x> = PowerSeriesRing(QQ)
            sage: f = 1 + 2*x + 3*x^2 - x^4 + O(x^5)
            sage: f.reverse()
            Traceback (most recent call last):
            ...
            ValueError: Series must have valuation one for reversion.

            sage: Series = PowerSeriesRing(SR, 'x')                                     # needs sage.symbolic
            sage: ser = Series([0, pi]); ser                                            # needs sage.symbolic
            pi*x
            sage: ser.reverse()                                                         # needs sage.symbolic
            1/pi*x + O(x^20)"""
    @overload
    def reverse(self) -> Any:
        """PowerSeries_poly.reverse(self, precision=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 921)

        Return the reverse of `f`, i.e., the series `g` such that `g(f(x)) = x`.

        Given an optional argument ``precision``, return the reverse with given
        precision (note that the reverse can have precision at most
        ``f.prec()``).  If `f` has infinite precision, and the argument
        ``precision`` is not given, then the precision of the reverse defaults
        to the default precision of ``f.parent()``.

        Note that this is only possible if the valuation of ``self`` is exactly
        1.

        ALGORITHM:

        We first attempt to pass the computation to pari; if this fails, we
        use Lagrange inversion.  Using ``sage: set_verbose(1)`` will print
        a message if passing to pari fails.

        If the base ring has positive characteristic, then we attempt to
        lift to a characteristic zero ring and perform the reverse there.
        If this fails, an error is raised.

        EXAMPLES::

            sage: R.<x> = PowerSeriesRing(QQ)
            sage: f = 2*x + 3*x^2 - x^4 + O(x^5)
            sage: g = f.reverse()
            sage: g
            1/2*x - 3/8*x^2 + 9/16*x^3 - 131/128*x^4 + O(x^5)
            sage: f(g)
            x + O(x^5)
            sage: g(f)
            x + O(x^5)

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: a = t - t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + t^2 + 2*t^3 + 7*t^4 + 25*t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

            sage: B.<b,c> = PolynomialRing(ZZ)
            sage: A.<t> = PowerSeriesRing(B)
            sage: f = t + b*t^2 + c*t^3 + O(t^4)
            sage: g = f.reverse(); g
            t - b*t^2 + (2*b^2 - c)*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: B.<s> = A[[]]
            sage: f = (1 - 3*t + 4*t^3 + O(t^4))*s + (2 + t + t^2 + O(t^3))*s^2 + O(s^3)
            sage: from sage.misc.verbose import set_verbose
            sage: set_verbose(1)
            sage: g = f.reverse(); g
            verbose 1 (<module>) passing to pari failed; trying Lagrange inversion
            (1 + 3*t + 9*t^2 + 23*t^3 + O(t^4))*s + (-2 - 19*t - 118*t^2 + O(t^3))*s^2 + O(s^3)
            sage: set_verbose(0)
            sage: f(g) == g(f) == s
            True

        If the leading coefficient is not a unit, we pass to its fraction
        field if possible::

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: a = 2*t - 4*t^2 + t^4 - t^5 + O(t^6)
            sage: a.reverse()
            1/2*t + 1/2*t^2 + t^3 + 79/32*t^4 + 437/64*t^5 + O(t^6)

            sage: B.<b> = PolynomialRing(ZZ)
            sage: A.<t> = PowerSeriesRing(B)
            sage: f = 2*b*t + b*t^2 + 3*b^2*t^3 + O(t^4)
            sage: g = f.reverse(); g
            1/(2*b)*t - 1/(8*b^2)*t^2 + ((-3*b + 1)/(16*b^3))*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

        We can handle some base rings of positive characteristic::

            sage: A8.<t> = PowerSeriesRing(Zmod(8))
            sage: a = t - 15*t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + 7*t^2 + 2*t^3 + 5*t^4 + t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

        The optional argument ``precision`` sets the precision of the output::

            sage: R.<x> = PowerSeriesRing(QQ)
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

            sage: R.<x> = PowerSeriesRing(QQ, default_prec=20)
            sage: (x - x^2).reverse() # get some Catalan numbers
            x + x^2 + 2*x^3 + 5*x^4 + 14*x^5 + 42*x^6 + 132*x^7 + 429*x^8 + 1430*x^9
             + 4862*x^10 + 16796*x^11 + 58786*x^12 + 208012*x^13 + 742900*x^14
             + 2674440*x^15 + 9694845*x^16 + 35357670*x^17 + 129644790*x^18
             + 477638700*x^19 + O(x^20)
            sage: (x - x^2).reverse(precision=3)
            x + x^2 + O(x^3)

        TESTS::

            sage: R.<x> = PowerSeriesRing(QQ)
            sage: f = 1 + 2*x + 3*x^2 - x^4 + O(x^5)
            sage: f.reverse()
            Traceback (most recent call last):
            ...
            ValueError: Series must have valuation one for reversion.

            sage: Series = PowerSeriesRing(SR, 'x')                                     # needs sage.symbolic
            sage: ser = Series([0, pi]); ser                                            # needs sage.symbolic
            pi*x
            sage: ser.reverse()                                                         # needs sage.symbolic
            1/pi*x + O(x^20)"""
    @overload
    def reverse(self, precision=...) -> Any:
        """PowerSeries_poly.reverse(self, precision=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 921)

        Return the reverse of `f`, i.e., the series `g` such that `g(f(x)) = x`.

        Given an optional argument ``precision``, return the reverse with given
        precision (note that the reverse can have precision at most
        ``f.prec()``).  If `f` has infinite precision, and the argument
        ``precision`` is not given, then the precision of the reverse defaults
        to the default precision of ``f.parent()``.

        Note that this is only possible if the valuation of ``self`` is exactly
        1.

        ALGORITHM:

        We first attempt to pass the computation to pari; if this fails, we
        use Lagrange inversion.  Using ``sage: set_verbose(1)`` will print
        a message if passing to pari fails.

        If the base ring has positive characteristic, then we attempt to
        lift to a characteristic zero ring and perform the reverse there.
        If this fails, an error is raised.

        EXAMPLES::

            sage: R.<x> = PowerSeriesRing(QQ)
            sage: f = 2*x + 3*x^2 - x^4 + O(x^5)
            sage: g = f.reverse()
            sage: g
            1/2*x - 3/8*x^2 + 9/16*x^3 - 131/128*x^4 + O(x^5)
            sage: f(g)
            x + O(x^5)
            sage: g(f)
            x + O(x^5)

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: a = t - t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + t^2 + 2*t^3 + 7*t^4 + 25*t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

            sage: B.<b,c> = PolynomialRing(ZZ)
            sage: A.<t> = PowerSeriesRing(B)
            sage: f = t + b*t^2 + c*t^3 + O(t^4)
            sage: g = f.reverse(); g
            t - b*t^2 + (2*b^2 - c)*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: B.<s> = A[[]]
            sage: f = (1 - 3*t + 4*t^3 + O(t^4))*s + (2 + t + t^2 + O(t^3))*s^2 + O(s^3)
            sage: from sage.misc.verbose import set_verbose
            sage: set_verbose(1)
            sage: g = f.reverse(); g
            verbose 1 (<module>) passing to pari failed; trying Lagrange inversion
            (1 + 3*t + 9*t^2 + 23*t^3 + O(t^4))*s + (-2 - 19*t - 118*t^2 + O(t^3))*s^2 + O(s^3)
            sage: set_verbose(0)
            sage: f(g) == g(f) == s
            True

        If the leading coefficient is not a unit, we pass to its fraction
        field if possible::

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: a = 2*t - 4*t^2 + t^4 - t^5 + O(t^6)
            sage: a.reverse()
            1/2*t + 1/2*t^2 + t^3 + 79/32*t^4 + 437/64*t^5 + O(t^6)

            sage: B.<b> = PolynomialRing(ZZ)
            sage: A.<t> = PowerSeriesRing(B)
            sage: f = 2*b*t + b*t^2 + 3*b^2*t^3 + O(t^4)
            sage: g = f.reverse(); g
            1/(2*b)*t - 1/(8*b^2)*t^2 + ((-3*b + 1)/(16*b^3))*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

        We can handle some base rings of positive characteristic::

            sage: A8.<t> = PowerSeriesRing(Zmod(8))
            sage: a = t - 15*t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + 7*t^2 + 2*t^3 + 5*t^4 + t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

        The optional argument ``precision`` sets the precision of the output::

            sage: R.<x> = PowerSeriesRing(QQ)
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

            sage: R.<x> = PowerSeriesRing(QQ, default_prec=20)
            sage: (x - x^2).reverse() # get some Catalan numbers
            x + x^2 + 2*x^3 + 5*x^4 + 14*x^5 + 42*x^6 + 132*x^7 + 429*x^8 + 1430*x^9
             + 4862*x^10 + 16796*x^11 + 58786*x^12 + 208012*x^13 + 742900*x^14
             + 2674440*x^15 + 9694845*x^16 + 35357670*x^17 + 129644790*x^18
             + 477638700*x^19 + O(x^20)
            sage: (x - x^2).reverse(precision=3)
            x + x^2 + O(x^3)

        TESTS::

            sage: R.<x> = PowerSeriesRing(QQ)
            sage: f = 1 + 2*x + 3*x^2 - x^4 + O(x^5)
            sage: f.reverse()
            Traceback (most recent call last):
            ...
            ValueError: Series must have valuation one for reversion.

            sage: Series = PowerSeriesRing(SR, 'x')                                     # needs sage.symbolic
            sage: ser = Series([0, pi]); ser                                            # needs sage.symbolic
            pi*x
            sage: ser.reverse()                                                         # needs sage.symbolic
            1/pi*x + O(x^20)"""
    @overload
    def reverse(self) -> Any:
        """PowerSeries_poly.reverse(self, precision=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 921)

        Return the reverse of `f`, i.e., the series `g` such that `g(f(x)) = x`.

        Given an optional argument ``precision``, return the reverse with given
        precision (note that the reverse can have precision at most
        ``f.prec()``).  If `f` has infinite precision, and the argument
        ``precision`` is not given, then the precision of the reverse defaults
        to the default precision of ``f.parent()``.

        Note that this is only possible if the valuation of ``self`` is exactly
        1.

        ALGORITHM:

        We first attempt to pass the computation to pari; if this fails, we
        use Lagrange inversion.  Using ``sage: set_verbose(1)`` will print
        a message if passing to pari fails.

        If the base ring has positive characteristic, then we attempt to
        lift to a characteristic zero ring and perform the reverse there.
        If this fails, an error is raised.

        EXAMPLES::

            sage: R.<x> = PowerSeriesRing(QQ)
            sage: f = 2*x + 3*x^2 - x^4 + O(x^5)
            sage: g = f.reverse()
            sage: g
            1/2*x - 3/8*x^2 + 9/16*x^3 - 131/128*x^4 + O(x^5)
            sage: f(g)
            x + O(x^5)
            sage: g(f)
            x + O(x^5)

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: a = t - t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + t^2 + 2*t^3 + 7*t^4 + 25*t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

            sage: B.<b,c> = PolynomialRing(ZZ)
            sage: A.<t> = PowerSeriesRing(B)
            sage: f = t + b*t^2 + c*t^3 + O(t^4)
            sage: g = f.reverse(); g
            t - b*t^2 + (2*b^2 - c)*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: B.<s> = A[[]]
            sage: f = (1 - 3*t + 4*t^3 + O(t^4))*s + (2 + t + t^2 + O(t^3))*s^2 + O(s^3)
            sage: from sage.misc.verbose import set_verbose
            sage: set_verbose(1)
            sage: g = f.reverse(); g
            verbose 1 (<module>) passing to pari failed; trying Lagrange inversion
            (1 + 3*t + 9*t^2 + 23*t^3 + O(t^4))*s + (-2 - 19*t - 118*t^2 + O(t^3))*s^2 + O(s^3)
            sage: set_verbose(0)
            sage: f(g) == g(f) == s
            True

        If the leading coefficient is not a unit, we pass to its fraction
        field if possible::

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: a = 2*t - 4*t^2 + t^4 - t^5 + O(t^6)
            sage: a.reverse()
            1/2*t + 1/2*t^2 + t^3 + 79/32*t^4 + 437/64*t^5 + O(t^6)

            sage: B.<b> = PolynomialRing(ZZ)
            sage: A.<t> = PowerSeriesRing(B)
            sage: f = 2*b*t + b*t^2 + 3*b^2*t^3 + O(t^4)
            sage: g = f.reverse(); g
            1/(2*b)*t - 1/(8*b^2)*t^2 + ((-3*b + 1)/(16*b^3))*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

        We can handle some base rings of positive characteristic::

            sage: A8.<t> = PowerSeriesRing(Zmod(8))
            sage: a = t - 15*t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + 7*t^2 + 2*t^3 + 5*t^4 + t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

        The optional argument ``precision`` sets the precision of the output::

            sage: R.<x> = PowerSeriesRing(QQ)
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

            sage: R.<x> = PowerSeriesRing(QQ, default_prec=20)
            sage: (x - x^2).reverse() # get some Catalan numbers
            x + x^2 + 2*x^3 + 5*x^4 + 14*x^5 + 42*x^6 + 132*x^7 + 429*x^8 + 1430*x^9
             + 4862*x^10 + 16796*x^11 + 58786*x^12 + 208012*x^13 + 742900*x^14
             + 2674440*x^15 + 9694845*x^16 + 35357670*x^17 + 129644790*x^18
             + 477638700*x^19 + O(x^20)
            sage: (x - x^2).reverse(precision=3)
            x + x^2 + O(x^3)

        TESTS::

            sage: R.<x> = PowerSeriesRing(QQ)
            sage: f = 1 + 2*x + 3*x^2 - x^4 + O(x^5)
            sage: f.reverse()
            Traceback (most recent call last):
            ...
            ValueError: Series must have valuation one for reversion.

            sage: Series = PowerSeriesRing(SR, 'x')                                     # needs sage.symbolic
            sage: ser = Series([0, pi]); ser                                            # needs sage.symbolic
            pi*x
            sage: ser.reverse()                                                         # needs sage.symbolic
            1/pi*x + O(x^20)"""
    @overload
    def reverse(self) -> Any:
        """PowerSeries_poly.reverse(self, precision=None)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 921)

        Return the reverse of `f`, i.e., the series `g` such that `g(f(x)) = x`.

        Given an optional argument ``precision``, return the reverse with given
        precision (note that the reverse can have precision at most
        ``f.prec()``).  If `f` has infinite precision, and the argument
        ``precision`` is not given, then the precision of the reverse defaults
        to the default precision of ``f.parent()``.

        Note that this is only possible if the valuation of ``self`` is exactly
        1.

        ALGORITHM:

        We first attempt to pass the computation to pari; if this fails, we
        use Lagrange inversion.  Using ``sage: set_verbose(1)`` will print
        a message if passing to pari fails.

        If the base ring has positive characteristic, then we attempt to
        lift to a characteristic zero ring and perform the reverse there.
        If this fails, an error is raised.

        EXAMPLES::

            sage: R.<x> = PowerSeriesRing(QQ)
            sage: f = 2*x + 3*x^2 - x^4 + O(x^5)
            sage: g = f.reverse()
            sage: g
            1/2*x - 3/8*x^2 + 9/16*x^3 - 131/128*x^4 + O(x^5)
            sage: f(g)
            x + O(x^5)
            sage: g(f)
            x + O(x^5)

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: a = t - t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + t^2 + 2*t^3 + 7*t^4 + 25*t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

            sage: B.<b,c> = PolynomialRing(ZZ)
            sage: A.<t> = PowerSeriesRing(B)
            sage: f = t + b*t^2 + c*t^3 + O(t^4)
            sage: g = f.reverse(); g
            t - b*t^2 + (2*b^2 - c)*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: B.<s> = A[[]]
            sage: f = (1 - 3*t + 4*t^3 + O(t^4))*s + (2 + t + t^2 + O(t^3))*s^2 + O(s^3)
            sage: from sage.misc.verbose import set_verbose
            sage: set_verbose(1)
            sage: g = f.reverse(); g
            verbose 1 (<module>) passing to pari failed; trying Lagrange inversion
            (1 + 3*t + 9*t^2 + 23*t^3 + O(t^4))*s + (-2 - 19*t - 118*t^2 + O(t^3))*s^2 + O(s^3)
            sage: set_verbose(0)
            sage: f(g) == g(f) == s
            True

        If the leading coefficient is not a unit, we pass to its fraction
        field if possible::

            sage: A.<t> = PowerSeriesRing(ZZ)
            sage: a = 2*t - 4*t^2 + t^4 - t^5 + O(t^6)
            sage: a.reverse()
            1/2*t + 1/2*t^2 + t^3 + 79/32*t^4 + 437/64*t^5 + O(t^6)

            sage: B.<b> = PolynomialRing(ZZ)
            sage: A.<t> = PowerSeriesRing(B)
            sage: f = 2*b*t + b*t^2 + 3*b^2*t^3 + O(t^4)
            sage: g = f.reverse(); g
            1/(2*b)*t - 1/(8*b^2)*t^2 + ((-3*b + 1)/(16*b^3))*t^3 + O(t^4)
            sage: f(g)
            t + O(t^4)
            sage: g(f)
            t + O(t^4)

        We can handle some base rings of positive characteristic::

            sage: A8.<t> = PowerSeriesRing(Zmod(8))
            sage: a = t - 15*t^2 - 2*t^4 + t^5 + O(t^6)
            sage: b = a.reverse(); b
            t + 7*t^2 + 2*t^3 + 5*t^4 + t^5 + O(t^6)
            sage: a(b)
            t + O(t^6)
            sage: b(a)
            t + O(t^6)

        The optional argument ``precision`` sets the precision of the output::

            sage: R.<x> = PowerSeriesRing(QQ)
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

            sage: R.<x> = PowerSeriesRing(QQ, default_prec=20)
            sage: (x - x^2).reverse() # get some Catalan numbers
            x + x^2 + 2*x^3 + 5*x^4 + 14*x^5 + 42*x^6 + 132*x^7 + 429*x^8 + 1430*x^9
             + 4862*x^10 + 16796*x^11 + 58786*x^12 + 208012*x^13 + 742900*x^14
             + 2674440*x^15 + 9694845*x^16 + 35357670*x^17 + 129644790*x^18
             + 477638700*x^19 + O(x^20)
            sage: (x - x^2).reverse(precision=3)
            x + x^2 + O(x^3)

        TESTS::

            sage: R.<x> = PowerSeriesRing(QQ)
            sage: f = 1 + 2*x + 3*x^2 - x^4 + O(x^5)
            sage: f.reverse()
            Traceback (most recent call last):
            ...
            ValueError: Series must have valuation one for reversion.

            sage: Series = PowerSeriesRing(SR, 'x')                                     # needs sage.symbolic
            sage: ser = Series([0, pi]); ser                                            # needs sage.symbolic
            pi*x
            sage: ser.reverse()                                                         # needs sage.symbolic
            1/pi*x + O(x^20)"""
    def truncate(self, prec=...) -> Any:
        """PowerSeries_poly.truncate(self, prec=infinity)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 734)

        The polynomial obtained from power series by truncation at
        precision ``prec``.

        EXAMPLES::

            sage: R.<I> = GF(2)[[]]
            sage: f = 1/(1+I+O(I^8)); f
            1 + I + I^2 + I^3 + I^4 + I^5 + I^6 + I^7 + O(I^8)
            sage: f.truncate(5)
            I^4 + I^3 + I^2 + I + 1"""
    def truncate_powerseries(self, longprec) -> Any:
        """PowerSeries_poly.truncate_powerseries(self, long prec)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 765)

        Given input ``prec`` = `n`, returns the power series of degree
        `< n` which is equivalent to ``self`` modulo `x^n`.

        EXAMPLES::

            sage: R.<I> = GF(2)[[]]
            sage: f = 1/(1+I+O(I^8)); f
            1 + I + I^2 + I^3 + I^4 + I^5 + I^6 + I^7 + O(I^8)
            sage: f.truncate_powerseries(5)
            1 + I + I^2 + I^3 + I^4 + O(I^5)"""
    @overload
    def valuation(self) -> Any:
        """PowerSeries_poly.valuation(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 119)

        Return the valuation of ``self``.

        EXAMPLES::

            sage: R.<t> = QQ[[]]
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
        """PowerSeries_poly.valuation(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 119)

        Return the valuation of ``self``.

        EXAMPLES::

            sage: R.<t> = QQ[[]]
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
        """PowerSeries_poly.valuation(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 119)

        Return the valuation of ``self``.

        EXAMPLES::

            sage: R.<t> = QQ[[]]
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
        """PowerSeries_poly.valuation(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 119)

        Return the valuation of ``self``.

        EXAMPLES::

            sage: R.<t> = QQ[[]]
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
        """PowerSeries_poly.valuation(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 119)

        Return the valuation of ``self``.

        EXAMPLES::

            sage: R.<t> = QQ[[]]
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
        """PowerSeries_poly.__call__(self, *x, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 176)

        Evaluate the series at `x=a`.

        INPUT:

        - ``x``:

          - a tuple of elements the first of which can be meaningfully
            substituted in ``self``, with the remainder used for substitution
            in the coefficients of ``self``.

          - a dictionary for kwds:value pairs. If the variable name of
            ``self`` is a keyword it is substituted for.  Other keywords
            are used for substitution in the coefficients of ``self``.

        OUTPUT: the value of ``self`` after substitution

        EXAMPLES::

            sage: R.<t> = ZZ[[]]
            sage: f = t^2 + t^3 + O(t^6)
            sage: f(t^3)
            t^6 + t^9 + O(t^18)
            sage: f(t=t^3)
            t^6 + t^9 + O(t^18)
            sage: f(f)
            t^4 + 2*t^5 + 2*t^6 + 3*t^7 + O(t^8)
            sage: f(f)(f) == f(f(f))
            True

        The following demonstrates that the problems raised in :issue:`3979`
        and :issue:`5367` are solved::

            sage: [f(t^2 + O(t^n)) for n in [9, 10, 11]]
            [t^4 + t^6 + O(t^11), t^4 + t^6 + O(t^12), t^4 + t^6 + O(t^12)]
            sage: f(t^2)
            t^4 + t^6 + O(t^12)

        It is possible to substitute a series for which only the precision
        is defined::

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

            sage: S.<u> = GF(7)[[]]
            sage: f(2*u + u^3 + O(u^5))
            4*u^2 + u^3 + 4*u^4 + 5*u^5 + O(u^6)

        As can a `p`-adic integer as long as the coefficient ring is compatible::

            sage: f(100 + O(5^7))                                                       # needs sage.rings.padics
            5^4 + 3*5^5 + 4*5^6 + 2*5^7 + 2*5^8 + O(5^9)
            sage: f.change_ring(Zp(5))(100 + O(5^7))                                    # needs sage.rings.padics
            5^4 + 3*5^5 + 4*5^6 + 2*5^7 + 2*5^8 + O(5^9)
            sage: f.change_ring(Zp(5))(100 + O(2^7))                                    # needs sage.rings.padics
            Traceback (most recent call last):
            ...
            ValueError: Cannot substitute this value

        To substitute a value it must have valuation at least 1::

            sage: f(0)
            0
            sage: f(1 + t)
            Traceback (most recent call last):
            ...
            ValueError: Can only substitute elements of positive valuation
            sage: f(2 + O(5^3))                                                         # needs sage.rings.padics
            Traceback (most recent call last):
            ...
            ValueError: Can only substitute elements of positive valuation
            sage: f(t^-2)
            Traceback (most recent call last):
            ...
            ValueError: Can only substitute elements of positive valuation

        Unless, of course, it is being substituted in a series with infinite
        precision, i.e., a polynomial::

            sage: g = t^2 + t^3
            sage: g(1 + t + O(t^2))
            2 + 5*t + O(t^2)
            sage: g(3)
            36

        Arguments beyond the first can refer to the base ring::

            sage: P.<x> = GF(5)[]
            sage: Q.<y> = P[[]]
            sage: h = (1 - x*y)^-1 + O(y^7); h
            1 + x*y + x^2*y^2 + x^3*y^3 + x^4*y^4 + x^5*y^5 + x^6*y^6 + O(y^7)
            sage: h(y^2, 3)
            1 + 3*y^2 + 4*y^4 + 2*y^6 + y^8 + 3*y^10 + 4*y^12 + O(y^14)

        These secondary values can also be specified using keywords::

            sage: h(y=y^2, x=3)
            1 + 3*y^2 + 4*y^4 + 2*y^6 + y^8 + 3*y^10 + 4*y^12 + O(y^14)
            sage: h(y^2, x=3)
            1 + 3*y^2 + 4*y^4 + 2*y^6 + y^8 + 3*y^10 + 4*y^12 + O(y^14)"""
    def __getitem__(self, n) -> Any:
        """PowerSeries_poly.__getitem__(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 408)

        Return the ``n``-th coefficient of ``self``.

        This returns 0 for negative coefficients and raises an
        :exc:`IndexError` if trying to access beyond known coefficients.

        If ``n`` is a slice object ``[:k]``, this will return a power
        series of the same precision, whose coefficients are the same
        as ``self`` for those indices in the slice, and 0 otherwise.
        Other kinds of slicing are not allowed.

        EXAMPLES::

            sage: R.<t> = QQ[[]]
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
            IndexError: coefficient not known

        Using slices::

            sage: R.<t> = ZZ[[]]
            sage: f = (2-t)^5; f
            32 - 80*t + 80*t^2 - 40*t^3 + 10*t^4 - t^5
            sage: f[:4]
            32 - 80*t + 80*t^2 - 40*t^3
            sage: f = 1 + t^3 - 4*t^4 + O(t^7); f
            1 + t^3 - 4*t^4 + O(t^7)
            sage: f[:4]
            1 + t^3 + O(t^7)

        TESTS::

            sage: f[1:4]
            Traceback (most recent call last):
            ...
            IndexError: polynomial slicing with a start is not defined"""
    def __hash__(self) -> Any:
        """PowerSeries_poly.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 79)

        Return a hash of ``self``.

        EXAMPLES::

            sage: R.<t> = ZZ[[]]
            sage: hash(t) == hash(R.gen())
            True
            sage: hash(t) != hash(R.one())
            True"""
    def __invert__(self) -> Any:
        """PowerSeries_poly.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 618)

        Return the inverse of the power series (i.e., a series `Y` such
        that `XY = 1`).

        The first nonzero coefficient must be a unit in
        the coefficient ring. If the valuation of the series is positive or
        `X` is not a unit, this function will return a
        :class:`sage.rings.laurent_series_ring_element.LaurentSeries`.

        EXAMPLES::

            sage: R.<q> = QQ[[]]
            sage: 1/(1+q + O(q**2))
            1 - q + O(q^2)
            sage: 1/(1+q)
            1 - q + q^2 - q^3 + q^4 - q^5 + q^6 - q^7 + q^8 - q^9 + q^10 - q^11 + q^12 - q^13 + q^14 - q^15 + q^16 - q^17 + q^18 - q^19 + O(q^20)
            sage: prec = R.default_prec(); prec
            20
            sage: 1/(1+q) + O(q^5)
            1 - q + q^2 - q^3 + q^4 + O(q^5)

        ::

            sage: 1/(q + q^2) + O(q^4)
            q^-1 - 1 + q - q^2 + q^3 + O(q^4)
            sage: g = 1/(q + q^2 + O(q^5))
            sage: g; g.parent()
            q^-1 - 1 + q - q^2 + O(q^3)
            Laurent Series Ring in q over Rational Field

        ::

            sage: 1/g
            q + q^2 + O(q^5)
            sage: (1/g).parent()
            Laurent Series Ring in q over Rational Field

        ::

            sage: 1/(2 + q) + O(q^5)
            1/2 - 1/4*q + 1/8*q^2 - 1/16*q^3 + 1/32*q^4 + O(q^5)

        ::

            sage: R.<q> = PowerSeriesRing(QQ, name='q', default_prec=5)
            sage: f = 1 + q + q^2 + O(q^50)
            sage: f/10
            1/10 + 1/10*q + 1/10*q^2 + O(q^50)
            sage: f/(10+q)
            1/10 + 9/100*q + 91/1000*q^2 - 91/10000*q^3 + 91/100000*q^4 + O(q^5)

        ::

            sage: R.<t> = PowerSeriesRing(QQ, sparse=True)
            sage: u = 17 + 3*t^2 + 19*t^10 + O(t^12)
            sage: v = ~u; v
            1/17 - 3/289*t^2 + 9/4913*t^4 - 27/83521*t^6 + 81/1419857*t^8 - 1587142/24137569*t^10 + O(t^12)
            sage: u*v
            1 + O(t^12)

        If we try a nonzero, non-unit constant term, we end up in
        the fraction field, i.e. the Laurent series ring::

            sage: R.<t> = PowerSeriesRing(ZZ)
            sage: ~R(2)
            1/2
            sage: parent(~R(2))
            Laurent Series Ring in t over Rational Field

        As for units, we stay in the power series ring::

            sage: ~R(-1)
            -1
            sage: parent(~R(-1))
            Power Series Ring in t over Integer Ring

        However, inversion of non-unit elements must fail when the underlying
        ring is not an integral domain::

            sage: R = IntegerModRing(8)
            sage: P.<s> = R[[]]
            sage: ~P(2)
            Traceback (most recent call last):
            ...
            ValueError: must be an integral domain"""
    def __iter__(self) -> Any:
        """PowerSeries_poly.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 466)

        Return an iterator over the coefficients of this power series.

        EXAMPLES::

            sage: R.<t> = QQ[[]]
            sage: f = t + 17/5*t^3 + 2*t^4 + O(t^5)
            sage: [a for a in f]
            [0, 1, 0, 17/5, 2]"""
    def __lshift__(self, PowerSeries_polyself, n) -> Any:
        """PowerSeries_poly.__lshift__(PowerSeries_poly self, n)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 582)

        Shift ``self`` to the left by ``n``, i.e. multiply by `x^n`.

        EXAMPLES::

            sage: R.<t> = QQ[[]]
            sage: f = 1 + t + t^4
            sage: f << 1
            t + t^2 + t^5"""
    def __neg__(self) -> Any:
        """PowerSeries_poly.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 479)

        Return the negative of this power series.

        EXAMPLES::

            sage: R.<t> = QQ[[]]
            sage: f = t + 17/5*t^3 + 2*t^4 + O(t^5)
            sage: -f
            -t - 17/5*t^3 - 2*t^4 + O(t^5)"""
    def __reduce__(self) -> Any:
        """PowerSeries_poly.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 93)

        Used for pickling.

        EXAMPLES::

            sage: A.<z> = RR[[]]
            sage: f = z - z^3 + O(z^10)
            sage: f == loads(dumps(f)) # indirect doctest
            True"""
    def __rlshift__(self, other):
        """Return value<<self."""
    def __rrshift__(self, other):
        """Return value>>self."""
    def __rshift__(self, PowerSeries_polyself, n) -> Any:
        """PowerSeries_poly.__rshift__(PowerSeries_poly self, n)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_poly.pyx (starting at line 598)

        Shift ``self`` to the right by ``n``, i.e. multiply by `x^{-n}` and
        remove any terms of negative exponent.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: R.<t> = GF(2)[[]]
            sage: f = t + t^4 + O(t^7)
            sage: f >> 1
            1 + t^3 + O(t^6)
            sage: f >> 10
            O(t^0)"""
