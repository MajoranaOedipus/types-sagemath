from __future__ import annotations
from mpmath.functions.functions import defun
from mpmath.functions.functions import defun_wrapped
__all__: list[str] = ['betainc', 'chi', 'ci', 'defun', 'defun_wrapped', 'e1', 'ei', 'erf', 'erfc', 'erfi', 'erfinv', 'expint', 'fresnelc', 'fresnels', 'gammainc', 'li', 'ncdf', 'npdf', 'shi', 'si', 'square_exp_arg']
def _ci_generic(ctx, z):
    ...
def _ei_generic(ctx, z):
    ...
def _erf_complex(ctx, z):
    ...
def _erfc_complex(ctx, z):
    ...
def _gamma3(ctx, z, a, b, regularized = False):
    ...
def _lower_gamma(ctx, z, b, regularized = False):
    ...
def _si_generic(ctx, z):
    ...
def _upper_gamma(ctx, z, a, regularized = False):
    ...
def betainc(ctx, a, b, x1 = 0, x2 = 1, regularized = False):
    ...
def chi(ctx, z):
    ...
def ci(ctx, z):
    """
    
    Computes the cosine integral,
    
    .. math ::
    
        \\mathrm{Ci}(x) = -\\int_x^{\\infty} \\frac{\\cos t}{t}\\,dt
        = \\gamma + \\log x + \\int_0^x \\frac{\\cos t - 1}{t}\\,dt
    
    **Examples**
    
    Some values and limits::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> ci(0)
        -inf
        >>> ci(1)
        0.3374039229009681346626462
        >>> ci(pi)
        0.07366791204642548599010096
        >>> ci(inf)
        0.0
        >>> ci(-inf)
        (0.0 + 3.141592653589793238462643j)
        >>> ci(2+3j)
        (1.408292501520849518759125 - 2.983617742029605093121118j)
    
    The cosine integral behaves roughly like the sinc function
    (see :func:`~mpmath.sinc`) for large real `x`::
    
        >>> ci(10**10)
        -4.875060251748226537857298e-11
        >>> sinc(10**10)
        -4.875060250875106915277943e-11
        >>> chop(limit(ci, inf))
        0.0
    
    It has infinitely many roots on the positive real axis::
    
        >>> findroot(ci, 1)
        0.6165054856207162337971104
        >>> findroot(ci, 2)
        3.384180422551186426397851
    
    Evaluation is supported for `z` anywhere in the complex plane::
    
        >>> ci(10**6*(1+j))
        (4.449410587611035724984376e+434287 + 9.75744874290013526417059e+434287j)
    
    We can evaluate the defining integral as a reference::
    
        >>> mp.dps = 15
        >>> -quadosc(lambda t: cos(t)/t, [5, inf], omega=1)
        -0.190029749656644
        >>> ci(5)
        -0.190029749656644
    
    Some infinite series can be evaluated using the
    cosine integral::
    
        >>> nsum(lambda k: (-1)**k/(fac(2*k)*(2*k)), [1,inf])
        -0.239811742000565
        >>> ci(1) - euler
        -0.239811742000565
    
    """
def e1(ctx, z):
    """
    
    Computes the exponential integral `\\mathrm{E}_1(z)`, given by
    
    .. math ::
    
        \\mathrm{E}_1(z) = \\int_z^{\\infty} \\frac{e^{-t}}{t} dt.
    
    This is equivalent to :func:`~mpmath.expint` with `n = 1`.
    
    **Examples**
    
    Two ways to evaluate this function::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> e1(6.25)
        0.0002704758872637179088496194
        >>> expint(1,6.25)
        0.0002704758872637179088496194
    
    The E1-function is essentially the same as the Ei-function (:func:`~mpmath.ei`)
    with negated argument, except for an imaginary branch cut term::
    
        >>> e1(2.5)
        0.02491491787026973549562801
        >>> -ei(-2.5)
        0.02491491787026973549562801
        >>> e1(-2.5)
        (-7.073765894578600711923552 - 3.141592653589793238462643j)
        >>> -ei(2.5)
        -7.073765894578600711923552
    
    """
def ei(ctx, z):
    """
    
    Computes the exponential integral or Ei-function, `\\mathrm{Ei}(x)`.
    The exponential integral is defined as
    
    .. math ::
    
      \\mathrm{Ei}(x) = \\int_{-\\infty\\,}^x \\frac{e^t}{t} \\, dt.
    
    When the integration range includes `t = 0`, the exponential
    integral is interpreted as providing the Cauchy principal value.
    
    For real `x`, the Ei-function behaves roughly like
    `\\mathrm{Ei}(x) \\approx \\exp(x) + \\log(|x|)`.
    
    The Ei-function is related to the more general family of exponential
    integral functions denoted by `E_n`, which are available as :func:`~mpmath.expint`.
    
    **Basic examples**
    
    Some basic values and limits are::
    
        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = True
        >>> ei(0)
        -inf
        >>> ei(1)
        1.89511781635594
        >>> ei(inf)
        +inf
        >>> ei(-inf)
        0.0
    
    For `x < 0`, the defining integral can be evaluated
    numerically as a reference::
    
        >>> ei(-4)
        -0.00377935240984891
        >>> quad(lambda t: exp(t)/t, [-inf, -4])
        -0.00377935240984891
    
    :func:`~mpmath.ei` supports complex arguments and arbitrary
    precision evaluation::
    
        >>> mp.dps = 50
        >>> ei(pi)
        10.928374389331410348638445906907535171566338835056
        >>> mp.dps = 25
        >>> ei(3+4j)
        (-4.154091651642689822535359 + 4.294418620024357476985535j)
    
    **Related functions**
    
    The exponential integral is closely related to the logarithmic
    integral. See :func:`~mpmath.li` for additional information.
    
    The exponential integral is related to the hyperbolic
    and trigonometric integrals (see :func:`~mpmath.chi`, :func:`~mpmath.shi`,
    :func:`~mpmath.ci`, :func:`~mpmath.si`) similarly to how the ordinary
    exponential function is related to the hyperbolic and
    trigonometric functions::
    
        >>> mp.dps = 15
        >>> ei(3)
        9.93383257062542
        >>> chi(3) + shi(3)
        9.93383257062542
        >>> chop(ci(3j) - j*si(3j) - pi*j/2)
        9.93383257062542
    
    Beware that logarithmic corrections, as in the last example
    above, are required to obtain the correct branch in general.
    For details, see [1].
    
    The exponential integral is also a special case of the
    hypergeometric function `\\,_2F_2`::
    
        >>> z = 0.6
        >>> z*hyper([1,1],[2,2],z) + (ln(z)-ln(1/z))/2 + euler
        0.769881289937359
        >>> ei(z)
        0.769881289937359
    
    **References**
    
    1. Relations between Ei and other functions:
       http://functions.wolfram.com/GammaBetaErf/ExpIntegralEi/27/01/
    
    2. Abramowitz & Stegun, section 5:
       http://people.math.sfu.ca/~cbm/aands/page_228.htm
    
    3. Asymptotic expansion for Ei:
       http://mathworld.wolfram.com/En-Function.html
    """
def erf(ctx, z):
    """
    
    Computes the error function, `\\mathrm{erf}(x)`. The error
    function is the normalized antiderivative of the Gaussian function
    `\\exp(-t^2)`. More precisely,
    
    .. math::
    
      \\mathrm{erf}(x) = \\frac{2}{\\sqrt \\pi} \\int_0^x \\exp(-t^2) \\,dt
    
    **Basic examples**
    
    Simple values and limits include::
    
        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = True
        >>> erf(0)
        0.0
        >>> erf(1)
        0.842700792949715
        >>> erf(-1)
        -0.842700792949715
        >>> erf(inf)
        1.0
        >>> erf(-inf)
        -1.0
    
    For large real `x`, `\\mathrm{erf}(x)` approaches 1 very
    rapidly::
    
        >>> erf(3)
        0.999977909503001
        >>> erf(5)
        0.999999999998463
    
    The error function is an odd function::
    
        >>> nprint(chop(taylor(erf, 0, 5)))
        [0.0, 1.12838, 0.0, -0.376126, 0.0, 0.112838]
    
    :func:`~mpmath.erf` implements arbitrary-precision evaluation and
    supports complex numbers::
    
        >>> mp.dps = 50
        >>> erf(0.5)
        0.52049987781304653768274665389196452873645157575796
        >>> mp.dps = 25
        >>> erf(1+j)
        (1.316151281697947644880271 + 0.1904534692378346862841089j)
    
    Evaluation is supported for large arguments::
    
        >>> mp.dps = 25
        >>> erf('1e1000')
        1.0
        >>> erf('-1e1000')
        -1.0
        >>> erf('1e-1000')
        1.128379167095512573896159e-1000
        >>> erf('1e7j')
        (0.0 + 8.593897639029319267398803e+43429448190317j)
        >>> erf('1e7+1e7j')
        (0.9999999858172446172631323 + 3.728805278735270407053139e-8j)
    
    **Related functions**
    
    See also :func:`~mpmath.erfc`, which is more accurate for large `x`,
    and :func:`~mpmath.erfi` which gives the antiderivative of
    `\\exp(t^2)`.
    
    The Fresnel integrals :func:`~mpmath.fresnels` and :func:`~mpmath.fresnelc`
    are also related to the error function.
    """
def erfc(ctx, z):
    """
    
    Computes the complementary error function,
    `\\mathrm{erfc}(x) = 1-\\mathrm{erf}(x)`.
    This function avoids cancellation that occurs when naively
    computing the complementary error function as ``1-erf(x)``::
    
        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = True
        >>> 1 - erf(10)
        0.0
        >>> erfc(10)
        2.08848758376254e-45
    
    :func:`~mpmath.erfc` works accurately even for ludicrously large
    arguments::
    
        >>> erfc(10**10)
        4.3504398860243e-43429448190325182776
    
    Complex arguments are supported::
    
        >>> erfc(500+50j)
        (1.19739830969552e-107492 + 1.46072418957528e-107491j)
    
    """
def erfi(ctx, z):
    ...
def erfinv(ctx, x):
    ...
def expint(ctx, n, z):
    ...
def fresnelc(ctx, z):
    ...
def fresnels(ctx, z):
    ...
def gammainc(ctx, z, a = 0, b = None, regularized = False):
    """
    
    ``gammainc(z, a=0, b=inf)`` computes the (generalized) incomplete
    gamma function with integration limits `[a, b]`:
    
    .. math ::
    
      \\Gamma(z,a,b) = \\int_a^b t^{z-1} e^{-t} \\, dt
    
    The generalized incomplete gamma function reduces to the
    following special cases when one or both endpoints are fixed:
    
    * `\\Gamma(z,0,\\infty)` is the standard ("complete")
      gamma function, `\\Gamma(z)` (available directly
      as the mpmath function :func:`~mpmath.gamma`)
    * `\\Gamma(z,a,\\infty)` is the "upper" incomplete gamma
      function, `\\Gamma(z,a)`
    * `\\Gamma(z,0,b)` is the "lower" incomplete gamma
      function, `\\gamma(z,b)`.
    
    Of course, we have
    `\\Gamma(z,0,x) + \\Gamma(z,x,\\infty) = \\Gamma(z)`
    for all `z` and `x`.
    
    Note however that some authors reverse the order of the
    arguments when defining the lower and upper incomplete
    gamma function, so one should be careful to get the correct
    definition.
    
    If also given the keyword argument ``regularized=True``,
    :func:`~mpmath.gammainc` computes the "regularized" incomplete gamma
    function
    
    .. math ::
    
      P(z,a,b) = \\frac{\\Gamma(z,a,b)}{\\Gamma(z)}.
    
    **Examples**
    
    We can compare with numerical quadrature to verify that
    :func:`~mpmath.gammainc` computes the integral in the definition::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> gammainc(2+3j, 4, 10)
        (0.00977212668627705160602312 - 0.0770637306312989892451977j)
        >>> quad(lambda t: t**(2+3j-1) * exp(-t), [4, 10])
        (0.00977212668627705160602312 - 0.0770637306312989892451977j)
    
    Argument symmetries follow directly from the integral definition::
    
        >>> gammainc(3, 4, 5) + gammainc(3, 5, 4)
        0.0
        >>> gammainc(3,0,2) + gammainc(3,2,4); gammainc(3,0,4)
        1.523793388892911312363331
        1.523793388892911312363331
        >>> findroot(lambda z: gammainc(2,z,3), 1)
        3.0
    
    Evaluation for arbitrarily large arguments::
    
        >>> gammainc(10, 100)
        4.083660630910611272288592e-26
        >>> gammainc(10, 10000000000000000)
        5.290402449901174752972486e-4342944819032375
        >>> gammainc(3+4j, 1000000+1000000j)
        (-1.257913707524362408877881e-434284 + 2.556691003883483531962095e-434284j)
    
    Evaluation of a generalized incomplete gamma function automatically chooses
    the representation that gives a more accurate result, depending on which
    parameter is larger::
    
        >>> gammainc(10000000, 3) - gammainc(10000000, 2)   # Bad
        0.0
        >>> gammainc(10000000, 2, 3)   # Good
        1.755146243738946045873491e+4771204
        >>> gammainc(2, 0, 100000001) - gammainc(2, 0, 100000000)   # Bad
        0.0
        >>> gammainc(2, 100000000, 100000001)   # Good
        4.078258353474186729184421e-43429441
    
    The incomplete gamma functions satisfy simple recurrence
    relations::
    
        >>> mp.dps = 25
        >>> z, a = mpf(3.5), mpf(2)
        >>> gammainc(z+1, a); z*gammainc(z,a) + a**z*exp(-a)
        10.60130296933533459267329
        10.60130296933533459267329
        >>> gammainc(z+1,0,a); z*gammainc(z,0,a) - a**z*exp(-a)
        1.030425427232114336470932
        1.030425427232114336470932
    
    Evaluation at integers and poles::
    
        >>> gammainc(-3, -4, -5)
        (-0.2214577048967798566234192 + 0.0j)
        >>> gammainc(-3, 0, 5)
        +inf
    
    If `z` is an integer, the recurrence reduces the incomplete gamma
    function to `P(a) \\exp(-a) + Q(b) \\exp(-b)` where `P` and
    `Q` are polynomials::
    
        >>> gammainc(1, 2); exp(-2)
        0.1353352832366126918939995
        0.1353352832366126918939995
        >>> mp.dps = 50
        >>> identify(gammainc(6, 1, 2), ['exp(-1)', 'exp(-2)'])
        '(326*exp(-1) + (-872)*exp(-2))'
    
    The incomplete gamma functions reduce to functions such as
    the exponential integral Ei and the error function for special
    arguments::
    
        >>> mp.dps = 25
        >>> gammainc(0, 4); -ei(-4)
        0.00377935240984890647887486
        0.00377935240984890647887486
        >>> gammainc(0.5, 0, 2); sqrt(pi)*erf(sqrt(2))
        1.691806732945198336509541
        1.691806732945198336509541
    
    """
def li(ctx, z, offset = False):
    ...
def ncdf(ctx, x, mu = 0, sigma = 1):
    ...
def npdf(ctx, x, mu = 0, sigma = 1):
    ...
def shi(ctx, z):
    ...
def si(ctx, z):
    """
    
    Computes the sine integral,
    
    .. math ::
    
        \\mathrm{Si}(x) = \\int_0^x \\frac{\\sin t}{t}\\,dt.
    
    The sine integral is thus the antiderivative of the sinc
    function (see :func:`~mpmath.sinc`).
    
    **Examples**
    
    Some values and limits::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> si(0)
        0.0
        >>> si(1)
        0.9460830703671830149413533
        >>> si(-1)
        -0.9460830703671830149413533
        >>> si(pi)
        1.851937051982466170361053
        >>> si(inf)
        1.570796326794896619231322
        >>> si(-inf)
        -1.570796326794896619231322
        >>> si(2+3j)
        (4.547513889562289219853204 + 1.399196580646054789459839j)
    
    The sine integral approaches `\\pi/2` for large real `x`::
    
        >>> si(10**10)
        1.570796326707584656968511
        >>> pi/2
        1.570796326794896619231322
    
    Evaluation is supported for `z` anywhere in the complex plane::
    
        >>> si(10**6*(1+j))
        (-9.75744874290013526417059e+434287 + 4.449410587611035724984376e+434287j)
    
    We can evaluate the defining integral as a reference::
    
        >>> mp.dps = 15
        >>> quad(sinc, [0, 5])
        1.54993124494467
        >>> si(5)
        1.54993124494467
    
    Some infinite series can be evaluated using the
    sine integral::
    
        >>> nsum(lambda k: (-1)**k/(fac(2*k+1)*(2*k+1)), [0,inf])
        0.946083070367183
        >>> si(1)
        0.946083070367183
    
    """
def square_exp_arg(ctx, z, mult = 1, reciprocal = False):
    ...
