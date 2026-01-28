from __future__ import annotations
from mpmath.functions.functions import defun
from mpmath.functions.functions import defun_wrapped
__all__: list[str] = ['chebyt', 'chebyu', 'defun', 'defun_wrapped', 'gegenbauer', 'hermite', 'jacobi', 'laguerre', 'legendre', 'legenp', 'legenq', 'pcfd', 'pcfu', 'pcfv', 'pcfw', 'spherharm']
def _hermite_param(ctx, n, z, parabolic_cylinder):
    """
    
    Combined calculation of the Hermite polynomial H_n(z) (and its
    generalization to complex n) and the parabolic cylinder
    function D.
    """
def chebyt(ctx, n, x, **kwargs):
    ...
def chebyu(ctx, n, x, **kwargs):
    ...
def gegenbauer(ctx, n, a, z, **kwargs):
    ...
def hermite(ctx, n, z, **kwargs):
    """
    
    Evaluates the Hermite polynomial `H_n(z)`, which may be defined using
    the recurrence
    
    .. math ::
    
        H_0(z) = 1
    
        H_1(z) = 2z
    
        H_{n+1} = 2z H_n(z) - 2n H_{n-1}(z).
    
    The Hermite polynomials are orthogonal on `(-\\infty, \\infty)` with
    respect to the weight `e^{-z^2}`. More generally, allowing arbitrary complex
    values of `n`, the Hermite function `H_n(z)` is defined as
    
    .. math ::
    
        H_n(z) = (2z)^n \\,_2F_0\\left(-\\frac{n}{2}, \\frac{1-n}{2},
            -\\frac{1}{z^2}\\right)
    
    for `\\Re{z} > 0`, or generally
    
    .. math ::
    
        H_n(z) = 2^n \\sqrt{\\pi} \\left(
            \\frac{1}{\\Gamma\\left(\\frac{1-n}{2}\\right)}
            \\,_1F_1\\left(-\\frac{n}{2}, \\frac{1}{2}, z^2\\right) -
            \\frac{2z}{\\Gamma\\left(-\\frac{n}{2}\\right)}
            \\,_1F_1\\left(\\frac{1-n}{2}, \\frac{3}{2}, z^2\\right)
        \\right).
    
    **Plots**
    
    .. literalinclude :: /plots/hermite.py
    .. image :: /plots/hermite.png
    
    **Examples**
    
    Evaluation for arbitrary arguments::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> hermite(0, 10)
        1.0
        >>> hermite(1, 10); hermite(2, 10)
        20.0
        398.0
        >>> hermite(10000, 2)
        4.950440066552087387515653e+19334
        >>> hermite(3, -10**8)
        -7999999999999998800000000.0
        >>> hermite(-3, -10**8)
        1.675159751729877682920301e+4342944819032534
        >>> hermite(2+3j, -1+2j)
        (-0.07652130602993513389421901 - 0.1084662449961914580276007j)
    
    Coefficients of the first few Hermite polynomials are::
    
        >>> for n in range(7):
        ...     chop(taylor(lambda z: hermite(n, z), 0, n))
        ...
        [1.0]
        [0.0, 2.0]
        [-2.0, 0.0, 4.0]
        [0.0, -12.0, 0.0, 8.0]
        [12.0, 0.0, -48.0, 0.0, 16.0]
        [0.0, 120.0, 0.0, -160.0, 0.0, 32.0]
        [-120.0, 0.0, 720.0, 0.0, -480.0, 0.0, 64.0]
    
    Values at `z = 0`::
    
        >>> for n in range(-5, 9):
        ...     hermite(n, 0)
        ...
        0.02769459142039868792653387
        0.08333333333333333333333333
        0.2215567313631895034122709
        0.5
        0.8862269254527580136490837
        1.0
        0.0
        -2.0
        0.0
        12.0
        0.0
        -120.0
        0.0
        1680.0
    
    Hermite functions satisfy the differential equation::
    
        >>> n = 4
        >>> f = lambda z: hermite(n, z)
        >>> z = 1.5
        >>> chop(diff(f,z,2) - 2*z*diff(f,z) + 2*n*f(z))
        0.0
    
    Verifying orthogonality::
    
        >>> chop(quad(lambda t: hermite(2,t)*hermite(4,t)*exp(-t**2), [-inf,inf]))
        0.0
    
    """
def jacobi(ctx, n, a, b, x, **kwargs):
    ...
def laguerre(ctx, n, a, z, **kwargs):
    ...
def legendre(ctx, n, x, **kwargs):
    ...
def legenp(ctx, n, m, z, type = 2, **kwargs):
    """
    
    Calculates the (associated) Legendre function of the first kind of
    degree *n* and order *m*, `P_n^m(z)`. Taking `m = 0` gives the ordinary
    Legendre function of the first kind, `P_n(z)`. The parameters may be
    complex numbers.
    
    In terms of the Gauss hypergeometric function, the (associated) Legendre
    function is defined as
    
    .. math ::
    
        P_n^m(z) = \\frac{1}{\\Gamma(1-m)} \\frac{(1+z)^{m/2}}{(1-z)^{m/2}}
            \\,_2F_1\\left(-n, n+1, 1-m, \\frac{1-z}{2}\\right).
    
    With *type=3* instead of *type=2*, the alternative
    definition
    
    .. math ::
    
        \\hat{P}_n^m(z) = \\frac{1}{\\Gamma(1-m)} \\frac{(z+1)^{m/2}}{(z-1)^{m/2}}
            \\,_2F_1\\left(-n, n+1, 1-m, \\frac{1-z}{2}\\right).
    
    is used. These functions correspond respectively to ``LegendreP[n,m,2,z]``
    and ``LegendreP[n,m,3,z]`` in Mathematica.
    
    The general solution of the (associated) Legendre differential equation
    
    .. math ::
    
        (1-z^2) f''(z) - 2zf'(z) + \\left(n(n+1)-\\frac{m^2}{1-z^2}\\right)f(z) = 0
    
    is given by `C_1 P_n^m(z) + C_2 Q_n^m(z)` for arbitrary constants
    `C_1`, `C_2`, where `Q_n^m(z)` is a Legendre function of the
    second kind as implemented by :func:`~mpmath.legenq`.
    
    **Examples**
    
    Evaluation for arbitrary parameters and arguments::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> legenp(2, 0, 10); legendre(2, 10)
        149.5
        149.5
        >>> legenp(-2, 0.5, 2.5)
        (1.972260393822275434196053 - 1.972260393822275434196053j)
        >>> legenp(2+3j, 1-j, -0.5+4j)
        (-3.335677248386698208736542 - 5.663270217461022307645625j)
        >>> chop(legenp(3, 2, -1.5, type=2))
        28.125
        >>> chop(legenp(3, 2, -1.5, type=3))
        -28.125
    
    Verifying the associated Legendre differential equation::
    
        >>> n, m = 2, -0.5
        >>> C1, C2 = 1, -3
        >>> f = lambda z: C1*legenp(n,m,z) + C2*legenq(n,m,z)
        >>> deq = lambda z: (1-z**2)*diff(f,z,2) - 2*z*diff(f,z) + \\
        ...     (n*(n+1)-m**2/(1-z**2))*f(z)
        >>> for z in [0, 2, -1.5, 0.5+2j]:
        ...     chop(deq(mpmathify(z)))
        ...
        0.0
        0.0
        0.0
        0.0
    """
def legenq(ctx, n, m, z, type = 2, **kwargs):
    """
    
    Calculates the (associated) Legendre function of the second kind of
    degree *n* and order *m*, `Q_n^m(z)`. Taking `m = 0` gives the ordinary
    Legendre function of the second kind, `Q_n(z)`. The parameters may be
    complex numbers.
    
    The Legendre functions of the second kind give a second set of
    solutions to the (associated) Legendre differential equation.
    (See :func:`~mpmath.legenp`.)
    Unlike the Legendre functions of the first kind, they are not
    polynomials of `z` for integer `n`, `m` but rational or logarithmic
    functions with poles at `z = \\pm 1`.
    
    There are various ways to define Legendre functions of
    the second kind, giving rise to different complex structure.
    A version can be selected using the *type* keyword argument.
    The *type=2* and *type=3* functions are given respectively by
    
    .. math ::
    
        Q_n^m(z) = \\frac{\\pi}{2 \\sin(\\pi m)}
            \\left( \\cos(\\pi m) P_n^m(z) -
            \\frac{\\Gamma(1+m+n)}{\\Gamma(1-m+n)} P_n^{-m}(z)\\right)
    
        \\hat{Q}_n^m(z) = \\frac{\\pi}{2 \\sin(\\pi m)} e^{\\pi i m}
            \\left( \\hat{P}_n^m(z) -
            \\frac{\\Gamma(1+m+n)}{\\Gamma(1-m+n)} \\hat{P}_n^{-m}(z)\\right)
    
    where `P` and `\\hat{P}` are the *type=2* and *type=3* Legendre functions
    of the first kind. The formulas above should be understood as limits
    when `m` is an integer.
    
    These functions correspond to ``LegendreQ[n,m,2,z]`` (or ``LegendreQ[n,m,z]``)
    and ``LegendreQ[n,m,3,z]`` in Mathematica. The *type=3* function
    is essentially the same as the function defined in
    Abramowitz & Stegun (eq. 8.1.3) but with `(z+1)^{m/2}(z-1)^{m/2}` instead
    of `(z^2-1)^{m/2}`, giving slightly different branches.
    
    **Examples**
    
    Evaluation for arbitrary parameters and arguments::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> legenq(2, 0, 0.5)
        -0.8186632680417568557122028
        >>> legenq(-1.5, -2, 2.5)
        (0.6655964618250228714288277 + 0.3937692045497259717762649j)
        >>> legenq(2-j, 3+4j, -6+5j)
        (-10001.95256487468541686564 - 6011.691337610097577791134j)
    
    Different versions of the function::
    
        >>> legenq(2, 1, 0.5)
        0.7298060598018049369381857
        >>> legenq(2, 1, 1.5)
        (-7.902916572420817192300921 + 0.1998650072605976600724502j)
        >>> legenq(2, 1, 0.5, type=3)
        (2.040524284763495081918338 - 0.7298060598018049369381857j)
        >>> chop(legenq(2, 1, 1.5, type=3))
        -0.1998650072605976600724502
    
    """
def pcfd(ctx, n, z, **kwargs):
    """
    
    Gives the parabolic cylinder function in Whittaker's notation
    `D_n(z) = U(-n-1/2, z)` (see :func:`~mpmath.pcfu`).
    It solves the differential equation
    
    .. math ::
    
        y'' + \\left(n + \\frac{1}{2} - \\frac{1}{4} z^2\\right) y = 0.
    
    and can be represented in terms of Hermite polynomials
    (see :func:`~mpmath.hermite`) as
    
    .. math ::
    
        D_n(z) = 2^{-n/2} e^{-z^2/4} H_n\\left(\\frac{z}{\\sqrt{2}}\\right).
    
    **Plots**
    
    .. literalinclude :: /plots/pcfd.py
    .. image :: /plots/pcfd.png
    
    **Examples**
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> pcfd(0,0); pcfd(1,0); pcfd(2,0); pcfd(3,0)
        1.0
        0.0
        -1.0
        0.0
        >>> pcfd(4,0); pcfd(-3,0)
        3.0
        0.6266570686577501256039413
        >>> pcfd('1/2', 2+3j)
        (-5.363331161232920734849056 - 3.858877821790010714163487j)
        >>> pcfd(2, -10)
        1.374906442631438038871515e-9
    
    Verifying the differential equation::
    
        >>> n = mpf(2.5)
        >>> y = lambda z: pcfd(n,z)
        >>> z = 1.75
        >>> chop(diff(y,z,2) + (n+0.5-0.25*z**2)*y(z))
        0.0
    
    Rational Taylor series expansion when `n` is an integer::
    
        >>> taylor(lambda z: pcfd(5,z), 0, 7)
        [0.0, 15.0, 0.0, -13.75, 0.0, 3.96875, 0.0, -0.6015625]
    
    """
def pcfu(ctx, a, z, **kwargs):
    """
    
    Gives the parabolic cylinder function `U(a,z)`, which may be
    defined for `\\Re(z) > 0` in terms of the confluent
    U-function (see :func:`~mpmath.hyperu`) by
    
    .. math ::
    
        U(a,z) = 2^{-\\frac{1}{4}-\\frac{a}{2}} e^{-\\frac{1}{4} z^2}
            U\\left(\\frac{a}{2}+\\frac{1}{4},
            \\frac{1}{2}, \\frac{1}{2}z^2\\right)
    
    or, for arbitrary `z`,
    
    .. math ::
    
        e^{-\\frac{1}{4}z^2} U(a,z) =
            U(a,0) \\,_1F_1\\left(-\\tfrac{a}{2}+\\tfrac{1}{4};
            \\tfrac{1}{2}; -\\tfrac{1}{2}z^2\\right) +
            U'(a,0) z \\,_1F_1\\left(-\\tfrac{a}{2}+\\tfrac{3}{4};
            \\tfrac{3}{2}; -\\tfrac{1}{2}z^2\\right).
    
    **Examples**
    
    Connection to other functions::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> z = mpf(3)
        >>> pcfu(0.5,z)
        0.03210358129311151450551963
        >>> sqrt(pi/2)*exp(z**2/4)*erfc(z/sqrt(2))
        0.03210358129311151450551963
        >>> pcfu(0.5,-z)
        23.75012332835297233711255
        >>> sqrt(pi/2)*exp(z**2/4)*erfc(-z/sqrt(2))
        23.75012332835297233711255
        >>> pcfu(0.5,-z)
        23.75012332835297233711255
        >>> sqrt(pi/2)*exp(z**2/4)*erfc(-z/sqrt(2))
        23.75012332835297233711255
    
    """
def pcfv(ctx, a, z, **kwargs):
    """
    
    Gives the parabolic cylinder function `V(a,z)`, which can be
    represented in terms of :func:`~mpmath.pcfu` as
    
    .. math ::
    
        V(a,z) = \\frac{\\Gamma(a+\\tfrac{1}{2}) (U(a,-z)-\\sin(\\pi a) U(a,z)}{\\pi}.
    
    **Examples**
    
    Wronskian relation between `U` and `V`::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> a, z = 2, 3
        >>> pcfu(a,z)*diff(pcfv,(a,z),(0,1))-diff(pcfu,(a,z),(0,1))*pcfv(a,z)
        0.7978845608028653558798921
        >>> sqrt(2/pi)
        0.7978845608028653558798921
        >>> a, z = 2.5, 3
        >>> pcfu(a,z)*diff(pcfv,(a,z),(0,1))-diff(pcfu,(a,z),(0,1))*pcfv(a,z)
        0.7978845608028653558798921
        >>> a, z = 0.25, -1
        >>> pcfu(a,z)*diff(pcfv,(a,z),(0,1))-diff(pcfu,(a,z),(0,1))*pcfv(a,z)
        0.7978845608028653558798921
        >>> a, z = 2+1j, 2+3j
        >>> chop(pcfu(a,z)*diff(pcfv,(a,z),(0,1))-diff(pcfu,(a,z),(0,1))*pcfv(a,z))
        0.7978845608028653558798921
    
    """
def pcfw(ctx, a, z, **kwargs):
    """
    
    Gives the parabolic cylinder function `W(a,z)` defined in (DLMF 12.14).
    
    **Examples**
    
    Value at the origin::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> a = mpf(0.25)
        >>> pcfw(a,0)
        0.9722833245718180765617104
        >>> power(2,-0.75)*sqrt(abs(gamma(0.25+0.5j*a)/gamma(0.75+0.5j*a)))
        0.9722833245718180765617104
        >>> diff(pcfw,(a,0),(0,1))
        -0.5142533944210078966003624
        >>> -power(2,-0.25)*sqrt(abs(gamma(0.75+0.5j*a)/gamma(0.25+0.5j*a)))
        -0.5142533944210078966003624
    
    """
def spherharm(ctx, l, m, theta, phi, **kwargs):
    """
    
    Evaluates the spherical harmonic `Y_l^m(\\theta,\\phi)`,
    
    .. math ::
    
        Y_l^m(\\theta,\\phi) = \\sqrt{\\frac{2l+1}{4\\pi}\\frac{(l-m)!}{(l+m)!}}
            P_l^m(\\cos \\theta) e^{i m \\phi}
    
    where `P_l^m` is an associated Legendre function (see :func:`~mpmath.legenp`).
    
    Here `\\theta \\in [0, \\pi]` denotes the polar coordinate (ranging
    from the north pole to the south pole) and `\\phi \\in [0, 2 \\pi]` denotes the
    azimuthal coordinate on a sphere. Care should be used since many different
    conventions for spherical coordinate variables are used.
    
    Usually spherical harmonics are considered for `l \\in \\mathbb{N}`,
    `m \\in \\mathbb{Z}`, `|m| \\le l`. More generally, `l,m,\\theta,\\phi`
    are permitted to be complex numbers.
    
    .. note ::
    
        :func:`~mpmath.spherharm` returns a complex number, even if the value is
        purely real.
    
    **Plots**
    
    .. literalinclude :: /plots/spherharm40.py
    
    `Y_{4,0}`:
    
    .. image :: /plots/spherharm40.png
    
    `Y_{4,1}`:
    
    .. image :: /plots/spherharm41.png
    
    `Y_{4,2}`:
    
    .. image :: /plots/spherharm42.png
    
    `Y_{4,3}`:
    
    .. image :: /plots/spherharm43.png
    
    `Y_{4,4}`:
    
    .. image :: /plots/spherharm44.png
    
    **Examples**
    
    Some low-order spherical harmonics with reference values::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> theta = pi/4
        >>> phi = pi/3
        >>> spherharm(0,0,theta,phi); 0.5*sqrt(1/pi)*expj(0)
        (0.2820947917738781434740397 + 0.0j)
        (0.2820947917738781434740397 + 0.0j)
        >>> spherharm(1,-1,theta,phi); 0.5*sqrt(3/(2*pi))*expj(-phi)*sin(theta)
        (0.1221506279757299803965962 - 0.2115710938304086076055298j)
        (0.1221506279757299803965962 - 0.2115710938304086076055298j)
        >>> spherharm(1,0,theta,phi); 0.5*sqrt(3/pi)*cos(theta)*expj(0)
        (0.3454941494713354792652446 + 0.0j)
        (0.3454941494713354792652446 + 0.0j)
        >>> spherharm(1,1,theta,phi); -0.5*sqrt(3/(2*pi))*expj(phi)*sin(theta)
        (-0.1221506279757299803965962 - 0.2115710938304086076055298j)
        (-0.1221506279757299803965962 - 0.2115710938304086076055298j)
    
    With the normalization convention used, the spherical harmonics are orthonormal
    on the unit sphere::
    
        >>> sphere = [0,pi], [0,2*pi]
        >>> dS = lambda t,p: fp.sin(t)   # differential element
        >>> Y1 = lambda t,p: fp.spherharm(l1,m1,t,p)
        >>> Y2 = lambda t,p: fp.conj(fp.spherharm(l2,m2,t,p))
        >>> l1 = l2 = 3; m1 = m2 = 2
        >>> fp.chop(fp.quad(lambda t,p: Y1(t,p)*Y2(t,p)*dS(t,p), *sphere))
        1.0000000000000007
        >>> m2 = 1    # m1 != m2
        >>> print(fp.chop(fp.quad(lambda t,p: Y1(t,p)*Y2(t,p)*dS(t,p), *sphere)))
        0.0
    
    Evaluation is accurate for large orders::
    
        >>> spherharm(1000,750,0.5,0.25)
        (3.776445785304252879026585e-102 - 5.82441278771834794493484e-102j)
    
    Evaluation works with complex parameter values::
    
        >>> spherharm(1+j, 2j, 2+3j, -0.5j)
        (64.44922331113759992154992 + 1981.693919841408089681743j)
    """
