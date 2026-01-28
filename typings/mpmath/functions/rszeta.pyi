"""

---------------------------------------------------------------------
.. sectionauthor:: Juan Arias de Reyna <arias@us.es>

This module implements zeta-related functions using the Riemann-Siegel
expansion: zeta_offline(s,k=0)

* coef(J, eps): Need in the computation of Rzeta(s,k)

* Rzeta_simul(s, der=0) computes Rzeta^(k)(s) and Rzeta^(k)(1-s) simultaneously
  for  0 <= k <= der. Used by zeta_offline and z_offline

* Rzeta_set(s, derivatives) computes Rzeta^(k)(s) for given derivatives, used by
  z_half(t,k) and zeta_half

* z_offline(w,k): Z(w) and its derivatives of order k <= 4
* z_half(t,k): Z(t) (Riemann Siegel function) and its derivatives of order k <= 4
* zeta_offline(s): zeta(s) and its derivatives of order k<= 4
* zeta_half(1/2+it,k):  zeta(s)  and its derivatives of order k<= 4

* rs_zeta(s,k=0) Computes zeta^(k)(s)   Unifies zeta_half and zeta_offline
* rs_z(w,k=0)    Computes Z^(k)(w)      Unifies z_offline and z_half
----------------------------------------------------------------------

This program uses Riemann-Siegel expansion even to compute
zeta(s) on points s = sigma + i t  with sigma arbitrary not
necessarily equal to 1/2.

It is founded on a new deduction of the formula, with rigorous
and sharp bounds for the  terms and rest of this expansion.

More information on the papers:

 J. Arias de Reyna, High Precision Computation of Riemann's
 Zeta Function by the Riemann-Siegel Formula I, II

 We refer to them as I, II.

 In them we shall find detailed explanation of all the
 procedure.

The program uses Riemann-Siegel expansion.
This  is useful when t is big, ( say  t > 10000 ).
The precision is limited, roughly it can compute zeta(sigma+it)
with an error less than exp(-c t) for some constant c depending
on sigma.  The program gives an error when the Riemann-Siegel
formula can not compute to the wanted precision.

"""
from __future__ import annotations
import math as math
from mpmath.functions.functions import defun
__all__: list[str] = ['RSCache', 'Rzeta_set', 'Rzeta_simul', 'aux_J_needed', 'aux_M_Fp', 'coef', 'defun', 'math', 'rs_z', 'rs_zeta', 'z_half', 'z_offline', 'zeta_half', 'zeta_offline']
class RSCache:
    @staticmethod
    def __init__(ctx):
        ...
def Rzeta_set(ctx, s, derivatives = [0]):
    """
    
    Computes several derivatives of the auxiliary function of Riemann `R(s)`.
    
    **Definition**
    
    The function is defined by
    
    .. math ::
    
        \\begin{equation}
        {\\mathop{\\mathcal R }\\nolimits}(s)=
        \\int_{0\\swarrow1}\\frac{x^{-s} e^{\\pi i x^2}}{e^{\\pi i x}-
        e^{-\\pi i x}}\\,dx
        \\end{equation}
    
    To this function we apply the Riemann-Siegel expansion.
    """
def Rzeta_simul(ctx, s, der = 0):
    ...
def _coef(ctx, J, eps):
    """
    
    Computes the coefficients  `c_n`  for `0\\le n\\le 2J` with error less than eps
    
    **Definition**
    
    The coefficients c_n are defined by
    
    .. math ::
    
        \\begin{equation}
        F(z)=\\frac{e^{\\pi i
        \\bigl(\\frac{z^2}{2}+\\frac38\\bigr)}-i\\sqrt{2}\\cos\\frac{\\pi}{2}z}{2\\cos\\pi
        z}=\\sum_{n=0}^\\infty c_{2n} z^{2n}
        \\end{equation}
    
    they are computed applying the relation
    
    .. math ::
    
        \\begin{multline}
        c_{2n}=-\\frac{i}{\\sqrt{2}}\\Bigl(\\frac{\\pi}{2}\\Bigr)^{2n}
        \\sum_{k=0}^n\\frac{(-1)^k}{(2k)!}
        2^{2n-2k}\\frac{(-1)^{n-k}E_{2n-2k}}{(2n-2k)!}+\\\\
        +e^{3\\pi i/8}\\sum_{j=0}^n(-1)^j\\frac{
        E_{2j}}{(2j)!}\\frac{i^{n-j}\\pi^{n+j}}{(n-j)!2^{n-j+1}}.
        \\end{multline}
    """
def aux_J_needed(ctx, xA, xeps4, a, xB1, xM):
    ...
def aux_M_Fp(ctx, xA, xeps4, a, xB1, xL):
    ...
def coef(ctx, J, eps):
    ...
def rs_z(ctx, w, derivative = 0):
    ...
def rs_zeta(ctx, s, derivative = 0, **kwargs):
    ...
def z_half(ctx, t, der = 0):
    """
    
    z_half(t,der=0) Computes Z^(der)(t)
    """
def z_offline(ctx, w, k = 0):
    """
    
    Computes Z(w) and its derivatives off the line
    """
def zeta_half(ctx, s, k = 0):
    """
    
    zeta_half(s,k=0) Computes zeta^(k)(s) when Re s = 0.5
    """
def zeta_offline(ctx, s, k = 0):
    """
    
    Computes zeta^(k)(s) off the line
    """
