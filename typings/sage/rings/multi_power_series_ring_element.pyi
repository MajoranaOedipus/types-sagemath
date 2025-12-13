from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.finite_rings.integer_mod_ring import Zmod as Zmod
from sage.rings.infinity import InfinityElement as InfinityElement, infinity as infinity
from sage.rings.integer import Integer as Integer
from sage.rings.polynomial.polynomial_ring import PolynomialRing_generic as PolynomialRing_generic
from sage.rings.power_series_ring_element import PowerSeries as PowerSeries
from sage.structure.richcmp import richcmp as richcmp

def is_MPowerSeries(f):
    """
    Return ``True`` if ``f`` is a multivariate power series.

    TESTS::

        sage: from sage.rings.power_series_ring_element import is_PowerSeries
        sage: from sage.rings.multi_power_series_ring_element import is_MPowerSeries
        sage: M = PowerSeriesRing(ZZ,4,'v')
        sage: is_PowerSeries(M.random_element(10))
        doctest:warning...
        DeprecationWarning: The function is_PowerSeries is deprecated; use 'isinstance(..., PowerSeries)' instead.
        See https://github.com/sagemath/sage/issues/38266 for details.
        True
        sage: is_MPowerSeries(M.random_element(10))
        doctest:warning...
        DeprecationWarning: The function is_MPowerSeries is deprecated; use 'isinstance(..., MPowerSeries)' instead.
        See https://github.com/sagemath/sage/issues/38266 for details.
        True
        sage: T.<v> = PowerSeriesRing(RR)
        sage: is_MPowerSeries(1 - v + v^2 +O(v^3))
        False
        sage: is_PowerSeries(1 - v + v^2 +O(v^3))
        True
    """

class MPowerSeries(PowerSeries):
    """
    Multivariate power series; these are the elements of Multivariate Power
    Series Rings.

    INPUT:

    - ``parent`` -- a multivariate power series

    - ``x`` -- the element (default: 0).  This can be another
      :class:`MPowerSeries` object, or an element of one of the following:

      - the background univariate power series ring
      - the foreground polynomial ring
      - a ring that coerces to one of the above two

    - ``prec`` -- (default: ``infinity``) the precision

    - ``is_gen`` -- boolean (default: ``False``); whether this element is one
      of the generators

    - ``check`` -- boolean (default: ``False``); needed by univariate power
      series class

    EXAMPLES:

    Construct multivariate power series from generators::

        sage: S.<s,t> = PowerSeriesRing(ZZ)
        sage: f = s + 4*t + 3*s*t
        sage: f in S
        True
        sage: f = f.add_bigoh(4); f
        s + 4*t + 3*s*t + O(s, t)^4
        sage: g = 1 + s + t - s*t + S.O(5); g
        1 + s + t - s*t + O(s, t)^5

        sage: T = PowerSeriesRing(GF(3),5,'t'); T
        Multivariate Power Series Ring in t0, t1, t2, t3, t4
         over Finite Field of size 3
        sage: t = T.gens()
        sage: w = t[0] - 2*t[1]*t[3] + 5*t[4]^3 - t[0]^3*t[2]^2; w
        t0 + t1*t3 - t4^3 - t0^3*t2^2
        sage: w = w.add_bigoh(5); w
        t0 + t1*t3 - t4^3 + O(t0, t1, t2, t3, t4)^5
        sage: w in T
        True

        sage: w = t[0] - 2*t[0]*t[2] + 5*t[4]^3 - t[0]^3*t[2]^2 + T.O(6)
        sage: w
        t0 + t0*t2 - t4^3 - t0^3*t2^2 + O(t0, t1, t2, t3, t4)^6


    Get random elements::

        sage: S.random_element(4)   # random
        -2*t + t^2 - 12*s^3 + O(s, t)^4

        sage: T.random_element(10)  # random
        -t1^2*t3^2*t4^2 + t1^5*t3^3*t4 + O(t0, t1, t2, t3, t4)^10


    Convert elements from polynomial rings::

        sage: # needs sage.rings.finite_rings
        sage: R = PolynomialRing(ZZ, 5, T.variable_names())
        sage: t = R.gens()
        sage: r = -t[2]*t[3] + t[3]^2 + t[4]^2
        sage: T(r)
        -t2*t3 + t3^2 + t4^2
        sage: r.parent()
        Multivariate Polynomial Ring in t0, t1, t2, t3, t4 over Integer Ring
        sage: r in T
        True
    """
    def __init__(self, parent, x: int = 0, prec=..., is_gen: bool = False, check: bool = False) -> None:
        """
        Input ``x`` can be an :class:`MPowerSeries`, or an element of

            - the background univariate power series ring
            - the foreground polynomial ring
            - a ring that coerces to one of the above two

        EXAMPLES::

            sage: R.<s,t> = PowerSeriesRing(ZZ); R
            Multivariate Power Series Ring in s, t over Integer Ring
            sage: f = 1 + t + s + s*t + R.O(3)
            sage: g = (1/2) * f; g
            1/2 + 1/2*s + 1/2*t + 1/2*s*t + O(s, t)^3
            sage: g.parent()
            Multivariate Power Series Ring in s, t over Rational Field
            sage: g = (1/2)*f; g
            1/2 + 1/2*s + 1/2*t + 1/2*s*t + O(s, t)^3
            sage: g.parent()
            Multivariate Power Series Ring in s, t over Rational Field

            sage: x = polygen(ZZ, 'x')
            sage: K = NumberField(x - 3,'a')                                            # needs sage.rings.number_field
            sage: g = K.random_element()*f                                              # needs sage.rings.number_field
            sage: g.parent()                                                            # needs sage.rings.number_field
            Multivariate Power Series Ring in s, t over
             Number Field in a with defining polynomial x - 3

        TESTS::

            sage: S.<s,t> = PowerSeriesRing(ZZ)
            sage: f = s + 4*t + 3*s*t
            sage: f in S
            True
            sage: f = f.add_bigoh(4); f
            s + 4*t + 3*s*t + O(s, t)^4
            sage: g = 1 + s + t - s*t + S.O(5); g
            1 + s + t - s*t + O(s, t)^5

            sage: B.<s, t> = PowerSeriesRing(QQ)
            sage: C.<z> = PowerSeriesRing(QQ)
            sage: B(z)
            Traceback (most recent call last):
            ...
            TypeError: Cannot coerce input to polynomial ring.

            sage: D.<s> = PowerSeriesRing(QQ)
            sage: s.parent() is D
            True
            sage: B(s) in B
            True
            sage: d = D.random_element(20)
            sage: b = B(d) # test coercion from univariate power series ring
            sage: b in B
            True
        """
    def __reduce__(self):
        """
        For pickling.

        EXAMPLES::

            sage: K.<s,t> = PowerSeriesRing(QQ)
            sage: f = 1 + t - s + s*t - s*t^3 + K.O(12)
            sage: loads(dumps(f)) == f
            True
        """
    def __call__(self, *x, **kwds):
        """
        Evaluate ``self``.

        EXAMPLES::

            sage: R.<s,t> = PowerSeriesRing(ZZ); R
            Multivariate Power Series Ring in s, t over Integer Ring
            sage: f = s^2 + s*t + s^3 + s^2*t + 3*s^4 + 3*s^3*t + R.O(5); f
            s^2 + s*t + s^3 + s^2*t + 3*s^4 + 3*s^3*t + O(s, t)^5
            sage: f(t,s)
            s*t + t^2 + s*t^2 + t^3 + 3*s*t^3 + 3*t^4 + O(s, t)^5

            sage: f(t,0)
            t^2 + t^3 + 3*t^4 + O(s, t)^5
            sage: f(t,2)
            Traceback (most recent call last):
            ...
            TypeError: Substitution defined only for elements of positive
            valuation, unless self has infinite precision.

            sage: f.truncate()(t,2)
            2*t + 3*t^2 + 7*t^3 + 3*t^4

        Checking that :issue:`15059` is fixed::

            sage: M.<u,v> = PowerSeriesRing(GF(5))
            sage: s = M.hom([u, u+v])
            sage: s(M.one())
            1

        Since :issue:`26105` you can specify a map on the base ring::

            sage: # needs sage.rings.number_field
            sage: Zx.<x> = ZZ[]
            sage: K.<i> = NumberField(x^2 + 1)
            sage: cc = K.hom([-i])
            sage: R.<s,t> = PowerSeriesRing(K)
            sage: f = s^2 + i*s*t + (3+4*i)*s^3 + R.O(4); f
            s^2 + i*s*t + (4*i + 3)*s^3 + O(s, t)^4
            sage: f(t, s, base_map=cc)
            (-i)*s*t + t^2 + (-4*i + 3)*t^3 + O(s, t)^4
        """
    def __getitem__(self, n):
        """
        Return the coefficient of the monomial ``x1^e1 * x2^e2 * ... * xk^ek``
        if ``n = (e_1, e2, ..., ek)`` is a tuple whose length is the number of
        variables ``x1,x2,...,xk`` in the power series ring.

        Return the sum of the monomials of degree ``n`` if ``n`` is an integer.

        TESTS::

            sage: R.<a,b> = PowerSeriesRing(ZZ)
            sage: f = 1 + a + b - a*b + R.O(4)
            sage: f[0]
            1
            sage: f[2]
            -a*b
            sage: f[3]
            0
            sage: f[4]
            Traceback (most recent call last):
            ...
            IndexError: Cannot return terms of total degree greater than or
            equal to precision of self.

        Ensure that the enhancement detailed in :issue:`39314` works as intended::

            sage: R.<x,y> = QQ[[]]
            sage: ((x+y)^3)[2,1]
            3
            sage: f = 1/(1 + x + y)
            sage: f[2,5]
            -21
            sage: f[0,30]
            Traceback (most recent call last):
            ...
            IndexError: Cannot return the coefficients of terms of total degree
            greater than or equal to precision of self.
        """
    def __invert__(self):
        """
        Return multiplicative inverse of this multivariate power series.

        Currently implemented only if constant coefficient is a unit in the
        base ring.

        EXAMPLES::

            sage: R.<a,b,c> = PowerSeriesRing(ZZ)
            sage: f = 1 + a + b - a*b - b*c - a*c + R.O(4)
            sage: ~f
            1 - a - b + a^2 + 3*a*b + a*c + b^2 + b*c - a^3 - 5*a^2*b
            - 2*a^2*c - 5*a*b^2 - 4*a*b*c - b^3 - 2*b^2*c + O(a, b, c)^4
        """
    def trailing_monomial(self):
        """
        Return the trailing monomial of ``self``.

        This is defined here as the lowest term of the underlying polynomial.

        EXAMPLES::

            sage: R.<a,b,c> = PowerSeriesRing(ZZ)
            sage: f = 1 + a + b - a*b + R.O(3)
            sage: f.trailing_monomial()
            1
            sage: f = a^2*b^3*f; f
            a^2*b^3 + a^3*b^3 + a^2*b^4 - a^3*b^4 + O(a, b, c)^8
            sage: f.trailing_monomial()
            a^2*b^3

        TESTS::

            sage: (f-f).trailing_monomial()
            0
        """
    def quo_rem(self, other, precision=None):
        """
        Return the pair of quotient and remainder for the increasing power
        division of ``self`` by ``other``.

        If `a` and `b` are two elements of a power series ring
        `R[[x_1, x_2, \\cdots, x_n]]` such that the trailing term of
        `b` is invertible in `R`, then the pair of quotient and
        remainder for the increasing power division of `a` by `b` is
        the unique pair `(u, v) \\in R[[x_1, x_2, \\cdots, x_n]] \\times
        R[x_1, x_2, \\cdots, x_n]` such that `a = bu + v` and such that
        no monomial appearing in `v` divides the trailing monomial
        (:meth:`trailing_monomial`) of `b`. Note that this depends on
        the order of the variables.

        This method returns both quotient and remainder as power series,
        even though in mathematics, the remainder for the increasing
        power division of two power series is a polynomial. This is
        because Sage's power series come with a precision, and that
        precision is not always sufficient to determine the remainder
        completely. Disregarding this issue, the :meth:`polynomial`
        method can be used to recast the remainder as an actual
        polynomial.

        INPUT:

        - ``other`` -- an element of the same power series ring as
          ``self`` such that the trailing term of ``other`` is
          invertible in ``self`` (this is automatically satisfied
          if the base ring is a field, unless ``other`` is zero)

        - ``precision`` -- (default: the default precision of the
          parent of ``self``) nonnegative integer, determining the
          precision to be cast on the resulting quotient and
          remainder if both ``self`` and ``other`` have infinite
          precision (ignored otherwise); note that the resulting
          precision might be lower than this integer

        EXAMPLES::

            sage: # needs sage.libs.singular
            sage: R.<a,b,c> = PowerSeriesRing(ZZ)
            sage: f = 1 + a + b - a*b + R.O(3)
            sage: g = 1 + 2*a - 3*a*b + R.O(3)
            sage: q, r = f.quo_rem(g); q, r
            (1 - a + b + 2*a^2 + O(a, b, c)^3, 0 + O(a, b, c)^3)
            sage: f == q*g + r
            True
            sage: q, r = (a*f).quo_rem(g); q, r
            (a - a^2 + a*b + 2*a^3 + O(a, b, c)^4, 0 + O(a, b, c)^4)
            sage: a*f == q*g + r
            True
            sage: q, r = (a*f).quo_rem(a*g); q, r
            (1 - a + b + 2*a^2 + O(a, b, c)^3, 0 + O(a, b, c)^4)
            sage: a*f == q*(a*g) + r
            True
            sage: q, r = (a*f).quo_rem(b*g); q, r
            (a - 3*a^2 + O(a, b, c)^3, a + a^2 + O(a, b, c)^4)
            sage: a*f == q*(b*g) + r
            True

        Trying to divide two polynomials, we run into the issue that
        there is no natural setting for the precision of the quotient
        and remainder (and if we wouldn't set a precision, the
        algorithm would never terminate). Here, default precision
        comes to our help::

            sage: # needs sage.libs.singular
            sage: (1 + a^3).quo_rem(a + a^2)
            (a^2 - a^3 + a^4 - a^5 + a^6 - a^7 + a^8 - a^9 + a^10 + O(a, b, c)^11,
             1 + O(a, b, c)^12)
            sage: (1 + a^3 + a*b).quo_rem(b + c)
            (a + O(a, b, c)^11, 1 - a*c + a^3 + O(a, b, c)^12)
            sage: (1 + a^3 + a*b).quo_rem(b + c, precision=17)
            (a + O(a, b, c)^16, 1 - a*c + a^3 + O(a, b, c)^17)
            sage: (a^2 + b^2 + c^2).quo_rem(a + b + c)
            (a - b - c + O(a, b, c)^11, 2*b^2 + 2*b*c + 2*c^2 + O(a, b, c)^12)
            sage: (a^2 + b^2 + c^2).quo_rem(1/(1+a+b+c))
            (a^2 + b^2 + c^2 + a^3 + a^2*b + a^2*c + a*b^2 + a*c^2
               + b^3 + b^2*c + b*c^2 + c^3 + O(a, b, c)^14,
             0)
            sage: (a^2 + b^2 + c^2).quo_rem(a/(1+a+b+c))
            (a + a^2 + a*b + a*c + O(a, b, c)^13, b^2 + c^2)
            sage: (1 + a + a^15).quo_rem(a^2)
            (0 + O(a, b, c)^10, 1 + a + O(a, b, c)^12)
            sage: (1 + a + a^15).quo_rem(a^2, precision=15)
            (0 + O(a, b, c)^13, 1 + a + O(a, b, c)^15)
            sage: (1 + a + a^15).quo_rem(a^2, precision=16)
            (a^13 + O(a, b, c)^14, 1 + a + O(a, b, c)^16)

        Illustrating the dependency on the ordering of variables::

            sage: # needs sage.libs.singular
            sage: (1 + a + b).quo_rem(b + c)
            (1 + O(a, b, c)^11, 1 + a - c + O(a, b, c)^12)
            sage: (1 + b + c).quo_rem(c + a)
            (0 + O(a, b, c)^11, 1 + b + c + O(a, b, c)^12)
            sage: (1 + c + a).quo_rem(a + b)
            (1 + O(a, b, c)^11, 1 - b + c + O(a, b, c)^12)

        TESTS::

            sage: (f).quo_rem(R.zero())                                                 # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ZeroDivisionError

            sage: (f).quo_rem(R.zero().add_bigoh(2))                                    # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ZeroDivisionError

        Coercion is applied on ``other``::

            sage: (a + b).quo_rem(1)                                                    # needs sage.libs.singular
            (a + b + O(a, b, c)^12, 0 + O(a, b, c)^12)

            sage: R.<a,b,c> = PowerSeriesRing(QQ)
            sage: R(3).quo_rem(2)
            (3/2 + O(a, b, c)^12, 0 + O(a, b, c)^12)
        """
    def __mod__(self, other):
        """
        TESTS::

            sage: R.<a,b,c> = PowerSeriesRing(ZZ)
            sage: f = -a^3*b*c^2 + a^2*b^2*c^4 - 12*a^3*b^3*c^3 + R.O(10)
            sage: g = f % 2; g
            a^3*b*c^2 + a^2*b^2*c^4 + O(a, b, c)^10
            sage: g in R
            False
            sage: g in R.base_extend(Zmod(2))
            True
            sage: g.polynomial() == f.polynomial() % 2                                  # needs sage.libs.singular
            True
        """
    def monomial_coefficients(self, copy=None):
        """
        Return underlying dictionary with keys the exponents and values the
        coefficients of this power series.

        EXAMPLES::

            sage: M = PowerSeriesRing(QQ,4,'t',sparse=True); M
            Sparse Multivariate Power Series Ring in t0, t1, t2, t3 over
            Rational Field

            sage: M.inject_variables()
            Defining t0, t1, t2, t3

            sage: m = 2/3*t0*t1^15*t3^48 - t0^15*t1^21*t2^28*t3^5
            sage: m2 = 1/2*t0^12*t1^29*t2^46*t3^6 - 1/4*t0^39*t1^5*t2^23*t3^30 + M.O(100)
            sage: s = m + m2
            sage: s.monomial_coefficients()
            {(1, 15, 0, 48): 2/3,
             (12, 29, 46, 6): 1/2,
             (15, 21, 28, 5): -1,
             (39, 5, 23, 30): -1/4}

        ``dict`` is an alias::

            sage: s.dict()
            {(1, 15, 0, 48): 2/3,
             (12, 29, 46, 6): 1/2,
             (15, 21, 28, 5): -1,
             (39, 5, 23, 30): -1/4}
        """
    dict = monomial_coefficients
    def polynomial(self):
        '''
        Return the underlying polynomial of ``self`` as an element of
        the underlying multivariate polynomial ring (the "foreground
        polynomial ring").

        EXAMPLES::

            sage: M = PowerSeriesRing(QQ,4,\'t\'); M
            Multivariate Power Series Ring in t0, t1, t2, t3 over Rational
            Field
            sage: t = M.gens()
            sage: f = 1/2*t[0]^3*t[1]^3*t[2]^2 + 2/3*t[0]*t[2]^6*t[3]             ....: - t[0]^3*t[1]^3*t[3]^3 - 1/4*t[0]*t[1]*t[2]^7 + M.O(10)
            sage: f
            1/2*t0^3*t1^3*t2^2 + 2/3*t0*t2^6*t3 - t0^3*t1^3*t3^3
            - 1/4*t0*t1*t2^7 + O(t0, t1, t2, t3)^10

            sage: f.polynomial()
            1/2*t0^3*t1^3*t2^2 + 2/3*t0*t2^6*t3 - t0^3*t1^3*t3^3
            - 1/4*t0*t1*t2^7

            sage: f.polynomial().parent()
            Multivariate Polynomial Ring in t0, t1, t2, t3 over Rational Field

        Contrast with :meth:`truncate`::

            sage: f.truncate()
            1/2*t0^3*t1^3*t2^2 + 2/3*t0*t2^6*t3 - t0^3*t1^3*t3^3 - 1/4*t0*t1*t2^7
            sage: f.truncate().parent()
            Multivariate Power Series Ring in t0, t1, t2, t3 over Rational Field
        '''
    def variables(self):
        """
        Return tuple of variables occurring in ``self``.

        EXAMPLES::

            sage: T = PowerSeriesRing(GF(3),5,'t'); T
            Multivariate Power Series Ring in t0, t1, t2, t3, t4 over
            Finite Field of size 3
            sage: t = T.gens()
            sage: w = t[0] - 2*t[0]*t[2] + 5*t[4]^3 - t[0]^3*t[2]^2 + T.O(6)
            sage: w
            t0 + t0*t2 - t4^3 - t0^3*t2^2 + O(t0, t1, t2, t3, t4)^6
            sage: w.variables()
            (t0, t2, t4)
        """
    def monomials(self):
        """
        Return a list of monomials of ``self``.

        These are the keys of the dict returned by :meth:`coefficients`.

        EXAMPLES::

            sage: R.<a,b,c> = PowerSeriesRing(ZZ); R
            Multivariate Power Series Ring in a, b, c over Integer Ring
            sage: f = 1 + a + b - a*b - b*c - a*c + R.O(4)
            sage: sorted(f.monomials())
            [b*c, a*c, a*b, b, a, 1]
            sage: f = 1 + 2*a + 7*b - 2*a*b - 4*b*c - 13*a*c + R.O(4)
            sage: sorted(f.monomials())
            [b*c, a*c, a*b, b, a, 1]
            sage: f = R.zero()
            sage: f.monomials()
            []
        """
    def coefficients(self):
        """
        Return a dict of monomials and coefficients.

        EXAMPLES::

            sage: R.<s,t> = PowerSeriesRing(ZZ); R
            Multivariate Power Series Ring in s, t over Integer Ring
            sage: f = 1 + t + s + s*t + R.O(3)
            sage: f.coefficients()
            {s*t: 1, t: 1, s: 1, 1: 1}
            sage: (f^2).coefficients()
            {t^2: 1, s*t: 4, s^2: 1, t: 2, s: 2, 1: 1}

            sage: g = f^2 + f - 2; g
            3*s + 3*t + s^2 + 5*s*t + t^2 + O(s, t)^3
            sage: cd = g.coefficients()
            sage: g2 = sum(k*v for (k,v) in cd.items()); g2
            3*s + 3*t + s^2 + 5*s*t + t^2
            sage: g2 == g.truncate()
            True
        """
    def constant_coefficient(self):
        """
        Return constant coefficient of ``self``.

        EXAMPLES::

            sage: R.<a,b,c> = PowerSeriesRing(ZZ); R
            Multivariate Power Series Ring in a, b, c over Integer Ring
            sage: f = 3 + a + b - a*b - b*c - a*c + R.O(4)
            sage: f.constant_coefficient()
            3
            sage: f.constant_coefficient().parent()
            Integer Ring
        """
    def exponents(self):
        """
        Return a list of tuples which hold the exponents of each monomial
        of ``self``.

        EXAMPLES::

            sage: H = QQ[['x,y']]
            sage: (x,y) = H.gens()
            sage: h = -y^2 - x*y^3 - 6/5*y^6 - x^7 + 2*x^5*y^2 + H.O(10)
            sage: h
            -y^2 - x*y^3 - 6/5*y^6 - x^7 + 2*x^5*y^2 + O(x, y)^10
            sage: h.exponents()
            [(0, 2), (1, 3), (0, 6), (7, 0), (5, 2)]
        """
    def V(self, n):
        """
        If

        .. MATH::

            f = \\sum a_{m_0, \\ldots, m_k} x_0^{m_0} \\cdots x_k^{m_k},

        then this function returns

        .. MATH::

            \\sum a_{m_0, \\ldots, m_k} x_0^{n m_0} \\cdots x_k^{n m_k}.

        The total-degree precision of the output is ``n`` times the precision
        of ``self``.

        EXAMPLES::

            sage: H = QQ[['x,y,z']]
            sage: (x,y,z) = H.gens()
            sage: h = -x*y^4*z^7 - 1/4*y*z^12 + 1/2*x^7*y^5*z^2 \\\n            ....: + 2/3*y^6*z^8 + H.O(15)
            sage: h.V(3)
            -x^3*y^12*z^21 - 1/4*y^3*z^36 + 1/2*x^21*y^15*z^6 + 2/3*y^18*z^24 + O(x, y, z)^45
        """
    def prec(self):
        """
        Return precision of ``self``.

        EXAMPLES::

            sage: R.<a,b,c> = PowerSeriesRing(ZZ); R
            Multivariate Power Series Ring in a, b, c over Integer Ring
            sage: f = 3 + a + b - a*b - b*c - a*c + R.O(4)
            sage: f.prec()
            4
            sage: f.truncate().prec()
            +Infinity
        """
    def add_bigoh(self, prec):
        """
        Return a multivariate power series of precision ``prec``
        obtained by truncating ``self`` at precision ``prec``.

        This is the same as :meth:`O`.

        EXAMPLES::

            sage: B.<x,y> = PowerSeriesRing(QQ); B
            Multivariate Power Series Ring in x, y over Rational Field
            sage: r = 1 - x*y + x^2
            sage: r.add_bigoh(4)
            1 + x^2 - x*y + O(x, y)^4
            sage: r.add_bigoh(2)
            1 + O(x, y)^2

        Note that this does not change ``self``::

            sage: r
            1 + x^2 - x*y
        """
    def O(self, prec):
        """
        Return a multivariate power series of precision ``prec``
        obtained by truncating ``self`` at precision ``prec``.

        This is the same as :meth:`add_bigoh`.

        EXAMPLES::

            sage: B.<x,y> = PowerSeriesRing(QQ); B
            Multivariate Power Series Ring in x, y over Rational Field
            sage: r = 1 - x*y + x^2
            sage: r.O(4)
            1 + x^2 - x*y + O(x, y)^4
            sage: r.O(2)
            1 + O(x, y)^2

        Note that this does not change ``self``::

            sage: r
            1 + x^2 - x*y
        """
    def truncate(self, prec=...):
        """
        Return infinite precision multivariate power series formed by
        truncating ``self`` at precision ``prec``.

        EXAMPLES::

            sage: M = PowerSeriesRing(QQ,4,'t'); M
            Multivariate Power Series Ring in t0, t1, t2, t3 over Rational Field
            sage: t = M.gens()
            sage: f = 1/2*t[0]^3*t[1]^3*t[2]^2 + 2/3*t[0]*t[2]^6*t[3]             ....: - t[0]^3*t[1]^3*t[3]^3 - 1/4*t[0]*t[1]*t[2]^7 + M.O(10)
            sage: f
            1/2*t0^3*t1^3*t2^2 + 2/3*t0*t2^6*t3 - t0^3*t1^3*t3^3
            - 1/4*t0*t1*t2^7 + O(t0, t1, t2, t3)^10

            sage: f.truncate()
            1/2*t0^3*t1^3*t2^2 + 2/3*t0*t2^6*t3 - t0^3*t1^3*t3^3
            - 1/4*t0*t1*t2^7
            sage: f.truncate().parent()
            Multivariate Power Series Ring in t0, t1, t2, t3 over Rational Field

        Contrast with polynomial::

            sage: f.polynomial()
            1/2*t0^3*t1^3*t2^2 + 2/3*t0*t2^6*t3 - t0^3*t1^3*t3^3 - 1/4*t0*t1*t2^7
            sage: f.polynomial().parent()
            Multivariate Polynomial Ring in t0, t1, t2, t3 over Rational Field
        """
    def valuation(self):
        """
        Return the valuation of ``self``.

        The valuation of a power series `f` is the highest nonnegative
        integer `k` less or equal to the precision of `f` and such
        that the coefficient of `f` before each term of degree `< k` is
        zero. (If such an integer does not exist, then the valuation is
        the precision of `f` itself.)

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: R.<a,b> = PowerSeriesRing(GF(4949717)); R
            Multivariate Power Series Ring in a, b
             over Finite Field of size 4949717
            sage: f = a^2 + a*b + a^3 + R.O(9)
            sage: f.valuation()
            2
            sage: g = 1 + a + a^3
            sage: g.valuation()
            0
            sage: R.zero().valuation()
            +Infinity
        """
    def is_nilpotent(self):
        """
        Return ``True`` if ``self`` is nilpotent. This occurs if

        - ``self`` has finite precision and positive valuation, or
        - ``self`` is constant and nilpotent in base ring.

        Otherwise, return ``False``.

        .. WARNING::

            This is so far just a sufficient condition, so don't trust
            a ``False`` output to be legit!

        .. TODO::

            What should we do about this method? Is nilpotency of a
            power series even decidable (assuming a nilpotency oracle
            in the base ring)? And I am not sure that returning
            ``True`` just because the series has finite precision and
            zero constant term is a good idea.

        EXAMPLES::

            sage: R.<a,b,c> = PowerSeriesRing(Zmod(8)); R
            Multivariate Power Series Ring in a, b, c over Ring of integers modulo 8
            sage: f = a + b + c + a^2*c
            sage: f.is_nilpotent()
            False
            sage: f = f.O(4); f
            a + b + c + a^2*c + O(a, b, c)^4
            sage: f.is_nilpotent()
            True

            sage: g = R(2)
            sage: g.is_nilpotent()
            True
            sage: (g.O(4)).is_nilpotent()
            True

            sage: S = R.change_ring(QQ)
            sage: S(g).is_nilpotent()
            False
            sage: S(g.O(4)).is_nilpotent()
            False
        """
    def degree(self):
        """
        Return degree of underlying polynomial of ``self``.

        EXAMPLES::

            sage: B.<x,y> = PowerSeriesRing(QQ)
            sage: B
            Multivariate Power Series Ring in x, y over Rational Field
            sage: r = 1 - x*y + x^2
            sage: r = r.add_bigoh(4); r
            1 + x^2 - x*y + O(x, y)^4
            sage: r.degree()
            2
        """
    def is_unit(self):
        """
        A multivariate power series is a unit if and only if its constant
        coefficient is a unit.

        EXAMPLES::

            sage: R.<a,b> = PowerSeriesRing(ZZ); R
            Multivariate Power Series Ring in a, b over Integer Ring
            sage: f = 2 + a^2 + a*b + a^3 + R.O(9)
            sage: f.is_unit()
            False
            sage: f.base_extend(QQ).is_unit()
            True
            sage: (O(a,b)^0).is_unit()
            False
        """
    def padded_list(self) -> None:
        """
        Method from univariate power series not yet implemented.

        TESTS::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(5)
            sage: f.padded_list()
            Traceback (most recent call last):
            ...
            NotImplementedError: padded_list
        """
    def is_square(self) -> None:
        """
        Method from univariate power series not yet implemented.

        TESTS::

            sage: T.<a,b> = PowerSeriesRing(ZZ, 2)
            sage: f = a + b + a*b + T.O(5)
            sage: f.is_square()
            Traceback (most recent call last):
            ...
            NotImplementedError: is_square
        """
    def square_root(self) -> None:
        """
        Method from univariate power series not yet implemented.
        Depends on square root method for multivariate polynomials.

        TESTS::

            sage: T.<a,b> = PowerSeriesRing(ZZ, 2)
            sage: f = a + b + a*b + T.O(5)
            sage: f.square_root()
            Traceback (most recent call last):
            ...
            NotImplementedError: square_root
        """
    sqrt = square_root
    def derivative(self, *args):
        """
        The formal derivative of this power series, with respect to
        variables supplied in ``args``.

        EXAMPLES::

            sage: T.<a,b> = PowerSeriesRing(ZZ, 2)
            sage: f = a + b + a^2*b + T.O(5)
            sage: f.derivative(a)
            1 + 2*a*b + O(a, b)^4
            sage: f.derivative(a,2)
            2*b + O(a, b)^3
            sage: f.derivative(a,a)
            2*b + O(a, b)^3
            sage: f.derivative([a,a])
            2*b + O(a, b)^3
            sage: f.derivative(a,5)
            0 + O(a, b)^0
            sage: f.derivative(a,6)
            0 + O(a, b)^0
        """
    def integral(self, *args):
        """
        The formal integral of this multivariate power series, with respect to
        variables supplied in ``args``.

        The variable sequence ``args`` can contain both variables and
        counts; for the syntax, see
        :meth:`~sage.misc.derivative.derivative_parse`.

        EXAMPLES::

            sage: T.<a,b> = PowerSeriesRing(QQ, 2)
            sage: f = a + b + a^2*b + T.O(5)
            sage: f.integral(a, 2)
            1/6*a^3 + 1/2*a^2*b + 1/12*a^4*b + O(a, b)^7
            sage: f.integral(a, b)
            1/2*a^2*b + 1/2*a*b^2 + 1/6*a^3*b^2 + O(a, b)^7
            sage: f.integral(a, 5)
            1/720*a^6 + 1/120*a^5*b + 1/2520*a^7*b + O(a, b)^10

        Only integration with respect to variables works::

            sage: f.integral(a + b)
            Traceback (most recent call last):
            ...
            ValueError: a + b is not a variable

        .. warning:: Coefficient division.

            If the base ring is not a field (e.g. `ZZ`), or if it has a
            nonzero characteristic, (e.g. `ZZ/3ZZ`), integration is not
            always possible while staying with the same base ring. In the
            first case, Sage will report that it has not been able to
            coerce some coefficient to the base ring::

                sage: T.<a,b> = PowerSeriesRing(ZZ, 2)
                sage: f = a + T.O(5)
                sage: f.integral(a)
                Traceback (most recent call last):
                ...
                TypeError: no conversion of this rational to integer

            One can get the correct result by changing the base ring first::

                sage: f.change_ring(QQ).integral(a)
                1/2*a^2 + O(a, b)^6

            However, a correct result is returned even without base change
            if the denominator cancels::

                sage: f = 2*b + T.O(5)
                sage: f.integral(b)
                b^2 + O(a, b)^6

            In nonzero characteristic, Sage will report that a zero division
            occurred ::

                sage: T.<a,b> = PowerSeriesRing(Zmod(3), 2)
                sage: (a^3).integral(a)
                a^4
                sage: (a^2).integral(a)
                Traceback (most recent call last):
                ...
                ZeroDivisionError: inverse of Mod(0, 3) does not exist
        """
    def ogf(self) -> None:
        """
        Method from univariate power series not yet implemented.

        TESTS::

            sage: T.<a,b> = PowerSeriesRing(ZZ, 2)
            sage: f = a + b + a*b + T.O(5)
            sage: f.ogf()
            Traceback (most recent call last):
            ...
            NotImplementedError: ogf
        """
    def egf(self) -> None:
        """
        Method from univariate power series not yet implemented.

        TESTS::

            sage: T.<a,b> = PowerSeriesRing(ZZ, 2)
            sage: f = a + b + a*b + T.O(5)
            sage: f.egf()
            Traceback (most recent call last):
            ...
            NotImplementedError: egf
        """
    def __pari__(self) -> None:
        """
        Method from univariate power series not yet implemented.

        TESTS::

            sage: T.<a,b> = PowerSeriesRing(ZZ, 2)
            sage: f = a + b + a*b + T.O(5)
            sage: f.__pari__()
            Traceback (most recent call last):
            ...
            NotImplementedError: __pari__
        """
    def list(self) -> None:
        """
        Doesn't make sense for multivariate power series.
        Multivariate polynomials don't have list of coefficients either.

        TESTS::

            sage: T.<a,b> = PowerSeriesRing(ZZ, 2)
            sage: f = a + b + a*b + T.O(5)
            sage: f.list()
            Traceback (most recent call last):
            ...
            NotImplementedError: Multivariate power series do not have list
            of coefficients; use 'coefficients' to get a dict of coefficients.
        """
    def variable(self) -> None:
        """
        Doesn't make sense for multivariate power series.

        TESTS::

            sage: T.<a,b> = PowerSeriesRing(ZZ, 2)
            sage: f = a + b + a*b + T.O(5)
            sage: f.variable()
            Traceback (most recent call last):
            ...
            NotImplementedError: variable not defined for multivariate power
            series; use 'variables' instead.
        """
    def shift(self, n) -> None:
        """
        Doesn't make sense for multivariate power series.

        TESTS::

            sage: T.<a,b> = PowerSeriesRing(ZZ, 2)
            sage: f = a + b + a*b + T.O(5)
            sage: f.shift(3)
            Traceback (most recent call last):
            ...
            NotImplementedError: shift not defined for multivariate power series.
        """
    def __lshift__(self, n) -> None:
        """
        Doesn't make sense for multivariate power series.

        TESTS::

            sage: T.<a,b> = PowerSeriesRing(ZZ, 2)
            sage: f = a + b + a*b + T.O(5)
            sage: f.__lshift__(3)
            Traceback (most recent call last):
            ...
            NotImplementedError: __lshift__ not defined for multivariate power series.
        """
    def __rshift__(self, n) -> None:
        """
        Doesn't make sense for multivariate power series.

        TESTS::

            sage: T.<a,b> = PowerSeriesRing(ZZ, 2)
            sage: f = a + b + a*b + T.O(5)
            sage: f.__rshift__(3)
            Traceback (most recent call last):
            ...
            NotImplementedError: __rshift__ not defined for multivariate power series.
        """
    def valuation_zero_part(self) -> None:
        """
        Doesn't make sense for multivariate power series;
        valuation zero with respect to which variable?

        TESTS::

            sage: T.<a,b> = PowerSeriesRing(ZZ, 2)
            sage: f = a + b + a*b + T.O(5)
            sage: f.valuation_zero_part()
            Traceback (most recent call last):
            ...
            NotImplementedError: valuation_zero_part not defined for multivariate
            power series; perhaps 'constant_coefficient' is what you want.
        """
    def solve_linear_de(self, prec=..., b=None, f0=None) -> None:
        """
        Not implemented for multivariate power series.

        TESTS::

            sage: T.<a,b> = PowerSeriesRing(ZZ, 2)
            sage: f = a + b + a*b + T.O(5)
            sage: f.solve_linear_de()
            Traceback (most recent call last):
            ...
            NotImplementedError: solve_linear_de not defined for multivariate power series.
        """
    def exp(self, prec=...):
        """
        Exponentiate the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT:

        The exponentiated multivariate power series as a new
        multivariate power series.

        EXAMPLES::

            sage: T.<a,b> = PowerSeriesRing(ZZ, 2)
            sage: f = a + b + a*b + T.O(3)
            sage: exp(f)
            1 + a + b + 1/2*a^2 + 2*a*b + 1/2*b^2 + O(a, b)^3
            sage: f.exp()
            1 + a + b + 1/2*a^2 + 2*a*b + 1/2*b^2 + O(a, b)^3
            sage: f.exp(prec=2)
            1 + a + b + O(a, b)^2
            sage: log(exp(f)) - f
            0 + O(a, b)^3

        If the power series has a constant coefficient `c` and
        `\\exp(c)` is transcendental, then `\\exp(f)` would have to be a
        power series over the :class:`~sage.symbolic.ring.SymbolicRing`. These
        are not yet implemented and therefore such cases raise an error::

            sage: g = 2 + f
            sage: exp(g)                                                                # needs sage.symbolic
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for *: 'Symbolic Ring' and
            'Power Series Ring in Tbg over Multivariate Polynomial Ring in a, b
            over Rational Field'

        Another workaround for this limitation is to change base ring
        to one which is closed under exponentiation, such as `\\RR` or `\\CC`::

            sage: exp(g.change_ring(RDF))
            7.38905609... + 7.38905609...*a + 7.38905609...*b + 3.69452804...*a^2 +
            14.7781121...*a*b + 3.69452804...*b^2 + O(a, b)^3

        If no precision is specified, the default precision is used::

            sage: T.default_prec()
            12
            sage: exp(a)
            1 + a + 1/2*a^2 + 1/6*a^3 + 1/24*a^4 + 1/120*a^5 + 1/720*a^6 + 1/5040*a^7 +
            1/40320*a^8 + 1/362880*a^9 + 1/3628800*a^10 + 1/39916800*a^11 + O(a, b)^12
            sage: a.exp(prec=5)
            1 + a + 1/2*a^2 + 1/6*a^3 + 1/24*a^4 + O(a, b)^5
            sage: exp(a + T.O(5))
            1 + a + 1/2*a^2 + 1/6*a^3 + 1/24*a^4 + O(a, b)^5

        TESTS::

            sage: exp(a^2 + T.O(5))
            1 + a^2 + 1/2*a^4 + O(a, b)^5
        """
    def log(self, prec=...):
        """
        Return the logarithm of the formal power series.

        INPUT:

        - ``prec`` -- integer or ``infinity``; the degree to truncate
          the result to

        OUTPUT:

        The logarithm of the multivariate power series as a new
        multivariate power series.

        EXAMPLES::

            sage: T.<a,b> = PowerSeriesRing(ZZ, 2)
            sage: f = 1 + a + b + a*b + T.O(5)
            sage: f.log()
            a + b - 1/2*a^2 - 1/2*b^2 + 1/3*a^3 + 1/3*b^3 - 1/4*a^4 - 1/4*b^4 + O(a, b)^5
            sage: log(f)
            a + b - 1/2*a^2 - 1/2*b^2 + 1/3*a^3 + 1/3*b^3 - 1/4*a^4 - 1/4*b^4 + O(a, b)^5
            sage: exp(log(f)) - f
            0 + O(a, b)^5

        If the power series has a constant coefficient `c` and
        `\\exp(c)` is transcendental, then `\\exp(f)` would have to be a
        power series over the :class:`~sage.symbolic.ring.SymbolicRing`. These
        are not yet implemented and therefore such cases raise an error::

            sage: g = 2 + f
            sage: log(g)                                                                # needs sage.symbolic
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for -: 'Symbolic Ring' and 'Power
            Series Ring in Tbg over Multivariate Polynomial Ring in a, b over Rational Field'

        Another workaround for this limitation is to change base ring
        to one which is closed under exponentiation, such as `\\RR` or `\\CC`::

            sage: log(g.change_ring(RDF))
            1.09861228... + 0.333333333...*a + 0.333333333...*b - 0.0555555555...*a^2
            + 0.222222222...*a*b - 0.0555555555...*b^2 + 0.0123456790...*a^3
            - 0.0740740740...*a^2*b - 0.0740740740...*a*b^2 + 0.0123456790...*b^3
            - 0.00308641975...*a^4 + 0.0246913580...*a^3*b + 0.0246913580...*a*b^3
            - 0.00308641975...*b^4 + O(a, b)^5

        TESTS::

            sage: (1+a).log(prec=10).exp()
            1 + a + O(a, b)^10
            sage: a.exp(prec=10).log()
            a + O(a, b)^10

            sage: log(1+a)
            a - 1/2*a^2 + 1/3*a^3 - 1/4*a^4 + 1/5*a^5 - 1/6*a^6 + 1/7*a^7
            - 1/8*a^8 + 1/9*a^9 - 1/10*a^10 + 1/11*a^11 + O(a, b)^12
            sage: -log(1-a+T.O(5))
            a + 1/2*a^2 + 1/3*a^3 + 1/4*a^4 + O(a, b)^5
            sage: a.log(prec=10)
            Traceback (most recent call last):
            ...
            ValueError: Can only take formal power series for nonzero constant term.
        """
    def laurent_series(self) -> None:
        """
        Not implemented for multivariate power series.

        TESTS::

            sage: T.<a,b> = PowerSeriesRing(ZZ,2)
            sage: f = a + b + a*b + T.O(5)
            sage: f.laurent_series()
            Traceback (most recent call last):
            ...
            NotImplementedError: laurent_series not defined for multivariate power series.
        """

class MO:
    """
    Object representing a zero element with given precision.

    EXAMPLES::

        sage: R.<u,v> = QQ[[]]
        sage: m = O(u, v)
        sage: m^4
        0 + O(u, v)^4
        sage: m^1
        0 + O(u, v)^1

        sage: T.<a,b,c> = PowerSeriesRing(ZZ, 3)
        sage: z = O(a, b, c)
        sage: z^1
        0 + O(a, b, c)^1
        sage: 1 + a + z^1
        1 + O(a, b, c)^1

        sage: w = 1 + a + O(a, b, c)^2; w
        1 + a + O(a, b, c)^2
        sage: w^2
        1 + 2*a + O(a, b, c)^2
    """
    def __init__(self, x) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: R.<u,v> = QQ[[]]
            sage: m = O(u, v)
        """
    def __pow__(self, prec):
        """
        Raise ``self`` to the given precision ``prec``.

        EXAMPLES::

            sage: R.<u,v> = QQ[[]]
            sage: m = O(u, v)
            sage: m^4
            0 + O(u, v)^4
        """
