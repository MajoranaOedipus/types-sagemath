r"""
Class for computing sums over zeros of motivic `L`-functions

All computations are done to double precision.

AUTHORS:

- Simon Spicer (2014-10): first version
"""

from collections.abc import Iterable
from typing import Literal, overload
from typings_sagemath import Complex, Int, Real
from sage.schemes.elliptic_curves.ell_rational_field import EllipticCurve_rational_field
from sage.rings.real_double import RealDoubleElement
from sage.schemes.elliptic_curves.lseries_ell import Lseries_ell
from sage.rings.complex_double import ComplexDoubleElement
from sage.rings.infinity import PlusInfinity
from sage.structure.sage_object import SageObject
from sage.rings.integer import Integer

class LFunctionZeroSum_abstract(SageObject):
    r"""
    Abstract class for computing certain sums over zeros of a motivic `L`-function
    without having to determine the zeros themselves.
    """
    
    @overload
    def ncpus(self, n: int) -> None: ...
    @overload
    def ncpus(self) -> int:
        r"""
        Set or return the number of CPUs to be used in parallel computations.

        If called with no input, the number of CPUs currently set is returned;
        else this value is set to `n`. If `n` is 0 then the number of CPUs is set
        to the max available.

        INPUT:

        - ``n`` -- (default: ``None``) if not ``None``, a nonnegative integer

        OUTPUT: if `n` is not ``None``, returns a positive integer

        EXAMPLES::

            sage: Z = LFunctionZeroSum(EllipticCurve("389a"))
            sage: Z.ncpus()
            1
            sage: Z.ncpus(2)
            sage: Z.ncpus()
            2

        The following output will depend on the system that Sage is running on.

        ::

            sage: Z.ncpus(0)
            sage: Z.ncpus()            # random
            4
        """
        ...
    def level(self) -> Integer:
        r"""
        Return the level of the form attached to ``self``.

        If ``self`` was constructed from an elliptic curve,
        then this is equal to the conductor of `E`.

        EXAMPLES::

            sage: E = EllipticCurve("389a")
            sage: Z = LFunctionZeroSum(E)
            sage: Z.level()
            389
        """
        ...
    def weight(self) -> Integer:
        r"""
        Return the weight of the form attached to ``self``.

        If ``self`` was constructed
        from an elliptic curve, then this is 2.

        EXAMPLES::

            sage: E = EllipticCurve("389a")
            sage: Z = LFunctionZeroSum(E)
            sage: Z.weight()
            2
        """
        ...
    def C0(self, include_euler_gamma: bool = True) -> RealDoubleElement:
        r"""
        Return the constant term of the logarithmic derivative of the
        completed `L`-function attached to ``self``.

        This is equal to
        `-\eta + \log(N)/2 - \log(2\pi)`, where `\eta` is the
        Euler-Mascheroni constant `= 0.5772...`
        and `N` is the level of the form attached to ``self``.

        INPUT:

        - ``include_euler_gamma`` -- boolean (default: ``True``); if set to
          ``False``, return the constant `\log(N)/2 - \log(2\pi)`, i.e., do
          not subtract the Euler-Mascheroni constant

        EXAMPLES::

            sage: E = EllipticCurve("389a")
            sage: Z = LFunctionZeroSum(E)
            sage: Z.C0() # tol 1.0e-13
            0.5666969404983447
            sage: Z.C0(include_euler_gamma=False) # tol 1.0e-13
            1.1439126053998776
        """
        ...
    @overload
    def cnlist(self, n: Int, python_floats: Literal[True] = True) -> list[float]: ... # pyright: ignore[reportOverlappingOverload]
    @overload
    def cnlist(self, n: Int, python_floats: Literal[False] = False) -> list[RealDoubleElement]:
        r"""
        Return a list of Dirichlet coefficient of the logarithmic
        derivative of the `L`-function attached to ``self``, shifted so that
        the critical line lies on the imaginary axis, up to and
        including `n`.

        The `i`-th element of the returned list is ``a[i]``.

        INPUT:

        - ``n`` -- nonnegative integer

        - ``python_floats`` -- boolean (default: ``False``); if ``True`` return
          a list of Python floats instead of Sage Real Double Field elements

        OUTPUT: list of real numbers

        .. SEEALSO::

            :meth:`~sage.lfunctions.zero_sums.LFunctionZeroSum_EllipticCurve.cn`

        .. TODO::

            Speed this up; make more efficient

        EXAMPLES::

            sage: E = EllipticCurve("11a")
            sage: Z = LFunctionZeroSum(E)
            sage: cnlist = Z.cnlist(11)
            sage: for n in range(12): print((n, cnlist[n])) # tol 1.0e-13
            (0, 0.0)
            (1, 0.0)
            (2, 0.6931471805599453)
            (3, 0.3662040962227033)
            (4, 0.0)
            (5, -0.32188758248682003)
            (6, 0.0)
            (7, 0.555974328301518)
            (8, -0.34657359027997264)
            (9, 0.6103401603711721)
            (10, 0.0)
            (11, -0.21799047934530644)
        """
        ...
    @overload
    def digamma(self, s: Real, include_constant_term=True) -> RealDoubleElement | PlusInfinity: ... # TODO: Zmod is actually not allowed
    @overload
    def digamma(self, s: Complex, include_constant_term=True) -> ComplexDoubleElement |  RealDoubleElement:
        r"""
        Return the digamma function `\digamma(s)` on the complex input s.

        This is given by
        `\digamma(s) = -\eta + \sum_{k=1}^{\infty} \frac{s-1}{k(k+s-1)}`,
        where `\eta` is the Euler-Mascheroni constant `=0.5772156649\ldots`.

        This function is needed in the computing the logarithmic derivative
        of the `L`-function attached to ``self``.

        INPUT:

        - ``s`` -- complex number

        - ``include_constant_term`` -- boolean (default: ``True``); if set
          to ``False``, only the value of the sum over `k` is returned without
          subtracting the Euler-Mascheroni constant, i.e., the returned value
          is equal to `\sum_{k=1}^{\infty} \frac{s-1}{k(k+s-1)}`

        OUTPUT:

        A real double precision number if the input is real and not a negative
        integer; Infinity if the input is a negative integer, and a complex
        number otherwise.

        EXAMPLES::

            sage: Z = LFunctionZeroSum(EllipticCurve("37a"))
            sage: Z.digamma(3.2) # tol 1.0e-13
            0.9988388912865993
            sage: Z.digamma(3.2,include_constant_term=False) # tol 1.0e-13
            1.576054556188132
            sage: Z.digamma(1+I) # tol 1.0e-13
            0.09465032062247625 + 1.076674047468581*I
            sage: Z.digamma(-2)
            +Infinity

        Evaluating the sum without the constant term at the positive integers n
        returns the (n-1)th harmonic number.

        ::

            sage: Z.digamma(3,include_constant_term=False)
            1.5
            sage: Z.digamma(6,include_constant_term=False)
            2.283333333333333
        """
        ...
    
    @overload
    def logarithmic_derivative(self, s: Real, num_terms: Int = 10000, as_interval: bool=False) -> tuple[RealDoubleElement, RealDoubleElement | PlusInfinity]: ...
    @overload
    def logarithmic_derivative(self, s: Complex, num_terms: Int = 10000, as_interval: bool=False) -> tuple[RealDoubleElement| ComplexDoubleElement, RealDoubleElement | PlusInfinity]:
        r"""
        Compute the value of the logarithmic derivative
        `\frac{L^{\prime}}{L}` at the point s to *low* precision, where `L`
        is the `L`-function attached to ``self``.

        .. WARNING::

            The value is computed naively by evaluating the Dirichlet series
            for `\frac{L^{\prime}}{L}`; convergence is controlled by the
            distance of s from the critical strip `0.5<=\Re(s)<=1.5`.
            You may use this method to attempt to compute values inside the
            critical strip; however, results are then *not* guaranteed
            to be correct to any number of digits.

        INPUT:

        - ``s`` -- real or complex value

        - ``num_terms`` -- integer (default: 10000); the maximum number of
          terms summed in the Dirichlet series

        OUTPUT:

        A tuple (z,err), where z is the computed value, and err is an
        upper bound on the truncation error in this value introduced
        by truncating the Dirichlet sum.

        .. NOTE::

            For the default term cap of 10000, a value accurate to all 53
            bits of a double precision floating point number is only
            guaranteed when `|\Re(s-1)|>4.58`, although in practice inputs
            closer to the critical strip will still yield computed values
            close to the true value.

        EXAMPLES::

            sage: E = EllipticCurve([23,100])
            sage: Z = LFunctionZeroSum(E)
            sage: Z.logarithmic_derivative(10) # tol 1.0e-13
            (5.648066742632698e-05, 1.0974102859764345e-34)
            sage: Z.logarithmic_derivative(2.2) # tol 1.0e-13
            (0.5751257063594758, 0.024087912696974387)

        Increasing the number of terms should see the truncation error
        decrease.

        ::

            sage: Z.logarithmic_derivative(2.2,num_terms=50000) # long time # rel tol 1.0e-14
            (0.5751579645060139, 0.008988775519160675)

        Attempting to compute values inside the critical strip
        gives infinite error.

        ::

            sage: Z.logarithmic_derivative(1.3) # tol 1.0e-13
            (5.442994413920786, +Infinity)

        Complex inputs and inputs to the left of the critical strip
        are allowed.

        ::

            sage: Z.logarithmic_derivative(complex(3,-1)) # tol 1.0e-13
            (0.04764548578052381 + 0.16513832809989326*I, 6.584671359095225e-06)
            sage: Z.logarithmic_derivative(complex(-3,-1.1)) # tol 1.0e-13
            (-13.908452173241546 + 2.591443099074753*I, 2.7131584736258447e-14)

        The logarithmic derivative has poles at the negative integers.

        ::

            sage: Z.logarithmic_derivative(-3) # tol 1.0e-13
            (-Infinity, 2.7131584736258447e-14)
        """
        ...
    @overload
    def completed_logarithmic_derivative(self, s: Real, num_terms: Int = 10000) -> tuple[RealDoubleElement, RealDoubleElement | PlusInfinity]: ...
    @overload
    def completed_logarithmic_derivative(self, s: Complex, num_terms: Int = 10000) -> tuple[RealDoubleElement| ComplexDoubleElement, RealDoubleElement | PlusInfinity]:
        r"""
        Compute the value of the completed logarithmic derivative
        `\frac{\Lambda^{\prime}}{\Lambda}` at the point s to *low*
        precision, where `\Lambda = N^{s/2}(2\pi)^s \Gamma(s) L(s)`
        and `L` is the `L`-function attached to ``self``.

        .. WARNING::

            This is computed naively by evaluating the Dirichlet series
            for `\frac{L^{\prime}}{L}`; the convergence thereof is
            controlled by the distance of s from the critical strip
            `0.5<=\Re(s)<=1.5`.
            You may use this method to attempt to compute values inside the
            critical strip; however, results are then *not* guaranteed
            to be correct to any number of digits.

        INPUT:

        - ``s`` -- real or complex value

        - ``num_terms`` -- integer (default: 10000); the maximum number of
          terms summed in the Dirichlet series

        OUTPUT:

        A tuple (z,err), where z is the computed value, and err is an
        upper bound on the truncation error in this value introduced
        by truncating the Dirichlet sum.

        .. NOTE::

            For the default term cap of 10000, a value accurate to all 53
            bits of a double precision floating point number is only
            guaranteed when `|\Re(s-1)|>4.58`, although in practice inputs
            closer to the critical strip will still yield computed values
            close to the true value.

        .. SEEALSO::

            :meth:`~sage.lfunctions.zero_sums.LFunctionZeroSum_EllipticCurve.logarithmic_derivative`

        EXAMPLES::

            sage: E = EllipticCurve([23,100])
            sage: Z = LFunctionZeroSum(E)
            sage: Z.completed_logarithmic_derivative(3) # tol 1.0e-13
            (6.64372066048195, 6.584671359095225e-06)

        Complex values are handled. The function is odd about s=1, so
        the value at 2-s should be minus the value at s.

        ::

            sage: Z.completed_logarithmic_derivative(complex(-2.2,1)) # tol 1.0e-13
            (-6.898080633125154 + 0.22557015394248361*I, 5.623853049808912e-11)
            sage: Z.completed_logarithmic_derivative(complex(4.2,-1)) # tol 1.0e-13
            (6.898080633125154 - 0.22557015394248361*I, 5.623853049808912e-11)
        """
        ...
    def zerosum(
        self, 
        Delta: Real = 1, 
        tau: Real = 0, 
        function: Literal[
            "sincsquared_fast", "sincsquared_parallel", 
            "sincsquared", "gaussian", "cauchy"
        ] = 'sincsquared_fast', 
        ncpus: int | None = None
    ) -> RealDoubleElement:
        r"""
        Bound from above the analytic rank of the form attached to ``self``.

        This bound is obtained by computing `\sum_{\gamma} f(\Delta(\gamma-\tau))`,
        where `\gamma` ranges over the imaginary parts of the zeros of `L_E(s)`
        along the critical strip, and `f(x)` is an appropriate even continuous
        `L_2` function such that `f(0)=1`.

        If `\tau=0`, then as `\Delta` increases this sum converges from above to
        the analytic rank of the `L`-function, as `f(0) = 1` is counted with
        multiplicity `r`, and the other terms all go to 0 uniformly.

        INPUT:

        - ``Delta`` -- positive real number (default: 1) parameter denoting the
          tightness of the zero sum

        - ``tau`` -- real parameter (default: 0) denoting the offset of the sum
          to be computed. When `\tau=0` the sum will converge to the analytic rank
          of the `L`-function as `\Delta` is increased. If `\tau` is the value
          of the imaginary part of a noncentral zero, the limit will be 1
          (assuming the zero is simple); otherwise, the limit will be 0.
          Currently only implemented for the sincsquared and cauchy functions;
          otherwise ignored.

        - ``function`` -- string (default: ``'sincsquared_fast'``); the function
          `f(x)` as described above. Currently implemented options for `f` are

          - ``sincsquared`` -- `f(x) = \left(\frac{\sin(\pi x)}{\pi x}\right)^2`

          - ``gaussian`` -- `f(x) = e^{-x^2}`

          - ``sincsquared_fast`` -- same as "sincsquared", but implementation
            optimized for elliptic curve `L`-functions, and tau must be 0. self
            must be attached to an elliptic curve over `\QQ` given by its global
            minimal model, otherwise the returned result will be incorrect.

          - ``sincsquared_parallel`` -- same as "sincsquared_fast", but optimized
            for parallel computation with large (>2.0) `\Delta` values. ``self`` must
            be attached to an elliptic curve over `\QQ` given by its global minimal
            model, otherwise the returned result will be incorrect.

          - ``cauchy`` -- `f(x) = \frac{1}{1+x^2}`; this is only computable to
            low precision, and only when `\Delta < 2`

        - ``ncpus`` -- (default: ``None``) if not ``None``, a positive integer
          defining the number of CPUs to be used for the computation. If left as
          ``None``, the maximum available number of CPUs will be used.
          Only implemented for algorithm="sincsquared_parallel"; ignored
          otherwise.

        .. WARNING::

            Computation time is exponential in `\Delta`, roughly doubling for
            every increase of 0.1 thereof. Using `\Delta=1` will yield a
            computation time of a few milliseconds; `\Delta=2` takes a few
            seconds, and `\Delta=3` takes upwards of an hour. Increase at your
            own risk beyond this!

        OUTPUT:

        A positive real number that bounds from above the number of zeros with
        imaginary part equal to `\tau`. When `\tau=0` this is an upper bound for
        the `L`-function's analytic rank.

        .. SEEALSO::

            :meth:`~sage.schemes.elliptic_curves.ell_rational_field.EllipticCurve_rational_field.analytic_rank_bound`
            for more documentation and examples on calling this method on elliptic curve
            `L`-functions.

        EXAMPLES::

            sage: E = EllipticCurve("389a"); E.rank()
            2
            sage: Z = LFunctionZeroSum(E)
            sage: E.lseries().zeros(3)
            [0.000000000, 0.000000000, 2.87609907]
            sage: Z.zerosum(Delta=1,function='sincsquared_fast') # tol 1.0e-13
            2.037500084595065
            sage: Z.zerosum(Delta=1,function='sincsquared_parallel') # tol 1.0e-11
            2.037500084595065
            sage: Z.zerosum(Delta=1,function='sincsquared') # tol 1.0e-13
            2.0375000845950644
            sage: Z.zerosum(Delta=1,tau=2.876,function='sincsquared') # tol 1.0e-13
            1.075551295651154
            sage: Z.zerosum(Delta=1,tau=1.2,function='sincsquared') # tol 1.0e-13
            0.10831555377490683
            sage: Z.zerosum(Delta=1,function='gaussian') # tol 1.0e-13
            2.056890425029435
        """
        ...
    
class LFunctionZeroSum_EllipticCurve(LFunctionZeroSum_abstract):
    r"""
    Subclass for computing certain sums over zeros of an elliptic curve `L`-function
    without having to determine the zeros themselves.
    """

    def __init__(self, 
            E: EllipticCurve_rational_field, 
            N: Integer | None = None, 
            ncpus: Int | None = 1
        ):
        r"""
        Initialize ``self``.

        INPUT:

        - ``E`` -- an elliptic curve defined over the rational numbers

        - ``N`` -- (default: ``None``) if not ``None``, a positive integer equal to
          the conductor of E. This is passable so that rank estimation
          can be done for curves whose (large) conductor has been precomputed.

        - ``ncpus`` -- (default: 1) the number of CPUs to use for computations;
          if set to ``None``, the max available amount will be used

        EXAMPLES::

            sage: from sage.lfunctions.zero_sums import LFunctionZeroSum_EllipticCurve
            sage: E = EllipticCurve([1,0,0,3,-4])
            sage: Z = LFunctionZeroSum_EllipticCurve(E); Z
            Zero sum estimator for L-function attached to Elliptic Curve defined by y^2 + x*y = x^3 + 3*x - 4 over Rational Field
            sage: E = EllipticCurve("5077a")
            sage: Z = LFunctionZeroSum_EllipticCurve(E); Z
            Zero sum estimator for L-function attached to Elliptic Curve defined by y^2 + y = x^3 - 7*x + 6 over Rational Field
        """
        ...
    def __repr__(self) -> str:
        r"""
        Representation of ``self``.

        EXAMPLES::

            sage: Z = LFunctionZeroSum(EllipticCurve("37a")); Z
            Zero sum estimator for L-function attached to Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field
        """
        ...
    def elliptic_curve(self) -> EllipticCurve_rational_field:
        r"""
        Return the elliptic curve associated with ``self``.

        EXAMPLES::

            sage: E = EllipticCurve([23,100])
            sage: Z = LFunctionZeroSum(E)
            sage: Z.elliptic_curve()
            Elliptic Curve defined by y^2 = x^3 + 23*x + 100 over Rational Field
        """
        ...
    def lseries(self) -> Lseries_ell:
        r"""
        Return the `L`-series associated with ``self``.

        EXAMPLES::

            sage: E = EllipticCurve([23,100])
            sage: Z = LFunctionZeroSum(E)
            sage: Z.lseries()
            Complex L-series of the Elliptic Curve defined by y^2 = x^3 + 23*x + 100 over Rational Field
        """
        ...
    def cn(self, n: Int) -> RealDoubleElement:
        r"""
        Return the `n`-th Dirichlet coefficient of the logarithmic
        derivative of the `L`-function attached to ``self``, shifted so that
        the critical line lies on the imaginary axis.

        The returned value is
        zero if `n` is not a perfect prime power;
        when `n=p^e` for `p` a prime of bad reduction it is `-a_p^e log(p)/p^e`,
        where `a_p` is `+1, -1` or `0` according to the reduction type of `p`;
        and when `n=p^e` for a prime `p` of good reduction, the value
        is `-(\alpha_p^e + \beta_p^e) \log(p)/p^e`, where `\alpha_p`
        and `\beta_p` are the two complex roots of the characteristic equation
        of Frobenius at `p` on `E`.

        INPUT:

        - ``n`` -- nonnegative integer

        OUTPUT:

        A real number which (by Hasse's Theorem) is at
        most `2\frac{log(n)}{\sqrt{n}}` in magnitude.

        EXAMPLES::

            sage: E = EllipticCurve("11a")
            sage: Z = LFunctionZeroSum(E)
            sage: for n in range(12): print((n, Z.cn(n))) # tol 1.0e-13
            (0, 0.0)
            (1, 0.0)
            (2, 0.6931471805599453)
            (3, 0.3662040962227033)
            (4, 0.0)
            (5, -0.32188758248682003)
            (6, 0.0)
            (7, 0.555974328301518)
            (8, -0.34657359027997264)
            (9, 0.6103401603711721)
            (10, 0.0)
            (11, -0.21799047934530644)
        """
        ...
    def analytic_rank_upper_bound(
        self,
        max_Delta: Real | None = None,
        adaptive: bool = True,
        root_number: Literal["compute", "ignore"] | Int ='compute',
        bad_primes: Iterable[Integer] | None = None,
        ncpus: Int | None = None
    ) -> Integer:
        r"""
        Return an upper bound for the analytic rank of the `L`-function
        `L_E(s)` attached to ``self``, conditional on the Generalized Riemann
        Hypothesis, via computing the zero sum `\sum_{\gamma} f(\Delta\gamma)`,
        where `\gamma` ranges over the imaginary parts of the zeros of `L(E,s)`
        along the critical strip, `f(x) = \left(\frac{\sin(\pi x)}{\pi x}\right)^2`,
        and `\Delta` is the tightness parameter whose maximum value is
        specified by max_Delta.

        This computation can be run on curves with
        very large conductor (so long as the conductor is known or quickly
        computable) when Delta is not too large (see below).

        Uses Bober's rank bounding method as described in [Bob2013]_.

        INPUT:

        - ``max_Delta`` -- (default: ``None``) if not ``None``, a positive real value
          specifying the maximum Delta value used in the zero sum; larger
          values of Delta yield better bounds - but runtime is exponential in
          Delta. If left as ``None``, Delta is set
          to `\min\left\{\frac{1}{\pi}\left(\log(N+1000)/2-\log(2\pi)-\eta\right), 2.5\right\}`,
          where `N` is the conductor of the curve attached to ``self``, and `\eta`
          is the Euler-Mascheroni constant `= 0.5772...`; the crossover
          point is at conductor ~8.3*10^8. For the former value, empirical
          results show that for about 99.7% of all curves the returned value
          is the actual analytic rank.

        - ``adaptive`` -- boolean (default: ``True``)

          - If ``True``, the computation is first run with small and then
            successively larger Delta values up to max_Delta. If at any
            point the computed bound is 0 (or 1 when root_number is -1
            or ``True``), the computation halts and that value is returned;
            otherwise the minimum of the computed bounds is returned.
          - If ``False``, the computation is run a single time with
            Delta=max_Delta, and the resulting bound returned.

        - ``root_number`` -- (default: ``'compute'``) string or integer

          - ``'compute'`` -- the root number of ``self`` is computed and used to
            (possibly) lower the analytic rank estimate by 1
          - ``'ignore'`` -- the above step is omitted
          - ``1`` -- this value is assumed to be the root number of
            ``self``. This is passable so that rank estimation can be done for
            curves whose root number has been precomputed.
          - ``-1`` -- this value is assumed to be the root number of
            ``self``. This is passable so that rank estimation can be done for
            curves whose root number has been precomputed.

        - ``bad_primes`` -- (default: ``None``) if not ``None``, a list of the primes
          of bad reduction for the curve attached to ``self``. This is passable
          so that rank estimation can be done for curves of large conductor
          whose bad primes have been precomputed.

        - ``ncpus`` -- (default: ``None``) if not ``None``, a positive integer
          defining the maximum number of CPUs to be used for the computation.
          If left as ``None``, the maximum available number of CPUs will be used.
          Note: Multiple processors will only be used for Delta values >= 1.75.

        .. NOTE::

            Output will be incorrect if the incorrect root number is specified.

        .. WARNING::

            Zero sum computation time is exponential in the tightness parameter
            `\Delta`, roughly doubling for every increase of 0.1 thereof.
            Using `\Delta=1` (and adaptive=False) will yield a runtime of a few
            milliseconds; `\Delta=2` takes a few seconds, and `\Delta=3` may
            take upwards of an hour. Increase beyond this at your own risk!

        OUTPUT:

        A nonnegative integer greater than or equal to the analytic rank of
        ``self``. If the returned value is 0 or 1 (the latter if parity is not
        ``False``), then this is the true analytic rank of ``self``.

        .. NOTE::

            If you use set_verbose(1), extra information about the computation
            will be printed.

        .. SEEALSO::

            :func:`LFunctionZeroSum`
            :meth:`EllipticCurve.root_number`
            :func:`~sage.misc.verbose.set_verbose`

        EXAMPLES:

        For most elliptic curves with small conductor the central zero(s)
        of `L_E(s)` are fairly isolated, so small values of `\Delta`
        will yield tight rank estimates.

        ::

            sage: E = EllipticCurve("11a")
            sage: E.rank()
            0
            sage: Z = LFunctionZeroSum(E)
            sage: Z.analytic_rank_upper_bound(max_Delta=1,ncpus=1)
            0

            sage: E = EllipticCurve([-39,123])
            sage: E.rank()
            1
            sage: Z = LFunctionZeroSum(E)
            sage: Z.analytic_rank_upper_bound(max_Delta=1)
            1

        This is especially true for elliptic curves with large rank.

        ::

            sage: for r in range(9):
            ....:     E = elliptic_curves.rank(r)[0]
            ....:     print((r, E.analytic_rank_upper_bound(max_Delta=1,
            ....:     adaptive=False,root_number='ignore')))
            (0, 0)
            (1, 1)
            (2, 2)
            (3, 3)
            (4, 4)
            (5, 5)
            (6, 6)
            (7, 7)
            (8, 8)

        However, some curves have `L`-functions with low-lying zeroes, and for these
        larger values of `\Delta` must be used to get tight estimates.

        ::

            sage: E = EllipticCurve("974b1")
            sage: r = E.rank(); r
            0
            sage: Z = LFunctionZeroSum(E)
            sage: Z.analytic_rank_upper_bound(max_Delta=1,root_number='ignore')
            1
            sage: Z.analytic_rank_upper_bound(max_Delta=1.3,root_number='ignore')
            0

        Knowing the root number of E allows us to use smaller Delta values
        to get tight bounds, thus speeding up runtime considerably.

        ::

            sage: Z.analytic_rank_upper_bound(max_Delta=0.6,root_number='compute')
            0

        The are a small number of curves which have pathologically low-lying
        zeroes. For these curves, this method will produce a bound that is
        strictly larger than the analytic rank, unless very large values of
        Delta are used. The following curve ("256944c1" in the Cremona tables)
        is a rank 0 curve with a zero at 0.0256...; the smallest Delta value
        for which the zero sum is strictly less than 2 is ~2.815.

        ::

            sage: E = EllipticCurve([0, -1, 0, -7460362000712, -7842981500851012704])
            sage: N,r = E.conductor(),E.analytic_rank(); N, r
            (256944, 0)
            sage: E.analytic_rank_upper_bound(max_Delta=1,adaptive=False)
            2
            sage: E.analytic_rank_upper_bound(max_Delta=2,adaptive=False)
            2

        This method is can be called on curves with large conductor.

        ::

            sage: E = EllipticCurve([-2934,19238])
            sage: Z = LFunctionZeroSum(E)
            sage: Z.analytic_rank_upper_bound()
            1

        And it can bound rank on curves with *very* large conductor, so long as
        you know beforehand/can easily compute the conductor and primes of bad
        reduction less than `e^{2\pi\Delta}`. The example below is of the rank
        28 curve discovered by Elkies that is the elliptic curve of (currently)
        largest known rank.

        ::

            sage: a4 = -20067762415575526585033208209338542750930230312178956502
            sage: a6 = 34481611795030556467032985690390720374855944359319180361266008296291939448732243429
            sage: E = EllipticCurve([1,-1,1,a4,a6])
            sage: bad_primes = [2,3,5,7,11,13,17,19,48463]
            sage: N = 3455601108357547341532253864901605231198511505793733138900595189472144724781456635380154149870961231592352897621963802238155192936274322687070
            sage: Z = LFunctionZeroSum(E,N)
            sage: Z.analytic_rank_upper_bound(max_Delta=2.37,adaptive=False, # long time
            ....: root_number=1,bad_primes=bad_primes,ncpus=2)
            32
        """
        ...

def LFunctionZeroSum(X: EllipticCurve_rational_field, N=None, ncpus=1) -> LFunctionZeroSum_EllipticCurve:
    r"""
    Constructor for the LFunctionZeroSum class.

    INPUT:

    - ``X`` -- a motivic object; currently only implemented for X = an elliptic curve
      over the rational numbers

    OUTPUT: an LFunctionZeroSum object

    EXAMPLES::

        sage: E = EllipticCurve("389a")
        sage: Z = LFunctionZeroSum(E); Z
        Zero sum estimator for L-function attached to Elliptic Curve defined by y^2 + y = x^3 + x^2 - 2*x over Rational Field

    TESTS::

        sage: E = EllipticCurve([1.2,3.8])
        sage: LFunctionZeroSum(E)
        Traceback (most recent call last):
        ...
        NotImplementedError: currently only implemented for elliptic curves over QQ

        sage: f = Newforms(46)[0]
        sage: LFunctionZeroSum(f)
        Traceback (most recent call last):
        ...
        NotImplementedError: currently only implemented for elliptic curves over QQ
    """
