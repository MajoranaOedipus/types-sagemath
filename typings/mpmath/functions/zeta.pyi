import __future__
from __future__ import annotations
from builtins import range as xrange
from mpmath.functions.functions import defun
from mpmath.functions.functions import defun_static
from mpmath.functions.functions import defun_wrapped
__all__: list[str] = ['altzeta', 'bernpoly', 'clcos', 'clsin', 'defun', 'defun_static', 'defun_wrapped', 'dirichlet', 'eulernum', 'eulerpoly', 'grampoint', 'lerchphi', 'oldzetazero', 'polylog', 'polylog_continuation', 'polylog_general', 'polylog_series', 'polylog_unitcircle', 'primepi', 'primepi2', 'primezeta', 'print_function', 'riemannr', 'secondzeta', 'secondzeta_exp_term', 'secondzeta_main_term', 'secondzeta_prime_term', 'secondzeta_singular_term', 'siegeltheta', 'siegelz', 'stieltjes', 'xrange', 'zeta']
def _altzeta_generic(ctx, s):
    ...
def _hurwitz(ctx, s, a = 1, d = 0, **kwargs):
    ...
def _hurwitz_em(ctx, s, a, d, prec, verbose):
    ...
def _hurwitz_reflection(ctx, s, a, d, atype):
    ...
def _load_zeta_zeros(url):
    ...
def _zetasum(ctx, s, a, n, derivatives = [0], reflect = False):
    """
    
    Returns [xd0,xd1,...,xdr], [yd0,yd1,...ydr] where
    
    xdk = D^k     ( 1/a^s     +  1/(a+1)^s      +  ...  +  1/(a+n)^s     )
    ydk = D^k conj( 1/a^(1-s) +  1/(a+1)^(1-s)  +  ...  +  1/(a+n)^(1-s) )
    
    D^k = kth derivative with respect to s, k ranges over the given list of
    derivatives (which should consist of either a single element
    or a range 0,1,...r). If reflect=False, the ydks are not computed.
    """
def altzeta(ctx, s, **kwargs):
    """
    
    Gives the Dirichlet eta function, `\\eta(s)`, also known as the
    alternating zeta function. This function is defined in analogy
    with the Riemann zeta function as providing the sum of the
    alternating series
    
    .. math ::
    
        \\eta(s) = \\sum_{k=0}^{\\infty} \\frac{(-1)^k}{k^s}
            = 1-\\frac{1}{2^s}+\\frac{1}{3^s}-\\frac{1}{4^s}+\\ldots
    
    The eta function, unlike the Riemann zeta function, is an entire
    function, having a finite value for all complex `s`. The special case
    `\\eta(1) = \\log(2)` gives the value of the alternating harmonic series.
    
    The alternating zeta function may expressed using the Riemann zeta function
    as `\\eta(s) = (1 - 2^{1-s}) \\zeta(s)`. It can also be expressed
    in terms of the Hurwitz zeta function, for example using
    :func:`~mpmath.dirichlet` (see documentation for that function).
    
    **Examples**
    
    Some special values are::
    
        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = True
        >>> altzeta(1)
        0.693147180559945
        >>> altzeta(0)
        0.5
        >>> altzeta(-1)
        0.25
        >>> altzeta(-2)
        0.0
    
    An example of a sum that can be computed more accurately and
    efficiently via :func:`~mpmath.altzeta` than via numerical summation::
    
        >>> sum(-(-1)**n / mpf(n)**2.5 for n in range(1, 100))
        0.867204951503984
        >>> altzeta(2.5)
        0.867199889012184
    
    At positive even integers, the Dirichlet eta function
    evaluates to a rational multiple of a power of `\\pi`::
    
        >>> altzeta(2)
        0.822467033424113
        >>> pi**2/12
        0.822467033424113
    
    Like the Riemann zeta function, `\\eta(s)`, approaches 1
    as `s` approaches positive infinity, although it does
    so from below rather than from above::
    
        >>> altzeta(30)
        0.999999999068682
        >>> altzeta(inf)
        1.0
        >>> mp.pretty = False
        >>> altzeta(1000, rounding='d')
        mpf('0.99999999999999989')
        >>> altzeta(1000, rounding='u')
        mpf('1.0')
    
    **References**
    
    1. http://mathworld.wolfram.com/DirichletEtaFunction.html
    
    2. http://en.wikipedia.org/wiki/Dirichlet_eta_function
    """
def bernpoly(ctx, n, z):
    ...
def clcos(ctx, s, z, pi = False):
    ...
def clsin(ctx, s, z, pi = False):
    ...
def dirichlet(ctx, s, chi = [1], derivative = 0):
    """
    
    Evaluates the Dirichlet L-function
    
    .. math ::
    
        L(s,\\chi) = \\sum_{k=1}^\\infty \\frac{\\chi(k)}{k^s}.
    
    where `\\chi` is a periodic sequence of length `q` which should be supplied
    in the form of a list `[\\chi(0), \\chi(1), \\ldots, \\chi(q-1)]`.
    Strictly, `\\chi` should be a Dirichlet character, but any periodic
    sequence will work.
    
    For example, ``dirichlet(s, [1])`` gives the ordinary
    Riemann zeta function and ``dirichlet(s, [-1,1])`` gives
    the alternating zeta function (Dirichlet eta function).
    
    Also the derivative with respect to `s` (currently only a first
    derivative) can be evaluated.
    
    **Examples**
    
    The ordinary Riemann zeta function::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> dirichlet(3, [1]); zeta(3)
        1.202056903159594285399738
        1.202056903159594285399738
        >>> dirichlet(1, [1])
        +inf
    
    The alternating zeta function::
    
        >>> dirichlet(1, [-1,1]); ln(2)
        0.6931471805599453094172321
        0.6931471805599453094172321
    
    The following defines the Dirichlet beta function
    `\\beta(s) = \\sum_{k=0}^\\infty \\frac{(-1)^k}{(2k+1)^s}` and verifies
    several values of this function::
    
        >>> B = lambda s, d=0: dirichlet(s, [0, 1, 0, -1], d)
        >>> B(0); 1./2
        0.5
        0.5
        >>> B(1); pi/4
        0.7853981633974483096156609
        0.7853981633974483096156609
        >>> B(2); +catalan
        0.9159655941772190150546035
        0.9159655941772190150546035
        >>> B(2,1); diff(B, 2)
        0.08158073611659279510291217
        0.08158073611659279510291217
        >>> B(-1,1); 2*catalan/pi
        0.5831218080616375602767689
        0.5831218080616375602767689
        >>> B(0,1); log(gamma(0.25)**2/(2*pi*sqrt(2)))
        0.3915943927068367764719453
        0.3915943927068367764719454
        >>> B(1,1); 0.25*pi*(euler+2*ln2+3*ln(pi)-4*ln(gamma(0.25)))
        0.1929013167969124293631898
        0.1929013167969124293631898
    
    A custom L-series of period 3::
    
        >>> dirichlet(2, [2,0,1])
        0.7059715047839078092146831
        >>> 2*nsum(lambda k: (3*k)**-2, [1,inf]) + \\
        ...   nsum(lambda k: (3*k+2)**-2, [0,inf])
        0.7059715047839078092146831
    
    """
def eulernum(ctx, n, exact = False):
    """
    
    Gives the `n`-th Euler number, defined as the `n`-th derivative of
    `\\mathrm{sech}(t) = 1/\\cosh(t)` evaluated at `t = 0`. Equivalently, the
    Euler numbers give the coefficients of the Taylor series
    
    .. math ::
    
        \\mathrm{sech}(t) = \\sum_{n=0}^{\\infty} \\frac{E_n}{n!} t^n.
    
    The Euler numbers are closely related to Bernoulli numbers
    and Bernoulli polynomials. They can also be evaluated in terms of
    Euler polynomials (see :func:`~mpmath.eulerpoly`) as `E_n = 2^n E_n(1/2)`.
    
    **Examples**
    
    Computing the first few Euler numbers and verifying that they
    agree with the Taylor series::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> [eulernum(n) for n in range(11)]
        [1.0, 0.0, -1.0, 0.0, 5.0, 0.0, -61.0, 0.0, 1385.0, 0.0, -50521.0]
        >>> chop(diffs(sech, 0, 10))
        [1.0, 0.0, -1.0, 0.0, 5.0, 0.0, -61.0, 0.0, 1385.0, 0.0, -50521.0]
    
    Euler numbers grow very rapidly. :func:`~mpmath.eulernum` efficiently
    computes numerical approximations for large indices::
    
        >>> eulernum(50)
        -6.053285248188621896314384e+54
        >>> eulernum(1000)
        3.887561841253070615257336e+2371
        >>> eulernum(10**20)
        4.346791453661149089338186e+1936958564106659551331
    
    Comparing with an asymptotic formula for the Euler numbers::
    
        >>> n = 10**5
        >>> (-1)**(n//2) * 8 * sqrt(n/(2*pi)) * (2*n/(pi*e))**n
        3.69919063017432362805663e+436961
        >>> eulernum(n)
        3.699193712834466537941283e+436961
    
    Pass ``exact=True`` to obtain exact values of Euler numbers as integers::
    
        >>> print(eulernum(50, exact=True))
        -6053285248188621896314383785111649088103498225146815121
        >>> print(eulernum(200, exact=True) % 10**10)
        1925859625
        >>> eulernum(1001, exact=True)
        0
    """
def eulerpoly(ctx, n, z):
    ...
def grampoint(ctx, n):
    ...
def lerchphi(ctx, z, s, a):
    """
    
    Gives the Lerch transcendent, defined for `|z| < 1` and
    `\\Re{a} > 0` by
    
    .. math ::
    
        \\Phi(z,s,a) = \\sum_{k=0}^{\\infty} \\frac{z^k}{(a+k)^s}
    
    and generally by the recurrence `\\Phi(z,s,a) = z \\Phi(z,s,a+1) + a^{-s}`
    along with the integral representation valid for `\\Re{a} > 0`
    
    .. math ::
    
        \\Phi(z,s,a) = \\frac{1}{2 a^s} +
                \\int_0^{\\infty} \\frac{z^t}{(a+t)^s} dt -
                2 \\int_0^{\\infty} \\frac{\\sin(t \\log z - s
                    \\operatorname{arctan}(t/a)}{(a^2 + t^2)^{s/2}
                    (e^{2 \\pi t}-1)} dt.
    
    The Lerch transcendent generalizes the Hurwitz zeta function :func:`zeta`
    (`z = 1`) and the polylogarithm :func:`polylog` (`a = 1`).
    
    **Examples**
    
    Several evaluations in terms of simpler functions::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> lerchphi(-1,2,0.5); 4*catalan
        3.663862376708876060218414
        3.663862376708876060218414
        >>> diff(lerchphi, (-1,-2,1), (0,1,0)); 7*zeta(3)/(4*pi**2)
        0.2131391994087528954617607
        0.2131391994087528954617607
        >>> lerchphi(-4,1,1); log(5)/4
        0.4023594781085250936501898
        0.4023594781085250936501898
        >>> lerchphi(-3+2j,1,0.5); 2*atanh(sqrt(-3+2j))/sqrt(-3+2j)
        (1.142423447120257137774002 + 0.2118232380980201350495795j)
        (1.142423447120257137774002 + 0.2118232380980201350495795j)
    
    Evaluation works for complex arguments and `|z| \\ge 1`::
    
        >>> lerchphi(1+2j, 3-j, 4+2j)
        (0.002025009957009908600539469 + 0.003327897536813558807438089j)
        >>> lerchphi(-2,2,-2.5)
        -12.28676272353094275265944
        >>> lerchphi(10,10,10)
        (-4.462130727102185701817349e-11 - 1.575172198981096218823481e-12j)
        >>> lerchphi(10,10,-10.5)
        (112658784011940.5605789002 - 498113185.5756221777743631j)
    
    Some degenerate cases::
    
        >>> lerchphi(0,1,2)
        0.5
        >>> lerchphi(0,1,-2)
        -0.5
    
    Reduction to simpler functions::
    
        >>> lerchphi(1, 4.25+1j, 1)
        (1.044674457556746668033975 - 0.04674508654012658932271226j)
        >>> zeta(4.25+1j)
        (1.044674457556746668033975 - 0.04674508654012658932271226j)
        >>> lerchphi(1 - 0.5**10, 4.25+1j, 1)
        (1.044629338021507546737197 - 0.04667768813963388181708101j)
        >>> lerchphi(3, 4, 1)
        (1.249503297023366545192592 - 0.2314252413375664776474462j)
        >>> polylog(4, 3) / 3
        (1.249503297023366545192592 - 0.2314252413375664776474462j)
        >>> lerchphi(3, 4, 1 - 0.5**10)
        (1.253978063946663945672674 - 0.2316736622836535468765376j)
    
    **References**
    
    1. [DLMF]_ section 25.14
    
    """
def oldzetazero(ctx, n, url = 'http://www.dtc.umn.edu/~odlyzko/zeta_tables/zeros1'):
    ...
def polylog(ctx, s, z):
    ...
def polylog_continuation(ctx, n, z):
    ...
def polylog_general(ctx, s, z):
    ...
def polylog_series(ctx, s, z):
    ...
def polylog_unitcircle(ctx, n, z):
    ...
def primepi(ctx, x):
    ...
def primepi2(ctx, x):
    ...
def primezeta(ctx, s):
    ...
def riemannr(ctx, x):
    ...
def secondzeta(ctx, s, a = 0.015, **kwargs):
    """
    
    Evaluates the secondary zeta function `Z(s)`, defined for
    `\\mathrm{Re}(s)>1` by
    
    .. math ::
    
        Z(s) = \\sum_{n=1}^{\\infty} \\frac{1}{\\tau_n^s}
    
    where `\\frac12+i\\tau_n` runs through the zeros of `\\zeta(s)` with
    imaginary part positive.
    
    `Z(s)` extends to a meromorphic function on `\\mathbb{C}`  with a
    double pole at `s=1` and  simple poles at the points `-2n` for
    `n=0`,  1, 2, ...
    
    **Examples**
    
        >>> from mpmath import *
        >>> mp.pretty = True; mp.dps = 15
        >>> secondzeta(2)
        0.023104993115419
        >>> xi = lambda s: 0.5*s*(s-1)*pi**(-0.5*s)*gamma(0.5*s)*zeta(s)
        >>> Xi = lambda t: xi(0.5+t*j)
        >>> chop(-0.5*diff(Xi,0,n=2)/Xi(0))
        0.023104993115419
    
    We may ask for an approximate error value::
    
        >>> secondzeta(0.5+100j, error=True)
        ((-0.216272011276718 - 0.844952708937228j), 2.22044604925031e-16)
    
    The function has poles at the negative odd integers,
    and dyadic rational values at the negative even integers::
    
        >>> mp.dps = 30
        >>> secondzeta(-8)
        -0.67236328125
        >>> secondzeta(-7)
        +inf
    
    **Implementation notes**
    
    The function is computed as sum of four terms `Z(s)=A(s)-P(s)+E(s)-S(s)`
    respectively main, prime, exponential and singular terms.
    The main term `A(s)` is computed from the zeros of zeta.
    The prime term depends on the von Mangoldt function.
    The singular term is responsible for the poles of the function.
    
    The four terms depends on a small parameter `a`. We may change the
    value of `a`. Theoretically this has no effect on the sum of the four
    terms, but in practice may be important.
    
    A smaller value of the parameter `a` makes `A(s)` depend on
    a smaller number of zeros of zeta, but `P(s)`  uses more values of
    von Mangoldt function.
    
    We may also add a verbose option to obtain data about the
    values of the four terms.
    
        >>> mp.dps = 10
        >>> secondzeta(0.5 + 40j, error=True, verbose=True)
        main term = (-30190318549.138656312556 - 13964804384.624622876523j)
            computed using 19 zeros of zeta
        prime term = (132717176.89212754625045 + 188980555.17563978290601j)
            computed using 9 values of the von Mangoldt function
        exponential term = (542447428666.07179812536 + 362434922978.80192435203j)
        singular term = (512124392939.98154322355 + 348281138038.65531023921j)
        ((0.059471043 + 0.3463514534j), 1.455191523e-11)
    
        >>> secondzeta(0.5 + 40j, a=0.04, error=True, verbose=True)
        main term = (-151962888.19606243907725 - 217930683.90210294051982j)
            computed using 9 zeros of zeta
        prime term = (2476659342.3038722372461 + 28711581821.921627163136j)
            computed using 37 values of the von Mangoldt function
        exponential term = (178506047114.7838188264 + 819674143244.45677330576j)
        singular term = (175877424884.22441310708 + 790744630738.28669174871j)
        ((0.059471043 + 0.3463514534j), 1.455191523e-11)
    
    Notice the great cancellation between the four terms. Changing `a`, the
    four terms are very different numbers but the cancellation gives
    the good value of Z(s).
    
    **References**
    
    A. Voros, Zeta functions for the Riemann zeros, Ann. Institute Fourier,
    53, (2003) 665--699.
    
    A. Voros, Zeta functions over Zeros of Zeta Functions, Lecture Notes
    of the Unione Matematica Italiana, Springer, 2009.
    """
def secondzeta_exp_term(ctx, s, a):
    ...
def secondzeta_main_term(ctx, s, a, **kwargs):
    ...
def secondzeta_prime_term(ctx, s, a, **kwargs):
    ...
def secondzeta_singular_term(ctx, s, a, **kwargs):
    ...
def siegeltheta(ctx, t, derivative = 0):
    ...
def siegelz(ctx, t, **kwargs):
    ...
def stieltjes(ctx, n, a = 1):
    """
    
    For a nonnegative integer `n`, ``stieltjes(n)`` computes the
    `n`-th Stieltjes constant `\\gamma_n`, defined as the
    `n`-th coefficient in the Laurent series expansion of the
    Riemann zeta function around the pole at `s = 1`. That is,
    we have:
    
    .. math ::
    
      \\zeta(s) = \\frac{1}{s-1} \\sum_{n=0}^{\\infty}
          \\frac{(-1)^n}{n!} \\gamma_n (s-1)^n
    
    More generally, ``stieltjes(n, a)`` gives the corresponding
    coefficient `\\gamma_n(a)` for the Hurwitz zeta function
    `\\zeta(s,a)` (with `\\gamma_n = \\gamma_n(1)`).
    
    **Examples**
    
    The zeroth Stieltjes constant is just Euler's constant `\\gamma`::
    
        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = True
        >>> stieltjes(0)
        0.577215664901533
    
    Some more values are::
    
        >>> stieltjes(1)
        -0.0728158454836767
        >>> stieltjes(10)
        0.000205332814909065
        >>> stieltjes(30)
        0.00355772885557316
        >>> stieltjes(1000)
        -1.57095384420474e+486
        >>> stieltjes(2000)
        2.680424678918e+1109
        >>> stieltjes(1, 2.5)
        -0.23747539175716
    
    An alternative way to compute `\\gamma_1`::
    
        >>> diff(extradps(15)(lambda x: 1/(x-1) - zeta(x)), 1)
        -0.0728158454836767
    
    :func:`~mpmath.stieltjes` supports arbitrary precision evaluation::
    
        >>> mp.dps = 50
        >>> stieltjes(2)
        -0.0096903631928723184845303860352125293590658061013408
    
    **Algorithm**
    
    :func:`~mpmath.stieltjes` numerically evaluates the integral in
    the following representation due to Ainsworth, Howell and
    Coffey [1], [2]:
    
    .. math ::
    
      \\gamma_n(a) = \\frac{\\log^n a}{2a} - \\frac{\\log^{n+1}(a)}{n+1} +
          \\frac{2}{a} \\Re \\int_0^{\\infty}
          \\frac{(x/a-i)\\log^n(a-ix)}{(1+x^2/a^2)(e^{2\\pi x}-1)} dx.
    
    For some reference values with `a = 1`, see e.g. [4].
    
    **References**
    
    1. O. R. Ainsworth & L. W. Howell, "An integral representation of
       the generalized Euler-Mascheroni constants", NASA Technical
       Paper 2456 (1985),
       http://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/19850014994_1985014994.pdf
    
    2. M. W. Coffey, "The Stieltjes constants, their relation to the
       `\\eta_j` coefficients, and representation of the Hurwitz
       zeta function", 	arXiv:0706.0343v1 http://arxiv.org/abs/0706.0343
    
    3. http://mathworld.wolfram.com/StieltjesConstants.html
    
    4. http://pi.lacim.uqam.ca/piDATA/stieltjesgamma.txt
    
    """
def zeta(ctx, s, a = 1, derivative = 0, method = None, **kwargs):
    """
    
    Computes the Riemann zeta function
    
    .. math ::
    
      \\zeta(s) = 1+\\frac{1}{2^s}+\\frac{1}{3^s}+\\frac{1}{4^s}+\\ldots
    
    or, with `a \\ne 1`, the more general Hurwitz zeta function
    
    .. math ::
    
        \\zeta(s,a) = \\sum_{k=0}^\\infty \\frac{1}{(a+k)^s}.
    
    Optionally, ``zeta(s, a, n)`` computes the `n`-th derivative with
    respect to `s`,
    
    .. math ::
    
        \\zeta^{(n)}(s,a) = (-1)^n \\sum_{k=0}^\\infty \\frac{\\log^n(a+k)}{(a+k)^s}.
    
    Although these series only converge for `\\Re(s) > 1`, the Riemann and Hurwitz
    zeta functions are defined through analytic continuation for arbitrary
    complex `s \\ne 1` (`s = 1` is a pole).
    
    The implementation uses three algorithms: the Borwein algorithm for
    the Riemann zeta function when `s` is close to the real line;
    the Riemann-Siegel formula for the Riemann zeta function when `s` is
    large imaginary, and Euler-Maclaurin summation in all other cases.
    The reflection formula for `\\Re(s) < 0` is implemented in some cases.
    The algorithm can be chosen with ``method = 'borwein'``,
    ``method='riemann-siegel'`` or ``method = 'euler-maclaurin'``.
    
    The parameter `a` is usually a rational number `a = p/q`, and may be specified
    as such by passing an integer tuple `(p, q)`. Evaluation is supported for
    arbitrary complex `a`, but may be slow and/or inaccurate when `\\Re(s) < 0` for
    nonrational `a` or when computing derivatives.
    
    **Examples**
    
    Some values of the Riemann zeta function::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> zeta(2); pi**2 / 6
        1.644934066848226436472415
        1.644934066848226436472415
        >>> zeta(0)
        -0.5
        >>> zeta(-1)
        -0.08333333333333333333333333
        >>> zeta(-2)
        0.0
    
    For large positive `s`, `\\zeta(s)` rapidly approaches 1::
    
        >>> zeta(50)
        1.000000000000000888178421
        >>> zeta(100)
        1.0
        >>> zeta(inf)
        1.0
        >>> 1-sum((zeta(k)-1)/k for k in range(2,85)); +euler
        0.5772156649015328606065121
        0.5772156649015328606065121
        >>> nsum(lambda k: zeta(k)-1, [2, inf])
        1.0
    
    Evaluation is supported for complex `s` and `a`:
    
        >>> zeta(-3+4j)
        (-0.03373057338827757067584698 + 0.2774499251557093745297677j)
        >>> zeta(2+3j, -1+j)
        (389.6841230140842816370741 + 295.2674610150305334025962j)
    
    The Riemann zeta function has so-called nontrivial zeros on
    the critical line `s = 1/2 + it`::
    
        >>> findroot(zeta, 0.5+14j); zetazero(1)
        (0.5 + 14.13472514173469379045725j)
        (0.5 + 14.13472514173469379045725j)
        >>> findroot(zeta, 0.5+21j); zetazero(2)
        (0.5 + 21.02203963877155499262848j)
        (0.5 + 21.02203963877155499262848j)
        >>> findroot(zeta, 0.5+25j); zetazero(3)
        (0.5 + 25.01085758014568876321379j)
        (0.5 + 25.01085758014568876321379j)
        >>> chop(zeta(zetazero(10)))
        0.0
    
    Evaluation on and near the critical line is supported for large
    heights `t` by means of the Riemann-Siegel formula (currently
    for `a = 1`, `n \\le 4`)::
    
        >>> zeta(0.5+100000j)
        (1.073032014857753132114076 + 5.780848544363503984261041j)
        >>> zeta(0.75+1000000j)
        (0.9535316058375145020351559 + 0.9525945894834273060175651j)
        >>> zeta(0.5+10000000j)
        (11.45804061057709254500227 - 8.643437226836021723818215j)
        >>> zeta(0.5+100000000j, derivative=1)
        (51.12433106710194942681869 + 43.87221167872304520599418j)
        >>> zeta(0.5+100000000j, derivative=2)
        (-444.2760822795430400549229 - 896.3789978119185981665403j)
        >>> zeta(0.5+100000000j, derivative=3)
        (3230.72682687670422215339 + 14374.36950073615897616781j)
        >>> zeta(0.5+100000000j, derivative=4)
        (-11967.35573095046402130602 - 218945.7817789262839266148j)
        >>> zeta(1+10000000j)    # off the line
        (2.859846483332530337008882 + 0.491808047480981808903986j)
        >>> zeta(1+10000000j, derivative=1)
        (-4.333835494679647915673205 - 0.08405337962602933636096103j)
        >>> zeta(1+10000000j, derivative=4)
        (453.2764822702057701894278 - 581.963625832768189140995j)
    
    For investigation of the zeta function zeros, the Riemann-Siegel
    Z-function is often more convenient than working with the Riemann
    zeta function directly (see :func:`~mpmath.siegelz`).
    
    Some values of the Hurwitz zeta function::
    
        >>> zeta(2, 3); -5./4 + pi**2/6
        0.3949340668482264364724152
        0.3949340668482264364724152
        >>> zeta(2, (3,4)); pi**2 - 8*catalan
        2.541879647671606498397663
        2.541879647671606498397663
    
    For positive integer values of `s`, the Hurwitz zeta function is
    equivalent to a polygamma function (except for a normalizing factor)::
    
        >>> zeta(4, (1,5)); psi(3, '1/5')/6
        625.5408324774542966919938
        625.5408324774542966919938
    
    Evaluation of derivatives::
    
        >>> zeta(0, 3+4j, 1); loggamma(3+4j) - ln(2*pi)/2
        (-2.675565317808456852310934 + 4.742664438034657928194889j)
        (-2.675565317808456852310934 + 4.742664438034657928194889j)
        >>> zeta(2, 1, 20)
        2432902008176640000.000242
        >>> zeta(3+4j, 5.5+2j, 4)
        (-0.140075548947797130681075 - 0.3109263360275413251313634j)
        >>> zeta(0.5+100000j, 1, 4)
        (-10407.16081931495861539236 + 13777.78669862804508537384j)
        >>> zeta(-100+0.5j, (1,3), derivative=4)
        (4.007180821099823942702249e+79 + 4.916117957092593868321778e+78j)
    
    Generating a Taylor series at `s = 2` using derivatives::
    
        >>> for k in range(11): print("%s * (s-2)^%i" % (zeta(2,1,k)/fac(k), k))
        ...
        1.644934066848226436472415 * (s-2)^0
        -0.9375482543158437537025741 * (s-2)^1
        0.9946401171494505117104293 * (s-2)^2
        -1.000024300473840810940657 * (s-2)^3
        1.000061933072352565457512 * (s-2)^4
        -1.000006869443931806408941 * (s-2)^5
        1.000000173233769531820592 * (s-2)^6
        -0.9999999569989868493432399 * (s-2)^7
        0.9999999937218844508684206 * (s-2)^8
        -0.9999999996355013916608284 * (s-2)^9
        1.000000000004610645020747 * (s-2)^10
    
    Evaluation at zero and for negative integer `s`::
    
        >>> zeta(0, 10)
        -9.5
        >>> zeta(-2, (2,3)); mpf(1)/81
        0.01234567901234567901234568
        0.01234567901234567901234568
        >>> zeta(-3+4j, (5,4))
        (0.2899236037682695182085988 + 0.06561206166091757973112783j)
        >>> zeta(-3.25, 1/pi)
        -0.0005117269627574430494396877
        >>> zeta(-3.5, pi, 1)
        11.156360390440003294709
        >>> zeta(-100.5, (8,3))
        -4.68162300487989766727122e+77
        >>> zeta(-10.5, (-8,3))
        (-0.01521913704446246609237979 + 29907.72510874248161608216j)
        >>> zeta(-1000.5, (-8,3))
        (1.031911949062334538202567e+1770 + 1.519555750556794218804724e+426j)
        >>> zeta(-1+j, 3+4j)
        (-16.32988355630802510888631 - 22.17706465801374033261383j)
        >>> zeta(-1+j, 3+4j, 2)
        (32.48985276392056641594055 - 51.11604466157397267043655j)
        >>> diff(lambda s: zeta(s, 3+4j), -1+j, 2)
        (32.48985276392056641594055 - 51.11604466157397267043655j)
    
    **References**
    
    1. http://mathworld.wolfram.com/RiemannZetaFunction.html
    
    2. http://mathworld.wolfram.com/HurwitzZetaFunction.html
    
    3. [BorweinZeta]_
    
    """
_zeta_zeros: list = [14.134725142, 21.022039639, 25.01085758, 30.424876126, 32.935061588, 37.586178159, 40.918719012, 43.327073281, 48.005150881, 49.773832478, 52.970321478, 56.446247697, 59.347044003, 60.831778525, 65.112544048, 67.079810529, 69.546401711, 72.067157674, 75.704690699, 77.144840069, 79.33737502, 82.910380854, 84.735492981, 87.425274613, 88.809111208, 92.491899271, 94.651344041, 95.870634228, 98.831194218, 101.317851006, 103.72553804, 105.446623052, 107.168611184, 111.029535543, 111.874659177, 114.320220915, 116.226680321, 118.790782866, 121.370125002, 122.946829294, 124.256818554, 127.51668388, 129.5787042, 131.087688531, 133.497737203, 134.756509753, 138.116042055, 139.736208952, 141.123707404, 143.111845808, 146.000982487, 147.422765343, 150.053520421, 150.925257612, 153.024693811, 156.112909294, 157.597591818, 158.849988171, 161.188964138, 163.030709687, 165.537069188, 167.184439978, 169.094515416, 169.911976479, 173.41153652, 174.754191523, 176.441434298, 178.377407776, 179.91648402, 182.207078484, 184.874467848, 185.598783678, 187.228922584, 189.416158656, 192.026656361, 193.079726604, 195.26539668, 196.876481841, 198.015309676, 201.264751944, 202.493594514, 204.189671803, 205.394697202, 207.906258888, 209.576509717, 211.690862595, 213.34791936, 214.547044783, 216.169538508, 219.067596349, 220.714918839, 221.430705555, 224.007000255, 224.98332467, 227.42144428, 229.337413306, 231.2501887, 231.987235253, 233.693404179, 236.524229666]
print_function: __future__._Feature  # value = _Feature((2, 6, 0, 'alpha', 2), (3, 0, 0, 'alpha', 0), 1048576)
