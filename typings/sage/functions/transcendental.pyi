from _typeshed import Incomplete
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc import increase_recursion_limit as increase_recursion_limit
from sage.rings.integer_ring import ZZ as ZZ
from sage.symbolic.function import BuiltinFunction as BuiltinFunction, GinacFunction as GinacFunction

class Function_zeta(GinacFunction):
    def __init__(self) -> None:
        """
        Riemann zeta function at s with s a real or complex number.

        INPUT:

        - ``s`` -- real or complex number

        If s is a real number, the computation is done using the MPFR
        library. When the input is not real, the computation is done using
        the PARI C library.

        EXAMPLES::

            sage: RR = RealField(200)                                                   # needs sage.rings.real_mpfr
            sage: zeta(RR(2))                                                           # needs sage.rings.real_mpfr
            1.6449340668482264364724151666460251892189499012067984377356

            sage: # needs sage.symbolic
            sage: zeta(x)
            zeta(x)
            sage: zeta(2)
            1/6*pi^2
            sage: zeta(2.)
            1.64493406684823
            sage: zeta(I)
            zeta(I)
            sage: zeta(I).n()
            0.00330022368532410 - 0.418155449141322*I
            sage: zeta(sqrt(2))
            zeta(sqrt(2))
            sage: zeta(sqrt(2)).n()  # rel tol 1e-10
            3.02073767948603

        It is possible to use the ``hold`` argument to prevent
        automatic evaluation::

            sage: zeta(2, hold=True)                                                    # needs sage.symbolic
            zeta(2)

        To then evaluate again, we currently must use Maxima via
        :meth:`sage.symbolic.expression.Expression.simplify`::

            sage: a = zeta(2, hold=True); a.simplify()                                  # needs sage.symbolic
            1/6*pi^2

        The Laurent expansion of `\\zeta(s)` at `s=1` is
        implemented by means of the
        :wikipedia:`Stieltjes constants <Stieltjes_constants>`::

            sage: s = SR('s')                                                           # needs sage.symbolic
            sage: zeta(s).series(s==1, 2)                                               # needs sage.symbolic
            1*(s - 1)^(-1) + euler_gamma + (-stieltjes(1))*(s - 1) + Order((s - 1)^2)

        Generally, the Stieltjes constants occur in the Laurent
        expansion of `\\zeta`-type singularities::

            sage: zeta(2*s/(s+1)).series(s==1, 2)                                       # needs sage.symbolic
            2*(s - 1)^(-1) + (euler_gamma + 1) + (-1/2*stieltjes(1))*(s - 1) + Order((s - 1)^2)


        TESTS::

            sage: # needs sage.symbolic
            sage: latex(zeta(x))
            \\zeta(x)
            sage: a = loads(dumps(zeta(x)))
            sage: a.operator() == zeta
            True
            sage: zeta(x)._sympy_()                                                     # needs sympy
            zeta(x)

            sage: zeta(1)                                                               # needs sage.symbolic
            Infinity
            sage: zeta(x).subs(x=1)                                                     # needs sage.symbolic
            Infinity

        Check that :issue:`19799` is resolved::

            sage: zeta(pi)                                                              # needs sage.symbolic
            zeta(pi)
            sage: zeta(pi).n()  # rel tol 1e-10                                         # needs sage.symbolic
            1.17624173838258

        Check that :issue:`20082` is fixed::

            sage: zeta(x).series(x==pi, 2)                                              # needs sage.symbolic
            (zeta(pi)) + (zetaderiv(1, pi))*(-pi + x) + Order((pi - x)^2)
            sage: (zeta(x) * 1/(1 - exp(-x))).residue(x==2*pi*I)                        # needs sage.symbolic
            zeta(2*I*pi)

        Check that :issue:`20102` is fixed::

            sage: (zeta(x)^2).series(x==1, 1)                                           # needs sage.symbolic
            1*(x - 1)^(-2) + (2*euler_gamma)*(x - 1)^(-1)
            + (euler_gamma^2 - 2*stieltjes(1)) + Order(x - 1)
            sage: (zeta(x)^4).residue(x==1)                                             # needs sage.symbolic
            4/3*euler_gamma*(3*euler_gamma^2 - 2*stieltjes(1))
            - 28/3*euler_gamma*stieltjes(1) + 2*stieltjes(2)

        Check that the right infinities are returned (:issue:`19439`)::

            sage: zeta(1.0)                                                             # needs sage.symbolic
            +infinity
            sage: zeta(SR(1.0))                                                         # needs sage.symbolic
            Infinity

        Fixed conversion::

            sage: zeta(3)._maple_init_()                                                # needs sage.symbolic
            'Zeta(3)'
            sage: zeta(3)._maple_().sage()      # optional - maple                      # needs sage.symbolic
            zeta(3)
        """

zeta: Function_zeta
r"""Riemann zeta function at s with s a real or complex number.

INPUT:

- ``s`` -- real or complex number

If s is a real number, the computation is done using the MPFR
library. When the input is not real, the computation is done using
the PARI C library.

EXAMPLES::

    sage: RR = RealField(200)                                                   # needs sage.rings.real_mpfr
    sage: zeta(RR(2))                                                           # needs sage.rings.real_mpfr
    1.6449340668482264364724151666460251892189499012067984377356

    sage: # needs sage.symbolic
    sage: zeta(x)
    zeta(x)
    sage: zeta(2)
    1/6*pi^2
    sage: zeta(2.)
    1.64493406684823
    sage: zeta(I)
    zeta(I)
    sage: zeta(I).n()
    0.00330022368532410 - 0.418155449141322*I
    sage: zeta(sqrt(2))
    zeta(sqrt(2))
    sage: zeta(sqrt(2)).n()  # rel tol 1e-10
    3.02073767948603

It is possible to use the ``hold`` argument to prevent
automatic evaluation::

    sage: zeta(2, hold=True)                                                    # needs sage.symbolic
    zeta(2)

To then evaluate again, we currently must use Maxima via
:meth:`sage.symbolic.expression.Expression.simplify`::

    sage: a = zeta(2, hold=True); a.simplify()                                  # needs sage.symbolic
    1/6*pi^2

The Laurent expansion of `\zeta(s)` at `s=1` is
implemented by means of the
:wikipedia:`Stieltjes constants <Stieltjes_constants>`::

    sage: s = SR('s')                                                           # needs sage.symbolic
    sage: zeta(s).series(s==1, 2)                                               # needs sage.symbolic
    1*(s - 1)^(-1) + euler_gamma + (-stieltjes(1))*(s - 1) + Order((s - 1)^2)

Generally, the Stieltjes constants occur in the Laurent
expansion of `\zeta`-type singularities::

    sage: zeta(2*s/(s+1)).series(s==1, 2)                                       # needs sage.symbolic
    2*(s - 1)^(-1) + (euler_gamma + 1) + (-1/2*stieltjes(1))*(s - 1) + Order((s - 1)^2)


TESTS::

    sage: # needs sage.symbolic
    sage: latex(zeta(x))
    \zeta(x)
    sage: a = loads(dumps(zeta(x)))
    sage: a.operator() == zeta
    True
    sage: zeta(x)._sympy_()                                                     # needs sympy
    zeta(x)

    sage: zeta(1)                                                               # needs sage.symbolic
    Infinity
    sage: zeta(x).subs(x=1)                                                     # needs sage.symbolic
    Infinity

Check that :issue:`19799` is resolved::

    sage: zeta(pi)                                                              # needs sage.symbolic
    zeta(pi)
    sage: zeta(pi).n()  # rel tol 1e-10                                         # needs sage.symbolic
    1.17624173838258

Check that :issue:`20082` is fixed::

    sage: zeta(x).series(x==pi, 2)                                              # needs sage.symbolic
    (zeta(pi)) + (zetaderiv(1, pi))*(-pi + x) + Order((pi - x)^2)
    sage: (zeta(x) * 1/(1 - exp(-x))).residue(x==2*pi*I)                        # needs sage.symbolic
    zeta(2*I*pi)

Check that :issue:`20102` is fixed::

    sage: (zeta(x)^2).series(x==1, 1)                                           # needs sage.symbolic
    1*(x - 1)^(-2) + (2*euler_gamma)*(x - 1)^(-1)
    + (euler_gamma^2 - 2*stieltjes(1)) + Order(x - 1)
    sage: (zeta(x)^4).residue(x==1)                                             # needs sage.symbolic
    4/3*euler_gamma*(3*euler_gamma^2 - 2*stieltjes(1))
    - 28/3*euler_gamma*stieltjes(1) + 2*stieltjes(2)

Check that the right infinities are returned (:issue:`19439`)::

    sage: zeta(1.0)                                                             # needs sage.symbolic
    +infinity
    sage: zeta(SR(1.0))                                                         # needs sage.symbolic
    Infinity

Fixed conversion::

    sage: zeta(3)._maple_init_()                                                # needs sage.symbolic
    'Zeta(3)'
    sage: zeta(3)._maple_().sage()      # optional - maple                      # needs sage.symbolic
    zeta(3)

"""

ζ = zeta
r"""Riemann zeta function at s with s a real or complex number.

INPUT:

- ``s`` -- real or complex number

If s is a real number, the computation is done using the MPFR
library. When the input is not real, the computation is done using
the PARI C library.

EXAMPLES::

    sage: RR = RealField(200)                                                   # needs sage.rings.real_mpfr
    sage: zeta(RR(2))                                                           # needs sage.rings.real_mpfr
    1.6449340668482264364724151666460251892189499012067984377356

    sage: # needs sage.symbolic
    sage: zeta(x)
    zeta(x)
    sage: zeta(2)
    1/6*pi^2
    sage: zeta(2.)
    1.64493406684823
    sage: zeta(I)
    zeta(I)
    sage: zeta(I).n()
    0.00330022368532410 - 0.418155449141322*I
    sage: zeta(sqrt(2))
    zeta(sqrt(2))
    sage: zeta(sqrt(2)).n()  # rel tol 1e-10
    3.02073767948603

It is possible to use the ``hold`` argument to prevent
automatic evaluation::

    sage: zeta(2, hold=True)                                                    # needs sage.symbolic
    zeta(2)

To then evaluate again, we currently must use Maxima via
:meth:`sage.symbolic.expression.Expression.simplify`::

    sage: a = zeta(2, hold=True); a.simplify()                                  # needs sage.symbolic
    1/6*pi^2

The Laurent expansion of `\zeta(s)` at `s=1` is
implemented by means of the
:wikipedia:`Stieltjes constants <Stieltjes_constants>`::

    sage: s = SR('s')                                                           # needs sage.symbolic
    sage: zeta(s).series(s==1, 2)                                               # needs sage.symbolic
    1*(s - 1)^(-1) + euler_gamma + (-stieltjes(1))*(s - 1) + Order((s - 1)^2)

Generally, the Stieltjes constants occur in the Laurent
expansion of `\zeta`-type singularities::

    sage: zeta(2*s/(s+1)).series(s==1, 2)                                       # needs sage.symbolic
    2*(s - 1)^(-1) + (euler_gamma + 1) + (-1/2*stieltjes(1))*(s - 1) + Order((s - 1)^2)


TESTS::

    sage: # needs sage.symbolic
    sage: latex(zeta(x))
    \zeta(x)
    sage: a = loads(dumps(zeta(x)))
    sage: a.operator() == zeta
    True
    sage: zeta(x)._sympy_()                                                     # needs sympy
    zeta(x)

    sage: zeta(1)                                                               # needs sage.symbolic
    Infinity
    sage: zeta(x).subs(x=1)                                                     # needs sage.symbolic
    Infinity

Check that :issue:`19799` is resolved::

    sage: zeta(pi)                                                              # needs sage.symbolic
    zeta(pi)
    sage: zeta(pi).n()  # rel tol 1e-10                                         # needs sage.symbolic
    1.17624173838258

Check that :issue:`20082` is fixed::

    sage: zeta(x).series(x==pi, 2)                                              # needs sage.symbolic
    (zeta(pi)) + (zetaderiv(1, pi))*(-pi + x) + Order((pi - x)^2)
    sage: (zeta(x) * 1/(1 - exp(-x))).residue(x==2*pi*I)                        # needs sage.symbolic
    zeta(2*I*pi)

Check that :issue:`20102` is fixed::

    sage: (zeta(x)^2).series(x==1, 1)                                           # needs sage.symbolic
    1*(x - 1)^(-2) + (2*euler_gamma)*(x - 1)^(-1)
    + (euler_gamma^2 - 2*stieltjes(1)) + Order(x - 1)
    sage: (zeta(x)^4).residue(x==1)                                             # needs sage.symbolic
    4/3*euler_gamma*(3*euler_gamma^2 - 2*stieltjes(1))
    - 28/3*euler_gamma*stieltjes(1) + 2*stieltjes(2)

Check that the right infinities are returned (:issue:`19439`)::

    sage: zeta(1.0)                                                             # needs sage.symbolic
    +infinity
    sage: zeta(SR(1.0))                                                         # needs sage.symbolic
    Infinity

Fixed conversion::

    sage: zeta(3)._maple_init_()                                                # needs sage.symbolic
    'Zeta(3)'
    sage: zeta(3)._maple_().sage()      # optional - maple                      # needs sage.symbolic
    zeta(3)

"""

class Function_stieltjes(GinacFunction):
    def __init__(self) -> None:
        """
        Stieltjes constant of index ``n``.

        ``stieltjes(0)`` is identical to the Euler-Mascheroni constant
        (:class:`sage.symbolic.constants.EulerGamma`). The Stieltjes
        constants are used in the series expansions of `\\zeta(s)`.

        INPUT:

        - ``n`` -- nonnegative integer

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: _ = var('n')
            sage: stieltjes(n)
            stieltjes(n)
            sage: stieltjes(0)
            euler_gamma
            sage: stieltjes(2)
            stieltjes(2)
            sage: stieltjes(int(2))
            stieltjes(2)
            sage: stieltjes(2).n(100)
            -0.0096903631928723184845303860352
            sage: RR = RealField(200)                                                   # needs sage.rings.real_mpfr
            sage: stieltjes(RR(2))                                                      # needs sage.rings.real_mpfr
            -0.0096903631928723184845303860352125293590658061013407498807014

        It is possible to use the ``hold`` argument to prevent
        automatic evaluation::

            sage: stieltjes(0, hold=True)                                               # needs sage.symbolic
            stieltjes(0)

            sage: # needs sage.symbolic
            sage: latex(stieltjes(n))
            \\gamma_{n}
            sage: a = loads(dumps(stieltjes(n)))
            sage: a.operator() == stieltjes
            True
            sage: stieltjes(x)._sympy_()                                                # needs sympy
            stieltjes(x)

            sage: stieltjes(x).subs(x==0)                                               # needs sage.symbolic
            euler_gamma
        """

stieltjes: Function_stieltjes

class Function_HurwitzZeta(BuiltinFunction):
    def __init__(self) -> None:
        """
        TESTS::

            sage: latex(hurwitz_zeta(x, 2))                                             # needs sage.symbolic
            \\zeta\\left(x, 2\\right)
            sage: hurwitz_zeta(x, 2)._sympy_()                                          # needs sympy sage.symbolic
            zeta(x, 2)
        """

hurwitz_zeta_func: Function_HurwitzZeta

def hurwitz_zeta(s, x, **kwargs):
    """
    The Hurwitz zeta function `\\zeta(s, x)`, where `s` and `x` are complex.

    The Hurwitz zeta function is one of the many zeta functions. It
    is defined as

    .. MATH::

             \\zeta(s, x) = \\sum_{k=0}^{\\infty} (k + x)^{-s}.


    When `x = 1`, this coincides with Riemann's zeta function.
    The Dirichlet `L`-functions may be expressed as linear combinations
    of Hurwitz zeta functions.

    EXAMPLES:

    Symbolic evaluations::

        sage: # needs sage.symbolic
        sage: hurwitz_zeta(x, 1)
        zeta(x)
        sage: hurwitz_zeta(4, 3)
        1/90*pi^4 - 17/16
        sage: hurwitz_zeta(-4, x)
        -1/5*x^5 + 1/2*x^4 - 1/3*x^3 + 1/30*x
        sage: hurwitz_zeta(7, -1/2)
        127*zeta(7) - 128
        sage: hurwitz_zeta(-3, 1)
        1/120

    Numerical evaluations::

        sage: hurwitz_zeta(3, 1/2).n()                                                  # needs mpmath
        8.41439832211716
        sage: hurwitz_zeta(11/10, 1/2).n()                                              # needs sage.symbolic
        12.1038134956837
        sage: hurwitz_zeta(3, x).series(x, 60).subs(x=0.5).n()                          # needs sage.symbolic
        8.41439832211716
        sage: hurwitz_zeta(3, 0.5)                                                      # needs mpmath
        8.41439832211716

    REFERENCES:

    - :wikipedia:`Hurwitz_zeta_function`
    """

class Function_zetaderiv(GinacFunction):
    def __init__(self) -> None:
        """
        Derivatives of the Riemann zeta function.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: zetaderiv(1, x)
            zetaderiv(1, x)
            sage: zetaderiv(1, x).diff(x)
            zetaderiv(2, x)
            sage: var('n')
            n
            sage: zetaderiv(n, x)
            zetaderiv(n, x)
            sage: zetaderiv(1, 4).n()
            -0.0689112658961254
            sage: import mpmath; mpmath.diff(lambda x: mpmath.zeta(x), 4)               # needs mpmath
            mpf('-0.068911265896125382')

        TESTS::

            sage: latex(zetaderiv(2, x))                                                # needs sage.symbolic
            \\zeta^\\prime\\left(2, x\\right)
            sage: a = loads(dumps(zetaderiv(2, x)))                                     # needs sage.symbolic
            sage: a.operator() == zetaderiv                                             # needs sage.symbolic
            True

            sage: b = RBF(3/2, 1e-10)                                                   # needs sage.libs.flint
            sage: zetaderiv(1, b, hold=True)                                            # needs sage.libs.flint sage.symbolic
            zetaderiv(1, [1.500000000 +/- 1.01e-10])
            sage: zetaderiv(b, 1)                                                       # needs sage.libs.flint sage.symbolic
            zetaderiv([1.500000000 +/- 1.01e-10], 1)
        """

zetaderiv: Function_zetaderiv

def zeta_symmetric(s):
    """
    Completed function `\\xi(s)` that satisfies
    `\\xi(s) = \\xi(1-s)` and has zeros at the same points as the
    Riemann zeta function.

    INPUT:

    - ``s`` -- real or complex number

    If s is a real number the computation is done using the MPFR
    library. When the input is not real, the computation is done using
    the PARI C library.

    More precisely,

    .. MATH::

                xi(s) = \\gamma(s/2 + 1) * (s-1) * \\pi^{-s/2} * \\zeta(s).

    EXAMPLES::

        sage: # needs sage.rings.real_mpfr
        sage: RR = RealField(200)
        sage: zeta_symmetric(RR(0.7))
        0.49758041465112690357779107525638385212657443284080589766062

        sage: # needs sage.libs.pari sage.rings.real_mpfr
        sage: zeta_symmetric(0.7)
        0.497580414651127
        sage: zeta_symmetric(1 - 0.7)
        0.497580414651127
        sage: C.<i> = ComplexField()
        sage: zeta_symmetric(0.5 + i*14.0)
        0.000201294444235258 + 1.49077798716757e-19*I
        sage: zeta_symmetric(0.5 + i*14.1)
        0.0000489893483255687 + 4.40457132572236e-20*I
        sage: zeta_symmetric(0.5 + i*14.2)
        -0.0000868931282620101 + 7.11507675693612e-20*I

    REFERENCE:

    - I copied the definition of xi from
      http://web.viu.ca/pughg/RiemannZeta/RiemannZetaLong.html
    """

class DickmanRho(BuiltinFunction):
    '''
    Dickman\'s function is the continuous function satisfying the
    differential equation

    .. MATH::

         x \\rho\'(x) + \\rho(x-1) = 0

    with initial conditions `\\rho(x)=1` for
    `0 \\le x \\le 1`. It is useful in estimating the frequency
    of smooth numbers as asymptotically

    .. MATH::

         \\Psi(a, a^{1/s}) \\sim a \\rho(s)

    where `\\Psi(a,b)` is the number of `b`-smooth
    numbers less than `a`.

    ALGORITHM:

    Dickmans\'s function is analytic on the interval
    `[n,n+1]` for each integer `n`. To evaluate at
    `n+t, 0 \\le t < 1`, a power series is recursively computed
    about `n+1/2` using the differential equation stated above.
    As high precision arithmetic may be needed for intermediate results
    the computed series are cached for later use.

    Simple explicit formulas are used for the intervals [0,1] and
    [1,2].

    EXAMPLES::

        sage: # needs sage.symbolic
        sage: dickman_rho(2)
        0.306852819440055
        sage: dickman_rho(10)
        2.77017183772596e-11
        sage: dickman_rho(10.00000000000000000000000000000000000000)
        2.77017183772595898875812120063434232634e-11
        sage: plot(log(dickman_rho(x)), (x, 0, 15))                                     # needs sage.plot
        Graphics object consisting of 1 graphics primitive

    AUTHORS:

    - Robert Bradshaw (2008-09)

    REFERENCES:

    - G. Marsaglia, A. Zaman, J. Marsaglia. "Numerical
      Solutions to some Classical Differential-Difference Equations."
      Mathematics of Computation, Vol. 53, No. 187 (1989).
    '''
    def __init__(self) -> None:
        """
        Construct an object to represent Dickman's rho function.

        TESTS::

            sage: dickman_rho(x)                                                        # needs sage.symbolic
            dickman_rho(x)
            sage: dickman_rho(3)                                                        # needs sage.symbolic
            0.0486083882911316
            sage: dickman_rho(pi)                                                       # needs sage.symbolic
            0.0359690758968463
        """
    def power_series(self, n, abs_prec):
        """
        This function returns the power series about `n+1/2` used
        to evaluate Dickman's function. It is scaled such that the interval
        `[n,n+1]` corresponds to `x` in `[-1,1]`.

        INPUT:

        - ``n`` -- the lower endpoint of the interval for which
          this power series holds

        - ``abs_prec`` -- the absolute precision of the
          resulting power series

        EXAMPLES::

            sage: # needs sage.rings.real_mpfr
            sage: f = dickman_rho.power_series(2, 20); f
            -9.9376e-8*x^11 + 3.7722e-7*x^10 - 1.4684e-6*x^9 + 5.8783e-6*x^8
             - 0.000024259*x^7 + 0.00010341*x^6 - 0.00045583*x^5 + 0.0020773*x^4
             - 0.0097336*x^3 + 0.045224*x^2 - 0.11891*x + 0.13032
            sage: f(-1), f(0), f(1)
            (0.30685, 0.13032, 0.048608)
            sage: dickman_rho(2), dickman_rho(2.5), dickman_rho(3)
            (0.306852819440055, 0.130319561832251, 0.0486083882911316)
        """
    def approximate(self, x, parent=None):
        '''
        Approximate using de Bruijn\'s formula.

        .. MATH::

             \\rho(x) \\sim \\frac{exp(-x \\xi + Ei(\\xi))}{\\sqrt{2\\pi x}\\xi}

        which is asymptotically equal to Dickman\'s function, and is much
        faster to compute.

        REFERENCES:

        - N. De Bruijn, "The Asymptotic behavior of a function
          occurring in the theory of primes." J. Indian Math Soc. v 15.
          (1951)

        EXAMPLES::

            sage: dickman_rho.approximate(10)                                           # needs sage.rings.real_mpfr
            2.41739196365564e-11
            sage: dickman_rho(10)                                                       # needs sage.symbolic
            2.77017183772596e-11
            sage: dickman_rho.approximate(1000)                                         # needs sage.rings.real_mpfr
            4.32938809066403e-3464
        '''

dickman_rho: DickmanRho
