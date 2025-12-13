from sage.arith.misc import binomial as binomial, prime_divisors as prime_divisors, valuation as valuation
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.functional import denominator as denominator
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.verbose import get_verbose as get_verbose, verbose as verbose
from sage.modules.free_module_element import vector as vector
from sage.rings.infinity import infinity as infinity
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.laurent_series_ring import LaurentSeriesRing as LaurentSeriesRing
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.power_series_ring import PowerSeriesRing as PowerSeriesRing
from sage.rings.rational_field import QQ as QQ
from sage.structure.richcmp import richcmp as richcmp, richcmp_method as richcmp_method
from sage.structure.sage_object import SageObject as SageObject

class pAdicLseries(SageObject):
    """
    The `p`-adic `L`-series of an elliptic curve.

    EXAMPLES:

    An ordinary example::

        sage: e = EllipticCurve('389a')
        sage: L = e.padic_lseries(5)
        sage: L.series(0)
        Traceback (most recent call last):
        ...
        ValueError: n (=0) must be a positive integer
        sage: L.series(1)
        O(T^1)
        sage: L.series(2)
        O(5^4) + O(5)*T + (4 + O(5))*T^2 + (2 + O(5))*T^3 + (3 + O(5))*T^4 + O(T^5)
        sage: L.series(3, prec=10)
        O(5^5) + O(5^2)*T + (4 + 4*5 + O(5^2))*T^2 + (2 + 4*5 + O(5^2))*T^3 + (3 + O(5^2))*T^4 + (1 + O(5))*T^5 + O(5)*T^6 + (4 + O(5))*T^7 + (2 + O(5))*T^8 + O(5)*T^9 + O(T^10)
        sage: L.series(2,quadratic_twist=-3)
        2 + 4*5 + 4*5^2 + O(5^4) + O(5)*T + (1 + O(5))*T^2 + (4 + O(5))*T^3 + O(5)*T^4 + O(T^5)

    A prime p such that E[p] is reducible::

        sage: L = EllipticCurve('11a').padic_lseries(5)
        sage: L.series(1)
        5 + O(5^2) + O(T)
        sage: L.series(2)
        5 + 4*5^2 + O(5^3) + O(5^0)*T + O(5^0)*T^2 + O(5^0)*T^3 + O(5^0)*T^4 + O(T^5)
        sage: L.series(3)
        5 + 4*5^2 + 4*5^3 + O(5^4) + O(5)*T + O(5)*T^2 + O(5)*T^3 + O(5)*T^4 + O(T^5)

    An example showing the calculation of nontrivial Teichmueller twists::

        sage: E = EllipticCurve('11a1')
        sage: lp = E.padic_lseries(7)
        sage: lp.series(4,eta=1)
        3 + 7^3 + 6*7^4 + 3*7^5 + O(7^6) + (2*7 + 7^2 + O(7^3))*T + (1 + 5*7^2 + O(7^3))*T^2 + (4 + 4*7 + 4*7^2 + O(7^3))*T^3 + (4 + 3*7 + 7^2 + O(7^3))*T^4 + O(T^5)
        sage: lp.series(4,eta=2)
        5 + 6*7 + 4*7^2 + 2*7^3 + 3*7^4 + 2*7^5 + O(7^6) + (6 + 4*7 + 7^2 + O(7^3))*T + (3 + 2*7^2 + O(7^3))*T^2 + (1 + 4*7 + 7^2 + O(7^3))*T^3 + (6 + 6*7 + 6*7^2 + O(7^3))*T^4 + O(T^5)
        sage: lp.series(4,eta=3)
        O(7^6) + (5 + 4*7 + 2*7^2 + O(7^3))*T + (6 + 5*7 + 2*7^2 + O(7^3))*T^2 + (5*7 + O(7^3))*T^3 + (7 + 4*7^2 + O(7^3))*T^4 + O(T^5)

    (Note that the last series vanishes at `T = 0`, which is consistent with ::

        sage: E.quadratic_twist(-7).rank()
        1

    This proves that `E` has rank 1 over `\\QQ(\\zeta_7)`.)

    TESTS:

    The load-dumps test::

        sage: lp = EllipticCurve('11a').padic_lseries(5)
        sage: lp == loads(dumps(lp))
        True
    """
    def __init__(self, E, p, implementation: str = 'eclib', normalize: str = 'L_ratio') -> None:
        """
        INPUT:

        - ``E`` -- an elliptic curve
        - ``p`` -- a prime of good reduction
        - ``implementation`` -- string (default: ``'eclib'``); either
          ``'eclib'`` to use John Cremona's ``eclib`` for the computation of
          modular symbols, 'num' to use numerical modular symbols or ``'sage'``
          to use Sage's own implementation
        - ``normalize`` -- ``'L_ratio'`` (default), ``'period'`` or ``'none'``;
          this is describes the way the modular symbols are normalized. See
          ``modular_symbol`` of an elliptic curve over Q for more details.

        EXAMPLES::

            sage: E = EllipticCurve('11a1')
            sage: Lp = E.padic_lseries(3)
            sage: Lp.series(2,prec=3)
            2 + 3 + 3^2 + 2*3^3 + O(3^4) + (1 + O(3))*T + (1 + O(3))*T^2 + O(T^3)
        """
    def __richcmp__(self, other, op):
        """
        Compare ``self`` and ``other``.

        TESTS::

            sage: lp1 = EllipticCurve('11a1').padic_lseries(5)
            sage: lp2 = EllipticCurve('11a1').padic_lseries(7)
            sage: lp3 = EllipticCurve('11a2').padic_lseries(5)
            sage: lp1 == lp1
            True
            sage: lp1 == lp2
            False
            sage: lp1 == lp3
            False
        """
    def elliptic_curve(self):
        """
        Return the elliptic curve to which this `p`-adic `L`-series is associated.

        EXAMPLES::

            sage: L = EllipticCurve('11a').padic_lseries(5)
            sage: L.elliptic_curve()
            Elliptic Curve defined by y^2 + y = x^3 - x^2 - 10*x - 20 over Rational Field
        """
    def prime(self):
        """
        Return the prime `p` as in `p`-adic `L`-function'.

        EXAMPLES::

            sage: L = EllipticCurve('11a').padic_lseries(5)
            sage: L.prime()
            5
        """
    def modular_symbol(self, r, sign: int = +1, quadratic_twist: int = +1):
        """
        Return the modular symbol evaluated at `r`.

        This is used to compute this `p`-adic `L`-series.

        Note that the normalization is not correct at this
        stage: use ``_quotient_of periods_to_twist`` to correct.

        Note also that this function does not check if the condition
        on the quadratic_twist=D is satisfied. So the result will only
        be correct if for each prime `\\ell` dividing `D`, we have
        `ord_{\\ell}(N)<= ord_{\\ell}(D)`, where `N` is the conductor of the curve.

        INPUT:

        - ``r`` -- a cusp given as either a rational number or oo

        - ``sign`` -- +1 (default) or -1 (only implemented without twists)

        - ``quadratic_twist`` -- a fundamental discriminant of a quadratic field or +1 (default)

        EXAMPLES::

            sage: E = EllipticCurve('11a1')
            sage: lp = E.padic_lseries(5)
            sage: [lp.modular_symbol(r) for r in [0,1/5,oo,1/11]]
            [1/5, 6/5, 0, 0]
            sage: [lp.modular_symbol(r,sign=-1) for r in [0,1/3,oo,1/7]]
            [0, 1/2, 0, -1/2]
            sage: [lp.modular_symbol(r,quadratic_twist=-20) for r in [0,1/5,oo,1/11]]
            [1, 1, 0, 1/2]

            sage: E = EllipticCurve('20a1')
            sage: Et = E.quadratic_twist(-4)
            sage: lpt = Et.padic_lseries(5)
            sage: eta = lpt._quotient_of_periods_to_twist(-4)
            sage: lpt.modular_symbol(0) == lp.modular_symbol(0,quadratic_twist=-4) / eta
            True
        """
    def measure(self, a, n, prec, quadratic_twist: int = +1, sign: int = +1):
        """
        Return the measure on `\\ZZ_p^{\\times}` defined by

            `\\mu_{E,\\alpha}^+ ( a + p^n \\ZZ_p  ) =
            \\frac{1}{\\alpha^n} \\left [\\frac{a}{p^n}\\right]^{+} -
            \\frac{1}{\\alpha^{n+1}} \\left[\\frac{a}{p^{n-1}}\\right]^{+}`

        where `[\\cdot]^{+}` is the modular symbol. This is used to define
        this `p`-adic `L`-function (at least when the reduction is good).

        The optional argument ``sign`` allows the minus symbol `[\\cdot]^{-}` to
        be substituted for the plus symbol.

        The optional argument ``quadratic_twist`` replaces `E` by the twist in
        the above formula, but the twisted modular symbol is computed using a
        sum over modular symbols of `E` rather than finding the modular symbols
        for the twist. Quadratic twists are only implemented if the sign is
        `+1`.

        Note that the normalization is not correct at this
        stage: use  ``_quotient_of periods`` and ``_quotient_of periods_to_twist``
        to correct.

        Note also that this function does not check if the condition
        on the ``quadratic_twist=D`` is satisfied. So the result will only
        be correct if for each prime `\\ell` dividing `D`, we have
        `ord_{\\ell}(N)<= ord_{\\ell}(D)`, where `N` is the conductor of the curve.

        INPUT:

        - ``a`` -- integer

        - ``n`` -- nonnegative integer

        - ``prec`` -- integer

        - ``quadratic_twist`` -- (default: 1) a fundamental discriminant of a
          quadratic field, should be coprime to the conductor of `E`

        - ``sign`` -- integer (default: 1) which should be `\\pm 1`

        EXAMPLES::

            sage: E = EllipticCurve('37a')
            sage: L = E.padic_lseries(5)
            sage: L.measure(1,2, prec=9)
            2 + 3*5 + 4*5^3 + 2*5^4 + 3*5^5 + 3*5^6 + 4*5^7 + 4*5^8 + O(5^9)
            sage: L.measure(1,2, quadratic_twist=8,prec=15)
            O(5^15)
            sage: L.measure(1,2, quadratic_twist=-4,prec=15)
            4 + 4*5 + 4*5^2 + 3*5^3 + 2*5^4 + 5^5 + 3*5^6 + 5^8 + 2*5^9 + 3*5^12 + 2*5^13 + 4*5^14 + O(5^15)

            sage: E = EllipticCurve('11a1')
            sage: a = E.quadratic_twist(-3).padic_lseries(5).measure(1,2,prec=15)
            sage: b = E.padic_lseries(5).measure(1,2, quadratic_twist=-3,prec=15)
            sage: a == b * E.padic_lseries(5)._quotient_of_periods_to_twist(-3)
            True
        """
    def alpha(self, prec: int = 20):
        """
        Return a `p`-adic root `\\alpha` of the polynomial `x^2 - a_p x
        + p` with `ord_p(\\alpha) < 1`.  In the ordinary case this is
        just the unit root.

        INPUT:

        - ``prec`` -- positive integer; the `p`-adic precision of the root

        EXAMPLES:

        Consider the elliptic curve 37a::

            sage: E = EllipticCurve('37a')

        An ordinary prime::

            sage: L = E.padic_lseries(5)
            sage: alpha = L.alpha(10); alpha
            3 + 2*5 + 4*5^2 + 2*5^3 + 5^4 + 4*5^5 + 2*5^7 + 5^8 + 5^9 + O(5^10)
            sage: alpha^2 - E.ap(5)*alpha + 5
            O(5^10)

        A supersingular prime::

            sage: L = E.padic_lseries(3)
            sage: alpha = L.alpha(10); alpha
            alpha + O(alpha^21)
            sage: alpha^2 - E.ap(3)*alpha + 3
            O(alpha^22)

        A reducible prime::

            sage: L = EllipticCurve('11a').padic_lseries(5)
            sage: L.alpha(5)
            1 + 4*5 + 3*5^2 + 2*5^3 + 4*5^4 + O(5^5)
        """
    def order_of_vanishing(self):
        """
        Return the order of vanishing of this `p`-adic `L`-series.

        The output of this function is provably correct, due to a
        theorem of Kato [Kat2004]_.

        .. NOTE:: currently `p` must be a prime of good ordinary reduction.

        REFERENCES:

        - [MTT1986]_

        - [Kat2004]_

        EXAMPLES::

            sage: L = EllipticCurve('11a').padic_lseries(3)
            sage: L.order_of_vanishing()
            0
            sage: L = EllipticCurve('11a').padic_lseries(5)
            sage: L.order_of_vanishing()
            0
            sage: L = EllipticCurve('37a').padic_lseries(5)
            sage: L.order_of_vanishing()
            1
            sage: L = EllipticCurve('43a').padic_lseries(3)
            sage: L.order_of_vanishing()
            1
            sage: L = EllipticCurve('37b').padic_lseries(3)
            sage: L.order_of_vanishing()
            0
            sage: L = EllipticCurve('389a').padic_lseries(3)
            sage: L.order_of_vanishing()
            2
            sage: L = EllipticCurve('389a').padic_lseries(5)
            sage: L.order_of_vanishing()
            2
            sage: L = EllipticCurve('5077a').padic_lseries(5, implementation = 'eclib')
            sage: L.order_of_vanishing()
            3
        """
    def teichmuller(self, prec):
        """
        Return Teichmuller lifts to the given precision.

        INPUT:

        - ``prec`` -- positive integer

        OUTPUT: list of `p`-adic numbers; the cached Teichmuller lifts

        EXAMPLES::

            sage: L = EllipticCurve('11a').padic_lseries(7)
            sage: L.teichmuller(1)
            [0, 1, 2, 3, 4, 5, 6]
            sage: L.teichmuller(2)
            [0, 1, 30, 31, 18, 19, 48]
        """

class pAdicLseriesOrdinary(pAdicLseries):
    def series(self, n: int = 2, quadratic_twist: int = +1, prec: int = 5, eta: int = 0):
        '''
        Return the `n`-th approximation to the `p`-adic `L`-series, in the
        component corresponding to the `\\eta`-th power of the Teichmueller
        character, as a power series in `T` (corresponding to `\\gamma-1` with
        `\\gamma=1+p` as a generator of `1+p\\ZZ_p`). Each coefficient is a
        `p`-adic number whose precision is provably correct.

        Here the normalization of the `p`-adic `L`-series is chosen
        such that `L_p(E,1) = (1-1/\\alpha)^2 L(E,1)/\\Omega_E`
        where `\\alpha` is the unit root of the characteristic
        polynomial of Frobenius on `T_pE` and `\\Omega_E` is the
        Néron period of `E`.

        INPUT:

        - ``n`` -- (default: 2) a positive integer
        - ``quadratic_twist`` -- (default: +1) a fundamental discriminant of a
          quadratic field, coprime to the conductor of the curve
        - ``prec`` -- (default: 5) maximal number of terms of the series to
          compute; to compute as many as possible just give a very large
          number for ``prec``; the result will still be correct.
        - ``eta`` -- (default: 0) an integer (specifying the power of the
          Teichmueller character on the group of roots of unity in
          `\\ZZ_p^\\times`)

        :meth:`power_series` is identical to ``series``.

        EXAMPLES:

        We compute some `p`-adic `L`-functions associated to the elliptic
        curve 11a::

            sage: E = EllipticCurve(\'11a\')
            sage: p = 3
            sage: E.is_ordinary(p)
            True
            sage: L = E.padic_lseries(p)
            sage: L.series(3)
            2 + 3 + 3^2 + 2*3^3 + O(3^5) + (1 + 3 + O(3^2))*T + (1 + 2*3 + O(3^2))*T^2 + O(3)*T^3 + O(3)*T^4 + O(T^5)

        Another example at a prime of bad reduction, where the
        `p`-adic `L`-function has an extra 0 (compared to the non
        `p`-adic `L`-function)::

            sage: E = EllipticCurve(\'11a\')
            sage: p = 11
            sage: E.is_ordinary(p)
            True
            sage: L = E.padic_lseries(p)
            sage: L.series(2)
            O(11^4) + (10 + O(11))*T + (6 + O(11))*T^2 + (2 + O(11))*T^3 + (5 + O(11))*T^4 + O(T^5)

        We compute a `p`-adic `L`-function that vanishes to order 2::

            sage: E = EllipticCurve(\'389a\')
            sage: p = 3
            sage: E.is_ordinary(p)
            True
            sage: L = E.padic_lseries(p)
            sage: L.series(1)
            O(T^1)
            sage: L.series(2)
            O(3^4) + O(3)*T + (2 + O(3))*T^2 + O(T^3)
            sage: L.series(3)
            O(3^5) + O(3^2)*T + (2 + 2*3 + O(3^2))*T^2 + (2 + O(3))*T^3 + (1 + O(3))*T^4 + O(T^5)

        Checks if the precision can be changed (:issue:`5846`)::

            sage: L.series(3,prec=4)
            O(3^5) + O(3^2)*T + (2 + 2*3 + O(3^2))*T^2 + (2 + O(3))*T^3 + O(T^4)
            sage: L.series(3,prec=6)
            O(3^5) + O(3^2)*T + (2 + 2*3 + O(3^2))*T^2 + (2 + O(3))*T^3 + (1 + O(3))*T^4 + (1 + O(3))*T^5 + O(T^6)

        Rather than computing the `p`-adic `L`-function for the curve \'15523a1\', one can
        compute it as a quadratic_twist::

            sage: E = EllipticCurve(\'43a1\')
            sage: lp = E.padic_lseries(3)
            sage: lp.series(2,quadratic_twist=-19)
            2 + 2*3 + 2*3^2 + O(3^4) + (1 + O(3))*T + (1 + O(3))*T^2 + O(T^3)
            sage: E.quadratic_twist(-19).label()    # optional -- database_cremona_ellcurve
            \'15523a1\'

        This proves that the rank of \'15523a1\' is zero, even if ``mwrank`` cannot determine this.

        We calculate the `L`-series in the nontrivial Teichmueller components::

            sage: L = EllipticCurve(\'110a1\').padic_lseries(5, implementation=\'sage\')
            sage: for j in [0..3]: print(L.series(4, eta=j))
            O(5^6) + (2 + 2*5 + 2*5^2 + O(5^3))*T + (5 + 5^2 + O(5^3))*T^2 + (4 + 4*5 + 2*5^2 + O(5^3))*T^3 + (1 + 5 + 3*5^2 + O(5^3))*T^4 + O(T^5)
            4 + 3*5 + 2*5^2 + 3*5^3 + 5^4 + O(5^6) + (1 + 3*5 + 4*5^2 + O(5^3))*T + (3 + 4*5 + 3*5^2 + O(5^3))*T^2 + (3 + 3*5^2 + O(5^3))*T^3 + (1 + 2*5 + 2*5^2 + O(5^3))*T^4 + O(T^5)
            2 + O(5^6) + (1 + 5 + O(5^3))*T + (2 + 4*5 + 3*5^2 + O(5^3))*T^2 + (4 + 5 + 2*5^2 + O(5^3))*T^3 + (4 + O(5^3))*T^4 + O(T^5)
            3 + 5 + 2*5^2 + 5^3 + 3*5^4 + 4*5^5 + O(5^6) + (1 + 2*5 + 4*5^2 + O(5^3))*T + (1 + 4*5 + O(5^3))*T^2 + (3 + 2*5 + 2*5^2 + O(5^3))*T^3 + (5 + 5^2 + O(5^3))*T^4 + O(T^5)

        It should now also work with `p=2` (:issue:`20798`)::

            sage: E = EllipticCurve("53a1")
            sage: lp = E.padic_lseries(2)
            sage: lp.series(7)
            O(2^8) + (1 + 2^2 + 2^3 + O(2^5))*T + (1 + 2^3 + O(2^4))*T^2 + (2^2 + 2^3 + O(2^4))*T^3 + (2 + 2^2 + O(2^3))*T^4 + O(T^5)

            sage: E = EllipticCurve("109a1")
            sage: lp = E.padic_lseries(2)
            sage: lp.series(6)
            2^2 + 2^6 + O(2^7) + (2 + O(2^4))*T + O(2^3)*T^2 + (2^2 + O(2^3))*T^3 + (2 + O(2^2))*T^4 + O(T^5)

        Check that twists by odd Teichmuller characters are ok (:issue:`32258`)::

            sage: E = EllipticCurve("443c1")
            sage: lp = E.padic_lseries(17, implementation=\'num\')
            sage: l8 = lp.series(2,eta=8,prec=3)
            sage: l8.list()[0] - 1/lp.alpha()
            O(17^4)
            sage: lp = E.padic_lseries(2, implementation=\'num\')
            sage: l1 = lp.series(8,eta=1,prec=3)
            sage: l1.list()[0] - 4/lp.alpha()^2
            O(2^9)
        '''
    power_series = series
    def is_ordinary(self):
        """
        Return ``True`` if the elliptic curve that this `L`-function is attached
        to is ordinary.

        EXAMPLES::

            sage: L = EllipticCurve('11a').padic_lseries(5)
            sage: L.is_ordinary()
            True
        """
    def is_supersingular(self):
        """
        Return ``True`` if the elliptic curve that this L function is attached
        to is supersingular.

        EXAMPLES::

            sage: L = EllipticCurve('11a').padic_lseries(5)
            sage: L.is_supersingular()
            False
        """

class pAdicLseriesSupersingular(pAdicLseries):
    def series(self, n: int = 3, quadratic_twist: int = +1, prec: int = 5, eta: int = 0):
        '''
        Return the `n`-th approximation to the `p`-adic `L`-series as a
        power series in `T` (corresponding to `\\gamma-1` with
        `\\gamma=1+p` as a generator of `1+p\\ZZ_p`).  Each
        coefficient is an element of a quadratic extension of the `p`-adic
        number whose precision is provably correct.

        Here the normalization of the `p`-adic `L`-series is chosen
        such that `L_p(E,1) = (1-1/\\alpha)^2 L(E,1)/\\Omega_E`
        where `\\alpha` is a root of the characteristic
        polynomial of Frobenius on `T_pE` and `\\Omega_E` is the
        Néron period of `E`.

        INPUT:

        - ``n`` -- (default: 2) a positive integer
        - ``quadratic_twist`` -- (default: +1) a fundamental discriminant of a
          quadratic field, coprime to the conductor of the curve
        - ``prec`` -- (default: 5) maximal number of terms of the series to
          compute; to compute as many as possible just give a very large
          number for ``prec``; the result will still be correct.
        - ``eta`` -- (default: 0) an integer (specifying the power of the
          Teichmueller character on the group of roots of unity in
          `\\ZZ_p^\\times`)

        OUTPUT:

        a power series with coefficients in a quadratic ramified extension of
        the `p`-adic numbers generated by a root `alpha` of the characteristic
        polynomial of Frobenius on `T_pE`.

        ALIAS: power_series is identical to series.

        EXAMPLES:

        A supersingular example, where we must compute to higher precision to see anything::

            sage: e = EllipticCurve(\'37a\')
            sage: L = e.padic_lseries(3); L
            3-adic L-series of Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field
            sage: L.series(2)
            O(T^3)
            sage: L.series(4)         # takes a long time (several seconds)
            O(alpha) + (alpha^-2 + O(alpha^0))*T + (alpha^-2 + O(alpha^0))*T^2 + O(T^5)
            sage: L.alpha(2).parent()
            3-adic Eisenstein Extension Field in alpha defined by x^2 + 3*x + 3

        An example where we only compute the leading term (:issue:`15737`)::

            sage: E = EllipticCurve("17a1")
            sage: L = E.padic_lseries(3)
            sage: L.series(4,prec=1)
            alpha^-2 + alpha^-1 + 2 + 2*alpha + ... + O(alpha^38) + O(T)

        It works also for `p=2`::

            sage: E = EllipticCurve("11a1")
            sage: lp = E.padic_lseries(2)
            sage: lp.series(10)
            O(alpha^-3) + (alpha^-4 + O(alpha^-3))*T + (alpha^-4 + O(alpha^-3))*T^2 + (alpha^-5 + alpha^-4 + O(alpha^-3))*T^3 + (alpha^-4 + O(alpha^-3))*T^4 + O(T^5)
        '''
    power_series = series
    def is_ordinary(self):
        """
        Return ``True`` if the elliptic curve that this `L`-function is attached
        to is ordinary.

        EXAMPLES::

            sage: L = EllipticCurve('11a').padic_lseries(19)
            sage: L.is_ordinary()
            False
        """
    def is_supersingular(self):
        """
        Return ``True`` if the elliptic curve that this L function is attached
        to is supersingular.

        EXAMPLES::

            sage: L = EllipticCurve('11a').padic_lseries(19)
            sage: L.is_supersingular()
            True
        """
    def Dp_valued_series(self, n: int = 3, quadratic_twist: int = +1, prec: int = 5):
        """
        Return a vector of two components which are `p`-adic power series.

        The answer v is such that

            `(1-\\varphi)^{-2}\\cdot L_p(E,T) =` ``v[1]`` `\\cdot \\omega +` ``v[2]`` `\\cdot \\varphi(\\omega)`

        as an element of the Dieudonné module `D_p(E) = H^1_{dR}(E/\\QQ_p)` where
        `\\omega` is the invariant differential and `\\varphi` is the Frobenius on `D_p(E)`.

        According to the `p`-adic Birch and Swinnerton-Dyer
        conjecture [BP1993]_ this function has a zero of order
        rank of `E(\\QQ)` and it's leading term is contains the order of
        the Tate-Shafarevich group, the Tamagawa numbers, the order of the
        torsion subgroup and the `D_p`-valued `p`-adic regulator.

        INPUT:

        - ``n`` -- (default: 3) a positive integer
        - ``prec`` -- (default: 5) a positive integer

        EXAMPLES::

            sage: E = EllipticCurve('14a')
            sage: L = E.padic_lseries(5)
            sage: L.Dp_valued_series(4)  # long time (9s on sage.math, 2011)
            (1 + 4*5 + O(5^2) + (4 + O(5))*T + (1 + O(5))*T^2 + (4 + O(5))*T^3 + (2 + O(5))*T^4 + O(T^5), 5^2 + O(5^3) + O(5^2)*T + (4*5 + O(5^2))*T^2 + (2*5 + O(5^2))*T^3 + (2 + 2*5 + O(5^2))*T^4 + O(T^5))
        """
    def frobenius(self, prec: int = 20, algorithm: str = 'mw'):
        """
        Return a geometric Frobenius `\\varphi` on the Dieudonné module `D_p(E)`
        with respect to the basis `\\omega`, the invariant differential, and `\\eta=x\\omega`.

        It satisfies  `\\varphi^2 - a_p/p\\, \\varphi + 1/p = 0`.

        INPUT:

        - ``prec`` -- (default: 20) a positive integer

        - ``algorithm`` -- either 'mw' (default) for Monsky-Washnitzer
          or 'approx' for the algorithm described by Bernardi and Perrin-Riou
          (much slower and not fully tested)

        EXAMPLES::

            sage: E = EllipticCurve('14a')
            sage: L = E.padic_lseries(5)
            sage: phi = L.frobenius(5)
            sage: phi
            [                  2 + 5^2 + 5^4 + O(5^5)    3*5^-1 + 3 + 5 + 4*5^2 + 5^3 + O(5^4)]
            [      3 + 3*5^2 + 4*5^3 + 3*5^4 + O(5^5) 3 + 4*5 + 3*5^2 + 4*5^3 + 3*5^4 + O(5^5)]
            sage: -phi^2
            [5^-1 + O(5^4)        O(5^4)]
            [       O(5^5) 5^-1 + O(5^4)]
        """
    def bernardi_sigma_function(self, prec: int = 20):
        """
        Return the  `p`-adic sigma function of Bernardi in terms of `z = log(t)`.

        This is the same as ``padic_sigma`` with ``E2 = 0``.

        EXAMPLES::

            sage: E = EllipticCurve('14a')
            sage: L = E.padic_lseries(5)
            sage: L.bernardi_sigma_function(prec=5) # Todo: some sort of consistency check!?
            z + 1/24*z^3 + 29/384*z^5 - 8399/322560*z^7 - 291743/92897280*z^9 + O(z^10)
        """
    def Dp_valued_height(self, prec: int = 20):
        """
        Return the canonical `p`-adic height with values in the Dieudonné module `D_p(E)`.

        It is defined to be

            `h_{\\eta} \\cdot \\omega - h_{\\omega} \\cdot \\eta`

        where `h_{\\eta}` is made out of the sigma function of Bernardi and
        `h_{\\omega}` is `log_E^2`.

        The answer ``v`` is given as ``v[1]*omega + v[2]*eta``.
        The coordinates of ``v`` are dependent of the
        Weierstrass equation.

        EXAMPLES::

            sage: E = EllipticCurve('53a')
            sage: L = E.padic_lseries(5)
            sage: h = L.Dp_valued_height(7)
            sage: h(E.gens()[0])
            (3*5 + 5^2 + 2*5^3 + 3*5^4 + 4*5^5 + 5^6 + 5^7 + O(5^8), 5^2 + 4*5^4 + 2*5^7 + 3*5^8 + O(5^9))
        """
    def Dp_valued_regulator(self, prec: int = 20, v1: int = 0, v2: int = 0):
        """
        Return the canonical `p`-adic regulator with values in the Dieudonné module `D_p(E)`
        as defined by Perrin-Riou using the `p`-adic height with values in `D_p(E)`.

        The result is written in the basis `\\omega`, `\\varphi(\\omega)`, and hence the
        coordinates of the result are independent of the chosen Weierstrass equation.

        .. NOTE::

            The definition here is corrected with respect to
            Perrin-Riou's article [PR2003]_. See [SW2013]_.

        EXAMPLES::

            sage: E = EllipticCurve('43a')
            sage: L = E.padic_lseries(7)
            sage: L.Dp_valued_regulator(7)
            (5*7 + 6*7^2 + 4*7^3 + 4*7^4 + 7^5 + 4*7^7 + O(7^8), 4*7^2 + 2*7^3 + 3*7^4 + 7^5 + 6*7^6 + 4*7^7 + O(7^8))
        """
