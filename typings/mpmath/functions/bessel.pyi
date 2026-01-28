from __future__ import annotations
from mpmath.functions.functions import defun
from mpmath.functions.functions import defun_wrapped
__all__: list[str] = ['airyai', 'airyaizero', 'airybi', 'airybizero', 'angerj', 'bei', 'ber', 'bessel_zero', 'besseli', 'besselj', 'besseljzero', 'besselk', 'bessely', 'besselyzero', 'c_memo', 'coulombc', 'coulombf', 'coulombg', 'defun', 'defun_wrapped', 'find_in_interval', 'generalized_bisection', 'hankel1', 'hankel2', 'hyperu', 'j0', 'j1', 'kei', 'ker', 'lommels1', 'lommels2', 'mcmahon', 'scorergi', 'scorerhi', 'struveh', 'struvel', 'webere', 'whitm', 'whitw']
def _airy_zero(ctx, which, k, derivative, complex = False):
    ...
def _airybi_n2_inf(ctx):
    ...
def _airyderiv_0(ctx, z, n, ntype, which):
    ...
def _anger(ctx, which, v, z, **kwargs):
    ...
def _coulomb_chi(ctx, l, eta, _cache = {}):
    ...
def _scorer(ctx, z, which, kwargs):
    ...
def airyai(ctx, z, derivative = 0, **kwargs):
    """
    
    Computes the Airy function `\\operatorname{Ai}(z)`, which is
    the solution of the Airy differential equation `f''(z) - z f(z) = 0`
    with initial conditions
    
    .. math ::
    
        \\operatorname{Ai}(0) =
            \\frac{1}{3^{2/3}\\Gamma\\left(\\frac{2}{3}\\right)}
    
        \\operatorname{Ai}'(0) =
            -\\frac{1}{3^{1/3}\\Gamma\\left(\\frac{1}{3}\\right)}.
    
    Other common ways of defining the Ai-function include
    integrals such as
    
    .. math ::
    
        \\operatorname{Ai}(x) = \\frac{1}{\\pi}
            \\int_0^{\\infty} \\cos\\left(\\frac{1}{3}t^3+xt\\right) dt
            \\qquad x \\in \\mathbb{R}
    
        \\operatorname{Ai}(z) = \\frac{\\sqrt{3}}{2\\pi}
            \\int_0^{\\infty}
            \\exp\\left(-\\frac{t^3}{3}-\\frac{z^3}{3t^3}\\right) dt.
    
    The Ai-function is an entire function with a turning point,
    behaving roughly like a slowly decaying sine wave for `z < 0` and
    like a rapidly decreasing exponential for `z > 0`.
    A second solution of the Airy differential equation
    is given by `\\operatorname{Bi}(z)` (see :func:`~mpmath.airybi`).
    
    Optionally, with *derivative=alpha*, :func:`airyai` can compute the
    `\\alpha`-th order fractional derivative with respect to `z`.
    For `\\alpha = n = 1,2,3,\\ldots` this gives the derivative
    `\\operatorname{Ai}^{(n)}(z)`, and for `\\alpha = -n = -1,-2,-3,\\ldots`
    this gives the `n`-fold iterated integral
    
    .. math ::
    
        f_0(z) = \\operatorname{Ai}(z)
    
        f_n(z) = \\int_0^z f_{n-1}(t) dt.
    
    The Ai-function has infinitely many zeros, all located along the
    negative half of the real axis. They can be computed with
    :func:`~mpmath.airyaizero`.
    
    **Plots**
    
    .. literalinclude :: /plots/ai.py
    .. image :: /plots/ai.png
    .. literalinclude :: /plots/ai_c.py
    .. image :: /plots/ai_c.png
    
    **Basic examples**
    
    Limits and values include::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> airyai(0); 1/(power(3,'2/3')*gamma('2/3'))
        0.3550280538878172392600632
        0.3550280538878172392600632
        >>> airyai(1)
        0.1352924163128814155241474
        >>> airyai(-1)
        0.5355608832923521187995166
        >>> airyai(inf); airyai(-inf)
        0.0
        0.0
    
    Evaluation is supported for large magnitudes of the argument::
    
        >>> airyai(-100)
        0.1767533932395528780908311
        >>> airyai(100)
        2.634482152088184489550553e-291
        >>> airyai(50+50j)
        (-5.31790195707456404099817e-68 - 1.163588003770709748720107e-67j)
        >>> airyai(-50+50j)
        (1.041242537363167632587245e+158 + 3.347525544923600321838281e+157j)
    
    Huge arguments are also fine::
    
        >>> airyai(10**10)
        1.162235978298741779953693e-289529654602171
        >>> airyai(-10**10)
        0.0001736206448152818510510181
        >>> w = airyai(10**10*(1+j))
        >>> w.real
        5.711508683721355528322567e-186339621747698
        >>> w.imag
        1.867245506962312577848166e-186339621747697
    
    The first root of the Ai-function is::
    
        >>> findroot(airyai, -2)
        -2.338107410459767038489197
        >>> airyaizero(1)
        -2.338107410459767038489197
    
    **Properties and relations**
    
    Verifying the Airy differential equation::
    
        >>> for z in [-3.4, 0, 2.5, 1+2j]:
        ...     chop(airyai(z,2) - z*airyai(z))
        ...
        0.0
        0.0
        0.0
        0.0
    
    The first few terms of the Taylor series expansion around `z = 0`
    (every third term is zero)::
    
        >>> nprint(taylor(airyai, 0, 5))
        [0.355028, -0.258819, 0.0, 0.0591713, -0.0215683, 0.0]
    
    The Airy functions satisfy the Wronskian relation
    `\\operatorname{Ai}(z) \\operatorname{Bi}'(z) -
    \\operatorname{Ai}'(z) \\operatorname{Bi}(z) = 1/\\pi`::
    
        >>> z = -0.5
        >>> airyai(z)*airybi(z,1) - airyai(z,1)*airybi(z)
        0.3183098861837906715377675
        >>> 1/pi
        0.3183098861837906715377675
    
    The Airy functions can be expressed in terms of Bessel
    functions of order `\\pm 1/3`. For `\\Re[z] \\le 0`, we have::
    
        >>> z = -3
        >>> airyai(z)
        -0.3788142936776580743472439
        >>> y = 2*power(-z,'3/2')/3
        >>> (sqrt(-z) * (besselj('1/3',y) + besselj('-1/3',y)))/3
        -0.3788142936776580743472439
    
    **Derivatives and integrals**
    
    Derivatives of the Ai-function (directly and using :func:`~mpmath.diff`)::
    
        >>> airyai(-3,1); diff(airyai,-3)
        0.3145837692165988136507873
        0.3145837692165988136507873
        >>> airyai(-3,2); diff(airyai,-3,2)
        1.136442881032974223041732
        1.136442881032974223041732
        >>> airyai(1000,1); diff(airyai,1000)
        -2.943133917910336090459748e-9156
        -2.943133917910336090459748e-9156
    
    Several derivatives at `z = 0`::
    
        >>> airyai(0,0); airyai(0,1); airyai(0,2)
        0.3550280538878172392600632
        -0.2588194037928067984051836
        0.0
        >>> airyai(0,3); airyai(0,4); airyai(0,5)
        0.3550280538878172392600632
        -0.5176388075856135968103671
        0.0
        >>> airyai(0,15); airyai(0,16); airyai(0,17)
        1292.30211615165475090663
        -3188.655054727379756351861
        0.0
    
    The integral of the Ai-function::
    
        >>> airyai(3,-1); quad(airyai, [0,3])
        0.3299203760070217725002701
        0.3299203760070217725002701
        >>> airyai(-10,-1); quad(airyai, [0,-10])
        -0.765698403134212917425148
        -0.765698403134212917425148
    
    Integrals of high or fractional order::
    
        >>> airyai(-2,0.5); differint(airyai,-2,0.5,0)
        (0.0 + 0.2453596101351438273844725j)
        (0.0 + 0.2453596101351438273844725j)
        >>> airyai(-2,-4); differint(airyai,-2,-4,0)
        0.2939176441636809580339365
        0.2939176441636809580339365
        >>> airyai(0,-1); airyai(0,-2); airyai(0,-3)
        0.0
        0.0
        0.0
    
    Integrals of the Ai-function can be evaluated at limit points::
    
        >>> airyai(-1000000,-1); airyai(-inf,-1)
        -0.6666843728311539978751512
        -0.6666666666666666666666667
        >>> airyai(10,-1); airyai(+inf,-1)
        0.3333333332991690159427932
        0.3333333333333333333333333
        >>> airyai(+inf,-2); airyai(+inf,-3)
        +inf
        +inf
        >>> airyai(-1000000,-2); airyai(-inf,-2)
        666666.4078472650651209742
        +inf
        >>> airyai(-1000000,-3); airyai(-inf,-3)
        -333333074513.7520264995733
        -inf
    
    **References**
    
    1. [DLMF]_ Chapter 9: Airy and Related Functions
    2. [WolframFunctions]_ section: Bessel-Type Functions
    
    """
def airyaizero(ctx, k, derivative = 0):
    """
    
    Gives the `k`-th zero of the Airy Ai-function,
    i.e. the `k`-th number `a_k` ordered by magnitude for which
    `\\operatorname{Ai}(a_k) = 0`.
    
    Optionally, with *derivative=1*, the corresponding
    zero `a'_k` of the derivative function, i.e.
    `\\operatorname{Ai}'(a'_k) = 0`, is computed.
    
    **Examples**
    
    Some values of `a_k`::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> airyaizero(1)
        -2.338107410459767038489197
        >>> airyaizero(2)
        -4.087949444130970616636989
        >>> airyaizero(3)
        -5.520559828095551059129856
        >>> airyaizero(1000)
        -281.0315196125215528353364
    
    Some values of `a'_k`::
    
        >>> airyaizero(1,1)
        -1.018792971647471089017325
        >>> airyaizero(2,1)
        -3.248197582179836537875424
        >>> airyaizero(3,1)
        -4.820099211178735639400616
        >>> airyaizero(1000,1)
        -280.9378080358935070607097
    
    Verification::
    
        >>> chop(airyai(airyaizero(1)))
        0.0
        >>> chop(airyai(airyaizero(1,1),1))
        0.0
    
    """
def airybi(ctx, z, derivative = 0, **kwargs):
    """
    
    Computes the Airy function `\\operatorname{Bi}(z)`, which is
    the solution of the Airy differential equation `f''(z) - z f(z) = 0`
    with initial conditions
    
    .. math ::
    
        \\operatorname{Bi}(0) =
            \\frac{1}{3^{1/6}\\Gamma\\left(\\frac{2}{3}\\right)}
    
        \\operatorname{Bi}'(0) =
            \\frac{3^{1/6}}{\\Gamma\\left(\\frac{1}{3}\\right)}.
    
    Like the Ai-function (see :func:`~mpmath.airyai`), the Bi-function
    is oscillatory for `z < 0`, but it grows rather than decreases
    for `z > 0`.
    
    Optionally, as for :func:`~mpmath.airyai`, derivatives, integrals
    and fractional derivatives can be computed with the *derivative*
    parameter.
    
    The Bi-function has infinitely many zeros along the negative
    half-axis, as well as complex zeros, which can all be computed
    with :func:`~mpmath.airybizero`.
    
    **Plots**
    
    .. literalinclude :: /plots/bi.py
    .. image :: /plots/bi.png
    .. literalinclude :: /plots/bi_c.py
    .. image :: /plots/bi_c.png
    
    **Basic examples**
    
    Limits and values include::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> airybi(0); 1/(power(3,'1/6')*gamma('2/3'))
        0.6149266274460007351509224
        0.6149266274460007351509224
        >>> airybi(1)
        1.207423594952871259436379
        >>> airybi(-1)
        0.10399738949694461188869
        >>> airybi(inf); airybi(-inf)
        +inf
        0.0
    
    Evaluation is supported for large magnitudes of the argument::
    
        >>> airybi(-100)
        0.02427388768016013160566747
        >>> airybi(100)
        6.041223996670201399005265e+288
        >>> airybi(50+50j)
        (-5.322076267321435669290334e+63 + 1.478450291165243789749427e+65j)
        >>> airybi(-50+50j)
        (-3.347525544923600321838281e+157 + 1.041242537363167632587245e+158j)
    
    Huge arguments::
    
        >>> airybi(10**10)
        1.369385787943539818688433e+289529654602165
        >>> airybi(-10**10)
        0.001775656141692932747610973
        >>> w = airybi(10**10*(1+j))
        >>> w.real
        -6.559955931096196875845858e+186339621747689
        >>> w.imag
        -6.822462726981357180929024e+186339621747690
    
    The first real root of the Bi-function is::
    
        >>> findroot(airybi, -1); airybizero(1)
        -1.17371322270912792491998
        -1.17371322270912792491998
    
    **Properties and relations**
    
    Verifying the Airy differential equation::
    
        >>> for z in [-3.4, 0, 2.5, 1+2j]:
        ...     chop(airybi(z,2) - z*airybi(z))
        ...
        0.0
        0.0
        0.0
        0.0
    
    The first few terms of the Taylor series expansion around `z = 0`
    (every third term is zero)::
    
        >>> nprint(taylor(airybi, 0, 5))
        [0.614927, 0.448288, 0.0, 0.102488, 0.0373574, 0.0]
    
    The Airy functions can be expressed in terms of Bessel
    functions of order `\\pm 1/3`. For `\\Re[z] \\le 0`, we have::
    
        >>> z = -3
        >>> airybi(z)
        -0.1982896263749265432206449
        >>> p = 2*power(-z,'3/2')/3
        >>> sqrt(-mpf(z)/3)*(besselj('-1/3',p) - besselj('1/3',p))
        -0.1982896263749265432206449
    
    **Derivatives and integrals**
    
    Derivatives of the Bi-function (directly and using :func:`~mpmath.diff`)::
    
        >>> airybi(-3,1); diff(airybi,-3)
        -0.675611222685258537668032
        -0.675611222685258537668032
        >>> airybi(-3,2); diff(airybi,-3,2)
        0.5948688791247796296619346
        0.5948688791247796296619346
        >>> airybi(1000,1); diff(airybi,1000)
        1.710055114624614989262335e+9156
        1.710055114624614989262335e+9156
    
    Several derivatives at `z = 0`::
    
        >>> airybi(0,0); airybi(0,1); airybi(0,2)
        0.6149266274460007351509224
        0.4482883573538263579148237
        0.0
        >>> airybi(0,3); airybi(0,4); airybi(0,5)
        0.6149266274460007351509224
        0.8965767147076527158296474
        0.0
        >>> airybi(0,15); airybi(0,16); airybi(0,17)
        2238.332923903442675949357
        5522.912562599140729510628
        0.0
    
    The integral of the Bi-function::
    
        >>> airybi(3,-1); quad(airybi, [0,3])
        10.06200303130620056316655
        10.06200303130620056316655
        >>> airybi(-10,-1); quad(airybi, [0,-10])
        -0.01504042480614002045135483
        -0.01504042480614002045135483
    
    Integrals of high or fractional order::
    
        >>> airybi(-2,0.5); differint(airybi, -2, 0.5, 0)
        (0.0 + 0.5019859055341699223453257j)
        (0.0 + 0.5019859055341699223453257j)
        >>> airybi(-2,-4); differint(airybi,-2,-4,0)
        0.2809314599922447252139092
        0.2809314599922447252139092
        >>> airybi(0,-1); airybi(0,-2); airybi(0,-3)
        0.0
        0.0
        0.0
    
    Integrals of the Bi-function can be evaluated at limit points::
    
        >>> airybi(-1000000,-1); airybi(-inf,-1)
        0.000002191261128063434047966873
        0.0
        >>> airybi(10,-1); airybi(+inf,-1)
        147809803.1074067161675853
        +inf
        >>> airybi(+inf,-2); airybi(+inf,-3)
        +inf
        +inf
        >>> airybi(-1000000,-2); airybi(-inf,-2)
        0.4482883750599908479851085
        0.4482883573538263579148237
        >>> gamma('2/3')*power(3,'2/3')/(2*pi)
        0.4482883573538263579148237
        >>> airybi(-100000,-3); airybi(-inf,-3)
        -44828.52827206932872493133
        -inf
        >>> airybi(-100000,-4); airybi(-inf,-4)
        2241411040.437759489540248
        +inf
    
    """
def airybizero(ctx, k, derivative = 0, complex = False):
    """
    
    With *complex=False*, gives the `k`-th real zero of the Airy Bi-function,
    i.e. the `k`-th number `b_k` ordered by magnitude for which
    `\\operatorname{Bi}(b_k) = 0`.
    
    With *complex=True*, gives the `k`-th complex zero in the upper
    half plane `\\beta_k`. Also the conjugate `\\overline{\\beta_k}`
    is a zero.
    
    Optionally, with *derivative=1*, the corresponding
    zero `b'_k` or `\\beta'_k` of the derivative function, i.e.
    `\\operatorname{Bi}'(b'_k) = 0` or `\\operatorname{Bi}'(\\beta'_k) = 0`,
    is computed.
    
    **Examples**
    
    Some values of `b_k`::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> airybizero(1)
        -1.17371322270912792491998
        >>> airybizero(2)
        -3.271093302836352715680228
        >>> airybizero(3)
        -4.830737841662015932667709
        >>> airybizero(1000)
        -280.9378112034152401578834
    
    Some values of `b_k`::
    
        >>> airybizero(1,1)
        -2.294439682614123246622459
        >>> airybizero(2,1)
        -4.073155089071828215552369
        >>> airybizero(3,1)
        -5.512395729663599496259593
        >>> airybizero(1000,1)
        -281.0315164471118527161362
    
    Some values of `\\beta_k`::
    
        >>> airybizero(1,complex=True)
        (0.9775448867316206859469927 + 2.141290706038744575749139j)
        >>> airybizero(2,complex=True)
        (1.896775013895336346627217 + 3.627291764358919410440499j)
        >>> airybizero(3,complex=True)
        (2.633157739354946595708019 + 4.855468179979844983174628j)
        >>> airybizero(1000,complex=True)
        (140.4978560578493018899793 + 243.3907724215792121244867j)
    
    Some values of `\\beta'_k`::
    
        >>> airybizero(1,1,complex=True)
        (0.2149470745374305676088329 + 1.100600143302797880647194j)
        >>> airybizero(2,1,complex=True)
        (1.458168309223507392028211 + 2.912249367458445419235083j)
        >>> airybizero(3,1,complex=True)
        (2.273760763013482299792362 + 4.254528549217097862167015j)
        >>> airybizero(1000,1,complex=True)
        (140.4509972835270559730423 + 243.3096175398562811896208j)
    
    Verification::
    
        >>> chop(airybi(airybizero(1)))
        0.0
        >>> chop(airybi(airybizero(1,1),1))
        0.0
        >>> u = airybizero(1,complex=True)
        >>> chop(airybi(u))
        0.0
        >>> chop(airybi(conj(u)))
        0.0
    
    The complex zeros (in the upper and lower half-planes respectively)
    asymptotically approach the rays `z = R \\exp(\\pm i \\pi /3)`::
    
        >>> arg(airybizero(1,complex=True))
        1.142532510286334022305364
        >>> arg(airybizero(1000,complex=True))
        1.047271114786212061583917
        >>> arg(airybizero(1000000,complex=True))
        1.047197624741816183341355
        >>> pi/3
        1.047197551196597746154214
    
    """
def angerj(ctx, v, z, **kwargs):
    """
    
    Gives the Anger function
    
    .. math ::
    
        \\mathbf{J}_{\\nu}(z) = \\frac{1}{\\pi}
            \\int_0^{\\pi} \\cos(\\nu t - z \\sin t) dt
    
    which is an entire function of both the parameter `\\nu` and
    the argument `z`. It solves the inhomogeneous Bessel differential
    equation
    
    .. math ::
    
        f''(z) + \\frac{1}{z}f'(z) + \\left(1-\\frac{\\nu^2}{z^2}\\right) f(z)
            = \\frac{(z-\\nu)}{\\pi z^2} \\sin(\\pi \\nu).
    
    **Examples**
    
    Evaluation for real and complex parameter and argument::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> angerj(2,3)
        0.4860912605858910769078311
        >>> angerj(-3+4j, 2+5j)
        (-5033.358320403384472395612 + 585.8011892476145118551756j)
        >>> angerj(3.25, 1e6j)
        (4.630743639715893346570743e+434290 - 1.117960409887505906848456e+434291j)
        >>> angerj(-1.5, 1e6)
        0.0002795719747073879393087011
    
    The Anger function coincides with the Bessel J-function when `\\nu`
    is an integer::
    
        >>> angerj(1,3); besselj(1,3)
        0.3390589585259364589255146
        0.3390589585259364589255146
        >>> angerj(1.5,3); besselj(1.5,3)
        0.4088969848691080859328847
        0.4777182150870917715515015
    
    Verifying the differential equation::
    
        >>> v,z = mpf(2.25), 0.75
        >>> f = lambda z: angerj(v,z)
        >>> diff(f,z,2) + diff(f,z)/z + (1-(v/z)**2)*f(z)
        -0.6002108774380707130367995
        >>> (z-v)/(pi*z**2) * sinpi(v)
        -0.6002108774380707130367995
    
    Verifying the integral representation::
    
        >>> angerj(v,z)
        0.1145380759919333180900501
        >>> quad(lambda t: cos(v*t-z*sin(t))/pi, [0,pi])
        0.1145380759919333180900501
    
    **References**
    
    1. [DLMF]_ section 11.10: Anger-Weber Functions
    """
def bei(ctx, n, z, **kwargs):
    """
    
    Computes the Kelvin function bei, which for real arguments gives the
    imaginary part of the Bessel J function of a rotated argument.
    See :func:`~mpmath.ber`.
    """
def ber(ctx, n, z, **kwargs):
    """
    
    Computes the Kelvin function ber, which for real arguments gives the real part
    of the Bessel J function of a rotated argument
    
    .. math ::
    
        J_n\\left(x e^{3\\pi i/4}\\right) = \\mathrm{ber}_n(x) + i \\mathrm{bei}_n(x).
    
    The imaginary part is given by :func:`~mpmath.bei`.
    
    **Plots**
    
    .. literalinclude :: /plots/ber.py
    .. image :: /plots/ber.png
    
    **Examples**
    
    Verifying the defining relation::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> n, x = 2, 3.5
        >>> ber(n,x)
        1.442338852571888752631129
        >>> bei(n,x)
        -0.948359035324558320217678
        >>> besselj(n, x*root(1,8,3))
        (1.442338852571888752631129 - 0.948359035324558320217678j)
    
    The ber and bei functions are also defined by analytic continuation
    for complex arguments::
    
        >>> ber(1+j, 2+3j)
        (4.675445984756614424069563 - 15.84901771719130765656316j)
        >>> bei(1+j, 2+3j)
        (15.83886679193707699364398 + 4.684053288183046528703611j)
    
    """
def bessel_zero(ctx, kind, prime, v, m, isoltol = 0.01, _interval_cache = {}):
    ...
def besseli(ctx, n, z, derivative = 0, **kwargs):
    """
    
    ``besseli(n, x, derivative=0)`` gives the modified Bessel function of the
    first kind,
    
    .. math ::
    
        I_n(x) = i^{-n} J_n(ix).
    
    With *derivative* = `m \\ne 0`, the `m`-th derivative
    
    .. math ::
    
        \\frac{d^m}{dx^m} I_n(x)
    
    is computed.
    
    **Plots**
    
    .. literalinclude :: /plots/besseli.py
    .. image :: /plots/besseli.png
    .. literalinclude :: /plots/besseli_c.py
    .. image :: /plots/besseli_c.png
    
    **Examples**
    
    Some values of `I_n(x)`::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> besseli(0,0)
        1.0
        >>> besseli(1,0)
        0.0
        >>> besseli(0,1)
        1.266065877752008335598245
        >>> besseli(3.5, 2+3j)
        (-0.2904369752642538144289025 - 0.4469098397654815837307006j)
    
    Arguments may be large::
    
        >>> besseli(2, 1000)
        2.480717210191852440616782e+432
        >>> besseli(2, 10**10)
        4.299602851624027900335391e+4342944813
        >>> besseli(2, 6000+10000j)
        (-2.114650753239580827144204e+2603 + 4.385040221241629041351886e+2602j)
    
    For integers `n`, the following integral representation holds::
    
        >>> mp.dps = 15
        >>> n = 3
        >>> x = 2.3
        >>> quad(lambda t: exp(x*cos(t))*cos(n*t), [0,pi])/pi
        0.349223221159309
        >>> besseli(n,x)
        0.349223221159309
    
    Derivatives and antiderivatives of any order can be computed::
    
        >>> mp.dps = 25
        >>> besseli(2, 7.5, 1)
        195.8229038931399062565883
        >>> diff(lambda x: besseli(2,x), 7.5)
        195.8229038931399062565883
        >>> besseli(2, 7.5, 10)
        153.3296508971734525525176
        >>> diff(lambda x: besseli(2,x), 7.5, 10)
        153.3296508971734525525176
        >>> besseli(2,7.5,-1) - besseli(2,3.5,-1)
        202.5043900051930141956876
        >>> quad(lambda x: besseli(2,x), [3.5, 7.5])
        202.5043900051930141956876
    
    """
def besselj(ctx, n, z, derivative = 0, **kwargs):
    """
    
    ``besselj(n, x, derivative=0)`` gives the Bessel function of the first kind
    `J_n(x)`. Bessel functions of the first kind are defined as
    solutions of the differential equation
    
    .. math ::
    
        x^2 y'' + x y' + (x^2 - n^2) y = 0
    
    which appears, among other things, when solving the radial
    part of Laplace's equation in cylindrical coordinates. This
    equation has two solutions for given `n`, where the
    `J_n`-function is the solution that is nonsingular at `x = 0`.
    For positive integer `n`, `J_n(x)` behaves roughly like a sine
    (odd `n`) or cosine (even `n`) multiplied by a magnitude factor
    that decays slowly as `x \\to \\pm\\infty`.
    
    Generally, `J_n` is a special case of the hypergeometric
    function `\\,_0F_1`:
    
    .. math ::
    
        J_n(x) = \\frac{x^n}{2^n \\Gamma(n+1)}
                 \\,_0F_1\\left(n+1,-\\frac{x^2}{4}\\right)
    
    With *derivative* = `m \\ne 0`, the `m`-th derivative
    
    .. math ::
    
        \\frac{d^m}{dx^m} J_n(x)
    
    is computed.
    
    **Plots**
    
    .. literalinclude :: /plots/besselj.py
    .. image :: /plots/besselj.png
    .. literalinclude :: /plots/besselj_c.py
    .. image :: /plots/besselj_c.png
    
    **Examples**
    
    Evaluation is supported for arbitrary arguments, and at
    arbitrary precision::
    
        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = True
        >>> besselj(2, 1000)
        -0.024777229528606
        >>> besselj(4, 0.75)
        0.000801070086542314
        >>> besselj(2, 1000j)
        (-2.48071721019185e+432 + 6.41567059811949e-437j)
        >>> mp.dps = 25
        >>> besselj(0.75j, 3+4j)
        (-2.778118364828153309919653 - 1.5863603889018621585533j)
        >>> mp.dps = 50
        >>> besselj(1, pi)
        0.28461534317975275734531059968613140570981118184947
    
    Arguments may be large::
    
        >>> mp.dps = 25
        >>> besselj(0, 10000)
        -0.007096160353388801477265164
        >>> besselj(0, 10**10)
        0.000002175591750246891726859055
        >>> besselj(2, 10**100)
        7.337048736538615712436929e-51
        >>> besselj(2, 10**5*j)
        (-3.540725411970948860173735e+43426 + 4.4949812409615803110051e-43433j)
    
    The Bessel functions of the first kind satisfy simple
    symmetries around `x = 0`::
    
        >>> mp.dps = 15
        >>> nprint([besselj(n,0) for n in range(5)])
        [1.0, 0.0, 0.0, 0.0, 0.0]
        >>> nprint([besselj(n,pi) for n in range(5)])
        [-0.304242, 0.284615, 0.485434, 0.333458, 0.151425]
        >>> nprint([besselj(n,-pi) for n in range(5)])
        [-0.304242, -0.284615, 0.485434, -0.333458, 0.151425]
    
    Roots of Bessel functions are often used::
    
        >>> nprint([findroot(j0, k) for k in [2, 5, 8, 11, 14]])
        [2.40483, 5.52008, 8.65373, 11.7915, 14.9309]
        >>> nprint([findroot(j1, k) for k in [3, 7, 10, 13, 16]])
        [3.83171, 7.01559, 10.1735, 13.3237, 16.4706]
    
    The roots are not periodic, but the distance between successive
    roots asymptotically approaches `2 \\pi`. Bessel functions of
    the first kind have the following normalization::
    
        >>> quadosc(j0, [0, inf], period=2*pi)
        1.0
        >>> quadosc(j1, [0, inf], period=2*pi)
        1.0
    
    For `n = 1/2` or `n = -1/2`, the Bessel function reduces to a
    trigonometric function::
    
        >>> x = 10
        >>> besselj(0.5, x), sqrt(2/(pi*x))*sin(x)
        (-0.13726373575505, -0.13726373575505)
        >>> besselj(-0.5, x), sqrt(2/(pi*x))*cos(x)
        (-0.211708866331398, -0.211708866331398)
    
    Derivatives of any order can be computed (negative orders
    correspond to integration)::
    
        >>> mp.dps = 25
        >>> besselj(0, 7.5, 1)
        -0.1352484275797055051822405
        >>> diff(lambda x: besselj(0,x), 7.5)
        -0.1352484275797055051822405
        >>> besselj(0, 7.5, 10)
        -0.1377811164763244890135677
        >>> diff(lambda x: besselj(0,x), 7.5, 10)
        -0.1377811164763244890135677
        >>> besselj(0,7.5,-1) - besselj(0,3.5,-1)
        -0.1241343240399987693521378
        >>> quad(j0, [3.5, 7.5])
        -0.1241343240399987693521378
    
    Differentiation with a noninteger order gives the fractional derivative
    in the sense of the Riemann-Liouville differintegral, as computed by
    :func:`~mpmath.differint`::
    
        >>> mp.dps = 15
        >>> besselj(1, 3.5, 0.75)
        -0.385977722939384
        >>> differint(lambda x: besselj(1, x), 3.5, 0.75)
        -0.385977722939384
    
    """
def besseljzero(ctx, v, m, derivative = 0):
    """
    
    For a real order `\\nu \\ge 0` and a positive integer `m`, returns
    `j_{\\nu,m}`, the `m`-th positive zero of the Bessel function of the
    first kind `J_{\\nu}(z)` (see :func:`~mpmath.besselj`). Alternatively,
    with *derivative=1*, gives the first nonnegative simple zero
    `j'_{\\nu,m}` of `J'_{\\nu}(z)`.
    
    The indexing convention is that used by Abramowitz & Stegun
    and the DLMF. Note the special case `j'_{0,1} = 0`, while all other
    zeros are positive. In effect, only simple zeros are counted
    (all zeros of Bessel functions are simple except possibly `z = 0`)
    and `j_{\\nu,m}` becomes a monotonic function of both `\\nu`
    and `m`.
    
    The zeros are interlaced according to the inequalities
    
    .. math ::
    
        j'_{\\nu,k} < j_{\\nu,k} < j'_{\\nu,k+1}
    
        j_{\\nu,1} < j_{\\nu+1,2} < j_{\\nu,2} < j_{\\nu+1,2} < j_{\\nu,3} < \\cdots
    
    **Examples**
    
    Initial zeros of the Bessel functions `J_0(z), J_1(z), J_2(z)`::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> besseljzero(0,1); besseljzero(0,2); besseljzero(0,3)
        2.404825557695772768621632
        5.520078110286310649596604
        8.653727912911012216954199
        >>> besseljzero(1,1); besseljzero(1,2); besseljzero(1,3)
        3.831705970207512315614436
        7.01558666981561875353705
        10.17346813506272207718571
        >>> besseljzero(2,1); besseljzero(2,2); besseljzero(2,3)
        5.135622301840682556301402
        8.417244140399864857783614
        11.61984117214905942709415
    
    Initial zeros of `J'_0(z), J'_1(z), J'_2(z)`::
    
        0.0
        3.831705970207512315614436
        7.01558666981561875353705
        >>> besseljzero(1,1,1); besseljzero(1,2,1); besseljzero(1,3,1)
        1.84118378134065930264363
        5.331442773525032636884016
        8.536316366346285834358961
        >>> besseljzero(2,1,1); besseljzero(2,2,1); besseljzero(2,3,1)
        3.054236928227140322755932
        6.706133194158459146634394
        9.969467823087595793179143
    
    Zeros with large index::
    
        >>> besseljzero(0,100); besseljzero(0,1000); besseljzero(0,10000)
        313.3742660775278447196902
        3140.807295225078628895545
        31415.14114171350798533666
        >>> besseljzero(5,100); besseljzero(5,1000); besseljzero(5,10000)
        321.1893195676003157339222
        3148.657306813047523500494
        31422.9947255486291798943
        >>> besseljzero(0,100,1); besseljzero(0,1000,1); besseljzero(0,10000,1)
        311.8018681873704508125112
        3139.236339643802482833973
        31413.57032947022399485808
    
    Zeros of functions with large order::
    
        >>> besseljzero(50,1)
        57.11689916011917411936228
        >>> besseljzero(50,2)
        62.80769876483536093435393
        >>> besseljzero(50,100)
        388.6936600656058834640981
        >>> besseljzero(50,1,1)
        52.99764038731665010944037
        >>> besseljzero(50,2,1)
        60.02631933279942589882363
        >>> besseljzero(50,100,1)
        387.1083151608726181086283
    
    Zeros of functions with fractional order::
    
        >>> besseljzero(0.5,1); besseljzero(1.5,1); besseljzero(2.25,4)
        3.141592653589793238462643
        4.493409457909064175307881
        15.15657692957458622921634
    
    Both `J_{\\nu}(z)` and `J'_{\\nu}(z)` can be expressed as infinite
    products over their zeros::
    
        >>> v,z = 2, mpf(1)
        >>> (z/2)**v/gamma(v+1) * \\
        ...     nprod(lambda k: 1-(z/besseljzero(v,k))**2, [1,inf])
        ...
        0.1149034849319004804696469
        >>> besselj(v,z)
        0.1149034849319004804696469
        >>> (z/2)**(v-1)/2/gamma(v) * \\
        ...     nprod(lambda k: 1-(z/besseljzero(v,k,1))**2, [1,inf])
        ...
        0.2102436158811325550203884
        >>> besselj(v,z,1)
        0.2102436158811325550203884
    
    """
def besselk(ctx, n, z, **kwargs):
    ...
def bessely(ctx, n, z, derivative = 0, **kwargs):
    ...
def besselyzero(ctx, v, m, derivative = 0):
    """
    
    For a real order `\\nu \\ge 0` and a positive integer `m`, returns
    `y_{\\nu,m}`, the `m`-th positive zero of the Bessel function of the
    second kind `Y_{\\nu}(z)` (see :func:`~mpmath.bessely`). Alternatively,
    with *derivative=1*, gives the first positive zero `y'_{\\nu,m}` of
    `Y'_{\\nu}(z)`.
    
    The zeros are interlaced according to the inequalities
    
    .. math ::
    
        y_{\\nu,k} < y'_{\\nu,k} < y_{\\nu,k+1}
    
        y_{\\nu,1} < y_{\\nu+1,2} < y_{\\nu,2} < y_{\\nu+1,2} < y_{\\nu,3} < \\cdots
    
    **Examples**
    
    Initial zeros of the Bessel functions `Y_0(z), Y_1(z), Y_2(z)`::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> besselyzero(0,1); besselyzero(0,2); besselyzero(0,3)
        0.8935769662791675215848871
        3.957678419314857868375677
        7.086051060301772697623625
        >>> besselyzero(1,1); besselyzero(1,2); besselyzero(1,3)
        2.197141326031017035149034
        5.429681040794135132772005
        8.596005868331168926429606
        >>> besselyzero(2,1); besselyzero(2,2); besselyzero(2,3)
        3.384241767149593472701426
        6.793807513268267538291167
        10.02347797936003797850539
    
    Initial zeros of `Y'_0(z), Y'_1(z), Y'_2(z)`::
    
        >>> besselyzero(0,1,1); besselyzero(0,2,1); besselyzero(0,3,1)
        2.197141326031017035149034
        5.429681040794135132772005
        8.596005868331168926429606
        >>> besselyzero(1,1,1); besselyzero(1,2,1); besselyzero(1,3,1)
        3.683022856585177699898967
        6.941499953654175655751944
        10.12340465543661307978775
        >>> besselyzero(2,1,1); besselyzero(2,2,1); besselyzero(2,3,1)
        5.002582931446063945200176
        8.350724701413079526349714
        11.57419546521764654624265
    
    Zeros with large index::
    
        >>> besselyzero(0,100); besselyzero(0,1000); besselyzero(0,10000)
        311.8034717601871549333419
        3139.236498918198006794026
        31413.57034538691205229188
        >>> besselyzero(5,100); besselyzero(5,1000); besselyzero(5,10000)
        319.6183338562782156235062
        3147.086508524556404473186
        31421.42392920214673402828
        >>> besselyzero(0,100,1); besselyzero(0,1000,1); besselyzero(0,10000,1)
        313.3726705426359345050449
        3140.807136030340213610065
        31415.14112579761578220175
    
    Zeros of functions with large order::
    
        >>> besselyzero(50,1)
        53.50285882040036394680237
        >>> besselyzero(50,2)
        60.11244442774058114686022
        >>> besselyzero(50,100)
        387.1096509824943957706835
        >>> besselyzero(50,1,1)
        56.96290427516751320063605
        >>> besselyzero(50,2,1)
        62.74888166945933944036623
        >>> besselyzero(50,100,1)
        388.6923300548309258355475
    
    Zeros of functions with fractional order::
    
        >>> besselyzero(0.5,1); besselyzero(1.5,1); besselyzero(2.25,4)
        1.570796326794896619231322
        2.798386045783887136720249
        13.56721208770735123376018
    
    """
def c_memo(f):
    ...
def coulombc(ctx, l, eta, _cache = {}):
    ...
def coulombf(ctx, l, eta, z, w = 1, chop = True, **kwargs):
    ...
def coulombg(ctx, l, eta, z, w = 1, chop = True, **kwargs):
    ...
def find_in_interval(ctx, f, ab):
    ...
def generalized_bisection(ctx, f, a, b, n):
    """
    
    Given f known to have exactly n simple roots within [a,b],
    return a list of n intervals isolating the roots
    and having opposite signs at the endpoints.
    
    TODO: this can be optimized, e.g. by reusing evaluation points.
    """
def hankel1(ctx, n, x, **kwargs):
    ...
def hankel2(ctx, n, x, **kwargs):
    ...
def hyperu(ctx, a, b, z, **kwargs):
    """
    
    Gives the Tricomi confluent hypergeometric function `U`, also known as
    the Kummer or confluent hypergeometric function of the second kind. This
    function gives a second linearly independent solution to the confluent
    hypergeometric differential equation (the first is provided by `\\,_1F_1`  --
    see :func:`~mpmath.hyp1f1`).
    
    **Examples**
    
    Evaluation for arbitrary complex arguments::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> hyperu(2,3,4)
        0.0625
        >>> hyperu(0.25, 5, 1000)
        0.1779949416140579573763523
        >>> hyperu(0.25, 5, -1000)
        (0.1256256609322773150118907 - 0.1256256609322773150118907j)
    
    The `U` function may be singular at `z = 0`::
    
        >>> hyperu(1.5, 2, 0)
        +inf
        >>> hyperu(1.5, -2, 0)
        0.1719434921288400112603671
    
    Verifying the differential equation::
    
        >>> a, b = 1.5, 2
        >>> f = lambda z: hyperu(a,b,z)
        >>> for z in [-10, 3, 3+4j]:
        ...     chop(z*diff(f,z,2) + (b-z)*diff(f,z) - a*f(z))
        ...
        0.0
        0.0
        0.0
    
    An integral representation::
    
        >>> a,b,z = 2, 3.5, 4.25
        >>> hyperu(a,b,z)
        0.06674960718150520648014567
        >>> quad(lambda t: exp(-z*t)*t**(a-1)*(1+t)**(b-a-1),[0,inf]) / gamma(a)
        0.06674960718150520648014567
    
    
    [1] http://people.math.sfu.ca/~cbm/aands/page_504.htm
    """
def j0(ctx, x):
    """
    Computes the Bessel function `J_0(x)`. See :func:`~mpmath.besselj`.
    """
def j1(ctx, x):
    """
    Computes the Bessel function `J_1(x)`.  See :func:`~mpmath.besselj`.
    """
def kei(ctx, n, z, **kwargs):
    """
    
    Computes the Kelvin function kei, which for real arguments gives the
    imaginary part of the (rescaled) Bessel K function of a rotated argument.
    See :func:`~mpmath.ker`.
    """
def ker(ctx, n, z, **kwargs):
    """
    
    Computes the Kelvin function ker, which for real arguments gives the real part
    of the (rescaled) Bessel K function of a rotated argument
    
    .. math ::
    
        e^{-\\pi i/2} K_n\\left(x e^{3\\pi i/4}\\right) = \\mathrm{ker}_n(x) + i \\mathrm{kei}_n(x).
    
    The imaginary part is given by :func:`~mpmath.kei`.
    
    **Plots**
    
    .. literalinclude :: /plots/ker.py
    .. image :: /plots/ker.png
    
    **Examples**
    
    Verifying the defining relation::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> n, x = 2, 4.5
        >>> ker(n,x)
        0.02542895201906369640249801
        >>> kei(n,x)
        -0.02074960467222823237055351
        >>> exp(-n*pi*j/2) * besselk(n, x*root(1,8,1))
        (0.02542895201906369640249801 - 0.02074960467222823237055351j)
    
    The ker and kei functions are also defined by analytic continuation
    for complex arguments::
    
        >>> ker(1+j, 3+4j)
        (1.586084268115490421090533 - 2.939717517906339193598719j)
        >>> kei(1+j, 3+4j)
        (-2.940403256319453402690132 - 1.585621643835618941044855j)
    
    """
def lommels1(ctx, u, v, z, **kwargs):
    """
    
    Gives the Lommel function `s_{\\mu,\\nu}` or `s^{(1)}_{\\mu,\\nu}`
    
    .. math ::
    
        s_{\\mu,\\nu}(z) = \\frac{z^{\\mu+1}}{(\\mu-\\nu+1)(\\mu+\\nu+1)}
            \\,_1F_2\\left(1; \\frac{\\mu-\\nu+3}{2}, \\frac{\\mu+\\nu+3}{2};
            -\\frac{z^2}{4} \\right)
    
    which solves the inhomogeneous Bessel equation
    
    .. math ::
    
        z^2 f''(z) + z f'(z) + (z^2-\\nu^2) f(z) = z^{\\mu+1}.
    
    A second solution is given by :func:`~mpmath.lommels2`.
    
    **Plots**
    
    .. literalinclude :: /plots/lommels1.py
    .. image :: /plots/lommels1.png
    
    **Examples**
    
    An integral representation::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> u,v,z = 0.25, 0.125, mpf(0.75)
        >>> lommels1(u,v,z)
        0.4276243877565150372999126
        >>> (bessely(v,z)*quad(lambda t: t**u*besselj(v,t), [0,z]) - \\
        ...  besselj(v,z)*quad(lambda t: t**u*bessely(v,t), [0,z]))*(pi/2)
        0.4276243877565150372999126
    
    A special value::
    
        >>> lommels1(v,v,z)
        0.5461221367746048054932553
        >>> gamma(v+0.5)*sqrt(pi)*power(2,v-1)*struveh(v,z)
        0.5461221367746048054932553
    
    Verifying the differential equation::
    
        >>> f = lambda z: lommels1(u,v,z)
        >>> z**2*diff(f,z,2) + z*diff(f,z) + (z**2-v**2)*f(z)
        0.6979536443265746992059141
        >>> z**(u+1)
        0.6979536443265746992059141
    
    **References**
    
    1. [GradshteynRyzhik]_
    2. [Weisstein]_ http://mathworld.wolfram.com/LommelFunction.html
    """
def lommels2(ctx, u, v, z, **kwargs):
    """
    
    Gives the second Lommel function `S_{\\mu,\\nu}` or `s^{(2)}_{\\mu,\\nu}`
    
    .. math ::
    
        S_{\\mu,\\nu}(z) = s_{\\mu,\\nu}(z) + 2^{\\mu-1}
            \\Gamma\\left(\\tfrac{1}{2}(\\mu-\\nu+1)\\right)
            \\Gamma\\left(\\tfrac{1}{2}(\\mu+\\nu+1)\\right) \\times
    
            \\left[\\sin(\\tfrac{1}{2}(\\mu-\\nu)\\pi) J_{\\nu}(z) -
                  \\cos(\\tfrac{1}{2}(\\mu-\\nu)\\pi) Y_{\\nu}(z)
            \\right]
    
    which solves the same differential equation as
    :func:`~mpmath.lommels1`.
    
    **Plots**
    
    .. literalinclude :: /plots/lommels2.py
    .. image :: /plots/lommels2.png
    
    **Examples**
    
    For large `|z|`, `S_{\\mu,\\nu} \\sim z^{\\mu-1}`::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> lommels2(10,2,30000)
        1.968299831601008419949804e+40
        >>> power(30000,9)
        1.9683e+40
    
    A special value::
    
        >>> u,v,z = 0.5, 0.125, mpf(0.75)
        >>> lommels2(v,v,z)
        0.9589683199624672099969765
        >>> (struveh(v,z)-bessely(v,z))*power(2,v-1)*sqrt(pi)*gamma(v+0.5)
        0.9589683199624672099969765
    
    Verifying the differential equation::
    
        >>> f = lambda z: lommels2(u,v,z)
        >>> z**2*diff(f,z,2) + z*diff(f,z) + (z**2-v**2)*f(z)
        0.6495190528383289850727924
        >>> z**(u+1)
        0.6495190528383289850727924
    
    **References**
    
    1. [GradshteynRyzhik]_
    2. [Weisstein]_ http://mathworld.wolfram.com/LommelFunction.html
    """
def mcmahon(ctx, kind, prime, v, m):
    """
    
    Computes an estimate for the location of the Bessel function zero
    j_{v,m}, y_{v,m}, j'_{v,m} or y'_{v,m} using McMahon's asymptotic
    expansion (Abramowitz & Stegun 9.5.12-13, DLMF 20.21(vi)).
    
    Returns (r,err) where r is the estimated location of the root
    and err is a positive number estimating the error of the
    asymptotic expansion.
    """
def scorergi(ctx, z, **kwargs):
    """
    
    Evaluates the Scorer function
    
    .. math ::
    
        \\operatorname{Gi}(z) =
        \\operatorname{Ai}(z) \\int_0^z \\operatorname{Bi}(t) dt +
        \\operatorname{Bi}(z) \\int_z^{\\infty} \\operatorname{Ai}(t) dt
    
    which gives a particular solution to the inhomogeneous Airy
    differential equation `f''(z) - z f(z) = 1/\\pi`. Another
    particular solution is given by the Scorer Hi-function
    (:func:`~mpmath.scorerhi`). The two functions are related as
    `\\operatorname{Gi}(z) + \\operatorname{Hi}(z) = \\operatorname{Bi}(z)`.
    
    **Plots**
    
    .. literalinclude :: /plots/gi.py
    .. image :: /plots/gi.png
    .. literalinclude :: /plots/gi_c.py
    .. image :: /plots/gi_c.png
    
    **Examples**
    
    Some values and limits::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> scorergi(0); 1/(power(3,'7/6')*gamma('2/3'))
        0.2049755424820002450503075
        0.2049755424820002450503075
        >>> diff(scorergi, 0); 1/(power(3,'5/6')*gamma('1/3'))
        0.1494294524512754526382746
        0.1494294524512754526382746
        >>> scorergi(+inf); scorergi(-inf)
        0.0
        0.0
        >>> scorergi(1)
        0.2352184398104379375986902
        >>> scorergi(-1)
        -0.1166722172960152826494198
    
    Evaluation for large arguments::
    
        >>> scorergi(10)
        0.03189600510067958798062034
        >>> scorergi(100)
        0.003183105228162961476590531
        >>> scorergi(1000000)
        0.0000003183098861837906721743873
        >>> 1/(pi*1000000)
        0.0000003183098861837906715377675
        >>> scorergi(-1000)
        -0.08358288400262780392338014
        >>> scorergi(-100000)
        0.02886866118619660226809581
        >>> scorergi(50+10j)
        (0.0061214102799778578790984 - 0.001224335676457532180747917j)
        >>> scorergi(-50-10j)
        (5.236047850352252236372551e+29 - 3.08254224233701381482228e+29j)
        >>> scorergi(100000j)
        (-8.806659285336231052679025e+6474077 + 8.684731303500835514850962e+6474077j)
    
    Verifying the connection between Gi and Hi::
    
        >>> z = 0.25
        >>> scorergi(z) + scorerhi(z)
        0.7287469039362150078694543
        >>> airybi(z)
        0.7287469039362150078694543
    
    Verifying the differential equation::
    
        >>> for z in [-3.4, 0, 2.5, 1+2j]:
        ...     chop(diff(scorergi,z,2) - z*scorergi(z))
        ...
        -0.3183098861837906715377675
        -0.3183098861837906715377675
        -0.3183098861837906715377675
        -0.3183098861837906715377675
    
    Verifying the integral representation::
    
        >>> z = 0.5
        >>> scorergi(z)
        0.2447210432765581976910539
        >>> Ai,Bi = airyai,airybi
        >>> Bi(z)*(Ai(inf,-1)-Ai(z,-1)) + Ai(z)*(Bi(z,-1)-Bi(0,-1))
        0.2447210432765581976910539
    
    **References**
    
    1. [DLMF]_ section 9.12: Scorer Functions
    
    """
def scorerhi(ctx, z, **kwargs):
    """
    
    Evaluates the second Scorer function
    
    .. math ::
    
        \\operatorname{Hi}(z) =
        \\operatorname{Bi}(z) \\int_{-\\infty}^z \\operatorname{Ai}(t) dt -
        \\operatorname{Ai}(z) \\int_{-\\infty}^z \\operatorname{Bi}(t) dt
    
    which gives a particular solution to the inhomogeneous Airy
    differential equation `f''(z) - z f(z) = 1/\\pi`. See also
    :func:`~mpmath.scorergi`.
    
    **Plots**
    
    .. literalinclude :: /plots/hi.py
    .. image :: /plots/hi.png
    .. literalinclude :: /plots/hi_c.py
    .. image :: /plots/hi_c.png
    
    **Examples**
    
    Some values and limits::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> scorerhi(0); 2/(power(3,'7/6')*gamma('2/3'))
        0.4099510849640004901006149
        0.4099510849640004901006149
        >>> diff(scorerhi,0); 2/(power(3,'5/6')*gamma('1/3'))
        0.2988589049025509052765491
        0.2988589049025509052765491
        >>> scorerhi(+inf); scorerhi(-inf)
        +inf
        0.0
        >>> scorerhi(1)
        0.9722051551424333218376886
        >>> scorerhi(-1)
        0.2206696067929598945381098
    
    Evaluation for large arguments::
    
        >>> scorerhi(10)
        455641153.5163291358991077
        >>> scorerhi(100)
        6.041223996670201399005265e+288
        >>> scorerhi(1000000)
        7.138269638197858094311122e+289529652
        >>> scorerhi(-10)
        0.0317685352825022727415011
        >>> scorerhi(-100)
        0.003183092495767499864680483
        >>> scorerhi(100j)
        (-6.366197716545672122983857e-9 + 0.003183098861710582761688475j)
        >>> scorerhi(50+50j)
        (-5.322076267321435669290334e+63 + 1.478450291165243789749427e+65j)
        >>> scorerhi(-1000-1000j)
        (0.0001591549432510502796565538 - 0.000159154943091895334973109j)
    
    Verifying the differential equation::
    
        >>> for z in [-3.4, 0, 2, 1+2j]:
        ...     chop(diff(scorerhi,z,2) - z*scorerhi(z))
        ...
        0.3183098861837906715377675
        0.3183098861837906715377675
        0.3183098861837906715377675
        0.3183098861837906715377675
    
    Verifying the integral representation::
    
        >>> z = 0.5
        >>> scorerhi(z)
        0.6095559998265972956089949
        >>> Ai,Bi = airyai,airybi
        >>> Bi(z)*(Ai(z,-1)-Ai(-inf,-1)) - Ai(z)*(Bi(z,-1)-Bi(-inf,-1))
        0.6095559998265972956089949
    
    """
def struveh(ctx, n, z, **kwargs):
    """
    
    Gives the Struve function
    
    .. math ::
    
        \\,\\mathbf{H}_n(z) =
        \\sum_{k=0}^\\infty \\frac{(-1)^k}{\\Gamma(k+\\frac{3}{2})
            \\Gamma(k+n+\\frac{3}{2})} {\\left({\\frac{z}{2}}\\right)}^{2k+n+1}
    
    which is a solution to the Struve differential equation
    
    .. math ::
    
        z^2 f''(z) + z f'(z) + (z^2-n^2) f(z) = \\frac{2 z^{n+1}}{\\pi (2n-1)!!}.
    
    **Examples**
    
    Evaluation for arbitrary real and complex arguments::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> struveh(0, 3.5)
        0.3608207733778295024977797
        >>> struveh(-1, 10)
        -0.255212719726956768034732
        >>> struveh(1, -100.5)
        0.5819566816797362287502246
        >>> struveh(2.5, 10000000000000)
        3153915652525200060.308937
        >>> struveh(2.5, -10000000000000)
        (0.0 - 3153915652525200060.308937j)
        >>> struveh(1+j, 1000000+4000000j)
        (-3.066421087689197632388731e+1737173 - 1.596619701076529803290973e+1737173j)
    
    A Struve function of half-integer order is elementary; for example:
    
        >>> z = 3
        >>> struveh(0.5, 3)
        0.9167076867564138178671595
        >>> sqrt(2/(pi*z))*(1-cos(z))
        0.9167076867564138178671595
    
    Numerically verifying the differential equation::
    
        >>> z = mpf(4.5)
        >>> n = 3
        >>> f = lambda z: struveh(n,z)
        >>> lhs = z**2*diff(f,z,2) + z*diff(f,z) + (z**2-n**2)*f(z)
        >>> rhs = 2*z**(n+1)/fac2(2*n-1)/pi
        >>> lhs
        17.40359302709875496632744
        >>> rhs
        17.40359302709875496632744
    
    """
def struvel(ctx, n, z, **kwargs):
    """
    
    Gives the modified Struve function
    
    .. math ::
    
        \\,\\mathbf{L}_n(z) = -i e^{-n\\pi i/2} \\mathbf{H}_n(i z)
    
    which solves to the modified Struve differential equation
    
    .. math ::
    
        z^2 f''(z) + z f'(z) - (z^2+n^2) f(z) = \\frac{2 z^{n+1}}{\\pi (2n-1)!!}.
    
    **Examples**
    
    Evaluation for arbitrary real and complex arguments::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> struvel(0, 3.5)
        7.180846515103737996249972
        >>> struvel(-1, 10)
        2670.994904980850550721511
        >>> struvel(1, -100.5)
        1.757089288053346261497686e+42
        >>> struvel(2.5, 10000000000000)
        4.160893281017115450519948e+4342944819025
        >>> struvel(2.5, -10000000000000)
        (0.0 - 4.160893281017115450519948e+4342944819025j)
        >>> struvel(1+j, 700j)
        (-0.1721150049480079451246076 + 0.1240770953126831093464055j)
        >>> struvel(1+j, 1000000+4000000j)
        (-2.973341637511505389128708e+434290 - 5.164633059729968297147448e+434290j)
    
    Numerically verifying the differential equation::
    
        >>> z = mpf(3.5)
        >>> n = 3
        >>> f = lambda z: struvel(n,z)
        >>> lhs = z**2*diff(f,z,2) + z*diff(f,z) - (z**2+n**2)*f(z)
        >>> rhs = 2*z**(n+1)/fac2(2*n-1)/pi
        >>> lhs
        6.368850306060678353018165
        >>> rhs
        6.368850306060678353018165
    """
def webere(ctx, v, z, **kwargs):
    """
    
    Gives the Weber function
    
    .. math ::
    
        \\mathbf{E}_{\\nu}(z) = \\frac{1}{\\pi}
            \\int_0^{\\pi} \\sin(\\nu t - z \\sin t) dt
    
    which is an entire function of both the parameter `\\nu` and
    the argument `z`. It solves the inhomogeneous Bessel differential
    equation
    
    .. math ::
    
        f''(z) + \\frac{1}{z}f'(z) + \\left(1-\\frac{\\nu^2}{z^2}\\right) f(z)
            = -\\frac{1}{\\pi z^2} (z+\\nu+(z-\\nu)\\cos(\\pi \\nu)).
    
    **Examples**
    
    Evaluation for real and complex parameter and argument::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> webere(2,3)
        -0.1057668973099018425662646
        >>> webere(-3+4j, 2+5j)
        (-585.8081418209852019290498 - 5033.314488899926921597203j)
        >>> webere(3.25, 1e6j)
        (-1.117960409887505906848456e+434291 - 4.630743639715893346570743e+434290j)
        >>> webere(3.25, 1e6)
        -0.00002812518265894315604914453
    
    Up to addition of a rational function of `z`, the Weber function coincides
    with the Struve H-function when `\\nu` is an integer::
    
        >>> webere(1,3); 2/pi-struveh(1,3)
        -0.3834897968188690177372881
        -0.3834897968188690177372881
        >>> webere(5,3); 26/(35*pi)-struveh(5,3)
        0.2009680659308154011878075
        0.2009680659308154011878075
    
    Verifying the differential equation::
    
        >>> v,z = mpf(2.25), 0.75
        >>> f = lambda z: webere(v,z)
        >>> diff(f,z,2) + diff(f,z)/z + (1-(v/z)**2)*f(z)
        -1.097441848875479535164627
        >>> -(z+v+(z-v)*cospi(v))/(pi*z**2)
        -1.097441848875479535164627
    
    Verifying the integral representation::
    
        >>> webere(v,z)
        0.1486507351534283744485421
        >>> quad(lambda t: sin(v*t-z*sin(t))/pi, [0,pi])
        0.1486507351534283744485421
    
    **References**
    
    1. [DLMF]_ section 11.10: Anger-Weber Functions
    """
def whitm(ctx, k, m, z, **kwargs):
    ...
def whitw(ctx, k, m, z, **kwargs):
    ...
