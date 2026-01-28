from __future__ import annotations
from builtins import range as xrange
import cmath as cmath
import math as math
import mpmath.functions.bessel
import mpmath.functions.elliptic
import mpmath.functions.expintegrals
import mpmath.functions.factorials
import mpmath.functions.hypergeometric
import mpmath.functions.orthogonal
import mpmath.functions.qfunctions
import mpmath.functions.rszeta
import mpmath.functions.signals
import mpmath.functions.theta
import mpmath.functions.zeta
import mpmath.functions.zetazeros
import typing
__all__: list[str] = ['SpecialFunctions', 'acot', 'acoth', 'acsc', 'acsch', 'agm', 'arg', 'asec', 'asech', 'bell', 'cmath', 'conj', 'cot', 'coth', 'csc', 'csch', 'cyclotomic', 'defun', 'defun_static', 'defun_wrapped', 'degrees', 'expm1', 'fabs', 'fmod', 'im', 'lambertw', 'log', 'log10', 'log1p', 'mangoldt', 'math', 'polar', 'polyexp', 'powm1', 'radians', 're', 'rect', 'root', 'sec', 'sech', 'sign', 'sinc', 'sincpi', 'stirling1', 'stirling2', 'unitroots', 'xrange']
class SpecialFunctions:
    """
    
    This class implements special functions using high-level code.
    
    Elementary and some other functions (e.g. gamma function, basecase
    hypergeometric series) are assumed to be predefined by the context as
    "builtins" or "low-level" functions.
    """
    THETA_Q_LIM: typing.ClassVar[float] = 0.9999999
    defined_functions: typing.ClassVar[dict] = {'cot': (cot, True), 'sec': (sec, True), 'csc': (csc, True), 'coth': (coth, True), 'sech': (sech, True), 'csch': (csch, True), 'acot': (acot, True), 'asec': (asec, True), 'acsc': (acsc, True), 'acoth': (acoth, True), 'asech': (asech, True), 'acsch': (acsch, True), 'sign': (sign, False), 'agm': (agm, False), 'sinc': (sinc, True), 'sincpi': (sincpi, True), 'expm1': (expm1, True), 'log1p': (log1p, True), 'powm1': (powm1, True), '_rootof1': (_rootof1, False), 'root': (root, False), 'unitroots': (unitroots, False), 'arg': (arg, False), 'fabs': (fabs, False), 're': (re, False), 'im': (im, False), 'conj': (conj, False), 'polar': (polar, False), 'rect': (rect, True), 'log': (log, False), 'log10': (log10, False), 'fmod': (fmod, False), 'degrees': (degrees, False), 'radians': (radians, False), 'lambertw': (lambertw, False), 'bell': (bell, True), 'polyexp': (polyexp, True), 'cyclotomic': (cyclotomic, True), 'mangoldt': (mangoldt, False), 'stirling1': (stirling1, False), 'stirling2': (stirling2, False), 'gammaprod': (mpmath.functions.factorials.gammaprod, False), 'beta': (mpmath.functions.factorials.beta, False), 'binomial': (mpmath.functions.factorials.binomial, False), 'rf': (mpmath.functions.factorials.rf, False), 'ff': (mpmath.functions.factorials.ff, False), 'fac2': (mpmath.functions.factorials.fac2, True), 'barnesg': (mpmath.functions.factorials.barnesg, True), 'superfac': (mpmath.functions.factorials.superfac, False), 'hyperfac': (mpmath.functions.factorials.hyperfac, True), 'hypercomb': (mpmath.functions.hypergeometric.hypercomb, False), 'hyper': (mpmath.functions.hypergeometric.hyper, False), 'hyp0f1': (mpmath.functions.hypergeometric.hyp0f1, False), 'hyp1f1': (mpmath.functions.hypergeometric.hyp1f1, False), 'hyp1f2': (mpmath.functions.hypergeometric.hyp1f2, False), 'hyp2f1': (mpmath.functions.hypergeometric.hyp2f1, False), 'hyp2f2': (mpmath.functions.hypergeometric.hyp2f2, False), 'hyp2f3': (mpmath.functions.hypergeometric.hyp2f3, False), 'hyp2f0': (mpmath.functions.hypergeometric.hyp2f0, False), 'hyp3f2': (mpmath.functions.hypergeometric.hyp3f2, False), '_hyp1f0': (mpmath.functions.hypergeometric._hyp1f0, True), '_hyp0f1': (mpmath.functions.hypergeometric._hyp0f1, False), '_hyp1f1': (mpmath.functions.hypergeometric._hyp1f1, False), '_hyp2f1': (mpmath.functions.hypergeometric._hyp2f1, False), '_hypq1fq': (mpmath.functions.hypergeometric._hypq1fq, False), '_hyp_borel': (mpmath.functions.hypergeometric._hyp_borel, False), '_hyp2f2': (mpmath.functions.hypergeometric._hyp2f2, False), '_hyp1f2': (mpmath.functions.hypergeometric._hyp1f2, False), '_hyp2f3': (mpmath.functions.hypergeometric._hyp2f3, False), '_hyp2f0': (mpmath.functions.hypergeometric._hyp2f0, False), 'meijerg': (mpmath.functions.hypergeometric.meijerg, False), 'appellf1': (mpmath.functions.hypergeometric.appellf1, True), 'appellf2': (mpmath.functions.hypergeometric.appellf2, False), 'appellf3': (mpmath.functions.hypergeometric.appellf3, False), 'appellf4': (mpmath.functions.hypergeometric.appellf4, False), 'hyper2d': (mpmath.functions.hypergeometric.hyper2d, False), 'bihyper': (mpmath.functions.hypergeometric.bihyper, False), '_erf_complex': (mpmath.functions.expintegrals._erf_complex, True), '_erfc_complex': (mpmath.functions.expintegrals._erfc_complex, True), 'erf': (mpmath.functions.expintegrals.erf, False), 'erfc': (mpmath.functions.expintegrals.erfc, False), 'square_exp_arg': (mpmath.functions.expintegrals.square_exp_arg, False), 'erfi': (mpmath.functions.expintegrals.erfi, True), 'erfinv': (mpmath.functions.expintegrals.erfinv, True), 'npdf': (mpmath.functions.expintegrals.npdf, True), 'ncdf': (mpmath.functions.expintegrals.ncdf, True), 'betainc': (mpmath.functions.expintegrals.betainc, True), 'gammainc': (mpmath.functions.expintegrals.gammainc, False), '_lower_gamma': (mpmath.functions.expintegrals._lower_gamma, False), '_upper_gamma': (mpmath.functions.expintegrals._upper_gamma, False), '_gamma3': (mpmath.functions.expintegrals._gamma3, False), 'expint': (mpmath.functions.expintegrals.expint, True), 'li': (mpmath.functions.expintegrals.li, True), 'ei': (mpmath.functions.expintegrals.ei, False), '_ei_generic': (mpmath.functions.expintegrals._ei_generic, True), 'e1': (mpmath.functions.expintegrals.e1, False), 'ci': (mpmath.functions.expintegrals.ci, False), '_ci_generic': (mpmath.functions.expintegrals._ci_generic, True), 'si': (mpmath.functions.expintegrals.si, False), '_si_generic': (mpmath.functions.expintegrals._si_generic, True), 'chi': (mpmath.functions.expintegrals.chi, True), 'shi': (mpmath.functions.expintegrals.shi, True), 'fresnels': (mpmath.functions.expintegrals.fresnels, True), 'fresnelc': (mpmath.functions.expintegrals.fresnelc, True), 'j0': (mpmath.functions.bessel.j0, False), 'j1': (mpmath.functions.bessel.j1, False), 'besselj': (mpmath.functions.bessel.besselj, False), 'besseli': (mpmath.functions.bessel.besseli, False), 'bessely': (mpmath.functions.bessel.bessely, True), 'besselk': (mpmath.functions.bessel.besselk, True), 'hankel1': (mpmath.functions.bessel.hankel1, True), 'hankel2': (mpmath.functions.bessel.hankel2, True), 'whitm': (mpmath.functions.bessel.whitm, True), 'whitw': (mpmath.functions.bessel.whitw, True), 'hyperu': (mpmath.functions.bessel.hyperu, False), 'struveh': (mpmath.functions.bessel.struveh, False), 'struvel': (mpmath.functions.bessel.struvel, False), 'angerj': (mpmath.functions.bessel.angerj, False), 'webere': (mpmath.functions.bessel.webere, False), 'lommels1': (mpmath.functions.bessel.lommels1, False), 'lommels2': (mpmath.functions.bessel.lommels2, False), 'ber': (mpmath.functions.bessel.ber, False), 'bei': (mpmath.functions.bessel.bei, False), 'ker': (mpmath.functions.bessel.ker, False), 'kei': (mpmath.functions.bessel.kei, False), 'airyai': (mpmath.functions.bessel.airyai, False), 'airybi': (mpmath.functions.bessel.airybi, False), 'airyaizero': (mpmath.functions.bessel.airyaizero, False), 'airybizero': (mpmath.functions.bessel.airybizero, False), 'scorergi': (mpmath.functions.bessel.scorergi, False), 'scorerhi': (mpmath.functions.bessel.scorerhi, False), 'coulombc': (mpmath.functions.bessel.coulombc, True), 'coulombf': (mpmath.functions.bessel.coulombf, True), '_coulomb_chi': (mpmath.functions.bessel._coulomb_chi, True), 'coulombg': (mpmath.functions.bessel.coulombg, True), 'besseljzero': (mpmath.functions.bessel.besseljzero, False), 'besselyzero': (mpmath.functions.bessel.besselyzero, False), 'hermite': (mpmath.functions.orthogonal.hermite, False), 'pcfd': (mpmath.functions.orthogonal.pcfd, False), 'pcfu': (mpmath.functions.orthogonal.pcfu, False), 'pcfv': (mpmath.functions.orthogonal.pcfv, False), 'pcfw': (mpmath.functions.orthogonal.pcfw, False), 'gegenbauer': (mpmath.functions.orthogonal.gegenbauer, True), 'jacobi': (mpmath.functions.orthogonal.jacobi, True), 'laguerre': (mpmath.functions.orthogonal.laguerre, True), 'legendre': (mpmath.functions.orthogonal.legendre, True), 'legenp': (mpmath.functions.orthogonal.legenp, False), 'legenq': (mpmath.functions.orthogonal.legenq, False), 'chebyt': (mpmath.functions.orthogonal.chebyt, True), 'chebyu': (mpmath.functions.orthogonal.chebyu, True), 'spherharm': (mpmath.functions.orthogonal.spherharm, False), '_jacobi_theta2': (mpmath.functions.theta._jacobi_theta2, False), '_djacobi_theta2': (mpmath.functions.theta._djacobi_theta2, False), '_jacobi_theta3': (mpmath.functions.theta._jacobi_theta3, False), '_djacobi_theta3': (mpmath.functions.theta._djacobi_theta3, False), '_jacobi_theta2a': (mpmath.functions.theta._jacobi_theta2a, False), '_jacobi_theta3a': (mpmath.functions.theta._jacobi_theta3a, False), '_djacobi_theta2a': (mpmath.functions.theta._djacobi_theta2a, False), '_djacobi_theta3a': (mpmath.functions.theta._djacobi_theta3a, False), 'jtheta': (mpmath.functions.theta.jtheta, False), '_djtheta': (mpmath.functions.theta._djtheta, False), 'eta': (mpmath.functions.elliptic.eta, True), 'qfrom': (mpmath.functions.elliptic.qfrom, True), 'qbarfrom': (mpmath.functions.elliptic.qbarfrom, True), 'taufrom': (mpmath.functions.elliptic.taufrom, True), 'kfrom': (mpmath.functions.elliptic.kfrom, True), 'mfrom': (mpmath.functions.elliptic.mfrom, True), 'ellipfun': (mpmath.functions.elliptic.ellipfun, False), 'kleinj': (mpmath.functions.elliptic.kleinj, True), 'elliprf': (mpmath.functions.elliptic.elliprf, False), 'elliprc': (mpmath.functions.elliptic.elliprc, False), 'elliprj': (mpmath.functions.elliptic.elliprj, False), 'elliprd': (mpmath.functions.elliptic.elliprd, False), 'elliprg': (mpmath.functions.elliptic.elliprg, False), 'ellipf': (mpmath.functions.elliptic.ellipf, True), 'ellipe': (mpmath.functions.elliptic.ellipe, True), 'ellippi': (mpmath.functions.elliptic.ellippi, True), 'squarew': (mpmath.functions.signals.squarew, True), 'trianglew': (mpmath.functions.signals.trianglew, True), 'sawtoothw': (mpmath.functions.signals.sawtoothw, True), 'unit_triangle': (mpmath.functions.signals.unit_triangle, True), 'sigmoid': (mpmath.functions.signals.sigmoid, True), 'stieltjes': (mpmath.functions.zeta.stieltjes, False), 'siegeltheta': (mpmath.functions.zeta.siegeltheta, True), 'grampoint': (mpmath.functions.zeta.grampoint, True), 'siegelz': (mpmath.functions.zeta.siegelz, True), 'oldzetazero': (mpmath.functions.zeta.oldzetazero, False), 'riemannr': (mpmath.functions.zeta.riemannr, True), 'primepi2': (mpmath.functions.zeta.primepi2, True), 'primezeta': (mpmath.functions.zeta.primezeta, True), 'bernpoly': (mpmath.functions.zeta.bernpoly, True), 'eulerpoly': (mpmath.functions.zeta.eulerpoly, True), 'eulernum': (mpmath.functions.zeta.eulernum, False), 'polylog': (mpmath.functions.zeta.polylog, True), 'clsin': (mpmath.functions.zeta.clsin, True), 'clcos': (mpmath.functions.zeta.clcos, True), 'altzeta': (mpmath.functions.zeta.altzeta, False), '_altzeta_generic': (mpmath.functions.zeta._altzeta_generic, True), 'zeta': (mpmath.functions.zeta.zeta, False), '_hurwitz': (mpmath.functions.zeta._hurwitz, False), '_zetasum': (mpmath.functions.zeta._zetasum, False), 'dirichlet': (mpmath.functions.zeta.dirichlet, False), 'secondzeta': (mpmath.functions.zeta.secondzeta, False), 'lerchphi': (mpmath.functions.zeta.lerchphi, True), 'rs_zeta': (mpmath.functions.rszeta.rs_zeta, False), 'rs_z': (mpmath.functions.rszeta.rs_z, False), 'zetazero': (mpmath.functions.zetazeros.zetazero, False), 'nzeros': (mpmath.functions.zetazeros.nzeros, False), 'backlunds': (mpmath.functions.zetazeros.backlunds, True), 'qp': (mpmath.functions.qfunctions.qp, False), 'qgamma': (mpmath.functions.qfunctions.qgamma, True), 'qfac': (mpmath.functions.qfunctions.qfac, True), 'qhyper': (mpmath.functions.qfunctions.qhyper, False)}
    @staticmethod
    def _altzeta(ctx, s):
        ...
    @staticmethod
    def _besselj(ctx, n, z):
        ...
    @staticmethod
    def _ci(ctx, z):
        ...
    @staticmethod
    def _e1(ctx, z):
        ...
    @staticmethod
    def _ei(ctx, z):
        ...
    @staticmethod
    def _erf(ctx, z):
        ...
    @staticmethod
    def _erfc(ctx, z):
        ...
    @staticmethod
    def _expint_int(ctx, n, z):
        ...
    @staticmethod
    def _gamma_upper_int(ctx, z, a):
        ...
    @staticmethod
    def _si(ctx, z):
        ...
    @staticmethod
    def _zeta(ctx, s):
        ...
    @staticmethod
    def _zetasum_fast(ctx, s, a, n, derivatives, reflect):
        ...
    @staticmethod
    def primepi(ctx, x):
        ...
    @classmethod
    def _wrap_specfun(cls, name, f, wrap):
        ...
    def __init__(self):
        ...
def _lambertw_approx_hybrid(z, k):
    ...
def _lambertw_series(ctx, z, k, tol):
    """
    
    Return rough approximation for W_k(z) from an asymptotic series,
    sufficiently accurate for the Halley iteration to converge to
    the correct value.
    """
def _lambertw_special(ctx, z, k):
    ...
def _polyexp(ctx, n, x, extra = False):
    ...
def _rootof1(ctx, k, n):
    ...
def acot(ctx, z):
    ...
def acoth(ctx, z):
    ...
def acsc(ctx, z):
    ...
def acsch(ctx, z):
    ...
def agm(ctx, a, b = 1):
    """
    
    ``agm(a, b)`` computes the arithmetic-geometric mean of `a` and
    `b`, defined as the limit of the following iteration:
    
    .. math ::
    
        a_0 = a
    
        b_0 = b
    
        a_{n+1} = \\frac{a_n+b_n}{2}
    
        b_{n+1} = \\sqrt{a_n b_n}
    
    This function can be called with a single argument, computing
    `\\mathrm{agm}(a,1) = \\mathrm{agm}(1,a)`.
    
    **Examples**
    
    It is a well-known theorem that the geometric mean of
    two distinct positive numbers is less than the arithmetic
    mean. It follows that the arithmetic-geometric mean lies
    between the two means::
    
        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = True
        >>> a = mpf(3)
        >>> b = mpf(4)
        >>> sqrt(a*b)
        3.46410161513775
        >>> agm(a,b)
        3.48202767635957
        >>> (a+b)/2
        3.5
    
    The arithmetic-geometric mean is scale-invariant::
    
        >>> agm(10*e, 10*pi)
        29.261085515723
        >>> 10*agm(e, pi)
        29.261085515723
    
    As an order-of-magnitude estimate, `\\mathrm{agm}(1,x) \\approx x`
    for large `x`::
    
        >>> agm(10**10)
        643448704.760133
        >>> agm(10**50)
        1.34814309345871e+48
    
    For tiny `x`, `\\mathrm{agm}(1,x) \\approx -\\pi/(2 \\log(x/4))`::
    
        >>> agm('0.01')
        0.262166887202249
        >>> -pi/2/log('0.0025')
        0.262172347753122
    
    The arithmetic-geometric mean can also be computed for complex
    numbers::
    
        >>> agm(3, 2+j)
        (2.51055133276184 + 0.547394054060638j)
    
    The AGM iteration converges very quickly (each step doubles
    the number of correct digits), so :func:`~mpmath.agm` supports efficient
    high-precision evaluation::
    
        >>> mp.dps = 10000
        >>> a = agm(1,2)
        >>> str(a)[-10:]
        '1679581912'
    
    **Mathematical relations**
    
    The arithmetic-geometric mean may be used to evaluate the
    following two parametric definite integrals:
    
    .. math ::
    
      I_1 = \\int_0^{\\infty}
        \\frac{1}{\\sqrt{(x^2+a^2)(x^2+b^2)}} \\,dx
    
      I_2 = \\int_0^{\\pi/2}
        \\frac{1}{\\sqrt{a^2 \\cos^2(x) + b^2 \\sin^2(x)}} \\,dx
    
    We have::
    
        >>> mp.dps = 15
        >>> a = 3
        >>> b = 4
        >>> f1 = lambda x: ((x**2+a**2)*(x**2+b**2))**-0.5
        >>> f2 = lambda x: ((a*cos(x))**2 + (b*sin(x))**2)**-0.5
        >>> quad(f1, [0, inf])
        0.451115405388492
        >>> quad(f2, [0, pi/2])
        0.451115405388492
        >>> pi/(2*agm(a,b))
        0.451115405388492
    
    A formula for `\\Gamma(1/4)`::
    
        >>> gamma(0.25)
        3.62560990822191
        >>> sqrt(2*sqrt(2*pi**3)/agm(1,sqrt(2)))
        3.62560990822191
    
    **Possible issues**
    
    The branch cut chosen for complex `a` and `b` is somewhat
    arbitrary.
    
    """
def arg(ctx, x):
    """
    
    Computes the complex argument (phase) of `x`, defined as the
    signed angle between the positive real axis and `x` in the
    complex plane::
    
        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = True
        >>> arg(3)
        0.0
        >>> arg(3+3j)
        0.785398163397448
        >>> arg(3j)
        1.5707963267949
        >>> arg(-3)
        3.14159265358979
        >>> arg(-3j)
        -1.5707963267949
    
    The angle is defined to satisfy `-\\pi < \\arg(x) \\le \\pi` and
    with the sign convention that a nonnegative imaginary part
    results in a nonnegative argument.
    
    The value returned by :func:`~mpmath.arg` is an ``mpf`` instance.
    """
def asec(ctx, z):
    ...
def asech(ctx, z):
    ...
def bell(ctx, n, x = 1):
    ...
def conj(ctx, x):
    """
    
    Returns the complex conjugate of `x`, `\\overline{x}`. Unlike
    ``x.conjugate()``, :func:`~mpmath.im` converts `x` to a mpmath number::
    
        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = False
        >>> conj(3)
        mpf('3.0')
        >>> conj(-1+4j)
        mpc(real='-1.0', imag='-4.0')
    """
def cot(ctx, z):
    ...
def coth(ctx, z):
    ...
def csc(ctx, z):
    ...
def csch(ctx, z):
    ...
def cyclotomic(ctx, n, z):
    ...
def defun(f):
    ...
def defun_static(f):
    ...
def defun_wrapped(f):
    ...
def degrees(ctx, x):
    """
    
    Converts the radian angle `x` to a degree angle::
    
        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = True
        >>> degrees(pi/3)
        60.0
    """
def expm1(ctx, x):
    ...
def fabs(ctx, x):
    """
    
    Returns the absolute value of `x`, `|x|`. Unlike :func:`abs`,
    :func:`~mpmath.fabs` converts non-mpmath numbers (such as ``int``)
    into mpmath numbers::
    
        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = False
        >>> fabs(3)
        mpf('3.0')
        >>> fabs(-3)
        mpf('3.0')
        >>> fabs(3+4j)
        mpf('5.0')
    """
def fmod(ctx, x, y):
    """
    
    Converts `x` and `y` to mpmath numbers and returns `x \\mod y`.
    For mpmath numbers, this is equivalent to ``x % y``.
    
        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = True
        >>> fmod(100, pi)
        2.61062773871641
    
    You can use :func:`~mpmath.fmod` to compute fractional parts of numbers::
    
        >>> fmod(10.25, 1)
        0.25
    
    """
def im(ctx, x):
    """
    
    Returns the imaginary part of `x`, `\\Im(x)`. :func:`~mpmath.im`
    converts a non-mpmath number to an mpmath number::
    
        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = False
        >>> im(3)
        mpf('0.0')
        >>> im(-1+4j)
        mpf('4.0')
    """
def lambertw(ctx, z, k = 0):
    """
    
    The Lambert W function `W(z)` is defined as the inverse function
    of `w \\exp(w)`. In other words, the value of `W(z)` is such that
    `z = W(z) \\exp(W(z))` for any complex number `z`.
    
    The Lambert W function is a multivalued function with infinitely
    many branches `W_k(z)`, indexed by `k \\in \\mathbb{Z}`. Each branch
    gives a different solution `w` of the equation `z = w \\exp(w)`.
    All branches are supported by :func:`~mpmath.lambertw`:
    
    * ``lambertw(z)`` gives the principal solution (branch 0)
    
    * ``lambertw(z, k)`` gives the solution on branch `k`
    
    The Lambert W function has two partially real branches: the
    principal branch (`k = 0`) is real for real `z > -1/e`, and the
    `k = -1` branch is real for `-1/e < z < 0`. All branches except
    `k = 0` have a logarithmic singularity at `z = 0`.
    
    The definition, implementation and choice of branches
    is based on [Corless]_.
    
    **Plots**
    
    .. literalinclude :: /plots/lambertw.py
    .. image :: /plots/lambertw.png
    .. literalinclude :: /plots/lambertw_c.py
    .. image :: /plots/lambertw_c.png
    
    **Basic examples**
    
    The Lambert W function is the inverse of `w \\exp(w)`::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> w = lambertw(1)
        >>> w
        0.5671432904097838729999687
        >>> w*exp(w)
        1.0
    
    Any branch gives a valid inverse::
    
        >>> w = lambertw(1, k=3)
        >>> w
        (-2.853581755409037807206819 + 17.11353553941214591260783j)
        >>> w = lambertw(1, k=25)
        >>> w
        (-5.047020464221569709378686 + 155.4763860949415867162066j)
        >>> chop(w*exp(w))
        1.0
    
    **Applications to equation-solving**
    
    The Lambert W function may be used to solve various kinds of
    equations, such as finding the value of the infinite power
    tower `z^{z^{z^{\\ldots}}}`::
    
        >>> def tower(z, n):
        ...     if n == 0:
        ...         return z
        ...     return z ** tower(z, n-1)
        ...
        >>> tower(mpf(0.5), 100)
        0.6411857445049859844862005
        >>> -lambertw(-log(0.5))/log(0.5)
        0.6411857445049859844862005
    
    **Properties**
    
    The Lambert W function grows roughly like the natural logarithm
    for large arguments::
    
        >>> lambertw(1000); log(1000)
        5.249602852401596227126056
        6.907755278982137052053974
        >>> lambertw(10**100); log(10**100)
        224.8431064451185015393731
        230.2585092994045684017991
    
    The principal branch of the Lambert W function has a rational
    Taylor series expansion around `z = 0`::
    
        >>> nprint(taylor(lambertw, 0, 6), 10)
        [0.0, 1.0, -1.0, 1.5, -2.666666667, 5.208333333, -10.8]
    
    Some special values and limits are::
    
        >>> lambertw(0)
        0.0
        >>> lambertw(1)
        0.5671432904097838729999687
        >>> lambertw(e)
        1.0
        >>> lambertw(inf)
        +inf
        >>> lambertw(0, k=-1)
        -inf
        >>> lambertw(0, k=3)
        -inf
        >>> lambertw(inf, k=2)
        (+inf + 12.56637061435917295385057j)
        >>> lambertw(inf, k=3)
        (+inf + 18.84955592153875943077586j)
        >>> lambertw(-inf, k=3)
        (+inf + 21.9911485751285526692385j)
    
    The `k = 0` and `k = -1` branches join at `z = -1/e` where
    `W(z) = -1` for both branches. Since `-1/e` can only be represented
    approximately with binary floating-point numbers, evaluating the
    Lambert W function at this point only gives `-1` approximately::
    
        >>> lambertw(-1/e, 0)
        -0.9999999999998371330228251
        >>> lambertw(-1/e, -1)
        -1.000000000000162866977175
    
    If `-1/e` happens to round in the negative direction, there might be
    a small imaginary part::
    
        >>> mp.dps = 15
        >>> lambertw(-1/e)
        (-1.0 + 8.22007971483662e-9j)
        >>> lambertw(-1/e+eps)
        -0.999999966242188
    
    **References**
    
    1. [Corless]_
    """
def log(ctx, x, b = None):
    """
    
    Computes the base-`b` logarithm of `x`, `\\log_b(x)`. If `b` is
    unspecified, :func:`~mpmath.log` computes the natural (base `e`) logarithm
    and is equivalent to :func:`~mpmath.ln`. In general, the base `b` logarithm
    is defined in terms of the natural logarithm as
    `\\log_b(x) = \\ln(x)/\\ln(b)`.
    
    By convention, we take `\\log(0) = -\\infty`.
    
    The natural logarithm is real if `x > 0` and complex if `x < 0` or if
    `x` is complex. The principal branch of the complex logarithm is
    used, meaning that `\\Im(\\ln(x)) = -\\pi < \\arg(x) \\le \\pi`.
    
    **Examples**
    
    Some basic values and limits::
    
        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = True
        >>> log(1)
        0.0
        >>> log(2)
        0.693147180559945
        >>> log(1000,10)
        3.0
        >>> log(4, 16)
        0.5
        >>> log(j)
        (0.0 + 1.5707963267949j)
        >>> log(-1)
        (0.0 + 3.14159265358979j)
        >>> log(0)
        -inf
        >>> log(inf)
        +inf
    
    The natural logarithm is the antiderivative of `1/x`::
    
        >>> quad(lambda x: 1/x, [1, 5])
        1.6094379124341
        >>> log(5)
        1.6094379124341
        >>> diff(log, 10)
        0.1
    
    The Taylor series expansion of the natural logarithm around
    `x = 1` has coefficients `(-1)^{n+1}/n`::
    
        >>> nprint(taylor(log, 1, 7))
        [0.0, 1.0, -0.5, 0.333333, -0.25, 0.2, -0.166667, 0.142857]
    
    :func:`~mpmath.log` supports arbitrary precision evaluation::
    
        >>> mp.dps = 50
        >>> log(pi)
        1.1447298858494001741434273513530587116472948129153
        >>> log(pi, pi**3)
        0.33333333333333333333333333333333333333333333333333
        >>> mp.dps = 25
        >>> log(3+4j)
        (1.609437912434100374600759 + 0.9272952180016122324285125j)
    """
def log10(ctx, x):
    """
    
    Computes the base-10 logarithm of `x`, `\\log_{10}(x)`. ``log10(x)``
    is equivalent to ``log(x, 10)``.
    """
def log1p(ctx, x):
    ...
def mangoldt(ctx, n):
    """
    
    Evaluates the von Mangoldt function `\\Lambda(n) = \\log p`
    if `n = p^k` a power of a prime, and `\\Lambda(n) = 0` otherwise.
    
    **Examples**
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> [mangoldt(n) for n in range(-2,3)]
        [0.0, 0.0, 0.0, 0.0, 0.6931471805599453094172321]
        >>> mangoldt(6)
        0.0
        >>> mangoldt(7)
        1.945910149055313305105353
        >>> mangoldt(8)
        0.6931471805599453094172321
        >>> fsum(mangoldt(n) for n in range(101))
        94.04531122935739224600493
        >>> fsum(mangoldt(n) for n in range(10001))
        10013.39669326311478372032
    
    """
def polar(ctx, z):
    """
    
    Returns the polar representation of the complex number `z`
    as a pair `(r, \\phi)` such that `z = r e^{i \\phi}`::
    
        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = True
        >>> polar(-2)
        (2.0, 3.14159265358979)
        >>> polar(3-4j)
        (5.0, -0.927295218001612)
    """
def polyexp(ctx, s, z):
    ...
def powm1(ctx, x, y):
    ...
def radians(ctx, x):
    """
    
    Converts the degree angle `x` to radians::
    
        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = True
        >>> radians(60)
        1.0471975511966
    """
def re(ctx, x):
    """
    
    Returns the real part of `x`, `\\Re(x)`. :func:`~mpmath.re`
    converts a non-mpmath number to an mpmath number::
    
        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = False
        >>> re(3)
        mpf('3.0')
        >>> re(-1+4j)
        mpf('-1.0')
    """
def rect(ctx, r, phi):
    ...
def root(ctx, x, n, k = 0):
    """
    
    ``root(z, n, k=0)`` computes an `n`-th root of `z`, i.e. returns a number
    `r` that (up to possible approximation error) satisfies `r^n = z`.
    (``nthroot`` is available as an alias for ``root``.)
    
    Every complex number `z \\ne 0` has `n` distinct `n`-th roots, which are
    equidistant points on a circle with radius `|z|^{1/n}`, centered around the
    origin. A specific root may be selected using the optional index
    `k`. The roots are indexed counterclockwise, starting with `k = 0` for the root
    closest to the positive real half-axis.
    
    The `k = 0` root is the so-called principal `n`-th root, often denoted by
    `\\sqrt[n]{z}` or `z^{1/n}`, and also given by `\\exp(\\log(z) / n)`. If `z` is
    a positive real number, the principal root is just the unique positive
    `n`-th root of `z`. Under some circumstances, non-principal real roots exist:
    for positive real `z`, `n` even, there is a negative root given by `k = n/2`;
    for negative real `z`, `n` odd, there is a negative root given by `k = (n-1)/2`.
    
    To obtain all roots with a simple expression, use
    ``[root(z,n,k) for k in range(n)]``.
    
    An important special case, ``root(1, n, k)`` returns the `k`-th `n`-th root of
    unity, `\\zeta_k = e^{2 \\pi i k / n}`. Alternatively, :func:`~mpmath.unitroots`
    provides a slightly more convenient way to obtain the roots of unity,
    including the option to compute only the primitive roots of unity.
    
    Both `k` and `n` should be integers; `k` outside of ``range(n)`` will be
    reduced modulo `n`. If `n` is negative, `x^{-1/n} = 1/x^{1/n}` (or
    the equivalent reciprocal for a non-principal root with `k \\ne 0`) is computed.
    
    :func:`~mpmath.root` is implemented to use Newton's method for small
    `n`. At high precision, this makes `x^{1/n}` not much more
    expensive than the regular exponentiation, `x^n`. For very large
    `n`, :func:`~mpmath.nthroot` falls back to use the exponential function.
    
    **Examples**
    
    :func:`~mpmath.nthroot`/:func:`~mpmath.root` is faster and more accurate than raising to a
    floating-point fraction::
    
        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = False
        >>> 16807 ** (mpf(1)/5)
        mpf('7.0000000000000009')
        >>> root(16807, 5)
        mpf('7.0')
        >>> nthroot(16807, 5)    # Alias
        mpf('7.0')
    
    A high-precision root::
    
        >>> mp.dps = 50; mp.pretty = True
        >>> nthroot(10, 5)
        1.584893192461113485202101373391507013269442133825
        >>> nthroot(10, 5) ** 5
        10.0
    
    Computing principal and non-principal square and cube roots::
    
        >>> mp.dps = 15
        >>> root(10, 2)
        3.16227766016838
        >>> root(10, 2, 1)
        -3.16227766016838
        >>> root(-10, 3)
        (1.07721734501594 + 1.86579517236206j)
        >>> root(-10, 3, 1)
        -2.15443469003188
        >>> root(-10, 3, 2)
        (1.07721734501594 - 1.86579517236206j)
    
    All the 7th roots of a complex number::
    
        >>> for r in [root(3+4j, 7, k) for k in range(7)]:
        ...     print("%s %s" % (r, r**7))
        ...
        (1.24747270589553 + 0.166227124177353j) (3.0 + 4.0j)
        (0.647824911301003 + 1.07895435170559j) (3.0 + 4.0j)
        (-0.439648254723098 + 1.17920694574172j) (3.0 + 4.0j)
        (-1.19605731775069 + 0.391492658196305j) (3.0 + 4.0j)
        (-1.05181082538903 - 0.691023585965793j) (3.0 + 4.0j)
        (-0.115529328478668 - 1.25318497558335j) (3.0 + 4.0j)
        (0.907748109144957 - 0.871672518271819j) (3.0 + 4.0j)
    
    Cube roots of unity::
    
        >>> for k in range(3): print(root(1, 3, k))
        ...
        1.0
        (-0.5 + 0.866025403784439j)
        (-0.5 - 0.866025403784439j)
    
    Some exact high order roots::
    
        >>> root(75**210, 105)
        5625.0
        >>> root(1, 128, 96)
        (0.0 - 1.0j)
        >>> root(4**128, 128, 96)
        (0.0 - 4.0j)
    
    """
def sec(ctx, z):
    ...
def sech(ctx, z):
    ...
def sign(ctx, x):
    """
    
    Returns the sign of `x`, defined as `\\mathrm{sign}(x) = x / |x|`
    (with the special case `\\mathrm{sign}(0) = 0`)::
    
        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = False
        >>> sign(10)
        mpf('1.0')
        >>> sign(-10)
        mpf('-1.0')
        >>> sign(0)
        mpf('0.0')
    
    Note that the sign function is also defined for complex numbers,
    for which it gives the projection onto the unit circle::
    
        >>> mp.dps = 15; mp.pretty = True
        >>> sign(1+j)
        (0.707106781186547 + 0.707106781186547j)
    
    """
def sinc(ctx, x):
    ...
def sincpi(ctx, x):
    ...
def stirling1(ctx, n, k, exact = False):
    """
    
    Gives the Stirling number of the first kind `s(n,k)`, defined by
    
    .. math ::
    
        x(x-1)(x-2)\\cdots(x-n+1) = \\sum_{k=0}^n s(n,k) x^k.
    
    The value is computed using an integer recurrence. The implementation
    is not optimized for approximating large values quickly.
    
    **Examples**
    
    Comparing with the generating function::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> taylor(lambda x: ff(x, 5), 0, 5)
        [0.0, 24.0, -50.0, 35.0, -10.0, 1.0]
        >>> [stirling1(5, k) for k in range(6)]
        [0.0, 24.0, -50.0, 35.0, -10.0, 1.0]
    
    Recurrence relation::
    
        >>> n, k = 5, 3
        >>> stirling1(n+1,k) + n*stirling1(n,k) - stirling1(n,k-1)
        0.0
    
    The matrices of Stirling numbers of first and second kind are inverses
    of each other::
    
        >>> A = matrix(5, 5); B = matrix(5, 5)
        >>> for n in range(5):
        ...     for k in range(5):
        ...         A[n,k] = stirling1(n,k)
        ...         B[n,k] = stirling2(n,k)
        ...
        >>> A * B
        [1.0  0.0  0.0  0.0  0.0]
        [0.0  1.0  0.0  0.0  0.0]
        [0.0  0.0  1.0  0.0  0.0]
        [0.0  0.0  0.0  1.0  0.0]
        [0.0  0.0  0.0  0.0  1.0]
    
    Pass ``exact=True`` to obtain exact values of Stirling numbers as integers::
    
        >>> stirling1(42, 5)
        -2.864498971768501633736628e+50
        >>> print(stirling1(42, 5, exact=True))
        -286449897176850163373662803014001546235808317440000
    
    """
def stirling2(ctx, n, k, exact = False):
    """
    
    Gives the Stirling number of the second kind `S(n,k)`, defined by
    
    .. math ::
    
        x^n = \\sum_{k=0}^n S(n,k) x(x-1)(x-2)\\cdots(x-k+1)
    
    The value is computed using integer arithmetic to evaluate a power sum.
    The implementation is not optimized for approximating large values quickly.
    
    **Examples**
    
    Comparing with the generating function::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> taylor(lambda x: sum(stirling2(5,k) * ff(x,k) for k in range(6)), 0, 5)
        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0]
    
    Recurrence relation::
    
        >>> n, k = 5, 3
        >>> stirling2(n+1,k) - k*stirling2(n,k) - stirling2(n,k-1)
        0.0
    
    Pass ``exact=True`` to obtain exact values of Stirling numbers as integers::
    
        >>> stirling2(52, 10)
        2.641822121003543906807485e+45
        >>> print(stirling2(52, 10, exact=True))
        2641822121003543906807485307053638921722527655
    
    
    """
def unitroots(ctx, n, primitive = False):
    """
    
    ``unitroots(n)`` returns `\\zeta_0, \\zeta_1, \\ldots, \\zeta_{n-1}`,
    all the distinct `n`-th roots of unity, as a list. If the option
    *primitive=True* is passed, only the primitive roots are returned.
    
    Every `n`-th root of unity satisfies `(\\zeta_k)^n = 1`. There are `n` distinct
    roots for each `n` (`\\zeta_k` and `\\zeta_j` are the same when
    `k = j \\pmod n`), which form a regular polygon with vertices on the unit
    circle. They are ordered counterclockwise with increasing `k`, starting
    with `\\zeta_0 = 1`.
    
    **Examples**
    
    The roots of unity up to `n = 4`::
    
        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = True
        >>> nprint(unitroots(1))
        [1.0]
        >>> nprint(unitroots(2))
        [1.0, -1.0]
        >>> nprint(unitroots(3))
        [1.0, (-0.5 + 0.866025j), (-0.5 - 0.866025j)]
        >>> nprint(unitroots(4))
        [1.0, (0.0 + 1.0j), -1.0, (0.0 - 1.0j)]
    
    Roots of unity form a geometric series that sums to 0::
    
        >>> mp.dps = 50
        >>> chop(fsum(unitroots(25)))
        0.0
    
    Primitive roots up to `n = 4`::
    
        >>> mp.dps = 15
        >>> nprint(unitroots(1, primitive=True))
        [1.0]
        >>> nprint(unitroots(2, primitive=True))
        [-1.0]
        >>> nprint(unitroots(3, primitive=True))
        [(-0.5 + 0.866025j), (-0.5 - 0.866025j)]
        >>> nprint(unitroots(4, primitive=True))
        [(0.0 + 1.0j), (0.0 - 1.0j)]
    
    There are only four primitive 12th roots::
    
        >>> nprint(unitroots(12, primitive=True))
        [(0.866025 + 0.5j), (-0.866025 + 0.5j), (-0.866025 - 0.5j), (0.866025 - 0.5j)]
    
    The `n`-th roots of unity form a group, the cyclic group of order `n`.
    Any primitive root `r` is a generator for this group, meaning that
    `r^0, r^1, \\ldots, r^{n-1}` gives the whole set of unit roots (in
    some permuted order)::
    
        >>> for r in unitroots(6): print(r)
        ...
        1.0
        (0.5 + 0.866025403784439j)
        (-0.5 + 0.866025403784439j)
        -1.0
        (-0.5 - 0.866025403784439j)
        (0.5 - 0.866025403784439j)
        >>> r = unitroots(6, primitive=True)[1]
        >>> for k in range(6): print(chop(r**k))
        ...
        1.0
        (0.5 - 0.866025403784439j)
        (-0.5 - 0.866025403784439j)
        -1.0
        (-0.5 + 0.866025403784438j)
        (0.5 + 0.866025403784438j)
    
    The number of primitive roots equals the Euler totient function `\\phi(n)`::
    
        >>> [len(unitroots(n, primitive=True)) for n in range(1,20)]
        [1, 1, 2, 2, 4, 2, 6, 4, 6, 4, 10, 4, 12, 6, 8, 8, 16, 6, 18]
    
    """
