from __future__ import annotations
from mpmath.functions.functions import defun
from mpmath.functions.functions import defun_wrapped
__all__: list[str] = ['defun', 'defun_wrapped', 'jtheta']
def _djacobi_theta2(ctx, z, q, nd):
    ...
def _djacobi_theta2a(ctx, z, q, nd):
    """
    
    case ctx._im(z) != 0
    dtheta(2, z, q, nd) =
    j* q**1/4 * Sum(q**(n*n + n) * (2*n+1)*exp(j*(2*n + 1)*z), n=-inf, inf)
    max term for (2*n0+1)*log(q).real - 2* ctx._im(z) ~= 0
    n0 = int(ctx._im(z)/log(q).real - 1/2)
    """
def _djacobi_theta3(ctx, z, q, nd):
    """
    nd=1,2,3 order of the derivative with respect to z
    """
def _djacobi_theta3a(ctx, z, q, nd):
    """
    
    case ctx._im(z) != 0
    djtheta3(z, q, nd) = (2*j)**nd *
      Sum(q**(n*n) * n**nd * exp(j*2*n*z), n, -inf, inf)
    max term for minimum n*abs(log(q).real) + ctx._im(z)
    """
def _djtheta(ctx, n, z, q, derivative = 1):
    ...
def _jacobi_theta2(ctx, z, q):
    ...
def _jacobi_theta2a(ctx, z, q):
    """
    
    case ctx._im(z) != 0
    theta(2, z, q) =
    q**1/4 * Sum(q**(n*n + n) * exp(j*(2*n + 1)*z), n=-inf, inf)
    max term for minimum (2*n+1)*log(q).real - 2* ctx._im(z)
    n0 = int(ctx._im(z)/log(q).real - 1/2)
    theta(2, z, q) =
    q**1/4 * Sum(q**(n*n + n) * exp(j*(2*n + 1)*z), n=n0, inf) +
    q**1/4 * Sum(q**(n*n + n) * exp(j*(2*n + 1)*z), n, n0-1, -inf)
    """
def _jacobi_theta3(ctx, z, q):
    ...
def _jacobi_theta3a(ctx, z, q):
    """
    
    case ctx._im(z) != 0
    theta3(z, q) = Sum(q**(n*n) * exp(j*2*n*z), n, -inf, inf)
    max term for n*abs(log(q).real) + ctx._im(z) ~= 0
    n0 = int(- ctx._im(z)/abs(log(q).real))
    """
def jtheta(ctx, n, z, q, derivative = 0):
    """
    
    Computes the Jacobi theta function `\\vartheta_n(z, q)`, where
    `n = 1, 2, 3, 4`, defined by the infinite series:
    
    .. math ::
    
      \\vartheta_1(z,q) = 2 q^{1/4} \\sum_{n=0}^{\\infty}
        (-1)^n q^{n^2+n\\,} \\sin((2n+1)z)
    
      \\vartheta_2(z,q) = 2 q^{1/4} \\sum_{n=0}^{\\infty}
        q^{n^{2\\,} + n} \\cos((2n+1)z)
    
      \\vartheta_3(z,q) = 1 + 2 \\sum_{n=1}^{\\infty}
        q^{n^2\\,} \\cos(2 n z)
    
      \\vartheta_4(z,q) = 1 + 2 \\sum_{n=1}^{\\infty}
        (-q)^{n^2\\,} \\cos(2 n z)
    
    The theta functions are functions of two variables:
    
    * `z` is the *argument*, an arbitrary real or complex number
    
    * `q` is the *nome*, which must be a real or complex number
      in the unit disk (i.e. `|q| < 1`). For `|q| \\ll 1`, the
      series converge very quickly, so the Jacobi theta functions
      can efficiently be evaluated to high precision.
    
    The compact notations `\\vartheta_n(q) = \\vartheta_n(0,q)`
    and `\\vartheta_n = \\vartheta_n(0,q)` are also frequently
    encountered. Finally, Jacobi theta functions are frequently
    considered as functions of the half-period ratio `\\tau`
    and then usually denoted by `\\vartheta_n(z|\\tau)`.
    
    Optionally, ``jtheta(n, z, q, derivative=d)`` with `d > 0` computes
    a `d`-th derivative with respect to `z`.
    
    **Examples and basic properties**
    
    Considered as functions of `z`, the Jacobi theta functions may be
    viewed as generalizations of the ordinary trigonometric functions
    cos and sin. They are periodic functions::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> jtheta(1, 0.25, '0.2')
        0.2945120798627300045053104
        >>> jtheta(1, 0.25 + 2*pi, '0.2')
        0.2945120798627300045053104
    
    Indeed, the series defining the theta functions are essentially
    trigonometric Fourier series. The coefficients can be retrieved
    using :func:`~mpmath.fourier`::
    
        >>> mp.dps = 10
        >>> nprint(fourier(lambda x: jtheta(2, x, 0.5), [-pi, pi], 4))
        ([0.0, 1.68179, 0.0, 0.420448, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0])
    
    The Jacobi theta functions are also so-called quasiperiodic
    functions of `z` and `\\tau`, meaning that for fixed `\\tau`,
    `\\vartheta_n(z, q)` and `\\vartheta_n(z+\\pi \\tau, q)` are the same
    except for an exponential factor::
    
        >>> mp.dps = 25
        >>> tau = 3*j/10
        >>> q = exp(pi*j*tau)
        >>> z = 10
        >>> jtheta(4, z+tau*pi, q)
        (-0.682420280786034687520568 + 1.526683999721399103332021j)
        >>> -exp(-2*j*z)/q * jtheta(4, z, q)
        (-0.682420280786034687520568 + 1.526683999721399103332021j)
    
    The Jacobi theta functions satisfy a huge number of other
    functional equations, such as the following identity (valid for
    any `q`)::
    
        >>> q = mpf(3)/10
        >>> jtheta(3,0,q)**4
        6.823744089352763305137427
        >>> jtheta(2,0,q)**4 + jtheta(4,0,q)**4
        6.823744089352763305137427
    
    Extensive listings of identities satisfied by the Jacobi theta
    functions can be found in standard reference works.
    
    The Jacobi theta functions are related to the gamma function
    for special arguments::
    
        >>> jtheta(3, 0, exp(-pi))
        1.086434811213308014575316
        >>> pi**(1/4.) / gamma(3/4.)
        1.086434811213308014575316
    
    :func:`~mpmath.jtheta` supports arbitrary precision evaluation and complex
    arguments::
    
        >>> mp.dps = 50
        >>> jtheta(4, sqrt(2), 0.5)
        2.0549510717571539127004115835148878097035750653737
        >>> mp.dps = 25
        >>> jtheta(4, 1+2j, (1+j)/5)
        (7.180331760146805926356634 - 1.634292858119162417301683j)
    
    Evaluation of derivatives::
    
        >>> mp.dps = 25
        >>> jtheta(1, 7, 0.25, 1); diff(lambda z: jtheta(1, z, 0.25), 7)
        1.209857192844475388637236
        1.209857192844475388637236
        >>> jtheta(1, 7, 0.25, 2); diff(lambda z: jtheta(1, z, 0.25), 7, 2)
        -0.2598718791650217206533052
        -0.2598718791650217206533052
        >>> jtheta(2, 7, 0.25, 1); diff(lambda z: jtheta(2, z, 0.25), 7)
        -1.150231437070259644461474
        -1.150231437070259644461474
        >>> jtheta(2, 7, 0.25, 2); diff(lambda z: jtheta(2, z, 0.25), 7, 2)
        -0.6226636990043777445898114
        -0.6226636990043777445898114
        >>> jtheta(3, 7, 0.25, 1); diff(lambda z: jtheta(3, z, 0.25), 7)
        -0.9990312046096634316587882
        -0.9990312046096634316587882
        >>> jtheta(3, 7, 0.25, 2); diff(lambda z: jtheta(3, z, 0.25), 7, 2)
        -0.1530388693066334936151174
        -0.1530388693066334936151174
        >>> jtheta(4, 7, 0.25, 1); diff(lambda z: jtheta(4, z, 0.25), 7)
        0.9820995967262793943571139
        0.9820995967262793943571139
        >>> jtheta(4, 7, 0.25, 2); diff(lambda z: jtheta(4, z, 0.25), 7, 2)
        0.3936902850291437081667755
        0.3936902850291437081667755
    
    **Possible issues**
    
    For `|q| \\ge 1` or `\\Im(\\tau) \\le 0`, :func:`~mpmath.jtheta` raises
    ``ValueError``. This exception is also raised for `|q|` extremely
    close to 1 (or equivalently `\\tau` very close to 0), since the
    series would converge too slowly::
    
        >>> jtheta(1, 10, 0.99999999 * exp(0.5*j))
        Traceback (most recent call last):
          ...
        ValueError: abs(q) > THETA_Q_LIM = 1.000000
    
    """
